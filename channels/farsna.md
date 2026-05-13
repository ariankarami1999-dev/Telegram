<div dir="rtl" align="right">

<style>
.tg-channel-box {
  max-width: 800px;
  margin: 0 auto;
  padding: 16px;
  font-family: system-ui, -apple-system, 'Segoe UI', 'Vazirmatn', Tahoma, sans-serif;
  background: #fafafa;
  border-radius: 20px;
  line-height: 1.7;
}

/* حالت دارک برای کسانی که تم دارک دارن */
@media (prefers-color-scheme: dark) {
  .tg-channel-box {
    background: #1a1a2e;
    color: #eee;
  }
  .tg-post {
    background: #16213e;
    border-color: #0f3460;
  }
  .tg-post-header {
    background: #0f3460;
  }
  .tg-footer {
    color: #aaa;
  }
  .tg-text a {
    color: #7eb6ff;
  }
}

/* کارت پست */
.tg-post {
  background: white;
  border-radius: 20px;
  padding: 18px 22px;
  margin: 20px 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  border: 1px solid #e5e7eb;
  transition: box-shadow 0.2s;
}
.tg-post:hover {
  box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}
.tg-post-header {
  background: #f3f4f6;
  margin: -18px -22px 16px -22px;
  padding: 10px 22px;
  border-radius: 20px 20px 0 0;
  font-size: 13px;
  color: #4b5563;
  border-bottom: 1px solid #e5e7eb;
}

/* نقل قول / فوروارد */
.tg-forward {
  background: #eef2ff;
  border-right: 4px solid #3b82f6;
  padding: 8px 14px;
  border-radius: 12px;
  margin: 12px 0;
  font-size: 13px;
  color: #1e40af;
}

/* متن */
.tg-text {
  font-size: 16px;
  margin: 14px 0;
}
.tg-text a {
  color: #2563eb;
  text-decoration: none;
}
.tg-text a:hover {
  text-decoration: underline;
}

/* تصاویر */
.tg-photo {
  margin: 12px 0;
  text-align: center;
}
.tg-photo img {
  max-width: 100%;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

/* آلبوم */
.tg-album {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 8px;
  margin: 12px 0;
}
.tg-album-item {
  overflow: hidden;
  border-radius: 12px;
}
.tg-album-item img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  transition: transform 0.2s;
}
.tg-album-item img:hover {
  transform: scale(1.02);
}

/* ویدیو */
.tg-video {
  margin: 12px 0;
}
.tg-video video {
  width: 100%;
  border-radius: 16px;
  background: black;
}
.tg-dl-btn {
  display: inline-block;
  background: #3b82f6;
  color: white;
  padding: 6px 14px;
  border-radius: 24px;
  font-size: 13px;
  text-decoration: none;
  margin-top: 6px;
}
.tg-dl-btn:hover {
  background: #2563eb;
}

/* فایل */
.tg-doc {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 12px 16px;
  margin: 12px 0;
  display: flex;
  align-items: center;
  gap: 12px;
}
.tg-doc-icon {
  font-size: 32px;
}
.tg-doc-info {
  flex: 1;
}
.tg-doc-title {
  font-weight: 600;
}
.tg-doc-extra {
  font-size: 12px;
  color: #6b7280;
}
.tg-doc-link {
  background: #3b82f6;
  color: white;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 12px;
  text-decoration: none;
}

/* نظرسنجی */
.tg-poll {
  background: #fef9e3;
  border: 1px solid #fde047;
  border-radius: 20px;
  padding: 12px 18px;
  margin: 12px 0;
}
.tg-poll h4 {
  margin: 0 0 10px 0;
  color: #854d0e;
}
.tg-poll ul {
  margin: 0;
  padding-right: 20px;
}
.tg-poll li {
  margin: 6px 0;
  color: #a16207;
}

/* فوتر پست (تاریخ و بازدید) */
.tg-footer {
  font-size: 12px;
  color: #9ca3af;
  margin-top: 12px;
  padding-top: 8px;
  border-top: 1px solid #e5e7eb;
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}
.tg-footer a {
  color: #6b7280;
  text-decoration: none;
}
.tg-footer a:hover {
  color: #3b82f6;
}

/* هدر کانال */
.tg-channel-header {
  text-align: center;
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 28px;
  color: white;
  margin-bottom: 24px;
}
.tg-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 4px solid white;
  margin-bottom: 12px;
}
.tg-channel-header h1 {
  margin: 8px 0 4px;
  font-size: 24px;
}
.tg-channel-header p {
  margin: 4px 0;
  opacity: 0.9;
}
.tg-channel-desc {
  background: #f3f4f6;
  padding: 14px 20px;
  border-radius: 20px;
  margin: 16px 0;
  font-size: 14px;
  color: #374151;
}
.tg-last-update {
  text-align: center;
  font-size: 12px;
  color: #9ca3af;
  margin: 16px 0;
}
.tg-telegram-btn {
  display: inline-block;
  background: #1e88e5;
  color: white;
  padding: 8px 18px;
  border-radius: 30px;
  text-decoration: none;
  margin: 12px 0;
  font-weight: 500;
}
.tg-telegram-btn:hover {
  background: #0b5e8a;
}
@media (prefers-color-scheme: dark) {
  .tg-channel-desc {
    background: #1f2937;
    color: #d1d5db;
  }
  .tg-post {
    background: #1e1e2f;
    border-color: #2d2d44;
  }
  .tg-post-header {
    background: #2a2a3b;
    color: #bbb;
    border-color: #3a3a52;
  }
  .tg-doc {
    background: #252535;
    border-color: #3a3a52;
  }
  .tg-forward {
    background: #1f2a3a;
    color: #90cdf4;
  }
}
</style>

<div class="tg-channel-box">

<div class="tg-channel-header">
<img src="https://cdn4.telesco.pe/file/EU0qUAghnO4Nz-5Bwf5oc6xFADnAG4o0k5BqW9-n-DUKMU7oYf8y_rbC0uH7okxaUCkKGgfbkOF5h6WBXCcanQRUXstxcc9OXFyxer2KegUlMcRcvYGUoH43KjNp8a5kY8xQ1ULpvP0m2TbWHA7cRcIRoWbS4rXF4ymE-5odQHLKz96J06n6lGb3G2uyvbOE4QX7MYppOsFCA-IS0_gfEqv6tvHA8cUaSAwQKbnY9BC8LgX_n1Omw2YZeTtTb9e7ZrC2gl2SUvCj88cNj6V136eXdgm8OEql3ZItgmwFU081C-mt7PNDQbB-oQ50_J59SCB4qopMYxvBFXMoefjKJQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.83M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-23 09:31:16</div>
<hr>

