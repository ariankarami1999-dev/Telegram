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
<img src="https://cdn4.telesco.pe/file/X8NG3rU_VPDH4CQ8f8kwC71K2QnnyQN67trcyFtZwgo_RqpdHEOn9hjksb_PHK0m89suYa3t0TN9O585AMzNXfMAHoAiApcTlkWlRd8zUn8Osi6VJO0Ak8W8HwsGcxLsJP6_NjTe9mQzFmqdrPFw9QiRniDYEEtlPSN-hW08tSpB8HwNT0t95WbskzwyYs70iyuEBhzs8OuMb-692oq1eyAwjcsTVRwx8aT5s92qxA_1d4eRQUFSHP0uPy95vhrNYIU9LWYQFYKQ0qRn1m44RWmuatPrv8eDD3PiHHkOVY6DeFYy5WhXoNrtg1jpgDzNHktzfixmVJU9yx1kwM2Q_A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 226K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-13 20:54:24</div>
<hr>

<div class="tg-post" id="msg-65268">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ترامپ: هنوز افتخار اینکه آیت‌الله خامنه‌ای را ببینم نداشتم، اما دوست دارم با او ملاقات کنم  @News_Hut</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/news_hut/65268" target="_blank">📅 18:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65267">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">‼️
🇺🇸
ترامپ: با مجتبی رابطه خوبی دارم. دوست دارم با او ملاقات کنم!  @News_Hut</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/news_hut/65267" target="_blank">📅 18:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65266">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">کاکولدزاده تر و بی‌غیرت تر از اعراب حاشیه خلیج فارس تاریخ به خودش نمی‌بینه، به مادر این اعراب تجاوز کنی شبش بیانیه می‌ده محکومش می‌کنه
#hjAly‌
@News_Huy</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/news_hut/65266" target="_blank">📅 18:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65265">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aa2babe8c.mp4?token=I0YNFHPK2uvjaZQaGWQd-fgEPw_X5o9kLLbLk1qOfzIxLorAeNc9sQvXqqPfQUBFezXGZ_muwUEIcknLpHQNF5qhDGOwvJBufp7mBrjocNmRdo185Z78lHpIJF0ebm3CebBW5rwUFulbv5gvQR6zw9z7zzbPWQyJZjpqe6yUqYCBiwJ3OtRLJQQ2ITrujTHq1qOUYkYrjS3PcGLTF8zz6h9TZvZIlJ6lh5Ox-BcJNEi7Pk7L9G6saiDjr10BwkpIZaTTwhgMM9h0TK1L_VQXd1KKcaqetu5eu4-ugCzgIkxSlvR9qxHsYjKiJcNq5JFv277ozgdhxeOpNRIDpUMNhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aa2babe8c.mp4?token=I0YNFHPK2uvjaZQaGWQd-fgEPw_X5o9kLLbLk1qOfzIxLorAeNc9sQvXqqPfQUBFezXGZ_muwUEIcknLpHQNF5qhDGOwvJBufp7mBrjocNmRdo185Z78lHpIJF0ebm3CebBW5rwUFulbv5gvQR6zw9z7zzbPWQyJZjpqe6yUqYCBiwJ3OtRLJQQ2ITrujTHq1qOUYkYrjS3PcGLTF8zz6h9TZvZIlJ6lh5Ox-BcJNEi7Pk7L9G6saiDjr10BwkpIZaTTwhgMM9h0TK1L_VQXd1KKcaqetu5eu4-ugCzgIkxSlvR9qxHsYjKiJcNq5JFv277ozgdhxeOpNRIDpUMNhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
ترامپ: با مجتبی رابطه خوبی دارم. دوست دارم با او ملاقات کنم
!
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/65265" target="_blank">📅 14:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65264">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8fa16c5af.mp4?token=ZH-ZBrSwcAwVHUPQYnR7japz3EIhL4EIp2qAevJFG3nRm1WArnYSCqlKanpwKFUFg_OmWG3U6OoMguSvtbMcJjIZEepdrNeyTFYAN29kcvJHJR_o0JzpC7PdDQatZzbqnK7tMvczVbrptsv3vx4YeqrLmyR835SOqUF83RLBm4kYiucI7muSAs9-XZXIBjEcIdkPyxMDRB-yOko_At-8o0DZBGDgrpyiocjjH0K5eqZPocGbt8UUG1mC4ixI-jzmDNPf72bP3d1tNF0EvK1yVN9B3a1YLidxAvkx2f7YmdmYzUNI9h6m53VrLfsULm8bo5R6iXA4TrAGkNHpb-74xA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8fa16c5af.mp4?token=ZH-ZBrSwcAwVHUPQYnR7japz3EIhL4EIp2qAevJFG3nRm1WArnYSCqlKanpwKFUFg_OmWG3U6OoMguSvtbMcJjIZEepdrNeyTFYAN29kcvJHJR_o0JzpC7PdDQatZzbqnK7tMvczVbrptsv3vx4YeqrLmyR835SOqUF83RLBm4kYiucI7muSAs9-XZXIBjEcIdkPyxMDRB-yOko_At-8o0DZBGDgrpyiocjjH0K5eqZPocGbt8UUG1mC4ixI-jzmDNPf72bP3d1tNF0EvK1yVN9B3a1YLidxAvkx2f7YmdmYzUNI9h6m53VrLfsULm8bo5R6iXA4TrAGkNHpb-74xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ درباره اینکه آیا نتانیاهو او را برای جنگ با ایران فریب داده است:
منظورم این است که من کسی هستم که این را شروع کردم.
نمی‌خواهم کسی را خسته کنم، اما من این را شروع کردم زیرا نمی‌توانیم اجازه دهیم که آن‌ها سلاح اتمی داشته باشند.
اگر من نبودم، اسرائیل وجود نداشت
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/65264" target="_blank">📅 14:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65263">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/416ff3bf1f.mp4?token=Q6AK0kulPOVm02YDbclbXVg7jrgyiaD0WvURwnVhJk4Apj4P7aOFsQm4f6dE1bBVKksyXeQkb0ZWVo6Nhjd6iQvR_NJ7MJUq8StweYEbDvdiuvKZKa9pulrZFBMXVHx3vlrLYYktj0ajgisvGNld960qlrRFDVg0llqsOfYWFDI7jFcELy0UEUxN_LkWBhama6Z3VVSRlMrEMYdY51Y6_s_kPYTocG-2NflZCPwZC3RqefLWHtVaCvZjz96oAU6kO4mp_uGRoqkuCedRT7xZJeXp1sYWuTvit6_evFJH-7vaE1Mt-VUbTh-mflXc5epY7Tg81UsOnMWtzyVdaB_9Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/416ff3bf1f.mp4?token=Q6AK0kulPOVm02YDbclbXVg7jrgyiaD0WvURwnVhJk4Apj4P7aOFsQm4f6dE1bBVKksyXeQkb0ZWVo6Nhjd6iQvR_NJ7MJUq8StweYEbDvdiuvKZKa9pulrZFBMXVHx3vlrLYYktj0ajgisvGNld960qlrRFDVg0llqsOfYWFDI7jFcELy0UEUxN_LkWBhama6Z3VVSRlMrEMYdY51Y6_s_kPYTocG-2NflZCPwZC3RqefLWHtVaCvZjz96oAU6kO4mp_uGRoqkuCedRT7xZJeXp1sYWuTvit6_evFJH-7vaE1Mt-VUbTh-mflXc5epY7Tg81UsOnMWtzyVdaB_9Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خوش‌چشم، تحلیلگر صداوسیما: انتقام کشته شدگان رو بخاطر حفظ جان قالیباف نگرفتیم
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/65263" target="_blank">📅 14:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65262">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">52.1 MB</div>
</div>
<a href="https://t.me/news_hut/65262" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✈️
اپلیکیشن MelBet
🥇
🎁
کد هدیه 100 دلاری:
Sport100
🔒
برای تعیین رمز ورود حداقل از 8 کاراکتر و حروف بزرگ و کوچک انگلیسی و اعداد انگلیسی استفاده کنید، مانند Hamid120
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/65262" target="_blank">📅 14:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65261">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-text">💛
هنوز توی MelBet با این همه آپشن خفن و ضرایب فوق العاده ثبتنام نکردی
⁉️
بعد میاید سوال میکنید کدوم سایت معتبره
❗️
👀
اگه میخواید توی شرطبندی موفق باشید و درآمد کسب کنید در اولین قدم باید سایتی با آپشن های بی نظیر و ضرایب استاندارد و امنیت مالی بالا داشته باشید
✔️
🎚️
همین حالا از طریق لینک زیر ثبتنام کنید و وارد دنیای جدیدی از شرطبندی بشید
🆕
🎁
کد هدیه 100 دلاری: Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💛
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/65261" target="_blank">📅 14:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65260">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
📰
#فوری؛ نیویورک پست: ترامپ پیش‌بینی میکنه که با رهبر معظم ایران، مجتبی خامنه‌ای که احتمالا همجنسگراست، دیدار خواهد کرد؛ «رابطه بسیار خوبی دارند»!!  رئیس‌جمهور ترامپ در مصاحبه‌ای با «پاد فورس وان» که چهارشنبه منتشر شد، گفت انتظار دارد با رهبر معظم ایران، مجتبی…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/65260" target="_blank">📅 14:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65259">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fU5vf017DH5K0K2rJ4sAfabkSz00gHeSs81upJzf0LAoqkefl0J6Ve2bMrFo1PmTST7Kzfk73sNLK7gmwc_OiEVv4CpsBwDnqkjsQ-viy4dio6_nZmOriU4CjxdE_PAegMaNygurlwZNrmR6ccxmGtFRKDHF_2cz8x7iB65gPGpbBxp5m9pG1QYfXKcap104alvbqICVECC9m1T6AOfBnvdCgnruCyL7FffACUk3eklJUI5EbZ7zyJXFlrRAVgLhJbddv5QSyT_q8L7LpbEcN5DmWdASKNxzyB8jj841qJ21YT-WVFt3FzDidTHuHukucIvXpXQpkKGzNBeDXi1XnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیست قیمت جدید و نجومی خودروهای آشغال داخلی:
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/65259" target="_blank">📅 12:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65258">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qcVyN21k_wYF1g4C5KypUkxjqkC6ZfeF-_kKOTWqsueoiCjvfW0vJOZxaGu4iV0KHV40dGwS6Kjp2fQXnSUfRTUBYf-gU78KpypI7BH04Uo_9tlWoOb6yubEC1eVukkLD_BCG0Wa7Vbvh38sP8eBZNslkSrnoODhOK2FNn1PNpHvwqjO-AzjN6EZEZ6TVtHuIQMwrru8zJD5B3n7X7KuoPdXESQMV5sPPLKIJ69UJSapvqYf9tJw4L7hJwW2MQ0qQAYBHE3XNLq_Kp7g3cSwtUstj-MargDQ8Hh5RQZHNMNVfi-RbliF1Zi6g7UKf0OS-KeGzkxVA6JznU_77vNM5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکنا: آخوندای قم پیشنهاد دادن علی‌خامنه‌ای در قم دفن بشه
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/65258" target="_blank">📅 12:22 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65256">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hf8EEJgL-c6J3PSUgX5B6Bex75Sy2z9Moy3KWfKKf4rfxObf0ujs_kygjaiM-6-iCrpQrbR0v4vmdontBJkPmASYkBiWdK7vT7tPVbr4YLtoAuZOJxJYOFK9IeUUh4_d2IeEGoM-nUzbANnrmDl902ddoHiAGbMUuhJc05mXygpGoTXXgXBwvnLLGaWKLe8VsI_x8CwM26c71cVpu_mlU622-p4AfLhovIUAnH_LCHWLH9_XDh77p8vR9QHKjn3COwfT6QYL3OAEFM6I7Bc9E-hvlUY7QsGlRHm20iKm6iR4PALO-JL_Dnc0bWwTQY_LJQJgb7VrVqHW6tKUHPsnGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aLKYwPa5aNodM6sNNIXta2yqrB4YXJuLpJusGQGcG52Hl-CnYOQUXKjhaL_hL-5nH1_ABIdOa-egm9Vh8AK9WfWJuZMs3DgAko3w2pFbYFC0gNvQcb998ig2niHIv_kFLcqBVgMLRRLlQlOE5Qc8isb9L84lx1tmqRTnKGAoXO1__J1JCkRpX0PzQR9kr1CPOEeYv4HvoMHpsK0Udah5hLH8F7UoLNUnUBfuNw4vEI-0yZZQHIud_JjV_8uiGnn8sMrC_kKoDhW-_fxkDnev-x1RsKcPVZvpPgbmHM2bHnPmmBjke_joHFvEvi8xr4U-u85fC-PDFNX8zucDTy8XgQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
وضعیت فرودگاه کویت که گفته میشه مربوط به حملات دیشب سپاهه
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/65256" target="_blank">📅 11:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65255">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vYmtunbqNlC3nor_cdTSGPV5BINoZTHo8GnRO6Z3_4QRAg4Yy0rGt0HqLjiN-BSKfVb7EKhvfcSff-M7Tzb17V9Wrpgsg6B9Qzg4M7X82Pz9RO2wvLPTuHvvGLwStxbd3Nu4xZsB-Ze-xFKIBWIjeNRAlxS55QVQeqLAVlEPrtR5M0UZT9lWllHlwHQboMPsZfntxrsbqfXfqNlFkI6YUjBLVKBjhlf8J-4M9Ov38KtdxNDll5XOgAhdAsk1BkaaV8t_Fl-OZmup2tQbgRB03JKVjgNVdSSYT-SZiLkvqJZyVr8G2q5RrXV0PCunJ7_ljPya1yBc4JlyhgHHst_h3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیت کوین در ۴۸ ساعت گذشته بدون هیچ خبر منفی مهمی؛  ۸۰۰۰ دلار (۱۰٪-) سقوط کرد
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/65255" target="_blank">📅 11:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65254">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">طبق گزارش سنتکام، ایران چندین موشک بالستیک به سمت همسایگان منطقه‌ای شلیک کرد. همه آنها به اهداف مورد نظر خود اصابت نکردند.
دو موشک شلیک شده به کویت در مسیر خود به هدف نرسیدند یا متلاشی شدند.
سه موشک که به سمت بحرین شلیک شده بودند توسط پدافند هوایی ایالات متحده و بحرین رهگیری شدند. هیچ پرسنل آمریکایی آسیب ندی
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/65254" target="_blank">📅 11:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65253">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">هواپیمایی کشوری کویت اعلام کرد که حمله جمهوری اسلامی خسارت شدیدی به تعدادی از تاسیسات فرودگاه شهر کویت وارد کرده و همچنین شماری مجروح بر جای گذاشته است.
هواپیمایی کشوری کویت اعلام کرد که ساختمان تی۱ فرودگاه شهر کویت بامداد چهارشنبه با پهپادها و موشک‌های ایرانی هدف قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/65253" target="_blank">📅 11:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65252">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bac9b656e.mp4?token=AmID9XKlnl_cL5lHOPweTkGFEO3z413fNUc8g5A_VZuRBohGNSpts02e6JmIvGvIT9cwMYpp9DeDSmV3Dsr8I74RA_VQ0REz_t0wLHfXSW9VtV3NdM4XdFeIOIJXFDYSEeQ4T4qKJa4AUIYp9LZvGnbiaY9aCnz2LC-CgB10iLhMQnu6DavGvOgM3Lx521AenQ2fYivQyV7g3WkXmP9yiMvhdJGtL5NkvJNo--9fdVA6C3f6zlCi2euRzWKaFTVQaAGzo1HtJHKefnhGKQTM2t-2g21bbvZKCW8M0ldjwpN_3sv1SxSYoN9dSIofMIdmlQXIpOC0Rm0B8Ee59deOvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bac9b656e.mp4?token=AmID9XKlnl_cL5lHOPweTkGFEO3z413fNUc8g5A_VZuRBohGNSpts02e6JmIvGvIT9cwMYpp9DeDSmV3Dsr8I74RA_VQ0REz_t0wLHfXSW9VtV3NdM4XdFeIOIJXFDYSEeQ4T4qKJa4AUIYp9LZvGnbiaY9aCnz2LC-CgB10iLhMQnu6DavGvOgM3Lx521AenQ2fYivQyV7g3WkXmP9yiMvhdJGtL5NkvJNo--9fdVA6C3f6zlCi2euRzWKaFTVQaAGzo1HtJHKefnhGKQTM2t-2g21bbvZKCW8M0ldjwpN_3sv1SxSYoN9dSIofMIdmlQXIpOC0Rm0B8Ee59deOvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلمی از پهپاد شاهد-۱۳۶ که دیشب به سمت آسمان کویت درحال حرکت بود
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/65252" target="_blank">📅 10:54 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65251">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
🚨
حریم هوایی بحرین،کویت،امارات به طور کامل به روی کلیه ترددهای هوایی بسته شده است
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/65251" target="_blank">📅 02:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65250">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
حمله سپاه پاسداران به کویت  @News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/65250" target="_blank">📅 02:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65249">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
حمله سپاه پاسداران به کویت
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/65249" target="_blank">📅 02:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65248">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚀
فروش ویژه کانفیگ پرسرعت
🚀
🔥
هر گیگ فقط و فقط 8 هزار تومان
💙
🌎
آیپی ثابت
⚡️
پینگ زیر 150
👀
🔗
همراه با لینک ساب
👑
💎
بدون ضریب و کیفیت عالی
❤️‍🔥
📶
مناسب گیم، دانلود و استفاده روزانه
🟢
✅
سرعت بالا
✅
تحویل سریع و آنی
☑️
تست رایگان
🎁
📱
با ورود به ربات…</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/65248" target="_blank">📅 02:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65247">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromA.R.I.A</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/isVWBNkkSy3Ldkj5_0mCEF6McdQPDkiq5v_ILWrHUHS-QGYTx49PNAtVCK-jiQYDmJXl8GW3hUSvmOTA-m1PqCxqFZP45-pljayO9VnO6Xutf-pchIHrsp8Sl-hIpVpxnIwegQ7y0UMIR4R2G-zKEF7hkHVYKCj4YrCvauy4PHVlkKiaDSQRWda_OSSMg4ngA7twllH3oddb35K3xG4si1B9YdyJ8NpZ7r-n4DyKhfRiEMfqRJL5vx1TwhZUBSaK3UaeFCutSB5ub9fpGHOkudxY9xQZKbavo7FTME2JrJZZVt7MEZnDjo75KFIljn_NUaDjc3pwyx2awOCE9qbsKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
فروش ویژه کانفیگ پرسرعت
🚀
🔥
هر گیگ فقط و فقط 8 هزار تومان
💙
🌎
آیپی ثابت
⚡️
پینگ زیر 150
👀
🔗
همراه با لینک ساب
👑
💎
بدون ضریب و کیفیت عالی
❤️‍🔥
📶
مناسب گیم، دانلود و استفاده روزانه
🟢
✅
سرعت بالا
✅
تحویل سریع و آنی
☑️
تست رایگان
🎁
📱
با ورود به ربات ونگارد 20 هزار تومان اعتبار هدیه دریافت کنید
🤖
ثبت سفارش از طریق ربات :
🤖
@Vanguarrdvpn_bot</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/65247" target="_blank">📅 01:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65246">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
آمریکا بزرگترین صرافیای ایران یعنی نوبیتکس،بیت‌پین، رمزینکس و والکس رو تحریم کرد
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/65246" target="_blank">📅 00:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65242">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/miVjh9GKqABMvKSi421DBPrpxDXYHh22QCaYe5_woAzyL_q8UVds0ZeG2oZrVwSnaa4xrcTeW_sVliGCOsS227WhSZeRXsHm8Xnf9f3lMjYIvFURjjeJbQSMzcYWxHI8BnRzVA6eDhy6KBKw3zQa_rujHOM_L9oUAQoFTUEEPZ8DdhrZjRanh8FgZUOZUMFr_ewvWnVPNrF_iv5WZPyE0bkGNSmaLWIlmKwv03ao0J1Wh2rrzxne1RnrPuwaDReHXiD1mTBxeQYFSziZ-3mfGl3EQFvI0FRq6QNNjECeYGQ5RDBsu9la5vtJuEzIhUb3L09ggluxYS5aaFvY7Ifuzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RLYY7DiTHhRR2VuVXo1P9aLjmIb5G0gLO-K1Z_2bTvDBM7DVxJEAbF-u8MnU7ifsu7Hdc2a5Cb597BMYoqrXwxI_fTcSd9bHQxXyv00Tv1icW-09W2ugWb6PzMIy3AJKQ49G9tywXyMxYCctR1xvp4Xn767ZCxssguNeMoFMeqQn5zc01b3LKx43LrhhwYtcmlOyvwxNVw5afQPBcPfasvEPSn9UjRAOPfE9bvSILngcwUwaPqCW9HVzCJh2mR_TKs0sodtnDOp60rzVZP5UuoehDcuCOfu-3bFVeux_azDJoKWIMvDemHyyMCKBp-vXmqPeEJdV_56gxTPEa4uB1g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یه شرکت به‌نام دکترتور اومده تور آب‌بازی تو چیتگر تهران گذاشته که مردم از جمله دخترا و پسرا میان بهم آب میپاشن و هم‌دیگه رو خیس می‌کنن
ولی خب بعد چند ساعت از بالا دستور دادن همچیزو کنسل کنن
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/65242" target="_blank">📅 23:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65241">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uVzFa_lTmTw1h3Qg1e1MO6822jHmxdNo2qhrci8TKUioHWYhO_wdO3npkqBu1ha9wvNbIzerkifEljkFV3LLQNQni0nt3VpAfKfovxtODWxAFSJTz3iBR9R7HS-Wuhex4HcAYywONwyoWlaqFmzvP9wr6thUwSIR0KeAn1xm2SssnDgS95iMoYIEiMKoICVSqphRQ8dYWQnDJLwcAsPwxo6dsNGLklVvwJDjxF-yp08rJNgwBOseWyhHlCcfNZJeTHwI6n3zfuzUBVKeYVUPNKlfqMULwJqd-QbYNIhDRGv8gU-3DCQ4UD1QNPLX5srvqQunFLtffbUjWd7nWDSbFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سنتکام: ابراهیم لینکلن و نیروها همچنان به محاصره دریایی ایران ادامه میده و تاکنون ۱۲۲ کشتی رو از مسیرشون تغییر دادن
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/65241" target="_blank">📅 22:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65240">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ngmLPhw8H39SIbpOoObHR3Cjyk2iNsO_piKEiJgQZC1Fl_WmBirNQaSamFdnhUKqXlBXcnA7LqL3Y5pT7x49VkXhkvEsltYN-x4hlZN0UMW3uL2lPyHvgx1yXPaukZdY0ex3-1v90-_5RzbbN2o2RI1w5CbfjDYMtGygh4pnPE0sWmfZlVM269XiwQy_dE1O4LgpVJGfUFS6V06cisd8cif7UK0StrHT6yDDziV-bFU8lzZ_9NEu4bHZkUT_GcR-GT-c8f7WzG5uSHwkVWLoYLiarY-pFU_HM1syl1oYMxt3_KjY4GNfoFKgRrYSALowNKnMChk38lq2V6MWvjsZew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق آمار، سالانه 60 هزار ایرانی بر اثر مصرف دخانیات فوت میکنن.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/65240" target="_blank">📅 20:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65239">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/news_hut/65239" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
#اپلیکیشن
اندروید سایت جهانی دربی بت
👍
اسپانسر لیگ انگلیس
👍
🔥
امکان شارژ امن از طریق کارت بانکی
➖
➖
➖
➖
➖
➖
➖
➖
➖
🪙
همین حالا عضو شوید
👇
https://t.me/+aCbq7yy8QY80NzQ0</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/65239" target="_blank">📅 20:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65238">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TBnmoHfIA9d3rdznfJsT0Qy8iWQe0JasZcqrWCPtMXOQrd-Lt4uIl240ERLL35eEpJFKK0ManxieEWCpYovk_bYEtOnjBB678v0mjRTyL2-MPVvIQ1dfTuHTqPeddiDNZVcbYJRpm_KEqHKaBZlAWny_afe3HacKVrGUW9iaSwlDH0pITQZZcdgdJ3BG7cjqYfnhL5LUd438wKL4b4uTNyIyBiGbiPkORjEgjSUWEhBLMLR4Y_p5FpUn7Vw2hvC3o5o52zd0UOxLJ9nVj_6gMP87IkJM--42Re_D5ewluALV755AmotcFpGpVr4TP7Td2wC-xGrtgwy8jVaAZw2LJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
دنبال یه سایت شرط بندی بین المللی بودی که به ایرانیا خدمات بده؟!
⛔
👍
دربی بت همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
🚨
کد هدیه ثبت نام:
GG007
⚠
️
برای دانلود اپلکیشن کلیک کنید
👉
🔔
کانال دربی بت g12 :
🪙
https://t.me/+aCbq7yy8QY80NzQ0</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/65238" target="_blank">📅 20:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65237">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
امتحانات نهایی که قرار بود ۲۱ تیر شروع بشه جلو افتاد و رسما از ۱۳ تیر برگزار میشن
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/65237" target="_blank">📅 15:18 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65236">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LKvMRyUXd0TNs1trzA3xUUoFFaZrA0Fv9RDnSF74j9X0tciYci3WUKAiiLGPwULfpcyrI-nZrXDe01RfmWtzLLsvrJJ-S1nn00pIdAgKX_IIxadrh5lm8hXZRSIJL-AlqjMrdQIycT6KyRNHGbd7Q1aAHScUukUHaZUVpCYZwpt4iEVfkskgK4UatTwTduYvg7fM8x0GZq_2ir-8tykgn34Zb2UrVb20Nz7IeY3gvZXlcMgPjnWydRcu6k6meP1CY28HomtwatDo5ZRlg1Aa1lmOzOLwuMyB8cVh0iNtjLRDy2gRf7qfulGKnGZ2RMbXd_eraU2T41zfCSquwhxB5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
داعش با انتشار پوستری، جام جهانی را به بمب‌گذاری و پاپ را به ترور تهدید کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/65236" target="_blank">📅 14:58 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65235">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a43d73ec7.mp4?token=VAGFxJJLImDmErlClm_M76r7ORzpzaHhu9Msa1Po0yE1g1SD6KvQJY1Sn07uvCRI-ech7Vq33Kc-v4qrOqlYWhmMI_jQQKD-MfRyonJZeecL-Nd6TTCb5diOaxGN6xNzj2Xyc4s5RoqDH3_8FKNo2GkooV5PRAfQ176OCtr4Hs--ohwL6WoAUfl5HlcLMLGkdKUDbZMCBdzM2vXSP1Qnl0Pyy1924bBMg-pAz6uq6QwBquHKr7pVPziunnn8dBK2Uxebt2VDOjv4N2zCrq5JQj6h2KDoK11QE-ejz5ooHQWbJuuldpF3VqD4QHEMUcoha1BU2SxJXzu6kmiosrV_Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a43d73ec7.mp4?token=VAGFxJJLImDmErlClm_M76r7ORzpzaHhu9Msa1Po0yE1g1SD6KvQJY1Sn07uvCRI-ech7Vq33Kc-v4qrOqlYWhmMI_jQQKD-MfRyonJZeecL-Nd6TTCb5diOaxGN6xNzj2Xyc4s5RoqDH3_8FKNo2GkooV5PRAfQ176OCtr4Hs--ohwL6WoAUfl5HlcLMLGkdKUDbZMCBdzM2vXSP1Qnl0Pyy1924bBMg-pAz6uq6QwBquHKr7pVPziunnn8dBK2Uxebt2VDOjv4N2zCrq5JQj6h2KDoK11QE-ejz5ooHQWbJuuldpF3VqD4QHEMUcoha1BU2SxJXzu6kmiosrV_Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
علی‌رغم درخواست ترامپ برای آتش‌بس در لبنان، ارتش اسرائیل دقایقی پیش مناطقی از این کشور را که در تصاحب حزب‌الله است، بمباران کرد
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/65235" target="_blank">📅 13:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65234">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f14e605921.mp4?token=W1TlL1axMLw9iSeA2uKqtnmmr572bgJ8ZhigPhfWdghQ9nJbNBKq6IOTWirn_KvBr0Gw-tdhzOdqILAFGX3npJZRb1z50CNJMo6lG0P6vn6qoGLTxhN1gPJBLGdI9DHRUl4JMTqeqUJ2GbPf2mPtJPki-eQ_6SUMZA4CzfJMSh0kLE6vNAKY9Or4VKm_jI1sbzLA94pia9hVhdlWPSW-nyHC7NhE6po5D1vkwX45HSydAArZJkZJT6P0LQPD8p7SBiyYPE2PI-xsPKAOOt52xyHbMbJJXBNpd7cIesf2N9AK3U_k5kvWyzqGxA2bYmwlowly-RwBIFaj_kZWFBwn5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f14e605921.mp4?token=W1TlL1axMLw9iSeA2uKqtnmmr572bgJ8ZhigPhfWdghQ9nJbNBKq6IOTWirn_KvBr0Gw-tdhzOdqILAFGX3npJZRb1z50CNJMo6lG0P6vn6qoGLTxhN1gPJBLGdI9DHRUl4JMTqeqUJ2GbPf2mPtJPki-eQ_6SUMZA4CzfJMSh0kLE6vNAKY9Or4VKm_jI1sbzLA94pia9hVhdlWPSW-nyHC7NhE6po5D1vkwX45HSydAArZJkZJT6P0LQPD8p7SBiyYPE2PI-xsPKAOOt52xyHbMbJJXBNpd7cIesf2N9AK3U_k5kvWyzqGxA2bYmwlowly-RwBIFaj_kZWFBwn5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🔝
دیوید بارنیا رئیس موساد:
تغییر رژیم در ایران یک هدف ممکن و قابل دستیابی است. این یک وظیفه قابل انجام است اما نیازمند تعهد، صبر و فداکاری برای هدف خواهد بود. این وظیفه باید در رأس اولویت‌های ما باقی بماند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/65234" target="_blank">📅 12:56 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65233">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b11e2b7f3c.mp4?token=mo-Ns878zMoMmeqjwhrwZ1HBRDtPIvHE1zOaHiUIgCH6p9JiQ-UZyXxeq6IVma5Iffv3u5unuWUaCmEMzrWEf4cHcn7fsM85p0dWpZDdBI27KlFvidYP4gvPlGrpcXpLlLkCnIk51v7-OKbzCUGZnTkhJ27OJEsk-9o09BHV0aWwhZywG21qHmIyN4o0RDkmr9RXlBWc9tA6IHQKi_B7N4t9R0cmGjv8uGUW42Xdg0RiAKJ1dSQktiYPR0L1iNW92E0NvsOlnK3woYU6O1439VqObjpiSnhTTYOD8XX_Z4zg3XGvVqD1cehw1-pFJON8ch6JmgR6fKYhH6skGqkrvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b11e2b7f3c.mp4?token=mo-Ns878zMoMmeqjwhrwZ1HBRDtPIvHE1zOaHiUIgCH6p9JiQ-UZyXxeq6IVma5Iffv3u5unuWUaCmEMzrWEf4cHcn7fsM85p0dWpZDdBI27KlFvidYP4gvPlGrpcXpLlLkCnIk51v7-OKbzCUGZnTkhJ27OJEsk-9o09BHV0aWwhZywG21qHmIyN4o0RDkmr9RXlBWc9tA6IHQKi_B7N4t9R0cmGjv8uGUW42Xdg0RiAKJ1dSQktiYPR0L1iNW92E0NvsOlnK3woYU6O1439VqObjpiSnhTTYOD8XX_Z4zg3XGvVqD1cehw1-pFJON8ch6JmgR6fKYhH6skGqkrvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
امروز دانش‌آموزای تهرانی در مخالفت با تاثیر قطعی معدل، جلوی وزارت آموزش و پرورش تجمع کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/65233" target="_blank">📅 12:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65232">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65232" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/65232" target="_blank">📅 12:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65231">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OpTOt3PoU1gNAevzXUZZINUt6yBMIItX7s_OxJDAPkUWHXwdNxKaFKjKTl-UgeJaCVnP8EGAcp_EX7UMZ2f7Ss6YL8EX8HXBOrT-7bfhHQwAtRp4V-gxT8lEw6yC_oZWGpR3Hqohu3bmwG-ojgpzKlm8Y7-MC3SJLX4m3zUJJ5TroLR10iW2GgZxYm7KLurBcyBYhi3y99WR6j8DwiXF_LKuD2X50re9BvQISgJ7RE4AnWkr-ywI7Yd1WrWG7xIWvwApqcQbhDeJ6v_e9t8MkF__24IEJ2FDDdJ-DrmiM0hsjXJJwVVuCtmJ8-ChD7_eUVH-vRjAbkFe7N0r5Xv_Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕹
روی بهترین مسابقات ورزش های الکترونیک پیش بینی کنید و برنده شوید!
🎮
تنوع گسترده از بازی های انلاین  CSGO, DOTA , FIFA وMORTAL COMBAT ...
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/65231" target="_blank">📅 12:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65229">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e2d6ed8f2.mp4?token=k1mHWr3q-3JF8QguBNgF2V9eJwkNcTI_oSzALSdjdSLaYGDa7bfxnKOVNGciI-mmp-aWYGbbmNdHSrIKsMqbfHDyftPXMbEWrlxcn6OMZFQ1WVeGUfdDtCNBds5tc1jjOjDtHdtxa5vfpiuEraXdZedDkm7uepxFYxT43y-1qjU3jQVvTQLlsEPJgVdBR3A2kxfajiMCAPB41V2ucbs6oqLvHUoZl6EstJkmVNWMlAGa7-8noINfJI5Pv7cLF6xY4VUSZTyHrvHkZcRCw5-g1qi6DjD6MQzK04RQMn2pUP7jVXauhxEcHtolVgXkOdQyOmbWF6ifRhf8hiiBk995NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e2d6ed8f2.mp4?token=k1mHWr3q-3JF8QguBNgF2V9eJwkNcTI_oSzALSdjdSLaYGDa7bfxnKOVNGciI-mmp-aWYGbbmNdHSrIKsMqbfHDyftPXMbEWrlxcn6OMZFQ1WVeGUfdDtCNBds5tc1jjOjDtHdtxa5vfpiuEraXdZedDkm7uepxFYxT43y-1qjU3jQVvTQLlsEPJgVdBR3A2kxfajiMCAPB41V2ucbs6oqLvHUoZl6EstJkmVNWMlAGa7-8noINfJI5Pv7cLF6xY4VUSZTyHrvHkZcRCw5-g1qi6DjD6MQzK04RQMn2pUP7jVXauhxEcHtolVgXkOdQyOmbWF6ifRhf8hiiBk995NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
واکنش یک‌عدد ملا در تجمعات شبانه حکومتی مقابل یک ماشین با چند سرنشین زن:
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/65229" target="_blank">📅 10:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65228">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e2983c9bf.mp4?token=rRqa3LInGBV-yDfdytLa0WqQQY0qSHwAJiTz7np7jfbyRBVtxxKpCfT_wWXu7juXmGlGWkFRef_0yQ4eWtSElvLKw0MLiPMQX-GpEKIcZaC9sYEp7RkpzR4G-0bSiERzW4MNEiLOM2DCYzxZ4Xgc_z-qtm-3FcewpTK6dGKQcRB7h1qGg08qaS9NS0Vh3wAkBa9rqWQi9ifIFp2FY0CNufLPpcpWgX9ulWxjFw5JrNrNsJqn2a-tBuq3djb4XgVYaWDdwjvn5dy_pXB4YBg9l19mGBhxYBiv1PBX0yAzbq14D1D_WdPwWVPeQw5y8vbT28ItCrPULQg4qIseM3WNMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e2983c9bf.mp4?token=rRqa3LInGBV-yDfdytLa0WqQQY0qSHwAJiTz7np7jfbyRBVtxxKpCfT_wWXu7juXmGlGWkFRef_0yQ4eWtSElvLKw0MLiPMQX-GpEKIcZaC9sYEp7RkpzR4G-0bSiERzW4MNEiLOM2DCYzxZ4Xgc_z-qtm-3FcewpTK6dGKQcRB7h1qGg08qaS9NS0Vh3wAkBa9rqWQi9ifIFp2FY0CNufLPpcpWgX9ulWxjFw5JrNrNsJqn2a-tBuq3djb4XgVYaWDdwjvn5dy_pXB4YBg9l19mGBhxYBiv1PBX0yAzbq14D1D_WdPwWVPeQw5y8vbT28ItCrPULQg4qIseM3WNMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
نواب دبیرکل حزب باقر قالیباف: آماده بازگشت به جنگ هستیم
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/65228" target="_blank">📅 10:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65227">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/159f752950.mp4?token=BRKR6i2HnbQ0WyGb3FT7TvHcUqXhy_zUNZogK5F6I_gn3WRgySs_Fjmw04d8vca1gTV68rHytDvJOLDbSHwGc-zylCgz0wn_5wxnLGl1ggRdUmenHB4Zslm0hTpPU0PcyObwV9pP8smcPUVXG6yWsT_vtM52n-1hEsikhU8aq42csKlMsEjEEfKAQOJMEuPXZSCXPtgCvyWGPLy1_0BRm8XEu-QHDoU72V5h32_aPCKtEhi0ujdAnP_pJ8z3CcWrKo_HokJoLMondljxC85gVY0YUnfnpDZnoRNKqOGSZxuBNTZxnCxnoCCXU6UMPJG89dMS6EWAHfPauiKAGQjvKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/159f752950.mp4?token=BRKR6i2HnbQ0WyGb3FT7TvHcUqXhy_zUNZogK5F6I_gn3WRgySs_Fjmw04d8vca1gTV68rHytDvJOLDbSHwGc-zylCgz0wn_5wxnLGl1ggRdUmenHB4Zslm0hTpPU0PcyObwV9pP8smcPUVXG6yWsT_vtM52n-1hEsikhU8aq42csKlMsEjEEfKAQOJMEuPXZSCXPtgCvyWGPLy1_0BRm8XEu-QHDoU72V5h32_aPCKtEhi0ujdAnP_pJ8z3CcWrKo_HokJoLMondljxC85gVY0YUnfnpDZnoRNKqOGSZxuBNTZxnCxnoCCXU6UMPJG89dMS6EWAHfPauiKAGQjvKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
🇱🇧
درگیری تن به تن نیروهای ارتش اسرائیل با حزب الله در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/news_hut/65227" target="_blank">📅 01:43 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65226">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f218bec310.mp4?token=XI1e0DaUPt4R2JP3KJPu3U6jWS1k8KR9e24F_jeQquQkkKG4C2I9yTa5XXUV3iHCG-kJskJJl7oEMS1z8KM02RFRIxrfnBn6va7ju3k27Hf2oa5zIoENVdrdnWChvzRODhRajNqe5OepqPNfc7M6QNfTg564EdkMbFK2zpqI32FXUPXlDi1mfPAaqCbE9UO87KPPJm-YP1gOBOn9P1PgqzMrCx1oSAha0VtuzMGuSnxwybccMFddtKMlOglCwv1Ho3vr_d1UD-4xIOLFnjhgZPPcIrIOt86Bvbcr2xNe3lFrhxiN8GqNIZ_SGlaQB4w1XHaErMqnSIq42aFF1e5DNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f218bec310.mp4?token=XI1e0DaUPt4R2JP3KJPu3U6jWS1k8KR9e24F_jeQquQkkKG4C2I9yTa5XXUV3iHCG-kJskJJl7oEMS1z8KM02RFRIxrfnBn6va7ju3k27Hf2oa5zIoENVdrdnWChvzRODhRajNqe5OepqPNfc7M6QNfTg564EdkMbFK2zpqI32FXUPXlDi1mfPAaqCbE9UO87KPPJm-YP1gOBOn9P1PgqzMrCx1oSAha0VtuzMGuSnxwybccMFddtKMlOglCwv1Ho3vr_d1UD-4xIOLFnjhgZPPcIrIOt86Bvbcr2xNe3lFrhxiN8GqNIZ_SGlaQB4w1XHaErMqnSIq42aFF1e5DNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
وضعیت عجیب جنوب لبنان پس از حملات امشب و امروز اسرائیل
@News_Hut</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/news_hut/65226" target="_blank">📅 01:32 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65225">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-poll">
<h4>📊 اخبار جام جهانیو پوشش بدیم</h4>
<ul>
<li>✓ 👍</li>
<li>✓ 👎</li>
</ul>
</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/news_hut/65225" target="_blank">📅 01:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65224">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">رئیس‌جمهور ایالات متحده آمریکا یک «تماس بسیار خوب با حزب‌الله» داشت، که یک FTO (سازمان تروریستی خارجی) تعیین شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/news_hut/65224" target="_blank">📅 22:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65221">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ji6X_PFbjWt0-5KekaDORsFmHWMjy8i-LdZcUx7OO-SshsrVesg1AqdIcsseY3JhEtILccZzBJ9QuXeym0KWsW9XQqQGAnxzHKrEQZGieVhTePhVnzLrGGwGLijdl6fmeyNy5J4RfUtB3xSN3puwNlHQmh5gxuCmhGRhc4O3R0wpJb5GKIqKkmACRpK_wNzHhRrGd1BlfC5ZFB10wPeIB51G_1YBm35yYdEjVGDdXgT3CfuhgZxADxAGTk0sP85KKN3bidKdnlAC1D7b4KjX14XoFiUxZJN33yGxeRkz2nFiElnADbz30IKNggbzcXdG7eEO7Ao8d7-ZuMnPCEUweQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ: گفتگوها با جمهوری اسلامی (ایران!) با سرعتی بالا در حال جریان است. از توجه شما به این موضوع سپاسگزارم! رئیس‌جمهور دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/news_hut/65221" target="_blank">📅 21:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65220">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/E0ql0x0xnIludR8kFVNmcUB1xBCiDeVD9Gpy9u8HKBnSJm3SAU8Q48smkz_IKU3MjHnvqVTaHVYPQcHignznm1S5KN9e1w1hbwVPL1Dgh71dwuzSfOtWlaq9bmfnrcShvBPVfqTKTscoRtIhWGxXDD1MFyOVqdTk7MlE-t_YhuXob33J6kI-Gy4bqL_AsegOh2Y5zj8xvPvdLsKfUY9NIt_gawmjdekBGh6ROofbSxEW4D10vMB1BPvruW2ozkhkqOfPlXqw_HjPU0OZ3Q6gW8B6WNc8gzv_XlXyCxovTVi3jGoPmD6L4Tn7kxmWwVfMqlqa5o8ExDLYGxfsuph9sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
#فووری
؛ ترامپ: با نتانیاهو صحبت کردم و دو طرف قرار شد به حملات خاتمه دهند و آتش‌بس را اجرا کنند!
@News_Hut</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/news_hut/65220" target="_blank">📅 21:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65217">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CiEM5tLc0eJfuhXnVQOWTBJDndcrmLpwUYtiG8pql3-VUq5dBLKB2YHkk_6coT_0WuIxKl80DeRY2XqRWdUKTLpktt4-MnAH-jGL_9vdZnQX018ogKf_jiKmPMDn_pVpjVE7SGKw4A-GljoSRzcdpM1OXj6KWHHHlwd-nBquc-AzKXeCXubAvTk1VejRYbj60JBiVz3oPSQUwrlGGSmvOXclp4f14aDM8n71_E7wZan5TdBcnwtbBtvpxE1rq3_HSwJ8oTYuwYt5eHoZldUTzhTl0utxJD8XJP9I1GH7LALJqgl52_muWAIbSABiCMcEK-jNf56aAP7snNs5o5Yr_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ایزدخواه، نماینده‌ی مجلس: آخرش که قرار است فلسطین اشغالی را بصورت زمینی آزاد کنیم؛ چرا همین الان تمرین آن را از امارات شروع نکنیم‌؟!
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/65217" target="_blank">📅 21:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65214">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
📰
مصاحبه NBCNEWS در گفتگو با ترامپ درباره تعلیق مذاکرات:  فکر می‌کنم ما زیاد صحبت کرده‌ایم، سکوت کردن خیلی خوب خواهد بود. سکوت به این معنا نیست که ما شروع به بمباران کنیم، ما محاصره را ادامه می‌دهیم. محاصره یک تکه فولاد است. فکر می‌کنم تا هر زمانی که آن‌ها…</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/65214" target="_blank">📅 20:57 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65213">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇺🇸
سنتکام: دیشب ساعت ۱۱ شب به وقت شرقی(۶ صبح به‌وقت ایران)، نیروهای آمریکایی با موفقیت دو موشک بالستیک ایرانی را که به نیروهای آمریکایی مستقر در کویت هدف گرفته شده بودند، رهگیری کردند. این موشک‌ها بلافاصله منهدم شدند و هیچ یک از پرسنل آمریکایی آسیبی ندیدند.…</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/65213" target="_blank">📅 18:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65212">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qnA1vjrUJk10HaTkb5F7wji1sQ1I5MirNsa0EzQcIegNBUJJjrrzL72SUwNMWZ1tWeH3nP9GpPOz2pMQrAyxBLaKsXTXKjctdGeTv1YUpg7RIaJlIOUh1AUXGQV7CO5BxObOmusXIKA3s0MtS1IlaCzgvboqeIFd4SrkXqQupGi_ytNt0IF8jRzsEKnnW2BF6jlF6OW5iqMkkP4icrkWttN11Spg8t48U9FMvkTKYWTjQMNMZKJfzal6oWdc0TDQd9fX_wKlnZNaaXVFv7RgWFxb8GkzTS-wKdmlu_Ad9QtUQsKoJiXCZhOxgpk8FcNztXT2eSpQxLJiljm78Z7G-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سنتکام: دیشب ساعت ۱۱ شب به وقت شرقی(۶ صبح به‌وقت ایران)، نیروهای آمریکایی با موفقیت دو موشک بالستیک ایرانی را که به نیروهای آمریکایی مستقر در کویت هدف گرفته شده بودند، رهگیری کردند. این موشک‌ها بلافاصله منهدم شدند و هیچ یک از پرسنل آمریکایی آسیبی ندیدند.
فرماندهی مرکزی آمریکا هوشیار باقی می‌ماند و به حمایت از آتش‌بس جاری ادامه خواهد داد و در عین حال از نیروهای خود در برابر تجاوزات ایران محافظت خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/news_hut/65212" target="_blank">📅 18:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65211">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wg7fwD8F5poNrAmQynJRWVPN6P-K2CtTdY1w50qjifArQGDFoL5BCcsMfkvFLt0U2C5SBMNzXgUhuJ0R4XqGrcM-P0rbC5425kC1pTJP5Ae1zj_topmgPuqGHQAdO5MGLVQ6hgWJ_DrLSHtxbtqzIpnPg01FVTBWvmeSyRZ1CFv0hiQvNGBTr_X5Hu_SzO9LO-4-VQPfU-rGPLJz0LkglhaIhuwNf3gsA8MNpvPju8pXFo96OIgo6T7uU1Db3Oe6rxVNCl37pgZHks6ygUXa68knieonOUwAcf9YBdYrd_R_xb_MNNnyxKlfC_Jf-50xM9OGi1R3enf4aPjL86GhZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیرنویس فوری شبکه‌ی خبر به نقل از سخنگو نیروهای مسلح: تداوم حملات اسرائیل به لبنان قابل تحمل نخواهد بود
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/65211" target="_blank">📅 17:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65210">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KX0oLA7P925LoqRhpTBbJKsEtT2bKC-g4IzRhg04JCnRZodb_YVX8EPJwk5AelBaxtnTNAHymTBgvY771JwyvohzUb73FgWp3anftITS3NeoIBMoCBeoZBKasrHT4Zzn3K6Z0ydizTTg0Riq6e9sZENm56Rbt4I5g5GVPXe4bQYjI4ZL9eSHDmJjStnP_flHMIZ8iVXwl7UM8MMiLWEbyBSOWPI7iOnZAvUBEuBolIzrBGhhGKPWxkdSatfqs3t7hVGhyWvKdztcsRtro-FlQzrR-BBslh-W6rzNLrXiM0C5gjRtqs4btxCC656OhSyKoo2su3ZYxB0-UODyf_5DeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تهدید امریکا توسط باقر قالیباف: محاصره دریایی و تشدید جنایات جنگی در لبنان، گواه عدم پایبندی واشنگتن به آتش بس است و هر گزینه ای بهایی دارد که پرداخت خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/65210" target="_blank">📅 16:17 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65209">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X1aRXbe7PxB3uQZAXG9QLXJL5HHr2DoPcVvIvVzdiUgc1j1Tri06lvwaV_2Iy1RbYbmaXaeshchG8KErjZn5XzqKIYF_Kv8t_JzFG24bGUPUSoNOMAxBiOnwY14oUeVOVIoEkr8PEqqpyJeS5x_0cEhSSVNSvWNrW4QBRJDduthcxfAD-Mo5h9cJiu0ilI22FZSBiukJwae-JW-LgTqzcF1-bVI3riN1n41cnWbDeyFCf84ziodVa_jjmHYvFXZjrUx1h1qKJNF6HA6Df1fvnTVDqsliID0yaiGwoLgC-l3O-7WGcpslQ8NkDj_xzRneTfY3RR2JbUkS7HY5mpu9gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضائیه جمهوری اسلامی، صبح امروز و همزمان با اذان صبح، مهرداد محمدی‌نیا و اشکان مالکی از معترضان دستگیر شده دی‌ماه رو اعدام کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/65209" target="_blank">📅 14:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65208">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65208" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/65208" target="_blank">📅 14:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65207">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v3dUQA82UHUvxeQLkdbY8cmMpwTmMDwtoyz6lcxxDwPHfepxJUteOUmw3rZwh5eLJYyzJVp_O74HM_EjHCZsC-ut6sj0O1sjM60PESqmDMkfp4TzwfndOLQ2P4R9iisn8XhmsKqr4yK9Mu0qThzPZLNevAyg_0fFupZfW1MgkLzFrxTrt7cC1806K7REeRA63tVY74swzXNLuix4FzwBjyr29Ch5OFqRUWhK4r3iOvv6yh0WFwaM8I5NwPX810Hs07Endm3FO8lyigiHqZSNZzA1VnKgxkVVlDmVc6-tOJ8YJmcLT9DRl-Ur3PwbeGYM0QAbdHmmIQmHRUs51nUWOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌇
بونوس‌های شبانه از 1xBet
🌒
هر چهارشنبه و پنج‌شنبه از ساعت ۶ عصر تا ۱۱:۵۹ شب، برای واریزهای 5.50€+، 50 اسپین رایگان در بازی
👑
Crown Coins
👑
اهدا میشه!
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/65207" target="_blank">📅 14:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65206">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FrCTIcRGCWkvmFiPdqq2c_kDPiY-Oq9nLh6ACR3CIEn9iVtcflB25JudIUWeBIohMgqoE7owMZyQLZKJlOp0FPSoN_K30EsSuLYRFX3sUYcSLr64uaS1DXbAGgkYXmKlzYH0zp4L9FAV4gwMNlahB6BIacxUT6-USprUBVbf9gxe3OJrfKkPi25tp-xpiC2AY9qyEU6dNnErFG6npTpRnzG8eoNAksijNFJ8U_-zxxNd67A51i_wtCcsW0IW1-z32ws5uEu7IP00OzYdt-cUnEl96ayfY-VMsoFzJ5MIXd7Mw4Unbw6NFscR8FFbAwNePwxjMH6dBTC6uR2PvnKqsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ: ایران واقعاً می‌خواهد به یک توافق برسد، و این توافق برای ایالات متحده آمریکا و کسانی که با ما هستند، توافق خوبی خواهد بود.
اما آیا دموکرات‌ها و جمهوری‌خواهانِ به‌ظاهر میهن‌پرست نمی‌فهمند که وقتی افراد سیاسیِ فرصت‌طلب، به شکلی بی‌سابقه و بارها و بارها به‌طور منفی اظهار نظر می‌کنند و می‌گویند که باید سریع‌تر عمل کنم، یا آهسته‌تر عمل کنم، یا وارد جنگ شوم، یا وارد جنگ نشوم، یا هر چیز دیگری، انجام درست وظیفه‌ام و مذاکره کردن برای من بسیار دشوارتر می‌شود؟
فقط آرام بنشینید و آسوده باشید؛ در نهایت همه‌چیز به‌خوبی پیش خواهد رفت، همیشه همین‌طور می‌شود!
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/65206" target="_blank">📅 14:31 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65205">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
شاید باورتون نشه ولی ترامپ و کابینه‌اش همشون خردادین!!
• دونالد ترامپ: ۲۴ خرداد
• مارکو روبیو: ۷ خرداد
• پیت هگست: ۱۶ خرداد
زندگی ۹۰ میلیون ایرانی تو دست خردادیای مودیه.
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/65205" target="_blank">📅 13:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65204">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🇺🇸
گزارش سنتکام از درگیری‌های دیشب بین‌ امریکا و سپاه در قشم:  در این آخر هفته حملات دفاعی به سایت‌های رادار و فرماندهی و کنترل پهپادهای ایرانی در گوروک، ایران و جزیره قشم انجام داد. این حملات سنجیده و عمدی در روزهای شنبه و یکشنبه در پاسخ به اقدامات تهاجمی…</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/news_hut/65204" target="_blank">📅 11:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65203">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e4c45b1ee.mp4?token=OhsAk5zRkVGO7sCnmRJEof26jEA2DyLpHsuQjF1zV0gE1l0nr9tNpolyjcFnEgX3XIptLXjLsiEaV9bcw2EKnWa3x0etDfQJ9D3vG-ElsmWwx1niw1R4ZS90oKsNAeSTSIRskz-OXdoMCuZtrmzjQywYXVqwQYBBQRIKgWb7WDWCjeHpDYod8vAdQePsAvlZ0bkRd27hF8vYWIujxhxotpkeKs7gz7gS2P8iHERhir958yIxAhpb22DoMu2GYVWgYroROxZlXu_f25syHpHLAnjLKDEwrLDsM_qKlJ1g-pOaYakaFFIQ37iEbEBUEUkzFWfGRQXveCgo27KUw131_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e4c45b1ee.mp4?token=OhsAk5zRkVGO7sCnmRJEof26jEA2DyLpHsuQjF1zV0gE1l0nr9tNpolyjcFnEgX3XIptLXjLsiEaV9bcw2EKnWa3x0etDfQJ9D3vG-ElsmWwx1niw1R4ZS90oKsNAeSTSIRskz-OXdoMCuZtrmzjQywYXVqwQYBBQRIKgWb7WDWCjeHpDYod8vAdQePsAvlZ0bkRd27hF8vYWIujxhxotpkeKs7gz7gS2P8iHERhir958yIxAhpb22DoMu2GYVWgYroROxZlXu_f25syHpHLAnjLKDEwrLDsM_qKlJ1g-pOaYakaFFIQ37iEbEBUEUkzFWfGRQXveCgo27KUw131_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جواد ظریف در پاسخ به سؤال میگن شما پشت پرده مذاکرات هستید، گفت:
من اصلا هیچکارم
@News_Hut</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/news_hut/65203" target="_blank">📅 10:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65199">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">بر اساس تحلیل تصاویر ماهواره‌ای CNN، ایران ۵۰ ورودی از ۶۹ تونل موشکی زیرزمینی هدف‌گرفته‌شده توسط آمریکا و اسرائیل را دوباره بازگشایی کرده است؛ در ۱۸ سایت زیرزمینی، عملیات خاک‌برداری و پاکسازی برای بازگرداندن دسترسی دیده شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/news_hut/65199" target="_blank">📅 23:53 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65197">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NtMK-Tvwuv7Iy4D13k5BXUKs4svZL3TWvfuV14xWXOHK7YWMBkZIcu1R3pjWFPGKegLakG5DFybTWqhKd_UordDVQSlrKDa_unW8h_lViS7colrxE-AGKDXTYgQtJa2Mw2qA4RG4MZYi-LFSIvIn2QkMzJTD5fnCJXUT_XvCXBPHCSnTE-M-f1b-Am_Op0haVPAdjqsgPdPUb1Q5lxNKbKLF8v8j_GR_M3guzPUjFkt0iKyoPnjOe_YoD0bmGGUSaPOxk3GwQeo2JElchmnjL62K94PaEpXkkDpUdbFqH5qcPxxi1Y7TsE_2Y25hXmfx_3f60M_1G2LyhjuA1tAc-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طباطبایی، معاون پزشکیان: رئیس‌جمهور ‎از خدمت به مردم عقب نخواهد نشست
@News_Hut</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/news_hut/65197" target="_blank">📅 23:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65195">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">طبق گزارش The Jerusalem Post، ایران ادعا می‌کند پس از بیرون کشیدن/مرمت تونل‌هایی که در جریان حملات آسیب دیده بودند، آمادگی شلیک موشک‌ها در سطح منطقه را دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/65195" target="_blank">📅 22:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65191">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
📰
#مهم؛ ایران اینترنشنال: پزشکیان از سمت ریاست جمهوری استعفا داد  @News_Hut</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/news_hut/65191" target="_blank">📅 21:18 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65190">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uryhwqguHR6p3vtzkWAJdQ5jzplrem-Idtvl0VDI7a8JLC4CugmOzwOXkg9yk8easE0eDFGmT93EjP23J1fDbBRZcRQCxjzKzG-sbiNe6lJtnSqoQ7QT4NpkO5YzSKWjURMkNzpZiskrF7aM98cD6uEhpTjKORKCB1a3kOlN1e7fNS28RelklO5iKTOrmO0EMvBEcTKrLe23LsLQlEzN-siBoTGQ-E5-ued-ujwFPzk2uwgI6p3df79mQRiHCX4lHGpElI_O_ah4Cc7BOZai95Bd09tnIY3hIbSzmu-C11lkpveZLIKI6TYifjY7g4cOmLjRyOI8D63DJ9f-jRTbuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
#مهم
؛ ایران اینترنشنال: پزشکیان از سمت ریاست جمهوری استعفا داد
@News_Hut</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/news_hut/65190" target="_blank">📅 21:16 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65186">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qMz1Xlz9FLReqmAbwiG-aibRckX0CHzWFImFzOtzxUK98cZ-aniHvxi_pbgU8nmrmH5QOtBoKZGAIceEQc62r_4n4IkLpKfbiyncC4HZ_xmCFdk7w8lU3Q0kpx0A8b3t9neWjdrX6ncNt66IYbQtTUU8gDjhZvO1WWLmGvOIXzrxzinYKRcpeN292W4oBaAJPtVtEeWtRwOUOA_fd88lN5mkgSUpMOoKKH7oGhVIiFEzrVu4MinKm3-iqsdtDj-gNRtXiziwajMVz0DzweOuodERxHMBi21u7ObBRJ3Iv1uR8M-kcZoyuKb8xBFcjhQxqS5E2cObECoJJpoq3lq6gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VYRACCTn8zFQE1ejvwcQHLdC6eu47D4SCPhRdnG8SpE6Uga60gz7fwYVh5EogvfJHbrnkzQpMg7Pw4KFRUgkeghH-mRrV0Gv_8HFI9kXnKPor-ILg_SH3v-1OMGvtdzKODNxXEgqkkht_li9SSwSsHQGnhtNNtGTnKazsG3-hNB5iNNgMdVMd7ZXJNztlYnyGm8cCMY3N-z-XMrsDerHf3UE2ndG6g11YRmBTM9xEd5GLYdLn8D3eVkGFIQglt_XD8I3BepryCrqlu2Z-EddFt7eVkoWNxNrVcU0KaN_TfscPebF62E7M_r0JNyoPeakKBdY4dzv55PXAZn3OZBgfQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a589784b7.mp4?token=pjipFM67CacjBw5vom6L5KD5JwfGWAjwrJ6O18L1GONK7qUWg0aJbR69LObFQmbnDHNvL6TdzHevX8oZ0Mo0jSEWYeWViVhTIRSfDIDjyAmhpFwJYiI6Igyj8bBFcwa5CKo9lS-8NPMr8GoIDCL1WZZreP_6t7iZaygrKWA1mr0jmdMou9fxRnovZ13kgcMKhSSR0kO2zCiJ8PRwGbe6cxMEjqkIFSRdExvy1kY9CNtP31aOcHKhDTsp59E6MKc4HU6v_y3DHB72998eJs79Z4jPsGLb901qNbjPY_vQnuV3CujbN49T8xe-yaBeclOWEcDQcTsGIt2XB1-Q6_eQXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a589784b7.mp4?token=pjipFM67CacjBw5vom6L5KD5JwfGWAjwrJ6O18L1GONK7qUWg0aJbR69LObFQmbnDHNvL6TdzHevX8oZ0Mo0jSEWYeWViVhTIRSfDIDjyAmhpFwJYiI6Igyj8bBFcwa5CKo9lS-8NPMr8GoIDCL1WZZreP_6t7iZaygrKWA1mr0jmdMou9fxRnovZ13kgcMKhSSR0kO2zCiJ8PRwGbe6cxMEjqkIFSRdExvy1kY9CNtP31aOcHKhDTsp59E6MKc4HU6v_y3DHB72998eJs79Z4jPsGLb901qNbjPY_vQnuV3CujbN49T8xe-yaBeclOWEcDQcTsGIt2XB1-Q6_eQXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
اسرائیل رسما داره حزب الله رو تو جنوب لبنان به شکل خایه‌فنگ‌طوری با خاک و خون یکی میکنه
@News_Hut</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/news_hut/65186" target="_blank">📅 18:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65185">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hxt3QY1mXItcyDtRQoKwyvOWatRFH4EaAggy-tcK0pTlchjH6e3luwaSF0K0v_0PHOUvMNpwik4dzfYNwdYvSGbmMWfxiDyn6hA4kbWYoBzf16-Ub-grG7OREKgyeKVe1KhmTJViwz0AEYG5cgMKRLibNh9jADa_WzpGLHbrxgHwVYwMgZT7rOwJWh2zMjwTX88QHwuugO-BAceGewu6D-uwLkYrJUGnZSvujeIgdXi94kaCSgHz3DtP7wtWKRhLncW94_rRGjb1MBo0rCT86nMK-EbTUE6crXMApoJsDRhBQdRNm7YtyWtRKz3TVLfRlHoe3t4OWtU58o40Xn6gsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست قیمت جدید خودرو های مدیران خودرو با ۸۵ تا ۱۰۰ درصد افزایش قیمت
@News_Hut</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/news_hut/65185" target="_blank">📅 15:00 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65184">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
گزارش شنیده شدن صدای توافق‌های عمل نکرده در جزیره قشم
@News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/65184" target="_blank">📅 14:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65183">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec47112ddd.mp4?token=OcY1_wOnEPkcsWXfelpmDl9edr_VglNTQSwOwlvoz7odM7hw60ekPsQZ7NrKVBFAEQD1SOAXZR27USZhv6r6LXGc-Zx92tFqQvT-4a-CImBwYXcSyQmmCjrhzIrWeOL9z2mYQP9qgXfk7WeKRu0Q91n_9Aint9VYmXiQU83OcfZYaJxmI26Qvpml17GRoIv3pF6x6wX0TkSCt9d9CP9bqauO81YYW2vczc6NcbzATg61IAHmFw89hCVaIDXD6ZXPmkFDH13JDTGz-1ewzGS4bo1vJWNEpg3LXI17N08tbDkPTMEQvWpNwsQ4CSLt9fIkTZ_rrJmfTcA6kyldPOy-7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec47112ddd.mp4?token=OcY1_wOnEPkcsWXfelpmDl9edr_VglNTQSwOwlvoz7odM7hw60ekPsQZ7NrKVBFAEQD1SOAXZR27USZhv6r6LXGc-Zx92tFqQvT-4a-CImBwYXcSyQmmCjrhzIrWeOL9z2mYQP9qgXfk7WeKRu0Q91n_9Aint9VYmXiQU83OcfZYaJxmI26Qvpml17GRoIv3pF6x6wX0TkSCt9d9CP9bqauO81YYW2vczc6NcbzATg61IAHmFw89hCVaIDXD6ZXPmkFDH13JDTGz-1ewzGS4bo1vJWNEpg3LXI17N08tbDkPTMEQvWpNwsQ4CSLt9fIkTZ_rrJmfTcA6kyldPOy-7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ: بزرگ‌ترین سرمایه ایران، «رسانه‌های فیک‌نیوز» هستن که مدام موفقیت‌های آمریکا رو کوچک جلوه میدن
شما یه پیروزی بزرگ توی یه نبرد به دست میارید
ولی اونا میگن شکست خوردید! این واقعاً چیز بدیه برای کشور ما
@News_Hut</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/news_hut/65183" target="_blank">📅 14:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65182">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lKiShrISx26Sl6dcXJ8VmeiPBME4JP0-rcmFXWSouVuOQxqIlHvZ6PM5Jq8_BmgNQjCDwdioEj4sbYw4Xjx4YbhmmaLnXLMBHe0X689ePV2n4hnwB0zANBCBGQrddi223pZHcjZ76ApxiyLVcTQQ5Vwv1Sd5tFoVCQeH5a4Y_1T-Cr7AdjZ-AuuY0gyj5qzBugJNedwJGLt4D6H6DRSd0AKKIQ00esLZdsxNPVU1jhw4gM3QMr5dRVYIgJ9j6AtVOfairmr64uxVEee-pCjuq8wOi9A8KjdeJG2xePQ1kQnjEgHIoELraSOumyCVJhW9BXhoavnjehkgsIrFMhq9aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تردد خودروهای پلاک مناطق آزاد  تا اطلاع ثانوی تو سراسر کشور مجاز شد
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/65182" target="_blank">📅 12:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65179">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/473b1fd669.mp4?token=MF0z9ZXTNPLJSSh5bx-pEPuyy5GmbBt7d0lTi0n6O3tvZf4tkEIVny4bn0CpE-2Eh46I2Kg-zS-vXkxX_MA-AG84VyjNrkOuXcMd34OqDagLGZMYnvgC-LRFzOz01Yt4QsHoXCJZhp26Uqe3bFWL9sy8EkaC6lcezA47-dkkAUR_fIb0caEwRb29pgOC27yKVh6WjgnMzeXcuaYi2SFI1PDmawSsK9enuKknXUn4x4UwOoca0r4gsbw4Mx7f1w1VYn4N6T64BX8q3VqdZXkimkg9o3dtfTVdR2yxYiw7L686A1QFIgyPEnq_nH61e0GXMYl5XRmHCubfe1SXVV1scA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/473b1fd669.mp4?token=MF0z9ZXTNPLJSSh5bx-pEPuyy5GmbBt7d0lTi0n6O3tvZf4tkEIVny4bn0CpE-2Eh46I2Kg-zS-vXkxX_MA-AG84VyjNrkOuXcMd34OqDagLGZMYnvgC-LRFzOz01Yt4QsHoXCJZhp26Uqe3bFWL9sy8EkaC6lcezA47-dkkAUR_fIb0caEwRb29pgOC27yKVh6WjgnMzeXcuaYi2SFI1PDmawSsK9enuKknXUn4x4UwOoca0r4gsbw4Mx7f1w1VYn4N6T64BX8q3VqdZXkimkg9o3dtfTVdR2yxYiw7L686A1QFIgyPEnq_nH61e0GXMYl5XRmHCubfe1SXVV1scA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ: اگر عجله کنید، توافق خوبی نخواهید بست. اما به آرامی و پیوسته، فکر می‌کنم داریم به آنچه می‌خواهیم می‌رسیم — و اگر به آنچه می‌خواهیم نرسیم، به روش دیگری به آن پایان خواهیم داد
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/65179" target="_blank">📅 11:12 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65178">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4173e3828.mp4?token=tPxGjYI5vJJ2ybsSn01Rn_u_5S8MrMdgr05kNTacG8Na8ru_ECDnxj0FvG6mYxT_7vnsAO_IPFaaSizHNMUAS3IfY2Xh-qGOgJc9vcVTOjX9gR7znGK2OpnmFG51sjSWTnjuurfFOx21FXrjaKtE3B-lz2LxMi1RVeB5CjhG1P-8H_AfDars1zhVnnXqGQbVnTaxygfqhdM4bUQRygO2FOy8evrecRfjoSz1LKWaGz-NTelDPdyACfODVD-qtuhSlpWYaDMc6WcXtiuevuk7HTY5i4OxU982oIEO8oKQh3cIvFdqslLCzN6XQejiYlY-2MQOYEiHYq132a0DZ-2RGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4173e3828.mp4?token=tPxGjYI5vJJ2ybsSn01Rn_u_5S8MrMdgr05kNTacG8Na8ru_ECDnxj0FvG6mYxT_7vnsAO_IPFaaSizHNMUAS3IfY2Xh-qGOgJc9vcVTOjX9gR7znGK2OpnmFG51sjSWTnjuurfFOx21FXrjaKtE3B-lz2LxMi1RVeB5CjhG1P-8H_AfDars1zhVnnXqGQbVnTaxygfqhdM4bUQRygO2FOy8evrecRfjoSz1LKWaGz-NTelDPdyACfODVD-qtuhSlpWYaDMc6WcXtiuevuk7HTY5i4OxU982oIEO8oKQh3cIvFdqslLCzN6XQejiYlY-2MQOYEiHYq132a0DZ-2RGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سردار حسین علایی: ۳ روز قبل‌ از جنگ رمضان‌ به آقای شمخانی گفتم آمریکا و اسرائیل با ترور رهبری جنگ را آغاز می‌کنند، آقای شمخانی گفت «نمی‌توانند، پيدايش نخواهند کرد.»
@News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/65178" target="_blank">📅 09:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65177">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff9b4e22f8.mp4?token=rYRBk1kdVMKZN9lSNCbAt05v6ulX9Ihqt8wrbW8tk5M6d0I-EwSxnQsXRntQeL59pLHIQ0QteLX5BQF0SCQPH1BYn0-bZ1G9f1qOLWzFKT92PKfecMIX4yneth0NjVm3-v-86FiMqGAvs3d9UpYq7SebD2oH668pOS-E94Kc8W2K62VJj1iirPqsXXDYM2gGFdhzx5_nJi5mL74Fg5DbTMNpRA2HYp68CMfUmmpYubiPmkJwYEzT1Pl2xrVHQSEkH6e1Buxr4T430KPNNIC1tJaua05ISlVgqmyIaVZw7WVvoL9ZL8EW545pMQolEaaHQhRn_s97IWsH2g1F8TauRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff9b4e22f8.mp4?token=rYRBk1kdVMKZN9lSNCbAt05v6ulX9Ihqt8wrbW8tk5M6d0I-EwSxnQsXRntQeL59pLHIQ0QteLX5BQF0SCQPH1BYn0-bZ1G9f1qOLWzFKT92PKfecMIX4yneth0NjVm3-v-86FiMqGAvs3d9UpYq7SebD2oH668pOS-E94Kc8W2K62VJj1iirPqsXXDYM2gGFdhzx5_nJi5mL74Fg5DbTMNpRA2HYp68CMfUmmpYubiPmkJwYEzT1Pl2xrVHQSEkH6e1Buxr4T430KPNNIC1tJaua05ISlVgqmyIaVZw7WVvoL9ZL8EW545pMQolEaaHQhRn_s97IWsH2g1F8TauRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو تجمعات شبانه حکومتی‌ها، دیشب سپاه یه قایق تندرو آورد وسط میدون و از نسل جدید قایق تندرو که ساختن رونمایی کرد
@News_Hut</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/65177" target="_blank">📅 08:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65173">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CX_i4i40FLTs-YAeJeXl0HpecdUbSLdEJ-LpNSVyftLuYmngC0gPvFfVFhzUJc1uqW-i0rhOaB1CwBGy38KJjV4uqzdvPA4ex7mRMgJqfUSQp4-RJG8LpYaXxJvxZQDTVuf5m5EanKNS0mLYh-n6qSatfmCtA7AKbUSwG0ldRzzHbk0jijiT6n7Bi64goJ34aChcY4yim9Y7GFIICMoBuhrGJ9hmch9rorOQLDJ0EDR6QqymqOcDg2sb3SjooOjOUYazkV0qJ-AN6kioyTyzr_m2g-D9zjSVI7ALluV8BrNdoiI6rZ9EYRffZwAfkM11JVhX5LaLtLumjBoxRq1TnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IAKk4DcGl5Iey-OJYa7kdlQ1YyUdwVACtKK0Ly5d6_ustPipf3IW7uQ2nNzB2XCNLN-uhZ1hIkyApvocqAvvZupyCMelJawSXGId4JpAsbGhJ5h5m4WKTVw5qX_ivBQxCRmp_BAiukglFuZfzY1Edg8YOhPzVDUDtccS6WO7uCEchfItloZcBvk0qfYJW9vXDx79y6ABLe3wgFiAg5bUQ0DShIZmYnAbLlVMKgMc1Ll2JoghM-6cCrkimUhvGznGBMFmQTMadv6eahc7HOYn1U-TRb2ipBKmahOr1tY_jIHKM3mzySzQbTLPFXpN6JJkiRJDMnPGwMV3HR1uZzhUGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پست های رندوم ترامپ دلقک تو تروث سوشال!!
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/65173" target="_blank">📅 00:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65172">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff2f73449d.mp4?token=DhEpTgmqMf3pnheXE9RnLb5Xyo8dsaZrNJRIKFU0O0CvCPJZWbhkpzlPRuLA_90jmBqnFAMbVJ9rGInVmVeZk47H2CKpxyyRP4kWpJg21pNfaTPfDAcVs3yUAYDPxD8nPDtlM9Ks5QmOdcBBrcRQYMoCJOXW2w_X11QRhWbl7jhfArEAY9IzE6UFjGt9yafAowsMtnuqIe_2YTrgbUi_1dBqdKbjMCjWh_g6SfekvLGmlaf3zyS0JpW91L1tXZo9blauNCFaJ8TgAZmCREeWc6CV44nwSM7Q4zKnUwOkKfC7rtjhhYt-k3bzRiZ2nSEsai6D5Gw-Q2JMam6qAp6rWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff2f73449d.mp4?token=DhEpTgmqMf3pnheXE9RnLb5Xyo8dsaZrNJRIKFU0O0CvCPJZWbhkpzlPRuLA_90jmBqnFAMbVJ9rGInVmVeZk47H2CKpxyyRP4kWpJg21pNfaTPfDAcVs3yUAYDPxD8nPDtlM9Ks5QmOdcBBrcRQYMoCJOXW2w_X11QRhWbl7jhfArEAY9IzE6UFjGt9yafAowsMtnuqIe_2YTrgbUi_1dBqdKbjMCjWh_g6SfekvLGmlaf3zyS0JpW91L1tXZo9blauNCFaJ8TgAZmCREeWc6CV44nwSM7Q4zKnUwOkKfC7rtjhhYt-k3bzRiZ2nSEsai6D5Gw-Q2JMam6qAp6rWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه عده تو عید قربان خاتمی، روحانی و ظریف رو بنر کنار ترامپ و نتانیاهو چاپ کردن دارن بهشون بعنوان شیطان سنگ میزنن:)))
خوب این ۳ نفر همینجا تو کشورن برین خودشون بزنین
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/65172" target="_blank">📅 23:32 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65170">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dd6247ddb.mp4?token=KXyRooIcC7aUhnkJF0QOreRYr450KdLCxa5UhCAGb9hg4imJVmK0a4QSbfnrbJc_fhw69Xe3m3Bc_L5g1O1zxGs7D0pfv3GbcvpeZ1xAHDLpbC_yvzCsjgYE7dzRslXHbZJCODoL_itZWs5c1ZqXQBcNzMn_CIch4iu6G1gTjWoUf-d6W2ISuL-Ivb-sf2qg7Ls61geK20ajfmxaAMSs_aOzElb7mt-ZCKv6MzMJSEyRhmXMswcey8aDi66MpZv5H4DIWiheKIYRP5AdnomwzWeAZA7WVZRtkg1nphsYn4g08Zv3iPUte64R7WzFm_qncH9uj2fWx-Z7O2mllT9NQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dd6247ddb.mp4?token=KXyRooIcC7aUhnkJF0QOreRYr450KdLCxa5UhCAGb9hg4imJVmK0a4QSbfnrbJc_fhw69Xe3m3Bc_L5g1O1zxGs7D0pfv3GbcvpeZ1xAHDLpbC_yvzCsjgYE7dzRslXHbZJCODoL_itZWs5c1ZqXQBcNzMn_CIch4iu6G1gTjWoUf-d6W2ISuL-Ivb-sf2qg7Ls61geK20ajfmxaAMSs_aOzElb7mt-ZCKv6MzMJSEyRhmXMswcey8aDi66MpZv5H4DIWiheKIYRP5AdnomwzWeAZA7WVZRtkg1nphsYn4g08Zv3iPUte64R7WzFm_qncH9uj2fWx-Z7O2mllT9NQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظه‌ای که معاون رئیس جمهور آرژانتین نزدیک بود ترور شود، اما اسلحه در چند سانتی متر جلوی صورتش گیر کرد و زنده ماند...
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/65170" target="_blank">📅 23:25 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65169">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">نماینده زاهدان: برخی مناطق شهر ۲۴ تا ۴۸ ساعت با قطعی آب روبه‌رو هستند
🔻
بحران کم‌آبی در سیستان‌ و بلوچستان وارد مرحله نگران‌کننده‌ای شده و به گفته نماینده زاهدان در مجلس، برخی مناطق این شهر بین ۲۴ تا ۴۸ ساعت با قطعی آب روبه‌رو هستند و زاهدان هزار لیتر در ثانیه کمبود آب دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/65169" target="_blank">📅 22:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65166">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">کانال ۱۲ اسرائل: نتانیاهو به زودی جلسه‌ای برای ارزیابی اوضاع در شمال با حضور وزیر دفاع، رئیس ستاد کل و روسای سرویس‌های امنیتی برگزار خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/65166" target="_blank">📅 22:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65165">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">شاهزاده رضا پهلوی در اودسا: دنیای آزاد هنوز ماهیت جمهوری اسلامی را درک نکرده است
🔻
شاهزاده رضا پهلوی روز شنبه ۳۰ می در نشست «امنیت دریای سیاه» در اودسا، در جنوب اوکراین، با انتقاد از جمهوری اسلامی و سیاست‌های غرب در قبال تهران، گفت که «دنیای آزاد هنوز متوجه ماهیت واقعی جمهوری اسلامی نشده است.»
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/65165" target="_blank">📅 22:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65163">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QGVE4SytQVmBBxf19SB0-ZvGgzfHIkzya02Y6ELnJtoqcoX1CaRSdpXBdYqX-yMAwI4AIsTM2DCHH8x9YGlnQbuj-R-4nBfA3tv8sv4F8TIdBXvSkL_YvUI9qbBiimGT8fnePWlxbO-NIyuHlihTMbJHWEyQ9jEmSkYmwOr0HZ4bVhAKsCoiFwqPuw9NGmGKHlAzm-2CJnjBT5X1VK3hdVb1yMDnfHA-Zkm6LGM0a_lPNq7iJ-_sKKFdxGsyUV78gTORjmp6ZjgQ4u2cOP6mK6CO9M0ry4BtRJNzpBHsboQdlmKeMsiTMFOsAJCLTeWHP1rmixpOQqk5IdZzmh5BtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوشته‌ای که تو تجمعات شبانه دیده شده؛
والله هزینه مذاکره بیشتر از مبارزه است
@News_Hut</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/news_hut/65163" target="_blank">📅 18:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65162">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
پیت هگست: وزیر جنگ امریکا: محاصره دریایی همچنان پابرجاست و به‌صورت دقیق انجام خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/65162" target="_blank">📅 18:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65161">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Imweg66rGBpXf9SxjQ439Tr3tGQ_vv5OteFgUFHApUwrXBD9BZXh_bCsq4YbjNpA5vFFBxVnWamRA2EUYvLk9B1qwemg1O8quV-TIH_0O_aoeWCg8YFEpFxrDQ2iBrXxQf1B7fDeSky5WiGqf8W2hlAVRHJOKheufs60J8bCm1MLFkPtdMBB9IE7eoZcMTp_ARIWlW0A5fQKAie9IkH4zZzxwkS0Q3W6zCcq1Y2HWdi_DmRKA-OEY6vxueO9ZH8YtXWKlS6OYaslOkk7wXTipAbTbukHkOY6FT60A0UJKmngt1NfBlgrMc8pFyeq_SVoHlZD-Pmpc36TveosOFld7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی: من فهمیدم ترامپ برای بار سوم در حال خیانت به دیپلماسیه.
@News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/65161" target="_blank">📅 13:49 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65158">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XJ94tUKGlBkbyQ-R09URhW2nvqrRxfpWkNjM-MqYwIrYUU_kBukN5o0x1tfyo5CsBN_xcibB6Fb6rvw-eTsuX6y_1wYjoTxaFg_tK9Obs7tAbF59OMIHFSxe-pHGzngfLLwghsop0IyDA-_T3O2XkydecgiDbNC-rKDUPaSyHH8nk6e0Er-X_hqww6iETi4jbsRMKNMY75hdg_1fVoU5fBJB1yIbH00J793Xsc9RHmemD3er8lQm4w7tdsuwhps2opiB95YsdjB8Wa_zJvuH077TNHj9cw8hVyZoXR7UPLUNrGsrHT-5wbADr4oP5SEDrR6huSzfqTBNpLp6VRNoFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کاخ سفید آخرین معاینه پزشکی ترامپ رو منتشر کرد؛ ترامپ ۷۹ ساله در «سلامت عالی» با عملکرد طبیعی ریه و سیستم عصبی قرار داره، و قلب‌ش۱۴ سال از سن‌ش جوون تره
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/65158" target="_blank">📅 13:17 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65157">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
سازمان سنجش: کنکور ۲۹ و ۳۰ مرداد ماه برگزار میشه
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/65157" target="_blank">📅 11:02 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65155">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pJj4Bj8QBqB8AL3A0Cw5FGO3Fw6FNgXrs1Z5zoDfM3jfR71ZvnLOjStOAgOES7LbtO3t2uEZFlVqEgO85Y0CNpeatq60Yh3HEWNNgC6e4hZ64YrIN8mby1rmca6fZErr-tcnSvr2MGDIaJ5L-QCqAgCS8EoQFelxJyuDS71y2P0fqQHz_HP5BvaBdsdZa1FfvSvSlu1TlFLpICFcUsDJ2LDxPqOhLf2pp7xNwEILCeScO_-YfHdu07SEUJ0tjVVv83-SR1XrHG-6ArXPHB26_tmCRMefV2t2u4oboilCs_or1B9EuCZzdIjvOc03q816v6hpssHpUGVKcXt3q53llQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AKSEexxcraWZcSFLYB8BO6zPqmEEhGx5jJZgYhEzyqMc6aOy0z96YlqwDUCFqga7MIDpeoMoo6ytSL1LREcHNKfyxpQGxAtBdk_ZrLky8xtIA3OOSG55qu19hkwWAgMmL4sdldTc5cxL4_QAY_QyEffcn8nmmfn_Xdzh9jK1SIKqqP-cwUFlX4E0_0JRKgLkQaYTP8oMQQsOc0l5BwsxxJb5m0WzYhbxqVbVxnCcW1UIJnGNpfrmbth2nSGbfsjtZc_7_KVgCSH1kFLqE-hOEC2DF2NGhio7X7EfubhKHfVnh1jpFJvQbD_4C1ITRQpVtRo6OU6B1yZHLgjKBBoP4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ملت اینجوری دارن قربون صدقه‌ پزشکیان میرن چون حق مسلم مردم رو ازش گرفتن و نصف نیمه بهشون برگردوندن!!
@News_Hut</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/news_hut/65155" target="_blank">📅 10:52 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65154">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/js_PgAeXO153tcDgpHie-1erUUDsPk0123I76vz8_ARmjAn2J6x8E7RNFZ0zqlkuQBxCfepkwZFXcH-8o7J9OkG7naX5VYEhLD-WdlwbncA6QqAV3r4QldnvOz3oBWwyqTD2gTz8vvpwqk6U3b45XZYr9AUQStx5Gtpe_5G0x151YntdlF1x9eYD0Rt_0pBhW50WfOPConq-5UjOLOBwLngA0xIJIG6wnINpTEBx5DvtdiY0HgbVLMQRl-pc1FYXtF1Rw8F81Z-1_z5QBa7dPsWyL1tcFjHVj2a420NoNMQoXcomQqRVMi1dF2TdNaEKEtUHRSsiOa-Ze_8xXhorEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از عروسی‌ها و صیغه‌های نمادین تو تجماعت شبانه حکومتیا یه پسر ۱۷ ساله با یه دختر ۱۶ ساله تو تجمعات عروسی کردن
@News_Hut</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/news_hut/65154" target="_blank">📅 08:39 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65151">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a38baf3c3a.mp4?token=Oy1jagzFpIXnHgJstPC40yPQNZBw_6OQRhBhWV6R_sDcazUCet2FDCWFK1uh5iH8jvF-xdA3FwYJLl1ZpEyomBgaVNXcCZE61dMQsbBwPRVEUbtv-BttbhYASc_d7Gp4OoOa6reaUO9DePIUfScRePT4AaUHn1weR62AVLt0svMgB1vrHLJN4SXX0R4kIF45Z6UAPzTscSBdUMiM5Artv7mVTtj_vrdFdmYM6ol7trvHeA4wGzJWEN8istG2A9uqKMphYE7L-u--L0B0_L1eSU6oz28KN0UlwokONnJMSU8QaRH7_hxrUgJ1l7fmKMq_AvZwi2PHxpdiXa7TQXLC8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a38baf3c3a.mp4?token=Oy1jagzFpIXnHgJstPC40yPQNZBw_6OQRhBhWV6R_sDcazUCet2FDCWFK1uh5iH8jvF-xdA3FwYJLl1ZpEyomBgaVNXcCZE61dMQsbBwPRVEUbtv-BttbhYASc_d7Gp4OoOa6reaUO9DePIUfScRePT4AaUHn1weR62AVLt0svMgB1vrHLJN4SXX0R4kIF45Z6UAPzTscSBdUMiM5Artv7mVTtj_vrdFdmYM6ol7trvHeA4wGzJWEN8istG2A9uqKMphYE7L-u--L0B0_L1eSU6oz28KN0UlwokONnJMSU8QaRH7_hxrUgJ1l7fmKMq_AvZwi2PHxpdiXa7TQXLC8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
اسکات بسنت، وزیر خزانه‌داری امریکا:
ما حدود ۱ میلیارد دلار از ارزهای دیجیتال ایران را توقیف کرده‌ایم — کیف‌پول‌ها را به‌طور کامل گرفته‌ایم.
برخی از دارندگان ممکن است همین الان در حال تایپ باشند و ندانند که کیف‌پول‌شان گرفته شده است.
این پولی است که از مردم ایران دزدیده شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/65151" target="_blank">📅 00:01 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65150">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YleoxVoL1UO5_SLGDruevDl4bBwG66ZDM35YsNdw9pDFEUzKDf7n0zXNc4o3JYsN00xNuaZmNgatFibO7a2jBYu_SQsqMUZ4_4mFieZVRlI41hXLXB2nSUy-4lmk-TNj3xD_v3CtC211AUxrVxKnibnR3OF0u2FfZV3kzfr63_d_ptMi0z-Sue54cR6oKGS7sKx_6AzyAv08gzfaJbrQ9RWx6WlCpFWykJdUgkI4_lQ1acyipNQvo8tPkqNN27HhsglOqYOai35knAMzdVXy0zujzW3XlLillOSnWkrZ30PUgu4X6DdcjmsBzsDM87pkvKYHHpLYUNVe5PNqtNdqVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحویل بگیر آقای املاکی!!
ابراهیم عزیزی رئیس کمیسیون امنیت ملی مجلس:
ترامپ باید بدونه که ایران به عنوان پیروز میدون شرایطو تعیین می‌کنه
نقد مقابل نقد، نسیه مقابل نسیه، هیچ مقابل هیچ
البته برای موضوعاتی که مورد مذاکرست نه آرزوهاش.
@News_Hut</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/news_hut/65150" target="_blank">📅 23:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65149">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kHegWnCu12UhxXafs7RPLOAYfEvLlZ5C0dUtyIWlk9FiCvP1tlLZSEnQxa4vHSMdSghOcVEIX8xUtrGqvXTPIj0ckdJH5MOjXpLaCePe41kwICXcObEHHaR2vctx8w3_hhwd4A-xJXlwuUPTKdTP1lF5h46DvXKiK_PWLmTfmc4l_EvLmh3UYJj3SnrIqtrhDJW4mme30VXEwEghS4wYranDaNC6yWYh9GTVm8fLLkNUwpbzTfzJ_rbm4i_cMhDOGSaySEIZAuGygRJRpzPQaiyka4cMafp0TL6By12h7DN3wyAef1do__MhbW7bGxgS2J8JIj-gLzLwoV4oeRH9ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمودی، رییس شورای هماهنگی تبلیغات اسلامی تهران: ستاد آماده‌ی تشییع جنازه‌ی علی خامنه‌ای هست و میخوایم با جمعیت میلیونی برگزارش کنیم ولی زمان‌ش هنوز مشخص نیست
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/65149" target="_blank">📅 21:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65147">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
گزارش فعالیت پدافند قشم
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/65147" target="_blank">📅 21:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65146">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">‼️
بقائی، سخنگوی وزارت خارجه: در این مرحله بر خاتمه جنگ متمرکز هستیم و در مورد جزئیات برنامه هسته‌ای مذاکره‌ای نداریم؛ مدیریت تنگه هرمز باید بین ایران و عمان تعیین شه
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/65146" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65145">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">خبرگزاری فارس به تازگی اعلام کرده ترامپ مفاد توافق ایران را تحریف می‌کند.
او ادعا کرد که ایران موافقت کرده تنگه هرمز را به صورت رایگان باز کند و مواد هسته‌ای خود را از بین ببرد هیچ‌کدام در متن اصلی وجود ندارد.
ایالات متحده باید فوراً ۱۲ میلیارد دلار از دارایی‌های مسدود شده ایران را قبل از ادامه مذاکرات آزاد کند و آتش‌بس کامل در لبنان (طبق شرایط حزب‌الله) نیز الزامی است.
این توافق هنوز در انتظار تأیید نهایی در ایران است. منابع آگاه اظهارات ترامپ را ترکیبی از حقیقت و دروغ توصیف می‌کنند تلاشی برای ادعای پیروزی زودهنگام.
@News_Hut</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/65145" target="_blank">📅 20:42 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65142">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sR5eJEw7GXesd6AdDDoEV0Vk0xU25M4t55Ta0B_hvstBb7QZgJ2jXUyOFpvoHtdC_KANmhns4I8xHo6VtUuRzYWrT310DkPyX8oT2T-fijKPjavBg351EsG9ZdpFskoJrHBPzyMNj6aDb-SvecQ4eqllNEOsFAhT8pDpihCCQ8fkCwpCyrlfxoxBh_zQ4ZJnGvBKK8Sep3pImIWirPTzjZx_MfMMvOO5mXaDel6uhmbMEmi-iod_O9UdK2IFqXl40-pW-G6HoiDZ-maZteg_vyc9vHFfjathYWChYIEyZUyUZUUAR8pK3_MH0DxFFu7R15UAn18QayoQZwpbHKL3_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف:
۱- امتیاز رو پای میز مذاکره نمی‌گیریم؛ با موشک می‌گیریم، مذاکره فقط برای اینه که طرف مقابل بفهمه قضیه چیه
-۲ به قول و قرار و تضمین کسی اعتماد نداریم؛ فقط عملکرد مهمه. تا طرف مقابل کاری نکنه، ما هم قدمی برنمی‌داریم
-۳ برنده واقعی هر توافق کسیه که از فرداش خودش رو برای جنگ احتمالی آماده‌تر کرده باشه
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/65142" target="_blank">📅 18:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65141">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">⭕️
🇺🇸
🚨
🚨
ترامپ در تروث : «ایران باید موافقت کند که هرگز صاحب سلاح یا بمب هسته‌ای نخواهد شد. تنگه هرمز باید فوراً باز شود؛ بدون هیچ عوارض یا هزینه‌ای، برای عبور آزادانه کشتی‌ها در هر دو جهت.
تمام مین‌های دریایی (بمب‌ها)، اگر وجود داشته باشند، باید از بین بروند. ما با مین‌روب‌های قدرتمند زیرآبی خود، تعداد زیادی از این مین‌ها را از طریق انفجار نابود کرده‌ایم. ایران نیز فوراً مین‌های باقی‌مانده را پاکسازی یا منفجر خواهد کرد؛ که تعدادشان زیاد نخواهد بود.
کشتی‌هایی که به‌دلیل محاصره دریایی فوق‌العاده و بی‌سابقه ما در تنگه گرفتار شده بودند محاصره‌ای که اکنون برداشته خواهد شد می‌توانند روند «بازگشت به خانه» را آغاز کنند! از طرف من، رئیس‌جمهور محبوبتان، به همسران، شوهران، پدر و مادرها و خانواده‌هایتان سلام برسانید!
مواد غنی‌شده‌ای که گاهی از آن با عنوان «غبار هسته‌ای» یاد می‌شود و در اعماق زمین، زیر کوه‌هایی که عملاً در اثر حمله قدرتمند بمب‌افکن‌های B-2 ما در ۱۱ ماه پیش فروریخته‌اند، دفن شده است، توسط ایالات متحده بیرون کشیده خواهد شد کشوری که طبق توافق، همراه با چین تنها کشوری است که توانایی فنی و مکانیکی انجام چنین کاری را دارد و این کار در هماهنگی کامل با جمهوری اسلامی ایران و همچنین آژانس بین‌المللی انرژی اتمی انجام شده و سپس آن مواد نابود خواهند شد.
تا اطلاع ثانوی هیچ پولی رد و بدل نخواهد شد. درباره موضوعات دیگری که اهمیت بسیار کمتری دارند نیز توافق حاصل شده است.
اکنون به اتاق وضعیت می‌روم تا تصمیم نهایی را اتخاذ کنم.
از توجه شما به این موضوع سپاسگزارم!</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/65141" target="_blank">📅 18:33 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65140">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/anmRNlOSpdglyNZre0F1KYGXmwySaZ039CoFzaxLYVQLMjb7BoC_Zs4JUTPZIEq6tjV7ew4hCk_5xF-66Z4jCeur3H1eF3lhQodpjlDZuL8djyzAGVMhELHP9BdJYbQoqDuY6ITcMfqn6zDyWw-tpy8okZBqZtdJwyBEzFyvcbKPV1DTLsFHC9egWQirJVK8C5EgmgOqFqI2awNlSq9YhANXq_Rj5FzoCGTPvQMiU0nLzVggpV0toVm7zndTBlZfjQo6dpkJlCjKAlAbeBTMWfP0u6kwZz5tVLgBseUPpWGaw-e_dQZjqP1vktxS56QJeCUu9eRIFF89gt53BDuBbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز روز جهانی مشاورین املاکه
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/65140" target="_blank">📅 17:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65137">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bWcuHW_Rvi6auQJm-9iToLztMXGB0CIXlW1l81sMhj3gqQ-HUx9VWWMmqvz3p3468GjIoT3zaEpN5vABub3bf5P3VW3SNEI9kV0vm5XOWiMsJi7VHOTDYlu701_KbF40WP_KAhE8_lSMnBEFdWMlZGRzBT6xRI91e2rvwLK6iXGY873nyOZaVF0ftZQKeukPeGw1qih3xnHvAcDZKuF_H6pvx1GcyEOMEQY5VcNDQCrhgFpr7VUQsd6bAbK0FzIf-6WJBknMnQDZatdsB24IHLOIxyiEfWYgPFKzrhchkizGiGvzaTLTnIHwouN6HYWJPbTs_UOaqHi40A_lw30dTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی شما نت نداشتین این دوتا شده بودن سمبل شرافت و نجابت حکومتی‌ها
😂
@News_Hut</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/65137" target="_blank">📅 14:12 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65136">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZX5d70O0VEwx5JLWu-EAJOmXEAhb5p7hEOXXb1yvevDAEQfguKx-gsRJ8j0OLKP7V68UQDnGR3sOLpW_cEeikElbunjuA9nOjSevoNkTcQCK0c5MSz4t1HBD_v44H0F4s28J2h4zpvYKFuX55kPjUcicc_b0X4jQWAhHJV-Jvz2Sjf0o_vufYS0bt3bV1x1YFSv-4p4vp4o8kZOZpKMtaWj0QZD_QeFuVw74BXUZIq_yDykW1IKs2x6Uc4uLDujyKeeEvTgVH9o0EYpMGxvKI9utuyJEz8AQW-21ED2mIWQ9IO5RDLNSsSkcy0gqvN45Xf0eiD_rMTUtE-vC5Tfuhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست‌های حمید رسایی تو کانالش درباره چه کسی شایسته جایگاه رهبری است با آیه‌یی از نوح و پسرش که حتی صدای خود طرفداران حکومت رو هم درآورده
خیلی‌ها میگن مجتبی رو به پسر نوح تشبیه کرده
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/65136" target="_blank">📅 13:20 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65135">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24db6374d1.mp4?token=p8Ayfgam-II1Xj-dPRPN-xZR788VEvqWnGE8qqrGUYpFDuScU1dxNORzxFjpsbF9BrdENYpBRZIaQ9vBv3h8uJpdayeX6Vn3wxjo3wA3QhyZeszkVvnkB7rh3Og6-tQVqOiCyYUu0O21EVcSdUW5EcnFC7ZDctvREH405FwxLFyHf-XmB_eVFvegqO3B2DviqGNpu89fS4LWH6x2nXZdnHT5kOPgDr0ftLDGZZNafZj__Hd7QZKcKC6ypiIILnPTYn-g5RLopo4RUMFngG2BLwiWhAe6l28-4Emx19QV_PbKkN35Rx47v4AS9yfnJ5GMif_12lQtlq3QuvmcC-1fFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24db6374d1.mp4?token=p8Ayfgam-II1Xj-dPRPN-xZR788VEvqWnGE8qqrGUYpFDuScU1dxNORzxFjpsbF9BrdENYpBRZIaQ9vBv3h8uJpdayeX6Vn3wxjo3wA3QhyZeszkVvnkB7rh3Og6-tQVqOiCyYUu0O21EVcSdUW5EcnFC7ZDctvREH405FwxLFyHf-XmB_eVFvegqO3B2DviqGNpu89fS4LWH6x2nXZdnHT5kOPgDr0ftLDGZZNafZj__Hd7QZKcKC6ypiIILnPTYn-g5RLopo4RUMFngG2BLwiWhAe6l28-4Emx19QV_PbKkN35Rx47v4AS9yfnJ5GMif_12lQtlq3QuvmcC-1fFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ماهواره فضایی شرکت آمازون دیشب حین پرتاب به این شکل پشم‌ریزون منفجر شد
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/65135" target="_blank">📅 12:58 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65132">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WwOaoSYTnDEr8BXKF3c6Wk1RM2wEq8ATQn8fNk7-VlOSty42hGoOJYjpFbqBsU9vzDblwynjPNG7ssWoyAD5nTn7v2qQZToWwWYdm_u8wBqte7wjupaskNdX-1h0R00P9x5hGUe3WWQurNmtJWrIpWkAdZxC2pl99_1q4LvtT_irfg4tISb8aMWYwucWRqObZ5h0pOHFKHg2ofpfa-KzQxl-km7EVIBAICZ3RrnaS7lyB6Zmkl3q4Ucc0FK-W3SJTvmlRAjNbcXoIVAVk8IGTw31fYM7Hy368NRjPs-LzAqf5MNP-0xBCpoug9ve99_Uii0iqCb7Yj0U2KzcL65MVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📰
واشنگتن پست: دولت ترامپ داره به اداره چاپ اسکناس فشار میاره تا ۲۵۰ دلاری با عکس ترامپ چاپ کنه
قبلا ترامپ ۱۰۰ دلاری های با امضا خودش تونست به چاپ برسونه و اولین فرد درحال درحال خدمتی بود که این اتفاق براش افتاد
همچنین طبق قوانین امریکا عکس افراد مرده میتونه فقط رو اسکناس چاپ بشه و از سال ۱۸۶۶ که این اتفاق بی سابقه‌ست
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/65132" target="_blank">📅 10:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65131">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d098f5f90.mp4?token=HFJAFqq-waD63tiCAZiIDWl9nLZTiinh1jzJCdQG9ogDWu5pw7moSJyOCQADE-2Wiiy0SbIN2msiAoPfJShc4mjfNCq7wz0vG1zOeKU-7kM6CnCYsDU2JEkggqi-PAAhx45O4V0jFkoavaedthvpwCEHYI5xcoRT_md8RglI0CLK2I39rXUJfaKwajEL5iE-NmzKEDACBSqkDpQPV9UbGPO5ufVW0L-7Ekn98XOkdVYA8-XpYWEktlRyi3XJ3Fwr3COgSD3ZRQPdTa2SoXSib9Hx78lbNWTYYPEcDu7MH1fiSOvZtZPh65u2IxV7EuaGDhj03mjj2tNyCalCMjr4Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d098f5f90.mp4?token=HFJAFqq-waD63tiCAZiIDWl9nLZTiinh1jzJCdQG9ogDWu5pw7moSJyOCQADE-2Wiiy0SbIN2msiAoPfJShc4mjfNCq7wz0vG1zOeKU-7kM6CnCYsDU2JEkggqi-PAAhx45O4V0jFkoavaedthvpwCEHYI5xcoRT_md8RglI0CLK2I39rXUJfaKwajEL5iE-NmzKEDACBSqkDpQPV9UbGPO5ufVW0L-7Ekn98XOkdVYA8-XpYWEktlRyi3XJ3Fwr3COgSD3ZRQPdTa2SoXSib9Hx78lbNWTYYPEcDu7MH1fiSOvZtZPh65u2IxV7EuaGDhj03mjj2tNyCalCMjr4Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: کشور‌های عربی مثل امارات و بحرین و مراکش برای تاسیس دولت فلسطین به پیمان ابراهیم نپیوستن بلکه چون اسرائیل رو یک متحد قدرتمند علیه ایران می‌دیدن به این توافق روی آوردن
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/65131" target="_blank">📅 09:54 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65130">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Su59KH_GUJEeRs6MH1xs8i3ygqwUg_bRKdBPNlifhZKDjDUOfrGxtRbBvlV4hD74rgS480cxzmpxcE4sNoq1GTqLk46n4g527udGU_-8DhvQdPhn_7gyjO_fAtqlYYzvdkSA44SC99TgzhUUSmZbbX5957llwMcqO3XI62VW7Btt6zCMeaIxFuN6mJpNiGAJaIX-4ZHDsUefCae_tnlJTFl5zMdbqGM5R3jcaNRaf73uTrYoQ0XMtpEKOGLexSCNzHhX1LHH1k8R5nW6juEHMDayMejXJkpbu5yl2eqJmG3CAAYO2-fOM02rPecpDZLC-3lXgaWVLnlgT29O15cdsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش دفاعی اسرائیل: از زمان عملیات غرش شیران تقریبا ۲۵۰۰ عضو و فرمانده حزب الله و ۸۰۰ نفر از اعضا رو از زمان شروع آتش‌بس حذف کردیم‌.
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/65130" target="_blank">📅 08:52 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65127">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
گزارش صدای انفجار و همچنین پرتاب موشک از شهر جم استان بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/news_hut/65127" target="_blank">📅 23:08 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65126">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/011753724a.mp4?token=W_frmRNM4PTfWr4SPvuv4qu1D9pzC1wEdpxJ06RWEoPnoDpLKSh-SKhy_SxT0T3mbqTRF292TTnlvmb5-j1yKcM7qemX0qQdby4JrLTv_FwSHQBClHxtlejDQeWsWgOBKfiv6q7phIwCe7_-p6BPTmu-UVv_2Do1LTdvyWEQLPHwX_KX7W92jj91sIA_pku0J-R5hMfjEg-YDtysh5nj1VRyJnXlFjsZ-RrE3JWx_9ugP7QKbAqEQsyCh-MbOQ3WQAV3Dr8S531LB_RE_Yz89-zIYlG-pmW4QkHJx36NJ4T2V8yZQXtC0dW0Nk2uhY3k_T8VxQb1nJxPnRjXn11-rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/011753724a.mp4?token=W_frmRNM4PTfWr4SPvuv4qu1D9pzC1wEdpxJ06RWEoPnoDpLKSh-SKhy_SxT0T3mbqTRF292TTnlvmb5-j1yKcM7qemX0qQdby4JrLTv_FwSHQBClHxtlejDQeWsWgOBKfiv6q7phIwCe7_-p6BPTmu-UVv_2Do1LTdvyWEQLPHwX_KX7W92jj91sIA_pku0J-R5hMfjEg-YDtysh5nj1VRyJnXlFjsZ-RrE3JWx_9ugP7QKbAqEQsyCh-MbOQ3WQAV3Dr8S531LB_RE_Yz89-zIYlG-pmW4QkHJx36NJ4T2V8yZQXtC0dW0Nk2uhY3k_T8VxQb1nJxPnRjXn11-rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آیا کاهش تحریم‌ها برای ایران روی میز است؟
اسکات بسنت: هیچ گزینه‌ای روی میز نخواهد بود تا زمانی که تنگه هرمز باز شود و ایرانی‌ها موافقت کنند که باید اورانیوم غنی‌شده با درصد بالا را تحویل دهند و نمی‌توانند برنامه هسته‌ای داشته باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/news_hut/65126" target="_blank">📅 23:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65124">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🇺🇸
#رسمی
؛ توافق موقت ۶۰ روزه‌ی ایران و آمریکا نهایی شد و متن توافق، فقط منتظر تایید ترامپ است، هرلحظه ممکن است خبر اعلام شود
@News_Hut</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/news_hut/65124" target="_blank">📅 22:38 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65121">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fbdc689a0.mp4?token=mOMvD1FCyt6Vti5lcHKHFvmFVTf7kFwdunAGjOU53pVllk420IfY2IsG0e4vC9M1VbwsHwSEdaj0_6SyP0Mgva-f_TqQG-nyZRiJHZd5vjAxrSS0w7EbGDMwAkrlgP74hZ53TyZsWIc6aSu-UIpEPaba6TdCmVPVfoU5NzcgtcCJG3FG7XxgO8GCFxyYLfZxiEfxfEoP13s_MGDQvqzHWFruF4_hY0UP61oxBtJ_9ZTGcgVcUkazXuYwWHEujO60EcNFBdNWn9m_bdKQwsvVl_YWk5dtFggo30u7lyPUdHFHk5NdiY5NlYTcs-iN4a6E7riXuw5UApIt2Kdk-cjlqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fbdc689a0.mp4?token=mOMvD1FCyt6Vti5lcHKHFvmFVTf7kFwdunAGjOU53pVllk420IfY2IsG0e4vC9M1VbwsHwSEdaj0_6SyP0Mgva-f_TqQG-nyZRiJHZd5vjAxrSS0w7EbGDMwAkrlgP74hZ53TyZsWIc6aSu-UIpEPaba6TdCmVPVfoU5NzcgtcCJG3FG7XxgO8GCFxyYLfZxiEfxfEoP13s_MGDQvqzHWFruF4_hY0UP61oxBtJ_9ZTGcgVcUkazXuYwWHEujO60EcNFBdNWn9m_bdKQwsvVl_YWk5dtFggo30u7lyPUdHFHk5NdiY5NlYTcs-iN4a6E7riXuw5UApIt2Kdk-cjlqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درحالی که جمهوری اسلامی اصرار داره یکی از بندهای توافق آتش‌بس تو لبنان باشه  نتانیاهو و اسرائیل در روزهای اخیر بشدت حملات رو علیه حزب‌الله افزایش دادن
@News_Hut</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/news_hut/65121" target="_blank">📅 22:08 · 07 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
