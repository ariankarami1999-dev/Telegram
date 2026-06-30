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
<img src="https://cdn4.telesco.pe/file/uQhk-sN4BYEX2u-XZQCdiJTOwlohhS5TRWvkaDwWKKRR49SEu-Gj0BKi_kM2efxvizIdexUN2xtbsgIJAjSbZ3eBq8TtPqNizxI10tTxJhHB8ihTP1QcJWQ_4WuzQ4LCSGS8CB1SC9ZI993XWs-7i5SYI0GeyfZMV6Ac380EhaEeJdWbgtr1WZYKOuzyUwkafw6z_Bi1hILqGJZRfZKvI1FmG6T62hfdF_YrWaRLlD5QigJg57owXM6Ta1ZvCpmry3O4c1IWMwxO0XmcOvZMy9pWwjGaMeE5_q1_ojZZ2mFS-if6vlpg7DazDDyTWhHujA3NNCPAVx0mpxEUM1EyOQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 356K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-09 22:44:58</div>
<hr>

<div class="tg-post" id="msg-24701">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BLnIdfs_am2_a2irfZi9CEF21zixY-pM1_5iQYYgSIh5hX2kFI1mkE9Y2BvKiI6YsVBFF6lAWTvYjIpMpx65jp3SiUqRtZK59JyGDs75iZhQQGDGsRD2uX0U0x1x97fQh5aQ92hAeBAoYXqCX3NrAg-OtX-7TRmfY4Lco_gUOzCVa3U-Z4nK6yFY6K6QHRuA0vOscYEFU5aUBomfeoTNdXO6FKSaUUH6jEq0iSozxataiAJUYA8RfcMo54cbmQpeUBcORKjy5eHYOBMv7iGf5r9FSy17clap2T1001xsghqYLiBRuSqTHcJ9y-BjGqo8TRAU1sTZgp1coxapHhv1zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تااینجای‌جام‌جهانی 2026؛ خطرناک‌ترین چیز نه پنالتی بوده، نه وار فقط و فقط یه عکس یادگاری!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/persiana_Soccer/24701" target="_blank">📅 22:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24700">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJRoAmosYAwTmtUiAs7-lkWJnwY_j3Ixtg7LGU4mD9tQHTvuefQ16dBdyGMBEFMSNL5EIHLpl6YHHWIVtSqxutTf5H9GJdaC7CR5SJ5s4VPkSNnKb0b4CrbKGDDD7iwszKbNfs_N62-SYSQg7SDChboQ4KfLAZlbIPQ43WIEAqinNAVjIKhP4iGjCQTd92kgX51l3TTXqafF6KKZ35R8G4hnlcj86vyRRKY67X69kwJeh6emxzgax8FH-tTiWZqBI7qHzjaeOBW6Qhr_ct4-jA0TA665dK5eP_sjVRyafSWTnGKePdza539ESwirHYWKV-vKXNvlLHW03Udjn8LNcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇳🇴
سوپرگل‌دیدنی نروژی‌ها در بازی امشب مقابل ساحل عاج در یک شانردهم نهایی؛ چه کاتی برداشت.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/persiana_Soccer/24700" target="_blank">📅 22:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24699">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XN8E5EHIz8S2wOQANxf9okRmytkNMnJz6PDROHGdef9mypBwzsUD31WcgsD6iHMxePswKVg7Imu61ByjBJ9v9cI_jauinKE54FlGfdVlikJFRG-n1yZaD-m81XYTqMQv4VkovAwIw7jMynznAUh6izF8DwQ7J15b7IISxy222VshJqR74Ell80t2cAI1tzVGVi1gSJIoUYpFHtxZT-Jv1oFAOFtttEykn_UBF9u3kztYOmnZ8UJ1BIG8M2ETaKSmBggpWw4jTteoGx7aDnplm2RTc-Jhigy10rlh46KzoD47F5wXqzzPaGsEe3cmHqTV6GA6xjdtYle4iPrT4Le0OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ به احتمال بسیار زیاد بخش رسانه ای باشگاه پرسپولیس فردا پوستر رونمایی از دراگان اسکوچیچ سرمربی‌جدید خود رو منتشر خواهد کرد‌.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/persiana_Soccer/24699" target="_blank">📅 22:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24698">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HkVdl4aWrmcD0-A2_biYRPwxfrqKdr2cHc8CbE5Yl-nFxv_fPUDspNZkOjGmLWobLs745wwAtbvR77P1C_h6iSAU51orEwtM6dcETFVK8deCnk2maha9sFhndsfKIisZ7LsT6wIsh_lvRvTBqj8RyD1Dc4vkh7WR1-9gX9J8eYlhQe-RQavSgWImn-_M0ClY1MNpeeMYVzBO_lWxoV4oEV6GHNiagm3jhot3pQ6MiSPSk2KkYhHkBfzEXNdt-p5s6vMBowF7edwQr19vdGy_u97OkkdKxKrU2J2IUiQZzFCfKSk_ragaitLSSizhIHzyqCqk_ZAdDIUheeN_gkHVDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خداداد عزیزی در ویژه برنامه امشب جام جهانی اعلام کرد بنا به دلایلی پیوستنش به تیم پرسپولیس منتفی شده و فصل بعد نیز در تراکتور خواهد ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/persiana_Soccer/24698" target="_blank">📅 22:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24697">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b011e22cad.mp4?token=dzzMgWHaFS5YeiGDShIN4Aj1tFkUeoJe9p20vIyvsqqn4jbsMNE_IqlPydxCkGeXaNTmEBVUZby53s_xgTCmc8eGap3dIocd3kZWjIhyzbFdRqWb_FJQyabxsVqkJ5doMyFVfp_pjnVV_fEbW8NeJzCmSQPIv1C7hqUNr4Yy8rdNEx2EVF96Fo5fxHFWzly7pZRyi5gpITisPgI3jkZ4Wwvo7fB9VYwuFiZMlZfazIxDKck-GiTZDPAXqiKDj5_G5Vy3s7ejUaTPlDtzdbcpi2Sa8NxLx3GNbUEjTf0FCCdNFxhhe__MY4SYY357ESwHAwkPrW0Q7ImW-NH861QN-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b011e22cad.mp4?token=dzzMgWHaFS5YeiGDShIN4Aj1tFkUeoJe9p20vIyvsqqn4jbsMNE_IqlPydxCkGeXaNTmEBVUZby53s_xgTCmc8eGap3dIocd3kZWjIhyzbFdRqWb_FJQyabxsVqkJ5doMyFVfp_pjnVV_fEbW8NeJzCmSQPIv1C7hqUNr4Yy8rdNEx2EVF96Fo5fxHFWzly7pZRyi5gpITisPgI3jkZ4Wwvo7fB9VYwuFiZMlZfazIxDKck-GiTZDPAXqiKDj5_G5Vy3s7ejUaTPlDtzdbcpi2Sa8NxLx3GNbUEjTf0FCCdNFxhhe__MY4SYY357ESwHAwkPrW0Q7ImW-NH861QN-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اون‌بازیکن‌تیم‌ملی‌هائیتی‌که‌کارش‌هندونه کاشتن و فروختنه، وقتی میفهمه من رو کلین شیت مراکش بت زدم: این چه سوپرگل برگ ریزونی بود که زدن!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/persiana_Soccer/24697" target="_blank">📅 21:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24696">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BdMojqV6Cs3jFm147rBSxfAypPmTUufUDaEziotwWerM_ogeWQoO7oRA2VD3a026B_NuHc_k7Rv7tK_Qlz3Jx_D-skupZFKkBrotguEQgvAwKcObGmpXZto6E7wRLgh1bOno6mZri0NzLhB2OfvYs7Ym417-oHpz4-6MYbAV0J2mEv5c7anmJBKY6UQVH233E3Rr6KjaYPB0HVjvmIVATL9BhkK5Nx5s7uWBNSH4R25naOPScMyNFf4Z3EbHW7O5NlOFzwVlcVs0rtpO9hxWI3baRLTHy_RasJh3k4j0OX49dzMM5HXwoecXZhQYXmneHsx1ext-59vtZsEG9pDhAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇪🇸
لامین‌یامال:
شانس تیم‌ملی اسپانیا برای قهرمانی درجام‌جهانی‌بسیار بیشتر از بقیه تیم هاست. فرانسه بسیار ضعیف‌شده و تیمی نیست که بخواد ما روتهدیدکنه. هرچند بازی دیگه با اونا داشته باشیم باز هم با اختلاف میبریمشون؛ ضمن این‌که تو عکسه هم خبرنگاره سرشوخی رو با سپهر حیدری هم بازی کرد‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/persiana_Soccer/24696" target="_blank">📅 21:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24695">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9726fa772b.mp4?token=KPetDvPBzAyfC-pilnTnr5XPmvNFAVmfrYZQTS6iTjE3DaC7-YzKAXuP2Ib5UH0CfW8oJijltEg4w1OJY6pi7ukn_HCVP77CpAw-O2O7RhRPP8-RTNb3sVEvth4P1p7XmM9SW9HK-6rleE17eOjUdbD9cA2hQL1t5yVJ4a73Vq8G1rTnp1igrc1kWLPEyngdb3ebQ1kO8iDjK3s-pr10rZ6DvNgIvSUbtr3U79TP5UlZDs-jQal-bN2atdQZpnWiLXrdVIHKdhpCxNcMUwPva9aytK6RvOynM2pv2bJGyfq5cXzt38dJvyKd9uLX1zdhsgSxb0ulVJVyaMzJTRU3ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9726fa772b.mp4?token=KPetDvPBzAyfC-pilnTnr5XPmvNFAVmfrYZQTS6iTjE3DaC7-YzKAXuP2Ib5UH0CfW8oJijltEg4w1OJY6pi7ukn_HCVP77CpAw-O2O7RhRPP8-RTNb3sVEvth4P1p7XmM9SW9HK-6rleE17eOjUdbD9cA2hQL1t5yVJ4a73Vq8G1rTnp1igrc1kWLPEyngdb3ebQ1kO8iDjK3s-pr10rZ6DvNgIvSUbtr3U79TP5UlZDs-jQal-bN2atdQZpnWiLXrdVIHKdhpCxNcMUwPva9aytK6RvOynM2pv2bJGyfq5cXzt38dJvyKd9uLX1zdhsgSxb0ulVJVyaMzJTRU3ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
برنامه‌‌ دیدار ها‌ی‌ فردا؛ از مصاف مانشافت برابر پاراگوئه تا نبرد تماشایی هلند vs مراکش و جدال حساس یاران هالند مقابل ساحل عاج
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/persiana_Soccer/24695" target="_blank">📅 21:17 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24694">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a72b5a564e.mp4?token=iIaTcFIqbXhneYRHgA90lt0cLtpx-nWoXMzBtALoCSG65NDBmZLjWmDIkOC4h12UKOs8b7LHSChgm-AQEuLod5Q2XDk-8nRilmfX_tZ63hIJH6q-UxmWwmm5k8HBS1-zr7YNUntBvjuhfUNx-Emq7G5E8vv7KuaS3nqQXJ0ZxRKMoMl8n56Uud2SnWFfymLuLNhmGwDszjxs_7O2UP1SQKywVDsROtpqBSnMFMG6KX6LXzk7PjV2S2JolFp-B5_1n4-0LeuDGtaQ6Mo0TUpZELqgN4u80ZYKgHip6L6lNY7rqak-lP2bAUHSmQbcbLk4CulVnaZmEWSDu688errU-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a72b5a564e.mp4?token=iIaTcFIqbXhneYRHgA90lt0cLtpx-nWoXMzBtALoCSG65NDBmZLjWmDIkOC4h12UKOs8b7LHSChgm-AQEuLod5Q2XDk-8nRilmfX_tZ63hIJH6q-UxmWwmm5k8HBS1-zr7YNUntBvjuhfUNx-Emq7G5E8vv7KuaS3nqQXJ0ZxRKMoMl8n56Uud2SnWFfymLuLNhmGwDszjxs_7O2UP1SQKywVDsROtpqBSnMFMG6KX6LXzk7PjV2S2JolFp-B5_1n4-0LeuDGtaQ6Mo0TUpZELqgN4u80ZYKgHip6L6lNY7rqak-lP2bAUHSmQbcbLk4CulVnaZmEWSDu688errU-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔴
👤
باشگاه پرسپولیس در اقدامی عجیب در روزهای گذشته با خداداد عزیزی سرپرست فصل قبل تراکتورصحبت‌‌های‌‌مفصلی  داشته‌اند و قصد دارند که او رو برای فصل بعنوان بعنوان سرپرست جدید سرخ ها انتخاب کنند. فعلا قراردادی امضانشده اما احتمال اینکه عزیزی به پرسپولیس بیاید…</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/persiana_Soccer/24694" target="_blank">📅 20:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24693">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A6-Udv9cN13f1Enyax2S9JS8VnWNsE4-sbwMu1UiA2073DBYpc1co6o8ter_po3ddWkOzyUqDPlE3yWYzPzbeSrtIrYqKhYSfUjvHSeA_585CaZtAmls5I-AYvrZ4OKmZdlTczg2wtSGxPMD6ROELsTw2LAZcJzJcTKvG7_hTwmMrLoLGnto93V4EcloQW11kygxvpIlYKWNq_he-GVrfb069QAp42r693L1JtOFjzJlqQS0YRpBV--oDMPLkoi5ena3NP8pSBxZ-GoNOE8NjoaW6keo4wZNQlnlSdiGp_keOg0ht42a4gDVe5N8AHjSG2uOdIf-lSgKPpMVwTATaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
همانطور که پیش‌تر خبر دادیم؛ یاسر آسانی ستاره آلبانیایی استقلال بامدادفردا وارد تهران خواهد شد و در تمرینات آبی پوشان پایتخت شرکت خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/persiana_Soccer/24693" target="_blank">📅 20:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24692">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AMN7AT8fRVngPS3XUv5d3wc8MsNkCBF01IRFEn1pcTCKpBgbLwPCxhmwZDa-yEh8zfkMInVMyP_jTSKoXV5juBtMyZKzKPsK6qjOadKgD33BGzEr4QbptHtNUynTzjmLmc-mKHOu3JCF2Ad700m4bZ0o87V0sdn6bk3cLgHAnhtUJR3mpdrk2jArjDuHpA8GU33roh7A0Qs1gSa1XmlHzWblFP-uxWrebV8MQ5H_y72SgSgBs2KjvbFrdrWpXOoRSeAWziK04VefQUFv0um9cLRY_mAjuMML9irTxLyKu-myUw_H7-IogGugQQl7gGvUosIGznTnWJI_MED_x4dn_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فلورین‌پلتنبرگ: سران‌منچستریونایتد با ماتئوس فرناندز برای عقد قراردادی پنج ساله به توافق کامل رسیده و حالا توافق با وستهم باقی مونده است.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/persiana_Soccer/24692" target="_blank">📅 20:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24691">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DLjnQQ59dRRCgV7u82sDsnyiy5kzunGlS8pZaSDZGrxZ6T86CThu4IFcdenOj0eaWFU_3L0-Mf4zYY70F6DyGAEw7JjEb7PlOYq8fQNTZySu5cnni-bz5WigHW59CELTyN8JTYdWdGdtKe5oFf2rsuiqT_iBdUwwi3fKNYhrBsAz5QCSnAzfZg0gT15f_XybORI_TUL537r70llv4NWdn1cOWvNNPlzH-syMBddjBacusTQb95omkknjWLgYjFs3IVizyULnS2UeBCqmJXWuU2cR21g_a3M1M6NMyYrGFJKdy-2G0qrD7hp3kuafJ7ngYkoadVmT-Qg6acVT-gcgCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ باشگاه پرسپولیس درتلاشه امروز برای دراگان اسکوچیچ بلیط‌تهیه‌کنه و این سرمربی کروات ظرف 48 ساعت‌آینده با دستیارانش وارد تهران شود.
‼️
بعد از رونمایی‌ از سنگ‌ اندازی این مدت بازیکن کهنه‌کارباندباز سرخپوشان‌پایتخت خواهیم گفت. این بازیکن از وقتی فهمید…</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/24691" target="_blank">📅 19:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24690">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HrGwScrGnSsY6uswge5bAXPzBNjLdDutkJJ_2NuEzmx4h2XB_ULAx5JGEy7M08oeFP-M94WhYRA1YZGGxnJ0zIYI8TuzBNFkd7Nu0TLBe6xIQQskIfNkkinLr4_a9uTDv_QwdIjXzg3NaJEouPxx1sEIzdx4hcUdfWY_xarTQa3iSlROYhO4UsZAD5dAiiT-yGq0hZxb6om3Z8V2KQuHotzb7gM8s3gUdXhIWmwbko3hN6AFA8ezS3CDSvbs_ke695X8RfTwzEy-VcLkvvru7rW5sRKvnFhZSNbC3Rk1JJ_nApIYPMdCvke3vNVENXR-XFy4MgtF0DT_LspxVmIsnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛باشگاه پرسپولیس و بانک شهر مبلغ توافق شده به اوسمار ویرا و کادرش روفراهم کرده و فرداصبح قراره‌این‌مبلغ به حساب او واریز کنه و رسما پوستر برکناری‌اش رو منتشر کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/24690" target="_blank">📅 19:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24689">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l1LhQXfUAV1hvnLemCvuhVrH58qle8UvTyaFDlSwF5wvFKp5feNRGuCbYFw4-IX-3fzZarideKCjVEsWbVA92zUu5o6YnIw5UHDsJ7b4iEP-YOcyEJp8xlIoa7Y1BcTk8hpseKMwjSa1vvxcn0TUnzS0Jgi4MVZqHYTYva2bOUFsBValbLa2K76vGAt4ovsU28YPfTARNWSYgYYpX-rpJ8GQbIOVOb4feqLCRqzs5mbQE_e36sgccM9DUOm_q0Y2aRXGY799Jue-q6AwBIya0rFQa95rH8lNb1DT1RhcnbbTuwopW_4qgBZ7kyBz7ZlVMrde4Leir4Afqrh-2__rLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
ضربات پنالتی دیدار امشب آلمان
🆚
پاراگوئه در مرحله یک شانردهم نهایی رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/24689" target="_blank">📅 19:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24688">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jkjvtxCqd_7Bz-cGUSWdTaq0IIjalJIKyEQlu-XOlEmEDDfLrxg-uQUZO38Lt-JZ1FhQDL5Y1aFSfmbqA3uzEtk1qD4j993JGr_5IZOWjP5sKDyMZu1pWihPxpYSGrauGh-APoWp2YldunqbTXCnOdWRQIVD9E-BijOkVpMXHMOwPq_YstVXInvyS-d76XhzcJRYGIuioSVv4uhJNqsEH2iJU-ZC6vCTvMNFLC8aJHmsJndJQ_syFQL8MEvaKLBWWx0ICVhnmJTwOxXBrDdaDB8p4o-IIMxTFUN02MAaIzKHrhZruCcRes5X4q-_Z1Nvmz839gQPMbahCRrIUX593Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مسابقات
جام جهانی 2026
⚽️
🏛️
رومابت دنیای آفر ها و بونوس های ورزشی و کازینویی میباشد
✅
🎁
با شرطبندی روی مسابقات جام جهانی وارد تورنومنت2.500.000.000تومانی رومابت شوید
تورنومنت
#میلیاردی
🚨
همین‌حالاواردحساب کاربری شوید و شرط مورد نظر خود را ثبت کنید
👇
🌐
https://halvirox9371.bar
✅
کانال تلگرامی
#رومابت
🔵
@RomaBet_official</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/24688" target="_blank">📅 19:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24686">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85e47b5880.mp4?token=S9fhAAM-J75y0qxEQKf1CYkpYA54zSx7Gi76-KpF1TGX7HKkRrXD0VqiX6QMMrGbpcP0_Lq0CU4Cg0dwyWRRz4cq2jl6Od7ZDx7yjHVdWlryNFvaCCLxoVCENzJ97R5rsyzoMJNTyecBrso4ifGi8DyHzHMrxncKfjKs9P2QCyQYWrNcKJY7EfLQPPyANTN8CjZgSa_CLMF6sjVlybIEEk741w5BoHgMZOfqjhZoREhFlv7CdxLS7p0BLLb_tDHnJJZvYN2OvpmXTqov8Ik4WEK_PuyAWBOvI6OwsKAQG2rP6WhsqqETOiGn31Srpw3aEY8_UvrFl0JYxI6j4m9d1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85e47b5880.mp4?token=S9fhAAM-J75y0qxEQKf1CYkpYA54zSx7Gi76-KpF1TGX7HKkRrXD0VqiX6QMMrGbpcP0_Lq0CU4Cg0dwyWRRz4cq2jl6Od7ZDx7yjHVdWlryNFvaCCLxoVCENzJ97R5rsyzoMJNTyecBrso4ifGi8DyHzHMrxncKfjKs9P2QCyQYWrNcKJY7EfLQPPyANTN8CjZgSa_CLMF6sjVlybIEEk741w5BoHgMZOfqjhZoREhFlv7CdxLS7p0BLLb_tDHnJJZvYN2OvpmXTqov8Ik4WEK_PuyAWBOvI6OwsKAQG2rP6WhsqqETOiGn31Srpw3aEY8_UvrFl0JYxI6j4m9d1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇦
سبک خاص و جذاب پنالتی گرفتن یاسین بونو که قبلا هم دیده بودیمش؛ پنالتی امروز صبح هلند رو به صورت عادی شیرجه میبست عمرا میگرفتش ولی اینطوری راحت سیوش کرد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/24686" target="_blank">📅 18:25 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24685">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c85d949fba.mp4?token=DayV63JvBtYo7iVk59NReyoqS1R3eIxpI5fv8GAm-IB87_POCHLmw5UDQqbO_ECzOEyV_Q8GBmOGMOXiTK7BdZE8tHPteeLq9A3A-Geq5rdECJXx1I1i4DVDrwERCIKKkWsgADyvYeKNyBo_81haL8cxkxvnylYj-M071bZSS9AjylqzUtbk-QIswIxDZZzUNj91nlXVdSDrswfGMhOuyWmlksUW1_bseAW4tywYKvBfOw4I30uEKBVqzwycInNSzS01BO5hiutPgKWv4SGO2pYbrSVeEoNPBNRQbB0aGoEXRbWv_11AgsQgj255iLMW9UgUbuSkKe2mI_r5K19VWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c85d949fba.mp4?token=DayV63JvBtYo7iVk59NReyoqS1R3eIxpI5fv8GAm-IB87_POCHLmw5UDQqbO_ECzOEyV_Q8GBmOGMOXiTK7BdZE8tHPteeLq9A3A-Geq5rdECJXx1I1i4DVDrwERCIKKkWsgADyvYeKNyBo_81haL8cxkxvnylYj-M071bZSS9AjylqzUtbk-QIswIxDZZzUNj91nlXVdSDrswfGMhOuyWmlksUW1_bseAW4tywYKvBfOw4I30uEKBVqzwycInNSzS01BO5hiutPgKWv4SGO2pYbrSVeEoNPBNRQbB0aGoEXRbWv_11AgsQgj255iLMW9UgUbuSkKe2mI_r5K19VWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
تیم‌ملی‌آلمان همینجا حذف شد، نه مقابل تیم ملی پاراگوئه؛ اصلا بعداین‌دیگه نتونستن درست بازی کنند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/24685" target="_blank">📅 18:11 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24684">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LLJgzDWZcG9AxvwON9lYhceyYnLF4GH8BZcYKnzbPYSbC5bVAr_MLEhNQqtRrpi4RcioAANtBgldc4svRg4U2bl97siRHtheVrIPzke7RvdbGvLhH6rCu7XYZt7-Lk8Pf08ZKG7iAILCiD5oq8GM3TEThaR4p5y3f3_5RuLWosk1jxNDX9NoDor5mtgmmY3U8DvxD8_il47lgLiYUiAWOX_tS8OHD2hCAQ7MmODCsIkwqRTwBQLtNrZcYW_C-ihTu81fm0c3rLw7VX7gLaK4v0-J5CpNf7hTIZf8vvqDXL1fC6aM9ALqs0RRSs8nBjiwwxGSIsRBC4P4HMbWQXpJvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
جادوگر تیم ملی غنا: در طالع و سرنوشت کریستیانو رونالدو نوشته‌شده‌که امسال قهرمان جام جهانی 2026 خواهد شد. سخت و دراماتیک است اماپرتعال بشکل باور نکردنی قهرمان خواهد شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/24684" target="_blank">📅 17:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24683">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CaCUPqxv32UYRku8h8qkKVQdWEAK8MtSQSZgjbsopbpTzAaponwwGxuokY5DqVCsnJQVLZpjT0jAZuANXM_nQvuBLPdjc7-IKXmp0NpnkvNi2LnmPGR0GEEWdHc8vzQD4EQvMk2wKbgGN7NuoZL8yoL3eF-pMlhW_JEbCnMJZ_X1kGBsVCH9eTc_BRTq-8WnpedUqejDJYhIUmIc5Mu5k6FVpRir2hOrsxT8-3ZHYfKNym5yEY4d8EelsQGlhyiAt9P4KD6YmAPR942htpcoW3bExbmJvk0y9iQirN9flb6Q1XaGHTqgF3W-Y-iwIG7h7T0cfinnefaydKflRMfCvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خوزه فلیکس دیاز: باتوجه به علاقه اینترمیلان به نیکو پاز؛ فلورنتینو پرز میخواد او رو با الساندرو باستونی مدافع 27 ساله این باشگاه معاوضه کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/24683" target="_blank">📅 17:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24682">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jsIXrE17XfkzWW8239RTeGd8uXxt-lz3UBWK42K4uF5GFgeowu3kJOdxtINLIWjFMQ2QxqPgQ71YgAWsnBXCBrO7yxOuK5_inqNfR9S9plfXdlP2tvA6WNcjVozwORoh3FvFBBEwaqbLEYDPL0YavgEOxWLF0yo3QEngIx8j0uZccz0qnqgJtKkGDi9syWYabscwXqfD8LcXHzgCQSznHL3bjZSPoP_EJvK-7WXMlwOdC2Cbw1EVUIl5heJYF80cq5qV0DAN9hndZO2K46pazLC7pXGZlELbyzOBlzNUJxmI9f-sOtGwkIAV-GNtj9_JVBkRgdDWukeenfCaJEaQqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
کنفدراسیون فوتبال آسیا AFC نمایندگان ایران در رقابت‌ های آسیایی را اعلام کرد که استقلال و تراکتور در لیگ نخبگان آسیا و گل‌ گهر در لیگ قهرمانان آسیا 2 شرکت می‌کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/24682" target="_blank">📅 17:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24681">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b6727cd80.mp4?token=QC0CcCVNr8lkSet0WcVm-rubgZTv-st0xs56uYPnF_IHywM2eFjsGS_hZqZsPORGr4Qi3djSndpFm1ux2Wc1SFE6Mipj8hACInQ3fjTQJGp63GFv5pvY1sSUFhdcWc2O7WBdBaSZlsXn1lfhZk4lv7ZXXL_Af1xoWdYrSMmF_npjpWTJZvCg8LM9fPbivwqPJQzrzKquwQP67DqJCRcKtM1E7W_GqBdu4ux5XrnVcczQsOa9Pjys3GAXXhW-PdCJNPL_mqQkTSiBWqPhDV-sYabjDGDtdAvaV4DLpaz13M0cqQ8BzAuOi7W_6nOd-IX9GlDtVQpiowQc4Yrswikgmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b6727cd80.mp4?token=QC0CcCVNr8lkSet0WcVm-rubgZTv-st0xs56uYPnF_IHywM2eFjsGS_hZqZsPORGr4Qi3djSndpFm1ux2Wc1SFE6Mipj8hACInQ3fjTQJGp63GFv5pvY1sSUFhdcWc2O7WBdBaSZlsXn1lfhZk4lv7ZXXL_Af1xoWdYrSMmF_npjpWTJZvCg8LM9fPbivwqPJQzrzKquwQP67DqJCRcKtM1E7W_GqBdu4ux5XrnVcczQsOa9Pjys3GAXXhW-PdCJNPL_mqQkTSiBWqPhDV-sYabjDGDtdAvaV4DLpaz13M0cqQ8BzAuOi7W_6nOd-IX9GlDtVQpiowQc4Yrswikgmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
🇩🇪
#تکمیلی؛ بعد از حذف آلمان از جام جهانی؛ مانوئل نویر گلر 40 ساله ژرمن‌ها رسما اعلام کرد که از بازی های ملی خداحافظی کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/24681" target="_blank">📅 17:25 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24680">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ESibDmisJKlZ2zyEycqGMW2K333jb-N7lpBKQhkLy5trmW6yFGSF32GgvOjVDYvVJeNwnhzs_Tg3ILjg3fmdlQDAawTZ51pzeSao1mg3oZLGK7_Eui5uZA4xmCmFSBqXp-pa2DYZY_y5SXH-X4Zs3SqxPbAbS_CeN9CkcFkwG4hRbadD2-XIPxeOhbqId05TcolPrWXD6Yi4QeJ9GC3toobkkmIQF6g3n01L3S9N_662qBqLPfhSZwLlxNAB2J_oOrblY9kxZJMcsPLWszT_TuhC30BZfhSSzOk3M3vU9ATgIoybrGzmjXylZyYj5fLgzv3MJV65xOhpxedoHRO-gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
مسیر به‌ظاهرآسون تیم‌ملی آرژانتین و لیونل مسی برای رسیدن به فینال جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/24680" target="_blank">📅 17:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24679">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q9VqGRQQwqWCw7DRSm5IRDFfkVW_AChBdyXlUaxdoVe3uUicRVMB09csv2FibYrSmeQpu63gol2w4fU0bVSY2Yzwbii54G_IibMx6VCsZdEQ6-TDHL8LQ6P7NvLDWsNOG53PzBaGnK-qlJOsmVIITlo4p9gUjDiO0QJDjm9YAD0nfaTX-57-fnNunrK9zuw8SAeNHb8XUEEr35R7xDXt1Rs9AgB5ezni1k-NuCTnlymdvB7f1qGPq00lW4Xr9iK_aWfTzlx4bh9zCksjT7A-HcfeYXeczT7hP2ZEMYn_OE1rd9aqxcR6CcTY_rWyvxlovltOJsDVz1u0eOTEN0-iaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تااینجای‌جام‌جهانی 2026؛ خطرناک‌ترین چیز نه پنالتی بوده، نه وار فقط و فقط یه عکس یادگاری!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/24679" target="_blank">📅 16:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24678">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V5a1o-ts5-egllzUBeHk_zg0YUrqQ_f51B-vXYjBNF-WZJwREc7u112BhGxTxqvFmwosPrYZe4o_a-APzoVlSWDolwBhviZsmVCp6XoAsP5YkNGpfaZe_S8ob0Gf_C2L9Fuuh1W3vb9tmdzi22DmWioitKt6p_yV4B-cO1KFn1V0HeUuLNRyTNUJYjyY6izFoYVdZMyshzeAsQX6PLRbv1q5st9pE8pULl-Mv3yTas5-FOyMLVZvSJNfQf3BcNaPvRUVrxQYK0vZGSpwGAWpEoejubFCNsOW5QmyFB76msG2eWPsBISiaXUzb1B532VO2ytf2xT1ZhWPSuDClWYIIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
بااعلام‌ایجنت دوماگوی دروژدک مهاجم کروات تراکتور؛ قرارداد این‌مهاجم‌گلزن بااین باشگاه به پایان رسید و هم‌اکنون بازیکن‌آزاد بشمار می‌آید. دو باشگاه پرسپولیس و سپاهان به دنبال جذب او هستند.
‼️
اولش دراگان اسکوچیچ باهاش حرف زد... بعدش مدیریت باشگاه سپاهان با…</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/24678" target="_blank">📅 16:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24677">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VmayYgkO170ckdvm_x-3h8bxi9DgB30vAeRIVswYJftkvIJhQPQx9LQwIlNnB9wA7vww5TI80KHHMwoqhGWD8zwKgXw70BaN-g60z9c9sWJEjIggq-KmPUzY90U-h-IAgIaS6NS_9YgGhzhOggDj-bS1BQTAHEXiFRfrTBziTipv0eq1dWuo3_hjUyoB0utt9BQuJ8N93_FKT0YWz7k54RV4OZWWEEI1eNErHzrdGA3vYVLaTlzO4v__NxXKm6v-uXLmTyxr9W9GeOfJcKNmUHY5L9YulHlEtoTTtngPQkDx0bND-CGmnoD9e7F6cN_M7v9NGL_REUBVBtNfY1ai3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
شش بازی بین آمریکای جنوبی و اروپا در جام جهانی 2026: 5 برد یا صعود تیمهای آمریکای جنوبی. 1برد تیمهای اروپایی. فوتبال اروپا این دوره بد ریده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/24677" target="_blank">📅 15:56 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24676">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LUDTzOf3jhg5g3q8R3rxF-ssYHIx9VOswn3pIVdAIuxz2jxqBOi3LDIVulByD7ocmayMR_91oXhLwPp6XEzQiFEiuepZMnFkRu3cO164q7CP1PHxL9i6S3xWmGEjURVXXpWS6V5TOg_4Du85qkdP5-27OJjHl3MvdXs_i-ve11ZWeKg4m8-SVmNENFHBC93jHxmLzXSHys__Fj1jqnbOUbt1CpWURItMWKJRlCHn7kgJwlk58AUJkuZCV9lIi1E-Z6N8w9eph3bCouFedim-rJmEEI6OdF3v7oyY8XtiW8bWQX_L6zQXKyPXnKqhMWhxE4AAq5OM6jpc5LIhUVxwtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#اختصاصی_پرشیانا #فوری؛باشگاه تراکتور به‌ سید حسین حسینی اعلام کرده مدیر برنامه هایش روتغییر بدهد با او قراردادی 3 ساله امضا خواهد کرد. پرشورها قصد دارند در صورتیکه علیرضا بیرانوند در این تیم نماند با گلر سابق استقلال قرارداد امضا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/24676" target="_blank">📅 15:22 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24675">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/puuMnT651eBumwg8P0YZTgPhz08vvocvaMXhZBOO9V5TVbuBG9hbSu49f5Xhdg1JW9X2QHTnTY7YH9cNr7_jOBlRWDdXJDFBWSARr9FXUxzg0tnNAsuDDkPJx11-TsG1Pe6U4QjjLDfTH7ZzWCPc8DfOdJ_gMuMHZLOWPhWazMZoPz_Du9n8MelZ85k7i1YsQsW7unx_8z8Od1w82n3ne-9EOuGYUm94KWUx1_komVvPa8QsAEOLeaKGcVX5_Vo4OaMHpQMZIScyCKiMbZ3N64HHqTgMHnCMCewj6ZVeZRWRKdptm7gmKBuW0ydtUnu0eaICep-FiqrTZXrUhpwNqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌شانزدهم نهایی جام‌جهانی؛  حذف تلخ و زود هنگام لاله‌ های‌ نارنجی‌ برابر یاران اشرف حکیمی در مراکش در ضربات پنالتی؛ مراکش در دیداری سخت و نفس گیر راهی مرحله بعدی رقابت‌های جام شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/24675" target="_blank">📅 14:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24674">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C3q6OzGUzSlNro-M3Y0YX7uVSw_7a10aSQMMGjox2ba3jIevT4_d4W68QfYEZJIU9I6N0epQbis5UMMbQH5490YbfcRhTgu3kEeYnIbn07lQxwe1DFvg4LhbHaQEKFWekk3mUpmAVFVo1ys8ONZYZGP_t45BGN9_b30oMVHjWuVWlPfAE7p5c4Gs7AmUT1Dwh4168ExVotc3Hd_0TIqpWmCVQPaHY7X--eZzWAJrsUGH_YkbaHwi6tJOgASXgwLxzk3IWjlVHOneGgMbCpg5B0POZG11LLrQw5vsZj6d32xCdMNTHnORx79xgOQO-RoPJsL_1RmKdoKUTO85NCJSug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باشگاه تراکتور در روزهای گذشته علاوه بر تمدید قرار داد دانیال اسماعیلی‌ فر؛ قرارداد خلیل زاده به مدت یک‌ فصل و قرار داد محمد نادری رو به مدت دو فصل با پرشورها تمدید کرده‌است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/24674" target="_blank">📅 14:12 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24673">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iv2ZM5YxtQuOAz9lQ438wWywnISJalMEfPkCnm7zp0JWcgNvDf7OHQjTeGoivchHGSkKeipoV7B9mkiQMdJDyl2lruWmbL4qGUnowOMRQV0UMOnX-328RGCzRwVH307kmsy3_XtcOzjV6QTxO0JwBzG9wOoCY1wtc-ayadRQssqvGI3IAu4veXeyN_r4gIcvrM7Ms2fHStMovqAerZq53LiKLxJZa3tUfuwwYL3ou9ePCIh5oI8nkfAe6PmGwgk6G5vnj-2XghdKiVOmpFMa39Dn_kBGMFs1qA5Jens3A7jE2GWNGn2u0BGT-d8zsFceWiVnHEj9fWSLpFwk9BE1rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌استقلال باید مبلغ 150 هزار دلار نیز به حساب جوئل کوجو بابت فسخ قراردادش واریز کنه تا پرونده این بازیکن به فیفا کشیده نشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/24673" target="_blank">📅 14:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24672">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82624c7740.mp4?token=NrX6H9rFhTJsuenC70BcCu7oXekcPyjoLis8FjiG8cV8-NgiW7hBfmafB4CIauKOHgmGMOAb4mAUyT-8BVeIvrlNgyANcv7Yd2Sw3rTpmBQ9X-yQdvKd8UfmeudyTWFvJqzGbdwrViSqzZN75Sza5IANBZJji7g9YBAvY0eUJNg54n4Pn8iGkldU3BEUcJ57qJqSLRnIacgIcRaNoDXbApzp5wFnMXSAYnhBaB03fL3Ph8Zy1vo3vFfGSUaEnkdyLgXqq3g3kuWs26qT9PoH-i7XBzABQMJBpsPbxxgHNKtcJliFh9_dF2vOixcoCPJqhMPvF0QpuSwwF-N_liL0nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82624c7740.mp4?token=NrX6H9rFhTJsuenC70BcCu7oXekcPyjoLis8FjiG8cV8-NgiW7hBfmafB4CIauKOHgmGMOAb4mAUyT-8BVeIvrlNgyANcv7Yd2Sw3rTpmBQ9X-yQdvKd8UfmeudyTWFvJqzGbdwrViSqzZN75Sza5IANBZJji7g9YBAvY0eUJNg54n4Pn8iGkldU3BEUcJ57qJqSLRnIacgIcRaNoDXbApzp5wFnMXSAYnhBaB03fL3Ph8Zy1vo3vFfGSUaEnkdyLgXqq3g3kuWs26qT9PoH-i7XBzABQMJBpsPbxxgHNKtcJliFh9_dF2vOixcoCPJqhMPvF0QpuSwwF-N_liL0nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
میثاقی ژاپنی که بعنوان بهترین تیم اسیا اونم نه مقابل هرتیمی مثل‌نیوزیلند و مصر، بلکه مقابل برزیل پرافتخار ترین تیم جام‌ جهانی حذف شد رو مسخره میکنه؛ جوری میگه منتظر 2050 باشین اینا میخوان قهرمان‌جهان‌بشن انگارخودمون‌خیلی‌وضعمون خوبه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/24672" target="_blank">📅 13:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24671">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YIsSCb36fo1rgDf4ULgwT7hV4OCP9uZUbmEekk5zyjMTqg87l9vwJBR3ODS8IhvkauRUzEKOzwreCBEmTLJFrgMTiOizP7yGXFcA8HlWgDm63r2NhStFbyx4WYBnv1GeGN7iz2CuZnOGLXmjC8GOMs5F7KKx1SSFoWQDEZV5uz-NcNLfkhPCO-vJHFQ2aFM7r_GAbqdizs0FPXF3olfgKtIUZ8-RsA4_fHatN5VSZQJ5l7zvEBrMppA_ooHiC3T--9A4zdhaAW0_nxWdVzkgMo0tVDqpU3wLIeDMIRxatUwgXQo5plzB0ipKXg5kW-Giyoxfy0DLT9rEkEbj2L9gYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه‌تنهابازی‌مهم‌امروز؛ گذر شاگردان آنجلوتی از سد سامورایی‌ها با گل نجات‌بخش مارتینلی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/24671" target="_blank">📅 13:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24670">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s9NghSB-ZbuC9C7zw_w6IGC9SgwsVMDlnxkdWKBocn5TdXHJH1FYcWlphk-LyPhdmt86RmVEiIwZnqkItgT1-a85o4IlDoe4qWcJbwr_FZEv1AS9c8bJ3Tr_owsr3kceyCc1e0N3i6JiJGOYNhIBEe-kmhqICWYpl2nNJnSxktfjieaUGIxVOY5dnVNmNkmsJD0YAtCqn3sPgRlgCDXXxUPQ1Z_4LuY-7VQxRmVkyClshz09j6UesJSh3n_5tcWsFqnIEhBL_QY65sCu6PWjgadvQkiz91SmzNbGxQfR6Qa4KbpvdDdI1c-JAHo3GKEfJ9k99uEKnVFGngyFnR83Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌های رسانه پرشیانا؛ درصورتیکه اتفاق غیرمنتظره‌ای‌رخ‌ندهد و اوضاع‌کشور آروم باشه منیر الحدادی و یاسر آسانی هفته‌اول تیرماه به تهران خواهند آمد و به تمرینات آبی پوشان اضافه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/24670" target="_blank">📅 12:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24669">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68e8477068.mp4?token=DHgfEELECk7ChhVVXy79hq4xWajwFZ7sM8iHTLigkuRr5hEXx1ylAHbivVgWFclcm_Y9hm6f375-pme2VetvYiSGjZGxh81p4-_HzylwBg3WH9b1759LOFc4j39ESScHCZGjd1IltXVB_fM4NsLNBR-OP6__WgsZDWTtta25wpGmRh_hZVDbPnKlV8LI22mINmfDsP6jldLXMruuUpJupgcdlesgoRYqrYc4sc8rBJpghE6CiB1H_AQRSoJi7fL80fMLkbExurKZPBWLQs0O-xK9BJFCMGmRemfTVEnhj5UInyuS4-iT9kbuznMxfji9p-LlEwZC2RxdeU_jDOLA1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68e8477068.mp4?token=DHgfEELECk7ChhVVXy79hq4xWajwFZ7sM8iHTLigkuRr5hEXx1ylAHbivVgWFclcm_Y9hm6f375-pme2VetvYiSGjZGxh81p4-_HzylwBg3WH9b1759LOFc4j39ESScHCZGjd1IltXVB_fM4NsLNBR-OP6__WgsZDWTtta25wpGmRh_hZVDbPnKlV8LI22mINmfDsP6jldLXMruuUpJupgcdlesgoRYqrYc4sc8rBJpghE6CiB1H_AQRSoJi7fL80fMLkbExurKZPBWLQs0O-xK9BJFCMGmRemfTVEnhj5UInyuS4-iT9kbuznMxfji9p-LlEwZC2RxdeU_jDOLA1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
یان سومر دروازه‌بان37ساله سوئیسی‌ تیم اینتر میلان بعد از چند فصل حضور در این تیم جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/24669" target="_blank">📅 12:00 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24668">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/786ffe7041.mp4?token=SaAmdpnyePTkoeLHVLVWHhc3h7qYHrQlXW6liKZphiy0MJWCWWtiOXfQ_37vUDlANRzH7Y2PUcAj6dpy3KdhK6AkqSgUC_abEVrDzcg7mgduwbtvJ-v76C0-p_lGkGPUKIOxsESo9t8p403wgXBfPapS_cCJTT7ncD6bx_Jbi8rRj5Sv0UKg1QGQ-8ATdg1ztC9K_jcwzvJhyobkOfTYFBdmE2_80AVFxp5oOypGg7vTZRsKsbDmywj4egecPPKxiYiP2oHfV-XjkPKr5IsXgbOvnHdKopUVZxtS7j38htUkxch0kUvOHsTA6d9o3RNKI097J5kwpaARRBZ-nqq6uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/786ffe7041.mp4?token=SaAmdpnyePTkoeLHVLVWHhc3h7qYHrQlXW6liKZphiy0MJWCWWtiOXfQ_37vUDlANRzH7Y2PUcAj6dpy3KdhK6AkqSgUC_abEVrDzcg7mgduwbtvJ-v76C0-p_lGkGPUKIOxsESo9t8p403wgXBfPapS_cCJTT7ncD6bx_Jbi8rRj5Sv0UKg1QGQ-8ATdg1ztC9K_jcwzvJhyobkOfTYFBdmE2_80AVFxp5oOypGg7vTZRsKsbDmywj4egecPPKxiYiP2oHfV-XjkPKr5IsXgbOvnHdKopUVZxtS7j38htUkxch0kUvOHsTA6d9o3RNKI097J5kwpaARRBZ-nqq6uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇦🇷
جادوگر غنایی درگفتگو با ESPN گفته شک ندارم که آرژانتین باتموم‌ ستاره‌هاش مقابل کیپ ورد غافل‌گیرمیشه و خیلی‌زود از جام 2026 کنار میره!
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/24668" target="_blank">📅 11:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24667">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d5676f715.mp4?token=nnuYxKHSQa9MSPdOhabi8Judun9mvJtOX2oI0oD8WtPBCi-dyd8R1xgfMDFzlOdwz68LYnkouIgbTbfzFxYmMRdp-qjAYDcomYphDqxSovNOcsNMamk3Tvr0adNp8U9wDfsh-Ea6Veoys7aEh1ZFLe6WwH1Ww3eDxRkglSWjXDtnCMfsuKzwuCiy9Nd5a10EjrydQUw2SnqN-Zke5Sp7F7HD9po6ZTaPbKLyzrTSpeE8OMilABjT1E0pTqgVTqRsxDvdRbYfl2mMWow-dN5gKKFaj03WdAizSyKGWX9WpNOj6x_u1EqmEmdHz-rmgdh5S2gWgHWCYimEniCf5X1SyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d5676f715.mp4?token=nnuYxKHSQa9MSPdOhabi8Judun9mvJtOX2oI0oD8WtPBCi-dyd8R1xgfMDFzlOdwz68LYnkouIgbTbfzFxYmMRdp-qjAYDcomYphDqxSovNOcsNMamk3Tvr0adNp8U9wDfsh-Ea6Veoys7aEh1ZFLe6WwH1Ww3eDxRkglSWjXDtnCMfsuKzwuCiy9Nd5a10EjrydQUw2SnqN-Zke5Sp7F7HD9po6ZTaPbKLyzrTSpeE8OMilABjT1E0pTqgVTqRsxDvdRbYfl2mMWow-dN5gKKFaj03WdAizSyKGWX9WpNOj6x_u1EqmEmdHz-rmgdh5S2gWgHWCYimEniCf5X1SyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صداگذاری‌باورنکردنی جوادخیابانی مجری ویژه برنامه جام جهانی روی آرناتوویچ و خداداد عزیزی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/24667" target="_blank">📅 11:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24666">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F5FtgdS-1zZbhiBfopeVm9wiSqURSBWC3uesYd9VzH2-vCvFUOEj_RSXIyFeVgmcH8UxhlLTO8eygVzYWdXWciXgG9C1zICczZxiy580mH-Jx2R371CEgcvItBmBDn2Mnf5W6gN1DUXNeuAfG2OL2fEr9RV_LZkvfrQ0SskYFcRYcy420tE8rGYRXclmH72aIZSpIZ8xwh-hLQIhr6ueY9AS0nn8IOSS7BPBXQUAgnfwoiL5N2TcKXbaI-MBJa9HROoPe2T0XIo7Y48Dc2wZ4nBFy0tgJfTSmgoIXL5glPMvmSzBLpb2j44EB7IcbJEBiLGpUJCVV5vltIc6_0gsAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌شنیده‌های‌رسانه‌پرشیانا؛
به احتمال فراوان باشگاه استاندارد لیژ قرارداد دنیس اکرت مهاجم 28 ساله خود را فسخ خواهد کرد و این مهاجم ایرانی الاصل احتمالا به لیگ برتر ایران خواهد آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/24666" target="_blank">📅 11:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24665">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IwHzCtYDTsxMlKTFF2SjdE-fxPTJKswEzh-AeIT93PL0_Mn56_9N6Hon3DgSM5tU0l_2WLjZXhMrfnbv74JZy-qW6Kut-z7yuDcQ8hcrv21gRhLPBoHt-r7MGR0jTlmIe4fYK6Dp8_VwV6n0irii0EvJ44iDNkg3HdMvuByql-9zXPjps-jDukpuKHE9TcY6y1hR6VDw3Yo0iE9CfZ1SiRQ7ap6JYsrP5HHiwpcZL5lXppY-FwGlPJAINGzJw9Xdl8kX4XlSdjBHdBDJwhY8UMGF8EQ3yheNfXgxu2p9SX9mBPvytPCo1vFwr-BLw-30_LgNzqcXvf8iMSeOB04evg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک شانزدهم نهایی جام جهانی 2026؛ صعود ارزشمند و شیرین کانادا به یک‌هشتم نهایی رقابت‌ها باپیروزی دیر هنگام و سخت مقابل آفریقای جنوبی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24665" target="_blank">📅 11:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24664">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RWch-bWR2vkPMsQ67_RvsiK0Bbpo1ExGMDcwXhUoG7I7V9RKmgZk9szqb6dNtE3nSvwe4tIdkKPWnow0VoBvjs6wEDPH195aIpvLTDldXl1_dT-EiPxgNjTxvVW_1AxOWwFmS5f-2a_PB1EqFypFsjr5TzgPAVPFZlB3qTU7QbobcoCP1NH7bDI-glw9z9wxWTheFvXjj6oDhDC4PKyFABbCCkzuIJCFMqWI9OJiyn3adzqWJzo0FxdXNrhDT8Y04B8neBQQ_RViPvge2UkeoK_fbqrvqCvRuIPqzDox2UODDA5z4uBBYQC75_88HH_U1SdCBOq-sRm2eFmQTNkq1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
از هر واریز
🤩
🤩
درصد شارژ اضافه خالص هدیه بگیر بدون قیدو شرط!
😮
تنها سایتی که
به ازای هر 1,000,000 تومان واریزبهتون1,200,000تومان شارژ میده
اینجاس
👈
این یک هدیه کاملا نقدی است!
✔️
هرچی شارژ کنی
0️⃣
2️⃣
🔤
موجودی خالص میگیری
👇
🔴
اگر هم باخت بدی همون لحظه
🤩
🤩
درصد  مبلغ باخت به حسابت برمیگرده.
⌛
پشتیبانی 24 ساعته
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان r9
@betinjabet</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/24664" target="_blank">📅 11:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24663">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CUlEetODGC81pwytzS52J5IPQR9mrOGdMdst3Vi90fbAj4kS5SvETBgUFHh_kVH0xHiXp69IV_ttNM7sBffoIR0TrSN22EJJ1WsC7TvaJFhP9NYKmPpXcssA8dJiHM7Yaa9L3AxYzL04dh_S7IZJhqFtBs-Ah7U4ntFt2icU-yX9-8r2SZglhjc1Ua8oYW8rdML4LnJUoSH693eb8VTi2Rbq2fO3f0B0wx0HMCoQT3gg2HiemzbQYer1fZreEUi9UCmwgQCLpytR--TyKKqTVpG0y43vESFlx4pEWvi2RYobcpDEz-rUQ2yZg9zjhaIjHs7rLNeca9WcZpfwlqYMkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ باشگاه پرسپولیس درتلاشه امروز برای دراگان اسکوچیچ بلیط‌تهیه‌کنه و این سرمربی کروات ظرف 48 ساعت‌آینده با دستیارانش وارد تهران شود.
‼️
بعد از رونمایی‌ از سنگ‌ اندازی این مدت بازیکن کهنه‌کارباندباز سرخپوشان‌پایتخت خواهیم گفت. این بازیکن از وقتی فهمید…</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/24663" target="_blank">📅 10:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24661">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/572d6647db.mp4?token=N5Ub3d5Cjanm7_9hjiBS2hPw5Yk6GvHMGSgTaiEQFfi8KYgt93ra3qSn-iOTtaPqdWqrfExcd78Udo8bBB1S67M24ORes2e-kytZZiYzxiOFp-8-AlvAaq9doIRy7YgpE7VSf_8hFKgFqnutJP85ZyrEksjSore6rJXvbFm_bzgWwthgVcJ7SkCeVMQfnc6KbkjleV6piWKKUBGbCYGJYVwfrfh4LC-hSVFkvSamSEDk3Oam1Byeuq2m0qVmr0Qvx5azoQUcf8uY8g6j293Nnv5Hk3V0Kb4YG4-aDdftk6TrgVOhZu5Bf_oCJUSbliA0GEF_kcHGH8CL1t3vnNYO_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/572d6647db.mp4?token=N5Ub3d5Cjanm7_9hjiBS2hPw5Yk6GvHMGSgTaiEQFfi8KYgt93ra3qSn-iOTtaPqdWqrfExcd78Udo8bBB1S67M24ORes2e-kytZZiYzxiOFp-8-AlvAaq9doIRy7YgpE7VSf_8hFKgFqnutJP85ZyrEksjSore6rJXvbFm_bzgWwthgVcJ7SkCeVMQfnc6KbkjleV6piWKKUBGbCYGJYVwfrfh4LC-hSVFkvSamSEDk3Oam1Byeuq2m0qVmr0Qvx5azoQUcf8uY8g6j293Nnv5Hk3V0Kb4YG4-aDdftk6TrgVOhZu5Bf_oCJUSbliA0GEF_kcHGH8CL1t3vnNYO_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
صحبت‌ها و عذرخواهی هاجیمه موریاسو پس از حذف ژاپن مقابل برزیل بدون بهونه اوردن و گیر دادن به زمین و زمان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/24661" target="_blank">📅 09:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24660">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vU1jTTmefvJJBxe4JK7Zg3vtmL6O9MDgA8mL87m0P_dXYf4oXnLffBEnqyi2g6VKdbBVnop8Mjj_i3wdyVR_ZBGAs1Ei9fz95oEW34CE1BwdhKfEyvpNLNqONJS2SSeOYfxelc4FeSk-hvCh2_YQaTwVAoS4t2_DpLbVMKnBJOfsfvLPdYUvqP8pDqOZ1vOEA-sPFw3HvmjNqIrOGmEEq4HmUHQ3E9_SQVSyWfAGRiDHeDpGgHhOepD9f1kn91X7_NUJHQaVQDxzSqRdu4rnm8IHVJK7EdHg-ocIKbt5HBwbsD9D4YmJKWj8JHZoaQZCslZPUh1LP2lR7QUKlkkDmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
سه‌فینال‌آینده‌جام‌جهانی فوتبال در این ورزشگاه ها برگزار خواهد شد؛ کدام ورزشگاه باشکوه‌تره؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/24660" target="_blank">📅 09:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24659">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">✅
یک‌شانزدهم نهایی جام‌جهانی؛  حذف تلخ و زود هنگام لاله‌ های‌ نارنجی‌ برابر یاران اشرف حکیمی در مراکش در ضربات پنالتی؛ مراکش در دیداری سخت و نفس گیر راهی مرحله بعدی رقابت‌های جام شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/24659" target="_blank">📅 08:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24658">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vlJCN2ocKfhdfW9EPAfrvjZZ5TdFEW_vvuOoKlGizRCSqJGqQ5YHrXp-dKpO08eqpdH9lpjnbFY6_-ceIhz-o4NZW3vAgcEoBN1ZoZZz4nnGMbEUzwEiDH2yoQzZMT71fELgYcVPSJ4WrwWV_HXQ9_BJDPiU_cJXqW50YKxJTQbZshF0osMZaidAZfzywHBQMFfqobJAohib1cMJ6UHqffje1oub21C5Dld-kqd23L8jU98xuxsK8NmNjb0N_u3WcluTn76yAawrHZm5-bxfFN8Ao1vvUvlqtXpYl9Rzgtz0ELA0e13wVFXJcC6ZKY8kW5MRrXNZ3RT5qOxKRnC15A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌شانزدهم نهایی جام‌جهانی؛  حذف تلخ و زود هنگام لاله‌ های‌ نارنجی‌ برابر یاران اشرف حکیمی در مراکش در ضربات پنالتی؛ مراکش در دیداری سخت و نفس گیر راهی مرحله بعدی رقابت‌های جام شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/24658" target="_blank">📅 08:43 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24657">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vwIDZDfav5NdbMKfs4aRKOr01PHJkZ99NWARoBfeBo3T40dP57n7ODNeXZxb8mibNUbd0pjS-gF6l5oQpXbRdwPBQFt3kOczuwYKEogtEFrbJOcxTBSF_uDD69Wj2jNFCUNyLFs7685pI2nX2-6pqffF9HG8pr50LSBo4qXsMWeypr5McWfSYQt_i-8iXx7HO8-EEENOk7EyokHtGV3ZNTft35QOYMBI9p6EWYzwFGbYW596ABidOcRm0Pf2K3cRCLNRwnTZ_66m_Zs2dUZRVScxc8pVkg1sOMDM_3HhvdY1DSgxE4LXZptIVLk46yQmwJ-LkSWGkT12Zgt4Yj_H2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله حذفی جام جهانی بعد از صعود برزیل و پاراگوئه به مرحله یک هشتم نهایی جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/24657" target="_blank">📅 08:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24656">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56f71a194a.mp4?token=v7RqjOxzervAeWLnt9eUD-PS_cE_dmDTD3KdlRC2R4ma5Cduv5QKBtKeuEfR_L3DaExluuCPYswXCBjU3BrRB874nlBpwoePb0XMtj0XC_TVMxCwbXlZ-49WUTXAuUNgeScTGOjkPikP4UGKtGBP-Evb1HwvBU3U5xMOYHzT2M6c0Lo-kxEGExzuiemGZY4dxVbRElMMWJUeC1gGk1eCXerwyed1Y-X6L-fJeblDdsjLWGh45nvn2gCS0q_jMru-vgoHXBp0IWIxdnZy_AfofX49-9uUZNLnj_jvKQJIIM6bvG9YYTf7yZcdkHnORLEThZtQ46ddWq_QnWL_hY3V80-ksxhapjgFi_bRtX4pPiVip2AlFVubDVnJ1qojztFTfLLtf1-yazSPjzoikz3KkOaNNqigzHT1OhP6LtWVxxq7GGW3KEdh-k-e8C5262tgGtWtEEm3stMvOWTe7363XV8HlVGuqez8B9Sur5LaFREWt8ABJVZ2lo5jrIosrQRxFrDKDtb_YGx3WdBvRKx-3VefkUuy4p67Vpi4MqmzFlDjRxt79lc6OwwkXuD71KmSwbLBby3ziYFCfNoZsfCIEPFIPA8yTZ4Xr2QQZ4W8uDXEBvr4h83YvSC6AOY29HvXA5ACAKwuiyuUeOp1QpX_49pUrdxhQeBVvLQhgRAjxLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56f71a194a.mp4?token=v7RqjOxzervAeWLnt9eUD-PS_cE_dmDTD3KdlRC2R4ma5Cduv5QKBtKeuEfR_L3DaExluuCPYswXCBjU3BrRB874nlBpwoePb0XMtj0XC_TVMxCwbXlZ-49WUTXAuUNgeScTGOjkPikP4UGKtGBP-Evb1HwvBU3U5xMOYHzT2M6c0Lo-kxEGExzuiemGZY4dxVbRElMMWJUeC1gGk1eCXerwyed1Y-X6L-fJeblDdsjLWGh45nvn2gCS0q_jMru-vgoHXBp0IWIxdnZy_AfofX49-9uUZNLnj_jvKQJIIM6bvG9YYTf7yZcdkHnORLEThZtQ46ddWq_QnWL_hY3V80-ksxhapjgFi_bRtX4pPiVip2AlFVubDVnJ1qojztFTfLLtf1-yazSPjzoikz3KkOaNNqigzHT1OhP6LtWVxxq7GGW3KEdh-k-e8C5262tgGtWtEEm3stMvOWTe7363XV8HlVGuqez8B9Sur5LaFREWt8ABJVZ2lo5jrIosrQRxFrDKDtb_YGx3WdBvRKx-3VefkUuy4p67Vpi4MqmzFlDjRxt79lc6OwwkXuD71KmSwbLBby3ziYFCfNoZsfCIEPFIPA8yTZ4Xr2QQZ4W8uDXEBvr4h83YvSC6AOY29HvXA5ACAKwuiyuUeOp1QpX_49pUrdxhQeBVvLQhgRAjxLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک‌شانزدهم‌نهایی‌جام‌جهانی؛‌شگفتی کامل شد؛ صعود تاریخی پاراگوئه به‌یک‌هشتم‌نهایی جام جهانی باپیروزی ارزشمند مقابل ژرمن‌ها در ضربات پنالتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/24656" target="_blank">📅 03:41 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24655">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b14530aa1d.mp4?token=gA2e5mo5U4pjl1MFlgzG7l1PLZNowkL6sZYmCA6cpWyI3y_X9mP3ULzZ6Mytb8EbKFx6RaEfSlM-7UXtiPrGLW2Qkg2i0v14vl9Klk0mGR0jwFqn2DBCOmUnHEREOTGP2byibZoMVs9rkCVtMHJMjvetfTj9s6J3fZzOkjgTea-6M371_xhkeWXNuB2sxemisFGUs_FJNRVb6c-0BHhv82hqUxZuA4iv427JHmqssHX2TSlKcu51fWZoT_No4mTEfL3sUoKGcbNXlJzVm0t0U6fNozAXOuIPT02xJ5TYzBUPY44prJnI0OK02InN3MUNsRLYTmzSWA3A1Wzfuvde6pe_HlzoOATaswO5nFLYP1235cXSpGFz3SiCYG5LEn6j04Dd3DYQNxL6kGg1VM2FYntacoJQJhRRj84QqdEkHei7IkdVg2XzQVrzXG-NtgLx_QSlh6T-fgPDyqvqSQ3PINFUAcKP-CnQ7ys4tUa2gCOaPbhlnJ5MkL6L-XHi9a2GbXKGBaw5UM-_h0ilheDccWi0AZNYFVdSCmW266mtxPXTw88k3MxGpo8Yl1I4UjbXaLU0KaBPYxeoqxaV2FpM2aqvcSEHoePeTDM8uQqP3JTuv-HfRCMxe80CFEl1ztx9B3uO7vcarT2o6lbFaslRdnTOST55mBFVYlF1bX7BJh0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b14530aa1d.mp4?token=gA2e5mo5U4pjl1MFlgzG7l1PLZNowkL6sZYmCA6cpWyI3y_X9mP3ULzZ6Mytb8EbKFx6RaEfSlM-7UXtiPrGLW2Qkg2i0v14vl9Klk0mGR0jwFqn2DBCOmUnHEREOTGP2byibZoMVs9rkCVtMHJMjvetfTj9s6J3fZzOkjgTea-6M371_xhkeWXNuB2sxemisFGUs_FJNRVb6c-0BHhv82hqUxZuA4iv427JHmqssHX2TSlKcu51fWZoT_No4mTEfL3sUoKGcbNXlJzVm0t0U6fNozAXOuIPT02xJ5TYzBUPY44prJnI0OK02InN3MUNsRLYTmzSWA3A1Wzfuvde6pe_HlzoOATaswO5nFLYP1235cXSpGFz3SiCYG5LEn6j04Dd3DYQNxL6kGg1VM2FYntacoJQJhRRj84QqdEkHei7IkdVg2XzQVrzXG-NtgLx_QSlh6T-fgPDyqvqSQ3PINFUAcKP-CnQ7ys4tUa2gCOaPbhlnJ5MkL6L-XHi9a2GbXKGBaw5UM-_h0ilheDccWi0AZNYFVdSCmW266mtxPXTw88k3MxGpo8Yl1I4UjbXaLU0KaBPYxeoqxaV2FpM2aqvcSEHoePeTDM8uQqP3JTuv-HfRCMxe80CFEl1ztx9B3uO7vcarT2o6lbFaslRdnTOST55mBFVYlF1bX7BJh0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک‌شانزدهم‌نهایی‌جام‌جهانی؛‌شگفتی کامل شد؛ صعود تاریخی پاراگوئه به‌یک‌هشتم‌نهایی جام جهانی باپیروزی ارزشمند مقابل ژرمن‌ها در ضربات پنالتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/24655" target="_blank">📅 03:39 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24654">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VTlBOs71pAm3-n7teXDENKk6kIVBpQsEI0QWLT_3P30VXPWa63rkL2D5pkJF9ZoVK608iOyqeiqzZgstVD0K0iXgx02RFsna5VZMgVdR5cF3h9TZeM3zm3TFU-ZoZmSK9qdAq3h32M3kJJolQJsk6VU8iVfiJOV7nB_TFFhHYzaA2bEZ3BLCbhoySlIMQUEp9lPdGqY7nLUpJL0SNzVeYlEJITnd7elaYfGMn3Xzr9KKT3S0aMwNmiUltT58GAlVXS1RXxvDXXzthoPpp448qW7Wes_eJQiF-sep9mET6BbnmiacCNGhvHLYHGioXn1cUgBqEx-dkGM5970W4gUKrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌شانزدهم‌نهایی‌جام‌جهانی؛‌شگفتی کامل شد؛ صعود تاریخی پاراگوئه به‌یک‌هشتم‌نهایی جام جهانی باپیروزی ارزشمند مقابل ژرمن‌ها در ضربات پنالتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/24654" target="_blank">📅 03:31 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24653">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef2bb58ba6.mp4?token=lvhx23D6_QOC0ANyeNH2YaIKBhuApeAW_wPfZikWkoUBOjFMbyagJfILWm96a7rcta1MhVul55yQ_mUp4e3EengQyH8w3SBwufwuxkB-Bqbpz3CHqgjTQ1gG0yT0XYPnfCYm9-qTPQ0Zaia2ctmOs1D0pBJk3cv_HkrpeAlp7bw5obvzn8XnVe3mwC_uXj5qGtzNOlpaWr9_Yr5zFp2glA0a9UUSYGmOuiasPbzoT_oHcQZ4kd3QhEh2xEcWXElTKNs3SiZJ3BtsUKeO6FKPW9k7hFOHzw_CRukVxOrxIs65Yr1bU44IuxHwPPJw2C1q3AtJLFlSSeGqpplZA0teSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef2bb58ba6.mp4?token=lvhx23D6_QOC0ANyeNH2YaIKBhuApeAW_wPfZikWkoUBOjFMbyagJfILWm96a7rcta1MhVul55yQ_mUp4e3EengQyH8w3SBwufwuxkB-Bqbpz3CHqgjTQ1gG0yT0XYPnfCYm9-qTPQ0Zaia2ctmOs1D0pBJk3cv_HkrpeAlp7bw5obvzn8XnVe3mwC_uXj5qGtzNOlpaWr9_Yr5zFp2glA0a9UUSYGmOuiasPbzoT_oHcQZ4kd3QhEh2xEcWXElTKNs3SiZJ3BtsUKeO6FKPW9k7hFOHzw_CRukVxOrxIs65Yr1bU44IuxHwPPJw2C1q3AtJLFlSSeGqpplZA0teSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هالک‌ایرانی‌درگفتگوباابوطالب‌حسینی:
شمشیر خوردم و مانع کشته شدن یه بنده خدایی شدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/24653" target="_blank">📅 03:19 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24652">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SYIrSVHlBUXH7PFHBlqnPMq21BhBYs35SVIX592uuC71CuR18weUPBpzwDnCVxnemOi3OgNUygwywr68P9sgiLhIKmrZV3y4pzFk3xaeqK4SD7FNteTO6edJfFjsTcGMwvCZQ950v1IpC1F4FgImVaeVe_gryva6tm0zzX5uSv8wjDztul-Ifyy4bpBDJMaF-4Ysi8CPoMOs6-NCzd6854cnH6Bni6xg570zjcKiYvZdKQcjvOuDFyP8GCF0RJulTovwh8E7X6jkSp2-FgOiXl5rH_hJUlETITxGGvQJ12R5sUsqbOWPb_gSZXoYvD8iuhrKcccS7N17o4DGihM7Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌شانزدهم‌نهایی‌جام‌جهانی؛‌شگفتی کامل شد؛ صعود تاریخی پاراگوئه به‌یک‌هشتم‌نهایی جام جهانی باپیروزی ارزشمند مقابل ژرمن‌ها در ضربات پنالتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/24652" target="_blank">📅 03:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24651">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mn31PyNhy2HTfir_1QKXBWP33KXdvQzHR6NDjzGxu1rvyx8jOOI1AFK5XfYIjAZ4iHuhUe2SJkcYzL2FTsAQYGgp1CL6yxBOlJG2jIlHGUo20AoPBkkwn-zVjwbHchnp-liRalkhbeJv7-qcmoKdik9InHJJzPpFM9QlUZ6LnKR3Y6q3Ktk8aC5MX-xkpNJqG7N9JkAepAEmjLwBNAMwdlxdc0llcJ5ckBkGCtqJeFCwR-sulIYh_RldYUtx9spwDd1xyUuOB1u-iSrJPAURQEfycdZCUTjP5RkswSnS5eouSMthlb40JIoxDiBm8zNEWZWZ1W4Xq9_IzgLF3SwnLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آلمان‌امشب‌از پاراگوئه‌گل‌خورد؛ آخرین کلین‌شیت نویر و آلمان توجام‌جهانی‌برمیگرده به فینال 2014:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/24651" target="_blank">📅 02:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24650">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8d0fcfa32.mp4?token=GcApVIcE0OmaMUNubbi-xf3MfEPdlPcojaCQUY4ZaJExOnz3IAP1NwiDAJwwdfK_VUzK_StsxutZ1r2-aVrh9Hx0tsbtrR9N_nHgPd6xaz0joj3FwR8vHGMT2kRJZq-jAK5Iay58s77ucNRUuaHbl05wZ-hdVhkh1PUVnBwle9PhhT1bFTsyZ0C2c3aHRFu-HvvN5TxpuSklwbocTkQIAJzG_xOAFfwbW4BYnLzYZgcM7eXV-C0AVY00DEm0sxWctEMUOUrM_CoBWhnRNGzGXc-zrr2AncI4VFrJc9aoo9I5DaP2s_rkHaNr2wGsFiVsiTR6vYbGgyYpsWhKC19QTwaYitaVGajm8Ht94_WX3m6JQ0EEyb7_rmTi7YM-joBvVvvYQOsPrwPeoH8dOwIfPPaHHOt6mqzo7UoK3dRkkIZUpZyLpe91s2n0cESbmaJjfBvTAsJnFSHicih84be1ECZlzTdWBZ9170XAgf7RhvFBsDVewcagTs5WlHVfwOiPKcvritdzb3EiZ474aadAJiTpDEz2wfbCCpmIcH098kI0Zz5HgMsW6qm8-sVTXKv1Wft53ZNExAI5GQJ_3OiC8k-pKQ5BwOUmcVh-lJXxui6FH8YrF9LUdbVZhwCs-YAZTkgKHpl7ggVeBoFFJ_oGO9KVomtwF1of8-oq0uQip3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8d0fcfa32.mp4?token=GcApVIcE0OmaMUNubbi-xf3MfEPdlPcojaCQUY4ZaJExOnz3IAP1NwiDAJwwdfK_VUzK_StsxutZ1r2-aVrh9Hx0tsbtrR9N_nHgPd6xaz0joj3FwR8vHGMT2kRJZq-jAK5Iay58s77ucNRUuaHbl05wZ-hdVhkh1PUVnBwle9PhhT1bFTsyZ0C2c3aHRFu-HvvN5TxpuSklwbocTkQIAJzG_xOAFfwbW4BYnLzYZgcM7eXV-C0AVY00DEm0sxWctEMUOUrM_CoBWhnRNGzGXc-zrr2AncI4VFrJc9aoo9I5DaP2s_rkHaNr2wGsFiVsiTR6vYbGgyYpsWhKC19QTwaYitaVGajm8Ht94_WX3m6JQ0EEyb7_rmTi7YM-joBvVvvYQOsPrwPeoH8dOwIfPPaHHOt6mqzo7UoK3dRkkIZUpZyLpe91s2n0cESbmaJjfBvTAsJnFSHicih84be1ECZlzTdWBZ9170XAgf7RhvFBsDVewcagTs5WlHVfwOiPKcvritdzb3EiZ474aadAJiTpDEz2wfbCCpmIcH098kI0Zz5HgMsW6qm8-sVTXKv1Wft53ZNExAI5GQJ_3OiC8k-pKQ5BwOUmcVh-lJXxui6FH8YrF9LUdbVZhwCs-YAZTkgKHpl7ggVeBoFFJ_oGO9KVomtwF1of8-oq0uQip3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
👤
صحبت های عادل فردوسی پور در تعریف و تمجیداز رامین‌رضاییان‌ ستاره36ساله فوتبال ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24650" target="_blank">📅 02:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24648">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff3a278b0.mp4?token=GTdxrlJ_7tv0BzNY3uzJh6J1cY3j623jnSvAI1pIquG1iZQOWMZw8F_TYp7Hc7s9LVHi9QtccNy6dEVxcxTBt1_lQH3_p3PQZsD5L4nJEB7QfmuqmzzKJ2Zm-2_x4uxBBsRfyIWNky8VJieMpoVZnLIuEXjFLL31mcyBmmC1Y5PpBkEij-nC4M4rJwuWK4MOQD2_NKDyb5sldzE0q9H-TEtCG72t1sWnNMRF5rsdN6_DVGEmSuN_jMN7wsGA1rW9qOmMv3hvgikc7eyFKFvJij8-0uxQet4qlGmgWlv_X-LDfMPD2-7s0lV13cGkBNidfhQufz5hy1XonoSxLii3ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff3a278b0.mp4?token=GTdxrlJ_7tv0BzNY3uzJh6J1cY3j623jnSvAI1pIquG1iZQOWMZw8F_TYp7Hc7s9LVHi9QtccNy6dEVxcxTBt1_lQH3_p3PQZsD5L4nJEB7QfmuqmzzKJ2Zm-2_x4uxBBsRfyIWNky8VJieMpoVZnLIuEXjFLL31mcyBmmC1Y5PpBkEij-nC4M4rJwuWK4MOQD2_NKDyb5sldzE0q9H-TEtCG72t1sWnNMRF5rsdN6_DVGEmSuN_jMN7wsGA1rW9qOmMv3hvgikc7eyFKFvJij8-0uxQet4qlGmgWlv_X-LDfMPD2-7s0lV13cGkBNidfhQufz5hy1XonoSxLii3ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇽
اینطوری که پیش میره مکزیک سال بعد یه افزایش جمعیت چشم گیر رو خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24648" target="_blank">📅 02:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24647">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IlPLQBnPBWIvqvZvo6EjrrnF1R20ZuAmGaCD5Pp743JMw8HQH3T4vDVlJXgU4ak3K9_WGaWbE45pgpfVh9y1kWYdehyRz0Gj2zUZSYQjL62JEi039SCndLtNuKv9Sn9Qy1ii0yiTLwDtcVJjOMl-eiTiM9VSIwJHlySBjCVP0Dsl8Ny6A4adNA8CMHlW1VLruWtPhr7vYwSecZpjcem_jGYsDb-miKhZ4tiI95t1By1wj5MJeM7s7q8ON1Ir-_NWdUGqh8QgaDxXpEDlYyCFwZ1S9zxA1-J7zE_HsFbYdYrLALlYi5QK8nheJ70z-mkGpJKv1rKeMkw5n-WLzeu24A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
جواد آقایی‌پور مهاجم‌سپاهان:مردم عزیز اگه تو رشت هستید و نیاز به کمک ضروری دارید به من پیام بدید، کاری از دستم بر بیاد براتون انجام میدم‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24647" target="_blank">📅 02:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24646">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‼️
بازیکنان چادرملو به لیدری رضا میرزایی وینگر این‌تیم سرود قهرمانی این تیم تو آسیا رو خوندند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24646" target="_blank">📅 02:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24644">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NxCW82rznTZp97-r6xo8cZk8JRSZwsankWq_t91uMTni_G3aF7HnRudnkVTDr05edEj3AyRMuE41MJsecWQJApNK_CnRG6bvlxlbyCCT1a40hnFBpuOyGixJj5xh-pyHCSfkCemodLOC2AX0tuXp76IAHSKsJl8Tng49eUORkA3i0Bh0OspA4NvAT50SKJMEJk0lmRAIR5zXVuYJ3GAzfwdL2wa5bdmgpiPiP77321LItAyw9JCN5liDSFH9E_OhcCWJ4pXHtNAVrNsv207Qxw5HOI6xFKUAPXjHwJZcEUv1pEdqPxaxdNpj26-wXL217jOzV1c4Yh2WsdMNdzqASA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
#فکت؛ علیرضا بیرانوند تو جام جهانی 2026 :1 کلین شیت نویر تو جام جهانی 2026 :‌ 0 کلین شیت
‼️
تعداد کلین‌شیت درسه‌جام‌جهانی اخیر: بیرانوند دو کلین شیت داشته. مانویل نویر - 0 کلین شیت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/24644" target="_blank">📅 01:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24643">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F3S0zQqIgx3DNh-1m3e5Szb170xFet0z5MVt2pzaEoQd5QklbRJsrEXO2BaXNYywaBnCJinjiV4CLgxIevpMm9W6Xsu0HHpKFUwJDJix7KOM2l51qh-pLe1c-Ca7Y0EuRDlsBOoEvTLdgQWzM50Gkv55q2EkbzAYAAD-JbNl0ceYl_D-9DCUbBmwdXLnmGJRwOagvI9H_qSHoksxjCwO8nTiOzobJYx7QwZ9OdatcPVd_HLgjiVyiMGyHlOOlUNGvwZzr4kaauPYSr3w5JWCbpou-euU6zDkY_CXsod7a6y9T2om3UU-_i6u94hRMV5EoyVIIXPqm0BXXs1EDo1WLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ مهدی تیکدری ستاره فصل قبل گل گهر سیرجان که دوبار تا آستانه عقد قرارداد با دو تیم سپاهان و استقلال پیش رفت درنهایت‌ ساعتی قبل با عقد قراردادی دو ساله رسما به پرسپولیس پیوست‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/24643" target="_blank">📅 00:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24642">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p77BhPA8orKWkQlZAih4IFiXkAvQVl9LmGw9r40Th5DcNY00pRTQNCxnW8qpER9UAcYGNdZ03wL9TkOdmkez1xSETFQMDF9x7bSQSiiJiUuZvOALiYdNl-gG4goomsGYhfxtiLrp23NbssNo-X1a14gPmgKD7FRBbUO306qJh2FMLUEYHDdd5aTBjVtTnM4U6dazpLm57btyb98m8o-hVVLnPWnyIVhUrkQjfTTlTqkaImDw0Vq1zTtXLCksANDHdL3SyR2B70MGPm0a0LORrbULPsfm_8CVARJAHNYmBuCtFx-TQ3h3VPcVIK6YRvmxJxlayDWZa--F6eSilD78Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
🤩
جادوگرغنایی: تیم ملی آرژانتین با تمام ستاره هایش مقابل کیپ‌ورد غافل گیر خواهد شد و باشکست در این مسابقه از جام جهانی کنار میرود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24642" target="_blank">📅 00:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24641">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qGLB0aKf1M9ib0HkU54xCp7KfLccYEgjM3eHtPDWkFbTDo9Pat9x_GzHsFOy7yhjdjeSVvqpgkNCQXS_UooF0RmAuzV2aLjryKzvBH6n47-ZlD26ClS2dhW4BevhCt6zEBsOwEf4AM6PuoBbJsIzsdvdD152p2EpQq1FLyWcgu63fv6aMpVNnVOR8Wa27No9u5t_gT7tIkVFHNtaWx8AXhvl2x58i_kji3PDZ4vnR1V7-3ut3pL3Oa4HDjMgRh57Za7s2GpaM-5c4R-XTfKYpXwyuxSt99QhCvV8xGUkrKi8PVTHJDvn1tU88XEnESgxER7xMeHaiBL5fs_YvwyP3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق پیگیری‌های رسانه پرشیانا؛ بخش رسانه‌ای باشگاه پرسپولیس پوستر خداحافظی از اوسمار ویرا روآماده کرده و بعد از تسویه با او منتشر خواهد شد.
🔘
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/24641" target="_blank">📅 23:48 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24640">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d09c7fb1ae.mp4?token=uJ08ffNR7rhVotk0JsOQCgb1aj0x7_bMuItljpjUVKFKN76AMGAdy_dLusKvHe71wtgMkZih1WB8cXtQaSGHhYiv1EqwydylzqyAqV0wulnA2aTb3oTEML7nvcde3tL5Sdv3Gug6SxK5MZjw-cTsy6NFdkuJRBMwhrqge-4Jw_HzN6gtu9sjn34z_2CBhS_ulF8-bXxusUH0yysMMBWY-uHyhO4Je37xFkyqQiQgfkt5gg-1k90Y9Rx4SCqOmMrxdKJ7aCjusXA444cpdKFYQG19vw5qIPvAymQJiL5efsLIo3F5m6nJkOOdMb31anbvyIbrhIr9iAnk7BzKVK24aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d09c7fb1ae.mp4?token=uJ08ffNR7rhVotk0JsOQCgb1aj0x7_bMuItljpjUVKFKN76AMGAdy_dLusKvHe71wtgMkZih1WB8cXtQaSGHhYiv1EqwydylzqyAqV0wulnA2aTb3oTEML7nvcde3tL5Sdv3Gug6SxK5MZjw-cTsy6NFdkuJRBMwhrqge-4Jw_HzN6gtu9sjn34z_2CBhS_ulF8-bXxusUH0yysMMBWY-uHyhO4Je37xFkyqQiQgfkt5gg-1k90Y9Rx4SCqOmMrxdKJ7aCjusXA444cpdKFYQG19vw5qIPvAymQJiL5efsLIo3F5m6nJkOOdMb31anbvyIbrhIr9iAnk7BzKVK24aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
سرمربی ژاپن بعد از کامبک خوردن مقابل برزیل: بنطرم خدا با من هم سر ناسازگاری داره. این عدالت نیست. ایناهمش‌آزمایش الهیه. خدا داره منو میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/24640" target="_blank">📅 23:35 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24639">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KZDCRwk1W2utAfpz4VQI60b7PGNg8WfvuLyNaghDPCOuWjTWKi7WvWiWH6WRlBmmpnAefUfmcPiM6O77OXQNMmAEwuewlZzmBIKp-7VL4r3r4ER0msj7XFoKyaRdU_ep2uZh9UO2LQmP-yZ9nd1t9DA0XVRPpI6_a_HO-deZf_T6vQogzFEl7qtEx0y5vpK2ysikzm9VZHtnYqNoBx0jwhLVWl-n5wa7JPWtpi_tHLlp_OnJ_73CfU2XT7ZRabEL2qBieTUzkmrlDGf2f2fuOZ4QI-bVHVaLTfTTJ2uinsXry9NSjKoDgbKViacbw1OOzSRC72TBrOwEyjtnHqtObg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇯🇵
سرمربی ژاپن بعد از کامبک خوردن مقابل برزیل: بنطرم خدا با من هم سر ناسازگاری داره. این عدالت نیست. ایناهمش‌آزمایش الهیه. خدا داره منو میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/24639" target="_blank">📅 23:23 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24638">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gA1ZzVFZz1cP6O77DtTSeyWmhuv8Lhfm6C9zDl4TRTkmTzR-0jnZ-OxkPCZ3RK_3VxV73HhvfWailA-ZWk916hOw0vTdJoDHdfq-NF3BJJWzNv_TPeS2RwOW-8f_db25dHO0zs8g8uTqXe5Q8_94Ob6UB0om_iuooBxekJp1g9GtMjgjFiqBNPLDXrb-a9-oQyYactz6XaGXqTL3ebLvbeY_P3w1p-hSezYTOgigjvFxtSFeuKHfrd58cdINWODxAx9ovtx2YuwjRNWBZ2g0qtDARJ72stJ0d-p4XxbAsHW-CZLiBNk_PNVymrK8HiuBgqOaL9jnhtOmLxdAcvw5mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌شانزدهم‌نهایی‌جام‌جهانی؛صعود دراماتیک و نفس‌گیر شاگردان کارلتو با برتری مقابل تیم شایسته ژاپن؛ سلسائو بالاخره سامورائی‌ها رو شکست داد و منتظر نتیجه دیدار ساحل عاج و نروژ خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24638" target="_blank">📅 23:18 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24636">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V8cDUSBpRCiwHshKeDzVKOCOiYN4RlKsBVn8K9KSdu2wqjgiu2Gz3N3cSr_t7K2zy_TenB7HSlquWWIDInW-8nEDo0EWwaO9IXhrOzF7FRk3LHEv4Ucvqtx8jyr0mzgqsRDRZa6NcrNnKRhfMA65L97RTwEPNGuMa7XBXwlu2YEI7ADRCfdG0K7IX9T4iEEfQWtYoehHQG7lWnFVT4d3eFfpsEooDYA5LTAle-KXOlM44WLbOxOjQjKilPShLSJ-PbKkPqlYnMDqRgHrq8dIEVTwLiWY5N1fwxGLGxWAraia89OIngbvtWpOejfSVGR1TpbAeWh-L-psDtTO5F1o3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدار ها‌ی‌ فردا؛
از مصاف مانشافت برابر پاراگوئه تا نبرد تماشایی هلند vs مراکش و جدال حساس یاران هالند مقابل ساحل عاج
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/24636" target="_blank">📅 23:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24635">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hpzhN8riObwOV9UxXRp1gley3QBM2Ik1Fkj9Q3Qj_r9y1qoKbSUhRucQQjKtgPbSjzTLMXafxGulz2ZAdZspMk26fsp5jIowFvJ9m45Vt2oPdJjRfaNdTL53A_yBkQVvT5BZAgVolqm1NOKH2MC95EoHlMZdiAvTTFhOhUBR1nsUluFXYCQDfFRIbXFT8VqmdcLTWoEzDR5k70FUcR4FXahPbBCgLuI6PeJQT86rWju7tOlHw6SRNs1xkLrORnXCwIYpvPwVeSPJbDILe4R08inzJYaOJSf-uQpnPgJU_q6NvtXCLz-8AUbfNCOw0J-LaeKkSMeKkP7mxxljtzLxow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه‌تنهابازی‌مهم‌امروز؛
گذر شاگردان آنجلوتی از سد سامورایی‌ها با گل نجات‌بخش مارتینلی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24635" target="_blank">📅 23:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24634">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pBjefye0DlfA1tpOi6_LSD4-C1CxET6wA29dHMZ1NV6eMzbqxKSFLi_w3ZBUExX5Ne9uTeQ-nnCvyv73YenY4Y_0Lby7PaOV3HkM57O3-o9BE4p0Utt8XbyRhbBiYNbPunpmCDlETdJnpHVQNuTMjYYWWMe80K_EaKFV_4g-b4j8IeFFEIvfcYZbZKrfuON9TLnngB5M9BybtcFI4dTlaV-yMBcBttYJ3CmM_0l0vhjkUN4Bqg4-ZLbovGCYylf0L1DSZzeqXan7fEpvRzMjBMJUbF75YquemDupzkQYbj4W9JFCi4mFU9Om8qI0zUHpf4VkSkHyWZ82gTX7MIiu2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇱
🆚
🇲🇦
🗓️
۹ تیر
⏰
۰۴:۳۰
هلند
🆚
مراکش
📌
هلند یا شگفتی دوباره مراکش؟
⚽
🔥
هلندِ که به عنوان صدرنشین صعود کرده برای ادامه مسیر قهرمانی به میدان می‌آید، اما مراکش با انگیزه تکرار شگفتی‌هایش، حذف یکی دیگر از مدعیان را هدف گرفته است.
👀
⚡️
لاله‌های نارنجی صعود می‌کنند یا مراکش همه را غافلگیر خواهد کرد؟
🚀
بتگرام در تمام مسابقات جام جهانی ۲۰۲۶ همراه شماست؛
با پوشش کامل بازی‌ها، آپشن‌های متنوع و هیجان لحظه‌به‌لحظه رقابت‌ها.
👉
🌐
🚀
betegram.com/affiliates?btag=3_l7
🔥
⚽</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/24634" target="_blank">📅 23:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24633">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iq4OW6yk8IFPtYKMG_8khj04vs6v52nlstN6iyVm1Z5pB4xBGnddymkxQxq54i6M-wiC-2bap41xuBhywFIkKHDAHPBv_Whw-cCMsifNdbMN2FZwWwiWJjJZf0P_aDqnu-MkiU2gUmN6HNHerwdB7mlh31w4DIgjwBNwJDjb8Qqdc4O6TRmMY1qE-UBDNL4hW2Ljk6dstJOB28FuQYRU6lFSMNTZILNgzcCD6-4tyOmCjNawqjzWTBP8YcCRLqFxE8zCzNw1b577kzU9GMEdZ1GZYIJK95D7OkPQ_Oaf-kozPIflH7kwxwsP-60QFuEeI5I2W9fCg0y0raRE3mBf7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ مهدی تیکدری ستاره فصل قبل گل گهر سیرجان که دوبار تا آستانه عقد قرارداد با دو تیم سپاهان و استقلال پیش رفت درنهایت‌ ساعتی قبل با عقد قراردادی دو ساله رسما به پرسپولیس پیوست‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/24633" target="_blank">📅 22:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24632">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oZZecVr44pOOrt0zx3sFRloTiXNR5ISgYGL0Dfwqeuzz2To0mk711zokalDEfozrjCBv5WNzOgso9bVAXxkNXO6QBJaVu5n1yJbUCDZ6OiUSMeP19MxNfHCUWQAUlj8zr_t9u0MAR6jVB7VxmbLO7-xyc8Wml0HTtGBnTEpFod8Zwx7BPW9xYzJPCDy6kDQcirclkUzuLOLg5VJfy4UrwiNddhLIJQpAXSWNfJlL3vdeW1AQ3XosanUHqoApI0NuaFNfqGsIpDCVnpIUlvybrLMVHKwdrS3YelYrvqEOED56FLZFx04SMuuLSPbK5MoGyoe0KXd7W9pH8gjvnuqyQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
کاسمیرو ستاره سابق رئال مادرید به این شکل گل مساوی رو وارد دروازه سامورایی‌ها کرد. سانتر دیدنی گابریل رو ببینید. قشنگ گذاشت رو سر کاسمیرو‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/24632" target="_blank">📅 22:36 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24631">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56a71ed73a.mp4?token=EDS9IkMrOdVokFBgwxnatgYxuPVSPyzWAe66b0Yc_Gd8xjIU3dbkHNfbJoiOrlAHpxlfj9kzfzWQU2eVMCeylS8nh9g69jw7s25DVUG3iWpUFEVkhd9KfmssfMS4EIb15-inUzDnxwG6Ym_ZEW4UKErxrT8L9kZaKEJ69cs_m6wKxG2T9gu25WTqO7z2-fwAdoR3SqmvboPargDh-FgX5OtEIPty-vMmQ6Gl0IDaV0SmkjKXH_HQKBFCqEFN3MO2tfTqCobSZZ2mwEy_ky1jlIofzGV2TCvRjUFPN4ibL-PzeKeisNJ9bv7zZJEa92EqXUWxHKL6XotTJwC4MIcRkmHDzdXdfMh3k3CrRuYwQq5xmycyVdzA9CNynyCK5JX7zbrTymwOtPUGQTQyccgMavVUoEmnMMmb4KCVu1pT8j9jpq0_pedHhfLmuqbk4iyybaGjFRhFY_-7SRAtMXT5sMwAuanyqsil_7Fh9ySik6cxpsLsRZqJZlMjAo4OYdgvgdLKUywIw7rg-kkkJ5E6wcqzTxUFMwNfz64F8A55_niRCt4-WHTJHBU5kEAzuN1Ndwhi7kRXR5fmgJ_nQMjPAyomCxD1XbtfmWl-M6TOwzer-JRaev9hyxqJt42NHaDIsLzJyy6Y_T1pfY437mHDzeyE-OTDTe0-PMRtpZxazX8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56a71ed73a.mp4?token=EDS9IkMrOdVokFBgwxnatgYxuPVSPyzWAe66b0Yc_Gd8xjIU3dbkHNfbJoiOrlAHpxlfj9kzfzWQU2eVMCeylS8nh9g69jw7s25DVUG3iWpUFEVkhd9KfmssfMS4EIb15-inUzDnxwG6Ym_ZEW4UKErxrT8L9kZaKEJ69cs_m6wKxG2T9gu25WTqO7z2-fwAdoR3SqmvboPargDh-FgX5OtEIPty-vMmQ6Gl0IDaV0SmkjKXH_HQKBFCqEFN3MO2tfTqCobSZZ2mwEy_ky1jlIofzGV2TCvRjUFPN4ibL-PzeKeisNJ9bv7zZJEa92EqXUWxHKL6XotTJwC4MIcRkmHDzdXdfMh3k3CrRuYwQq5xmycyVdzA9CNynyCK5JX7zbrTymwOtPUGQTQyccgMavVUoEmnMMmb4KCVu1pT8j9jpq0_pedHhfLmuqbk4iyybaGjFRhFY_-7SRAtMXT5sMwAuanyqsil_7Fh9ySik6cxpsLsRZqJZlMjAo4OYdgvgdLKUywIw7rg-kkkJ5E6wcqzTxUFMwNfz64F8A55_niRCt4-WHTJHBU5kEAzuN1Ndwhi7kRXR5fmgJ_nQMjPAyomCxD1XbtfmWl-M6TOwzer-JRaev9hyxqJt42NHaDIsLzJyy6Y_T1pfY437mHDzeyE-OTDTe0-PMRtpZxazX8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
جالبه بدونید که؛ گل حساس کایشو سانو مقابل برزیل اولین گل دوران حرفه‌ای او برای ژاپن بود. تو ایران هم‌بازیکن‌داریم تو بازی دوستانه هتریک میکنه تویه بازی خیلی مهم مثل مصر پنالتی خراب میکنه. فوتبال ژاپن 100 سال از کل آسیا جلو تره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/24631" target="_blank">📅 22:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24630">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔵
تیم چادرملو بعدتساوی بدون‌گل دروقت‌های عادی و اضافه توانست بعداز زدن ۲۲ پنالتی در مجموع ۷ بر ۶ گل‌گهر را شکست دهد و به سطح دوم آسیا برسد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24630" target="_blank">📅 22:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24629">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/stjpPRUhE66THxxqdDv5Fw2pCl6ZRWOa7xvCa_2X1T541-3EOqqIlTk-exnR1lDLHGzL2yrCCZgr89Dk-TPixbwDi44Q9QHl1dQLyb2vI8O__zmaIAdoQCYttDs7lSPbH66MNIswQOhKkmA7wNVAEeS2jLxLf1_OofZbn2EwMJof9w4aVKtkHzGBl5X4zwGpa-oS1SKWO1zjbCRCZi6t3et4dVMhTkRNjlyL4u7lJO5vnHNE07dEyiupvSkffVjVjH_0lAeJ6CqaaSjPMy9lGPrL-r6E0-vr9qTm0JgnZnTc41UrhnpGf3NpMjVd5ZzPjhzFrnU2-nxzMfJJ7bDTxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
🔴
باشگاه گل‌گهر سیرجان: مدیران باشگاه پرسپولیس مدعی‌شده‌بودند که این تیم یک ماه کامل برای تورنمنت آسیایی‌تمرین کرده و این تورنمنت باید حتما برگزارشود امادیدید که تیم چادرملو در تنها دو جلسه تمرین این‌تیم رو تهران باتمام ستاره هاش برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/24629" target="_blank">📅 22:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24628">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b41af009b6.mp4?token=aTweec_3zl6nxfXJ7pqnVhV6n4BxYlzrRsYQsGMFaEkFeOKAtTVQDKpLHAM0f2qFTKhu0vAEVFJdL4kI3ycL4uRRYUMVxCV3F_ygTcDrOMg6-WpXHO3_uscpLJjkTDaNL3sZGSi1M1OOxuQs7h7Wt90uQKRqy-pW5IDmFIlEv1PY8-L0kOA07urbkG_8dwnuNtI5gtd5dnnJ748lht8Ydvp0vTtsPJ7LRGcJcupkjI2yizUaQjKajiTTLtDjjowtOZHfmo2pOgAgIQU-UZ7Bzo8-dynRjLDQtw9ElOi_Dd7fx2VUYnwmjNy9R_SnMVFtxtKpJMjga7GT2PhWZsrrPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b41af009b6.mp4?token=aTweec_3zl6nxfXJ7pqnVhV6n4BxYlzrRsYQsGMFaEkFeOKAtTVQDKpLHAM0f2qFTKhu0vAEVFJdL4kI3ycL4uRRYUMVxCV3F_ygTcDrOMg6-WpXHO3_uscpLJjkTDaNL3sZGSi1M1OOxuQs7h7Wt90uQKRqy-pW5IDmFIlEv1PY8-L0kOA07urbkG_8dwnuNtI5gtd5dnnJ748lht8Ydvp0vTtsPJ7LRGcJcupkjI2yizUaQjKajiTTLtDjjowtOZHfmo2pOgAgIQU-UZ7Bzo8-dynRjLDQtw9ElOi_Dd7fx2VUYnwmjNy9R_SnMVFtxtKpJMjga7GT2PhWZsrrPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت های ابوطالب حسینی درباره خوشحالی بعد از گل شجاع خلیل زاده در بازی برابر مصر‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/24628" target="_blank">📅 22:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24626">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/863d336b56.mp4?token=QKkF-KilDP02coDEhtzkgZ84OXOWGdo57YCdYlGGzkfr5aYXIM5U4NfVMQEnOaD1-dMLpD64_YNtyaOkOrqNa8iQ_0WnhMfql9VXZzjT1e_5JfJ2txVyiiVFK153OAPN1FBn-PrRCPapNuuHpt2DwJeMcZRUBpkFtNlIJrHriBoYxnxzOTPPD86rBbUtohiyaM7Ga9r7aDcgf-lrys0_1BDD2WZpMViaXvcqWyvGeoslwAdBaTa5zNtEag5snojd9E_gX_3ecr8WOAeh8FEvMAgaknx0t0bMr2osspe090aPf57VTX17ycFTvzHW3q4nrsoK79Dd-MmOJAkZS0yRLGHrdjosLQI_TZsYCAAzq5es8oVUXu4V0ihdqOkN0aLBD8M73XOf6C6IQPhGEDYX2xNa5_PbACCokXR_HDczIotoNIjke1JQK9Z5pbT3CCZbQLxNzv_JfsoNjsR5Bne400cnpAPedG7whrajaycevp-GOaT3An7iQ1IVZXsxGT6iGlz4jt80iYXO6VpNj8bPzfa2HgyOQukSL8We-rN1YsQyJ7hqW67GFYrVrYjeK8db-WzkXzWiEts8j1d6yombaMaT5DoRMcQW4FahiRAz6FhX1vx5QJvY6HoS_ivIKumVmTtnDSzWQoWPoQ-2cOQxzmv8aIAs3oyRAsps3p8hpdI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/863d336b56.mp4?token=QKkF-KilDP02coDEhtzkgZ84OXOWGdo57YCdYlGGzkfr5aYXIM5U4NfVMQEnOaD1-dMLpD64_YNtyaOkOrqNa8iQ_0WnhMfql9VXZzjT1e_5JfJ2txVyiiVFK153OAPN1FBn-PrRCPapNuuHpt2DwJeMcZRUBpkFtNlIJrHriBoYxnxzOTPPD86rBbUtohiyaM7Ga9r7aDcgf-lrys0_1BDD2WZpMViaXvcqWyvGeoslwAdBaTa5zNtEag5snojd9E_gX_3ecr8WOAeh8FEvMAgaknx0t0bMr2osspe090aPf57VTX17ycFTvzHW3q4nrsoK79Dd-MmOJAkZS0yRLGHrdjosLQI_TZsYCAAzq5es8oVUXu4V0ihdqOkN0aLBD8M73XOf6C6IQPhGEDYX2xNa5_PbACCokXR_HDczIotoNIjke1JQK9Z5pbT3CCZbQLxNzv_JfsoNjsR5Bne400cnpAPedG7whrajaycevp-GOaT3An7iQ1IVZXsxGT6iGlz4jt80iYXO6VpNj8bPzfa2HgyOQukSL8We-rN1YsQyJ7hqW67GFYrVrYjeK8db-WzkXzWiEts8j1d6yombaMaT5DoRMcQW4FahiRAz6FhX1vx5QJvY6HoS_ivIKumVmTtnDSzWQoWPoQ-2cOQxzmv8aIAs3oyRAsps3p8hpdI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خطای شدید روی وینیسیوس در بازی امشب با ژاپن؛کارت‌قرمزنداشت؟ داور به کارت زرد اکتفا کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/24626" target="_blank">📅 21:22 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24625">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OkMBQtsIBvwR6sTWH9lYfm82vJH6yoo2kU_SvWdWysHaO3ruFHDsAxa_kKpiQej7ng1dDlidKeBdf1vvliyh2jEJfu7_RwWTgCt8Qk3Cns_njNHKMzj5XPeX-X5bWCAdiBIVxZ1lPmdiG5e5gpSQTSakqY9x6K9gizTIIDADDcRUzoslDXl85mEuofDIc_r_L4cdlZovBtYiFDetR2ws0VPi0xRKQK9HwTr0P0zx2TXWJ0Omljb18KlI5aieoi4SuLsWI1pmwSzuXCnscacmsCGv3i-mEWAVfzhGN3rnrW9wJaPLrIX9P6qoN_U1sx5P9InZtH4RLSwSvLTj-QPsfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک شانزدهم نهایی جام جهانی؛ شماتیک ترکیب دو تیم برزیل
🆚
ژاپن؛ ساعت 20:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/24625" target="_blank">📅 21:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24624">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7056183539.mp4?token=pJl-kVVhYIZC8xiXtClBq-VSbs1VWkQudUbaMUBT7Wx9dQlzwILmi5a7bmwfLA3TUCCQb8nGUQC4gw-hW_LcwI1Xv0xs_aKDzVsAxJkQdGNVW8iLOH5wSkSuFLT4_NbLV6-Tq7Sp9KqThjoC4IxDUh96lfiMskeoVKEOa-vz6Ag_P_x82lPHCff3ehuB_36M519CRunNzaohWH6dlcjpkAPBGxc5oTUicRQcwHNMWD9i5XKU_kmdw3zJ5eghtV0M8fvPoO_BrhIXUhrvRphCPc2gyIQHcCINUi2pe-5X6Hfx2y_1vl9YL9bJw-PN0LjojE_t-6m2qwZwUCynUz_SrqZ_kf-uNCm_sxY7OMkhaZ6UPuOF1GpzgUAEyR5R31NZPXuWN4_jebOtvhUHEpnKzupASq_IrfYMUd0buC8CDnIpZrG7HgCbFzplg0CfIH4gJXLaFybj3dt-VQCnPslbd3vQhauD0t1Qz8_AjuDufDOWkjWyzO1oohMvgF1rMVYBf6oR-iC0H0QQMBd9hdffhxr2ZMTBFh8Jn_jni57_Azf9UE0X_q_0Vw5MYu4kxUjT9rmIEO4lfgnufFuKbwjSMazUOdIIdClyES-5937awRjKKDw95pTBV_yDBjEsNXDvmnhEtMZVRw3ZNGMma_GPqn7fTy1fDRdDlyFkZeYRfag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7056183539.mp4?token=pJl-kVVhYIZC8xiXtClBq-VSbs1VWkQudUbaMUBT7Wx9dQlzwILmi5a7bmwfLA3TUCCQb8nGUQC4gw-hW_LcwI1Xv0xs_aKDzVsAxJkQdGNVW8iLOH5wSkSuFLT4_NbLV6-Tq7Sp9KqThjoC4IxDUh96lfiMskeoVKEOa-vz6Ag_P_x82lPHCff3ehuB_36M519CRunNzaohWH6dlcjpkAPBGxc5oTUicRQcwHNMWD9i5XKU_kmdw3zJ5eghtV0M8fvPoO_BrhIXUhrvRphCPc2gyIQHcCINUi2pe-5X6Hfx2y_1vl9YL9bJw-PN0LjojE_t-6m2qwZwUCynUz_SrqZ_kf-uNCm_sxY7OMkhaZ6UPuOF1GpzgUAEyR5R31NZPXuWN4_jebOtvhUHEpnKzupASq_IrfYMUd0buC8CDnIpZrG7HgCbFzplg0CfIH4gJXLaFybj3dt-VQCnPslbd3vQhauD0t1Qz8_AjuDufDOWkjWyzO1oohMvgF1rMVYBf6oR-iC0H0QQMBd9hdffhxr2ZMTBFh8Jn_jni57_Azf9UE0X_q_0Vw5MYu4kxUjT9rmIEO4lfgnufFuKbwjSMazUOdIIdClyES-5937awRjKKDw95pTBV_yDBjEsNXDvmnhEtMZVRw3ZNGMma_GPqn7fTy1fDRdDlyFkZeYRfag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
صحبت‌های جالب حمیدمحمدی درباره شبه علم، خرافه و فوتبال در ویژه برنامه جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/24624" target="_blank">📅 20:14 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24623">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/awTF96YALOPgVtBQHR5D3hk_MzSHe6Gl7YbGS-z8_ioVUFPz-XWwkBMpHSb4cz1Fe-s_Bor3ZwbQTD4gR_7jh43BvjeMtKhQg7rLbap_qDizJHa9vEEbUObXBco8Yy2nj7lx08uuJ10w3AanUGwvpiX2M4eysZzNKAMsUlpFJqiEe0ET80hKQFDbjp683RYBSNOwhfJ2WXzLp4ePTSkcijKSVRHFTTd94JfpprCGVBuUQt42hr41iaC9sl2khXTnvYoVkdxkVyKhVql06q2B1g1QgKxhBMaHg_hCiZOEphCyRIvQBqW6WR1WgaotFiHzVPdYA5nuRF3fjhi6TACr1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
طبق‌شنیده‌های‌پرشیانا؛
جواد نکونام در جلسه با مدیران‌ایرانخودرو برای‌پذیرفتن‌سکان هدایت باشگاه پیکان برای یک فصل حضور در این تیم خواستار 55 میلیارد تومان شده. درصورتی که پیکانی‌ ها موافقت کنند نکونام قرارداد خود را با این تیم امضا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/24623" target="_blank">📅 20:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24622">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Le8BezqoOKeixnkIGnaQp_4C4FZb9778TgTOr1UnrI35Im6QFJd1CFz9UHh7kVnJ4157U7_Sl3dVyqEznf02VULNfjDIafCPUPI1l65hwv3DiqSJVdcIvr6RIRz2QJtjYt6P4wWc2t5TvHLTYTG6-_ZAQEvwXmJ9fTvQPFAjzabMBGybAHqUGBQMu-lsxhN8Lop4-BSsVwymrF1zNCNovd8ygmHppenhXHT_rh8JOru5AyAfbmpL3uy5pXA7Mc0w2OBqn6SWcPQw8dsZjDGIodtJMhy1tbZLkHm0nO2u2BKGpieJE0brSaeDsi0cnBz3EWocuyieck1_rt6tqk3mXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌شنیده‌های‌رسانه‌پرشیانا
؛ سیدمهدی رحمتی بعد از عدم توافق با مدیران ذوب آهن؛ با صنعت نفت آبادان مذاکرات مثبتی داشته و احتمال اینکه به‌زودی هدایت این‌باشگاه رو برعهده بگیره زیاده. تیم صنعت نفت در آستانه بازگشت به لیگ برتر ایران قرار داره‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/24622" target="_blank">📅 19:35 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24620">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aKI9rvadwBpmtb-ekSf7OW2aPcy9wtcFG_8Seuxgbbkmm6Lz_XJdBBviOVw7QPvVEzm-H_MizxG5guwSk-1ootVeze8J9FzkX5ZNLhXbtXsia0zwmsV5MMqw69d5ivjkgc39h-JPDV4O85V0V1FOf_5H69NV0_AZzWgbwU291DOi5vxW42LwwUzp52-1saTHF53eVBVwt2nIVGyZD--uq-hH0C7ADni7EA-Y9ACWmDeZtM7b2XoE_d07HnjjvxdD6oeappsIvYEaJtOK4SM4s9TTb2YTo0z0pROycy-_Kg0Ob10-zG0PPWb6f0FN4FlpQpPMGgUCGr-klVPQOkS7Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YUk8iCZqgtGcZH2OWbErTKZM7l-ziHgIxnXZF6cjmlBiahT-v8ScAlFxmlHG0N5xNuHqRjjPSkIUEyMVZOSojUR4vJs5CIVI3U5ap_AipSMWJjh7j-hcqyBTh3m60Mdbq0-R7TxcRDWkSSlyYHPLDGDVEF-gD_ttsinnC7cYCeYHiPsr-bd7nlvjUn1pa7i3eTLJ0pOxMAOpt_rvgWOMS3ztxf5Z4VUxiDWVLxnFx86yEwgsTo08vXqBTGvYL9vz0Lln3jfNpOfmvCViPNZQG6ojK-Xj8oFlyP4Q4yC2G098xi9SMQ6XDYUwe0hhgEKRJAxgeMNoU8O2a9HzkRN00w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
از تلویزیون تا زمین فوتبال؛ بالاخره اتفاق افتاد؛ تقابل جذاب ژاپن
🆚
برزیل؛ امشب ساعت 20:30
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/24620" target="_blank">📅 19:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24619">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qkhVcsGw6w4kQCSgjfJon4ZMS3y7p2f_ZZ7TznW5jtYyxU6JuRXrZC2b4_qJKi4voM_58aY6yJs93bI1deF0v7lr87FgaovgQU_O70hBAXwMNXhRFmu-3j0ltYW5VrIBkRIys0ckmf9RFZ1ip0DWJRFuULo_Gdxb7IALbP8e5sUqXpxEW7fQFSCgOKmYqgSQiy32i4lTpGygt6T9Kbm1wNx2Z1e5TvsTmd_4cBTzMq7S9islfLpedNwCAox_VhXNhdeEB-SemMLyac7px9zquqOhOMP3SAL_R-tE1apXRRajqxckBJ5DVuD1JVKu6Qr2qxtf5Gg4GYSwYV_Qp8X8yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
شانس قهرمانی تیم‌ها درجام جهانی ۲۰۲۶ از نگاه بازار پیش‌بینی؛ فرانسه با شانس ۲۳ درصدی در صدر قرار دارد. پس از آن آرژانتین با ۲۰ درصد و اسپانیا با ۱۱ درصد در رتبه‌های بعدی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24619" target="_blank">📅 19:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24617">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iSym67_nYMMl64Dq9OaiH2GmsXb7g8Ca4zt9RJzMYXWm1EUKcp8j1HP24xP9RthNySHhbPsNf_PhcCWtgdETG9-wsMcZOyFncA0S_vrYFAa-88kJ0fweU_7_XkwFipRy1Oqb7KPzMSAHEruR5RhR5yCzmjXtxE50duTQ2mXFAqhGSJAFE5qeJxHMwmcBOo_2lAlSTsB2k9ZfzVM-pZWzzl0RIblsxeu-b8EaOTh55uaa9IJKj-ZWv4e9b0xdU51HFo-EsXT8wpWFIDlLYAlh19eqMjH1YuwDwAKkVAX_huamW9BpiT1O-uC5w9ivpZFpughLQQVgYh-c5wBcOfgUdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قفل کردن تیم قلعه نویی روی عدد سه؛ ایران توی این‌جام‌جهانی ۳ بازی انجام‌داد که با ۳ مساوی ۳ امتیاز گرفت،۳ گل‌زد، ۳ گل‌خورد، ۳ گل آفساید زد، ۳ تیرک‌زد، رتبه ۳‌ گروه‌شد، بازی‌هااز شبکه ۳ پخش شد و برای‌صعودباید منتظر ۳ بازی آینده بود و در نهایت باتساوی ۳ بر…</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24617" target="_blank">📅 19:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24616">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N4x56AexJyEVXA8XHzil8A6IM5IQYmnkD6mzF9AIo73DMIPwHBnjj6KdLDRd0t3r0XvCfLByAwtzvVRmyG6uOfJ7bcuEqmcN8bUHxOn0SNuVHkcew53Hj-UVxCxDhwzk2FIgvLWHBViq-sYLU54nrMcqsrPwZxdqa6biqum7j1BdAtjFkPzIHBL1wvnFRh4Q6qtLWPL-3temQ15lHmG_peyf_r_DScfxio6S3x5KyLI9y19bBiHVZL174sDNCKG-O9OaLdk5r4Hxv4vhNe_s6JIiZYjEFgokfo0QoKaPQwFNlMOS3TkMebQMkpMbA1pFKPESOGm0wLwxGMKJ9Zg1RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
باشگاه‌هایی که در جام‌جهانی رکورددار بیشترین دریافت جایزه انتخاب بهترین بازبکن زمین‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24616" target="_blank">📅 18:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24615">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZD2n0FczTdx9ZBzPGAOL4We15TMgfKpvdcGufH2-ml98lqKedsrpT9lAhx9gok7e1bVKGxYbQx89ROnniIt-xhsljkr1OWMZD1JP1P5Yq8fTOkzPl1bDheley1CyVuiuW7l-v21thHBMSdqX4ScQmMWeCSeMJStfCSRma1lwWoLHqHx5OTpvnEe9duolEr3d3cQXQ-qua4grtUATD88uWpqi2RJY9eV75uJ9wgI_ecmcYcf0_SSQuFM7hCzRB9taJ9b4o6R69XcPrAiwU1iho-cjxtcWE8CN6LDx_pJGcmPW4J-LwUM4wr0muSUukhYfZzwbkw1z8fh6cANA0TR2JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
باشگاه‌هایی که در جام‌جهانی رکورددار بیشترین دریافت جایزه انتخاب بهترین بازبکن زمین‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/24615" target="_blank">📅 18:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24614">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kog4dFNxsGXMhGs0uIWuES7CkTt6RubJaiM3xODrTateZ2b3p9Finvt9duHCm5gBUOcpVwEm6zqj7gm7kH1O_oPELKUQdp01y7AWDg6mmgj_hrrnGmKWdmbJRneWlQJKYw4AcdVCpedU0urlvAY0xcQnjYucC4C80Zplk6J9F_PSkBt87BlW4cdLMTpFJbJg1OWgW6bNRICgt_P_mGal4HMfgIcgPGYXi6bAxq3HZonnopL7YQF9xWsNgMP3o8syuSS2k--M6Xu1GwDnaJSSycyKABzV_FYInpvlzVlv4Nvim_5YaBucBkXZLEDKsk5ygtXgIzvRrlzEKFbhhhf4Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ نشریه مارکا: مایکل اولیسه بله ضمنی رو برای پیوستن به رئال مادرید به مدیران این باشگاه گفته و اعلام‌کرده‌درصورت کردن رضایت سران بایرن مونیخ اماده عقد قرارداد با کهکشانی‌هاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/24614" target="_blank">📅 18:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24612">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WqzILe34GgilKoLdkE4hgX6tS9-b0mm-JKmvh7lsEDVDIwUZupCBIl_lOJJ-ixVpFnG3-PgvInnwN8bMP9lucV9fSSFR1YzezFEiwDb1aUu-_VIjmxDPYUrSzGtgyVF-ePw02RVcozVxQAqNdxkmoSHXP8htUqtqMHeA8PyS52kEsqowSH5meYdy-OSQ1NM18I-08bH_aDWiwb-Y5AYsA3HM4hFtNryItGh8DBSFO2mRRDAoMx1aVmjI_LwenFFLH6dO5zXUYhyrzolQbX17yK0MJBLecPPTJepCkawR6cBgcGfm2YHiehCJT73Aloe2Ezj4cWhVRbVYRP8In0XX2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
محمدمحبی امروز به‌ایجنت‌ خود گفته تا دو هفته‌آینده‌افری دریافت نکرده به استقلال برمیگرده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24612" target="_blank">📅 16:56 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24611">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iro_Hdk_JpBmtlYcCiD9RciL9CEEQdirAeCuh7wuoSain5Ouni3hHy7_zFvpi7ItNVqME_DBNdKpL3ZNedUmHp6qb57hcBuxHltaaaZ79-jixPY0ZB2_6W13DuVncoDM6dFTyxSyCo8rmLT7kAB_-L2k69t1ZArgDCZZgbKUla9EALHK8ZyxQiOsxAMlCXCgCPdykPAuoPhiUl5iNSgzb49QoxmUp2Lj1jyRF4QuVc_I7B7Q1gKRZoipt90R_Le3asnhe-dng-G2cQfsyZNmnJKpTWQ4WOkYIufyY8efSJqc5SHhiaTmJGsKwk1MKiEvAWJg7dhjWbDngKBFknrrig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فابریتزیو رومانو: انزو مارسکا با قراردادی 3 ساله به عنوان سرمربی جدید منچستر سیتی انتخاب شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24611" target="_blank">📅 16:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24610">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HlyiMO78uRLWjyxyD2NeShlsTD1gIjRYZcmj3zZcbSIDGzRchDl1vPxFSYkFZHARBLvq_rIriLGnf3UWZmMtunKl8DUlzLBBJwKv3AaShDDT-I2RsXY4tpBdfDImdflWx_137EO1JRDYVjxIbkJS5CXWNvN--Pps9dQTAUG77b7Ocf2emviTtjcVIeoWTVl6jjBZE9j0EJ_2V3e77pWnH1lOvOldD3fUyjxnQ4heKAr4mbSHc9hUmL3lgZQY2fV0mkZOnUSnPLthklBxKDiAsMQI0jsKx5vdTMtwTXniEK5gnEoJ89ISYRv3Vg7Fl8n3EIDUFDeS41FXhPvdUL3Rqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇫🇷
باشگاه رئال مادرید رقم فروش ادر کاماوینگا هافبک فرانسوی خود را اعلام کرد: 60 میلیون یورو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24610" target="_blank">📅 16:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24609">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6c7c83867.mp4?token=mrjz1becixfNWIiwvWUqLzxAryL5zC-wDLjUcgR-vYeCZEOqYPivH2koynA-RcMDr-kxMCl6cKGNRp7s_dtmSldzTo8w46sodaU3BqLx9hKQ_ZmLtP_u_Ac87pbpzZFE3AOUB899gkSEENoQbwISVnPlQCN5GYeEqMxeGfzR6yHGIlOqaCL2Oez5cRe5vyoSCMUZQnppp-RCWjMW5mBwPK2wUaDT701Lx-jFTILred9MHmPo0EJKGXv5H4ouz4YRygV5AksfKcEtRaoDduOFPIM2BIFv7dtkaOFl9n5cQo_7KPF0FGZ2GDxll1CP8YqVPUdsW0kX3n-r_My-715HSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6c7c83867.mp4?token=mrjz1becixfNWIiwvWUqLzxAryL5zC-wDLjUcgR-vYeCZEOqYPivH2koynA-RcMDr-kxMCl6cKGNRp7s_dtmSldzTo8w46sodaU3BqLx9hKQ_ZmLtP_u_Ac87pbpzZFE3AOUB899gkSEENoQbwISVnPlQCN5GYeEqMxeGfzR6yHGIlOqaCL2Oez5cRe5vyoSCMUZQnppp-RCWjMW5mBwPK2wUaDT701Lx-jFTILred9MHmPo0EJKGXv5H4ouz4YRygV5AksfKcEtRaoDduOFPIM2BIFv7dtkaOFl9n5cQo_7KPF0FGZ2GDxll1CP8YqVPUdsW0kX3n-r_My-715HSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آهنگی‌که وقتی شاگردان قلعه نویی بعد حذف از جام‌جهانی به ایران برگشتن باید براشون بخونند:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24609" target="_blank">📅 15:38 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24608">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rj-AcHeS0Np_p3fGPrwIVVtR2JOvtPk8_X86P9tGtE1QxKHiULPc_AV84KoT5eayU2UzNW19HEWv9M56oU3pZAGPDmJhYhZYlyL7XscUoEWAMZq2mpCWdasBUL17Dp2NvkHnR6OArEuvsQ1jNBnqDj388Q84f6tyXniEsdwp73su9pyAyorwauD-sQaTKL01a_qRmfJ5eDJUHr8LbJhyJnP5CRcRkxRuAScCxFvk9jJERIu7cQp_LQQN7VJlVW5I1eGMEQncWtWrZmr3BoqTetnQQRGdRmeu8c56RWkg1aG-mqfFHkxK4rs_ypK7jFc39NlEXjpOJaZwtsK3qpL6wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رسانه‌های‌اسپانیایی: هدف اول و اصلی مدیران بارسا برای تقویت‌خط‌حمله این تیم خولیان آلوارزه و درصورت‌پرداخت 150 میلیون یورو به اتلتیکو قطعا این انتقال انجام میشه. حالا اگه یه درصد این انتقال انجام نشه گزینه دوم بارسا هری کین 33 ساله است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/24608" target="_blank">📅 15:23 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24606">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iBp38YdftoF5lnyHOBpdT7o-FzxwIOEK-AegABck5rkSsbfO5Yz9ZU6Xv60EBpEJNTXJlzHpQIFFB6qN9QxLXxxOoAo71nrZutrqKuYbyS-SOaWMjbW2D5XPiYv3tIXI0tbXo6XImN8yB6hVTSOkcGx4N51qm6-yGtchaMcaSArf9IQQzMvAHKR1tVl7HSpnRIePTO3RVBH5jNS7l-RnwhBe8ZA8KgNUXmveqXtGQku9eYJu4bFE4KD5paNspAZqQ-C6okyZE6rUdmY5S8Spwip1eNqibIhuUoVxMT1mfM3BazM_YEL5W8wn0s1CdEISJOIQVQ-IDPeadT8UV-MswQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/shEtHjXx218n7ldCRYhs9Le9FERR0CFovYpF7a3zXf_BaDYerxwXkpSpCHblOVG5cylpxCvz1GXIX-ZABR15YIgmRaqMAJGEFypQVy3GnI1uJT9t-3Qb0MM4Ik3cXvgWcgEg02bwTV4wzyadNrC8y0q7ocdniYtTRsjUVUNjfwczGlckEJ3Y4thLCQ51nsp1H4pJV2phBFznrhZ74nZ4yU4xB4Qng8JOzrfN85ANNtGx2zc5BOwcMRTV3qkjHokNFUtdmgs0iYjYd-Q0GAr4stiFvTut-hNsXY_U7FETs4G7YJ1ysv6oyK1RApRcIggQwJqaIfYOsJ7dwEfzL1Bk2g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
🇧🇷
نیمار جونیور کاپیتان دوم تیم ملی برزیل: وینیسیوس فوق‌ستاره جام جهانیه و مطمئن هستم که میتونه ما رو به قهرمانی این رقابت‌ها برسونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24606" target="_blank">📅 14:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24605">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rv6paXZ4IIUOFQ_NJjAUwPahwO5L72vr13vKNuJAps7Z6mhUL4Z93cBI5j6XoiYy9m_zCu6XrxXnDUBgKrn23Iv3C5Vb19azdMvPUZBtDUyNkHIaESBIzaVQyp3rtKD1rALSH5qz5G_yrEP98sON3bRHuGcoUzWqyFzEt-19eXNW4v0I7sO_oaXR10kFDeKQRnVIiabTFjmI0GegBOn5KtzIfc6j8iX8-xd-Jvq7ve3lhiyYxm30XrosrR2MvY3_oCjVzDoLq2VlCL1T85tlRuqHk1r8JBSb-OtRS5OTUATSthYG1DmOug__bMh8qGmtaoG68GckQ53lrE6h3kkg1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این بلاگر و هوادار تیم ملی اردن در پیجش افشا کرده یکی از بازیکنان متاهل تیم ملی آرژانتین بهش پیشنهاد دوستی و رابطه داده که او رو بلاک کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24605" target="_blank">📅 14:38 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24604">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bPISE9oDFYSoeB0MO5k1Mkn2vSbmvzyf2HTVq_4lZT0dSU9ConDrEu_b7sh2ul-2blXdagPr3ioKmOVlHtVkesnJ40SH0gPaoA9ygitjIatmhxiRYYeS-dukttoSKBBi05Qd9x8Sai8XTdgBjI8jQ439S_aekbT7pKkqaPgZAFVxFpoMOY4J3-nQY8JXTjjEUOySeVGzSVVD_02NR6SsYtUCZLP44gdyaHbrRHOoXI2FeGSCv-kdIQ8LXRwIuiV-Bci-UdkCdr7GjTDDGoYTgElqZUd4Jm-fc8Ji9AYSNBUN0w4s4jFSjyaUvntpmEi57etzS_-giYC5ow_AyqWnvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
مسی باگلش‌‌به اردن حالا ۷۲ گل با کاشته به ثبت رسونده، همون‌تعدادی‌که جونینیو افسانه‌ای داره. لئو به۷ کاشته دیگه نیاز داره تا این رکورد رو هم بشکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24604" target="_blank">📅 14:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24603">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QqxOgnsIDJ5hTKHHGLRWlIhdLRm5C1ngw_YRZmzzdtl9RXW6Km23aUqKHEs41wm1nS26FFAYgH-SAq5veR0FBCrR54cJ6sRQkOOUgsU5c7ZWERRkWql5is9l-2OM4kyO35tpVFB2Y46e4xC89Ejf7rv3jn721489_Wo9ZJVC05g6x2GCi-jOMb87MJ9D3iLsAa6nEp4E-3NNVsRc_ChepOOovmwKIDd52pnlvZRYlfq4yO7rV4nFeH0U8KB4QU3z9A9xcNK5uUTCZYFllDxY14co0-UczxQ_56AxbSb37nysFRpCfReArGeSmiqlgW-71hiWE8klwxtgOIGHdfw_nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
درباره اسکوچیچ پرسیدین؛ با پیگیری هایی که داشتیم پیوستن‌این‌مربی‌کروات‌به پرسپولیس منتفی نشده و اوسرمربی‌فصل آتی سرخپوشان خواهد بود. فقط بین مدیران بانک شهر یه اختلاف نظراتی بوده که تو کانال پرشیانا آنلاین بازش خواهیم کرد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/24603" target="_blank">📅 13:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24602">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2df383dff2.mp4?token=S7Ne4etAaCvzgz1xQ-nqPT81_FZIsqCiTSGopDMTSQ2_oIYSGKHuNmCpkpZc1V_bJ1zTwib_hEITyFt5skGBwGyx8x3TgIEtJg0Xlw3Byd1N5zj0sBKy8gXmxi6SjTRwBEC3vK065ehSocVQ_zLzIOcMSYFHXsqOr3CxpX8SxWPRl3w5pTMUSmIvOaDdq21uzDAsLbzKCfMxYvS-y1fKmlLcbP7xoGVyCsn-0Yy16PpYs443JlSG-GbDRw7rP6edxIPJG3pW6fsnm-PRB7R87xIdYSoCVUWg5_9krtE8YY1s41ZErcTwXlLsS5gI5V4qwXpasQxhMhqWJmaxMk3CRzhHtoO47gF69eRRvjHg0Ap68xswDxOTzxV4kkzmfOTL0B9yfz5ThAX7l-3p_SZCgEFYPouklMHvWjPmd27RrAP7QegzCkVzkzy5T-pZQatB2D1MR6t1U8of-z_PH8clBRPK72uHfaUw6sFh75tgF9EICxyLlNXKi8MHOOygAMhSoWrfGulHYk1k7XIC0_TApGIHbM7qlKxjJ17yIWuX8HXcvA4uxyemOJ0hvHVreEBJpqNVMrYDOdtNjPgELPTQuri22ll6GfrpRUQMYCLjiEBG7RlmDkpG50iHBEMeZOmxRgARex-j_8NDnGx2MHABAkjDFYwkz3O-An-vKUen0W8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2df383dff2.mp4?token=S7Ne4etAaCvzgz1xQ-nqPT81_FZIsqCiTSGopDMTSQ2_oIYSGKHuNmCpkpZc1V_bJ1zTwib_hEITyFt5skGBwGyx8x3TgIEtJg0Xlw3Byd1N5zj0sBKy8gXmxi6SjTRwBEC3vK065ehSocVQ_zLzIOcMSYFHXsqOr3CxpX8SxWPRl3w5pTMUSmIvOaDdq21uzDAsLbzKCfMxYvS-y1fKmlLcbP7xoGVyCsn-0Yy16PpYs443JlSG-GbDRw7rP6edxIPJG3pW6fsnm-PRB7R87xIdYSoCVUWg5_9krtE8YY1s41ZErcTwXlLsS5gI5V4qwXpasQxhMhqWJmaxMk3CRzhHtoO47gF69eRRvjHg0Ap68xswDxOTzxV4kkzmfOTL0B9yfz5ThAX7l-3p_SZCgEFYPouklMHvWjPmd27RrAP7QegzCkVzkzy5T-pZQatB2D1MR6t1U8of-z_PH8clBRPK72uHfaUw6sFh75tgF9EICxyLlNXKi8MHOOygAMhSoWrfGulHYk1k7XIC0_TApGIHbM7qlKxjJ17yIWuX8HXcvA4uxyemOJ0hvHVreEBJpqNVMrYDOdtNjPgELPTQuri22ll6GfrpRUQMYCLjiEBG7RlmDkpG50iHBEMeZOmxRgARex-j_8NDnGx2MHABAkjDFYwkz3O-An-vKUen0W8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سه‌شاهکارتاریخی مهدی طارمی مهاجم 34 ساله تیم ایران در ادوار مختلف رقابت های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/24602" target="_blank">📅 13:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24601">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LCNNx1rkY1Yob2Yn8TJ5Ng1RXdDIfZxnQyKznrzB2jXRg36MMqwVr8kCMZi4Br0KL6NjBl3S__EbokQ3dcOeC9is---Bp6MgDE1_2OQfugTLO6QpY-VQ2IwbfIMOgDFgs17Wm3opJ5opLjz2Tu1d4Rv3Wo-3WklNA7rlzzgCOUXwm8Vm1gBVAqyGKb5Eg9qsx2i5ZXFTzDgzJVCkVVqFUeQWqcr3fqnPGRmDRUqvFgrnYVnXeF6NekqcFY9G_2CvwrvyBkKVTQ-1GonuGGxLgWQblKJRXR-ZxQ6BSQNoU1t-tkpiIMnuf2kIh2Q-M_0OhYpWhhWO5V-ABhbDhMq4iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
کاشته دیدنی لئو مسی دربازی بامداد امروز مقابل اردن درهفته‌سوم‌جام‌جهانی‌از زوایه متفاوت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/24601" target="_blank">📅 13:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24600">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/268dcda4c9.mp4?token=EZ4YhZ-n0k9V0i3YYYbb5Gs8KxOF20Se_kQuUb-x3cA93MZ_dn_kIzqw-w4zGiioObfJSkRz4hsTUKP4aMNVvHvn1Rb7fNmRiD7OlRR42g0uXY88NHh0JsMvh6OMGQXcf65LT8Rneh7MpZBMheCFHFJNFTlh_wLQ0fZhw2MVeBxKoqb_ZsczaJyXEwU5KmzSH99uZPFvR8jtxTCGwf7MQ4S_aUbF7ivuGEuCNsm_n8l_rJvRWLUvamuAan55Wkp_CERKG8U6iAUOvPDUWqlpObMp0CjK5zLkVab59g229fU7RC-CFVy4g_cSzJncPL-P6OPl0V2W1VxAhwxn7zR-qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/268dcda4c9.mp4?token=EZ4YhZ-n0k9V0i3YYYbb5Gs8KxOF20Se_kQuUb-x3cA93MZ_dn_kIzqw-w4zGiioObfJSkRz4hsTUKP4aMNVvHvn1Rb7fNmRiD7OlRR42g0uXY88NHh0JsMvh6OMGQXcf65LT8Rneh7MpZBMheCFHFJNFTlh_wLQ0fZhw2MVeBxKoqb_ZsczaJyXEwU5KmzSH99uZPFvR8jtxTCGwf7MQ4S_aUbF7ivuGEuCNsm_n8l_rJvRWLUvamuAan55Wkp_CERKG8U6iAUOvPDUWqlpObMp0CjK5zLkVab59g229fU7RC-CFVy4g_cSzJncPL-P6OPl0V2W1VxAhwxn7zR-qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
به‌مناسبت‌دیدارحساس امشب؛
24 سال پیش، فوتبالیست‌ها رؤیایی را به‌تصویرکشید که میلیون‌ها نفر باآن‌بزرگ‌شدند؛ نبرد دو تیم ژاپن و برزیل، جایی که هیچ چیزی غیرممکن نبود. «رویای ژاپنی» فقط یک مسابقه نبود؛ یادآوری این بود که با باور، حتی بزرگ‌ترین غول‌های فوتبال هم شکست‌دادنی‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24600" target="_blank">📅 12:37 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24599">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AdtOnjLJxbMwNQB7S-mxX3cl0-csJ5DvToWzeBUA68R6gQBwRgF0kQkFkt8bbGllyI2nI_vDtVKGmAeodU-963JAfPCKskJKpygGf7t1l9yVDlIpsch_L5Bo03Y2JsaOJtL14oeQZWNU-ZKnpCBPPc-YavSB9vfY97FqXLk2F1G6Izg3iOBIPbweAI9s-uzcyIZfEEzcXfIKUp-KekCUdSH3rEGLXglxRdV6-Vhi7PR_CcvI_L946V1Qs_koUO0eNPYnRFzOvwn7GsHX9zB24cMcJ_MtZd4-UR0dAgmYg2-2OwfhAiT4pcMJclBA3U0BEXq1meccV1xwWcOasinfbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
خوزه‌فلیکس‌دیاز:فلورنتینو پرز رئیس باشگاه رئال مادرید بعداز فروش نیکو پاز به کومو با رقم 60 میلیون یورو به‌اوقول‌داده در تابستان‌سال‌بعداو رو به رئال مادرید برگردونه تا برای کهکشانی ها بازی کنه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24599" target="_blank">📅 12:23 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24598">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V8O4vxTMRVhUUZ6svhvAp3Zsab-bz8CAptgb6iCSk9zt64ezdOAJYamokzHV8gmDG4b8aYWCDOJgrl94q4uX1iXIR0fP2XcZlXvdhn4gi6nDGXI-t6j0liKMDKl9PDbpi4ptKx6Mt_ez5vrLNmkOumZoXdw21IG2ny4PRZIG7Vj2IXwkvyWLrDGc8IJfPBKlgxlqut33Ku3ajs52urtR5fx-6g_2Np2Ten6vzGzdLu_mys6oTBrsHZtscE-DjJyxA6sDeLbNUdF3964nqMUICHDzp78YN77PVgXw6QQwyHDrI7ivX9y8VEYU2AY4Y9QgO7r7DHPlzt0sK5ajB1LKSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جالبه‌بدونید؛
پدرو همچنان‌تنهابازیکن تاریخه که لیگ قهرمانان اروپا، لیگ اروپا، سوپرجام اروپا، جام باشگاه‌های جهان، یورو و جام جهانی را فتح کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24598" target="_blank">📅 12:06 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24597">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A050D1eW88pebPqbbc8T7cL53Gca-Kwdy_a2bf383zO4nW4iN71huh8YfcqTZ7-_R_lGAbHdWAZTVeLwvAiiW1JaR2Bpgj8nzOV0Vr8aP-fgrmKFdxhU42MPd1NVDgrVEyYfMJthLaBwQxAmR0AqHmvOwQb7Ih4rMS-fWZBKN6g8JVIh0by6Qkq5mRxPgDntX4IOjn7rVwF76twmt0vLmJmVLIVdDyc2S92dN7K1jTNa3f6J02mwpwMSpaMFsYUZ66TBTTqsVnOOkETzDhxvW1G6rMyHRk_Y0RB4q26E8bX7iYtQqsBLXOXWFyBLHomaa20U4NKNO5gEpuMi6oqwiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا
#فوری
؛
طبق‌اخبار دریافتی پرشیانا؛ اگر اوضاع منطقه آرام باشد در جام ملت‌ های آسیا سرمربی خارجی روی نیمکت تیم ایران خواهد نشست. با امیر قلعه نویی قطع همکاری خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24597" target="_blank">📅 11:51 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24595">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jtZyOU3uDxUWHW6lVJElInHqjL9iqVguNiLI_9_MccH3abOtNh2L2j33PcHeO3-X6mcZEx-6n2i6L8TE2nUhTEtiAjX6-Kg3J3B3VPkcBA09TkmTlDugcYvBAWwIYAP_e_FcNzqALm4UeemyGpbzmRS1Gzzk4n_wNo8v68Noa9PlWGC9wYNPsM1lCxTEfb80bCq8ldgj_xaj31K4jL-3qn8O_nN2Fes_JaynUCuQDABeZMbWRidMAwcoI7ahWVfMKZRY2KrByYD7fk0_AX3G_wbv7EOsVqESKTpmKgkKAjTZAYcKDPCK622mYIZWUj2VHw_404PgG_b0bVIfrAlEsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدار ها‌ی‌ امروز؛ تقابل‌های حساس دور حذفی جام‌جهانی با دوئل جذاب برزیل vs ژاپن
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/24595" target="_blank">📅 11:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24594">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CnakvBiPJBT5L3dKJ-Br8aLakOijizMNFRWjl5VmKjDo7PTKGn8O-eFAyXTkvCnUuznvhn7B4su6c-M6INCA80qDZt3bhG2T9uPe1HRY9qD2KlNebZ742f3w9wLIvNu5M_cEQo_nUGlDGR_2HrCPfSsGgTef6Syt8IZwGT-9H0EYZEpvRlZEw06TfyjDxX34C3d2oGpMM2Y7Jf-iXV3TX8NJioF8ksJdvRPY6P9AV_mvikNOrJXIEQbMBqqNNDaP0mD576Gh3T7kJDDA_zjx3JCXXRoXRYLgj43MTBivRLbhxUeo1S3CwiAbuVM5rRL0CHZQ1GVIwAmV4iuDAj-3Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
👤
#تکمیلی #اختصاصی_پرشیانا؛ باشگاه شباب‌الاهلی پاسخ نامه باشگاه استقلال رو در ایمیلی داد: 2 میلیون دلار نقدی پرداخت پرداخت کنید تا ما رضایت نامه رضا غندی پور رو براتون صادر کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/24594" target="_blank">📅 11:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24593">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kgDQtJV9DFea9eAH5Q8y4VJJxbn1_b5hgE41zuo5JDeznhWznuISnx7mbRuWh4Tus5amsMJyS2NqAHMUEP4IbzJDV6guQhROeT-kZRlBLJokqdJTedWPA_8TUdT9OANOGwYhnkiGtVR4ZPSDrq_iJ5ngfAEoTfGSaOYkmansUBUik8dDkx7ATfXT3C_i72P0XHXF13GCKUq9b2oF-QpqAggkk7VeZXGVmJT-CJyGvTUKeCqKe8qagx5hQEiwJ_drqHTTEcqWEJ5U13XXZkpIQPQEwpKCDDX046KI4YwVVnt5m8Kq-R7OBHolaNJrX29TpcPfA2Z5Hc6seQxuClgGLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🟠
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال در تماس با مدیریت فولاد خوزستان آمادگی‌ خود را برای‌پرداخت‌رضایت نامه یوسف مزرعه وینگر چپ تکنیکی‌این‌تیم اعلام کرده و این بازیکن بزودی با عقد قراردادی چهار ساله به استقلال خواهد پیوست.
🔵
باشگاه‌استقلال پیش‌تر باخود…</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24593" target="_blank">📅 10:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24592">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99ad96741e.mp4?token=cfsJ34wUR01obr6Fzc8x7jeYUd7-_qaznD8tY__CMW8qOr4FINRu5T9rGDoAkRO-jLGCxPS3eE78xx7jGi9uCJrCIb_IH6dqe8eU_LgtNMnBzYnzTVrlrkVgj6FGjE1uadGcDGLGqnsgZg1l-PadpKvkUo917NlCPvqy9kSijTPXxq7zuCqoOEoIQ9xe1OeT2HDjSTFkBZxG23AREB19M3fQ-xsgZrtclSJASdTj6T8rdCw_KHzTIDIjExcGGmuSLqWLwZJhT2Iv_8pcDaOOD1fAIuCyyGGSUTcoGcHDfq7qmo47-nKTH17jw-owv9h-oMs2d-gdYl2nLrkARGLyXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99ad96741e.mp4?token=cfsJ34wUR01obr6Fzc8x7jeYUd7-_qaznD8tY__CMW8qOr4FINRu5T9rGDoAkRO-jLGCxPS3eE78xx7jGi9uCJrCIb_IH6dqe8eU_LgtNMnBzYnzTVrlrkVgj6FGjE1uadGcDGLGqnsgZg1l-PadpKvkUo917NlCPvqy9kSijTPXxq7zuCqoOEoIQ9xe1OeT2HDjSTFkBZxG23AREB19M3fQ-xsgZrtclSJASdTj6T8rdCw_KHzTIDIjExcGGmuSLqWLwZJhT2Iv_8pcDaOOD1fAIuCyyGGSUTcoGcHDfq7qmo47-nKTH17jw-owv9h-oMs2d-gdYl2nLrkARGLyXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شمامصاحبه امیر قلعه‌نویی درپایان بازی امروز با مصر رو ببینید؛ از اول‌تاآخر این مصاحبه سم خالصه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24592" target="_blank">📅 10:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24590">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uUm_es0C3YyfPgmjrkG9QszakSyR0Ma1Z46myKSBwbL55Q7js88aNH8G7pZqsPklMLGZZMdcV6j_BdaVQijNwnQ6MMncsyTfeHHDEUmUSicXs6w_t0dZpRkXOD3lijSKBwyfpX6QnjNOH-RF54ValFlVHHycGqnxdNf_1OhbjXgVr7nOWl718th1Nxx9p7CXJZDUAjtu6ZrP1fD7W3FyW0X63yQQsMJ9wbJj2W9uKS2n5MI5k8JqvPv74zpG_yxrY71TMk926J0AGdaYSjkB66Ke3fXWmBfce05guJLLJkShGRTRbLGUEKYOSp9YdT3r1cw0W98DyY9OrGASrdvgBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رسانه‌های‌اسپانیایی: هدف اول و اصلی مدیران بارسا برای تقویت‌خط‌حمله این تیم خولیان آلوارزه و درصورت‌پرداخت 150 میلیون یورو به اتلتیکو قطعا این انتقال انجام میشه. حالا اگه یه درصد این انتقال انجام نشه گزینه دوم بارسا هری کین 33 ساله است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24590" target="_blank">📅 10:32 · 08 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
