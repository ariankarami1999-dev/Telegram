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
<img src="https://cdn4.telesco.pe/file/CTVfq0lPhVwc7XBGgMfy5ttbF_jA3hbT5CTEDLEFwy27SsAl1-QE-5PjVo_wW5O9B9WCBXA4UwfKDpqLjFKzNIK2ZJss7Q2PNYkZAZQZm-foi-VK0kKljP-Qukk38hdT6HU-EWe4WA2V0c3MIqOYRunDx-ULgISg4dPHJ_g3_tAZkai_01H3xY0_amUbpBeIzWH87vzv6SDsVPPnTdYnPARTcVc6Li0muDe6ivMRJ9GSAyZUqX9YXg2I5o6y74-0mgLVVbKpgEHsCku8eaOFMKF4ekhOim-4s7jHTC9VHlKqPM2XnfZxpgTXwRuoogOYJGIgckA6IFx4ztCHJ8-wWg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.31M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-11 06:32:46</div>
<hr>

<div class="tg-post" id="msg-695011">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔥
هوا دیگه کم کم داره سرد میشه، هیترتو بخر!
هنوز هوا سرد نشده و قیمت‌ها بالا نرفته؛ الان بهترین زمان خرید هیتر ریموت‌دار
HANDY HEATER
👌
✅
توان ۸۰۰ وات با گرمایش فوری
✅
ریموت و تنظیم دما ۱۵ تا ۳۲ درجه
✅
تایمر، نمایشگر دیجیتال و خاموشی خودکار
🔴
قیمت 1,990,000 تومان
🔥
🔥
تو 4 قسط 560 تومنی میتونی پرداخت کنی
ضمانت تعویض سه روزه کالا
خرید از سایت
👇
https://memarket24.ir/product/brief/35574/180124/
مشاهده حراج آخر فصل
https://l.memarket.me/lp/15/180124</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/695011" target="_blank">📅 00:30 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695007">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BN7cz-BBsGJxBbcG4lYV1_N1A5tSlh2A0pJN1ZByF2WQYIyEl42zB7Cpy8DaE13k0djVTN4u_LAkgSCG8bRptsMYIwpqQU1oDCMIw1cAGo3fjiT_dtiv4SPQ0WrZapMQQ1sO6PLvbxSinLDLPKci2c4eMnfy9L0-W8n2PwsUBN9tyfEvWRPBytxzoLH4T6hzVp-k07sCa-yku7LCZ1HVQ-LD4A6jX0JGL1chTkY4yooRrBWqpbDuCeYOzU4YpazKVMuI4kbSr04XwkovlN0qUXVywKSwg0kZlQXiuyUDD_MnRdHJkVTVmQsGabz3G5ktQXzUWu72flmlb6a9pScjhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hJATFHDWYv4Vu6OKifEUTbtItcvCalaZypQ0W425AJmFWknQ__BRkKtvntN5CunPqGU4sT5Slo_vuUoNeUdXZT6c4qzAmFk2iedFWBCiRZ_iEa4_pd-2bDzMOgThlpiO5dNfmf93aEHneSSH29YUf1X73GuZqGXQdvfV3qmigq5oPan6NgBP87mEK2ky8TttXTQD5zV0OhMmR7jU-s_QbcQI_Vk2igNBXJoHbzMl8dMI8PE_SXeAPb7Pi_j7AiEG6LwoC0jgNskK4KA1IREfyMVkIFjop8pFthKZ3unU1nsinuG_dy4juOIq4YkNL9YxBJSw84MFP8hbRfSaDdEoVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SqPfpLdY1ZlAnO5Rts1J7HWy9ymxo39Ur8ytA2wL1ecnrVAym7p3tuVua6QM-sJF9iQVDt6-rcJ-8w-pNPKjUAV8uWcec4ooccBuGQ1XYxo4y8LQIbaerwpYX8JLWeUx8S-74kJblmrytkgQlgX5gjKyDuguFenLnxTf0n9RpB5vGROjFxGDcbp7B1LJvdNt9kGZO9AVDl2U--maqh5G6QpMOTSlV8aJ3XY5AlNH0cNt6AuD4p2ppZLScuTk-CRkTSsH1MLJoLZW-7HhNGM98pA2cHDTOiFkgpa8wNZzY5NtLcJbdbrJuCYn7elnakpb_FF0HkO7lggzWbS-xmWQgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pQyxCPDskCTqtNDk8rieK0hG3QXF9oNqPn6mi1xatLetlSxE9y-iviXelSqqEqa9lTnL7n5agRjGtxMH1mQCKh5A6o9l3qj9j6LUuOgTc28DWtXorj5z3AzZWDCwYwBYK3ngVmE3ecxvNoQb3E8-iJZDfRkfnCHc80cmK9OKg8jMd2WHu90n1rB7bdvJiL7qqTuvrtSg8ynayT6FEdsqYYfiOa_7BAseEoMycDep92EXuXkSyLh-8KbGvmil3EyJ3Uj15Cmefigfe_0A_KvSM6xSS0vpc3zqcwn4NwSyuM1yhev2Y2Bm67cS6TZJsJOPn7fr1B44n-4iCmFpdo5h8A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۴
مدل لقمه خوشمزه و سریع برای مدرسه، محل کار یا یک میان‌وعده متفاوت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/695007" target="_blank">📅 00:25 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695006">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
واکنش ترامپ جنایتکار به احتمال استیضاح شدنش: من هم می‌توانستم این کار را با بایدن خواب‌آلو انجام دهم!
ترامپ:
🔹
این یک استیضاح ساختگی است. ما می‌توانستیم همین کار را با «جو خواب‌آلود» انجام دهیم.
🔹
من می‌توانستم همین کار را با هیلاری کلینتون انجام دهم. اگر می‌خواستم، این فرصت را داشتم
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/695006" target="_blank">📅 00:22 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694999">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dx3z6AdKp4u06MG5Sv4yRgC1t3kKyDcBUL-E0DhPhsT8aNgAk1Lgr8ZBdZzEBQcutwUpWxB-aLG---4JlBoqsy98qflNj6vQqlV9LUcPQDvSTXjUqpoZULIt46zIowoXvhswvLO9gB6xnpHPdMPBOz1UEzjM-CifVdQhrHYHHocDIbKxUBBG59Km2-Z3jOxVEoU2pBKU7NlxSodXZTIqacSK48uj5Zi-JuUhTouhiiWXY0PZwCyQfY4bh-tZzqFranpNytksNs1tq-DikSUpKo9NCzOuo7dFUAdraPUY9he8r_Rdp9gnU8Wb5TPeL6Of6Lh24oxGhE1W6ThBdWSZFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ksVHYUvogczuRgc80OQQE9U36fisc4SIECWwHHDLIbLC3FWSKPhgvx2lY4JwAEKoAdCK1K5tYpLo8OIShq6g104in67h1h1P_xmx3OxD9BcnGJ8p1NMPnQRDFZpGsCtrMSCAFIBDNMTpjkFnFzxxPhL9kLxwef3WH0Vb8qjusqjfntfNSo0E4z_RfoIQlEI19V9qo1vRELbwBbU7laFKBLAS0GwUNETC--n8iuOwqsiDJsZushNRRdMzzNovQaExayudTw030Q3_bTKuZ5eEgEWaRM_tutMiBIJTbBe-F1K6q6MpwxuEYxjwM7N4H34D3znwnGuz7-H3cQXNDN8guw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LJjBNGrw-BasIWBHB6bSkH9K5wGdG_djFnA-Q5WaIShx1Ol5uL2sGI04aQhIg3yIjlsXXhvXsQcZx0ZkeHHKw6K89H6jS6Z0eXpbz7N7nLYZoaVZKXVhU4lNWjUj9T39p6cNCX-MfBrCPjCsV3FXB2ZD5NGS7_3XcOL2SUWlKzGZCw9WRtwk9k61iGIJjzdw4eLpEk9Hmeq_PgGdOnYdtns8uJOkcrMNd8cl6CQvgWL5b2r9F0rwaMllsRShEIBykViu-llS-eSqf4-NO-LYNMfzprjmJAad35wl6NYMwSe01WPIf059lgjyDjr2vdBK1WJ9xxzVoEDCsfHSqhXAZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D2n4xo9NDLAxgnttF2hADRferTiq-GOfhGNyytskDGWi3dyiTyHZYi13JAinEtJqwsayPI1SQfAOxJ-ecOI0ZFh_VJKL-W-I-KjpJQt512QH5w3HS_kC_Yvz7KlecNugGID1pY8VHgQ1aHBRpYIAxIsW3pBo_d3tg-Xi0ORkaUE5FWNf1ip7XwJeRonig6NUNRTc8snnWRnFYWRlkg_eMep34enYQIrK8xAfrIIBdhZbyvWjmZl3Xm5s_xhc4AIQvNOflpXSYsd1Mm42nW0TkJI2EHaFtEErLdxAp7g1oS7QkP4wgR-2Y7hahtd_HvPj-FNOGUDZEcf1XE-r08hzWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EqDot-Y4gw3Z5VcuWe-ATbh-7fhoWRrCpsF4tkkjCK6gWExQfjN9V1fYf_S2oyX3jHnLr8nOuKjX7rFW_I7RSKd_LMJiUPW25dJr_-LZmu0CNcC4ETC7YdDA5nBM7zb_iNqKLJlx-b6yFLt0B20O_h-6MfDtJOmrTaR4GXHmeu9fy7Z58n6NkKlHDW1rL0rAVu2Crw4oYw7SqP3eiNoY0FYIzdLXeZFG756yLugCpBTDP_-JAqqE31B2HE20UpqC8DWNecCdJxHPm9qespdO01VdJyCsTNhOdoTBRE4Ma9L_-z45XWSCfD2i4EBZD5kQ_u3TLw31ivNDul4jxXSfXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oy3Fv9DAHGiCFtiPKLa0nSb-6eRpdmkl4C2L-SGT19R_sg1IoXjL_4qlIHPuI4knj5c3dgsxuYLBDUFhROjo9G7obKqvXoPM0wX1qLW3b6I4-3eJCUMdvmtTwzQU1FqbFfbtN--xeToDlCcB2YfSH2i7vEWueI7y8T8PLZmbLrpOkxE8XVH_7iBGQfTTqY3i083gJAD1Joe76GVfgLIghp50ixJ9_lr0U1RoCnE0EcbysZXJUPVbAN8W0SZ1pZJHes_Y8XaUd0f2jWhp8rWADPK4oVj3rx1kzx7Mrbrbvgp5-wjDaxppzh878veTX8E5fXUF0ntApfrlKroW9SsWHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bPvyNjbYJNRT-OTbnz6uBO127r3oaJn5F7wqSDZjV1IG_GNJiOFipJysnMaQMTfRQVVbEbP3uxd9aGeBmObc1rQu8vd6rBKFnyNy-gZq0o7hNaUy0XUh4DnfiyGdz0ZhImLVp_LLDa_atVbkmEYvb3Ut_ltFmEuj9so0jpd9cpIuYmYndgiKem1JQpcHOx1YG-9fGtLbeaRQIRJJ_8E9D9awE-B9_jDWLGNDpPXX_t1wBJVdQbqTWB7S5dL_7q3nV6sArXtNE3k2D_4G5P8Yzs7g0rk0pVXGAzBH55B_BV8lZmIdyiIvo5YKpmzW1ToTPG5DcQk6mUtsAsy5sJ_wNw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویر جدید از بقایای موشک کروز تاماهاوک بلاک-۴ که از آوار مدرسه‌ی شجره طیبه‌ی میناب بازیابی شده
🔹
روی برخی قطعات در تصویر مانند عمل‌گر هیدرولیکی بالک کنترلی دم موشک، تاریخ تولید اردیبهشت ۱۳۸۹ نگاشته شده است که با بازه‌ زمانی تولید بلاک-۴ موشک کروز تاماهاوک هم‌خوانی دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/694999" target="_blank">📅 00:11 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694998">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bC3Z8NHZsbmvDzDAUTIdrJts-zZG-tD5trIui7rBfEXGDQzbthCcN-lUUy7QrSKZgEAAtQUlGMoZ7MRHZCd4wEHEaNT2PPipxOSMjAf9TmrhCoL830VOU6d1fxHOMNwtcOJ9K7vTUs0i4FNENkWmP2abq5PrTqjhsPEenzx-5crqSbwEP8qsoGHNyT8Wwco4xpwhWDAhXgH1Pfjzi3BxKu-Uv01p9RxLeOyUi9ldah9s2u5a0_8EyjthIkg6cWPyM1poImnFKatO1NFmRX8Q1Jg7kqYmCmuJPFTDgbTn-QbNeis_WaCumMwK4yZjeIGKtjppxh-O2ZDyC1MzfICQLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بهترین خوراکی‌ها برای عضله‌سازی موثر
💪
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/694998" target="_blank">📅 00:08 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694997">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
حاج سعید حدادیان، لبنان: بیش از هفت ماه است که مردم لبنان آواره‌اند و تقریباً بدون امکانات در یک مدرسه زندگی می‌کنند، اما با صلابت ایستاده‌اند/ با همه این سختی‌ها، حال رهبر معظم انقلاب و مردم ایران را از ما می‌پرسیدند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/694997" target="_blank">📅 00:01 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694996">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IG4a2ONofnal2vrHimVsF__MxZ8m47G6jQ7tqBmnrMjzRhquKYhlwCb940lPty6XrkEHO35tOd8KkqSOsqLgx7UmXqtYsxMv3YvOV71yKDIi84VOwq91xXd4UG8mV1pr3wsirsRCTSgncLb4Z-7izkfvciVrZmdRW3_tQ4H52di-PfN4RLU1jT1YrdHs6J6c8reVmGTnOjECdnCmb7o1-nzpBm1cxl9KLUEdvE4VZDQw1ZpEd8EzSG5HU1aR9AHeVAu1fzXtEXA7RwHe0txw0kT8lkTRxCG2am7--x7wJGufORwl1oNQQjOO692DiIjdenBmH9YKJjV_Ugd65moaxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/694996" target="_blank">📅 00:00 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694995">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f58dabdb74.mp4?token=oCvWHF0ejdSZpby3wMQahZxFpZ67yqzaKcz7WvpyxunuESLvb4lZkoDhhU7FGgPtPjap_wcdBebXtXZQMubE5MYQ-H2Jhz_ts5GcpIER7YVxHzUcL1y67uUPbKH1pDK6sJ0KAzi6b1jGXH80aqek-GV2iG_i7OlET0r236giqaqh3hl_ZyqAbtdSeDNrCSuuLfUIt72j--SukfVP02xf_zvN02WljigmeDPF6B7IuvuuyrK2g5l0EONvuJ_om2jKcb5s01SCQpndkodBlCw7AC8E-xeK8OsQZ2RbPF_V3jZZRovQfQ7csYcb1xZztZyQLErZLvrEg70GJBidLzwrnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f58dabdb74.mp4?token=oCvWHF0ejdSZpby3wMQahZxFpZ67yqzaKcz7WvpyxunuESLvb4lZkoDhhU7FGgPtPjap_wcdBebXtXZQMubE5MYQ-H2Jhz_ts5GcpIER7YVxHzUcL1y67uUPbKH1pDK6sJ0KAzi6b1jGXH80aqek-GV2iG_i7OlET0r236giqaqh3hl_ZyqAbtdSeDNrCSuuLfUIt72j--SukfVP02xf_zvN02WljigmeDPF6B7IuvuuyrK2g5l0EONvuJ_om2jKcb5s01SCQpndkodBlCw7AC8E-xeK8OsQZ2RbPF_V3jZZRovQfQ7csYcb1xZztZyQLErZLvrEg70GJBidLzwrnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۳ دلیل آسیب دیدن افراد در حفظ حریم و حقوقشون
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/694995" target="_blank">📅 23:55 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694994">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
خبرگزاری فرانسه: پلیس بریتانیا دو ایرانی را به برنامه‌ریزی برای انجام یک اقدام علیه جامعه یهودیان در منچستر متهم کرد
/ انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/694994" target="_blank">📅 23:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694993">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
وزیر رفاه: معوقات افزایش حقوق فروردین‌ماه بازنشستگان در شهریور ماه پرداخت شد/ معوقات اردیبهشت‌ ماه نیز برای گروهی در مهر و آبان انجام خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/694993" target="_blank">📅 23:49 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694992">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/361e266983.mp4?token=viXcVfXwIDSdTZ80FAJNH6ugEsSEIw7Z9Ac3aiXyHb-AP5rcptRxjosrG7L-kbcqEKWOXF4uDe5GiHudRIaKDRPACHeUuOBFIPCX53AEu3MG0JBmTlNrm-g335L6T_NQWyTkM1aJUYZz55gmoRb3CNuyp1G21G54VhIZc8lZPSx0TTOQhGFXFGNyaFbcbmW3mExHu6QNF4SQTHQrlUzze1rj0-IFgc5qSQdfPmgwwbXW6QNAqk4S-__-gUjy5EjBQjMJEL0DZW5lSHgGrIvr2di0EthKKfJhIAXjVP2aZaA7bsMkkhl94tMyKS-hF1X8fRo2Qj7M2v1VgPS15SKVWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/361e266983.mp4?token=viXcVfXwIDSdTZ80FAJNH6ugEsSEIw7Z9Ac3aiXyHb-AP5rcptRxjosrG7L-kbcqEKWOXF4uDe5GiHudRIaKDRPACHeUuOBFIPCX53AEu3MG0JBmTlNrm-g335L6T_NQWyTkM1aJUYZz55gmoRb3CNuyp1G21G54VhIZc8lZPSx0TTOQhGFXFGNyaFbcbmW3mExHu6QNF4SQTHQrlUzze1rj0-IFgc5qSQdfPmgwwbXW6QNAqk4S-__-gUjy5EjBQjMJEL0DZW5lSHgGrIvr2di0EthKKfJhIAXjVP2aZaA7bsMkkhl94tMyKS-hF1X8fRo2Qj7M2v1VgPS15SKVWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای تکراری ترامپ: ایران در شرایط سختی قرار دارد/ به محض پایان جنگ با ایران، قیمت نفت به سطح قبل از جنگ و احتمالاً حتی کمتر از آن خواهد رسید #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/694992" target="_blank">📅 23:45 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694991">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
حاج سعید حدادیان، لبنان: انگشترهای اهدایی رهبر معظم انقلاب برای خانواده‌های شهدای لبنان مثل «خاتم سلیمان» ارزشمند بود/ وقتی می‌دیدند رهبر جبهه حق این‌گونه به یادشان است، احساس افتخار و عزت بیشتری می‌کردند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/694991" target="_blank">📅 23:44 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694990">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6212815d00.mp4?token=Q201ICBCQyN8SbxRoD4XQmmet8dvzC4kJ40Qh4eezps3ytfBEbgrOYOJijqx2YHbqTX7b3rFq4hyrk7qAKHWlNkaZD6VmmTRJD22Zxsf8THGCwD50XvlGSHhOZWY1ZKbAnBZCuruYpXr3sHO8W_7VPw9C46XRiFh4MY3iOWPXk5Wu8WxcgbuhNbQQfDL9I8M79O9zEhAhKHRhhBzoKOLH8Kc2_9Y-ezx1tcVFopLmYnGocCjIJy9JM9YAyBEua8HqaVWvUwK-Gpuxs8E0Y8-6DKaSt0RE-17uwOgZmUV9URywi_r3pSYZzb4WdJoQDuFQgbaDVlWoSH5_FoWE5a75g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6212815d00.mp4?token=Q201ICBCQyN8SbxRoD4XQmmet8dvzC4kJ40Qh4eezps3ytfBEbgrOYOJijqx2YHbqTX7b3rFq4hyrk7qAKHWlNkaZD6VmmTRJD22Zxsf8THGCwD50XvlGSHhOZWY1ZKbAnBZCuruYpXr3sHO8W_7VPw9C46XRiFh4MY3iOWPXk5Wu8WxcgbuhNbQQfDL9I8M79O9zEhAhKHRhhBzoKOLH8Kc2_9Y-ezx1tcVFopLmYnGocCjIJy9JM9YAyBEua8HqaVWvUwK-Gpuxs8E0Y8-6DKaSt0RE-17uwOgZmUV9URywi_r3pSYZzb4WdJoQDuFQgbaDVlWoSH5_FoWE5a75g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چند خاصیت طلایی زردچوبه برای بدن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/694990" target="_blank">📅 23:39 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694989">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
ادعای تکراری ترامپ: ایران در شرایط سختی قرار دارد/ به محض پایان جنگ با ایران، قیمت نفت به سطح قبل از جنگ و احتمالاً حتی کمتر از آن خواهد رسید
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/694989" target="_blank">📅 23:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694983">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RsunKbRPfbJUvgzNumNFkvwo_itEwT--EPzkMBSDQ89JhhMhoC1MSDpqbIjKgwlPjQRwntkoFe0Npog0BSiN3oudE7L1lK2kOpTBNFylJaEi18vn4uCwI2a60xRAiKxgx92XV4zXXeqgjlx8ul8XXxcl3dxjEJS9rDaEqgqevJeFcoGBtQsQJrJzgfxgmXczoP0AXnKGwbsLAizCQH8wQSPGBZaCpIP8wVssxjpHvyYGWqfYlHjA6slkoJeh0_54uHKr1YrOf2DfXZyzsuLnlnBTl18c_rySRt8vgITU2z2FMzURpI_8Co1jIVUmfuRSQ7Dk0OJxGxqgzRdmtDwRnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CdqXsEA-wG8Nw5PHcEj10n4r2kbJVc40QsO-f4Vs6BWY1LoFOV7CMq8uLdicyS6mwM3T7iSbFTpvmNkp0_bUfOyzHyb3igpgZ7hyDl0_WP0i--sJqe6j4p6ZmVHn-zSAj8StO14pmcvs4qVcop1TCxJg-Ur5VqzpOJX-7pH5rZcqqqdjKe55dozXsAQBVTbyCz9uxfiHEUjiHbxyj98vcf3TXXXghon-ABJxtrOqO_QVVbUuSy9ajrik39q_4Dk1hSbVnz5w85jR8urLwehoALHQLdhRZYdM7NI1kAUf9TYvmbqNODm7QJ3XCrEYBNuaObSy_5JXjGqLWNql4sr4Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GrIxBcwhMMtZ_YpUUlzdEKNYYqifs9L6uVHL-oGqd9c4FJKTIPfpVK7oDynU5nc-xnuzihDOMcy0-W5qHhsytC-iTNJB5Jb3Zz9Ju9H7r-nHcI66XJMjoEuF7O4uUj8w7o85HC3mOlBm4bfOyfxms6sDbKwhoEj2-0IbnxLoJh4BpaQPfleZGSQQGkuuqZF2it5DMGuciL7norrbAQCCASOsHjxsJ1PzPgQzmss7HHOxdJelnzwnfDxZlp_fMthgrwhxuJwVTo1IbxXwMljgPSn6VSB-VP0EWrFtDrEqvPo49jfPU48RDJaZapv8YdxdqkIg91O1XujnH2p7YD9qwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rMxv6JhPA_Kno8Y_vsBMTtD0jW7Nl2kf32YoJBOFwTGisCY1jiucjKFl5B_1yGD4mPmNp3NyhdZJbf-4tWt5TN0U-PfdRmI9Op7KF_7MdSypbWWX7di9Z4-Cuv8yE2b9E8JMme_1vxNZRQfwtJF3fOAOtiiA22IQ28oQPbUYvyF5N6MVH2XJXmiHZGd4CS3ydhzM8Prri1b2P4d4YyKeSWuOXwjwC5okr2gVGN1F_DNZXcorevxzsTiaUw9fG3D2nYpSL298IS6kMJKHgIWIEFjYNEiN6cLJAi4Tr7BXDMRaUCSaxwSoezGuu5jX_oKu4S41FJRzk6qCQ04BEcQdWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XmsTaZIiL5pajHcIxuhIKI5-yKjaRxy_1begmRKfbP9EocDidE9L1uazMjE83tBWxMtRBlqQOkepP51HCfxUVV3bRBxEmAIDbgG1GWkbnUW9OteJFC1g2eX2-KP1lYxqDDy8PdjPaWiFO1cBkjbOIEJV6W04gGZVwztHy8y1-NbiV7is0UxSGu9rX8zECn_3syt-VqnoWnKwzvv_Qltf9FVmi6GxJLS7iN_L_oKSKIbgxBaY9KBCiWqqi5alJoRaVnAPIZ-H3ZKbhvpX0pPg1956tYuikGaP6FC9xy0UAG4wK3euJ7LBAgy2biAjIblw75XIvxt3_lgBsuj-kPF3tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QGyvJdrWJwNfKOrqi7byaRjiMTWa7uGSmCyfHUXp_7yxBVg97hiWHde9b9cbH8g1jb3R83TuCMilrijNPtOW5OJtJ3fCyl8EmKLBw-yEWVcPK_E_vZqM--Lje6Z4jfCfuJhPxOZ4-Z2djyHTZ072T3F5MICl5hJrNMZsnsqLxS3_8o0azU0DweKZTX7M2Nf4MdMF8Puiee6vuhPQJZBx21Q0V6aL5dD7pLAT2qxzrszE-uJCXOVCqnXSfhycX7iDebVn_BuLJqFSPS7nKOkIskN8-noaMIvIyKZAwdS6yfxwUQZ0R4zz5lOavJGRh4Vak8NmR7TRF7mOzM0vmIxFJQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چند مرز جالب در دنیا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/694983" target="_blank">📅 23:29 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694982">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
حاج سعید حدادیان، لبنان: در دو جنگ اخیر تعداد شهدای حزب‌الله لبنان دو برابر شهدای ایران بوده است/ این خانواده‌ها برای مقاومت قربانی داده‌اند و نباید حمایت از آن‌ها فقط به دیدار و سرزدن محدود شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/694982" target="_blank">📅 23:25 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694981">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6985af1efd.mp4?token=W-GopAul8gUxTymxsQY-USe5vhVOjXxzwA4v_U4LyRb2r3jlF5jsMDl9ZENYTB3fFV9cH7AzUlXRD9y6PZ8fJON2bB8soCNg2sYOzFQst8nGdhB_H07MRqcT0j_tfJTl2IZiy1arkeeoTdLbkTsCWRf7mbyW9YcFv-bKFn41Ln9-nr8N1gXfNccF4ahTOloHvq-03qsS3JnVuRlbdltSqnoj7HgrhM1wVWQL55kSjGKO52q3U_aJ3cLLDIDxSsWb_kVrZjUXoPV0cxRdDhgcoDv5M0-13Hs4bDVsSuSMmFPM4RNSBN9QDjzStvllWcj1Upi0iD33pwFX7fk6E8FBdjOkwq9KhMZ0yynglStAXGEfQPIzGWNhR3mnMl5CxDsqwGAz37jUJKrp5Jen_NcRhJymA2Y3vi1CXDlwuqViqn8oVVht96IeQARM9ZP24penbAWsmoukWvgHM0n7VIvnTleVkAChHAW0Pe6VxOulK1owV4lph5Eu1IeS5Olb8MBJjnx3B6L11GHkK7hLp2lctUVIg2_wXOmwnT_HaB1Hyudz0l4DXvaro3W2HGNS0fUuwhjmgGYAwRoj0Ao_L4t_LyS6VsQ5yfBvDk_TRtZTQy2HTO1qyscFaSLkouf-dMGxJg2zlccUdr0twrp5PzjrtzELdDV22QGbnV5irOQdn6I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6985af1efd.mp4?token=W-GopAul8gUxTymxsQY-USe5vhVOjXxzwA4v_U4LyRb2r3jlF5jsMDl9ZENYTB3fFV9cH7AzUlXRD9y6PZ8fJON2bB8soCNg2sYOzFQst8nGdhB_H07MRqcT0j_tfJTl2IZiy1arkeeoTdLbkTsCWRf7mbyW9YcFv-bKFn41Ln9-nr8N1gXfNccF4ahTOloHvq-03qsS3JnVuRlbdltSqnoj7HgrhM1wVWQL55kSjGKO52q3U_aJ3cLLDIDxSsWb_kVrZjUXoPV0cxRdDhgcoDv5M0-13Hs4bDVsSuSMmFPM4RNSBN9QDjzStvllWcj1Upi0iD33pwFX7fk6E8FBdjOkwq9KhMZ0yynglStAXGEfQPIzGWNhR3mnMl5CxDsqwGAz37jUJKrp5Jen_NcRhJymA2Y3vi1CXDlwuqViqn8oVVht96IeQARM9ZP24penbAWsmoukWvgHM0n7VIvnTleVkAChHAW0Pe6VxOulK1owV4lph5Eu1IeS5Olb8MBJjnx3B6L11GHkK7hLp2lctUVIg2_wXOmwnT_HaB1Hyudz0l4DXvaro3W2HGNS0fUuwhjmgGYAwRoj0Ao_L4t_LyS6VsQ5yfBvDk_TRtZTQy2HTO1qyscFaSLkouf-dMGxJg2zlccUdr0twrp5PzjrtzELdDV22QGbnV5irOQdn6I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصویری پربازدید از ساعت هوشمند در دست رئیس سازمان پدافند غیرعامل
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/694981" target="_blank">📅 23:22 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694980">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
ایهود باراک: نتانیاهو دنبال به تعویق انداختن انتخابات است
ایهود باراک، نخست‌وزیر پیشین اسرائیل:
🔹
بنیامین نتانیاهو در حال فراهم کردن زمینه برای ورود به جنگی است که برگزاری انتخابات را به تعویق خواهد انداخت.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/694980" target="_blank">📅 23:16 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694979">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
وزیر امور خارجه پاکستان: نباید هیچ‌گونه هزینه‌ای برای عبور از تنگه هرمز دریافت شود
🔹
به‌زودی نشستی در ریاض برای کمیته دفاعی، سیاسی و راهبردی بر اساس توافق مکه برگزار خواهد شد.
🔹
بیش از ۶ کشور خواهان پیوستن به توافق مکه هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/694979" target="_blank">📅 23:15 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694978">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
ژیلا صادقی، لبنان: زنان لبنانی به ما می‌گفتند «دل‌مان به قدرت شما ایرانی‌ها و ایران قرص است»/ این حرف را از خانواده‌ای شنیدم که هشت شهید داده بود، اما از اقتدار و آرامش مردم ایران می‌گفت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/694978" target="_blank">📅 23:13 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694977">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
وزیر رفاه: از این هفته بازگشایی حساب کارفرماها مثل انسداد حساب‌ها از یک سامانه انجام خواهد شد تا مجبور نشوند به چند بانک برای بازگشایی حساب مراجعه کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/694977" target="_blank">📅 23:11 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694976">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0292f00aa1.mp4?token=V-rerDKL7gcewQnvEyExdxtJ31xXRUmeZvv8r9jFHXcWrHNj2hk86GDTEKfSKWeJGUHkaE2rvqc06UR9WIpSLxyPHCxItO0EI8m3W89dFqpnJEm7KvUlmK4VwyjlC9qoo4lAsr4aghtck-PAum55mbbE_UThHwKnE_0uMneZBbB62LRL_xUqvUGFJuFlPBDM0AftOqCYwZhCfN_Pu8iqtWwi3C1j7Rwef0Wk_w9THhp4rZX4V-xRIpv7olBFxh0_ZzdbptLzTjDw0F7DpqQRSwUOcwqir7DOS5O59g773yXumh9qWXN8nQbyB9-UD8774iDnlw-L_2SecrZa_Zo2Gz9deXERUcxU9JXo0WlT0msAGkAkRwlE1Ni3iibP5tQRJOAZF3753tQ11xvhnip2vo7zEFykAJ8nWUQA7zrhqtxuHtOxwvAf1hOWbfq0IjQ1w__gZiT1D5j-SnPfTPlH5t33yHniECiTW68TampGdCNFji_gurHihn50sHIM_E7HtxOvuPrpa7egv1z0CKSzFJlzYBKxxn-uDPvNw6YEBMmRZJSBYpfd13sv496XvAxCeaOh4CL_uRwhlyUrN34W9HsiX1kHv3ZeXWOlGEPKIzFq_pQCANjksDX9bPy8dd7Cgm6JDSbFsLtahZi4-GWnlhBfoejS-QdG4SkAEDhrWrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0292f00aa1.mp4?token=V-rerDKL7gcewQnvEyExdxtJ31xXRUmeZvv8r9jFHXcWrHNj2hk86GDTEKfSKWeJGUHkaE2rvqc06UR9WIpSLxyPHCxItO0EI8m3W89dFqpnJEm7KvUlmK4VwyjlC9qoo4lAsr4aghtck-PAum55mbbE_UThHwKnE_0uMneZBbB62LRL_xUqvUGFJuFlPBDM0AftOqCYwZhCfN_Pu8iqtWwi3C1j7Rwef0Wk_w9THhp4rZX4V-xRIpv7olBFxh0_ZzdbptLzTjDw0F7DpqQRSwUOcwqir7DOS5O59g773yXumh9qWXN8nQbyB9-UD8774iDnlw-L_2SecrZa_Zo2Gz9deXERUcxU9JXo0WlT0msAGkAkRwlE1Ni3iibP5tQRJOAZF3753tQ11xvhnip2vo7zEFykAJ8nWUQA7zrhqtxuHtOxwvAf1hOWbfq0IjQ1w__gZiT1D5j-SnPfTPlH5t33yHniECiTW68TampGdCNFji_gurHihn50sHIM_E7HtxOvuPrpa7egv1z0CKSzFJlzYBKxxn-uDPvNw6YEBMmRZJSBYpfd13sv496XvAxCeaOh4CL_uRwhlyUrN34W9HsiX1kHv3ZeXWOlGEPKIzFq_pQCANjksDX9bPy8dd7Cgm6JDSbFsLtahZi4-GWnlhBfoejS-QdG4SkAEDhrWrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این سگ هر کاری ازش بخوای، انجام میده!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/694976" target="_blank">📅 23:09 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694975">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
پاکستان: نشست توافق عربستان، پاکستان و ترکیه برای بررسی تعامل سیاسی با انصارالله برگزار می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/694975" target="_blank">📅 23:07 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694974">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
حجت‌الاسلام پناهیان در محضر خانواده‌ کم سن‌ترین شهید سال‌های اخیر در لبنان: پدر این شهید خاطره‌ای از پسر شهیدشان نقل می‌کنند که بعد از حادثه پیجرها، این شهید اصرار داشته یک چشم و کلیه خودش را به رزمندگان مجروح اهدا کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/694974" target="_blank">📅 23:05 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694973">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
هکرها به سامانه پیشرانه ابرنفتکش آمریکایی نفوذ کردند
بلومبرگ:
🔹
اف‌بی‌آی و گارد ساحلی آمریکا در حال بررسی حمله سایبری به یک ابرنفتکش در نزدیکی سواحل تگزاس هستند. این حمله سایبری که تابستان امسال رخ داده، منجر به دسترسی موقت هکرها به سیستم دیجیتال کشتی شده است.
🔹
هنوز مشخص نیست هکرها چه مدت به این سیستم دسترسی داشته‌اند و با استفاده از آن قادر به کنترل چه بخش‌هایی از کشتی بوده‌اند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/694973" target="_blank">📅 23:03 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694972">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">صد میدان 4- میدان چهارم، فتوت</div>
  <div class="tg-doc-extra">علی مقدم</div>
