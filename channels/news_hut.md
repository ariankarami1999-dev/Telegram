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
<img src="https://cdn4.telesco.pe/file/JkcmrJKE4WdavYJdmHBxrv6Bp0Ih1wPm_zhMBBiRFxmXFdPqKrI9Hs0LCRTbuq8jmWGp22wmfaoB3QSUCokxRQ07kOUj-ewfSbbRmZsDtXP6cX3ZPndaEVi3mPtQ2XCPq5AXkNs7uewLNks24EURkn-RKCAmVHsbaxrkp52rAQqFyZeyI-WXCASKY5_pR8nTMfK86EAWJM6ROudzAKsJbDONWA8CVQ_N0GEF_S4x-iMUEzMSgfjhBT0FO7rsKRfYXtcxYqh9CCHPAw2i9cax9DT-HpWaLWevug27rAtM_IeKlzX042F87o2dKfrZlkTmbsm1GEl7YxRJKGEpGif-rw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 201K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-15 15:51:24</div>
<hr>

<div class="tg-post" id="msg-67378">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J__UM0vRWzdUx8buMz0w6fTQXWoC-BtIi5aquNRBkQz2XKksehrJZgfTpZeHKGGJAHH8vNrlDVHZ5F_q02_CFeAsBIINZZRPDq8Eb9BYSUVSaxSrMArJKkoE3kuhIxbY-n_Wbi6MK7FoqM9_1xXe0jij0qkVA59zitYTL-XfFnKtAmWOVth4Dj60wQReJTyiQ73UfyDy2JemZLchNBlENl4Aig6IlA70KIV7T7bIvLSCTnMnlKA4uTckwAhXRPOO20yX-S9LkX3xa_UfXSPl7_U6KM5q5PffqpQpETedSxWgIEOKdgCWqzaflnoVPmo5_f2XviNJACGTY7dMXaTAvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
واسه کشتن نتانیاهو وترامپ 100 قطعه زمین 2000 متری جایزه گذاشتن،آیدی رو هم زدن اون پایین و گفتن انجام دادید پیام بدید
😂
@News_Hut</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/news_hut/67378" target="_blank">📅 15:28 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67377">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E93PNiVU_9hhOJCexaJcs1_s3yy62SMIQXJMdX1lvOHEdgjOADHvM42atm04YT90mU0AeUMX3IXhWeWu2Q7s8M7tlccmTDs7nvHbkDMBwuuzKR5dKRVGCTGvxKYyz_T3ARxyk7h5cQVxacbxU5acOrcX1B_jKyhf9DFi0pZZP3wNrQmtygc_cAeJKk179jbG5jIgwH56QDgHClR9p4pMnxhFSG100hxVLqHOL38t-Ar4tWrZY3Zlvq7DH4lznphiUHmHZCWT0lh2WJJ8eLhkbhWy7O45-BhTQLHXR2oXsECdD7UTz5x4Vhu0qH5_yLu0vbI9SCt1Jf4M_t0aEz-OdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دو حمله پهپادی هدفمند اسرائیل در جنوب لبنان.
@News_Hut</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/news_hut/67377" target="_blank">📅 14:56 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67376">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZWjtWBUPbO7Ui-NAOQmhny9_Cq__42jgHDoI-ZQ7CcBMoDXpAS3dg0LtJIThAbFHQ1bEzKLRX0eoRqiFLvrIGBQ4ygHg7vSgLy92y3RETBU-YEkrq7hz2_Je5hwLl8D4-IV8An9cZsZefhqGWWlqje_FKeOIUou0kvml1sbrky-YYV1Ng3Ise2J23NtK9-GV86iVFS0mjP0F4uLBmHKxRFv51yjITW5-64Bo8Zj2wYh91szAGbxOEykaDSdiQl4shnihcmCMR08ggE2orKvU87jMnb7dzn2hzkqCi3vlrMgvzCnlMGEhWf7nMH_5dxvibbovah8CEf2LHOzp3MR5nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏شبکه ۱۴ اسرائیل :
سپاه قدس واحد جدیدی به نام « یگان مختار» تشکیل داده است که با کارتل های مواد مخدر مکزیکی و آمریکایی و همچنین ایرانیان خارج از کشور برای ترور ترامپ و ژنرال های آمریکایی همکاری می‌ کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/news_hut/67376" target="_blank">📅 14:26 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67375">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mW7Z8yWGz-97GTyWZj9uziA2dqsMLHsUFd471aia2isyuBEFBrKjeJdD-5GNDfvd7DYOpS6Nhpc1e-KgPB8yEQPXJvXRJWj41kh1iUqlavpGL12Gmqctn-zXHS6LyYAYPDH9plJN3jbiin9eHqm1J1oCok4C8HgjNoTSb3FhgJcZvK6e6tRQItJae8seYWld8h1SEpZyc5ay48KCwcaALOrYAwjfzH5SxDoO8IDquBAFxwk7iw4f8YDPoapri2UA6ynwCEJK_7LTBHJCf9JneZnp7UaZ81tFjBhw5IePgZBb_cKtIiaUlwdTvT_ur-JaiZbKDpTSv_L5aKhZ7gecww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یک بنر در مراسم:
دونالد، نابودت می‌کنیم! از توجه شما به این موضوع سپاسگزاریم!
@News_Hut</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/news_hut/67375" target="_blank">📅 13:47 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67374">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fvCkDSZ8O863B7T78ELG3EhQzhDfvnNJQSnpR4h0jE4soCC8mrfgK0yjBGzrr2BBTMx5ssu5gdazMGqRyL8jCwQOvGwURNXnNQc1inVeht6fzr3tOLfBMX1HFuFu5LK56h46HHT5iY_3EbfSosbttSEHhHRNvH_Er04azq-hTL43VfctQu5o07mpXVW_35lwzR3cY0KdwXCPMvR4eaRdSmRqaQ-mh2xyxc_GOU_hh_nwL9Lwh1Hp1aAHfoFkxfUS05ulbDEKLr8a3VvE41hiI8f7vieMIoBzKOfWcRXFYNHPNgzfLfqH-tS3RkfJda_aqgS3A-OB4JLAWII0FRn8WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
ادعای
نجاح محمد علی کارشناس عراقی مسائل خاورمیانه و از حامیان نظام جمهوری اسلامی:
در مراسم تشییع امام سید خامنه‌ای رضوان‌الله‌علیه در تهران، فرزند ایشان، بقیةُالسَّیف، آیت‌الله سید مجتبی نیز حضور داشت. او پنهان نشده بود، بلکه در جایگاهی قرار گرفته بود که کمتر به چشم می‌آمد.
هماهنگی بسیار خوبی با نیروهای ویژهٔ امنیتی و فرماندهان ارشد سپاه پاسداران انجام شده بود…
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/67374" target="_blank">📅 13:13 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67373">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fssQ0jhqkUsS6dfJyUxUUlXdDK6hYuhPFnmDF9V0mRTIY4F8cH4KoeyR0LapBV_yHBg2t5AgfsuRxSG1odzogHO09x9fLrVZ_GNaNKMPhQlOybzYVneZagPykJ1dFRHuO495tPqupZgwqIhxFTkPpMcrqUVVMlISJyOTc_yFTYtO4vmUjqJIIeaFo2k5pBRAqo_9xtqQzYZlQtJ5NSLIv_owdN5e76fYo-0A4OqQYnHQNx2KMPYOnXwmd7NO7dsBszJNwdFq3twDz3AzTHAymX2DmpwoUdZlA36NOqJQSer-ctKf_1Elo8EIxdErY-7cCC26iavtENrB5Dtb4XaavQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇱
اسرائیل کاتس، وزیر دفاع اسرائیل:
«آیت‌الله خامنه‌ای که مراسم خاکسپاری‌اش هم‌اکنون در حال برگزاری است، توسط اسرائیل حذف شد. هر رهبر ایرانی دیگری که برای پیشبرد طرح‌های نابودی اسرائیل تلاش کند و اسرائیل را تهدید کند نیز حذف خواهد شد.»
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/67373" target="_blank">📅 12:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67372">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22aca7392a.mp4?token=bMm_uIC3uyHZHav5t3dtz-Wq8vZjgftGvn0ikf1waiCSGzaH1sja91aLTbQC2YiXYro-yiQSG6mRVmLT3eQKRMzrnfxpmMlSUmWBXQoNgRMjnzUK9XQOStCjHimFyHw73IchXqeZe0HCcMVlm8DSTWTqOUVmmN_X1Ohjg3scFOtONwrRCu17nAuE2q4V4O6B3nctdv_cZJOsw3m8FqZMzaMHTnZ8LlXisQ4asfYKQfgBPS1p9oYP6cYMKCWHoainT6C1_rssRa7h2ITsBgSxgnsGU2PxeXXTFTPjRFlagRnbFy5SjMS94xrqxJ9VEZdf6IauQokNO4AJxkICUgXeBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22aca7392a.mp4?token=bMm_uIC3uyHZHav5t3dtz-Wq8vZjgftGvn0ikf1waiCSGzaH1sja91aLTbQC2YiXYro-yiQSG6mRVmLT3eQKRMzrnfxpmMlSUmWBXQoNgRMjnzUK9XQOStCjHimFyHw73IchXqeZe0HCcMVlm8DSTWTqOUVmmN_X1Ohjg3scFOtONwrRCu17nAuE2q4V4O6B3nctdv_cZJOsw3m8FqZMzaMHTnZ8LlXisQ4asfYKQfgBPS1p9oYP6cYMKCWHoainT6C1_rssRa7h2ITsBgSxgnsGU2PxeXXTFTPjRFlagRnbFy5SjMS94xrqxJ9VEZdf6IauQokNO4AJxkICUgXeBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حضور احمد جنتی در مراسم وداع با جنازه علی خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/67372" target="_blank">📅 12:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67371">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ad63d7f30.mp4?token=s0ojebqwmOEJIVoNOhdlt0q7QiDD_QJJpWXhLI35dH73Zt8D4vhzgcRSI7goTzfCgtzvuIW_0hE7XBNjukN2mpbIlQMzbxfYpYwz3JJBNoN53ZD2HsvQcOJthe3y2wEXOG1BfU5q3xBKotsjQuRB8-sgEab5OqaVt7KMNiZK28a2VCdly_q7x7AJZOtL9jS_9Ev9asDKFqB91xb5WxWuIhbvTfgKBkRnkPp6g57U_XTYqmcPnPiid-X76Oq22l8M2tS9YWkaBFNK-KWLBYpsaVhnPgAwdKXw2JyshkPnkTF74Co_WJ6fLoUQY8G1SHrTUFe9aMYmoPMSvci4coZawg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ad63d7f30.mp4?token=s0ojebqwmOEJIVoNOhdlt0q7QiDD_QJJpWXhLI35dH73Zt8D4vhzgcRSI7goTzfCgtzvuIW_0hE7XBNjukN2mpbIlQMzbxfYpYwz3JJBNoN53ZD2HsvQcOJthe3y2wEXOG1BfU5q3xBKotsjQuRB8-sgEab5OqaVt7KMNiZK28a2VCdly_q7x7AJZOtL9jS_9Ev9asDKFqB91xb5WxWuIhbvTfgKBkRnkPp6g57U_XTYqmcPnPiid-X76Oq22l8M2tS9YWkaBFNK-KWLBYpsaVhnPgAwdKXw2JyshkPnkTF74Co_WJ6fLoUQY8G1SHrTUFe9aMYmoPMSvci4coZawg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیوی عجیب منتشر شده از وحید خزایی شاخ اینستاگرام با سردار رادان که میگه کار دارم با وطن فروشای لاشی،ترامپ گفته گوه خوردم
من سلطان دختربازی ایرانم ،حتی سردارچندبارمچ منو روی کار بادخترخالم گرفت ! اماخداشاهده آنقدرمهربونه،هیچ کاری باهام نداشت و ولم کرد
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/67371" target="_blank">📅 12:04 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67370">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a17dafc375.mp4?token=FzyEjmjiQV0df-pqQlfMETuJyKXdLlwoO-HdITmYi4BS7J6F57c4p82ZKkwSce8EXW2rDk2O60-cVziNHytelnQGQoAZGLC8a4i807wGNxKxdUkRQz8uk-48Xs76T1Siy9-49Dx2t0-legX_dCzFPnC4kgUg0eMbsktqoQEeKDHSD2jSk-o0W0iOKjhwFpmyWkAbnu71zC99GbNnW9VAu_BNxHL7ftW492KivQPlAjl0zYKEl4rT1AmNgU5EDC9mR4goYsecEd0CsP2DKOIyloe9FOAuSS6ajnZW8uUJilGfyVdFksLcnRJ8jIlU9lyZEDiWdBvsqJ6ewg8pj80ZDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a17dafc375.mp4?token=FzyEjmjiQV0df-pqQlfMETuJyKXdLlwoO-HdITmYi4BS7J6F57c4p82ZKkwSce8EXW2rDk2O60-cVziNHytelnQGQoAZGLC8a4i807wGNxKxdUkRQz8uk-48Xs76T1Siy9-49Dx2t0-legX_dCzFPnC4kgUg0eMbsktqoQEeKDHSD2jSk-o0W0iOKjhwFpmyWkAbnu71zC99GbNnW9VAu_BNxHL7ftW492KivQPlAjl0zYKEl4rT1AmNgU5EDC9mR4goYsecEd0CsP2DKOIyloe9FOAuSS6ajnZW8uUJilGfyVdFksLcnRJ8jIlU9lyZEDiWdBvsqJ6ewg8pj80ZDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وحیدی فرمانده کل سپاه با موتور اومده مراسم
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/67370" target="_blank">📅 11:34 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67369">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abfc46c7e6.mp4?token=jzEZOSoAotmv2J8cQkgJ1Y3IKq4RpbQKhlxGPwaH_gCiquI_lwXdOSeM9tDwRYFFIHPuN8ntAXB49PMG1s8dedNX2AlD-_pJttkbtgLTUGLtRNezGLJ2AF2qvZiG-mhtbrGLqQNOemSviKgAOYPCq2vFEmGqinGnVtd8HfZgQbWWyV1XSJOlK5T34lafiGSu5xyQV82Ox6vdp7xcv2kbuUVjVJ_JQksIm9-bF7TJuDdZJeCRQBKRJ92St7Y0Zc3Z6kcRl04lE6sgrRPzRDW1CCIzzMlFrnYX7fqdWIdzTj4X7SMDedOUiZOxXqQTT3vGXnY-hZ01cADtnUH2B9qrng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abfc46c7e6.mp4?token=jzEZOSoAotmv2J8cQkgJ1Y3IKq4RpbQKhlxGPwaH_gCiquI_lwXdOSeM9tDwRYFFIHPuN8ntAXB49PMG1s8dedNX2AlD-_pJttkbtgLTUGLtRNezGLJ2AF2qvZiG-mhtbrGLqQNOemSviKgAOYPCq2vFEmGqinGnVtd8HfZgQbWWyV1XSJOlK5T34lafiGSu5xyQV82Ox6vdp7xcv2kbuUVjVJ_JQksIm9-bF7TJuDdZJeCRQBKRJ92St7Y0Zc3Z6kcRl04lE6sgrRPzRDW1CCIzzMlFrnYX7fqdWIdzTj4X7SMDedOUiZOxXqQTT3vGXnY-hZ01cADtnUH2B9qrng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عباس موزون، مجری صداوسیما:
چند بار [روح علی خامنه‌ای] از بدنش جدا شده بود و تا ارتفاعی بالا رفته بود.
«اصلا بعید نیست آنهایی که علیه بشریت عمل می‌کنند، از نیروهای شیطانی کمک گرفته باشند.»
چی میگه این
😢
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/67369" target="_blank">📅 11:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67368">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hCGmu_G7lKVEjBQbjDGNK9EKoiF3o8wE6vhI4efs_lNVrll75pb1C4rfdBxML7TqNjIDRhyg2IYrn_W_0HJD9y1R2fhT0wJu3ll1O8fVwPP7rf4f-Zrj8lVybwQFx7axDUeHhRR8UeJtqmSv64ahdeDjuF4pUoghUzyyi4Hp8EuKIXd1d9ESKWmVizX0bKH85qFNSRWzIHMc3RY9sGaQVb-olUEhLfVjwYvO7jZELGfMKee8OR47shZ5RQwwBV1674VzyoSW-1t4KjwtviJLdjE96YE5l12D5jT008uUTeljloE6syj1lZoOnBFmyiSY0rVIs8I3p4-1YXpsFWbc8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اکبر هاشمی رفسنجانی،24 اردیبهشت 1370:
سری به بیمارستان زدم. آیت‌الله خامنه‌ای مشغول صرف صبحانه بودند: خاویار و پنیر
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/67368" target="_blank">📅 10:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67367">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38c47b7b97.mp4?token=cBttqZZX1RASI2Xd7kLdGcBk0tte5siUZsGK2kiPnPF6q0l8kHina9hDDGF15HqdxWQOCXedK2XgGklhADwHF5o1F49ZaUOSYbelKG68ESPGgdJrTj9d3wD6wx-x3wiTbDbhcPRKp_UFD0OgBHoV207KYrqJfbesY_ofgYzyATksXScb15fFQPoKGfqvrau79t5rNRXbeLnecj2hJWPc5ENVC7XkNHpTFn9jvalkfT85z4lPhZ7sJLwoc6LMgSNZtGRHV1w9zJfpG9UYvZTeG9Tt4ffgCt8u6qTjYdyoaTY-BIo8R9pHGmW1PFR3kIOVBgNdoucAcpphVRzlFYiZhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38c47b7b97.mp4?token=cBttqZZX1RASI2Xd7kLdGcBk0tte5siUZsGK2kiPnPF6q0l8kHina9hDDGF15HqdxWQOCXedK2XgGklhADwHF5o1F49ZaUOSYbelKG68ESPGgdJrTj9d3wD6wx-x3wiTbDbhcPRKp_UFD0OgBHoV207KYrqJfbesY_ofgYzyATksXScb15fFQPoKGfqvrau79t5rNRXbeLnecj2hJWPc5ENVC7XkNHpTFn9jvalkfT85z4lPhZ7sJLwoc6LMgSNZtGRHV1w9zJfpG9UYvZTeG9Tt4ffgCt8u6qTjYdyoaTY-BIo8R9pHGmW1PFR3kIOVBgNdoucAcpphVRzlFYiZhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زنده یاد مانوک خدابخشیان:
خرافات پدر ایران رو در آورده.
آینده ایران در یک جمله است؛رنسانس.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/67367" target="_blank">📅 10:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67366">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33573d06e9.mp4?token=rCU-rqqHnRDqzmN6-q6xiHygvmHiJKusNZPs--WBKhdmFptLSl4HnmCIclBFSorki9XM6f0RRzXun1XtUktd9EZkMFNv4tXelU1AA9bEJZ2pEhfcpu9wYmQBiMg0HoBs7H_0qmTZz4P3bPhiWAZNH9OO8GLCAYnimJ30s59CSl8w3phkJ8zjl1BdANuXvUYNKqo1bdMioWVCqfgiuRIf-FZK7lXzqH_mo0WMpP8n7liODLuA7Y2kn61Us3NkbPaZrYdvW65otJ-nA4Y9NZl1z6gG3MZejfoNwi4SufpSd9mQX13DkQTsTghcb0cr4e3YUWEnUMLg4l9q9nwZl7VozA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33573d06e9.mp4?token=rCU-rqqHnRDqzmN6-q6xiHygvmHiJKusNZPs--WBKhdmFptLSl4HnmCIclBFSorki9XM6f0RRzXun1XtUktd9EZkMFNv4tXelU1AA9bEJZ2pEhfcpu9wYmQBiMg0HoBs7H_0qmTZz4P3bPhiWAZNH9OO8GLCAYnimJ30s59CSl8w3phkJ8zjl1BdANuXvUYNKqo1bdMioWVCqfgiuRIf-FZK7lXzqH_mo0WMpP8n7liODLuA7Y2kn61Us3NkbPaZrYdvW65otJ-nA4Y9NZl1z6gG3MZejfoNwi4SufpSd9mQX13DkQTsTghcb0cr4e3YUWEnUMLg4l9q9nwZl7VozA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو مراسم وداع با جنازه علی خامنه‌ای، وقتی نوه‌های خمینی میرن جلوی تابوت سید علی خامنه ای، قاری این آیه از سوره نساء رو به کنایه می‌خونه:
آن گروه از مؤمنانی که بدون بیماری جسمی در خانه نشسته‌ان، با مجاهدانی که در راه خدا با اموال و جان‌هایشان جهاد کردند، برابر نیستند.
اونا هم برمی‌خوره بهشون وسط آیه ول میکنن میرن.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/67366" target="_blank">📅 09:30 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67365">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/InBe6CyMcedOzNWnh8cTop-GOT0XTTR4aUzGS99NfZwPrD-6dWJkWz2sjc6996UWW7NNnQZEsmRRuwJQOe0jE7ElFI6TzONmlQ101p8Ui31RUQNIXia1rnn7RMmYzBGv_FcdyXAjXSo-n-jHeEbQLG69QhZy9PC13MDg5YXo7BTkRuOhxpzjjSPOGf9r9ZaXQ6jxuWBMKdE2mz9Gg7D-QP0ARSc_1Q45UzgQiSwXIDUf_h5N2hLuGk3vt4l2oViNq9vgoCE4DIP06b7gN4trAV7HfYTu3De1kZXxHm4uGwv8oQX9xGtI60edh1mmPbLNEuN2AyZR-ICdOC7OywagHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
قالیباف در گفتگو با محمد درویش، رئیس شورای حماس:صلحی با آمریکا وجود ندارد و اسرائیل را به رسمیت نمی‌شناسیم!
🔴
دیپلماسی باید در خدمت حفظ و تثبیت دستاوردهای نظامی باشد.
🔴
مذاکره زمانی موفق خواهد بود که کشور همزمان آمادگی دفاعی خود را حفظ کند.
🔴
ایران بر حفظ تمامیت ارضی کشورهای منطقه و پایان جنگ علیه متحدان خود در محور مقاومت تأکید کرده است.
🔴
جمهوری اسلامی صلحی با آمریکا ندارد و اسرائیل را به رسمیت نمی‌شناسد و حمایت از جبهه مقاومت را در قالب‌های مختلف ادامه خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/67365" target="_blank">📅 09:04 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67364">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67364" target="_blank">📅 03:58 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67362">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Kb60kppNtGUbRxgL1M0jKjiAdO22VNs5mlwzt8WUtf3pAZLVoOWy7G92d64OKOg-cFL_RtjQBV0QRP9uQjSGH3wTuzzoU9XABDOc1RIBp18kU9p1tBAV37TVgnIgG5n3oSC2z5E1cw_ugP1PR4d_qf7Movvx2vmNXWkv9INkZA15yb51ObV6w8UZAiVRTBr-viY5ymilp9dIS135sTTP8kI7FAe3c1KvTgp5C0TbdIvp7-oeIdmIA_ugtl7mUujIF7R1NZsIPYNS76Zz1qvmfldQcBnlZXppwJxKySyOAQEBmkXKNbX70etdE6y5KtdSVWLAPxOpWq8rq8mQqkQn5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67362" target="_blank">📅 02:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67361">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a1fe48304.mp4?token=WxFit6KpQSLJQaiTdnpj3tWxZOIHlpc29-8ALtwJNHayqytyztfrcU9sW2W99q98AEUX-oaL4yWd3l6Rb65e59tQKMd8NmxwAJ_faW-QX3mZskNWmE_DgmQcL1_JNLNsscmBq9i5m5-a1is2Q_ursuKm-yO9bRz0m56MzOLFRRv5oDPMxSHvIijQ1nab5rIBtXedWVZynvpNj3OChxXatr6rphRMbR-xOa-UBIvCzPek_lsN8ZlMWD9RfOpxpXLKl8JoxvqAZByFd3S-hogPaKe7_puy4ujn00xwD7dV0KPvzdZmHzOCBJrpdosogE3cCZaEn8SdHLv4Grvtetz2Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a1fe48304.mp4?token=WxFit6KpQSLJQaiTdnpj3tWxZOIHlpc29-8ALtwJNHayqytyztfrcU9sW2W99q98AEUX-oaL4yWd3l6Rb65e59tQKMd8NmxwAJ_faW-QX3mZskNWmE_DgmQcL1_JNLNsscmBq9i5m5-a1is2Q_ursuKm-yO9bRz0m56MzOLFRRv5oDPMxSHvIijQ1nab5rIBtXedWVZynvpNj3OChxXatr6rphRMbR-xOa-UBIvCzPek_lsN8ZlMWD9RfOpxpXLKl8JoxvqAZByFd3S-hogPaKe7_puy4ujn00xwD7dV0KPvzdZmHzOCBJrpdosogE3cCZaEn8SdHLv4Grvtetz2Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
ارتش دفاعی اسرائیل:
پس از فعالیت در نزدیکی نیروها: ارتش اسرائیل یک هسته تروریستی وابسته به سازمان تروریستی حزب‌الله را در منطقه العقیده هدف حمله قرار داد
امروز (یکشنبه)، نیروهای تیپ کماندو یک هسته تروریستی وابسته به سازمان تروریستی حزب‌الله را که با موتورسیکلت در منطقه العقیده، در نزدیکی منطقه امنیتی محل فعالیت نیروهای ارتش اسرائیل، در حال فعالیت بود شناسایی کردند.
فعالیت این تروریست‌ها تهدیدی برای نیروهای ما محسوب می‌شد.
پس از شناسایی، ارتش اسرائیل در یک حمله دقیق، این تروریست‌ها را با هدف رفع تهدید هدف قرار داد.
ارتش اسرائیل به فعالیت برای رفع هرگونه تهدید علیه نیروهای خود ادامه خواهد داد و به سازمان تروریستی حزب‌الله اجازه نخواهد داد به شهروندان اسرائیل و نیروهای ارتش اسرائیل آسیب برساند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67361" target="_blank">📅 01:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67359">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WaPT6RWhqkjXN-jyalnLJmnY73C10zKmf_aUKn0nCBhGp_M8m0GyscTMAzmfOe2ER8cw7QU5yrriXAN2Oi13jnnllXjTkrGkwf2ceUXWHCYTEtlwQ_OzoMERXimQA_5nx8xyUFQd1dakNrpE8pnibOgMtpsYfYynwmLoV4rdZ-Wdeq06MZD5qDlFkFnt4RPV-LOXVUaSh35a478xG1PnE1hGEEIUx48VVbt68LTUNOdar4QtnlCBuN6e2SoXm3uhCPMrUYB-83wG4HC7FnuI1FAeOGwA_o2c3eKsyfiWa0nTayBnSooBChqjkX0BRPnGYOecb2EyNz1RYb5DDbhCeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کانال ۱۴ اسرائیل:
انتظار می‌رود نخست‌وزیر اسرائیل(نتانیاهو)هفته آینده برای دیدار با رئیس‌جمهور ترامپ — که هشتمین دیدار آن‌ها از زمان بازگشت وی به قدرت خواهد بود — راهی واشنگتن شود؛ دیداری که در آن برنامه هسته‌ای ایران و خرید احتمالی جنگنده‌های اف-۳۵ توسط ترکیه در صدر دستور کار قرار دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67359" target="_blank">📅 01:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67358">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6d2fa6e6a.mp4?token=jWJ6SorMn5Zr-SwtbwPjVbeY6MCOlB95OLobrHAb-5YH4ZW8z5ekY3k5vPzJEBt37wbmcPoPgmTG2c-CzE24705AeS75jyInVyrEmCa_w1uHxuqZ3oqE6WS3x_3_ok0yqTCbcsHLBVMKHZ6GB5QVtQrTtzRWPuhh6q82VBmDpl2rQWSYRzEqStcj646jAFjHGGVJ7H2VbIIkhKNEJN8a0VTnsRZI-3uccJuuMR2Qg6y4_kuukABofHwzk1A1diOJiCUi9N3m5vQbJZVw3soUPa1FEaHDMSgkcj4wo0jGmBiFS_iaBYLQu-XPCJnDrYBU9g3N_KEz24PyQKLQdBq2dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6d2fa6e6a.mp4?token=jWJ6SorMn5Zr-SwtbwPjVbeY6MCOlB95OLobrHAb-5YH4ZW8z5ekY3k5vPzJEBt37wbmcPoPgmTG2c-CzE24705AeS75jyInVyrEmCa_w1uHxuqZ3oqE6WS3x_3_ok0yqTCbcsHLBVMKHZ6GB5QVtQrTtzRWPuhh6q82VBmDpl2rQWSYRzEqStcj646jAFjHGGVJ7H2VbIIkhKNEJN8a0VTnsRZI-3uccJuuMR2Qg6y4_kuukABofHwzk1A1diOJiCUi9N3m5vQbJZVw3soUPa1FEaHDMSgkcj4wo0jGmBiFS_iaBYLQu-XPCJnDrYBU9g3N_KEz24PyQKLQdBq2dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو ای که فرستادن به صداوسیما از لحظه حمله به خونه نتانیاهو و ترامپ و گرفتن انتقام علی خامنه‌ای
😆
😆
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67358" target="_blank">📅 00:10 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67357">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/237c10defa.mp4?token=AlsN1BKTid6YKlGhg_i7FbS9ltXuECCvw9grH_o5rIKpR92RfRG_n3MjCBZxQeuf3ivOJcUe93e_wXcp4dFPrEPtesE6582qMmBh1imaD7eNyqIL1fXWAzUETVJJvIDGNu6JBMRaXP0hpmkwGgT30u-hH-GfsVfYy2VSkCWQp1PdPKaIZl3FfxIPpgfH8Xxu0zrQSsP3u3x7Zpo_wOc5X-UT1l_FyXq55otUMEAgrg653hvoMrcZD6L8KuGS_Gig-SBWvGsRJjo_5epeQW-VvoQQHmPGBJXuwYW2326Z1gww8ROt5NLOjfkXMVMtvbASx4KgC3ZhG9l8p3mQ5bdUGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/237c10defa.mp4?token=AlsN1BKTid6YKlGhg_i7FbS9ltXuECCvw9grH_o5rIKpR92RfRG_n3MjCBZxQeuf3ivOJcUe93e_wXcp4dFPrEPtesE6582qMmBh1imaD7eNyqIL1fXWAzUETVJJvIDGNu6JBMRaXP0hpmkwGgT30u-hH-GfsVfYy2VSkCWQp1PdPKaIZl3FfxIPpgfH8Xxu0zrQSsP3u3x7Zpo_wOc5X-UT1l_FyXq55otUMEAgrg653hvoMrcZD6L8KuGS_Gig-SBWvGsRJjo_5epeQW-VvoQQHmPGBJXuwYW2326Z1gww8ROt5NLOjfkXMVMtvbASx4KgC3ZhG9l8p3mQ5bdUGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه پهپاد اوکراینی یه سرباز روس ـ افریقایی رو تو یه مزرعه تو شرق اوکراین بدون شلوار حین دسشویی کردن گیر اورده و افتاده دنبالش
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67357" target="_blank">📅 23:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67356">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nhJBO20txXNK-eJMxl80OtCM6OkOkmy1I5mIrlYyCNMLXudaDRCgz6kruFnNLrWuypjbI8HOSlwOMeQ3333R86WLA9sXAnxmxG0h5ZHymNV6iiP59HkHPv8b7S09CWB1qKZ6P8ysTOhezXL4PAml1QXgr639F4Rjiq71cJYkmCSakrtSSbRs8N_Dlem9S0_4UrRY5tZdxhOHxt1QJOpe--UBEraHOCLW4y93CUL-g2GxgCoQ6AjUoYood3H0qBbIJBcwdTyEKZRrWqTjiDUm52ou83HnGk6shSZkygK2p34opp8IgVVyiK6yXvtuhNchO0bU6XUDC_pwbZVU_z9q2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سنتکام:
یک چترباز ارتش ایالات متحده اعزام به خاورمیانه، آموزش تیراندازی انجام می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67356" target="_blank">📅 23:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67355">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eb140a8f9.mp4?token=YvjmhSZihxA0-FIuLPRtNpkDKdN-GGgbRnHTadgUbqglH_hSM5Yh5Zc7nuiS02kV8lHtJ_bxaGeVuzBJoeESxARa_TMJKSgOMzXbYRJ_q2R62O9Hrn9e_x7hcRFg8qNSni4v183VMK592hdLhe4dCE5QCxemt9rwsFSHa9SFbKA1JDOdwKTJ75pGl5oXCpL33v_mIDxVF3X9yFwaM3lDEl9K__8j1iA3_Xospyj77X2mLYDLvgL_nxVHMAk2Mau60IYtg1OxzTIroXeasATcCnyFmXROQ7yyTuE7yDdHUcV30KG3ylrIDAzMqk9UMpNP4OrrayzBsHyMzR_I4_dlSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eb140a8f9.mp4?token=YvjmhSZihxA0-FIuLPRtNpkDKdN-GGgbRnHTadgUbqglH_hSM5Yh5Zc7nuiS02kV8lHtJ_bxaGeVuzBJoeESxARa_TMJKSgOMzXbYRJ_q2R62O9Hrn9e_x7hcRFg8qNSni4v183VMK592hdLhe4dCE5QCxemt9rwsFSHa9SFbKA1JDOdwKTJ75pGl5oXCpL33v_mIDxVF3X9yFwaM3lDEl9K__8j1iA3_Xospyj77X2mLYDLvgL_nxVHMAk2Mau60IYtg1OxzTIroXeasATcCnyFmXROQ7yyTuE7yDdHUcV30KG3ylrIDAzMqk9UMpNP4OrrayzBsHyMzR_I4_dlSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خایه کنین؛ توی اردبیل چند تا آقا نشستن با یه خرس نون و پنیر میخورن
🗿
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67355" target="_blank">📅 22:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67353">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bsAvuRmsWZ7Ez1ViAqQ4ezqi1_AzXyhSpR3NF7sKuYAfIRsDR14bFkFIzGGSXt7FK3VtDwDAyf6iY8vL6Pei9Wjk0iZajy57Ewuf20bsqw5FkKYwefgKVrucJTyCheSLRqikXRSJLcXxOc8XWqHfuOXztkd8F4E7iaIBNe91NyXKu-jjoY8ycERJqLaYvkqJNB4ke5IgdobjTc1t434T5EqER0oO0obUM65gdub4UI-4HlW5wk3FdXENxjgB816T_qeGRSutLi089Vuc0y7aFlyGryPidJRZRrZwckV0Qb9FaTPEOXj1yUlV3wWKio_CVkbLsNOib9K_dK4aeVLaNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسرائیل به فارسی:
مثل اینکه مجتبی هم بوده
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67353" target="_blank">📅 22:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67352">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc47a54d3f.mp4?token=tZ5sCffD7WCct99py9GLIs9TDpasW9Tr2jORH_MfxTnwqoyeVRQyb1M9CUeZ7UDIRd8HAJ8oKY1xmiLuVDcK_cMpS5YGDgdUBrm5rq61XI5cUHvP0fqGOkUo24luq4WeFbmajax5J06w1AqZz_JNnRfPsQVWzlF0L6Sa-yr8x4qns2Ypk31xGeqTPOHiZbhr1AQz08d6QD-nCtbmC83YIjTdWmE-lkCTa8cxYMGflcYbKxTkjHQtYlk5SpFLOYDXxHTUzrbnNXHAZwi2uu7KBDPvh-cHLKgqoMyut2_Zq8X6rafxgdqoVilwgonkHoFJbS95HrgpQV0v9ySCWuBbCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc47a54d3f.mp4?token=tZ5sCffD7WCct99py9GLIs9TDpasW9Tr2jORH_MfxTnwqoyeVRQyb1M9CUeZ7UDIRd8HAJ8oKY1xmiLuVDcK_cMpS5YGDgdUBrm5rq61XI5cUHvP0fqGOkUo24luq4WeFbmajax5J06w1AqZz_JNnRfPsQVWzlF0L6Sa-yr8x4qns2Ypk31xGeqTPOHiZbhr1AQz08d6QD-nCtbmC83YIjTdWmE-lkCTa8cxYMGflcYbKxTkjHQtYlk5SpFLOYDXxHTUzrbnNXHAZwi2uu7KBDPvh-cHLKgqoMyut2_Zq8X6rafxgdqoVilwgonkHoFJbS95HrgpQV0v9ySCWuBbCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمزه صفوی :
یکی از گرون‌ترین سیستم‌های حفاظت در بین رهبران جهان مربوط به علی خامنه‌ای بود، اما نتونستیم اونو حفاظت و پنهان کنیم و از دستش دادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67352" target="_blank">📅 21:21 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67351">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
ترامپ:  از فیفا برای انجام کار درست و جبران یک بی‌عدالتی بزرگ سپاسگزارم!  @News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67351" target="_blank">📅 21:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67350">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I4upekQoej-XpbxK0uss2szlCe612a4HUkZ6PZBm4cpAOUVroCflrdQ-AdFjKZnUF45l5TJi110f1SUXcUEhpz5aEKo-VJt9yLHhf2642zHabF-Cse9-GKudFc-Lu6ehEmPY2Zd-mvBjfA0gdKg5Rie_R-I3fC_TOlwKzRni1A_4LMw-IPB02LdKKd4M1oS6RWX7CKXSwt6M2TGNIkSfR4e0QGHdayzQeKs0lFLHrb0Opzf3eQyeGwhf9_ZiTMK9IRK-Hdn5B2CcgvowSKF9_fU4Z9gNSxqfF-rNBbVzGYymVtSzXW2SOB162uV0cVSJjGc742jJb-JcdqFxUqFRMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ:
از فیفا برای انجام کار درست و جبران یک بی‌عدالتی بزرگ سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67350" target="_blank">📅 21:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67349">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d12e972bb.mp4?token=DWNJelCDRgMyxMwGGJzJiBQT3uzKfin-za-RnnibAl-j7VuasWnbCDk01vb9F2W7RA2DlCmvlfwYsBeGuOrKPT5HOAwOJ87nB-WL7a-D_YJNHVLMV0Wl1BNVaZslkRzHutpSzxYyn3dUWRi0ZXxvuyPF4Pbkv67X9YxTlz3GSNSIkWlJSjnBKv1EO5SOfpyJ3jK2peRnztZgU7Osa9EjooTyZ48MEWl7nB19oqJPej79EGgaPzrT75AJH4lklaXGzeu8QZ7fXQzorpbKD4SaJqX9Lpw5NBtV0LGNOzNGBboDuHouttEvyD5WyJw3Kuus-LqXwnSr7ioIoRYLBuMJRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d12e972bb.mp4?token=DWNJelCDRgMyxMwGGJzJiBQT3uzKfin-za-RnnibAl-j7VuasWnbCDk01vb9F2W7RA2DlCmvlfwYsBeGuOrKPT5HOAwOJ87nB-WL7a-D_YJNHVLMV0Wl1BNVaZslkRzHutpSzxYyn3dUWRi0ZXxvuyPF4Pbkv67X9YxTlz3GSNSIkWlJSjnBKv1EO5SOfpyJ3jK2peRnztZgU7Osa9EjooTyZ48MEWl7nB19oqJPej79EGgaPzrT75AJH4lklaXGzeu8QZ7fXQzorpbKD4SaJqX9Lpw5NBtV0LGNOzNGBboDuHouttEvyD5WyJw3Kuus-LqXwnSr7ioIoRYLBuMJRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
محمد مخبر مشاور علی خامنه‌ای:
قاتلان امام شهید به مرگ طبیعی نخواهند مرد و نظام آنها را به قتل خواهد رساند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67349" target="_blank">📅 20:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67348">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5503b743a2.mp4?token=NlWwW7vnuUNIj9uaZ1i5QNOWw3ZP5TbCgS8ZjDGDIEBidndQfb77dnGx25fqXPV3bTafD_dMlVV0hOGmVtze-MzG7u4Ala_laIjGADnlVQLU3_e7AXGNOSoqpYI83lVvAffDCiQ4BhX1QhseulVPg8gUqFBRrG0q_VISZcW0fQFJeTlnXOeQ9_dJe1GsxmArrs1S-pqZpnnAuddg_V1POePXrMqIVmNsQMbuRSHLqJCUk1jYz2ZFyA1FYkxbHXETqnwkdunm5nT2lqIjKXToYfCAzeSqU0l3xlb9Sd2gXpboicfwjkitJGZiMkLmEcmglBxxo1ixeq-ROj55Bdl03g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5503b743a2.mp4?token=NlWwW7vnuUNIj9uaZ1i5QNOWw3ZP5TbCgS8ZjDGDIEBidndQfb77dnGx25fqXPV3bTafD_dMlVV0hOGmVtze-MzG7u4Ala_laIjGADnlVQLU3_e7AXGNOSoqpYI83lVvAffDCiQ4BhX1QhseulVPg8gUqFBRrG0q_VISZcW0fQFJeTlnXOeQ9_dJe1GsxmArrs1S-pqZpnnAuddg_V1POePXrMqIVmNsQMbuRSHLqJCUk1jYz2ZFyA1FYkxbHXETqnwkdunm5nT2lqIjKXToYfCAzeSqU0l3xlb9Sd2gXpboicfwjkitJGZiMkLmEcmglBxxo1ixeq-ROj55Bdl03g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان:
قول میدم راه امام شهید رو ادامه بدم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67348" target="_blank">📅 20:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67345">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cTPhuvSE5b-e9DKIz4S6Ujs4AuqnpllnbBJUFbLFdiwxVmp8aHuNQ8nNhDOZb6LOtCBG2eGRc7-XXejmnHZtpf7rvjdMnWuNgP5UsvvHEf5Y9SZ46QC2vjqvm3Is7L5i6Yi3bF365gBOynE45JT08VYH45QHBWgDIdDQ6ucHIoH_gIkEhQLv7H1-PYevXS4H9qtlHjUMPpfBR3SkKCOfJIfV9uX-eOBmt4Z9abTqr09K4rKVUbUqcfGzUQvJrzY7Sm6jVqmsyLoXYpwUWZBWJRDaQ319iOGptgMPL9Hcwbe0-At66INuixsjBEXNObOAG_kH1M0Icxd1jK3bHmsPEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/egMDAUTfNJgsfPq048HlQAjhMOEq_3vDTYU782DIu8aRKWsfZ2Bc8or4uCLZZpx_QNk6c6Tjm6gMqKbBvhlZ3oZEMyMH5r3WQtxZsFCaj2wqB4yRgFLlwjaeQh1wAtv6VSR5xoL-jqbShCMEeGf9pP796tO4D1xORxmJOoX48wG08tdy-_XS3U_G5tNfXMndFO-OG_Y7em5ErDm7y6bGSks6z035HfkIxIDK2mVRTsozd51NpekccUJchgKhGaytOOgfUwTJ5UmTvV3vA9T8T2cIwKiueY26YJzvmCSasRgW2P49ZidunH2HGerzdnGTuXvUHZO_SAjPCRntm2KeEg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a975887416.mp4?token=U3joaOb4oAOtMU2e8Q0Gpd8bxV6_6P9Lztz7se6R9AL2XuWWYMNX1limuZzcq3xZjrfy3HfSicWaT8ZSmmT-mHfSUD3P9t2im2ngvpptnKrO27na_9vfftg_zXDOD3p6baIge0ujY7zuyifkU1UYwFFEHjj-FyZ5jZTpwIynzLxuS6liN53nCRdmWGRvH0uI38fecQX_gn8EDMak1rJS1XoAH6s4ORH_91VbEV60S4Dx5RZdInVNhPdjWnvwGTalSYtOtPgG7dOrzQ1EOFLKU6vXQR02lIosP0h4Oo-sW6C3MYA36ogBPFlhwu8KIwMyg0bJjojXR5gbPIjINocCKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a975887416.mp4?token=U3joaOb4oAOtMU2e8Q0Gpd8bxV6_6P9Lztz7se6R9AL2XuWWYMNX1limuZzcq3xZjrfy3HfSicWaT8ZSmmT-mHfSUD3P9t2im2ngvpptnKrO27na_9vfftg_zXDOD3p6baIge0ujY7zuyifkU1UYwFFEHjj-FyZ5jZTpwIynzLxuS6liN53nCRdmWGRvH0uI38fecQX_gn8EDMak1rJS1XoAH6s4ORH_91VbEV60S4Dx5RZdInVNhPdjWnvwGTalSYtOtPgG7dOrzQ1EOFLKU6vXQR02lIosP0h4Oo-sW6C3MYA36ogBPFlhwu8KIwMyg0bJjojXR5gbPIjINocCKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
حملات ارتش اسرائیل به نبطیه الفوقا در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67345" target="_blank">📅 19:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67344">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af4c05c580.mp4?token=hXVLhMKAKXyV5g-izkJF6qn7zG4fsRvBopwIFTMyqaLciR_enlSv2zHdmsheyoBuWrfPVqoCr2W-a2xp6sBbyQ9aB-mEl_Vx4Dt3u1dAg1eWtgvVmuBm0_wXcDJlOonu-3uZSZx8TqDNLc4IbZlnHE7L99an_olSnXJaGm7_nqwLcX_SA9PedCdhJnUiGBVGBo32hjV_KSeW3hzie-NpNGLiWHBvQsliHxkT0qRs00AxNx5mQ_SW96ZK8ITferVvmioj3pOd9uHfTiWlFHgWnRWiA-3scxbinaoFM1OrpAncQUxkeumjBBtcQ9pG04Y8citYmpBlxsNMJuuvFifPsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af4c05c580.mp4?token=hXVLhMKAKXyV5g-izkJF6qn7zG4fsRvBopwIFTMyqaLciR_enlSv2zHdmsheyoBuWrfPVqoCr2W-a2xp6sBbyQ9aB-mEl_Vx4Dt3u1dAg1eWtgvVmuBm0_wXcDJlOonu-3uZSZx8TqDNLc4IbZlnHE7L99an_olSnXJaGm7_nqwLcX_SA9PedCdhJnUiGBVGBo32hjV_KSeW3hzie-NpNGLiWHBvQsliHxkT0qRs00AxNx5mQ_SW96ZK8ITferVvmioj3pOd9uHfTiWlFHgWnRWiA-3scxbinaoFM1OrpAncQUxkeumjBBtcQ9pG04Y8citYmpBlxsNMJuuvFifPsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو:
ما در وضعیت دائمی جنگ نیستیم.
من خودم، به همراه رئیس‌جمهور ترامپ، چهار توافق صلح را به پیش بردیم.
تنها مسیحیان لبنان نیستند که از ما درخواست حفاظت می‌کنند.
دروزی‌ها هستند، مسلمانان هستند، مسلمانان سنی هستند و حتی تعدادی از مسلمانان شیعه نیز همین‌طور.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67344" target="_blank">📅 19:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67343">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a4244b191.mp4?token=PmekmtM0Gtsgvqwwu1k0SCmW63IaScKYLZi7BV1wEILZqK-5UK-dED8BKWYOo-OsdbK_c5ihJexurjbBVkhfHqHeEC19WQ0_5GVneJQZUw8Y-NnXeJTngfb_vMU6A7aU0fBUmgFP8QWL6WjnxF1rHHtdbltrBJ5FA11wSSMuSWiZKyEKHJvkSegI2VE7p2dYxBFytVS4gle40ywft8ir20ZDrFtdt-Pn5FjuzyM48vBNnuls2osKMiZbcRccadnjWHKthkmMVmUeQBxxSrMvfqLf7GDiDjn_k226KjQoijCAyMS0GXMKyxs_xgp_4_SxQwdhbEmXVRwo-2WjCZNaCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a4244b191.mp4?token=PmekmtM0Gtsgvqwwu1k0SCmW63IaScKYLZi7BV1wEILZqK-5UK-dED8BKWYOo-OsdbK_c5ihJexurjbBVkhfHqHeEC19WQ0_5GVneJQZUw8Y-NnXeJTngfb_vMU6A7aU0fBUmgFP8QWL6WjnxF1rHHtdbltrBJ5FA11wSSMuSWiZKyEKHJvkSegI2VE7p2dYxBFytVS4gle40ywft8ir20ZDrFtdt-Pn5FjuzyM48vBNnuls2osKMiZbcRccadnjWHKthkmMVmUeQBxxSrMvfqLf7GDiDjn_k226KjQoijCAyMS0GXMKyxs_xgp_4_SxQwdhbEmXVRwo-2WjCZNaCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو:
روستاهای مسیحی در لبنان...
برخی از آن‌ها در واقع درخواست الحاق به اسرائیل را داده‌اند زیرا ما آن‌ها را در برابر حزب‌الله محافظت می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67343" target="_blank">📅 19:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67341">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccd048f948.mp4?token=iinzDX12uE2asqAErGq1u5l0i4MT4a0ivJzjpN9zMLqr9c-evlOG9jbQVA8YCtNXf1F64in5Vd_36wmFTQAWgzOb3rEj1OMeu9qLKsQbwQIV3NsItbBjBoePhzf_OZAAFECE3kNtUJe6chbeMQcyDKVM4wxKztMWadQvn3YgVXrUNdb8QGtdZ_YRwG5h9vc7QHMGE9_5qlT4HATfOZqITDMi_TqKFl0mv7RPfB3Xi_SJ2nge0TJ0rSdSr2G0dxNLyzpvqzdVB6Mb6wAXqx8br_XtDa6tfgQ09Cu3lO2Dpc-UYavPq8TQA-NuRe78lcoEf8jDod42KViL3mSbfZhHgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccd048f948.mp4?token=iinzDX12uE2asqAErGq1u5l0i4MT4a0ivJzjpN9zMLqr9c-evlOG9jbQVA8YCtNXf1F64in5Vd_36wmFTQAWgzOb3rEj1OMeu9qLKsQbwQIV3NsItbBjBoePhzf_OZAAFECE3kNtUJe6chbeMQcyDKVM4wxKztMWadQvn3YgVXrUNdb8QGtdZ_YRwG5h9vc7QHMGE9_5qlT4HATfOZqITDMi_TqKFl0mv7RPfB3Xi_SJ2nge0TJ0rSdSr2G0dxNLyzpvqzdVB6Mb6wAXqx8br_XtDa6tfgQ09Cu3lO2Dpc-UYavPq8TQA-NuRe78lcoEf8jDod42KViL3mSbfZhHgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار تسنیم : نظرتون درباره رهبری مجتبی چیه؟
🔴
زن عرزشی : چی بگم؟! نمی‌دونم ما که همه منتظر بودیم مجتبی حداقل برای تشییع جنازه پدرش بیاد و حضوری باهامون صحبت کنه، ولی بازم نیومد!
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67341" target="_blank">📅 18:30 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67340">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c05464482.mp4?token=FUH0kAqCufOK7TmCItSFRKq298WUwom1MjTp9swfr2mBeGUkesCaeo35LpLoJTppPSuorHcdusH9SWu5_cd-CXn6Xvt584u2iISjc8bsvZEtBmARvODLpz2u9a-PWfAi_rrqOotwm2KYFfCI2Mtv04I3HmCkp4p7DFudzWDueSeYPl8RvDX2CsPxoQN3U0obz8-R35R8GDTrnhkTbLrtSBGNFVBc6xdcgorPnVDPXsj0k6U1hk6rPu0Ik6TuzhnxWmQk_GLZeNvNQXweqZ7yzc-3uU7jynqlFlfmo_IeWM9VjM5maz6gIkLTrmu0rc-vl3nrXUyRyxlZbeHuaJ-MnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c05464482.mp4?token=FUH0kAqCufOK7TmCItSFRKq298WUwom1MjTp9swfr2mBeGUkesCaeo35LpLoJTppPSuorHcdusH9SWu5_cd-CXn6Xvt584u2iISjc8bsvZEtBmARvODLpz2u9a-PWfAi_rrqOotwm2KYFfCI2Mtv04I3HmCkp4p7DFudzWDueSeYPl8RvDX2CsPxoQN3U0obz8-R35R8GDTrnhkTbLrtSBGNFVBc6xdcgorPnVDPXsj0k6U1hk6rPu0Ik6TuzhnxWmQk_GLZeNvNQXweqZ7yzc-3uU7jynqlFlfmo_IeWM9VjM5maz6gIkLTrmu0rc-vl3nrXUyRyxlZbeHuaJ-MnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زینب سلیمانی:
شهادت آقا برای ما سنگین‌تر از شهادت حاج قاسم بود
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67340" target="_blank">📅 18:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67339">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/syev0Yd0fSShz7EdxCf8FLrtvfGam8_cHQQoOlOZg6jcPHF28x1B7Fu4gfOTYQlLNIprgXFavF4Rb18mPqnU2jwNq9mJkHsTXnGoDSRSeBSylGht-PAlmovg4EaLbYj8tZrfOcI0WysSF0YYLmAOUMaAzD9cHUUKSF327awt50t6GYWmDz4GYiYY1JnuCcKpvXjoHL6jNVvGOzH7mQebrRqzpYj996rBiVUvuKui_wKsI5FzD5foIwdsf8fZ3Auhyp3L6dm1dm0Aacb6jIJGqdDSFqSolRR-oDZ5FxqAjNW9HlYvqfoNsPUTS014QNPY1j_PgWnyksz_Fxoc7ocLLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دفتر شاهزاده رضا پهلوی:
🔴
‏تلویزیون بی‌بی‌سی فارسی در صفحات رسمی خود، با انتشار بخش‌هایی تقطیع‌شده از گفت‌وگوی شاهزاده رضا پهلوی، تصویری نادرست و گمراه‌کننده از اظهارات ایشان ارائه کرده است. تیتر و متن این پست، با اتکا به نقل‌قول‌هایی ناقص که پیش‌تر نیز توسط رسانه‌ها و حساب‌های وابسته به جمهوری اسلامی برای تحریف سخنان ایشان بازنشر شده بود، به‌گونه‌ای تنظیم شده که به مخاطب این برداشت نادرست را القا می‌کند که شاهزاده رضا پهلوی آغاز جنگ یا تصمیم به حمله را به سفر خود به اسرائیل نسبت داده‌اند. برداشتی که هیچ نسبتی با محتوای کامل گفت‌وگو ندارد.
🔴
آنچه شاهزاده رضا پهلوی تصریح کرده‌اند، این است که سفر ایشان به اسرائیل، در کنار تلاش‌های گسترده میلیون‌ها ایرانی، به روشن‌تر شدن این واقعیت برای افکار عمومی جهان کمک کرد که مردم ایران دشمن جهان آزاد نیستند، و از این رو دنیا در برخورد با جمهوری اسلامی باید حساب مردم ایران را از این رژیم جدا کند. اینکه مسئول اصلی بحران، جنگ و بی‌ثباتی در ایران و منطقه، جمهوری اسلامی است. ایشان همچنین بارها تأکید کرده‌اند که هدفشان پیروزی مبارزه ملت ایران با کمترین هزینه انسانی ممکن است. چنان‌که در همین گفت‌وگو نیز تصریح کردند: «تمام هدف من این است که این مبارزه با کمترین تلفات جانی به نتیجه برسد… هر انسانی که جانش را از دست بدهد برای من واقعاً دردناک است.»
🔴
این‌گونه رفتارهای غیرحرفه‌ای و تحریف‌های آشکار از سوی بی‌بی‌سی فارسی در حالی صورت می‌گیرد که چندی پیش، مدیرعامل کل بنگاه رسانه‌ای بی‌بی‌سی و رئیس بخش خبر این سازمان به دلیل رسواییِ دستکاری، جرح‌وتعدیل و ادیت مغرضانه سخنان و مصاحبه‌ها ناچار به استعفا شدند. از رسانه‌ای که هزینه آن از مالیات شهروندان بریتانیایی تأمین می‌شود و با وجود ادعای راستی‌آزمایی، به دلیل نقض مکرر استانداردهای بی‌طرفی با بحران جدی اعتبار مواجه است، انتظار می‌رود فوراً نسبت به اصلاح این گزارش مغرضانه اقدام کرده و سخنان شاهزاده رضا پهلوی را به طور دقیق و امانت‌دارانه منعکس نماید.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67339" target="_blank">📅 17:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67338">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d7e9ec8c8.mp4?token=Ow2hztpRfWm1lcqbtJN1j3TnnjeFaWnG8PlqrvEMKIo6smu1UBQUlF-eSmu4P80JuOYfgeL5nBg1qVsMsVMQQE8AIb6tT5JT1Y9s647ohsqG_b_ZIDjbGL_fazXGp2kfLhmKpBmrwi3zW1KXvvgWEEUMyO-t3459KDrfD3Gc3Wk9-ygFqTqadCsnmm88lYl1eWGyv81dD-POiD2uOxzocUpH0k_6nqe8__O-a8DiYTGI6UgzHrMcoNPI5TD1OnqIyuCPL--2yTQ5BRqXw6eZfdqq6e0aQ43AtZRIp3jkh5ZtKPcFxwDmnJMGWC8mGjEciXjBcj3j_7SvH9fK4sG9uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d7e9ec8c8.mp4?token=Ow2hztpRfWm1lcqbtJN1j3TnnjeFaWnG8PlqrvEMKIo6smu1UBQUlF-eSmu4P80JuOYfgeL5nBg1qVsMsVMQQE8AIb6tT5JT1Y9s647ohsqG_b_ZIDjbGL_fazXGp2kfLhmKpBmrwi3zW1KXvvgWEEUMyO-t3459KDrfD3Gc3Wk9-ygFqTqadCsnmm88lYl1eWGyv81dD-POiD2uOxzocUpH0k_6nqe8__O-a8DiYTGI6UgzHrMcoNPI5TD1OnqIyuCPL--2yTQ5BRqXw6eZfdqq6e0aQ43AtZRIp3jkh5ZtKPcFxwDmnJMGWC8mGjEciXjBcj3j_7SvH9fK4sG9uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بزرگترین آتش بازی تاریخ آمریکا در واشنگتن دی سی به مناسبت ۴ جولای روز استقلال آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67338" target="_blank">📅 17:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67337">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IJj9w6hCvO8MmLbrZGDfdeKUSgI-U8l40d0B_Ul695JXuVroMPiHwAd2nUpdWrCS5tDd-zHk1OUw-kjPKWntEEfkc4fUs0QhMsITkyl7IsepJQpmvfdFPG24NSpoS7s6ThkE2kJi9hBwMozx6dfDQZ0l_zBjZKGct64KZpl7jGiL7rFKyKPvu7-8hv4On2G7Ltqbc4qAMuItwiMH-ufpDRu4Cz3xx73Pd1QL77NAUImZSURG9Y75NC425kLfmcRsUWLPh_fE9pn0mFiVM9Bg7Di3BHtatLp9CzSCnMfYxqEHzjeYFCi-y8cXe08mU6IovlFPByZMILlrZnaWtxvPDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
❌
دیوید کیس مشاور و سخنگوی پیشین نخست‌وزیر اسرائیل:
تنها دلیلی که ما امروز تشییع جنازه خامنه‌ای را بمباران نکردیم آن است که 10 هزار مأمور موساد در میان آنان داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67337" target="_blank">📅 16:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67336">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e644784ac.mp4?token=DwOmp7BF3G3-AfW4sxu5-UsrS2IwRSUHproT4yG-_0iOfyucGJ5yyqr3PQVcqjK1iDJBoFuOwfXGUYKU_AVjANpH1m-hBaI0s_8_zdKiptz3qqBDjOyC6E630mLrjnz26gqQkm2UutCOdP6ky4S82v2ZeYjEakIPKcmgqnPBg_vtwETtm9MyyaWRW0FVBxpswPMkNh4aKWrU0iXw2JZbg9ssYeDdPyDkpnfiG6Zo1vaWxSH5SMKmVl-x5lisRxXqPeXhJpmR-nfvJiOdIXVd6Nr7NlMt9hE1XR_0ezwgm6YGn1m9YEwv9THnGLi0Gf2zdOTr6NiMFR0AF7NbWGeuHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e644784ac.mp4?token=DwOmp7BF3G3-AfW4sxu5-UsrS2IwRSUHproT4yG-_0iOfyucGJ5yyqr3PQVcqjK1iDJBoFuOwfXGUYKU_AVjANpH1m-hBaI0s_8_zdKiptz3qqBDjOyC6E630mLrjnz26gqQkm2UutCOdP6ky4S82v2ZeYjEakIPKcmgqnPBg_vtwETtm9MyyaWRW0FVBxpswPMkNh4aKWrU0iXw2JZbg9ssYeDdPyDkpnfiG6Zo1vaWxSH5SMKmVl-x5lisRxXqPeXhJpmR-nfvJiOdIXVd6Nr7NlMt9hE1XR_0ezwgm6YGn1m9YEwv9THnGLi0Gf2zdOTr6NiMFR0AF7NbWGeuHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
اگه اهل دعواهای خیابونی هستی، این ویدیو از استاد طِقه زنی رو تا آخر ببین تا به امید خدا پیروز میدان نبرد بشی؛
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67336" target="_blank">📅 16:28 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67335">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/67335" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67335" target="_blank">📅 16:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67334">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
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
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67334" target="_blank">📅 16:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67333">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ieU28ao3VEdmiUPQqmeWepMZZ2TIRIc6Gnp4ulsTyQW95NcV_VSof-gsWq9dzrLe5MyIddv0gMb857F4Noi72-LZIu96QIKkQaErZtABg8hBBkDG0a-Gz_ytX30X_xDHdeelNAZwnJ52N69vQLV11bGxZ4HmE0KtJsO6idi7ucrKD2G6owp_X7OzPAru2-BZRfzW2lNwwnfBizRv7B-hWQBjIs50V9jxxKvrhRQi0814H5DXktFexzOFq1_Zjl6SQC5ayhEOvEhJoc1WUpWQkfmsekHV6podkF1k41KJl_xcKjEXArsRslgw2uueaBSiUILPY_2XXFp8s6-kdLJi8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گویا کامیون حمل جنازه علی خامنه‌ای مبلغ2,298,000 هزار تومان خلافی داره
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67333" target="_blank">📅 16:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67332">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kIYmX3of1UxRvrTP39UEmDpjtB5Gym1ZJ4QkSs4gVWjDW2xCsDPCLRgQlJRe5mOggzjHyLlbXlPp5FsTlE6sJwrkvxEibU6T3v6AUuNNLB7kDdhlmOMWyUvy4W77rfa3LZYbKniGkSiIgkENWNc_KkyFtjHqyrWSmO5F6xJxV6Lf0lipJ8dOs-e-FeaMQLtCUziyDzSzFqY1Mjf15PWMzaR-cxNc4L1PMYM9QoQAOcHpMjPvanC_HX6Hcrj7nJLRUPCK1ZIQPEKDK9ghrSAvOURH4pboWlt0bZyVYHwpKnBs9254cE3LRNbDPtUaDZvVZrWwNspwqNozlymnaaYjzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
محمد اکرمی‌نیا سخنگوی ارتش:
«هرگونه اشتباهی از سوی دشمن، با پاسخ قاطع نیروهای مسلح ایران مواجه خواهد شد. ما بارها اعلام کرده‌ایم که از فرصت آتش‌بس برای ارتقای توانمندی‌های رزمی خود بهره می‌بریم. ما حتی یک لحظه را هم هدر نمی‌دهیم و تمرکز خود را از این مأموریت برنمی‌داریم.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67332" target="_blank">📅 15:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67331">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو در جلسه دولت:
شنیدم در رسانه‌ها گفته شده که رئیس‌جمهور ترامپ خواسته علیه تونل‌های تروریستی در لبنان اقدامی انجام نشود. این یک افسانه و خبر جعلی است.
او حتی یک کلمه هم در این باره به من نگفت و من هم از او چیزی نپرسیدم. ما بر اساس ملاحظات و تصمیمات خودمان عمل می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67331" target="_blank">📅 15:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67330">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dk4vbPIaM5vkB_-BfvjYL8CmmNa8l_1NKsHCXbZuxdhIIf5tgo4cVuVXvVcnJk7hjfQ-Te1DG7p0t3hpvqZJS6JPNq9jTgB6q5X6YYMdrKvBGF3kFeygaiNPM7yH6yVlz2C_UsHX6zZCiKZLSa18Tzlif5_iAfilpjI0L7YMgV6XJNeYK-8U4NAV6SK87NyOzGKAhL_4ltIOxqC9nCNum3eRPwq2c6A9Z_OBqr0pZ9UCE8SA9gECiz1nrKtiC8bZB0IFAMsPinlxFUGvV8k8G20eGb0SWFLkXoyXbRDF9kVbgQCp6GKaeNoQaN74vEN1Bm5IVNfN66A05pDV3iLoGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تصویر ترامپ در مراسم وداع با جنازه علی خامنه‌ای که روش نوشته شده:
خواهیم دید چه می شود
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67330" target="_blank">📅 14:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67329">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TdjGIR4zQTunYeIvc3ozF6YUla9sG4jPzcUy24ANf1pZZC1pSU98lzqrrxHjt-wTVI9igj_IHt3Iuv-yJtjrEFCTf7gnB916kcDsXDaYmvT3gKVA2O7Cm3gO6UH8DA5sXe5idiqtKg0NMdZKgc8LzF4Sq5BKkKegsyS_15SRQVzWx1I1DN4qlFkS37oSpdxjdvPeZC2xcDgfXVnHE4IGic7Wj1ZNPCAJLj2PGMHEIblQEG-1APYVkM0CXU-1w-wu4byXq5NAncPn09v2V35Y9c107I9VtuQSZU8vEv5AT-ZLiObwP71hlVSnclACy90mKQQQyG4Ldw5jmEN5mSSR8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسرائیل به فارسی:
بهرام که گور میگرفتی همه عمر
دیدی که چگونه گور بهرام گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67329" target="_blank">📅 14:09 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67328">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b8ead8806.mp4?token=jeO7hahZCp6IpPUPR-arM1tDwjHvjDnsJtPUPBiVQbF8KFYXIBdF6oHkgWBAHiPL-kS_dhniAJhF4pTdj-q2kNv1tfYmegllHoje_BScJmekujtwGn9bacT_kYXqgEB0jp1cSst9h_IkpEM509_EkvuT5-MPf14XFQ9_smg0T2u-I3ezCtwweUB7g-WvykFFHlgDw5-__3O7TFBL9yhiWbmCH9ePXrbhZpx1-WPJSiHVz7eZQpDWB_GUfiZA5fZWadKajKEnezUBM5kut2EgmLBhNygj1B-tpLSFbYakbCCDiAXWk1ZJQcH9t-rb8kcIUjHK7tZ694VyqAR1QUlQSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b8ead8806.mp4?token=jeO7hahZCp6IpPUPR-arM1tDwjHvjDnsJtPUPBiVQbF8KFYXIBdF6oHkgWBAHiPL-kS_dhniAJhF4pTdj-q2kNv1tfYmegllHoje_BScJmekujtwGn9bacT_kYXqgEB0jp1cSst9h_IkpEM509_EkvuT5-MPf14XFQ9_smg0T2u-I3ezCtwweUB7g-WvykFFHlgDw5-__3O7TFBL9yhiWbmCH9ePXrbhZpx1-WPJSiHVz7eZQpDWB_GUfiZA5fZWadKajKEnezUBM5kut2EgmLBhNygj1B-tpLSFbYakbCCDiAXWk1ZJQcH9t-rb8kcIUjHK7tZ694VyqAR1QUlQSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این بزرگوار که قبلا گفته بود بخاطر یه تیکه نون به سگ دادم اومده داره ترامپو تهدید میکنه میگه بیا کوت عبدالله ببین چیکارت میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67328" target="_blank">📅 13:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67327">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
❌
دیوید کیس مشاور و سخنگوی پیشین نخست‌وزیر اسرائیل:
تنها دلیلی که ما امروز تشییع جنازه خامنه‌ای را بمباران نکردیم آن است که 10 هزار مأمور موساد در میان آنان داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/67327" target="_blank">📅 13:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67326">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0be756a04.mp4?token=DpVrxArBNKDXWEA2vzfu9ugaL5ApdLOsYlOxlE93LG5qGGarJeOMWPFbWELfHBwRQA2Ng2EnnxUPiZ3gKFp1KLlHCln3ADNmT4eB7IfGbzj9dHP1D3hIQEs9B1ucIj13_C_r0QjlrgnaKUlyWtAdNjw8EK_L_28JjGf5nOaohhej_fEsO7rWzelB07Qqh6DL8rN50kz8BY0KYjvnQ0E2oqzoC3pT4M4l1H4qKxr5WlDDZSx43KEMq0NjlOzJ0BjOZ2vp6yeIw5r3bWQ_nFaNDeOjIY3-z2dTygs8rutYO3HkatSB_z3-mBUiOJ6-hu4yMgkuIpSVOPWUqNYUSJJH5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0be756a04.mp4?token=DpVrxArBNKDXWEA2vzfu9ugaL5ApdLOsYlOxlE93LG5qGGarJeOMWPFbWELfHBwRQA2Ng2EnnxUPiZ3gKFp1KLlHCln3ADNmT4eB7IfGbzj9dHP1D3hIQEs9B1ucIj13_C_r0QjlrgnaKUlyWtAdNjw8EK_L_28JjGf5nOaohhej_fEsO7rWzelB07Qqh6DL8rN50kz8BY0KYjvnQ0E2oqzoC3pT4M4l1H4qKxr5WlDDZSx43KEMq0NjlOzJ0BjOZ2vp6yeIw5r3bWQ_nFaNDeOjIY3-z2dTygs8rutYO3HkatSB_z3-mBUiOJ6-hu4yMgkuIpSVOPWUqNYUSJJH5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جمهوری اسلامی پس از ۴۷ سال در مهم‌ترین رژه‌ی خود حتی به‌اندازه‌ی بند پوتین‌های ارتش شاهنشاهی هم نظم نداشت.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/67326" target="_blank">📅 12:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67325">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BUdjI1BQVcZ9ppXT98zCwMfX2iePypdWg5Nyf1y_N4P0PZOtE-fOoGhN4Z6Gr-lT7wYqlG6dQgxKVhBWDPpMuiLoVB8HxEOQTauGk-kEZARlf_YqARA8BZEHVXZgDHIe1-zN4xZNcEIFwM9IzRPGwlHMWOeZ32e5zM6yNm-bfyy46AabVkOdlR9i7rHnMsWaO74ZB3QHAj9L24kMN4eAmKGqbAoA9JKTiYH_OQaLsGpWMI05RRIa65xBp7x3U8MH-ntHTQQhM36HGEbdIotd8RTynpbyz-sWsBLOXV4uB7H_PYgNRrYzwSZ6--h-sS_jSDTJ1QKkTbar7sivl1aYtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هرمزلتر:
🔴
نیروی دریایی سپاه با استفاده از قایق‌های تندرو، کریدور مورد حمایت آمریکا در تنگه هرمز را به طور کامل متوقف کرده و در نیم روز هیچ شناوری از این مسیر عبور نکرده
🔴
سپاه صبح امروز از طریق بی‌سیم به تمامی کشتی‌ ها هشدار داد و همزمان قایق‌های گشتی نیروهای ویژه را برای اعمال کنترل ایران بر تنگه هرمز مستقر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67325" target="_blank">📅 12:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67323">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FBa2NEhbirtddMj6PoCQFtrxG_Hcu86jiOTLfOzbt2TD87IX_bd6vMx3WGC2z8b6wr59cCb740cuj_CiwJt1hdzpGy2j_oPMswSi27QlY2ywOwGg1ESxLijyRERWHl9lo-1JrG_soo5Ki8SEY3-lKZE-u1xwBh_EKfIHaZnrAFGqc5C22CXRYwdIAIgA586yFeL8cmL4WqM2PETT5soUDg7HIIpNYQqT_7IxRZd7kqrWp6j-fpIeScQjoTz9c60NWMMl9gEuqjk-YxnZ9fKL5WFz8ppixWBOWS3xGhDIjw2lYai3S_WdI5dvWk_A3iCY2bQDqsV7dAxjIGR_bHaoyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f22dc07ca.mp4?token=C9tcmASPPPrP666g-by2_4wAQMFAqBg7LTgVJo6vRsubMvKZfPiI9wN_WvEKpawFuiModLrp0PaglS8cW5TPC9M_1YMIURtxf8qL1atSSbjeDGNrER67cxzl_qfUUz34MxOIG9042RoTLmsX9OVFtyLM8tycuhV2tXZXsBfbp6I1HFg07EZAxvFsXq4G9GlrVspS9c-BxaHMJay1yltOSgyJ1xx3xT85LV5jmAHcLk4ILLLyts7TRVwyvg8r0s_i7sYyKTNbo-do_ssJN4eT31oLHLRzZlFsrYVDnuo83AKq_fiIR4jQmnILgsLGpDFTXTVmstlOWgJ_YoGrIx6F5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f22dc07ca.mp4?token=C9tcmASPPPrP666g-by2_4wAQMFAqBg7LTgVJo6vRsubMvKZfPiI9wN_WvEKpawFuiModLrp0PaglS8cW5TPC9M_1YMIURtxf8qL1atSSbjeDGNrER67cxzl_qfUUz34MxOIG9042RoTLmsX9OVFtyLM8tycuhV2tXZXsBfbp6I1HFg07EZAxvFsXq4G9GlrVspS9c-BxaHMJay1yltOSgyJ1xx3xT85LV5jmAHcLk4ILLLyts7TRVwyvg8r0s_i7sYyKTNbo-do_ssJN4eT31oLHLRzZlFsrYVDnuo83AKq_fiIR4jQmnILgsLGpDFTXTVmstlOWgJ_YoGrIx6F5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
و بعد از چهار ماه همچنان عامل این جنایت و قاتل فرزندان ایران چال نشده و اجازه چال کردنش رو از قاتلش گرفتن!
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67323" target="_blank">📅 11:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67322">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5f6d58549.mp4?token=T0p1HEfx1irMjcgE43DZnOoz_Yxgc3NaWBjUT7EGjCX-9KykMieUDcdDOx6F7jymKoKpSlpsQlio2SlFcyXuSeRqlKaGE5POD0m90X6D7ZdDJCBGp-gbNMkk221zds5kfu4EjLd0dgeTrBbO43BwQad1gbx1f2NeIXjJdCN66LfKKZcydYLWMAkXYr-NXHym5jOJOsai_3NDgPtADWr4hksluS9pF2SYXJnqThJqprfVgJd0_rg6KvC_koGfpRfStUJdaXF4riURNOdMelgJwwbWri1MYvdx47jfZjI4ppu1roVkPKYXy59NWU21B4yV2tQDJZFnNEEYpTRDhgtFZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5f6d58549.mp4?token=T0p1HEfx1irMjcgE43DZnOoz_Yxgc3NaWBjUT7EGjCX-9KykMieUDcdDOx6F7jymKoKpSlpsQlio2SlFcyXuSeRqlKaGE5POD0m90X6D7ZdDJCBGp-gbNMkk221zds5kfu4EjLd0dgeTrBbO43BwQad1gbx1f2NeIXjJdCN66LfKKZcydYLWMAkXYr-NXHym5jOJOsai_3NDgPtADWr4hksluS9pF2SYXJnqThJqprfVgJd0_rg6KvC_koGfpRfStUJdaXF4riURNOdMelgJwwbWri1MYvdx47jfZjI4ppu1roVkPKYXy59NWU21B4yV2tQDJZFnNEEYpTRDhgtFZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مهدی رسولی  مداح بیت رهبری میگه برای خون‌خواهی اومدیم؛
شما هنوز خونخواهی سلیمانی و... رو نگرفتید بعد میخواید اینو بگیرید
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67322" target="_blank">📅 11:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67321">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5807c7f54.mp4?token=Q9Gp5EHnKVHylnvSLGhVp4GOTQvHVIT0D0vHD0eKwLEYMFtLlRC3Lm9P4hw3L1LHs0_3LyXKhvb8hNYfQFowWY-CG5EGzn3Obc8fMcHmN_ni55lirQ1CNFxFQwHrkt5syYNoviQ-614pEVwxiMF_NGnsCL5r_47UwXxLnalrlR7lakYH1mHRm8YYwMaVYx5vGNmk_Hph4nnGdryRcmb8WqAmf5kjYVb97gI9tO5aXoz5aOPt0Mr_PJlUfZ-rxKRzwL86LkRqHIrbtVfSLPNv75k_l6cIjeLmIDOdqRG-PwAsWlwcLyZBVlOlrzGmy4s-s4aIIow-gzw-K5u6rM9grQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5807c7f54.mp4?token=Q9Gp5EHnKVHylnvSLGhVp4GOTQvHVIT0D0vHD0eKwLEYMFtLlRC3Lm9P4hw3L1LHs0_3LyXKhvb8hNYfQFowWY-CG5EGzn3Obc8fMcHmN_ni55lirQ1CNFxFQwHrkt5syYNoviQ-614pEVwxiMF_NGnsCL5r_47UwXxLnalrlR7lakYH1mHRm8YYwMaVYx5vGNmk_Hph4nnGdryRcmb8WqAmf5kjYVb97gI9tO5aXoz5aOPt0Mr_PJlUfZ-rxKRzwL86LkRqHIrbtVfSLPNv75k_l6cIjeLmIDOdqRG-PwAsWlwcLyZBVlOlrzGmy4s-s4aIIow-gzw-K5u6rM9grQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف یه 20-30 سالی هست درحال گریه کردنه
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67321" target="_blank">📅 10:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67320">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/810ada8a67.mp4?token=uz1ikFBKsqxfOPHSEYbvNKPY0p_qf9UV6dWr8nYUcjjMa6InharHM5j40etOJpHAhTHBoV2b7QAaHqj4gWPEJt9n4yK4LKHhsHtIXWQfsxxV4dRCqJG_uC1DNI1pFkRwxwIrAaX4iBEy_TZbSm6w_XPmJQwYS7cjOU1O0_zQDUPHhDQna9rsdKeSLQoelECklkxzwqJL7n9V4PEhemDN_gEYDhnlogE-WXFVCvqI-zIR0jkc1LuRaBIP9tNppn9AIJFtVPxUk3jgQuQB3gPFp9Qpvn6tXRG3tUll1Gv9xJlZgFW96f3z1KILELM0-3Au8xqSKwnYa2RrwS82qLwDDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/810ada8a67.mp4?token=uz1ikFBKsqxfOPHSEYbvNKPY0p_qf9UV6dWr8nYUcjjMa6InharHM5j40etOJpHAhTHBoV2b7QAaHqj4gWPEJt9n4yK4LKHhsHtIXWQfsxxV4dRCqJG_uC1DNI1pFkRwxwIrAaX4iBEy_TZbSm6w_XPmJQwYS7cjOU1O0_zQDUPHhDQna9rsdKeSLQoelECklkxzwqJL7n9V4PEhemDN_gEYDhnlogE-WXFVCvqI-zIR0jkc1LuRaBIP9tNppn9AIJFtVPxUk3jgQuQB3gPFp9Qpvn6tXRG3tUll1Gv9xJlZgFW96f3z1KILELM0-3Au8xqSKwnYa2RrwS82qLwDDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در جریان مراسم افتتاحیه مسابقات «فولسوم پرو رودئو» در ایالت کالیفرنیای آمریکا، یک چترباز پس از آنکه پرچم همراهش به درختی گیر کرد، تعادل خود را از دست داد و به شکل خطرناکی روی یک چادر سقوط کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67320" target="_blank">📅 10:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67319">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ca0cec0e0.mp4?token=S7f7syw7AB5ct_LfZ8yp6aNMkH9S-3c0mTqgDdGoOY2yeJhiulKyXXaGc4XsqDHcFi5_V-FtuREoCI17M72Te_R4TMEcQtvREOoSbZvHrUn4wBUdZprJKS2ewJIkG1AwGzIg4hmbXeJ00NwOxAM4uQcj941-KZF9D_d6b9JnmLZ3Gh32jmxd26jjGJVFkONe011NMGRBjlTAJqmY_xCuxpE-s90UmpM96e_fdIunhYxOp6lycalen2o6Md2GGBcaorylFrDCBHoK7mN4Myr5orXXoDnfz_Sisrtu49M2RDx910asTVQlAl9X-Vjw5sm7Gj2OPNHa5yfb8qrrA8qLcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ca0cec0e0.mp4?token=S7f7syw7AB5ct_LfZ8yp6aNMkH9S-3c0mTqgDdGoOY2yeJhiulKyXXaGc4XsqDHcFi5_V-FtuREoCI17M72Te_R4TMEcQtvREOoSbZvHrUn4wBUdZprJKS2ewJIkG1AwGzIg4hmbXeJ00NwOxAM4uQcj941-KZF9D_d6b9JnmLZ3Gh32jmxd26jjGJVFkONe011NMGRBjlTAJqmY_xCuxpE-s90UmpM96e_fdIunhYxOp6lycalen2o6Md2GGBcaorylFrDCBHoK7mN4Myr5orXXoDnfz_Sisrtu49M2RDx910asTVQlAl9X-Vjw5sm7Gj2OPNHa5yfb8qrrA8qLcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اولین حضور عمومی مصطفی، میثم و مسعود، سه پسر علی خامنه‌ای، در مراسم تشییع او در مصلای تهران.
مجتبی خامنه‌ای، جانشین علی خامنه‌ای، اما همچنان در انظار عمومی ظاهر نشده و در این مراسم غایب بود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67319" target="_blank">📅 09:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67318">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd6157bafc.mp4?token=VqoShaHp8RKJ9-5d3PSLTlgxtvA-4RndHog3KdyT6l9VhPCQa-_1K6eLn3bewT1z0WAHoOD04wlO-rDW64VwoHaTYtqGpqvyanglI-SE_QOwikCEVgmbINZ2zP01D4y3sJ7iKZARJ2Gmy4xxVTfDaoR4QQmFjNyjSZcN--A-xLxhiS7AYFdhlqemX15lfNJAqhlztOdtaSOieRj39LzVG3ZUve7i00Mqp-FAmXkLd9I5lMzfxmldgCtMHcZPnno9nhzmFALcMYfioxZrSagREXJN40bWyZPauduNz1Z2Rv-sgn-0Wa5QOmFRlxk70C_zeTDpLtFWrcks7SYqH2NmKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd6157bafc.mp4?token=VqoShaHp8RKJ9-5d3PSLTlgxtvA-4RndHog3KdyT6l9VhPCQa-_1K6eLn3bewT1z0WAHoOD04wlO-rDW64VwoHaTYtqGpqvyanglI-SE_QOwikCEVgmbINZ2zP01D4y3sJ7iKZARJ2Gmy4xxVTfDaoR4QQmFjNyjSZcN--A-xLxhiS7AYFdhlqemX15lfNJAqhlztOdtaSOieRj39LzVG3ZUve7i00Mqp-FAmXkLd9I5lMzfxmldgCtMHcZPnno9nhzmFALcMYfioxZrSagREXJN40bWyZPauduNz1Z2Rv-sgn-0Wa5QOmFRlxk70C_zeTDpLtFWrcks7SYqH2NmKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زاکانی و برخی از مسئولین تو حاشیه مراسم رفتن چلوکباب خوردن، عرزشیا هم اون بیرون زیر آفتاب، صف وایسادن تا تخم مرغ آب پز بخورن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67318" target="_blank">📅 09:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67317">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HmqaDLNmtYLHvUY063oUh1_A-K8ldpEZtO-X4LWwK1ccuKXa-pzQz_pgFrhWdPFQ8-I2iOo_b8yGD2fXzjZVwIv0U6EYv_MO9kUATWpsRr2hbN3dbpfL_LzbD5QXmYDoZvokzv0ZZsb31Umip46dIIU3pqbVCI8XcElWnAjVpYVT4-u914sEd2ghGIcfxY5r-JPc0OlNQ0pLm20nz1lOyVI9BoVB7FRAyIMGpLs6VN75iMTMH0GDiCqsF2MQa-6x3Nk3rwrczj8N-hM1ToI0vFyA_wpDPOvNZIq1nG_IdtZ3DnADgvwvUi69FSKtyclRamZgUATmgfRGIMmdfyDDSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
8فروند جنگنده A-10 Warthog در پایگاه هوایی موفق سلطی اردن مستقر شده‌اند.
🔴
این جنگنده ها برای پشتیبانی عملیات زمینی استفاده میشود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67317" target="_blank">📅 09:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67316">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67316" target="_blank">📅 02:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67315">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iweZmqYOLrp5LgwIQUBzODtrAsaSGpgJjAh9-fOWNYNYWSY4SUkh7-8HBN6a2ivtS8Js2IJrWJf_oAMqxt50D3_8S9gDKsVfJ9E86XP_T7vm8w4_N3ouygKJn1j0n1cLJv3rhrvbL_OzZmx6VvffS6iYIS5YQs1DQbn8RJOU3nVo5gX6Woz7FHKJPHUa20zm54MwTKKcCyIbYtF5ZkbSDr_8qRIQ3Qi6umC7fueT1gzt75BdloAhjIAyFZ7F0pWYBiTEwz7k3uGDw7UBA0qFu9ntok2GvY4DTo0gJcDuQPZv4yqlafkHQZ3p-ywhIRXfJ44648ON7oD1fbC6f0K2LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet
@FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67315" target="_blank">📅 02:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67314">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q5SoWwc78P2PN13PkVTLYY4PHEUA3-oDuGR-O5HDFcmRiYmRwvGUiGa66PiNZXMkYT0IH01rlOd7uFejEABV32UF7yeBdXOfKk6WCTXjaivXhwfagWg3bqH0nO0JoOVcFfNlW058m2hS0YqwMcd07WlZ0ldseCo9y3Bauu3cOfQu1Ul4xEEsHXm9mMRO1slJoj5wAB_6TSos1Q44NPM-27sjU7J0o3KEigjZrNItpjmbRpqgdUOT4TyXRyQer6ngR3g3p7snm9Dx2UKv_k-FCaOM-NFo2TiHLi64V_IZnV3HhEfn69mFa8d0L-XUNW9G6TQxzmOkLLk0LFs4bBadDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید:
ولادیمیر پوتین، رئیس‌جمهور روسیه، با دونالد ترامپ تماس گرفت و دویست و پنجاهمین سالگرد استقلال ایالات متحده را به او تبریک گفت. کرملین اعلام کرد که این گفتگو یک ساعت و نیم به طول انجامید. پوتین از ترامپ برای سفر به روسیه دعوت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67314" target="_blank">📅 02:06 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67313">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79806b6dec.mp4?token=SYqUzSZuqMtIk8olC954KVeyC5fyBvC3_eMak-DeRCVm3wC850UaJCbXtozaM8LOlI5WXriw8ekgPUAo5Nn1pXgTKJTGw0M_R_8EMoTWg4ossq7LWZGVD_vVKtg6q7ZsvM49I4y_Lf5peUMwVYMMeznGN-E2I6Ved3pto7NoAF3MR2seoZxqmB488uJcKJEc8jWDTzbE_favm-Bi_wv962fn2OjVA7d-yvjokUF03W7smc0JPqfgSM1pzoZHCqfgicffJ9vztt_x7a9Adu-iVpywT65MvbZC5c12pRapaacgVgHTKq0zQYiIuaPK60JChJxffAOHgkmYDTnZLBFg9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79806b6dec.mp4?token=SYqUzSZuqMtIk8olC954KVeyC5fyBvC3_eMak-DeRCVm3wC850UaJCbXtozaM8LOlI5WXriw8ekgPUAo5Nn1pXgTKJTGw0M_R_8EMoTWg4ossq7LWZGVD_vVKtg6q7ZsvM49I4y_Lf5peUMwVYMMeznGN-E2I6Ved3pto7NoAF3MR2seoZxqmB488uJcKJEc8jWDTzbE_favm-Bi_wv962fn2OjVA7d-yvjokUF03W7smc0JPqfgSM1pzoZHCqfgicffJ9vztt_x7a9Adu-iVpywT65MvbZC5c12pRapaacgVgHTKq0zQYiIuaPK60JChJxffAOHgkmYDTnZLBFg9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
جمعیت هموطنانمون در تجمع چند ماه پیش تورنتو رو ببینید و با جمعیتی که در مراسم تشییع جنازه علی خامنه‌ای اومدن مقایسه کنید
🔴
فرقش میدونید چیه؟ ۸۰ درصد جمعیت در مراسم خامنه ای اصلا ایرانی نیستند. کلی لبنانی عراقی یمنی و فاطمیون افغانی گرسنه رو با پول و... آوردن بازهم نتونستن مصلی رو پر کنن!
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/67313" target="_blank">📅 01:29 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67312">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KWS3PsQEDCzySWZPnRg2WG-H5jtna7fTsYGSHo5rOOilPDvOAYKa2LpN-9o4ZgqoZ5aWn2JCVKQkc_VO226KwOYm_h0OC6YILJVjRI2IIFTJldxE4u9xUKIOhFOYN8fC2-9U3-2KNzkwrvhBGPBKyd7QNS2c6cbwAe90TjHlEeklfZnN6LISjNfqFmiLUQi57iUE116RS3gFfSqZQfVUprIF5mva3f0GcUB7fhQ-LMokm_bMl2URrePbL-IxnhNek9u-V49bYS4SRV8K3NzdFPkRxymLzUVWuBGwk1P9oIdK8ZnlUFESPL7A2zCcn5vNQXzatxUkM8FfTZMLAps2Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
نیروهای ارتش اسرائیل در حال عملیات در منطقه حداتا در جنوب لبنان هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67312" target="_blank">📅 00:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67311">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5be218b45.mp4?token=jqI7IZvDYeghCbHhJCiWkqytu5Cwd4mTVFzMdKKS_UUrh71ndnS835dnZQMVYxMUPdIRRRhc4HJRx5GYSW-0rdjlywMlXVGhfI0euyOLsztDZjRMVS4woIj7_VYb3zwpf2oGNBiyzNjNl5_vm3L2roMwye-RW1STS0DRrpcR5rQDsIFaPhrp-KYnHu5phWtnXxTj4Gh0gUpuIHfuuBYlpgN_bQlMaMH4SZacPuTqJN-N3qcCe__e-oV_Tt-7shbHjGLhBirg8dFJSaBvAqfyK8ZVMYo0HKgoyr_JKokqbWTpzOaeY2ihcWG8zpu-LKEQz4Bg7KSng57HXGXza4nLSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5be218b45.mp4?token=jqI7IZvDYeghCbHhJCiWkqytu5Cwd4mTVFzMdKKS_UUrh71ndnS835dnZQMVYxMUPdIRRRhc4HJRx5GYSW-0rdjlywMlXVGhfI0euyOLsztDZjRMVS4woIj7_VYb3zwpf2oGNBiyzNjNl5_vm3L2roMwye-RW1STS0DRrpcR5rQDsIFaPhrp-KYnHu5phWtnXxTj4Gh0gUpuIHfuuBYlpgN_bQlMaMH4SZacPuTqJN-N3qcCe__e-oV_Tt-7shbHjGLhBirg8dFJSaBvAqfyK8ZVMYo0HKgoyr_JKokqbWTpzOaeY2ihcWG8zpu-LKEQz4Bg7KSng57HXGXza4nLSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علی خامنه‌ای،‌ 3 بهمن 1403:
ده‌ها متوهم به درک واصل شده‌اند. من به شما عرض می‌کنم به فضل الهی این تجربه تکرار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67311" target="_blank">📅 00:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67310">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67310" target="_blank">📅 00:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67309">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/P70UT0a5H8-sOEJXLpi9CPQkGH3hCGumpIolLEbhS7eUPvuB6z1O9nru-zjRYz0jIdXefatAvKGWKbicI0WbAzxjy6ZXsIQdkGcBYWrpw3B3D8vJJG_nXbgTQAWYLTgN37bSRxsK1ezoeyNwTq5DCp0NGholkvz2DFj6dhTpvtBiY5ex7oBScdfxgQPqgqUkHSPO-T1GIgCWQUlGfE5vWwMtQXlagHFDb73Bp9xesKJwfF6uK-lqTz6SOesMMNIi2fv5I03G8-BEcN31wUWlk5Ze7n7W50kgIeQfA9fqGrX6q3S8GVfY9tvSSmPNYGeQFJ9NienVMk-pampMvjXYlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet
@FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67309" target="_blank">📅 00:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67308">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/842bb5b4aa.mp4?token=vsydLC0ZRtwqf1BwPGFg2nm7qd6ApyqoxS2EZKrYnuticzjmDzCZ4RNyJsainqJcMuUKQBznqjGJXxCKuiokMCYtDGWy6k9qaAz_UHIYvMYEM3wWpkKGmOOLi2i8Zuy9VKv97gSr9X4EAzsm3jPuD0yu-WRy_VzoUzylEQy1ALZ3xw90U63xyHQqDwrmV5FvLFwAffMMMWrA7QIAcJ-SSqqtEy2bCX-aqnGvbwt2BD1sDKKiyuvcHxApoOhDSQwnUFxxrvl4oAWHut6ySmOPv95B17kqiZeyAxG3LRc4ypS0zNrwivFakG21FESEBOzl5XnJ8S11Wy4kf3hLSIZHig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/842bb5b4aa.mp4?token=vsydLC0ZRtwqf1BwPGFg2nm7qd6ApyqoxS2EZKrYnuticzjmDzCZ4RNyJsainqJcMuUKQBznqjGJXxCKuiokMCYtDGWy6k9qaAz_UHIYvMYEM3wWpkKGmOOLi2i8Zuy9VKv97gSr9X4EAzsm3jPuD0yu-WRy_VzoUzylEQy1ALZ3xw90U63xyHQqDwrmV5FvLFwAffMMMWrA7QIAcJ-SSqqtEy2bCX-aqnGvbwt2BD1sDKKiyuvcHxApoOhDSQwnUFxxrvl4oAWHut6ySmOPv95B17kqiZeyAxG3LRc4ypS0zNrwivFakG21FESEBOzl5XnJ8S11Wy4kf3hLSIZHig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویس‌هایی لو رفته از ابویسانی، معاون وزیر اموزش پرورش حین گفت‌وگو با دانش‌اموزان معترض ؛
دانش آموز:
نه اجازه میدین تشییع رهبرمون شرکت کنیم ، نه اجازه می‌دین پیاده‌روی اربعین شرکت کنیم، چه کار مهمی الان دارین؟
+ ابویسانی :
اربعین بخوره کمرتون!
دانش آموز:
ما می‌خوایم تشییع آقا رو شرکت کنیم.
ابویسانی:
برو بابا تشییع تشییع..
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67308" target="_blank">📅 00:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67306">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/etT27LrCQCW8mecKDaZTgaizz_qzujqHGq-FQvx0zyxwZvAPDFTxzXcuP-8-pqaGAWvz_QXR6ofBqpBq1upT3pQl2A3Nd-XSdtIPrncGI7VezZFdzCQIHRbtr7SdHZZA-pBoi7EfkTmDDyxLMPtsjCNltUn6aMoVzHFIwoZb2wHdLDApx9UmJOTAPaX64MZheMS5Gy5lRFw4vE8CCyAy7jDsmskbCuqDVzUHsUolLPMwJ2eWlt7DGLZUMxrAwdZU57zbi9klSckDBJIbLRTwMo1aW-73Q58uINm0ZEo6fIM_6C-PlPFDI2gg1VDKOdVt4j2uarSwZmemyeTaoh4aYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7ffa7579f.mp4?token=qWV6du39_y3Tge7ku38R4GJDP-4DYBlJbbSRTqrI6PUl4Gjc5L8FBbL5OKxBshvXsRaCjzQQsDVWooenOX-7lXMn-SalUI-GTpmYgwM4xX0ouwvRg0xbJ5VtsAfOadkzTJ5kPjFFGU-4xdJlqigie2TqFadhleKTkmhU6EPKvHm5lsRqzg7eSSfpjgnjmtaqTh6rXFOSd_NqPx0cxELA1Md8d6PXlnaXWkccY1j0tnTPLu8lIKg1AwUiO--vSlxnPr1SMf8Z2fVxEcrKObnzXlgYOlSBoxc14-RcweZXGP1A7CFipabBRug07UP5nD2dDJ7uzupYJqiNSZ7ApP934Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7ffa7579f.mp4?token=qWV6du39_y3Tge7ku38R4GJDP-4DYBlJbbSRTqrI6PUl4Gjc5L8FBbL5OKxBshvXsRaCjzQQsDVWooenOX-7lXMn-SalUI-GTpmYgwM4xX0ouwvRg0xbJ5VtsAfOadkzTJ5kPjFFGU-4xdJlqigie2TqFadhleKTkmhU6EPKvHm5lsRqzg7eSSfpjgnjmtaqTh6rXFOSd_NqPx0cxELA1Md8d6PXlnaXWkccY1j0tnTPLu8lIKg1AwUiO--vSlxnPr1SMf8Z2fVxEcrKObnzXlgYOlSBoxc14-RcweZXGP1A7CFipabBRug07UP5nD2dDJ7uzupYJqiNSZ7ApP934Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بعد از مزدوران نیجریه‌ای حالا یک فاطی کماندو از بوسنی و هرزگوین ببینید
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67306" target="_blank">📅 23:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67305">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af68b2c3a9.mp4?token=P8qMe9H2-gwXrwZbkgdiY7JRaJQLxsc88qbG1hUbsdufrIQ5IP9jxqRvclxaPOavGHY6TWanSYXp_wMjo2s2rNSO2c_cF_mc3Vo2xPPNewKrR9hUbFMQoYHKZlYh77m1eaQB6U1dFFOc9Q_KimKphG_VgpIe8E7P1KxOIvUa1mK5mlbvpIdXqjXcW_kiaSOsmVcXtRfPC_vCYVZ_KFMXhSMen_7H1PXoxD2jTD2cN3zgSeE5EYglW9ONnC6ZEPvwVmtZhsw0LslnmA5t_UcKXMXvO0VFhJmvuaJQ4p4M7RdJUrNrV0-CtN9vMRrdD36w3C_JfHyzF_kx-YmjrPtEZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af68b2c3a9.mp4?token=P8qMe9H2-gwXrwZbkgdiY7JRaJQLxsc88qbG1hUbsdufrIQ5IP9jxqRvclxaPOavGHY6TWanSYXp_wMjo2s2rNSO2c_cF_mc3Vo2xPPNewKrR9hUbFMQoYHKZlYh77m1eaQB6U1dFFOc9Q_KimKphG_VgpIe8E7P1KxOIvUa1mK5mlbvpIdXqjXcW_kiaSOsmVcXtRfPC_vCYVZ_KFMXhSMen_7H1PXoxD2jTD2cN3zgSeE5EYglW9ONnC6ZEPvwVmtZhsw0LslnmA5t_UcKXMXvO0VFhJmvuaJQ4p4M7RdJUrNrV0-CtN9vMRrdD36w3C_JfHyzF_kx-YmjrPtEZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیلم خاکسپاری رضاشاه بزرگ در تهران، زمانی که جمعیت تهران فقط ۹۰۰ هزار نفر بود و بیش از ۲۰۰ هزار نفر در مراسم شرکت کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67305" target="_blank">📅 23:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67303">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jf8DCCuZkLZBmiqGNtyxj7x7uXC2dsWxukLnriR2NWS9RrQpIYaew7DErSbNpG8xKGuhXPd_rnugmpkTxZ-1WKJ1vRzgxosb7DJAlFMR7W2-WMIMXajzJ4eTDaP1Bp_-_R05U5nzd91S6leflGwILepZhSEeMDPqjQSGKDvGT0jrDDujmre0T9andjIVruYUWEhE-KgAmdZZA7qkPWqYz3xEyhFs7asVsqlzCWM8oad30_UaFfqm360twrMeke03aRBT_x738UXZPMgDKA4vJG0nFbFbBg5llvnkLD905BSRhkL5lkVOuyPpFIAG9TH2tR4b87NUTCQDk3vnx-0zyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ac-f25vEiUQoZmu9eC57oaCSgt9IJix03hwPXskA5V5kQifelEm-IUsnC078x9pGF9S1j2q6sFHQ53AqLaxiwfJzqNwuEArm0A2zumHzR4Xz2clezx_J36u4sENZQVZS3_KQILW-DTHXIAdx8-WjE9FuDij842QKlJ7Ky-C-84pyS4yqWZLYVZLxA6QGBUD8vBjCBqwUhIglyiTeVmpPDH26_fgPsYkaNO6elMp7seMnEaxlW2pyiGaBm4qWnJcl0RdEqEnLkr7XRBCo9sPqec6stnqnQamfBpdctas_jOVP-RjtyWcLLod2JK6Jf-xBqHm1INMNTma9QIFfLQUzAQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
زمین گرده...
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67303" target="_blank">📅 23:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67302">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ihn0qdsumUdpMXsdTam0n0hPsnY2mh-nqS2d2CLESxPDGPwpNVtDQb5FZhJnkNwEmBmKE8XifNCTQwlm7Yd4N8VIAcgdOBfTi-pE5hNo5syfENQgdG2gNW6xxubMX9t96w01QuoL7kw38h4BtQgXIYUOIjYRvfRExeJd8If8662nC4tdLldtUflpU4VnsEMj0_wLObWqqXKtZ44vRb_01YiteQD-NytaikzVMnckvJ9nD68aqhgv2jxr9Jf87mqYVOLHv8rgsRxTDOp4YC1ySKG2f-zVnJ8eoaRBGjmH8PlOhgSSGmZM0JlMForITRJ6O3FDSu8Jo0NQxVcPIn9Y0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید:
دو مقام آمریکایی به من گفتند که مسیر جنوبی در تنگه هرمز همچنان فعال است.
یک مقام آمریکایی مدعی شد که اکثر کشتی‌ها با سامانه شناسایی الکترونیکی خاموش تردد می‌کنند تا توسط پلتفرم‌های اطلاعاتیِ «منبع‌باز» (Open-source) رصد نشوند.
این مقام تأیید کرد که ایرانی‌ها تلاش می‌کنند از طریق رادیو VHF برای کشتی‌ها ایجاد ارعاب کنند.
مقام دوم آمریکایی اظهار داشت که سرعت تردد در مسیر جنوبی طی روزهای اخیر افزایش یافته است (حدود ۵۰ کشتی عبور کرده‌اند) و این مسیر همچنان باز است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67302" target="_blank">📅 23:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67301">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0711bc2f95.mp4?token=DPMbFRfrNVeJByOZfMomXSwz_1hgGmr5sUwG2DmOo1qd-P2qkPG6VaRKBUJQlHPAkbCMO25c5idDdI57paZoPCiRwCQmgtQdtW6STL8gN6xA4fshXgt6iZVIYY208kRw67jc66ydSmrbEVrxga8MUApE1rHDdXva4bNjz1wZgly5t_H4l4PzF2U6eXPMaYSG0HgIKzjlKkltLIURHIhcjaUN41zohe4V0uBXyeZb-oAPoWrL3XX5NKp_yBkHFmezntcXQdUKm41IpMvj4lpiRKRmdqW0T2-liEb4kjK8FhqGVokxARx6rRuFLwkBvZE2tgNvY7nNp4DCugFBkmbH1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0711bc2f95.mp4?token=DPMbFRfrNVeJByOZfMomXSwz_1hgGmr5sUwG2DmOo1qd-P2qkPG6VaRKBUJQlHPAkbCMO25c5idDdI57paZoPCiRwCQmgtQdtW6STL8gN6xA4fshXgt6iZVIYY208kRw67jc66ydSmrbEVrxga8MUApE1rHDdXva4bNjz1wZgly5t_H4l4PzF2U6eXPMaYSG0HgIKzjlKkltLIURHIhcjaUN41zohe4V0uBXyeZb-oAPoWrL3XX5NKp_yBkHFmezntcXQdUKm41IpMvj4lpiRKRmdqW0T2-liEb4kjK8FhqGVokxARx6rRuFLwkBvZE2tgNvY7nNp4DCugFBkmbH1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مردم اروپا با دمای نهایت ۳۶ درجه
🆚
مردم خاورمیانه با دمای حداقل ۵۰ درجه
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67301" target="_blank">📅 22:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67300">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eda932d9d3.mp4?token=EIeTU3oN-GQ8scy7YbbrFLRH59uxBbCFVHEcjEnHaIPfrmnRzSggbAml8KHZ_zy_XV1aWAg_v-yc4u6ZGeO6nG8fia-WV287iU2lvHpu7pGwvcgWLyBi0P7JglcBXHfQjMg6fOO7EXoHy-CgsBX7Q3XbH23Uo0TmmsT2QaWBungCPmTQYYYH5isuBfjbAeLAjM6d_PQe0PNMxcQLV-NYOWZO0vdFGyOrgXZCTcvBnbq3dCuvRbqqPulG5eNP7zDLvBWxFTZFI37KxPpdnYEC4m4RkEuK3Uqj51uxfbzJpd2hKnHBQ8Vj0BN_KDo63CRjh1IieDSKrewdaGdF2iJYMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eda932d9d3.mp4?token=EIeTU3oN-GQ8scy7YbbrFLRH59uxBbCFVHEcjEnHaIPfrmnRzSggbAml8KHZ_zy_XV1aWAg_v-yc4u6ZGeO6nG8fia-WV287iU2lvHpu7pGwvcgWLyBi0P7JglcBXHfQjMg6fOO7EXoHy-CgsBX7Q3XbH23Uo0TmmsT2QaWBungCPmTQYYYH5isuBfjbAeLAjM6d_PQe0PNMxcQLV-NYOWZO0vdFGyOrgXZCTcvBnbq3dCuvRbqqPulG5eNP7zDLvBWxFTZFI37KxPpdnYEC4m4RkEuK3Uqj51uxfbzJpd2hKnHBQ8Vj0BN_KDo63CRjh1IieDSKrewdaGdF2iJYMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پیام نتانیاهو به آمریکا به مناسبت دویست و پنجاهمین سالگرد استقلال:
🔴
«۲۵۰ سال آزادی. ۲۵۰ سال دفاع از آزادی.» او این مناسبت را به عملیات «انتبه» در ۵۰ سال پیش (که در آن برادرش «یونی» حین نجات گروگان‌ها جان باخت) پیوند داد و اظهار داشت که آمریکا و اسرائیل در ارزش‌ها، سرنوشت و مبارزه با مستبدانی که شعار «مرگ بر آمریکا» و «مرگ بر اسرائیل» سر می‌دهند، اشتراک دارند. یادآوریِ یک اتحاد مستحکم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67300" target="_blank">📅 22:12 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67299">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lCVw9MY5L_ZzfiNA_uQl8rQNPK04xTncKavkgSnhtkUKDaq1nogcIEZ8QQ3PP0kVE9_N4fw0QSS_BJLTjN6wTiDZtEuhbrgz5D5d7NK3TKj7KuQlej7GxWO07BiDKNql69AlA2huksJJ6qIbMKfwnEja1VVQ_CsHRV07phB7aFYwQ6-P7fHJH6l7WteSX2z53skCLthni98UePICwA3wYjuacutkNj7pt4MhiSe9R3qY_ZH-pbz4mNZVLyh58Omu37oNfu97SWMog7Zf-O4YVPXwQowtebPM9Z10uFhGy0lKEZGWdo0BcUFCDETSYI5xkWQvSYXnbBeVth-YgcZOPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
العربیه:
دور بعدی مذاکرات ایالات متحده آمریکا و ایران در تاریخ 11 ژوئیه (21 تیر) به میزبانی پاکستان در اسلام آباد برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67299" target="_blank">📅 21:25 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67298">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EcGDciAn9yH0rJS0lQDwJcXg5WKkHfcvm2z-hU9K93vbgw1VHV8fdvgB_ZcdYIfBzlFK5Ggiajj3amV-Xkp_xZWis_PuzrgXp68iZzbBZt5d1VvnDPU0tuGsi75FCxkORjts_L1gHbkmfW8Gr7bNTWSx_iJ1DqTlbM_zjpg1iDaP021ZQFxqGWna3LjYWr5XelzZFo-KPxh7VvAdOIF9zKc5YimVCkK4OEg36XXPsGjPtpWXdujZuMFAD7usksmnV6KEDg0BjGoCu0sT_Wd8V_8UuoaqKC4vbXGj0-j4orpOQcV5Y0XxdaOHsdwjh2oZNjBFkIRKT3SniXvYh1Yu8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترامپ:
فکر می‌کنم آن اشک‌ها مصنوعی بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67298" target="_blank">📅 21:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67297">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TFAq2Pv5HrvI23KV0XU_5q3SP_6grl-c6qwdWxj9uUKoNSsg_imIOELBzznT8Ib5fY125IQ3nsw8U3VJh7MWQdt6B_hvdz8mPfrc34ICVM26DqAly6NzHeeCqoXzZaCiYOKxxf5ovZAeEdi6upiznqIiuqYH8A2xehiGpaVrX1i-2bp43Oaek5tE75wzA6KuifzR15LoiJ6gCcIDBL2Ft2rNyZlyNa41CaY9VoupUwoj9lsRVrnH9RLuDDPQfZyC6q0qBRn_vnxbuP8wQhzL32kVLPqEgwxAPazJ9W0mbEkIZ5vHOjEMMnuMdaweyEVQEx--mwOLMuyLLtPMP1r2Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ به آکسیوس:
نتانیاهو میداند رئیس کیست.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67297" target="_blank">📅 20:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67296">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
پرزیدنت ترامپ:
نتانیاهو درخواست ملاقات در کاخ سفید کرده است و این ملاقات ممکن است همین هفته آینده رخ دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67296" target="_blank">📅 20:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67295">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ به اکسیوس:
از دیدن ایرانی‌هایی که در مراسم خاکسپاری خامنه‌ای گریه می‌کردند، شگفت‌زده شدم. من فکر می‌کردم مردم از او متنفر بودند.فکر می‌کنم آن اشک‌ها مصنوعی بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67295" target="_blank">📅 20:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67294">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
🚨
پرزیدنت ترامپ به آکسیوس:
«همه آن‌ها آنجا هستند. یک گلوله [و می‌توانیم همه آن‌ها را از بین ببریم]، اما ما این کار را نخواهیم کرد، زیرا در آن صورت، هیچ‌کس برای مذاکره با ما نخواهد ماند.»
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67294" target="_blank">📅 20:48 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67293">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/589cc62912.mp4?token=J1D7Jk9Jt4VNeoPkF4EYbQA3dsn4THGqknDKEjAhg7k9zKJrNg-x9bdevKj8wun6doEGiwbdLSjsImYBDhtpeUtmJaY16EnI-SJYGg3IJ6nP4UYtNMxOnultPFdr8quUiwTDxsAclZ2xgPjebcb1FLgZwSOj4H8ZhqiKSEmN0vZRCwb9MRNF5JxLlZHakH3fJJYIz1Fk65V2pLHuVhW4Sd5N0UXcrqzRQ1Zy2Ww_Nqj2EkCK_NSU9wP27Y9uQOCVRBCBl_Dq-T7bvZ2HPBXN56CushC55U8CxclcKqxyC1C4VmJ5dBAV2BqlF-f4tqZmpqrpOypOm5M1CTHOSQGK-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/589cc62912.mp4?token=J1D7Jk9Jt4VNeoPkF4EYbQA3dsn4THGqknDKEjAhg7k9zKJrNg-x9bdevKj8wun6doEGiwbdLSjsImYBDhtpeUtmJaY16EnI-SJYGg3IJ6nP4UYtNMxOnultPFdr8quUiwTDxsAclZ2xgPjebcb1FLgZwSOj4H8ZhqiKSEmN0vZRCwb9MRNF5JxLlZHakH3fJJYIz1Fk65V2pLHuVhW4Sd5N0UXcrqzRQ1Zy2Ww_Nqj2EkCK_NSU9wP27Y9uQOCVRBCBl_Dq-T7bvZ2HPBXN56CushC55U8CxclcKqxyC1C4VmJ5dBAV2BqlF-f4tqZmpqrpOypOm5M1CTHOSQGK-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
۲۸ دسامبر ۲۰۱۱؛ مراسم تشییع جنازه کیم جونگ ایل، رهبر کره شمالی؛ مراسمی که تصاویرش به یکی از عجیب‌ترین صحنه‌های تاریخ معاصر تبدیل شد.
وقتی این تصاویر را می‌بینیم، شاید اولین واکنشمان تعجب از شدت گریه و شیون مردم باشد. اما واقعیت احتمالاً پیچیده‌تر از چیزی است که در چند ثانیه ویدئو دیده می‌شود. در کره شمالی، مردم دهه‌هاست در یکی از بسته‌ترین نظام‌های جهان زندگی می‌کنند. از کودکی به آن‌ها آموزش داده می‌شود که رهبر، شخصیتی فراتر از یک سیاستمدار است و باید بی‌چون‌وچرا به او وفادار بود.
از سوی دیگر، در چنین حکومت‌هایی، ابراز احساسات در مراسم‌های رسمی همیشه یک انتخاب شخصی نیست. بسیاری از تحلیلگران معتقدند که آنچه در این تصاویر می‌بینیم، ترکیبی از باور واقعی، سال‌ها تبلیغات حکومتی، فشار اجتماعی، ترس از حکومت و گاهی هم منافع شخصی است.
شاید مهم‌ترین درس این تصاویر این باشد که وقتی دسترسی مردم به اطلاعات آزاد محدود شود و فقط یک روایت سال‌ها تکرار شود، همان روایت می‌تواند واقعیت ذهن بسیاری از افراد را شکل دهد.
تاریخ بارها نشان داده که پرستش شخصیت، فقط به یک کشور محدود نیست؛ هر جامعه‌ای که آزادی بیان، نقد و گردش آزاد اطلاعات را از دست بدهد، ممکن است در همان مسیر قدم بگذارد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67293" target="_blank">📅 20:12 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67292">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/648e669177.mp4?token=aJI-nrBwlqTYEIR1DYM_Alt5Zd66P19JcjGrbP9ssZDGCckSH9lwwb-kcGAy9II8NiEqsoyxvp3aW4BKVBD3dfuAq_LBk-y6_0-V7-Z1vEbzqNZEDqeTmjiCMqBR-wx46bQOkNTrUWknTbaZAByAPC62Rr6TZo2m5p0A05ywV9U0onAqi_jJ-pBA5RCUIoO4HSEnbltlpgMCU_IhRTfBjNV69JPZTkPGELrTF-JWkczte-1zbbnbLyL3F5dL7pXncOdMiQhdGG8YbjUt9X0Vf1GZHKWTmRMtCxWtcCBOkx8Twfp5dL0JqXrOWwxBrpvE0rUmzVm4hhav6gyFjF9-iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/648e669177.mp4?token=aJI-nrBwlqTYEIR1DYM_Alt5Zd66P19JcjGrbP9ssZDGCckSH9lwwb-kcGAy9II8NiEqsoyxvp3aW4BKVBD3dfuAq_LBk-y6_0-V7-Z1vEbzqNZEDqeTmjiCMqBR-wx46bQOkNTrUWknTbaZAByAPC62Rr6TZo2m5p0A05ywV9U0onAqi_jJ-pBA5RCUIoO4HSEnbltlpgMCU_IhRTfBjNV69JPZTkPGELrTF-JWkczte-1zbbnbLyL3F5dL7pXncOdMiQhdGG8YbjUt9X0Vf1GZHKWTmRMtCxWtcCBOkx8Twfp5dL0JqXrOWwxBrpvE0rUmzVm4hhav6gyFjF9-iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
▶️
داده‌های تارنمای ردیابی پرواز «فلایت رادار ۲۴» (Flightradar24) نشان می‌دهد که یک خلبان آمریکایی در آستانه چهارم ژوئیه، روز استقلال ایالات متحده، با طراحی مسیر پرواز خود بر فراز ایالت اوهایو، عبارت «USA 250th» را در کنار نقشه جغرافیایی آمریکا ترسیم کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67292" target="_blank">📅 20:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67291">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
خبرگزاری مهر : مراجع تقلیدی که‌ قراره نمازِ علی خامنه‌ای رو بخونن که همچنان خبری از مجتبی خامنه‌ای نیست!
تهران : سبحانی
قم : عبدالله جوادی آملی
مشهد : نوری همدانی
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67291" target="_blank">📅 19:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67290">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cc795d411.mp4?token=BCdB3D3F_ig3eNLwTGyZvEF9D5nwcCpUMbK0jZJMIieHKQbnCznuCUTZ8tunkoFBsZRVqrShqq0KOjOGpZZ4KIQ0dziLpQBbNeOAsmLUPRMnkkAZdAXwkhl6N8kB5Ptge1zL94BcGble7m-ZGGSg-hTbcgW7yMNrxa3ElMMGT03GQF3nIqzsaNxS55YDPaoRJx5Sx-D27TCbSWpNfNvq3hMJVHF92k8Qb8qpSFxW6ikj0vG2kVluh34illhlIqYIQEKHwvtBemnudcV8prY8WRTgRti-npkl3i-Grh-DXXowXgBvGA_1rN0wNDbITWvt5_2spvzJFDuo2pRFiSUZIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cc795d411.mp4?token=BCdB3D3F_ig3eNLwTGyZvEF9D5nwcCpUMbK0jZJMIieHKQbnCznuCUTZ8tunkoFBsZRVqrShqq0KOjOGpZZ4KIQ0dziLpQBbNeOAsmLUPRMnkkAZdAXwkhl6N8kB5Ptge1zL94BcGble7m-ZGGSg-hTbcgW7yMNrxa3ElMMGT03GQF3nIqzsaNxS55YDPaoRJx5Sx-D27TCbSWpNfNvq3hMJVHF92k8Qb8qpSFxW6ikj0vG2kVluh34illhlIqYIQEKHwvtBemnudcV8prY8WRTgRti-npkl3i-Grh-DXXowXgBvGA_1rN0wNDbITWvt5_2spvzJFDuo2pRFiSUZIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
یحیی رحیم صفوی:
بین ایران و اسراییل جنگ موجودیتی است یکی باید بماند
.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67290" target="_blank">📅 18:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67289">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v04eF-kFX1SnsWnpSEIrCX8d9x2ERyAI7e-hbJ6k4TsLcucAkdcgai6XJBMU4seKE57k1nH4xQGazTb3lTfL945IRWsiNBSZtnY9290ECFZcrtkF7_atUoWezCib7eG9d9UCRxO3UTPZMFqr5UHr_aJJCmZrP0gl3uJR1a-Bgg2HShAi1sGxuAt2iscrUNUttFJMZ33y-eN1NgUwAISrz3qXhVAt3Qj5wyxqHwUCsyS4j1jcVzZk97GRNhcgodzQLrSGmRsT3h5vlcNBdJXfH2EawwtGusjZ-gZ4pzne0oiwugpHdSItHJOYx3EsX-a1zepDXxvol3Kc_SNtCCLP5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شاهزاده رضا پهلوی:
🔴
خطاب به نمایندگان خارجی حاضر در تهران برای سوگواری علی خامنه‌ای، دیکتاتور فقید ایران: ایران در سوگ او نیست.
🔴
ایران سوگوار بیش از ۴۰ هزار فرزند خود است که در روزهای ۸ و ۹ ژانویه به دست خامنه‌ای، قالیباف و ماشین سرکوب آن‌ها به خاک و خون کشیده شدند.
🔴
رژیم مبالغ هنگفتی از ثروت مردم ایران را صرف برپایی این نمایش تبلیغاتی می‌کند، حال آنکه حتی یک رهبر دموکراتیک نیز در آن حضور نیافت.
🔴
آنچه امروز می‌بینید، ملتی نیست که در سوگ حاکم خود نشسته باشد؛
🔴
بلکه ملتی است سرشار از خشم برحق، و همین خشم و دلیریِ قهرمانانه، بساطِ باقی‌مانده‌ی این رژیم جنایتکار را درهم خواهد پیچید.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/67289" target="_blank">📅 17:54 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67288">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20335e95a0.mp4?token=grgOig-1OKxyjsuF1Wxpk22-Snqm4u_6iUHeVVUENjNLedkXNmO5gYVvsO7ThhLFf58nECQrJT680W4nJW-_ZzRNBtH-7oPcaB0feGISBlSYVxWuDQukSFP3jr_vzqFRdNdXqeQlMTi1I7Oiqllnpiprk830M6lSm-zUNAiATtLgjhi9MGnDtqcfWHTrWE04HfWZIE85oxG1VRTJ1UIKU2FGpQ3bKdlKtHFUUmFBt4o-YK7U_INXg7Qia6JxHjUWp75-PYMwHkcXQ-OOrW14lBLyCizINgNLWvmCK3XreMkPRNlq2okygADVyQbCdKtmNdf2ciJ2ziKVjyFiSLwgnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20335e95a0.mp4?token=grgOig-1OKxyjsuF1Wxpk22-Snqm4u_6iUHeVVUENjNLedkXNmO5gYVvsO7ThhLFf58nECQrJT680W4nJW-_ZzRNBtH-7oPcaB0feGISBlSYVxWuDQukSFP3jr_vzqFRdNdXqeQlMTi1I7Oiqllnpiprk830M6lSm-zUNAiATtLgjhi9MGnDtqcfWHTrWE04HfWZIE85oxG1VRTJ1UIKU2FGpQ3bKdlKtHFUUmFBt4o-YK7U_INXg7Qia6JxHjUWp75-PYMwHkcXQ-OOrW14lBLyCizINgNLWvmCK3XreMkPRNlq2okygADVyQbCdKtmNdf2ciJ2ziKVjyFiSLwgnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
روایتی تصویری از شاهنشاه آریامهر محمدرضا شاه پهلوی:
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67288" target="_blank">📅 17:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67287">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‼️
ادعای نیویورک تایمز به نقل از ۴ مقام ایرانی:
پزشکیان به مجتبی اطلاع داده بود که در صورت عدم توافق، از سمت خود استعفا خواهد داد.
نامه‌ای از رئیس بانک مرکزی ایران باعث شد مجتبی با یادداشت تفاهم موافقت کند.
پزشکیان، قبل از امضای توافق، به مجتبی خامنه‌ای اطلاع داد که محاصره دریایی، ایران را فلج خواهد کرد
.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67287" target="_blank">📅 16:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67286">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c90b7a34aa.mp4?token=u2WCQwRdfcEStaZT-q6sGT-M4pE0xW9OLHMv-x00NSlKRemztNA4jmqtpmLQeXihVqMc5SgJSFE0st9M_hlm9_qx_3PlZ2DkpJ6-gSEWs0F4tOPEFsftz7CgyQqg4cgmlXVu9rjm_LLEVwCU13MFxUsV2-gRY6iT8z7TMNToZ_BpYCnWY-eIGpVGvovJ7ger1nYrxE7a9WT_6vrWPL31-3z_Z8USkmWZLlDXMmLHiz8BusI3WWXzyr12iYa_k4-W2vr_J1aexx1soZuxVArJapsUi2AOAUZcQUf8e1x9tvlGzuPTvhRgZI1XOnYDM_WBpaDApEXg26KZQSf015xxng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c90b7a34aa.mp4?token=u2WCQwRdfcEStaZT-q6sGT-M4pE0xW9OLHMv-x00NSlKRemztNA4jmqtpmLQeXihVqMc5SgJSFE0st9M_hlm9_qx_3PlZ2DkpJ6-gSEWs0F4tOPEFsftz7CgyQqg4cgmlXVu9rjm_LLEVwCU13MFxUsV2-gRY6iT8z7TMNToZ_BpYCnWY-eIGpVGvovJ7ger1nYrxE7a9WT_6vrWPL31-3z_Z8USkmWZLlDXMmLHiz8BusI3WWXzyr12iYa_k4-W2vr_J1aexx1soZuxVArJapsUi2AOAUZcQUf8e1x9tvlGzuPTvhRgZI1XOnYDM_WBpaDApEXg26KZQSf015xxng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شعارهای عجیب در تجمع شبانه علیه قالیباف و آمریکا
😂
😐
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67286" target="_blank">📅 16:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67285">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/441130dd0d.mp4?token=Esqas93-n7m0xvfUtMerLBA4lvLr5xiTN623oLQ05yq6c5bgh1GFLCBsXsgljFMZBT6UKBMXyV6OBnoBaGBeflSsRiPGqUYRL7_fsi0bmv-JwSyqGmaNOQHmlvqBUEm_AOSesg78SZiztgxQLVqMgA7DTyI3mXAlN_wXZL5zU36OrryrATvEZvlYpXBepxalHXC637ujzEWhIhTicg1wYvxfyss0VGE_VU1JA1Mr6gauUCbno-BEvE9GZpcM_lHXkk2LNarAx1SwvwR8VhdSJkL-bBzExoz0B8Y3EP76e88gBgctNkKcx8xTx8XvNtlGawn4K9W4y_zb7PFAjHgzbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/441130dd0d.mp4?token=Esqas93-n7m0xvfUtMerLBA4lvLr5xiTN623oLQ05yq6c5bgh1GFLCBsXsgljFMZBT6UKBMXyV6OBnoBaGBeflSsRiPGqUYRL7_fsi0bmv-JwSyqGmaNOQHmlvqBUEm_AOSesg78SZiztgxQLVqMgA7DTyI3mXAlN_wXZL5zU36OrryrATvEZvlYpXBepxalHXC637ujzEWhIhTicg1wYvxfyss0VGE_VU1JA1Mr6gauUCbno-BEvE9GZpcM_lHXkk2LNarAx1SwvwR8VhdSJkL-bBzExoz0B8Y3EP76e88gBgctNkKcx8xTx8XvNtlGawn4K9W4y_zb7PFAjHgzbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
😐
ویدیوی این بسیجی که در مراسم تشییع علی خامنه‌ای وایرال شد!
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67285" target="_blank">📅 16:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67284">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/67284" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67284" target="_blank">📅 16:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67283">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
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
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67283" target="_blank">📅 16:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67282">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zb8dN49v0hn3sniFbl8PiZjOI2SzQjHYGw5Jq1CJJS5fI9HjEv3bWmYmw5oqm9Tsz416e48Znh-gRpa_EwaB9nVAjsovwWj5YKlz9HdivL_hE25oUgY1GDfHd8fwDlw27DX5iwNV0rJe1bIyQsIrzkp7n2g-2EWe2s8vpCE9G7MD76xCfuxjpwnxvrFsphIMx8aamHHN4P7eQakAMQjGr63vZhVhrsFD1fLidG6xbuvWrKICvC8SSDp0L513VGNCNkIS4rPJxPGqItdLRMQ_t4vQOEqIH12tPQibBSSP9Lv1q9GOlDi-VwMma0InyAqh9sulib5NUd2ESto3YOFXSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علی عظمایی فرمانده جدید نیرو دریایی سپاه پاسداران
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67282" target="_blank">📅 16:27 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67281">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
با تصمیم هیئت دولت، کل کشور فردا تعطیل شد
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67281" target="_blank">📅 16:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67280">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BzietPP6eWcbCRJqr2LI_DWqMgQnthgMXvja_Lu-0nqx2zIshnOFn6POrlz3_iUXamATKLV_3LVFFEGoiLNbkJy8PflWLUJ07WwXPqspdcC9C4NYQwmE-kxUecVoJFuL6WFLkVp5lT3jRwzZWCqahVx7DF1qrvOko38X77_xBJhfL6_fDopU-pUauz_tsWK5stSvI5yaAkF3JaUUYyghj1zwzenKkTEHpyMSg9C80jZCmFHB-C_RCB1u2O7b5MbuH9p4WejYF2ustR0YxLjKoXqoXbl2w_9gyfPAvF46413q79W59cCw8eSrfu23cLvmC34_rcdqcfiAX_68W4c27A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
نیویورک تایمز به نقل از منابع آگاه:
🔴
مجتبی خامنه‌ای به مقام‌ها گفته است می‌خواهد در مراسم تدفین پدرش در حرم امام هشتم شیعیان در مشهد، که برای ۱۸ تیر برنامه‌ریزی شده، شرکت کند و نماز میت را بخواند.
🔴
مقام‌های امنیتی تاکنون با حضور مجتبی خامنه‌ای در این مراسم مخالفت کرده‌اند، زیرا نگران هستند اسرائیل از این مراسم برای کشتن او یا ردیابی محل اختفایش استفاده کند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67280" target="_blank">📅 15:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67277">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nfCG03vp7m8HGlPe0BwdCMOf-nVMUmMr7md8E-_LHHpPx8L4MwXVQU99khEV6Fh6dxAhD6eekvRr9BAsb6EdTVIBjqJUYXwb1_qphBZqjTSdqZp9d4TrcI1-qRjfkI5GvQusuEBAU50cZHa_YEQrn3wLSlENtCCbBETIx0TlGKVv7n8JWuynLsteT8EuuRYu8ustTvUxZkGEyrmO6sOFzeBcjGJQn5XjMy9wnjUeIz09z3B_mj4zdVz33NeOvxtmXE5PEAjXvWhKCTNC9uYmD6K-AYWDp0vwOszw1EzZgz7hcWWyCygP4_lyvRBEqxG8gMkGCn85guFmtmvXQPkcZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MspUhJK0LBIGg-pKRu4bwq1GhCz4EEkA4tgjlqyWfPoGmIht9-6M4vfU05qua3DBx6RATiH4m1zVLj9xd4OZ5DHvE7ejxNYynSTdedDG-LQ4V8RvOf500V2bwCEyK9rdWuSR7paLhRDyJDB72MMSYS6glu5zzDG7TmmtpiVV-zr0DHcvv2fCFB8GWPYS0AW5uRQozN_Z7J-yys1EU7WYxNOC5AfRD3kQEalI0NOgvay5AXwd0RNEXzkd-FnG_SuEJPI8GAJSIA9_J1h7EEx6GTcmCJsQO2YbYRrQL10Jhfp6msB6WGGVShwEjC5iX5HvZDy8Ny3PmhRsFjQc9krWEw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/502fac7d76.mp4?token=CU0v63dsv17j0MwLDfgcn_ikhrwZrpzBhnccQNvvhiMX-9XGB3oS-HGv6kTNAI4lpN5IHBr0dDDoTIvi20dh7uCYithAQS_lsmDMtBkoNSD6Pxdv4OjX4_bMehddR1OYxwHWSr--DPe0Jxmad66LKUxetPjjSp9OOwE82sFrkjSUanGK52J4TAyjzWPe6eqKnI363aQq5nONDoeLSQ95kN2cA5gi2CppuOOb9hijXtPUhYHIhNk5TLygwr3O4RgVMQGPG17YahP2U8b9-aJi8-TRfcvZBA1ZYkEAbLvAsiv5eqS1qGDjIER6fG3z1sghPcObpzuCaLTXDgkgYfWSMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/502fac7d76.mp4?token=CU0v63dsv17j0MwLDfgcn_ikhrwZrpzBhnccQNvvhiMX-9XGB3oS-HGv6kTNAI4lpN5IHBr0dDDoTIvi20dh7uCYithAQS_lsmDMtBkoNSD6Pxdv4OjX4_bMehddR1OYxwHWSr--DPe0Jxmad66LKUxetPjjSp9OOwE82sFrkjSUanGK52J4TAyjzWPe6eqKnI363aQq5nONDoeLSQ95kN2cA5gi2CppuOOb9hijXtPUhYHIhNk5TLygwr3O4RgVMQGPG17YahP2U8b9-aJi8-TRfcvZBA1ZYkEAbLvAsiv5eqS1qGDjIER6fG3z1sghPcObpzuCaLTXDgkgYfWSMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیشب، برخورد یک صاعقه با برج وان ورلد ترید سنتر در نیویورک
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67277" target="_blank">📅 15:37 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67276">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B8_5dPoXcSnwaqiXWGpyf27CgYv_0cd84ONC_j0tQvIb6acWsuh_f2jDIzxjubgv_ZdwpyinOHypLzEK9BoJ4gp0nAVZJHODC57s4vfqfEWUBAViYlEGMKvYGqvN42O1K9q5hOAm-3Ht-nBQi6o8DhTcwCuKsVuByY4x3bqJFJ1BLads7HlbpdACHvVVchPqCegOFsaA_2M0dtv722a56Bl2xiybJ2cCBiMUimn97EaEnNFTZHnPW_26Ak-V8tT_zPiUjiJD_q48uIld5xeMYt0Z5qSukezi7jbOPmZckLkGfIi07Xe2UZNlNO8lVF1VABCrXR7mhuCWsHQ-Umebsw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67276" target="_blank">📅 15:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67275">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/geRCY7lAdK4OpoF6_r7n9s00eITM0qj2GL6RexA7evOs0El7sbpmHIEdX2k4-Yg_O-tHM6fnCwKOk1MNnaQmWDtouI2t-M-ze-a1nr-acMVqAPzATh9zDTyplZxdO9qNcalba0gSdch4STqNONiWw9lu7jTqa8xGHC0PUEGan1xgmdQQfP54wmtxwrqqdzSVJDNmNbK5r8S8OXhE4Rn_FbWergeagkvEdDSaVIGVeTKHShnIShGLVVOoRd-UZbIabxwPawuNdaaEBt-dK2BKVXBUguDRfIrozw-EjEwfQqNda_b_3R-EkBm57C0zKdzyb2pymKDamq-grAT-AB_AuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمال مجازی‌شدن مدارس و دانشگاه‌ها در سال جاری!
🔴
میزان کسری گاز به حدود ۶۳۰ میلیون مترمکعب رسیده.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67275" target="_blank">📅 14:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67274">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jrxmSd2YCMfl_8cFg7d49GmisTrJCAzCeTfzRPe0E0g5ljJMuLIxOp19-2S5AZ4oRm9kgI1hNyEnyxB-ZjR63W_8C4kHUcgWMpA3X6eyhoQ6NadI2Pvs1dqtd1ny2-v4_-XC1VKElUnVYebfOpXpQTtTmkXKSE2gROkVkWIQIPsjVLi_PAppOtMrK30jIKsrqcAybTz-Z_PIhOjcwgj-jMlcNCKAA_mUxPcnibUVz513Fn-oB2qQeRf12XlQ8tN2aMTN65pSfN5mQhBmW-QBZqvsTltelA_6m_IPrx-6CTlqa6eCQsSIWwV0jvccehTb0rel6AFhR8lJhrnfFPX9Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برافراشتن پرچم «ترامپ را بکشید» در مراسم وداع با جسد علی خامنه‌ای:
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67274" target="_blank">📅 13:57 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67273">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2883f7592b.mp4?token=eKyuGDS3wEQchwiOy416avKC2-EymrLd1rakc01tVRirq5WUu8HafToEy_ErIirSy1IwafkwFmhWAdbDJYc1foRJgcysTv7jwWVD69MguaV6Ouadcyhryxnx8VWqdwxd-xHcEk8p2Y29u661Y4_vAjbypwHAWeoIPFB1svqxK3qCTMeSaxFHxNemVEUFCgtEC9E-dp_YTumPx9e7qyO_e6xzcGIfC82_T941cdd9CPZeG1lFLJcWs65QCH1M7Kw57VrglD6JUI9XOd3bczE-TFO1N-iiSCm52-AXW-vq_gjqTdVDJ9zKIr_LxiWTniG3UYzbkV5StbSpCmqh3bAUZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2883f7592b.mp4?token=eKyuGDS3wEQchwiOy416avKC2-EymrLd1rakc01tVRirq5WUu8HafToEy_ErIirSy1IwafkwFmhWAdbDJYc1foRJgcysTv7jwWVD69MguaV6Ouadcyhryxnx8VWqdwxd-xHcEk8p2Y29u661Y4_vAjbypwHAWeoIPFB1svqxK3qCTMeSaxFHxNemVEUFCgtEC9E-dp_YTumPx9e7qyO_e6xzcGIfC82_T941cdd9CPZeG1lFLJcWs65QCH1M7Kw57VrglD6JUI9XOd3bczE-TFO1N-iiSCm52-AXW-vq_gjqTdVDJ9zKIr_LxiWTniG3UYzbkV5StbSpCmqh3bAUZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش نکیر و منکر بعد از ۱۲۰ روز
😂
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/67273" target="_blank">📅 13:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67272">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F9fO5eQujpCBwcYLqB1Z6pveiaVYuolVT2RC-5tyVXCI0wK2ElNwNIgkRsPRo7024lokDAyEhKrkeJrF03-pMhY32f_aeWuz1F1vTlBYYGdUvPyJTxLHVGEmyHAu3DN7f-jwQ5wJ46YF2pLKIwbLKuqr2kQa-Q6FL1nIrn6eNwJzet8ESnTPBBTKYfMCZDN_FXakyk6f_bzQW-8jwuENrIPYGuAQ1NYUG8MaO1fy_-rVBrrjNePum3bRdATUBvMsKTSEO1PgtvcOcqeM8OQw_tJ6xwEXXBdj4Dryc6Uc0HYL7Y7IWbhxTOUMKveMcQoUpMg4cda09advC9oe0E4Dgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
التماس رسانه حکومتی در ایتا برای حضور در مراسم ؛ جمعیت کم است...
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67272" target="_blank">📅 12:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67271">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc8da4a29b.mp4?token=T7doiWBWEVBc4fS_xk_oMv4RHYM_7ZM-pn9KevAY1ltgzRAtBDMGhPTlAfc_sSMY5cczVPs0YP9IRbVRufHJ6DjOM0_PpJN5p7sJXov2uxZbpFVkTWgqigwtUm7QfVp59-nVL1axWco6drKr1hbqY8bV9cdfhOOz84zRmIENtrS3LRdAgVfUAjEEgfoqgYaCqiLuvclowXATxpfWjOejHUJnIHqD2sHpMhYvAH3c4KSvwjRWRfwDJixohrVIXVfzC4f8d8si8p3pnAZnhrgLeC_qququbKfDwZDp98lo_JTCzUJu7pbCCeP-kXJpAApoo8tnanaicnmQzEEDrWxj2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc8da4a29b.mp4?token=T7doiWBWEVBc4fS_xk_oMv4RHYM_7ZM-pn9KevAY1ltgzRAtBDMGhPTlAfc_sSMY5cczVPs0YP9IRbVRufHJ6DjOM0_PpJN5p7sJXov2uxZbpFVkTWgqigwtUm7QfVp59-nVL1axWco6drKr1hbqY8bV9cdfhOOz84zRmIENtrS3LRdAgVfUAjEEgfoqgYaCqiLuvclowXATxpfWjOejHUJnIHqD2sHpMhYvAH3c4KSvwjRWRfwDJixohrVIXVfzC4f8d8si8p3pnAZnhrgLeC_qququbKfDwZDp98lo_JTCzUJu7pbCCeP-kXJpAApoo8tnanaicnmQzEEDrWxj2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
ویدیو ای
از بمباران بیت رهبری9 اسفند 1404
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67271" target="_blank">📅 11:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67270">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccea9f87ad.mp4?token=KVqnu0w0kJid58NX5BhjwYq9rUH39l8YOI9Yw4dF6BlgZO55omDMclZwIBN1Hw2tUY-oblXXT-X3mEcZU2-QUezgVzlNeAR8ZBTOuXSQ2fGGYZwkErm1udlb6qUM58Nc24ri5np94NhopqQlmY5ATArJdywvifj_CLtFtR5scKdUqq2UMjWyoQzJ46N4a1KbkSnCpeMZaZ_pm0hfxWWMgFu8Y_vTPCIA9GIQY1j8H8wIHN3z_xm4RLlKb3UWdONNk4PZgNMAmLUhoIGdWD9jHi775rcE2Y6uP_mgCwHHasrC9O6MWeHKsuyRpiR7gothS_cz28oBtU-uegPlOCDPQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccea9f87ad.mp4?token=KVqnu0w0kJid58NX5BhjwYq9rUH39l8YOI9Yw4dF6BlgZO55omDMclZwIBN1Hw2tUY-oblXXT-X3mEcZU2-QUezgVzlNeAR8ZBTOuXSQ2fGGYZwkErm1udlb6qUM58Nc24ri5np94NhopqQlmY5ATArJdywvifj_CLtFtR5scKdUqq2UMjWyoQzJ46N4a1KbkSnCpeMZaZ_pm0hfxWWMgFu8Y_vTPCIA9GIQY1j8H8wIHN3z_xm4RLlKb3UWdONNk4PZgNMAmLUhoIGdWD9jHi775rcE2Y6uP_mgCwHHasrC9O6MWeHKsuyRpiR7gothS_cz28oBtU-uegPlOCDPQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سر دادن شعار مرگ بر آمریکا در مراسم وداع با جنازه علی خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67270" target="_blank">📅 11:41 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67268">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0d436c597.mp4?token=KAnXyNK33YiBmGoRJ4Zi6rRijVPeyX1OAFF6K1mZHbIWQlKmiPipWwPzdRMIr4pC0cs7ZwsMXMAdIVpjEKYt0oEqxb52RqhWTbjmLu4f92Wk0F3T23dhDS39ws8yNN6xRL4x12tYddKoVe8sLIsQ2lXXGbF4C445tgIC0BSYpMAysvhrwMtkJx5cz0lSXDSB5oDU1UIwDfbC_C1FRKH0V4p73ep_drMW2u6z5nT4NqVu33grLJfwx253ZyEEx0MMetGd1OId8-CjgKU34DsYoEQpGWRu3Npn4UznCabSsqDZZ8BoUaHAe9dygIxjeK5iRi6jNcR0QRsHFyQoElOWPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0d436c597.mp4?token=KAnXyNK33YiBmGoRJ4Zi6rRijVPeyX1OAFF6K1mZHbIWQlKmiPipWwPzdRMIr4pC0cs7ZwsMXMAdIVpjEKYt0oEqxb52RqhWTbjmLu4f92Wk0F3T23dhDS39ws8yNN6xRL4x12tYddKoVe8sLIsQ2lXXGbF4C445tgIC0BSYpMAysvhrwMtkJx5cz0lSXDSB5oDU1UIwDfbC_C1FRKH0V4p73ep_drMW2u6z5nT4NqVu33grLJfwx253ZyEEx0MMetGd1OId8-CjgKU34DsYoEQpGWRu3Npn4UznCabSsqDZZ8BoUaHAe9dygIxjeK5iRi6jNcR0QRsHFyQoElOWPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای از پرواز جنگنده‌های اسرائیلی بر فراز بیروت در مراسم تشییع جنازه حسن نصرالله دبیر کل حزب‌الله لبنان بین سالهای1992تا2024!
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67268" target="_blank">📅 11:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67267">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64adeed1d2.mp4?token=iZsU9AYqvedgLXqKZhA8Cy1LUbzfgzogDdWdzSIDQJEuDn5RSdNhHNuThUPGIOp7BOFP21ET4m9Jy9kcIjqTBtPn2MysP47rTcf-xszI1V-NJIU8qAP15_r3jds_rL8orpq2yx0FW-TD3IqKb9MdZ99gPqNgXhQ9RFBKuQ6bK6bMEoAn5R9jouFWdv3S7MskYdPfGkCoEAty6YnXXgnzgm21cYFmqcA-OMegB8xJPlKRjinQxZTyVXh3CDeVMsfzpS0oKDVYYwN4dxvJLvaka6XpQSFJERtySLjms_YmGR2tSxXvkaGiaa2RXRj1519OxZ5iKi6pCEJzrgSIk2pnfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64adeed1d2.mp4?token=iZsU9AYqvedgLXqKZhA8Cy1LUbzfgzogDdWdzSIDQJEuDn5RSdNhHNuThUPGIOp7BOFP21ET4m9Jy9kcIjqTBtPn2MysP47rTcf-xszI1V-NJIU8qAP15_r3jds_rL8orpq2yx0FW-TD3IqKb9MdZ99gPqNgXhQ9RFBKuQ6bK6bMEoAn5R9jouFWdv3S7MskYdPfGkCoEAty6YnXXgnzgm21cYFmqcA-OMegB8xJPlKRjinQxZTyVXh3CDeVMsfzpS0oKDVYYwN4dxvJLvaka6XpQSFJERtySLjms_YmGR2tSxXvkaGiaa2RXRj1519OxZ5iKi6pCEJzrgSIk2pnfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مایک والتز نماینده ایالات متحده خطاب به نماینده جمهوری اسلامی در شورای امنیت سازمان ملل :
🔴
اینجا تهران نیست که بخواهید همه را خفه کنید ، اینجا آمریکا است ، اینجا سازمان ملل است. این اسناد حملات شما به مناطق مسکونی بحرین است که دروغ نمی‌گویند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67267" target="_blank">📅 10:34 · 13 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
