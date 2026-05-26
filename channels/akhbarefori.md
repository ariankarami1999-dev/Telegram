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
<img src="https://cdn4.telesco.pe/file/LOmm47VkYr54Fv5EbfcjMyo2gps5sTghdTO5RHR9kdUOAneDgNFQpNfxfPAnX3Jdv3saBMTONFKAI46jOE42pzHAYaNkpe6MxqnJRsedTyz8wvdOcRH6vxigx9yJLBvHJB-Ix1zDo8bV196_dO3-Cok7WAeP8CJEmS6CCKEJ0UBGNjZGs2Waih6pLRmcQFfssaRWSvQ3-AGXSs1_nCxwZ-25W45zh92qnt28G9rSa66bN3i4RpjeOZmKiCu97Va1kska-3nCUvrt06yeMWHdyC1amusXvHNZp2WwQO8K_ztxYDMR3sTPTG7lt8UVXD4s8c--A02mvp4Q1IaLRIMKZg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.05M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-05 17:41:59</div>
<hr>

<div class="tg-post" id="msg-654177">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kwid4yKD9n3tqce-yWn5k9e1WQS6858jBuARzP0KdBxV73ksmZo8ztOHySQzysLEiih6_63UUS9gD4chBKRFUUpw8UCwAAzT9NlIh8HLzfZ4Fzbts2ShDXJzpWBfT9KW1qChMmHKfxfgJtpIubZY_wqj4UgscN6asq_Qcn7GjKI6SV8-Eg0t2gw1OFDcjzixoF7xMSWb0I3EtX0FcQ65cvZQVCutU-6PYJI6UIlsLG91TXHBw7dDLqRSZcy0kBNm4xQEXkLCIHBj9UJQzjyyef0991EGhOeGvDRnMYk2YLk-dZZxe4QApHPtNEbe5M_EbywJljFHPgDVj0yY7h5jnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۱۱ شهید در حمله اسرائیل به مشغره لبنان؛ بمباران حومه سد فرعون
🔹
همزمان با تداوم حملات هوایی رژیم صهیونیستی به جنوب لبنان، وزارت بهداشت لبنان از شهادت و زخمی شدن ۲۶ غیرنظامی در حمله ددمنشانه اسرائیل به مشغره خبر داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/akhbarefori/654177" target="_blank">📅 17:36 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654176">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
معاون سازمان حفاظت محیط زیست: حدود ۸۰ درصد بحران‌های آب و محیط زیست کشور حاصل مداخلات انسانی و مدیریت نادرست منابع آب است
🔹
در حوزه آبریز تالاب جازموریان حدود ۲۲ هزار حلقه چاه وجود دارد که نزدیک به ۱۱ هزار حلقه آن غیرمجاز است و برداشت‌های بی‌رویه فشار زیادی بر منابع آبی منطقه وارد کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/akhbarefori/654176" target="_blank">📅 17:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654175">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e989bfbaef.mp4?token=HJ9JIbfxSNgaDy5zbeKxBmnLe6rqpntMVKLaph450FWOpfevIQPxz9EHI2j9p6gL7LBFNY8vvqD6mtlH40rQiWSs070SYJIJPQvLj3__hsPqm6Su1gvPtIW1ONx3ZRspmk9Xc8B9ttZ3LYZEUQNJa9yR1oP92ucNYHNld2j53hAq1j3RTSPt18mIIfOEiAFwNGQHOwm8IwML0BmGyVnWNRd8mnvBiNfyYHixlpIPIuEKCw3TyZsDyGj-Czm9H8lKzMsOVtycGjKYMlJCLZYeyJ68ErhIzOJxUJtvADgNxgaAxtL-WO8ZgSBs2FdHgMH7VnYYQA76bPFwCtoGuB8OcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e989bfbaef.mp4?token=HJ9JIbfxSNgaDy5zbeKxBmnLe6rqpntMVKLaph450FWOpfevIQPxz9EHI2j9p6gL7LBFNY8vvqD6mtlH40rQiWSs070SYJIJPQvLj3__hsPqm6Su1gvPtIW1ONx3ZRspmk9Xc8B9ttZ3LYZEUQNJa9yR1oP92ucNYHNld2j53hAq1j3RTSPt18mIIfOEiAFwNGQHOwm8IwML0BmGyVnWNRd8mnvBiNfyYHixlpIPIuEKCw3TyZsDyGj-Czm9H8lKzMsOVtycGjKYMlJCLZYeyJ68ErhIzOJxUJtvADgNxgaAxtL-WO8ZgSBs2FdHgMH7VnYYQA76bPFwCtoGuB8OcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حملهٔ صهیونیست‌ها به نزدیکی سد قرعون در شرق لبنان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/akhbarefori/654175" target="_blank">📅 17:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654174">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
مالکی: در قطر توافق شد که نیمی از پول‌های بلوکه شده ایران پرداخت شود
فداحسین مالکی، عضو کمیسیون امنیت ملی مجلس در
#گفتگو
با خبرفوری:
🔹
سفر آقای قالیباف به قطر در راستای موضوعات مذاکره، مسایل دوجانبه و موضوعات بین‌المللی است و آخرین تحولات بین‌المللی آنجا بررسی خواهد شد.
🔹
از آنجا که قطر مسئولیتی درباره پرداخت بدهی‌های ایران به عهده گرفته است، یکی از موضوعات سفر آقای عراقچی و قالیباف، موضوع بدهی جمهوری اسلامی ایران است.
🔹
طبق یکی از بندهای توافق‌نامه، قرار شده است که نیمی از پول‌های بلوکه شده که در اختیار قطر است به جمهوری اسلامی ایران داده شود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/akhbarefori/654174" target="_blank">📅 16:44 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654173">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
ادعای وال استریت ژورنال:
🔹
مقامات ایرانی و میانجی‌گران عرب گفتند:
🔹
«محمدباقر قالیباف» برای دومین روز متوالی در قطر مانده است تا درباره توافق پایان جنگ گفتگو کند.
🔹
به گفته این مقامات، قالیباف روز دوشنبه برای رفع موانع باقیمانده در طرح صلح، از جمله درخواست ایران برای آزادسازی دارایی‌های بلوکه‌شده خود و جزئیات مربوط به بازگشایی تنگه هرمز، وارد قطر شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/akhbarefori/654173" target="_blank">📅 16:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654172">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
سازمان حمل‌ونقل دریایی انگلیس اعلام کرد گزارشی از انفجار در یک نفتکش در ۶۰ مایلی ساحل مسقط دریافت کرده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/654172" target="_blank">📅 16:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654171">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vgp01D7Uv-nsoHATVreidEOONqx9nRylsVILZBGWJE98hqzC1F0BVo-Cf2A6t5Og7Iz72M0SPS-E7hLJ-HEnoMU2rsIxjsYm3ksTw7YNHmaRjJ5YrjWRLpYUUAdk2i9WAwmJ6XYejQzj2KPv2nFLb-_FoE32U6BDMZkyeigrjyH-SpYkSwjcg6gcok3AqwhX98n1QwsLcazxSpIS10x86yJ7ukZ57b3YDxbZaNgk_AVZnSRvaAxV30s8ZEGzP3tbCyPN29FnfpVZZJpnH1MJZrLgMwbIETsgvo5uE-U23jPkRH6RLAlGF-ve8Dz6BkCjzZSqs3bBMKhqsHCV1pj_Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازگشایی اینترنت به دیتاسنترها رسید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/akhbarefori/654171" target="_blank">📅 16:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654170">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72a0b54080.mp4?token=nPReiJPn5TLpS5aoMzh-6IOAJxkgljU4A6n9QxiteFK4JtLIGnMWeEt3y29nzCtBFYTnWCQClU6GZXuJscZfVk_ZCDwONUAaDhr1nnGT6Hr6pkwmwIdDc7hFLgtAL594--EAzquPNZ9Df5g7kEQ2FBwPbC3VtiImlRlR7aeI06UCRKzXaxifAnEVSK_ZpfdqXzOp1TtvK9uXAiALdVXvOkzWBc4Fia_Zsp6-lC2TD4ZDDtCmvFoJvzt7bJkTNB4559cjEm7Ojzsxtf4VOgUnCBWB7Ib6f5aN4KnNXZ64DjkLaxUYe1ziF5G-0W2uOxwu13_xfAsl5048Y1BA-CLFQyK0t3oJy8WOV9uc2WC-t4zN-Q0bXKn8s_q4HRSSsLu3kt1gBNRtY0HxejzJdc6fU7ssuQ9IB5u3aukWShAp58Ncv16EQBrzFm-9oZ_uWqgQK8HqWRWDnisTcpNFMTTuZEBeAAlWmRPN7gxnucDrcI3pJrTsRGB2bu7KNPnMNiupb_ZE62gWNuoe2g_9Jtqyf6HXPZu6u0BQNR8UTCpyo9oWRD5OzLhluUqh40csH2WKWal31bsYVihrAmMhOHnjF2BEAfI7X1YGL94TOy4bK6v8mBHhMkEIqOh4BNfAcksamEDbWcOpSPS5E19kMCObUoUcowmx5VOOpkPLb8tj0Ck" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72a0b54080.mp4?token=nPReiJPn5TLpS5aoMzh-6IOAJxkgljU4A6n9QxiteFK4JtLIGnMWeEt3y29nzCtBFYTnWCQClU6GZXuJscZfVk_ZCDwONUAaDhr1nnGT6Hr6pkwmwIdDc7hFLgtAL594--EAzquPNZ9Df5g7kEQ2FBwPbC3VtiImlRlR7aeI06UCRKzXaxifAnEVSK_ZpfdqXzOp1TtvK9uXAiALdVXvOkzWBc4Fia_Zsp6-lC2TD4ZDDtCmvFoJvzt7bJkTNB4559cjEm7Ojzsxtf4VOgUnCBWB7Ib6f5aN4KnNXZ64DjkLaxUYe1ziF5G-0W2uOxwu13_xfAsl5048Y1BA-CLFQyK0t3oJy8WOV9uc2WC-t4zN-Q0bXKn8s_q4HRSSsLu3kt1gBNRtY0HxejzJdc6fU7ssuQ9IB5u3aukWShAp58Ncv16EQBrzFm-9oZ_uWqgQK8HqWRWDnisTcpNFMTTuZEBeAAlWmRPN7gxnucDrcI3pJrTsRGB2bu7KNPnMNiupb_ZE62gWNuoe2g_9Jtqyf6HXPZu6u0BQNR8UTCpyo9oWRD5OzLhluUqh40csH2WKWal31bsYVihrAmMhOHnjF2BEAfI7X1YGL94TOy4bK6v8mBHhMkEIqOh4BNfAcksamEDbWcOpSPS5E19kMCObUoUcowmx5VOOpkPLb8tj0Ck" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
«بیش از دو سال‌ونیم است که یک نسل‌کشی زنده را تماشا می‌کنیم»
🔹
روایت هیثم عرفات، فعال آمریکایی-فلسطینی از تجاوز، شکنجه و تحقیر اعضای کاروان جهانی «صمود» توسط ارتش رژیم صهیونسیتی.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/akhbarefori/654170" target="_blank">📅 16:04 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654169">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
اینترنت بین‌الملل در دسترس قرار گرفت|خط ثابت فعلا
🔹
برخی کاربران خبر دادند که اینترنت بین‌الملل در سرویس خانگی و ثابت مخابرات باز شده است؛
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/akhbarefori/654169" target="_blank">📅 16:04 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654168">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
رایزنی امنیتی نتانیاهو و کاتس درباره ایران و لبنان
🔹
«بنیامین نتانیاهو» نخست‌ وزیر رژیم صهیونیستی و «یسرائیل کاتس» وزیر جنگ این رژیم، هم ‌اکنون در حال برگزاری رایزنی امنیتی در رابطه با تحولات جبهه لبنان و پرونده ایران هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/akhbarefori/654168" target="_blank">📅 15:55 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654167">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MSvZk6HB5QtgetoYW5ci9DHuS9j3A7DGQljcQmNEJv_CJ5F5pqf0Kz04gXFCxN1Q1Ka3OFhaBswisxyH6_INIKKHOToECO9Xdrs_5y8wgMt0qaeGj2tdh2AuGCyofXijmjM4Px_zQOZgA_1FCNMR6ic01n8I3EPirWQvBHK484tIGF5EYpmzSc3Un617qBT6LGq-4Iy8Ai3vM_n6ZupJVyrNbLeATpqJt5cUZ25AoYmL1reyFIw58v_84eQWT9cwj8xknoqPcfN2kDayUaP7inDCLPIPx2rblNPsmNg1hTLMhv9ZAWUrL7rjHjISGgjH3jhSHrlNLcpxTe3o8uWY5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قانونگذار ارشد روس: زلنسکی در پناهگاه است
🔹
همزمان با تشدید تنش‌ها بین روسیه و اوکراین بر سر حمله مرگبار اخیر به دانشگاه روسی، رئیس کمیته دفاعی مجلس دومای دولتی آندری کارتاپولوف می‌گوید که ولودیمیر زلنسکی در پناهگاه مخفی شده است.
🔹
کارتاپولوف اعلام کرد که حمله به دفتر ریاست جمهوری ولودیمیر زلنسکی و شورای ملی (پارلمان اوکراین)، بی‌معنی است چرا که هیچ‌کدام از آنها، مرکز تصمیم‌گیری واقعی نیستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/akhbarefori/654167" target="_blank">📅 15:54 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654166">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6045f895b4.mp4?token=Zc_OvLBLH4ziKyYkwj4XGCrmxGGeug76rhMDmaIU8BHQ0P67I-I_bsbpTa9WsUbOuEFpTvE8mvwCo07XDe9KvcEffOrFiSYrnC70FLkFg1j7VdGzYzKyApY8ISf7FrJfS9o4Jk-aoQ9GTtYgw5smFSiPVYJUfq-KltUc9LLLlujGJICLccHXDEgCqqjn-ZdOs96QNT41T7R6I7WiKDTxIbLF_MMdiHCaT2WywZjOyrmroITNR4p2gQTG5Osb-QG16ED5hSSc0VkWBIjICwINvqmbFzP0mglUTxnroyRsqB3OT3CCBsLt5DSSP2Y0xAP1P4yK3b0Z-gPoHaZAEilD7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6045f895b4.mp4?token=Zc_OvLBLH4ziKyYkwj4XGCrmxGGeug76rhMDmaIU8BHQ0P67I-I_bsbpTa9WsUbOuEFpTvE8mvwCo07XDe9KvcEffOrFiSYrnC70FLkFg1j7VdGzYzKyApY8ISf7FrJfS9o4Jk-aoQ9GTtYgw5smFSiPVYJUfq-KltUc9LLLlujGJICLccHXDEgCqqjn-ZdOs96QNT41T7R6I7WiKDTxIbLF_MMdiHCaT2WywZjOyrmroITNR4p2gQTG5Osb-QG16ED5hSSc0VkWBIjICwINvqmbFzP0mglUTxnroyRsqB3OT3CCBsLt5DSSP2Y0xAP1P4yK3b0Z-gPoHaZAEilD7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توافق با ایران، حفظ وضعیت فعلی و ادامه محاصره و حملات نظامی سه گزینه دشوار برای ترامپ
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/akhbarefori/654166" target="_blank">📅 15:45 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654165">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XzdqYVgzB7M8VdoPNgU7VGUAj5Mdq95OAK3RzjO1VcuZmnFVehBDT9wHdEAGkkS1HbCgvz1dxeNM-SffEEhY_shQ92kP8Igzl7225x0D0lM0hBKbMpb_iz6eM62V_Lv0-_TeNMQpBtX0N4WFjYFu3c3_BelrO58PAAvbM4-jUV8-179PbxG6gj9EYLkVKxzjZi4YQZaEDHEasT_bs2PgjzpDX6bfc4iqEIEAgXXudHLujHE_0dFyJkqij23w5yfnSpw8R8bIFCP3Ri-u9Lxxezo8us3MahE63dwi1nQW97bR7VyyvlDqIDUebnobPdF7xzwm04NnO2csx_mV7qbdEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برق اروپا در گروی محموله‌های گاز قطر در پشت تنگهٔ هرمز
🔹
شرکت‌های اروپایی برای قطع وابستگی به روسیه، از قطر گاز طبیعی مایع (ال‌ان‌جی) می‌خریدند که با حملهٔ آمریکا و اسرائیل به ایران، صادرات قطر، یکی از بزرگ‌ترین تولیدکنندگان ال‌ان‌جی جهان متوقف شده ‌است.
🔹
حالا قطر ماه‌به‌ماه این شرایط اضطراری را که از ۱۳ اسفند ۱۴۰۴ با حملات موشکی ایران به تاسیسات راس‌لفان اعلام کرد، تمدید می‌کند که به‌معنای عدم ارسال محموله‌های گاز به شرکت‌های اروپایی نیازمند سوخت برای تولید برق است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/akhbarefori/654165" target="_blank">📅 15:32 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654164">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FwclS8shqd9-rKbzQAQ1kneVLFVLxcdYhFxkqeArnLmdPUTSnXiuOp1V2i2rj1F2LrmmjbKVmQZXY_84hH9UKkVRR851qX8p5sjr_kpmmeAbUa1ZOtL26ETe4hufKJXkpDR8UKAtGhfFPT5V3z96IqTW_uomSJ1zNPBnH7XF54t17hS9N46C95_j2gtJi_-JPEtmhWUs2CeiacCMCXgD5BJBTl1SdYdppW8fIwqM51Il0duXIv-Dt9Uuax7Ipv1RdH-FEkLVipmIhtws9PgoZ8bgB65FyWIOgVzLd01z33MnOq1c82w5oJenMCzjziuhpjJchVo8pZKtqFAqVcpmng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
امیر آراسته: از اقیانوس هند تا مدیترانه را برای دشمن جهنم می‌کنیم
🔹
جانشین رئیس گروه مشاورین نظامی فرمانده معظم کل قوا، با اشاره به گستره جنگ فرامنطقه‌ای از مدار ۱۰ درجه در اقیانوس هند تا دریای مدیترانه، گفت: چه جنگ شود و چه نشود؛ آمریکا دیگر در منطقه پایگاه نظامی نخواهد داشت.
🔹
آنچه که تاکنون انجام دادیم، همچون رزمایش بوده است؛ زیرا ما سربازان، جنگ را زمانی جنگ واقعی می‌دانیم که سینه به سینه دشمن وارد نبرد شویم.
🔹
در دفاع مقدس ما تجربیاتی بدست آوردیم که در جنگ ۱۲ روزه و جنگ رمضان به کار گرفته شد و برای مثال ساخت موشک و توپ جنگی بنا به شرایط از همان تجربیات دفاع مقدس بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/akhbarefori/654164" target="_blank">📅 15:32 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654163">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
فوری
بازگشایی اینترنت بین‌الملل ثابت شروع شد
🔹
در پی دستور رئیس جمهور به وزیر ارتباطات برای بازگشایی اینترنت بین الملل: تا ساعت ۱۵ امروز سه شنبه (۵ خردادماه) حاکی از ادامه روند بازگشایی است و توقفی در اجرای حکم رئیس جمهور صورت نگرفته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/akhbarefori/654163" target="_blank">📅 15:29 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654162">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-poll">
<h4>📊 با توجه به تورم فعلی، مبلغ ۳۰۰ تا ۳۵۰ میلیون تومان وام ازدواج تا چه حد می‌تواند در شروع یک زندگی مشترک «گره‌گشا» باشد؟</h4>
<ul>
<li>✓ هیچ فایده‌ای ندارد</li>
<li>✓ در برابر تورم فعلی رقم پایینی است و تأثیر چندانی ندارد</li>
<li>✓ نسبتا خوب است، اما فقط بخشی از نیازهای اولیه را تأمین می‌کند</li>
<li>✓ بسیار موثر است و کمک هزینه مناسبی محسوب می‌شود</li>
</ul>
</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/akhbarefori/654162" target="_blank">📅 15:17 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654160">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
بانک مرکزی: وام ازدواج ۳ ماهه پرداخت می‌شود
🔹
بیش از ۸۶ درصد متقاضیان وام ازدواج موفق به دریافت این تسهیلات شده‌اند
🔹
صرفاً ۱۴ درصد از این افراد در انتظار اخذ این وام هستند که با میانگین مدت سه ماه به متقاضیان پرداخت می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/akhbarefori/654160" target="_blank">📅 15:12 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654159">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SOVbZgftAJTnO2XBFuDYjqZss80hkA01y-hT1Vf7HPwu-DeLCGfULv3ykBKe20NrEpQgk0HjHiIpFRkahhU_7ZSq07aBDUaS-8rbWs2OZ6e4cNgPm3lzykeS0h2r8uBTko_XUTQdVsRJg6v2EdDeFziLJPXF3Aw9qgM0FnobwjD3J2ddeOiVK08sBHlkjtzxoeaAD9a2-ZzBNhlN4w9SX37uK1sj6x4SKEaNgVlqKPthm8TOgpzotfC30Hh3UnR7Pglz_anJY77tcWFb7P_Y2xEGMoXM0wSZ55VZ6GBg6UaKYenvghFExBJkWOX2hgci5GvjrdwRzEqf6PXywtC6vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزارت خارجه: نقض آتش‌بس توسط آمریکا بی‌پاسخ نمی‌ماند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/akhbarefori/654159" target="_blank">📅 15:05 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654154">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0efaaad45.mp4?token=l3oGA7QSa0JmQPzr3lR2VGFf0Ptx15_fKztsSsYJt4iTfbZuzp8WPomw-5cBPptT14FQ0-KgpE2WPKI9ExeRY8mbAxYCeeOrDJf2WWFA0H9n9z1kvSoRSYDfPBOR4W-kDNHTUlg2FsseucD_L4BcMx0UWo8h3H9UE4nXjhHS4q94J3a0Xy33gnDbGJ9HnZdXq2USfvsb4VqCoiIAE5RU_efwNIBG-uTjja4A0wDO3bMoqlPm1fSUEtwXrq8fzf9z93coKwKLMJiNZKMFssgsyMt_pyMNue--fcrQbyNoDMddULLA0LbbDwYZCbYLmYNsJb1mYVD2ympc8fwe7m8Ywg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0efaaad45.mp4?token=l3oGA7QSa0JmQPzr3lR2VGFf0Ptx15_fKztsSsYJt4iTfbZuzp8WPomw-5cBPptT14FQ0-KgpE2WPKI9ExeRY8mbAxYCeeOrDJf2WWFA0H9n9z1kvSoRSYDfPBOR4W-kDNHTUlg2FsseucD_L4BcMx0UWo8h3H9UE4nXjhHS4q94J3a0Xy33gnDbGJ9HnZdXq2USfvsb4VqCoiIAE5RU_efwNIBG-uTjja4A0wDO3bMoqlPm1fSUEtwXrq8fzf9z93coKwKLMJiNZKMFssgsyMt_pyMNue--fcrQbyNoDMddULLA0LbbDwYZCbYLmYNsJb1mYVD2ympc8fwe7m8Ywg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ارتش اسرائیل آماده یورش گسترده به لبنان می‌شود
🔹
با تشدید درگیری‌ها در جنوب لبنان، منابع اسرائیلی از احتمال بالای یورش گسترده ارتش این رژیم به مناطق گسترده‌تری در لبنان تحت عنوان عملیات ««تیرهای آتش» خبر می‌دهند.
🔹
طی ماه‌های اخیر حزب‌الله لبنان با ریزپرنده‌های انتحاری مجهز به فیبرنوری (FPV) توانسته ضربات دقیقی بر ارتش اسرائیل وارد کند؛ پهپادهایی که امکان رهگیری آن‌ها وجود ندارد و در نهایت مقامات نظامی و سیاسی اسرائیلی تصمیم گرفته‌اند به زعم توقف این حملات، دایره تهاجم به خاک لبنان را گسترش دهند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/akhbarefori/654154" target="_blank">📅 14:57 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654153">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c07ac5071.mp4?token=aEpGh0KbRibUprsFeZL92fu0ATE_H9bRioCMPc9SYinIHIbQl8rS1eyDjRBynCd7iTeRT1nBJQlhF2qLDpzWw6bPaQzm-R_S2wnuOfJhIpvR29nHhc2NdhlMNlhDjInmHAhebpDHC1a8RdbFfsdkmVvBvUXkFRZQZkIDsFjaWIi6SZQsaIePgMsAdOpUlq9skBD-JcMl_ryRDlS2wUbyySRIF5xx1wztOqUoV1ArrMN7n3fbvNNjGd1C88I15HzmtINSFJZ-qvxn-W-k0-V4C_m0_ra8MqghWZNgV7j-fUILvn4rb7fqvinkr9teRoLShl1anGlPT2g-AVj07fFz-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c07ac5071.mp4?token=aEpGh0KbRibUprsFeZL92fu0ATE_H9bRioCMPc9SYinIHIbQl8rS1eyDjRBynCd7iTeRT1nBJQlhF2qLDpzWw6bPaQzm-R_S2wnuOfJhIpvR29nHhc2NdhlMNlhDjInmHAhebpDHC1a8RdbFfsdkmVvBvUXkFRZQZkIDsFjaWIi6SZQsaIePgMsAdOpUlq9skBD-JcMl_ryRDlS2wUbyySRIF5xx1wztOqUoV1ArrMN7n3fbvNNjGd1C88I15HzmtINSFJZ-qvxn-W-k0-V4C_m0_ra8MqghWZNgV7j-fUILvn4rb7fqvinkr9teRoLShl1anGlPT2g-AVj07fFz-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پهپاد آمریکایی زیر پای آرش‌های کمانگیر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/654153" target="_blank">📅 14:44 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654151">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
شکار یک مرکاوا و یک هامر توسط حزب‌الله
🔹
حزب‌الله: یک تانک مرکاوا و یک خودروی نظامی هامر دشمن اسرائیلی در دو عملیات پهپادی صبح امروز منهدم شد.
🔹
در شهر «زوطر شرقی» نیز یک بولدوزر نظامی طعمهٔ پهپاد انتحاری شده و دو تجمع نیروهای رژیم اشغالگر هدف توپخانه و موشک‌ها قرار گرفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/654151" target="_blank">📅 14:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654150">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
ارتش اسرائیل دستور تخلیه نبطیه را صادر کرد
🔹
ارتش رژیم صهیونیستی با صدور هشداری دستور تخلیه نبطیه در جنوب لبنان را صادر کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/654150" target="_blank">📅 14:29 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654149">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e062176e2.mp4?token=oO-1Bt4Pm7ew00fBRKJS5zuBTNZAxRR6NW1kA-n7FSEQASCiG4tYI23l6LXpSZ1uGKmcQuThqrVh-kTtNhMc97FF758Yllmv639iz15vmQBrXzQ5AC2pSql5GpmmqzU8A7_CSI_p0lIJnkOwB5X9i6THh1pvDKroNeKAOK2Z-aoHUy_PJeHjANX6Ac1BPbSztJqgMPOsqk_XDoGRoDuXq2zClj9kgkWwA-qsAzUHQR8uLGHYkwqB3FiWvALHi0-LwIunIQEo5VEJnIoDZj1DJSmJ2lIr_qXLBPm6l5tBuy69WSiA37CsU7mOzRwWTlM1sUy_oQwttIvv_NlN8D5lyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e062176e2.mp4?token=oO-1Bt4Pm7ew00fBRKJS5zuBTNZAxRR6NW1kA-n7FSEQASCiG4tYI23l6LXpSZ1uGKmcQuThqrVh-kTtNhMc97FF758Yllmv639iz15vmQBrXzQ5AC2pSql5GpmmqzU8A7_CSI_p0lIJnkOwB5X9i6THh1pvDKroNeKAOK2Z-aoHUy_PJeHjANX6Ac1BPbSztJqgMPOsqk_XDoGRoDuXq2zClj9kgkWwA-qsAzUHQR8uLGHYkwqB3FiWvALHi0-LwIunIQEo5VEJnIoDZj1DJSmJ2lIr_qXLBPm6l5tBuy69WSiA37CsU7mOzRwWTlM1sUy_oQwttIvv_NlN8D5lyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جولان صهیونیستها در مسجدالاقصی
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/akhbarefori/654149" target="_blank">📅 14:22 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654148">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_xxU2Gc-Bl8J2F0o1p7GCnxAuP2rEnb7H-hPJQRnvkr51NZ8tF106lf7tN3mIecnaddiHsRWw_pusYuGnlS_HgUFFr5rtOTdxW5OTeL8wHYqWIgMGUz4l07sTRp6odaJIwBfUmWo9yoylea1UWzVF-4TcyE0xvumlYv9egz7EMrTUNxDWBlAO_gJFBC4WVWKjTY_dDF9vcRiDFTwPoa4xSFrQvG95fXvxm02z82fRjmUFw-CL86hIKwmz55Ca53jdRDt8cq7MBkRa4DpwKW3aWillEHvN6Dfw5os3UZEQRlvcPVpZUOXEV5K3xVu6fmyMRUi6BJP1_NT113e8zbCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عارف: مأموریت این ستاد تنها در پیشگیری از افزایش قیمت‌ها خلاصه نمی‌شود
🔹
معاون اول رئیس جمهور در نشست ستاد تنظیم بازار:
🔹
ایجاد نگاه جامع برای حمایت همزمان از مصرف‌کننده و تولیدکننده برای دستیابی به پایداری اقتصادی، مهم‌ترین مأموریت این ستاد است.
🔹
معاون اول رئیس جمهور با توجه به چالش گرانی، بر ضرورت ترسیم تصویری دقیق از ریشه‌های تورم تأکید کرد.
🔹
برای برنامه‌ریزی در جهت مهار گرانی، باید سهم عوامل داخلی، خارجی و اختیارهای حاکمیتی به‌درستی تفکیک شود.
🔹
عبور از مانع‌ها و دستیابی به ثبات در بازار، تنها از مسیر استفاده بهینه از منابع و ارتقای بهره‌وری در همه بخش‌ها میسر خواهد بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/akhbarefori/654148" target="_blank">📅 14:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654147">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f434bd9b85.mp4?token=ruNVNzBS5SBPTS0taM2AzbuD031lm7-GcvHqg--wPRc9SVlfsnWv9zRlVAv_0DhZPO2sBvbHfSFhCr_lzcNIweNWBsTMJTJNNpT9uBlmahVBmvDPsFwnK8oKVzY_amWMUX_CAPqkP9WpHKqYnDT9q4bc5vGkuCuopLSAivtXQmJ8Tqg5asm1BiVpYZ4klFxs3aVDy1kWlGVmk55u9IqrxrvgxhioprhwSeddSFd4qc8gaeqetB7FzEj_ecylMS__3IDO9XjFAUOK0E2kcoA2YMa0gYNPBQ3SLwqw1115fhFty4V-FKsZYcxR3JmyfcfEAx0FwzmvXjx1ZSR38LuBRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f434bd9b85.mp4?token=ruNVNzBS5SBPTS0taM2AzbuD031lm7-GcvHqg--wPRc9SVlfsnWv9zRlVAv_0DhZPO2sBvbHfSFhCr_lzcNIweNWBsTMJTJNNpT9uBlmahVBmvDPsFwnK8oKVzY_amWMUX_CAPqkP9WpHKqYnDT9q4bc5vGkuCuopLSAivtXQmJ8Tqg5asm1BiVpYZ4klFxs3aVDy1kWlGVmk55u9IqrxrvgxhioprhwSeddSFd4qc8gaeqetB7FzEj_ecylMS__3IDO9XjFAUOK0E2kcoA2YMa0gYNPBQ3SLwqw1115fhFty4V-FKsZYcxR3JmyfcfEAx0FwzmvXjx1ZSR38LuBRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مرشایمر: آمریکا در جنگ ایران شکست خورده است
🔹
نظریه‌پرداز مطرح آمریکایی جان مرشایمر، به شکست ایالات متحده در جنگ با ایران اذعان کرده و گفت که واشنگتن  «نمی‌تواند راه‌حلی برای پایان این جنگ پیدا کند».
🔹
این نظریه‌پرداز خطاب به مردم آمریکا تأکید کرده که این شکست آمریکا تبعاتی منفی به دنبال خواهد داشت که همه مردم ایالات متحده را تحت تأثیر قرار می‌دهد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/akhbarefori/654147" target="_blank">📅 14:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654146">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HS5U-oOVFf9pnIzwEloEhsdp5DURqYftzcra5yJ6oPnvZ8luH0CdiJMQEV-3xYAFzO7Sq0Jl7jkA4kQnTjLRIgZNDkfw9SLlnCYVAax8oAkF7X9dtL2CEsod2ODM2l8FtiJkLOD3UEyytlsdoaV70qtDEODyLn-VyhbHa-1-1R-o7CKDaBSGbcDk8zgnM3yF7b_15OOfntxnDHHOOBWk3PklCB_Blifp-X0Z60eoyV3olPNs6oVUsZzBjthJaIkhaxJxbWgJg3FUrYYB4euGC99_tO9QGSIrfgZKjjRohMU19UYGMJcwNxSPjkanOp35OySQbftU804yFq8DZW02XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چین به نقض آتش‌بس توسط آمریکا واکنش نشان داد
🔹
به دنبال ماجراجویی‌های اخیر آمریکا علیه ایران در خلیج فارس و تنگه هرمز، چین از «طرف‌های مربوطه» خواست آتش‌بس را رعایت کنند.
🔹
مائو نینگ، سخنگوی وزارت امور خارجه، در یک نشست خبری گفت: «ما از طرف‌های مربوطه می‌خواهیم که به تعهدات آتش‌بس خود عمل کنند، اختلافات را از طریق مسالمت‌آمیز حل کنند... و احیای زودهنگام صلح را ترویج دهند.»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/akhbarefori/654146" target="_blank">📅 14:05 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654145">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QWtttpsCql-gD6pycc_DFP0uAJG-Ob9QYDMxSIsDVo9JenmgUL00DQZtmzWVA03woWWdQjdcaH952VKK6vqmNtXRPBMB76VJxYVS-O3PnNTCHRWXriHWtoi0UqBRUduddgCcLCVPAxR2p9YaFDyGL2We5jrBPiMPbs1R3Gt_HCKCv0CyTRsaNRVp5a8fmhkm4u7ZdQBNJ7OHaLSVcWtjMmcU2SE7BRT0OjCSAbNIzBtx7c0KR-x3L6cB5rke5jGVrZtA3BTw4znQPq8nx58ZAH2POGV4PYofq9uy2l40wPAOjue7-C_D1weM2cMZcPVboJ_N4rYaWIBcuNOC82-ZXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از شوخی اینترنتی تا موج سیاسی؛ ظهور «حزب مردمی سوسک»!
🔹
فضای سیاسی هند نماد عجیب و غریبی پیدا کرده است: سوسک. این نماد نه نیلوفر حزب حاکم هند (بی‌جی‌پی) است و نه علامت دست حزب مخالف کنگره، بلکه «سوسک» است، موجودی سمج، منفور و به‌باور بسیاری نابودنشدنی که به‌تازگی به نمادی سیاسی، غیرمنتظره اما قابل‌همذات‌پنداری برای جوانان هندی در فضای آنلاین تبدیل شده است.
بیشتر بخوانید
👇
khabarfoori.com/fa/tiny/news-3217224</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/654145" target="_blank">📅 14:00 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654144">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
منبع آگاه: هیچ مذاکره ای بدون دریافت پول‌های ایران امکان پذیر نیست
🔹
یک منبع نزدیک به تیم مذاکره‌کننده گفته شده آخرین اختلاف جدی میان ایران و آمریکا بر سر آغاز مذاکرات که مربوط به نحوهٔ دسترسی به منابع مسدودشدهٔ ایران بود، با میانجی‌گری و ابتکار قطر در حال برطرف‌شدن است.
🔹
براساس این گزارش، پیش‌تر آمریکا نسبت به اجرای تعهدات خود در این زمینه عقب‌نشینی کرده بود، اما ایران با پافشاری اعلام کرد «تا زمانی که پول‌های مورد توافق واریز نشده باشد، هیچ توافقی ممکن نیست». نهایتاً با رایزنی‌ها در قطر، پیشرفت‌هایی برای حل این مشکل حاصل شده است.
🔹
با این حال، تیم مذاکره‌کنندهٔ ایران با توجه به سابقه عهدشکنی آمریکا، این تفاهمات را تمام‌شده تلقی نمی‌کند و بارها اعلام داشته که «ایران برای همه گزینه‌های محتمل آماده است».
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/akhbarefori/654144" target="_blank">📅 13:56 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654143">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ct12WSAVWmN-G3UhUgrMHKCYwpm93jQIdf48GxWJV0uraLct43GeIQpSoR-bhy01zL96xp3mq_vGurcu1bGg115SUc-yiHW6WhbKbiHGxAnBcih_QzwRE3Z1Jyfh0K4poevTXWr34YxsM6MSTEILfoYxbJgBsoT3D_j5cS2x0-Ndw-ifsXvWT69MwLGS1tS1g8rbtH8qUO6R51YhXo3_qjvNXBUcLCpqhDpetfBu1ML8VyygE2ZHtV858_FIMJq6exVgfQIewhIGYACcD76KFyExTyLjFuw_imLPoG5bnLaJTfAhtxe3ltir4JNFJc4nLO82XoQ8r5yUJgNx-d9l2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیام الله اکبر
رهبر معظم انقلاب اسلامی در پیامی به مناسبت برگزاری حج فرمودند:
🔹
با سلاح الله اکبر بود که ملّت مسلمان ایران در چهل و هفت سال قبل قیام کرد، رژیم طاغوت، دیکتاتور و وابسته‌ی پهلوی را ساقط کرد، دست و پای امریکای طمع‌کار و مستکبر را از کشور بُرید و نفوذ صهیونیسم را بکلّی قطع کرد. ایشان خاطر نشان کردند: رژیم متزلزل صهیونی و غدّه‌ی سرطانی اسرائیل نیز به مراحل پایانی عمر منحوس خود نزدیک شده و به فضل الهی و مطابق با سخن قاطع و آینده‌نگر ده سال قبل رهبرعظیم‌الشأن شهید قدس‌الله نفسه‌الزّکیّه، بیست‌ و پنج سال بعد از آن تاریخ را نخواهد دید، ان‌شاءالله. به همین منظور، خبرفوری طی فراخوانی از هم‌وطنان خواست امشب ساعت 21 در هرکجا که هستند، الله اکبر گویان، سلاح اقتدار را به دشمن نشان دهند.
🔹
هفتصدوشصتمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/akhbarefori/654143" target="_blank">📅 13:46 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654142">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5482e0431c.mp4?token=dXC_hipxjDDIft44jsckFBTk_K9XQxmr2HAeTnvh_DvzKV0Ojy43slBL9yjJhvc2D_dr1hbNpGWy1uwGH_iaHkvChIifAy-aKWrBYXS9QAW_vBkFkxU0QiGMdFJYOTUUd5xNQw5ZlXjFMzwx4QTNFxY6lLCkMURPajA7pyE1o-ObDM8k2PphbfhSm3HtsSiwe8IE-nhpPDp1c6uNENB71tyOB_JtmVOgbphBkbIYAGyJPtMtsRU5Y4ZYwaCwBuny-R5kUondTmLSMgx_wnroCrzkx8ul9MlOu7Xc3bXgS-VvapbF1KBBACynTDzzUlk3DGWFUXCnHMwIXRBY4T09dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5482e0431c.mp4?token=dXC_hipxjDDIft44jsckFBTk_K9XQxmr2HAeTnvh_DvzKV0Ojy43slBL9yjJhvc2D_dr1hbNpGWy1uwGH_iaHkvChIifAy-aKWrBYXS9QAW_vBkFkxU0QiGMdFJYOTUUd5xNQw5ZlXjFMzwx4QTNFxY6lLCkMURPajA7pyE1o-ObDM8k2PphbfhSm3HtsSiwe8IE-nhpPDp1c6uNENB71tyOB_JtmVOgbphBkbIYAGyJPtMtsRU5Y4ZYwaCwBuny-R5kUondTmLSMgx_wnroCrzkx8ul9MlOu7Xc3bXgS-VvapbF1KBBACynTDzzUlk3DGWFUXCnHMwIXRBY4T09dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مزدوران و عوامل وابسته به رژیم صهیونیستی بدانند هیچ حرکت و ارتباطی از چشمان تیزبین پاسداران سازمان اطلاعات سپاه  پنهان نخواهد ماند...
🔹
پاسدارن سازمان اطلاعات سپاه با رصد شبانه‌روزی و اشراف کامل بر تحرکات شبکه‌های وابسته، این عنصر مرتبط با رسانه‌های معاند و اسرائیلی را شناسایی و در عملیاتی دقیق دستگیر کردند.
🔹
امنیت مردم، خط قرمز مدافعان ایران است؛ و هرگونه همکاری، ارسال اطلاعات یا تولید محتوا برای دشمنان این سرزمین، زیر ذره‌بین سازمان اطلاعات سپاه قرار دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/akhbarefori/654142" target="_blank">📅 13:41 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654141">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PKihuWNs8Y-3DMxkDoIV3d6MQof_pIYeWdsqvdPiNlI1vOAa8DQn0lULYigOLCCz2_ndnTlhuI1LA8N8VvCil53h56FrLWxl79C0E-C2Ar1I1bsSe4GW9gvaiEJvNfOjmvfqVtdfIt3jmnUZPvBa-c-lU92Sh0ayIQbpU2hWJ4H5v2jhCYW_N59PbthCayvz__ALl8cwDE-9rlQitlu2LmIxOPKGAxUtt0OH-aiK3MLgopGJlhJ_7i85rUYYIxLPXzmOWbxGunsofrzu-YXKhD_axfussYEfzPIz9IjPasvFIHXh4f0w02cEvm5RqgF7FZ0CCrpCLi2DCPVLearWMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شهادت سرباز وظیفه در یک مرکز ایست و بازرسی عقدا در استان یزد
🔹
سرباز وظیفه محمد معراج نظری در ایست و بازرسی شهر عقدای اردکان یزد در حین انجام وظیفه به شهادت رسید.
🔹
محمد معراج نظری در حالی‌ که در مسیر پاسداری از جان و مال مردم و تأمین امنیت عمومی در ایست و بازرسی ورودی شهر عقدا مشغول به خدمت بود، با ایستادگی در برابر خطرات، جان‌عزیزش را فدای میهن و امنیت مردم کرد.
🔹
مراسم تشییع و خاکسپاری این شهید عزیز، روز گذشته در اردکان برگزار شد و مراسم یادبود این شهید هم روزهای چهارشنبه، و پنجشنبه و یکشنبه هفته آینده برگزار می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/654141" target="_blank">📅 13:19 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654140">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GL0boQGB72py5HYfQ6cMPF0hxeOPXT-fnweYCvCHDgHWlm12h2RRMIkFFvUdJos1EHGg0ntKxT7FSwDOKRaA50jEBH21UTJNGI6lFTl-fPLLBOymlZr_aZdjgfhX39zt5EtXzaWAMzLR79cmKto2mx4_B74mh49Cl60GJ6-8FIsbXsK0rzYjxn70Q5Yo-PlVAO3KTkBxOg6MUcgyehm7gF1vTodgrkSn-lHwcztZm9gMH-SiJiB_CsYtxyYUgCXQ_ee0GraqzdR76gMa52bDKH6qF0p5oDLYPcpVpRUxB7E4qU6ukWslqKPfTwf3zQIUFYiSUQ5rsraqD5dL_ny0vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
امشب ساعت ۲۱؛ ملت ایران فریاد «الله‌اکبر» سر می‌دهند
🔹
در پی پیام مهم ولی امر مسلمین جهان و تأکید بر وحدت، مقاومت و فریاد بر سر استکبارجهانی شیطان آمریکایی و حیوان دست آموزش رژیم صهیونی، از ملت بزرگ ایران عزیز دعوت می‌شود امشب رأس ساعت ۲۱:۰۰ در سراسر کشور،…</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/654140" target="_blank">📅 12:49 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654137">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DKrhn0B8G47VBbQJZcrCEYblmLTcmi-zj8i4C_UR6x8K6z9YK6sqFV0fmyHiM7RiA2JZ2pssJ3-G5Naof5GB4YL5ktA2LoE8CyyRR7B_Ra6uqwOFlrEfUvECc11b4Li1F4buhbfZUhQCT-57Ce2PWoH8jTIKTAGEHctkzCdOOnRYBnsNHwJTgRcKnAvoDpibAh2bHO_99hur6W9i2ZLZYvhKqI0QXoTDEu1u6AfRCOsjEZ-VTS03x1wleab4XmTP7vLeptFqLV25Q_Bcv4IA8y9gtqy-BCMl1d8AYiDOLbV3ySxHKxa1kYckP6j4RYfcGzcUEyZEwLM5aoWvLx8_nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
امشب ساعت ۲۱؛ ملت ایران فریاد «الله‌اکبر» سر می‌دهند
🔹
در پی پیام مهم ولی امر مسلمین جهان و تأکید بر وحدت، مقاومت و فریاد بر سر استکبارجهانی شیطان آمریکایی و حیوان دست آموزش رژیم صهیونی، از ملت بزرگ ایران عزیز دعوت می‌شود امشب رأس ساعت ۲۱:۰۰ در سراسر کشور، بر بام‌ها، میادین و خیابان‌ها ندای «الله‌اکبر» سر دهند.
این فریاد، پژواک وحدت ملی و اسلامی، حمایت از جبهه مقاومت و تجدید عهد با آرمان‌های انقلاب اسلامی است.
🕘
زمان: امشب ساعت ۲۱
📍
مکان: بام منازل، میادین و خیابان‌های سراسر کشور
الله‌اکبر
🇮🇷
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/654137" target="_blank">📅 12:19 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654136">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V9fRIG6XvHe0xOVosiWVql6Y7XwH_DvYbZf81lxKehMQx15duRbC28iWPlyAlUryjIGYdwKOUFKrp9DXufGZrxK5L4ukcn2cqoHptOl7FwGHs95nhDqFDD48N2gNzzL5UFqhWzI2F87dn7XE_xFd_zb5BZvgH7KTmVOHUD-ChydHoFUM6daH3iyBZoqk1-VxYlzgMe2j0NzajnW4KsgOw9r_T_rQgA_PYVYrTt-fZTnvlouPJ_Z_iQTG8w8zmvndOCpPgWhBE7XWdLsENxeULpvValGNtlvlrtWYtcSN_uT2Y4HspqX8RCw3I3lPa23ZTmgo_iu2um9OMl-JeB_gBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انتشار تصویری از مِنا، دختر شش ساله‌ی فلسطینی که فیلم عزاداری پدرش بر پیکر وی، موجی از خشم علیه صهیونیست‌ها در شبکه‌های اجتماعی به راه انداخته است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/akhbarefori/654136" target="_blank">📅 12:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654135">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VqzaJ1VHuq732Kz9bVkD8fqlSOChZc3aLnrpoNJj1WvVIIwDV5tGw6YHtp9myMD1a0xDxgaWWimdLz3e7nCrUJYx8oz5sFV3xdWkpcGDwxzO3v-8EeE2MYFBaE4flCFk2va_nuUJo-SPpTprNsn3X5BDCr2MSLarIIRx6K2p5YKa7Q8Y8iJslSvVOxuwwHESZrGHBOfpiOKej3ZAFC19Nh0-C5xEuB3rQqcqvQIdEO2-AsyJyf8_HgVV829DvmEVU7tv9wRbt0P7aJN8ArsCUlqt1MEDgJnQtMnQMxk_l_Jvk2HWkn4xC7QPEF4kOXu2ZIucIEqhdhu97o_Rt4TwsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کسری بودجۀ میلیاردی قطر با بسته شدن تنگهٔ هرمز
🔹
قطر که پیش از بسته شدن تنگهٔ هرمز سود سرشاری از فروش گاز به‌دست می‌آورد، حالا با توقف کامل صادرات، کسری بودجه ۲.۸۳ میلیارد دلاری را تجربه می‌کند.
🔹
صندوق بین‌المللی پول پیش‌بینی کرده که اقتصاد قطر در سال ۲۰۲۶ تا ۸.۶ درصد کوچک‌تر شود چرا که هر روز بسته بودن تنگهٔ هرمز، صدها میلیون دلار زیان جدید به قطر تحمیل می‌کند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/akhbarefori/654135" target="_blank">📅 12:11 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654134">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QfNBYJw5zhTjP4SVNX7KUIA2FOumDtSP8IyakWGk-Z01ybyx-T7vWnXNYu42E9-MbWQps_n1kA_vNBM1zRm0BjzFHBrANF0ookHg5j9eiwLMQrIOVjEVamq2scrEPaTMRoE-6zbg7mEkVb9lK9VBFgt-sy0Mb4wno0ihMnXqGnI8oi8DQcbExt8srLRN8zm0U02rn_2xf55GroHpYJnjfSiFVRt0bICaYfQkQ8AkitIwZILOCwPcqdFJ3a8V40DBeYig2e8_l2sTBtgirgckqHfMQAJtepJZ4U3x5keErWBRvdnKC1xkg8oQAFa1dsRL5E6amUlwjOgvo28zCtWwOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی دولت: برای بازسازی‌های ناشی از جنگ تحمیلی برنامهٔ‌ بلندمدت داریم
🔹
موضوع ارزیابی خسارات ناشی از جنگ در ۲ شکل مستقیم و غیرمستقیم دسته‌بندی می‌شود؛ هر یک از دستگاه‌های تخصصی درحال ارزیابی خسارات ناشی از جنگ هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/654134" target="_blank">📅 12:06 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654133">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
سرشبکه سرویس جاسوسی رژیم صهیونیستی در خارج از کشور به دار مجازات آویخته شد؛ رژیم صهیونیستی به یهودیان هم رحم نمی‌کند
🔹
غلامرضا خانی شکراب به جرم همکاری اطلاعاتی و جاسوسی به نفع رژیم صهیونیستی، پس از تأیید حکم در دیوان عالی کشور و طی روال قانونی، به دار مجازات آویخته شد.
🔹
او در راستای مأموریت‌های واگذارشده از طرف سرویس موساد تلاش کرده بود به عنوان سرشبکه، افرادی را در داخل جذب و به سرویس معرفی کند و پس از جذب و تأیید افسران سرویس، غلامرضا خانی از طرف موساد مأموریت‌هایی را برای اجرا به این افراد واگذار کرد.
🔹
بر اساس اعترافات متهم، یکی از مهم‌ترین مأموریت‌هایی که سرویس موساد برای وی طراحی کرده بود، اعزام او به یکی از کشور‌های منطقه با هدف شناسایی و فراهم‌سازی مقدمات تروریک خاخام یهودی بوده؛ مأموریتی که نشان می‌دهد رژیم صهیونیستی برای پیشبرد اهداف پلید خود و متهم‌کردن ایران به اقدامات ضد یهودیت، حتی از قربانی‌کردن یهودیان نیز ابایی ندارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/654133" target="_blank">📅 11:49 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654132">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tGI7AHPEAS9dP4kEpqiDvo2VKX_isQ5d8s52X8b6FvrL0VURyWP9STC0E8ktNQlsDSszQvSniDKuAy1KbW_Q60pXpggFUsmAypy3I_LA_56KYi7OUURWsftqA7bS77VYxdG6mL1gPpTN93jZXKisfVOAMjdh6PNskczpwWRvUEUd8MIHesiSjQ6StN-b0gQZw21CQjLwGftTIA-5hslSRGl8BF-JL4areaYyM_1HP3jACkwaqt_tJHM35qmVd-qpbPYgmM5yb6iu315ZlDsjDoKqOh_jzYydf89kKKEW12ZVc8eOeJDMYLjIhiqPafCEyHhfCFA2HuDyIl50SQXUCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی دولت: وام ازدواح افزایش می‌یابد
🔹
سخنگوی دولت: رقم وام ازدواج در بودجه، از ۲۰۰ همت به ۳۵۰ همت افزایش پیدا کرده است؛ این افزایش با هدف دسترسی بیشتر جوانان به وام ازدواج انجام شده و رشد ۷۵ درصدی را نشان می‌دهد.
🔹
دولت همچنین در تلاش است مشکلات تأمین لوازم خانگی زوج‌های جوان را نیز کاهش دهد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/akhbarefori/654132" target="_blank">📅 11:43 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654131">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FuQddhhR-8Tu9FnjgaD4v8U8ExCrJiSm8XmtwlcrKS8zql7tFe3RSQc8gvyHZ7SqIjkGl9C4lcHTppE-dM766H2lsqbrxLgjpVyeWQ72k51uktM5MkwfGoxJdPGT__dBAI08E7LXmgKGAygpoKF1K13am6YKtyftQicEjnzf8EF95JIgo6JpxcmKoFGcKIBDY5gZO2jAzuvP2O59WXcw_fYiL0_T_si1RQUz7Oq_OkysWQWpy8CE2lh6k4_vwwc751K8FWaCwZeA5SxNjNznNCixrPO7RJF_njROcJezcagIfD9pVNYLp_vZEhMblPo0wWRyOEiFvUp4QrC5dfP8Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس‌جمهور: دشمن از توان آفندی نیروهای مسلح ایران غافلگیر شد
🔹
مسعود پزشکیان در نشست با جمعی از فرماندهان و مدیران وزارت دفاع: اقتدار دفاعی کشور مرهون مجاهدت و آمادگی نیروهای مسلح است. دشمن از توان آفندی نیروهای مسلح ایران غافلگیر شد. معیشت و مسکن نیروهای مسلح از اولویت‌های راهبردی دولت است. حرکت صنعت دفاعی به سمت فناوری‌های نوین باید شتاب بیشتری بگیرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/akhbarefori/654131" target="_blank">📅 11:27 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654128">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JR6e-CT9hoID1ATXyu7xLt9NQOvhllh5h6z0feO9b6r5546lXAV7fyti7n21xQNBa3XDZsV3tAjH9iGfmwa1seyR2cXQPRzR6nveXWm81Rugsz2TPZOwGA6X51-FdYbRofSxUV11ITfeZzAFEVZHMvNW0nCfFgLSBgLk2ct58VAOfuGJ3Q3sAyYraS7X7-UBkjk31mOcgP14nm0cbRWGSu5S1qCtLFb15jbTSF1HSedO9LX-az2041i0FnQfMogiEVghyr4sxYS6Our32ZQd6oN6-e8uudnnJpZ9-H2tZaRXOd8Nbu9GGhPj1OY6w1vUunijtPobFSUezKd6SdVKZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FNDJ4suRshDcpqvzNq_k5z76WstoBVhDWKfBlWeTnT1Aem55P-49IhZUkl3dpnGP7Fo8YJTxE0L1Rgqs8AusBJzYbc_9Qf9We-ozde6NHTQOsi9qIoz0ESLwicXKwlaeafO0ssGQ7PX_9u9AU3NErCFDhIMvZnmnN8eFIIcUsNz5DRtN1IjiHCW8ykXwHKF0rajsDjcKEj1BFobC5FKKYyM1z-CMglI5y0GGTL1xb74KjtkH-pSGE4qHw3TYXXQhKBl1w9V0iZZmKzmkVusgRkcr_3o_sAF3RWv9jUUgBZe7gDMR65ft6h6WYiCVPpsmmGjUrM-t6lLDX30tcPLIyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bwznH6peNZOwPsJhTUE_95pxsD4XKLOegHA_l7LvkzTm_EfWixl_jBX5Z-Jlv7IG4_EGvxXadQf9Jq9Rgn9_JlM_lKFSWOXMZ9h2Qt62WJmSf6bEDiXtYQlUYpOVPx2lFci_InNNHTe9Rh8GodKPjAHAVzuAIoZ_FMW6ehAM9TEvfaXcTQc-PrVo3XokBIH-bLSA1Ct1fOlWaLkqvugcpbhZpfMoPozHDQheetL78xzk1xaU255wCj5LokIIQmaJSriVtQyZqT6i6fr7Ow3ugX1QurD8raUZzGX4aNOLQ_6M3DEgBlPUs17aYGJP0RQayujUdN4v10iyaRsrjbCWXQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری از  نشست رئیس‌جمهور با جمعی از فرماندهان و مدیران وزارت دفاع
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/654128" target="_blank">📅 11:19 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654127">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a084d0138d.mp4?token=N4-wQ5b1xGH3f2zmUOch8AZXlVfkGw_9ihrTR2rLMg7Cb5aLalqYbHc1c71bZk4gT5uTc40DwuHBolWRLCCwQRtTS20G2v6lQDCcn3FgkVAE8TdFm48eHrm9SCzM6pAfTwgI4DU2NXm_A4KPbHMMEgbQr5A1AA2-G59YTmiyoTXY_Y_gOtwIUrjl_rQxtfg6minOzd0w2zxODqYChtUwHNUjVc8DNPtFkZTbP3FdG0pJaFG6FDRxswuIt71iBXbxmGoCF_sMzd0rfVZbNYdNEt4dYEVXYukhralbsDk7qv9P_-vYsjRtuxMLk7qnb-Tjyjpyz8Oi6J-PDVUOc5NPEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a084d0138d.mp4?token=N4-wQ5b1xGH3f2zmUOch8AZXlVfkGw_9ihrTR2rLMg7Cb5aLalqYbHc1c71bZk4gT5uTc40DwuHBolWRLCCwQRtTS20G2v6lQDCcn3FgkVAE8TdFm48eHrm9SCzM6pAfTwgI4DU2NXm_A4KPbHMMEgbQr5A1AA2-G59YTmiyoTXY_Y_gOtwIUrjl_rQxtfg6minOzd0w2zxODqYChtUwHNUjVc8DNPtFkZTbP3FdG0pJaFG6FDRxswuIt71iBXbxmGoCF_sMzd0rfVZbNYdNEt4dYEVXYukhralbsDk7qv9P_-vYsjRtuxMLk7qnb-Tjyjpyz8Oi6J-PDVUOc5NPEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش سخنگوی دولت به حمله دوباره آمریکا حین مذاکره با ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/akhbarefori/654127" target="_blank">📅 11:11 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654126">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oyaYdbyqYnJbG1AHi1RVXR4qutgBikAkluqjnlMju62gUL5iJVFSZ4a4Gede-rgKa6_8KEJ80WIwaiaVFfETTIufYJeqAMvfhYpGuRRPJg2Ti9xSJHXaT5eIaGoABAttmhI1vBTgMtr4qlPxQA8lNSDr4Rbp2Ju3sQg_HF23__6Zx8qz7kvGWSIkly0EHEp-GXiRk6AB0qf6Q2OOajINypbp8BquVeq__hNIORIdeaeFzJYxVjxn6ps07qedJIoB_9pEMkhpJdZ8vsVh8AFU53kXcYsNJr9atz6TcSeGAmVk7nmjL2Q3GnhPPWt99mJtllCPzyWNhBEfES5fiGBIAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
افشای دیدار رئیس شاباک با گزینه امارات برای اداره غزه
🔹
رسانه‌های اسرائیلی امروز از دیدار رئیس سازمان امنیت داخلی اسرائیل (شاباک) با محمد دحلان، چهره سابق جنبش فتح، در جریان سفر اخیر هیأت اسرائیلی به امارات خبر دادند.
🔹
رادیو عمومی اسرائیل «کان» با اعلام این خبر، گزارش داد که دحلان سال‌هاست در ابوظبی اقامت دارد و از او به‌عنوان مشاور «محمد بن زاید» رئیس امارات یاد می‌شود.
🔹
دیدار رئیس شاباک با محمد دحلان، نشانه‌ای مهم از تلاش اسرائیل و امارات برای بررسی گزینه‌های مطلوب این دو برای مدیریت غزه است، گزینه‌هایی که در آن امارات و اسرائیل برای حماس و تشکیلات خودگردان جایگاهی قائل نیستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/654126" target="_blank">📅 11:06 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654125">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
سپاه: مقابل هرگونه نقض آتش‌بس پاسخ قاطع می‌دهیم
🔹
ارتش تروریستی آمریکا در ادامه ماجراجویی‌های مداخله گرایانه در منطقه و رفتارهای متجاوزانه، در منطقه خلیج فارس وارد حریم هوایی ایران شد و یگان های پدافندی سپاه پاسداران در راستای دفاع از حریم سرزمینی کشورمان پس از پایش های اطلاعاتی دقیق، یک فروند پهپاد MQ۹ را شناسایی و ساقط کرد.
🔹
همچنین با شلیک به یک فروند پهپاد RQ۴ و جنگنده متجاوز F۳۵ آنان را وادار به فرار و خروج از حریم سرزمینی کرد.
🔹
سپاه پاسداران نسبت به هرگونه نقض آتش بس از سوی ارتش متجاوز آمریکا هشدار داده و حق پاسخ متقابل را برای خود مشروع و قطعی می داند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/akhbarefori/654125" target="_blank">📅 11:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654124">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
طبق کسب اطلاع، ادعای شبکه سعودی العربیه درباره یادداشت تفاهم ۱۴ بندی ایران و آمریکا کذب و بی اساس است
🔹
العربیه ساعاتی پیش مدعی شد به متن پیش‌نویس نهایی یادداشت تفاهم مقدماتی بین ایران و آمریکا دست یافته که در آن موضوعاتی از جمله بازگشایی تنگه هرمز، آغاز مذاکرات درباره برنامه هسته‌ای ، نحوه آزادسازی پولهای بلوکه شده ایران و برخی موضوعات دیگر مطرح شده است که تمامی این موارد تکذیب می شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/akhbarefori/654124" target="_blank">📅 11:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654123">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7838afe4e0.mp4?token=lP7P-I2pa2uWMpTUQK-_pZn58nkylk_gw052jBcYB9c-chRw7ngvxmxyDteiHFxG2E1FRRxsWjsXmczjAHICemtpgLF2-rzOMVPwt8mn_h-nra9T8DtV_hYqmEH-XS7P7RmRnxUwds2qWSF4cby8I3pOBdXwauYjs42ystOHAp3YjydVkYLBz000t29Dd5qdKI3WLAh8_xaoaER3vc675O2tTHSdIP0qvqPoNxpTg0O-uYgubhEsJ5ylQvNF1Rd-acqlEJSafnl2BFhbATLUYoT13CfJna3cTcJ3EUqJOBvBEp9cufXVesYFGgSU5CihZ7qi2BvXVl3QSl5yw9Eq6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7838afe4e0.mp4?token=lP7P-I2pa2uWMpTUQK-_pZn58nkylk_gw052jBcYB9c-chRw7ngvxmxyDteiHFxG2E1FRRxsWjsXmczjAHICemtpgLF2-rzOMVPwt8mn_h-nra9T8DtV_hYqmEH-XS7P7RmRnxUwds2qWSF4cby8I3pOBdXwauYjs42ystOHAp3YjydVkYLBz000t29Dd5qdKI3WLAh8_xaoaER3vc675O2tTHSdIP0qvqPoNxpTg0O-uYgubhEsJ5ylQvNF1Rd-acqlEJSafnl2BFhbATLUYoT13CfJna3cTcJ3EUqJOBvBEp9cufXVesYFGgSU5CihZ7qi2BvXVl3QSl5yw9Eq6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی دولت در پاسخ
🔹
دولت خود را مکلف می‌داند که بتواند مرتباً کالابرگ را به کسانی که واقعاً ذینفع هستند، پرداخت کند؛ لذا افزایش این رقم به‌صورت مشخص در حال بررسی است و ان‌شاءالله پس از نهایی شدن، اعلام خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/akhbarefori/654123" target="_blank">📅 11:00 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654121">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
‌رهبر انقلاب: امسال مسئلهٔ برائت از مشرکان اهمیتی مضاعف دارد و عمق و گسترهٔ برائت از آمریکا و رژیم صهیونی، فراتر از آیین برائت در موسم و میقات حج است و در نقاط مختلف ایران و جهان پس از این ایام مبارک، مرگ بر آمریکا و مرگ بر اسرائیل، شعار رایج امت اسلامی و مظلومان عالم خصوصاً جوانان خواهد بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/akhbarefori/654121" target="_blank">📅 10:52 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654120">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
‌ رهبر انقلاب: امت اسلامی و ملت‌های منطقه، ظرفیت‌ها و منافع مشترک زیادی دارند که نظم جدید و هندسهٔ آیندهٔ منطقه و جهان را شکل خواهد داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/akhbarefori/654120" target="_blank">📅 10:51 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654119">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJX-iXzWc8Gu8tzK-tvW90UuRe231nJp2oRf1d2XP-9NVs8DtH_TOPteONPtNNEtwuVw90H2TGASlNM4BMiQTdXzAWX7B22vAvvpFZZ_EyrSB_8WmVpgenl1WZVsxFUpd2p_JvZMZxZic7us_Hg4AuOZEAu2gh7syEMYMZyuA_aYh_ip30FKb-UAl6NY2jg90W4EQ4MDrVYY0Q7Jvtx2th_mI3-b90m6cXlyfyV0b-8iJVXLCUMQNoUy0yZ79mCkcMY2ZPiSJj3bxs5vT-KUd-lXY6pYRhyVfancRwZ-gqVU2uZbWQhTDtzLJ9unbOiPTTj8MS1Ik2nBWM-AlaOOgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کره شمالی چند موشک بالستیک شلیک کرد
🔹
ستاد مشترک ارتش کره جنوبی (JCS) اعلام کرد که «حوالی ساعت ۱۳:۰۰ روز ۲۶ می (۷:۳۰صبح به وقت تهران)، ارتش کره جنوبی پرتاب چندین موشک، از جمله موشک‌های بالستیک کوتاه‌برد، از منطقه چونجو در استان پیونگان شمالی (کره شمالی) به سمت دریای زرد را ثبت کرد.»
🔹
در بیانیه جدید کره جنوبی آمده است که ارتش کره جنوبی در واکنش به این پرتاب، سطح هشدار و آمادگی رزمی خود را افزایش داد تا برای پرتاب‌های احتمالی بعدی آماده باشد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/akhbarefori/654119" target="_blank">📅 10:49 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654118">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
‌ رهبر انقلاب: رژیم متزلزل صهیونی و غدهٔ سرطانی اسرائیل به مراحل پایانی عمر منحوس خود نزدیک شده و به فضل الهی و مطابق با سخن قاطع و آینده‌نگرِ ده سال قبل رهبر عظیم‌الشأن شهید قدس‌الله‌نفسه‌الزکیه، ۲۵ سال بعد از آن تاریخ را نخواهد دید، ان‌شاءالله
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/akhbarefori/654118" target="_blank">📅 10:48 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654117">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lrh8ULi8ioQb8u_HAEe-zyZNztrMRhV8fFcy_lWfcWD5bsiZtuyxhhSdcvBWtTvBbZ0EYxwfsDzNLbTDNo7qWTSoVM33uAeSNh2d0P_j0l6XXE1tHzUU1eLEVjQ80lkeR1Ym5mjYqpJ8_fV4TIzwd4EsFFUgNL3ONGrdu7YRjAKRkDFTqvnwIYBXfjNH65iTjwx5xOWPRKtc8kfR6GLihR2hXXw63dAW-PRh65wSf_k9dA7nl2EB6HzLR-QRDTTlMn94qTfcXyg9DoWkMWTsWKD7zx0N5BdqjrMFX_X1qC6uI58AOFauUmTj8EaWAw-zOL0DClKJnb4IMfyyAR8ytA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دولت‌های اسلامی را در راه پیشرفت امت و حل مسائل دنیای اسلام به دوستی و تعاون دعوت می‌کنم
🔹
بخشی از پیام رهبر انقلاب اسلامی به مناسبت برگزاری حج | ۵ خرداد ۱۴۰۵
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/akhbarefori/654117" target="_blank">📅 10:47 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654116">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
سرزمین‌های منطقه، دیگر سپر پایگاه‌های امریکایی نخواهند بود
🔹
اینجانب با صدق و خلوص، همه‌ی‌ کشورها و دولت‌های اسلامی را به دوستی و تعاون به خیر و نیکی دعوت می‌کنم تا با همکاری یکدیگر در راه پیشرفت امّت اسلامی و حلّ مسائل دنیای اسلام قدم برداریم. آنچه در این زمینه مسلّم است، عقربه‌ی زمان به عقب برنمی‌گردد و ملّت ها و سرزمین‌های منطقه، دیگر سپر پایگاه‌های امریکایی نخواهند بود. امریکا علاوه بر آنکه دیگر نقطه‌ی امنی برای شرارت و استقرار پایگاه نظامی در منطقه نخواهد داشت، روز به روز از وضع سابق خود فاصله می‌گیرد.
🔹
بخشی از پیام رهبر انقلاب اسلامی به مناسبت برگزاری حج | ۵ خرداد ۱۴۰۵
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/akhbarefori/654116" target="_blank">📅 10:46 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654115">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
رهبر انقلاب: آنچه مسلم است، عقربهٔ زمان به عقب برنمی‌گردد و ملت‌ها و سرزمین‌های منطقه، دیگر سپر پایگاه‌های آمریکایی نخواهند بود
🔹
آمریکا علاوه بر آنکه دیگر نقطهٔ امنی برای شرارت و استقرار پایگاه نظامی در منطقه نخواهد داشت، روز به روز از وضع سابق خود فاصله می‌گیرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/akhbarefori/654115" target="_blank">📅 10:46 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654114">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98217d691c.mp4?token=bm5mePW0u6bd4snIhhy39UzEtiTld4M_NehGwL8_rStm9SHPVhJkChMVD83VmlUq9n4ypuNISu6D-nznFiM0aDw1t4cy5qfvy19BHKnmQWa1wgGiH90JIUGEcdi1D3gCofhwSPBOjw19qRi_3qLTvS2Kf5_LvWeM3O7tSZ0Sx0XAKfg3K-0SgyjikJnJH4WURD2Zt6gKtMKr0Sv_tGnm-oPk2vQKnHNt1m2zbP4Bm4XgmRpb8NTlkumIrCTxVHhdfZiKrSlYtDp3RcRsvSVqab3UQuEztxP0eOnthjBOUtUZQ_zlOZDbP9KzJHPxG2IZ3fXl1ft5ZdoV5rUz71bC5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98217d691c.mp4?token=bm5mePW0u6bd4snIhhy39UzEtiTld4M_NehGwL8_rStm9SHPVhJkChMVD83VmlUq9n4ypuNISu6D-nznFiM0aDw1t4cy5qfvy19BHKnmQWa1wgGiH90JIUGEcdi1D3gCofhwSPBOjw19qRi_3qLTvS2Kf5_LvWeM3O7tSZ0Sx0XAKfg3K-0SgyjikJnJH4WURD2Zt6gKtMKr0Sv_tGnm-oPk2vQKnHNt1m2zbP4Bm4XgmRpb8NTlkumIrCTxVHhdfZiKrSlYtDp3RcRsvSVqab3UQuEztxP0eOnthjBOUtUZQ_zlOZDbP9KzJHPxG2IZ3fXl1ft5ZdoV5rUz71bC5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
امیر آراسته: آمریکایی‌ها جایی در خلیج فارس نخواهند داشت
🔹
رئیس هیأت معارف جنگ شهید سپهبد علی‌ صیاد شیرازی گفت: نیرو‌های مسلح ما آمادگی خود را نشان دادند. بدون اجازه نیروی دریایی سپاه پاسداران انقلاب اسلامی کسی اجازه تردد در تنگه هرمز را ندارد و کشتی‌های خارجی هم بدون اجازه ایران تردد نخواهند کرد؛ همچنین قوانین تردد توسط ایران و عمان تدوین می‌شود.
🔹
دیپلمات‌ها هم پشت نیرو‌های مسلح برای پاکسازی منطقه از پایگاه‌های آمریکایی بایستند. آمریکا جایگاهی در خلیج فارس نخواهد داشت و چه جنگ بشود و چه نشود، این امر محقق خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/akhbarefori/654114" target="_blank">📅 10:45 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654113">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8dc0c560c.mp4?token=ewDcRVbCJTEQag7u8o25LlOjiAGYu9srM9uLLVanifB3z-P9CZ1Xs2cel-LNgXZsko-ONBQp0av-JeF7pFnDOvQa6rLRb6JFV-LDRyMBmcGT0ay1Iqt4QpzxxsiCuxRxf44DM8nhNS7mkUEkTMPiYR36agf9uqDhAM216nQyuvmRCoYZClI7RUPZpIn5dyPyeHl6TdCQhlz7Mnu5Pz0EKKuGxhY-48EMRopcSan6t6UEfdjhY1ngAuw2FdnfxKUVltEyTRhBFv9IQTFDzk05T3CI3GL5pyK99tovuuIIhs25hIkdfXDVhwCQuB77K9T6Wsp9uLW803TtPqeci32zmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8dc0c560c.mp4?token=ewDcRVbCJTEQag7u8o25LlOjiAGYu9srM9uLLVanifB3z-P9CZ1Xs2cel-LNgXZsko-ONBQp0av-JeF7pFnDOvQa6rLRb6JFV-LDRyMBmcGT0ay1Iqt4QpzxxsiCuxRxf44DM8nhNS7mkUEkTMPiYR36agf9uqDhAM216nQyuvmRCoYZClI7RUPZpIn5dyPyeHl6TdCQhlz7Mnu5Pz0EKKuGxhY-48EMRopcSan6t6UEfdjhY1ngAuw2FdnfxKUVltEyTRhBFv9IQTFDzk05T3CI3GL5pyK99tovuuIIhs25hIkdfXDVhwCQuB77K9T6Wsp9uLW803TtPqeci32zmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آیا بنزین گران می‌شود؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/akhbarefori/654113" target="_blank">📅 10:43 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654112">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LH0zKIKdy7Wye3SbXK_YAQ8SbH3GQ_qD-RnbgYMJNELPUSfX30L_AbQw4RJ9hYFoz5QCI4E7nwHcDr6XkN046kqaaL598XBVWiC9oRMCuDMT3ctaLvMgw9ugvwvVGjPH8IfNr6kLhCAaWwJaSyYn2XeYAxxLBQWYfaCXbmjyxd1HWkkiktrvDHzm-O4OPl4slVZhbYVOwkbAoipkq8eqCAqZc9qQCWprm8sf-k1tcD9GcQp1g_UBEPcMGI4GvwXu_HFaHbujFposj12eAgqhAybDq_VqE4P7SqszDjSwSs6_C4MgH7-21Qb_8NJwm6d0-DzLNrugu1mVaUP60t_-eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سلاح دشمن‌شکنِ الله اکبر
🔹
با سلاح الله اکبر بود که ملّت مسلمان ایران در چهل و هفت سال قبل قیام کرد، رژیم طاغوت، دیکتاتور و وابسته‌ی پهلوی را ساقط کرد، دست و پای امریکای طمع‌کار و مستکبر را از کشور بُرید و نفوذ صهیونیسم را بکلّی قطع کرد. با همین سلاح الله اکبر بود که پس از تجاوز رژیم بعث صدّامی به خاک ایران، مجاهدان غیور و جوانان از خود گذشته، حماسه‌ی هشت سال دفاع مقدس را رقم زدند... و این ایستادگی را تا سالها بعد در برابر محاصره‌های اقتصادی، کودتا، تحریم‌های ظالمانه، حملات بی‌شمار سیاسی و تبلیغاتی و اقتصادی دشمنان علیه جمهوری اسلامی، محکم و استوار ادامه دادند.
🔹
بخشی از پیام رهبر انقلاب اسلامی به مناسبت برگزاری حج | ۵ خرداد ۱۴۰۵
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/akhbarefori/654112" target="_blank">📅 10:37 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654111">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bJjsh5CeaK81YRvPnIVRPoifD-gVP1yU2t3mHBmXHi7X9b8TWvC0x484F0zCmxZOCOz9TA_jk51HGSl0po_-Blg_oh4Nxz8Hz46gmcQOoFxlGDpioRLV6E1rWZYOK_keY0Hy0aYjt_uVGbMGiTSowBhnU7-bL1dCkhOIt3H0EMZah0txIi3PpyIudG34KVyPAeMZvxVTCnRwEIJKdixsflWDDYslIND2TdzvPYaMPbWrYSFx9u16QNb0ADc2IFE0rKT5d131z9qQSVi1xK5eq88vS5FbXAk6mvD1uAsHLQFFD5GZxNKGJdV97BbHt9SVSBGBClwLrg2eIEP0whBMvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رهبر معظم انقلاب در پیام خود به حجاج بیت‌الله الحرام تأکید کردند
🔹
آمریکایی ها بدانند: زمان به عقب برنخواهند گشت
🔹
حضرت آیت الله سید مجتبی حسینی خامنه‌ای رهبر معظم انقلاب اسلامی در پیامی به مناسبت فرارسیدن موسم حج ابراهیمی، اَعمال و اَذکار پر رمز و راز حج را نشانه‌هایی برای همیشه‌ی بشریت جهت هجرت به سمت خداوند تعالی و رهایی از قید و بند شیطان و اذنابش و سعی و تلاش بیوقفه برای عمل به تکالیف الهی و رهایی از هواهای نفس و سعادت‌مندی دنیوی و اخروی برشمردند و با اشاره به تکیه ملت بزرگ ایران بر این نشانه ها بویژه سلاح «الله اکبر» از دوران نهضت اسلامی و پیروزی انقلاب و دوران دفاع مقدس تا جنگ تحمیلی دوم و جنگ تحمیلی سوم و ناکام گذاشتن دشمنان برای تسلیم ایران و واقعه اعجاب انگیز بعثت الهی مردم، تاکید کردند: امسال مسأله برائت از مشرکان اهمیت مضاعفی دارد و عمق و گستره برائت از آمریکا و رژیم صهیونی فراتر از آئین برائت در موسم حج است و از این پس «مرگ بر آمریکا» و «مرگ بر اسرائیل» شعار رایج امت اسلامی و مظلومان عالم خصوصا جوانان خواهد بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/akhbarefori/654111" target="_blank">📅 10:35 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654110">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">459345494016_1779778963692.pdf</div>
  <div class="tg-doc-extra">415.4 KB</div>