</div>
<a href="https://t.me/akhbarefori/694972" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
شرح صد میدان خواجه عبدالله انصاری
🔹
میدان چهارم، فتوت
🔹
فتوت به معنای جوانمردی و آزادانه زیستن می‌باشد. در این نوع جوانمردی، آزادی و آزادگی در کردار و رفتار مشهود است.
🌱
در مسیر فتوت شور و شوق و ذوق جوانی می‌بایست جاری باشد.
اقسام فتوت:
🔹
فتوت با حق (به توانایی خود در بندگی کوشیدن): از جستن علم ملول نشوید_از یاد وی نیاسایید_به صحبت با نیکان بپیوندید
🔹
فتوت با خلق (به عیبی که از خود دانی میفکن): آنچه از ایشان نداری ظن مزن_آنچه دانی بپوشانی_بدان مؤمنان را شفیع باشی
🔹
فتوت با خود (تسویل نفس خویش و زینت و آرایش وی نپذیرفتن): بازجستن به عیب خویش مشغول باشید و عیب خود را بد دانید_شکر نعمت ستر بر خود بینی_از ترس نیاسایی
#صد_میدان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/694972" target="_blank">📅 23:01 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694971">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
وزیر رفاه: دهک‌بندی خانوارها به شیوه قبلی نیست و براساس سطح درآمد به سه گروه تقسیم‌بندی می‌شوند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/694971" target="_blank">📅 22:59 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694969">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/816b2002b3.mp4?token=T4qDOFdy3OcjknBFk-W6Gx4CNrRRFIkCsLZRaSVhWbfRzKLtcVpFIFZYyjPDCEPT3MygaARpw6xjYBGOmS4Rh-Lx1AlTxz_j1J4Zc-LIaHt6wYl4jc30jLyuE65Xy94sVNdFIwHno_JBccsRRYoot17uOevSpi2IZ4P4bmQiMZjDBEQU7t-ngsINxOt-aCuHuUF_2Tn09SqJZWXfswTikxTI69Rme2kjvjVer92oxdOyHx_KZjuNY7jjvWDV_siHVib6xcTuIc8FabjoV-Y31umPXPPW2pFwsuLU8p7mtJpktArWvoQ5Tlt8xSZSMaZmbijmGlib_2xPLExslI05MwrH883Hcm8NlWP9prkMjzk_QwKXLdSfbHEVX_GhRwJO6kdhZ4iuPUPkT_fhti87Oro_nfipSNt4F6R9vBZ6QCQb6k5p_xwqMqfv17xOdWhcwNC4xs-xELLHNejpKQM3Cgn70q6KAgupZd7xfHOpVNm-p3lT9jYUzZaKf0_AyrUMOmAOpQ5HE0NO28n8udfSSdjDIFIgDLGl-jEWR5wjwmavdkD6FN05sSJD8LdpP3iGXvrwQ1cnYNl0ZpZUoW-pc6MsXEyZ3l0zOfXlpqNZsQwAT1kG1LbxN_8k7s6gQ9Fw5L3KXRxgY8hFaD703aK73EghfAR723WqL5GuGS74rrI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/816b2002b3.mp4?token=T4qDOFdy3OcjknBFk-W6Gx4CNrRRFIkCsLZRaSVhWbfRzKLtcVpFIFZYyjPDCEPT3MygaARpw6xjYBGOmS4Rh-Lx1AlTxz_j1J4Zc-LIaHt6wYl4jc30jLyuE65Xy94sVNdFIwHno_JBccsRRYoot17uOevSpi2IZ4P4bmQiMZjDBEQU7t-ngsINxOt-aCuHuUF_2Tn09SqJZWXfswTikxTI69Rme2kjvjVer92oxdOyHx_KZjuNY7jjvWDV_siHVib6xcTuIc8FabjoV-Y31umPXPPW2pFwsuLU8p7mtJpktArWvoQ5Tlt8xSZSMaZmbijmGlib_2xPLExslI05MwrH883Hcm8NlWP9prkMjzk_QwKXLdSfbHEVX_GhRwJO6kdhZ4iuPUPkT_fhti87Oro_nfipSNt4F6R9vBZ6QCQb6k5p_xwqMqfv17xOdWhcwNC4xs-xELLHNejpKQM3Cgn70q6KAgupZd7xfHOpVNm-p3lT9jYUzZaKf0_AyrUMOmAOpQ5HE0NO28n8udfSSdjDIFIgDLGl-jEWR5wjwmavdkD6FN05sSJD8LdpP3iGXvrwQ1cnYNl0ZpZUoW-pc6MsXEyZ3l0zOfXlpqNZsQwAT1kG1LbxN_8k7s6gQ9Fw5L3KXRxgY8hFaD703aK73EghfAR723WqL5GuGS74rrI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر تعاون، کار و رفاه اجتماعی: تلاش می‌کنیم افزایش کالابرگ اقشار هدف از ۱۵ مهر آغاز شود
🔹
میزان افزایش اعتبار کالابرگ احتمالا ۵۰ درصد است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/694969" target="_blank">📅 22:55 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694968">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DU1bceIBzr93Z2beNyZCQRd8L7tBmOOtiafbGlzwWGShjbAEMZyXrFWWusKQgRp1ujhF4td1mX3beMzR_sOakyPlJI_5nyYL37e-6WDJUsGbbJ5-UwLGeF6jI_aK0t1jo7vmNR01inUPREblGhaORpdIagBcM3FDwgSpY8FEeptiVnpuDT_Ilvuco_hRM6oX15aHerYzpiBiIHJpKyhxflpau7oFt16YLe2rzTDo6lMmXhcEUG0yhqJ0MYGWZmL17E1PkYUSBNjDayrM92QCxZLA9EMV2L-tnfndrwBQ-cUYxUE03l137eauTLuPd5L_ahEKRloqGznG6hk37wBDiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
درآمد ارتباطات دیگر با هزینه‌های این صنعت همخوانی ندارد
🔹
در ۱۲ سال گذشته، هزینه‌های زندگی و تجهیزات شبکه چند صد برابر شده اما تعرفه اینترنت در مجموع فقط ۷۲ درصد بالا رفته است. این فاصله یعنی اپراتورها برای توسعه و نگهداری شبکه، هر سال با هزینه بیشتری روبه‌رو شده‌اند، بدون اینکه درآمدشان به همان اندازه رشد کند.
🔹
داوود زارعیان، معاون ارتباطات شرکت مخابرات ایران می‌گوید ادامه این وضعیت انگیزه سرمایه‌گذاری در این صنعت را کم کرده است. به گفته او، فقط تبدیل شبکه مسی به فیبر نوری در مخابرات به حدود ۵ میلیارد دلار سرمایه طی پنج سال نیاز دارد.
🔹
به اعتقاد زارعیان، شبکه برای پاسخ به مصرف روزافزون مردم، به سرمایه‌گذاری مداوم نیاز دارد. اگر منابع لازم تامین نشود، توسعه فیبر نوری و حفظ کیفیت شبکه هم سخت‌تر خواهد شد./ انتخاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/694968" target="_blank">📅 22:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694967">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e0098664c.mp4?token=efaYjQb6JPFKcXdfwlEsJ_jgeySe3gui8XtXOshzzWoCgTPKAOA0xIdezP9OhRbXp_ueVl6PpO4ONuzxcLzzQ_0xXuVLQJfjiQ2mhntuwp33AK5SJMFm41WxxH-NqXPLIkGqPCS5zAWBifHCYHiGyj5Sx7zGA6Lhl0qQ9qpycKwN1pJJAeDduchaFn7rWJLO6G5g13yqC_5RbqmsUmJtzzKd_NCjJgve7N9u_Xblkc63XHLu4rhF_Ebl3O_9lsd4NqXbwEV-ddS8FPwQucOzQaFB-gcBMvw1FEMhEF_c3kUiXG8baXkIj5UxXF-4wnz5Q64iPhnTGHvKdjCL2NBaRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e0098664c.mp4?token=efaYjQb6JPFKcXdfwlEsJ_jgeySe3gui8XtXOshzzWoCgTPKAOA0xIdezP9OhRbXp_ueVl6PpO4ONuzxcLzzQ_0xXuVLQJfjiQ2mhntuwp33AK5SJMFm41WxxH-NqXPLIkGqPCS5zAWBifHCYHiGyj5Sx7zGA6Lhl0qQ9qpycKwN1pJJAeDduchaFn7rWJLO6G5g13yqC_5RbqmsUmJtzzKd_NCjJgve7N9u_Xblkc63XHLu4rhF_Ebl3O_9lsd4NqXbwEV-ddS8FPwQucOzQaFB-gcBMvw1FEMhEF_c3kUiXG8baXkIj5UxXF-4wnz5Q64iPhnTGHvKdjCL2NBaRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجری صداوسیما وقتی اسم حسن روحانی را می‌آورد: منظورم حسن روحانی کاراته باز است، باز نیاید بالاسر ما چرا اسم حسن روحانی رو آوردی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/694967" target="_blank">📅 22:47 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694966">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d15e41163a.mp4?token=QiN_k1Jlr6M-sOQebpQu3UJwYFKfVzaTcE1ras33LNHklCd8ZF-u79pFURCuXpwwsagwQiDOqv93scNQYXpjwDbzaKG5LtVPR5clu_Q09n57LoioEjj_W1wWzecSWCC6FSvZRLqNIT8Ox5XnjPtuLKum3rNBZyDqkryxPrOb-7em4wURmCVi4by4Jo8GlNuEHIaNN4pZB67DrRg_Atbnd5ra0Ar_ljR9IyjLFMvxs7XqKxlbHu9F4wx6YasyR0dLsxyyu0584Ajxqn1DAZvDMUphOtqBa2iz7yXUOSUJfw5o7goV5B5dtPq37bBKofFJ-jrIA3IgbfT0Wa_zKEGSvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d15e41163a.mp4?token=QiN_k1Jlr6M-sOQebpQu3UJwYFKfVzaTcE1ras33LNHklCd8ZF-u79pFURCuXpwwsagwQiDOqv93scNQYXpjwDbzaKG5LtVPR5clu_Q09n57LoioEjj_W1wWzecSWCC6FSvZRLqNIT8Ox5XnjPtuLKum3rNBZyDqkryxPrOb-7em4wURmCVi4by4Jo8GlNuEHIaNN4pZB67DrRg_Atbnd5ra0Ar_ljR9IyjLFMvxs7XqKxlbHu9F4wx6YasyR0dLsxyyu0584Ajxqn1DAZvDMUphOtqBa2iz7yXUOSUJfw5o7goV5B5dtPq37bBKofFJ-jrIA3IgbfT0Wa_zKEGSvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توضیحات خلبان هواپیمایی زاگرس در خصوص نبود رادار و تاخیر پرواز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/694966" target="_blank">📅 22:43 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694965">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77717107eb.mp4?token=Kugs0uT2O-9M3WlOqyzkRFPtIzHGHmuJ-hg_IpHQthRARlEyHWn-_LEZVJckYxV_riyQ5LYUOuJJUEKomNrlr4iK3nuQCyxxEgSlnw3AV3rZQ_jXpapkpICNIBgHB-661oZRcKv7QUuG2fFkkL3by68l6Iv4rMWx792dLtbkjVXGTjwojeeU5yEWgJsamCzC0vYpAgvBbiX3WPgD_8vXA-alXGO8fR1rM6AKg1Cc_4GqtxceTyen24UYR8EjDKUruso1ZsMOXlT5iqefzkCxlIH7J_cQq4QzsVdTmUqDDJB_oEXMd6O-V0JegfiKGWVlLYjOZ2k_TmjwT0UGpXpuIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77717107eb.mp4?token=Kugs0uT2O-9M3WlOqyzkRFPtIzHGHmuJ-hg_IpHQthRARlEyHWn-_LEZVJckYxV_riyQ5LYUOuJJUEKomNrlr4iK3nuQCyxxEgSlnw3AV3rZQ_jXpapkpICNIBgHB-661oZRcKv7QUuG2fFkkL3by68l6Iv4rMWx792dLtbkjVXGTjwojeeU5yEWgJsamCzC0vYpAgvBbiX3WPgD_8vXA-alXGO8fR1rM6AKg1Cc_4GqtxceTyen24UYR8EjDKUruso1ZsMOXlT5iqefzkCxlIH7J_cQq4QzsVdTmUqDDJB_oEXMd6O-V0JegfiKGWVlLYjOZ2k_TmjwT0UGpXpuIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ماجرای لو رفتن عملیات وعدهٔ صادق ۲ و دستور شهید سلامی برای ادامهٔ عملیات
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/694965" target="_blank">📅 22:39 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694964">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
اموال غزل(ربکا) قادری، بلاگر در داخل کشور توقیف و به منظور جبران خسارت‌‌های حوادث سال گذشته مصادره شد
🔹
غزل قادری، صاحب برند ربکا قادری، ساکن کالیفرنیا است و در پلاک ۸۴ بازار دلگشای تهران، محصولات خود را با نام تجاری RG Perfume به فروش می‌رساند. علاوه بر غرفه های او، چند حساب بانکی و اموال دیگرش نیز توقیف شده است./ تابناک
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/694964" target="_blank">📅 22:38 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694963">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
وزیر تعاون، کار و رفاه اجتماعی: پیش‌بینی افزایش تورم، خود به تورم دامن می‌زند/ باید منابع را به سمت تولید هدایت کنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/694963" target="_blank">📅 22:35 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694962">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b44abae0d.mp4?token=vYN0CqBNUdQDARfINjpOoYTms-Gvm2tNrgubcIG77DxZLqJ0r-uyvmy0cGJMcMd90oiGQln0NALaCtmsS_l4iC2YJH4ndmAdTF803pa_Hgx9CTlIW4YvuIN6hOskqIA6aDKdnwsk3OT5ekYUQXC_TobFNLJHflr5AVHHym6dKFep4hGL_up-V8Go5fqbbRpfdeYtwlzwNQlOl2kqlPIRi1_yo0YGLFaJoGzdv_7K4jfCJZB45y-yD1FPPlBIf8fQ2sIn1ummf9HPXsaeXMHbOIroCbZgxrSrVcpiX50SI9bq5ZpDX0vlSCnIHt2gUJjTj6-RdhMp9J3er10_cj0t7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b44abae0d.mp4?token=vYN0CqBNUdQDARfINjpOoYTms-Gvm2tNrgubcIG77DxZLqJ0r-uyvmy0cGJMcMd90oiGQln0NALaCtmsS_l4iC2YJH4ndmAdTF803pa_Hgx9CTlIW4YvuIN6hOskqIA6aDKdnwsk3OT5ekYUQXC_TobFNLJHflr5AVHHym6dKFep4hGL_up-V8Go5fqbbRpfdeYtwlzwNQlOl2kqlPIRi1_yo0YGLFaJoGzdv_7K4jfCJZB45y-yD1FPPlBIf8fQ2sIn1ummf9HPXsaeXMHbOIroCbZgxrSrVcpiX50SI9bq5ZpDX0vlSCnIHt2gUJjTj6-RdhMp9J3er10_cj0t7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هر سردردی یک علت دارد؛ با انواع سردردها آشنا شوید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/694962" target="_blank">📅 22:32 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694961">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
وزیر تعاون، کار و رفاه اجتماعی: پیش‌بینی افزایش تورم، خود به تورم دامن می‌زند/ باید منابع را به سمت تولید هدایت کنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/694961" target="_blank">📅 22:28 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694960">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
فیلم جدید از درگیری در هواپیمای فلای دبی
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/694960" target="_blank">📅 22:25 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694959">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
موضع‌گیری جدید آمریکا و تروئیکای اروپایی علیه برنامه هسته‌ای ایران
🔹
آمریکا، انگلیس، فرانسه و آلمان با صدور بیانیه‌ای ضمن نادیده گرفتن بدعهدی‌های خود در چارچوب توافق هسته‌ای سال ۲۰۱۵، اعلام کردند متعهد به جلوگیری از تأمین هرگونه مواد یا فناوری برای ایران هستند که ممکن است در فعالیت‌های هسته‌ای مورد استفاده قرار گیرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/694959" target="_blank">📅 22:15 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694958">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sm3Ai9XQQVuEAjbo2kPwImLzjLG8mfenFV2Zqn0liTlY3dhilZDJ6EkInAZaQtauJvpDJisbpKmrazP4UZwYv05u7297NE_dTIE4GBTcRaplrHLnDbvJ_XVYvttOtJTmpsgINDBF6EdnScOO-e51CT6Ma55PyIdOvzGDQApTQzfVrpqnfQv88F-YHpyR0Z9wiGRn7ZdhqB6MT3ycVBzpJxzT9WvFJLCBHP8hXhwmh5e2PQG3ptMbu8ilVjUDLxAhJEB5PEyKPlTUEdmOV21CceLzCChi911hJWGaeLwCX-UKHJGx2Zd-4KOyE4XXHBIj-29OjwPae-rSUkMvXwYvrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر اندام بدن برای سالم موندن به چه چیزهای نیاز داره؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/akhbarefori/694958" target="_blank">📅 22:08 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694957">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
اداره سنجش آموزش و پرورش کشور: ارائه اصل دیپلم فارغ‌التحصیلان خرداد ۱۴۰۴ تا شهریور ۱۴۰۶ امکان‌پذیر نیست
🔹
بر این اساس، تمامی دستگاه‌ها و دانشگاه‌ها و مراکز آموزش عالی باید امور مربوط به استخدام، ثبت‌نام و پذیرش این افراد را با دریافت گواهینامه موقت و تأییدیه تحصیلی انجام دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/akhbarefori/694957" target="_blank">📅 22:01 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694956">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
فدراسیون فوتبال: جام حذفی این فصل برگزار نمی‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/694956" target="_blank">📅 21:59 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694955">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/274deba3fc.mp4?token=s-ICBF6FMBO9KNzgTUEgCSO3bJnZ1u-A4wr3fziyHLPQjkdXvXj0iXj6h9R4ImGyDy0_ep-5AVkf0WeaLt3rfkkyF6V0SFxl7lrqvgginHTe9EhVxxy6-XXgZlfFddRUNJ6AZ8GG8fUJ-8rflZWuhWl3PuimyyUA10L2SVMaIIVWrx5XYr8H9R3LWldt0OJDi69-Vf9adK4OLJL1--ZgZI3nLTfGibTi_ecjU5hDYeGkxtH7QsaYNvzJG0kGSykYXTpOhkYBKwG9AJ6c-dhIjRvFLiwFIE7mQKr_iTkkJnwhaNkItwGIM-8Up9mjviNFTLlYQZF8xSE8RJZj8vu6tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/274deba3fc.mp4?token=s-ICBF6FMBO9KNzgTUEgCSO3bJnZ1u-A4wr3fziyHLPQjkdXvXj0iXj6h9R4ImGyDy0_ep-5AVkf0WeaLt3rfkkyF6V0SFxl7lrqvgginHTe9EhVxxy6-XXgZlfFddRUNJ6AZ8GG8fUJ-8rflZWuhWl3PuimyyUA10L2SVMaIIVWrx5XYr8H9R3LWldt0OJDi69-Vf9adK4OLJL1--ZgZI3nLTfGibTi_ecjU5hDYeGkxtH7QsaYNvzJG0kGSykYXTpOhkYBKwG9AJ6c-dhIjRvFLiwFIE7mQKr_iTkkJnwhaNkItwGIM-8Up9mjviNFTLlYQZF8xSE8RJZj8vu6tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بعضی کافه ها گزینه «هیچی نمیخوام» هم اضافه کردن و هزینش هم ۶۰ هزارتومنه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/akhbarefori/694955" target="_blank">📅 21:58 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694954">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ePUc9PkRlHDm9PHt_iMt3WXuOiubc8l6CmaosiNTA6zMD5hsnDWIgWBva26XfK8LGt4SE0i03qDprLQx6-vB2xKIp0x7-YdkVIdQjmJ1nlwa-r418XfrZajYyMOGWKSGzdsD326K8XtShb76hQoibdR5PKoEdxqcj52mXSAbVbDPqd-ReFQZjPqCiGOqggtl4ZDlNoThyswqXaMlGyFGCqXzUfJF7RtZIP3iXFL78JMzozAlbwaNIbMNtxAJyCOJ7Ko8FfFpwL96DjWb6FF8_cHTiu4_oDHSTMZq9kvEOE5xjiW01u-fOthrL63QAZylaCvm_s03r9mdsL8EJdyEfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خیابان، دیپلماسی و میدان نباید غافلگیر شوند؛ تهدید شرطی ترامپ در مصاحبه جدیدش با تایم چه بود؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/694954" target="_blank">📅 21:56 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694953">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
روزنامه یدیعوت آحارانوت: مسئولان پرونده حادثه فلای دبی تاکنون وجود ارتباط ظاهری بین کمک خلبان این پرواز و ایران را بعید دانسته‌اند
🔹
امارات نیز با ارسال پیام‌هایی خطاب به رژیم صهیونسیتی خشم خود را نسبت به پیش داوری‌ها قبل از تکمیل تحقیقات و مطرح کردن ادعای…</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/694953" target="_blank">📅 21:54 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694948">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8464edba8.mp4?token=BBjQdYSrd5J4difD-fEohkNhcC3EPrG-B-lggCJ1d9UW6Pbez89yRbdAGVFHXwiYzkmZWiWmR2w_9cpaywJjyMERD4oIfjGzvNheYZHc_f__WrCTiEiFINuGN2KZDhJeOcux7zEGhGh7ndr_GgEe9AMAxwWO9Tf5Jq_0Y_5laLXCzAfwna6q9OCZlKWvW9it5FA-BmFLKbXjHdRTpSfXm4pG_isG9DjotJdTJKgyraQw53RzYwpuUnX6shABtHa54t2bBvSjC_8zGRv03rsRG3A0WXMP-suPKZ8k4s8ILqPsQbB9LQJcIIv6-zhXRbazHFcZahDVFJMDWVBtwqHQ7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8464edba8.mp4?token=BBjQdYSrd5J4difD-fEohkNhcC3EPrG-B-lggCJ1d9UW6Pbez89yRbdAGVFHXwiYzkmZWiWmR2w_9cpaywJjyMERD4oIfjGzvNheYZHc_f__WrCTiEiFINuGN2KZDhJeOcux7zEGhGh7ndr_GgEe9AMAxwWO9Tf5Jq_0Y_5laLXCzAfwna6q9OCZlKWvW9it5FA-BmFLKbXjHdRTpSfXm4pG_isG9DjotJdTJKgyraQw53RzYwpuUnX6shABtHa54t2bBvSjC_8zGRv03rsRG3A0WXMP-suPKZ8k4s8ILqPsQbB9LQJcIIv6-zhXRbazHFcZahDVFJMDWVBtwqHQ7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
موج اعتراضات دانش‌آموزی به دانشگاه‌های فرانسه هم رسید/ رنگ‌وبوی حمایت از فلسطین و مخالفت با صهیونیسم در تجمعات
🔹
اعتراضات سراسری جوانان در فرانسه با گسترش به دانشگاه‌ها، به تعطیلی چندین پردیس دانشگاهی و لغو فعالیت‌های آموزشی انجامیده است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/694948" target="_blank">📅 21:49 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694947">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d8d6b66d8.mp4?token=PSidgznjOO7h4GULPdDiGK2Cd5XFzipTXZzMUc0C2a7tbaNmz_ipx4bwwOH8Oh3W21aQ0YmAxZw-iziGxXIp8uQDSZr7Qoz-wZczPDwrfMFyoyngaWdTsoqDC8M6jb_WgE0llHRJe8MS3PUGz3F21XW1ruN4VxXkyNk-6P1rUzo1GIPvcxOphq0WnEcEfWhWDAKLTOHXKlbQz8WBzkefBx2fTgUoQsmO-SRhnisbz4QrPaBkNjN9WmmH1NrRRCLCF0Nu4qJWy2KlnS8S6IYSBszg08DMF5R3OGS2kffVtCUQd5O1nOOrV2LzUznLkLudRRV5MAafIy7leCSDsBOlyUgzex6EtJxISAU95SxieXiM_IJsX-sei8bcTRkU_yHYEsHCE5Sz1yLA0RFgIrWXVToKW4wA2yu7SRNWrgniZd8tVcBD55iMQ2GuZw8NSicMN8EUusH0GFFLSVuk1M3YPTwhvZZJnRk-ZHIZTMKK5PlsygxOMjkM9bIwd4PXx9Wuhq4gJ-Nb9nPK29MOqqQy-6OxBpj5X80zHY8P3JtYUJjrs73Oz-3Vb5HcNlArTySdTljFNTWMKgLTyisq6IBX6a6t7EBlnm8RiqI_ZhLE24o9f9QexN09GfKkMHus0X_eHbtNgE5xYCHQweNHvG6J7P61TSllI3VNaEPEuJoYJNE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d8d6b66d8.mp4?token=PSidgznjOO7h4GULPdDiGK2Cd5XFzipTXZzMUc0C2a7tbaNmz_ipx4bwwOH8Oh3W21aQ0YmAxZw-iziGxXIp8uQDSZr7Qoz-wZczPDwrfMFyoyngaWdTsoqDC8M6jb_WgE0llHRJe8MS3PUGz3F21XW1ruN4VxXkyNk-6P1rUzo1GIPvcxOphq0WnEcEfWhWDAKLTOHXKlbQz8WBzkefBx2fTgUoQsmO-SRhnisbz4QrPaBkNjN9WmmH1NrRRCLCF0Nu4qJWy2KlnS8S6IYSBszg08DMF5R3OGS2kffVtCUQd5O1nOOrV2LzUznLkLudRRV5MAafIy7leCSDsBOlyUgzex6EtJxISAU95SxieXiM_IJsX-sei8bcTRkU_yHYEsHCE5Sz1yLA0RFgIrWXVToKW4wA2yu7SRNWrgniZd8tVcBD55iMQ2GuZw8NSicMN8EUusH0GFFLSVuk1M3YPTwhvZZJnRk-ZHIZTMKK5PlsygxOMjkM9bIwd4PXx9Wuhq4gJ-Nb9nPK29MOqqQy-6OxBpj5X80zHY8P3JtYUJjrs73Oz-3Vb5HcNlArTySdTljFNTWMKgLTyisq6IBX6a6t7EBlnm8RiqI_ZhLE24o9f9QexN09GfKkMHus0X_eHbtNgE5xYCHQweNHvG6J7P61TSllI3VNaEPEuJoYJNE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سوخت هواپیماها در کجا پنهان شده است؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/694947" target="_blank">📅 21:46 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694946">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O6ena-O1vCcJo6TQ-0qVW6CrsPIEwDmSktRtajV3Pb_9RCYEDlCgLZQIInitsIJ9kcyyV2qFjFqewG4apgU03pCKYZh8nlwL0KCq-eEBcACkeAfVleqx2yB8LnjEdThAShyHpKmIQn6VGVINhQFz5PYzj28_DjMNWdGB720-ZqvQI4F8xV-w5QO34OIM-a0Xxm31PQ69BUfvdXWCNRNFrz2KzqD-EvFdOHWKxC2aSRYdm7PBm811JSWR4qpv3ch4DI8cM3xmL77L7ZJBcMfsbBaMCZcPL4yN-yjBVc2G4wPR_p8lyCbwFdfcPsZA58W9fA6xvgW3mWiu2b9bBRQNyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلودگی هوا؛ شبکه پایش کشور چه وضعیتی دارد؟
🔹
بر اساس داده‌های ارائه‌شده از وضعیت شبکه پایش هوای کشور، از مجموع ۴۳۷ ایستگاه پایش، تنها ۱۷۹ ایستگاه (حدود ۴۰ درصد) دارای داده معتبر و مستمر هستند.
🔹
طبق این گزارش، خسارت ناشی از آلودگی هوا در کشور سالانه حدود ۱۷.۲ میلیارد دلار برآورد شده و مرگ‌ومیر منتسب به آلودگی هوا نیز بیش از ۵۸ هزار نفر در سال اعلام شده است.
📊
آمارفکت | مرجع تخصصی آمار در ایران
@amarfact</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/694946" target="_blank">📅 21:44 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694945">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
وزیر امور خارجه عراق: بغداد آماده میانجیگری میان آمریکا و ایران است
🔹
حدود دو یا سه هفته است که توانسته‌ایم نفت خود را صادر کنیم و از این بابت خوشحالیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/694945" target="_blank">📅 21:42 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694944">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
نیرو زمینی سپاه: با جعبه مهمات‌های آمریکایی برای سربازاشون تابوت ساختیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/694944" target="_blank">📅 21:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694943">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gSj206bR0B5jpzUlIH7-0jrD1TSOH1vBw6HXe7vWwfR9W74IP5LRLmilJ5LuwJYxwBDTuJh9vkU8fVn-JB6Mevne31ohjrjIoSagEUKlz0wxNkYOnjGe9b771JcJb3PVUd3n0T2TSsxbdTpnRPWYs6tV111csZKp6nLE5LGj4bmWMX65CCSIiKbR3mC6DXZvCXbcMy4ejYXzIYj_SkyyXl7D3ITKxB89R6LASctPa3mso1HkxNTsKGQNugAVA_gBiYPkP5NbZy1O5ocZPrrChJatLHuQY-j38OjE1BCRKDaH-dIdYhB5kCAs74mlU4bZbCTEtd_Wgi3KHaoAQqNVhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آیفون ۱۸ پیش از واردات رسمی، در بازار ایران دیده شد
🔹
برخی مدل‌های آیفون ۱۸ در بازار و کانال‌های فروش مجازی عرضه شده‌اند؛ این در حالی است که ثبت سفارش تجاری گوشی فعلاً به مدل‌های زیر ۴۰۰ یورو محدود است.
🔹
هم‌زمان، برخی فروشگاه‌ها این گوشی را در قالب جوایز و طرح‌های تبلیغاتی معرفی کرده‌اند./ تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/694943" target="_blank">📅 21:35 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694942">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
رویترز: پاکستان بین ۳۰ تا ۴۰ هزار نیروی نظامی در عربستان مستقر کرده است
🔹
مأموریت این نیروها دفاع از مرزهای عربستان و کمک به مقابله با حملات موشکی و پهپادی اعلام شده و بخشی از آنها پیش از تشدید اخیر درگیری‌ها وارد عربستان شده‌اند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/694942" target="_blank">📅 21:32 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694941">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27f4b1fd92.mp4?token=bBeNM8JAUqsHg5_PzPBKR1SQzvDE4r-RAavtzxwb_VUvKDqXdMNWRfLLBpG7Tj0citmq-DU093kSNpBUMPAqQMBiUnVUMFHXj0AA7yZVdT3xlXkztVasbquJHJ7bWSnV8TNOI9DNR4TVOfeAxGW-pK5maGZ2JlphwF5CCIHkcSFYP73LEaOV-GIkUUXiBiwidT0EHFfK_7MOo4y4c-SydJaeAtJKC1sr1lCeUXuYEqCnOV2OL6_iDcbEdf_TddKv0JdPMul5Tb8ndTyMTGdBBRhT2f1CdgByphGRUf6dsBw6e8QFAii_num0mU1qvwLazps23XWM6NJu2-LlMhDNAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27f4b1fd92.mp4?token=bBeNM8JAUqsHg5_PzPBKR1SQzvDE4r-RAavtzxwb_VUvKDqXdMNWRfLLBpG7Tj0citmq-DU093kSNpBUMPAqQMBiUnVUMFHXj0AA7yZVdT3xlXkztVasbquJHJ7bWSnV8TNOI9DNR4TVOfeAxGW-pK5maGZ2JlphwF5CCIHkcSFYP73LEaOV-GIkUUXiBiwidT0EHFfK_7MOo4y4c-SydJaeAtJKC1sr1lCeUXuYEqCnOV2OL6_iDcbEdf_TddKv0JdPMul5Tb8ndTyMTGdBBRhT2f1CdgByphGRUf6dsBw6e8QFAii_num0mU1qvwLazps23XWM6NJu2-LlMhDNAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حجت‌الاسلام راجی: فکر نکنید چون به آتش‌بس و... انتقاد داریم، باید احساس بکنید که شکست خورده‌ایم/ دعوا بر سر میزان ابرقدرتی جمهوری اسلامی است، ایران ابر قدرت عالم شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/694941" target="_blank">📅 21:28 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694940">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/199d391437.mp4?token=Y-pAucPzzDLXmnyV-TwsN6wUDyQfM-dtBxmLqd4FzLbjj99IJqdqn6eR5YV8l8v-VjNbnyivCE79GsVKm9z94AjaCDHjfLCwOG3mJtK006mhCTlOfgoU0bsMquw5WxElyRX7mPct9t3lk6f7ezs18V3hOqwS7XbSy-tahTmVSxQD1Q1TEZuhWN5rr4mp6maTUNkJhS2BstIrGLOU7B66VAsmSHBdoOfuhvnTGrzyrlKDN3rMeOgu3Yxjm1ruCNfYJHq86cFOfyjEqIgqboQRYrS-MIATjXyqpqEz6YS2lVCMSqalFpDMb419kUasZuynr7f3pcsrVa7uJAMqq1E1Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/199d391437.mp4?token=Y-pAucPzzDLXmnyV-TwsN6wUDyQfM-dtBxmLqd4FzLbjj99IJqdqn6eR5YV8l8v-VjNbnyivCE79GsVKm9z94AjaCDHjfLCwOG3mJtK006mhCTlOfgoU0bsMquw5WxElyRX7mPct9t3lk6f7ezs18V3hOqwS7XbSy-tahTmVSxQD1Q1TEZuhWN5rr4mp6maTUNkJhS2BstIrGLOU7B66VAsmSHBdoOfuhvnTGrzyrlKDN3rMeOgu3Yxjm1ruCNfYJHq86cFOfyjEqIgqboQRYrS-MIATjXyqpqEz6YS2lVCMSqalFpDMb419kUasZuynr7f3pcsrVa7uJAMqq1E1Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۳ دهه پیری پوست؛ تغییراتی فراتر از چین‌وچروک
🔹
با گذشت ۳۰ سال، کاهش کلاژن و خاصیت ارتجاعی پوست، تغییر چربی صورت و بازسازی استخوان‌ها می‌تواند فرم کلی چهره را به‌طور محسوسی تغییر دهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/694940" target="_blank">📅 21:23 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694939">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KJStJvAmHAQsPB3VJGnHyQPyob9LTz5DHyYv5YPBS5vBoz77UBTc00TrugEVKBSIrum4il7uicrYZd4zxyoN3Gk166U8suza67ScjuRZgPzZ7fhfN_GLCV6kxSVQoVB1SyS9I3jAV0WLQJoB5tCeT98O5s75Mj3qjekPv3Cxg-uoVkENq-oj_P3y8lj01SkwIjU_dPwAB8mrWHr-kqhJxaVyOXfnpjAlDElAXsyYgQ1Hjetxs43svmhcyZXBVmFcPtaI_RuRkDjTlP_5SUQ7OiaSsXiLsl5P0HTYyBtJEMcv-H5nrhdF26R-pfZmXmPN1241O77V8jWNLv0_aBXC6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فیلم جدید از درگیری در هواپیمای فلای دبی
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/694939" target="_blank">📅 21:20 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694938">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
رئیس انجمن صنفی تولیدکنندگان شیرآلات: اگر محاصره دو ماه دیگر ادامه پیدا کند کل کارخانه‌های شیرآلات تعطیل خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/694938" target="_blank">📅 21:18 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694937">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
پوتین هشدار داد که قدرت‌های هسته‌ای یک قدم تا جنگ مستقیم فاصله دارند
🔹
دمیتری سوسلوف، معاون مدیر تحقیقات شورای سیاست خارجی و دفاعی روسیه، می‌گوید پیام اصلی سخنرانی ولادیمیر پوتین، رئیس جمهور روسیه، در باشگاه گفتگوی والدای این است که تشدید تنش با ناتو می‌تواند سریع‌تر از آنچه انتظار می‌رود به «نقطه بی‌بازگشت» با پیامدهای «آخرالزمانی» برسد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/akhbarefori/694937" target="_blank">📅 21:15 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694936">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bb612c7d3.mp4?token=aEYWsb5dWi7VErkHMDPRgx5nSipzWkuousw7v64W_lAY34fYxtPJOj7dXHcKcHJy_iXEpIcB4xxxh-mQ_q8Aa5UcDxWZPFWjiacwC5rrW4nyz36ZKcggz7FahQXGMostQGehnuciFNzbBOye0WygU2LktPpSh07fbhTKtYMwvQJECD3DbLHKDflpR8aQnyCf_rNgBs1rFQJbECwiXLti1ywFuct_gkSyIKyF6_KgW4Qeq9qlLTCvbFUkH4oYedwmsrNzENM_zN7wibLwh-uj9YQhAPkx6a0SKYVz71Si_21i48xbdD-_FxG9d6i_VrtP2mxjucpl1cjBWT-AK2vcBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bb612c7d3.mp4?token=aEYWsb5dWi7VErkHMDPRgx5nSipzWkuousw7v64W_lAY34fYxtPJOj7dXHcKcHJy_iXEpIcB4xxxh-mQ_q8Aa5UcDxWZPFWjiacwC5rrW4nyz36ZKcggz7FahQXGMostQGehnuciFNzbBOye0WygU2LktPpSh07fbhTKtYMwvQJECD3DbLHKDflpR8aQnyCf_rNgBs1rFQJbECwiXLti1ywFuct_gkSyIKyF6_KgW4Qeq9qlLTCvbFUkH4oYedwmsrNzENM_zN7wibLwh-uj9YQhAPkx6a0SKYVz71Si_21i48xbdD-_FxG9d6i_VrtP2mxjucpl1cjBWT-AK2vcBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یکی از تماشایی‌ترین خطوط راه‌آهن ایران، دورود–اندیمشک؛ سفری از وسط تاریخ و طبیعت زاگرس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/akhbarefori/694936" target="_blank">📅 21:03 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694935">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/soV2cTHPnkcTbUQcwKvNzUchJJ-xxfcgzoaa1eHB36KpdUt1iBbBvvVEJ1ULjO6I309h0sSfMq0CgQ2WpCLoX2M0gvqy-atgHBKNE-wNwqbF_978wXhUwqD8FqCdZIJ-DwIyzm3An4n3XBykU1iJfcM3pFLe3go7hT_HMLaCIWuVTgxF_YeLhKtYvnSfRhvlXSUnthaJBqYQ_uJitjIjzyRE0d5Q4j9zCSEMb7bejFz3FIoGoWnPxnn1maZR3aReBRkIkFegXkm1GL76L-6BmKAhn9KDfxQuhRk4jvetY3xxojrJlyF2kHnYTDoXPBrZImp3shIhId1brS_pr_4inQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دیپلماسی در بن‌بست | پاسخ سخت‌تر ایران؛ تهران اهدافی خارج از منطقه را در برنامه دارد
🔹
رویترز در گزارشی مدعی شده است ایران همزمان با ادامه تلاش‌های دیپلماتیک برای جلوگیری از تشدید درگیری با آمریکا، در حال آماده‌سازی برای واکنشی گسترده‌تر و شدیدتر در صورت آغاز دوباره حملات نظامی واشنگتن است؛ واکنشی که به گفته این رسانه ممکن است دامنه‌ای فراتر از اهداف و منافع آمریکا در خاورمیانه داشته باشد.
در خبرفوری بخوانید و درباره پاسخ ایران به حملات احتمالی نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3249468</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/akhbarefori/694935" target="_blank">📅 21:00 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694934">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BdXgod8wVrDDy01fZJVHE8TEqxtV6ELSKqw0OTT1iS4oii3HcJlgi7vvdwzyiBY-lDZ2IL1Zi-K0T-5FJoCxg_NPnz4ZyWZM2eyCNj-Rvb01UZgpWwwYNMhrHZwoQpGCsj3irFLwmL7Vtt6-P5tlsmH9W8mX-J6BpaeJd1gp63OAlBRp5IRq8Z56BDHQWsLHD7O0KV3xFz350TjhlwiS09rY5u_yTBvOM1tGalGY_otaVlibYydt5lDL69zu_XrRxDyFLhumkEwdv4DKO3_at8jhmWjK5SA_yZP7tj6QxJ2kTGyb_cFiFfTdJom75ApEeTvpn6oqTml4sW-pvUxN3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
افزایش مجدد قیمت نفت برنت/ هر بشکه ۱۰۲ دلار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/akhbarefori/694934" target="_blank">📅 20:55 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694930">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17c8a54664.mp4?token=USMSDKmmRF7DRx6xAYH5DHV8RDS9xmOu-kObwfI2ZkIDlNiuCsR_0stdKeVeR1jKKyYkM-pnEUyLyV1JoQNXxcU0eodZ9vsGxoA2owlKZOtjjh--v5zUPo6WoIBa_DQ642MUZj3_T2qhQgKHj3I7PCrjY-DLhp5anD3uXtewSMeiv3yVFgDUX9yWYayc5MFVe8ExUVkWIlMjArLj2M5Ww_AjZdTjMCVyAZBBOugehnwRuszcZgNGfXO6WFU5KjzdADd3qynym3qpbLTfDb3vpcs5GxQT02Ze3kG2R4KgeKIzQXwRIAYYKNWMQRiCRUjtHR7ySy8QvjOBr_goxrlF2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17c8a54664.mp4?token=USMSDKmmRF7DRx6xAYH5DHV8RDS9xmOu-kObwfI2ZkIDlNiuCsR_0stdKeVeR1jKKyYkM-pnEUyLyV1JoQNXxcU0eodZ9vsGxoA2owlKZOtjjh--v5zUPo6WoIBa_DQ642MUZj3_T2qhQgKHj3I7PCrjY-DLhp5anD3uXtewSMeiv3yVFgDUX9yWYayc5MFVe8ExUVkWIlMjArLj2M5Ww_AjZdTjMCVyAZBBOugehnwRuszcZgNGfXO6WFU5KjzdADd3qynym3qpbLTfDb3vpcs5GxQT02Ze3kG2R4KgeKIzQXwRIAYYKNWMQRiCRUjtHR7ySy8QvjOBr_goxrlF2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری دیگر از آتش‌سوزی در ریاض؛ دود از یک نقطه در پایتخت عربستان دیده می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/694930" target="_blank">📅 20:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694929">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00c559c74d.mp4?token=GQqeihs3eDzueaqdC93WT8qTQ3X3d08TqiWCN1ThuWfC7Sd_kt1CvyBXbGqpqXikqrDswlvJJM5jh04f-sFJtpv368aCjOwrDTBin8i69kxMmUbwACrxKIHa5SgcDvMaAzzguFg1NcyLvJjDx9whNfzJawI4AtGBhdYXCD4Z_rfpnKrZ4XVLHX1PJeAJwdECymYYKtGLO_viwRHq0-BVKDkH7LFCNYmDKx8MT2kjmo1WsBs38di8KhU4e4BfWIkRGWK-0XQ3PbI1HeAiWd66TkqPj_CG6eGcUJ6TTCQKxlfisTy1MK0xcMQJUknlWRnqW335BGWjNDEHPqIyx2DMZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00c559c74d.mp4?token=GQqeihs3eDzueaqdC93WT8qTQ3X3d08TqiWCN1ThuWfC7Sd_kt1CvyBXbGqpqXikqrDswlvJJM5jh04f-sFJtpv368aCjOwrDTBin8i69kxMmUbwACrxKIHa5SgcDvMaAzzguFg1NcyLvJjDx9whNfzJawI4AtGBhdYXCD4Z_rfpnKrZ4XVLHX1PJeAJwdECymYYKtGLO_viwRHq0-BVKDkH7LFCNYmDKx8MT2kjmo1WsBs38di8KhU4e4BfWIkRGWK-0XQ3PbI1HeAiWd66TkqPj_CG6eGcUJ6TTCQKxlfisTy1MK0xcMQJUknlWRnqW335BGWjNDEHPqIyx2DMZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در امارات بنزین گران شده و مردم برای یک باک ارزان‌تر صف کشیدن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/akhbarefori/694929" target="_blank">📅 20:45 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694928">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a62d4bc71.mp4?token=speAJ_Nim-fjU4BDFeglUScwGsrcFO-ZZyEy20tB_pAiTt1enIg6gRiTey41xfMj7u0A9WQkzJFEyUG2CtE9r_bCQsCELYWeNYSCn5fk-UxhzlEv_H4Hx94aB7gbQrcRgsWdgh3sQDfPWxpH50FkAF9f5Bbm8EfyuJUaObo5JWErVCxql49zNpfsHEWunkFia-kWfA5mDm_aZuDa4P3EFultms5JWKIy2UxGIstPSIxFcQVc3kQb6cIFtGIvdqzS9Tkfua-idgdiuo40jFg-3h3bezQP7gl5co9DoBNYyYPq16Y304cOA-SbG55Mb_nJmeDw3Ft0cFOzTMjRJNFRhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a62d4bc71.mp4?token=speAJ_Nim-fjU4BDFeglUScwGsrcFO-ZZyEy20tB_pAiTt1enIg6gRiTey41xfMj7u0A9WQkzJFEyUG2CtE9r_bCQsCELYWeNYSCn5fk-UxhzlEv_H4Hx94aB7gbQrcRgsWdgh3sQDfPWxpH50FkAF9f5Bbm8EfyuJUaObo5JWErVCxql49zNpfsHEWunkFia-kWfA5mDm_aZuDa4P3EFultms5JWKIy2UxGIstPSIxFcQVc3kQb6cIFtGIvdqzS9Tkfua-idgdiuo40jFg-3h3bezQP7gl5co9DoBNYyYPq16Y304cOA-SbG55Mb_nJmeDw3Ft0cFOzTMjRJNFRhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مادر همسرِ شهید رهبر انقلاب: آیت‌الله سید مجتبی خامنه‌ای با امور اجتماعی از نزدیک آشنا هستند و فقاهت ایشان را همه قبول دارند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/694928" target="_blank">📅 20:44 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694927">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pweegpanxgK4q9mAv9PFtVijV9VCN55VToxzh1F0iua2wUwJwLTtnqq6OGNBxcsIfDOI7yJNRuQNNUuowq6QcqMlWJH9nuF4jebT-26AZBtppjFDHRsRuIZJ8MqoO_1Cw_DO3D9LA37egvtOP1xg8H6nhZfD-AfR-Lnac5A-Eg_DBQcUKcEmSlU8rCpWTBg2nZhLS1x5l33qSA38XiDSAPspmPlT9yEyUCpcB_bYTmDakL5DeIeJvs1AleBFI0kjdTl3TmW6qVOxw7K3QkhLWTyn7SAwqJrkHyg7Gcu4aPV1u2mplUPUbJYcIlcu_99WBC9FshiJRCRW5FdiszIBMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رویترز: عربستان در حال آماده‌سازی برای آغاز حمله‌ای جدید علیه حوثی‌ها در یمن طی هفته‌های آینده است؛ هدف این حمله بازپس‌گیری کنترل تنگه باب‌المندب و تأمین امنیت کشتیرانی در دریای سرخ است که با حمایت اطلاعاتی آمریکا همراه خواهد بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/akhbarefori/694927" target="_blank">📅 20:42 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694926">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
گروه هفت خواستار برقراری فوری آزادی کشتیرانی در تنگه هرمز شد
🔹
کشورهای گروه هفت طی بیانیه‌ای خواستار بازگشت فوری و کامل آزادی کشتیرانی در تنگه هرمز شده و اعلام کردند که تلاش‌ها برای تضمین تردد کشتی‌ها را افزایش خواهند داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/akhbarefori/694926" target="_blank">📅 20:38 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694924">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/297e84ff75.mp4?token=rGBcmoiASj7qgs6nonivNj38DjPSFquT9y-TzKHDoLAnYyooRJHZkeNNnZVz3AIM0W4YFBFH0m3IwT_rzxhbJHPL_TiZfae-RsyFCGgvBcb4XGsQHa0kgFEFDQDjcibxu_QrOYW3_520DJ4v9riXySrY6yDS98zbH9V-Qq9dWWLBlhRjkYvtssGo7xbw9DRROQD6Cr_RpoQ_HW7dDoQnVwpiQHOhdaXHYite49mVGTz-OOVXshqS1ZQ99bTWOzfyInESC_tuh-yDSeRcGnBUi30gLL-dTmuqWmeKnMOyMBvvPo5-eBuPK4v54G9KE3txB74vauvl7JR7PAOjPM_3RFi33qid9NjtX6P8qLjVQVhfn5d5vyHRix0pRWTe2_mEhbnW6LqmxqCgodC0oQU9Ps5oW7y-PixC5at7df5Ps1l5fFdAZQgaIpeSXfc7behyLtQe36cmDUBrW75wvtiyr-pnI997eTBgymKo5ACPHCpyK0t2wsAkUEG06Zk8AncFId6gVLLjFJDtr1M-6DusEAnNklaqaErgEY76RMihEGaOB-qpqzaL18rlCaUWuwYkkoEheRZb-H2plqNJadCYDWM58zWFsbhX28rISx4H3NXR61L_lUx4eSubdRpLiX4Fq8-lV2tOUhDQuIqPL-H-DmxxK4df1TR2baZQzjdYpAc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/297e84ff75.mp4?token=rGBcmoiASj7qgs6nonivNj38DjPSFquT9y-TzKHDoLAnYyooRJHZkeNNnZVz3AIM0W4YFBFH0m3IwT_rzxhbJHPL_TiZfae-RsyFCGgvBcb4XGsQHa0kgFEFDQDjcibxu_QrOYW3_520DJ4v9riXySrY6yDS98zbH9V-Qq9dWWLBlhRjkYvtssGo7xbw9DRROQD6Cr_RpoQ_HW7dDoQnVwpiQHOhdaXHYite49mVGTz-OOVXshqS1ZQ99bTWOzfyInESC_tuh-yDSeRcGnBUi30gLL-dTmuqWmeKnMOyMBvvPo5-eBuPK4v54G9KE3txB74vauvl7JR7PAOjPM_3RFi33qid9NjtX6P8qLjVQVhfn5d5vyHRix0pRWTe2_mEhbnW6LqmxqCgodC0oQU9Ps5oW7y-PixC5at7df5Ps1l5fFdAZQgaIpeSXfc7behyLtQe36cmDUBrW75wvtiyr-pnI997eTBgymKo5ACPHCpyK0t2wsAkUEG06Zk8AncFId6gVLLjFJDtr1M-6DusEAnNklaqaErgEY76RMihEGaOB-qpqzaL18rlCaUWuwYkkoEheRZb-H2plqNJadCYDWM58zWFsbhX28rISx4H3NXR61L_lUx4eSubdRpLiX4Fq8-lV2tOUhDQuIqPL-H-DmxxK4df1TR2baZQzjdYpAc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اینجا هلند یا سوئیس نیست؛ تهران خودمونه
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/akhbarefori/694924" target="_blank">📅 20:30 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694923">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
۹۷۴۵ کلاهک هسته‌ای موجودی زرادخانه‌های جهان
🔹
برآورد ۲۰۲۶ فدراسیون دانشمندان آمریکا نشان می‌دهد حدود ۹۷۴۵ کلاهک هسته‌ای در ذخایر نظامی جهان وجود دارد؛ روسیه ۴۴۰۰ و آمریکا ۳۷۰۰ کلاهک در اختیار دارند. چین نیز حدود ۶۲۰ کلاهک دارد و باقی بین کشور‌های هند،پاکستان،کره شمالی و رژیم صهیونسیتی تقسیم می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/694923" target="_blank">📅 20:28 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694922">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Axvb0JNaM1hbZWt4pk5X4D73r8FSL0eEI404qBrydjExr1LEE3UEy0_mdTyPFnt6v0zBsbbybumqPyq2r8GL8KX9OwqCV0KJshgBBjODkg0qSuByxmI97nHiEg4IaIPmdRRb9AEZuofTdhY-WO_OljXHkn9C0axYWydUP9kz8dMfti2LpGsiK1uP_u-KmlfOCuHdTJNx-PlHC4-itGT0GmWw4WrQY5Ox6pG2VqnHrJQM0uDSpwuzh02ngKfzjOn3HkTckPuYn1lqAYasQea5WGzQZdOo98nP1jDzk3fenoI6GCk6Omm8BY9ZeyvwfnfbQIIHKSHVsVldtZcBoOIQvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روستای عجیب لهستان با یک خیابان
🇵🇱
🔹
روستای Sułoszowa با حدود ۶ هزار نفر جمعیت، به‌خاطر قرار گرفتن خانه‌ها در امتداد یک خیابان طولانی مشهور است؛ تاکسی‌هایش واقعاً «خطی» هستند!
😄
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/akhbarefori/694922" target="_blank">📅 20:17 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694921">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">21-2 Ane Manaee (1404-02-08)Shahre Moghadas Ghom</div>
  <div class="tg-doc-extra">@Aminikhaah</div>
