Attribute VB_Name = "Module1"


Sub StockDataMODERATE()
    Dim ws As Worksheet
    For Each ws In Worksheets
    
    ws.Activate
    
    Cells(1, 9).Value = "Ticker"
    Cells(1, 10).Value = "Yearly Change"
    Cells(1, 11).Value = "Percent Change"
    Cells(1, 12).Value = "Total Stock Volume"

    Dim Column As Integer
    Column = 1
    
    Dim Summary_Table_Row As Integer
    Summary_Table_Row = 2
    
    Dim TickerSymbol As String
    
    Dim TotalVol As Double
    TotalVol = 0
    
    Dim OpeningPrice As Double
    
    
    Dim ClosingPrice As Double
      
    Dim YearChange As Double
    
    Dim PercentChange As Double
        
    LastRow = ws.Cells(Rows.Count, 1).End(xlUp).Row
    
    OpeningPrice = Cells(2, 3).Value
    
    
        For i = 2 To LastRow

          
            If Cells(i + 1, Column).Value <> Cells(i, Column).Value Then
            
            TickerSymbol = Cells(i, Column).Value
            Range("I" & Summary_Table_Row).Value = TickerSymbol
            
            ClosingPrice = Cells(i, 6).Value
            
            
            YearChange = ClosingPrice - OpeningPrice
                If OpeningPrice > 0 Then
                PercentChange = ClosingPrice / OpeningPrice - 1
                End If
                
                            
            OpeningPrice = Cells(i + 1, 3).Value
            
            
            Range("J" & Summary_Table_Row).Value = YearChange
                 If Range("J" & Summary_Table_Row).Value > 0 Then
                    Range("J" & Summary_Table_Row).Interior.ColorIndex = 4
                    Else: Range("J" & Summary_Table_Row).Interior.ColorIndex = 3
                 End If
            Range("K" & Summary_Table_Row).Value = PercentChange
            Range("K" & Summary_Table_Row).NumberFormat = "0.00%"
    
 
            
            
            TotalVol = TotalVol + Cells(i, 7).Value
            Range("L" & Summary_Table_Row).Value = TotalVol
            
            Summary_Table_Row = Summary_Table_Row + 1
            
            TotalVol = 0
        
        
            Else:
            
            TotalVol = TotalVol + Cells(i, 7).Value
        
            End If
        
        Next i
        
           
        Next ws


End Sub

