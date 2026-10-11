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
<img src="https://cdn4.telesco.pe/file/X2vhO_RfsG2FwHv5iDTvgW6gK4QqykL8bfl4iWAgj6dvkaEgStGoYHQXg7XZIdPx8_MknYDkT2a60EiObWiUavayGIgUN2yFslGJMfquYbqkMtNvcz737fh25Vo3_S2v9xmIdytAXpoDcYmNOfwKueHmXe5kyP5bZf85gv0AMrepQh86RL9vbDZ8pUeO5kk77zzaoxsAs0UMokNlUhNQyCA3sB9Q2EGRuV4aofzMYOpFKJ_fJn6-HOJkH9DIoZEyIU15JjflI8HU0flSIUqeP0SgdvQaEnUTrX1VMyL19zErvzlQW17Mqe2oFZycM_vsrg_kBN0dGlaXEDTeKs5nbw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 268K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-19 21:42:35</div>
<hr>

<div class="tg-post" id="msg-84708">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">تا دیروز هر روز صبح میرفتم سایت چک میکردم بلیط بازی بارسا و گالاتا رو بخرم یه امروز چک نکردم کسکشا تصمیم گرفتن بفروشن و تموم شده</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/funhiphop/84708" target="_blank">📅 21:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84707">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">تا دیروز هر روز صبح میرفتم سایت چک میکردم بلیط بازی بارسا و گالاتا رو بخرم یه امروز چک نکردم کسکشا تصمیم گرفتن بفروشن و تموم شده</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/funhiphop/84707" target="_blank">📅 21:11 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84706">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">خاطرات وینی پرایم داره برا ارائوخو زنده میشه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/funhiphop/84706" target="_blank">📅 20:30 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84705">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">دوکو خداسسسسسسسسس</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/funhiphop/84705" target="_blank">📅 20:26 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84704">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aNg07j-SV424XMO2xnrX0tGVkKUgR0U9DZ2m0XLEIQ8yzaD-n2CpJ5RRYIljx3_4tm3NtLMqgjXTwxyio4YaBuKhX0q_8lsJdKEjBAY7Fvow70m7ALrwpzG68VhslutL0MJs1wSClt2iWOvvzdO_j7Tw0_w6NhsZ2XtFPm07iGF68yUrpHtb6MNnox4cfYznUTs9q73oARA44V-k0MFs8s0LpCNMC4Wwm3NLP4ckqSbcdewvFlxlSa0YrkbedwQuYbrOVCa4skt14VU2j_gc9vYXkZlnOE8xNi6zYub5bGGApDOYKyxhUJ7oHuSYNRHqMUmkRr7w0YzdE-2-w-DzVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چه سخنان شگفتی به زبان  می‌رانی، ای مرد؟
❌
چی کصشر میگی کصخل
✅
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/funhiphop/84704" target="_blank">📅 20:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84703">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cd2361427.mp4?token=of8OKQhQUP4STS4-E62APz9NZzjLMFGOUaPF-wMdKvc1B63AO5TYUvPjNzZPT1ORyOJ3p7ce3c7SO9bXhXw415Mpivw4-HrPPxnvutqx8t5Hn-R_gkc7ucTxnDBSpb9KGDuxSFdnhUKX2Rj2xscXi1WgGy1mwgggfm54nHu-XpKBXk13SRwGzfw5jm5DpCtE9bOrWUGx5uTtFgLr2vU-W_l0Ctx29VUaDMrahcxI3Co0lY6wEg14LBofI-0-jVDO_S76rNKA7UbsZvRgC0gysMqBdFqUcFKmZIfZ4aPtcJ4QDalbh0LD6LvQY0nWtpWB5thD_itl3JXtmRSb45CChJZXFqLwXWXKYuWUB0C8k1zf7LKsrjQjBoXTunkdWpYVJtezK7p-dMFPLnZT2cpdGb2g6ilrsPvvA7qJ5se8YtRmm2VU2DfrO3GYWruoQLxSkJvpiAU2zR6Tkhpot58zTQUlhm0AO8JpajZT9hoeHk8sWeMel8Z-_mpSPwwZVX3CKYTa87E0sTtMH_jZSFP6XNKnwiM7Ab7-yFXXUSmVje6ABt8XoEZHti4L0SNt0ZYxYdjQA2bb9Sk6l9PEDHXebUWaY8WsOmW7YGm4Vp4FsHYRp1swYN1J7IahdEKRXFK01n7G9fRNfhJJSUjNzuIXN7PjoNBZ1PNYYsJmDkeLC8k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cd2361427.mp4?token=of8OKQhQUP4STS4-E62APz9NZzjLMFGOUaPF-wMdKvc1B63AO5TYUvPjNzZPT1ORyOJ3p7ce3c7SO9bXhXw415Mpivw4-HrPPxnvutqx8t5Hn-R_gkc7ucTxnDBSpb9KGDuxSFdnhUKX2Rj2xscXi1WgGy1mwgggfm54nHu-XpKBXk13SRwGzfw5jm5DpCtE9bOrWUGx5uTtFgLr2vU-W_l0Ctx29VUaDMrahcxI3Co0lY6wEg14LBofI-0-jVDO_S76rNKA7UbsZvRgC0gysMqBdFqUcFKmZIfZ4aPtcJ4QDalbh0LD6LvQY0nWtpWB5thD_itl3JXtmRSb45CChJZXFqLwXWXKYuWUB0C8k1zf7LKsrjQjBoXTunkdWpYVJtezK7p-dMFPLnZT2cpdGb2g6ilrsPvvA7qJ5se8YtRmm2VU2DfrO3GYWruoQLxSkJvpiAU2zR6Tkhpot58zTQUlhm0AO8JpajZT9hoeHk8sWeMel8Z-_mpSPwwZVX3CKYTa87E0sTtMH_jZSFP6XNKnwiM7Ab7-yFXXUSmVje6ABt8XoEZHti4L0SNt0ZYxYdjQA2bb9Sk6l9PEDHXebUWaY8WsOmW7YGm4Vp4FsHYRp1swYN1J7IahdEKRXFK01n7G9fRNfhJJSUjNzuIXN7PjoNBZ1PNYYsJmDkeLC8k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
تورنمنت پاییزی بری بت؛
5️⃣
🔣
1️⃣
میلیارد تومان جایزه!
💞
🃏
پاییز رو با یک رقابت داغ در
کازینوی
زنده
Creedroomz
شروع کن!
🎰
🎁
هر هفته
0️⃣
5️⃣
7️⃣
میلیون تومان جایزه نقدی
🧭
۱ تا ۱۵ اکتبر
🏆
جایزه برای
۵۰ نفر برتر
⭐️
هرچه
گردش مالی
بیشتر، امتیاز بیشتر!
💝
بازی کن، امتیاز بگیر و برای جایزه‌های پاییزی رقابت کن!
🎉
📱
ورود به سایت
👇
📱
https://ieoruyxtsud.shop/fa/affiliates/?btag=914641_l303106
📱
کانال رسمی ما در تلگرام
👇
🅰
g19
📱
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/84703" target="_blank">📅 20:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84702">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AmGffRPiTIbK32aWcNr1Ddsx2SHGf2sy82cEaC5DMOvb0iwgUspT6mxjaocQlwrTDZLoKY7YcrmP98P0UhOxNKYr5Pj_-pCh92gQUx0Iqw0Jo7hrh_EFOY-8mr2n4J97XvSvqNFiwzOsBGGLqLPW0vaO9GLi8dGD_WLGVxLzG-yD9MEJOG4aM-1FDUP_uH3z8Q557YQxu-rhDUKfp1bFiOZk5-HRd35HEg8h4p6Z1vk53wRztJXE3ykAa8rl1duwvjYFx4k4tgCbYJ-ykkpbLIL-zNGH3hSG90aS395FHFwZUfGGRVFNXG8aIcyRHgq6--1TeQsVBYxTf5ht8u19AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو بابلسر ی کافه افتتاح شده که با پستونک به مشتریا نوشیدنی میده :
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/funhiphop/84702" target="_blank">📅 19:24 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84700">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lL7YXPi74JAG1zMrIkgg5zLWSRHw_560dq1KkGX7fbCBRE5X5mzi-4ro6cKwebtaDx7CLWvxYs3g_MDlK55u21IgIx8TEIq3B0kXQ0IqohHo4FrJSK0_s7bwaozyD8zKUvAJjdLeVkRiL4S0mFOXIlYBRp3uLRr6LLmU4IFjFclxmlHBz1VostTR501BYPsaeuH5UudF4XoARpX30n9fO-x_1AgGPbUiL7czYyIjlQKxXzpzXdcywT3aXRNDho5u0OC3ZAZ290migKZwSycoCWloZ013_Ronyirba3tmJ9yjSUbBROoJTEN9GrgF8RJMSRJ3XZKAAULk8A7YTF3T2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا به طرفدارا لیورپول صبر بده، حضرت ایوب هم نمیتونست همزمان مونیوز و بارکولا رو تحمل کنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/84700" target="_blank">📅 18:04 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84699">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kdOJk-ZFX6wqvv24ufwgC7DSY4-IFiLF_BOdgcinOs9AQ4nOZbLppti4CNTNOwBrRTXJsmHUJzxnr_fw-U3qG6RrGsUQG3hgFP-jajH2KI6Hi_tWL40_6KgNAC4d8i7T_CzvXuhcSuInTIrK6tqW0-vblrPlpWa2OPj__LtPuTLlANKeWVHF_XkYHe0M1YnZtKzE7rw_US5xb_QfnZiXuKj3iKkuvpUy13hKh3dZNNQauuaTcuREnZbtyB1RRmpmzHZ-nSPgkJR-p64_IjPk_mTe39F7_P5PEwPgl0cwkipvFA-uJ-NgQu8orFZKjvGAfTRDkGwp-atvftj4viz7zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسیری که گل‌گهر برای رسیدن به بحرین رفته:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/84699" target="_blank">📅 16:50 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84698">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dde88b838.mp4?token=TyKi8e8UNBxn2irITQ8qIR8PbNk8dnPdMoKqfMcqNwk7dU0e3XktaDqebIn72zW5yR7Ytr7qU6GL6-eut3GTOEvKcJ4mW13dDdnyJ86VFS6rqteGZFt-kVqDRB5xkH0CWsVtaoq1ywQreAXevaBkvfcrwsBBoysDha96f9_lt_oAI3GAedwlBHg-FLMw6UNpQF_wwbTmDMytmiq4Lr6GO7h5xM176c-DGVQgwOyjxJe15eUaMPINf0Xk3h7Ngp_gMM6NGRwym72hM3MBUwyVznyTH_MDmNDtXx6KZH_5VDtHI-4L26vqOQa16xC3f8C6y56_U2vniYoaP8Wk2WUD5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dde88b838.mp4?token=TyKi8e8UNBxn2irITQ8qIR8PbNk8dnPdMoKqfMcqNwk7dU0e3XktaDqebIn72zW5yR7Ytr7qU6GL6-eut3GTOEvKcJ4mW13dDdnyJ86VFS6rqteGZFt-kVqDRB5xkH0CWsVtaoq1ywQreAXevaBkvfcrwsBBoysDha96f9_lt_oAI3GAedwlBHg-FLMw6UNpQF_wwbTmDMytmiq4Lr6GO7h5xM176c-DGVQgwOyjxJe15eUaMPINf0Xk3h7Ngp_gMM6NGRwym72hM3MBUwyVznyTH_MDmNDtXx6KZH_5VDtHI-4L26vqOQa16xC3f8C6y56_U2vniYoaP8Wk2WUD5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقا ابوطالب یک رپرا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/84698" target="_blank">📅 16:29 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84697">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">دختر خانومای گل، روزتون مبارک.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/84697" target="_blank">📅 16:03 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84696">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NRvVFJiOxBDM0ayAFgPTL0_0AY6Ndk6_dW6VYqIFnjvdRKqMUE_4CO2rj_DzBwe775q2LiAmAQBYeDsBoPNjtVD0_tRmZL9TjaROcni8NrKAmDcwVgIWXSCnMGAcqpBStfRS009-qFDbyYtpzYG154uZID2YHElBSmb6GQHHvncgqhmGrXmvCHIyGrFpd2MFB-YtA88lR5-Cnl7fTBDgBCDHUkhDISoDOudocMsnpLLyXyc1P3TJGriPRj8xyQ-bv_hcf597EE1qrFj9SN9eEaHy8wMoJVUU8HB6K98j6AlgcQGv0oqqBmuPHwXqD5jlGDyBYSIFTpuxmdfpDEum_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گراز پدرته کصکش، حرف دهنتو بفهم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/84696" target="_blank">📅 15:44 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84694">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JAyzh6NaUdRrwRYCWwuHVWGbbNWrPQZMDaXzMObiJRakzd8pTGqUTAqotLYaOx3bH4JT-lcxsrhUdcNd0oqK8mr8z-Tom3dpsB8WYFffc4Q9v5t5e7k2VL-SAjBRYtRP72O44JYITYXjeVhNfYJ_kIzJvaoKYq_i7q4wUn4YDJteg2XHu9Xr1ocHAAI-5qaKj8ZNtRyuNsrcm6FN_Y0QiF1qYL6Q8-XuEDu1RVokDXwiqRwxEx0wcGTgpwJvQ8WPnAbq0ZF10cMF0ZUxc8F72XzPRecncj12xO4JotGcGfDm0dh45e6ZRVewGWQgIMtH-UiiKxLahKbYHApYK31KHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منم یه سری رفتم موزه همینجوری تابلو راهنما رو با یه شاهکار هنری اشتباه گرفته بودم دیگه نرفتم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/84694" target="_blank">📅 14:15 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84693">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">زلنسکی:
اوکراین آماده است تا حملات خود به پالایشگاه‌های نفت روسیه را متوقف کند، اگر روسیه نیز حملات خود به زیرساخت‌های انرژی ما را متوقف کند.
پ.ن: این ترامپ لامصب چیه که از یه راست افراطی مخالف مذاکره که کشورشو به کام جنگ با یه ابرقدرت کشونده همچین آدمی ساخته
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/84693" target="_blank">📅 14:01 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84692">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/548dd7a29a.mp4?token=bAd7OxmF0SNLhXRYeOh_t_Y9h82TXzYe48qcrx4kBDAsouUXI6HTiwlP6S5LJThgvdzWCh9iKBApIg0wzBjSkm8phjQE5GFi0-nIkUyN9Mpur_F4jllPBm15Frwa7f1DMXM23txibZqqEZ_zOodxdr7LWml3-AzUpjcMakabAvVCXg5CLcld6ZVIvWmQNsXTFsTFt-3SJTkrDXomup4pFzzbOmfvog0uDv_yBGBU2B8OpYeAh_rpGdbfGiLal9gYgdQZ7MBAESL1Gepx0VR-lJvfp5YgTxDPEx1hoD6XttLOTf-fRtgaxSgQIXAz4ouGXvGljBg7kMivHVX_ayyJBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/548dd7a29a.mp4?token=bAd7OxmF0SNLhXRYeOh_t_Y9h82TXzYe48qcrx4kBDAsouUXI6HTiwlP6S5LJThgvdzWCh9iKBApIg0wzBjSkm8phjQE5GFi0-nIkUyN9Mpur_F4jllPBm15Frwa7f1DMXM23txibZqqEZ_zOodxdr7LWml3-AzUpjcMakabAvVCXg5CLcld6ZVIvWmQNsXTFsTFt-3SJTkrDXomup4pFzzbOmfvog0uDv_yBGBU2B8OpYeAh_rpGdbfGiLal9gYgdQZ7MBAESL1Gepx0VR-lJvfp5YgTxDPEx1hoD6XttLOTf-fRtgaxSgQIXAz4ouGXvGljBg7kMivHVX_ayyJBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنازم یه جوان فلسطینی که کشته شده بود بعد از به صدا درومدن آژیر خطر پاشد فرار کرد.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/84692" target="_blank">📅 13:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84691">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vXrhoQt48uBZQRVcdMhtYDvd_KCaquVOcSseJ2aoaDCeasKAKxdPZx2x3wP-kgaLYJdFMaEscRYuYvrTNwikf-rJYUz5T3-JZ8WWOrXw-yanLqdLd240Xus7lOFa163XoDvDETCH_oalxJ1uJRyhGmz0-0bKJPRaqEbwcmPT5lWvNGJb-Jm5mwh2SoY9lQqJuR-kxPrTadb9FKpQx-qHFHTuP6F9q0kA4hLqJ8ys1NWOlMlijJfBEnmAUIVDePv7P4kPoYR9RKnnDtQ4RDg1A-qq4JINJr7ibKB5XfRM5T4hgyIE9DjWZEtaVq9-hr2q4YjfUm0uXcTFQh271fchjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گنگتون بالاست مشتی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/84691" target="_blank">📅 11:48 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84690">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">همین حالا ثبت‌ نام کنید و از بونوس های جدید ما لذت ببرید
💵
🛍
👆</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/84690" target="_blank">📅 11:48 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84689">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LtCiTpyqxSc2vG-thpR06ECyI0mMCl7MwmqrDV9MH24u5HRrZ2t1253Y_BLOrneFspUBQffs-XBeKOzqN5V23pz0fRuj4D5WKtao-NFEtoT6VXxFh7nPoA0Pllhg6afJufuIV0zhEcCAdydpnpb2kaorWLOsRYLJ3xLlMQTr6OBx-WwPU6siYLyfhS7LXOzBJAbgbSVyLor7LkltpFdcI9zkgvRaH_dJxt4rOHyHEWePasyn_c6XIj8p4GmN15BrGuJJVdsac6fdLcZZ28viNqiBhL6wLVoeS2_MvSlIEwh-GcRG-ip1_0t7_qhARJGXQ7IgXlOeEYwboRaTQkacyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡
بری بت | BerryBet
🔥
مسابقات امروز
👍
⚽️
لیورپول  - منچستر سیتی
🌎
ساعت ۱۹:۰۰
⚽️
هال سیتی  - اورتون
🌎
ساعت ۱۶:۳۰
﻿
💸
ضرایب ویژه و رقابتی
⚡
پیش‌بینی سریع، تسویه آسان و پخش زنده مسابقات
🎯
همین حالا شانس خودت رو امتحان کن و هیجان فوتبال رو چند برابر کن!
✅
۱۰٪ شارژ بیشتر برای روش‌های رمزارز
🤙
ورود سریع | شارژ آنی | پشتیبانی ۲۴ ساعت
کانال سایت:
✅
https://t.me/BerryBetOfficial
آدرس سایت:
🅰
r19
🔗
https://ieoruyxtsud.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/84689" target="_blank">📅 11:48 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84688">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hp_qqoZos2FSUyoCO8ZYdSkZ2km3mVIV0f44-NS-vVDFtQM-rQqdbzu84ddX-hfuk-F1I2ANP14-K8MVbwikLesYxffyu5V2Fep-e2NgAVjRAR_o0h81Z8s3aHNpNAn_0l0BLZmTJe0hRrL1PNkPDvLHECQ-iwE5cmg0twvOmw2LFWNZCZ15FB6a_D6jGKFBJw4fUbn31PBlj8jOsv2b2Mpq3030U0xJUNqcROnQDP3-X1RigwD3It9wutw6jRVqtKGDgskQ6FR3yEwaWnmhMh9NebopV75iXE0mRwDAMNhXufAiG2Bt_Jdt6E_oH-0d6QPkn25USGdvhbnoPBDZnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دم هرکی اینو ساخته گرم یه ماه بود از تهه دل نخندیده بودم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/84688" target="_blank">📅 01:52 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84687">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gJtbqiyHTR2XOmtxkgwzp3CI-fyevt-LsXufhwgk0DWcAlZEbyluC_n8jAytRG9OsUX4Q8HmsOEEl2k-ajxp7mplclFNJiqdIbOW8oATxO7teSajWKBj_il1ibhpR6NfjXen6-3_Bngu4tdCeSpPk_P1_qK6chuI-grhyGhFLHToBk2cPx3LEt8qoSt3P8VD0NGXqh2f3oiIUqrWdgTykyJ2NarGWbG13Wlp8jIjGinqrMXYvhMLYy-XSOaJ3UVS3o9GFgbPpFUFRAJrPkihzhNvRwf2kTNpGoxK7zZn36MQ28Q-rASoNGjdXQHgYy_0ji6lWs1-a2UEWv99Pi-j1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بمیرم واس دلت دادا
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/84687" target="_blank">📅 01:24 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84686">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">داور کسکش فقط به من کارت نداد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/84686" target="_blank">📅 00:29 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84685">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b32a1ac263.mp4?token=cpSeOdt6cYb1rBZvwMdVAiUa1Jp5X8GmVNdnBpPEk3BOJG7MTsBmpy-kS6w63AJ0PNPOsSyidGRaPQQAPM8xaf2tWgme7zIO6yVy_x7l9amHqqtWSKsrxgvKfMli-hByDdVgbxdsz5yYqUY8cQobp3b8xBMU2-0xhMWvRwAsk48TclQN2AQWx_gyS9xkZnlGJsP5pKuXMvvNeuo5TzhUQAiC7jBCnbaaUXW9GeEPJUS2-L8LaRJ9l4NdNW8NhiP8QNTfaDa5CpMrXf2W4IiFMuzD9RbvoWgNG5iKtmdOpCyVvVxZGehPAka3mJa5O_mZjwFuBjEXpdnFW6FSmzOjF5Pf7rde7c7bLakYDXwf6vU601Dp7lLlQV2_VCjxFJITm4S5uAVGplrg4AX3bAyrirACHdwGR2DRmIxGOkAnMSMCqPemtNZUQ4RA1GcWTmyY9CJiDBXNzcbijQ-TQxYmdvCikk1JAti50iAszsKxvWoyDTixAJOEUaeHbMvQZLvxF0I3D335t8TguYBeu-lyNi12_qJIt90nVdufKrlokYY0b2uuZh1Hi7mrV97LuiWD6x2pHrzOin4rhpgpuuDSn2cb3MoGFkpswTD_QM8J9WUttTtubvVzQJzfFw5ahVy6ISFbiJJD-vV55GJ2bPu_aytilR3RUNTBRwjyP6aP5_M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b32a1ac263.mp4?token=cpSeOdt6cYb1rBZvwMdVAiUa1Jp5X8GmVNdnBpPEk3BOJG7MTsBmpy-kS6w63AJ0PNPOsSyidGRaPQQAPM8xaf2tWgme7zIO6yVy_x7l9amHqqtWSKsrxgvKfMli-hByDdVgbxdsz5yYqUY8cQobp3b8xBMU2-0xhMWvRwAsk48TclQN2AQWx_gyS9xkZnlGJsP5pKuXMvvNeuo5TzhUQAiC7jBCnbaaUXW9GeEPJUS2-L8LaRJ9l4NdNW8NhiP8QNTfaDa5CpMrXf2W4IiFMuzD9RbvoWgNG5iKtmdOpCyVvVxZGehPAka3mJa5O_mZjwFuBjEXpdnFW6FSmzOjF5Pf7rde7c7bLakYDXwf6vU601Dp7lLlQV2_VCjxFJITm4S5uAVGplrg4AX3bAyrirACHdwGR2DRmIxGOkAnMSMCqPemtNZUQ4RA1GcWTmyY9CJiDBXNzcbijQ-TQxYmdvCikk1JAti50iAszsKxvWoyDTixAJOEUaeHbMvQZLvxF0I3D335t8TguYBeu-lyNi12_qJIt90nVdufKrlokYY0b2uuZh1Hi7mrV97LuiWD6x2pHrzOin4rhpgpuuDSn2cb3MoGFkpswTD_QM8J9WUttTtubvVzQJzfFw5ahVy6ISFbiJJD-vV55GJ2bPu_aytilR3RUNTBRwjyP6aP5_M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
این فوق العادس پسر. من میتونم کسشر ترین حرف‌ها رو بزنم، و شما تشویق می‌کنید.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/84685" target="_blank">📅 00:23 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84684">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">مورینیو رو
😂
😂
@FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/84684" target="_blank">📅 00:04 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84683">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">مورینیو رو
😂
😂
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/84683" target="_blank">📅 00:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84681">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HLSn_faI7BYIpk_9WKLQetk8tXm4aAl_eWsCUJqlJVFwSBH2lyAdXZ2Xo_qeSUOGUdpdgZ1xXCGnfd48QDobM53V0Ru6ugARcYJm3Mn5TRPEsPdnZWwhkSaEiJYuYv_NUEGNEVDsKizUsJfnFZs-doWo7UOJWUDjYuuRtmEtvwrR_vfwOY10uCqi6VdeuxDQLwsQ66ZnmiA0EWdSH6nzTBjTq4A7tYQZGcxdCzd4hNDT9gvMZFB5-UTkF8cLdgwcS5Y9gx-iFeb8dRT9_KpUxjVMtkQXaZ-F9WuC9ypCOTNA3A7Iasc5DXcq2yh9LdL-ihy8U0sARnyCuB1okKtFJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xs1Sty9aBtC2_NejmJnOy2dFrJtTUMUpDG1tu6qm8jvFR3alVjo2yDcbR1kNMFgNc-EmOwX1-lfJbXnbr4toNjyaaKR3Q3_c9GGYUxnMZ5c9HqsoQjqUr3CY9GhWmAHL3orEnRxM6VswMXmzVH3yI_Z9wIGjHuIq-GcJslGX1C64ysFPqfHruzD2wWgA22BcONnm-d9Ko2mY4B_d7Cdyy_X1ZyMxZ5xZ8TelkI7gfbRULok0INl2N7ZIt8yZI-HpIQsjc50k2AxqK5f_g9zQSX9BJAG-v9U2sbW92xv4X7KpVJIE2WMNVMWQVSFt3J-eOcQEZjuFtYkyjCYj0LPaKg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">با پاسپورت شمرون به ۱۹۵ تا کشور میشه سفر کرد؟
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/84681" target="_blank">📅 23:46 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84677">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kQgdxwmjuyoBvTQVeVM8uQADuMjZF1ACsrI5a8BjmJVsc0r1FiNUU4TNjHsY_QoyagZkVrD9N4xd2F54_xZXc-cAPLCWvyblCElAxmBqIp9xGJfL_1P7bRg9tvNYtZzcZ0W7B31dLDjTeCAlnLyMT3ETxPdlQXmtCQoh45U4p1K5EJGyUkvG5QQTgP7x5HZY80JFCti1CwRpmR_MAfFMrmHzz-6lwj2yFXIiIKD08zIVF9DZ7ZxcJXA1FaFaywX-eoN6TscJ8FuPVaUzUvrbXKHa0FJImcyjzYWd8E-FesYohNsO-s-N9ciFksZXfB1bCCObSabKAqCttIKE06-eXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bucuMaHf9c0Y00Wk5FeHMhLKVshGvjFseNmsTS0l1TUC-6GsqnPPJsqC1QjfMKRT9AeGIP-tyKkV7ra88mgQfQ74o8P-UYGmTBZVsic9PastAaeLu32L1p-dyiSu7bvqxIOLKE8rwThscqSlymnJl1yxIwUHXOu1hjS9NO0s4pnep7nkDc69ov71IE4So2WZnRGQu3gYZdcvMdv5tC1c2A3wLhx6L_GPvNgLWbpxiWiIY5odQmC5ts9iizngF4Rj7Lsypu9GIBwVQ8ZXRxesWLgqdTaVvm3hjW3Fwe_skFolhVNiWCtLsU6U4OTbCKw8p-CNkOqZjoOMepVZUr_Vbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GL9QwLFtA-0Kj2uCswmNSjUCuEQ1rjruOvCZh9NQc7rDtHlzp6D5AKmvV9--NTK83obyjh_W9DwytoyQWyY8JfHOIaiy4HxqOl4PL3J6UPEm31ALmdg7Dc5S0-BzzzD2DUK6FVbF7M0noGLO73Rp58bpPgElT5ZuaO4gWfjkeSDsGjsQWnoGPQHRF__IOQY8_SdS4aSnc6e842hdWlZAoCm7dya72zwdlZ22PbikUi-yPnx9v1umdqBAqvnz81EQ_IDq9YxKGW7R-f4rvX87kLxNCLa9y5dZKMLNKnLEqPKyyIzHRNvO5Kyc9qpSpU8CMfpiy5Q6HifqgJiwh6u91Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hPdFVSjOW_m2ojb4RnsHSgbdMTTLQjnMVNyv6TNkkYppLhOlAYCmSS-6KcTM6tY22I-tbrWD2k_o7Mt2fUq_pc4hIl1O_QStBDZlGYpxrOozwQle2xsKCM2tw0-qTYoOUfdn71wwFAurvi_Iy9tgxBuztuvJDukqlA65nEEj0rLk4Xy6WACbkJERv5TCPamSZsIkWprkOjjriDzq6qO_Ivg-9YxdvfBSeSgswaV8zEZ2DrtBZcOtOOYrOed2BpOa9iYwkXU_rKECQ5-KpQxEbMemvOlWMIus2v1NuDkGAGlb6PxwWoFzsG3HRz-mXuYUMhQgBb1JyY1i7WcP3VsMUg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بسیجی‌ها امروز با پرچم فلسطین رفتن دم در سفارت فرانسه که به سرکوب خشونت آمیز اعتراضات تو فرانسه اعتراض کنن.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/84677" target="_blank">📅 22:17 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84676">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd88d22e31.mp4?token=TAFwdhqadKlopa4qVv0SDrztVLqdCm1dKtUDKTCybx9MlXWdIbQm-DgA3vWLbgxMN_QsfB7ffY73Jtb6llRzbHj4J9N5ZVBKm69T87hrUe_2HHEuN49jVv6ZcfOcSkNQHDa_tc7hWZgFEw9kMjyMtWnBSMDgWx5WIV54biNfEtICWGMQ29Tulxs1iaKov1AgVNwoYd8bCERyQDWcyE6j6CSwhDoSIo5lW2RnEJUx82iprj7ES7EzaJnBKy_IiQ3RB-hEppTpvG_GDAvG85wTN9zpoj_MsNjK3Gs7zl5buIi-HCWEnp_RvETD-JLovOq-tUIRUlPi4G2pqeEVg7KD4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd88d22e31.mp4?token=TAFwdhqadKlopa4qVv0SDrztVLqdCm1dKtUDKTCybx9MlXWdIbQm-DgA3vWLbgxMN_QsfB7ffY73Jtb6llRzbHj4J9N5ZVBKm69T87hrUe_2HHEuN49jVv6ZcfOcSkNQHDa_tc7hWZgFEw9kMjyMtWnBSMDgWx5WIV54biNfEtICWGMQ29Tulxs1iaKov1AgVNwoYd8bCERyQDWcyE6j6CSwhDoSIo5lW2RnEJUx82iprj7ES7EzaJnBKy_IiQ3RB-hEppTpvG_GDAvG85wTN9zpoj_MsNjK3Gs7zl5buIi-HCWEnp_RvETD-JLovOq-tUIRUlPi4G2pqeEVg7KD4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمسه میگه به خدا من بادیگارد ندارم چرا به من فحش میدید
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/84676" target="_blank">📅 22:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84675">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QQi-EFLutwKaH4Ptx3NgKq5A0E2MRSkd6zHLfYVigsfR7wdRsDS2KQKrJvOqutziWLu4WwBvTt4K_HzWq0d_fD_ZClaAgy7V5mFvrZEH1exAEnmX8uarHiDR7YLfYCBnCytNgDuspAT3YnwhCwogHyHgl9jTS2IgQY0CQPsYN9D5aSSYUgBe2aakVw_5IyaiJqf0bAEqprr2blJwDeytErmB819stmxfIPQu979r5e-6ZUf09WWDHmoBgOBVMMjQ_ULE9v4ucGEtA4gM8r2GhCfzSNRi7cmc1VxIcPZwFoKu4X6vdcBbCF5KB8KE9l3jq6ZvavOkibfVnClzH-Sp-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاره شدم.
بعد از اون کامنتای مردم، اسطوره نوید برگشت به تیجی گفت شما اسطوره و مرجع تقلید منید و افتخار می‌کنم که باهاتون تو یه خاک نفس می‌کشم؛
تیجی هم اد استوری کرد نوشت پرچمت بالاس
❤️
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/84675" target="_blank">📅 21:19 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84674">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from“Creator”</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Talangor</div>
  <div class="tg-doc-extra">The Creator & Lickel</div>
