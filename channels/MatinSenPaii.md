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
<img src="https://cdn1.telesco.pe/file/ZeXry-49a_8b481VFgm2jv5OIaEh35a7LCeQiVPKKisVD3koZsqUQxBK0CnMIXVhmC_yqAhbKNqCGIcOC5kKJjA0M4BKzi2hlRkHvBwUp_UCh5qO8nq3bJ9WJ46Ty4y2d5gE5rq7HB1S3vSA_QY34OQN3rVpEJnXUITHPioMMMAUTsACq88n10fN1XhcW3VHMUUGxQgUjJ2nuOH87C3zuHqyZ-Z7BC-LvuXcmrxu3U5qEXiWpbADUc9G6XZfnhEdX_OLURnK28Ag9wdYxNQcZFPURLCfyvSl1HQXlK-vqXyuaAuFxXl8Sm8_m6SlSDVFw42DnivRVayREbhtqSFyfA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 159K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPaiایمیل کاری: matinsp.job@gmail.com</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-14 19:13:36</div>
<hr>

<div class="tg-post" id="msg-4240">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">بالاخره کار مقدمات و آموزشا تمومه
کم کم توی ویدئوها میریم سمت ساختن پروژه‌های واقعی</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/MatinSenPaii/4240" target="_blank">📅 18:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4239">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vk_CkLElxwmVP5zCJIaqZEiFdL_61cGpyM6UTrDSwNtgj7_OCB7ZQVZVmBfztWVKzMrRWtgKOSUnO9N3ksSu83urZsKUxTrVnEKt7loK3cb0f_GiKg3eXaofEgdb_qcchOa1h092_xfNr1zq9Z4x-cre0lF37oiFZxblz30Jh8JHBDz6QkUtXO8oc35GfKFOP5k656gBpbic3XcGkilH5yCAUOsPF6_WMJieCIPPRYOyG-UpArixpGBHOQgLMroowLSj66DtuMkc9Vtdr5Eh0opG-q4NKYOoPb4vXZgMsF3Kz6aNzLgCnEeWAJoh_2dtUw7GEZ5WphevnAtvORGuiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز Hacker News رو چک کردم، یه سورس تو گیت‌هاب ترند شده که پرامپت‌ها و ساختار دقیقی که برای Design System با مدل Claude استفاده می‌شه رو افشا کرده. برای کسایی که می‌خوان از AI برای ساخت سریع UI کامپوننت‌های یکپارچه و سیستم‌دیزاین استفاده کنن، این ریپازیتوری عالیه. با دستور /learn بدیدش به هرمس و تمام.
گیتهاب پروژه:
https://github.com/Trystan-SA/claude-design-system-prompt
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/MatinSenPaii/4239" target="_blank">📅 17:49 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4237">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QjOc-sfGVIh3A5_PSqTAS4FJgB-Qc6rNcO88nFO9NHKip9h_pJ2Wn8SXBUXJVhW4b6R4aB0WXsGcu3uvD3_Nr32JefCeoNW7Wb_neM3NyJSy1MJiXQXgJRtEiUcR_paiSCujhryQg6z_mhJde2F1TC99OVHMdwl-oVk-51GqbRxa7gtgmm7lrvrl0XLxUSAFhKOZb73iufLvK0PgIIlJADkLBQAByHd_ri9zyDsXBCb64k1qM-cmHHt0BU94Q0PdmMS0Y9FvyVzxAf_gXcbX0YdBrjzg56FQ_-DEZQZ_qiGrzoPQACBDMjiG3p3wKq1xAij8UI8d50N_P2DwdliNvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ulYQjpulIYc8SXjQg8W6vAFcqUkSjdJUw4obumk0673CEzxqYnPJWCkAP0C4n_LcCRHUqdbCOR5KJt2gEyJyUzo2oanz5f_gjBAOXymzElrL0f9v9qXjpDHP1RIL-oE_Ari2P2CxuiJ6etVmxACW9NkuY5l22ptAauZUQLsxsL446OnV5UB0sZ1FCqtm1GADChSbD-jOj8pEDULAkwc8Eo-p3Q8vNhVBGUm9JoCWOv1EvmGh45gJQjBM4rQzCjdweGkr4sBCCo9u5WRQElDJs9rf8jXpOUBpLpcDU3gkP0LE5s8afjyUo3l1eQ95n_jG778V8AznKZD4Or8dQQruHA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یه سری از دوستان کامنت گذاشته بودنکه این api nara که پولیه و کردیت می‌خواد و فلان.
سایت Nara چندین تا مدل mimo داره
که همین الان یه اکانت جدید ساختم و مجدد تونستم با api key اش به mimo 2.5 وصل بشم
شما صد درصد از چیزی غیر از mimo 2.5 (mimo hermes , ...) استفاده کردید</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/MatinSenPaii/4237" target="_blank">📅 15:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4236">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Hermes-Commands-MatinSenPaii.txt</div>
  <div class="tg-doc-extra">7.3 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/4236" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">دستورات استفاده شده توی ویدئو، با توضیحات کامل