</div>
<a href="https://t.me/akhbarefori/654110" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
پیام حضرت آیت‌الله سیدمجتبی خامنه‌ای، رهبر معظم انقلاب به‌مناسبت برگزاری حج منتشر شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/akhbarefori/654110" target="_blank">📅 10:32 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654109">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVvG0knGtfS39mU6qjb-Sje9uQJrZDYJZ20D6hDDi193j4GQDisDO3VdoqfX3wNkVKKrMqOu1pRAIX52ymNpp0SOwwHafwZBcCcJgcF6leeZqejMBHnTSdqeBSAuUktIQoct7vNs9dVIVQKHF0LKRaSghUVpj_7UQyYoh0ZmZNII6KRUl04Z4N97MuBa_ku8jwbm8ZnsI7NhnPH-CbVu6hJq4J-GUjB4aAVmUtDye_gHt9q55S_y40wzCCigbTbBElTShBRB4D9Yq5Pylakqeuw3alWPcwyI6huxgA0t96WKlO0PfF7VKRkUysp4FtXKbDLOvdu1SbeiNkAuXrzgew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مسکو: غرب تروریست‌های سوری را به جنگ ایران می‌آورد
🔹
رئیس سرویس امنیت فدرال روسیه (FSB) اعلام کرد که سرویس‌های اطلاعاتی غرب به تلاش‌های خود برای استفاده از جنگجویان تروریست سوری به‌عنوان نیروی نیابتی در جنگ با ایران ادامه می‌دهند.
🔹
طبق گزارش، به گفته الکساندر بورتنیکوف در پنجاه و هشتمین نشست شورای رؤسای نهادهای امنیتی و سرویس‌های اطلاعاتی کشورهای مستقل مشترک‌المنافع (CIS)، غرب در نظر دارد این نیروها شامل افرادی از کشورهای مستقل مشترک‌المنافع باشند که در گروه تروریستی داعش و سایر گروه‌های تروریستی جنگیده‌اند و اکنون در زندان‌های سوریه به سر می‌برند.
🔹
بورتنیکوف تصریح کرد که این شبه‌نظامیان در حال حاضر به اردوگاه‌های ویژه‌ای در عراق منتقل می‌شوند. او تأکید کرد که بدیهی است چنین نیروهای عاملی می‌توانند و خواهند توانست نه‌تنها در غرب آسیا، بلکه در کشورهایی که از آن آمده‌اند نیز به کار گرفته شوند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/akhbarefori/654109" target="_blank">📅 10:21 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654108">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83b1739b88.mp4?token=q_2LPRBrmwYiGJJekvUXWJiroGt6pI52D0YcJ8rC2RN5DZMuoatAwuaNb5uR48kLOgD1tVm8GNZQUkvNelO8alD7X8PQllbUuxVBCkdzCx-dTD7W7PuvGmNEqez2YtMztYs_3Or995pUxBUM3Afrp1ZJG5eV1AUaEqT0UjCX5vvxUQXVe0yOJ49t6R85BIAoVamFsnXnlmqJEs1mrT4HIj7B8qaBy0pysKkLsJpOk132QUVkskkv_N4PSNkIAgIS9JoWHUe78JmaMYVhZQg1IErwLeUe_c4SD7ZUtU_eerFahYdPxLwas4jGzCOgjoGPNm8cJJ1q-9u87qZsQjrizw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83b1739b88.mp4?token=q_2LPRBrmwYiGJJekvUXWJiroGt6pI52D0YcJ8rC2RN5DZMuoatAwuaNb5uR48kLOgD1tVm8GNZQUkvNelO8alD7X8PQllbUuxVBCkdzCx-dTD7W7PuvGmNEqez2YtMztYs_3Or995pUxBUM3Afrp1ZJG5eV1AUaEqT0UjCX5vvxUQXVe0yOJ49t6R85BIAoVamFsnXnlmqJEs1mrT4HIj7B8qaBy0pysKkLsJpOk132QUVkskkv_N4PSNkIAgIS9JoWHUe78JmaMYVhZQg1IErwLeUe_c4SD7ZUtU_eerFahYdPxLwas4jGzCOgjoGPNm8cJJ1q-9u87qZsQjrizw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
«نبض ماندگار» از مرز ۱۰ هزار نفر گذشت
🔹
تا این لحظه، ۱۰ هزار نفر از طریق پویش
«نبض ماندگار» خبرفوری، برای دریافت کارت اهدای عضو ثبت‌نام کرده‌اند.
🔹
در سال جاری، بیش از نیمی از ثبت‌ کارت‌‌های اهدای عضو کشور، از طریق پویش «نبض ماندگار» خبرفوری به ثبت رسیده است.
🔹
به پویش «نبض ماندگار» بپیوندید:
عدد ۱۲۰ را به ۳۴۳۲ ارسال کنید
یا از طریق لینک زیر ثبت‌نام کنید:
https://ehdacenter.ir/api/gateway?code=120
🔹
پس از دریافت کارت، تصویر آن را برای ما ارسال کنید
👇
#نبض_ماندگار
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/akhbarefori/654108" target="_blank">📅 10:17 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654107">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
کابینه امنیتی رژیم صهیونیستی امروز تشکیل می‌شود
🔹
کانال ۱۳ رژیم صهیونیستی گزارش داد که کابینه امنیتی رژیم صهیونیستی عصر امروز در ساعت ۱۹:۰۰ به وقت محلی تشکیل می‌شود.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/akhbarefori/654107" target="_blank">📅 10:06 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654106">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2de5a1a73a.mp4?token=iuMlE_8HkLg6UeUoSaIezbJ1JcqwNjzLVQX5wd1crs6uxECbs8aoNU6kTHMpDODGoNaoSMC7m9Bi8m1Z6Z8_qxBMPUOobzU4ygeS5_wSsJJaBZCTTeaWW1KjoMiz1uqj3RE_UhWGQDEOf5kaAIk_OMcTOutzT-lOHDmhxEYi6ZASrmYrFxJEk1FeE4EEICQ1bZvRyJ5lGBXKOBweonfZeQTtsUorQZOJBWMfodG2vDGFYotw8zF1ufw9V0WC3L5kO1uZX7S6DoCX6j2gbv95Rau-BloJ1Fw5aNrJwSRTy9TNvwKYuN8cNnHPmhL86lrs_0T0ReY4jscsLcC2SqsljQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2de5a1a73a.mp4?token=iuMlE_8HkLg6UeUoSaIezbJ1JcqwNjzLVQX5wd1crs6uxECbs8aoNU6kTHMpDODGoNaoSMC7m9Bi8m1Z6Z8_qxBMPUOobzU4ygeS5_wSsJJaBZCTTeaWW1KjoMiz1uqj3RE_UhWGQDEOf5kaAIk_OMcTOutzT-lOHDmhxEYi6ZASrmYrFxJEk1FeE4EEICQ1bZvRyJ5lGBXKOBweonfZeQTtsUorQZOJBWMfodG2vDGFYotw8zF1ufw9V0WC3L5kO1uZX7S6DoCX6j2gbv95Rau-BloJ1Fw5aNrJwSRTy9TNvwKYuN8cNnHPmhL86lrs_0T0ReY4jscsLcC2SqsljQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فیلترینگ دودش رفته تو چشم فعالان فناوری
امین شریفی، مدیرعامل پیام‌رسان سروش‌پلاس:
🔹
با وجود سه راند فیلترینگ در سال ۴۰۳، طبق آمار مراکز افکارسنجی، تا قبل از جنگ رمضان ۳۰ تا ۴۰ میلیون کاربر فعال در اینستاگرام و تلگرام داشتیم. اما حقیقتش بی‌توجهی و بی‌تصمیمی مدیریتی باعث شده دود این وضعیت برود توی چشم کسانی که در این صنعت فعالیت می‌کنند. مردم اشتباه فکر می‌کنند که ما عامل فیلترینگ هستیم، در حالی که بارها در نامه‌ها و مصاحبه‌ها به این مدل تنظیم‌گری اعتراض کردیم. سوال اصلی این است: استراتژی جذب کاربر باید حذف رقبا باشد یا ارائه یک ارزش پیشنهادی واقعی تا مخاطب خودش انتخاب کند؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/akhbarefori/654106" target="_blank">📅 09:52 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654105">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
اعمال محرومیت های چک برگشتی از ۹ خرداد
🔹
بانک مرکزی: محرومیت های تعلیق شده برای چک برگشتی ناشی از شرایط حادث شده در کشور با پایان شرایط اضطرار، از ۹ خرداد اعمال می شود و برای صادرکنندگان چک برگشتی، علاوه بر مسدودی حساب به میزان کسری مبلغ چک، پس از این تاریخ امکان افتتاح حساب و صدور کارت بانکی جدید، اعطای تسهیلات و تعهدات، صدور ضمانت نامه و اعتبار اسنادی و صدور دسته چک و یا ثبت چک جدید وجود ندارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/akhbarefori/654105" target="_blank">📅 09:41 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654104">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hb9-EReJA_v9hUWgWBScCgTxOPscom55IO0PGS66Rfj3c9xRfHpoaW5Yey1KN0whptVKxXj42TwmE9SC5xyWyNwdNLJ6moshNREbpEqJE2Jih3GuJGiYjaHEP8JfrApWv_fCNgm-igfFOw4w4V-C0IzBp3gTUZHU-4RIwPgZFb-joCW44YuQVB3OYm-rE0oaaszT13HJwyCLbRrUM-XZDoW-sZ17pYgVh3a3oq-XMkW0KQJwxxkSYQUe1-Exl07mcCPZ5AOWeuZXWgCtSwGfJOsgRQkhVdSNE2gNj8B1KfbYWIiAzdCHN3ZuapoQWf2j47UtQHKsBPKPQYbVJCK5xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توافق ایران و آمریکا در صورت انجام، نصفِ راه است، راهی که باید به سرمایه اجتماعی، بهبود فضای اقتصادی، نفوذ هوشمند در نظم جدید بین‌المللی، حفظ توان کشور و امید به آینده ختم شود وگرنه این راه اشتباه است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/akhbarefori/654104" target="_blank">📅 09:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654103">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h0gjqsiJ6DyT1i6d229D2lCoM8sWylAynvFE4CwIpQOmG6DMn98694dgWcgJY-j-EAlv4JcpDEwL8ysF9zvgplOK_OY3xLwJrH7d8e_5CuFDQ-rHFUoOX4UtNlJDZ4tdZbbPgF2sq84bQLak2n5ozWpl3BYyqbnHVlXfUOgww2LppZi1myTEYVoZ_-pbLGbqZhhbiE0A6D9gHi8i-zNDDznMOIh47lOkSY96_N0jdUiFhyYNG4UMMzIVU7TWcOF1y4hHvPI_Kiu6W_MzS66EHJrvu_r1tZS6PrcDrF_fX8uz1Kt-qkyW8QXwO3evupYzCvx5gIfP2aLxVn5T-5avmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اعمال محدودیت در شهرک‌های اسرائیلی از بیم حملات حزب‌الله
🔹
به دلیل ترس از حملات حزب‌الله، محدودیت‌هایی از سوی فرماندهی جبهه داخلی رژیم صهیونیستی بر ۴۳ شهرک شمال اراضی اشغالی إعمال شد.
🔹
در راستای آمادگی برای پاسخ متقابل حزب‌الله و بنا بر دستورات فرماندهی جبهه داخلی، حمل‌ونقل در خط مقدم و منطقه میرون لغو شد و کریات شمونه و سایر شهرک‌ها پس از نیمه‌شب، اعمال سیستم آموزش از راه دور را اعلام کردند. همچنین محدودیت‌های مربوط به تجمعات تشدید خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/akhbarefori/654103" target="_blank">📅 09:36 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654102">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c9c3a7d3e.mp4?token=eLuWtZ2dL9MDpmL9OmPnsk3kDm5qgRaqUhpv8uuZG2Am-1dOomoo5VOomnpc0mayKGr4b5pjnfeE35RbA5C9Acqn-R9r4BWZPzCM6jxneZqrbiv5Y2_eNXb-I5fHngj47PDoD4YsEEOM6iHxM3efAJDPPKHeWOwiOYeZ7xolQgckVQJlLPTx9G5_LJPRiqN8K-5f7a_QzNxTWR5zu6xMdb2YIOhQH9g4kZA7uZjwHkzWWaaV2VGvk8RC8q1jHeqCbXzMNdGlDa6SnGl6M2qdDF9rMniVbUNVRAVfLkZ7MSLgMGvBWDufS-ZMQPAhpYrGVk9p3EktXxxpDYtVkCwdqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c9c3a7d3e.mp4?token=eLuWtZ2dL9MDpmL9OmPnsk3kDm5qgRaqUhpv8uuZG2Am-1dOomoo5VOomnpc0mayKGr4b5pjnfeE35RbA5C9Acqn-R9r4BWZPzCM6jxneZqrbiv5Y2_eNXb-I5fHngj47PDoD4YsEEOM6iHxM3efAJDPPKHeWOwiOYeZ7xolQgckVQJlLPTx9G5_LJPRiqN8K-5f7a_QzNxTWR5zu6xMdb2YIOhQH9g4kZA7uZjwHkzWWaaV2VGvk8RC8q1jHeqCbXzMNdGlDa6SnGl6M2qdDF9rMniVbUNVRAVfLkZ7MSLgMGvBWDufS-ZMQPAhpYrGVk9p3EktXxxpDYtVkCwdqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معاون رئیس جمهور: اگر نیروهای مسلح ما آن روز صبح آن پاسخ کوبنده را در LNG قطر نداده بودند، دشمن بقیه انرژی و زیرساخت ما را هم می‌زد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/akhbarefori/654102" target="_blank">📅 09:35 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654101">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eMBGqdto3odF029TvjrVHAcip5tWFkybSe93HckguXxtNw75BGHRldDSifptiLZrBspRv-yGsEtif6JcBB9QhkOG08MoKEJtMGVaftURZbTjRD_ULtShPRI2m6C3FSyAaZPIt6vXWCeGmUyfr11M2TNg4Jyhe-9sqhIqA35841WdRhrav5uIEtH9XKoIn2B5KiVmHIcP-x9HEli1Dk4NDDVUrMRj41PPWsILrTGt67HBkSX54v-DjlidCBOJvMoXYUso0jBKg00diHtpc6nIubM8J9dMEkHt8GtX5QXu331o9j-rNy2Og_mI6T0eltGqEMDWrkc8JsJYr3NhXw4rBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هیچ آتش‌بسی در غزه وجود ندارد
🔹
ویدئویی امروز منتشر شده که یک مرد فلسطینی بر پیکر دختر ۶ ساله خود گریه می کند. او در حمله اسرائیل به یک چادر آوارگان کشته شد. آتش بسی وجود ندارد. هرگز در غزه آتش بس برقرار نشد. و صهیونیست‌ها هرگز از سلاخی کودکان غزه دست برنداشته‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/akhbarefori/654101" target="_blank">📅 09:35 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654100">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c740b029de.mp4?token=tgPtfvLWqh70imGNMkASw0kV-nNKv_DzyA7NNEfTweKeTs5edGgr9Pfwn0TSOspmKQR131P5jQ-sAZCTIgHTtsciJcWbrpISzhEPHTDxB_HrXNQmAPcd00IM3HtVzmJD6LU6FqaD_yxUyvSFroOvHuANKKN-mLxjlfXfFYHyWqhfmISDW496NViytFbjiY8E_s43FrN8P8C7WSR9HyQTsUhQKDjjXfgRAIsTDgYMmWCNMtiipBSRG4A2YeYDggTM4SnJ2oOFp88OdZWkYato9LKQK4LGtzZYzXELz0GdfXNYsGYLgjfncQ4o7Ck6EE1U_LH5dou1zZLrVl1Gw_rUog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c740b029de.mp4?token=tgPtfvLWqh70imGNMkASw0kV-nNKv_DzyA7NNEfTweKeTs5edGgr9Pfwn0TSOspmKQR131P5jQ-sAZCTIgHTtsciJcWbrpISzhEPHTDxB_HrXNQmAPcd00IM3HtVzmJD6LU6FqaD_yxUyvSFroOvHuANKKN-mLxjlfXfFYHyWqhfmISDW496NViytFbjiY8E_s43FrN8P8C7WSR9HyQTsUhQKDjjXfgRAIsTDgYMmWCNMtiipBSRG4A2YeYDggTM4SnJ2oOFp88OdZWkYato9LKQK4LGtzZYzXELz0GdfXNYsGYLgjfncQ4o7Ck6EE1U_LH5dou1zZLrVl1Gw_rUog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پاسخ صریح معاون رئیس جمهور به میزان خسارت به بخش انرژِی و زیرساخت در جنگ رمضان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/akhbarefori/654100" target="_blank">📅 09:34 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654099">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرسانه رهبر انقلاب اسلامی</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T2bBN3vTG_pTXyBSD5aYeR_C9yo4467PjIw_8imkCAIA2NAzZiTc2_wMe1HriICycKPd-E8lOOxS62rHudb9aQ439O-dAFTREIIH8pUUXq8fMErg-bwE12DQHAa6yRA2DcNAiJVKzaIebG7yO8Zq64Fwp6YHZLLUBURmoUWJeZXojyznmjIhKo7Lesv1JhUB_YqpStEc6PAxWzGXQOqu3mswgkHstf_KwcDLdm6jmCpPM6HG6EA7nhh3Q5IhwLuEAh_WUfQgwwOWc6EYS4qb0t-tqrCSaYNGXAkr_sigSi4zzBvPu8Bf80Jc3rV6rs7S1oGwWsRmNPZZpZSFqkdEbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📝
تا دقایقی دیگر پیام رهبر انقلاب اسلامی به مناسبت برگزاری حج منتشر خواهد شد.
#سلاح_الله_اکبر
📲
@rahbar_enghelab_ir</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/654099" target="_blank">📅 09:28 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654098">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
سردار شکارچی: اگر از صادرات ایران جلوگیری شود، جمهوری اسلامی ایران از خروج نفت از منطقه جلوگیری خواهد کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/akhbarefori/654098" target="_blank">📅 09:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654097">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5elqmWbz-OgPwviRtrwqIyXeuyhSah5iHmGYuhKS6e_C02R1Z55uyS3oCi7QE1aldW7RKTLgowLaCgWaLNVwXINXLbcvAYPyiwU6GP4Nuo6_xDLttmJIikzBURB2SstRiSgcyWYKwf_JbaTSCavhVuFISXDSjQ2SG9sZM5s6-0AMbITcVptKMdux4jg4_8WOObyWfFiCiy3FnaFPaMO6dkAdg2iVXIEDk9g5wdQe7FxOYbonljYB3y6Bvkkk2zwI_0xRxqLvHnbTAv6085m_S9eXa9dzByv5Nu1NCWR42O8FlrtvwkQQRUJWflfacDgUp_KKZewlSjX50njoX9_SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از محمد، کودک یک ماهه‌ی فلسطینی که شب گذشته مادرش را در بمباران رژیم صهیونیستی از دست داد و پزشکان مجبور شدند به‌علت کمبود تجهیزات بیمارستانی در غزه، یک پای او را نیز قطع کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/654097" target="_blank">📅 09:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654096">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
زیر نویس شبکه خبر: اذعان آمریکا به انجام حملاتی علیه ایران؛ سخنگوی سنتکام به حمله آمریکا در جنوب ایران اعتراف کرد
🔹
ادعای سنتکام:
🔹
[شب گذشته] دو قایق در حال مین‌گذاری در تنگه هرمز هدف قرار گرفت.
🔹
سامانه پدافند هوایی بندرعباس بمباران شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/akhbarefori/654096" target="_blank">📅 09:06 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654095">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Avg7x0d15vK1vQXs1-v393NknVQIKBh64Z5bvO1uZqLb_SL-Ucl0YWQ75d-TiLuJ8nRPzwrDBrOblmsVFNUmqqyzYY9XPKi3uufInAftcjRfbDSfRY1oiJxCKBxjcvAIpKe-lilgKVt3Kr_RhxEWj69UhMC1cUHpwc-br4dxsjZE2pWoN7Lrcsr9_VBgEW5EiQM4kKG4t439SHw5MZjALwbKsuRmCpM3fdfKKeX_ez5PIqtP6BwVHEhr_SfEoNhIiRre9At7edRCGavQ9rw42vVv7j-KeORxZNaSnlwLVcgP63DvWTt0D3A-sd9vkPE3zz2oR9Wqm_HR8XGwVQI2gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سردار شکارچی:اگر مورد حمله قرار بگیریم، حملات ما شدیدتر، سنگین‌تر و قوی‌تر خواهد بود
🔹
سخنگوی ارشد نیروهای مسلح ایران در مصاحبه با شبکه الجزیره هشدار داد: جمهوری اسلامی ایران برای جنگ آماده است و در صورت حمله جدید آمریکا و رژیم صهیونی، بانک اهدافش را شناسایی کرده.
🔹
پاسخ به هرگونه تجاوز جدید با آنچه قبلاً بوده متفاوت خواهد بود، دشمنان قطعاً با غافلگیری‌ها و تاکتیک‌های جدید روبرو خواهند شد و حملات ایران، در صورت ورود منطقه به دور دیگری از جنگ فراتر از مرزهای منطقه خواهد رفت و بسیار شدیدتر، سنگین‌تر، خشونت‌آمیزتر و قوی‌تر از دو جنگ قبلی خواهد بود.
🔹
اگر جنگ دوباره آغاز شود و از صادرات ایران جلوگیری شود، جمهوری اسلامی ایران از خروج نفت از منطقه جلوگیری خواهد کرد.
🔹
در مورد تنگه هرمز، ایران با هدف ایجاد امنیت و حفاظت از تجارت و اقتصاد بین‌المللی، این آبراه حیاتی را قاطعانه و با قاطعیت مدیریت خواهد کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/654095" target="_blank">📅 09:04 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654094">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
سخنگوی ارشد نیروهای مسلح در مصاحبه با شبکه الجزیره در مورد تنگه هرمز: ایران با هدف ایجاد امنیت و حفاظت از تجارت و اقتصاد بین‌المللی، این آبراه حیاتی را قاطعانه و با قاطعیت مدیریت خواهد کرد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/akhbarefori/654094" target="_blank">📅 09:00 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654092">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
۲ شهید و ۲۰ مجروح در پی بمباران اردوگاه آوارگان در جنوب نوار غزه
🔹
منابع خبری فلسطینی از شهادت ۲ فلسطینی از جمله یک کودک و مجروح شدن ۲۰ نفر دیگر در بمباران اردوگاه آوارگان غیث در منطقه المواصی در غرب خان یونس در جنوب نوار غزه توسط رژیم صهیونیستی خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/654092" target="_blank">📅 07:55 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654091">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c2003476c.mp4?token=nquT2Ez74e_0eVbbTm8_pwOOKlBlpj99ceHYAphnqIBDh3gm4_Cw_MjxB--7DIl_RZxxWV-uIkB1ohs-FO83f3xgcg13_7n-nYP2edTMznWooJbu4xy4a_zZu_6FsVGCkHBZP3vhrbRPVYn-oFguVjM5QEuVGOgPQe-AnyWvRk7MQMoDuvBh-mqiji65s3Bhrs_Q9p65iPxGoW3VnBan__ScbZ4HQ-_Qe2nFXglOalwx7UgVzcvCMz9UZNZNGeDP5WGAdnhbM3kyVUzwnjMqmbh3tY0-AQF5c-ztX1uPpxxtj_A3p3ReNdRR2C8ofrzTeebx5YJcd7pVHz_k9oyJ9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c2003476c.mp4?token=nquT2Ez74e_0eVbbTm8_pwOOKlBlpj99ceHYAphnqIBDh3gm4_Cw_MjxB--7DIl_RZxxWV-uIkB1ohs-FO83f3xgcg13_7n-nYP2edTMznWooJbu4xy4a_zZu_6FsVGCkHBZP3vhrbRPVYn-oFguVjM5QEuVGOgPQe-AnyWvRk7MQMoDuvBh-mqiji65s3Bhrs_Q9p65iPxGoW3VnBan__ScbZ4HQ-_Qe2nFXglOalwx7UgVzcvCMz9UZNZNGeDP5WGAdnhbM3kyVUzwnjMqmbh3tY0-AQF5c-ztX1uPpxxtj_A3p3ReNdRR2C8ofrzTeebx5YJcd7pVHz_k9oyJ9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئو حاوی تصاویر دلخراش
🔹
سگ هار آمریکا در منطقه باز هم کودکان را هدف قرار داد. در جریان بمباران جنوب غزه، خانواده‌ی یک کودک به شهادت رسیدند و کودک یک‌ماهه نیز پای خود را از دست داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/654091" target="_blank">📅 07:47 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654090">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">قسمت بیست‌و‌ششم - پادکست کافئین</div>
  <div class="tg-doc-extra">ابومسلم خراسانی</div>
