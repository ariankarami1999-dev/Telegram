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
<img src="https://cdn4.telesco.pe/file/Hvpr_Q44tgiHuR9qmbd4gTcOw-QR_Kp4XkfnFpWhnjLi1nzgIoI58xuIzBZl4gVeWAPYuCVSciwmy6a_KHxQLa_1VKpNyqPdzF4Rg93ONN46p0w7F0vRQtdMYsc87BH6UeXXLfgzTvf386FOcx9zqGWlqXySvKprXJjWU89C0mp5RHxQfImLCLDFGZCJVOEPHlyCOjwkI2X_G5EtvvoGnHSf0p14ud-hBnkK8cajbTYeDNbeyiiYYg0Fsbj2--fjdeZwHmI7dwgLd_JZelhZ_eYVW8zoepXkuXnrbdA_unlFUnX1wXK3CNsYNZx4Wh2vwy58LrYXx3kkIsEEgW4ajA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-11 21:34:41</div>
<hr>

<div class="tg-post" id="msg-466102">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce2b222702.mp4?token=EKgJduC0HOclTv3xuP1c-ue7Doa3yjzV49A5XHnkzs-ar6fiVd0QHAQOIXWIRJhDflelCdp5_7IcrTT8T4E0jsUOtBLtxoqZ5TqE0HRd7LUqhicu3glAbqAeRYp3y0C375ZYGQoR9Spc6j0rQqHRKFQ-WrzUrzwXeMmgNAD_WIx0LI-U29EoJYUUzP9tnbXTe3sUG7rcEKFV8kdILlS9I4p6jnSp5HtVzMV0mwV5cb-YVwMJVYrxslwNU-ov9p0fMxuNe60dAX1BkerL2u6lMHATyDLC2NWllb041ZDKBaZgExAnemC8BDFFlM_QbjiZxOay1M8blK6k6Ef70k55UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce2b222702.mp4?token=EKgJduC0HOclTv3xuP1c-ue7Doa3yjzV49A5XHnkzs-ar6fiVd0QHAQOIXWIRJhDflelCdp5_7IcrTT8T4E0jsUOtBLtxoqZ5TqE0HRd7LUqhicu3glAbqAeRYp3y0C375ZYGQoR9Spc6j0rQqHRKFQ-WrzUrzwXeMmgNAD_WIx0LI-U29EoJYUUzP9tnbXTe3sUG7rcEKFV8kdILlS9I4p6jnSp5HtVzMV0mwV5cb-YVwMJVYrxslwNU-ov9p0fMxuNe60dAX1BkerL2u6lMHATyDLC2NWllb041ZDKBaZgExAnemC8BDFFlM_QbjiZxOay1M8blK6k6Ef70k55UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
محل‌های استفاده از طرح «تورم صفر» شهرداری تهران را بشناسید  @Farsna</div>
<div class="tg-footer">👁️ 996 · <a href="https://t.me/farsna/466102" target="_blank">📅 21:32 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466101">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J7ikMJxSPAt0JOpOa5A1VouVst3hjbl8zNUWB6XXPeLjeEs_WRizT0rVpTE6aJgu4_jBPrFyun7QjGPY3wzzVJqWhA9tblDWRR-tvtlXUx7h02NiaxYvNsVM5zZHsBX-0JKWWV1vniEyRnjMx1WouZm62GCMu0XYkgE9HRInT6hCxXQYrfD2044TF29BKlU7ZPoM40xdaiRD8RCceKCTguOAlsjb5GTTsn4fZS56t-bCJiTU7zfPNT24Hp1gtb_D-NNX6_VC25Y00qlj3rFSLSK6zxZPpN7gj2AzvYywc70MfactDtHV6EYMDBX2ebIH6ExQY7ACM0K8QopN4kSefA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
نتیجه‌ای عجیب در لیگ ملت‌های اروپا؛ کرواسی با ۷ گل مقابل انگلیس تحقیر شد
@Farsna</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/farsna/466101" target="_blank">📅 21:28 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466100">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">انهدام تیم تروریستی مرتبط با سلطنت‌طلبان در فارس
🔹
یک تیم تروریستی مرتبط با جریان سلطنت‌طلب در شهرستان نورآباد استان فارس توسط سربازان گمنام امام زمان(عج) شناسایی و منهدم شد.
🔹
اعضای این تیم علاوه بر تبلیغ و تحریک به خرابکاری، در حمله به زیرساخت‌های خدماتی و تخریب اموال عمومی در حوادث دی‌ماه ۱۴۰۴ نورآباد نقش داشته‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/farsna/466100" target="_blank">📅 21:25 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466099">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XnHeAMZrYL_NG0kLn3qkt9NwjsFUtwcqQZMYJm-K7j58ZVy3AYsau7_IiKNhO8XfhQ6O5dohbu0kmLLcdMjRAnW7IRKfK1b2knWYGY4j1KyKpTEu4rT0XT-SqoEunJFn4q880HRuUAHG2rSiqPp0dov1V3j7nmgYs4lkpzEUkUt89jUl7C-m67mOZqJT0-ouE5imljYiYGIQeEFckf2Y64RzsRZ7MQs2g4PKP_aIVl9I65AAHamghepTi9qiELa3BpoZNOFXXZX34UNMDsi5p5w9cm9eCaFxWXGajXjQ6XIoY26zph7chqay8rfNR-EtSSej1_Hj7SlPBKxeZ1UqUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واعظی: اختلافات داخلی، دشمن را به طمع امتیازگیری بیشتر می‌اندازد
🔹
محمود واعظی، قائم مقام حزب اعتدال و توسعه: دشمن بیش از هر چیز به پیام‌هایی که از داخل کشور منتقل می‌شود توجه دارد، اگر احساس کند میان مردم شکاف وجود دارد، جسارت پیدا می‌کند و به امتیازات بیشتری فکر خواهد کرد.
🔹
نه دفاع از کشور را جنگ‌طلبی بدانیم و نه مذاکره را وادادگی یا خیانت تلقی کنیم.
🔹
دشمنان با برداشت غلط از وضعیت انسجام اجتماعی ایران، تجاوز خود را آغاز کردند. آنها تصور می‌کردند طی ۲۴ یا ۴۸ ساعت به اهداف خود می‌رسند اما ایستادگی نیروهای مسلح و همراهی مردم، محاسبات آنها را تغییر داد.
🔹
مثلث بازدارندگی بر سه ضلع؛ قدرت و توان رزمندگان، حضور و حمایت مردم در میدان و خدمات دولت استوار است و این سه ضلع، ظرفیت کشور برای دفاع و تأمین منافع ملی را تقویت می‌کنند.
🔹
گاهی تلاش برای حل یک اختلاف، اگر با شتاب و قضاوت عجولانه همراه شود، خود به اختلافی تازه تبدیل می‌شود.
@Farspolitics
-
link</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/farsna/466099" target="_blank">📅 21:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466098">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b171e0ba8e.mp4?token=Kwa4rJX9gVzkBkudHjgM3j__1gqQ_WL4zpgmcvgpxRJOwe-yGY6S_cXAgAV-UnpwWy-WEewLoAUXalJjM1H214XMGasLW3oW9FD5Gw1qwyUp8ZnPBsW3CEQEQeyKiZCCne1ie21CyEWHf43wrRMF4Y3lKfbvCQEFHoy0rRDXrqpvWY5FYJU3FWC6JiOIjcUHlPE17s6Zp4UGfpvzRdSG8z8lpxMBugHOy-0hLuvIPROuF8VTw2VJDM3-EYoVOl5VBT1EKjVkB3JN6IVQD56mOIb_B6-cHkXZnmyEDX1xZ8CyxbWzAzUe-7uuEwCf8pFI40VCFKfLJBNJUonwu7T2-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b171e0ba8e.mp4?token=Kwa4rJX9gVzkBkudHjgM3j__1gqQ_WL4zpgmcvgpxRJOwe-yGY6S_cXAgAV-UnpwWy-WEewLoAUXalJjM1H214XMGasLW3oW9FD5Gw1qwyUp8ZnPBsW3CEQEQeyKiZCCne1ie21CyEWHf43wrRMF4Y3lKfbvCQEFHoy0rRDXrqpvWY5FYJU3FWC6JiOIjcUHlPE17s6Zp4UGfpvzRdSG8z8lpxMBugHOy-0hLuvIPROuF8VTw2VJDM3-EYoVOl5VBT1EKjVkB3JN6IVQD56mOIb_B6-cHkXZnmyEDX1xZ8CyxbWzAzUe-7uuEwCf8pFI40VCFKfLJBNJUonwu7T2-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موج افتخار از ناگویا به تجمعات تهران رسید  @Farsna</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/farsna/466098" target="_blank">📅 21:13 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466097">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9266b5859f.mp4?token=ZFGZFCNIoibLHeydx3p4__ulj9NMygZpEJtvZQ1gq3xCR-V5CTSGjz3t58Ne9Y-hNghiktr-B5gea3SV4q76c47see9wjGSTOMsUO4-SvFMPE91772F-yxtUKif0DY8d2LTL-jWe65MHjClYktfqOHT-GZ2vZNYJIDkZUM1qZc6fvICGTH7sZYS4qtPKRC4xetki5goS-S78fHxXs3afkkzV4YQEeByE51HQR59TllcBq-qFNf_-dwMOpvBmSksiKh-udfmOVmc8oK1zM3sGB7Bra7vLx2FvNVnW1pvRO3Ay6c1MEHJRZ2nK_GDQn5F9R_mlCChf1l3iCXVQZoFBNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9266b5859f.mp4?token=ZFGZFCNIoibLHeydx3p4__ulj9NMygZpEJtvZQ1gq3xCR-V5CTSGjz3t58Ne9Y-hNghiktr-B5gea3SV4q76c47see9wjGSTOMsUO4-SvFMPE91772F-yxtUKif0DY8d2LTL-jWe65MHjClYktfqOHT-GZ2vZNYJIDkZUM1qZc6fvICGTH7sZYS4qtPKRC4xetki5goS-S78fHxXs3afkkzV4YQEeByE51HQR59TllcBq-qFNf_-dwMOpvBmSksiKh-udfmOVmc8oK1zM3sGB7Bra7vLx2FvNVnW1pvRO3Ay6c1MEHJRZ2nK_GDQn5F9R_mlCChf1l3iCXVQZoFBNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ایران، بالای بچه‌پولدارهای آسیا قرار گرفت  @Farsna - Link</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/farsna/466097" target="_blank">📅 21:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466096">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbfbb2d99f.mp4?token=APVDAjYHzrloQYMGxb8nnU0B0hdhfRbaRLX5saiE1Oig3WWVafYxw9bffixj0Q1q2q-Bznxj8DaiS_YhBvPon_V2zxuGTvOK7hWGfkjXLBO9CalkCbCQmf23wZpITXsERqEjLCClvuYs-asCYbq4dvfWJxMRLmM_5ogx1WTKn4h8oUEnzJh-YR7zJRsytBKY-U7cxTGmJLZNgPzZjREbX1S6LJxM8YZ3tq_r4Eai6hOj82rzR-mjHxQT7kxQsqB0rC1NsHWWZy1DlEj31ukNKlsCp-ytk9KCQXKG-Fa7aQoWRYs5G1O8ElEdwYblQU-UN6rY2ordHHty30RpE_O56g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbfbb2d99f.mp4?token=APVDAjYHzrloQYMGxb8nnU0B0hdhfRbaRLX5saiE1Oig3WWVafYxw9bffixj0Q1q2q-Bznxj8DaiS_YhBvPon_V2zxuGTvOK7hWGfkjXLBO9CalkCbCQmf23wZpITXsERqEjLCClvuYs-asCYbq4dvfWJxMRLmM_5ogx1WTKn4h8oUEnzJh-YR7zJRsytBKY-U7cxTGmJLZNgPzZjREbX1S6LJxM8YZ3tq_r4Eai6hOj82rzR-mjHxQT7kxQsqB0rC1NsHWWZy1DlEj31ukNKlsCp-ytk9KCQXKG-Fa7aQoWRYs5G1O8ElEdwYblQU-UN6rY2ordHHty30RpE_O56g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پدافند هوایی نوین نیروهای مسلح کشورمان در قشم موفق به رهگیری یک پرنده متخاصم شد
🔹
مردم محلی می‌گویند در جریان فعالیت پدافند دست‌کم یک هواگرد در آسمان قشم هدف اصابت قرار گرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/farsna/466096" target="_blank">📅 20:53 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466095">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e00f18bbd6.mp4?token=rQfTH3aKJL9Y33FyBeX-QOg4JiP6RKm7SENd8SQsafSIrLEoNhTdP0qi-nM9acEWWkaMMyrXdnzc_WPCW7gefHWWtpraEDB407AmeeXbPfd1WPJD1C8rN6oVbJZUrHARRSwY_Eiyp1NVZlqCbHk6yAiFYhi_3WzX_p5qhvG2Le13EA57orV_r1sWWeVdD5Trw_nY56XZH1gE1WU8ToXbXZEvdfXdz-vsIQtoK38fiPYZvpRhEhw_mQcXpVn5eZkRtYhak2fWVL93s-rHlGnTnaYGJrV51oFBqlxxcG5GxdGO0wRNQ3LggXdFuDYGKHNED-7v4i3-wDSXaoCg7lI3Fw6hQyfBNbQlZEdBD5K5TgxIUfNo1LAYDHaX6oUlU9kNKMc5o9cYdAiitBACaSaO0oJh572_qzFhmJATWTyoHm3_GTrwkGRJluSgOrbg3sTF1f3PracH2AXsOG4Wlv6YTen3ypck4vh1J-hj-kwKxgrdGv0oP_ZHfE_wE0OCtb3zIYCqy4thJ8RUZGMu_MEn6LMiq8sOzun9A13fb_tAoL-w-TdBjnoujX8hHmUFgszpi9X77UMhIh3pybe_wIFn1N66RpW0GyCRhGKu9xibmLauGUz4w8p1RRPyFDFOaMe7BGE9DDPlIk8roTrxJpoIOJI5f8AEeBY0axGRE_8PtBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e00f18bbd6.mp4?token=rQfTH3aKJL9Y33FyBeX-QOg4JiP6RKm7SENd8SQsafSIrLEoNhTdP0qi-nM9acEWWkaMMyrXdnzc_WPCW7gefHWWtpraEDB407AmeeXbPfd1WPJD1C8rN6oVbJZUrHARRSwY_Eiyp1NVZlqCbHk6yAiFYhi_3WzX_p5qhvG2Le13EA57orV_r1sWWeVdD5Trw_nY56XZH1gE1WU8ToXbXZEvdfXdz-vsIQtoK38fiPYZvpRhEhw_mQcXpVn5eZkRtYhak2fWVL93s-rHlGnTnaYGJrV51oFBqlxxcG5GxdGO0wRNQ3LggXdFuDYGKHNED-7v4i3-wDSXaoCg7lI3Fw6hQyfBNbQlZEdBD5K5TgxIUfNo1LAYDHaX6oUlU9kNKMc5o9cYdAiitBACaSaO0oJh572_qzFhmJATWTyoHm3_GTrwkGRJluSgOrbg3sTF1f3PracH2AXsOG4Wlv6YTen3ypck4vh1J-hj-kwKxgrdGv0oP_ZHfE_wE0OCtb3zIYCqy4thJ8RUZGMu_MEn6LMiq8sOzun9A13fb_tAoL-w-TdBjnoujX8hHmUFgszpi9X77UMhIh3pybe_wIFn1N66RpW0GyCRhGKu9xibmLauGUz4w8p1RRPyFDFOaMe7BGE9DDPlIk8roTrxJpoIOJI5f8AEeBY0axGRE_8PtBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبر درگذشت حجت‌الاسلام قرائتی نادرست است
🔹
پیگیری خبرنگار فارس نشان می‌دهد اخبار منتشر شده در فضای مجازی درباره سلامتی حجت‌الاسلام قرائتی نادرست است.
🔹
این استاد بزرگ قرآن هم‌اکنون برای حضور در اجلاسیه سراسری اقامه نماز در مشهد حضور دارد. @Farsna</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/farsna/466095" target="_blank">📅 20:52 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466094">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FfX8YdsD1lSXuVPMOd4p8J0Qnr_a-tfL1o8u1yNSeoJyDOxehuT_VgTuZ0BdRT9235ssqxLwKu13Mdy-rnm51zteT9czuxesTt0KLktHmCmWmJ9PZHjOHEIeRTqfOn8p3VbkhczFkw2_DxW1ywXKfzSX5vTtY2VKqdgHaQ7OsIWM_S4B1YR0h5J3fvBzKa3lnGAB6cyAyE9PTpbZeB4fGJD1z6uWQptztabcjxUAkTRakXtffK7Jnz3GBC-7dwOm9yphVaMg91YvZ3i80J2HFYsjOy6DdRX_C2mVioOs3S6Y-XmSGhZjaQKLrGapCrHu3kEZOGFDdVRqtH57AeSSGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کورس دلار آزاد و تلگرامی در اولین روز هفته
🔹
قیمت دلار از ابتدای امروز و با شروع هفته بیش از ۵ هزار تومان در کانال‌های تلگرامی افزایش یافت و به حدود ۲۶۸ هزار تومان رسید.
🔹
همزمان صرافی‌ها و دلارفروش‌های اطراف خیابان فردوسی نیز نرخ فروش دلار را بین ۲۶۵ تا ۲۶۷ هزار تومان اعلام کردند.
🔹
آخر هفتۀ گذشته قیمت دلار در بازار ارز فردوسی حدود ۲۵۳ تا ۲۵۴ هزار تومان بود که نشان می‌دهد نرخ دلار طی ۲ روز بیش از ۱۲ هزار تومان افزایش یافته است.
🔹
بانک مرکزی از امروز عرضه ۲ میلیارد دلار از طریق بانک‌ها را آغاز کرده که در ابتدای عرضه، قیمت دلار حدود ۲۵۹ هزار تومان بود. سقف خرید نیز برای هر نفر ۱۰ هزار دلار اعلام شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/farsna/466094" target="_blank">📅 20:49 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466092">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb15d2d6d0.mp4?token=unDCTcMOoQol28p1Da_OkXVH6RR1wcyhkYq3zBO9SRnWWIiMkpHEfTMYSfsrHf89P_uPUI8PTpurz30iPRmY9vYmLbDRIucNvVxUIjBqjhl7my_tbJYLxb-sM9Nj2h8u2fMSMs--Nw4EKQsWNjz1UjSMamAzH2xXFl6IIKYT4fFIN-GAOierMsdQY4IPLBhm-XT1VjxOrnemP9MjTk1agJHPI4Te-R7zBhy-8k4elqwomm8JOSBYMOqjrSDmQJmNQ3YY4IpFNZ0rBzc0rdCfuFhG6P3_qoyW3jhSi0uzfCjNFfVOHI4tC4BOUCRmeZMtCbi_5V21Bk68VWsjlhCubQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb15d2d6d0.mp4?token=unDCTcMOoQol28p1Da_OkXVH6RR1wcyhkYq3zBO9SRnWWIiMkpHEfTMYSfsrHf89P_uPUI8PTpurz30iPRmY9vYmLbDRIucNvVxUIjBqjhl7my_tbJYLxb-sM9Nj2h8u2fMSMs--Nw4EKQsWNjz1UjSMamAzH2xXFl6IIKYT4fFIN-GAOierMsdQY4IPLBhm-XT1VjxOrnemP9MjTk1agJHPI4Te-R7zBhy-8k4elqwomm8JOSBYMOqjrSDmQJmNQ3YY4IpFNZ0rBzc0rdCfuFhG6P3_qoyW3jhSi0uzfCjNFfVOHI4tC4BOUCRmeZMtCbi_5V21Bk68VWsjlhCubQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خراتیان، تحلیل‌گر مسائل بین‌الملل: سیگنال‌های مذاکراتی تلاش یمن برای افزایش قیمت نفت را خراب کرد
🔹
پس‌از اوج‌گیری قیمت نفت با اقدامات انصارالله یمن، سیلی از اخبار مثبت ایجاد شد تا با «خبردرمانی» جلوی التهاب بازار نفت گرفته شود.
🔹
یکی از مواردی که بازار نفت…</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/farsna/466092" target="_blank">📅 20:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466091">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">آرایش جدید اقتصادی دولت برای مدیریت شرایط ویژۀ کشور
🔹
در جلسۀ ستاد هماهنگی اقتصادی دولت، آخرین وضعیت بازار ارز، بودجه، تجارت خارجی و تأمین کالاهای اساسی بررسی شد.
🔹
در این جلسه بر ثبات بازار ارز، هماهنگی سیاست‌های ارزی، تجاری و مالی، مدیریت انتظارات و تأمین ارز مورد نیاز بخش واقعی اقتصاد تأکید شد.
🔹
سازمان برنامه‌وبودجه نیز یک
بستۀ پیشنهادی ۷ ماده‌ای
برای مدیریت شرایط موجود و عبور از محدودیت‌های پیش‌رو ارائه داد.
🔹
وزیر کشاورزی اعلام کرد کمبودی در کالاهای اساسی مورد نیاز کشور وجود ندارد.
🔹
همچنین پیشنهاد ایجاد ساختاری چابک‌تر برای تسریع تصمیم‌گیری و اجرای مصوبات اقتصادی مطرح شد.
🔹
دبیر شورای‌عالی امنیت ملی نیز اعلام کرد شعام آمادۀ هرگونه حمایت و همکاری برای پیشبرد امور و کمک به مدیریت شرایط اقتصادی کشور است.
@Farsna</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/farsna/466091" target="_blank">📅 20:36 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466090">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IPPfIXG__uTdNrw0kO23H6XBq9iv5m6gqrUQrilncTOdDMMVtJxcmWZ4BaZTuN8yenN9gbuj_wasrpVwAObSRD5FEAVZxAqxyMbHqidJuN3s4Hl1UMHX6pq3lo7ZY0nJmrMuQRndFz-lLRvsPFyodFgU32iPUlLuO40b79wHieL0qy40ZGtFfLlTGgW2tetLffvfCgd2oQK9ZuSxV65UxpDgVK1U3nloteNXnfLXyHIbaK7BU7PFH0oB0PjIV401QHHppb5gk80UU_Pjd5Jusfw4_MpAyGI-AUPu5VSCEtvdxyxZcx9koBO-MJB1poGhqPtCTI3ZETiyBmFSYMBIdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس سازمان هواپیمایی: پروازهای ایران و عراق از فردا توسط شرکت‌های هواپیمایی ایرانی و عراقی برقرار می‌شود
.
@Farsna</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/farsna/466090" target="_blank">📅 20:29 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466089">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FgopmHtVSf16iR4gITfpiphHfiZJ_POEgxlrA_h3uvRToiMlYuiPkxm0DrLU4U1UTDIL3lyly7zNHao-vHdJaP3ReYEhL8B9mFOQlPROu6LKFjsqfWbsWeyXnzPZNerQGmi01WGJx6Od2NLsVhZ6k4CxKVp77sscLcBUnLnCjD526dOautNbXeQmzt00WYBFVAHSgWtuamPDdfkPMUMqTI5on9ZxBOZOikmsBMQp2UT38LXI59-oujB91RStcdEwcIJwKANmgwrqR_ZM7refOqQ2rhrfsJYg7BkZFM-WlgD1L9D48CGTK7-hJa5gBBHn4R-zXEXkj5_nkjtE3JqgeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دردسر دولت پرتغال بر سر پایگاه آمریکایی
🔹
دادستانی پرتغال پس از شکایت حزب «بلوک چپ» این کشور تحقیق دربارۀ قانونی‌بودن مجوز استفاده آمریکا از پایگاه هوایی لاخِس در جنگ علیه ایران را آغاز کرد.
🔹
طبق توافق دو کشور، پس از آغاز خصومت‌ها، استفادۀ آمریکا از این پایگاه به موافقت پرتغال نیاز دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/farsna/466089" target="_blank">📅 20:28 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466088">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91d70b79c1.mp4?token=I8XXentCHsKf75G5Rjoji8mpOYWyQ1SK-KHLjLynwQ-BvQHdB4OOOzG6lJz4rcGEF_zm3qciey6je34E2IsaR_yxQBHUY_NLUSSqvPIc2d_yacfPrzXP4VNqO9IA_tHe74qxEmYalWUTd3PyIbggrJpToe7hsvO7EYLy1e_ZxPfJFTkYEiGJtagj_0j_Donu9X2_NVMQqImTlTuFMCyZ4nBHZG7R42ke4LDewJKIJEZq9RRbO1y9o9WJ-yFng6W3hCEEmcDOEDtwPZeX-vNjc47Hbo078v6fgraLcBl77ip0PFmQEnNxWL8oen55d2WoavOTiTTDCBr36AyG8AX0ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91d70b79c1.mp4?token=I8XXentCHsKf75G5Rjoji8mpOYWyQ1SK-KHLjLynwQ-BvQHdB4OOOzG6lJz4rcGEF_zm3qciey6je34E2IsaR_yxQBHUY_NLUSSqvPIc2d_yacfPrzXP4VNqO9IA_tHe74qxEmYalWUTd3PyIbggrJpToe7hsvO7EYLy1e_ZxPfJFTkYEiGJtagj_0j_Donu9X2_NVMQqImTlTuFMCyZ4nBHZG7R42ke4LDewJKIJEZq9RRbO1y9o9WJ-yFng6W3hCEEmcDOEDtwPZeX-vNjc47Hbo078v6fgraLcBl77ip0PFmQEnNxWL8oen55d2WoavOTiTTDCBr36AyG8AX0ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خراتیان، تحلیل‌گر مسائل بین‌الملل: سیگنال‌های مذاکراتی تلاش یمن برای افزایش قیمت نفت را خراب کرد
🔹
پس‌از اوج‌گیری قیمت نفت با اقدامات انصارالله یمن، سیلی از اخبار مثبت ایجاد شد تا با «خبردرمانی» جلوی التهاب بازار نفت گرفته شود.
🔹
یکی از مواردی که بازار نفت را آرام کرد خبر «نشست تنگۀ هرمز» بین ایران و کشورهای عربی بود؛ نشستی که هیچ‌وقت برگزار نشد.
@Farsna</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/farsna/466088" target="_blank">📅 20:21 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466087">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b58d4866c8.mp4?token=SltbG-_NhuNHXRdSLcSBD7zXnVF3ojDrn_ku5ur0UOeyLXvkBkJasO6vqm2XFxzZEvR5hyzuDGlvj6pUs5wCAcLmz9LOVomiM1W7esyfkKtCfxk9jzmS_04K6Xh26qslKABXl0m4rqN-WYoKYc1HupRDVBp6TnCEwIfDGJb2Ot8vAT0pPHXdtI0I5DyfqDhVbYIshyua2oEKAC2a12kYQUCJ3fT3A_qpRjqYSFNR-f1-e7Tyxu89XbiEltP7m6dYHgSn9WGzsmThKa7HYFiinjyz6dltX2360i-mbm8b6YSrzwgVQQfqi--oha1Zrcs1kb0lGMFJ-sb-seqeZVnajg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b58d4866c8.mp4?token=SltbG-_NhuNHXRdSLcSBD7zXnVF3ojDrn_ku5ur0UOeyLXvkBkJasO6vqm2XFxzZEvR5hyzuDGlvj6pUs5wCAcLmz9LOVomiM1W7esyfkKtCfxk9jzmS_04K6Xh26qslKABXl0m4rqN-WYoKYc1HupRDVBp6TnCEwIfDGJb2Ot8vAT0pPHXdtI0I5DyfqDhVbYIshyua2oEKAC2a12kYQUCJ3fT3A_qpRjqYSFNR-f1-e7Tyxu89XbiEltP7m6dYHgSn9WGzsmThKa7HYFiinjyz6dltX2360i-mbm8b6YSrzwgVQQfqi--oha1Zrcs1kb0lGMFJ-sb-seqeZVnajg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سقوط قیمت نفت هم‌زمان با سفر میانجی به تهران
🔹
هم‌زمان با سفر وزیر کشور پاکستان به ایران، روند ریزشی قیمت نفت شدت گرفت.
🔹
پیش‌تر هم، سفر میانجی‌های مختلف به تهران زمینه ریزش قیمت نفت را فراهم کرده بود اما هیچ پیشرفت قابل ملاحظه‌ای در پرونده مذاکره اتفاق نیفتاد.…</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/farsna/466087" target="_blank">📅 20:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466085">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس پلاس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SfqNxQs6rn4gR_rDgcG6oKUJxPpZnNf_EwiVAzP0sVEH2DZZBjFtjg-GaLRIWHvPiQ7MhDaHC16ANTTfUMk9nnt6M9KCqcxyk7Pd0fD31E7xQn5Lvipel20ipReK5H0OApEvoQQp89HVhyktPy0wUVI0FsiRC534wUi1MaaS-e2pETeuNgaxdtnlS0WjxOTVh-h_M1I_cRrVTjde-OUoevUh0Hvg-OXz9pbc82Ik0FJ2lrpIjfbFmeauiHhMVHjE82FdWXWTfRQDJJ0RhenPNn4mN6sW3Zl0_fEgLJoYPrL1LvFwtlEJ6Pe_QE-QF1CV2-ELSaG98TaYb-oHHNp44g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله اصلاح‌طلبان به زاکانی به‌دلیل همکاری با پزشکیان؟
🔹
درحالی‌که شهرداری تهران طی ماه‌های جنگ بخشی از امکانات و منابع خود را برای کاهش فشار بر دولت و شهروندان به میدان آورده و اکنون نیز برنامه‌های معیشتی تازه‌ای را آغاز کرده است، هم‌زمان فشار سیاسی و رسانه‌ای بر علیرضا زاکانی افزایش یافته است؛ وضعیتی که یک سؤال را پیش می‌کشد: چرا درست در زمانی که شهردار تهران بر همکاری با دولت و کاهش بخشی از بار آن تأکید دارد، حملات علیه او شدت گرفته است؟
🔹
به گزارش فارس، اختلاف سیاسی علیرضا زاکانی با دولت مسعود پزشکیان موضوع پنهانی نیست، اما این اختلاف دست‌کم در ماه‌های جنگ مانع از همکاری مدیریت شهری با دولت نشده است.
🔹
شهرداری تهران در جریان جنگ، مسئولیت‌هایی را پذیرفت که بخشی از آنها فراتر از اداره روزمره شهر بود. اسکان خانواده‌های آسیب‌دیده و پذیرش مسئولیت بازسازی و نوسازی بخش‌هایی از مناطق خسارت‌دیده از جمله این اقدامات بود.
🔹
در همین مقطع، مترو و خطوط BRT نیز رایگان شدند؛ اقدامی که علاوه بر تسهیل تردد شهروندان، در شرایط محدودیت سوخت به کاهش مصرف بنزین در پایتخت کمک کرد.
🔹
این اقدامات در کنار فعالیت‌های عمرانی شهر در دوره جنگ بارها تحسین منتقدان و ناظران از جمله رئیس جمهور را به دنبال داشت.
🔹
در روزهای جنگ علاوه بر پروژه‌هایی از جمله اتصال‌های بزرگراهی، تقاطع‌ها و زیرگذرهای جدید حالا دامنه ورود شهرداری به مسائل فراتر از خدمات متعارف شهری، به حوزه معیشت رسیده است.
🔹
زاکانی هفتم مهر از اجرای طرحی با عنوان «تورم صفر» خبر داد که در مرحله نخست، قیمت ۱۲ قلم کالای اساسی را برای ۶ ماه ثابت نگه می‌دارد. این کالاها در ۱۰۸ میدان میوه‌وتره‌بار و سپس فروشگاه‌های شهروند عرضه می‌شوند و قرار است تعداد اقلام طرح نیز افزایش یابد. شهردار تهران گفته است این برنامه با استفاده از ظرفیت‌های قانونی شهرداری و همکاری دولت اجرا می‌شود.
🔹
مدیریت شهری همچنین از بسته‌های دیگری در حوزه حمایت از خانواده و فرزندآوری سخن گفته است. زاکانی اعلام کرده برای فرزندانی که از سال ۱۴۰۵ به بعد متولد شوند، حمایت ماهانه‌ای در محدودۀ ۳.۵ تا ۴ میلیون تومان پیش‌بینی شده است. او هدف مجموعه این بسته‌ها را کاهش بخشی از بار اقتصادی مردم و دولت عنوان کرده است.
🔹
هم‌زمان با این روند، انتقادات از زاکانی در فضای سیاسی و در میان برخی اصلاحطلبان شدت گرفته است. این هم‌زمانی افزایش فشارها با ورود مدیریت شهری به طرح‌هایی که بخشی از بار اقتصادی و اجرایی دولت را کاهش می‌دهد، یک پرسش سیاسی قابل تأمل ایجاد کرده است.
🔹
اگر شهرداری در روزهای جنگ برای اسکان و بازسازی خانه‌های آسیب‌دیده هزینه می‌کند، حمل‌ونقل عمومی را رایگان می‌کند، فعالیت عمرانی شهر را ادامه می‌دهد و در دوره تورم نیز برای تثبیت قیمت بخشی از کالاهای اساسی وارد میدان می‌شود، دقیقاً کدام بخش این اقدامات باید محل نزاع سیاسی باشد؟
🔹
پرسش زمانی جالب‌تر می‌شود که دولت مستقر، دولتی است که جریان اصلاح‌طلب از آن حمایت سیاسی کرده است. انتظار طبیعی در چنین شرایطی این بود که هر ظرفیتی خارج از دولت که بتواند بخشی از فشار اقتصادی، اجتماعی یا اجرایی را از دوش آن بردارد، دست‌کم در همان نقطه مورد استقبال قرار گیرد؛ حتی اگر مدیر آن مجموعه از رقیبان سیاسی دولت باشد.
@Fars_plus</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/farsna/466085" target="_blank">📅 20:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466084">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71a5ec1fd8.mp4?token=lTNN3AbKPSN665z3CXRO5qU4pbt4_GlGBCkCtv79kd5K4vUbDo2oTTHSO0t7b21h_3eINuqEBA7X8v6S2ekDSpB7W0aVNOO6MC29tZQLldF0RAnwvBnzoXrCbzb-3PFnnq7J75BknaYIjOr8izngLwslnZ9RzcR1HHHEsr_mAtfrZ4Hq1ykM1evpjb0DlYjaUUKFrRMEdptt6nnRLd3tPR-ys_n4NL4EdUon8zJShaF9TKxWxRe4q3gmYsuLlvpkQeRADV737_9dE_AG9MvUD1F59JHwfZNba5FeNQtQxOjCWqXcsIlTKpJd9eGXVvWvm2DxnkgdDqfTnllXpZfPQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71a5ec1fd8.mp4?token=lTNN3AbKPSN665z3CXRO5qU4pbt4_GlGBCkCtv79kd5K4vUbDo2oTTHSO0t7b21h_3eINuqEBA7X8v6S2ekDSpB7W0aVNOO6MC29tZQLldF0RAnwvBnzoXrCbzb-3PFnnq7J75BknaYIjOr8izngLwslnZ9RzcR1HHHEsr_mAtfrZ4Hq1ykM1evpjb0DlYjaUUKFrRMEdptt6nnRLd3tPR-ys_n4NL4EdUon8zJShaF9TKxWxRe4q3gmYsuLlvpkQeRADV737_9dE_AG9MvUD1F59JHwfZNba5FeNQtQxOjCWqXcsIlTKpJd9eGXVvWvm2DxnkgdDqfTnllXpZfPQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسوایی در کپلر؛ آمار نفت ایران دست یک سلطنت‌طلب
🔹
مسئول ارشد آمار نفتی کپلر یک ایرانی سلطنت‌طلب با نام همایون فلکشاهی است.
🔹
عکس پروفایل فلکشاهی پرچم جعلی ایران بود اما پس از رسوایی اخیر، او عکس پروفایل خود را تغییر داد.
🔹
کپلر پیش‌تر مدعی صفرشدن صادرات نفت…</div>
<div class="tg-footer">👁️ 7.26K · <a href="https://t.me/farsna/466084" target="_blank">📅 20:00 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466083">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c08f93b8e.mp4?token=GAZlABn6bqlXjKEj-w2sgMEiOa38GoMg619UhLi5t1i3X-aDyu1GBpKsShazATej1ucQAcm7eRrvCJYbnv89X5IAnOaCYtj6E0-CtW0RAOFzbaDAdrrjoMvtORtS3NDczEFsSQc7zV5q0I05Vw95o5rkYXPa0kTm47urup2WkYGEEAZR4lOHPSM91queTeLjog9FNNkdKb-KPO4w9zWV5Ro2P06GRB5XUMWfgStrFK3q2njPDdJDZGY4Yw40430RynL6Adv5OAk9hYfc9OiWjgBXkqnOItP-xIUhxPTESPJp4kEgdC6cUDYRtyVOtM9axcu7vwv8wu4Np7xd94peskJx6OiZzaolVqgLaPCGMwQDU-qG9DNO0TT820b949Exbuan3eq1htnr2Xo1kPaJnkD-W1xE-BOmu04eeeUWvlNHlvFB_El75ifIlFRVl-KcPiYrSf6BXvLU-uqp7pKd1QfXd6V9Wy4BEiuGBkXKiyOB5t3FG-UO4ncrxwbavXdYyYSzDKzyIe-HuhGO7J6Ht1PwmBkHQfaeln9uJGifzHltm8Hop90neHbB9AJ6HZfhQq3W1ebmyI5TgwXYh2sasGc0TZVRsrRLSZQiqZCC0EsIID6T05XrJRt0wR6nxKi2oo7d3teymqrh6Azqaew3Rmylu6VaYZ5DYsSg9ZA6Oi0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c08f93b8e.mp4?token=GAZlABn6bqlXjKEj-w2sgMEiOa38GoMg619UhLi5t1i3X-aDyu1GBpKsShazATej1ucQAcm7eRrvCJYbnv89X5IAnOaCYtj6E0-CtW0RAOFzbaDAdrrjoMvtORtS3NDczEFsSQc7zV5q0I05Vw95o5rkYXPa0kTm47urup2WkYGEEAZR4lOHPSM91queTeLjog9FNNkdKb-KPO4w9zWV5Ro2P06GRB5XUMWfgStrFK3q2njPDdJDZGY4Yw40430RynL6Adv5OAk9hYfc9OiWjgBXkqnOItP-xIUhxPTESPJp4kEgdC6cUDYRtyVOtM9axcu7vwv8wu4Np7xd94peskJx6OiZzaolVqgLaPCGMwQDU-qG9DNO0TT820b949Exbuan3eq1htnr2Xo1kPaJnkD-W1xE-BOmu04eeeUWvlNHlvFB_El75ifIlFRVl-KcPiYrSf6BXvLU-uqp7pKd1QfXd6V9Wy4BEiuGBkXKiyOB5t3FG-UO4ncrxwbavXdYyYSzDKzyIe-HuhGO7J6Ht1PwmBkHQfaeln9uJGifzHltm8Hop90neHbB9AJ6HZfhQq3W1ebmyI5TgwXYh2sasGc0TZVRsrRLSZQiqZCC0EsIID6T05XrJRt0wR6nxKi2oo7d3teymqrh6Azqaew3Rmylu6VaYZ5DYsSg9ZA6Oi0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وقتی جفری ساکس هم از ادعای برخی جریانات ایرانی تعجب کرد
🔹
به‌جز ترامپ و برخی افراد در داخل کشور، هیچکس از احتمال «سوختن کارت تنگۀ هرمز» برای ایران صحبت نکرده اما این عبارت هنوز از زبان برخی کارشناسان داخلی تکرار می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 7.59K · <a href="https://t.me/farsna/466083" target="_blank">📅 19:56 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466082">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ekJBzh5aDeRJz03sc8jbFY5c9DM5s1YM4qPxd-TQ8bjEeBSuuPZctLETQP4RGWjEYmIe6Pnup3tRVauDccx9TxYintBVPTTHdmM5bHcjr7UK6gkSAqiYli8agvqrQG-zI2ezAWpp0o1C9Y9A7lBAXX8f2RIW7AlDQWuexhDIpoOlupyuhg2eiA0UuANT8M7rDdl9pNi6cz-PUDWxE_ffhbsuYtAsrQj0QJpnWOhUz8u-c_AXnIUFoC96p4wmqMMRHkI1gXHkNMOg2WvH7CuDecfJRjYPZn6bOHb3X0-Z_NEdKl0BgCqz_Sx3phcwRSrx_YxSf20kDJy3XXj96c1A3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم حبس الناز شاکردوست در دادگاه تجدیدنظر تأیید شد
🔹
شعبهٔ ۲۳ دادگاه انقلاب تهران، الناز شاکردوست را به اتهام «فعالیت تبلیغی علیه نظام» به یک سال حبس تعزیری محکوم کرده و به‌عنوان مجازات تکمیلی نیز ۲ سال محرومیت از فعالیت‌های سیاسی، مجازی و هنری برای او مقرر…</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/farsna/466082" target="_blank">📅 19:51 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466081">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9685b35a01.mp4?token=JpoejihadRn_8K7fEHT4jnboXptRsZAQpRFkDwUCgd7rrJdhuy_d-Un7O8nNVGpkAsf1bfk31UHqwxl0rOXUG0ofLVyIPM068f3FKXUJ-ljJgg2PDpZbqWPo57TzTAiau3dxaR-3MMuXptpR2inH-ODCuoToSBgL9IEkyybGscKQ5lCryB9IREKFyytccHMXv3ZwHBZ_cqy6ShoEAwlW8pYerkeL8rFrr4v6lDd14Vsql-g8c1z3ZUDtdys632u_o8W650ELvcn4Z-vL8wbiQNzTg7479Utx2VsGk6c370nLu7LXTM2AXF9ip8FuuVCcSHUzv0dsrs3fz53jDcxirQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9685b35a01.mp4?token=JpoejihadRn_8K7fEHT4jnboXptRsZAQpRFkDwUCgd7rrJdhuy_d-Un7O8nNVGpkAsf1bfk31UHqwxl0rOXUG0ofLVyIPM068f3FKXUJ-ljJgg2PDpZbqWPo57TzTAiau3dxaR-3MMuXptpR2inH-ODCuoToSBgL9IEkyybGscKQ5lCryB9IREKFyytccHMXv3ZwHBZ_cqy6ShoEAwlW8pYerkeL8rFrr4v6lDd14Vsql-g8c1z3ZUDtdys632u_o8W650ELvcn4Z-vL8wbiQNzTg7479Utx2VsGk6c370nLu7LXTM2AXF9ip8FuuVCcSHUzv0dsrs3fz53jDcxirQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طوفان قم را درنوردید
🔹
طوفان و تندباد با شدت ۹۰ کیلومتر بر ساعت به همراه گردوخاک شدید قم را فرا گرفت. @Farsna - Link</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/farsna/466081" target="_blank">📅 19:45 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466080">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">پیاتزا: بیشتر از خودم برای مردم ایران خوشحال هستم
🎙
سرمربی تیم ملی والیبال:
🔹
از همه مردم ایران حمایت‌ها و پشتیبانی زیادی گرفتم. واقعاً خوشحال هستم، بیشتر برای مردم ایران خوشحال هستم تا برای خودم.
🔹
من در رویاهایم به یک مدال دیگر فکر می‌کنم که به نظرم آن مدال می‌تواند از این مدال مهم‌تر باشد.
🔹
من در حال پیر شدن هستم و زمان برای من محدودتر شده و امیدوارم به این رویایم برسم. در ایران استعدادهای بسیار زیادی هستند، اما باید بدانیم که استعدادها را در یک مسیر درستی قرار بدهیم. اگر بتوانیم این کار را درست انجام دهیم، می‌توانم آن رویا را در سر داشته باشم.
🔹
امیدوارم صلح در ایران برقرار باشد. به نظرم صلح در کشور از موفقیت ورزش در کشور مهم‌تر است. من دوست ندارم در دنیا جنگ را ببینم. مهم نیست چه رنگ پوستی، چه نژادی و چه کشوری باشد. ایران منابع زیادی دارد و به همین دلیل معتقدم که می‌توانیم در این کشور خیلی خوب زندگی کنیم. در کشور شما همه چیز هست، خیلی‌ها ما را حمایت کردند و تعدادشان هم خیلی زیاد است.
@Sportfars</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/farsna/466080" target="_blank">📅 19:38 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466079">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t2S2pyKzjjSGm2RFd3EtRLyIN9xVTw4XfXkUPseHEvQdgw0sy00pH-Umu28yq47xUCXY5PG-bGfw3wB6GEiRwHSh1r6Drz_FJcJD0aXUq9vxyzE2Zjww2doGJK0Umsn3L6bUQHwCD5UZRankMsIoNYmdcA9by3e-IIJwZOlhY6SyNu8H5eWfymXP4NDD6sy1PhJqtVcan_sCtc4VjAWupC-n7T7e7XDVqHQ963SwbEVIh408RFZS1HdzWWZEoOnR71gDfja3saS7kOs_h36UVO9Gm5GUun9y3NzMOcSpy_LA_Gd5G8GJifyFSU8xPaq7x4vZh21oaE9ylXXlnSAvhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیاده‌نظام ترامپ در شرکت‌های آماردهی تردد از تنگۀ هرمز
🔹
برت اریکسون، تحلیلگر حمل‌ونقل و امنیت انرژی، با اشاره به تصویر پرچم شیر و خورشید در پروفایل «همایون فلکشاهی»، رئیس بخش تحلیل نفت خام کپلر، نوشت: «اگر کسی بخواهد به دستکاری داده‌های نفتی فکر کند، کپلر…</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/farsna/466079" target="_blank">📅 19:31 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466078">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67f1cbb697.mp4?token=Kx8AgnF__rrXS7SdpHCQT5ARGpkdZ_l-_24eAO4rdtLhGmCfeibjbeqF80K_X9LBxLRwszy8bBwIz6mJvlfwj10VYwTHVulPtgglnUlWq_1mmtc2Sa0RcCPnUAD0n6nQA4Xt6Q_JGt8ZerScEnFJwAV-lWJerMl4LgCbqappseumrEfpD85zods8TyXt-UsViQoIi5-BJFmwuPVcVieU4otDxH0pLgmF2J386olVDc2TS1vopZuEBk17SaC4AjFsuw3K8wIt1GS3py8In7N9h0Rj9mlhQsrnCsA3rtGWCZl5cjeqvZev8fOlW8h9qwA2_qh7l-UVgvo0v5KcKGj0BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67f1cbb697.mp4?token=Kx8AgnF__rrXS7SdpHCQT5ARGpkdZ_l-_24eAO4rdtLhGmCfeibjbeqF80K_X9LBxLRwszy8bBwIz6mJvlfwj10VYwTHVulPtgglnUlWq_1mmtc2Sa0RcCPnUAD0n6nQA4Xt6Q_JGt8ZerScEnFJwAV-lWJerMl4LgCbqappseumrEfpD85zods8TyXt-UsViQoIi5-BJFmwuPVcVieU4otDxH0pLgmF2J386olVDc2TS1vopZuEBk17SaC4AjFsuw3K8wIt1GS3py8In7N9h0Rj9mlhQsrnCsA3rtGWCZl5cjeqvZev8fOlW8h9qwA2_qh7l-UVgvo0v5KcKGj0BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آب‌گرفتگی در جاده اشتهارد پس از بارش شدید
🔹
درپی بارش شدید باران، بخش‌هایی از جاده اشتهارد البرز دچار آب‌گرفتگی و سیلاب شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/farsna/466078" target="_blank">📅 19:22 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466077">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92d6303657.mp4?token=HejE5KMPpxvdjmukEm42lPVQUspqtNqlPcslvghXCA4aGF6w51FmQP-6s4saHkb72ueR6kpU2gpUPSWEgn_7-K6pFamz1rMFp0LmngggFnjaryEvPSREJYNIyP9-wgVjucrape-YtekjlMj6XklBJI57YG_WO_5fsgZ7e07oWCjuAbDXEREKRSZnZvRlFTGA7QiXxPqAi-MvTOKUrQVdB_Ww10IZ_QySNwSXwHscoKi2ydtrzL4Lj96xj4P0Fzod-YaqRHp7tq1QHTRLMVBWWn32o6yFHcVjgP406vrUZa8-g8My3AoKB1_8M3z3arI6XyDwfXl6Xct9f1sGmYL6Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92d6303657.mp4?token=HejE5KMPpxvdjmukEm42lPVQUspqtNqlPcslvghXCA4aGF6w51FmQP-6s4saHkb72ueR6kpU2gpUPSWEgn_7-K6pFamz1rMFp0LmngggFnjaryEvPSREJYNIyP9-wgVjucrape-YtekjlMj6XklBJI57YG_WO_5fsgZ7e07oWCjuAbDXEREKRSZnZvRlFTGA7QiXxPqAi-MvTOKUrQVdB_Ww10IZ_QySNwSXwHscoKi2ydtrzL4Lj96xj4P0Fzod-YaqRHp7tq1QHTRLMVBWWn32o6yFHcVjgP406vrUZa8-g8My3AoKB1_8M3z3arI6XyDwfXl6Xct9f1sGmYL6Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش در آرامکو همچنان زبانه می‌کشد
🔹
تأسیسات وابسته به شرکت آرامکو در جنوب ریاض از بامداد امروز دچار آتش‌سوزی شده و به‌گفتۀ رویترز، پس از ۱۲ ساعت همچنان دود و آتش از این تأسیسات بلند می‌شود.
🔹
رسانه‌های منطقه پیش‌تر از حمله موشکی و پهپادی به تأسیسات آرامکو…</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/farsna/466077" target="_blank">📅 19:14 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466076">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fD3h5HY-hoCoiYhkhV4qb-xYJ2Zxf1CBug44eC70XCa7sqKas8lrTjfsZ4ffGXuQ9Ry_qSdB0cZhxt8PgwyBzQsC07_q_Gr-fqpRPOZ-inT0SgoNpjHtxF0AcD8mccr83Rm1Fb6lX8MmuSdvdMs55OgCVZjzUzFuqui1wO-54NKGb54kppnJZ1fII-ARi4Ssp97NcGuxctUdMzOviCbkxsxzEJPgBHoj4h9Gccmf4Tak2gJAwYMFxZkYS54oDqOK0fp0SkzVbTuhBDYqZCT9IaWs3IJN7W3HSKv2xOo2jY_bpqX-XgpZ1iiC3oawcZFLeF7pwfAXdahw0BiI-dSb1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
ایران، بالای بچه‌پولدارهای آسیا قرار گرفت  @Farsna - Link</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/farsna/466076" target="_blank">📅 19:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466075">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cf47e0e13.mp4?token=gHrbi0Apbhgjwi4LjegKAmNCZ2BXS9yEVEpxRh5F98Hl3nE7gJ3IJPxe00IXCY6WzBPjiL0JYRPsv3DZuG1MY5WZnBwj4nhH-44FmfbBBJuF1TXlp6tqzEb99KX4eM2jqISoY39MucQUOSym6iFlf0JXB1URT6PXA6tOmUUx5I8x2YkaKTaN3Sz5YTFRRAWglQlhH_oieVlV_1uJLtdO3pZXQhXAviZe4R_w3Cl2_LKRt8XF43R398MiueeXAjs_XpS9BXBbpSGJHzIV_s68ntVES9jGMAIBms6HGBgkkVZ9xYj-HvBTtdqNB0u44DedOdwkzpg0lM_9ShW9Xcac5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cf47e0e13.mp4?token=gHrbi0Apbhgjwi4LjegKAmNCZ2BXS9yEVEpxRh5F98Hl3nE7gJ3IJPxe00IXCY6WzBPjiL0JYRPsv3DZuG1MY5WZnBwj4nhH-44FmfbBBJuF1TXlp6tqzEb99KX4eM2jqISoY39MucQUOSym6iFlf0JXB1URT6PXA6tOmUUx5I8x2YkaKTaN3Sz5YTFRRAWglQlhH_oieVlV_1uJLtdO3pZXQhXAviZe4R_w3Cl2_LKRt8XF43R398MiueeXAjs_XpS9BXBbpSGJHzIV_s68ntVES9jGMAIBms6HGBgkkVZ9xYj-HvBTtdqNB0u44DedOdwkzpg0lM_9ShW9Xcac5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طوفان قم را درنوردید
🔹
طوفان و تندباد با شدت ۹۰ کیلومتر بر ساعت به همراه گردوخاک شدید قم را فرا گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/farsna/466075" target="_blank">📅 19:03 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466074">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd8ea1125f.mp4?token=UA-Qq3EYk1rOOJ728eac24LIaLR09T9QirCHfxIg8hAXWqT76Ri5JYaP65Nxvdi-RYED9VrhqIVEzNj3r8IuHD06aQ0KK2q42IlQ0iZzxn7x59Ez_V_SWp_R0BifhAInQvQUUjaKO0sxapLEvZoVaDoM5oIX6L5dgbesAydSIMQWp_nAy8qDSb-VOkRPcQ-K0SWGliKy3YP9GEG44j29YYJH_vH22-wP8aSoVD7XO4nXJfH772Ua4-4s3nRWfyQb2rK0q750WxaLTGARJ36BBcxofwMhmXLF3Iv_UDyMwS8MKn_JabTeKMiTjpxcRn-Btcp7VvgnFWIBCPlXUFB2fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd8ea1125f.mp4?token=UA-Qq3EYk1rOOJ728eac24LIaLR09T9QirCHfxIg8hAXWqT76Ri5JYaP65Nxvdi-RYED9VrhqIVEzNj3r8IuHD06aQ0KK2q42IlQ0iZzxn7x59Ez_V_SWp_R0BifhAInQvQUUjaKO0sxapLEvZoVaDoM5oIX6L5dgbesAydSIMQWp_nAy8qDSb-VOkRPcQ-K0SWGliKy3YP9GEG44j29YYJH_vH22-wP8aSoVD7XO4nXJfH772Ua4-4s3nRWfyQb2rK0q750WxaLTGARJ36BBcxofwMhmXLF3Iv_UDyMwS8MKn_JabTeKMiTjpxcRn-Btcp7VvgnFWIBCPlXUFB2fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ایران، بالای بچه‌پولدارهای آسیا قرار گرفت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/farsna/466074" target="_blank">📅 18:58 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466072">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dmik3mGjD7oRj430XWIRABqZ-t41Dw70mGoORX-0OMC_96su3Z1ONoRy9uV8ifHh-y7NHbjJvJEicycngXwU1X85bKRhTt1yvPx0-X2pnVoLGDKUlsgTpTahdAVynSBdj55QqebUElTd04GS1Be3h7RdVmmiRI0tJETdOi15DEiTY6OLrWSGJAIadAhakLTCEsa8QGPpkJqLQEGUeCmnNzLkwqVBwiyhjSZj1anlHSZvl1O4hB5zKtM-o7bDuzm8AG4oBqo9d_kn0L1EXsOH6pm21y_zoTReGJbNksz4kZ8osvHwmenIlYItB7W1ec686gty12wrZfdtwbFBiry6Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JZ2UGha1WJFhshAxWoNwnT07UmJa1UpIDkbq30Yj8FK14p4dLjUH4LZVijRJHl5nZkuJ7-jYrJlZEJdqNTa4l7lFU__YuGHZSjS2LczO7NapbWDCxaM12cFdeE-FQb8HsYMmPvYV7OALp5fyHQ-CTsI2wZoFqpOePMXf92L8PcI8yuXldaLsFlTtQgWc1hiFXmAzr5Dnp5dUKi8dWgq3CVQxbo_M6rUl_RVxerQCoADRdgz7VdmCjJAbX9m5wzuQ9APIMMEHjj_099iZ6aS2OrjcKDOX4UW3Ps14PfLztH9qcvruOfFoSLwXEiqji45iLZBTFCvAzBKUFiYRcwRKhA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">والیبال ایران با قهرمانی در بازی‌های آسیایی از ژاپن انتقام گرفت
🏐
ایران ۳ - ۱ ژاپن
🇯🇵
۲۶ | ۲۵ | ۲۱ | ۲۴
🇮🇷
۲۸ | ۱۹ | ۲۵ | ۲۶ @Farsna</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/farsna/466072" target="_blank">📅 18:54 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466071">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22e99023fc.mp4?token=R-PFG04yEdtCVL9DUXCC03f-4SWEId6HIt91QcfSuBcap-OvdBxS9mPexCy_LaCgO2bAPsQx0I6DLKJTpWc1Y--R5lSPqgUDMl1nXfHsLEZUACb3oNb2WZtYmg8HxgQg44Gk4h7wlZ1FQpI6KBFGV73qnlTRwVbw_ihDKG1vzO8iqi3Ao1nafL2t7XTzSOo8eOrtoSmRxutfFUmddYP86yBaym1oQ-kqKrnSGzV9odKR0IYMGTGp3sDaeYBNrZyERGIQcGNq0Vkinq4FPgPGaUGlaPZMLKsyNDxgx8uBMoV4j0M9lNBaQ2q_GVpzAUxtIJ-Di2_Nsyz7WCxOxJVi4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22e99023fc.mp4?token=R-PFG04yEdtCVL9DUXCC03f-4SWEId6HIt91QcfSuBcap-OvdBxS9mPexCy_LaCgO2bAPsQx0I6DLKJTpWc1Y--R5lSPqgUDMl1nXfHsLEZUACb3oNb2WZtYmg8HxgQg44Gk4h7wlZ1FQpI6KBFGV73qnlTRwVbw_ihDKG1vzO8iqi3Ao1nafL2t7XTzSOo8eOrtoSmRxutfFUmddYP86yBaym1oQ-kqKrnSGzV9odKR0IYMGTGp3sDaeYBNrZyERGIQcGNq0Vkinq4FPgPGaUGlaPZMLKsyNDxgx8uBMoV4j0M9lNBaQ2q_GVpzAUxtIJ-Di2_Nsyz7WCxOxJVi4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
باران امروز هم مهمان تهران شد  @Farsna</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/farsna/466071" target="_blank">📅 18:49 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466070">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vujnH0ShjRw5QD50WgNyz3PeXcz2_mjh9SSxXY2i8vDEw4pElKilzMRVON_guNZbc-MtZwgJyQp0S5Gu0bmtVa2hOn7QWECJPmJJOfvbHjaT188hMOg7ldvQl0MS_L2ZuqQP1gF-ytDd_uOffUBtt_nan83x_O-YwWxZYJX5Hu6lOLxIaFsaAhboGiK0cqbq-TssCS6mxVLj-b7owt9NmH7hybZ2ctK1JXvOhtRlXKM05myXeoBwPKUM8-EEOOaULE0mXMF_9esq7hS25VQKw21gc4ZMGLCazhIBAW2GlJZRVqvVEKvZAzL3RqtYJOavvs9a7Cdk_Y16-CfPl14frA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
ولایتی: کشوری که عمرش به نیم قرن نمی‌رسد دربارۀ جزایر تاریخی ایران ادعا می‌کند
🔹
تنب بزرگ، تنب کوچک و ابوموسی ایرانی بوده‌اند و ایرانی می‌مانند.
🔹
تجربۀ منطقه نشان داده است که امنیتِ وارداتی تاریخ مصرف دارد.
@Farsna</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/farsna/466070" target="_blank">📅 18:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466069">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uIztK3JKykuMQNlrU85o_-o2kj54fbspcj7gk5OzuniQExdQcQYHYgKDXlULwy0a2Tha9XjIGd2uwxoLpSfoxwkxXDyxGQ4rtCKOcQweovWy112cRvIJbBpuS4qgqD4NcNqRe55s9FqRTe1eI-3cqXN7gOJUj4-H3iA3SfCsuTAQSIwQftjl-OBF32WY33NwhX9QVmmqMhWkQd8y5LPEU676bRvPts9nvlkObPD-Nbg_t7kKuYf7yRT1CppR8Ywqj3gqzX_gCxALdAkf4hYXNILDqnpIclo6pdmoSaUCmBdfhm2GT0aVFirSNvo74zntCNmonSyzpf_SYkbv4tcT5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیاده‌نظام ترامپ در شرکت‌های آماردهی تردد از تنگۀ هرمز
🔹
برت اریکسون، تحلیلگر حمل‌ونقل و امنیت انرژی، با اشاره به تصویر پرچم شیر و خورشید در پروفایل «همایون فلکشاهی»، رئیس بخش تحلیل نفت خام کپلر، نوشت: «اگر کسی بخواهد به دستکاری داده‌های نفتی فکر کند، کپلر واقعاً این کار را برایش راحت کرده.»
🔹
کپلر به‌تازگی مدعی شده صادرات نفت کشورهای حاشیه خلیج فارس، به‌جز ایران، در ماه سپتامبر به دست‌کم ۱۶.۵ میلیون بشکه در روز رسیده؛ ادعایی که تحلیلگران با توجه به ظرفیت کشتی‌های کوچک عبوری از تنگۀ هرمز آن را زیر سؤال برده‌اند.
🔹
آخرین نقشۀ موسسه واشنگتن هم نشان می‌دهد که حداقل ۲۰ نفتکش در یک ماه گذشته در تنگۀ هرمز هدف اصابت قرار گرفته‌اند. در همین ۲۴ ساعت گذشته هم ۳ نفتکش در مسیر عمانی آتش گرفتند.
🔹
رئیس بخش تحلیل نفت خام کپلر، چند ساعت پس از انتقادها، عکس پروفایل خود را تغییر داد.
🔹
اکنون با توجه به تناقض میان آمار کپلر و گزارش‌های میدانی، این پرسش جدی مطرح است که آیا گرایش سیاسی مدیران این شرکت بر داده‌های منتشرشده دربارۀ تردد نفتکش‌ها اثر گذاشته است؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/farsna/466069" target="_blank">📅 18:35 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466068">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cdzfRIrieons3v3r15No2dTlf_WvFI4faw2gLQNX5sY06NE63yopTtzcdIKS4yP2azg8vJG3orUR6JRBejbm4GCjE6bEQHE24JRWr1yCnBLtycv2LgI6yuJr-MeAHplzlUP0BBPAHySVgo3SM6Vyg1aJ96nbYcrGkLKvqsB0gydJ_WpitEJ41e4Pk49Iphk8p9PUC7-ekSQ42iR9x5Klj9_kgwgPxpyIL8e6ibbcYbqf_ciWm4lassOqZ5zNgAidswI3s4P9cZLCW7m_nfUL1S1Nh5BATy0C5JkFrTdb8WJS4ujpcD6v6mwVydCfeIS68_ELiNc1MhXvJnHfF6z1bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله به یک نفتکش در مسیر غیرقانونی تنگهٔ هرمز
🔹
سازمان عملیات تجارت دریایی انگلیس اعلام کرد که بامداد امروز سمت چپ یک نفتکش در فاصلهٔ ۴ مایلی شرق عمان هدف قرار گرفته است. @Farsna - Link</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/farsna/466068" target="_blank">📅 18:25 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466067">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f843506628.mp4?token=F3R5entoxRJv_GPHEMDIurJUdLaXxP8I02dOGm06_MdL11x1CUdYGyfID13Iqbrkq5ldsaP-6EZSzEyO7UCnRYCWnWRwVZZvlsM01C-7OOw6QsBEQ4LIht6mTw9Clk-dhBCIQPUYDZBexki17uvRhlEI2nyGrVas70O_Y4nw6Vz5Y5MW_Se4SqJSNWfKyOxjDq0g0blcS8yDfqRxUxso17-6GaLOm7sgWjr57L1psUf3fvKxxrb1D4djSAKj97aaf9Gm5SGNmHbcjaC5zE-YIWd1FC_Soc4yb8DlxftsQfgOHiev9nTG503k8JIheEZZRWRPfrSopBwDht1Sw7xgwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f843506628.mp4?token=F3R5entoxRJv_GPHEMDIurJUdLaXxP8I02dOGm06_MdL11x1CUdYGyfID13Iqbrkq5ldsaP-6EZSzEyO7UCnRYCWnWRwVZZvlsM01C-7OOw6QsBEQ4LIht6mTw9Clk-dhBCIQPUYDZBexki17uvRhlEI2nyGrVas70O_Y4nw6Vz5Y5MW_Se4SqJSNWfKyOxjDq0g0blcS8yDfqRxUxso17-6GaLOm7sgWjr57L1psUf3fvKxxrb1D4djSAKj97aaf9Gm5SGNmHbcjaC5zE-YIWd1FC_Soc4yb8DlxftsQfgOHiev9nTG503k8JIheEZZRWRPfrSopBwDht1Sw7xgwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
«میدان هفتم‌ تیر»، دومین پایگاه آموزش جانفدا در تهران شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/farsna/466067" target="_blank">📅 18:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466066">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48b6addc4f.mp4?token=cATjXKOv-8QoTxD019F5KGCnGrLtQy_0b4P7K3d1FKsi4cdPfPq6UBg_XvIg50jpsX8Fe3X6MniUOnIKIJpNdmeejUIb4mHeazDXQW4uOMyY3cDEHvW5TlazgGVz1SE8lcqCwzMTOla4XtTQJQIKqoh7OM0LLrFA8HamLuyqiFHJLlWXi4uL3i4r9tOjOBkRFMj7CGdIg01UxBfq53YwG-ZP5lyhxg-6M4sI1aYt26pwtuyqAlEHy1qwOghQHL9tCd2sa5REaoxhDdLOBU7TUYgU7LVfcnZordw0XC0KNtstUkiNNcFiwlWsw_NRxHzZBkQxAYH4TOU1-wvhRgjZRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48b6addc4f.mp4?token=cATjXKOv-8QoTxD019F5KGCnGrLtQy_0b4P7K3d1FKsi4cdPfPq6UBg_XvIg50jpsX8Fe3X6MniUOnIKIJpNdmeejUIb4mHeazDXQW4uOMyY3cDEHvW5TlazgGVz1SE8lcqCwzMTOla4XtTQJQIKqoh7OM0LLrFA8HamLuyqiFHJLlWXi4uL3i4r9tOjOBkRFMj7CGdIg01UxBfq53YwG-ZP5lyhxg-6M4sI1aYt26pwtuyqAlEHy1qwOghQHL9tCd2sa5REaoxhDdLOBU7TUYgU7LVfcnZordw0XC0KNtstUkiNNcFiwlWsw_NRxHzZBkQxAYH4TOU1-wvhRgjZRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بارش شدید تگرگ در دزفول خوزستان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/farsna/466066" target="_blank">📅 18:15 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466065">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cqmg7e6BY2Ghh9F13aubsa8biQj9HFZ03jtbZHKthPnabbzyKzwAJRAqzUAnyK7hAinoFDr2VlBOGefNqslZP_Qfcjvjl0nVouoHc0DB_TdPumnC6iSsYOYNPTbhGHTV-Sy1_JMbHZZQ1GQBOSdr0PFa1zhkB2QQ7hGX7Fs1kM-PoIo3JbQRi0GftgBKQ0b_k6oT193eM4YR8Wv7zraaKOzyuJT6Uy0tQILZvQRXcMqlHRiCA9K329KUNsDLCaj_GnXk21yZN8CIaHwobIg08VgLF2yukaNKrdGKu3bfd138csycHikY_m-1fcB-DiiL4QpObIckoRm2ALZeaU64DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انصارالله: پایتخت را در برابر پایتخت هدف قرار می‌دهیم
🔹
حزام الاسد، عضو دفتر سیاسی انصارالله یمن: حملات عربستان به اهداف غیرنظامی در صنعاء، مانع ادامه عملیات نیروهای مسلح یمن برای بیرون‌راندن نیروهای تحت حمایت عربستان از تعز نخواهد شد. پایتخت در برابر پایتخت…</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/farsna/466065" target="_blank">📅 18:08 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466064">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iwgw0YO27eVPXlhA6NrsXAyKZJ3hrv4Zx_-vcqJYa2X2JYYMjNWadadFMWJmRDQJckk49M-CUg8yTslEU48yYo6nF9fan5X6Fb0JDCB5ia28QaqYxL9uA4yQ49yhgPBoIgugfk6wn0qmnA2NXYTYM3v6RfM3lWRHQy60RwC4t3MVhO_vhwFbMpv3ivxSjvcFunm9i02WqQu4yuUV-7Gce_hAQQnr6oTv2x6IEYE59mWIQ9h4-Sqa4Hyy4_YfKhVagnUNpGKvpb8YHJfISDpLJz9vynu73SvKBOhKukX6AWid9QHV6_HSeSq7UNRYBIGW-mGDUkyB9nXbi0-VKsjr4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخۀ «بدیم بره» اصلاح‌طلبان این‌بار برای تنگۀ هرمز
🔹
تقریبا از زمانی که تهران از مدیریت ایرانی تنگه هرمز رونمایی کرد و اثرات اقتصادی آن در اردوگاه دشمن نمایان شد، برخی از چهره‌ها و رسانه‌های سیاسی سعی کردند تا از اهمیت این آبراهه استراتژیک بکاهند.
🔹
تیتر…</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/farsna/466064" target="_blank">📅 18:04 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466063">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88ca0ecb9e.mp4?token=Ze5L94PIdI_a6pS_JqNfGqfw5mUxTw1O9byEhDOqvYHl0I3d0VgmLqv0LkVITEUmeXfYtti1n0KJdpOe81CCYGJTOoQBR-1ucmGWmqklN95Nx1MNhaKCFVjC2rptIaou3QkmEAfd5H0HiggQRhG0it3vp0PyNSKxfoz2SZHopYaddvAalmGMg-ndhJW3d66aSXSxi8PjkRnZ2G81OzC49QVVc46__5gXGfCtwDcy4A0Gp5ZREmgdcQ8e77Ay1lvszq9y-ei-iFWIeSAxOKUdctupwVKH0QhEmlf911N-FF06jZ5D-jt0oeWM4wD8j0oKq36FXZzTcaScavy1waLwBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88ca0ecb9e.mp4?token=Ze5L94PIdI_a6pS_JqNfGqfw5mUxTw1O9byEhDOqvYHl0I3d0VgmLqv0LkVITEUmeXfYtti1n0KJdpOe81CCYGJTOoQBR-1ucmGWmqklN95Nx1MNhaKCFVjC2rptIaou3QkmEAfd5H0HiggQRhG0it3vp0PyNSKxfoz2SZHopYaddvAalmGMg-ndhJW3d66aSXSxi8PjkRnZ2G81OzC49QVVc46__5gXGfCtwDcy4A0Gp5ZREmgdcQ8e77Ay1lvszq9y-ei-iFWIeSAxOKUdctupwVKH0QhEmlf911N-FF06jZ5D-jt0oeWM4wD8j0oKq36FXZzTcaScavy1waLwBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
باران امروز هم مهمان تهران شد
@Farsna</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/farsna/466063" target="_blank">📅 17:40 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466062">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ce2245da0.mp4?token=o2CUrk-zid4wGTF2wxbDeozbj14VZuBqqlxazoqplZr4SuvfSoaPTIyKkk6oQwICmrZYVl-V9CDd2CQDnaSvUwX1PmEyf4JvZtVAGLeZOIhj4WA-IToplXO7GIt4cE-buMYsgE7AkWS4o3Jg0muWVpITuiPjCrn9gq5E4xo3-s-LAHz_llVaSsXlOldNZ3wLx3xpH4nLahBxoxFNkTZod0he03Uuqm8G8TP2C2m8naaIaFipXd7IXDSMDRut-7aYXnugrOruPapYJ8Ryu5gXF0QBwdAYTylsys-lUiKSH54pR5hiG65bd4_XvKs8YcD7-QbUaKqXrs1pDB96airgKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ce2245da0.mp4?token=o2CUrk-zid4wGTF2wxbDeozbj14VZuBqqlxazoqplZr4SuvfSoaPTIyKkk6oQwICmrZYVl-V9CDd2CQDnaSvUwX1PmEyf4JvZtVAGLeZOIhj4WA-IToplXO7GIt4cE-buMYsgE7AkWS4o3Jg0muWVpITuiPjCrn9gq5E4xo3-s-LAHz_llVaSsXlOldNZ3wLx3xpH4nLahBxoxFNkTZod0he03Uuqm8G8TP2C2m8naaIaFipXd7IXDSMDRut-7aYXnugrOruPapYJ8Ryu5gXF0QBwdAYTylsys-lUiKSH54pR5hiG65bd4_XvKs8YcD7-QbUaKqXrs1pDB96airgKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اعتراض به قیمت بنزین، سخنرانی ونس را مختل کرد
🔹
«بن براور»، نامزد دموکرات مجلس نمایندگان فلوریدا، در جریان سخنرانی معاون ترامپ، با فریاد به قیمت بالای بنزین، جنگ با ایران و پرونده اپستین اعتراض کرد.
🔹
او با کنایه از ونس و ترامپ تشکر کرد و گفت: «ممنون بابت قیمت‌های بالای بنزین و پروندۀ اپستین.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/farsna/466062" target="_blank">📅 17:37 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466061">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GCJR6CuOSBHWImlb1yowILvAHeezQs2-O-jhTUCFeGLhiBPnqKpoxiVISajNbUHe_X4T71cXldVlVUodz6AyB_OVRUgPej2Z2KC_ofonLWg2ORBTxN3ckYEk0h56DY5majF3fr_BBqBpxUVN6WjNOjnk3kL3R9ak6o2yg7lSsOEYoVQwBrYk9KsFkQWvmhySNPD9zQJ7_ShTOSpLTKJYj4spO7LBh2j_D7QBhwQSQBllzsB7Nb5MZ9JMuW6n9PK1_oIuRkYUofIOfjYFDA6XwqeUfAqquhZdEKMjLh_SSRAwijtq10wO4E_WhoaqhueMJrGfTACZHN_mCKMQrBF2Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخبگان سر قرار همیشگی حاضر شدند
دکتر افشین معاون علمی رئیس جمهور و جمعی از نخبگان کشور که هر سال در دیداری حضوری با رهبر انقلاب، پای صحبت‌ها و رهنمودهای ایشان درباره آینده علمی و پیشرفت ایران می‌نشستند، امسال در مشهد، ضمن زیارت مرقد مطهر امام رضا(ع)  در جوار مزار رهبر شهید گرد هم آمدند تا سنت دیدارهای سالانه را در قالب تجدید بیعت با ایشان برگزار کنند.
@Farsna</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/farsna/466061" target="_blank">📅 17:36 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466060">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pXOuXcDdw77eo8SezzrYZI5ICDD1YWcyYXLaDFdWvfWFu7HCDTSPgkcOwg1v5erflrp1X-qjI1-DeoXTnkdtF0B2xoEPOkiiJQyx0SZIoZgL0401xQmA7Ljbeufmw0_RkPGfka07FdTd_8Be0OiEwEuH5qxo34rxgN_9g_ymWyMa1C00-BhpqmrslJOX7mzSqeoqbmVFee28Wx0gC4V-OyBEka9AicTgGa2ubywDtzCfp-DjUpHqNhXn9V4JDikit_D9MEN9JK-s438Z1aW0aFSSwsn6z7DtT6jdD-5xsqHu78GGaviDSLv9nzBVMoQQ6uxUh8wsIU8yFHwmK2F4ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یار دبستانی اُپارک شروع شد!
🎒
💦
شروع مدرسه رو با یه خاطره هیجان‌انگیز برای کوچولوها همراه کنید!
🥳
اُپارک به نوآموزان متولد سال‌های ۱۳۹۸، ۱۳۹۹ و ۱۴۰۰ یک بلیت هدیه می‌ده.
🎁
📅
۴ تا ۳۰ مهر
🎟️
کافیه هنگام مراجعه، کارت شناسایی معتبر کودک رو همراه داشته باشید تا بلیت هدیه‌تون رو دریافت کنید.
👇
برای مشاهده شرایط کامل و اطلاعات بیشتر، همین حالا وارد لینک زیر شوید:
🔗
لینک</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/farsna/466060" target="_blank">📅 17:34 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466059">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/farsna/466059" target="_blank">📅 17:34 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466058">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kNLiUpJ9IfsYZXQ--XYuAJ6B66aIgk06gCase3eP6Md4_5ngo3tgtGCpMXZMoJVGkqwpADe5fymgG8wiQTFErK8vkx40krPt2vLQer389mZ26fybHW51QiLin5OnJr4cjCQhlqu4qnWFOcOLoUeQXnfoxNoviHkyQYEFS6rABif4yzA4iroCwlCbaHcN-R5ZK7mu5M_H3RvdPd-Pm2kCWg6Kif25OtqRIO1nMKn7pvQDHu0AJhX7q8D-GWXzH7FlkmoeGLTTeeJw0EJ60g7TkLVWajAIoLox8Lr34hwJG4Zu7pRyhyCwQxUpfov3I15Og6ZfHAu222lJ0t8WCCbC-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعطیلی معاملات شبانهٔ تتر در صرافی‌های دیجیتال
🔹
طبق اعلام صرافی‌های ارز دیجیتال، از چهارشنبه ۸ مهر تا یکشنبه ۱۲ مهر ۱۴۰۵، بازار تتر-تومان هر روز از ساعت ۹ تا ۲۱ فعالیت خواهد داشت.
🔹
همچنین در این مدت، سقف خرید روزانهٔ تتر برای هر کاربر ۲ هزار تتر تعیین شده…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/466058" target="_blank">📅 17:26 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466057">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34379a9399.mp4?token=rrfJ7nRsjwB2M9v4Zobxo-E3Em3Rr2UyjMD3Ao2MocoX8wnrFB3alsYIZZPa6nOCMGq3gCScQxS9a1Fk4QZWOWIcK8ekZ1w5aQUr6cJliTxCYIqinr0kPzva20oRWAoLesTDsJTMz7iOuXA2XYV7UKwGthE6DciO1eSIVr-e3J8t8vDdtvsFiovWb81t4W1bdrabSh4L-UdvETZ4viU4iXQYEJY5PIb3EJkBI0VlNpTNs9B2iGe6Pa25m4QE66Q5XCkTQcYVjoygKqpjddulrIMGxiMo8vXxZiRcC_VdwUp-XlZ5wYK0CfFCTAYpgKHMktHS-EbNhFc_tONA6hb8Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34379a9399.mp4?token=rrfJ7nRsjwB2M9v4Zobxo-E3Em3Rr2UyjMD3Ao2MocoX8wnrFB3alsYIZZPa6nOCMGq3gCScQxS9a1Fk4QZWOWIcK8ekZ1w5aQUr6cJliTxCYIqinr0kPzva20oRWAoLesTDsJTMz7iOuXA2XYV7UKwGthE6DciO1eSIVr-e3J8t8vDdtvsFiovWb81t4W1bdrabSh4L-UdvETZ4viU4iXQYEJY5PIb3EJkBI0VlNpTNs9B2iGe6Pa25m4QE66Q5XCkTQcYVjoygKqpjddulrIMGxiMo8vXxZiRcC_VdwUp-XlZ5wYK0CfFCTAYpgKHMktHS-EbNhFc_tONA6hb8Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
توقف پروازها در فرودگاه ریاض به‌دلیل انفجار
🔹
همزمان با گزارش‌ها از حملات موشکی و انفجار در عربستان، فعالیت پروازی فرودگاه بین‌المللی ملک خالد ریاض با اختلال مواجه شده و پروازها با تأخیر یا لغو مواجه شده‌اند.
🔹
برخی منابع عربی هم از حملات موشکی یمن به مخازن…</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/farsna/466057" target="_blank">📅 17:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466056">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sc2-M2HPT9GJbztM5C6DuTf7twMqhhI1V450V9pt8VjQ6njAoPI4tTW_s6x8l6O6_rWkOTifAZW-3PUxDuXjgoUlj7bC8G6cDaCVKDdedfMHCptjQgzNdPQUNZZ8babuLyPicfOxQkVLPXjn3XzFcGyrctie7FIeU-yAZ-_DxzIE1B655yT9Qj9CxFJZnU2_YfRsSxNzaA6DaCCMfNp6TcCBmmXUwS382zdsyhRs3dQR28HL2gZVq60lHBy1uL2Qk9yzcmhHH1Nwu6LSsxd5PzUIT7U4saq-Dh3N8UjnNDoZB-UMIA3TBkcfURsYNsd7Q2qs0Rg2lG3Oo6QIP72NAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پدر و مادر رتبه‌های برتر کنکور چه شغل‌هایی دارند؟  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/farsna/466056" target="_blank">📅 16:59 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466055">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uXGCpY8aNzMarHYYloMbofqfkLnF65-IrJX9kxMUJLxY75h1kjzik_tenmoeSWOm6SSCaOREM8Wa1esD8gbcKt7gWLUGwPPd_epbGvDm9X5APXrm7_belbIs7RchpygRfpTm4lQtstRYVNPi-4qujhkvCoHROWpkcYkiYTCAOXY1vcwvzMwbmmmWfLkTc5PuHEz2Ra0l0c21nG4aJTIjNnWlb8l_dyy3GpBIwCR5R9RN9co47l9CHExBvnpWGQ_HdbPXlbgNY09Us-SzCsQF5GfrbdGLtUdwk2NtBQREbwCGEJxfn8CTZ0hFnaCLJ9qK9baljtyD4bo6wKqOomVjcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
المیادین: عربستان در ۲ ساعت گذشته بیش از ۱۰ حملهٔ هوایی به پایتخت یمن انجام داده است.  @Farsna</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/farsna/466055" target="_blank">📅 16:54 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466054">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mQwfqaqOsyW1DMSoL9ajZRuYZZ0p8Zofp-TdH0bRh1HKIiA5siMxQq8dcCWhwO--N_3WyVYGD4DkztZkuYZGhc2CaRoRE409v1FmOLpnc1owrb4onfSRAEsdjCvi9vPL7-dYma0YdNaxh4FIS7NHCuTWoq7FpoMoiWbmpWRZ8Qtfw61wqBmrq_1yJ-sEQ8L66-5yEhY-tQNCovYAo3-wD6S-Wv7owv-UR9QJAZ8MoTd4-zdpRGMux__vxA1ydugaognvJpHc8ZV8tXz0wlgxw46BiiyXX1rFywiYllogT-aQqH4IvjcHfPSWtLDlYy495Z9DVkyX-jXzmj1B34QZIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دست‌کم ۳۰ هزار نیروی پاکستانی در عربستان مستقر شدند
🔹
اسلام‌آباد در بحبوحه تنش‌های بین ریاض و صنعا، ۳۰ تا ۴۰ هزار نیروی نظامی خود را به عربستان اعزام کرده تا به این کشور در دفاع از مرزهای زمینی‌اش در مقابل حملات نیروهای مسلح یمن کمک کند.
🔹
یکی از مقامات پاکستانی در گفتگو با رویترز تأکید کرده که قرار نیست این نیروها در عملیات نظامی در خاک یمن شرکت کنند. به گفته این مقام، نیروهای پاکستانی از سال گذشته به تدریج در چندین نوبت به عربستان فرستاده شده‌اند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/farsna/466054" target="_blank">📅 16:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466051">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58f2ece7cd.mp4?token=NFTYB34wjEsBWJPSyu5_W7hdBrUWGgcNM--Z3wo8ZvwlyLPi6erkNALi9Rkf2JusxqM1zyYQHyx5axrpElonNPwxW6M5lOsVrHCuaEGHor2MGwQY3GRW8_cfitdIVN_nK9c-Wcl4ieIDd1e3hqAQ3rk_VsS7lhT2Yoo89L8rKWt1SdQJHikJ47zvqfHSouN0OPceNJWrWcLllVhwqSnMrmezOCmUSjDroJbDppSNq6rgIlfmso6suabHrLPQdlWxFo30PLX5ZaMRO5MbQkLG2bH8wcgCHKmfQGJ2scC4DwWbfayeUQHsUolHPCZJfe7SWkVtNZzQdOtjeMnMETSBFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58f2ece7cd.mp4?token=NFTYB34wjEsBWJPSyu5_W7hdBrUWGgcNM--Z3wo8ZvwlyLPi6erkNALi9Rkf2JusxqM1zyYQHyx5axrpElonNPwxW6M5lOsVrHCuaEGHor2MGwQY3GRW8_cfitdIVN_nK9c-Wcl4ieIDd1e3hqAQ3rk_VsS7lhT2Yoo89L8rKWt1SdQJHikJ47zvqfHSouN0OPceNJWrWcLllVhwqSnMrmezOCmUSjDroJbDppSNq6rgIlfmso6suabHrLPQdlWxFo30PLX5ZaMRO5MbQkLG2bH8wcgCHKmfQGJ2scC4DwWbfayeUQHsUolHPCZJfe7SWkVtNZzQdOtjeMnMETSBFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خیابان‌های مادریگراس اسپانیا رودخانه شد
🔹
بارش شدید و بی‌سابقۀ باران در منطقۀ مادریگراس در ۲۵۰ کیلومتری مادرید، خیابان‌ها را به رودخانه‌های خروشان تبدیل کرد.
@Farsna</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/farsna/466051" target="_blank">📅 16:39 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466050">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/179823c671.mp4?token=HkWDAIv75pflCrBKn3JmikM2KqzRVMOFG3RjOk9sj9Z7rtqrUpGCDTBQfITZHXtpKKt0m5vkmVzQn0_xD8hyb852FgnVTV0PwOOOxSWEujBZ0PZ3hpq83h3oDC6NXAXJZigUiXKXciXBPYVyBA8GwWfsFabfHQu5DOWVQB9TbgeC5CRAWu8dkq5IxuR4WQft0gTopBB1ihoQLeQ2mhx4IZAmtgQiCutxMT43QKLKXmH3RbUMUO9x_NLT4OarEq6Q_ehFiEEUuqLR9-2Hmk2lm-9dasimRW6GNdRMGJ9WaIfMCXRR3IxdgfDg3UeaNucSbWJs2QaZAaUbhn5LbN6UAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/179823c671.mp4?token=HkWDAIv75pflCrBKn3JmikM2KqzRVMOFG3RjOk9sj9Z7rtqrUpGCDTBQfITZHXtpKKt0m5vkmVzQn0_xD8hyb852FgnVTV0PwOOOxSWEujBZ0PZ3hpq83h3oDC6NXAXJZigUiXKXciXBPYVyBA8GwWfsFabfHQu5DOWVQB9TbgeC5CRAWu8dkq5IxuR4WQft0gTopBB1ihoQLeQ2mhx4IZAmtgQiCutxMT43QKLKXmH3RbUMUO9x_NLT4OarEq6Q_ehFiEEUuqLR9-2Hmk2lm-9dasimRW6GNdRMGJ9WaIfMCXRR3IxdgfDg3UeaNucSbWJs2QaZAaUbhn5LbN6UAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زمانی آرزویمان این بود که آمریکا به ما موشک ۱۲۰ کیلومتری بدهد!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/farsna/466050" target="_blank">📅 16:26 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466049">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lKc3ioZLavwttrsRD15INKyo0GZtEQ7u6ekkUN2Em1KeIzhRkrMTyk-UhAuQ4sooG1IgWqWEUvpoaeMSizy26sY05U4PSd8Yyhuvt_Vvm6rCRRCdHPkAShKIIbDPyefhUADPE6t5yam9y6b5KtbGikdnZ2wBTpn7waAbXBT0ouA1CcTFwbT4rTkAHQ_CA5Hp396cBYgg7aIv5jt_K-MTv04WqfTdNPvghKbh8-yr0oXMi86o9LUz3F1dZfCMgtr_FJ5THfM0FQyFjOKKK9ThZJUMr2YFMCA_9BGMWpXNBpAan7nt3rqg-bMDHXpQKBcLsqKOHN7QDwB0f_-3Dmt-Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طعم تلخ وابستگی را از عراقی‌ها جویا شوید
🔹
گاهی برای فهمیدن معنای استقلال، لازم نیست سراغ کتاب‌های علوم سیاسی برویم؛ کافی است به کشوری نگاه کنیم که برای برقراری یک خط پروازی، دسترسی به درآمد نفتی خود و حتی انتخاب نخست‌وزیرش، ناچار است ملاحظات قدرتی بیرون از مرزهایش را در نظر بگیرد. عراق امروز یکی از روشن‌ترین نمونه‌های این وضعیت است.
🔹
استقلال برای یک کشور، کلمه‌ای تشریفاتی نیست که تنها در قانون اساسی، سرود ملی و پرچم آن خلاصه شود. استقلال یعنی کشوری بتواند درباره سرنوشت خود تصمیم بگیرد؛ یعنی دولت بتواند در چارچوب منافع ملی خود تصمیم بگیرد، حتی اگر تصمیمش با خواست یک قدرت بزرگ همخوان نباشد.
🔹
درغیراین‌صورت، ممکن است کشوری روی کاغذ مستقل باشد، اما در بزنگاه‌های مهم، اختیارش محدود شود؛ آن هم نه الزاماً با حضور سرباز خارجی در خیابان‌های پایتخت، بلکه با ابزارهایی به‌مراتب پیچیده‌تر؛ تحریم، دلار، نظام بانکی، تجارت، فناوری، امنیت و تهدید به قطع حمایت.
🖼
اما تجربۀ عراق چه درسی دربارۀ معنای واقعی استقلال به ما می‌دهد؟
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/466049" target="_blank">📅 16:11 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466048">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQTFKTWyzYT6A_55XER9RQDrh8cNo6qoRZHBa2W4A6hYytUVVYJJIHpkxS_H6e1OB8kVtO9bmXfjQehZJWppqplK4EHoSfbODAJuq5jymuP6Vju7g9UQPQz8vZMWesnHkrJH6A4wV9OwROmMgZPX_EG1uxsXWg17Free-qGECoO0w5RJnjYiwtIxROOZPOysLzrCNK9TFEMaHMQA25CAn0N864I3Dt66-KK0mAtN_4t7v_hj-7oa_8aQ3-JdN6XUzZLp1qhNSrruwnJq-FGW9AP4p5m_Rd882Wj8cckiRSwOx_HEu_dmv_ImWO6Uw3yElLzEQsliUWOhyX8ww0deKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
روسیه یک پل مهم کی‌یف را هدف قرار داد
🔹
خبرگزاری فرانسه: برای اولین‌بار «پل جنوبی» که شرق و غرب پایتخت اوکراین را از روی رودخانه به یکدیگر متصل می‌کند، هدف ۲ حمله پهپادی روسیه قرار گرفت. @Farsna - Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/466048" target="_blank">📅 16:01 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466047">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔴
حملات شدید هوایی عربستان به پایتخت یمن
🔹
منابع عربی از حملات شدید و کم‌سابقهٔ‌ عربستان سعودی به مناطق غیرنظامی در صنعا خبر می‌دهند. @Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/466047" target="_blank">📅 15:55 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466046">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d42f08273.mp4?token=h8B12ioPj1FjU7m9boezvFdHoMwWWOInuZ5FN8mamxDgU1DI481fanmdO5HHlFzbmghSXkG42u73qENd66R8_MNYD-dnAiscjZCXDXyYhNhsPBhwZ_oqxBEn5M7JurYgKhXYeb0_oOqmfp9OLCHvmgdpKyg7PNHtBgKXo5XlquVM26p1GqUnV3m_jYcjFZKVdAuQFCnv9Mx6q9x69mYkf18vXbqwNlnM8nT1mqn2X1EeYdProY5N1ZyCHHDMJRx-dI9tusJvS_XP0yRnl26SVvZf4P8ST4NjTfbVbt-0qQ_jG6h-x_M_6thRHzmIvkCnfcyN5IcTp43ofBsTHIBlgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d42f08273.mp4?token=h8B12ioPj1FjU7m9boezvFdHoMwWWOInuZ5FN8mamxDgU1DI481fanmdO5HHlFzbmghSXkG42u73qENd66R8_MNYD-dnAiscjZCXDXyYhNhsPBhwZ_oqxBEn5M7JurYgKhXYeb0_oOqmfp9OLCHvmgdpKyg7PNHtBgKXo5XlquVM26p1GqUnV3m_jYcjFZKVdAuQFCnv9Mx6q9x69mYkf18vXbqwNlnM8nT1mqn2X1EeYdProY5N1ZyCHHDMJRx-dI9tusJvS_XP0yRnl26SVvZf4P8ST4NjTfbVbt-0qQ_jG6h-x_M_6thRHzmIvkCnfcyN5IcTp43ofBsTHIBlgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">والیبال ایران با قهرمانی در بازی‌های آسیایی از ژاپن انتقام گرفت
🏐
ایران ۳ - ۱ ژاپن
🇯🇵
۲۶ | ۲۵ | ۲۱ | ۲۴
🇮🇷
۲۸ | ۱۹ | ۲۵ | ۲۶
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/466046" target="_blank">📅 15:50 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466045">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🎥
رئیس سازمان سنجش:  فردا نتایج اولیهٔ کنکور در تارنمای سازمان سنجش قرار می‌گیرد.  @Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/466045" target="_blank">📅 15:46 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466044">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0485d5cbe3.mp4?token=jPjQ0_MpdYdmw0qcIKhXT5SY-BLByH2_QgSQx2FQ6yRvAcUUfW4XmDbTqRMTSpdAm6Y8Q0B9ciJ6_m1zhTHzIa-qD3kaGAF8bm1Hktbq2LhXw6Elo2qnk4PNxj2m5CoCajg0k1BD0ixBuiJwG3OQ3Icv6fRQsq3PgFrR6kpUQt-3xyL5wu0QYMybnDxZnzE_ZE3LnerDmYG1cGXsNHBZMci2ve-XzWG2EWgFVnKRN2U1x7P8zbzaUz-5xFkfx4TMHo36SZddcX0mkZ8KbwcZKGbhf9buR8w7ypIGv5oLT-ere8ObacstEdV8-OqumYmf09Pmnf6hYPQmIQCVET9qjYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0485d5cbe3.mp4?token=jPjQ0_MpdYdmw0qcIKhXT5SY-BLByH2_QgSQx2FQ6yRvAcUUfW4XmDbTqRMTSpdAm6Y8Q0B9ciJ6_m1zhTHzIa-qD3kaGAF8bm1Hktbq2LhXw6Elo2qnk4PNxj2m5CoCajg0k1BD0ixBuiJwG3OQ3Icv6fRQsq3PgFrR6kpUQt-3xyL5wu0QYMybnDxZnzE_ZE3LnerDmYG1cGXsNHBZMci2ve-XzWG2EWgFVnKRN2U1x7P8zbzaUz-5xFkfx4TMHo36SZddcX0mkZ8KbwcZKGbhf9buR8w7ypIGv5oLT-ere8ObacstEdV8-OqumYmf09Pmnf6hYPQmIQCVET9qjYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دور افتخار آذرپیرا با پرچم ایران  @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/466044" target="_blank">📅 15:45 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466043">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZvfsoXZcJWJQd1RqBQVpKO1X8k7ctEedW3zA_IF21i9f7sCvZWt_m6FmjM2md8LrwWHBfJIRkB6v3rfyFNtw9CpcKF4_bSTtV3j0ebEjYfQkIsbQhsH5OXrLaH0o5Sr2bxKiM3LTHgLZb8sheZRrXBni5FXQx3x9AjB6LJr47dEJwOhfbb_FjqQC7n6WYFNQOS8gdrT7y_sR48aUKTCnUDLrOsQYgiSdz2c6K08jJafHS3RP0aJBBmOYKWKSAqDTLFUc_vAE-rqrlMyqJe8sT2WM4L0rz-qmj_wlbRr-fKLaRkdjKVACyIPOIFE5Hqj8oIYPQjjpD42MY9BDebxA0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
کهن‌ترین درخت گردوی ایران ثبت ملی شد
🔹
مدیرکل میراث فرهنگی لرستان: کهن‌ترین درخت گردوی کشور با قدمتی حدود هزار سال در منطقه کهمان شهرستان سلسله لرستان، در فهرست میراث طبیعی ملی ثبت شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/466043" target="_blank">📅 15:35 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466042">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/REKQGXGwbSjhD5hQdoipXFi5N9Dal2-dqrE5WL2Tu6Yw95K8amW09W2st-6lzimJIjTrpUGQaZraCGqdj1sznZvQZRDRPd3TwClHBU6Iy9VmoC1ui-JhIt1hMzTITLz5dGfZI4-utGzb_A-wsF0y8sS_EZocI2oVEO2SQ7XfeFmfwQ6HVIfHnLcv_JMXmwMECRF3AFsqARfkaMIh9fTJqQAH_MHjEmJlsBh0wX_WgKy_ZkjKW01Q6aE9jqhEuwOQql2R6X7o3XdR_6mgT9mm16nNsz82O5ntuXlwx0n3e8PXCpGtCmO2Eh3A_A1gKrbdRG8HhdWh8MqWZBeEQ_4U4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پدر و مادر رتبه‌های برتر کنکور چه شغل‌هایی دارند؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/466042" target="_blank">📅 15:21 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466035">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SRMtM_hSp4iFzsiXTg85a1y3uNIZCGGpGMRLhElTKAvVewOg9QZ_iY7LXm7iXM44ErukoZRI8tflYXiJXZ7ax57WaDT9OSNgO82w-GJRVGnE_7xbpWDmY6K4pb6NeucutQv0RiUS4iBo8Lc5DulbSKLhD685FcxtF4nnmMdH7kdmOC0OZKyZyGAeWEDTidHrN4oyMLZihUCHWXedEPWem2uZdYg97zXJQssL3CU5tvaTwmHKIJlBB4478ymelOOfeeleuE2xaMxyEFWjCkS_yl-P5LnmF-A9m1oyv3hMHQfDBcy0-Us5a04J7cIpVxzMBYfJO6ARmd3aTREukxUEzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jZcxM7pDKy0UX2P4uHbtBvRKj6w9XjfcDjK13knSpdETcfOHUK8AtD3Vpe89t16DjPrbq0AZ7YlEWDBhEXM-AF5BPKs1t2AIJCKlJ6-1Unh2GrUxhA6tHZ766sc91-xPPVAM8RYOQih0dVxcLpHv1WdaJwd7vFzgig0hhuEU72_6zwz4yS02NHTeLyPKED19JmiNFA_Nay_-TF2xxlnoJtNPxENR0hRr4sy9kol-mDheIdc_7h27bjjnGPleCHrCq9Y5sJH-OjPk2rOfuKse_8fV8N-AIyk9IXH7VW8padC3jZ86Bp4U0gA4THc2Aic-QsVVXIeBRq8h86MPRQsduw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CiZkcb__ZHsCDO8uUNT-AW30Z6ryds-ssf8V_GL4zlRDGfGp6Mk0lXtCJ03VieWS3d7uOymJhFRfziEtyG4m1Er9SJZmHxv9hJyANnYsR7jzsWcREeBVp3Hgg-_Cyd1xYfj5QX18NhBBIus6SGbakuuzKEi6OaNPuM_wq91EuSEHzsA2NzByEhkLOJSBudBkRlF17SFZHAByqy4k_WZ700-VQdYiTkOVGCWCJB0bwFUzcFmvkol6aoO1OG5q27GoRnFlhX6ZtW2HriHhTByHofRPpN8A8jKv6UBpN1OyaeTuxwZ1Enbl0SVlh8f9w6QhKoZbSOfiwa78BkRu-tEu2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I4PeYp_n2HCavGA4G2OrdQyVA2763G5A_gdJ6TwEv4siueTDoYyQMj6jXMH_4upvR3PNj_WWNRoJBMyMbtrtjRLRGHjEtX5ydoFJllVil5KtGnVLxhhKup_p_Ac5EZLO62esclwBLNwql2XZlkzZBsYAV8cRIEnT4b7eUEzuwK20-H13bFPB-JiFHl1D2MYxYJmSSM3o87Z1V0MGILbu1w4LOlQPgWWjg_qtrFRMlJFPxuWWe1Zy46aJk-AexSwZnWCEHYa1TAhCOaiMLWXmUTJbjjntz_hQGHqsAcrs7CMvfFZRVWIGkVnCiqH2QTR4QYFskT9pD-heyMQEoJBOAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d5SVBO-fmu0DvXv1_0VI6PmNeFiwBBflZaQ6D14stBHpLbNbJEblPvPqVU_ZvBk6vTAYuoj6DXWxX2EsSPHPzCOnkENaUCR8mfz34akdv2ZXt6ia6zIGdnDlHhnpHMA1zYDPt4ibfmwMvKBmBWlwQtGKYsW_DATVp9zKsHUhMOMfiDbyJTqU0DyWHtkdoT-jVbgceztrN82eEOjebSbpq5RI6vJwyRr0Ame-ETpCTEiPlLvcq6bccis4ndRVIq82q4aC_pA5GsDuVdUP_3-dNVOk8id6FoOJRCEsYoA6D-b80VCi0wx_h8QWI9HZlmaLtyApWaugFEZzzUmvKwhraQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pA3bLomA_0S0K9fRdotlhJ3q-ammiREbuOUJotytuBSS8RRyhW0NjglD5KT19miOVYiVc77sqySx9NshsSU3RjeZICU9LKw7CW_thC1pLYZkbBPVWW8tjlS3VMM2J72LpHCeoad54zf-UgjtxDhWgm9SttXi6zu5RPiLmW7vCyY5SHhjPSN8l5hR0exXmltuqXWN25aPgt4LYbgmgNeZvQLfmewhATehF7CjU_SYuQajxuX4mNmcrhmIRqroxBotBW8kGpVGzqcBBAEdiPtx8VzsEmFyQQDnZSl4ujgkFNRMM3N6h_JhFID_KFCkLE1F4pwyZ2WGT7ghHlW5venKmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r8CRxBlvn32TQEJqgl8sXcDIOlxnb3biH6owAZaxzBzhHUI4LxhY5gk8JpF31dqL1ketKQ_owDuY44iM_YDl9zwfJb6JrD6f_RKr3srROLbV1GIwvcgzhkkJn0f6TaL3KxLkLfGLOVkI3aCgpdh-hWJRMeTU89MOAc8J1chEzqDJpKAMqhcIkin6d5D5vuX8_zNaxG-EWlHCcc2EbkhP28OzEaVaB0_7PSCJsW9i8tCT3WahlgPhKgObl7C6Prh33mdCElZDf3bVZm9_qt-5t__G9nZDBiXcbFWmVwmRHzB4knsv36FHtiAyiHqdRIV0Bf5NxGfzZZA8XgS1L9Msww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حال‌وهوای حرم مطهر رضوی و رواق دارالذکر؛ مزار نورانی «آقای شهید ایران».
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/466035" target="_blank">📅 15:11 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466034">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">🥇
اهدای مدال طلای یونس امامی و بالا رفتن پرچم ایران
@Sportfars</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/466034" target="_blank">📅 14:50 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466033">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8bfc45069.mp4?token=K30CVEULnVqQRu51zjVZ_HjlAEqcZEh3CNj0Jz3o3pI1F1n8YmY08885h2vaZCP59PmFYPvNa9flFLtHjradj3-euJ3eJqp0d7BYIKH519gyyz-uHP-cMvgYHPXRTgWPOtcWSnDdBY7y7Ubb0V9pcXi-A9tuoZ6iLN2HNK8AWlWnvRag_A3-WSwvipTA5-JFEU4b8zU_2r0DSWNA1ff8RtwSAN5YGXmnDbDoUgCBtGugLywQybCd_fIIE6zRPbTjmEYpnA_uqQxHXdWKWkBZDH_2ta5MZ4WDCGKUO7WTkjOIZ_FUh2F8v4hTWT_NXLcd8LolLXBekigqYhBSG2yq2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8bfc45069.mp4?token=K30CVEULnVqQRu51zjVZ_HjlAEqcZEh3CNj0Jz3o3pI1F1n8YmY08885h2vaZCP59PmFYPvNa9flFLtHjradj3-euJ3eJqp0d7BYIKH519gyyz-uHP-cMvgYHPXRTgWPOtcWSnDdBY7y7Ubb0V9pcXi-A9tuoZ6iLN2HNK8AWlWnvRag_A3-WSwvipTA5-JFEU4b8zU_2r0DSWNA1ff8RtwSAN5YGXmnDbDoUgCBtGugLywQybCd_fIIE6zRPbTjmEYpnA_uqQxHXdWKWkBZDH_2ta5MZ4WDCGKUO7WTkjOIZ_FUh2F8v4hTWT_NXLcd8LolLXBekigqYhBSG2yq2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ ‌آذرپیرا طلایی شد
🔹
امیرعلی آذرپیرا در فینال مسابقات کشتی بازی‌های آسیایی ۱۰-۰ حریف ازبکستانی‌اش را شکست داد. @Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/466033" target="_blank">📅 14:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466032">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pi8YzB2l7wJZFIEDs9NEeSxyLp1qOIOq_brU_pD2nv34V-uEHThoZSwC8_H00UaApfCs7yyePckRqCBB6y-bK2ATS6g_SQb6f4MBtD_flqa0UdpYB_gV7WfYAgkfKwO471Hada2BE3fhQklidNTDSS-5IL5_mUh4QRksUV5pAQQDUbJ_JGVtgnG-zpcf5zIQbxi_i68Px0fjXCxhA5_VtmLnvU0HFEamuFkM5nxhEiwz0bhhQ1Zb-cYasYBYg4NDsAd70pScIMpHdDP9COLoyKOkI1q98ExpQ9RKmCT7gzzWh2FMhF09iXwH1VgCIWJm7r7bShj0yuSTE8zWMz-dSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا اصلاح‌طلبان قواعد مذاکره را رعایت نمی‌کنند؟
🔹
مذاکره در سیاست خارجی صرفاً به‌معنای نشستن دو طرف پشت یک میز نیست؛ مذاکره زمانی معنا پیدا می‌کند که هر طرف با اتکا به ظرفیت‌ها و اهرم‌های خود، برای گرفتن امتیاز متقابل وارد میدان شود.
🔹
با این حال، بخشی از…</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/466032" target="_blank">📅 14:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466031">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">‌ آذرپیرا به فینال رسید
🔹
در نیمه‌نهایی وزن ۹۷ کیلوگرم کشتی آزاد، امیرعلی آذرپیرا ۴ بر ۳ آرش یوشیدای ژاپنی را برد و به فینال رسید.  @Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/466031" target="_blank">📅 14:23 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466030">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b0fbc8d7a.mp4?token=N3xxE1B_OTBnw7Oh6oagfQHcqssc_jIDlMNZg29OYB2HyPAb7HM_3zxmK0IrsR4C229YGW0TTZ69T6P72AX7kKNKFNb_937hBbpOKjym1kMJMVwkiV_dMbWtAqw7ytxrj52BPQA3wNjYgH2P7Zj1PAh_cDzCZhROy2O3Nsgm5szL7dfbbyjvEudAwhpcpDDiKsaugOwqGRbQjB_aRkBfGYo1qltLjgpsQm_K2TxRfAfIbDq0uynwR3Quv5HFB2GeYaD0tR5LvPM77StZlwnnOIGtHTJVJCSERy82FC8sJt83K6rjUlO9CBbo5UMUqlBcusFkErZr8ZBMR7Ggk0H5VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b0fbc8d7a.mp4?token=N3xxE1B_OTBnw7Oh6oagfQHcqssc_jIDlMNZg29OYB2HyPAb7HM_3zxmK0IrsR4C229YGW0TTZ69T6P72AX7kKNKFNb_937hBbpOKjym1kMJMVwkiV_dMbWtAqw7ytxrj52BPQA3wNjYgH2P7Zj1PAh_cDzCZhROy2O3Nsgm5szL7dfbbyjvEudAwhpcpDDiKsaugOwqGRbQjB_aRkBfGYo1qltLjgpsQm_K2TxRfAfIbDq0uynwR3Quv5HFB2GeYaD0tR5LvPM77StZlwnnOIGtHTJVJCSERy82FC8sJt83K6rjUlO9CBbo5UMUqlBcusFkErZr8ZBMR7Ggk0H5VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دور افتخار آرین سلیمی با پرچم ایران پس‌از کسب طلای بازی‌های آسیایی
🔹
آرین سلیمی در دیدار نهایی تکواندوی بازی‌های آسیایی با برتری مقابل حریف ازبکستانی خود شانزدهمین مدال طلای کاروان ایران را به‌دست آورد. سلیمی در راند اول ۲۶ بر ۴ و در راند دوم ۲۰ بر ۸ به…</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/466030" target="_blank">📅 14:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466029">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aCsjAWSRdtqaVtnuL4d7ErQoLGpbOWEycGcnUhY5Wb4QwgJOzHyWBM8Tt3GWl8dzQnzzA42ucZSDmtQp48URsECxpRS0a554F9EtTQRvD3UYH-6ZlOzAezLnApo5bke8OnpxMKRMrGTa_ve__t7doDXcnUPLitn4ccldF7GFZ-quGGjNQlQs9da0ncTuxtqZH_TBksXW_UVb7ViMGoafbKSh5mclmVPKxRZxQarctbcDScjilBzd-jjM8BI_GZ9lwwCUTM4rTbGPJf9MSYo4hirBCKbQCRncstc38O6BD7plsUX3yncjrjqxdY8r4u1sFZ6jp5wQphObflBqvn68eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حملات شدید هوایی عربستان به پایتخت یمن
🔹
منابع عربی از حملات شدید و کم‌سابقهٔ‌ عربستان سعودی به مناطق غیرنظامی در صنعا خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/466029" target="_blank">📅 14:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466022">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o5mUc2vKc7Vf9NplBjuYWq30i9M4AvvwPeujy5LhE-5_GJOZiISAQOl1FMmQ_vGcTaA-aMJzMmZNjsgmdNRdqPuNM47l5xUx-yicDuv7PlZt2x5ji_4WjzS8etFBaF5NqNSdUllxEhKLA2bxLYl05P-gXDrQwb53NW8MFYskxfo3r4VMmuUmLjwVfGbsGK_PM6uZtYevE1LOjOIFzcFRIWdKAvQuu7QVRh9vLVOKPAlkFultmI_ReqsqOPDWaYUD8Hvnhm_PafMB-gKqdwB37Sc90SyOmfsRyPeUjBDhyW-czm9zWB3n2DkEmTtk83TJ97EEy1y-_kg4eNJVqR8jkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ml-1HIbP8VHtCJZ5Jjp2txe4sDBl4J0Y_gm5BJocFCxfue-EVp9ShCD475Zxfdm7H6CXQHDR6-cvfKMk_nv39IfeHMsjrj7ht9uFqEYckNsoYDbduxFDNBX4dXAQnsE_l0dYVs_oWNa04via0cKQR3bh9XNeYZmREB2z-cGk6uQN9EULmTcGYTsHUGQLg1FhmTooAzQ97gwr2FgRdIMoqoE8qILOMxDuDXikH6qHCRsw2IQi6Q4O-UMoU8vldGDvb5CL7Ko4ufb3-hOQJ31GNzE4A0lFGsfpaJcgsqxKdAShMJDynTOuDcjc3gHIJJ1W3s8MrcbEahZc448R8L-14A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tlaixRhP3uGBrBgcKymfUhRZMssc1NEoTixrfZzcvdqgBckcOcJAG5Ee5XxnQutNpCrvh1f4WbAt4RPxq4rG3GiN3G0UhnZQGITA-CRzZJjmhNb4fMszWQLlcnx_PFRPgH9VKIt7N8sLMjU7ooP4gDOyQem_znrbtlk6OTJl_YDjT02xi7ce4wOaPonpAj8oUtSnWNpGdiPDwxr2ZuZo3mmMoTUDAft9H9OslVIoIfNrklyzExdI2Zu8m3GoVdAhMKkno0D5b3k1cheuRDwodwGdfp3W7-BCAgOBLkU204M988MNM4A618MWPz-y5okhNjmreipPrI6t6UkxokNsvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u6ZBcdlIy0zx217Ku_Z0C4-ow2oA-mtpSCdUyVGmIvhFgcChtvTbsHmfOXZnbYoFi6z4cYr9eUhB0WwhjaoPn1NO51DBiZdP3ijRlBBdkU3fRgRZx4diq5aAhP7W87ga1ewfhQyVJUuVxzpqGsITKy4WhPOX_wP1rQmN8zuuOrJMlRk6nEuCR83YGzjqe4QXkDJ1GMigPkRZTGYxVO8DDSa6mcucn9JvwiXHsQ9UBCTnbdb1XUxgYf1DgRsWpb6TK70InxAug02Kxm2wu5_uBFSZbFsn6vbSeifG-Paqs3yxIJageEPCk4AvTRIpWeHht1oIUZ17wAXmJ2GHOJkUZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/btBHvWd9Zb2C3WTlXRuZsM5loWbY6AkywLQhPxu_KSVhg3db8uL-z-StvuGsXeb4u4018U_TfbeVXjDjkIea4fAQuM7rNjlr8F63Z89lBWekOVwNBgtDNOFpuMDBKJ7fyQX3Lf5woCsH26UFMmfLTG2StIk23vaZmQtWdpsWh0hugupxCmp0k1AQnGsnHqPl0l9uEtTPGrHKbvE6QLV_xIXhFSWN4EHsaDEUQPcHqiigFGAsGNL96F6bsliiENzS_NctT3zdo4UUkIyPisjd8dMuEgug8vy1ixVjIFhwQOSUCOYQs0v1YENajqqg8xQ8izf38gAkGuOk_vtISFDhKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PezgJfH0DRDDO5_3UNNfmIZAeJRn-CQprzMxNhG1u9xxVX3xZh3HyelTPQIccoysBLDt761Ts2EACxuM51JY_0SfaGaeVs5u8eE6Z_AjwSd9OA8fBXeznJAMzS0Bx6XT6H07BLZuZCIdI0v_wSjQY7dKX8DfGeMPjegdFl6WiUzomRVg4-WvpH9xbeGGcjPk3XVoiONQfj0oBiaXlN1S3ammxPGyBfCtcwNRGbf_qneYAFiX8inZuDjz8e3zaZtkat7oF1A_oeSiCgPojGuXdYfCsKNSIxXD9cpP2aX8kEJezyrvUcFLj5DXX5oyGjU0cpukvM84yifnda2sW0Y4Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OpsZLDoOCwuHQWxI8SwHHZX1-kRQroWik9UteFPPrLMRI7FDvocHm9TBUVsBepLSelBUlNx_alJc-5nAueuxv5GCivwd8XJ8n7E6hLq_prYXJ948uIhzFi1u-_XD9C9EORLYhvik__LD1Dc-L9gYPZhZvAYQdEJPtP0-SrIecRTALEluO0Pp7QAE_HimwLFLZ3ey4dGKzpbQIn9GOs3hB7mM2m4H1HnAwq522IR8QZHhOkLVdy_RtGtUFRN21Nkv5x1bemqg9Tlbh-KRkQiHm3HodmECofPAc8vkRvrNuu5VGzjv0UDG3Y346yIBe2Xn7uR41hpjm2BTQhb_voYwMQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
برداشت گردو از باغ‌های خرم‌آباد
عکاس:
نگار ده‌دهی
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/466022" target="_blank">📅 14:03 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466021">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e10e00e80b.mp4?token=svaAnWGyiejOQy8NcNjuiiU0wTcsGcskzcNe11eNydyQUcO81B06vfsJUYFpiP9J6f6IYxd6TryTyp3oB_0ah0w_RF3jak98u_m6EhbXqRHzWiJrRAYnP_bwN7xXCCYl2sWLz91bT00DCdyU-ahyw2YLdGPFn-OMDyJt03AcKEixRVgn5y5jdmGqnDzhLaIG1pvJhzBpiBU1EgqwqkoY5A__-9TkCtqJuiKRrKmreQhJe7z17Hyc0713iL5xF52WhfKchVmU-Y0YN1JICZwrP9XLrDdgPQFeWqE4EQmgQVFCAKSw1SD3vsJiqb9rpVER811kad7rc-0MnSHwrvMQcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e10e00e80b.mp4?token=svaAnWGyiejOQy8NcNjuiiU0wTcsGcskzcNe11eNydyQUcO81B06vfsJUYFpiP9J6f6IYxd6TryTyp3oB_0ah0w_RF3jak98u_m6EhbXqRHzWiJrRAYnP_bwN7xXCCYl2sWLz91bT00DCdyU-ahyw2YLdGPFn-OMDyJt03AcKEixRVgn5y5jdmGqnDzhLaIG1pvJhzBpiBU1EgqwqkoY5A__-9TkCtqJuiKRrKmreQhJe7z17Hyc0713iL5xF52WhfKchVmU-Y0YN1JICZwrP9XLrDdgPQFeWqE4EQmgQVFCAKSw1SD3vsJiqb9rpVER811kad7rc-0MnSHwrvMQcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امامی به فینال رسید
🔹
یونس امامی در مرحلهٔ نیمه‌نهایی وزن ۷۴ کیلوگرم کشتی آزاد، ۳ بر ۲ حریف قزاقستانی را برد و به فینال رسید  @Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/466021" target="_blank">📅 13:46 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466020">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0309f01f6f.mp4?token=qvyhIOgbnIUXuVn4EaaR63snvgvj6_S2K5LeVkgdrrvmNc9Zo3Y0VmK-0sIp-cxfZPi2Lh9qEXRF2NKFmSslgIe91FsmiWo0FwHVXSWqnIEx8ZHSsbR_C-DAxc1wAzFNc49L9BpAIasOFy-OoS157x98Mk9fsHEr71TZFVFUZmh09cvlf5um7WIMUjh-UIW8GBXLDW9QBPR9DVcWKHRxhhhIquD7onQ6PEUixvBpjMJrfSOggDzKW5Sjo7-XF3weqrcv41sG3pGP1zgyPX6ANdo33EuePFll3BpefgJnBCfCNBAV-xSOP2VQYldbKBNfzaGTc8ZqO8LL5eACXJT1Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0309f01f6f.mp4?token=qvyhIOgbnIUXuVn4EaaR63snvgvj6_S2K5LeVkgdrrvmNc9Zo3Y0VmK-0sIp-cxfZPi2Lh9qEXRF2NKFmSslgIe91FsmiWo0FwHVXSWqnIEx8ZHSsbR_C-DAxc1wAzFNc49L9BpAIasOFy-OoS157x98Mk9fsHEr71TZFVFUZmh09cvlf5um7WIMUjh-UIW8GBXLDW9QBPR9DVcWKHRxhhhIquD7onQ6PEUixvBpjMJrfSOggDzKW5Sjo7-XF3weqrcv41sG3pGP1zgyPX6ANdo33EuePFll3BpefgJnBCfCNBAV-xSOP2VQYldbKBNfzaGTc8ZqO8LL5eACXJT1Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی ارتش: در جنگ ۴۰ روزه، نیروی زمینی ارتش فرصت تجاوز زمینی را از آمریکا گرفت
🔹
نیروهای زبده و تیپ‌های نیروی زمینی با استقرار در مرزها اجازه ندادند آمریکا جرئت تجاوز زمینی پیدا کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/466020" target="_blank">📅 13:34 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466018">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MD7z-52uWf5sY3yI6lw6kBYR6Q7v3FHwxSNX3sIEImw5C-eb75COrC221Egb7_iaTToeiQVItELPl8vMdOjAthrcB1oNL-rT8_C38reKkevnWc-XM8yiUjW_TpzaW9PGlCEaX4ZQLJq92UzDr7svjPf7M-Y-tbeOHyLMU78m5FYR_-a6vhIPtTsE6YSeli4V1vStgiCZzNPdzVUEumxuAnROhn_hGsaM9Bp-BH7jV-zuOgmXfsrwiq7NSELWCCFeW7_fQPHR-8n9N50z1LO2evxkUYG1__tFsLSj3BQC3aYUEKUIhbj-vfXDMZe8lsbqFvl1FT6CR7YHnEXJ8SSvzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bBJlmdgalrOOr-dBijOpeY2poUywGJ8x_pFVe-o9qAhAA9QR55vS_iTquOhAS0K66kTqNtmYoxVw1knz-DL_riQuVnkAp_KUbhKRohtNiWSDSMjhZT0F4wMqI2ssmOFMQUYy7k5zcvthPsqftCY28TVTjlvENy4swmZ7Wauj4T8ov0a67AMij0sOiUQKgfnPcv-ifp9gbsdBU9n2PFE6Y57vKwv4G7AvzbIrVsQhEdIrYdvtze9uF1GJ1hLDr9QcVXyXTIao8jsglrLYH69VDD1AWEBduSCGclTSI91jsSi7ZaWeuc7zBy2s8_a7XVHeyxBmqmPMW6U-GHP1QAnz6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
اشک‌های حاجی‌‌موسایی هنگام دریافت مدال نقره
🔸
مهدی حاجی‌‌موسایی در فینال مسابقات تکواندو به حریف تایلندی‌اش باخت و نقره گرفت.
@Sportfars</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/466018" target="_blank">📅 13:13 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466017">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">وزارت اطلاعات: ۴ شبکه خرابکاری خیابانی منهدم و ۳۱ عامل مرتبط با دشمن بازداشت شدند
🔹
سربازان گمنام امام زمان(عج) در اداره‌کل اطلاعات استان کرمان ۳۱ عضو ۴ شبکه سازمان‌یافته خرابکاری را در سیرجان شناسایی و بازداشت کردند.
🔹
این مزدوران برای حضور در فراخوان‌های سراسری سازماندهی شده بودند و کوکتل مولوتف و ابزار تخریب دوربین‌های شهری تهیه کرده بودند.
🔹
اعضای این شبکه‌ها در دی‌ماه ۱۴۰۴ نیز به گفته وزارت اطلاعات، در آتش‌زدن فرمانداری، تخریب بانک‌ها و ادارات، تخریب اموال عمومی و خصوصی و حمله به مقر پلیس با هدف دستیابی به سلاح نقش داشتند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/466017" target="_blank">📅 13:01 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466016">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uhZwfkeH4kRG2BBsfmLQCr07yLLH3fYJu3j88KPZ5DRgCksBh4hCbrdPR8OXkfgSR74yCjHRYGzKWsOHOLYeNfk36BV3rf70syqm4z0mZsFoogu-U6qdndAgz3WIDmpHCgO9re1OK3Aw8qlwGaJLzjTyjkviVxHgMNpOyWvLjJjWdjLAN-w8J2lI_Rmv1nRXRMEN18xqMmXFIwHJhcNHJn52baygzbms0DM2EEt0qZCEHOEy_jY5RU-FzeykLq8UB572aA2Xm_WJRuhuy_gPScSctc1zaCzWoglHU1cdkfZ_s_DRkZHpOmTd0ZvWkf4ghF_BspzOSTHLvO_V4pjBCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آغاز هفتهٔ بورس با عبور از رکورد ۷.۹ میلیون
🔹
شاخص کل بورس که امروز رکورد تاریخی ۷ میلیون و ۹۰۸ هزار واحد را ثبت کرد، در پایان معاملات به ۷ میلیون و ۷۸۸ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/466016" target="_blank">📅 12:37 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466015">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">تیراندازی در مقابل دادگستری مهاباد
🔹
دقایقی پیش در مقابل ساختمان دادگستری شهرستان مهاباد در آذربایجان‌غربی تیراندازی توسط فردی مسلح انجام شد.
🔹
پیگیری‌های اولیه خبرنگار فارس از وقوع تیراندازی در جریان یک درگیری خانوادگی حکایت دارد.
📝
هنوز اطلاعاتی درباره شمار…</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/466015" target="_blank">📅 12:35 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466014">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f96ccd1a9.mp4?token=lHbYSOCvxfP2SgfSs5nTUkOHyphNZYvtj1lWw5RJvqtJ0_rEX-yjUDuuXQweyjt4cqsvapB_2TitiKrWHcLuSCF7Mfab0_TzoxY5Is7-NqNX8I3dt_WURgHa-l3hHQpzXecXu9LXZg1AFoLQ9nJgdo7_kwkUS8cRG5AJ38dN-tOAwGnrjqxEIe2e5ot1NIzI-lP19UBdOPS16j19tye2aEp8TWe9ltG5QmS8i6pfDv5l6M7uA-gD-FEBoWq0dfQ2NPtrbSoGr2VwL0l-WhSNK6exBhiITnlew4bF7gQyWIJIZ4zA9d9aCRtStZSS0up1NFCib73HoQN4Tm4KJuGIWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f96ccd1a9.mp4?token=lHbYSOCvxfP2SgfSs5nTUkOHyphNZYvtj1lWw5RJvqtJ0_rEX-yjUDuuXQweyjt4cqsvapB_2TitiKrWHcLuSCF7Mfab0_TzoxY5Is7-NqNX8I3dt_WURgHa-l3hHQpzXecXu9LXZg1AFoLQ9nJgdo7_kwkUS8cRG5AJ38dN-tOAwGnrjqxEIe2e5ot1NIzI-lP19UBdOPS16j19tye2aEp8TWe9ltG5QmS8i6pfDv5l6M7uA-gD-FEBoWq0dfQ2NPtrbSoGr2VwL0l-WhSNK6exBhiITnlew4bF7gQyWIJIZ4zA9d9aCRtStZSS0up1NFCib73HoQN4Tm4KJuGIWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدال برنز آرین سلیمی قطعی شد
🔹
آرین سلیمی در مرحلهٔ یک‌چهارم نهایی وزن ۸۰+ کیلوگرم تکواندو بازی‌ای آسیایی ناگویا، با «هائو تانگ» از چین مبارزه کرد و دو راند پیاپی به برتری دست یافت تا ضمن صعود به نیمه نهایی، مدال برنز خود را قطعی کند.  @Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/466014" target="_blank">📅 12:26 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466013">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/izi3Poz--GNGTxJhC0mDe7uEc45b2YWJdbHBQ0WtjqvW5-nxjWSnvINujIeyyWzKoNChLuYKr5KLa-uv-Y_y64QbB_iGQZJYErY1dj0cgQKoZs13VUTGKHKk_t200WCGqEOKgezKJSDu1z4ZnKmS_Zc6inc0LrDAJdFtZB8Rv2s36aWccOqzphqdMwRqJ24JjXzGKS0q4fieYDA87tWske3Kc-_bs0oYZYjlEo7qvTEwbU7R7OZ3zXHO-GvrgO9-TBbXs-z5EARJ0v0z24hgZUvHWqMBPaoaJDJOkwc4jVMTyfLdJTjowlsgGpIFeO5mo__jur-2LcEnH_jJPU-thg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرلشکر وحیدی: فراجا نماد پلیس مقتدر، هوشمند و حرفه‌ای است
🔹
فرمانده کل سپاه در پیامی به سردار رادان نوشت: «فراجا امروز نماد پلیس مقتدر، هوشمند، حرفه‌ای و متکی به پشتوانه مردمی است.
🔹
فراجا با تکیه بر نیروی انسانی مؤمن و انقلابی، توانسته است پایدارسازی امنیت و آرامش اجتماعی را در هم‌افزایی با سایر نیروهای مسلح و نهادهای امنیتی در سراسر کشور تحکیم بخشد.»
🔹
سرلشکر وحیدی همچنین با گرامیداشت یاد شهدای فراجا، از نقش آنان در دفاع از امنیت و مقابله با اشرار، قاچاقچیان، مفسدان اقتصادی و مخلان نظم و امنیت تجلیل کرد.
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/466013" target="_blank">📅 12:14 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466012">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">تیراندازی در مقابل دادگستری مهاباد
🔹
دقایقی پیش در مقابل ساختمان دادگستری شهرستان مهاباد در آذربایجان‌غربی تیراندازی توسط فردی مسلح انجام شد.
🔹
پیگیری‌های اولیه خبرنگار فارس از وقوع تیراندازی در جریان یک درگیری خانوادگی حکایت دارد.
📝
هنوز اطلاعاتی درباره شمار مصدومان احتمالی این تیراندازی در دست نیست و اخبار تکمیلی متعاقبا اعلام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/466012" target="_blank">📅 12:07 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466011">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">تشکیل پروندهٔ قضایی برای فوت ۴ نوزاد در بیمارستان میبد یزد
🔹
دادستان میبد: برای فوت ۴ نوزاد در بیمارستان میبد پرونده تشکیل شد. احتمالاتی چون قصور پزشکی، قطعی برق و مشکلات زیرساختی درحال بررسی است و نوزادان برای تشخیص علت فوت به پزشکی قانونی ارجاع شده‌اند.
🔹
تاکنون علت قطعی فوت مشخص نشده و در صورت احراز قصور یا تخلف، با عوامل متخلف طبق قانون برخورد خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/466011" target="_blank">📅 12:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466009">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ki6b4EmtwBacD1sdzIz5vIggtyVcFNsfkBBdBn_vVoEQlVtrm4dnfatEo28CH1R37aRI85WcOPi2WTBF5MA4lvwxtE9Tx3uUGDsZPcpw0K2aeMEic6KHF16tv_0Abl8_H_NcWeYEG8nHtnFZWY0n4ifg2vXiPHowI2jq4dKL8RcNEy2gaJ4IRnUHhjpDAQ6C_4XTOQLxU68VAgqt3qqFwgUx4tojjefGfNTG7DAvWuChlddbakpkup9UChiOIJn_Du_130xoFiA0xqDyHLHlFIGvQPYozXvhuPTkU4Q3Pm7i4FFZqNMxLVTL8u76x9ZRQPh5YmoyHIeUjlZAV8CaHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UZu_MPjmaj-mh0r5txVaDOSCOT5YFI7rgWgiLhwra4awJHCG8rgOfyRtpml5yO62LNU2hkBGvht7kGRDrLWszsatHkUGFpjjyIULsKHsAnWHknkf2YHwnaUqUGY_rOdjeS3cR-TnonyhOLoKWOUYMs-3JAfZYjeEjDTXL7pRSTHzJ4n9BDAUkoaBvPnxdbnLlDwiY0uZJi3Kl23wqCPITitkTliyxpUYDBh4aEAPBNiWAnQa0pEz-UysH_cLnjJxuRH2OAnNs33vrH9WK9OEb1WZX_oWnJzkg3BOFM67QHKkRDnsnRqG_mA-GFCU-SUmJgdWagvXr-VKkR6cwL7vKg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اختلال در فرود پهپاد جاسوسی آمریکا
🔹
یک فروند پهپاد شناسایی MQ-4C Triton نیروی دریایی آمریکا پس‌از آنچه به‌نظر می‌رسد «فرود ناموفق» و عبور از انتهای باند بوده، در حاشیهٔ رودخانه در نزدیکی ایستگاه دریایی «می‌پورت» در ایالت فلوریدا متوقف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/466009" target="_blank">📅 11:57 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466008">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدانشکده خبرگزاری فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gJQ4cF7P6jC-QyUSgpgs_qt1WaiBG41L0LaSFPbVGzTYX6uBL-C4nb_zfHWCMxRkfaOsFxnZP6HcRWJJAPAL3T4J8o2wXjVOSE3KdmBisFzZyGTBn-sULGdsY6Iz_4OdFTpCD2PJWFoGaBEvrB5XdX8z-Vp-KoNPTTSJIPJq_QRFDT6Vfb9mjGQCCAbkRi3S48MjyKd8OYN_XTx0B0fwn8tpsoqnIrcEKy_2YnXNPojgvh7-s5hR5wSOyET5EPde02odP2dcRTAfA5ryNtC-SwOT0V5c0uGeyXEI5lgf4P0-nqHdigKgDCXehS-UT-m8I63hvfD9j17uFVooJMU5Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔰
مهلت ثبت‌نام و انتخاب رشته در پذیرش دوره های کاردانی و کارشناسی ناپیوسته دانشکده خبرگزاری فارس مهرماه سال ۱۴۰۵ تمدید شد.
🏷
براساس اعلام سازمان سنجش آموزش کشور، مهلت ثبت‌نام و انتخاب رشته در پذیرش دوره کاردانی و کارشناسی ناپیوسته دانشگاه جامع علمی کاربردی
از امروز تا ۱۳ مهرماه تمدید شد.
📚
رشته‌های تحصیلی:
🎙
خبرنگاری
📸
عکاسی خبری
🎞
سینما‑تدوین فیلم
🤝
روابط‌عمومی
🎤
گویندگی و دوبله
ارسال  عدد ۱۴ را به شماره ۵۰۰۰۱۰۱۴
🌐
لینک سایت ثبت‌نام
🔗
futurix.ir/go/rxDxXO
☄️
☄️
این فرصت رو از دست ندهید
🎓
مرکز آموزش علمی کاربردی خبرگزاری فارس
🎓</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/farsna/466008" target="_blank">📅 11:54 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466007">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4d0da5230.mp4?token=gKpzMBoToGQcngRUkJX5-WruPiINGfIlOSW1umTR3gOzCpFxE2Eqy2SkAV9YevLI0BdYIgiAQ4ejEj2uL2aV7GLMhMg7ImBc8ciWIyj8uwxJpsbbpzYLsFGCxL-6UJXJz_MCoyw_CJW_R9A73sawfC0hLD1XCR41MvanwfqOVud8XKFZjq2Nsvr2f0cmCzUleQC3zIZRL1XZurRu5Q-F_h3TEhHHo8jaj34VY5f6zpINdh_KFtZzcGhc9uZBVr3-cnJ3gthb8URGo1n_D6v7a9bNE8Au2Noiaw5QQL0MBieiAAjR8YQOml2cwMVS6KTFPdoNGf-efShs77GNN6_C-Z8qZV8tKvEwC8EO8iO5hCfNMiMc0eQDo3iqm6Xk0XUgCP3yV1JHxLi1eKZVFEKdTljPq2h_65zgcHRKKXNjWCbCIYL_wz8jmouqhHS3WYAepg5o7G4HtCDqEv_lTTdXtIAmD2sssvOqmjN1LKu5cPDkiJbkkeFMBb8yOHk-hKOMf-3j6hFkOiXFLWugA8mJvZnvNIIfiV0rFPhWaik-1AkweHpMiNrSjKIU-qzuEzanHDXVJdkDKEOnBlDozCJjqgrXCgqQ_Nx1jlj8XPRNEVibUmT4NiUPd8JLuUpcHBNwW6ruuQX4tJauF4pE51OvrJi3mWVgC3VjVEgKCrVb5MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4d0da5230.mp4?token=gKpzMBoToGQcngRUkJX5-WruPiINGfIlOSW1umTR3gOzCpFxE2Eqy2SkAV9YevLI0BdYIgiAQ4ejEj2uL2aV7GLMhMg7ImBc8ciWIyj8uwxJpsbbpzYLsFGCxL-6UJXJz_MCoyw_CJW_R9A73sawfC0hLD1XCR41MvanwfqOVud8XKFZjq2Nsvr2f0cmCzUleQC3zIZRL1XZurRu5Q-F_h3TEhHHo8jaj34VY5f6zpINdh_KFtZzcGhc9uZBVr3-cnJ3gthb8URGo1n_D6v7a9bNE8Au2Noiaw5QQL0MBieiAAjR8YQOml2cwMVS6KTFPdoNGf-efShs77GNN6_C-Z8qZV8tKvEwC8EO8iO5hCfNMiMc0eQDo3iqm6Xk0XUgCP3yV1JHxLi1eKZVFEKdTljPq2h_65zgcHRKKXNjWCbCIYL_wz8jmouqhHS3WYAepg5o7G4HtCDqEv_lTTdXtIAmD2sssvOqmjN1LKu5cPDkiJbkkeFMBb8yOHk-hKOMf-3j6hFkOiXFLWugA8mJvZnvNIIfiV0rFPhWaik-1AkweHpMiNrSjKIU-qzuEzanHDXVJdkDKEOnBlDozCJjqgrXCgqQ_Nx1jlj8XPRNEVibUmT4NiUPd8JLuUpcHBNwW6ruuQX4tJauF4pE51OvrJi3mWVgC3VjVEgKCrVb5MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حاجی‌موسایی نقره‌ گرفت
🔹
مهدی حاجی‌موسایی در دیدار نهایی تکواندوی بازی‌های آسیایی مقابل حریف تایلندی شکست خورد و به مدال نقره دست یافت.
@Farsna</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/farsna/466007" target="_blank">📅 11:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466006">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UTaOcPF6-D81vvL3pRYbmE9IK-elrhFKmcBnxwcfgKL8UR4txWSwLvbvBVyqLD9lrX8k9CF-9JfpeYKUzp44zgktb22RGMg6sMQqJiFYFH_dGevrF6c3alvRc8R2bUDvbcfwK7eUBPVfrSsdWIL8JglGFZCZMtSN3hSzr3RsRZCSwU3TjnGU1N7fFjUQ3VN0wRQ8Od1MUS93TZh5sc_RPsp8bnH-t7ByrZOvDGNdXEe4O1MJacqIXmwa0waHaeLfxrY5x0VaRTF1FGQzGVjUQL2hl9an7SzL8uC_4Cb88SEIWtSYIqiLgU8k1uR9prMYs9b-PIPUmc_yTItD0vJi0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمادگی‌ وزارت کشور برای برگزاری انتخابات تمام‌الکترونیک شوراها
🔹
وزیر کشور: با وجود شرایط جنگی و فشارهای اقتصادی، تجهیزات کامل و کافی برای برگزاری انتخابات تمام‌الکترونیک آماده شده است.
🔹
تمام تجهیزات، دستگاه‌ها و تعرفه‌ها در سراسر کشور توزیع شده و آمادۀ…</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/farsna/466006" target="_blank">📅 11:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466001">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TBCp0YtFz4dhm0gwDwOkiWPHEOU1DGuDQRIb_EdHMi7J6OJp1sNLEwyn5CXjcj797UGVQ38_8FCTnLRTRYL7zLO5O0Zazv-FtNgyxNEb4twB0-mOfPxwNn7NLtZdlFtWMrlKrVV585q8_7LZ8DH0D1rJdC4qPLL1o55htNbaG5M6XMzkWMhX9Xt_Zr6-laXJa3QF-FvGLKyD8SZErRC5TiuQ8Q8AMltYTZBVBRi5ZbJOmemQtF4tODutAG-R-5tE3PZmtPCIx44Q-DM13k1BlDC2cTEaL4Oy6cg8y0fZ_-UIVeIgzMWMVDc_hcBAM6uZgjJQiuKVHLhuFtx0vi5Zsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/puirWOTuT7rTFglLJqmIJoUVKZ-yB-jTsHtkCwyytCwhftFf9iz2h7r5Pv4dhgan4ak1V7shLcZlztPkj-DAXTuZh7u-Mo4zu80uu0yS-hxe1YBHY7vdCrKn98GHU7BVfEmSGiR6c5IHKs6FZbEfmNwUM4CY325gcW6J4MIG3_aabZkbuf32F02ArLOOdtvD8bf__AjKzsckOab1VFhQ52RssROIR_4U-i8wxTWnNmrK9KNtlH1WcF65GydH1TBmdJaVmhzRj0m1wbXeDnxNeH-r0uf7RbkGa5_MM9glowM5mTSiD40s5qzVgYZEcqVSa4MVfYwAQzaRTiVZ5aiQBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vHfYbctcbi_UyiDSLfb42PKy4muwNzsBvqtrws2IpThL7E7rJlwuR_7Zum93kMEN51gbcnfDrYCsnB-YCKAbDiy092y3gZRNJZU7m_EOtqg2ZsCR7v6oXxdxCjLkPcBBGC87-NrGjX0Dl_yd96S6IGGE73PJwt4ulYyaGnCWasgp4cSSs4d-lDSC5p6Y7HTSbrA51zkNQwXrLrKOQrEivXMZiLVbpJ3F7NEQiVTOhkZVTpe5t4pvL-OiYtxzp2lZoavVwYFgoS75EYowxmzSEl4uWD5dINGBTxa85YyNzV5PCTJJqoSUlqwCOiNGNeLaDtxixfXuTlpk99mM4-0z2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OGuIKFHp7_4wRuF-uscxwIyC0h-rhhOFcd-oge9rrv8kbA2XMyiahNR_h2ehzI2if6_YxVisSGmdBIhuwgpFZpavgRCxY0kad7b5Cr5E-81ixOkO7Za8Ia7LyrfwqteK9mmE1cRBrBAuRqyQNe8EUFaH0gYCc6QSqeP_t8UgkqdSEePkhMdpwfZrQlzIRq_Lwd408SnaGnmygIXMmm9Pn9YsXBN7vAt3kpITuPBbbwVdUNLk-XGDTtaOxZ2u7kFoo66B5AWMK20YzrjUjpJW-TAtRtNBT7KXQnOQPdiD7kdxIU5eKQ9jg_aYJhiICKgH9t2QdJeAZuZsnIx747KReg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GuolJ9OMhW8O0HYaq1X_CEAubA2iqXYP6cdLogMB4lm6EzkOb00JOYbWs43fKKm1Aw74p6pGrL25KVesrLimgSXn0a1XcjW5BN-DuadQozdUIJMdde56dxjG2Z6s698trfRvJ1jQh-G30tl7zPG-7e-E1EckBM4RLRSFDtPwWJfkaCjmUXe9-CnMoPDCVqjYK7MIBGBy4p6UaS-W_gtSs3GLchmVZBJibleOad08OniYtuXGjqJyNwma62-TNa1f5nJn1vDr_U76dvHlu0FLA6_GxSh49wQ2qcvS2z2P_zx3LzXjHBsQpEucTFTjtSOfTbkJpgBv4HSK-68Z2-yevQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
روزهای برداشت پسته در پروین‌آباد مرکزی
عکس:
حسین شاه‌بداغی
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/466001" target="_blank">📅 11:37 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466000">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q2BOf3J_z5PozYWkrHKwUBmPaytcpRxvLKCqa5RssrhOYRz7wWUfW2EvtjCWI3G2-WO3yfr0yZ_4Q9bUZxuW9RQmRpOFzrLa_CQDYAAWn3b9k9-CzAsNGB4XLAWm3UVSfuauCPTf5N_VYNYB2mUuB5LJ7XKHeq5Mfiao55CvVg_QaDlFEn8NskPqWIVG95GG_sSSLawCooRZMuAjFEh7KDjODeCW4cDYT_ORlkWabXUTYrJiCo5YAVACapSFhKHmVAPuiXUKXpRo3-wJ9ND4Mg1dmWUstJe_DQ53vAS5yIWvClrgq_6xLjSiYP9dOMHGNty9kfYZc7Y11x30i2aK0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه پاکستان، میانجی بی‌طرف یا طرف منافع آمریکا؟
🔹
در حالی که پاکستان نقش میانجی را بین ایران و آمریکا برعهده گرفته است، وزیر خارجه این کشور خلاف تفاهم‌نام اسلام آباد، خلاف خط قرمز ایران و هم‌راستا با منافع آمریکا، خواهان عبور نامحدود کشتی‌ها شده است.
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/farsna/466000" target="_blank">📅 11:26 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465999">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84cfdb285d.mp4?token=Tg6vwd9IJTmvCa5lq7hicddPKv7N0ZJHl8oZC6tr4R99MR7qR1ALnjjA2HYb3tCEtw2VIRh5Nygb9maR90-DSu3xS15YsPTvuY8QMDbQVRr301wT69LBwmAzzaQFaqHyAfjVqagm8GPPFVgRf7fiRhJxRykZPqhNeCBN6SdhuhwJq8HMrziGlkoa7dPiWtHpyoQesmbwRzRJ6ItxzIQbTyHGryhPPzgxfO8My_GuzQaBhsUflm9P88PEvHbwatC5sG69sV1bNFXLOE5ZazJThKhI9IVfBx6e6Ny4tgARK3oE8ktGpWbNsN9wiJo43YmwNuXReqOtdGNuJ_R9ZJfc5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84cfdb285d.mp4?token=Tg6vwd9IJTmvCa5lq7hicddPKv7N0ZJHl8oZC6tr4R99MR7qR1ALnjjA2HYb3tCEtw2VIRh5Nygb9maR90-DSu3xS15YsPTvuY8QMDbQVRr301wT69LBwmAzzaQFaqHyAfjVqagm8GPPFVgRf7fiRhJxRykZPqhNeCBN6SdhuhwJq8HMrziGlkoa7dPiWtHpyoQesmbwRzRJ6ItxzIQbTyHGryhPPzgxfO8My_GuzQaBhsUflm9P88PEvHbwatC5sG69sV1bNFXLOE5ZazJThKhI9IVfBx6e6Ny4tgARK3oE8ktGpWbNsN9wiJo43YmwNuXReqOtdGNuJ_R9ZJfc5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بوسه حسین یکتا بر تصویر شهید لبنانی در منطقه نبطیه در جنوب لبنان
@Farsna</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/farsna/465999" target="_blank">📅 11:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465998">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e49ed69e1.mp4?token=orEZdIT0RWFeeELP_5OreYG_2TRmmWp_p-zYitTZQVcAzzvee0qNBqlSM5SLOZemD_GVzcAn2u-jhcP-Eng8V5Ux3kV7S2y11C7IaBnr4cPYDLGkPBUDdpy7Woz8lrfcC03D9HrYttZkhwvlLkV_f6Bvp4UkBWx3StwH0n0uaCH-Ism1wxc-91PeuHBZj1lhD5c10KHf46ix0CWFI01vpVUuy__kfSGLnmUOCk65Mk1R8EaQjz7fzMj4AlwOJ4551_l2kZUDuFsat-H94UjPPhnx-gNNA-lo4qT50Mh33EcmJvac_kuKKCqL5oWRiec8cjbCMJq7RUYz8YNRchJt8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e49ed69e1.mp4?token=orEZdIT0RWFeeELP_5OreYG_2TRmmWp_p-zYitTZQVcAzzvee0qNBqlSM5SLOZemD_GVzcAn2u-jhcP-Eng8V5Ux3kV7S2y11C7IaBnr4cPYDLGkPBUDdpy7Woz8lrfcC03D9HrYttZkhwvlLkV_f6Bvp4UkBWx3StwH0n0uaCH-Ism1wxc-91PeuHBZj1lhD5c10KHf46ix0CWFI01vpVUuy__kfSGLnmUOCk65Mk1R8EaQjz7fzMj4AlwOJ4551_l2kZUDuFsat-H94UjPPhnx-gNNA-lo4qT50Mh33EcmJvac_kuKKCqL5oWRiec8cjbCMJq7RUYz8YNRchJt8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
رتبه‌های برتر کنکور امسال از کدام شهرها بودند  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/farsna/465998" target="_blank">📅 11:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465997">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35dc49736a.mp4?token=cxyh5zmHk6BB1mzm_NsRmTDmtb8oGH2cDWShykuqbx-qWbISupzDzHK84cA_THFeUqAIh5Kx9zmqwMuzf10RLPxge_NVmPHeU0LpE48hG-gd7f6pg31AblvGlvLOzBFGEQC5NcBHbMqmpK1at7kj7O1Th_vmOMrpnW3gQt9OiS31eGFlYOh-iMxyQXOu-yb2X5KsM_KUwgqrUmqE4SJb6NbNx5NkyoQhVBSeA5phaJyp-YkP2l0qS_-f9PUNISY7fT_izAooPX5_J_4p2rMzUvWa0eZu8twQ1FD2TJibQr0L69DZysCM2k7GXF4VEy9l4yijZoH3tHJOB8Hyi4n6YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35dc49736a.mp4?token=cxyh5zmHk6BB1mzm_NsRmTDmtb8oGH2cDWShykuqbx-qWbISupzDzHK84cA_THFeUqAIh5Kx9zmqwMuzf10RLPxge_NVmPHeU0LpE48hG-gd7f6pg31AblvGlvLOzBFGEQC5NcBHbMqmpK1at7kj7O1Th_vmOMrpnW3gQt9OiS31eGFlYOh-iMxyQXOu-yb2X5KsM_KUwgqrUmqE4SJb6NbNx5NkyoQhVBSeA5phaJyp-YkP2l0qS_-f9PUNISY7fT_izAooPX5_J_4p2rMzUvWa0eZu8twQ1FD2TJibQr0L69DZysCM2k7GXF4VEy9l4yijZoH3tHJOB8Hyi4n6YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صف‌های طولانی بنزین در امارات
🔹
درپی افزایش ۱۶ درصدی قیمت بنزین در امارات، خودروها پیش از اعمال گرانی برای سوخت‌گیری در جایگاه‌ها صف کشیدند.
🔹
افزایش قیمت سوخت درپی بسته‌بودن تنگهٔ هرمز، گرانی نفت جهانی و اختلال در عرضه و انتقال انرژی رخ داده است.
@Farsna</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/farsna/465997" target="_blank">📅 11:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465992">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LwG_g_j2bfWuG_CrLYhMp4o0d9XQfFvq5w7hdbiQpg1QbHR4Zt9TfCh_he9qRYddVMWBh2q8TwMcOxoFxlCEBiKs1MVOww1w370auNLC7HzLynkxuBbyMaOycW3BCTZSVK1ph4xQul-Mn4ZXTHBsnj3Byrw7155KDDptV2hLU9e2V1Y277GapMHjarFgGpaFfOXLtBeKgnO0S_GYiRi6Fvrc6GrQFFuVcG9Cdbe-Qh8mc4Zx6uyzNp0TXY5q4PFg12_yhuXOMrKNsuqT7xmxwJL73nw0KAmr_Qi-WwkDqtcoxfu0WhsiEvcZvAxBlvJOL2i5Vljz7dkAaN9yrdsUWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uKK1Ijomhw3VAzOwqaXoymAV-mKz6cL3IqXgi2Js-2BW3Vg_Ppj6CTySkUFR5y8ygUSjCjY6P8sxl4qcSTRMxmGqM6jFH5gLxAm9eNvPioFyN-NE-YU5_guDwabEgpHJzfijl66ktfaWB2K-XuFGnILTszqmuDGxAs7ggpmyb1yaxrc2VTKm_NdcU9KeamK1rAVM9Ybmz9WynANGmG20jjIORjuFtzVJtzISMxuLJnhR0zvhx6lGhjOcotRi_PP0Bo4Qk_qBQabD0DiaChILLeKVgwHRDT0GEMSmqDoBCy2urHyh8GDOVz71-EWt-ELGNMBtaRPAFdgg0H3pcQ-UcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u2Ru5-Tlcw97SaElF6KC94NeS3taJFDVHvYReKHXfBIhG6xEg8ij5b8BJXtojqLtJVl9yO7utCwwju30yBXZfzQNrfcmztx0cT1G5CrFTnU4Z50KukSZYxfY2bEgNDL4MvdRVj7SBYPe4whVevJeMRbMyztW8LmE1X7pQqrmzLkecTTJXmIMy7F54Pam9UkY0noRs-JA-DU_7y22Sr6yecUoQhfl0U09acCZ392jQrHSC7c-MEYx5ebMGGiHMzViCk1CInT_7XyHMARvQhjsgxKvlUMuxsCqycXRhwWKtCxgV0j7-m0EpCdfcstd_ANBi9n3dHush4QEvrtdNdCSTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nTHRtR4xz6nOwdKLMmAS_JqW05IV_HAbZfUgeJM1BhU0hObHYIDTwAkiwfWyC4W2US6GwjCRDXP1Fvbgv0wkRweLgglbxPScGf27vb1Q-5kMeZwNXzAAjFLJMowISOlVcwJUD2Kkx00P4WEqKAAgFIwKKWI0LO2gVrQJ9XR9YrsiTWIGX29F41uV2ygSR_tIwLtoPwVNd8sfaApKqXTsjWs6mS_ENykHRMYNR_cZtTfX58JZjIB6t5MY56JJ9GQ06E9H4YOsMc-yOhrKwWo5tX44v3jRxedN7x-dyj4Jv5abjEOWnrw0T5Js76Uwy96JLieQmVzjETp39yltP4t2nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SF0KngjQ8IJSaVw5ynkNHBRhN4MWDfNW6XKrAhxIWHBscAaSdgyucd8AT4CcO8dVwD-LseAk9teEcn41KOrieEMMGGjZhAYbTF5EY8UBJu2GGq8_SE2VBzO58ZcBiLPCqY1jqnU0BUTG2eebtDBLWdTows9IIbWgpfzaNCwnaHQ-zmpVuwkfmdMyj2NvUxB3X0cBsCjcJZgN3QFVMEEbqTgut88crAC3zYxUlvcMGxVXZmaafV9yeR7s37Ygwja8Y_umWerswCuCkwKOzOj8F-wnJLeHWLUnueoOV4olmp3kOeVzx-gBZXfchFECT4PdxPMNkcg1KuVQAt3xTRZYzg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
رتبه‌های برتر کنکور هنر
🔹
۱‌. غزل کرمی
🔹
۲. هدی ناصری طاهری
🔹
۳. ملیکا شجاعی @Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/465992" target="_blank">📅 10:51 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465991">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5d8a9de0f.mp4?token=MAgadmMe1iTsfdNs6D9lg-4FGzldAL3S_WEQeaMau_lMHxU__pgMednj6pYNTxDbo6DCxR2VfkOPUE0j3gosLC84DCqQcgHa-T0dyzv83TjDsBjFDffOLMHLbMpgT_1KlCZc_o1BvlqblUhODOCQpYYL07woyTmwaS4JKlB9cU-TKM7z5kdYLj_K3DU210aWVle4OqtjKJxTaP_eVuhoj3y1e-4GA3a7pf8rpGX1AkKPx7jnbN3Rp5KSS7Sxupfw2Cy2RZIarKPxCMTHW5jhp8xyDcupR32hf3g0yxZIuLLH4O2KRo-HyZ3jav7M51Uvv5R_Zx6TE_njsxpxqXW0MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d8a9de0f.mp4?token=MAgadmMe1iTsfdNs6D9lg-4FGzldAL3S_WEQeaMau_lMHxU__pgMednj6pYNTxDbo6DCxR2VfkOPUE0j3gosLC84DCqQcgHa-T0dyzv83TjDsBjFDffOLMHLbMpgT_1KlCZc_o1BvlqblUhODOCQpYYL07woyTmwaS4JKlB9cU-TKM7z5kdYLj_K3DU210aWVle4OqtjKJxTaP_eVuhoj3y1e-4GA3a7pf8rpGX1AkKPx7jnbN3Rp5KSS7Sxupfw2Cy2RZIarKPxCMTHW5jhp8xyDcupR32hf3g0yxZIuLLH4O2KRo-HyZ3jav7M51Uvv5R_Zx6TE_njsxpxqXW0MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رتبه‌های برتر کنکور زبان‌های خارجی
🔹
۱. ثنا اکرمی
🔹
۲. سارا اعلایی
🔹
۳. ساینا دهاقان دهنوی @Farsna</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/farsna/465991" target="_blank">📅 10:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465990">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/698d1a0e28.mp4?token=GpG1W0M5nJ4nUM15WXh4o9GLfODhkUE28y1PQuP7xjjowj5cM0VWDJVyDpw7icRhqwK_E6fuBB0mKq7C3FlEmqGAoz4c5F5E52ZCQCSMAtFpHnEJDjya_XlUyNxEuy0TABWLJLvdSzPTlIWDfKkXrkUX837T9uvSvK2BlsEJlDMKP9vA8HSSYOnRZFqdD5AwF6kNfcLu3bqyyTid2hobUZ2zBQDAoWeC7bHgYcpwLm5jZWp1t5i8S6xRQuPKz8cHb4VVzQ6_c0XS7UPGX9vW0MWa7CxOQnM4c4ARfqpA1UpaZ7uOGY-Ec4LhozI7po1l-TeymcVavmBQFTuHysjjiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/698d1a0e28.mp4?token=GpG1W0M5nJ4nUM15WXh4o9GLfODhkUE28y1PQuP7xjjowj5cM0VWDJVyDpw7icRhqwK_E6fuBB0mKq7C3FlEmqGAoz4c5F5E52ZCQCSMAtFpHnEJDjya_XlUyNxEuy0TABWLJLvdSzPTlIWDfKkXrkUX837T9uvSvK2BlsEJlDMKP9vA8HSSYOnRZFqdD5AwF6kNfcLu3bqyyTid2hobUZ2zBQDAoWeC7bHgYcpwLm5jZWp1t5i8S6xRQuPKz8cHb4VVzQ6_c0XS7UPGX9vW0MWa7CxOQnM4c4ARfqpA1UpaZ7uOGY-Ec4LhozI7po1l-TeymcVavmBQFTuHysjjiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رتبه‌های برتر کنکور علوم ریاضی
🔹
۱. اشکان کریمی
🔹
۲. امیرکیان رئیسی بهان
🔹
۳. امیرحسین جعفری @Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/465990" target="_blank">📅 10:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465989">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c89758407b.mp4?token=Jsm6iIwIIhtaI0nz-lK5Y8b5a0twzQnvtGczGjmp5znq6JT3H6ShTROKkqLD4Hm3bMoQ_Taz9SxVku22oTSVvPMgrNcjlutwm8IsxQvhDFqybLI1tqVwqOpvPSZt7vpIo7mW5iK8lAuoZK2mwPMUAiRaJkktjhEjBklZSbnS9irvw9x0UXnZiTP0JPmv3QAn625WghMm1UA6UuH3VuZFZhOZKcD_CwmluZ4y-zAoPA9W9d76x1_IQ2-dhitIQ6rv0cBFm2_EzlSzYBfSh95HND7_nIdwA-cOX5W12q7KX4V8oR2MBpGYVKkOs-6QhljaK2_E6eMpCHVmr605YvL4Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c89758407b.mp4?token=Jsm6iIwIIhtaI0nz-lK5Y8b5a0twzQnvtGczGjmp5znq6JT3H6ShTROKkqLD4Hm3bMoQ_Taz9SxVku22oTSVvPMgrNcjlutwm8IsxQvhDFqybLI1tqVwqOpvPSZt7vpIo7mW5iK8lAuoZK2mwPMUAiRaJkktjhEjBklZSbnS9irvw9x0UXnZiTP0JPmv3QAn625WghMm1UA6UuH3VuZFZhOZKcD_CwmluZ4y-zAoPA9W9d76x1_IQ2-dhitIQ6rv0cBFm2_EzlSzYBfSh95HND7_nIdwA-cOX5W12q7KX4V8oR2MBpGYVKkOs-6QhljaK2_E6eMpCHVmr605YvL4Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رتبه‌های برتر کنکور علوم تجربی
🔹
۱. آرش محمدی
🔹
۲. سیدآروین حسینی
🔹
۳. علی جعفری @Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/465989" target="_blank">📅 10:46 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465988">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42af7f2d26.mp4?token=f60P6rF9NroSlgbdtV7vdPYjfLMqCwi0dcOLWXlEJZC3DJl5j4gtFfyrV41xvdUAj3wdotJwI_02KCCv47MjtohodSP86OllM68Udo9gca6eMD2brLc-La9rK04m-_-u2dHKFVsJSfUxrLDZAbSdSM14j8hrFGDxKdQg3BYUer6ZEHzapZKpD8eQFQOf4R8nRF86LRII-pk8VoYQK08hh2ZRDpFzGOIx046mYvxSMFnkrYPlLQgv5K3KbBJ5Yay-UCGRWUNKoFcnYYckRvCdRMHv7ZPEnU80cJLlw1MRzz177OPxC7qKoFpO7ef6I0AgEuiXNFLBbDZSleXN8nWxMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42af7f2d26.mp4?token=f60P6rF9NroSlgbdtV7vdPYjfLMqCwi0dcOLWXlEJZC3DJl5j4gtFfyrV41xvdUAj3wdotJwI_02KCCv47MjtohodSP86OllM68Udo9gca6eMD2brLc-La9rK04m-_-u2dHKFVsJSfUxrLDZAbSdSM14j8hrFGDxKdQg3BYUer6ZEHzapZKpD8eQFQOf4R8nRF86LRII-pk8VoYQK08hh2ZRDpFzGOIx046mYvxSMFnkrYPlLQgv5K3KbBJ5Yay-UCGRWUNKoFcnYYckRvCdRMHv7ZPEnU80cJLlw1MRzz177OPxC7qKoFpO7ef6I0AgEuiXNFLBbDZSleXN8nWxMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رتبه‌های برتر کنکور علوم انسانی
🔹
۱. پریزاد نیرومند
🔹
۲. یاس هاشمی
🔹
۳. پوریا زارعی محمودآبادی @Farsna</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/farsna/465988" target="_blank">📅 10:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465987">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d38177d2c.mp4?token=ZDlaKKVwUVe4CNaaAKvc-T7w2WhyaaWGRpncV7LPyZK3iiWUSjf9xOem3hLDmDwaNyLT2Lnl_Al7DuGjxI0c2sbztquokR4bGEzHaRn22ALo9J9gaUQLAYn2_LTfq0-Os6qFVfS_dr5jpX8r-YMHuksYR0AZDL_Jg-hSIrWxUwthCcBAbHhyJo4cwW8xYQkOrSFMEEHuyferM7JZy3Ud88ggOBqWA57l77g7Uce4qOkN05OPnqj9Ytqns1V6-FfjEupCwOuHAKre_BgtrUdf6stMkEKIe2QIMMORp93vKmajg9H-TzXKDy_ZnO22buXjXr7JSGGXagFsi4oJcEZArw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d38177d2c.mp4?token=ZDlaKKVwUVe4CNaaAKvc-T7w2WhyaaWGRpncV7LPyZK3iiWUSjf9xOem3hLDmDwaNyLT2Lnl_Al7DuGjxI0c2sbztquokR4bGEzHaRn22ALo9J9gaUQLAYn2_LTfq0-Os6qFVfS_dr5jpX8r-YMHuksYR0AZDL_Jg-hSIrWxUwthCcBAbHhyJo4cwW8xYQkOrSFMEEHuyferM7JZy3Ud88ggOBqWA57l77g7Uce4qOkN05OPnqj9Ytqns1V6-FfjEupCwOuHAKre_BgtrUdf6stMkEKIe2QIMMORp93vKmajg9H-TzXKDy_ZnO22buXjXr7JSGGXagFsi4oJcEZArw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان سنجش:  فردا نتایج اولیهٔ کنکور در تارنمای سازمان سنجش قرار می‌گیرد.  @Farsna</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/farsna/465987" target="_blank">📅 10:43 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465986">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e635afaa1d.mp4?token=Ck1dXX4uR8O20neIE1CV18209g-8dp39wSJO3DQAJXe7YjLoGkA9UC6CvQxCUYFxfVb3bUVfbEsHjrDh4p8I1zjXFFLpFA0cpLtpS2J1Eb0LYl9P2xLKarfzf9MWlP09JNlzltlJwUnx9AMkqlHY-IpjD4MA1oQ4IcAy9bWREym12DfDuwH_dsvqchtarWixAVYm5vElF2fMem0gq-1mM_fIwq6wE-RdJ0zNEWyhA3iDnNa4vy75FRp-cV58X8AtQRdfzff0_JEMLmlFLDKjrkGnpGYbTqvNiRHODzdI59wMFFcVSodmsn0yq48NkPawzYKj2iIj__qrZwvblOfwtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e635afaa1d.mp4?token=Ck1dXX4uR8O20neIE1CV18209g-8dp39wSJO3DQAJXe7YjLoGkA9UC6CvQxCUYFxfVb3bUVfbEsHjrDh4p8I1zjXFFLpFA0cpLtpS2J1Eb0LYl9P2xLKarfzf9MWlP09JNlzltlJwUnx9AMkqlHY-IpjD4MA1oQ4IcAy9bWREym12DfDuwH_dsvqchtarWixAVYm5vElF2fMem0gq-1mM_fIwq6wE-RdJ0zNEWyhA3iDnNa4vy75FRp-cV58X8AtQRdfzff0_JEMLmlFLDKjrkGnpGYbTqvNiRHODzdI59wMFFcVSodmsn0yq48NkPawzYKj2iIj__qrZwvblOfwtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیاره، معاون سازمان سنجش آموزش: تا ۱۰ روز آینده نتایج کنکور سراسری ۱۴۰۵ اعلام می‌شود.  @Farsna - Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/465986" target="_blank">📅 10:41 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465985">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a2e23b992.mp4?token=rooyDoG-D_KnWGFMKiB7Ak-9oS54eIhNKMX70VJfOzmg7HaU0fBGEwsU6nrVYjaTPSZX7fgnX21inX8pmRFcEYSZ4i1Y71stvEYx0Eev1R23UehMQM3WvlgBoOmw1MvDfzs6H1MhVGtjfyQbBF_gvFLZA-0vllVZrqGhPVZaUdI89lRjK-C9VMm3yC0N4Ru58YrJXDsqKeI9rNr_SyH5jqt-bSqwcc2B9ynU6LVEv4ftH259Q81CWStvLDxJ9KfM6MnASBtnFttRdvRsAHtXb0E1hdnwMtagzQw02YBz_U_qN6pJEmqIMFzPyE-S7ttMO9DFupXdt-c-tNQQtr5maA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a2e23b992.mp4?token=rooyDoG-D_KnWGFMKiB7Ak-9oS54eIhNKMX70VJfOzmg7HaU0fBGEwsU6nrVYjaTPSZX7fgnX21inX8pmRFcEYSZ4i1Y71stvEYx0Eev1R23UehMQM3WvlgBoOmw1MvDfzs6H1MhVGtjfyQbBF_gvFLZA-0vllVZrqGhPVZaUdI89lRjK-C9VMm3yC0N4Ru58YrJXDsqKeI9rNr_SyH5jqt-bSqwcc2B9ynU6LVEv4ftH259Q81CWStvLDxJ9KfM6MnASBtnFttRdvRsAHtXb0E1hdnwMtagzQw02YBz_U_qN6pJEmqIMFzPyE-S7ttMO9DFupXdt-c-tNQQtr5maA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازی‌های آسیایی ناگویا  یک برد دیگر در تکواندو بانوان
✅
فاطمه احمدی در نخستین مبارزه خود در وزن ۶۷+ کیلوگرم مسابقات تکواندو با نتیجه ۲ بر صفر مقابل لین یی‌چن از چین‌تایپه به پیروزی رسید و راهی مرحله بعد شد.  @Sportfars</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/farsna/465985" target="_blank">📅 10:38 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465982">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pHr-Fg74HC_o2nxTu5V4ONz6q1LUk_wo8pImwGffsSQGPNwydtZnZePXhYIYb4_OYLukteF7iiQ4LbFq6okbt8RD_rVYXjyCYSjr6hCgPKYlaiJD7r23g1usYqYkL7-CQtATjtV2KIEnXB8Iz_Pndxp63EyiEgHwcguJ0MtaBlrv6EvBITuKqyHQNIOZzwK7NVdJ8tHCxnjM1_d9jcxTj8yEA-wTMkIJm4iSU8bqBn41l_M7g_xBvGu3g0-CQz21RaQRVEAU-fR5zTF028yg0RsDqAuzM7JfbHI1PPNMd_VXxGbrLCpPt4jVd5JgdyttD02EgVpRLE3WMztTtjIzbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EVb_THql9qPsqwMLewur04y5CScgKxGFJLCw6he6kHp7ox1fNhtWfwjYsePH_JWSljVZccNaN9jHZK1gx4QcjMh8H6qzbRYO-MCwMn_dPNDeInCGZfgr5DIuMw-QkdZGhgUZ2zbePCmI2TWX28ELKyistKGXe51EEKb7JIqQ1i2cOj1mhOg1mZ5rx7lOttW08Hs-Wv5cUnVGfd_1mQtXQdq2CkyCJZTx4WHz92OydhDSOcUQKKwXnvmGr_n7c4Ou6BC0ePmDWy1Psn3R1pha01sLUR7HiA03BiZCLNrvpSnqaegL0BKj4s7k-DXa4OF1Nfq_WJfRsQQyDvT567zMNA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a86287d76d.mp4?token=tOKg63leROKb317dVyRmQJGZpBKc8XOlKbbqEyg6wGlSv6phM8YtfGOIrnpHIm8bplEQNG_ilW25lOS7c6epE1WhxRqrBGKq1r3zaAJSSg9lHvPPXUUkBjxEm-pxc8uVok0o-L5gXKPSdgkkOIWNEpR8e2yYxtkVbVk32Qb01LHh9cF6qzPbKdKTdw0QMjSXU2mciXGTzgYDiCBqjoTb7O3mAHP-zOOmcx0KrBCJEVglqhlgraZS-WsxL-fPKaN7cyuP97v9BZt0olor6VGo3YTbOJK-IDgVUv3Ot5paeULVK23V_9A3Dfufa6Wjfode9AOAc41nBjSSrgNow-aC-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a86287d76d.mp4?token=tOKg63leROKb317dVyRmQJGZpBKc8XOlKbbqEyg6wGlSv6phM8YtfGOIrnpHIm8bplEQNG_ilW25lOS7c6epE1WhxRqrBGKq1r3zaAJSSg9lHvPPXUUkBjxEm-pxc8uVok0o-L5gXKPSdgkkOIWNEpR8e2yYxtkVbVk32Qb01LHh9cF6qzPbKdKTdw0QMjSXU2mciXGTzgYDiCBqjoTb7O3mAHP-zOOmcx0KrBCJEVglqhlgraZS-WsxL-fPKaN7cyuP97v9BZt0olor6VGo3YTbOJK-IDgVUv3Ot5paeULVK23V_9A3Dfufa6Wjfode9AOAc41nBjSSrgNow-aC-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
استوری‌های راحله امینیان از وضعیت مدارس لبنان و تنها خواسته مردم لبنان؛ «فقط سلام ما را به مردم ایران برسانید»
@Farsna</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/farsna/465982" target="_blank">📅 10:31 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465981">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ViQcU6vgDjrVi0-9HKx9AAAsFdXpUgyiUdTu0-OpkrBChGtBFQuprl3_25lhNL7_FPUnvgb2NipSMZi34YzIfiBtkahAg_Y4Cv_DxQzUIcyKY57MGTUQLPa4Rru3L64nxKNoBy0Ct35YtjZfgKmpMnJmm5VLKQ0rU3MQVqbcLFdWoMiiqahVGGYJ8-2blZGKko3-kLwA2JoX9NRlOjpptc6srPTA8Hw_PZ0ZDxE9TTz9Rr7TStvb2X21XHgNz_R6lfNPy_ONpY_E3p0WVWp0vJla5SVa7Xkz5_a_H9on3NrSM7hBjQ7M6w-a8D0oNEvkH8tZ9nAnOJuIGjsTAq-_Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله به یک نفتکش در مسیر غیرقانونی تنگهٔ هرمز
🔹
سازمان عملیات تجارت دریایی انگلیس اعلام کرد که بامداد امروز سمت چپ یک نفتکش در فاصلهٔ ۴ مایلی شرق عمان هدف قرار گرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/farsna/465981" target="_blank">📅 10:29 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465980">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebf8d6aa62.mov?token=O3qLhSzuxscTldFPD32g1v1qdU5x_oq1MyX5Y6bFZUFAuHF_XMerjpThkRSkSLp_E_trh9XkbEHPe-RObD-0WVOv4NuLaZZNZPkrRm200qB4RUAl5OGlhTJxjDmMUelj77v2_FnRAx8mm7ayvJnNpyyZ2Uua5qk4uAyAHehYp6hsW-MNZTU3ULmONAKvcqF-txXmHmBNc4vXG1vQeKBbmWCTOB7ToBactT1z1D-rdBq4TgCjQ3V9Yh2KdFVbWRPBy-J1dK-AtPo9oOJKy2PYs7oCuVmeAbGoNi_If9yzO-o8Temi_u4fwddd9i5p55g-rDVQt209yj8slF-kFD9hYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebf8d6aa62.mov?token=O3qLhSzuxscTldFPD32g1v1qdU5x_oq1MyX5Y6bFZUFAuHF_XMerjpThkRSkSLp_E_trh9XkbEHPe-RObD-0WVOv4NuLaZZNZPkrRm200qB4RUAl5OGlhTJxjDmMUelj77v2_FnRAx8mm7ayvJnNpyyZ2Uua5qk4uAyAHehYp6hsW-MNZTU3ULmONAKvcqF-txXmHmBNc4vXG1vQeKBbmWCTOB7ToBactT1z1D-rdBq4TgCjQ3V9Yh2KdFVbWRPBy-J1dK-AtPo9oOJKy2PYs7oCuVmeAbGoNi_If9yzO-o8Temi_u4fwddd9i5p55g-rDVQt209yj8slF-kFD9hYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رده‌بندی تمام ایرانی بدون سرمربی!
🔹
با توجه به اینکه دیدار رده‌بندی پدل بازی‌های آسیایی بین دو تیم ایران در حال برگزاری است، سرمربی تیم ملی در جایگاه ویژه، تماشاگر این مسابقه شد و هدایت هیچ‌کدام از تیم‌ها را بر عهده نگرفت. @Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/465980" target="_blank">📅 10:04 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465979">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86b3fc0d84.mp4?token=G7Z_li4iVIMQoRnlqKpQyj6AgA5idh50fAY5kGGRN6yLyQE0qdKrZ9f6bgR25Yb6nl5fRnVGByYi9cKzsyCrIXQN56iX75-ZCidq5qxyocbQJtD0On0IfJeMkrt7v30rlssLm0BeWLomF_B9aAAkAjV15JGWGSE92ftlGCuGtca3nTiXUg9kBbCzbolya0YBHMVTq-sG0aFYbk3bahG5LAjZaizck34pt6Dquvf677kBu3q79C5NaXBg74B36834CN_S2gMAmYIta0Ip070405uc-oQa3w-xyseeZ7EQqDjkrPGx0Zp2L5pu6eyDkAP0sqKM3i-0NxedgV7Zsnx_Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86b3fc0d84.mp4?token=G7Z_li4iVIMQoRnlqKpQyj6AgA5idh50fAY5kGGRN6yLyQE0qdKrZ9f6bgR25Yb6nl5fRnVGByYi9cKzsyCrIXQN56iX75-ZCidq5qxyocbQJtD0On0IfJeMkrt7v30rlssLm0BeWLomF_B9aAAkAjV15JGWGSE92ftlGCuGtca3nTiXUg9kBbCzbolya0YBHMVTq-sG0aFYbk3bahG5LAjZaizck34pt6Dquvf677kBu3q79C5NaXBg74B36834CN_S2gMAmYIta0Ip070405uc-oQa3w-xyseeZ7EQqDjkrPGx0Zp2L5pu6eyDkAP0sqKM3i-0NxedgV7Zsnx_Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام پناهیان در لبنان: مجاهدان لبنانی پس از حمله اسرائیل به ایران و شهادت رهبر ما وارد جنگ شدند و با چند هزار شهید، نقش بازدارنده‌ای در برابر دشمن ایفا کردند
🔸
برای احترام به این فداکاری‌ها کافی است فقط ایرانی باشید.
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/465979" target="_blank">📅 10:02 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465978">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b040582fd6.mp4?token=dihD_ngtigztTPcM86-7Lwz3L6aVxiTsfDXbaZkJezGUOlMhsncjPmAPj3gQ0utNUtDPwy5V7YFQy9sYIKi5OcFRfzB-H9S6XzRjjAb6S6uKdbtw-Fmw2hFwjkXsh9AMg5zTb2FpMBMJuwA2xtMJeDkSPid4TpB8EHGYQDYuxpV2ijc1YroZHrvehaTBbcAs4IE7wZnPOtddc5kA_JqcAyVB-10a5MkRfq2FL8fPyM4XBVmdB7CgfZ2pUSD5nAfxXuOd0DoDvaQM5wGmEP3JG1d5THMDRk-Jydi1fSn-eBWP2LAl9qfz9LA48ztA-AtglOfRKp6BL2jyOcs4AlHULg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b040582fd6.mp4?token=dihD_ngtigztTPcM86-7Lwz3L6aVxiTsfDXbaZkJezGUOlMhsncjPmAPj3gQ0utNUtDPwy5V7YFQy9sYIKi5OcFRfzB-H9S6XzRjjAb6S6uKdbtw-Fmw2hFwjkXsh9AMg5zTb2FpMBMJuwA2xtMJeDkSPid4TpB8EHGYQDYuxpV2ijc1YroZHrvehaTBbcAs4IE7wZnPOtddc5kA_JqcAyVB-10a5MkRfq2FL8fPyM4XBVmdB7CgfZ2pUSD5nAfxXuOd0DoDvaQM5wGmEP3JG1d5THMDRk-Jydi1fSn-eBWP2LAl9qfz9LA48ztA-AtglOfRKp6BL2jyOcs4AlHULg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
منظور، رئیس سابق سازمان برنامه‌وبودجه: ۱۰ میلیون خودروی فرسوده، بنزین را می‌بلعند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/465978" target="_blank">📅 09:52 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465977">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/769e47fdeb.mp4?token=SLlyMFk7FDOdScZvYNIzmd6jTsXbAof-vuOZTpuGuVxYFFwNTzdjFXh3aY2i6nHkEu1MGhJQWzOmGHrSZAwyQ_Tu4-xQqiB_1-e5z6PwspTkath8QN2PGNbC1vrNVxYCvYJkKUWqjbz7e1XfEC0zQuAloW3dwS_jYOHcFj0HhVtt9KSqOpLJf0tnriOQZisyqWiTEhLCq5NlafCwjTsiLLzLFZg--0RZDPll21bKIac751PnNcOmyvCSu8efZo8ThR0JJOm4s-P9pWcIF9BCi8o8w4CmGEYqzOc3PIN3XrvtLuAU27iafb77TD4Y37FrAqU2iaRgwhUIhuogXAinJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/769e47fdeb.mp4?token=SLlyMFk7FDOdScZvYNIzmd6jTsXbAof-vuOZTpuGuVxYFFwNTzdjFXh3aY2i6nHkEu1MGhJQWzOmGHrSZAwyQ_Tu4-xQqiB_1-e5z6PwspTkath8QN2PGNbC1vrNVxYCvYJkKUWqjbz7e1XfEC0zQuAloW3dwS_jYOHcFj0HhVtt9KSqOpLJf0tnriOQZisyqWiTEhLCq5NlafCwjTsiLLzLFZg--0RZDPll21bKIac751PnNcOmyvCSu8efZo8ThR0JJOm4s-P9pWcIF9BCi8o8w4CmGEYqzOc3PIN3XrvtLuAU27iafb77TD4Y37FrAqU2iaRgwhUIhuogXAinJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام پناهیان در لبنان: مقابل رزمندگان، مجروحان و خانواده‌های شهدای لبنان جز شرمندگی احساس دیگری نداشتم؛ این مجاهدان دارند جهاد می‌کنند
🔹
خانواده‌هایی را دیدیم که چند شهید داده‌اند، خانه‌شان را از دست داده‌اند و در اتاق‌های کوچک زندگی می‌کنند.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/465977" target="_blank">📅 09:45 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465976">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">یکی از متهمان پروندۀ دوومیدانی در کره‌جنوبی به ایران برمی‌گردد
🔹
یکی از اعضای تیم ملی دوومیدانی ایران که در جریان رقابت‌های قهرمانی آسیا در کره جنوبی با اتهام آزار جنسی مواجه شده بود، پس از پایان مراحل اولیه تحقیقاتی و رفع ممنوع‌الخروجی، به‌زودی به ایران بازمی‌گردد.…</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/465976" target="_blank">📅 09:43 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465973">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a14e06e9c.mp4?token=RnCZIGiYyOkKviBuVN1j7ttqVIoxuaYbb6hzphjPEefi3VOJ9Bc6IgnVgL5Jd6sNOB1sX0tHypq1gcl7bdIgBCoGO19ZyIayAP7b9HVh_OdgcIAQWNbcLEhFFEJRhHmA5iQ-hjCMQn_oQSF7FMN6TYr5KE4ayQWLdREUBzuF2qzSon81MNQQg2yN0dfDQzK0aQ2qimzv8gCUDNks5-TfMfPfWB689XAxx1Pxu-DyViFItRoMcNdJq7y8FcGWA5zup5iiER1lW0uuF6ZyM110plmb__BJRCDZuJV6jNE8Frx8cGZ8S0dh6L01BZAaHL7YaSTG-VVzEdPL3Mun0XGs9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a14e06e9c.mp4?token=RnCZIGiYyOkKviBuVN1j7ttqVIoxuaYbb6hzphjPEefi3VOJ9Bc6IgnVgL5Jd6sNOB1sX0tHypq1gcl7bdIgBCoGO19ZyIayAP7b9HVh_OdgcIAQWNbcLEhFFEJRhHmA5iQ-hjCMQn_oQSF7FMN6TYr5KE4ayQWLdREUBzuF2qzSon81MNQQg2yN0dfDQzK0aQ2qimzv8gCUDNks5-TfMfPfWB689XAxx1Pxu-DyViFItRoMcNdJq7y8FcGWA5zup5iiER1lW0uuF6ZyM110plmb__BJRCDZuJV6jNE8Frx8cGZ8S0dh6L01BZAaHL7YaSTG-VVzEdPL3Mun0XGs9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
توقف پروازها در فرودگاه ریاض به‌دلیل انفجار
🔹
همزمان با گزارش‌ها از حملات موشکی و انفجار در عربستان، فعالیت پروازی فرودگاه بین‌المللی ملک خالد ریاض با اختلال مواجه شده و پروازها با تأخیر یا لغو مواجه شده‌اند.
🔹
برخی منابع عربی هم از حملات موشکی یمن به مخازن آرامکو در ریاض خبر می‌دهند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/465973" target="_blank">📅 09:27 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465972">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/simzBoesBqiMimDGGA0PWPCf8HEEcqrYpysoJJPttkSkYKIPa4f_8Ufajfi7taLUHug5baqe_f4KmpeGsCf4eKT3_7cuiKniy4KOYz-A8i8RpEGMN0jQik-Y2hKGXoO9Sbo4a6w0gG96HMYaMcCcjsyCWi7JXbu-As3WcjGwhHTKKuX4Vy8yxUgxSfvOjAnd8xvpOjv1Rl-riBVbvf6Lx51Oo4qXh6VZBuv6mlwSTKA1d4rI5u-aLAohmTlvgpb-Zvcb5soJs-oA-NTpWiT-9Ypgp3F5owHnITO9wmTFEvKDpJHeCMw4Y0BkdmwOn58AFNvwKc3zWt2oGgHmgu7_lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدیدترین نقشهٔ نفتکش‌های تنبیه‌شده توسط ایران در تنگهٔ هرمز
🔹
جدیدترین نقشهٔ مؤسسهٔ واشنگتن که نفتکش‌های هدف‌قرارگرفته توسط ایران در یک‌ماه گذشته را نشان می‌دهد، حداقل اصابت به ۲۰ نفتکش در مسیر غیرقانونی تنگهٔ هرمز را ثبت کرده است.
🔸
این در حالی است که ترامپ همچنان مدام مدعی «نابودکردن نیروی دریایی ایران» می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/465972" target="_blank">📅 09:23 · 11 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
