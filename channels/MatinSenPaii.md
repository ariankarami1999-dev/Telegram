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
<img src="https://cdn1.telesco.pe/file/iJGRUo8UodtOG0uSs40uPHuuESwi33zZducNjZtmhHsZeV7V8AqbNHaxdsQ7S4AzGN1i5qeTsNPthZr0fgRUQQ40eYDibdRyKZ119s6kwX32hI6JZf7npxNI9k6tgXwC1SbwXlvb7fpDZ3rSLW36zPQUqirKi-95sFnqvr1J8_5r7U6t93-NZPVfyJFn56rV_NVMLHyZ233LBy8hlKDiJDmlpj6oCOgZr-PBcVtORHQ9YLigrYHCrXp6e_KEyZbfhGSL3r6iE2l2hGee0V8PVh3z_xYZnFbblAXwpdKz1AOt6JiGLuq30zj10rGIy9YoAd8xZOttxHRCnno364l9jw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 158K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPaiایمیل کاری: matinsp.job@gmail.com</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-18 12:21:09</div>
<hr>

<div class="tg-post" id="msg-4332">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اگر می‌خواید اکانت Claude بخرید، بهتره بدونید علت بن کردن‌های کلاد distillation attack هایی هست که اخیرا بهش شده؛ و حتی کاربرهای خارجی هم یهو اکانتاشون بن شده. بهتون دوتا توصیه می‌کنم.
1- به هیچ وجه از سایت‌های ایرانی نخرید. و حتما بدید دوستی، آشنایی، چیزی بگیره از خارج کشور. اگر ندارید، برید سراغ توصیه‌ی دوم. احتمال بن شدن داره به هر حال و ریسکش پای خودتونه. من خودم به شخصه هنوز بن نشدم(نمیدونم شانسه، یا چون دوستم از خارج از کشور واسم گرفت)
2- اشتراک Codex بگیرید در عوض و یا نهایتا اگر کار خیلی واجب دارید و می‌خواید حتما کلاد باشه، cursor بگیرید اما کرسر خیلی زود تموم میشه طبق تجربه‌ی شخصی. به نظرم Codex سخاوتمندانه‌تره به شدت. و صبر کنید تا وقتی که بن شدناشون شدتش کمتر بشه.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/MatinSenPaii/4332" target="_blank">📅 21:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4331">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">نشت مخفیانه‌ی دیتا از ریپازیتوری‌های پرایوت گیت‌هاب با یه ترفند ساده‌ی هوش مصنوعی
📚
فکر کنید یه نفر بدون هیچ پسورد و دسترسی‌ای، بتونه کدهای مخفیانه‌تون رو توی گیت‌هاب بخونه. چطوری؟ با گول زدن ایجنت هوش مصنوعیِ خود گیت‌هاب!
تیم Noma Labs یه آسیب‌پذیری خیلی خطرناک (به اسم GitLost) توی سیستم جدید Agentic Workflows گیت‌هاب پیدا کرده. داستان از این قراره که این ایجنت‌ها می‌تونن issueها رو بخونن و اتوماسیون انجام بدن.
🫵
حالا هکرها چیکار می‌تونن بکنن؟
هکر کافیه بیاد تو یکی از ریپازیتوری‌های پابلیک شما یه Issue باز کنه و توش یه سری دستور مخفیانه به زبان انگلیسی (Prompt Injection) قایم کنه.
ایجنت گیت‌هاب این متن رو می‌خونه، گول می‌خوره و به جای کار اصلیش، میره فایل‌ها و دیتای ریپازیتوری‌های پرایوتِ همون سازمان رو می‌خونه و برای هکر می‌فرسته!
نکته‌ی جالب اینجاست:
گیت‌هاب کلی گاردریل امنیتی چیده بود که دقیقاً جلوی همین اتفاق رو بگیره. اما محقق‌ها فهمیدن فقط با اضافه کردن کلمه‌ی "Additionally" (به‌علاوه/همچنین) توی پرامپت هک، مدل هوش مصنوعی کلا گیج می‌شه و به جای اینکه درخواست رو رد کنه، تمام محدودیت‌ها رو دور می‌زنه و دیتا رو لو میده.
این دقیقاً نشون میده که توی سیستم‌های جدید هوش مصنوعی، همون متنی که ایجنت می‌خونه همزمان می‌تونه پاشنه آشیل و نقطه حمله باشه. حملات Prompt Injection الان دقیقاً دارن همون بلایی رو سر AI میارن که قبلاً SQL Injection سر وب‌سایت‌ها میاورد.
البته این باگ به طور مسئولانه به گیت‌هاب گزارش شده، ولی حواستون به ایجنت‌هایی که به سورس‌کدهاتون دسترسی دارن باشه!
منبع:
https://noma.security/blog/gitlost-how-we-tricked-githubs-ai-agent-into-leaking-private-repos
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/4331" target="_blank">📅 19:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4330">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">یکی از چیزایی که راجب کامیونیتی فارسی باحاله و دوست دارم، اینه که زیاد توی کامنت‌ها با هم در ارتباطیم. کامیونیتی خارجی، این شکلیه که ویدئوی تکنیکال می‌ذارن، 60 کا ویو میخوره اما کلا 25 تا کامنت میگیره. یوتوبره اون 25 تا کامنت رو حتی لایک هم نمیکنه. اما کامیونیتی فارسی، ویدئوی 10 کایی کم کمش 200 تا کامنت رو میگیره و خیلی از یوتوبرا هم جواب میدن و اهمیت میدن</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/MatinSenPaii/4330" target="_blank">📅 16:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4329">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">☠️
ساخت رادار پیامکی با Hermes Agent بدون کدنویسی + API رایگان OpenCode
⚡️
دستورات نصب OpenCode برای ویندوز، سرور لینوکس و دیگر سیستم‌عامل‌ها: https://t.me/MatinSenPaii/4259
⭐️
توی این ویدئو: 1- باهاتون راجب کسب درآمد از Hermes صحبت می‌کنم 2- با همدیگه…</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/4329" target="_blank">📅 16:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4328">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/apuQYQXGy8gxJYSIJiMEgvYrZxcxYihKHCi5cU_RN3dzXXd_oa1PonTINzuf9OtZ_0QTsQOTf-cA0yMvOe7CdEluq_l_4ArOCIDsxP5ZpcD3DPojBdXYcoXRnu_ZO6VcbPTkN33lWK0780Xd-DeFxBpYBg-gtNZW3abUj2sQjFMjXgeGAEnlB90hoYSIhVgOCB5tqvpZL39sMYTKlIEN0dte5RffvJ9azi7qVpf3y32O-8AwUZzpidwL6AMaaFabwwjxKlyo5h5AYKYGnsbeNowbyrhTMKYfA6943jJW4T1mg_VjU_TZx8qC4zhwz0nWBTrPvBj73lvkJ_S5tXO7Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
ساخت رادار پیامکی با Hermes Agent بدون کدنویسی + API رایگان OpenCode
⚡️
دستورات نصب OpenCode برای ویندوز، سرور لینوکس و دیگر سیستم‌عامل‌ها:
https://t.me/MatinSenPaii/4259
⭐️
توی این ویدئو:
1- باهاتون راجب کسب درآمد از Hermes صحبت می‌کنم
2- با همدیگه OpenCode رو به 9Router وصل میکنیم و روش دور زدن یه باگ خیلی رو اعصاب رو بهتون میگم
3- از هرمس استفاده میکنیم که با سامانه پیامکی، یه کرون جاب بنویسیم(قابل پیاده‌سازی برای هر ایده‌ای)
4- و کار با پنل‌های پیامکی رو بهتون یاد میدم
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
همه‌ی مراحل ساده‌ست و نیاز به پیش‌نیاز خاصی نداره. از api رایگان هم استفاده شده توی کل ویدئو
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/4328" target="_blank">📅 15:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4327">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Zombie</div>
  <div class="tg-doc-extra">Bad Wolves</div>
</div>
<a href="https://t.me/MatinSenPaii/4327" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/MatinSenPaii/4327" target="_blank">📅 15:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4326">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">خب انگار فعلا خبری نیست
نت منم اوکی شدش</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/4326" target="_blank">📅 13:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4325">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4325" target="_blank">📅 12:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4324">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHaoodi Senpai</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a627c5c6e.mp4?token=rKb3InbWINSFTbaMYzcamB8MDOeoHVrl2byb7IneRV7MsIfg-NF4xcHp1Zycw4EoYz40Ypwxp-qtiTBpzqoYcjQi289QZe2upoC8-SZhPebHljm6Uw1fXxW-5gMDNzJaVNuWPw1TU8Aj-43lQ3AELxwpefZI2K2c7R-R_IapFh_q6rPc3aj6_Eej8r5gzJDiF_GVux8rResJ5eUXRgHJeoDCUUpSELm42QUiLX8Y3dl3PikLjUa8kP5JUBj1ES3VJbU7a8mLOlHHGvowLEwUyq7nxqG3cEJ2BuvJvowSKFTKPydT_oprSSRGUxbS983TLAv9S-KLd_Q1jlOFxFapRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a627c5c6e.mp4?token=rKb3InbWINSFTbaMYzcamB8MDOeoHVrl2byb7IneRV7MsIfg-NF4xcHp1Zycw4EoYz40Ypwxp-qtiTBpzqoYcjQi289QZe2upoC8-SZhPebHljm6Uw1fXxW-5gMDNzJaVNuWPw1TU8Aj-43lQ3AELxwpefZI2K2c7R-R_IapFh_q6rPc3aj6_Eej8r5gzJDiF_GVux8rResJ5eUXRgHJeoDCUUpSELm42QUiLX8Y3dl3PikLjUa8kP5JUBj1ES3VJbU7a8mLOlHHGvowLEwUyq7nxqG3cEJ2BuvJvowSKFTKPydT_oprSSRGUxbS983TLAv9S-KLd_Q1jlOFxFapRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">The Return of
قدرت مذاکره</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/4324" target="_blank">📅 12:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4323">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/4323" target="_blank">📅 12:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4322">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">مشکلی در وجودشان وجود دارد. آنها دیوانه هستند.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/MatinSenPaii/4322" target="_blank">📅 12:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4321">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">روی اینترنتای خود من به شدت اختلال هست
همراه اول که به زور چیزی باز میکنه
ایرانسل 4g+ اما هیچی به هیچی. آپلود 0
فیبر مخابرات هم از صبح 2 دقیقه وصله 20 دقیقه قطعه</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/MatinSenPaii/4321" target="_blank">📅 11:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4320">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">نسخه‌های اندروید(اگر نمیدونید کدومه برای پردازندتون، Universal رو دانلود کنید)</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/MatinSenPaii/4320" target="_blank">📅 11:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4319">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">💬
آموزش قدم به قدم استفاده از اپ CoreForge  https://youtu.be/filwdiPKN90</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/MatinSenPaii/4319" target="_blank">📅 11:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4318">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">💬
آموزش قدم به قدم استفاده از اپ CoreForge
https://youtu.be/filwdiPKN90</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/MatinSenPaii/4318" target="_blank">📅 11:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4312">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.5.1-arm64-v8a.apk</div>
  <div class="tg-doc-extra">5.7 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4312" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/MatinSenPaii/4312" target="_blank">📅 11:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4311">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">آخرین نسخه‌های مک-ویندوز-لینوکس</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/MatinSenPaii/4311" target="_blank">📅 11:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4303">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.0.0-beta5-macos-amd64.zip</div>
  <div class="tg-doc-extra">27.2 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4303" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🐧
