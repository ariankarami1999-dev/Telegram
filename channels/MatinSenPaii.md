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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-14 09:00:04</div>
<hr>

<div class="tg-post" id="msg-4236">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/MatinSenPaii/4236" target="_blank">📅 04:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4235">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/MatinSenPaii/4235" target="_blank">📅 04:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4234">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">دانش و پیشرفت علمی، پیش از هر چیز، به پذیرش نیاز دارد. دنیای علم آن‌قدر گسترده و پیچیده است که با ورود به آن، با انبوهی از اطلاعات و دیدگاه‌ها روبه‌رو می‌شویم؛ دیدگاه‌هایی که گاهی با باورها و عقاید ما همسو نیستند. اما اگر ظرفیت پذیرش در ما وجود نداشته باشد،…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/MatinSenPaii/4234" target="_blank">📅 02:11 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4233">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBloom.(Tin.)</strong></div>
<div class="tg-text">دانش و پیشرفت علمی، پیش از هر چیز، به پذیرش نیاز دارد. دنیای علم آن‌قدر گسترده و پیچیده است که با ورود به آن، با انبوهی از اطلاعات و دیدگاه‌ها روبه‌رو می‌شویم؛ دیدگاه‌هایی که گاهی با باورها و عقاید ما همسو نیستند.
اما اگر ظرفیت پذیرش در ما وجود نداشته باشد، توانایی درک حقیقت را نیز از دست می‌دهیم؛ به‌ویژه زمانی که حقیقت برخلاف باورهای ما باشد.
در نتیجه، از جایی که گاردهای شخصی و تعصبات وارد میدان می‌شوند، گفت‌وگوی علمی عملاً پایان می‌یابد. علم زمانی رشد می‌کند که ذهن، پیش از هر چیز، آماده شنیدن، اندیشیدن و پذیرش شواهد باشد.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/MatinSenPaii/4233" target="_blank">📅 00:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4232">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/509058c8eb.mp4?token=jzzYSGLGPXub-BaY8Mp-MZrWYCnAPfUgPyGUScBOtfWAQKr4-9j15zZXGDnQeIKQUH7IIiKGBmzc0oRaGmQomNecTaErrJA8bJcM2D-rOmegOXG13pojehjKOSccovXVPje4dqq_MHu5cgDiGLZrWGmg-ptQtuYe8n8uS1IQLYufCkCM20pdaepqPHbgmflRJu9aGoHxAGTBvNHNFcEHqfr3mgUFcI7RtopH6Fe41ew_sZL8x2RIIxCVi3Qlu9vw3HFnt7lj9L0PYiP_hPlehiQnWEgORkvqXcqbjUPBF4-t4Dwu-jPwWXq_IJRNLZ4hwLzu9qR9cIP3XTZB4kNVHg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/509058c8eb.mp4?token=jzzYSGLGPXub-BaY8Mp-MZrWYCnAPfUgPyGUScBOtfWAQKr4-9j15zZXGDnQeIKQUH7IIiKGBmzc0oRaGmQomNecTaErrJA8bJcM2D-rOmegOXG13pojehjKOSccovXVPje4dqq_MHu5cgDiGLZrWGmg-ptQtuYe8n8uS1IQLYufCkCM20pdaepqPHbgmflRJu9aGoHxAGTBvNHNFcEHqfr3mgUFcI7RtopH6Fe41ew_sZL8x2RIIxCVi3Qlu9vw3HFnt7lj9L0PYiP_hPlehiQnWEgORkvqXcqbjUPBF4-t4Dwu-jPwWXq_IJRNLZ4hwLzu9qR9cIP3XTZB4kNVHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاید براتون عجیب باشه ولی من خوشم میاد وسط ویدئو به ارور بخورم و بهتون نشون بدم که ارور ترس نداره و میشه خیلی راحت، راه جایگزین پیدا کرد
👍</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/MatinSenPaii/4232" target="_blank">📅 23:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4231">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sDrDjDZMcEHX14JoODM9-uPmNh9oR57WKbzD2eHEeSZ4lslcPoP7ph5G1bYZgn-nM_M3aYdvOVzaC_DmEybvNm5zHoDjSDAX9OAhD49w7dxePOPuvFjPSC5J06xU6jLgbajqRB_h9OmAhjMMAfiOS3b9_wvB7Prxij1uQ_KW5dB09U0yzvo5WDBpki5tB6YVZnctb3I1s33AP4_KGyDB1h0Nrh1iSUd0Vnqcy57-DkWHFMjHBXm8sltX0X7W4-K8llKQyA9PzeGhQ198UihZqNFUuesroTwN8Z99L5qlacfUc_Dq4uPOlGkM-bJYaB2dz9nUZmdVwVoDY5b1-UX3Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر، قابلیت Deploy کردن پروژه‌ی جدید رو برای اکانت‌هایی که با سرویس ایمیل‌هایی مثل Atomic mail ساخته شدن، غیرفعال کرده.  با جیمیل اکانت بسازید موقتا. شاید پرووایدر دیگه‌ای تونستم پیدا کنم که راحت بشه ایمیل ساخت که کلودفلر گیر نده</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/MatinSenPaii/4231" target="_blank">📅 23:25 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4230">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oEb8Y4MmjjLrwQL7YFm92Kc1yidckN2QERDn90XweCtXIQD0gZaOOgC9h1iLXcT5v4lcu3xg5yHv_zQ6TXBd_AOgz_mdBI9-hlig7VZ_lOkq52liBzlTN_LijZIW6VxVxVEl06G5ivMbveroT7cNBa5Qo9b144TzP7YJEBeah5WlzZXKzGtNEyonG3qeBFv-gl3UO7AK-hxv8nlvruHCb1Rv71CQ1ifvD5Cuqq2M_EGJCCyC-c5_mNnPIcZdVMItY634h_CzCho-xosYRNwY2gPR0-abOOcc3xIqk7roi0KDxj4xB2spVrti8f5ATURfq1E1SOrkm2okYxiI3faXRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر، قابلیت Deploy کردن پروژه‌ی جدید رو برای اکانت‌هایی که با سرویس ایمیل‌هایی مثل Atomic mail ساخته شدن، غیرفعال کرده.
با جیمیل اکانت بسازید موقتا. شاید پرووایدر دیگه‌ای تونستم پیدا کنم که راحت بشه ایمیل ساخت که کلودفلر گیر نده</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/MatinSenPaii/4230" target="_blank">📅 22:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4229">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">روش فارسی نوشتن درست و حسابی بدون به هم ریختگی هم توی ترمینال یاد میدم توی ویدئو. که یکی از دوستان عزیز توییتری دیشب بهم یاد دادن</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/MatinSenPaii/4229" target="_blank">📅 21:06 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4228">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">توی این ویدئو که دارم ادیتش میکنم، کلا با cli پیش رفتیم و از اپ دسکتاپ استفاده نکردم برای هرمس. علتش هم اینه که پروایدر شخصی اضافه کردن روش هنوز داستان داره و محیطش پر از باگه همچنان. با اینکه آپدیت هم کردم الان هنوز همونه</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/MatinSenPaii/4228" target="_blank">📅 21:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4227">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🛡
آموزش کامل نصب و راه‌اندازی سرویس MTProto با ابزار MTProxy  فیلترشکن قوی و پرسرعت برای تلگرام    https://www.youtube.com/watch?v=pyvB6VSPhwg   @WhiteDNS</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/MatinSenPaii/4227" target="_blank">📅 20:54 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4226">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🛡
آموزش کامل نصب و راه‌اندازی سرویس MTProto با ابزار MTProxy
فیلترشکن قوی و پرسرعت برای تلگرام
https://www.youtube.com/watch?v=pyvB6VSPhwg
@WhiteDNS</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/MatinSenPaii/4226" target="_blank">📅 20:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4220">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/orIWqIMWiVmP1_ywP863xKIvbPOQRlCutRQ2XTbGgVYGqoG5Z_wYpYTKf9ZF6BUw-UG_wiL0dGvwIBUR98AkSauFW0pk_Cu7sNx9uTpDtwufdQTMLU0wuiw6CqvgQr9xqV-CD1FuwWw1KMpiXaRzKkzfN-oO-Fx2gsDpwzX3oXNd9IayJb5InBQhZlF6bs76mZFNDr3yBm_9RpNxdBlyD-1UjobY1jvr6C0eZlL5PtHqmRZokG27bcRv2WHahn-tqgjg6tfuvFKrb9IcCQ9VU661KLal8ndmCVVnPm4NwZwqxjKP2r0AAnqFdU7oi-4QDb3p_eRxFOOzfyt4KB16Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TzhguowwV4y4hc9M_ywXbVWeOfRS6rtG4UUKLbYicxOeJmlQCvaVDWvj1Rd79ItGYXzmBjYiCRfLEaaGAdYjXhF0rcRXNeIHSXQU7U782Gji9kYtKPo1CIgjjIMyWj0PrsYX8WintBq2K46U0meYqelKO_Pu2bF3Oi2sakMznw2VMz3LdrqYDKbwlHGMkznqMTjlwJ00Pv9MX6UChVD8kUwh1zM9wxhpqsRT07sZ4HtZ0OScU63zPSRfjufLbmqtC5JPwaYOiB7StHtqThjQiWWkdw09oJN2dS3-hS6sUAx2sxBFk2mepP0I9vPOPxpL9elTWLAazISxKbNwIW4vDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aWbNDsJ9fiyx4Cc_y--ZZG5FXpJMc4zoJqYcyFpFZYcDFQdNcS6_H-YY8SC1QRy5FC1Ybd15ixrB9_1-AleW43LZG-3NNCeloMlqUY5lUkvdrLWnJufM1gGtnaIMRmmhBrXvyOCfgUUBN2ea3lsWqQFjqw1x8_yGGoIZ93tGhSSpgXnf0m3nyRNrjiaC5cA9bjbQ85Xxo8B5KtZwRcBJcisY7GkvVglR-aHQ6lp0BwyBj-5qutxEsVc_-ZBIktQDi86vkIgz5qovR216Dcem4O1xiNL2V074q7CUl42cEKRPFgjjlJC1wMwJdOp_V5_v5P4PdcgG1lY7kFaMTHZK8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Q1o8BjXYEXXbEs-5dhRrGBTIfujSkNJo9gjEwVmKWOA20CgkxaXxNc2Ys2kPh4QvjdYMjyxrjN3PX9kPuJX4rzS_dSS3K_lNkSVDSm5y4CKYgI1HmQUwimWkCqkkSNmcWa8XLSY4k6H_boIWfsZnlpr16-KzBWnfav8kxFBZrA0UwHMho1OzYAMoFUQQfUYzH9J3LhjvSrnEo6fZbn2HFHChHkzx6e0i4NPL4SAKspmwhr8TRH5XfKidwTqR6Y3lWeOXhho6SqyakjVAOjxjK7K7WzKRf6qxCvcGn8qz2CIW2DjIooe0FXHOZi2EjevHiAvwWOY4FuH-4POZx8sJFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fRDWT9gytCbonO_ru8R8pjSmjYMGH560f-la2VCTLfndpREBAdmon35fFYP-BuqopcTo6QJEdaCG-cjHp3DRmsiak8sjdeV1fE7vFsRwe9346hUCh-1Fd-O5gSffYLiIQTGzcR8vJS7Q5wtM0eCnP4x_QYaA0T8ZcD-9cZTJM5qR6002qFtErmrQOfGJ9aeQeTmSEBVWv15l0w9QA1vH-Fc4gKdSI6wGjmifCofRy9_WK0UyqIt1i5hNHHhvcUy7iHRT3gKu7tRzYKkaAbAfqgRnfsQgS0kLgl86bHHhez-1cSFVPMtu-yL-BrzPwRxysS6JAZG4HziCAmE9AmV7qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ihsa68s682InKES1crNTEucDqb60BSNM4eO7vwGdzXU-nSGtvpPyEhY-9cxra9xWs5Tqpikx8TAKdpmShyRQV_d50DplW3hcBSkXgkMAfhc244fg3T1InuO6i_KX3yE1HM9tTwjywBE77tbQNqTiY-sq7RPJlXziDWKvuYGtII71MCPejdwfn89Z3iSW9Djm7O6hkyvZNPwnLBx7LpaJZox7VYTyHC9OOzJYrsaIs37jlq-i_4-QoiVRWcD1TLkpBJu5PmeOLZJHsx9-IV_7PJSuBZX1Odl4ggRT9M1Jw61sEVI4ARpmCHRCa5A5Myx-IfLweY-_Az4Oa1I-HS8HiQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">راجب این هایپی که در مورد «ادیت ویدئوی بلند با هوش مصنوعی» راه افتاده چندتا نکته می‌گم و دانشم رو از ۵-۶ تا ویدئویی که تا الان دیدم باهاتون به اشتراک می‌ذارم:  1- نه. اگر دنبال جواب مستقیم و سر راست هستید، هنوز نه. هنوز توانایی این رو نداره که با هزینه‌ی کم،…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/MatinSenPaii/4220" target="_blank">📅 20:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4219">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DSjlURaa5CLJN4TRI2s3fr31pUvfI9sQV6lPgaD9PKX3mu234wCB_PBErtB10Hv44qocpfXe8Bo6mf_WtY8TdoZWZVlYqHD6djj9OfP6BRDODyCvcegsBqpbgbsvcRxKKtLglmsiFjcoSsCVTiPlskRf2W3MIOm1KIyH_t0yL6MRS-pZXbqJwzn4GK2wssSyiqS9SJ9NexnMyzwPHNFjE6NZpnYARlOSLpri5cV7pU8kt6osghI1qs0x-GFypCoNInPE-bjz8m2jf9MqnnD-P5qKXxmuiAwdG2oHsJFeus9DkEp2MD454Hg8TIrOO9D4-s_osjzjMLLMDlGjCqbuRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راجب این هایپی که در مورد «ادیت ویدئوی بلند با هوش مصنوعی» راه افتاده چندتا نکته می‌گم و دانشم رو از ۵-۶ تا ویدئویی که تا الان دیدم باهاتون به اشتراک می‌ذارم:
1- نه. اگر دنبال جواب مستقیم و سر راست هستید، هنوز نه. هنوز توانایی این رو نداره که با هزینه‌ی کم، بدون اعصاب‌خوردی و بدون زمان زیاد اون کاری که ما می‌خوایم رو انجام بده.
2- چیزی که من از ویدئوهای این دوستان عزیزمون فهمیدم توی یوتوب، اینه که میان با مدل Whisper و یه انجین شروع می‌کنن به کات زدن(که همون هم پر از اشکاله و نیاز به ادیت فراوان داره) و بعدش شروع می‌کنه با یه سری mcp و یا پلاگین کلاد کد که اونها هم اکثرا نیاز به api key پولی یا اشتراک دارن(کما اینکه خود کلاد کد هم نیاز به اشتراک داره) یا یه سری ها هم با Hyperframe، واستون موشن گرافیک می‌ذارن.
3- حتی همین موشن گرافیک‌ها و... هم باید قشنگ و دقیق بهش پرامپت بدید. این نیست که خودش متوجه بشه و این کار رو بکنه. همینطور توی این ویدئویی که تام‌نیلش رو گذاشتم، طرف برمیداره کلاد کد رو اگر درست یادم باشه با Opus 4.8 می‌ذاره روی Extera High effort که خب توکن بسیار زیادی هم می‌بره و فقط ۴۸ ثانیه‌ی اول ویدئو رو باهاش ادیت می‌زنه(بقیه‌اش رو داده ادیتورش
😂
خب مرد حسابی، واقعیت رو بگو دیگه. که مابقی ویدئو رو دادی ادیتور خودت ادیت بزنه)
4- هایپ اطراف برنامه‌نویسی هم زیاد بود، و تا حدودی تبدیل به واقعیت شد و الان ai سرعت برنامه‌نویسی رو بیشتر کرده. پس شاید بتونیم انتظار داشته باشیم توی آینده‌ی نزدیک، با هزینه‌ی کم و یه اشتراک معقول، زحمت ادیت رو از روی دوش ادیتورها برداره. ولی جایگزینی رو بعید می‌دونم</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/MatinSenPaii/4219" target="_blank">📅 19:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4218">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">کاربردش می‌تونه اینا باشه:
۱- وقتی دوست دارید هر چیزی رو بگید و در لحظه کامپیوترتون تایپ کنه
۲- یه ایجنت لایو با Hermes بسازید
۳- و کلا کاربرد عمومی. مخصوصا برای کسایی که disability حرکتی دارن و مثل خودم توان تایپ کردن زیاد رو ندارن</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/MatinSenPaii/4218" target="_blank">📅 19:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4217">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">چند روزه می‌بینم همه دارن در مورد whisper حرف میزنن. خواستم بگم یه ساله برای تبدیل گفتار به متن از Handy استفاده می‌کنم و واقعاً بی‌رقیبه. کاملاً آفلاین با پشتیبانی دقیق از فارسی. حرف زدن با کامپیوترو خیلی ساده می‌کنه. github.com/cjpais/handy‎  فقط کافیه شورتکات…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/MatinSenPaii/4217" target="_blank">📅 18:57 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4216">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XOLegCJTFv46dbT4a_HxeO0Y-Atb-aPeH71QDDRc1FZoQ3Mx9m9XxzW1_XK3R9ozeE9Lv-mIt_OCeXrbAvzfTQUEv32A7RNB-2vl1VyM9rbIBTKGUMTmwHkA9mmX0_g1NHj3BgliCHwnfGp-LostinXfliIRFHKlHsK8kDr2EecCU1iKNEWASIGUHL9xtPic9UUsuGui_-miKl_eyKCKKyB-9h0JV0xHh23fJUTvTPfG-yJcm6S4kfTD52LcAs3-N0KmN0mpqfIGdrBTdMA9CWFpEVc9J-vNhbq9ljPwGa8f1RDBROY9cODbd6sGwsmqUNs9L538k0nSIxiBJ45a3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چند روزه می‌بینم همه دارن در مورد whisper حرف میزنن. خواستم بگم یه ساله برای تبدیل گفتار به متن از Handy استفاده می‌کنم و واقعاً بی‌رقیبه.
کاملاً آفلاین با پشتیبانی دقیق از فارسی. حرف زدن با کامپیوترو خیلی ساده می‌کنه.
github.com/cjpais/handy
‎
فقط کافیه شورتکات رو نگه‌ دارید، صحبت کنید و رها کنید تا براتون تایپ کنه.
اگر دنبال یه ابزار STT بی‌دردسر و رایگان برای لینوکس، مک یا ویندوز هستید، حتماً تستش کنید.
✍️
apt_hq</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/MatinSenPaii/4216" target="_blank">📅 18:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4215">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ezWSYemnCURuhyjRfgge5-pzAQ1jVC331EigUI-1UIJiq_u8e1px-WSXvx2AHi3k4nKyz_l3bjF4gsvYMXRYOFsQaYksWoGhPX9mi5wcmNnA1_ipA3HQKPmJ42NS9J18G9BDp4OXpri7F0JveTeuMcblTOYRIp_UduaMILVu3U3_ibE8RXPzrIPrqg2lNd5P3SLIKxYdvXmjUVD-gHyd-YOb18hfwqbkxYQRFDq8AAOiX-KzsaCHkRQpCPSZ3e72BHD17xqcn3E0ULZegO_K5TyIlz51CQl05r-UN8uAMpsYUg7QdPZdJGxCfz7-2dawa5pnPtDadhrQ8cj1xcPTrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا به دادم برسه
3 ساعت و نیم شد ضبطش
😭
😭
از بس دستورات هرمس زیاد بود یا طول میکشید(کل ویدئو رو با api رایگان رفتم بدون سرور و... و واقعا هم خوب بود) و قلق داشت انقد شد
اما ادیتش کنم ۲۰-۳۰ دقیقه بیشتر نمیشه</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/MatinSenPaii/4215" target="_blank">📅 17:36 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4214">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">برای مثال کیوریتور (Curator) که توی ویدئو توضیحش میدم، یه جورایی کتابدار هرمسه که تو پس‌زمینه سیستم بی‌سروصدا کار می‌کنه.
و Skill هایی که خیلی وقته استفاده نکردید رو پیدا می‌کنه و آرشیو می‌کنه تا سیستم سنگین نشه.
ویدئو پره از اینجور دستورات و همه رو هم تک به تک انجام میدم و تست میکنم و صرفا روخوانی نیست</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/MatinSenPaii/4214" target="_blank">📅 16:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4213">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">هرمس قشنگ یه کارمند تمام وقته. ویدئویی که تا آخر شب می‌ذارم رو حتما ببینید، تا بتونید از تمام پتانسیلش استفاده کنید</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/4213" target="_blank">📅 16:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4212">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">به زودی یه ویدئو داریم برای تمام دستورات ریز و درشت Hermes</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/4212" target="_blank">📅 12:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4211">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">به زودی یه ویدئو داریم برای تمام دستورات ریز و درشت Hermes</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/4211" target="_blank">📅 12:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4210">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dXPP6ZknaQLsXm4JHOl7Wbo4Ki7bTYGVYGJQoU_axv2vduJU604B7p4Ql5Si9wgfl34i1-hN4LxKXeB1FwRKLt8grmwB-is7AbFYUvaFyXBIG4pzVFEiR6vEWa6pEPewcCBYzKrRmib6fURiuZXM0ZJRKhjz_e7CvMrU95qdJZxBxW8rtGUdjHCzrvFOZDhdtwDR2MgewP7nYGpBz0A7Gn-CXAxQQucXS03ehF6QTpZqL2h_2s-QplAzglgIG-E7z0NhewXZlFABiZ-Zmnew8YbShi-OgBJzcm--DBVGrCIv4A9GcMht3gJbx2nKESTxgnEqGSYilP8tBtArQOyz-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این داستان، ایرانی بودن</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/MatinSenPaii/4210" target="_blank">📅 01:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4207">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/4207" target="_blank">📅 01:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4206">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56bbdb4680.mp4?token=CeuEmBciP3Ntr0t4n7I_ozYWf4kXPUEC6QpnclI49-LhcA0UHofX6VPr9NRMFo7OIkuCbBEnBV4bmtzV0k013688ZNhHEvnIuFAldfDoLAI1xzzme3tyA_5Qgun74xj9PsMnEbM_9oJggUv5xxwiJyFUOnj1RjH7A2JIJs6BmJmhxJUzCPKcNJqCkGXN83QRb1WhUAR_Z5vLsKSzE4BKn46Of15I8BDyx1V-8EOAdYc5DAYWJfmK7a9K4Er3UPA9MxNExV6n9ZZuKEP5LaDBTB51Yuu_sacdwDYKnicvr5hz5lI7fXwdk4CgmrGC7NyLf6iQ8KSMKDTKULdCyOcF-4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56bbdb4680.mp4?token=CeuEmBciP3Ntr0t4n7I_ozYWf4kXPUEC6QpnclI49-LhcA0UHofX6VPr9NRMFo7OIkuCbBEnBV4bmtzV0k013688ZNhHEvnIuFAldfDoLAI1xzzme3tyA_5Qgun74xj9PsMnEbM_9oJggUv5xxwiJyFUOnj1RjH7A2JIJs6BmJmhxJUzCPKcNJqCkGXN83QRb1WhUAR_Z5vLsKSzE4BKn46Of15I8BDyx1V-8EOAdYc5DAYWJfmK7a9K4Er3UPA9MxNExV6n9ZZuKEP5LaDBTB51Yuu_sacdwDYKnicvr5hz5lI7fXwdk4CgmrGC7NyLf6iQ8KSMKDTKULdCyOcF-4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بی نهایت آدرس ایمیل با یک دامنه روی کلودفلر:
https://youtu.be/Z069VNFAgAc</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/4206" target="_blank">📅 19:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4205">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">خب دوستان GLM 5.2 اومد روی Nvidia وقت استفاده‌ست
👋</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/4205" target="_blank">📅 19:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4204">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NjSZ_C7I8LY0tNGsUk69ArN-7wXLRBv3qmdajLmGGdAIhvc82Au86JJIeUqF7K4lb_4nOU1Wi2dzgx6b7NBMh8kchX2lhwosXq9fw4C5qAq1QAV7ZsnyN3HPz2od94knB7TqYE9YBALmMyFpic6dMSX-91LCOIelXDDO7hMmOT5g7rRamQOHNJt2rRMUn1UTvRNPqremXs-urf5o40G2gMMlDoDHzXuj0Xibux7lyJf20d20UQWvSuJ6L-E2Cz33EuxUlMPMNE6M3z2e99CgutFDiQuD8AVwzmTaLGg8_L6JCj4UQ-QDiRp4ARg-qw4RGPHzy9-4hB1vb9NsvunpDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب دوستان GLM 5.2 اومد روی Nvidia
وقت استفاده‌ست
👋</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/4204" target="_blank">📅 17:09 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4202">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Q-v0AtcsiX4nUXSNlFCzuW4Cq4A-9CdNr5vnRCeubXxedP8l2i_UcyAc1yPe0P6RMTeev7gzwQNDnYvucQmlAYgALOWXUqcEvfyha9EgDNm_Uwam0bRj82XrdjueoSiwzL7gN39F2JQzISGcG6xzLmIkGrp3qD5lLC0I-3rkl5FlIDP3I15tGJQ6ThqMjZqXf_jqJWrwi9xa045b4JcowiH9QEUQChCinC5Ke70RK8eVqvaTcsmc0ZVSXQHysoloKCl9L9GHa3lsvckBDZhmd5Kb24BDe2k8zTpMrSeWK2wXmAz__jzccLPypwBmuvKyPG6sxrKIx3bZHcDHK2_GCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NHFy2zkUp_5J-v6N6Eddks8cJEshWihWUof924_vHBJnZttmF3oSnKH-ljMMBgyJdFkLtJlY_bM0Adap4A2ToyGrIEL9W3hlEozOSYWeLoBP8bcfjauMtVMqIbsU3aI-3rwfOrxMiCoGqJk6o5tQ43ltCGhF8PPOgbdnFaE4zmbfqtpX_1G8nqfeZXM6RefC7WyUnuyrkU_Is0U1CWGnJU_iRoAFVS6T_YF4epa_8o1z3m66p4vTA8eZiO-3QRjnenXX015j6HFS0_8VqXCxYzSK77MoR-JInKvQHxZay3awMHFWR_bpiC-e82jjNv6h9vCA0HdXikBNakjcg64RrQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">چیز بامزه‌ای نوشت اما پر باگ. دیشب GLM 5.2 برام دومی رو نوشته بود که کار می‌کرد همینو الان با sonnet-5 هم تست میکنم</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/4202" target="_blank">📅 17:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4200">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QPPZU0VeOrMLEA00Ir_5d1nZ-nehTC_aMJv6sH0CPtpF-QQAYeD9JwMH50LklsoWyRAfo_IntInEjboyajhC-Y-FjCnBBVlenUF7Lx_GMCUdd9lYlZgKXsSbna0hBTNcNi2yV5ncKtcfU1Z_-M9YkecAkoXmAGHgy1EFLUMtoor5whjc7I8cH9P-_VXnHDMyCNj8z02_Vy8dim9afBZ5EEgJRfqYNd4K4bbmA02d8s96tUwIZQ8I7ar3UGJ-FBesDcu3vsi4wwNv_L_gsYTq-LB7dD_bH-uEadtjdGeofKUctI5ZpTE686NaWxgHnlGH4DTjfAJLx0DD6tttj3rzBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dKDjZnZCkJRGBlnqQD5Khkyv_h-0TBqu0ht2uoffVxai65ZiKWxzkETqP084sAbjNtldDVAnQF8p_2K9EoAZf6jOy585tXx1GMTiMjMZ_fhX7gF9xLO2nSMoHxilnFyI9PuE81bS0kgum0SYsWkgbLA-eNo3K3bNJCoJRP83Zuipwesnkh548BngEkIO0jHxxioNryIB0s8fncNJjoxm4CYh0bK262XNAT1iYz8hajb_PS0tuJEgWoW44eWDPtEafjmIawFhRSTXfJLJAp8yl931qUZv-dj0RPSpVMGzDS8NN7cR4eehpT6nhsx-XkuQuVL05618GnMq8SZYQ9JVTQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بریم ببینم با یه تسک گنگ و غلط غلوط چیکار میکنه</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/4200" target="_blank">📅 16:52 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4199">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nqckhItoj7n9rOPj7HYuSOdqJfZjuOx7ueEaxEvsPrTrTrw80xKrzEhWRJv5ik5qWQNS55EctiB-zCqVnG00jQ-11QN-Vzht3imQx0CZYra4vrE6ZTLNhdNUs6t8ytQN6BdJNuWglbeGBnaqFyoMS9AFnwOGl7-cp5sGUgoIvRCwFDvH5CgN1edWrfWy2l0ikJng14o_NSIrj21Rq4mrlK0PNgd7mMOQbTHcOypaOpSRJMPsMSWTDeLJkwQkxGCi_t7EJ09ucS1fZpKIQn5qUE8OqjCmFUQ3ljcmwA8bLRoRaaOsanX7f3esw4RPhGlXqJkE1F4uaxuqNLQ8iQHPFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مثلا هیچ فعالیت روزمره ی معمولی غیر تخصصی و تاحدی تخصصی ای نیست که با chat.qwen.ai نتونی انجامش بدی و نیاز به خرید اشتراک chatgpt یا claude یا gemini داشته باشی. البته دارم تواضع به خرج میدم و میگم که qwen صرفا از پس کارای معمولی برمیاد! برای سرویسی که میتونه…</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/4199" target="_blank">📅 16:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4198">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KlLpdKan4muDLcqfcJbDi4wBSoi_AnsZV6fs2e0rjDyO9DD8Bwx2JCqYwxZE2XeylkltA1_ycJtBlHlzGmCjIWGbf6cBdKvPJG0-6JCYfUFrg187MPl7GKLZFizJq2tLOtLri2VrrQcIxAWo7lMzw8li7OKcWqs94Uq9hIzB-AZTVO-yBxHZlNXo2SNVg7b1dqr306Rybx-tlzYTQey325veRevs1Uoz-WPMxOmvnpDMTBF-_7Y9a_vwfDfHoIuT6JEMymYaJODOaOcT8jsbHgix-nzN0v-3a3SucLs9m4RZrbqDAlhBEq8hiYihDQt2RJsj_9aQ8hINHZq-KNLI_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مثلا هیچ فعالیت روزمره ی معمولی غیر تخصصی و تاحدی تخصصی ای نیست که با
chat.qwen.ai
نتونی انجامش بدی و نیاز به خرید اشتراک chatgpt یا claude یا gemini داشته باشی. البته دارم تواضع به خرج میدم و میگم که qwen صرفا از پس کارای معمولی برمیاد! برای سرویسی که میتونه پروژه بسازه، مموری زیاد داره، عکس میسازه، فیلم میسازه، ریزنینگ قوی داره و برای هر سوالت یه لشکر ایجنت بسیج میکنه استفاده از واژه غیرتخصصی تحقیرآمیزه.
✍️
بوکانت</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/4198" target="_blank">📅 16:36 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4197">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">توی مدلهای چینی طبق تجربه‌ای که روی هرمس داشتم، MiniMax m3 خیلی بهتر از Kimi 2.6 کار کرد واسم روی api انویدیا</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/4197" target="_blank">📅 16:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4196">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">به قول یکی از بچه‌ها هر روز جوری با Claude کار می‌کنم که انگار روز آخرمه</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/4196" target="_blank">📅 14:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4195">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">اگر ZCode رو نصب کنید(با Zed Code فرق میکنه) می‌تونید روزانه 3 میلیون توکن رایگان GLM-5.2 و دو میلیون توکن GLM-5 Turbo بگیرید با یه محیط کدنویسی تمیز شبیه به Codex با هر ایمیل هم می‌تونید یه اکانت بسازید و... بله خلاصه
🥰
اینم لینک نصبش: https://zcode.z.ai/en/docs/install</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/4195" target="_blank">📅 13:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4194">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fvRlO3wrd8TfA1lEYw9pnwsnm-7p-kVDrJ5DSRFEwcPgp98HwwcUB23_xwSEt2EDJz0L-eouIcOB-GHLg7d2zV4v8myvNT2YENwgP5yoiPbMUD-scVMGI08JKOaVNylYH107NjDurUo_Ezb0_aKFwRjGruMG9SvHwzKBUy8GI4myh8udyB6ph1Np3DNkqdBvhk5iub2teFcZMstIiIdfq4w1PA3esqT4UL8qklVaI5yF5hCXXH3Ttj5JTFeT0Isb--ii47WW9kLGJIFuIsSP1R10mlZcudntl8aqwu2DrxP3WN5r_EYTD23CMbTz8JOdAKrHzg5vhdehkUxkTziXYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر ZCode رو نصب کنید(با Zed Code فرق میکنه) می‌تونید روزانه 3 میلیون توکن رایگان GLM-5.2 و دو میلیون توکن GLM-5 Turbo بگیرید با یه محیط کدنویسی تمیز شبیه به Codex با هر ایمیل هم می‌تونید یه اکانت بسازید و... بله خلاصه
🥰
اینم لینک نصبش: https://zcode.z.ai/en/docs/install</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/4194" target="_blank">📅 00:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4193">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rWh-PlE9a-x8yCQA_Cr3JBerhxX4QW8z5riiKvHVYxr38A3JcpH8yW6sCzh5blJBGwo_qRer8kfk49Ye_-AEN1_DthPLJDeSlD0O4b9l7ERCJNbLjKp3kSOlVfPjYytw3Q-WdWuI9r6E2QhlGPHtVL45saSU1YM7UisFx1vGqfEQ3u6xSprCrAiqEuomptQH-Rp0UEv8hSsea336RfXRAmTRvn5i8F-ki6FzKj4VZ319965Hr1Zcjz55_W6zWmcB5uh06EPpHut2tHN3TkanUbcJt-WrOf5QPmABQEzhsgXxhieqnEijrR0IO1FNB0HO3fRpDhuzDBuW1GuxQBwegg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر ZCode رو نصب کنید(با Zed Code فرق میکنه) می‌تونید روزانه 3 میلیون توکن رایگان GLM-5.2 و دو میلیون توکن GLM-5 Turbo بگیرید با یه محیط کدنویسی تمیز شبیه به Codex
با هر ایمیل هم می‌تونید یه اکانت بسازید و...
بله خلاصه
🥰
اینم لینک نصبش:
https://zcode.z.ai/en/docs/install</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/4193" target="_blank">📅 23:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4192">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسمپا- آزاد سازی اینترنت</strong></div>
<div class="tg-text">‏DoH HTTP Proxy یک ابزار سبک و کاربردی برای ویندوز است که با ایجاد یک پروکسی محلی، درخواست‌های اینترنتی را از طریق DNS over HTTPS مدیریت می‌کند. این برنامه زمانی مفید است که DNS شبکه دچار اختلال، جعل، مسدودسازی یا ناپایداری شده باشد و تلاش می‌کند با استفاده…</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/4192" target="_blank">📅 23:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4191">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسمپا- آزاد سازی اینترنت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vvl0KdmvT9ozeyg7uARbX4gWeIUzqstIniMsCrdwDhrxSjH8FRwE0JOf-nMHP5Lfwv6eexUm5lNBFODulR5PoGkEqnS_PqQzMAReQlIqEORMoOl8M2n2S55zMjjFz7YB8mDsgBXuXTuXvjzQOzoxClK8OtogrRnTHVe3rifhZgd3DFHZfsuRXLaXztKnyjcbM1V2dzpOXvcd7dQ1ganCFYehOTROGCyVSUEuHWFXR6YC6AL-V7LXL8_iABSYxOTQYEy217IjMhKG3_8B0lvqpURnm_o7xa4EbMqkxuhVgEPVsDiMT_ZcbuJd7cw_dh6wUqQxO7GbuvMEKcyq72NZ-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
DoH
HTTP Proxy یک ابزار سبک و کاربردی برای ویندوز است که با ایجاد یک پروکسی محلی، درخواست‌های اینترنتی را از طریق DNS over HTTPS مدیریت می‌کند. این برنامه زمانی مفید است که DNS شبکه دچار اختلال، جعل، مسدودسازی یا ناپایداری شده باشد و تلاش می‌کند با استفاده از endpointهای DoH، کش نتایج قبلی، fallback و حالت اضطراری، اتصال کاربر را پایدارتر و قابل‌اعتمادتر نگه دارد.
لینک دانلود برنامه:
https://github.com/SAMPA-ASA/DoH-HTTP-Proxy/releases/latest
لینک پروژه
👇
https://github.com/SAMPA-ASA/DoH-HTTP-Proxy</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/4191" target="_blank">📅 23:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4190">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dcpF7qU1W7kXqZTQKzknk5jj1Oa7jT2LIQBfwpHfxSkL6ReFSMqdVAlRZMraUfs3XvhY_jlFDYRsLoJ79ZgRWyicUPSWHkAcd_QeNQeHHq0yV9ZN02K8FwTWx9GifjAXZzl1ygTCJWRxqhDfJg-jFHXFuM4sGbb_i1FztCloNSxP2VRvukypKSE9HK5AW7xBLfm__w-bR3EllpeMyvJ-WZYz0Zb8XZz9P0afOyhcHJhn7qJkNBl7nnDhSM2Go12HI1ZSP-lJNNnoLMHKlQTqi5oNETfGvif_KsbNMXPbOjnWN3caEtcoIZTncnxhVvnVyYWKQqiQwTszPRo98WANig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر از تلگرام برای ارتباط با ایجنت هرمس Hermes استفاده می‌کنید بهش بگید که تاپیک فعال کنه یا فرمان /topic بزنید. بعدش بهتون میگه که برو توی تنظیمات BotFather و گزینهThreaded Mode روشن کن بعد از اون برای هر موضوع میتونی یه تاپیک جدا باز کنی و ایجنت موضوعهای مختلف باهم قاطی نمیکنه
✍️
Hessamsh</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/MatinSenPaii/4190" target="_blank">📅 23:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4189">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">برای هرمس، 1 هسته سی پی یو و 1 گیگ رم به عنوان Minimum کافیه. اما پیشنهاد میکنم 2 هسته - 2 گیگ رم باشه</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/MatinSenPaii/4189" target="_blank">📅 22:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4188">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aza-RiNgc9PXn9alFRgwUA6Hipfp9kv8Nas0UvfkBkE4DNChZt_LP0DlCmgeGvr1MdB8PQNtb8txELRaRzJHNzztSXFbhUGY66WNepZPLIux-nyjllXN8CEPFumoQMbF8y6zKSK7L2_NOSE0o-U75q96_-BbzaJkJlIBa6kbMC_jrPpNFOl7GD_JCKWhNrVWFYpRfgOli1I8em81a4A0oAmJW2uBQ8Ey88r3wytz9fLZZ5odnYI8ZPysRifRRXF8RbMWQ23-Jb3ktW4tNF-52ga3EAZe5_5V9pLfJJfVBcERfkTAYuzP-TQ3Yem09xYRbnT4G5zV7QygA5uz8wfOCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفقا اگر صحبت کاری‌ای داشتید با من، از اینجا می‌تونید ایمیل بدید و مطرح کنید:  matinsp.job@gmail.com  سؤالاتتون راجب متدها و... رو توی کامنت‌های یوتوب بپرسید. این ایمیل برای این منظور ساخته نشده
❤️
ممنونم از درکتون</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/4188" target="_blank">📅 21:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4187">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">رفقا اگر صحبت کاری‌ای داشتید با من، از اینجا می‌تونید ایمیل بدید و مطرح کنید:  matinsp.job@gmail.com  سؤالاتتون راجب متدها و... رو توی کامنت‌های یوتوب بپرسید. این ایمیل برای این منظور ساخته نشده
❤️
ممنونم از درکتون</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/4187" target="_blank">📅 21:50 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4186">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">رفقا اگر صحبت کاری‌ای داشتید با من، از اینجا می‌تونید ایمیل بدید و مطرح کنید:
matinsp.job@gmail.com
سؤالاتتون راجب متدها و... رو توی کامنت‌های یوتوب بپرسید. این ایمیل برای این منظور ساخته نشده
❤️
ممنونم از درکتون</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/4186" target="_blank">📅 21:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4185">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Dh2qFcpCZLXNXz7xBwsDPVSf5VqkTcvVal07ykhxm2GyPbLiMua6lDCbUX1KfOrH5PkXWOoWo03o7El8Qfi6sqjvYzv0cYlrFUq9jfQAiMPc9KuNg2-VqIiOnAp0KN1lfW_YAfX4w462KgwUyOyTJ232ZH30N5AdaoqL9E1cxtTe1DIDuuFReAlDgUzACZQ8aADkA1i0CfA92WNG4zm7xxtBdNheT1HxtdDWbIforD5gkE9GeOOI8of8SQdcj3dXcDrkH1XbKLFWL4ibAtdfgCJRTiMX2omgZOaziYq30IynAgP_BXrW_C45rGKpoOa_Emi5fyxQMSzCKJGLfiCNHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی هم تر و تمیز و عالی</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/4185" target="_blank">📅 21:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4184">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">فیلم آموزشی Clash Party
https://youtu.be/gMFH88yRghg</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/MatinSenPaii/4184" target="_blank">📅 21:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4183">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">سلام خدمت همه دوستان
✍️
سرویس ساب WhiteDNS در گیتهاب راه‌اندازی شد.
✍️
اسکنر های ما هر ۳۰دقیقه بیشتر از ۲۵۰هزار کانفیگ را اسکن میکنند، از خروجی این اسکن تست سرعت، دسترسی و DNS Leak گرفته میشه تا بهترین کانفیگ ها جدا بشن.  نتیجه این تست، هر ۳۰دقیقه داخل…</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/4183" target="_blank">📅 21:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4182">
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/MatinSenPaii/4182" target="_blank">📅 21:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4181">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">بن شدن حساب‌های کلاد واقعا نگران کننده شده. هرکسی هم بن شده از ایرانیکارت خرید کرده یا سابقه خرید داشته</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/4181" target="_blank">📅 20:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4180">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">بن شدن حساب‌های کلاد واقعا نگران کننده شده.
هرکسی هم بن شده از ایرانیکارت خرید کرده یا سابقه خرید داشته</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/MatinSenPaii/4180" target="_blank">📅 19:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4179">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">☠️
نصب و استفاده از Hermes، آینده‌ی هوش مصنوعی
⚡️
فایل لینک‌های مورد نیاز: https://t.me/MatinSenPaii/4178
⭐️
توی این ویدئو: 00:00 چرا هرمس؟ چه استفاده‌هایی میتونیم ازش بکنیم؟ 04:17 نصب و راه اندازی روی دسکتاپ(ویندوز، مک، لینوکس) 13:47 نصب و راه‌ اندازی روی…</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/MatinSenPaii/4179" target="_blank">📅 17:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4178">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/4178" target="_blank">📅 14:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4177">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qHTBkrU-WksOkkTOkvR2wSU2SGfRCbt86GfuP8JMgDbKDwLh0sV97bOy0rGdrFMvHJMrHfQ7tNTZpCM1goY3-87BYZYrG9LlzBwPp1ZKxeExMdFklVVTwCG6yC3Ba8WVYK5rLyPidAtKIZNhaymgDFBW8PDnzotL5wUNQ5ntdYcf50m08Zxr4xjef2vFdpThLN66czcQEdUZd7rLhJYLjyCz71EWQfwCAXfHWDtLozv10In2vC8AYBpp9GC99DxHgtOjmgExKfuIDe2ydcc_no7ImgUUverdlSCalC2wIxDv43AsfxRMBn9uoRAJgyPvAtE2WuiX11r4Qsb3RQUb2g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/MatinSenPaii/4177" target="_blank">📅 14:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4176">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ویدئو 2 ساعت و نیم ضبطش زمان برد، بعد از ادیت شد نیم ساعت
😭
دستم شکست انقد با موس اسکرول کردم</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/4176" target="_blank">📅 04:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4175">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KbNOt2hiRexN0VnG5NC-Sq7-m5TNrPGxb4Mv-cUTpGiWXG5968peFdHdmd2y-bZ331Ze-SrJHc3R0muG4F4t1rSAuMr-u4fXhnHLz-EF2rPcIZ4vM9aA6Edk3Fy9rW9vLQ2xILWJXvZ8_1wBOfdHHrT81lAFw70hsnJSjLRe7uHltvN_dbk3BxQa06rIFYOYnmoGt27vGVQcyeFCfIB6gXl8SoKiQrVYTWOvC2KWbwJuoHV9EL9M7gqSuXtG2GEr56Ec03tCaIj2wSN3SKvbmjT43kK99uQh3pCfazZ7gIMh6HyRL-JVyDgF1Scrmg4Oz17NHrwldKPQ3As7xrRfYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این وسط دسترسی به Fable هم برگشت</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/MatinSenPaii/4175" target="_blank">📅 01:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4174">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">وسط ضبط ویدئو به طرز ضایعی یه ۱۲-۱۳ بار به ارور خوردم
😂
(اون پشت حلشون کردم و شما قرار نیست ببینید. هاها)</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/MatinSenPaii/4174" target="_blank">📅 01:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4168">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-Desktop-1.0.0-beta6-linux-amd64.deb</div>
  <div class="tg-doc-extra">19.1 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4168" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/4168" target="_blank">📅 22:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4167">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PsnX9JyxstaVgsR4OggjxsCAhsdCf2Jjsw2MDTrBqEgzAgJIwv2rhRH8c4v3DN4Ln2E6UsFZ2E4Flwk6CsCtmUBGEqk2aMH-NWIibRUcEI6o77mTdvwCUevbgfcLcoGZd2xaEXLrc4BbVIAGHyxKgmMUbidVh91o8WXE8VYiRy3BkFPso0mKvYnx5mgNeABKMjR7EpZ3O7FQN9mo2TdPs_bIzTQ6aY0BPSsdeXFGr19mjEVst_Ar46j5kHb2Ms5nGtDXXt3EXkr__uJy114TML-gv9B70zdoC-lpLhDvV6l9tK9SJoXkZSKVajIn2tegxC7dW8Wfdvrxi-FVlMN4Wg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/MatinSenPaii/4167" target="_blank">📅 22:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4166">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K2-Zw3FXL0JfZZk3SyYYCc4J5VV55JRLkVGvoAurz7ssdFMDb136PTh2VAQ3QuAd0-37XCIHFfSxQvmfaXI4wlvFTIGx127zwsxYgF1nT-9kUYm8s8B0SRhtdD9KhHLxaArssIEQlfUKlO29Dhl-_iHbCMg51LAVq2qg_pFb5UMZNCOXZWNlNWoKbrO4fs2hPm56Bm4PIp5LBmcXvkeyG8CfdkQW5ze3MkMygzPaTxRL3rbhWzyWrAMrIzDfxJeTL30zFUdlUt35fnRfFq5A76-ngFSWWXs_08ihrRqm4m9wvs-FOGKTUvunuU8_kwu851fDlm2lLsFy-mTtnoW-aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این api هایی که Nvidia میده واقعا سخاوتمندانه‌ست. 40 ریکوئست در دقیقه
