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
<img src="https://cdn4.telesco.pe/file/V2VEBOYmAQ_uahw2NGUfcn2pZG1_y4Axe8PquWEChYFVJCI160dbLBZNujF4GGUGWj1UrwElqOubUygrg0O0KtMcRQk_bmCthTAuZR6pdY4ivLVJk8uX0LiIf0j0jrR9zcB909O3y35zLN548jcKsaqDJmiFuZlb_MtgkoFuU32BhTVw3s_XoRVFrb0nor81IQwKXu1msiqFJBnd1l1t9D_a1uhE_yFz72KYdPpUBZ7Gd6G98qQOkIN__0AjbxC2yQI4UqjkDAdI8W6gbf-zdskWEqUft7SUTuTmXCH0Ih0PSbJ9lFi9OAUyPzP_ro2VJfNdJUf2ydTBe7sJS77Fug.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 491K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaaa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-18 03:38:05</div>
<hr>

<div class="tg-post" id="msg-31295">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OxMsGA6cnGgMOC3YJIzHxQKvjpL1RyNBhmkjFE-qk4n2yvEbAGe4jtHMdG56Y44bfY4vpC4Un5xz2xRVejzyxmR1sPJfaHOrBoxQkE9K1Mx3Sh2vb_4RBabABvjjnW7jIsNOqA4fsGqSKjGmSJp-AyeDg733-imz1nR9sCtTT__gnHM1DHfvILQvODYijdMw_CG1jEUmhzLpywmw27h8bGNRu70TQ4OULi0oxaaOAWGPyIWKPYe5LUFV8Va3Pdm6hJjkUw7AntmqNnFSkxcwHaHE1bRA628Wj71w2yvNP-65DndLGczB9R6hNzy8WFmXwhFmAH0P5PHkV573cQoO5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌امروز
؛از تقابل شیاطین‌سرخ برابر تاتنهام تا مسابقات رئال مادرید و بارسلونا در لالیگا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/persiana_Soccer/31295" target="_blank">📅 01:24 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31294">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HXI_ObCJknLlbpzJXLSNMddYt_zXT4cC22WNvoN6La8-xdhp8sP_q1giZnJnAUx7tGcMu6XDVc-YOP_-ouKQ9ij0rO4nLcBSvURcf4GtKUm5z19T7SIADdYydyiPakrmOJXkfuQxhJphnKEpOGzjKvdMoIhvfXHxFdvgrGmvyywrNbZxSXZ3lO0LNg1r9on3FsXlyIrE_JjWRMXeYE1k9VKgIWZYdOhAC1iaDdIbTokenSG1tZP98UnSOeJlJUQIrO3MwIUFdxYBb-vFkbT-b4p3A4gQPIsHfjAwsnQubgi-DtgFfXpb8i3r_BicJfOt8L2udnxvAJuQamLPLmzmGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌دیروز؛
نزدیک‌شدن پرسپولیسی‌ها به‌صدرجدول‌لیگ و برد النصر در شب گلزنی رونالدو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/persiana_Soccer/31294" target="_blank">📅 01:24 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31293">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j7qadi7nNkuu-SErlmtZyVq6BTzhyFuWcsYa_h_LeN5GSL_LZRgTht9Jv62gH33NzIiyIXimLQ1QEBU1hUPbuFV-WfzThiOjLrciTT9QMAaCVY_ybzFf9aUUUMKIq7_D6FtbDecz6XrigbEHsikunmsYhVVbYLqeA3RULF4sBC1AR2Jd0T8nFgxxMZvttKpgp7C4NZER9OHANzYHyu6sUGaPd01UuDnQrY6Y38liX8Q-n1iAmBLaXTB3KNPi1R98HcgmwShBXBl0dzA6m5wRHenjbJFGUeBDyx6RkTiv2hIpWuekN49BvF1U2IXhy_auvX1q5Ew1Mmvygl4zpjGNag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛برنامه بازیای معوقه هفته هفتم رقابت های لیگ که روز سه شنبه و چهارشنبه برگزار میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/31293" target="_blank">📅 01:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31292">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yz0d6ZhUdde9rX6Z0vMNkqBgiYFqSR0KipwKXzzJHSC5PFH4csombh6jXYsVGAS1ZMI2oA2RzmD9ohr0feZbKtWUOmwEIc8hJve8kwTPGAcLt14yb06un3YHIXPeZRibCwA-vgh6IbKuVBkOYRE3n3h425WgIE1nm23ITIgQ9AlVcb5gqdJ1uP_7Ecq4OasMXXviXb8YXKp0dPaUBP7dnWjHksA9PMtzOwkF-4WkeM5mQiSi9yWk-DZ39iQTYiXNH0TGTOjyjHmo9HNH5pzdUGcu6HR4TL6ZskIMWqpfm76zrESHYdGorbxECVWoSIeB88DOEcInxBJ1WQlp5ACxWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌‌‌ امروز؛ نبرد شاگردان تارتار با صنعت نفت و دیدار زنبورهای وستفالن مقابل وردربرمن برای حفظ صدرنشینی در بوندسلیگا   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/persiana_Soccer/31292" target="_blank">📅 01:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31291">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/byAwcO-ag1YPbA2dPVuARQiKCGj7fat5IuogiZP_uX5cfqW5UqXVvvdWR8n6BpWR1yRwC5iCa-rKqhcAom7eNfug8zbcVkBt8451zvazqXtGApfaIqqzjCn6VJ_xBongPUZp6Z9JyrCC7g_WY-EQFhTRpEVN4jDOCPNgFASjuEDOcnlspcjMYFqizSl_YkaCvRsB4Gb8QjbTfni12ZXUYNX3COm6OT4Gu7f93ffGQxcXtaWbECjKH5M9mVGqD6D8x7Vtrh6z0813omrtPgoDrKVoVZdPYBREXCUMv7GEgOrgsOnNwdXUBBUUaPLbPNAd0IfXeAuQzjfZQeIR0xzRvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📈
10٪ شارژ اضافه بر روی واریزی‌های ارز دیجیتال برای کاربران بری بت
⭐️
🌟
📢
در سایت بری بت وارد حساب کاربری خود شوید.
💸
از روش ارز دیجیتال اقدام به شارژ نمایید.
🔋
🪩
بر روی واریزی‌های ارز دیجیتال تا
0️⃣
1️⃣
🔣
شارژ اضافه دریافت نمایید.
💰
✅
ورود به سایت:
👇
🅰
17
⭐
https://yewirkxojf.shop/fa/affiliates/?btag=914641_l303106
🌟
کانال رسمی ما در تلگرام:
👇
🔗
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/persiana_Soccer/31291" target="_blank">📅 01:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31290">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qT_WYKXeHTFQt3zLzGr78y0e_nDfYr90kZY7pNcvn8b1Ag9V4UEyDAqfbr0DVxqPwzfiAqNndUUrQ2XOP4fnqaflK7fTYhrk9H6YMmKVoK6ZyJA4fhoM1FwB1_KsVDLkl4Cir556RjhzSsaj7kigjC43VKmI5ZBdXPMLrlvkCBbNol3VqNdM0_XMitrzjzYKCthU_l83Jo73MK9MqaLWOqFA8VxHS7txPuzBfQ_G0mFXyBgofzz26DgTqHz9qBxdM4YobMITIhEgrwzjRawCIk6J1ZGPb_7RbRnIKBhFRrfXc2X4Qd8P26sEMH8ok-YEu6savLjx3FVjyPM0GcsnCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
گلزنی کریس رونالدو دربازی‌امشب النصر با الدرعیه؛ این 980 امین گل کل دوران حرفه‌ای CR7 بود. همچنین رونالدو به اولین بازیکن‌تاریخ‌تبدیل شد که مقابل 160 باشگاه مختلف موفق به گلزنی شده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/persiana_Soccer/31290" target="_blank">📅 00:36 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31289">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sDyjIWhksiCzYzKNFJxbg1wg5yWogtHm2811MhYtQ2Y4BV3atjceuCyG8erRFobsm0XOsvveaQDJicCPZmxhJ3VUgu0bOQdcXfiOljRcXwXSbKIKz_krDavu7fTb2LSgDWNiR8iKULkB7t4SmETUvhvEIFkNdNIZv3OdmlBcfZBneejRMb8B3FOSR51n6QGG_nmcPqRfzaxlA8E8VXa-NOP3EPewy_aGw0IIqgdizrhzNnOjUtLKbJxDfbBbzCrMNmPGyTewpb0aiaq4URkgEAHkz2uw-fQQNcLetkcy35qnbR5XqRqyrasqGd3IFxMk1idQpJx4l5yhDVBteVHZZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
دختر خانوم پا اسکولز اسطوره باشگاه منچستر یونایتد: جود بلینگهام بازیکن مورد علاقه منه. بنظر من او در حال حاضر بهتریت بازیکن فوتبال جهانه.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/persiana_Soccer/31289" target="_blank">📅 00:25 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31288">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KcUfRoutML9IOS5ZluyshPKFBDL9yxYYZaU_z_-VosLRnKIVKd3MuqUWTZ-OQhutAJlylAPOiswiiHm1MJBt472crUYrwr0VtQ1_21lksY0bsalBsQjQDIzo4cb0dcpN8gB-lRCUylmC-HD8NM22O-GCH0cp0K8r9EA9ItHdBabWBRrrSWxmYSdzYGGWfo5mGjM1AmuEfLyQ1S3KGh8VCIy7cis_s_XxROwDodqEVsZsJyEYS4buHOJj98SzxNv_T33xsj-Tlv1BnKeDQsC9_NzBdfeBK4O8Z_LDLUJAxoTiScWXexrSz0L6-lgyMimLOhMTWwxSQy_GAQTDuQRoAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول رده‌بندی لیگ برتر در پایان هفته هشتم؛ البته بازی‌شمس‌آذر با پیکان و بازی‌های معوقه هفته هفتم بازی مونده تا جدول رقابت‌ها تکمیل شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/persiana_Soccer/31288" target="_blank">📅 00:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31287">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‼️
سازمان‌نظام‌وظیفه‌به‌علیرضابیرانونداعلام کرده تا زمان مشخص‌شدن‌وضعیت کمیسیون پزشکی‌اش حق خروج از کشورو ندارد. از طرفیم نکونام به مدیریت باشگاه نامه زده و گفته بیرو رو دیگه نمیخوام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/persiana_Soccer/31287" target="_blank">📅 00:00 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31286">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DcV6RQONWAXjhr-adHgYyuQ7xKBPOtzXOOJZOaBOgGKPqpoRLCJHfzwqI3zbw2q3VI0l3pbg45vBSTFhIi6C_6oXIlaK4GWCcd7CWB5RUqzKHHcv-apOpAbAEECbsVqLVKNblM3qzGw2a2rI0z5ZKxZ9pikN5i875RiA6aJJLz5gmdjeDKIrGOxzzsJthTSIlVnmz_2RhzEIT_q_4ChdRUPeCBlHe6QBNdZ0gJBKSdkW-4T6dEnUJOktnxtzR_0PUeP8UQLQ2_CSHUX07-oMauZZ6iZFU-aVNmRsLd3Vq9Q4f8kK5Vs0JYsx25ryNxt9K3phORS4tRXUrGu6qA5nDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
تایید شد؛ علی رضا بیرانوند از هتل و اردوی باشگاه تراکتور تبریز اخراج شد و با صلاح دید جواد نکونام برای همیشه از این تیم کنار گذاشته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/persiana_Soccer/31286" target="_blank">📅 23:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31285">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pUIk85HOso4TwVVDlkBKfbVf_VcU-3ZodZvIBNAEGG0ndPuk9xEaCLNK8iuiu6sMRJ6UCBsrccrCy1JHv-yLkhtVooX4zi44YinUwUnAYlb62Zrk_kPdw3UqiYyjeuXiFa2T_x8G-LdekAeV2eHY8cC_nK6KzsOhpxtPyFzT-o7i_skfvOirk20eZqpaxoPp6tJuLWqX7itjclEWVNKLwFmC1EWNu6-e7nOFduAstURO7Dbc8TTpj4hFHd8I3uPnf53oeXDuSDLxNyyCfk2MDCURgK9q2jdcBOJ1K88X6MG-YtvLzVdtWEsTqI4ASyB6NIWrioC_sePr_kKsNFanOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جوانگرایی‌بسبک‌تارتار؛ حضور پویا اسمی بازیکن 16 ساله به جای ابرقویی نژاد در ترکیب پرسپولیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/31285" target="_blank">📅 23:24 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31284">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fVp-SB2-5nMhaXxVshYnKWVTjp-RrqjTJBaX0e_T2DoK41dO3sb701SFKPLE1U7L69gmBet3ovwGOK5tH7dsrQhvZ2j0ZsRog6yy4LKc0IdJlw2GZFEPEX58xF806iDJCofXtxfSl5cjeBBq8xWf__Ubq--TGA6Fhn0L0cqO6D0bU1-j4vVtFKmZakx6Q3LqT9JKZZ0qjBrCQKvEhiY8h6kf3lCzYJAoEG76PU5g7opj0visjL4IHanCqnGIALuDTHTa-js9G1ZK9xkepGfBFWHZcFVyuUwbuyEeS_Jk_ZCWtLYGXNPruuQo-abZJE93BCL-gd2-z50DM_aXV6JiZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی‌تاج رئیس فدراسیون فوتبال: هیات رئیسه مخالف دادن جام‌قهرمانی به باشگاه استقلال بود ولی این مورد مجددا در حال بررسیه. اگه بخوایم‌جام هم اهدا کنیم توی مراسم برترین‌های فصل اعلام میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/31284" target="_blank">📅 23:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31282">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iC9NPx70psNW5at3fXFr2f3zYFZydAxdXXSmoqMfA4fJ4dF2waDiNLI5TsiRDozA3EDPFyCKwzDk2Z1mA6L3kvx7Nksd8u57w1-ZR7yRpp-0T55AnUTaH2m7Z5jpH5iVrswfUpX77g5xtlKTv9PG_v2NimCQxSpByiGVx8Bf7X9tT5ANGTlSlWlLGlJNlTMeB4GehTbKYJ6-0ustdPbs7ktjpvPgr2O6-s0aPc48Y10pqcK7r-EiPBNn6iApFicd7IjyOkJKchoBAmrk2Rc7CuSJ_wfupTl4hIFHfD8-vnGmzKqR0f1aDoxqS1VXaHgXfCuZB37XyENoYMSVMU5DXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h78pdM4vmhxYIHKTIkNMI6wLGXL8BZtGZ4GQ3IeB74SsJkmTLgo7VPx1sSbiXe7WkiXfSZo_QSGj7DsDbPirTpGxCymvPQPW-c71kDJjBLSS-3OFjkVlNtJyIM8BzrKnoOrm8J22GgteFQ4BuKYjaCL3M9TuLzvC6NEcxzqkghf_CS5_lv7URp643wY112mJUxg7GPkWKmFc3Sj_DkUK89V6b90pHs8WcQUfwR76HCr6ZamR24USx8KKt0bYzDXih8woIG_yVCL-XBgcAzm62m8lPXlVVKDcyyXvBQvEOe88TcqFS7e5e0ol8ZZKEqrI9VM0obBx4SRqEP9AWjSOxw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
قدمت باشگاه‌های فوتبال ایران از ابتدا تا کنون؛ آبی پوشان پایتخت قدیمی ترین باشگاه ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/31282" target="_blank">📅 22:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31281">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sXBtMME98o-k-ACQWdCkjYy9OaznBDOokVEic2HEudi1p1-dDnG85WwswB-gU1pCD1OAlA4erSY2c3YGP6z8LMmK0_54t8uMaARgeezidEa5Y4bZ8sDVqhJe1OLAtkehgfd65Yh4UgOzqCmTM2iy6gG_xhtxOqjCLUgkvZWolcjKVrgYfPG7lX7m9dv_S2hGFXb183WBmiMrLqmQo-jhnukQ9L5dafSQY-e6Dkx02kt6OxiCUM5_lcE3FXV29fJ9gKXhqOkRCXhrw0mBYeVjr7dUDjJdY1G6OaK4ROA3B7CPvU1BptKRZ5pDNGysAf1TH09tLyR4MvOtP2T98uNnEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هشتم لیگ برتر؛ دشت 3 امتیازی و ارزشمند شاگردان مهدی تارتار درتهران مقابل برزیلی‌های ایران.
🔴
پرسپولیس
3️⃣
-
1️⃣
صنعت نفت آبادان
🟡
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/31281" target="_blank">📅 22:34 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31280">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tslluv4lP8aIuLtPYgeHmKbt7lQ_qlg0fd9eUcWxEJ1-libdbWMNBSjqln5zvGNP_nTnpg1LmlAoO5Mi5-w1R_FdliQKZdrKNVgkwI0HcsJKnrxj8kKAXwhdBIagz5dlxz8MP_FjroPGYPAtZ5Fzpef3Ye_88677RrEUWK0TooqroDnV7moi4LGyp9pNuPYFAZ8CLzAXfzYRt9r6jFvjqjhUU8hBNHPVPJcUYiQhwRqb7IT0k1uerVF7qN1ie00bTXiKB_GzPn5GmILQU4gKvvOLj7qvihmzR392Kh8a5HFAMRaZOEDeh0lKuQNJq0ARss40JHSlq34lUz0mvLz_CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛دستور واتساپی‌شجاع‌خلیل‌زاده کاپیتان تراکتور به‌بازیکنان‌تیم‌تراکتور:همتون علیرضا بیرانوند رو آنفالو کنید. او دیگر جایگاهی در تراکتور ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/31280" target="_blank">📅 22:24 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31279">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🟡
👤
#فکت؛ کریستیانو رونالدو در طول کریرش مقابل 159 باشگاه مختلف‌گلزنی کرده است. اگر فردا مقابل باشگاه‌الدرعیه گلزنی کنه اولین بازیکنی خواهد بود که مقابل 160 باشگاه مختلف گلزنی کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/31279" target="_blank">📅 22:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31278">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ فکر کنم تنها کانالی بودیم که بارها گفتیم که رئیس فدراسیون فوتبال به باشگاه استقلال وعده اهدای جام قهرمانی فصل گذشته لییگ برتر رو داده. حالا هم طبق شنیده‌های رسانه پرشیانا تا اوایل هفته اینده فدراسیون رسما در بیانیه‌ای استقلال رو قهرمان فصل قبل لیگ…</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/31278" target="_blank">📅 21:45 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31277">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mTkSXKE7foBojBjcDCgp1A7NgWz3HbefRw_ea_Y71RgqvhS4cEgEgfgZTvO7HAWfectKQUjfdZ7DKW4XKeNsXhPiMZ2EoJvoYApqXYNb-2VJet4TdzbCnbYbPCgRYvEfuCX0osOwC386AUJA4OF0LD8rEqqA3326uQepbPnvBm-4di6Xjkkl2u7AOoPXsbWlbMqB0UAkKNiVVtbOHQ0xUpiC2WNuKiqnGWZPc4bHPfEB9xImvuoTlMO2CMC9NJ7WDT2Y08LeHeX80Jg9F5d_Mblg23VGVdaKaXrGgA5r0a0v6oBwbPbGEQUzgxphOL4xo_l50P1qDuGg2DuZ-CmsHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
قدمت باشگاه‌های فوتبال ایران از ابتدا تا کنون؛ آبی پوشان پایتخت قدیمی ترین باشگاه ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/31277" target="_blank">📅 21:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31276">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i3uPK9HFC8HXNP2zAEFvfMaPmsd-1BsfdCXbNxB_GwFmBVgSyoSun47ezCEo5v-XlkimQq-wlMEGWUrK2uB8BkdCHcGet9L9cdxqzjNmIwCIE4wmLS38eSRcbuRmgwHwwNoirVAVvc6QASms2sBxHSKOsvbjhwQm0_jaXjlCOaIHFKtV6izGhmO2TOse62lLzhGls0apc38_5caP99vMzRsGarErelDJycatRqfnnowAm8UgrxJ_KSTAi4vvuAI8i6_I22e667Z8Kwpw94lQw0W2z9Oj-90XsA8RNzhawjE1Y_4qdSXXkGrEYRckVCPQRRA3qU1pmHGqU-WWcJwmmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام وزیر آموزش و پروش؛ به احتمال زیاد مدارس بزودی و در روزهای آتی تعطیل خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/31276" target="_blank">📅 20:46 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31275">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eMuK_XeMrlH2COh_yxo2GFtFcwGWmB89UyhWur6JLgL7C4HRkB7i8OMmpEFpuyhfR8aOyXAxHbcvqtjFvN_rcuP14yjgytuJYxUK_e-1VDpMXkT2_XY3nK0no_murBIPc4hOo02_ep4EL8kvk9RWBZhVzAcsE_AfYKPRuN6o1RUV9cWlPWynrP5IOG4U1P4pFFAXQkq2CRi7UZwd1pMHPU9wqOSfzF5fHNMp1xA-LzmcXrRk5QxZWBjUOZOS0UiJVeQQU8Gm4-6DCIqcADmR5v-QlCQwYvV2uYLGxzX1D52OjcsOmui-Oe1sdGGF0pNmk_wPuckgQPBh2m867uEGAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ ادعای بن جیکوبز: خطر این سناریوی فاجعه‌‌بار وجود داره که باشگاه بزرگ منچسترسیتی به‌طور کامل از دنیای فوتبال کنار گذاشته بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/31275" target="_blank">📅 20:16 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31273">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f3u9gwcumV3VbopCFtMUEMVUAdODlluvrPM6F0Pcx_VCwHf-BRX0RQqkvtQHTnefYmT_QAmzEUz0o2Ci2DI9SgliuWtOVIAQRMnCYq4UMwv8NLE0W_av4S1zcXnvnfVyeDZUUBp8VzR-FkgvOUiA1K4cdQWQPGxKQEP2LjfgOUcK1hyhPc1k--HPHuvoDCrw9p6P1637WpIGGeR8irlwESmvAxa4nfT6l8avXNxqAE4jmRho4vBZsAXNV-uxD3tYUkqg3Jf7dXV0QKdSeCQ3edIeyGT1JPNDHOgZQXNJPcO_Faxr_50USQGwSRAnXvRS9nQjL8XrBE31cIHFQjtsqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L_MO2Sm6--7qTurHn_znScqzXC1TUZZAQ0KHA09cYWHX2UqmkZxUPdyQsgqE00aGOH0zBEy1U8V85qygaLe5_mMWEDGaP6U8QsIjLYQsy5T4Q3Qfk5zNeltTKVZZw8tciLx5eHYlOOOwrR5MZORh9E2d9L0lSBlAsrzTCSVP6gro4aEuXQA8LEsaQJV2W6OmO54N64Xady9UABO5sowigCOSoI2bcJr02JsTsKUWwl2vfYqhxL6ew28j3lExCJDROmT6dvBwKu9Wp9xSLdVw-Dyj074hg5W0zwTHucseE2zVjmOxdne7xlUSdugynsW4-ZZuyy6msbprjex8j1aabg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
تفکیک‌ گل‌های کریس رونالدو و لیونل مسی در مسابقات ملی؛ رونالدو 146 گل در کل دوران حرفه ای خود با پیراهن پرتغال به ثمر رسانده و مسی 126 گل برای آرژانتین به ثبت رسانده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/31273" target="_blank">📅 20:11 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31272">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0e9e6b867.mp4?token=TkxdlQjNI5E1qDxxN54aO2H3naND0ZNeTuY3vVEgQqRGpG3LkArrPzFdXy77sy4oqjN_7wp6S3JLfoegB4IDpL8gC1Xg2AfwVSfmwlIoBxJA9OTI-oKiuIlDGQBU-QpMyEqniJRnxRVkE6tI2o7GrISAWw01i7KEITh9iMLSZJFo6VHvtuLFyzXaMNxdG9RpCSzglYpDaqAqx7WdD7UXqffekMNiSSV4TAlRRsz-HxX0UPaWypzZnxxydUCWBWMf-UM_3e8bjDMoOjTf7RCIXfvJkLtj8PMk4NqRfMY11ytBjIq4_uaPA15kFbG53vkNCZhp9bBI35JXaCInf_ILbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0e9e6b867.mp4?token=TkxdlQjNI5E1qDxxN54aO2H3naND0ZNeTuY3vVEgQqRGpG3LkArrPzFdXy77sy4oqjN_7wp6S3JLfoegB4IDpL8gC1Xg2AfwVSfmwlIoBxJA9OTI-oKiuIlDGQBU-QpMyEqniJRnxRVkE6tI2o7GrISAWw01i7KEITh9iMLSZJFo6VHvtuLFyzXaMNxdG9RpCSzglYpDaqAqx7WdD7UXqffekMNiSSV4TAlRRsz-HxX0UPaWypzZnxxydUCWBWMf-UM_3e8bjDMoOjTf7RCIXfvJkLtj8PMk4NqRfMY11ytBjIq4_uaPA15kFbG53vkNCZhp9bBI35JXaCInf_ILbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سوتی‌های عجیب و غریب دروازه‌بانان باشگاه‌ها درهفته هشتم رقابت‌ها بعد از اتمام فیفادی مهر ماه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/31272" target="_blank">📅 20:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31271">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sK8MZcpgD1Y8unX60G1xbcXjyv3L7nucl5E1AklspfUWgECejqMZEEfO4PtaFCiI1WEu7IGrTsHIB0UbhGkjVWO3BrMr0x8SL8Ax_vFRFbF3_7nyNHJzFmK1w88XzvQj9OdS1IFYHfD6zVtKeh2zZyRWzGBIl2xzP_7BYU9nCaeIvfnSl-eZ-GJnEGEwvm70vjNmZfdnXVi4JRaLJXxzji93-cFL9-flblJLu8MRgTMOs6r3vIeDKOTK0gTnC9wjvA83sVXuuET7zwu0AvAWRYWaCQMGoRE1BZqcP_-bK3UlBSyBZCci1rrHUl9sPrJb4TPy-g-OHaolyP4gjrPDGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق اخبار دریافتی رسانه پرشیانا؛ کادر پزشکی باشگاه‌استقلال به‌سهراب‌بختیاری‌زاده سرمربی آبی‌ها توصیه‌کرده دربازی‌روزدوشنبه استقلال مقابل الغرافه ازآسانی استفاده‌‌نکنه‌ تا مصدومیت امروز او از ناحیه ساق پا کامل برطرف شود. بدین‌ترتیب‌به‌احتمال زیاد آسانی در…</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/31271" target="_blank">📅 19:55 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31270">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">📊
جدول رده‌بندی لیگ برتر در پایان هفته هشتم؛ البته بازی‌شمس‌آذر با پیکان و بازی‌های معوقه هفته هفتم بازی مونده تا جدول رقابت‌ها تکمیل شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/31270" target="_blank">📅 19:55 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31269">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qX0_pTTTxyaZKGQtd59i7CHkPXG64Z-6SM3v5eT9PFBK9x66q5dIBhYo3Y-neZ59LIquL80E9A4kSwa-YkQ1PT3SjLD0pt6UFP_LIXD98xMb_FWp0PqTiiM4fAI6Oz5ChBUS5IhgwzN-WPueVg9Dv_ndblN_zcAXKBR8cBSkL-fz8W-EMpY_mE1nsFMuL23-nBkmUkqup26pvEhKoouZ31aYdD71O7DydN-4smD98eGSSLSBLeSkceLhWs6XkdrN1X3fgOaTx4SXZQmXS-ZLHgDKhbWh0jeMLEraRMIk_uDSSulJ2oEwUOW3Y3zTfL60mwR1rOu9COiyaZLlEUHKSA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/31269" target="_blank">📅 19:55 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31268">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d0BAkWQYPKMYrU3HgzDlZBo0d5jH0b6auX4j-tyDbR6-Tz_GsxAgGi9QmYOlE3M59mhVLSFB6q00FWg3du1YxlzhXS9OT1pYRHYLDyZOqh5mXCv83NKD-SSkJz8CyGmxPMIx_xtW792GRgCu4cj6iCNYqxB9ttZ5jzwRYxV-h936bXCyAFOqwlf6j0CQGQjc_zP75EynY7Xjs4Y-0hrR82CKM0p_Q9tqcAS4MITUnai0Ql2YpVbEv7j7HyoPnulx6IhF33Yn-PbbLi8AMj1g48z_ZU8ebqIou4eA7_jet7C155QmgAWHAw97mzZ7qIPqt3IT5CM1MNJbig9ZfSTpkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فوری؛ وزیر آموزش و پرورش رسما از تعطیلی احتمالی مدارس به دلیل تهدیدات جنگی خبر داد.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/31268" target="_blank">📅 19:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31266">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v-R9WPBrPaTlcUuZSUcxmT1QFlk-8lzmUMzMj_R_ej8YiaY41ByosvrWreaOeLTl86FBAVTyfZQSB1k8m9tEvP5obbS1-RqdHc4GyxFAbHUSWHlXBySkK5xRhzpU5V6zfVj0Zq3CFXbTUBbHbTIV74fktj4HEKAaB9PqgrFFZjL8RTEOgo9wYaNNo8h0otSl7Y6nj3yWfqdzrhU0FsGu_tFzoPmKWBfDmfcmrk6PkT2aC7FtJ_nlSqEkvJiQeGMnIA-bY4llaDUX_gEXOV8ys2WAirOZL9bvNWvUJBz5UPjv-X37tWG2NxLKtaBN8GIWT-ZKn24iiQMAE2RIH1z19A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MesuaPHL0ixhdOKfQG0-h8tKXljVdu53-KNUvKWwpEVZCtV6MFZrwAnSs6laINpEmVMI2tDl0a_SxYw5MyVRpyQfpavtC3tNM9iWzeGTaz0zusytjFaDg0NX-suvL4okVg2M2m1_JSvcVB5AkXvpMUXw4PQP-hoHmvo6ijbY32xCl7AU7HsvcCEYXXSnT5KLTFkX_0DfwEZiZwV5cuQIwpQCJuhCApB3l22R04X-hjBxESF2yrKvQvy5HF5P5pJ88gyB_W08762Yts43KUVJWPEsLln52O9epUTXEeGTMeeIU4mO10AX5APU21_ewdXs_dxu-vB6rPlGFKlE2Ma1Lw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
بانوان هوادار پرسپولیس درقلعه‌حسن خان.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/31266" target="_blank">📅 19:19 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31265">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qW5OoHhxBiLVXL3Gz0PKuQBM7fwO7Yqm5Lnd5ThUhf2w43Z7llQHkYfT_GN1vdZeLW7MzCWEO3CzP5Eoo-4uXp-pOgMhFotqGLsn9PWYScFPz1ZyJz9_gHLqLJUEgbYMiXqTNxy8oIXA_5AxfOdTEIEQyXhBcyJ897l6-MOZFWNDD5A1y241eKZmly5AFoj9KkAYtnxg0E5qPdowOqgVpLPcAwOeUROvnv1BPnZRX7ibdYOlEgXDv5feGO0lGof2oZtmL7T0iSpaZG7j8meHouewgOQpKsUnXxFsgwm_NUjMI0bb7T5LQ_a1DKcI7-D9zeSxa7-148qNqkM5VFyqqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هشتم لیگ برتر؛ دشت 3 امتیازی و ارزشمند شاگردان مهدی تارتار درتهران مقابل برزیلی‌های ایران.
🔴
پرسپولیس
3️⃣
-
1️⃣
صنعت نفت آبادان
🟡
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/31265" target="_blank">📅 19:08 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31264">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c4Ba3939bWsjBCNBMFcRRxdP8AoOC3AIR1wcV129BIYZGcgIwV26cnXToD09YzZ-bSpdbrVygRFIgcXCG2nDsyd_cYkoslzZScBtCS5A68pFcpTQPid6tOwvRGU3tWBpxYqsLImrZBlwvKCp-HdTeRNjsf7G4i8laHk5lRq1nAUHWVqdHrE827CHz23p852CtNrbJVdkH1Cdm4WX2pOMcbnMlUmPoLILd0q2zfMzndaLToUbxtYepWMc_gojwtljsilVl-WhMHPS2wPqYRJgTzRdd9zZYpBZc2bp1ZB3xWnDb9AuFPifmX7KaBCEjS1zXUCWXjLqsuDM3JNWCM6uuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هشتم لیگ برتر؛ دشت 3 امتیازی و ارزشمند شاگردان مهدی تارتار درتهران مقابل برزیلی‌های ایران.
🔴
پرسپولیس
3️⃣
-
1️⃣
صنعت نفت آبادان
🟡
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/31264" target="_blank">📅 19:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31263">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WiEeCwg0hrhow9zWkUMcO36zX26hoFN4OPUHYpT3QVICbNK2EVPfLa14ITw07-QxN4lmBWocVl5ZGG9YPJT_koGV4tI3assMaFFfl279p7KG4mtF2W9VBe1XHXveGzn1Wtd4MITMgl0BeS0BVMgGGNVUkXRNxA8hBtI0Z-gnxSdlcVeCUNGVoc0AK7iRUOS2730qMNIuDlW-Y6vMbfbMrIHtMODokEZ8-OiOT63QZTb9qQiQlzx2byHQ0gnrOjpskPCpG-33_kqBdLMh2aa9ZTPJ6P7mQgO0PmbxNUN-ySPEE8fTkGN7N5aPLX3zRpegeO9dV0KM_sW7XE-CH1R8Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
سرخ‌ها روی‌کرنربازم گل خوردند! گل اول صنعت نفت آبادان به پرسپولیس توسط باصری در دقیقه 66
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/31263" target="_blank">📅 18:59 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31262">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/866119f609.mp4?token=mLyVJfYMHEavEIcO4F55G4kM8D5xl1IwMOS-VFIsM-uNkE1AOy4OymPng0UQ-3NkDJIDjLIsla4oAAII4utVH_11sKeDG2rs_5GukmyjWbZgocVUnaN6RAzXwqh6m-6U3LSkL0ld-qP45q8iD03Bvp2-31-LUl2-KKc1nLLHHhfGKgkDDouK3zlGw4y360goUxB4Kjx4OcQpjNqalXFa--S2fvI5cg5Y05-haYo3wEtKj4Ol_Z_EnxnY2uHhBF8_S7nuxMhSj2HfMEHZtRrX880ykrNk8-uUx_vDfbKnwAJSiRrPknzx9PdPvtrHrhM-b9GLJpuJJnUm_xMg8W_9_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/866119f609.mp4?token=mLyVJfYMHEavEIcO4F55G4kM8D5xl1IwMOS-VFIsM-uNkE1AOy4OymPng0UQ-3NkDJIDjLIsla4oAAII4utVH_11sKeDG2rs_5GukmyjWbZgocVUnaN6RAzXwqh6m-6U3LSkL0ld-qP45q8iD03Bvp2-31-LUl2-KKc1nLLHHhfGKgkDDouK3zlGw4y360goUxB4Kjx4OcQpjNqalXFa--S2fvI5cg5Y05-haYo3wEtKj4Ol_Z_EnxnY2uHhBF8_S7nuxMhSj2HfMEHZtRrX880ykrNk8-uUx_vDfbKnwAJSiRrPknzx9PdPvtrHrhM-b9GLJpuJJnUm_xMg8W_9_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
اولین گل‌ستاره‌ ازبک سرخ‌ها درفصل جدید؛ گل سوم پرسپولیس به نفت توسط اورونوف دقیقه 85
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/31262" target="_blank">📅 18:59 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31261">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aaaacac90.mp4?token=YuB5JUQz6x-qG82yPZHDTLSrAAr-fyY_h0EtDvHcRFlXlgvBR0BKqMankLtCRwfX6OiCtv3DCnyCVajqUnWkDjFA-9WzEug1H1C08ifggcOpHK1z7XFp9plW99SOLrRpcM_H0St7DVBVXBvpq_VHkUbjyMbxaFc4LimeE3Vp1ugEXh2nY6Lih3sMdb-ngkp5FF0p8jGmAjeUPoQe89-YOCMvc0nUiWWxViilIHEZjG0iAmSMfhGLScPNx3ZDFLi8l9dPw6PU-y3_Dac2gJGa0sc2qsGaBWATqHDnDM3dFm2B5AG-OnZZMJbkey4t_BRzMecTbZMfAQ5Ke-muA0Hb4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aaaacac90.mp4?token=YuB5JUQz6x-qG82yPZHDTLSrAAr-fyY_h0EtDvHcRFlXlgvBR0BKqMankLtCRwfX6OiCtv3DCnyCVajqUnWkDjFA-9WzEug1H1C08ifggcOpHK1z7XFp9plW99SOLrRpcM_H0St7DVBVXBvpq_VHkUbjyMbxaFc4LimeE3Vp1ugEXh2nY6Lih3sMdb-ngkp5FF0p8jGmAjeUPoQe89-YOCMvc0nUiWWxViilIHEZjG0iAmSMfhGLScPNx3ZDFLi8l9dPw6PU-y3_Dac2gJGa0sc2qsGaBWATqHDnDM3dFm2B5AG-OnZZMJbkey4t_BRzMecTbZMfAQ5Ke-muA0Hb4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
سرخ‌ها روی‌کرنربازم گل خوردند! گل اول صنعت نفت آبادان به پرسپولیس توسط باصری در دقیقه 66
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/31261" target="_blank">📅 18:52 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31260">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acd9e6967b.mp4?token=tOafOF6dbB5tK8txlbG3f5nH5HfSb6cVtM4oGKG5p67A3W5-Rk37-busiVMJBRxBkghm8G4f3tdoHPGzCLwust6DX3ikyRVIEUpCj9WkytxXe5VNywDCQvstEzcS785BUM5yaDb-745ZEteChxZlGPmXAEDPghODEuoxuI3peHcOCsXs4k6uipKgSXJKxuduPmWPOVAbDqd6VZtXxHhk0S-Xd9v0EkMCcR0TgWsSao8Owl6ofXPhe3OAqAfD3GWE93qBCdh1QPrEBBXV8tZiZPm-kdd3GBX0yPbyCKI5UNGNCO_pmzjc3Sx7oNbyVWLz04sVqFLpgW08sGPKuw0gCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acd9e6967b.mp4?token=tOafOF6dbB5tK8txlbG3f5nH5HfSb6cVtM4oGKG5p67A3W5-Rk37-busiVMJBRxBkghm8G4f3tdoHPGzCLwust6DX3ikyRVIEUpCj9WkytxXe5VNywDCQvstEzcS785BUM5yaDb-745ZEteChxZlGPmXAEDPghODEuoxuI3peHcOCsXs4k6uipKgSXJKxuduPmWPOVAbDqd6VZtXxHhk0S-Xd9v0EkMCcR0TgWsSao8Owl6ofXPhe3OAqAfD3GWE93qBCdh1QPrEBBXV8tZiZPm-kdd3GBX0yPbyCKI5UNGNCO_pmzjc3Sx7oNbyVWLz04sVqFLpgW08sGPKuw0gCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
تثبیت‌پیروزی‌خانگی سرخ‌ها؛ گل دوم پرسپولیس به صنعت نفت توسط علی علیپور در دقیقه 50
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/31260" target="_blank">📅 18:34 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31259">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db73f92ec5.mp4?token=m48dDSEpiFWaJ0xgzOrEXZ5QKiFaOhRs2CxLwOOQ1NPEeRzxeY9Amx8e4HkaZz_pxtMfABI82QwelS5wYVIFSM8r1_aiV1hdwg5zzNAuOiilsFTeiYA4T0Jb3h4nLqgPM2OgIxBTF4dqftyi5DDqJmAJnf_B5chPSoXiuIeub898sPlHqPH9YMZVbiDM-nh3RrUISJEnwbbdomuIvHFkGhW9xlU34ZJkVS5BjFzF35syOpeHtb6fBamqHHP1yFDt3vibn7qtjd2mWj-CrysX8Y2u9RP3gdsLIt1gyy27nADHACffbhVYTUK2ZsCVdU5Y3K0gSlb663EL5p91Uj6LGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db73f92ec5.mp4?token=m48dDSEpiFWaJ0xgzOrEXZ5QKiFaOhRs2CxLwOOQ1NPEeRzxeY9Amx8e4HkaZz_pxtMfABI82QwelS5wYVIFSM8r1_aiV1hdwg5zzNAuOiilsFTeiYA4T0Jb3h4nLqgPM2OgIxBTF4dqftyi5DDqJmAJnf_B5chPSoXiuIeub898sPlHqPH9YMZVbiDM-nh3RrUISJEnwbbdomuIvHFkGhW9xlU34ZJkVS5BjFzF35syOpeHtb6fBamqHHP1yFDt3vibn7qtjd2mWj-CrysX8Y2u9RP3gdsLIt1gyy27nADHACffbhVYTUK2ZsCVdU5Y3K0gSlb663EL5p91Uj6LGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
شروع‌طوفانی‌شاگردان‌تارتار؛گل اول پرسپولیس به صنعت نفت آبادان توسط تیوی بیفوما در دقیقه 5
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/31259" target="_blank">📅 18:20 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31258">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h9dDE1B2rVO1bZa6IrS3kievp_5oFltY98jBhZyGR2fqgyzpUkRMUNeszQt2uvDXGcG6UckLg0sNfO1RbM3Tvpfzh_xbln3ecSAa5Z0F7ODYFDA53Tke9RN4ZdIc-EBhZkNzholOaphYLFn_ZBa_ESXuW-xE2sOtfcTU0BShc5P4b1KdANQyLMiN2zJTe_DIucsY2PYFG5UKrofxfxAJ9JYE8OCp--ws4x-9I6fCFAKyzCwu6OXs53sF7XJeay4iADtPjYxv98hhofOiDLT3Xjf27VcnSMimQUhOVN_2FcOXRakLb6rzRUErOqGujUOkTeVOlu4h5FS89R_bUiZ21Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎮
تصاویر جدیدی از بازی GTA VI؛ این تصاویر در بخش موسیقی وب‌سایت بازی قرار گرفته‌اند و نگاه تازه‌ای به فضای جهان GTA VI ارائه می‌دهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/31258" target="_blank">📅 17:48 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31257">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0462dcd97.mp4?token=Qgad1eh7zqkc1fBXVcLVK0957wPt0YnA2UeKWXHT2pJrnS8eq1Yr21YUKcfUItlcToOTY4nHOjHhmzWzerySVh47wtPkYv8k1R06XWoKX5aYIJ4jUM6sKRtjlu1UIurqe-hqEUsVAcaUdugams-NVZ1g-XDKtdtrQ_lEvo_vR1uW9nG6sKwF7-zQMUmHh-sY9UF8YREZtK2gnPPUBtTa4604rAFTR4JDG28URyXL2cVNEa9qIwzzr4_KllsBEvmNNvYrEvWetgX5ssN2e3cDwouXc79hB_Ho7Dzd_RiWcqBLrLH0RtSFkVNyI5d4rET_Fp7nN2jhFXo5eBWOhpB7Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0462dcd97.mp4?token=Qgad1eh7zqkc1fBXVcLVK0957wPt0YnA2UeKWXHT2pJrnS8eq1Yr21YUKcfUItlcToOTY4nHOjHhmzWzerySVh47wtPkYv8k1R06XWoKX5aYIJ4jUM6sKRtjlu1UIurqe-hqEUsVAcaUdugams-NVZ1g-XDKtdtrQ_lEvo_vR1uW9nG6sKwF7-zQMUmHh-sY9UF8YREZtK2gnPPUBtTa4604rAFTR4JDG28URyXL2cVNEa9qIwzzr4_KllsBEvmNNvYrEvWetgX5ssN2e3cDwouXc79hB_Ho7Dzd_RiWcqBLrLH0RtSFkVNyI5d4rET_Fp7nN2jhFXo5eBWOhpB7Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
از وقتی که مسعود محبی مدافع تیم خیبر توسط رسانه‌ها بولدشد و باشگاه استقلال نیز به دنبال جذب او افتاد هر هفتههه داره سوتی میده لامصب. این چه اشتباهی بود که تو بازی امروز کردی پسر خوب!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/31257" target="_blank">📅 17:19 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31256">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/499a1fc96c.mp4?token=p_E8xjUzQ54gOkY8phu7OKaICEA2vj4fw-LeHUBf8slTLWOOrY6Dg3UU42FVyl7khrJ9Y6_8PRbNR7cwc8QyXxt7sdGQ3PO7Zy_27lP7PshIAPx_YpdqLCFqcD6uM6pRZSwkoUw18QRviewynP1mVvDiLhB4wvEaRYt3BnEsW-5DBoZDYlWMuEJP4wfssoWSznezyMoMJER2u0eBcPhQ6xPw2dVdk17Cg2Gf9uGiK35UhwTGzgLauu_eEHuz4Gp5-qTuZKeOz4I1qfI1-UassoW_W4r-cVSBCeQZYrRga0f-CQtcQFH9mkxm7QNs43MdNFXecgGrsQQo-HkTNVg8Cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/499a1fc96c.mp4?token=p_E8xjUzQ54gOkY8phu7OKaICEA2vj4fw-LeHUBf8slTLWOOrY6Dg3UU42FVyl7khrJ9Y6_8PRbNR7cwc8QyXxt7sdGQ3PO7Zy_27lP7PshIAPx_YpdqLCFqcD6uM6pRZSwkoUw18QRviewynP1mVvDiLhB4wvEaRYt3BnEsW-5DBoZDYlWMuEJP4wfssoWSznezyMoMJER2u0eBcPhQ6xPw2dVdk17Cg2Gf9uGiK35UhwTGzgLauu_eEHuz4Gp5-qTuZKeOz4I1qfI1-UassoW_W4r-cVSBCeQZYrRga0f-CQtcQFH9mkxm7QNs43MdNFXecgGrsQQo-HkTNVg8Cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
شماتیک‌ترکیب پرسپولیس برای دیدار امروز مقابل صنعت‌نفت آبادان؛ علی علیپور، کنعانی زادگان و ایری بدلیل‌مصدومیت این بازی رو از دست دادند.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/31256" target="_blank">📅 17:10 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31255">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7613725c1a.mp4?token=mqo9Etn2SXc4WCbm1KKU7zPvg-II0kiXY0l27D8E8vzAfrCTKlue6qBS4Hapcye9o34s2OSMmbNfE-PWULOBL9iHhdnrppuF1WIY9rEUx3XA0ZlE02RlZyAxbcITzFh4_8xrnkXIMaYkNEGGWyNm8stH7qxYLDpC54xHTvvae4Yq9-lUdTHzEf4GvXmjKdKdcS7zigi8oIJXFmSUyAFBdbn3cNlUwA7ajGEDtwKJsXz3Uu-BCFEODlPB5yYDd8wH6CL5LDjXie57lq7oeK1qC1pPgFDNbtkATo49SsDcSFcVxBBrvrEvVNRNoH7egYnPSKBrowXVpR8xDDId2Djamg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7613725c1a.mp4?token=mqo9Etn2SXc4WCbm1KKU7zPvg-II0kiXY0l27D8E8vzAfrCTKlue6qBS4Hapcye9o34s2OSMmbNfE-PWULOBL9iHhdnrppuF1WIY9rEUx3XA0ZlE02RlZyAxbcITzFh4_8xrnkXIMaYkNEGGWyNm8stH7qxYLDpC54xHTvvae4Yq9-lUdTHzEf4GvXmjKdKdcS7zigi8oIJXFmSUyAFBdbn3cNlUwA7ajGEDtwKJsXz3Uu-BCFEODlPB5yYDd8wH6CL5LDjXie57lq7oeK1qC1pPgFDNbtkATo49SsDcSFcVxBBrvrEvVNRNoH7egYnPSKBrowXVpR8xDDId2Djamg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بخش رسانه‌ای باشگاه خیبر خرم آباد در اقدامی جالب شماتیک ترکیب این تیم مقابل چادر ملو رو به این شکل "یه نوع شیرینی محلی" منتشر کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/31255" target="_blank">📅 17:00 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31254">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZqESWV_Hi0wuiBUHgnzRhoyRvEE-c1AtjVP1uohrFFWZomT1mPhxADCQ0hOPqahkGa_GCmf54vNzuG9yeYysoUYdd27rW-imvPtsl76duE8Y6wW6utIXLmgGediRYTNL8yHd3bj23Tw6eUPboVI9ckOHRkSmnHx94FIm7k2wrZx76MLvc40ENQwCN4ct2GuNFfCYy49vdnJdpNDL1FbDlrJc3xqzmtr1G7fRZk3kX6OksIs7sN7bgji19XzCm6QHuycgkcmxYlGo7C0rdxcS1CR12c32_lHMbgfF2fnFhMrbQ0EomLRHgOwWAqHBxxdVnIwhdTidN8Bu6v_kvGltg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیست‌کامل بازیکنان دو تیم پرسپولیس و صنعت نفت درهفته‌هشتم لیگ برتر؛ مارکو باکیچ و دنیل گرا از لیست سرخپوشان برای این بازی خط خوردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/31254" target="_blank">📅 16:51 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31253">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">‼️
#تکمیلی؛دستور واتساپی‌شجاع‌خلیل‌زاده کاپیتان تراکتور به‌بازیکنان‌تیم‌تراکتور:همتون علیرضا بیرانوند رو آنفالو کنید. او دیگر جایگاهی در تراکتور ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/31253" target="_blank">📅 16:47 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31252">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bwiMchr5iqOGJC6rXabIGekTYS1Y-PmOPdwd4CT1qAS0jS7Ap4_pJDpgaiBJ5_UwzegAmFI6TM9euxVVJStvHDU-CVo4AwurqfJJI1StYis7XqmqNT8Zv5qNoP76ovk9kfJRd_GHSQGALZxdjTmHEi0GObWMDhua4rAT07OC0OCE6P3_CUvQsA26rN1HT0R_Lf8g5fNaC8SYUo_1XdHNEeY7jMetChPIjBDUtvbDBJPYdTIg9TVVWAKZ0svLk_vuH2kv9cgt1fE_9XIha7pavA6dImcPcToE10EtW-4l7HRR-Wib8doZK7fEQb0KBYLAW0mSi05M8u9VU6jMvCy-vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هشتم‌لیگ‌برتر؛ ترکیب تیم پرسپولیس برای دیدار امروز مقابل صنعت‌نفت آبادان؛ ساعت 17:00
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/31252" target="_blank">📅 16:30 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31251">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cCD2z-YRTN07x0EtV70aZZSLim9nu4HpzuqlN-ocKxgpgKUcspIC6WKFUujMTvJW52l1VECDCMpRR_ph8QhcmFHdq4jFytqXjRWbgx_zwiXeCJ3B4ehQQ759DPJgS49-JSWQOK1bBJxBZgU8HbJhjmoriv4_9Em9OcFDY74pY5aQ6XOHLA_Sk8O2RDjQtyXU6zykVXPxm_q5QETv2BFqRSf-pdM6Gufzk4T2joLT9nkSK9AHnFDU3V9h561b0NdZLi7oL-POINn6_6zdOtpsA1h8pFtNfdsMQyFARh1UiJp623k0uEAmoJTK4M-4PRLfdAsKMxxBD4MwSB_k8Zw6vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ همانطور که‌چندهفته پیش اعلام کردیم که جدایی دنیل‌گرا و باکیچ ازپرسپولیس در نیم فصل قطعی شده؛ مهدی تارتار نام این دو بازیکن خارجی رو از لیست سرخ‌ها برای دیدارفردا باصنعت‌نفت خط زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/31251" target="_blank">📅 16:24 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31250">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WdmUNmi3SOVvyJCQAFrjWnkL3bBzlndMBP2aasCbVouxCIAdvUNUhSqaPejx0ipFHrYNsZqs-8kT0QieitmmE_8vJnhIyvJP2cI8a-cY665qLz0TmXONNAxxY70_EvO_UxSmFL7xXC3IDqlM4pFFOGE2I-O-FQ_04tDi8Qca18BtzKnspG-RzG8xhciLww4K5Mziz_e4DwIRQT7p_c_Eaa5celye-d4-ITb7lF7wsVM0Z7Qkk3fsI1AJj4Q9Vo2zB8erpKI0THiXZ03WhJbxmMOdlCxT7dOuK_OsVPh_G1kkywg1Mz_8vB2JkAKP6bRDVTxl5QeOTkbZiY6q2Y8XDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
به احتمال زیاد پرسپولیس امروز عصر با این ارنج به مصاف صنعت نفت آبادان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/31250" target="_blank">📅 16:05 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31248">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kz2XJADiZamrBXZXygFRFZW3Sneje89fMwsXzHRWO6CSrp_yo18HuKGoGfP7lnuBlv_p1twrTHFIihpuAhUkzAqf-ZdkYZKXPFljf6LTrppHpdnma6XvNFpdY3AabT2hmOSnSciQP8-mwHOklCSrR74ceu_cLHSVKz60lc3zuCX48gqbeUH8dZi8e_1LU8yK3OZdFQcGFv06kUp-t4MZe26mO9HZ1bQrRpSi7sfT3385KGHT4jmYf22K3STuwD59Y5QI66JIFKo-KQ7NHvwphyN2IWLNFHuQggwsU1BPUPLgVG9KbrF_HhWxDrwWSjv3Js6dd7HpfvcwnGZ88bn9kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DxtBX9qdVHgUHdM5Gs2CTX8j1S3q1M2DvhVGbFTjP91OFP8ICTNhw7-bdZch70ayu4IXcSWgIOKXNaETNjR2jB3Dq3MuokW1-jNptESDFH8Et7Wvfz2CfcNxGdve_19-oBue4I9u5n9DTk5kTWGbdgEcOrqthoEBw-TFk2BjtnmfkpXxS5UbVLqsrYbEOUxts1wPSS6ArJ75wM8J5EtGqQKNPXijFYcT3LFhwGOrmQN3ExpVOr9kyJT0rACdPrEu7Vi0FGqD83OdfHxxU-DetZqErWq8UWj40NNI5cCBPfCpN_jI_hOeKGB4ntihGKrot1VCSpi9gcj7SvnPwoxTJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
تشویق‌ده‌ثانیه‌ای‌لیونل‌مسی شماره 10 آرژانتین و ایستادن به افتخار او در برنامه ورزش و مردم بخاطر خداحافظی او از تیم ملی فوتبال آرژانتین در اوج.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/31248" target="_blank">📅 16:05 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31247">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">خبر داری فقط همین امروز می‌تونی از اسنپ، طلا و نقره رو بدون کارمزد بخری؟!
🤩
کافیه وارد سوپراپلیکیشن اسنپ بشی و از بخش سرمایه‌گذاری، اسنپ‌سرمایه رو انتخاب کنی. حالا می‌تونی به‌صورت آنلاین طلا و نقره بخری و دارایی‌ ت رو مدیریت کنی.
پشتوانه خریدت هم اعتبار اسنپه و هر وقت که بخوای، می‌تونی به‌سادگی طلا و نقره‌ت رو بفروشی.
همین حالا با اسنپ‌سرمایه، بدون کارمزد خرید کن!
خرید از اسنپ‌سرمایه
خرید از اسنپ‌سرمایه
خرید از اسنپ‌سرمایه</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/31247" target="_blank">📅 16:05 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31246">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ua81F3pAUaTxx0fUspuPbpMTgJqg9jaVZhggh8HW5xVOfM0rZBLIwa0SPNxMCFkwTvkIb_ntBdBMekm7-IpEs-oTjbmvlBiZbMv0UGgfNe-6qptl7uIDGCFz5pns3OF-OlWgSoDiS96oLnBDzNr-P0dg4zUGUvtKPqWqD52m_bzqfP0hXO7e8Papc290QDmridy7KigsfCRtxMWF-w8S3tm35SFmVEnlXKG_z8xC1Vmj1eKUkEZXpTKgJcZNcyz4EpuGmC7F0H7M5EJVwfWJO2WrPB8x7KkAAzdIYD6LIkiQ4plI7vSQ5xCUGwL53yzc3vzt3fnkFF2fY9uh60B1Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد نیمار جونیور، گرت بیل، محمد صلاح و ادن هازارد درکل دوران حرفه‌ایشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/31246" target="_blank">📅 15:31 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31244">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2089087958.mp4?token=Sbok8w-UPc6tBibjpEcP16mLETFG93rBW0GlO-OpmM_U7cgRIEtFUVzx4Gz6-m8eDmezsAkoi3b_Uj2Y8OFyx_X2rBJ4Qx-8zXwCkU9w0fJvZ1LgY3B-qHEqTMmR8tN4a3RH5ryD2UT-Sp1gU6HQHhvliFyD9onDOtJQddKuI1J2Tr7qDcPfBwfc-bUGhaQOLw0iP8I1LdsqmJ6giJBzlDsyRM2fYvLwkM1ix4K1O6aLwCfaxTkR5zHD1q4ToaZHgo-OWqgH8jX8c2tsePtp_2NDYz_wKW5a3UYZ2cStRs94GM5M8_yQgpJ--Yxgx2ZxCPs80gNoXbY6SpJ1BVSOsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2089087958.mp4?token=Sbok8w-UPc6tBibjpEcP16mLETFG93rBW0GlO-OpmM_U7cgRIEtFUVzx4Gz6-m8eDmezsAkoi3b_Uj2Y8OFyx_X2rBJ4Qx-8zXwCkU9w0fJvZ1LgY3B-qHEqTMmR8tN4a3RH5ryD2UT-Sp1gU6HQHhvliFyD9onDOtJQddKuI1J2Tr7qDcPfBwfc-bUGhaQOLw0iP8I1LdsqmJ6giJBzlDsyRM2fYvLwkM1ix4K1O6aLwCfaxTkR5zHD1q4ToaZHgo-OWqgH8jX8c2tsePtp_2NDYz_wKW5a3UYZ2cStRs94GM5M8_yQgpJ--Yxgx2ZxCPs80gNoXbY6SpJ1BVSOsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
شعرخوندن‌بازیکنان تیم ارژانتین تو اتوبوس برای مسی : "لئو تو مثل اونشب تو قطر جاودانه ای. مارو ترک نکن همه میخوان تو بمونی و..."
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/31244" target="_blank">📅 15:07 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31243">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cmL3ZTriGrG2BxUws5mavVEhqJvEIilybxi9jkXpHmXbywZAgiEHTQlMxlJiadaOxvfOxIY46RVXtt5jeykR2SiSN3C6JSxZyx0F4Dh038mp9PaN0tbQVMvjYO2JJIhQ5swtGO_9_4fJxa2s6xhDSlyaTgG1znMUgAsSlelGLtEcTrHkNpgiS6Y4XTlEbFmZUMj0BKnnHUeTaMTcLSx5yNQFUVkPpeyPuPPP_f_PbvE7vX08R6DFmLPLG3uotdraL-Q_3fZO7T5YTyeUBLemq9w_z8URScEh_T9W24gP10PdTEfbyX0bUh1xvopSQ498JtRNDw4ZI_Roi1rxIrjJVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🇪🇸
🇧🇷
#تکمیلی؛ با تاییدیه کادرپزشکی باشگاه بارسلونا؛ مصدومیت جزئی رافینیا دیاز برطرف شده و او مشکلی برای همراهی آبی اناری‌ها در بازی مقابل ختافه در هفته هشتم رقابتای لالیگا نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/31243" target="_blank">📅 14:56 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31242">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33992a38c0.mp4?token=OmZ2O1Ir3oJCXswCKUUQ_7zhgzFSLjlVH--0xs__cfj6yWrg9qPE9CChab1mcwznuyaQ29CMCiK2Qq0GKhD1BxkptagC8YzyVxNmzKJBHZlTqymVt9-p-EIbp0AJOyQYMJtRLqRssLgu36f_IGT1gdd_Jcdxqi37fdSLNQEcKH2LvX6JltFcqLVAP3-LYoDSx3mlb7z2oJSx6wIUH_vcEyCpx03X-Axia4wdSmhKUfGCx37VxeR5UORpKdT-bTDX7qQZJLs2IBeGYx1xF2H_PONkS7z6vfy73GJUZX_o3TEFkXKbSrDy-H_QgEaC1_94rdVNJhNVfGQtEnQ0kBc06A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33992a38c0.mp4?token=OmZ2O1Ir3oJCXswCKUUQ_7zhgzFSLjlVH--0xs__cfj6yWrg9qPE9CChab1mcwznuyaQ29CMCiK2Qq0GKhD1BxkptagC8YzyVxNmzKJBHZlTqymVt9-p-EIbp0AJOyQYMJtRLqRssLgu36f_IGT1gdd_Jcdxqi37fdSLNQEcKH2LvX6JltFcqLVAP3-LYoDSx3mlb7z2oJSx6wIUH_vcEyCpx03X-Axia4wdSmhKUfGCx37VxeR5UORpKdT-bTDX7qQZJLs2IBeGYx1xF2H_PONkS7z6vfy73GJUZX_o3TEFkXKbSrDy-H_QgEaC1_94rdVNJhNVfGQtEnQ0kBc06A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بهترین‌نمایشی‌که‌یه‌مهاجم مقابل ایران از خودش نشون داد. استپ سینه‌ هاش آدم رو یاد پرایم زلاتان مینداخت. همون استپ سینه‌اش رفت تو گل ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/31242" target="_blank">📅 14:51 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31240">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KvpKGGSygx-9gnWozYN5ofvJ9Zzyp6ZAyGnjUl4skOJKfgyLQpNpTH98dLcNZ6QmITy1pT-RdT9AemhFVOI-Nav3iHJkPvZG04xMliTspya1cmr-qgJhMN_s9sDPs6ApNK_ZSJypum_gbtT_t-fC-nzMldNZfoStrf4a7WyjN0psbRsxkXVcwI-VmX4dK10wMydbyNuzjZrU7MzIrMGx75Mh3MBqrKVIB6ZSE4mE2NvDR5tz6e0hoSAEDrt2T0vBAJt9jQMkInqZ3vBmlh2lbRGeOy8-CRZsGG_NbJZ1iEcQZDidl2bnAtf1mrAmill64DBbCkKkyk88kVfOCDDC5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q6dwuByrKuakR7zTMFGVPTX37qYL2V2BXx18UM17VyC-vcJpLkWyhdMz4xBvHP2m3gpN4J731guM4rWs_aAkgaeeSU7X8qqV48fynsPI8Jd5qfYVfIH_PArCXh6fREW4O0eT8A2kxDpoa5i1--zy-W-cWPLlDTJIQ0Nx2pYVHbey88z7UVdsLaW54hkolto6S8hgkAnvlsN2PyC32Q1Y-89sjsEQh542HdoLmxugvwd_It7xs3s5snkKfz4e0QvrOE8I8wmi0t7mVgTluX3KPjdTm7u2L0wMGVLoqC70vC0HAlik954lN_FafM14I731yFxbDANyqL6sn71slXGm4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
حضور بانوان هوادار تراکتور در ورزشگاه یادگار در جریان مسابقه روز گذشته پرشورها با استقلال.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/31240" target="_blank">📅 14:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31239">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jy6KwTXSvHj2t36buV04p1ZugdSZmrEdnnD3fVypUiaFtFbVAttfJB--FbI66M-MCS6CBfujIqI9-z1PUwqUoJmMQ_kOG4Aq59SRnxmcT54_bKx9vIVwsGlTTHzpY2fbzxSIGnJF28vRB0V6D0gG47lxwRchuk9DWUrpym5XjeTFRzIWf7CQRKItBc9bKIo089qp7rXNtHHb_YYM4b8uZ3a7FkKTsoSCqEnDTPIvv6k3BUXg3dLIDYDy0xFkUHSW9RwbZEiOtwlcinXZ-jdatHJn3_wBVqgbGnXPKhcHfL7UIggfXfNw4UNnvrXE5aKiKGmm155AOLfAQR0WSkX5xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تاریخچه تقابل‌های دو تیم پرسپولیس
🆚
صنعت نفت آبادان درتمام مسابقات: 48 مسابقه، 31 پیروزی پرسپولیس، 6 برد صنعت نفت و 11 بازی مساوی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/31239" target="_blank">📅 14:33 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31238">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S-Vwcx2ATMc_828-bhr1Th1CLDTpV6O-JrU2YZReFu8QXta-KsVS_UVW8075IFNDEL0h5RfUFsLliytgIi48WnJ8bqKi6FA0srG2eDiz1UXOO7UUFjrYD-HpX4duv0Fuf6YioySaEw-e-bZsjFjFKnt6gTj_e9oYAI-hk3nnl__vEA0R-R_0UiZL7GW0bZvvITxqbZx6QvwN7YQctRF3OkVdcAdk6wuS0KnK2rVdixNyxZmNmmtMwD0rS7KbHaCfOutMjroLFYg70H2Q9u1ttTDRJlrYxHZOChrOFb01rCZ0DttNQ77knQnKWAlrzpm2tlfP05M1W_H_B0vv2nm0Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
👤
دبل نیمار دربازی‌بامدادامروز سانتوس در لیگ برزیل؛ جفت گل‌های نیمار از روی نقطه پنالتی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/31238" target="_blank">📅 13:57 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31236">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GZ8gHA4n7Nztzs8e2EmUF-bRfb8yJLMpUwqZLMTaIinSP_Xfo7zX6kxwi22poImQVYNWCi7n7gL8ZrVgmVViPAfxVMjV_CNDJgPv7n00wdkoeDmvYl2Cul59nSEPMpxCTiCeRxAhQyqlcXqMuULE6C1EZfHsMwbh8Lu_vhPauaNAfijaEO4dQi5RdGZrqj523rBv9QluaLQbIzsNQH71gLWujN7BBkwU6u5Ho93z90hDSfJktL2rAlgKVG6fJOIMgyZzGJpi5oO6ufv_rLoQtFOZtri0t0vmXuE4CrStDyVmIyGOy9zw6x3BkpxUpqfHecmf7HbnFG7NUsi8Olo4FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qsbmz186mqZaBQK4gzXUX6oyzPKCBbMUmKJNYnM5UTvkomMUTH9icFnqQ4gnR8dvf7SpcPNduiFdCruyfFM9VRs1XXt60C37US0Hef1l9ZqZbVUeM1T5A_mPjypGPhBHuWvIiCVWCNbEDLG4m-tIdPCNGCzxECqy7zBmWeEH_mns7t_QNQrS5O8iCOfptLx4h2BgHP6KnlIW_GbZeqQRYvgG73ooQFAiY0t_O95i-lOwTWq3fopRTuv9w86k-o8VqMpzo9X0WnOTJhTMPJPb3yp1b33mH3cAvILz_t1M9MVzivZIsuib_ungyPuRZtzLo2GNuXP3A6pkW_Vqd_f72Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
صحبت‌های تلخ همسر خدا بیامرز هادی نوروزی اسطوره باشگاه پرسپولیس که با گذشت 12 سال از فوت هادی هنوز لباس مشکی‌اش رو در نیاورده‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/31236" target="_blank">📅 12:13 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31235">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1sNDwAD3zQve35udSJQydO8f17W0CZDCQnavwD-XJlgwTpIQxxCkQlnMIioXafNM-m3_WrslCbtvC3ljMMT8k0ip_bwh8oQEkuxv_eXJj9kKJ_r2eMcxvgSG8G-7TY9ECwZQoHbJ_kCCbvG40ejX6f4_39Hky49RsO_QnBpekzI9aSUyEhq0ZPPfg1bzDA94YoWidKVmAbSYarRlyBSxNqOxQ93VxZXhnOKsTs-GgkWt2bRz0_0w8WuLKrsqNnWUS4fEvEbx7d0TlfSsFj7BTUHe746oYu-cN-3dRdChBHFodnBBS7zLmJZLn-AdXpONlksbOuKx8_HlbzIGx5fPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تعدادجام‌های‌معتبر کریس‌رونالدو و لیونل مسی دو اسطوره تاریخ فوتبال در کل دوران‌حرفه‌ایشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/31235" target="_blank">📅 11:38 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31234">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TuVhOHozvo4vlrV7FvM4_sqVD70LUTEdYS2cjoCk8-BTxcN3qBkRej9Z_FMKLS6m_MBlObpGyS8NjctfUKIb7vDY6pYPfiPJPsC38jhcKqCIkXHgNfPyRDKbsAt1owkILawkPu7CYEKCTbC2Y2aTTOi2GgI1Bc-zaNdWVK45FpRXmyJOnGdmH_ExNBA0KHOPdxkKC-3cqoelyKo5A9Ie0SJn-iOigX7K2H5gjUVaXFDfpsYOYS89V_9XQNLxlucMNgzhZPARVSxLA7Euqnhar51paOS_aKrO9gf9E4Z7M54ue-VUXspvMn2O2iVkoP6z7XMiefU7Gn830AzjRieuhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
باگذشت‌دو روز ازبیانیه کریس رونالدو هنوز هیییچ بازیکنی از پرتغال این پست رو لایک نکرده!
‼️
این‌ویویو روببینید تامتوجه بشید که چرا کریس رونالدو اردوی تیم‌ملی پرتغال رو اون شب ترک کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/31234" target="_blank">📅 11:21 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31233">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">❌
این هفته هرکسی برنامه داشت امیر قلعه نویی رو تیکه پاره کرد؛ این بار نوبت به تیکه های سنگینن ابوطالبه که اینجوری زنرال رو چپ و راست کرد.
‼️
ویدیو کامل قسمت سوم برنامه ابوطالب رو هم میتونید از طریق پست ریپلای شده مشاهده کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/31233" target="_blank">📅 11:21 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31232">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vZeFKTI9KLu5mi99KnOof30mJA0WH2Ssu3c8GllqnpDP65p46N7UdEJX7xXkJl3sz0BUllKUi3fq76G-0W6A0kJZzjl5f_yjEinYc9i8Wae5iIcdqQ_O01cbz6kPkF3vpJAbcn8F44UCSaxQ3AQx0A6Eep-3CHQlksQGj5cVrbzJm1uJIXsZYCL4GFKn8cQ4iDzEFJ8tzWpqZTwtPH27i48xcKlsP9ftEyBBekwdRnRpI7OAhQk6t678zViOJS7JqOD53Iq4Ed-8TGyRfqjbvbZJ2e7214XthGz0p-xUHdla1NPRtahioDb6oD4XGavvEu4G1CmvA5G1VtGGwjvKiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دربی‌بت؛ جاییکه پیش‌بینی فقط حدس نیست، شروعِ برد های واقعیه!
✅
با لایسنس بین‌المللی معتبر، وارد زمینی شو که حرفه‌ای‌ها بازی می‌کنن!
✅
آفرهای خفن ثبت‌ن
ام در دربی‌بت؛ فرصت‌هایی که تکرار نمی‌شن:
⬅️
۱۰۰٪ بونوس اولین واریز؛ شروع انفجاری مثل قهرمان‌ها
⬅️
پشتیبانی کامل از همه ارزهای دیجیتال
⬅️
درگاه ریالی و تومنی امن، سریع و بی‌دردسر
⬅️
برداشت‌های آنی و بدون معطلی
⬅️
پشتیبانی حرفه‌ای ۲۴ ساعته، همیشه پشتتیم.
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
✅
دربی‌بت؛ بازی کن، ببر، لذت ببر!
🅰
r17
✅
https://DerbyBet.com
📩
@Derbybet</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/31232" target="_blank">📅 11:21 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31231">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kG9bZn1saMpVmshqEtSDou6cU41eF51-vM9mDfVa1CfRIpoq5E1EDTwPa8_FEmzWrveMPY7ejNs46hZp_or3yWjJjIlztVJC5zODot3V9-b6wPLvHQtcVEKAODIUNws58pCewn_oYtK0X11niAKYRNACUKxWlZqx24UhNWwrhME6uHOR26McRDe1kNQlLfP9O3Y0KrTY1ZCZlgtkUtExKMv-rFPL0Co4cvO47mzDQxpnmVHJ9kG7qPwqaN8lHdMi5zxNY6RJIiu2Zg0V94WfCCqvA-dWwY4dofzT-m75xyVyGWkuYxTCe0Pbw1yejWUaOSALTwbZRjOalgHmlZ06CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
به احتمال زیاد پرسپولیس امروز عصر با این ارنج به مصاف صنعت نفت آبادان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/31231" target="_blank">📅 11:04 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31230">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VPfcN95V7ywktdTHs7jAKChuuzSLGXn87C_EB0af_IlbcdxODr-cuNHMQ5mjm7uUqbM8K1F3eA7vu3TV5srSeE13gFZZKCsZ5GJm9XSTxVeNZdhC2-1uUfZc28rIPXnvJ68798MzjQdTLeCzPdOX6AqLIZaM4QOrypbzsVcJxQj21xHosmlc11o2lIgfdifxvBEtVICORm5jiltvn_udm-q2-zWDAXBv7zFZSZOnWn8_9piI5ZMCxHAFhAsqhy13OJHDvcPMnpWlUOD9juqpngf0zv1oK6oRJwTyLbwNBeRGBqaH4n8IyoS7ZEapF_fxTV1Np2TNJXrn0v_k-5lK2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صحنه‌ای‌که علیرضا بیرانوند درپایان دیدار دوتیم استقلال و تراکتور به‌این‌شکل‌سراغ‌یاسر آسانی ستاره آلبانیایی تیم استقلال رفت و جویای احوال او شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/31230" target="_blank">📅 10:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31229">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f9af88968.mp4?token=Lv6A7XKhe3k7_AOgSXZO7ZKYK9mIyWEJfI6G01QWLXyingeiPNeKW5s62ZfLNGWA6Nwyb35aLkK2ZYEhUbUp5QIL21YeZOIHrVHUL6fVob0Il3PKk8QkQxeTUBowjl4dYRPyAjd4ZS7L-Q7Zr1LxCE3NvRWs04OrGJnxFeUz8VyvhUhGIdD09ACrj0W-HQHBUzEF7JzJRrmaQ5pfL3bi-oEL3Z0jJEQy0jSnYgU49iGnsPgXvNbPBw_FiBBS2HXsaEGZgiRHS3Gsm4Vt4bdAgCSW0Vj1jRGKMLgSIeWw9f-w3kZY0ocB0rf-T7yvkaU0lYhTKt5Zx9RLmPFBErBvkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f9af88968.mp4?token=Lv6A7XKhe3k7_AOgSXZO7ZKYK9mIyWEJfI6G01QWLXyingeiPNeKW5s62ZfLNGWA6Nwyb35aLkK2ZYEhUbUp5QIL21YeZOIHrVHUL6fVob0Il3PKk8QkQxeTUBowjl4dYRPyAjd4ZS7L-Q7Zr1LxCE3NvRWs04OrGJnxFeUz8VyvhUhGIdD09ACrj0W-HQHBUzEF7JzJRrmaQ5pfL3bi-oEL3Z0jJEQy0jSnYgU49iGnsPgXvNbPBw_FiBBS2HXsaEGZgiRHS3Gsm4Vt4bdAgCSW0Vj1jRGKMLgSIeWw9f-w3kZY0ocB0rf-T7yvkaU0lYhTKt5Zx9RLmPFBErBvkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
ادعای نشریه فوت مرکاتو: نیمار زمانیکه در الهلال بوده به سران این باشگاه گفته جزیره میخوام اونام درجابراش‌خریدن. درامدنیمار درالهلال به حدی بالا بوده که درامد سیزده روزش رو به خرید جزیره اختصاص داده‌. نیمار در تیم الهلال به ازای هر لمس توپ، حدود ۱.۱ میلیون…</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/31229" target="_blank">📅 10:19 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31227">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AU2VDqmi2NpQ3K9Kvt4AEOgLkNA7WNy-d3Jg5ouxLUyhbSFn2k580SgMOe1y93O5eDxouvhIE7AOO50ighFwlp-dWEBaJkMU0mwnirrGYh2PqgJXk-J_EtgMKmoCQ5f-ovhTr2pTuVcG05qx327GXg6c_CVTiAPpDofnndTpJduSEGmE4OXKmviViyt-Xjgbui3qiXKgDnl0OfLXLbNHzD-2BYc8nEqiKWXun-7on-67vKWrWUfTqu29LSVDsj3h89Khm_Ikvwo0NSm2tSIwq8TgFwKdRPDk6UCVA276mM2fmg3mek-lqHHHsI97LdgjpbIrb_Jygr9hL3HPEehE_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
به احتمال زیاد پرسپولیس امروز عصر با این ارنج به مصاف صنعت نفت آبادان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/31227" target="_blank">📅 10:00 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31226">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TYfDPqU3j-6TzAYAf1wFTV6t7n-PSOFhPMPX8rok-vRscnuENqkL3VtFqdp4FSp-JKDJD5V3My6gdUNnpdagIK8nGnpG3ptzTnPdBLqlMYHEmtazOaI4Lc4YkZn_6pygvyKvhldOaCqf3XoqTpt6ekthwVE8zsYi16iXutN1iocUQGCK1362S2M_pjkB4EO1AIstI9PJzsrRjKJ-pnedVnx_I6TyYeVPuaNmEFVL4DY-b0lBRzgEUjw7cKDVITKRLo5jOG3AC9WOpvlMCaSwyWjbaDU-y7p102dQBGbVhd72iTWVWopUqMiQa0kf4n98X2Cqpo2Rz4BFRk3a2CA98w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌‌‌ امروز
؛ نبرد شاگردان تارتار با صنعت نفت و دیدار زنبورهای وستفالن مقابل وردربرمن برای حفظ صدرنشینی در بوندسلیگا
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/31226" target="_blank">📅 08:05 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31225">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FhwhilGqEdxfN9dWFIPT19NnHNLPHS52Oio5qF_j3B5Xr58B4-bc0IVKTr3R59RlUBslc9ysCZHW8RyH6n-sR0Dj9klls2IqU1WZBubVIf6ptqXZ_frzigYyiZok2fx4cOW43FQuWszCvgKh3bTOrZmapTIkF8FHD-ZNyK16sB52OBj6BYOiBK6ULIAF86-WlYuWizrGxPAAwVSDqEjVVYleXwlDOPL9OxfBViF-gz6Ke5cYGz3s74pT2tA5AcUl30OExQC1cscgocLTwl64NQMm39ukFG0nWgLn_CTGr5fY-tTtsGdVM--p65iy2qhZmO0sys4MDqiliwPG87tn-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌دیروز؛
از تساوی‌در نبرد استقلال و تراکتور تا آتش‌بازی سپاهان با درخشش حاج‌صفی
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/31225" target="_blank">📅 08:04 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31224">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">✅
هفته‌هشتم‌لیگ‌برتر؛تساوی‌شاگردان بختیاری زاده و نکونام در یادگار تبریز به کام پرسپولیس و سپاهان.
🔴
تراکتور تبریز
1️⃣
-
1️⃣
استقلال
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/31224" target="_blank">📅 01:06 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31223">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jr3LZ5yeIoYoMBmZ-SIQoY2JSX0FFDpEtDqKI-uls8ctsjrYlksoJGid8zffJGks9rR0WvQt273l6x2uWQ7WONPU3VPJAxWQ8j0Pbs7tzjDY8k6AfRc3DBv79Vs4Qu4LA0r1pGLDl7No4fHyjNmtewURSmDeSmltFX0OmooxdWTkUr-BasgI57yc7FUMXa-nAGuROAFJTMHx-wsYudvGpZCY9vByA5JMiuGU3eYUl0iv3A-ABc0ZkkoOaggw6NN2n7KNdoFwaloaJ5z3YkeTM5eHdjgONwNl-gqKbWWbZ9QBAbkam68LWWgmHaQhO954tMdHE0bTS28TqATenlR0tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صحنه‌ای‌که علیرضا بیرانوند درپایان دیدار دوتیم استقلال و تراکتور به‌این‌شکل‌سراغ‌یاسر آسانی ستاره آلبانیایی تیم استقلال رفت و جویای احوال او شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/31223" target="_blank">📅 00:48 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31222">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">‼️
علیرضا بیرانوند به‌دوستان‌نزدیک‌خودگفته تا تیر ماه سربازی‌اش به پایان میرسه و در نقل و انتقالات نیم فصل با قراردادی سه ساله استقلالی میشه.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/31222" target="_blank">📅 00:17 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31221">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a328e3cc8f.mp4?token=Udh19sXRM_gIiPdX79Gpi36eYmZUw_Rwv4alR1yhKUNBhPvJLt-n3rOW2W05PI62fcITQFj9y9hPyq_Yl0pT27YFow4xfD8aJ5Rap5UNLr5ffc86eQWv0QtdBnwLWkO80HtZaQAF-EcV18IxhujJOFuabrP5rBEDgyPu0vD2KKjOWTr5iKh3qjU1Xoc49Iy44jrztewI8IL53oc64Z2HDV6TtmwFXtKfbtvnqt8oEjqzGaAD8yH86h4-bPiuJSbeNgIWqHRWLxrqRkjU3wPG5uBg6APA7qUFywSJxbxRiRxTz6oMQvQI3vZ36IXCnRZFU9Obi_wgnH16Mtv70nPRjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a328e3cc8f.mp4?token=Udh19sXRM_gIiPdX79Gpi36eYmZUw_Rwv4alR1yhKUNBhPvJLt-n3rOW2W05PI62fcITQFj9y9hPyq_Yl0pT27YFow4xfD8aJ5Rap5UNLr5ffc86eQWv0QtdBnwLWkO80HtZaQAF-EcV18IxhujJOFuabrP5rBEDgyPu0vD2KKjOWTr5iKh3qjU1Xoc49Iy44jrztewI8IL53oc64Z2HDV6TtmwFXtKfbtvnqt8oEjqzGaAD8yH86h4-bPiuJSbeNgIWqHRWLxrqRkjU3wPG5uBg6APA7qUFywSJxbxRiRxTz6oMQvQI3vZ36IXCnRZFU9Obi_wgnH16Mtv70nPRjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های تلخ همسر خدا بیامرز هادی نوروزی اسطوره باشگاه پرسپولیس که با گذشت 12 سال از فوت هادی هنوز لباس مشکی‌اش رو در نیاورده‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/31221" target="_blank">📅 00:06 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31220">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FlKDjakjgtw3S_VBHACyqbKIBOLWlr1I_P19Xqcj7Ow-8120nMAc6zbd1yXFY4Ve5QtH2jFyBvr8S2yQbnlC9wgxUqIObALHUrrJcyKYxsq8oCb9M1iAfmS27poNqfltEHjAnH4CtVR51mWUj5Ma7O0BvRMtoTPk2KmmSGn9ieJycBAcQ65E-VT6tE-17ndlvLegYdewK6Dg11wvQ1G6r19H5snruvSxJW7dv9xEtL7wjgKPIPEsew3cbDU_1x1cBQ28sesPNyyk-Lie9rORjcHZbl6mizy_LQMnl0w7j29UhVTswRsfrwGl-lDjAqN_yUjkcubPI_bonuc2692lVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#فکت؛ کریستیانو رونالدو در طول کریرش مقابل 159 باشگاه مختلف‌گلزنی کرده است. اگر فردا مقابل باشگاه‌الدرعیه گلزنی کنه اولین بازیکنی خواهد بود که مقابل 160 باشگاه مختلف گلزنی کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/31220" target="_blank">📅 23:48 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31219">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K4TwDP0GH8vrxKMGgxYCgw5sTijfylsOGPLqmakQM7KA2WVoVjqc6DnCxWYQpWL81jM26BnF16wdhW3xFq_NSe9lZE9He-EARlErqR_q4LdtZFHwaGaT3DmGjrkeMp3d9WlWnGWTg5Cgq_q36h5cI_r21diKfYySbpZW1CxkcHYWS2NtKn3PCX6_MsjHYXdFf3eGbT7gEECOX23f8zEUcQivNDdwT8adFFcnhD4pKiPMCvvctA4vjEi6AyktZb6lmIS5bxe36-OYAsv3NAn6OwN06dn5-wCbu5Bz9w9WsL--s_JJPujS9eKPuEAD8xfMTGufrxdRJxwYEDpF8vqLBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شجاع خلیل‌زاده بیرانوند رو آنفالو کرده و از همه بازیکنان خواسته‌که‌این‌بازیکن رو آنفالو کنند. بیرو بعد بازی بااستقلال گفته تصمیم نهایی‌ام رو برای پیوستن به این تیم در پایان خدمت سربازی ام گرفته ام.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/31219" target="_blank">📅 23:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31218">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CIpW61jG40XBSrrQkDnFVM-xtMLqwl2b6DvYBdXQA3VaIjlxtc4xLevvDq0oBh4Qr7MFo_BLSVvrUMoFdxJ5DLzUJQZUlIZAsm67_qh2B8nynPJCxZk1RCT1GiUuiWKN9GVM5qaEhbcbBsF0EeP0IPw2hcaBP8-Y4bYeACtElpV8pTgbLdXDQ7Pr2QQjbgABYrsjatWJBHlgVDTegujgnRgCzjTwXGGBVqkhZ9Olks5gfDZH9tNveqUOYMtmKWBy5JIuBsCTNVvZYfYy96l9qsbSB0wpxA2qxfQht8xJCbl4DHCGD7zn1JjXMiyWq6eRzINJEE5E0ReZifiQTKCwxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#فکت
؛
کریستیانو رونالدو در طول کریرش مقابل 159 باشگاه مختلف‌گلزنی کرده است. اگر فردا مقابل باشگاه‌الدرعیه گلزنی کنه اولین بازیکنی خواهد بود که مقابل 160 باشگاه مختلف گلزنی کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/31218" target="_blank">📅 23:18 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31217">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e52465a28.mp4?token=uAvNJ65g_98rkx4ElJrslWS1gVnGolX4CTu7hBvk8q7n0TVdB5DPyStsaytG1l9sKfDhfa39xUeZX6r_hEADus_HSshOY7jUi9u84KaDjDIRGrgSBb3qcH8muFVBo5TmC9DCCj_z8WlnF0PyRHq-IYNx7sG1I76LGFl6GpTglOV348IDoZKbYwchDIL3Td-6l4qsJwGf0o1SvVVr3KijLAFGTwv08AlIAg359rP2NWAzGf2UNe333Btb0FGQCOp7jptUkiz_mYV24NigKewaEWwhaqzGCBiwS2s9gvUUg2GNCeDr8_tJOA_YprWkUgYD_mfWSG6ko_Wb7OVfyjody0hVt0OUOv-uNmV_c9SXG0pWJFYNkr-0LDuONtxtyhaFI9hCHPv6AzUVR56CqzCRS6ZgD7JnZM324JiTY6vDigC-NmJ6qM62RwXMrPfSuz9vbLc4rW6_WyWFYr2z_BWKdXWLJXIrMknvIei-NglHdv-LdV27IEc8QXHWJu7Hra0_xiaqmndJmcQFwdfcoDnGgaRQb2XBUBcR1mWjvSq2XtTluNK0m1-_c2Puf3vbdGAHfqATT9808VOB2KuH40NdBboxG0qieoErml0NkqmKBgv_OU1YUXP_J7aFLtNHRAAv7DAtJPkSkL6XnUsbD-NOoIXqQ36IpcdNL1xpJGJzMvU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e52465a28.mp4?token=uAvNJ65g_98rkx4ElJrslWS1gVnGolX4CTu7hBvk8q7n0TVdB5DPyStsaytG1l9sKfDhfa39xUeZX6r_hEADus_HSshOY7jUi9u84KaDjDIRGrgSBb3qcH8muFVBo5TmC9DCCj_z8WlnF0PyRHq-IYNx7sG1I76LGFl6GpTglOV348IDoZKbYwchDIL3Td-6l4qsJwGf0o1SvVVr3KijLAFGTwv08AlIAg359rP2NWAzGf2UNe333Btb0FGQCOp7jptUkiz_mYV24NigKewaEWwhaqzGCBiwS2s9gvUUg2GNCeDr8_tJOA_YprWkUgYD_mfWSG6ko_Wb7OVfyjody0hVt0OUOv-uNmV_c9SXG0pWJFYNkr-0LDuONtxtyhaFI9hCHPv6AzUVR56CqzCRS6ZgD7JnZM324JiTY6vDigC-NmJ6qM62RwXMrPfSuz9vbLc4rW6_WyWFYr2z_BWKdXWLJXIrMknvIei-NglHdv-LdV27IEc8QXHWJu7Hra0_xiaqmndJmcQFwdfcoDnGgaRQb2XBUBcR1mWjvSq2XtTluNK0m1-_c2Puf3vbdGAHfqATT9808VOB2KuH40NdBboxG0qieoErml0NkqmKBgv_OU1YUXP_J7aFLtNHRAAv7DAtJPkSkL6XnUsbD-NOoIXqQ36IpcdNL1xpJGJzMvU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
نتایج و جدول رده‌بندی لیگ برتر در پایان مسابقات امروز؛ تقابل حساس فردا پرسپولیس مقابل صنعت نفت آبادان در هفته هشتم لیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/31217" target="_blank">📅 22:52 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31216">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WC6GqTvb9romXSIY0L7p9hPjdSVl7TQ65gJyvbocU71cGrVhGZBOF2SiXN7-ewhUsP4ovN3QrnHf0or5S7UdYhgCmEnboaB5npcTbxT7Jm2cSPWLAFiomHu4KkYNeOkg9PqdewsgOhVOUo-U5qh-HWspFaDTlcbmnc-R_K_3Ct0GcFytlvxxbiEfBCJwiUhfYxwNCRPL_G_gfuls4fMcMlqkONDAVAQ48k-yCh9SOpPpaMbjXTurbaQCyweLk6oEQrc7pB7y_YeGOYf4LiCUGQNQlhTECz9XWguAAOMAZH6-xLE4-8yX54JJ1WzAQ4rh6IyOopbGaucqhg6nTqz4pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق آخرین اخبار دریافتی رسانه پرشیانا؛جدایی‌دنیل‌گرا و مارکو باکیچ در نیم فصل از پرسپولیس قطعی‌شده‌است و مهدی تارتار به مدیریت اعلام کرده نیازی به این دو بازیکن خارجی ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/31216" target="_blank">📅 22:44 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31215">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JTOZNp_y9m0aJa4Cne8gdFEOwn1ntDRWdMblcGXQ5LnCuMSRn5hRIInGhQoVTqKlMT55N7lnpz_1FSNoz3LfK-kFeG5mtB94-HzpEpYqUC2vBf7ioxjPiAgVU48rvOLkhU2lVUb_oZV9RIc7Q4WnDoHFGKITKE16qWbFLoHIp4ttcXkG7QSQKNq6mmv5clXu2HatkZvvzWFAul4Fmz3RPsukCzmDKiXJKwqt8bOCK6FvHzipG1yFMs69ibk9bp9faMWxUl4qug64ZBqZTf6bcjV7zIEhc3ZAto9s6UzDOxJMn-oAfUg75mL0N0j3xgDsuonmkud5wGspvcRtKrBcLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ژاوی اسپارت ستاره 19 ساله تیم بارسلونا قرار دادش رو تا سال 2030 با آبی اناری‌ ها تمدید کرد. اسپارت قابلیت بازی درچهارپست مختلف رو داره و در واقع آچر فرانسه جوان تیم هانسی فلیک است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/31215" target="_blank">📅 22:34 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31214">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gxyJlTmBCHJryEgo86oxp9RisvAyOoAyfJwf-VxzTz_Sov3Pub5x0vr_irJK_hkCWTOT1ACLYxj43UdKOfpEZj67EdpP3PTwXHlVnR-GzyGhFqNnVpqdMKBGwCtzoMxI-eh9DRufzRsVXnltiDmhWmQbZTGZiyKqxnG-mMowsNU3nNetK3nPgG3WXu6TkGeEJhqEC7aE8IIzKDE03ESWyc-MxnM58h_3_irF8FoVyYjJAze9f-bOhLoE4Z61rRAbwiNEfpFEBBdZ0EyEcumzkCG9ZTWrF8wbCNUeAgNnAEWSH2ZMuiVKG3VS8eIimNknB8YP6N1-ylNMMrJ8aOgtLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه ال‌ناسیونال: اولیسه خواهان بند آزاد‌سازی ۱۷۵ میلیون‌یورویی درقرارداد جدید با بایرن‌مونیخه و گفته درصورتی تمدیدمیکنم که این بند رو بگنجانید و هر باشگاهی "رئال" این پول رو داد بند رو فعال کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/31214" target="_blank">📅 22:25 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31213">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e828d2e24.mp4?token=jnqwZCDghn4gJnlllly2g6kcuJTzr295Rk-YncL4mrwh8EKtQGEwm6ZymNHodkPA2Z7inKMiWoPcazSkKnS5OqB0TSvsln85kX50pIna7HbTvFA-5oMQoeukoFTypChD_D0VY5EycNqtUkyAm0KjUxe9aQCRIyZrVmzmD54fvIMJooBiaK4YULdWDAVQWrfBdmGFNLrxsvqNiVufMUO1KS1wyb0qInO7I0IpFDQ8qLjs8QC0bF_GZFe6LgJfyp8OBRfDwlj0z4XEEiZTgSdoiykSAYHO9S1SDimkGFPlNifJ19XOhjqt0z4FT-_NYF8gSeLTmEWzBcj2_xYpVwaC8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e828d2e24.mp4?token=jnqwZCDghn4gJnlllly2g6kcuJTzr295Rk-YncL4mrwh8EKtQGEwm6ZymNHodkPA2Z7inKMiWoPcazSkKnS5OqB0TSvsln85kX50pIna7HbTvFA-5oMQoeukoFTypChD_D0VY5EycNqtUkyAm0KjUxe9aQCRIyZrVmzmD54fvIMJooBiaK4YULdWDAVQWrfBdmGFNLrxsvqNiVufMUO1KS1wyb0qInO7I0IpFDQ8qLjs8QC0bF_GZFe6LgJfyp8OBRfDwlj0z4XEEiZTgSdoiykSAYHO9S1SDimkGFPlNifJ19XOhjqt0z4FT-_NYF8gSeLTmEWzBcj2_xYpVwaC8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
مهدی طارمی مهاجم 34 ساله تیم الوصل در اقدامی خیر خواهانه 8 زندانی در تهران رو آزاد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/31213" target="_blank">📅 21:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31212">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z3ZZdUVYnVeC9hUbQbDoRW54N0cC3At2Os5qDgtn_HcwJd2kBllZybWUhMLOcVUMpEZPRip7tGLEtArY4AoNoojYoujiH03uml0uuENa8in48hHI4VhPc4oWGfe3xFYd0L9zSBOtXmBVBQIrsYzs0zNr9cBKWeq25MdDNHXvlivIChzByK4XaGre5rLBlmz47jnKc2NpDAx7_hUnYQDYTRQSqYE24LTTYWs3Gg_IJxjouf87yrxXALg2e4xgwesZrC2q6VMXI9-ln27Q5YB07nR3x2dTalNLV0aRlZz-RI_aPbslSKfTuiqtYXZMMna2DBKtIFFjXFDW-N4wHkJyVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
واکنش‌ علیرضا بیرانوند به احتمال حضورش در استقلال: استقلال تیم بزرگیه. من یک تصمیمی گرفته ام و 100 درصد روی تصمیم هم هستم. من نیم فصل سرباز هستم و بعد از نیم فصل بازیکن آزاد هستم و تصمیمی خواهم گرفت که به آینده ام کمک کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/31212" target="_blank">📅 21:28 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31211">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">‼️
#تکمیلی؛ علیرضا بیرانوند گلر33ساله تراکتور به دوستان نزدیک خود در تیم تراکتور گفته دیگر برنامه ای برای‌تمدیدقراردادم با تراکتور ندارم و بعد از اتمام خدمت سربازی ام به باشگاه استقلال خواهم رفت. با توجه به این‌که محمد خلیفه نیم فصل به استقلال باز خواهد گشت…</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/31211" target="_blank">📅 21:08 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31209">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YsGSLizQ2qOZGjYKNqZy5leVO3ftEctq9FR2pNBznPttGlxwxyhkX74tCjiVJKCdlz3mBpACehhaWtDABSSSG2CK1bfUrI8VU6T2cuewcLIqSagfHblWTqcS91jlbGnPwCcp9tuj88AUYGMRKt2jAsaEtzRIIaLVqR8g4dwtz1LpCzGKJkrN32BANHUS_RoXfpkTFf6tJiv_Yh8LHASmi23qyCrZU49LJFX1zTBxeobHix_cYuqPjSHYtHVm9C_53Zf-kVB7dwhJRS8s8eYWH2_5zREgKp1ERmg9IcSrrhw8GfPezH5b3AJpuTuBXowT_yOR5kSV38PrNseL4yE1ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DTfzKvn6OBt4FkcjadYXBqzRtW1gqZGn5XNRm-vAbf95zH7LcFx4atfY7pR0ZExS7tevsO1LKs8XPt0UsAQONEwpHArxtfxB4q54L0wB2ai80FQIua-imjQK9b-Z9Zp5weTffmy-7OfvYLjTeOjmjAfBP5N5jWQZC8vNkYGcwFmJQ_0z2TN68QINRNljNBso4dDKc2fc4jQJAU9BC98oU63ftU6J2bO8BJweGAb0d59KDPPWIxenK93fS89cgXvaemaPNXIDm3rnU8YB033QOiV1xMaM5tN0Ibj7SH3GNJoLvrrvUPIBetrL3gXVqHxFDu72w_xuF6W4osD0AZ8-FA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🟡
گل پنجم و ششم سپاهان اصفهان به فجرسپاسی توسط مهدی لیموچی و آریا شفیع دوست؛ هر دو گل خوشکل و تماشایی زده شد جفتشون رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/31209" target="_blank">📅 21:07 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31208">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd5e0f0ae9.mp4?token=cJQKlfBMH-DJMzX64tu9vfQf882iVBay_Qnlk1zLd8XEQVSLhA02DiejHLKZovptS6ANIs8MnW4zcCsR2BgZCnyjgn8lvgXIm6a2sCYd1rIZQgIpQKZwTtTMXlrY4O4CNgTHjuhZNYYYAWnQzQ_BmjaTmD-mxS5bK7WAPDyarAZ5mCwqa2CE-Y9X-KvsLBG6xEVQadA_vQhwGPErmMKP2jnuGSPGhmSFIt2tMBGPA5eoNCncesi7Ls5Z7A7HbVN5Qh8gi1JzAteux6D4Fbz1oX4Vp7O5KnMzUXsMfFvsIiAX5edhpwaJlEK7PHQn4jODoqlUwKvrjcPyCJzv6I-8F59K8QB4cUJauD71b96OOpGHcDKRkRjO3_tc4C_5kt-QmOz2XdrYx_Tlj64XU7lE5JgrNjWQhuAiVbev4A0zkrZvt7uNAcneP5qXtOVQ_cVJm352LOdDi2uF0SO-gQjIU4mmYVNZwLqQnI7iJHCmXxnAKNkqboV0bnHumuOKIOCYMn6SkSaUn-hkw08FzyLDo2vdKKPtSUMH-yBu073RZ6M5Nmm2rdG_XuNCzIF8SidbVMpXl0AQeUtdd-MhO7pNGDHn9eSksQZ2V3LT_i_aDkBwfHXOELdGxk4dI4hBgIdXoRK3CROgE664h9N1QaLIcF6nluIfdjdoLbHYZ0ENfBk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd5e0f0ae9.mp4?token=cJQKlfBMH-DJMzX64tu9vfQf882iVBay_Qnlk1zLd8XEQVSLhA02DiejHLKZovptS6ANIs8MnW4zcCsR2BgZCnyjgn8lvgXIm6a2sCYd1rIZQgIpQKZwTtTMXlrY4O4CNgTHjuhZNYYYAWnQzQ_BmjaTmD-mxS5bK7WAPDyarAZ5mCwqa2CE-Y9X-KvsLBG6xEVQadA_vQhwGPErmMKP2jnuGSPGhmSFIt2tMBGPA5eoNCncesi7Ls5Z7A7HbVN5Qh8gi1JzAteux6D4Fbz1oX4Vp7O5KnMzUXsMfFvsIiAX5edhpwaJlEK7PHQn4jODoqlUwKvrjcPyCJzv6I-8F59K8QB4cUJauD71b96OOpGHcDKRkRjO3_tc4C_5kt-QmOz2XdrYx_Tlj64XU7lE5JgrNjWQhuAiVbev4A0zkrZvt7uNAcneP5qXtOVQ_cVJm352LOdDi2uF0SO-gQjIU4mmYVNZwLqQnI7iJHCmXxnAKNkqboV0bnHumuOKIOCYMn6SkSaUn-hkw08FzyLDo2vdKKPtSUMH-yBu073RZ6M5Nmm2rdG_XuNCzIF8SidbVMpXl0AQeUtdd-MhO7pNGDHn9eSksQZ2V3LT_i_aDkBwfHXOELdGxk4dI4hBgIdXoRK3CROgE664h9N1QaLIcF6nluIfdjdoLbHYZ0ENfBk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
گل سوم و چهار سپاهان به فجرسپاسی روی دبل دیدنی احسان حاج صفی و آریا یوسفی در نیمه دوم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/31208" target="_blank">📅 20:34 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31207">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b78ef0133d.mp4?token=sTnS5f3iNXWl0GxLgNIGe9dpK1BXthWSLWx2Yu7WoaxmYJmn4Kd6KiCrNcU2aTAAC7NKFVwMY-p1B83f1c0lN-Oc5LxYrXAjcGeuIhSFHVPHdrg8XWDpgarVN6RxP5W_j_T5UfR1ivWhHkL72MCKiOW5Y_QwQGoB7U8ph60ySuFgYxRlm7KOxGSK6a20TxOaowvC9c8g2P-S7fEfrmSXxJo4g80vSpMc3rKsN-cX6bTEtZ6ZSZtMu8L2P7U-k8Ez703v61S9D3j9w9GIe-VXhMjv32RGOcq7qg35DAF7kFAe6adtwLehRD9luiyHnDmX3nmA8KHVR8zopjj0r8_YiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b78ef0133d.mp4?token=sTnS5f3iNXWl0GxLgNIGe9dpK1BXthWSLWx2Yu7WoaxmYJmn4Kd6KiCrNcU2aTAAC7NKFVwMY-p1B83f1c0lN-Oc5LxYrXAjcGeuIhSFHVPHdrg8XWDpgarVN6RxP5W_j_T5UfR1ivWhHkL72MCKiOW5Y_QwQGoB7U8ph60ySuFgYxRlm7KOxGSK6a20TxOaowvC9c8g2P-S7fEfrmSXxJo4g80vSpMc3rKsN-cX6bTEtZ6ZSZtMu8L2P7U-k8Ez703v61S9D3j9w9GIe-VXhMjv32RGOcq7qg35DAF7kFAe6adtwLehRD9luiyHnDmX3nmA8KHVR8zopjj0r8_YiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
گل سوم و چهار سپاهان به فجرسپاسی روی دبل دیدنی احسان حاج صفی و آریا یوسفی در نیمه دوم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/31207" target="_blank">📅 20:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31206">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bH1QYZ2VCXnqZUrD7A0M5igIDvZ6fSK2b-o7LK9-LeY2iZaJqLeDahj7y44xHarQ9Na1nEZwcQ2hHKILepXuKSKcxi3RDVJDPsDdm0RRQmSZTopoD-5phQyRDwopvrZak6LzHcQjyuSDDfHq4JOqHFaRMmUkNzLCUcEL0HOyS5V_9V-uppimvT96VDvHNAIip-Ha8Bxxlm04e8Gww-IWyOMLG_06nt69EBNLErbzxPNvfHtMis07dqzbc9bSy2hAi3VR7K-FwjdSjbXhOZyvdZ5WdVP0_C3UOJIuR4U3IsoVwW9Y648UpLenkeYiGbYaFKPGmUimju7s9lTrzEY1nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دونالدترامپ رسمااعلام کردکه تاقبل انتخابات که ۲۵ روز دیگر شروع میشه به ایران حمله نخواهد کرد.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/31206" target="_blank">📅 20:22 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31205">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20c2c2b307.mp4?token=MOWi3CBXOq0jro2RSRa01eIExHV8Athm6e7LBqOYR4HAycZtA0PLjE6TjzGBKVlfBrXHarJE60pgLgq-ZPHVn6XNh7EfAUqYpXq7yhPK4kmHgr75oHbKIxnzUply2IhbHyI6NstRWcZBrwuI_N9AlO7rT_D2iUy8ggg71ePmst2QZV-xZGVKMoegQWuoM8UqrrIO01eP7tF8TnyrUXbx9kr7jbT35ZoZjT1qOy3xwc1FyUkH5b5TgCYUBBi8j0zKlLolRZ2FYuA6XGx2HJy6qS1iPLc5BXPDSFAlBBxn_p1TeQPoJ2YHRuRx60ZBUb1pcjl_pqXfTImXdMLoSu-v7KUKh7Xex3OgmIk_XNOxQq1A1vkW6E4FGefcMdN8EO6FWgmnO9UYlAe7OvECjWxpAgtFXHxr2NxosmpgMVWfPGpklH8OgNcYV-EMfQK8YURmMFat1Egu8EoADattRQDvE2qDAwvVCPbaDCqIC7t3P7vDqapDih-0yCFAYsKoWHtvvUBg4v_TLUY3f5Q21lrOycpl0A8i1RMtlHniU8MfWOdWUa6ZOwj5wxUjvbl2gg5QTcDV1zf7wcShJkkXdLzfPV_c204_F2-NnQmw6r5DwKf4TApiYD2Ui1gMIMKU4H-3h7HH7aDN-Nlt4-hnBA8xzAPCbt7PlsIl5Ktiiw1h4v8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20c2c2b307.mp4?token=MOWi3CBXOq0jro2RSRa01eIExHV8Athm6e7LBqOYR4HAycZtA0PLjE6TjzGBKVlfBrXHarJE60pgLgq-ZPHVn6XNh7EfAUqYpXq7yhPK4kmHgr75oHbKIxnzUply2IhbHyI6NstRWcZBrwuI_N9AlO7rT_D2iUy8ggg71ePmst2QZV-xZGVKMoegQWuoM8UqrrIO01eP7tF8TnyrUXbx9kr7jbT35ZoZjT1qOy3xwc1FyUkH5b5TgCYUBBi8j0zKlLolRZ2FYuA6XGx2HJy6qS1iPLc5BXPDSFAlBBxn_p1TeQPoJ2YHRuRx60ZBUb1pcjl_pqXfTImXdMLoSu-v7KUKh7Xex3OgmIk_XNOxQq1A1vkW6E4FGefcMdN8EO6FWgmnO9UYlAe7OvECjWxpAgtFXHxr2NxosmpgMVWfPGpklH8OgNcYV-EMfQK8YURmMFat1Egu8EoADattRQDvE2qDAwvVCPbaDCqIC7t3P7vDqapDih-0yCFAYsKoWHtvvUBg4v_TLUY3f5Q21lrOycpl0A8i1RMtlHniU8MfWOdWUa6ZOwj5wxUjvbl2gg5QTcDV1zf7wcShJkkXdLzfPV_c204_F2-NnQmw6r5DwKf4TApiYD2Ui1gMIMKU4H-3h7HH7aDN-Nlt4-hnBA8xzAPCbt7PlsIl5Ktiiw1h4v8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
یادگار رستمی ستاره 21 ساله فجرسپاسی به این شکل از پشت محوطه جریمه روی یک شوت تماشایی دروازه سید حسین حسینی و سپاهان رو باز کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/31205" target="_blank">📅 20:12 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31204">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b8e357fbe.mp4?token=pnQOcXxpcFeuPjBVcfOgnFhPy0z1uYbKJfvUsYQ1y8ar4xr64d_ZvCd2R0BzObHeghlgAPjRc5ko16pzTB9LV3-jpPUwsvCGoJOBC__vPbj-hQ2S9hEbCCoPAFCWDtlZRwX_iEYrVwvlrk_QXMb12WKacnHQkcYPm6yWqvgK765ZHxNZupxBNhFf-oPKhVvI596oPueTw3lWtx1bH53RtZgtrxJHPdix8VET4kqoOwzzzN5MZB1EbrQnxezGLRgvuq2WcvF6Hcau_mxorG03oTyUlhDTl_FcGecIIrdVLAKZgs8cxGxZGAHrUUPLbwhh-lzt1NS9ZAZZBsh-UHKNjh3YhSkNS8kEiemLRoF8q3PBuEDBUWSHb4LCyHSk8PXZBT-LbttYooCjeYzXEupD4lvQj1Y344bIQ1AwspY4ILCTbGD3LiSYixf-4-k5-S5wZ0IGxW4cxUq4k2n3WP0xB1tcMeJbkvqoaMEEH2lX-KJumX6SHHm7V3v3d-Y6uOUh3PDJ55QNYT2KHV2ex2VNZ14MiSEDPXTBidTVLS7JMFKzTSk24kYIBhnNg_l-0C-_fqj3JD9jonBfUyqSI7oEXFB-5qHwoRNCaLEuPpU9TJqNNvaDEywTICcQClb21WuH4zUyq4W_ANMtY3gEsfVFYEnjCche5HD0ulmwzZltj04" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b8e357fbe.mp4?token=pnQOcXxpcFeuPjBVcfOgnFhPy0z1uYbKJfvUsYQ1y8ar4xr64d_ZvCd2R0BzObHeghlgAPjRc5ko16pzTB9LV3-jpPUwsvCGoJOBC__vPbj-hQ2S9hEbCCoPAFCWDtlZRwX_iEYrVwvlrk_QXMb12WKacnHQkcYPm6yWqvgK765ZHxNZupxBNhFf-oPKhVvI596oPueTw3lWtx1bH53RtZgtrxJHPdix8VET4kqoOwzzzN5MZB1EbrQnxezGLRgvuq2WcvF6Hcau_mxorG03oTyUlhDTl_FcGecIIrdVLAKZgs8cxGxZGAHrUUPLbwhh-lzt1NS9ZAZZBsh-UHKNjh3YhSkNS8kEiemLRoF8q3PBuEDBUWSHb4LCyHSk8PXZBT-LbttYooCjeYzXEupD4lvQj1Y344bIQ1AwspY4ILCTbGD3LiSYixf-4-k5-S5wZ0IGxW4cxUq4k2n3WP0xB1tcMeJbkvqoaMEEH2lX-KJumX6SHHm7V3v3d-Y6uOUh3PDJ55QNYT2KHV2ex2VNZ14MiSEDPXTBidTVLS7JMFKzTSk24kYIBhnNg_l-0C-_fqj3JD9jonBfUyqSI7oEXFB-5qHwoRNCaLEuPpU9TJqNNvaDEywTICcQClb21WuH4zUyq4W_ANMtY3gEsfVFYEnjCche5HD0ulmwzZltj04" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
ویدیویی زیبا و دقیق از آنالیز بارسلونا مدل هانسی فلیک در فصل جدید رقابتای لالیگا و UCL.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/31204" target="_blank">📅 20:02 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31203">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbbf119a08.mp4?token=I_mm7pF5Y8J5o0_tkHVOPIekVkg-LZWGw0w_JDl2oS3UDNzGsRTNuhQ9E4EapxxAw0tZgKiwkj9XX0vp467bDkCMhtdeMmymsC-ttamWN5sL2VMolsh9JbJGc8GUUdTCrFuJ5g_brn2DMI2JqYy2NisK1-u1Zy1hYkn5FLXCgr2tPb0outZVjnOOmSE6h_9hXtrbz5sQ4ent-kqgsf4ALlJX-g73LEaeDdXl6Xrxxk8F7tqw60aSeOefXJIRDLJsYYfC0LeiyNuy3uEH93NXNnGMp_HTLGo2JBtBqu887j6asgFnUg_TYxCXD6G7bt8bBvIw5wITfYSsUsKUnLvavw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbbf119a08.mp4?token=I_mm7pF5Y8J5o0_tkHVOPIekVkg-LZWGw0w_JDl2oS3UDNzGsRTNuhQ9E4EapxxAw0tZgKiwkj9XX0vp467bDkCMhtdeMmymsC-ttamWN5sL2VMolsh9JbJGc8GUUdTCrFuJ5g_brn2DMI2JqYy2NisK1-u1Zy1hYkn5FLXCgr2tPb0outZVjnOOmSE6h_9hXtrbz5sQ4ent-kqgsf4ALlJX-g73LEaeDdXl6Xrxxk8F7tqw60aSeOefXJIRDLJsYYfC0LeiyNuy3uEH93NXNnGMp_HTLGo2JBtBqu887j6asgFnUg_TYxCXD6G7bt8bBvIw5wITfYSsUsKUnLvavw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
گل‌دوم‌سپاهان‌به‌فجرسپاسی‌روی‌شوت دیدنی احسان حاج صفی کاپیتان طلایی پوشان دقیقه 38
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/31203" target="_blank">📅 19:40 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31202">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L9p3khxQACmS_xlryJ_upcCxqwv9aj4A5EliCOVmnROU52fZj7nkhEUqfOvOmfo6KWbTSVpWy4qv5gs0SW6CyNRAAvGZ-qvwZPGwYBAI-BNnQ3JUFgpu1fqOMrERLHuurdaBp76LmVGXl3Gz8LLBV8cLD0cazkuTrmCfI5JzMZpP7irFCf6FwL2s9bWcdI7fNiWby9m1XrJvXrku0O2BRI8MmX6KJEkANzGDi--YFmzPcIfMaKXc9Wo8ww9Z4x8GkcZ40_rs1xNfOPI5NkNQiTMyZXoeY2hyJgoWiuQ26wltfWX9OACJpLNMzFXkTceZ4eG937WdJPELuv4KeS1I8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
خرافات جواب داد؟! یاسر آسانی ستاره آلبانیایی تیم استقلال به دلیل مصدومیت در نیمه اول دیدار با تیم‌تراکتور دربین دونیمه تعویض شد. آسانی چند روز پیش با حضور در برنامه عادل با او گفتگویی داشت.
‼️
پیش‌تر نیز عباس‌کهریزی، پوریاپورعلی دو بازیکن  آلومینیوم و پرسپولیس‌نیزدچار…</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/31202" target="_blank">📅 19:36 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31201">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/194218a84f.mp4?token=FAArFissOi-XuLI8WmEaGqd9B-QcQBgLkTw3Orwpo9_YTEPF8SNYXECBKiMTZWeYQ8VZJKhAUBRBZ6POXncbAVJEtZlqvQnj4ihn245g9S-RFk7Zm092EhTveNyXZ9Fhp7V5_yT3C3RZYWRe0lmrLSjDWtA_YMPbnGNH9McI2S9QETLNuD1Ak6Iy-jntPR5y6lroAGuwqm6QL99IRVSAAmPgyE_fxvjnwKMQim2YiDJEO03zByC8G9qAxx80sYJXHv2t9QervjK7cGoAg2Ifcti6bS98Ao8CFQ-8TUUpZ9gG2cmclAgY64CgEZWYk-e2_TOOjt2AbrhiSkjI-ymcxD7FxY5SJ7IJz9x20FOdZtJ_gIyYhFFyjmtAVlD4urtFvcZwwYIkOIN3iPIqMmKdZvOQI3tkjgMMCqUrTPuDjxrUQ-Yd48uqFxl7M7kBzHkJnuEs0PyluahIfxLo05Svy7b8AdGNK8ypf79qTtwp1YsIS6bonfmSbGkNWSx9jl-77R0rsyIm-TrlR_-pWZy5S1rSCQ__PApb6NPHeAzKbpjDJZrSpZE04Qxo2iv2AHRv5n1A5AfW6nQbHMYFB0VPuznTt1KjlGfntOxuNQ7GR62qI9uwPhHcANFWm8nbfpIS2wcCC40mM-BX3dMFmV4pOABXppMq3XN5pbrG5fXpQAI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/194218a84f.mp4?token=FAArFissOi-XuLI8WmEaGqd9B-QcQBgLkTw3Orwpo9_YTEPF8SNYXECBKiMTZWeYQ8VZJKhAUBRBZ6POXncbAVJEtZlqvQnj4ihn245g9S-RFk7Zm092EhTveNyXZ9Fhp7V5_yT3C3RZYWRe0lmrLSjDWtA_YMPbnGNH9McI2S9QETLNuD1Ak6Iy-jntPR5y6lroAGuwqm6QL99IRVSAAmPgyE_fxvjnwKMQim2YiDJEO03zByC8G9qAxx80sYJXHv2t9QervjK7cGoAg2Ifcti6bS98Ao8CFQ-8TUUpZ9gG2cmclAgY64CgEZWYk-e2_TOOjt2AbrhiSkjI-ymcxD7FxY5SJ7IJz9x20FOdZtJ_gIyYhFFyjmtAVlD4urtFvcZwwYIkOIN3iPIqMmKdZvOQI3tkjgMMCqUrTPuDjxrUQ-Yd48uqFxl7M7kBzHkJnuEs0PyluahIfxLo05Svy7b8AdGNK8ypf79qTtwp1YsIS6bonfmSbGkNWSx9jl-77R0rsyIm-TrlR_-pWZy5S1rSCQ__PApb6NPHeAzKbpjDJZrSpZE04Qxo2iv2AHRv5n1A5AfW6nQbHMYFB0VPuznTt1KjlGfntOxuNQ7GR62qI9uwPhHcANFWm8nbfpIS2wcCC40mM-BX3dMFmV4pOABXppMq3XN5pbrG5fXpQAI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
آریایوسفی ستاره‌سپاهان به این شکل گل اول طلایی‌پوشان‌زاینده‌رود وارد دروازه فجر سپاسی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/31201" target="_blank">📅 19:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31200">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b6aefbc83.mp4?token=iIMRlp0q9uM9x6Jcue-fyn3NSPkZxV5dJz3h05h8TN7vA0--ZeNGUIWLkV0fWQhqMAkdW677ALdb_bBffkPCcwBPBqnF3PzKqbg1W1D2G9xjS0ASCVQJOvLJNqMjF2uGiiaJvGIoXh3jEU0HrpXGOvTRZ0dfSwmMnfIszR3x8fDR82pzErdl8goAuP7kXr4bzrhR8R4zOiQFDttZ7UDUxqsCoT-Dw1QtcyYnPiMtNmKjNT9aBn9CuV06NDkVu0SiuqQNYCTP7jS67FozmNOKxJwcc6lJbvZE4fPc8dvCUsTnCKu7bj34dhdRpjIYgBT-NjaXJ_GQF_XtssTvhZHvEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b6aefbc83.mp4?token=iIMRlp0q9uM9x6Jcue-fyn3NSPkZxV5dJz3h05h8TN7vA0--ZeNGUIWLkV0fWQhqMAkdW677ALdb_bBffkPCcwBPBqnF3PzKqbg1W1D2G9xjS0ASCVQJOvLJNqMjF2uGiiaJvGIoXh3jEU0HrpXGOvTRZ0dfSwmMnfIszR3x8fDR82pzErdl8goAuP7kXr4bzrhR8R4zOiQFDttZ7UDUxqsCoT-Dw1QtcyYnPiMtNmKjNT9aBn9CuV06NDkVu0SiuqQNYCTP7jS67FozmNOKxJwcc6lJbvZE4fPc8dvCUsTnCKu7bj34dhdRpjIYgBT-NjaXJ_GQF_XtssTvhZHvEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
سپاهان محرم نوید کیا امروز ساعت 18:45 با این ترکیب به مصاف فجرسپاسی خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/31200" target="_blank">📅 19:14 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31199">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IU6sk1KyLolydG5m-6FzRIEIFHEjIlBO6G1xqma19F0MJj7hR9RbWu-o4xUN8d5fE8z_d3MThMsfcECoBgwZr49paDQ98EQdOOKCsswLLvc0nlWGTKMsXZ0nkytnXAdl_2cXRmv_J9sSRvFcgALTdH-aiCnzxAKe0nBblBBJ0JqGiWUMBCoIVFzO7cWM_Xai3BfTq-FHUyxTRkNjVB0QOVSaLU6jjs7sPL5IlEYJFqV9at2SFNDIf2i7VBKZ8VmhUV0EAPwHaCN8myruycx2yl_ELFORM-PjPejrFjE2i5guS201qoqpiruSxHr35uAuXyGMLvj6J1kC3qDd5Ffj3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بالاخره آبی‌ها گل رو خوردند؛ گل اول تراکتور به استقلال توسط سید مهدی حسینی در دقیقه 74.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/31199" target="_blank">📅 18:57 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31198">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e1b0fadf9.mp4?token=LeUNoR7T3DGV44H7-VcJu9uKFvbLqUPbeF56ezqMm9jIIpoWFHhm8q0R8sVHoSI0us9O2VbKFsMAAHvf0XcIJ2xIMI5RIMqdG4OW9mdWUUvDUztj4zmRD52vdYkjUjRSVYc3v56k2jBYX5qsZ-nksU-bTmBvC9OqDr00guCHVIr_d52eGKZwtY1DwmHRI3dMyZlF5kOdlMngPsFqqqrTC-iKWjBDm5yH1z_5L6AezkregBtFnfix8vGNylzAoGJ6xO2v7XOhPlGLT-suPIBy_Prfc6ytY8uW9xqUICUXARGL3q2RsoT83Bydl4givdDS-1WnMLhZ_qvxG5fOIdUB6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e1b0fadf9.mp4?token=LeUNoR7T3DGV44H7-VcJu9uKFvbLqUPbeF56ezqMm9jIIpoWFHhm8q0R8sVHoSI0us9O2VbKFsMAAHvf0XcIJ2xIMI5RIMqdG4OW9mdWUUvDUztj4zmRD52vdYkjUjRSVYc3v56k2jBYX5qsZ-nksU-bTmBvC9OqDr00guCHVIr_d52eGKZwtY1DwmHRI3dMyZlF5kOdlMngPsFqqqrTC-iKWjBDm5yH1z_5L6AezkregBtFnfix8vGNylzAoGJ6xO2v7XOhPlGLT-suPIBy_Prfc6ytY8uW9xqUICUXARGL3q2RsoT83Bydl4givdDS-1WnMLhZ_qvxG5fOIdUB6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
گل اول تراکتور به استقلال توسط هلیلیوویچ در دقیقه 68 که VAR هند بازیکنان تراکتور گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/31198" target="_blank">📅 18:38 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31197">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7d03b757a.mp4?token=pY0EkqGWhyaggkEwm0Hp_9V3pSA_7YuMUQE_vo2vtIThvvQlUEbMs-_tk-2vz_i46ZXKgWDDMoo3wOqKP8IJV23TaSH5TyjcUuN6qVqwM5UwI4aIhb21ZalzBptSzRyZn-cvVVMOrswdS7yJycGF6f9BHVJQ5C6WnOr3gQ1_HvO7Vlq3Yz1eK0sJRM8QgcgjYdZI45oorU-vbEkZlPDSxGVmJa3-EHABSx9UNCg8zDZD2LSrBFIsB9QvPExCiuqgCOuzC_vW9VROq-gqt0LXgciR47Jaunn3SmBj4glXrQJF4SJmu94HLiQpKApMTC4gEDQj8k9Gxxy9Lq0t7zZCSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7d03b757a.mp4?token=pY0EkqGWhyaggkEwm0Hp_9V3pSA_7YuMUQE_vo2vtIThvvQlUEbMs-_tk-2vz_i46ZXKgWDDMoo3wOqKP8IJV23TaSH5TyjcUuN6qVqwM5UwI4aIhb21ZalzBptSzRyZn-cvVVMOrswdS7yJycGF6f9BHVJQ5C6WnOr3gQ1_HvO7Vlq3Yz1eK0sJRM8QgcgjYdZI45oorU-vbEkZlPDSxGVmJa3-EHABSx9UNCg8zDZD2LSrBFIsB9QvPExCiuqgCOuzC_vW9VROq-gqt0LXgciR47Jaunn3SmBj4glXrQJF4SJmu94HLiQpKApMTC4gEDQj8k9Gxxy9Lq0t7zZCSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
استارت‌انفجاری‌ستاره‌آبی‌ها؛ گل‌اول استقلال به تراکتور توسط سعید سحر خیزان در دقیقه 28
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/31197" target="_blank">📅 18:33 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31196">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZNC87GT1oUUNSQWWT11EBqMAd5HqXVjizYSHkAgramwoMhsdoGS-EfPcb7imB2DcKhg6Da_MoYcX678uZCeho07Nb3h1hqog3qvZxYHl6JRgHb1KmGXA7NSApZ6jk2h7hCH_28FjGLNNShRoJUfLeqD_wMUBIQVa7fP5eqjtno3XCehK0DDjeYN4v6hzWiupxSdc1il7YQVrqpCjMatqCO1ou0DKIDJfqq6oXCFkcBiIM2Rzp-IWURtRrANMpqgHA-yIBZAvPQMepSpmKVxFIs-1gyfIZ5yxal8aMunMvW-EXbFaE4sTLLpOn9t9TDOrJsBr-dZz00y2YGMHnUMztA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
سپاهان محرم نوید کیا امروز ساعت 18:45 با این ترکیب به مصاف فجرسپاسی خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/31196" target="_blank">📅 18:22 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31195">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZosRsyKC7cc2gfMaQC4qTuynfSYX6dcBgGGonZchQo8m8gB_HVOSRyzKQy7SaZaazQ8bY-X-cPpl4bfrPqt2hAEuX30nscOk3HbaXDmQ58Dy5foqBaeZ5yC-PK6yCyByZ_JtGesjK-5ZSrlHU-yzhZXKwWkTKxtCewVXAD-wxDvqeGa4XqR9NtiE6DeCqxmpgY_eKsuGL-CzwyB1LzrAYJ42jv-2HwL9BA4r_iYsnFK88U5D1dPnrXJeO43lRA8DaNugz8_5FV4gsVt0nP60_T5sG3VNyHdqCPrCPJQpXu8kZ2PrflWgy-JdnV3_WxnPh0ayzZdVK0TAf2kG30j6IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
استارت‌انفجاری‌ستاره‌آبی‌ها؛ گل‌اول استقلال به تراکتور توسط سعید سحر خیزان در دقیقه 28
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/31195" target="_blank">📅 18:12 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31193">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HJpSwghkmB1VcWcNHZSeJ6tOjwa-7tS8JwEtJXF7r_QDqnRlvrqo6HNFoFmZFJPDj0qEvyG1NrZUo0cf_xKcjm8q86_fkNMuCtjdGBJTbHpyrSV9YGpGz3Z_zso992yQ7y3RanSDeFrJ2Lv0OiOrOISu1DNYgzXYEpdOsxA5rmWtBEXm-hNGxIE-lMFyDBwSUKwl85l8UmX3E--p2blH6rza-dUyqajYWBVJBeuae8B4HC0U5nNbouC-UAxLhpvzUI9IKSuQ3Y5NL8D-4hAPY0XLM-OluNjX4YW-87mnGD4e-Ff4fMAts4hDdD-8R1zH0pJKOeK-B9T6oxTJfRb51w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/My97uiPqdd4VmhioSeXyqma1y3tyhZB2l3aMdmW2hnoNmfpUEOYgHNwxOE9Jwz7UzI8fi7Qp-Zv6hVFL5bVhvEj4y9rN43Fe_5SI4u4CuTY-bv7CPJVBmjoVQRTcuFjXHkXlHub5HarleFXsDWQ4oVIg3B9XUUIoRWAfDvbXVnef4IdW07i4qDgETm37JIZZ0R9cbP5TSYTe39eCVjYj7VEETSC5BG9Djpy02LdaB_YMcoLaYfOIbQ9Hzz2Fqy2GzrsUydsW609qRu-W0s7HLVDi-RUyMJ308HzUGaCT7i-jJNvV0mbxcDqJ55mDLK9YH7j0NFirZG2RrbvzUD0NRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
سوفی رین اینفلونسر مجازی مدعی شده که لامین یامال ستاره جوان و پدیده بارسا اشتراک 12 ماهه اونلی فنز اون رو خریداری کرده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/31193" target="_blank">📅 18:06 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31192">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b022014318.mp4?token=jPmXrALlwk5WAxQZJLOUZalfPt-kmMLOJXokjqImi1lnFCFvF5cwXP3ADMN3ZXolnJDXiaMwuzL7x0dxy-FYKd3REEHca_78JIPK558EQFNJYDnLAqksLAj5t946XShzjbrqX0KnBn4VOpRS-iQrdHAx4LoWihwNoUARimW0TN0NCsvGJ9qd6wQ0sChLXZ2Jjgsp5dI1UV7X7gjGEJiMX8aPfAT5DNyastGhEru8G8o2t4DUntyTlvah4W1Zh1wCimXQG0W00qRTWXCBdKolZBI3k9MOTf9YkgIjAfqfk9p8jSphJbJzMc_ogVjn1mLQd1Mv8sSKyGzwXv2d4fEPXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b022014318.mp4?token=jPmXrALlwk5WAxQZJLOUZalfPt-kmMLOJXokjqImi1lnFCFvF5cwXP3ADMN3ZXolnJDXiaMwuzL7x0dxy-FYKd3REEHca_78JIPK558EQFNJYDnLAqksLAj5t946XShzjbrqX0KnBn4VOpRS-iQrdHAx4LoWihwNoUARimW0TN0NCsvGJ9qd6wQ0sChLXZ2Jjgsp5dI1UV7X7gjGEJiMX8aPfAT5DNyastGhEru8G8o2t4DUntyTlvah4W1Zh1wCimXQG0W00qRTWXCBdKolZBI3k9MOTf9YkgIjAfqfk9p8jSphJbJzMc_ogVjn1mLQd1Mv8sSKyGzwXv2d4fEPXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
گلزنی‌سامان‌قدوس‌ستاره33ساله الاتحاد کلبا دربازی‌امروز این تیم مقابل خورفکان در لیگ امارات؛ در پیش فصل باشگاه پرسپولیس خیلی تلاش کرد که قدوس رو به این‌تیم‌بیاره اما مخالفت همسر او باعث شد که این انتقال انجام نشود. همانند مخالف همسر مونیر الحدادی برای بازگشت…</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/31192" target="_blank">📅 17:55 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31191">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tdm6Gbssg0ibHmcmeA2zvfcR4RZCzxJkIkz7xtsxw6vNl4132HCwQooiJCGXSn1xnsXUoFiZyrDdTmi8jLz9Z-NjippwYH2pdMWF65QVonS6-N0HMgFOlNA1u4Z2QkC4Ztdb4Yrsg48YkpwqR3RN9T2P2yrzbV802KbQuVbk0RnF-xhfQGzLLQKUzyKgXbFnHT7MweBC1c8V0z5txNk5ybRw1mOtUQ8gLm3oc6k4qarFuOS1dr8dJebSdr7uP1FNAzGgwuJHPUnTAIEGjyLKgWQhVOMX57yj6UZOvT8SQzImKpOPZgcbgURzuCW663R-T-qO6car2ophP-NhXWk5Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
باخداحافظی پدرو از دنیای‌فوتبال؛ از ترکیب استثنایی بارسلونا در فصل 2011 تنها لیونل مسی باقی مونده و همه خداحافظی کرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/31191" target="_blank">📅 17:47 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31190">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5be0608b6a.mp4?token=qXE5ftwHl6w51IgI89rqGXyyfKZrEuZgIw8twgTzkIr6FcIvumy6LIgBU5d-17sgV0LFHsrOJ3iz9kUxqB7cj8-VgsZ3HMgE78VtW3yd70I_RlNLRP32vVLZVWoOXDZPXqOHrGkF30bGeGNqulzwR0yijhwOqBshU7jdudqFuGMUlP4-hr7_ex2F5DSu-XeLgbJX2AtbMc9C1GPr8nYOz-zfv-XTSB0DMV4yeUaxWaeBHhwWX2UM9q2h-DUfj9D9MC4KbAJhIgYX7JpxGjHccDKHxsKwqQQWejD9zvq_nFsFH-UOCdNOo_RtBig6DYO93q9-wsy6wcOBY8RRRraw0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5be0608b6a.mp4?token=qXE5ftwHl6w51IgI89rqGXyyfKZrEuZgIw8twgTzkIr6FcIvumy6LIgBU5d-17sgV0LFHsrOJ3iz9kUxqB7cj8-VgsZ3HMgE78VtW3yd70I_RlNLRP32vVLZVWoOXDZPXqOHrGkF30bGeGNqulzwR0yijhwOqBshU7jdudqFuGMUlP4-hr7_ex2F5DSu-XeLgbJX2AtbMc9C1GPr8nYOz-zfv-XTSB0DMV4yeUaxWaeBHhwWX2UM9q2h-DUfj9D9MC4KbAJhIgYX7JpxGjHccDKHxsKwqQQWejD9zvq_nFsFH-UOCdNOo_RtBig6DYO93q9-wsy6wcOBY8RRRraw0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
شماتیک‌ترکیب‌تیم استقلال برای دیدار امروز مقابل تراکتور در هفته هشتم رقابت‌های لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/31190" target="_blank">📅 17:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31189">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04026264da.mp4?token=pXQSAHUFwleYw9q6nsaqiHaEi9UpQbVqaUbLC4eNlUhfIKVGY0JRpDrgdMUNAjFVSRcIPv1OEgCOgbLCx4Wks868RrYpF5cBACFQM-S6Ey1hA3LM1BUnLaCOLZTLr8P_iuBzGWfdT4O91GJQjcG5eusqVMaODzog76Xw0fBgV5B0tUOFwJ23nzk-r_RtBa3s_r-E7P87insrIK9vNm1OFJNdUwPMSmcLOwPhVIb_LsH0Yhc0iSsT_6Umm6nZNQKOjy_Dk1TJUw2Ji4lbuIuLMqvnMtc9NHfmMCpBWHODQHvCVdtMvlKPvr5okJLkz5kM8edV-CR5yf2mm4J5Yuvtgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04026264da.mp4?token=pXQSAHUFwleYw9q6nsaqiHaEi9UpQbVqaUbLC4eNlUhfIKVGY0JRpDrgdMUNAjFVSRcIPv1OEgCOgbLCx4Wks868RrYpF5cBACFQM-S6Ey1hA3LM1BUnLaCOLZTLr8P_iuBzGWfdT4O91GJQjcG5eusqVMaODzog76Xw0fBgV5B0tUOFwJ23nzk-r_RtBa3s_r-E7P87insrIK9vNm1OFJNdUwPMSmcLOwPhVIb_LsH0Yhc0iSsT_6Umm6nZNQKOjy_Dk1TJUw2Ji4lbuIuLMqvnMtc9NHfmMCpBWHODQHvCVdtMvlKPvr5okJLkz5kM8edV-CR5yf2mm4J5Yuvtgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درحالیکه هفته‌اخیر سارقان تو اتوبان همت تهران تلفن همراه‌آیفون17پرومکس پیمان حدادی مدیرعامل پرسپولیس رو زده بودند. امروز همین اتفاق تو اتوبان تهران - کرج برای مهدی تارتار سرمربی سرخ‌ها اتفاق افتاد و گوشی جدید آیفون 18 پرومکس او مورد سرقت قرار گرفت. خداروشکر…</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/31189" target="_blank">📅 16:40 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31188">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R8c2TFLg8OYprYoNT0aRzS3KqvTD_8slEe0ynzPJuwizV2qLZ9cbjjkM7De6kKmidd4Y6LUR-0CDoAmwCIq5c0qvjrEpRXM8YsBSZYArJZsU_x43piRoDiX9pNwV3NKAtegU0yCKfpYE24zd5jcHQBSnIJ6zyKKOFUZSd4kCrT0-14SqjB2RicpwcmNd90lzfHOU_7HsKHXZoiQiO1ts3XVq1F0U-L-Dj12yqBLm3MJ0wmvBS_8VyBxw6uYDNn9074-B4Cn4eL0999TWkfH6qQzSQud0JTyRR08URV7KA0t7WTgCJuJGrTwiQcyWVHAWTEDNzHQxGVfdq6IF8PmWmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پرونده‌پشم‌ریزون‌وجنجالی‌فوتبال در دیواندره؛
دو مربی به اسم‌میثم و ادیب 5 سال توی تیم فوتبال ستارگان دیواندره‌بودن‌که توی این پنج سال به بیشتر از 50 کودک تجاوز کردند! به کودک ها وعده میدادن که اگه باهامون رابطه جنسی برقرار کنی توی ترکیب اصلی میزاریمت و میفرستیمت تیم های خفن تهران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/31188" target="_blank">📅 16:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31187">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XJgyYkf-YtnjUWVop9ew1ha-_hpq3UA-s1HckCOosQI4O24fqIYPXDnfY-SOnr_YWXa-UIFL6FTHshIGz-V7fO0YDz157aXmY1v80cksbOuFvYnSqMa7tN8PXLwGVT5eYxHuApxVoAGeiccJs6LgeU45Wr6WTHnw88uwlP8cJGWfUZtWYRLw5MxYkL1G0RFANjNs-yEo8eReoMZ0gSbaucUCWR44zleGiuVKz68Hnvr8-3a6Zw4AeqvEG9seGNtuVIPuTPF6g8k5qiDrurcKYFMullybTjdVSAF0GgFhnuqU73EUXNjnr8yEcuDlN03YXU01FjrTfFbSjmhnwMugCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هشتم‌لیگ‌برتر؛ شماتیک‌ترکیب‌استقلال برای دیدار حساس امروز مقابل تراکتور؛ ساعت 17:00
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/31187" target="_blank">📅 16:14 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31186">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HdnC3Eao8hgXGiiiU8YootA8vLooCtLGizvVHOh6A1vTYSIPY2uEifMmMPe5Pg2bRSexedIJS92LxM0bHdqe23Yx1hwA9A24pf3HnXcHyMLR6HSkZVpc3n58_XUGzYjhfjwgAu0qcBBY7pm5hHtLoaL8c6xu4i1cV1g15mkLG7T0yDuQF0e-icmfNaaaLXbQSyPvtAQbdkL4sWocNp9KB7sKuGnok2QdVxUKEZh5zZxf_Xkjsv8q8gYIJU8MWXGnVTngQtMHzZVded5x6ZKpl64kPuGqaR1Hg0tVC8EfyZZ3dqY1AejCrfUG16ckKLmaGq8um0G_7MfPFqfUxIDtqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هشتم‌لیگ‌برتر؛ شماتیک‌ترکیب تراکتور برای دیدار حساس امروز مقابل استقلال؛ ساعت 17:00
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/31186" target="_blank">📅 16:00 · 16 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