<div class="tg-post" id="msg-435264">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e-gojYoXcgc_1dgnzNq2ff4xGt0hBnD8KMPrR9x2f3Wih1J6d4d8CjktqrEt2nnT7VScOyLJjZyYiNh1K2HVbtyyjPYMWRrwx0LbMET4xAYxjCgo_sDB3lqfB_83fOnQ8fu_sgpd1bMUiS3IZC_OTcAp19ll6MHKn1UzAHnO6--kprkPswOZ4GiBXaq-DlXdtB3KcGa5zf5Jb3U8zZdrHC7vWwJeu43vL7quMxQFOuLiNs1jfe8h-a7FED0uvkoANBBn73uyWEc0141Qpcdvxkd34MUuVrNsZd8DBq-pZjF-QhDqHpZzk1M69p0ncH0AOmkC1WW8LWyLP4W9MWZtOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Md4Pd8u65uZs3ZKUZaLZRnmyTnhLC0NwehHtLX6h8t3ieAmz2eB6p0C7roz5UcNU22pGtSwYW4_dxvUYies5gkLCCeZ9oyCFeRCAUrNCF5SRARUYydgO-8skBKEnjly_S2coOulaTHMjAzcsFdF7xRSofZznqUyLZlIR5xykCuxf2X_EdbpDFI5IIxVqvf62dCxfu0gmkr1MIDyB4FtG_7hiboKTrzGQPY_zyZy3kO-uhU83dLmnEO3ZeDddmmomKAydqyi9YpHzHOeh_0NiQVu7WvYiGaT9TGrjGLbPQYU2aHGrc7PF55412vQC-ELoumCw7ZI-iHVJ2P5_nnU6mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NOvXGBl3JGimByHtySuLAZm_4FYnKN6lPxxejt33gOdx6kxLOjHEuuAxDsy8xx69InGn9AMj1wrkAEyFa1aw8WWTvzkp4vhrBg66NJnUoCI7IhJDj52EsrrG77ndxpqFu-HzY8klLLHUDpTCxja1vLE-YlSb0NvZpdGsHJHQln9NJw3mc76KxBxSQ_GRxhs955p-CcZaHOc5qSXO5luQOZGUMMcRRFUyPj-CopXnfhcMCSPOdH2Jm9FLq2eLkn4NDnHtMZ5BwJ1MKh7yqznuLL2IDaMAZbXD2xJG1J0TKdqGEbs6Uf-P7kbb04bxIQaiXCSU61F001-B-SzN6PhN_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nWqOf3gmYJC5PLO1ckCHo7gRT9vgn-xxBrFS5-jEFI3tC7WfI-KgaRnhRsZ_3tBYmC65tWOoq1ViIenG5-0My7_86l2pTJ11ks_wUzd1HQtUg-cAq-dP-L6JgJfzGju2S8YqYN0gHqTQLE3X9OD1D4it0CfeK0XArH65V-z3BgXb8fD-SetEjku92FN8SxTU88DuH30lA-vXZw3nWLjK-AdiXqnzz-2qZhWBbh02XNi1ybRVheHr2r-zGzpHqGKSJTyKXqB1YnamXRypfVY_wVBoROzO2c4bpy3lgZ7P5-O0qKwPQYPxG0GxPbvZaHFSIFQiiWt_nt3MmtRCpSme8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P7-fp1Y8vDVyihkYY3VVAuMB-66T5szHZv5jErmsik2eubZODUYlzUHSpIzVTIklmoLkRzUtL2HCW9Bx9mRXKPDbUQgqMkJxX-48VaOLCqXRa7E7D_DcHlbqc_Yjhi_0UWbdNzxMCQR1I5jPrCBtHi6loPvFg7xOIXbr6Lsi70M8hCh03kMLaM3vNhy5VKnIVQYCJPn_6Ts-AUNjQSXv-6za4TFnLMht5uUeRVWiS7-j9Jb1tjDyuP62Tx63BzeWgbKSqSxlWhodi0tDNjm9Dsr1G0L0wx8WWp8J1Guj29pBlWwgh5v9FxpQK_isdpN0B9BKGDVK4XA-YpcaNDYH1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IDwm49O66_SggFQCMC--BZeIUN7z1gDKHEM9lRouQoXd6nEnaStkMkEjU9UScME7Am-IMvMuVaJoU55kKyEiJSl_odoZMeCoITVrOOhfqbb04wzlW_8nwGQmU9s1NJjHdIo64WlgECsmZSUACMf2KxyaFige59TowSJiCh-1-OfXDEpKtG6IbFj5Vvo31gBh_GbjhyOBO2mTCH3_2RvQvIhNEWNBQuuJpzom-YUZnZdUts8-sVzjS9Qn9uZP6uhigZClTUiBxzToFFk3C-eVwQMB6kdhIwcgT_-UPxzY9avXc-KUQ1PSBznDeHwy8clAroPOkA1RBt329v015cHQ8Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
قهرمانان کشتی با حضور در چایخانۀ حرم رضوی از مردم پذیرایی کردند
@Farsna</div>
<div class="tg-footer">👁️ 670 · <a href="https://t.me/farsna/435264" target="_blank">📅 09:25 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435263">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-text">🎥
ویژه برنامۀ سپاه تهران برای گرامیداشت شهدا
🔹
معاون فرهنگی سپاه محمد رسول‌‌الله تهران: در میادین برنامه‌ریزی انجام داده‌ایم که براساس آن، هر شب به‌نام یک شهید تمثالش در تمامی میادین نصب می‌شود.
🔹
در میادین سیرۀ زندگی شهید، اقداماتی که انجام داده و دستاوردهایی که به‌دست آورده، برای مردم بیان خواهد شد.
@farspolitics
-
Link</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/farsna/435263" target="_blank">📅 09:19 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435262">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fcba5805d.mp4?token=NRJRx1IQenAbAtE2TrvY8UbzMC1GTa6SB8kJVb2WO2qkL5WgkPeCqhwFaxhAiIQdIJG_UDqCU5ZoUvGqmuQ3kTqVGIp98fNT2ThkH8Z0XayeL_2uRLG2pnkozoNxHEDaQ2-gbu40fAG96uyqW2UAL8XWP0kTfIl-7WZ_AM_eFk0kyfxHzuf8tjl_0ml_B6vYZIYSAg0O8vD9n35L1Pg3m04OG0pq1x-kKiKIU6s2Ol_H47TLjCXOEwtXSeFn6tTjsz3FEdjsek_9YuBNKUW8gSZH1c0Fc1tlVeFymplWoSFZ_OH34eWszfhNJZJtst2jftsXI_TveRfSDTFvADFtwIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fcba5805d.mp4?token=NRJRx1IQenAbAtE2TrvY8UbzMC1GTa6SB8kJVb2WO2qkL5WgkPeCqhwFaxhAiIQdIJG_UDqCU5ZoUvGqmuQ3kTqVGIp98fNT2ThkH8Z0XayeL_2uRLG2pnkozoNxHEDaQ2-gbu40fAG96uyqW2UAL8XWP0kTfIl-7WZ_AM_eFk0kyfxHzuf8tjl_0ml_B6vYZIYSAg0O8vD9n35L1Pg3m04OG0pq1x-kKiKIU6s2Ol_H47TLjCXOEwtXSeFn6tTjsz3FEdjsek_9YuBNKUW8gSZH1c0Fc1tlVeFymplWoSFZ_OH34eWszfhNJZJtst2jftsXI_TveRfSDTFvADFtwIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فریاد زنی در صورت پهلوی در واشنگتن: شرم بر شما
🔹
یک زن معترض به جنگ آمریکا علیه ایران در جریان نشست روز گذشته نشریه آمریکایی پولتیکو و کارخانه اسلحه‌سازی لاکهید در واشنگتن، که رضا پهلوی در آن سخنرانی می‌کرد، فریاد زد «شرم بر شما!»
🔹
وی در حالیکه فریاد می‌زد، خطاب به پهلوی گفت «شما کجا بودید وقتی مردم ما داشتند فرزندانشان را از زیر آوار بمب‌هایی که شما به کشورمان دعوت کرده‌اید بیرون می‌کشیدند؟ چطور می‌توانید بگویید «مردم من! ایران من!» و بعد‌ آنها را دعوت به بمباران مردم کنید؟ شرم بر شما!»
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/farsna/435262" target="_blank">📅 08:54 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435256">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B4-iRZXcBpTuJNClaT2S4fcY9dC73DlNnWxxhvCHLojhpv_a63_lKuSnnmdpedsdUuUj5DvWtZ10txvWsVMBKRx8n-TWht9rrMD93co1Y8_9jodgk8fnP0JE--lGTlWNBNUi36_tR1CrstWsc22yL2asxcu26v4Z5sAHsYi1BQZSTMs3z1Tb0sDFlz7CwJ7xoYS3rcNJRRJnDlBUDNhLi5nNAiraRr7n3jdCBnrSjrqMasliZw0QHO8SHbWOdijvpOKxU3xuyYU3Px8i2WNzHXPCbPR-DpyM2I57KBc4zViUKUziQYfDkkoE3yEsz31rRRtu2Wsb7VYhmP2CcIVkqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JhNmHbh_AKIa9Rn0g8vyMMLU8c5xZFcG2iESANsZG41Sgaaz8ux7sqONuwoUQKXHjGncnWUYZ4dBr-vZ6MurL_5aNcCruamlZAsQq-WNHoUDhr4tU8Drfqjj0bmcrQ4jHDBUCyZZsa4zkns4SWtifbSxU4MrTCI4PJ50SlYLZ188NVlIkXNX2qsLE_l0U5cS3lGHOuLpk8e9Wlz_JHrGMX7zB4SmwMpUNebZBFBK6YjaUpgugclLDuERbil6YhkIWiSuYPHkoC3qForDU8qBDzLw1bE80xcP5KaQY2BPc2jDxp6nklRN6QlyyBD_St-aryQgRWKzGLiRkVU1DrUN1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a-3dZeiD63yDSQQxVXdZKiHT7tddx0SuUkEQ9rthOcGOqlE4EVE4-Gitn2C13hJ0xJ5JYl1huI1ZQ8KP3jybumgs040r7XTc0a-Xgn8r8lFTeD5EzIvSLdqtHDC4l2yyHz_3kqNEGLyQGxn6KiSXFYzNTOq5Z7m1Aaid2u43Bs-BkBnNZ1Y5j6CHkDUW3wy95VsVHfd1bGbRH920_mvKpZwx2Vkg_vKbKi7dduPe-XgK7J8yG8z6pPnJDj6K6Pst6E-JIMsCLecc_wDaXq4ciQKQS-7nRQRRMDHmXm17NxMFRyH8t3d-tQg0AhG8vI-PDiScfrw-Q3zCkDs5mDj2sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QYj2ACSJgLY0I_YbVck3s8RB0jKzxD3mlWpVNwAsA_bFdpfbBtyeRjT8bk_ibqP6nDWArB6vDDrpxxZ-pLOvtSUIn5nXbaGA7LcNQ8p_-2KTP7HwVhHk3NVgqftLNgf49MG4a4_gNiGIM6Xx6J9GNsV16cMkEKNLdkHASok3A3dG7oFA6ix2o9UNZUeHRebsrj93ZxRazuq9XH3obPoKnHuYyRahY9GL79xS-pFMb338pmfsI7XO9-DEiU0hvpILuYiQp32g0HDCxxueLTKXWlNTyt0NSwqF-kJmr7t9dU8k8r9tKrdVL7k5Sabo8z3Xn4kslZiv6kQ6uoeT9StwOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hpSz-Jq_-9H5YoMiAyzCLkmUVMvIrs5-NM8p-seA3I2H8xdlw2h9OfLTxzh82DqLV_E5NGC8Kj-7a4kyv_DvJCCEf2TCiE_eypRT5p9oUAuW8YIwF2pioEwBMT8PYHL_7p6pdsR-ycqd1AZ8cGnltNtWJdP0uIqBZAVHQJzaG2Lv-dfToymmzq8bT8LpQGTH6qJTnmqh9KwLeRXJQdxkvDsaaTv8myXOZV14ftZ2udYYdh3B0JX9CyJ1Gg7M___20XLAYerYrII56pgV9yn1fPnI3bbEqoft4Y9bEOawqLmnufiCZIQHbzN2xmfmkqxtewBffFuGbI__ubO_F_oFVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vdEsOr6u7_LZanSOhRU-mGGbMsJRJvXkB_9g4evGkb915Ekz1GUF2jFLFGNvUTYdeg0jbjsLfgsiutKrCCmkFEm1kbp8WDB_zce32j8gZn7Iwzp8EOVx-a2xErIkQMuP7cdnvJqhFkBCb59h2hATcxBQSnOZuHwLSNt1hDYw-rv625Afedbssq1u50JPQdNe_cjNYEtJYzSKkYI8cadQHPcbV4aDvOPZ3Wz-OgsIq_-860CTiS6hxYINT4QykF017i3vcjV8cmVZWH6x4XnvDBXqvvcN2Gz25kxHpGIvUVbjsXrNk2hARbvYweNLCjS4o7jbIV2o_JC3u49zq0hkHA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">احسان افرشته، جاسوس موساد اعدام شد
🔹
احسان افرشته، فرزند مصطفی که به اتهام جاسوسی و همکاری اطلاعاتی به نفع رژیم صهیونیستی بازداشت و محاکمه شده بود پس از طی فرآیند کامل آیین دادرسی کیفری و تایید و ابرام حکم در دیوان عالی کشور بامداد امروز به سزای اعمالش رسید و به دار مجازات آویخته شد.
🔹
او از بدو ارتباط با اولین افسر موساد چند مرحله تماس از طریق پیام‌رسان‌ها داشته و در ادامه از طریق پست الکترونیک باهم در ارتباط بوده‌اند. افرشته در ابتدا در پوشش راننده تاکسی اینترنتی دستورات افسران موساد را اجرا می‌کرد.
🔹
افرشته در طول همکاری با رژیم صهیونیستی به زبان‌های انگلیسی، فرانسه و عبری مسلط شده و نام سازمانی او نزد سرویس موساد «جیمز» بوده است.
🔹
محکوم در طول همکاری خود با موساد حداقل ماهانه ۴ الی ۵ پست الکترونیک فارغ از تماس‌های صوتی و... با افسران اطلاعاتی موساد داشته و بیش از ۳۰۰ پیام بین آنها رد و بدل شده است.
@Farsna</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/farsna/435256" target="_blank">📅 08:24 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435255">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OSb25O97mVisVf6nq02ok2xSkoXpEmW3VkuBfQmhDmkXgUGP9zds-fQA9Hw0gkQrLACF3w3Gz-k-sC_6YdOpsv3da9rzpCQzLkQMOoVk9-M7j6i1PsT2-d0jttl2J92oWj_CsOVGU8BwhhTR8vlYS9h48eAefTmFTPo6u1H1Q-eyyZ-DEtuyNqOXLwhmm0QCg1I6xTHki0ZMdlM0uS49viYNxr5zQ8w852OegU-8lbVJLeBBQmp5Z01NYXgN529I9F8kSDBENf6CUJ16h0ulogNpV-S3ix3d_tahpREc2xB4EMXIXQ8jgs-R4WGwoVNGAIAyz_Diqip-fUjsSn7A5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظرفیت ۳۰ میلیون تنی که محاصره را دور می‌زند
🔹
در حالی که تنگۀ هرمز به گلوگاه تحریم‌های آمریکایی تبدیل شده، دریای خزر به خط مقدم تاب‌آوری اقتصادی ایران بدل شده است.
🔹
استاندار گیلان می‌گوید که بنادر شمالی ظرفیت واردات ۳۰ میلیون تن کالای اساسی را دارند؛ رقمی که معادل کل نیاز وارداتی کشور در سال گذشته است.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/farsna/435255" target="_blank">📅 07:46 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435254">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">پیش‌بینی رگبار و رعدوبرق در ۱۸ استان
🔹
هواشناسی: امروز چهارشنبه در برخی مناطق استان‌های آذربایجان شرقی، آذربایجان غربی، اردبیل، گیلان، مازندران، ارتفاعات گلستان و سمنان، کردستان، زنجان، قزوین، البرز، تهران، قم، همدان، مرکزی و برخی نقاط واقع در جنوب خراسان رضوی، شمال خراسان جنوبی و شرق یزد، رگبار و رعدوبرق و وزش باد شدید موقت، گاهی همراه با گردوخاک و در نقاط مستعد بارش تگرگ پیش‌بینی می‌شود.
🔸
امروز آسمان تهران قسمتی نیمه ابری همراه با وزش باد، گاهی افزایش ابر، وزش باد شدید و رگبار و رعدوبرق است.
🔹
جمعه با ورود سامانۀ بارشی جدید از شمال‌غرب و غرب کشور، بارش در این مناطق آغاز خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/farsna/435254" target="_blank">📅 07:35 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435253">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🎥
روایت مجری ثریا از مدافعان هرمز: در گرمایی که تحملش دشوار است، رزمندگان ما ۲۴ ساعته در جزیرۀ هرمز از وطن پاسداری می‌کنند
.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/farsna/435253" target="_blank">📅 07:20 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435252">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PmOyVAwA90vNZ--pvCaYhCfMCWZjg0TMe9mzR0hBk9F0CgSUitxXBFASodrThQW6XL7AdPwggmzxBatwlbHqF4tbPBAecXTm7GFylvt-3tpqqrl2HvWtriYPbV4QVEbnkAfdgYY7M459Xrxgl15Smhntp7aD8gR98QNksNWskk9APNjFx6UfRBpy2VVoqMs7--txy4oFqStw7AD5JO_OBi7i0q6cHQVODOUyQlZHYjp_qlE3HuOkohGgt15LDv-w8_gJLHnYINMjOwF8rx6F5pjiLQahpvhmu7sDFXB77v3O2pyP715PW75ndQALQGHSsAYrRiRCsQay3sNngG6o0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرداری تهران: انبار کالاهای اساسی تا ۶ ماه آینده پر است
🔹
معاون خدمات شهری: مردم اطمینان داشته باشند که با تأمین گسترده کالا در ۳۱۵ میدان میوه‌وتره‌بار، تا شش‌ماه آینده هیچ کمبودی در کالاهای اساسی نخواهیم داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/farsna/435252" target="_blank">📅 06:32 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435251">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس علم و فناوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WXwno-A4gYg3yhBN_3VlqXbl8ctHfXdjYmtBCUH9y2YXqLfMsuXM1Y6HMjMpHyyRFkr8Oj9vVaN3Ig7bCSyFtU8ETcQgcRzzvipyjxrhf6483s5a11IVTSO3gf7SltAYD7YWk1n7ofjAilWkCDQqkoFy7XNFT8Y3c7p_Rfsb63gq6ebe_ikNIq86GyLjghSiR2-5-h6wT8nwhy6w9Stp0OOfibh8XwjB9_PTqbIaYMTCQ8cujuiYTawKv1d0eZG0EmaluoS_iHh2zRz8CCeS8hlBuUYJAZnlDF0-zrnu1Xb1wqZhg9HtkVELPKRtaDoJaTOraGlp4_bESyMI8FocHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حذف خبر توافقی مهم از سایت دولت آمریکا
🔹
وزارت بازرگانی آمریکا صفحه مربوط به توافق خود با شرکت‌های گوگل، مایکروسافت و ایکس‌ای‌آی برای آزمایش امنیتی مدل‌های جدید هوش مصنوعی را از وب‌سایت خود حذف کرده است.
🔹
لینکی که پیش‌تر جزئیات این همکاری را توضیح می‌داد، اکنون به صفحه «یافت نشد» هدایت می‌شود و بعداً به سایت «مرکز استانداردها و نوآوری هوش مصنوعی» منتقل شده است.
🔹
طبق این توافق که چند روز پیش اعلام شده بود، شرکت‌های فناوری قرار بود مدل‌های پیشرفته خود را پیش از عرضه عمومی در اختیار دولت قرار دهند تا از نظر خطرات و آسیب‌پذیری‌های امنیتی بررسی شوند.
@FarsnaTech
-
Link</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/farsna/435251" target="_blank">📅 06:11 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435250">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o93HJNhd73YuNh21LSNzMYb7UXMaTZyj2U6vq3No-pty-oFOSl3DF5XQnfd53aedDR5YWgYSMPR7dskpj4z0U5Q-XuMGp5Ep67XEhVL80keqB4ihvp_wbZazQYFhcOfrUTCyOOqp5QMa4o-9HOPmhL5Hgm3m-6Qz1khIPkANQ9s7EDJu-4T2mnqw2NCy9LmAJFjRgMIMQ15lz9JdtL-UCyMZs2TzhWDlVK9Cekha1eYrWA2OPW-Ref4ZpRh0-6WEX2940wFmREmzwhWNRzpRA91Ov_tRlZxYKhM0pvYlUCPCfkBinYHkv5hFJUhJAI9cGuH7RvkgSQcV2Djv6dou0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماجرای مسدود شدن شبانۀ تونل‌های پایتخت چیست؟
🔹
در ماه‌های اخیر بارها اخباری از مسدود شدن شبانۀ تونل‌های تهران در رسانه‌ها منتشر شده و دلیل بسته شدن شبانه تونل‌های پایتخت سؤال بسیاری از شهروندان تهرانی است.
🔹
مدیرعامل شرکت کنترل ترافیک تهران می‌گوید: انسدادهای موقت تونل‌های شهری عمدتاً با هدف انجام عملیات فنی، نگهداری و ارتقای ایمنی زیرساخت‌های ترافیکی انجام می‌شود تا عملکرد تجهیزات حیاتی این تونل‌ها در سطح مطلوب حفظ شود.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/farsna/435250" target="_blank">📅 05:43 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435249">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F2k_GZFeeM5x51cRer4C4efZgeAI0kRix4MIgUikon5P6O8x-cARrHKqp2bRt5hAn0rrMCZxMSfq0mLJAD5tb2j5JIZY_uTqhNE_G7Y-LwiqAjOtNMdG5Y7Tsh11p4j2FXx2VWBQ_9Su-Ov5kKFzhx0EdRODA-fhrzucjWUN_7xkZ942JlsN1wukrZVK_MbcS4bDu1tm6Ed5quTLPYRvVwbE_nLL6b2GVk-RaBmspF9ob_BBr-2j8GDaCw-qe1vS799C0pCQogQ-va_6t7ljC__KEbbiX4ANzKK1lVTVYLklt_KEJa_-_YUSb5nRzvV8b-VUQAv3bg3IH7_g4NaFAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پکن: پاکستان میانجی‌گری بین آمریکا و ایران را تشدید کند
🔹
وزیر خارجۀ چین در گفت‌وگو با همتای پاکستانی خود، بر تداوم حمایت پکن از میانجی‌گری بین آمریکا و ایران، و مشارکت در این روند تاکید کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/farsna/435249" target="_blank">📅 05:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435247">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62277199ed.mp4?token=GXl-qve8g_dueTk1aq4WEJltPEIb8xpaALl2G568PrSdMH6yc3t8WtsSyCunC1FP4zMOmPoAdVyYY1tXyMHNQPqjRIEG2J41rPA8j2verFNlwTBhMokQ38-lSvlprfjOIcYFEsC9KxdSzzJgatUyz7rwJn6NU-ZRSV-tvs1UrjsAfkuDFquiq4PlhFl7X4YM7SeXD2w6xfiXu7t54xvlzWWFE_QSfqIGidvKSlaLvhZoWMJOntduz8ROmv8_RnpnDlZxfDbla_LEDb2mc9_bxG9S49gJlJ-WWx91H5OK3s6IXPA2OO39vvpUtZLgKuFxaxC88x9a0Zet7JJR2zprIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62277199ed.mp4?token=GXl-qve8g_dueTk1aq4WEJltPEIb8xpaALl2G568PrSdMH6yc3t8WtsSyCunC1FP4zMOmPoAdVyYY1tXyMHNQPqjRIEG2J41rPA8j2verFNlwTBhMokQ38-lSvlprfjOIcYFEsC9KxdSzzJgatUyz7rwJn6NU-ZRSV-tvs1UrjsAfkuDFquiq4PlhFl7X4YM7SeXD2w6xfiXu7t54xvlzWWFE_QSfqIGidvKSlaLvhZoWMJOntduz8ROmv8_RnpnDlZxfDbla_LEDb2mc9_bxG9S49gJlJ-WWx91H5OK3s6IXPA2OO39vvpUtZLgKuFxaxC88x9a0Zet7JJR2zprIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
آخرین ایستگاهِ خط هفت مترو تهران افتتاح شد
🔹
ایستگاه مترو ورزشگاه تختی به همراه ۲.۵ کیلومتر مسیر تونلی در خط ۷ متروی تهران، امروز افتتاح شد. @Farsna - Link</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/farsna/435247" target="_blank">📅 05:10 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435246">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">آموزش‌و‌پرورش: احتمال دایر بودن کلاس‌ها در پنج‌شنبه، جمعه ۷ و ۸ خرداد
🔹
معاون آموزش متوسطۀ آموزش‌وپرورش: اگر دبیری احساس کند نیاز به رفع اشکال برای دانش‌آموزان وجود دارد، روزهای پنج‌شنبه و جمعه ٧ و ٨ خرداد، کلاس‌ها برگزار است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/farsna/435246" target="_blank">📅 04:44 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435245">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">شهریۀ کودکستان‌ها تا قبل از آغاز سال تحصیلی جدید تعیین می‌شود
🔹
به گفتۀ رئیس سازمان تعلیم‌‌وتربیت کودک، تلاش شده که تعیین شهریه کودکستان‌ها مبتنی بر واقعیت‌های موجود باشد و از پرداخت شهریه‌های غیرمتعارف جلوگیری شود.
🔹
این فرایند از ۱۵ خرداد آغاز می‌شود و تا پیش از مهرماه شهریۀ کودکستان‌ها و مراکز تعیین خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/farsna/435245" target="_blank">📅 04:14 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435244">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K0BXPtP4MpbJK-vC0ZRNntmM_jCbji06rusq2fP70Mt7y4_7cPY-6PK59SzrW6OuyEfJQ0A9zMyE2YLz8Zezp2Oyssn-BIA8u54fEno6_YjMn15ufciy63MZoPHmo0ogJ0AObZRnOsbp7YPRkYKp5CCOKqB_Nq-9TIPgwQoFhbVu4D2Q83o0TMHepi0V3sOOFWuSi13d5aZEwuqmKjmy045bHPCxqFh65ZzlDXN2X2SAOLh1Qk67PtVllLbP3VoVH8o6YQoUvek5Rzk98isJGv0BHqGvFb7_i5dZsL20X420F6YYQf_lFndCYxmHuC5SQxQkXtHdNMugBR-RBtfIaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان: اسرائیل نگران توافق بد آمریکا با ایران است
🔹
مقام‌های صهیونیست به شبکه «سی‌ان‌ان» گفتند که تل‌آویو نگران است آمریکا بدون رسیدگی به مسائل مد نظر این رژیم، به توافقی با ایران تن دهد.
@FarsNewsInt
- Link</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/farsna/435244" target="_blank">📅 03:45 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435243">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🎥
آبادانی‌ها امشب را با نوای صادق آهنگران به میدان آمدند.
@Farsna</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/farsna/435243" target="_blank">📅 03:37 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435242">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/anNcRnCzS_RWLnAVqzUFLWlk3pRI3QUdQsf1o8BY2vhCphGUMpdLaCUtDE0qWkvJcrxmzXWHsfQsBPIjvTM_RuQ4ZkLOeXGN8qIlGhYYE48HJfb5uxTkOZGI0iGD0Apmmj-8Aii4bVRK9oec6KmvPzsYbVw9erBWj4ND8_4-jKYoZTmXJcXF9q_qjyVvTrTC3LrWhkPsdoGZwmrW_5zItpGcOcvV8POg_DpVEWT9gsASw7jpWuEPkrFUAZiw4ybp-tYBQ7GIrYu9UijJ-aV_ZE5oYe2W5QYP0AWkdGxsr7W9QIUlOaVWbF5BaCoUZLuVgPGS04IxNPrOmNW2k0XDiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گفت‌وگوی ترامپ با رئیس امارات در راه چین
🔹
رئیس‌جمهور آمریکا حین پرواز به سمت چین، به‌صورت تلفنی با «محمد بن زائد» رئیس امارات عربی متحده دربارۀ تحولات منطقۀ غرب آسیا گفت‌وگو کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/farsna/435242" target="_blank">📅 03:16 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435241">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🎥
زمین جایگزین بازار جنت مشخص شد
🔹
شهردار منطقه ۵ تهران: زمینی به مساحت ۱۰ هزار مترمربع در سیمون‌بولیوار، جنب ورزشگاه شهید کاظمی، به‌عنوان جایگزین بازار جنت اختصاص یافته است.
🔹
قرار است در ۴ هزار مترمربع از این زمین ۲۵۴ غرفه احداث و باقی فضا به پارکینگ تبدیل…</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/farsna/435241" target="_blank">📅 02:58 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435240">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🎥
اجتماع دوقلوهای شیرازی در میدانِ خیابان، به‌مناسبت روز دوقلوها
@Farsna</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/farsna/435240" target="_blank">📅 02:37 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435239">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oAZo8x1ErDyE7KnWeTzWcku40WqxUwmQkeeOA4rW5PBxkEaDupoPDBIbqhnRizrBFtq8a0uJDfipNBoGQXAjNk7AKw2ydzdf_WAcz0LOfVSlEjoPL0B9XdTHcIjkCB9I_J0N9Sfz87nkar4jzOu91zr3JHoKpcOnS2-Sz7m7p4LKWoliCmgSkyHEYshueLp2sbUovo_u2YraHOF352u-ZHB-G4mGLtfXDBfJ3vxSqwqpEo3SIxHoBFKQV3l1qRpe1QRLb17ZV0eEYGkuRL1SgGfdgzYRS-ThBorWSOCVIlMCIkTDQoLdh4srL7T1gbGWG8taxugR4OwZnYGDfSDJ4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره: ۱۱۲ کشور به قطعنامه آمریکا درباره تنگه هرمز پیوستند
🔹
منابع دیپلماتیک می‌گویند که ۱۱۲ کشور هم‌اکنون از پیش‌نویس قطعنامه پیشنهادی آمریکا به شورای امنیت سازمان ملل درباره تنگه هرمز حمایت می‌کنند.
@FarsNewsInt
- Link</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/farsna/435239" target="_blank">📅 02:22 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435238">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">طوفان امشب تهران ۱۷ مصدوم در پی داشت
🔹
بنابر اعلام اورژانس تهران، در جریان حوادث جوی شامگاه امروز مجموعاً ۱۷ نفر دچار مصدومیت شدند که ۶ نفر در محل حادثه درمان شده و ۱۱ نفر دیگر به مراکز درمانی انتقال یافتند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/farsna/435238" target="_blank">📅 02:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435237">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E2YFr6O5a5ahnZDTCXR7Ss19DFCojVYiRUdQCjHm4mTwkQ0gop9hWjWk5uJ11-8WnLSlCZ_PnTrP4R4FMkNB5xms-JGRq6kNIyx6Y4Jc3Wf7I0jMRk7hKjR8CqQ1Mhk_nMRtppnDGjnO95gFBOz3MbcshOAdnNE1e5jQFO8mqm_a180RR-1T3sCf6pa83DTHtG4ggKLr1wWZT3InvX7ARhNKPQkNAgxGq1Eun2zkMvuEJcy_Fli4d3sV2SiabqDI_BcPCtjBy0Xjz1_wAnenDrh9gx7cBVK3Ybvwwkyv8H_Pd4IxZxvxpcdJ8Mk7DwJV5pl3CNNSav9qb7U98VoFnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاهبرداری جدید ترامپ از آمریکایی‌ها با موبایل طلایی!
🔹
۵۹۰ هزار نفر برای خرید گوشی طلایی ترامپ ثبت‌نام کرده‌اند اما هنوز هیچ موبایلی دریافت نکرده‌اند.
🔹
مشتریان برای پیش‌خرید این موبایل ۴۹۹ دلاری، مبلغ ۱۰۰ دلار پیش‌پرداخت کرده‌اند؛ یعنی در مجموع ۵۹ میلیون دلار  پرداخت شده اما با گذشت یک سال، هنوز حتی یک دستگاه هم ارسال نشده است.
🔹
تاریخ‌های عرضه هم مدام به تعویق می‌افتد و منایع آمریکایی می‌گویند که بازپرداخت و تحویل کالا تضمینی نیست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/farsna/435237" target="_blank">📅 01:59 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435236">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">اقامۀ نماز آیات برای تهرانی‌ها درپی وقوع زلزله واجب است
🔹
به دنبال وقوع زمین‌لرزه در مرز استان‌های تهران و مازندران، بر اساس موازین فقهی، با وقوع زلزله، اقامۀ نماز آیات بر افرادی که در محدودۀ لرزش حضور داشته‌اند واجب فوری است.
🔹
طبق رسالۀ عملیه و فتوای مراجع عظام تقلید، رعایت نکات زیر حائز اهمیت است:
🔸
محدودۀ جغرافیایی وجوب:
اقامۀ این نماز تنها بر کسانی واجب است که در شهر یا منطقه‌ای حضور دارند که زلزله در آن رخ داده و یا لرزش آن را احساس کرده‌اند.
🔸
زمان اقامه:
نماز آیاتِ زلزله باید در اولین فرصت ممکن و بدون تاخیر (پس از رفع دلهرۀ اولیه و پیدا کردن شرایط ایمن) خوانده شود.
🔸
اطلاع دیرهنگام:
اگر فردی در زمان وقوع زلزله خواب باشد یا به هر دلیلی متوجه آن نشود و بعداً از طریق اخبار یا اطرافیان مطلع شود، همچنان خواندن نماز آیات بر او واجب است.
🔸
تعدد زلزله‌ها (پس‌لرزه‌ها):
با توجه به وقوع پس‌لرزه در ساعات گذشته، برای هر زمین‌لرزه یا پس‌لرزه که به صورت عمومی احساس شده باشد، یک نماز آیات جداگانه بر فرد واجب می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/farsna/435236" target="_blank">📅 01:45 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435235">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">نیویورک‌تایمز: ایران به اکثر تأسیسات موشکی‌اش دسترسی دارد
🔹
روزنامۀ نیویورک تایمز بر اساس گزارش‌های آژانس‌های اطلاعاتی و امنیتی آمریکا‌ نوشت که بر خلاف ادعاهای ترامپ، ایران به اکثر سایت‌های موشکی خود دسترسی دارد و ۹۰ درصد آن‌ها عملیاتی هستند.
🔹
ایران دسترسی عملیاتی به ۳۰ سایت از ۳۳ سایت موشکی خود در امتداد تنگۀ هرمز را احیا کرده، که می‌تواند کشتی‌های جنگی و نفتکش‌های آمریکایی را که از این آبراه باریک عبور می‌کنند، تهدید کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/farsna/435235" target="_blank">📅 01:30 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435232">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t181wTKzMS7GNRPKuwzdyCqQbccA0lC1hSlDAv2Gs0IUgNWKwTKNupqS5tMSj06Gwd0dv69ehv-9QhMdg8cNA4jLKXbKvoSJl858xlhrZfGC0qub5fgzAMd_8uRMhNovsGBhMikf7FCUKFsqAZZy3nXmmwl7vh5v9dGHPEN2q6Yh3Sstq1jmFH1-VIKOwxd2C1PbwmeTafnLtv5JgkhjWC2HmLkQGa5gUi0rRC_zlKwaAPmCHkRyAPwCl-OS-gWY6XSQROqw0Xu4JFh9jFjRurYC77rEHWc0MgenIQ1x_Fnag7_oQCqXqQeTI8eG4oc_BvgBvHcbz4_MQJ8SmyrbjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بقائی: آنچه بر ملت صلح‌دوست ایران تحمیل شده جنگ متعارف نیست
🔹
سخنگوی وزارت خارجه در شبکۀ اجتماعی ایکس نوشت: در یک سو کسانی ایستاده‌اند که از نقض قواعد حقوق جنگ و زیر پا گذاشتن اصول انسانی لذت می‌برند؛ کسانی که برای تفریح آدم می‌کشند، کودکان را سلاخی می‌کنند تا خانواده‌هایشان را عذاب دهند، و به سالن‌های ورزشی زنان حمله می‌کنند فقط برای آزمایش قدرت تخریب جدیدترین موشک‌هایشان.
🔹
این جنگ میان کسانی است که با افتخار از غرق کردن کشتی‌های غیرمسلح برای «تفریح بیشتر» حرف می‌زنند، و مردمی که حتی در میانۀ تجاوز، برای حفاظت از جان بی‌گناهان نهایت تلاش خود را می‌کنند.
🔹
این جنگ میان دروغگویان حرفه‌ای است که برای خشونت‌شان توجیه جعل می‌کنند، و مردمی شریف که فقط با تکیه بر توان و ارادۀ خود، از وطن و کرامت انسانی‌شان دفاع می‌کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/farsna/435232" target="_blank">📅 01:14 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435231">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316c432ae2.mp4?token=o2HN_A-OMJhKCPBOWmrFZORA2oLnqhZXExS2Uz3p4lawJkFG5Y3GD4WEkUGfJ7PLMHUwSolHIXcsqU7HS3ax0_U419wWWqnel74mBVnz_yksOjMQ6c6DI4eR3AH0WZ1czNrZNc2TYeJ3oneUpvRuO8XJZQnnt01S5WC1HyYXb7iN9kmtVDiQPXwgSQIYK4zpqSPe8VP6h5gEbpW30Wf9dXcbdks8bArbyv5FQCA3WSMGLX6cCA2HjhXbXyOyySDNrHRhPu48t3k5r8Plv1A23qpQ3zMD-v-hzpzHdwPdsuk1eZn5IQOrVh5i1H1aKGk1lSkJv_dfnQpFjT59H_c5w2BgZCT-4OOq2xwxH41EYxu2aYa8IWH6MGsyTtA69dZ9hNgyhxj2hyswjAQCokIgNkvF92zGAXpqvlarBN_8Dr1yiz3fVLdfzkma1f74slqkOjS3hvGVCjaf6XqWZLx1XupU4JxS_D21Nsx7ZPK5uSCOu0cGko7N9TNK-iAmY4rc3GNnrnFgANUa-NZoXGHPjViw8QJpzxMFpnlP9III_1UthrS5v3WomDs1iXjPVkN0a4zfR4tXqBidD5d24cZ8i3LpS1Snzg4RVWFQTnyiasuUYG2Rdlmoj090rGvcFXG9J8dT1pk3HO00USVYlNjOubCo-0O8A6da5rXM8YWE17M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316c432ae2.mp4?token=o2HN_A-OMJhKCPBOWmrFZORA2oLnqhZXExS2Uz3p4lawJkFG5Y3GD4WEkUGfJ7PLMHUwSolHIXcsqU7HS3ax0_U419wWWqnel74mBVnz_yksOjMQ6c6DI4eR3AH0WZ1czNrZNc2TYeJ3oneUpvRuO8XJZQnnt01S5WC1HyYXb7iN9kmtVDiQPXwgSQIYK4zpqSPe8VP6h5gEbpW30Wf9dXcbdks8bArbyv5FQCA3WSMGLX6cCA2HjhXbXyOyySDNrHRhPu48t3k5r8Plv1A23qpQ3zMD-v-hzpzHdwPdsuk1eZn5IQOrVh5i1H1aKGk1lSkJv_dfnQpFjT59H_c5w2BgZCT-4OOq2xwxH41EYxu2aYa8IWH6MGsyTtA69dZ9hNgyhxj2hyswjAQCokIgNkvF92zGAXpqvlarBN_8Dr1yiz3fVLdfzkma1f74slqkOjS3hvGVCjaf6XqWZLx1XupU4JxS_D21Nsx7ZPK5uSCOu0cGko7N9TNK-iAmY4rc3GNnrnFgANUa-NZoXGHPjViw8QJpzxMFpnlP9III_1UthrS5v3WomDs1iXjPVkN0a4zfR4tXqBidD5d24cZ8i3LpS1Snzg4RVWFQTnyiasuUYG2Rdlmoj090rGvcFXG9J8dT1pk3HO00USVYlNjOubCo-0O8A6da5rXM8YWE17M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر اقتصاد: امیدواریم که یک روند کاهش قیمتی را داشته باشیم   تیم اقتصادی دولت در تلاش است و این تلاش به‌تدریج آثارش را نشان خواهد داد. بانک مرکزی نیز برای کنترل تورم درحال اقدامات جدی است. @Farsna</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/farsna/435231" target="_blank">📅 01:10 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435230">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c74ca1d8b.mp4?token=v4B8Bc2tkTRfMCSyiKLf4vsqcmKi669qbJOjUb5a3w2NjjmwxNZbwK3PgtuXabKGyQjpc8dKV2aa_3yKknJuKSZQ08aPdZgxPxGXldH9WsYgS2LdmFJSdW3ubQ4hrQ7nHU8enHPO5XPHEJvKAG4v9QFqZhzLBg72DmGuhgc95ArM-sBJDHwXi38tjxCPUKSnMcNEBlKHON9OOnQD8PiGM9Za_Kg1zDO-43NHJPyqqS3ts7YT8NbLi1swRk2hF4Sm1ZlXeSyPH-NiOGFwmlHf9olQpg4iNGBxAZ7a2qHQda8Inkake2AOaZRUkRC8DX2fRabp2xxsK7WPr0LWfqXhQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c74ca1d8b.mp4?token=v4B8Bc2tkTRfMCSyiKLf4vsqcmKi669qbJOjUb5a3w2NjjmwxNZbwK3PgtuXabKGyQjpc8dKV2aa_3yKknJuKSZQ08aPdZgxPxGXldH9WsYgS2LdmFJSdW3ubQ4hrQ7nHU8enHPO5XPHEJvKAG4v9QFqZhzLBg72DmGuhgc95ArM-sBJDHwXi38tjxCPUKSnMcNEBlKHON9OOnQD8PiGM9Za_Kg1zDO-43NHJPyqqS3ts7YT8NbLi1swRk2hF4Sm1ZlXeSyPH-NiOGFwmlHf9olQpg4iNGBxAZ7a2qHQda8Inkake2AOaZRUkRC8DX2fRabp2xxsK7WPr0LWfqXhQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انیمیشن طنز «عملیات پروژۀ آزادی»
🔸
دیگه یه راه جدید پیدا کردم که از تنگۀ هرمز رد بشیم!
@Farsna</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/farsna/435230" target="_blank">📅 01:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435229">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">‌
🔴
ثبت ۲ پس‌لرزهٔ ۴ و ۳.۴ ریشتری در مرز تهران و مازندران
🔸
لرزه‌نگاری: دقایقی پیش ۲ زمین‌لرزهٔ ۴ و ۳.۴ ریشتری مرز استان‌های تهران و مازندران را لرزاند. @Farsna</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/farsna/435229" target="_blank">📅 00:50 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435227">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">‌
🔴
برخی کاربران از حس‌کردن لرزش خفیف دوباره در تهران خبر می‌دهند. @Farsna</div>
<div class="tg-footer">👁️ 8.27K · <a href="https://t.me/farsna/435227" target="_blank">📅 00:43 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435226">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‌
🔴
رئیس هلال‌احمر: زلزله در تهران هیچ خسارت مالی و جانی درپی نداشته است.  @Farsna</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/farsna/435226" target="_blank">📅 00:30 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435225">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‌
🔴
لرزه‌نگاری: لحظاتی پیش زلزلهٔ ۴.۶ ریشتری مرز استان‌های تهران و مازندران را لرزاند. @Farsna</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/farsna/435225" target="_blank">📅 00:28 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435224">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🎥
رجز دختر کردستانی در اجتماع شبانه سنندج
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/farsna/435224" target="_blank">📅 00:27 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435222">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lKPZsekoGRxXmB8A-GazSBVC2Ifat0casUhrhGlHfeWId-s3bL5aCilF-wgNRLFMqrNAabOIfYH5ODWgIR0wY6VytMvHRZwxyWaXA9O6dWZZ9ucL8ZPwmPSchaR5TY_vfATnNCpWgSQPGP7NRMnpDQajYoJ3zYQlrQGNyZqgIZRmd201Mc_VzGHL5oLZXh469RDMfkNM91J65AYonNT9EAp3JRy_G_64_OkI4oWrSOLiRwAwUHa-aEoIVj4gQDHvq1g6K_ZRd_kzzq5SJACuJxcFNH0-DCTCKiOD1SWT1cYW8sKAGaZ_TvD988nLQ6w_28MFXoY3Du5_mLNa0glT7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی: زیاده‌خواهی و عدم صداقت آمریکا مانع حصول توافق است
🔹
وزیر امور خارجه امروز در دیدار معاون وزیر خارجه نروژ رویکرد زیاده‌خواهانه و لفاظی‌های تهدید و تحریک‌آمیز طرف آمریکایی و فقدان حسن‌نیت و عدم صداقت آمریکا را مهمترین مانع برای پایان قطعی جنگ و دستیابی به توافق احتمالی خواند.
@FarsNewsInt
- Link</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/farsna/435222" target="_blank">📅 00:19 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435221">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b12b97a7d.mp4?token=hcMB7PGIgxttSG13WtPK4cgTbOmowcc5RrU2v2W0tyTnVldQOYgYfczeGB4dCdRJ3pa1KB6zJ2HXPMymT3QtMyt2ZR17cnU3L8f2_c2aFweLNG_7AnMAnoFdA3LgT87EkaGLydy5MNcPRLVXvPn0kWq2WwtHwtAw_TqKQG0RZ2H6QXgENzkUy4JqUwji1z1lO54LK_uXx4uxbzsmrBWAapXij9TR7SmU5wp2JoMbgwI4IK4V31H85ztxySfyIFbst6Dx8A38rYdl_xn56flsm4NQlmvdxnHoucYSSu6Tiye93mEHQSEHw4IG8KLBaz6QRKi2FdPc4PW5cm9zvOfBV3peIDx5zj8GRW3gNbrOLzblg0QrhOLhLf_Pzj2kDkkai9-H1Mri-nRS2Dhql4Tt56ZoZw2AFjD1MkJWyr7yEVHJfK5_bn9tM0MntlVTW6yGM4Aa_wl2euwQfWkLmvfQkjufJO7JMgZVV_F9sE_K_v_yAjrvhMjfmTr3PMb7eE93EOmmeaDynkjp4zB16OehcdVfkJ6YtX2NtpqGCHaz6u_Fo-5L5mr5jNVF_lfb0f76s938slRVjsoPO-OLj5P-kKouWekewTOCB8h3_A8JgCwjSTi0TltMnC45hWDwypZv-x5VMXnAvVb8iSHoGwjecB8qujD7sjRDSJcOCPKYvVU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b12b97a7d.mp4?token=hcMB7PGIgxttSG13WtPK4cgTbOmowcc5RrU2v2W0tyTnVldQOYgYfczeGB4dCdRJ3pa1KB6zJ2HXPMymT3QtMyt2ZR17cnU3L8f2_c2aFweLNG_7AnMAnoFdA3LgT87EkaGLydy5MNcPRLVXvPn0kWq2WwtHwtAw_TqKQG0RZ2H6QXgENzkUy4JqUwji1z1lO54LK_uXx4uxbzsmrBWAapXij9TR7SmU5wp2JoMbgwI4IK4V31H85ztxySfyIFbst6Dx8A38rYdl_xn56flsm4NQlmvdxnHoucYSSu6Tiye93mEHQSEHw4IG8KLBaz6QRKi2FdPc4PW5cm9zvOfBV3peIDx5zj8GRW3gNbrOLzblg0QrhOLhLf_Pzj2kDkkai9-H1Mri-nRS2Dhql4Tt56ZoZw2AFjD1MkJWyr7yEVHJfK5_bn9tM0MntlVTW6yGM4Aa_wl2euwQfWkLmvfQkjufJO7JMgZVV_F9sE_K_v_yAjrvhMjfmTr3PMb7eE93EOmmeaDynkjp4zB16OehcdVfkJ6YtX2NtpqGCHaz6u_Fo-5L5mr5jNVF_lfb0f76s938slRVjsoPO-OLj5P-kKouWekewTOCB8h3_A8JgCwjSTi0TltMnC45hWDwypZv-x5VMXnAvVb8iSHoGwjecB8qujD7sjRDSJcOCPKYvVU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بروجردی‌ها و حماسۀ ۷۳ در خیابان مقاومت
@Farsna</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/farsna/435221" target="_blank">📅 00:19 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435220">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SDKUvGPM8TbQS4KXGZPpvvA4tU05DPS6iOVI9eL73De9bikxKuZ0HbKgdButVcwA55Ie2cYIU4LVba2rZYY4uQ31_9T9t027xk-QQSDGVVMGoiie39dZyJKNzW6P6nybzmV8GcngYgQ5n9YdrUktT1N0VcaqFzi91QpanoaOeBh4-w8RVQuIUG097mlclIWwsadEGW6lyg6EWm9AINgV8IhjUdkAYPtD_L8D4JxD6tOmgIDMVznCmkW5fepBFhyeZiI9zPbOsymL_37y9-sXae90RT_WflFkyBg1kmo3TjubprdVCPF5wG0a7XZk_TDP1K8SmB8ALtLjv2rOsPC-Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکبر عبدی در آی‌سی‌یو بستری شد
🔹
مهران غفوریان از بستری‌شدن اکبر عبدی در بخش آی‌سی‌یوی بیمارستان خبر داد.
🔹
فرزند اکبر عبدی با تایید این خبر، علت بستری‌شدن پدرش را سکته قلبی عنوان کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/farsna/435220" target="_blank">📅 00:10 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435219">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
دقایقی پیش زلزله تهران و کرج را لرزاند   @Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/435219" target="_blank">📅 23:57 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435216">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
دقایقی پیش زلزله تهران و کرج را لرزاند
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/435216" target="_blank">📅 23:51 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435215">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس علم و فناوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KjBbDHzzsBQ0Wd8LpsUE7PgJgU8xViuUi9U7BKhRJC0PkNbW7gOK6YqWQbdHi_rX644YSxPj1m3Y2Sl4qpC6yem7bm5bCTZBpTVgxITxwdc38PFhnlVfHFUDly5SE_FH108Z7yU2FO1Y9cKNNZKM9iR2zVWV9IZqute4tdSSbBKCts_8vzcSgLGKUGJ5FfVpV7fYNzJNDWttpXpTvNyjYJHhuxmAKE_tUMdwhMCCHL1wU4CBSSh38U25C168cVLRslGrEJ8ztxFZGlOXFRbYvN4jeKPP1vu5S1C1vY8oAKd6y8KJNH1vj0hhG3g0cZFnUONW7e1Vr8F3A5MBUNgSSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استعفای مدیران مایکروسافت
🔹
شعبه اسرائیل مایکروسافت پس از تحقیقات داخلی درباره همکاری این شرکت با نهادهای امنیتی اسرائیل با بحران مدیریتی روبه‌رو شده است.
🔹
«آلون هایموویچ» مدیر مایکروسافت اسرائیل پس از چهار سال از سمت خود کنار رفته و چند مدیر دیگر نیز شرکت را ترک کرده‌اند و تا اطلاع ثانوی مدیریت این شعبه مستقیماً از سوی دفتر مایکروسافت در فرانسه انجام می‌شود.
🔹
این تحقیقات پس از نگرانی‌ها درباره نحوه استفاده ارتش اسرائیل از زیرساخت ابری «اژور» آغاز شد.جایی که طبق گزارش گاردین از سال ۲۰۲۲ حجم زیادی از تماس‌های تلفنی فلسطینیان در غزه و کرانه باختری ذخیره شده است.
@FarsnaTech
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/435215" target="_blank">📅 23:45 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435209">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UHWmTK36WTdf_Q7knYPP-iJn0dvfhGKkQcZ0fr31Qh61tA-jHF6kwv1SBsYNTWb9d45jfoYHSPbE_v7jPbceU2QI73BalLt0xZE6p7fA_iAqmA14k0pWQnAuo-SBN452bAyoxvCk0z9cYMrxpXKzKssF9WZfrWUEUPxGm2AnCKixjLOfkOnAGZCiZYW0rbsBYZj-AfeaqRO6Rp1wzRfdsT-6g09G27lrHMUJnSTyAeY9nIppv6MWcm1SdqTYT4lRvqyGjxAY-0-EgG2SGR5DUr1F0UMoTxduqn6uIigMW3IVdsEqHVCpG5kihrWBF0ib_sGiGaTsMwAfReUjFElHpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PVtbvrydi8O_uMLUFXXbeP1qLWCl9q81yPY6HiRZPG7zACZen_VW_gGz_M1T9lo8IOz5YMXdJBzXSsdzfpz0eMkM17pFoksscFzmebGdcdBZtN1jYWnY1GMTxiu9mlQqiBDGKNpQasKaBukqQ2vfnNkbAt-5UW2TvhoXQR3nstOlFxP_1w8EMrLGEHfUTdPEHuaPVue61VUd7vlueK5rrFlGq_f3a0Pf6G4iBHyW2HcGp5H5v-EXMhKPuYkHUszOpKVlWJk7mCl3awqwC3YbypB0je-j1JzGPiUKt9e_WMYgmxl6aZNHiEloZMxpy5uilGfj8CR5W9GchbxueH43LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t7uc05pXXGkaIAp0_22uZLWy7Puki5tuw3w069eFkxeC12gQt0gQSlhJU64zv33Q5eBrd2pSEYj1aSrPinK8TVCtGBNoKLbx7fYpfze3TFvmau5QcD1_ya4rXk7edWgtxY0MN6VokekGV73hkLswj-nQXXkYGi7WDzl7zynJUlVG0axKEUarhyif7iRW4mmm66VtXJ1_x3U-Fe2QhbISt5LlujL6d3b2UoO7c8yGSsXEWYwts8UXks8abonjYZ1qXzUmonP7UDXOF_XqXG3DA6LvtSs-LcaLxJPiY1QpHSft9l3gFRlqUay2yPmKYfefE2XbIKvevBc8qm2HT-k_Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KLWoV5SxsSNG_vyXkMDArprFxbVTMBJjPqrL-IZY2-Xl1_xpBKuGHL3MG7ZYekUL7eCGwIq6T9lOB24FU7Mk9NFFWnrNlORkF9UQVW3MFUy3tNutDvNgvDXzKf7L498eQ2y1BJ9cVebtjsNGD8B03692BlfD8M2kvVxriIGkO9ONDosb9MWovKjfQOvEOput01rt7PwHSXeVrfuHYJmDF_KTnAjLLUABGXZpYMyYXMR4kEszo9Jz58cnKbb_ygO86tqFS0WBGJ2khysSZ-XU31O4DuQuFs_8mBMENycWKFGBO_sDHFuwIXnUtm6aHoQ_Se7HUQ0FAJM1YWb_zFvaUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h9gpXNx7JfqHHyRVhW5dPCdTQU4CSx8cWeAOIMnXpd6SPTq_Ly5fDJiJ8FtPuVN7W5x8KDspPtrIi28KVo0mCa7pP6pg26JYL9aD99a76vMguWde2bxfRIlnpSHs1qpzc_rhy3Bu2vhqEaLZgLi_D0DXeaASiWN-P1Jh3ZYCzd_tRq9k6iPIvWtBktY5JpOFw07GknUxmMQBUt5gAAPzgNK44MtR5mO_d7sm9nYTEVzlNVj3pro2CFalq_xmd5SqXmNpfDzipjHRUdSrIf-ZUN0yzpmeMj4KZhREfEMQPJZvzbMOWl4nhS7dxWOlKQiLCsGnaDOCg1bLIQRxOA_WSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HgqydFS3BG1ev1N6YAi2hKP-cJJXsLk7qwyeKBxTHMWUTqysny2ynXrcD3gGLRFo9wUKuPJTGFVm09FcWqwhYlI07WkHP0eSpMesuSJ49FpKtsBVKhVweKXUfew92MZ3QZb46w4RMJ3EGOSFntNHbtlxaxwDKjKLHZQ3ViynqKmpcGwKoBAodgcTeIjfubcPu4lVW6NRnBaG2hgcyFSObnZep4fvt9zfUfmGOqVp7bbdu_FTh0lEjPDKonRclFJdTgICnPIFtK_CajcnF6b59xFyCaE_79pQ1-JxPNCyk5apjs5cVmLy2Xbel0KS-Oi_dyhKgNiy-7EE1D4yqLASyg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دست نوشته‌های بندرعباسی‌ها در تجمعات شبانه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/farsna/435209" target="_blank">📅 23:43 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435208">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beee3a0abd.mp4?token=h31xP7VPtqCh9mb3ZIG51-eapX_6sRz9tpilsrmaFy_g0AYORSucvcPz2jLOkSaVUpHt0_aOj2kLSFcSC_D3XhfY6gs1qQenneRkDuRQ_npYBTv-mnXFphT-uvANhEPocLJU3CA3KJjqeT08DFkkOiYnr9TBBPHSIV3scxvhKqBryyccm1iO9tzmGMwuEs028aHlH69TIvYPnoJqyfrmR-2PVdjmrtvQYP4hwVG5NoKXdx2AP6WygmEGpc8bXUZhDHa1G4QOLqthPoKjrn5hMzyhPKtASGNRhWT9m2oHFg6-90hayi80RX9oViD67eDUdmlidi8bOhcQFe2WLxMFfnPW8i1SZ19gP5AZdsRTrsMa5RpppQzrPNArHe9uqyKdufCEgTCCsRGaDUqiYVFG4O45GxI_RhfCj5SzKQ8E9FXLBAyjdSqeVqh39iE_KKbl5sNRBbDPD1D8VSCs9K1zQ26oSWxN38BjoyuXHe00c1yjwPJsTb292LbXtuMiavVG7aSnj26UADSnT_T6lHITseTjiMApry6inUCEkw03yq5A6fuulG8z8fUd70Hy9IyspdH5KYzboR1aMvEluKH5LrfNa9uLdjhFLuworU1DAyh6biiLEHj75aIPWKUYyO1OI7JMXRrXBvPnEj9RTZS9GvnA_h0gekFqk2aT-ZUQALE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beee3a0abd.mp4?token=h31xP7VPtqCh9mb3ZIG51-eapX_6sRz9tpilsrmaFy_g0AYORSucvcPz2jLOkSaVUpHt0_aOj2kLSFcSC_D3XhfY6gs1qQenneRkDuRQ_npYBTv-mnXFphT-uvANhEPocLJU3CA3KJjqeT08DFkkOiYnr9TBBPHSIV3scxvhKqBryyccm1iO9tzmGMwuEs028aHlH69TIvYPnoJqyfrmR-2PVdjmrtvQYP4hwVG5NoKXdx2AP6WygmEGpc8bXUZhDHa1G4QOLqthPoKjrn5hMzyhPKtASGNRhWT9m2oHFg6-90hayi80RX9oViD67eDUdmlidi8bOhcQFe2WLxMFfnPW8i1SZ19gP5AZdsRTrsMa5RpppQzrPNArHe9uqyKdufCEgTCCsRGaDUqiYVFG4O45GxI_RhfCj5SzKQ8E9FXLBAyjdSqeVqh39iE_KKbl5sNRBbDPD1D8VSCs9K1zQ26oSWxN38BjoyuXHe00c1yjwPJsTb292LbXtuMiavVG7aSnj26UADSnT_T6lHITseTjiMApry6inUCEkw03yq5A6fuulG8z8fUd70Hy9IyspdH5KYzboR1aMvEluKH5LrfNa9uLdjhFLuworU1DAyh6biiLEHj75aIPWKUYyO1OI7JMXRrXBvPnEj9RTZS9GvnA_h0gekFqk2aT-ZUQALE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نوحهٔ حماسی کریمی در میدان انقلاب: «رهبرمون هرچی بگه همونه»  @Farsna - Link</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/farsna/435208" target="_blank">📅 23:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435207">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bd2e9a41c.mp4?token=EnXQ9b4PRRushVtCQ3jbN5fz-geVbuGo5DfscQx1lc8sTV8WzTbGlLA5EPMfuf3zklEXsibtUIbN_Lp5i6bG_isy-sXyIpO4jhVrQAgx8Kl8gfQIRG7057Y3mHeWKaVVMKIiEj5df69Hk-Pit2NG4Dzm7hUvX6aLvZts5tJH6jDCXKSfGbgZ3FHdMhdGPJSpxx2wjT905iSZhUMbbZ2LxDsp06zn9H75oD-tl2PtkVDSuqEHLAlm7iQcK-JbdgoFRwesIFOe-qdFI2rKYnCcAdg1OwZWCKPvwqOsxyjezJYUC9oTHtyxz75iQjFCZcbjZ-LAkHH1vnFhTxmTEs7Upw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bd2e9a41c.mp4?token=EnXQ9b4PRRushVtCQ3jbN5fz-geVbuGo5DfscQx1lc8sTV8WzTbGlLA5EPMfuf3zklEXsibtUIbN_Lp5i6bG_isy-sXyIpO4jhVrQAgx8Kl8gfQIRG7057Y3mHeWKaVVMKIiEj5df69Hk-Pit2NG4Dzm7hUvX6aLvZts5tJH6jDCXKSfGbgZ3FHdMhdGPJSpxx2wjT905iSZhUMbbZ2LxDsp06zn9H75oD-tl2PtkVDSuqEHLAlm7iQcK-JbdgoFRwesIFOe-qdFI2rKYnCcAdg1OwZWCKPvwqOsxyjezJYUC9oTHtyxz75iQjFCZcbjZ-LAkHH1vnFhTxmTEs7Upw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کودکان ایلامی غزل ایستادگی و ‌مقاومت می‌خوانند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/farsna/435207" target="_blank">📅 23:32 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435204">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🎥
حماسی خوانی یاسوجی‌ها: «اینجا ایرانِ، کشورِ شیرانِ»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/farsna/435204" target="_blank">📅 23:11 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435203">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c4_jT1RnGb9pL1rgwYIlc-o-acJkjl6SSSeJrNUEEAOxLL1-PoAmV-s-T4i2drMLi2hwq4qK5uupHU13x-qEw1rJ7gitgEn0LiKUo0WZTJg0tBCJflXV0zv0A4o1KBrN8G5iIyUiODCwy8Q-wYp5DSRRzlx392AfYNu-EJFvDTcLloLrTV0kpYDbMWuGO9Fmmr_RMuLd9zhBbfrONbyxbaMlIX1EeF8PwmohkSqOgOOs55QiopcMowduIbP-V067y1ZF-wYZecHih9qWDYJ4osxijMvByQHjGydmU10AreNexrPzICXFxtXTzVDG3oR_GxC9Q2USqED8O-uTNccaCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کویت سفیر ایران را احضار کرد
🔹
وزارت خارجۀ کویت با ادعای ورود چند نیروی سپاه پاسداران به جزیره بوبیان، از احضار سفیر ایران خبر داد.
🔸
کویت مدعی شده گروهی از نیروهای سپاه با ورود به این جزیره با نظامیان کویتی درگیر شده‌اند. @Farsna - Link</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/farsna/435203" target="_blank">📅 23:10 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435196">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N4THHNgcmUklNz4UmD03QvxoXrW0X929t_OiauftaZBhxlu_4WNFTQI_-TNBKNMe7wVPLo1ElxWdnr6QvdGSxDlRsadJzfagipe-yGHyOsQcBCzbq6Rqvaz-oSgGUfaV8z4wy8QylSTXpzRZh80SM2foh3eqdCRnq6_wHf5OBqj9DTW6_BbAFv5xJBvBkH0eanF2iGSOJ6Dy7OBYxBRpDQc61HvY50BSERdFgIRXlmJoe0YGPbiep56eCATfLctZ5IDrv3NehhDM6lSBO3xjPNXYyOwrX460rr7Uqc2vrPoYqJrIa5ZnZHraCFH4689l6Xd7emlfFAjQPpUPyAACZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K3a3Gl5Wn5KYr9QgL8qj_ALiObNIGeFdBd1yjvi7_aTZsMTSbIOWRH5sI6H5y1secCQcXNpzbTLMbtM0fO44ZJSoKLC3QNE8Jelq0LsVdBQSLO_vaS3A7EqZ1tU116os1A4YiFhwDA7dfP0Bgx2oUTCh1qF5PIroY6VHAHrRda7UJtTpupznUWKVzwsa1qE7xRpKZdLnUV9GlSlJ9V8_7A6a5pe3Crhnb76ZmudLj0a6QQJGQSLULwgPbglyQLCRVCLDaV30xVJSyU-MRyTRr-PnHpG_N93rIxuASd5lRWA9OZlH1MsmqewvBGDCjE7AbHy5lrCyR0Hxoq1q5tVxZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rqNnmuBelJ1fg-qvTDTZjo6-roL0qveCCkmVzg6WSQuD-xeukZJVmqLL88Phj6IyDsNRwUvrrV6Sx5wRA1ms7Qr__0qu4tL2hicnrGlDNNYfZUvWYsyzo1rFRt3q0A5oRDpMIxnk4gI-Jo82JsKUKpVces4Ivj5N-mmYFUAFW9AWaFOnt1kFpKwZ0ueOC5hsJoXY_ap9U51UFP-LIym24UtgTVeeGD_xfzsuq39ODIP1zv7vlBFb2-I4kuRH6EP7wOmzrbI2sKOk7w0o67vdlj7-DuOaZuNAKWLM_JHrWhQ3uSYW79k7F2bejpKAjnqPRL8SBrq6XLKkGkww4da8Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HoU1zPsbrwqCoHf9kvrAR9zCKnsyfLbl7wsvNAE-KFy1UGu2eqH-gxcpx4M7ZazYuFEOYql2hIJLMnd8SI0lhkvgI_utiDSmpmEs-TqDGNSA4q-P2y-I0kz7bSVga2AorkgqcK44zr1A6PPcBjA_-KRid0wpLA6j7ANnefBQr1EE2J6G-MOztG9IuF_Mh5mPfVGHt6oXwS0UsdvXlCGE7Pf4UKcNFWQctV4AQ1TnBSaDx8f1xKZtHQESffwE2zUrphgUbytVEAE9eCJmv-8pZ72fHlOuuvPAirOT0Eqb2zYwYdQz3FHyIZuJZgqDvJbIKCV0jrZA6Uu7C0M1i9MKjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/THOmQoNBtDWwfi-ZFdUvpRDDAzLnAVgFbjVUOI-S5drh5-djCWcoGxI13_F-VI6eYN9bJ3LNXDMMre-0FLLE8v4HAxZsUiwQUn_QPpo3_sjEeeYVOoF0euhPgPesQ-chDLG4O0Mn3pl2a-6FC4CneL0jI9ypxDXLujxl-z1eDhFWR00IGHLaLcp-HO0qy97BnLBFb85c8fqjr9zM9uQ7G-rWLPzi2XFW0rSsqnVZYCkwFteFI_6REMby61TNrNsDhKq1wsc0z_S0wFFNfuptYolkX9Q8YbmQDQxPsAYz9mFOYQIfwKHUOalNYE_gyOfcuJeeEXTYMU_y89cCUsth8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sLto07jQ1kQ8pRKbMv88A5a-R-dfMGNzTNIgM2GN47CT9VgHCN87iJv8GOVLyh02VtGQ_gZ2yBqePVoCA3VU4AzC0FHBBlcS49F5AGCF5WBMpTmi2OL8z2WNG1TK5_pJhKyq9G4gPkHgmI0jci9fo39KRthD7Yhj5e3MrUnVi1VYBodtUF1VB_tbQ2bSmQzKvhRRtDQFig8WbfNd_OXEXLNIO3XeDZYpkqmaAIh4ZlHv3x8xR3XwbgzrhZQlTz0jIgc27-sLcS03zMELX5L9tZeVVDMX9sVrMuZZWbrwMOv9pvUo_QYiri9SbBdCHuBnJdgVH8DQG-rqlOQyKENy_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bnt4-inlt_T4ZLr5mDQCbV8jOTB2vr4RyB9S_LBdNmV9Z0vsr_u2unmg7Pb-Cc1ZMpzolIqs-HFOM0mOFDYD4rcC-LyY3NGNRUoK8a_dPPrxq9CHFe8JU-WBBxEk4YmvJUhlXU3DcwMdVr0LHhCYshKBVi_qLj6K-3Eh8L-zTe8UkcwGkCeY4QNWZV-6YibUtVWosQrnpZYNUw-JFi8nnf3fpTtBFp6X4VKHk8veTWA8IkdV7SRkI0zPFSgbvPeiC7f73mYqyrMnTgBV6F1qpPFKJSEJwHxhoyvfTY5bVuYuf_tEdCDPooDlR9S2iwYI8X0yo2M5PMrkiQwRrCrxjQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برد پر گل تیم سفید ایران مقابل تیم قرمز
⚽️
گلزنان بازی: علیپور، ایری(۲)، یوسفی، حسین‌زاده
⚽️
تیم سفید ۴ - ۱ تیم قرمز  @Sportfars</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/farsna/435196" target="_blank">📅 23:10 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435195">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ceec062a4.mp4?token=s4NZ4ghVNC1UnZl4z-1P2zSPB3QpdNSk558yh19xSBO2Q8I4VjCFta91gTgW8UEGc7F-vU2O9ipCiCl1VVbPKWqX4xE6efRQKZnsV2fmx4D4G-wv2YfujMpq3A3GHaAQdnlvz0ZE1nrwp7XpNJfWq-9QpYVIonwf2IQun9M338MTaiSpH_UN3vdBtkCcu-kXKXQY-QyXCpKSPjW6AZBlXAIBmVn7_QgTaRMXuzv4UVIEP0drj1Xw4SH5ws1s6x7QbRvA-uN7NzBFOmbT-ZGOEpHaE9sJ3hqiru5bQfPH6qIJzWS5ArbTTgNquWVHmKwmP1CU6pNB1twKdBxlxradSJRBRhXBpA70Mve2Bkuu9ZotHzh3tGag5LPQEnorSZnGZ3hBXbFzev42MnP5zybQC8c53lt_4glSzNd1jU-AUPCBm_EWdin-e1i-QEjWnO6FB9QSJX96XkYV00y4rF4hbO0glXKk8f0KEfYq0X8zDZppsG7bitNdSTykOjlX5FRJAxCoN0to3wzdCocPbZFmI9mkeTs9DQjfKbS_fnwf5G685Zl1rndQK4hmUpY1fce43xf3wPD9iSJnNyikmtCcf7lmN4ZI5Yu8L3w0T_xv9RV5Gya4jPu_PxS9ThZr8DjGsn6Zd87fHAXGyEs-4Dauk-46v0mids3J-yYCff4FKoI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ceec062a4.mp4?token=s4NZ4ghVNC1UnZl4z-1P2zSPB3QpdNSk558yh19xSBO2Q8I4VjCFta91gTgW8UEGc7F-vU2O9ipCiCl1VVbPKWqX4xE6efRQKZnsV2fmx4D4G-wv2YfujMpq3A3GHaAQdnlvz0ZE1nrwp7XpNJfWq-9QpYVIonwf2IQun9M338MTaiSpH_UN3vdBtkCcu-kXKXQY-QyXCpKSPjW6AZBlXAIBmVn7_QgTaRMXuzv4UVIEP0drj1Xw4SH5ws1s6x7QbRvA-uN7NzBFOmbT-ZGOEpHaE9sJ3hqiru5bQfPH6qIJzWS5ArbTTgNquWVHmKwmP1CU6pNB1twKdBxlxradSJRBRhXBpA70Mve2Bkuu9ZotHzh3tGag5LPQEnorSZnGZ3hBXbFzev42MnP5zybQC8c53lt_4glSzNd1jU-AUPCBm_EWdin-e1i-QEjWnO6FB9QSJX96XkYV00y4rF4hbO0glXKk8f0KEfYq0X8zDZppsG7bitNdSTykOjlX5FRJAxCoN0to3wzdCocPbZFmI9mkeTs9DQjfKbS_fnwf5G685Zl1rndQK4hmUpY1fce43xf3wPD9iSJnNyikmtCcf7lmN4ZI5Yu8L3w0T_xv9RV5Gya4jPu_PxS9ThZr8DjGsn6Zd87fHAXGyEs-4Dauk-46v0mids3J-yYCff4FKoI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر اقتصاد: تیم اقتصادی دولت با وفاق و همدلی درحال کارکردن هستند و تلاش می‌کنیم مشکلات برطرف شود
🔹
دورهٔ پساجنگ ورود به دورهٔ جهاد اقتصادی است. @Farsna</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/farsna/435195" target="_blank">📅 23:08 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435194">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35693b9790.mp4?token=vqgZt1IBgUBsoaRIs5pIH8xQovRYSD1xI0IHOyGAHlsOm_FOjJHeM1-KUUmOoxQMd6HkUSIpdIIgMs049VekDb7DnnNrK2Xtk3jKVvdVI0QyX2_P41_PFFsh9Ec5esZAL1szKPNuE47cn51ghRluggjKJa3jVzVB8aaHzc4F8MelrSeG3vl4MGJHfvgxJpn8XPm-_IaSyOAXjJSSSUSXykk5oVD_9qkEouMO7VlqHYsKNZUDQV9uHoCUbxAjx9-XWgzK8s0SMLdvQACt4_439KCBEKAENaeClpGdES0eocEfiUBXkn2JSXBnc_Uf74BBYm1E167z4r7K8HdPIhBCOyq1gijeu-vnzHUSmO2zuis5MHmhop1mA4p6HUXVUYVeFPRHLpBBZNsUqfRLvXN3HMMDh8MzqtjxWIrh8JDSLh0Lod6uYp67Ykm3n9tAPJuIFDBWOIFaU_VrJVqpWEwIBVNa2oTSeMqBLL5TNnPv1ClHOpWweXgM_zm9ZzCYxXR07c5uue7kn80dy1XeTB9ZmHhnYWMbj-bAWGG8P7QPGsjfVX2abz6EqQYjh7YXZt7852ZxveEFlfF4rXGoUXGPnaRZsRTdZZI1dVxbFXRp7q9eIm6se1sKq2BHG5ZDIKyILe20YzxX76kMkOlZ04aXmpAUJsEe2B1j5kjCWP1fEzo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35693b9790.mp4?token=vqgZt1IBgUBsoaRIs5pIH8xQovRYSD1xI0IHOyGAHlsOm_FOjJHeM1-KUUmOoxQMd6HkUSIpdIIgMs049VekDb7DnnNrK2Xtk3jKVvdVI0QyX2_P41_PFFsh9Ec5esZAL1szKPNuE47cn51ghRluggjKJa3jVzVB8aaHzc4F8MelrSeG3vl4MGJHfvgxJpn8XPm-_IaSyOAXjJSSSUSXykk5oVD_9qkEouMO7VlqHYsKNZUDQV9uHoCUbxAjx9-XWgzK8s0SMLdvQACt4_439KCBEKAENaeClpGdES0eocEfiUBXkn2JSXBnc_Uf74BBYm1E167z4r7K8HdPIhBCOyq1gijeu-vnzHUSmO2zuis5MHmhop1mA4p6HUXVUYVeFPRHLpBBZNsUqfRLvXN3HMMDh8MzqtjxWIrh8JDSLh0Lod6uYp67Ykm3n9tAPJuIFDBWOIFaU_VrJVqpWEwIBVNa2oTSeMqBLL5TNnPv1ClHOpWweXgM_zm9ZzCYxXR07c5uue7kn80dy1XeTB9ZmHhnYWMbj-bAWGG8P7QPGsjfVX2abz6EqQYjh7YXZt7852ZxveEFlfF4rXGoUXGPnaRZsRTdZZI1dVxbFXRp7q9eIm6se1sKq2BHG5ZDIKyILe20YzxX76kMkOlZ04aXmpAUJsEe2B1j5kjCWP1fEzo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طوفان پرچم‌ها در آسمان رفسنجان در قرار هفتادوسوم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/farsna/435194" target="_blank">📅 23:01 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435193">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca283db5f4.mp4?token=saDX9HgWtiZlij4E7zqMAGdiQCjCanf1WgSh9MQ10Z1lSewuuxVh13t0oMZRLFzYFbnZYS-1O5SAdepSg-WyjJi-s9rjarWX89AIEgOpFHW1EY1u6AtS2L1yfWKUqcKvbZ60jAvVH5vvF8z643wcTKETSXVt_1niXXHAbuZ7S8dATKMDb0Er1gPAspEk8V79Q4bKus6FSvqopLj_JOHBuedsOq3zExi62Mp6bZ2Lr20yBBp860HfqHl4xDrxs1flmdt6E7vTyi3kE_EesDE-8e-z4yJLxkAsv534xUY9cYmlTT8Bw4WsIbB7EqUK3gz1HQScZh90TpKovUj-rEjwQVApyVylgGqkewxO_vnGtap9N2ZgcjX7ZDPBLggJzzgvvRbNYZA5JGqUtNXSX_lZ2EghZclI6Wb8wvQtlxSj8BxUwKPns7TOpbzXof-q1n7_N3UCCPIWts2nSt_BnVbiUVvAmPUvKM4L99EYJ1pmBuBTZOhzBHDrTDZsVVuX_XxfyUV3NDNSOID4xLiPWYCsvgWTGbOdt_rsR-FpGiQFBHPRNCS31fSZwjDKa3bDpWqGesExr2_vpvLW7CDNXRnOE6nDSn9DrP_xs_C7WVvv6gEwo2IdABAtBT8lRU9p33hZDnEFBcx5HmbmaN9YAPAPEzXriqS2lm_uXb-cuFbx2zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca283db5f4.mp4?token=saDX9HgWtiZlij4E7zqMAGdiQCjCanf1WgSh9MQ10Z1lSewuuxVh13t0oMZRLFzYFbnZYS-1O5SAdepSg-WyjJi-s9rjarWX89AIEgOpFHW1EY1u6AtS2L1yfWKUqcKvbZ60jAvVH5vvF8z643wcTKETSXVt_1niXXHAbuZ7S8dATKMDb0Er1gPAspEk8V79Q4bKus6FSvqopLj_JOHBuedsOq3zExi62Mp6bZ2Lr20yBBp860HfqHl4xDrxs1flmdt6E7vTyi3kE_EesDE-8e-z4yJLxkAsv534xUY9cYmlTT8Bw4WsIbB7EqUK3gz1HQScZh90TpKovUj-rEjwQVApyVylgGqkewxO_vnGtap9N2ZgcjX7ZDPBLggJzzgvvRbNYZA5JGqUtNXSX_lZ2EghZclI6Wb8wvQtlxSj8BxUwKPns7TOpbzXof-q1n7_N3UCCPIWts2nSt_BnVbiUVvAmPUvKM4L99EYJ1pmBuBTZOhzBHDrTDZsVVuX_XxfyUV3NDNSOID4xLiPWYCsvgWTGbOdt_rsR-FpGiQFBHPRNCS31fSZwjDKa3bDpWqGesExr2_vpvLW7CDNXRnOE6nDSn9DrP_xs_C7WVvv6gEwo2IdABAtBT8lRU9p33hZDnEFBcx5HmbmaN9YAPAPEzXriqS2lm_uXb-cuFbx2zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موج ۷۳ میدان‌داری عاشقان ایران در قزوین
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/farsna/435193" target="_blank">📅 22:57 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435192">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/004694a3d9.mp4?token=jTgySsyPbKABSKpoECi3zHp54LYSDGKeEuJtHp367rYofJlaLd3b5ogmtfczyVZQy1pAKjx7ZYBr-Q_srwmUnf8pOEubrK-58a3ICiznWKkheEM6oc7yqoCwFEZnNMvK6NumVLtlBtmC0cfDBqGvt_4k522Durp-G8CmMPyFo1Cwjl6IkwyUlR8OWY28F7lTonw38YwgeAzz848stjue4M-HF5A7AC2j73bA15Clm_mSeA7CPQiKDsrH8aa2y05hF2B5P2oMc9sN2CfmDNfAav7KQyibvJIW3h--77x2JgEWBZgADNu4A0ZPd7mi-nJAUYeCsaFt_PMGgUTmkrrjiH2fYkBFaXluw68EEM59YHGmil3P33FUSrumAmcLjyo92HTqCIOZ3o5AB28CD11vZdOhQYMd62CFs2L7qqHScUOLAv0RDSbeLpFHiQUZhR2cMPEis12WUF7wGVY1i7S8a7izWNuIKz98LILaZmeA4disKchUvWgOs1SRONB6t4IfU6tOJOEAD7j9M8_39yTwu7Q8j7EQJETquMuz_CNSjJgPqIJz2UMxMIAe28V8_wFW_4v9d9xtkK4CtOovum6xwTQ1IRuoqFw1LyEigVi7Cr1WQpvXY2Vp6Uaf-GvxcPpo6XNMAytnY7MLyGcz2gA67f3AOLE-84QmWhujguHXZV4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/004694a3d9.mp4?token=jTgySsyPbKABSKpoECi3zHp54LYSDGKeEuJtHp367rYofJlaLd3b5ogmtfczyVZQy1pAKjx7ZYBr-Q_srwmUnf8pOEubrK-58a3ICiznWKkheEM6oc7yqoCwFEZnNMvK6NumVLtlBtmC0cfDBqGvt_4k522Durp-G8CmMPyFo1Cwjl6IkwyUlR8OWY28F7lTonw38YwgeAzz848stjue4M-HF5A7AC2j73bA15Clm_mSeA7CPQiKDsrH8aa2y05hF2B5P2oMc9sN2CfmDNfAav7KQyibvJIW3h--77x2JgEWBZgADNu4A0ZPd7mi-nJAUYeCsaFt_PMGgUTmkrrjiH2fYkBFaXluw68EEM59YHGmil3P33FUSrumAmcLjyo92HTqCIOZ3o5AB28CD11vZdOhQYMd62CFs2L7qqHScUOLAv0RDSbeLpFHiQUZhR2cMPEis12WUF7wGVY1i7S8a7izWNuIKz98LILaZmeA4disKchUvWgOs1SRONB6t4IfU6tOJOEAD7j9M8_39yTwu7Q8j7EQJETquMuz_CNSjJgPqIJz2UMxMIAe28V8_wFW_4v9d9xtkK4CtOovum6xwTQ1IRuoqFw1LyEigVi7Cr1WQpvXY2Vp6Uaf-GvxcPpo6XNMAytnY7MLyGcz2gA67f3AOLE-84QmWhujguHXZV4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر اقتصاد: بحث انتقال کریدورها به بنادر شمالی و مرزهای زمینی در دستورکار ماست.  @Farsna</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/farsna/435192" target="_blank">📅 22:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435190">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1143c6c122.mp4?token=KZHMly2rHLH-LN2rnXfg5acj0H96GzZzEItfJRnLMv3bo2f7aX1F3n6ZPG0N5uHdgK4n0ip5PAAAr1Ux_oHBb0d3lBM4FVlgQEsBVY8GAkXzHsGrW_JD89sksyOlGnKLTiR9rSmDzXMcg9XaiGOyYOuMRlsjJeeu2HH_0Sh72blC0ODfod5LswuaMOn4RRxMSFnl4YrCYDZ7IjqkqHqB2gJ0vdMaSFkiSiCxwjHYig6e-CSOdepnCuTZRGbfCLNI8epzrYlroZczTFGgGlU8SfCp1z70e_9MZtnVb5xWyLF_fDv76kcMt5_RucrRClZlzw-hF4qBhoSZiVWSbUBzWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1143c6c122.mp4?token=KZHMly2rHLH-LN2rnXfg5acj0H96GzZzEItfJRnLMv3bo2f7aX1F3n6ZPG0N5uHdgK4n0ip5PAAAr1Ux_oHBb0d3lBM4FVlgQEsBVY8GAkXzHsGrW_JD89sksyOlGnKLTiR9rSmDzXMcg9XaiGOyYOuMRlsjJeeu2HH_0Sh72blC0ODfod5LswuaMOn4RRxMSFnl4YrCYDZ7IjqkqHqB2gJ0vdMaSFkiSiCxwjHYig6e-CSOdepnCuTZRGbfCLNI8epzrYlroZczTFGgGlU8SfCp1z70e_9MZtnVb5xWyLF_fDv76kcMt5_RucrRClZlzw-hF4qBhoSZiVWSbUBzWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر اقتصاد: متوسط زمان ترخیص کالاهای اساسی به ۹ روز رسیده و تلاش می‌کنیم آن را به ۳ روز برسانیم.  @Farsna</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/farsna/435190" target="_blank">📅 22:50 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435189">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03ed6ad1cc.mp4?token=jFbzq8eh3N85EwkUfcip51on0x8D6fOhq22kGymm9vvmnL1Kp3N2dKvue-yC4Q1orDKeN4Mmm2DSp_JE6PNZErYovFosBL4mLmAVpTcTh0IVYrOtZB1E4X7RnmuxqUFQIPsXXud7zy_U8r-1AxEfyeMB2kimyqbSzQdHcZVShY7E__1gGON7v3onlk9bMMGtvw-g72TE50rKtO0XRgKcrB5IcPk3jt9ONnuYWUZDnCwcqykCPsBwi0z8TXVsRody1mLQcsglSBbeibfQlyNpumcsnQUx7uZouB8LI678nVOuYjvNijEqTrwRJQ8SmWQ_EiOWF2hwkPlYI0rOkaih7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03ed6ad1cc.mp4?token=jFbzq8eh3N85EwkUfcip51on0x8D6fOhq22kGymm9vvmnL1Kp3N2dKvue-yC4Q1orDKeN4Mmm2DSp_JE6PNZErYovFosBL4mLmAVpTcTh0IVYrOtZB1E4X7RnmuxqUFQIPsXXud7zy_U8r-1AxEfyeMB2kimyqbSzQdHcZVShY7E__1gGON7v3onlk9bMMGtvw-g72TE50rKtO0XRgKcrB5IcPk3jt9ONnuYWUZDnCwcqykCPsBwi0z8TXVsRody1mLQcsglSBbeibfQlyNpumcsnQUx7uZouB8LI678nVOuYjvNijEqTrwRJQ8SmWQ_EiOWF2hwkPlYI0rOkaih7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر اقتصاد: کسب‌وکارهایی که تعدیل نیرو نداشته باشند، از دولت تسهیلات می‌گیرند
🔹
دولت از این واحدهای تولیدی حمایت ۱۰۰ درصدی خواهد داشت. @Farsna</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/farsna/435189" target="_blank">📅 22:42 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435188">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">اقدام جدید امارات علیه حزب‌الله لبنان
🔹
دولت امارات متحده عربی خبر داد ۲۱ فرد و نهاد را به دلیل ارتباط با حزب‌الله لبنان در لیست تروریسم قرار دهد.
🔹
ابوظبی مدعی شد این تصمیم در چارچوب تلاش برای «تقویت همکاری‌های بین‌المللی جهت مبارزه با تأمین مالی تروریسم» اتخاذ شده است.
🔹
امارات می‌گوید کلیه نهادهای نظارتی موظفند هر فرد یا نهاد وابسته یا مرتبط با هرگونه رابطه مالی یا تجاری با افراد و نهادهای ذکر شده در این خصوص را شناسایی کرده و اقدامات لازم را مطابق قوانین این کشور، از جمله مسدودسازی دارایی‌ها در کمتر از ۲۴ ساعت، انجام دهند.
🔹
امارات که سابقه طولانی در حمایت از گروه‌های تروریستی دارد، ادعا کرده تلاش‌های گسترده‌ای را برای مقابله با افراط‌گرایی و تروریسم انجام داده است.
🔹
حمایت‌های امارات از تروریست‌ها در سودان و یمن، بسیار چشمگیر بوده است که رسانه‌های غربی هم به آن پرداخته‌اند.
🔹
روزنامه گاردین چندی پیش، در یک گزارش تحقیقی جدید فاش کرد که امارات نه تنها به نیروهای واکنش سریع سودان سلاح می‌دهد، بلکه به فرماندهان متهم به نسل‌کشی اجازه داده ثروت‌های نامشروع خود را در ویلاهای نزدیک باشگاه ترامپ و آپارتمان‌های برج خلیفه دبی پنهان کنند.
🔹
به گفته این روزنامه، فرماندهان نیروهای واکنش سریع که متهم به ارتکاب جنایات نسل‌کشی هستند، از امارات متحده عربی به عنوان «خزانه پشتیبان» و پناهگاهی امن برای پنهان‌سازی ثروت‌های کلان خود و اعضای خانواده‌های خود استفاده می‌کنند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/farsna/435188" target="_blank">📅 22:41 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435187">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a58dc4d7e8.mp4?token=LchMulEpz3BS_PecmkMGAkQ5fH-HiVQqeUVckv3ssy9x01FzGWqHcl30eBFJUC2k0_oXwWF4YCNTdIDYE0jJhon0MkYxZrgH6I00b45bcfpG-K3t51AmyEf4BftTsPGWRV9tXnyjq_oStGZgxuJcXwxFZB6Ja2xBZfQht8veiP3FJAFfUlzEwuTvWHJtw5ujpeiaUa5AqLjt6Uz6h4Ml53HPUulIFJaIu2mLLdxUYiw230f4FvxuoDL-9W3N_enuVxhGuGmk335KGmWRSvJlvu4TicAPD077yzFqLxtzRLncR1Z248raxVc2VaY3AYU_YM-7H9NL7bULvrYNY-JEGptD9DblOhB4UG_8jQYKcOFF7FaBSpo2lyGTIDEGfoQY8q84OkBD9A4aMClbbzaDLZ9tPE_FncUJX-7jr5pBVANFTKtDrw4-d5fF4OgxHGnhOjVpZWSg7Owz6o6QRecm2YXDK7rinUEM7lRXYp2tW-za57MALPOTZyAP_fnfMDSnVr_NV6EB5bHle6iIszjpUuBxQHb_NUg8ytEjr60GMNm67IPFZtwyIySAfbtFZfhK15XKZVQVF-YuzvRwFqglBbD0_4G6KeHgJz7tFx53cinJwxOr0YjfsZHxm1_GpyDOrgLNdvv5zOCU50loFVhRl0_n4vJ1Ya_o-oe_QEsq7Qk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a58dc4d7e8.mp4?token=LchMulEpz3BS_PecmkMGAkQ5fH-HiVQqeUVckv3ssy9x01FzGWqHcl30eBFJUC2k0_oXwWF4YCNTdIDYE0jJhon0MkYxZrgH6I00b45bcfpG-K3t51AmyEf4BftTsPGWRV9tXnyjq_oStGZgxuJcXwxFZB6Ja2xBZfQht8veiP3FJAFfUlzEwuTvWHJtw5ujpeiaUa5AqLjt6Uz6h4Ml53HPUulIFJaIu2mLLdxUYiw230f4FvxuoDL-9W3N_enuVxhGuGmk335KGmWRSvJlvu4TicAPD077yzFqLxtzRLncR1Z248raxVc2VaY3AYU_YM-7H9NL7bULvrYNY-JEGptD9DblOhB4UG_8jQYKcOFF7FaBSpo2lyGTIDEGfoQY8q84OkBD9A4aMClbbzaDLZ9tPE_FncUJX-7jr5pBVANFTKtDrw4-d5fF4OgxHGnhOjVpZWSg7Owz6o6QRecm2YXDK7rinUEM7lRXYp2tW-za57MALPOTZyAP_fnfMDSnVr_NV6EB5bHle6iIszjpUuBxQHb_NUg8ytEjr60GMNm67IPFZtwyIySAfbtFZfhK15XKZVQVF-YuzvRwFqglBbD0_4G6KeHgJz7tFx53cinJwxOr0YjfsZHxm1_GpyDOrgLNdvv5zOCU50loFVhRl0_n4vJ1Ya_o-oe_QEsq7Qk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر اقتصاد: برآورد خسارات منازل مسکونی آسیب‌دیده در جنگ درحال انجام است و برای تعمیر و بازسازی و لوازم خانه منابعی توسط سازمان برنامه‌وبودجه در نظر گرفته خواهد شد.  @Farsna</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/farsna/435187" target="_blank">📅 22:33 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435186">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">رویترز: عراق و پاکستان مجوز عبور از تنگه هرمز را از ایران گرفتند
🔹
منابع مطلع به رویترز گفتند بغداد و اسلام‌آباد برای انتقال نفت و LNG از خلیج فارس، مجوز و هماهنگی لازم را از ایران دریافت کرده‌اند.
🔹
به گفته رویترز، این موضوع نشان‌دهنده نقش و نفوذ ایران در مدیریت عبور انرژی از این گذرگاه راهبردی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/farsna/435186" target="_blank">📅 22:31 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435185">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7f724386e.mp4?token=pnXefLVBL27qviLgB7jFzoWJm19HOgZscLSXO_QGDVmxfeUY0PLmhK1a8njvgKeo1Rp8JlL_wLmvHlE8hJ3pVIh1hn3okXPjjueH5NQBfMUbcrYMmc34vd56h19sLYb5pozOTONe_GcMZECIKy_IM0yvTkptzaCFBn2Joa9ut-zej3OE3xfKCWwxn233POV5H869Oo_LHN58KoAtnROPEymsDXArZ8NzSqdMRhEu92Rt_Modff0ePoj78TYJlkaXy11_PNCoTWgrpODWnScZ0JMpsb2-le5Q5G_tqRqDlmjWx5Ain8tU0J_HLIaHsiRAUKmerDVbF9mmzNhLjoX4Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7f724386e.mp4?token=pnXefLVBL27qviLgB7jFzoWJm19HOgZscLSXO_QGDVmxfeUY0PLmhK1a8njvgKeo1Rp8JlL_wLmvHlE8hJ3pVIh1hn3okXPjjueH5NQBfMUbcrYMmc34vd56h19sLYb5pozOTONe_GcMZECIKy_IM0yvTkptzaCFBn2Joa9ut-zej3OE3xfKCWwxn233POV5H869Oo_LHN58KoAtnROPEymsDXArZ8NzSqdMRhEu92Rt_Modff0ePoj78TYJlkaXy11_PNCoTWgrpODWnScZ0JMpsb2-le5Q5G_tqRqDlmjWx5Ain8tU0J_HLIaHsiRAUKmerDVbF9mmzNhLjoX4Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر اقتصاد: در ایام جنگ با تفویض اختیارات، ادارهٔ کشور به‌صورت غیرمتمرکز انجام شد
🔹
بعد از جنگ ۱۲ روزه الگوی ادارهٔ کشور در شرایط جنگی را آماده کرده بودیم و بعد از آغاز جنگ رمضان، سریع روی آرایش جنگی قرار گرفتیم. @Farsna</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/farsna/435185" target="_blank">📅 22:28 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435184">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aymzVNRfqBALhKbZAYI_K71hpw_ewlwQUa-lcEi0-PVXqlXmgDfZmloosuGBy9hI_InJzvbDaljmmTnhc3My-hHXeBiPzDn9MygyxlSWeFlq2MS0nIxobbnEuj2iQx_vepaBqY14pzP2QSXRBvf4eFUQJksAot0W-GgnkqaWiVimEceif8qzFXs6LO_HpquOYPpRmtDLpwsjVSBN4N76MeQnC8cPA3rRYB_SloK5dsI1KSRgB0RuRPU_0hRyHw9TA4vZFx0Wd3Ivn_0pxh9iVmHZUrVYpDQHEtlri7XZMhsSDBQt73Pk_OYDmEJwe_gv1ibL8-6BTaioiXPip4vmtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۱ حادثه در تهران بر اثر طوفان امشب
🔹
قائم‌مقام اورژانس تهران:  تا حالا ۱۱ حادثه ناشی از طوفان تهران به اورژانس اعلام شده که ۴ نفر در محل درمان شده‌اند و هنوز روال درمانی مابقی مصدومان مشخص نیست.
🔹
مصدومان به ۵ بیمارستان امام حسین (ع)، امام خمینی (ره)، شهدای هفتم تیر، رسول اکرم و لقمان منتقل خواهند شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/farsna/435184" target="_blank">📅 22:25 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435182">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecd2c68828.mp4?token=QcNrNRMcfrKBfc_yx9xEpu4sODCel1Nls_qlEMzwEIP6dc-hKv8T_EKj6d4xlfN9_VRHZN-BO6gGlsLoH85rAlEvXf0u9sJ3PdrLjPZz1FWbeiXxURxXurOCq_R5lAikOSee4SYKxwF1DLi0penTa2JVUt9hIpcffYH-VkUgCk-1q1qr5F5-WzKtrZnJCGfdUVKjgsfL6ddAAxCETxizlX6t30AhtxDPEpWnN1672ihRwV0uhfZ_xeclpqLvm9H1fUxTygqgHtXEkSoSMmTyerEPR4V4IOqraXNkBolAvbZ3Qw6x_QKcWOfn8-QbHNdIM61cjJAYxd652bPzqkWByFdvSNaS2BkjBE8_TPlQSj07wLI840b0C1YSIHvAbHZTO4rXqIVs5AKi2ruBB85KxG-KRpzeqGzjdgYs0F4Ap3juIcSqbg_i-WO3TNOdJnQr4TsKrCCzuoJ4x8rq9Dpc6jYhFj4F8drFHxyEXWiis4pKFIvVqLAV6rHxV451yXMqxv7QnvR60XSE3dIYiFcotBOxr5YUbxpqu_Q7AXtqrMapuozZy0WcCH3spPkT_6mQlozyakhMsZFtF8TkakoxKcO763xrxLBm1mvBrBQ7Z0fiJ5vdUrj7d-UlWA603oiKOCTDZPztdE9ZaFqLxRfisrRuQLgMPBDg-xHEhI3pA5s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecd2c68828.mp4?token=QcNrNRMcfrKBfc_yx9xEpu4sODCel1Nls_qlEMzwEIP6dc-hKv8T_EKj6d4xlfN9_VRHZN-BO6gGlsLoH85rAlEvXf0u9sJ3PdrLjPZz1FWbeiXxURxXurOCq_R5lAikOSee4SYKxwF1DLi0penTa2JVUt9hIpcffYH-VkUgCk-1q1qr5F5-WzKtrZnJCGfdUVKjgsfL6ddAAxCETxizlX6t30AhtxDPEpWnN1672ihRwV0uhfZ_xeclpqLvm9H1fUxTygqgHtXEkSoSMmTyerEPR4V4IOqraXNkBolAvbZ3Qw6x_QKcWOfn8-QbHNdIM61cjJAYxd652bPzqkWByFdvSNaS2BkjBE8_TPlQSj07wLI840b0C1YSIHvAbHZTO4rXqIVs5AKi2ruBB85KxG-KRpzeqGzjdgYs0F4Ap3juIcSqbg_i-WO3TNOdJnQr4TsKrCCzuoJ4x8rq9Dpc6jYhFj4F8drFHxyEXWiis4pKFIvVqLAV6rHxV451yXMqxv7QnvR60XSE3dIYiFcotBOxr5YUbxpqu_Q7AXtqrMapuozZy0WcCH3spPkT_6mQlozyakhMsZFtF8TkakoxKcO763xrxLBm1mvBrBQ7Z0fiJ5vdUrj7d-UlWA603oiKOCTDZPztdE9ZaFqLxRfisrRuQLgMPBDg-xHEhI3pA5s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر اقتصاد: در ایام جنگ با تفویض اختیارات، ادارهٔ کشور به‌صورت غیرمتمرکز انجام شد
🔹
بعد از جنگ ۱۲ روزه الگوی ادارهٔ کشور در شرایط جنگی را آماده کرده بودیم و بعد از آغاز جنگ رمضان، سریع روی آرایش جنگی قرار گرفتیم.
@Farsna</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/farsna/435182" target="_blank">📅 22:14 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435181">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NVWkO2YrstraaClB6RwRJObIErenuLmhRbjodraXh5fyLaHE5ndelmK-x0rt-CnEPxSYB2E2UMewLvwXAcUG2yxGd8xCh6-b13X1N1C8a8tnwKMRh2IsBeW0enVqzfDAJULZ1LK7unfzO4HrgR1zlrZOHlZ4Q4vGDOq-8WMREj4pfKLZrflbT5zQPZ2YOrNsuz-O-PXE3zE0nGuQtMTEH7WE8ywaDRK1vFiDXKHoQEMNvuT2qmhxO2p_XZjGQM0mat5n4FHoXOPkEeG1wm5U0og8hC0j91B5z9ca1JCe7XwAMWBJDJX5Iy-zUW1wE6PG1DWsMwigzWVF7nG_Qr2rfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فولاد مبارکه مامور واردات ورق فولادی شد
🔹
وزارت صمت اختیار واردات ورق مورد نیاز بازار داخل را به فولاد مبارکه سپرد.
🔹
براساس اطلاع فارس از وزارت صمت، ارز مورد نیاز برای واردات ورق نیز تامین شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/farsna/435181" target="_blank">📅 22:11 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435180">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🎥
مشق آمادگی دفاعی مردان و زنان در تجمعات شبانه!
@Farsna</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/farsna/435180" target="_blank">📅 22:09 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435179">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🎥
هفتادوسومین شب خروش مردمی در مراغه آذربایجان شرقی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/farsna/435179" target="_blank">📅 22:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435178">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d473b933bf.mp4?token=Fzg8iVjLDkcaYHjWoSWf3wCnCJXno0euV1eDKXFqUj8PDbxd2Kp5FuRCcajr3Vr1dqRjo5dyvltUu3Jqm5CtIuDdIegUnr4SFxK1IIFpWzHBv87PGlCQV3tNZO44wmzIvwExdKz2fOp7WmPv54GvHhsnjXJJn0ilzy8FNBdb724nJOI9h6N0sIbxEpinBhSncMHAx25qe9kuz-C6_XBoB8m6X6LKSIt_MRXJmPrlaHD9JnON2ERLy14mFo4bHKlSW_L4r2gK10TUWS__IfgreRdZasgZmhf19ievExG6EahQ3oPJGoZ5qJOdvLII7iks1knerm2mfZXeJBWk7u6iFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d473b933bf.mp4?token=Fzg8iVjLDkcaYHjWoSWf3wCnCJXno0euV1eDKXFqUj8PDbxd2Kp5FuRCcajr3Vr1dqRjo5dyvltUu3Jqm5CtIuDdIegUnr4SFxK1IIFpWzHBv87PGlCQV3tNZO44wmzIvwExdKz2fOp7WmPv54GvHhsnjXJJn0ilzy8FNBdb724nJOI9h6N0sIbxEpinBhSncMHAx25qe9kuz-C6_XBoB8m6X6LKSIt_MRXJmPrlaHD9JnON2ERLy14mFo4bHKlSW_L4r2gK10TUWS__IfgreRdZasgZmhf19ievExG6EahQ3oPJGoZ5qJOdvLII7iks1knerm2mfZXeJBWk7u6iFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حزب‌الله ۵ تانک مراکاوای دیگر هم شکار کرد
🔹
مقاومت حزب‌الله لبنان: طی ۲۴ ساعت گذشته  ۵ تانک مرکاوای ارتش صهیونیستی در جنوب لبنان را منهدم کردیم.
🔹
همچنین پایگاه تازه تاسیس اسرائیلی‌ها در منطقه بلاط در جنوب لبنان موشک‌باران شد و محل تجمع نظامیان صهیونیست در شهرک رشاف نیز هدف حملۀ پهپادی قرار گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/farsna/435178" target="_blank">📅 21:57 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435177">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07628c1387.mp4?token=vP-BDvxTzN1yly0iJ7i5zqUfGHbGRi1p27GaiphhEP5_2EVuiSuyME_tRx2tdOrMcWVE4VZypqQ3dTepa-W3l5cSXZbAateMDDvGnzgWioZn5syeBFEHCOtmGB2ozvGvOSIIflpHhr33BkTvYkRrrT9vpZIVw85PeI-gq4go-4S-g8tYb_7T-36iyRtRhde6O5aRki8qMxNnVA52IWzsroCEpPtjUjaD_Eqf6sNH4O4FjL_t0wFvuubGfRheLkCQBFOms_Y6gEzoxaTtYzTbCs5YdvIrvRZ4ETxHi8fM6TYJB_nyMqNUrEAle9fj_3hJeWfAf7dA9E9Sym-9xM7INg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07628c1387.mp4?token=vP-BDvxTzN1yly0iJ7i5zqUfGHbGRi1p27GaiphhEP5_2EVuiSuyME_tRx2tdOrMcWVE4VZypqQ3dTepa-W3l5cSXZbAateMDDvGnzgWioZn5syeBFEHCOtmGB2ozvGvOSIIflpHhr33BkTvYkRrrT9vpZIVw85PeI-gq4go-4S-g8tYb_7T-36iyRtRhde6O5aRki8qMxNnVA52IWzsroCEpPtjUjaD_Eqf6sNH4O4FjL_t0wFvuubGfRheLkCQBFOms_Y6gEzoxaTtYzTbCs5YdvIrvRZ4ETxHi8fM6TYJB_nyMqNUrEAle9fj_3hJeWfAf7dA9E9Sym-9xM7INg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای تهدید جالب شهید
ناظری که سربازان آمریکایی را به گریه انداخت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/farsna/435177" target="_blank">📅 21:51 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435173">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">یک منبع آگاه به فارس: ایران بدون انجام ۵ شرط اعتمادساز وارد دور دوم مذاکرات با آمریکا نمی‌شود
🔹
یک منبع آگاه تأکید کرد که پیش‌شرط‌های اعلامی ایران، تضامین حداقلی اعتمادساز برای آغاز هرگونه مذاکره با آمریکا است.
🔹
پنج پیش‌شرط ایران برای طرف آمریکایی شامل «پایان جنگ در همه جبهه‌ها به‌ویژه لبنان»، «رفع تحریم‌های ضدایرانی»، «آزادسازی پول‌های بلوکه‌شده ایران»، «جبران خسارات ناشی از جنگ» و «پذیرش حق حاکمیت ایران بر تنگه هرمز» می باشد.
🔹
ایران همچنین به میانجی پاکستانی اعلام کرده است که تداوم محاصره دریایی در محدوده دریای عرب و خلیج عمان پس از برقراری آتش‌بس، گزاره غیرقابل اعتماد بودن مذاکره با آمریکا را بیش از پیش تقویت کرده است.
🔹
بنا بر اعلام این منبع آگاه، مجموعه این شروط صرفاً در چارچوب ایجاد حداقل اعتماد برای بازگشت به روند گفت‌وگوها تعریف شده و تهران معتقد است بدون تحقق عملی این موارد، امکان ورود به مذاکرات جدید وجود نخواهد داشت.
🔹
بر اساس اطلاعات به‌دست‌آمده توسط خبرنگار فارس، ایران این پیش شرطهای ۵ گانه را در پاسخ به پیشنهاد ۱۴بندی آمریکا معین کرده است؛ پیشنهاداتی که به گفته منابع آگاه، کاملاً یک‌طرفه و در راستای تأمین منافع واشنگتن تنظیم شده بود. به گفته این منابع، آمریکایی‌ها در این پیشنهاد تلاش داشتند اهدافی را که در جنگ محقق نکرده بودند، از مسیر مذاکرات به دست آورند.
@Farsna</div>
<div class="tg-footer">👁️ 7.5K · <a href="https://t.me/farsna/435173" target="_blank">📅 21:29 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435172">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37dea67a11.mp4?token=LqQV2_yVvCsjdzJfuqd_Z3aYWqNNzIp7ujeVBOQ5w8v-abJzbRHQW1QLL5J8ThjAaLbc3wIHSk7E5gfzKzDabHkIgLjZYHmpPxfjb-6mM1VaW-uIHYGV4-ZfpqYnNXOWN6mUD1XSWxFSuWt5FdI0UswUhfw6oRM4gUZ4PVXvFK4NiCF0WveVXxZ8dW1gPJV35vXmes3LgeBjgwEQumiWobE5eY1izvtYbzUHGmzGLF-wYWuUuupdOgwxkG9sr365UU2SL6N8IgOtvAZN8WAXz9mGUQG-bOaxa9i9Jw8TbgmEmdeD32WFgt8KXu_mVkBdYMjpmKm8Z5LG6uBuqU5G7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37dea67a11.mp4?token=LqQV2_yVvCsjdzJfuqd_Z3aYWqNNzIp7ujeVBOQ5w8v-abJzbRHQW1QLL5J8ThjAaLbc3wIHSk7E5gfzKzDabHkIgLjZYHmpPxfjb-6mM1VaW-uIHYGV4-ZfpqYnNXOWN6mUD1XSWxFSuWt5FdI0UswUhfw6oRM4gUZ4PVXvFK4NiCF0WveVXxZ8dW1gPJV35vXmes3LgeBjgwEQumiWobE5eY1izvtYbzUHGmzGLF-wYWuUuupdOgwxkG9sr365UU2SL6N8IgOtvAZN8WAXz9mGUQG-bOaxa9i9Jw8TbgmEmdeD32WFgt8KXu_mVkBdYMjpmKm8Z5LG6uBuqU5G7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظهٔ اصابت موشک حزب‌الله به محل استقرار  نظامیان صهیونیست
@Farsna</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/farsna/435172" target="_blank">📅 21:29 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435171">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">تهران طوفانی شد
🔹
هواشناسی: از ساعتی پیش، وزش باد ۵۵ کیلومتر بر ساعت همراه با گردوخاک در تهران آغاز شده است.
🔹
توصیه می‌شود شهروندان از تردد غیرضروری در فضاهای باز و ماندن در مجاورت درختان کهنسال، سازه‌های موقت و تأسیسات ناپایدار خودداری کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/farsna/435171" target="_blank">📅 21:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435170">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/299a972263.mp4?token=MAueGj6R9KdEAwWKJqCrv5qdt2RZyGEQPQT79CxrAUQLqEAJVkcf5KYsILXEFlayR0y355hrSkqhWtb-_k44U5-45f4404y9mMiBUDTeUWbxxwQnRcgC6EJlmA5qS0mpGyK2cVoqfUyGWIkCcWq5svA_nXK1eZcHU5ytNglChWG22v78RKHPySfqYjiaUi6UsOnkDGz98FF58oW0C-vOr2WYLf7HdC0c-q61cTuDYyiwet1j5OcOdZBJ-B8yN6VUFYCJuGhQfZZQVEBisZfh7ZtPTZyfcoPdRKV8vIUrVZ_cUfwsu5JKIXAfKTQ_95B-INXGdx26DiO1IKUwfVS7ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/299a972263.mp4?token=MAueGj6R9KdEAwWKJqCrv5qdt2RZyGEQPQT79CxrAUQLqEAJVkcf5KYsILXEFlayR0y355hrSkqhWtb-_k44U5-45f4404y9mMiBUDTeUWbxxwQnRcgC6EJlmA5qS0mpGyK2cVoqfUyGWIkCcWq5svA_nXK1eZcHU5ytNglChWG22v78RKHPySfqYjiaUi6UsOnkDGz98FF58oW0C-vOr2WYLf7HdC0c-q61cTuDYyiwet1j5OcOdZBJ-B8yN6VUFYCJuGhQfZZQVEBisZfh7ZtPTZyfcoPdRKV8vIUrVZ_cUfwsu5JKIXAfKTQ_95B-INXGdx26DiO1IKUwfVS7ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تروریست آموزش‌دیدۀ گروهک تروریستی انصارالفرقان اعدام شد
🔹
رئیس دادگستری سیستان‌وبلوچستان: بامداد امروز حکم اعدام عبدالجلیل شه‌بخش فرزند جلال، عنصر آموزش‌دیدۀ گروهک تروریستی انصارالفرقان اجرا شد.
🔹
در پی بازداشت عبدالجلیل شه‌بخش در جریان اقدامات ضدتروریستی…</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/farsna/435170" target="_blank">📅 21:22 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435169">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">افزایش حقوق بازنشستگان تأمین اجتماعی امروز تعیین تکلیف می‌شود
🔹
خبرنگار فارس کسب اطلاع کرد، تکلیف افزایش حقوق و زمان پرداخت ۳۰ درصد باقیماندۀ همسان‌سازی بازنشستگان تأمین اجتماعی در سال ۱۴۰۵، احتمالا در نشست مشترک سه‌شنبۀ مدیران سازمان و نمایندگان کانون‌ها…</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/farsna/435169" target="_blank">📅 21:15 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435168">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">معاون وزیر خارجه: رویکرد فعلی آمریکا مذاکره نیست، اجبار است
🔹
غریب‌آبادی: تاکید ایران بر اصولی روشن است: توقف دائمی جنگ و عدم تکرار آن، جبران خسارات، رفع محاصره، رفع تحریم‌های غیرقانونی و احترام به حقوق ایران.
🔹
نمی‌توان هم‌زمان از آتش‌بس سخن گفت و محاصره را ادامه داد؛ از دیپلماسی گفت و تحریم را تشدید کرد؛ از ثبات منطقه‌ای حرف زد و به رژیمی که منشأ تجاوز و بی‌ثباتی است، پشتیبانی سیاسی و نظامی ارائه کرد.
🔹
چنین رویکردی، مذاکره نیست؛ ادامه سیاست اجبار با واژگان دیپلماتیک است.
@Farsna</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/farsna/435168" target="_blank">📅 21:11 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435166">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/682dd68c95.mp4?token=MyWNhvN5NWXBLWlZZyO5ibnZhcxfOVX6POLTuVFym5rzhF6IcqF1dT4GRV11BNwWzVuM5GDD6T2AAaAQ2s3_dBifq8mjusKE2fVR207F9-tG4uyRlfS3aL_uYR1jVbfnDnQdQLVmg2KI4P5ko0NZBXWJvd_a10iN1BCtpO13T7h2sO_7YtRQ8qErV9bkdbwiwCphHc1xK4UipjqQP4hF3CK9jo2eHLlk2qy5GwMPHHnVkfK2TUf_f-Q_ruXoCQZslNePaxck4_u8E6Rm_EzigdN3_4Vi6rVfaGTqu5SqGrut6Ig4Uuv9yNUCbFrOhOtj00lYoN314ao5wxs-CcJmhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/682dd68c95.mp4?token=MyWNhvN5NWXBLWlZZyO5ibnZhcxfOVX6POLTuVFym5rzhF6IcqF1dT4GRV11BNwWzVuM5GDD6T2AAaAQ2s3_dBifq8mjusKE2fVR207F9-tG4uyRlfS3aL_uYR1jVbfnDnQdQLVmg2KI4P5ko0NZBXWJvd_a10iN1BCtpO13T7h2sO_7YtRQ8qErV9bkdbwiwCphHc1xK4UipjqQP4hF3CK9jo2eHLlk2qy5GwMPHHnVkfK2TUf_f-Q_ruXoCQZslNePaxck4_u8E6Rm_EzigdN3_4Vi6rVfaGTqu5SqGrut6Ig4Uuv9yNUCbFrOhOtj00lYoN314ao5wxs-CcJmhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کریس کونز، سناتور آمریکایی خطاب به وزیر جنگ آمریکا: شما در جنگ با ایران موفقیت‌های «تاکتیکی» دست یافته‌اید اما در آستانهٔ یک شکست «استراتژیک» هستید، چون ما اکنون درحال مذاکره هستیم تا فقط [تنگه باز شود].
🔹
وزیر جنگ آمریکا: این حرف خیلی احمقانه است!
🔸
کریس…</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/farsna/435166" target="_blank">📅 20:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435165">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oWnDurrsaxRyXcz3GgPPFX6evLusybGwQpr6BNaX1Whqfd7mjdGGGnkaUHPycUxl5B1XTFhjc0ogGMowFABwABRB4kbhFsZHyJ2xJsvMUIBcL8sltfGpdaGPdkskJ9Hqo5pdEei4dHb8rgv_dFFTdFckG4bRD4gt4g00EiebxQy-sz5HvK3U9mbYJMeJZGEdky7BlO1QdJ6GQ5t7_btUokVvbekU5qDDsjscDuNhULmQD-Nmity6sKHgxtFmMEuajX6sJM2mpj56QtVUiUgiU7pzDf7MvtZtVBZOitAVPLrK1S_zTUeKiRfmAhS-BTqRrSdYFJo4EkjlUyPnfxvB4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
حسین پاک، خبرنگار حوزۀ مقاومت: حاکم بحرین ۲ هزار شیعه را زندانی کرده است.  @Farsna</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/farsna/435165" target="_blank">📅 20:55 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435164">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/005efbb538.mp4?token=NtzhxvAU8pfcVhrkckF8oWknZNzqByj3ohlzuQ4nDAvODvjHPvEQf6H1IXv7vwqY8fD2va-rIAGOvrkZZIdXGqperJfcn0e0uqfklGHiS4yHyhgpcxvBcSQOhp1wsaa2UImvZIaqgkQwLI50pbfscYgsE_J5Hp84Itcu4iqlxnP4h_v8DDhjL0BqxW8eVFKwzumHuhiCWr1Sk6r1JYelk44sLCBpV2t2lHYg-uRyzcDnB9Qv5Dq1XpL4vwWrHJPTaNQrVR0WgPUxYssUPa5RzPcEvk0fkhg3tEvLR7fxF4yM6iuRxhmGQOGZR5KdM5pPLilR7eq7bs5DCNDv1L2jyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/005efbb538.mp4?token=NtzhxvAU8pfcVhrkckF8oWknZNzqByj3ohlzuQ4nDAvODvjHPvEQf6H1IXv7vwqY8fD2va-rIAGOvrkZZIdXGqperJfcn0e0uqfklGHiS4yHyhgpcxvBcSQOhp1wsaa2UImvZIaqgkQwLI50pbfscYgsE_J5Hp84Itcu4iqlxnP4h_v8DDhjL0BqxW8eVFKwzumHuhiCWr1Sk6r1JYelk44sLCBpV2t2lHYg-uRyzcDnB9Qv5Dq1XpL4vwWrHJPTaNQrVR0WgPUxYssUPa5RzPcEvk0fkhg3tEvLR7fxF4yM6iuRxhmGQOGZR5KdM5pPLilR7eq7bs5DCNDv1L2jyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سناتور آمریکایی خطاب به وزیر جنگ آمریکا: شما ادعای کنترل تنگهٔ هرمز را دارید اما مشخص است که تردد کشتی‌ها در دست ما نیست
🔹
کریس کونز: آقای وزیر، شما همین چند لحظه پیش گفتید که «ما کنترل تنگه را در دست داریم». اما کاملاً مشخص است که بازگشایی تنگه هرمز برای…</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/farsna/435164" target="_blank">📅 20:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435162">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3953e09c1f.mp4?token=Krr2CP1byjfxduihE3CWkJE7RCHHBNz2-nWbY3sB0aWXmoXf0qbAHcfrMDf9kwjkd5uqIrZvJXK6DhYAKq44-UWs3GsGAwDC-5rHJbZmzUwg9YKRl2ACupFhPn-YdHWSRXX2dZktLl7bhoMwmuvVJ63mR4F-5oNRXgXBrTIwtROa427pl-mNM320tomRrJojbJMzxPPys9dU6sfEtfpXvusRLwlrfcyl0y7yTLSQX7tvmiZYcSalKTbe9c7ro_bdPhf_FSvEtk_HuWriRQ8CgJCAfyXZcT8OveqZ2AaJIcMkv5Amp-27HdkG_fc_JJg2dX11J8GrR_ZBAizDeS-CoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3953e09c1f.mp4?token=Krr2CP1byjfxduihE3CWkJE7RCHHBNz2-nWbY3sB0aWXmoXf0qbAHcfrMDf9kwjkd5uqIrZvJXK6DhYAKq44-UWs3GsGAwDC-5rHJbZmzUwg9YKRl2ACupFhPn-YdHWSRXX2dZktLl7bhoMwmuvVJ63mR4F-5oNRXgXBrTIwtROa427pl-mNM320tomRrJojbJMzxPPys9dU6sfEtfpXvusRLwlrfcyl0y7yTLSQX7tvmiZYcSalKTbe9c7ro_bdPhf_FSvEtk_HuWriRQ8CgJCAfyXZcT8OveqZ2AaJIcMkv5Amp-27HdkG_fc_JJg2dX11J8GrR_ZBAizDeS-CoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سناتور آمریکایی خطاب به وزیر جنگ آمریکا: شما ادعای کنترل تنگهٔ هرمز را دارید اما مشخص است که تردد کشتی‌ها در دست ما نیست
🔹
کریس کونز: آقای وزیر، شما همین چند لحظه پیش گفتید که «ما کنترل تنگه را در دست داریم». اما کاملاً مشخص است که بازگشایی تنگه هرمز برای تردد تجاری همچنان از دسترس ما خارج است؛ و دلیل عمده‌اش این است که ایران ذخیره قابل‌توجهی از پهپادهای ارزان و مرگبار «شاهد» را حفظ کرده و رقبای ما نیز در حال کمک به آن‌ها برای بازسازی این ذخایر هستند. آقای وزیر، برنامه شما برای بازگشایی تنگه هرمز چیست؟
🔸
وزیر جنگ آمریکا: بخش عمده‌ای از سوال شما بسیار غیرمنصفانه است.
@Farsna</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/farsna/435162" target="_blank">📅 20:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435161">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/675f7d368f.mp4?token=q-xhCi995L8zIGM1ELS9I_6gSn3DAzBS73GIIWmrzYmxlVQDSYaYHM8Hww9utowe4wc3RdYBtev1M707K94WRiLmDmgo-Cx5RDWMs8km_szpB26UQdJdL2rkYmhAmApmEsTJnfXs3mYseHyQzjtFPeBaSY_HVqDUgfLjDrDNBxhVlN_YHBH23WbuXFJHpqT0ySTS8D3bkBvnSgFYtk4zw84LZvTBNAp0pRc-J4-_YqpG-XSKv_VDAiISBSYdeICqRG39kvUtGyOhpPh1uAtqDueeqE-BhnyofwWMbLCFVQajTjSUnHoR9s25B--wzrGcZz-fI0k14jD9bYfVkp25xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/675f7d368f.mp4?token=q-xhCi995L8zIGM1ELS9I_6gSn3DAzBS73GIIWmrzYmxlVQDSYaYHM8Hww9utowe4wc3RdYBtev1M707K94WRiLmDmgo-Cx5RDWMs8km_szpB26UQdJdL2rkYmhAmApmEsTJnfXs3mYseHyQzjtFPeBaSY_HVqDUgfLjDrDNBxhVlN_YHBH23WbuXFJHpqT0ySTS8D3bkBvnSgFYtk4zw84LZvTBNAp0pRc-J4-_YqpG-XSKv_VDAiISBSYdeICqRG39kvUtGyOhpPh1uAtqDueeqE-BhnyofwWMbLCFVQajTjSUnHoR9s25B--wzrGcZz-fI0k14jD9bYfVkp25xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مجری منوتو صدایِ نوجوان ضد جنگ را هم تحمل نکرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/farsna/435161" target="_blank">📅 20:31 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435160">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5bb8f93b5.mp4?token=pqGx5MtQs5mi2gTur6xpEAFCMvKBmi0KCvS4BfCrLCcchwvTcJhZv1aPKZa8q9BTzPoD5II6ZA9TCup9xFViVrRDtDYu3s14CjtXCqe3iYpY4NFMYEgW-fDxl-QAxo1Kuvcp8xHiGMCnS1DdCDMZW70dFizj3pwPcT4Or92lb7Njy120fYC1qVOOd6gu1Q4UIjy5J7swEvuuHPoZDMl7LMMwkF_1AXy3VycFR71W_4L8hE2JJy3sPghGEIlnp3tY2_Y9dBpk5Gh8Ib7MGfdoY1aK9UQ3RRSGTxlIPKEaoA4rt6n7Zkw75_2RvCcGr0qBHfGmnyUgF8KCB4XRB6gkqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5bb8f93b5.mp4?token=pqGx5MtQs5mi2gTur6xpEAFCMvKBmi0KCvS4BfCrLCcchwvTcJhZv1aPKZa8q9BTzPoD5II6ZA9TCup9xFViVrRDtDYu3s14CjtXCqe3iYpY4NFMYEgW-fDxl-QAxo1Kuvcp8xHiGMCnS1DdCDMZW70dFizj3pwPcT4Or92lb7Njy120fYC1qVOOd6gu1Q4UIjy5J7swEvuuHPoZDMl7LMMwkF_1AXy3VycFR71W_4L8hE2JJy3sPghGEIlnp3tY2_Y9dBpk5Gh8Ib7MGfdoY1aK9UQ3RRSGTxlIPKEaoA4rt6n7Zkw75_2RvCcGr0qBHfGmnyUgF8KCB4XRB6gkqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت رئیس دفتر رئیس‌جمهور از آخرین دیدار شهید لاریجانی با پزشکیان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/farsna/435160" target="_blank">📅 20:23 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435159">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j_XhgI648R_tByBDhFJF41qIHThkhocRU8C8BBguB-1sh0dXjg66HWTRTlySWo8GaK6ikKPmqdm9EASEBVHdI2DaQmoWNC5df5GpXdWYpjxdo7iG_JbRJ_GH4fclmlu92Axs4YN36ykiFy6qZfGPJ5NelJaLbno8x7Su_cU_GP0wk0wHrp4ccdrWdGJmC0ZALqXzLeQloEGTTzThj3HLtYs0pCrMo8hxthAjDrs3q06tAkaLGjoUuE1F3jQ9_-xoq3xO-bdpI1lS-b2rOyG4TJAnc9nTWs17pYFZzrokiskjHLL9ESaTPssW6Go4NbN6mPkGy1gw0otWitRN9PEh1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۴.۵ همت کالای قاچاق و احتکار شده توسط اطلاعات سپاه
ِ
اصفهان
🔹
اطلاعات سپاه استان اصفهان چندین هزار تن کالاهای اساسی، سوخت، لوازم خانگی و مواد پتروشیمی احتکار شده و قاچاق به ارزش بیش از ۴.۵ هزار میلیارد تومان را کشف کرد.
🔹
همچنین یک انبار بزرگ حاوی ۱۶۸۰ تن الیاف مورد نیاز بازار پوشاک به ارزش حدودی ۱.۷ همت که در سامانه جامع انبارها ثبت نگردیده بود، توقیف شد.
🔹
پرونده مجرمان جهت رسیدگی به مراجع قضایی ارجاع شده‌است.
@Farsna</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/farsna/435159" target="_blank">📅 20:18 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435157">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0f0907b65.mp4?token=bWwSnnJTemj9lqGvUedCmUaFIMcapbiLq1DgwzSnH5hRuhdYvt088XZAQFsDAcDdvB93RhPuxIpVWZp7dBEj-AtYIm0dAWtF6xKTfYi4ObXBTIJChlCMQJAibZmZQrFR-G2VpKDxIvepJQBegPGTVw6d58MXqMS6ABOMZNqIIlMfXef_3E9XBR8U1OhsJwbk29_8Kbw24TLfdThu20fDDOOMxYIx9sLSPm-SP6KxEABR3zMQkBFm4A7zQ15YX08PPq6vxaJxutNXzRxwl4eAKWq2R2140BAo48ol5rYN_6_umsaJXU0tMmDcIVUdE1SKlXeuWxJPf0MKllfop1Ug2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0f0907b65.mp4?token=bWwSnnJTemj9lqGvUedCmUaFIMcapbiLq1DgwzSnH5hRuhdYvt088XZAQFsDAcDdvB93RhPuxIpVWZp7dBEj-AtYIm0dAWtF6xKTfYi4ObXBTIJChlCMQJAibZmZQrFR-G2VpKDxIvepJQBegPGTVw6d58MXqMS6ABOMZNqIIlMfXef_3E9XBR8U1OhsJwbk29_8Kbw24TLfdThu20fDDOOMxYIx9sLSPm-SP6KxEABR3zMQkBFm4A7zQ15YX08PPq6vxaJxutNXzRxwl4eAKWq2R2140BAo48ol5rYN_6_umsaJXU0tMmDcIVUdE1SKlXeuWxJPf0MKllfop1Ug2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
واشنگتن‌پست: ایران حداقل به ۲۲۸ ساختمان یا تجهیزات در پایگاه‌های آمریکا حمله کرده است
🔹
این حملات شامل آشیانه‌ها، پادگان‌ها، انبارهای سوخت، هواپیماها و تجهیزات کلیدی رادار، مخابرات و پدافند هوایی بوده است.
🔹
میزان تخریب بسیار فراتر از آن چیزی است که دولت…</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/farsna/435157" target="_blank">📅 20:10 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435156">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mr1pygj68PeRoe_iliZeWqafgmZzll_IvdjKrAu8VOKWUrC6sGTn9RU-lH9W6ZEOYajIODt0DnrdrE43rOFIqbWRgiey7peIEarXIgec6FG-2_sNHRZ3d7wqRSpfJETEx1CA1NC91dFaJp4TO4pvCOUIzRzgQ2qcpAbTCC03qoR30TN5x2tAhnVkq3oelZh7iBj37rGXI0s549hXqTfJ-FoJtJIB-hXEs4rJjEPMm9pRk43nSnfYZJFGJAiM1yT_ynjbPHlqM2CMTiDagTSjZoAEOz1gqRlIjQxTfoD6HFvq4wHywwBr7MIjpR2M6U3gTRAt-b4eC3uLCoSgi7FDNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتایج یک پیمایش ملی از ابعاد پنهان تجمعات شبانه
🔹
یک پیمایشی درباره تجمعات شبانهٔ ایران که با مشارکت ۴۳ هزار و ۳۹۱ نفر در بازه زمانی هفتم تا یازدهم اردیبهشت سال جاری انجام شده، ابعاد مختلف این حضور جمعی را از منظر انگیزه‌ها، تجربه اجتماعی و پیامدهای آن بررسی کرده است:
🔸
۹۴.۸ درصد پاسخ‌دهندگان اعلام کرده‌اند حضور مردم در تجمعات داوطلبانه و خودجوش بوده است.
🔹
۹۳.۱ درصد شرکت‌کنندگان با این گزاره موافقند که نهادهای مردمی نقش اصلی در سازماندهی تجمعات دارند.
🔸
در شاخص «توجه و شکر نعمت وحدت» میانگین امتیاز ۸۷.۵۴ درصد ثبت شده است.
🔹
۹۱.۸ درصد پاسخ‌دهندگان هم معتقدند در تجمعات بر حفظ وحدت اجتماعی تأکید زیادی می‌شود.
🔗
شرح کامل پیمایش را از
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/farsna/435156" target="_blank">📅 20:06 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435155">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TluJEUrjG2D1iwcaoenpuBkZa1KQ72x1dX2HvUPoTz1SaCYUKgII0eQn2nW_-STcMMkJ95AlQfraCQXwwegLw4f6vYriYWSbGeh1E_XDY3VQbOpbnU6cYpC4Lrmo8ypFJ-W2_ye80EtTLlcmsRNAh_Id1APEdex8Ty_hpA7mAdnGJfnYl1kdPPvEep4M3iUZjAVhe2H6_9XMVdWzhPhZhyvx1Y-fv40Oqt3ES2yo_KpQIxv9Dxr6EocMTAhRtZScpAMdbMIvMGH-8Mrnb5MMUABoFodsCneWP2tul3vzUFoEoKoq2RZkhYBl0mXTL3ciMRc3SkkTL4E31Y-XSiML9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برد پر گل تیم سفید ایران مقابل تیم قرمز
⚽️
گلزنان بازی:
علیپور، ایری(۲)، یوسفی، حسین‌زاده
⚽️
تیم سفید ۴ - ۱ تیم قرمز
@Sportfars</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/farsna/435155" target="_blank">📅 20:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435154">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c11c0a8608.mp4?token=DlBraGikJloX6MxG_TBdERW0eoQlkeMMyWNRLN3RvmDE6py1h6I4O4NHbQLdsMFz9xGmfUHTb2SiYHrygd3GsK1FTqCChbxPG4z83rSv7UrtM3miOAo_KgfO1s2lg6-qhBFgzGeRFCM3yGV2MPY7YlNuXBSRZvlND6LBDfuPvM6O3UANCD4B8GJca0DJwkXQyrkCOUHPrRtFfpvKdp2_p-Rp7nhsgU00RfpwepC4j82z_nz02MfBLsq9PHIFDRS3wQjHj38FOcP_NCkrxpUHlkM0uuzGCiFKcWrRInbW4X8essI12LLPYgxqXEfv4IBE52qcHLG91-tnef85k8w_1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c11c0a8608.mp4?token=DlBraGikJloX6MxG_TBdERW0eoQlkeMMyWNRLN3RvmDE6py1h6I4O4NHbQLdsMFz9xGmfUHTb2SiYHrygd3GsK1FTqCChbxPG4z83rSv7UrtM3miOAo_KgfO1s2lg6-qhBFgzGeRFCM3yGV2MPY7YlNuXBSRZvlND6LBDfuPvM6O3UANCD4B8GJca0DJwkXQyrkCOUHPrRtFfpvKdp2_p-Rp7nhsgU00RfpwepC4j82z_nz02MfBLsq9PHIFDRS3wQjHj38FOcP_NCkrxpUHlkM0uuzGCiFKcWrRInbW4X8essI12LLPYgxqXEfv4IBE52qcHLG91-tnef85k8w_1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نوحهٔ حماسی کریمی در میدان انقلاب: «رهبرمون هرچی بگه همونه»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/farsna/435154" target="_blank">📅 20:00 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435153">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SKZK8QROVSnMY29sYMkTKgizLm-SRmfDNciFsQaj_Pdf9k1RFxEszPugEBkYOnqcNSyYudkX8HTQs7XDiYQCg-YCGWurbLAdJMFtAJbZZKsGwOWJGmh0zON6ZF-I-BNFIbOYoZr9-ApudBLDBkVHT0t1HhXecigeXBK-T7GqpByELDIC3HILrR3Ohl-HvhzMaLe8UXZXF8SJSglbISYfsKM9sTlTNs5q7PeQ-ZNA9-C52TtlTKeQARSloKIa7vIygiR4L5XYSZGXgnNje_vq2xkt7rfiml42oQFaMwPk2HfkEpZ1yauvYoUbQhkCv95RfEGQqE_Qn9VJ1h9nKpPwKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افرادی که وسط جنگ هم دست از افزایش قیمت خودرو برنمی‌دارند!
🔹
طاهری، عضو کمیسیون صنایع مجلس: ایران‌خودرو با مدیریت جدید نباید هر اقدامی را بدون توجه به سیاست‌های کلان انجام دهد.
🔹
پیش از این بارهاهشدار داده بودیم که واگذاری‌ شرکت‌های خودروسازی از نظر ما با تعارض منافع همراه خواهد بود.
🔹
انتظار می‌رود قوه قضائیه به‌صورت جدی به این موضوع ورود کند زیرا تصمیمات مدیریتی در حوزه خودرو مستقیماً بر زندگی مردم اثر می‌گذارد.
🔹
الان کشور گرفتار افرادی است که وسط جنگ خودرو را گران می‌کنند.
🔹
حتی در دوره‌ای که مدیریت خودروسازان دولتی بود، اگرچه مردم از وضعیت خودرو رضایت کامل نداشتند، اما سیاست‌های کلان حاکمیت در حوزه قیمت‌گذاری رعایت می‌شد و کم‌تر شاهد تصمیماتی بودیم که در شرایط حساس کشور موجب افزایش قیمت‌ها شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/farsna/435153" target="_blank">📅 19:51 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435152">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db78859303.mp4?token=Agf_mUVlwSyIqYn1N1LbdsYmkeM0AYpEDVQ8vXwlXlF3JfJ4jp4Rmzx1ppAR4eDupxI_ScxUSj4HhboEU7WV0HUkms2SFCBBL5rcaZX_tzZWFc4yA9mepemBLuM4fxFlKC55mJ8l-q9dOWbz8ZWyYoIx-JzineVZ1P0gUJO_CHCdzHLIRXU581bR-iQfLjzZfDNGzuTGmmhM94G6Y1RY4EIWE1AQEFDR9bEcxpuCuEesyCTPnjQ4n-5sPtFDIUdVxyuBl140xGu-sQkMloBdKPUdPebLiR-EJGFQ7Oc8-ZDszzQ5kxaB92GgAVzdCH-_qSD7ZdCLu2aDP0k6DHv7-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db78859303.mp4?token=Agf_mUVlwSyIqYn1N1LbdsYmkeM0AYpEDVQ8vXwlXlF3JfJ4jp4Rmzx1ppAR4eDupxI_ScxUSj4HhboEU7WV0HUkms2SFCBBL5rcaZX_tzZWFc4yA9mepemBLuM4fxFlKC55mJ8l-q9dOWbz8ZWyYoIx-JzineVZ1P0gUJO_CHCdzHLIRXU581bR-iQfLjzZfDNGzuTGmmhM94G6Y1RY4EIWE1AQEFDR9bEcxpuCuEesyCTPnjQ4n-5sPtFDIUdVxyuBl140xGu-sQkMloBdKPUdPebLiR-EJGFQ7Oc8-ZDszzQ5kxaB92GgAVzdCH-_qSD7ZdCLu2aDP0k6DHv7-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هزینهٔ جنگ آمریکا با ایران ۴ میلیارد دلار بیشتر شد
🔹
نماینده پنتاگون: چند روز پیش برآورد هزینهٔ ۲۵ جنگ میلیارد دلار بود اما در حال حاضر فکر می‌کنیم این رقم به ۲۹ میلیارد دلار نزدیک‌تر شده است.
🔸
پیش از این سی‌بی‌اس فاش کرده بود که هزینۀ واقعی آمریکا نزدیک…</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/farsna/435152" target="_blank">📅 19:34 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435151">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c40069255e.mp4?token=qMnwb2sjNSnN_KRVcQETGkbRhNaGhRLM-PVcH3ZhAzkvxUVmR8EUb1jhRkN2fRhRnLXf4IElw572MYsiO_jNOyinVsYFXQ_xpoIW7V5snmWDyuMUNs-EBiMcrjkqm8ur-UrXrXBABgnk6pykCBqkAxwTpqQyy7Twg3mVUyfFtI_ta7Iu5KuXzXvHeA6Y9GNrxQkaIFOXG1nm5I97Y8BQiai6SK-xsjLJlPd30K_517atYByzJegZB4RkhTyODL_sB7LqTmE8fkCWUvVvFJQatcMQXoFMOiJzxC42NjlDbJj_PbiDGw7g47AJUQQ2fnEtrTpPo4H8OHULMaQKvFUVVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c40069255e.mp4?token=qMnwb2sjNSnN_KRVcQETGkbRhNaGhRLM-PVcH3ZhAzkvxUVmR8EUb1jhRkN2fRhRnLXf4IElw572MYsiO_jNOyinVsYFXQ_xpoIW7V5snmWDyuMUNs-EBiMcrjkqm8ur-UrXrXBABgnk6pykCBqkAxwTpqQyy7Twg3mVUyfFtI_ta7Iu5KuXzXvHeA6Y9GNrxQkaIFOXG1nm5I97Y8BQiai6SK-xsjLJlPd30K_517atYByzJegZB4RkhTyODL_sB7LqTmE8fkCWUvVvFJQatcMQXoFMOiJzxC42NjlDbJj_PbiDGw7g47AJUQQ2fnEtrTpPo4H8OHULMaQKvFUVVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نماینده کنگرهٔ آمریکا: طبق گزارش‌ها ما تا یک ماه پیش در جنگ با ایران ۳۹ هواگرد از دست داده‌ایم که برخی از آن‌ها جایگزین ندارد
🔹
اِد کِیس، نماینده کنگره: طبق گزارشی در پایگاه «وار زون»، ما حدود ۳۹ هواگرد از دست داده‌ایم، که البته آن گزارش قدیمی است. متعلق…</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/farsna/435151" target="_blank">📅 19:32 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435150">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b70a136fd5.mp4?token=qju5tKiaINhie0JAPlzNgS56d4OtjqUcf9ilL9bJxch8VDA5T3GWgl-OCivKOem3K1vTRfvReSG37MKizba3U6nbSiXk1_EJoKdpbZsZRYpyLE6xpwfem7pnzqhqXj9NhJUiVXE0wkdcr3BPKaeIBgAqa4yV6o-Cf89gRF4qfmHg0Fb9Amg3z9W7dvd8iOaFLce2aF68QFZzv474TVUx91U-x7Emmq_kNSVNkLih7qwVkW0AG5yoLpbXozs73GsdG70Duui3BiGq1Bxu2Rj11DRJHOmja11842ybIakfmi8fr8BLXZ80tW5HE24v2G39LkGpEJXWcJjEvSGVtdd0TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b70a136fd5.mp4?token=qju5tKiaINhie0JAPlzNgS56d4OtjqUcf9ilL9bJxch8VDA5T3GWgl-OCivKOem3K1vTRfvReSG37MKizba3U6nbSiXk1_EJoKdpbZsZRYpyLE6xpwfem7pnzqhqXj9NhJUiVXE0wkdcr3BPKaeIBgAqa4yV6o-Cf89gRF4qfmHg0Fb9Amg3z9W7dvd8iOaFLce2aF68QFZzv474TVUx91U-x7Emmq_kNSVNkLih7qwVkW0AG5yoLpbXozs73GsdG70Duui3BiGq1Bxu2Rj11DRJHOmja11842ybIakfmi8fr8BLXZ80tW5HE24v2G39LkGpEJXWcJjEvSGVtdd0TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نماینده کنگرهٔ آمریکا: طبق گزارش‌ها ما تا یک ماه پیش در جنگ با ایران ۳۹ هواگرد از دست داده‌ایم که برخی از آن‌ها جایگزین ندارد
🔹
اِد کِیس، نماینده کنگره: طبق گزارشی در پایگاه «وار زون»، ما حدود ۳۹ هواگرد از دست داده‌ایم، که البته آن گزارش قدیمی است. متعلق به تقریباً یک ماه پیش است. آیا هزینۀ جایگزینی تمام آن هواگردها را می‌دانید؟ با این فرض که برخی از آن هواگردها قابل جایگزینی نیستند، اما قاعدتاً باید آن‌ها را با نوعی ظرفیت و توانمندی جایگزین کنید.
🔸
نماینده پنتاگون: هزینه‌هایی در این مورد وجود دارد، اما می‌خواهم جزئیات دقیق آن‌ها را به صورت مکتوب به شما ارائه دهم. چون همان‌طور که می‌توانید تصور کنید، محاسبه هزینهٔ تعمیرات هواگردها کار بسیار دشواری است. ما می‌خواهیم پیش از برآورد هزینه، یک عیب‌یابی کامل از هواگردها انجام دهیم.
@Farsna</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/farsna/435150" target="_blank">📅 19:15 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435149">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d359f5beb6.mp4?token=JsvWZlHV7Zb_OF0t131_dWMWMe707tFv7a30Daqr3DOzyy0Fd0W8xsyCfBd6vEhamlCfdSJrKKKpfPOCfXvItW4XNr_O_3jHjc5bazjwvxKczA7PQJP953kg8QXE3kBSZ8Tie0nFAbvVFxugOKt6kHV6dKrXbokrwrZx5AbOzBKvgt3Dpkb-v5QpyrvXMMYoi39d0H4vVrSJ4IGkPY3BXRTHpiRp1keVhqH6xE_xe0LPoxLAMAdh4hOJghdS9xhRIP18u9Z20ogG12y7MITX2mmcVKAnpzjPTg1T6481qXs3MzOtT18lI1qDFqeMEEep8N7bwikaoJoWaCrukn_Azw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d359f5beb6.mp4?token=JsvWZlHV7Zb_OF0t131_dWMWMe707tFv7a30Daqr3DOzyy0Fd0W8xsyCfBd6vEhamlCfdSJrKKKpfPOCfXvItW4XNr_O_3jHjc5bazjwvxKczA7PQJP953kg8QXE3kBSZ8Tie0nFAbvVFxugOKt6kHV6dKrXbokrwrZx5AbOzBKvgt3Dpkb-v5QpyrvXMMYoi39d0H4vVrSJ4IGkPY3BXRTHpiRp1keVhqH6xE_xe0LPoxLAMAdh4hOJghdS9xhRIP18u9Z20ogG12y7MITX2mmcVKAnpzjPTg1T6481qXs3MzOtT18lI1qDFqeMEEep8N7bwikaoJoWaCrukn_Azw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آتش‌سوزی در پایگاه نظامی اسرائیل در شمال فلسطین اشغالی
🔹
منابع اسرائیلی گزارش دادند این مقر در نزدیکی شهرک «مرگالیوت» قرار دارد و دچار آتش‌سوزی شده است.
🔹
این مسئله ناشی از حملات حزب‌الله به این شهرک اعلام شده است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/farsna/435149" target="_blank">📅 18:57 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435148">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fce65d3c53.mp4?token=Stiu9-qHjVdy7voh-hpRomyONm0dFqGSPP7KDLTo-__1i7tv5H4QTXmHey_-UbYuqd2JUT7pkf-CtESMkyDo17SfLN876Rxbm6Wjn1MF8UvAvwZtzxAsRvuzRCYykxoG_I9CG4WNR6sS9oPbBGBZxZ633_Ey32U-HIub9H2WVRH9gclqrCSYDcGSywC21_reDuxlexEla_RdMw25Dt-ayWbSHryTIgTEiCzWji35CmVjPU5cMWNJnlPnN2DSHJO8cigEhIt0dZ9DP5kEWGZm2nsAjn8Kbg2GM_K6v8MFCFf6lFyKcPWi3j8yYy0wD7y68se88BjRETFzg91HA38JLh1WxvoKxsnQxUvWoDDmYbBZA_09M0iVOSTXZyd5_zLl8WGMj5ru3-N38uyy6gFemVJkyuUjG6GDfx2FydVuL4_lCkyKoABccVGNiWrv07uZFKfTv8alTo7njRnoZitd8y2RNwv7Ip29m9LtROtj5kwn9EfmPKGsfQssj7fbrx36NvmVvFXTdU-kbDhxyYmqgBKvdLRqK2LIqIg_0sEyFxE06JuJcw0k8Ph93DGX1mCCCBjW_si5o6j9WlHnl59zM5OwISOU_IYWSOrPtERwHDZyN9YK5-_r33dDiN3XXrTT7WujMzj65A5wqozAdRhjx6DsRExQlSXWP3QqS8vaWQ8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fce65d3c53.mp4?token=Stiu9-qHjVdy7voh-hpRomyONm0dFqGSPP7KDLTo-__1i7tv5H4QTXmHey_-UbYuqd2JUT7pkf-CtESMkyDo17SfLN876Rxbm6Wjn1MF8UvAvwZtzxAsRvuzRCYykxoG_I9CG4WNR6sS9oPbBGBZxZ633_Ey32U-HIub9H2WVRH9gclqrCSYDcGSywC21_reDuxlexEla_RdMw25Dt-ayWbSHryTIgTEiCzWji35CmVjPU5cMWNJnlPnN2DSHJO8cigEhIt0dZ9DP5kEWGZm2nsAjn8Kbg2GM_K6v8MFCFf6lFyKcPWi3j8yYy0wD7y68se88BjRETFzg91HA38JLh1WxvoKxsnQxUvWoDDmYbBZA_09M0iVOSTXZyd5_zLl8WGMj5ru3-N38uyy6gFemVJkyuUjG6GDfx2FydVuL4_lCkyKoABccVGNiWrv07uZFKfTv8alTo7njRnoZitd8y2RNwv7Ip29m9LtROtj5kwn9EfmPKGsfQssj7fbrx36NvmVvFXTdU-kbDhxyYmqgBKvdLRqK2LIqIg_0sEyFxE06JuJcw0k8Ph93DGX1mCCCBjW_si5o6j9WlHnl59zM5OwISOU_IYWSOrPtERwHDZyN9YK5-_r33dDiN3XXrTT7WujMzj65A5wqozAdRhjx6DsRExQlSXWP3QqS8vaWQ8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نخست‌وزیر سابق قطر: آمریکا با جنگ به دوستانش در منطقه آسیب زد
🔹
شیخ حمد آل‌ثانی: اقدام نظامی [علیه ایران] در کل به سود هیچ کسی در منطقه نبود. آمریکا به دوستانش در منطقه آسیب رساند.
🔹
عملیات نظامی تنها به سود شخص نتانیاهو بود. به برنامه‌های او کمک کرد.
🔹
او به‌صورت آشکار از ضرورت ترسیم یک نقشه جدید در منطقه و تشکیل ائتلاف‌های جدید برای اسرائیل بزرگ صحبت می‌کند.
🔹
آن‌ها اطلاعی از ساختار قدرت در ایران ندارند؛ این هرم [قدرت] طی ۴۷ سال و از زمان خروج شاه ساخته شده. به آن شکلی که آنها فکر می‌کنند سقوط نمی‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/farsna/435148" target="_blank">📅 18:43 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435146">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">کویت سفیر ایران را احضار کرد
🔹
وزارت خارجۀ کویت با ادعای ورود چند نیروی سپاه پاسداران به جزیره بوبیان، از احضار سفیر ایران خبر داد.
🔸
کویت مدعی شده گروهی از نیروهای سپاه با ورود به این جزیره با نظامیان کویتی درگیر شده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/farsna/435146" target="_blank">📅 18:39 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435145">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df4b69123b.mp4?token=STu1eZEBm3fsmQMCiTMrh9wTmXRYFEFF6tYb5uI2PjB55DRWkOIMMwiG_k0pRHcSrKe2BfcjxL7MqqwCROy4sNS8xcDsa_keWRC0Vbf81v6WxVkCZPya3y1qXUs2qLEPZ0tJkaG2iX6WHv_CNPMnhvQE5CRsSS_KZrJOKQUs99lR2aAPzctIjz30B-aoxxpUchNHx1ZniG8lFlVygbdG2f7BzOjwdy3cPa03NgVgayLWlrP5RJnLttRyW5apDx42gw7c_xYtYJZxZVOkQxRkwD4HIc2-PNt9H_IgNJ1znVSsPqB-iQEPvPmTZfgQhdfYl6GW5I5U2wTcav-vHLMSVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df4b69123b.mp4?token=STu1eZEBm3fsmQMCiTMrh9wTmXRYFEFF6tYb5uI2PjB55DRWkOIMMwiG_k0pRHcSrKe2BfcjxL7MqqwCROy4sNS8xcDsa_keWRC0Vbf81v6WxVkCZPya3y1qXUs2qLEPZ0tJkaG2iX6WHv_CNPMnhvQE5CRsSS_KZrJOKQUs99lR2aAPzctIjz30B-aoxxpUchNHx1ZniG8lFlVygbdG2f7BzOjwdy3cPa03NgVgayLWlrP5RJnLttRyW5apDx42gw7c_xYtYJZxZVOkQxRkwD4HIc2-PNt9H_IgNJ1znVSsPqB-iQEPvPmTZfgQhdfYl6GW5I5U2wTcav-vHLMSVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مارک
کلی، سناتور آمریکایی: وزیر جنگ ترامپ گفته جایگزینی مهمات استفاده‌شده در جنگ ایران سال‌ها زمان می‌برد
🔹
دولت ترامپ حجم عظیمی از مهمات را در جنگ با ایران مصرف کرده است. بعد از ۱۵ هزار حمله، تنها چیزی که نصیبمان شد، ۱۳ کشتۀ آمریکایی، بسته‌شدن تنگۀ هرمز، بنزین ۴.۸ دلاری بود.
🔹
آن‌ها بدون هدف استراتژیک، بدون برنامه و بدون جدول زمانی وارد این ماجرا شدند. حالا هیچ راهبردی برای خروج ندارند و به دست‌وپازدن افتاده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/farsna/435145" target="_blank">📅 18:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435144">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9337725a2.mp4?token=Xj-5IhxKMTvkOHc1jG2bbY0TK8IZBMpnl172LUB0MvDJgrLgOH47gS38qTGmWieLXHz-3hdz0EFfBlcFk6Aoz-4RWDWHiUZx93eJmMRxNmFuZfYAyaKzGkrGdG1OIFeXPVwFvgJTaA2FOkYA3MvLheVezz9ZLdhZcYPNpwr8J2-IeIjVYApqen1e2oTzpuhy91WxJxhby8EsLRDfZeyyugvj1nnq_bHGViu3Ikv_CxSF-OO-dK1yezNw03n1YATwAR6NowkeobaMWgr7UbhSXeGcKKzOKHU2XMwFE-LFlyN59zpuDRGrZTE2QyRU-UWupIbLOUazimiCYfdRNMSkjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9337725a2.mp4?token=Xj-5IhxKMTvkOHc1jG2bbY0TK8IZBMpnl172LUB0MvDJgrLgOH47gS38qTGmWieLXHz-3hdz0EFfBlcFk6Aoz-4RWDWHiUZx93eJmMRxNmFuZfYAyaKzGkrGdG1OIFeXPVwFvgJTaA2FOkYA3MvLheVezz9ZLdhZcYPNpwr8J2-IeIjVYApqen1e2oTzpuhy91WxJxhby8EsLRDfZeyyugvj1nnq_bHGViu3Ikv_CxSF-OO-dK1yezNw03n1YATwAR6NowkeobaMWgr7UbhSXeGcKKzOKHU2XMwFE-LFlyN59zpuDRGrZTE2QyRU-UWupIbLOUazimiCYfdRNMSkjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هدیه متبرک خادمان حرم امیرالمومنین(ع) برای آسیب‌دیدگان جنگ
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/farsna/435144" target="_blank">📅 18:20 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435143">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-text">🎥
سلام نظامی ملوانان ناو دنا هنگام نواختن سرود ملی
🔹
ملوانان ناو دنا، مهمانان ویژۀ سومین بازی درون تیمی تیم ملی هستند.
@Sportfars</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/farsna/435143" target="_blank">📅 18:16 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435142">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار چهارمحال و بختیاری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8369afb88.mp4?token=fZ5051heN8SX1P0Nn2NDtPMn_RLmU4ibHgr9mhmQRTl095LcsV9-oKh1YwfrRTxbSD3ArmCfzMW3nD6pNDnUQjp9nS9zvBGjZpG1PCGm57PD1fUSrRxXHzazMDo8ciS-opejX3WZY-gFy_rBBIQgCnN_S4ZuHgdTWXYSat2vBhwSnorl6W7lbdoYZgc2BXT2nvM2s84hjUGHFE_rg8ONZ8Z2cH9a7sCACz3TfY_RNSLG4L55qNgN2YXC41v4TYayq8QQNW5-P0XGmHBBZzI0ZUQV7Z90LCHVv9MDCvPVwMoYGOGfvPVjSu0ugo4uiJ61Pze-XPXYPkeyizUJLb9waQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8369afb88.mp4?token=fZ5051heN8SX1P0Nn2NDtPMn_RLmU4ibHgr9mhmQRTl095LcsV9-oKh1YwfrRTxbSD3ArmCfzMW3nD6pNDnUQjp9nS9zvBGjZpG1PCGm57PD1fUSrRxXHzazMDo8ciS-opejX3WZY-gFy_rBBIQgCnN_S4ZuHgdTWXYSat2vBhwSnorl6W7lbdoYZgc2BXT2nvM2s84hjUGHFE_rg8ONZ8Z2cH9a7sCACz3TfY_RNSLG4L55qNgN2YXC41v4TYayq8QQNW5-P0XGmHBBZzI0ZUQV7Z90LCHVv9MDCvPVwMoYGOGfvPVjSu0ugo4uiJ61Pze-XPXYPkeyizUJLb9waQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اینجا خانه مادر شهید سردار خادمی رئیس سازمان اطلاعات سپاه است
🔹
ماجرای عجیب لحظه شهادت سردار شهید خادمی و حرف زدن مادر پس از ده سال!
آخرین خبرهای جنگ را اینجا ببینید
👇
@Fars_Chb</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/farsna/435142" target="_blank">📅 18:14 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435141">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۳۳.pdf</div>
  <div class="tg-doc-extra">2.2 MB</div>