سایت ConEmu برای ترمینال:
https://github.com/ConEmu/ConEmu
سایت Nara برای API رایگان:
https://router.bynara.id</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/MatinSenPaii/4236" target="_blank">📅 04:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4235">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z-jBAwQej8LnN2rXgevtfv7DQExYE1Kft_w49xE_V2bKnd8WKNPaI_sGWFyo6Z3SbPoERyqzoFF07LRfaIKOcx5r7RL36G1f4pYkOv1CZnf6DCkvKWZaL7zhHNu2wMeI_mhhpfKBrNZTGLujnt7g4ARvmhe79ad3KAnwm2szCMvSTx8dOovVrkqqAbcRP07pC1NXPDRQaWpD_N9rvU2_NEe7P6393ugIRcCvQ8s1lQvSNv5RnnMVwGewuAYzRMCLgdJwikuBDrYF47qk3SEKags4jI5uvqxTFFfLnrLSmLz4iD3VDiaGZWNTCsHxz1g9Zl0vpMkRU4b6ckl2RFhDkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
مثل یه حرفه‌ای از Hermes استفاده کن! 47 دستور مخفی هرمس که باید یاد بگیری
⚡️
فایل خلاصه‌ی دستورات:
https://t.me/MatinSenPaii/4236
⭐️
چندتا از چیزهای باحالی که تو این ویدئو می‌بینید:
دستور
/learn
: با این دستور به هرمس یه داکیومنت یا سایت رو میدی، می‌خوندش و کامل یادش می‌گیره! دفعه بعد که سوال بپرسی از همون دیتایی که یاد گرفته بهت جواب میده. همینطور ازش یه Skill شخصی هم می‌سازه!
دستور
/goal
: یه هدف بلندمدت براش تعریف می‌کنی و اون توی کل پروسه‌ی توسعه یادش می‌مونه که باید به اون هدف پایبند باشه.
دستور
/snapshot
و
/rollback
: دقیقاً مثل سیو/لود کردن تو بازی‌ها. یه جای کار رو سیو می‌کنی، اگه هوش مصنوعی گند زد، با یه دکمه برمی‌گردی به قبل!
دستور
/yolo
: خاموش کردن ترمزهای امنیتی هرمس!
دستور
/suggestions
: اگه گیر کردی و نمی‌دونی قدم بعدی برای پروژه‌ات(یا زندگیت
😂
) چیه، اینو می‌زنی و خودش کارهای هوشمندانه‌ای که میشه انجام داد رو بهت پیشنهاد می‌ده
دستور
/moa
: ترکیب قدرت چندتا هوش مصنوعی با هم (Mixture of Agents) برای حل باگ‌های غیرممکن. با چندتا مدل موازی و یه مدل تهاجمی
دستور
/browser
و
/bg
: دور زدن محدودیت سرچ تمامی مرورگرها برای ایجنت با CDP (Chrome DevTools Protocol). این یکی فوق‌العادست
دستور
/pet
: این رو دیگه باید خودتون ببینید...
😂
بتمن رو تبدیل به ترمینال پت می‌کنیم
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
همه‌ی مراحل ساده‌ست و نیاز به پیش‌نیاز خاصی نداره. از api رایگان هم استفاده شده توی کل ویدئو. دو تا ویدئوی قبل رو دیده باشید، عالیه
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/MatinSenPaii/4235" target="_blank">📅 04:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4234">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">دانش و پیشرفت علمی، پیش از هر چیز، به پذیرش نیاز دارد. دنیای علم آن‌قدر گسترده و پیچیده است که با ورود به آن، با انبوهی از اطلاعات و دیدگاه‌ها روبه‌رو می‌شویم؛ دیدگاه‌هایی که گاهی با باورها و عقاید ما همسو نیستند. اما اگر ظرفیت پذیرش در ما وجود نداشته باشد،…</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/MatinSenPaii/4234" target="_blank">📅 02:11 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4233">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBloom.(Tin.)</strong></div>
<div class="tg-text">دانش و پیشرفت علمی، پیش از هر چیز، به پذیرش نیاز دارد. دنیای علم آن‌قدر گسترده و پیچیده است که با ورود به آن، با انبوهی از اطلاعات و دیدگاه‌ها روبه‌رو می‌شویم؛ دیدگاه‌هایی که گاهی با باورها و عقاید ما همسو نیستند.
اما اگر ظرفیت پذیرش در ما وجود نداشته باشد، توانایی درک حقیقت را نیز از دست می‌دهیم؛ به‌ویژه زمانی که حقیقت برخلاف باورهای ما باشد.
در نتیجه، از جایی که گاردهای شخصی و تعصبات وارد میدان می‌شوند، گفت‌وگوی علمی عملاً پایان می‌یابد. علم زمانی رشد می‌کند که ذهن، پیش از هر چیز، آماده شنیدن، اندیشیدن و پذیرش شواهد باشد.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/MatinSenPaii/4233" target="_blank">📅 00:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4232">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/509058c8eb.mp4?token=jzzYSGLGPXub-BaY8Mp-MZrWYCnAPfUgPyGUScBOtfWAQKr4-9j15zZXGDnQeIKQUH7IIiKGBmzc0oRaGmQomNecTaErrJA8bJcM2D-rOmegOXG13pojehjKOSccovXVPje4dqq_MHu5cgDiGLZrWGmg-ptQtuYe8n8uS1IQLYufCkCM20pdaepqPHbgmflRJu9aGoHxAGTBvNHNFcEHqfr3mgUFcI7RtopH6Fe41ew_sZL8x2RIIxCVi3Qlu9vw3HFnt7lj9L0PYiP_hPlehiQnWEgORkvqXcqbjUPBF4-t4Dwu-jPwWXq_IJRNLZ4hwLzu9qR9cIP3XTZB4kNVHg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/509058c8eb.mp4?token=jzzYSGLGPXub-BaY8Mp-MZrWYCnAPfUgPyGUScBOtfWAQKr4-9j15zZXGDnQeIKQUH7IIiKGBmzc0oRaGmQomNecTaErrJA8bJcM2D-rOmegOXG13pojehjKOSccovXVPje4dqq_MHu5cgDiGLZrWGmg-ptQtuYe8n8uS1IQLYufCkCM20pdaepqPHbgmflRJu9aGoHxAGTBvNHNFcEHqfr3mgUFcI7RtopH6Fe41ew_sZL8x2RIIxCVi3Qlu9vw3HFnt7lj9L0PYiP_hPlehiQnWEgORkvqXcqbjUPBF4-t4Dwu-jPwWXq_IJRNLZ4hwLzu9qR9cIP3XTZB4kNVHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاید براتون عجیب باشه ولی من خوشم میاد وسط ویدئو به ارور بخورم و بهتون نشون بدم که ارور ترس نداره و میشه خیلی راحت، راه جایگزین پیدا کرد
👍</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/MatinSenPaii/4232" target="_blank">📅 23:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4231">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sDrDjDZMcEHX14JoODM9-uPmNh9oR57WKbzD2eHEeSZ4lslcPoP7ph5G1bYZgn-nM_M3aYdvOVzaC_DmEybvNm5zHoDjSDAX9OAhD49w7dxePOPuvFjPSC5J06xU6jLgbajqRB_h9OmAhjMMAfiOS3b9_wvB7Prxij1uQ_KW5dB09U0yzvo5WDBpki5tB6YVZnctb3I1s33AP4_KGyDB1h0Nrh1iSUd0Vnqcy57-DkWHFMjHBXm8sltX0X7W4-K8llKQyA9PzeGhQ198UihZqNFUuesroTwN8Z99L5qlacfUc_Dq4uPOlGkM-bJYaB2dz9nUZmdVwVoDY5b1-UX3Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر، قابلیت Deploy کردن پروژه‌ی جدید رو برای اکانت‌هایی که با سرویس ایمیل‌هایی مثل Atomic mail ساخته شدن، غیرفعال کرده.  با جیمیل اکانت بسازید موقتا. شاید پرووایدر دیگه‌ای تونستم پیدا کنم که راحت بشه ایمیل ساخت که کلودفلر گیر نده</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/MatinSenPaii/4231" target="_blank">📅 23:25 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4230">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oEb8Y4MmjjLrwQL7YFm92Kc1yidckN2QERDn90XweCtXIQD0gZaOOgC9h1iLXcT5v4lcu3xg5yHv_zQ6TXBd_AOgz_mdBI9-hlig7VZ_lOkq52liBzlTN_LijZIW6VxVxVEl06G5ivMbveroT7cNBa5Qo9b144TzP7YJEBeah5WlzZXKzGtNEyonG3qeBFv-gl3UO7AK-hxv8nlvruHCb1Rv71CQ1ifvD5Cuqq2M_EGJCCyC-c5_mNnPIcZdVMItY634h_CzCho-xosYRNwY2gPR0-abOOcc3xIqk7roi0KDxj4xB2spVrti8f5ATURfq1E1SOrkm2okYxiI3faXRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر، قابلیت Deploy کردن پروژه‌ی جدید رو برای اکانت‌هایی که با سرویس ایمیل‌هایی مثل Atomic mail ساخته شدن، غیرفعال کرده.
با جیمیل اکانت بسازید موقتا. شاید پرووایدر دیگه‌ای تونستم پیدا کنم که راحت بشه ایمیل ساخت که کلودفلر گیر نده</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/MatinSenPaii/4230" target="_blank">📅 22:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4229">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">روش فارسی نوشتن درست و حسابی بدون به هم ریختگی هم توی ترمینال یاد میدم توی ویدئو. که یکی از دوستان عزیز توییتری دیشب بهم یاد دادن</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/MatinSenPaii/4229" target="_blank">📅 21:06 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4228">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">توی این ویدئو که دارم ادیتش میکنم، کلا با cli پیش رفتیم و از اپ دسکتاپ استفاده نکردم برای هرمس. علتش هم اینه که پروایدر شخصی اضافه کردن روش هنوز داستان داره و محیطش پر از باگه همچنان. با اینکه آپدیت هم کردم الان هنوز همونه</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/MatinSenPaii/4228" target="_blank">📅 21:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4227">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🛡
آموزش کامل نصب و راه‌اندازی سرویس MTProto با ابزار MTProxy  فیلترشکن قوی و پرسرعت برای تلگرام    https://www.youtube.com/watch?v=pyvB6VSPhwg   @WhiteDNS</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/MatinSenPaii/4227" target="_blank">📅 20:54 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4226">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🛡
آموزش کامل نصب و راه‌اندازی سرویس MTProto با ابزار MTProxy
فیلترشکن قوی و پرسرعت برای تلگرام
https://www.youtube.com/watch?v=pyvB6VSPhwg
@WhiteDNS</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/MatinSenPaii/4226" target="_blank">📅 20:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4220">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/orIWqIMWiVmP1_ywP863xKIvbPOQRlCutRQ2XTbGgVYGqoG5Z_wYpYTKf9ZF6BUw-UG_wiL0dGvwIBUR98AkSauFW0pk_Cu7sNx9uTpDtwufdQTMLU0wuiw6CqvgQr9xqV-CD1FuwWw1KMpiXaRzKkzfN-oO-Fx2gsDpwzX3oXNd9IayJb5InBQhZlF6bs76mZFNDr3yBm_9RpNxdBlyD-1UjobY1jvr6C0eZlL5PtHqmRZokG27bcRv2WHahn-tqgjg6tfuvFKrb9IcCQ9VU661KLal8ndmCVVnPm4NwZwqxjKP2r0AAnqFdU7oi-4QDb3p_eRxFOOzfyt4KB16Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TzhguowwV4y4hc9M_ywXbVWeOfRS6rtG4UUKLbYicxOeJmlQCvaVDWvj1Rd79ItGYXzmBjYiCRfLEaaGAdYjXhF0rcRXNeIHSXQU7U782Gji9kYtKPo1CIgjjIMyWj0PrsYX8WintBq2K46U0meYqelKO_Pu2bF3Oi2sakMznw2VMz3LdrqYDKbwlHGMkznqMTjlwJ00Pv9MX6UChVD8kUwh1zM9wxhpqsRT07sZ4HtZ0OScU63zPSRfjufLbmqtC5JPwaYOiB7StHtqThjQiWWkdw09oJN2dS3-hS6sUAx2sxBFk2mepP0I9vPOPxpL9elTWLAazISxKbNwIW4vDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aWbNDsJ9fiyx4Cc_y--ZZG5FXpJMc4zoJqYcyFpFZYcDFQdNcS6_H-YY8SC1QRy5FC1Ybd15ixrB9_1-AleW43LZG-3NNCeloMlqUY5lUkvdrLWnJufM1gGtnaIMRmmhBrXvyOCfgUUBN2ea3lsWqQFjqw1x8_yGGoIZ93tGhSSpgXnf0m3nyRNrjiaC5cA9bjbQ85Xxo8B5KtZwRcBJcisY7GkvVglR-aHQ6lp0BwyBj-5qutxEsVc_-ZBIktQDi86vkIgz5qovR216Dcem4O1xiNL2V074q7CUl42cEKRPFgjjlJC1wMwJdOp_V5_v5P4PdcgG1lY7kFaMTHZK8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Q1o8BjXYEXXbEs-5dhRrGBTIfujSkNJo9gjEwVmKWOA20CgkxaXxNc2Ys2kPh4QvjdYMjyxrjN3PX9kPuJX4rzS_dSS3K_lNkSVDSm5y4CKYgI1HmQUwimWkCqkkSNmcWa8XLSY4k6H_boIWfsZnlpr16-KzBWnfav8kxFBZrA0UwHMho1OzYAMoFUQQfUYzH9J3LhjvSrnEo6fZbn2HFHChHkzx6e0i4NPL4SAKspmwhr8TRH5XfKidwTqR6Y3lWeOXhho6SqyakjVAOjxjK7K7WzKRf6qxCvcGn8qz2CIW2DjIooe0FXHOZi2EjevHiAvwWOY4FuH-4POZx8sJFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fRDWT9gytCbonO_ru8R8pjSmjYMGH560f-la2VCTLfndpREBAdmon35fFYP-BuqopcTo6QJEdaCG-cjHp3DRmsiak8sjdeV1fE7vFsRwe9346hUCh-1Fd-O5gSffYLiIQTGzcR8vJS7Q5wtM0eCnP4x_QYaA0T8ZcD-9cZTJM5qR6002qFtErmrQOfGJ9aeQeTmSEBVWv15l0w9QA1vH-Fc4gKdSI6wGjmifCofRy9_WK0UyqIt1i5hNHHhvcUy7iHRT3gKu7tRzYKkaAbAfqgRnfsQgS0kLgl86bHHhez-1cSFVPMtu-yL-BrzPwRxysS6JAZG4HziCAmE9AmV7qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ihsa68s682InKES1crNTEucDqb60BSNM4eO7vwGdzXU-nSGtvpPyEhY-9cxra9xWs5Tqpikx8TAKdpmShyRQV_d50DplW3hcBSkXgkMAfhc244fg3T1InuO6i_KX3yE1HM9tTwjywBE77tbQNqTiY-sq7RPJlXziDWKvuYGtII71MCPejdwfn89Z3iSW9Djm7O6hkyvZNPwnLBx7LpaJZox7VYTyHC9OOzJYrsaIs37jlq-i_4-QoiVRWcD1TLkpBJu5PmeOLZJHsx9-IV_7PJSuBZX1Odl4ggRT9M1Jw61sEVI4ARpmCHRCa5A5Myx-IfLweY-_Az4Oa1I-HS8HiQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">راجب این هایپی که در مورد «ادیت ویدئوی بلند با هوش مصنوعی» راه افتاده چندتا نکته می‌گم و دانشم رو از ۵-۶ تا ویدئویی که تا الان دیدم باهاتون به اشتراک می‌ذارم:  1- نه. اگر دنبال جواب مستقیم و سر راست هستید، هنوز نه. هنوز توانایی این رو نداره که با هزینه‌ی کم،…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/MatinSenPaii/4220" target="_blank">📅 20:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4219">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DSjlURaa5CLJN4TRI2s3fr31pUvfI9sQV6lPgaD9PKX3mu234wCB_PBErtB10Hv44qocpfXe8Bo6mf_WtY8TdoZWZVlYqHD6djj9OfP6BRDODyCvcegsBqpbgbsvcRxKKtLglmsiFjcoSsCVTiPlskRf2W3MIOm1KIyH_t0yL6MRS-pZXbqJwzn4GK2wssSyiqS9SJ9NexnMyzwPHNFjE6NZpnYARlOSLpri5cV7pU8kt6osghI1qs0x-GFypCoNInPE-bjz8m2jf9MqnnD-P5qKXxmuiAwdG2oHsJFeus9DkEp2MD454Hg8TIrOO9D4-s_osjzjMLLMDlGjCqbuRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راجب این هایپی که در مورد «ادیت ویدئوی بلند با هوش مصنوعی» راه افتاده چندتا نکته می‌گم و دانشم رو از ۵-۶ تا ویدئویی که تا الان دیدم باهاتون به اشتراک می‌ذارم:
1- نه. اگر دنبال جواب مستقیم و سر راست هستید، هنوز نه. هنوز توانایی این رو نداره که با هزینه‌ی کم، بدون اعصاب‌خوردی و بدون زمان زیاد اون کاری که ما می‌خوایم رو انجام بده.
2- چیزی که من از ویدئوهای این دوستان عزیزمون فهمیدم توی یوتوب، اینه که میان با مدل Whisper و یه انجین شروع می‌کنن به کات زدن(که همون هم پر از اشکاله و نیاز به ادیت فراوان داره) و بعدش شروع می‌کنه با یه سری mcp و یا پلاگین کلاد کد که اونها هم اکثرا نیاز به api key پولی یا اشتراک دارن(کما اینکه خود کلاد کد هم نیاز به اشتراک داره) یا یه سری ها هم با Hyperframe، واستون موشن گرافیک می‌ذارن.
3- حتی همین موشن گرافیک‌ها و... هم باید قشنگ و دقیق بهش پرامپت بدید. این نیست که خودش متوجه بشه و این کار رو بکنه. همینطور توی این ویدئویی که تام‌نیلش رو گذاشتم، طرف برمیداره کلاد کد رو اگر درست یادم باشه با Opus 4.8 می‌ذاره روی Extera High effort که خب توکن بسیار زیادی هم می‌بره و فقط ۴۸ ثانیه‌ی اول ویدئو رو باهاش ادیت می‌زنه(بقیه‌اش رو داده ادیتورش
😂
خب مرد حسابی، واقعیت رو بگو دیگه. که مابقی ویدئو رو دادی ادیتور خودت ادیت بزنه)
4- هایپ اطراف برنامه‌نویسی هم زیاد بود، و تا حدودی تبدیل به واقعیت شد و الان ai سرعت برنامه‌نویسی رو بیشتر کرده. پس شاید بتونیم انتظار داشته باشیم توی آینده‌ی نزدیک، با هزینه‌ی کم و یه اشتراک معقول، زحمت ادیت رو از روی دوش ادیتورها برداره. ولی جایگزینی رو بعید می‌دونم</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/MatinSenPaii/4219" target="_blank">📅 19:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4218">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">کاربردش می‌تونه اینا باشه:
۱- وقتی دوست دارید هر چیزی رو بگید و در لحظه کامپیوترتون تایپ کنه
۲- یه ایجنت لایو با Hermes بسازید
۳- و کلا کاربرد عمومی. مخصوصا برای کسایی که disability حرکتی دارن و مثل خودم توان تایپ کردن زیاد رو ندارن</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/MatinSenPaii/4218" target="_blank">📅 19:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4217">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">چند روزه می‌بینم همه دارن در مورد whisper حرف میزنن. خواستم بگم یه ساله برای تبدیل گفتار به متن از Handy استفاده می‌کنم و واقعاً بی‌رقیبه. کاملاً آفلاین با پشتیبانی دقیق از فارسی. حرف زدن با کامپیوترو خیلی ساده می‌کنه. github.com/cjpais/handy‎  فقط کافیه شورتکات…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/MatinSenPaii/4217" target="_blank">📅 18:57 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4216">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IQcOZ6Uxr3AuUSwZytk5ICysJhpL9dav2M71l58sYoItqOIUVXqaOdzDahgU_Vrnd_n7S4_nvfrCRufbaoAOgZmG1wdTK26iY-Pp29brJxR3SPjh7qGFWLfO7Zuhzk5LhAu9D6SDbAX5Wn2-hnQCWZluYxbEHrosUrFYEx3Iju9sosx6N23RXDXdQ76ERWlknQ1nNPs2cRST2saCHjbB7nykQwhk9Hs92N0hZwlgk9XHYjcbdtYR_gVQ5O5SLd0hmPr-N3SVHQTks9diGFsN_xs7isPmw8PjLxhEWVwX2hbh_7dsYtmKhOcMl3vKYLISOiSgnU51kwAhB6rw-Cl0zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چند روزه می‌بینم همه دارن در مورد whisper حرف میزنن. خواستم بگم یه ساله برای تبدیل گفتار به متن از Handy استفاده می‌کنم و واقعاً بی‌رقیبه.
کاملاً آفلاین با پشتیبانی دقیق از فارسی. حرف زدن با کامپیوترو خیلی ساده می‌کنه.
github.com/cjpais/handy
‎
فقط کافیه شورتکات رو نگه‌ دارید، صحبت کنید و رها کنید تا براتون تایپ کنه.
اگر دنبال یه ابزار STT بی‌دردسر و رایگان برای لینوکس، مک یا ویندوز هستید، حتماً تستش کنید.
✍️
apt_hq</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/MatinSenPaii/4216" target="_blank">📅 18:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4215">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/so8ySR3z6b8a9UBo0ZQx-ugS7DnrrLXEm5RKLSP9XsXydEWJP6QTmK97BJdNBFjVuGsWfSz9uAskGsEeNvcXNyQr8a0coZul-HS_2e4O-fz5Qf_cLiUH3wTgrRYjvUzFcg2s7QAmCzJaTPEfeDOEkQSHofYExunnHlKaLMeR3X70_nkQx6a8fupKimonXse7pbXxFlo3osY9qHprsEyEqADm4WTK-cnZ9yJFux50W_tZQcXGXq2Dku-KIhyslfsMczO_IAS-vrIrqNr93DjZiImZFR4eRukxhZRlQb57wWH-VGx2SR8gV-nNymRi00gii3M_Fyy6FNU8l8vcMTxsHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا به دادم برسه
3 ساعت و نیم شد ضبطش
😭
😭
از بس دستورات هرمس زیاد بود یا طول میکشید(کل ویدئو رو با api رایگان رفتم بدون سرور و... و واقعا هم خوب بود) و قلق داشت انقد شد
اما ادیتش کنم ۲۰-۳۰ دقیقه بیشتر نمیشه</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/MatinSenPaii/4215" target="_blank">📅 17:36 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4214">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">برای مثال کیوریتور (Curator) که توی ویدئو توضیحش میدم، یه جورایی کتابدار هرمسه که تو پس‌زمینه سیستم بی‌سروصدا کار می‌کنه.
و Skill هایی که خیلی وقته استفاده نکردید رو پیدا می‌کنه و آرشیو می‌کنه تا سیستم سنگین نشه.
ویدئو پره از اینجور دستورات و همه رو هم تک به تک انجام میدم و تست میکنم و صرفا روخوانی نیست</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/4214" target="_blank">📅 16:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4213">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">هرمس قشنگ یه کارمند تمام وقته. ویدئویی که تا آخر شب می‌ذارم رو حتما ببینید، تا بتونید از تمام پتانسیلش استفاده کنید</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/4213" target="_blank">📅 16:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4212">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">به زودی یه ویدئو داریم برای تمام دستورات ریز و درشت Hermes</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/4212" target="_blank">📅 12:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4211">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">به زودی یه ویدئو داریم برای تمام دستورات ریز و درشت Hermes</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/4211" target="_blank">📅 12:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4210">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dXPP6ZknaQLsXm4JHOl7Wbo4Ki7bTYGVYGJQoU_axv2vduJU604B7p4Ql5Si9wgfl34i1-hN4LxKXeB1FwRKLt8grmwB-is7AbFYUvaFyXBIG4pzVFEiR6vEWa6pEPewcCBYzKrRmib6fURiuZXM0ZJRKhjz_e7CvMrU95qdJZxBxW8rtGUdjHCzrvFOZDhdtwDR2MgewP7nYGpBz0A7Gn-CXAxQQucXS03ehF6QTpZqL2h_2s-QplAzglgIG-E7z0NhewXZlFABiZ-Zmnew8YbShi-OgBJzcm--DBVGrCIv4A9GcMht3gJbx2nKESTxgnEqGSYilP8tBtArQOyz-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این داستان، ایرانی بودن</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/MatinSenPaii/4210" target="_blank">📅 01:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4207">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RMSSqCNStpA-VNiXG-F0eH4OPZKoAQJFgEtSP5SvnMDr6yHbkQXA1GvisWjzzCosOGyjHjAJt8qz09Bg3IkHam4qEZhK-i7IOX1cPukhaiJ9YTEcFyziHovwwjGmWcFaAQSmR7MNrPHGgdbCCe6B8nFWJ5jZMvGxUmGMsXMpArhchfotJ-7Y3mzS3YAdCt79IBx0MvWjj2ijFTJ3yIZ5mThfOFDsdbajFsjoLm956nTKDjhSuHq6cpv6m4i5idJw22atYAcx-jJn_n6djIprVBMAcNT7sca2uO3m6bpKYsOU4aJexXAyxgEMOzv_bw5b0tml-mF9yzUZkd6u9UXsLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tSvgLMCKPW7eRKg9wKmC7U1AL-Irz65FFC5Ka4wa30nLX9R-k5dIYcBv3ZidQvsg5iQL0xg1sw4zXQDWg7EjEUZ31ZHLjs3_qVpL92nfRmOAUzWsVRIgOjkQUN_jmaMx0v0z3LCvMeVCVeAckUWVZ5y6PJLUGB1Ko10HSLFZPPdKQynxksShlCIn5b5K_z3ahEwpfOzB_E_eU-1KaqWgF7dzSwfB6ZIyinCI-y1aMlIdY-hopO062jXPKyhLQg-_doAZLvWYQY-z2jP7go-GYMXFK0dHi7YUcgHEcBD4nHguzBfObTxUZ1CbJuT9QRYmT5bJI9TX-_CEyicw2tGtNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vaZWlMpYKkzNwaZUf3ZemM1dmc47SDdTrGDDqqw1gJW5N2jbrTMjHn97oc5LwikdHd_q6ZLaJAinHtbMkqYJSYiO7ADgpiYHzMtSn0DOYXXQFYC8EtYr2u2W3-xfxUOASi0rAqoQpeI00GYSQ-AvGrgWS49KmOQCrSUn05g3NJWIMltre5N1x6nSFz3IxReW35WEJdn38FIw0Ddx_K1Rr2KotNczCZjkqvNv_8x3LVX3FqkExGJ5tbjF2tYSPsHtf1cLJE5GRplen3c_AR1-GMvr3vkKU-2RrucesSsIPrIB519dCt1_hYRsuNUKNmy55JqoZ6ZsR6m7sq6vV5G93w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">توی Hermes اگر از دستور Compress استفاده کنید، به صورت دستی زمینه گفتگو رو فشرده می‌کنه و چیزهای به درد نخور رو حذف می‌کنه. هرچند خودش وقتی توی هر Session به 50 درصد ظرفیت برسه این کار رو انجام میده، ولی تأثیرش روی توکن مصرفی خیلی زیاده! همونطور که توی عکس دوم می‌بینید
💪
/compress
—> فشرده‌سازی معمولی کل تاریخچه.
/compress here
[N] —> فقط تا قبل از N پیام اخیر رو فشرده می‌کنه (N پیش‌فرض ۲). پیام‌های اخیر کاملاً دست‌نخورده می‌مونن (وقتی می‌خواید مرز فشرده‌سازی رو خودتون کنترل کنید).
/compress [موضوع خاص]
—> مثلاً /compress database schema — خلاصه‌کننده اولویت رو می‌ده به موضوع خاص (مثل schema دیتابیس) و بقیه چیزها رو یه خورده شدیدتر خلاصه می‌کنه. و محوریت حافظه‌ی Session حول همون موضوعی که گفتید می‌چرخه.
حالا شاید سؤال پیش بیاد، که متین آیا این قضیه، کاری به اون حافظه‌ی بلند مدت و حلقه‌ی یادگیری خود هرمس نداره؟
✉️
باید بگم که اتفاقا چرا. هرمس قبل از فشرده‌سازی، memory flush انجام می‌ده تا اطلاعات مهم از دست نره و توی حافظه‌ی بلند مدتش ذخیره می‌کنه. و این شکلیه که چیزی از قلم نمیفته!</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/MatinSenPaii/4207" target="_blank">📅 01:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4206">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56bbdb4680.mp4?token=jwHwC6XfoH7uZBb9cRgGlwjFm-tCnpp2Y5xlALZ1GuOESd2-0JhSd3S17qQKDWGK8kWukX68sohwHsa5Ro_TID5eqx8HeQpfclfPwmrPzRZ4nvqOpQ8DptkF5WkLTBUcfafW059oQrz_meVUK5PmDRdSypEp9uIxa_pzjYJZtg3hCllpQtsCbUUtThpdaeAFcOj0WqAD-ivTz0kD4kSmLEPrVpRmE_tf6_D1wkrsrYq_4e_6xaCE9ZbsbJOBTiqqNNiou4cwJs9ttgtdSWYWLi7j4q-UxtBzfGt-i-IcJUsrfvHtblzcur0K6YL_4vKkIu7tMVbqAbFHCJvO5fOjKoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56bbdb4680.mp4?token=jwHwC6XfoH7uZBb9cRgGlwjFm-tCnpp2Y5xlALZ1GuOESd2-0JhSd3S17qQKDWGK8kWukX68sohwHsa5Ro_TID5eqx8HeQpfclfPwmrPzRZ4nvqOpQ8DptkF5WkLTBUcfafW059oQrz_meVUK5PmDRdSypEp9uIxa_pzjYJZtg3hCllpQtsCbUUtThpdaeAFcOj0WqAD-ivTz0kD4kSmLEPrVpRmE_tf6_D1wkrsrYq_4e_6xaCE9ZbsbJOBTiqqNNiou4cwJs9ttgtdSWYWLi7j4q-UxtBzfGt-i-IcJUsrfvHtblzcur0K6YL_4vKkIu7tMVbqAbFHCJvO5fOjKoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بی نهایت آدرس ایمیل با یک دامنه روی کلودفلر:
https://youtu.be/Z069VNFAgAc</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/4206" target="_blank">📅 19:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4205">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">خب دوستان GLM 5.2 اومد روی Nvidia وقت استفاده‌ست
👋</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/4205" target="_blank">📅 19:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4204">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lHLq3U7wbE92hOCOPm3A4wgSxPLy3ILkCQDXcdzr4DTx6TJWee5i0wGU0BfU249gnNYjNycJybToA4MNRWVf80sj8eu_eSfLRXOkegoXrtiI2Z5fS213iFHOp9aAkCNtGJp4hSq2bdyfib2fpNi_mxRgB6MILA-LuLLvqYpkv8N0Em-BKD9hc7V0X-Qlw0OTaZ4tJu2zOZ8xtxB7vleThgdPT_nL6Ra5KSjeyHM4Axpg-CykzUJ5GrBEqq1AoWeHy-lgwjvtEAYImtw3jGnhyD3B_KQIgt-3KKeM3sqo6oi5PswL2MF12WPcKuQFdSHeNeM8iNDd9QXucLF7dJQI_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب دوستان GLM 5.2 اومد روی Nvidia
وقت استفاده‌ست
👋</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/4204" target="_blank">📅 17:09 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4202">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/meitaJZfy7ejZn9uVGohQUlKG9oxMNCYrmkY_uL8sD7V5EGj5lz6glg5t4Yaw-TU9w5iK-5rELsWXHO8uBotbt6tJlKhhAXsZZtxmW9HKUC57OdmoH9utZCg0YTGkjk6tKUt50Yp3KtZccyc-QTKo9mwpXlKkTDFiYlsvjnpY5fYbqGEtUshAGyHhTTIriJLda6kFUeyCK5xM1n5fES1zvR9YpG6nwLqH5Kcyxd-3OT0-cGM7kQLo0SyyLDUh3x6X5zN7t8F4tKbKkl8S8AJYWuBzXnEV2oGkp6ZZtl1czxquSd8G2c3xZNdX_qICI6bOsxdmmn_E44QXrBSKkT2mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GOwzoi1MLESTZTh9svUwVahHjz_5qPjUD1E1ZFiGtlzSKoKO-xLp9VBJR53EQZaceakkiyvBlL2s13pGStn8t__Y_ny9WJuRq4Dc542aeh8-dDqY_LiksVPnhCdNKg5bINXDvyxKA7vlqCQ_wEHnr-mrK2bExP5yD4SV6BwNk_ymtu0PWGwAhWFOQSUdz36gLTYjimK7euAOOI5tQ0_Bf_Ep_Ad-3sl58NnfqN5BntxFRiAlNqdhgb97HuvnVKrmgM3Vzn6qpqcY6Y5D-GWWGcqcJJyQKHXncePY1wZy-AEJZjTZKSmTjcG3rt-0zjZWx5H4dtEpAF-1XkVrTtxxoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">چیز بامزه‌ای نوشت اما پر باگ. دیشب GLM 5.2 برام دومی رو نوشته بود که کار می‌کرد همینو الان با sonnet-5 هم تست میکنم</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/4202" target="_blank">📅 17:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4200">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jQzpRtJjigCrXyQh2_OFka5h1mBXDw9aRkG7733y1uuyweYeVDz2cYx3Fdm5mD-F0YgX2RJdziQtDP4Q3ZgjmSrySBQqBGoVybqQLCnU8MmkrMeFg30vML1yZ3UJxxBoczzDlHKgsIoTLNMEVF-iKxSyH0TD9ebgAw3_owj2jgFBL42dsSycael3EDKmDki4Ht0vgwmUxZ5xKIgN7zWjdeAL6tM4EXNrICropIuzbvcaD_lBrPtMx-8WBMeZDi59C1_nBSqQDvr3ktVXIbdj-1cWiz2OLwqVDFOw3_7EciyI-gT6XFuWa_nmToFTcSP2epsr-QtsgoRiS0wDrAKIxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aE6ye_x4OzdPsSXgcpzetHPE6kLikFw4XE8Ay2l5wg2-3DHEuKdICqSx1GpFjzYpKgYm67L5MtV5ivrH7E8qwb-JOQjt1XWUTCeEspILcp0ah6C0ILy5M7Org-4fUIiA36qCPq0xEvlz2pCm-HS1kqgHb3b7ljkvor6hJXP5K0oR716Sn9THdYIH82MQpPs7KGywoMLv6XSglTFl0xQHMrQq_gNTzSaFQ5olYlx9cU-ylwE1KDR8d2q0thaAP9or5b3lxP2VVtEXaNOkuv5wZmuRURV-ws3PJcLutqbd37s8Q9aet8pPIeVsir4WsgY-aVasqUWY2hhD_3uL67S68A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بریم ببینم با یه تسک گنگ و غلط غلوط چیکار میکنه</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/4200" target="_blank">📅 16:52 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4199">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RZigGfIxOZhWLSPZQPQI1Tt4l7HmGSmZIId6iMuv_2-lrP5olTswqnQFzG3vTsEi7ZuNHMfn8cUT9-HLZ3LR_MjIP6HyHwWOXzv69ItaDujisEsyYafUW3RaK7O7FOUrlz5A_FUub9rI525MQJnqqNFQ-ORmGj_P1z--7HGYPF73pQ8iNxWAFyKWWH5rPapkTN0uiKUfMI6yEMOpEJ9BXC74Qmbp5kvPiUHmI3mSOwmdym-bgBuAlCrlpdWI5TjJ99_RUf4I5HtlJ6Xo7XyYgPyIK5JDDSrlCu2aa659GsbrG6Q_o6er8HZ60IqqvqcJ77-MO0g3gXB2uYAO9TigjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مثلا هیچ فعالیت روزمره ی معمولی غیر تخصصی و تاحدی تخصصی ای نیست که با chat.qwen.ai نتونی انجامش بدی و نیاز به خرید اشتراک chatgpt یا claude یا gemini داشته باشی. البته دارم تواضع به خرج میدم و میگم که qwen صرفا از پس کارای معمولی برمیاد! برای سرویسی که میتونه…</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/4199" target="_blank">📅 16:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4198">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HLGzCZWe4EOJUwWpYnIcKbbK8fjM-sLtTOvoBGx941NgUDz0zzmO-8366O1HcjP23MoxjcCiX_YSQsuJCcR2A5gPPRTw4QrMP1mKZkVdA5HxYUWNcOYcK4Su65QoXluFh-TjytbpyYfy3R-Wi-eOr5YnWzBeykVB_690qgzG4bFSzb9MVYVp76jKipUWAf6bkMKdza9lTOri3B9O_bHMToFLQHQknYC5vyQIx29HQGbaSg8j7DEmrnAtMMyd6Jw85cdG_RAjOr3zpFtqh5eoUIfL4EisTNGDTtvsGOwgBcaFi7yK8aM3LJA6tltgmVSyeCERiigzVttKhflb6rMGMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مثلا هیچ فعالیت روزمره ی معمولی غیر تخصصی و تاحدی تخصصی ای نیست که با
chat.qwen.ai
نتونی انجامش بدی و نیاز به خرید اشتراک chatgpt یا claude یا gemini داشته باشی. البته دارم تواضع به خرج میدم و میگم که qwen صرفا از پس کارای معمولی برمیاد! برای سرویسی که میتونه پروژه بسازه، مموری زیاد داره، عکس میسازه، فیلم میسازه، ریزنینگ قوی داره و برای هر سوالت یه لشکر ایجنت بسیج میکنه استفاده از واژه غیرتخصصی تحقیرآمیزه.
✍️
بوکانت</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/4198" target="_blank">📅 16:36 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4197">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">توی مدلهای چینی طبق تجربه‌ای که روی هرمس داشتم، MiniMax m3 خیلی بهتر از Kimi 2.6 کار کرد واسم روی api انویدیا</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/4197" target="_blank">📅 16:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4196">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">به قول یکی از بچه‌ها هر روز جوری با Claude کار می‌کنم که انگار روز آخرمه</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/4196" target="_blank">📅 14:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4195">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">اگر ZCode رو نصب کنید(با Zed Code فرق میکنه) می‌تونید روزانه 3 میلیون توکن رایگان GLM-5.2 و دو میلیون توکن GLM-5 Turbo بگیرید با یه محیط کدنویسی تمیز شبیه به Codex با هر ایمیل هم می‌تونید یه اکانت بسازید و... بله خلاصه
🥰
اینم لینک نصبش: https://zcode.z.ai/en/docs/install</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/4195" target="_blank">📅 13:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4194">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/adlrJdfaNLvNDjNYv03cGfAunZyDF_Ze3xL5-dkZMIDhQXvAi5WOha6CwP7QxdGY7v_pwQi1D4YPp8rp8kLWqfzO-q1LI45TK-FaPuJIfN6iRzpHhHCKtSWszT1bgnfCwfh1XfjJ9dCRYXtC0wy4EPmKCEZCjVTp-_mhk4NHgS0hwJF6WMnyAyhFWItz2Qp7ABvcdILBBp1brVl_L7Hm-2YEqW79fWwdmS8kfM7hXA-gdTN6ztgKxyFt3CwyCtt_Eu_H71jZnnqyZMqVR31NiLvO_-vRbtx2XQct6r9tcAfcHRgp4IXvPJEvO0gL5Sbxozu-5BC_Y2YqeGMI9UNaGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر ZCode رو نصب کنید(با Zed Code فرق میکنه) می‌تونید روزانه 3 میلیون توکن رایگان GLM-5.2 و دو میلیون توکن GLM-5 Turbo بگیرید با یه محیط کدنویسی تمیز شبیه به Codex با هر ایمیل هم می‌تونید یه اکانت بسازید و... بله خلاصه
🥰
اینم لینک نصبش: https://zcode.z.ai/en/docs/install</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/MatinSenPaii/4194" target="_blank">📅 00:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4193">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ar2SsTAjYovaaisy4Gig2KgqnS6yJKuZZnp0iJqFVgxQzV9DUfP0w2QP7q8w9pz-q0EJi2s_oyMAoC2pjAK1cO8lKdM41oJlkp4qGChuNTJuspV37wFWBsXmy8-pGLAUN3AyU-lxaof3nqd5wXC_lNZ6I_E6TKVa69f4Z-8Gn3cBekXfsFa2Bp2K1pAG7jhEqGDgVfgn4DogbjwhNhaalogCij-iHQRwH4V3QmNX5rlxuyhx4w3PyDW5MYD5k0-7123qO1QZCUdQZ9lWdi8qWmAdn0_95ROuRBMuABFVRV7v2D2zg-2XaGyPLStub45Z37Yt0QFo0IuJjDsTb8s6Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر ZCode رو نصب کنید(با Zed Code فرق میکنه) می‌تونید روزانه 3 میلیون توکن رایگان GLM-5.2 و دو میلیون توکن GLM-5 Turbo بگیرید با یه محیط کدنویسی تمیز شبیه به Codex
با هر ایمیل هم می‌تونید یه اکانت بسازید و...
بله خلاصه
🥰
اینم لینک نصبش:
https://zcode.z.ai/en/docs/install</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/4193" target="_blank">📅 23:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4192">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسمپا- آزاد سازی اینترنت</strong></div>
<div class="tg-text">‏DoH HTTP Proxy یک ابزار سبک و کاربردی برای ویندوز است که با ایجاد یک پروکسی محلی، درخواست‌های اینترنتی را از طریق DNS over HTTPS مدیریت می‌کند. این برنامه زمانی مفید است که DNS شبکه دچار اختلال، جعل، مسدودسازی یا ناپایداری شده باشد و تلاش می‌کند با استفاده…</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/4192" target="_blank">📅 23:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4191">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسمپا- آزاد سازی اینترنت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IN_ZEKPCSi0i87WtCISMaldP4BYBb1KPuwRAGn2G3YYOcIpNnLJg1YCv50qlfAx-D5UouhB-7ocSQuFKQ48N52RjszqjTWCY4-_hyp2avGAobaPFxtMhwGIIc_5kDw2vL-jsZg_G6Osp7lJxXPZKpMj2IEpCS0jcYRr754wbNKpsn_wInkwxA-rnr1cD2XRyOv15EW5RdPA1de33PYZMyD3-5ARnu3rG0X8Z-fY5vNNmmv41ugA8CQeKBCEAN3Ot34qzgYLMGmqgfeNrEFjLCHZysWaG1dtZFISIuEqorOPUuZINta1pWcHQxeZldWCMX_A3PEDKw29CmhW1wnCuGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
DoH
HTTP Proxy یک ابزار سبک و کاربردی برای ویندوز است که با ایجاد یک پروکسی محلی، درخواست‌های اینترنتی را از طریق DNS over HTTPS مدیریت می‌کند. این برنامه زمانی مفید است که DNS شبکه دچار اختلال، جعل، مسدودسازی یا ناپایداری شده باشد و تلاش می‌کند با استفاده از endpointهای DoH، کش نتایج قبلی، fallback و حالت اضطراری، اتصال کاربر را پایدارتر و قابل‌اعتمادتر نگه دارد.
لینک دانلود برنامه:
https://github.com/SAMPA-ASA/DoH-HTTP-Proxy/releases/latest
لینک پروژه
👇
https://github.com/SAMPA-ASA/DoH-HTTP-Proxy</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/4191" target="_blank">📅 23:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4190">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZlAZBmD9rXknYm8C9T26iRY2UshiVW7NJKTNURS2Qe-ejzOC4z-AxjY7XelvYEeZb_kgTSRBnaN0iO2OoQP8wfqrONqds4iwkc6X3tody0e43LKhRyEetUhSq68Km0L83GVscKNH00X7igiWaA7iLPFpF5SO-mhJwJnO5ch6kf2Fvmo1iAlUyYk1KTpIV-fQzhqMo0PbJ7hozUWhQsw7yGWQhlQ7L4ZMrB9fQQKKRf5spW5AOosmJq7EMpv8Mb8XIOoO3UpkFAZUtsSd5uQm4BdHryWvalFUus4161ZiQ9Jdyuiqh4w_VDYgasIh8b3esEl9GjkiQwqosSwoKqVM2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر از تلگرام برای ارتباط با ایجنت هرمس Hermes استفاده می‌کنید بهش بگید که تاپیک فعال کنه یا فرمان /topic بزنید. بعدش بهتون میگه که برو توی تنظیمات BotFather و گزینهThreaded Mode روشن کن بعد از اون برای هر موضوع میتونی یه تاپیک جدا باز کنی و ایجنت موضوعهای مختلف باهم قاطی نمیکنه
✍️
Hessamsh</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/4190" target="_blank">📅 23:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4189">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">برای هرمس، 1 هسته سی پی یو و 1 گیگ رم به عنوان Minimum کافیه. اما پیشنهاد میکنم 2 هسته - 2 گیگ رم باشه</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/4189" target="_blank">📅 22:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4188">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nFGpvtH_cl0Y0STW1HI_z5UWyU5KOzhFB-dKv0gnyF1CNnyC2DSd_sAEOXjVJgaaV2bGpPcYFC_DCKxybG8iXjbfLEfNmQuSb-5k3JPn-Gi4POE_ty0gAio1H5H_54JYRQkOkjP4zrH_8HgfOJwvp-qy9R4HQak2Skv2fbnWzAjmVxswbGE4_LqH48UPwt-uZHDW3HnCuDe451LC65I_K7rJ0s60AezbejEwh70p3qT8b9DRSFuNrTbnYpjcv6OZ4IIormPf9BSFF6zuMEx_OhrGwfyP0lCoQh0RVThXIdKXD2lkRpeQk8IO-vyGnaXs7MXBFeAvRx7SyQriKOlgYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفقا اگر صحبت کاری‌ای داشتید با من، از اینجا می‌تونید ایمیل بدید و مطرح کنید:  matinsp.job@gmail.com  سؤالاتتون راجب متدها و... رو توی کامنت‌های یوتوب بپرسید. این ایمیل برای این منظور ساخته نشده
❤️
ممنونم از درکتون</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/4188" target="_blank">📅 21:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4187">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">رفقا اگر صحبت کاری‌ای داشتید با من، از اینجا می‌تونید ایمیل بدید و مطرح کنید:  matinsp.job@gmail.com  سؤالاتتون راجب متدها و... رو توی کامنت‌های یوتوب بپرسید. این ایمیل برای این منظور ساخته نشده
❤️
ممنونم از درکتون</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/4187" target="_blank">📅 21:50 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4186">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">رفقا اگر صحبت کاری‌ای داشتید با من، از اینجا می‌تونید ایمیل بدید و مطرح کنید:
matinsp.job@gmail.com
سؤالاتتون راجب متدها و... رو توی کامنت‌های یوتوب بپرسید. این ایمیل برای این منظور ساخته نشده
❤️
ممنونم از درکتون</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/4186" target="_blank">📅 21:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4185">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GaLzomEsdBK07WDNYBmApeIXBiMYZjO0AObshbjNCLcYSDiHGWw72CVzyMwLUYloYUNCyzA6b2QRU410632b01LpmCKdrfjk_C2OBUPtSOTM041zvMHXbDRge2jZ9GOKtJYfDEvbLvbGAtZmy2bPH5VKFf9nIR_J597PEsQTAC9-mLyVjX3_AxM2YA9Q2gPp2qm3tfVE6jf2LISokuthEi5S31ewI3kZMXs2J-Mk6o9BOBeA_JdWHuXb4UGJnoTI3Zd1aos09b1ijiXT6E_gZwMTIzQcg1pjyF2DXJL0IHi-Vv6b4uKYq2UUC4yq_PfDUkN3M2YJd-iAVdvmWIC9qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی هم تر و تمیز و عالی</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/4185" target="_blank">📅 21:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4184">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">فیلم آموزشی Clash Party
https://youtu.be/gMFH88yRghg</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/4184" target="_blank">📅 21:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4183">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">سلام خدمت همه دوستان
✍️
سرویس ساب WhiteDNS در گیتهاب راه‌اندازی شد.
✍️
اسکنر های ما هر ۳۰دقیقه بیشتر از ۲۵۰هزار کانفیگ را اسکن میکنند، از خروجی این اسکن تست سرعت، دسترسی و DNS Leak گرفته میشه تا بهترین کانفیگ ها جدا بشن.  نتیجه این تست، هر ۳۰دقیقه داخل…</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/4183" target="_blank">📅 21:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4182">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">سلام خدمت همه دوستان
✍️
سرویس ساب WhiteDNS در گیتهاب راه‌اندازی شد.
✍️
اسکنر های ما هر ۳۰دقیقه بیشتر از ۲۵۰هزار کانفیگ را اسکن میکنند، از خروجی این اسکن تست سرعت، دسترسی و DNS Leak گرفته میشه تا بهترین کانفیگ ها جدا بشن.
نتیجه این تست، هر ۳۰دقیقه داخل این مخزن گیتهاب برای سرویس های متفاوت قابل دسترسی خواهد بود.
🌎
ساب مناسب اپ های V2Ray, V2rayNG & ...
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/base64.txt
🌎
ساب مناسب Clash Mi, Clash Party
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/mihomo.yaml
🍏
IOS App
: Clash Mi, Karing
👾
Android App
: Clash Party, Karing
👍
Mac App
: Clash Party
📱
Windows App
: Clash Party
📱
Linux App
: Clash Party
@WhiteDNS</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/MatinSenPaii/4182" target="_blank">📅 21:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4181">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">بن شدن حساب‌های کلاد واقعا نگران کننده شده. هرکسی هم بن شده از ایرانیکارت خرید کرده یا سابقه خرید داشته</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/4181" target="_blank">📅 20:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4180">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">بن شدن حساب‌های کلاد واقعا نگران کننده شده.
هرکسی هم بن شده از ایرانیکارت خرید کرده یا سابقه خرید داشته</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/MatinSenPaii/4180" target="_blank">📅 19:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4179">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">☠️
نصب و استفاده از Hermes، آینده‌ی هوش مصنوعی
⚡️
فایل لینک‌های مورد نیاز: https://t.me/MatinSenPaii/4178
⭐️
توی این ویدئو: 00:00 چرا هرمس؟ چه استفاده‌هایی میتونیم ازش بکنیم؟ 04:17 نصب و راه اندازی روی دسکتاپ(ویندوز، مک، لینوکس) 13:47 نصب و راه‌ اندازی روی…</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/MatinSenPaii/4179" target="_blank">📅 17:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4178">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Hermes-MatinSenPaii.txt</div>
  <div class="tg-doc-extra">886 B</div>