نسخه لینوکس</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/MatinSenPaii/4303" target="_blank">📅 11:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4302">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c0SB2Co6DNEjhRKBWApe95UBXZV9-ZFH63cBjANoOOzWpGHFCslLpwrmEjcw2BjLL3BpkMyYbEqX4HFT_6WeTpIpuisX1S6qH6d5PklZqme80zplyXdIZRXGrf_kEF5xHburc-JyLAXfj8BrrQ3wkDkHKpNCtWh5TL1PIlIqwn57JVcIlNwM0CbddUoKKTa8yk4UGr0NOOZnFzr_wk-w0ZT7ooAa9zj6EtsP-Raqh6eDI9BaWRkpRpdDV5dkp7eLiOS5nZFU_a14JzM3TM9-z0b6SmtHGfJDnsswIZUr7EuLB_6ytlUT_ByHEiqy3PDhwA5hrAPLHSn-msw4No2LkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق معمول، پیشنهاد میکنم WhiteDNS رو راه‌اندازی کنید برای خودتون و دوستانتون
آموزش:
https://youtu.be/6Pm7kNQb3mo</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/MatinSenPaii/4302" target="_blank">📅 11:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4301">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">اعصاب و روان نموند برامون. نمیدونیم درس بخونیم، کار کنیم، کارگری کنیم، لپ تاپو بفروشیم و دلال بشیم که بتونیم زندگی کنیم، چیکار کنیم</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/MatinSenPaii/4301" target="_blank">📅 11:08 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4300">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">میترسم پنج دقیقه بخوابم ببینم نت قطع شده باز</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/4300" target="_blank">📅 11:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4297">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/l3yjSmzCzGepjLbEYlU3-ZKN2st3MD8E5tI8LdDKiGXO4Tn4zWpETEBH5Ii2dEEf_164hWzQA5uK3mBUOil3gIzNlILx7cBQsSMhafimEv58LlY3wKtHFq7k78nO170lsBFR5dPWmBK5cP4Lcxa0yWPL3WHtAPWxSD2fGv4GE7smQtFDoAwCxf8YPldXC5l4Wxljn5dsRwOR-1HdvqAmNHNqpKF5FVjsJW1zmQPFCqO9iU2XLGZY9MOM8QPFX-LV7xugl67IieSWfCuQKc3T74v-pqinIRFVNldll4pkeU21d-iV5K_pXQHL_8KwL4WDwMyOYMz1P8WitIt4Z2RU_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VnLCUGb8T5EnwRjBeyOVfO0eVroqCDd6h9sToER26tAFK3g_wnPsYnmL6icAv7LGwMkDYfDJMXR5iXrZE3R1uWYVls_R4_B8zh59U64CI7UsRrUnpHpOKzuWD2Ozpj48zFcjlZZtrwHZqP9jc-giuiSFA5tVXK1pJw1EQhS7B7rjdVlIeMMk-3ilqHD-9M1gCN61bwYdrL47qtS0hnj3MOJWn_cQdo8rJS9RgffbDVeHTIM78qfrVnpZvhF--ZI2EKmOwIh4OozSXJTEZCPF7x9ykFvHNQlDWIeIelH31E41pWd-oy1DlFsu3Wq8V4M_GmRBf83T1WXh2Fq8KEtSCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uUriDRH9BYcC5s4uyvOHZcnumYEGTB_mz9A57Nni0AohUdbc-_4Ul7RutoUX0S3sngC6xt3STL39Yoa7_4j9Su2jOL5JplZXX2QZp4ZVdHBRkuK1n3oEuBNRV3qL22zL1Sa3PSU3LHKwOECxLskfn0omvoJEcHZQzTdPMrAEztP3zoG86EUCQzslDUpyRjG2e4mKep23Mnw91Twl-vVCT0-eR-uwWOxA2NB_UdRg67IHbTdrvk-EnnRgbKbcX60UFM6LXJX3TCsKWZdFrfDkkhdI42fiGXkwC7wurlM4ZsPNVBD2raj1yooop59M929_6a1pLDXYtDf_5DhWlUj5bg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی هزینه‌ی هوش مصنوعی از حقوق مهندس هم بیشتر می‌شه
خلاصه:
شرکت «آنتروپیک» (Anthropic) حدود ۲.۳ برابرِ پولی که بابت حقوق و دستمزد می‌ده، خرج زیرساخت و پردازش (Compute) می‌کنه! یعنی با حساب حقوق سالانه ۲۲۴ هزار دلاری (با احتساب تمام مزایا)، سالی ۵۱۵ هزار دلار به ازای هر مهندس خرج پردازش می‌کنه. در حالی که ۱ درصد از برترین شرکت‌های نرم‌افزاری فقط ۸۹ هزار دلار و شرکت‌های میانه بازار (میانه آماری)، کلاً ۱۳۷ دلار خرج می‌کنن. حالا ۳ تا سناریو برای سال ۲۰۲۹ داریم که نشون می‌ده این شکاف عمیق چطوری ممکنه پر بشه.
همونطور که اشاره شد، آنتروپیک ۲.۳ برابر حقوق پرسنلش، در حال حاضر داره خرج زیرساخت و پردازش می‌کنه. با حدود ۵,۰۰۰ تا کارمند و تقریباً ۱۰ میلیارد دلار هزینه‌ای که توی سال ۲۰۲۶ برای آموزش مدل و استنتاج (Inference) می‌کنه، سهم هر کارمند سالی حدود
۲ میلیون دلار
هزینه پردازشی می‌شه؛ اونم در مقابل حقوق و مزایای کلانی که برای هر نفر احتمالاً بالای ۵۰۰ هزار دلاره!
بقیه بازار نرم‌افزار خیلی از این رقم‌ها عقب‌ترن. ۱ درصد از برترین شرکت‌ها سالی ۸۹ هزار دلار به ازای هر مهندس روی هوش مصنوعی خرج می‌کنن؛ یعنی ۴۰ درصد از یک حقوق ۲۲۴ هزار دلاری برای یک مهندس ارشد. این رقم برای شرکت‌های میانه بازار فقط ۱۳۷ دلاره! اختلاف فاحش اینجاست:
۲.۳ برابر حقوق
در لبه‌ی تکنولوژی
۰.۴ برابر حقوق
در صدر بازار
نزدیک به صفر
برای شرکت‌های معمولی بازار
حالا بقیه‌ی بازار چقدر می‌تونن خودشون رو به این سطح برسونن؟ جواب این سوال توی ۳ تا سناریو خلاصه می‌شه.
(توضیح نمودار خطی(عکس سوم): نمایش سه سناریو برای هزینه‌های هوش مصنوعی به عنوان درصدی از حقوق مهندسان تا سال ۲۰۲۹؛ در سناریوی خوش‌بینانه، این رقم به رکورد ۲۳۰ درصدی آنتروپیک می‌رسه)
سناریوی بدبینانه (کاهش قیمت توکن‌ها برنده می‌شه)، سناریوی پایه (رشد ۱ درصد برتر بازار کند می‌شه)، سناریوی خوش‌بینانه (بقیه بازار تا سال ۲۰۲۹ به نسبتِ هزینه آنتروپیک می‌رسن). هر کدوم از این سناریوها، هزینه سالانه هوش مصنوعی به ازای هر مهندس رو نشون می‌دن(عکس دوم)
توی سناریوی خوش‌بینانه، فقط هزینه هوش مصنوعی به ازای هر مهندس، با کل درآمدی که یه کارمند توی شرکت‌های معمولی SaaS تولید می‌کنه برابری می‌کنه! همین الانش هم شرکت‌های آنتروپیک و اوپن‌ای‌آی به ترتیب ۱۴ میلیون دلار و ۶.۵ میلیون دلار به ازای هر کارمند درآمد دارن، که بالاترین رقم توی لیست ۲۰۰۰ شرکت برتر فوربز (Forbes Global 2000) به حساب میاد.
ساختار هزینه‌ها، دقیقاً جا پای ساختار درآمدها می‌ذاره.
موتورهای محرک توی سناریوی خوش‌بینانه:
قیمت مدل‌های پیشرفته ثابت می‌مونه، چون هزینه‌های آموزش به ثبات می‌رسه و تقاضا از عرضه جلو می‌زنه. فرآیندهای کاری مبتنی بر ایجنت (Agentic Workflows) نسبت به چت‌های معمولی، چند سر و گردن توکن بیشتری مصرف می‌کنن؛ طوری که «گلدمن ساکس» پیش‌بینی می‌کنه مصرف توکن تا سال ۲۰۳۰ حدود ۲۴ برابر بشه. تازه، اگه شرکت رقیب قابلیت‌های جدید رو سریع‌تر عرضه کنه، دیگه پرداخت صورت‌حساب هوش مصنوعی یه انتخاب نیست، بلکه یه اجبار حیاتیه.
ترمزها در سناریوی بدبینانه
: قیمت توکن‌ها توی سه سال گذشته، هر سال ۱۰ برابر کاهش پیدا کرده. مدل‌های متن‌باز (Open-weight) دارن با کسری از هزینه‌ها، شکاف کیفی رو پر می‌کنن. از طرفی شرکت‌هایی که مصرف هوش مصنوعی رو بر اساس نقش یا حجم کاری کارمندان سهمیه‌بندی می‌کنن، می‌تونن شیب این نمودار هزینه رو خم کنن و کاهش بدن.
نظر شخصی: اصلا نمیشه پیش‌بینی کرد:) با اومدن ایجنت‌ها، سناریوی توکن داره مطرح میشه. از اون طرف، چین غوغا کرده و با رایگان عرضه کردن مدل‌هایی مثل MIMO و GLM-5.2، واقعا نمی‌تونم نظر بدم.
منبع مقاله:
https://tomtunguz.com/ai-spend-breakeven-2029/
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/MatinSenPaii/4297" target="_blank">📅 00:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4296">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">یه مقاله از نیویورک تایمز(با اینکه ازشون خوشم نمیاد) دیدم که توی هکرنیوز بحث‌برانگیز شده. داستان در مورد اینه که با پیشرفت سریع مدل‌های زبانی، مهارت‌های کسایی که فلسفه خوندن، چطور توی بحث‌های اخلاقی هوش مصنوعی و Alignment مدل‌ها داره به شدت کاربردی می‌شه. و انگار یه بازار کار جدید داره برای این رشته شکل می‌گیره =)
لینک مقاله:
https://www.nytimes.com/2026/07/05/business/philosophy-majors-ai-jobs.html
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/4296" target="_blank">📅 23:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4295">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">اگر میمو روی اوپن کد بهتون ارور ۴۲۹ داد که به لیمیت رایگان رسیدید، نترسید. یه continue بگید دوباره میره ادامه:)</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/4295" target="_blank">📅 21:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4294">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">اگر میمو روی اوپن کد بهتون ارور ۴۲۹ داد که به لیمیت رایگان رسیدید، نترسید. یه continue بگید دوباره میره ادامه:)</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/4294" target="_blank">📅 20:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4293">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ft11FrXkG-bTNbWh2DoNny1TDb59FLYwiFm9g7AzD4eEjpoi8w0Bvpl95G6LiRJngzTqxCsN5Xcx9IcVHbXB7KIA95-EpIk-JfEXbZPg3Ts-l5xEam5_9n5oWMAggdpug9AYu2FvkqTBY5LLwTwzyWtKqPVNhL7_xycP8u7-vGY_7464pAB490yg2024JAYlRpfSpTErUDbaj7V-C3VHlzBbccGJzAANWPXc2mFfJg7hDYgb80mw0ZIQO5sSV_A66xEng6cVR3FyuVFANfVV4o9puv0pRUdNtSt6o7DMul6DH8eNswx7TIOiizKZTK2ilGLlXhab-yhZuu7w2Xu29g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زبان برنامه‌نویسی Cyrus(کوروش) چیست؟
سایروس یک زبان برنامه‌نویسی متن‌باز و جدید است که برای ساخت نرم‌افزارهای زیرساختی و سیستمی طراحی شده؛ یعنی همون نوع نرم‌افزارهایی که نزدیک به سخت‌افزار کار می‌کنن و به سرعت و کنترل دقیق نیاز دارن (مثل سیستم‌عامل، درایور، یا ابزارهای زیرساختی).
فلسفه اصلی سایروس این است: هیچ اتفاقی پشت پرده و بدون اطلاع برنامه‌نویس نیفتد. یعنی کد باید همیشه روشن و قابل پیش‌بینی باشد و برنامه‌نویس دقیقاً بداند هر خط کد چه کاری انجام می‌دهد، بدون رفتارهای پنهان یا پیچیدگی‌های اضافه.
چند ویژگی مهم سایروس:
بدون گاربیج کالکتور
: بر خلاف خیلی از زبان‌های مدرن (مثل پایتون یا جاوا) که حافظه رو خودکار مدیریت می‌کنن، سایروس این کار رو به خود برنامه‌نویس می‌سپارد. این یعنی کنترل کامل و دقیق‌تر روی مصرف حافظه، که برای نرم‌افزارهای سریع و حساس خیلی مهمه.
کامپایل مستقیم به کد ماشین
: سایروس از فناوری معروف و قدرتمند LLVM استفاده می‌کند تا کد رو قبل از اجرا به‌طور کامل به زبان ماشین تبدیل کند؛ نتیجه‌اش برنامه‌ای سریع و بدون واسطه است.
سازگاری استاندارد با سیستم‌عامل‌ها
: طوری طراحی شده که به‌راحتی با نحوه‌ی کار سیستم‌عامل‌های رایج هماهنگ باشد.
سینتکس ساده و مینیمال
: تلاش شده که نوشتن و خواندن کد تا حد امکان ساده و بدون ابهام باشد.
قابلیت‌های پیشرفته بدون هزینه اضافه
: مثل ژنریک‌ها (نوشتن کد قابل استفاده مجدد برای انواع مختلف داده) و چندریختی (Polymorphism)، بدون این‌که سرعت اجرای برنامه رو کند کنند.
ساخت افزایشی (Incremental Build)
: یعنی موقع تغییر کد، فقط بخش‌های تغییر‌کرده دوباره کامپایل می‌شوند، نه کل پروژه؛ این باعث سریع‌تر شدن فرآیند توسعه می‌شود.
هدف کلی سایروس این است که زبانی باشد نزدیک به سخت‌افزار و ماشین، اما بدون این‌که خوانایی و سادگی کد قربانی شود.
این پروژه هنوز در حال توسعه است و به‌تازگی نسخه بتا (Beta) آن منتشر شده. اگر دوست دارید بیشتر بدانید، امتحانش کنید، یا در توسعه‌اش مشارکت کنید:
مستندات:
https://cyrus-lang.ir/en
گیت‌هاب:
https://github.com/cyrus-lang/Cyrus
کامیونیتی:
@cyrus_lang
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/4293" target="_blank">📅 18:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4292">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">آخرش یا atomic mail ایرانو بن میکنه یا ما atomic mail رو از کل جهان ابیوز میزنیم
😂
😂</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/MatinSenPaii/4292" target="_blank">📅 16:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4291">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">دیروز و پریروز می‌خواستم ویدئو بذارم، اما با اینکه موضوعات زیادی دارم برای ویدئو ساختن، حس کردم که کمی عجولانه‌ست و تایم گذاشتم که هم خودم کمی بیشتر با ابزارها کار کنم، هم وقت داشته باشم برای مطالعه‌ی شخصی که محتوای باکیفیت‌تری ارائه بدم. برای همین تا وقتی حس نکنم کافیه، ویدئوی جدیدی منتشر نمی‌کنم
❤️</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/MatinSenPaii/4291" target="_blank">📅 16:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4290">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QVUjQzTslFGHl1A9RbgkBWTBwttuV-VrgQOPV2NDxWzLjalzsuSnLgGIwXKPGGX5zNhY-PLCNRjP00UeZUMx0pza2rtIQbsyixaOXQy2VMnKL8v2_ixPOO8q_pYiIg9wLG8m3JTBNDQ6lQp5sVgrnnw0rPrjp8RGUn3ASzO3KxNO06lFmPb3nKHN3BLk6VtBaqN0C891EJRU0_Q-Wcd-oupLtu_e3m1HXkyV6IdGm3wzbhEqRqDwieDLP4vhVKNrCCBSFlBamadJtr5WnPhPLz2rcoZIDIA70tcDUgCGApwWPBm2JuxkrYc64xye4Le1uhdu5zCXkeSeeuL9VaaJDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا هزاران پست سیو می‌کنیم ولی هیچ‌وقت نمی‌خونیمشون؟
🤔
اسم علمی این رفتار
Digital Hoarding
(ذخیره‌سازی وسواسی دیجیتال) یا "
پارادوکسِ بعدا می‌خونم
" هست.
این اصطلاح رو اولین بار
Van Bennekom و همکارانش توی سال ۲۰۱۵
و داخل یه مقاله توی مجله‌ی
BMJ Case Reports
مطرح کردن؛ اونجا یه مورد بالینی رو توصیف کردن که یه مرد ۴۷ ساله هر روز حدود ۱۰۰۰ عکس روی کامپیوترش ذخیره می‌کرده بدون این‌که هیچ‌وقت سراغشون بره.
از اون موقع، این پدیده به یه حوزه تحقیقاتی جدی تبدیل شده. تحقیقات جدیدتر (مثل مطالعه‌ای که سال ۲۰۲۳ توی مجله
Journal of Obsessive-Compulsive and Related Disorders
منتشر شد) نشون می‌ده Digital Hoarding با الگوهای شناختی و هیجانی شبیه به اختلال وسواسی-جبری (OCD) و وابستگی هیجانی به اشیاء مرتبطه؛ یعنی حذف‌کردن یه فایل یا پست، همون حس ناراحتی رو ایجاد می‌کنه که دور انداختن یه وسیله فیزیکی.
چرا این اتفاق می‌افته؟
👩
هر بار که پست مفیدی رو سیو می‌کنیم، مغز دوپامین آزاد می‌کنه؛ حس «پیشرفت» بدون این‌که واقعاً کاری انجام داده باشیم.
✈
ترکیبی از
FOMO
(ترس از دست دادن اطلاعات) باعث می‌شه به‌جای مصرف محتوا، فقط جمعش کنیم.
💤
نتیجه؟ انبار دیجیتالی از Save‌ها و بوکمارک‌ها که عملاً هیچ‌وقت سراغشون نمی‌ریم.
چندتا راهکار عملی:
قانون 5 دقیقه
: اگه محتوا کمتر از 5 دقیقه وقتتونو می‌گیره، همون لحظه بخونید؛ وگرنه رهاش کنید.
سقف هفتگی
: حداکثر ۵ تا ۱۰ آیتم توی یه هفته سیو کنید تا تلنبار نشن.
دسته‌بندی و پاک‌سازی دوره‌ای
: هر چند وقت یه‌بار Saved items رو مرور و پاک‌سازی کنید.
اگه واقعاً مهمه، به‌جای سیو کردن، همون لحظه یادداشت بردارید یا اجراش کنید.
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/4290" target="_blank">📅 16:16 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4289">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">آخرش یا atomic mail ایرانو بن میکنه یا ما atomic mail رو از کل جهان ابیوز میزنیم
😂
😂</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/MatinSenPaii/4289" target="_blank">📅 15:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4288">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kpP88DPpPPHEFfhcdywzx9Bcs9UK8So3--cYtUA56VWs_ezB7-aKMBGJdy7SHEdvN2lhmCCAXwjL0ZqFbD-uV_JyOMzCkSuKgEZIQMvKmvBK2jf4EC95Na1YIxH0c5fU9xGHAWaSGKunOoFqIjcNGD4032UstqZDSYu_-wStFK4jjS0yj4HTx7hmxOG-_qhsmG2mdtEvw2TjTlxsCHDG1iGI1Msij2akt1rIm2c9Jo9Fc1M2-8y9oJLge6fUtRo6AtrKdeo3Jl8cryFkes1SPXQj5MOlzG60f1ESbQQUJj7iYlipv6CcMOKWqwLYSXv5qkRUq0XJHdHyNYt06argJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرمس نتونست لینک مقاله‌ای که بهش دادم رو باز کنه به خاطر firewall امنیتی توییتر، خیلی راحت با قابلیت Browser که اینجا: https://youtu.be/_30_ng3Hyfs یاد دادم، روی دسکتاپ برام هم عکس‌هاش رو دانلود کرد هم مقاله رو کامل ترجمه کرد:)</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/MatinSenPaii/4288" target="_blank">📅 14:47 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4286">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/h-zDxMoQFGRSpoP8FgpsDxPOfcIIZRub98pDTlzicOxbVytwjrXeEnqSK0rwuxiSqchGRWUdPuRzNDye6GcdcI29cqk5hjpayepGEhxG7LyA9Q-FSTbiNAitUyraZTzacYzxP1XZQaVdlHaSGpt5ka5jGRKJZks5St21xWBONaLCHUzZRN8c_JSwHXS1L1W0gbyhjK4Ug7H9eE9FNWPfz669fn8i_B8i04XuxP1zxMR41RklHXU5mfuFYd9823Utw6CXW394O1xnefu4BIc7dh4o1OGL5Jv8ITKJcKL10obfodG2izY28p17V_mZXG43KgUDi01Vz3V31469tRSI9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tRSbW_3wfaYgC3KqonMG-mac6lrQOa_cTDih8RMGvo2wH2G1twt5crTpa0m4T_yxYEWyFcmRibPqQDVj4lr5smJvclJ0FFbM7Y94vykXqeKIir-NpexGmm4QpBZmpZDWOazLAHXUTLRsdu3iJigitOs7ITbzJRogL11FixIQZ86Xz1kbFHqgzTGpAFgrwD31kh-Qd8X49ebanKsXjO_JGyhgFy7gZdnTTDZqgd2Xfhfz6ee7OCeB44L2Xs6UOM2s5M2rrmrCd6JNkNgSPW76I4nf3QbH4qkvSxP1Dx3EDYvoCxEciD_SDNpD7ixM1Pc3isJa_-SgFzi5HifaCRUmpA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هرمس نتونست لینک مقاله‌ای که بهش دادم رو باز کنه به خاطر firewall امنیتی توییتر،
خیلی راحت با قابلیت Browser که اینجا:
https://youtu.be/_30_ng3Hyfs
یاد دادم، روی دسکتاپ برام هم عکس‌هاش رو دانلود کرد هم مقاله رو کامل ترجمه کرد:)</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/MatinSenPaii/4286" target="_blank">📅 14:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4285">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K90ihFgl4m4MnRc5qLUFs81ylkaUPKRKTVDXkYtua79euHR5Bq0TyNICratjHNgRxFFUHIj0aKt1VE7TJrPof0kx5coLAKK1hjWOgHq-2UqK3Rp1m7vtiXmpeiUaV_nsGhN05pLfBSKzobgS1PCuoc3fWiOfuEMX8wqAnZsg6Fu0Jw_S-TqcqEcoN0k5MNAOtliD_Z6laJu5RR7il6pncHgxpfCrc7W6jDPA1AbyPJoUj26f9mOlp3I_m5qilTLswGcvsytLz4IpW0KZlPB9AfYVB6REuPI79NcMCHQCfiYwjGo9by5819hfdvckgP3DMz6_NXrFEmOjXEgZ5XTH1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه با docker کار می‌کنید، احتمالاً درگیر زدن پشت‌سرهمِ دستوراتی مثل
docker ps
و
docker logs --tail 50
هستید تا چندتا کانتینر رو همزمان مدیریت کنید. این کار هم خسته‌کننده‌ست و هم ترمینال رو به هم می‌ریزه.
ابزار
Lazydocker
دقیقاً برای حل همین مشکل ساخته شده؛ یه TUI برای داکر و داکر کامپوز که تمام کارها رو با شورت‌کات‌های کیبورد براتون انجام می‌ده.
-
بدون switch کردن:
همه چیز از مصرف منابع (RAMو CPU) تا لاگ کانتینرها به صورت زنده توی یه داشبورد یکپارچه نشون داده می‌شه.
-
سرعت بالا با کیبورد:
لاگ دیدن، ری‌استارت کردن یا پاک کردن کانتینرها فقط با زدن یک دکمه کیبورد انجام میشه (بدون نیاز به موس).
-
پشتیبانی کامل از Compose:
سرویس‌های داکر کامپوز رو هم به خوبی می‌شناسه و مدیریت می‌کنه.
-
بدون کانفیگ:
با زبان Go نوشته شده و فقط یه فایل اجرایی باینریه؛ نیازی به نصب سرور یا دیپندنسی اضافه نداره.
و خلاصه این ابزار سرعت کارتون رو چند برابر می‌کنه.
گیتهاب Lazydocker  + آموزش نصبش
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/MatinSenPaii/4285" target="_blank">📅 14:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4284">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">اگر روی هرمس برای اتصال به api به مشکل VPN برمی‌خورید، از تکنیک رایگان وصل کردن پروکسی کلودفلر که توی این ویدئو توضیح و انجام دادم استفاده کنید: https://youtu.be/Ae8oyaIHi9o</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/MatinSenPaii/4284" target="_blank">📅 13:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4283">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">پیرو ایمیل یکی از بچه‌ها، تست کردم، با موفقیت بدون شماره مجازی و با atomicmail فیک تونستم api key رایگان Nvidia بگیرم:  سلام متین خوبی داداش متین به خدا شوخی نمیکنم همه میگن سایت انویدیا برای اینکه Api بده باید شماره مجازی بدی و از این کارا من تو گوگل سرج…</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/MatinSenPaii/4283" target="_blank">📅 12:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4281">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Ag-JgGIUC2iPlYukHLxk4RN46_W3lgnEpAUQClk-gLabXRFATizA9unKgZ-Pp1odueuUaHZP0M2Au5Pvu8n7o8xYiqm7oe_Gm_z1l3rOJF2Rk0FeYgQ8nHOVtBRTCcfANpJIHI7SjWq8wdoPTuOiSFIPeTwBR4uG6Kaw6i0Fn9uvjUmvH8pbOBNMxrgwoU6Fvd00kKgRQibO-lg7inKTyjv-s0hqLydyNZ-0S9Q8sPTfZGURBZdXqmVvJYYLGmP4vDVN0l4PfYAUen7PJEStg-WH2Gnlae58f5cpE31q_0ijP0UgakrfslrYU02w2vAOuzPV3LyL3xvCw5DlU8E1Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KwhKggYKklTzWMpRVNrh76ZkfvDNA0u6hgSdE4kYXM_z1i8LrOyp3iz6mMzwnOdVd_bDCCxeXAVohSwQ2TcPTIfeZxfqSGYXtnK1-639rSS5_9Hxza2wYiSfTjXk9XZmKYMb_VVz1fBtaio8BtKLHnWNiSrgPdjfDnZF_sZxUqqjuDhCM-hppCdKx5W0g6p2bdWcp7WvjBfR4JPa5Ld5SoshbFPMP2q5J3M3qqbksLCPBHG_kMURzdGL5yIITy9ifJoxlgBWX28Nn_skM7aSCI6H896BoJsyUEIPyTRcTAjD4JIR1XgsIg-bYsLofKdCfAkmg-UnGAoP7W0_FceqvQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیرو ایمیل یکی از بچه‌ها، تست کردم، با موفقیت بدون شماره مجازی و با atomicmail فیک تونستم api key رایگان Nvidia بگیرم:
سلام متین خوبی داداش
متین به خدا شوخی نمیکنم
همه میگن سایت انویدیا برای اینکه Api بده باید شماره مجازی بدی و از این کارا
من تو گوگل سرج کردم و هنوز هم شماره مجازی نخریده بودم
https://build.nvidia.com/settings/api-keys
ببین دقیقا ادرس هم برات گزاشتم
تو گوگل سرچ کردم Nvidia Get ApiKey
بعد سایت اومد بالا ازم ایمیل خواست
تازه atomicmail وارد کردم ایمیل گوگل هم ندادم
بعد که وارد کردم منو برد تو یک صفحه ای یک کپچا داشت تایید کردم و رمز عبور خواست اونم اوکی کردم
بعد گفت نام کاربری رو وارد کن اونم وارد کردم
منو مستقیم برد تو صفحه apikey ها و استفاده هم کردم
با تشکر از محمد عزیز. نمیدونم انویدیا وریفای رو برای ایمیل‌های شخصی برداشته یا اینکه کلا برداشته</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/4281" target="_blank">📅 11:47 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4280">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">اگر روی هرمس برای اتصال به api به مشکل VPN برمی‌خورید، از تکنیک رایگان وصل کردن پروکسی کلودفلر که توی این ویدئو توضیح و انجام دادم استفاده کنید:
https://youtu.be/Ae8oyaIHi9o</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/MatinSenPaii/4280" target="_blank">📅 11:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4279">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">یه پروژه‌ی خیلی عجیب روی گیت‌هاب (با اسم Pon) منتشر شده به تازگی که تونسته پایتون ۳.۱۴ رو مستقیما به کد ماشین کامپایل کنه و دیگه نیازی به Interpreter و مفسر نداره. این برای پرفورمنس پروژه‌های پایتونی می‌تونه یه انقلاب باشه
👍
https://github.com/can1357/pon
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/4279" target="_blank">📅 11:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4278">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">یکی از دوستان رو اون روز باهاش صحبت کردم، برای یادگیری فرانسوی داشت از Hermes استفاده میکرد در کنار منابع و ... دیگه‌اش. و به شدت راضی بود و می‌گفت حس میکنم بازدهیم چندین برابر شده
جالب بود برای خودم</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/4278" target="_blank">📅 02:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4277">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">یعنی حس خوبی که وقتی از api رایگان در سطح کلان(
😂
) استفاده می‌کنی، با هیچی قابل مقایسه نیست. فکر کنم Open Code ازم شکایت کنه اینطور که دارم توکن میسوزونم</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/4277" target="_blank">📅 00:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4276">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">یعنی حس خوبی که وقتی از api رایگان در سطح کلان(
😂
) استفاده می‌کنی، با هیچی قابل مقایسه نیست.
فکر کنم Open Code ازم شکایت کنه اینطور که دارم توکن میسوزونم</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/4276" target="_blank">📅 00:16 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4275">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d956281ee.mp4?token=EogGW0-vGatBQYD6a00-JKHld_X2YIlpZbs4egxgueDp-lkM-qodZi83nNdhlbyYDO_djjibeoyKSIZMGW0s7sFwizGSDG1dA4Yffz1BkdLi-1AldaiO2C5gawaUyX8PAfSvHBlP9qGxV9Dylrhzyr34kzBcuZkI19KXTqhaVoUElWgZJfCk0HsQd9eBdyLHqcwOIbqZBfao21y6Ayqop56C2S768otidTlyLzBN6gMGie8th2P4LXWg4JOMZTX11YJCqZeLEX90AiJvw3-_jp2GnZ9texSPie-NPCz0Fvh6A7AIhIaSdzg6HPm3m9U2wGBzFEYOO0p1pKsg7_S3XUlmFBfZaps1iZ3ktHRKkyuTQ0psdzNzb4DrWz9gN0XOcSbsMnn_D2AVXsKMaZjcDgipGtz375FU46iuHI_rkdEJGDNyZAOEL46Da0SDaDjCWEO8HKvF-7SEkf9ziYJOyhjuhifHbDL1n1qAHIDEinD7sRo6Xkkb0ObPV-NvyZFQQHWcFHHFCFgX_mz3QBHwj4Fvv7iqwygZ8oIQAfknhwYH_AuRSzJDdh2KrgtUlKXeUcwdJWREn3oYkeViL96Wmot1Yl06zT-gxWqg3oWaiIIJpUD_er__QmXDSUt4IwgLoVs_RPiIEFuabmfcOPK-PQv3g0nefHQUEmEof_YORxI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d956281ee.mp4?token=EogGW0-vGatBQYD6a00-JKHld_X2YIlpZbs4egxgueDp-lkM-qodZi83nNdhlbyYDO_djjibeoyKSIZMGW0s7sFwizGSDG1dA4Yffz1BkdLi-1AldaiO2C5gawaUyX8PAfSvHBlP9qGxV9Dylrhzyr34kzBcuZkI19KXTqhaVoUElWgZJfCk0HsQd9eBdyLHqcwOIbqZBfao21y6Ayqop56C2S768otidTlyLzBN6gMGie8th2P4LXWg4JOMZTX11YJCqZeLEX90AiJvw3-_jp2GnZ9texSPie-NPCz0Fvh6A7AIhIaSdzg6HPm3m9U2wGBzFEYOO0p1pKsg7_S3XUlmFBfZaps1iZ3ktHRKkyuTQ0psdzNzb4DrWz9gN0XOcSbsMnn_D2AVXsKMaZjcDgipGtz375FU46iuHI_rkdEJGDNyZAOEL46Da0SDaDjCWEO8HKvF-7SEkf9ziYJOyhjuhifHbDL1n1qAHIDEinD7sRo6Xkkb0ObPV-NvyZFQQHWcFHHFCFgX_mz3QBHwj4Fvv7iqwygZ8oIQAfknhwYH_AuRSzJDdh2KrgtUlKXeUcwdJWREn3oYkeViL96Wmot1Yl06zT-gxWqg3oWaiIIJpUD_er__QmXDSUt4IwgLoVs_RPiIEFuabmfcOPK-PQv3g0nefHQUEmEof_YORxI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🍷
آموزش کامل Mahsang VPN | تنظیمات جدید CDN Fronting و اتصال پایدار
اگر می‌خواهید با روش جدید اتصال Mahsang آشنا شوید، این ویدیو را از دست ندهید.
✅
آموزش نصب و راه‌اندازی
✅
تنظیمات کامل CDN Fronting
✅
روش جدید اتصال
✅
بررسی تمام گزینه‌های مهم برنامه
✅
نکات افزایش پایداری اتصال و رفع مشکلات رایج
اگر قبلاً در اتصال یا تنظیمات Mahsang سؤال داشتید، احتمالاً پاسخ آن را در این آموزش پیدا خواهید کرد.
🎥
ویدیو را از کانال TakTarfand ببینید و اگر مفید بود، برای دوستانتان هم ارسال کنید.
لینک مشاهده ویدیو در یوتیوب :
https://youtu.be/35-GhIi-egg
@mobamoz_channel
⚡️
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/MatinSenPaii/4275" target="_blank">📅 23:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4274">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">سلام
❤️
توی این آموزش، تمام بخش‌های برنامه V2Ray را از مبتدی تا حرفه‌ای به‌صورت کامل بررسی کردیم؛ از اضافه کردن کانفیگ و Subscription گرفته تا تنظیمات پیشرفته، Routing، آپدیت برنامه و حالت‌های مختلف Tunnel.
🇺🇦
لینک آموزش در یوتیوب:
https://youtu.be/i1-XenoSalk?si=5jbQK3BrGAe4ctsu
اگر موضوع یا نرم‌افزار دیگری هست که دوست دارید آموزش کاملش را ببینید، داخل کامنت‌های یوتیوب یا گروه تلگرام پیشنهاد بدید تا برای آن هم آموزش تهیه کنیم.
@WhiteDNS</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/MatinSenPaii/4274" target="_blank">📅 22:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4273">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">توی همین 5 دقیقه شد دو میلیون</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/4273" target="_blank">📅 20:31 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4272">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TyiKqPp0XH9LGWS3Q33RtLn7ZANyk2rAHUQj8CE8Jn3HZxrGekS6HV9K03s2sFAM3X6QgC0FXlQoehBA4fwW0OkNNdZ11MSyF4jGpLiBvkAEkqRbu54XtNTcHDTHMNT7ynUhO1S56yHnX3RIBulDG7-oJhi3PNgzic95zXCcXOKtD4MIlY9D0lv5VmTW35lEUC3Icc_PhQSKnpD_NyB-wJaN4QCB6pf4zdXfg3laobh2JVBTECpR1S7SupzupWgE7HzVaauB_3ePD8HQSbVJW7J7dGeO_wKG-DNJ_DktHw3DM4dtaco8SJVq2ZObJDG6d7LZXHn0P55xqNzxJkoE8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه جوری داره توکن می‌خوره که واقعا توصیه میکنم همچین کارهایی رو با api پولی و اشتراکای محدود مثل claude pro انجام ندین درود بر چین
😂
😂</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/4272" target="_blank">📅 19:53 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4271">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WPzybRWFpS7Gk2VAe94f5JQBz_ZUmr0DUcXCjft0a-F0IuJOyAQ4jMTlX0o3w-q26VB9HSpr_-8TdcYo32lB42ccK5QcUP0RKxccilFulAPyTm3NP8UpY2TJgWcNKgEXya9r0ooExi3SBMVVRWWpKR_Tqyw41Gd3KXry483zujwb-vrBgex8D-CBLnRvoZdeUoqj55Eo96NMVwG7KuIkQFVuUroRFRsUnFjNgQyssVs7afZX6ArHVXWviyV2gIb8BTu3SKDRkPoW_hfyjNlWgvnvYxj7RONTDBtb2i_KZKMvSrjf4kvzEHT7568uPeWM3Ff_JdG121hMeTAAxhP-dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه جوری داره توکن می‌خوره که واقعا توصیه میکنم همچین کارهایی رو با api پولی و اشتراکای محدود مثل claude pro انجام ندین
درود بر چین
😂
😂</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/4271" target="_blank">📅 19:48 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4270">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eppS3bF30qxizWlEGEDycBFML7DHuc0S8yH-UbRW9pBdO3ViguXljKgKj2ZjPXbjWRq_xjHWKa9ywTYC4SfagKKbfXJokMP3MN5PBN47sp_fNva6ybjGcP0dI1eXFGPVlGS76Bb5iAsm3Mws1iWbY2ESFBqIGiGyrFqZHepT2nDky2WaDUN1XQhjfBRDQTACVhbg66trUJkFLesgtTF4HnLcO6pZuHTmM6oRgpvTDxQ4PNx1d7gJQ0ajwUVVP4De7WUrqFpJFon3w9FUFkkWFdb4EoytXmER1Zd8B4KnvHGgb4HiOa8kElOlN1Qd7UwDfv3tGN-RlFIvNKP_7rHxAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب این قراره خیلی باحال بشه
😂
برم ببینم تا چه حد پتانسیلشو میتونم بکشم بیرون</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/4270" target="_blank">📅 19:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4269">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CHvFkTCEywYyVSE--vNAoijrRjqr3te2FkCx6FwFEeVzTw28AO1_LeYvervgqEyY_hHK5fuDck5WgDJhWzgP62bQ4vt8sR7fezh5o6qlU0T1EXbx772tKniSmSM8qgC-j9Bjfj5lCYfmZeN3mIBPMpyVSBVy5ZWbug-kWa4ewYEOk0RPYxAar8uxGlo4w_MILjJe4F_Lhg2wHPjDMJx6Ohy_f6EmoLnmgd-BwCQ_Kby-jPsxl_RcSN_rNqYSaonOr8QvjhQlxOr9RnUK0NEakjCw-3T6yhP0cFz3GOGeGSY-bShq8hGLwtS0EMSgGlrRYJGY_i6soSZDmTUJxdeF1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب این قراره خیلی باحال بشه
😂
برم ببینم تا چه حد پتانسیلشو میتونم بکشم بیرون</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/4269" target="_blank">📅 19:38 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4268">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tHliXjn1LZtJTLp5Edqu1kaEKWN1_gOJz3dF_FkybyunQHuO3rKIVChuSpAVdgf9Qo0EGKNGgYLMvTrvWoEnjzCiKF-2T8adYeu6xW7sJcBRXPXMcyJvNBlTQtCGvz1F4vHwUdHCbW9RAcodvYETEIserRrZCl4xa7RdzwOMvK2Us9Cl3Zm6XKhdiUsscTprHDIbQ5DSdUdquGi0NddC7YpNTgzd4FjTvA6SpNlcTLBHmbsAsE45M23f0-eRF80VNqlIziUDJOsWZOKCZ75amDKmjGaBWKL_VuRcwAXAKDO5S3KTV-6KyVWnZwX9805OCeqsnAE1GpOyrItD-bvigg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به زودی احتمالا به Hermes اضافه بشه برای کارای روزمره
😁</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/MatinSenPaii/4268" target="_blank">📅 16:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4267">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">خیلی از بچه‌ها به من ایمیل دادن که متین چه مسیری رفتی؟ یا برای اینکه توی حوزه‌ی ai یا برنامه‌نویسی یا شبکه یا... وارد بشیم چیکار باید بکنیم؟  اولا که خیلی لطف دارید به من، اما من هنوز خودم مشغول یادگیری برنامه‌نویسی و کامپیوتر هستم(که به زودی با کمی اوکی‌تر…</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/MatinSenPaii/4267" target="_blank">📅 07:39 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4266">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4913b2f340.mp4?token=JHzNxSMLt2Wvlr5NjLSYorr_950jnzDS0rbi5-XMZNVjyDraVYY-y8ZIj95LKMpw8TCpkxCBYuYJhpX-2YlqDHYE1EMAf-neHrqPNI_4FJ72d9SWLJG1lda5YTOS3N4HcSdxUbmW3jJNXTgVDgYzxIa8OcT50SfpmiKhPOrCVA1hN2CbsTn6IhfyUuerVBy1wQE7ZFEPlGiV_49PTPktRknliTQJR8WWQRK408vx4ctvXEN6vQLIPB4KrdO4fzMKSSuHPSAJMyt-LhrwkmEMILiFZFLuiTHwAwLJw1V73wzMiaIReUZSti1mKfUlkPtb1IibKhzd3cCKglfTucRagQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4913b2f340.mp4?token=JHzNxSMLt2Wvlr5NjLSYorr_950jnzDS0rbi5-XMZNVjyDraVYY-y8ZIj95LKMpw8TCpkxCBYuYJhpX-2YlqDHYE1EMAf-neHrqPNI_4FJ72d9SWLJG1lda5YTOS3N4HcSdxUbmW3jJNXTgVDgYzxIa8OcT50SfpmiKhPOrCVA1hN2CbsTn6IhfyUuerVBy1wQE7ZFEPlGiV_49PTPktRknliTQJR8WWQRK408vx4ctvXEN6vQLIPB4KrdO4fzMKSSuHPSAJMyt-LhrwkmEMILiFZFLuiTHwAwLJw1V73wzMiaIReUZSti1mKfUlkPtb1IibKhzd3cCKglfTucRagQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه ابزار رایگان رو دارم تست میکنم ببینم هایپی که دور و برش هست اصلا واقعیه یا نه و اون عملکردی که می‌خوام ازش رو با مدل پولی مقایسه می‌کنم، اگه خوب بود بهتون یاد میدم</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/MatinSenPaii/4266" target="_blank">📅 01:27 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4265">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">رفقا
freemodel.dev
گویا api رایگان از claude opus و اینها میده، منتها به هیچ وجه سایت امنی به نظر نمیرسه. استفاده کنید اما نه برای پروژه‌های حساس و چیزی رو در اختیارش نذارید. روی هرمس شخصی و لوکالتون هم ترجیحا نزنید.</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/4265" target="_blank">📅 00:52 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4264">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">متین واقعا باهوشه اولش بهم گفت برو فلان ویدیوم رو تو یوتوب ببین و تمرین کن و وقتی دید اینکارو نمیکنم گفت خب باشه خودم بهت یاد میدم تو کلاس. بعد جلسه اول بهم گف تکلیفم دیدن سه تا از ویدیوهاش و ساختن چیزایی که توشون یاد میده‌ست. و همشو هم باید تا جلسه بعد تحویل…</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/4264" target="_blank">📅 00:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4263">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">متین واقعا باهوشه
اولش بهم گفت برو فلان ویدیوم رو تو یوتوب ببین و تمرین کن و وقتی دید اینکارو نمیکنم گفت خب باشه خودم بهت یاد میدم تو کلاس.
بعد جلسه اول بهم گف تکلیفم دیدن سه تا از ویدیوهاش و ساختن چیزایی که توشون یاد میده‌ست.
و همشو هم باید تا جلسه بعد تحویل بدم</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/4263" target="_blank">📅 00:11 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4262">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">Matin SenPai
pinned «
خیلی از بچه‌ها به من ایمیل دادن که متین چه مسیری رفتی؟ یا برای اینکه توی حوزه‌ی ai یا برنامه‌نویسی یا شبکه یا... وارد بشیم چیکار باید بکنیم؟  اولا که خیلی لطف دارید به من، اما من هنوز خودم مشغول یادگیری برنامه‌نویسی و کامپیوتر هستم(که به زودی با کمی اوکی‌تر…
»</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4262" target="_blank">📅 23:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4261">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">برای نصب کردن 9Router روی سرور اوبونتو اول sudo apt update && sudo apt upgrade -y curl -fsSL https://get.docker.com | sh sudo systemctl enable --now docker و بعدش این دستور رو بزنید docker run -d \\   --name 9router \\   -p 20128:20128 \\   -v "$HOME/.9router:/app/data"…</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/4261" target="_blank">📅 23:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4259">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sSTX_SU8TUcKQLQYUdRMOaLXRT4LC6HgQYjfFU2MxkVnyD4UQeN9Z7B_b7oap2EmKAAl4bzyTFAGJoWFDpSpWh9JA7HteOtlH_TVs1JttzldSSgyIiQ9Ts8S892wMIzqbFvTEfo7phjQaoqTYwMZqWJV3E9R9w-JfGaj7wDn8C9l9_RcoMPN_OZ5AWUb4ohRdhC1A7kQNlBx5hxUD77ROqGdwlThi-bb_4FZqm2tXhR8S7hFLwzroEj5_rHuPaqYRFxbwaQFjuD6hUDRM3suCxMAKCPO29L0OZhEh3-gzlNxnC0ykzw-2GR2bijR0dU9yKVPbKKOpZSvSzvHcl1ECw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ulpuFiaDpoisobgn_RSirwzoRsCArtajFv0cD6egeR_GDIARtA6N_FnKt0BwrXsN51hUHxAEVwyE_QfVUKdLF_flmoBp78vwmZLxVm0BcIU14JxkjP6QX0eDjwadH7p8N_a6tuvx_IlVb5_HcZiPZecDB-OH60YEiNAODg0cMrNTJhSIcnY7iHUFltk0r_kPQIjv045drKam7ZfjUgA5jGO3ib4QShEyCS1817xddjDxMU5o0yRJ25MZ0I34H9N04dkK_7LaUd-P4hjdS7gbJXvmIvcVmvCy3SNOUViGAYMAOhoWSnWXdNbjOdK13jSi9N0fXR6nUbNUVKHM6WBa3g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من عذرخواهی می‌کنم از همگی. حق با شما بود. متاسفانه درست بود و الان برای من هم پولی شدن مدل‌های Mimo روی Nara:) گویا سایتشون باگ داشت فعلا از Open router + Nvidia nemotron استفاده می‌کنیم</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/4259" target="_blank">📅 22:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4258">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">یه ابزار رایگان رو دارم تست میکنم ببینم هایپی که دور و برش هست اصلا واقعیه یا نه و اون عملکردی که می‌خوام ازش رو با مدل پولی مقایسه می‌کنم، اگه خوب بود بهتون یاد میدم</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/MatinSenPaii/4258" target="_blank">📅 22:36 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4257">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">امروز اولین جلسه ی کلاسم با متین برگزار شد و واقعا دوسش داشتم
🌱</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/4257" target="_blank">📅 22:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4256">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">خیلی از بچه‌ها به من ایمیل دادن که متین چه مسیری رفتی؟ یا برای اینکه توی حوزه‌ی ai یا برنامه‌نویسی یا شبکه یا... وارد بشیم چیکار باید بکنیم؟
اولا که خیلی لطف دارید به من، اما من هنوز خودم مشغول یادگیری برنامه‌نویسی و کامپیوتر هستم(که به زودی با کمی اوکی‌تر شدن شرایطم، راجب خود برنامه‌نویسی هم ویدئو داریم) ولی در حدی نمی‌بینم خودمو که بخوام توصیه بکنم جدا؛ دوما در حال حاضر، فعلا خودمو نمی‌تونم هنوز متخصص هیچ حوزه‌ای بدونم. که اصلا بخوام راهنمایی‌ای بکنم توی هر حوزه‌ای. خیلی افراد بهتری از من هستن که بخواید سؤال کنید. اما یه سری نکات رو می‌تونم بهتون بگم که خودم با تجربه بهشون رسیدم و شاید مسیرتون رو کمی کوتاه‌تر کنه:
۱- دنبال پرسیدن مسیر از من و دیگری و این و اون نباشید. اگر توی این چرخه‌ی باطل بیفتید و هی دنبال ویدئوهای مصاحبه‌های آدمای معروف راجب زندگیشون برید مثلا زاکربرگ و بیل‌گیتس و... یا حتی پادکستایی مثل طبقه ۱۶ آقای علوی، هیچوقت نمی‌تونید اون چیزی که دنبالش هستید رو پیدا کنید.
صرفا برای اینکه گوش‌ـتون به یه سری اصطلاحات این حوزه عادت کنه این چنین پادکست‌ها و مصاحبه‌ها رو ببینید.
۲- شما الان AI رو دارید رفقا. می‌تونید به راحتی بپرسید، Roadmap درست کنید برای خودتون، شروع کنید به یادگیری، بعدش هم توی توییتر بیاید و وارد کامیونیتی برنامه‌نویسا/یا هر حوزه‌ای بشید، تایم‌لاینتون رو درست کنید و مشارکت کنید توی بحث‌ها، اشتباه کنید، یاد بگیرید، و...
۳- همیشه حواستون باشه که علاقه‌تون کجا ظاهریه و کجا واقعی. خیلیا هستن که دوست دارن «از اینترنت» یا «با کامپیوتر» یا «با گوشی» پول در بیارن، اما اکثر مردم وقتی واردش میشن تازه میفهمن نیم ساعت هم اعصابشون نمیکشه پشت لپ تاپ بشینن. عجولانه تصمیم نگیرید و راجب مسیری که می‌خواید برید، خوب تحقیق کنید
۴- توی یوتوب خیلیا آموزش‌های خوبی دادن؛ با ترکیبش با ai و مشورت باهاش و کاری که می‌خواید بکنید و هدفتون، می‌تونید به یه جمع‌بندی نهایی برسید و اون موقع هست که تازه می‌تونید نظر یه متخصص(مثلا بکند یا ai engineering یا حتی یوتوبر یا دیزاینر یا فرانت اند) رو بپرسید و اون هم برای صیقل دادن Roadmapـتون هست صرفا، نه اینکه بخواد صفر تا صد آموزشی رو بهتون بده. من هم خودم از خیلی از دوستان توییتر راجب بکند پرسیدم وقتی برنامه‌ام کامل شده بود، بعدش رفتم راه خودم رو ادامه دادم. وسط مسیر هم چند بار چرخید پلنم با پروژه‌های مختلف</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/4256" target="_blank">📅 21:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4254">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/N-CCamLhOJR-8MfhrN6A2pCYUmb-6B8ICDPKuOOPZbjs3I5lGTWcCEr6DXX1M0a8MYz5k7zrIssPxBMc2g4-BnFA42I-PVGPrUbi5Jd9JmmcHfLnTOxw2_b4HBrn5h60yhTgPF2LJVMC6IY_vVzFnq0NAFDYccbjT1cmFc647Pg5Kx9q5uStnynVEUyPundxiV3sOA5bxxQcgUPVvTeRWAgGWrU97zJH-HejSrE2CT_Vd6xTTFC1PaTz9R0cQo-eBat4tXDy9dc_afv7t0qUa9J4n4jwBJr3ruxyhENNczVxVGqGI-oYnOwiq4vz6TvQ7RPX91-qNpl0fIYeGTRJ2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vJDboa8ho3hpb1F_T5dNIrwvQnLNZ9qtFcXDlhXAPOjF3HmR5dzJKPZQQwPrGp5BS0ShrakJAtQJVubgTQVm9y3het_XhE0ks3e1F7pJsICVi_pwrfoBufLK6FXNC9ZURbAt4A90PvExPZ34LOWPdSZE6ljZhhFnSe095JPyCDNIMH1yeLGEFaMEaewNYFJup8-AseFkwg1T-6WNQ8dQn6sP-oSeuPMc9GhXUsQvZRN4ku2m8Mvj5Tbfj0nrWUSntdaoLT2ARMw604i26J0xRpA9J566Bv7ByvHvag8r9VqIQrKWqIVmwv7qEoMnIg3NJMXSmxOGaN_zJrIswfeu6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من عذرخواهی می‌کنم از همگی. حق با شما بود. متاسفانه درست بود و الان برای من هم پولی شدن مدل‌های Mimo روی Nara:) گویا سایتشون باگ داشت
فعلا از Open router + Nvidia nemotron استفاده می‌کنیم</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/MatinSenPaii/4254" target="_blank">📅 21:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4250">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhitednsProxyProfiler-Android-v1.0.7.apk</div>
  <div class="tg-doc-extra">55.4 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4250" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">پروفایلر پروکسی WhiteDNS نسخه ۱.۰.۷