با 9router انداختم پشت هرمس، چه میکنه این Qwen و MiniMax3
توی ویدئو آموزشش رو میدم که چطوری بتونید وریفای بکنید و ProxyPool هم بزنید که روی سرور مشکلی نداشته باشه(مثلا با آیپی سرور من مشکل داشت انویدیا که با یه رله کلودفلر حلش کردم)</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/4166" target="_blank">📅 22:29 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4165">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">کلودفلر یه درگاه جدید معرفی کرده که اجازه می‌ده روی هر وب‌پیج، API، دیتاست یا ابزار MCP که پشت شبکه کلودفلر دارید، سیستم درآمدزایی پیاده کنید. تسویه‌حساب‌ها از طریق پروتکل باز x402 و با استیبل‌کوین انجام می‌شه؛ یعنی عملاً دیگه نیازی نیست درگیر ساخت و پیاده‌سازی…</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/4165" target="_blank">📅 22:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4164">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Kn19dWlAnMNQ9_c7gzTGxXi_xjmU3bHpIZemDnLkMA6lTOlBA6ubvM_sSrt33D3sAGk_d1aBgaeobXs3ihif4ZQ4vf4z0HhbZNEh0qcTrq1igZkUvX6aK95yVZ78_-BTt1Ur8GccdgdSTFhLRh-OfnR3Nzw_ms_Ihn2R1lF6S5neLqx0cNUHAQa_Sx--Tmddqvyt8mGWaBL_i1Jafy8p2XguYW1YFFFCCvr_xp-UThb1hlSqXfTDXL6jeUtOKSfgIGGfDX_XKTARbFrab-_YFWvPXTZtwfjfXK1SpZ91mqLNvGZPWv00pbKxrSMYBgeeVaKL8EzxMqjV6dX3vngNHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر یه درگاه جدید معرفی کرده که اجازه می‌ده روی هر وب‌پیج، API، دیتاست یا ابزار MCP که پشت شبکه کلودفلر دارید، سیستم درآمدزایی پیاده کنید. تسویه‌حساب‌ها از طریق پروتکل باز x402 و با استیبل‌کوین انجام می‌شه؛ یعنی عملاً دیگه نیازی نیست درگیر ساخت و پیاده‌سازی زیرساخت‌های پیچیده‌ی پرداخت هم بشید
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/4164" target="_blank">📅 22:06 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4163">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">از بین سایت‌هایی که تست کردم برای SMS، کاوه نگار که باید میرفتی از دفتر اسناد رسمی احراز هویتشو انجام میدادی، فراز اس ام اس هم که شیش ساعت گشتم اصلا بخش API پیدا نکردم. بیست دقیقه وقتمو تلف کردن این دوتا تا وقتی که رفتم
sms.ir
و همه چیش اوکی بود و 10 تا هم پیامک رایگان داد. خیلی هم سرراست api تنظیم شد از خارج به داخل هم دسترسی داد</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/4163" target="_blank">📅 21:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4162">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">تمام رادار جنگ الان فعاله و AI هر نیم ساعت یه بار، خبرگزاری‌ها و پنج-شیش تا کانال تلگرامی رو چک می‌کنه و اگر جنگ شده باشه و اسرائیل و آمریکا به ایران، یا برعکس حمله کرده باشن، پیامک میده</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/MatinSenPaii/4162" target="_blank">📅 16:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4161">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PmB-Myd6xPKe-86TUe-37vzMw0Sy_2V7GBm5JduMy32HDoVc-QC0Git1_ks9KR1ZEvWj5EiGnRciuXbfDo3bQBTz5mI8j8seWG0hUWK2VguEUDm1SiCMdd-pEzDcP-_aREGJ8w25wsKdXbFMbulUxcaX8fUIesurHG-Z5D9Z3cbLM-IEbKJ6nTEQDjezZxhOFVl8UCMSKWKKaeWd88DjXNQ6oD-doix7Gtyb5B5z1kSUMlbxUE4W62r-p9GxpY_3PX3kNjRYKa27bZB17cdAvO6X4_802ibwi84aqnA5OKZP0EiT6I7ipxVP1Z49e6D-xiLo-yO7NYSMhkb_6LqKfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌خوام باهاش یه رادار جنگ بنویسم</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/4161" target="_blank">📅 16:26 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4159">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">می‌خوام باهاش یه رادار جنگ بنویسم</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/MatinSenPaii/4159" target="_blank">📅 15:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4158">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Qt0H_ZAtdM_jmDCzcTVOm4LWhuYfZS_ZAqsw3xVeySh5jzERMQWeg2SONXVhv3kwGMiT5zG0Vka-0135myegDDjGMawiKNpiM99iW8r1ODMlD5Z2-SLvW_ft9-X4eukLYb4tDJ8R0fFNWbAWn4i98u6_JCCMO4uYdRkdH4I2e3cbcpGOA2Ue2Msarec1OvwXeW_ltBymZOHZmUDQovw-Z7arB7h8TBpuxxSwdSdMvaEkU9eWG5J3SmTcql17aVQnmDk9OrDy9KRZ8KZSaw1ZgVXryo3s7hJcpAgCUJhb-yuTsV3nvCG9VJ3UzzLWcR8K7mXlUkSXNa82WztfNyYuJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کمی برای خود یادگیری را شیرین کنیم
(دادم همه رو هرمس با gemini 3.5 نوشت چون هم یادم میره چی رو تا کجا دیدم و هم همه‌اش هی چک میکنم که چقدر ازش مونده و الان درصد دارم و اعصابم آرومه)</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/MatinSenPaii/4158" target="_blank">📅 15:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4157">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">می‌خواستم ویدئوی هرمس رو ضبط کنم اما انقدر برق نوسان داره و هی سه راه قطع میشه کلا برقش، اعصابم داغون شد. می‌ذارم یه کم برق بهتر شد میگیرمش آموزش رو</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/4157" target="_blank">📅 14:55 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4156">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">همین الان ویدئوی یاشار عزیز رو دیدم، و باید بگم دیدگاه فوق‌العاده‌ای میده به شما از ai
اینکه دیدم یه سینیور چطوری بدون گارد و با آگاهی و مطالعه‌ی کامل از ai استفاده می‌کنه توی حوزه‌ی خودش، واقعا لذت‌بخش بود.
نکته همینجاست
با این ai عزیز دل، حتی باید بیشتر از قبل مطالعه کنید و دانشتون رو بیشتر کنید تا برتری داشته باشید نسبت به رقبا. و قوه‌ی حل مسئله‌تون رو تقویت کنید و کارهای تکراری یا سنگین رو، به راحتی بسپرید بهش. اگر به مبحث باگ بانتی هم علاقه ندارید، ۱۵ دقیقه‌ی اولش رو ببینید حتما
https://youtu.be/-Rt_Z0allhM</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/MatinSenPaii/4156" target="_blank">📅 13:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4155">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">متا قراره برای استفاده از عینک‌های هوشمندش ریت‌لیمیت بذاره
😐
و یه مدل پرداخت (soft paywall) داشته باشه که باید ماهیانه اشتراک تهیه کنید  لینک خبر
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/MatinSenPaii/4155" target="_blank">📅 13:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4154">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WOn5TrUopjfz3WrgWzQWJ5bfIoeW-JHpp2FtpNYBo3STBqgTVIA3ZZ6rTWHzaeMPfLW_WM3s-si4BIjzTFPe-29RVbDs7QhNLJno2Jrmcr-xle8XJTTAGA5oM1Ex0-A5r9w1pp2xzSHOzDQexWoLC9vmPvO_z5Eg4vJQ9cNdw_fudtJNqDdRBq4bFYVyR4yEUkkasTBBH0cTeak9WPLdqOkWKY2re0J6e6ebiAZpeCE4AergU89aqX6P3r-jJPQLyFlgwWD5C3xWU8-a-0ZjaPMEmOxe5X8pVdbtB-fYjTAWquvIJfPcwX5dZwQzGSclFNnqkPe2aRfoyBuLr7Cytw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متا قراره برای استفاده از عینک‌های هوشمندش ریت‌لیمیت بذاره
😐
و یه مدل پرداخت (soft paywall) داشته باشه که باید ماهیانه اشتراک تهیه کنید
لینک خبر
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/MatinSenPaii/4154" target="_blank">📅 13:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4153">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/guGFjFcmCNqnhaZBhIgdF_jtH6sFXPXOlw2QS9GKyAF4aFcJ6wbzoAvVeXN_qT5KKos1QjImIo5exD_2ZFFWt03tYrPlNhg2y7olUlOCko4Gt1RyBIGctf4Q_eznjquYbnINaOfai6mYFl8dpAFZIsZbNkms-1uQG5BCkqbdEKJt1NJoPHacrr3Nr4v0Lh4C21AKxJ5G7CpTTM4gdbukkzPTBVcIpdcJC9Bjm4JyNN1sCfoo5jsyD2sAtpDZf9GSG8eASe8-klmINUXvwpflnD7AMtOWN4Bv68stCSGxZ4Cc0X7DgY1kdR4y1IizU79wo6maalnrzrfjZEZjuqSXvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">غول چینی، GLM 5.2
همچنان ارزونتر از حتی Sonnet 5</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/MatinSenPaii/4153" target="_blank">📅 10:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4152">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">خب گویا کلاد Fable 5 امروز برمیگرده
😁
آنتروپیک گفتش که با دولت آمریکا مذاکره کردیم و امروز مجددا مدل رو آنلاین می‌کنیم</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/MatinSenPaii/4152" target="_blank">📅 10:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4151">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JuRCrD36dqTbQQ6AmQcrmFZrI-kn4JXbJbtz3pTmExeUQj_rYNbuLq55FjQhukaUhVsZq4KiZyOBXiaoi7eunkiupdnYbZjuHu_i7tJZTFsSaNOOKbNvNzqRlQ4AOLKntR9J6f0ImTEB5rT0ykSSeGv_MGy_rl5da592S4la2Eel-cCcJ5YI4_qhkXcenO309swmotubvyKlGD14iTN3ZermNNIxiacUayCnr-DQdT5a6hleUY83DqUIa7u7qjr2XVF0EIi7xC1S8eSDrZAiJJZd_3v5nZbDoM8bim73HDBeJW5i-FQE7GAGxTTnq38oaf5ltqqae4Ck98IdEiVhoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انقدر هوش مصنوعی‌ها چند ساعت اخیر آپدیت دادن که نمیدونم کدوم رو برم تست کنم
😂
وضعیت عجیبی شده</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/MatinSenPaii/4151" target="_blank">📅 01:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4150">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">انقدر هوش مصنوعی‌ها چند ساعت اخیر آپدیت دادن که نمیدونم کدوم رو برم تست کنم
😂
وضعیت عجیبی شده</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/MatinSenPaii/4150" target="_blank">📅 01:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4149">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f2ffa3ab51.mp4?token=aS0XtgjksWQ9xkBurAvP-rm6eYc2DcUhCoJT-uk5qvrdkCRxGgARK68yUHAhfon3CZibSVpAIeTZzfrW-pyGUCRUM2rf-RZEWWipdHewDkloJLnCisqaRe1-VBBiagsEoxvzp66hrX3DyvOVM97HgrnYpbr7BD0gPbjlTs2v7xWBCOlolXwff2HHkR9Me4dDainGD2vbbmUOx9K0Lo5Oz70GnBkgLTCewwbr8kXR_aSwJvEanMq13LJNgHAoCSd9GZmticN5ZsZPN_KGDeBzWgvlmAV5dUwXCwvEUHLvdIUCX3Fd2TuwCkFslLqFtn04oD1F4yc98qyYNtYX50uKVA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f2ffa3ab51.mp4?token=aS0XtgjksWQ9xkBurAvP-rm6eYc2DcUhCoJT-uk5qvrdkCRxGgARK68yUHAhfon3CZibSVpAIeTZzfrW-pyGUCRUM2rf-RZEWWipdHewDkloJLnCisqaRe1-VBBiagsEoxvzp66hrX3DyvOVM97HgrnYpbr7BD0gPbjlTs2v7xWBCOlolXwff2HHkR9Me4dDainGD2vbbmUOx9K0Lo5Oz70GnBkgLTCewwbr8kXR_aSwJvEanMq13LJNgHAoCSd9GZmticN5ZsZPN_KGDeBzWgvlmAV5dUwXCwvEUHLvdIUCX3Fd2TuwCkFslLqFtn04oD1F4yc98qyYNtYX50uKVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شرکت Anthropic از Claude Science رونمایی کرده که به صورت اختصاصی برای مراحل مختلف کارهای پژوهشی و علمی طراحی شده.
توی این نسخه محقق‌ها می‌تونن کدهایی که مدل می‌نویسه (Artifacts) رو به طور دقیق ردیابی کنن، محیط‌های اجرای کد رو بر اساس نیازشون همون‌جا بسازن، و جالب‌تر از همه، بیشتر از ۶۰ تا دیتابیس معتبر علمی رو مستقیم به کلود متصل کنن تا تحلیل‌ها روی داده‌های واقعیِ علمی انجام بشه. این نسخه فعلا تو حالت بتا در دسترسه.
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/MatinSenPaii/4149" target="_blank">📅 01:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4148">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9603918fce.mp4?token=BHpWL2XWKEw4aocJe5LsRpFPNU9DJBimfq4vYQ-Iygn5uXgLZIEDD3_Il-Lf3v_l25lx996qAwl3p1Q4FSXKoR2ZzodLONdDKDnekwjT-GPXGWen36V4LK1HPRoIWCHm60EMgCyoph9FP17t95X2l8YDBzzAfjLqQmlhQt0VOrQXVbp9eVkrsQCAb6KT7mLVVgzZ4WprEsDqAd5Gq5nhgNxpMsDYHgMp7eegvbAn0gTImgw1olTftWC065AdLjNBGdZnHZPMf90HmkX23CGuxDx4d5hILJA6O1I2KYcRT5uAk_Z-MTLfpAlLRxhPMBCzuduITrNaJaPfxaWwhj8dpg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9603918fce.mp4?token=BHpWL2XWKEw4aocJe5LsRpFPNU9DJBimfq4vYQ-Iygn5uXgLZIEDD3_Il-Lf3v_l25lx996qAwl3p1Q4FSXKoR2ZzodLONdDKDnekwjT-GPXGWen36V4LK1HPRoIWCHm60EMgCyoph9FP17t95X2l8YDBzzAfjLqQmlhQt0VOrQXVbp9eVkrsQCAb6KT7mLVVgzZ4WprEsDqAd5Gq5nhgNxpMsDYHgMp7eegvbAn0gTImgw1olTftWC065AdLjNBGdZnHZPMf90HmkX23CGuxDx4d5hILJA6O1I2KYcRT5uAk_Z-MTLfpAlLRxhPMBCzuduITrNaJaPfxaWwhj8dpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نسخه جدید Hermes Agent سرعت خوندن صفحات وب رو ۶۰ برابر بیشتر و هزینه مصرف توکن رو ۴۹ برابر کمتر کرده.
تیم توسعه‌دهنده‌اش، Nous Research،  با حذف پردازش‌های میانی کاری کردن که دیتای تمیز مستقیماً از بک‌اند به ایجنت برسه. همچنین برای صفحات طولانی و سنگین، داکیومنت‌ها اول روی سیستم کاربر ذخیره میشن و ایجنت به صورت صفحه‌بندی‌شده و فقط در صورت نیاز اطلاعات رو می‌خونه.
این تغییر یعنی کیفیت تحلیل و پردازش هیچ افتی نمی‌کنه، اما زمان و هزینه‌ای که بابتش صرف میشه به شکل چشم‌گیری کاهش پیدا کرده. و یکی از نقاط ضعفش یعنی مصرف زیاد توکن رو پوشش میده!
کم کم تیم Hermes داره یکی یکی مشکلات محصولش رو برطرف می‌کنه و امیدوارم همین شکلی جلو بره
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/MatinSenPaii/4148" target="_blank">📅 01:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4147">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l9REUXuN6Kcu3B8Df8vTPU9hNGbRt9ggUyWsIOkdW_2rFrnzIkVj1GlTDNNQQEyyKJMQTgHabjIA1fTOZ8e0jL_DD9_hQ-VHQ8DFXylVXknRFKGsR9FI7kr00ojk0Ld_8OvekOe3IFBPsgxiwq9enBBBJm6PK-jEHJFyw7bHoxfv1D2Oqkb2VZ7_ev0dUs0kBpTKRoGb-OKLinhWdLRWKPkhtkOH1JX5DF2Cyx63xL8qNJ9JNNqqkUKDJeACEvHV2QnX8Nrub8wSCVe6bxoZmn-VP1pvjdgToaOapitmMCmCvTqdntT369Y27gd5R-7o7fKIogF8Xv5gqKjZwBZjOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم بنچمارک منتشر شده توسط خود کلاد</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/4147" target="_blank">📅 23:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4146">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/O9Hjg_zX-izrjILL2hsPXbwwzOtAJ9WDTL1yzdECeWhU0jpLWVXnT2wth-qWVMzA-9_TffF381jUDFx862TCo7NT3rz8gYIppf8gEc2n8gsC-lUN02ON_-fJqTknWikNB_IuAVVlF6eMFYHSkjPZh9ts76ZW2dzlOZ3yjk2bYdmMgo4WJyMWG2lXkAzrYzEKewHSnR9HSIuulxgLCyVvKR9v8cx8wQ1cNcianwi0-3H7GuI2t6uzz4J8VA_WJ6mJWQYaDPZGqW6Uwm74wIydphMajDLEDcCg5ozy2-WreUywtGi_zKu1j1-g1k7XNOEJZjkTce-FxkTJ4goYAxbGew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسم‌الله‌ آنتروپیک Claude Sonnet 5 رو معرفی کرد همین یک ساعت پیش</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/4146" target="_blank">📅 23:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4145">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IWpghatrwI-60q8EiTgn0gqBiXMgRBCUTJQ0Ex6kdDJ7jdQLrXgK-UMDI9A3cN6oRdo0h4Lk89V_7lwJSmJA_DH1UF0hQSBDvJ2F9WrEgt74O6_FQtYZYSxW3hmF5TdDpFX04bMJoLkgPW9iMoZm6Hf09CXQr3hoWyb9BiX528ELOXle3C0v62T5BoIiN5EvUaUXBiEbjku5eB4s7NOkKZMDte2Ci4CFKvGcX12wIVYBKe4-e5FuhyBN_kB1XSKR93mx0Osl4w7Py8FWs2P-bGtUXr5xaOw-cbNycvL425AVB5Y8S1qRskAoAzduWwic1VF9BzMq7NSgBYXoIkfC5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسم‌الله‌
آنتروپیک Claude Sonnet 5 رو معرفی کرد همین یک ساعت پیش</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/4145" target="_blank">📅 23:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4144">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">پولسازی از طریق کانال‌های انیمیشن کودک با کمک هوش مصنوعی!
🚀
تا همین چند وقت پیش، ساخت انیمیشن برای کودکان نیاز به یک تیم بزرگ (نویسنده، صداپیشه، انیماتور و موزیسین) داشت، اما الان با ابزارهای AI، یک نفر به تنهایی می‌تونه یک امپراتوری محتوایی بسازه!  این ویدیو…</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/4144" target="_blank">📅 23:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4143">
<div class="tg-post-header">📌 پیام #22</div>
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
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/MatinSenPaii/4143" target="_blank">📅 21:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4142">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J2kKHGUxztORaeX8yLL4s8qLQLshznxN-sxA8YOy_sVO_FwD6qlg0PLl5E3GNhht83miWoUr62o8HBKsJN-5z4Bi-96wqgR4eL5pqHDHL83H1wMe50hv1bTvLWm6db1A-ab83FRLte4JBYxAcrQ2LkTPu_wpYTTIXjQ1PSHeUY_289x9qi7COAQGZOYsVVRZE0OAUwYdvXxPr_gQodhNb0Vdt0gq2mRCKH7hKSFWWNv3sE4FXwfUAG7YRLWDMsMu6xCw3D8tcJE8M_jGFMe3LAu6mQefGkWwwWK8zVkKIzVon5K1S3gZMNIcIBDSgTqhBpnQzbf_IdYrn7OWspc_lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوتوب یه قابلیتی آورده به اسم Ask پایین ویدئوها، که می‌تونید وسط ویدئو اگر جاییش رو متوجه نشدید از جمنای بپرسید
🎨
فعلا برای وب فعاله گویا</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/4142" target="_blank">📅 21:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4140">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">برای نصب کردن 9Router روی سرور اوبونتو اول sudo apt update && sudo apt upgrade -y curl -fsSL https://get.docker.com | sh sudo systemctl enable --now docker و بعدش این دستور رو بزنید docker run -d \\   --name 9router \\   -p 20128:20128 \\   -v "$HOME/.9router:/app/data"…</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/MatinSenPaii/4140" target="_blank">📅 18:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4139">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">☠️
این شکلی از هر API ای استفاده کن برای هوش مصنوعی🫪
⚡️
لینک سایت 9router: https://9router.com/
⭐️
توی این ویدئو: 1- یاد میگیریم که چطوری از اینهمه API Key رایگان استفاده کنیم 2- ابزار 9Router رو نصب کنیم و این API ها رو اونجا جمع کنیم 3- کلی API رایگان…</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/MatinSenPaii/4139" target="_blank">📅 17:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4138">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">انقدر برق رفت و اومد و نوسان داره روی محافظ میترسم لپ تاپ و همه چی بسوزه آخرش. آقا بیا قطع کن همون دو ساعتو، نخواستیم</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/MatinSenPaii/4138" target="_blank">📅 15:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4137">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">بیشترین درخواست توی یوتوب و توییتر ازم این بود که آروم تر صحبت کنم
😁
من فقط نمی‌خوام حوصله‌تون سر بره یا وقتتونو الکی بگیرم
اما از ویدئو بعدی سعی می‌کنم شمرده شمرده تر صحبت کنم</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/MatinSenPaii/4137" target="_blank">📅 14:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4136">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/We0B3DvFMDLPAPUssqQVj5GxY28wJXRHuOJh1DH26xx6EJtwUMNaUHvySdpGUEXh5YsOrq_R_xR9TMn_6rLn59tbMSqi3g84oPJXgtp9q726mVOUsd4ZTWNYJXRQlteXDmVfyL1ojv__uaG9c9zRN8f--n-vg8v8Yd7hHv6xZpm0A0QGnUhr8jOxCvMb9YiIWUMvuqgqZMMLgQhRLNwAz4H2E8_2aLZ_37SlQDH4fhWvQNiCLlHYhGQeYA4MjoSR-W_VflIYEJ3lUIm0oJY6ATWyq-mOSrEFYjSVD2w6htbKI6-xIeZwt8_D83yeVApiVNGigfuiSFURgu6szzAPQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مورد نسخه‌ی موبایل Hermes، من توی ساب‌ردیتش دیدم که یکی واسش نسخه اندروید ساخته و Pull Request زده روی گیتهاب(که کدش ادغام بشه) منتها هنوز، رسمی منتشر نشده</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/MatinSenPaii/4136" target="_blank">📅 14:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4135">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4135" target="_blank">📅 14:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4132">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pgCP2WmK47C11-1vykPtw_aaZg3Woz6NZIxngorkoOkHY_8lHG_5FofHsm_ZrZ7vJIhLcrNPjFXUDiD4Bb7u6dmuB2A_y_23xyI0b9gQ6c3Ckqh4q_uAaHYe68BU9Tbc1L0Vcnw0-_7SeDkQDLSFHQHpg94UEtjzbYyiJgBySuoJYNM8hHMdre0ZrM69y9-htijPP1m4MGoWUxtOgyvie-lQC0JzHXx7O5gMDPE1dRrmUOZHrD9pL07CvZ7tjUQui27_W_dfWVN4ifxxY0IK3NfGzln0RIbcvmGViiIzXlnYCdgviOAx2Jhl8R9D537iPju2NzBupmNt1zfnQ96BUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SrKvEtaL_A56fGHSMFYHTkfSeHwFGfC3TNdwd97fmVjNAdStbXVTsxrhKscDhdJG7DqT5wF_yJmWA8ivudnfVRjUNcOQePjoxh0tesIhvtZ50d1Phvrs9w4aSNUaAT4eKgOWX7bKZBUTM63PfF-KqcEHxeRDjN-niBwVOzgHrtXpEIaXgq06Sd692WufQfe1cPcUOM1mPKCDuoSxCQCt3EnesbT74EItj8ChkhUP5S8onRCcBo7cT9UiIEdxzprcACGa2qPAVP7dNKfZknBSAAOzQ0Bli-vWOiNuFbbV2tCRGDsWH-UFz0tQssskR1zQ7LGyLm9FkmZEzGUsb6qj3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ReAAYyUaW9-Zp5bns9zlDWBOlYJWCGnlpCRIXnZqJNnARv0DaVqDP0jP14yU86_mD3LIcxWkb1Fg2foZMILsWV3k1BPmG_jwu1QWNNveRXTK_tFNm7up2uI0I4apVFxBVGcxUlpX3sfgyoa0jv3g5BpfGeXtuWmy9maV4Pkg5kRjd2NfC2CHeXAA76PQQAjQ0uDf1jcR9xcZaHOBwFuv9TIsHuIfPeBM9aQ9Fd9O8ehD35upJ75tkLII5xYFSv83GtnXCZ1EX0R4b441yw5ksfS7Qn1yS_d_kbGEvUU85uDlq4jq-7IEif5VQ2PT4jhqvFaEwmcekljT339PW9RPng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">واقعا Hermes و وصل کردنش روی تلگرام، یه چیز دیگه‌ست!
فقط کافیه ازش بخوای، و بوم
انجام شده. ویدئوی بعدی، هرمس هست
👀</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/4132" target="_blank">📅 13:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4131">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🚀
اسکنر WhiteDNS  اسکنر WhiteDNS ابزاری برای اسکن، تست و مدیریت آی‌پی‌هاست که در دو نسخه در دسترسه:
💻
نسخه دسکتاپ مناسب برای اسکن‌های سنگین، سریع و حرفه‌ای؛ مخصوص کسایی که می‌خوان تعداد زیادی آی‌پی رو بررسی و تست کنن. https://github.com/WhiteDNS/WhiteDNS…</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/4131" target="_blank">📅 08:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4130">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hPby7hIjxEIUh_3GC5HKNVAMUQZnz8O2X_TZq5_LnGzhLmvhWhL4GpG5DSyDJKuK4G2_RbEAJg2Kvl0eAl0gYgGpjShTXFlXXbBRbryV9_PulUBXd2M_kAyHPfqkR7e4XKXf7Hd2dc2eV0kEOiePdV3rTEmygfpLxWuLaYYKKwRupJy2qiGsmpxbHZOrMD1o2yGEFUnzP4cycYpTarR6BY3FpZMqzpjqFAg7ShbymlmpFr42zJ1h1-u3WlHDpVQH4T2dmOimnWV0_jAavAut-g4J_GUON8hUSpvHrkWJtGt5dtfctfdUqIUhccN2wCJDor9gdpRu93gS3403omOGeg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/4130" target="_blank">📅 08:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4129">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5950435463.webm?token=JnTzZZSpIex493V5rUNfgV3RSUK-h4fC7wsf8N-k_fWB11fKAz_fiYgye3xDo6XwqJy6SDVnxWCaqD8zzbCTaz12jfDjTKPzSUZBYQnM3cIukW6Cp7byZvp_4JA79h3uC1jv1Y0KrQeKTyDa0NdV1W0U54lZuo71vqg4Ckj6Cpd6U-0-L5COtehsfpg86Y6RcVg7wvxO50i2-DVnxr_FeEHwg04wKEa6A6SALlqpYmYQftezO3FdBkeoQIDkYbNDVnWBwMQrV6x8iuvvXdRZgUR0rkvwtXn8ryIKBVln3MF-8yQSjtoGTsvY6gGUT-wdq6ZgY9a3ytjdLyjNZL678w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5950435463.webm?token=JnTzZZSpIex493V5rUNfgV3RSUK-h4fC7wsf8N-k_fWB11fKAz_fiYgye3xDo6XwqJy6SDVnxWCaqD8zzbCTaz12jfDjTKPzSUZBYQnM3cIukW6Cp7byZvp_4JA79h3uC1jv1Y0KrQeKTyDa0NdV1W0U54lZuo71vqg4Ckj6Cpd6U-0-L5COtehsfpg86Y6RcVg7wvxO50i2-DVnxr_FeEHwg04wKEa6A6SALlqpYmYQftezO3FdBkeoQIDkYbNDVnWBwMQrV6x8iuvvXdRZgUR0rkvwtXn8ryIKBVln3MF-8yQSjtoGTsvY6gGUT-wdq6ZgY9a3ytjdLyjNZL678w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/4129" target="_blank">📅 04:39 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4128">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">☠️
این شکلی از هر API ای استفاده کن برای هوش مصنوعی🫪
⚡️
لینک سایت 9router: https://9router.com/
⭐️
توی این ویدئو: 1- یاد میگیریم که چطوری از اینهمه API Key رایگان استفاده کنیم 2- ابزار 9Router رو نصب کنیم و این API ها رو اونجا جمع کنیم 3- کلی API رایگان…</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/4128" target="_blank">📅 03:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4127">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aTP8UefNufnspFXGLg93RMRXQgkR3NULn6Vfex82iv5-rXLS470GuteNT92tWmpY-dWTDYg_4YJQVinxtqE0Y2smM0UFNJZg-xD0U5Ka-xfHYdAZyLh9Xq4gwaH-rBirsPZlWFF5tf_EIU8tJydlSNiONanb4MvMiEjNPOIWjLbetxJzyX8_OdTJxrPPYgzxV43RUCh-fGcFJW6Ylx1JyI9rDW-8f-opUcYbD8caXmLg3cnx6V73vbnuXPteE8F2MOLlK9nAW1fs8zhVCwL6HZuWUhXFUIfH68GQqwsEfEv9lDK-vh-gX8m1EscykRVzTB6LljGIMe4tHgyRhGK9_Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/MatinSenPaii/4127" target="_blank">📅 03:33 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4126">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">وسط ویدئو متوجه شدم اگر کانکشنتون با api ها خصوصا جمنای قطع میشه هی، می‌تونه مشکل از proxy-ip یا آیپی تمیزتون باشه
گفتم این نکته رو بهتون بگم</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/4126" target="_blank">📅 01:28 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4125">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">کمی ویدئو API بیشتر طول میکشه تا آماده بشه
صفر تا صد تمام API های هوش مصنوعی رو میگم بهتون
محتوا رو فدای سرعت نمی‌کنیـم
🥰</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/MatinSenPaii/4125" target="_blank">📅 21:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4120">
<div class="tg-post-header">📌 پیام #6</div>
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
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/MatinSenPaii/4120" target="_blank">📅 18:18 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4119">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">اگر نمی‌خواید این بلا سرتون بیاد و کس دیگه‌ای بفهمه ای ایران هستید از وی‌پی‌ان‌تون، از نسخه‌ی جدید WhiteDNS استفاده کنید</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/MatinSenPaii/4119" target="_blank">📅 18:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4118">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ولی GLM 5.2 واقعا عجیبه. قیمتش روی api تقریبا ۴-۵ برابر از Opus 4.8 کمتره
این چینیا چیکار کردن با آنتروپیک، خدا میدونه</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/4118" target="_blank">📅 18:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4117">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">☠️
آموزش استفاده از هوش مصنوعی MiMo Code + پروژه‌ی ساخت ربات تلگرام با AI
⚡️
لینک‌های استفاده شده توی ویدئو:  1-فقط گروک استفاده شد. ویدئو رو ببینید متوجه می‌شید: https://grok.com
⭐️
توی این ویدئو: 1- یاد میگیریم که چطوری از هوش مصنوعی استفاده کنیم تا ابزارهای…</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/MatinSenPaii/4117" target="_blank">📅 11:59 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4116">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">تمام سعیم رو می‌کنم که سری ویدئوهای AI، برای همه‌ی مردم مناسب باشه. تنها خواهشی که ازتون دارم اینه که نترسید، وقت بذارید، و ویدئوها رو ببینید و کار با این ابزارهای جدید رو یاد بگیرید
🥳
خیلیا که کمی از این فضا دور بودن، فکر  ما داریم راجب چه چیز خفنی حرف می‌زنیم و ...
در صورتی که شاید تفاوت درک و دانش ما از این زمینه با شما، صرفا دو سه روز کلنجار رفتن با ابزارهای مختلف باشه! همین.
به محض اینکه کم‌خوابی ۳۰-۴۰ ساعته‌م جبران شد ویدئو رو واستون ضبط می‌کنم
🤲</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/MatinSenPaii/4116" target="_blank">📅 11:36 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4115">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aKC7ySpkW9tbrFynBvbfrY0dYQdPlnUc00xp5mqwhOzACve9rrZ_8oTA18crrg3MG1c8J2Duk8pxmXEcz6rRsTSoSASR69cdXEN09hV-Cil_0T3YyLB_MjmgbRm8O973lFsngLV7ukCkthkoAwJ9DADQCQx9UdjL6rJfmb8ZD4-v0TgF7GM1y17hsRquhchwEXnRdQvdRB3Tmbi1Tac4GbSBC-LHX409N4VkWEWcxJ-3BMFAbwloIefc2TgPp2-WSomus_WgL7ixPT3jkVztGjMap-LhMymF7HHbWK2Fq1rGCsO-r8mK7XKxR6iCZZPreWOVVyIrMGlGHDtrchXOzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت هم دقیقا شبیه همینه حتی قالب‌هاشون یکیه
😂
https://api.bluesminds.com/register?aff=drPB  ۱۰۰ دلار میده باز هم میگم مراقب باشید و توی پروژه‌ی حساس استفاده نکنید</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/MatinSenPaii/4115" target="_blank">📅 11:18 · 08 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