</div>
<a href="https://t.me/MatinSenPaii/4178" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">دستورات نصب Hermes روی سیستم‌عامل‌های مختلف و سرور
سایت YottaSrc:
https://yottasrc.com/
سایت Netlen:
https://www.netlen.com.tr/
سایت Senko:
https://senko.digital/</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/MatinSenPaii/4178" target="_blank">📅 14:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4177">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KZ9aXXrFz6MkfbreFVe8TsJZoqXowq2-QDv24NLeUrs2zuLm9fZBYuUoOZRW9FCcLQWrPLyz2llXSeyeg0JkUsaS1JqiCMEWdDh43N70gvuY1teYqic7A2SG-ybr-QuaaX_hjDqQPVJmKG18OOhqGDgrZKmZyFQAwKD707ZOZ4wgSQxH2t0fCPirkl2QO9lnDuAASnE-OEIvgf1ez4VbiSY-To2s7lc-wAnMXIXvqrpTtJkWMtBg0BxO7MPd4a0vlaX4wHEbc4L27Lhy6JxF26p4oETSQKhzWMe7H5ereC54xVbihK5O6JrSTsegQb4mfY-q1ATKdszRtE2DZXiqVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
نصب و استفاده از Hermes، آینده‌ی هوش مصنوعی
⚡️
فایل لینک‌های مورد نیاز:
https://t.me/MatinSenPaii/4178
⭐️
توی این ویدئو:
00:00 چرا هرمس؟ چه استفاده‌هایی میتونیم ازش بکنیم؟
04:17 نصب و راه اندازی روی دسکتاپ(ویندوز، مک، لینوکس)
13:47 نصب و راه‌ اندازی روی سرور لینوکسی
16:46 نصب 9Router روی سرور لینوکسی
18:10 استفاده از API و مدلهای رایگان قدرتمند Nvidia
21:20 دور زدن محدودیت دسترسی به API ها با Worker کلودفلر
22:40 استفاده از Endpoint 9Router بر روی لینوکس و ساخت Combo
24:31 اتصال Hermes به اکانت تلگرام( و واتس اپ و دیسکورد و...)
26:35 نوشتن یه کرون جاب کوچولو که هر 5 دقیقه قیمت بیت کوین رو بفرسته و تحلیل کنه
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
همه‌ی مراحل ساده‌ست و نیاز به پیش‌نیاز خاصی نداره. دو تا ویدئوی قبل رو دیده باشید، عالیه
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/MatinSenPaii/4177" target="_blank">📅 14:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4176">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ویدئو 2 ساعت و نیم ضبطش زمان برد، بعد از ادیت شد نیم ساعت
😭
دستم شکست انقد با موس اسکرول کردم</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/MatinSenPaii/4176" target="_blank">📅 04:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4175">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DjTfp3Y8yp1r5IyuKo-axS328HoWZvoN8_qnhbVekuQZJeds2ODDyi1ExWfwF4cdUO1OeH_4Y_EZhAgGL86ORr3JYl_dvINUBZxkYC2Gezyr0cKYYL_E7mkOZNT9AWJrOmzeCS-X279HmVhu0SZsj0azwIGD7EoNuO5YEZOBICb5oZPNse_Jo2AKSmFxxqQusAUr0eIPlEzRhMGYTjx6WPItzHWXbCU_e_zdhX2_2nTwSO5FiX6pEQy2Neh8TEiFvfUqpejafnpUaOjWJzz52FWtj0J5VLrh7le5Kdfc8rSg-ohZFZneyARArdlyukATxagUbBW4zlkvjpogZHO4bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این وسط دسترسی به Fable هم برگشت</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/MatinSenPaii/4175" target="_blank">📅 01:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4174">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">وسط ضبط ویدئو به طرز ضایعی یه ۱۲-۱۳ بار به ارور خوردم
😂
(اون پشت حلشون کردم و شما قرار نیست ببینید. هاها)</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/MatinSenPaii/4174" target="_blank">📅 01:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4168">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-Desktop-1.0.0-beta6-linux-amd64.deb</div>
  <div class="tg-doc-extra">19.1 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4168" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/4168" target="_blank">📅 22:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4167">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jk5Cxqd0lGMNxvIQrvrFb7ZohJuFzqFMZjpoOKrCi3Rl49IGjCGB9QayuVE1nHmzZcKzDjCkklON-PnVK1SrAsOQkS75xGeD53hmYGbDjof04Gu6N7p5i35mrCsjV3m4hXvtzQ3O2CaXv98ItjcD-xH42az9o-cEA_UsVk13cvBcRKJ-PGrb11I9NA3YQYctAZBkI8DndUXqmnCmNEAeL5kcOTtyMDEN3bNHwPKuuJZO_hEfzRyT_CdEqwnyhw_U2yjqGxf074NTeBGJunkXgkvsEelt1U8dP7bOIHOOfxaU8Qe2ExkHMi9tZsthw6S8Lo44qVgNWwT8mSOOKV6KJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
