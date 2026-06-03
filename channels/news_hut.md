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
<img src="https://cdn4.telesco.pe/file/pUdZ3zBioOzRsxJo2WVcvnVfoAvoJaQGSPR52ImHFzLgNXWK1oWuAYXoErm29hY545LbsLyvhZt8lgWI2pSIUdFnFg9mJjYmMJZ3b_j91hl7jahyPFPrO_uBpU_Ng3-Kl6xy8ZzkFYjX9xl3HBCFBn51CQoTsFuPCkg66zl4q2uLYgItnAoI9XuH-j94PmwMenia1vYLWKVHw8dkHg9Oo82YsYzXnO1Pfqg1rj8u4SPADi3k4jOWF52WXaJ2TayF0N8vArtexMUrqrvwIZYM6JiRdA_NAinozhJ5grOyDixlrmxLEOyUcF4ghBAcHPQJV8_fj7TyFhIBTv4iwNbSOw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 225K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-13 15:47:09</div>
<hr>

<div class="tg-post" id="msg-65265">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/news_hut/65265" target="_blank">📅 14:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65264">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/news_hut/65264" target="_blank">📅 14:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65263">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/news_hut/65263" target="_blank">📅 14:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65262">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/news_hut/65262" target="_blank">📅 14:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65261">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/news_hut/65261" target="_blank">📅 14:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65260">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
📰
#فوری؛ نیویورک پست: ترامپ پیش‌بینی میکنه که با رهبر معظم ایران، مجتبی خامنه‌ای که احتمالا همجنسگراست، دیدار خواهد کرد؛ «رابطه بسیار خوبی دارند»!!  رئیس‌جمهور ترامپ در مصاحبه‌ای با «پاد فورس وان» که چهارشنبه منتشر شد، گفت انتظار دارد با رهبر معظم ایران، مجتبی…</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/news_hut/65260" target="_blank">📅 14:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65259">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fU5vf017DH5K0K2rJ4sAfabkSz00gHeSs81upJzf0LAoqkefl0J6Ve2bMrFo1PmTST7Kzfk73sNLK7gmwc_OiEVv4CpsBwDnqkjsQ-viy4dio6_nZmOriU4CjxdE_PAegMaNygurlwZNrmR6ccxmGtFRKDHF_2cz8x7iB65gPGpbBxp5m9pG1QYfXKcap104alvbqICVECC9m1T6AOfBnvdCgnruCyL7FffACUk3eklJUI5EbZ7zyJXFlrRAVgLhJbddv5QSyT_q8L7LpbEcN5DmWdASKNxzyB8jj841qJ21YT-WVFt3FzDidTHuHukucIvXpXQpkKGzNBeDXi1XnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیست قیمت جدید و نجومی خودروهای آشغال داخلی:
@News_Hut</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/news_hut/65259" target="_blank">📅 12:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65258">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qcVyN21k_wYF1g4C5KypUkxjqkC6ZfeF-_kKOTWqsueoiCjvfW0vJOZxaGu4iV0KHV40dGwS6Kjp2fQXnSUfRTUBYf-gU78KpypI7BH04Uo_9tlWoOb6yubEC1eVukkLD_BCG0Wa7Vbvh38sP8eBZNslkSrnoODhOK2FNn1PNpHvwqjO-AzjN6EZEZ6TVtHuIQMwrru8zJD5B3n7X7KuoPdXESQMV5sPPLKIJ69UJSapvqYf9tJw4L7hJwW2MQ0qQAYBHE3XNLq_Kp7g3cSwtUstj-MargDQ8Hh5RQZHNMNVfi-RbliF1Zi6g7UKf0OS-KeGzkxVA6JznU_77vNM5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکنا: آخوندای قم پیشنهاد دادن علی‌خامنه‌ای در قم دفن بشه
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/65258" target="_blank">📅 12:22 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65256">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hf8EEJgL-c6J3PSUgX5B6Bex75Sy2z9Moy3KWfKKf4rfxObf0ujs_kygjaiM-6-iCrpQrbR0v4vmdontBJkPmASYkBiWdK7vT7tPVbr4YLtoAuZOJxJYOFK9IeUUh4_d2IeEGoM-nUzbANnrmDl902ddoHiAGbMUuhJc05mXygpGoTXXgXBwvnLLGaWKLe8VsI_x8CwM26c71cVpu_mlU622-p4AfLhovIUAnH_LCHWLH9_XDh77p8vR9QHKjn3COwfT6QYL3OAEFM6I7Bc9E-hvlUY7QsGlRHm20iKm6iR4PALO-JL_Dnc0bWwTQY_LJQJgb7VrVqHW6tKUHPsnGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aLKYwPa5aNodM6sNNIXta2yqrB4YXJuLpJusGQGcG52Hl-CnYOQUXKjhaL_hL-5nH1_ABIdOa-egm9Vh8AK9WfWJuZMs3DgAko3w2pFbYFC0gNvQcb998ig2niHIv_kFLcqBVgMLRRLlQlOE5Qc8isb9L84lx1tmqRTnKGAoXO1__J1JCkRpX0PzQR9kr1CPOEeYv4HvoMHpsK0Udah5hLH8F7UoLNUnUBfuNw4vEI-0yZZQHIud_JjV_8uiGnn8sMrC_kKoDhW-_fxkDnev-x1RsKcPVZvpPgbmHM2bHnPmmBjke_joHFvEvi8xr4U-u85fC-PDFNX8zucDTy8XgQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
وضعیت فرودگاه کویت که گفته میشه مربوط به حملات دیشب سپاهه
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/65256" target="_blank">📅 11:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65255">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vYmtunbqNlC3nor_cdTSGPV5BINoZTHo8GnRO6Z3_4QRAg4Yy0rGt0HqLjiN-BSKfVb7EKhvfcSff-M7Tzb17V9Wrpgsg6B9Qzg4M7X82Pz9RO2wvLPTuHvvGLwStxbd3Nu4xZsB-Ze-xFKIBWIjeNRAlxS55QVQeqLAVlEPrtR5M0UZT9lWllHlwHQboMPsZfntxrsbqfXfqNlFkI6YUjBLVKBjhlf8J-4M9Ov38KtdxNDll5XOgAhdAsk1BkaaV8t_Fl-OZmup2tQbgRB03JKVjgNVdSSYT-SZiLkvqJZyVr8G2q5RrXV0PCunJ7_ljPya1yBc4JlyhgHHst_h3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیت کوین در ۴۸ ساعت گذشته بدون هیچ خبر منفی مهمی؛  ۸۰۰۰ دلار (۱۰٪-) سقوط کرد
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/65255" target="_blank">📅 11:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65254">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">طبق گزارش سنتکام، ایران چندین موشک بالستیک به سمت همسایگان منطقه‌ای شلیک کرد. همه آنها به اهداف مورد نظر خود اصابت نکردند.
دو موشک شلیک شده به کویت در مسیر خود به هدف نرسیدند یا متلاشی شدند.
سه موشک که به سمت بحرین شلیک شده بودند توسط پدافند هوایی ایالات متحده و بحرین رهگیری شدند. هیچ پرسنل آمریکایی آسیب ندی
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/65254" target="_blank">📅 11:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65253">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">هواپیمایی کشوری کویت اعلام کرد که حمله جمهوری اسلامی خسارت شدیدی به تعدادی از تاسیسات فرودگاه شهر کویت وارد کرده و همچنین شماری مجروح بر جای گذاشته است.
هواپیمایی کشوری کویت اعلام کرد که ساختمان تی۱ فرودگاه شهر کویت بامداد چهارشنبه با پهپادها و موشک‌های ایرانی هدف قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/65253" target="_blank">📅 11:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65252">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bac9b656e.mp4?token=AmID9XKlnl_cL5lHOPweTkGFEO3z413fNUc8g5A_VZuRBohGNSpts02e6JmIvGvIT9cwMYpp9DeDSmV3Dsr8I74RA_VQ0REz_t0wLHfXSW9VtV3NdM4XdFeIOIJXFDYSEeQ4T4qKJa4AUIYp9LZvGnbiaY9aCnz2LC-CgB10iLhMQnu6DavGvOgM3Lx521AenQ2fYivQyV7g3WkXmP9yiMvhdJGtL5NkvJNo--9fdVA6C3f6zlCi2euRzWKaFTVQaAGzo1HtJHKefnhGKQTM2t-2g21bbvZKCW8M0ldjwpN_3sv1SxSYoN9dSIofMIdmlQXIpOC0Rm0B8Ee59deOvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bac9b656e.mp4?token=AmID9XKlnl_cL5lHOPweTkGFEO3z413fNUc8g5A_VZuRBohGNSpts02e6JmIvGvIT9cwMYpp9DeDSmV3Dsr8I74RA_VQ0REz_t0wLHfXSW9VtV3NdM4XdFeIOIJXFDYSEeQ4T4qKJa4AUIYp9LZvGnbiaY9aCnz2LC-CgB10iLhMQnu6DavGvOgM3Lx521AenQ2fYivQyV7g3WkXmP9yiMvhdJGtL5NkvJNo--9fdVA6C3f6zlCi2euRzWKaFTVQaAGzo1HtJHKefnhGKQTM2t-2g21bbvZKCW8M0ldjwpN_3sv1SxSYoN9dSIofMIdmlQXIpOC0Rm0B8Ee59deOvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلمی از پهپاد شاهد-۱۳۶ که دیشب به سمت آسمان کویت درحال حرکت بود
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/65252" target="_blank">📅 10:54 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65251">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
🚨
حریم هوایی بحرین،کویت،امارات به طور کامل به روی کلیه ترددهای هوایی بسته شده است
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/65251" target="_blank">📅 02:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65250">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
حمله سپاه پاسداران به کویت  @News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/65250" target="_blank">📅 02:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65249">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
حمله سپاه پاسداران به کویت
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/65249" target="_blank">📅 02:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65248">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/65248" target="_blank">📅 02:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65247">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromA.R.I.A</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HViQfnAbGpVLI5Gx23cwMXvIIOhEECu6JjxMCUiUeUvbgYGDlO1QkIqwrw9T15vcMAdUL5MK5B4Iw4FGrd_dek9HKNBBdPuf4jzk8ro-w9fDD9nDnDNlEnU258koVUeu7kJ_2Wz9d6NuZ1FsUNr7yRURIj-OqlXI2bxLMcie9aB0oQy03Au_JURNCmaflu_iKNS31AULqVSGdRTjpvtODM7S68E8PRG281jx9g0CJLyeq69fDS1zH1ZKi5gMAw_Z28CmWWmLKEXeknH4Sh8vFL8HnEHb3dsSVqSuN6rBIxgFycd3pWjuzzqBcsP2CU4TDTneiW7_KiKwiykdxr4vfw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/65247" target="_blank">📅 01:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65246">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
آمریکا بزرگترین صرافیای ایران یعنی نوبیتکس،بیت‌پین، رمزینکس و والکس رو تحریم کرد
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/65246" target="_blank">📅 00:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65242">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ku9d9iKsvD22FpmLk2jFwj0_ecmg1Ry5uEO8JlgsFmo3Jl2YMV5J1YF9HjtblXyJTKo80C7Mnold6XoVovYoF02OTIHiPSlDbnBrMoo8YwyomO7MxfzFS7mQ8TBrJAZj63dYIeafSi8CzV5t6GZ_ggzZUsq4aZTk4Jv2l-JL_2zw_4BgwH8zgJB3cfwxEjD0SoBxVwrPDI41badaJAny76gRqnfVuyaudR-X93TlOll7txxX0uJLBsDQ92Zi48eoRR7TB_1rRa4gd2p342LCZ3r7nJmBIj4kojgI9KHub5_6QNyWKJVawvX5PGE0Kp44HWcUWS2R9ICywfFfud5rNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pLt6jmARb6ZOmmMrIeLj9LeW-3bzkYr9DQcwOwt2fCDMYWWDDpl7rSU2UWiRdAWMlQagZO9wbN_n9imsNPBslfi5jYJq0KNJWxAe_n85OPBgon_PRiPJwgQXbrAFM5hK9dh9pXr0EK7H7R7I7rFNhb4QA9H5mdNbNGcnJK3csJ_XnN4M49FPO_N24OsdvwO38iztM3qUsW598bPCYij230boaF4-Fkr5eQr_iFEdVN0QpSTyPEMWURGlS5oJIra8k9cS2jl2T6qny0SKZkGXy56MOAXdr9bYoS0aOT4mUOo0UP5dMvERmOVS6HwuD0fpf8sBPUPXnFlz5aIGUSO3GQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یه شرکت به‌نام دکترتور اومده تور آب‌بازی تو چیتگر تهران گذاشته که مردم از جمله دخترا و پسرا میان بهم آب میپاشن و هم‌دیگه رو خیس می‌کنن
ولی خب بعد چند ساعت از بالا دستور دادن همچیزو کنسل کنن
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/65242" target="_blank">📅 23:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65241">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H8M3OwsPa6Pk0mbONLPOXfacatB-sABeZe0duoy6NyptYbZpDpfB00P7UAl66BklKOv6IWouW878iSCyJoL1aqWRGESJBnQbYEC7zuO8XF0PHDHeLTAR7C3Tf9jxaTPn1lM7JEr9-pOBrIg8ERw0KOfshmIfDjX7ILnbEHc8J97ewfWqj78jkGyDIHBl7etlJcqhTR_1Apj9On_hH3u7JScZm_zInIgnEmKvFKD3uS1-gPeV5gxVn3qjz5cP-4jLd-EPOUViqiAxNiK7YymjTS7S-VC9gC5jD67R3SWghLc4rvI9WbEshC2BCansqpKnF6x7PdUDG4NvASrDijnqUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سنتکام: ابراهیم لینکلن و نیروها همچنان به محاصره دریایی ایران ادامه میده و تاکنون ۱۲۲ کشتی رو از مسیرشون تغییر دادن
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/65241" target="_blank">📅 22:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65240">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Etu05lbtOvyBbiUa8o5fbQR7tmHbcxHgsA26GYvtaahKgW4-TnZwHfvLR5F-z26I6VkJ6dPeMIMgsQvbfVflzMaq2vnwF8Sou7nw2b57qKiJIYE9iY_IbvJemI0CY5Eh5oVHlRatxNOdyz-SdUxf5ISvSXfm_NYG7JPveZsCwZRQlt8lfCRhWva5Y0VCdHR8N3uayZlSkqnSCRnhmyJN20gRTzvy7PzeF80mRDZ5gnX01rpSUx9WlaTNC3t10AVsVz-HB9cF_wI1w_N3Qkud3PXBm0griCI8MVeDr0JQzOMkMebvQVUF3V31FKnCnkQjc1u-ZJoJYFWYT9OLurKwvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق آمار، سالانه 60 هزار ایرانی بر اثر مصرف دخانیات فوت میکنن.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/65240" target="_blank">📅 20:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65239">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/65239" target="_blank">📅 20:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65238">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ax3l_9pjVyrvlUn1BQAFlYod7_6PkMBscGDNQsgvupI30KklaQKN4g5i2PM6ihZpwBZVZcSLCPs5OFL_cIm_iOTRWiDeFZHwYnLtcC-DrCfmzM729l9wrN7MwetzplqmHwVVlayP5R2_tUElQMmPqn6oam1fGi8BKkPeB2UJPlfwGe_BwszpQYleV-nzXVeIodiPFrZvPF_3w_0m9KVZYvrZG5znwTMokyA6hkY2UQLMM5BIO_4j0Hes0sEXjDFkvzt0KnWLyfZJN0GXWPUXSlNHq-vWF7K7HCVIWx2Ggd6wiSrjtv-WxAt1KdX5Afl2l_rCF8AY9_gK6KSes-sgXg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/65238" target="_blank">📅 20:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65237">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
امتحانات نهایی که قرار بود ۲۱ تیر شروع بشه جلو افتاد و رسما از ۱۳ تیر برگزار میشن
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/65237" target="_blank">📅 15:18 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65236">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BtSU2scYEA6iSyPWCCtIs6EgdQWfOk6dQF76AAStgtA6mqCaTE2rEMdMM-CjY0SvpfqN33y_Gj9yFBIxGXqmFbnvrpknmhQWNfTL-j7ADSVdB3gJPfvSex3kVOAnpMO27GLcN30gAZ0Uul8RHV8pkQTYFBbLJds-36wxyf2N8CC1OT9mIf6YTWoXMq4BW_LheZ_-9yENnpM1Bay_4jJv-S24Xj8rJpXFcWXF-HfNsxpo6ZSF7X3rmviBVRr7mGVH6jiWseCYahRowInXkJ5bJdrlPZQZbMXlvNUbaQYDhn-9vSstJhGLLlDmh3Z8qrlyHnoxTSW7NLYRKvMs5LxsRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
داعش با انتشار پوستری، جام جهانی را به بمب‌گذاری و پاپ را به ترور تهدید کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/65236" target="_blank">📅 14:58 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65235">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a43d73ec7.mp4?token=p7GICXvD_OHlPJCC8kZTM-MIoU6qbs5PNNporxBC9rgEfUknt1LIlVluFOMChw_B5KEO0WyTCferzjNxhvBeCDdZK5tdKbKVkXgavSsmIcyJUVU_qSnlOgLYTj8GLCO7beQkw_ygGr6y2cPwmR_NR_o2l7MlO969LFsvYzsWwSgs7Ik5HE-JXK_zz_k18U2udZPlqIC-nnbsGaEAFRDz2uHH6EzH_Xbi9eq8JQ9R4jhP6mBSUyXyI4DH8XdD1TPMWr3razAub2DwmLrs3ppwzPnspYmSy5VE1roKBJJM_3ifkyHqdint-hfaXDlNNGyNHK0vXQqMPegvwkLPnL2P1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a43d73ec7.mp4?token=p7GICXvD_OHlPJCC8kZTM-MIoU6qbs5PNNporxBC9rgEfUknt1LIlVluFOMChw_B5KEO0WyTCferzjNxhvBeCDdZK5tdKbKVkXgavSsmIcyJUVU_qSnlOgLYTj8GLCO7beQkw_ygGr6y2cPwmR_NR_o2l7MlO969LFsvYzsWwSgs7Ik5HE-JXK_zz_k18U2udZPlqIC-nnbsGaEAFRDz2uHH6EzH_Xbi9eq8JQ9R4jhP6mBSUyXyI4DH8XdD1TPMWr3razAub2DwmLrs3ppwzPnspYmSy5VE1roKBJJM_3ifkyHqdint-hfaXDlNNGyNHK0vXQqMPegvwkLPnL2P1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
علی‌رغم درخواست ترامپ برای آتش‌بس در لبنان، ارتش اسرائیل دقایقی پیش مناطقی از این کشور را که در تصاحب حزب‌الله است، بمباران کرد
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/65235" target="_blank">📅 13:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65234">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f14e605921.mp4?token=Ftwk83_HP2cVcfSVxkYOvkew0aMwBq96rHhh6Q_-pWBIFdkQ2G8DO_iQ22hG7AiWhMNQ13wUxa0FU5EeJrb_aaBUivh_E6Cf83QG1lIbUmFp7Tzx9S8v8u4sGZWVbp2H4GAnuQboHdXLHJoqC8VFe4eQTBxtTHXl4tqRfgYFp-u8hwkAYAuyyCtpaVCcmseuqUk2EiWbLX5f4KKR00aR7sNXm8ghEWM_xv6tkZX6YPiFEvTh66ifqfcImEJ68oGesf1d01eeQRKDqWQicCZxMFw37PSja442EI9ZCiZPUdHw6tnvMxo7Xc27U-HspQcyMBT9kywJbvU8TxBkJCfXBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f14e605921.mp4?token=Ftwk83_HP2cVcfSVxkYOvkew0aMwBq96rHhh6Q_-pWBIFdkQ2G8DO_iQ22hG7AiWhMNQ13wUxa0FU5EeJrb_aaBUivh_E6Cf83QG1lIbUmFp7Tzx9S8v8u4sGZWVbp2H4GAnuQboHdXLHJoqC8VFe4eQTBxtTHXl4tqRfgYFp-u8hwkAYAuyyCtpaVCcmseuqUk2EiWbLX5f4KKR00aR7sNXm8ghEWM_xv6tkZX6YPiFEvTh66ifqfcImEJ68oGesf1d01eeQRKDqWQicCZxMFw37PSja442EI9ZCiZPUdHw6tnvMxo7Xc27U-HspQcyMBT9kywJbvU8TxBkJCfXBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🔝
دیوید بارنیا رئیس موساد:
تغییر رژیم در ایران یک هدف ممکن و قابل دستیابی است. این یک وظیفه قابل انجام است اما نیازمند تعهد، صبر و فداکاری برای هدف خواهد بود. این وظیفه باید در رأس اولویت‌های ما باقی بماند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/65234" target="_blank">📅 12:56 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65233">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b11e2b7f3c.mp4?token=eEOj4Tife3CVH2c3kOJTR3HE1icNc8JrvUTzgJZzJKSUubn2INU_uI3cveBZpIj2SjFUz1MgrmFdB2oD8YbaziH_G6lNPfW1t-QTiU4RPwnF0AvB2eItB6hGudByUj-kWy4RzESsmVTfqiupISMcbJdW810Hfavu-n9KKMfZygRMyQikwIJk-ckT-DtOxJuNAjP6Hx2YgDHoZWRewyKfIYao_By8M9sgDaKjYdqlOme6WTcuwfzhNMaH-2NwTkYpHf_2HuDkPibOoo_905bLk5DaYyrYrQ8nEUFmCl4QL6b55q7ugeCA2hJX1pusoyjP_rqcL6pdtxyrwRi0VAnwAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b11e2b7f3c.mp4?token=eEOj4Tife3CVH2c3kOJTR3HE1icNc8JrvUTzgJZzJKSUubn2INU_uI3cveBZpIj2SjFUz1MgrmFdB2oD8YbaziH_G6lNPfW1t-QTiU4RPwnF0AvB2eItB6hGudByUj-kWy4RzESsmVTfqiupISMcbJdW810Hfavu-n9KKMfZygRMyQikwIJk-ckT-DtOxJuNAjP6Hx2YgDHoZWRewyKfIYao_By8M9sgDaKjYdqlOme6WTcuwfzhNMaH-2NwTkYpHf_2HuDkPibOoo_905bLk5DaYyrYrQ8nEUFmCl4QL6b55q7ugeCA2hJX1pusoyjP_rqcL6pdtxyrwRi0VAnwAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
امروز دانش‌آموزای تهرانی در مخالفت با تاثیر قطعی معدل، جلوی وزارت آموزش و پرورش تجمع کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/65233" target="_blank">📅 12:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65232">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/65232" target="_blank">📅 12:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65231">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CAs0XlEOJ7ghTNv0SBdV-9O5Enwt3ARksiZ8Jplnw0ecUf_KZhcSzlUSRwpwaIAA_S1In-r1h9WRSjnQhXLjPdaAZB1tDA2TMe9gzXgreuaLGqKaavol-uPK8ceF--x8_fZS5hJjqVWEIxjaFZaBiBMG2RPMdGvWa6kDfQ0kz4UlYp7TTiBq6MVqvBnanwS--ajLaApSAhIjLgFHKOFA-UGrnD8yb-27JycImi-4GtFwJ_PcFFX8lx4RJT9pe9jqb4QvQFxWYh31S1FrfJnB11GmPOUMGhYBCwHg0BvgnX4ZH8irs4e_J_Owp97v5CD_pcfewXeLRbMsRMursfPkCA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/65231" target="_blank">📅 12:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65229">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e2d6ed8f2.mp4?token=okhSm0nRPh2awinFtcjFn_RdUJ_Ajqh6pvBcfwnZFmU8dyP7xBeeAfKXD7caOrhdWPFwbYkpKbWt4njHdBkDViKyMCLyBZjY8bBra5BgsTxcUhJSvJzX6yWtxGDEUhJZVD4aTwt7axGEM_G6dskpKn9SujN62g5dm0AVomC0rPZ_NIm_DaZ7i5ht3yqcbQsU1YOl4tuLUN64yYluETniv8Im2bU1rxtBXocS7DAQClKIGwHzP1laVZgurDSF4Mp0K6__ew0ptCGJR2_phr-DW83v9RySVPGEyKvG7TeLq4zH1eXo8w4bGNz1uOppeMlK6vV0UmBtQ2nCe4UUt4BGPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e2d6ed8f2.mp4?token=okhSm0nRPh2awinFtcjFn_RdUJ_Ajqh6pvBcfwnZFmU8dyP7xBeeAfKXD7caOrhdWPFwbYkpKbWt4njHdBkDViKyMCLyBZjY8bBra5BgsTxcUhJSvJzX6yWtxGDEUhJZVD4aTwt7axGEM_G6dskpKn9SujN62g5dm0AVomC0rPZ_NIm_DaZ7i5ht3yqcbQsU1YOl4tuLUN64yYluETniv8Im2bU1rxtBXocS7DAQClKIGwHzP1laVZgurDSF4Mp0K6__ew0ptCGJR2_phr-DW83v9RySVPGEyKvG7TeLq4zH1eXo8w4bGNz1uOppeMlK6vV0UmBtQ2nCe4UUt4BGPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
واکنش یک‌عدد ملا در تجمعات شبانه حکومتی مقابل یک ماشین با چند سرنشین زن:
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/65229" target="_blank">📅 10:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65228">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e2983c9bf.mp4?token=N54doUJvXL62LGU5Y1PcAN4_xUwzK0hkrdMFmlCSCSIX4_pK2TevbU5kq5xTtV6XwyT5o4jZ_cafI1-INETjVaoQpSV39V9h5DeSxVNBR4f2lDqmkehd55oFyFBa7e4tO5nt5c9CQ8QpVGYSwioqnFa4PS7-UIIq6XB2_ZINLRLa08SIyTh7FXhyLW6m3_zEaZ9OQIRouhPwFub1IeDEbFgfJqIHEx0_qLmn-vfWKLSZ4lDMkQ2_rPq9sgd4bY52RBE3A0IJOJnDho96RZSGUHKCUAQExdtY_XAzsArOJ-AgL3x1Q0rjs0d46A_0ay56NkLannT94jfK8gPTY0DvEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e2983c9bf.mp4?token=N54doUJvXL62LGU5Y1PcAN4_xUwzK0hkrdMFmlCSCSIX4_pK2TevbU5kq5xTtV6XwyT5o4jZ_cafI1-INETjVaoQpSV39V9h5DeSxVNBR4f2lDqmkehd55oFyFBa7e4tO5nt5c9CQ8QpVGYSwioqnFa4PS7-UIIq6XB2_ZINLRLa08SIyTh7FXhyLW6m3_zEaZ9OQIRouhPwFub1IeDEbFgfJqIHEx0_qLmn-vfWKLSZ4lDMkQ2_rPq9sgd4bY52RBE3A0IJOJnDho96RZSGUHKCUAQExdtY_XAzsArOJ-AgL3x1Q0rjs0d46A_0ay56NkLannT94jfK8gPTY0DvEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
نواب دبیرکل حزب باقر قالیباف: آماده بازگشت به جنگ هستیم
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/65228" target="_blank">📅 10:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65227">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/159f752950.mp4?token=JeP6l6Y9OsOtAHJYILKjIEWlshZ9z25QYRxxvobkhkE9MAWqOvrncol8U_S0J3Yp9fC-erSt6Q2os03yYmnNK_szGhwx9FxGB3hYoUJ1sdh0FFfQ2BwqPhRfKuaJe4jz4ZCbIFv4XMonk4ByZTA1OX8Dx2VjEmz33YTCcD_-wXdm4sAPeizbugA_5a1bDDPGYiVGK6mn3QpxODbu4D36bmg24P2NzeIIegI86HCcY1ciShWRI3J0jNczV5INUCLGlo4vMtpZWElfy6RKxgCKg_glryi3oV9JArYuD1L9IhziPdQZPZXwPKg3j8THA-ZDRsIEEJqs3i25x6cDy0-bTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/159f752950.mp4?token=JeP6l6Y9OsOtAHJYILKjIEWlshZ9z25QYRxxvobkhkE9MAWqOvrncol8U_S0J3Yp9fC-erSt6Q2os03yYmnNK_szGhwx9FxGB3hYoUJ1sdh0FFfQ2BwqPhRfKuaJe4jz4ZCbIFv4XMonk4ByZTA1OX8Dx2VjEmz33YTCcD_-wXdm4sAPeizbugA_5a1bDDPGYiVGK6mn3QpxODbu4D36bmg24P2NzeIIegI86HCcY1ciShWRI3J0jNczV5INUCLGlo4vMtpZWElfy6RKxgCKg_glryi3oV9JArYuD1L9IhziPdQZPZXwPKg3j8THA-ZDRsIEEJqs3i25x6cDy0-bTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
🇱🇧
درگیری تن به تن نیروهای ارتش اسرائیل با حزب الله در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/news_hut/65227" target="_blank">📅 01:43 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65226">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f218bec310.mp4?token=vIWnVf3bos8OsPExTjdMH1qkBedu1EpT8wYgnkE7dc9BAMCPzwnF42w9gALIbAQxiwcqeB2BmcYU2NxwNZbwe99kHli9EXC1Op2LqUyGRCGFd-uo6lQbKhOjdfgZ6Z4p1BTunq29p5JR3K3F75wCznCQ-a746XYh0108hQ9SXaJm7UcZDbtpY0CDpy-9waYgzxHAKcC9G0LxPpQu6S-D8-X93qa_yfWecJonuXc3DQRfv8iSU3im-yMmlyetGomaasP2tVxWC9lHz_NBVrF0iMl_ZtYAkt8l_p7cEqVMb2n0JTUnR-AiqI5dmf4WWwrSnVJUhmaL3s0A1lBwlg257A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f218bec310.mp4?token=vIWnVf3bos8OsPExTjdMH1qkBedu1EpT8wYgnkE7dc9BAMCPzwnF42w9gALIbAQxiwcqeB2BmcYU2NxwNZbwe99kHli9EXC1Op2LqUyGRCGFd-uo6lQbKhOjdfgZ6Z4p1BTunq29p5JR3K3F75wCznCQ-a746XYh0108hQ9SXaJm7UcZDbtpY0CDpy-9waYgzxHAKcC9G0LxPpQu6S-D8-X93qa_yfWecJonuXc3DQRfv8iSU3im-yMmlyetGomaasP2tVxWC9lHz_NBVrF0iMl_ZtYAkt8l_p7cEqVMb2n0JTUnR-AiqI5dmf4WWwrSnVJUhmaL3s0A1lBwlg257A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
وضعیت عجیب جنوب لبنان پس از حملات امشب و امروز اسرائیل
@News_Hut</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/news_hut/65226" target="_blank">📅 01:32 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65225">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-poll">
<h4>📊 اخبار جام جهانیو پوشش بدیم</h4>
<ul>
<li>✓ 👍</li>
<li>✓ 👎</li>
</ul>
</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/65225" target="_blank">📅 01:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65224">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">رئیس‌جمهور ایالات متحده آمریکا یک «تماس بسیار خوب با حزب‌الله» داشت، که یک FTO (سازمان تروریستی خارجی) تعیین شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/news_hut/65224" target="_blank">📅 22:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65221">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zbl4PsbquC4mz0muOoRR3_DoLGEa_FvWKedTndHj8LcthbwdHf7SG_BEevZf0Kx1WUgeeUsmtHEBtBcbr5Dy8uWSKwhgnvMpw3zzj3bL8m5DUlPWePJCYLKRxeKyqwYqNA3pCo-83G45BJJf3Bt-uBhMKAtWbzpCsgbSdb-SlP5BhrbmOa6RcN_ByJiXVS7QiE7Y5U6OjLJOXwvu_c3bviF8871niK8sp_DHmLfmy1nv5g7P3yM8oDDUkuEcXGb2icsHxesKg9_-SvOCYCnGd9PKnktvOxXMmwIBuYnNj4zs_396Wini_Mgz37fA7m5kJN4qS58wuOnpWz8A6Yp9ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ: گفتگوها با جمهوری اسلامی (ایران!) با سرعتی بالا در حال جریان است. از توجه شما به این موضوع سپاسگزارم! رئیس‌جمهور دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/news_hut/65221" target="_blank">📅 21:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65220">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V-_ttBnOqLj9KXp8Nzb_UR4X89wudiBQtSTb51aBEeZuHfadGuh2OR0EL2cnJCiEecBXUVfEc687jZGTZWipO6rIfEyzfdloHCa34-lewTow6D33riK_W7ptlr2FUbUaTv-FlO8WBAHEKJp8IRWb6yg3_ib7zTWtulF_I2tFYbXVQfwXlJJPw7hhWx3rE0lA8c_Qqt9B20z5r_Ga7UM5cBEP4rp00G3h4pckydPjFTAJqffPGrwMaj6CaiLLLoMoNM9BQb9HBojQZgxD3V7v6oJm3VRalmV_3bpNQ9VoTgxBlzFiT2tmlHzgoyJ49MBvPW-fWzfjA3kweGT4QVKOtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
#فووری
؛ ترامپ: با نتانیاهو صحبت کردم و دو طرف قرار شد به حملات خاتمه دهند و آتش‌بس را اجرا کنند!
@News_Hut</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/news_hut/65220" target="_blank">📅 21:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65217">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kWAZMSkaSYhZRHzrxgwhWpOe8TvqGHJ9Yeio_Vfg8Dc-fvqxEYChNX_It6i90LgLLqHVnc7gfUnOWjM31W5wMhwkDAnpKXxeaIKmLZ0FvSEduS8D34vVz3SCfZTBp9TtsbjKL0Gxoe3WNhhIBd8KEKuwoo4cWEYsiulNfqV7ZEvec-zitrQg-tWSYLauYne0ke6IyRoO3V4e_5Qj92QgpwBInRPfTxUlJu5WwzOXdb09qy4a_QQfCCFHyTnrP11MH4ZswRN7NletyETmSnjDuFHTc5rElkOxDZUdlOjvVorGa9tRnDeSramSWLu0_Bc5kt24C4qrQruZBrdTXgFtKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ایزدخواه، نماینده‌ی مجلس: آخرش که قرار است فلسطین اشغالی را بصورت زمینی آزاد کنیم؛ چرا همین الان تمرین آن را از امارات شروع نکنیم‌؟!
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/65217" target="_blank">📅 21:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65214">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
📰
مصاحبه NBCNEWS در گفتگو با ترامپ درباره تعلیق مذاکرات:  فکر می‌کنم ما زیاد صحبت کرده‌ایم، سکوت کردن خیلی خوب خواهد بود. سکوت به این معنا نیست که ما شروع به بمباران کنیم، ما محاصره را ادامه می‌دهیم. محاصره یک تکه فولاد است. فکر می‌کنم تا هر زمانی که آن‌ها…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/65214" target="_blank">📅 20:57 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65213">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇺🇸
سنتکام: دیشب ساعت ۱۱ شب به وقت شرقی(۶ صبح به‌وقت ایران)، نیروهای آمریکایی با موفقیت دو موشک بالستیک ایرانی را که به نیروهای آمریکایی مستقر در کویت هدف گرفته شده بودند، رهگیری کردند. این موشک‌ها بلافاصله منهدم شدند و هیچ یک از پرسنل آمریکایی آسیبی ندیدند.…</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/65213" target="_blank">📅 18:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65212">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pIAmGDWPkQtyuZY2YSPpHOI9u7f5UR58d27iSteg9U0Dt3_AjrtyJ3kQrzICQ3wj6ELuTtEKLawAVTXL1LEH_OA75TeLrLbaq9EX7LjoDRyw_3yaRGD2hUKKGZXfRx3enqQpQ_6cojWpvqOelx6JEGkMb6nGnIoDyCrM5G5W9heP0Wbec9noHsjvqi-k6MegOYJUH4lzpfJfsFiVh7tnuBka4n_wm6qSbLJH_Fsn0wzBAnn3VQhB2V6RB7epTmg0KY7eLDW3vbYGdONrRk3wY0AYKfeHBQxh19B3hXZqjrnC4hUGYMlRWN0ngA9lY_bI1DOsiBv0ORxZRs0Gw1adpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سنتکام: دیشب ساعت ۱۱ شب به وقت شرقی(۶ صبح به‌وقت ایران)، نیروهای آمریکایی با موفقیت دو موشک بالستیک ایرانی را که به نیروهای آمریکایی مستقر در کویت هدف گرفته شده بودند، رهگیری کردند. این موشک‌ها بلافاصله منهدم شدند و هیچ یک از پرسنل آمریکایی آسیبی ندیدند.
فرماندهی مرکزی آمریکا هوشیار باقی می‌ماند و به حمایت از آتش‌بس جاری ادامه خواهد داد و در عین حال از نیروهای خود در برابر تجاوزات ایران محافظت خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/65212" target="_blank">📅 18:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65211">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rTG0oOYTGsfqpMsKpLBxqt5sjWMc_U-j6eQ8v3RWgO9EKFR0lhBP8ArDV0abAb4yNxAlZvAodsBl2rSR9u9Za3V7rww0-WW_dS-LSTSOzC77HVd4Y_xLpJvA1qJTPYvJiKtexrBZqM9nTS-nLVUgjgb-AgqTe2tpXDcBn-WXNzJIWy9VZ2eVCLBsU5xRevn_QRabNEY8dgMQ31F4E1jXfvl2LstRiq41dMVN0SmOZTdQc69pw1OIHdSWr68AwGJselHr_7v9g1KclcZwHIpWaoW-StQcR2klZX0w__mwd28USd7gr7J3GyhReFt0npJnIVrOloGEB0eTkS9ciNZagg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیرنویس فوری شبکه‌ی خبر به نقل از سخنگو نیروهای مسلح: تداوم حملات اسرائیل به لبنان قابل تحمل نخواهد بود
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/65211" target="_blank">📅 17:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65210">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EtUDNsO6RhLwVp8vyqI4CV9KWkkX5hW24YvwkMTI7gBVFhK3wjD9DzPvCRvXb7R0voh4nQGt7XfLmvBHiFloHY3H7PvA7ZCpqjxUmod_nXbQXaQUc3L7zJWdynUyRFCpyN34z0DrPjaKWpldncbWdXvULot1Bt6rHZj2PAojSqke4o0-todVVUHDyK90R6-MpGRmysvcI6mYUW_3k36t31KeBO2osTO6UJGVHqTnnE9H1zT1N5N_xhpwAJjCSjkrCphPS7XkzbVTGQw3_3_4eT84HObNBog_VpsAUbz4RgecA92IhXt7fkLNOYoOCt20ddxIsWeltPw3GwQCavju8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تهدید امریکا توسط باقر قالیباف: محاصره دریایی و تشدید جنایات جنگی در لبنان، گواه عدم پایبندی واشنگتن به آتش بس است و هر گزینه ای بهایی دارد که پرداخت خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/65210" target="_blank">📅 16:17 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65209">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qdn2vZ1o6NblTSD_sGcKrTLGgyFYWedC4D3drSO-ISzOzytWROBp11yoEK2HN_J8j-ITPPFrGjoV4odxuZjTZGAFB2eD2L0z6Vs7izkkuAZux96d1cyZ0y3cHJkhITSD_cPdUUht-COlH0gW1TgPbo6Y4spJQnhZbyjcD7LkPRs7MGElkv8VfhcR7bvuRWWxWhslH1ifHrjgzizEv3ckts_9jy-0ZMzR7T4PK9PPv8QRdrKR3fyx51W2c-tiYpjehxrsBeXD2AuG1OhUTfjEtC3_GXHeVlSs4j8RxJHIdWPRUuwxKQFx5uzk0TIYbirNywSesZLZbR-qGjAVB2j-aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضائیه جمهوری اسلامی، صبح امروز و همزمان با اذان صبح، مهرداد محمدی‌نیا و اشکان مالکی از معترضان دستگیر شده دی‌ماه رو اعدام کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/65209" target="_blank">📅 14:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65208">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/65208" target="_blank">📅 14:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65207">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b_t6OW_-nKVD-7VMBxRigvattLO7EBGSsqJOz-_qkEwe9UdkbJgOe5h90ymYX_vnkzoptD-c9PWHEd5vBZhNNx1JMsiN-4Wc7wwRG4Ytb71SF92sy7UkitJd6R-yV6i7gYPeATXNlr4G-gcNI_s8dSoFtvlkvphADGMv0SvE5lWZpluQarMAymx9Me6aZCdopxphe0OTxYFNxUXk1QCaDxakhJu15Ry036cQyMaeMuxVrdryNqNxVzJQ19whBkraaKY-2OnD0Z1i6mlo7YUymHVRhVBPqxLLqOm2j09V_W3hJZdSjaog2_7xqktEfQVUPiaLyYPKLlCpse6UKAYKaQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/65207" target="_blank">📅 14:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65206">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DSgJJmvP345ZXLQW76-zTif8i616wPwkLuP6k9tnjov9khCsu-4hc4o9caHBQMkV3d3p1lrXBIy70a-COKWV0eds-0MkYGIC7z2F1wdzmf_yn_EZWcKq4KHyHuh5VPaOmW17nb34eNmoHvFjBMx6mvyC_wHKINjN_kYTiVx93T-Z-Pc8JdUhjvgnuCV1MMxDIDZp_IU6y9BdAkDw1YSvysI566cTu5sKDHRjfGs02qEnrNq1yfK4BZac2YRqVGlR0g0btbreB3FicTmoZDhX_ODRBF4AgfVK1zzfmLxsa_x7wBgEn-g38ejcrAlJXirEBFo34QZOV6i_nI-j53M1TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ: ایران واقعاً می‌خواهد به یک توافق برسد، و این توافق برای ایالات متحده آمریکا و کسانی که با ما هستند، توافق خوبی خواهد بود.
اما آیا دموکرات‌ها و جمهوری‌خواهانِ به‌ظاهر میهن‌پرست نمی‌فهمند که وقتی افراد سیاسیِ فرصت‌طلب، به شکلی بی‌سابقه و بارها و بارها به‌طور منفی اظهار نظر می‌کنند و می‌گویند که باید سریع‌تر عمل کنم، یا آهسته‌تر عمل کنم، یا وارد جنگ شوم، یا وارد جنگ نشوم، یا هر چیز دیگری، انجام درست وظیفه‌ام و مذاکره کردن برای من بسیار دشوارتر می‌شود؟
فقط آرام بنشینید و آسوده باشید؛ در نهایت همه‌چیز به‌خوبی پیش خواهد رفت، همیشه همین‌طور می‌شود!
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/65206" target="_blank">📅 14:31 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65205">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔴
شاید باورتون نشه ولی ترامپ و کابینه‌اش همشون خردادین!!
• دونالد ترامپ: ۲۴ خرداد
• مارکو روبیو: ۷ خرداد
• پیت هگست: ۱۶ خرداد
زندگی ۹۰ میلیون ایرانی تو دست خردادیای مودیه.
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/65205" target="_blank">📅 13:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65204">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🇺🇸
گزارش سنتکام از درگیری‌های دیشب بین‌ امریکا و سپاه در قشم:  در این آخر هفته حملات دفاعی به سایت‌های رادار و فرماندهی و کنترل پهپادهای ایرانی در گوروک، ایران و جزیره قشم انجام داد. این حملات سنجیده و عمدی در روزهای شنبه و یکشنبه در پاسخ به اقدامات تهاجمی…</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/news_hut/65204" target="_blank">📅 11:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65203">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e4c45b1ee.mp4?token=rfwH6d0fEANvZak-Gw1voXQE8k9v7PAoMQH9IjqmWW9yzqWGXbRTOHPzhDJv87M1VuCnQDnsunrJaesQNqtYeB2O_Is5Ezngmj7dVA216Fdtk9cZNGGOTLu_yzYN8Zn5riTwukYswmLbbeS_JCRvHIAUGs4jfjlwlq2RfT9eaiqKCwRrz5jC-ps6J2ZCutyTrHLyietQ86XnrM7xBpqXTXEDYVfSOvWRwloCwGy8gy9MVNmjsumIpnBuvDx7JxSdXRZ1VHiRO_TZf1qD1GYhoeR-varcbInWBsQ96mZ7NWB9Kv0KVfuxtTz5MzyOZZxqlOP9dFSuM_mJ_3bUgzPISw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e4c45b1ee.mp4?token=rfwH6d0fEANvZak-Gw1voXQE8k9v7PAoMQH9IjqmWW9yzqWGXbRTOHPzhDJv87M1VuCnQDnsunrJaesQNqtYeB2O_Is5Ezngmj7dVA216Fdtk9cZNGGOTLu_yzYN8Zn5riTwukYswmLbbeS_JCRvHIAUGs4jfjlwlq2RfT9eaiqKCwRrz5jC-ps6J2ZCutyTrHLyietQ86XnrM7xBpqXTXEDYVfSOvWRwloCwGy8gy9MVNmjsumIpnBuvDx7JxSdXRZ1VHiRO_TZf1qD1GYhoeR-varcbInWBsQ96mZ7NWB9Kv0KVfuxtTz5MzyOZZxqlOP9dFSuM_mJ_3bUgzPISw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جواد ظریف در پاسخ به سؤال میگن شما پشت پرده مذاکرات هستید، گفت:
من اصلا هیچکارم
@News_Hut</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/news_hut/65203" target="_blank">📅 10:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65199">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">بر اساس تحلیل تصاویر ماهواره‌ای CNN، ایران ۵۰ ورودی از ۶۹ تونل موشکی زیرزمینی هدف‌گرفته‌شده توسط آمریکا و اسرائیل را دوباره بازگشایی کرده است؛ در ۱۸ سایت زیرزمینی، عملیات خاک‌برداری و پاکسازی برای بازگرداندن دسترسی دیده شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/news_hut/65199" target="_blank">📅 23:53 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65197">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/poRuDjKPEYDTZNv7XCouqGJBfmEp1JegNWxa4GvaFydiCUwxL5ge99d9YbzdjjRW2y3ERfzVLv_CXtWlu2iZg2rCeORD5bppfbH2PO0r1mAcUQR9g1uNcZQojBc9B-3BKBVggDoDGPRxtqzRfBpRyuF_z4A9wFEakFSkZO1_hhiNgoHXzyB6GE0x3BZCAQzV3WXghAcUKmPE9kNoClx5atRELJxMhytYIVwk7wFA-lS0AB8PzR2NFqUQRZP6hYw58XlDQxHn5tcykHCP7ydLGbymjKe_QupXgN0QyenjOFViG6Suwlph2frGvKt-IV2zcFKY7jCqVo85T52yjgN0hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طباطبایی، معاون پزشکیان: رئیس‌جمهور ‎از خدمت به مردم عقب نخواهد نشست
@News_Hut</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/news_hut/65197" target="_blank">📅 23:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65195">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">طبق گزارش The Jerusalem Post، ایران ادعا می‌کند پس از بیرون کشیدن/مرمت تونل‌هایی که در جریان حملات آسیب دیده بودند، آمادگی شلیک موشک‌ها در سطح منطقه را دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/65195" target="_blank">📅 22:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65191">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
📰
#مهم؛ ایران اینترنشنال: پزشکیان از سمت ریاست جمهوری استعفا داد  @News_Hut</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/news_hut/65191" target="_blank">📅 21:18 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65190">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GMzwaA8MxW91o2EdDFHgKMCn3C3TpJ1v2EbQUVwzFLNH6wEGKE84LakQUi9Nu_t7ZF2V6RQEGAXLOfYDk7jpGsLMIDv3WZ1pR2yQGZzR8p_Z2CE-yyjm7lv1WA3SnNgZLFk051zG5XGrnxkQVmhmJnt1F3uh-ciiAO79b05RQ_gNJu5zoM6gBdjfDhcuTUaq4-WirINisTJhttqKXwxnkV8ovuB32A_p71udnp491OfLJ7hJFvqiCed3m4eRf1ECUZPaOyyq2_uFWAc42cYujVhECPsZPXscr4mdQtxNpOauQe9658KsUAwmCO3dodVkuGBq3ZC6uJVH-dbZez_mHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
#مهم
؛ ایران اینترنشنال: پزشکیان از سمت ریاست جمهوری استعفا داد
@News_Hut</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/news_hut/65190" target="_blank">📅 21:16 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65186">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PCEeNTLjPGVj7x_wVCoL22lCeltRgZNMN_9MPqCj2jJDZGQLl61YUuJpOGxueSdH6u1C6ymii7MYnIAL9h92uGu063mg721_pKeJLeMLmMGBDEhqA4r3RziV5HVezSIDrNnsHJJ-tYlMEWlt9NaVbIV2i9re0UzWYXDH1ZxRsyEJiFUrXMaQtZW1FGg0el4wUsM23Ed5e6qE2DBOhUgP7etPpFcQZYbITGVtnlsdjGSk56i3z_ozTlud-dUjf8x7aq9pRGsb2qfr_oJG7rMeSnp_ZWYzjUvY_9HUNmdcmrW1yL03P3P-u6dm6hnTELgBurzQi3Gna30hh6oCZJmxpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lGkew1AvGo_0CuMgOL2kLiCzV5GHbmoA5W5UIwXfTx7ajQMydNwJWmd4z8QQLbNQ_4EdFAmJxkyN2f72FyGRDzOMH-8zELOYj_w417ZmprwhYZirTmxfIuy5-_IaXzV9OFINBjptt89NQTlDZLICcXVJMv3hGbrQ4wKDChZ0qbJLzlmnZtiE-VV21ulRYsfhug_0hk9DQqlJuFGKUj7gW4v3Kt7HpC7RjqXQFU0_zDq0vfmK1q8h9XyVZaxK88lrwYcOoSpPXOIu6Bkcw76Pjk6mlkb1pZ8pOoL4NGfN8rFTBtBQCjaC_ghtwxf9IClxewfoPXYJM2eewznabExuGg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a589784b7.mp4?token=pDLChejMgqzcSQXEURBCYs0x5CyOJEbfn2I0E3lhRvxEJx7OrUFf9PvJgMM4JJB4D2YNZhdrguR8TiOA8INr2szZwplpNXKdUxvf99SQMBe-vvQ4YS5ZBy1B0JOg2EXbZ0c1Cl8QsmQLm4OOaPQsAgEh4hu569x5IEEUFz9NaYW1Z0zDsrEb9oiMzWm78VZ76EAcL8wA7FMXfY2xDCv-V1yxtl889VB5WP9fpiTzZwaQ-W2k_8YojaYX9sFH9mtEU22BEiVFFUuDo2EKh6Lr1aKIbbWOURzCg2ApHBK81OjmftVU8RZLhhzhbxFaApYipG5AV_af9YNFgocezmMs2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a589784b7.mp4?token=pDLChejMgqzcSQXEURBCYs0x5CyOJEbfn2I0E3lhRvxEJx7OrUFf9PvJgMM4JJB4D2YNZhdrguR8TiOA8INr2szZwplpNXKdUxvf99SQMBe-vvQ4YS5ZBy1B0JOg2EXbZ0c1Cl8QsmQLm4OOaPQsAgEh4hu569x5IEEUFz9NaYW1Z0zDsrEb9oiMzWm78VZ76EAcL8wA7FMXfY2xDCv-V1yxtl889VB5WP9fpiTzZwaQ-W2k_8YojaYX9sFH9mtEU22BEiVFFUuDo2EKh6Lr1aKIbbWOURzCg2ApHBK81OjmftVU8RZLhhzhbxFaApYipG5AV_af9YNFgocezmMs2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
اسرائیل رسما داره حزب الله رو تو جنوب لبنان به شکل خایه‌فنگ‌طوری با خاک و خون یکی میکنه
@News_Hut</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/news_hut/65186" target="_blank">📅 18:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65185">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IurXzm8JFS2GpPgGuiMJH40pspPEyw4F7K9K2GlBHc2G2j69xXpBPlF02AFptjmj0Uv8MfMXxy_C6S0Ul6OVBkr6QphHEXhFR8LCfsmIFQ8mksm3e75s4fGnPKtMRA0GII7dh855KRjZzC8r7BidMyFAAAqCTjgRVPujRfPbevEVr92_OW9cefXssrecCMhwVzMLbn0n4-f6nNb7nXyAzi1pz-UVP5-6wXQ4v-FkWRZryyXfur1dVu9g4vyXUq7qtrI73LHCn8N1oFNOcyQvn2J1KLGMWgyGKnc4sJch417mFlUiBSnJvS_3FakU99qn7eGkF6Ms5JkSbyc0qer9ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست قیمت جدید خودرو های مدیران خودرو با ۸۵ تا ۱۰۰ درصد افزایش قیمت
@News_Hut</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/news_hut/65185" target="_blank">📅 15:00 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65184">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
گزارش شنیده شدن صدای توافق‌های عمل نکرده در جزیره قشم
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/65184" target="_blank">📅 14:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65183">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec47112ddd.mp4?token=PdBSrWL986AcwGq4DvyNJvfgVStvJcfj_0nJ4CuK_lx8slCu1V3oCmlwln9Ieho9AOUViLVxDtn3_gmg6e_qLP-Bq7GfDBZ-R5SUW-KQ8-HjO6pPsDFZfm4XHZIxP_rKrCR-4DmcGQmihzAxJAUZriwIT4t0KPzDd0G51buWliyP7Xigu2f0K2UcMTTFYGqVYqKRqbkNaFivViSiiWpCUeWJ6UOR1Qf4s10h6B9EisfHpQQ7PDrqT8iTnQO0iQafP_JN11NRJ1YtRsVirDbvTeqwOtYVJcJOY_zNXr4-78SuQYglzdNYqEaJv0G6RZFldM4ZF7iTlizJLE3zt3ZCww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec47112ddd.mp4?token=PdBSrWL986AcwGq4DvyNJvfgVStvJcfj_0nJ4CuK_lx8slCu1V3oCmlwln9Ieho9AOUViLVxDtn3_gmg6e_qLP-Bq7GfDBZ-R5SUW-KQ8-HjO6pPsDFZfm4XHZIxP_rKrCR-4DmcGQmihzAxJAUZriwIT4t0KPzDd0G51buWliyP7Xigu2f0K2UcMTTFYGqVYqKRqbkNaFivViSiiWpCUeWJ6UOR1Qf4s10h6B9EisfHpQQ7PDrqT8iTnQO0iQafP_JN11NRJ1YtRsVirDbvTeqwOtYVJcJOY_zNXr4-78SuQYglzdNYqEaJv0G6RZFldM4ZF7iTlizJLE3zt3ZCww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ: بزرگ‌ترین سرمایه ایران، «رسانه‌های فیک‌نیوز» هستن که مدام موفقیت‌های آمریکا رو کوچک جلوه میدن
شما یه پیروزی بزرگ توی یه نبرد به دست میارید
ولی اونا میگن شکست خوردید! این واقعاً چیز بدیه برای کشور ما
@News_Hut</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/news_hut/65183" target="_blank">📅 14:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65182">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EZIspljfrNGsS6AoCxZDr27K5xMuPNaOI_6077qcNLQ6AvA0c1iVbNFjlNi1yZlwNwwhZchJgAOIVAkj7-aILwlLGspDlBsuj2MCNi7bDaqyomODMrD7ESRpBlbOfytWAYeXNcSARgBaNorzG0qYneyCuY3nn7qdy2O0sBSt1FuUx-fYe8sqmykpOrm3_CfkB_Zkkn7uDJWAsJrVOH5FUEg-6_QydhQs_pgig46DI1RjXFISPKlWiye3vTJVOh2FOTnHlXh3PPFuNHodDrjr2T7BmK78zsVj0G6WaH78cY-A15AK_iJk4awxe5sCoLTxNbFMp62VkBbm_3ZCmtoBTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تردد خودروهای پلاک مناطق آزاد  تا اطلاع ثانوی تو سراسر کشور مجاز شد
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/65182" target="_blank">📅 12:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65179">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/473b1fd669.mp4?token=SI3bJ11ZwruwPQnuzvuQPVV7DJE5zagKU4aNCiSoF04aRRgnOrXwWZnDhllVX2KbCmb9VZZxNIl_kVAMYzmkFhSpnEDqaUPTSYVlAfxCU8PMjh7YaUA05eLu1WJJGd0JHtIE01fb26b3WdG7X4g_OO4nAkIrfrFLh3uxN5RQ8KGdZuRmzDOoCtzIh9UkPpLO5ox9PE8U-CXf58WRBZdIC9mzuiVPAbAqRduIo19iOYUZLPG6DpmJ96sBaVHmP01R_Rl1CxE8ExrKA9CXGeWMpqvWkFz_4wo2EMI96RHeobBTKla4e-ZjDqeYQ0S202X8iwP9MOGM3JHT5NPTOA4ivQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/473b1fd669.mp4?token=SI3bJ11ZwruwPQnuzvuQPVV7DJE5zagKU4aNCiSoF04aRRgnOrXwWZnDhllVX2KbCmb9VZZxNIl_kVAMYzmkFhSpnEDqaUPTSYVlAfxCU8PMjh7YaUA05eLu1WJJGd0JHtIE01fb26b3WdG7X4g_OO4nAkIrfrFLh3uxN5RQ8KGdZuRmzDOoCtzIh9UkPpLO5ox9PE8U-CXf58WRBZdIC9mzuiVPAbAqRduIo19iOYUZLPG6DpmJ96sBaVHmP01R_Rl1CxE8ExrKA9CXGeWMpqvWkFz_4wo2EMI96RHeobBTKla4e-ZjDqeYQ0S202X8iwP9MOGM3JHT5NPTOA4ivQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ: اگر عجله کنید، توافق خوبی نخواهید بست. اما به آرامی و پیوسته، فکر می‌کنم داریم به آنچه می‌خواهیم می‌رسیم — و اگر به آنچه می‌خواهیم نرسیم، به روش دیگری به آن پایان خواهیم داد
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/65179" target="_blank">📅 11:12 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65178">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4173e3828.mp4?token=ChWyFR2t1GtzoxNcnqD1ESAcaLPQGRi2CRKsRtQfUG6KFZ1WtnZOvkil5TdaZF1ik7skz2RbYYIA38uaLkrmMDp4hXvLdcycJPuRVRT1GjULs-ToAARa8VwYt1y0F2fj1X-Aimi7PwT-mgmzjObcuceGtYZGLTtl_u8GLQVRgJH1u5nAFBBwk3QcDaFVJs9_Kv1YVvDw3cTcUKwSRv2jruva-4ZOeja8sh5otzMQvykphMuPzTddW10G283e2SqPkJP4KA1XSImdHjMS-YoDv1IXwU7QkDTnDe-Ej9lhiUwB6cpjfoRyN8fGN1L9sZLLLL6sE78rM96Qgv7Zye3Cqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4173e3828.mp4?token=ChWyFR2t1GtzoxNcnqD1ESAcaLPQGRi2CRKsRtQfUG6KFZ1WtnZOvkil5TdaZF1ik7skz2RbYYIA38uaLkrmMDp4hXvLdcycJPuRVRT1GjULs-ToAARa8VwYt1y0F2fj1X-Aimi7PwT-mgmzjObcuceGtYZGLTtl_u8GLQVRgJH1u5nAFBBwk3QcDaFVJs9_Kv1YVvDw3cTcUKwSRv2jruva-4ZOeja8sh5otzMQvykphMuPzTddW10G283e2SqPkJP4KA1XSImdHjMS-YoDv1IXwU7QkDTnDe-Ej9lhiUwB6cpjfoRyN8fGN1L9sZLLLL6sE78rM96Qgv7Zye3Cqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سردار حسین علایی: ۳ روز قبل‌ از جنگ رمضان‌ به آقای شمخانی گفتم آمریکا و اسرائیل با ترور رهبری جنگ را آغاز می‌کنند، آقای شمخانی گفت «نمی‌توانند، پيدايش نخواهند کرد.»
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/65178" target="_blank">📅 09:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65177">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff9b4e22f8.mp4?token=qbPNwCsZ0iq-dvzPRkhUfPGUUNLJ1yDaxjcs82-EYKSCwxOuTW6qG0xuhtv7LjUmYSDMwjzgW4C0SSRDjZk0yHykoYZawl8j09KTASuzXEG-Mpuf3-tCEm4nWapVjjy9yWAledJ91CX-bUEYN9AGKVd9yLEq-o4eKukwtKQXczW-Lqck47MBz1l91lONuc4B-J2u6NwsQhWCsmpMHxe4Izh3UbTXBQc-joRzBNWoPES0YMwNOs02118NhdeVvuNOBRXqIWEtctsQwYHkm2kxvUTF-g7Mqt2RWNCOvjKp3dd-kqXGCYOT7VDqZZgKfgCHmVYfDWddw7fLSnHMllkTkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff9b4e22f8.mp4?token=qbPNwCsZ0iq-dvzPRkhUfPGUUNLJ1yDaxjcs82-EYKSCwxOuTW6qG0xuhtv7LjUmYSDMwjzgW4C0SSRDjZk0yHykoYZawl8j09KTASuzXEG-Mpuf3-tCEm4nWapVjjy9yWAledJ91CX-bUEYN9AGKVd9yLEq-o4eKukwtKQXczW-Lqck47MBz1l91lONuc4B-J2u6NwsQhWCsmpMHxe4Izh3UbTXBQc-joRzBNWoPES0YMwNOs02118NhdeVvuNOBRXqIWEtctsQwYHkm2kxvUTF-g7Mqt2RWNCOvjKp3dd-kqXGCYOT7VDqZZgKfgCHmVYfDWddw7fLSnHMllkTkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو تجمعات شبانه حکومتی‌ها، دیشب سپاه یه قایق تندرو آورد وسط میدون و از نسل جدید قایق تندرو که ساختن رونمایی کرد
@News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/65177" target="_blank">📅 08:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65173">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XlLTnmwbAqgs_WAVeGdZSVcXQjj7plses4YczlmGUiO3YsMEw8UqpqAIl1LIvUF6_bWQ8t5oUODBMmrzgASYfAbHsA6cswV0KB1bLJu5qPzerymXcOdn0FcZiPOq2GfILGJ0fCUZReV1PKAMCwus0rD9qPzJkvmsxR9_qF6HmdflOgWaN2ZSFKC2baSmCzwre3L3xY69vSU8lnAOOuGOI9apUb_3fbubpmBCsR4FJYdPirVkcqX-BcQKzKl5zyebKFH0C-DHqp8IAExy3j3sp4igLRLFbBw2KHNoRYUWp1IR_I-b33BM9jLh2gEBuSuQepNh0g4H4lTgQMMsyb6zlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XpLPrzZNzNDJ--zRoYJjgiN1KkIvrNSGGFFbor1Z9ZxQsaZ688HR5vQtcEv2_4WZOOmnvOweKhgf7EeT3zI7HUnY_Yj-yWmPksoBoBpAVpLmmEf4fjK6VRd3t2Pq1KwB57_UDojBTZmKwQtJTIXSoeHhC3HttD0_UeYxyxTFf9iIBqdQ_BuVYRUXPHBEFGtPxgInNgpd9Acq7qCXHPfsMl5ciZrWqXGZRQYH-CPD8uiiq7SX0AQwTFgp26t7Wd16f8uDj3niEXYPtMo-h1KoK866oU5JsH9ahMSQQPtKcCOpXeR-A3zbH9Rew9fJiKI65IvQ7bpNsuyMIIzHEUfx2w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پست های رندوم ترامپ دلقک تو تروث سوشال!!
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/65173" target="_blank">📅 00:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65172">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff2f73449d.mp4?token=o54fzj6aTJRjTB5Uh0VJOkww13hVj0oaC_bRPkSBRzEx9o9MLFSIV-g1BVy9XgwfD-RHXRNNLyCC-R4eXBKoljQZe8RiAPVdDqhvGCmjuphIL9lyrUicGQjZv9qPe70lhnRTWU1WZYWFfvRWViBscrJJrNxJnj7w9ZrWKj5PsjcCN85qn_l-fP8QRelCRJjEvEE5cnCQIG7uiHdohYUDVdwXF9uEL-v7H6fUvamliwZswYCQdveSz-pNsEw97epmMDAKEFpnHaQ3U17881Oq4AcQY38XFXlww01pAAseZalraaT_BuzofjlAgSSr_WPXoeWrxpdnvXocKJH0bUmsTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff2f73449d.mp4?token=o54fzj6aTJRjTB5Uh0VJOkww13hVj0oaC_bRPkSBRzEx9o9MLFSIV-g1BVy9XgwfD-RHXRNNLyCC-R4eXBKoljQZe8RiAPVdDqhvGCmjuphIL9lyrUicGQjZv9qPe70lhnRTWU1WZYWFfvRWViBscrJJrNxJnj7w9ZrWKj5PsjcCN85qn_l-fP8QRelCRJjEvEE5cnCQIG7uiHdohYUDVdwXF9uEL-v7H6fUvamliwZswYCQdveSz-pNsEw97epmMDAKEFpnHaQ3U17881Oq4AcQY38XFXlww01pAAseZalraaT_BuzofjlAgSSr_WPXoeWrxpdnvXocKJH0bUmsTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه عده تو عید قربان خاتمی، روحانی و ظریف رو بنر کنار ترامپ و نتانیاهو چاپ کردن دارن بهشون بعنوان شیطان سنگ میزنن:)))
خوب این ۳ نفر همینجا تو کشورن برین خودشون بزنین
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/65172" target="_blank">📅 23:32 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65170">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dd6247ddb.mp4?token=ezzpZrfjuMcQcuwZ8qEHt_dR2UPHBYZZrgZRYBVQoLH5UU4M0xnO7aKanOAytMwkveQsfAzZCdMFSUBYzdubBp8p2TEZQxGP-oXNUnaG01KPKTElz_-aW_fjLYCixb6xIOjWz4r4h7a7VVicdq6OG3FeiXvPItzj25xaDTggG7YxYNVRouQoK1rg12KVO0nEKLjwBbMAKW6ioJYeY-gOBWCG8QPRSf87zE58TEBhMRr2g88QAX25LzgbCnpX7RC1wyG9sErL1eC7qHdl5sUvZmvBzMVBYcxuFQ7XzutNLsYDxtiTYvJKGT4dy4OEttiZwB8PO90sqbkigKxuhDu54Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dd6247ddb.mp4?token=ezzpZrfjuMcQcuwZ8qEHt_dR2UPHBYZZrgZRYBVQoLH5UU4M0xnO7aKanOAytMwkveQsfAzZCdMFSUBYzdubBp8p2TEZQxGP-oXNUnaG01KPKTElz_-aW_fjLYCixb6xIOjWz4r4h7a7VVicdq6OG3FeiXvPItzj25xaDTggG7YxYNVRouQoK1rg12KVO0nEKLjwBbMAKW6ioJYeY-gOBWCG8QPRSf87zE58TEBhMRr2g88QAX25LzgbCnpX7RC1wyG9sErL1eC7qHdl5sUvZmvBzMVBYcxuFQ7XzutNLsYDxtiTYvJKGT4dy4OEttiZwB8PO90sqbkigKxuhDu54Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظه‌ای که معاون رئیس جمهور آرژانتین نزدیک بود ترور شود، اما اسلحه در چند سانتی متر جلوی صورتش گیر کرد و زنده ماند...
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/65170" target="_blank">📅 23:25 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65169">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">نماینده زاهدان: برخی مناطق شهر ۲۴ تا ۴۸ ساعت با قطعی آب روبه‌رو هستند
🔻
بحران کم‌آبی در سیستان‌ و بلوچستان وارد مرحله نگران‌کننده‌ای شده و به گفته نماینده زاهدان در مجلس، برخی مناطق این شهر بین ۲۴ تا ۴۸ ساعت با قطعی آب روبه‌رو هستند و زاهدان هزار لیتر در ثانیه کمبود آب دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/65169" target="_blank">📅 22:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65166">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">کانال ۱۲ اسرائل: نتانیاهو به زودی جلسه‌ای برای ارزیابی اوضاع در شمال با حضور وزیر دفاع، رئیس ستاد کل و روسای سرویس‌های امنیتی برگزار خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/65166" target="_blank">📅 22:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65165">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">شاهزاده رضا پهلوی در اودسا: دنیای آزاد هنوز ماهیت جمهوری اسلامی را درک نکرده است
🔻
شاهزاده رضا پهلوی روز شنبه ۳۰ می در نشست «امنیت دریای سیاه» در اودسا، در جنوب اوکراین، با انتقاد از جمهوری اسلامی و سیاست‌های غرب در قبال تهران، گفت که «دنیای آزاد هنوز متوجه ماهیت واقعی جمهوری اسلامی نشده است.»
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/65165" target="_blank">📅 22:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65163">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PZqY1_DCYSua3ejXZtBqjBe8wEijCFqYznr8f5E0cOKPNRS02QwMbT7fQOLJBDGf6G8GM3wEHdrtiZrK_tJb8Q_59VoOPkpJoHZb3THVrQgLyb-cRJrrYFah6jO0C6kKbrXdH8poMpDhUdP-ZRlu31td5y4Fh7Jpen6tVn1DcB0fDiTgA2EBtrQcK9RMI-PJGKiQdkropZo7Dsf4kUguCVufEZ_6pHDLLPtC1sTTpBcmt2B68jfoacl2Z5fyagVDlcWKBNsnBYLP8QIK_J5KmsTd_3QTAxcfBd4k1mtlCsUxeo8ysNDcPV82ttDDIFzonhcUNXn9Pdu7rhIvH_-xMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوشته‌ای که تو تجمعات شبانه دیده شده؛
والله هزینه مذاکره بیشتر از مبارزه است
@News_Hut</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/65163" target="_blank">📅 18:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65162">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
پیت هگست: وزیر جنگ امریکا: محاصره دریایی همچنان پابرجاست و به‌صورت دقیق انجام خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/65162" target="_blank">📅 18:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65161">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tahwo0wJ1wE3pdw6h6HyZaepSwi8dhxx9VcC0O_u505wqJlX4mhdRdmqJjEB1v68ombvfsdoaiSrcbWWyQjOiaME913vufNKyNX6LVBaGwVGGDqNOfYSiMWJD3R1ne4fsogFhGabf7R2_IkgdygGwMntRXNekCZ6Vyzy8XCI9tIhm6CAT8WjziUCL_gDm5-J-3kJcx5BmewYNYGWonpJigsrM4K73xiG5K0sKjiG4BDSmK2Idu0QumfO5sSeCACXS0yweCP8NUIft-1PcUaR1_zzdgoVWrw_2JFWhcUl86robtOqYSEYQp4pwUu_q9q_48vvhckHCyW5Dd3FTm1Qgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی: من فهمیدم ترامپ برای بار سوم در حال خیانت به دیپلماسیه.
@News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/65161" target="_blank">📅 13:49 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65158">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lkxOwSE_Ke6F3RoRkdDBxXI3126jUVh_Zbo7JIbi-b5ZVDSnIwNMF-pjHDSxyr0lX8jT57deeI42YZW0HtjOkPOqCT17sKwcqFm8V_SW9ob359p1czymDnNKiBruf_xe0lQiZCVCaZKYRuvKD3Vsqi7vxFahrAt9wVvO4QqJRaoebttL6I_2wEPxq6UXEzZgj8lMFLjOzgZ2qMIENi445GsrFVucvtQYuL6mcy1XKkPjCR8dA9SIsJaw7sO_Y2S6QAOkDfrqPUFuF8IrI2I-4RpA1x3bItqhZ5-dJVIQI4pHAXkSMP-zjHCODIX3RnEBpEnpo9XWNu8pcJbK2hV_QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کاخ سفید آخرین معاینه پزشکی ترامپ رو منتشر کرد؛ ترامپ ۷۹ ساله در «سلامت عالی» با عملکرد طبیعی ریه و سیستم عصبی قرار داره، و قلب‌ش۱۴ سال از سن‌ش جوون تره
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/65158" target="_blank">📅 13:17 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65157">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
سازمان سنجش: کنکور ۲۹ و ۳۰ مرداد ماه برگزار میشه
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/65157" target="_blank">📅 11:02 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65155">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S5sxDgC2WqZbr86hObLaCpuhzTipZVOChxKMn8tpqKYiSMVh1rr8CRleA2W-RKilcRVWpuluXnZJ1RdZR2aquU0nTu87xFjBCuA8qU9pXcCGj1Ud8XoplX1j_CVmajtrSOhhzdDcFRqEc8x5USW7IbXre18wmPf1EmSgAFvQGO3gqdSt_XUfQ0-TluZPJK73XPGV6ZZ7RDag7WXtTG9VcBEip-Rmvy1FV5oa5lLcVlzX8KOMtzfmiO3X13X3zysjC_oaINHCQqOM0gAIw9vMGoMqOM-gQYdLMRs4jmCZ8SLuN0oPHAMzAvL619cpQg-hCWQl7iJP-uu5l6J4ZrkS5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uACn30VNKJluEpFamKc1wdC99q7GI4LPujLOsQYGqOYr09ojffQyi_d6DomJRBkL4jz_mVeRBe0MxLiR_rrPyb4UrRbVz0rZAXEUKSfvl-fBn9MXNCHSNEqbGTQhMKyrRf_uHoJMvax6_dVixXocziWkSQ4s1m4XdkAJv_-0pnkl5YgvRvv2I9DO__FFJlStzYYQzIaXtXEei8y_HY30bi4aBeIhf1wqEQPOMgNWqCPqCqkSBFQmNwr0kcYTHD2psO0Icz6NSBtRgwVUwHNzR5a8ulXu5tf_sCfjlSclEFJkWH_j4PATigSEe8OQHGtz58IqsvtHfbHjg-T5X1Sf0w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ملت اینجوری دارن قربون صدقه‌ پزشکیان میرن چون حق مسلم مردم رو ازش گرفتن و نصف نیمه بهشون برگردوندن!!
@News_Hut</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/news_hut/65155" target="_blank">📅 10:52 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65154">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GDZFar9TByvtzVybbhvnCC0MGpxFED9OQwIDOVuTIupbrePr4_4KhrGe7YxmI-GZc2Irjg8bVTSPghRwRw7fiFCvOR0t9aIoAqMwGPzAUeQU_O33cJ_-dMjQNmB3L8F-_g2yEsYuWP-mpkylOAwleYfBWmCWO6EseLb4Hj8vIxAcSJb9ITL3OSRImVlbCP4dIXNgXNgvqSoaE8MPMeI6eXSlcRaqtB56nXwCtYeXJhHh8nXfQQLs1Q85i7ZKn318nQ8lfvDsiJ8_O7yi2J-jpuIWBdORpbakft7QpL88JmwJz-xqHm2FE40m2-9bJQz4zqW4iaTV3XlduUkQG9CEEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از عروسی‌ها و صیغه‌های نمادین تو تجماعت شبانه حکومتیا یه پسر ۱۷ ساله با یه دختر ۱۶ ساله تو تجمعات عروسی کردن
@News_Hut</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/news_hut/65154" target="_blank">📅 08:39 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65151">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a38baf3c3a.mp4?token=L5vdUJ43NjncnE_tt7MNfSodmICMusYqnr2UT3sUJuk--unEQ7oZ36Lc_pAqqDzmrY01b00bUq6BVcV1lVa2ShaFhwL1UKXx0d5AbhOncwAQy8hrPdvuysqF26kA8UKGITGAak2f53m8MNZvvSdQ3Ch8IcxIX6_gK1diOcPn55VvXmlGNYP_PsvJPAamfPNixGfKnU-A4Zv_Un2C3i4uiU9wlEcG4aHVEM_MpuvHjmkuwcpf0ZM-Bn9mk9KurdtJbzHFZ3kgj97SiCrPDQfHGBwT2COLZOqDCe5ciIIL1hLEfdB9STkHfoLAZP1DhJ7f_uhCZj8O14Fs_gBdW_DBDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a38baf3c3a.mp4?token=L5vdUJ43NjncnE_tt7MNfSodmICMusYqnr2UT3sUJuk--unEQ7oZ36Lc_pAqqDzmrY01b00bUq6BVcV1lVa2ShaFhwL1UKXx0d5AbhOncwAQy8hrPdvuysqF26kA8UKGITGAak2f53m8MNZvvSdQ3Ch8IcxIX6_gK1diOcPn55VvXmlGNYP_PsvJPAamfPNixGfKnU-A4Zv_Un2C3i4uiU9wlEcG4aHVEM_MpuvHjmkuwcpf0ZM-Bn9mk9KurdtJbzHFZ3kgj97SiCrPDQfHGBwT2COLZOqDCe5ciIIL1hLEfdB9STkHfoLAZP1DhJ7f_uhCZj8O14Fs_gBdW_DBDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pKe5DqavjXmuU5va1ZtdNF8NwAp71l13jsLF6JIOSlkAr_1oQ9jALCmqXIdamC02-ptiHVQCDJB3xA8_6wufwzooc1-Q43vW_U_qlJK2aGkqVkZDGedDMmisZU2K78CWXFwZGbkp8l_yH6nNB63ApH74pLq4ILXUcj9IPxCf0PUEwycvmB6tuVabo6X05s7PurJZPkq4BB4U_ZJRl9LXp3OwPIw-ksf36A4Y-MUPK0JI3KUYQS-0DANcjNsVmFuCwLCapB3hzvUmP5_WnfAf54WtQRMXmES8cWqn3zVMyBArZ_cK2igOX0m4FlOmzbx5PJ9_SCFpP4_BNFdK5s4FtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحویل بگیر آقای املاکی!!
ابراهیم عزیزی رئیس کمیسیون امنیت ملی مجلس:
ترامپ باید بدونه که ایران به عنوان پیروز میدون شرایطو تعیین می‌کنه
نقد مقابل نقد، نسیه مقابل نسیه، هیچ مقابل هیچ
البته برای موضوعاتی که مورد مذاکرست نه آرزوهاش.
@News_Hut</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/news_hut/65150" target="_blank">📅 23:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65149">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qr69fYhSBVkx3biunkbWrFq6sRJFjok315GhB70nzLgAW_CsNGkl6a2KSW57PnsvGa0h8sHy979XjS-PRuthc8KmGMENv2ix1xkKLwSl2j3aASDa0m2ekoGqIzDUEPMWK2hO3IQ693FmotxgrRYeDQRtrSVxSY87AE684FvzM9NbRbVKkLYmxs4K3Gw0yp4aUm87crT7Iv9jHDeQ8-MNI45bZouEUhZW6_vsFlQntHjocGhdlQx0VMps9m70EORYMjE2BBEw_MGZAcozPMoDObl209la6G1np7etSWclKRRjnF3CpR6q6WhqDLIyYkTyTQfQtQSlTACTTeB3fpY5Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمودی، رییس شورای هماهنگی تبلیغات اسلامی تهران: ستاد آماده‌ی تشییع جنازه‌ی علی خامنه‌ای هست و میخوایم با جمعیت میلیونی برگزارش کنیم ولی زمان‌ش هنوز مشخص نیست
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/65149" target="_blank">📅 21:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65147">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
گزارش فعالیت پدافند قشم
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/65147" target="_blank">📅 21:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65146">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‼️
بقائی، سخنگوی وزارت خارجه: در این مرحله بر خاتمه جنگ متمرکز هستیم و در مورد جزئیات برنامه هسته‌ای مذاکره‌ای نداریم؛ مدیریت تنگه هرمز باید بین ایران و عمان تعیین شه
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/65146" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65145">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">خبرگزاری فارس به تازگی اعلام کرده ترامپ مفاد توافق ایران را تحریف می‌کند.
او ادعا کرد که ایران موافقت کرده تنگه هرمز را به صورت رایگان باز کند و مواد هسته‌ای خود را از بین ببرد هیچ‌کدام در متن اصلی وجود ندارد.
ایالات متحده باید فوراً ۱۲ میلیارد دلار از دارایی‌های مسدود شده ایران را قبل از ادامه مذاکرات آزاد کند و آتش‌بس کامل در لبنان (طبق شرایط حزب‌الله) نیز الزامی است.
این توافق هنوز در انتظار تأیید نهایی در ایران است. منابع آگاه اظهارات ترامپ را ترکیبی از حقیقت و دروغ توصیف می‌کنند تلاشی برای ادعای پیروزی زودهنگام.
@News_Hut</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/65145" target="_blank">📅 20:42 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65142">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NEuKRXHAartI9Pe4FN_DYh4XwuXNFRI6ZK3NQaJzN7W6ZIbdkbl6ojh64VJJIVQsG5N1kjew2ATo5fLkEc7Q_UEWfW--1h07pM9Vb_E5V8W6HIglcURaatroOK3mSsgzUbGFwmxRXsHhKSmaBVrBfx5YePr8PDVqoz0Yq8wEA5Wlr-1ZCI1sOYraRnr2Z1XSHiL403JEx9mmDvIGexai1hWnUwEsGXv8vF7v0xWIDZ64k-c_xSqY-CyS8O3VGyp8Q1rCMjjDMhhtqX35SvZRY2PBuSegSDV-PLY0xEdcQNoxYU9av3Dv0DwX8AE_zIbsULei_9c0OHXafC17eC7pKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف:
۱- امتیاز رو پای میز مذاکره نمی‌گیریم؛ با موشک می‌گیریم، مذاکره فقط برای اینه که طرف مقابل بفهمه قضیه چیه
-۲ به قول و قرار و تضمین کسی اعتماد نداریم؛ فقط عملکرد مهمه. تا طرف مقابل کاری نکنه، ما هم قدمی برنمی‌داریم
-۳ برنده واقعی هر توافق کسیه که از فرداش خودش رو برای جنگ احتمالی آماده‌تر کرده باشه
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/65142" target="_blank">📅 18:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65141">
<div class="tg-post-header">📌 پیام #15</div>
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
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/65141" target="_blank">📅 18:33 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65140">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bxdn67IBT4mEuKhQdteFhnuB09Yi3i6FIm39LIGS9iGlPg_RWKveRxdmxsCHsaadrTcsnxSjbUpajFaPjrajpOy5UVEtxjtm3DokCTbPcj0H5xyTAMHtPR_aba0vsAsPxT3QYXosho1UgPjijTmSWqCTKahhogDypCN_zPLSxMLku0itv0yE3f6tZS4ekNYAqIC40D-NOI7wNKTssOY8pzqP_oUGAnzZI1xdS0mFNaC0LO4YRcwolT7-vGLqWKYCsird_qOp-_H582gkhIvL0aTlTyDDxo0FWlk7CL4Z9ZGOHmXSxzu5oEFZmDHQVml3IVkeBMpEzSqkaaYAGv2xKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز روز جهانی مشاورین املاکه
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/65140" target="_blank">📅 17:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65137">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eYW5vyXxu2P4Wy9gOGtL3s1JCzZYGIW0M2Rif50J_fUsy0R-A50RPLytViwxGsqWWCz10FUKQ-20T1-KHXQhiKzoIwN5wzjIc6poHnN5ZvNTEYEj2I9QqgIvKk-vriaMLc44QePvJt411faqHX5znSH3U4WQj0r0ekMNSO6_AQr9BzC1XItHOpUQRem4YC80yqhLnouUYBG8nMBJuv1tVhd4MdGfDtJUsDjmvbgc_iTtiyD6J0kggcsctvSJkNMX6tmXWa-EwMfuthzJcpawGTmSoTDr8Bo_Uft-ok4dPhec0iCCIQAu8fexC4yLeq6rT3VAAgIun2Sz0PA2XeRWgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی شما نت نداشتین این دوتا شده بودن سمبل شرافت و نجابت حکومتی‌ها
😂
@News_Hut</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/65137" target="_blank">📅 14:12 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65136">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IjQ-xYAlgLzxQPMTJM9XXnS4_lrnUB3-b3ViNV4l8rDyDfZ_DWdeqg-v5uO7T2Rcb9wHNMPRrt_WeHjMk9h0-BWbh9A40r92lfdPfXadjUtElbXMtAi8cBxVk57Pfd1uQDeY7U-Ed-luRXHuQtt0Ddq4ISN2pzoGG_Mapi--jKC3Fj9_JoN2jgjRM9OAJyHZGWcZ7a1HdJbJHXqLUoCkm_ZvdDK8XIOmx38CTcJtqvVZaC6O-qDxQyw1fSnB4CRcOhaffyJK8k3w8yJQOeMFoLY7DvWhr1895vfrkajbObDF_NEjdI9qWKDBDbcYeNWfYX1sUfrqdxxK824ivHnNfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست‌های حمید رسایی تو کانالش درباره چه کسی شایسته جایگاه رهبری است با آیه‌یی از نوح و پسرش که حتی صدای خود طرفداران حکومت رو هم درآورده
خیلی‌ها میگن مجتبی رو به پسر نوح تشبیه کرده
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/65136" target="_blank">📅 13:20 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65135">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24db6374d1.mp4?token=d5mhfdXFoqDh5aXZoNnEpNPsMfFFFZbYq6D5rgXOZbN2rcRyQFZplCquu7Jt1YaWlhzSUCL5Rs9e_NeiPCXf39iOgy_zzuoU5-KGCdiY7ss9FVqm3eG8jWWhaCTzNOE2Ilcfd502PtBXzlpC2l-dwFPfNPbym6H3EQYPxzKo0jLAg0YK9KW-e1-qnDOdR056LAHm3-yW26JoufIEorkXfMhC0PfN5XbAdISRqDDysX7TilqUgCMDWZ9kQpj_dunTRAN_W3x93VLTrF_RJPkVZwZ09ns3YzQShUYR9jfFxm1c0y3mbRNF5ELHKfrkz51n10hn4xEC_ujg-ldXhnLEHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24db6374d1.mp4?token=d5mhfdXFoqDh5aXZoNnEpNPsMfFFFZbYq6D5rgXOZbN2rcRyQFZplCquu7Jt1YaWlhzSUCL5Rs9e_NeiPCXf39iOgy_zzuoU5-KGCdiY7ss9FVqm3eG8jWWhaCTzNOE2Ilcfd502PtBXzlpC2l-dwFPfNPbym6H3EQYPxzKo0jLAg0YK9KW-e1-qnDOdR056LAHm3-yW26JoufIEorkXfMhC0PfN5XbAdISRqDDysX7TilqUgCMDWZ9kQpj_dunTRAN_W3x93VLTrF_RJPkVZwZ09ns3YzQShUYR9jfFxm1c0y3mbRNF5ELHKfrkz51n10hn4xEC_ujg-ldXhnLEHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ماهواره فضایی شرکت آمازون دیشب حین پرتاب به این شکل پشم‌ریزون منفجر شد
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/65135" target="_blank">📅 12:58 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65132">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iwW6rOb86cSYLhOkTCjbHYrVykpiSJYxGvLN64Tu0VqgtwgID6eHuJTS5YItPLWJE1yJ0VtchfY_3-vNuoZtRovw94ZWkcDc8RumMx4uRgeW-6eEhMmmQqTlp06iqB_zYHpdIGYlmN1gGUPW2cuoJaZ2V4G6NDBvZxTMRW0joGFyqqjwgZSUdc17vURkBQEU9MOIOOwyVFLgOwwCVOFQ7mOZzjcglgu4HCysAmm5JN7l8yPNHnnuS4LHqMnhl07COfBTwGHAbsMIx2kl_goas6WCNwzmHYX20ccPOZFOL-tTj5lj3aKNKFsnGlVp0QVp75zFwOTkYGK_bBWVhDG-pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📰
واشنگتن پست: دولت ترامپ داره به اداره چاپ اسکناس فشار میاره تا ۲۵۰ دلاری با عکس ترامپ چاپ کنه
قبلا ترامپ ۱۰۰ دلاری های با امضا خودش تونست به چاپ برسونه و اولین فرد درحال درحال خدمتی بود که این اتفاق براش افتاد
همچنین طبق قوانین امریکا عکس افراد مرده میتونه فقط رو اسکناس چاپ بشه و از سال ۱۸۶۶ که این اتفاق بی سابقه‌ست
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/65132" target="_blank">📅 10:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65131">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d098f5f90.mp4?token=vf5ecbkwFmhRndGXIFS7GU5Tbxv-e7IIEpSPMLnkA-l92n3bMkkbJcEWHnwZOwMw1DWKewE8lQ9oET3mu3t47bVUYR5wHO_X8fmkxaRCzk5l1ppgdY9MdvyeR59PEK5xf7tiqlFByuQtqCD-_IuQ3kdfdr0lViHNGMkgkarDk7oF1ZpPx-SaHZITy8rZ-n-i9IPQ09TWLA4bfL3NNfdExnwJKED8JYptr3-9vPCFHRI11g5smwSk1zIHi1YpVk8bepCdA0fXhSHXmUjDGM2Gzu8y_ULnMoOscnvZbXuXfMhTcYRV1-IlvbIHqZgzO9Pa1RwC2F0XSt9zfnRxJDN5Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d098f5f90.mp4?token=vf5ecbkwFmhRndGXIFS7GU5Tbxv-e7IIEpSPMLnkA-l92n3bMkkbJcEWHnwZOwMw1DWKewE8lQ9oET3mu3t47bVUYR5wHO_X8fmkxaRCzk5l1ppgdY9MdvyeR59PEK5xf7tiqlFByuQtqCD-_IuQ3kdfdr0lViHNGMkgkarDk7oF1ZpPx-SaHZITy8rZ-n-i9IPQ09TWLA4bfL3NNfdExnwJKED8JYptr3-9vPCFHRI11g5smwSk1zIHi1YpVk8bepCdA0fXhSHXmUjDGM2Gzu8y_ULnMoOscnvZbXuXfMhTcYRV1-IlvbIHqZgzO9Pa1RwC2F0XSt9zfnRxJDN5Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: کشور‌های عربی مثل امارات و بحرین و مراکش برای تاسیس دولت فلسطین به پیمان ابراهیم نپیوستن بلکه چون اسرائیل رو یک متحد قدرتمند علیه ایران می‌دیدن به این توافق روی آوردن
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/65131" target="_blank">📅 09:54 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65130">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mhtu6O8W-vRCkJ4jcCXHzc-Xay2_9mWhjgawayxAr1U3xpmIjSNcmEoQYEcdfJXDR0JJgjHy6r5zvNPV5QsoUDxa-I6_PyGBHqmiFgo7J3u2A852blWKZys-EB-lPP_cN5lyp13XBzUX_4C6Qfsy2D8BsmwAmC8CUHd4kXsvjhLSorCnwuKiIeurDlR2iyHaHBD7dwIwxQ0QSfGXNQONwx3yFV47ZP2ij9285TBRvgUV6sn0-q7GVfov5G8lsPqkzM0hK2rOF8yCRqUpYny_W0YNsURhjuUT-CHIBG4C0nRb8PYO5np8lsbEA0cepD9IP-6yDKVB2A3m9PrWhIIpPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش دفاعی اسرائیل: از زمان عملیات غرش شیران تقریبا ۲۵۰۰ عضو و فرمانده حزب الله و ۸۰۰ نفر از اعضا رو از زمان شروع آتش‌بس حذف کردیم‌.
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/65130" target="_blank">📅 08:52 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65127">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
گزارش صدای انفجار و همچنین پرتاب موشک از شهر جم استان بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/news_hut/65127" target="_blank">📅 23:08 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65126">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/011753724a.mp4?token=Wpe63J6II4mBVhS7qMBYFONb27NO56TaXTcK09-RSduUIs6R2Eq4R_xYR4fsVgpUuQvGyNmXQEDccx43ZmwwfMVtnI0iiTv1ava8jsYSUlMiUIsXWlkxPSax3YWhRBP_touSblYpuSdRMeTVE7Pkp_Odp-Jsbrf0ZfGNOtyBECRrrFMAi3iuCv5f6-xImEvc62wxTG_XLWVflPSgcchtfsTB16p5J7TBbHyOVg8GVdgmWMLkW_grxZse_VJRFi62lSmZkcrebKJL5aSzJ5qSAbZKaEprv86NHHBRqcfKaKWAquBuaYsrDNFCeDp5FzOHH-rU6RKgsL9OK5BzBI25Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/011753724a.mp4?token=Wpe63J6II4mBVhS7qMBYFONb27NO56TaXTcK09-RSduUIs6R2Eq4R_xYR4fsVgpUuQvGyNmXQEDccx43ZmwwfMVtnI0iiTv1ava8jsYSUlMiUIsXWlkxPSax3YWhRBP_touSblYpuSdRMeTVE7Pkp_Odp-Jsbrf0ZfGNOtyBECRrrFMAi3iuCv5f6-xImEvc62wxTG_XLWVflPSgcchtfsTB16p5J7TBbHyOVg8GVdgmWMLkW_grxZse_VJRFi62lSmZkcrebKJL5aSzJ5qSAbZKaEprv86NHHBRqcfKaKWAquBuaYsrDNFCeDp5FzOHH-rU6RKgsL9OK5BzBI25Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آیا کاهش تحریم‌ها برای ایران روی میز است؟
اسکات بسنت: هیچ گزینه‌ای روی میز نخواهد بود تا زمانی که تنگه هرمز باز شود و ایرانی‌ها موافقت کنند که باید اورانیوم غنی‌شده با درصد بالا را تحویل دهند و نمی‌توانند برنامه هسته‌ای داشته باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/news_hut/65126" target="_blank">📅 23:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65124">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🇺🇸
#رسمی
؛ توافق موقت ۶۰ روزه‌ی ایران و آمریکا نهایی شد و متن توافق، فقط منتظر تایید ترامپ است، هرلحظه ممکن است خبر اعلام شود
@News_Hut</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/news_hut/65124" target="_blank">📅 22:38 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65121">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fbdc689a0.mp4?token=ffKCwm9SmD8xn2r4BYoBUNSnDm4mtW4ODdcXHicqiWDC6ZB_kUk3G8YL1Z5QvDYb7jHUFRyNNj2yAEDefpVxt88SmqGAjr4EmTSL4ucNEsg2G5EHnnOosnCrv9-llRuKdMyvdG4TBL-ftTimCu5lat25itakyCHx6J9aJYnWKVfuQgzKkKZzlclb0TVOHgr_Z8BbaDOn4p9j5obwh0JRHx5QLbhPKkYn4f7nBthwh-pHzMZqJTMtgf4Vx4C125GGZzMU29rFk0VMR96fE6NPL1KM2z3FWUq6FUNscJA9lyiaPVlHBKn60vhLqpvBoxo0rfZO_7Ak134-XRFMBfrukg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fbdc689a0.mp4?token=ffKCwm9SmD8xn2r4BYoBUNSnDm4mtW4ODdcXHicqiWDC6ZB_kUk3G8YL1Z5QvDYb7jHUFRyNNj2yAEDefpVxt88SmqGAjr4EmTSL4ucNEsg2G5EHnnOosnCrv9-llRuKdMyvdG4TBL-ftTimCu5lat25itakyCHx6J9aJYnWKVfuQgzKkKZzlclb0TVOHgr_Z8BbaDOn4p9j5obwh0JRHx5QLbhPKkYn4f7nBthwh-pHzMZqJTMtgf4Vx4C125GGZzMU29rFk0VMR96fE6NPL1KM2z3FWUq6FUNscJA9lyiaPVlHBKn60vhLqpvBoxo0rfZO_7Ak134-XRFMBfrukg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درحالی که جمهوری اسلامی اصرار داره یکی از بندهای توافق آتش‌بس تو لبنان باشه  نتانیاهو و اسرائیل در روزهای اخیر بشدت حملات رو علیه حزب‌الله افزایش دادن
@News_Hut</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/news_hut/65121" target="_blank">📅 22:08 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65120">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">به گفته باراک راوید خبرنگار Axios، به نقل از دو مقام آمریکایی، یک تفاهم‌نامه ۶۰ روزه توسط تیم‌های مذاکره‌کننده ایالات متحده و ایران مورد توافق قرار گرفته است و در حال حاضر منتظر تأیید دونالد ترامپ، رئیس جمهور ایالات متحده و تصمیم‌گیرندگان ارشد در ایران است. طبق این گزارش، این تفاهم‌نامه شامل بیانیه‌ای مبنی بر «بدون محدودیت» بودن تردد دریایی از طریق تنگه هرمز، رفع تدریجی محاصره کشتی‌ها به بنادر ایران توسط ایالات متحده متناسب با افزایش تردد آزاد دریایی، تعهد ایران به عدم پیگیری سلاح هسته‌ای و تعهد به برگزاری مذاکرات در مورد از بین بردن اورانیوم غنی‌شده با خلوص بالای ایران در بازه زمانی ۶۰ روزه خواهد بود.
علاوه بر این، طبق این گزارش، این تفاهم‌نامه شامل تعهد ایالات متحده برای بحث در مورد کاهش تحریم‌ها برای ایران و آزاد کردن دارایی‌های مسدود شده ایران خواهد بود. همچنین قرار است در مورد از سرگیری جریان تجارت و کمک‌های بشردوستانه به ایران بحث شود
@News_Hut</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/65120" target="_blank">📅 19:33 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65119">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">⭕️
توییت جدید اسکات بسنت وزیر خزانه داری ایالات متحده.
دولت ایالات متحده هیچ تلاشی برای اعمال سیستم عوارض در تنگه هرمز را تحمل نخواهد کرد.
به ویژه عمان باید بداند که وزارت خزانه‌داری ایالات متحده به شدت هر بازیگری را که مستقیم یا غیرمستقیم در تسهیل عوارض تنگه دخیل باشد، هدف قرار خواهد داد و هر شریک مایل به این کار مجازات خواهد شد.
همه ملت‌ها باید هرگونه تلاش ایران برای ایجاد اختلال در جریان آزاد تجارت را به طور کامل رد کنند. روزهای ارعاب تهران در منطقه و جهان به پایان رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/65119" target="_blank">📅 19:06 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65116">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L2V46v1VE4fgJyRHu_CVtXo3gDkhmFwB31KJTGkYTQQEnzocYgGn43gfR00Xo80yQ5elkp6HIX_0IGLuOiNtbXcOvcqaNh0gc0PBKv2yzrt9LpIWX2YrRJHlGiqj71EbNyfWX2VhfElUzNKkxC81EsuaWFcOXQoeqh-pvgKR5JinsNk4slRWPjzGy26yi8lA5DXP29JxmcFNztNUvOnxp6ya9w8nUbjAZDHuNzu_UxAq3dwa-rV6PSGUvliE8IDMuZGLHVc6IozG3iIqpkcTZPKyRnxCr30seFsQvxFGl_ao6cEVN3YOf4ZYTwXXQbWGGXtW1bEJWcDHwC_cY02D0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📰
آکسیوس: اکثر شرایط تا سه‌شنبه نهایی شده بود و مذاکره‌کنندگان ایرانی بعداً اعلام کردند که تأییدیه‌های لازم برای امضا را دریافت کرده‌اند. ترامپ در جریان توافق قرار گرفت اما به میانجی‌ها گفت که «چند روز» برای بررسی آن می‌خواهد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/65116" target="_blank">📅 18:43 · 07 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
