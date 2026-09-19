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
<img src="https://cdn4.telesco.pe/file/KAyfCbHIOFfzUwuAWOtccekW7gSsx-stCduXDCrodh-7kyzXjoigPxJV3SoIxHA8zxdpbPHeSLGw87HKbbk0w_NYDX6jk6q7R4fR1vVZa3RYWxDi9eczWZ6PIDy3_ZwZ1OLRA0f76ELPIV9CkB0bOk7G4qAxI5CvleCQcDzKvTQ0NCXV23UOSDhGblymCezE7Ray9RdV_PI8AXxe9EQRUaFFu5RUS26QLQhdftLtta33xT3ZLGZ5BbhJObLvZA5btKT_-Ir4QwG_BESiYNcxMrjeoFpjeR6HScg_lo_hhR87rgIs0O76k4Y2LGNOeQx6I3N9x1522ijtmO7QrfPMzw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 10.1K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐تبلیغات دایرکت کانالwww.youtube.com/@ArchiveTell</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-28 21:48:15</div>
<hr>

<div class="tg-post" id="msg-7797">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🤖
JIJI AI
مدل‌های موجود:
⚡️
GPT-6-astra
⚡️
GPT-5.6-sol
🧠
Claude Fable 5
✨
gemini-3.8-flash
🚀
glm-5.3
🔥
deepseek-v4-pro
روش دریافت API :
1️⃣
وارد سایت بشید و با گوگل لاگین کنید
2️⃣
وارد بخش API بشید و کلید جدید بسازید
3️⃣
شناسه (ID) مدل‌ها داخل پنل سایت مشخص شده
Base URL :
برای GPT:
https://api-slb.jiji.cc/v1
برای سایر مدل‌ها:
https://www.jiji.cc
🔗
www.jiji.cc
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 242 · <a href="https://t.me/ArchiveTell/7797" target="_blank">📅 21:38 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7796">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hUhZXuu5sj74Tar1FT2ceq04H7UCnTM61KSN0T3F_AMFLTiATqjGX7eJJRYOAIQf8Yo44sQfZKTrqdUo_itXW7ZwfV6wZrVrxRXKO1duIICIrntYeu9yS0lfG_29gwi9g6BMcXCpNtHTcmRzl0DWBcCCOyuR6q8CJPiOLf1t4Xw4H2SDG8pgmJ5iN2ni3HxRMycaifcAV9ik94MZyO84Lxy9ByjXwGlgwk5Qxb4OgRTNG1enOT0Nbx7I0i4NMcOE4bMcyRSe8uY7Ix5uKQj1m-SgbADAN7LLJj439ooRaBfOMmyYvrEJB4WqLLQBp-bETegYfcU0fqMQ6Pd09C1-yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
مدل GPT-6 ASTRA به صورت رایگان در MiniApps در دسترس است!
قدرتمندترین مدل شرکت OpenAI، بدون هیچ هزینه‌ای.
آنچه دریافت خواهید کرد:
✦ مدل GPT-6 Astra به صورت رایگان
✦ قابلیت‌های استدلال، کدنویسی و انجام وظایف پیچیده
✦ اجرا در مرورگر، بدون نیاز به نصب
نحوه شروع:
1. این
لینک
را باز کنید.
2. ثبت‌نام کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 899 · <a href="https://t.me/ArchiveTell/7796" target="_blank">📅 17:58 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7795">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UsWMU-LRSitytYCDmeKbvGBsSJ1djTetMmamWZaGCftixASQOEkcnG03YZTppsIIg0Sb06uacbJYpkJsulWrSVxNLL8fvCzNe3NwSOZ4fLoNmPMztBZfQVTNbDtQwpHoLGhIQf5GBJqR1nk_9KHrVcNVFfNzfuee02zqpOPzZQW5KF_IfqKtLFDUZZxD8oavbO3V1zQDJ4LXYjqULecdaXDj1rcl4hF4qKUDc6fro9rKRRkovrRBEs7YXWYDYHHhcdER63vNXcV8sqNeDxjSOmHH022Eg7M1gHrCodjL29Rha_VYfa10y1xgaC-hbTg3ExQ2o_pTu4NK0B5ds7_VSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⌨️
مقایسه‌ی تصویری GPT-6 Astra Max در برابر Claude Fable 5.1 Max در تست کدنویسی Code Arena
به طور خلاصه: Astra در انجام وظایف تحلیلی، محصولی و محتوایی عملکرد بهتری دارد. Fable 5.1 در جنبه‌های بصری و تعاملی عملکرد خوبی دارد.
در حال حاضر، GPT-6 Astra Max در مجموع، رتبه اول را دارد. می‌توانید جدول رتبه‌بندی کامل را از طریق
این لینک
مشاهده کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/ArchiveTell/7795" target="_blank">📅 16:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7794">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_b00W4Ro7nIRbgld_cWkwA3qvZ8wL2yicP_X_wO4BS4VwWoU3fcCmWiW35hRlVuIhVEW_kAfNks7lujNBHEXAAcZ2Us37FnQJixFmiQN6wrxRBk-1qVBRa41UM_OEUiuhi2hnvGJt0MLyB88cySMKarGaQw6S-nPyqaECbz_hVV8w7Gq8kd7RrSNCS10vKzRPWIW7s3fFa_CkoxxRaW2_t2j9QPHPKbn7Xx0HTLlqIGOyXo9fEy5KMp_W5yZvbPdAWptG2SRQN0VdAHNxByuzfVjXhVBg9WajHbB3Ar5OScG-uhwGqcb4ml8bV0Uer_ZGmy-YLEvZsFeheD8ylQKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⌨️
؛Qwen3.8-Flash رایگان تا 30 سپتامبر با 0.0× اعتبار
مراحل:
یک حساب کاربری شخصی در
Qoder
ایجاد کنید یا وارد حساب خود شوید.
یک محصول واجد شرایط از Qoder را باز کنید و Qwen3.8-Flash را به عنوان مدل انتخاب کنید. برای اطلاع از قوانین این طرح، به
صفحه رسمی تبلیغاتی
مراجعه کنید.
از Qwen3.8-Flash استفاده کنید. نرخ 0.0× به طور خودکار در طول این طرح اعمال می‌شود، بنابراین استفاده از آن هیچ اعتباری مصرف نمی‌کند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/ArchiveTell/7794" target="_blank">📅 15:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7793">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mDkKq-DpFR1RmKMyFIdkT7J2kLTdO0XVeE5QtmQgY_mU4bqZ-jT6ItWRMrKr5zu5wNSi6diG2igew-ZKGgFokTujxEIKrg-pXgl4nmCVajSCB0krj0GX7fVvPfe_qjCxuLVmK0IeRt1cA95N5vBKpHPd5985DAN4MTVV6uo9zrI4nCyMho8fG_U9mkqmGuvc_tGo0FaiS2ZQ4Kv3xwYcmOU4DA6BDqxVuniy5lH9lsadz7sdWXiEsaTTgPDqv7ymi4631Di5QMD11tfsliFbuLLh0CcWc8iUgNTOZmG8vlf41oobdcsn_hcTp1FQ-uHkJ2BqMYf-sPOa2vH9shQtNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
چت + تولید تصاویر و ویدیو با Kleo
🔥
آموزش
مدل‌ها:
➡️
GPT-6-Astra
➡️
GPT-Image-2.5
➡️
Kling 3.0 Pro
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/ArchiveTell/7793" target="_blank">📅 15:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7792">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6341cb8e8e.mp4?token=hGkN8B8jLbfttiVsuhU-3qANi4ZyC47QOx4JqZcIt1BfVDUN-4EShd4cClYzGcDHY0DWIw1sG2TWGycT9hp2_s_n7V8e-0eYNO-K0kOq36kBN-eH5b5UBzt6z4liBp7idGreSVn4W-6zpepsEYFuTMmGESmYmWfu7kBPwYcI9ObO0HZia6iHL0soF0uRhGR5c1s0uFf2BtTtLmGEhW9vq5xUAIMeb7IY8UbWHcO3-OJhOygVGxCD1Bt-V4VE-fVmnhQiBsxNwDEf_xI-vYPnfyIPMYdZSUFjQtIW1JfGlZlYr_whYDicsOOZ5dospZNyGQcoriDiEMKW9xRZrMrPyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6341cb8e8e.mp4?token=hGkN8B8jLbfttiVsuhU-3qANi4ZyC47QOx4JqZcIt1BfVDUN-4EShd4cClYzGcDHY0DWIw1sG2TWGycT9hp2_s_n7V8e-0eYNO-K0kOq36kBN-eH5b5UBzt6z4liBp7idGreSVn4W-6zpepsEYFuTMmGESmYmWfu7kBPwYcI9ObO0HZia6iHL0soF0uRhGR5c1s0uFf2BtTtLmGEhW9vq5xUAIMeb7IY8UbWHcO3-OJhOygVGxCD1Bt-V4VE-fVmnhQiBsxNwDEf_xI-vYPnfyIPMYdZSUFjQtIW1JfGlZlYr_whYDicsOOZ5dospZNyGQcoriDiEMKW9xRZrMrPyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😎
مدل Kimi K3 به صورت رایگان در Cline Desktop در دسترس است!
🤔
شرکت Cline به تازگی مدل Kimi K3 را به خط تولید مدل‌های رایگان خود اضافه کرده است.
🤔
دسترسی رایگان برای مدت محدود.
🤔
از مدل Kimi K3 مستقیماً در داخل Cline Desktop استفاده کنید.
🤔
مناسب برای برنامه‌نویسی و گردش کار هوش مصنوعی.
✨
؛Cline Desktop همچنین از سایر مدل‌های رایگان نیز پشتیبانی می‌کند.
⌨️
برای شروع
اینجا
کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/ArchiveTell/7792" target="_blank">📅 13:32 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7789">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/Ci4AKIGMiwecVxq2tRurr1hjEZZAdgP2haBMuGx7cEJc47vE8PafErc7225S5Fw7WnO_bBIEbByBeox2giW-fd8RY3ng71tHD7v32Yk3XT6h5KIMfYy_ppqhqGHlXS7Wxlr-H3YBgR9I53V75TMFMYm9SWwFsa9Abpr8q78EbF3OsConSrlr0IREz1SV6I6g6RQtkEqNHhm5Cv1vEaPy30WazItQcPcoQMOnnzhMpjlfMU7SorpGiNFoZTdQqKxTxYtqRrg8U0zhLunvw5Zpk1LHJZjXj4Cv3iC-hRLC0hrzVbjznLpmfp80y8c3twB9cbBT88dwHhrstJK_a3tLUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PKrGIRtPqvtsmzyUenEYC9bk3YDW-jL5rQ_B1M-TlUA7fcAuo3N7F_Wyq5OK78fvLjBWK5U1Ob80tEWwkmQhXGIeXFhsVk0Wc9ChfOG70koZK-_JFJzA4Ln2FbWMaJRHSbkYLYTjniYodBzVpLAGUi0JiM2CLOo-WHj7d66NCtbRdDI3tHPyI-MgIx1Nss9mjkNvNd8XkBn5PC10qyEac_wxqnGxm_La82YEKwGA47q03AaXVF6_NwavPCvQSJnG-G-dW8IgBzV6_LZoxY5qbO1luFK--xTbi_6q8z7mkqf49RuI6KVjl7fiEI5x4UIdox67AN-jgYMuatOrwFSo9A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">seekAI
$2,000 credits
API key:
sk-Ok0xV7Zp4vfigk6qXL8M6hQSeVGa5cRhhfkZ06yre2RUIAfN
base url:
https://seekai.cc/v1
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/ArchiveTell/7789" target="_blank">📅 12:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7788">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jw8XCraATnCvLLgJcb32uFPke3CUx2OSPuG64u3gVlQlYkGlrDku9f1Mo_UpiaHE8TvLmgy2_K5HVNjQxr8XYR3rXfAugBqRR1n-rJnDsTtxriaWn4nhZ7TXDntgnGUcVOwxgJt9aM9__0tYSb656xtzhV-vEITsFXR3Vg6V1uNwZKSniH0V4_gYTffSLz4oFgtMPfBAHaN4FmJv5A7IGR7evhDGL0Tnz1jJQ2WTv9a5k3qGcdjVB2MxLyAH_PZ-Tgp2clRg4RbWSlifbyUxlEhy0PmsqiZetL8NxbGDXjyXi5ISZbn-V9mJv7abpu5MMElJNLuvbV-P2XQEk8kuTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
نسخه Claude Fable 5.1 به صورت رایگان در Freebuff CLI در حال حاضر در دسترس است.
👾
📢
؛Freebuff یک ابزار کدنویسی کاملاً رایگان است که در ترمینال شما اجرا می‌شود (مانند Claude Code / Cursor، اما با قیمت 0 دلار)
🆓
✍️
مدل‌های رایگان دیگر موجود:
🔍
🤔
GLM 5.3 Flash (پیش‌فرض، بدون محدودیت)
🤔
DeepSeek V4.1 Flash
🤔
MiMo 2.5
🤔
GPT-5.6 Luna
🤔
Solar Pro 4 (به مدت محدود)
🤔
Muse Spark 1.2
📌
نحوه شروع:
🤔
ترمینال خود را باز کنید.
🤔
؛Freebuff را نصب کنید:
npm i -g freebuff
🤔
به پوشه پروژه خود بروید:
cd your-project
🤔
دستور زیر را اجرا کنید:
freebuff
🤔
از لیست مدل‌ها، Claude Fable 5.1 را انتخاب کنید.
⚠️
نسخه آزمایشی محدود — فقط 500 جلسه در مجموع (1 جلسه برای هر کاربر)
🚀
از این فرصت استفاده کنید تا زمانی که باقی است!
⭐️
🔗
اطلاعات بیشتر
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/ArchiveTell/7788" target="_blank">📅 11:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7787">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">اگه موقع ورود به gemini یا سایر سایت های تحریم به ارور ۴۰۳ برخورد میکنید، میتونید از dns های زیر برای دور زدن تحریم استفاده کنید
👇
dns 1
111.88.96.50
dns2
111.88.96.51
dns1
45.155.204.190
dns2
37.230.192.51
dns1
83.220.169.155</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/ArchiveTell/7787" target="_blank">📅 11:06 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7786">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♊️
جمینای گوگل سه شرکت واقعی را هک کرد !!!
جمینای در جریان تست امنیتی ماه مه ۲۰۲۶ به‌ صورت ناخواسته به اینترنت دسترسی پیدا می‌کند و شرکت خیالی مورد نظر خود را با شرکت‌های واقعی هم‌ نام اشتباه گرفته و با استفاده از اطلاعات ورود لو‌ رفته در سراسر اینترنت وارد سیستم‌ آن‌ها شده و نفوذ می‌کند،  پس از پی بردن به واقعی بودن شرکت‌ها، خود به خود عملیات نفوذ را متوقف می‌کند.
گوگل اعلام کرده هیچ آسیبی به این شرکت‌ها وارد نشده است
✅
منبع
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/7786" target="_blank">📅 09:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7785">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">سلام بِرارون و خوارون عزیز
حال دلتون خووِه؟
🌟
فردا یه آموزش خفن داریم که حسابی به کارتون میاد!
🚀
مو فردا مِخام یَگ آموزش مَشتی راجب «تورنت» براتون بزارم که کِف کِنِن ینی قشنگ بِتُم مِگُم چطوری انواع و اقسام فایل‌هارِ، هم اوریجینال و هم مُفتِ مُجانی گیر بیارِن و حالِشِ ببرِن.
😎
🔥
بِراگَم، گیانِ دل! از بهترین کیفیت فیلم‌های خارجی بگیر تا همون فیلمای پرده‌ای که تازه لو رفته... اصلاً هرچی برنامه کرکی، موزیک، فیلم و کتاب نیاز داری رو یادت میدم چطوری سه‌سوته رو هوا بزنی!
🎬
🎵
📚
پس فردا حواستون به کانال باشه یاشاسین بچه‌های گل خودمون قشنگ هر فایلی که ایستیسَن رو بدون یه قرون پول دادن یادتون میدم دانلود کنین. منتظر باشین که قراره بدجوری بترکونیم، ساغ‌اولون!
💣</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/7785" target="_blank">📅 23:18 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7784">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚀
Ashna AI
قابلیت چت مستقیم و یا کلید API
🤖
مدل‌های موجود:
⚡️
gpt-6-astra
🧠
fable-5.1
✨
مدل‌های متنوع دیگه
روش فعال‌سازی:
1️⃣
وارد سایت بشید و ثبت‌نام کنید
2️⃣
اطلاعات حساب رو تکمیل کنید
3️⃣
از بخش Integrate وارد API Keys بشید
4️⃣
روی Create key بزنید
5️⃣
گزینه Dynamic model routing رو روی Off قرار بدید
( نیاز به تایید شماره نیست ولی اگر خواست از این
سایت
دریافت کنید )
base url :
https://api.ashna.ai/v1/api
🔗
app.ashna.ai
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/7784" target="_blank">📅 23:18 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7782">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qTgUh3qdteVsPAdnepkH4Tl6kdV3YcT1Ss6wpcPk2Dkk6NlxN43_wQJQdsYhYQ7PQ9HhwBYi_2CTQaWHXdVD9dSPU2JcbTBn7Aq1GiDwdDnbpcZTmWRRrZ3ObtiRIotMpQMgaMLFH9UmzLBXcnh_3TRTUorEyYiyQROLuSTvEfmCSunhDhW8-5H7s5ZQF2Ke9TWdvtKOQak-D2f7t-cWaGvI3e4nyZztWDTKskF2j9ffbx8d3nAIhOjWFZ53N_ybAc5hyFvi7vrvOiyh23y0CGOisf0rXR-8JdX1Z1JaiIZhXAoKSdVBCVH2gSEl56l-In-ZpajdbC8ni4L8MXz9rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Gemini 4 pro is out now
💪
😎
گوگل بالاخره پر قدرت به بازی برگشت
تست کنین نظرتونو تو کامنتا بگین
(این پست طنز میباشد)
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7782" target="_blank">📅 20:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7781">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RJp4dbpnQdW-v7zWAgAhUeoaXEvHcb0rpjuU_SAOlLycPXo6GnIdbGN2r0GIZdVE3Wdt6Wm2-5IfbDmt9eWh5VljuXo-eBuT2aoK6CP27KfEMLfBDb_Zsiog_wPtLzT9ECXgdlK7GahU1tDaZiUF-0lDCQ_R24Va7Vn_36nA2aiRMekqq9wP3jE5sEO6oUfS_nccEmo0VNW3zaFI_kPs1IyiBuxqnwM4tLX-kLDCECj-bXlxfOdi9wtrJzmnh1KIiP-RlC3YnaI0tvhUhZxAebnYiS8cBgjrGOW27XxCPJz6xH-4_2VpW7EBLqFRXQ__nGERxZPFvkvalqcd-8s_xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تبدیل ایجنت‌های هوش مصنوعی به کارشناس امنیت با ابزار Cloudflare!
بچه‌ها کلودفلر یه اسکیل امنیتی خفن
منتشر کرده که در واقع بیس اصلی سیستم کشف باگ و آسیب‌پذیری خودشونه و هوش مصنوعی رو به یه هکر کلاه‌سفید تبدیل می‌کنه.
✨
ویژگی‌های کلیدی:
🔺
ا
دیت ۶ مرحله‌ای:
ایجنت رو گام‌به‌گام از اسکن و تحلیل کد تا شناسایی عمیق آسیب‌پذیری‌ها جلو می‌بره.
🔺
گزارش‌دهی کامل:
در نهایت یه گزارش تحلیلی، تمیز و ساختاریافته از تمام باگ‌ها تحویلتون میده.
🔺
راه‌اندازی ساده:
کل ساختار در قالب یه پوشه از پرامپت‌ها و دستورالعمل‌هاست که راحت روی ایجنتتون سوار میشه.
💡
نکته/استفاده:
خوراک دولوپرها و تیم‌های DevSecOps که می‌خوان قبل از ریلیز، کدها رو با ایجنت‌های متنی ممیزی امنیتی کنن.
🔗
سورس پروژه در گیت‌هاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/ArchiveTell/7781" target="_blank">📅 20:04 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7780">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">💎
دسترسی به مقالات و کتاب های
پولی خارجی به صورت کاملا غیر قانونی
https://libgen.im/
https://z-lib.id/
https://annas-archive.org/
https://sci-hub.se/
https://libgen.is/
دوتا اولی فوق العادن
😱
، علاوه بر مقاله، کتاب های پولی رو همشو داره. هر کتابی بخاین.
کاملا غیر قانونی
😂
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/7780" target="_blank">📅 18:15 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7779">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ارسالی
http://64.23.188.133/v1
gpt-6-astra          ←
⭐️
تأیید هویت شده
gpt-5.6-sol
gpt-5.6-terra        ← سریع (۵.۳s) و باکیفیت
gpt-5.6-luna
gpt-5.5
codex-auto-review
gpt-image-1.5
gpt-image-2
API key خالی
سریع بزنین تا تموم نشده
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/7779" target="_blank">📅 17:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7778">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bU13AHHPsyahXHfaXCDskp95G0sn0vfS8B18Yi1FDyqXNKljnmokM0UoBdhaDyP9UnRYHSTDwwTvcUgI56LQ_b_s2H4-gBAUt9Eya8-Tm1Ntw2BH6njY-c3lWdgW3m_aPHcOoJteIhYvnHBN52OlC0BS8LQGAdRjtjmLaMISyIOeCC1A5P1UQDpx2HZQPW2j4Jm98xJcs9YtoohHiC2aiPH7kxrZjoT6h-BFROnhe43oT71hSfIwYNQ_o0EtHlbR-hg-HJXQK0K6WaSOdvP0i9hfUijI1P21hu17gVnU28JMNeq7NNtgyN8lz7M4jUEl-Rz0u0gRNc6YvVrgP1wRUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
جنریت رایگان تصویر با مدل جدید GPT 2.5 SUNBURST!
بچه‌ها پلتفرم Weavy داره کردیت روزانه میده و می‌تونید جدیدترین مدل‌های تصویرساز مثل GPT 2.5 و حتی ابزارهای تاپی مثل Topaz و Magnific رو رایگان تست کنید.
✨
ویژگی‌های کلیدی:
🔺
کردیت رایگان روزانه:
فقط با اولین لاگین ۱۵۰ کردیت هدیه میده.
🔺
مصرف اقتصادی:
هر جنریت با GPT 2 فقط ۱ کردیت و با کیفیت بالای GPT 2.5 فقط ۳ کردیت کم می‌کنه.
🔺
محیط نود‌بیس:
دستتون برای تنظیمات دقیق پرامپت، رفرنس و تغییر کیفیت کاملاً بازه.
🔺
ابزارهای پیشرفته:
به ابزارهای محبوبی مثل Magnific و Topaz هم داخل محیط کار دسترسی دارید.
💡
نکته:
وارد سایت بشید، یک نود از مسیر image models -> edit image -> gpt 2.5 اضافه کنید، پرامپت یا عکس رفرنس رو بهش وصل کنید و ران بگیرید!
🔗
لینک ورود به پلتفرم
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/ArchiveTell/7778" target="_blank">📅 17:22 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7777">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ShbkRQ9D7yog6I6kxDM_qg6pE2Ubu1Ow5bTTnnBcFyO9FcTpf1lAdoVJuOYHVAtnRwsEFIPlz9xXjN0lItw80P1ASx8JJTjU9wNsjBFTdl2uEtzLk0lQNpp5-RTihZ3CVWq3wflNHREKbwi0oIGEXevg0wfQi2VlaLgU6vkkHziahWO3SE45ib3K-NnB84t-OtfwXLZ2wraE8oQwmoQ77_9KulDQZlvaoZl4QwZLqY8_1r4iZ7gi6OW5CZjfaW7qEPg3pMq22j5daRGj7T7Hbq4s8f2Ts0n57t43QYbTvW-00IUwLO_hYwzNELsMR64O5vVflEk4RI-XeVCExgGd4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
یک میلیون توکن رایگان GLM 5.3 Flash
برای دریافت
اینجا
کلیک کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/ArchiveTell/7777" target="_blank">📅 17:06 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7776">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/rdkEvv7Iesvp5s2ldq-IEa7kjk5UKOorkw7OfCwnBsiz5nclE4SaK0pjzsdSDQKcMsHz_7mCvfliIAG41K0ri-2VteO5HlOg0LBKaYV4u54QfD3kaQLtlLMP7LmOW05368WeV42HXD9JVk9kJLUPds0BW8x6m3zRm8RONCFD_yL9_RnE6WAQE6c4tc4huxRibfVeKDsIT_uYguMjilW94XW49arMv-B9qWUSis6BiXkXLVapjr9X9x0OAa8I7JwtIUIvr_gevwzVv9ZhIxkXQxDtD--Czun-Mxnl2h2qPDWUUdQPBaQWsu2_F2hdoYtZSdlmuGWo0k3vYR2bjlsMXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
6 مدل هوش مصنوعی رایگان که همین حالا در Cavoti در دسترس هستند
👾
📣
دسترسی رایگان محدود (تا 25 سپتامبر)
🤔
Hy3
🤔
MiMo-V2.5
🤔
DeepSeek-V4-Flash-0731
🤔
Qwen3.8-Flash
🤔
GLM-5.3-Flash
🤔
MiniMax-M3
✍️
آنچه دریافت خواهید کرد:
🔍
🤔
استفاده کاملاً رایگان
🤔
؛API سازگار با OpenAI
🤔
مدل‌های قوی برای کدنویسی و کاربردهای عمومی
🤔
نیازی به کارت اعتباری نیست
📌
نحوه استفاده از این پیشنهاد:
🤔
به این
لینک
مراجعه کنید.
🤔
ثبت نام/ورود به حساب کاربری خود را انجام دهید
🤔
کلید API خود را ایجاد کنید
🔑
🤔
هر یک از مدل‌های رایگان فوق را انتخاب کنید
🚀
⚠️
دوره رایگان در تاریخ 25 سپتامبر به پایان می‌رسد.
⌛
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/ArchiveTell/7776" target="_blank">📅 16:05 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7775">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZkN2VDZqusf-tmpkM-1H8xBIt6s6ztsHqL-Nna4g9t632XIfT64KWbzFmJcyk5Tv6TITqCS-y8QWO6o2tGVad22ndza8a39ARRIq7kMOAQfZU9C3C4e3bvH5noTrdA8Gyr-bTx4HYHA6xLSPD_v0aMTjWrSrYcGe36fSMnadyr73J9-5uUZI1EROK_tTD9zsSDZ-hKLFZyF25frYGA3VYwYDYB_zdOcpgomJdfq8ab-f0C7zk2yBTQ8w-QW1GrfalWY8hbmlONhSvx2y8Qcfl_HthAsqqmLtsUJuaWGGPPqarIV8IBnKSplTuBhYqP3HDO77D1-JVC4SSjEQ1sxnKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
تبدیل خودکار هر مقاله به ویدیوی کامل یوتیوب!
بچه‌ها این اسکیل جدید کلود رسماً برگ‌ریزونه؛ با
Anything2Explainer
کافیه یک متن، مقاله یا موضوع بهش بدید تا تحویلتون یک فایل آماده MP4 با موشن و صدا بده.
✨
ویژگی‌های کلیدی:
🔺
فول اتوماتیک:
سناریو می‌نویسه، استوری‌بورد می‌کشه، انیمیشن می‌سازه و زیرنویس اضافه می‌کنه.
🔺
صداگذاری اختصاصی:
روی ویدیو با هوش مصنوعی نریشن و وویس باکیفیت میندازه.
🔺
کاملاً رایگان و متن‌باز:
با یک خط کامند راه می‌افته و خروجی تمیز بدون واترمارک میده.
💡
نکته/استفاده:
آماده‌سازی کل ویدیو با تمام جزییات حدود ۱ ساعت زمان می‌بره و همه پروسه صفر تا صد توسط AI هندل میشه.
🔗
سورس پروژه در گیت‌هاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/ArchiveTell/7775" target="_blank">📅 13:02 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7774">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6370f25b3.mp4?token=FE0_5bkqbh8YrOZDYZwED8Ql0crprDrHD7yZH-uZtBmdOXnOocfjM43shGdIzgzaQE0FOkXrkk0jY4D4Hzd19TNnJFnupUfrfS6Q_fBskim4jw9QsxTBXMZTY-b68t44YYqxJ-C9MJjvpQtnzmWShsz5lybFNZfaXkpImw-blrjK9KGeObopOipueBcVI_yW2KDjDm9an6ipInuldlTOja-0hQ_jzEW7cZbLpMFhOHNC0Pj1DOWRfR_-VoHykGm_xPr5ySdjr-n_-R4ET_KJmRRb01OmAo4TAtuhJkB25suk6RDxZxDL3gVoyTz7oKgAC0SL8rKo7Fsw2MYMgT6KHnDNSLGClMbYGRmNIKFePXOCZjiNMSLcPlGoxHFyiw1MEHx-GChvUnmgPNRVcjSJmA41WsoL3h73IdCFA2iAZfVCA8mr8O-ZHOWYS9L2Hc_dnN-idUsvjj4Z08UquvmBiOe8tYRgdRkQ85Tv_fQJsrK-q5CR7SLs_zNmKOSzKslA722iWORXiP_KOBTaGv7oswXzk4UbcE1PSQRM3W5nSQJcaPTzcbP6GeH9-Wpybx3Lw5jslW-frHM8biFz_zKJL3SyIQuF2FeWFzqqi0vp2t6JOAj7m2YcF4KYDDcAIopP0SbC_9nUL4T-6MvflRMVQJE0BiaQkhEa42HyDhdjj2U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6370f25b3.mp4?token=FE0_5bkqbh8YrOZDYZwED8Ql0crprDrHD7yZH-uZtBmdOXnOocfjM43shGdIzgzaQE0FOkXrkk0jY4D4Hzd19TNnJFnupUfrfS6Q_fBskim4jw9QsxTBXMZTY-b68t44YYqxJ-C9MJjvpQtnzmWShsz5lybFNZfaXkpImw-blrjK9KGeObopOipueBcVI_yW2KDjDm9an6ipInuldlTOja-0hQ_jzEW7cZbLpMFhOHNC0Pj1DOWRfR_-VoHykGm_xPr5ySdjr-n_-R4ET_KJmRRb01OmAo4TAtuhJkB25suk6RDxZxDL3gVoyTz7oKgAC0SL8rKo7Fsw2MYMgT6KHnDNSLGClMbYGRmNIKFePXOCZjiNMSLcPlGoxHFyiw1MEHx-GChvUnmgPNRVcjSJmA41WsoL3h73IdCFA2iAZfVCA8mr8O-ZHOWYS9L2Hc_dnN-idUsvjj4Z08UquvmBiOe8tYRgdRkQ85Tv_fQJsrK-q5CR7SLs_zNmKOSzKslA722iWORXiP_KOBTaGv7oswXzk4UbcE1PSQRM3W5nSQJcaPTzcbP6GeH9-Wpybx3Lw5jslW-frHM8biFz_zKJL3SyIQuF2FeWFzqqi0vp2t6JOAj7m2YcF4KYDDcAIopP0SbC_9nUL4T-6MvflRMVQJE0BiaQkhEa42HyDhdjj2U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔍
با این مدل، هر عکسی رو با یک کلیک تا 4K آپ‌اسکیل کن!
بچه‌ها اگه عکس تار یا بی‌کیفیت دارین که می‌خواین زنده‌ش کنین، مدل خفن
Crystal Upscaler
دقیقاً همون چیزیه که دنبالش بودین.
✨
ویژگی‌های کلیدی:
🔺
خداحافظی با ماتی:
عکس رو مات و غیرطبیعی نمی‌کنه و جزئیات واقعی رو حفظ می‌کنه.
🔺
کیفیت تا 4K:
رزولوشن رو تا بالاترین حد ممکن بالا می‌کشه.
🔺
عملکرد جادویی:
خروجیش رسماً شبیه زوم‌های فوق‌العاده توی فیلم‌های علمی‌تخیلیه!
💡
نکته/استفاده:
نیازی به سیستم قوی نداری؛ می‌تونی مستقیماً روی بستر وب و از طریق FalAI آنلاین تستش کنی.
🔗
لینک تست و استفاده
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/ArchiveTell/7774" target="_blank">📅 11:22 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7769">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p9Pxj87PWM85UXh9iQHd9RBaZzB6h29M-orX2oJ6pR29rgjQSJliJpOOclFcGtdsEuq3nJ2ihOgiz4EkC9DjWjxKub4z6Pza-rbVRZ8692jOc0ofQd8-pTnMOBLzUaZjFG0jaalxNmHFPgl0hde2pVzxyecK7oo92IVAiv05-0cnQa6Dtu9UbYrWEc96B1M1Te6IfuiPhpu_XlFAHa79IRZmcQiMv1Qlk-XMlf_eqE0C9qTX4N5ZgHqxHvR251eNEL4yf9GqiyV3x57qHtaGdPY-0M9QasNi7Ivjg5cC8nQ45D33-CU_S-YhlHWtM6Y4WRGcYpVH3p8a70WG8Hbf1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pD3_hUK5yf0OoP2hu6-nABQkQ01ksLGRZ-PtSUUL5lZ3HcGiIXnWC37r_iX8Z-lMIc7ekoSigFqd9BwULPhGT5ZKrrA4RgrlfHlaKrCBGYN7Ol3gkGPqHyATti6ZmhXtIjJh-hDYUPLlngYZWLzgtAqngjCh7Ik3UW056zsExBTWgIDGKdf7TsKbsNPPtixCfmps6acjZU6YFwRLP07WTWNbSuGnd0vjc7pO6XpZNHa6yZAgb_QTR1ApUQS_plaa0wroWiWZByLHVRoKNvh7YdrVGHE8-7hIsWDIAZRfNmol-NrsAABV7uYUUje4juxYD7yRYB97cRde9_U22nUj4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tm323CwtkQVulB0c1ngowj2TGgNvR0kTlD2GzGBFGaYsZ1cZGAv74OniwLrqqo2suLmM-uzK-l091q08MIlFZ60iONSrmm4bWzRQIph5xc322z67EkDOKI-5229iXNJ2xoOqc43RDxysgklpBdhJJITwVREnk816bMi0rJJXg8sRm7K0g9rD1w-TMRDeFr4cxhOn1y2bhFkrrZ8-aCoAPjZsDin98j11_O-XCWJuvw14EfyQVsdKVO-Vh1d-hJeBvZVs2veX8qt1KTsbTRvP2mFw_YHuGCdhdukDnDECfEGnFSRjACG1HjN6rmLm3UFT5rkrN_9DKT80lMZ7hGKwLQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3248c435c.mp4?token=JDSZtDJw1PI1qPboA-862arYogowFYnCtmBCjQ7DjsRQmeL2wxAdy-63ozW-jylSvKPk4poXPg8nDZ22fZGBKelgDmGD7UWsTtaHM89WwN2OlG2OIZqWnxfI4F53JBO5jEtIScEkZ9zZGUdlesHUxfyKkvdD7qVPxYze3Loo3U5bTIfxc6Jp3JthV_whrKTCUTTUtbDuxtGH3EZYbvGcwGbVDF-eX4F2LBGrAwOI0qLXBixt0S_cyHru3D_z8gUEFncd5lfxEKKFTc7EHKfDzqDBY6nBiaZBOjDm3F9xtXv_1IPXXonFUlGiZY8pphauKbfWPvMssbgwiAGZicp4vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3248c435c.mp4?token=JDSZtDJw1PI1qPboA-862arYogowFYnCtmBCjQ7DjsRQmeL2wxAdy-63ozW-jylSvKPk4poXPg8nDZ22fZGBKelgDmGD7UWsTtaHM89WwN2OlG2OIZqWnxfI4F53JBO5jEtIScEkZ9zZGUdlesHUxfyKkvdD7qVPxYze3Loo3U5bTIfxc6Jp3JthV_whrKTCUTTUtbDuxtGH3EZYbvGcwGbVDF-eX4F2LBGrAwOI0qLXBixt0S_cyHru3D_z8gUEFncd5lfxEKKFTc7EHKfDzqDBY6nBiaZBOjDm3F9xtXv_1IPXXonFUlGiZY8pphauKbfWPvMssbgwiAGZicp4vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
Arrow 2؛ قدرتمندترین مولد تصاویر وکتور!
🎨
‏مدل
Arrow 2
اومده که کار طراحان و تصویرسازها رو خیلی راحت می‌کنه و ساخت وکتور رو به شدت سرعت میده.
‏
🤔
کاربرد متنوع:
ساخت انواع آیکون، لوگو و اتودهای گرافیکی با دقت بالا
🎯
‏
🤔
خروجی حرفه‌ای:
تبدیل پرامپت‌ها به طرح‌های برداری تمیز و قابل ویرایش
📐
‏
🤔
تست رایگان:
دسترسی به دو هفته
trial
برای شروع کار با ابزار
⏳
‏این ابزار خوراک بچه‌های طراح و گیک‌های گرافیکه
🔗
لینک دسترسی
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7769" target="_blank">📅 20:29 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7768">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">یه مدل جدید و قوی برای کدنویسی اومد و فعلاً رایگانه
🔥
‏Union Alpha امروز روی OpenRouter و OpenCode در دسترس قرار گرفت
✨
‏چیزایی که داره:  ‏
✅
Context ۲۶۲ هزار توکنی (تقریباً کل یه پروژه‌ی بزرگ رو یکجا می‌تونی بدی)  ‏
✅
پشتیبانی از تصویر (اسکرین‌شات و دیاگرام…</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/7768" target="_blank">📅 20:16 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7767">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T0vc_n6clxKaO61S-gctefk8eB0zcD5lyhppsSZCu_L7YP9ST8bhez5YmjG65VtZoQU_nXoZsHRqyulwbkx1St30upOXCj13TSvwMX07wfGfmzd8OEiIBWQE_Rq9TcSzrt3hobA7hm1HMFzqICfL6EJJPPZMBzjLYxY2rD0FrgbqnPZ9i1swpvgL9sDPuizGMuOnEPVgsEHDlAK4LXsmrjz_n-FjuRFWeS4BPnBDf8HRVN9lJh6Ne5Tev2Wx5HJy-14H9F40xhrp1LxWG4sHdXxknVYD9Xq395uN_h_2cFHdia5Pl3F8k2y1bSBLGdXAVdr2wMHUsFaPni2KayYyLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه مدل جدید و قوی برای کدنویسی اومد و فعلاً رایگانه
🔥
‏
Union Alpha
امروز روی
OpenRouter
و
OpenCode
در دسترس قرار گرفت
✨
‏
چیزایی که داره:
‏
✅
Context ۲۶۲ هزار توکنی (تقریباً کل یه پروژه‌ی بزرگ رو یکجا می‌تونی بدی)
‏
✅
پشتیبانی از تصویر (اسکرین‌شات و دیاگرام هم می‌فهمه)
‏
✅
Tool calling و structured output
‏
✅
بهینه‌شده برای کارهای agentic و کدنویسی خودکار
‏
✅
داده‌هات برای آموزش مدل استفاده نمی‌شه
‏فعلاً کاملاً رایگانه
🆓
‏
🔗
لینک مستقیم:
‏
https://openrouter.ai/stealth/union-alpha
نظراتتون رو بگید
👇
🔹
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7767" target="_blank">📅 21:47 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7766">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">😎
یک میلیارد توکن Muse 1.3 به صورت رایگان
به کاربران جدید، تا یک میلیارد توکن در Muse 1.3 ارائه می‌شود.
(این توکن‌ها از طریق API ارائه نمی‌شوند، بلکه از طریق وب‌سایت توزیع می‌شوند.)
اینجا
ثبت‌نام کنید (از VPN آمریکا استفاده کنید)
بعد از ثبت‌نام، در تنظیمات، کد تخفیف زیر را وارد کنید:
LYA0IL
+ در opencode، این مدل به صورت رایگان ارائه می‌شود.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/ArchiveTell/7766" target="_blank">📅 20:23 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7765">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚀
بدون یک خط کدنویسی، برنامه‌نویس شو
😱
(جادوی Vibe Coding)
دیگه لازم نیست ماه‌ها وقت بذارید کدنویسی یاد بگیرید.
الان فقط کافیه با زبون آدمیزاد (فارسی یا انگلیسی) به هوش مصنوعی دستور بدید تا براتون برنامه بسازه! به این کار میگن
Vibe Coding
(برنامه‌نویسایی که میگن الکیه کیفیت خوبی نمیده، حتی اونام از این استفاده میکنن
😂
)
برای اینکه مثل یک حرفه‌ای خفن‌ترین پروژه‌ها رو بالا بیارید، این ۴ قدم رو پیش برید (پست رو سیو کنید که به کارتون میاد):
۱. اول نقشه بکش (Deep Research)
همون اول نگید "فلان اپلیکیشن رو بساز". اول بهش بگید:
💬
"ایده‌م فلان چیزه. بهترین روش پیاده‌سازیش چیه؟ چالش‌هاش چیه؟ برام یه دیپ‌ریسرچ (Deep Research) انجام بده."
۲. گیرِ تله‌ی پایتون نیفت!
🪤
هوش مصنوعی عاشق پایتونه، ولی همیشه بهترین و بهینه‌ترین گزینه نیست! بهش بگید:
💬
"سبک‌ترین و بهترین زبان برای این پروژه چیه که اجرای اون دردسر نداشته باشه؟"
(مثلاً خیلی وقتا یه فایل HTML ساده که تو مرورگر باز میشه، کارتون رو راه میندازه).
۳. لقمه‌لقمه پیش برو (توسعه ماژولار)
🧩
بهش نگید "یه فروشگاه برام بساز" چون قاطی می‌کنه! تیکه‌تیکه پیش برید:
۱.
"اول ظاهر صفحه رو بساز."
۲.
"حالا کاری کن دکمه‌ها کار کنن."
۳.
"حالا اطلاعات رو ذخیره کن."
۴. ارور دادی؟ فدای سرت!
🐛
کد رو زدی و ارور داد؟ اصلا نترس! تو وایب کدینگ، ارورها بهترین دوست شما هستن. متن ارور رو کپی کن و بهش بگو:
💬
"این ارور رو داد، مشکل کجاست؟"
خودش باگ رو پیدا و حل می‌کنه.
🔥
با چی این کارا رو بکنیم؟
با همین مدل های زبانی هم میشه انجام داد ولی ایجنت های حرفه ای مثل Claude code و Google Antigravity هم میشه استفاده کرد.
👇
تا حالا با هوش مصنوعی چیزی ساختی؟ تو کامنت‌ها
معرفی کن رایگان تو چنل بزاریم
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/7765" target="_blank">📅 18:02 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7764">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">پروژه bkup یک پروژه اوپن‌سورس برای اینه که فرایند بکاپ‌گیری و بازیابی پنل‌ها، ساده، متمرکز و قابل مدیریت باشه.
🎉
نسخه 1.2.0 منتشر شد.
⚙️
تغییرات این نسخه:
اضافه شدن
Restore
برای بازیابی مستقیم بکاپ روی سرور از طریق
SSH
پشتیبانی از
3x-ui، HM Panel، PasarGuard, Rebecca
برای Restore
پشتیبانی از بکاپ‌های حجیم و چندبخشی
➕
امکانات کلی bkup:
بکاپ‌گیری زمان‌بندی‌شده، ارسال مستقیم بکاپ‌ها به
Telegram
، پشتیبانی از بکاپ‌های حجیم و چندبخشی، مدیریت بکاپ‌ها، تاریخچه و لاگ‌ها،
Reassemble
فایل‌های چندبخشی و
Restore مستقیم بکاپ روی سرور از طریق SSH
.
همچنین امکان نصب خودکار پنل در زمان Restore، خروجی گرفتن از تنظیمات و انتقال آن‌ها به سرور دیگر و اجرای پنل به‌صورت
PWA
هم اضافه شد.
⭐️
اگر bkup براتون مفید بوده حتی یک STAR
روی GitHub می‌تونه بزرگ‌ترین حمایت برای ادامه  توسعه پروژه باشه.
🔗
github.com/AliRezaC-xrol/bkup
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/7764" target="_blank">📅 16:06 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7763">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ipzS74KUMbziSpXj4Mmxqcad6coyudquyAPXc63UzUacmxgtYoJEmol8C8dcI15OvuE_wmWKddn_aVL3116U4IVMPW_7Ojlh1Zt_IHn-nfTQng3PKIE9ag_nK_FKf-YmdYXLUdLUqswmqCanEJ323_ImhM9NOxh_UlTRIpRlIt9LaNBTaDGBtLklVmFFTFC3ojnHMiM3YhDvSNdBL-V_dJVC_76vNLZ7Ab6rMhTivUvryhiAn7h6iY2ZOFeJXwyu9Xrth6_T-mFthw5FW1Z7joh9O0W2b3hL4qslszCf082th3X1jDdaHBhMrF5wiLeVIwawrTSTBD4qC7atebtCdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
مدل جدید دیگری از شرکت‌های چینی با نام ATRIA عرضه شده است. آن‌ها 100 میلیون توکن را به صورت رایگان برای هر حساب کاربری ارائه می‌دهند.
اینجا
می‌توانید با استفاده از حساب کاربری Gmail خود ثبت‌نام کنید، یک کلید API ایجاد کنید و از آن در صورت نیاز استفاده کنید.
نتایج تست‌های عملکرد در تصویر نشان داده شده است.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/7763" target="_blank">📅 14:47 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7762">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">⌨️
آدرس‌های ایمیل رایگان برای استفاده‌های مختلف در سال 2026: یک فهرست کامل - بیش از 60 سرویس
▫️
تکنیک "نقطه" در Gmail - اساس همه چیز
username+anything@gmail.com
→ همه ایمیل‌ها در یک صندوق اصلی. استفاده از IMAP از طریق App Password. هزاران نام کاربری فرعی. محدودیت: سیستم ضد تقلب گوگل - حداکثر 20-30 ثبت نام در ساعت، تغییر IP. سرویس‌های Oracle/Webshare، نام‌های کاربری فرعی را در مرحله اعتبارسنجی مسدود می‌کنند.
؛ SmailPro - آدرس‌های
واقعی
جیمیل ایجاد می‌کند، با بیش از 5000 آدرس در دسترس. تحویل در کمتر از 10 ثانیه. از تست‌های تشخیص ایمیل‌های یک‌بارمصرف عبور می‌کند، زیرا یک جیمیل واقعی است.
▫️
تقریباً همه جا کار می‌کند
؛ SimpleLogin —
نام‌های کاربری فرعی نامحدود
(در اکوسیستم Proton)، فوروارد و پاسخ با استفاده از نام کاربری فرعی. متن باز. نسخه رایگان: 10 نام کاربری فرعی
؛
addy.io
— قبلاً AnonAddy،
رایگان‌ترین سرویس
: نام‌های کاربری فرعی استاندارد نامحدود، متن باز، امکان میزبانی شخصی
؛ Cloudflare Email Routing
*
@your
domain.com
→ فوروارد به هر جایی. رایگان، بدون نیاز به سرور. ایده‌آل با دامنه .pp.ua
؛ ImprovMX — فوروارد رایگان برای دامنه شما، 25 نام کاربری فرعی
؛
33mail.com
— نام‌های کاربری فرعی + پاسخ‌های ناشناس
؛
spamgourmet.com
— نام‌های کاربری فرعی خود تخریبی
؛
erine.email
— فورواردینگ خصوصی
▫️
ارائه‌دهندگان ایمیل IMAP (غیر موقت، در همه جا کار می‌کنند)
-
mail.ru
-
rambler.ru
-
yandex.ru
-
aol.com
-
gmx.com
▫️
ایمیل‌های موقت با API (قابل اسکریپت‌نویسی)
-
mail.tm
-
1secmail.com
-
guerrillamail.com
-
temp-mail.org
-
mail7.io
-
anonaddy.com
▫️
ایمیل‌های موقت بدون API (وب)
yopmail.com
·
temp-mail.io
·
dropmail.me
·
emailfake.com
·
emailnator.com
·
mohmal.com
·
tempail.com
·
getnada.com
·
inboxkitten.com
·
mailinator.com
·
burnermail.io
·
fakemail.net
·
tempmail.plus
·
mail.td
·
mailpoof.com
·
trash-mail.com
·
temp-mails.com
·
emaildrop.io
·
temporarymail.com
·
generator.email
·
mailsac.com
·
tempr.email
·
atomicmail.io
·
emailondeck.com
·
crazymailing.com
·
tempmail100.com
·
tempmail.ninja
·
boomlify.com
·
tempmail.dev
·
internxt.com
·
adguard.com/temp-mail
·
webmail.raoshahzaib.site
▫️
بات‌های تلگرام برای ایمیل‌های موقت
@e2tgPM_bot
·
@mailtemprobot
·
@hidemail_bot
·
@TapMailBBot
·
@botmail_io_bot
·
@temp_mail_bot
·
@fakemailbot
·
@etlgr_bot
·
@DropmailBot
·
@tmpmailbot
·
@TempMail_org_bot
·
@TempMailer_bot
·
@smtpbot
·
@SenthyBot
·
@TempMailBot
@telegaemail_bot
·
@hs_temp_mail_bot
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/ArchiveTell/7762" target="_blank">📅 14:42 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7761">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">😎
دسترسی رایگان به FABLE 5، OPUS 5 و GPT-6 ASTRA
مبلغی معادل 1 دلار به عنوان سرمایه اولیه ارائه می‌دهد، اما با توجه به ضرایب، این مبلغ به موارد زیر تبدیل می‌شود:
🤔
Fable 5 → تقریباً 7 دلار
🤔
GPT-6 Astra → تقریباً 18 دلار
🤔
Opus 5 → تقریباً 20 دلار
استفاده از چند حساب کاربری (Multi-accounting) امکان‌پذیر است.
————————————
📝
نحوه کار:
1. به
وب‌سایت
مراجعه کنید و از طریق حساب Google خود وارد شوید.
2. یک کلید API ایجاد کنید.
3. آدرس پایه (Base URL):
https://www.rsiai.net/v1
4. برای مشاهده مدل‌ها، به وب‌سایت مراجعه کنید.
————————————
💻
نحوه اتصال:
Claude Desktop (Code):
- Help → Troubleshooting → Enable Developer Mode
- Developer → Configure third-party interface
- مقادیر زیر را وارد کنید: baseURL، api-key، model-id
————————————
♾️
دسترسی نامحدود:
1. یک پروفایل جدید در یک مرورگر ضد تشخیص (anti-detect browser) ایجاد کنید و موقعیت مکانی خود را تغییر دهید.
2. یک حساب کاربری جدید ایجاد و کلید را دریافت کنید.
3. کلید API را در کلاینت خود جایگزین کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/7761" target="_blank">📅 14:13 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7759">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/qoaXL46fqpnMTq1M7hqmaQBSWCdjaFGxXFMDfUjIvjlzTjg9iZrgT0g9DoJgAvF7pegSoFaN_4S2jMuuZGo93eHIB-TOLTlTJGaY7V_Fp-YEfJtkC0cQttHpYQHV8kl2JIK-N7bN4fLOOCzF6weZQs8ve43EWu-_L6dbVdF07KivWrZ6DmOnqxlbBhXRAG6vEiNJQFQK_gJlnfNqa7meunNp-ioXe5dKGNcBhObVAaBr1TP2BqfMSdHC0Jkk60IUPO2K3jCEr6G1lejfSyebjFfN5GWUNZWrzU5QqBMiMC9g1nb7Ln-mtsuitirsDvRGBv2sCZ14d-7EyGgvGQ9bAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/smnYt6sMuJx6V1VJDdL0LEL3SKn8Uq4zl2FYn-NT8H0U1YjEVA7pt-XNyDBKUYUe6xPwbyT28bMMvuIxXe8UjqSs8BivDIx4aVI8TZ1G8QTjvy970f5G6WhiUumBXCUTtXuqGNfshC--x6EmBr5SNU0a3nWZ__-0KCO4KsJsjkrrmsYyHgJ2xIwuaaW7_ggDHiiSZ3ZdDpnaszAL_SDzfkM6SxrV9NuZtZcnW34DLy5qjtojaNQyrY5uYZ1QNh40yBAyZOWOADZPDJu020o2QEDSdyu5juopZ43o2TweRYoyBTnEsphcfDdKzRugRz7kjlQQxkaNwZJh3zsWrc66kA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‏
🔥
کلونر اتوماتیک و خفن تلگرام روی کلودفلر!
‏بچه‌ها، این ابزار Serverless روی ‌Cloudflare Workers⁩ بالا میاد و خوراکِ کپی کردن و همگام‌سازی کانال‌هاست؛ بدون نیاز به سرور و کاملاً رایگان.
‏
امکانات اصلی:
‏•
🚀
دیپلوی تک‌کلیکی:
بدون دردسر و سریع روی زیرساخت کلودفلر بالا میاد.
‏•
⚙️
فیلترهای پیشرفته:
می‌تونید فایل‌ها رو بر اساس نوع (ویدیو، عکس، سند) یا سایز دلخواه فیلتر کنید.
‏•
🤖
چند بات همزمان:
هر تعداد بات که خواستید اضافه کنید و تسک‌ها رو بدون محدودیت مدیریت کنید.
‏•
⏱️
همگام‌سازی لحظه‌ای:
هم بکلایت تاریخچه رو انجام میده و هم پست‌های جدید رو هر دقیقه سینک می‌کنه.
‏می‌تونید سورس کاملشو از گیت‌هاب (‌
iamLiquidX/telegram-clone-worker⁩
) بگیرید و با یه استار حمایتش کنید.
⭐
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/7759" target="_blank">📅 12:19 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7753">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/h0AEkRq1jC47ZOVyZSfwNx7yy9u9_aSAg7xO-FYS0aZhySjOkljUjJJtYQ9YZgk29Yex8nqYcI9hSMe601-cctW4ifFV7w1upViKLaqn9kpCuQDO4yZEV3vQvYWlIRSdlpcfuLzOY2d5L_FDCVRBGNrJCLvGCfK6CvqKPvScsVDrC7jjmAGDSC_vR772OkYViKcAnExjyVflU8acKdyEQp6Co-ty0EOiDRKU53e96UocVyXOFkoKyPLKcT0eq74XKJjZFq-VxDJD7BKNYKbTUu2uOFp4foMH9T1RIiD69vbaYkaB-CyXXN-BT7liAH0DKeST_Hn4NuzDTGOyfbiB6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/StQIfvySpyYF1jEc-Jd5We3DnaiiDVC5bfdyD0R05sVfWYYBCnV-9WGhlHCaMOC7A2rTf8E7rK_vMo4B2hnGQr8_be3i_KOb2s8dS-f_91BTCERsvgdlaBoaVU7hWjvkYh2NLKi6yUt4PZvSe-gVcikrIboPrU5gpu0C3-QRolsD5MxInDsfZwSM34_MF43F5Dp6coc0Y01oE1TyEtCdWsr-EZp9ompR0WLp3nOXf_zWIrUQTCH_sH6X_Nf5noh4Joc-lXodUJSN4Tl0LSSoyPBUsl3xno4AORSHVJVT6sfQlmARseNOvmOjeqxEucAD4j9V0CDTk6vNLxAps699nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/IGsb4RHlpeXz-EbvUgFDSddmP4ubmjEQHtinXaw_uYDnLW57uYSvn8rjkZ-4k5Mqu4rdYPZelnFv1a3NQtammZf3Of0dV6SHA7dCbkuxrLssE9vOzOdOepgbM_Uy3M969F4BcU-HauUoqYDMptebFl0HvFgDiTNRHf8ix7Q-PHpvvigRGN_NsDXkgpBLGOzkC7kWxRuhjR-qIAwQ9eMy4uDltJdjz4UA9gz0YPU0-k6-9HP8bmQvn16QY2HT0srI-WLIFTGzIWpQE_CyyCqy0-L50m2f5vM3eNgA0_i2VBwlI4oSozdsIFXU46iRXKcgQ47X19oF__wtk17pxRYs3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/mbpNlYs5lNiPCWRosfxDHf5sJYJSsuWHzZnnME-tsA5n1y8b1PmaJhQQ7CuNVI2uctmW7l0cCYwqXluvVqfoYYVbykjqCG0xiYRNAGpnP15nxgOVEWWWalglgWcMzQ-jWKHZiygbFATlOlw36phMAxqatfMBbaSzkJFyknR4aRB6dXMbvR4WU406r6ntD0va8crAbYquIeh1nXfMAZvJMeoQm1_UkJ81CQw-mq2Ek8sStFKd96eMGZKTEMJ2cGt60khpidDfDqmwXe_wwHpyxrkfqJsv3pTRHV3Sd9Ut4js5BiLqH6-TBXJmuriJXW7J_MDnwbrKq-MvaQqaHn9G4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/ZgySGMDZT5-3i39y5jLjfTLg1lPsNCC3zAuOvDePCopZlSZFYpyat2upC1leFx34qT4FsCRBaLEJSdmbEBiWojeqGTG2E9wISjFHinGTGFTxzFTCLED0_y1zDp_5IjwQjnwS0TpNhLAVuoeWQD-EZes-KKj4gd4jf2T1WnmJ33w53sHK2ErmbNPqyURIVAdn6urVuF4cifUOxaDREscWlQ7lCjoiDKpvjwpjhwyUMLMVcxLpRzsjt3cGc01KDlgVxPQKy6nSjQdkOWYMkT8Sp21YAdoh6A-En0pf2HWTqEEUynIm835-BDDL6F6qmpA5m86hq1t30izwWBEPwj_ajg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/QmGgHLWaGA0BU2UQ8FAKPOad_EZOzQ8LUGUWp5lUnnL33PmVOIro20HodGt7Kkf6IQn4e4RclEPt4RVJ-7hJABPP8IKtb_MXqf_vORsyuyqpxEOfbE5J74rQA7yiRvCHIoeg6e2M62up-nrRL5-CkxdmTK258FYlF_1k9BQsCEm3L5PBhsMdli-uIemRdm3TB3eNHXqfWhtYwpO8zygKbPKkUDot5CrImSaZPLT4yiNUGhRqa52nJrZfi9Mah9XeoTKyyTvKQ-wFcXr0tJ-aru6XNepjCtjwAvuQmhEunpzEIFAzjXmyNGh6ja0irNVMkGIIDtC1mFsW5v-x2Nc-8A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😎
از 265,000 اعتبار رایگان برای استفاده از مدل‌های برتر مانند GPT 6 ASTRA، CLAUDE FABLE 5.1، GLM 5.3، و غیره بهره‌مند شوید.
یک حساب کاربری جدید ایجاد کنید و فوراً 250,000 اعتبار دریافت کنید. با ورود روزانه 15,000 اعتبار دیگر کسب کنید و با انجام وظایف، اعتبار بیشتری به دست آورید. نیازی به کارت اعتباری نیست.
1min.ai
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7753" target="_blank">📅 10:13 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7752">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">⌨️
؛ DeepSeek V4.1 Flash، Muse Spark 1.3 و GLM-5.3 Flash به صورت رایگان در Cline Desktop
​تیم Cline یک برنامه دسکتاپ جداگانه با تمام قابلیت‌های یک عامل مستقل را راه‌اندازی کرده است.
​
📌
امکانات برنامه:
🤔
استفاده از ClinePass یا کلیدهای API شخصی
🤔
انتقال یکپارچه وظایف از Codex، Claude Code و سایر عوامل
🤔
برنامه‌ریز برای اجرای پس‌زمینه عامل
🤔
مدیریت سرورهای MCP، پلاگین‌ها و مهارت‌ها
🤔
مرورگر وب داخلی و ورودی صوتی
​
📌
مدل‌های رایگان موجود:
🤔
DeepSeek V4.1 Flash
🤔
Muse Spark 1.3
🤔
GLM-5.3 Flash
​
📌
نحوه شروع کار:
1⃣
دانلود برنامه:
https://cline.bot/desktop
2⃣
نصب و اجرای Cline Desktop
3⃣
ورود از طریق حساب Cline یا اتصال کلید API خود
4⃣
باز کردن پوشه کاری پروژه
5⃣
انتخاب یکی از مدل‌های رایگان از لیست
6⃣
ایجاد یک جلسه و اختصاص وظیفه به عامل
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7752" target="_blank">📅 01:44 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7751">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bAhrUS8jF7NTvOI886NzKNBFJ8fqWV4z98j0e4BknNt_PSZ3dWFQTiMz2WFPcVAh1MpFGDebI0a1aXaJnTbxMAiF-X9B2o_Alftt1fO-bS5ywJlKzhaiegZRgyiULMkdTpmA28It8wLCTslNvqsBIoKOCU7QuBB-17pWi1yQIRRmR6_sx_X6J1eo3wdwjrv2Mkp1-lZl4wWl9hiZ6ujdl06upAbjaEFKKBu68OI4QCAYD2OBUSxRlaBjlwJLokIBY3M08xd8W6n3sj4RWOB4dAGNpftxJzbG9g62KkMe1_R2pGtegjK_w0dw4xnlnZdF7175r9EBB9pBoM3VIPciCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
؛ LIGHTVELA - یک هوش مصنوعی رایگان که 24 ساعته در دسترس است.
4500 اعتبار و 100 میلیون توکن
مزایای طرح رایگان:
🤖
1 هوش مصنوعی
💳
4500 اعتبار در ماه
🖥
2 پردازنده مجازی + 4 گیگابایت رم (محیط تست)
💾
50 گیگابایت فضای ذخیره‌سازی
🌐
دسترسی 24 ساعته
📱
ادغام با تلگرام و سایر پلتفرم‌ها
نحوه دریافت:
به
lightvela.ai
مراجعه کنید.
یک حساب کاربری ایجاد کنید.
از آن استفاده کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7751" target="_blank">📅 22:06 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7750">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">کانفیگ مخصوص چنل -
سرعت خداا
vless://e4b11ac9-46f7-4cc0-92ed-bb9dfaaf3600@94.237.92.65:443?encryption=none&flow=xtls-rprx-vision&fp=chrome&pbk=lkMM9FR-o7Z6NwmmQVK8rLhCQR1mbJTgjY_0upeS2SY&security=reality&sid=0436301fb0178b&sni=google.com&spx=%2F442987454d44398&type=tcp#@ArchiveTell
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7750" target="_blank">📅 11:02 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7748">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/O3F0qxNh2RZgV2pJvsXyUqErd9uNatMu0CeKbb6fx8xaz0hUctoOjA1jJXxm0Uh2B-hyUbaPPnEthFqzP6Q3LrFVmfslsVzd46AMnGiuFpnEieiNWrICxIwiHgEfDK4jBQS97iq85d-FG0rQaDJzna5fNzdoXSwye1cZ3SY2xLVoquC-H9fxadCX0JIL6q9zRpGGyPjTFTfQMIz2isAvzWJFdktUGOYAJLXFbH0XlEa6UeGiq4xHB64LtBDj7g8Cd-wRGSZKIVy9iMHkmT5pHnr1rOnWSQSSh00S3-JJw5iDlsAu-Rw_BUV2mFp26UHa2gltNr24eYdNtd4UsV1UWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
از تاریخ ۱۴ تا ۱۶ سپتامبر، با ورود به
Z.ai
؛ ۶۰۰ میلیون توکن GLM-5.3 به شما تعلق می‌گیرد، بدون نیاز به اشتراک.
🔗
https://autoclaw.z.ai
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7748" target="_blank">📅 18:36 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7747">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/adqwvwrStK8gtEjomoOCKR5o6sspjz0k1XPCPb9Q2hL4UecSeZIUNgY6Kk7J7yMpMNEe5OokyKaJHZoaVwBZSTCH_XQq0-J0ssNsdnwOzRG2bxGSetVFcoDxUfgNptvcTDEyvb5mYW5khYF92p3sYr6EeJig1cwQKD-A9bX3PPkgilKdnkIFcTdnS4x_lwgtIbTutL-rSExN2GxF0P-xDemytvCfjaY7cl0uzdWTHr8uV0ATpHlWaFkkbVte2Dslni6Gk_GS5K42-ecq1jlGa--AL8MKERIqCBvhJm3ZIBcB2ZH43Hr8VEFvcW4CwLi_pxOPLBOYMxQhe1PTKiLsnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔓
رفع فوری خطای ریجن و تحریم Antigravity
اگر موقع کار با هوش مصنوعی Antigravity گوگل با خطای تحریم ریجن یا گیر کردن روی Eligibility Check روبرو شدید، ابزار متن‌باز
Open AG Patcher
در چند ثانیه این مشکل رو حل می‌کنه:
▫️
رفع محدودیت ریجن:
بدون نیاز به دستکاری یا تغییر کشور اکانت گوگل
▫️
پشتیبانی کامل:
از Antigravity 2 و Antigravity IDE و ترمینال (CLI)
▫️
امن و خودکار:
اجرای پچ با یک کلیک + بکاپ خودکار برای بازگشت به حالت اول
💡
نحوه استفاده:
ابزار رو اجرا کنید و شماره نسخه مورد نظرتون رو بزنید تا پچ در چند ثانیه اعمال بشه (سازگار با ویندوز، مک و لینوکس).
🌐
دریافت ابزار از گیت‌هاب
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7747" target="_blank">📅 16:52 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7746">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gbGckQtm7hYl_m3l0z9uqR0WpmeXt89hUT2AGxWUWa8O2LrDrQjQnL-KtI7FseGg_Sx8AhjOJVXQQT_JPzLUa91S55BVbDzWuAO8Q2uG3zU5_qCXuob1YHAKSS8co1dPv5Kp6rwAGt9CbmEkb4n8B9R36X4MGJz0LrxD_RH0bjUoS3Vekpoagbjni6lZCUHzWEHcCJs5TuECNopt7fu--a67tJ4KLKgquIf9fWEsmj3Txio1TGDlcK1WopBIomRxdpDGlx_JpU9glr3HlET_1bDYiJMMo4FLdjHT5zuAQo3c1JAf7cAKqVRjsUMcbPYT49ro4jsePE-HxPccJU6WKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
نحوه استفاده از Claude Opus 5 و GPT 5.6 Sol
به صورت رایگان
📣
حساب‌های جدید در
Verdent.com
، یک دوره آزمایشی 7 روزه با 100 اعتبار رایگان دریافت می‌کنند
💯
🆓
🎉
✍️
آنچه دریافت می‌کنید:
👀
🔍
☑️
Claude Opus 5 / Sonnet 5
✅
GPT-5.6
☑️
Gemini 3.1 Pro
✅
GLM-5.2
☑️
Kimi K3
📌
نحوه دریافت:
🔥
⚡️
☑️
به
➡️
🔗
https://verdent.ai/
مراجعه کنید.
✔️
برنامه دسکتاپ یا افزونه VS Code را نصب کنید.
☑️
یک حساب کاربری جدید ایجاد کنید
✉️
✅
مدل مورد نظر خود را انتخاب کنید.
☑️
از اعتبارها برای شروع استفاده کنید
🚀
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7746" target="_blank">📅 11:05 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7744">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔥
KiraAI
روزانه ۵۰ میلیون توکن رایگان
🤖
مدل‌های موجود قابل استفاده :
⚡️
kira-3.5-pro
⚡️
kira-3.5-flash
⚡️
kira-3.0-image
🔗
kiraai.vn
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7744" target="_blank">📅 23:09 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7743">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔎
scite.ai
— موتور جست‌وجوی استنادی برای تحقیق جدی
۷ روز اشتراک رایگان (تریال رسمی سایت)
📑
Smart Citations
نشان می‌دهد هر مقاله توسط مقالات دیگر تأیید شده، رد شده یا فقط اشاره شده — نه فقط تعداد استناد
🧠
Assistant
پرسش پژوهشی‌ات را می‌پرسی و پاسخ با استناد واقعی و لینک به منبع می‌دهد، نه حدس
🤖
دسترسی به مدل‌های تحقیقاتی:
Claude Sonnet 5 | Claude Opus 4.6 | GPT 5.2
🎛
Personalized Feed
فیلتر و شخصی‌سازی حوزهٔ تحقیق ، فقط موضوعات مرتبط با کارت را ببین
🔗
Custom Dashboards
داشبورد اختصاصی برای کلیدواژه، نویسنده یا ژورنال خاص + هشدار مقالهٔ جدید
📊
Analyses & Topic Classification
دسته‌بندی موضوعی، شناسایی روندها و گپ‌های پژوهشی
آموزش فعالسازی
🔗
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7743" target="_blank">📅 22:40 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7742">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nVeLM9cXiJlURtqw-W1Naj-c_0FQDQ4lfVVJvFKaLxvt0YBRvjE-E-OE63CWtA5LgQKal9_zr-AuZRnHCbuDdohez0P32wuYFTboLHqyIuzC4YcCINo9aOAGdDPd4qfjS3fNf9nUX6gaEMHzhR3EDUXmX9qBQV87OJ1NYwv13nWveGtguTJqCo1MGxy7wcjuPQERWcaCpUhe2tPggPBCe30a8XbFO2zaJJ4E4mKI2Bul8TiG1VGsKmvBnL2BC78bwgeEy6A4EX_fsWxPwnDSg8mvyhACx5vW_MfYCN1r2H1jC0tCyl4A_xJBY8u3ntTqvlSXtegJNUmByNweUhG9Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
دسترسی به Seedance 2.5 و سایر مدل های تولید ویدیو، عکس و اتوماسیون
آموزش
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7742" target="_blank">📅 22:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7741">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">keys.txt</div>
  <div class="tg-doc-extra">2.7 KB</div>
</div>
<a href="https://t.me/ArchiveTell/7741" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎁
دریافت 20,000,000 توکن رایگان  claude-fable-5 | claude-sonnet-5 |  deepseek-v4-pro | muse-spark-1.2
✅
وارد ربات زیر بشید و api key رو دریافت کنید  @kiro86bot
💡
سازگار با همه سرویس‌های OpenAI-Compatible
🌐
base url: https://api.xpiki.com/v1
🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7741" target="_blank">📅 22:17 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7740">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BqorlWjtuq79i41ZcKWeXvsuC1cqUxqIbEeaKU6GOygUy1D-lN8aS4F6ju7OhJnpmfDHl7UI4T_aEVuBPXOwUgD0AG7kDmGb7Y_41iS2atEHMLnBfxnkbIOA0qzAhuFJb-neHJ2XkKd5KumvMnCHioDerGMJ8mbIWGbiagMdBvqvrSKsBihKpYlZygzt3KYWKFblMqm-Pat6qYD-iHXq76WlwH3tQOlrUCiPDc2PWbSIJGsAI34_RJD-2pAhjgZ02cD8rtVlVBDDpTcTnUAroSp6rY039llNBvtYF9fgVHHIAQ1vuvsU_-KORP1yMktHrzGnwvYw4J306glFLPe4eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🎁
دامنه رایگان همیشگی بدون کارت اعتباری!
‏بچه‌ها این
پروژه گیت‌هاب
با نزدیک ۲۰۰ هزار استار، دامنه‌های رایگان دائمی میده که واسه پروژه‌های تستی و سایدپراجکت‌ها کاملاً خوراکتونه.
🚀
‏•
دامنه‌های متنوع:
پسوندهایی مثل
.us.kg
و
.qzz.io
بدون هزینه فعال می‌شن
‏•
کنترل کامل:
دسترسی کامل به
Custom Nameservers
و تنظیمات
Cloudflare
دارید
‏
💬
نحوه استفاده:
کافیه برید به سایت پروژه، اکانت بسازید، دامنه دلخواهتون رو ثبت کنید و نیم‌سِروِرهای کلادفلر رو ست کنید.
‏
🔗
سایت پروژه
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7740" target="_blank">📅 18:59 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7739">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">⌨️
ترجمه سریع و هوشمند، بدون دردسر!
اگه دنبال یک مترجم ساده و کاربردی هستید که فقط به یک سرویس محدود نباشه، پروژه Translator می‌تونه انتخاب خوبی باشه. این پروژه با پشتیبانی از سرویس‌ها و مدل‌های مختلف ترجمه، امکان ترجمه متن، استفاده از قابلیت‌های صوتی و مدیریت تاریخچه ترجمه‌ها رو در یک محیط مدرن و ساده فراهم می‌کنه.
🤖
قابلیت چت با هوش مصنوعی؛
با استفاده از API Key با مدل‌های هوش مصنوعی گفتگو کنید و پاسخ‌های هوشمند دریافت کنید.
🔑
همچنین امکان استفاده از API Key و ترجمه با سرویس‌های هوش مصنوعی مختلف رو داره.
🌐
نسخه آنلاین:
https://codewave4.github.io/Translator/
🔗
سورس پروژه:
https://github.com/codewave4/Translator
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7739" target="_blank">📅 18:42 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7738">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/087627b2c4.mp4?token=UzoCBx2H7VXw0PvPIEaPGMY4xGwps3zwRk4ZnvWUZROyjfl9NHkq7H-pN_MRzr7Tj8iMeBLUweiyixFbGQtw56PZkB0UHXcBnPOkc93ArpVOIRWebdXfjrDh8ouHEEhAWd996FyuMzGUR3qSjrloFy_s_R1myFImhvdETPga_UA8UMwgm7T3-L3S_yE6DS2EvzWCWRu98woUuPnGVhEEPfZ760s_TVQSI94G-2KfaYFs5qQMMIBQLPSzoT8g4C7ER3RZFqJX2HC1MZ6q7wbxufR5DN56wlxBx8Lw6OpTU-yu90GAIAZHoAeN4gAy_BQA0efc7yyH6priUdhTgU9Vug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/087627b2c4.mp4?token=UzoCBx2H7VXw0PvPIEaPGMY4xGwps3zwRk4ZnvWUZROyjfl9NHkq7H-pN_MRzr7Tj8iMeBLUweiyixFbGQtw56PZkB0UHXcBnPOkc93ArpVOIRWebdXfjrDh8ouHEEhAWd996FyuMzGUR3qSjrloFy_s_R1myFImhvdETPga_UA8UMwgm7T3-L3S_yE6DS2EvzWCWRu98woUuPnGVhEEPfZ760s_TVQSI94G-2KfaYFs5qQMMIBQLPSzoT8g4C7ER3RZFqJX2HC1MZ6q7wbxufR5DN56wlxBx8Lw6OpTU-yu90GAIAZHoAeN4gAy_BQA0efc7yyH6priUdhTgU9Vug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🎬
ساخت موشن‌گرافیک حرفه‌ای با یه پرامپت!
‏این ابزار هوش مصنوعی کل فرآیند ساخت تیزر تبلیغاتی، از استوری‌بورد تا تدوین صدا و انیمیشن رو خودش انجام میده و خروجی رو با بیت موزیک سینک می‌کنه. خوراک بچه‌هاییه‌ که سریع میخوان خروجی باکیفیت بگیرن.
🔥
‏
⚡️
دسترسی به منابع غنی:
۱۵۷ مدل سناریو، ۲۱۴ استایل بصری و کلی الگوریتم انیمیشن آماده
‏
⚡️
شروع سریع:
کلی تمپلیت آماده‌به‌کار داره که کار رو برای پروژه‌های فوری جلو میندازه
‏
⚡️
عملکرد هوشمند:
کافیه ایده‌تون رو متنی بدید تا در لحظه ویدیو تحویل بده
😎
برای دانلود ابزار تولید ویدیو
اینجا
کلیک کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7738" target="_blank">📅 16:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7737">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">1.7B token MINIMAX
url:
api.minimax.io/v1
key:
sk-cp-k8fnOYl1xeWGiSNy7qWxNP3Gu-nkuMKLaAFl7ZoCnGiqA2sabKF30eMTQNurXcyGtgGdbM168WEvBhyTOo2WQaE9RoXzVPAyyG3CYwZuybXzDILyBEBc5nk
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7737" target="_blank">📅 14:09 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7736">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vSmsBogif_LvicZTpAM8R6OpHEDfOgq_HxiiDw5XyHoQintS2SA3VVHVwvike0k1F562yatSu-iwG-LuNudcwJSv89SqGMh_ebYSGIhwOHRUAsWn79ugUgQQVuhpuT6xiwI9Dw2TDFerVE0RK42UoQfO7i-EvsY17X8-9lpmN3Hpnu6_sPytwzRaSi0mNJFKdPSTDgdql0VBlR6WBhkdk6e9oOzS5gwfgFDTrZhIP9ozcZ4isJohwu27VaO2LweAuMPFtgznN2n_3caBEOoZ3CbkCMyAmUNIJtGFIrj1VoHrv-XhFwHM0J3jFCghaNHY5wlymJ2BGgiXSuGLBabmGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🔥
مرجع خفن اسکیل‌های ‌Claude Code⁩ و ‌Codex⁩!
‏سایت ‌SkillsMP⁩ یه کاتالوگ تر و تمیز با بیش از ۳۳ هزار اسکیل آماده‌ست که تو کار با هوش مصنوعی کلی جلوتون میندازه.
🤖
‏•
دسته‌بندی جامع:
از برنامه‌نویسی و ماشین‌لرنینگ تا امنیت و کار با ‌API⁩
🔍
‏•
دسترسی سریع:
لینک مستقیم به گیت‌هاب برای هر اسکیل
📂
‏•
کیفیت‌سنجی:
دارای ایندیکاتورهای کیفیت برای انتخاب بهترین ابزارها
⚡️
‏خوراک بچه‌های وایبکودره که بخوان پرقدرت‌تر پروژه‌ها رو ببرن جلو.
🚀
🔗
skillsmp.com
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7736" target="_blank">📅 14:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7735">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🛡
دیگه ایمیل و پسورد اصلیت رو به هیچ سایتی نده!
حتماً براتون پیش اومده که برای ثبت‌نام در یک سایت مجبور شدید ایمیلتون رو بدید، اما بعد از یه مدت صندوق ایمیلتون پر از پیام‌های تبلیغاتی مزاحم شده یا اون سایت هک شده و رمزهاتون لو رفته!
ابزار جالب
AliasVault
دقیقاً برای حل همین مشکل ساخته شده:
💎
این ابزار براتون چیکار می‌کنه؟
⚡️
ساخت بی‌نهایت ایمیل دائمی:
برخلاف ایمیل‌های موقت که بعد از ۱۰ دقیقه می‌پرن، این ایمیل‌ها
کاملاً دائمی و همیشگی
هستن و برای هر اکانت می‌تونید هر تعداد ایمیل دلخواه که خواستید بسازید!
⚡️
دریافت کد ثبت‌نام داخل خود برنامه:
نیازی نیست برید یه ایمیل دیگه باز کنید؛ ایمیل‌های تایید و کدهای ورود مستقیماً داخل همین برنامه براتون میاد!
⚡️
مچ‌گیری از سایت‌های متخلف:
اگر یه سایت ایمیل شما رو به تبلیغاتچی‌ها بفروشه، دقیقاً می‌فهمید کار کی بوده چون برای هر جا یک ایمیل اختصاصی ساختید.
⚡️
نصب روی گوشی و کامپیوتر:
هم اپلیکیشن برای موبایل داره و هم افزونه برای مرورگر، و خودش پسوردها رو سر جای درست پر می‌کنه.
💬
چرا این ابزار فوق‌العاده‌ست؟
•
ایمیل‌ها هرگز منقضی نمی‌شن:
هر زمان در آینده بخواید وارد سایت بشید یا رمزتون رو بازیابی کنید، پیام‌ها باز هم به همین ایمیل دائمی میاد.
•
سقف تعداد ندارید:
برای ۱۰۰ تا سایت هم می‌تونید ۱۰۰ تا ایمیل مستعار و رمز مجزا بسازید.
•
کاملاً رایگان و امن:
بدون هیچ هزینه‌ای، امنیت و آرامش صندوق ایمیلتون رو تضمین می‌کنه.
🌐
ورود به وب‌سایت AliasVault
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7735" target="_blank">📅 12:42 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7734">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GiF3Y2e4tDvdxVI56dhZivx8MRYDNXpD-_b0iqF1bz_wfOHpsuO91XH9DvPN01FgFMwYliuFRvcCQnOCw4L2u-h0XSoka64p6Ww9N4to5vureVtY3tLVD54oQV-wGDkfbbK8kWTBGyHfAUhOfJA3yleRs98zFvz2O9RHXYFUHS6mcyWcpxq0I49KnaGyYw_ry5_cIxqNxuDcjljBRrs3hegXBGUI1g0mQ_QT54WJ31qjkiCk52rvjaDEj5GQCRP6YsYgdQT68xi17W4ZkyyTsxjUKY2uQsi0icx2Vs9kctZSW_5Xm1hcBhctkPgkTygPAkwwOHi_WQA8iy-sjvlJCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک سایت، ده‌ها مدل و ابزار با اعتبار رایگان روزانه
🎁
💬
Multi AI Chat
GPT، Claude، Gemini، DeepSeek، Grok، Qwen ، Llama
همه در یک چت، با امکان مقایسه جواب‌ها
🎨
تولید و ادیت عکس
تولید تصویر از متن (Flux، Stable Diffusion، Ideogram…)
حذف/تغییر پس‌زمینه، حذف اشیاء و متن از عکس
Face Swap، Upscaler، تبدیل اسکچ به تصویر
ویرایش عکس با دستور متنی + تولید تصویر سه‌بعدی
🎬
ویدیو
تولید ویدیو از متن و از عکس
Face Swap روی ویدیو
خلاصه‌سازی، زیرنویس و ترجمه ویدیوهای یوتیوب
🎵
صوت و موسیقی
ساخت آهنگ (Suno، MusicGen…)، Text-to-Speech با صداهای طبیعی
شبیه‌سازی صدا (Voice Clone)، تبدیل ویس به متن، حذف نویز
✍️
نوشتن و تولید محتوا
تولید محتوا، بازنویسی، خلاصه‌سازی، ترجمه، گرامر
تحقیق کلمه کلیدی و تشخیص محتوای AI
🌐
لینک سایت :
app.1min.ai
🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7734" target="_blank">📅 12:24 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7733">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🎁
دریافت 20,000,000 توکن رایگان
claude-fable-5 | claude-sonnet-5 |
deepseek-v4-pro | muse-spark-1.2
✅
وارد ربات زیر بشید و api key رو دریافت کنید
@kiro86bot
💡
سازگار با همه سرویس‌های OpenAI-Compatible
🌐
base url:
https://api.xpiki.com/v1
🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7733" target="_blank">📅 11:16 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7732">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🆓
هوش مصنوعی رایگان  — بدون ثبت‌نام
Kimi K2.6 | GPT 5 mini | DeepSeek V3.2
📌
امکانات:
⚡️
چت هوش مصنوعی نامحدود
⚡️
تولید متن و محتوا
⚡️
بدون ایمیل، بدون رمز عبور، بدون کارت بانکی
📌
نحوه استفاده:
🔗
وارد
این سایت
بشید مدل موردنظر را انتخاب کنید و شروع کنید.
🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7732" target="_blank">📅 23:45 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7731">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BJT-QtWzsXHG6jmruBvYbsdLqf4Er6G9WxKlFbrOddCdq_26e4K9XP_1Un-k4ZnMLXAlai05GY_5D6F7vFhKFHZk7pvMi9XJfyYzgboaUK68iHd_vFnJ59ousV0bv45PNWoeYO23LAYHQwEAMdMGxvm__sB5S8uT9OOWQNoQbRNIGaN38Gncd-NteprW_4EyogLo8FJiXD1bn-SCPvmtuUxkbm43Rh-6GmYNpthPXB2z8BMKgewspb_yzr9v248aVWfK-WTW8EEkU6zQfJzO7RzC1ypTis_gLpb_vq8Kz7XL0ysRKHK_oe3CCWpM82tKVfc1-4q3iFCwEU8sUKTB4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🆓
۵۰۰ مگابایت پروکسی رزیدنتیال رایگان (
proxyma1.io
)
یک سرویس پروکسی رزیدنتیال که با ثبت‌نام از طریق تلگرام ۵۰۰ مگابایت ترافیک رایگان می‌دهد و API هم دارد.
📌
نحوه دریافت:
1️⃣
وارد سایت
proxyma1.io
شوید و ثبت‌نام کنید
2️⃣
پس از ثبت‌نام، یک پیام برای استارت ربات تلگرام نمایش داده می‌شود که داخل آن یک کد هدیه قرار دارد
3️⃣
ربات را استارت بزنید و کد را برای ربات ارسال کنید
4️⃣
۵۰۰ مگابایت به حسابتان اضافه می‌شود
🚀
📌
ویژگی‌ها:
☑️
پروکسی رزیدنتیال (Residential)
☑️
۵۰۰ مگابایت ترافیک رایگان
☑️
پشتیبانی از API
☑️
ثبت‌نام آسان با تلگرام
🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7731" target="_blank">📅 23:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7730">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qG7NCx71N0mtjCQKOPFBK1t3smzvFo0uXqNuWfjYujjQOeDFL_M4OPwa3oWs0ZOJT3vsgJhjmHJAvtqcWs7dRghkqNhtiBYseb1Ep5RrZsw-9S6duEoQJWLI2CIfc-hTneot3MV8L-JAZAKKI-3x5cG8sFGqFP3bzVe1LWsqEjqPhpFFBtA3zHmXOI-9xwMaWtQ3avkz3qG07NyiHrJikkCIGtnYp_mqf3AG-n3a1tekuMSKYCuPeBslFRlupb59vXlw0XYaU1iU2yIxST6XZblYKtYTO6iJY6ZgE8szn677h-X0D6rMQ7_nGIeIoiqcrJBctUY8cNr_2XQp0GsqMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
۵۰۰۰ اعتبار رایگان برای مدل‌های برتر هوش مصنوعی
پلتفرم جدید در شروع کار ۵۰۰۰ اعتبار به شما هدیه می‌دهد تا با قدرتمندترین شبکه‌های عصبی کار کنید: تولید متن، عکس و ویدیو در یک جا.
📌
امکانات در دسترس:
☑️
چت چندمدلی
☑️
تولید تصویر
☑️
تولید ویدیو
☑️
موجودی اولیه: ۵۰۰۰ اعتبار رایگان
🪙
📌
روش دریافت:
1️⃣
ورود به
getunikey.ai
2️⃣
ثبت‌نام یک حساب کاربری جدید
3️⃣
ایجاد کلید API در تنظیمات پنل
4️⃣
استفاده در رابط چت یا ابزار های واسط
base url:
https://getunikey.ai/v1
🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7730" target="_blank">📅 23:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7729">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔍
Hidden File Hunter — شکارچی فایل‌های مخفی ویندوز
دنبال فایل‌های مخفی و سیستمی توی ویندوز می‌گردی ولی پیدا کردنشون واقعاً دردسره؟ این ابزار دقیقاً برای همین ساخته شده
👇
؛ Hidden File Hunter یک برنامهٔ دسکتاپ ویندوزیه که تمام فایل‌های مخفی و سیستمی درایوهات رو پیدا می‌کنه و توی یه جدول مرتب و قابل مرور نشونت میده.
✨
امکانات:
✔️
پیدا کردن تمام فایل‌های مخفی و سیستمی در همهٔ درایوها
✔️
نمایش نتایج در یک جدول مرتب و خوانا
✔️
خروجی گرفتن از فهرست کامل مسیرها در قالب فایل TXT
✔️
کپی کردن خود فایل‌ها با حفظ ساختار پوشه‌ها در مقصد دلخواهت
✔️
فقط می‌خونه و کپی می‌کنه — هیچ فایلی رو تغییر نمیده، حذف نمی‌کنه و بهش دست نمی‌زنه
✔️
ساخته‌شده با Python و PySide6
✔️
تم تیره و روشن
✔️
رابط دوزبانهٔ فارسی و انگلیسی
یه ابزار ساده، سریع و امن برای وقتی که می‌خوای بدونی توی سیستمت چه چیزهایی از چشم‌ها پنهان مونده.
🔗
لینک گیت‌هاب:
github
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/7729" target="_blank">📅 22:37 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7727">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚀
اپلیکیشن Bifrost (بایفراست)؛ پل ارتباطی فوق‌سبک تلگرام بر بستر ورکر کلادفلر منتشر شد.
بایفراست یک بریج لوکال (Local SOCKS5) مدرن و بهینه برای اندروید است که ترافیک تلگرام رسمی را از طریق پروتکل TWP به ورکر رایگان کلادفلر متصل می‌کند؛ با پینگ پایین، بدون قطعی و با سرعت دانلود فوق‌العاده بالا.
🔒
بدون نیاز به VPN، بدون روت و با مصرف باتری نزدیک به صفر:
این پروژه کاملاً متن‌باز (Open-Source) است و برخلاف فیلترشکن‌ها از VpnService استفاده نمی‌کند (هیچ علامت کلیدی بالای صفحه نمایش داده نمی‌شود و اینترنت سایر برنامه‌ها کاملاً دست‌نخورده و بدون تغییر باقی می‌ماند). مصرف پردازنده در زمان عدم استفاده دقیقاً ۰.۰٪ است و امنیت و رمزنگاری پیش‌فرض تلگرام (MTProto) نیز کاملاً حفظ می‌شود.
📥
دانلود و نصب برنامه (از گیت‌هاب):
https://github.com/Qorvhex/Bifrost/releases
⚡️
کانفیگ تستی برای شروع (بعد از نصب، کپی کنید و داخل برنامه Paste کنید):
twp://telp.qorvhe-x.workers.dev?clean_ip=1music.cc#Bifrost-Test
🛠
سورس‌کد اسکریپت ورکر (TWP):
https://github.com/Qorvhex/TWP
📁
لینک پروژه و سورس‌کد در گیت‌هاب:
https://github.com/Qorvhex/Bifrost
لطفاً تستش کنید و سرعت و عملکردش رو بهم بگید!
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/7727" target="_blank">📅 21:16 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7726">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🖥
مرورگر ضد ردیابی Private Browser Pro؛ هویت جعلی و دور زدن بن شدن اکانت‌ها!
​بچه‌ها اگه نیاز دارید روی یک سایت چند اکانت مجزا بسازید بدون اینکه سیستم‌های امنیتی بفهمن همه‌شون مال یک نفره، یا می‌خواید ردپای دیجیتالی‌تون رو کامل مخفی کنید، این مرورگر اوپن‌سورس ویندوزی دقیقاً همون چیزیه که دنبالشید. این ابزار بر پایه نسخه فوق‌امن Ungoogled Chromium و Electron ساخته شده و از زبان فارسی هم پشتیبانی می‌کنه.
​
🎭
جعل مشخصات سیستم (فینگرپرینت):
شبیه‌سازی کارت‌های گرافیک قدرتمند (مثل RTX 4090، سری RX 7900 و تراشه‌های اپل)، اضافه کردن نویز به Canvas و AudioContext و هماهنگ‌سازی هدرها برای عبور آسان از سد کپچاهای Cloudflare Turnstile، hCaptcha و reCAPTCHA
​
📁
مدیریت و تفکیک کامل پروفایل‌ها:
امکان ساخت محیط‌های دائمی (Persistent) برای ذخیره دیتای هر اکانت در پوشه جداگانه، یا حالت موقت و یک‌بارمصرف (Ephemeral) که با بستن پنجره کل ردپا پاک میشه + دکمه پاک‌سازی آنی
​
✅
پروکسی پیشرفته و ضد نشت اطلاعات:
پشتیبانی از پروکسی‌های SOCKS5 و HTTP (با یوزرنیم و پسورد)، حل آدرس‌ها از داخل پروکسی جهت جلوگیری از DNS Leak و غیرفعال‌سازی WebRTC برای مخفی ماندن کامل IP واقعی
​
✨
محیط کاربری تمیز و دو زبانه:
کرومیوم دست‌نخورده بدون واترمارک‌های تستی، تم دارک با کلیدهای میانبر سریع و پشتیبانی کامل از منوی فارسی و انگلیسی
​
💡
بهترین سناریوی استفاده:
ایده‌آل برای مدیریت چند اکانت در شبکه‌های اجتماعی و پلتفرم‌های حساس، تست وب، ریسرچ‌های OSINT و حفظ حریم خصوصی بدون نیاز به خرید اشتراک‌های گران‌قیمت مرورگرهای ضد ردیابی.
​
🔗
گیت‌هاب
​
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/7726" target="_blank">📅 21:04 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7725">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">📥
تبدیل فایل‌های تلگرام به لینک مستقیم نیم‌بها با ربات Leecher!
بچه‌ها اگه کندی دانلود از تلگرام یا قطعی فیلترشکن موقع دریافت فایل‌های حجیم کلافتون کرده، یا می‌خواید تورنت و ویدیوهای یوتیوب رو مستقیم به فایل تلگرامی تبدیل کنید، این ربات لیچر ایرانی حسابی به کارتون میاد.
🇮🇷
لینک مستقیم با ترافیک نیم‌بها:
تبدیل آنی فایل‌های تلگرام به لینک دانلود پرسرعت تحت وب (سازگار با دانلود منیجرها) با محاسبه مصرف اینترنت به‌صورت نیم‌بها
🌐
دانلودر همه‌کاره (لینک به فایل):
پشتیبانی از دانلود مستقیم لینک‌های یوتیوب، اینستاگرام، وب‌سایت‌ها و حتی فایل‌های تورنت و تحویل فایل داخل چت
☁️
اتصال ابری به گوگل درایو:
امکان لینک کردن اکانت شخصی Google Drive برای ذخیره و آپلود مستقیم فایل‌ها در فضای ابری بدون مصرف حجم گوشی
🎁
شارژ رایگان روزانه:
۱ گیگابایت حجم رایگان در هر ۲۴ ساعت بدون نیاز به پرداخت هزینه یا خرید اشتراک
💡
نکته کاربردی:
لینک‌های ایجادشده بین ۶ تا ۸ ساعت معتبر هستند؛ کافیه فایل رو به ربات بفرستید، لینک مستقیم سرور ایران رو داخل IDM کپی کنید و با حداکثر پهنای باند خط‌تون دانلود کنید.
🔗
استارت ربات
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7725" target="_blank">📅 20:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7723">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ukBS15aHukzCYfVXae6mZy7BWbwOWrFzvwDOZRYIvfOEpKCHpaM7Via9gR8kOR3Qpo-afiqhHOhuTZyy4mLfFoeGFgSxhV8-6pNBCV7ZctTZ_TzMTU5GlYLyN4E-CEcR7k-UbxP_s5rIQ7CjkcUKFGa8e24t9wQaV2VVFlWWqSMK9gVab7JCyoZdADU9KdBi52wbBzujnvMLZmxrQrFLAvAPg1r1f9rGqlfhXw5O_UkWwfjhzEH7fVl7W0GjPtFl64wSYC44_RghcSIV5xDAV7WDCWYIuAweQasDA-hQN9inWOC3qwWFdHn1fUIq_7bko0ZAJ4e6xsUXj_3OPbN5HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید (1.8.0) برنامه MSN-GUARD منتشر شد :
💢
BOOM
💢
تغییرات :
1- اضافه شدن متد اختصاصی SHARD برای اولین بار
-_-_-_-_-_-_-_-
2- دسترس‌پذیری کامل و پشتیبانی 100% از صفحه‌خوان TalkBack برای عزیزان نابینا و کم‌بینا برای اولین بار
-_-_-_-_-_-_-_-
3- آپدیت هسته
-_-_-_-_-_-_-_-
4- اضافه کردن قابلیت Backup و Restore و Reset Factory از تنظیمات برنامه
-_-_-_-_-_-_-_-
5- برطرف شدن مشکل دکمه Reconnect در نوتیفیکیشن
-_-_-_-_-_-_-_-
6- اضافه شدن Theme کاملا روشن برای استفاده زیر آفتاب
-_-_-_-_-_-_-_-
7- برطرف شدن باگ اتصال خودکار پس از قطعی اینترنت و چند باگ دیگر
-_-_-_-_-_-_-_-
6 روش دسترسی به اینترنت آزاد:
1: متد Masque
2- متد Wireguard
3- متد Warp On Warp
4- متد Psiphon (اختصاصی و اولین)
💯
5- متد Tor (اختصاصی و اولین)
💯
6- متد SHARD (اختصاصی و اولین)
💯
💻
ریپازیتوری گیت‌هاب (متن‌باز):
https://github.com/mbm110/MSN-GUARD
📌
لینک مستقیم دانلود :
برای گوشی های 64 بیت
برای گوشی های  32 بیت
برای تمامی گوشی ها
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/7723" target="_blank">📅 18:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7722">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">✉️
؛ Turbo Mail ایمیل موقت، سریع و بدون دردسر
اگه برای ثبت‌نام یا دریافت کد تأیید به یه ایمیل موقت نیاز دارید، Turbo Mail یه گزینه ساده و سریع برای شماست.
⚡️
ساخت فوری ایمیل موقت
👌
بدون نیاز به لاگین و ثبت‌نام
⏳
اعتبار ۲۴ ساعته
🔒
مناسب برای دریافت ایمیل و کدهای تأیید
🚀
ساده، سریع و بدون مراحل اضافی
کافیه وارد سایت بشید، ایمیل موقتتون رو بسازید و استفاده کنید.
🔗
https://mail.turbocenter.shop
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/7722" target="_blank">📅 18:12 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7721">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🎧
دستیار هوشمند و همه‌کاره موزیک‌بازها؛ دانلود با کیفیت FLAC با ربات MelodyAddict!
بچه‌ها اگه عشق موسیقی هستید و از دانلود تک‌به‌تک آهنگ‌ها، افت کیفیت یا پیدا نکردن موزیک پس‌زمینه کلیپ‌ها کلافه شدید، این ربات فوق‌العاده با پشتیبانی کامل از زبان فارسی دقیقاً خوراکتونه. همه‌چیز از شزم اختصاصی گرفته تا رصد خودکار پلی‌لیست‌ها رو براتون یکجا جمع کرده.
🔄
سینک خودکار پلی‌لیست‌ها:
زیر نظر گرفتن لایک‌ها و پلی‌لیست‌های Spotify، SoundCloud، YouTube Music و Apple Music و ارسال خودکار ترک‌های جدید با امکان زمان‌بندی ارسال (۳ ساعته، روزانه یا هفتگی با دستور /digest)
🔍
شناسایی جادویی آهنگ:
پیدا کردن نام و فایل موزیک فقط با فرستادن یک وویس کوتاه، زمزمه، فایل ویدیویی یا لینک ریلز اینستاگرام، تیک‌تاک، یوتیوب و توییتر
💎
کیفیت استودیویی FLAC و Lossless:
قابلیت تنظیم کیفیت پیش‌فرض خروجی برای گوش دادن به بالاترین بیت‌ریت ممکن، با سرعت عالی و کاملاً بدون تبلیغات
📂
مدیریت پلی‌لیست‌های ابری:
امکان دسته‌بندی، ساخت و اشتراک‌گذاری مستقیم پلی‌لیست‌های شخصی داخل تلگرام
💡
نحوه استفاده:
ربات رو استارت کنید، زبون رو روی فارسی بذارید و برای شروع کافیه وویس یک آهنگ یا لینک پلی‌لیست موردعلاقتون از اسپاتیفای یا ساندکلاد رو براش بفرستید تا بقیه کارها رو خودش اتوماتیک انجام بده.
🔗
استارت ربات هوشمند
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/7721" target="_blank">📅 16:52 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7720">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bPVNvVT8oVC4HWhU-kwWQPXTZvUR91qMOahFfuQAb-MoHdThMmlfRIT8qTDTePbeoXOQvGT_GfwsNaqK-DZ7bwL6bOxGN8-tS9qF_iU25eFpmvogXNnBfzRff9JbuW9klZeNV-P42PaCnsl26UrjmN1V76wH5RaPDP8d-owHivbXx59W_jCOSNhCgGj7RXkEd2diJzJXSG1XAgF_6obFpwzkWY1c4Bd5I0IA5iUoeuCei8KwWCKlsp8oGq9-yj2Zq7jYzwbkM5bzJB4ebeBXzEGD5RD8ravLwAMoXQ0ifl3NC5yPAWpozOxN-SyaXIAisS6val4Qs4_B6MsHPmZAXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آپدیت جدید ArasClient منتشر شد!
نسخه جدید با اضافه شدن بخش Free منتشر شد و از این به بعد این بخش به‌صورت مرتب آپدیت میشه.
📱
؛ ArasClient یک کلاینت سبک و کاربردی برای مدیریت و استفاده از کانفیگ‌هاست که تمرکزش روی سرعت، سادگی و اتصال راحت‌تره.
🆕
اضافه شدن بخش Free
⚡️
آپدیت منظم کانفیگ‌ها
📊
تست و مرتب‌سازی هوشمند سرورها
🔄
انتخاب سریع‌تر سرورهای مناسب
📦
پشتیبانی از نسخه‌های مختلف اندروید
🔗
دانلود نسخه جدید:
https://github.com/ArasTey/ArasClient/releases/download/v1.6.8/ArasClient_1.6.8_arm64-v8a.apk
🔗
سورس پروژه:
https://github.com/ArasTey/ArasClient
💬
نظر، انتقاد یا پیشنهادتون رو کامنت کنید.
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/7720" target="_blank">📅 15:57 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7718">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IFmTC-Q5w7ARpjQDHJE1285ruG4sxCijgEuHFUaukXMjY88JL2QhsewaBbIBoMdEk3AGgyTGlRFEVJM988LAloVqtI0oX_tJrrwQ9JZ08ebLXRW0G3iimXqPXKiMDuqskDPySCOw64N4_0__UwrPMC_7IanRm7mJfTbIVO0X0aaNk7q4GOQx11D_iMYma00nMVeQFIxnzUrV0SPScsOQHkou2uaRtX-dgJXVeP29s5_Jf2VEs2eng6PpELbq6Jki2yYjWVyM-_yQkxs1Pmmqb8_x4Cti5v-TjBe7AafSoBh-FL9r7eDEr2FS6rnAjtzFL7Fx2XnibEnTwgJo0ioNfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⌨️
اگر می‌خوای شبکه‌های کامپیوتری رو از پایه تا سطح حرفه‌ای یاد بگیری، نت‌داد دقیقاً برای تو ساخته شده.
از مفاهیم بنیادی مثل آدرس‌دهی IP، سوییچینگ، مسیریابی و امنیت گرفته تا شبکه‌های مدرن، همه چیز با پروژه‌های عملی و مثال‌های کاربردی آموزش داده می‌شه.
✔️
۱۰۰٪ پروژه‌محور
✔️
۵۳ درس تخصصی
✔️
۱۴ بخش آموزشی
شروع یادگیری از اینجا:
🔗
https://netdad.vercel.app
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/ArchiveTell/7718" target="_blank">📅 15:14 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7717">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mOAyZHpSVG_cg7_XHS01YVLj9DdJ0PHOD1nVn9J6FiCZ7M6leVL6Ip3F4289eA6Bx9fKS1hjVLLDtbBWnjNeBOcS84C6ykniNKP5m7ZfanViePaOrDFAcy9HgmdwHBDE_uIDVEQyEqV-Fk4hpgWQirp8mEK4LT6pizX_xn5Y68zA-VvklQfkQrLpX17Oe3BfhKrzWOc0r-LwG_OBSs-LXfQ-yu2vWeQc2FuDfneVqJldXY1-pd6sx8vuNkj8qHf8w6qmraDL0MTvWmd6fYWNnJ2e__OJCWynPaTKYK52wVe9UODAnC8mWnRf6JaRlwPUFYValSy0RxyioI1qNTDjrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
100 میلیون توکن GLM-5.3-Flash با ثبت نام در AutoClaw + ZAI
از تاریخ 14 تا 16 سپتامبر (دوشنبه تا چهارشنبه) 600 میلیون توکن GLM-5.3 و DeepSeek 4.1 بدون نیاز به کارت و همچنین یک کد تخفیف ارائه خواهد شد.
این پیشنهاد در
اینجا
قابل دسترسی است (در حال حاضر شامل ۱۰۰ میلیون توکن می‌شود)
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7717" target="_blank">📅 14:46 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7716">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j4i-6lRiI8bCn_jme-fVewLj9sFLC4sDTi8PJWTva_yD6uY1nH8GHRMr1POaY2ehYWbN_TSdN-DnO2q_AvqCyB48LUOkQczCaHG0xcu2MbXxq4U-oVGHHGr117F7omjdEtPfRTQ9Z0fPJZWMgpH_F7a0utWBASrQsGK_DNR5JLOaFCFHPjCZLLkL4r4g4DuaD3ikojk3twFkTeSmTQidECSv_XwhnF8CTQzch62hCVH6dvyTAgtRtPe5OeKfGRjv5gTg65juEkgIZuVCrrELbiE_pVbUKn5t4lFr90KhhXMD2FBb7Bk_QiZ5wsSbT-eUuqDk8tOuIG_slzY7-8vWAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥁
کیبورد لپ‌تاپت رو به یه درامز حرفه‌ای تبدیل کن
پروژه خفن KeyBeat یه استودیوی درامز تحت وب هست که بدون نیاز به هیچ نصبی، مرورگرت رو به یه ساز واقعی تبدیل می‌کنه
🔥
یه پروژه اوپن‌سورس عالی برای برنامه‌نویس‌ها، آهنگسازها و عشقِ موزیکا
🔗
لینک سورس کد و اجرای مستقیم:
https://github.com/faithsaly5-stack/Keybeat
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7716" target="_blank">📅 12:45 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7715">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eVHJPGyIOpGe3q0oiJs5RRFShhlc80O5cmH4LMdpUnN_Ex57tW2uOZXOMmeWO8aBfY5TtSh3Q5rfUEkW1cY_oY9hvk4RW-2jJNqYi1GAfg6_WyjqrrZGFo3_d6Bdp3fU5Vp7iNJYxNnkRX_bmtSKNKrbIgW98BGE4b-ywCqa642kQoaIPL_mF1i3CL_z0ELT6HGcLzo5hozRnFc3KI9s703AdJCpYkgfK1qAcQXmgq500ns23F3_MRcvHF0KrNfxt6m87WLBLMRGBSTRT7yuVg3Ai1rudwhS_jhvy0ldV6m99ylL26tJN5STRhp4-Afk1NbeOV7HJktaFcEE5RxTYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
دریافت آیپی رزیندنتال رایگان
💎
با گوگلتون سایت زیر بشید و روی claim offer کلیک کنید.
بعدش برید بخش proxy generator و پرش کنید و بزنین براتون 300 مگ آیپی رزیدنتال میده
🆓
http://rainproxy.io
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7715" target="_blank">📅 10:21 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7712">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CbbZDeEKrhKaqObx0ZW1gES2oC0_M6LDtzQ5Y6FT_L3-caT981Jd94hrEVtEAMCDOhGdJ4gu1MdX0zJAjuTDNOvIeWpn6-4fxMfvJr8i2IB3fSVcFg6QX2d5Uktj-RSiuAE2iHHtvC40wCDnGNCMqpcNx0moWkVP9p2vLw5BoozdVwqEo30IPNvENDalMvwU5sdw8uGTP70Z5sILlzi8ajinG0jf4prv6HuePO7jxGnYnwxKfCsxcHXzXnABxSAGLINcnU2gmetEJctD7-WOLoe8oDTo51RM-qBfTz0RhkQwMjqs4CWwlAvBQPlt_rScHDMNvDd-sikmAM-xQxhs-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
15 دلار اعتبار رایگان برای دسترسی به بهترین مدل‌های هوش مصنوعی
استفاده از مرورگر به شما 15 دلار اعتبار می‌دهد تا مدل‌هایی مانند موارد زیر را امتحان کنید:
• GPT-6 Astra
• DeepSeek V4.1 Flash
• GPT-5.6 Luna
• Claude Opus 5
• Grok 4.5
برای دریافت:
🔗
browser-use.com
با استفاده از حساب گوگل خود ثبت نام کنید و شروع به استفاده کنید.
برای دریافت اعتبار بیشتر، از چندین حساب استفاده کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7712" target="_blank">📅 21:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7711">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🧰
جعبه‌ابزار همه‌کاره و فوق‌سریع تلگرام؛ معرفی آپدیت بزرگ بات Amir Tools!
بچه‌ها اگه کلافه شدید از اینکه برای هر کار کوچیک (هوش مصنوعی، استعلام قیمت ارز، دانلود یوتیوب و تبدیل فایل) یک ربات جداگانه استارت کنید، این بات همه‌کاره دقیقاً خوراکتونه. در آپدیت جدیدش کلی ابزار مدرن با رابط شیشه‌ای اضافه شده تا از ده‌ها بات متفرقه بی‌نیاز بشید.
🧠
هوش مصنوعی با حافظه اختصاصی:
مکالمه پیوسته بدون فراموشی کانتکست چت، سوئیچ خودکار روی مدل‌های پشتیبان و امکان ریست سشن
📥
فایل به لینک مستقیم و دانلودر یوتیوب:
تبدیل آنی انواع فایل، ویدیو، آهنگ و ویس به لینک مستقیم پرسرعت + دانلود مدیا از یوتیوب با بالاترین کیفیت
📈
نرخ لحظه‌ای و چارت زنده بازار:
استعلام آنی قیمت دلار، تتر و ارزهای دیجیتال (BTC, ETH, TON و...) همراه با نمودار اختصاصی و باکس High & Low
🤫
پیام ناشناس امن و دوطرفه:
ساخت لینک اختصاصی با آیدی تصادفی برای دریافت متن، ویس و عکس ناشناس با قابلیت پاسخ‌گویی مستقیم
🎁
سیستم قرعه‌کشی خودکار کانال:
ساخت مسابقات و چالش‌های گروهی با دکمه شیشه‌ای و قرعه‌کشی کاملاً خودکار و عادلانه بین اعضا
🛠
میکروابزارهای روزمره:
ساخت بارکد تصویری (QR Code)، پسوردساز غیرقابل‌نفوذ، مبدل ارز به تومان، هواشناسی و مینی‌گیم‌های کوئیز
💡
نحوه استفاده:
وارد ربات بشید، دکمه شیشه‌ای منو رو لمس کنید و بدون نیاز به رجیستر یا مراحل طولانی، به تمامی ابزارها به‌صورت یکپارچه و رایگان دسترسی پیدا کنید.
🔗
استارت ربات هوشمند
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7711" target="_blank">📅 20:52 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7710">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚀
دسترسی رایگان به Claude Fable 5 از طریق GitLab!
💻
✨
اگر می‌خواهید به صورت کاملاً رایگان از قدرت مدل هوش مصنوعی Claude برای برنامه‌نویسی، ساخت سیستم‌ها و توسعه پروژه‌های بلندمدت استفاده کنید، گیت‌لب (GitLab) یک فرصت بی‌نظیر ۳۰ روزه برای شما فراهم کرده است.…</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7710" target="_blank">📅 19:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7708">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">😎
دسترسی رایگان به GPT-Image-2.5 Sunburst به مدت 72 ساعت
📝
مراحل: ① به https://arena.ai/ مراجعه کنید. ② حالت Direct Mode را انتخاب کنید. ③ در لیست مدل‌ها، GPT-Image-2.5 Sunburst را پیدا کنید. ④ به مدت 72 ساعت، این مدل به صورت رایگان در دسترس خواهد بود.
✈️
…</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7708" target="_blank">📅 14:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7707">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">175 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | GPT 5.6 Sol | GLM 5.3 | Opus 4.8 | Deepseek V4 Flash
✅
برای فعال‌سازی فقط کافیه یک اکانت گیت‌هاب قدیمی داشته باشید و از طریق این لینک وارد شید
✅
🎁
با هر رفرال شما 100 دلار و شخص دریافت کننده…</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7707" target="_blank">📅 12:01 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7706">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ix_bgfRrgSWWjiPNaENpGuqtxYdULYi-6mgw0uKnF_TMbmlwv2OU4MBsxXUeN4VeUVZNuRnH5eGKGseddN3NAT3wk00m7GkmNMBgTppDbWMUao-GIVE0jPD2kIL3SuJM2fBQ_Xrewu3tNM8M_9BiNhzFp6o3ERRefcKHBaGmKw0RPUMGl4kk__ZM5mkINzcfEC6wLR4nWTixE9mezXIBcoad55hjcg6IbNzlDrsh6RTVUUkSQ5Q20X7RLrM08qxPul-lp2lIMQjX-xw3Lj6FmlS4CZprXyfZ8KrI1ufOkDWV8QYRM1wKT-Mkx6fwuW-sp8M95NmayRUBYqK5MiIzPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
دسترسی رایگان به GPT-Image-2.5 Sunburst به مدت 72 ساعت
📝
مراحل:
① به
https://arena.ai/
مراجعه کنید.
② حالت
Direct Mode
را انتخاب کنید.
③ در لیست مدل‌ها،
GPT-Image-2.5 Sunburst
را پیدا کنید.
④ به مدت
72 ساعت، این مدل به صورت رایگان در دسترس خواهد بود
.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/ArchiveTell/7706" target="_blank">📅 21:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7705">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sl5tYElBYYdKxaOuIdq7AipuwFz62tO8xg3srXB_JtIWMUqHcRPH1TBTb4FI1HfIwuXuPmoFMVFuJlImQv88Kg1c43rJU9_hw2kQJQAC9rxoQQOedf38WH0jZI6D0uzfCeg891dwnfvV9CWEfcW64ujJ4H54v7j_adHuCxKOX2WUAYSuHh1MFScv7KN5240QdpAHdqpbf52OYwsgoKSMyAhMUR4nU3P5llBi2dXXxyCrbg0_djw1G6qKSpfE9NR_qgcUGKYlPy6HDQgJtZHmmT6up3nvcnkc1zmlnNzxp1k1Hyk6mxMbafJe-eKaTa18FCmjythPdfGYE1d9j2kHHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل DeepSeek V4.1 Flash به صورت رایگان
💥
🆓
این نسخه ۲ روز پیش منتشر شده است. دارای ۱ میلیون توکن متن، قابلیت‌های بصری پیشرفته و کیفیت مناسب برای استفاده در سیستم‌های هوشمند است.
🚀
🔺
رایگان به صورت روزانه
🔺
پنجره متن با ظرفیت ۱ میلیون توکن
🔺
سهم استفاده روزانه هر روز ریست می‌شود.
هنوز مشخص نیست که این سرویس چه مدت به صورت رایگان باقی خواهد ماند.
‼️
🔗
لینک سایت
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/ArchiveTell/7705" target="_blank">📅 15:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7704">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mBeIJgQxckJygHVkN9NH12wmjoEAO0QLzq5gmHK74q0wR9fdMDVcsPETo5iOR_SdCnJ7zoNhWTRKTBhP3mG67c-v2Eq77JvhOyldwvakm8iW8lLHL958NU0JNnpfbcWVw0t2yQodfI0IIkCc6Cu0VceRe4FZwY-iSQaWdr-8ByF5bORanrbD94DiSPmvGPfgooMmIgRUi-eH0Dq7SZuCIU2jce730RmA4-bGko3Kdkuc2l0AFrS9RQJVhKEMSfFiLvr_4XpOocbXBvcVvKa80C4kVwbT9eksD-5fJMkRS2JTiRjJ5m6Kb_zm4Gff0zJWuMpIGzIYTvN5dTbIwN_kng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی به غول های هوش منصوعی به صورت رایگان
💥
🆓
با این سایت میتونید 5 دلار اعتبار رایگان برای بهترین مدل ها دریافت کنید همچنین این سایت 3 مدل کاملا رایگان بهتون میده
💵
😎
Kimi K3 | Deepseek 4 Flash | Mimo 2.5
✅
📌
Base URL: https://tokenharbor.ai/v1  با جیمیل…</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7704" target="_blank">📅 11:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7702">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AaFWePVC2FYPuf_JJ1G24pHbUVtSGVPnhtDS75CrgWH1aQC4u3jKzO7Yt0Eu3qfQOkl5xCyiCM3ACWRA3hBYx28l8gutnW_Q5JS4bqskyZr-xpl9yuq_RboTnnP5DrGLqC1m4s9bDKVtzHG5CFyQlPVzI9vXC9KOT5ZsFt7CZnQZ6yKan2zUBTsogthOl4pOBJOqdOdcNuLxN3eedIqvF0sGE7HkT3pQq7zrdTCWjUj1lT5VfbqMAgK0CvlcUvgchFHibn9u7AOkHdfGhJDA0gZNymKds4Br3Tx9hrL5a2tGSolKgahVqaIE-znK9R9CV-zVNRDprVe7Fx57LkRz0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">GPT-6 Astra
1 Day Free
⚡️
⚡️
https://arena.ai/text/direct?model_a=gpt-6-astra-medium
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/ArchiveTell/7702" target="_blank">📅 19:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7701">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a6fuq-Etq-Ea1JneobYe95tS5eN_l5I1GUdsEFHd6GntONFlmHhRYuzrHrDih21bOSModmsquInlE4Qhqic23KG3EFadmUaaCjxDDXzpZt1ihn24bcvWdV1p3oNg55gLbjpF2X5ZTIBDaej0qij0emTG1soktcJYl7h8dvY277SQaNmcerY775IWvrILaWYgP0WxkYsFBn_BKWM72A6xAEbHFm9Bxw2rP25GGWYI9Gmr3-C7Y6fY0QEdC7u62xGzt6hHMljdg0cy6Mvssby8W_16ioiIXPiQAT9SvXFrIrY6Of9xj0dDUC9EkHMOqXghaMIGwRP5FJZaiC7X_l4oCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">150 میلیون توکن رایگان برای مدل های زیر
💥
🆓
GLM 5.3 Flash | Qwen 3.8 Flash | Mimo 2.5 | GLM 5.3 | Hy 3 | Qwen3.8 27b
✅
وارد سایت زیر بشید با جیمیل ثبت نام کنید سپس از طریق منو 50 میلیون توکن امروز هم دریافت کنید
✅
‼️
نکته :
از مدل های با پسوند Free استفاده کنید و احتمالا این دسترسی شامل محدودیت تعداد ریکوئست در دقیقه باشه ، همچنین ممکن هست هر لحظه اشتراک رایگان بپره
📌
Base URL :
https://kiraai.vn/api/v1
🔗
لینک ثبت نام
🔗
لینک گرفتن کلید
🔗
لینک دیدن مدل ها
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7701" target="_blank">📅 18:42 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7700">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🧠
پروژه OXYGPT — یه ربات تلگرامی که هوش مصنوعی رو حسابی جدی گرفته!
بچه‌ها این صرفاً یه ربات چت نیست، یه اکوسیستم کامل AI روی تلگرامه: چند مدل هوش مصنوعی، مربی‌های حرفه‌ای تریدینگ، sandbox واقعی لینوکس، اخبار فارکس زنده و داشبورد مدیریتی. خوراک کسایی که می‌خوان یه بات production-grade بسازن نه یه دمو دو ساعته
🔥
↔
مسیریابی چند-مدلی AI
: استخر کلید Gemini + سرویس‌های سازگار با OpenAI، round-robin می‌چرخن و روی خطای 429/503 خودشون فالبک می‌زنن
🪟
پنجره‌های مکالمه مجزا
: هر کاربر تا ۵ چت جدا با تاریخچه و state خودش می‌تونه باز نگه‌داره
🧙‍♂️
مربی‌های تریدینگ (Persona)
: چهار شخصیت آماده (ICT، Quarterly Theory، Matrix/369، Price Action) با یه دستور سریع صدا زده می‌شن
📓
ژورنال معاملات
: ثبت و پیگیری ترید‌ها با قالب‌های اختصاصی، مستقیم داخل تلگرام
📰
اخبار فارکس زنده
: رویدادهای پرتأثیر Forex Factory رو با تحلیل کوتاه AI نشون میده
🖥️
قابلیت Sandbox واقعی لینوکس (E2B)
: مدل می‌تونه کد اجرا کنه، پکیج نصب کنه، ریپو کلون کنه و فایل بفرسته/بگیره
🔑
قابلیت BYOK
: کلید API خودتو وصل کن، از محدودیت پیام و quota عمومی بی‌نیاز شو
👁
مانیتورینگ کانال با AI
: کانال‌های تلگرام رو زیر نظر می‌گیره و پست‌های مهم رو تحلیل و تحویل میده
💡
دیپلوی با یه دستور روی Docker/Railway انجام میشه، و هر ۵ ساعت یه بک‌آپ خودکار از کل دیتابیس‌ها زیپ و برات تو تلگرام ارسال میشه — دیگه نگران از دست رفتن دیتا نباش.
🔗
گیت‌هاب پروژه
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7700" target="_blank">📅 17:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7698">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7698" target="_blank">📅 17:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7697">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/up_Q7JX-x0uOrrdoRE8LVyWAH559w_sViwIl8-uUgXNcmRh95EJ5MMkyRt7Jpy5eqHI8Mt2B4clayObG1QQEuLaIiQZZHYByD_FJPmBMVG1ybq-g_B92BvYSui0MEE-tc9b8prXfmE3kLYkqfyMxdBTQmZkQdozK9-rD5TrsmD0l9kfnRiv5rCFG6c-nl1UCeEr1Zje1e-lFCOeXE5ShKoP0qm-A9OYgP_zhtY1ChVVK2Y_ARLhW96K4ZKVJcoMvIIf5Nro5tllW1NHbYOSFSj4GPdcOgNM0RCVS4pKofFcr5xUAgR3QUfkDUo-wiZ5trFysWz4SGliHtMHg8Lxy6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 میلیون اعتبار رایگان برای بهترین مدل های هوش مصنوعی
🚀
Opus 5 | GPT 5.6 sol | Sonnet 5 | Kimi k3 | Gemini 3.5 | Opus 4.8 | Grok 4.20 | Gemini 3.1 pro  همچنین دارای چند مدل رایگان :  GLM 5.2 | Deepseek 4 Flash 0731
🤖
|Minimax M3   به این سایت برید یک حساب…</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7697" target="_blank">📅 16:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7696">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚀
دسترسی به بهترین مدل‌های هوش مصنوعی به صورت رایگان    Mimo 2.5 Pro | Deepseek 4 Pro | Minimax m2.7 | Mistral Small 4 | Mistral Large 3 | Mistral Medium 3.5
✅
برای فعال‌سازی فقط کافیه یک ایمیل داشته باشید و از طریق لبنو زیر وارد شید و سپس لینک ربات تلگرامی…</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7696" target="_blank">📅 16:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7695">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jPhP6eWhWFOVbh-GoCrhECrDtj1RSKmUcB0UUkPqukgOamTG5-SZGR0I_RFNUOMVljM369DH4oitRzEPlmU96Lai1n4K_RpvrFRZN84SDrckIXEiXJzgPvWse6TsbGfJu3h5vUfKrUhAKTjK0JzbJPuU-MosS8SiJGXOd58j5ZKnTuCh1szZbfum8nv9w7x4ntluYqqQTcp5izmEOe0gdZ5X2o0KjvnBzjOSphxlUWPPK-KNC3eLRsOmA9w45GFEcKXKIvI6NLtaVYcw8FvGui-HTYTUJeUVgLIGvZgYwrjlVJz1_UPBQUXJjr03ox4q_McX7HZQbDu21ONxlQZHVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزانه 1 میلیون توکن رایگان برای مدل‌های زیر
💥
🆓
Gemini 3.8 flash | Muse Spark 1.3 |GLM 5.3 Flash | Deepseek V4 Flash | Deepseek V4 Pro | GPT 5.6 Luna | Gemini 3.1 pro
✅
وارد سایت زیر بشید و ثبت نام کنید و یک کلید دریافت کنید
✅
‼️
نکته :
با هر آیپی ۱ بار میشه ثبت نام کرد اگه میخواید چند اکانت بسازید هربار آیپی هارو تعویض کنید
📌
Base URL :
https://apinex.bond/v1
🔗
لینک سایت
🔗
گرفتن کلید
🔗
دیدن مدل ها
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7695" target="_blank">📅 15:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7694">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m_8UiatidEDOO-GotpP2LtJRlW3meu_AVWpoQygNDOO21wXaLCkipB8LzuE7hMQVin0II2ZoUcOv8zO7_dwf5CwXapHiZvwZL5hXpdCeUjfinLUFE9890rPW6baIVM418UeB9wMJ3dlVsnUDsMV3KUsRliILNy0u2XKUfsbeU6X7n0_K2vOy-n_RuEJe8RuUMciLVNmTfoNCNgN_tk21ssDCEoAX9biIiOgKuMugELA7bNfcyC86Qe3CB6ii5smqDHd1uhBGo71W09af8xsnyhRMBJdDrRtzaYXsXdcBKVl7B8JSMVeNhTy2aIO3ZXc3mDFn8F-N-KpclQ67UElBeQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7694" target="_blank">📅 14:52 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7692">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R7fWYFgDL02yJ3F0gnKwrM6ZLRecc4sw7DwierRHautiwwqKgx00DpROYqVlfdvly_C-aVpQdG8dX89C_SfjRWE9C_1dBBt54Hrui4QbLUZpNClCtlxIdGDoTdsW1LXMOCkDMpYWxxCzuFmaL_iDDTluFmnJe-ntOkH_stfJGaSOJG8xfgEkBFZFlvt5QwRx1F_Rlc7UHhtuzZhfs1XYeE_-Z4eqVHxhI4jEgxlLR3UYOU6YrMhpfyyGD8K_JKuljdgaQgx4Um9aHXuYDmbJEqRuj2qaNUbCuCyz-LoJyumthwM7C15fJdgyzxV6LaWFCt3vlDNIuSYyjt4KXhw7_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">DEEPSEEK V4.1 رایگان
🙂‍↕️
🔗
alysiscode.com
✅
50 کردیت در هر 30 روز
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7692" target="_blank">📅 11:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7691">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🎨
غوغای جدید اوپن‌ای‌آی؛ مدل ChatGPT Images 2.5 منتشر شد!
⚡️
۵۰٪ سریع‌تر با جزئیات خیره‌کننده: جهش بزرگ در نمایش طبیعی بافت‌ها، شکست نور و واقع‌گرایی رنگ‌ها در نصف زمان قبل
✏️
قابلیت جادویی Sketch: کشیدن طرح اولیه و ترکیب‌بندی به‌صورت دستی، تا هوش مصنوعی…</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7691" target="_blank">📅 00:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7690">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7690" target="_blank">📅 23:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7689">
<div class="tg-post-header">📌 پیام #16</div>
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
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7689" target="_blank">📅 23:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7688">
<div class="tg-post-header">📌 پیام #15</div>
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
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7688" target="_blank">📅 22:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7687">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9374b9e092.mp4?token=F5vBv9gLIXE8ZV1yOAPiZ0iDs-RxstegTeZteC62Adqkoc0pTKfIE10kEpQyUM4kLwDwgcU2Xvzveowa6WVmwQh51qh_miml41Ho5oeaijipNQfHKSULqBQp7Pi6nOxSyWxaGLgFGvEziKbtH0DzKm43hOU319Vu8hzMnBiwBGRcbWk5EsoAnAohzTU0FwpRZ7bdtcDVLlD0F_6dXh6WpcX4ajpEIBOgnFd3a2d7yrO7NQ1AobBV8x7gKE4F1CHA3jYBumdgxtcM00gid_rX4E6iG9bQkxX8RcHxz56XQ-p99FPHQ3ovLdLlY5s-AfghrZpCplQ-dkRe68P2NoF6nCX5x8N3jxDAM12fyC56lsQ6TdT19wh1Jb07ldCLVUtNHbMHILIi1WSsrQh8S6qCRLuw688sQZW-QKbFJ9UwlWVUYR0lt0vnn4HFGVdgFWtLEE3QkXw28n5MFIWpMZMlSTASBcz4Tj2RFbF7TM0wnwjqP-ACEKCjlvU0ayuwl-SkJKu51xSvUf92mm53ny5EhtyHx_QVzUJimoxcl0UUtViNi4jjlYm5NEMKU8Am8X7nBK-2Etf26OtmSKnRAw_IySAZJgCz_aYAKiTaqY2XwwdaVr5TqhXFM_D51gVU3nvXQk9Ym0XjLiyMykDaZBCHM2M-idUj1qXN9C7wI18TvVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9374b9e092.mp4?token=F5vBv9gLIXE8ZV1yOAPiZ0iDs-RxstegTeZteC62Adqkoc0pTKfIE10kEpQyUM4kLwDwgcU2Xvzveowa6WVmwQh51qh_miml41Ho5oeaijipNQfHKSULqBQp7Pi6nOxSyWxaGLgFGvEziKbtH0DzKm43hOU319Vu8hzMnBiwBGRcbWk5EsoAnAohzTU0FwpRZ7bdtcDVLlD0F_6dXh6WpcX4ajpEIBOgnFd3a2d7yrO7NQ1AobBV8x7gKE4F1CHA3jYBumdgxtcM00gid_rX4E6iG9bQkxX8RcHxz56XQ-p99FPHQ3ovLdLlY5s-AfghrZpCplQ-dkRe68P2NoF6nCX5x8N3jxDAM12fyC56lsQ6TdT19wh1Jb07ldCLVUtNHbMHILIi1WSsrQh8S6qCRLuw688sQZW-QKbFJ9UwlWVUYR0lt0vnn4HFGVdgFWtLEE3QkXw28n5MFIWpMZMlSTASBcz4Tj2RFbF7TM0wnwjqP-ACEKCjlvU0ayuwl-SkJKu51xSvUf92mm53ny5EhtyHx_QVzUJimoxcl0UUtViNi4jjlYm5NEMKU8Am8X7nBK-2Etf26OtmSKnRAw_IySAZJgCz_aYAKiTaqY2XwwdaVr5TqhXFM_D51gVU3nvXQk9Ym0XjLiyMykDaZBCHM2M-idUj1qXN9C7wI18TvVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7687" target="_blank">📅 22:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7686">
<div class="tg-post-header">📌 پیام #13</div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7686" target="_blank">📅 16:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7685">
<div class="tg-post-header">📌 پیام #12</div>
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
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7685" target="_blank">📅 16:23 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7684">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fc89182f1.mp4?token=CIqB576HHZscn33JsiMnm-hOqtxOcz208hWv3U5oxcEESWJhFiblHWqux0pZgIqo8J9E3GQtmzL2c5ylaSKkN4-K5p1QJGZmXt2oebznhc4yHe1oSTJJnTyTVs7Y__AjLBBwcgRoHbN5NBYtbKUI0amVKXIAgC8azS-Xgere1IRF2b0e2axcmVPBiG8Be1rRfm-GWCyb20wzc1RHDpa4DA1p4ON2VvH3QAs5yCbSnnNujBpuogQILnucb8i8iZaE7BHAUldvGUNmyuXdvVI0wtfGt8uk39wEydBCIATT0gutRKaGRp5z2BhbfF5j8tM2HiHQXhV97klSfquwV3vFyTUVSe4_UKdl1m0GHdGtCI7T-WuMjDiwSmMj2ZUFV2CBeB3av510FiplKph8H3JqzJI2_Tv-WeXNR89bj3gvu2A1TzOlfrm1D5ZDy-svnT2vzGjF5WAvwqznppUAGWnZNGLNI9TzP0D5Aw7k2SzJfH9gzPsG5oGGYRgPY7APX3R8LdFgRiY-bA9Akf8TSdiJ9zeoVLDbrGwtT1iarXP9xMqlzYwhzZRAu8UCENJP2HG8-VGZIA_d8v5BafpuqzbluFTgs6OiwJyzq0jmSaM7SmCPyuoS0maV7je1rf4J8wZ6J_X_kcVFAqNlIGUHjz0tlKzGOdQ1cDpIrTIK1l7vFIU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fc89182f1.mp4?token=CIqB576HHZscn33JsiMnm-hOqtxOcz208hWv3U5oxcEESWJhFiblHWqux0pZgIqo8J9E3GQtmzL2c5ylaSKkN4-K5p1QJGZmXt2oebznhc4yHe1oSTJJnTyTVs7Y__AjLBBwcgRoHbN5NBYtbKUI0amVKXIAgC8azS-Xgere1IRF2b0e2axcmVPBiG8Be1rRfm-GWCyb20wzc1RHDpa4DA1p4ON2VvH3QAs5yCbSnnNujBpuogQILnucb8i8iZaE7BHAUldvGUNmyuXdvVI0wtfGt8uk39wEydBCIATT0gutRKaGRp5z2BhbfF5j8tM2HiHQXhV97klSfquwV3vFyTUVSe4_UKdl1m0GHdGtCI7T-WuMjDiwSmMj2ZUFV2CBeB3av510FiplKph8H3JqzJI2_Tv-WeXNR89bj3gvu2A1TzOlfrm1D5ZDy-svnT2vzGjF5WAvwqznppUAGWnZNGLNI9TzP0D5Aw7k2SzJfH9gzPsG5oGGYRgPY7APX3R8LdFgRiY-bA9Akf8TSdiJ9zeoVLDbrGwtT1iarXP9xMqlzYwhzZRAu8UCENJP2HG8-VGZIA_d8v5BafpuqzbluFTgs6OiwJyzq0jmSaM7SmCPyuoS0maV7je1rf4J8wZ6J_X_kcVFAqNlIGUHjz0tlKzGOdQ1cDpIrTIK1l7vFIU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/7684" target="_blank">📅 15:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7683">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQdh2iWbGLdgyjb1QjItTLNIwsFPq1_VlXhTFINXF-YSv5oBsq11N8_-yOpB_CW7V0nQobiS8sVvp7vIaaEI2eSATeAalSo4V2nQQLY0ZUNVm5PXbpGAscnr9SOPB7sgs0E5_8IKdLGr8rxlmC5Q7k5MTGptlT_KrCTPvJ-Z8D63CA5sAZK1w856uycysWlRA_NHBMPBcWurLk2Qx731D5qZ-7EcMPpXVuaXqXvH3sP0g5hwivCzGkjXGzOQ8fK57snkbT2xX1_V7_rtpSFSEJZ5I6cO0MpNwrJVBVCwtEnUp9nBrgD8iGIxSrfJv1fb756UvpqgR-jkhtoAYHAMJw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7683" target="_blank">📅 14:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7682">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e226c05d7f.mp4?token=A4C8ZPBYTDvutLAfsBwIapcVygOWjjyKacT__wlrZ7UW5RBn91mI0FvqqDVizb5BxVprq9aHlvrZI1ijAwQm7A3aCVyW7X-kikwk4DSwn7B8Bl4IZfE51A6OYjHYvg71E1O5K6RlgLFwUzbcqj03HXrA0ALlnw2Bof2itUIxqSI6X-gVIt5BX873DjGVpaYQUs-wVPCOdgrrzlszF0j7wq1pVxbDT6-hFh63eWyM4Fei4vQ91SdLV8D5nqLwNIk8OxfKcxEIIsUE7u2mEo-sjAdHcgFv1aheBdY8YB7AFEvcroMrU7b7wJ03OEId-ROs8JYRxKzr6LdrTe_3raknmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e226c05d7f.mp4?token=A4C8ZPBYTDvutLAfsBwIapcVygOWjjyKacT__wlrZ7UW5RBn91mI0FvqqDVizb5BxVprq9aHlvrZI1ijAwQm7A3aCVyW7X-kikwk4DSwn7B8Bl4IZfE51A6OYjHYvg71E1O5K6RlgLFwUzbcqj03HXrA0ALlnw2Bof2itUIxqSI6X-gVIt5BX873DjGVpaYQUs-wVPCOdgrrzlszF0j7wq1pVxbDT6-hFh63eWyM4Fei4vQ91SdLV8D5nqLwNIk8OxfKcxEIIsUE7u2mEo-sjAdHcgFv1aheBdY8YB7AFEvcroMrU7b7wJ03OEId-ROs8JYRxKzr6LdrTe_3raknmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/7682" target="_blank">📅 14:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7681">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N_OqiCR8icmoNZpp3REokgE-F8KC7j2pSdW_B3XcPDgZTRn0hxGlLBiVAlFO6UCG5vpbL6h6TV7BM7BZribw3anJgg96ZfY9lgRYghI3BoDYXsr4uHt9JofDNEX772NbIjlV7wp5JsCrYdybLDJ2Vd5GOZoN1Y9jqI9sRPfwGxWhybDqUuQZx0tQCfQKEn4rhav-BC071RGNxW29hg8rKmLHg3QkFzR85gxfRtSmHXkRcwj4OA3OEs_Lu5z7t8yI3lXWZ3_uytd8nOEgLF63kl-PwruFMl6M-DSz37pZNXx8DdhUhtHTfUMsMwMv9zNqacArGxhSedDBfbiqlkaUQg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/7681" target="_blank">📅 13:49 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7680">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c846b7bad.mp4?token=VmPihM8_8cajdeTwvAmqz_O181GgwDXckvuV92l2du3ioYevlCXlRZJevGzaUjw4SE8rerMaz3575_owRdf6fhzaHyWR9th5peUh3xEtGDM6iOjBiFjiaWJqtDrmwTiIbZmwe4h5600202iBQ2ulNeA6odvhtpDs4Xa2twdt9G6Toc7p_UKMZtt9MMe2sCu7ipd3SHHMN6NmwcLNA01Sfl5nNF18hYz1EfShaKJhCcSFfXnEJthZGD52gkIJ20WGwstkOtCa4_LFY-GMffk4asizXDnBQsi-KizCepJAACSsAtrjcVmIcr21iFVx6rhLzc53KgTGyxTWnmefwCBw9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c846b7bad.mp4?token=VmPihM8_8cajdeTwvAmqz_O181GgwDXckvuV92l2du3ioYevlCXlRZJevGzaUjw4SE8rerMaz3575_owRdf6fhzaHyWR9th5peUh3xEtGDM6iOjBiFjiaWJqtDrmwTiIbZmwe4h5600202iBQ2ulNeA6odvhtpDs4Xa2twdt9G6Toc7p_UKMZtt9MMe2sCu7ipd3SHHMN6NmwcLNA01Sfl5nNF18hYz1EfShaKJhCcSFfXnEJthZGD52gkIJ20WGwstkOtCa4_LFY-GMffk4asizXDnBQsi-KizCepJAACSsAtrjcVmIcr21iFVx6rhLzc53KgTGyxTWnmefwCBw9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/7680" target="_blank">📅 13:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7679">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l3FtN3atlIXoxmSUUdPv4X5rB2NZ8qSaCpm4EVJNVW4gDOorRRaT2CB25b6J7PMIfvU8uy2WismY-I9lbKblXUor0Y_f1iHYDsU5ohUxp_QDQDb1txHXRc2vPyMcRs4Utq8JhIjMkUjtOlOOAYD3d8OvyDyknK6OdAE2AxjhBy1p7t3rBf0DHj6BdfhGH_KXZxAublGTWTRRUY_b77rklTnmmxgb2PlRM-SY7c1n1YooUiirPonFcaE9jFG-NHkow_mC91qPa4iKpy99wDc-T3tnSSvWotdPl6N-xkWO35ICm_bMWPTnjaKKH79N6ZBcfj48sAa8ocZWCVOZ9THVQw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7679" target="_blank">📅 13:33 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7678">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jcrzyjTngUQdQf_LS9UYpWtCOVJwaph9x18mb3rjOPkiAwnDjPKeArdmr8yZ5BDJwUwMvbXhX257CTOcXBj3IkbNlmW60tDiJYKEz1lAKehjH4YgZ5rMHhAMn4KY2Yo_feyrnYR-en2QbtqA9ymYe9PyZI0ziyfINN7Q_-tIxvMrgiiVtkRgptR9hE8xWL2lYAZH5lus_M8iZDzaxnEuoAmbfZ1CZFgcEza_NiYhSmM_iulWSRtsX-iJ9GGKF7KcoqgI-eNMljniJ0qmO05xFd84ReKV_VXWJVt-s0S2DwHwnAXX-Qhbdlhl0DpB_RZC_SOzbRW6T7alfUU3OA85gw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7678" target="_blank">📅 09:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7677">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ArchiveTel
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/7677" target="_blank">📅 00:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7676">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mSz3IY4hUsVW-P0PRIQ-xQcwgZhDVr0xoiwnOGsQfGVwg7WoaiN7loNxr7UWYM5MxToB_NRxL5Hxdn4S-aKshIgvBaasZPfFYm9jGrCtTPKstfedJVrTRJrxLjOlqY87T7JRBgz7Ow6rwdzLrQtQdSfXMasdKfheI8K8Oy64N4I6I4dXxtBl7zoaDLSLAbrhxnc_kjg7LzsMOoX4MGtyaq2USdN1LUr0_LjkGmtkf0MZ-6tEFFxRioPMDRkxoNYhbxUJhMSIyjfefsVGASnTcrLV44F7uAvHgy4gHULIQzx8rAUuF1NHg3rHyA0etnn99VsXdqgIY5W80ZaDhMI7lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت
یا کاملا رایگان باشه یا فریمیوم
با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم
اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7676" target="_blank">📅 00:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7673">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/piLSCnbZW9ojEvB90TKijANzQZAOXNz5txL3mFfCaSoeCbOG99HXFM5RrxRORuRvumH1UsWiuogRP49D2HtCDfvJguykGlYs8eJkrW2UyWkNhuklcgpKs-ox_60PWClOnCxBPOcD3AK71M3DfHp9FMBZxwrnh8SaFqj_H4nxkJwUWqoCRqjPPmXlWhRknM5AmfmjHyTM-pq4X6ID4uEZQ2PLF3dblOfNVTYsQS-IF_WK8rKrUqo9AtwggvyQuSAkGzYmT9LGaSHUaham5Csk8IXogqsDCY5a92Yqun3LS5ahWcqi9O-Kh5IDIVpX7_tOyLyL02LI2J0IfIfT0cKrdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a1_QJ-H7VF78u3APtnY-_8-0MQ7qk8ldWpj8E7RiGIS9oxWuqkACe5JBHYjnUi0xX_wP-EAC9Hin1jkwwVyrGMe66Fvh-jabndBsJWm8uX6qfCglgZWy56Ql2OoiNLTKbDOPRP2__aDlVzYHtMmxxEFUMRcUDd7evcNnoSfyIj3OnkaYpBSbaqUF9EH7xO0NHowqoqXNaccf9Ddblm0-xjmGb7WpOlEqlIKHhIoxROlsH3FOR5AHvSrtxMIBdNNkvdLmMEPooG5MklcmTYmTiB6OxXWKDgrG64mt6pEBkdXuvYHLYxdKRBoY1s8IQ1bJ3R_BbLU11d5W8rfqPyMQNw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7673" target="_blank">📅 23:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7672">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GycNwD651L-Bgk7ZuNZNTvXgT7TChpotLutLL7JHCddq8RDy4icCnTqJJcsDoz-ShKOdyQgJHN1XJ_pE5QtpNlp2ZpwfhOP_iBGUlhGzFQUNy6F6BJQfBMfj6t32Xrc0qXD09DW1Ea58t0cwV-qwtPgJubthnHu_Tdav_YOevBpCwgI_v326OJlCkkbqH7m6GFqgbXg4Z_RVsN5A_MhxoRkZmHnOE-6V57twham3tsG3h3_7mc-ygklntxGxN794J_MAGhVzuB02ETMTkqM6HUPzWmVEKs8uYG26Le1y_Q0WcMGXSP0CaJBh3xS-DY3xx2dGXh5FD2tRrbSelhm0uw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7672" target="_blank">📅 23:22 · 16 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
