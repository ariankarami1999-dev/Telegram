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
<img src="https://cdn4.telesco.pe/file/oQEi69z3ULo_fds4nRrRbpvuByIXQ9rDRbpu3m2Oe4BKb5g_7rPCjDN6aaql_y2uuOcF_8dJvI-HxezUzicOda-sPsU-C8Il3XbwWDyQ5GszK99uWSSYg_TKr_N5exytDJ85NwISRTNqAqcRIz2CWRcR_GFNSDAfmezR3JP3CHVWUHRtXWyUl5z3uKxFSQ4-LuDcHk0ZG-MfmV5ghglWRyxbFCXgrBrIIiWUCKMZcUkniYYn8-_JyM7qncouf-qj9WVfdi0vhA3blkGu16wgpfXleqi9gNUIm4gycOGL3HCX2N6FtplN0aEtu6HTPxRRDwLOpKWDJy_tip8tycqoaA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 209K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-13 15:31:30</div>
<hr>

<div class="tg-post" id="msg-67276">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eak7R0FXUkNxsieiZlmub8hdxKF_A3KYB1vRwxeZkK3y46AdcXL3iB0ByRa5z-EeZ2ZN2GZpesVv9qbivqGdeoCZp6gtWimWF4R0BM-mDfk9kGdAAaEosKoRp6XxyWWHiqdyF_617gsfd6C3aiNojYWWTvWA4KgkQfxLiUXvxweUh7-fUFM6qezDrJ7q31sHR-bNn8VhhhT_zjuvvfwJ-Tcv7vvniolgsbZIrgkaohomG0UzFzY-ASXnP_WsJQ50aT8cdzobSt3q-TBlivSMVw1aYPoYQLLvcUZ6eFKAOd_xrA8DrVBYJ99NgzTb5eGFycJpucRE9dqmWu68hMHPMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدودوف معاون رئیس شورای امنیت روسیه:
🔴
ج ا به‌جای سلاح هسته‌ای، به سلاح دیگری دست یافته که دست‌کمی از سلاح هسته‌ای ندارد: تنگه هرمز.
🔴
بحث‌ها اکنون بر سر این است که در آینده، درباره نحوه کارکرد و وضعیت این تنگه چه توافق‌هایی حاصل خواهد شد.
🔴
مقام‌های ایرانی همچنین یک «سلاح ترمونوکلئار» دیگر هم در اختیار دارند: تنگه باب‌المندب.
🔴
اگر این گذرگاه بسته شود، همه محموله‌های نفتی و سایر مسیرهای حمل‌ونقل عملاً قفل خواهند شد
@News_Hut</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/news_hut/67276" target="_blank">📅 15:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67275">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6T4xuzwHyquX2gmfs4tUJjFv9pQ0j59wrnpon7yybAdAL8bO9_YwfR4BPNVr1zObVntL4vI7jqwJkrWsI_RM4Oy7X3SXL47bsUsBjAhLHB5_kghJ-ZnALCCtdXcCxljbQ7wvmnJ9nrE3y7gls6zU9DW54qRiRV3-V6imkepMBXuDFjdHSAX6vVvTyCSvfuPXGrJomKyYgdN6RzMkylrrjX97uDgIjUZymar7c4S6DHvpyFZHX6MesUhu4ho9zyiO2_0eX8QAeHcK1OrKGrc_BRZJz0oglJTWCq9Xw6Eldom4-gHFourw6N2Twp9wYxg7K_Ce7IGTpp9OfFrYB7KOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمال مجازی‌شدن مدارس و دانشگاه‌ها در سال جاری!
🔴
میزان کسری گاز به حدود ۶۳۰ میلیون مترمکعب رسیده.
@News_Hut</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/news_hut/67275" target="_blank">📅 14:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67274">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gBQAoWe53VRAs_nSCpUpveb7Z4tZegMKXHRKAJZ9An1ycGqgpfFS3W3xWFoRibr9cRPHHJ3r7jDmTojekZqpBJompfBka0F5BQXOnXgGIJMjw-QKKQVdeKo1AK1vuqm0d3rfzBaiVEYm66Tc0WiGe9gIymF01ST4hRVnozErrdRwiNlWZU5o0kWSM2CC7aQ7RsQZHnS7ghB3ex0v_k8B6BDJj0XQs5NOge-dYCdZ-in1hlRmNzQIVtFNmyZHfejaHgLttQLbwY2P6h1W4_J0uW_dtfWQib7l-YJmlV1VMGMH3fe4dGB3TaudrywSyMULCLfWojOSjX9D5-GOTEvQ0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برافراشتن پرچم «ترامپ را بکشید» در مراسم وداع با جسد علی خامنه‌ای:
@News_Hut</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/news_hut/67274" target="_blank">📅 13:57 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67273">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2883f7592b.mp4?token=cNzTaMO0Tu0tJQ7HfzpZG31OqzEEKXpIho1Qa6SyG5nuXPJ7aInzwuAhh3Tjf6ThItStYx1liPdzqlRydx0sAN3N-bY2_3BLrVFZvRpcCUvsVipopjZ-WmW_bYwBdDCioel88KIvDPoZv-VxpV-mPGR7PdM14MOJz7ibjuB0MQeoDf7iRd6wSH8MhyiHNnacgoYvo4GyD9SSPUDsPigH4weranspoMR_w6Wy7FF_wI33Z691hIQZ6SKbMutse6r1AwxVDBmxosy770g88iGwXay3acOz_dH16o-l_LGYfQQdxROPv_X6s-TA6mwPFuUBZwnphQjzQo0NCZEN0Y37GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2883f7592b.mp4?token=cNzTaMO0Tu0tJQ7HfzpZG31OqzEEKXpIho1Qa6SyG5nuXPJ7aInzwuAhh3Tjf6ThItStYx1liPdzqlRydx0sAN3N-bY2_3BLrVFZvRpcCUvsVipopjZ-WmW_bYwBdDCioel88KIvDPoZv-VxpV-mPGR7PdM14MOJz7ibjuB0MQeoDf7iRd6wSH8MhyiHNnacgoYvo4GyD9SSPUDsPigH4weranspoMR_w6Wy7FF_wI33Z691hIQZ6SKbMutse6r1AwxVDBmxosy770g88iGwXay3acOz_dH16o-l_LGYfQQdxROPv_X6s-TA6mwPFuUBZwnphQjzQo0NCZEN0Y37GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش نکیر و منکر بعد از ۱۲۰ روز
😂
@News_Hut</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/news_hut/67273" target="_blank">📅 13:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67272">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rN1iX3Dj1ejxYuAiEbe7JJwfvrugjvL6IbsGjau7PNlnxoLO1TJiW5jzNcJGZOwbg4dVkb_RMiNf2w_hfWEa6BnVw6HJy8t878wC3-wTwaYtokbYDpS2wEhoxQFram6c4Dp-Y9RXXrev5IUDmVN2GOzKLFGMO9RMppcLQCHgDdkTnMRK3wjzcIYbm6srCQg_4_IbpSSimFo_sghDfmY652B-YhrF84QXy8ElaWmki0O2xTqXYHpXYrvJTo9Wfnv6PGl8zLOdQ2NBcEYYqj6VAG6sczHIaoDPfO_eJGAp-PTWOMD8CWoCJJfCvhJYjawDFujik7kqLd4QvwqmAfzckg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
التماس رسانه حکومتی در ایتا برای حضور در مراسم ؛ جمعیت کم است...
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/67272" target="_blank">📅 12:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67271">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc8da4a29b.mp4?token=LOs0diW-0H25y81hP3OSLAVqWAsLZ6HW7rGvtHmgwJoL-sCPzp6KkJZ7g4e0nfiYEbJUetmkGgjKn6fKx9x9hgosvyIerYQ9vnefqflPppKc0wKz1cfltL4UWHbT6TYLat74B1a1KzHx-__55y0vU_SBfzVqfNq5-0UpbeoE483_XhBfKdmMqDuNb2tWwcLQHsUdDkVNWN3NVqMwctzCmdurxATfRz6Pb4CHICgcid_fu0ZVpYOHbkHw7hnj8CKb-rMc14f4lIyrkZmWz4QXEvLfAeyp0lVpRG6DeF2r-H41a1IlWI98-Cc3F9XkBg7PL13z_8lna5kfeB5HOlx0Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc8da4a29b.mp4?token=LOs0diW-0H25y81hP3OSLAVqWAsLZ6HW7rGvtHmgwJoL-sCPzp6KkJZ7g4e0nfiYEbJUetmkGgjKn6fKx9x9hgosvyIerYQ9vnefqflPppKc0wKz1cfltL4UWHbT6TYLat74B1a1KzHx-__55y0vU_SBfzVqfNq5-0UpbeoE483_XhBfKdmMqDuNb2tWwcLQHsUdDkVNWN3NVqMwctzCmdurxATfRz6Pb4CHICgcid_fu0ZVpYOHbkHw7hnj8CKb-rMc14f4lIyrkZmWz4QXEvLfAeyp0lVpRG6DeF2r-H41a1IlWI98-Cc3F9XkBg7PL13z_8lna5kfeB5HOlx0Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
ویدیو ای
از بمباران بیت رهبری9 اسفند 1404
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/67271" target="_blank">📅 11:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67270">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccea9f87ad.mp4?token=ILCZeFxAI4s_F2-rS32UHeR1rgN43SDGMIHwQW3mHFLoeA9KETtDMl8nei-mi7IlqACZm3FFV8QYrq7AIOW61tHy0XI_oNfzk-hm9TNU1r4si-r4N9NFOoGtoCkNLRPXjKXjmzAqdGEoGEfBYFEz-OFvEuF9biw1wsUq9tYPtDC1yhD5lKCU049Zrx7lkOTcrr86Jlo5RlaB0516MXLMNvNkAB28bh1T1DD0pBLemHft8-SboNQOWiWR5ScCB4TVd8Eiy1wu7WrmahNmUBJ03o42YHlcm2WA5t-i88rQzZoi_lG1fsIQMkQL-iguwKMADBv6ixxaesiYa896BGcWFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccea9f87ad.mp4?token=ILCZeFxAI4s_F2-rS32UHeR1rgN43SDGMIHwQW3mHFLoeA9KETtDMl8nei-mi7IlqACZm3FFV8QYrq7AIOW61tHy0XI_oNfzk-hm9TNU1r4si-r4N9NFOoGtoCkNLRPXjKXjmzAqdGEoGEfBYFEz-OFvEuF9biw1wsUq9tYPtDC1yhD5lKCU049Zrx7lkOTcrr86Jlo5RlaB0516MXLMNvNkAB28bh1T1DD0pBLemHft8-SboNQOWiWR5ScCB4TVd8Eiy1wu7WrmahNmUBJ03o42YHlcm2WA5t-i88rQzZoi_lG1fsIQMkQL-iguwKMADBv6ixxaesiYa896BGcWFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سر دادن شعار مرگ بر آمریکا در مراسم وداع با جنازه علی خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/67270" target="_blank">📅 11:41 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67268">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0d436c597.mp4?token=cqcuHo-bCFQm5DV_oAW7uZI--MpP5ujfmBx5P-Pmc11b8As5drQjngRYyyD-tEOhrXePLowJn4tT5UypUzAbYWb1KjH_BAVYrSkm-6fGxHd_XlNm2j1h4M5rDOJaxR9cZQcKrzcoINc1zC-xy9kvkSxZjznxNzEoOlTqeDQ9DbrtKsOAozRSHDA4Y3bE1kpMI_m4NsmSYtSKDPjoxuZtgc8cndpFXoYdz0dJj70DlHJyYmN70u4aqWsB5sz0ADUqEr5Tc9Wbx1stW4z9l6GrrOUZo125LROZrqgxOYnj_09uAj_X-0B1RGpCq1ry2Rmgd2qQosOGlG1aeQtIanrY6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0d436c597.mp4?token=cqcuHo-bCFQm5DV_oAW7uZI--MpP5ujfmBx5P-Pmc11b8As5drQjngRYyyD-tEOhrXePLowJn4tT5UypUzAbYWb1KjH_BAVYrSkm-6fGxHd_XlNm2j1h4M5rDOJaxR9cZQcKrzcoINc1zC-xy9kvkSxZjznxNzEoOlTqeDQ9DbrtKsOAozRSHDA4Y3bE1kpMI_m4NsmSYtSKDPjoxuZtgc8cndpFXoYdz0dJj70DlHJyYmN70u4aqWsB5sz0ADUqEr5Tc9Wbx1stW4z9l6GrrOUZo125LROZrqgxOYnj_09uAj_X-0B1RGpCq1ry2Rmgd2qQosOGlG1aeQtIanrY6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای از پرواز جنگنده‌های اسرائیلی بر فراز بیروت در مراسم تشییع جنازه حسن نصرالله دبیر کل حزب‌الله لبنان بین سالهای1992تا2024!
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/67268" target="_blank">📅 11:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67267">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64adeed1d2.mp4?token=prSH689w1qAoPCbcQ7rKAFcWlq6UYBjUIJPdW5xGB_3opKQb5ud2IE_S6ciOQw5VwWAj4NnyEzYXAkoU9tc1C_qZfHxeIfOxnmYQGNUHKM_vZNjWAfvocPXBPcGZrm6U6eFQy1ykTnKMafV9FrifGzY-d5k-VBuD7eA9P0C8MVXcuHHExwR9-LKQ5hW7J2wKTOOaK9b0O4GhQgJYN41Mysp-BmSzkx0XKt4A1InWfVBnXztg5vMwFHI0siaOZQwROrCOzIzc0tJ7IG9h-FYHFFVng9703kiyKSIS7gIi1H1VpZ1ljqxYexC4YZMtqlji27YL9_IK0cTp3c_0xtnXcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64adeed1d2.mp4?token=prSH689w1qAoPCbcQ7rKAFcWlq6UYBjUIJPdW5xGB_3opKQb5ud2IE_S6ciOQw5VwWAj4NnyEzYXAkoU9tc1C_qZfHxeIfOxnmYQGNUHKM_vZNjWAfvocPXBPcGZrm6U6eFQy1ykTnKMafV9FrifGzY-d5k-VBuD7eA9P0C8MVXcuHHExwR9-LKQ5hW7J2wKTOOaK9b0O4GhQgJYN41Mysp-BmSzkx0XKt4A1InWfVBnXztg5vMwFHI0siaOZQwROrCOzIzc0tJ7IG9h-FYHFFVng9703kiyKSIS7gIi1H1VpZ1ljqxYexC4YZMtqlji27YL9_IK0cTp3c_0xtnXcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مایک والتز نماینده ایالات متحده خطاب به نماینده جمهوری اسلامی در شورای امنیت سازمان ملل :
🔴
اینجا تهران نیست که بخواهید همه را خفه کنید ، اینجا آمریکا است ، اینجا سازمان ملل است. این اسناد حملات شما به مناطق مسکونی بحرین است که دروغ نمی‌گویند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/67267" target="_blank">📅 10:34 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67266">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b206a5500f.mp4?token=JSZII4__NY8RAFKgS-AB_KDMpyQt9sGPV0WiBxGwqM3kHd0qyOsLQOWyUn8oUsk8bY75JyYaT9e-y-ttpKxWiIGvHndeUFFXd1D-sutrmp4edNr3Ai26KCEl4Cf11qL1ptcxjuVVSHcZ6-E-0QrA_V4dZGU5_niihcaWMGEzpg7pVfvbgA0pgB5J1AWWcEYE9LuNE8k4Ns9P7aDMtaCHyhLnHNpUf34KYPCLSJ-uy9Hc98hEbH3bJtwDePMc12NDZlcgIsnFTWn0N86IDXSbiJmgdXMk4chFl2skvVHF3O-f7nECx4rXU1--un6ckAdRr3khppI9Hoj-144nauk_MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b206a5500f.mp4?token=JSZII4__NY8RAFKgS-AB_KDMpyQt9sGPV0WiBxGwqM3kHd0qyOsLQOWyUn8oUsk8bY75JyYaT9e-y-ttpKxWiIGvHndeUFFXd1D-sutrmp4edNr3Ai26KCEl4Cf11qL1ptcxjuVVSHcZ6-E-0QrA_V4dZGU5_niihcaWMGEzpg7pVfvbgA0pgB5J1AWWcEYE9LuNE8k4Ns9P7aDMtaCHyhLnHNpUf34KYPCLSJ-uy9Hc98hEbH3bJtwDePMc12NDZlcgIsnFTWn0N86IDXSbiJmgdXMk4chFl2skvVHF3O-f7nECx4rXU1--un6ckAdRr3khppI9Hoj-144nauk_MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚬
وقتی تو ایران میخوای پیشرفت کنی
واکنش آخوندا:
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/67266" target="_blank">📅 10:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67265">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b88ddeb40.mp4?token=WjjzbwHbiwacnGkyDuxvm_H6ZvOYSHSoiu_fUEW5M58xmym_WLkzTgYOqsEK8pplJl9DV-z_V4YqrnI7HPdvuzFLzUps7G0zpPjSOVdD3WnC9-KnuARY2TTVSXBxYxYWcQnNx6MqLa_xJPB9MuNyaKzpw-aKkklx0X1R73sQuZmcOWSq78_uxdkXHxpmrMxESToBucJHfrwklP7rrJTABgdXWgRfcHjYsfoos6YB_MBQmeSJ1P5Etdz_tp2No140v30CmGUsgxJ498b8rxN4sM1sOuFnubSdF-YbYqFnv6qTF_u15jhuNPeO3Dogd_M29FOyRcPtOSPAFd0GYghlHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b88ddeb40.mp4?token=WjjzbwHbiwacnGkyDuxvm_H6ZvOYSHSoiu_fUEW5M58xmym_WLkzTgYOqsEK8pplJl9DV-z_V4YqrnI7HPdvuzFLzUps7G0zpPjSOVdD3WnC9-KnuARY2TTVSXBxYxYWcQnNx6MqLa_xJPB9MuNyaKzpw-aKkklx0X1R73sQuZmcOWSq78_uxdkXHxpmrMxESToBucJHfrwklP7rrJTABgdXWgRfcHjYsfoos6YB_MBQmeSJ1P5Etdz_tp2No140v30CmGUsgxJ498b8rxN4sM1sOuFnubSdF-YbYqFnv6qTF_u15jhuNPeO3Dogd_M29FOyRcPtOSPAFd0GYghlHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
ما ایران را حسابی درهم کوبیدیم. آن‌ها برای توافق لحظه‌شماری می‌کنند؛ به‌شدت خواهان توافق هستند. ما به خاطر یک مراسم خاکسپاری، یک هفته به آن‌ها مهلت دادیم، چون آدم‌های خوبی هستیم. واقعیت همین است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/67265" target="_blank">📅 09:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67264">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb8124f389.mp4?token=oPKeDi6eYW5Rzc5T6KWMs0lX3ZxuX3xDkHwdwNiCIXJ02Zor35BG9EtJp8EBHMjfktlTMH4NsVcZ0_MQ8ja5V-6fO2M0-qmPP-6m1RgvQwOMvKpoCtTvc0u3Lv8Pc8yVxS_UmN-XxCpwUnmuPgAOHKEgWfpdyBvhFoyXCC7nK2pfH8didl2eoj_Q0lDQ0YCp2_FRuIJOSLI_g616SCAGWzlEFlLvuPpNJGiLZCeeyPo12sRzFcVuGHB-Gi3rTSGfw5RSJAIQM6lbY8_dbdA6jnHHjMrojP0n2SiGgF4m_uvdeqsjtXMeLqF1LwCNjA3IqpqMwLPaZ4jvt1j5hfhj1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb8124f389.mp4?token=oPKeDi6eYW5Rzc5T6KWMs0lX3ZxuX3xDkHwdwNiCIXJ02Zor35BG9EtJp8EBHMjfktlTMH4NsVcZ0_MQ8ja5V-6fO2M0-qmPP-6m1RgvQwOMvKpoCtTvc0u3Lv8Pc8yVxS_UmN-XxCpwUnmuPgAOHKEgWfpdyBvhFoyXCC7nK2pfH8didl2eoj_Q0lDQ0YCp2_FRuIJOSLI_g616SCAGWzlEFlLvuPpNJGiLZCeeyPo12sRzFcVuGHB-Gi3rTSGfw5RSJAIQM6lbY8_dbdA6jnHHjMrojP0n2SiGgF4m_uvdeqsjtXMeLqF1LwCNjA3IqpqMwLPaZ4jvt1j5hfhj1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زنده یاد مانوک خدابخشیان:
آمریکا یکی از داکترین هاش برای به زانو درآوردن کشور مقابل اینه که هزینه ملیشون رو بالا میبره مانند شوروی که همینجور کمرش رو شکوند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/67264" target="_blank">📅 09:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67263">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">⏸
مستند کامل و 46دقیقه ای شبکه 14 اسرائیل به نام از «چشمان جاسوسی در تهران»:
این مستند جنجالی دیشب از شبکه 14 اسرائیل پخش شد.این نسخه زیر نویس فارسی دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/67263" target="_blank">📅 09:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67262">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/W6fZjvEJcMp9D7TXH-tqS5phNCktm5a13S5gpF4f0i2gb9Hm6kd1SGeBU5zxHq5R5HVjK_n9Bp-H1KLmrN6hg5S1GmVDcSH48p-sZO38s0I64tzE7gvbhR321pR7_tYYWVj2m2IulNTJpxZAexVl-PpiMQwZh1KiPHVwhvozy57_Fc416SPstg9KCzecxh67TiVIHVcuhuTDCvev0Zb6r2xryYZCpXXudSiPmosXfT1hEderm8RsFCzcZlVxg4lrHSi2hfZ9KgNs4L0sTh3Ei9RDaN-AfQ3YZ3pUe5zwvC4aQSfuGT3XjcVUx5-yn85WdUidK8Mb6PpcseDtPydyYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🔥
انقلابی در صنعت هوش مصنوعی
🔥
🔥
🔥
🔴
میدونی هوش مصنوعی ترند دنیاست و اینده ی اقتصاده ولی بلد نیستی ازش استفاده کنی و درامدزایی کنی؟
هوش مصنوعی TimeTrade این مشکلو حل کرده
✅
هرکسی با هرمقدار علمو دانشی میتونه ازین هوش مصنوعی استفاده کنه و با سیستم auto trade به صورت لایو و روزانه درامد داشته باشه
🔥
👇
https://t.me/+hcwmoHXpF6k5Y2Q0</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67262" target="_blank">📅 01:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67261">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@Vision_Bet @Vision_Bet @Vision_Bet @Vision_Bet</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67261" target="_blank">📅 01:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67260">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/koWgyGceZ52C6NM7MhhG5QXd1u1I0fORsv2ArZPGMpsU_uS_7mHDF_qmpG6G36NQ3N_E7wKAiPlExhIsbJL6W4NJXrOVCouy4PpuR0_4bgmFtGLIzMUMhFQQtqRtEcvU27Fzp9cbdZIAhqovJCg91XsRdTLhhTo88U_S9GtdtpneKwK7LK1ACxK8F9cIoFFU6FuKoqqZ2L2_4Ww3tlNffeotey4hIh43mZOFvS5eKXZmVtjI9X6x6yG7fkJOqsBiMvnwAyz0AD_NeUPW0CdV9dU6B1zVa2G4pA5DnYw98f6IM_XA9HBchH476u04WiM639W_7zL9nvdUW3StNufWuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@Vision_Bet
@Vision_Bet
@Vision_Bet
@Vision_Bet</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67260" target="_blank">📅 01:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67259">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
🚨
سخنگوی ارتش اسرائیل:
اسرائیل آماده است به صورت مستقل با جمهوری اسلامی وارد نبرد تمام عیار شود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67259" target="_blank">📅 00:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67258">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0b72ac39d.mp4?token=QM-mNUjBZX337UkozIQLyBalZy2XSxDyqORPCzCyByVCYWoxv1yinY_F2_ovNPf7Rt88YE3k24uRR9NcSY3n-0qorR5o4yxVh1zl_SzRBY1bZYGPTqt0p5AZ2s1dFmXx0gDs6wyZk3zfw_FrIf7GDud6J65h7CCy0LeCNsADwoX_LM35sLflJUAs80A-FSnEzR4DzWeJt1r2vnB2ojdGhlXww99F5YpjqeGM_FJkCEE0sZ1MafdqvzUSr8tuZjbR65zdCrCXAjYglBA4NL2WWrp0CfR8ifY47n_cb58W3A9x1XPawgyK_iNi18OyN3qsZjLEkAhZ3XeImvG_VdlHdkw4tUz9odLpLEHDgGxeNyNWFz3vN9HlWyzBGzIiY3O7st8Dk4MBpTY7CisHE6TpcgAfTYPFBH7mK6QDKu8dsYC2MA1yfdu6Xd7N8TcAImq6zxZAhnQbJ0rQwCabH5XTQLfJ3IuKMOPgB0ixh7hOpICfxIeLmtaad1gjns0cijiB4DNgF8-_yd2224uQdVXvcfPhgy81ne9OJc_9LP6hNKHwewhquWs7DI-grZz-vs7u3_9WqVw8k9Y8DeSXxELouzef5xYb0CJMt2vSeFfW3jKSHOZsI6iJVnmmXb1MJ0W3qZ0hdUd-mMs6PqQOmNpuOP8c8cUlkedKfqAQFeVsfqI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0b72ac39d.mp4?token=QM-mNUjBZX337UkozIQLyBalZy2XSxDyqORPCzCyByVCYWoxv1yinY_F2_ovNPf7Rt88YE3k24uRR9NcSY3n-0qorR5o4yxVh1zl_SzRBY1bZYGPTqt0p5AZ2s1dFmXx0gDs6wyZk3zfw_FrIf7GDud6J65h7CCy0LeCNsADwoX_LM35sLflJUAs80A-FSnEzR4DzWeJt1r2vnB2ojdGhlXww99F5YpjqeGM_FJkCEE0sZ1MafdqvzUSr8tuZjbR65zdCrCXAjYglBA4NL2WWrp0CfR8ifY47n_cb58W3A9x1XPawgyK_iNi18OyN3qsZjLEkAhZ3XeImvG_VdlHdkw4tUz9odLpLEHDgGxeNyNWFz3vN9HlWyzBGzIiY3O7st8Dk4MBpTY7CisHE6TpcgAfTYPFBH7mK6QDKu8dsYC2MA1yfdu6Xd7N8TcAImq6zxZAhnQbJ0rQwCabH5XTQLfJ3IuKMOPgB0ixh7hOpICfxIeLmtaad1gjns0cijiB4DNgF8-_yd2224uQdVXvcfPhgy81ne9OJc_9LP6hNKHwewhquWs7DI-grZz-vs7u3_9WqVw8k9Y8DeSXxELouzef5xYb0CJMt2vSeFfW3jKSHOZsI6iJVnmmXb1MJ0W3qZ0hdUd-mMs6PqQOmNpuOP8c8cUlkedKfqAQFeVsfqI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
هواپیماهای اف-۵ و بمب‌افکن‌های بی-۲ بر فراز نمایشگاه بزرگ ایالتی آمریکا در حال پرواز هستند و جمعیت از پایین نظاره‌گر آنها هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67258" target="_blank">📅 00:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67257">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd926d6f8c.mp4?token=XK5DaQ0aDwJIHO7WOy6ntksN-kSNknvXCD3Tzw1sYdStSFMsynaOx2o_xhUJGNt5Tu-Kf0p_eAmlTgVY2e3JquNvsfFzk3r_kgT5QJtLxKvnw4QLxrfmxnsef9aOzTyWU06V5L-mXdrqRg00R5v3C-9PmIYM8iiW4iLjfpJCZkmRju1SEYStBkf5GxSkPJciMzZjcC17t6eyLVK7GrUhFOQ_2HtFG4kwYtjBoqB2uy9dwuTRr-NJGTMtS4FxKpF4wnajC90iyXmcwHKl3iFtFSFO9CyHXDIF_SswdtOPpM4JwohoHVjWkTowfT1u1jTl1YAsqzlW4kSh312XHFIMtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd926d6f8c.mp4?token=XK5DaQ0aDwJIHO7WOy6ntksN-kSNknvXCD3Tzw1sYdStSFMsynaOx2o_xhUJGNt5Tu-Kf0p_eAmlTgVY2e3JquNvsfFzk3r_kgT5QJtLxKvnw4QLxrfmxnsef9aOzTyWU06V5L-mXdrqRg00R5v3C-9PmIYM8iiW4iLjfpJCZkmRju1SEYStBkf5GxSkPJciMzZjcC17t6eyLVK7GrUhFOQ_2HtFG4kwYtjBoqB2uy9dwuTRr-NJGTMtS4FxKpF4wnajC90iyXmcwHKl3iFtFSFO9CyHXDIF_SswdtOPpM4JwohoHVjWkTowfT1u1jTl1YAsqzlW4kSh312XHFIMtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
با هر ثانیه این ویدیو سوپرایز میشید
😐
😐
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67257" target="_blank">📅 23:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67256">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e000f4f43c.mp4?token=oMVEJEW1CItvAJX1FfZfwP2q40yLZCfk1HRlq9Yv9mE3_Ddbjxt2I5SQn_iAkzCDKGQGTOYWLOQYntBOH5--t22Pz3U1lJRT91scnI-neY-81YfRtsEuSoj7NJIv0H3t49ig2PK-8KFlMDLymvMYCkGZbjbYocAwEEigSzdkoqwzuwEX0lsJrF5TCqO7CycjaNQ9PlBWvvYXfd_VYJvPHQwu6jpwcTmMncIVJ--JAt5blY-92w6B93mSyFoG0kkx_jMI_yjRPRJXKCgyZkC0cMA7rG8AK1HPEOkb79ROaaVKjTNd5uek-_4HDU1hck7KpcENTv9vrIWk-xMRm5WZCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e000f4f43c.mp4?token=oMVEJEW1CItvAJX1FfZfwP2q40yLZCfk1HRlq9Yv9mE3_Ddbjxt2I5SQn_iAkzCDKGQGTOYWLOQYntBOH5--t22Pz3U1lJRT91scnI-neY-81YfRtsEuSoj7NJIv0H3t49ig2PK-8KFlMDLymvMYCkGZbjbYocAwEEigSzdkoqwzuwEX0lsJrF5TCqO7CycjaNQ9PlBWvvYXfd_VYJvPHQwu6jpwcTmMncIVJ--JAt5blY-92w6B93mSyFoG0kkx_jMI_yjRPRJXKCgyZkC0cMA7rG8AK1HPEOkb79ROaaVKjTNd5uek-_4HDU1hck7KpcENTv9vrIWk-xMRm5WZCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عزاداری مجری آیت‌الله بی‌بی‌سی از سران حاضر تو مراسم تشییع خامنه‌ای بهتر بود
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67256" target="_blank">📅 23:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67255">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1191e0b9a.mp4?token=jlix6Nrb35jPb9gOdWZPIUG-1CN7_YS_IJOiH2nhX_vjKskT66ozPwWzw_tL3cCoExbi4mmBNatZWfySu_-97bULRNP6kJ_pVCxVGxveNT4GO6dza5v7nie1xI_B7JFQBYRAR_OZNipXjWUO1DMMy-abWJDKUxzcHZKIdWZ2JL392pT5bgJUWuEiwjVsVfN3kZBUkO8lQ7cLnC2zNd7fYWFVgJU7XhT3Gmyuuw1XSdbebUb5gDhSnjtrrFsk6RoSb-tC6U_DarBfeh4OhVvgJIKaQ89cRnPEhPTH5vj177cuwalhII2-DyY_2etJwAQR5xFfUekEZciJGFDdRb5AoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1191e0b9a.mp4?token=jlix6Nrb35jPb9gOdWZPIUG-1CN7_YS_IJOiH2nhX_vjKskT66ozPwWzw_tL3cCoExbi4mmBNatZWfySu_-97bULRNP6kJ_pVCxVGxveNT4GO6dza5v7nie1xI_B7JFQBYRAR_OZNipXjWUO1DMMy-abWJDKUxzcHZKIdWZ2JL392pT5bgJUWuEiwjVsVfN3kZBUkO8lQ7cLnC2zNd7fYWFVgJU7XhT3Gmyuuw1XSdbebUb5gDhSnjtrrFsk6RoSb-tC6U_DarBfeh4OhVvgJIKaQ89cRnPEhPTH5vj177cuwalhII2-DyY_2etJwAQR5xFfUekEZciJGFDdRb5AoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تصاویر شلیک موشک‌های بالستیک آمریکا از کویت به سوی مواضع رژیم جمهوری
اسلامی
منتشر شد
ویدئوهای منتشرشده نشان می‌دهد نیروهای آمریکایی مستقر در کویت، موشک‌های دقیق ATACMS و PrSM را از سامانه‌های پرتابگر M142 HIMARS به سمت اهدافی در خاک تحت کنترل رژیم جمهوری اسلامی شلیک می‌کنند
.
بر اساس توضیحات منتشرشده، این تصاویر مربوط به ۲۸ فوریه ۲۰۲۶ است و بخشی از عملیات نظامی آمریکا علیه زیرساخت‌ها و مواضع رژیم جمهوری اسلامی را به نمایش می‌گذارد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67255" target="_blank">📅 22:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67254">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3720a35424.mp4?token=evHV3ucnTx0LTRXG5JpWWkADx4mkXXtzqUpVmezeNF8il08gng11Qd2MNVs0_W2b16L8LBcdi8cGwUAIzAYvldXDp-RAjhjJbja5jEGzvrKEoRzhhwdVloVrE3BFK877EhtWTCcwoNs9XAt0HL_qgKJ_i_s3gIbQ_YzK_prWXr1agog0my42yj_NInBkRw7jap-_IBs6RaNKvGnWONxmNUW9eUerwZG95TY8XKkv1C0Q1J5HF6JRitK7IPG8LDW_cPIcKarVrLydScqFbocwzZ4tvzAeYGXV2ARiUusbMQ4U2xgaH4jgxdz2tfAdv1_15NIBxDX3j6j5oDTkXTV1Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3720a35424.mp4?token=evHV3ucnTx0LTRXG5JpWWkADx4mkXXtzqUpVmezeNF8il08gng11Qd2MNVs0_W2b16L8LBcdi8cGwUAIzAYvldXDp-RAjhjJbja5jEGzvrKEoRzhhwdVloVrE3BFK877EhtWTCcwoNs9XAt0HL_qgKJ_i_s3gIbQ_YzK_prWXr1agog0my42yj_NInBkRw7jap-_IBs6RaNKvGnWONxmNUW9eUerwZG95TY8XKkv1C0Q1J5HF6JRitK7IPG8LDW_cPIcKarVrLydScqFbocwzZ4tvzAeYGXV2ARiUusbMQ4U2xgaH4jgxdz2tfAdv1_15NIBxDX3j6j5oDTkXTV1Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ورود خودروی حامل‌ جنازه علی خامنه‌ای به‌مصلی تهران
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67254" target="_blank">📅 22:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67253">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O3ENSkopgj3JXfFSeEOYbqo2eruKq5Edd6uXeXvu_pj1G3br8DcKRbTZ0tHhq0y0l0eW2H6P0LG3qUbxg99ag38C9Ksb7_MCB9om1jESbEyB_fTJNx28yKneO9ckwN5X3MV5T0ad5Jmc8QJqwRNSTC8ZK7X5B1bbx9MqESLbAkDISRA-7Tju_8v_nyQoQF5YVNViGsEKVj0joFJRSwfA_yJBsyGzKIFUSghqZPXSDAIAo7K--WXXVc9Cq2No9X0oySGYziZix4OU4T9Y8rIMdn6PBOIF0PSWxe5oFtEVs99hoKOtZHhSBpjCEm_6XPQ9xkilXiVmnvywHGzq2dmXxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سید مجید نقطه زن فرمانده هوافضای سپاه هم بالاخره از سوراخ اومد بیرون
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67253" target="_blank">📅 21:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67252">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GyrM_b_XCOK2IvpO_UtxfdYuZzUjU1NJ_umw4cgwCNdN4dWfVU-0bjUSVNBw-e67Bp1p-tvcgPD2F9Sa03oobo-UQBRdl2shbP2YzvXVsVZjrxu2y8kL-sNiRD5V77BI5G20bhbjyY-ZoRT2ZgTGtFXJTVG-bHtZi-oe8SBUcl47LJOn4_ZWx_ns0MwF6LUraCLp2wwmNixH3TcEMcBiAOxLnadAuF_wki-7GEvc6qGOX3hryjnc5hyykwMM3nyWlvjO9SR8wsGEPvMUnRceOzwA3ZcuALb7kl_6PCb1glI-8s87VG4Q5pNrcu9OzktZ07SlLwJ1s33Ia1OkIm1y4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بلومبرگ: ۵۸ میلیون بشکه نفت و میعانات رژیم روی آب مانده است.
حدود ۵۸ میلیون بشکه نفت و میعانات متعلق به رژیم تروریستی جمهوری اسلامی روی آب انباشته شده و نزدیک به ۹۰ درصد این محموله‌ها هنوز مشتری یا مقصد نهایی مشخصی ندارند.
بر اساس این گزارش، با وجود تعلیق ۶۰ روزه بخشی از تحریم‌های آمریکا، خریداران بزرگ همچنان با احتیاط عمل می‌کنند و خرید نفت از رژیم جمهوری اسلامی محدود مانده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67252" target="_blank">📅 21:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67251">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sdc-DEWcWxE8_kpSg87J0QwqayHK-o7oRLx21eMTDF6ZRcURzzG1IKZZrtZkAAbR9vnRAX8kHxWv2xEOUF2w-QO26s7pIXDamDz1thQ5pcJ0KqQWJT7Yxdpeg39HpIie-YYdhsODuc8BejlBaDbBmGvBft3yuqwkF8i-V_rM-0r9v45tn6_TagD2DDOZNYDhTIWWCHesklmT7QaUCpQ0Vr698wTGL1wb22V7h2bKlKCJC0TCfgzV0Lu6-ewBl-GWHFTbyMHcuFsI-9FFZiQDJe8oHzFswn-dTlrUDhCo2k8dp8LdS_vH6FPFdWYsZzw1EGtB3VlYjifNGd0lyEFayQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
نگاه معنادار عراقچی به قالیباف:
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67251" target="_blank">📅 20:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67250">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bfb7i3vKjbMXa19xtT2ohmM62JvwU5v_xC57UlCYTptHJgGVGcIECy1v55bNxPILnZWuLIyGwTuQt_TyjvH4e24PfmWeDgYka0uw3RsRg2xhIO0H1PMK6r4dSW10ZbVJsRslyQEqJ94S8BBl3UBnXgP15DOXAb8C-YnxvoxvmL21qNJheOqbq7XmcAm5vXOt0GuCRjw7RzjVHU6xbj6aLQcUWIbSRAZ3LsKK-4jsEnHRN0NtQpMOP-TWs7xO3SLdmiWtTDenYbYRXHJnJL3EU68sD32g6qLZROghnrCL1cX3KFt-mDYk06I1giUqGyXs3ewRKENxCyXHS4WisPtAZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
باراک راوید (آکسیوس):
رئیس‌جمهور ترامپ امروز با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، گفتگو کرد. دفتر نخست‌وزیر اسرائیل اعلام کرد که آن‌ها توافق کردند به‌زودی در ایالات متحده با یکدیگر دیدار کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67250" target="_blank">📅 20:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67249">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aUavKjwEezKvp8yxDjk9f3K-ucBsScwQlwnXUmmtxzWc3_tsBb9QqmtVZipj8kY5hE3R1Dwb1S7o98X4Wmou_kfZsMIHdoNaPhURpBZmNBdNY23l3kaN4WhEbDetNkZsLehKmqQnyFNQEQSGLsXTvIAKHn_B9pLEWYedjCRYdXNT6NJQSbbSdDbjli0wDagNU0WQNXH2ytn-J69JjotIawSW-_ytk_OMzFvwpko06yKyAbcD_-L5-pXMORwfqFEWNLTB2h_zdgUz_RFEFd90y7wTf7cMqQWlYq58cYU1AeE-3MxNCBWuWI1BdfjS2o0WOoQFDUqRMYnv7kwXh7m44Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😆
😆
‏سی تی اسکن از دندون عقلم:
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67249" target="_blank">📅 19:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67248">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nu0Y2YptHn0xmHobEYUMo8AXbByF4SL9Ch-ubCiHBgwbA7_Taq5S0ocEU4DvJjHnBb_SSGEdnumZAt-50Ns6HwPcc5gKC1ZEfC9WE4KVcEwlEnRVBm1Oj5jmP9s6iUYcXLQUx1T5LrgmiNx-tOXtTY3WuuTYoVAeP6F_C59WxPmvNRKVuTjKA3ILKSXMTQ0UWxu1eq0n1j21BCpm2LkN8JeL-fGwdvn0DBBphst8C0VbmpAvL4tEXskq5Cg_fQ6AtyNCZnjr-u-AJqJFXfXckbvrdK9DkCTEISv6qUvEakjBwm7Pz4laeSkoXxlY3X5rZDPHPFaFykduxO-Jt9b9iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
دفتر نخست‌وزیر اسرائیل؛
گزارش نیویورک تایمز را که حاکی از آن بود مقامات آمریکایی معتقد بودند اسرائیل در حال توطئه‌ای برای ترور مذاکره‌کنندگان ایرانی در جریان مذاکرات با آمریکایی‌ها در بهار امسال بوده‌اند، رد کرد و آن را «یک تحریف کامل از واقعیت» خواند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67248" target="_blank">📅 19:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67247">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4bc1c344f.mp4?token=ZFRoDF9nIEP2u5c-IYosKxYHvuI1J-jkqxgimXQI1pGjSlym4IpkXvrxVubiaNOsy716_sUWJfjCekaKGuauJc4weVbRobCae5MrqypXBNdn06zKG0r7FIgnh6fT2oNXXQi_y7YE4suVcpRVwwdpmy8Vwluy57TmLCaXSUDYLOlXz5PuLzGoKLshwyQUTpQ9A4l_3WmT_ErJztp1mqLEJsM-eD5_0WW82DNGDg3BsfMda3wuwzF-wnHCm1g7Cs9x8lJdY_57LAFUFmcxVW-ys6p1lB7h4FxH7huqgbPioi1XHXDY4HlNCw2T-JxbtA1rgbQFZWzWgU1WjtXEEDO1zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4bc1c344f.mp4?token=ZFRoDF9nIEP2u5c-IYosKxYHvuI1J-jkqxgimXQI1pGjSlym4IpkXvrxVubiaNOsy716_sUWJfjCekaKGuauJc4weVbRobCae5MrqypXBNdn06zKG0r7FIgnh6fT2oNXXQi_y7YE4suVcpRVwwdpmy8Vwluy57TmLCaXSUDYLOlXz5PuLzGoKLshwyQUTpQ9A4l_3WmT_ErJztp1mqLEJsM-eD5_0WW82DNGDg3BsfMda3wuwzF-wnHCm1g7Cs9x8lJdY_57LAFUFmcxVW-ys6p1lB7h4FxH7huqgbPioi1XHXDY4HlNCw2T-JxbtA1rgbQFZWzWgU1WjtXEEDO1zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظه بمباران بیت رهبری 9 اسفند 1404
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67247" target="_blank">📅 19:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67246">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Mm0eTpentLWwI-BezpPzzp1uVQ4v0DDhSyr-ld5orRNGAO7bkroQuE7kUUCcZL-oXBB8VdRsdpeEfmLkKo2Zp93xN27m93VvKzWstBgnponJvi8bwYqMyzRqi92pFYeRq8-NknDvrB4L1a685bFeO3Q_nQY21WN7DA_HnZ7efwFjLhcsfdUqTeFGe8-ylLnRpXWE-5zSg5Rb5-GkNtHa7OtHEelxV1CgY4qZweUB0G3f6kxG2jG4wpzI_sl23R97jBwX0y9i38JhBKhDChkoVYd1AEWTDcz3X55MfSOcq5Ppe_BkNQQzM9jR4LvcOZfBCGSRS68yvsrLDw29Yeip_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67246" target="_blank">📅 19:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67245">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1099f5d95b.mp4?token=c880j0fwUUQlNe4Kfy3G-Ydn_JJeCiQr09WL0PT9QmlulSFEB_1dcEMqNYg1jeRjSm1oZK6q_EDrhtH7V9NnEaqenbrF9-_M-cukRq3Yopr5TXK6jAvOUjj3nWu7Y6AH53MQZc14t5Kk-9a8HRqWu1e3NFKdRG8Y-yzl-8_EbsKcrw9k2YLec9COtO_XvGpbLnnDlunYEHVb6JDq0DsPSRJwzAwU8S-Wkx0pdD7Xys5ZQE3Dx3txPd75jhQma76CP0afskir4pRjUQEZgAiaeuYgDAsMRg6PvHr6CGqgrTLjKFhGuMhXGuZog79op8yd4LxlpLjrTd9GbJkBFg3YKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1099f5d95b.mp4?token=c880j0fwUUQlNe4Kfy3G-Ydn_JJeCiQr09WL0PT9QmlulSFEB_1dcEMqNYg1jeRjSm1oZK6q_EDrhtH7V9NnEaqenbrF9-_M-cukRq3Yopr5TXK6jAvOUjj3nWu7Y6AH53MQZc14t5Kk-9a8HRqWu1e3NFKdRG8Y-yzl-8_EbsKcrw9k2YLec9COtO_XvGpbLnnDlunYEHVb6JDq0DsPSRJwzAwU8S-Wkx0pdD7Xys5ZQE3Dx3txPd75jhQma76CP0afskir4pRjUQEZgAiaeuYgDAsMRg6PvHr6CGqgrTLjKFhGuMhXGuZog79op8yd4LxlpLjrTd9GbJkBFg3YKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
بغض و گریه های تمام نشدنی قالیباف در مراسم وداع با علی خامنه ای:
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67245" target="_blank">📅 19:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67244">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff481eda8.mp4?token=XA8D6Dgl2zpGlVkJmHH845aXlgoD-Q0nQij84VuCZLlnscl0rD5Ib-J4CjBkJJ8urBbF5ImPWJiugcIhug8Z9l9wkLZrygdD-X_KF_pjQzLblwLRBJK8kFMfaaTylY9clvr8vgK-crmqbs5iUhT8NoZpx9BGh0bw0yeKddBcVzKiaKuE-GCQ88oum-NMPcCdp2AGR9uT5g-gpXNBgtydQ6SFT_7G8qM8E-bWQed-I0A9E0-ESr7Nn9_CM6tiGq6LipdCprXTJ4qV35HAy3x-PTBcsw-fFQq-3caKOTvgDm2IKLvxp6SSzUWSj8PDuo5_TMCP9lP9tzqgUdIlR7ATvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff481eda8.mp4?token=XA8D6Dgl2zpGlVkJmHH845aXlgoD-Q0nQij84VuCZLlnscl0rD5Ib-J4CjBkJJ8urBbF5ImPWJiugcIhug8Z9l9wkLZrygdD-X_KF_pjQzLblwLRBJK8kFMfaaTylY9clvr8vgK-crmqbs5iUhT8NoZpx9BGh0bw0yeKddBcVzKiaKuE-GCQ88oum-NMPcCdp2AGR9uT5g-gpXNBgtydQ6SFT_7G8qM8E-bWQed-I0A9E0-ESr7Nn9_CM6tiGq6LipdCprXTJ4qV35HAy3x-PTBcsw-fFQq-3caKOTvgDm2IKLvxp6SSzUWSj8PDuo5_TMCP9lP9tzqgUdIlR7ATvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
برخورد سردِ حدادعادل ( پدرزن مجتبی خامنه‌ای ) با عراقچی و قالیباف
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67244" target="_blank">📅 18:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67243">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6d67ab774.mp4?token=FiRibpYvMlVRuVSgTJxAZxkzLHiirJBbgTH0tT8Sf_LB7pkbFsoC6TLM5NqsSqFrLop3PL6JAa5l6WB6bGNazTgR5T4HoWmXwgQ7o56oLyzJkFiDQiEmkeVP4DlQJeykR7XAdQyuKHozqskdehcUy7rBxpL7IYP5rSx5QKfE4ZYZk49X1SD0vOX6SR1yug_xSvbBPRvxGGdOzWp2odtPA-KHe5JD0bH9qjbN0oaLXnHiww9UrAP7_2CUZrbcP3eI4dBS__6l2xt01fmfKVNlcPMxKEqAPnXSsOSoVfdhkQ2lc0aO65_yQ30ytfsdoMTPjxog6ajRhH-crsCG4uLxBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6d67ab774.mp4?token=FiRibpYvMlVRuVSgTJxAZxkzLHiirJBbgTH0tT8Sf_LB7pkbFsoC6TLM5NqsSqFrLop3PL6JAa5l6WB6bGNazTgR5T4HoWmXwgQ7o56oLyzJkFiDQiEmkeVP4DlQJeykR7XAdQyuKHozqskdehcUy7rBxpL7IYP5rSx5QKfE4ZYZk49X1SD0vOX6SR1yug_xSvbBPRvxGGdOzWp2odtPA-KHe5JD0bH9qjbN0oaLXnHiww9UrAP7_2CUZrbcP3eI4dBS__6l2xt01fmfKVNlcPMxKEqAPnXSsOSoVfdhkQ2lc0aO65_yQ30ytfsdoMTPjxog6ajRhH-crsCG4uLxBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کلیپی قدیمی مربوط به انتخابات ۸۴
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67243" target="_blank">📅 18:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67242">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tx2eRCTIr9uMunLHKizc6XYcVAMMOGe1GHYmgIRaVMmLZg7KPfikcW81nxcTGRtsABOiJ5-h8Bip0BsS693PQvaK1_B1pduEjPu-7MDh3P_1qomfkfkYL8_bzvxOysZqiaffSkoOst5x-zi0LtojWVchjIPLDn3j1iRqocMu9GDjo68JA5nbXN4L89oik1DE07iOI0gYq40W35yWTNazsDX8sdjS6H8r391cVCLSeGsn-DcB_vqbNqKBzjFlBPS8BrgO4UH84T_DYOztpfFTHu2TPp0dC0HjWFd3YCcYs7wmTdYiSuNmgwmBkXlDLpzd4qsDUprvy79LV4IFA4Wqgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
چهره خوشحال پزشکیان در استقبال از مقامات کشورها
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67242" target="_blank">📅 17:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67241">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4864316f1d.mp4?token=mbRhuqC8pwKhdRr-p5VchtPf7ev1RYCfFx0U5O9z8R5bmk3sG4NvdwWdFxorHBWpqoQlfMku-iofdnhzWyc8nUHTHAGnPOER91rkE1BpntFMYLARGQYiRgtZnNAaTD9QvwzkzXEIQQd73kzrR9SQJn3YPE8D-gPeqvye9QCTAF6acpuiNvK2_sPmbIQnzW7hHosZsb38lI33AQWbDtXZCNeKUbLXu4G4uyda_8nU0Q1FNA4IxjxgDYouWHEEd777MH22ld41MGi3TV0h3Su0MdNn8v2AGDK7-uQyu7MyP3yDFW2-BsYx_C3Tmv8bvmgNIWGoIslQR3MAcEN_8FTpdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4864316f1d.mp4?token=mbRhuqC8pwKhdRr-p5VchtPf7ev1RYCfFx0U5O9z8R5bmk3sG4NvdwWdFxorHBWpqoQlfMku-iofdnhzWyc8nUHTHAGnPOER91rkE1BpntFMYLARGQYiRgtZnNAaTD9QvwzkzXEIQQd73kzrR9SQJn3YPE8D-gPeqvye9QCTAF6acpuiNvK2_sPmbIQnzW7hHosZsb38lI33AQWbDtXZCNeKUbLXu4G4uyda_8nU0Q1FNA4IxjxgDYouWHEEd777MH22ld41MGi3TV0h3Su0MdNn8v2AGDK7-uQyu7MyP3yDFW2-BsYx_C3Tmv8bvmgNIWGoIslQR3MAcEN_8FTpdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان در تلاش برای جاری شدن قطره ای اشک از چشمانش
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67241" target="_blank">📅 17:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67240">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/597b986b2a.mp4?token=gtE0PkH6vOdykd-R0MukAgS20dYKGPB4d3sqP05OBTIKrqSEQ1KdFYcd_XAD54guhzdAE5LgNrQh7LV1SKTvEbLUaNcAlLp4nVvSQDEZfjQ1QkIX9ip_tfkR5bX1bu9Mad6y_pPLxr2dVjlMN_24mf0JuPeTWgepYhGK9ZP5owUAbtE9xtQOKnonyKPcndx9PYcsFgsgrUUvn-lmb7olC-_f4Fop5Zh_ceScvHWuLq7tAtvPgiFZP97b6iqHim2YXwFULovjGaTGdYelfz82IfPHzfSYqKUXudTsHboLw2wDIUWbkb2HiPOeFSORwjCfFrAzB0ygNaKK5wCYBaU9GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/597b986b2a.mp4?token=gtE0PkH6vOdykd-R0MukAgS20dYKGPB4d3sqP05OBTIKrqSEQ1KdFYcd_XAD54guhzdAE5LgNrQh7LV1SKTvEbLUaNcAlLp4nVvSQDEZfjQ1QkIX9ip_tfkR5bX1bu9Mad6y_pPLxr2dVjlMN_24mf0JuPeTWgepYhGK9ZP5owUAbtE9xtQOKnonyKPcndx9PYcsFgsgrUUvn-lmb7olC-_f4Fop5Zh_ceScvHWuLq7tAtvPgiFZP97b6iqHim2YXwFULovjGaTGdYelfz82IfPHzfSYqKUXudTsHboLw2wDIUWbkb2HiPOeFSORwjCfFrAzB0ygNaKK5wCYBaU9GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در یک سو مردمی که در زباله‌‌ها باید دنبال غذا بگردند و در سوی دیگر «تامین ۱۲ هزار تن کالای اساسی برای تشییع قاتل فرزندان ایران زمین و عامل شماره یک تمامی مصیبتهای مردم ایران!
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67240" target="_blank">📅 16:26 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67238">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b4f0f3e3e.mp4?token=LCuO6G-hE-pE1l1Uc5L4TPJgYHLmTc_hCbFeGRxawvHWwsbyW654quoMiBcN5Rpim6UtUEGe5jOxKYLEl4Fn4LDyxZU4wwh762u9zuatDBYCY0ige8wx8m7XnePmXd-If8eje1vxNv7khSjCMTQLbkxr-GGzTdwv-gWGMIM9xLcY4Zriv9rDPh6HL6wBeLftfqG29DGrCu2j6qSR3vuSGtisbzrxz-p0XDOSAUChs3iHtDS83F1A8KmGDrequ6DvslEtZXQ1o3ghb0nqD-F88Ne0_Mr0c6yl61t9iaYKDyCfWpCz5XUjgV1M60l6_Z03o6LaPgb-sfbT1GlO7WfO_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b4f0f3e3e.mp4?token=LCuO6G-hE-pE1l1Uc5L4TPJgYHLmTc_hCbFeGRxawvHWwsbyW654quoMiBcN5Rpim6UtUEGe5jOxKYLEl4Fn4LDyxZU4wwh762u9zuatDBYCY0ige8wx8m7XnePmXd-If8eje1vxNv7khSjCMTQLbkxr-GGzTdwv-gWGMIM9xLcY4Zriv9rDPh6HL6wBeLftfqG29DGrCu2j6qSR3vuSGtisbzrxz-p0XDOSAUChs3iHtDS83F1A8KmGDrequ6DvslEtZXQ1o3ghb0nqD-F88Ne0_Mr0c6yl61t9iaYKDyCfWpCz5XUjgV1M60l6_Z03o6LaPgb-sfbT1GlO7WfO_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ارتش دفاعی اسرائیل:‏در واکنش به آسیب واردشده به نیروهای ارتش اسرائیل و در پی نقض توافق آتش بس: حدود ۱۰ زیرساخت سازمان تروریستی حزب‌الله در جنوب لبنان هدف حمله قرار گرفت
🔴
در حمله‌ای دیگر برای رفع تهدید: نیروهای لشکر ۹۱ یک کامیون مورد استفاده حزب‌الله برای انتقال تسلیحات را هدف قرار دادند
🔴
در حملات دقیق نیروی هوایی با هدایت لشکر ۹۱، روز گذشته (پنج‌شنبه) حدود ۱۰ زیرساخت متعلق به سازمان تروریستی حزب‌الله در مناطق بنت جبیل، بیت یاحون، کونین و براشیت در جنوب لبنان هدف حمله قرار گرفت. زیرساخت‌های هدف قرارگرفته توسط این سازمان برای پیشبرد طرح‌های تروریستی علیه نیروهای ارتش اسرائیل که در منطقه امنیتی فعالیت می‌کنند، مورد استفاده قرار می‌گرفتند.
🔴
این حملات در واکنش به آسیب واردشده به نیروهای ما در منطقه امنیتی توسط سازمان تروریستی حزب‌الله و در پی نقض مجدد توافق آتش بس انجام شد.
🔴
همچنین بامداد امروز (جمعه)، نیروهای لشکر ۹۱ یک گروه از تروریست‌های وابسته به سازمان تروریستی حزب‌الله را که در نزدیکی منطقه امنیتی در جنوب لبنان، در حال انتقال تسلیحات با استفاده از یک کامیون بودند، شناسایی کردند. بلافاصله پس از شناسایی، نیروی هوایی برای رفع تهدید علیه نیروهای ما، این کامیون را هدف حمله قرار داد.
🔴
در پی این حمله، انفجارهای ثانویه شناسایی شد که نشان‌دهنده وجود تسلیحات در داخل کامیون بود.
🔴
ارتش اسرائیل به فعالیت برای رفع هرگونه تهدید علیه نیروهای خود و شهروندان اسرائیل ادامه خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67238" target="_blank">📅 16:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67237">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KdbmmFl4u9WmTcCDsyMkQoEJ-w4vh246RIt9vI6jrfyGqTg7uXrszvZk5XIIkeu-I1knKa4xHguNh4n67z9B8VNSNatXeGfTG3ja_4aAKBzW5UQkd4E571-x5nsjDEg3LND83gBUuQEiBywBYEWb_3RRDOMM67yJPkJRGHz3yx5SW8SQzlEh1X8wp1SzdVqT9G3Txa-sY0iMP-GwFncUteHJiN7eujoSRsf1vc-Gt_9fRPw1PcOUTHX3WqBgS3VLQS61tCyKxvod74kSKamfUCSQxES4toalJaTE8tUCeLlHDphPycpvaG3QhsxjQDKY7xpgESVdssuQrqGonLHRuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
پنج فروند بوئینگ ۷۷۷ سعودی سابق علیرغم تحریم‌ها به ماهان ایر تحویل داده شد:
پنج فروند هواپیمای پهن‌پیکر بوئینگ ۷۷۷-۲۶۸ER دست دوم از خطوط هوایی عربستان سعودی به ماهان ایر ایران تحویل داده شده است که دو فروند از آنها در فرودگاه مهرآباد تهران تأیید شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67237" target="_blank">📅 15:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67235">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dmyBF9by3E2HynC_5ciF_XAdFK_JM7tp3kVvqzTRb0ipqujkGB5n-7z4JCaW3dGEwTF3nUi8vzinAFNFQYHNj5urSItfXmXVsy5CCzgs3cLe1h_3gbUa8HXzOhFXubbatPUKq0QAPglorkUezuTrlmUmny-mJOB7WwnDzlp0muXp-k7uQ15dUH-q-dWq4iULgj7cIJINrkvtAz250OvkiHOT9MTq4W1ILvYZeUqM1KTpo1t39AJVS5m7osEMTFXmr8cLPwGsyz9OoDYWkuzxgLymotLZDmeyfiA4OKc-SIRGEN1qzZ1I8HN3apCcKSfrpN8rVsuiYKfnkcioGgH41w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e169f3d67d.mp4?token=nDsL2wjOAvmBcUT0S3PmSPyITWtdM70eMBzPVhPZIIG1MkHbWAuUlLzKPjLgU6b1KHsE0CYwsNpUzMWr4FBP2okI6rhn2quZ_RpOLgBt3kYGgRFEA4MrP-W2jlf1Vrz_b77Ju_kXRqp4w9CHtgegoV2yApmKHfCTGI9ZyBYbEYf3gn3v2iPFFdcyGTRQO9xZk62QZWicO9jRKLSdWgFt1v1YfQ59unQZ4hWGuBsGVM1n0sgaLXz-Tfl9TWZJnu-C0gVogMj6dFn850iHFp4MvGkLKCgqdZonYO1mJyKMZK9Q9_2rNFdXAoxb7txj6AvJETfJEMzB_2Rxg6XoyQJqIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e169f3d67d.mp4?token=nDsL2wjOAvmBcUT0S3PmSPyITWtdM70eMBzPVhPZIIG1MkHbWAuUlLzKPjLgU6b1KHsE0CYwsNpUzMWr4FBP2okI6rhn2quZ_RpOLgBt3kYGgRFEA4MrP-W2jlf1Vrz_b77Ju_kXRqp4w9CHtgegoV2yApmKHfCTGI9ZyBYbEYf3gn3v2iPFFdcyGTRQO9xZk62QZWicO9jRKLSdWgFt1v1YfQ59unQZ4hWGuBsGVM1n0sgaLXz-Tfl9TWZJnu-C0gVogMj6dFn850iHFp4MvGkLKCgqdZonYO1mJyKMZK9Q9_2rNFdXAoxb7txj6AvJETfJEMzB_2Rxg6XoyQJqIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
بر اساس گزارش‌های اولیه، جنگنده های عربستان بر فراز صنعا، پایتخت تحت کنترل حوثی ها، به پرواز درآمده و مواضع این گروه در نقاطی از یمن هدف بمباران قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67235" target="_blank">📅 14:57 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67234">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iAjGTLN4ijGl0AraxNe_JeNYO9GEFnYQWWEb-R7zypkf2Jh0ejxDuPHy4gPhu2cNaDYe5Y_HJGZWt4ob9N-dxPEkOekxEJ_D16jUhyTER98wfB_CoFvnz6UbwDS_YsTm_l7g50vUBQ4tjdO4_LdAn-QfyKYRG7C4QhMdCr99oWn9PU7jUmZzyRJPBJjZiBCt5WKoDf6o0YRcerT1cXdTLk_8nVT6L9J3g1PM2qs6Yjn0epNCGxUAeQ56Quv3ugVxJNHGXga2G3FdZX8120EJ0Hx3mfs1UWgoONVr3w3v7XavXzwa93P93UVtGOfpT2bRiQfbh3u1HZLCl-KBQTDmXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این عکس از تفاوت تابوت محمدرضا شاه پهلوی و علی‌ خامنه‌ای وایرال شده، تابوت شاه کاملا ایرانی و تابوت خامنه‌ای شکل و ظاهر عربی داره.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67234" target="_blank">📅 14:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67233">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4654e8258.mp4?token=vV3ZwdtmNCO411xc3101jqhI6RBx0oMSnwOzuirbapj2d7JEuxONspP0-dgqhUlE1AENXIXuYKcxRLNG3NVviZbc1xV1IB2ZCE_YiGxzwuAY-oUCwF9ZoeZl9ialaFWigzr2nq2AkBToeeZQUrJoZquWBg7o1Tp6tTFJp1K7sQgq_OXmTydByQ7EMO42LILQAVQuv0RR-55Auvs2CMjemgMAxq9WxTK5BZPDxbKzdJB0k9L6hIvI5WZ6WYcCSijyzUqVNmb8l4esiY6ylkfQ0_i9aTav1pbREgncsVmjF39vX6be2sW9zFlaxqPB3PXESWRmNkcxwYF1Uu-U4CFpzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4654e8258.mp4?token=vV3ZwdtmNCO411xc3101jqhI6RBx0oMSnwOzuirbapj2d7JEuxONspP0-dgqhUlE1AENXIXuYKcxRLNG3NVviZbc1xV1IB2ZCE_YiGxzwuAY-oUCwF9ZoeZl9ialaFWigzr2nq2AkBToeeZQUrJoZquWBg7o1Tp6tTFJp1K7sQgq_OXmTydByQ7EMO42LILQAVQuv0RR-55Auvs2CMjemgMAxq9WxTK5BZPDxbKzdJB0k9L6hIvI5WZ6WYcCSijyzUqVNmb8l4esiY6ylkfQ0_i9aTav1pbREgncsVmjF39vX6be2sW9zFlaxqPB3PXESWRmNkcxwYF1Uu-U4CFpzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
حضور فرماندهان ارشد نیروهای مسلح جمهوری اسلامی در مراسم وداع با جنازه علی خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67233" target="_blank">📅 14:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67231">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_U4_FU-G05CQBr-bHGOy19gjmcSVvy6N_nX5EFUUVdpufQsHDXdBaEqngcTgfA_oi7JyJTnDfjkjEEx_Jtii0G8KpssO4vRfWMJSx2P4_Pi7Nb90ifG1cBcO2MmRhx79vVqdt9C-ffDCvdx_ljmQM9R-pdv4AmxrbOyM9ujZ-_hI6QcbuuSDONA-Gw2mOMSmwRXk9AWaVVhwsR7oZP-jc_R4gUGv_mW_8KQD7gkzifOkV_8p7aWWY-PA0RwuY9YjQnCFLyBcZKkvad22x2YRNRPDQ49ngTK_sMjNKDAjfqstPyp9-JclwYtj5OzF4YgnvcvD2tjEquWJDkspGSyeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1483e21a1f.mp4?token=DAFZycUKAI0IPOKSqRZVthsbR1pcg0IoAxq2PN1i7OAXdXOFivI0-Go5eHJL-UbMVx-H05ck9ihUGAHq2Tj4cdCAEcvs8sq-GkVl70DzJpuYZQWMhVP8GfhncqfxJICy-Iox2sQR3_-tbpj9Z84Mn23L7qdjauPl1hBdLG-MIpkQIdlMyUXTgGj9gLUGFPqfUGlOI9RyiB0L2sNJz3S5-jVl8oFr0b9n_GyOwTjUM7eHFnXQT2SrZcP1E345pLaeekK3ZEVM9txm74xW3qjNESxe8e_blyCOD5iFBRrbMfYhaHi2Es-nbFGR02Bl9w3BVQofJjc--5ek1RNWOQn3dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1483e21a1f.mp4?token=DAFZycUKAI0IPOKSqRZVthsbR1pcg0IoAxq2PN1i7OAXdXOFivI0-Go5eHJL-UbMVx-H05ck9ihUGAHq2Tj4cdCAEcvs8sq-GkVl70DzJpuYZQWMhVP8GfhncqfxJICy-Iox2sQR3_-tbpj9Z84Mn23L7qdjauPl1hBdLG-MIpkQIdlMyUXTgGj9gLUGFPqfUGlOI9RyiB0L2sNJz3S5-jVl8oFr0b9n_GyOwTjUM7eHFnXQT2SrZcP1E345pLaeekK3ZEVM9txm74xW3qjNESxe8e_blyCOD5iFBRrbMfYhaHi2Es-nbFGR02Bl9w3BVQofJjc--5ek1RNWOQn3dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس حوزه انرژی: تنگه هرمز از مسیر عمانی، اتوبان شد!
این فیلم از موسسه کپلر را ببینید،
چقدر تلخ است، کشتی‌ها و نفتکش‌ها در تعداد بالا از مسیر عمانی از تنگه هرمز عبور کرده و همچنان می‌کنند.
با این روند، به زودی ترامپ بابت تامین امنیت کشتی‌ها از مسیر عمانی، عوارض هم می‌گیرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67231" target="_blank">📅 13:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67229">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50fa301248.mp4?token=kdv0s_IaE6T7pbhDpcxJFDmKoMHAmrLHSexkr0tc8FExnGRuy6yK1pK3U2LQBX6d3vtNGpRAnGXqdUqAn93hZW7AvtkGY792BJIjxoOhPcoXtJy2g45icsunhZUxQdgj4INHcAG6jXiPmflMv35rPPqjJf29GSPEe4gGTEkLtfb1I_O0bJhR0GQfG3crL_zWbjgY8GItpeR2ig3vUSPu90H9P3gE789G7KqYx90sLtnhoDgMWosNrVZCr5uvakgoCkDVa9YxufVix7ymW5g3yyHyfaVNXDZ5UASRobVyq_KB9rvCX7HIRm7praIu45uvEfKcuvCt1slKl-MKStzBkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50fa301248.mp4?token=kdv0s_IaE6T7pbhDpcxJFDmKoMHAmrLHSexkr0tc8FExnGRuy6yK1pK3U2LQBX6d3vtNGpRAnGXqdUqAn93hZW7AvtkGY792BJIjxoOhPcoXtJy2g45icsunhZUxQdgj4INHcAG6jXiPmflMv35rPPqjJf29GSPEe4gGTEkLtfb1I_O0bJhR0GQfG3crL_zWbjgY8GItpeR2ig3vUSPu90H9P3gE789G7KqYx90sLtnhoDgMWosNrVZCr5uvakgoCkDVa9YxufVix7ymW5g3yyHyfaVNXDZ5UASRobVyq_KB9rvCX7HIRm7praIu45uvEfKcuvCt1slKl-MKStzBkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
پالایشگاه کلیدی لوک‌اویل در روسیه هدف حمله اوکراین قرار گرفت!
این تاسیسات سالانه حدود ۱۷ میلیون تن نفت خام را فرآوری می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67229" target="_blank">📅 12:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67228">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kt1V0Mgvn4PnPVztTGYkkw44rnXN-vXZeplMiY-yOO62VxJ1jszsGDQaGJcrHCI_TXxEqy51-S_qzaO6jyFKB10tKHA6psD3NA0vJezBs5F2ohOzMGUcR5ulbMwk6yprmrjN-NCQRmLU1i3LSGVYm81Jqh2pWllxuVpiI56TVwRf8_kcmIm_0-gwbsbkO01oUAvrlWZy63r4jYvWmJzQXN0bmQlD_Vr4S9Xo9I--KjEUyTNRKr7AnmABCOlGOeszsg4bfA2mkYB7o84UH1WUtC6ll1XRX05_kZkuGxO8KvUDmRAPIC1oOULolQLcjriHiOAuPtp67HIbPgxZB_zHRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
همان‌طور که ترامپ درباره درخواست ایرانی‌ها برای برگزاری جلسه در دوحه دروغ گفت، دیشب نیز دوباره دروغ گفت؛ این بار درباره حمله به تأسیسات راداری ایران. نه جلسه‌ای در دوحه برگزار شد و نه حمله‌ای به ایران صورت گرفت. هرگونه حمله‌ای از این دست، با پاسخی کوبنده مواجه می‌شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67228" target="_blank">📅 12:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67227">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QbEZRkaF2KFpyqrqZMNbRQN9-MpqAjXi8PECu3JCcu36M9H5c475sigqdtQCRqMryLq_SejNU-KeFp_HEbuxnQ_xKSiHuvNdZBNGbO17s0bE-AOi5clmFgYCaixSiHqt_HIpWRlvqcxh8hEos8CQ2MMsvEbAc0ZRtkJLd_3a1AVvvaT7Wh6bANZ-uDiSwqLPClTs8Ca6hpX8N8T4geCkG3tsjOl0mK_RLq6jeav_SBmGmo12ybFiS2bfJEZs07ELWq6RSh4tPGSrh2cHKjDp9S2SqTEk0GcT4uDcv58zV9LRoHM6ZvM-MvZie4vFge5_JhDh0REztWgkKoau-SDBgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی طلات رو روی ۱۶,۹۰۰ فروختی و توی یک روز،
قیمت طلا
۵۰۰ تومن بالاتر رفته!
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67227" target="_blank">📅 12:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67226">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cSN8gJ4yl-mmHs4vKpDw9RCdtZDX--v5G0C2xDLIR-VDq_ik9jXD381tx0fQmekxOiVmjPnU9qe_Tbsw2GPbREPXOvsuERjTM4NBUV0178juJ_YhIyMBP1N84gmKPqzdVG--l5Q_vr3dHQz-keasG6eavTpwyNT6PnbEBVqUdg9LzSUkai4vACHzVN0I0Iv6XH7CQWda5XCf-obG43lC9BXxQOz260LmgiyyNyiMUhABjg4CDsPMxn3p5r0_zCE0F99LHitryjMx-UJDiiDz6-ZRgNaJaLHZ1dCeo-AiAqaRoU4i4uNe-G4GvqZ2VY_xs5Dh2OdX2GZJ48YVfBAe1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توییت جدید محمدجواد ظریف:
ایران، پس از دو قرن تجربه تلخ ناامنی و آسیب‌پذیری، با هدایت رهبر شهید به مرحله‌ای رسید که در گزاره «دوران بزن در رو تمام شده است
🤣
🤣
» متبلور است. این تغییر پس از دو سده، احساس خودباوری و اعتماد به توان داخلی را برای ایران و ایرانی به ارمغان آورد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67226" target="_blank">📅 12:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67225">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f10282a802.mp4?token=bA8w9lM6BJVxUoXuXw1eHCyR7eDqF1T43ohnKJZNwxOnhbJYoLCewru9WD7Kja1-KiTUi32ItVyAzUJPwKlh1GXgiG_n4eCqUyblZkf9_rP1UIvW08hi8SvzUcetpgSHFq1nvu30kgcteIRZVZxHptoKq_M83ZEfx4zLdALPR_DfhxZnQKC9fLOktg70LejVn6ril0MHXzOqzxbV_ZIDBLJMtBv0NoabzFdid1wg1ryvBBKHk274FBotP7hLbKj3UAWC4DbKw97xXaA2KdaUZ8hRBefKISpNlLntFelVMNeGy8VJjrqDO254yZG9XBE1pg6RNIp0XIYyxP9_seyIKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f10282a802.mp4?token=bA8w9lM6BJVxUoXuXw1eHCyR7eDqF1T43ohnKJZNwxOnhbJYoLCewru9WD7Kja1-KiTUi32ItVyAzUJPwKlh1GXgiG_n4eCqUyblZkf9_rP1UIvW08hi8SvzUcetpgSHFq1nvu30kgcteIRZVZxHptoKq_M83ZEfx4zLdALPR_DfhxZnQKC9fLOktg70LejVn6ril0MHXzOqzxbV_ZIDBLJMtBv0NoabzFdid1wg1ryvBBKHk274FBotP7hLbKj3UAWC4DbKw97xXaA2KdaUZ8hRBefKISpNlLntFelVMNeGy8VJjrqDO254yZG9XBE1pg6RNIp0XIYyxP9_seyIKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شاهزاده‌ رضا پهلوی درباره اسلام:
🔴
من نه با اسلام دشمنی دارم و نه با هیچ باور دینی دیگری. ایمان، امری شخصی و محترم است و هر ایرانی باید آزاد باشد که دین خود را انتخاب کند، تغییر دهد یا هیچ دینی نداشته باشد.
🔴
مشکل ایران، اسلام به‌عنوان یک باور مذهبی نیست؛ مشکل، حکومتی است که دین را به ابزار قدرت، سرکوب و فساد تبدیل کرده است.
🔴
همان‌گونه که هیچ دینی نباید بر حکومت مسلط باشد، حکومت نیز نباید در باورهای مردم دخالت کند.
🔴
ایران آینده، کشوری خواهد بود که در آن مسلمان، مسیحی، یهودی، بهایی، زرتشتی و افراد بی‌دین، همگی از حقوق برابر برخوردار باشند.
🔴
معیار شهروندی، اعتقاد مذهبی افراد نخواهد بود، بلکه پایبندی به قانون، آزادی و کرامت انسانی خواهد بود.
🔴
اصل جدایی دین از حکومت، آزادی عقیده و برابری شهروندان.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67225" target="_blank">📅 11:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67224">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/226825be38.mp4?token=YGw5yvcolkzwp0uFVOwCJ7DDz5i5PPSWrhR8TXjyU2jYq0PCP8-kLLLjateNXRwkPzhcqbG9FZnyhmkP1pOj1XMHZvOc7XE2_WXJxojrFp5I1bXkABLRZGhNUweLdauHqbZhIoXTp3A_kUUQ21dP9Aeqxq0zy5woebT_M70L_PiYN7SSUWSbFp30yTguV60RlpIOrqNEMA5Zlgo5Y9rPaREMhPSff2A3axOjXXGpS3HKKyaJvtDP6F3ArKcDMan927HPYkURaqk5AANMRuJ2zMUBCYg9GZ505g76REZ04tVOP9FlAmi2nk6pkHg0NnGvEjvNZGtZ9na6QN--7Wl3Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/226825be38.mp4?token=YGw5yvcolkzwp0uFVOwCJ7DDz5i5PPSWrhR8TXjyU2jYq0PCP8-kLLLjateNXRwkPzhcqbG9FZnyhmkP1pOj1XMHZvOc7XE2_WXJxojrFp5I1bXkABLRZGhNUweLdauHqbZhIoXTp3A_kUUQ21dP9Aeqxq0zy5woebT_M70L_PiYN7SSUWSbFp30yTguV60RlpIOrqNEMA5Zlgo5Y9rPaREMhPSff2A3axOjXXGpS3HKKyaJvtDP6F3ArKcDMan927HPYkURaqk5AANMRuJ2zMUBCYg9GZ505g76REZ04tVOP9FlAmi2nk6pkHg0NnGvEjvNZGtZ9na6QN--7Wl3Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نریمانی مداح حکومتی:
منطقه شیعه نشین جنوب لبنان ۱۱هزار خونه صاف شده، آقایان چرا نمی زنید زیر میز مذاکره!
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67224" target="_blank">📅 10:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67223">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uIseKigDJnjKzjlryZ6WYCF5mUgokDr3a9fubZVz6YT3fWcdgEKOFkUHwEfMS4kTnUlGfIM85GcAlYYBOEolDEAcVWs08LzP4xIIW_3d4_mGeYRJIZaJK-_aXGBcdgKNvBE2aFMc0kEzcinJv9LEDsj6aZ2VpaGUs6FNN4uVCnMT1v7aoDcKPGPaxnkghqW0MpGEmSgCikgNLjdxmLBWG_zMaqAJUEk1e1XnAJLdNpfvHlN49gU6W_UWaPAHuX_VUYghOuM1ui0wJ4w5xxVCr6QXNzzL6uyK45K5riUv4vsFJMbbc_kz5L3s610Q_WZbFlVV_jTMd42PeqRJoaePjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گفته میشه بانو الکسیس پورن استار معروف اعلام کرده با مردای همه کشورا غیر 2 کشور رابطه جنسی داشته، ایران و غنا
برای اینکه کلکسیون خودشو کامل کنه، گفته فرم پر کنین و درخواست بدین تا یه نفرو انتخاب کنم.
از غنا 2700 نفر و از ایران بیش از 1 میلیون نفر درخواست دادن! جوون ترین ایرانی یه دهه نودی 10 ساله و پیرترین یه پیرمرد 78 ساله بوده
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67223" target="_blank">📅 10:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67222">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55805ed771.mp4?token=kFUj-PgClWDmXPOI7hOBjml4lpfVs2KSaBd7srT3-cSJcd6s4vzeOtOHiWQUojxRUtnWcKY79U5w1XVEtklucT5eH2tZ7dvrthTPPrOrU24xJ21kK3fY66MFkwq3Qe84-q6KML0cpchCS-QmoMmXG29LXKuJgqAnLIJr2G-JVhngGMVtlByOYQQ6W-2YKwEfnTKi0LbDPeWadvEn2sAg8uLwDjlLsSTnQDSQbThf88WmX28MtCIaftpH8TvF9SizjQqCdi6-a5AVu1kp3UHZyBr3GGkkfFf94-Zx-PbfUmRPRP8Q9Betsn45C86tqPhrqfWGJ5r8HtGKjQGYIqzg6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55805ed771.mp4?token=kFUj-PgClWDmXPOI7hOBjml4lpfVs2KSaBd7srT3-cSJcd6s4vzeOtOHiWQUojxRUtnWcKY79U5w1XVEtklucT5eH2tZ7dvrthTPPrOrU24xJ21kK3fY66MFkwq3Qe84-q6KML0cpchCS-QmoMmXG29LXKuJgqAnLIJr2G-JVhngGMVtlByOYQQ6W-2YKwEfnTKi0LbDPeWadvEn2sAg8uLwDjlLsSTnQDSQbThf88WmX28MtCIaftpH8TvF9SizjQqCdi6-a5AVu1kp3UHZyBr3GGkkfFf94-Zx-PbfUmRPRP8Q9Betsn45C86tqPhrqfWGJ5r8HtGKjQGYIqzg6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پروفسور جیانگ:
آمریکا احتمالاً بین آذر تا اسفند یا حتی زودتر حمله زمینی به ایران را آغاز خواهد کرد و امضای تفاهم‌نامه فعلی تنها برای خرید زمان است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67222" target="_blank">📅 10:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67221">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/szP7KYIhIDiYtjiqufMjkAivna6QazWx2PIWNWHCPSt3xC3Hc6j_4-EkxL33rd-I39ZYDfB1Uymu0affU7TGKbHYjYyP3cEcQsClDb5MDqosj4bnUhIVTFiFBDy9IAb7sVTtq7cMaEEJR2udM5ySwEZ91PrHKsfVZ5dEWseCWMkRl5ua58Fp8nJllR1vVovQbF-1PUcMo_OODWis1-A4CtFSuZcp-8xTj0sCT5GPdBUtRY6AaAyqPjp_8-dmtyYAgl8e7VbCW9UILhg2n0jbQa_eU9E75KRhohzJT8iNMTNNk-AOEMc0gDGI-vx4T4vV7Qxv2pPJ7_RBO5zCzfJBdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیشترین فاصله زمان مرگ تا زمان دفن رهبران جهان، مربوط به الیزابت دوم بود با ۱۱ روز فاصله که سیدعلی خامنه‌ای با ۱۳۲ روز فاصله با قدرت این رکورد رو شکست و نام خودش رو در تاریخ جاودانه کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67221" target="_blank">📅 09:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67220">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f82b0159b8.mp4?token=fdJYcVi6liJ4Q3hybqsc0-D-vY5aE6TXE-NsP0N5r4lxI3g_efszPdwaDU2fPuJnPm3to-OoQ4P7FC4CRdat0MSZLCrdufGSe9ZWT1xrWnRN4U4DA0SdHcdy-H5ptezdbkSID8xwDJkCWhI3Ib0nSmgfsc8ji5DiyVdkq3hpxzkAR97wz5u2tUb5yeVbBK8wEFeWLqVGfBLVVQz7aYv1EmNsrqtoSwRmJYjvxqah0lKLu5_bLTqgb1qn93qF20FAG1vSp9zp7dwhMtMoOwOM_X_tpyY1g5zvQ2KFIg5EawIIZwJ1V1GIO5dVxYulkI5roFBxcsQgVHD7ccONCV2-JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f82b0159b8.mp4?token=fdJYcVi6liJ4Q3hybqsc0-D-vY5aE6TXE-NsP0N5r4lxI3g_efszPdwaDU2fPuJnPm3to-OoQ4P7FC4CRdat0MSZLCrdufGSe9ZWT1xrWnRN4U4DA0SdHcdy-H5ptezdbkSID8xwDJkCWhI3Ib0nSmgfsc8ji5DiyVdkq3hpxzkAR97wz5u2tUb5yeVbBK8wEFeWLqVGfBLVVQz7aYv1EmNsrqtoSwRmJYjvxqah0lKLu5_bLTqgb1qn93qF20FAG1vSp9zp7dwhMtMoOwOM_X_tpyY1g5zvQ2KFIg5EawIIZwJ1V1GIO5dVxYulkI5roFBxcsQgVHD7ccONCV2-JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان
:
من به عنوان مسئول دولت نمی توانم ببینم مردم مشکل دارند و بگویم همه چیز خوب است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67220" target="_blank">📅 09:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67219">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">📈
کنداکتور فرم های امروز
💸
مبلغ در نظر گرفته شده ثابت 100 دلارز
🔥
سود کلی 1,287$</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67219" target="_blank">📅 02:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67218">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromFuck Bet(cheGuevara)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MBk173d6NG_SFb9eKct9Be7zAVmq1Z-OsDGWhyWAit7T0wCqyLwT8wdMJyV85wQD72buDJXBs_fXVBb3mPBMu5IBJAxJHJqdv8SdevYkcDCxu5XXukp4RcRMQZudBlU4Zy4KmPEs15w9A07yY5qOqGqn132XvGqErJMDYIw8GMBgKcGz4NqAXLENqdn4VFycnwRmuKiJVlhryWDEWlFWXexpo9n8sq_a8zzBWOMG-eKPGQmQfjfQ9fb6YYu9p5-eR-Cm53y2q1IvnBpxlELNGJaYeUechAlX3SnhfRcrYQDGQ_pV3Ib6YxVQ_9gzw-DmkW_z_Ub3jI0ae6KemXT-aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📈
کنداکتور فرم های امروز
💸
مبلغ در نظر گرفته شده ثابت 100 دلارز
🔥
سود کلی 1,287$</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67218" target="_blank">📅 02:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67217">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54a8c8202f.mp4?token=S1ObtrM7hpKPPkKhrwRZ5WUEApc3DAo1DTF5PvCowUHc6MWF9dx4Qoq_U8XIlTZYMAdSeu-W5WPuHWaZxyBXoQO5E_ts-PfjflaydmNEC07Vcc8Xh4i70mwvV5WlzP_YWGTJG5n3roqjE80ADW9DhXWOna9BHK_uJdjcEHVOuCY142DDQboFdky47ru_3yHNFu3WcLeZP1uOc4DRJNuOF2egn-Ja9ZZzq2wqDCbWN2Frsi9UafUkWqo8cT08XGxUWwvJ-jzYyL_YHcQ-Utt-ZALxe4-AwmSpCBOOoJS4sUJwLGuWbhHf6BvKwMEgH6KNFTfOXaBQWGcBbqCmdu1L6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54a8c8202f.mp4?token=S1ObtrM7hpKPPkKhrwRZ5WUEApc3DAo1DTF5PvCowUHc6MWF9dx4Qoq_U8XIlTZYMAdSeu-W5WPuHWaZxyBXoQO5E_ts-PfjflaydmNEC07Vcc8Xh4i70mwvV5WlzP_YWGTJG5n3roqjE80ADW9DhXWOna9BHK_uJdjcEHVOuCY142DDQboFdky47ru_3yHNFu3WcLeZP1uOc4DRJNuOF2egn-Ja9ZZzq2wqDCbWN2Frsi9UafUkWqo8cT08XGxUWwvJ-jzYyL_YHcQ-Utt-ZALxe4-AwmSpCBOOoJS4sUJwLGuWbhHf6BvKwMEgH6KNFTfOXaBQWGcBbqCmdu1L6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«آن‌ها تورم ۳۰۰ درصدی دارند. هیچ درآمدی ندارند؛ بنابراین ما بخشی از آن پول را برمی‌داریم... و اگر به آن جایگاهی که باید برسیم، دست یابیم، تأمین [مواد غذایی] را منحصراً به کشاورزان آمریکایی می‌سپاریم.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67217" target="_blank">📅 01:38 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67216">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25ff4f4224.mp4?token=D99O17iDKWJDiDCchXW84omc_gA6HJFHpJnR6Drk6mgqcOad9KOSdAMW2WbkaW1xEiIJru0g6lZ2MyBd9YcaLs_PA_PzwFS_YUSAcwJ0nnthK45pKiW0fKnHBJwspNx8coeCpgpI7nXyi2nulL77XtvVHouZE_V5uKBrXjsiHQLiXHPim7W-Y76sItQ8FrK4CzEpT4FLVE_Zs1ukp0T4x0JbgDECFbmx9kkgskkWRFViZu-zfPI8LfdiVwnt0t2NDgl4vAa9SY9TpnL60JMmZlgtWjaz8kLrvRtf4aCgp5FwvyZx5EOrJ-BmkB4NJsUDUToUh_FhcwDxOdQz_j8gfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25ff4f4224.mp4?token=D99O17iDKWJDiDCchXW84omc_gA6HJFHpJnR6Drk6mgqcOad9KOSdAMW2WbkaW1xEiIJru0g6lZ2MyBd9YcaLs_PA_PzwFS_YUSAcwJ0nnthK45pKiW0fKnHBJwspNx8coeCpgpI7nXyi2nulL77XtvVHouZE_V5uKBrXjsiHQLiXHPim7W-Y76sItQ8FrK4CzEpT4FLVE_Zs1ukp0T4x0JbgDECFbmx9kkgskkWRFViZu-zfPI8LfdiVwnt0t2NDgl4vAa9SY9TpnL60JMmZlgtWjaz8kLrvRtf4aCgp5FwvyZx5EOrJ-BmkB4NJsUDUToUh_FhcwDxOdQz_j8gfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ما رادار ایران را منهدم کردیم. آن‌ها هیچ راداری نداشتند؛ هنوز هم ندارند. همین چند شب پیش دوباره آن را منهدم کردیم. آن‌ها یک سیستم راداری جدید و خوب داشتند.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67216" target="_blank">📅 01:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67215">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82798a9488.mp4?token=qf21aVob9s5jid_tHN1ISRJabGsMvUQ9eBR-fMoqASlKSIAxFJMvgkrr-CyXCmMm-zGpJ-597DLvJaylDgwfgX6AqALRRQfZ1oRQDLvPXT53sV-q5A7BWBp2fokuJ4fbeb6egFBfVsek-6Za9PflYcB4mwneMaf_C3XOvjxz0M8LZ-CJgCIbsz7L9E4EeuwZ4scjpfgEAjEMo7xFZ0T68T_NAy2PU0AuvuYMxgBVcgE7KREjiPoSsAGaEr7NW73AOlrWfezpidgAPkSoblIUlcFyFRXRjZRHyTI5OVana2lub3rPR2ympX--AwUYCwdG36PgeT-QjtgTQojbnS8nNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82798a9488.mp4?token=qf21aVob9s5jid_tHN1ISRJabGsMvUQ9eBR-fMoqASlKSIAxFJMvgkrr-CyXCmMm-zGpJ-597DLvJaylDgwfgX6AqALRRQfZ1oRQDLvPXT53sV-q5A7BWBp2fokuJ4fbeb6egFBfVsek-6Za9PflYcB4mwneMaf_C3XOvjxz0M8LZ-CJgCIbsz7L9E4EeuwZ4scjpfgEAjEMo7xFZ0T68T_NAy2PU0AuvuYMxgBVcgE7KREjiPoSsAGaEr7NW73AOlrWfezpidgAPkSoblIUlcFyFRXRjZRHyTI5OVana2lub3rPR2ympX--AwUYCwdG36PgeT-QjtgTQojbnS8nNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ درباره ایران:
ما آن‌ها را به طور کامل از نظر نظامی شکست دادیم. آن‌ها هنوز تعدادی موشک دارند. ما می‌توانیم آن‌ها را نیز نابود کنیم.
به نظر من، آن‌ها تقریباً به تمام خواسته‌های ما تن داده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67215" target="_blank">📅 01:26 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67214">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">‼️
لحظه ورود تابوت علی خامنه ای به مراسم ، امشب در حسینیه امام خمینی
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67214" target="_blank">📅 00:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67213">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IsTrXgtacrPizXYif6sPN5Y06H76nGxI1rgxAiYA04w3FkR8PojTBHdFaL-bC3ABh5pVLpvgLHkznvp3oSj3ueWdec3c08UkQ2lZHsZoBKftIMbynwYDhLtuF5UeSzJuC-ar0so9xJAWGaD_4I-4zpRtyO9fEzbIMwAMGdTuzrnsbXlVybeWxKaP4D8RRmOXpIDjoaOZBN3jTPyzY25koQsB_E14t-lRBtjRDBSRtid9lPdY9dGcrXzVLRFXi3dujrGqWNdjNb_WHx6VEv2F45LKyMmybjDqdjaoPVonfhnjHFb-akz_oOMyv5xmS2bfLIYADNhnksm2wCjsvtCqjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محمود احمدی‌نژاد بعد از ۴ ماه سکوت امروز درگذشت علی خامنه‌ای رو تسلیت گفت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67213" target="_blank">📅 00:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67212">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IERzcFWAWoHaBrQ3BEiM859IlhdtZJyeQGLnyKoSatyifKNpHdsUx9PMkz3qO0C1_vOQTIzXuVOaGYFysw-3RMlCVgwqSvoirJtrt9CGzJ54aRAo7TLh3ytkLGLRPGEsH0GePFuef9i6GxK9AUcXkVE9DBSmABzRBALyk_TxBFrnqldUDSki4DurHtXzmIgyG4uTLhMZKbmDEQN9Xu0U6Ncz98QvLI_cA7FWPF0--pWWItQOGkbK-6jHEfsf-TIm6E_kGU_z_v2Kse92SQJSQC7w8xN4SUHB24tHxvRsptnMlsVSbYme3T-yaF9t5BwXgBevCE2SZ7FVn59qkDBDow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📈
رشد همزمان انس جهانی و قیمت طلا در ایران
📊
همزمان با عبور انس جهانی طلا از محدوده
۴۱۰۰ دلار
، قیمت طلا در بازار ایران هم به مرز
۱۷.۵ میلیون تومان
نزدیک شد.
🌐
مشاهده قیمت معاملاتی طلا در میلی</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67212" target="_blank">📅 00:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67211">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iWj85n6pvW-nG3jEBF5MyPcIHyw9VCXlSfIUfh2e2mWa6EZ1yNe2BzbLctBpgJ4sR6zlSsQEeZPyExJVQW2FBU_KzAD-7oGmQzKs4XXl3LHuLwflSABV5zZmjBB-Iu4EvhkAOTTWfXus1NBqDi5tCmjr6p0lRAvypg_5ZsjvZtqf574lyBZBn73nHvr1qBQVUANUhaXv_pRVZPQkMx9DF8CwgAe-dCLhXZ0xvdqldDY_aHkvGu_fDv_53_jljOcx7Z37QwGnAJquh6mclatEswmS4kZQNKh0_iI7HA2rQTYWYBd3zU_Uo7j4Zvw69-f-SLK1f_6VW336rW2zQGQo-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصورم از دیدار ترامپ و مجتبی خامنه ای
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67211" target="_blank">📅 00:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67210">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1459d85069.mp4?token=kRwu3HG3gVL4WIGGm1fA-y60OTgQMXMIyvMSSpoI5P2lXAxBlbpag69bOsopRdQP3r-4U2Pe_5GrrWGWXY03djJcsdCEVuShOSGNUgk9ysgOag8uTVJF_OHQ_XqC1Ls73EjNWSq3wLLxzbTVNM2FARVdrsUDAaBw7EMcdpuSfcua5SoWHbbwhQUwVqaz3AmdG8fHgQFgjCz-ThdgiRuBqfAtpePghS4uOnNbsVdrkYiKc7dsGOyrJiMqI2Qts3dgrc_OwEd34YEl-qGDaIpbpYE5h7CqwOrAtxIpu9ywduX4sJ3-OV4qEgYzi-NwP9VMerxzx7egXEheN7sQOKCDXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1459d85069.mp4?token=kRwu3HG3gVL4WIGGm1fA-y60OTgQMXMIyvMSSpoI5P2lXAxBlbpag69bOsopRdQP3r-4U2Pe_5GrrWGWXY03djJcsdCEVuShOSGNUgk9ysgOag8uTVJF_OHQ_XqC1Ls73EjNWSq3wLLxzbTVNM2FARVdrsUDAaBw7EMcdpuSfcua5SoWHbbwhQUwVqaz3AmdG8fHgQFgjCz-ThdgiRuBqfAtpePghS4uOnNbsVdrkYiKc7dsGOyrJiMqI2Qts3dgrc_OwEd34YEl-qGDaIpbpYE5h7CqwOrAtxIpu9ywduX4sJ3-OV4qEgYzi-NwP9VMerxzx7egXEheN7sQOKCDXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه شبکه ۱۴ اسرائیل با جاسوسان اسرائیلی شاغل در سپاه :
در برنامه ای که الان تیزرش پخش شده و میبینید شبکه ۱۴ اسرائیل با چند نفر از جاسوس‌های خودش که در سپاه مشغول فروش اسناد و اطلاعات بودند مصاحبه‌ای کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67210" target="_blank">📅 23:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67208">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/N0h4Em9uCFhxAr-8HPV0cLXRIshRHSn7NLyYCeGExl0-uSH_03a-T5Xx4k30SJZVOzKDorktQm6npXzMxRsmsS_Zpekkq6bngDq3mlcqh_7e60pS5a4b49MEJ5cnSlTXBiK9khQyV2YASJAPEyV8sDDwC6j8oYkZEM4BvlXyQDRuLAAwHZ11bFqmVf7Dum3iZd38Dkc1KcahQgAgPjY7obwORKzg5JX3DTgzburGxTirnOtzxd78v-HjJN6g_glrZHYrRSDEScwqx5DEP2GxMnMAuxcPH4L2kVDgo1MplNs0MwBUbFnPFapGpbXBk_G6uJMEkYtioweLwIGAo1P5KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1f3d132bde.mp4?token=CsJ095k3wxF1AKQ0pYPBsboBm5poUSL2fF1Xu4xw3AJ_9YMshzcJV4p_0eOZ7UwkaMWlP8vMp7RI561ANFu4aTro0zdrtNhf1-il4CNPElnuf2uRiy1O5V6-e61eEbzQy4oEwNkKTtHaZH4CRmJlzHAdJIJlLnFWS6u7LIyTB28LHOjQ7651hm4rUtNRKRpMYSNKLwn_sjjI3_J2IFeDjRX-tmDXZ-eC6Y2f2yu8KXocRB1_01fPwLfEtEzLLnSfv7QpsYG01UYpTRAjbYEvJaFFkhdzuFie_QHlQ7lHlFKLFqvUTWHRXBAxxMLVSKB37Zo5DakTfz2qRo1L3YoP4A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1f3d132bde.mp4?token=CsJ095k3wxF1AKQ0pYPBsboBm5poUSL2fF1Xu4xw3AJ_9YMshzcJV4p_0eOZ7UwkaMWlP8vMp7RI561ANFu4aTro0zdrtNhf1-il4CNPElnuf2uRiy1O5V6-e61eEbzQy4oEwNkKTtHaZH4CRmJlzHAdJIJlLnFWS6u7LIyTB28LHOjQ7651hm4rUtNRKRpMYSNKLwn_sjjI3_J2IFeDjRX-tmDXZ-eC6Y2f2yu8KXocRB1_01fPwLfEtEzLLnSfv7QpsYG01UYpTRAjbYEvJaFFkhdzuFie_QHlQ7lHlFKLFqvUTWHRXBAxxMLVSKB37Zo5DakTfz2qRo1L3YoP4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
امروز ۱۱ تیر ماه، تولد جاویدنام سارینا اسماعیل‌ زاده هست.
سارینا اگه زنده بود امروز ۲۰ ساله میشد.
تولدت تو آسمونا مبارک
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67208" target="_blank">📅 23:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67207">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_rI3kwYKGV5E-l_qy3yNkIkhEXLBLoam2gUkZZNJBLl8f4R6mm29ov9WUto8SsziVecHmpi27HYBrLmQ213tsg9Jp68Mj8pibnr9AL-ix2IeQvlJi-61uMQnTgemdpjv3ee9HVYv3NmMjVebesQRuMrp6wSUjsOS391C47QrnDdfzEW-d6uDTzRrt0Ta9pC2_thpHgP8zZx6M0KlG_h9b5LgdZvc4BYPaEc0k7Rx54_0NJDBGgCa2doSIqeeAzKBjGtThUQ7d2pA9eoRtlhHRpfg9jmq9SduNjzt2wscXzD_fPkW3lnEb8N03Mgx2ezeWw-mGGHbRt_EtfhNb_P-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
رسایی:
طرحی جدید و فوری برای قطع اینترنت بین المللی بدلیل حفظ جان رهبر و فرماندهان در جز اولین اولویت های مجلس قرار خواهد گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67207" target="_blank">📅 22:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67206">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb76f1aa0b.mp4?token=nM4qQeD6XTxMgtPb61qzU3W-vjdN2RbNDYsgUlOVZvdlzsvzW7b4o3a_w66gTvjxDe4Ep48I2gmRUnUW84tMnF7YQsAFh8S8ckG82VwBDsxBFOlmhzhjRe3ZkzZG4IKkYzmZXb3HDeZcQdGAkCYmzpfl1UF9m50Q-xj1aZRe6W-0fL2E8m8uPSQF0Je6_-_dbpLUL8sZKt3yzPm_yG8AePWYVgxkQ8Zau9r6es5_gD4XAtY0gNksrdK1w3BFDbzqjf919WE_pBB7lqaAE76TxLv5j2AQ7_ie1JLqON720DKOxXP31YoY7ZuWawwVI1Ym_zqWzFJ_EzZbrSHRB8CugQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb76f1aa0b.mp4?token=nM4qQeD6XTxMgtPb61qzU3W-vjdN2RbNDYsgUlOVZvdlzsvzW7b4o3a_w66gTvjxDe4Ep48I2gmRUnUW84tMnF7YQsAFh8S8ckG82VwBDsxBFOlmhzhjRe3ZkzZG4IKkYzmZXb3HDeZcQdGAkCYmzpfl1UF9m50Q-xj1aZRe6W-0fL2E8m8uPSQF0Je6_-_dbpLUL8sZKt3yzPm_yG8AePWYVgxkQ8Zau9r6es5_gD4XAtY0gNksrdK1w3BFDbzqjf919WE_pBB7lqaAE76TxLv5j2AQ7_ie1JLqON720DKOxXP31YoY7ZuWawwVI1Ym_zqWzFJ_EzZbrSHRB8CugQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جایزه یک مداح برای کشتن ترامپ و نتانیاهو
100 کیلو طلا
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67206" target="_blank">📅 21:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67205">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f4NRkbM-D1hZq4buVVnO_0ildSwTeY2TjEHOIWEIG9NdIh-Zuk3VKmnIPoWTHlkU7PcLpenwXrz7yvOzPjFZa3BOz3lL2S8Oxtfm4HyuqkmLzYJBOv4762Z3LXrLAXdCeTvVEZUCyOHCgYjHjZYC762LxvrWAl-dKlUtlQ3iQuRh93XYwcqFmsmyUklaBmiMMLJIzJwxmUCKHzXPpI4735jpaQPijSqjXVOX57cyf8e4-qfTe9Msk2udxMQ8fKK9kJUWDTqbZz7aN4Sgd-yp4NnjR8pWupmWPYPOcTJJynHRfJqu9jl0jBMP6SpcWmdFEUfyw2_EthfoEhEp6mP1mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بر اساس داده‌های مؤسسه کپلر، روز گذشته در مجموع ۳۸ کشتی از تنگه هرمز عبور کرده‌اند. از این تعداد، دست‌کم ۷ کشتی در مسیر بنادر تحت کنترل رژیم جمهوری اسلامی و ۱۶ کشتی در مسیر عمان ثبت شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67205" target="_blank">📅 21:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67204">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RnFBKZQQjjg9wNoLVqzSjpk9HbuMxh6_Fnq1q12SxY5gMiY0QFF-3XYn0wWFkL9uWyQ0UVxtpXPps-f-vWtIhRY2RqluUPi6Zzf_RWSTPpabEYkiuOC70KxQusNhgCUloIhWmpIthuZcj17g3UCZPU1bfLfhmePRGh_r4JrPICIFZnjNNnexyTM-venmkeewkVt2Q4w8Z_MspJTqwDHjZL1evcn2LL6ZgZZHAnHF0ktwICCRm0fxiMcc1M_Mf5ZrKuI4TKfM-bgFC-UKCuGbu2nzzUDUmmCfsv6iE5KAzES2bVN5yQ00WQOueqgzO9ut1Yy8yFbJ8XE-tjciMa7G6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
احمد وحیدی فرمانده کل سپاه پاسداران برای اولین بار بعد از آتش‌بس رویت شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67204" target="_blank">📅 20:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67203">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hfR2uKMpZxaozKql3yKRfTriBtXIsHPqitXBnvPJMArXuYvL8rsTSshHcmETvEVYXOsJ2bdxUvst21Zq2mvaGWBQcuiU4VHPo0bGSr0urljNuoL8uchLMaHO70yN6XphDxyLm6EivmN315H31N0Rx5a8Y_0C_PHIwHASZYzdigWJjJNEJIKuUbHK18cNkWICHzPQzOfx4qQHPJ9VIc4Q-FjZ1h32C7mHsfnw1iHNgpCL23T5f4WebVkxTvj0axj5Y8P9KTsxi8TPz3Vi_NJQ1yH04xoXLqMoYsLCQGpbbL8LDFbmOzTuErpiVJrbpqRBBISN9kFLS5fsuW7qK_BUPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نبویان بعد از گفتگو دوستانه با ممدباقر:
دوقطبی جنگ‌طلب و صلح‌طلب ممنوع.
کسی در کشور مخالف مذاکره برای پایان جنگ نیست.
اما تحقق اهداف دشمن در مذاکره در حالی که نتوانست به آن اهداف در جنگ برسد، قطعا خسارت محض است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67203" target="_blank">📅 20:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67202">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cuw4MF4D9TC2Gj-FtaQ15-u4e9BDUxNhCTHiZp2cV76VWbvdpDdHMRPkiKgex6gJwRgsV7grtL11VgGV1iMW-6Vg076kgqi_HmYwaCXaGeH2i8EUHu4hFETrmj81RH3Ac68dgxx0dPyFRTu2WvdcyhHCnYsfCWuENQtcpwUeB2s047he0O_opIsrl8171jgnzcgkVljbVYLAVk8fQHQbKZnQsleHL2Tgo7L8x3KJbBAR3_hqm83JXRVjLmqLuHDvUnK8ZH6G1toAusrjl3DCNsWqF-hPdVi_vrLK99hs-xBY0JnuHmfaJiuy5xANk4QvhtldXO-jkmeHbrvjwZfWAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
باراک راوید:ویتکاف و کوشنر تلاش کردند این پیام را به طرف ایرانی برسانند که اصرار آن‌ها بر دریافت حق عبور در تنگه هرمز می‌تواند توافق احتمالی میان آمریکا و ایران را به شکست بکشاند؛ توافقی که در نهایت برای ایران بسیار سودآورتر خواهد بود.
یک مقام ارشد آمریکایی گفت: «پیام ما به ایران این بود: "بزرگ فکر کنید."»  به گفته این مقام، درآمدی که ایران می‌تواند از طریق توسعه و فروش آزادانه نفت و سایر منابع — در صورت لغو تمامی تحریم‌ها توسط آمریکا به عنوان بخشی از یک توافق — کسب کند، «برای آن‌ها صدها برابر ارزشمندتر از توسل به روش‌های باج‌گیرانه برای دریافت حق عبور خواهد بود.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67202" target="_blank">📅 19:43 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67201">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/acGXQLlXaf8k1skuWlDXkARWehvhDM_o5VNMeRqo6yk7QfcTboZDIaGeZZK8PSENbNXZMSM243o8hNvarZFHGQ7pKVHXwYklnHHP_zWPq51UkhkfJYt1YIHi57sHPkT6rzHtZ6s_D3E6mAUOHDY36mpHj-Pj9zPHqs_iK1HbLMJ6v4isr-rHEA-4D7SZwFC-Nz_KOuHJKXMfZgFQYnIy2YcUi46jAPvc9yR3w8YeATYmqiOsDX3Dy132PVGnQ9VSoVITkn03vSACsLLyuP1nERy2vg1YK37aISMnGp7ZLDyZz7xNOB7dYs_69bC1WPuffCMSTOnIx63NPIz-tXOLYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لارا لومر، فعال سیاسی آمریکایی خواستار بمباران تشییع جنازه علی خامنه‌ای توسط ارتش اسرائیل شد
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67201" target="_blank">📅 19:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67200">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8af16d4917.mp4?token=nTJVUnphATrAQ3Usfv4GK3GDvdIN_0bRFPlsuenOlvIwgBXX6Pam-ip4XWULE10WNvvDQqMyG6viwtSOyNeZpnskbEs5KR_b2Q7l3ljW8vQ5qu73_X0Fm15s0mDWTZHJRVdwiq--2G8eKLEOktghnpFesiqCjtLfuJDnJ6tHZgy9m_tx6RJBXvo3mwtLgLkCuxSHLUWXrPYSrQIr567Zs0qJHG04ctXSC2ncL4Y1YNLJ38_jrcp9jaJQmkwFWzNhZJviszF5eb_W8Iv2e-P1YER2jd42MJ2DbRtgcuXlDWWbY3XOBw-5oCy1SbXsRiQuZQA9UOSuz0wGLNG8CA3aVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8af16d4917.mp4?token=nTJVUnphATrAQ3Usfv4GK3GDvdIN_0bRFPlsuenOlvIwgBXX6Pam-ip4XWULE10WNvvDQqMyG6viwtSOyNeZpnskbEs5KR_b2Q7l3ljW8vQ5qu73_X0Fm15s0mDWTZHJRVdwiq--2G8eKLEOktghnpFesiqCjtLfuJDnJ6tHZgy9m_tx6RJBXvo3mwtLgLkCuxSHLUWXrPYSrQIr567Zs0qJHG04ctXSC2ncL4Y1YNLJ38_jrcp9jaJQmkwFWzNhZJviszF5eb_W8Iv2e-P1YER2jd42MJ2DbRtgcuXlDWWbY3XOBw-5oCy1SbXsRiQuZQA9UOSuz0wGLNG8CA3aVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس شبکه افق، به قالیباف:
این مسیر به جایی نمی‌رسه، حالا دیگه خود دانید.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67200" target="_blank">📅 18:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67198">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67ae57b0be.mp4?token=XhZtzHc0jZbEl5D8bGkM5Yxpdmcfr3Nu3qtLb9LhrSAmVUnyOXYjPwdkuRvI7Mgiem68XZUzj5qvDdMerLbLzRAMGSerA-ppFosY2UoYPzynKQIKFd886Qblzv_SkVKw2_GEEZasFEOVu6qFaGWuT2e_SKUOqhnHJPs3zVtA-ZREDMBq5JFqgD-u1JYMu9CvQcuOktEzR0gPNmQDLJYnkxckj_CdThiYkwl7KidUnbDYmKlMyJwr9a9C06ti3wQwzpoN_8qQU1xC8hL6OspY8I1GFEFh3LpbrlZrb_r0ddJPiGa_euiWpT5wHgXkwewGEeoto641Al7i-FtXjZeHBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67ae57b0be.mp4?token=XhZtzHc0jZbEl5D8bGkM5Yxpdmcfr3Nu3qtLb9LhrSAmVUnyOXYjPwdkuRvI7Mgiem68XZUzj5qvDdMerLbLzRAMGSerA-ppFosY2UoYPzynKQIKFd886Qblzv_SkVKw2_GEEZasFEOVu6qFaGWuT2e_SKUOqhnHJPs3zVtA-ZREDMBq5JFqgD-u1JYMu9CvQcuOktEzR0gPNmQDLJYnkxckj_CdThiYkwl7KidUnbDYmKlMyJwr9a9C06ti3wQwzpoN_8qQU1xC8hL6OspY8I1GFEFh3LpbrlZrb_r0ddJPiGa_euiWpT5wHgXkwewGEeoto641Al7i-FtXjZeHBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یک پهپاد روسی اوایل امروز به یک سالن شنا در زاپوریژژیا در جنوب شرقی اوکراین حمله کرد
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67198" target="_blank">📅 18:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67197">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحاشیه نیوز</strong></div>
<div class="tg-poll">
<h4>📊 با توجه به مذاکرات دولت پزشکیان، قالیباف و عراقچی با کسانی که آنها را قاتلان رهبر و متجاوزان به میهن می‌دانید، آیا به نظر شما این آقایان حق شرکت در مراسم تشییع پیکر مطهر رهبر شهید را دارند؟</h4>
<ul>
<li>✓ بله، باید شرکت کنند</li>
<li>✓ خیر، نباید شرکت کنند</li>
<li>✓ نظری ندارم</li>
</ul>
</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/67197" target="_blank">📅 18:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67196">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9db45e91a.mp4?token=vn9q4d6cnMRtEIO70_CDvWvyi5cKBKEswrwxyZQsxoaDxh_xROg6rL9d__HKJsgu8CaiXBnqOV2QLRC4qFFrILkwHONPg2j1t0b_5EX-qx1zHzDlIW4UNQKDNvxFUF4UNtthATglERI8YUKUTOegJ_FYvHn2G_gaC_nt90F19gfayCry3pSz9AIaYi5rz4D-xeTbnFM9qx51-Yc9WZd5MQJ3lxWVFUrLGJ_AajMGrLKag9xDPPjf0xUoHh-izm8yoPAd0Bwhm3zWDtlH9SSHalKs7hiUDfKZbL8ESwYr_jocGgw00b_spbmcZiMj0JGbmvJniOd2AYx0GkzKAGS-SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9db45e91a.mp4?token=vn9q4d6cnMRtEIO70_CDvWvyi5cKBKEswrwxyZQsxoaDxh_xROg6rL9d__HKJsgu8CaiXBnqOV2QLRC4qFFrILkwHONPg2j1t0b_5EX-qx1zHzDlIW4UNQKDNvxFUF4UNtthATglERI8YUKUTOegJ_FYvHn2G_gaC_nt90F19gfayCry3pSz9AIaYi5rz4D-xeTbnFM9qx51-Yc9WZd5MQJ3lxWVFUrLGJ_AajMGrLKag9xDPPjf0xUoHh-izm8yoPAd0Bwhm3zWDtlH9SSHalKs7hiUDfKZbL8ESwYr_jocGgw00b_spbmcZiMj0JGbmvJniOd2AYx0GkzKAGS-SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در جریان تجمعات شبانه صیغه یابی راه انداختن و یه نفر یه دخترو به مدت یک ماه صیغه کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67196" target="_blank">📅 17:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67192">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ik_r3m7u3idPBIjTMz-LkMbQUL1IdvlrowNyvG8y8Lks2vtpW-J_Pp5vDT7MozWO8vg6jamFB0qgx1lB2EBCBJYoU0mzoCMX7NXlpl6mVTcIuiDsKM47alu5FUMljkvo7nzqzcWhIGLl3wJRahzJeNVAJ1vZHYBLLSqD5AXtmOcLRlvVslAEbqQwSBV5EaMQpshnWP4_UjyjTo4xjgrxQdslStEMRMZiUjsUuk5iD1PgN8KqqNvrcbJKfMFG-i1yDN6bEvZJJ5VZig3FqF1f9UKMyAUaN6-ad2yesISICZza0NNfVNw1MVetKNPyLb3UvhSH6EYkBFJYLz8g041huw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bxEzaZ1wRPD99C2hxaIR2cb-dczFSI9LL_CT_U0VRntbgDAJdLgX0KHoXBq6ZiQFYK1eqsZjJv9fQLa7XaQAdy_YrsOMkdC6AtFTtDZEFOrveSg5vCiOAQ5QNk0OAXJ9_ppMbG9XeUpKIIjG4WdkW6vtHm9cqk03TXHvoEx7U6oNazPQ0_UAoSwrGCrQoZv8PuW1H3OEk24FxMkRq7LHPEmuW29AgUQCNOAoj7uvO3LKmVeKfbZiKS9UC3NpuRV0w75fF9WCApcClAFKeRug6FxVc6jW3eefLiF8eF-AzKQeYHW4cngcb5mj2EaLEYmo_q-ACzPEAJqrF0CEJZarfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PVB1ehgGqVcgPknX1vu7slvTgRY9gwZiEE5OVJaNGuqOEbbtplgx_atKd8u9R7oIkSxvoRsEEH1wboTKvVTpzxFyHkizn5tvJ6XoyVBGwgfhTaSlGihwp9gaWKQMDQsc2ZSRDy2eBoNCgEDIk95G9wD6SZGuP_U54gEioMA6f8yKLwDNyGNQvcVOcoNxbYK1znM7I1OfFgrMoMhYha5DJJZK5ggVt2-PqsnTVl9WVLY5c2GKiIYcIEm9o5qITQQYRRpG1H-USD2UpdGoZatBp9OuM3UFLUy-J85ISGXy-Y9Cpi0VvINyHdYtp2YhtfzvUl-vdL6QxmqdohBuTHxgzA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/543c505f1c.mp4?token=kSgxfdHx86TFo5kAIwJJ1ZYtsyMEvZYAB9C8efu0axbzG2HMCr2Ixlb1mZiXV_5Nvpv_hXM-ZB31mu8K1iPlvpKSt3tNb8OkUm-wAaZLc3NoVi4FtjFIaXltd-rISPnU6AcwR8usy_mrXBgf05oxSHFbihxpPLILXI0nzH1xHOXA2z1ogSvSy-Suk9QcmFaG1dUwjDnLqJcVMTBIQcwd6zWEvWvTxKtOG1_BNsug022wZ696cWMH830W1iVKfCIkG1Hfy74mZz2kyLh_HLlKaj6dywZaFc9XLeoyFLVHS5GZ1kj3B-WDZYFH-lFq3QyV2mNMGxdqATzgd0uJ8vGQ2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/543c505f1c.mp4?token=kSgxfdHx86TFo5kAIwJJ1ZYtsyMEvZYAB9C8efu0axbzG2HMCr2Ixlb1mZiXV_5Nvpv_hXM-ZB31mu8K1iPlvpKSt3tNb8OkUm-wAaZLc3NoVi4FtjFIaXltd-rISPnU6AcwR8usy_mrXBgf05oxSHFbihxpPLILXI0nzH1xHOXA2z1ogSvSy-Suk9QcmFaG1dUwjDnLqJcVMTBIQcwd6zWEvWvTxKtOG1_BNsug022wZ696cWMH830W1iVKfCIkG1Hfy74mZz2kyLh_HLlKaj6dywZaFc9XLeoyFLVHS5GZ1kj3B-WDZYFH-lFq3QyV2mNMGxdqATzgd0uJ8vGQ2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیروز این دوتا زوج تو نیویورک رفته بودن بالای یک برج ۴۴۰ متری، که یهو پسره ازش خواستگاری کرد
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67192" target="_blank">📅 17:04 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67191">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afce812fcb.mp4?token=GQERSAfNhvczK6ul0R-NPO0mRVoZZbxA8Q5_ya7PauVfA9zJ-v5Ft5bLG5UBMpbBgyNgRRtru1iKbDg_ZJ-kJ0umZKQxoD2ZCEIbBtO8SpOgwUlBan9uAS9ZkWZ_1FNYCUz7wJeUOkZTvlAFiryu9cqvn8fNn8MOkMinuAMakkxt03Z_OwC8N6bZCnF3TPKDQ4uGATCQtlfaKebtgwXbRZ0H-Ek_qNwwCZGe826gI7hrtZ4ewXBS7-5fzRLeV9tTW_aFEep81k_7d71_yBQNxcVNZ_ihFSo-m-1cP41IHbh7YIMxY1nlyYKDxsP6Vc-FvODFtpDGDewjKdCIovrI8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afce812fcb.mp4?token=GQERSAfNhvczK6ul0R-NPO0mRVoZZbxA8Q5_ya7PauVfA9zJ-v5Ft5bLG5UBMpbBgyNgRRtru1iKbDg_ZJ-kJ0umZKQxoD2ZCEIbBtO8SpOgwUlBan9uAS9ZkWZ_1FNYCUz7wJeUOkZTvlAFiryu9cqvn8fNn8MOkMinuAMakkxt03Z_OwC8N6bZCnF3TPKDQ4uGATCQtlfaKebtgwXbRZ0H-Ek_qNwwCZGe826gI7hrtZ4ewXBS7-5fzRLeV9tTW_aFEep81k_7d71_yBQNxcVNZ_ihFSo-m-1cP41IHbh7YIMxY1nlyYKDxsP6Vc-FvODFtpDGDewjKdCIovrI8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پست جدید ترامپ:
ترامپ پزشک می‌شود و بیماران مبتلا به «سندرم اختلال ترامپ» را درمان می‌کند
🚬
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67191" target="_blank">📅 16:36 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67190">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cadc1a3fe.mp4?token=o2mETUmh-hTihRPDYp3GfGpe7639ADg2jJz3vI896m5MfeO2IlL2S75jYT3XYA3W8CN7Y_pXYo92siU6lPxmsQANM4VHWeU7LYkKsocV7_8o9AmeQsE5lwyLUoXzm1vZj3WsPDOszR6pUtno_XlqSdQAwCBXpypSy4DyFZIgjsmfIIWMhJWKZ-4qXfjerMXj9SfN4yM3au7WFUCmZ6_I_w_WndU72e3pr5pT_VLcDD-uJiL-nkvgaYpizd6MrX5hEPUlSwbewwkhvKX-uQzFQr920YJwEKdKI-jUbT3ysh19EVLan_n4h35FzH8ZMw6mibn2No6Hy9GUOihmrZWDug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cadc1a3fe.mp4?token=o2mETUmh-hTihRPDYp3GfGpe7639ADg2jJz3vI896m5MfeO2IlL2S75jYT3XYA3W8CN7Y_pXYo92siU6lPxmsQANM4VHWeU7LYkKsocV7_8o9AmeQsE5lwyLUoXzm1vZj3WsPDOszR6pUtno_XlqSdQAwCBXpypSy4DyFZIgjsmfIIWMhJWKZ-4qXfjerMXj9SfN4yM3au7WFUCmZ6_I_w_WndU72e3pr5pT_VLcDD-uJiL-nkvgaYpizd6MrX5hEPUlSwbewwkhvKX-uQzFQr920YJwEKdKI-jUbT3ysh19EVLan_n4h35FzH8ZMw6mibn2No6Hy9GUOihmrZWDug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این چیه دیگه
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67190" target="_blank">📅 16:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67189">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcf57c8dbd.mp4?token=BFrzG8DHUXgRVmqNNW9vIJPNriPKQYbgbC_Dt-qZkUDqlbdiyWBCajc4MaSGXrOfm-NXfZv9WFBTE8UskDN_CKwkyAyaqm050RjEP3F4Qlih7R7l3AeaXUDh-XBr8sBn_bUwwSSj24rs0rHUmZTbrCnaigCs4qM74mkSdocPPqmBG9YpgqgetMt4CG-zeS0cD1UwpNkvOsCWiZ9Ef8U8al5HatCwqbeAhXclSoIxi1jV8nz0gXgr3vIlHCd3tHEYkDxsOtR1Nw8PGV-fE9MAg6T2x5n8akLOmUue3hUC14kBvuw_zz5buT7PTrayY89qt7pt0PrmRdFvn228fGl2lx9UMegIPHOZ_dniwXFdEEifezdeEK5l8NQF8BSoLzhfr5s1VIJnpV2RIX6SlALAfZ6ud2zZ_xsFchKtWUPooNaibJy6j7tFUIE59iLacRa05p1ch65EsqAFhWuOBjy0x5GoU6FH7lFTo81PQ3r2KQuXwyXVGjZU0afPJbHPCmjEDVsLKOarDaeryGUq6GpBgIXUVCCsMVUbaP8bcumYl3kAq4fvF5d2uAOOKXSqKqep6fWPpl5iG1N8zeBQrDQ_ZEQ63UZRsYcPzKNLO1CMGVWquQTXZhqm1snMwIJ8X1mcHAYXUgzOWZbH0mXwv3LtqlHYyjQQG1qmc6LC68Zayuk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcf57c8dbd.mp4?token=BFrzG8DHUXgRVmqNNW9vIJPNriPKQYbgbC_Dt-qZkUDqlbdiyWBCajc4MaSGXrOfm-NXfZv9WFBTE8UskDN_CKwkyAyaqm050RjEP3F4Qlih7R7l3AeaXUDh-XBr8sBn_bUwwSSj24rs0rHUmZTbrCnaigCs4qM74mkSdocPPqmBG9YpgqgetMt4CG-zeS0cD1UwpNkvOsCWiZ9Ef8U8al5HatCwqbeAhXclSoIxi1jV8nz0gXgr3vIlHCd3tHEYkDxsOtR1Nw8PGV-fE9MAg6T2x5n8akLOmUue3hUC14kBvuw_zz5buT7PTrayY89qt7pt0PrmRdFvn228fGl2lx9UMegIPHOZ_dniwXFdEEifezdeEK5l8NQF8BSoLzhfr5s1VIJnpV2RIX6SlALAfZ6ud2zZ_xsFchKtWUPooNaibJy6j7tFUIE59iLacRa05p1ch65EsqAFhWuOBjy0x5GoU6FH7lFTo81PQ3r2KQuXwyXVGjZU0afPJbHPCmjEDVsLKOarDaeryGUq6GpBgIXUVCCsMVUbaP8bcumYl3kAq4fvF5d2uAOOKXSqKqep6fWPpl5iG1N8zeBQrDQ_ZEQ63UZRsYcPzKNLO1CMGVWquQTXZhqm1snMwIJ8X1mcHAYXUgzOWZbH0mXwv3LtqlHYyjQQG1qmc6LC68Zayuk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
صحبت های جنجالی
غضنفری، نماینده مجلس جمهوری اسلامی:
عده‌ای میخوان تجمعات شبانه رو جمع کنن. دارن علیه مجتبی خامنه‌ای کودتا میکنن. دارن هزینه‌های سنگینی میکنن و به مداحان و سخنران ها پول دادن تا دیگه تو تجمعات شبانه نیان.
به بسیج نامه زدن که دیگه تو تجمعات شرکت نکنید. مجلس رو هم ۴ ماهه تعطیل کردن که نتونن اعتراض کنن.
قالیباف و پزشکیان میخوان کم کم مجتبی خامنه‌ای رو کنار بزارن و خودشون اداره کشور رو به دست بگیرن.
رهبر از مسئولین قطع امید کرده و الان فقط امیدش به مردمه.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67189" target="_blank">📅 15:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67188">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1148d0ce1d.mp4?token=aloMNGHqrHAGf2Gc9u7mKcCPi6u0XmSjfHvLKtJIWHkPb_nEgrCvx3KL6p3j9tiaPAjUAwmu7Qq22CIH8gXiq1ecJhMALvcg05U5CQAcr0NCpKS_YnPW1YK52OuTRTu4DhYhaVuIXl6IjU1NypvXJY6cZNS66kI35D2cyjyyrQE7waeSaxIjpYe_7AWJQJkshpjuD_MJkX9blbMazdqijTxiyMe2XJMWQtAQnNca7IBpp2xiEcaokoX92UEQUSz9l1TFwKQiGixyBY883Wx6B6CqXWSQ_GBCoN7NMeKTAOW4rY3TyiH0ZpoCd_HiHtjFvLDmHaGdWrNkhgem4OMj6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1148d0ce1d.mp4?token=aloMNGHqrHAGf2Gc9u7mKcCPi6u0XmSjfHvLKtJIWHkPb_nEgrCvx3KL6p3j9tiaPAjUAwmu7Qq22CIH8gXiq1ecJhMALvcg05U5CQAcr0NCpKS_YnPW1YK52OuTRTu4DhYhaVuIXl6IjU1NypvXJY6cZNS66kI35D2cyjyyrQE7waeSaxIjpYe_7AWJQJkshpjuD_MJkX9blbMazdqijTxiyMe2XJMWQtAQnNca7IBpp2xiEcaokoX92UEQUSz9l1TFwKQiGixyBY883Wx6B6CqXWSQ_GBCoN7NMeKTAOW4rY3TyiH0ZpoCd_HiHtjFvLDmHaGdWrNkhgem4OMj6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درتجمعات شبانه عرزشی‌ها:
مردها: گندم و جو ارزونیتون
زن‌ها: تنگه، نمیدیم بهتون
😂
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67188" target="_blank">📅 15:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67187">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57a2c0f9a4.mp4?token=DOkuS1BHZ2WU0iWui_BJ3SDtRMEvVEenNir3U_kuTzF7xVgA4phBYNd2ZDPdxWT9GPtzLBPVlRqbbi_AaRxHVjUOBe30NSqQU2nkv3l3O-kUVU5zPf0ncCL8yMKwC7Js-fnfT6YZxwLZuuzLI6AtS5KjryEkZhA4xI5erxbHTB3_jYedzMPEYMHdMoFHLvyNTqyaKRnWFaP0etUWqBD3db290qZfCRu43MzwfukY20OIuswOcoxzBR8oBeiCpzDlJjxfrkqoU3xVgfqHmov1hFVwyvgeB60e_I459iFa0Tu1sN7b_mK1ueIT0Qg9M9buL-6bfJOhU_6flhilwYmODw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57a2c0f9a4.mp4?token=DOkuS1BHZ2WU0iWui_BJ3SDtRMEvVEenNir3U_kuTzF7xVgA4phBYNd2ZDPdxWT9GPtzLBPVlRqbbi_AaRxHVjUOBe30NSqQU2nkv3l3O-kUVU5zPf0ncCL8yMKwC7Js-fnfT6YZxwLZuuzLI6AtS5KjryEkZhA4xI5erxbHTB3_jYedzMPEYMHdMoFHLvyNTqyaKRnWFaP0etUWqBD3db290qZfCRu43MzwfukY20OIuswOcoxzBR8oBeiCpzDlJjxfrkqoU3xVgfqHmov1hFVwyvgeB60e_I459iFa0Tu1sN7b_mK1ueIT0Qg9M9buL-6bfJOhU_6flhilwYmODw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
رسانه‌های اسرائیل: تصاویر ماهواره‌ای تازه از سایت هسته‌ای اصفهان؛
تصاویر ماهواره‌ای با وضوح بالا شرکت وانتور نشان می‌دهد ورودی‌های اصلی تونل‌ها در سایت هسته‌ای اصفهان، جایی که بر اساس برآوردها بخشی از اورانیوم غنی‌شده رژیم جمهوری اسلامی نگهداری می‌شود، همچنان با خاک پوشانده شده است. این وضعیت نزدیک به یک سال پس از آسیب دیدن این مجموعه در حملات هوایی اسرائیل در عملیات «با شیر» و عملیات آمریکایی «چکش نیمه‌شب» در ژوئن ۲۰۲۵ ادامه دارد. بر اساس این گزارش، جمهوری اسلامی در آغاز سال ۲۰۲۶ به طور عمدی دهانه تونل‌ها را با خاک پر کرده تا آن‌ها را در برابر حملات احتمالی بعدی محافظت کند و ذخایر اورانیوم غنی‌شده را در بخش‌های زیرزمینی پنهان نگه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67187" target="_blank">📅 14:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67186">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMoris News</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PYRZkIzrQZ6EGMilPim9LRhrSabI8BgJiJ5YWLssULSgiCYBPd2hUz-wQ2GJY12ZHqYflTX_NmBGu2n33DJOzMGso5OtPlEj3vI4Tu8JvV7vAt8BFX2Bv6ypDl_12zLfxeFQ8LosxAmBuEwH334AqNTC5gRa7mQw6JuFdUNeulz1UCFhZg7h4wdS3n75nlpK-b6ZD4VFyIcEeFM2cXeldEwwlBhqIl_Hkblze1TqA3wU5r27gilFLy_UlAQkb9ErtscOz-N_yX-KGnF4lt1lALqjlM8snk_Lf71lYt3u2aARWdDmFIEEd0aK7VC3AbmFwSRTmEvwEp8VBT1A-1SGiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه جدید یک دوست عزیز و هنرمند که احتیاج به حمایت داره
از دوستان خواهش میکنیم با فالو کردن و شر از این دوستمون حمایت کنید.
@egyptinpersian
در اینستگرام</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/67186" target="_blank">📅 14:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67185">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ohDCr-5dYuZRQFT0J4Fmx2duLw9cTqpJRBhe2P9_g3KPM5U15xFCLC4KDpNrP2BXy8t-6C6oTr6PGk6kvgExI3kKkRkv6mfKyhTnF7xg3ObyEQedqwMezmpauYYqaSi2AwznfL6DDn2KT9TS9RgVIagjKBRoKe6a-MkLipHLT2RYjdAVO0pb4igcUmsTWbf69Qz9XB0ZDexOcUELvn9yBh7BD35h1Qx1z2ha7H2b6seupRjB2A8zryt0uungAD881Yfdm37CS8EfT9BjZ6O4Dt6k5bzljMl3NF0n6e5FBXa2iSbdwkhh71gX3fRDdfwSqaPBcsmJQEbUFEM0zoVIHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
العربیه:
دور بعدی مذاکرات ایران و آمریکا ۱۸ ژوئیه برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67185" target="_blank">📅 14:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67184">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/885b0b0686.mp4?token=PfqzlA1K1MlbgTCUsa2mA5Uv2kzE6HVTQed5uNkXWR1uH3H1oa5YcGn7W5Mk5kcSZSeTUzoVPve-nl70pZ0f2_BkYAVKdemv4ZOeQz-d5SBP-UrEfg_XOehicr6Lsl3XqNbRgkycniQq3Bc2YZsR8qHQjAxPpeMiLVHToZv0r8ScRQWGB6uSuSD3BysxCZ9Qfw6dwbCavE8G35HRUOU6zqDUlyshakAb1igvPXH7IR6JIZgIpiP4mmf_2bsBL4mjEdm4Gmh7-DWXbMObHNPAxIcoH8d1j-LDqE2RhNnGU9o_FhHQYkmHDU92rxF_l8O4lOUVDTe8F1mHKgwudDlTGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/885b0b0686.mp4?token=PfqzlA1K1MlbgTCUsa2mA5Uv2kzE6HVTQed5uNkXWR1uH3H1oa5YcGn7W5Mk5kcSZSeTUzoVPve-nl70pZ0f2_BkYAVKdemv4ZOeQz-d5SBP-UrEfg_XOehicr6Lsl3XqNbRgkycniQq3Bc2YZsR8qHQjAxPpeMiLVHToZv0r8ScRQWGB6uSuSD3BysxCZ9Qfw6dwbCavE8G35HRUOU6zqDUlyshakAb1igvPXH7IR6JIZgIpiP4mmf_2bsBL4mjEdm4Gmh7-DWXbMObHNPAxIcoH8d1j-LDqE2RhNnGU9o_FhHQYkmHDU92rxF_l8O4lOUVDTe8F1mHKgwudDlTGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پرواز جنگنده های رادار گریز F-35 برفراز ورزشگاه Bay Area سانفرانسیسکو در بازی بوسنی و آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67184" target="_blank">📅 13:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67183">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dd137decc.mp4?token=S8oQ5G8WPuObTj2xVOAsv8bMGNoo75pdzFuCBkUlXaT3ZBxGL5n0JI626fPr3iXQvbMzEvUNgpSzoPeWvYjIztdlWwDSsO_FVyrgNCNLXw3tjO4l-6OpEQiJoz6S_EHOAYNhnnsIUGKD1bw3uRuwsP_cgW_N0b1panCtxNPsmRZCRedeUaawVUCfOPXP3cueJqm6ldApU5PrX1avpFaLaNRyo_-pBHN-lJXjhL6mOJDKG9TZaoLFEY0TwgxHl1xy5sFZ89xLeit26-elOJQk-kUHC9CdhtnSLgETUJTHam8cymXvIBl2cVczLvU7ryn3Wd03FGaGRvAHabq2cuGQHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dd137decc.mp4?token=S8oQ5G8WPuObTj2xVOAsv8bMGNoo75pdzFuCBkUlXaT3ZBxGL5n0JI626fPr3iXQvbMzEvUNgpSzoPeWvYjIztdlWwDSsO_FVyrgNCNLXw3tjO4l-6OpEQiJoz6S_EHOAYNhnnsIUGKD1bw3uRuwsP_cgW_N0b1panCtxNPsmRZCRedeUaawVUCfOPXP3cueJqm6ldApU5PrX1avpFaLaNRyo_-pBHN-lJXjhL6mOJDKG9TZaoLFEY0TwgxHl1xy5sFZ89xLeit26-elOJQk-kUHC9CdhtnSLgETUJTHam8cymXvIBl2cVczLvU7ryn3Wd03FGaGRvAHabq2cuGQHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو:
ما دو بار به ایران وارد شدیم تا خودمان را از نابودی نجات دهیم. در صورت لزوم بار سوم هم این کار را خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67183" target="_blank">📅 13:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67182">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b216695e17.mp4?token=YC_gkK06RchSgxv8C-6A4WygjOFPSl8zqB0H-qkM3JwsOhsdCoiYnHTy_WciBT0nplO0DwTDH3XugfLDfdu9WGnc5Gkt50rhbv70uUiJGBMPuK_isEg-96yr8fhmzsL_WkUalMpk5STaazVbvyVqrGdodJtt9-eQJhZTDxMLFXJtSJXiH0cU3M-UtjkXsiU18mIgTC2esx-IxfZDIlzcHxC6cA5anYIkGCYDYwmLi4uesZI-ptW-lZEXfSW876aEePT0QPYA1IQ9wcGXBn75fZwE_kNeQusZhec0ugPzPjiKxULZ6mWq_LesLpeaddiqQKcKk1JsfC93QaZslHuOng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b216695e17.mp4?token=YC_gkK06RchSgxv8C-6A4WygjOFPSl8zqB0H-qkM3JwsOhsdCoiYnHTy_WciBT0nplO0DwTDH3XugfLDfdu9WGnc5Gkt50rhbv70uUiJGBMPuK_isEg-96yr8fhmzsL_WkUalMpk5STaazVbvyVqrGdodJtt9-eQJhZTDxMLFXJtSJXiH0cU3M-UtjkXsiU18mIgTC2esx-IxfZDIlzcHxC6cA5anYIkGCYDYwmLi4uesZI-ptW-lZEXfSW876aEePT0QPYA1IQ9wcGXBn75fZwE_kNeQusZhec0ugPzPjiKxULZ6mWq_LesLpeaddiqQKcKk1JsfC93QaZslHuOng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
ناموسا این چیه ؟
جدیدا تو تهران یه روش درمان افسردگی به نام "هیپنو‌تراپی" مُد شده که مراجعه‌ کننده رو می‌چسبونن به درخت و میگن گریه کن !
درختی هم چند میلیون می‌گیرن...
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67182" target="_blank">📅 12:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67181">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
🚨
قرارگاه مرکزی خاتم الانبیا:
استمرار حضور جنگنده‌های آمریکا، با سرنشین و بدون سرنشین بر فراز تنگه هرمز، باعث ناامنی این آبراه می‌شود و امنیت منطقه را به خطر خواهد انداخت.
جمهوری اسلامی در صیانت از حق حاکمیت خود در تنگه هرمز، از هیچ اقدامی برای درهم‌کوبیدن هرگونه تعدی و تجاوز توسط ارتش آمریکا و حامیان آن دریغ نخواهد کرد
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67181" target="_blank">📅 12:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67180">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a5u42HXsqc-9ECbV0FM1L5t1iH1pAws43SxdZ-CahXIEanEX9tMicmUTe_JawGnehhA7jdCCkaq5h-V1Nt8QU060m7YlhUus-OtncszkfKCOc_en80QupHxr8ImEmSnabPFwFM2ds5eDHvJjT7th4w7gasTCctValFUJ9MELDzhmq7DXs99Yfwp5B1VRdbQ8Cvc7qGDG0Iido1xb_MdyZQBGAGTamhubD6BdfCFou4YpbPJ5ZY5MNUQyHKMIVJvoMWgwauWtXn1oRwq_XUZvAdrDKP4CpZQyJTx0Mkqcu5bYxmISpvXpSHXubSZ-g4pOgPSdHYiOO9FSy4eGb02IHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
‼️
وزارت خارجه پاکستان: مذاکرات غیرمستقیم ایران و آمریکا در دوحه پایان یافت.
ایران و آمریکا در جریان مذاکرات غیرمستقیم دوحه، ضمن دستیابی به پیشرفت‌هایی در موضوعات مرتبط با تفاهم‌نامه اسلام‌آباد، بر سر ادامه گفت‌وگوها توافق کردند.
زمان برگزاری نشست بعدی در اولین فرصت ممکن پس از برگزاری مراسم تشییع رهبر شهید ایران تعیین خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67180" target="_blank">📅 12:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67179">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d167641bf.mp4?token=akXP40dBbIOaRc48ZAZ7lU7C1z2GhXBKEsom74Ym-Z7EGcn-TXYbK_VUKDgjl54TEIw23blzmGediPvGV2uS52w_sxAN3HdAC_PW6R1XV9URP9_0b37d3lNzt5g4WjGaBLaXyubL24aAdnpexZArsfQUBchzVDNUq9PYk3o4BJCKjKxuPtzfVTZ06ezWC3axZPY_AA3m_IqSzKwUvhYd_yUgwVdlfsQKFeTUWm2iRVJcYxNU8Qe9-4prTBK7SybiZ7Ioqz5_Umq4UVsTWY1e5mCm8yQZUPtcCGnfnO_JcDXcCKid6dGwY53rE2S-3voUTBBLSrL_WRG60r8KKl4pgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d167641bf.mp4?token=akXP40dBbIOaRc48ZAZ7lU7C1z2GhXBKEsom74Ym-Z7EGcn-TXYbK_VUKDgjl54TEIw23blzmGediPvGV2uS52w_sxAN3HdAC_PW6R1XV9URP9_0b37d3lNzt5g4WjGaBLaXyubL24aAdnpexZArsfQUBchzVDNUq9PYk3o4BJCKjKxuPtzfVTZ06ezWC3axZPY_AA3m_IqSzKwUvhYd_yUgwVdlfsQKFeTUWm2iRVJcYxNU8Qe9-4prTBK7SybiZ7Ioqz5_Umq4UVsTWY1e5mCm8yQZUPtcCGnfnO_JcDXcCKid6dGwY53rE2S-3voUTBBLSrL_WRG60r8KKl4pgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
جی‌دی‌ونس،خطاب به هوانوردان نیروی دریایی:
«رئیس‌جمهور ایالات متحده از شما خواست اطمینان حاصل کنید که توان نظامی متعارف ایران را نابود کرده‌ایم، و امروز که اینجا نشسته‌ایم، نیروی دریایی آنها در کف اقیانوس است و هیچ توانایی برای نمایش قدرت ندارند...»
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67179" target="_blank">📅 11:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67178">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc4627802a.mp4?token=BhfrLWOglQaICc5jvEQKK-MtkpHjUelR3Y4gdBPycTScflJMwgckCdQ1HDRl3FT0p3O6-ZbKF9K9JUBTv2EllKTYudWWsWsXQC6cAs0GqBsM5SoDCIa0qxxthTtdRVAFknm6hP8lp5bqhz70yIVA9Vo-53Px3P8IoXKlpzm0sn3snTZnHCwY96VVvXE6CNGTNPzhBMe1cFQMxYkQ8yFShtrmsqXTk9roth-nwiIRDEmmDjBUc7Eb9qtT5R7SzNFIhkZF6CNB0ssNIH1vgJV2q-AnIIqidvhhCuIrmu7Ddbu1oM1W6h0XcqTkhaktFkTIp63YYvjkoYWjI9P1W59W4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc4627802a.mp4?token=BhfrLWOglQaICc5jvEQKK-MtkpHjUelR3Y4gdBPycTScflJMwgckCdQ1HDRl3FT0p3O6-ZbKF9K9JUBTv2EllKTYudWWsWsXQC6cAs0GqBsM5SoDCIa0qxxthTtdRVAFknm6hP8lp5bqhz70yIVA9Vo-53Px3P8IoXKlpzm0sn3snTZnHCwY96VVvXE6CNGTNPzhBMe1cFQMxYkQ8yFShtrmsqXTk9roth-nwiIRDEmmDjBUc7Eb9qtT5R7SzNFIhkZF6CNB0ssNIH1vgJV2q-AnIIqidvhhCuIrmu7Ddbu1oM1W6h0XcqTkhaktFkTIp63YYvjkoYWjI9P1W59W4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اشک‌های مهدی تاج پس از کسب قهرمانی در جام جهانی فوتبال 2026
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67178" target="_blank">📅 11:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67177">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7280fbe763.mp4?token=LlJL3cijKxWoqc3GviJiMevfxTUSlDTlsYNxGXmLwzwaySyNjvAgsfmnykiP6DWjg3-mx9BdlyQaqYqypNjYg1nJYQKcxRMy8L3FtE8RYcBpp-6-CyyHpz91SC4nBy0oT_wro9nwuZyG8p-A2Et_53zGifyulL-F4TlGOpMcp1uWkl01xS0Kfv7Ig_zIwn-nMSEj8ZdbYXaDK7tO5XKqAG0l0Musc_eLrDYn3uWESFanF5RZG_vmR9ImDMnLunp5VoMSg_SvP9qN3Zl-ZDLASE0oq7GP8uu5iaDZwiC-5_aCMG4z7sYPuiJX9KP8EvCPvSBkqF1a_aQywRnGW3ElZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7280fbe763.mp4?token=LlJL3cijKxWoqc3GviJiMevfxTUSlDTlsYNxGXmLwzwaySyNjvAgsfmnykiP6DWjg3-mx9BdlyQaqYqypNjYg1nJYQKcxRMy8L3FtE8RYcBpp-6-CyyHpz91SC4nBy0oT_wro9nwuZyG8p-A2Et_53zGifyulL-F4TlGOpMcp1uWkl01xS0Kfv7Ig_zIwn-nMSEj8ZdbYXaDK7tO5XKqAG0l0Musc_eLrDYn3uWESFanF5RZG_vmR9ImDMnLunp5VoMSg_SvP9qN3Zl-ZDLASE0oq7GP8uu5iaDZwiC-5_aCMG4z7sYPuiJX9KP8EvCPvSBkqF1a_aQywRnGW3ElZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‏فرهنگستان زبان و ادبیات فارسی از سال 1369 تأسیس شد
از اون سال کلا 158 کلمه رو تغییر دادن و تو 8 سال اخیر، 2 هزار و 100 میلیارد بودجه گرفته
با ی حساب سرانگشتی کنی، می‌بینی برای تغییر هر کلمه، حدادعادل، 64 میلیارد پول گرفت!
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67177" target="_blank">📅 10:25 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67176">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/514f1dff1b.mp4?token=POyQQ5epwG-D1tuaeDOIdsdw3zKCfJnVM04Vt0W88L62lX0L6RSLOnAGeNAbX8ulkjMCLXmtkPZjHslMLLWy3naFnfzdnwWmLSjXW5IVyYzI_AcDnoAEdn1DDDt-UTJ7unXETni35o1idp2kXOYiVxdURzaO5o0G1wkzluH3CbpfSP7HS5CDEAx5i3oNeVT5G_ICzDULgKBhHsrgCnjdo7JF8TTn6esSIYmv5fDCuhrPVpVphpTuiji4193_rtLSPvJtiWmU9ZvhNAu39azEK3ahq2glsnLsyU0Tp1aQKCyGVhy2QcrmjkjJr1LjP0hNUL1b4n4cNTmj5-qNlRyrHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/514f1dff1b.mp4?token=POyQQ5epwG-D1tuaeDOIdsdw3zKCfJnVM04Vt0W88L62lX0L6RSLOnAGeNAbX8ulkjMCLXmtkPZjHslMLLWy3naFnfzdnwWmLSjXW5IVyYzI_AcDnoAEdn1DDDt-UTJ7unXETni35o1idp2kXOYiVxdURzaO5o0G1wkzluH3CbpfSP7HS5CDEAx5i3oNeVT5G_ICzDULgKBhHsrgCnjdo7JF8TTn6esSIYmv5fDCuhrPVpVphpTuiji4193_rtLSPvJtiWmU9ZvhNAu39azEK3ahq2glsnLsyU0Tp1aQKCyGVhy2QcrmjkjJr1LjP0hNUL1b4n4cNTmj5-qNlRyrHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
حملات سنگین روسیه در طول شب به کیف اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/67176" target="_blank">📅 10:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67175">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIRAN ANKER</strong></div>
<div class="tg-text">.
☀️
هوا گرمه ؟
🔥
ما قیمت‌هارو
💲
خنک
🧊
کردیم...
🥳
جشنواره‌ی تابستانه‌ی ایران انکر شروع شد
🤩
برای دریافت لینک جشنواره به لینک زیر مراجعه کنید
.
.
🛍️
تمامی محصولات انکر در این جشنواره انقدر تخفیف خوردن که این گرمای تابستون رو خنک کنن برای شما
❄️
.
.
📍
فرصت جشنواره محدودِ ،
دیر نکنید که این قیمت‌ها حالا حالاها تکرار نمیشه...
👇
لینک ورود به جشنواره
🌐
اینستاگرام
🌐
@iran_anker
#anker
#soundcore
#جشنواره‌ی‌تابستانی
#ایران‌انکر</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/67175" target="_blank">📅 10:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67174">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b45db1d5ff.mp4?token=WitrGYTclFI4HG4_wKqDLZ_3oDiPxbAyfwm-RDlDbzdcmf7BdcJ6sTr2_LpJO335oYprn0H6T_dUa7-ffGCXoq-NP7UMFI4BX1BnNpAdvlDe_weZ7xnif8OUC8uaIvVpkoVoZ6Ekgv-vo3K97PETnpq6kUI5DXuJVGTAPQ3AzLL-oLeJZxIGm-bzN-uncBRZmUJrpi68VerGjANSO_Y__cclH-Q2-BaajKhTv59NoBXhen0s_0_DmC4qOWylecYRUcI2P1r4O8ZrfsOmZWqp_b4eu3n60uOCooIXc7WqQH5WU4iOUWQ3S0WSr1OvOFAOS8C4iYYWDarz_4wFlnQXvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b45db1d5ff.mp4?token=WitrGYTclFI4HG4_wKqDLZ_3oDiPxbAyfwm-RDlDbzdcmf7BdcJ6sTr2_LpJO335oYprn0H6T_dUa7-ffGCXoq-NP7UMFI4BX1BnNpAdvlDe_weZ7xnif8OUC8uaIvVpkoVoZ6Ekgv-vo3K97PETnpq6kUI5DXuJVGTAPQ3AzLL-oLeJZxIGm-bzN-uncBRZmUJrpi68VerGjANSO_Y__cclH-Q2-BaajKhTv59NoBXhen0s_0_DmC4qOWylecYRUcI2P1r4O8ZrfsOmZWqp_b4eu3n60uOCooIXc7WqQH5WU4iOUWQ3S0WSr1OvOFAOS8C4iYYWDarz_4wFlnQXvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جلیل محبی:
مهدی محمدی(مشاور قالیباف) جی‌دی‌ونس ایران است!
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/67174" target="_blank">📅 10:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67173">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18665cc14b.mp4?token=P45QGOUeoK7vLYHcG8Uk79y8qbIXzSO8GWcd_TXHZ9foodhsjKrlxV9sTtCGFLevgqliN36Mq8xwSLSItPR79xdJMczTb4U5k2okeRivyndtiw2A6iPE9bBqFCKk3m3yMUyI4ux_e_mZr4EqQhdC9-PLOJLK4lAFn36NDlA6Uror71y_4pUiOi6iwEoAKoKSzBdXBDTt84OGV_COhoPBoPjYI2NcmY8EJd3n4xjvliMgWWcYEytup3yJXp8rsKVKKWNxO5-ycXIBIP6pTimGuVqW3YEVzroowwvYsOdgRmd5iYfHjpuj04bC5FbGeacBIfcrzcPv-b2pBcOgyAsTLG60R-OXxwaPt4c0U3hQ-kqjsBVaFob2HpWJrcUeWm5Yh0MbSOgWApiVUIg7loadp9CwqLqrpOFQsTFAWBqPpi3zSjSf792RZRegmsUP0KULLBJbG2UeBppLg1zbb_h_uryBd8_68V4ocwilKGKVTimDkaRnxOel0m4gAx1CzXUQG9EFfMC9rRzz_buQCmZeSsCCGOzpBcdt8Pd06zdR5SfTW4I8TFnAM0h-Y751t79i4xcNEXsd8amkG8iBaPxw2g62KNz_RliX6-3nVK4OP5nAFuSy1zPO84l56L5ODkGKity--iT9z7_fpSPo9ZuO4Erzpu1t2Km76wGVNgrqT_8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18665cc14b.mp4?token=P45QGOUeoK7vLYHcG8Uk79y8qbIXzSO8GWcd_TXHZ9foodhsjKrlxV9sTtCGFLevgqliN36Mq8xwSLSItPR79xdJMczTb4U5k2okeRivyndtiw2A6iPE9bBqFCKk3m3yMUyI4ux_e_mZr4EqQhdC9-PLOJLK4lAFn36NDlA6Uror71y_4pUiOi6iwEoAKoKSzBdXBDTt84OGV_COhoPBoPjYI2NcmY8EJd3n4xjvliMgWWcYEytup3yJXp8rsKVKKWNxO5-ycXIBIP6pTimGuVqW3YEVzroowwvYsOdgRmd5iYfHjpuj04bC5FbGeacBIfcrzcPv-b2pBcOgyAsTLG60R-OXxwaPt4c0U3hQ-kqjsBVaFob2HpWJrcUeWm5Yh0MbSOgWApiVUIg7loadp9CwqLqrpOFQsTFAWBqPpi3zSjSf792RZRegmsUP0KULLBJbG2UeBppLg1zbb_h_uryBd8_68V4ocwilKGKVTimDkaRnxOel0m4gAx1CzXUQG9EFfMC9rRzz_buQCmZeSsCCGOzpBcdt8Pd06zdR5SfTW4I8TFnAM0h-Y751t79i4xcNEXsd8amkG8iBaPxw2g62KNz_RliX6-3nVK4OP5nAFuSy1zPO84l56L5ODkGKity--iT9z7_fpSPo9ZuO4Erzpu1t2Km76wGVNgrqT_8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
شادی نروژی ها بعد از صعود تیمشون به مرحله بعد
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/67173" target="_blank">📅 09:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67172">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CB0XP0Giyu-0MfhWp5xD6rHVyLScFtPqp-jbnSSRsH09U_GD1ihcDj9Zbs-evgLbsHFW42tcL3tcBPQx2Ke9Klq5PBc9l2pzu-ZoN1GMZr5zHsr31CnrHYz6BwGff5mZSvkNgCHoBdXY_Mk-jRx9mq72SWwWlxctGtEsbPjN1OfWFrMbq0iYj29acXsFtAylSBteVPHsZ5pC0sfwKMfedjkAbZolxLN6xLwMmG6BuOiEG3qDTt_50AFanjYaWtJj2gKUFNqJJ2L2tXtKrB9wBFYc3EmC98jx-GBYq54B-RN4I9NNf8OVvmo52lty4eI0DDD01fGuy07esRUGkpVtiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
‏اطلاعیه ناوگان پنجم دریایی آمریکا در بحرین در پی یک سانحه برای یک بالگرد امریکا که طی آن یک تن از پرسنل مفقود شده اند:
🔴
در ساعت ۳:۳۰ بامداد به وقت شرق آمریکا (ET) در اول ژوئیه، خدمه یک بالگرد MH-60S Sea Hawk که به ناو هواپیمابر USS George H.W. Bush (CVN-77) اختصاص دارد، در دریای عرب فرود اضطراری روی آب انجام دادند.
🔴
در حال حاضر هیچ نشانه‌ای وجود ندارد که این وضعیت اضطراری ناشی از اقدام خصمانه یا حمله دشمن بوده باشد.
🔴
سه نفر از چهار خدمه بالگرد نجات یافته‌اند و هم‌اکنون در وضعیت پایدار در ناو جورج اچ. دبلیو. بوش هستند.
🔴
نیروهای دریایی آمریکا در منطقه همچنان در حال جست‌وجوی چهارمین خدمه هستند که هنوز مفقود است.
🔴
علت وقوع این حادثه همچنان در دست بررسی است
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67172" target="_blank">📅 09:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67171">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
Join Join Join Join Join Join Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67171" target="_blank">📅 01:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67170">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/li0-dC0eFInf8aLHZ-2z6J2Oj1e-IZRfGNvJ6Lo_t5x31ydWfxPdh0ABXyw1PhP6B3OcBA2h96jUFvfJpIZqWGJtc5p46LDpQMlki8gN9n2SvKTHWt5Xwt58ARLWCYxVqZUf7xqu2Agef76iZxBQY6KDdRTQ_265WvM-ZchHSMduAXXRoTM1vPNekwEbJ_PB1BwJnWWseZj53usWIMsVoXkktIZBw9MLngXuOzzDdlfuhNI2CIlIAqDKB2B3TKu75zEa7t32DLRU_bKigUTxkr5luDoaUQbYjb5ZihenD2VqW4WQYXqfbddVoemsSRVB1sVyU6DguUPj1HkaWM-0YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
Join Join Join Join Join Join
Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67170" target="_blank">📅 01:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67168">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BMzb2jPvZl1kVvbqSbn8-AtGq8L1cAuA5vgd_1hiDrHZ-ABXTnZsJAzc4DmVSLgrAGUXHvtI7v5T1DAgcArcK04wxW2fCI3m1zDG5A7CQ4lQ0ygqJCutRMU8nVOirU3Vf1r1_xAHxXjujQA93VQ3J0cOuFTwZpX00oRv4yHrGqyBnVq6YyARcd0TEBET5kLaPI_jIOl_sp0lfJUgI_ESn67rxk4clQI_xXnTCKb3N_PQvAI5QcFQ7evNWU3iKY2i9p4jYOzW5UZVJuuJonJTKiu1f2mizOGs_S8ABhDeW9VlQqWD8Luc4wauEJRvdDHiTQqYzGWTejsxZJjRazoARQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53ac383b11.mp4?token=Mh1RET6d-26eMERe08YtydtD92HVBXYWF9seezv_QWL6d4dKYse-YcB6paF1IobXmMTtX3_MKAyMil0HfSCslTnUinqIkm8OD5eCavcd2AGiNHQZbmpgWZGehgsI-1I-jMY4037d6WOIxVLfA4-OxY8hK-tcTNDYfOpN56u2qamunf58BXTkKLq64rTnXatnJyIxuQacd4Z-BDv4vu7mv-Xdt809MIlIIJe1NNHtJSRHpWgjghke95mGqlblsXNjths_NgOMAwAoCwcjgwmmgHPUlnI-bUrxSTuFBfXl0iWYSP7zEytIPH8yFmTUF-FZIiRBTGWq7qZE9IByl6rOcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53ac383b11.mp4?token=Mh1RET6d-26eMERe08YtydtD92HVBXYWF9seezv_QWL6d4dKYse-YcB6paF1IobXmMTtX3_MKAyMil0HfSCslTnUinqIkm8OD5eCavcd2AGiNHQZbmpgWZGehgsI-1I-jMY4037d6WOIxVLfA4-OxY8hK-tcTNDYfOpN56u2qamunf58BXTkKLq64rTnXatnJyIxuQacd4Z-BDv4vu7mv-Xdt809MIlIIJe1NNHtJSRHpWgjghke95mGqlblsXNjths_NgOMAwAoCwcjgwmmgHPUlnI-bUrxSTuFBfXl0iWYSP7zEytIPH8yFmTUF-FZIiRBTGWq7qZE9IByl6rOcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
حملات موشکی سپاه به مواضع کردها درمنطقه کویا در استان اربیل عراق
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67168" target="_blank">📅 01:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67167">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">‼️
ویدیو‌ ای که گفته میشه مربوط به پارک ملت تهران هست و هلال احمر چادر های زیادی رو برای پشتیبانی از مراسم دفن کردن علی خامنه ای در آنجا قرار داده.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67167" target="_blank">📅 00:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67166">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b0f2d20b2.mp4?token=VRLhSwLyOAZq-Zx7NPtGMgNSrDPP9C0E2qT-NHFHjlCxo0xxnHE-i-DtgigomvECsMK9fndCXNP7nCGTUGS6_GlLzZFQMRpbkHSNrX6SQMNQbB42Sswf1SIXucHVlQunGJv_lfQcCsny3azbGbRUY7frqAHIUVyNYC_jxpde5Hd7ss5yXtZvUKo8VrIur9_UADCsVpTWLNZH34wm_SW2YGwB25vmHFlyVgRvTEX-4RAFKlL9Civq7VXHgkei2GpbMh64gqjkr6OQjPAQwHjwTTQ5gvalebSZ8YtKI3rjrtqkjeAG3MmuVcg0fXg3Fkc0E2zqwaIAIOg4BQC0pwoi8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b0f2d20b2.mp4?token=VRLhSwLyOAZq-Zx7NPtGMgNSrDPP9C0E2qT-NHFHjlCxo0xxnHE-i-DtgigomvECsMK9fndCXNP7nCGTUGS6_GlLzZFQMRpbkHSNrX6SQMNQbB42Sswf1SIXucHVlQunGJv_lfQcCsny3azbGbRUY7frqAHIUVyNYC_jxpde5Hd7ss5yXtZvUKo8VrIur9_UADCsVpTWLNZH34wm_SW2YGwB25vmHFlyVgRvTEX-4RAFKlL9Civq7VXHgkei2GpbMh64gqjkr6OQjPAQwHjwTTQ5gvalebSZ8YtKI3rjrtqkjeAG3MmuVcg0fXg3Fkc0E2zqwaIAIOg4BQC0pwoi8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یک آخوند:
در خانه ای که اسامی محمود،احمد و محمد باشه فقر وجود نداره.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67166" target="_blank">📅 00:28 · 11 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
