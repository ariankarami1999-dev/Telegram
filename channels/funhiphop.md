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
<img src="https://cdn4.telesco.pe/file/QaoBuVEt99TBzrx6dV-H0yO5HdA8xW7baC-_WwLhwodXWBpHTCyZILZFrbxYwmldB2jwWKjTmOgGXLovN5UzrxMqPG5oJbWwMjRgXnnVy6D8WzIWyRZyIG6z87rNv5Bu2SmxxhctnfZhvdLdEEh-jr_Ob95MdO-lgCPHE-V1f822Bl6A0liuAbiA7RaaWhfIMRhZf1PnEKULEYxLtT6fkLjhMZ6OIREXOkalBAZ6Hbrr7wQcdgpgxuA-fYmxqNvXtWIQbTSi9dwwMRG1hFWuDYa4DkrptynwXXUZrGZ0rjV9_boP5GJzjyiTVmeQ9HPmignyS6-veLKQ7WMeERPCoA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 170K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-29 19:58:23</div>
<hr>

<div class="tg-post" id="msg-78259">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Offc9nsst3g5qbCEokUWAW0ETT0YgruT3k2eYp8oxpSik3p2k_rpxz4hAEOXD_3ooysol2GEX-m181QxWx0aKGv3Xdd26N8ZrU7tZ5la-iNt-WUj-awZ4tXTJzi056OI3GBlHtDMDLhhBbRtqKw5J0gWlRt7j0JdTBpXkHsh1JWgQTnI52ymFJAWDacf0RU8eshNDH0h__0k_plrQNDKDBSr-5N6_vhY6FowMXEi5y8Z--NrwZf8pikl8T7vPjMYioOQCF751c2NXFPTWHP8I7PqNhsoiPT_hLSxb0lbqM_VqLG-8-Y7qnD6YcYnJIrSFXyWt2N6KvgMoI7cCG9vuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید شایع به نام بلاتکلیفی منتشر شد.
Download
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/funhiphop/78259" target="_blank">📅 19:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78258">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">شایع ترک داد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/funhiphop/78258" target="_blank">📅 19:01 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78256">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gTQARp8KE_y7dbdJkNq01OQqMly6NYsXgyI7WG4OBhJYODqn18n7P3Kn_neLskwJmKz0DcU5X0Xn7Ly3R3sOuVjVpTbwZ5QFc9aSUXMRqgT77EYPnZa8d-_CBYyNpqwNatmvkmsCBer11DnErKPw-yDkifXbSVXOxt-umVauICW-MFH-2ZyyhVae6uEVfWOxcs0QNkS4NK5kaFJgcOUcg9K4Kw2YOKczwaYyOyenHC4YhBCuDKzKXfqL-whF9xaka3Nvoyp4lT-DpWP9i-pw7oolCz_6HVjaAM1meo1n9WKASkChHmm4HsUuKlHqXEViFiTpq7uyYf9xSNzJngYJdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حنیف عمران‌زاده: یه شب تو باغ با برادر خانمم مست کردیم تصمیم گرفتم از فوتبال خداحافظی کنم، به خانومم گفتم یه پیام تو پیجم منتشر کنه که من خداحافظی کردم از فوتبال، فردا صبح بیدار شدم از تصمیمی که گرفتم پشیمون شدم ولی رفتم تو گوشی یهو دیدم همه واسم پیام گذاشتن داداش تو ادامه مسیر زندگیت موفق باشی، منم دیگه مجبور شدم از فوتبال خداحافظی کنم با اینکه دلم نمیخواست این کار رو کنم.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/funhiphop/78256" target="_blank">📅 18:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78255">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9eBzYif42E4kp34bwXPpcKL_EeeKj0miAi0pYSg2EpaQP-okfzQJBSXqz0c9TNuALjvIRYJue1tqstBvYsjPunfbODKuITNIlePhSlLZ6cdYmiEWeCzfLyb9BoTO_cRpsfhnHzxOUuH7QI2wSKGs5fLydRrSnLux2DZyQJXnf4KEOJE9mOzSSnXrKyZnxE7wltnE88Z8G4gkqZu0opZM69A76hkM0Dc8nVFGk498V3csIbsAx2NIyo5epee5d0aNdl5jV6Hy2C6wOOMGeez6Hnti6sYrbLYe2aPnLwiKZ9q50HvOS4cNETkEzkA3PVPtMNjFiQOWRs0-pultdYU5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من مردم.</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/funhiphop/78255" target="_blank">📅 17:57 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78254">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P9pFfjXai5SMJo61nJBQEu3eXAoW3cthNBWqAiZOAZMfm1qZQI0_xujh0cC0klNb0GWs5wJdGd237z4rcBcJB5HyVgvqJXD3X19DgTDFa2EELz76q0baDYuRjKDitJ0WLcP5bmfcuaU5VOpwHoFBSTynXVu53rnPk3w4jcpe1XitnXRfLyIE9nDv1iTyVNWey7o4yYJa0tToGTAI29irHHUVM5RSpWbt9Zu7OBRqm70iHz6IO_YcwfWkGkZDm0V9S8QeerMKjMuHDeBxJE3ViTeODnJ0Ah1ODESFVEifG6-GHspJa1WgJ6NzLb9yDA4C0DSpLZV-sK3rihW6Wt6nMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من مردم.</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/funhiphop/78254" target="_blank">📅 17:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78253">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">جام جهانی ۲۰۲۶ با بری بت شیرینه
🔥</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/funhiphop/78253" target="_blank">📅 17:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78252">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🎁
🌳
جام جهانی با سوپرایزهای بری بت
🌳
🎁
⭐️
تورنمنت 1،000،000،000 تومانی
⭐️
✨
شارژ اضافه
0️⃣
1️⃣
🔣
برای واریز کریپتویی
💰
🏆
5️⃣
🔣
کش بک روزانه ورزشی
🏆
📱
همین حالا در بری بت ثبت نام کنید تا بهترین‌ها را تجربه کنید
✅
G29
🅰
🔴
ورود به سایت
👇
🔴
https://gfyweuuchsa.shop/fa/affiliates/?btag=914641_l303106
☑️
کانال رسمی ما در تلگرام
👇
☑️
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/funhiphop/78252" target="_blank">📅 17:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78251">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dZR1PO7G2rta2Jgy6ytfRGkEaoVBXdKO3izzhS1gRZY6QXy123Rg7K6KZTzbnrplPMc3UIswIX6heg1_-pkAx9gfB1LiIc-hjacK8DlFVsuWwNeq0H_gnFZz4MzfJotgbMtKyY-bsiY9mRJO3sjjI_M2Ka5GEUYWIrjEBpBFiIvFjArU8EclHtCoO9XSv97mQBlhEu-zng8bhfzhBoZ8zkA0te5Waf_Ex2mbUQk5r8Xh_A1UpjmNbY3SnIRIvJK0nP44BcpP6WUO9KZDikHeR2hy7OHlhP7LYW3OegOO886QYYq7mDQsZgcoWu6uw82l7pHFq6pGZstU5CqExfeywA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ژوتا یالا از قبر بیا بیرون پاس بده دیگه
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 7.46K · <a href="https://t.me/funhiphop/78251" target="_blank">📅 17:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78250">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NnO3i1rXeM1pbj9aocaTYwqe47gBYrE79kheNhSW4nUcuBoVa3SgHWBeSIkkrEqdlVORRjeQULWH1JOYXf52VLYEt-3pW7gVAowt3HgwKPtv_dwnIc3XxD_Uwp1k9GiXZbqJXkqmBCEiAJSjEjVBTLMZnVa1D0ypLKoZ0KTHkTAdbQlDvFfveGgWDquWytsfZF72V9f_VyAex4Fx1IiBjW4WE6THTautqMbSaP8XnG9OhPhHHVEszGrRaUs7U24vo0z8qj_bFJ6y89gOAvWabXgRLlMw-eRDNkNBfOBp6qM7Ukt_IYuFDCw1DZIEPK3pIN5h9utlKN0OWeoj0oMh9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مکزیک به عنوان اولین تیم به دور ۱/۱۶ صعود کرد.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/funhiphop/78250" target="_blank">📅 17:12 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78248">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sfvfNjp3TTV64OB_EjswTRdHy3mNsR2iOOTSn2sYWD5DqKP8SBj2zztAwQDA643DfSBt1WaBVrvG23XEQzdcHnl-rwxqUZ3cQPqVptemweYpKcg_hWf5nBS0KHWKW_5VS5Uv-UAweD9wWUGBKwPTYyVDVvQrGCLFNtK1CK4X4NvwqdeGiobpCqHxXc_BmcMBUbM9h2FZOcFCdk2G7njs6CMwCnzYJ7rTzOf2m6CdMLPomhwYVtlqbDjj0TJAsGVwjJTtAWHIAUDaavloErBF1iMbWMgfsTHceNPHwJuDiscCTh199wK-buoEx-SqmBB3IcjclE-lEcB2K5Hsic25og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در واکنش به لغو دیدار فردا و کنسل شدن مذاکرات:
«ما از روی استیصال به دنبال دیدار نبودیم؛ این ایران بود که چنین درخواستی داشت. آن‌ها تمام شده‌اند!
ما همان مهلت ۶۰ روزه را تا آخر اجرا می‌کنیم.
هیچ پولی هم دریافت نمی‌کنند؛ حتی یک سنت!»
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/funhiphop/78248" target="_blank">📅 16:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78247">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LUREKsdi9BTa20ZGwQ5WNzqX3QETw7QNce9s3u_cNNDS59i5BfZ7Ek4ZUQKLSuubiME9b6lZgU-sbHeIsTG4FR0MSdttEm32XJTVOpZg4mIA40M2jQiFEVEDOKiL4gf83y08zMwI95Q5k9N-QdNGFh7IgmKRjL0VMPOulb6DKt_ETh6dVf-AVkOAYZv3GcyE6akZvjG1wcN7bz48LMsnLzWB0EeN3OXwNfyFV3LFCSRHiLPf6GX8S0Pf0LMK-155Qmxk3QqrHv-0PYZ8p6FmGIIR-BU_TG-MK_l3cN7HHiLCgtE1eOkdYW8YZ1Oe4i5YFo2rjUbZbquRNbBmhdeq3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلبوم جدید بهزاد لیتو به نام "Late night drive" منتشر شد
SoundCloud
Download
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/78247" target="_blank">📅 15:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78246">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">نتانیاهو: دستور داده ام، جنگ در لبنان با تمام قدرت ادامه یابد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/78246" target="_blank">📅 15:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78245">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">اسپویل از چند ساعت آینده:
ترامپ میاد خایه مالی میکنه و میگه اسرائیل باید حملاتش به لبنان رو متوقف کنه وگرنه باهاشون برخورد میشه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/78245" target="_blank">📅 14:46 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78244">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">سپاه باز تنگه هرمزو بست
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/78244" target="_blank">📅 14:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78243">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">معاون راهبردی پزشکیان: تجمعات شبانه باید جمع شود. آنها سلامت روانی جامعه را بر هم می‌زنند.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/78243" target="_blank">📅 13:05 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78242">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">مادر اشکان لئو رو گاییدن الان تو کماس
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78242" target="_blank">📅 12:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78241">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kABgFYkt7yQ0mUnUn83awhITkBfu423t9waadZxRK_8GDAorcW6SsK2i7GPcSk-2o_g6EMoXoU0TwDADjf08fFD-8_u5AnxR_fpvWWCY5VaeWz5_wfV18XExTLEMWhIrfSQqgD051Eh16Bphi1I1_nIz6umG9wzNvtrTH_uwh0DKuTxun1iji6K65nkgCYtx6N6NWzNZvFLH1pF_VkgG7-m8nfKPN8L63WTPqmqZLDVW3Ek9BXEXaXg9pZ8Ocdcfbgp3QrtjbJMFUzrPFbQWHsXSR38hLtxDuzonoHJxEGx-0kDcVzdDV8a4VWOBBUx2K_ri05cuPGa1GgHPM_UtGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهم ترین دغدغه این روزام اینه که بدونم این یارو پایین تنه چی میپوشه میاد جلو دوربین
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/78241" target="_blank">📅 12:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78240">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">جنوب لبنان چرا منهدم نمیشه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/78240" target="_blank">📅 11:50 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78239">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b546bT_-TiaZ4vLlz82O_mq6Fs2hiJBYsaKVX76W9a00WDUMZ7T3s4lWa4HdUvBsh0L8r5lrTrbaElvyLRlKMoFEoHOZx1Tf7-CVq9OYW3Y4ERi-XSngwGt5H7IsdQsTPuOxUKmmUbwKQqERUUinyzNZLwF0bWEFr0R_S8sHV5_niNjJUhbCwZy925wiF5sEyWq1oe-g5ET8mJIz0IWxRGbPyHgvEGvdrv2AG3F17ZP4NEb6YdZ3qKL27lMDWEulgCpaZBdFuuyD6Ob5R51ELbzDoCVKJ0mGLjPJRGHRHLeR-eQXaKwOSCQBGItcq3LSYhQmjaIK7f153a0V8plaOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبلنا که ترک پوریو میذاشتم آرشیو تو کمتر از ۲۴ ساعت بالای ۲۰۰۰ تا فوروارد میشد، امارش تقریبا یک سوم شده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/78239" target="_blank">📅 11:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78238">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7wGi5ZtL15kd4buEiDMFwbkfLPWWAfmYJjQNsnT9OrzyNWvxR-hG7sllFkjhgvvPMonVqFqBwk5hQKpiVq8Pahnd2b_oeZ5usMn-OhSAFK06OeMHU_YE7W8FJFE8mUv6A4x82e3UNI-a8l9tN8hBbimYCuw2buzbQJZGLYkZgWCihM4pU-wNQPkSRBS_Iv0fIr5SH20gMS1AzrDx7-IJmZpzp9-ugF7zojPbC8VWK3sdLDqB7CPmTv0KvK0xf3JL17YfaiEdk5f2se2Dj9zValsH30HZDdPLIAfB7qzlZP_AljbTMdqOSq5Yt2trh7_LgTlWBcvzV6p6Tav7vZsZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقای مادرجنده
💔
آقای مادرجنده چقد فید شدی آقای مادرجنده
💔
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/78238" target="_blank">📅 11:37 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78237">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/78237" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکشن رسمی سایت دربی بت
🌐
DerbyBet.com
💰
امکان شارژ ریالی ، ووچر ، کریپتو در کمترین زمان ممکن
🔥
🆔
@DerbyBet</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/78237" target="_blank">📅 11:37 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78236">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NkCKu_I6KOmaOf1wx2D3Ny1wnURQtbhqGcKvKHuUwF3AQiO4D65AjTmL56qwoxavPJQs1RjBKi-Nxp5GhQPqicianlkUUnhJkRQoMrZUKx6ItjYM_LC8TmLbaHJp38aRL94g8gJ8nAkPorA4SWdcf0IbH6GyZEX2CgcQs4R7oHAPhSaQgSXqL40l4yPeJ3IbI7CaAT7shTR91QRIChfWss2eHe3VHJMPlvR0NkODo4YsNIGchx5ZueFigd8uJVA8A3CTMfacZ9zhe1szWdvKA1Uu8cpfbhR67HWVUSx-iMwvPwZ6jEZp_0FImr9AnWUIXHj7usGbfGFXo95cXIxKvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دربی‌بت؛ جایی که پیش‌بینی فقط حدس نیست، شروعِ بردهای واقعیه!
✅
با لایسنس بین‌المللی معتبر، وارد زمینی شو که حرفه‌ای‌ها بازی می‌کنن!
✅
آفرهای خفن ثبت‌نام در دربی‌بت؛ فرصت‌هایی که تکرار نمی‌شن:
⬅️
۱۰۰٪ بونوس اولین واریز؛ شروع انفجاری
⬅️
پشتیبانی کامل از همه ارزهای دیجیتال
⬅️
درگاه ریالی و تومنی امن، سریع
⬅️
برداشت‌های آنی و بدون معطلی
⬅️
پشتیبانی حرفه‌ای ۲۴ ساعته
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
✅
دربی‌بت؛ بازی کن، ببر، لذت ببر!r29
🅰
✅
https://DerbyBet.com
📩
@Derbybet</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/78236" target="_blank">📅 11:37 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78235">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">سوییس کنسل شد
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/78235" target="_blank">📅 11:28 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78234">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ولی سکانس به درک واصل شدن حرمله >>>>
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/78234" target="_blank">📅 02:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78233">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">دوستان کسی از ساعت دقیق پخش مختارنامه خبر داره؟
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/78233" target="_blank">📅 02:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78230">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">فردای شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/78230" target="_blank">📅 00:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78229">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">اون سازمان دریانوردی که اسمش یادم نیس: تنگه هرمز گشاد شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/78229" target="_blank">📅 23:59 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78228">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">تروخدا وضعیتو المیادین: هیئت ایرانی به دلیل ادامه حملات اسرائیل در جنوب لبنان، سفر خود به سوئیس برای مذاکرات را به تعویق انداخت.  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/78228" target="_blank">📅 23:57 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78227">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">تروخدا وضعیتو
المیادین:
هیئت ایرانی به دلیل ادامه حملات اسرائیل در جنوب لبنان، سفر خود به سوئیس برای مذاکرات را به تعویق انداخت.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/78227" target="_blank">📅 23:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78226">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">شجاع خلیلزاده به عنوان مادرکسه ترین موجود هفته اول جام جهانی انتخاب شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/78226" target="_blank">📅 23:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78225">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p8Wzv8JxOwF6wo19FS0-EfRdP6NfJrT9W1PYvQmtKVNu5xVavltPNOFupRp5qUPB14ZkAviil9ts18Lui7rq01OsqoW4mbnpkgU1HPBHgic8i867Ph2TwSGDdylyQA3QtLXNe9DHEsZBU93xYXNTtiuf9cNGpy3JJ6XIHJ8N-WvtiV_qy5ThxeEeHzbXEG5HJwAChFPREsB_aqzCFYUMli3uABaWb1VWOcS0pFoJtYSnsgnyPlUgUkBSoc7gYDy3uPTUhUjT8TTbcF9usXd1GmHmBX3HmJtHuQ4kmZDkNYGUBfsIK8fvM9Sl2CoO5uCLrfECveQAxNEl2-fX8C_7sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینستاگرام چه داره پیشرفت میکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/78225" target="_blank">📅 23:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78224">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/78224" target="_blank">📅 23:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78223">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWeera news | ویرا نیوز</strong></div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/78223" target="_blank">📅 23:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78222">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T0dbDCnFKlRzZM9dBBPXpFwb4N78pP5Td5ClvQ2wLyqJ2uBf_LRpypvQtfcJ_DcgEIs2M3CFKZRCBeg3AFC6QjmM7Zx-zHW1ADwjrAHRJ-mzDYIJTodHUk1c3kYP1xgJZK-iSRcl4NyI391ycKO8ADABntLaHYydy8z89HhIpGLYxjzhPIi2os1wlzUuIZHOTZZphbDER66I5hBZak8wA_cXOYwNqmnrTRg3skE_4mpxgypG3F8PuqOn4m8olxE_tkm3ynCK4FZXdT1-NZ2lWpgGo18aSpPufxK1_DNymw7IuLuAkTqJaNynoWRaNHbT4cJbAN0xRFrSLr49eiXR9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون ۱۰ نسل قبل یارو نسل کشی کردن یعنی این دختره خوشگل نیست؟ خار منطق
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/78222" target="_blank">📅 22:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78221">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">خب حل شد</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/78221" target="_blank">📅 21:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78220">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">شما جنبه افغانستان ندارید، بزار یچی دیگه بزارم</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/78220" target="_blank">📅 21:46 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78219">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">پوری کیرم دهنت کاش خایمال نبودی</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78219" target="_blank">📅 21:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78218">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">تنها کسی که میتونه برینه وسط مذاکرات تندرو های داخلی ایرانن، تحلیلای مرادویسی من‌باب نتانیاهو همه کاره اس رو جدی نگیرید، نتانیاهو خیلی وقته قدرتش تو لابی کردن در آمریکا از دست داده و توهم اینکه آمریکا سگِ اسرائیله هم از تفکرات رائفی پور طوره
ونس امشب یه حرف حقی زد، نتانیاهو بدون ترامپ و آمریکا(عملا یعنی بدون جمهوری خواه ها) هیچه.
تا فردا صبحم لبنانو بزنن هیچ آتش بسی نقض نمیشه، ولی تندرو ها تنها کسایی هستن که میتونن کیر کنن تو توافق بین ایران و آمریکا
اینکه مجتبی خامنه ای امشب همه چیو ریخت رو پزشکیان اگه نتونن جو رو کنترل کنن میتونه استارت یه درگیری داخلی بین موافقان و مخالفان مذاکره باشه
تنکس فور یور اتنشن تو دیس متر
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/78218" target="_blank">📅 21:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78217">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">پی دی اف جدید مقام معظم رهبری در کمتر از یک ساعت دیگه منتشر خواهد شد  @FuunHipHop | Farid</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/78217" target="_blank">📅 21:07 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78216">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a862002bab.mp4?token=jEnBp1r-iYifrP8gwmVyg9zWeCCAQhFAZwgRqRimdhSt-yoelELdvkNV3n08C1Ltbh6NOdOXYdcLrr35Hpl2fgU1A9zZLOkmWSofGcKHe1rm6uolej7fLf9AzpSmlyX3BIxSie2oWpmZD8koSbJe-XsaRfJcfya_gSjE0cIhEWTjMyW9HEKehFkI9ezyVHag53CLewHaQaxFs7yUpVAK0LuYzOtLI3GZ9breIkPCo916w5HGRxaTbzACQo5o3xrZj692CTQHv2c0iIrb7Pn_STk9PGXeteFuoySc_IF3-j8VdSAWjmm5kSCJWSGrqH4ukJfbiDDcF6bLad0ZBZfsTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a862002bab.mp4?token=jEnBp1r-iYifrP8gwmVyg9zWeCCAQhFAZwgRqRimdhSt-yoelELdvkNV3n08C1Ltbh6NOdOXYdcLrr35Hpl2fgU1A9zZLOkmWSofGcKHe1rm6uolej7fLf9AzpSmlyX3BIxSie2oWpmZD8koSbJe-XsaRfJcfya_gSjE0cIhEWTjMyW9HEKehFkI9ezyVHag53CLewHaQaxFs7yUpVAK0LuYzOtLI3GZ9breIkPCo916w5HGRxaTbzACQo5o3xrZj692CTQHv2c0iIrb7Pn_STk9PGXeteFuoySc_IF3-j8VdSAWjmm5kSCJWSGrqH4ukJfbiDDcF6bLad0ZBZfsTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نظریه داروین درمورد تکامل انسان
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78216" target="_blank">📅 20:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78215">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">محاصره دریایی تموم شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/78215" target="_blank">📅 20:36 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78214">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">پی دی اف جدید مقام معظم رهبری در کمتر از یک ساعت دیگه منتشر خواهد شد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/78214" target="_blank">📅 20:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78213">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wbze6XUT8Z7JLpo0KcR5_h_CO60t6y1Q8yvcobRVbYfkNrY6NB5PRMKOsinEWyXyL0XNIzZ0ZQzOvJRjbxihlvVfTzGJPRiCnZ7Q00h33pZMfXPyzsf_5WDcAtTyxKipYxvzoyi0rPyiif9wuyhWzBSKhTqcKk-iDgQwWWt2arX7Y2pb6weenII8kzsVUo57B9JdTMhso8xfngdLTQN9wcVL73RCV4eiolVESxhO_6eS5m8RB_IWaXuXDt-QEj57FyAaXrNm5ryYjm_9allpVi3deD3tAUBRKlONQ9jTJI-gI5Qcvmaa5pVGKFbkztWw0hrGJIU3t2fZx0m5JClqfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تتو جدید ممد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78213" target="_blank">📅 19:54 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78212">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pOnYsgwvpOvcQBVZWQu7ois-xJWK_m3wRKVglW7S6lLYsXrhZ22BELmQ7E2YrMihq9RZv4bOm4RxZlEjTmCGU28q_Qc4iJejXmk4wxXdkKy9B3LHfJs1WqwAzySpKrb2bXhVZp0mCl58MLNZgPXI8hwWBiIGZM1Qu1qRj09tvpDHW2SyiNh4WHeVSgKE9JP1aopGKuzlYiDxeObIjQJd42_RVq_1dn3vUPytsA_kT8Jx4qb_o5PDiKoj4K06VftsuoQ2Ij7j9zsd49nwOjvllnT7aK3eLqdRbPX6Zis3nOL6rLQeHrJNDPcfmWXCF2qdHkTva_Q-pwZIoJ1lIm3IAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری عماد قویدل برای پوری
@FunHipHop
| Behi</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/78212" target="_blank">📅 19:46 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78211">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dnxqjzAWXNWZuobcQtWMrx2ZrQlzm5MmfO8VFWoOzuojPiWpBtJqEquSN9DTvuas-O8BM_P1L3G5JyMF6zO1aS2o0q1XKajMiyXFtU8ur8NOM1EMLh6ZqfuiTS6saDz4rhhAiSwpDiSMBf9-yP3f0Zl5KBsP4bScSTJGBMp-nAtxLGrOxQnwP4nYfG24Mr2SuCIrfrX6Ivgqe1SR6IeCvHDFON6wGj6Ep_mDjgefve7lu4tWQ7KQy8vvkhz_ecUWaK6o9wcWDuDinFIAkA7xK-AEwJ_6rFP-NWX28OfWMB4vPC_acWwYxkGN_pXlXwsjdXvDD2xoMc1XTqhWHFVFoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">4 کامیون ایموجی خنده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/78211" target="_blank">📅 19:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78210">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">تیم منتخب هفته اول جام جهانی 2026  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/78210" target="_blank">📅 19:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78209">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iTg40hfC1Y7-dYew-etsBdzOa9qhSybEbnJnsg4UjlFuVGnpI3L8zKzaE8TPFk5-mrDSFlTiO0euDS5lZCWM8LbYunkLmwHeiB2zYH7DKa1ReaoJM_56tnHGCK5QNOnQaCUF00pnUaap2_bGl2b-rMYL3OBMkic8lsrSBJpuiUFhGObY0BMxv2HyY7qgM3bw0VvLF1HOH1BwsQM6s89k2RKKgJPhYIREEeLNn5xmHWmMcgs75_mo8Tp8FUPMLtt1IVfY9vO8N3FYBK5Y4mp1h2_CER7_ZiwJRLaszh2w5VQbqTvYq_B62ZHAjHJDTrf11xH6NahMeI4GVnisAZ9tlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم منتخب هفته اول جام جهانی 2026
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/78209" target="_blank">📅 19:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78208">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qJPG_waTbWqrFUgIPB3Aif1pQzkLlei7XXXJD6QVlwPkZcT7ebOsTayFL7X0tZI_hPN425LOrl5v4pNoeHwDkw2-FFGuC7SqXwIwcNoqbBGkkSXXqgX3_kICvEcEu-y5syz2fkjiKdHPgzTQsgimHejj_ymlAnGbiBNMuroKs3rVtJ8yPskXVqpbvQZ8OBNmkpH2XYQmCiDHjLhLrgQiDCVUXiiN3TOceHF40Oew9Q5pDpZa588RVz1vU98VV1UXttDtKVXqjb57IgnZDCbUEuf7ssAM_R9BpfPAMpvYEQm36GBY9ldHCNRY8XDn2O_A4fgAlUBtanYiVclpEPYaRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چند ساله ترجیح دادم پول سیگار
بشه غذا واسه حیوونای تو خیابون
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/78208" target="_blank">📅 18:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78207">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">گویا پوری و تیمش این مدت توسط موساد تحت تعقیب بودن
🙏
@Funhiphop | Mmd</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/78207" target="_blank">📅 18:23 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78206">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l7Yc_gcyEJvhV-hJ86Msdnxqe934dGYaAqqv6se4lDcKT2C8sheIb_It4oPhKSWDsML2_ikCsJDbVlYlmcgdJ4qZ5Q2TgDLsx44LKSSp57isdJ-zEOPZmaGHzQMKVdY5xP3DlY7IO1ex-4G3x7FhIpatdYHZP_l8lDtLisjUa7YHzFsXJCYmdQ4lZAT2cqjnI2wPF37heQbHiYLN0Z6WMjxzR6UD1Q534aUCxJ64zMDGcjowZmYVz5jGamzIiClQGJaG_ka3nK-tB-nmISoSVop5Jg1sIed4SIOqxWHwVBIvVeUXeXAkQ0dwfbRsiP932E0yUMWpbALbYK8eOg_R4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از عجایب جام‌جهانی
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/78206" target="_blank">📅 18:01 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78205">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLk</strong></div>
<div class="tg-text">بچه بودم دوست داشتم مثل رونالدو بازی کنم،
الان رونالدو مثل من بازی می‌کنه</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/78205" target="_blank">📅 17:34 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78204">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oTMCvMJWfOUrpKscXVRKp2maZ_9HvxzDhoUWf6DXLHBf06OkWucsel-NrAtuL4Eh7hr2C5zo5GwI_tDk5LmgCVwNJV7j8FxlXGg2b4gM_udJRPc1BrYRE1fNggtiaXMcyCb-s_2xcOjOV6Qkb7vsxlcyWsZpDGBsaZNTDGm9Gg17kHWuiXb-Twe173qKGapbYsYkmwn6A8qCZ8lsORyKt1gjEg5GAz0NjPpU47t68zOg0htgtqxlwn4B-BtpL_Ibx7fsJBg-uuGBL1MHYSZx-9gwtlEHg3bJFRl9ui43I3CP7sokp6ld9hohr-2zBEwHreyaQembaLHkbk5K-xRL-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازیکنای تاپ دنیا توی اولین بازیشون درخشیدن
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/78204" target="_blank">📅 17:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78203">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">با ماف بت از جام جهانی پول در بیار چون کلی هدیه هم خود سایت میده
💵</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/78203" target="_blank">📅 17:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78202">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AYZ4HzXo6AZp_NqhHp7rKK5iJc10Mi3da15LGmQ8EXxaSaW6nmFGoBgTNxbAbQ18SFBaHZwadC6x5vFkeBW2_q0SDBLE6xjBardKC8f40HOFsWpo2Vt7pm47tB4qLd8IcbQoCnr1eq9ISJVimx3OmRx8_Jrk7QNiXue9I48DSZfaqL25G_UfIVOp2vejCQruxF5SBtfk1wCamQuSu2ucwaiGdPsd8QaDagvg6vH8kf3ijYtQ_8C71jCQuL-zlTFUR9q_fMGexRRKDaRkhCpJJsxdQw1Bprrs2N9FPza4IlvrWeIFMvzMVYvgjTaA3de52XFWlMDbXq-F4N5ljMc26A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
چرا سایت بین المللی ماف بت بهترین انتخاب برای پیش بینی جام جهانی
❓
1️⃣
شارژ و برداشت اسان و سریع
2️⃣
پر اپشن ترین سایت فعال در ایران
3️⃣
دارای مجوز رسمی curacao
4️⃣
کارت به کارت همیشه فعال
➖
هدایا بی نظیر ماف بت:
👇
🎁
100% بونوس خوشامدگویی
🎁
برگشت باخت هفتگی
🎁
هر روز 100% فری بت هدیه
🎁
هر روز 20% شارژ اضافی
🎁
گردونه شانس با جوایز بی نظیر
👍
با فعالیت در ماف بت طعم واقعی امکانات در سایت جهانی حس میکنید
👍
🎯
ادرس بدون فیلتر سایت:
✅
https://mafclub.online/fa/?btag=260368
✔️
کانال تلگرام سایت: g28
🅰
🔹
https://t.me/+3Zxs6WU7L_UzY2Fk</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/78202" target="_blank">📅 17:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78201">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">گویا پوری و تیمش این مدت توسط موساد تحت تعقیب بودن
🙏
@Funhiphop | Mmd</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/78201" target="_blank">📅 17:27 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78200">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vWIgF_Gy1emcZvdWDGXpqEnpshS9mM5s8lVCM6JiiKoSkxoGpgy4jqupEFrQuHsagQkM9ZtQaFAl3m6zemxXIBoU0SQaBLY0yac1rj_5nwvNnkwrzcWFlo5nxPs004UTPSCg7H0CDp1mwsihzjMgi5HrC5xn-r8JufSo4KCD6chtSgm2VQgHv6MnoXkrm5rR1h0bfA-oMgU7wiGaZ9gDylY6rCngnLoaejwVdhPGod9iExTlB0qj2Jfe83azycNCCOV8RMJUZTOQlE6_guddXxAwyzsKxZd28mgz_m1hpy-j4IbwtelPDLLgzROZ9ZD-Vp6pDvgClG4LhWdsVOOJDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موزیک جدید پوری به اسم سرپا ریلیز شد   YouTube  @Funhiphop | Mmd</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/78200" target="_blank">📅 17:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78199">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rTUMc6qeMyuSOyWAfKmR6BFiIh4GmlECQjkuZPwYM4fw4CSoovZXiaTDUw66WzWEaI3hRfcFB57BIkIlsDGaIgr28bjkhkh3a-si4zIKPssxXvNWrEht_MOucNjyBackdw_x1rdEXplwsL2dU18EW6l8lemw4z-4tDaxuj9m9xVVeuweZGTprXUhTcgWuJJArPnd9vXo6QThfLhIkskyLZbtfqSZCcsXIB8cozDVKr1k0A2HynlP40qSO8tbwUx8Vfn7kBHKa4rMMlpa1L1e-QMdClZV64M5t9laKJqJJ5_lwV1NfGlHQEuzHFhpBb-XZ7g_5zIE3ZxEppLwN6kkpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موزیک جدید پوری به اسم
سرپا
ریلیز شد
YouTube
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/78199" target="_blank">📅 17:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78198">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">وقتی مردم ایران صدای بمب‌ها را نمی‌شنوند، ناراحت می‌شوند؛ آن‌ها می‌خواهند همچنان صدای بمب‌ها را بشنوند. چون آن‌ها می‌خواهند آزاد شوند.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/78198" target="_blank">📅 17:01 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78197">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ترامپ: فقط مردمان دیوانه میگویند کشورم را بمباران کنید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78197" target="_blank">📅 16:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78196">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uTSd382Zm1Raz4X0V-p8G9rqJHSqMhxYs5yZesM6TH_Wz2JZhnntSX9D3l4npo3KiEbGPyIYgw-Vk5kT_fngVE9HIb7Ga9StHUibAgdF8WfuDhy61MDSrAa797zYwzy55DqIUvv3adQEY2-oSHwy0jIJAQm0QB0wHfVcBhSJoV_ncSuf3_ljr1p_CAiFKphChNZDq8i3qjFHKRUErTr2xAyvL8yvhKIRzV9XkxaLutrCzuj6QMHQXgLe4PE5viOFxzmEJQZvniOGXpQcFAvRavoIyDn5duJ3P3jRmtp7QwBR6nBt_NCk5Sd4rYu9yirXB1gR9Wlujm1XPfO4J7C4yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/78196" target="_blank">📅 16:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78195">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KKUo2NzpYLpgKI4vX1uoJtNDMKXN2DwwgFHpET-99ZwH3r8IPQDTtG-bzmYuYMhWQEsTXAvj7Myuu7ck5kJtAgFbDjX0C8z4eRcP8qUAUtrQd39vC0p4Ic_uFFDAE3FBB3Sy6-UeZ3JXq1hOaZwlBhmumTrt94qQY7dMnE87LVprflyth3hEe_jXNhy2dtJeT7SobJ07Ru9AuRLz5xXXMDRjyzgMs2gDETJWd_aN_Uf_Dxb6AqVTcdrTH4PXDDXU4PQtrhsZc0KAQz3G9GxjfocCbfvbUgwnvxtLfWwysA6k8wpRN0iZG7yd7nwLlkLm8qohhe6DbIpnOHJEmvX6Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از سنت خجالت بکش کصکش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/78195" target="_blank">📅 16:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78194">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">پوری میخوام برم بیرون، سریع تر ترکو ریلیز کن یکم بخندم برم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/78194" target="_blank">📅 15:59 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78193">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromuıǝssoɥ pɐɯɯɐɥoW</strong></div>
<div class="tg-text">مهدی واقعا افغانیه؟ آگه آره که کیرم دهن صاحب کانال که یه سگ افغان و ادمین کرده</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/78193" target="_blank">📅 15:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78192">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06ef661660.mp4?token=VEpeZoRD_XcfbmXpj_3yK324_Aej09Mnz2uru9m2IH_UoZedsxKsmGKxuv6_D5rEyon9i7rNBPiLAOXuSEikmN8E3FPyw0ewai8cwtgqNS61mQn1QqbA9E3fz9ZpGKTkIucgzSKhI-nDe2g8svQCk2nVTGittJvSRrHTio1jHxR3HFmZ9HySIFZLtNVlc3H4_wfQ7ytwk6rwm_d6nk6kskeqDZ1_n29wWbIDUIPxY44NzdNaSz3r3ee7szWNRMqMEax5z80C-JOPcb8fp1MAWSlUnEHNK0LuT7OIXXHvUl_l6PnweX97J_0kENm9XXvKSDDDQWVj8GBtLgmjKw4aNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06ef661660.mp4?token=VEpeZoRD_XcfbmXpj_3yK324_Aej09Mnz2uru9m2IH_UoZedsxKsmGKxuv6_D5rEyon9i7rNBPiLAOXuSEikmN8E3FPyw0ewai8cwtgqNS61mQn1QqbA9E3fz9ZpGKTkIucgzSKhI-nDe2g8svQCk2nVTGittJvSRrHTio1jHxR3HFmZ9HySIFZLtNVlc3H4_wfQ7ytwk6rwm_d6nk6kskeqDZ1_n29wWbIDUIPxY44NzdNaSz3r3ee7szWNRMqMEax5z80C-JOPcb8fp1MAWSlUnEHNK0LuT7OIXXHvUl_l6PnweX97J_0kENm9XXvKSDDDQWVj8GBtLgmjKw4aNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ریچ یک کانادا و حومه
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/78192" target="_blank">📅 15:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78191">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">راستی محرمه، پرچم عوض شد</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/78191" target="_blank">📅 15:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78190">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">انقد همه پرچم گذاشتن جلو اسمشون منم تصمیم گرفتم بزارم
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/78190" target="_blank">📅 14:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78189">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bFzYbJ94KeDhTK3Uk54IfktNxxs4lY-jyWVcT1wNeOg-ax4xRy5h4oYc_QBH69qTDIa0obvVD4cAJTO29bcrzyX9T5Z321TzqJw4xJ-ujzM5dolNmrJln0zspwcsYw3CDfRuys1MDHTHt6QLfnQMG8s2FB3GH-Lyz8Le5LDIvOYU8zZVwOlRAK7YC6jKnkjXdgeRwNK_-Sum5_jkxM8cHUJNsL9wpI2zxp8hQ321UetMLCcVRnY_OP8eRUtbWvZi2DBOyZmW6GWvXU_iIxud-5LkHc8JutOhpEg2fpapCBKLAmnGcZ3wvIJgYQzERjQabPj1qddAZCQKGKpBb8MdqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرامپت اوردم براتون که توش میتونید خودتونو درحالت امضای توافق با آمریکا قرار بدید
پرامپتش:
A tight close-up mirror selfie, black and white, grainy backstage aesthetic.
Subject 1 (Foreground): A young man with messy, sweaty wavy hair. He is wearing a tight superhero suit with a web texture. His face has realistic battle-damage makeup (cuts, dirt, bruises) and he looks exhausted but calm.
Subject 2 (Right): A girl leaning her chin heavily on the man's shoulder, snuggling in very close. She is holding a small retro silver camera directly to her eye, covering half her face, smiling.
The lighting is harsh and direct (flash photography style), creating strong shadows. The background is cluttered with a hanging white t-shirt and messy towels. High noise, raw, candid snapshot.
‌
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/78189" target="_blank">📅 14:06 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78186">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">کصخلا فریب و فرید دو تا انسان متفاوتن  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/78186" target="_blank">📅 13:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78185">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">کصخلا فریب و فرید دو تا انسان متفاوتن
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/78185" target="_blank">📅 13:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78184">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tLkMwcTgeBhnxI9x6spLo3SSo13ME-TOyjFIka24kmpRDritVilb9g9QglERSFxSX15wfYNU3vkFYke6jwp43QfY4eI1dEPoq_6T1AvM68k0Dm6kHcaDWJzJVo5tm-FHx5wSe89RpUwvTvw3N9kKZXZJdjFkMJut-7fMoIC7_OYzql03hysP76ERD1PigDGUe0OEmolkFEJnZRi-Pi0-8ASq77IRLRREKkSSRd04jgGu8mmMSgrW1zUMn2r8dJd70nKytltynWGEX0tMFLBUCLY9V0qsHLT42iVZdf1duv7UPc0QVV_cPmJySeMSeYJIg-HHQccyH_XUfenqtUSySQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/78184" target="_blank">📅 13:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78182">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">خب دیگه توافق هم امضا شد و مانعی برای سخنرانی مقام معظم رهبری در ملا عام وجود ندارد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/78182" target="_blank">📅 13:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78181">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ترک جدید هودادکا به نام Best In The Game ریلیز شد.
🎵
SoundCloud  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/78181" target="_blank">📅 12:54 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78180">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EzMzLJnSHPzgWxRnLQ3W0Aei3mrtCg4QCzZ_SdTrWY100pNE7abF8znRd-A7bHCIlnZoGKSphoDHKpv8Aas4bQ5oREh02rd018YcA-Z0yGVFX9_bQ-WM8GwCvGST3bN7y193DH_1hN82bg4uUdash-fywj_EZBRnXVEAac7Wrhz0Mtrk_dk7Pk0L33EkFkbqWsEK5HaG8M5wfIgE_mZ6CUSIVpgMl9mYrp0CxMIZRnoRQhCEaw1jl6YG03WK5ukHJhskrc4u0kZFCkjZnG0FgrfR_PtoV1wCouC5QZGZXZSvo2DC9aY5_Dfjc-6tAX6I9BRWsui8_Ug0YNkYIEgqSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عزیزان ببخشید من یه لحظه حواسم پرت شد این قسمت از بازی شطرنج مرگ و زندگی رو از دست دادم، لطفاً راهنمایی کنید این چندمین تاس ترامپ می‌شد؟  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/78180" target="_blank">📅 12:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78179">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">عرفان چطوری میتونی انقد کصشر باشی داداش</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78179" target="_blank">📅 12:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78178">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">آرتا:‌ کصه بشینه نمیره عین جمهوری اسلامی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/78178" target="_blank">📅 12:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78177">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ترک جدید آرتا، کوروش، ویناک، عرفان و کچی به نام میتونی مگه؟ منتشر شد.  Download Spotify  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/78177" target="_blank">📅 12:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78176">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ترک جدید آرتا، کوروش، ویناک، عرفان و کچی به نام میتونی مگه؟ منتشر شد.  Download Spotify  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/78176" target="_blank">📅 12:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78174">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q8LETRiQc7n8VqyZ2Lz-jpr5qbPnp7M7XtdFMDL_wDMlxkBSxMTtAi4Rd3CK2t_PA_6vzd3q214g3nPMkaCQgoaXadWR0YJJExN6FJlyWECvgfd60A2vFG5TnuO2IB4pp0jqkJm38_jbHwDZluVkhdqq09w9kZEJ08gnt4IHku4vs3iT9jgW-kBIrMkroSqUNL-OqDSQhKCEn-SQNu3eV27F8RclnYXmvbsHtU7yNk2SFYH1fyhUX0awTAaxF2piylZXF034OoQGUMhrpMN5kySWnDdXf5YFh6ZUL3I7mhh-1PJ28uT1aGIF-4D9AD5eAf6zu5hua6_9U7FBYwWGTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید آرتا، کوروش، ویناک، عرفان و کچی به نام میتونی مگه؟ منتشر شد.
Download
Spotify
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78174" target="_blank">📅 12:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78173">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">آرتا، ویناک، عرفان پایدار، کوروش و کچی فیت دادن</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/78173" target="_blank">📅 12:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78172">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/INq1egpCrIBUZCGAiHCRwPYbOmFu5A9Fj_QDLRz8geDGmOJc2Pv-G4MIgVBhfXTaaCyw67jH6wT604gR-Q2mOsYHY1yBudPTQX-Lc2PDN4zMzbwSAUzA5BTpTKrDHun0-Bn3Rap2nlaO9REILsu6poAPzzbFVJwGCe2yKreA4B4vh21RqbHwCsDkKhTH3Ko9ymMy4MhQfGQiBmpKJKj7nz00bF0HdtQ39tN2b1oIaO67rwqquiRLTgMU3x4eUiglOzNWhqdwh2X68Z5ovTlji_6QldoOFtZQCMaaSjpyOqURml0h1Nmy7WB6KYKRwGU7j4fZyeyMylWkH9W5En2chQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایرانی بدون خایه نمیمونه، بالاخره یه جفت خایه پیدا میکنه برا مالیدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/78172" target="_blank">📅 12:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78171">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">آیت الله سید دونالد الدین ترامپ(دالگخیز): عادلانه نیست تمام کشورها موشک داشته باشند اما ایران نداشته باشد
آنها باید بتوانند دفاع کنند
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/78171" target="_blank">📅 12:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78170">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">رائفی پور: اگر میخواستین توافق کنید قبل از ۹ اسفند میکردین حداقل رهبرمون زنده بمونه.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/78170" target="_blank">📅 11:55 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78169">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">رائفی پور: اگر میخواستین توافق کنید قبل از ۹ اسفند میکردین حداقل رهبرمون زنده بمونه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/78169" target="_blank">📅 11:54 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78168">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">شاهین نجفی نوستراداموس   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/78168" target="_blank">📅 11:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78167">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c40ff98049.mp4?token=sNxc0W-s4nc0c4u5MR3Rqxfq4UK3-iqDi5p9byy_GhKXlFGGgg4MAUCZp1gXtIBQP6kCVddOeEXok3mHRuLGHOdzsvf2G8VsXhW_r52jlTzsMga1wOuPY3yrGzvirtxzDG2r4a3KHuSAxMz7Lwv37JfuLLH0DEH1f3Bcy0lVq1XDhAkULRzxmi0ht4dDuSDU0NDWbuGJf-F78jCXlPedaYtxwXC2dsXvqhBYPILN7s0r9sLhFS_CmCvkMQRVKufcGl-7mGMj5JAi4pGIwyMzVFNYIdvnSNCMX-uPosZmAiZ-jalbYUH_vdb2IVphrSggnnId4VxgnhdV0l_oov8e8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c40ff98049.mp4?token=sNxc0W-s4nc0c4u5MR3Rqxfq4UK3-iqDi5p9byy_GhKXlFGGgg4MAUCZp1gXtIBQP6kCVddOeEXok3mHRuLGHOdzsvf2G8VsXhW_r52jlTzsMga1wOuPY3yrGzvirtxzDG2r4a3KHuSAxMz7Lwv37JfuLLH0DEH1f3Bcy0lVq1XDhAkULRzxmi0ht4dDuSDU0NDWbuGJf-F78jCXlPedaYtxwXC2dsXvqhBYPILN7s0r9sLhFS_CmCvkMQRVKufcGl-7mGMj5JAi4pGIwyMzVFNYIdvnSNCMX-uPosZmAiZ-jalbYUH_vdb2IVphrSggnnId4VxgnhdV0l_oov8e8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهین نجفی نوستراداموس
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/78167" target="_blank">📅 11:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78166">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SDrsFaREi5j_8op8U6t83jlp5JkpU0pgsTjj9VShc3tXpiW4Fu55yoQr27hpecbzu3gSwgiBFfw_0p_XDerh8pjdlF1ETdVd36SD1MMJkQz4mMH0QYSsMAsbqifVOKFicCbN88hXtb-wB7_tqvYfoataDo16i6tG5KwDqwNsffU1YnkRDS2q99VaojpHtGLbHpUJI6K-s8WVCxAG7QhDjaX8rnKoVkMTI9ahRv9X7Na_ja487yt_GQcpjVIMm-9KkKKkX9j2nrED9bD7WB4UeRlQf6BWRgdYi1PFT6b4g2CdP3xzQEbpb6_qZ4LUI47oic82MA3afHEXIhWxVHeQsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین ها درحال درخشیدن....
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/78166" target="_blank">📅 11:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78165">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/78165" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکشن رسمی سایت دربی بت
🌐
DerbyBet.com
💰
امکان شارژ ریالی ، ووچر ، کریپتو در کمترین زمان ممکن
🔥
🆔
@DerbyBet</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/78165" target="_blank">📅 11:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78164">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m9hzj3qYQwuQSYlTsK0Q_mk8gNIpstNwK9Dcw_p-_zRYrFu49OZT92ZsSEzjwlvbRqTEPIw3DlvC5LtVG8RWLqev6QWST7axhRXK4_dd6cdc264bnO_eLFvi7VrFGdNXcQSRmywtGkF_9VYdSwH7pAj3mbUa5Vn1KfIe3tIPUUYyqMauOsDaMY7ozsX6wxHsWQPtM9St3K_XBZMjIGmX3CQ1R9E0_zjFAJk1Gy4T6fk9ScbOKGA0dbv_CvyYmwzxdI2xCWHuvSsK1XwLG4oIVC1vTSnzWys63Hek3N0Ls1gXGBzH9JrmDTHOEL629g-cqKEalFkvu0yVdDVKlaDLNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دربی‌بت؛ جایی که پیش‌بینی فقط حدس نیست، شروعِ بردهای واقعیه!
✅
با لایسنس بین‌المللی معتبر، وارد زمینی شو که حرفه‌ای‌ها بازی می‌کنن!
✅
آفرهای خفن ثبت‌نام در دربی‌بت؛ فرصت‌هایی که تکرار نمی‌شن:
⬅️
۱۰۰٪ بونوس اولین واریز؛ شروع انفجاری
⬅️
پشتیبانی کامل از همه ارزهای دیجیتال
⬅️
درگاه ریالی و تومنی امن، سریع
⬅️
برداشت‌های آنی و بدون معطلی
⬅️
پشتیبانی حرفه‌ای ۲۴ ساعته
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
✅
دربی‌بت؛ بازی کن، ببر، لذت ببر!r28
🅰
✅
https://DerbyBet.com
📩
@Derbybet</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/78164" target="_blank">📅 11:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78163">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be730c80f1.mp4?token=rpvBsCJWDQqjquuC5rfozuWLWvEX8hvfn5-f9ymr9PMUtRKT_gQuevng57D4Xe5kMV3pTq4G7r56gMVH2Aur8f9RfWmbVpnqphZs8c3rZvdAcNehKIQZhEsNCUmg_DfXeTM-zkP7vCxNcFMA0OdLNhBEBWBzTQsl0ufnZvwekHd0igFlsKnuq0X9exU_HIMa15tLCt5V4_ZNLH0AXpEs94QnfJsTvzM6CGj9YtUyaFHzAXIADNGZPrEx8j_dypwRLI1H7I_AH9dESM4S3Kr_B4yCuCIj8x8LZxYlDQdRZJmzExHiH_U1hK1WnGziN8QN1AT58r5dOGbo5j-qF1Xz7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be730c80f1.mp4?token=rpvBsCJWDQqjquuC5rfozuWLWvEX8hvfn5-f9ymr9PMUtRKT_gQuevng57D4Xe5kMV3pTq4G7r56gMVH2Aur8f9RfWmbVpnqphZs8c3rZvdAcNehKIQZhEsNCUmg_DfXeTM-zkP7vCxNcFMA0OdLNhBEBWBzTQsl0ufnZvwekHd0igFlsKnuq0X9exU_HIMa15tLCt5V4_ZNLH0AXpEs94QnfJsTvzM6CGj9YtUyaFHzAXIADNGZPrEx8j_dypwRLI1H7I_AH9dESM4S3Kr_B4yCuCIj8x8LZxYlDQdRZJmzExHiH_U1hK1WnGziN8QN1AT58r5dOGbo5j-qF1Xz7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار:
یک انسان خردمند در ژانویه ۲۰۲۰ گفت: «ایران هرگز در هیچ جنگی پیروز نشده، اما هرگز در هیچ مذاکره‌ای هم شکست نخورده است».
ترامپ:
این را چه کسی گفته است؟
خبرنگار:
دونالد ترامپ
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/78163" target="_blank">📅 08:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78162">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JiOW7ggMJqsHGxbgbjPHdSLMr6s3IZsZiMRbRcL0Bq7iMColBINs43O1feVtoUpuSjsBV7hnUF3qJ8XO4yG_nP5bion2gaRgo1-2AzSq0zA_4lWX37AbWYdsEKqNfJAy1wLj79u2lcTDpppsleYNRszN6fB0Q87sCSYL3fx9MtBF1gRIuVfSjrtTj1w5XU3WVj17oZgOLJowXoIiWjSqgyzgxs29aQhYvxkYFwk6B-_en03QWZUGm9Yl77ihAO7HxqaEKk4JGLe3LbLjP3xNvdQP4mcSQtxjxOTwpSqXceSeyFdY-9wugIGwMEug7dqRckWKTaxpYp3d8rNQXqd0YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عزیزان ببخشید من یه لحظه حواسم پرت شد این قسمت از بازی شطرنج مرگ و زندگی رو از دست دادم، لطفاً راهنمایی کنید این چندمین تاس ترامپ می‌شد؟  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78162" target="_blank">📅 06:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78160">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jGh3SL57wd85y0aWQLOYRKlXW8y2qQMoAHny0ylJpkJ4qGg7-t-ZD61qxk4K01oZU45Y1JUtOp_UNmHVZHWglD0ABQMaJVR9hXDVTN1QVb6FuHBPgnUigzjPm6MwD8p-qCJZbdgYHkstVD8UtY6A1DsdHC4C-CSDa8wRTNhmJnOJtwfKVW70-HSrCee2GYHWH0n4y1TekC4NGFF3Tcuu9oeFWF6eJQcG3mYiEV82uu0W4LFHzEUcR0CrE6NI8Q_jM-r96iWMSd3evjeWU6CauTyd7FIPzZPPTVQVs8XXvTBjBUBriz4FWJGbpW_cXN2q37sm8hpDJdTxuAwkmZLWfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Moq8szIVP2voOxSUC5MuBRDcIoyt97B8xazViY-QGsi7gUw-xcJweH7HthZnr4Ey0vPgrF9mhqlc7ajOOQusiHPI2dXtfdoMF44t61-8Og1AL_3EnIuMyQ644TEl4J0MOCWb9bdASXHBtywmMxGOAB5NayJGChJtvomYChUbrUmi6f-YnZf6AKBLSf6zs_JozAQHG_ESHLoKSLBCMXnqKg_uTL-OYWnxWqFe0wSD7FWSXPRCHEdox5xt4HwshmZtFC34BA7FueMNhwFqTnk_3pnnJQyQNkLyTp9g_HPPC4GXIPuJgNB9KJOUBJgbRtBcXaFEp7FoFN0olnr5yXtAPA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عزیزان ببخشید من یه لحظه حواسم پرت شد این قسمت از بازی شطرنج مرگ و زندگی رو از دست دادم، لطفاً راهنمایی کنید این چندمین تاس ترامپ می‌شد؟
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/78160" target="_blank">📅 06:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78159">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">جی‌دی ونس دو سه روز پیش اومد گفت تمام بندهایی که از توافق تو رسانه‌های مختلف پخش میشه پروپاگاندای سپاه پاسدارانه.
امشب خودش از رو تک تک همون بندها خوند و تاییدشون کرد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/78159" target="_blank">📅 02:55 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78158">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">سخنگوی وزارت خارجه:
ایران دو قدرت هسته‌ای را که توسط برخی کشورهای دیگر نیز حمایت می‌شدند را شکست داد.
ما شعار نمی‌دهیم؛ ما واقعاً یک ابرقدرت هستیم.
روند تعلیق تحریم‌های نفتی از امشب آغاز می‌شود.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/78158" target="_blank">📅 02:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78156">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">کاخ سفید جدی جدی حسینیه شد؟
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/78156" target="_blank">📅 01:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78154">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">رشفورد چهارمی رو زد و تمام
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/78154" target="_blank">📅 01:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78153">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">خب طبق بررسی های میدانی و حضوری تیم من در ژنو، تفاهم نامه به صورت دیجیتالی توسط پزشکیان و ترامپ امضا شده؛ ارزش قرارداد سیصد میلیارد دلار با بند فسخی که بعد شصت روز فعال میشه.
Here We Go.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/78153" target="_blank">📅 01:17 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78152">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">میگن که تفاهم نامه رو امضا کردن ولی فعلا بچسبید به بازی انگلیس کرواسی این مهم تره.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/78152" target="_blank">📅 01:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78150">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">عجب سیو پشم ریزونی کرد گلر کرواسی
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/78150" target="_blank">📅 00:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78149">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">بلینگهام گل سوم رو زد برای انگلیس
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/78149" target="_blank">📅 00:42 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78148">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VC8gruY65DKYUooixEcTNK2lh7L0VqmFsuXBspeQP7YMoSHWz1wlgknzSQdkBtGRQzJ3sKXezr58VwM7EdE-PauP6Ny3RuABZifccj27PbcQqAbfcNArslefAhjfhHHChkvvHOhMnU8lBLhyhw7PwA4o0tjK1R9tZoaATAf-cIVzeQdm-QSxDsTa8ZncW7NdELd_sjs0I9QFkt8XWVTtF2ZRpiE3qX1tGSryUvQ_SkiF6kNmWbNTSZU7oBUjEu3OY1-JlorJU2NmQ1QMUB81v2eHnmRfSFAnORl5Htvy43sXCrCO0TEgZHyAS48dMzlMs_t_4SVxOMoytaVvSppFMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کمتر از یک هفته تا منتشر شدن فصل سوم سریال خاندان اژدها مونده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/78148" target="_blank">📅 00:39 · 28 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