نسخه جدید WhiteDNS Desktop 1.0.0-beta6 منتشر شد
در این نسخه، ماژول جدید WhiteDNS VPN به WhiteDNS Desktop اضافه
شده.
امکانات این نسخه:
• اضافه شدن WhiteDNS VPN به اپ دستکتاپ
•  انتخاب هوشمند بهترین سرور
•  نمایش کشور و وضعیت سرورها
•  اتصال بدون نیاز به تنظیمات پیچیده
•  تجربه کاربری ساده و روان</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/MatinSenPaii/4167" target="_blank">📅 22:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4166">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jJoAlUWx9QC6CQiJvwK77KssCaIk2BDj44fjwzivLrCkBpotpTR7eVpzYU35XOyfRq-lxWS0VQWDkkk4n0iKi53ezRkOmI2e0n22x0rqwjqlVhHEmFhHG_89-y3l1IYkGDhLH00-MftAOyU1JblkzyEbiKaZYEmEP2lprADpoYvMu9kfOJyXOOd8fnbEOoMKfoucu5t_D3SB3VereX_hqsrFSNTKkSHgKa6KnJWbl8JdPKEhv1EXn5ioyc_NCcEvSkp5pLl1mygCGLeS-K6iFUe3oTaqJf2HHdiPlvVk0hVu6_8xUs0bSJ9puKMUR5E06a3RwgOgbbB4jltaQ__ayQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این api هایی که Nvidia میده واقعا سخاوتمندانه‌ست. 40 ریکوئست در دقیقه
با 9router انداختم پشت هرمس، چه میکنه این Qwen و MiniMax3
توی ویدئو آموزشش رو میدم که چطوری بتونید وریفای بکنید و ProxyPool هم بزنید که روی سرور مشکلی نداشته باشه(مثلا با آیپی سرور من مشکل داشت انویدیا که با یه رله کلودفلر حلش کردم)</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/4166" target="_blank">📅 22:29 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4165">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">کلودفلر یه درگاه جدید معرفی کرده که اجازه می‌ده روی هر وب‌پیج، API، دیتاست یا ابزار MCP که پشت شبکه کلودفلر دارید، سیستم درآمدزایی پیاده کنید. تسویه‌حساب‌ها از طریق پروتکل باز x402 و با استیبل‌کوین انجام می‌شه؛ یعنی عملاً دیگه نیازی نیست درگیر ساخت و پیاده‌سازی…</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/4165" target="_blank">📅 22:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4164">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GMXqLF4BIKrsJk3dhS3RlbSkcR2RxFfzAU1Nw77uSwCmw6LHgwwh_SuthapEjec2i-xI_xwEIqHTtKzsXLVUX1sqDMGGiKvM9tHUo32iSn81HUepUtTm-g0w3r8ahlYI3m7qFVso76HjLN-9CCre2wD5hwacJykicbwJHnGi89FzQ9nUarU8vYoeCt8lp_BREk8ZvyRBzLZAVuJQ3RLnVpu8tijEs4-Z58w9TfUG5rnazOmOH3grgYuQPTPHxZvDqa3P8gT4tUts8muhuXS48SNAbc5iNtk92Teaq6VqNMx_XLebyxvSnC4Mi0DlsIc3Tu3KKcO4zheewiVgNXAdzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر یه درگاه جدید معرفی کرده که اجازه می‌ده روی هر وب‌پیج، API، دیتاست یا ابزار MCP که پشت شبکه کلودفلر دارید، سیستم درآمدزایی پیاده کنید. تسویه‌حساب‌ها از طریق پروتکل باز x402 و با استیبل‌کوین انجام می‌شه؛ یعنی عملاً دیگه نیازی نیست درگیر ساخت و پیاده‌سازی زیرساخت‌های پیچیده‌ی پرداخت هم بشید
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/4164" target="_blank">📅 22:06 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4163">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">از بین سایت‌هایی که تست کردم برای SMS، کاوه نگار که باید میرفتی از دفتر اسناد رسمی احراز هویتشو انجام میدادی، فراز اس ام اس هم که شیش ساعت گشتم اصلا بخش API پیدا نکردم. بیست دقیقه وقتمو تلف کردن این دوتا تا وقتی که رفتم
sms.ir
و همه چیش اوکی بود و 10 تا هم پیامک رایگان داد. خیلی هم سرراست api تنظیم شد از خارج به داخل هم دسترسی داد</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/4163" target="_blank">📅 21:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4162">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">تمام رادار جنگ الان فعاله و AI هر نیم ساعت یه بار، خبرگزاری‌ها و پنج-شیش تا کانال تلگرامی رو چک می‌کنه و اگر جنگ شده باشه و اسرائیل و آمریکا به ایران، یا برعکس حمله کرده باشن، پیامک میده</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/MatinSenPaii/4162" target="_blank">📅 16:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4161">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Bs1M4VTOa2Yfbl_vgjPGvt4zfjkqWD2-AUZFragtNgSWIJQ8ENjrIJGk2Mj0tEYbTgtdGkxM94JUvoMocGKhfiIKWSyEQpopxtJMx1IIbXKinZHCKmAIb33BZpLzPY4R4mpnhLbUQB2puA2fx7bfqJbuXKKpAOUpvutShZ6UdXC4G5in8lTGpVbtVLoVtmmnEbE0ADoyfJAgL9R9qLyF_KT-Dn6VcJ0rod8tx8YtIVblriSFHvo_4ZeT623TR5GfNFJ49JD8Ii1fyQcy5iTtIsqtoz3SH7KtsNn-ema32LjFq_XUUSqf6x7JkRS7Ht9Pl6AF4lTMXzNxNajOeMBkgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌خوام باهاش یه رادار جنگ بنویسم</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/MatinSenPaii/4161" target="_blank">📅 16:26 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4159">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">می‌خوام باهاش یه رادار جنگ بنویسم</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/MatinSenPaii/4159" target="_blank">📅 15:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4158">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SOrCey4nMWlIZtAEcj04vX7j3VsMDi-QDPfeRd8uLoIAS7940FsGnJTxV4UsGYgjcUZbNAVGvHPdl1QLz3gmw9Dy_DkQ0BhWuoIgAijwVyNORAfZB02WD--VdRpWDHaLMeCA3whum7YznW7M8qDruYeNSubHGHV9CtGaCjvNtT0eEPNxBpeyHk9CMCitq2FEuHmEghE5bRdYkd0Q61oimvxS7uy18yf_-rTfgeFWvT3dhMdMztffYrihO-u62k_tGtwGS_NpudDzV8r8LpWX4rVkZ6vd5aMU7dlqvTe1tLIto3RqQjIJgkD9FCBvcmtyAQkOTDBb1cJC8zNKQK5-HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کمی برای خود یادگیری را شیرین کنیم
(دادم همه رو هرمس با gemini 3.5 نوشت چون هم یادم میره چی رو تا کجا دیدم و هم همه‌اش هی چک میکنم که چقدر ازش مونده و الان درصد دارم و اعصابم آرومه)</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/MatinSenPaii/4158" target="_blank">📅 15:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4157">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">می‌خواستم ویدئوی هرمس رو ضبط کنم اما انقدر برق نوسان داره و هی سه راه قطع میشه کلا برقش، اعصابم داغون شد. می‌ذارم یه کم برق بهتر شد میگیرمش آموزش رو</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/MatinSenPaii/4157" target="_blank">📅 14:55 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4156">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">همین الان ویدئوی یاشار عزیز رو دیدم، و باید بگم دیدگاه فوق‌العاده‌ای میده به شما از ai
اینکه دیدم یه سینیور چطوری بدون گارد و با آگاهی و مطالعه‌ی کامل از ai استفاده می‌کنه توی حوزه‌ی خودش، واقعا لذت‌بخش بود.
نکته همینجاست
با این ai عزیز دل، حتی باید بیشتر از قبل مطالعه کنید و دانشتون رو بیشتر کنید تا برتری داشته باشید نسبت به رقبا. و قوه‌ی حل مسئله‌تون رو تقویت کنید و کارهای تکراری یا سنگین رو، به راحتی بسپرید بهش. اگر به مبحث باگ بانتی هم علاقه ندارید، ۱۵ دقیقه‌ی اولش رو ببینید حتما
https://youtu.be/-Rt_Z0allhM</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/MatinSenPaii/4156" target="_blank">📅 13:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4155">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">متا قراره برای استفاده از عینک‌های هوشمندش ریت‌لیمیت بذاره
😐
و یه مدل پرداخت (soft paywall) داشته باشه که باید ماهیانه اشتراک تهیه کنید  لینک خبر
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/MatinSenPaii/4155" target="_blank">📅 13:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4154">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XP7guezJQnxrD6FWUgVmVMIMqGmSBiLmKVk7VQvoUdv_acCQPHxmeXktV0YZm-PolEVi1cIf0qxzLH1fhtz6XPQibI7IqzlaO3JWhNqUATdKVQrG_s8OxcEs88EUOGmhVEwFo3o7qsHSOBWm_oUaoPIhcwKOluwoT_yYUq9L8huvOBtnGtZfIJcn2kiBaxpCUEPxTH_hj68wmjyOYSPbRdv4lQy0CXSdA4lmu2QOW7e5u-EtuqbDeKKMAQbrml0CwcsYBadO490lj85DsD0fC2vDlp-DbTl5duQARFnfLlf7yb3OZXuLZJrAzQH87r1z6OkdJprs9KANzniVCAX9Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متا قراره برای استفاده از عینک‌های هوشمندش ریت‌لیمیت بذاره
😐
و یه مدل پرداخت (soft paywall) داشته باشه که باید ماهیانه اشتراک تهیه کنید
لینک خبر
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/MatinSenPaii/4154" target="_blank">📅 13:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4153">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bg3n1FPygtaYuuZ6gDTAl0txF8uhifry8_s0LhZ1zYpsevObLWgli6r5cN3d8HtO6lA2V3xF0fGQvEqAomyQLsWlI9tadg1vaO5YYsQK_j-tbe-wWsTtwKUBNuV_VfbS9Li8Jvo7gTjhQbKjZm60Q3b8FPONiO7WGuQQ_TrvlUPCkM_X0mVe7093Y5uX8pkvmASskJ5H-KCgAdYMFfuF4OSlvTY2FpGh3jtitskNnWqSijS9Z6xb3BHlzfM4Zs7Q_vFxbbYC4dRw-9_uRRFFFP5c1J7qHJasAk1Kx24JE-Z-pZzF_r_SDKd-8sixIajOrsN4O-rfLKWZkG_-Gsed6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">غول چینی، GLM 5.2
همچنان ارزونتر از حتی Sonnet 5</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/MatinSenPaii/4153" target="_blank">📅 10:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4152">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">خب گویا کلاد Fable 5 امروز برمیگرده
😁
آنتروپیک گفتش که با دولت آمریکا مذاکره کردیم و امروز مجددا مدل رو آنلاین می‌کنیم</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/MatinSenPaii/4152" target="_blank">📅 10:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4151">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cAnzv3CeJIwbODML9udURtO2-KfTpw2S46WifJzwMXwB8INJH-SZWqSI_g20XuQvu0p66JKqkJpwSKNp0JWK7LHzVh1wHwnGPm9sa7lyM6i03gOBnnsCaFsCh0E6fycAYHHfo7k7O-l6PeHX-oA2MBXZ9AtLJWY5a7GNWSq1LlIWqsd-kLI8JUVNURBdUyPl34Uxl3L4iz1QlmzSIA0g49yB1GFP8FhqoYyDMTkbd8f3SUvj1HLyz_fGU9ZcAlHIgOflxoh38nKh1Sd0KBw0hE40zXA6I_NviJXEGJIAjwHMYz5uOfU-WcR1wnww3Yuf2w4XN--a7ihbLEf4YnKUnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انقدر هوش مصنوعی‌ها چند ساعت اخیر آپدیت دادن که نمیدونم کدوم رو برم تست کنم
😂
وضعیت عجیبی شده</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/MatinSenPaii/4151" target="_blank">📅 01:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4150">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">انقدر هوش مصنوعی‌ها چند ساعت اخیر آپدیت دادن که نمیدونم کدوم رو برم تست کنم
😂
وضعیت عجیبی شده</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/MatinSenPaii/4150" target="_blank">📅 01:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4149">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f2ffa3ab51.mp4?token=wBgAZys5DV-zNuQDLRniZGVxzVKT6rsiEMJ2K-C9FEYS4qtu_0FKfWOMnzYuLzv_wMX2r9XDV2m7gD-0fyymKCbhfb4x9Wh_MzkVcVDXxqqJI5_eMAwVUWpA24twaHz7HKUNdGmCiwI4ZwBdpKnJ3-yHCibky_0SBDVfdGb99vWeI2M25DZ1rl3hH-IupSB2c1UPaUkyZZpvBF83nUBZLViOxkAsVfmYnGd7ADuGxzDLEXfjGpK57ZDNics0sNZ20w33fnadckBclWlTTewyHgrY5gnP1v2u10fv0TY_7svYe0F6n52VoEy-yHf2m0Yt2w9o9T7GPiuB-8NXSr60bA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f2ffa3ab51.mp4?token=wBgAZys5DV-zNuQDLRniZGVxzVKT6rsiEMJ2K-C9FEYS4qtu_0FKfWOMnzYuLzv_wMX2r9XDV2m7gD-0fyymKCbhfb4x9Wh_MzkVcVDXxqqJI5_eMAwVUWpA24twaHz7HKUNdGmCiwI4ZwBdpKnJ3-yHCibky_0SBDVfdGb99vWeI2M25DZ1rl3hH-IupSB2c1UPaUkyZZpvBF83nUBZLViOxkAsVfmYnGd7ADuGxzDLEXfjGpK57ZDNics0sNZ20w33fnadckBclWlTTewyHgrY5gnP1v2u10fv0TY_7svYe0F6n52VoEy-yHf2m0Yt2w9o9T7GPiuB-8NXSr60bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شرکت Anthropic از Claude Science رونمایی کرده که به صورت اختصاصی برای مراحل مختلف کارهای پژوهشی و علمی طراحی شده.
توی این نسخه محقق‌ها می‌تونن کدهایی که مدل می‌نویسه (Artifacts) رو به طور دقیق ردیابی کنن، محیط‌های اجرای کد رو بر اساس نیازشون همون‌جا بسازن، و جالب‌تر از همه، بیشتر از ۶۰ تا دیتابیس معتبر علمی رو مستقیم به کلود متصل کنن تا تحلیل‌ها روی داده‌های واقعیِ علمی انجام بشه. این نسخه فعلا تو حالت بتا در دسترسه.
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/MatinSenPaii/4149" target="_blank">📅 01:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4148">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9603918fce.mp4?token=A_HYuITq6wKCeQw69vpIrbx37Y77Y4gAOMUV0nkp0lRsz1_I6R-KQQ1uAKvK20jksTNI3owUZygHFaeAOgUpMxGnFsEdvPawyYdlWJXjpVK3uwz8DlIKZx5nUbbpkC5A85Q3qsE3gMFqPAznSYZlUOdqYcfM-lTMmdJWbTR_75KjyzRbhNWHEMOn39bBIHsQY4BMUVbLryuvhp_SXXszAtfBJ6ovgAdskecetbavd1qhjgzRWVG28Hyv-TZ_v-j1kUpkRo1L1HibjthQP4fTWXKGO2XYo5zkwcNa0fgqEdMyfTmpevrPg55_s_jHsyggVnz7_1wd6XZuHQU7GYADEA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9603918fce.mp4?token=A_HYuITq6wKCeQw69vpIrbx37Y77Y4gAOMUV0nkp0lRsz1_I6R-KQQ1uAKvK20jksTNI3owUZygHFaeAOgUpMxGnFsEdvPawyYdlWJXjpVK3uwz8DlIKZx5nUbbpkC5A85Q3qsE3gMFqPAznSYZlUOdqYcfM-lTMmdJWbTR_75KjyzRbhNWHEMOn39bBIHsQY4BMUVbLryuvhp_SXXszAtfBJ6ovgAdskecetbavd1qhjgzRWVG28Hyv-TZ_v-j1kUpkRo1L1HibjthQP4fTWXKGO2XYo5zkwcNa0fgqEdMyfTmpevrPg55_s_jHsyggVnz7_1wd6XZuHQU7GYADEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نسخه جدید Hermes Agent سرعت خوندن صفحات وب رو ۶۰ برابر بیشتر و هزینه مصرف توکن رو ۴۹ برابر کمتر کرده.
تیم توسعه‌دهنده‌اش، Nous Research،  با حذف پردازش‌های میانی کاری کردن که دیتای تمیز مستقیماً از بک‌اند به ایجنت برسه. همچنین برای صفحات طولانی و سنگین، داکیومنت‌ها اول روی سیستم کاربر ذخیره میشن و ایجنت به صورت صفحه‌بندی‌شده و فقط در صورت نیاز اطلاعات رو می‌خونه.
این تغییر یعنی کیفیت تحلیل و پردازش هیچ افتی نمی‌کنه، اما زمان و هزینه‌ای که بابتش صرف میشه به شکل چشم‌گیری کاهش پیدا کرده. و یکی از نقاط ضعفش یعنی مصرف زیاد توکن رو پوشش میده!
کم کم تیم Hermes داره یکی یکی مشکلات محصولش رو برطرف می‌کنه و امیدوارم همین شکلی جلو بره
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/MatinSenPaii/4148" target="_blank">📅 01:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4147">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lN22jNZMmoeToiM9q32DoGv2B6dhYwilnPi1OUEO0tMhGaayh_XEZYBUttXo6sTo9UG3w2PlH1lc-G8irKUgOjMjZaLV-p_N_VqVetufPQuAA2yKND_KFSO1RK7qNKUMmsU-sGZlz--ziwTMWMDkD7nM1xr7PM0Zes7n3yVSu0dIZ5-KLPU1DsOoW7K4RjfkCDHVKfwMHf89kR1JKMVSEoePIsF1nmQWNkFgp9wuxV1fN-ScttBr0iUkFuxsRJLTAliHH2YNrzN0UvHk3SsfQY8WLEFuztEOvMxvZ2I9HkLCFKmgFBNFGt5Er_dBbsAYdj7xz8LxQJpnroCCUzh95g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم بنچمارک منتشر شده توسط خود کلاد</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/4147" target="_blank">📅 23:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4146">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G-g7yQEutWwrAIHiBAydU435poqA_1vBFfCEpnSn2sIiA9P9XLJ9nPpIuwO_vqDMZf6onrcyI8mif28Jn6ZKXrxw8RASEyq0dbwqfGwVKjpv3CWWoyCthNapxXttraMlq3DVKp9I7KKVHDAQ_ZmRZrkNbQZRKp4jTi9-yufNlIjpRSjBBkARTskTKQ90384a1ybdv5MMxw-gFsoYB_0NPWZ1j_i47NIKOfOe3azGBHaaMyKqQXRNb0xhymtWaAsv1JkPkOZaDE6CT26O_rml0-hT-2FNiaLnZWh2SjbKf4yMrWF3jZkXoyvQfWzZKyFDoOdN_KPdrpG_CHfg9a8QPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسم‌الله‌ آنتروپیک Claude Sonnet 5 رو معرفی کرد همین یک ساعت پیش</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/4146" target="_blank">📅 23:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4145">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dCgoZPVjGNtLtkC8Kd1TditmNRaQp4KAG3C47GrW64C1c-PNsU38IVXso-kv0Nx62Hcag9xRwXihy8_TpTPUuc5guC1xwGEW7XpCJtFqVeAtbCEYlUV7ulSXnEBJIazi53ABkwZM_A2acNrPgezeY7bxP-LN8cRk5z-If8iJ7jUx_KH_JQgzmbNjC4eveqcAUd2CqzB1HxqM0kcdyEEIbCpoJ5TGnBa2CwBITD3V95EQw7ICX_xM9_EoId7ToukTVsZB9kJKPqtogEyPbUC_bpHykrQl15FE4Nux2GF_4-nv3ewXcaSIuzu675gEQoHU-vg8Xq0ByEkk01XLCbaxew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسم‌الله‌
آنتروپیک Claude Sonnet 5 رو معرفی کرد همین یک ساعت پیش</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/MatinSenPaii/4145" target="_blank">📅 23:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4144">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">پولسازی از طریق کانال‌های انیمیشن کودک با کمک هوش مصنوعی!
🚀
تا همین چند وقت پیش، ساخت انیمیشن برای کودکان نیاز به یک تیم بزرگ (نویسنده، صداپیشه، انیماتور و موزیسین) داشت، اما الان با ابزارهای AI، یک نفر به تنهایی می‌تونه یک امپراتوری محتوایی بسازه!  این ویدیو…</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/4144" target="_blank">📅 23:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4143">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAiSegaro👾</strong></div>
<div class="tg-text">پولسازی از طریق کانال‌های انیمیشن کودک با کمک هوش مصنوعی!
🚀
تا همین چند وقت پیش، ساخت انیمیشن برای کودکان نیاز به یک تیم بزرگ (نویسنده، صداپیشه، انیماتور و موزیسین) داشت، اما الان با ابزارهای AI، یک نفر به تنهایی می‌تونه یک امپراتوری محتوایی بسازه!
این ویدیو دقیقاً به شما یاد میده که:
✅
چطور کاراکترهای ثابت و باکیفیت طراحی کنید.
✅
چطور با استفاده از AI سناریو و موزیک مخصوص کودک بسازید.
✅
چطور انیمیشن‌ها رو با صدای کاراکترها لیپ‌سینک (همگام‌سازی لب) کنید.
اگر به دنبال یک بیزینس مدل جدید و پولساز در حوزه هوش مصنوعی هستید، این آموزش گام‌به‌گام رو از دست ندید.
ویدیو با حجم 300 مگابایت اپلود شده , از طریق نسخه دسکتاپ تلگرام میتونید با حجم کمتر دانلود کنید.
〰️
〰️
〰️
〰️
〰️
〰️
در صورتی که مایل بودید میتونید از لینک زیر دونیت کنیدتا قسمت های بعدی و موضوعات بیشتری پوشش داده شود.
🌎
donate.isega.ro
〰️
〰️
〰️
〰️
〰️
〰️
📽
زیرنویس فارسی
🌐
ترجمه این ویدیو با وب‌سایت
isega.ro
انجام شده — حتماً سر بزن!
📌
برای دیدن قسمت‌های بعدی کانال رو دنبال کن:
📺
🌐
@AiSegaro
🚀
هر روز یک قدم نزدیک‌تر به آینده‌ای هوشمند!
📤
بازنشر آزاد با</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/MatinSenPaii/4143" target="_blank">📅 21:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4142">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eUlXGRVtMSIbIwA3mtx1_3JoGIzY5-4GDTrEQnUr-KVbb9yU6w4rza8zRDo4VJjiSZsveEruXGF_vZq-miZLQ5tFzDW9mYxlKhgyrBk9o4HEwJYp1z7ivnKrtIZ2oJNI9SK6x2n1qlefO_gW2f_zUDk15VfDYJreKuBYdwhrrLplW73xN0NLtdt-d4A6iIRKEYLwpcTSZAUBneHFh3gqLJUhzeEXxhm3dKrg_Vm2Ej_I9rQr7eo2D4M2oioxgvwO2cpOACvVwfvUS7iInQJtd-zHKZaZ-aYA0Ndpwoo2BmejWH2v5Pfb41VKvwLtDf0TsQMgd3wWwe0yvonQm58D6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوتوب یه قابلیتی آورده به اسم Ask پایین ویدئوها، که می‌تونید وسط ویدئو اگر جاییش رو متوجه نشدید از جمنای بپرسید
🎨
فعلا برای وب فعاله گویا</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/4142" target="_blank">📅 21:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4140">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">برای نصب کردن 9Router روی سرور اوبونتو اول sudo apt update && sudo apt upgrade -y curl -fsSL https://get.docker.com | sh sudo systemctl enable --now docker و بعدش این دستور رو بزنید docker run -d \\   --name 9router \\   -p 20128:20128 \\   -v "$HOME/.9router:/app/data"…</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/4140" target="_blank">📅 18:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4139">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">☠️
این شکلی از هر API ای استفاده کن برای هوش مصنوعی🫪
⚡️
لینک سایت 9router: https://9router.com/
⭐️
توی این ویدئو: 1- یاد میگیریم که چطوری از اینهمه API Key رایگان استفاده کنیم 2- ابزار 9Router رو نصب کنیم و این API ها رو اونجا جمع کنیم 3- کلی API رایگان…</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/MatinSenPaii/4139" target="_blank">📅 17:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4138">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">انقدر برق رفت و اومد و نوسان داره روی محافظ میترسم لپ تاپ و همه چی بسوزه آخرش. آقا بیا قطع کن همون دو ساعتو، نخواستیم</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/MatinSenPaii/4138" target="_blank">📅 15:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4137">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">بیشترین درخواست توی یوتوب و توییتر ازم این بود که آروم تر صحبت کنم
😁
من فقط نمی‌خوام حوصله‌تون سر بره یا وقتتونو الکی بگیرم
اما از ویدئو بعدی سعی می‌کنم شمرده شمرده تر صحبت کنم</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/MatinSenPaii/4137" target="_blank">📅 14:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4136">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cvcfx2_fc5zhrEZWoGK-iI3j-C0SllAO24mT-HJFwfhSQf4KJGXZJMlEQfpBvz3ypJkDe2-vLDdIwaJ1Fq_fhzeblJk7b77GQSs-4ca7X2eRG4e5jnBNvIcB90o1ucilQo3B1yxLmz1d8gVsDq8FqRrvjFZRW45qj3C08lDkli8BWURG-jETurQIRb05Rp-gQ6inUBO5WlJ7bF3UqS2_B-qSszSZlakH3j9FQ_7g4h7yt2v1snAWV1WQij8mVP6mbW4jsPYc9fic0OYZ_uJwyFYtuk68Q9LG2mPPuqwgA9l731SssCBW5etuIqG4n6gppRq4s8Xo2ubljAViaklNuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مورد نسخه‌ی موبایل Hermes، من توی ساب‌ردیتش دیدم که یکی واسش نسخه اندروید ساخته و Pull Request زده روی گیتهاب(که کدش ادغام بشه) منتها هنوز، رسمی منتشر نشده</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/MatinSenPaii/4136" target="_blank">📅 14:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4135">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4135" target="_blank">📅 14:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4132">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aknSEQzX9MVJKo9Ajco5WgM-tlhKQ2owzDVDa_u7azPAGc6Zm6w8Fg8MJaE5UH_KZ0wt0YxKCnf1vQ8B2z-1Sehi0wM0Ux3BOJxsAk2Bg3gt1vRShkdCmXZRVI011zkK3tAI_1j0-ZaTik4dqWC86vk3uqop9LAhd3Zo-rMXGQyN9T6rANb5NVxCfrH2xhsZB4IzVaALpiFU4A7_92TtxJBSgRzvAsxUt8QyjZ3sMj2J4hYY6V5wVvksJcsRsiM2us2AGN2AZBmiXglfc_5PNzmA_tKcpdTQ7hTStRAO5cONYPsOiy84luf3aHXsT5lPLGZycNM3MP7_NWE4aktm1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/exIHNS7x_k_VNMpA2lGfDYvbo0foQYJ0jruNJqLoEax-vbF_EFxr7QvEYFmZ2bGpsHKKneL7NUXzI3FwI85wfqqaRMRfsvdnA9BXHBpgVuAvMbyyR7QwztWAGO1DyIWUnNRs9GG_EvaJS9pfI0Euc7vX-wVmTpPQE3upusFCSu0jeeLg2obzr6W1RcUt-AjRj2foOJuCF8r7X5JBYFH-ihiH2hnSAfd-cK1oL2Ht-iQ06_DgRajTwdw2Tp_xIxhxJoMlysQn7XAINrZrUaXrkCi_Hyz2BNod5kIgwIgiNCYbxdibxDhRno2OUiLe_VNbYMlpIB66LR3fdAYes1ssFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NKIuz9R9viREgKx3beAdG7k4lwwewJaCKBudMLhCNFpYK0WBO7C04r5zOmUcxY3SGUJ3q-tji_RdG0lNvLyxg3GDj2wRSjTEcwpwT2s3b5nrsXx2vcIetFjdQsOOwFRXALKTT5fuSXf3JkOM-r5XbHNDovVd11Kd5kh2lZ0RuL55pHNZiX1PQCHSGXMf5WLkeeYe4muuYDvmt7t2zL_YtN_d_R3ufYEw--oJmLN6MbDitF6hIwgfEH7FNdDXf5h5N33pbLjhCiFOWluQ0kc9aATvONSb_vusWlJ1YP0LV1cYuKIG3ydUGfpJF3EY8PAVWZlclbIUW-HShEfVQLvh0A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">واقعا Hermes و وصل کردنش روی تلگرام، یه چیز دیگه‌ست!
فقط کافیه ازش بخوای، و بوم
انجام شده. ویدئوی بعدی، هرمس هست
👀</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/MatinSenPaii/4132" target="_blank">📅 13:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4131">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🚀
اسکنر WhiteDNS  اسکنر WhiteDNS ابزاری برای اسکن، تست و مدیریت آی‌پی‌هاست که در دو نسخه در دسترسه:
💻
نسخه دسکتاپ مناسب برای اسکن‌های سنگین، سریع و حرفه‌ای؛ مخصوص کسایی که می‌خوان تعداد زیادی آی‌پی رو بررسی و تست کنن. https://github.com/WhiteDNS/WhiteDNS…</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/4131" target="_blank">📅 08:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4130">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/STfoS-8TB_dSexuejh42HYGPb_KrJ9-b76wZeVNTdzY-abL_23fF8_pl6c62QYaTEyxUWgGqTznobK8UbRwBzXInlGGLQB2qneq9OiSihfyFqRikYDxeaP5BtPselE0_b1RrkFyr_vnjIxWTNllEuEvmReYZL2xT-rYqJ7htvQ8Sl_3vWjNnK2KPcxeuNinL7YkVRefsxtyjJbJjWH7GVjevRxodl_laiemnLOqCPXdNxWuSn32Uxo06JwEyHz-9aVBApFn1izPoeRHvY_gZaicFVRRDBiuaL4bOjNi7_4aHkUSGC4ddcyvpKGAkEYcUcsLsvYbPsLGJ8Iku5oyitg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
اسکنر WhiteDNS
اسکنر WhiteDNS ابزاری برای اسکن، تست و مدیریت آی‌پی‌هاست که در دو نسخه در دسترسه:
💻
نسخه دسکتاپ
مناسب برای اسکن‌های سنگین، سریع و حرفه‌ای؛ مخصوص کسایی که می‌خوان تعداد زیادی آی‌پی رو بررسی و تست کنن.
https://github.com/WhiteDNS/WhiteDNS-cleanip-finder/releases/tag/v1.3desktop
📱
نسخه اندروید
سبک، بهینه‌شده برای موبایل و قابل استفاده روی گوشی، با امکانات کاربردی نسخه دسکتاپ.
https://github.com/WhiteDNS/WhiteDNS-cleanip-finder/releases/tag/v1.3
⛏
قابلیت‌ها:
• لیست آماده از ASNهای ایران و ASNهای معروف داخل اپ
• امکان وارد کردن لیست آی‌پی دلخواه
• Health Check برای توقف خودکار اسکن در زمان ناپایداری اینترنت و ادامه بعد از پایدار شدن اتصال
• ادیت یک کانفیگ و ساخت تعداد زیادی کانفیگ روی آی‌پی‌های تمیز با چند کلیک
• استخراج آی‌پی از داخل کانفیگ‌ها
• تست سرعت دانلود و آپلود آی‌پی‌های اسکن‌شده
• انتخاب پورت از لیست آماده یا وارد کردن پورت دلخواه
• لاگ پیشرفته برای بررسی لحظه‌ای روند اسکن
• خروجی کامل و دقیق از نتایج اسکن
متدهای اسکن:
⭐️
IP Scan
برای پیدا کردن آی‌پی‌های تمیز از دیتاسنترهای داخلی و خارجی و استفاده در کانفیگ‌ها.
⭐️
HTTP Scan
برای پیدا کردن آی‌پی‌هایی که امکان استفاده به عنوان پروکسی HTTP رو دارن.
⭐️
SOCKS5 Scan
برای شناسایی آی‌پی‌هایی که می‌تونن به عنوان پروکسی SOCKS5 استفاده بشن.
⭐️
SNI Scanner
برای اسکن دامنه‌های موردنظر روی لیست آی‌پی‌ها و پیدا کردن آی‌پی‌های مناسب برای SNI Spoofing.
⭐️
Speed Test
برای تست سرعت دانلود، آپلود و Packet Loss آی‌پی‌های اسکن‌شده، همراه با رتبه‌بندی خودکار.
این ابزار برای کاربرهایی ساخته شده که می‌خوان با دقت بیشتری آی‌پی‌ها رو بررسی کنن، خروجی تمیزتر بگیرن و زمان کمتری برای تست دستی تلف کنن.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/4130" target="_blank">📅 08:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4129">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5950435463.webm?token=JJD-vvYopEz4hD6rb0eZvyXyiYylQnSAvZqHMSoqG5o7Cmlrklbk0k-HzYycQfkf9i5gPLFhYDJLKmSfsbSSb9cKmGXgtzZSid1eZkkFL6pJlzafcKAd62rbzYcVE_PFmvqtHh0SHFWEQcyZamyUfMZL8eqM6IA-AKamYXG_FUOKPh-6TIyD4mtnP6e806ZMxkIMynMR4Sqb7ZsDA12KqfiRnu35k3LoHKGqR3zEo060WLHATtIzns6In6MRxd1H7Kp_x0--mo9InTN_BD-lYGEIFNLgd-OVCvKiEgbW_h--Bek0uB__uxDIWgLFwFonpFPJ31ZL737Eqmat9aDEVw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5950435463.webm?token=JJD-vvYopEz4hD6rb0eZvyXyiYylQnSAvZqHMSoqG5o7Cmlrklbk0k-HzYycQfkf9i5gPLFhYDJLKmSfsbSSb9cKmGXgtzZSid1eZkkFL6pJlzafcKAd62rbzYcVE_PFmvqtHh0SHFWEQcyZamyUfMZL8eqM6IA-AKamYXG_FUOKPh-6TIyD4mtnP6e806ZMxkIMynMR4Sqb7ZsDA12KqfiRnu35k3LoHKGqR3zEo060WLHATtIzns6In6MRxd1H7Kp_x0--mo9InTN_BD-lYGEIFNLgd-OVCvKiEgbW_h--Bek0uB__uxDIWgLFwFonpFPJ31ZL737Eqmat9aDEVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/4129" target="_blank">📅 04:39 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4128">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">☠️
این شکلی از هر API ای استفاده کن برای هوش مصنوعی🫪
⚡️
لینک سایت 9router: https://9router.com/
⭐️
توی این ویدئو: 1- یاد میگیریم که چطوری از اینهمه API Key رایگان استفاده کنیم 2- ابزار 9Router رو نصب کنیم و این API ها رو اونجا جمع کنیم 3- کلی API رایگان…</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/4128" target="_blank">📅 03:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4127">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qVtp-iZAmjh0Cb8OhX69YgvcmhcETKfZdb9N_p_WQxhSVC0IKnwR9dNz81h0OnFhqzgmoa6ZIRmcowWnT3EK6Odwhlp7qdVOnE9wtW0tc5i2xpqBZwtK0Fg8-f_Ve8MOrpSOA11PUkfclG3YXXU2nmC0O99kSHASJz3ALWHlJnk9F62OVl8Iik1bL_h0acMmcmR_9jqyFHEh3-Wi9eMTlKcSg8azMuCt1ieXnaEB4zq6PVpY4n0yDRm9aQkPypBZY-hy-imd5OCKxz082DWZOzIJNvXlgubzmwuNQ0ZNekdm73di-9_jTTp_zPacs2xPoFB8yUBNZq9vsKlMWTYOIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
این شکلی از هر API ای استفاده کن برای هوش مصنوعی🫪
⚡️
لینک سایت 9router:
https://9router.com/
⭐️
توی این ویدئو:
1- یاد میگیریم که چطوری از اینهمه API Key رایگان استفاده کنیم
2- ابزار 9Router رو نصب کنیم و این API ها رو اونجا جمع کنیم
3- کلی API رایگان وصل می‌کنیم بهش
3.5- اگر تیک آبی توییتر داریم، به راحتی از گروک 4 و اگر جمنای پرو داریم، از AntiGravity استفاده می‌کنیم
4- از امکانات 9Router مثل Combo استفاده می‌کنیم و چندین هوش مصنوعی رو توی یه مدل فرضی کنار هم میاریم
5- به ChatBox و افزونه Cline وصلش می‌کنیم که هم بتونیم عادی چت کنیم، هم بتونیم کد بزنیم باهاش
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
همه‌ی مراحل رایگان و ساده‌ست و نیاز به پیش‌نیاز یا هزینه نداره
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/MatinSenPaii/4127" target="_blank">📅 03:33 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4126">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">وسط ویدئو متوجه شدم اگر کانکشنتون با api ها خصوصا جمنای قطع میشه هی، می‌تونه مشکل از proxy-ip یا آیپی تمیزتون باشه
گفتم این نکته رو بهتون بگم</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/MatinSenPaii/4126" target="_blank">📅 01:28 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4125">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">کمی ویدئو API بیشتر طول میکشه تا آماده بشه
صفر تا صد تمام API های هوش مصنوعی رو میگم بهتون
محتوا رو فدای سرعت نمی‌کنیـم
🥰</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/MatinSenPaii/4125" target="_blank">📅 21:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4120">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitedns-v0.0.8-arm64-v8a.apk</div>
  <div class="tg-doc-extra">18.9 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4120" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">⭐
