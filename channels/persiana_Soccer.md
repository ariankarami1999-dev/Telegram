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
<img src="https://cdn4.telesco.pe/file/dxqpSRbA1xS9BN8Q3JEwY6Nu9W1COBz_7JWtds_bJfEuHltUyOkbrHLi6ruPanWHZ8_i-UAFJi3KXWPpjhdJIHe2WS3FCtIj3nni1a5owFUQ-SLyfCd5HMPJOOor08fN-RDCXd6shx35kLi4XE2iCkQOstc1r0fU5AlWqkDylXlsPqI5UycDO6Nwjl4EFRw6nt2xAT1R8hV12bL2zcH7A_Gd87ujpXeqNUjojUd7uZsUOF5nWnVTmrACUtPfFEKRhpt_Pj1Jyc2pXyJaf1B37WeyZXDB6RUsuibDvNBT_ZFuB81CpoQSxZxRS5cUC-UaQkqWlMGhMXeQt9YmgjxSAg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 460K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-23 22:34:32</div>
<hr>

<div class="tg-post" id="msg-25708">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u59DIGH5jfYOFKVbSD7FlithfWTbaVn89eDHhrsG_VbFXaiHYDhlk2E1IeXPyi4WRkC0kqLkbl-5Ve9cGOPDs8A5L51uvKVZ1Ut680dqyCkwef2T-bZ6phsgH7_BIEvq43y53oku0icAANAGQmnfprDi97USiMyRJDx0f-xxSMlNwI64T5XbB4mEuBaUG2fkQlwjW8TvsA1BS_6eEFvFiQsLkBVtjBCvAxr2VTlzeoAYrlCdNxYwZhUI9uf-X_c2YWFeuZvK47vJcmwnS6U0hSybzU5P4PmMRWEFH8OJfHxcQbAkXi_ILj-_w1-k14PXLg6e9i-OH03Jh8ZWxhNe2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
با اعلام وکیل اسپانیایی منیر الحدادی؛ این ستاره اسپانیایی به خاطر مسائل خانوادگی "بارداری همسرش" و آرام‌نبودن وضعیت‌منطقه برای جدایی و فسخ قرار دادش با باشگاه استقلال به توافق رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/25708" target="_blank">📅 22:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25707">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JqESK59AIQSqGUQlvn0YCu1GMQWYzhIoTi4PW48LXRtUNsHMQFPPhhpqxbY0jbOFskRKvQbiVk20WmbURFY1TxTShytTtrfTb4rr2oLQszf5oolDuaM-TFuT6YtRX_rrFbDAMwRCa8dyeTb4NnN_kmgQb_FUCjAWMxC-qz3hh2UogE0X3tD69v-OlO6ahyiVZHuN-3oJVUUdJGHyEwFG13e_6doNl7BTOA645WRm6tPLdMxghRmNemmOWbZvUISzBGeg81KswnYdzO8EKCMYufXY8Sg5fo6s6GrPfXLP7e-fXOyAHEwxVm-khNXeC7-22Nj4nn7SY0TA8QISfBBVew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛ شماتیک ترکیب دو تیم ملی اسپانیا
🆚
فرانسه؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/persiana_Soccer/25707" target="_blank">📅 22:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25705">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LrVw6FjPV_GUkuK4wGuOiaR3gK46Pq-Hx3NuI2PhmSuByFddfXL3VP9Qd_vzFXg0HwwT4g77s0azjyh6lPqWsD8DV9VTOKYZPVmTi28QnXHug6ecTJsVi5-_KUV4ntpWSxgtWM1XFzWcLd-kahnEsDBvACeq86ZSo893sG2ImDpnnd67_WPcOBIm-1Co8dKtfEur095hZ8piQMDnCsy8hFJ1cDnetxBcCUWmo7l3FfmoJSXqD4vwbuWqjlarGK02R-3RhdjtaFfi-wAExT0y4DLrEb1qE6IKc3vNnF-wLDiZMvwUr02DemS8YVRq2qAX2Uhmi38DzqmMB2Y-r4NFew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n-zgPegZARH6DWVgXz9UbRTG_Hx_kCKPlYZUmHTit8HDBUQ13vOTztPtlCYVg4tHiYB9Na458Bfwxetacnw2_Ee3-VdnteyRmnG2yX57vxGqiv1EMfU6aTFWPTLWPSFM2uzRz3ntiobWwIbEcMiJhrWygYRh6pFkQPGPRsWWg9_3vXT9VcvK7dZA-il8SqK3_hjGmgo1emeiAdikSXPbYBxY6HpCEPWW7M2vy-zHhMzu8WCFaR4WraVAdieRkQvxk0O6FRgvPW0uwfCtzLm2UudNgN8qK8Qs68T0pw86IOUxkIMgkg1jhEXjm_7YfkPYXooddsh7SOdSHpmLL4aMhg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
خبرنگار معروف‌ شبکه ایتالیایی DAZN که معتقده تیم‌ انگلیس قهرمان جام‌ جهانی میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/persiana_Soccer/25705" target="_blank">📅 22:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25704">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BpQ0aEmAcPgq4-5xhU8gMVmP2XCtC4fN863Zx_HyBbPW66OFnvucLzA3M6bTB4SdVFTkia9XFSuRbhHZPX-XAaKHhwjtNHlBCTqpSTFQz7SR9bFlwBL34Hslx8mghc88hd73t-l2wJIk1il5FpWNJ9AbLguTopk1kW9QC2q2AJYhvig1k0ob9oUqxkYB3swqwJJtx03jFBDZiLBIBycMn-zcHxzgvcdnUobZMwRk1maALqap3hV8-76X83qpg81ujQTRrFyppToqiYo3rZxYGEskNg1UT7CutZ8TrCSaIiS83yY-GeyJZnkUzSPMx6bI_tN1kwN4dDVOrHYVcXOkUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شهاب‌زندی‌‌مدیرعامل‌‌تیم‌نساجی: برای خرید یک بازیکن‌دیگر از روسیه باباشگاهش‌به‌توافق رسیدیم که روی 1.8 میلیون‌دلار این‌بازیکن تهاجمی روبخریم اما خودِ بازیکن حاضر به امضای قرارداد نشد. پدر کسری طاهری به نماینده از خودِ او امضازد و به تیم‌ما اومد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/persiana_Soccer/25704" target="_blank">📅 21:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25703">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iMEXgwPCPw7O-ZskfCZVD8mBLyyd8keHGf7uJp2qp_A6wpHFHaYQ5D9OHpJeCOjSpDKHFwUOkIHAsz-pljjyqJUDqd4LGjy9nP1f-P_aTTMA2zqHhS2ZD3nX5BipTUKitfi-cN1oXFmJdk10nnTSvDDGd5SqbsALHwpVVmJSDzlYNiQ3yvL6zuqW742ctsSumvVzTjYV_eM2pVbqRdI8zvdXLZcwktgwYVXUyKPvHVxupzQjBbCOfMYbDCBgusKjBngTsk_Ag29FdF-mE5P5MhHlqulx07OX0YZsSFvQ6_kCvbvLQhHP6jM8jWNB72XM89XObu2Pt3lOEvSUrOa_gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
طبق‌نتایج‌یک‌نظرسنجی‌درکشور پرتغال، اکثر مردان حذف‌شدن رونالدو ازجام‌جهانی را سخت‌تر از جدایی‌خودشان‌ازپارتنر و کاپلشون توصیف کرده‌اند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/persiana_Soccer/25703" target="_blank">📅 21:57 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25702">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lRXlTxKkcBYkWXPZYM35G9Uxhk_hq2_0_P0oECSQRC0tnBZmuvEd9Env7igLOg-1DRIJeY4N22wcZiY8K-4Q3qa7YZcm-PZS662uipMtNkzrNUs5RAwgzAtl5tVkic3Aa4Ket4_Y02qJMYjYi4vWQoFmGySnyWxaB6cjKjbBfyvuh3DMOqMbp94Wf2OJnNAsQZH_ob264i6lGakkzBJlxOithL5DzEmHZM4bIrmoSqqqseDSqvOYzjfZ_pxulGqurRF8TwAFI8l63IIlDwndBiPpZt13_deQXzpATrIzrI7kxo_1E3OevkbweTk2fs4Jip0qcack5BOl8M4aQmUniw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
۵۰۰ دلار جایزه نقدی + ۱ گیگ اینترنت رایگان!
🎁
🇫🇷
فرانسه
🆚
اسپانیا
🇪🇸
🔥
نیمه‌نهایی جام جهانی ۲۰۲۶
فقط کافیه نتیجه بازی رو
قبل از شروع مسابقه
درست پیش‌بینی کنی.
🏆
۵۰۰ دلار بین تمام پیش‌بینی‌های صحیح بصورت FreeBet تقسیم میشه.
🎁
علاوه بر اون، همه برنده‌ها
۱ گیگ اینترنت یک‌ماهه رایگان
دریافت می‌کنن.
⏳
فرصت ثبت پیش‌بینی محدوده؛ بعد از شروع بازی دیگه امکان شرکت وجود نداره.
👇
همین حالا وارد شو:
https://t.me/betegram_bot?start=p7_r4EF37DCE</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/persiana_Soccer/25702" target="_blank">📅 21:57 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25701">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bbtYseLdWufDRwclDg9ra3j5GDIia5JlODC-NA4B1PU28PLmCLchbNsbPzmMof37kGTm--0LtoIABlZm7Ob6GcpKBX7FS2ekZSSCk8UwZhDgxuA-SrMLDAn8qRDgnIVg9I95DAAGx2nsmHvhFS4yQjLE2fk0q0P64AWO2JcdaZWHDqcCoLxbDAwWe4orUylDwal6pc95RniFlzp5ZIkAPTJhP0G3shZZrteMIhpcqOG5L8xW4kBWSTDXDj7_bXD0-HnXu8nBDhUFzW_A5D5pQ-3u7155_OzSRuJlxoB4iwMbroFErXa1fP3p0FxBxWng5ZZ5ZV4qNMgs5seL8olsuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
با اعلام وکیل اسپانیایی منیر الحدادی؛ این ستاره اسپانیایی به خاطر مسائل خانوادگی "بارداری همسرش" و آرام‌نبودن وضعیت‌منطقه برای جدایی و فسخ قرار دادش با باشگاه استقلال به توافق رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/persiana_Soccer/25701" target="_blank">📅 21:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25700">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RVhN7eUFirKynwpzlxVYTajPrwU7zoQygdYkvLERLfju3tJAXLvnbSUZHPuaE8wsNN_kgnqLXcmwWZYFRAnQhb1N-hUAg5D02cCWEInPbFUI0d4s03S_4pXxHUCMUBoxgREimY-GidUw5CPVwcSbwLE0XEStL83vWJxXhSddGsC-fq_-u47IiXe69SGNBUvdvuZcfcQWqGoTO7_OE0Mehwcv_MNXdJNTPRgQmGQfE8npHSDv2eZ7tJ23m85_DE8J_RBr0kFmjTm4rgXvmTejnnvXhidvaoSN1dgsn12OE1oAQ0vIcLWOXjxedYaoNkg629oYxYSr2kg8rk7gwHT5ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
طبق شنیده‌های رسانه پرشیانا؛ هفته آینده جلسه‌‌ای بین ایگور سرگیف و مدیریت باشگاه پرسپولیس برگزار خواهد شد تا مدیریت‌سرخ‌ها این بازیکن رو برای‌موندن دراین باشگاه برای فصل آینده متقاعد کنند. سرگیف بخاطر مسائل خانوادگی قصد داره فصل جدید رو در لیگ برتر ازبکستان…</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/persiana_Soccer/25700" target="_blank">📅 21:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25699">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PipkfCB69lms6JTPn3-3Rs3GrdtprDN0FRTePGzhkiZm5IdkXjPiSw4iI7PKQp8fgDL94FKvVEwQyJr9aAAh2AqDHg0nGeGLEpvpjRJE1xYnP2VK_QHEp7kIxGuX6_YDS2l4bjBoBrbJA03_uPcJ706CRfTXX_cJVbcML1RWeYbRjHoWduwwoLim1mG9lc1Mlx5izEtyD9vq6SR78pLxh8WJvYvKu5j7znJ3viF3iW9LZ3kDwOeGVGaVgrfevAVt79NVAlWODrEQHkhcjNz24XD-T7imLhzOeVthlyWEn4gexpq7_HuCaHar5kCmhy4EqBpXq769TqY2zUM9Mt9_xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛ آخرین پیغام منیر الحدادی به مدیران باشگاه استقلال: وضعیت منطقه آرام باشد این هفته به ایران باز خواهم گشت امادرغیر اینصورت باتوجه به شرایط خاص همسر و به‌دنیا اومدن فرزندم نمیتونم باهاتون کار کنم و ازای فسخ قراردادم مبلغی برای شما واریز…</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/persiana_Soccer/25699" target="_blank">📅 21:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25698">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b34e61019.mp4?token=ius6dyI5YG4Kma4kEDRt8KHKgToBb0WlLz2ZX1alrtR8G7iz48lf38qooosznVM2kRr0iSr5GUkVVkTKmBK9fPtPa4ScMyWSyMl71pAz0ICMDkiem9We3U-Iaupr7rIJ8w3wG2bxsW_Qt7msUvHURzLv8F7wDyxdwnbia5fFB3YzFII1-joyxto0Ff3sXkR8k8BuAxvFWSXuMsK8xIjmztnl7ssdcTtp5t7x5c4MSuhab-fsCvTrP4SreJ11H-q8rIXUBYiHktSK9k0QIBiCMZI6Ql6DjgEJ-7tzYHvuCtjIw7_mlPqvImBsp_pp07c7Isfd9ETkNiu2ai5uZ8s67Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b34e61019.mp4?token=ius6dyI5YG4Kma4kEDRt8KHKgToBb0WlLz2ZX1alrtR8G7iz48lf38qooosznVM2kRr0iSr5GUkVVkTKmBK9fPtPa4ScMyWSyMl71pAz0ICMDkiem9We3U-Iaupr7rIJ8w3wG2bxsW_Qt7msUvHURzLv8F7wDyxdwnbia5fFB3YzFII1-joyxto0Ff3sXkR8k8BuAxvFWSXuMsK8xIjmztnl7ssdcTtp5t7x5c4MSuhab-fsCvTrP4SreJ11H-q8rIXUBYiHktSK9k0QIBiCMZI6Ql6DjgEJ-7tzYHvuCtjIw7_mlPqvImBsp_pp07c7Isfd9ETkNiu2ai5uZ8s67Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇧🇪
خرید خوب‌کریک‌برای‌شیاطین‌سرخ؛ یوری تیلمانس ستاره 29 ساله تیم ملی بلژیک با عقد قرار دادی چهار ساله رسما به منچستریونایتد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/persiana_Soccer/25698" target="_blank">📅 21:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25697">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/obzQKmNs1eJ4LbI0Q4o0S3ybfDKY79dzELtiXC3nQw-km5B3AO_3Ov57iV-VS3mEIwpH_4GDXYGpzpNCI4jd-kd4Vg7h5jH6dALlaIaU-lvD_VcUye4XVSRcZx2F76hL3zxw0q8Bp5ivz0fztf1J2PTFIOV7JQAQNsc2r8a2BwRVOjodT9NMeRuYhMOdp9gY-UAHyYANc7csJMk-absBkRuJ7bpHcvC1quo-IHou8jZwr1t_KnZFT0q-QzJZ6eguiPLX6VuEnptaY8NNKZb11D0Jgr2xLK3bC8ykObpsvsTbMuU9Tm2VSsp4hw17wz-_3633WJvu9A_hsoF0wOryxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛پوریا لطیفی‌فر ستاره‌جوان گل گهر امروز از سیدمهدی‌رحمتی‌بابت موافقتش باجدایی از این‌تیم‌ و پیوستن به پرسپولیس تشکر کرده‌. همانطور که‌درروزهای اخیر نیزخبردادیم تمام توافقات بین سه طرف انجام شده و به احتمال زیاد این انتقال بزودی انجام خواهد شد و لطیفی‌فر…</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/persiana_Soccer/25697" target="_blank">📅 20:57 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25695">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HH48wKDkQvtoQ6g5k3YM5XGypYCiPRfk2UuX8lVDMvIskCFY8_L-sgu9JflJkQMd6H2C6lOLSftFgr4O2iLzRcNFW0Q0b9NA4wqZI5aA8x6oeOaQb4sIzCqA57aiVqmIsEioexDUGJ57DIxuQFJvI7-zw7zNUZYCAK_TChPuoUX8OmJbJuL1gVlz75bxFnGhwIy_KtapkWdR0JDqMPN3kd4gJ6N9HqMxS0eeep1o1HpV1SZq1PlwOc7BOgO1wSIdnYVJ2g7-E4ILoEDFkbdwdzdTjo51EodqQcaapxZRn9uaZvrg7VBnEwBEovXpf55ZWfUpREg9D8OosCHXrcyfSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oh951LdfyGgH_bVXE2_IT8jfRngrt9IxEQE_ml5z7TWXf7Fo19NWUJ19e9LzbgmKiY6erJxmkip5ctU3892Ms6D74Lqr8ekUfoGb3Z-ba8TNAnBytBHjoNsUCBxwvTWprZfcfz2gubVvLYO8aoncfpDkcnvxJSjn2aWXrKvNAiCcRBRb-mH89X1UF1vc96OOo-vYkXOIxsOpZ9edTU5ElcuuvjdvRvYB-wTsuVaRCv9LCHyU6k4tmVOsYmleEPgbVhdNfi5bcfsPhejOVkK_0UBvevuQTp9pzLqahNw76RYgGI-MmWjgHbPhJDSQ8zVxDZfH0UjJezGkeR9WpuNaRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛
شماتیک ترکیب دو تیم ملی اسپانیا
🆚
فرانسه؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/persiana_Soccer/25695" target="_blank">📅 20:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25694">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MQ4VuuJX86IZnwDx_gNlrVNs8XwWlCiDQbnydpKTYslzDNBv34gFa5_s7LilvIvrIPYzJIXgDdzDms4oVO0yb8eeb_sa-ed57pxgNwt44vz44y613YnBrnGfHSHNzMk8l0VsHHRoRxJt9068PgwQlG6yZDM4Ef4wRyx7iOsIxQrwu2HxZI3gIzZ3XNo-iMfl_TeFdbRfaFWcmZvTnSmHp4MeY4YhePHl4zWY68yOMMuli4lR-TpnyV7-LjfON6y3-_CHB6Vsv90UDkddo2TCcvYXMheclzstW34uq3KKrHqiDwy7h5qioZYtN2m2sK6_2fWTXtcIzT5ByCPQDzlK6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
کمیته‌داوران‌فیفا پس فردا عملکرد نامزدهای قضاوت فینال‌جام‌جهانی رو برسی میکنه و به گزینه نهایی دست‌پیدامیکنند. علی آقای فغانی در این جام جهانی سه‌بازی‌قضاوت کرد که به بهترین شکل ممکن هرسه بازی رو در آورد. یه کوچولو شانس باهاش یار باشه قطعا فینالم بهش میرسه.…</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/25694" target="_blank">📅 20:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25693">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eimQIYOmGkepOjYDH3rSdreqrhsnP52Ag3Eue66moK8nbioYst21x4daNXJ1pawMFpP2TBKrpGTsKrdqiljmrC-yJszobOlPrmH06r38whEUT6X9bB0uHVJoqeLd1F2g70LjiXnnb4rzWVr3bUi8EwVvlXM1Fw81MCMCQpQxWIBp-x7GZsFiWmaSjT8WPb9W1uo4lUBjVGAiSPQ3P5FAzUbf-FZ6u9VYGgum6oyXrymGrY0jI9IUw5P7mFPDN6WVe_5J9BkB7_QjBayGoYA2j7KdCdhPmLb9Y1Kj9nV3scsg8AY-uDSjwjl6DCkw9jk9Wu34EUv6m3gGheQmSlmLwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق پیگیری‌های پرشیانا؛ یاسر آسانی به باشگاه استقلال قول‌داده که از شنبه هفته آینده به تمرینات آبی‌ها اضافه‌شود. خانواده او علی الخصوص همسرش از وقوع جنگ احتمالی بین ایران و آمریکا بشدت نگرانه و مدیریت باشگاه با او صحبت کرده که خطری آسانی روتهدیدنمیکنه.…</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/25693" target="_blank">📅 20:24 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25692">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e-sfXlVuZQoodC7-z6i8qlQtP9DC-eu1k_VUW1R7wCEFtlvd-vFuyDJfUnRminFJq9osPTBGFUPiw8lJLqzC5pKBAZJrzgk3g6pgn_gdobCzTNPaaJA_JlalrDYe0cnvbh9yJICiMuW0Kh6q4sjldEKJXijE6W0nIDEcclNp5beDou3R_VDrV-93t3jlq16-rdGGSOoPfnJXwb5kDck2PzUcejiIt9T9QQuZ8Dr9eV0yWzwmnqnmbLFX-UyKx62gUBx-Lp9Fwpc8rDD16qbBsy0i5yqfIw9-1nuUIUJGKqpCiGpTmdMMD51YvhJTRKdx5HRH-PrZFuuc4UDro_mPQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
👤
یاسر آسانی ستاره استقلال ساعتی قبل با ارسال نامه ای به مدیریت آبی‌ها خبر از فسخ قرار دادش با این‌تیم بدلیل عدم پرداخت مطالباتش داد.
❌
مدیربرنامه‌آسانی: باشگاه هیچ‌علاقه‌ای به ادامه همکاری دو طرفه نداشت و از قصد مطالبات آسانی رو پرداخت نکرده تا او قراردادس…</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/25692" target="_blank">📅 20:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25691">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YAqpsYOtATHNO_827NeugGBupsR5O4CTmrQgo1G-hyCUyKj0gJPZW8Au0xytNEodIsYplY2UxzWnLfeH1Ro5ulKi9aELG037kEhOIMocWi6vVGyzr6EYZD0qs8bWE2Lz2bvMCC_so3t3rZ0-2oRJju_a1rtZwROvzGOE6Em7g5opGE6efinfbX15VEZ2piDS_F4AUQV-WLfdJLbESqHEdBz9vbNmQExQ87m_MgTfqyT-7LvtJEhox7mZVUHCRKDnlc_10lSl2hIg9SV_I5d6f8vJgyYanIgRyURokr_n7Wc7d44tehg_gJF1buDZB07yBDjNKN5SWkj1WKYcTcIT5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رئیس‌هیات‌مدیره‌باشگاه استقلال: یاسر آسانی و منیر الحدادی با باشگاه استقلال قرارداد دارند و به ما قول دادند هفته اینده به ایران برگردند. امیدواریم به قراردادشون پایبند باشند و آن‌ها رو داشته باشیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/25691" target="_blank">📅 20:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25690">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">آخرین‌آرزویی‌که مادر عمو پورنگ داشت. فقط اونجا که میگه بالاخره‌آوردمت. عمو شما بلیت بهشت رو با همین نوکری کردن مادرت گرفتی خدا بهت صبر بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/25690" target="_blank">📅 19:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25689">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZe-7RHbIs1eioaF4FceFIfTZNpZgLEljG483O--oTJuZPnZ4MfoCbyHXX8ThLeqWPjnj75UryIxDndoHrwmcpdvlTxWGgxwO2DS8IpLawkKRD7-Vdlm0FFu9oXaUST3fMFVlyS05iNl2-joTyYP97Wl_T1bTV_tAsuUFaT4cs47otPCYtUKbAU1ESjR8zQlF5U2cJVU600V11GMuOzfCT_M1eJouUBDUIZI80YZYS3kVURH6XiD9NhW1WfxoVPa-oM91wVHh4sxEHyzvYF38u10h8FvRIgisxGKXncwPEfRrietTK9SGmIjLzHu2u8mI3k3PvRh7hAD30tiBBnRYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
عزیزم این نیمه‌نهایی جام‌جهانیه خیلی مهم تر از چیزیه که فکرش رو میکنی؛ نمیتونم جلو اسپانیا از عمد بد بازی کنم چون کشور توعه:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/25689" target="_blank">📅 19:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25687">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ONoG5C_v9zg2V6A41jbnPzvTUmuLxa2nesE18NR6T_JP7ESiJCuxDby477nqta7ZcM-wXKC1YbQnwxdafVusxZC4yhC3dblrfDYjHwy5as4OiKJljOZeyI55I4uTTa0-QrI8nnJletAXqnaroF7AhFyu6R9WpraNiqgZ4ShMdTSs7e9WH3386H2PzUJ_cVwJQpsYdwVpPX1ip9jfopRfimi_2EgM4wrYBs5e8oqhJGVdgk_w00LUKaecXK48vUGLaErBpEWPIbNcv1RXiUaSdJ1LauQyW028-CtXgJijauSA8QeTQSGXpZHuFurzTgmuIK8dfMsJW0GY_vvb4M1dGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B8vbCiihuY_cUM4ffYa0bPQEaB8x7j8hg0xusaf9h7FeSXbjPfdYU1MqgVmQy2huE4-F31JVII6fvS9ShwRPC7r9K45foeQ62wCv38pPer-pNpRgIPcb28jQlVVYdEXpUIYaru29veIZooXpgSLUJtGbuTfqK0CrArLNCnDFKgbQ15TWRZRC3Q6Z72cWpA8PcHtRgL5rZA0cJ_0CF2sAAqc2mGfs70tOibd9UOr218LpnFvkI4XpQpsYtpgOn1afp0phC71vBRvWnsliZbSKCYdVD_W-cZmlNuZ7VYGRAT5VOx_etyIq77jAtGoEV8yb4f9fp6oCH6l7w2dmAnf6qw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏐
برنامه‌دیدارهای روز 24 تیر لیگ ملت‌های والیبال؛ هفته سوم لیگ ملت‌ها از فردا شروع خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/25687" target="_blank">📅 19:35 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25686">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sGCpvVZok_FztYJ43Tq_JVa8-oTNCPtKH2BxtMIRQ3dyfBYJR5etSONYEniT-ztYIwcNbY3CsqnzYtBfa2030LmmGrdZVF4CsGI5liDnloZwaHbaGg-toaOf0k7TovjUozhdcpMc3OjuxuaGLYCijLCfZe8FzotLIh9zEib0QgUFLm-nw-8Y3JUJ-bz7IhAu7naff1R8MxP_GD2LTuXxFZTZLua6LerM6f8590KZgU2-QC6pMVytVTs_UOnjvt2guw-Ab82Sv80GB9B5ZzG945g1Exjx5yTAopOYS0eTgc8shFpV9hGmmGSXobnQ2o-3Fziebso2kCPRUZvl7mEBFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛ با جذب مجتبی فخریان سیدمهدی رحمتی موافقت خود را با فروش پوریا لطیفی فر به پرسپولیس با رقم 600 هزار دلار به‌مدیران تیم گل گهر سیرجان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/25686" target="_blank">📅 19:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25685">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BYzCm-Gff4UbFbKd_EXn7Sz_bhrswI2UX5jbUiEK-f_rdFX9xQ_TIqGegNHKEeGaZcQ_y6OA0-ID4SZDA_J-e29OUeGO3rMwJdL4M-SAAGZASiQLvWiFGG0Rg2mQKm0vFlSlQycMdXptahATgzTd7hPIMtrN5bD9FFq3sKLmwFMyTXC_LNmJQ-RmnDE1RNPwOtA0mc48irpWg56a4GDj9FMmZwrYS3erm8xBLx2eczuthFDIxUS5YYKjocd5VR4SJoepQ-P3gkq3fvDfoD35e_ss39paZBHuIMIuTzrusRbMTpXyPepNkF7tINB93UMEbIWhWs6045WR-LwPtziKzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی‌پرشیانا؛باشگاه‌استقلال علاوه‌ بر پین؛ با یک‌مربی اسپانیایی که بالاترین مدرک مربیگری اروپا رو داره در حال انجام مذاکرات نهایی است و به احتمال بسیار زیاد با او قرارداد امضا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/25685" target="_blank">📅 19:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25683">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M6cxROF32YOiorVKKno5WmRT_T8XeLdVe2vMF__Ra21PIVHT9VgYNfGBfRyQ1tmoyqOKl7Fu_mSlKAQyebmzlpisiDKgfLUW-JIQ2HFAICZBsPiLZ1ee2uUtcC1qmUXM276PHfsbe72IBElUQXDYPzjggaLoIfyZsFTIHMuMnVb1u6Lsx-bp-55p0XSul1q-eeG-GcA1hbHOqFcYcukvtoJoutfF1qev2A3uDRGfuf5AS9Td4-FCalikRsORqYaT38TA89guJ8zNfGjfxcUjmXCQl_ttGYG_k4zXhYKpAmtVQ6SjLI4jy5SDKjZLuR5o0JaaLOJV5HHsyzj2ItsTLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eo2ENMGups1Z7nf2h822ojfdArOAI3ISQYOYvk1Pf_x10AqU2blIwL_Ui5Kt7g0sm5SjyOi0S93uM2lgDQo_XlCLKDf1uv7eawX3GqtZYy4Pr4bV1tCeVaeDVp2SEVPdzuBYi2s0QfzHfMxU9yb9DElchnDCNXiRRfMSDgpV46HCICgA41oVPtphzoaCfHqdD3hmraH_oOHjJN0Jr7vTwjvsAWPt4tf_H-4TPcAxUQYBkwWyXF9k-soAFCBTkXwMTwWk2uT0YGFi0S7C9qEyTbi8hOWQ4Orz6ozWDmdkrPoDMuCr_k7TZDnfX-Z1B6BNGdbXvyUdnvckdCrW765Ngg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇫🇷
عزیزم این نیمه‌نهایی جام‌جهانیه خیلی مهم تر از چیزیه که فکرش رو میکنی؛ نمیتونم جلو اسپانیا از عمد بد بازی کنم چون کشور توعه:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/25683" target="_blank">📅 18:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25682">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🏆
40 سال پیش، بازی انگلیس و آرژانتین یک چهارم نهایی جام جهانی 1986 گل دست خدا و گل قرن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/25682" target="_blank">📅 18:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25681">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pq-Bo1CfK-9Vw7NWEinnvnnrvR7-2M39V4BoCHyZLKj_PG8WljmUIT_xbZ6lILGuUF99csQTHSAUOQPH4a2Ib53dmKD1LBlHAOkl3Z_887MCE7KP8NTpgvNT4F8UMW5p591kb9CH_9EdcwB9dfuRDtl9hjMKlNgyFt_Fh8_PK9V2s973-7bABhdLYplHIUGMwX7WkQWUXHB5A6zvbl7kFCRMdbsZOCQhtSpimK-l9L_kukd9bgMuSWrdov-vchbwWBBVyQG9hD-XnHuP8iIG-qooLJhF1wASFwR-eiixnqi9sN7TTPgnR8qH8V1n96odn9uPZkpXUA1VjYqWOUhlaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
در انتظار دو دیدار در نیمه نهایی جام جهانی
🕐
فرانسه
🆚
اسپانیا؛سه‌شنبه 23 تیرماه؛ 22:30
🕐
انگلیس
🆚
آرژانتین؛ چهارشنبه 24 تیر؛ 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/25681" target="_blank">📅 18:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25680">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uCvi9xg4xeLltkf9YePO9Ec-s877JD2-pOrJkVTS9BJjToK754_IPpCLbyS_SBsLjyrqlZQyWfMr-wncx1jivK3ESKq62yNUS_Cx4Oumy62SveK1bvBqUl2f8PsxbqUdjvI2miE3kZne1wUzfXH87Hzk5Et92x9E0Ur1uyk5oQ3fdPoVILqfaU62P-gCs1_KvfIl47DHpdX8CSYPHG8yJWLohLGsdtPir6L_WsuDviWnMj0wW2vrYCXMUZISchqGrmie6gtDV3Vx63Y5lEsa8onXA0aiuLok7mfjQIa53FqaGmAWt825diKTS474-G15g6CB4_BFioSe7AoaQ3Z-gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
🔴
🔵
#اختصاصی‌پرشیانا #فوری؛ باشگاه خیبر خرم‌ آباد رقم رضایت نامه مسعود محبی مدافع جوان این تیم رو 350 هزار دلار اعلام کرده است. یه چیزی حدود 65 میلیارد تومان. دو باشگاه استقلال و پرسپولیس به دنبال جذب این بازیکن جوان هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/25680" target="_blank">📅 18:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25679">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GtZKSmmBAb36WnoEdObz4jy4ah7AHR7wt5fVBzqVuysVrN170WxLiZBnu4uEHunjhMlOu8i8p-88CImQvRraDIxlvKdoYwsZHdkwRD4EdB5vDC_cpEEl4eM2DHKkOPeqkIpYzqe-DOOwzWdFCISxBJN0MoS5c_GHeiG3ddB7pknDy-OHAy-eVPrSoXFyaYwTQ78NmgNB3rzqEVo1RHG5Ak2QL7xms-ck9ZAJVdE9B5pH0w7OIjLAb9ntZKc6wMry_xcjqTAI64f0VL79XGfNrlKTTtBYeFjEOX8xGPqV3cS47ezXx5vBOZkev2gMyCznpxzhB8PvmPv5StYg_imaPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری #تکمیلی؛ آغاز مذاکرات سرخپوشان با ستاره سابق برایتون!
🔴
بعداز صحبت‌های شب‌گذشته علیرضا جهانبخش در فوتبال برتر؛ صبح امروز پیمان حدادی مدیرعامل باشگاه پرسپولیس با کاپیتان 33 ساله تیم ملی ایران و مدیربرنامه‌هاش تماس‌گرفته و پیشنهاد مالی…</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/persiana_Soccer/25679" target="_blank">📅 17:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25678">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g0mGgrbY3t1DIJ-MdKR6mVYN7as0LeejIsYmWmd4UCzrGdR3O8uc5LUQvx2xG9Eu-PutnBSYnUofhs1RnDHQVSvQioa7OIDc68aMtc6WKCoDcjIei0wKe23DPz6xOT_P9gj54R4m8u7v2ak4_cGf4icHbS5jBBJpsdCy9-vpnEuBE8MJTVSgXgtWMxTBijSxlHziC7gVj3nNHzICP973GPRCrPweF2txfZY8Ai6qo_4Dp9xoA-NOfYNC3r3NdBuWwhnTx76KXA7An7p2teLxppma7IJjuet8HQuvLxdZCChOTPlimJATdWYr-nDyEoBukHXRgmcrd25zQifoAQblCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
👤
علیرضاجهانبخش کاپیتان 32 ساله تیم ملی: تا یکی دو هفته آینده از باشگاه جدیدم رونمایی میکنیم‌. اگه‌ایران‌بیام بین استقلال و پرسپولیس یکی روانتخاب میکنم که از همین حالا انتخابم رو از بین این‌دو تیم کردم اما همچنان دوس دارم اروپا باشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/persiana_Soccer/25678" target="_blank">📅 17:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25677">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p-1rMzDsH669EIrd2mk7P1mwpKBnBPsGh6FWaSWU94nzNKPNFLpx7CchC9dLV3zIiMVGBlfi6rboXraBTKSzC_RrnObDf__j0lzyfUVJo8aG_kGB_04S7B0HeQFmQ4GSHNsnLYVgP2Nyh3jSZC9GUwM551wGVAwawU8_mjOonFlsbuxUALqTrNhTBqpC6JAGBJcDR9IILF7YOLK2H0a-7GjAHt2n0AUpA_R-px7OCFQpAPRE9whSuxOFAZW22DwIGYm_E8rJr48qzUEUdpZpY7solG4_5AtuODnuM-Tv3MUFmVsUONwyYTRs1YIl_gh4-I65cQxz38b94GawnBtjcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مسی، نیمار، رونالدو و هالند اگه دختر بودن:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/persiana_Soccer/25677" target="_blank">📅 17:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25676">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bTV4dROefUiO0u7oOWWL1KF7P76ByP9LgMzg6iEA1hYZ6Lbx_Qe2offr5JjaxTZ0O8AWru7Uw3b0be3eNahf_XC_2Wzyn8JHbWpJlSUaABV2h3nmCOMPdO2gQA6ylS58DnXH4rLC8qhDaIi3YMGZLiEmZDXz7dgKh7h8asOv2cf7Od29pXVGIAspqChOd7j0OI8VrGJqTkyu6uo5LDOgEFwDBcbynIVX51U0naPDahfNHjGgWHv0oNuv_FChusz1tN3S1jWD1t4JDjCpS4KYsu-EyMGj3-Zp4_RLu38fiRWBMIupauCd-mXXCMid45VBwkd6v2v34mDqZ50VpvnVwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد... علی کریمی هافبک سابق استقلال با عقد قراردادی 1.5+1 ساله به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25676" target="_blank">📅 17:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25675">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBJWSR-yAJCxhKtEb-PCKYCu126syHB7B1LBa0EVomKAotZ3WNli4SjKtqfkC5vijqMinGmwGlhyM8CC-aINO-uSGz99Y5129ryf-AO4W5cq9jufIG47ueJX99y03KSbD4Re7i38iVoP2TBPpov-gkGhBvm2eUfBmdaR721NJpI-wBf77RYcwsEEihcJ58-MXvW09Mjc5ryQ34cJ6kbj85wTBrwWN-DT5laYtNUiJsrUo2V6Owz_ux15791VSxLHrGQduaEkm5ipPCnODYMzSVdeGw_bqSo6ZDLYzQo9T9Wnl6SUyYJooRN4OsasuuPRhTuZbjjEWeN7S367dIrT3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق پیگیری‌های پرشیانا؛ یاسر آسانی به باشگاه استقلال قول‌داده که از شنبه هفته آینده به تمرینات آبی‌ها اضافه‌شود. خانواده او علی الخصوص همسرش از وقوع جنگ احتمالی بین ایران و آمریکا بشدت نگرانه و مدیریت باشگاه با او صحبت کرده که خطری آسانی روتهدیدنمیکنه.…</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/25675" target="_blank">📅 17:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25674">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0znaSXysMmU5hTNAomq9Y_W8Ao7jNN7xoTMmm3GC-Mu1it2l-rxkiHCS4us75IOGv5nlA5GEkTYFXhSu-9hQfOv2tKrta5zmZs5ArJQ-Pi14s8my1vJ-OPQysUeZTI_F0mMB5zzh5hbpHocSG3TqdgImHCRP5MFeeHhfdNBHj5k9LYVpBjyiq_YQvQwJ9Vyb2W_glffYLzxG6sycy_SEFgQD4OeVz9v8gb3aZsKOL-omcIjpk4AUWd5kuoYR5VoO7vLLxrueXn6D_exbMqBGvqWDv2y3lZn1p9HbkoSO1kT8FUjMEnh22rnV9TTQOPR9lxnc0zpRzbUh9Wdw1t6tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
آندرس اینیستا اسطوره فوتبال اسپانیا و باشگاه بارسلونا مهمان امشب برنامه عادل فردوسی‌پور.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/25674" target="_blank">📅 17:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25673">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aeff2dd56.mp4?token=Zuc-4Apwc8w9gVyfbpIH5UQYL9R9tknWth5Pcu0YF47moFKsE9dD8YDUWe1PrYLIum0uweKWfTrgHZhcTMrXp0bB52gNFT2z5znzOSF4o1kT992RISTBEKGOUjGLRMkrCSIjtqqpZgipg0YZTKliT9xee3AjO3Ti0f1TeWUpLX5uCO5h8ZSM6C8pTF5o5aawCeZL8Pmbc4FUV4sh2tM4jC7fEjhE62rhDQEuEAbUDK5W1Gtvucwe3MWyFQDo4_Ot5-Qm0OxDwnUCbDmcAf4f47KAnCoC7twUA2-M58DcZ6thutW3Lm8ye8wdea1K3g266DBZpsp_--gUFm-Cq_hymw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aeff2dd56.mp4?token=Zuc-4Apwc8w9gVyfbpIH5UQYL9R9tknWth5Pcu0YF47moFKsE9dD8YDUWe1PrYLIum0uweKWfTrgHZhcTMrXp0bB52gNFT2z5znzOSF4o1kT992RISTBEKGOUjGLRMkrCSIjtqqpZgipg0YZTKliT9xee3AjO3Ti0f1TeWUpLX5uCO5h8ZSM6C8pTF5o5aawCeZL8Pmbc4FUV4sh2tM4jC7fEjhE62rhDQEuEAbUDK5W1Gtvucwe3MWyFQDo4_Ot5-Qm0OxDwnUCbDmcAf4f47KAnCoC7twUA2-M58DcZ6thutW3Lm8ye8wdea1K3g266DBZpsp_--gUFm-Cq_hymw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛طبق‌اخبار دریافتی پرشیانا؛ اگر اوضاع منطقه آرام باشد در جام ملت‌ های آسیا سرمربی خارجی روی نیمکت تیم ایران خواهد نشست. با امیر قلعه نویی قطع همکاری خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/25673" target="_blank">📅 14:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25672">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YeCY7yzELLfWhYa1L8cBls2uT7yWFCTOHTzTgqYoflT18dSdLMbE0BSe6NDvnkhvqvGBcDAwKJR--EXQiMVAKqW6Clc2Su-0Eh3CzRmyHSbHcWqjZBzI2oKwTj7PWBb6-9amSDdOp0apf0p-4NlWAv2KprnOqzfdJ2tyr6cSU-Hm2r6Ck_sI8iV9vCIIp9_6c6GGfFD-5z_zGbJOpxAzbObZ0oauFCkHWW-QeUO0QjXrd0wBw0ysdwHt7tbpmyRjftJZAFeMGSesBAMv5zC9qXitrGYYO3PRE6RnmvwI-iN-MTWq3CbY1urCTzTD3tphy8wiHnyyURgU4j4ZABNbuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#فوری؛فرناندو پولو خبرنگارمعتبر اسپانیایی: بارسایی‌ها یه‌فرصت 72ساعته به اتلتیکو برای خرید خولیان آلوارز به ارزش 100 میلیون یورو داده است و سران اتلتیکو رو تحت فشار قرارداده تا زودتر این انتقال انجام شود. آلوارز به اتلتیکو اعلام کرده تحت هیچ شرایطی فصل آینده…</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25672" target="_blank">📅 14:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25671">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bc72012ce.mp4?token=uesQdjV1W0msJ5AMVwf0I5R5G_AadY_aA5qA2rMAI8UJYnHWJDUJIu8qRBegiJDOWUE97QNC9oaSVPRCZELEmmQ76ol1BNAVPm9ArvlxqM2-8L6WIiHMFqFiwDIDUVKUONBaNlreEmNPp_Lhjs3FxYZbMRWyWAl8ezTUuC6dgc5pRR-CkzgrwwhCN82fgsB-i7d4F9ftVgf_M_j4EyNuAYtmfWo-sk4Qz-VkFdYT3yHdF037uHFTwgXW3RkXLTFGwRSB_cxhLcl7oXGIeNH4mgyr3Zgoal7V5ph1nKkQ439kwFiMQDaHAgofbuFjLsdHx8pDBjN_gV_Gb9Y5d9MxEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bc72012ce.mp4?token=uesQdjV1W0msJ5AMVwf0I5R5G_AadY_aA5qA2rMAI8UJYnHWJDUJIu8qRBegiJDOWUE97QNC9oaSVPRCZELEmmQ76ol1BNAVPm9ArvlxqM2-8L6WIiHMFqFiwDIDUVKUONBaNlreEmNPp_Lhjs3FxYZbMRWyWAl8ezTUuC6dgc5pRR-CkzgrwwhCN82fgsB-i7d4F9ftVgf_M_j4EyNuAYtmfWo-sk4Qz-VkFdYT3yHdF037uHFTwgXW3RkXLTFGwRSB_cxhLcl7oXGIeNH4mgyr3Zgoal7V5ph1nKkQ439kwFiMQDaHAgofbuFjLsdHx8pDBjN_gV_Gb9Y5d9MxEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
کریم باقری اسطوره‌باشگاه پرسپولیس:
تو عیدها و مناسبت‌ها هرکسی بهم پیام بده جوابش رو میدم. اصلا برام‌فرقی نمیکنه طرف روبشناسم یا نه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/25671" target="_blank">📅 14:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25670">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb91ba980d.mp4?token=P9ijkgYwO2VT0eKcAl1Qm6CuM--sUuYQjI-NMLxrPQlIs8GvQgSR_9jhBHikI_gav_cdBjGVP6iNydX6gjhqfORP4HbTZZTqh-N-KR-2qT1b2yzz8AQ0NIfAujNfAmvU9ld5k3qw34sD-w_eslAqs9DzpiX8n707pJmvMBSnVM4jyTEA8vOkHuw2LcHguEPBA0jcKphQnzHE3vcm-JqE-NY3729789pUZSi37nUBn-IX1V6VWr95HpKv1G9H1IKEczxComMNPJjAEVtatpr61G5Pvpx89tlE2l_yEzLx4xlmkcp079vlH5HDe24kKVwxPUAvuD8SoN0P-KStN2YRu25EiJ6-GkPNsTLDFvXCBlA_a71pXS8V_Osz0RvhziO-a1b0kxFcYkTo7OvSb2hKMqSrXRQ7km6sEg4AbD7rMHnhvh9GMQHR-sDvkg38Y3io648eXSpxOXvYeyPBX9_S3fkfSZ8b2xCp894cyhV5ZY6bFzhFv3q8C3SnXYbb1WghIsm_vyphPlBJ5Ky0GQkywDedgpUt1k0dfzcSNhC7BIvoxCG-cHRwlAjEuOlAHFkgi1cmnUNV0N8uZNMRFrbHLN0vHdNRQovs9klpG3JxfajUKFD_3VauGOcHL5ptnUv39wdQc8kcLb9th4eitI-Wy5AjwlaXUJGPYrpSRxqGz5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb91ba980d.mp4?token=P9ijkgYwO2VT0eKcAl1Qm6CuM--sUuYQjI-NMLxrPQlIs8GvQgSR_9jhBHikI_gav_cdBjGVP6iNydX6gjhqfORP4HbTZZTqh-N-KR-2qT1b2yzz8AQ0NIfAujNfAmvU9ld5k3qw34sD-w_eslAqs9DzpiX8n707pJmvMBSnVM4jyTEA8vOkHuw2LcHguEPBA0jcKphQnzHE3vcm-JqE-NY3729789pUZSi37nUBn-IX1V6VWr95HpKv1G9H1IKEczxComMNPJjAEVtatpr61G5Pvpx89tlE2l_yEzLx4xlmkcp079vlH5HDe24kKVwxPUAvuD8SoN0P-KStN2YRu25EiJ6-GkPNsTLDFvXCBlA_a71pXS8V_Osz0RvhziO-a1b0kxFcYkTo7OvSb2hKMqSrXRQ7km6sEg4AbD7rMHnhvh9GMQHR-sDvkg38Y3io648eXSpxOXvYeyPBX9_S3fkfSZ8b2xCp894cyhV5ZY6bFzhFv3q8C3SnXYbb1WghIsm_vyphPlBJ5Ky0GQkywDedgpUt1k0dfzcSNhC7BIvoxCG-cHRwlAjEuOlAHFkgi1cmnUNV0N8uZNMRFrbHLN0vHdNRQovs9klpG3JxfajUKFD_3VauGOcHL5ptnUv39wdQc8kcLb9th4eitI-Wy5AjwlaXUJGPYrpSRxqGz5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
رونمایی‌جالب‌از شباهت مربیگری پپ گواردیولا و فیروزخان‌کریمی دربرنامه‌جام‌جهانی شبکه جم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/25670" target="_blank">📅 14:02 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25669">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e-g_760eFBS4glTmHdN1V6JBV9b-vUt36D9sW4kOuml-lrcuBw_jT91NFZy3D3z4vXW_eO_AjsbAMHAlqV_as639xtlRABgACnIu5T0AFugtKmis9wsPTF8NDqr4oT7PYl98E3xB7GBnARnK2_8J_glULzrQxjqGVt_5HiPPTcjVrvcfHUZ_67liX5Gv3r4l8qste4dYYLkweeoMHqFh1avdO68xjqP6HSlfNgZHoeo5BuuA3pmAMecR0rRd8FnElc8XhBKmONKrcL4QXHBKrsa48qKOSzALzyxL06Dx_Z8RvZQvci2ftlDRx_3Hqwt0_TUBgAGo1wUXPFrRWSC3Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
‼️
کرک و پرتون بریزه
؛ رئیس فدراسیون فوتبال سنگال گفته که: من‌اعتراف‌میکنم که بعد از حدود 10 سال متوجه‌شدیم‌پزشکی‌که همراه تیم ملی بود، اصلاً پزشک‌ورزشی نبود؛ بلکه متخصص زنان و زایمان بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/25669" target="_blank">📅 13:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25668">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd10299011.mp4?token=QQBRza5k5GcuT6dfFI5QJUfx9DErIt-mmetRX5B4pNwqoczEPSNU5QcpcUxGFKejZlc4wXhIZWa1AphsAujMB1T2CW04aI_NfMTrVEJuU45pfu7mvlpISGxxhYZZwJjtgxzo01yOWNYvMZVrUhJ71B-IUa-tVrsliW2shTFaS_MJfArc3u0kKYgVgjqby2HV-IgJtqHSol__nUM_VDx82K3Dcq14X33e78OgR07PYfldOIg18Cgx0_5C_cibE1zqO6rWpCrtVMgIXy03Smf6f-5tP_EwBS4fdKdJNIF1H0XnuzuPlDcK8ssPXAUw35-5wmw-edVKH7E5C60G9U6UdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd10299011.mp4?token=QQBRza5k5GcuT6dfFI5QJUfx9DErIt-mmetRX5B4pNwqoczEPSNU5QcpcUxGFKejZlc4wXhIZWa1AphsAujMB1T2CW04aI_NfMTrVEJuU45pfu7mvlpISGxxhYZZwJjtgxzo01yOWNYvMZVrUhJ71B-IUa-tVrsliW2shTFaS_MJfArc3u0kKYgVgjqby2HV-IgJtqHSol__nUM_VDx82K3Dcq14X33e78OgR07PYfldOIg18Cgx0_5C_cibE1zqO6rWpCrtVMgIXy03Smf6f-5tP_EwBS4fdKdJNIF1H0XnuzuPlDcK8ssPXAUw35-5wmw-edVKH7E5C60G9U6UdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖤
متاسفانه مادر عمو پورنگ صبح امروز درگذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/25668" target="_blank">📅 13:43 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25667">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3e0f878ea.mp4?token=h9zustLE1RR_wJ8EsOHKwf0Eq2dH8OsWnkaRa0MiPQ3n2ow0F1EReCkEb4_uS2itELxj1boHTzjejF-nTZNvwYTXV_plGVf9Wgb_-UM18lE2SwCw22017WnN5hwLKTYHB64QSyA77YpN6gWfsTJxad5Fqeu6Pe9uw1JmECOgZkx_donnzVD7usBpphPAABi1ovLX1d3YqWi7E3pn2LYD2KmDxO9ChaU4pLeplsuKiocHxqVDfGg9QrtCaVuZ86vU_hYT8FgwgyfvsBIoW4FiZ-x7GpSvFVv9-xa_C3uWKxR7VqMHGdP9LW--HbvaawwXwRWHT9V8gEPkfQK8zl7LAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3e0f878ea.mp4?token=h9zustLE1RR_wJ8EsOHKwf0Eq2dH8OsWnkaRa0MiPQ3n2ow0F1EReCkEb4_uS2itELxj1boHTzjejF-nTZNvwYTXV_plGVf9Wgb_-UM18lE2SwCw22017WnN5hwLKTYHB64QSyA77YpN6gWfsTJxad5Fqeu6Pe9uw1JmECOgZkx_donnzVD7usBpphPAABi1ovLX1d3YqWi7E3pn2LYD2KmDxO9ChaU4pLeplsuKiocHxqVDfGg9QrtCaVuZ86vU_hYT8FgwgyfvsBIoW4FiZ-x7GpSvFVv9-xa_C3uWKxR7VqMHGdP9LW--HbvaawwXwRWHT9V8gEPkfQK8zl7LAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔹
فدراسیون فوتبال و سازمان لیگ بزودی خبر به تعویق افتادن لیگ برتر تا اوایل مهر ماه رو منتشر خواهند کرد؛ با این‌ شرایط موندن بازیکنان و مربیان خارجی در ایران سخت و سخت تر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25667" target="_blank">📅 13:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25665">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KfugoIbsbMo4pq081ZSxLCYSQsf12SZQiervVSMMTXXxqptruOFz9IJ-5frUMTib2cD1vnY5IUN9WwJls5bJCuYobkvJEdA6zekRndAaiW8g1uagjo9-BtrzA9dSPdKahx9ibgOcPsJryaak49yipz1nL8BTY8yW5NdbyT-JJ5pTLskp4dez3xd1JHwJkwrX7L5QlGVTIl2KnXTJEZFY2PuVRtZ9Vg1mtRale_Sla180yqdTb2pPaSp2e6sJYXPKnzW8_6KsvTWlKgg-r5HRqmYcLEX4SIwY37zC5R0BbdtDtJqAV8PsSrHWLM-H5vYmg8-vLfaTGNxm2nxP9iQR1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/700f8025d4.mp4?token=drmlS5H_oE6ov8QN4CxouvVS6FhE2EdEnp0CYj8MSNlJqMNEte299hpMblrJbednRrIFjp0E397GfdboZMsGTAK26LSN_-OkhRgaFl_QbkxYEzNzRj1B2kK9ufgCsuuG6IkfeDlqO8TpGz1XxEfxB9rXA1rm-PvFmzhStT41sQFlkj0qE4pVoy34reCmt7v7vnFxhP4qmHFuOckXtZYh4qLTBIWtKgQbU4TR6Doo5csZw75Qcu4G_5OkyZFUFpQwwFXg80vshiTVCThEhCczy06cSvS0PYE-JlkDFGVzMFlhEZw6CC9_M2qVHVLhUVeOevM4sTal-qx9fgIAMXTzrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/700f8025d4.mp4?token=drmlS5H_oE6ov8QN4CxouvVS6FhE2EdEnp0CYj8MSNlJqMNEte299hpMblrJbednRrIFjp0E397GfdboZMsGTAK26LSN_-OkhRgaFl_QbkxYEzNzRj1B2kK9ufgCsuuG6IkfeDlqO8TpGz1XxEfxB9rXA1rm-PvFmzhStT41sQFlkj0qE4pVoy34reCmt7v7vnFxhP4qmHFuOckXtZYh4qLTBIWtKgQbU4TR6Doo5csZw75Qcu4G_5OkyZFUFpQwwFXg80vshiTVCThEhCczy06cSvS0PYE-JlkDFGVzMFlhEZw6CC9_M2qVHVLhUVeOevM4sTal-qx9fgIAMXTzrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
بیژن مرتضوی خواننده‌وآهنگسازایرانی با تصمیم فیفا در بین دو نیمه فینال جام جهانی ۲۰۲۶ به اجرای زنده ۱۱ دقیقه‌ای خواهد پرداخت. عمو بیژن بابت این یازده دقیقه مبلغ ۱۷۰ هزار دلار نقد میگیره از فیفا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/25665" target="_blank">📅 12:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25664">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/URFy2dV9_j9mGqY5ibJ3XdEsjKET4QYN8_S1-x2Hr2utCNW5_9J4NDvjOkh5IHsw_MaNuB-qoEmzZVg6hGZEenaX6OcIUigQtIhgFkCytL-j0XZ5sIPhkn20hQ9aoIGIfPuR-Pj0e-QhK31r7zvgqHRTD0bMeC6z5mE4sJer4RGO6b-V9ELMBfX1BMobJJv1wfaMgl1hJP2jvwBDJYiINSUdPyCRZ-eKpZja6Ntk6OjDV34nljJGDzXO0TOj1o29HMG9SRBMwfwBIWjhvRIB0z7Bojh3hnLr2wzY7MChMYzO-uCbxBy2CL9TGnX-ZIFzAeielVxZofaZJcC0mxTSAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🔵
#اختصاصی_پرشیانا #فوری؛ مدیریت باشگاه‌سپاهان‌برای‌جذب‌قطعی‌سامان تورانیان مدافع راست آبی‌ها به باشگاه استقلال نامه زده. با توجه به اینکه‌باشگاه‌استقلال‌تمایل به‌جذب امید نورافکن داره و مذاکرات‌مثبتی با او نیزصورت‌گرفته درصورت باز شدن‌پنجره آبی ها این معاوضه…</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/25664" target="_blank">📅 12:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25663">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f07accb99f.mp4?token=HzSQ8szYbF4l6hN9lLUCAWdFv826Fctegxs2RdYa1ug0qDIDfB1Qu3Qupsge9VyE7m1SfW7KIaBvpDOLkn16z2VoT2QPqRpdtt7YwxSVGCMnu47NYdq_hSuUvcNz1Toy3C169CLg6fruQot6vMsNq0F-zw8Ln34siPUY2E1V5WAEQY0Z7i7lPOxAE0aoC75VdXCg8hFmsj0t0w5pecr1_7db9hN1zHkOlJ8l3jO0GOyWGHv14nJ7SAVXmtnQkFFYS20zF2svui0j4WBhIGMyIiRTt7wWcpc_dd08wuoSf86ZelJcWkprwsI9ctJJkHOGYBue0VOkZSn1sDY-cmVBQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f07accb99f.mp4?token=HzSQ8szYbF4l6hN9lLUCAWdFv826Fctegxs2RdYa1ug0qDIDfB1Qu3Qupsge9VyE7m1SfW7KIaBvpDOLkn16z2VoT2QPqRpdtt7YwxSVGCMnu47NYdq_hSuUvcNz1Toy3C169CLg6fruQot6vMsNq0F-zw8Ln34siPUY2E1V5WAEQY0Z7i7lPOxAE0aoC75VdXCg8hFmsj0t0w5pecr1_7db9hN1zHkOlJ8l3jO0GOyWGHv14nJ7SAVXmtnQkFFYS20zF2svui0j4WBhIGMyIiRTt7wWcpc_dd08wuoSf86ZelJcWkprwsI9ctJJkHOGYBue0VOkZSn1sDY-cmVBQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖤
متاسفانه مادر عمو پورنگ صبح امروز درگذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25663" target="_blank">📅 12:21 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25662">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IjqczQ2hFjEwU5rLhHLeod6FfwNprPgAUu5TNpMlUXzVIyBdndff2ot7tzD41lt39MDjJj5-F_rvhaaJCiUwgAnkb6Mn7S9acozqR6ZwvfEDXu7CRZJhk1XFuplFBN8m8TPG4ZhiEHXM2YpIFa_UvqhaxG9E6hdf3kTJ08P0a8qw5Wem_V44V_SgQsmzqP3l9YiPKKYvwfl7m0W0Sil817JBd2V93FadZEr51nMjv5wR7LSy6C1d99drDB-tvpily2Eyp936ZPk3Jy9pBW4nabAHvM6yo4sVWZ0jpNnWLDcP89miJVSeRNJnlrUM0YIUzmgKSqHrx3XiCifq4wNfjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
برنامه‌دیدارهای روز 24 تیر لیگ ملت‌های والیبال؛ هفته سوم لیگ ملت‌ها از فردا شروع خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/25662" target="_blank">📅 12:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25661">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/thff6Fel2Bxpk8tIkoFktChDg3wjNunqBgKR367EZ7vtDFPmfvgfaqYY5RDjLToLfNE879mEFZGVz_i8Pj0AYZZF6KjpSnc-5NDGbNgdPPCY4L2sZ80SXx6Kw1EM1LvRhmxZNqVzaQFMU9MNjM7RhqydjaZEkvbPMpoBj8n07qdo4S2kbK_nfPBHEBlTYAoJFhG4yHtwr97_eH7kZkZlpmxoypurQNgQmGLA4UYdTro9WmLD5zQKCr_AtSXTTUO7W-0HakcpLjFYqHyrnk7Q35-7UsnZymbAx8P4sp3Gtx6aiW0wHVz4HWhvxqFfHjbj1eWNJ02CL8h1L5Y7fr2m3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اولین تصویر از حضور یاغی جدید فوتبال ایران درتیم‌جدید؛ سیدابوالفضل جلالی بعد از پنج فصل با لباس آبی امروز با لباس قرمز پرسپولیس دیده شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/25661" target="_blank">📅 12:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25659">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FcwOCiV0Iay2BsuD-MEtFD2R1nXrsxriAPrpxvVTSKxQbgdKj8-3BMs0SLNZjJzGeS22FbnfQU-ljWVtBs0pTVo-FEERq03druKbj1aZCsXDza5Hz5Y564R-HPdD6GmH4qebjGeUE63quA2vG9UGFbcLmmHfYPB2ULb-ov6yY7pBHOtWOuCJoCAKphmt9h5Zd_lDR9Z9R3s7sORUMsOpHTVeZeokXkGY9uUwVqHCBPNJNoflaaX6afFMO0y9mC47EQ09jKW2iJXSI0lT3CsGAtzSBtYEKC2vUZab4uLx4bm1cPDs-SV-PabizoYR7s9K4fG3beyHMBVNR7D86N8ekQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#فوری
؛ افشاگری‌برگ‌ریزون عادل فردوسی از امیرقلعه‌نویی:
ماجرا از این‌قراره که چند روز قبل از دیدار بانیوزیلند؛ امیر قلعه نویی به مهدی تاج زنگ میزنه و میگه‌من تو فشارمالی‌قرارگرفتم و همین الان 140 میلیاردتومان‌میخوام‌اگه‌جورکردی خب دمتگرم اگه نکردی من انصراف میدم و روی نیمکت تیم ملی دربازی هفته اول جام جهانی مقابل نیوزیلند نمشینم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/25659" target="_blank">📅 11:53 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25658">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OKY87OkvvJkWdtJFwZ-a_QhEOAFWuxBrVb5in188nSLqa5hNnnmsCAoOQm3SSLLY4zABcM3D2n5BrN--RgeRSvzDW70vHwipS-ZJrZ5DJA2arP4bsS0xgK7-baGte8Ie1DlBUYRmI4zoi9oz5ltIPTeZPL_U9zXgcwADYy7FKS6-RC3CaMyVtjO850BuniDBJSvDy1-rMJKdXH9jolw8umJDqSVP9AwgRfk9SQAKNZ4V0b8-caNRoOLYF-gOyRubBGqnwjqZKSpZ5CsKSBucdDNag2hYJAC5rID-BhhLHblxIwXil90qXbNrmBY_etRZfZYx_BJBpVOevHU4fatsow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
5 داور نامزد اصلی قضاوت مسابقه فینال رقابت های جام جهانی؛ علیرضا فغانی در رتبه سوم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/25658" target="_blank">📅 11:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25657">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91bb7a3c33.mp4?token=HEDVetb2L2mfDQ0wmVLkamv2LOL6w04nM4ca556iyH5dGmVnPsdNP9Qbm-vNbLFajjhpLAFOunuqGasJrWrMAnbZJM15gaYqwm8Bp43unz9NKz3ANpWRG3CDcLutbuOnoKjj74vWanyvQKkcOrHm6rNYaiqMq9SvMS-S3L2Z8e_VW-QsP6BpkHLnjtSbqttfKOuMXfE3hYfI5dCMTRkhrsMh5P1dNhq0OVBu7iV0izTR0-mr_zC4L_e3p98kWdDB70lSqkcBBaIR3L7VX0bLzVjuVS-TCA4TK4KRQ2Y-oUm3m04RD_C6NgBQx8Jr8FfHuTwh_Zm-d1-SQsCBot5tXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91bb7a3c33.mp4?token=HEDVetb2L2mfDQ0wmVLkamv2LOL6w04nM4ca556iyH5dGmVnPsdNP9Qbm-vNbLFajjhpLAFOunuqGasJrWrMAnbZJM15gaYqwm8Bp43unz9NKz3ANpWRG3CDcLutbuOnoKjj74vWanyvQKkcOrHm6rNYaiqMq9SvMS-S3L2Z8e_VW-QsP6BpkHLnjtSbqttfKOuMXfE3hYfI5dCMTRkhrsMh5P1dNhq0OVBu7iV0izTR0-mr_zC4L_e3p98kWdDB70lSqkcBBaIR3L7VX0bLzVjuVS-TCA4TK4KRQ2Y-oUm3m04RD_C6NgBQx8Jr8FfHuTwh_Zm-d1-SQsCBot5tXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری دختر علیرضا بیرانوند گلر تیم تراکتور دربرنامه‌امیرحسین‌قیاسی: بابام خودش استقلالیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25657" target="_blank">📅 11:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25656">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1f067d59f.mp4?token=lSJdUSLmq501U2oMOeZBFRRfvkPXFEC4P9XxJPtm4TtopAuOzJg6Jj-ABbmIK2deIUVaStzZDO3vKjagFXhFto1zeoPVvMt0aVHtAdf989p7EDia_M9N2kgX_k1oeNRA4aG5AAeukHPMhUKHTYrsEa3qEdFuYC9Fa1MA-c_VPKv0WOLXikYMMCk11oO16H86BdV2wG7vBBEvE-nzp0HC_VgHiGX85WAxPD79fWWFBtYvqPcPZr3UkUYeF9eOkndg8-Nlv-ynDszRJCunJqqhJzmgOi2nXb6SZpD52xl-Mhe2PeXy8v7PSIcRG62Y133j9nvh1f3csaz3kxZcjqjIvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1f067d59f.mp4?token=lSJdUSLmq501U2oMOeZBFRRfvkPXFEC4P9XxJPtm4TtopAuOzJg6Jj-ABbmIK2deIUVaStzZDO3vKjagFXhFto1zeoPVvMt0aVHtAdf989p7EDia_M9N2kgX_k1oeNRA4aG5AAeukHPMhUKHTYrsEa3qEdFuYC9Fa1MA-c_VPKv0WOLXikYMMCk11oO16H86BdV2wG7vBBEvE-nzp0HC_VgHiGX85WAxPD79fWWFBtYvqPcPZr3UkUYeF9eOkndg8-Nlv-ynDszRJCunJqqhJzmgOi2nXb6SZpD52xl-Mhe2PeXy8v7PSIcRG62Y133j9nvh1f3csaz3kxZcjqjIvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کسری طاهری مهاجم جدید نساجی:
من اونشب تو شوک دعوای آقاخداداد باجواد خیابانی بودم که به یک‌باره‌رسانه‌ها خبر دادند که پیوستنم به پرسپولیس منتفی شده. بله از الان به بعد بازیکن نساجی هستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/25656" target="_blank">📅 10:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25655">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OylnSll1Zio04qumMO2xUQ3qnnmS0VFX1a78kKGXtAsBxSmqGEbAnzU7qj3oT-UxM0gYuyoNDqult2idAYKr4tqM51AhuBjffj_zkesGjsBe_SN_svDGIDZU4DQ5Nwekuz0moAbaBIMzYjTrHqfWTl0vICJZu2dCnWiatRpI3xMOv_-DyLET7Aup2DX7V90WfiTH994XU63IR_zzwQYgD3qIIdcc3eaFo71_iJGysBqVbC_SWbnh8Wl0_yRuBsiDaaegqZEHvF_QdQkaXoTmxTwBUW0c90P_hIhBTe3Cdxm5JSczdtWOVHVDz2gzKLLw3UkvZOAbxSZK0_jCFHFwWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدشد؛ باصلاحدید کادرفنی استقلال؛ آرمین سهرابیان دیگر مدافع میانی استقلال در لیست مازاد آبی‌ ها قرار گرفته و بزودی از جمع شاگردان سهراب بختیاری زاده جدا خواهد شد. پیش تر عارف غلامی نیز در لیست خروج استقلالی‌ها قرار گرفته بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25655" target="_blank">📅 10:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25654">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5705053c4.mp4?token=PO1LtwWgASS0qwuFALw_PAKrWumz0le_eMK2h8ZRBOV4rbiLQowYRk0kmKuww0DzIG02EK9CsyihopfTy470EPATlZRtMH9rDeciUF-GA3UAoFK7XcFmkHDbQlvSjkEnIvU7cJdqK2Iycr5rrIAIrSRo2gwu5pXVQ4W_d5imzv61-PB5El1tZUn2L_qbQ_oJdYW1S-fD8V4ATzukVfTbXpW8Ruk36rsIRWh80UWih8fA7ew3wSR51AZz6iIWFCvCV9G_maHdq0fJ3Q_Q4N0T2s_G8BYfYrwarrOYImbTxOEZXEvc9LXjLt3Q4NJwRK5anjOpcclNEqvHlIwwS3__Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5705053c4.mp4?token=PO1LtwWgASS0qwuFALw_PAKrWumz0le_eMK2h8ZRBOV4rbiLQowYRk0kmKuww0DzIG02EK9CsyihopfTy470EPATlZRtMH9rDeciUF-GA3UAoFK7XcFmkHDbQlvSjkEnIvU7cJdqK2Iycr5rrIAIrSRo2gwu5pXVQ4W_d5imzv61-PB5El1tZUn2L_qbQ_oJdYW1S-fD8V4ATzukVfTbXpW8Ruk36rsIRWh80UWih8fA7ew3wSR51AZz6iIWFCvCV9G_maHdq0fJ3Q_Q4N0T2s_G8BYfYrwarrOYImbTxOEZXEvc9LXjLt3Q4NJwRK5anjOpcclNEqvHlIwwS3__Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های ایسان اسلامی درخصوص درگیری شدید دوشب‌پیش جوادخیابانی
🆚
خداداد عزیزی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25654" target="_blank">📅 10:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25653">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d33fe4e361.mp4?token=RrtUizkw4IfD-bziA65MlldGDEMYf-HoYl4qvZ70OJdg01wPwIqeN7yL_kOBP3qW9XB03Rg1KpmUD8D_iHRb8NFipdLTy0LHg51HTJ0XE-mihVkXhxpckLVfxLCJ-zYrA1V22HMZkuK04Fx7MnPmwX4ZBEOjKqdowGgJVO5XdaX427AcmgFlSBJ8pD12sbZiPqExrcDwsZ7Z_EkW6C6xp8ZJu9k6vBQQL3V_cQCX5Al7l2uoyNPuvWNquryP7AewA-Lo8zEABqsv6AE8GxDCRdZqOBXg1yw4lei-zRCLNLdZBsdXeqCNGQZl2qTODEea8E3PPyrxisOPT6qyJCGoHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d33fe4e361.mp4?token=RrtUizkw4IfD-bziA65MlldGDEMYf-HoYl4qvZ70OJdg01wPwIqeN7yL_kOBP3qW9XB03Rg1KpmUD8D_iHRb8NFipdLTy0LHg51HTJ0XE-mihVkXhxpckLVfxLCJ-zYrA1V22HMZkuK04Fx7MnPmwX4ZBEOjKqdowGgJVO5XdaX427AcmgFlSBJ8pD12sbZiPqExrcDwsZ7Z_EkW6C6xp8ZJu9k6vBQQL3V_cQCX5Al7l2uoyNPuvWNquryP7AewA-Lo8zEABqsv6AE8GxDCRdZqOBXg1yw4lei-zRCLNLdZBsdXeqCNGQZl2qTODEea8E3PPyrxisOPT6qyJCGoHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علیرضابیرانوند: توقع‌داشتم‌عادل حتی به دروغ از من حمایت کنه و بگه‌مورینیو از من تعریف کرده:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/25653" target="_blank">📅 09:39 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25652">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3c3b52fc8.mp4?token=QYpghaJcXMJRZHgEPUNTmpkfpniTtror33pNZQEEDH0GPJ5UzzcfcRhcJpwwKBuOxkRzinFDPClXKyEPE4h9eOJu99WykFi5aQ3lOhN94xypxD_ES5UgnTWh1IM9q5loc1uLFxGuUCuhl0UKMZIJUt7lnr0y3gJOGIuNvK-X_Dw7V6ZqLCvVRX8H-sD4a0OEYxE6NE9hMF1uIsajBQaH7goyarH5NPqi2QCr1uf6-CQwCVxSDY6TYqIE6sZQUX-2DTmeHE_LYGmJE0cAGJ6QJERfrPBriECuHWMS_bv19kzcDdE1zYY8bDJ-Ub6xFd64XK7HPUmPnnHZQh37g7arUGf-Juhd7HNq1wgN19SoYPjdxlLW6uulGJ3_LatOOLjhL0ewSIoS0P6JlZm9uNK6MkqnZseYxnJqUEXJh-epz-ShS0H2KdpPjzsOmEruiQc2KDmarnhWlaD4i_CqN6PTE4YjHlhWRu-S79wxz9TrxyxijjpJGHgJYxLIunzFq5kLhllpjMeJJikMX5s6gQeuuZJ2ItaMDAxEcAfyGSaaLYALVg0AzfJaSgiKdkE_n8sal17MUIb1d-huuO__kdqxlZKjSTtGBL1SXQojzwDdHVSgxSZ4Wlrt7TKC5lZGVI89PGjRI9ZII3Y3hqm06ePh75Qm1OAjTSyVWe5Coohfmt8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3c3b52fc8.mp4?token=QYpghaJcXMJRZHgEPUNTmpkfpniTtror33pNZQEEDH0GPJ5UzzcfcRhcJpwwKBuOxkRzinFDPClXKyEPE4h9eOJu99WykFi5aQ3lOhN94xypxD_ES5UgnTWh1IM9q5loc1uLFxGuUCuhl0UKMZIJUt7lnr0y3gJOGIuNvK-X_Dw7V6ZqLCvVRX8H-sD4a0OEYxE6NE9hMF1uIsajBQaH7goyarH5NPqi2QCr1uf6-CQwCVxSDY6TYqIE6sZQUX-2DTmeHE_LYGmJE0cAGJ6QJERfrPBriECuHWMS_bv19kzcDdE1zYY8bDJ-Ub6xFd64XK7HPUmPnnHZQh37g7arUGf-Juhd7HNq1wgN19SoYPjdxlLW6uulGJ3_LatOOLjhL0ewSIoS0P6JlZm9uNK6MkqnZseYxnJqUEXJh-epz-ShS0H2KdpPjzsOmEruiQc2KDmarnhWlaD4i_CqN6PTE4YjHlhWRu-S79wxz9TrxyxijjpJGHgJYxLIunzFq5kLhllpjMeJJikMX5s6gQeuuZJ2ItaMDAxEcAfyGSaaLYALVg0AzfJaSgiKdkE_n8sal17MUIb1d-huuO__kdqxlZKjSTtGBL1SXQojzwDdHVSgxSZ4Wlrt7TKC5lZGVI89PGjRI9ZII3Y3hqm06ePh75Qm1OAjTSyVWe5Coohfmt8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
به‌ بهانه بازی امشب فرانسه
🆚
اسپانیا در نیمه نهایی یادی‌کنیم‌از بازی دوتیم درجام جهانی 2006؛ فرانسه‌ای که به زحمت از گروهش بالا اومده بود به اسپانیای آماده خورد که هرسه بازی‌گروهی رو برده بود و اغلب فکر میکردن فرانسه رو هم میبره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/25652" target="_blank">📅 09:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25651">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tz_1CxwSpy1ADs9WedlZOTaGwfciAF9MAi-VxPpyS2uuuHpnSWejWWUi63uqD4aJxN2By0FOGfhs26JO5f7zaY3CMQvAVR95zn-08KQDB0QfJrT7b79imYxxpznqkrAPQHQDvKnjcb6m05d6D9or8xWs38sdp5mTcqLO5Lmzf76dM1Tz2WnYiK1Jy1CSlnTDxGFxANvbx9CEu1pg1lGYaFhS784Pp_wh95BtmUE9Xc3x_HyyH8YRcGrmLZygsgG8eXDMgTktDjAgBz9RG399BRRDx2Uit8J7gxpF0rr0oX7UpWnjL3039BwQJMbEIVzpn5NwSQC0x7nzIkgtzlWPeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
#تکمیلی؛ با توجه به اینکه قضاوت دیدارهای نیمه‌نهایی به علیرضافغانی نرسید؛ شانس ایشان برای قضاوت بازی فینال جام جهانی بسیار بیشتر شده.
🔴
فکرکنم‌دیگه هممون دوست‌داریم که آقای فغانی فینال رو سوت بزنه. انشالله که نخوره تو ذوقمون و فغانی بعنوان داور فینال جام…</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/25651" target="_blank">📅 09:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25648">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/298c4f2fe3.mp4?token=ULxb71JDSZb1AEbQadLJMLYHCR2RHFqKMwFt-TpdsjGqftOIqYnrhQQX4qvPgGkV6SRRS4Wk7PBrm2dA8HqGKfbBswRZ0cTf9k2Qa372hmtapO-_gwqsusNuaQVo0kPUR3GPVxxyf-VrxWEdIlMJ5QlVbyzEtfU6zSvgGLm-3Yxw83SRDI1C4OKlqiN2BOWIVsHXKrAhYfeANhoqnohMXRyVZGWsSYRBQP245HgQ664Q4ajGzheC3xZWlvuLGfWf4gOmxny6d9l1GbQncoCoZE6UDgn9_73aQG3Ypb1fLSLi4-jWkVvWPySSwPfRsFSI0s89njm3DwCV6B4UBOiXgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/298c4f2fe3.mp4?token=ULxb71JDSZb1AEbQadLJMLYHCR2RHFqKMwFt-TpdsjGqftOIqYnrhQQX4qvPgGkV6SRRS4Wk7PBrm2dA8HqGKfbBswRZ0cTf9k2Qa372hmtapO-_gwqsusNuaQVo0kPUR3GPVxxyf-VrxWEdIlMJ5QlVbyzEtfU6zSvgGLm-3Yxw83SRDI1C4OKlqiN2BOWIVsHXKrAhYfeANhoqnohMXRyVZGWsSYRBQP245HgQ664Q4ajGzheC3xZWlvuLGfWf4gOmxny6d9l1GbQncoCoZE6UDgn9_73aQG3Ypb1fLSLi4-jWkVvWPySSwPfRsFSI0s89njm3DwCV6B4UBOiXgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👤
افتادن شال یکی از مهمون‌های امشب ویژه برنامه عادل فردوسی پور؛
تعجب عادل عالی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/25648" target="_blank">📅 01:21 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25647">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WP3S10WKLBWunaRxKUO_qweBAhO6-NiksMNpW54B0A1jlMrXFpTy_Ys2nzvjpSCFw2Mh6mCOB7JJpjaFJueC9d0E4bF7GhnQtlMaRZbjvXMMIMJem4XlmDecZ-89MaGCkNpHB1Xcdy2vx-sjjhXjy_i8jmUdT2eLPsDLDXJU-vVWWm_fEB2bSptDaIkdXAtxmIgiywRd5eIQZX2GHWwtLt4akqTxB32Pgx0OopBNcLQfXCqLB4jwISa_dvzxyw4JWjfDet4wcpF-pWHqDn8xDZPcaQn7CkwWs-HcZ3PDDNbXCYFOzDrwZTlCqjwLMnU7VqrhwMMUTHsWntO6pXlVFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
👤
علیرضاجهانبخش کاپیتان 32 ساله تیم ملی:
تا یکی دو هفته آینده از باشگاه جدیدم رونمایی میکنیم‌. اگه‌ایران‌بیام بین استقلال و پرسپولیس یکی روانتخاب میکنم که از همین حالا انتخابم رو از بین این‌دو تیم کردم اما همچنان دوس دارم اروپا باشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/25647" target="_blank">📅 01:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25646">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hi-RCtg8EYY6j-4QbuuIxUY7wqUwcRYIuefRUWrkoUazZqX7_fI__q9D3KZ-jcDTNYBYyhLb80xqcjBfjMR3nH-IhznjYXWTtveTPQV-aUF60z5ixeg2FETVggwwQ5CAI7rPIHM-QCbCRfcXFEgwIUnjByp2QvM-CeqVErmMRC3rhdy9lb3jD3eOsCFCoJvwmsSkcF1wk8DBIW2VDOqE7LTbWcRzzHpW2yv1J8Wgp3I7BYLYASZs9cbo5p2lqcpzSOC_03tH5v612DuGW1_FN5eDICrGrEVOHvMHtwo9PmarHwMZnXbVBBbEEFiJJy7-7pTnSSwIN21aNEYpJlkYCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تنها دیدار مهم امروز؛
نبرد فوق‌العاده حساس دو تیم فرانسه و اسپانیا در نیمه‌نهایی جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/25646" target="_blank">📅 01:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25645">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3e63bfe28.mp4?token=Ik3TJf5WptFpRQdblz66JNtnzJDgpSeS0vSRm9TVGdYKXvZmpP0CmynSoTGkNW2kD9k6xntntM9uMLn5DVHgXsz4kgjJhTFzOqKv-DYTfxMcVSWLmpVu5IHuTS-7SzRS4XbR9Qdl7dQCega1dDLf8c0D4rhcZmo9KcVPsAsLP3Td64DDCvhT3YNlJUkmTobaKt-czcCJChMGMA35_aX-EfdOd5uJkGy6KDrh9PuTtxCXN1cRzGnEQqwaO_TZw5Jwcaos3ZKGBPmbLy5ZManqUZ9payyFuj9xTAlEBX8D7K3RnYWx0z7awakyhUu7ipcLYTPjRqIzELto7vP3rHZLJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3e63bfe28.mp4?token=Ik3TJf5WptFpRQdblz66JNtnzJDgpSeS0vSRm9TVGdYKXvZmpP0CmynSoTGkNW2kD9k6xntntM9uMLn5DVHgXsz4kgjJhTFzOqKv-DYTfxMcVSWLmpVu5IHuTS-7SzRS4XbR9Qdl7dQCega1dDLf8c0D4rhcZmo9KcVPsAsLP3Td64DDCvhT3YNlJUkmTobaKt-czcCJChMGMA35_aX-EfdOd5uJkGy6KDrh9PuTtxCXN1cRzGnEQqwaO_TZw5Jwcaos3ZKGBPmbLy5ZManqUZ9payyFuj9xTAlEBX8D7K3RnYWx0z7awakyhUu7ipcLYTPjRqIzELto7vP3rHZLJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#فکت؛ازوقتی‌توخل‌به‌‌یارانش‌اجازه‌داده بازیکنان انگلیس دراردوی تیم‌ملی‌میتونن با پارتنراشون رابطه داشته‌باشند جود‌بلینگهام یه تنه این‌تیم رو به مراحل بعدی جام برده. انگلیس دیشب با دبل بلینگهام برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/25645" target="_blank">📅 01:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25643">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qUgkitB52aSAFFDdvO5SpIIzLFV_vu-ui43tMWGWd9w-UcyUE7l3AeG0aX5BKqYpMdHudLA2D-Mdg_plBcTHR9vIYiF9w5d7Vw-mzLMSA15u55uOi1NTRe6l_69fhz9xOlCcPC_Irr2toex4iXrtswez9uh5DqUr1YPMd6_qDqjIlCibkE-LIFRLkz6LpR9Lly6Ik1YBB1Nzeg6J0wgrvWQ8PrLoajm3lcMKE1Yt5T5N_GMLiBpKEw6V70yrPkoPdv2RO7-G_AXkMzUtTBMssbAEr1KCBrsxcDyP7Xs-KWORwWjaVlOcBWvCYCqlVzrBptmirEw-p25EP7DxkL1uFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇹🇷
با اعلام باشگاه فنرباغچه؛ اسماعیل کارتال با عقد قرار دادی دو ساله رسما سرمربی این باشگاه شد. ارزش قرار داد دوساله کارتال پنج میلیون یوروعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/25643" target="_blank">📅 00:43 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25642">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98ca4a5638.mp4?token=vFq0NDOqBl8cx7_fWDePQz1e5EIKNqVdJNAGbL_QOoteQZlHXe4XKxGRvgy_DXGYixQ0YIn7g-gm9oYODKPsbMZkqbR68L-IJXh9yrVL-aNXNirsWRiJLeKVJfrFbTVfA1v_7jKdHkr0Gm1ycOybD6FX9GJ7ZcamEzLXhJ4Ti6vBiAlqgSvs845CnFi86_VUPXnODhEen9vSBsDECCdxMgwuJx0VXluRp61r3EYSdzBr15eS11GdO1rid26mFX3k3vE2YsYSj__Cfs4F-acTzmCaDvFc2aFa06mKe7Td2GUBaTB38s58QW9jM_gxO9JH8UePcLLkr0hd7lbHCNp0uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98ca4a5638.mp4?token=vFq0NDOqBl8cx7_fWDePQz1e5EIKNqVdJNAGbL_QOoteQZlHXe4XKxGRvgy_DXGYixQ0YIn7g-gm9oYODKPsbMZkqbR68L-IJXh9yrVL-aNXNirsWRiJLeKVJfrFbTVfA1v_7jKdHkr0Gm1ycOybD6FX9GJ7ZcamEzLXhJ4Ti6vBiAlqgSvs845CnFi86_VUPXnODhEen9vSBsDECCdxMgwuJx0VXluRp61r3EYSdzBr15eS11GdO1rid26mFX3k3vE2YsYSj__Cfs4F-acTzmCaDvFc2aFa06mKe7Td2GUBaTB38s58QW9jM_gxO9JH8UePcLLkr0hd7lbHCNp0uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دعوای شدید و مجدد خیابانی و خداداد عزیزی که مجبور شدن پخش زنده برنامه رو قطع کنند:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/25642" target="_blank">📅 00:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25641">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d3d13a462.mp4?token=qojPOfp13dTLom7lii5OTFA9rkTsDRhULyR1vpyI4BK_H4OsgswydDkMqBPBcwTbjJXG_ayuYWwd8zm1HZXuakqdEMV7es_mm3SeB2zTdzvabYAguM1-T0GSPOi1-Wheq6alYeJC4OEHH30dZsHAVZu7aOaIa1y9QXjuyrm_gv9kniRUiplBfdyy28rRcpQGY44TZcLNa58CYc0cKENG1h3dk71iPOaJLZ22RRPWwLmRiVw2uL0H0IHo25TzwCq1zc1RsFbh48F5KzbH23dhhJWva_dY-EnI65pUmDjf22XluL5az9p_1A3TKv6rX62nbSSjtxT3Ukj6iY6ciwxXVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d3d13a462.mp4?token=qojPOfp13dTLom7lii5OTFA9rkTsDRhULyR1vpyI4BK_H4OsgswydDkMqBPBcwTbjJXG_ayuYWwd8zm1HZXuakqdEMV7es_mm3SeB2zTdzvabYAguM1-T0GSPOi1-Wheq6alYeJC4OEHH30dZsHAVZu7aOaIa1y9QXjuyrm_gv9kniRUiplBfdyy28rRcpQGY44TZcLNa58CYc0cKENG1h3dk71iPOaJLZ22RRPWwLmRiVw2uL0H0IHo25TzwCq1zc1RsFbh48F5KzbH23dhhJWva_dY-EnI65pUmDjf22XluL5az9p_1A3TKv6rX62nbSSjtxT3Ukj6iY6ciwxXVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
فیروز کریمی درباره‌انتخاب دومادش بعنوان سرمربی تیم پرسپولیس: انتخاب خیلی خوبی بود‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/25641" target="_blank">📅 00:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25640">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LlZxliSRV6wBVfdhWHycStPCHUsQGWH_qdwkRjAVov4G6nAL9sPI7ZtHoizxVi1sbXnURVNp8kd-oVldytvxUUAPhcrGjjbt5K4p7ZMfbZ2bbkV1GT6FYGRAl70YWvoGP8-nqLUVGQmZRn5SSR-6KNrWjHA_mQSecemQ448ZQ0hfFS7IUM29QRn5Ate9BBbZ8DYlO1qBJVOteuSQsaagVkQzNloUKW598gORXf7mbu3RoltRN4HHnqJx78xGsfinQRS7X0KzUTnqPzifKlkVuBSnX0EXQDHolsZ9G9X5FDa2FVg6a1Dyegf5TQDO7JdtRcwjB5HTWMYb_5VY4uLStw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
رامین‌رضاییان ستاره‌استقلال درسفر خود به فرانسه‌کیفی‌از برندمشهورHermes به همراه داشت که مدل‌آن Birkin 40 است و قیمتی حدود 21000 دلار دارد؛ معادل 3 میلیارد و 800 میلیون تومان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/25640" target="_blank">📅 00:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25639">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c371yzfp-4W4s3NLwpcPNSIpnFI0TlZ2LTITmJxXKYjpxwSKS-Zn-ToFU08F7UrlMDsE6m1H7l9oDxzSlfwdrO6wytk3r5CZZtdtQZxWUQc1KOqhfZCAnpuvduEu8LkEOVfKVlYq_O5jDGiUT2HLZ_A25ltvUaCsZbb_oPVLHoFjySkCJNLPQFZVQzwdHQgm9Q_EAiE95Y9e8eqL7NWyuN4CxN9cYcNOYjSCCsrD_V64bygpXIcQ_bUG1riQvOCKwqYRKC_xqmDuF7eoKSzuujmtV-eMf5dEfl07J1GMZwZC35gWfa-fOO_Za6rBDlkvlloli1mwxfc13PCz4Z-2ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ باشگاه پرسپولیس باارسال ایمیلی به‌باشگاه‌‌الاهلی‌خواستارجذب رضا غندی پور مهاجم 20 ساله این تیم شد. اماراتی‌ها پیش‌تر مبلغ رضایت نامه غندی پور رو 2 میلیون دلار اعلام کرده بودند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/25639" target="_blank">📅 00:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25638">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ph5Ueqb5Skxt4szftSmHx1sscHvclZ9jEYBuQ5F5944zPQQmSluO8-PfEf4dJ-DkElRDgOVh8ld8wRqIn5NT0bWE76g69d5LI-rMQi9-gA-MtQlsBE6Rm54AhlhvdsVpvAITVJ_2LSdItqR3JvVDdR7f8_4a4o1cIXMGRhOZ2mE8GX4slPtfgN-igGABj-HBWULKseqX0Ht6ICRuQ2td2Y04q1kpsWQBp4MNt1yoHs-gsxevAHLdH_h-KXUWVLYNe7EmfA_RXNc0chV3lFhyd44c9wjKJ_G0u7TqFE3B4lRdmHt1HjmU6el9-CWlfj_27ARaGNvfbhlyp4TbxoSf3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
این صحبت‌های مدیرعامل تیم نساجی نشان میدهد درصورتی که باشگاه استقلال در جذب جواد حسین نژاد عزمش روجذب‌کنه با مبلغ زیر 3 میلیون دلارم میشه این بازیکن رو خرید. فقط مذاکرات باید حرفه‌‌ای‌باشه و بی‌تعلل مثل آقای زندی‌. گفتنی است باشگاه استقلال برای جذب حسین…</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/25638" target="_blank">📅 23:55 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25637">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8ae1ae07d.mp4?token=EOaQPKk0Flatqciusp2kAW221AB0Br4zayjjliZRnVlRxorZVuOtq4HgKD7H44yy_suamcs-7FVczLYU9OC0lFYuJqgaYEaMe3FtOiDg8ASvhtKIMTq1gfSAr79cPqI8gnWlgs-HYF9NbYPiXIknjra9H5hjLq2rFpCrlZgvkgZ8Rv5W-qeTwx44k0pYt8AkqPtGWCsO-5biEKgdImCewXQTqXGyHYmvv_ihlW7-jxJlH1odSLY3g8YA7CaGPP0jssHjIaOSxPJeo_jOs8We_ROk1QYfX9mR3W-jIHGhG9cA8nVVKMBllrgpotOOhVUtJvzUeuFqPLI3hf3GL5nqDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8ae1ae07d.mp4?token=EOaQPKk0Flatqciusp2kAW221AB0Br4zayjjliZRnVlRxorZVuOtq4HgKD7H44yy_suamcs-7FVczLYU9OC0lFYuJqgaYEaMe3FtOiDg8ASvhtKIMTq1gfSAr79cPqI8gnWlgs-HYF9NbYPiXIknjra9H5hjLq2rFpCrlZgvkgZ8Rv5W-qeTwx44k0pYt8AkqPtGWCsO-5biEKgdImCewXQTqXGyHYmvv_ihlW7-jxJlH1odSLY3g8YA7CaGPP0jssHjIaOSxPJeo_jOs8We_ROk1QYfX9mR3W-jIHGhG9cA8nVVKMBllrgpotOOhVUtJvzUeuFqPLI3hf3GL5nqDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علیرضابیرانوند:
توقع‌داشتم‌عادل حتی به دروغ از من حمایت کنه و بگه‌مورینیو از من تعریف کرده:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/25637" target="_blank">📅 23:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25636">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4483a354d.mp4?token=SRkkVKMSPNOOw-n3OQXcUnQLbYgYtuXefZoA6wvYf1dee5cdTUPt_Uzzqz7Ue_IEP-YIwCSeV-vj3MQfwGvYIHkfgPwaYDL9D6tquEMnCsGddz1rgFp_yUbGEprZX0sEpks24BjQCK6yfqB2gmhtdl8d97Fzv1eJGLAR_u4Xp-8ansnSdK-QUqSRKlpSMTHv3sxjUBFxvZwkxzqgmMWlsuvL_XAGHAThiIL8jzUaLdpbSNc-1-g9AR-R9y0etOtL50J-RuoAVbcvB8gQGeqOc6c2iH7mA5dGwEum66asaQ6nlYrO70WlecKh-H48vmJlJTIOeSSxB8JmRlU9P8TUAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4483a354d.mp4?token=SRkkVKMSPNOOw-n3OQXcUnQLbYgYtuXefZoA6wvYf1dee5cdTUPt_Uzzqz7Ue_IEP-YIwCSeV-vj3MQfwGvYIHkfgPwaYDL9D6tquEMnCsGddz1rgFp_yUbGEprZX0sEpks24BjQCK6yfqB2gmhtdl8d97Fzv1eJGLAR_u4Xp-8ansnSdK-QUqSRKlpSMTHv3sxjUBFxvZwkxzqgmMWlsuvL_XAGHAThiIL8jzUaLdpbSNc-1-g9AR-R9y0etOtL50J-RuoAVbcvB8gQGeqOc6c2iH7mA5dGwEum66asaQ6nlYrO70WlecKh-H48vmJlJTIOeSSxB8JmRlU9P8TUAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وسط برنامه زنده شبکه ورزش برق رفت!
رسول مجیدی مجری‌برنامه: بازماانتقادکردیم نذاشتن ای‌بابا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/25636" target="_blank">📅 23:24 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25635">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U0H10ecLL3YZ55qX7OZ0xXvfqgT_TX4ZbYjDhKv-nbLd2Gh-HN4yiVD3pgNWGkGebSqU_Jgbk2gbdiGV38N5x7yuFlkxvjQXaWYFUqbgtcQ5PZE2JCnKNMkzbfkXisSOk7_o5pDlBAyfShxqNlpdJaaGYTfsr8bgLC0kLOV_b2hTfT0z4ua-ZCLUJx7pJHY-WqaKIW0N_p8MG_JmATetPMtDhnIwyrGTKXNbcI3F--UdHZImUynl7LA2HRAgDc7uEPMpSgWAqEwgROltE5q0jTsFAOuo7VucPbYjubsU6wXkvtcrZ4C9IOogIhNSc4LQFQuDc2rQM5FBdUg2-h9M7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
خوزه فلیکس دیاز: مایکل اولیسه به سران بایرن مونیخ اعلام کرده میخواد بعد از جام جهانی بلافاصله جلسه فوری باهاشون برگزار کنه تا تکلیف نهایی‌اش‌مشخص‌بشه. اولیسه میخواد که در همین تابستون از بایرن جدا شه و راهی رئال مادرید بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/25635" target="_blank">📅 23:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25634">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z8QiT1xsqXXHIArLrHxmhpKFTmbsYrrYP2gG3HhW2fmm0fgg_E7amjiwZobNaJ7tVmXcrPYJRn3SqSxSYFJqcjsL1223H4ueQV-zZm0iQwq-pdpBgaOrrImatlWuA6SMkZh9Ogk4V3bt6B6C_mrUeDO1sJBnWNFKSzJfylu0zX3aFtTEe5K3LJyCR81_PZix3NlNeMulbL_36imbaYaItPyvzPQMSlemCysFMlzIcuVTppJaJL_xBEpwB0OtcvtEJhVO4GZUO_Tb7DTWIJENcaPLzX68Q7ZClfoX-86YPRP8jebFXN7JQpfnjSZUpm-xZ6StXOJY7-E9Rqj-ed_M_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
خبر شوکه‌کننده دنیای فوتبال؛ جیدن آدامز بازیکن ۲۵ ساله تیم‌ملی‌آفریقای‌جنوبی که همین چند هفته پیش در رقابت‌ های جام جهانی ۲۰۲۶ هم به میدان رفت، به علت افسردگی خودکشی کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/25634" target="_blank">📅 23:06 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25633">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KQBeTPrZaqPZ-sets5ARuRK7fhgCMOOE_Hr1tD04EmsucmXg-1_1psI7CE5kbcgAIgg6Y6yi8HqyGYTIY6GaLkf6dnyc9Gjx14HCp-ELYTcjYjr_4y-U9puRAVXKY9gGhhUjWjxNt6wnLZJcEAltvBbO8di-50weEMtQdfj93s7kvkl5DN5Z9yUEMBksO7tJYrj97sMlBYoo8I3x-oebonBHUo-0P5rhjZ2fZDxv5ucxqIz6y0cLTw1iU4A8lckHA_PsCPauy9Ye3l9aF1o_npt1nJj0VoznUNWA5Z6Qe3pS5etE4OYDFIvm7QDwhetH9u0y8Wnnhb9hqWFzmjhRZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
علی تاجرنیا رئیس هیات مدیره باشگاه استقلال ساعتی قبل بازمصاحبه‌کرد و گفت کار انتقال محمد خلیفه و بهرام گودرزی نهایی شده و باشگاه بزودی پوستر رونمایی از این دو بازیکن رو منتشر میکنه‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/25633" target="_blank">📅 22:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25632">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PKAniuHVa_Q1Q6tGza--BxYB-ERnOF2aISf581rKjmGIFG8QWkCMPQ5-YPid1IiS4aZI4NIiHO5zjcrxvXk7-tyDJiLsVmCS6BqyjlflbhG0949CouhMxKkENFcKMVlctxroBqTmQ35jo-8zQSfH-b1L5HySaO2liBvhUwDCzrqyajT8L3fod04zwzrRbTeRFhy5Kac0G5rbgGshLmZqEvmzFppGoETFps-s138rEGEN81SClwf0ORXOjHcL79k_EZFdhBwezL-WDkYQpx74yfOTltb6yLV1Rr91pQ5GOLlRy6z66dDbUKaUHYh2rUH23v3CxBxKcLAbiIDpSKS8yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
نادیا خمز دختر خانوم پاکو خمز سرمربی سابق تراکتور هم با پارتنرش ازدواج کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/25632" target="_blank">📅 22:24 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25631">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4c24c7d9e.mp4?token=KFLmAhi1iDCUPOq-yUkpgWdgttcU4gW9ZsM-taNZ8AL08oXsrN8VOeOPZ9Qth-V4l4KPjFfVc-1dS86Xd2TOkMLViafDQKcFxnN26VGOj3M1gHecMu4KYK1acbaDroFkqbNTOKtrBCz_nSnrpj8ZgYkcDKSgl8PiJiN8_nFrAQnFlAxKiFPBZa395OXQdxU54kM8Q2YGknOXacgvbrNWVi00Bs0HJEpKFfYqCgQXX9a-31k40Wkc9CFY70-0PYXSGbnK_nR1O2rAXirBuJCUbsjszBmOa_V5X6kEjcngYqqn6MhsdbGMzqc4VrOSrOiZDJg6eNDFDuNF6W4-M768vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4c24c7d9e.mp4?token=KFLmAhi1iDCUPOq-yUkpgWdgttcU4gW9ZsM-taNZ8AL08oXsrN8VOeOPZ9Qth-V4l4KPjFfVc-1dS86Xd2TOkMLViafDQKcFxnN26VGOj3M1gHecMu4KYK1acbaDroFkqbNTOKtrBCz_nSnrpj8ZgYkcDKSgl8PiJiN8_nFrAQnFlAxKiFPBZa395OXQdxU54kM8Q2YGknOXacgvbrNWVi00Bs0HJEpKFfYqCgQXX9a-31k40Wkc9CFY70-0PYXSGbnK_nR1O2rAXirBuJCUbsjszBmOa_V5X6kEjcngYqqn6MhsdbGMzqc4VrOSrOiZDJg6eNDFDuNF6W4-M768vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیم استون ویلا یوهان مانزامبی پدیده ۲۰ ساله سوییس در جام جهانی رو از نیوکاسل هایجک کرد با پرداخت ۷۰ میلیون یورو. اینجا هم مارتینز ازش میپرسه میای ویلا که میگه آره آره بزودی میام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/25631" target="_blank">📅 22:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25630">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dqVg53v9VYQthAy-hH-aAAToWW_gT0fHGtBcwfXweC4NA78BAj9KnKbF3s8IHoBYUMdQl6jSddvQ610uxrVbNkpEeC95RjuzC7eli53p1NLrBd5wXzyuWSj4dCnP-Wd_2qogsD63-sgPRuNF1L3qDgGZ8MWXZxzGvMRa6v7PWwpmHR2xDdOygKUQ7HCRsFxEPot7_W0zw_SYBeIVOSFfnvQq-6q6SwlhsNyubkE1NqqPoa_9Ns5K_M4VBB--0i7pXpcYNik2cvw7FiUU2_zPCK0EV3lqAm0ZbRbqTJKgeNWvC9uH7I61QAxvMK5p2bISmC8cizOfaGedQjR0bd0AHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
پارتنر جود بلینگهام ستاره انگلیس هستند که قبل از هر بازی حسابی به جود انرژی میده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/25630" target="_blank">📅 22:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25628">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_nxC1gqgVrH-EY7CQX_zLcge2zgFr7VdJGhn9Oiw2NOqwFDZNegB-mcWnJOXke-i0CUdt731lVI1HdQrnqXwEoK1Pm9LiN3ZGoVV7qDtADIea6R06VQGAxG9nMCqkeJ6EyZk7Ycrb9XTD3saT-_CTOVttcWUUcGtGCfuXU_7xM4DxAgfT1-ZlIsAlslvituJ4j5G-iMJYUMhVd8CXzI8sahW6KlFQeR-Ef2K2Cv-qp_wU8Wj_LcVrqXKXMn5JsO8u7QbMfc2bioOxmlyypD3s6WOwlt-LQbmfJrTI9Qxhr1QL7Tfzz5przzu0A-w2NJnoEg0er--9oIib-KO_qtbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
#نقل‌‌انتقالات
؛
کرارنماری‌وینگرسرعتی 19 ساله آکادمی فولاد با عقد قرار دادی به تراکتور پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/25628" target="_blank">📅 22:00 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25627">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o2sXV_HEUnxi4UfvoeiWpWbCHGBr6ie2AyFoKqQBT6k-kc-Am6LNIZgtGfp1VzVo5L3747pG2qCFl9HxS_MsG1bnvN3RfaHpmIASh-zM3yyHisHC6erDDh_nQsP_vTk2C9RyCoqNd6-DZT8wy05-nWXX-xjkCf9vLC-7nh1neRo409E3xtkgl7uqM5mrsQiRf_ZMNfXgA-i1mfX1O_l1Wm1kc9s8KqDTzisJU47QDGtF0B_1VQ15kEf3qvO2iFlp2lzE4vaw6Fo1haqBS4fEB16ciMR-gY5UKGiA0XN-b2myZEfKLvpSMfSwMbigWLr0YGyDK_bv1lDOXDDmxiF_ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ادعای‌فوری‌نیویورک‌تایمز: ترامپ رسماً به کنگره اطلاع داد که جنگ با ایران از سر گرفته خواهد شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/25627" target="_blank">📅 21:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25626">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AwnjixSQFubvC8iJ2GXffapIJepF4mr-oQwjRwCy8WMVOF1Q7TpWs5QaQYPe-Yye5BeQ1C4gaNG8TNlF96u7r1Y46euZ6soaFiIkmDvWKPfCsBM6MwZTlrvDtbmpb4a7qBGCJJYQoeQ4MGbr08WYYa5WXuHahyQ0dBNA30yrn_5BlBCfEChJPUEZ7ucYvpcZu13mGcElICPFQUFMxpr3rjQcnp-UmA-63mC0QnGszY_oMwtOp-Nloc1HfMRLELxlmcQTL1t8U8m1ofqGROi_hUKOT2EHkVPbUsRJl5Toey1cSHQ3Bsqj10MQPrjkRXKytd2KTgugX3toqRdjnghn1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه مرحله نیمه‌نهایی جام جهانی 2026
🗓
سه‌شنبه 23 تیرماه
🇫🇷
فرانسه
🆚
اسپانیا
🇪🇸
⏰
ساعت 22:30
🗓
چهارشنبه 24 تیرماه
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
🆚
آرژانتین
🇦🇷
⏰
ساعت 22:30
‼️
دیدار رده‌بندی‌ جام جهانی ساعت 30 دقیقه بامداد روز یکشنبه 28 تیرماه و دیدار فینال هم ساعت 22:30 همین روز…</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/25626" target="_blank">📅 21:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25624">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z7-FZx8xmYWqq-_bWob42jZncoZnYWLOwtVZ9eSwmWfWz9RK-E3H5MEtL1FMhPXtKuczto2oCfSyBbpZzAPFAS255XD6TaSpiuCXqapBCX2sSyQ6-mlURDupEHf0U5WKHrHbmoeGMjioKVq_fxAH35kUtHUeg14ArfT6ByCo_o9ZB6JVmv50kkhk_-6sZMmkq1wEDvxSj4a7lncaioEyHYoObJLAYz-vcUyKKpSk05gvc1N5DYdhub9YNHqSg_3pNiAgdTEQG056TUJg4kavocihAV_tYFoKo98G1pNZFXXNymnQqd8MK2y8ijdS0_Fv1rS2eyU8tkI-Y9NDyAlmZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QVp-dJFJsrsOTMqQ0prPKBXN5t42epPsgRM0qLjeSCchwqeCHR-yfWffzRwW3B3amZMxKXBgo1wV6ZtGp343PHjoohzUsVL4Gm8fyLFTs_VqQ9N5IazD9b7Roqkt4oBX0bVGibcBkI3DDEbTmID6_U31YsGUmsz5sglfPfq-FeezGKfyyGkZvK7TcrWEg1u_Byqg28WX3Jf_FLQ2s7S92igOLB8qQn5t2VWto1RKz_ElEUcn0zqnpNfnrXz_VLYsu6tjVQcQBLtISyr1CFTXeFIQ4yY7BMP5esOzShm5EXx-DjqA8E0OF8vqIZj2-cwGHim_sKTBzHeQMRBvuIFwGg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
🎙
نادیا خمز دختر پاکو خمز: من علاقه زیادی به‌فوتبال ندارم اماامروز همراه‌پدرم بازی ایران مقابل مصر رو دیدم.ایرانیاخیلی‌خوب بازی‌کردند اما شانس باآن‌هایارنبود وگرنه میتونستند با اختلاف دو الی سه گل مصر رو شکست بدهند. امیدوارم ایران به مرحله بعدی صعود کنه و…</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/25624" target="_blank">📅 21:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25623">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rZNwN02BX-ppFi6jskg44nYHmnZjM4DyBVcCmF7QOdBG3e9_Xon1AG6ldu3LELitk6c0vZC3Dbf6rE1_K0u0JIrQ9VEbyoHbcGIEHp4svUEiFNxF4Nc9N5LySY0lGRGuAmybnGRPF0FQqIRq3GRjWfcQ5ee4gW5YbLSs9pYCd9ozc48-xTre0i_poBQKrRTY56BL1NV5qpUybJwFQpPUMPlBzpN6zNruvF7b_2EQAvh6SVRYFIBzX6C_sRoHAQdlRJhO4tSIVOZjUpsbwTb7daIxamTYesRPcYayQi4h315fxZzbb_nbYNoWAVFVYS4UO6Cu4Nolra1Znxk7jF9k4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#تکمیلی #اختصاصی_پرشیانا؛ محمد خلیفه ظرف 48 ساعت‌آینده قرارداد چهار ساله خود را با استقلال‌امضاخواهدکرد. حالا درصورتیکه پنجره باز شود از ابتدای فصل برای آبی ها به میدان خواهد رفت و درصورتیکه پنجره باز نشود قرضی شش ماه درآلومینیوم بازی خواهدکرد. در کل شماره…</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/persiana_Soccer/25623" target="_blank">📅 21:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25622">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ETBcIhAt9FDvWIGV8HVGyK65jAflCAS7lBnBpKz6aeG-1mVwbjdpVTU7USOAxqjzgzy_8VrvppJ7T7CXw8hmuJ4r0xph-85Mo6NfdnwFC0sn4A3iaWF_JZgVnptdSoHVqXrOJb_qfRPMY2KNeeCU3OPzJzjsPny872eaMbs2LSI4eXBMwH2_7juKaFM9hbrW82xtqo4CH86K2htORMp4lLeGpq66Vb_IPHWNTZKpK-OjcNj4hwSgnNpr88TlY3L6yC0tN9CGDYzJg2giA3xZGUHVkr_ofxbIrNvj9EWtpshNryv-Txx2u0qOs-PfesKEF-6Cx7auanv0RulvjJNOTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#اختصاصی_پرشیانا #فوری؛ بعداز منتفی شدن حضورطاهری‌درپرسپولیس؛تارتار سرمربی این باشگاه در پایان تمرین امروز با حدادی تماس گرفته و خواستار جذب رضا غندی پور شده. قراره باشگاه بزودی با ایجنت غندی پور ارتباط برقرار کنه. غندی پور از تراکتور و استقلال نیز آفر رسمی…</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/persiana_Soccer/25622" target="_blank">📅 20:42 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25621">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EBbDW3-u3rYaTDuFXkOklbBT4VvcCg_ITymFtmElmRtJ5IA9N-EBH0GABUp6fbGnYMjOu54UoaNcJJAH39VknT5pwak_WMNuHITU9WRLQQeysXWNBuVHcmwppzV7hfkV_ttADIg6AmF0SPXxSg03NC2Xq8GjbeUyk_Ik2kBqUVMzP4E-Nv5xvuWtBzPnqf5ezYT5dIbkdW3AXdXCgVk1yD7J2TliXpVOHbdevczodTiqgbIKxozNa0OrHJNhmcwRKnvo2V0YIBSNv-5bk7UPAgUWteO8ka0wU0X0bf1DTKPLI-sbWzRuG5pUqXDt7CXyWP2LS1i2n8umSQ0Re0Tisw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ رضا شکاری بعد از دوجلسه تمرین با تیم پرسپولیس در لیست مازاد مهدی تارتار قرار گرفت و به مدیریت باشگاه اعلام کرده قرارداد این بازیکن رو فسخ کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/25621" target="_blank">📅 20:38 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25620">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/evuNPgAQ47Pus6hVoMCpdZD-A3q1plomfTtfgpBKfjLrN710xptE7QJjWAnoKILJFagDepjWDMq4j2TBcn5C2k6kJ78rsULZChYNzaP_JapN3oQtwQyCosJBB90mLeM-iRQNiCRzCFviqm5m6vGKnVETChpq2DWpe9fadhoFiiepdhenptuiONhAKilhER1yJ9RrkBaczSkyXcSZay1yFoGymKOBsxIzDB6QGTGSniA3Ehm24i6zqKJqlc7DI6UiU3fq-14OLPDXlc22GkiotVJdqLDqozKsYGUkuqol6n6onnUkzI_Clo_BnwRbZpuVW00n9yWMJJvUcKMt6bd6Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
خبرگزاری CBS: علیرضا فغانی داور ایرانی الاصل قضاوت‌فینال‌جام‌جهانی2026 برعهده خواهد داشت. فیفادی بزودی این خبر رو اعلام خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/persiana_Soccer/25620" target="_blank">📅 20:18 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25619">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CPpi_QWnL_Tru-TZbjvOHj31FdU7d6j8j8cfAS3m4wDvjjVSJebbMZAJWv7BGnBISBpY65OFRtp4Z967Q2Lg-S0wD7Klj0lGC1thNuvXnakwL4p5sRvhqXpqRdFaDs_wOfiaDt79KHwc9_EcHGYjpE0zbr6pyAyXc6mQWQ5i60Ioy0ip7pVH6vRYyc1kxWNmtCrSz3UkCDJHNJ36KARxkyaZOJtzhNVvJC0ze0Pm1Vr95B-yx7MaeIEpwZdIXLeVX0-efdY5PqZUTocNFT8pSRLJEzoazfxae2gflUMXd2h7cdXfLc_B2Kz1mMYtXoLvN5kjqLSqFOIUOfJhPQQxlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه‌استقلال: باآسانی برای‌تمدید قرار داد او به مدت سه فصل دیگر مذاکرات مثبتی داشتیم و توافقات خوبی بین طرفین شکل گرفت. امروز آسانی برای دیدار با خانواده اش به ترکیه رفت و به محض بازگشت به ایران قرار دادش تمدید خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/persiana_Soccer/25619" target="_blank">📅 20:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25617">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ORB1KLSi5v6MUqj5oSqj3KxbWgJmN0DA-zhKVVyIAW3L0UZZrmNanAHrGQe9IiBJ-cppzpiT_VOZhYYAeGjcV0HjEkOwheegj_KDVTPRY1cYuO9LtnuwF-IjQ1ZvRvMkuJcgkzV5Mhj-G2JJhUdVcotlJM__h1sjYyvUZL_QZGiTpwyIM0uZ4Mna0fjAraIObmhBR9_hlVL1wfFiLqFH5fanOS7yHo8yMi--tf4r48FerE4PR_gp41Y1ducOYl4hx8QiL_RkJGoWB14WDWeYtDR3k4bn_YC0JQXbFhsvtzVfo5p-H0xJsuPoX11jp8GCFrUCShnup2Q8tSdytBt0CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال به مدیربرنامه های یاسر آسانی اطلاع داده قصد داره که قبل از شروع فصل جدید لیگ قرارداد ستاره 30 ساله آبی‌ها رو تا سال 2030 تمدید کنه.
❌
آسانی آمادگی خود را برای انجام مذاکرات برای تمدید قرارداد بلند مدت خود به ایجنتش…</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/persiana_Soccer/25617" target="_blank">📅 19:39 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25616">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b1cKnW3UAHrWhdpz7c1n9usugeKNHsBGb7dPTXHVkz1yaWND_P3rBddTWS0wBi7RfsHWByjftYBCWd8L1-784FlUVghfxccLUZSEjGOYIYzAR4J6ivRxgACuJVpSv1t1XuTBmrgNfx5xqf2eikRz-qz0r-YL3wvLimHZvczPiJKHVrnMSLtceQ3Y9dOykqilQu9K7ojNFkiqiIXpJWBwDzsqsNPPUejaW6dXgM1oD-8IkLTky8hur2dhGnCG1GkqzPFYfuqByPEXQkH3P-h7xiK9ViWVcLyoGqmb_xu3p7IF0Ddz94KvxaQozDl9ai5r4aR63xCnBFKyEkHcybGAPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#اختصاصی_پرشیانا #فوری؛ بعداز منتفی شدن حضورطاهری‌درپرسپولیس؛تارتار سرمربی این باشگاه در پایان تمرین امروز با حدادی تماس گرفته و خواستار جذب رضا غندی پور شده. قراره باشگاه بزودی با ایجنت غندی پور ارتباط برقرار کنه. غندی پور از تراکتور و استقلال نیز آفر رسمی…</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/persiana_Soccer/25616" target="_blank">📅 19:26 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25615">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q7xwBN9nIctFyR6BQ5jq00MEQGszPyDE_SihlqQCYyOCRNAJVC0QCEmyXnmYHBx7ncBKaTmnLEnKWuDqum2JCWF89yLZ_ze49f574GF9VkDY47V0zztY3i0s3X__LGMg1IX-vPygzkh1J4-9dNUcD2wtB8H7PSh84OcCzMjmO6bvmM1DHGBZVgvBvwa3nYyPkQrDeQ3E9hXxRrSPkc1MiqugCSJgARk9p4iuZsuL7PIEJcw-QchVjECPtmZh-FxV-k5I_1NgIyF1b_1g_uCJz_P3RhwKsUcILNkdL8jN3_EAGRPvxAX3YiNXvuW43q7OSI_GbRqjn2vOrUyp-3lFiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
👤
#تکمیلی #اختصاصی_پرشیانا؛ باشگاه شباب‌الاهلی پاسخ نامه باشگاه استقلال رو در ایمیلی داد: 2 میلیون دلار نقدی پرداخت پرداخت کنید تا ما رضایت نامه رضا غندی پور رو براتون صادر کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 84.6K · <a href="https://t.me/persiana_Soccer/25615" target="_blank">📅 19:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25614">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d281ac96dd.mp4?token=LIjcdvRqE-jU4EpvVZiIUoSnTgGusW6tVHiE--GYqIIf3Jsurz7yKsknIeGtTMT9PY011H0MQDdXZ12-yusVhwqK1_c8vn45zKx8Ggz5Opql4fKSsta8BH7TgDQG2LvuPRzh03E4l88lYVi7KJCjjKAtvGS7uYX6lAX-ILdnF9fxYsOmPAdc62ux_l9IOQ2aUPzJh4XsE1KKS88zlGcKCT3W_InLgvzrSTLg4bXEq8nXZ2GcbAF8KzWI6syfyY_qpUJ-1Op-QHKRQj5dPFxWPAySazmLctiLyCXsyaduOVpPZ6XeucGOz_j4hBrdlIs7xVYnhyPmYD0KQcNwvG47nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d281ac96dd.mp4?token=LIjcdvRqE-jU4EpvVZiIUoSnTgGusW6tVHiE--GYqIIf3Jsurz7yKsknIeGtTMT9PY011H0MQDdXZ12-yusVhwqK1_c8vn45zKx8Ggz5Opql4fKSsta8BH7TgDQG2LvuPRzh03E4l88lYVi7KJCjjKAtvGS7uYX6lAX-ILdnF9fxYsOmPAdc62ux_l9IOQ2aUPzJh4XsE1KKS88zlGcKCT3W_InLgvzrSTLg4bXEq8nXZ2GcbAF8KzWI6syfyY_qpUJ-1Op-QHKRQj5dPFxWPAySazmLctiLyCXsyaduOVpPZ6XeucGOz_j4hBrdlIs7xVYnhyPmYD0KQcNwvG47nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تقویم
؛ یک سال پیش در چنین روزی؛
تیم چلسی با‌آتش‌‌بازی‌ مقابل‌ شاگردان لوئیز انریکه در تیم پاریسن‌ژرمن قهرمان جام باشگاه‌های جهان شد. دوره بعدی این رقابت‌ها احتمالا در قطر برگزار میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 83K · <a href="https://t.me/persiana_Soccer/25614" target="_blank">📅 18:46 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25613">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5adfb3366.mp4?token=p6WsFaDKtGphUzI_q0uZA7Wz5S2dW978QsNkn8FBM8gU5hN0KPGESdERCfmLTchSLa9DYRvjsnHjxCng5tU9JZx6dxKigPGPnmficdMXpJkXwht8I_a_y5mXnz7EqulmJL9vJZsdWgZum7jZQTzUS_j6TGomNENM4trjru7G3wtU01zvY93t3661FJkyCLSZT5Wz3lFalXJ2f_b_mlv9xh66a6104e4sTu8DLv3VJuLAsgWh3aW5xDQp0f2IlZ99jAA-LAtFRjyMMSXGySAlHptCevzzklg3z6Go5iuZw0nN8bqh5GoYaVGGPtj_TjKPhBnOmsN9OX490dgqkakERA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5adfb3366.mp4?token=p6WsFaDKtGphUzI_q0uZA7Wz5S2dW978QsNkn8FBM8gU5hN0KPGESdERCfmLTchSLa9DYRvjsnHjxCng5tU9JZx6dxKigPGPnmficdMXpJkXwht8I_a_y5mXnz7EqulmJL9vJZsdWgZum7jZQTzUS_j6TGomNENM4trjru7G3wtU01zvY93t3661FJkyCLSZT5Wz3lFalXJ2f_b_mlv9xh66a6104e4sTu8DLv3VJuLAsgWh3aW5xDQp0f2IlZ99jAA-LAtFRjyMMSXGySAlHptCevzzklg3z6Go5iuZw0nN8bqh5GoYaVGGPtj_TjKPhBnOmsN9OX490dgqkakERA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
برنامه مرحله نیمه‌نهایی جام جهانی 2026
🗓
سه‌شنبه 23 تیرماه
🇫🇷
فرانسه
🆚
اسپانیا
🇪🇸
⏰
ساعت 22:30
🗓
چهارشنبه 24 تیرماه
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
🆚
آرژانتین
🇦🇷
⏰
ساعت 22:30
‼️
دیدار رده‌بندی‌ جام جهانی ساعت 30 دقیقه بامداد روز یکشنبه 28 تیرماه و دیدار فینال هم ساعت 22:30 همین روز…</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/25613" target="_blank">📅 18:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25612">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KgLOI4r2qqSsxb3aowm6HazY5EufnzF3CJICa9NTgKQHjtejBt78iSC0ByR8Rzr3u9PT7cSdyytU7N3B9LD-3ZCSAomAfQgO9AlC6sXfZiDe2cIrcfuQBuaCnFu7ptPJWCQYtUmCbTKuHqT6I-KAr9CRzbV6IVVeDoKHx5Y_eWVLwipH5b4B1l2aKlcsAxY4qyZ7225WhokAHNWd8jO4OXXflZXRZJaDb-QvaQeiyQY1xCDr-yzI_fVI9sA_MKGKQvZslM4olXckRg65qnjdSC8A4vLmcLNvnW9zseIgP_qTeU5ThhEeQhnbGX5URQmpdzmu9zgV6XtdAQvk-3Iyaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه نساجی برای فروش دانیال ایری به باشگاه استقلال دوهفته زمان خواسته تا درصورتیکه پیشنهاد بهتری برای‌فروش این‌ مدافع‌‌جوان‌ملی پوش دریافت نکند این بازیکن با قراردادی چهار ساله آبی‌پوش شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/25612" target="_blank">📅 18:07 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25611">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dp2XNW5j7l4NXLpN6HctwhE4e5Yqlt_p61Rcp5Ly0JFl_2C1L-jtJnVuCh1oVDm8GNVBTtqmTaA2CKhG9MTw8V1J1oKwpcVny8yXTTwNBxV0MyvSkiQYBto9j4DuJxA5lpDvthHeDuYJ2It8H3SqhYrN26u2otrsMT7X8MPJXe-Ley7EvFhmJvzgWMXWZdrKYKEhGrVkwKDWdIPDZYVRDHMECQ1eZjeDz3Ba5NfkknRyS_0yN7CBj6ytBPsUMBrNqfWs7cCSVzOWbdr8cw5LLVUgEIWOznmMLmK4IYoa-9FHgq7ziFv0owSFNLY3L1Hyl6KE4RHkVjsE-2K0V-Fjdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
مهرداد محمدی وینگر سابق استقلال و تراکتور؛ باعقدقراردادی دوساله رسما به تیم فولاد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/25611" target="_blank">📅 18:00 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25610">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sok9FCO75kxYHWaiVyW--vxYwRwAYhJ49g6glyZ1pJZi9CeENMmOpwTqgzhL-YGMBITJ5mZ_fMd317hblAHEfn-HUyqvqgPVqEvDeaHSQ4q-OAungsDv43KvdDSJFpEiSQF1ZQYgw09nXihajO5ibQMCg8HHnUg6BTh2wxdBgdQN0ylPSyNRRQWbcDd9nsMoJMy4_yiVwTq6PyxlskGumc2GNPzczbivixBR7B98cUYOwEWAx_uho7piU33ZO6uu_i1KxLvch-sKona9QBhhvGcrkGWwKHKxhJSB_xJgc56OjqXbeBPUjh_rBtuwF5r1ZnShG8NP-ahPHxP2ttYBzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
محمد کریمی هافبک طراح سپاهان قرارداد خود را به مدت‌یک‌فصل به ارزش 65 میلیارد تومان باطلایی‌پوشان تمدیدکرد و در این تیم موندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/25610" target="_blank">📅 17:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25609">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QoLkz9cb4o2ZKqeG-6PI4y4N9af24jD8kSG8A9sRgXtFHbf-I4HsFXHFHcXVeUU47oMnxFUTEnImdKgITuVf3PB4HDV890f6pkB5J71Nl36-lHK4_C4Xbkoo_QgDZV2bRuImzZD89eLy3jKSZiKQK2-AUN7bXl0rNXYtkfKDnsqSD5ADcYomrVtBh798lV38czrBdCZPvSaMxcTw6d9YvoVE2NHyN6KZK7o_76wwKEkawYcbrMYWMM8qIf0ueGoeDBXnjkAvSBtLbp7OfsgTm4RUhzaR0igCRDluAtGOFRMLTgbQ-uWYDh0jtIN0cEzb1lez5vivlcnfP6ZC5K6alA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه پرسپولیس دو هفته پیش با ارسال نامه ای خواستار جذب فرهان جعفری هافبک تهاجمی 20 ساله ملوان‌انزلی‌شد که‌درکانال گفتیم. باشگاه با خودِ جعفری به‌ توافق رسیده و توافق با ملوان باقی مانده که باتوجه به‌فشار بازیکن به باشگاه در روزهای آینده رضایت‌نامه این…</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25609" target="_blank">📅 17:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25608">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f9-xqxwXtkoUkGyiEEKeiHR5lk-7_D24KmhSo14asHpQ5Fudvq6qNvr_V6F07BwRqrFz5aMUC1XJdk15Z4ZxsWCfS636FAX4cj-zpR1pCpMuFat2v9R1MOlI5oGslKp49uCAR8D5gmbNpxYefdTiK4A6WINu_CiXuB3p4f5gCUNiyXd2KQ0EfEJLZhH6Du-lazNrASW83cmduUAo2WH9gKpSe4wPqS2CD7KtNir1Xy7VP9iSpW9yB7u5Rcx11gpO3pvRtJDNEw9xS-fM5PM8bMWCyMHXf1mVQKTCXgLKOb7IJmTgQ9GI0S64IVFk4hwJhwpFFpQdy6DsTUj0xw4ZGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇫🇷
خریدخوب انریکه‌برای PSG
؛ لوکاس دینیه مدافع‌ چپ آستون‌ویلا با عقد قراردادی رسما به تیم پاری سن ژرمن پیوست. آستون ویلا 10M€ گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/25608" target="_blank">📅 17:13 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25607">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vMMBr7CZb6pMlnZTYhUe99LwatFfCQXXJLZFULRtU2z5D76RfDGE8ipui2vQftebRzBJA3c-XAg_0Xsk31EOPa06R4gcR5ikMpKURajgGqQoLJsO3-_g0SgpRSdebJkIggTU0PrsEzKJOcKx6YSBLCBv8YRGVRb3ZCC0F6ROfScrTrzfl-eHMR_Hirw3SgxbHrggSxcqweRgV6DE6ZCXRaSeJYIcQsZOg7sOB5kAmOzlrRDmdespRw9giCy3HLFGCz76tGOmToGROx7j1ciQTQllufJWA8A8lOPAPfyHwgUqsQkHwIJYsUAARvzQ29IaQReNPY6magR6MWDI6Zd8Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
#تقویم؛ 5 سال پیش در‌چنین‌روزی؛ ایتالیا مدل روبرتو مانچینی دست بکار بزرگی زد و قهرمان یورو شد. آتزوری بعد از مانچینی دیگه روز خوش ندید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/persiana_Soccer/25607" target="_blank">📅 17:07 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25606">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLIcq_p0a6onMqOfvaWbiNxyLw2SUp21bycfo-LksdTtfUxIB0-9vyYhkT-NjS_DxPLFdrfrb8CUPWveuh0NXjYQj8GD6wWWk6guZ0w1JJuqI0fZ3oWmDYkiTQ5mfe-zj1OtdRiJKjXV5wJw7nj_m8GC79AUx9sQ5n3l0CJ59ZjdqPyDGNCyZe4MgJHUHYBBwwgx0Xkm8fDezVpxdp5mb62NsWhhXKLq204GXS8F4IAc8c4rtKfwEShEEc_4uSPnEgF7SLpy_P7_86JB1cm7IC3QrOcpplzaEarbQyiKRMLxRJlv7IX4ijGNmT4CWQJKwMbuhQqAbHz31EUfgi5c1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
پارتنر جود بلینگهام ستاره انگلیس هستند که قبل از هر بازی حسابی به جود انرژی میده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25606" target="_blank">📅 16:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25605">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EnaZ-_c4w7mlGyo39IuvMtryV_1u4Xz4KaDukUFeKdTq6CD_pZWc1sKuiOSZ7ByQLH2598M86-QQeMtWn9E7eTpFx0BqmcqW08f4mLsBZ95TfJaXDzwtFWKw2C0tDjdydEPqqeVY99Kk_X6ncjf20pSGppts677zca7zDQpP4srwjroMQdn140_S5LVXSJgnXFKuBqcGoehb2_XJcXWf3NCMUFPd_TRg_TRNKC9mQj30NMVcCKuzKyYrPtxaB1IyMe3jIdl2e_brxIHYMU7GvPr_RmTv0oOvZpOL8yNBE4LhP3fPK-vyhRH0C54xiWQONFb_1UjckLXQd37j04ADiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علاقه‌ویکتوریا همسر دیویدبکام به فوتبال کاملا درتصویرمشخصه‌چقدر زیاده:)از سِر الکس فرگوسن پرسیده‌بودن‌اگه یه اسحله بادوتا تیر داشته باشی به کی شلیک میکنی؟ گفته بود آرسن ونگر و ویکتوریا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25605" target="_blank">📅 16:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25604">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uc7brH1URCeuyNKL-OEFElU5GsvVUlT-SU_Uy_Rjh-7a7wC7f3wsoFUDo_5IIHkusEqyIglEm3fMYK4QYOTgXGXZXjDF_AenYptmKrcAtWjocYbx1_lAHgN8n9qD3yTTxKKWWBZ5R47-cWEl50Qa-fn4D6mJCsa4vAdE-9R4VvSDPoYF77i4QFn29sxRkuDpPsMmP0mKLExtmI4uRL4QE7qB38oO9J6H5JWAZPKd_DwU7waRhHUdyMUSOxafeF-JB3cGS8Cq5Rdw3Ux9mcVnYZXpVG2hC7wkslEwGz5W4IYZu8U5V1G2U1wU02jHAp4QHlDPPRKMcLc0VJmCDC9prg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇧🇪
خرید خوب‌کریک‌برای‌شیاطین‌سرخ؛ یوری تیلمانس ستاره 29 ساله تیم ملی بلژیک با عقد قرار دادی چهار ساله رسما به منچستریونایتد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/25604" target="_blank">📅 16:23 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25603">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CpLRYPxvPh5B9VIeKUHjqFdlFqld6eH3-CdptxuWw13dSvDqWCWT37Sn6Yo9v9VsuD_40AWRRblYrSy_p7h_2JjHtCX9xauzfXniGfQQiCcCu8IyFjcVUnEWlIr1kKyVxXdfp5cnXsH7N32mfM9PfTlklSUy-NjDbW35G7IKQyQ0E09HOPoWnh-9sQKN8nyOxEc0c6aOPs-Ag5SvJ0_5NXllimD-135c0pOIKMUQmISro_TrIZskbJTrHid4BiicLAEs4SvJoNwP8wHhc5GScHg7j69RyjjmpVY0qFLhCKo506nee5hhee6d7UhKSfgFrYTZBk2oy_x0vF_tGBbmDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق‌اخباردریافتی‌پرشیانا؛ باشگاه استقلال برای تمدیدقرارداد روزبه‌ چشمی کاپیتان 32 ساله آبی‌ها به مدت دوفصل باایجنت او به توافق کامل رسید و بعد از بازگشت به ایران قراردادش رو تمدید خواهد کرد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/25603" target="_blank">📅 16:17 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25602">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XZUZFb1nHdPjQT6fBwLBTaulS5N1T9B2DcstWsDty7gicXD06W_9WxcNFTg10FXNHCWzl62LguFDHpt2_MPdPbvT7FAWvZTcgWdlAv7tAD1eZ6NGYGG2v679-dBx_pTSEW4uy4kcBzfzOB_2ZckfbzDCskSXUuI1qlZ8SaMLRvm5GigPjuKg_x7F8XDHYe5NORIS6X2WlvnPtQ8vRNR699GAugoUcAAHWd-Z13uSSfFZIZI7ZCeT5cwnDKPySwLSnsaa6yBOabs6vTnDw5DgyWclaTghegknMxaEGvkbfz3ztJj1bTC4VdusUwJmXke_9e-JuJhuuRbsR1OGis4cnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همچنین مهرداد محمدی جدا شد.</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/25602" target="_blank">📅 16:17 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25601">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">📱
دیگه وقتشه دانلود از اینستاگرام و یوتیوب رو بسپری به یه ربات خفن!
🤖
👑
هرچی بخوای فقط با ارسال لینک برات آماده‌ست
😎
👇
📥
دانلود پست، ریلز، استوری و ویدیوهای اینستاگرام
🎥
دانلود ویدیوهای یوتیوب با سریع‌ترین حالت ممکن
🚀
بدون دردسر، بدون سایت اضافی، بدون اتلاف وقت
✅
فقط لینک رو بفرست
✅
فایل رو تحویل بگیر
✅
به همین راحتی!
اگه دنبال یه ربات کاربردی و تمیز برای دانلود از اینستا و یوتیوبی، اینو از دست نده
👀
🔥
🤖
لینک ربات:
@instafilerrr_bot
📱</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25601" target="_blank">📅 16:17 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25600">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QidipM0qEtNptXTxpe-_mAiHyRUPe3KkqBaIv1Bi6U98DSdIhY_aN72MdlHoy8UGz4I6Dgk4DlQl1f9jZ_fclC6zC1JYkFsSAUfmjOSbjrf7qgQ5p44nahZ_kH2NXJemNyYqFPqM80Kg0UxNrTfQL50HjDwvkfa6c8F9towmvA0PH0_sJLkOko2epZ9yzGjCg0fkHEUilSh_O9_Jw2R-e8aKxi22vXkVZzsgmGL_Har9QDcVPCXkl6h0-mr1wxLCqeV4diRYj-8OG-4tbKz7qOe2DUVjJC1xJIA0J8sbti5PWrkEezICz_JLSU8djvN7LJMlcHzkxLIsnEc4VEYg2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
طبق اخرین اخبار دریافتی رسانه پرشیانا؛ امیر هوشنگ‌سعادتی‌ایجنت پارسا جعفری دروازه‌بان‌ سابق ذوب‌آهن او روبه‌باشگاه تراکتور پیشنهاد داده و عصر امروز جلسه‌ای بین طرفیت برگزار خواهد شد که به احتمال زیاد به عقد قرارداد منجر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/25600" target="_blank">📅 16:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25599">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a69b3302b.mp4?token=HC0KGwJnydzWbRSCWP1-Ghh89RSKoK3DyvU5lp5RyKwWCD5NZLA2PtItT8QDVmoNOBtfOJaeNMbL_kPrncELClnEk-3bmK0MeBkCQKUWfRG8tevs5xNMHO1YbHq3Q-VsKK3QVhj0lgJeaGEV9Lf-ZkEnpxqupvpk-ssZ9cnxd5agHw08Bdv7bQDBV8c71DI6NvARosPo-6KrnD4Vsbu629h1VIxF-kVGJrML557sGwEggDRtP30za8VLmeE2BqGdzolHAJUFSaaaNTpmGH-EqBHYALOwnvkdWAIDnNxjW-QAMw6tIDBiVCMN4hDbIqSQHrVW6N07DpYAc3YAS1lagg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a69b3302b.mp4?token=HC0KGwJnydzWbRSCWP1-Ghh89RSKoK3DyvU5lp5RyKwWCD5NZLA2PtItT8QDVmoNOBtfOJaeNMbL_kPrncELClnEk-3bmK0MeBkCQKUWfRG8tevs5xNMHO1YbHq3Q-VsKK3QVhj0lgJeaGEV9Lf-ZkEnpxqupvpk-ssZ9cnxd5agHw08Bdv7bQDBV8c71DI6NvARosPo-6KrnD4Vsbu629h1VIxF-kVGJrML557sGwEggDRtP30za8VLmeE2BqGdzolHAJUFSaaaNTpmGH-EqBHYALOwnvkdWAIDnNxjW-QAMw6tIDBiVCMN4hDbIqSQHrVW6N07DpYAc3YAS1lagg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
علی رضا بیرانوند: یه‌ روز طاها پسرم گفت بابا دوتا اکرم تو رو دیوانه‌کردند. یکی اکرم عفیف که همیشه بهت‌گل‌میزنه یکیم اکرم خانومت. منم گفتم اکرم خونه خیلی خطرناک تر از کرم قطری هاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/25599" target="_blank">📅 15:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25598">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YufAfD8F9RbsXULZULStOnhbNr0GeBElBudWnEuF-hw_ZkVyQ1_g6E-FpVjSnL6mJgfDpQA_qrgml3SBOqqs60fHvYo4Jm_iiZBdpPuGWtgAPl4qXhIxsHUPYN8CtIowF7cPEQ_aDo1WwjMmvYB46VpxynMMmCR97-MpJUaAJIyhbzLK_RZVIpqYGvEqL-Ti8xv4zettHy2xQWkf1IoGHC18UoaY2CfRZO9l8Am1X5KuudUdfQtlhRQQfKIMPmBf6XQ_3wrNhtte3q9TllFg6IYOt6SFnBLpvLsSGRRk1OgrHV01a5IxyK94DdxgXzj7hZ5yzPE4WoTV2VtyJl8xow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فدراسیون فوتبال کرواسی رسما جدایی زلاتکو دالیچ از سمت‌سرمربیگری‌این‌تیم رااعلام کرد. دالیچ سال 97 دریکقدمی‌پیوستن به استقلال قرار داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/25598" target="_blank">📅 15:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25597">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tibtl5QF-B40RY-j0X65pnxi-NhTl9dBmxUdsB9pQqZpqQshps35rllHq3zCDryO47gZltx4kJ82-ulz9tfpGRlnu-8DvQ9mSlQzNbFmHJ73IRhe0sFy5Nh9lskOPvynF7qW2zJDMJ1Gskad27KzPmPgbnepJwbrwH2r739_Sc9XLdNi5PAdo5TvoPhMScOkiZj0XI4lTvSu4FvadhyN4XFCc5lukngBaob1il7zpc0EQr0L-A4SckgL8ocOD8D_ildXzECA7H_0hJ_9C_KjyhKyzaJuaGtKD_pm0ayhV5RDHwQsy4pMpUOFSmM4Qvn5lwwHGmJtvrqin-Y_E-En1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◽️
👤
محمد جواد آقایی پور 26 ساله که دو فصل پیش سپاهان برای جذبش 100 میلیارد تومان هزینه کرد باعقدقراردادی به نساجی پیوست. آقایی پور در استقلال خوزستان فوق العاده بود اما بعد از پوستن به‌سپاهان با اون رقم فوق العاده سنگین افت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25597" target="_blank">📅 15:20 · 22 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
