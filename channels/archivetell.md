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
<img src="https://cdn4.telesco.pe/file/ohEmD06bAw9YfcDzaId8UAQs5UMCuYoiLl2Eo-ap7kI2YgaH_r-fCyi790M3B-ap94PPHScAVf2RBDr6a_8nFUxw2TF_wCQswoOWRrxhl7ldJViM31179ITvafQAtjdrxFN0zhQIB-Nnd0F0ksHsfctLzR6i3QvBgEWiv-aChqntTbicc6HF11DZBgoJSNua8uH92k3IZYQZ0So_KpagngR3dTCoV2SexlbpAyHA-BYfHzWPFOpF1dWYXVYSFJ9MDpKL3YIlNYD8djS36O9mH3avjmnE8oHDG7wyr0ix1HI73g3iVVthjlUFO6dvvygvmrtkz68AjGCJdRKImtXf3A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 10.1K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐تبلیغات دایرکت کانالwww.youtube.com/@ArchiveTell</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-18 15:07:03</div>
<hr>

<div class="tg-post" id="msg-7694">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/So9L93KoAs6QfRKYXkGXSPOPtZS_h82ddM9xz6syeof7-7CH9ZeKWFn_JYM6-O8vTxTwaFwkoF-hXO5xLqYQVMDewyKMm2uefnwk3rm58ZRNa660ScYy_XTxVntJOwz9j2jeoY2AX6av2EjeUURAaTgDAnIdUqVuW8fYBpio4Xg3_ac1QVELiHbvff5Rg4Izz-r4MaHtx_OT8jmNXPvquINcjvbsNDiRYijme26mLFglwsy8qaiO-Z39Hsgw44BqDJbiPIsp9eMdmxxtijuwTI-91uvZewX4Bs9RNHlXwDhd7BwsExKkO94C68_L5nPcEd6lb6La91ux_eocuhuNVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">100 میلیون توکن رایگان 1 ساله
💥
🆓
Fable 5 | Opus 5 | GPT 5.6 Sol | Grok 4.6 | GLM 5.3 | Qwen 3.8 max | Kimi K3 | Deepseek V4 Pro 0813
✅
برید داخل
این سایت
ثبت نام کنید
حالا برید داخل
این بخش
پلن سالانه رو انتخاب کنید و این کد تخفیف رو بزنید :
DEVWEEK
بعد اینکه تخفیف اعمال شد تایید کنید و تمام ، یک api بگیرید و استفاده کنید
✅
📌
Base URL :
https://codecraftapi.com/v1
اکثر مدل های جهان رو داره میتونید از Playground چک کنید ، چون سایت شلوغی هست طول میکشه تا ریکوئست ها جواب بدن
‼️
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 326 · <a href="https://t.me/ArchiveTell/7694" target="_blank">📅 14:52 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7692">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QAE3Sm5ay9M3cWg_rjBnwQCbK-aTTNiL_X-HugsAzs16y3e_NMrT2WmnpEgvNokozmZihR8wleFYIWgqbFYNI5eQDJmPT7tNzcbzqj_7C8yxygtL22HvXXfkVpo6uyc_kJG8gSxE40Ryi8S7Vw9iZZ5GtABn2OKqgwoXOitVXBzF7pWibm8vYTCaQQipQeePFfB3rTe5ZqzsWGP9XlFm9xIYGaET-N7_TXxZjs8VaRHnkcKyCietjDK1MZb1T84e_C4DHjDfF4ZLw78zVU5m-sgSN_XnkM0s6VwpZyF24W3ngqa7ffJ5ywUSlpxdkS3TFDlrXwha5D2fd5VUcFWhig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">DEEPSEEK V4.1 رایگان
🙂‍↕️
🔗
alysiscode.com
✅
50 کردیت در هر 30 روز
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 916 · <a href="https://t.me/ArchiveTell/7692" target="_blank">📅 11:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7691">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🎨
غوغای جدید اوپن‌ای‌آی؛ مدل ChatGPT Images 2.5 منتشر شد!
⚡️
۵۰٪ سریع‌تر با جزئیات خیره‌کننده: جهش بزرگ در نمایش طبیعی بافت‌ها، شکست نور و واقع‌گرایی رنگ‌ها در نصف زمان قبل
✏️
قابلیت جادویی Sketch: کشیدن طرح اولیه و ترکیب‌بندی به‌صورت دستی، تا هوش مصنوعی…</div>
<div class="tg-footer">👁️ 1.29K · <a href="https://t.me/ArchiveTell/7691" target="_blank">📅 00:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7690">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/ArchiveTell/7690" target="_blank">📅 23:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7689">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✅
تغییر ریجن گوگل در ۳۰ ثانیه
⏱️
با فیلتر شکن کشور مقصد یکم برین تو گوگل بچرخین،
بعد به لینک زیر بروید، ریجن را انتخاب کنید، دلیل تغییر را بنویسید و ارسال کنید.
https://policies.google.com/country-association-form
حداکثر تا ۲ ساعت ریجن به جایی که میخواهید عوض می‌شود و ایمیلش میاد
✅
بعدش میتونین به راحتی از antigravity و سرویس های دیگه گوگل استفاده کنین.
از توجهتان ممنونم
🙏
✈️
@ArchiveTell
|
#method</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/ArchiveTell/7689" target="_blank">📅 23:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7688">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">📌
Model :
gpt-6-astra
📌
Base URL :
https://api.eirouter.ai/openai/v1
sk-e76d452dff7eccef0a1b6bde4f8262c7f628f4f2991676cf3188d0cb68023b3f
sk-778bbaffd07397311260074542e405ab11833bf458e0250363ac1afd7db02297
sk-b028d3f23d96d0b0fc96a24985164437fcaf272276caf33548a664a0df424dc1
sk-1f153c31ccd2448b30c2f56287d5dc8fcc8ddafa579d12a797450321d86e9d29
sk-3334618935b09f67a70938d3379971e3ad350fec1154008d3abbaa07565c00b3
sk-242582ef9fc5e53351eb2fd67178b83033a450a61d048cf66be6aacf98a9e2bc
sk-db726cb7cc5b14160f9d8900455fcd34fd56cbb94f3afac65494a5161eee35b6
sk-7e85fc089be2d58f76c236c8ae1efc6062f68a459bdc9f87bcbe896c2d7307e2
sk-cca857a86f2c62b5d704f2234ed5632f8ef4dfbfcc0da509fe0e021516a0406d
sk-3c3eb497a104328775de0ddb333c7c8d596c20a89e25bbe7e204318f35e2b050
موجودی هر کلید هست 5 دلار ولی نکته اینجاست توی سایت قیمت هر یک میلیون توکن این مدل هست 1 دلار
😁
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/ArchiveTell/7688" target="_blank">📅 22:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7687">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9374b9e092.mp4?token=BEzFFtJ27bdr9Qx-erY_TfUbVcIEKp01O067tqzm27Ksds-DU5RC--KNioBRd8CgttqKx_mfE2tIW820foZUYyqIE1Ud0d0wfEBp8H7FMsrayWNmu8Ecz6W5HrqTKbs_iJltKZcC6ZQGVFbnd0uOHZANCahObSF1J11Nqk_Gg2u0xDvVvVq1n46Mz9ZwwoeJRDaPwFVwD6_e40it66ymjWexkYZBSYus5tEiGmS0SZdBqAutYyxBp-0z3_krjG3xVbi_pwa6UP0YXVXkcgzSMZV7sY2VxSqHFtMswz8EyxqtIOmcE7v4DOrkWQ5mA9wLlUdgn3bUDiVNksLiQ9vC36M7FUiEOKcg-2mLtccc8f-qIfA07rWMH87fUkyCBn7AZbRYObSATcn6lCR32x9Nh-6D9sUzAtpwuaZ9jqqFN6LVWtjdDQ_B5VOk5_FxQv7Y7-LArUAzTdn6x0L-tYAeAhCQRjMkB1LEG2zwqslVK0Oxxo4ZTFPkhYA5gagNkV4E96FXc-x8o-tCdCkBvHHV_NHL7nlza8Hx-JZBaC8cPvitstqrUd6E_kVidTgMybKOn0uH82xoELDrXrXOcdah_Xxjd9vrKbzsf96Lwhd2EWqtIkIfe9cecDFhzL8Hcxc2JSxrIQ0EjbrVmJ6WBXkDYXhbrreKDQGvliU-JrKH1bs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9374b9e092.mp4?token=BEzFFtJ27bdr9Qx-erY_TfUbVcIEKp01O067tqzm27Ksds-DU5RC--KNioBRd8CgttqKx_mfE2tIW820foZUYyqIE1Ud0d0wfEBp8H7FMsrayWNmu8Ecz6W5HrqTKbs_iJltKZcC6ZQGVFbnd0uOHZANCahObSF1J11Nqk_Gg2u0xDvVvVq1n46Mz9ZwwoeJRDaPwFVwD6_e40it66ymjWexkYZBSYus5tEiGmS0SZdBqAutYyxBp-0z3_krjG3xVbi_pwa6UP0YXVXkcgzSMZV7sY2VxSqHFtMswz8EyxqtIOmcE7v4DOrkWQ5mA9wLlUdgn3bUDiVNksLiQ9vC36M7FUiEOKcg-2mLtccc8f-qIfA07rWMH87fUkyCBn7AZbRYObSATcn6lCR32x9Nh-6D9sUzAtpwuaZ9jqqFN6LVWtjdDQ_B5VOk5_FxQv7Y7-LArUAzTdn6x0L-tYAeAhCQRjMkB1LEG2zwqslVK0Oxxo4ZTFPkhYA5gagNkV4E96FXc-x8o-tCdCkBvHHV_NHL7nlza8Hx-JZBaC8cPvitstqrUd6E_kVidTgMybKOn0uH82xoELDrXrXOcdah_Xxjd9vrKbzsf96Lwhd2EWqtIkIfe9cecDFhzL8Hcxc2JSxrIQ0EjbrVmJ6WBXkDYXhbrreKDQGvliU-JrKH1bs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎨
غوغای جدید اوپن‌ای‌آی؛ مدل ChatGPT Images 2.5 منتشر شد!
⚡️
۵۰٪ سریع‌تر با جزئیات خیره‌کننده:
جهش بزرگ در نمایش طبیعی بافت‌ها، شکست نور و واقع‌گرایی رنگ‌ها در نصف زمان قبل
✏️
قابلیت جادویی Sketch:
کشیدن طرح اولیه و ترکیب‌بندی به‌صورت دستی، تا هوش مصنوعی خودش اونو به آرت نهایی تبدیل کنه
🎯
ادیت موضعی دقیق:
امکان هایلایت و تغییر دادن فقط یک نقطه خاص از عکس، بدون دست‌خوردن بقیه جزئیات تصویر
💡
نکته دسترسی:
تعدادی تمپلیت آماده هم برای تسریع کار اضافه شده و این مدل در حال حاضر به‌صورت عمومی داره برای تمام کاربران فعال میشه؛ حتماً حسابتون رو چک کنید.
🔗
ورود و تست در وب‌سایت
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/ArchiveTell/7687" target="_blank">📅 22:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7686">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">⭐️
۶ پلتفرم برای تست رایگان GPT-6 Astra
دسترسی مستقیم و استفاده از API مدل‌های پرچمدار و سنگینی مثل GPT-6 Astra معمولاً هزینه بالایی داره و اگه حواستون نباشه خیلی سریع اعتبارتون رو صفر می‌کنه!
💸
با این حال، یه سری پلتفرم کاربردی وجود دارند که اعتبار (Credit) اولیه یا سهمیه تست رایگان می‌دن تا بدون نیاز به پرداخت، بتونید قدرت این مدل رو توی چت، کدنویسی، پردازش تصویر یا ساخت ایجنت بسنجید:
1⃣
پلتفرم Vercel AI Gateway
یکی از مطمئن‌ترین گزینه‌ها به‌خصوص برای دولوپرها. این سرویس هر ۳۰ روز حدود
۵ دلار کردیت AI رایگان
به کاربرانی که حساب فعال دارند میده. محیط Playground، پشتیبانی از ایجنت‌ها و سازگاری کامل با فرمت OpenAI API داره و برای ادغام با پروژه‌های شخصی عالیه.
2⃣
پلتفرم Brainbase
اگر دنبال کدنویسی پیشرفته، تحلیل ریپوزیتوری و ایجنت‌های خودکار هستید، اینجا فوق‌العاده‌ست. بعد از ثبت‌نام اولیه،
۲۵ دلار کردیت رایگان بدون نیاز به کارت اعتباری
دریافت می‌کنید تا بتونید تسک‌های سنگین برنامه‌نویسی و اتوماسیون رو با مدل پیش ببرید.
3⃣
ابزار Roboflow Playground
بهترین جا برای محک زدن قابلیت‌های بینایی ماشین و پردازش تصویر (Vision). توی این محیط می‌تونید اسکرین‌شات‌ها، نمودارها و تصاویر پیچیده رو بدون نیاز به کلید API آپلود کنید و دقت تحلیل مدل رو با بقیه ابزارها مقایسه کنید.
4⃣
سرویس CometAPI
اگه مدل رو برای اتصال به ربات تلگرام، افزونه یا اپلیکیشن خودتون می‌خواید، این سرویس کار رو راحت کرده. بعد از ثبت‌نام کردیت رایگان میده و چون ساختارش دقیقاً مشابه API استاندارد اوپن‌ای‌آی هست، بدون تغییرات عجیب غریب توی زیرساخت کارتون راه می‌افته.
5⃣
پلتفرم Imaginode
یک فضای همه‌فن‌حریف با محیط تعاملی Canvas، چت، API و ادغام با پروتکل‌های MCP. بدون کارت بانکی کردیت اولیه میده و هر پیام با این مدل حدود ۱۲ کردیت مصرف می‌کنه؛ بنابراین برای ساخت سناریوهای متصل‌کننده متن، تصویر و اتوماسیون حسابی جوابه.
6⃣
سایت Vibany
ساده‌ترین و دم‌دستی‌ترین راه برای تست تفریحی و سریع. در بدو ورود حدود ۳۰۰ کردیت رایگان می‌گیرید و هر بار اجرای مدل حدود ۱۰۰ کردیت کم می‌کنه. یعنی حداقل ۳ الی ۴ تا پرامپت عمیق و جدی می‌تونید بهش بدید تا خروجی رو با مدل‌های قبلی مقایسه کنید.
✈️
@ArchiveTell
|
#AI
#API</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/ArchiveTell/7686" target="_blank">📅 16:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7685">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🧠
شیائومی وارد میدان ایجنت‌ها شد؛ معرفی دستیار همه‌کاره MiMo Desktop!
بچه‌ها شیائومی رسماً وارد قلمرو ایجنت‌های سیستمی شده و یه دستیار دسکتاپی معرفی کرده که مثل ترکیب Codex و قابلیت‌های کنترل کامپیوتر Claude عمل می‌کنه؛ این ابزار خوراک خودکارسازی کارهای روزمره شماست.
🖥
کنترل کامل دسکتاپ و وب:
اجرای خودکار تسک‌ها، کلیک، تایپ، کار با فایل‌ها، پر کردن فرم‌ها و امکان ضبط و اجرای مجدد فعالیت‌ها (Record & Replay)
⚡️
پیش‌نمایش تعاملی و ادیت موضعی:
رندر زنده سایت‌ها، گیم‌ها و داشبوردها با قابلیت هایلایت کردن یک بخش و بازنویسیِ انحصاری همان قسمت
🧠
دسترسی رایگان به مدل‌های نسل بعد:
بهره‌مندی تسترها از دو مدل معرفی‌نشده و پرچم‌دار MiMo-X-Pro-Preview و MiMo-X-Flash-Preview
💾
کشینگ فوق‌سریع تا ۹۹٪:
فناوری بهینه‌سازی توکن برای تغییرات مداوم پروژه‌ها جهت جلوگیری از هزینه‌های اضافی
💡
نحوه ثبت‌نام در نسخه بتا:
ظرفیت بتا کاملاً محدوده و اولویت با کاربران فعال اکوسیستم MiMo Open Platform خواهد بود؛ فرم درخواست رو پر کنید تا لینک دسترسی و مدل‌های جدید زودتر براتون فعال بشه.
🔗
فرم ثبت‌نام در نسخه بتا
🔗
صفحه رسمی معرفی
🔗
صفحه رسمی قابلیت ها
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/ArchiveTell/7685" target="_blank">📅 16:23 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7684">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fc89182f1.mp4?token=OFfUo69yjSuYTpEiOePJ1RX9vnEgqQqdGErwIYHDw2xJiS8ewvkI_oZZL0LWc-bXV0sCEMbRVV58e3fdgAMBBssGr0XCxU5pdi5p8-UzwjPDIS3JW1Loxnizvfn-rE1ZyORD6nwbhlcGyUfCcMjMNpbTvSmh0ON7L-Xv4c2suNmqGsA-EqIhJYsKVR_wPLXjIOTz3ew-YhdJRpEk9HZ7XNK06z_wa08CeqkeDpp2cIWAhsoZRHwbkejs4hXGwKJW3oXAfoq2WNRCuxuxywwaC0BkA0JUYmCHja7pUynlljDDDjMgCfwQZDCNtPYTGyvW-VrgfgIDng7kneOw_YtO4nRnZYw_azox4s8eWo8wHKO3fbem_tl6Q3ddVwDevV_9PU4aD1soYOB_CecdHRy4ujNFqiHZzjhABIXlU4KU4Ku6ML1kMklllyqt3twbepV0CqPFIXRAkpuaW_tylhoxiYjTI5OAc1te0BlpkxTfeiO0QU4YNXrlKcf7jcZ20SXr5MGCdKvl2NBNJHnbSYy0Imp2memcW20HmUQqXoGA6ymVU-jfKeFofcy45xWQS9zyPacxQOKzTVI_R1EyUW6DzotdrclVfOFqfzyYTwFA8cxWR8q47FsJzSp57XWaQTvhoerhvGXnp5feO5u9bEJf4eSGdEuOVM3t5ryCYUCDVzY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fc89182f1.mp4?token=OFfUo69yjSuYTpEiOePJ1RX9vnEgqQqdGErwIYHDw2xJiS8ewvkI_oZZL0LWc-bXV0sCEMbRVV58e3fdgAMBBssGr0XCxU5pdi5p8-UzwjPDIS3JW1Loxnizvfn-rE1ZyORD6nwbhlcGyUfCcMjMNpbTvSmh0ON7L-Xv4c2suNmqGsA-EqIhJYsKVR_wPLXjIOTz3ew-YhdJRpEk9HZ7XNK06z_wa08CeqkeDpp2cIWAhsoZRHwbkejs4hXGwKJW3oXAfoq2WNRCuxuxywwaC0BkA0JUYmCHja7pUynlljDDDjMgCfwQZDCNtPYTGyvW-VrgfgIDng7kneOw_YtO4nRnZYw_azox4s8eWo8wHKO3fbem_tl6Q3ddVwDevV_9PU4aD1soYOB_CecdHRy4ujNFqiHZzjhABIXlU4KU4Ku6ML1kMklllyqt3twbepV0CqPFIXRAkpuaW_tylhoxiYjTI5OAc1te0BlpkxTfeiO0QU4YNXrlKcf7jcZ20SXr5MGCdKvl2NBNJHnbSYy0Imp2memcW20HmUQqXoGA6ymVU-jfKeFofcy45xWQS9zyPacxQOKzTVI_R1EyUW6DzotdrclVfOFqfzyYTwFA8cxWR8q47FsJzSp57XWaQTvhoerhvGXnp5feO5u9bEJf4eSGdEuOVM3t5ryCYUCDVzY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
آرشیو ۱۵۰ پرامپت آماده برای خلق ویدیوهای سینمایی با AI!
بچه‌ها اگه با هوش مصنوعی ویدیو می‌سازید ولی خروجی‌ها تخت و مصنوعی میشن، این کالکشن خفن خوراکتونه. یه دیتابیس آماده از ۱۵۰ پرامپت تست‌شده که دقیقاً دستور زبان کارگردانی و سینمایی رو به مدل تزریق می‌کنه.
🎥
کنترل دقیق نور و دوربین:
پرامپت‌های تخصصی برای مدیریت لنز، زوایای حرکت دوربین، نورپردازی و دکوپاژ
🎞
همراه با نمونه ویدیویی:
هر دستور شامل پیش‌نمایش رندر واقعی است تا قبل از خرج توکن، خروجی کار رو ببینید
🎭
تنوع ژانر و اتمسفر:
پوشش کامل انواع سبک‌ها، سناریوها، اکت کاراکترها و فضاسازی‌های سینمایی
💡
نکته استفاده:
تمام پرامپت‌ها آماده Copy/Paste هستند؛ فقط کافیه کپی‌شون کنید داخل ابزارهایی مثل Runway ،Kling یا Luma و المان‌ها یا کاراکتر مدنظرتون رو با کلمات کلیدی دلخواه جایگزین کنید.
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/ArchiveTell/7684" target="_blank">📅 15:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7683">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gfeWUm6t0dSQWYgn1eQLMK5UtTU_ImUuscakRaOINDQVNQacAJkGloPnqfmg56ZEvWXVtdD7RUZjbz7qrOj0ld1wlzBWE9mLhc8V0ZqM-ncXkqCe0_Q3nIYJ6PcxSFYdyFNJDHvcDYPgFVHkdYcJLUklL3Vy09ZblDP8xY0O83Lkbj6IP2NdlRXjYjb3kRtGy8HLHqWfD92kn1fnSyozTymjb-DMAZvXTaoHvrfnbebbLrYdr-xoHbn2lYLehrYs7aB-lBiVnwKXZ6xm9ckDOS4YIxeGrJgqYuU8H3KIbmY1voJ5gPwLfEecCgYNlMKB6-XL7eSPn_lKAtlD8oehyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مایکروسافت آفیس رسماً مرخص شد؛ معرفی غول اوپن‌سورس GenOffice!
بچه‌ها اگه از خرید لایسنس آفیس یا برنامه‌های سنگین خسته شدید، این پروژه جدید خوراکتونه. یک جایگزین کاملاً رایگان و متن‌باز برای مایکروسافت آفیس که ایجنت‌های هوش مصنوعی رو مستقیماً آورده داخل اسناد، جداول و ارائه‌هاتون.
📝
پکیج کامل و همه‌کاره:
مدیریت بی‌دردسر داکیومنت‌ها، شیت‌های آماری، ساخت اسلاید و کار با PDF بدون نیاز به ابزارهای متفرقه
🤖
ایجنت‌های تحلیل‌گر:
اتصال مستقیم به مدل‌های قدرتمندی مثل DeepSeek ،Claude و Kimi برای تحلیل داده، نگارش متن و تولید محتوا
💻
آزاد و مولتی‌پلتفرم:
پشتیبانی رسمی و نیتیو از مک، ویندوز و لینوکس بدون نیاز به پرداخت حتی یک ریال
💡
نکته جالب توسعه:
جالبه بدونید نسخه اولیه این پروژه رو فقط یک مهندس، توی مدت یک هفته و با سوزوندن ۱۰ هزار دلار توکن هوش مصنوعی جمع کرده! ریپو تازه پابلیک شده و سرعت استقبال ازش وحشتناک بالاست.
🔗
گیت‌هاب GenOffice
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/ArchiveTell/7683" target="_blank">📅 14:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7682">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e226c05d7f.mp4?token=ZWyNYC3XWf7dI0DGAg1TrtbnlCWIPSF1MoMQszn1Bx8zl4zVsRGZS8TcVRUocko4nrBnTYL_wPMTfOTGugQuSYcw7sMdYKACbinbtdpNdpeKEExKNmAHx3xJlED-t-JHXzqRx4xlTcBaKAKRstuS9ZVe2Cczlr0hzZkDl6p3PD41_AfWCl_g0t9yfI4zZ9jOZEXU1puivcdOcaOj88ypS_iXvcNfvogtqZOK0ObamroZdgaJzjxo6BMTYvaiV5aULokaG9lVRIh397vVnpXGx14_c9Z8np8wA-4Y2XeO-Fl4-zdHBIaU0SVk93Qa-E_t_SmXHJyiYrUtXifJSlmg7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e226c05d7f.mp4?token=ZWyNYC3XWf7dI0DGAg1TrtbnlCWIPSF1MoMQszn1Bx8zl4zVsRGZS8TcVRUocko4nrBnTYL_wPMTfOTGugQuSYcw7sMdYKACbinbtdpNdpeKEExKNmAHx3xJlED-t-JHXzqRx4xlTcBaKAKRstuS9ZVe2Cczlr0hzZkDl6p3PD41_AfWCl_g0t9yfI4zZ9jOZEXU1puivcdOcaOj88ypS_iXvcNfvogtqZOK0ObamroZdgaJzjxo6BMTYvaiV5aULokaG9lVRIh397vVnpXGx14_c9Z8np8wA-4Y2XeO-Fl4-zdHBIaU0SVk93Qa-E_t_SmXHJyiYrUtXifJSlmg7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرکت خفن: تبدیل هوش مصنوعی Astra به یک بات بازی‌ساز حرفه‌ای!
🎮
🔥
داستان از این قراره که یه دولوپر، Astra رو طوری شخصی‌سازی کرده که عملاً تبدیل شده به یه ماشین بازی‌سازی. اصلاً هم شوخی یا بازی‌های دوبعدی و پیکسلی دم‌دستی نیست؛ کیفیت کار در حدیه که باورتون نمیشه کل این دموی سه‌بعدی خفن فقط توی
یک ساعت
جمع شده!
👀
⏱
سازوکارش چطوریه؟
🛠
همه‌چیز با یه اسکیل (Skill) جلو میره:
* اول Astra باهاتون گپ می‌زنه و از بین ایده‌هاتون، کانسپت اون بازی رویایی که تو ذهنتونه رو درمیاره.
* بعد طبق همون پلن، توی ده‌ها دور آزمون و خطا پروژه رو قدم‌به‌قدم کدنویسی می‌کنه و می‌سازه.
پرامپت استفاده‌شده برای ساخت این دمو:
📝
Prompt (high effort): /dream-loop Build me a graphics demo: isometric camera, voxel-ish art style with realistic shading and reflective wet floors, a character in an interesting scene. Fantasy setting (think Elden Ring, Diablo). Three.js in browser, >60fps. Don't download assets. Time limit of 1 hour. Controls: click to move the character, camera lazy-follows; drag to rotate camera; scroll to zoom in/out. No gameplay for now. World should feel alive: motion, animations, subtle environmental behaviors. Area around player should look expansive, but only allow movement in a limited space. No need to confirm the art with me or ask questions, just go!
🔗
دموی بازی توی مرورگر
🔗
خود اسکیل Astra
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/ArchiveTell/7682" target="_blank">📅 14:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7681">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J9SEUGZSyjOLMzV1q7zBAWWm0Qe10N15li1iv3pCDfwHYWTheHY0g6ewhy4I450ArWToIGdgEavKP8ts_b0XoTmgCC-F-6rb3dxbzJeK4wtBoWXNg1R6oMXcWN5sqHo08oVEgiptMiuBkvZwD-dh02y6IQqDAn8kCUpsXOdvCSAgLzoTpU76D5yGbbLZcBEHkDnnPvQr-N3CZ7Ct6NOIE8FcZDqmG_3sh7WJbIQarjr3oqnksVv1xckoOsSOyyWiKzvIG4JF4O03VF1uKLBrdnFAyHodGEUZ_INTPhJ39hPztVGmaPFMdG-BhlKkF0QmEasxTSPvU7fksK1UHVVbHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📝
باز کردن بی‌دردسر فایل‌های آفیس روی اندروید با OpenDocument!
بچه‌ها اگه فایل‌های متنی یا اداری دارید و دوست ندارید برای باز کردنشون تو سرورهای ابری آپلود بشن، این اپ خوراکتونه. تمام اسناد OpenOffice و LibreOffice رو کاملاً آفلاین، سریع و بدون نیاز به اکانت باز می‌کنه.
📁
پشتیبانی کامل از فرمت‌ها:
خواندن بی‌نقص ODT ،ODS ،ODP در کنار فایل‌های رایج DOCX ،XLSX ،PPTX و حتی PDF
🔒
حریم خصوصی واقعی:
پردازش کاملاً لوکال، بدون اتصال به اینترنت، بدون ترکرهای تبلیغاتی و بدون نیاز به ثبت‌نام
⚡️
سبک، امن و باسابقه:
یکی از قدیمی‌ترین و پایدارترین پروژه‌های متن‌باز اندروید (فعال از سال ۲۰۱۰)
💡
نکته کاربردی:
بهترین گزینه برای کسایی که با فایل‌های کاری و اسناد حساس سر و کار دارند؛ با خیال راحت می‌تونید حتی در حالت Airplane Mode به تمام داکیومنت‌هاتون دسترسی داشته باشید.
🔗
گیت‌هاب پروژه
🔗
وب‌سایت رسمی
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/ArchiveTell/7681" target="_blank">📅 13:49 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7680">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c846b7bad.mp4?token=snCFzFBmxuaICiZlzDnw7C-sPX0QAnIxK7cdDd_-6TUjPRwHzd0Sup4SrxX-OVKtORsX0spHaWvq8FuOQc-AnB3YqKfbPoMC2iUGogEG7uvM6sL6V6MaHKGcu2EvA4rN53J0Hq0DV5x0UCN2XpnwFvliZvMlp5Mi-fDby0I42VQoWiLW-U8-_6FcEYkPtbDs4_SMm605zMHoZbSRC5SOqUC6-7jnVMaJfIypiAgAc0tcpgAYcOR6if6M-RIuaagxXE00TT8vibJRjn8SDkLFJ2ZPDOnHcGTf--t_uJFildOUMZvrZkdCXYelYpT0jTXi-6DP28BX93SW6WIh3IeJgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c846b7bad.mp4?token=snCFzFBmxuaICiZlzDnw7C-sPX0QAnIxK7cdDd_-6TUjPRwHzd0Sup4SrxX-OVKtORsX0spHaWvq8FuOQc-AnB3YqKfbPoMC2iUGogEG7uvM6sL6V6MaHKGcu2EvA4rN53J0Hq0DV5x0UCN2XpnwFvliZvMlp5Mi-fDby0I42VQoWiLW-U8-_6FcEYkPtbDs4_SMm605zMHoZbSRC5SOqUC6-7jnVMaJfIypiAgAc0tcpgAYcOR6if6M-RIuaagxXE00TT8vibJRjn8SDkLFJ2ZPDOnHcGTf--t_uJFildOUMZvrZkdCXYelYpT0jTXi-6DP28BX93SW6WIh3IeJgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📍
با GeoSpy لوکیشن دقیق هر عکسی رو دربیار!
بچه‌ها اگه دنبال لوکیشن یه عکس رندومید یا اهل چالش‌های OSINT و ژئوگسرید، این هوش مصنوعی خوراکتونه. حتی اگه متادیتا (EXIF) پاک شده باشه، از روی خط‌کشی خیابون، گیاهان، معماری و تیر چراغ‌برق مختصات رو براتون پیدا می‌کنه.
🌎
جست‌وجوی جهانی (Global):
پیدا کردن چند تا از محتمل‌ترین کشورهای دنیا حتی از روی اسکرین‌شات یا عکس کراپ‌شده
🏙
مود شهری (City Search):
اگه شهر مشخص باشه، با عکس‌های خیابانی مچ می‌کنه و آدرس دقیق پلاک و خیابون رو میده
📸
تحلیل چند زاویه‌ای:
امکان آپلود تا ۴ عکس از یک لوکیشن برای بالا بردن نجومیِ دقتِ حدس
💡
نکته طلایی:
کیفیت عکس اصلاً مهم نیست؛ این ابزار حتی فرم شاخه درختا یا مدل آسفالت رو می‌فهمه! موقع ثبت‌نام اولیه هم یه سهمیه سرچ رایگان بهتون میده تا تستش کنید.
🔗
وب‌سایت ابزار
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/ArchiveTell/7680" target="_blank">📅 13:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7679">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R4yjj5cz1pPDWKvMImwm7whXU-cui8q-zi6kD1Nm4DX2UI7dUCANx_ypI0Lt5RQ2KNGZNg36DHIquJQ5Dx2SO4caUTa8d57Ntk1KDpKTNo1IA5ejtBSLLZmIvVpl1CLu3dIalTBtUTNLLznp_LTj7KRbB211853y0MLPu8j_ACmIEPOPl8M-rJwMw3CDzgIWE1dSe3vA2wEvEjsnmj32hgHdUt1h73BeDI6FdoAVr5lGhc9kOlr--f4dnAKfGau7xHJojd0uM-mTpcvFYn5sHW1bzf6PlQKkw04aQf1acTnqYLCKQ-qef812uko8KM--GiWvQBa8xuClFrk0aypqBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕸
با SpiderFoot ردپای دیجیتال هر چیزی رو توی اینترنت بیرون بکش!
بچه‌ها اگه تو حوزه امنیت، تست نفوذ یا اوسیانت (OSINT) کار می‌کنید، این ابزار دقیقاً خوراکتونه. اسپایدرفوت یه ابزار متن‌باز و بی‌رحمه که کل سطح وب رو شخم می‌زنه تا تمام ردپاهای دیجیتال و آسیب‌پذیری‌های یک هدف رو دربیاره.
🎯
تارگت‌های همه‌جانبه:
جست‌وجو بر اساس شماره تلفن، ایمیل، آیدی توییتر و تلگرام، نام، IP و دامنه‌ها
🤖
اسکن تمام‌خودکار:
جمع‌آوری آنی داده‌ها از بیش از ۱۰۰ منبع اطلاعاتی بدون نیاز به سرچ دستی
📊
نقشه ارتباطات بصری:
تحلیل داده‌ها و نمایش گراف‌های دیداری از اطلاعات لو رفته و پیوندهای مخفی
💡
نکته و اجرای سریع:
راحت‌ترین راه اجرا با داکره؛ کافیه دستور docker run -p 5001:5001 spiderfoot رو بزنید و پنل تحت وب رو باز کنید. (یادتون نره، فقط تست امنیتی قانونی و اهداف آموزشی!)
🔗
گیت‌هاب پروژه
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/ArchiveTell/7679" target="_blank">📅 13:33 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7678">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JsmJdAC8Q72zbZBqOJ6WaLt1JoxK038n3OdfvbgclmWadutYx09HYMXPkUt5MLgFivqVTzN48xKM9iIdA4iNpR7tBgQxeHybOmFQ_YxnCXF5sa41hJkdvLzlYjiGfydiuqf3U03_6L8EBAmiQzGNhMLMl_iJLAzdr2PMNKyZqgsST1nKvXEQyLFW2N68RSNnpmJ4ZKMzcX-a3IeZVt75VRxNCsyt9PHbnOVw2PwU3QF2kYYVG9cLgZ2-nRx9FaSJzPOzqNVi5MZE0NuYCuI06ZKYhPfwzxCvQCHY9EYBqrijqrkvryqxJf-3vybuVaq7O-R4a3PCChT_m38Wm7seMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توکن‌های نامحدود برای Claude Code با شاهکار مهندسان اسپاتیفای!
🚀
🧠
پلتفرم
Portal
مثل یک مدیر هوشمند عمل می‌کنه و با واگذاری وظایف ساده به مدل‌های ارزان‌تر، تا ۹۰٪ در مصرف منابع و توکن‌های هوش مصنوعی شما صرفه‌جویی می‌کنه!
🔥
🔺
تندخوانی با Gemini (bulk-reader):
فایل‌های حجیم و چند هزار خطی توسط Gemini 2.5 Flash آنالیز شده و فقط یه خلاصه مفید به Claude تحویل داده میشه.
🔺
کدنویس روتین (code-writer):
تولید کدهای استاندارد، تست‌ها و تنظیمات خسته‌کننده به مدل‌های کم‌هزینه سپرده میشه.
🔺
تمرکز روی کارهای حیاتی:
با این روش، Claude فقط درگیر کارهای پیچیده و استدلالی (مثل رفع باگ و طراحی معماری) میشه.
💡
در
نتیجه:
یک ترکیب هوشمندانه از چند مدل AI که باعث میشه هزینه‌های شما ۹۰ درصد کاهش پیدا کنه و خیالتون از بابت محدودیت توکن‌ها راحت باشه!
🔗
لینک دسترسی و پروژه
✈️
@ArchiveTell
|
#TOOLS
#AI</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/ArchiveTell/7678" target="_blank">📅 09:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7677">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ArchiveTel
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/7677" target="_blank">📅 00:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7676">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Amg_QX94P2k5HvtpDely_S-CDxtNeCsuFW2GjW9HFet4TpdFwCkHu7uG3UVlSGFTAZqRsz031rLrRKCNJKJ3-JY5ls6i19P2xN069CgFQYw8IwYo1evp4IWoiypk0yHkHGQrLlbL1EIxQV7moryGBvkfxQ5oF9Daf7rlkfpo-gbDMffKDPTxPnNeO9GQBsiCmhNxnkQ6uzBI2yig4Nc6utZX8C-TI2cC1yts6uA-C8zBUmpavgjuc-5c5_P8nxy9zsjXWR-ghTDGJFTvty5RmTgb1qKJR4weoueVXlFVg_ppz3txEBvANITI0deSwQ-6lICz9xa4KYxME5glYE_z0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت
یا کاملا رایگان باشه یا فریمیوم
با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم
اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/7676" target="_blank">📅 00:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7673">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mS-rK0XIV__3FewBioU7BZmdfxfCdvt_h3p-ztw9Tzx_POhar7UzYkCHa-b38ZgG5Xa4Ay3Aw4xMwBaxw8zJvyXSickubW_fERVGDQLpA9yfcpBXN-WD_CDjXoAXXt_v0Jd_jWB0gY-H2doLCNszyExgqs7GD02ZjRBHz-JSGLrqK3IUuzRXx9ho1krm4nhA-_VBD3T5On8PGClxW1SGLJnYcXMNI4c9lgb6mpUUeOzErNphA72d8oVeYkTxN6-gYkpu509trdemkUAlYVBclRDT_5za-U1MTglCzkKVAadb76042neAaUpj9xLTuUjczGUJQX7ZhlrQb7KVTE6pKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h2e1h_u0YubY_kJ4KObVm30y6jrwDPDEXIsswIkKO6NSzntm-L-iurXDTsM-0G-RmEdPNUVBxz176-_jiujXEAyFokOZQObmqATioXtRKJSq-SPIQmbKAtyrXv3prRgZ_S2-IDaoxMBhZk8_fvUwAmM4_EA0VB-ttSd9u5nKrNAZB_bqaC8JxKuzoOxKkDi6lbQRxcgEBErq0mkzRlT0bOqPMGh9yg8-pi_wN6xoB9FKJq23wruyfwFKyM_MG2PKxRL5bz54FbTP4lDAjJO4YgzrLvWzDDupQdGj1_J_3UEu7MrulmeUzHkbnDe0U1RQv6eG4BCUJW4hrhJzUlZcrA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📌
مدل GPT-6 Astra بازم یه حرکت دیگه ثبت کرد؛
بازی Portal رو تو 23 ساعت و 43 دقیقه تموم کرد!
مدل به طور خودکار شخصیت رو کنترل می‌کرد به طوریکه هوش مصنوعی یه تصمیم می‌گرفت، بازی متوقف می‌شد. GPT-6 Astra با استفاده از تصاویر، موقعیت شخصیت و زاویه دید دوربین، تصمیم می‌گرفت که چه اقدامی انجام بده. بعضی وقتا هم تصمیم گیری هاش تا چند دقیقه هم طول می‌کشید، اما در هر صورت تونست بازی رو به پایان برسونه.
🔥
این کارو آقای "cozyblaze" با کمک اشتراک ۲۰۰ دلاری Codex Pro انجام داد.
🔗
سورس پروژه
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/ArchiveTell/7673" target="_blank">📅 23:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7672">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h8TPFpEnvTxoriu8P6_9PV0RaeaGUbPxuYdJQ43GWVqzIX24OUv7EYQeOd4UivKS_WSZ8XFN8eOp1kzC9VmtpPmsE977mEzqjiixCsTmFKzBTP6-4mg_bQM1Kn-C1qOjgHW7q33Ax1IkAcUrmV3SnTP5rA0mRHrdEN3ag76L8QGZFnP1rNKcZ2njlrkqYdEod5wYngxly-KXh3N6oF-1lIpDb-UP2mxIBAFHWKn8IHgoNNq8TW_fnaSmZk3-KbZbuYfrNC9IHPvwqCK_XPwVzc763RbiV2yTVMmhFtK_ImA6LRQhhirI8VRwc_LMf3YgQL_HqVmsiufOqrNI1cSElA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جعبه‌ابزار همه‌کاره برای برنامه‌نویس‌ها با DevToys
💼
اگه خسته شدید از بس برای کارهای روزمره (مثل تبدیل JSON به YAML، تست RegEx یا دکود کردن JWT) مجبور شدید سایت‌های مختلف رو باز کنید،
DevToys
دقیقاً چاقوی سوئیسی شماست!
👍
🔧
بیش از ۳۰ ابزار کاربردی:
انواع کانورترها، انکودر/دکودرها (JWT، Base64، QR)، فرمترهای کد، هش‌ساز و فشرده‌ساز عکس.
📄
تشخیص هوشمند کلیپ‌بورد:
به محض کپی کردن متن، خودش می‌فهمه چیه و ابزار مناسبش رو پیشنهاد میده!
🛡
کاملاً آفلاین و امن:
تمام کارها روی سیستم خودتون انجام میشه و دیتای حساسی سمت سایت‌های ناشناس نمیره.
➕
پشتیبانی از اکستنشن:
میتونید ابزارهای دلخواهتون رو هم بهش اضافه کنید.
📌
لینک مخزن گیت‌هاب پروژه
✈️
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/ArchiveTell/7672" target="_blank">📅 23:22 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7671">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/ArchiveTell/7671" target="_blank">📅 20:54 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7670">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/786d6d3a9a.mp4?token=oJC7zb0z9DptsZmMq9-c8wEcedYG4kiXEAWmdeJfDidzQ4YtvFrQndr3hAiQW0hIV5N6tebvXs43H5nxhpKmYtruS17A6ts2_IdKaxnJVdmhOAHPX6dSqxq4iouwdy4dkDadWGMXXHMQzzWiJ21I67fGWKo01fqDCXOuw3aK29XUFl6R38aR2Tls9sF_aBthD4g8CwZPeIyExbxoqTOcYI0ia57wNL3ri_sNMrKLImQj6A3_v3FWofilFzBsJ0yy0E2HW3rG4cRsJUdhLmOt8j5NophZoKhJd66AcFc0k4w9Pxjqz0X-Ez_fBsBbZmcXjUyIsVtkf7SHRVNaoVwh7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/786d6d3a9a.mp4?token=oJC7zb0z9DptsZmMq9-c8wEcedYG4kiXEAWmdeJfDidzQ4YtvFrQndr3hAiQW0hIV5N6tebvXs43H5nxhpKmYtruS17A6ts2_IdKaxnJVdmhOAHPX6dSqxq4iouwdy4dkDadWGMXXHMQzzWiJ21I67fGWKo01fqDCXOuw3aK29XUFl6R38aR2Tls9sF_aBthD4g8CwZPeIyExbxoqTOcYI0ia57wNL3ri_sNMrKLImQj6A3_v3FWofilFzBsJ0yy0E2HW3rG4cRsJUdhLmOt8j5NophZoKhJd66AcFc0k4w9Pxjqz0X-Ez_fBsBbZmcXjUyIsVtkf7SHRVNaoVwh7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم 7 برنده خوش شانسمون
🎉
:
1.
@reza1629
2.
@mhti9
3.
@KIING_ZOG
4.
@Gogogrugo
5.
ＮＯＢＯＤＹ
( 6641463426 )
6.
@an_Y008
7.
@AshenOne2077
برای دریافت جایزه به دایرکت مراجعه کنید
✅
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/ArchiveTell/7670" target="_blank">📅 20:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7669">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">قرعه کشی اکانت Gemini Pro 18 ماهه
💥
🆓
برای شرکت در این قرعه کشی کافیه کلمه ArchiveTel رو توی کامنت های همین پست ارسال کنید
✅
هرچقدر تعداد بیشتری از شما مراحل زیر رو انجام بده تعداد اکانت های بیشتری برای قرعه کشی جمع میشه
👇
1️⃣
وارد این ربات رو استارت کنید…</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/7669" target="_blank">📅 20:00 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7668">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🥇
رکوردشکنی دوباره از GPT 6 Astra
خبر رسیده که GPT-6 Astra تونسته تمام ۴۸ مرحله بازی «I'm Not A Robot» سایت
Neal.fun
رو بدون غلط رد کنه ، خیلیا جوری جو دادن که انگار آخرالزمان امنیت سایبری رسیده!
😂
طبق معمول، ته این هایپ‌های رسانه‌ای خبری نیست. کپچاهای تصویری سال‌هاست که عملاً مرخص هستن و حتی مدل‌های پارسال هم با یه پردازش تصویر ساده دورشون می‌زدن.
سیستم‌های امنیتی واقعی وب الان با تحلیل رفتار موس، کوکی‌ها و الگوی کلیک کار می‌کنن، نه با ۴ تا عکس چراغ راهنمایی و خط‌کشی خیابون
😁
تست کن ببین رباتی یا نه ؟!
🧐
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/7668" target="_blank">📅 15:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7667">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oj5r6zRrhw_YOvYlZM-K1uLBxTNq7e_DR4rxns8iRZGUvmWF7cxnBSX99oaWUpUuGslvkVyE8FDFoa0ZSEKviPI55bQn5o8mJ3ZJCGz4Fbgb3HCFC9gCdFg6u6gnK_hDdDVPncoWmIHgu-P5V9PnwTMw2OMLx31975_ZcJvzQDQbqssIgxkCyNqEe86KYEY2TdENQh8zTmkTkfm_87gMtKOXdXHWPRluDZMsbY_l1AWhfPqIzHFK806tmPLr69vgwsq2f2fTAwKgnlT3208sg2VaeAZ2x1PkigNF0u5DiL3FvIWVHpOp_9O5KOsAh-cZcHEZR4Tdaj-LjOv3W-t11A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جداسازی صدای خواننده از موزیک با هوش مصنوعی؛ تمیز و بدون دردسر!
🎤
🎧
بچه‌ها اگه دنبال ساختن نسخه کارائوکه هستید یا می‌خواید صدای خواننده رو برای ریمیکس بردارید، ابزار آنلاین
AI Vocal Remover
دقیقاً همون چیزیه که لازم دارید! با استفاده از مدل‌های صوتی AI، وکال و ساز رو در چند ثانیه مثل آب خوردن از هم سوا می‌کنه.
✅
🔺
پشتیبانی از انواع فرمت‌ها:
هم فایل صوتی (MP3، WAV، FLAC، M4A و...) و هم فایل‌های ویدیویی (MP4، WebM) رو به راحتی قبول می‌کنه.
🔺
بدون نیاز به ثبت‌نام و کاملاً رایگان:
پردازش تماماً در کلاود انجام میشه، قبل دانلود می‌تونید آنلاین پیش‌نمایش رو گوش بدید و تا یک ساعت خروجی MP3 یا WAV بگیرید.
🔺
کیفیت و دقت بالا:
تفکیک دقیق لایه‌های صدا بدون نویز و افت کیفیت محسوس سازها.
💡
نکته:
برای آهنگسازها، تدوین‌گرهای ویدیو و یوتیوبرها برای برداشتن کپی‌رایت یا ساخت بیت‌های بی‌کلام، این ابزار سریع‌ترین میانبر بدون نصب نرم‌افزارهای سنگینه!
🔗
آدرس ابزار
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/7667" target="_blank">📅 14:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7666">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iy3UGGaJ3wZyDbnGzRNIc2BWM8KZpsmucy2xx0AfQLCzfMXnycc9XdAEGldKQkNcWjX_HzepD601GKAEO_lQ9rl0LoNgHZ0vn71-p73VGOtMXzZlmWsaEA6-FfrirVLxbgd2QHDSHIDJ7ElR1e5V5mXNv4hAnaN3w82f3x9cVXVKUXsmCFZU4oIJES_FsZTqaaTwACU7Uo71vhIzXfm1PKDRWxDt1_7KwJytvEs2YZ1vKRmUx7VYOHMcIf6F6bo7k5e0GB_mMPB7NgZJDyOsa0Hgz6Yajg4t093z6H0-Inbnsdl2DQXUtCmM-mla_-ZYuggpSdeW4qZXxg40KGgRCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبدیل گوشی اندرویدی به یک کامپیوتر دسکتاپ کامل با Android DEX!
🖥
📱
اگه از قابلیت محدود سامسونگ دکس خسته شدید یا گوشیتون اصلاً DeX نداره، این ابزار خوراکتونه! نرم‌افزار
Android DEX
با ترکیب جادویی ADB و موتور قدرتمند scrcpy، گوشی اندرویدی شما رو به یک سیستم‌عامل دسکتاپ واقعی با پنجره‌های شناور و کنترل کامل تبدیل می‌کنه.
🚀
🔺
تجربه دسکتاپ چندپنجره‌ای:
اجرای اپلیکیشن‌های اندروید در پنجره‌های تغییر سایزپذیر روی ویندوز، مک و لینوکس با اتصال باسیم یا بی‌سیم (Wi-Fi).
🔺
خوراک گیمرهای موبایل:
کی‌مپینگ حرفه‌ای کیبورد و ماوس، شبیه‌ساز جوی‌استیک WASD، قفل دید ۳۶۰ درجه شوتر (FPS Mouse Lock) و حتی شبیه‌سازی ژیروسکوپ!
🔺
دور زدن شناسایی امولاتور (No Ban):
چون بازی‌ها مستقیماً روی سخت‌افزار واقعی گوشی اجرا میشن، آنتی‌چیت بازی‌ها شما رو شبیه‌ساز تشخیص نمیده و بن نمی‌شید.
🔺
امکانات یکپارچه سیستم:
مدیریت اعلان‌ها، پخش صدا، انتقال فایل با درگ‌اند‌دراپ، رکورد صفحه و تعریف پروفایل‌های اختصاصی برای هر بازی.
💡
نحوه راه‌اندازی:
فقط کافیه گزینه USB Debugging (یا Wireless Debugging) رو توی Developer Options گوشیتون روشن کنید و برنامه رو اجرا کنید؛ بدون نیاز به روت!
🔗
گیت‌هاب پروژه
🔗
سایت پروژه
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/ArchiveTell/7666" target="_blank">📅 14:51 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7665">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qEwNkDpSbk_yeHTnzOse8kwbsmDEngap7_FF4Ka2nsBVEH065-DuQDsJR85HIsXkMHJJn0PhncSt-n35tKdluM_ZocLOu7KfkEPHum-zb-LiFZ5pCFKSKthdPkyPTr8Ui_telZLCV7GMRKjuL9UbGQAauHX2IlVCDSM5p3x5nCnNIhxQ1_EyGrHrBBRlq3tcP7FyVZ9eaI_HHJ3f5AtigTRAh242ymcoXFZWHBPW8TN9K1p8s85rYNoagiy-vG8NJD7RoH1Eicv6myBxXANq0namar7BsoXNJQa6U_-jgwUWr81M0diE7bPdKMU6eZwHUR6VxsWqzW_OZtjW6-UorQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معدن مقالات و دیتای آکادمیک اروپا؛ گنجینه‌ای که کمتر کسی می‌شناسه!
🎓
بچه‌ها اگه دنبال مقاله‌های خاص، دیتاست‌های خفن یا پژوهش‌های پروژه‌های اروپایی هستید که جای دیگه پیدا نمیشن، پلتفرم
OpenAIRE Explore
دقیقاً خوراکتونه! یه پایگاه عظیم با بیش از ۱۳۰ میلیون دیتای علمی دسته‌بندی‌شده و رایگان.
✨
🆓
🔺
آرشیو عظیم ۱۳۰ میلیونی:
دسترسی مستقیم به مقالات اوپن‌اکسس، دیتاست‌ها و حتی سورس‌کدهای پژوهشی پروژه‌های اروپایی.
🔺
بدون لاگین و کاملاً رایگان:
بدون دردسر ثبت‌نام، پی‌وال یا محدودیت دانلود، مستقیم به منابع معتبر دسترسی دارید.
🔺
ردیابی شبکه‌ای پژوهش‌ها:
می‌تونید خروجی‌های مختلف یک پروژه (مثلاً مقاله + دیتای خام + کد نرم‌افزاری) رو به‌صورت متصل به هم پیدا کنید.
💡
نکته طلایی:
برای پژوهشگرها، متخصصان هوش مصنوعی که دنبال دیتاست‌های تمیز و رسمی اروپا هستن، یا کسایی که دارن روی مقالات بین‌رشته‌ای کار می‌کنن، این ابزار مثل یک میانبر تمام‌عیار عمل می‌کنه!
🔗
وب‌سایت رسمی
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/ArchiveTell/7665" target="_blank">📅 14:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7664">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CB1BMDQrZNJoVRz5VMlUM6pI9kXVtotAfXmHFJLsj4aT7mQ1Vk9jeC5HNQMlDKLwqYGjYhJ0Rqgg6vvTfqVk2QjhrqJuUbyF5lY73mMtUwANGHGaAKKbVVLufwNQ3CxFEGYVqM315pTlIPmJgWbWzpGxluK4VVUexfEmG4g5h5aDT1OY98DxQ6foTP7A8Jk3YtlyDG4VJRDLkNd2c9JWUNtJor4N4RW6PBShuvAu80FgKm70h4zBS44A-EtkwrajMp2SNw7VOAJQKVwgeoyQyMK9WSEHd362aggRTS0maJXKB8Dp3ZxFHTel6ulRP632oQQkITKI9BRh9Potpr6heA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیبورد «شریک جرم»؛ قبل از ارسال پیام حواست به جریمه و حَبسش باشه!
🚨
بچه‌ها براتون یه پروژه به شدت سمی و دارک آوردم! این کیبورد اندرویدی اسمش «Соучастник» (هم‌دست / شریک جرم) هست و کارش اینه که موقع تایپ، متنتون رو آنالیز می‌کنه و آنلاین بهتون می‌گه ممکنه بابت این پیام چقدر جریمه بشید یا چند سال برید آب‌خنک بخورید!
😁
🔺
کاملاً لوکال و آفلاین:
نیازی به اینترنت نداره و داده‌ها از گوشی خارج نمیشن؛ با llama.cpp مدل جمع‌وجور Qwen3.5-0.8B رو آفلاین روی گوشی اجرا می‌کنه.
🔺
سیستم دوسطحی سریع:
اول با یه دیکشنری سریع کلمات حساس رو بررسی می‌کنه و بعد مدل هوش مصنوعی جرم یا تخلف بودن متن رو می‌سنجه.
🔺
پروژه کاملاً اوپن‌سورس:
کد و نحوه کارکردش روی گیت‌هاب قرار گرفته و برای گیک‌هایی که می‌خوان اجرای مدل سبک LLM داخل اپلیکیشن‌های اندرویدی رو یاد بگیرن عالیه.
💡
نکته:
هرچند قوانینش بر اساس مواد قانونی روسیه تنظیم شده، ولی معماری استفاده از مدل‌های فوق‌سبک لوکال برای پردازش آنی متن موقع تایپ، ایده به شدت خفن و قابل شخصی‌سازیه!
🔗
گیت‌هاب پروژه
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/ArchiveTell/7664" target="_blank">📅 14:38 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7662">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j5yPgJY7CuZ_ZY0dmyve-QX7aKfrT6QK77R7YXsQdyLnuOXun3VVJCwUG2VkhGWdiPdc97TcI7VjQqx0Y4Yt_D_VmPjZI1csVJotYuIKPYBW_1f6H7nP7rLsY0Bv3gN1ki4ATVue5VQzeBRfiL3Htj31etWoWYDW0sPDQrcPffKzdd8QoR9bvFVA0tH_gBmac7e1rofqibBuJQALitphfenXe0SB5cPg3tX9ALOGYs-u7ZRigLLpSACXoh1yI74MM6HCNuq04IoMdcOHL3LPhX_-rN0aaNNT2-F2uxafUuK7nD4x7Kp197Ur-InPtSv7KE6YRfVTkNICzBV4mSo3_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طراحی و ساخت اپلیکیشن با M3E Canvas
🛠
📱
پلتفرم
M3E Canvas
یه پلتفرم اوپن‌سورس و جدیده که بهتون اجازه می‌ده با درگ‌اند‌دراپ و کمک هوش مصنوعی، برای اندروید و وب رابط کاربری بسازید.
🔺
طراحی سریع:
المان‌های آماده رو می‌چینید، رنگ و فونت رو شخصی‌سازی می‌کنید و همونجا تو مرورگر تست می‌گیرید.
🔺
تولید پرامپت جادویی:
جذاب‌ترین ویژگیش اینه که در نهایت از طراحی شما، یه پرامپت دقیق می‌سازه که می‌تونید مستقیم بدید به ابزارهایی مثل Claude Code یا Codex تا براتون تمیز و بی‌نقص کدنویسیش کنن!
📌
لینک دانلود / گیت‌هاب پروژه
✈️
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7662" target="_blank">📅 22:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7661">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">قرعه کشی اکانت Gemini Pro 18 ماهه
💥
🆓
برای شرکت در این قرعه کشی کافیه کلمه ArchiveTel رو توی کامنت های همین پست ارسال کنید
✅
هرچقدر تعداد بیشتری از شما مراحل زیر رو انجام بده تعداد اکانت های بیشتری برای قرعه کشی جمع میشه
👇
1️⃣
وارد این ربات رو استارت کنید…</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7661" target="_blank">📅 19:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7659">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">قرعه کشی اکانت Gemini Pro 18 ماهه
💥
🆓
برای شرکت در این قرعه کشی کافیه کلمه
ArchiveTel
رو توی کامنت های همین پست ارسال کنید
✅
هرچقدر تعداد بیشتری از شما مراحل زیر رو انجام بده تعداد اکانت های بیشتری برای قرعه کشی جمع میشه
👇
1️⃣
وارد
این ربات
رو استارت کنید
2️⃣
در چنل ربات جوین بشید
3️⃣
با آیپی خوب ترجیحا آمریکا وارد دکمه بشید تا سایت باز بشه و دکمه وریفای رو بزنید
‼️
نکته :
در هر گوشی فقط 1 بار میشه اگه میخواید با یک گوشی تعداد بیشتری بزنید باید هربار کلون های تلگرام رو نصب کنید  ، هر 5 رفرال برابر با 1 اکانت هست ، تمامی کریدیت های جمع شده تبدیل به اکانت میشه و قرعه کشی میشه و لینک فعال‌سازی به شما داده میشه
‼️
شرایط : حتما باید در چنل آرشیوتل عضو باشید
تاریخ برگزاری ، فردا دوشنبه ساعت 20
🚀
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7659" target="_blank">📅 17:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7658">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTyerGS1keyGsWAEyOkvqrMMZ9koR0bTUCclTQOq18I1amOOAGHryphz52EmfnQDilWlFh913gLFOOIMdSsjcMJsHCxaInJF74IUz4-skDEPbifIoMsLjltn548GH7-u-9imy1UdT2Sxl-3-sK_AIHxRQDunlPUEHGiC2cxLe9X2F6hKj7e3M2DTtsm6lksYcR8JKrEoAvK-qVuleK0EdpLHnApsGtgpf_mfzRhc1_WPFG2Ok5AJyCb28pBhQRfUGy5tiXvgnVm0M29lnCG_5_hZB7LqLvpRUsjx-Ftfs3t2brhzzSzwOpL7zd6lEp3jcJuDWk5eQvvQxTPbACW72w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API هوش مصنوعی ها
💥
🆓
DeepSeek-V4-Flash-Vision-Exp | DeepSeek-V4-Flash-0731 | Qwen3.8-Flash-Next
✅
این سایت ثبت نامش کمی آزاردهنده هست بخاطر UI بدی که داره ، باید با گیتهاب لاگین کنید بعدش میره تو داشبورد و به ایمیلتون کد میفرسته و اون کد رو توی مراحل وریفای وارد کنید ( شماره تلفن لازم نیست ) حالا بگردید عقب و از سایت API دریافت کنید
✅
هر روز این سایت 1 PTS بهتون میده که معادل 10 دلار هست و خیلی زیاده برای این مدل ها
🚀
محدودیت هم هست 20 درخواست در دقیقه
‼️
📌
Base URL :
https://developer.amd.com.cn/radeon/api/v1
🔗
لینک سایت
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7658" target="_blank">📅 14:55 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7657">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">دسترسی به Deepseek V4 Flash به صورت نامحدود و رایگان
💥
🆓
به مدت محدود در این سایت این مدل به صورت کاملا رایگان و بی محدودیت درخواست قابل استفاده هست
✅
📌
Base URL : https://api.b.ai/v1
📌
Model ID : deepseek-v4-flash
🔗
لینک ثبت نام
🔗
لینک بخش گرفتن کلید …</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/7657" target="_blank">📅 14:37 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7656">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DqaiZ1H5I-_UeNImJbS-_H6MKvp6G2btgLVtZ7SKfdGKQrKWBPvvXbVxBEBwN29QYlCbONGsTP6LpNlJa9XX9wvd1J9yj5HE0dyoSWfwc8lTgK245FNuCtBOCnItC0FMWYkBoE0ZwqmOaPpJ1mZl3TZr9DSTKJ6qtL97MPFPN-Qm1inRTmRCHhMihUZ670JYxvnEuG4OPPDuPNLzn-ybuigqTAHi97ssleNOl6Drg4oS476c6BE0fbPqjmEDSw7xipbS41HvuKIaJczOJtGJ7icwidKrJxFwX-w7-hVW1i5XiqVhywH8S3K81zNVx8OgHjNgMmmg7FtQAtFaSEJ8lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به هوش منصوعی های محبوب
💥
🆓
Opus 5 | GLM 5.3 Flash | Deepseek V4 Flash | GLM 5.3 Flash
✅
4 میلیون توکن میده که میتونید استفاده کنید از API هر روز هم ۱ میلیون توکن میده برای opus 5 ( حد مصرف روزانه هر مدل ۱ میلیون توکن هست )
📌
Base URL :
https://helyxai.space/v1
🔗
لینک ثبت نام
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7656" target="_blank">📅 14:08 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7655">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I6XISLwhvhU0nDGfgxMUvm9IHK96yaYAzoQRuyGqoPdV3H2kfj_ClNu9XxAz9aKUWRMQVo50GViAgg7Yt8vX0M_kqpIIRJsij7MQ97GLO7qGAQ24m6iqRUZvxclRVk7lec8PN1SXx_u7kbEkxpjGOh-ksAH9ADWGXlZr92dlv3Mj8Epv1h5wFIT338zTnTSvlDnvxNmoyR4JtfnXWtfoUDKtPE5QdE1wF3c_owzbecxDt3DsapjaYRZfqRVI1Hj7W6nWBAuxrzKYnblRoo_ok7WIeJ5k79o7jnYinvoPFE7NlzQLj-TxIbKFsJ4MRvTYS9wm8ddlfOuLBWpzDHxdIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش گرفتن ایمیل دانشجویی رایگان
💥
🆓
کلی از سایتا همیشه به دانشجو ها تخفیف هایی قائل شدن یا چیزای رایگان دادن مثل گوگل که واسه وریفای یک ایمیل دانشجویی میخوان
✨
‏اینم لیست مزایایی که داره:  ‏• جمنای: ۱ سال رایگان  ‏• چت‌جی‌پی‌تی: ۴ ماه اشتراک ویژه  ‏• جت‌برینز:…</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7655" target="_blank">📅 11:08 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7654">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">آموزش گرفتن ایمیل دانشجویی رایگان
💥
🆓
کلی از سایتا همیشه به دانشجو ها تخفیف هایی قائل شدن یا چیزای رایگان دادن مثل گوگل که واسه وریفای یک ایمیل دانشجویی میخوان
✨
‏
اینم لیست مزایایی که داره:
‏• جمنای: ۱ سال رایگان
‏• چت‌جی‌پی‌تی: ۴ ماه اشتراک ویژه
‏• جت‌برینز: ۵ سال استفاده از تمام ‌IDE⁩ها
‏• گیت‌هاب: پکیج کامل توسعه‌دهندگان
‏• آفیس ۳۶۵: نسخه کامل ورد، اکسل، پاورپوینت و تیمز
‏• فیگما: نسخه حرفه‌ای مادام‌العمر
‏• نوشن: اکانت پرمیوم مادام‌العمر
‏
برای دیدن آموزش کلیک کن
✅
✈️
@ArchiveTell
|
#METHOD</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7654" target="_blank">📅 10:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7653">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lFCFy_lfJgo9X4t1EM7vUWbEf-Pa7V9zlOVYrSCJ6V4Bf416dCekF25Dkp8o4GcxqdewAHZOrwGJlcJnZwaPs6AHb53j-UQIbDuNg6TOLcyXCL_qqvbc7eiMpAamxIc3MnGLlQ8NfheEv2ZxwCsPKRqe0WTd95u9dVfIq3dBZAWFfjxXxLSR-Je68Dkdd64Sd7QpIhGqFKnkz-_ma4NzcVvGn3llnm72DbW_SCRTELQaS9RLvMps7agP7vnNbLdJNZrWfxf_OJ-jjdcPN_e_1aImbduhKwOi-x0IVRFOM5K3RhAYUU_ojFyczwERdZ9hixCYLlC1OV_Rby3FTY7jfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
داستان GPT-6 چیه؟ انقلاب هوش مصنوعی یا فقط شوآف تبلیغاتی؟
🤔
این روزها همه جا پر شده از اخبار رکوردشکنی GPT-6 Astra و نمره عجیب ۹۹.۹٪ در بنچمارک ARC-AGI-3.
طبق بررسی‌هایی که کردم، این نتیجه تو شرایط کاملاً ایزوله و خاص ثبت شده و توسط منابع مستقل تایید نشده.
قیمت‌گذاریش هم به شدت نجومیه؛ هر یک میلیون توکن ورودی ۱۰ دلار، و خروجی ۵۰ دلارِ ناقابل
😁
(مقایسه کنین با جمینای ۳.۸ که ۳.۷۵ دلاره)
در ازای این هزینه سرسام‌آور، وقتی در کل حساب کنید، برتری خاصی نسبت به رقبای خودش مثل Fable 5 نداره.
یکی از معدود بنچمارک‌هایی که هنوز اشباع نشده و به نظرم بهترین معیار برای ارزیابی مدل‌هاست، بنچمارک Humanity's Last Exam عه
تو این تست، عسترا نمره ۵۷٪ رو ثبت کرده؛ در حالی که Fable 5 با قیمتی مشابه و حتی پایین تر، نمره‌ش نزدیک به ۵۸٪ عه
🔥
با دیدن همین آمار میشه گفت OpenAI با این Gimmick های تبلیغاتی، رسماً داره به شعور کاربراش توهین می‌کنه
😐
من حتی کاربرشم نیستم ولی باز به شعورم توهین شد
#طهلیل_ai
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7653" target="_blank">📅 23:46 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7652">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nGpGGyKHfwRRWQHVPHxAPVL3GZiOWbZe9wsE7DYfVoErSugebrYfxYYTjGmi_8_hm5tJ4deiS-RS9OVEuVtPbVfh0o6diV1DQfOnzqfkgvzD4fvtWeuAGPXfEFpWo6rTkTiqNCvGFNhpK8vYJYW4PPbDxxs4bWvHBZlbmPt9zoTWNX5S_l_DyHmApm6BRhFt2LbBtrWZ1FfBj0sHzdj18uNtNvaCkfQkz_GpNJ5rkfrZY7IKyVMm1JD3dENsozW7c2r0bGmSM5Y3dtwOnIbORWg8A5Fg1LyHJ2_4KDCysFZlPrV4vHDUiEFC0rZdaCC2oQYXyX2GtKCTW_ZXc9iqSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Free 2k$ model GPT
💵
📌
Base URL:
https://vip.9aws.net/v1
📌
API KEY: sk-g926rIr0SG7pfoD4WextkZwRRAgFOwYZDsG5hnDr8mL2ZH9d
📌
Models:
gpt-5.5
gpt-5.6-sol
gpt-6-astra
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7652" target="_blank">📅 22:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7651">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bfwOw8Za8t0PtIPsVDouVPtO802aJSriz_dwK1SC243v0i1ik572isitRXcfvx795PTZLocxcu4_s4jNABGj2iZW_UX2VwjmVfRhOYISpBRN4MyfxwuAfEwZyLjuFMxg-pIejIyQsDjrmNPx-Hc70HgDM9F9BWsrv4d6MlX8FJ-R2-Mm5pEYTQ6CTjQmJ-4Uu-FTDhmpPLNAgg1lGO5svjTXwT_kjeqn9rd0EojR2Ua0T6d363hMKUmZjacJQIs5kv1gpc76Dpgl2_D47chxtsYwzyn7sVfQxtD2_KtcT3eoroG4r3tB-DD-ARguG3BJFmDvcHXVuFJt6CuhhQTtYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی آزمایشی رایگان به مدل‌های پیشرفته هوش مصنوعی
💥
🆓
Opus 5 | GPT 6 Astra
✅
سایت ClickUp فقط یک ابزار مدیریت پروژه نیست؛ ClickUp Brain حالا امکان استفاده از مدل‌های مختلف هوش مصنوعی را در محیط کاری ClickUp فراهم می‌کند. طبق مستندات رسمی، مدل‌های OpenAI، Claude و Gemini در Brain قابل انتخاب هستند و می‌توان بین مدل‌ها حتی در یک گفت‌وگو جابه‌جا شد.
🚀
🎁
سهمیه رایگان
در پلن Free Forever، نسخه آزمایشی Brain شامل ۲۵ استفاده برای هر Workspace تا ۱۰ نفر است. در Workspace های بیش از ۱۰ نفر، این مقدار ۵۰ استفاده است.
✨
⚠️
این سهمیه ریست نمی‌شود و پس از مصرف، برای استفاده گسترده‌تر باید پلن/افزونه پولی تهیه شود.
🤖
حالت Agent هم دارد؟ بله!
دارای دو نوع Agent است:
• Super Agents برای انجام کارهای چندمرحله‌ای، تحقیق، کار با اطلاعات
Workspace و اجرای workflow ها
• Autopilot Agents برای انجام خودکار اقدامات بر اساس trigger و شرایط مشخص
💡
علاوه بر چت معمولی، Brain می‌تواند روی فایل‌ها و اطلاعات Workspace کار کند، جست‌وجو و تحقیق انجام دهد و حتی Task، Doc، گزارش، اسلاید و موارد دیگر ایجاد کند.
🔗
لینک وب سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/7651" target="_blank">📅 22:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7650">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uiJJq1ZrCBwtZQHk7Nwrb34zglqRSu7kL3e9kDG78eImnFbqZoCOBN1Dh2qrrBaGDBx6YBrDsPbt2j_JRE7KGeHT0jIny1dLe1MGvEBDCITlsEDOdq6JdB5W7JubJr3A2znCZcejQ0AVcrbuOJuByr7IKkl1xwqrVTorY7SDBcn6LFoDAklXmelBnh5IZCI5fjTD9no8n_cjn6sz_yYs6wtbwEjOpsw4CYqUfFi-xa2Ph8IxTxcNk37dxTEPNBrnD8D_b0X4VyHMrXSh6P59IBZrXGZ2v9d47xB3GpQgesrHgTscPA7Bn7gTkw92749gJZMur6jbZgDMR7bJYwHULg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API مدل های هوش منصوعی
🚀
🆓
Opus 5 | Grok 4.6 | Deepseek V4 Flash
✅
برید تو سایت زیر ثبت نام کنید و موقع گرفتن api باید گروه Free رو انتخاب کنید از این گروه این سه مدل بالا رو تست کردم جواب دادن ، بقیه چیزای خوبش کار نکردن این مدل ها رایگان هستن و کریدیت نمی‌خوان
✅
📌
Base URL :
https://kiosapi.com/v1
اینم کلید خودمه اگه دوست داشتید میتونید تست کنید ریت لیمیتش رو نمیدونم
📌
Keys :
sk-ZoCd9hc91if9INutCoTC6zA0wJ2pbrd9a75GQJTyj5V4gIup
🔗
https://kiosapi.com
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/7650" target="_blank">📅 22:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7649">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r1FnAf81wopLz7XkMaG7ODu3XdmpkyAiYoNEYMYWoYfNbjs8cSPpuL-MmgMalnBPPsJi_AVHE3XFz1gdTaBJpdukb1pbi4zWWEH4R3YjgcxjXQaCv49I6E1NfLDf7olyp_yKaxfx_nU9i0UzDXkGZ6tPQnGhnChhtqleCRsgZpJIkK0FbVXlpUkBdn3gLooF-wD1PThj58ZdNfalQ1G8v6vY_Te-oGJIZH9s8uHoUn0LoAg9qYXE9cFKy4215Wysa0FEpJDOXtooF4_satd_9zZmo6zDGs26n2vvZb9S-O7QXJBByQFQhok2iRcr9jUbWKikkPIlQ2Y2ucRniyFPmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5000
دلار
😎
📌
Base URL :
https://vip.9aws.net/v1
📌
Keys : sk-faNuu4uK9WqIYAiXjdmYxeX6PI1Z5wNLzCsIXKbKVQ67W1rG
📌
Model ID : claude-opus-5
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7649" target="_blank">📅 17:35 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7648">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qi2jWeTOmMBYCcpxM8P8V-B6iIoa2w0FjlwO1m78RCZTcX0X1glL1DWfVCIHd5NTbUp7Y3S4ZESxKCDSxG-9Ct57OeOMbGvcisA9NNyTJj52dYU35ObCsnPlKQUb601QYxSBh_8pfDlOP_xRoHknO3zh3CTcELv8Nz5jIBydDTCx7eDmVGXXxq7omtVVsrw7dd75KQIZXjq87QsbrhSFEczgdEb-qu01ZKrz3DWuF9YCq23TU6aSftqRum3UpyKVHAkIVrhNZkZF2OZqXxz0F2d_WtJSULKwOwgQ9_AQxiB61E-GyVJMO3tjQOJCkuA36aLLl_DnlpDZH4yDH7Hcng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
ساخت وبسایت ۱۰۰٪ رایگان، فقط با یک کلیک!
​سایت شخصی یا پورتفولیو می‌خوای اما حوصله خرید هاست و دردسر کانفیگ رو نداری؟ این پلتفرم اوپن‌سورس رو دقیقاً برای همین ساختم.
​
🔥
چرا ZeroWeb؟
​
💰
بدون هزینه هاست: کاملاً رایگان و مادام‌العمر روی سرورهای کلودفلر.
​
🤖
مدیریت با تلگرام: پیام‌های فرم تماس سایت مستقیم میاد تو تلگرامت و همونجا جواب میدی میاد تو سایت.
​
⚡️
نصب با یک کلیک: فقط روی deploy.bat دابل‌کلیک کن، تو ۱ دقیقه سایتت بالاست.
​کدها و آموزش کاملش رو تو گیت‌هاب گذاشتم. همین الان دانلود کن و سایتت رو بساز
👇
​
🔗
https://github.com/faithsaly5-stack/ZeroWeb
​
⭐️
خوشتون اومد استار بدین
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/7648" target="_blank">📅 17:21 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7647">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yx3iYXKWXKEwWQWsayOYP-pJaXrz05ozIMWCMGI8qu2ZYhqzBvaXs3xxxrn_nlF0CVUWajhAn-o5VfcJQ1D7bsFr6ZYr0lZvAsGJZArVq9dV_0hvGMumRTdfmAkgmeBo-egTh6hh8B6ClbiaypGZDHF3oM3l7aMN5EUnU0ihS7XgaI4Zedyr4kXTGxYlMoRC7xUQvZqU_xajZ4fXsIvaP5A6IZPtX8kM8k0CI8qx8VG1dz8ENQpUNFZERWg_fToF_e-QaOb5PfJz-3xWi1YgctxJLFOUP6FDqv15Y-PpCKiJOKMS8VIejWfirgtGGopQwoyx0puR378UTxtvlYcMzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل GLM-5.3-Flash به صورت رایگان
💥
🆓
شرکت z.ai کمپین Global Build رو تو اپلیکیشن ZCode راه انداخته — از ۳ تا ۱۸ سپتامبر
🌎
⏰
دسترسی روزانه: ۱۰ ساعت ،  به وقت تهران: ۱۸:۳۰ تا ۰۴:۳۰
👑
کاربران Coding Plan: هر روز، تمام ۱۵ روز، رایگان و کامل
🥚
کاربران جدید…</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/7647" target="_blank">📅 15:17 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7645">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rRM9YXpoS33lP6WD9ibGbO1tRCCBpg6fgEFZr83IS3uTeinNXFjD1VXb4C_KdMmacHOf_lHRiy6XnPzoHWJBEjrZt1bCa0siXrTwkZhMz2xmqHlg74uALR59YTVZN6V2ZNzhORLD9mdBTSvD8KqfsWb2TRPM6yddEfVldaCMSJKzol3EuJPJbQX2zFvn4nTnEWZrId5A9xyA5gmZLUo91atrcE7jv18m2ilBe8N1hRNeo8L8Q2alQdDIF5pt6Xzibe9_IC1gXQPNu34e47M_5uwsPux0z40bcugsOt0BktSwv1KhFd-ozsDARjgcpw9yjZpCaX_sWrnmZ7TJIhn0Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">1,000 دلار
😎
💵
📌
Keys :
sk-ByTi6xCfB7Pt1N8Hp9z7VdsRwGIMM5pdnh4CsorUfflysvbq
📌
Base URL :
https://tabitoken.com/v1
📌
Model ID :
claude-opus-5
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7645" target="_blank">📅 14:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7644">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cwHLd_5-dT8GGk43lFIOApbcnVpNDLPqoh-vkuBf-RMvpsXOf0csl7RFapM4MTRj19p35oMhgXlAWddtUswDfe7Yu8NAcFdTGSyhTSMTTbmf0Yy3BmqBxkB1tL1T-LcEogTw0Pnpz7yr_nCp6ydPYe5b7Ox7LAKpHZyyVdrs9pyeR5V1TzqZbQeZ3tjRU7gUASi8R122ef5Jlm7-VtWwo-0DjoLN0G3SaofTtKkp3eAhGEBK7ewOfADXvxUp7XzJE76SOzuAAK1KSebN4dPDBxJF02lc4hBSeH2rdUvxjVXY3AO--JIjZNpY2TxpJaCr2tUvwq7Jl-7VItPq6x_7ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏دسترسی به مدل‌های زیر در ترمینال به‌صورت رایگان
🚀
‌GLM 5.2⁩ | ‌Deepseek V4 Flash 0731⁩ | ‌Step 3.7 Flash⁩ | ‌Laguna S 2.1⁩  ‏وارد سایت ‌Cline⁩ بشید، با یک آیپی مناسب حساب بسازید؛ اگه شماره خواست، از سایت‌های شماره مجازی رایگان استفاده کنید. مانند این سایت…</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/7644" target="_blank">📅 13:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7643">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLVjJdLqBnGqHrPssngUVGyXROcupNmRDpfJjQivGKZ0iQlw2e_M9nLKTnhG2lRGXL0Rixzx8AslRif97x2bsmDs8VuGjRacZlM9HILvOsk6q4vKo1CiXP7P-yOEYwH3mwKMuaDebJ-nwWR0lIKx_gmGDNOsKGoNDGntx-AyjScOsnN1IlK97gHPEEJ4ZsB_0L6eGPgBRAA_lioYZrgGv8WV1Cj97BtMQFzEq2rn_azEzSukbKLJhJHVyKuyMe1OY84X_Sk8LYAYmqSpJhVGXOlRQFg9y84LmlbZW8w7xqz19ULbCmhroPwK-Q3GKudBy7OKGeJGUaqj0Muf_YDEhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت هم به دلایل نامعلومی میاد API مدل های Fable 5.1 و GPT 6 Astra رو میده ایشالا که خیره
📌
Base URL :
https://api.experientiallabs.ai/v1
ماهانه 5 دلار میده و همچنین فکرکنم Fable و Astra کلا رایگانه
تست کردم اوکی بود
🔗
لینک سایت
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7643" target="_blank">📅 11:59 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7642">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TsjNNdPrx4Hv0jEH5L0s5LcA003b_3LGdn_NEWGEIKDp4vnhK9_3R99NHTJtNS92qqkg8wF_vufHmjIe5PHCHCF9KNYmB0vfhPaU-2DjHRKIta1Sxftt7V8_6muK14OE8wDlh4HN6QCrp1olGesjQly6JnJ84lbn95U5jAp_8agNN50GofO-0pnF8McTNoYIPCb7-C0qOE919BvcTX9iI5pqGSmGq_adRIwfgYAnlvTZ2LaLyZEKr5kPb7MCKnUHYZbCj0NxICfXj__C6ixPeaANIJ9uy42ij4JDyGFlMIYw_zxE633mJRcK8RTaxgTUiFKlOIL-iGr7CiBrqkiEVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
Anthropic از Claude Fable 5 رونمایی کرد  شرکت Anthropic به‌تازگی مدل جدید Claude Fable 5 را معرفی کرده؛ اولین مدل عمومی از کلاس جدید Mythos که برای انجام وظایف پیچیده، پروژه‌های طولانی‌مدت و جریان‌های کاری خودکار طراحی شده است.
✨
مهم‌ترین ویژگی‌ها:  • عملکرد…</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7642" target="_blank">📅 11:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7639">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d39922c53.mp4?token=mHT1xY3olxotqRrr6YUVRiny78SSRiGVXDiwuIjC7zvFNdD6PWykCHCql7LQV3wFwdyKZszwN6dBSvjoNtAZ6J6qlrID0utk-A_CF46uOyVP0MitP259n6O1lnf6sL2mPrxtvloMVKTEWGeqY33igyN9VVzHUpBXQLoRrPiIS8fDjoCJO12zipwsFrQfsbFW125lN8Sk-Fn41EzmXDJ8mjxVorzqimJIszQkHs_Uwn-Ia5gHglXQBXQGjIUsMhxWqd7x3MTAm3yMzJCuC19zYe0gMiEll3iaAB5rWg5Kq9cM4cpgue7FxrMGYQZJvJQaPC1WXwxLOHnbVqk_aUDPXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d39922c53.mp4?token=mHT1xY3olxotqRrr6YUVRiny78SSRiGVXDiwuIjC7zvFNdD6PWykCHCql7LQV3wFwdyKZszwN6dBSvjoNtAZ6J6qlrID0utk-A_CF46uOyVP0MitP259n6O1lnf6sL2mPrxtvloMVKTEWGeqY33igyN9VVzHUpBXQLoRrPiIS8fDjoCJO12zipwsFrQfsbFW125lN8Sk-Fn41EzmXDJ8mjxVorzqimJIszQkHs_Uwn-Ia5gHglXQBXQGjIUsMhxWqd7x3MTAm3yMzJCuC19zYe0gMiEll3iaAB5rWg5Kq9cM4cpgue7FxrMGYQZJvJQaPC1WXwxLOHnbVqk_aUDPXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هوش مصنوعی حالا می‌تونه با YouTube کار کنه!
یک قابلیت جدید به نام youtube-skills به ایجنت‌های هوش مصنوعی اجازه می‌ده فراتر از باز کردن ساده‌ی ویدیوها، مستقیماً با محتوای YouTube کار کنن.
🤖
🚀
قابلیت‌های اصلی:
🔺
استخراج ترنسکریپت کامل ویدیو همراه با تایم‌کدهای دقیق
🔺
جست‌وجوی ویدیو بر اساس موضوع و پیمایش کانال‌ها
🔺
دسترسی به ویدیوهای جدید و محتوای پلی‌لیست‌ها
🔺
دانلود زیرنویس‌ها
🔺
پردازش گسترده‌ی محتوا؛ از جمع‌آوری ترنسکریپت‌های یک کانال یا پلی‌لیست گرفته تا تحلیل چندین ویدیو
🔺
امکان انجام تحقیقات عمیق با بررسی هم‌زمان چند ویدیو درباره یک موضوع
📊
یعنی ایجنت می‌تونه ویدیوهای مختلف رو جمع‌آوری کنه، متن اون‌ها رو استخراج کنه و برای تحقیق و تحلیل از محتوای YouTube استفاده کنه.
⚡️
مناسب برای ساخت AI Agent، تحقیق، جمع‌آوری اطلاعات و تحلیل خودکار محتوای YouTube.
🔗
لینک مخزن گیتهاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7639" target="_blank">📅 21:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7637">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WrO2qTCx29al7qCjuuWEfj6hhMweytwaU_4nOgwUseV2uBgj6cnocyuupAXcchhPbw_4EKBm1_JIiut0WV07YM2DmB8GYjnq9TPofsIzzdJ9ZFLSGJmV6PIOHs19vwnAk6yyJSbs-tH6fr3Ytku9v2z3GQBT2E5TvIQU4pglXQito-u8M9Gc8sHXetCfGSE1W_E1thtNq4WHkv_SvXMSHmQy86whSmO4fvjfvcWGgEendL6Xd8mx5-LvIr6iWs12NrXsja491VEtuN_06DFzYj00kGtP4ID9_oyxdF-GrwEmJFk97izZKHuByrw8WMB94lhc6OQQrRzd8pEEBQLWlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">200 دلار برای دسترسی به مدل‌های هوش مصنوعی محبوب
💥
🆓
Kimi K3 | Deepseek V4 Pro | Deepseek V4 Flash | Sonnet 4.6 | Haiku 4.5 | GPT OSS 120B
✅
کافیه با جیمیل ثبت نام کنید و یک کلید API دریافت کنید تا 100 دلار دریافت کنید
✅
📌
Base URL :
https://api.you.com/v1
📌
Example Model ID :
kimi-k3
حالا برید بخش تکمیل پروفایل و یک ایمیل با دامنه ناشناخته وارد کنید
مثلا تمپ میل
سپس 100 دلار اضافه دریافت کنید
😎
🔗
لینک سایت
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/7637" target="_blank">📅 20:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7636">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🎯
چالشی بزرگ برای وایب کدر ها به همراه جایزه
اون لحظه‌ای که به یه دایره چرخان خیره شدی و منتظر جواب هوش مصنوعی موندی؟ Commons میگه این وضعیت روزانه
۳۰ میلیون ساعت
از وقت آدم‌ها رو می‌بلعه و حالا با پول جدی می‌خواد حلش کنه.
😎
💵
🎮
چالش چیه؟
به‌جای یه پروژه‌ی کلی «چیزی با AI بساز»، این‌بار هدف مشخصه: زمان انتظار برای پاسخ هوش مصنوعی رو به یه تجربه‌ی سرگرم‌کننده تبدیل کن. یه بازی کوچیک، یه تجسم تعاملی، یا هر ایده‌ی تازه‌ای که به ذهنت می‌رسه.
🚀
⚖️
داوری روی زیبایی کد نیست؛ روی کیفیت خود تجربه‌ی انتظار، اصالت ایده، ارتباطش با AI، قابلیت استفاده‌ی دوباره و کیفیت اجرا تمرکز داره.
💰
جوایز:
🥇
نفر اول → 20000$
🥈
نفر دوم → 8000$
🥉
نفر سوم → 4000$
🏅
رتبه‌های ۴ تا ۱۹ → هرکدوم 500$
🔐
+ 20000$ جدا برای بخش ویژه
📌
مراحل شرکت:
ثبت‌نام تو
commonsmade.com
← بخش Hackathons ← Join the hackathon ← ساخت پروژه تو بخش Code ← وقتی آماده شد Publish کن و تو Hackathons ارسالش کن
✅
🗓
مهلت: ۱۷ سپتامبر | کاملا رایگان
اگه مدت‌هاست دنبال بهونه‌ای برای یه پروژه‌ی وایب کدینگ بودی، این هم خلاصه‌ی مشخص داره، هم جای خالی تو نمونه‌کارت رو پر می‌کنه، هم یه جایزه‌ی جدیه
✨
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7636" target="_blank">📅 19:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7635">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mWL92XQV9sI1vL96fLOjHyFmsD6wMvIMlNidxsPpv8mRWZiXjnIPqFlPYHHjHu0nb726jdK_H-z8NPspu8tzYtgSPFyLZyLofXSnq1Slye3DafCs2yRuEy5GuO7IebfjaHR2eBwVMcYyO67pMidlRRUefNalCnL9fh88_e9gE7vFaqYSIoTsZrvR_qlvX9dgyu4zFcsgf2RiINYaVPbFezRWZu-qimW76dB5MvyeKP3gZRDoPrVMQQBnzkqwRtYImcrOedPBXEHT2Vc0eJmFnMIzUs2QDhc8ow43wT4y3eZFqVXOoYmtdxo6JOSoQiJEv67iTaHI__X-Qrqm-l6d4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل GLM-5.3-Flash به صورت رایگان
💥
🆓
شرکت
z.ai
کمپین Global Build رو تو اپلیکیشن ZCode راه انداخته — از ۳ تا ۱۸ سپتامبر
🌎
⏰
دسترسی روزانه:
۱۰ ساعت ،  به وقت تهران: ۱۸:۳۰ تا ۰۴:۳۰
👑
کاربران Coding Plan:
هر روز، تمام ۱۵ روز، رایگان و کامل
🥚
کاربران جدید عادی
: یک‌بار ۱۰۰ میلیون توکن رایگان موقع ثبت‌نام (تا پایان کمپین باید مصرف بشه ، با اکانت جدید ثبت نام کنید )
⚠️
توکن‌های رایگان فقط داخل خود اپ ZCode کار می‌کنن، نه از طریق API.
🔗
لینک سایت
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/7635" target="_blank">📅 18:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7634">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f17211673d.mp4?token=kweTrsCaMXqHOpIutb74mo3dk4OUD44eZlP6LsAWghPPgDp3ifVmWAVNAo1TLLbYExM_D3NYO5pF23_S9BbjNIOHUr8X0D0TREGlQM_cxcNQdnOV65NhYRSGXr_Y5fKEq_ijbs7i_oAUQ2k_WfCh7xJP4Gkd3-CUhCiA1i200VyeiwAmXlV2hq8uhAgUyz2YohZzIml-gwObSC1xl7rgHf3_3d271e_3ourXj4Y6fCpKOg3dDnhoRfk8ClXM2pNMv0IbfrHJujG6mDY3FQ_G6ZMtT1UWcqLL0vtMpV8BhdZl10uqlA74RO8LiLbLhHEbbBIEK9qI8iV51UfgVQl65w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f17211673d.mp4?token=kweTrsCaMXqHOpIutb74mo3dk4OUD44eZlP6LsAWghPPgDp3ifVmWAVNAo1TLLbYExM_D3NYO5pF23_S9BbjNIOHUr8X0D0TREGlQM_cxcNQdnOV65NhYRSGXr_Y5fKEq_ijbs7i_oAUQ2k_WfCh7xJP4Gkd3-CUhCiA1i200VyeiwAmXlV2hq8uhAgUyz2YohZzIml-gwObSC1xl7rgHf3_3d271e_3ourXj4Y6fCpKOg3dDnhoRfk8ClXM2pNMv0IbfrHJujG6mDY3FQ_G6ZMtT1UWcqLL0vtMpV8BhdZl10uqlA74RO8LiLbLhHEbbBIEK9qI8iV51UfgVQl65w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌍
Pythia — رادار زنده جهان برای هوش مصنوعی
ابزاری متن‌باز که وضعیت لحظه‌ای کل دنیا رو جمع می‌کنه و بهت میگه احتمالاً چه اتفاقی قراره بیفته
🛰
🔺
بیش از ۴۰ منبع خبری و اطلاعاتی رو هم‌زمان رصد می‌کنه (اخبار، درگیری، بلایای طبیعی، هشدار آب‌وهوا و...)
🔺
پیش‌بینی از فردا تا یک سال آینده
🔺
کاملاً رایگان، روی سیستم خودت اجرا میشه — بدون اینترنت، بدون سرویس ابری
🔗
لینک گیت‌هاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/ArchiveTell/7634" target="_blank">📅 17:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7633">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0211ff0275.mp4?token=bxM1YzUBbOTPMJZ1AettpNFVIJX3yWE7oHIkROZ8yv0aioP7P5z6ORjPjcKhNSvM0M3TTQ6P5bEFLMJq87_g73TI8-iqz5HpmMLxpJjOHhNwnoSh2FXTFJLqkY5unnssNaEUyJ_XMJBf87n6AIxqmP8FC6pMnfPXfMU1dXhLwHS7I8ZqFyOLY-lWirgHBRzbNhzj4YAzqPjItDiSx8sx4bYszNVCj0e05gbBDvQ3ACiGqoJUex66jlhmdKJrvBgspTvXJI3uMggGV725-xRLL5wTihUEB6XoNlJsh2dsLDFeA2aDHj3ZenaD2nH-xcFyMFigEZKoWu0WVVqi8kFPrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0211ff0275.mp4?token=bxM1YzUBbOTPMJZ1AettpNFVIJX3yWE7oHIkROZ8yv0aioP7P5z6ORjPjcKhNSvM0M3TTQ6P5bEFLMJq87_g73TI8-iqz5HpmMLxpJjOHhNwnoSh2FXTFJLqkY5unnssNaEUyJ_XMJBf87n6AIxqmP8FC6pMnfPXfMU1dXhLwHS7I8ZqFyOLY-lWirgHBRzbNhzj4YAzqPjItDiSx8sx4bYszNVCj0e05gbBDvQ3ACiGqoJUex66jlhmdKJrvBgspTvXJI3uMggGV725-xRLL5wTihUEB6XoNlJsh2dsLDFeA2aDHj3ZenaD2nH-xcFyMFigEZKoWu0WVVqi8kFPrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔍
شرکت Anthropic ابزار رسمی بررسی محتوای Claude رو منتشر کرده
راهی برای فهمیدن اینکه یه فایل با Claude ساخته یا ویرایش شده — مستقیم تو مرورگر، بدون آپلود
🔒
📎
دنبال یه نشونه امضاشده (C2PA Content Credential) می‌گرده که Claude موقع تولید عکس، ویدیو یا صدا داخلش می‌ذاره.
🖼
فرمت‌ها: عکس، ویدیو و صدا (تا ۱۰۰ مگابایت)
⚠️
محدودیت‌ها:
🔺
فقط نشونه Claude رو تشخیص میده، نه هوش‌مصنوعی‌های دیگه
🔺
نتیجه «پیدا نشد» یعنی نامشخص، نه «قطعاً انسانی» — این نشونه با ادیت یا اسکرین‌شات پاک میشه
🔺
هیچ اطلاعاتی درباره سازنده فایل نشون نمیده
🔗
لینک ابزار
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/ArchiveTell/7633" target="_blank">📅 16:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7632">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/424c6d8acc.mp4?token=eX8V_FhTZi3gOWzqJJBJyf1Rp1lISxuV1EZy7hdT5rrmQjTavgX8eUDVcJ2QM7n59AaTfZI4VQ4KerTrqlRPOs4Rm-57TMoWOSVC3KgqT0PP8gTSeShd4z0XjXjkzJ5tuQd2AaDtweSdw9281UqvTommx6-JodB3ZWgk7fofUxPtPyLC-M5J0NZhVllwso8q99mGnVmrXd8753MxKzNa7qcSJ-skeUurnrjqUZXkIbYixwKc4DT51ZsOJV5Fu8ylY4-zLFGpk5by0C8nx_m0FE637YazpAr-Cr9BXxVR6uWh9cVrBfaNpuFHpakD9M-BvOwYLOwvUp4JAtLvdWLAfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/424c6d8acc.mp4?token=eX8V_FhTZi3gOWzqJJBJyf1Rp1lISxuV1EZy7hdT5rrmQjTavgX8eUDVcJ2QM7n59AaTfZI4VQ4KerTrqlRPOs4Rm-57TMoWOSVC3KgqT0PP8gTSeShd4z0XjXjkzJ5tuQd2AaDtweSdw9281UqvTommx6-JodB3ZWgk7fofUxPtPyLC-M5J0NZhVllwso8q99mGnVmrXd8753MxKzNa7qcSJ-skeUurnrjqUZXkIbYixwKc4DT51ZsOJV5Fu8ylY4-zLFGpk5by0C8nx_m0FE637YazpAr-Cr9BXxVR6uWh9cVrBfaNpuFHpakD9M-BvOwYLOwvUp4JAtLvdWLAfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساخت رایگان ویدیو با مدل قدرتمند Seedance 2.5
🎬
🆓
خبر خوب برای علاقه‌مندان به هوش مصنوعی! سایت Dola مدل Seedance 2.5 رو به خودش اضافه کرده و حالا می‌تونید هر روز به‌صورت رایگان با این مدل ویدیوهای جذاب بسازید و لذت ببرید.
🍸
🎉
✨
ویژگی‌ها:
🔺
تولید ویدیو به صورت…</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/7632" target="_blank">📅 15:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7631">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gPKbfxtqmAdgCIfVEV-_NeY8AckMNP_jR3g85ygrGOIX-prNAh3FHROova3FTo7gN7dEjbPtsCAOUqUR8D0AzqTJi5Uh-NSSeiMPYFcn6wmxqbkeA-DYhjwadglrLzppGSLP5rJFDee4_CaMut9CzcWUpTzctwa5DzcTfGWVSYKhTZhlygltAWfshlR37ssYXH44W3eiLjmzyKcEO81-QcLhNh5cXiLi9b56p_rAwTs2L7jIYPYs4MuGFPUthmoKqoJEY2kKBQ6GXANqrW_Db7_JbE5TLE_scdMYIf57tWYUXe4hzobS3MQ5wmZ9DNtnc7chCxr7KsKP3ZxysmDQPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گرفتن API رایگان GLM-5.3 از طریق TokenRouter
💥
🆓
بدون کارت اعتباری، مستقیم قابل اتصال به اپ، چت‌بات، اسکریپت یا هر ابزار هوش مصنوعی دیگه‌ای
🤖
📌
راه‌اندازی:
1️⃣
ثبت‌نام یا ورود به حساب TokenRouter
2️⃣
ساخت API Key
3️⃣
تنظیم Base URL:
https://api.tokenrouter.com/v1
4️⃣
انتخاب مدل:
z-ai/glm-5.3-free
⚠️
نکته :
به دلیل رایگان بودن ، مدل کمی کند هست و باید در ساعات خلوت استفاده کنید ، محدودیت و ریت لیمیتی اعلام نشده ، این پیشنهاد به مدت محدود در دسترس هست
🔗
لینک ثبت نام
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/7631" target="_blank">📅 14:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7623">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d216f75e8.mp4?token=EScMXAbwwI95RoVJ2wJNCw4D1-ixNgLHxVGEgjxOrCFP9L1JNwtmd1XX8RrFttkJ3lRuEKu-sMDAsiEYM3if3z5LPyB01gpsILVZLMGRaKAAFDCSohIP3uzjhWO3FBXD7Qa4pg7fTJE3QQjyMGvX5MvRBpvM7-veurZx3i8WqCBaDhvnX1gkKx9OqIAroQ3Q8RMwzd2A66gMbNkltE0le9vRmb9lSdRE_NWSlSQrcgnf4L_Cj-0t3GCpnbl91l2onwSeD8GJ9ZglOck_58UXTpVgYT_qaFhKuIWAR1F24zxgWXEjjP4rmpN41xg5mo4MoClhDLr9sQ2BFIeU-8Bvng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d216f75e8.mp4?token=EScMXAbwwI95RoVJ2wJNCw4D1-ixNgLHxVGEgjxOrCFP9L1JNwtmd1XX8RrFttkJ3lRuEKu-sMDAsiEYM3if3z5LPyB01gpsILVZLMGRaKAAFDCSohIP3uzjhWO3FBXD7Qa4pg7fTJE3QQjyMGvX5MvRBpvM7-veurZx3i8WqCBaDhvnX1gkKx9OqIAroQ3Q8RMwzd2A66gMbNkltE0le9vRmb9lSdRE_NWSlSQrcgnf4L_Cj-0t3GCpnbl91l2onwSeD8GJ9ZglOck_58UXTpVgYT_qaFhKuIWAR1F24zxgWXEjjP4rmpN41xg5mo4MoClhDLr9sQ2BFIeU-8Bvng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اثر های شگفت انگیزی که تا الان توسط GPT 6 Astra خلق شدن
🚀
✨
🔗
منبع اول
🔗
منبع دوم
🔗
منبع سوم
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/7623" target="_blank">📅 13:08 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7622">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/ArchiveTell/7622" target="_blank">📅 13:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7621">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fffh0ccBPCiK6UePllQ2IFWYQVXGpVhoZvu-TbubIJ5WPk9blbICckuVL4F2c2xFnP_XsfaVQDNYYUHRMGqHNmut-03f7NW3VnB3Gb2ISR__fWwh4EJ-8s9vMrpG_agOev1sIX9vh_tRC9KgOs3qFdYncr-eo78HTdLxzztQR536US2iZsp7mzU-GEU_BxUBQLJB4oDAcwkdJ4yfuryM-y3H66ZOXUtDwGb3WLaUc7eulCjR06dy5q8EDLrm0G3G2Uz45-3wuHKJHO85Z3oeLOCA-nz-EZ_Phu42V-81CRN9vYmqmDuZ5VGvMY9XOMieEOpTJZkPXE_HmlHW37ctJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎨
کتابخانه پرامپت YouMind
بیش از ۳۰٬۰۰۰ پرامپت آماده برای هوش مصنوعی
100% رایگان و هر روز آپدیت می‌شه
⏱
📦
چی توش هست؟
🖼
پرامپت تصویر (+۳۲ هزار)
🎬
پرامپت ویدیو (+۹ هزار)
🌐
پرامپت طراحی صفحه وب
⚡️
بر اساس مدل‌های داغ:
GPT Image 2 · Nano Banana Pro · Seedance · Gemini · Grok Imagine
🗂
دسته‌بندی حرفه‌ای بر اساس سبک، کاربرد و موضوع (پرتره، انیمه، سینمایی، سفر، اکشن و...)
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/ArchiveTell/7621" target="_blank">📅 12:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7620">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/ArchiveTell/7620" target="_blank">📅 11:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7619">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7619" target="_blank">📅 10:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7615">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SSZAxWi5psWHWo4nh7dHWjga5M5a5ehhy3sWnDb0pkZKhUfjGTEadaXC3nulAqp5hA4knzO09zjzsaXP3lJ3gleUpJ9H2iysECMAnFNlKFH9y-osHXz_K9AbQXgXScFPshryV4oO4ZmjrTp4BD44WYhGy1fqdUXbvbC46c2H84N9hyC5oBLVqx5R91fryfv9xFeYWoyq3gn_sOtUlhh8QKLw_1Ux2x6sGrBU8-uc69QNrc1Ddmk0JP4TgHF8ziQQr8BzJj-W8T57zYGjmtIfQGoYVz9WQH8-Uo84Jd7N1-CXYQ0ATT0zOWPLmBclU84lrxT6FQPcpmZ9GRnFeXRi3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Fable 5.1 2 days Free
⚡️
⚡️
https://arena.ai/text/direct?model_a=claude-fable-5.1-high
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7615" target="_blank">📅 19:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7614">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eOsaVY3YHt9oTv1e0tv5VNf0ken3rrO6RRzXOeuaGdWxx5kQ12fIGIG9KHcYGjJiFoMmepDqbYjb1xgnkHG071bJTFFJoNkTdzV0UuDpd_RLXFIUykUw_dfkkFK8CPh6V8yXdWNPyfEdKnSxT2HYjt4OgaJlpVs7Xu0YA3BYphqiZp8BW0P3vG8GfIZmRwxsrpfYhkVzvGOOzwq-144fh5Wqoz7C1zBkxR2fRm4AQa-4aFhjCTUbc6YzemPo9oDfhikj7ezKS1HieQJpRKS-7aO8VBh-2nYG7MOUyS0EDz-yI2VhYgzhchRSqEGM-iporiExFwob6kj0x8z_TamOHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
خبر خوب برای برنامه‌نویس‌ها و علاقه‌مندان به AI!
مدل‌های قدرتمند GLM 5.3 Flash و DeepSeek V4 Flash الان به‌صورت کاملاً رایگان
🎁
داخل IDE چندعامله‌ی Verdent در دسترس هستن — بدون نیاز به کلید API جداگانه یا اشتراک مدل!
❌
🛠
روش استفاده:
1️⃣
برو به سایت
Verdent.ai
2️⃣
نسخه IDE رو دانلود کن
3️⃣
وارد شو و از GLM 5.3 Flash یا DeepSeek V4 Flash به رایگان استفاده کن
⚠️
نکته مهم:
این دسترسی رایگان دائمی نیست! محدودیت مصرف ۵ ساعته و هفتگی داره پس قبل از شروع یه پروژه‌ی طولانی، حتماً سقف باقی‌مونده رو چک کن
📊
⏳
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7614" target="_blank">📅 18:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7613">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔥
۱۰۰ مهارت برتر ایجنت‌های هوش مصنوعی — رتبه‌بندی روزانه  سرویس Linkly AI هزاران Skill رو از چند اکوسیستم (skills.sh، ClawHub، SkillHub چین) جمع و بر اساس نصب و رشد رتبه‌بندی می‌کنه.
📊
⚙️
بیشتر لیست رو ابزارهای توسعه‌دهنده پر کرده: مجموعه بزرگ Azure از مایکروسافت،…</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7613" target="_blank">📅 17:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7612">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qsGRcNMThm2yqEfkyBfdZnlGPjL5p5VPwlYq7nijswzBXxaXMmYfa1FsnV4nylBb9486zkZ1RpLQh6vP5IAz2iXjivxYaHCSfkv6e-0nBtA7cF9KgIRe_B1A-N8w_ospY3RkQgaPUakiqMeMbTmFEWikwSIpmh9x73TLy2l_3ZDq4YwgVKy6ZmFIIg82p7eHzjHyB5RgAJL4LHlzGJWEUcBvmptZoIh_5k4wuhBMq5VyYWcUfeS2s3f0J_eG0uMBVMTVSK1rZanp6ubfuk3i2-rir4Gt1W-z_zaxXMX_oLn_asBGYxoP0RaC5ewdFVG9Ys4TSEBzEm95PyklRF9aRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
۱۰۰ مهارت برتر ایجنت‌های هوش مصنوعی — رتبه‌بندی روزانه
سرویس Linkly AI هزاران Skill رو از چند اکوسیستم (skills.sh، ClawHub، SkillHub چین) جمع و بر اساس نصب و رشد رتبه‌بندی می‌کنه.
📊
⚙️
بیشتر لیست رو ابزارهای توسعه‌دهنده پر کرده: مجموعه بزرگ Azure از مایکروسافت، Prisma، Supabase، و اتوماسیون‌های ClawHub (اسلک، دیسکورد، نوشن)
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7612" target="_blank">📅 15:42 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7611">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">10000 دلار کریدیت رایگان Fable 5.1
💥
🆓
🔺
Base URL: https://syntro.up.railway.app/v1
🔺
Model ID: claude-fable-5.1
🔺
API Key: sk-pHXhquluKg5xOejYuGxaFkrZbgArNB7kX9HtvekqCwA64pWc
✈️
@ArchiveTell | #API</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7611" target="_blank">📅 14:06 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7610">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TN9J1yKpatUaGbT8Ho4QV-RccZ8sXVvIVJf-U-Dbbt0k5es_b1IgLQMP8HbmNduOvcPo9NDSMyEUi5Tq7hvldtpHKLhwdj8KyQXqLAQ8XOW2tbG73h8o6qI6aKRmsaqU4ffWr7GFs2kiTjFe2x7BuKceYyv9KnstYYfUv3B8Q0RwgrfFirpAf4kVynnGfk4wZd0uFl-DFQf-_TTjuy88E6QAjoq50y90tdly8nWtDq5I5vac_B647EPS1Tv6iwXhrhntNu-v5SlwBd5Rk9PnGGP14J39QyXsUM45PX9rrW_nJ6a9jzygK2nP_A5eZ7RHnzKauUVRUUTbHOkFtjuJcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">10000 دلار کریدیت رایگان Fable 5.1
💥
🆓
🔺
Base URL:
https://syntro.up.railway.app/v1
🔺
Model ID:
claude-fable-5.1
🔺
API Key:
sk-pHXhquluKg5xOejYuGxaFkrZbgArNB7kX9HtvekqCwA64pWc
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7610" target="_blank">📅 13:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7609">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ری اکشن بالا باشه
😁
🔥</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7609" target="_blank">📅 13:36 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7608">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">Free Deepseek 2.5 Billion Tokens
🌊
Base URL:
api.pkay.fun/v1
Endpoint:
https://api.pkay.fun/v1/chat/completions
Key: pkay_f38d9bbbfdaea88a190f415eb007ef2ffb74bed33961c366
Model: deepseek-v4-flash
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7608" target="_blank">📅 12:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7605">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GyZYFuKmQnOxS1CFPwvo02OHJpXYR59S-IzHAaungh8gUAlssro7Nb42lYlwUhJmHX7PPXANqxuEWnNEZOLHGqsNDN0Xdt-418RoOyS47HiIHjDLOkKbk_2Fc1F-sVvi4K2gDUo0prtpdT8V2aINqW2Y6FV5QrxPrAro05RkF5ibWV0aXFIEKqDznvSyRyymVgp9qtJXBPjtZj_AzbwU0lUvvggSL3IsfAcgUzv30FdyQbywL5-Y220mBBQgCkQHTtx929YISkdKVQ-O5TN0kGJCmymxiiHkCJqkNlANF-UXs6NXMy_ifUlPMEy9ExPtZDeyn7xQbjAf9RvoYsIsWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
مدل Gemini 3.8 Flash در برخی موارد از Opus 5 پیشی گرفت - با قیمت 0.75 دلار برای هر میلیون توکن
شرکت گوگل، سومین مدل Flash را در عرض شش هفته منتشر کرد. Gemini 3.8 Flash برای برنامه‌نویسی، کار با ابزارها و سیستم‌های عامل مستقل طراحی شده است.
بر اساس تست‌های گوگل، نتایج به این صورت است:
⚡️
Terminal-bench 2.1: 89.4%
در مقابل 89.1% برای Opus 5
⚡️
Finance Agent v2: 61.4%
در مقابل 58.6% برای Opus 5 و 53.8% برای GPT‑5.6 Sol
⚡️
HLE-Verified: 54.9%
در مقابل 54.4% برای Opus 5
⚡️
پردازش ویدیوهای طولانی: 87.8%
در مقابل 75.4% برای Opus 5
اما این مدل در همه زمینه‌ها از مدل‌های پیشرو پیشی نگرفته است:
⚡️
DeepSWE v1.1: 71%
در مقابل 74% برای Opus 5
⚡️
Terminal-bench 4.0: 19.1%
در مقابل 51.8%
⚡️
OSWorld 2.0: 59%
در مقابل 75.4%
به عبارت دیگر، این مدل "جایگزین Opus" نیست، بلکه یک مدل سریع و ارزان است که در برخی وظایف به مدل‌های پیشرو نزدیک شده است، اما در کارهای پیچیده و تست‌های جامع سیستم عامل، عملکرد ضعیف‌تری دارد.
قیمت این مدل تا پایان سال 2026 ثابت باقی می‌ماند: 0.75 دلار برای هر میلیون توکن ورودی و 3.75 دلار برای هر میلیون توکن خروجی. پس از آن، قیمت دو برابر خواهد شد.
همزمان، گوگل مدل Gemini 3.8 Flash Cyber را برای جستجو و رفع آسیب‌پذیری‌ها معرفی کرد. این مدل در CWE-Bench امتیاز 47.2% را کسب کرد، در حالی که مدل پیشرو امتیاز 47.8% را کسب کرده است. دسترسی عمومی به این مدل وجود ندارد: نسخه Cyber فقط به متخصصان امنیت تأیید شده از طریق برنامه Fairwind ارائه می‌شود.
در حال حاضر، این نتایج توسط خود گوگل ارائه شده است. هنوز هیچ تست مستقل از این مدل جدید انجام نشده است.
⚡️
جزئیات بیشتر:
Google
⚡️
بنچمارکش داخل سایت
https://artificialanalysis.ai/models
اومده
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7605" target="_blank">📅 21:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7604">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">Gemini 3.8 is out
💪
از اینجا رایگان تست کنین نظرتونو بگین:
Aistudio.google.com
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7604" target="_blank">📅 21:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7602">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vf6LIgyPyX-B-J8qEH80CuBelWeEz5X7Hb7t522JsDl1pCbih3zJbcZ8BymB-tqQg9skrEJZBVI84OSrJAhpX4IKarVilm4xTQMSFFluytD9cQ6KzziohWPGG6FpE8VZzF9t6SpGp9fo_amzc1EXw9TZGAqpd1VP2T1fEhtgNHmd5l3rDQ3klOm2NaWJ-lz7XmEdOFAc7NufzMulzJrQOEUCdMCb7SgrN9vykaH1zTdR0Ud44E9aQs5gQAEizSe9KJT2oZQeKMD5TMyJZoizEJW3TbeN9XPcxT6hr8dZOXRtOW4zwF0v3DPbobccc3kyD-Jje2hjne5kNm-NN0ZWcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل DeepSeek-v4-Flash را به صورت رایگان از طریق سایت Flatkey دریافت کنید.
🔗
https://flatkey.ai/
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7602" target="_blank">📅 14:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7601">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">هواوی کد (Huawei CodeArts) به صورت روزانه 10 میلیون توکن رایگان ارائه میده که از مدل‌ GLM 5.3 Flash پشتیبانی میکنه و امکان نصب آن در VS Code وجود داره.
🔗
https://activity.huaweicloud.com/codearts_agent.html
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7601" target="_blank">📅 14:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7599">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/atcBD8e-eX9sRjkq-OCKCW4Lkiuyy_va_-8o27uFDvAC7ciTmyooJYgbtJxfSJioOnnRDqZfLwBIEMF9GucELKBoEcNlKL1kwoSdR_oe3-ThtuupeMfXupGrkrewVz7YzsYGdz-NISRGRTZvmi2iLO38Aqauxoj2ygcpGuKTBE4m3Wd09Nm5ythETE_u-vMI3p_ssEUp5pLAluexWzvsAt8irTKoVGjGUBWc7uvbkFcCKQu1j2DAP2w-6Nq2J4GFUfyUp_IZNsVf8TAAS4Yhduw0FBEvw2lgrNdjf1Ajv1Oo6RMClWL8F2kY3jq9sXLQAegxgmtADNaUSRGI-gUmog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاد فابول ۵.۱
⚡️
😎
با تفاوت معنا دار antrophic هوشمند ترین مدل ai رو داره
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/ArchiveTell/7599" target="_blank">📅 22:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7598">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">GoRouter  Opus 5 $13000
🔑
کلید:
sk-vWZcSRFLAJF0Id4G9AQ1HUZ4CmpWGIish3QseC7fuxb7LmzF
🌐
آدرس پایه:
https://gorouter.app/v1
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7598" target="_blank">📅 20:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7597">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RNYi2qiJfJbVNjt9FrMOrz5HuogYBKpAHmV_ez0pQKEpS3IAq5Wx9uVfS8Z8T7UY5VqK5LSY8MMjCzK9tvo21pbFzh-NtPgtNMDPRrIA7Ix3NIKLnBqgWIlt681QkEHSaousydtKthvnZGQEIJL2SrlviIp_N5cU7fXPyGvvy4WqdfNBcgDh35riIKKe6yradxMi4lpabEzTdQjwrsod88ytninbVCSxivHCQQXkuzv7eRFPYWz9Ptn5b-XBSKkz0k9n-sTMB11NOPl2HfJWNAd6yuVJdlaqe46ZHpZUdLWcYxPPAUu2zC_X21SZewsCzh163o9mfM9K-FoPdVOJdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
ریپوی ArasClient پابلیک شد!
بالاخره سورس کامل کلاینت روی گیت‌هاب عمومی شد
✅
🔗
گیت‌هاب:
github.com/ArasTey/ArasClient
📥
دانلود مستقیم:
github.com/ArasTey/ArasClient/releases
فایل arm64-v8a برای اکثر گوشی‌ها
✅
فایل universal برای بقیه دستگاه‌ها
⭐️
اگه خوشتون اومد یه Star یادتون نره — برای ادامه مسیر خیلی انگیزه میده
❤️
━━━━━━━━━━━━━━━
چرا ArasClient؟
چون کار چند تا اپ رو یکجا می‌کنه:
⚡️
اسمارت کانکت
یه دکمه: همه سرورها همزمان پینگ می‌گیرن و سریع‌ترین وصل می‌شه
🔃
سورت سراسری
بعد از هر تست، سریع‌ترین کانفیگ از هر سابی بالای لیست قرار می‌گیره
🔓
فرمت اختصاصی .arasc
ک
انفیگ‌هات رو تو یه فایل رمزنگاری‌شده امن ذخیره و به اشتراک بذار
حالت Protected: طرف فقط می‌تونه وصل شه و پینگ بگیره — نه آدرس، نه URI، نه اشتراک‌گذاری مجدد
📊
اطلاعات ساب
حجم مصرفی، حجم کل و زمان باقی‌مونده ساب مستقیم از لینک ساب خونده می‌شه و بالای کانفیگ‌ها نمایش داده می‌شه
📣
اعلانات ساب
پیام‌های سازنده ساب خودکار نمایش داده می‌شه
🏳️
پرچم کشور
کنار هر کانفیگ پرچم کشور سرورش (از روی IP واقعی سرور تشخیص داده می‌شه)
📊
آمار اتصال
تایم اتصال، آپلود و دانلود لحظه‌ای + آمار کلی در تنظیمات
🛡️
همه پروتکل‌ها
VLESS • VMess • Trojan • Shadowsocks • Hysteria2 • WireGuard و…
💎
پر-اپ پروکسی، روتینگ کامل، بکاپ و رستور، تم روشن و تاریک
━━━━━━━━━━━━━━━
🔒
ویژگی‌ای که هیچ کلاینتی نداره:
کانفیگ‌هات رو با پسورد به دوستات بده — اونا فقط می‌تونن وصل شن و پینگ بگیرن. نه می‌تونن آدرس سرور رو ببینن، نه کپی کنن، نه برای کسی بفرستن. مخصوص فروشنده‌ها و ادمین‌ها
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7597" target="_blank">📅 19:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7596">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/by6MzdNTAm66INhmgJF5iWNuN6v7No82uXE2p913yCPgfrLM12IdUmoDBobTCUKrfaoH6PAp9zcqFclHuQl2Po2laesfxNsi6Dbd9ZrvrZUDHnMwWk5SvnP3qOUTusphZd-eGKjhll81zqi49rDG_LHrom1HyeKoTX7a2WuGfVqsaFjGXwJ3x8JQukM1pZEKhAMRIIVAw8suu8Np3TWB3KPWpf9DGnYBKQLMR257X5x1L1mcjHgzAk_pGObWdEkL-8FRIqVDUxQKdWa2qX4gN2Vd7tHzXArOnxWBgpW9pKYlDg349thdGL7y0XuOW8TvequnSbBhuaTKPtS3Xa5Y5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧑‍🎓
✨
OpenMAIC — کلاس درس تعاملی با هوش مصنوعی
هوش مصنوعی داره تبدیل به یه دانشگاه آنلاین کامل میشه!
OpenMAIC
یه پلتفرم متن‌باز برای ساخت دوره‌های آموزشی تعاملیه — شبیه NotebookLM، ولی با کلاس درس مجازی واقعی
📚
📤
چیکار کن؟
یه موضوع، فایل PDF، اسلاید، صوت یا ویدیو آپلود کن، سیستم خودکار می‌سازه:
✍️
ساختار منطقی دوره + اسلایدهای آماده
🔤
آزمون، تمرین و سیستم تصحیح خودکار
🔬
شبیه‌سازی، مینی‌گیم و مدل‌های سه‌بعدی
👨‍🏫
معلم‌ها و همکلاسی‌های هوش مصنوعی برای بحث گروهی
🎙
سخنرانی صداگذاری‌شده + تخته‌ی هوشمند با نمودار تعاملی
📦
خروجی:
فایل
.pptx
یا
.html
قابل ویرایش
🔌
سازگار با:
ChatGPT، Claude، Gemini، DeepSeek و مدل‌های محلی (لوکال) هم پشتیبانی میشه
⭐️
۲۰.۷ هزار ستاره روی گیت‌هاب
— پروژه‌ی فعال و پرطرفدار
🔗
لینک سایت
🔗
لینک مخزن گیتهاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7596" target="_blank">📅 18:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7595">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gm9GvvxomTPsKF8e_favlbKunkDmdHkI_fysdi1Sc980pG9CviBrxmZhtscmV8V3TNIVa1r0Dt7O2AHytpZ2BMGN4FSzA27saUA25mUsKSBQZ5A-S3tIpdD14p0YKZA-paSUfBr3CXdmrSmLxgFnmaGwzEC3_eAUpRxqvoF-EhjyA23b0ofFjRZXEka2qWy98H9Nvyc82jB6Rd1Mw4aTWiuAhXtPNriR2OrpA9kmSkZbSW5GG0jSKAJYqnyFGFnSJY1rPLuXnPv2IKp2gBelJoIT3tyGQ36fKkj23cWczo964Ft7U7wWQBxvLHZB4DMWQpy2H87NVbTG2MSzKuzfFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
✨
۵ ویدیوی رایگان روزانه با MiniMax H3 Max — بدون ثبت‌نام!
با این سایت میتونی این مدل ساخت ویدیو رو به صورت رایگان امتحان کنید
🔥
✨
ویژگی های کلیدی :
🔺
روزی ۵ بار تولید ویدیو، کاملاً رایگان
🔺
هر کلیپ ۵ ثانیه، کیفیت 768p
🔺
صدای طبیعی همزمان‌شده
🔺
متن و عکس به ویدیو
🔺
فریم اول و آخر بده، مدل حرکت وسطش رو بسازه
🔺
نسبت تصویر: 16:9 | 9:16 | 1:1 و...
بدون نیاز به اکانت برای ۵ تای رایگان روزانه — با لاگین هم ۵ تای دیگه اضافه می‌گیری (تا ۱۵ ثانیه‌ای)
💡
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7595" target="_blank">📅 16:31 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7594">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ceb_ZZX7irHCPSjie5U2w-ec4AwQjSPSygglklj-HHciCodVZpH_cdnGBCE_lYXJvEM6m6UwmG0BxLaJbWCTd1CKx8obcaa0lsosQ2UuwcYdBGD8FyXIDMpX6NVmg1dXRFDae3aI2VftrHTB326Qcymbo1C2g6jgsa40HRk9sqm800QxcbSU8MOCPiwa8Cs3qAfGHatYqi86GREvfIVU2NUQZpcS-DyH_06W-4MFWFhMLcUJEz90pKUjgQjZR1mdKEQE1gi9UkK1OdoL7dT1eh7yREPgeXQ7OhccG_6VCVuUoMIq5BoB5BPc6yO5Q3usxymzjCUE3drJfrMbgT8afw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔧
✨
دانلود کامل گفتگوهای Claude با یک کلیک!
معرفی
Discussion Downloader
— یک اکستنشن ساده و سبک برای Chrome که گفتگوهاتو با
claude.ai
به فرمت
Markdown
ذخیره می‌کنه
📝
📥
چیکار می‌کنه؟
کل گفتگو رو استخراج می‌کنه — همراه با:
👤
مشخص بودن نویسنده هر پیام
🖥
بلوک‌های کد سالم و دست‌نخورده
✍️
لیست‌ها و جدول‌ها با فرمت درست
🏷
هدر YAML با متادیتا (عنوان، لینک، مدل، تاریخ)
⚙️
چطور کار می‌کنه؟
برخلاف روش‌های معمولی، داده‌ها رو مستقیم از API داخلی
claude.ai
می‌گیره، نه از روی صفحه! چون توی گفتگوهای طولانی پیام‌های قدیمی از DOM حذف میشن و روش‌های عادی نتیجه‌ی ناقص میدن
🎯
🔒
حریم خصوصی در اولویت:
✅
فقط دسترسی
activeTab
و
scripting
✅
بدون آنالیتیکس، بدون تله‌متری
✅
هیچ داده‌ای از مرورگرت خارج نمیشه
✅
رایگان و اوپن سورس
⚠️
محدودیت‌ها:
🔺
فقط شاخه‌ی فعال گفتگو صادر میشه
🔺
آرتیفکت‌ها و بخش thinking صادر نمیشن
🔺
رابط کاربری فقط روسیه
🔺
نصب دستی (unpacked) — توی Chrome Web Store نیست
🔗
لینک مخزن در گیتهاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7594" target="_blank">📅 15:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7593">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rJE8ubhRIGBd9H6q5kxnwI1Z4e6zYCgmAIzclZnQFNtYUggRSI876XBncXkK3Zons2ahum-hmH-0fiRnMNR_gSu-JZzrCfMfNVAm5SLj298D37v1c56RTYObXWbYUOigXg5TpWs3DpRWhW8THHgVFUHU_xsbcReL2CircZ9N_YEhSV5xmcMWSX_mlhxsPcMXqwbdQacbQP7KERAe_IkgwJscq0Ti-YzLQwAwtaPXE1vZb1DMuhKsbb9d-AZduApMYYd2trNVYgBedqiOLqqOjy1nirQ_r49uie2rO6anELu40SQxsOXKDBM4VFOKaHaGewPRd8gMOgvXnWeRIsZR0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦆
✨
حریم خصوصیتو با هوش مصنوعی معامله نکن!
با
Duck.ai
بدون ثبت‌نام، بدون اکانت، بدون هیچ دردسری به قدرتمندترین ابزارهای هوش مصنوعی دسترسی داری
💥
🆓
💬
چت و وب‌سرچ با GPT 5.6 Luna
🎨
ساخت عکس با GPT Image 2
🔊
ویس چت با هوش مصنوعی
سؤال بپرس، جستجو کن، تحقیق کن، عکس بساز —  همه‌چیز رایگان و خصوصی، بدون اینکه ردی از هویتت جایی بمونه
🥸
🔒
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7593" target="_blank">📅 13:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7591">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t9IsqOdRPkdA-902bWvX6QOUPtvaoIsSH_PIExLEuFn10PFv1ssrznhco_Ho_QJi7kWNv-qtCMjbxvC68825vp2Hk7nNNYDEIgxd0sQnS8P-8PAhWJMb96b09XmHctNBur2B2PpB5_vV71V_yalBfoEb1AUNOWyAtDI1OcU4Ay39H4XPvYp8G84itLkmhghmujIh4oypv6oWkLK9qe8MYd3NGdckcJt3ygAHtLen0PCTP5i0ueKWkbLFhrN0pNiw4pbnb3qiS7OANo4jGPatAqW28vDplt1zyPCUPU0hZqlA-LKkrDAxwDjOrja776AztujZGENXGPJq3INPvSrNdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی Hy4 Preview: رقیب جدید GLM-5.3 و Kimi K3
شرکت تنسنت، مدل جدیدی از خانواده Hy را منتشر کرده است که قبلاً با نام Hunyuan شناخته می‌شد. این بار، برخلاف روال قبلی، مدل به صورت عمومی منتشر شده است، وزن‌های آن در دسترس قرار گرفته و به سرویس‌های محبوب اضافه شده است.
اطلاعات کلیدی:
🟢
770 میلیارد پارامتر، با 49 میلیارد پارامتر فعال به صورت همزمان
🟢
ظرفیت پردازش متن: 1 میلیون توکن
🟢
حداکثر طول پاسخ: 64 هزار توکن
تمرکز اصلی این مدل بر روی وظایف پیچیده و طولانی است: کار با کدهای بزرگ، تحلیل چندین سند، نمونه‌سازی بازی‌ها و تحقیقات علمی و غیره.
در یک آزمایش کور، شرکت تنسنت 203 وظیفه مهندسی را به 163 متخصص ارائه داد. نتایج به این صورت بود:
1. Hy4 Preview – 2.99 ( از 4 )
2. Kimi K3 – 2.94
3. GLM-5.3 – 2.92
این مدل در تست‌های منتشر شده نشان می‌دهد یکی از قوی‌ترین مدل‌های متن‌باز موجود است.
نکته جالب دیگر این است که این مدل به طور جزئی در فرآیند توسعه خود نیز نقش داشته است. این مدل نقاط ضعف در عملکرد خود را شناسایی کرده، پیشنهادهای بهینه‌سازی ارائه داده، آزمایش‌ها را انجام داده و به افزایش 31.8 درصدی سرعت پردازش کمک کرده است.
نحوه تست:
>
WorkBuddy
– به صورت رایگان در دو هفته اول پس از انتشار
>
CodeBuddy
– دوره رایگان دو هفته‌ای، با تمرکز بیشتر بر روی کد
>
OpenCode Go
– مدل به اشتراک اضافه شده است
>
Hugging Face
و
GitHub
– وزن‌های مدل برای اجرای محلی در دسترس هستند
برخی مشکلات شناخته شده وجود دارد: مدل گاهی اوقات بیش از حد طول می‌کشد و نتایج نهایی را دوباره بررسی می‌کند. به همین دلیل، این مدل در حال حاضر یک نسخه آزمایشی است و نه نسخه نهایی Hy4.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/ArchiveTell/7591" target="_blank">📅 16:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7590">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RpBrQD6Yyl4O4-kzIZOimy2mFDa9LfNzU2uG_AGg5B9Wr_8-zjh6CjrvPSIOleRu85oPzZx91uUWq1rdqvVDFqpIIcPD-V0iUvzebfzcQ0g5CjGC5sIdhueWPfccNfvTne8jkb4soDBiEkquRy4c1P2O1egtrGzUH7wdmHbS5hSlIRY8lpA3QLMDrznCfvQHVmJkhyJM22KYGaaqfenb-Oz_QAbcFD9HBiBkJmcHxX-hm8h5VXLgZEmjKdRNEjhz4V-KrTHQNngs5ywPi807h0Qv6A_m2dJ5i3Lf7GyEdAzeL1cEKbZLH2fWsp5C36CsiKtGTtKXNc0cYq18bBXOtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
تبدیل PDFهای قطور فارسی به متن تمیز برای هوش مصنوعی!
نرم‌افزار ویندوزی و رایگان
PDF2MD Studio
. با این ابزار، PDFهای ۱۰۰۰ صفحه‌ای رو به متن استاندارد مارک‌داون تبدیل کنید.
فقط در ۳ قدم ساده:
1️⃣
تبدیل هوشمند:
PDF رو بکشید تو برنامه تا به عکس‌های سبک و باکیفیت تبدیل بشه.
2️⃣
استخراج متن:
عکس‌ها رو تو Google Drive آپلود و با Google Docs باز کنید (بهترین OCR رایگان فارسی).
3️⃣
تمیزکاری نهایی:
متن خامِ گوگل رو دوباره بندازید تو برنامه. نرم‌افزار تمام خطوط و نیم‌فاصله‌ها رو مرتب می‌کنه و یک فایل فوق‌العاده تمیز میده!
حالا این متن رو بدید به AI تا براتون خلاصه کنه یا تست امتحانی بسازه!
😍
🤔
پردازش امن روی سیستم شما
🤔
بدون نیاز به اشتراک پولی
🤔
اصلاح خودکار باگ‌های تایپوگرافی
دانلود رایگان از گیت‌هاب
(ستاره
⭐️
یادتون نره):
🔗
دانلود نرم‌افزار PDF2MD Studio
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/ArchiveTell/7590" target="_blank">📅 10:00 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7585">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eQLBmNoLjdpec4RwPZz3aowHFkibn7OnIOxkz5CYFoEtbvr3CN71_7ldpezgfYwES876KijMTrLlRUrKKFAuXaUy7ZCYfstmcOuF1fpKajNxq-S4LAQ2N8F0d6UxVFFoPLtGh8o9etjks-7MIdOLQSCOEqcvdgl2fFbFLgxALR2xVC9uhyjkKi_y1r4QPLH50EOFf0eSucQCkO3ug5sIjH2HKu5TIvnu8VA4W2Z8pYXoPCf_UxJhHJRnwQJfP_bWHyAHi9dkapgNhsmp3gG3FEVK72c-VhG2ViVsvZx9a0MvXS09Jtdi8KamF3XxwL2bAWyKagAPeLxt0JjNeGWxjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">100
د
لار برای دسترسی به API بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | Opus 4.8
برای فعال‌سازی فقط کافیه یک اکانت
گیت‌هاب ( قدمت یکساله )
داشته باشید و از طریق این
لینک
وارد شید
✅
🎁
با هر رفرال شما
25 دلار
و شخص دریافت کننده
100
دلار
دریافت می‌کند!
همچنین 20 دلار پاداش روزانه
🎉
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/ArchiveTell/7585" target="_blank">📅 12:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7584">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NLLnZ5v1Z1vnYf7NYMDldyRmdWg04hZd6ydxmheACigHmYQuBRfTgocbvFoW4AWz2Ft5ebXUtbEKA2GIM8uR8yDAyo4gUNCwjF6vAJEs8atuo7YvuYs9FYriDL4jYkoW3vWUwOnnA5BMfkfuxHUTkXn84OSL9OE_IPX4FUqYUra90BnRW7u-Vo23EcxiS_nOdlRuCRJfDMosqTI3SoI3c1eDxWLPTHDvZwR4CWYqnCpwhAifFK9nUxqYc5hox5Km0cLMpY7ZOXwAp-Fjh8zhiBRdQU4b7PTGbtMnvPJgeTSjZHZhu5QZJPkD1mglaBva7kQQka00XKjVv-s2dmQqJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت 10000 کریدیت رایگان سایت Genspark
💥
🆓
با این روش میتونید داخل این سایت برای مدل های زیر و دها مدل قدرتمند دیگر 10K کریدیت ۱ ماهه معادل ۲۵ دلار دریافت کنید
💵
😎
Opus 5 | Fable 5 | GPT 5.6 Sol | GLM 5.3 | Kimi k3 | Grok 4.6 | Deepseek V4 | Nano banana 2 | Seedance 2.5 | GPT image 2 | Gemini 3.1 flash TTS
✅
❗️
نکات مهم :
چت متنی در این سایت نامحدود هست ، محیط وب سایت یک محیط دارای Agent هست ، همچنین می‌توانید از این سایت API بگیرید ، همچنین این سایت یک نسخه cli هم داره
برای دیدن آموزش کلیک کنید
✅
✈️
@ArchiveTell
|
#METHOD</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/ArchiveTell/7584" target="_blank">📅 18:11 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7583">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aT3pQgIVhJgK964p2Z-6NP5qF4gwSEJTYcFFckdD3LsBRI9g637K-b--v0GR9Xs2fRGOKHbXtSUzqXubCYmR0HA8Hi3XHxivZRXEsBG50YH0g58JvXJ1nvFGS1EA6cmps4kDj4nx0LT8zSG6AJ8Ah1o8D67CWHJMHoaU7IesPPMfW2CDS9jso0AWR9lVnSEMGw5m3gXnmGUOAcgN09NiYYAoo1O3LfDEy4ow-XnV9Jv3iJxN6vect2cSPepgekjx2mtshLhqKOLQiKw1tMeJggOXidwxlFCKVApmxjvsoZVpzG955SKTQ9tl6q-qLqHsWoN5uASKP-dtxnh1yARlFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎨
ساخت تصویر با هوش مصنوعی؛ رایگان و بدون ثبت‌نام!
🔺
بدونه اکانت و کارت بانکی
🔺
بدونه کردیت و واترمارک
🔺
بدونه هیچگونه سانسور
🔺
تا رزولوشن 1024×1024
🔺
چندین سایز تصویر
🚀
فقط وارد سایت شو، پرامپتت رو بنویس، فرمت رو انتخاب کن و تصویر رو دانلود کن
⚠️
مدل دقیق استفاده‌شده مشخص نیست و محدودیت رسمی روزانه هم اعلام نشده؛ ممکنه در ترافیک بالا با صف یا محدودیت مواجه بشی.
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/ArchiveTell/7583" target="_blank">📅 18:44 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7581">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69bf2a763b.mp4?token=WHjXlgsEZTha99GEhFTrleuR-fkUH7Rp2IhAHFOOzPHOXdErz2XofaOv1mYumYp9JOZ4-OP2Lu_LJMUOLYQl9arn8umW6H3GC3rLVVYiQgfj8V6Mo_G9IpklTVEAoqt6_s0p0PVQ1zUdhnpeKKlnMIG24c3NBUTFqE8pLmpnSZ-CXpAYstLedfTXdaP7eVA-MrzkKqn0glpBN9WYT3A4ogudbprI-8-J7BxMV7EcZR7vKc8IUZtecjNcUvJg8hcQ_umnLj84Du0OWglKONJL9EhqeW21sWbuHSROOUsA9d-tT0s9s7XOaqLH-RUA7o8y5FEe382AQ6qtT8DIoL5BTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69bf2a763b.mp4?token=WHjXlgsEZTha99GEhFTrleuR-fkUH7Rp2IhAHFOOzPHOXdErz2XofaOv1mYumYp9JOZ4-OP2Lu_LJMUOLYQl9arn8umW6H3GC3rLVVYiQgfj8V6Mo_G9IpklTVEAoqt6_s0p0PVQ1zUdhnpeKKlnMIG24c3NBUTFqE8pLmpnSZ-CXpAYstLedfTXdaP7eVA-MrzkKqn0glpBN9WYT3A4ogudbprI-8-J7BxMV7EcZR7vKc8IUZtecjNcUvJg8hcQ_umnLj84Du0OWglKONJL9EhqeW21sWbuHSROOUsA9d-tT0s9s7XOaqLH-RUA7o8y5FEe382AQ6qtT8DIoL5BTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صدها ابزار متن‌باز و رایگان، همه توی یه جا
💥
🆓
سرویس NoSignups یه دایرکتوریِ از جایگزین‌های متن‌باز و رایگان ابزارایی مثل فتوشاپ، کپ‌کات و فیگما رو جمع کرده — همشون هم به‌صورت آنلاین توی مرورگر کار می‌کنن.
✅
🔺
بدون ثبت‌نام، بدون نیاز به کارت بانکی
🔺
توی کاتالوگ، ابزار برای برنامه‌نویسی، کار با متن، عکس، ویدیو، موزیک و خیلی موارد دیگه هست
🔺
همه‌ی ابزارا کاملاً رایگانن
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/ArchiveTell/7581" target="_blank">📅 16:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7580">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VoxFx5C57xjW3fcM-dQwfAtBcpT4mRGKshqfutZ_yEVWvKyr_0np_nvMwGb5v1XrdtJ4Lx1Va_bQpz9FflTDepvINU9JQn5VnvQrVt3CCMFTXugvJKzquqSLJwxNbA2UYc_eYWBFieeT8TnVbO97mlpWchM9yhb_IlQsIpsYUCbbP7EjP05mRzdKOZy2QDYPRySDfXtEXwg8xdoPxfSvgJPHu3EPIHUJw2X0aRgO1z7mpYku8jiXUhGnZgdFofVvhXTLfBKdjDzUtKMnhclD7HcWTu13ahB6ih7JM2Sq2-1Sb8eL4NDDJOP_k2w5I1mT_lIq0-FUcZF9YZKpJtTAow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجموعه رایگان ابزارهای تشخیص محتوای جعلی و تولیدشده با AI
🔍
سایت
forensics.media
یه سری ابزار مرورگرمحور برای بررسی عکس، صوت و فایله که کاملاً روی دستگاه خودت اجرا می‌شه — هیچی آپلود نمی‌شه
🛡
✨
چیزایی که می‌تونی باهاش چک کنی:
📷
تصویر:
تشخیص ادیت و اسپلایس (ELA)، متادیتای عکس (مکان، دستگاه، تاریخ)، تشخیص تولیدشده با GAN یا دیفیوژن (Midjourney، Stable Diffusion)، واترمارک نامرئی، SynthID گوگل، کلون/کپی‌-مووِ بخشی از عکس، و متن مخفی داخل پیکسل‌ها
🎧
صوت:
اسپکتروگرام، تشخیص موزیک ساخته‌شده با AI، فینگرپرینت صوتی، ENF (برای فهمیدن منطقه ضبط از روی هوم برق شهری)، و تاریخچه‌ی فشرده‌سازی
📁
فایل:
هش SHA-256 برای اثبات دست‌نخوردگی فایل
⚠️
نکته‌ی مهم:
هر کدوم از این ابزارا فقط یه سیگنال جدا رو می‌سنجن، پس هیچ‌کدوم به‌تنهایی حکم قطعی نیست. برای اطمینان واقعی باید چند سیگنال رو کنار هم دید
🔗
لینک وبسایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/ArchiveTell/7580" target="_blank">📅 15:31 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7579">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7791db8f9c.mp4?token=mdgJJUtJt6Nvh600PP6TvFrR07MciErmIbZViY_5MdXLDJblhWYF-pKVQZLW7tPpF6MJzzyYotVfeqZwh7WDcv1aZ-fGAcJQtTK044UOJd-C3P94DD5d1O0qbZSKvboI_CXcGEM0NYt10LFMPqTMUTtuQaLsuTafUFB7GVkd-HiVc7tjYsex1LBQAB9Uxaz9v6bjDDKqA9xMwISqjwCtWGK5GY2JCNtulKncWSPFoYPvt0PJALThB3recerqu5e6KZYDdcJE5FGUYdYCs-Q8wXQtfKnt3LvN0L4oXLjD4uQXvymur5rEUs4RElGL56CuJcnBFmitmx7Nb_xIlC2-bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7791db8f9c.mp4?token=mdgJJUtJt6Nvh600PP6TvFrR07MciErmIbZViY_5MdXLDJblhWYF-pKVQZLW7tPpF6MJzzyYotVfeqZwh7WDcv1aZ-fGAcJQtTK044UOJd-C3P94DD5d1O0qbZSKvboI_CXcGEM0NYt10LFMPqTMUTtuQaLsuTafUFB7GVkd-HiVc7tjYsex1LBQAB9Uxaz9v6bjDDKqA9xMwISqjwCtWGK5GY2JCNtulKncWSPFoYPvt0PJALThB3recerqu5e6KZYDdcJE5FGUYdYCs-Q8wXQtfKnt3LvN0L4oXLjD4uQXvymur5rEUs4RElGL56CuJcnBFmitmx7Nb_xIlC2-bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قوی ترین ابزار افزایش کیفیت ویدیو رایگان
💥
🆓
🎬
هیچی نصب نمی‌کنی — فقط فایلو بنداز توی مرورگر
✨
خروجی با کیفیت 2K یا 4K، هر کدوم بخوای
🔍
جزئیات ریز هم تمیز و شفاف پردازش می‌شن
🎁
کاملاً رایگان — نه واترمارک، نه حتی ثبت‌نام
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/ArchiveTell/7579" target="_blank">📅 14:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7578">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DZLIUc1v_VVZ7iiQA9RYwtI0O9261VCikQgNU4e-9UEjkeNQW4LDDabb36NYL6JEJmLLRQU8LFJYjX6qjFIGWWAMOWYizaPNq_WLCzgosy9FTCrk7-PcpqJtpprQM7zkbOHuL_2nkfvxdF6bsUhPxTWabtaYrsXZuJV58tRsNAPoFUm-gY61j6nHu0iKsArtQDKuto8E84YIExC8uUyVRrHNQu7w5DwEniLQvEBKR6PaEdmMb8GetcshucEsMuyTTj0MI4N-ggXU29Q4rChhuYibJIM8l0r2l0uC8uvJ6EExFRPr1zCPwcraMElWhSj3K7G1zBMLQd7ho3VOynMPZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی به API مدل های رایگان
💥
🆓
مدل MiniMax M3 و چند مدل دیگه از طریق Ollama Cloud به‌صورت رایگان قابل استفاده‌ان ( با محدودیت روزانه و هفتگی
⌛
)
1️⃣
وارد سایت
Ollama
بشو و اکانت کلود بساز
2️⃣
با گوگل یا جی‌سوییت لاگین کن
3️⃣
از داشبورد اکانتت یک API Key بساز
4️⃣
کلید رو به 9Router یا هر سرویس مشابه دیگه اضافه کن
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/ArchiveTell/7578" target="_blank">📅 13:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7577">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tGEX8bMxzZJSSU6hWjazVrdYzTWHx_WgqzU-WsJMAXt0E17fti54TGSv5GCmHw0LR4StS_2N3nl-JMcDkzKs-O7X2GUHT6lPYgA_2_gspMocDYPMy7kGNMpKFeEUrhXk48Tlx-4RiOKKSz0ZNpY-XZy8Is469yfJAf6KvP-Ujgyq0E9LJmO78JcoJYVbxI9A7hR9MHWJY5JBXIrdKMwegoqffqi_uQeBvlfKXGTFVE9poRHbW_X0n_FgW0Dp7zN8eJvKuMf_klqx4pwS9IHCzYQJmcdPC9BLKMKaK4W2I89F2cvWMDFwuny5eePbluSHQhIIMakOos2B2btopeqg8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
DeepSeek Harness Studio
رابط گرافیکی ویندوزی برای DeepSeek Harness
🤔
بدون نیاز به ترمینال یا Node.js!
🤔
نصب خودکار در اولین اجرا
🤔
وب UI رسمی داخل برنامه
🤔
پشتیبانی از پروکسی داخلی
💎
https://github.com/ScannerVpn/DeepSeekHarnessGui
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/ArchiveTell/7577" target="_blank">📅 21:44 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7572">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dh5srILY8dDnjHZrlsASt1LM0JDvaFffTyPVLc2Sq0a1vEV6au0GKDpsPlq8NHlTKmqkxumWD3BpB6Tf0IezeqtGV3NjJBaqjJqcrlFt8YdpFSOCHdObWAmktPMPHHzEqLAHMmP2f1auCaIPcx7udtjAbZ1VBDJO16wwqEQS_fGKOXQVer7Ujl8g3MrSQQ9Zv-6YizJxpFz1hGHpIyNhGdPavitPMu4y3rg9JpGH9-chUKsLRywDrwvQfTemiiHc4h0YDSGPQxLCtVwrFZ1uECSloZRH40d1ko78KPYgNisbytr8W1eHvqJ6eoXcseH9TLjRRR0Xr0leLCgbeCa79Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X2njm1PLMr4d8Jmn_2gV-aQG7hwk7zWPGlB8hDEHoLoWMsahP7JqoIaayj2UbnOL8JbRnRNMu4EEfXrRpj3ytIt5bec6EnaS6FdvlAqTvAz5HOqGpdzTSfMQwF5Dfhwq3_u39PkBwTWSow6hnUghpVJYi9S8dKkW1a-Bqjrx8fhpWHF42coghOIXndXdXYsESSIJevxWpaLTDOYCImz0y_T69AeDSbBouvdOEYrmQ9G4y0qFoc7nGfcpaFN6z_XGxIY2vMDS9VSeh9vRIrx7x1i6ZOJeMNXi5791NwYyJVXB03-9Pys_DYNu7GjS-IIXriWk5QnFkdCIhIXI2iG6OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mT_0gQAw80RY3iDSgnFV1HgkRd7jnsu1qQ_pqosWJPO3pa4tTsL02uoFX7mYiR__YnN_pDvtQO8sy28Tk-sPnsCDAAXp9tLHtM10NHCCIVlL7yHZzgn3zEOQg9iwunNumWpEwpGMLK7LF1POdi35Ebvh0Avth7ED9-ZekvieIi7lkAvq5PcB6d4xsCBweBp-C2ToK9Xt93r9i02wwKtIoSTQyrRaiSZSct4ff0Xr_t_F06XsH1Nuph_vthexIBtn3Zipoe2ceGId1n2GaQkX5s2I3swmV8upwddWOB-kac9eD6gi5QgzDxIpOxnX9ir4GG_csr8hVPICoqH0NW56AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IJsCSseba7Qk5tJrrcjrRbWnmzyU_0ouPWNiEEf5l-93XwNJF3CSOC8YyPkbD5lOtcOtQbaSQq6xBucWcPicot5l8KDD3F8_JKBcO_edgtXJ4e4kbkc8j-1Ts2It2q_S-03gEEdQUgMGEOophXz6Wr3fv_D1Wi8TdHUKLD6g87RoW6AwxLqz39dOySfC-hPzpo8qEOl8ek1kq0YG1fc1R7cuZCO97Cqdz35xZ_wp__3muRVpq3cwRj8Qjh4LyC0338nen3gFr1fFQdtAPL5poGqmZSfSKl4XmUExHO5nb2zS9KcQ7hdQe92qAJ2HKg4Dp4hD5MRM2z14_QO7CXL_8g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🛍
خرید اکانت
Windscribe
با کریپتو از طریق
Build a Plan
اگر قصد دارید اشتراک
Windscribe
تهیه کنید، می‌توانید از بخش
Build a Plan
پلن دلخواه خودتان را بسازید
⚡️
کافی است مقدار دیتای موردنیاز و مدت اشتراک را انتخاب کنید، سپس در مرحله پرداخت گزینه
Crypto
را انتخاب کرده و پرداخت را با ارز دیجیتال انجام دهید
🪙
🔵
انعطاف‌پذیر و اقتصادی
🔵
امکان انتخاب لوکیشن‌های دلخواه
🔵
پرداخت با ارزهای دیجیتال
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/ArchiveTell/7572" target="_blank">📅 19:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7571">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">‏
🔥
سورپرایز دنیای هوش مصنوعی؛ قاتل جدید ‌Fable 5⁩ اومد!  ‏مدل مرموزی که با نام مستعار Ox Alpha همه رو شگفت‌زده کرده بود، همون ‌GLM-5.3 Flash⁩ محصول شرکت چینی ‌Z.ai⁩ از آب دراومد. کمپانی رسماً تأیید کرده و قول داده وزن‌های مدل رو همین امروز منتشر کنه
🚀
‏توی…</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/7571" target="_blank">📅 18:47 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7569">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ekn1RRide4KDs_g_xBGHNLu_Ri2uM6ltjWj3X1iDwAiia6aQ-inq_77rUwIe5TD0OybjI0uDhPTX6UWc0pozgfeiLGlLdtD5MRWlDFkrLOZ62U6FYDG2D_y-ErvAB7roMneGj1ZFL4FFL3SA4P_ikq1Q48H-IU2ZFwmXrlXBmxqBS81uAS_neOSElx2eylTzzyF9_F_qmhnGBsb4OzOKaKRxZ8jBd5RMsP0CKNo6OFrDPoZOLjWDvTcjV7LEoLE9DELFFonr1fCJAylYM0XWLbdli0KZgboQsvzRFq5QUXHKt_MkrEKocA0L4wkbstwzGZFNciYfbrnpToCpbPwiUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🔥
سورپرایز دنیای هوش مصنوعی؛ قاتل جدید ‌Fable 5⁩ اومد!
‏مدل مرموزی که با نام مستعار Ox Alpha همه رو شگفت‌زده کرده بود، همون
‌GLM-5.3 Flash⁩
محصول شرکت چینی
‌Z.ai
⁩ از آب دراومد. کمپانی رسماً تأیید کرده و قول داده وزن‌های مدل رو همین امروز منتشر کنه
🚀
‏توی تست واقعی با ‌Cline⁩، هر دو مدل از پس باگ بر اومدن، اما Ox Alpha با مصرف یک سوم توکن و سرعتی خیره‌کننده‌، برنده بی‌‌چون ‌و چرای میدان شد
😎
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/ArchiveTell/7569" target="_blank">📅 17:32 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7568">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">عکس‌های داغونت رو تبدیل به شاهکار کن
✨
دیگه لازم نیست از عکس‌های بی‌کیفیت بگذری! نورون InvSR رو پیدا کردیم که هر پیکسل رو زنده می‌کنه، بهش عمق و جزئیات واقعی اضافه می‌کنه.
🔥
📦
نصب لوکال از
گیت‌هاب
🖥
آنلاین رو
Hugging Face
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7568" target="_blank">📅 15:04 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7567">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">Avast SecureLine VPN
4KAX6F-Q7LM6J-5LCJ6E
3N7RAW-SG38HJ-5LCJ7W
BJS8N3-NNAVTJ-5LCJZJ
J3BSAR-XJZR32-5LCJME
VUYR9T-JZ5GBJ-5LCJVN
23RWWJ-SEAQGJ-5LCJTN
GFU46H-QA2CDJ-5LCJBE
7SKUU3-S97Y42-5LCJD6
UENGEB-Y9NGA2-5LCJEE
EBF8PY-8CPH82-5LCJ6J
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/ArchiveTell/7567" target="_blank">📅 14:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7566">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P5Ei2K9e43zFoLfja0v-3YtqRcBKjzDyNSlN1VRmGFSdtlUNGs8enMGJ0VKzQrLob1u2PS-M2C_i-6VGdr7o_hXR_Na3tJMrAx9oI6FbHcZkr4dqlCewV_u71fNLAhEUpcw22FDo1Ul-IaXNy8_IW0_KgUwp8COXHbWvaLCFx4Uyjv90zJ5NaJnhAxLOqNtZKQ-BkbnSRhergnTHUEuInIkUR5xhU1Fdxy0KgRkgPamI8unUtcj7SZSfwVjic3-LWVMDR3kctyBD--5iNcms20Tv_Gz1uT7CaSGVvGRbin8sRJjHv_c9N5pAEMXbyN5rXjS3ZP3BkKj_891uSCrBbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">175 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | GPT 5.6 Sol | GLM 5.3 | Opus 4.8 | Deepseek V4 Flash
✅
برای فعال‌سازی فقط کافیه یک اکانت
گیت‌هاب
قدیمی داشته باشید و از طریق این
لینک
وارد شید
✅
🎁
با هر رفرال شما
100 دلار
و شخص دریافت کننده
175 دلار
دریافت می‌کند!
فقط در کلاینت های گفته شده در Docs میتوان API را استفاده کرد
‼️
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7566" target="_blank">📅 12:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7565">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/7565" target="_blank">📅 10:10 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7564">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t2OX7m2JTKlKwlio3CmUmtXDqkrogiJMEAQmtyc3iJOL2Uk53I97peN6m20rYcypicrwpmM1CdNP6e2985zm3ZpOajuOODIPobrOm8vf-Dg-Rj-xlqzJ0apJHijplqGnE6r9Otx3MkrlqmIe_U0sq8IcmkGwznMnrC78nSj-q030S7Gv34TYbcpBdg4sLLqUuoogFQh5vcvJkEsoFLUzLuVCWVrkX6X4H0VkuQsyxtNKywKnaANBUb2pkzkdUwQ4UmMOOygMeAUyEFCe2Wes_Lhuhtv6Gf4-eK3XXhPrTVW5QfgIJ6U0RUqObYE1OVPY2GyOGftv6vPVnuvwmjOjUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل‌های قدرتمند MiniMax M3 و M2.7 به مدت ۱۴ روز کاملاً رایگان و نامحدود روی GMI Cloud در دسترسه
⚠️
⚡️
📌
از
۲۴
اوت تا
۶
سپتامبر
🔥
همراه با
Speech 2.8
و
Music 3.0
🪧
دسترسی از طریق
API
خود
GMI
یا
OpenRouter
💎
بدون محدودیت استفاده
⛓
Link
🔝
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/ArchiveTell/7564" target="_blank">📅 18:51 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7563">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">📱
پروژه GhostGram (روح‌گرام)   همزاد هوش مصنوعی تلگرام شما که هیچ‌کس متوجه حضورش نمی‌شه!
🤖
تا حالا شده دلت بخواد اکانت تلگرامت اتوپایلوت بشه و درست مثل خودت (با لحن، شوخی‌ها و تیکه‌کلام‌های خودت) به پیوی‌ها و گروه‌ها جواب بده؟  پروژه «روح‌گرام» یک یوزربات…</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/ArchiveTell/7563" target="_blank">📅 13:29 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7560">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rm7Tu5qr0bWEu_i-n5ZlMd8FuFmBaoI-4B8oE3aclB5Gr8ZL-04Et8TDQBmeuPAIZ0GSmSiAmOvldUUF5uxsZCOXG5uM1613GbbnZ-tCZaUHxdR91WTGVsOYXuAYmt8ReHHCllKwXcbfShsmayH2LLb5o1C8pUIR_qqxDvQ0K3q33edpEqtJXpV8DkbIM3jgUtEZzmlFlhyK6OFtbFv9rVd5icwEkT4t8wZ9rb6yqserB63hbMk-n9PBP6o3vz5IdOF1gveKogOe0gyjQKsJdxc5qjGuIl2FrTXeVZUM7NPfeI7uT_Zwx_o_iAt8Lenl3pzxjhbQhAVU38JXbEfKlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API بسیاری از مدل ها مانند
💥
🆓
:
Gemini 3.7 Flash | Gemini 3.5 | Flash-Lite | Gemini 3.6 Flash | GPT-OSS 20B | NVIDIA Nemotron | Nano 9B V2 | NVIDIA Nemotron | Nano 12B V2 VL | Ling 3.0 Flash | North Mini Code
✅
📌
Base URL :
http://aihubmix.com/v1
🔗
لینک ثبت نام در سایت
🔗
لیست مدل های رایگان
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/7560" target="_blank">📅 23:28 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7559">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MKVZnA5GTH3jC9cqpbXZdlyVtD5X4ci9ey8Yy6hxHWLVQi0rokzOgvFjqC6QYA0IYr6IB6NyYzpVd0CD1YdYaQOIyR7L9-_nEHGxIubPsfn_F_xvDHXmbz72tZW8y9Zyr3mbM8k4sVt-JrWBbCvJPrrBGvhGb1M8SkY6V4n9GXao7ae5ksmLa7bM4S5cTEKeQlyn6ve4sADK_Ap61WByNLDriDjZ1x966R4pzwrBUiY1t5VZaCN-YvclgsailLsbRhS5wuohqzzXtMcBD7Vl0S85DUhoBxF0pR8Ys2qUVCU7kjTqD7dAjFnvGOFhfNbTx3QGG5i9JMfh7MyapyfoUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به برترین مدل های ساخت ویدیو
💥
🆓
Seedance 2.5 | Kling V3 | Minimax H3 | Seedance 2 | Seedance 2 fast | Happy Horser | Kling V3 Omni | Kling O1 | Q3 Pro Video | Q2 Pro Video
✅
با این سایت 1000 عدد کریدیت معادل 10 دلار برای دسترسی به مدل های بالا دریافت میکنید
🚀
✨
مراحل فعال‌سازی :
1️⃣
وارد
این سایت
بشید
2️⃣
پلن رایگان رو انتخاب کنید
3️⃣
با اکانت گیتهاب یا گوگل ثبت نام کنید
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/7559" target="_blank">📅 22:20 · 02 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