</div>
<a href="https://t.me/akhbarefori/694921" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
تفسیر سوره محمد| جلسه بیست‌ویکم؛ بخش دوم
حجت‌الاسلام امینی‌خواه:
🔹
مفهوم عمیق "منا" در روایت الحقیقه جناب کمیل بن زیاد [00:00]
🔹
جدا شدن از غیر اهل‌بیت و اتصال حقیقی به ولایت، از مراحل سلوک معنوی و فلسفه اربعین است. [04:46]
🔹
شهر قم، "آشیانه اهل بیت" و جایگاه پرورش‌دهنده یاران امام زمان ارواحنافداه [11:58]
🔹
رابطه عرفانی و روحانی آیت‌الله بهجت با حرم حضرت معصومه سلام الله علیها، به‌مثابه چشمه حیات معنوی [25:09]
🔹
نقش زیارت در تربیت و سلوک معنوی و نمونه‌هایی عینی از رابطه بزرگان با حرم اولیای الهی [31:49]
#تفسیر_سوره_محمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/694921" target="_blank">📅 20:13 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694916">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vxiwo57feak6xEySoh49bUBd7lYgXx0-GNSJBtP_547aRJ0SeJx4qWYw4I0hPOWUTFjLPNi4QUSWAdAK04BkOXIjX_JbFGKGEa7zxzUQZLvFuNcu_Emcpzs9QrYYAS9Tf-GRqe0AA5Avez00C84gqqr0fIZ4F50U5mHr8gow56dJYC-vF3mX3t-UxgeB12ZzUqYLJNQQcFjqY6BDtFirg6UxE5T_hwtFG8FNZHkzCBpWQKwkGpTKrFHBh89REuJddByhDQTD0H14_K5Gn9T1ziyQFAUEfc1fKl5gE8GFlvs83YmVEI6AbXxPfUV6LXILXbbt4U6ys_gnmH5c-e5BJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QVVajE0lZG5r3PfUFLeF21A8PF_lRWZx6x3VVqQDNAtQ7xgXtG0ZiH5L4aQSVPhL7D5add501Xqi973lWU3qD9clZxR43_5qlGQ98aETU2f4mRNWgy5qcGAA4xILgo-zCRGTRawZIYETSnnn3jJooaAnKe-zxWA9MvUGNIRFTQU0C5u3x7Ww4Zy7T_lvyJTL1vx_sKhWVJHL_g150mj7gSI-yVI3JUzBe2f_s0nkEXmCRQqduZzYvl64uiDoqfHOYuBNQMuS8I2T-sI1ThHNKBs_vJh5RCOlrPonjPtBZ4YqIxyLToR2qhUCDsQg3djwVUgxynPKcsxg54yDou-s_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VznLtBH6HLXhbVwx4-yQJJQaUlpvyaBLYg0yHMNkAv0IMnweJ3k-W-eh74Qgl6o0Hb0mJcgnaxMpzJ-DP30tRRZmqf8_NbI_nz-ClinBR8JC8O63YpWhHPq4cCYaAjx9bWPPsSf9J1PoTcHps0nprrtSP-CstGWfhxBWSeAZRq5yjlm1jg6-Ijl0F_QEPpyzkbEe9VY7fK0R14r08K6oWyMyltYV15qlgkeKwhIAdrPMRDqqe4dSXkwHe_7hs6PAzba6ab5yj_qtT1214bxPc8HpQoQFk6yQwg3kQAV_fP0Bzs5o5vp4TtJtg9GVyCnF866qleojz_DbPfxy2XRzKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/srirIuiiWA7DjV86cM8P6NCGoOuEXlRwS9Y0W5X4TMOjqtGFuZpDGGZlvOBO-tOt5PFmmMVk34IJ9dwS5pdbgp-xwhQkN5h0J__u8zVkygsQNYLPwibS4lW34KTEN1ybtIGbni0aK4M5ff-njHrTFtdXVdyr7R_z5IkN3Qj2auoQS-_dbSs0br_Khz3kWHi0XNxW5BKWPhK0HKUUL3UvPxGmmxwlJFTlTW968KlZfBlLMMbD1zi1nsgYnNDUxGAKceDEDWiBPrHzWP7ERmqXyrEN1z3Tao1xGVj5UTyHS01C9lEYdWNhlWNpfJjphnN9v2Ro88dYfReSbEdclwEHHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G9zZUPo6xg55FyYPoXyqlQ53BzNN9Mu6cFJCT8hNlZ3F-QlOl6yp-uRFT3k3GwM3fePtccOJg2uN1W4VrYhhdiVBMxe5cKVjOVwzJjPUNtnWYuypc7EqKScNtf8dFjujRqFrYuBXgisXdNLFXGNo8mKXtdFmVm3B9yodBWwYhjO98T6_SCzvKqs-1EB9hnCJrArzjj6S4dTN54TnNWKJJpn-dWFZuYE8FgLZupekrRMPcwmXUveaGvhSfje8tB7nEob70GRr6k87Ebjz9as42sgzXCGI_FTooDD7f2wrIRxI38AkRl2GEF4USqjTVoanMSvG549b-2zy9rw7x0pUOw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ماهواره‌ها؛ میلیاردها چشم در مدار زمین
🔹
امروز حدود ۲۹ هزار شیء فضایی ثبت‌شده در مدار زمین وجود دارد که نزدیک به ۱۸ هزار ماهواره فعال هستند. از این میان، ماهواره‌ها بیشتر برای ارتباطات و اینترنت (حدود ۷۵٪) استفاده می‌شوند و پس از آن مشاهده و رصد زمین (حدود ۱۵٪) مهم‌ترین کاربرد را دارد.
🔹
آمریکا با بیش از ۱۱ هزار ماهواره در صدر کشورهای دارای ماهواره قرار دارد؛ و کشورهای چین، بریتانیا و روسیه در رتبه‌های بعدی هستند. ایران نیز با حدود ۲۵ ماهواره ثبت‌شده در این فهرست حضور دارد.
🔹
در کنار فرصت‌های جدید، مدیریت زباله‌های فضایی، شلوغی مدارها و خطر برخورد ماهواره‌ها به یکی از چالش‌های مهم آینده صنعت فضایی تبدیل شده است.
📊
آمارفکت | مرجع تخصصی آمار در ایران
@amarfact</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/694916" target="_blank">📅 20:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694914">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j_ootnq7dda6cREL0G_PvcvYOYm5CtqWlcksR8QKWxCE2s9804cOSs3PkvvgyjOnOBNLtLrKUzfDZusgpe94ugf34X9QLSbg9hWZMk3j3i0gNaygVgZZd4X_uR3BNc-9Mm0QyXrbNTcqeAAXvFJ3folqO0Oc75BKPZb6O4A5aCyEoxol19uc4xpDeE6uJKD36h2VV5nYR64oTXHb_thP0AEEHw-Ewl86mQtHdybCWczE-x6fam2jZ5zi40j_thfI5IJDarMbnUgLNvQGm85wP20bM8pGedP-p3lCNIwmOMby_WDJfMnLd8AVWINbc0bJ2MI60ElIqHReEmdhSXmpzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت بیمه تجارت‌نو از متقاضیان واجد شرایط در سراسر کشور، برای اعطای نمایندگی بیمه دعوت به همکاری می‌کند.
🔹
بدون نیاز به سرمایه اولیه
🔹
آموزش و پشتیبانی مستمر
🔹
امکان فعالیت تمام‌وقت یا پاره‌وقت
🔹
برخورداری از بیمه تکمیلی برای نماینده و خانواده
🔹
تسهیلات و طرح‌های حمایتی ویژه نمایندگان
🔹
امکان رشد و توسعه فعالیت و راه‌اندازی دفتر نمایندگی
این فرصت می‌تواند گزینه‌ای مناسب برای افراد جویای فعالیت حرفه‌ای، شاغلین، دانشجویان و علاقه‌مندان به صنعت بیمه باشد.
📌
ثبت نام مستقیم درخواست نمایندگی
👇
:
🌐
tjrt.ir/a/life-agent
ظرفیت پذیرش در برخی شهرها محدود است.</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/694914" target="_blank">📅 20:05 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694913">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
اهالی بخش «التعزیه» در استان تعز علیه مزدوران عربستانی بسیج عمومی تشکیل دادند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/694913" target="_blank">📅 20:01 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694912">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4eabbbb33c.mp4?token=AJLJeQ69skiKihVtZkq6d-YvsGoTS7arMQFJ8ftfrhXhcvc3uelfRntp72WFCAxwA11eM54yWPAHP-_5kIGbESgfQg7RqR4T7DNJUptVwX78xwWZ_IMIkIUAixccDDDJfVQpInJJFQUrJZFGOTcbTnCcDQHyYjMPww9gEXW5_qBO-WBJxHz1MX4p_LYg-FJxw-MTo4fGfMWk_BinLjz3irrCfF2p2ZCrv4il7i6NKR61J2uPnSQwogzFyR3cqCVaLDszkrYSgJuXr36zqz44vSEdiCHTUwZw9LzLEMbIta2r-Nl4wMjkPlhkJsAbU39R8kNbDiYWjFhsKcw2vZX0rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4eabbbb33c.mp4?token=AJLJeQ69skiKihVtZkq6d-YvsGoTS7arMQFJ8ftfrhXhcvc3uelfRntp72WFCAxwA11eM54yWPAHP-_5kIGbESgfQg7RqR4T7DNJUptVwX78xwWZ_IMIkIUAixccDDDJfVQpInJJFQUrJZFGOTcbTnCcDQHyYjMPww9gEXW5_qBO-WBJxHz1MX4p_LYg-FJxw-MTo4fGfMWk_BinLjz3irrCfF2p2ZCrv4il7i6NKR61J2uPnSQwogzFyR3cqCVaLDszkrYSgJuXr36zqz44vSEdiCHTUwZw9LzLEMbIta2r-Nl4wMjkPlhkJsAbU39R8kNbDiYWjFhsKcw2vZX0rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت مادر همسرِ شهیدِ رهبر انقلاب از سفر به کربلا
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/694912" target="_blank">📅 20:01 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694911">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e76399d2d9.mp4?token=ffC6Od0KzaJam4_4DwUI_EBYrMlYAhn088GRl4r4MQFf1Pn68oMw0kvsXdOpXAj-5K-_yY3GNcdBPZj8aDGV-RysSf0DpXerqc3_7c1X8j4Tz-mrc8_vQ_IOHs4_3PikAo3Bje2GP_VVSC0paHXIzfy3TZMesz5PY0hi-m0rkBSwf2Ig69BdYhH78TE5Ogh_wveKzu9_qZDEVrlvvUX2rrDp1lpkeqE4sseBvMsFjkwJKghTHZVOCoNg2aQTacW6cy1pNoBawEFvez8d3yYKL_2cYbcecnTHWvzoOdQoosGYgZ91UwwyrSJBs39U7M_yWvEZcpqZNEvEehyHcxtP5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e76399d2d9.mp4?token=ffC6Od0KzaJam4_4DwUI_EBYrMlYAhn088GRl4r4MQFf1Pn68oMw0kvsXdOpXAj-5K-_yY3GNcdBPZj8aDGV-RysSf0DpXerqc3_7c1X8j4Tz-mrc8_vQ_IOHs4_3PikAo3Bje2GP_VVSC0paHXIzfy3TZMesz5PY0hi-m0rkBSwf2Ig69BdYhH78TE5Ogh_wveKzu9_qZDEVrlvvUX2rrDp1lpkeqE4sseBvMsFjkwJKghTHZVOCoNg2aQTacW6cy1pNoBawEFvez8d3yYKL_2cYbcecnTHWvzoOdQoosGYgZ91UwwyrSJBs39U7M_yWvEZcpqZNEvEehyHcxtP5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت مادر همسرِ شهیدِ رهبر انقلاب از سفر به کربلا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/694911" target="_blank">📅 19:59 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694909">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GHbfumyts-Q4e4m1GN-Jrg8vA4fCbw46MlpK9OxinCCaRRTeAuW9xNb1Y9K0TBqT9Xor4V-B2Vhl5m-fiYUW3vtzCn0lU9vxWLgnMJDSTLZV7PotZHiq6-9PSXMTaHjyG9_hQogEMF4qacaOBJ9FkD-AG04X1Ggk34bYumsMZwoC9ODu2JqgC5qdxD4xY0_e2OPRvsn52m0-eHh5IgVCgXrn8IjQK1sMlGgUlclcyBQmHhiKTgbeGcM3xxP-M9keY1hHh_gNOg6hu5JLWWRhQDwGv8nG-7-OW53T_UMZCXnq7jJmLpWMno_jXOS8s-Qnvp5zp9XlSu_h4jXml0RGBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rkN2m6I3Vx5uRxhwvL0PWi8soxZzufIGZpSlXdb1U1za-OzFpoCePsQTy_AWh9_g0ouIeV-BB30TD4CC4NXfwrNLGqUH_iOEn3EsNBZLIwRlTof1VzWHclZampma_OeTofcwbzr3eUwrPkKJZVVBuR2NXlMIqXUQif5NswNaqNk7RU_4oMBFb5A5z8f7mpaEb1W0bv9w8ksNz9LkPNcF30cjeFVgJx9LKmMZE7n6BD941f9uF-nmKeMSHPBlhAeSIIOFycTGeiIHFqunbGZFUfqsoMC1r44EBZHbDMUglcGB1d_RF4vjy4QdKN8yS_nMwLy7MKAiFPHTsrd9jxWE7w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
کدهای مخفی ChatGPT
🤖
#هوش_فوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/akhbarefori/694909" target="_blank">📅 19:59 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694908">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RJG9Y5z7f6xj9r9GoCwdWaegHIda0s2mOU38GwhMLIcxzYvBZoHSawLgG_RW7PWuMY8Q_e6W31Psd3nl57PR_rHfiBUEk8V89WbTT62T1kN_x18o8D_gOilzvfdObNwDyBDwPRkJc4MmC6vdPuGVSr2zAQDkFVzCrKJW8lJ8fMI6k-pzwPoC2WwGgELe1Qp1rOMaDzaU2l9VOwGdWYgpXGcfq0rSIHDGzgKJiZkAlof28bfouF2DBZCqbsIlOWPdvDtFK7rcgS-0EKZkpfVsn7p3c1HJtD-9M3kHRN2QFMkx8ue6urq4MG_qJdrg4BG_SHHzrH8D3dgJ6hD-62klIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رادیو قمه؛ رسانه ای که باعث بزرگترین نسل کشی تاریخ شد
/
وقتی یک شبکه رادیویی باعث تجاوز به ۴۰۰ هزار زن شد
🔹
رادیو هزار تپه که در میان مردم رواندا به «رادیو قمه» شهرت یافت، نمونه‌ای هشداردهنده از این حقیقت است که رسانه‌ها می‌توانند هم ابزار سازندگی باشند و هم ابزار تخریب. نسل‌کشی رواندا نشان داد که وقتی رسانه‌ها به جای اطلاع‌رسانی، به دنبال تحریک و تفرقه‌افکنی باشند، می‌توانند به مؤثرترین ابزار کشتار جمعی تبدیل شوند.
گزارش تاریخی خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3249439</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/akhbarefori/694908" target="_blank">📅 19:53 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694907">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
اولین تصویر از «اسمیت ماچهار» خلبان ۳۸ ساله هندی که در پرواز فلای‌‌دبی با خلبان دیگر درگیر و با چاقو مصدوم شد ولی اجازه سقوط هواپیما را نداد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/akhbarefori/694907" target="_blank">📅 19:49 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694906">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/633c871b0f.mp4?token=j2lr-Y0ksKCH_qdw0YomeccETENg9nZFXga4bncwwDKX1CTPo-Jvbbf-YtEB0KzU1fBh0DGVlODBJZsFta437_fNPP3fZye9N2_IHFFAFitOVUWSzNxnPMfFBDkl47Tc5DxX6dCtLvJ8AlIszITYGUb_9bImqpqdr8ooByLqpk8gaAPeOv5T2spgJtcNk4xFkzdz8jgSNtp2QLdAOShQHpfPfBVZCfouj8Srfncz1OJnOXdmFIi_wp-W5tKgogQrVoISCF-GQibrb0-7DeQKUnTKYMttAI459_rXfVng6qNvDvFomAWqki5cjs_rB4K6R40DLZul0refETQZP0NKCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/633c871b0f.mp4?token=j2lr-Y0ksKCH_qdw0YomeccETENg9nZFXga4bncwwDKX1CTPo-Jvbbf-YtEB0KzU1fBh0DGVlODBJZsFta437_fNPP3fZye9N2_IHFFAFitOVUWSzNxnPMfFBDkl47Tc5DxX6dCtLvJ8AlIszITYGUb_9bImqpqdr8ooByLqpk8gaAPeOv5T2spgJtcNk4xFkzdz8jgSNtp2QLdAOShQHpfPfBVZCfouj8Srfncz1OJnOXdmFIi_wp-W5tKgogQrVoISCF-GQibrb0-7DeQKUnTKYMttAI459_rXfVng6qNvDvFomAWqki5cjs_rB4K6R40DLZul0refETQZP0NKCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سحر ولدبیگی ۴۹ ساله و همسرش نیما فلاح بعد از مدت ها کناره گیری از بازیگری شغل گارسونی را انتخاب کرده و در رستورانی در مازندران مشغول به کار شده‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/akhbarefori/694906" target="_blank">📅 19:42 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694903">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4347a5175a.mp4?token=WMMcGn9qBqomRRspk9nTASeDpdxPwRzYLrbWYN8TRqGugZRxrzXkPMGC_dCaMBWY2VPf7MBk1O5JMb6jSTqA30MFHWtgnitfVqp3DT0NBvF_90uAD7G-9N7885gN81yZx96LTdJE7KM0hQGsyTsuBdoEDE25oaLtrl7QiboEvCrwSTFu4h3M6zUESB14wWaCRhfy4N-bfnReDR1kQ2Brx-BJ3BnBJECB7MtS0AurGgo8wDyjWWwbemu9JoOK99qJ6TuppASqJTy2d5vSS8O3hyzcMpT-Us0F7Fu9S5R2Rg7uYJx76W7PcW4dATJC9j3buUoCaXyZR8r2J0yKFHcrqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4347a5175a.mp4?token=WMMcGn9qBqomRRspk9nTASeDpdxPwRzYLrbWYN8TRqGugZRxrzXkPMGC_dCaMBWY2VPf7MBk1O5JMb6jSTqA30MFHWtgnitfVqp3DT0NBvF_90uAD7G-9N7885gN81yZx96LTdJE7KM0hQGsyTsuBdoEDE25oaLtrl7QiboEvCrwSTFu4h3M6zUESB14wWaCRhfy4N-bfnReDR1kQ2Brx-BJ3BnBJECB7MtS0AurGgo8wDyjWWwbemu9JoOK99qJ6TuppASqJTy2d5vSS8O3hyzcMpT-Us0F7Fu9S5R2Rg7uYJx76W7PcW4dATJC9j3buUoCaXyZR8r2J0yKFHcrqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گاهی رها کردن راه رسیدن به آن چیزی که می‌خواهی‌ را هموار می‌کند
...
#سلامت_روان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/akhbarefori/694903" target="_blank">📅 19:33 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694902">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pxPgo6HvjiGGsnIbGlVZK9ZYZ91rMwrg4QELN6pbNj8Gt8rRZo6wGKKRO8k61GPMVhs_W5etZEbQWZl_z3tVNfiZwyOXMhDfjvd77Tihk7wzYeI6LPyeDzm2jIpGPponY5HEx5TBAEYGl-QL11sMNeOIEI8MlNSWn-WxcmAbbwr1nLTk3M5iZp7lFV9vxO3mbzHKEtXJe9OKaSaR4H03vzB5pVI3cGeqWbH9ZPCBps3EvGtX6Qbs3B-o1hPysVbZC3dQybVqw-UY5xX9fH52kXFIAyVYFD9a7-YakKx0A49rvOssJuFJLTgToLWQZ1e2CRcI6b_xuM7u7marr7WFlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بزرگ‌ترین واردکنندگان نفت جهان؛ آسیا در صدر تقاضای نفت
🔸
بر اساس آمارهای سال ۲۰۲۵، چین با واردات حدود ۱۳.۷۶ میلیون بشکه نفت در روز، بزرگ‌ترین واردکننده نفت جهان است. رشد صنعتی، نیاز بالای بخش حمل‌ونقل و ذخیره‌سازی انرژی از عوامل اصلی جایگاه چین در بازار جهانی نفت هستند.
🔸
پس از چین، آمریکا با حدود ۷.۹ میلیون بشکه، هند با ۶.۲ میلیون و کره‌جنوبی با ۳.۸ میلیون بشکه در روز در میان بزرگ‌ترین خریداران نفت جهان قرار دارند.
🔸
تمرکز بالای واردات نفت در اقتصادهای بزرگ آسیایی نشان می‌دهد امنیت انرژی و تأمین پایدار نفت همچنان یکی از موضوعات مهم در اقتصاد جهانی است.
📊
آمارفکت | مرجع تخصصی آمار در ایران
@amarfact</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/akhbarefori/694902" target="_blank">📅 19:28 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694901">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
سازمان عملیات تجارت دریایی بریتانیا: یک نفتکش هنگام خروج از تنگه هرمز بر اثر اصابت یک پرتابه ناشناس آسیب دید
🔹
این حادثه باعث وقوع آتش‌سوزی محدود و قطع برق در داخل کشتی شد؛ آتش‌سوزی مهار شده و کشتی به مسیر خود ادامه می‌دهد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/akhbarefori/694901" target="_blank">📅 19:23 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694900">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ccf1e5f71.mp4?token=L9sXemC-ctgh3GWQwA9Du6P9K8cHtc8cd-pt1_gSaTB-mlLJzYqcUWPL3tDPH6bJHhCkPUHhkrrximTIw7sl4cMaHlEglkF7eUnA5awlQBIgf-Ng41-PMCvRpvQ6sCkZeUWTPW1WKO12Ea06LnxiY6w6f8MyDjC4iomIBvzRFu-JkpvnYqEYW5l9ThARjvGZzAeFi3Tc4mXwSyYJbBg9Eiki5_aG6lMRxdw9Ft7IpJzxw5_H1EQKDuWQgdPTae0RlczjQc9m_UtGQDedNyNKvQAXq4czqo8QKR4sKgYO7ruNXmGiJ-nN7NqwuA0jgieKw0632AfJPUS1XyVeasO2Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ccf1e5f71.mp4?token=L9sXemC-ctgh3GWQwA9Du6P9K8cHtc8cd-pt1_gSaTB-mlLJzYqcUWPL3tDPH6bJHhCkPUHhkrrximTIw7sl4cMaHlEglkF7eUnA5awlQBIgf-Ng41-PMCvRpvQ6sCkZeUWTPW1WKO12Ea06LnxiY6w6f8MyDjC4iomIBvzRFu-JkpvnYqEYW5l9ThARjvGZzAeFi3Tc4mXwSyYJbBg9Eiki5_aG6lMRxdw9Ft7IpJzxw5_H1EQKDuWQgdPTae0RlczjQc9m_UtGQDedNyNKvQAXq4czqo8QKR4sKgYO7ruNXmGiJ-nN7NqwuA0jgieKw0632AfJPUS1XyVeasO2Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صحنه تسلیم شدن نیروهای تحت حمایت عربستان به حوثی‌ها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/akhbarefori/694900" target="_blank">📅 19:23 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694899">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Os0dd-V9ZvdSJ_1mRcIwamkW6wx-EPDf9wioA1Bv8ChXFNMOsL7ggHCezdU9-VxjTdUcLzE2HSQSTBSVbfFNTB7OpXbkan04DKf14ns-M1zu65Mp1GBlgRPwezaSsDshDZPsl5Nek9MLrrFzWkia1nZGRkbnI1UFlslrvC9ZYFQH5LCsjmXB8t8XfxGXrgQUdDYyAthJTOH9k78lwcJUnxTsIsRmu08SCUVblfiOLVhs1Ie3Wt0fmotuO9diYMugMcI0mEkpL4RLWSpipw_2dA8n0fLG9Jg3CG_jW772iGi7eH1r-mqEkssfAZhi3MhXDAUfi_RDo8FRzN9AABVgcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قراری به وسعت یک دلتنگی؛ نخبگان در جوار مزار رهبر حامی نخبگان
🔹
دکتر افشین، معاون علمی رئیس‌جمهور، و جمعی از نخبگان کشور با حضور در مشهد مقدس، قرار سالانه خود با رهبر انقلاب را در فضایی متفاوت  برگزار کردند. این دیدار که در سال‌های گذشته به‌صورت حضوری در بیت رهبری برگزار می‌شد، امسال پس از زیارت حرم مطهر امام رضا(ع)، در جوار مزار رهبر شهید و با تجدید بیعت حاضران همراه بود.
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/694899" target="_blank">📅 19:18 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694889">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZPr_2AJDMpYpHf10PcpcrAU9lXcHOlwJuxa6R9ZVyhC9hYjRK-joXzQj7GqB-dsoUH5kGUKc5OiIpE67942yljUq9Z30si1F4lMcCfvUv1_n3o_Obu52DEMidx9Ssk_Xaw9S4vR7N2tqjXYWN998s46YRpYtEVxmm090g2JEL3Xum5ICvIe6TaQ_Uo4-irbfb4nAYQhQXWSeWrYO_uw-MyjkKovDDOIAIKEK39D5ZJFZ46x6YMmY9iI84n27X6pz8N5vZofOGx2qmA34acnl2M6LmaLrSr0p0MdrQ0I120btKiIsaWJwjC4o8t5KzRjzKgzRIP1LqSuybmcBhBvmSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dkDge5oDQKUV139YJRaxAido9kQM0P3IhbzgvkHFurwsxs2yuWTFCMPd0J2DE-mH57PvmtFZnFZ6C_jRZ5grxzO7ayFmlFDPHNRfcjsDDTiycIoj4b1fw8eBh1B42_tDUtwu5QzCFzr3LA1THBLt7771CEPzsqtftCvwQ8AXarV_5aon06cagOnOuIUBqLzZcfxiHAF-C6so8NGlasD6kww2YNOCjOEf8R6GQpt3a7knoEm2hwG8O7WVODokFAzqU0SszuBkfPpMY16TRANEJNwFZ6dnC47E6NjtgmwIJptzVVdjPKfijmNbakoLQBrPmWy8y-dy830atGwLE3S9cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VvwjnWN3Y0u0Cl4PW5_yO-NH1p8-6xOpbqTxxUhc6E73_FayC88_FrLD_N0NS--hiutmLGobhANJDU2-8Z5Dx9LeDpnuwWDiezDtXWySkGIaepr7QWyCCAnnrtw8JJ9ZKlWp8lhyTT7X7g2rjSQPBMOMTq2FYijgUrW58EEvDhLKX5BV4tKaG7Z4qKda2NgYhlLyteYvl9dFqMLI6-9XGmn4KhdthVmWl9YxqwB-dMcYK4QvgtvsdS9WrRW7dOHphDnBXA3G49jjcgeOMkO_Jb4jRaWcz66iSEaPaihlFQK6dSrZVY3lRvRsccLykepe2NqfnF_g9rOfJZfi1F7rug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uROBhPCPu-yWNBAGC0GNMFd1ttFDHIV0oBeamz0fMj2UKSmVK-uxg2W5R6V2WpunCW_chx6uqeq91U12ZSJH49m0GD5Xi83wqH3dl9YOfXN34VUM3AHRW3rZ8IA8stDB6o6VuptuXqAhHKqz1baVYsdmBSGX8OOgXbBxYExW3WCMqaQp4WWpFrI6lVYfad7miKnoXZxSOlrpgX1BmrF-KjiJf1NGwOcVIUrA_V0rjIiPabX5-XNg2wcCiukufg5pjssrOcHv0f9Jm0RNamvHonlWSPJRfnOiTBvOGrQpL8zu_E4YXCYdygW6ZdwFb10DpyNxZ7KIKWnRYMaOYw6aGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L4279EcWQAsC0R5bSTh2XtyYcIoXiweazr8bUi9C9qY6vv6wphBS_1HbsJ3KWk7RnllB-PIgHwReayBR5MYasyNnydDayfiiIkTCD2bwiKgbYYmAVMsUwwFHjKDzvFCsHCB_UR9JcxI2NC5CiATsTmao663PnCtQri7O3T7K9Bz9M3C-YVN96X9rXAWEMveNpmBNMc3n3FK_x8jslt5eFFfMjD3ETxzQMfNtJjVm9YsDam7Xkndp73rUOB9mEub__BvRH0hXUbkfC0TvOgxHlyUl-YCeqfkCWYrvbmqPcILtCypD5vSBI6wpDRCMojVS1guJIrvmpSGrTNgCGlsoGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/stc5H36cabvxApk0laJdOGJcnxjBIBqPdqD20PM_hAJ7gnrgefUewDqmyI0kLpVNoX_KyWl2IhDsclPftwccPgqwJfvxEQmLGtqJ7dGL2StqcVagMupiKe5IsIjzv8nmlVZa-o9Kkpz5VTX1ZTnSCmcBx_-etneEL_ebMiirUCvPRdwGYMsxGKJMc2GLVfdeKRl9hSwK3VkW9_qVkYYDgo2kZL2B7FFPdSXxJDeSJXthjb65l-P0oH3kfjdAHWwVELlC3KEoJqSPzixtELlGfg-JFd-DWpVBldFIfOZz191nTP58rrpRpXIhQmJnIdvFU0vOQy0FShdj-u1iicTyDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qzZq_n2bPmc3VVLUZ_vkI2Y9wS0Z9yvS4_wJ8UY4G3JWMbtz7sEkbPSLLQgEvoIuU_CBnhRXPVCP4-d_qH-4ojPxP7mfV95tYPTGqkQZPFd7y6aiDkz8ydS63mLzN-zAYVk_PvVz3f7Pxxq97W5nesRelhNlgBHOv_k-7HUyO8-L8j3cuwq_bolIkbYvbW55_h8gFv7fG47HYTKk4mOu1qOGu_i5IH6vLiWYItZjPAcz18rP1mNmgmsVyaQqTArG8FvwCOL1QCVtnkTh1w0iIc6Vmr1F-tzgM0Gdr__fyWJNg3X_XHvOFWAXNNEiG-qAZZvyj9hR_900d4eF4K1ZAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EocH2YX4Mpu6WYCQI2h2a9lSCJJMHZbb_RMopHhenhJaiFC3NG_kbjnBSzJJME72fXR-N9xs6YQnaoW5JVaf6rcO2vOOgoRzks1t0PbwcfWq4lh2nEs3p7Xe0cUhnOi4u4nyqphcSl9vyvSFJ7xIIBo3FnISHlX_fervUCFFj6wG1kgs_fpf-uShOP59o0OzrPkLDqq2SOj4MjuXgvy0CH1f8diHyaLYyfmku6N-iHZiIgTFuVH1SmA7fobpFzDwh0g-dNRKl5sjc3wGVmKfTo_GlNk_q3TuD_bYJyUmCg6VHo_rfj_KDE49GX2mlft16Hnm12dTr-wPcHVlBnrQQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZPzax5kIfCJMIb-wrI5AontOPDvEBSj5shj1647MO-02OV_JssNHtnoURkFViOLWILGWHa5fwVPnbpN9aeNBw_YJFf-qku93w1_yOuodBf4kz1xQPSlYqWjg5eUcSFi4c7X5nY3hCdL7oo7kSd3WQYN_POrubJ1RwBbquoQbmYQfeTdsLDY88Rv15muRnk0NGSXdPizeo2QUQk3i9Mz7w9hy0WQIJi63pv4HiZpATl7DbH79H9RD33pscbgtRFSFcbOwXVMSabSLa2rHuAAhFm5HPmnCFYAfh_CU07XWC-s6VzSh93KIjU_6EITc7pT_RJRkA2MyZtwN3mMxNV8C2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b9403uBLAf8XvScsMFN9EWVoFO0_Lkuu7Yq783RbNMRjbCApurLlUxZOlz8Yoa7hvMxkimUTpuv3PmTt-Jl2DvtJd-1kR37XAjIsBYAu7I0spwfdmBCVWNdaERmTPeBPdtd7EbYu1BMLSQXgtH9P1RVpohVEHPGWpT3OwN6l30vFXrVIGJbl3DzFzn4LQq3wEGjIHtf-zzSKUDmoW0Ka4vOyhoGbE5BPtz7Wap_GGTwIZiCtwR7XCB6do4b9aF7WN__LlYy-_7TN8FQEGtHD7qpwpv1dbrh_oJqjL7VK1RsRu3xX1Zbaz9E_9zzfXuaW497KyUSfMsll3s8ozpBYnw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
وا‌کنش کاربران فضای مجازی به توئیت عجیب و کنایه‌آمیز حسام‌الدین آشنا به طرح «تورم صفر» شهرداری تهران
حسام‌الدین آشنا که با بازنشر اظهارات زاکانی شهردار تهران با عبارت کنایه‌آمیز "بماند به یادگار" به استقبال این طرح معیشتی در میانه‌ی جنگ اقتصادی رفته بود، اینگونه با واکنش کاربران در ایکس مواجه شد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/694889" target="_blank">📅 19:15 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694885">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PmNGEs68epOW055TE1lA4OAHEGIWCBaPYpJIprDD_20s72GmWNjiogUfBLKJS4Fpe8oQ0IR3uhCAu9szh3sqEIES8s2a6qOjOtpPzHZCaieXWpy0Wg9RihB3zzp4WIcF_INYQv_zgfWoEpbm0_LEzJSUUxjuf2NWhjYPhMeWqfeMYs31-E8RdluVb_KcX3IM5lBZRZPnmpLBRipdGHf7C1VqqlCfnIokwRZy6_ihr2jiKxoXqmc052MqaJMHFozWm3Cw8j3Qrvnxi5ABBqyzB-Gw9lgaJHCaUpzbQFUP7quSj9xBACs1MZJ2jsgHT5U_ZUSS7XkMZjUc5LzHqHbRaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r5T7pRgoLU4UYhY7ShB_CFVJtGRCg6a4KbIuYZY_iWuQWJwKSO5TS3YCqX4qXWn7vGRjmwihS03mE-NiQJIdxOmiE94Z4h5_q8hlgCNnYproXsJbr7bWwwtDbkPGFnUM2dIGClBH72gwawbAvu7zUVPPygEhp1s9awWUeCHmWLKUnkJv9SQRdZGurWMK021Vh0S7sqF0YZpF_128OOjmUAIp4dxqmFcDAOjDMFD_p_quviejKimdouDcSjX_qThpfM_Av6Kfm5fiGbyaCz7QelGvIWaXVluCU1E1WSFCD4WGLZDFbmvQuukcvJqFQHX11Kx7P4z6pH-_YmHouE1xVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PCLHuIrxTXIMABrEXRpRyEQognHOU8p-YxcU-pA7I8Y1U1h15GJT1RVFnknW4WKsVRkz8zZhGPYpaMJ3aN_WWnXeqm94e3dAhVKtEhJhRY1DwWtp6hqnMOyBZFO3mxybqrLKm4ISY9fPYSsPKxJ4shyNjBSpybPnfYdWQWUP1kQfswiH_-sHhskyuzAbuGw0CZTbVE9eEcL521NxI27KRnYrCyGrrQZMWRw5iz-6r_tKSr0B8mjgj1Tz2I5LGX7E1p5z8gtN-ewpvX6uN-d0hpNkQkY03NfdulEmr3RuZanmNQzZ6t-3cFi6FuF0oARn9EOoO7yz02jtNYz4zOUD6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lZ7wFaNJJtOCsVZttJizT9FNmXkJYqI0s2O7teraAAT_ts78S3fj6J_JR3OKkCDRfnB7zyWafsY4JT36UMq0My3Cf6clBv7IAbdOiiUobAeRkp6AcrRZRWJmphF8_PcsxhJakAySXAYL_qZesG3x9BTaJokQdxg7GSFGeS_J4Z71WMFW6LvRCNR7AXEzyL873GebN9ydgWMvk3033MS2D7xmn9Qi_s3t8DfUOoKu_iebaCq747JM2nqciu9rvdk1wAPY38phO5H1GC3zWPGYCBFu9ZhUU1lh-KwEjiTY71xl5qxJL2auiQd0rlUIailxCjF9hc50ZwtaFLVVR3rgFQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
آموزش ۴ مدل بستنی خانگی خوشمزه
🍦
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/694885" target="_blank">📅 19:12 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694884">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88532b4554.mp4?token=hn2Lgl5e0-xCqY3ns0-qbB-pLT5bhvaGorG1bi8xrNL2wuuN3cYdxjDMLRs8R_rS4a2EnZ_YZ5HkmKeVO11UuzbTe9-u5kS04l7XXHTfg6MEdQXo9cK76jQQTNaJMUOssLpbpPp6SsFMppAm1Xkz1mSYm7MiEsHtGLL0oDKJiqQziX0Rc-j--IskPgWsYJquTDlZBTONeat-jOcqNO_nD3ekiTibcZZNWq0cW9Q2AIwHiQKBxfmlosrvdW5QNmCTiMmocrFvkxnk3pTb0o6KAu8aWRxjOZLKxhvOECa_kJg4SEBkkLWVeNVi1MYBeMQCacTCuiHc3I2fugh1BLUlEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88532b4554.mp4?token=hn2Lgl5e0-xCqY3ns0-qbB-pLT5bhvaGorG1bi8xrNL2wuuN3cYdxjDMLRs8R_rS4a2EnZ_YZ5HkmKeVO11UuzbTe9-u5kS04l7XXHTfg6MEdQXo9cK76jQQTNaJMUOssLpbpPp6SsFMppAm1Xkz1mSYm7MiEsHtGLL0oDKJiqQziX0Rc-j--IskPgWsYJquTDlZBTONeat-jOcqNO_nD3ekiTibcZZNWq0cW9Q2AIwHiQKBxfmlosrvdW5QNmCTiMmocrFvkxnk3pTb0o6KAu8aWRxjOZLKxhvOECa_kJg4SEBkkLWVeNVi1MYBeMQCacTCuiHc3I2fugh1BLUlEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
منابع خبری از شنیده شدن چندین انفجار شدید در شهر ریاض، پایتخت عربستان سعودی خبر دادند/ تسنیم
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/694884" target="_blank">📅 19:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694883">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
مجوز روزانه ۴۰ پرواز ایران به نجف
🔹
رسانه‌های رسمی عراق از توافق برای انجام روزانه ۴۰ پرواز شرکت‌های هواپیمایی ایرانی از مبدأ و به مقصد فرودگاه بین‌المللی نجف خبر دادند؛ شرکت ماهان از این توافق مستثنی است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/akhbarefori/694883" target="_blank">📅 19:02 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694881">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o7kHZ1AmpBeieuxGtv7pyG3dtEB5RBXS32qdlFQgHjrqhattSoWUjvyJuzVqvxM0k8cPwQB0uYx1FN0IDp5Y8Su2-8TdUqkunLtt_ljjSCpz7VtmDg5Wlc-iP8wImASZgk9DOtjwowSc5j7aaL3_J_shCoCN-k1EE0nDjPf7Qnql7GPgrFTRlRFYsQkis3j7akdq8dnhaanPBOLKxlVKb9caI19xqA2egorLpfe8ztNA_kG5_pj61ujVcLjopo9GZeW7dGjrH4SOcZFVV0cxLjNc78-v8hC4wZSWwpeUYWSkOINbvGgL_JhNouDaqPsdK7mZ64uPQsJ_CBDxzDBwnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خرید بلیط رویدادهای فرهنگی با اعتبار و کیف‌پول دیجی‌پی
🔹
با باز شدن فروش بلیت کنسرت‌ها و رویدادهای پرطرفدار، سرعت عمل در خرید بلیت اهمیت زیادی دارد؛ اما پرداخت یک‌جای هزینه‌ی بلیت، برای بسیاری از مخاطبان می‌تواند چالش‌برانگیز باشد.
🔹
حالا کاربران می‌توانند با استفاده از
کیف پول و اعتبار دیجی‌پی
، بلیت کنسرت، تئاتر و دیگر رویدادهای فرهنگی را از سامانه فیدیبو آرت خریداری نمایند.
🔹
در این روش، خرید بلیت با موجودی کیف پول دیجی‌پی بدون نیاز به وارد کردن اطلاعات کارت بانکی امکان‌پذیر است و علاوه بر این، کاربران با اعتبار دیجی‌پی نیز می‌توانند هزینه خرید بلیت را به‌صورت اقساطی پرداخت کنند.
🔹
دریافت اعتبار دیجی‌پی از طریق
این آدرس اینترنتی
انجام خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/694881" target="_blank">📅 18:56 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694880">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nGZ960Bdn24wGdTNwDQgHyIKNT4RDm2TwkJDVpZmDGxfRfKgnbC81yUjcsSsEtE7Bprt-vQLh3FFLqUErBJszOEx8uNkhxy7fvU6oVJV8aNvq5Xk8PEi-rOvOT-IwwXEg_pQdruhmn0YD-RDgJ5zbluQvNPPOoho5igNF9R1ZBCt5DJr1NqQEwLjsONKeRC8k1Zen5DUB6Oyk5EU6odKXsuzBIl49fGgjlzCnvWk0BvRcvQfIuo2Ss-8qHuxThkSx94Q5gkOJKGB0qK9oioLTgIF6IeplmYZU172fuwXukq5JO8ADKHL545kVonTx2gLOB_K7XMbuPhHiVDzcSoe9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ضرغامی: ای کاش،بعد انقلاب هم یه حسینیه_ارشاد داشتیم تا صاحبان افکار متفاوت در آنجا آزادانه حرف بزنند و مخاطبان هم با آرامش و در امنیت پای آنان بنشینند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/akhbarefori/694880" target="_blank">📅 18:54 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694879">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
ظریف: روابط ایران با چین و روسیه باید راهبردی و همیشگی باشد
وزیرخارجه پیشین:
🔹
روابط با چین و روسیه نباید به معنای وابستگی به شرق باشد و ایران باید همزمان با حفظ این روابط، گزینه‌های متنوعی در سیاست خارجی داشته باشد.
🔹
او تأکید کرد گسترش دامنه گزینه‌های راهبردی، به افزایش استقلال و قدرت چانه‌زنی ایران کمک می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/694879" target="_blank">📅 18:52 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694878">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
منابع خبری از شنیده شدن چندین انفجار شدید در شهر ریاض، پایتخت عربستان سعودی خبر دادند/ تسنیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/akhbarefori/694878" target="_blank">📅 18:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694877">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d25rLaS8CtUwnQBRfGK0Xz0XO_QxifWa09EBze_poM6mNweyDKTxds2TzIKJfXx7J_t0kyvTEZ_kTq-bsWazX89PcAO47Idr9Hevu6RImLoX1lsFUz-Z8ueEFtPW4AVLskx5_-M-yTTcALwHluL_UwUwNIBggJuXSA0gc-BLBV_dicJzLTtli0frgUF-roMBejmYXMffIAA6SBgJM-p_hk1tVSvEFxpmm7btiaXFtGMFKNXofRf7EIhcXhlTxqp96JKTcAWnyc2V5RU54fJZpiMInYwRa3MITBynT8BpZwgiuFAQYYetKhdqm_cTrvb7mBj06swdTCNlEDmXLVxqvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سرویس دوره‌ای قطعات خودرو هرچند وقت یکباره؟!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/akhbarefori/694877" target="_blank">📅 18:39 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694876">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0df570e359.mp4?token=A6vO9_38HNkw43XehxpiRs6akqkc2EMB027EB2hCL9O7bSP_GH1IxVpApJ3PeULNREjS7YjRzTMFjUnvJryIESJ3j3MGeT4eOvB-_HaUkkOOh6KEc5DCCjZAFbcuNVwiXcnjajX_BOE4hM8OJxeTjZcIL4Ml1rJ5ERO69s_OH3iYPgrcOSCXPv0-AcrsnZ9timhDuYcUytUTfHDwKcf5t9kUkCcGjLQrbAbbbySjmlouqrud6XsTx09qHZM-pjMbSBIde_llmuwPA2VMQMACYd6xfp6lM4KDFr4NTscbEtMNcO8Oo1G-r8MD-imzWejYwmGLAURAU6ha_qxrcoTPGrkwe6fasGLi654col-1dqKESZcsd9U_LJK-5bU07Qnj6vlZrJ2F2wBQSf2NsC01dZAF4ko-tmT2vTi0WIfzgI7_kuUiAJzu2N-nosIEgRVw1g36HeH59eu6EPLla6hhtbD-MiIwNByugtVD-5l1V2xeu2QqgGHqfJFwzfhfFf8a0lu8ZzLLsy7yDbbWPpydDxkpdPZyS3wji6IGB2UFMaPy9PRbXLYjcw5_OxXHvUAHWQQ7Tn29O6Tw0lxwwJqrachRhK6Df2xsgOR1nsAi2dCXf1Boy9m_oKP8EaV5MKm2KNaoA3YZYd2eNkGdYqnVfGktA58_gglNoJwtASVrDV0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0df570e359.mp4?token=A6vO9_38HNkw43XehxpiRs6akqkc2EMB027EB2hCL9O7bSP_GH1IxVpApJ3PeULNREjS7YjRzTMFjUnvJryIESJ3j3MGeT4eOvB-_HaUkkOOh6KEc5DCCjZAFbcuNVwiXcnjajX_BOE4hM8OJxeTjZcIL4Ml1rJ5ERO69s_OH3iYPgrcOSCXPv0-AcrsnZ9timhDuYcUytUTfHDwKcf5t9kUkCcGjLQrbAbbbySjmlouqrud6XsTx09qHZM-pjMbSBIde_llmuwPA2VMQMACYd6xfp6lM4KDFr4NTscbEtMNcO8Oo1G-r8MD-imzWejYwmGLAURAU6ha_qxrcoTPGrkwe6fasGLi654col-1dqKESZcsd9U_LJK-5bU07Qnj6vlZrJ2F2wBQSf2NsC01dZAF4ko-tmT2vTi0WIfzgI7_kuUiAJzu2N-nosIEgRVw1g36HeH59eu6EPLla6hhtbD-MiIwNByugtVD-5l1V2xeu2QqgGHqfJFwzfhfFf8a0lu8ZzLLsy7yDbbWPpydDxkpdPZyS3wji6IGB2UFMaPy9PRbXLYjcw5_OxXHvUAHWQQ7Tn29O6Tw0lxwwJqrachRhK6Df2xsgOR1nsAi2dCXf1Boy9m_oKP8EaV5MKm2KNaoA3YZYd2eNkGdYqnVfGktA58_gglNoJwtASVrDV0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت یامین‌پور از سفر به لبنان و نقطه صفر مرزی در سالگرد شهادت سیدحسن نصرالله: مردم مقاوم لبنان، مشتاقانه درباره حضور مردم مبعوث ایران در خیابان ها سوال می‌کنند/ ما حامل هدایای چفیه و انگشتر متبرک به دست و دعای امام مجتبی خامنه‌ای برای مردم لبنان بودیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/akhbarefori/694876" target="_blank">📅 18:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694875">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
وقوع تیراندازی و درگیری مسلحانه سپاه با عناصر تروریست در راسک/ تسنیم  #اخبار_سیستان_و_بلوچستان در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/akhbarefori/694875" target="_blank">📅 18:34 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694873">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
الناز شاکردوست به یک سال حبس محکوم شد
وکیل الناز شاکردوست:
🔹
حکم یک سال حبس و دو سال محرومیت از فعالیت‌های سیاسی، مجازی و هنری او به‌دلیل انتشار یک استوری درباره جان‌باختگان اتفاقات دی‌ماه تأیید شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/akhbarefori/694873" target="_blank">📅 18:28 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694867">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uWer6rQsX4SMDc6gL3vE83a_L56aDuwrb6G0o7wSDmt1_OfMAPfgXGG7On3Y7T8WT7crCZtX3mtqlkzF6NfJlnPkiYj-0IRUEuHkb3o4seoLFmbMhKkNopoU95mFSfwPggFyPHFifX-beTfS0y6rqllfFAeZ66glM9CHCn2R2oaAeVp5iA1ZQ4k-1eOMIdsVorz5SK40Kuum37eftNKiGy_Jtz1HLV1N668GlhSQxvTIh3hKCGjE4J3x4mYPA6TfV_ur28nWmE4xYl9z-b05-Hw9UBXgvqAQuT5BxcfYHXG7pIzg-jAmWiYGu9AVJ-sqbIHVv70q3-2t_eNIETFdGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kKBRhqHzJL0vcPo-OXqvzkPYKd-fBnknK0JjtgmLDspqquniBnwEKJqfnhSv60nJz_dFS0VwbZUM24F7DTb8QytQBF_yWkHOeonqB7tTXKatVU7tR1RPKa3Me9TIUfe6ZeuwEUbGjASERfHW9zy2sFsYnjDVVpsVEywPkgsbTA86roKLx6oYUufUo0kepTNKTB5cP6jGS_Lzkcp1OuhtdgvDr7eUP0unlZ8Anrn2WHB38XmR52d-f0VEduYVYEvE0PG65tKLey0AQ3rjNr68lYlGTHPBCWNLf9gzAGK4EODxc_sI9sk2kY8MssBSrGDHRxrncEK3D1vKK-jkiEz-3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KFZRH7wUmUEj8AxECvK6-PIiQSLAzU1Cc1R3t7lUP8uXpJdXGAqBsoqnXn-c5_xl5C0aoPpsXRTPxr5RMEFLidgNbL8QnWvvHNlm1GK1hyd09a5feHJFRNGEobiXuAgx_0j7kqrjInWlsqAUofgp2tVIs38hDoc5zPzDzbtwNbtDbuIMGrkWOeimY6nu7vTx2UcsvMpSruvIaAkGSWPQ0GHzNS3dPKZNt3gyk_YEryAbTab9vmRWsxi5P6y1wOVfIb2vbgJ09IS1nN6yaQ7-7jX9hRc0HGx5Q3uy5X6Dhu5pqxgKdEJn_HlIHXg-xE6mxirgJpeFSNQsMIJyI6XArw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/onvb7_8U_4B9fKKsa-T83KBALGQd3mtHtSdGtIqJNcKNa2mZ7QTEdXS9tP84aph9lGPR2GeDUYArT09i8hGQmxih1DdrngQQKIdnppOZ7dq46ZqnBbm_wesswf9mwZW7cWe3rdPe9ZNLOumiCuLjqCNkEUSHw0vv_ZvaDWTrit2IPFm-fctw1KBuLKI2N2NYwH7MAl44wnx52lSWXuwDVMfiBF8-05oM6MiSxB2Bm9PBPVKYCue7sXvQKR2i_8vDVbynJPnv2LBYCTqlGB_NLIbz0j_PX1-IEVl-t7MEJrtftXMC7EEThzoNZj-eoKrtuXZUTRh2b4N69YhB7Rx9-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FMUvBo24zMh7A6FYlJyD02C81eEpqTPWAHQjONjvD1aiMqe_jGD79jfHyDW0OwAoazCoNUtwXW1BQi6tn70K1RYm4xcbolGcfQxDqUj72bJPcV8mpreaId_5jX40Vok6GRr5ZyGe8VkbIMm5in1xatQF0VR6RBAlxujwROFuiBmZyXPhVeaU6JyHm8SSwaSY-I9dET_9IqCwrX9V9cxIt7_KjkKPHEgwViTwmyTVp7DZOv3ZGviv1JhpWUbnsrPs7MYLpVl_5sdKHFJtPPSpD4H01HU0787LCsvv3JOStg24y-bJ8q0v6w8tb1ZiCE7v5w7v40ihOnJPSE2WoqnDNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nNi8H-V6PQ7t0ASTdBn7e3m8EuhqNaYJcGeGlEZbfgrTN_jqGbrhljdfLC1dTrroZ5vkh4GEOSYgbamHyaKl_TkvPn06ewK1TQUkx9W-vVjCb4xsp7stfleCJ5JnKRYalVwteHxZcNWxPMxkferlKetT45Af1w1Q1Q-gyHI6O_CD3qM0vB5EsSs_aTsbJ8uM2HrbVHo7a39iSJf5ps1joWfagTv-Gjhyz9FNxWazKdONdFNwJ3jYgcs0TKruvLeIv0VpXbvrQCUzANE5rIFbgeTuaAFsrssB1Xn-Zg1qjaszxyY-FFW-DE5s2Ke9MGixCp6JHpx7McCQ7bBYTeS90A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اهمیت تغذیه در سلامت بدن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/akhbarefori/694867" target="_blank">📅 18:26 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694866">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d9f749cf.mp4?token=tfIeSUjYyM64qoWt81Ac0Kvt8eYA2PZ6vx3fbNGvkxX0O45iqm4goJBScNVMGtowziTQyay-PDRikWWUNz6IdpPe4d5Ghsx-r_1NFUIfLPdIN9qugswxFPom--7X9u-8QOZledBtrB2i2Zb-WzpRlrtOGmqmiX3KML_7JV9sdfJoQ0QjutY-f5h2Yv7air_cgkqEEsWbpt1G6lZ5sjLerisAvmKZTfEP8kxvA9E0xs-IdVhmByi0RbEyNYDcmwCBfyPeq3pVs9omIjRZ6CtY3eQWF-Z7ytiRelDgOQyqShIP6jZVmCXOF3zMHphKWsDOIHFidfIqanF1Eo00Yj4wr02r1BrjA7gR3p_DtV21C5B8G56Wr4Z0SdiCgmkBo_7sCfEAD8xqP4mYKKq_-i81JpLtQTp7LXtm-uDPv_DpVAlUylAg7ZtDUwl3_WttW2ntnBu-FZpzRnHa4zU0kbxj5w3cW6d27kX_2wu42GtGtLeleYuj5IrMPhhSRbg1lNKdeREtFH-Z6eBkaa0v9gDsikB1avUZCivTzBGFI4fMorIrmkh51uQD8aDKXSec5JyMSRnDC-DyJsUJEPpSPkxyFf5DqXAGCAmGqcXCS6aHK_QRdW-KHk8Z7DN8kAN2hW8IoCHoHeuBqLvi0xSCwRnCJ6JXqsq9jg5gLg4CRm_wHj4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d9f749cf.mp4?token=tfIeSUjYyM64qoWt81Ac0Kvt8eYA2PZ6vx3fbNGvkxX0O45iqm4goJBScNVMGtowziTQyay-PDRikWWUNz6IdpPe4d5Ghsx-r_1NFUIfLPdIN9qugswxFPom--7X9u-8QOZledBtrB2i2Zb-WzpRlrtOGmqmiX3KML_7JV9sdfJoQ0QjutY-f5h2Yv7air_cgkqEEsWbpt1G6lZ5sjLerisAvmKZTfEP8kxvA9E0xs-IdVhmByi0RbEyNYDcmwCBfyPeq3pVs9omIjRZ6CtY3eQWF-Z7ytiRelDgOQyqShIP6jZVmCXOF3zMHphKWsDOIHFidfIqanF1Eo00Yj4wr02r1BrjA7gR3p_DtV21C5B8G56Wr4Z0SdiCgmkBo_7sCfEAD8xqP4mYKKq_-i81JpLtQTp7LXtm-uDPv_DpVAlUylAg7ZtDUwl3_WttW2ntnBu-FZpzRnHa4zU0kbxj5w3cW6d27kX_2wu42GtGtLeleYuj5IrMPhhSRbg1lNKdeREtFH-Z6eBkaa0v9gDsikB1avUZCivTzBGFI4fMorIrmkh51uQD8aDKXSec5JyMSRnDC-DyJsUJEPpSPkxyFf5DqXAGCAmGqcXCS6aHK_QRdW-KHk8Z7DN8kAN2hW8IoCHoHeuBqLvi0xSCwRnCJ6JXqsq9jg5gLg4CRm_wHj4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور ژیلا صادقی و راحله امینیان در خانه شهید علی زنجانی، از شهدای ایرانی حزب‌الله/آرزوی فرزند شهید زنجانی: «دوست دارم آیت‌الله سید مجتبی خامنه‌ای را ببینم»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/akhbarefori/694866" target="_blank">📅 18:22 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694865">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cd7792b6d.mp4?token=s_0ezOxy15tYrAH56L0m3ZGrrjNMJxk_qtP8HK9nAKLN9OPZ44ZOIfcFHj4neAuLbon5ckp5zxLKPj-IyYRO2nPXiLE9JYB2-hwzGDnQVoWqCj6WC1KOBzx_zaDz0F2ZRx6Se1Abtqld8iqjS4o-0FUpV5k20j2Nuck1GDDb8GNRWB19ko1-JgneE2WCgAd8cqxh8-yxUsmh0C4fkJD95P71TuJdCkTskRN4jWlkqaU4e8es3cSsV2ltfTdyNQIPvZMasMkYTD3KNEpEllzBVQAR0335Ti9kAK6peKXSLG1ZLfRQ8g6j1ONeX-KC-5eLWWh6MmdezpX_JGtRXs_dcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cd7792b6d.mp4?token=s_0ezOxy15tYrAH56L0m3ZGrrjNMJxk_qtP8HK9nAKLN9OPZ44ZOIfcFHj4neAuLbon5ckp5zxLKPj-IyYRO2nPXiLE9JYB2-hwzGDnQVoWqCj6WC1KOBzx_zaDz0F2ZRx6Se1Abtqld8iqjS4o-0FUpV5k20j2Nuck1GDDb8GNRWB19ko1-JgneE2WCgAd8cqxh8-yxUsmh0C4fkJD95P71TuJdCkTskRN4jWlkqaU4e8es3cSsV2ltfTdyNQIPvZMasMkYTD3KNEpEllzBVQAR0335Ti9kAK6peKXSLG1ZLfRQ8g6j1ONeX-KC-5eLWWh6MmdezpX_JGtRXs_dcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا مدام دچار سردرد میشیم؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/akhbarefori/694865" target="_blank">📅 18:11 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694864">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
ترامپ جنایتکار:اروپا همین حالا موافقت کرده است که مقدار عظیمی از ذخایر انباشته گازوئیل خود را آزاد کند #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/akhbarefori/694864" target="_blank">📅 17:59 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694863">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b17bbb7604.mp4?token=NfomL9bbiPR3m1-PQ5RGdYprhtcofWS70quMYka8L4azpxBkWOPc1fDu1DPanq55vw9G5u5ePFTrBg8R7OCbH5v_QVJbFZt2WySAVhqQ7IXeMerNPa6N05p7Ndh_qAnGG-0gwR6g9Utk-ZjVBiaqQEuXNJo0xKk-n6gPsiyojm8gNThQUEUiYlgq9Ejsbmwo-aZlbbNI7ur0RD1zLa_PQ-qk00gHM1Fyp4BN43wFAVNiAP1wUBaTmisooNjXbbOsxZR78isik2DYgxKMkCNQDtQN0caGMg11tiG-JBdf2qjdSlG9lVn8L-3wbRbx2cNG1BO7kvR4G4ddJoTLpqkMEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b17bbb7604.mp4?token=NfomL9bbiPR3m1-PQ5RGdYprhtcofWS70quMYka8L4azpxBkWOPc1fDu1DPanq55vw9G5u5ePFTrBg8R7OCbH5v_QVJbFZt2WySAVhqQ7IXeMerNPa6N05p7Ndh_qAnGG-0gwR6g9Utk-ZjVBiaqQEuXNJo0xKk-n6gPsiyojm8gNThQUEUiYlgq9Ejsbmwo-aZlbbNI7ur0RD1zLa_PQ-qk00gHM1Fyp4BN43wFAVNiAP1wUBaTmisooNjXbbOsxZR78isik2DYgxKMkCNQDtQN0caGMg11tiG-JBdf2qjdSlG9lVn8L-3wbRbx2cNG1BO7kvR4G4ddJoTLpqkMEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی مرگبار در خاک‌سفید تهران
🔹
گزارش‌های منتشرشده حاکی از آن است که مردی پس از درخواست طلاق همسرش، خانه پدرزنش در خاک‌سفید را به آتش کشیده و در این حادثه خود او و مادر همسرش و دو همسایه جان باخته‌اند؛ همسر و برادر او نیز به‌شدت مصدوم شده‌اند.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/akhbarefori/694863" target="_blank">📅 17:55 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694862">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10f8148314.mp4?token=SsE4fLo7MX3mQcqoCWyVfnjuJ_tpMliWhZyy0yvM-HfgTmwk5E89ioVI-7XVv97_7HEwIqKmmRauSqrc3H102I8L85W-Mzhyy2qdloCoZzKpfDmEs_UNixmdnGavRwkv504yYmbmzOqy_quVntTjwVBsBshtPlp3ei6rakDtRhwl618IUI0IaKt2YR_Vc8_hIl_uauponaN1gjbxlx4SqT-Y_TXQOR8pWb8jwV1JV5zB1BODjDLIYwKC7qeOCOhW3y2KTBfllk1e6Kq_uX6znLxLrLmIASpf7eaH5urZ-tURLg1cMfEbwFe3hFfs9Fvw_A1Je3VaE6thmcMo9i8Z3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10f8148314.mp4?token=SsE4fLo7MX3mQcqoCWyVfnjuJ_tpMliWhZyy0yvM-HfgTmwk5E89ioVI-7XVv97_7HEwIqKmmRauSqrc3H102I8L85W-Mzhyy2qdloCoZzKpfDmEs_UNixmdnGavRwkv504yYmbmzOqy_quVntTjwVBsBshtPlp3ei6rakDtRhwl618IUI0IaKt2YR_Vc8_hIl_uauponaN1gjbxlx4SqT-Y_TXQOR8pWb8jwV1JV5zB1BODjDLIYwKC7qeOCOhW3y2KTBfllk1e6Kq_uX6znLxLrLmIASpf7eaH5urZ-tURLg1cMfEbwFe3hFfs9Fvw_A1Je3VaE6thmcMo9i8Z3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وضعیت این روزهای پایتخت اوکراین
🇺🇦
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/akhbarefori/694862" target="_blank">📅 17:47 · 10 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
