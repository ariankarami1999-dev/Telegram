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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-20 04:57:01</div>
<hr>

<div class="tg-post" id="msg-84713">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">روسیه حرف ترامپو به چپشم نگرفت و به نیروگاه برق خارکیف اوکراین حمله کرد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/funhiphop/84713" target="_blank">📅 01:31 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84712">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">به رضا پیشرو ميگن: از مسافرت برامون چی آوردی؟ ميگه: تشريف.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/funhiphop/84712" target="_blank">📅 01:08 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84711">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">بچه‌ رضا پیشرو یک ماه دیر به دنیا میاد، ازش اجاره میگیره.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/funhiphop/84711" target="_blank">📅 00:45 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84710">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">دسسسسسخوش و کیرخر.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/84710" target="_blank">📅 23:31 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84709">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HBs0P6QchLxX-yL8sbRYCIRfg2v39NI1uynfrzxtL-5tW1TIh85WjmiCFjVh1U0odLGRTWVD5Ovyl4Eou2ZTCdHZBWOaikbh7DhsWvwJmCqh35M6hWyMUBIC0npeuvU1GQ2qN6KnoSZHV3bUTTv5Ah_NF1aalB3yiIw6ryAYV6rRJsh-YWC1SabLeseVJOuLfc4lyF8LOEQHRlchbzwstNbG9FweN7VikE0hLXxiifL0RqPMDnsLtuXEUUZFgTG75pvlL9F2dyqLkm1snxDYJHj987XewsdmUOZKpaluCoTKhr8-PTZ7bbjW6pohKv4i0wg58HOMs6xzyHhiwuWy8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان First blood از اینجا اومد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/84709" target="_blank">📅 23:04 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84708">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">تا دیروز هر روز صبح میرفتم سایت چک میکردم بلیط بازی بارسا و گالاتا رو بخرم یه امروز چک نکردم کسکشا تصمیم گرفتن بفروشن و تموم شده</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/84708" target="_blank">📅 21:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84707">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">تا دیروز هر روز صبح میرفتم سایت چک میکردم بلیط بازی بارسا و گالاتا رو بخرم یه امروز چک نکردم کسکشا تصمیم گرفتن بفروشن و تموم شده</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/84707" target="_blank">📅 21:11 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84706">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">خاطرات وینی پرایم داره برا ارائوخو زنده میشه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/84706" target="_blank">📅 20:30 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84705">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">دوکو خداسسسسسسسسس</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/84705" target="_blank">📅 20:26 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84704">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aNg07j-SV424XMO2xnrX0tGVkKUgR0U9DZ2m0XLEIQ8yzaD-n2CpJ5RRYIljx3_4tm3NtLMqgjXTwxyio4YaBuKhX0q_8lsJdKEjBAY7Fvow70m7ALrwpzG68VhslutL0MJs1wSClt2iWOvvzdO_j7Tw0_w6NhsZ2XtFPm07iGF68yUrpHtb6MNnox4cfYznUTs9q73oARA44V-k0MFs8s0LpCNMC4Wwm3NLP4ckqSbcdewvFlxlSa0YrkbedwQuYbrOVCa4skt14VU2j_gc9vYXkZlnOE8xNi6zYub5bGGApDOYKyxhUJ7oHuSYNRHqMUmkRr7w0YzdE-2-w-DzVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چه سخنان شگفتی به زبان  می‌رانی، ای مرد؟
❌
چی کصشر میگی کصخل
✅
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/84704" target="_blank">📅 20:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84703">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/84703" target="_blank">📅 20:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84702">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AmGffRPiTIbK32aWcNr1Ddsx2SHGf2sy82cEaC5DMOvb0iwgUspT6mxjaocQlwrTDZLoKY7YcrmP98P0UhOxNKYr5Pj_-pCh92gQUx0Iqw0Jo7hrh_EFOY-8mr2n4J97XvSvqNFiwzOsBGGLqLPW0vaO9GLi8dGD_WLGVxLzG-yD9MEJOG4aM-1FDUP_uH3z8Q557YQxu-rhDUKfp1bFiOZk5-HRd35HEg8h4p6Z1vk53wRztJXE3ykAa8rl1duwvjYFx4k4tgCbYJ-ykkpbLIL-zNGH3hSG90aS395FHFwZUfGGRVFNXG8aIcyRHgq6--1TeQsVBYxTf5ht8u19AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو بابلسر ی کافه افتتاح شده که با پستونک به مشتریا نوشیدنی میده :
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/84702" target="_blank">📅 19:24 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84700">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lL7YXPi74JAG1zMrIkgg5zLWSRHw_560dq1KkGX7fbCBRE5X5mzi-4ro6cKwebtaDx7CLWvxYs3g_MDlK55u21IgIx8TEIq3B0kXQ0IqohHo4FrJSK0_s7bwaozyD8zKUvAJjdLeVkRiL4S0mFOXIlYBRp3uLRr6LLmU4IFjFclxmlHBz1VostTR501BYPsaeuH5UudF4XoARpX30n9fO-x_1AgGPbUiL7czYyIjlQKxXzpzXdcywT3aXRNDho5u0OC3ZAZ290migKZwSycoCWloZ013_Ronyirba3tmJ9yjSUbBROoJTEN9GrgF8RJMSRJ3XZKAAULk8A7YTF3T2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا به طرفدارا لیورپول صبر بده، حضرت ایوب هم نمیتونست همزمان مونیوز و بارکولا رو تحمل کنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/84700" target="_blank">📅 18:04 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84699">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kdOJk-ZFX6wqvv24ufwgC7DSY4-IFiLF_BOdgcinOs9AQ4nOZbLppti4CNTNOwBrRTXJsmHUJzxnr_fw-U3qG6RrGsUQG3hgFP-jajH2KI6Hi_tWL40_6KgNAC4d8i7T_CzvXuhcSuInTIrK6tqW0-vblrPlpWa2OPj__LtPuTLlANKeWVHF_XkYHe0M1YnZtKzE7rw_US5xb_QfnZiXuKj3iKkuvpUy13hKh3dZNNQauuaTcuREnZbtyB1RRmpmzHZ-nSPgkJR-p64_IjPk_mTe39F7_P5PEwPgl0cwkipvFA-uJ-NgQu8orFZKjvGAfTRDkGwp-atvftj4viz7zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسیری که گل‌گهر برای رسیدن به بحرین رفته:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/84699" target="_blank">📅 16:50 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84698">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/84698" target="_blank">📅 16:29 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84697">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">دختر خانومای گل، روزتون مبارک.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/84697" target="_blank">📅 16:03 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84696">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NRvVFJiOxBDM0ayAFgPTL0_0AY6Ndk6_dW6VYqIFnjvdRKqMUE_4CO2rj_DzBwe775q2LiAmAQBYeDsBoPNjtVD0_tRmZL9TjaROcni8NrKAmDcwVgIWXSCnMGAcqpBStfRS009-qFDbyYtpzYG154uZID2YHElBSmb6GQHHvncgqhmGrXmvCHIyGrFpd2MFB-YtA88lR5-Cnl7fTBDgBCDHUkhDISoDOudocMsnpLLyXyc1P3TJGriPRj8xyQ-bv_hcf597EE1qrFj9SN9eEaHy8wMoJVUU8HB6K98j6AlgcQGv0oqqBmuPHwXqD5jlGDyBYSIFTpuxmdfpDEum_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گراز پدرته کصکش، حرف دهنتو بفهم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/84696" target="_blank">📅 15:44 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84694">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JAyzh6NaUdRrwRYCWwuHVWGbbNWrPQZMDaXzMObiJRakzd8pTGqUTAqotLYaOx3bH4JT-lcxsrhUdcNd0oqK8mr8z-Tom3dpsB8WYFffc4Q9v5t5e7k2VL-SAjBRYtRP72O44JYITYXjeVhNfYJ_kIzJvaoKYq_i7q4wUn4YDJteg2XHu9Xr1ocHAAI-5qaKj8ZNtRyuNsrcm6FN_Y0QiF1qYL6Q8-XuEDu1RVokDXwiqRwxEx0wcGTgpwJvQ8WPnAbq0ZF10cMF0ZUxc8F72XzPRecncj12xO4JotGcGfDm0dh45e6ZRVewGWQgIMtH-UiiKxLahKbYHApYK31KHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منم یه سری رفتم موزه همینجوری تابلو راهنما رو با یه شاهکار هنری اشتباه گرفته بودم دیگه نرفتم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/84694" target="_blank">📅 14:15 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84693">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">زلنسکی:
اوکراین آماده است تا حملات خود به پالایشگاه‌های نفت روسیه را متوقف کند، اگر روسیه نیز حملات خود به زیرساخت‌های انرژی ما را متوقف کند.
پ.ن: این ترامپ لامصب چیه که از یه راست افراطی مخالف مذاکره که کشورشو به کام جنگ با یه ابرقدرت کشونده همچین آدمی ساخته
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/84693" target="_blank">📅 14:01 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84692">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/84692" target="_blank">📅 13:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84691">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vXrhoQt48uBZQRVcdMhtYDvd_KCaquVOcSseJ2aoaDCeasKAKxdPZx2x3wP-kgaLYJdFMaEscRYuYvrTNwikf-rJYUz5T3-JZ8WWOrXw-yanLqdLd240Xus7lOFa163XoDvDETCH_oalxJ1uJRyhGmz0-0bKJPRaqEbwcmPT5lWvNGJb-Jm5mwh2SoY9lQqJuR-kxPrTadb9FKpQx-qHFHTuP6F9q0kA4hLqJ8ys1NWOlMlijJfBEnmAUIVDePv7P4kPoYR9RKnnDtQ4RDg1A-qq4JINJr7ibKB5XfRM5T4hgyIE9DjWZEtaVq9-hr2q4YjfUm0uXcTFQh271fchjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گنگتون بالاست مشتی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/84691" target="_blank">📅 11:48 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84690">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">همین حالا ثبت‌ نام کنید و از بونوس های جدید ما لذت ببرید
💵
🛍
👆</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/84690" target="_blank">📅 11:48 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84689">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/84689" target="_blank">📅 11:48 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84688">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G1sswXuoLElq_M4LtR342gWVbGMiAW8JNXHPPEZBR1SsTso-vQuSEetBZ_MLEJu-Di1tWNAbYLGZ-CZFuVb8gsl3nfBN_YPCrEG4laF7kflbga3viIBNJIVqYvPBncb5-6c0pO4PTLmiD8dhQVMy6hcJzT64vR_P5j4vmaFoX1Zbpt-jPakh9tb87Ur4myRkq4Fwve9-zP1yq4suTTvhAIWhSMIuSlehL29kRpKmXNvR0epOeZfj7fOhlumkdqpKAhTy-XFT0dQafuTBCfbe8Z5uNdriOIRaXpj6mqGnmdi6qACWPBsFAMRMgzghLMDpQrsrlRzD2H6YeBaUDKNnOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دم هرکی اینو ساخته گرم یه ماه بود از تهه دل نخندیده بودم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/84688" target="_blank">📅 01:52 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84687">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J7EYkrfedhQK3coOIs7WKKsNUz1X1UNA9eA_KvPAmygtMo3o7jQcE2sCcfVhP-5z-8iuhNRqbD1wuyuQJsQzccQv_twoV6fFQY4w_DXlGLrgh2QAwplbvOVj5EnnmbPkAKtlu3me66jayQwUtqrxg27jQhEb7DuxeOVxIi81eDaTIk-6z5QBihK-OvZo8chSFJJqjnzIDD4fyWOebUW7geMulo0SnJtQtGN_d68FKT4DNo4fvzbYq6Piv1sAtzF1XiJ7coYVuMFaiUsUKiF8e1BhLhaX_FKHxyYYTrdx0wWffBAE1IaCQoLRsvLPpRD3wvKsMgELkmRz4WzsH19Qgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بمیرم واس دلت دادا
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/84687" target="_blank">📅 01:24 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84686">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">داور کسکش فقط به من کارت نداد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/84686" target="_blank">📅 00:29 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84685">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b32a1ac263.mp4?token=ANmzb6AomkPeKslHlLquZK7NIpyNdjV1ifqHLSsquoh-DTBOJuSrd1_LOl-s59ZhkwaVa9N7hGKV96ljH89N23Y08o7M-PlpXPjiBCjac6tI3uytOIvH_tVSnowh5RW_tDXQ5ioyuQhDAdaaYVOKBbHnZ73wywnCOojeKUyAbUqlfUQxWDokWu0GogZGv9folxMD8-nsgImPma2ClKy1fEojinwp6lNd3EYqL5_3d0fpHrBNeuai6dBj7Tp4WZ0jGnxumaGFE1c6AKrUG1dCOnYsGIWIPwn7hGzuFjlMKYdJMluuAUcs9v4JRgFk6MJBPDBMjL5rOsEWr-e7EG1x5BKUGsjXMuQMaJ9tF1E8fQgX8csxkcZojxBpeC44jP8GIZ6q1XYApxTlho6Rj7zmtqHzPNnnXI4cIZlueTSqMFbrEiJwNiRCd74nNwhSvTfL177RxMGkm-aD_k6K1hE47vsCTwEgf45WZ4Tr0Re6oCwJdQfG4AnVw2oIEiDGJ3Gh_Ix_B8tydQ5ksiuXY2V6JUTbYFcpwdKz8OWU5GkETVyrycYzp_MjR236Wr6VAGUJGsIXOU74tSN7AE8qubAu1D7JpDjHNKaKLMCfQEgy0D0KNZOYq2npa9W3H_5PjZ3AYXofAN5pEfDEwsCvk1Sayl6tfeo8-umluLLYkYsxRIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b32a1ac263.mp4?token=ANmzb6AomkPeKslHlLquZK7NIpyNdjV1ifqHLSsquoh-DTBOJuSrd1_LOl-s59ZhkwaVa9N7hGKV96ljH89N23Y08o7M-PlpXPjiBCjac6tI3uytOIvH_tVSnowh5RW_tDXQ5ioyuQhDAdaaYVOKBbHnZ73wywnCOojeKUyAbUqlfUQxWDokWu0GogZGv9folxMD8-nsgImPma2ClKy1fEojinwp6lNd3EYqL5_3d0fpHrBNeuai6dBj7Tp4WZ0jGnxumaGFE1c6AKrUG1dCOnYsGIWIPwn7hGzuFjlMKYdJMluuAUcs9v4JRgFk6MJBPDBMjL5rOsEWr-e7EG1x5BKUGsjXMuQMaJ9tF1E8fQgX8csxkcZojxBpeC44jP8GIZ6q1XYApxTlho6Rj7zmtqHzPNnnXI4cIZlueTSqMFbrEiJwNiRCd74nNwhSvTfL177RxMGkm-aD_k6K1hE47vsCTwEgf45WZ4Tr0Re6oCwJdQfG4AnVw2oIEiDGJ3Gh_Ix_B8tydQ5ksiuXY2V6JUTbYFcpwdKz8OWU5GkETVyrycYzp_MjR236Wr6VAGUJGsIXOU74tSN7AE8qubAu1D7JpDjHNKaKLMCfQEgy0D0KNZOYq2npa9W3H_5PjZ3AYXofAN5pEfDEwsCvk1Sayl6tfeo8-umluLLYkYsxRIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
این فوق العادس پسر. من میتونم کسشر ترین حرف‌ها رو بزنم، و شما تشویق می‌کنید.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/84685" target="_blank">📅 00:23 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84684">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">مورینیو رو
😂
😂
@FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/84684" target="_blank">📅 00:04 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84683">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">مورینیو رو
😂
😂
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/84683" target="_blank">📅 00:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84681">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GEvweUJX1thCsEL19h_5IRuZrqJec54hDnp_cFGAlgf8WZAlRdGLbkwEz1-UWuzOvnJAOosjG9Uzu-t4msHPB9K_zxbg6T2fg2L-qjWrUILS-BLK51bcw0FdRXRGQ0MDnLWJc3QwaxF-DRyaZE5KZaBsA70y7w9ej6PV8l2J2XJR0myXYVgVnP_c9vov1tcKRlhGhQ_9pzADVGD4EVWl7Kv2jrZDml75pdDtlxO7scZkGiom_YL476mbCgT9aTE7A3WsxGhHirEBE-Xjkzc2owicVnILdPcbVbJDYhSqIVR03K6-h7mZ1_U5yGeN6kpLHP_PneUpVcJYo94lsyTICQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Uwmx9AAye4Nv5kAdbrNDYgnmo6BTjU0vYhSAqQZmhzGyvxZvpkZX2-gzv3On2AZsfnquEY2IYi542_e0kNh8iPc3RaR6aMkmU3Hou6sN9pQIrEdspwEo35v_kj9oNr-6107cOsxQvBuQXZ_cBeN7fuhbfsiArsRo1YUgV6eNR4Lchfh_WD2Rx-qKMQ8pdZ_X18VFVdcT9oVB6dIZGoYJVYSkAcHF4LKODEqeBcUiwwSPpMrPvQ9zjBlyhkDGyG5IlEh4OAFItZwRWH72_GT0VaxkE5qry1avFAWdkY_g1-hJsaySOm5g66wHTEiiROB4Vgs0UuLrUvQ41P3VadTG1w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">با پاسپورت شمرون به ۱۹۵ تا کشور میشه سفر کرد؟
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/84681" target="_blank">📅 23:46 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84677">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/voIQvdFttGwKM31KMsUrN59KUSNywemDj_IX6K3RQxWttn1wGdqp_3fa5PzccOGfQ0lj-sOE6RPYtCIL9ethWrCU9p48vICt2kdtyNhgDrnzLK1Rzj3oaQ2fbl1usnhFuvJOGDu1Qc50WPCPRZJi85XQqL3_tHSUShsMXAlrBk5G7j82-SSyCeG6_hyK3PmEgnFH7Rnp5x6pD15-_-04vJADeCyI5aJy_H6kJQjZkxGz81YTTUtWfVACLcqmYZazi6au5K4u8cJKHb6tx2Zn-NVtMlI4aOvyfxFP9NKPe9xsmdXR_YsdAHTCkrEa-DyyGbUZnF9VyQv8C821guzW3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JyPqQd9TjuUGZ3X50VTF9XxjsjuT0M3DOaGreuk2zgSzWJc8hFEtVUZJYMxi6Q4V1MlG05Syh_QnCeKoOJHIvHt73CoBCQPIuqMqM-B5dn84z0pO02lQjQGLDZTVs6NQmDgFKyW4hyKjKkjK2b87zn2ArIsTsakiELBYYQISXCX98kbBtNuae_3pqzbUVbbCxWQxuL90iggHT7udPBL5AAxyKH0iFTnroFerkIBv3L3hOLDwi0SKhC-iSMy5dDIm1T0ayjQ9MGRML8PqAQQQu8MmeaoZyMpvaWNi-lfFDDN-81lqqw6nQ-4M4r1IbJwtijGMmzL-5uCYoUrcvZQpmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LZeEMThx70zCDt-7aHITUnkxnu_jmpo5i3IVo_lt3-0MHL_xiW6gmalCHJXrBaHZkxh5eFel3ZkBnDyxud4sGY6Gk7UTmHJuplPq5gLgOZDqcjKX-MoXSa4UJHNFoGb4Bpnxo5mW-Ew3TquJN3j-eT27x_m3U9k4Dh453KCu1v1oAUuQz0_VipiHx2CsjH2J-ZTY6975iTHIw8w-0fhMKzZbZyjTPDGKVD1JhtNtrp0S7z9FbhsPDIPBRE1-WFz10qbUFyPLPNz9lKdf0sfoafj7tO5I5K69oBFp_HIQYXXee7xCkCgNylzC1MstT6quXTRTGx5a-ccYrypFEoe0eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SMMuJoXUslqWMIKWrIo7wsbEEDWzBSFBBPv03ttWzOZUFqFhdDF2ezI3wIeqDr9JOmUqVv2UK8OOKBBT_hWpdwz8ma3mca90BGpZrTgnvNz1M7HA01q4kk0YJdGX6YjsXi1kaUF1p6UP7a3XwyEzbGCuSpiFz4o7jGjnIcYmzKeecXMJhIZhV4eNd0XV7E1zskzlX-f5rJgNH0zyDITDLpt5EgVwrsi3tf8TlwoqjqLr30H1mPeKxyEQDX6-zp_I14LEjCsbV36f6aZKQ1xISaDLbpl8SX831N1VHC6y0XQvWXCNw8gz79WJzOY20JhENTORh0wjETFCULPS3qZLTw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بسیجی‌ها امروز با پرچم فلسطین رفتن دم در سفارت فرانسه که به سرکوب خشونت آمیز اعتراضات تو فرانسه اعتراض کنن.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/84677" target="_blank">📅 22:17 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84676">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd88d22e31.mp4?token=C8osbtURjbFNnYlgPrwlLvhw4d3fUaFIrH9XcqxxWJcnceG_wDk5Ng4Dzrr0q7VB43TSKUZSx7jvCxnft5akqnXcxsP0uyExbRphxbJCmZBB0i3SyT724mKiZIuYYD2PCRJZZEZg7-xE99H-Ki5JnMguFEyIjuaiU1KJYzoyekHvPGD6YM4Ak0_H7rUkKOJPF4lFSv02CSq7bF2S-73DzYzL8yCifrZsSNBKTiMZTTaXCIbFkT8LMzYnCWevajA6uSiDeVMgkxplcWTdmtiN2eEKRnIcPto3FlNDF7wRYjn6YE-mR-hSTc-MAMgG_Sn7rReFvcKOysc3r8w5glE7gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd88d22e31.mp4?token=C8osbtURjbFNnYlgPrwlLvhw4d3fUaFIrH9XcqxxWJcnceG_wDk5Ng4Dzrr0q7VB43TSKUZSx7jvCxnft5akqnXcxsP0uyExbRphxbJCmZBB0i3SyT724mKiZIuYYD2PCRJZZEZg7-xE99H-Ki5JnMguFEyIjuaiU1KJYzoyekHvPGD6YM4Ak0_H7rUkKOJPF4lFSv02CSq7bF2S-73DzYzL8yCifrZsSNBKTiMZTTaXCIbFkT8LMzYnCWevajA6uSiDeVMgkxplcWTdmtiN2eEKRnIcPto3FlNDF7wRYjn6YE-mR-hSTc-MAMgG_Sn7rReFvcKOysc3r8w5glE7gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمسه میگه به خدا من بادیگارد ندارم چرا به من فحش میدید
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/84676" target="_blank">📅 22:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84675">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qC13UMOkt8O7biUgfgCsBUdwQRy9eL0dk0fKJ9FcPZmxEtME9jiBDq1BprfPymyjSoTRdATPun1KKOMQL2V_-kuSftE2HShfir7XjgLz6jKvaRtjBPcwNXExzIRaJlgMXPHF04MLan2RT7PGkqX7jh0ddKeCB2nS-vDx1HbHY9psd6lNwg5lOOSEj0Mfo0eQz52tMJEHAnXi6x0tdRqI7yzKoAPRD7AEvcOPy9I2aekJmKL13GfavUw1CS3IBoMPGc3WmIU3azi0irtdssjsnrCnsBsDGa2uPUshqRMcweRhg1PIHU8cz3uAnKn_MVOrZlEOrRwR2a61AjV2ukJibQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاره شدم.
بعد از اون کامنتای مردم، اسطوره نوید برگشت به تیجی گفت شما اسطوره و مرجع تقلید منید و افتخار می‌کنم که باهاتون تو یه خاک نفس می‌کشم؛
تیجی هم اد استوری کرد نوشت پرچمت بالاس
❤️
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/84675" target="_blank">📅 21:19 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84674">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/84674" target="_blank">📅 21:09 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84673">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/84673" target="_blank">📅 21:09 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84672">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/84672" target="_blank">📅 20:47 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84671">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
ترامپ درباره اوکراین:
«پیشنهاد می‌کنم اوکراین رهبر جدیدی انتخاب کند که بتواند به توافق برسد.
-به دلایلی، زلنسکی هیچ‌وقت به توافق نمی‌رسد.»
بابا یکی جلوی این کصکشو بگیره
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/84671" target="_blank">📅 20:29 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84670">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">وضعیت فرودگاه ریاض  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/84670" target="_blank">📅 20:23 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84669">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EF9SPTF8lc7ilEsTXTJB4vLtjH3cKC7dyx602Hx0297CHVEfRyzNxRgxE2n-SgpSvIHpYwXJNgWa6gmOqvTyS7o-lh0iVHlqQuqigwxLOHXsNjnJBupVNTSGI4fYcCu3ekVRvxHZc51oTyxiMqPvVn89zkxWuGPK-RRJibPNvp2MCse0zDdOqT20NQPvPZVCAxMazrpkHZ38FP0K2ARdwwUcXaL_TNALjW6w_xHe4keRf-Ru-3_Ti0RONt9dSy5vqzMBZufSHkCbVw5OfGXQuzi4heFT305krx-2WORe8P6Z8phe6rX1T_w6eQeM90Zn7G3FrRhptPB91yPXt4Y_Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت فرودگاه ریاض
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/84669" target="_blank">📅 20:22 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84668">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">شانس
0️⃣
0️⃣
1️⃣
میلیون تومانی خود را در بری بت از دست ندهید
🔥
😎</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/84668" target="_blank">📅 20:22 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84667">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lue9AGkPDZJTvzXVzILHiJMU4w_GLI73680aAst6bNsbRnFSPDwES0Vp5NMFHP4xKRaqPfdRAc6NsDhZH-PJzJr9Rq-ePIRZNRALSbbrTLJ-hgklvNzwiZyLqlXTLrpLE3wlhVeXx6Pfjw8QvdDkTM3K5NzJ8seyvVFDZfB4UtcbhlD3UUl_MITBC2kmaK1dM5tlv68HNM6I4jJ0ga8XcFN2blyXMZuC8iCu-YrD_DOBEimGlrh1qSli9-moYUEhwl4_jj_6-1ikDWtuxnc-SxfEQPT6DRYEgfHU29R-8UuoJKWbGcBw7A-3IiUJlNaVh3VjNanT-RSK-_f9nsNkzw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/84667" target="_blank">📅 20:22 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84665">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aae2137c8.mp4?token=Sq454mkrsJxNwAeZnRbd5AkaVMOBJuyROneOHuR4AFzu_muGU3fZJ7gv0uPeEUDsqnSgyEWXmEcsxF9UAUvTjqWgTp1AnHgOZScbfVQfeuCMpLXihXQTS8u4U-rkHqC33KKV6uwIThRmIUaNslUQi08oaImdsOAh8gLOJBMM3K4GFtxeUik-0DfGlzXs95DcjmmX2DOyAG9de6gMSwA7KwsO7CATXyAlLO3MHYBfjBNFlaqLUkRyvquO-7nUxzJjaTU6idLGWW0b8noIQcB6pwXQE09hA9QnDAryZMRcAf1F7fujLchu4C1fPHZ0tnojmkVSRM6kODJ6i1hYkVJW6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aae2137c8.mp4?token=Sq454mkrsJxNwAeZnRbd5AkaVMOBJuyROneOHuR4AFzu_muGU3fZJ7gv0uPeEUDsqnSgyEWXmEcsxF9UAUvTjqWgTp1AnHgOZScbfVQfeuCMpLXihXQTS8u4U-rkHqC33KKV6uwIThRmIUaNslUQi08oaImdsOAh8gLOJBMM3K4GFtxeUik-0DfGlzXs95DcjmmX2DOyAG9de6gMSwA7KwsO7CATXyAlLO3MHYBfjBNFlaqLUkRyvquO-7nUxzJjaTU6idLGWW0b8noIQcB6pwXQE09hA9QnDAryZMRcAf1F7fujLchu4C1fPHZ0tnojmkVSRM6kODJ6i1hYkVJW6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/84665" target="_blank">📅 20:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84664">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">امین تیجی جن زده شده.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/84664" target="_blank">📅 19:55 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84663">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">چرا حس میکنم هوا دلش میخواد سرد بشه ولی روش نمیشه</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/84663" target="_blank">📅 19:45 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84661">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/umILoFamV7ctSQB0e-GSuDPB1F2N8CS5xAJDxHM3cNVkJjQ1bXdPsjIkKflz7lGseUkpZauyLfP3XzDitbBygorPm2uTRxIAHsNc0-b3rW3_u91m2FcJe9gULxadBbMpy1OpelSYq8P-UCv2T6AINtb6D8-hA8BhTY7uIz-sLcci7lIvcxhezoWC3ZytIANPg8kQ_-1BjBZpusquNFBU6zfHqdP8leeLiEsx_t37JGBVoNRjeUGIXJR6iw1UG-yqG2QbM-jpm8ybjGpY-sxe8RdEktXnXHZLvtl2rjv5tBxM4WvRGxT2vK7t7bsxu_OtMpatkx3r9IVrQ8wtNHLJyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VFCKCKBBzQtDF4PoG_eabtwDAjYBl41zepiSSXWSKD5UZ7rF10Y8KdrrvEeMkfTB9R-XC9mG3fdy3U1sE6rJjJnFIDWdzUTze5W8oqnrccrIqozfOyiT7Owe7aDI0webm9CRUZ5Lejv8Hic_SlfBQalftD609t6nVcfR_NlFwD8Ag23LdPioQC0l-FM7RDKmgUmi8wKhJgHJR_n7yq5VqzxFAOH0nWNwlZfHinQRBV1Jsi0lyOyrOjB6ywYI_mNG3sahPWUg-hHdBEb659xdqwCmYj9KLN_wN-5EWxJ5w6n0RglJt6knKw1lJjSynZ5YAvt4Sl52IPpNjgpJMidKtA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کریستیانو رونالدو موقتاً از تیم ملی پرتغال محروم شد!
فدراسیون فوتبال پرتغال بعد از جدایی جنجالی رونالدو از اردوی تیم ملی، تصمیم گرفته فعلاً این ستاره رو محروم کنه.
کمیته انضباطی هم رسماً پرونده رونالدو رو باز کرده و قراره به‌صورت فوری به این ماجرا رسیدگی کنه.
هنوز تصمیم نهایی درباره مدت محرومیت رونالدو گرفته نشده و مشخص نیست تا چه زمانی از حضور تو تیم ملی محرومه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/84661" target="_blank">📅 16:50 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84660">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">کاش آرتا و هیچکس یه فیت بدن، هم فنای آرتا کف و خون قاطی میکنن صدای اگزوز خاوری هیچکسو بشنون هم فنای هیچکس کصخلشون در میره صدای اوب دار آرتا رو گوش بدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/84660" target="_blank">📅 15:54 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84658">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cslKD6Ia29aC7Yz2uOAQljnmJKpiyF0MndismKmv18QK4aFyhATlnKe9o2EryMy9EqlkayDIY2bnbMY7fBrdYCuBW7g0vl6-P2baZqVU0-1iW9dFla9KLf-YhSz0vlWK5pT3UTCINwtLcB1CTv-dvF0rscKvSH6mOY-jB1A2-R9baaztjjr_G9U0U_K2MLj7y4Kf1EeGbPWab1BnB0QXf96sm8O6gbp3LociFY10q4zKG8i3q0tjTtG1oPOZ8jT5RAs3y3GHnb3FCMr-9GC96qEkgIhbi4Bt-vT82pz5v58ktEhBfImwM4Dz_VgCo2NLSbHqt_Woh5YqzIhK3e26jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IogdNWzVa9kNA_Xc6ayXR0mdlA-gfi1pRVLfdpwvdiJNrpL0wAqsBQfI26kwED8sh6BoOaxIAjdLizgGpQFeVfSdYV-7vLm2TBhoQpmXSGJ9nbvflV8rVhzSTehyU4idfRVRgodohntkYdR5O9zo8YX21dhvkH43ey-vYXJ8fN8ctfh40Dk7EYsWwrVoKs1LcvNf5WzbO1J-M6Ut8eIO7bDRYv5JXu43r_98WrBfOJWiZVyVcsGecNBansM0Gu9HMUIkd_zb8fDOmQKmuinRybuub6PdFTpXzXJ2WlCHFertRDpY7KHIkn2WV50R2_ds1ye9M7E8-e-p66Za7eJF7A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سوتیدا، ملکه تایلند برای نخستین بار پرواز انفرادی خود را با هدایت یک جنگنده گریپن در استان سورات تانی در جنوب این کشور با موفقیت انجام داد.
وی همچنین خلبان بوئینگ 737  هم می باشد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/84658" target="_blank">📅 13:59 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84657">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">حصین جان جوس ورد از اون دنیا هنوز داره آلبوم میده، این یاد کیریو بده کونکش پیر شدیم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/84657" target="_blank">📅 12:00 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84656">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">در این دوره از تاریخ که ما شاهد امپراتوری آمریکا در دنیا هستیم و دیگه بریتانیای کبیر و شوروی سابقی وجود نداره، هنوز عده ای وجود دارن که کلش آف کلنز بازی میکنن، منم جزو اون عده ام، کسی کلن فعال داره؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/84656" target="_blank">📅 11:40 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84655">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ترامپ:
ما گرینلند رو با قیمت مناسب به دست آوردیم: صفر دلار!
کصکش املاکی
😂
😂
😂
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/84655" target="_blank">📅 11:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84654">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rRbdoM59K9S6ZB-wB8CZP_m2WMZqPgAZ6J990aZKkHBdrPB1cBeYUZjEYCNf8d2ibXwkJ36j7fQ1ivQntIKRVTYpmzd_W83M2sSd1ZPMo2YixYCdcZQyAYoVdO7WRvBr6xk60prMjKDpkApmCym1yamo-47mJQnqMzEXmSiVA17rhSS4zYbC2FJO750I3dfRSimwJ5FtA30NP2GSxcxpJtvxGUMnU06cfZLZPjJ3-0cTRT_NCfSXfxRztLtlk38stjfCmtQuUQCpVhRWemqYZKM-p0ePorvOlUyTFaoqAoeu-9ipgXsczrIeLPT7j9-YvJBEZpsuvxpJNkr2B1MZww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من میدونم تا مدت ها قراره اکسپلورم با این تصاویر گاییده شه، فقط بگید چقدر طول میکشه، میخوام بدونم تا کی اینستارو باز نکنم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/84654" target="_blank">📅 11:12 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84653">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">همین حالا ثبت‌ نام کنید و از بونوس های جدید ما لذت ببرید
💵
🛍
👆</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/84653" target="_blank">📅 11:12 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84652">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GWVmXeepv26u_NPWcHtzX9LDTOxJZy3-kj1fFmDL1rEalulrtlM-Hq9yMcq3_YyUWMaxeEOu76WFGUMCnhJNygxm_kqQT8M4Wb60HHVUkiN2gfNFF8QNrnXNxo4Ty8k8WIv46BYOmGl3CJeakGoSMztG1tpKrE3CgLTfwbICzIWvnjLjg_xBn0zWzfa_h-3ykyhHHyxkUMwH36iLHKNf3XIRXA3UTMMJ6E4u8Og5r9UAh3Te9lE5ujvYNdyoULZys7zyFFK9sMnfGSQL4nC4y5lAoW1DizKz5xN7ltkhSiLNu4Ilb4Ct1FBN92FLSiRDAnuq3ZiqWHUlLPgQjQsdvw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/84652" target="_blank">📅 11:12 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84651">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4795cf2815.mp4?token=eep-imB7p8gt49lYanvyMpLsn_5KymYiYuA8FILFLvMdevrdV2XYOAJZ3OJREen8IWpmNL3pwuHyR0uwQn9yIoxAfNwF4Uj4LMenar48xpdNs80jtOHrdeCn94mCpxekPpUkq61WPKzVnFSubZBaq0DFSci0JvEQgRQTJ0CCjT5Iy54XBXKH7fX0VxfTk1VAWSlXKAJq4PanyWJryvvev7GiPSYaWrIZKUuX8f-7dTlADIJcnVxSI_Pb7MzcyYgqBECYfOQiYHHPrRExc2PO4IFSRS84s5dEzT7wupLsqavk3AUluHFnEVCa3n2S2upOBa9qrCFL7-SI76hPsOt7Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4795cf2815.mp4?token=eep-imB7p8gt49lYanvyMpLsn_5KymYiYuA8FILFLvMdevrdV2XYOAJZ3OJREen8IWpmNL3pwuHyR0uwQn9yIoxAfNwF4Uj4LMenar48xpdNs80jtOHrdeCn94mCpxekPpUkq61WPKzVnFSubZBaq0DFSci0JvEQgRQTJ0CCjT5Iy54XBXKH7fX0VxfTk1VAWSlXKAJq4PanyWJryvvev7GiPSYaWrIZKUuX8f-7dTlADIJcnVxSI_Pb7MzcyYgqBECYfOQiYHHPrRExc2PO4IFSRS84s5dEzT7wupLsqavk3AUluHFnEVCa3n2S2upOBa9qrCFL7-SI76hPsOt7Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خداوکیلی ۵ سال پیش به یکی میگفتی پیشرو و هیچکس رو قراره یه روز کنار تهی و ۰۲۱کید و آرتا تو یه کنسرت ببینی فکر میکرد مواد زدی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/84651" target="_blank">📅 09:58 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84650">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/258be0442c.mp4?token=dQxH88TmLYEJlYwx1Qkh_CW_-_rj0L_hgy7UDOEzlZYMhqejdIIzk4RK2iqJbosaY6fELOe3GPTwv3itrcg08x2qV5OPXTi8ru8I3aPkNpTECAGnTn9X3xv5bWkhgX3aU5g9tkWOj_nxhP6B6NcqSYW0E5JtEzV5IsrQW06LkNgEIz2XY3u_iyOeV7mvrXpHWf0Cidckyh1ih7msGTWIupnV9YEjCqfyoyvE5CiNnvAEgVkenMdyf_Tw-iP3gt8M_CxOx5LKeGoVMv_xx-QLlUuePQhxwQrqhadl8OUoPpfbKvtnK0vf98_AmWyUADKqMHgzYHlzi33NGzYtwICr3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/258be0442c.mp4?token=dQxH88TmLYEJlYwx1Qkh_CW_-_rj0L_hgy7UDOEzlZYMhqejdIIzk4RK2iqJbosaY6fELOe3GPTwv3itrcg08x2qV5OPXTi8ru8I3aPkNpTECAGnTn9X3xv5bWkhgX3aU5g9tkWOj_nxhP6B6NcqSYW0E5JtEzV5IsrQW06LkNgEIz2XY3u_iyOeV7mvrXpHWf0Cidckyh1ih7msGTWIupnV9YEjCqfyoyvE5CiNnvAEgVkenMdyf_Tw-iP3gt8M_CxOx5LKeGoVMv_xx-QLlUuePQhxwQrqhadl8OUoPpfbKvtnK0vf98_AmWyUADKqMHgzYHlzi33NGzYtwICr3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درمورد جنگ ایران:
آنها یا همه چیز را به ما خواهند داد، یا دیگر وجود نخواهند داشت، آنها این را می‌دانند.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/funhiphop/84650" target="_blank">📅 05:06 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84649">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">تو تنگه بزن بزنه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/funhiphop/84649" target="_blank">📅 01:21 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84648">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">اوه اوه
روسیه تا ۷ اوریل سال ۲۰۲۷ توسط امریکا معافیت تحریمی گرفت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/funhiphop/84648" target="_blank">📅 00:09 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84647">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fTIY_Kbao1jEJiXh4qWI_3fwoA-4yOXC5B0w3T1RiueRHygOA9f2SEiBF-q0jYV1eqA_f4m_F2MU-GE1_Bqd-n4HlNkAazh5pKHFylybWUk1RwBwMEg5I-0Bp_oVwRnlh2scLlDWdNw_kJ1SHxZSF4RzYbr1ZDOB9xhf0afUpUuVFr4kRaaf8MRoX7h65MmLnR6KtcgIM0usydcfYVB2iY_Ff8T-m6qvTmbVcWFXPm3X-sTyajtv8_klC4wanRSvPAp-YYrFypk0UcItXUnMnpftM4iF9yIhm1xSAIGKKcooivT61mkcHVSKEqodq16V6SoxUYABiNlLE-pK7IjVrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هی داره یکی بهشون اضافه میشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/funhiphop/84647" target="_blank">📅 23:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84646">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J_wQ2wmMZk71ym5EslezpMbnsnCagbGbFGqZAFgJYHpnygSO8rPZUzze7pMpZkRZ08tE6SpULvg0jNKl1yC0ex7TWY4O5q_geyY_65tDHWaGDkxxJkA9gae7zSb3IIvM3l8hAtiwRljnTdKzWstEuxg2vjnlJHueTs1Ppq3wm5_7BFI3X0SBvqGxezr5TZF88c7k4tMsvArT_4Q0hEnAfIRy-xsQTLySi1SdE2cRMtpZAaDf-50ZA5gRAavX-GfcAayP-umaxi8f9IIDep4VFjCUDKrDLwGPaDs_TrRTLBgQ6mn3fMXhx9BCVh33jtnH8_9L2m_jmnhzzd7QAPhDtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان فعلا پست ندارم اینو داشته باشید تا بعد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/funhiphop/84646" target="_blank">📅 20:52 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84642">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tLCajCdrPNOl8Grb5SGvlELcn5XyYYqxGvidwY8gUQhh1KaWS6bAS5sgAj2gMRil_7iQL6F6YpxEKP5DVeRnwRQp33LDQcCEmTtOWBSVmhDyH6yPyuav9Kxj2mTsW1f34B0vJelyRnW6gzKvmyfTgZN5tDEDguWEJ3DZ2rwMp5l71RIXdVOmxQYp_HSS5t41aTlND7zV6fXx4Yhe513f5wn9wE9Qp-RLnu_MJTVfxQnDfAbduZxQo9hdCOYZ2TBFz2V7uRhJ6unkYwlWOoLG3LT7iBb-Y3CTy0612GEZxxYBJFm9-zFzlNuIZlEky5ujETJKxC6XZy5GQiBRINgLDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uj-YtA_Be6pEYSe0EcIlaRvrXsMoS6rUoMgR0G1yo_-EsoRI-4LHv04l0J1_4USGwb5Bp9ThPvlbtQuGAMLuEWWiN4Jv5uOEUW8d3d8ubJ5gp_i2sCArOe9B_EQy8C2E2UVZktFmCPbK1aOtjZiuJ6OfAWTvYVH1hTM-Sb-Ak0Vsj25UJIt7WLP24pwkhNI1k83fDv-w6IrjTm02gJVYyQzfyl_FX0NDuyNArn5TUVidKzr7U91T0YYy1kAzRjADZPUVIWQjU5m287wQ-83xHNltN5rPpdbhyHXzkBs8DvqA6VT_i605JeuVzLUgj8hrHt0RQan4YCEe8A7BFq_0dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LK8C2d68bn06XBkXiuKbZ4ZBunUbOWScmi5_cPxY93dfit4SnGVgQidrAZAGW_CbqsYgAOp0EpOUoQxM4_9WGTGSyquZEdXM5vxKZS33HkpiHuQil3uEX2U6QuOMTJqh5OnX-GReCF_KlNJV8AF9hjVJFiqalSgb3OmUTNkbE7phT23JV9gey6oWzZOmX4sHlSZXSNSvPH5lzGTw_vY87uD8pifcgE0fNsMYw-DqX1ToNZ3pkMPhlhLEcn1PENWyUYeIVerSsk9OqZtKoB_3RvU788F_iW4J93m4VuXLoF2elnDF7jqpPeuBmwhsPLi8-2A1WbKscTDcn4JtVqwOsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/v9x2Qq3-xsxFcWyivZne8gnan8PfO8miua3sw8XEmds5DzqqLvZc7cB-z-Rli86eaNSkLuOvpe7GpOT-8_LbNytwPal8_8VNZ-Pfctqz0dEbM0RptfRDU4ogi3QGt18o_3VvmLNxoW8dThMi_ezrj44NK_GmzHsh2Co7O8c2hwlX4Gu4qpUH-2gpTGij052VkhXHxu5_fPuMKarFoR0jCpKS9DZwDGULIfB7E5IPyc7OWjJkOL9WrnKEGBL5SqspBgCD1yp8MEQOSOWQIaooTTYBI_6mX-MSs-pjdaHq-0U4SVwUekbLB_60ixAwt4oMGlCBQlB1ErO9wSp1yRtOpA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">همزمان با ماه کامل بر فراز آرامگاه کوروش بزرگ، این اثر هنری زیبا خلق شد:
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/84642" target="_blank">📅 20:30 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84641">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V4vh_oFLBB07IAC9lI9pkNa95t-2j7SQxVntXfLISDfBy-YwhPI8QozsHY2SgxhwHM3IT8HGSQqpUWFp7NGCP5fwlumhSnp1KXBxb-iRqx3TPS30dMqAjmDHVCz1POegvbJGxKB5BhWvce0fL0WjAk7838hJYLwlLgymzJAdtTlxkWZll98A0Nm5tjsT-9ed5GErwGdmqqEnvvp1xsmKvHo9Fr0FvPw-UNeih2brvb05oRvRCu5jBSi13KsT-E4Il7sqvXJ2j7fKl_-6qGg_I7zN0gfcvagNArjRIRfiiVGkpZOm8Zfpt10aWUrNzIkLyCi-blAixN6yF51CU6LJ7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چجوری مصرفمون از خود افغانستان بالا تره؟
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/84641" target="_blank">📅 20:28 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84640">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ea1SljZaXAPYed8eylW4OXaibehyrJEqjnibju7N5XKUQBATgCK69iJC88IR-1Bv0-ciKXf4tZY273hiu1KKiPvM4T2zCvaRYpQnW5qE86m4jn1IJUUYnjHNZF1ouGu1JSJ7Z7yvXMUPyf-z4-k0-aMgFrm9VjgPRAs7muBzuegVYeRezFNt3df2s5_cX3wOlHY8-uf1CHYWeyI9L2-_KXKWQyYhcIJ9-B24cHV5S194Trk4KLs641QPSQjV2Jb2htj6rakJ14S4Bt28TeDNc8b8VUXlBqtrpB5-a2FgImBLbBC-lIR4XWnZB1WtW7HEkh2Ngp7BQ9QKcuyc6M3mCw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/84640" target="_blank">📅 20:28 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84639">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V-ChFrXcvgkrRzBnuBnmDqnfEi1jDTEC_oMppl7A8szfTwGRILZQGOEmKa7UFWE_eiKkCU4Su7Wih3SJ4_LF1y-_CgDzdtuIZHvMtZnnpZrxx6d3SbUwkW884rDZOn1OkkFKYkuUzhjNslTNhXgz2WvWKX71dX1BcO6bgYyBu7WpqyBKoF_SWFnM8nF8mzY_szzAKgw1icy4xnWnhC6jSArqb2zBBWnhmvzqpogLenEry5qlNJk2Q6YhB-QmVw-yCDPhXJLwK1-oVONlPhAmPZmIRYYXlQ1LQp96XwpNoaK3tSXdifE3ja4hQa7IVM03FCh_LY91Y6L1eiS5d2cOdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدایا خودت رحم کن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/84639" target="_blank">📅 19:23 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84638">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J_OekxHtuepweP3fFXSWOCgXsqW45a6FNw-OEwWg8IKJq0yaJm_BM-KJD2eo-X9GqafTVbhhrHBjtK_LEWKktiA_DAroEKJFdK6JTkC-_lRcwtRRAvTedgdCuWOTTtg3jr3wtcBs4z6u65YyjGNJH1x7ZsMXnoO1gd6Rm_AfsAAIbVn1mid5z-TmTopyCExuOOh5R4sDwIXasRFzpGXQkhVIQ9BOqKKuAShop8oJupOVyfhsnW-4Ui6n2bfGBNwe8YlvRTQ3zkN0yL-lcfG9l5lT_uESU4ckraYdsAEPxsXSQeMTBhKOVLuw5xj1CiGQ2QlR4wW9HlFgJoe_zUySoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجیب ترین چیزی که امروز دیدم
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/84638" target="_blank">📅 19:11 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84637">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">دولت آمریکا در حال رایزنی با پاکستان و ترکیه برای بستن تمام مسیرهای زمینی ورود و خروج از ایرانه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/84637" target="_blank">📅 17:59 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84636">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">خدابنده‌لو چقد شبیه رودری بازی میکنه</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/84636" target="_blank">📅 17:42 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84635">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">گزارش‌های اولیه از کشته‌شدن معاون اجتماعی انتظامی استان در پی انفجار مین کنار جاده‌ای علیه خودروی نیروهای انتظامی در منطقه چشمه‌زیارت زاهدان حکایت دارد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/84635" target="_blank">📅 16:59 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84634">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">میرسلیم، عضو مجمع تشخیص مصلحت نظام : تیبا در سطح ماشینای معروف خارجیه و به راحتی می‌تونه باهاشون رقابت کنه.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/funhiphop/84634" target="_blank">📅 16:04 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84633">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/funhiphop/84633" target="_blank">📅 15:45 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84632">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">بچه‌ رضا پیشرو یک ماه دیر به دنیا میاد، ازش اجاره میگیره.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/funhiphop/84632" target="_blank">📅 14:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84631">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fbJmkrigPxCFMDRsRKrvFceu-8W8ypo5CQKezJPrsDS9Qvjv4kAzcGKrQjamImv82wywm8nsKkHSaB_yz_o3zODqy7vXwGhoZH_sQZ3hApLjaKEa_WTkhUGAu9SaumamXmHOmt6ZjieOi0R4B2Xq3dtUyuSuAQVjiT0JuH642FtSxCT3jQ6QMyZOJ5vKS0jUhwfMOaJ8oxO4pNsVqEJfVgzculSyBYE81lBB7psPWwpumQyBfNR9EDGf7LGUz7XLUe78C0vTH24hZ1ITxQYnzwDwu_9IQsTD06m2af33TcHS7PUaigrZEl_8FjM6I1TsKihrvqwX8iOOvTxsn5aLTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماشالا حاج اقا
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/funhiphop/84631" target="_blank">📅 13:17 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84630">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">سر همین اصلا به مشکل خوردن، پیشرو زنگ زده بود به هیچکس گفته بود داداش مالزی کنسرت دارم، هیچکس گفته بود خوش بگذره داداش</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/84630" target="_blank">📅 12:43 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84629">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">سر همین اصلا به مشکل خوردن، پیشرو زنگ زده بود به هیچکس گفته بود داداش مالزی کنسرت دارم، هیچکس گفته بود خوش بگذره داداش</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/84629" target="_blank">📅 12:39 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84628">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">من اینو صب دیدم سریع رد کردم گفتم ای آیه</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/84628" target="_blank">📅 12:36 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84627">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromᴀᴍɪɴ.</strong></div>
<div class="tg-text">من اینو صب دیدم سریع رد کردم گفتم ای آیه</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/84627" target="_blank">📅 12:35 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84626">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vgmPOkhsoZht4mEdgdIS-oNzTq5CJcHUzt1pZznSya3An0JR-iZpoENmkXnjpkLJsB8jt6AOiCxBIjUvQH99Zikp51RVVjYNjf9mgucE_eRH-o66jMyLaK51RKgVZ7ElPZDc0CFbL7NvKVxjWJtEsv1b6O3_LQZePF6Wg4W3tICCT5w9ajPogoc4S3U6cXjdQYsO9p3JJDq05tXl45HSO_bHmYbHe9ZRsr1CdIGgfswF75Pi2rEcC3eUvVYRl4a7cI6T24dgGCOJ1ru2E1W8eMrBwkZY1UR0qMomW1j2y0eP4Mj9XH5AFER4oLU5W_OxYGg43N7ZiZq7PiLryHSmiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا فک کن فیت بدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/funhiphop/84626" target="_blank">📅 12:29 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84625">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">هالند و امباپه تعویض بشن بین سیتی و رئال جفتشون بهترین تیمای جهان میشن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/84625" target="_blank">📅 11:58 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84624">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cemt8FLaPqONebA2VxzrpM0QNkPpZg0Pyb2hg964jEI8c5N7riParWRTpK8JWetA8UNQDJW73Rq2bp9EbP4mqVv2FDkSOESN-dlQPJiclWDaqLS8uUwxgL0qdcdwyhdrwKgEmjfOeVPpDl-Fcbi6CSrqqnRzUZpisCY0MIuenObXatPhqrjZcyCXgw8vj-PBdsiAL5q295cIspsdo-hAGa1ftvFWsv_uEuDTWVnHuoduaqnk21TArA-eT1HtC-duxYWQrp2TlmARhwhbFu0NU8UFZBjOdlLhcajoorwL4tZ97onJ6IOoy80WWnMJ37z96N7qm3KO6tO6n8nVrJXUig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس داستانای کیلیان دیکتاتور حقیقت داره پسر
آاس :
امباپه توی رئال هیچ رفیق صمیمی‌ای نداره و اون توی رختکن رئال احساس غریبه بودن میکنه. با بلینگهام بینشون یه جور تنش و سردی وجود داره، با وینیسیوس هم رفیق نیست و با بقیه بازیکنا هم رابطه‌شون بیشتر در حد کار و فوتبال حرفه‌ایه. حتی از بازیکنایی که قبلاً باهاشون صمیمی بود هم کم‌کم داره فاصله میگیره، کلا تو تیم کسی با امباپه حال نمیکنه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/84624" target="_blank">📅 11:31 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84623">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QseuVLTBRJVHzunnKmuId76NXlR2RVLbEJSG-lFNrDXVXAWWEZtBp2BAlNcoZgmWplWErKEIoC15-WqmLperU8thSrn1FRPru1j6X2r0Mpgsx4e_4AAol9IaFsBO6LC7AqhCHj4nWcGh8etGserClWaLZvcrKGuzjmLluIxI_hRtCuDEuM_fJ2Hit6dTNSiE868DONlqolRVSKn9oddH8c0soNXT7yyrMz3ZOKb2mqfCXkihT-yrN-K3FmyzxuCX7oLBkYCIta2kpRXZaq-GxlmKfUn_wR6mPq5V2nSHNxGkZAY0vwkH7-atv0lhKxOcE2HF2LjHEIvtVkpWquXlRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مستند تک قسمته ۲ دقیقه ای(یک دقیقش تبلیغاته)
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/84623" target="_blank">📅 11:00 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84622">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">عراقچی پالس های مثبت از مذاکره با آمریکا داده، شیشه هاتونو ضربدری چسب بزنید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/84622" target="_blank">📅 10:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84621">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ویچرت؛ تحلیلگر معروف آمریکا در توییترش: اسرائیل دقیقا قبل از‌ انتخابات آمریکا به ایران حمله میکند. این پست رو‌ ذخیره کنید.
پ.ن: این یه بارم گفته بود آمریکا لحظات آخر جنگ ۴۰ روزه میخواسته به ایران بمب اتم بزنه که ایران میفهمه و مذاکره کردن رو میپذیره، قبل از شروع جنگ ۱۲ روزه ام میگفت دیر یا زود یه جنگی بین ایران و اسرائیل اتفاق میوفته
پ.ن۲: آیزنکوت رقیب نتانیاهو در انتخابات اسرائیل هم دقیقا همچین حرفی زده دیشب
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/84621" target="_blank">📅 10:20 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84620">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">من جای تهی بودم دیسای قدیمی پیشرو و هیچکس به هم دیگه رو جلوشون پلی میکردم و از واکنشاشون فیلم میگرفتم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/84620" target="_blank">📅 09:58 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84619">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mU5n71Xs4qaRLn7OwpBguNF12s17B9a1mF4aG32MJieQKyp5b-CuuHcHL3By_Y-YHLTMeu0qcUG9ZqhjNee1KPHGHLDGt2HkG9UZ2Pnq7vY8NpZIKNSycY3G9FqBCgoIZf2ktteyyQcByFcjcb-IeJuA07wer7ppXGS65cJxzTHuVUIbLUKtLqAeh2ANqtKJLz2M_MT-F2IXokePhXVeptp26H4HpD8wZNhyiLGamohtySj3R_YGx5wsUaICA9jhrMP0ZlMrpfyYuB4d2hZKHEMykvsHGEXpHHv-VgSbiRBe3kTSsU_QqpX2PzDbqMPgKgfBvJu9KI7flxRzVqRHjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یعنی کیر تو روزی که با این تصویر شروع شه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/84619" target="_blank">📅 09:48 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84618">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">همین حالا ثبت‌ نام کنید و از بونوس های جدید ما لذت ببرید
💵
🛍
👆</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/84618" target="_blank">📅 09:48 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84617">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jEiV58ZIiPuazLQPsFyDZ2AwYdJwyu1XKN9qquyIeQA0xpvubGKP11obttD83wzhbFnQ6lln6oFAHM4VKz0nl7B76lB6tjkn3jz2Co9sGsugK0p9_0kz94nIKbPuSehgXDlz4jAeVJ5qbU7rKx4zHHuYftg_lw05qNbX8YqJciViM8FvtBeP_3h1EVmhegp9hLN-K1MPEi1j39QveBaHI_iQhPEuh1Dh0PDklY8Pph3fhmSgbsVZ3Eypig7ZS3RYYDWOoTUT6r6hNUmy7vo0kw3UOJwA6vsnlLTBvH7vchbw9ojKQjH6p6Cnqrd8EQZA30XbyMUXaAM784TRAOIDdw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/funhiphop/84617" target="_blank">📅 09:48 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84616">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a66d8a6ead.mp4?token=cBlNFOvVeRZxICa3xx7E2TULXTBh9yAn5paSgXQqd_67BkA0g0f8rVH5ykBiX2nFIcdTc5aySXAMO9nVtWtzts3kvknlx5wx7mhQnIeMH1cHCKZtCnpVtxMG4VsDxHFbi7T9MjRaSrETFEQnqS0mncM2XqDM8eNc0xipD0-r2gClv66bSKDlLr8yE98bGC5re7Ke4aJ3lhasjprk5i3XgRB-ARU9pNoXYeipbLyhHtvdSsyZJ1VtruMx-08Zu5-TXSd9ukl6_xdthDuJiNeBcDcLf6E7cRUJRjpbh7MCVSoOnbNAom2bYM5VvGyBFukTboQ8jvE6siYShLaq9NCYzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a66d8a6ead.mp4?token=cBlNFOvVeRZxICa3xx7E2TULXTBh9yAn5paSgXQqd_67BkA0g0f8rVH5ykBiX2nFIcdTc5aySXAMO9nVtWtzts3kvknlx5wx7mhQnIeMH1cHCKZtCnpVtxMG4VsDxHFbi7T9MjRaSrETFEQnqS0mncM2XqDM8eNc0xipD0-r2gClv66bSKDlLr8yE98bGC5re7Ke4aJ3lhasjprk5i3XgRB-ARU9pNoXYeipbLyhHtvdSsyZJ1VtruMx-08Zu5-TXSd9ukl6_xdthDuJiNeBcDcLf6E7cRUJRjpbh7MCVSoOnbNAom2bYM5VvGyBFukTboQ8jvE6siYShLaq9NCYzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیشرو و تهی رفتن لندن که سروش هیچکس رو از نزدیک زیارت کنن.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/funhiphop/84616" target="_blank">📅 02:43 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84615">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/byLivDBBUMy60pD9x8Bnlfd7Z2G_VHrZ_VNNjTLV3hAknFWJ_NGL9HsshTtbH9G_rVY2QXqKeNrT8xdYgdOWxBYzJbfDoYbLRDnmutyottvW6glXzb-Yz9CQq9DY1hHG-Lj5Ti_rGhC-wfWx7SUlTtqc67NGQTDRaQhVocS3Fjst5wA4Fm_2UKDXCnxEVxG2DcZ8lxEVu17dIQO1EZNaaRBRYjkuMTm2SgNx4eN7SJvieQrntbfBZmCZqoNiuDnurTdLDzaRonwssAZzK8_aI-4KzapdwzCLTAyzPkfOIo8Nk6rlNfwSyF491guqPbKH4ifcw32Vzh-Mv54ou-BLFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنوز شیوع طاعون تایید نشده؛ تو ایران شروع کردن ماسکش رو میفروشن.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/funhiphop/84615" target="_blank">📅 00:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84614">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">سپاه به اربیل عراق حمله کرد، احتمالا هدف مقر کرد ها بوده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/funhiphop/84614" target="_blank">📅 23:36 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84613">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">اجرای جدید هیپهاپولوژیست
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/funhiphop/84613" target="_blank">📅 22:53 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84612">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d16fa565c7.mp4?token=et8Nxz1AU4e7E5vH1o_Z6CSN4a-kYnb0YNh4kyjD2c2GrA-Q35cTxJxLq6bgC0lVdXzmQYhWqh_WY2VUHGJCboOPTE69UZ9Al4FPukrDLth2ymEemBmJQi_ICNaxYrB-TrKyQw0JFyqyORRNttl5vpLVberlPmHaWrZJB35OO7U4t_sgk4igxW2lmx__5_IW1jk1clUb-M4XJy2-RyzdEFBzWdk6STZy3I7yDt-rFud2ZzUlZT5A-tphT2YRBLcy8Fgj5XJaR07QK6Kcg8VeB6bPbJuTqDww9iV7WevPiddkL7cuKia1zC0zjCtsle5FgCiYTEL0LNM2JPU-Q6y9OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d16fa565c7.mp4?token=et8Nxz1AU4e7E5vH1o_Z6CSN4a-kYnb0YNh4kyjD2c2GrA-Q35cTxJxLq6bgC0lVdXzmQYhWqh_WY2VUHGJCboOPTE69UZ9Al4FPukrDLth2ymEemBmJQi_ICNaxYrB-TrKyQw0JFyqyORRNttl5vpLVberlPmHaWrZJB35OO7U4t_sgk4igxW2lmx__5_IW1jk1clUb-M4XJy2-RyzdEFBzWdk6STZy3I7yDt-rFud2ZzUlZT5A-tphT2YRBLcy8Fgj5XJaR07QK6Kcg8VeB6bPbJuTqDww9iV7WevPiddkL7cuKia1zC0zjCtsle5FgCiYTEL0LNM2JPU-Q6y9OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوجی انانوبی بازیکن بسکتبال+۲۱۰ سانتی نیویورک نیکس رفته دایرکت یه دختر ۱۲۰ سانتی و میگه بیا ببرمت نیویورک.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/funhiphop/84612" target="_blank">📅 22:14 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84611">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49025c86d2.mp4?token=S9TmvxQ_suwAwXXPlDwt3HRAmr-ZSbHRKpnwHHUDM6mLHk4sSLdTNmfm1vFXS3tRZZCGnp_Al-ohSM6KNojXe__6qeW7VjNMOKtTXWAstl-ViyPuJGghILe-gjV5li7RloTWISZ6f6eAON0HMexKkPjn3pktoEIMvL8kiei5iT7HamEDoIhbrEJMdrILljDaLUZioF2sxP9uw6KZVn1S8w7RYYDE1K0NWfH4eO8vhh_1itc8IvCbzh7bSAuOOQqxvZ9qdlns7PIviRKEuR4v_ygIT6a79J-h2HAj7GP1bB9zw99v2O1_P2qQjYZUg7l8t32Rc3QdCYRj70uLp1qi3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49025c86d2.mp4?token=S9TmvxQ_suwAwXXPlDwt3HRAmr-ZSbHRKpnwHHUDM6mLHk4sSLdTNmfm1vFXS3tRZZCGnp_Al-ohSM6KNojXe__6qeW7VjNMOKtTXWAstl-ViyPuJGghILe-gjV5li7RloTWISZ6f6eAON0HMexKkPjn3pktoEIMvL8kiei5iT7HamEDoIhbrEJMdrILljDaLUZioF2sxP9uw6KZVn1S8w7RYYDE1K0NWfH4eO8vhh_1itc8IvCbzh7bSAuOOQqxvZ9qdlns7PIviRKEuR4v_ygIT6a79J-h2HAj7GP1bB9zw99v2O1_P2qQjYZUg7l8t32Rc3QdCYRj70uLp1qi3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرقت غذا تو یکی از فست فودی های کشور:
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/funhiphop/84611" target="_blank">📅 21:49 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84610">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f08a78a31e.mp4?token=MZ1FMwtEbchbKefgvLDht-hyluRq8hA6lJtKuBFW_XijOKACO-Moh8cAew69FIkDL9dhhAxA3VvvTuN5FrfvpMXJERXVHffGZES52_qeakavQ8uDKGIYSQl4fNo4YePziV-VDqfwTnmvyJEtp2jLKQdIJ8aiZz1fUkPz8eAIIUDqqXyDhprIGwkZXSmycBy_4uH4C7vLWi_-FhWJsR_AvblXdu7jrHzoM3DIXi-Ngzl7b5b3AywDzVBF1OXvLwHFvBZwYpZm40v-jhjCrhLoiVgzBBf-I5BZMaBktGnjRFj9YMt-ZRluv-JxrozSvseJsQcTCfdrzGVDBy9x8Djvuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f08a78a31e.mp4?token=MZ1FMwtEbchbKefgvLDht-hyluRq8hA6lJtKuBFW_XijOKACO-Moh8cAew69FIkDL9dhhAxA3VvvTuN5FrfvpMXJERXVHffGZES52_qeakavQ8uDKGIYSQl4fNo4YePziV-VDqfwTnmvyJEtp2jLKQdIJ8aiZz1fUkPz8eAIIUDqqXyDhprIGwkZXSmycBy_4uH4C7vLWi_-FhWJsR_AvblXdu7jrHzoM3DIXi-Ngzl7b5b3AywDzVBF1OXvLwHFvBZwYpZm40v-jhjCrhLoiVgzBBf-I5BZMaBktGnjRFj9YMt-ZRluv-JxrozSvseJsQcTCfdrzGVDBy9x8Djvuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من هیچ کاری به این که رئیس بانک مرکزی ایران به وزیر خزانه داری آمریکا سه روز وقت میده و این که دقیقا برای چی وقت میده ندارم.
ولی چرا میگه ۳ روز بعد با دست ۴ نشون میده؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/funhiphop/84610" target="_blank">📅 21:36 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84609">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d8dc7bfe.mp4?token=gSsX3dD-vaOKS2in_dDZseFkHr0OAcCiSjnd5doy0RFaq4apBjgWCuCanSaT9PNjqwp202SeOu98YOagBnPHjUfRj3SJcdkV7eAU5N6eaR5ylNoH5MCt6x2VxxHcDW1dul6zf-AmLbcKiL3OHV5xML9YJynK4n78MplqcCJaVAbacmcUVcS__3oe5-pfDA4hIHAwKecnGgS4hkChVsKUlsIwmjCL0hOWLU6a-5VRMb0IKnw1GvqI5y-KSivuxrolqjECNakLhspTkNor-wyEKzzTEJHs6o0EPrM1KOaDFTPaGWS6md9uLysBDjPb7a3FuaBn2Fr-Ac8gC-if42ULrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d8dc7bfe.mp4?token=gSsX3dD-vaOKS2in_dDZseFkHr0OAcCiSjnd5doy0RFaq4apBjgWCuCanSaT9PNjqwp202SeOu98YOagBnPHjUfRj3SJcdkV7eAU5N6eaR5ylNoH5MCt6x2VxxHcDW1dul6zf-AmLbcKiL3OHV5xML9YJynK4n78MplqcCJaVAbacmcUVcS__3oe5-pfDA4hIHAwKecnGgS4hkChVsKUlsIwmjCL0hOWLU6a-5VRMb0IKnw1GvqI5y-KSivuxrolqjECNakLhspTkNor-wyEKzzTEJHs6o0EPrM1KOaDFTPaGWS6md9uLysBDjPb7a3FuaBn2Fr-Ac8gC-if42ULrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با اعلام رسمی سخنگوی قوه قضائیه، بی‌حجابی رسما جرم اعلام شد.
از این به بعد در سراسر کشور، با خانم‌های بی‌حجاب برخورد و براشون جرم ثبت میشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/funhiphop/84609" target="_blank">📅 20:52 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84607">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LxOt6-nbyLTkXdwJjsY5y0_w-617tRTWSaHYlyHggWbvkhcLnERtofr-4RDpuVynUNEkVZFnPKKIEeA71r7J7e2oRvWPXL24kIIAf08wtNAu2I6uR59VFTxd6awd65NkYe5u32qhLPcjAHDIko3buMOF7rHPAwpwACOZXTM19HyakPdA96qEXmvPt3IhXm2CKT-JabZw0_Sa44CiqkwpCchn1NYCfi_7qV54XFpw3s9gfu-ARHrX29wGqSTm_hk54RebcnxXFhMVa47FLr6QHVeaa5WLHI31DtEvVtXtScNa9YcTX8GL08teJC3Hs5tK85l1ttWhp3Z4S7wB12CR4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین الان پاشید یه جوری شیشه‌هاتون رو چسب بزنید که ذخایر چسب کشور تموم شه.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/84607" target="_blank">📅 20:27 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84606">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qK9rEw6JLjcQS1iyMbKO4M6Fyf5PYcPKsgAAPY-sjNLewdlCxY_ICRjJpFL3Btj_cxjsFkR9NyGqlg6H1rOk9bP8ofW9J2-8aGSwQyY8mC_73nG-g3twxeS-f_EQ_ezEHRDhHwC9hBv3n6eqZ9K9kIbNyo2W4ML5FA-VcCJG0Ok9dhEGVEbcHhQr6IrI1k7CWdFyzB4p7VvqLgDZUjnBZZb_UbNb_yZbTo_SVRkat-AhSvrnpvVzuNBuLkAUZ9LaANkS9ug_mCmn7wQ3nWd-v5vG0gjhleer9AnqlvwETZ93eeW42W6INxqFVhuYB8Arp2bk2pP-Vh6I3uiADcn3ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خخخ
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/84606" target="_blank">📅 20:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84604">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d7adN-FTx3lGj4JFxl4NQcaxJF-D4_sIMeuvlR_jTG-QccodH5zr40pz8baCVC6Rx-txN5ex_k9ZrkDOWLzr97xqZsNnKCBbmiThtb8IL0sglaSmJECoC0N9Rg3CKo0M7yow7SRCJi6T7s08C5sHpsLE4N5r3dzJufsfqqBAebkiALfQTDsy_wtbUFxoqvnJC17sJY_SopF7ASFpg09O-VhVkaFaVjpJ5eHjhh_wYfctiVIL8AKq3k5I6NvvYbzvzQBuzysq6vXbaBZMVU-9hHQdDjfBjJi1hmiSPAGowf2f8wmk35X5XXVa_Zu_8peNOygrg1zmOkYxTtsDh19wxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توماج صالحی با رپر بسیجی‌ای که شبا تو تجمعات اجرا می‌کنه درگیر شده.
(به نظرم رپره داره حق پسر ایرانمون رو می‌خوره
💔
)
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/84604" target="_blank">📅 19:44 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84602">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50ebbea01a.mp4?token=DdeXSZP8tESmAkCEltfzW1AlnebCYTs17MtbJXzC7ugG3KTImESPxmnUKi1C-wG0hwAcwMnWIruyoR2b7MWdURK5LR8HHT1k5cdYsVS1t1e34rved1Py7FJHcuiaYHv8rJ7BlK-V8BxV0dNyXM1VVV8Lw-HhQUTLmIS50fSn8fHyeVIDmw9ifW1ksMl4ndShL4OVuJgogCjxFektlOk5moHF5pMEr6woXDXzR20IIeAWW0r_hF2eBdIQMorMN2l3qa1kX54-8LUJEGosVGUaGpZqD_rBbi8E7bv6gAEKY8Tn4csXgB0yOafQsPxzE2g2qmV7bstfTDSAfo1lxwBlXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50ebbea01a.mp4?token=DdeXSZP8tESmAkCEltfzW1AlnebCYTs17MtbJXzC7ugG3KTImESPxmnUKi1C-wG0hwAcwMnWIruyoR2b7MWdURK5LR8HHT1k5cdYsVS1t1e34rved1Py7FJHcuiaYHv8rJ7BlK-V8BxV0dNyXM1VVV8Lw-HhQUTLmIS50fSn8fHyeVIDmw9ifW1ksMl4ndShL4OVuJgogCjxFektlOk5moHF5pMEr6woXDXzR20IIeAWW0r_hF2eBdIQMorMN2l3qa1kX54-8LUJEGosVGUaGpZqD_rBbi8E7bv6gAEKY8Tn4csXgB0yOafQsPxzE2g2qmV7bstfTDSAfo1lxwBlXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی رشت رعد و برق جوری میخوره به دکل برق فشار قوی انگار که زدن
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/84602" target="_blank">📅 19:28 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84601">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">با اعلام رسمی سخنگوی قوه قضائیه، بی‌حجابی رسما جرم اعلام شد!
از این به بعد در سراسر کشور، با خانمای بی‌حجاب برخورد و براشون جرم ثبت میشه.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/84601" target="_blank">📅 18:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84600">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">هوا الان یجوریه که همه تو خیابون فکر میکنن شخصیت اصلی داستانن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/84600" target="_blank">📅 17:43 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84599">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">حالا من که میگم استقلال یکی زده به تراکتور، ولی ناموسا فوتبال ایران دیدن نداره</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/funhiphop/84599" target="_blank">📅 17:37 · 16 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