نسخه جدید WhiteDNS VPN 0.0.8 منتشر شد
میدونم آپدیت کردن این سرعت یکم برای هم شما هم من سخته. اما تونستم دقیق مورد رو پیدا کنم و فیکسش کن
ی
م.
ممنون از تمام دوستانی که نسخه‌های قبلی رو تست کردند و مشکلات رو گزارش دادند.
⛏
در این نسخه، مشکل لود شدن بعضی سرویس‌ها مثل یوتیوب و اینستاگرام برطرف شده و اتصال‌ها پایدارتر شده‌اند.
✍️
از همه شما بابت اختلال‌ها و مشکلاتی که در اتصال داشتیم صمیمانه عذرخواهی می‌کنیم. ممنون که همراه ما هستید و با گزارش‌هاتون کمک می‌کنید WhiteDNS بهتر بشه.
تیم
@WhiteDNS</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/MatinSenPaii/4120" target="_blank">📅 18:18 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4119">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">اگر نمی‌خواید این بلا سرتون بیاد و کس دیگه‌ای بفهمه ای ایران هستید از وی‌پی‌ان‌تون، از نسخه‌ی جدید WhiteDNS استفاده کنید</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/MatinSenPaii/4119" target="_blank">📅 18:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4118">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ولی GLM 5.2 واقعا عجیبه. قیمتش روی api تقریبا ۴-۵ برابر از Opus 4.8 کمتره
این چینیا چیکار کردن با آنتروپیک، خدا میدونه</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/MatinSenPaii/4118" target="_blank">📅 18:01 · 08 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