🛠
پروفایلر پروکسی WhiteDNS یک ابزار تشخیصی برای ویندوز و اندروید است که بهترین ترکیب‌های پروتکل پروکسی/VPN را در یک شبکه پیدا می‌کند. این ابزار می‌تواند هم بررسی‌های محلی بدون VPS و هم تأییدات عمیق‌تر مبتنی بر VPS را اجرا کند.
🌐
ویژگی‌های اصلی
اسکن شبکه محلی:
آزمایش سریع بدون نیاز به اعتبارنامه‌های VPS.
🏠
اسکن VPS:
تأیید از راه دور عمیق‌تر با استفاده از اعتبارنامه‌های VPS شما.
🖥
تست پروتکل‌های VLESS، VMess، Trojan، Shadowsocks، WireGuard، Hysteria و HTTP.
🚀
پشتیبانی از انتقال‌های TCP/RAW، WebSocket، gRPC، XHTTP، HTTPUpgrade و mKCP.
🔄
پشتیبانی از ترکیب‌های TLS، REALITY و بدون امنیت (در صورت معتبر بودن).
🔒
تشخیص دسترسی‌پذیری، فیلترینگ، پورت‌های مسدود شده، مشکلات SNI/TLS و رفتارهای شبیه DPI.
🔍
نمایش نتایج تشخیصی دقیق و اطمینان از شواهد محلی.
📊
کمک به شناسایی ترکیب‌های ایمن‌تر پروتکل، پورت، انتقال و امنیت.
🛡
نحوه استفاده
برای یک آزمایش سریع بدون VPS، گزینه
اسکن شبکه محلی
را انتخاب کنید.
⚡️
از
تنظیمات پیشرفته
برای تست پروتکل‌ها، پورت‌ها، مقادیر SNI، انتقال‌ها و انواع امنیتی بیشتر استفاده کنید.
⚙️
وقتی به شواهد قوی‌تر سمت سرور نیاز دارید، گزینه
اسکن VPS
را انتخاب کنید.
🌍
آی‌پی VPS، پورت SSH، نام کاربری و رمز عبور یا کلید SSH خود را وارد کنید.
🔑
اسکن را شروع کنید و پروفایل پیشنهادی کارآمد یا نتایج تشخیصی را بررسی کنید.
✅
نکته مهم
اسکن محلی نشان می‌دهد که شبکه فعلی شما به چه مواردی دسترسی دارد. اسکن VPS شواهد قوی‌تری ارائه می‌دهد زیرا هم سمت کلاینت و هم آنچه واقعاً به VPS می‌رسد را بررسی می‌کند.
🧐
نسخه:
۱.۰.۷
🏷
@WhiteDNS</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/MatinSenPaii/4250" target="_blank">📅 21:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4249">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">بهم یاد داد از این وبسایت‌ها برای جزوه‌ها و تحقیقاتم درست کنم</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/MatinSenPaii/4249" target="_blank">📅 20:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4243">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kN9QGSnuQ9CfWmqKI34dyWrJ44K_3caBk_R4L0A-rK2KQF9EZf2aVb1pVB150g6_GSvgm6rtHhRZzt_gXnmBrburm-P0LrsGVmf7Zj7KlTlq1_OaZJM3MzpTztqAe3jwPX-d4fSHQN4hiOmjy7llYX48vbmRuEavjGyCru4gM2-P6AEcP20gfW10Nyl44FNE5NMLuou-UoXGJ87xcfTGVo734Jhtu3nlBfCpIV-69IVa-kpJ6fCLGpPHcomBHOVeCTy3VXrodmrb6x5U8xLMXXVejWsZQJVeoluTtcUT0IqXi-v0wngWhM63yrr2uPdNnTwUgIJY04udeR3lWTTboQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/e1ji2jYRoVJI4Vsxpw4wtyy5qG6G3cWbxjN2yPlMvgzLoZo8lY6fP0t3jQRrhjJ4J3YivTu0O9F2MFmBuuupg9WiRUt_humyNkOO0jgg-uXbu-EImsvAuMA8Njr2fTtsgDIsbj9qaQemLumQcIJ5p9p21aAWbcr9mSVr8HIGzy727nQME2MaD1ilRlj_ysBMReoH_v6PeQN3SZK77SNTECskaUcNlYkPh1-dQK230o1f-L2qEcdsNgNqVnJnoAbevjjBedh-iooxToYO-Affir0Aca4zCji6sXcY3A5oVdAzGnK8g_TTDMVe2kjA4uBs-gxU6BFOWXEFFarXsgfFYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/i3D-IeQ0yd-Jv47tnFh74Pa41pPiTr5nLC7EfVgpicWdAt-Qdx1MhJxvUN8kt2KnF4_ldP7ks5_X-Whsm5HfvM1FKehq-25_T4Vhe9i4Swt7r0aXBWkhsiWvxiQVZ3bdiMN1hLZ16nem4BbeE3DjcUpW0viMq_pbobQsbYwwsyxrSv4ZLTpmN2CVU_kmePx22k11YGTJxC_RtZ80E0c6V9hII3XHp_TqNCzXO_jLCYBSlOv_7JQiLrG5_p7lUjEFzt-vk3BEo1u9aOT9MaJHUFxmkt4i_BMyejuhibWXwg0PVSznOf2VhDtzPmwmjdA_qeaHfyqD_oh7B9AUp1vLNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nTg-BsxUBBPPvwd3BmqGZOK32DoPlRoXbhsVNNMQiJElE37-FJGLbVvdAOQXw1PD686R5LeAaQ0pG6hDMB-PZlw0byYITIV_-gJlkmazmsUNVM28kotx8eXjBe5mA65ywLta8ob4UtDSHOA_qLp1ootz5QZ7Xxnk0ImFewQOy09X8fC4ONjojviV7JifzUdZJDdtkwVW2U9IcjxN7ObYuBUqqQfCisZIss56LslM0FRLelFnMswo_CVb7ekFn6W1uLdrbaFZdnyu2akSVswPIJpQJP365kQtGnz8gP1FssMyEaj2ZbqRl5w6prMvInBDoSNfHBE2ujfB9OcUnRLzSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MCTIWWCHh7jTp0mc2Cd_ik3Z8tGP9YoiflUhGssQ_dRfy3oAP8NxYVTieSFaBsw1EH87SZ9uQBDN1xiEE2CURXd_14MOY50URf9P3KwYpwoObXPER3pk98vx31DE17qg7voQbWlebQygSD6MvG-EKhjs5NRb3U9y-TZjwxJeM47Ll2RRCH1zGBwZDIREPmLs-EO6-X4lrQbMqlz1AzlstZFISa5NOOGM1F8hUvlpf_gqcPbtUr22cFQWNijEjivxjVVVR_XKeKA-GHMSA9rVWMLwnsF2ziyV4IeAEc4n0Jh2iG4EoRuVcydWuA9NS7OH6jkfYO5avhQdtXyQ5lb9fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YGJwKGTr_nrcoLmLt8ZKSj0Lr3M1XlkSBF0bL5BABXC2H6rGg7ZbOSDCR9Xsat3E1Imh6Lpc_KxZA9iIN7K_psbE-ft_aEM8gT-yw_Fiy8t9FHO4O-bxSpt2HRuCs9hlkAPsfzv0NcLbrdUWwGmCzM0SRgDoXN2qBqMH-PSpgwAF54JdR8DM-PTrkmU9AmBmSztQze8MGHorrNUuc_wcKSsmkmutz_hOwfTCCL6y3t234TObBzLBb8FCYeRhaKCXsKaOuYzKMA9i4xSf1EuNKVHzCopRW7y1OHHCP_Zry5zbBWcGBAz8KVW4ZxpWvtZ-plxWD4XpSmQjbGhpTQhpKQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تیم مهسا توی آپدیت جدید، یه صفای حسابی به UI دادن
😁
اما UI کوچیکترین بخش اپ هست که عالی شده.
۱- هسته‌ی سایفون برای ایران بهینه شده و به راحتی تمام، وصل میشه(الان با همون پیام میدم)
۲- اسکنر قدرتمند اضافه شده برای اسکن آیپی cdn_fronting
۳- الان میتونید از سایفون+آیپی تمیزتون، کانفیگ بسازید. مثلا من اینو ساختم با لوکیشن آمریکا:
psiphon://?region=US&protocol=cdn_fronting&aggressive=ON&cdn_type=any&cdn_ips=
104.16.73.68
%2C104.18.180.6&cdn_sni=
pypi.org
&no_sni=false&skip_cert=true&proto_tls=true&proto_http=true&proto_quic=true&builtin=true#psiphon+2026-07-05+20%3A26%3A39
۴- یه منو کامل برای Chain کردن دوتا کانفیگ V2ray(مثلا یه کانفیگ آمریکا دارید که کار نمیکنه، یه کلودفلر دارید که کار میکنه. با کلودفلره وصل میشید به آمریکا و آمریکا VPN نهاییتون میشه)</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/4243" target="_blank">📅 20:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4242">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">کتاب کامپایلرها و طراحی زبان - Introduction to Compilers and Language Design
اگر دوست دارید بدونید زیر پوست زبان‌های برنامه‌نویسی چی می‌گذره و کامپایلرها چطوری کار می‌کنن، این کتاب آنلاین یه منبع رایگان و عالی برای شروع طراحی زبان و درک کامپایلرهاست. خوندنش برای عمیق‌تر شدن تو مفاهیم پایه‌ای سیستم‌ها خیلی بهتون کمک می‌کنه:
https://dthain.github.io/books/compiler/
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/MatinSenPaii/4242" target="_blank">📅 20:12 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4241">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">تعداد پنل‌های وی پی ان بر پایه‌ی کلودفلر کم کم از تعداد کاربرا بیشتر میشه
همشونم شبیه هستن تقریبا. زیاد فرقی ندارن با همدیگه</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/4241" target="_blank">📅 19:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4240">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">بالاخره کار مقدمات و آموزشا تمومه
کم کم توی ویدئوها میریم سمت ساختن پروژه‌های واقعی</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/4240" target="_blank">📅 18:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4239">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X2DlIBYsRD6hNJuHJeMgeofget6g7ORQjfaTfP7cf9QbA5PfLrXGnCSt3GHcZGtx5iSJx2SoWdt6dtympEkT2fu3Ptn12UGyv70NswvQDxegFkar6oHUemDbkwMB3Xk4U3Bl2-Xf1OXPerb0s8YzybbjaqovVB7bV6CmsmGptRR2JsPF_NOhbZJVyoNugRvVZDSemjcM1XOdyJQJsjnQhOuk_RJaPVMCs9FbvDNPwFUcHP1QdCDTG0UBMh0DQzAYAQSB53Vw0nNenpnguURvdmt8UVeJYJu572zyWOJ4nSFbB1SUZZZ1634DS-oDX0yrebhYwDgLAuf5PiNHGlIhQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز Hacker News رو چک کردم، یه سورس تو گیت‌هاب ترند شده که پرامپت‌ها و ساختار دقیقی که برای Design System با مدل Claude استفاده می‌شه رو افشا کرده. برای کسایی که می‌خوان از AI برای ساخت سریع UI کامپوننت‌های یکپارچه و سیستم‌دیزاین استفاده کنن، این ریپازیتوری عالیه. با دستور /learn بدیدش به هرمس و تمام.
گیتهاب پروژه:
https://github.com/Trystan-SA/claude-design-system-prompt
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/4239" target="_blank">📅 17:49 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4237">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/e-Lx2kpHFnAoG5xt43EJlLUuhohxku0YE9GkL2GxgrqRk-z_b9qmI4qv3WRuPCd3W9TDNzMMgZ0SPgnXGo6uCDOEgRZ9NSPi8v6cSMfovrPT7HA08P1aX-sq4VYUcV8fIGXY2TuKguRx-ck8XsqUySE_HDBS3HYnNk-hUr1kr4PicqmDNZfgE8zggJ1oCtiPigVw-1F6fJ-DNiqOVyGEK1ayyZsnnTCqZ8JkG9N-rdnGtXz4WQ565MzAP7zpkYfTl9EHzNaiShEMFQx7mfcvfww98Iqeu9ZYO3XCZlYNrPmv8AHL1ACAhlKBETY9DcNIZ7rffdsr0pSFmvtcEx9mJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YMJFUCBXLNsaf2ShQZibQ1m9Jbs5-vKmrJb6OI2bqjOmbP9c4XBFXZ_yQDfSG9szJ4CEHu7UDK-myK8NqVmAw-OJX1v1FDRGRAS_z6y6NbjDZHVuut_PX2R8BDaf8-6hG8fEglBTopxnNnA_vuvQZgMa_qqtkecEVah2lMBYJy4d7C070vG81XTS38aIekKELIz-DG_WIZQMFWcVhSGB1_GXbnWBKza-RlN7JnOI6-0fgtTFMMwSi0Bw6VJ7EEbUe3AVGLSUBDdDVjlnvfNI5uXakWCLT-pR5Eh4IFv8ssgJzEy5fqNkrPnqMKI_2e2-d4MMpoVfoWxYgW6Ka80WBg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یه سری از دوستان کامنت گذاشته بودنکه این api nara که پولیه و کردیت می‌خواد و فلان.
سایت Nara چندین تا مدل mimo داره
که همین الان یه اکانت جدید ساختم و مجدد تونستم با api key اش به mimo 2.5 وصل بشم
شما صد درصد از چیزی غیر از mimo 2.5 (mimo hermes , ...) استفاده کردید</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/4237" target="_blank">📅 15:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4236">
<div class="tg-post-header">📌 پیام #31</div>
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
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/4236" target="_blank">📅 04:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4235">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XcCYlreFdXfMRmuCrJXVmEkw-JKZxY8mVh4R88nddhWEZUKWIwql02EcAYBC7kpw0S-5VrcHaeKTw5EhZQNvV2ZBCtvSZGyIWQ6QGncoKSravW-_QDry4Y21jIQykgc3ZJcLDZlnKCIdNYr5ffA_3rv_ZdcHpm1zCrHnpVdK8OhC1IJMFOvWsAEV-1DUOn-Mubx1BJPXxWOmDH2dLSIMLLOPHJ4JABHxHSkmsNIX538kLg84ZZv_Jybw0DcffxRTgbU0M9PKEzsGQaUvurzephTnmqXy64jYME9k732xVvNGmkR4FoSYOxRLUF36HLT857cH-8O6f1GjZNgjaKkjqw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/4235" target="_blank">📅 04:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4234">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">دانش و پیشرفت علمی، پیش از هر چیز، به پذیرش نیاز دارد. دنیای علم آن‌قدر گسترده و پیچیده است که با ورود به آن، با انبوهی از اطلاعات و دیدگاه‌ها روبه‌رو می‌شویم؛ دیدگاه‌هایی که گاهی با باورها و عقاید ما همسو نیستند. اما اگر ظرفیت پذیرش در ما وجود نداشته باشد،…</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/4234" target="_blank">📅 02:11 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4233">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBloom.(Tin.)</strong></div>
<div class="tg-text">دانش و پیشرفت علمی، پیش از هر چیز، به پذیرش نیاز دارد. دنیای علم آن‌قدر گسترده و پیچیده است که با ورود به آن، با انبوهی از اطلاعات و دیدگاه‌ها روبه‌رو می‌شویم؛ دیدگاه‌هایی که گاهی با باورها و عقاید ما همسو نیستند.
اما اگر ظرفیت پذیرش در ما وجود نداشته باشد، توانایی درک حقیقت را نیز از دست می‌دهیم؛ به‌ویژه زمانی که حقیقت برخلاف باورهای ما باشد.
در نتیجه، از جایی که گاردهای شخصی و تعصبات وارد میدان می‌شوند، گفت‌وگوی علمی عملاً پایان می‌یابد. علم زمانی رشد می‌کند که ذهن، پیش از هر چیز، آماده شنیدن، اندیشیدن و پذیرش شواهد باشد.</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/4233" target="_blank">📅 00:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4232">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/509058c8eb.mp4?token=ehh3TlkbkGBe2jbZ5_xh5eR24W66OfcIyOaCjIr0PfrwDGQdVHnSRfqL28DS0ENOly99Nse4na2fSYOVtA2w_z1FiGIk1wTh55BhW_3KGblb-V0UWmKOLyIvgdY3vAWjyoTrZcDBpBTNlsaDdLOK4qXOszWzvOxr_9HFy7B6NP33nX4K1sNBFjnhoBzde31pA-jCzG3xyUhRrWp90R_K7tLdbKz4kVBLcIxNFrXFoo_xW3WtaiO3IJRacFkEvfiUrSYQoKmjVbzJf-UF1S3F6VqKdKqfFMjTPH9dxhNmyPaZkEoPsiT5a9NcCuxYRJa8M3fXwkncOmZeLs88AyiwOw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/509058c8eb.mp4?token=ehh3TlkbkGBe2jbZ5_xh5eR24W66OfcIyOaCjIr0PfrwDGQdVHnSRfqL28DS0ENOly99Nse4na2fSYOVtA2w_z1FiGIk1wTh55BhW_3KGblb-V0UWmKOLyIvgdY3vAWjyoTrZcDBpBTNlsaDdLOK4qXOszWzvOxr_9HFy7B6NP33nX4K1sNBFjnhoBzde31pA-jCzG3xyUhRrWp90R_K7tLdbKz4kVBLcIxNFrXFoo_xW3WtaiO3IJRacFkEvfiUrSYQoKmjVbzJf-UF1S3F6VqKdKqfFMjTPH9dxhNmyPaZkEoPsiT5a9NcCuxYRJa8M3fXwkncOmZeLs88AyiwOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاید براتون عجیب باشه ولی من خوشم میاد وسط ویدئو به ارور بخورم و بهتون نشون بدم که ارور ترس نداره و میشه خیلی راحت، راه جایگزین پیدا کرد
👍</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/4232" target="_blank">📅 23:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4231">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bt8txDRH11ub_sYqeQ6wpMif_u50OJqiOzGF5630l7O-bQQlAp67vqiX4Goy1MtCMllPSUXleK4Cl3yFK3GukoUX8vpT84EPYAuVlYkl9jiUTn6VGsjqtq_QRkpJayDvtjtOAx0sikrLrRYlFpsT392b3W3uZomn4J2UQpZFFI4TKXGkpNkdIdsrAvBpT1pGlga0qTqkjbO2hmo1quGeDILzj9hc2HIUHNZbesVqtQP1yFwN_KzFLIh3A82x0SicBya1oPRSxf9y4v0s3qTIvrULGjqP5SEM6cBoluQhdrv-YA8i3MzQtpAcO3iSiFpT3u5_WTCkl3L9v2BFPpRSQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر، قابلیت Deploy کردن پروژه‌ی جدید رو برای اکانت‌هایی که با سرویس ایمیل‌هایی مثل Atomic mail ساخته شدن، غیرفعال کرده.  با جیمیل اکانت بسازید موقتا. شاید پرووایدر دیگه‌ای تونستم پیدا کنم که راحت بشه ایمیل ساخت که کلودفلر گیر نده</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/4231" target="_blank">📅 23:25 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4230">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hJjMY9ek29B0ThiLtJTCXAFG18nbZcEhcuEHDJgdFWxU7fJ74ZjyDfk1BgQoePhVmQp47Fc6K8HlENWh4CPECXdIpDe2hbEQzfQHGlKVEpe2Sy4jM0j3wcH6O20XtLNlT0-WhJ_Z6ZwMVuQcuvLQ5fX2znqSQMOGqrUjf2MIVVFPf2Cz7C3yhk7bNl16ek3lq4vP42zCwYUEA3Nhvdp7UEh8sXaSSHZkjyHEIBIGCHyb-d3YQFspaKtTf58hHpufGE9QKdTffLqebotskRiTzRoghcWNyyIapsg67uEuU8CCe5ZstCaQwwMs_Ekek6IFY7fXfUvqqzcM48cvLFxPLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر، قابلیت Deploy کردن پروژه‌ی جدید رو برای اکانت‌هایی که با سرویس ایمیل‌هایی مثل Atomic mail ساخته شدن، غیرفعال کرده.
با جیمیل اکانت بسازید موقتا. شاید پرووایدر دیگه‌ای تونستم پیدا کنم که راحت بشه ایمیل ساخت که کلودفلر گیر نده</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/4230" target="_blank">📅 22:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4229">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">روش فارسی نوشتن درست و حسابی بدون به هم ریختگی هم توی ترمینال یاد میدم توی ویدئو. که یکی از دوستان عزیز توییتری دیشب بهم یاد دادن</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/4229" target="_blank">📅 21:06 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4228">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">توی این ویدئو که دارم ادیتش میکنم، کلا با cli پیش رفتیم و از اپ دسکتاپ استفاده نکردم برای هرمس. علتش هم اینه که پروایدر شخصی اضافه کردن روش هنوز داستان داره و محیطش پر از باگه همچنان. با اینکه آپدیت هم کردم الان هنوز همونه</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/4228" target="_blank">📅 21:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4227">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🛡
آموزش کامل نصب و راه‌اندازی سرویس MTProto با ابزار MTProxy  فیلترشکن قوی و پرسرعت برای تلگرام    https://www.youtube.com/watch?v=pyvB6VSPhwg   @WhiteDNS</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/4227" target="_blank">📅 20:54 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4226">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🛡
آموزش کامل نصب و راه‌اندازی سرویس MTProto با ابزار MTProxy
فیلترشکن قوی و پرسرعت برای تلگرام
https://www.youtube.com/watch?v=pyvB6VSPhwg
@WhiteDNS</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/MatinSenPaii/4226" target="_blank">📅 20:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4220">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sIwci43bj1HGhwZJBzwQHLK_OUuXTBgu9OGVjS8WyoTD2Y8P6cGAomI5fZDuz6l5Uhn_QtwD_wcDU7rHeLeewUlWSigWd6ypsR5WNoPV_pQf-dRKZmv3DPy34wdK9dwaJ-TEjic7yVcZsK06MR3X6PPEEykbCIPCcZKHoiYnLfq2xxZcRTuzYbQySjmuVUNKWkQ_hLybbt7vKyrPrs0qAkxaj4vVgEtcdTNBbadYRtBhS5eqnG4xkVUbi8PJMcWm2IT4GLrUhD_K10NWY_mynt2HFLA1fQZ2vHZGuR945l2l1oap1l9-Qryd539Ut_cLLCToOk0yAmLi_iGGBHshtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nUKZUiPEf0piUsj2Ds2ihk2vBUWO0EqOpqgkHgIuzZe3RJJ2QhfsJbfyhnfit_VeahNToHj9uFD5_cMzS9xWGasPKXTY4ZKLADb5M34yOIPWX9xIwHESFTdYcg1eopxD4qpxquZtJlllOgQsLyoalrR6oUtWqFiDz2ZzXAVCYTyiNyB7IaVI_iGa3wP8ocOvpp6fyStFc836AkY5X9zrKLixUeom9ikzr01yF8r3czcTWLflDdHDXAFcnTlUoz9ae79m9HkZGvBraA7Kml7RD8mZDtTHT5nIH2vl_6hFF7ZNSuBDl3GYM6_DV5T_ajl8bPITHIVfWFnhKCr2tc820g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rEZhEFhRURW1XzGQZg1wJEjOtsGsG57yyIjQPxNRUOV8kj85LrKLw1-Xpn_sl53jEZBRzCSrNGuPfXgqfI3kKDqmBvJdbZtPvoslNPXqARrdn9Kx77N1Jl0XAxbTTUn0AeLnIDnPU7B7CqTuhnkCWqghmNCR-l5Y8jZkUg83bcDyUIvSXckEcG7BFrm1HXcUywrJoAT2tFVTlEDq30AKWEcserhHk0V4q_Ilh6-QKffDww5Qa0z3nE1JHWvSLsKsW2jC2G8M8DvAhiZtB1e_r9SqATcjRPiU3tXeUqO0BULqe_pDfc52aPN6h_FMERWIc5YNSbX12CNuHt9rWcRM4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/v7IiSbggZOXY4w7sijUbyQYiJEDoL8JUcXpIN4-yp43MFETOl28aqbdzn1Qdxv-TyZ4MKhZn7ybAXXRlFPrAGdAzLNUX8MfgdiIRTUNNRn86qdEkXPW1gpjMKXYJYfoE0m1hULvGLhPjI8vNDPe0gZ3mmHfHIPFUp650BdrQHAJZ7tOL0YimpyOuLtrJUSe12au1dNJIMcg7A4wNaf3e3gp-z1U2eRdBQB_aWMbDihtml0KMQDbXOialxftzhGx3jo8pMA0_K6tdPxlNlnSF9FRdUu09LvRJ2mdrJ7xb6PEg9RC1c6UTG4lYuz2CA1RhTIkMTdp9sspP9Z6mtat68Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qpQiByIPjd1cmkKZjG2i6L8CmiajRaBn9A0svmNHNHokKMYcDMGUQx2l7GDghZGTIKX9Jm3Cw2yBHhSBp9GIGZShZ2ZTdzQak-8qsuHz0TEHGC7wO0sjzxGipyMwlJUtyF_ZVivBhKKRZYs0inJNHjSNDZR6taPfvPiFaJLjRxIC9mdyiAvlp4HrvP_lqMQM2qcvfHlsJm6o8Q8jTN0b9R-JqZr0bglywyZViF0LHzcpTLFeSKJMlCjt0AaIhubo7Oy-8KjIHYb11s5MXgQvR4Kuq_Hc8X8TBGeKv2tlc8GwMoxSumOmdypRGFoVpayTBaG4JRfcd9eDDyoxZr-WTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fBgk8mzgswN-k0lvEYvcIStiC_RLAlG96TfPM4A8GSqAqc4TvmZYmRmXpIEtAShAzDB61kTBVuyK2q9tGSSaTMUgF8QER9kt89Evm6Ju1VtNBJ8PjwPevH0AWZgYUfS3JfwmNtdnHXGJsqZpQ6MAcuJngtnJWoSqtMQZabpLIdo05bwphNgkpA39F1vfKASeOWEYz_eRp0Gh5Y6TjKmCZLq7q5Yt00D63G_J6WADcy_ZnyOlm29sgt-VG-_oyCSoWJY-7DtmUP0-d6B66WQm9RtEmM_mFud8UIqXOs-Ogc2vvpV4WZeMkJKYtoW5B55DQpW1DWMZTPV4lXSBMgaIoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">راجب این هایپی که در مورد «ادیت ویدئوی بلند با هوش مصنوعی» راه افتاده چندتا نکته می‌گم و دانشم رو از ۵-۶ تا ویدئویی که تا الان دیدم باهاتون به اشتراک می‌ذارم:  1- نه. اگر دنبال جواب مستقیم و سر راست هستید، هنوز نه. هنوز توانایی این رو نداره که با هزینه‌ی کم،…</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/4220" target="_blank">📅 20:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4219">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V4Vim2vp59N2JIcz_bKQKvkGS1-q9LxSaZbWYT8Y_rh-NPwLt1FBPpKHgInJXQpAmxzmSSJi7RdAr7mdoxdSfjLfbx2AewDwcAv2b25HLFlYzVuDB_c5UB899w-hAVmdp3jqaurHR95F3tmYFlBrTS0nRWtMoZRyDBHess_snILXk168BMI6YBUTOn-sjoUA_mtOXKXJCGcNn_XM7IJQQfwIXZ5J04K3i2tL95yyeMS0n9Y2KMKZhO2p88wWJrPHplB1QsPC5hkjOn4k3BKBjdTNptmH1pvIcLehMcF5Kdv3vIneUgCdkIoUGnHsSVz4qrxzREZt6r5Zb037yZFVPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راجب این هایپی که در مورد «ادیت ویدئوی بلند با هوش مصنوعی» راه افتاده چندتا نکته می‌گم و دانشم رو از ۵-۶ تا ویدئویی که تا الان دیدم باهاتون به اشتراک می‌ذارم:
1- نه. اگر دنبال جواب مستقیم و سر راست هستید، هنوز نه. هنوز توانایی این رو نداره که با هزینه‌ی کم، بدون اعصاب‌خوردی و بدون زمان زیاد اون کاری که ما می‌خوایم رو انجام بده.
2- چیزی که من از ویدئوهای این دوستان عزیزمون فهمیدم توی یوتوب، اینه که میان با مدل Whisper و یه انجین شروع می‌کنن به کات زدن(که همون هم پر از اشکاله و نیاز به ادیت فراوان داره) و بعدش شروع می‌کنه با یه سری mcp و یا پلاگین کلاد کد که اونها هم اکثرا نیاز به api key پولی یا اشتراک دارن(کما اینکه خود کلاد کد هم نیاز به اشتراک داره) یا یه سری ها هم با Hyperframe، واستون موشن گرافیک می‌ذارن.
3- حتی همین موشن گرافیک‌ها و... هم باید قشنگ و دقیق بهش پرامپت بدید. این نیست که خودش متوجه بشه و این کار رو بکنه. همینطور توی این ویدئویی که تام‌نیلش رو گذاشتم، طرف برمیداره کلاد کد رو اگر درست یادم باشه با Opus 4.8 می‌ذاره روی Extera High effort که خب توکن بسیار زیادی هم می‌بره و فقط ۴۸ ثانیه‌ی اول ویدئو رو باهاش ادیت می‌زنه(بقیه‌اش رو داده ادیتورش
😂
خب مرد حسابی، واقعیت رو بگو دیگه. که مابقی ویدئو رو دادی ادیتور خودت ادیت بزنه)
4- هایپ اطراف برنامه‌نویسی هم زیاد بود، و تا حدودی تبدیل به واقعیت شد و الان ai سرعت برنامه‌نویسی رو بیشتر کرده. پس شاید بتونیم انتظار داشته باشیم توی آینده‌ی نزدیک، با هزینه‌ی کم و یه اشتراک معقول، زحمت ادیت رو از روی دوش ادیتورها برداره. ولی جایگزینی رو بعید می‌دونم</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/4219" target="_blank">📅 19:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4218">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">کاربردش می‌تونه اینا باشه:
۱- وقتی دوست دارید هر چیزی رو بگید و در لحظه کامپیوترتون تایپ کنه
۲- یه ایجنت لایو با Hermes بسازید
۳- و کلا کاربرد عمومی. مخصوصا برای کسایی که disability حرکتی دارن و مثل خودم توان تایپ کردن زیاد رو ندارن</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/4218" target="_blank">📅 19:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4217">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">چند روزه می‌بینم همه دارن در مورد whisper حرف میزنن. خواستم بگم یه ساله برای تبدیل گفتار به متن از Handy استفاده می‌کنم و واقعاً بی‌رقیبه. کاملاً آفلاین با پشتیبانی دقیق از فارسی. حرف زدن با کامپیوترو خیلی ساده می‌کنه. github.com/cjpais/handy‎  فقط کافیه شورتکات…</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/4217" target="_blank">📅 18:57 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4216">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/geOejz_f523MX5-qYMrOguOM0DU-fiDujyfJPuG9kQIzqJSL2R0dCayU7YGiskzdXCGt6p0GiO95yRWbesZUXT-K8OUftIguBf9QAQgM9MXa-1gcV01TbxCPZj2qQx7P3y5QZqW5s_eqR3kSyx1ItYCeePLO2xFGW3lx8y5cccT0-uVEUzrMbzzENoRj3ctadH9QebnFhxdJYpjJ-YGyTmJMuud19fs5ezcHNEBzIyVYMv-DVVkHYgSDqP4YG1pkBXCcp566XAD6EuoWB3aA7fp9tkdrGS6ZiwiXZPPxRqqwpVpCX7YkWib5H8ajQSC3nFPUVhR9hQLhGPYsJjQ0FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چند روزه می‌بینم همه دارن در مورد whisper حرف میزنن. خواستم بگم یه ساله برای تبدیل گفتار به متن از Handy استفاده می‌کنم و واقعاً بی‌رقیبه.
کاملاً آفلاین با پشتیبانی دقیق از فارسی. حرف زدن با کامپیوترو خیلی ساده می‌کنه.
github.com/cjpais/handy
‎
فقط کافیه شورتکات رو نگه‌ دارید، صحبت کنید و رها کنید تا براتون تایپ کنه.
اگر دنبال یه ابزار STT بی‌دردسر و رایگان برای لینوکس، مک یا ویندوز هستید، حتماً تستش کنید.
✍️
apt_hq</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/4216" target="_blank">📅 18:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4215">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fAJOz49cP2aZMGHM2iRozrETGdjbI2xdLs5CJLbxsIxRqzWb_8e7AuA7PvmCU-hK2hTO3IiqzU20A7eC7VeURE1p8CwfSZ9BOKzsNB2uqFCGxfGq9XlW_GY1rnFKV-VQ49MPzqvKdaBOlrCFZBn8CzDHT4m2_bIKD3yhZ9tkFG81vKC5FyQOsiqF1G2888aQ6HlWersLdZQowRLs16ZwRRgUN13Y6inRdFDbD0RZPMdHRS02Bp8isHk_qX5deAk4ikA4dkUbx4E-oDHBZdRcdiozjT-s2-uYNJ-k0E_alhmnOTb2xp1IzuCkUIrqKJxmMx6uHZ8BBvhc-9iDP10ajQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا به دادم برسه
3 ساعت و نیم شد ضبطش
😭
😭
از بس دستورات هرمس زیاد بود یا طول میکشید(کل ویدئو رو با api رایگان رفتم بدون سرور و... و واقعا هم خوب بود) و قلق داشت انقد شد
اما ادیتش کنم ۲۰-۳۰ دقیقه بیشتر نمیشه</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/4215" target="_blank">📅 17:36 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4214">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">برای مثال کیوریتور (Curator) که توی ویدئو توضیحش میدم، یه جورایی کتابدار هرمسه که تو پس‌زمینه سیستم بی‌سروصدا کار می‌کنه.
و Skill هایی که خیلی وقته استفاده نکردید رو پیدا می‌کنه و آرشیو می‌کنه تا سیستم سنگین نشه.
ویدئو پره از اینجور دستورات و همه رو هم تک به تک انجام میدم و تست میکنم و صرفا روخوانی نیست</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/MatinSenPaii/4214" target="_blank">📅 16:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4213">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">هرمس قشنگ یه کارمند تمام وقته. ویدئویی که تا آخر شب می‌ذارم رو حتما ببینید، تا بتونید از تمام پتانسیلش استفاده کنید</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/4213" target="_blank">📅 16:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4212">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">به زودی یه ویدئو داریم برای تمام دستورات ریز و درشت Hermes</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/MatinSenPaii/4212" target="_blank">📅 12:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4211">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">به زودی یه ویدئو داریم برای تمام دستورات ریز و درشت Hermes</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/MatinSenPaii/4211" target="_blank">📅 12:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4210">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r5Q4_6oUhvFf_xEOOqVVxaRUd_JCBjy02Ujh7sW9J0ITywM5Ogfingrpda3lCP4d3xippkDVvurAqW0gM-2wFSE4PBorqh9yk8XkMW6054xcuZeHO18ReZ5qqBDOyCBNxNuydm_EZ1oS31X8DKsNAEQyg8HWlYZB39h3SQ1E6HHannXmN9Sq_O4KdniSzCDw-VgY2L8AJJ2pbjRlNLnUyXxo6z8Fg223ncx0TBBxalW_HPRyqchKmGD4-zvsAHlbnxZC2wNR7fn1-N3Hl-Xaqw7JnZUlI59tKmgYI5Bj6K6q7PNgQvbNYR7MPzK7uKmklgeHlIIJqrOprXAn4mphag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این داستان، ایرانی بودن</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/MatinSenPaii/4210" target="_blank">📅 01:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4207">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pGlsiDeBHNYT60o0znPPcmC6xX9j-2F9ogOSXCwLzH-T9lHTYx22F4bXgGK0au2hJRMSp6BOl5uv9z1G1-J9O0d9oNVKDo6GpRZaYZhn7CiAmUcRqsZCL3wUVT3f1o5-UkC8dRMGl3DSJ1Feh0Z2LoZ-cBRJ-s3AFSMb29_nodwv_xPkAZWJ_6KXQ-WYuuZPSXxEYXo2-UMGU4lvZWshZHCw5itmRdittfnWUYPvdbdm2F9ngl7Q3mE5CanbpksS5p9obVvrlyb0uK3eoUXVshYlvPnKLOlDhtF00a_VSqbvT_bz--XF1AXJOhWXXomQ0ka0egWTW_g1gvYDghTYuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YTZgWrff0x8rjidkjsglKUTd0rUsDYg1kgr5aiEDV9-Nvjic_jKGp9-8xdNcQ7qjCphDzXifLL94_gZp5KaNmpP84f6AJiL7WlF7Z4CckJlKiwMMx5rJGi0FupB_SocTcWVib3GQmlvrPdF3mEEq8Uondy2FiqmDQIeLIHANbxtwIrNtsGfyaaQH3z4E-qHDzq4Dbp9M88oxYvmWC6GF2N8cuwg9rpBPN7-RPmGx3WHNJVZ3sZcWpmFF7Kw7J68RGHx1-S4IR29S3Hqa93B0yiNygRittVOaKkK3yUIxFzfwrmH7MXLl2tG59FngNCvnfqmXEqUNpvjY9yay_YMZWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tUTb3bX49TlnuZH4uHfzsx4cCAV72i-o6hx-p58TOKM3sqbwYwkKXzkj41umyx0bzkdAbKEiLvoe6NEU3fnvqjNPy4yO0EVbGI7IHsZ6TcmBuSV3aHrmCj2R5GmqsPOwpSjZU5pw9wojqHEsrzBfExS0MtTrVeq_Ifp3aOzRtoH5uOlIK7-GQy-Z6cL0V7i8pKMS7PEGB8FP0E_nigAA8J7bUcJziubl8VFsqeR4B-0qA2g4PBc17JGWyYb8MqneDwbCqxvB-93e3pGUJz4EyM2XZMdLJPr47PSjJ8VxYEZDYewX9Ba-F8WEbDO5eYWcUEQNBmV6Wwjw1ZFYttRWkg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/MatinSenPaii/4207" target="_blank">📅 01:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4206">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56bbdb4680.mp4?token=KHzXBTchsK6-fEmsEH4o158_XbMPDS6PKFl7h70Y2KJZPc1ZvTjCGg7yAJubYPErsy213FID2Dfrtv-thTX9Fu0FvcWX-UKvJtRPCn3PsnNS7BsDa68tYnP4GD_OYT8Ffp-jOl3ESuQ-9ZmLhqH5pNg7gUCP3C3BNe_cI9xY6TC4cjTjvg1JQXA_au8-2ngXPeLUahnREEUPyCtGEpxf-VqMjwyb1XLwpzAPxdDF4zmNTrt2xpdWnZXRn_hdr4W_oDJlrBKZLZvy6hRRn6q8SgoI_jEUMWSL7KXmmD_qZtWtMXqMT29kmzeGGOLlSByD5X3dV0aSbHa54qNxw3fLd4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56bbdb4680.mp4?token=KHzXBTchsK6-fEmsEH4o158_XbMPDS6PKFl7h70Y2KJZPc1ZvTjCGg7yAJubYPErsy213FID2Dfrtv-thTX9Fu0FvcWX-UKvJtRPCn3PsnNS7BsDa68tYnP4GD_OYT8Ffp-jOl3ESuQ-9ZmLhqH5pNg7gUCP3C3BNe_cI9xY6TC4cjTjvg1JQXA_au8-2ngXPeLUahnREEUPyCtGEpxf-VqMjwyb1XLwpzAPxdDF4zmNTrt2xpdWnZXRn_hdr4W_oDJlrBKZLZvy6hRRn6q8SgoI_jEUMWSL7KXmmD_qZtWtMXqMT29kmzeGGOLlSByD5X3dV0aSbHa54qNxw3fLd4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بی نهایت آدرس ایمیل با یک دامنه روی کلودفلر:
https://youtu.be/Z069VNFAgAc</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/MatinSenPaii/4206" target="_blank">📅 19:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4205">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">خب دوستان GLM 5.2 اومد روی Nvidia وقت استفاده‌ست
👋</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/4205" target="_blank">📅 19:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4204">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZknkSsVn9pOK2f4qR0sKs2-jjmf0XCgnwlOn7xGww5i6xZr77ccCqiztJk7vx3y6B3PlCWrHQQW9x9_l9WXyQpv22NbS0zpGoilo7Z2C2aaFWth7e950qs2BEjX8ZI3u3HHYvYhIlQl8b_v7-ZCD-vZ98nW1d7ZPi1XKhwBg1nBxOXOJ8Vl-pTnAdBqEFuj0WP_w8fD5m3Mw69Gu6G1piqF_0SFIAOI9xECw1cZtV5OQkEDOIYZWLOuxoaoBv-Q4HYeoWEEaTHEix5JTWGPmaSV6UzASXoHhy3LJbSFWGY01fkD6W3Bmq3NUHnoIhDQ22SXhIdql1pt6bQe-_x7_Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب دوستان GLM 5.2 اومد روی Nvidia
وقت استفاده‌ست
👋</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/MatinSenPaii/4204" target="_blank">📅 17:09 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4202">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/S3Cke6uWrql-Ijd46_F71KFDzIbB6yhKt36xmmScwq7Os3tD9B2kFtQfaUwHCZGfmHzhmvd2yTT3erWvNLYzsSmi_oPmn3lutxhoYYBmhwv3eOZ4x5imPu6ClOniuizflL5LJim5DjhGkfXtsBSV-aPpZGN7tBDa4i8iUjpiout3EcZ1FYbysZVntUR5cqBnVVTXrfrV5nw7udVlNlF33VaeOyn__mnk67VODah48v1JwoeO0LJO6mgJOp-TodTlAL7Dox5HZttQb1gl2jQZsxMEHNyocFWgh5H7DtR7f9h9Q4qNKB-xHuJzP4W88C5kneDEshRkIFWiUU-SYTg6DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VI4Qxfh4VftAJCXrZUq6bpkB9O1SJ0-Xv5uCYZYJcqNqTSXb5lAwv6P3wCUwtCHNIc7hxBUG1HYiyChQPxtHwXCSBbIv1w2NGrtu9h0Gm5ZuSRXXo8EmbzsGyAQO5qyQtrTWBRdA7o2P8qQr57b3awnY_T5ZAQjf718BiGet8ym2MNmJGSQIAXQPBO5A8m5vgHwnBmqFhuU82cv2kl5BUrSbKm1wzFUPi9PmsAMkqCZBMoI_K8ImzKQCtFnnEXmEWYDLAMqo8ZRz8JK-RqFXy4F4fHOMbSLMGBrPiTc9G-kFbVw7efrR0bn9jsXiRTVHpC2N1zA2S0Kdg34IZE7CaA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">چیز بامزه‌ای نوشت اما پر باگ. دیشب GLM 5.2 برام دومی رو نوشته بود که کار می‌کرد همینو الان با sonnet-5 هم تست میکنم</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/MatinSenPaii/4202" target="_blank">📅 17:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4200">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HRxdJbRaPoNBIHmDFKAc5sQa56HQbo-_g1u6Ft7_hhspkfXXK9NfdDnwrcb6eZomiH4GPD3SOALiadHFHirEDOH8BjMgl5LifQOZzmPDcSS5NFdsBNl-ZPJ8hVFC70t9TaggBrnbaH7nMeOCNiUR7jPnvOP1oTdyBvMZ5SwGd0yJqhOmWrqC8Wc3lJOdj-1uN9p_9ueXKIV7R2buXpFQzo80cMAmGtiGQIJlKS0F9IZV07oBFmZlTo93QWtsmRfy-BD5HZaG0LTyjD7kst_5Oi-tjw0_eJ2sMmEUj21J4ymCEhJD9kb2NK1PtPxCOjoLOsv24xMnvcFflbwEk99Ajg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aHrCdjrbt8RfxU3_VhzZRB-mdXUbX_BU5nhnrUYKL0c8g2S2iYPt6fFmGRRxcnUpFA2bV8Pc2Ch_CcEuiBgOqLRkSBC7pYvkf6TZ3jKLs3M_Jxi8oJj_vDrkyn1eKwKohrs19oAkC5_gCdKOvuiWsOkuEpoUXPKxqX5Z4_cEeyJ7dl204yFU3H93g07GSSX_qXc5lPzEatmx8tt2IxLsvZLCGYVuAtvezoSiC3VwX4849a7gfecG5Yfz-BAY6Gw99YSoFA_mTwq_IJBpKqcsIqCVtml2odysJ10OuLGd8cFr3C5BfWcLYsdi71LJQCvMz9dxvLsvZYPysw18OcVMxw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بریم ببینم با یه تسک گنگ و غلط غلوط چیکار میکنه</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/4200" target="_blank">📅 16:52 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4199">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sfPnuWf55W7-eRdSeE1Un3HJOvWFxvsWjNA0XkZ9X_3OcDMR1l6Yiuwh-2kbNuciih8bmXv4VLdF-nUipoOsXC9cOK-RbX0EfIS18kbKkpZoWJ-NzPxBA-MVMC7woR3jwv8JJhgvOZBscK01fZ4XyTtv7CKqStZm6BMoS7cGYbBTNCs2y-9v6xk_gvy7iKCTw_u048oGTFCn1P6TN3YmnmL5Tpsnv9f44r0rIpheOvyqXrYmef7vNiUrgzZcvg5wh3EBjuok-K8_G6CCN8sfzswlgx9LOPlgy1m1qJYK_-mm9lBMbrcjygW5ZFLvKsW6OyBy6RuoF85zA3wi5AL8tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مثلا هیچ فعالیت روزمره ی معمولی غیر تخصصی و تاحدی تخصصی ای نیست که با chat.qwen.ai نتونی انجامش بدی و نیاز به خرید اشتراک chatgpt یا claude یا gemini داشته باشی. البته دارم تواضع به خرج میدم و میگم که qwen صرفا از پس کارای معمولی برمیاد! برای سرویسی که میتونه…</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/MatinSenPaii/4199" target="_blank">📅 16:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4198">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ovgM4SQFzZMeC4M4Kj01-R0oEdcwn9j8WdaOnJthOfoeJWXEup88wI0HdiHe4ODU7Qk7PvGipKmtpOme18AIsrU-P8EueaGQmpo2dHYKM52gj9rMSMZwcd8BdoXtyGRLq67uoGsufRTHNbC6ghApd_Vs3DanMg0mY35LNPTs6yQhqnQG2RLX9V8pvzfvllqd0FdfYTPiB_8FOtjZx_SlE46zhyMgswYIVWOeYOMJ7gSS_YSc8fAKfl5F2th34YUqavRn6tHVLChb_Ga8UJy1W40beRlm2saEm-2aG2L6ilscJX-2wZ5GF1ILY0kuBj_ygtbhzSLcFlhqJpAYHp3ZTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مثلا هیچ فعالیت روزمره ی معمولی غیر تخصصی و تاحدی تخصصی ای نیست که با
chat.qwen.ai
نتونی انجامش بدی و نیاز به خرید اشتراک chatgpt یا claude یا gemini داشته باشی. البته دارم تواضع به خرج میدم و میگم که qwen صرفا از پس کارای معمولی برمیاد! برای سرویسی که میتونه پروژه بسازه، مموری زیاد داره، عکس میسازه، فیلم میسازه، ریزنینگ قوی داره و برای هر سوالت یه لشکر ایجنت بسیج میکنه استفاده از واژه غیرتخصصی تحقیرآمیزه.
✍️
بوکانت</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/MatinSenPaii/4198" target="_blank">📅 16:36 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4197">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">توی مدلهای چینی طبق تجربه‌ای که روی هرمس داشتم، MiniMax m3 خیلی بهتر از Kimi 2.6 کار کرد واسم روی api انویدیا</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/4197" target="_blank">📅 16:10 · 12 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