</div>
<a href="https://t.me/akhbarefori/654090" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
پادکست
#کافئین
🎧
▶️
ابومسلم خراسانی
🗓
وقتی تمامِ جوانی و تخصصمان را پایِ ساختنِ کسب‌وکار و رویایِ دیگران می‌گذاریم، آیا پاداشِ وفاداری می‌گیریم؟ یا دقیقاً در لحظه‌ی پیروزی، توسطِ همان افرادِ ناامنی که خودمان به قدرت رسانده‌ایم، حذف می‌شویم؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/akhbarefori/654090" target="_blank">📅 07:47 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654089">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/280cde0e7d.mp4?token=AAGDMDCKRxDwWQn3Exg0cfs5myiub8qPRksP7nOjCPZFcxdCIEjqb3D2O7n0cp45KELAeL8fsNxT3C1HPti2eP7XMtr9rI6l4r5UggALRSmOH6cRlP9bOHUrLlyDKNyHBne1bK1MdOJ8EHBmho1wmv7-_09mWhIvWcdDE0Wovxv5CJRO585JWe8XkNQa39L3qWOcNkLAQaqmoyR6hbjqGxajU6d_DnhiVFk331Y-3qte8fIkUAGY9DqmMAEJpCaYkDqqihZqgHPRi5mknjPxtFIKBZhYfKhLTr871IinVy1oE3lexnXlSdGM8JAR7fSzcBq0pUDLsiaJLku5pwgt9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/280cde0e7d.mp4?token=AAGDMDCKRxDwWQn3Exg0cfs5myiub8qPRksP7nOjCPZFcxdCIEjqb3D2O7n0cp45KELAeL8fsNxT3C1HPti2eP7XMtr9rI6l4r5UggALRSmOH6cRlP9bOHUrLlyDKNyHBne1bK1MdOJ8EHBmho1wmv7-_09mWhIvWcdDE0Wovxv5CJRO585JWe8XkNQa39L3qWOcNkLAQaqmoyR6hbjqGxajU6d_DnhiVFk331Y-3qte8fIkUAGY9DqmMAEJpCaYkDqqihZqgHPRi5mknjPxtFIKBZhYfKhLTr871IinVy1oE3lexnXlSdGM8JAR7fSzcBq0pUDLsiaJLku5pwgt9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ابومسلم خراسانی، سردارِ سیاه‌جامگان و تراژدیِ ساخت رویای دیگران
#پادکست_کافئین
| قسمت بیست‌و‌ششم
☕️
در این اپیزود به سراغِ استراتژیستِ نابغه‌ای رفتیم که با یک قیامِ طوفانی، طومارِ خلافتِ بنی‌امیه را در هم پیچید و حکومت را دودستی تقدیمِ خاندان عباسی کرد. اما تاریخ یک قانون بی‌رحم دارد: کسی که رویای دیگران را می‌سازد، در نهایت زیرِ آوارِ همان رویا دفن می‌شود!
هر روز صبح با یک شات غلیظ از تاریخ، آمادهٔ شروع روزتان باشید!
از اینجا ببینید و بشنوید
👇
https://www.aparat.com/v/ohc3lx2
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/akhbarefori/654089" target="_blank">📅 07:46 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654088">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XICKfm5DQrsjOgL3C0uHbSnOWFg_2ZW5st6HLFYq09VMqbxO1NgDR_mA256tweohlHxIqdPkjQ7vpCAxGbMp6QLnvxfSqccZcd4QYfif6BOABW5TlzNuIt9RV-YQnJ6zn4uY5Jjv_yUvtEzXjCh7cCnAR2i4dTWXEwE_QG9J4oGDDjWYSb4dnjyAIoZUS6jBsF7CYKZRHiCJnkRC1nkK1JoG2RbRt4DvgFv0K2X4Rg3BD6401TndGKwApYuNlS-8JSPG8XxwE9p9u6MvUE23tWRuzZU4S2rwyRV8zgN457wP4KeE8Eq2SF3_RnyQXblsk6GiqjE9sUHVKfmzYQWTqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز سه‌شنبه
۵ خرداد ماه
۹ ذی‌الحجه ‌۱۴۴۷
۲۶ می ۲۰۲۶
سه‌شنبه‌ها
#دعای_توسل
بخوانیم
⬅️
متن و صوت دعای توسل
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/654088" target="_blank">📅 07:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654087">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
سخنگوی سنتکام ؛در جنوب ایران عملیات داشته‌ایم
🔹
سخنگوی سنتکام به الجزیره: نیروهای آمریکایی در جنوب ایران حملاتی در دفاع از خود انجام دادند.
🔹
این حملات برای محافظت از نیروهای آمریکایی در برابر تهدیدات نیروهای ایرانی انجام شد.
🔹
ما همزمان با خویشتنداری در جریان آتش‌بس، به دفاع از نیروهای خود ادامه می‌دهیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/akhbarefori/654087" target="_blank">📅 06:58 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654086">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
عصبانیت سناتور جنگ افروز، عربستان را تهدید کرد: سازش نکنید با عواقب وخیمی روبرو می‌شوید
🔹
«لیندسی گراهام» سناتور جنگ‌طلب جمهوری‌خواه آمریکایی: به ترامپ می گویم که در اصرار بر اینکه عربستان و دیگران به عنوان بخشی از این مذاکرات به توافق ابراهیم (سازش و عادی سازی روابط با رژیم صهیونیستی) بپیوندند، قاطع باشید.
🔹
در صورت توافق بین تهران و واشنگتن، عربستان و سایر کشورها در صورت عدم پیوستن به توافق ابراهیم با عواقب وخیمی روبرو خواهند شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/654086" target="_blank">📅 06:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654085">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
وال‌استریت ژورنال: اختلافات آمریکا و ایران ادامه دارد
🔹
یک نشریه آمریکایی شامگاه دوشنبه گزارش داد که واشنگتن و تهران همچنان بر سر برنامه هسته‌ای و لغو تحریم‌ها اختلاف نظر دارند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/654085" target="_blank">📅 04:22 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654083">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qQBs8r5feoQ8sqY_EwAsojYT6q3gIcIhBSqnaMBYsJVgZl5IEA1aVjrxO6RNu14Q_-Fv-NT_3Ha0KXoAzKTlTNeVAh7yczf0h0hE1NZAJyhZrmONh0Yzcxs1bwtUzTFJou5CmuSJEX6JOIF4andAmm5gBFftIMrcNfxxyuOsP2x4ttu5PTLiqkUATb91EtP915eZSmgEJAxW-u8mP93QbdVj_awnRZUBo105yyc7kOcl47z30HHZxMxlQne_k6UHzYwQsq_RHvHOap_YHOgZhIgSk_z4YPdgTNr7fBqMo4H0Yobg_N1JwD2DLN6XKAHIjdGKp4Y2fDY5tYxhcigong.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تأکید بقائی بر محاکمه و مجازات آمران و عاملان جنایت جنگی لامرد
🔹
سخنگوی وزارت امور خارجه حمله آمریکا به اماکن مسکونی و سالن ورزشی لامرد در روز ۹ اسفند با ۴ موشک بالستیک را جنایت جنگی شنیع و نابخشودنی خواند و تصریح کرد: آمران و عاملان آن باید در هر محکمه صالحی تحت پیگرد کیفری قرار گیرند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/akhbarefori/654083" target="_blank">📅 03:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654082">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
هشدار حزب‌الله به اسرائیل درباره گسترش دامنه جنگ
🔹
یکی از سران مقاومت اسلامی لبنان شامگاه دوشنبه گفت که تشدید تنش‌ها توسط رژیم صهیونیستی،‌ در پی آزادی عملی است که آمریکا به آن داده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/akhbarefori/654082" target="_blank">📅 03:42 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654081">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
خبرهای داغ امروز و امشب را به انتخاب مخاطبان وبسایت خبرفوری مرور کنید
♦️
🔹
آتش‌بس نقض شد؛ آمریکا حمله به ایران را پذیرفت
👇
khabarfoori.com/fa/tiny/news-3217914
🔹
اینترنت بین‌الملل فردا باز می شود
👇
khabarfoori.com/fa/tiny/news-3217890
🔹
رهبری برای مداوا تا ساعت ۲ بامداد دهم اسفند مهمان ما بودند
👇
khabarfoori.com/fa/tiny/news-3217778
🔹
کانال ۱۲ اسرائیل: تصمیم برای حمله بزرگ علیه حزب‌الله لبنان گرفته‌ شده
👇
khabarfoori.com/fa/tiny/news-3217652
🔹
سلاح مرموز آمریکا و عربستان علیه ایران/ جنگ پهپادی تهران - ریاض آغاز می شود؟
👇
khabarfoori.com/fa/tiny/news-3217866
🔻
ویدئوهای منتخب را در آپارات خبرفوری ببینید
🔻
http://aparat.com/Akhbar.Fori</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/654081" target="_blank">📅 03:00 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654080">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jhNdqIuzsDODllyLUMyK7iH8AnqH8fdkBFds6nVjyi2pgvqXuehb3tPhlfaXvKA_PFhfONcgXilzu1wB_3Vf8OjwdkMGw58oUcdt7zq3apMRWC_Ti0mNnzg094svD8Y8w0QkLq8keQaZ5rFjlkXrKMKL5qh_zWDKbVOTJNoiVSWSmS9FySu7Bq-_KcQTAJeoESPtvnGZUsaivAzdtEcbjpvfLV4n-a4GoU2-YyiB20WHR6Ai0l4Vu_Dv2g71tFNXBwJejvM0MLRcEpn03D_naqAFzVX4uT3_Qp2wCtMQRydNF5newhREupLA8JfLcQq22pRDDWYRwzVzLC2p53gT5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اذعان سنتکام به نقض آتش‌بس با ایران
🔹
سخنگوی فرماندهی مرکزی ارتش آمریکا بامداد سه‌شنبه به نقض آتش‌بس با ایران از طریق حمله به اهدافی در جنوب کشور اعتراف کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/654080" target="_blank">📅 02:46 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654079">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aP2zPv6468CxI0wkCmgb9mTyM_RPOTIUQrVCYnWBctZG_EnOJSUsZyufYRkvEe3zJmzDeoYpmswTAmS0vC6gidRN6oGyLsOs1nJCkQNwKbtpmbElVlY20oZ0nP6VNCeEXsRuH18fdDEN_Qhitl5Jioi32B8UayzgDv6auiNNa0LZc0KWKRJjkN32g7bVBYXuMS4Aa7rKAYqtGrpQY5D7OBooDU4tmSnEE_ncNP6zckJodWiaO3TS0hf3y6lvSKh7k1uho0iic7hNNFNzv4ICpjCDWkZ-QdC9W4S-LJxY9tslO4RBKQHthxdUFWRW4OhsOvejHySU6u_x1F4EMQ9FAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ بار دیگر زیاده‌خواهی درباره اورانیوم غنی‌شده را تکرار کرد
🔹
رئیس‌جمهور آمریکا بامداد سه‌شنبه مدعی شد ایران یا باید اورانیوم غنی‌شده خود را تحویل دهد یا آن را با حضور ناظران، نابود کند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/654079" target="_blank">📅 01:24 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654078">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h5aZwzsbituUBO9s-nATkr6JCH3ZuvR2a6AomqlqPTcrrSaCR29ov2UWCOFuWB9JP9OmS7ALCMrNo8SocTQa33pZGQVWtx4YYGA8c_K7rVzjlSNvgk9MunBp3wuE1AE69v_u-Y7fwlOF1ipyy0wjmebRwfOyTXjySAhiR9a0sI01TAJReXgNh8RrcVJTj2MIV5cLouMDYQYM4Q86UGDTexYl_Q48uY8gNxYwPl7EUItjOZCQ4Nrz0Ue-bL4S0M91NdAztIIvZPMyfyTQw2OjkhW3O8igavni-n_O1dZDURVBKT_2cB3meX7wERfGVHzMe_tBhK9TIghB4cUlS57Otg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شبکه خبر: منبع صدای انفجار در بندرعباس هنوز مشخص نیست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/654078" target="_blank">📅 01:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654077">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
دو قایق نیروی دریایی سپاه پاسداران در خلیج فارس توسط جنگنده‌های آمریکایی هدف قرار گرفتند و چهار سرباز شهید شده‌اند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/654077" target="_blank">📅 01:02 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654076">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
مهر: اوضاع بندرعباس کاملاً تحت کنترل است
🔹
منشا صدای انفجار از منتهی الیه شرق بندرعباس بوده است.
🔹
همزمان برخی از شهروندان از شنیده شدن صدای فعالیت پدافند در این شهر خبر داده اند.
🔹
اوضاع شهر، کاملاً تحت کنترل است و جای هیچگونه نگرانی برای مردم شریف بندرعباس نیست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/654076" target="_blank">📅 00:52 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654074">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
دقایقی پیش مردم در بندرعباس صدای چند انفجار شنیدند
🔹
هنوز محل دقیق و منشأ این صداها مشخص نیست.
🔹
همزمان در خلیج فارس حوالی سیریک و جاسک نیز صداهای مشابه شنیده شده است.
🔹
سحرگاه امروز یک فروند پهپاد متخاصم در محدوده خلیج فارس توسط نیروهای مسلح ایران منهدم شد.
🔹
اخبار تکمیلی متعاقبا اعلام می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/654074" target="_blank">📅 23:59 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654073">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UcVG8nSoWGHSyLPsMzJVrPbqonZwNtK8Ufo_81gJl9b6qSrroOlIETzIiqY7Z9_-ihzK5TvLZDZoDwdrQcIFjRbclrob8GiImYGlkykCk5a6saKDlvLbimbmxyUJosbBniSo5ceZUIpcjMe38f6BEDw2ogbw3zp7c3jhJuiWLFf_JZl6dwgAoQQU2B1xsEcBDUx9gzfLC5klfKXCeulIzLzb2Cg1Y72qcjXlDcprcvkGe1OtZGgWRuF079ZEcmVfE_DIWtNE5IzrOCu4l7X-Sky5YsQjo0VZwUwSTc5IyXBQFABBUxTv-ZcbrZDRVF1bx5dPcgOnA1pIeyCw9kLUBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وظایف مسئولان و دستگاه‌های اجرایی و مدیریتی در جنگ
🔹
مروری بر وظایف مهم کارگزاران نظام در شرایط فعلی کشور براساس پیام‌های رهبر انقلاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/654073" target="_blank">📅 23:45 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654072">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc38a79f3e.mp4?token=A_KSvofc0bBYPFoQ3UP_5I53AekrChTJJikx5xd5ndtlvwGjH6Azot6A4DJzoDL6FsHkNNRfEf32ou-5_Qr8HIBzgXnz613mGK-EZIE9VfdUK2jYJLKBuPmGkdO6SeEw3-bIdQ40C5x1Yxxx788BRSCj0OFaB6bFH55FD1bkyRUhAk9SnhqAW9UiXqfLN2L_B5u-J_X9LPy7ujiqXwrr4yEaHG6-qoYgc2qfJDVRN4Q1RdGzBz0ZbGkN9bKrNMhIPUw6OVgjjkbUv4pJlMU43sCqFmlJ70CBd-ilYhL0teh2QSBRvDtF0aQLuzeT519YH12RraQ1eV0vHGTm0agbGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc38a79f3e.mp4?token=A_KSvofc0bBYPFoQ3UP_5I53AekrChTJJikx5xd5ndtlvwGjH6Azot6A4DJzoDL6FsHkNNRfEf32ou-5_Qr8HIBzgXnz613mGK-EZIE9VfdUK2jYJLKBuPmGkdO6SeEw3-bIdQ40C5x1Yxxx788BRSCj0OFaB6bFH55FD1bkyRUhAk9SnhqAW9UiXqfLN2L_B5u-J_X9LPy7ujiqXwrr4yEaHG6-qoYgc2qfJDVRN4Q1RdGzBz0ZbGkN9bKrNMhIPUw6OVgjjkbUv4pJlMU43sCqFmlJ70CBd-ilYhL0teh2QSBRvDtF0aQLuzeT519YH12RraQ1eV0vHGTm0agbGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آیا ایران به سمت ساخت سلاح اتمی می‌رود؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/654072" target="_blank">📅 23:40 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654071">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51e1d60f76.mp4?token=Ug5YWekOD6gTaAZ-W8LtdDC7E8emsQvgGTi3j41cqjh71DQt2x2OOqDrCyDp_lN5jYupk2OjGwJ-oKS8tuPjFud1ov3v2vnorm7WyQhgbH_DMyNHVAD-60dPk_ZCd3MWcgXT_pDKco_uGO-72v--LrGJieGrP4DHVFLeCK39o1R1iYzPnhn96miu2As4ZrTmHp-wyBjcvfXKcAyOxXZ-wdFeq2s15c4xjqgNpHHHrjaFmB_wrX2d3okNV-s1C64AYwZ4cMOf8_9LAZ9FcL7UrM24T5tqiqCLaG6o77tt98OIPhHI36HPHJN9BXG1GL1wlt3tkUfnWVNk1xwRXOMjlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51e1d60f76.mp4?token=Ug5YWekOD6gTaAZ-W8LtdDC7E8emsQvgGTi3j41cqjh71DQt2x2OOqDrCyDp_lN5jYupk2OjGwJ-oKS8tuPjFud1ov3v2vnorm7WyQhgbH_DMyNHVAD-60dPk_ZCd3MWcgXT_pDKco_uGO-72v--LrGJieGrP4DHVFLeCK39o1R1iYzPnhn96miu2As4ZrTmHp-wyBjcvfXKcAyOxXZ-wdFeq2s15c4xjqgNpHHHrjaFmB_wrX2d3okNV-s1C64AYwZ4cMOf8_9LAZ9FcL7UrM24T5tqiqCLaG6o77tt98OIPhHI36HPHJN9BXG1GL1wlt3tkUfnWVNk1xwRXOMjlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس کمیسیون امنیت ملی مجلس: اگر توافقی با آمریکا شود به معنای پایان چالش‌های ما با آمریکا نیست
🔹
در شرایط موجود بعید می‌دانم که آمریکایی‌ها وارد توافقی شوند که خواسته‌های جمهوری اسلامی را بپذیرند و این موضوع خیلی دور است و اگر بپذیرند باید عمل کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/654071" target="_blank">📅 23:20 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654070">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ceac5dbe5f.mp4?token=ebZjYs8DOQ9J-Pnkn-FSjt0hreLaatvQmDqfeqFqSXJKSIMbHFbQR4K5njKXOi6E_fbBVATjxW_im93Um5k79HMBg3HoHh9cc65AqV_e5r199ffO39lqc7SmedvI4kdte4xPVtWWcoSAuL2NdNIP4tomqUyiz5BQCGvh9Ao-Cmu_xxVGEDQ-fGKgL2j-xfdzdX5hL7EyXLEnPpUnT3ConlXO3gkPlat3kTxVBXc6woENgLudMW_jBvPQ7aOJZpjARHriT7sRDiGpj-DrIQ3qoYaD-AJwWScKiUspV694wUq0rMFQ93C6ij-QJJAszYytKzN0ljFPQRrr756hT4KgZIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ceac5dbe5f.mp4?token=ebZjYs8DOQ9J-Pnkn-FSjt0hreLaatvQmDqfeqFqSXJKSIMbHFbQR4K5njKXOi6E_fbBVATjxW_im93Um5k79HMBg3HoHh9cc65AqV_e5r199ffO39lqc7SmedvI4kdte4xPVtWWcoSAuL2NdNIP4tomqUyiz5BQCGvh9Ao-Cmu_xxVGEDQ-fGKgL2j-xfdzdX5hL7EyXLEnPpUnT3ConlXO3gkPlat3kTxVBXc6woENgLudMW_jBvPQ7aOJZpjARHriT7sRDiGpj-DrIQ3qoYaD-AJwWScKiUspV694wUq0rMFQ93C6ij-QJJAszYytKzN0ljFPQRrr756hT4KgZIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس کمیسیون امنیت ملی: پهپادهای دشمن همچنان در مرزهای ایران در حال گشت زنی هستند!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/akhbarefori/654070" target="_blank">📅 23:16 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654069">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
۲ تلاش اسرائیل برای ترور شیخ نعیم قاسم ناکام ماند
🔹
شبکه الحدث گزارش داد تل‌آویو دست‌کم دو بار به تازگی تلاش کرده شیخ نعیم قاسم، رهبر حزب‌الله لبنان را هدف قرار دهد اما موفق نشده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/654069" target="_blank">📅 23:14 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654068">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c740ca854.mp4?token=IzYze0teOdYi5mVF0IbE7z3KWujTe-qdZjE5KEZz7qJEErzD4Ry8-BAdgDqOtBSbmfbKYMP75Zi_gxKQwW44VA2IjvO6PgHNXtC1ZjrqxBKdOcpVGeGniTdJLK4A92d_6ZugvmPIqo7_tHK_xYqpAba4Z3r4cw2HB84kL18f_jyPlxrwon1fADoupFGFUm6G7iW0UTj-sXbyhO5eO4D8or4UOUhp5SjidJUBjiS__haNCC8_CP0ylpqd6kp5HNpVnDBEeDOlrSnLu9bT-hak5S4u8MFmYy_bXBm44DU-v9LfJYTKZ2r57InWbYEOcgqc57nZ7tY4CSq_TU3SH62i-rRmXwNQYJMWVM3RZVj1MCfywVhPZ-ZQXjUoQhO_PfmCQpMuJO-tNVRNNJbrppqn4TzyZkLi6dDL-HjxHm9xnuSFzQRVXpl6wiKySfF3RsrtgytwUWSfzZyR7GV38lqZ50kF1H88xCatGe5TeuENccqocJhR32AIy8Tza5Mj5RwVzc3Vo7TOhOOuthfGsMx0QS3ifO0U_w7bGpvEneKP7vvJ_oe1qPC4IyE3pVD2y5svt8VEBItIymHvDE1npkPM6hKV9sS7ND7hn0peU3xqc-Kkx7Vf4bpSdZp14Z08NGMb5e53fNSofBOFM5y1TB4YbVkKcccJHlS5o8774-TCiRI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c740ca854.mp4?token=IzYze0teOdYi5mVF0IbE7z3KWujTe-qdZjE5KEZz7qJEErzD4Ry8-BAdgDqOtBSbmfbKYMP75Zi_gxKQwW44VA2IjvO6PgHNXtC1ZjrqxBKdOcpVGeGniTdJLK4A92d_6ZugvmPIqo7_tHK_xYqpAba4Z3r4cw2HB84kL18f_jyPlxrwon1fADoupFGFUm6G7iW0UTj-sXbyhO5eO4D8or4UOUhp5SjidJUBjiS__haNCC8_CP0ylpqd6kp5HNpVnDBEeDOlrSnLu9bT-hak5S4u8MFmYy_bXBm44DU-v9LfJYTKZ2r57InWbYEOcgqc57nZ7tY4CSq_TU3SH62i-rRmXwNQYJMWVM3RZVj1MCfywVhPZ-ZQXjUoQhO_PfmCQpMuJO-tNVRNNJbrppqn4TzyZkLi6dDL-HjxHm9xnuSFzQRVXpl6wiKySfF3RsrtgytwUWSfzZyR7GV38lqZ50kF1H88xCatGe5TeuENccqocJhR32AIy8Tza5Mj5RwVzc3Vo7TOhOOuthfGsMx0QS3ifO0U_w7bGpvEneKP7vvJ_oe1qPC4IyE3pVD2y5svt8VEBItIymHvDE1npkPM6hKV9sS7ND7hn0peU3xqc-Kkx7Vf4bpSdZp14Z08NGMb5e53fNSofBOFM5y1TB4YbVkKcccJHlS5o8774-TCiRI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس کمیسیون امنیت ملی مجلس: تا اقدامات پنج گانه اعتمادساز آمریکا انجام نشود، مذاکره معنا ندارد
🔹
اتمام جنگ در تمام جبهه‌ها و تضمین عدم تکرار آن باید از طرف آمریکا اثبات شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/654068" target="_blank">📅 23:13 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654067">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fjAVNPuNIJJIUsW9fpTnQ62_wHVjFAMb70jukTxOwUPDah9fCSXO-C1Uf_-WFtrU4UuG-t52vY3Q2sL44sXDUb_iOTJmduuMTty5lYUQ4XG_Jj3PL4u1UfPlc624jOILlPZWxJsAH4w8ntH_z8VU-sbUQUIzoObF-rUA6i6BTZa3pa82LgPlZnu9pEEuAKFnh06FfFQWJQQg1KGC40fhVbbqQEEq3BOELabBP8zO9WhThc95--Nxt65pTi2oq5I5mGABJtOd-43JhnAlwkX2Im9R6ilhJ2DGms5b08cv4l2vWjYlPugNh9WrJhF8ggKi3f5FjFKI8ZATP-6GcZ1jUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گفت‌وگوی وزرای امور خارجه روسیه و آمریکا درباره ایران
🔹
وزارت خارجه روسیه روز دوشنبه خبر داد که سرگئی لاوروف و مارکو روبیو در تماسی تلفنی درباره «ابتکارات دیپلماتیک برای غلبه بر بحران در تنگه هرمز» تبادل نظر کردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/akhbarefori/654067" target="_blank">📅 23:13 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654066">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
رئیس سابق سیا: آمریکا بعد از جنگ اخیر تمایلی به استفاده از پایگاه‌هایش در منطقه ندارد
🔹
دیوید پترائوس، رئیس اسبق سیا و فرمانده اسبق سنتکام در مصاحبه‌ای گفته که ایالات متحده آمریکا بعد از جنگ اخیر علیه ایران تمایل چندانی برای استفاده از پایگاه‌هایش در منطقه ندارد.
🔹
پترائوس گفت: «ما از دسترسی به بسیاری از پایگاه‌هایی که معمولاً در اختیار داشتیم، منع شدیم. البته حقیقت این است که خود ما هم حالا که دیده‌ایم ایرانی‌ها چه توانمندی‌هایی برای هدف قرار دادن این پایگاه‌ها دارند، دیگر تمایل چندانی به استفاده از آن‌ها نداریم. این تهدیدها بسیار فراتر از زمانی است که من فرمانده سنتکام (ستاد فرماندهی مرکزی آمریکا) بودم؛ یعنی بین سال‌های ۲۰۰۸ تا ۲۰۱۰.»
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/akhbarefori/654066" target="_blank">📅 23:11 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654065">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b4bf824f0.mp4?token=D-kWHWkncTNDRnydjrk1uMu2vj6qdmJSp5Gt7AFYg-MWSyktH6W5bMAVYgWVl9RqixK_uHKpy5mIjbLs6f2USaZc4ZDFYEO4-ecI3S8yLlAhSd9qNAoPhfLEyssyVD0B0XhOpTwPQaWPrRIoI_s3hvZKk5pD0nk5WDDxWPKwycBEv_amjY5l2Gx6JyXvhIsA7h9gIPoFTu-ipoDbN34lPYWnqGohs5bhvaKXOczvZsw_YjPTX2c0Nu8Lf1UVdG-oPmlcZnZ1KK7xZ-UDMlqHpRR1sh9F4beDy10Cmu48l2isYXv_rw3UkCuxT6zudKDMxddgbzi3IHYNeNTNqwlBAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b4bf824f0.mp4?token=D-kWHWkncTNDRnydjrk1uMu2vj6qdmJSp5Gt7AFYg-MWSyktH6W5bMAVYgWVl9RqixK_uHKpy5mIjbLs6f2USaZc4ZDFYEO4-ecI3S8yLlAhSd9qNAoPhfLEyssyVD0B0XhOpTwPQaWPrRIoI_s3hvZKk5pD0nk5WDDxWPKwycBEv_amjY5l2Gx6JyXvhIsA7h9gIPoFTu-ipoDbN34lPYWnqGohs5bhvaKXOczvZsw_YjPTX2c0Nu8Lf1UVdG-oPmlcZnZ1KK7xZ-UDMlqHpRR1sh9F4beDy10Cmu48l2isYXv_rw3UkCuxT6zudKDMxddgbzi3IHYNeNTNqwlBAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس کمیسیون امنیت ملی: آمریکایی‌ها هنوز درباره آزادسازی منابع بلوکه شده ایران هیچ اقدامی انجام نداده‌اند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/akhbarefori/654065" target="_blank">📅 23:10 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654064">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
فوری
🔹
۵ پیش شرطی که ابتدا آمریکا باید انجام دهد
🔹
رئیس کمیسیون امنیت ملی خبر داد:
🔹
۱. خاتمه جنگ در همه جبهه‌ها؛ مخصوصا در لبنان؛
🔹
۲. محاصره دریایی آمریکا علیه ایران باید برچیده شود؛
🔹
۳. پذیرش حاکمیت ایران بر تنگه هرمز؛ اگر محاصره ایران برچیده شود، تردد کشتی‌های غیر نظامی برقرار خواهد شد؛
🔹
۴. تعلیق تحریم های ایران طی ۳۰ روز؛ از جمله تحریم نفت
🔹
۵. آزادسازی منابع بلوکه شده ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/akhbarefori/654064" target="_blank">📅 22:59 · 04 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