</div>
<a href="https://t.me/funhiphop/84674" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">ترک جدید The Creator و Lickel بنام تلنگر منتشر شد
🆔️
@Amircreatorrr
🆔️
@Rapkadeh_official
®
🎶</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/84674" target="_blank">📅 21:09 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84673">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from“Creator”</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NP937n-t85SCG0NJxHtkj_-sK2Cbz38Hy0NC1wQJ2yBcUMGj2lBonr8k3gzAvND7fZQOEDLlWl0cTaUbuXLBIYBAVezaN5YaA2TtvOPQTX31McWZDXZLyfBvFvk2JcnbGDWKticXRg82FJcZoe0GXbtyjiK-w5x-9GZxeimcBTnmSzTSqhdfx2JGNvIVjPaCT0jjTfpXSpvpGdIqZDSnrsgGnw-TiAvbMhFdWpC0HFEwt3Y2N8cqnuW9bKedRrz3GwhTFbo-jp61VMC5EArM4sgE5qBlxQv8Nk26W6M1zpy2-GPyqJoZa6JiguUhjLnUscTx9qdymcSRzL_9t8WvPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید The Creator و Lickel بنام تلنگر منتشر شد
🆔️
@Amircreatorrr
📥
Download
نظر شما درباره این ترک ؟
عالی
👍
خوب
🔥
متوسط
❤️
ضعیف
👎
🆔️
@Rapkadeh_official
®
🎶</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/84673" target="_blank">📅 21:09 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84672">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25eadd38c3.mp4?token=bizNDSAaY1KMEXyn6pWCwoB8GQISLnpFMAWIGWGg7f1eHI6MsHxBrAM212dwmCX8wFn4y5TFAzwCkM2kk7m4YgY4FmWIEtS0saA-1AB4TImMjnh4z6D81f9GVXljA8gzsS1zajH3_g-A7rax5SUUjj4A4Wt9Q5FmIGDVoPSNhqCxImbZoMDdOUM2Zis6vVSFLBFK5lEHL884KqjWKAngYkOiISRBQvSFC3a8aTJDt4mePcQ--hMTqEv794H2ooinYFRb5-auxemnI-fK3Cj_l2vLQHFgczzXy-tgNmvDuXfHRrltgbImavNMm6ZRg_5USu9jyTEARn15J7qtONVYFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25eadd38c3.mp4?token=bizNDSAaY1KMEXyn6pWCwoB8GQISLnpFMAWIGWGg7f1eHI6MsHxBrAM212dwmCX8wFn4y5TFAzwCkM2kk7m4YgY4FmWIEtS0saA-1AB4TImMjnh4z6D81f9GVXljA8gzsS1zajH3_g-A7rax5SUUjj4A4Wt9Q5FmIGDVoPSNhqCxImbZoMDdOUM2Zis6vVSFLBFK5lEHL884KqjWKAngYkOiISRBQvSFC3a8aTJDt4mePcQ--hMTqEv794H2ooinYFRb5-auxemnI-fK3Cj_l2vLQHFgczzXy-tgNmvDuXfHRrltgbImavNMm6ZRg_5USu9jyTEARn15J7qtONVYFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ببین عرفان جان میدونم ضرورتی نداره من الان این پستو بزارم، ولی تورو خدا برای یک بارم شده یچی بخون بشه گوش داد، من خیلی دوستت دارم ولی واقعا نمیشه گوشت داد، لطفا لطفا
🙏
🫀
🌱
🌹
✨
🌟
⭐️
🔥
🌈
☀️
🌨
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/84672" target="_blank">📅 20:47 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84671">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
ترامپ درباره اوکراین:
«پیشنهاد می‌کنم اوکراین رهبر جدیدی انتخاب کند که بتواند به توافق برسد.
-به دلایلی، زلنسکی هیچ‌وقت به توافق نمی‌رسد.»
بابا یکی جلوی این کصکشو بگیره
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/84671" target="_blank">📅 20:29 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84670">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">وضعیت فرودگاه ریاض  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/84670" target="_blank">📅 20:23 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84669">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EF9SPTF8lc7ilEsTXTJB4vLtjH3cKC7dyx602Hx0297CHVEfRyzNxRgxE2n-SgpSvIHpYwXJNgWa6gmOqvTyS7o-lh0iVHlqQuqigwxLOHXsNjnJBupVNTSGI4fYcCu3ekVRvxHZc51oTyxiMqPvVn89zkxWuGPK-RRJibPNvp2MCse0zDdOqT20NQPvPZVCAxMazrpkHZ38FP0K2ARdwwUcXaL_TNALjW6w_xHe4keRf-Ru-3_Ti0RONt9dSy5vqzMBZufSHkCbVw5OfGXQuzi4heFT305krx-2WORe8P6Z8phe6rX1T_w6eQeM90Zn7G3FrRhptPB91yPXt4Y_Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت فرودگاه ریاض
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/84669" target="_blank">📅 20:22 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84668">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">شانس
0️⃣
0️⃣
1️⃣
میلیون تومانی خود را در بری بت از دست ندهید
🔥
😎</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/84668" target="_blank">📅 20:22 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84667">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xhs7hFyGMc1XISk6857o-IQW_F79wUFLt1iie6Rog02qMqjj4bdjcb3eSzgoCSvwua_tV2kG0j4IIQBDemc3yN7zaP4DAcgW3Qs1Gd6Zj1XquVIx-D084AmWJ5uNGkhwGpF3yRgQour6Xag3GH8LbcZYcsNDub5krcLdblHjnSMaDyAEhBvPs8O9EOMasymkIBXiFuYcSirpQvlq-3FsvyWflp0qnvEh9Q0l2H9aGPmV2AGC4USzqW-ZMLC2hudXDIXu7atVTw17qZQzf9c3pyCVbU31am_KLReoFFSNVC5C2EnXih1fGJKmxXg9eDz2iChtdhjIr-rqSSbQrijYmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
۱۰۰,۰۰۰,۰۰۰ تومان!
🎁
🫰
💰
فقط با یک ثبت‌نام ساده در
BerryBet
می‌تونی وارد این آفر بشی!
💰
✅
شرط رایگان دریافت کن
💯
کد طرح تشویقی:
888
💸
شانس برد تا
🔢
🔢
🔢
میلیون تومان
💸
🕔
همین حالا ثبت‌نام کن
G18
🅰
🛒
ورود به سایت
👇
✅
https://ieoruyxtsud.shop/fa/affiliates/?btag=914641_l303106
⚡️
کانال رسمی ما در تلگرام
👇
✅
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/84667" target="_blank">📅 20:22 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84665">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aae2137c8.mp4?token=AyTrHE_K1kK9Rqi6qIfVtt95XV06AZKAN_kJoQeKoMqfSdWOtOP2HN-ws8FZcKfz7SlOJDRb4Yk3xDjn7NXZyPS1lxqLF_D4F6UAO60a-TtotDucL54FpXceALdjLzzzM5_Hpd15GzcJKKsaRvAMR2rmdbSxVa7FO5f9Iyeydz3mF1xoX3pyoR2lDz6FqmIca3M8LQLX9BR2PtshYfGwgtjT0x2XORn9-Du912PIY25bQly5gsBTGQD_-E744HEx-nlBKVgJ6_iC4DuvJbpct_d1MmlnjtldQxEXpHiy8QuR8xgyNdC_8cJhFvT6EznwOUl28fC-0TGUzV34Jltfkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aae2137c8.mp4?token=AyTrHE_K1kK9Rqi6qIfVtt95XV06AZKAN_kJoQeKoMqfSdWOtOP2HN-ws8FZcKfz7SlOJDRb4Yk3xDjn7NXZyPS1lxqLF_D4F6UAO60a-TtotDucL54FpXceALdjLzzzM5_Hpd15GzcJKKsaRvAMR2rmdbSxVa7FO5f9Iyeydz3mF1xoX3pyoR2lDz6FqmIca3M8LQLX9BR2PtshYfGwgtjT0x2XORn9-Du912PIY25bQly5gsBTGQD_-E744HEx-nlBKVgJ6_iC4DuvJbpct_d1MmlnjtldQxEXpHiy8QuR8xgyNdC_8cJhFvT6EznwOUl28fC-0TGUzV34Jltfkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/84665" target="_blank">📅 20:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84664">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">امین تیجی جن زده شده.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/84664" target="_blank">📅 19:55 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84663">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">چرا حس میکنم هوا دلش میخواد سرد بشه ولی روش نمیشه</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/84663" target="_blank">📅 19:45 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84661">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VofaVgYUJUJOGTVdra_3qQB2zNLtysKNXadJMNeMOXlmJlpDxfQBcOWRiObZsn_kWzm_F8zZd3ic630wFRQJoqgElLq_XeCrEN2_Xxc0cHXldG31YirUQnvSEVz8j7H95fGvo9tpZ3DF2nOIu2I0zOgUosZck5WrYLIYrIwczeia3Sk1RawYahEoa_jBXGPLUruXm8pQ4O7YpRWYrjBPIr9x9iNzFqQspV7UM4d4YbQ17tx6gIew7Ap6YLvAHgDRk5dQulxxBitqRDhodtWDD0rqTIPmJQ8-WbX64JV2qiiKrIRkU7_cG2mRBiXUc8p_rLqJmjrWXX8nW_QAKo6-KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jGv4VHXfZ9j4Rz_oWHgbNxA7bxTQP9Q69-KN3APRt2cCIc3cy80doc2utDJNUzlCrUxQVyRP5_k2bHL_r_XzlvCDIJIP0vVR0w76Bim0l0aEXmFWyOri4A8-kGwWznOEeyOmsleMn_HBfGoxCc_8a76WSWffQQc6Ad7TPgTmr3lLo8zHSNvu1oCGlSAUPpAosNY3pBZN7Fq3s98NuXGXglchsj_E4PT4Ogzqq36ILqxjHohJ-hWjm7RSa9aVWY9C3OShU6NLMhI-7euhUhZ8LnEK2RajtPyKnnH882l6yKLsBkfZ9UQ1duWBD25cYNTSgVrfJdUrHqo29-KMrEwnMQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کریستیانو رونالدو موقتاً از تیم ملی پرتغال محروم شد!
فدراسیون فوتبال پرتغال بعد از جدایی جنجالی رونالدو از اردوی تیم ملی، تصمیم گرفته فعلاً این ستاره رو محروم کنه.
کمیته انضباطی هم رسماً پرونده رونالدو رو باز کرده و قراره به‌صورت فوری به این ماجرا رسیدگی کنه.
هنوز تصمیم نهایی درباره مدت محرومیت رونالدو گرفته نشده و مشخص نیست تا چه زمانی از حضور تو تیم ملی محرومه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/84661" target="_blank">📅 16:50 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84660">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">کاش آرتا و هیچکس یه فیت بدن، هم فنای آرتا کف و خون قاطی میکنن صدای اگزوز خاوری هیچکسو بشنون هم فنای هیچکس کصخلشون در میره صدای اوب دار آرتا رو گوش بدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/84660" target="_blank">📅 15:54 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84658">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/txPDKAFGMy1WGxNDH1RxZwhvOsoYHcJJOigsHt78yLuULNtBwB9srCi9gZ59nMuZEvIGIE5BLZMwKi4AzMDHiKi-QZbTiNOcwenaMxDksbFqIFdgYJJbv6_J8R13i93YexwzP0Qqw0CVUwPvAyJgDqChIGDi8CWGJ7KFU1EVxJ25UD2cDMgZTWV7xGbKH6G_d4cFMvuQtG_C4YM_rYRqdtXiUEh4TKhjeUEQgoCP9PZldELS7x84WDlywc-qGOQ8nqAtJ0MjLdqwIVFgkiNcg8B2BcPWYW0c6BTPax8DgCOsqTMFXYlgfxfisQ0kI3Rn5MKhpIC_PmintjT8hrUYUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iADADCeq23szt7PUQE8tHzjnv6eqGhHIGdWztH2kD3xStj3ecMlj7aSfXw5CRm9WbnGp_5s04LCfMXj7qWdGihImTBxibL6Cot2K8BH5rhWjUwNCb4aD9K8-NYo1unYmaDTVoztUOCOEA8spfcGGvL7hjHNL13-edmmF6EE-9GVPB0yQl769-y0BYgumVuTgzDl8Hpn4q1_vXSwCelO5nxFX4Ypw2J7YNmKe8K_hcBes1VeREBfgt1MkoaujHvzH-aG4b9phRYz2Q5okdsSKWq_kF4rJIpEf78eZPfrKeb-xG6lvBV8IZOu-AOvoSrG2AmSoP3C1_3n1R7PH1UUa-w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سوتیدا، ملکه تایلند برای نخستین بار پرواز انفرادی خود را با هدایت یک جنگنده گریپن در استان سورات تانی در جنوب این کشور با موفقیت انجام داد.
وی همچنین خلبان بوئینگ 737  هم می باشد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/84658" target="_blank">📅 13:59 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84657">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">حصین جان جوس ورد از اون دنیا هنوز داره آلبوم میده، این یاد کیریو بده کونکش پیر شدیم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/84657" target="_blank">📅 12:00 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84656">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">در این دوره از تاریخ که ما شاهد امپراتوری آمریکا در دنیا هستیم و دیگه بریتانیای کبیر و شوروی سابقی وجود نداره، هنوز عده ای وجود دارن که کلش آف کلنز بازی میکنن، منم جزو اون عده ام، کسی کلن فعال داره؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/84656" target="_blank">📅 11:40 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84655">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ترامپ:
ما گرینلند رو با قیمت مناسب به دست آوردیم: صفر دلار!
کصکش املاکی
😂
😂
😂
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/84655" target="_blank">📅 11:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84654">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fVzJNnjreID1oZuyhFZAwa_yrgp1tBmi4zRQM3NpRfAarTeZvNmappzH_8oz232G28V0oCUic8HukUk2DL4y-O1BNHbd7gHIpLYY4o-_AKXN7Xra3u4AjegEmsvlU-epakTExpx5803vfwPR2fuWAEy3QviBhjAySmdIeEHmDRQsz0gS4NzldKUorkHuh-o4Asx-UjD9Y4Pv3sY-zf2DNd0ay6sWmDrkQiqV0L3s6OT1-Ojc2xkq_S8Mnja2iw1E3kQ179252Lyu7HTnm0h8gbJ5yAH6A-dKsu3_lEZGRXa6RYEc65LYYh-i2QtPcgqfvizJ8mBRI0O2nubNwSUEYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من میدونم تا مدت ها قراره اکسپلورم با این تصاویر گاییده شه، فقط بگید چقدر طول میکشه، میخوام بدونم تا کی اینستارو باز نکنم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/84654" target="_blank">📅 11:12 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84653">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">همین حالا ثبت‌ نام کنید و از بونوس های جدید ما لذت ببرید
💵
🛍
👆</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/84653" target="_blank">📅 11:12 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84652">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gHDE6WEMEMW_KXKS2xlNYL3_3xAhygwUgyHSYwwS_zQxY_W_okYD49jGeTluxVd-MAuYegNn9lOZ_RSiK41MqTEO9tQpdGdPj4ls3fjlfJG92XzMrZR8rfaj2E5HXYpR-KvcPV7WmtMrj4Or3FJ5U3r7rvk_9oJbtHjONZSUqKZETWeJDQfKlmEe5ky-QRybUf-iLBJWJXrqz9pOab-Cvdyqta7dBt7ShUjLTdD-Wy94McfHLhjtWLcA2-XJW05xhbs9QvzvepaWypeWCtoXM4MvvKCkon9pp3c1FEpr6vjeehV7lLN-UCfsON_F5ay71w06adLSdkKsUl6hld8uSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡
بری بت | BerryBet
🔥
مسابقات امروز
👍
⚽️
چلسی  - بورنموث
🌎
ساعت ۱۷:۳۰
⚽️
منچستر یونایتد  - تاتنهام
🌎
ساعت ۲۰:۰۰
﻿
💸
ضرایب ویژه و رقابتی
⚡
پیش‌بینی سریع، تسویه آسان و پخش زنده مسابقات
🎯
همین حالا شانس خودت رو امتحان کن و هیجان فوتبال رو چند برابر کن!
✅
۱۰٪ شارژ بیشتر برای روش‌های رمزارز
🤙
ورود سریع | شارژ آنی | پشتیبانی ۲۴ ساعت
کانال سایت:
✅
https://t.me/BerryBetOfficial
آدرس سایت:
🅰
r18
🔗
https://yewirkxojf.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/84652" target="_blank">📅 11:12 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84651">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4795cf2815.mp4?token=BC893Ev_WCDD1AHvYClaUePZKE9m-BWGwTUrArSq4tb4_a091q27tK4OMv-7oysnrDatRd6b7MsYZn3XtBz_BfppU2LPh7VWHWZn2ZmdDcwKcOqGsj1mTkuHRgLXCTtHstIwaQVuCadoWRAQZatX-P3qF0qYvJg8lp7HafsT08ep4IlFGpqrBYA4JXO9gU3a3tcWE4yMrCVGIgbAA2Ve6EA4IjRZBf43ehyUM6zz4rfCMVnfJ_ix2wu5u_BlUexa4pkKJjtIaJP2WMYV6XISQdeIpwkJXbdIYqDS4xTy4q9DjNvx4t7zgylB8-fS-1TSjfAmlhHbMfEYkSlNCk_caA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4795cf2815.mp4?token=BC893Ev_WCDD1AHvYClaUePZKE9m-BWGwTUrArSq4tb4_a091q27tK4OMv-7oysnrDatRd6b7MsYZn3XtBz_BfppU2LPh7VWHWZn2ZmdDcwKcOqGsj1mTkuHRgLXCTtHstIwaQVuCadoWRAQZatX-P3qF0qYvJg8lp7HafsT08ep4IlFGpqrBYA4JXO9gU3a3tcWE4yMrCVGIgbAA2Ve6EA4IjRZBf43ehyUM6zz4rfCMVnfJ_ix2wu5u_BlUexa4pkKJjtIaJP2WMYV6XISQdeIpwkJXbdIYqDS4xTy4q9DjNvx4t7zgylB8-fS-1TSjfAmlhHbMfEYkSlNCk_caA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خداوکیلی ۵ سال پیش به یکی میگفتی پیشرو و هیچکس رو قراره یه روز کنار تهی و ۰۲۱کید و آرتا تو یه کنسرت ببینی فکر میکرد مواد زدی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/84651" target="_blank">📅 09:58 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84650">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/258be0442c.mp4?token=QlbGKq8HhNkih0OgbKbmIBEe2YAonkAqi78QHiDWdlyVCbCADmePNjDQJxQFoUrGodzyg8KB89ctFcLNaCt8l8Dejt7TbkLeGgGnwuaKdauWkXbk1OTAC1oLZsg3q6mY8d_nO-AED7GGka_ffZcPDRCluyXmQ_E6OrPzmRbRbQU9c_TElloA9ab9BAmtV-ciDN-LHhnI7G7tACJeY_0Ke7d0A9uzfXuDkAwlhb9qowiJn4wramo4N5D1AYzgU207BE3-45YaVikQyVbae2LYRlsn-1FgpehL6ADFFwx7GdeDKJaBeT1QgFVqZcUhoNxkaoHZEDQigql2A9WDYokqFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/258be0442c.mp4?token=QlbGKq8HhNkih0OgbKbmIBEe2YAonkAqi78QHiDWdlyVCbCADmePNjDQJxQFoUrGodzyg8KB89ctFcLNaCt8l8Dejt7TbkLeGgGnwuaKdauWkXbk1OTAC1oLZsg3q6mY8d_nO-AED7GGka_ffZcPDRCluyXmQ_E6OrPzmRbRbQU9c_TElloA9ab9BAmtV-ciDN-LHhnI7G7tACJeY_0Ke7d0A9uzfXuDkAwlhb9qowiJn4wramo4N5D1AYzgU207BE3-45YaVikQyVbae2LYRlsn-1FgpehL6ADFFwx7GdeDKJaBeT1QgFVqZcUhoNxkaoHZEDQigql2A9WDYokqFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درمورد جنگ ایران:
آنها یا همه چیز را به ما خواهند داد، یا دیگر وجود نخواهند داشت، آنها این را می‌دانند.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/84650" target="_blank">📅 05:06 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84649">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">تو تنگه بزن بزنه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/funhiphop/84649" target="_blank">📅 01:21 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84648">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">اوه اوه
روسیه تا ۷ اوریل سال ۲۰۲۷ توسط امریکا معافیت تحریمی گرفت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/funhiphop/84648" target="_blank">📅 00:09 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84647">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sg5ET29p5lZ0uycqwGIeQMY_QDlYodQAEJ73Ju6SImsyaMzZiwyEaTft1rosPdUT0UL40y95dU0AB6Uyb967S6Tuv8pqne1SsPt0GT4lBZ4cA2ZDQOK1MZh3Q2O4VHvnbbhqTXE5UKgkhmjWKl1L6hFaKJ7pl06BMtwosSDQ9-DbgZMJzgYLzTI_lQZUrcuq50ZN_LID3wL9ayAbdjaSB3jP1Jy4_5phx2mgn73usLPOKPgMzgnoTlcTnHBBmx7gLNWO6LrSNnGU58s6VbfjLrDBEFrmj3_f2_jtqU0ABA--pIUefdVjPzBybBWFfZKG3kxNbKhiksXx-3EgPDBKdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هی داره یکی بهشون اضافه میشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/funhiphop/84647" target="_blank">📅 23:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84646">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hP4lvf-tUfG4Hwl2JRiwhVzp5z3nHA82iIlvGNsWkRDWoOlB2P_vv5GRu_7KkLsBf9IYHIzmzamQvYA0mA6R38iUAAnTiT6t0oFXKIdVuW2XFskLUEwrvz6Joly63w2vhLC-70zjU2dYJOsoveF16Kx78ef7DJAxG9ByaLO0rZxK1rqPEiDbyBVS8wu6MYYh6JuYXWCAcPSxRZe3SS-UsyRMdg0J80kFewe6Aa414V-N_J6qkKzokoVeYcDizl8w4nGtOve0_SjK5v-bU-GO3yYCIXVkorieiYCjP2YJX_47pLo977yOsqj47cZU9dfLcoGqS5cANaclZzjGif4yCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان فعلا پست ندارم اینو داشته باشید تا بعد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/funhiphop/84646" target="_blank">📅 20:52 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84642">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DKfO2EicVTgoTUDNSgFtp-jxFlk4BWtA3bTVzz9cw2y0fdT2SPGiYA_6WOLjGR_iTo_W4HTYucnWqpl2EE-wpFAdZ3Y471NN2YwyHYvmIo94hVPlENdi9TUjslEYdaAuIV0E62qtPHwY4ML3kHLL_mWvRSnRxc98wBZTjvwkO3XqMMHyynC-EIZ_V2zpSn7T_MUTH1ZLRm3plyKBreuizlTocP_lsEwprOiZ0saFRUokYTJ580kivYQDQVjfukojlPC5BPFtkHdZjjk-BVEZ3XrNkpNeMIDShJxSibWWphntKs92OWu3THffEMqEJudEL5Wzbalhxrx2FlzKp-SYbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QsooKqZ5uM-Tp-rM-Vj8HE1caxj2wjZPlgUccWlrtdCnLQmhGOc4HFwEd1hniYdi77-LxIlApE48XXrTvLDp5rVBfKco5QOIHUDysGz0bjOnXxVsJ-ZNu7VwQyX8j9-uDS7Spjyuhw9gsm4qi-MXbYkW-Nxtu4jdCFPH4roZxDvfaEQfCyXDDh6cVqsLAXWvvhRewVBO3QuqiMQDd5NoBcLjF2TUrrn31s8F3X9CDBZx4QOK37hGl_vwLiU2VZ9tD27nKcMQcFqJtzLO2YpDPyOZwvzLouH1OlexoeHCwx4aDV_LkN8K9DRSVPgQBLzVBrTndgEH8eSK4A0R7EC1jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aKee7fvwkWV0t4jBYT5IUCEMoXSJWlvrgtHvBoPtcWvUZ79V0mbNC13MTNnmgjO9-yv4-205DTqlt7RbsiKwziZ_D55_h1XMcRECvwugb5wRZCkoYTVsgDG9EI8G8NwmXHFaYvKkjZnahxofSvtXmpoFHp2tL-vYzOmW-s-KEcZe6kJYXZld0wKx20pVKYYAn-uz4ucxdHG4KMjrrL9gQOT0O1OBgPTYuySDONvTCwfnnrNhAiildx4Jvn6UCUKHjlFw1LTYKwD0O6qpmPYvwfkhWorp0fL5Gtdv6VZy7s7jy2L2Hpij3n6eYYeGk3RfAki5nOyIjQhPJ5b2ssPyng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GkS5fw97nmcPOeDNoaoufug50rV5WHOMWVxVPOnWEbt--jCLvWqZuy5JLpcKGHPuFXax7ZbmiHRC-nNY62LzcocL2UlgDgrySekU204qZrbQGPmX24vBHfG5xsNnjqd-nKtCQxdQrCdKICIgeGTZjdMjpSdlVl50uVJDXLzGihRquEQGDYTorhqlUkaZ1_Xi6zsfFLMnz9NVHUdsJZqKzA7iQmBmYT_5evNuY6IZ5FGfQxShc2wkI2vj-C02fgEft9_AAM3FdJj0k0PPz-NrdhbPR-JiDe3yqfalXYHb4A2LyG6W13P3LSViohQPX-pB_JCxGEw89ag6bf9menh52A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">همزمان با ماه کامل بر فراز آرامگاه کوروش بزرگ، این اثر هنری زیبا خلق شد:
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/84642" target="_blank">📅 20:30 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84641">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gnVRN1jpPoGvWOsOQLvFQHnPUyeox3FtyuT_vmCGAjkmM-tzES-u3pP1JKLDJtrOAtfXWWoy_CMoGrP03Geo9zcVPj1xaR4pPqvubUviAAMkWJZZjmVtl5qJm4bERRp4ISvBQzX69kRyAEhnvXOaYvmayjOaoCCl9DxgxYL3bk1yEbScmVq8V9zXGELm9NnKIVP7iWD1_wju3NaROt-1dlqhJA7dEL61htzIgPon0tfFrrLXYepcOyNYaY_YYWAAneQ6mcAUFQscjtIFfAmPNuYEDX8-_STr5ok1nZFpcpVLp4n5DH7bvwJbohvk_wUrYRiC-fVi3C7ntpTGDxMzxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چجوری مصرفمون از خود افغانستان بالا تره؟
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/84641" target="_blank">📅 20:28 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84640">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lMOd1-ANQD2e54yqFWkMkkd8kAHIx1OXE8rmAD9v4B8Y9Nw970ZMNNAMqflmUNxdKXeWjrgv67wE8qmic8qQAQuvcVUCJ8W80jv1AMGzcnSd2HP9E8ik0IW8twRt9Ven3gxzq4e7keMoju5RmXHC8oKgPbq4PEXBwLsss6Magnp5F1XNJY4B3GTzIHOSEO-3vdFRuzk_iW6AQ5uqFwrZd9hnqXmYyUflJTamav9t8khtOGtuWlLk5s36LQoWid4eHPZhni_KTj9UrybK95gIM21yXG7Yu4SXQcbBA6-ddlIrrVb7sg3NMmjMDSEPjtttkCLOcQZxoyEwYkieNpTU6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
۱۰۰,۰۰۰,۰۰۰ تومان!
🎁
🫰
💰
فقط با یک ثبت‌نام ساده در
BerryBet
می‌تونی وارد این آفر بشی!
💰
✅
شرط رایگان دریافت کن
💯
کد طرح تشویقی:
888
💸
شانس برد تا
🔢
🔢
🔢
میلیون تومان
💸
🕔
همین حالا ثبت‌نام کن
G17
🅰
🛒
ورود به سایت
👇
✅
https://yewirkxojf.shop/fa/affiliates/?btag=914641_l303106
⚡️
کانال رسمی ما در تلگرام
👇
✅
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/84640" target="_blank">📅 20:28 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84639">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fx5ZKjVsHSMcqST-uYKhlD8kz6LZXHp-KKXNJRlxEy-gPILmkyDW_36yYZfTv7SXbkbrVNbVgTOJ-FhtS7JPINGucUGc_4c4Mz0fHM777bj8gDSkGXfzLtmY6jLJpoXeQgy3-qpnYmYCHiCQE7Gj4S_DhLSTtEeiDI-1EFz1JtGeqXkh1Ea8iZgWNIp5L3O0e0xhPwV9jBN8nCvQIVxJvXj8-8L3RB1lEeDTee0tLYdhVizbZOBmjzIpcsjlfIBt8_p7whxIrKN0hZc8iFxbF1bPmJaB0WJJ6tkAndOnsTc5DWQ25JMI-vDFKqD6uPTo_ZXszQJJP2nc6bYjeUGc8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدایا خودت رحم کن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/84639" target="_blank">📅 19:23 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84638">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GdEK6JfyTZj8A2dnPhOXH67kQ92VP6qdZAVOx75GTH9URefhLlUn0EjFKtlVbL1CiXpV8-H6Puov5GGt2CwzGIrp0DHlbh44YwLeWG8Qi9qHfNlPBWt49l9gcTslc0jpTA7D9XmkYSTIbU2tsQZv8YCPoxZ5zqZGputYqJ33-9pAux519wnFaM0_JDSZjQCqOXAW8D9boaUM8t1WV5fF2qTAvda4JBIWVZ-uS5lDQWt6Anhd0bghC0QTalQRN-mP7nV03zdY2VZyQ6Wj_eKdZxJKewj9RtE6z1LMbKMjkrmhzFcIcduTjUg1-l9VD10AuHn7UrhlJw9cESFw9TIsng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجیب ترین چیزی که امروز دیدم
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/84638" target="_blank">📅 19:11 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84637">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">دولت آمریکا در حال رایزنی با پاکستان و ترکیه برای بستن تمام مسیرهای زمینی ورود و خروج از ایرانه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/84637" target="_blank">📅 17:59 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84636">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">خدابنده‌لو چقد شبیه رودری بازی میکنه</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/84636" target="_blank">📅 17:42 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84635">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">گزارش‌های اولیه از کشته‌شدن معاون اجتماعی انتظامی استان در پی انفجار مین کنار جاده‌ای علیه خودروی نیروهای انتظامی در منطقه چشمه‌زیارت زاهدان حکایت دارد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/84635" target="_blank">📅 16:59 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84634">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">میرسلیم، عضو مجمع تشخیص مصلحت نظام : تیبا در سطح ماشینای معروف خارجیه و به راحتی می‌تونه باهاشون رقابت کنه.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/funhiphop/84634" target="_blank">📅 16:04 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84633">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/84633" target="_blank">📅 15:45 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84632">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">بچه‌ رضا پیشرو یک ماه دیر به دنیا میاد، ازش اجاره میگیره.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/funhiphop/84632" target="_blank">📅 14:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84631">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QfEYjVX3CE8qmdchwmY9Y2X0S2Vj6n-T_IN0F3Sn4vNtkMWSfQG-nxnr871d0ZzcWAhLq0MFzylX5NaJqvGTjGXE8BOm7G5TSv8_Jh68NK6dfkgiRUfip762m8F5CC0AwDo5GOpRuCZecHDpoq6cLPdwmp3nUa-CiDGj-0Ear3t1-XgJ5mZvWreoRJC282DvNRA2ZVbqaHeOycV4EMi63hvlJqQEw0mBDXgRqLMlFDTOVgB4c3taM7mazCokxfKWY76LAyt9U6B0epro4DEoJHK1YZz81jVprpwHCG9qijAzfVNCMwztr0Kuv75UtOFNOPrK4yslCloy8w7qObMFYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماشالا حاج اقا
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/funhiphop/84631" target="_blank">📅 13:17 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84630">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">سر همین اصلا به مشکل خوردن، پیشرو زنگ زده بود به هیچکس گفته بود داداش مالزی کنسرت دارم، هیچکس گفته بود خوش بگذره داداش</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/84630" target="_blank">📅 12:43 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84629">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">سر همین اصلا به مشکل خوردن، پیشرو زنگ زده بود به هیچکس گفته بود داداش مالزی کنسرت دارم، هیچکس گفته بود خوش بگذره داداش</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/84629" target="_blank">📅 12:39 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84628">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">من اینو صب دیدم سریع رد کردم گفتم ای آیه</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/84628" target="_blank">📅 12:36 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84627">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromᴀᴍɪɴ.</strong></div>
<div class="tg-text">من اینو صب دیدم سریع رد کردم گفتم ای آیه</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/84627" target="_blank">📅 12:35 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84626">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EA8G1CrgFZ6r2RUBbEEVohKyZCksubaxcv2Gb8Ykoj8XXVZzivR1GUt96kaMs-Ed5529VOgsYZhMDbAbTn4huOmr56D8t1Zf7gjmwKRQDKjMZAWlv8n_R4GYoRLAisDp-WmoiWgeidKvZXX6s-2962iISbZr87cNpxTVdJCx7ncOFg39cVjdRqttt_TuZx8NJjNaZ56FW5ENOD6P2fz-Gg4CaUgArvmtQpR_44G8woVGuPqvwZZXPFcpfMLlIEeqtN5tBrY_lJa9QkWjWqVi1ivuqZu0icrIgFkp2HfQuDoddH7QdcVhyu_5mFGoYxZ2QfGJQ_ZMvGWJYQDKHQ7imQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا فک کن فیت بدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/84626" target="_blank">📅 12:29 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84625">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">هالند و امباپه تعویض بشن بین سیتی و رئال جفتشون بهترین تیمای جهان میشن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/84625" target="_blank">📅 11:58 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84624">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WwzwD3Fua3Zo6GKq1MkXz0jUEwYPWPkfIWnqPuhnPX5sqqPC6lozz-y3uv2JEz9LpvAZEAnSmWXdfVW9N9eulkTzwVO8WO05gWXv_Ws6TY0P3x2wyD58XUUFzu6PtXza5V4Xr0rbg7XKMHvmzWsc0bnfAH-FFkvQO3BrZ1a-BuO9gU_lcfbvu3zRrNLBDLk8TzTO1zqy4ntZJXTlj2E2vkIdIT1pDvS0lOPwASshzLyrnf6cvT6e9sWShxOJ1hmiHGOSNlPL5Quxgs4Qjm5sMW63X7AZ9lk4qQnjW8qEgvzyPN6qlv1Ygv-jKv_qy5NOpQz29FRIyx7zoLmeuPu3ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس داستانای کیلیان دیکتاتور حقیقت داره پسر
آاس :
امباپه توی رئال هیچ رفیق صمیمی‌ای نداره و اون توی رختکن رئال احساس غریبه بودن میکنه. با بلینگهام بینشون یه جور تنش و سردی وجود داره، با وینیسیوس هم رفیق نیست و با بقیه بازیکنا هم رابطه‌شون بیشتر در حد کار و فوتبال حرفه‌ایه. حتی از بازیکنایی که قبلاً باهاشون صمیمی بود هم کم‌کم داره فاصله میگیره، کلا تو تیم کسی با امباپه حال نمیکنه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/84624" target="_blank">📅 11:31 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84623">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FzLU_Xz9ITLnFnMoot9OUKvrQBLKJyhG_CjQb3sRqBG9iBy-KSM1O6PmhwT9jNP_t9Ec0vQxau1pZC74RRfjmkqAVkXdYNaq1VzaZ2hnLcGMoAVzh2hGlemaMlT27ZDmaV9CkDOag9xBeDPtsegtpmPbwfaAbzUBDrWjie8k7nzK0e7E92d4zEoiPkF6DtNUWlhuOMO3thQKL-omP367Ov2VVwuaDqr9xTAIWl9DGxtaEV4V47bxSh_hIsRbj_NAjxkhK9uqHHIh695K0ht6oYq3ckslQyFw26FATzdE0UeRb21DDFM9EgbEUX1H45sCjN1FNyqnklNCeeqyPfQGHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مستند تک قسمته ۲ دقیقه ای(یک دقیقش تبلیغاته)
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/84623" target="_blank">📅 11:00 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84622">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">عراقچی پالس های مثبت از مذاکره با آمریکا داده، شیشه هاتونو ضربدری چسب بزنید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/84622" target="_blank">📅 10:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84621">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ویچرت؛ تحلیلگر معروف آمریکا در توییترش: اسرائیل دقیقا قبل از‌ انتخابات آمریکا به ایران حمله میکند. این پست رو‌ ذخیره کنید.
پ.ن: این یه بارم گفته بود آمریکا لحظات آخر جنگ ۴۰ روزه میخواسته به ایران بمب اتم بزنه که ایران میفهمه و مذاکره کردن رو میپذیره، قبل از شروع جنگ ۱۲ روزه ام میگفت دیر یا زود یه جنگی بین ایران و اسرائیل اتفاق میوفته
پ.ن۲: آیزنکوت رقیب نتانیاهو در انتخابات اسرائیل هم دقیقا همچین حرفی زده دیشب
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/84621" target="_blank">📅 10:20 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84620">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">من جای تهی بودم دیسای قدیمی پیشرو و هیچکس به هم دیگه رو جلوشون پلی میکردم و از واکنشاشون فیلم میگرفتم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/84620" target="_blank">📅 09:58 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84619">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dSWGbahzaC3XEAOkM3y-Dp0mwk53hWClrXLnyNaLwZmHxAw_dIi9d4tpqzRjX9_nR1RZ4uzE05BPEQBjdnet9RT5_yB6L8PMcIJS0yuZqV5z_P9bjWvTiWjKSMTje7Udyv2J94Zgt8DTz020lIm66HA64pj6xAtTy4VUMpahOmpIyMSuQzvjK-I6GrYNffwUt57nfxNWJTq3zkFL7JYsHzfec82neoOd5aQoRU7HlHmvG2wXKXm002JCYSieWUeCJ11BewX4E4enD8y1wo4uxntw4r9O-MN8z8ZU_vZPWOgCMd4CN3VZ4jkhlKv6UjbPqM57qOe84R_5lnxnDdXuew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یعنی کیر تو روزی که با این تصویر شروع شه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/84619" target="_blank">📅 09:48 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84618">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">همین حالا ثبت‌ نام کنید و از بونوس های جدید ما لذت ببرید
💵
🛍
👆</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/84618" target="_blank">📅 09:48 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84617">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wg5nove5FSoCnjKuduPvKXci6jDJtUyoVd3CaLZ6_Ew4Dton0NfwT0cRgmjDEJM7TSxRvBvc3j-A6tvLYIS1R3k5EjmWi41xhwvvGHlLjNEhpLWs92cv3xO5PjgqsqdBME1TD4fbXlqooBR8S41ChR_ssR3K5htKSO8mZWI-sn_nuelZ_qMQs_iicxdvyEXXlQRE_vy3ZDWUS_NuGFju68O8dOUJDf3JKXyI5EJpS9pEkf45PXXWTfao2MYo1JFdZxiZw9yPkdRNqp_4cGUePAZWjKHUiEum6dcJw_OoHGItWzETDHPXMqnwvXM97ltnxKdWtREYxCQLut5qMrRTJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡
بری بت | BerryBet
🔥
مسابقات امروز
👍
⚽️
پرسپولیس - صنعت نفت ابادان
🌎
ساعت 17:00
⚽️
چادرملو اردکان  - خیبر خرم‌آباد
🌎
ساعت 16:45
﻿
💸
ضرایب ویژه و رقابتی
⚡
پیش‌بینی سریع، تسویه آسان و پخش زنده مسابقات
🎯
همین حالا شانس خودت رو امتحان کن و هیجان فوتبال رو چند برابر کن!
✅
۱۰٪ شارژ بیشتر برای روش‌های رمزارز
🤙
ورود سریع | شارژ آنی | پشتیبانی ۲۴ ساعت
کانال سایت:
✅
https://t.me/BerryBetOfficial
آدرس سایت:
🅰
r17
🔗
https://yewirkxojf.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/funhiphop/84617" target="_blank">📅 09:48 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84616">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a66d8a6ead.mp4?token=L16xpczr3k5QKTmJUB2YIjjI0_02cyw2gw2FEzyqip6C8ZqadRW5tKvGxzDb1DMzKqnKw2aXWpBVPFscZnNNxGdmglmkRZJow3gK-alpQ_tPlL6dPQcKLHQ6gLU487XaHkLJn0-sz8cQpAmUfACrf5Snvnv8-ZsKawQQ44oQiCzAbJdcoxu4fKDow8g2LaM1xQZ9zd0x-gmBVnj55gIK8KqFdxSvXqGlgnC0ko0gq38bQu4E05FrIihWHjtzj_jAgr8ReeQsXA6-LUQTAJC8IMxJtBCUwlmfMdEu8_D4ijUXGPuuoM9jh1hMYdLUrirjb3_vhLf3aM5a6o1V12bJjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a66d8a6ead.mp4?token=L16xpczr3k5QKTmJUB2YIjjI0_02cyw2gw2FEzyqip6C8ZqadRW5tKvGxzDb1DMzKqnKw2aXWpBVPFscZnNNxGdmglmkRZJow3gK-alpQ_tPlL6dPQcKLHQ6gLU487XaHkLJn0-sz8cQpAmUfACrf5Snvnv8-ZsKawQQ44oQiCzAbJdcoxu4fKDow8g2LaM1xQZ9zd0x-gmBVnj55gIK8KqFdxSvXqGlgnC0ko0gq38bQu4E05FrIihWHjtzj_jAgr8ReeQsXA6-LUQTAJC8IMxJtBCUwlmfMdEu8_D4ijUXGPuuoM9jh1hMYdLUrirjb3_vhLf3aM5a6o1V12bJjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیشرو و تهی رفتن لندن که سروش هیچکس رو از نزدیک زیارت کنن.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/funhiphop/84616" target="_blank">📅 02:43 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84615">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ml2MjqC1RlxiLbzn4Q_NOp909CovoEEsGxPNTQFawU_0FwnuzNIzyScNUDfCqprKSXbJTW03nZVIuj9MDXxRRwJgquDz4mgzTVfzbt2J7V6ol9sw-NJ0QqxcYI4HvPqU1AGBJ5pDx0d_Iv23TGPhhdpdlUmfMeLK7Bd_U_u35uhNxlel9sMFBHhwzTjMiz22tHj6SVGwg-bGmuRLewYoAVjD7DksvCSsprmatS82ex1t5FPhsmF3tZvey0Ubzc8UIGU4Ovq_8rcRb0BCp9yAbX8eZX_04YNJDUpbqpYQuXYh0UMndtGqOkykbgOWtbKwqM0VWvqMP7AC-Vorj_KxPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنوز شیوع طاعون تایید نشده؛ تو ایران شروع کردن ماسکش رو میفروشن.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/funhiphop/84615" target="_blank">📅 00:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84614">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">سپاه به اربیل عراق حمله کرد، احتمالا هدف مقر کرد ها بوده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/funhiphop/84614" target="_blank">📅 23:36 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84613">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">اجرای جدید هیپهاپولوژیست
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/funhiphop/84613" target="_blank">📅 22:53 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84612">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d16fa565c7.mp4?token=QDCZPW90sqqKsgUQ948Kgwl6lxPLhdjGSS3sxIRPAxckOKFYJBLwcC0hL2o6-odlqWje5rzJlPXXNWtcC4HTxP9px9xMdMuT220z_j_4Z-TWvxfOO2NxMcvWdjkG3BbkCu99xDKsgGayoEsnNk_i5t3BmqJDXoOA6ELpkDuwAobKI2w__cjELpgUe8XigU--8wfWER7BxpBplphd4VUBk25DCZZdjmfq2yVFST7Sh_88QLTl_c1FfVYCOCJn_tu9jz9Qj7wnMcSf2sq60CYfK6kichWb4F36qf-JQ-pFoEes2s2sMkVwiUwhue8w9fQwnjgnWVaWYINfUWaENd5aGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d16fa565c7.mp4?token=QDCZPW90sqqKsgUQ948Kgwl6lxPLhdjGSS3sxIRPAxckOKFYJBLwcC0hL2o6-odlqWje5rzJlPXXNWtcC4HTxP9px9xMdMuT220z_j_4Z-TWvxfOO2NxMcvWdjkG3BbkCu99xDKsgGayoEsnNk_i5t3BmqJDXoOA6ELpkDuwAobKI2w__cjELpgUe8XigU--8wfWER7BxpBplphd4VUBk25DCZZdjmfq2yVFST7Sh_88QLTl_c1FfVYCOCJn_tu9jz9Qj7wnMcSf2sq60CYfK6kichWb4F36qf-JQ-pFoEes2s2sMkVwiUwhue8w9fQwnjgnWVaWYINfUWaENd5aGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوجی انانوبی بازیکن بسکتبال+۲۱۰ سانتی نیویورک نیکس رفته دایرکت یه دختر ۱۲۰ سانتی و میگه بیا ببرمت نیویورک.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/funhiphop/84612" target="_blank">📅 22:14 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84611">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49025c86d2.mp4?token=L4CZz-_64Vgl5GWvtjf0YmtwZQ0fUSqTz26Ll1eDJijg_Vc3rmeeDk4ojaUG5rozimKGIEgR8YbxLWlQxv3ecHDhQhjNr8XkeAGH-Nb4S__06ToZ5cnGZxKCp3rf2FDV9O9PjFEonDA4UhTPaFvL2Cl-mJIaP2hDTYNpXfZBwEp6tHHyov6Dd7iXYXYDTUoXTfVz-CB6JZeAadBXgJOzDemWy7skBdzOPTEChl3qf7TR1MKVTKSyN0WKycZDw8DEbXmDwhANqTCFri8bn-miXRtLPsl-syGmKdFlOHciKeYk0lJYzfy0Lylt9JCWqzqGImuN0E4d7SzvdcZnfyG4aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49025c86d2.mp4?token=L4CZz-_64Vgl5GWvtjf0YmtwZQ0fUSqTz26Ll1eDJijg_Vc3rmeeDk4ojaUG5rozimKGIEgR8YbxLWlQxv3ecHDhQhjNr8XkeAGH-Nb4S__06ToZ5cnGZxKCp3rf2FDV9O9PjFEonDA4UhTPaFvL2Cl-mJIaP2hDTYNpXfZBwEp6tHHyov6Dd7iXYXYDTUoXTfVz-CB6JZeAadBXgJOzDemWy7skBdzOPTEChl3qf7TR1MKVTKSyN0WKycZDw8DEbXmDwhANqTCFri8bn-miXRtLPsl-syGmKdFlOHciKeYk0lJYzfy0Lylt9JCWqzqGImuN0E4d7SzvdcZnfyG4aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرقت غذا تو یکی از فست فودی های کشور:
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/funhiphop/84611" target="_blank">📅 21:49 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84610">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f08a78a31e.mp4?token=s-YmtWDtxU2-ufoUBQs7Uap2hZVHdSK7eBeI2GsaDZHIx6DfiyACOhO8u2eTcdUNzCYOTp542jjmIfCri_xW9dY36Ru1CjUr5KEGHct2u4XUYzOLehnoUR6yXN8Mou8hHLSoE6uEaX7Kf5DgYVf-pwzNBQ2BM4bAXQuWDgraaAHRbp1GTJJIEu8kkcncFBHoRBlQqYr22OcEaGwKplqp7yKKIxwzFh5KBQlOm-wDAhbU_NrR-V6P5yUNx5-U9IOr3JZFz5sO_oGL69Ahrg11qi3aQsuUeMjkjKPnyE7mf5_ZQdnOa7Z9QErZN6lvT6K5p2KFS_CDXggKMOHrP7u4eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f08a78a31e.mp4?token=s-YmtWDtxU2-ufoUBQs7Uap2hZVHdSK7eBeI2GsaDZHIx6DfiyACOhO8u2eTcdUNzCYOTp542jjmIfCri_xW9dY36Ru1CjUr5KEGHct2u4XUYzOLehnoUR6yXN8Mou8hHLSoE6uEaX7Kf5DgYVf-pwzNBQ2BM4bAXQuWDgraaAHRbp1GTJJIEu8kkcncFBHoRBlQqYr22OcEaGwKplqp7yKKIxwzFh5KBQlOm-wDAhbU_NrR-V6P5yUNx5-U9IOr3JZFz5sO_oGL69Ahrg11qi3aQsuUeMjkjKPnyE7mf5_ZQdnOa7Z9QErZN6lvT6K5p2KFS_CDXggKMOHrP7u4eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من هیچ کاری به این که رئیس بانک مرکزی ایران به وزیر خزانه داری آمریکا سه روز وقت میده و این که دقیقا برای چی وقت میده ندارم.
ولی چرا میگه ۳ روز بعد با دست ۴ نشون میده؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/funhiphop/84610" target="_blank">📅 21:36 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84609">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d8dc7bfe.mp4?token=pVwr-fmr2EFrIilaauU1epkdLpx82VgiCdgMnI7aDYDzP_7iAub8riHSogDN7BocrQCtDgYXqxiYkc10Kr3WuhvKl7-pX46HjfOrqskiJCuBNEszB7Ua-3WaIe7yIaBcSrJCXoBpmCA0CYrUpEB4A-wI3eAr_h8e8jb7mZOaqeyPKTFCQT9ieXifySiBVseddoG3zHsyN-dKpry6_1JSndsWzCJWsIfXYQkgyhQcxEC6dPLfd3FnE04L0UCL22z7jjf3a9ucOsme8dEBJ1ago0J9s59k6DEu6SlEdT85msKpb_NN9xaLbuxqjc3laGKcJsRU0a6GDAHvSB2Z5SJWJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d8dc7bfe.mp4?token=pVwr-fmr2EFrIilaauU1epkdLpx82VgiCdgMnI7aDYDzP_7iAub8riHSogDN7BocrQCtDgYXqxiYkc10Kr3WuhvKl7-pX46HjfOrqskiJCuBNEszB7Ua-3WaIe7yIaBcSrJCXoBpmCA0CYrUpEB4A-wI3eAr_h8e8jb7mZOaqeyPKTFCQT9ieXifySiBVseddoG3zHsyN-dKpry6_1JSndsWzCJWsIfXYQkgyhQcxEC6dPLfd3FnE04L0UCL22z7jjf3a9ucOsme8dEBJ1ago0J9s59k6DEu6SlEdT85msKpb_NN9xaLbuxqjc3laGKcJsRU0a6GDAHvSB2Z5SJWJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با اعلام رسمی سخنگوی قوه قضائیه، بی‌حجابی رسما جرم اعلام شد.
از این به بعد در سراسر کشور، با خانم‌های بی‌حجاب برخورد و براشون جرم ثبت میشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/funhiphop/84609" target="_blank">📅 20:52 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84607">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ibHJFvRgJ9IWqN5SlPO1mFIyFdCReo7z313RtQZksGdopAuy93IPiMZ-A4lkXh_IbCzsZzsS0mtvYcb2zQjLWRFqrq9-uBfaWU3R7FM1u5DxSeAY5JZmbQCCosmhEU23s7vV1YNqQ21oMu3UsaBVvfWXBgPeG8ojjFTtP2DXhdQ_Asud4Lf79kcpxxr2JiAfsLBIACvsAf2QtR_Phu1UflIdG0IzhK7TbGHQASAo0bSwd_HYurVNNBAp4sYIRCB2tEvLhGMrM1_yw4opRQPXy67jP_Hwp1tM7QDQ3LerD324YIpFS9aHuqkKI52sBKcvdKJ0CPZwk_P6MxkJQeQBHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین الان پاشید یه جوری شیشه‌هاتون رو چسب بزنید که ذخایر چسب کشور تموم شه.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/84607" target="_blank">📅 20:27 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84606">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EVB-9q70CeJ0MxccZ09U4XGBGR0gS5m3KV9z9Y1GCBK6ta-Z2Mcobo1TZL7PAkB2I8JqzXQ3OLWnAcQ2eV64R0Htvfaj4Qga0M1p4kEIxpgs_0hy6HPwg3f4HXRLBR9NKu9f7ENO-vSBaMzyE8MFY1FP4OGeXB8DOtNw2gVsce28qGxR8qcBThs_qH3pXrMmJ25RAqMHhgsU1BrglDMx5ZVSZcsYmIMas9f9ULOScz5efyOv2oLzou87o_S1HiJ7dVGyHvLa1rvHL-28hUPH9iTvCMeXbbRJdKtYK9SuAzfcoWMo_M2Hw2sqi9GJ4zMO9sAc9nfLP_GWm6MulPlE8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خخخ
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/84606" target="_blank">📅 20:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84604">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r5qcdJalvsMrVJztqOJfgMz3kDSasrGFhrzRYiBBOdc9xxP1wLG0NZnAtZ6FBhJTZgcJY9pvQ9fjMPZSLe7rtSYwUl2RSpbDiCy5DadsNMDh3czxHahzKNIj5FHAkI9qq-Id3mEW5PZXY3d_eSNtCSx67HAiGJH-hi7bh6h_uiwvnKR932jhQHeMMvK_ZbQ5iwTqahZjZ9o4vfwFgclQ9dkcsEoXNLsSHUKrGFCeGu_WoXzCMi9ePXpwtKfkP9jCCktg_FtKVGWzOdcdfZ5WmCGHjqPq8c2OehHUB8btQQDjshdeChefCGImc1d2Udr42wvwDJwifUOQXMjpegd1xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توماج صالحی با رپر بسیجی‌ای که شبا تو تجمعات اجرا می‌کنه درگیر شده.
(به نظرم رپره داره حق پسر ایرانمون رو می‌خوره
💔
)
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/84604" target="_blank">📅 19:44 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84602">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50ebbea01a.mp4?token=m1Pma6D8XIYzaiGC1wQ2frQtRdnwf7-lBRbRNj6Pgf9R0jNnzlQNgg8_pIm-g6y6fo708usWqRfzulFc3D3UzMEFpg32Vbgl3BhYAfcpEK86xIfNeYlpFfW7ocNADAqRzlf4A7LzRF8t6GevFFd0mRQD269vThRyEdCl_kh4T6xpa2Ed841d3sJh1oIOw32xLMkc32D_TdaQlPK9XK5yiUwkUb-Uc4dZTylSub6xzSLV1dVtR8xUrGp_3fiIMvdUiBAp6u3RwZLLpwhDjyC03AKViLOpco0Fqks-bQRTePU_huT38n46du85iX42WE15QCo5LHM31jS4Bl4JkWyZBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50ebbea01a.mp4?token=m1Pma6D8XIYzaiGC1wQ2frQtRdnwf7-lBRbRNj6Pgf9R0jNnzlQNgg8_pIm-g6y6fo708usWqRfzulFc3D3UzMEFpg32Vbgl3BhYAfcpEK86xIfNeYlpFfW7ocNADAqRzlf4A7LzRF8t6GevFFd0mRQD269vThRyEdCl_kh4T6xpa2Ed841d3sJh1oIOw32xLMkc32D_TdaQlPK9XK5yiUwkUb-Uc4dZTylSub6xzSLV1dVtR8xUrGp_3fiIMvdUiBAp6u3RwZLLpwhDjyC03AKViLOpco0Fqks-bQRTePU_huT38n46du85iX42WE15QCo5LHM31jS4Bl4JkWyZBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی رشت رعد و برق جوری میخوره به دکل برق فشار قوی انگار که زدن
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/84602" target="_blank">📅 19:28 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84601">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">با اعلام رسمی سخنگوی قوه قضائیه، بی‌حجابی رسما جرم اعلام شد!
از این به بعد در سراسر کشور، با خانمای بی‌حجاب برخورد و براشون جرم ثبت میشه.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/84601" target="_blank">📅 18:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84600">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">هوا الان یجوریه که همه تو خیابون فکر میکنن شخصیت اصلی داستانن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/funhiphop/84600" target="_blank">📅 17:43 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84599">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">حالا من که میگم استقلال یکی زده به تراکتور، ولی ناموسا فوتبال ایران دیدن نداره</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/funhiphop/84599" target="_blank">📅 17:37 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84597">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">محسن زنگنه: قراره 110 هکتار از چابهار رو بدیم به مردم افغانستان تا بتونن یه سرزمین متعلق به خودشون داشته باشن.  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/funhiphop/84597" target="_blank">📅 16:46 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84596">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">محسن زنگنه: قراره 110 هکتار از چابهار رو بدیم به مردم افغانستان تا بتونن یه سرزمین متعلق به خودشون داشته باشن.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/84596" target="_blank">📅 16:43 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84595">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bUouKYkIIvdR25KxvVZKq9DNrBYiXuGurxg27WMQ4zhFDHUa3PIEZAZUCtT3Py4YxvS8s3HD70RdGF6Cu5ixvuaVX1SI3vYtxWc47r9BgMweDxk_UH8BWcQg9KAzDYBp2D-_HOK8IEQce6Jp-jgRDkt2TC0BBaDtBDe-GIXyPUrWnQ1ZbaJsRgYxCrOl-ira3A0zHH3bPBhP39ipCU9gvBZ_DuOPzxnqcSIZxqwHss5q5N04MmjXBSOsdwmxeWV6LQuFxs_B8U0fl178dB218a1P0PsQwOCmLRyIY2_nu4TFhurb_UDFc5sMSyHQug6KKkd2RJzhxUjUq5mMLNgDVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر دلو فوت کرده
خدابیامرزه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/84595" target="_blank">📅 15:29 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84593">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XtRWo0Fv1zO8ABpE97uASOwV4uUTXN3TDWuldcRyANNopWQFjhXd8aUc2fSDibbJTJFHg7THDMk3VDaBJyUVv0ajGlqEXUGSbokZxBg5hzaB6ctex9SEO2uSyNlKlpUq98ypECICOBakDVL2hAtH8W4DGnTnuhgICYfmPkPluilE0pZVQovFGxMgQ7l5r_iTuVxxHQUZVAIgGS_pPat03bQ7aeA6P8_liZDZeUB4n4ycKVOPrnPcLpguZS-xBoUbqneNkaA1n1i7GLFhFY_vFPGMReiECCBLQau086H8Fh8iNvDDik6LfvsaSgqOMkg9cATKk_o87tSDang22wOyHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YKSOfN7ImfV0-3CKNv94kcxZSQqhCrxNbAur1jJDX-CwTXOI20Pg34-V1UxUTB1nmcT0x_cNwG4bRvI1lWa5QIawNagSdFvHh8o-1dmMR460dBvAo0eZIG9g3rwJMqH0nkvxrGbEjAQWnL45Xolh2aC7s2LF7Wgi9YcMxcWI4nHi6170dgvO4b0uxeUkRXLkjeEqliRQilYrvTuB6iaLftWhEvcSRIStYCEqaun0YeT2E3rsHtbUmlQYL9XEj4yxZjJNMugU1z0UwZynC9_nOf956jNY6b1XpFWx1BfOZvDvn88iJckN2m8Hqst9GF5ydcZw-CUp8X_XrOjXaO3HHg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مشتی ریدی که
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/84593" target="_blank">📅 15:22 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84592">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">مجری صداوسیما:
گاو که دلار نمی‌خورد، پس چرا شیر گران می‌شود؟
کارشناس:
اتفاقاً گاوها هم دلار می‌خورند
عالیه پسر
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/84592" target="_blank">📅 15:10 · 16 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