</div>
<a href="https://t.me/farsna/435141" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۳۲.pdf</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/farsna/435141" target="_blank">📅 18:05 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435140">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lLlo29w23Rg5cedRU_rBP6CR0o2x25DnclwSW-TqPpNmwQNq13KVtz83RPTmTB_Gb-cxrCQZCS3udvYMySUA5hR6OSc0rH9NxGqplVtysnhneHwzgJrjTser1A-qZMkIN2xbQURIokZlCi1AitYSRJn0XfvDaC5_1i0nPNGuBEJk1gQO5Q0k2ZLOB7U3_nUocmnHRtzStucME_pZswj6OWPNd3g3vIdrjOcpIyp7et6SbCuZQePI8unblAmA9dVRiA1E9nSc-trwB3GxI_nVTrJo5VXKBpYI_zBjT_GpHl2b9F0wkEdNvX6o1ZpghleDw4hmjzYGwdGkQMxL-gYNBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پزشکیان: ارتباطات مبتنی‌بر فناوری اطلاعات و اینترنت به بخش جدانشدنی زندگی مردم تبدیل شده
🔹
به آقای عارف ماموریت دادم با لحاظ حساسیت‌های حکمرانی، نظر رهبری و وعده‌ای که به مردم داده بودم، در قالب ساختاری چابک موجبات خدمت‌رسانی بهتر دولت و تحقق انتظارات عمومی را فراهم سازد.
@Farsna</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/farsna/435140" target="_blank">📅 18:00 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435139">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd9b7db5f8.mp4?token=phcprMmcv6NiNvi_A0hUzH05POgWtIW6Mtl3NKOxSdQFlRNGzMwAP1kh6vgm4BmNPyCZ0WOyAGZfXH-VdoaomBI8fzQt0xaqlCoWkVWEvWgXAPtb__29I0LiCopLydo8XpBWBqKhh5O6DJcGg1fnkq67yVRT91ezL06gGWPaIyldsidBAezCWr6rUNuQl_-yf7sDqq-sSquPq8Muiv8aqh_SbGgMs3U5rTlfpDwsZtm6d8WyypTAcMDNKQdDip9WL9IV4sYd3KNdWOIMnzm1APmniOLgNouhClywPIGM_j5ubzaDtHFCcsQwf-LgklsKcjGPkcpYZD7RTl4RCBocZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd9b7db5f8.mp4?token=phcprMmcv6NiNvi_A0hUzH05POgWtIW6Mtl3NKOxSdQFlRNGzMwAP1kh6vgm4BmNPyCZ0WOyAGZfXH-VdoaomBI8fzQt0xaqlCoWkVWEvWgXAPtb__29I0LiCopLydo8XpBWBqKhh5O6DJcGg1fnkq67yVRT91ezL06gGWPaIyldsidBAezCWr6rUNuQl_-yf7sDqq-sSquPq8Muiv8aqh_SbGgMs3U5rTlfpDwsZtm6d8WyypTAcMDNKQdDip9WL9IV4sYd3KNdWOIMnzm1APmniOLgNouhClywPIGM_j5ubzaDtHFCcsQwf-LgklsKcjGPkcpYZD7RTl4RCBocZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بحرین، کشوری که با طناب پوسیده دیگران به ته چاه رفت
🔹
بحرین دهه‌ها تلاش کرده معظل جغرافیایی و  سیاسی خود را با تکیه به دیگران پوشش دهد؛ اکنون در زمانی که امید داشت از این راهبرد بهره ببرد؛ با واقعیت‌های بی‌رحمی مواجه شده است.
🔹
در ذات موقعیت ژئوپلیتیکی خود،…</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/farsna/435139" target="_blank">📅 17:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435138">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5ab333d5b.mp4?token=Su1Ahuae8kxbZSboMNzHWGa4SNkwIhExjePXb5pF6TyWJ4DCFhcvwqdPpWe6m393o7wMSZQHSio4KRFmGTDZEL4yJ9I16ads2fE9sCGutxbWbOTIUeymMyjXtDllKBudHz9y6IUq503QjQy8OYQbz-HJpEOkW55dAd10eEaXZ6u7xVOyp6d37_cHUp0pW9VMNS4CAqLIloMKvE9xWu9HnSd61dcF6o3knNGS8LRuCylC8rOUA5opQ_CFwNMnLuCVGbYuu1-YXYgk-6ltwBQt5hLRD40vGX7dDIRulnShBgeRleuUpHi2vKLAVNMNV8gTv8Dl1r-_avCE2PqvhBSsEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5ab333d5b.mp4?token=Su1Ahuae8kxbZSboMNzHWGa4SNkwIhExjePXb5pF6TyWJ4DCFhcvwqdPpWe6m393o7wMSZQHSio4KRFmGTDZEL4yJ9I16ads2fE9sCGutxbWbOTIUeymMyjXtDllKBudHz9y6IUq503QjQy8OYQbz-HJpEOkW55dAd10eEaXZ6u7xVOyp6d37_cHUp0pW9VMNS4CAqLIloMKvE9xWu9HnSd61dcF6o3knNGS8LRuCylC8rOUA5opQ_CFwNMnLuCVGbYuu1-YXYgk-6ltwBQt5hLRD40vGX7dDIRulnShBgeRleuUpHi2vKLAVNMNV8gTv8Dl1r-_avCE2PqvhBSsEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پخش لحظه شکار سامانه چند ده میلیون دلاری گنبد آهنین به وسیله پهپاد ۲ هزار دلاری حزب‌الله از شبکه سه
@Farsna</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/farsna/435138" target="_blank">📅 17:55 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435131">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gUb39khlNkk9MxtfEtuww7-nPsAgv7Bj3i44_jEki0ge1pNnVgNHUYSMspNA-i1TiCQe_Krpyp3_QZLbzqXS11chF69pwRangwTb0q8XbLNLcc_QU57m0nu0Spw_oBSuZTRB85ujUj4_8kY8sPTpE6dLvuk_mqcCR3XeknD4PHYrIOe_70s-hgUvwaocd_QDqT-o5P3UUYxuND0d5LcGzCUn870s2aQXNyI5B6STbwwqKTLJvVwvzfejJsqvzLshVFMTIj8GCkKKIGV34qzayGhwIMJO6E5gjvZYShowcvk14O38L-fNVShMNNs5CUaZzHXDQFVaL1lSqpv_qyjtdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IczG0EwMTKwO3ftrlTHkMNFg8mJbe_fwmjHyjvIDXH7rJExrt_be6et-_wOeY9Rs8GNlJ25kQXRLfyCuXP2_UIjA4jShCNsGDmCuc9BQYY5jyt275GMco0Bhxm-8IOm15HtCl-sQoJdoYnNxUJ7qLSUdXfBYnHNF7bV4qQfMl6VTczMBOcktQVeC2gh9kZLWa85Ys8io_93BWym1IyAdAX0LQHsHU_C6iKjGSm4MvJWf2GTVKVPvwouZwm5VEgtOcSMupWp8XGAyjQ2ajDMRx9dZEUtoqhs6BWSor18KXMZLvjfOC9fZrOFzrERb2H7B8vnF5C_oVNNv5K8EeBWi_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vr4ItaFn02lFp4A_P6viqoz0PMTFQhLbs7jXK-VpIX10_0cmYqUR13UEbxs1i4JX97Lx-8oNjF_dP76BmtEiz7dPVVgA3Q1VrMvEhmvc7EaPAIQNJcr807g4Sd_SpBwfF2vhH0j8GdCcU1sPDCYpT5ACYfgsknMnmfIV_LjNz8hzLSOOcbBRzc58C60rxrMxjtmra5443fWDcwoeF6luQZfv16_Qnhf87xSmtgPIKd_jvB3k-yC1_eFS_aakcRvOWDK1yitys-BnrZZbfO0dxV31wiJa3dsk4zyeLEUflI3o4AIHmMJF3Hlw6UdqeNI8Xw6b3Xb_IWQAeo47KEQX8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ekZUpj0gW0cKM0Anfm8_gOGpLgP9DSgknNnCY5CmEtvkooPMitwEv36jAuQ4NV4fnEb6ceWrT3u9N2PrTLDS9_ckJNXFIH7JdXphgb93yx6-unPtFmvyvzEn113SGO87uWrnTqUaqntkTaEAgjm9gx3FHbLZDw1EPmHsf_kV2MMJ3zMB5_DcyPY2VX-eFHkCHdUPCC14SdhCRVw1caBGpPQnlvC3XtStvm1FzpwIhdh0mCVrcMjJE_u9rpS4a92ZSkhRN0TDFWCc4R1FbRPCSG95m6b8sZm8k2nIO3pwrn-GqHmzld7O7geLNVGtIbnLDGsw8XprD9_LbUBE0OJcdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/edrmWs3VO5R9tSleffsDun0FM_9TU1PjRzb-hENXV3oTCrbUmBKqp_WubkHMQuC7zoTKfqgkfUrKFmdrUgehlr4t7oVUvUewRqR-5JNp7FpD0sP1VmZYtf8csNrUtLHD1h0eYWh1bWeyLHG6rrz708_9DzCC0OlXtcSId-hwv4jcgnm8bu8sM4xvumZIjyjiY38Qf3ez02WzyTyGO2s5vJu_lf8vBkQEFNvSyeNdx5qsSWZNkcvpQr0zxw7l3zrjZ-ZOTo5w2MtwE8_ASuokWp8WK-awAExejMkXV_qAYVNQr6aQSlWIiudn_zmAYIPHiTDHJhgQFRHH3ymSReViZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fGpS7Z0RWhJPORDthqu3WVYBGeaqMw0S158q-z9amTJmgVsNWtA1cJetWZcWTQcLW2UasElWFjtDJ36n_vKEwFJd8-5ucmTFgrTlZWyxxA20UYEUG5QXX0aj-FlFYJk67NbdrjK7JjrviyCJayL61TQR2QSUiZN6lO3lDTM5cv6JO9XkFi0GAaNrEtJr9YtWtiQtzrp0iJlCo6FA534dAylOQNXj_7k739OOjOI7wp4HSWSF1LplJhbLZaMbL0KjsQquz0b2aJJBKpJtSncrRuT_yqny28_cW3QpKp8IVFRKZM6jy5ZzPZ5bhM_cBKIXzjwYeHxgwYvFszQDfnydhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BtEEeit5U7rgCEvsJ49ixtec3qnshkvE5ggpYL6TckAbvKPbom9wBTUcWwm6-7DIHRl5b5eDiPqVOhR2TlP2ZcuW2t1j8rPfWaeXahXIP-wBsLYobASOkbMqhXjYWEH9rkvW6L76372OMl6P5zhrIo9ExlHVaNvmE3NW_TFymhNUpsIk9IGU8iBowKBxrgfO3uL4D-91_JfzAEnXH2DCZib_tRGBfxoyLsIOsIRcv8WdADw5ynkL4Oj_RYte5Hz8rrW4oDFG7TnCFqG6LrsJKHAuPY_YQcJwa4pEgPElWKJDH1_yX7SiAYslQpsOEFbCz3_EXLJFHlbq4XN9BytixQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
عطر نان و زندگی روستایی در دامان سبز دشت مغان
اردبیل
عکس:
رضا خانبابائی
@Farsna</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/farsna/435131" target="_blank">📅 17:43 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435130">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N2H7EI17U5vpdFLPbwatb1o8M8G88XPYWZetmNgub4xphRNXWf2RvzuUYbLM5lHic5LzePc-59DI7LKBc3R1qrqeZk_ZxIwR_u2UaPM9NkrMlRkibg-6eHG_l53BnI5aDO24jVLLWwSaimZ9BZnHpH8Lp9L4rk9joQ6jbkEMtl7lFWpAjiG8sTRtUTrJ9Y4woHwjax7JGH-jh6GYZ3C99Fo9WRYyCu0AYFMXJhmNnLEROdJar-gWIp1GzJR_CrEQzkW2Na6qiS9JZfMOvpAUQdOGCS3MrEYNPbn0jcKQ8nfCTY4R97aA1_IQhjFwfuaazsVgQgLVXON1LLoJP12m6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانهٔ عبری: زندگی در شمال اسرائیل به جهنم تبدیل شده است
🔹
خبرنگار کانال ۱۲ رژیم صهیونیستی: «زمانی که عملیات‌های رهگیری و تیراندازی از داخل اسرائیل به سمت لبنان انجام می‌شود، زندگی در مرزهای شمالی به یک جهنم واقعی تبدیل شده است.»
🔹
این خبرنگار می‌پرسد: «تا چه زمانی قرار است در لبنان بمانیم؟ آنجا چه می‌کنیم؟ ما فقط به یک پاسخ درباره مأموریت‌مان در آنجا نیاز داریم.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/farsna/435130" target="_blank">📅 17:30 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435129">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad0a7cb8b0.mp4?token=JuNqJB3DbOoRDDLAfvpliyr1hNQ-LTnDXNXr-Jb43D9GxO0W7I9GtR_r9rKodhmN9dA54ctyC6lUPTnVAE_Z5FqoprbYT4BYa5kU5ZsxZkbMKoh-LM5nG2Ye747EnseFRwJu_IXZPAULS4sGkP-K1FGH1O2AzT6XFVGvchdLFCD3aQamW5KOOikheH5MkmGMHcJRM5qXHBTGxJ4V4mn0sPznx074kZlGdWY9pRadS2nf45cPuymspQflt2oxphVOHdu4KStjQfaojwzhO6Psh3AfpOUcvF6w71lxW3hNTWucGv8Ib6ASb2o346ialwqMRZGOyvXD0rxhXywxCDaGYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad0a7cb8b0.mp4?token=JuNqJB3DbOoRDDLAfvpliyr1hNQ-LTnDXNXr-Jb43D9GxO0W7I9GtR_r9rKodhmN9dA54ctyC6lUPTnVAE_Z5FqoprbYT4BYa5kU5ZsxZkbMKoh-LM5nG2Ye747EnseFRwJu_IXZPAULS4sGkP-K1FGH1O2AzT6XFVGvchdLFCD3aQamW5KOOikheH5MkmGMHcJRM5qXHBTGxJ4V4mn0sPznx074kZlGdWY9pRadS2nf45cPuymspQflt2oxphVOHdu4KStjQfaojwzhO6Psh3AfpOUcvF6w71lxW3hNTWucGv8Ib6ASb2o346ialwqMRZGOyvXD0rxhXywxCDaGYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ضربهٔ سازمان اطلاعات سپاه به ۵ شبکهٔ قاچاق سلاح
🔹
سازمان اطلاعات سپاه تهران: ۲۰ عنصر در قالب ۵ شبکه سازمان‌یافته ناامن‌ساز، وابسته به گروهک‌های تروریستی و قاچاقچیان سلاح و مهمات، شناسایی و منهدم شد.
🔹
از این افراد بیش از ۵۰ قبضه انواع سلاح گرم، ۷۰ کیلوگرم مواد منفجره، ۲ هزار فشنگ و مهمات مرتبط کشف و ضبط شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/farsna/435129" target="_blank">📅 17:20 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435128">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">حملهٔ‌ حزب‌الله به محل اختفای نظامیان اسرائیلی
🔹
حزب‌الله خبر داد با یک موشک هدایت‌شونده، یک منزل مسکونی را در شهرک «حولا» هدف قرار داده است؛ نظامیان اسرائیلی در این منزل مخفی شده بودند.
@Farsna</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/farsna/435128" target="_blank">📅 17:18 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435127">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q8c9n7sRawew4cXAenxMR1MEaVVfJRF_hqSDskV1N0Glu56PDv5LJWziw1jheCKOF5OKo3uUrIU4HAuoH2x7A-XZSwKFQRkVbQGdla4mmYjCOyuRweh7fff3jbf0rTZ3-ur69AFQi4aaHFWaDFqP6iXIAaG26_SKQHZbbln5tVUcaFcDb2UDyjotZUyvuPYY96ShtbfR1LqnAZKrfXZNrZnbaZAdSSygmGbAW4IXCGPveHzMJBurEUOMfN5Rvgqu0ngAnsF9mlXUvdg_zCPSiA1HrMrjSeHY8fmLrYPpDuion3K8tDGdLOCZDZoGFrY_ZHjQqHw7LcmobSlo-W6fUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
نفتکش قطری در تنگهٔ هرمز متوقف شد
🔹
طبق گزارش بلومبرگ نفتکش «محمزم» حامل محموله‌ای راس‌لفان قطر، وارد منطقهٔ تحت کنترل ایران شد و پس از دور زدن متوقف شد.
🔹
سیگنال‌های این نفتکش که مقصد خود را پاکستان اعلام کرده است، نشان می‌دهد که اجازهٔ عبور از تنگه هرمز…</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/farsna/435127" target="_blank">📅 17:14 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435126">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QLOg_OVy77IAWpG7U3St2eQkz1glEq5cWWJ-hTNqya4VjVwsoYB6xcSN-SXbeRrPeNi1fek6U9wDCvqCxHlAlPr4xtX0-QRKClbyriRaZ51X6mg53cIjDnBrbdxOcdX9u3B4hJb7sQBl4HDuj9-FLsVupAYvh5UD7bb-WtxKcJbNJH22hreG4fKXup0rPzxn2oths_2NoDuZ2-W_QG0a1xeilhqmolLiMkssnEHS7ASwfX9DXsIbEbgzVshJIehk6esQAsCbJH3u6iKLbYZI6hyFfl2j1m4OOxW433QyskH8_yrZHIkbs3N3ldBo_1WctsbWRsNonjOKSfVvHPaAkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی به هند می‌رود
🔹
سیدعباس عراقچی وزیر امور خارجه جمهوری اسلامی ایران برای شرکت در نشست وزرای امور خارجه کشورهای عضو بریکس به دهلی‌نو سفر می‌کند.
🔹
رئیس دستگاه دیپلماسی در این سفر ضمن شرکت در نشست وزرای خارجه بریکس که در روزهای پنجشنبه و جمعه، ۲۴ و ۲۵ اردیبهشت، به ریاست هند و با تمرکز بر ثبات منطقه‌ای، همکاری چندجانبه و تاب‌آوری اقتصادی برگزار می‌شود، با سوبرامانیام جایشانکار وزیر امور خارجه هند و سایر وزرا و مقام‌های شرکت کننده در این نشست گفت‌وگو و تبادل نظر خواهد کرد.
🔹
این نشست، مقدمه‌ای برای هجدهمین اجلاس سران بریکس است که قرار است در شهریور امسال در دهلی نو به ریاست هند برگزار شود.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/farsna/435126" target="_blank">📅 17:10 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435125">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">جایزهٔ ۱۵ میلیون دلاری آمریکا برای مختل کردن سیستم مالی ایران
🔹
وزارت خارجهٔ آمریکا از برنامهٔ «پاداش برای عدالت» خود برای پرداخت تا سقف ۱۵ میلیون دلار به افراد همکار با این کشور، با هدف اختلال در سازوکارهای مالی سپاه پاسداران خبر داد.
🔹
این اقدامات در ادامه کمپین موسوم به «خشم اقتصادی» دولت ترامپ علیه ایران انجام می‌شود در حالی که آمریکایی‌ها خود اذعان دارند چنین اقداماتی تاکنون نتوانسته اقتصاد ایران را از مسیر توسعه و تعامل با شرکای بین‌المللی خارج کند و بیشتر جنبه روانی و رسانه‌ای دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/farsna/435125" target="_blank">📅 17:00 · 22 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
