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
<img src="https://cdn1.telesco.pe/file/BrFXbyAg4B8ERgl1ujzllUqyV6wCmmY3zyncgOOFVy79VgnAFkTrbksY_YrmGZHloyguGYC9tpYZxVo-jwL8worF6hTRB7PhLnW35PrBB0CVJBMY4Fgx7sS0ok25YR8p8-5QJh_y38WEqAxnjI0E0JPbDRQf_uZMsLOgax4SBVbGqFj1qXxWszX1-GBKdF2v6F0HGX-e22OH0iO0DNeyLBnQBKp1oSacxM7nYQLTcRbv3ryf_j_vDD8sONuOGC-u5HF3VKxDwUwSY_6sPYZ4ccj40P-aq0HA6FDvmKjRBujRezFADsuuPWezyxm-s5-DyFeOllH3rHgXDSROQHX0vQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 97.1K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-23 07:03:48</div>
<hr>

<div class="tg-post" id="msg-2554">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اینترنت ایران باید به لیست شکنجه‌های تاریخ بشر اضافه بشه ...
©
thepanue
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/ircfspace/2554" target="_blank">📅 16:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2553">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7887a97904.mp4?token=c2yITlDjnxqydzfVg2ORCqp-U4ER0DJRwyKS44k9jUGPQpjjkvmiHHQfYJCLUd-my_9ugHoUJHWE6zAZnwIEWxm2ZH1R3HaQTJFjBopTSLpY8UJ9C9KlrmXOmD0TWD_xtCzRUmFa6qtY14EyK6s_OrFFEm8cb4GY6-t1cHr9N08aUhrAZAYdGKXzbtx0CuciBW1LX4ouakTTcX8SMNPrAlupjMnBPXHk861euee8l5AOErgTMhczb_SEdZwzGuYgGVM8v07spn3Rut67RjhT7GOgC30Wc4euhmZpCsvy5A-8zO70YewM5u18ZBn4wE1pnKyLfwTroQi2vJR6MECoXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7887a97904.mp4?token=c2yITlDjnxqydzfVg2ORCqp-U4ER0DJRwyKS44k9jUGPQpjjkvmiHHQfYJCLUd-my_9ugHoUJHWE6zAZnwIEWxm2ZH1R3HaQTJFjBopTSLpY8UJ9C9KlrmXOmD0TWD_xtCzRUmFa6qtY14EyK6s_OrFFEm8cb4GY6-t1cHr9N08aUhrAZAYdGKXzbtx0CuciBW1LX4ouakTTcX8SMNPrAlupjMnBPXHk861euee8l5AOErgTMhczb_SEdZwzGuYgGVM8v07spn3Rut67RjhT7GOgC30Wc4euhmZpCsvy5A-8zO70YewM5u18ZBn4wE1pnKyLfwTroQi2vJR6MECoXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینو ممد ساخته. یکی از محمدها، که نمیشناسمش و قرار نیست بدونیم کدوم یکیشونه؛ ولی باهاش کلی خندیدم
😂
©
Mohammad
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/ircfspace/2553" target="_blank">📅 10:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2551">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l_lu1L1Zb1oVSEditV89R0X-uL5JrQN3_jFoTU0ZLJNJvOSn9hpSOYpcrF1Dg0qT8yLqTsjE9FWHxmBH9EAwvpqVaf56BzBbrZdR51M6-zDMJX6SKC8nw5zbz4dJsaFyb0A3nbOeyeH1uKqZFUJdeQfYR6wi9EPkXeUkjZdQqy8FZhBo9mXd63hEBjM6Q86sasFkehex1J672pJXVgxT9EXFXYV2qQZr8MvsRPZMaZKChcN4XTjqYjNpm4-VySLuc8nH7xTwJIGaf5ZO4uydYFMabiQ_Q9qZDuiItm5u-_nvI2rd7RHmkDkIMeRE3hYEUBmkm4H_jTvXMXse6RUqig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکثر آنتی‌ویروس‌ها (از درپیت تا لاکچری) سایت بانک ملی رو فلگ کردن، چون سرتیفیکیتش منقضی شده!
©
Teeegra
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/ircfspace/2551" target="_blank">📅 10:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2550">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TpHyqOiGzAtMeI0hb0S4bICJ-652I4AYAyRaW6_QhfWYaic9y93__EteamHI47JsicOhe8oGSUYDdBTEGdU9NhvXDa5_i9eyvQwCw9e7hQWVRRYncti898AVx8teVseH-3ol14Xc2R5Ije39yBwcRcCtGx79dke2myxFR8TMnxTBohjfE7lPsu61tnsrE2dv_yz6ZVbzcn3KYBlE_rN69fwY7T3t5ifmwRKVlnlbcBYWCe8jyjY62MpOlcoeJgVL-3X2wqZ4DAI96SeCegZN30_mCVT3WmplXT-8nEsURqxMLnsnZjoV6H9PKZ02kKOBCCKAKgxfPdTCNBgHRDr8oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون ارتباطات مخابرات گفته دستورالعمل جدیدی برای محدودیت VPN روی اینترنت ثابت ابلاغ نشده و ممکنه از مشکلات فنی شبکه یا نحوه عملکرد خود فیلترشکن‌ها باشه!
🤡
در رابطه با اینکه اختلال‌های اینترنت وضعیتی فاجعه‌بار دارن که جای صحبت نیست؛ فقط اگر بدون دستورالعمل دارن گند میزنن، یعنی دیگه خیلی کاسه داغ‌تر از آشن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/ircfspace/2550" target="_blank">📅 09:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2549">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sIC5uKJjuMROBNC8zZt_iL4_hnP8muRrwkjCx7Dj7AwTnwNNIVZtQIrywFwERaV3B6xt5QNqwhpVmSwJB9fWHIMqsuCTKjV6h8k4A6jstKZPFQ-EteeklU_EvXUdTZXQDr-2i64CUe3c5n6zUnqpm6DDDn-6UfVH-2omRIbrMpIBleoI8iKfc-qotDM1_6D8DkdjO_xivGoPngkb-mlrcQOTQCMdRWK_EpzXn92OGjJQRyqMOAayg6HNQOZrRExaGhot-yhAvae1EQLhGgBcS9lALzqRRHeM1ELiapLe9-00oq7ljKB0JKmF5PGVOsbxTuPkXUJoY1UG_qUaMj5rIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از فیلتر شدن فوتبال ۳۶۰ و دستور رئیس‌جمهور برای پیگیری مشکل چقدر گذشته؟
هنوز نه رفع فیلتر شده، نه کسی فیلترشدنش رو گردن گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/ircfspace/2549" target="_blank">📅 09:47 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2548">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nGdDzoV1UU1OuCGd8Wn07w4UNK44DBCPkGgYu8v5K4lNwI1kpOl-k-l7-eLIdEk7YnTpEL08_eVn6D1vb2BiOnJ7aDYLRCZ5qe6KX7sZCw5MZDeDquXSlzmet2mMbMcLq-Gya4m_44t7V27Cw1-nQSTdcRv8X0ow0lwAMogspbsK4FP_YzwrXCgI3gG5D68mTnaYKrQWlyIdiOqftW2FSsweTnHf5Q4UKbCbl2263UlBpaX-T7QQsAEKLAJ2WuZP0WEe1RNNYFTSyssnlmXXMGAON3rEEjJV4sEwuS2zlGoWYl6LQJf-ga92OoCQYsKRsMJGYO-kRY1zMaR3x2vCmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلتفرم لندین که برای ساخت لندینگ‌پیج بود، بدون اخطار قبلی فیلتر شد. بعد از یک‌روز که با تعهد در دادستانی رفع فیلترش کردن، اعلام شده دلیلش فروش آمپول لاغری در صفحه یک کلینیک زیبایی بوده!
یعنی هنوز که هنوزه نفهمیدن فیلتر کردن یه کسب و کار چه آسیب‌هایی داره. هنوز که هنوزه نفهمیدن وقتی یک صفحه محتوای خلاف قوانین داره، کل کسب و کار نباید فیلتر بشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/ircfspace/2548" target="_blank">📅 09:45 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2547">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RL2mkQIkP3ksxHg15r9Ri7AETfsUP-xrPCuWofVCMGryIzf4sAZUg69QydwfsFA8_8YTb0umCnoBLtp0S3LsFsJhS72jNHDeWtczydzXLdVWU1hdSyf_ToXqtpiYTNcGNyqzsFrAstPWW2oLR0K17ZlemqsIM6Nx8-8h-qPTCSZyNBKjcWaiDqW7U5SCmaCInoO_PLh-fTRoA7-r_4BUC4YjL5WvPCUrsvmmVORaaj1Av2CIZi14OTsh6VhpiVISAvvBzvTIspu9Kn8Oadk-LFjsAn4_b0OGZN0c1sA61hsU15mrRXAXbALILHGIQbwqgsrFOUkkCFjNHN1XCvHZxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با قطع سراسری اینترنت و نابودی هزاران شغل، هزار میلیارد تومان به پیامرسان‌های رانتی کمک کرده بودن! همون پیامرسان‌ها در عین دریافت پول بیت‌المال، اختلال داشتن، ثبت‌نام جدید نمی‌گرفتن، محدودیت‌های تازه گذاشته بودن و چشم‌وچار مارو با تبلیغات کور میکردن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/ircfspace/2547" target="_blank">📅 09:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2546">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fOrccWvupMY2PLzGGLg73GxT4eaII2aVO7J9x_mXN3YPMxcCtJvUtzfxDNO9fyXKyYjf0qoTp3D5s9pxQa5MVQgtBbI_fYfjzkxL4ZgZizl-W-ZIfoQApg5uyHgU1Al-bNUHK2cYBKh2uVsXVTGZgHHE9iLsId-gk5FtQb7o7OVXYvPr1WHmf_UseY0f5ZdqtiXoDW9V16s0gvIj6i9L1Wuq3we-Z3X5GTrX8zG3H35jZQHs1u4Z_J-K3XUAmp74cx4Gnfthhiy-ROqDoIgKTvqwNgG2aplM73TZG82Nk_jGnQll1raSaF3WKcuUVcJHa2YfYXRcDpkt2e8BRQQTjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه عده‌ای از عناصر فرصت‌طلب سودجو عنوان می‌کنن اینترنت قوی و زیبای ما گران شده است. برای شفاف سازی میگم بسته‌ای که شش ماه پیش خریدم 1,348,000 تومان، الان شده 3,870,000 تومان. قیمت فقط ۳ برابر شده، گران نشده.
بنده هم با ارائه سند میگم اینترنت گران نشده، فقط ۳ برابر شده!
©
mrweb24
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/ircfspace/2546" target="_blank">📅 19:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2545">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gBPq846nOPStcKx_acopWL4hIXADoCef7_gBPOmO_48PHa8WkymbL9Efb8koVq02nXqe-r7EKeobWpy6Iv8Uf-eUsMIZKbbDHReLgRm06TC9jExgKIU497obhCB2aSuGZe9MNLPnjpW6axjlj9lzpLdTqBTNoIAwo7BZdThZ4_bQZDcgFyahD-MxZOH7bskNMlwXK-dfMxuAGRZMGIocqpEEqSRDhMEejUMypUMq4zqssN7_wAsTK7--xK6a5tO-K7l810pmQ72__DnWsoU0PC58vFxu07YxVT2P9cjzw7S0mGAu9tGhi51wGNIy04dS3DZedbEoCIxJxPmrsj-VQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگین چرا با وجود اینکه چند روزه اختلال‌ها و کندی اینترنت شدیدتر از همیشه هست، چیزی نگفتی. خب الان گفتم؛ کدوم احمقی قراره حلش کنه؟ همونو بهم نشون بده!
ده‌ها پیام داشتم که نگران بودن چرا چند روزه نیستم. غرق در گرفتاریام و گاهی حتی آب از سرم رد میشه، ولی دوباره برمیگردم سطح. نگران نباشین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/ircfspace/2545" target="_blank">📅 10:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2544">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jrzFYVCQVMXnCkJZWubIqMmAaEML9-yVAgr7p1hOz_Rd6PQZjJAJ65fmy5OeaCR7meqiBD5sMJuKU1T7q03pxsLwwqZe85uR-U__kyZ7vtfmmq6H4ycHRg8xJneJv1Bp9E_1Y86Ya4Kyi2AomryqAPH9nLanMKhmSrcDPotzOmNS4pRcFYt2gA0xcI6Y2_lLhk0uvdHEmqIjEHSI3INQMizpMBN_NpU3nYBts63zFe9sXVE-r9Ce0Uwtb7rQ2qkxoe8U9RJ1F82Pp-fAsY-7zROuIglMLcIwxpGWpb4t0pBG0o5q5b8Sr4NXSp8sfrfnjrFTTFMYbEFCqF0CjQkvjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر لو رفته از وزیر قطع‌ارتباطات هنگام رونمایی از طرح تشویقی "نسبت حجم ترافیک بین‌الملل به حجم ترافیک داخلی"
😄
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/ircfspace/2544" target="_blank">📅 11:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2543">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">این قضیه اینترنت نیم‌بها و ترافیک تشویقی برای استفاده از سایت‌ها و سرویس‌های داخلی واقعا داستان جالبیه. فقط ایرادش اونجاست که کاری می‌کنن تا سایت‌های داخلی روی ملانت باز نشن، یا به حدی کند باشن که بازم فیلترشکنت رو روشن کنی!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/ircfspace/2543" target="_blank">📅 10:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2542">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">چند پورت مهم مانند پورت ٢٢ از سمت زیرساخت بر روی آیپی‌های ایران به سمت شبکه بین‌الملل محدود شده است.
همچنین شواهد و بررسی‌ها نشان می‌دهند که ارتباطات زیرساخت برای ایجاد یک قطعی گسترده در حالت آماده‌باش می‌باشد.
©
manageit
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/ircfspace/2542" target="_blank">📅 10:28 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2541">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u6TcbjIaiHUB9ybVTXZ-QvI8-e14vPcyo6bNAbJuRu7nj7uzvx3kkrnCOkbDSv_IbF24R3h-xDLqEc56IYwA67ryX_J2saZ5CQmMqDOLCsye2BL8ju1Gv4DBck1ygaIRKYGwZXJ7IsweKOIUyUWZRcLhPUBDz3pF7zXk2B87-Fy02Irf5d-vgjRLMwMGFhwTCZtPNe26yIU2KVbje56S-So6CXtWBcyo0UYS_K7S7Xah8q4IhcV7u60fey_hOHPri0zy5R5EWIWqVR8rAIaaX69svdh6bqoDOjar8kP_E5zuKf-yxEAer4Z_gA92ZMBgS7-41GqPWP0KJhwlnY8iow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باورم نمیشد که بعد از ۸۸ روز قطع سراسری اینترنت به جای اینکه بیرون بندازنشون، به نمایندگان حکومت تریبون دادن که در اجلاس جهانی اینترنت سخنرانی کنن؛ بعد دیدم این اجلاس در چین برگزار شده!
روابط عمومی وزارت قطع‌ارتباطات گفته نمایندگان جمهوری اسلامی در پنل‌های تخصصی اجلاس جهانی اینترنت که دیروز برگزار شد، مجموعه‌ای از پیشنهادهای راهبردی برای توسعه همکاری‌های جهانی در حوزه‌های اقتصاد دیجیتال، هوش مصنوعی، امنیت سایبری، خدمات ابری و تاب‌آوری زیرساخت‌های ارتباطی ارائه کردن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/ircfspace/2541" target="_blank">📅 17:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2540">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">چرا کسی از این موضوع که "سیمکارتایی که استفاده نمیکنی رو واگذار میکنن، در حالی که طرف با اون خط اکانت تلگرام داره و چتاشو شخص جدید میتونه بخونه" چیزی نمیگه؟
©
shara77miaa
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/ircfspace/2540" target="_blank">📅 17:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2539">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pFncz-0ejAZSdxe3frufBbLgMZnXZxVQVg3eHv7XLTBCNKpyu9-ts6g390ptqXcJZ6cvCf3ncTGML7X4u9Xn4GbQpbO7gRyJTQry6YUuJin3qv06-hbFmMbcYfN7jHVCQMWhkOseVTQSa6lV0OFkxKH7XbRG18OgU8dyYiBRhcWrIskoZXiJhrDucyJ8Hi_0SBN5So4K5Pt99YncOzFxXhb_Ua0xTF18uGmzOgYUXJlJWrpA3EXs7mF3N6W4b_z94nRtrj-m4u9gtJWH6tHrBjp29Tvb89oKxtQtJa-cyhPcHw5_lQSl1naxATWcbqXr34F8j1y2W9irz1ERyXgHEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدیدترین داده‌های مرکز آمار ایران نشون میده در بهار امسال ۶۳۰ هزار شغل صنعتی از بین رفته و سهم صنعت از اشتغال به ۳۱ درصد کاهش پیدا کرده.
حالا این آمار رسمی مربوط به مشاغل صنعتیه، ولی فکر می‌کنین آمار خسارتی که بعد از قطع ۸۸ روزه اینترنت به درآمد و مشاغل اینترنتی وارد شد چقدر بوده؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/ircfspace/2539" target="_blank">📅 17:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2538">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b1nkEUMS_H1JC7dbGiXdNc-G1dpoZjb_-bth158maugNfT4MCiTCzAfPvxvduBPG6COTOZi8At0i6PXAVYfw0wuPxyQeZXCSys2in1pFynVZ86TatIFBkv0Y3ih9Mo5XBjNiDBr4j97Ri9USN3D98a2JKlma0z_Z2gGd3bZdCRalH8bwEWIVUhvgYkjphEtze8qoG43KVaw9Dx4uN7XqtVMXYZetpVeVrXEsomzRUimR9p1QcXgh6pfTYsnti89kf-Ja78uZmEr0XebqnPmqZ0iSSZJ6X3_bEI7LxAxV-AU0DkVmXqNEDJNXuOMa-65Jv0Up1D7I5fCOHLfJA3Sp0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چه کسی و با چه مجوزی تصمیم گرفت ضریب بسته‌های اینترنت بین‌الملل رو بدون اطلاع‌رسانی تغییر بده؟
قبلاً ۵ گیگ اینترنت میخریدیم = ۱۰ گیگ داخلی بود! و فقط پول ۵ گیگ رو میدادیم. الان پول ۱۰ گیگ رو می‌گیرن!!! فقط نصف اینترنت بین‌الملل میتونی استفاده کنی! بی سر و صدا دزدی میکنن با عوض کردن مدل درامدی!
غرامت قطعی‌های ماه‌ها اینترنت هم هنوز پرداخت نشده. این دزدی سازمان‌یافته‌ست که با حمایت وزارت پست و تلگراف اجرایی شده !
©
iSegar0
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/ircfspace/2538" target="_blank">📅 17:12 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2537">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FqKbXKfgXOOzkTrM3iokxR0dP_XIp2YHT89H14gpAm-iGhOw0_2HCJ6rfJs5Q-fJUCWvTqOc2ePby-N6W0eNHitoMlp1T5mhJzkEJbUydrRLmRBjQORdL5cA1E7tt6sNeZCjIGpXbAnCwkqnqbfSbCVL1XwGEUeMbnN9Xg0uAz8wNzv4jEXLHTIeiZv1b_FfWw6TAmuQUicxwlgWezKWpUHrYhjeULaGlC8DuwDTTkgWX7HFJiRBS_MRkLF3Sdpo7BEKkosl3N8b37FrYSCM-2NwFIKymPySqZdtOK2-s70KfD2IiJkAPvMy7SKD7wZZb6SZEdk3x4f1Oi4KHdPMlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Aerial یه رادیوی متن‌باز و رایگان برای اندروید هست، که باهاش می‌تونین بدون نیاز به ثبت‌نام یا استفاده از فیلترشکن، به ایستگاه‌های رادیویی مختلف گوش کنین.
👉
github.com/shapeshed/aerial/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/ircfspace/2537" target="_blank">📅 20:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2536">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VPGe0XOcue-Lt7uNvt55QUcWzb27vxVJ4wxJS76AlTzL_9R39K60-WxxbwVDNNkYsR-SpNhUzeDjYsyqy1EFXWFsVQ4OWTVuGlNNnRH3ilZtn609XBq-KedGmjErhJLHHJ-BnIs2O5-35kVDTLhUyEMUmLT72_1tT3jfyQyYKO446Tu3UqtQpatpPX5tyyBUqi6I5cilExLzzDzysL9C1wDDe_Mud4ywax2XBioelO96XpLfnAneOdqchVNikvPKHei8lomU-AVQpUHZADc8b-EcPQszs9SrCM1-EABe1UpwGoQmbXwF39nsLVCcDEUJK0UyfV0OkY_vrpOUofB9OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سری برنامه مثل GlassWire، NetWorx، TrafficMonitor، DU Meter، DataMan و ... برای اندروید، آیفون، ویندوز، لینوکس و مک هست که باهاشون می‌تونین مصرف اینترنت خودتون رو بصورت روزانه، هفتگی و ماهانه مانیتور کنین.
چرا میگم؟ چون صرفاً مصرف اینترنت شما اون چیزی نیست که خودتون دانلود می‌کنین و ممکنه خیلی از برنامه‌ها در پس‌زمینه مشغول رد و بدل کردن دیتا باشن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/ircfspace/2536" target="_blank">📅 20:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2535">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Olu7_tzF5fkiIym5Hxusoe6CfcykuByZE7PNeWxglJliCE3gPGspt7cwjxtss9bC9z7qMLTkoMC_hku2ZurFkOM_M3Q9tcUg6UGBznGb-3GFwOj5Hna4mdKiq4uRkmmA_1ddh0heVWfbVMC6jOfyYl8OrZiixmaho2UGruI66JXCLFWN7iHgDjBrS9toLcveltMX4EQvb5pldwq7XArL03gvs3Kombukt5azQgpjqciuE7lXI8Tisd05nXDBEEdP_1U-MH8uIYNQZyNt7gH4lUM7UYsUhNA9nRiGkzyjQumNkiFp403OoZJJVShHYO614w9DQdhNevUgCHp6oP1sfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از راه‌ها مخفی‌کردن صورت مسئله، اینه که چندهفته پیام خطا نمایش بدی!
©
AmirMahdi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/ircfspace/2535" target="_blank">📅 20:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2534">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XjHolDs5lQwJLl83ct6RK-vjhER4cJl7T_kvUXpItifV2nDLeW82gO00WCHhgj--4Cmsa88r-jVfMugko_dRfPxIAXfU3c2zdO7xjijoFjgfsNVoDmnRISX5Of7oCFyPASeoxDtq_nVruTVvKOATGYjoVD4XgSksvbl0Ylvh0Xs832tGO8yAE45eOKykQokHxCbrXJ8Q7nqFHDHY1KeRj2pEdn2cQ30kdXPQQBEVagajt6DUiWnyailaXRswNcmOO5od5u4phe9GGL7aXfIYLy28b01WMcMl7fKWzcLGgRUZ4wTa6RiRlRXS2PaCZreKTv1qqli5D4vBfU2ocV83gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر میرسه این تصویر وضعیت رو برای بسته ۹۶۰۰ گیگابایت شفاف‌تر میکنه. در توضیحش نوشتن برای این بسته ضریب ۲ واسه اینترنت بین‌الملل لحاظ شده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/ircfspace/2534" target="_blank">📅 20:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2533">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Dw2mgPCOEW3h3wbgCm4XNYyQOc3mOtuCuiua5XHWBP37MdHtqSxo16Z2wf_FLi6vj3PGiwHRrD8VHzDExNg_TnvLmXriq3pjnEJZGofZyXFEqWGbn_kC1HlImXBZS-3fcEfnMiljQ9Zg68UVG7mdcjmLNYnCSSsgYtA90yii90WNT2cMSMYbBt7zIy17Uni8fantzNjBcylK9BRqvb0euOUcvGhkYJQ56ry-ZuCRyijcV05H_bAncU7KX8Nr4eqfJmpeeG5Hl6cELFRIzFBDvYhxmAZsnzoLUksq-yDUlj3rtoGymrW5ml0r7cL4XWRUhZib35W6YSIkPRm8NUNOTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جهت کنجکاوی در مورد موضوع ضریب جدید روی اینترنت بین‌الملل، ۱ گیگ دانلود کردم و توی پنل دیدم ۲ گیگ محاسبه شده!
©
Farshad
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/ircfspace/2533" target="_blank">📅 19:53 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2532">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ضریب اعمالی به اینصورته که شما اگر ۲۷۰ گیگ اینترنت داخلی دانلود کنید، ۱۰۰ گیگ حجم از بسته بین المللتون کم میشه.
این کار کلاهبرداری خواهد بود، اگر حداقل یکی از حالت‌های زیر اتفاق بیفته:
۱. اپراتور موقع فروش به شما حجم ترافیک داخلی رو نمایش بده.
۲. این اتفاق برعکس بیفته، یعنی شما وقتی ۳۷ گیگ دانلود کنی، از حجمت ۱۰۰ گیگ کم بشه.
ولی هیچ کدوم از این دوتا اتفاق نمی‌افته.
متن دقیقش اینه: هر گیگابایت ترافیک بین‌الملل معادل ۲.۷ گیگابایت، ترافیک داخلی است. به عنوان مثال سرویس دارای ۱۰۰ گیگابایت ترافیک بین‌الملل، معادل ۲۷۰ گیگابایت ترافیک داخلی است.
مساله اصلی اینه که
این تصویر
و وایرال شدن این قضیه، شاید بیشتر بخاطر ویو گرفتن بوده نه انتقاد یا اعتراض. ما میدونیم که انتقاد اصلی، انتقاد به گران‌تر شدن و بی کیفیت‌تر شدن اینترنته؛ و همیشه هم این اعتراض رو داریم و در موردش بحث کردیم. اما انتشار این خبر که مبنای درستی نداره، صرفا قدرت تکذیب اپراتورها رو در مورد مسائل مهمتر بیشتر میکنه.
باید اضافه کنم این ضریب ۲.۷ اینترنت داخل،
در آینده میتونه بهونه‌ای باشه تا بی‌کیفیتی سرویس رو توجیه کنن! ا
ما فعلا در قالب یک هدیه، کادو پیچ شده و به ما تحویل دادنش.
©
Taha
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/ircfspace/2532" target="_blank">📅 19:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2531">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">نسبت حجم ترافیک بین‌الملل به حجم ترافیک داخلی ۱ به ۲.۷ هست؛ یعنی اگر ۱ گیگ خریداری کرده باشین می‌تونین برای استفاده از سایت‌های داخلی به میزان ۲.۷ گیگ مصرف کنین.
اما چیزی که کاربران میگن دقیقا برعکس همینه و جالبه!
چند نمونه از پیام‌ها:
- اپراتورها درحال شعبده‌بازی هستن
- ایرانسل و همراه اول ضریب دارن، اما هنوز از رایتل ندیدم
- من مصرفم در یکماه طبق آماری که خودم دارم حدود ۵۰ گیگ بود، ولی ۲۵۰ گیگ رفت توی پاچه‌م
- بسته‌های اینترنت با سرعت چند برابر تموم میشن
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/ircfspace/2531" target="_blank">📅 19:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2530">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">پیام‌های زیادی در این چندروز داشتم که میگفتن اپراتورها ضریب جدیدی لحاظ کردن و مصرف اینترنت بین‌الملل رو چندبرابر محاسبه می‌کنن.
یکی از پیام‌ها اینه که "امروز با پشتیبانی آسیاتک تماس گرفته بودم بابت اینکه یک فایل ۵۰ گیگابایتی دانلود کردم و اونا بیشتر از ۱۰۰ گیگ از حجم اصلی من کم کردن. پشتیبانی بهم گفت که اینترنت بین‌الملل با ضریب حساب میشه و همه اپراتورها این مصوبه براشون اومده".
توی خبرهای رسمی چنین چیزی ندیدم، ولی اگر اطلاعات دقیقی دارین می‌تونین برام بفرستین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/ircfspace/2530" target="_blank">📅 19:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2529">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/stoxCIxu5K_EziB2dc5gr0GGbwyiC4z6x9X3-T908kV-RrjdX6P8X9NXp-W464rr7opFjj15rRTF3me-hzZmmcvhBVUVOYvc-XijgsgtLlZoDisxOWifOez8P1t0V1GI71dxEbyHiGUQODiaUG0CxanZxrsV91FFrQX0CD-_H-mSaF5KT2ytMlR56bu_gz00mLvZODQ9Z25nB7BHciJiksGYbQT5uJQkswxDgGUdfCfgv-Es3QCuyBGaYlEvKuYXf0RU0lSIoKE_GB09mYidlNRPIPM-71-9F_SZqG546eTLX_LiOeOcuNC8T61nOLWt7ZobCvoLbEBPRpITLcvp8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچ‌کس این چنین به ستیز با مردم برنخاسته بود ...
©
sadroddinfallah
بروزرسانی: تعدادی از کاربران میگن متن داخل تصویر گمراه‌کننده هست، که درست هم میگن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/ircfspace/2529" target="_blank">📅 19:11 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2528">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iuAQafKnmB_gjpkDV9C3N-MPX9YOZ9RDoXVWtY433ixNUQ2KhzihisxXd7SPmPyOkPKZmNtthUKczTwwntPQ_hOXF0NBUVEdvGwRtSY0swP7PbGWhKnW5dUs2-yxKuV92RwlOG68mKgTUTvOByDmLVVd55GKYHIAYnwK6FRuHzvo6qipi6SuB1FOyepwzAOEy2YFxBLD8ksRA1wrLMxZsce6ueS79WzYPj3f8eQdTyCrghN3LsiR5zMJDy4OjR9M9P-cHs6yYapLuwoaZPvukyziAL-oOnKd86wDg2cj1-ilLg-hI8eSo5ylj1E3_2sI899bggh6FXAjK-J5BXEMCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هسته Aether یه آپدیت جدید داده، که امکان پشتیبانی از Zero Trust و تعریف قوانین مسیریابی، مهمترین تغییراتش هستن.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/ircfspace/2528" target="_blank">📅 18:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2527">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uN64HQML4N4V6DFPep_PFg6CMg6JRTP9-MNl-vl5EdtqK8cMvwQGqk2hmBzJXS9p5X30j2oEEHa7So1sB-4vs68lDX025x9UV4NPt6Y3RugBM6SJ4d9JgxFiPX1IKs5y3TPyStzGzyI-inbTT3m9SbZnOKVbKUxYJFBvQ4uywTLdVogajVhGZ4ayTnOj2j9Rr5eLNtQmjSu8WoF00PuIbZDJpUPQIV7LzhJC-qXkN-q8i9zqGvhDfeUGPslqVjRzkijOIeSQvvDYSc5a5_4gDyVgKDc2OZkcYi8MMpsApg_PwlvgV0HjCyRhc9hPuUx98HVp8oRhbWx33SaTj5o1aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید از فیلترشکن بگذر برای اندروید در گوگل‌پلی قرار گرفت. همینطور می‌تونین نسخه ویندوز اون رو از صفحه گیت‌هاب و نسخه آیفون رو از تست‌فلایت دریافت کنین.
در این‌آپدیت هسته ایکس‌ری به جدیدترین نسخه بروزرسانی شده و روی افزایش پایداری اتصال، بهبود عملکرد کلی و افزایش سرعت برنامه کار کردن.
👉
play.google.com/store/apps/details?id=cloud.begzar.begzar
💡
github.com/Begzar/BegzarApp/releases
💡
testflight.apple.com/join/cRSCr51a
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/ircfspace/2527" target="_blank">📅 18:11 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2526">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">وزیر شیرین‌سخن قطع‌ارتباطات گفته توسعه زیرساخت‌های ارتباطی کشور حتی در شرایط جنگ تحمیلی سوم متوقف نشد!
انگار نه انگار ۸۸ روز اینترنت کل کشور رو بصورت سراسری قطع کرده بودن و بعد از مثلا وصل شدنش، اختلال‌ها در ملانت ادامه داره ...
برای راهپیمایی اربعین هم در ۱۰۰ نقطه اینترنت رایگان درنظر گرفتن و پولشم که با افزایش ضریب و هزینه‌ها، از جیب مردم پرداخت میشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/ircfspace/2526" target="_blank">📅 19:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2525">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iAMJQvWV9nSOguwWlwZk5P3RSxOvmaZIyHMKh-Y6Ulw2YDHXJuaibl4-S4qSkUTw3Q4MnyC8Y2ASfy8Pa1eU27lO4Flo6IJnd6mjD6onBr9sFY7alS0UfpZ0cJolpPHL21Dk-gJyJnR1bQzeAj_4GUjGvc48iYGwtbAAkAxULqqTQF0QltW7PUofHf_hSjlbgeXYX5CNW8ESC-v_PyM7DVbc0v5UtU07gj4YjbaBcz4aDax7WrGK8RNQ8FOfr8YbP6AeRpcm0de-NL_e4I7Vs7LGjlDOmZdm_c2KFvc6w_Twl-cblq3LrJaXVKdE7tL2S9ZGRKHzI8uILxIxX_yzMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گردش مالی ماهانه بازار فیلترشکن‌ها ۱۵ هزار میلیارد تومان است؛ بیانگر حجم عظیمی از سرمایه که به جای ورود به چرخه تولید، نوآوری و اشتغال، صرف حذف یک محدودیت می‌شود.
با چنین ظرفیتی می‌توان ماهانه برای حدود ۳۵۰ هزار نفر، حقوقی معادل ۴۰ میلیون تومان پرداخت کرد؛ اما این سرمایه، به جای آنکه به موتور رشد اقتصادی تبدیل شود، در بازاری گردش می‌کند که هیچ ارزش افزوده پایداری برای اقتصاد ملی تولید نمی‌کند. /هموطن
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/ircfspace/2525" target="_blank">📅 18:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2524">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mhJC2iNaKinDyL9v3eV8RRK3qd6G07u7HlkHaEWg7nzW6kF8OVG6q_AxXEDHhWq7LgX126SJt4wA0b2xUFbp3h3iKo5pKDBD1oUXCmAJjyI5ylY4xfgNh5TP6IBvEzPFM3OIXPEgLcY3AhALMoCAkorgfNkkuN5r7QsvRvYhgtGmHlm-qvKY7K0nNUHB-4FIFTs-mvVG9OVsU32CvsMqIlOKY1f8zZ0ll-uYbPFCV8J9DKZOUnSSzRrB-nO5vQxwbSAB8IRucvxSr2vhKQal6YtisHhuC1CGYD-SkX_cvwx7n8pKa6DHo7TSQUIuxf9wikgSa6EBrVIoPHy6XDFbqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنوز کسی مسدود شدن سایت فوتبال ۳۶۰ رو گردن نگرفته، اما سخنگوی دولت گفته "هرگونه انسداد، تعلیق، تحدید، ممنوعیت فعالیت سکوها و کسب‌وکارهای دیجیتالی پس از اخذ نظر ستاد راهبری و ساماندهی فضای مجازی و دستور رئیس جمهور شدنی است" و "این موضوع یکی از دستاوردهای رئیس‌جمهور است"!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/ircfspace/2524" target="_blank">📅 18:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2523">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KwrZrQ1w40j2Slyhx70orStGkLvnuWpSJsoOK7o6_hRGBhy5DeXlPs00tO7ARqQhiJMbxPNmeW-rXI2ZykwQpICsiU1jZ3yOOXPpQ_aO6yvoF0_8P8V61uRk0qfhrFufdKDTalHZLLgw0K3imcUNTnlVNJLwYE3SX5DHmIIJiiDrxtqNBFGySYeHP1CsYXFKsS0YGJ5uesMBBidofP2Vvvz9SIlwB0mRm5IoUCSXGvGVNG-XfdMAT1_aDLeb_vwK2QMWHHvyBcgwwmai8QJsOOlXewMaHCw7XkU_MGU39mQqEovpz1JlIgdlpju6KtkTgACqHPYenwNOjm-5zoLo9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ AetherST Tunnel یک فیلترشکن متن‌باز و رایگان برای اندروید هست، که با ترکیب هسته Aether و SOCKS5 مبتنی بر HEV، امکان اتصال از طریق پروتکل‌های MASQUE، WireGuard و Gool رو فراهم میکنه.
👉
github.com/immaghzbad/AetherST/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/ircfspace/2523" target="_blank">📅 18:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2522">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ThmhFt0vO7lZpxJpM9XOIbrBkAxkb5aCC-1-rCkVL-v3MSnV0YXz71kR2xb8B5ATPDd5IyOxRU856aOPvPXSdd2yo8_RtHWUZQYv0k4ha8KsCXC1xVHdBBOvlNc-h5dX8boYof7ErLpdYfpMZpTBCaFu-2IqlbR4blWDY40HiL_u6WAOn3aJIZ3QnpWymAWBr_lmLpkfcqQHWHvqa-8nQp4fJVJCCcDoedWqrReVaMx3eV3ciWyUAVaEoawwuogryraUxXMSQcNiUzxTP83XrB2V_wVaNhkPJughpHxN6NEPdbtdimNwhPTNcN37c6T5QW-QgTs4GPC0VxTRbrpxSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از چندروز آینده بخش جدیدی از قانون هوش مصنوعی اتحادیه اروپا (AI Act) اجرایی می‌شود که شرکت‌ها را ملزم می‌کند در موارد مشخص، استفاده از هوش مصنوعی را به‌صورت شفاف اعلام کنند. بر اساس این مقررات، اگر محتوایی مانند تصویر، ویدئو، صدا یا متن با هوش مصنوعی تولید یا به‌گونه‌ای دستکاری شده باشد که بتواند کاربران را درباره واقعی بودن آن گمراه کند، باید برچسب مناسب داشته باشد.
همچنین چت‌بات‌ها باید به کاربران اطلاع دهند که در حال تعامل با یک سیستم هوش مصنوعی هستند و محتوای تولیدشده نیز باید دارای نشانه‌های فنی قابل تشخیص برای سامانه‌های دیگر باشد. البته استفاده‌های ساده مانند اصلاح املایی یا ویرایش‌های جزئی معمولاً مشمول این الزام نیستند.
در صورت نقض این الزامات شفافیت، شرکت‌ها ممکن است با جریمه‌ای تا ۱۵ میلیون یورو یا ۳ درصد از گردش مالی سالانه جهانی مواجه شوند.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/ircfspace/2522" target="_blank">📅 18:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2521">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rRor_8L5M7Ct_AZDbQt6w3weeYgrsFFGCAUYI60SfA2IxmKYcGEXDGailS1h2Cp-UZdlUY36l4sMxuasLCb2zQov7Ri_aejeTJa0x3ZrL23_zWMsGlzWHTgOZAo4dsHA6L-VCrT8CL36gVZ91pb8DEtf7kWVhODr3zccx78Pe3O6SGj0QZq-9jgDFMpo-CDNSrWYjMwiHB_MNv30Ux5f5pLJY0s1Ryy0tSiEV4BbbWLrcF1wxji6N9WOJnMLum5_Rbdrz8lr-FSEsz38xhEJkubTlXBM-XKH8-8GfbKELsCK5hBiQVMdcTBP40ZikVlDt3UkmYWeVt0Wiq74ot6oCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کسپرسکی از فعالیت تازه گروه هکری تحت حمایت حکومت ایران به نام Nimbus Manticore خبر داده، که با نام‌های Mirage Kitten، Smoke Sandstorm و UNC1549 نیز شناخته می‌شود.
این گروه در حملات جدید خود از یک Backdoor ناشناخته ویندوزی به نام NightLedger و دو ابزار Tunnel با نام‌های BridgeHead و ArcBridge استفاده کرده، که قادر است اطلاعات‌ سیستم و شبکه را جمع‌آوری کند، فرمان اجرا کند، فایل‌ها را سرقت یا حذف کند، Processها را شناسایی کرده و از صفحه‌نمایش Screenshot بگیرد.
بخش نگران‌کننده‌تر، ابزارهای BridgeHead و ArcBridge هستند؛ این بدافزارها سیستم آلوده را به یک Relay مخفی تبدیل می‌کنند تا مهاجم بتواند ترافیک خود را از داخل شبکه قربانی عبور دهد و به سایر سامانه‌های داخلی دسترسی پیدا کند.
روش نفوذ اولیه هنوز مشخص نشده، اما این گروه سابقه استفاده از پیشنهادهای شغلی جعلی و صفحات تقلبی استخدام و ویدئوکنفرانس را دارد.
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/ircfspace/2521" target="_blank">📅 18:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2520">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">فیلترشکن
#دیفیکس
در نسخه ۵.۸، هسته وی‌وارپ رو بروزرسانی کرده و میتونه به دورزدن فیلترینگ از طریق متد مسک روی بعضی از اپراتورها مثل همراه‌اول و مخابرات کمک کنه. همینطور مشکلی که باعث میشد فرایند اتصال در همون ثانیه‌های اول با شکست مواجه بشه، در این‌آپدیت برطرف شده.
👉
defyxvpn.com/download
💡
github.com/UnboundTechCo/defyxVPN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/ircfspace/2520" target="_blank">📅 07:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2519">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Iy6nuUXks8xRH2iiINy5QeWz4frpRvFVr6Krug5okwZWOkB_0oAzVEtsxMRPfYo7OERPK79sp2VVqwYjh5MLZdSM71QmcUlaaMFNkhLxreCAGwgogOQBc_A7iuwpfK0M0Lfcn1Kt0I43MRvOU8W18JSK5wjQwUsVRXepzCAtic22p-IkAsQKmkXz0VUazjZVSgmluX7W4XXcJJhXpN38d2NEBEJdSkB4ga3bFgpnsy0NnXhT22Okbea6_bia9DUroluBe22YSEP9zKuo5mHfQmKgf2zgEjpAnhp7zhR2bC4D5oZkpet0VH2kQvHBDPIng--nps6UKPD70Y585vmRqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ
#Aether
یک فیلترشکن متن‌باز و رایگان بر پایه هسته Aether هست، که برای اندروید (AetherMobile) و ویندوز (AetherDesktop) ارائه شده و از پروتکل‌های مسک، وایرگارد و گول و حالت‌های اسکن مختلف پشتیبانی می‌کنه.
اتصال مجدد خودکار، انتخاب و تغییر خودکار پروتکل درصورت شکست اتصال، برخورداری از حالت نویز، امکان تنظیم MTU و Keepalive و همینطور Split Tunneling، بخشی از امکانات این برنامه هستن.
👉
github.com/QW-AI-Code/Aether/releases
👉
github.com/QW-AI-Code/Aether_Desktop/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/ircfspace/2519" target="_blank">📅 07:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2518">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d1cc8cywe_7vYx1bZwOQ2MGIB2bz2m2HX4H0HR_Ij4TcbFdYx8OG9l7PxmTzm4SzW8DiMP6nYnGy2YgrFVN6tTvLth0B6pCVp35ava6KFoiAdUp8d6rS1FQl-EGol5Lufl7gAb-KhqN4-npChP-uoR_iR_AKMSOSxRFMg4qAsDqKp6UW5N3kSHWIGvBbNE7QijnauQ-blPUtt4uMJfYSDJQJ4TdFkJCHa_zyiKy4wzn08idrTAx3bSMPBboAfLYzFi9RqDGZK7MA8GSMZB-34sRoBnBw_a-bx98XsBe9WIFa6HUUkAHG4OKz0dR4dwqXEQfmMKkPMsmUrBj28IIP9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تازه‌ترین نمودار ترافیک اینترنت ایران بعد از ۲ دوره قطع اینترنت، نشون میده ترافیک هنوز به حالت قبل برنگشته.
الان دیدم یه نفر یادآوری کرده "۴۰+ هزار نفر دیگه نیستن که به اینترنت وصل بشن"!
#دی_ماه_خونین
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/ircfspace/2518" target="_blank">📅 18:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2517">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CoychOLDEtSprN3Tx_D_nyWz7N0B0WhbF-YTOTEMa5x4aRZ-lexXYI3TLHnJeVQfn_447b-n7hL2wcdYogltFp3gvaPAgkxo6tQLXJfIUAFKIrj0KpJlbvhmcsVL1wLqwCQ5mjZdyOwvE2Ly0kP3JIfj9vDETgV5Dv4OS-nf5QkYCowBM58R7c_0Yg7RBinhTyU74t5oAlRFIgBtFfVv1SNZuDZp8YcBblj7b1d8DcasR_6fEPBofpU-6qUBA2nVt6E-1jHs171Lzw3qkQo7HhFWC4F_Kp7UhCGqU8Yh33W-gSy0jS3nPXS7Q0nxBb0Q4d0MdNxVG9UmSORIcGp9tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر شیرین‌سخن قطع‌ارتباطات گفته "سایت‌های ارتباطی در خاموشی‌های بیشتر از ۲ ساعت قطع میشن و راهی برای تامین انرژیشون نداریم".
یعنی از هر زاویه به این مرد و عملکرد درخشانش نگاه می‌کنیم، حل مشکلات و امیدواری به آینده فوران میزنه!
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/ircfspace/2517" target="_blank">📅 18:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2516">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qD8NAGHaDkTDKcITnVqTWtLs4B_r_VMpDVG5LSZoPHYEiGB6KFO_h3PbcRQsPxaGKuFPxyTDj-wts_meA3srHjE8_USft1FLTQrgupAYyphs9kPYBEwOsjzgN0P40NpuwAKqsSp1VYBTz6VstGLmbLGSHGTnCdq2Vfdr6qbVTv_thEbyjwqwMDgZuAL8pVTqKgplVywIekf9rhAe72hlgEZBmaDh23XDsvI52MYkoirYVmRXbYrsrSZ6-_7fdLgOQrxO-kFnFfXZz2YFn55p6_FhqNqZF9nJzabs3nc9yh91LtDXqfiQ1HwEFLKF_cd6ZEi221F8hR-mXeJ_DrsTXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی هسته ایکس‌ری از نسخه ۲۶.۱.۲۳ به بعد یه سری هشدار برای قابلیت‌های منسوخ‌شده اضافه شده، که شامل allowInsecure و Shadowsocks، VMess، Trojan و VLESS بدون Flow میشن. مثلاً برای Shadowsocks این پیام در لاگ نمایش داده میشه:
"The feature Shadowsocks (with no Forward Secrecy, etc.) is deprecated, not recommended for using and might be removed. Please migrate to VLESS Encryption as soon as possible".
اگر در حال ساخت یا انتشار کانفیگ‌های مبتنی بر Xray هستین، بهتره به جایگزین‌های پیشنهادی مثل VLESS Encryption مهاجرت کنین، تا بعداً با حذفش به مشکل نخورین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/ircfspace/2516" target="_blank">📅 18:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2515">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r_MbA3l4_9VZTal-7bblZqjbbC9bVP3SMdZ2E7QUcC1xpx4XH98RPTJjtv5T9iSEFk9YwAtaHUc8CabQrxTJBF-KVt2JaDrlfzpwbKrf-SGWuaJ04CSus2auzfbExt0TyZRop8bxiOZoMdvSXqFdIL6xADR1N_MXEh--Mv8YoznlnH51c78W0nbNeVXsjLEaSJ7txFseVZq3H5hIj87tIQL2-Jt420GdchcL7TEc8ieXJV4_CFGWKtzGSgQAOHcAWVjnJNnJiZfHLYE0u89_EiGrt6GH-56rEK9AwZC2R9wgAN2w2g78lZ9DY7SXrg6oUirRrkpOjs2JyuP1BOzT2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت دسکتاپ v2rayN یک بروزرسانی امنیتی اضطراری منتشر کرده و از همه کاربرا خواسته هرچه سریع‌تر برنامه رو بروزرسانی کنن. این هشدار در چند ریلیز اخیر هم تکرار شده و توسعه‌دهندگان تأکید کردن که نسخه‌های قدیمی حتماً به آخرین نسخه ارتقا پیدا کنن.
در توضیحات این بروزرسانی اومده که "یک آسیب‌پذیری امنیتی بحرانی در دانلودر داخلی نسخه‌های قدیمی برطرف شده، که می‌تونست به مهاجم اجازه بده فایل دانلودی رو در مسیر انتقال دستکاری کرده و به جای فایل اصلی، فایل مخرب رو بهشون تحویل بده".
👉
github.com/2dust/v2rayN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/ircfspace/2515" target="_blank">📅 17:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2514">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I9peEQxDYKQALggohDHgEFstgzzf4joYsgxSI2nACioaRdleRHRtBGeB_9u6cSR6RkBBPJ2fKSV1BMYmV-Ps6sOgrG2AHYbM6MW0FisiEBwDBxi_JTCZ5gQQEvfUsYSkioXdrKbTNqKpGJQYZvU19l82T0zn8J1ScQJNJbtoFq7OXDdR3ChOmFXiD-MbJPEG2h1ElvELtsV_qIw6ufQm5L6Qypita6PPoGMh0Uh5PaI9JnXoxZedYZEcx3UsH9w4qVGabLdTn2yY9KeNVA1Krq4T7qYoZkCV-1UXPUoQE1LHeLtbgIV08mbKEyD55BBm8rZW-MAe9VYca4FiU9sApQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطع اینترنت در راهه؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/ircfspace/2514" target="_blank">📅 19:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2513">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cd3AdiqUzh5w2nfyC3--UdBBl_D8evRXnFGdcwyWa8Dn3fR7JCJHBCdUqMMUphD_POyCWWvm8BLqSstkvWc6-YvZMJyMQnSIYdthjifdej5-fCE3Qpv2preugyx_e9RqJ4oF1WsG39m4GN-vQoLl8WI-nKsLY_g5w_GNgrBdgy1G2806eHrnvgIiTYjbZ83nNr0E2FHw2tT6M2338klSEbb9wd4f4mTTSDcJ3wLur1SdOJxnvU1-uL-xSFT3i2MkJmiW4ySKSym0onDIt7snMGug7v1KXbEtwqrOrnG-PKyO58pc-BZNbCUL27KX9Wgnl0NqdrpqdK6zRQrC-JK2Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبلیغات تلگرام ابزاری شده تا بعضیا مرزهای بی‌شعوری رو جابجا کنن.
هیچکدوم از تبلیغاتی که توی کانال نمایش داده میشن توسط من ارسال نمیشن، به هیچ‌وجه مورد تایید نیستن و اگر سرتون کلاه رفت یا امنیت و حریم خصوصیتون به خطر افتاد، مسئولیتش پای خودتونه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/ircfspace/2513" target="_blank">📅 19:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2512">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Zgi3UW9Pjzsd_XkPaYUM89dG6ABCY54P1XejtozcZuv_SFgeuRDv90cYei7L-hj1a4Zxm4o1zS84UtY88oqvedW5K7n7dABr5tvznizTAC4j9W1cJdIH9iREej1KU6SuMG8tXUT6L0WqTrCVJcJTPgH3dmxrMzOPRhsStVuqe1sE9vEQFnCji_9iEZBMw6qWkC03u9fKJTTkBg00TNYs0A7dzEoWnwW8YV-OZHFbIrg5ZLz3C2ijYzym0pL-ssnud-YG5HWJTjYdGaiOc1yfHpW1HTjvK-D3w9NNQaTpoIDwz8LhXJWYq6Llhw1stgYHD2xdV_Zc6g5zGt0J3qCt4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انجمن تجارت الکترونیک ایران یه بیانیه داده و نسبت به تعلیق دامنه فوتبال ۳۶۰ در رجیستری ‎.ir اعتراض کرده.
اصل بیانیه قابل دفاعه، اما امیدوارم برای کسب‌وکارهای کوچکتر، استارتاپ‌های کمتر شناخته‌شده یا پروژه‌هایی که بدون پشتوانه رسانه‌ای قوی دچار مسدودی دامنه یا محدودیت میشن هم کوپن بسوزونن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/ircfspace/2512" target="_blank">📅 19:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2511">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ساترا گفته نقشی در فیلتر شدن فوتبال ۳۶۰ نداشته و قوه قضاییه اعلام کرد مسدود شدن این سایت ارتباطی باهاشون نداره.
وزارت قطع‌ارتباطات هم طبق معمول نقشش فراتر از هویج و سیب‌زمینی نبوده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/ircfspace/2511" target="_blank">📅 18:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2510">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MNUJzhb_7wb4NhFRpxNgLJzy70Wx1feaJ1EfVh3ZqVDknHdfW1YzjdXCo01Eq_TLOtkoh0RxQOYRgzjBjPF9v3_JRyku6VGNvhtlGNiNveAxqACFfsTQgTeu6MvQMpH6CmbGPF5xcdJUE-YEfasCj_MVEQllFw4SBnTu6fUaakkWZCUBetloLhVojmXhdy2k4QTjv4KBUmaJUvoytdmLxBIf5k3V_alnB4wZcK25pmIseu1V7CE8qZqPh341zoE_iG2LYWxLWNMeknWLa7rhsPJ-2IOVea4AWWVs8335175GF1ypr-n1CceNN_AT79Gm-yk87xOKof0xMfS9O5GLpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ ShineNET VPN یک فیلترشکن رایگان و متن‌باز برای اندروید هست، که از امکان انتخاب هوشمند سرور بر پایه هسته‌های Xray و Aether برای دورزدن محدودیت‌ها استفاده می‌کنه.
👉
github.com/shayanheidari01/ShineNETVPN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/ircfspace/2510" target="_blank">📅 18:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2509">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EoRbiIQZDGE2ScIsV82YEBdmDGykYW1cboFmAcc-k5JuoqYuE9aYR8E5rumHEYFXAqTGIwd-aZ8zMzylBKZY6hp9rakNgZLOvlrQ0jCT6zvvK3KPuYGtE0ORHRF7EQWWiJzcbp0l1HWSDfXQpz2TLLJ5ypk5NyZxIoce1p1PJ7yetEv7lYyh5caEk64RuKHFwAUFCN_6yNLcrFkzAmDFwyxupEkYfHC8K8N6GpqlWpcILc8_ELIZWmwFONIisHGti8_OImEFyQQ5p6fLisKiPt2F715LQRhMUZjftGR9OCIZ3ejv8Te2Mj9lIKwDl45nxWTV7JxHUmwD3-RLkaZeGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت فوتبال ۳۶۰ عادل فردوسی‌پور توسط قوه عاقله فیلتر و دیشب چند دقیقه قبل از شروع برنامه زنده از دسترس خارج شد.
هنوز علتش بطور رسمی اعلام نشده، اما این اتفاق پس از درخواست سرمربی پرافتخار(!) تیم فوتبال جمهوری اسلامی برای برخورد با این برنامه و یک روز پس از جوابیه به امیر قلعه‌نویی صورت گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/ircfspace/2509" target="_blank">📅 11:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2508">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NgBVjC2bRvUEQuVSrQnRFx6kU__y-FV89PH-X9Qt9Pe531Z-WFYz_aHFaGUWEDoGTNsbK8LmN2uk8d1qlOlyZ_fJRqkv3RP3b-_OzQVMEQXB66j2hZeS3C4yxN_fFXidgRJbHUvFBikQiqCMKEJW1vxSI0mASm6wzI_Bs6tis59Ys0_hOgi-baV8FxTFirivqlV6cMzbWPTG44sRxxr26lwAOeVbdbQ97ppdaOcIChhdl3HdRsUUgDU5AgEDfAbfCa6yEgLlHFes3hMpphgrPDlbSNFIDDcvBMVwF22iDLy57lLLVfOONZQ3sMFsSdus9veflBVNIBrJGT5tO3yYTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن Aethery برای اندروید یکساعت قبل به ورژن جدید از هسته Aether بروزرسانی کرده. اپ Aether-GUI برای ویندوز هم کمی عقب‌تره و ۳ روز قبل بروزرسانی کردنش؛ البته احتمالا بزودی براش آپدیت جدیدی ارائه میدن.
👉
github.com/ZethRise/Aethery/releases
👉
github.com/MatinSenPai/Aether-GUI/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/ircfspace/2508" target="_blank">📅 17:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2507">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lC03MNyFpkMoJde0BcjdzKTQyB1i4sV9IoQoDEW2Q3AcxIGdvgvixru3oBiIAAHpUYdesQ-jC5CyFziGezXlr_7s5ALzmVFr9TsdPf-SeCaJLBsbUQ-ScewiDSjq7hx35uvJWtwOHhOp9kyte4vkVKBMh9kpC4RVfQmgxpgPbrgv9wb5fpBZlGvmbBeA-UfWU3qgernSSXIaWl80QFKZ8lkRXUVJwcS2qPdSmxIPrr4hNU5wnfGnx--YfTa0stiz5-LHURoAGfcJYSjGA0Ln283G8HzEey6uqSlbKw-nw4-kAVDN3HpGZm0zAoQLu2Hkt8ZA595OdnhdMK0Tpyhpfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه ۱.۳ از پروژه متن‌باز و رایگان Aether منتشر شده و مهمترین تغییرش اضافه شدن حالت اسکن Ironclad هست. برخلاف حالت‌های قبلی که فقط بررسی می‌کردن یک اندپوینت در دسترسه یا نه، این حالت قبل از اینکه به یه سرور اعتماد کنه، یک تانل واقعی برقرار می‌کنه و یک درخواست HTTP از داخل اون عبور میده تا مطمئن بشه اتصال کار می‌کنه. البته این روش زمان بیشتری می‌بره، اما در عوض احتمال وصل شدن به اندپوینت‌های خراب یا ناپایدار رو تا حد زیادی از بین می‌بره.
توی این آپدیت روند اتصال مجدد هم هوشمندتر شده؛ اگر ارتباط MASQUE یا WireGuard قطع بشه، Aether دیگه برای دور زدن فیلترینگ مستقیم سراغ اسکن کامل همه اندپوینت‌ها نمیره. اول همون اندپوینتی که چند لحظه قبل روی اون متصل بوده رو دوباره امتحان می‌کنه و فقط اگر از دسترس خارج شده باشه، اسکن جدید رو شروع می‌کنه.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/ircfspace/2507" target="_blank">📅 16:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2506">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">پژوهشگران امنیتی Insikt Group وابسته به Recorded Future از شناسایی یک کارزار جاسوسی جدید خبر داده‌اند که با استفاده از بدافزار MarkiRAT، کاربران ایرانی را هدف قرار می‌دهد. این عملیات به گروهی با شناسه TAG-182 نسبت داده شده و طبق ارزیابی پژوهشگران، ایرانیان داخل کشور، مخالفان جمهوری اسلامی و فعالان مدنی مرتبط با جنبش‌های ضدحکومتی مقیم اروپا و آمریکای شمالی از اهداف اصلی آن هستند.
مهاجمان برای توزیع بدافزار، نسخه‌های آلوده برنامه‌هایی را منتشر کرده‌اند که برای کاربران ایرانی کاربردی یا جذاب به نظر می‌رسند. از جمله آنها می‌توان به فیلترشکن Pis2ray VPN، نسخه‌ای جعلی از Star VPN، برنامه‌های YESHICA، YEPlayer و YEMPlayer و همچنین یک وب‌سایت جعلی با هویت Starlink اشاره کرد.
بدافزار مذکور پس از اجرا می‌تواند اطلاعات سیستم، فایل‌ها و داده‌های مرورگر را جمع‌آوری کند، اسکرین‌شات بگیرد، دستورات مهاجم را اجرا کرده و ارتباط خود را با سرور فرماندهی و کنترل (C2) حفظ کند. پژوهشگران همچنین زیرساخت‌های جدیدی را شناسایی کرده‌اند که نشان می‌دهد این کارزار همچنان فعال است و احتمال ادامه فعالیت آن وجود دارد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/ircfspace/2506" target="_blank">📅 16:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2505">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">مدیرعامل شرکت آسیاتک با رد شایعات منتشرشده درباره کاهش ظرفیت دیتاسنترها و احتمال قطع اینترنت، اعلام کرد: تاکنون هیچ‌گونه اعلامی در این زمینه به آسیاتک ارائه نشده و خدمات ارتباطی و دیتاسنتری این شرکت مطابق روال معمول در حال ارائه است. /سیتنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/ircfspace/2505" target="_blank">📅 19:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2504">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">گزارش‌های زیادی از کاربران در ۴۸ ساعت اخیر در رابطه با کاهش پهنای باند، اختلال یا کندی اینترنت تلفن همراه در مناطق مختلف کشور وجود داشته.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/ircfspace/2504" target="_blank">📅 19:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2503">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c2zefZNu-WMzHcNX4pQDosc9L1QTgm-79I7jJdP61-LploBQCnrTzpKLJOfZTVMNrNWg3vCztmls45iG2UlD6FTU8Rp5OI3u8zP3inPQ9IwXrHbiNgovviwbn2y2cV3VVQmrvO8aeyYPZlOYL0EPR7FLUtpVZBOUyh_NQWhHnMn6K8XqmbB_35qF174K3MgzznRFakCvuRBsb5B9GU0O1UGboRzBBZzAJ08NelMDRK-tyML8E4PhSD2QINr2Mp4zSg7OMlrvundgXpO9Uq5pTN1o5kvESRjZaxiuLAhToqZLw2TiJT0oZ365a6VWe_CYNGCZCb9MXqYVyS_m2l2PrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران امنیتی از شناسایی یک زنجیره آسیب‌پذیری جدید با نام wp2shell در هسته وردپرس خبر دادن، که می‌تونه به مهاجمان اجازه بده بدون نیاز به احراز هویت و حتی بدون نصب هیچ افزونه‌ای، کد دلخواهشون رو روی سرور اجرا کنن.
بدلیل شدت این آسیب‌پذیری، جزئیات فنی و کد اکسپلویت فعلاً منتشر نشده تا مدیران سایت‌ها فرصت کافی برای بروزرسانی داشته باشن. این مشکل در نسخه ۷.۰.۲ وردپرس برطرف شده و برای بسیاری از سایت‌ها بصورت خودکار در دسترس قرار گرفته.
©
slcyber
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/ircfspace/2503" target="_blank">📅 18:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2502">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">بیش از ۱۱۶ دکل مخابراتی استان هرمزگان در پی حمله آمریکا دچار اختلال جدی شده و خدمات تلفن و اینترنت ثابت و همراه در شمال بندرعباس و بخش‌هایی از استان با قطعی مواجه است. /عصرایران
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/ircfspace/2502" target="_blank">📅 18:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2501">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">زهرا مرادی، مدیر اجرایی سامانه پیشگیری از خودکشی طعم گیلاس: در روزهای قطع و اختلال شدید اینترنت، روانه حدود ۷۰۰ فرد بحران‌زده که به کمک فوری نیاز داشتند، امکان برقراری ارتباط با سامانه را از دست دادند. برای تصمیم‌گیران، شاید اینترنت تنها فشردن یک دکمه باشد، اما برای سامانه‌ای مانند ما، این شبکه تنها پل ارتباطی با انسان‌های ناامید است. قطع کردن اینترنت، فاصله میان زندگی و مرگ را کوتاه‌تر می‌کند. وقتی شبکه قطع می‌شود، افراد آسیب‌پذیر دیگر نه تریبونی برای شنیده شدن دارند و نه راهی برای دریافت کمک‌های حیاتی. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/ircfspace/2501" target="_blank">📅 08:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2500">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UkbJbh4a4H-NcqGi-egoSEyPXoybzI8q6J_9af8qPSt35I5w_WA5hio32wMqfd3J4C2Ux_OZ1jUfBpd1rv0588SKPj-i2S7lAMBNY6oEe9R8pSDyABm5hAFJqGvGgmW9WsckNk--WDMUl_w6MXi8RRCQqaeRc_tRXYgaa-EAOJ-cVdltlWVAiZQXCDFYf-41KRglJa7d_3agOfu4jTQP5SLCPkWphmuFg-v3jM0tK6u2gNAPmvmLXaHnS28b0PoD0SUkyAmolQ1p11ipvVOYl5ZWZrNbdo_4r39-iTNZHzYJSAnJsio2QRVf2Bt5FNz7ihw5H2aOPoDnDdEnVJ5OAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگرچه قضیه ترند شدن "لغو عضویت جانفدا" در نتایج گوگل بزرگنمایی شده، اما یه نقل‌قولی هست که میگه "وقتی دیکتاتورها در حال سقوط هستند، فقط دو گروه کنارشان می‌مانند: هم‌پیمانانشان و احمق‌ها".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/ircfspace/2500" target="_blank">📅 07:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2499">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ObilGf8NzsetMVj3UXDWFvR3vhTFogUIM1GNDA2pyXbpA8BEFPEE4fZ0Be_R9dUDv0kpjtELhXE3RwcF9FGorGzvEtbsq7mJxVJtLAWXhCiUbuh9tRRMRQAr3Q1GyHZ9DV2yVm0J3wQ-aIHze87lkY_XBlVqGJ6stk84zcd8JlQsZxSmQxLIRyQ4nsnIRmj5UIFNpKJaE-pLc07OHleYCW4BrPfaYoGcdivNukw4ri70XD-Yh4EgphcuHcEGx65mjOjqdf7uhNlcTRgUel4c2LS14NhCK5FBNONIIWAQIzVhOuXaF_sfF60lZJxmmOmWF3QMWaBxC2Mhw2iOpHvatw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ dicodePing یه کلاینت متن‌باز و رایگان برای اندروید و ویندوزه، که مدیریت و اتصال به کانفیگ‌های مبتنی بر ایکس‌ری رو راحت‌تر می‌کنه. این برنامه از مدیریت سابسکریپشن‌ها پشتیبانی می‌کنه، می‌تونه بصورت خودکار بهترین سرور رو بر اساس latency، jitter و سلامت اتصال انتخاب کنه، از حالت TUN/VPN پشتیبانی می‌کنه، آمار لحظه‌ای اتصال رو نمایش میده و امکان تعریف دامنه‌ها و برنامه‌های خارج از تانل رو هم در اختیارتون قرار میده.
👉
github.com/mcodersir/dicodePing/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/ircfspace/2499" target="_blank">📅 07:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2498">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">پژوهشگران دانشگاه میشیگان، دانشگاه نیومکزیکو و مؤسسه فناوری دهلی، ۲۸۱ وی‌پی‌ان رایگان اندرویدی با بیش از ۲.۴ میلیارد نصب رو بررسی کردن و به این نتیجه رسیدن که بخش زیادی از این برنامه‌ها برخلاف ادعاهاشون، امنیت و حریم خصوصی کاربران رو به‌خوبی حفظ نمی‌کنن. توی این بررسی مشخص شد ۶۱ اپلیکیشن بخشی از اطلاعات رو بدون رمزنگاری ارسال می‌کنن، ۲۹ مورد دچار نشت ترافیک یا DNS هستن و بیش از ۸۰ درصدشون هم با سرویس‌های تبلیغاتی و رهگیری در ارتباطن. علاوه بر این، خیلی از اونها هنوز از تنظیمات امنیتی ضعیف یا روش‌های رمزنگاری قدیمی استفاده می‌کنن.
اما نگران‌کننده‌ترین بخش گزارش مربوط به ۵ وی‌پی‌ان بود که فایل تنظیمات اتصال رو از طریق HTTP و بدون رمزنگاری دریافت می‌کردن. این ضعف میتونه به مهاجمی که روی یک شبکه عمومی مثل Wi-Fi رایگان حضور داره اجازه بده تا اتصال VPN رو به سرور خودش هدایت کنه و تمام ترافیک کاربر رو بدون اینکه متوجه بشه زیر نظر بگیره. به گفته پژوهشگران، ۲ مورد از این برنامه‌ها این مشکل رو برطرف کردن، اما BambooVPN، Free VPN و 101 VPN همچنان در برابر این حمله آسیب‌پذیرن.
©
thehackernews
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/ircfspace/2498" target="_blank">📅 17:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2497">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rMZ_xJBYDOCWDP17U7GxEgvVswu5BvJy76wPuNPLtXwYYBjAt9AS9lyyiWWo5KoBL_FLu7GzfeujX6268XsjmXUzHldFlGpe3M-jg6NegF5aUG-ZYlHDYQ9ErpghqsPSe4SkJfiMZdIM6AMk4-GU6yylR8aqoouCXAKd375F_Gts8fP6T1IjIeIEMt-mlsGmwmCEeFbpbLazVCQPCJWZxOD4zuDd56ktr1OC3V4zZCH6FoRUHRXtxRdY9xJEESnuIaXR7Cdvy3MawPlbUwet0YzxcAU8IuId1kx43mH7d-gHSG24cuO690SuEwuWuX39m4hSSNNKp_oSiwjU8v7o6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Aethery یک فیلترشکن متن‌باز و رایگان برای اندروید هست، که بر پایه هسته Aether ارائه شده.
👉
github.com/ZethRise/Aethery/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/ircfspace/2497" target="_blank">📅 16:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2496">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YHEuQ1-bZ9qmOqqqNX5uWS7IXPzuAUQOxzdEjgct-3AvulswnE8kXeVLMUJNA93rwQE4aTOj-7l9dP5f8rLpoTWIiaqPRxdXZbJwQLxk7uKZ53gvQ4ucQCuZF38Vvuf-2KQ7-1J4kh6ffMfS1Yu4QoumGWwX_6WdkZ2Ub9uE28NccmgxlDGSZYPeIXdW6lai44yOKJgJveXYb0IEcNVaKEfAEgnr89MVK84B7kk9E2RRyTUTBZtFkUdhJ3LF6lar8hphxiCgkeVHetStHV-hG5dG8uUMRfacJzGBId2uT5Ff50t1xDNpANSb2Ew_cjByQpMQgrBu4Vvpgfq0GRteVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت رسمی Sing-box برای سیستم‌عامل ویندوز بصورت پیش‌ازانتشار عرضه شده و طبق اعلام توسعه‌دهنده‌ش، همون تجربه‌ای رو ارائه میده که پیش‌تر در نسخه macOS در دسترس بود.
👉
github.com/SagerNet/sing-box/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/ircfspace/2496" target="_blank">📅 08:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2495">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HcEjtyxsaYlO48dvkbF9DkpEcHysKgULXuWfERqe8UWUidSkiXkjYNavLGEclumjhBvBhCgg3iC9Sde8FIZCcvldXnFZxVx2agohGEr7ASEB7C6KbS_x0gPkicY5npvI3eVRJHwLCVtcYrd0KeUZaGOh9ok6Ekq9bg6iOlz-Wo2FAxI982kU5xXlDHed2qonyKpVBbEFppJPowcJZL_SIsfqxJETMRJkYMRlMusa-OfNnD-WaHQ-R4Uv-zQ29n7w7EeIqfSjKo1BegrjE1QleDmqy1fFIyqwAflcF7Qud9zRLoZtnTWnpOp28ZWIW3WquSFJV-mhA3VRmtj0EnAQ-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Aether-GUI یه واسط گرافیکی برای هسته Aether جهت دسترسی به اینترنت آزاد و دور زدن فیلترینگ هست، که دردسر سر و کله زدن با محیط ترمینال رو برای کاربران سیستم‌عامل ویندوز حذف میکنه.
👉
github.com/MatinSenPai/Aether-GUI/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/ircfspace/2495" target="_blank">📅 08:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2494">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WfUyNliJeclIqfWbcGEtRBygN3opESWI6rH5GKz49a4z3OOn8_xn39dl-KcivI3_puhv-P6jze32Y-YqMkatKRplgsEsi3GBEOAbjeU3a6FDZaRyQl5ti8FZ_7FRSg6oTOnHCJPmAE5WHIvMLMIS1C-2CxY9yZrdj4kRE4PvpOB4gh_p1C21z1cpuky3ac-Wjs42d7SgYS-VNd9wjrUeZcBolqe5KB1RXpM2TmUFb-j2jBC3BhQHSto2mhS96ZTRpR_8NDKgyLUGBE6d_cLubthhVMcqu6XruPoLWiyFTjTXSz2K8H71I6ZuMIA7nuI-ZVQZcbx4t4hEuTXmI9vD8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکروسافت در بروزرسانی امنیتی جولای، بزرگترین بسته اصلاحات امنیتی تاریخ خودش رو منتشر کرد؛ بسته‌ای که ۶۲۲ آسیب‌پذیری منحصربه‌فرد رو در Windows، Office، SharePoint، SQL Server، Exchange، Defender و سایر محصولات این شرکت برطرف می‌کنه.
اهمیت این بروزرسانی صرفاً در تعداد خیره‌کننده آسیب‌پذیری‌ها نیست؛ دست‌کم دو Zero-Day Vulnerability پیش از انتشار Patchها، عملاً در حملات سایبری مورد Exploit قرار گرفته بودن.
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/ircfspace/2494" target="_blank">📅 07:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2493">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AbmfHISog0juvct8CEEWyXP_e2SRU5A4RSbyP4fOsbdzN21zqEI7BJ27AUQSLj_k8Z-G1FPIQzi9a1QZWH25pKTvegOljSAXWKiORNRt-l3aFRia_qpAjrIsfrsRyonBuROfVda0NkIJiKdBnNdvgYDiqlM-MWw9a5iF4OuAU3wqZQ8B1On2vPTFCmeKovtPQwhKZzzK3MKpdr5JVH6jdQ_qLznPztGVlL1xARvEpGIrVC-CSP0bvHQZe8ESmu3NZIvUl6aGoEAb775KknQAOIHWeUyoeW_MLrt0d90szKWtxLbkW9awVy2em5_fD3rv63ZnKRbv2vAMbXosJ72ifg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژه Aether یک ابزار متن‌باز و رایگان برای دسترسی به اینترنت آزاد و عبور از محدودیت‌های شبکه هست، که با تمرکز روی سرعت، پایداری و مقاومت در برابر فیلترینگ توسعه داده شده. این پروژه با ترکیب وایرگارد، MASQUE و WARP-in-WARP، ترافیک رو تا حد زیادی شبیه ارتباطات عادی نشون میده و به همین دلیل روی شبکه‌هایی که از DPI و روش‌های پیشرفته فیلترینگ استفاده می‌کنن میتونه عملکرد خوبی داشته باشه.
یکی از قابلیت‌های کاربردی Aether اینه که خودش بصورت خودکار اندپوینت‌های تمیز رو اسکن و بهترین گزینه رو انتخاب می‌کنه؛ بنابراین نیازی نیست که تنظیمات رو بصورت دستی انجام بدین. بطور پیشفرض هم از HTTP/3 استفاده می‌کنه، اما اگر شبکه‌ای QUIC یا HTTP/3 رو محدود کرده باشن، میتونه اون رو روی HTTP/2 قرار بده تا سازگاری بیشتری داشته باشه.
این پروژه روی ویندوز، لینوکس، مک و اندروید (از طریق Termux) قابل استفاده هست و توسعه‌دهنده‌ش اعلام کرده که بزودی قصد داره هسته Aether رو با زدن Pull Request در فیلترشکن‌های ابلیویون و دیفیکس ادغام کنه.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/ircfspace/2493" target="_blank">📅 19:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2492">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C4cDuCrQ4KKJ8AMXUH5w5rSec8iVQe3XzcrRcJ8BK6xOYZx2dpz6gKUPaJrCbp0mPv7a0U234wq5M0eLtbELxyWmwCMcxkt3eUiDXFmFRsrlQzxMFkcyg6io08Pxnac-4-OuRGjK0LPMjFH7Fsxk17jv0FdspK2pyLRirnQt3qWfnjowS-aq7Exk0CCu3m0SGCImQe1fvTrUFsH0obbyFziEq1e6c8f2TIIbuocoH8I97PEZnnqUJtDopk0mpUT18JT3YP11QlQsCnBB9IC81hcWY2-7MaQ6q9AyQqsIQdC2bYW_h7MKQyySaaclbMupCpvoWDDNmaUMsbZ2-epD2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دامین
t.me
که بدلیل تحریم‌های وزارت خزانه‌داری امریکا مسدود شده بود، مجدد فعال شد.
©
Linuxmaster14
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/ircfspace/2492" target="_blank">📅 19:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2491">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">نزدیک به ۵ ماه مجلس تعطیل بود، آب از آب تکون نخورد. ۱۵ ماه وزارت قطع‌ارتباطات هم تعطیل بشه، وضع اینترنت بدتر از این نمیشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/ircfspace/2491" target="_blank">📅 19:16 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2490">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">دیروز کاربران گزارش دادن که IPv6 بصورت محدود روی بعضی از سرویس‌دهنده‌های موبایل باز شده. همزمان گزارش‌ها از اختلال شدیدی که روی اینترنت موبایل و ثابت بصورت منطقه‌ای اعمال شده، زیاد بوده.
در مورد اینکه آیا با از سرگیری جنگ ممکنه دشمنان داخلی اینترنت رو قطع کنن یا نه، نمی‌دونم. البته قطع مجدد اینترنت از کسایی که ده‌ها هزار نفر از مردم رو توی ۲ روز قتل‌عام کردن، بعید نیست.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/ircfspace/2490" target="_blank">📅 08:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2489">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rVMrqqLqTiPemP7o-eJYE_7u_Fgm-0Ln-xXlgaPWf5yluxoVlg-uirH1BBIsFLb5GJku8E1B1hMz0NPIGVVa-i0msWG8d42_fwNL8PwVThApHFG2UqKQPGVLcG85rlJWNA7WwzYxUrh_e8QlGJMDwMtGnwZXAz98LgeylunlQONUG52ubIlPh9zrmy7XQVZ3DyxON2Ned-9rCYL-6ZWloZ1kvEq3RQiyWdVO-aAA9t5Qz5uLjVUrimpFyJfn3gaz_0f_8SafsaajyC5xPVpkklaooVrnhgDMeJleo82rmzkUMEAnDLivK-eJzhnm-6KBn2SyU2jmLfonV3JszEq4Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به یکی از شرکت‌هایی که API می‌دهند مشاوره مارکتینگ می‌دادم. چند راهکار برای کاهش هزینه جذب مشتری یا CAC گفتم، ولی تاکید داشتند که باید API‌ رایگان هم بدهند. پرسیدم چرا؟‌ خیلی راحت گفت: چون رایگان است، طبق شرایط Privacy & Policy تمام پرامپت‌ها و داده‌ها و خروجی را می‌خوانیم و ذخیره می‌کنیم. فکر کردم شوخی می‌کنند. بعدا دیدم نه. جدی است.
(...)
مواظب باشید، لااقل اطلاعات حسابداری و مالی و مارکتینگ و اکسل فروش و لیست مشتریانتان را به این API رایگان‌ها یا این سرویس‌های هوش مصنوعی حتی پولی که در ایران هست، نمی‌گویم ندهید، می‌گویم دقت کنید.
©
AdelTalebi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/ircfspace/2489" target="_blank">📅 07:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2488">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BNuWwDkLWMBpyW5GnHsaWkrz4NqWF82ufAatuuAVGMwD_leQhQiCNOmVlHplbgV6Ad1cBeMVga0ahwyGMoOlIH-CBwUD8Sg70QvZyjZcqVkR07wudlaIyvOtI9Xb5cwzmjmhZMT55UI5JK6lGjaV-y8KOjcp_DESFosHaQAepvpG_zPG2fXtN9N3GDpSeTxuYOCUHQay7ONTlToxssw9DtDtRq4QhKdKUehBp8MGBpxSuJAVZKZ07BjSrubk-0wElI7AsXkzlOHlRB7FDemA7Yhe7pGygcYbg_QOmxz4PujwLzxZHkRt7GN8JrrGGzgRASkQ0CVB-ciUmSg_4EI2fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروتون در
یک مقاله
جنجالی ادعا کرده ویندوز دارای شناسه‌ای پنهان به نام GlobalDeviceId (GDID) هست که میتونه یک نصب ویندوز رو بصورت پایدار شناسایی کنه. به گفته این شرکت، این شناسه حتی در برخی شرایط با وجود استفاده از VPN هم میتونه برای مرتبط کردن فعالیت‌های یک دستگاه به کار بره و حذف یا تغییر اون برای کاربران ساده نیست.
پروتون با استناد به یک پرونده قضایی معتقده مایکروسافت درباره وجود و نحوه استفاده از این شناسه شفافیت کافی نداره و به همین دلیل از عبارت "ویندوز یک جاسوس‌افزار است" برای انتقاد از سیاست‌های حریم خصوصیشون استفاده کرده. البته این عنوان بیشتر یک موضع انتقادیه و نه یک نتیجه‌گیری فنی قطعی.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/ircfspace/2488" target="_blank">📅 07:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2487">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">بانک ملی اطلاعیه زده که "کلیه خدمات بانکی و مالی این بانک شامل همراه بانک و اینترنت بانک مجددا فعال شده"، اما ایسنا نوشته "اعلام بازگشت خدمات بانکی به شرایط عادی، لزوما به معنای پایان مشکلات برای همه مشتریان نیست و گزارش‌هایی از تراکنش‌های ناتمام، کسر وجه و اعلام زمان انتظار تا ۳۰ روز کاری برای تعیین تکلیف، نشان می‌دهد بخشی از کاربران همچنان با پیامدهای اختلالات اخیر دست‌وپنجه نرم می‌کنند".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/ircfspace/2487" target="_blank">📅 17:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2486">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">طبق گزارش‌ها اینترنت در برخی نقاط کشور از ساعات گذشته با اختلال و کاهش سرعت همراه شده و دسترسی به برخی سرویس‌های آنلاین با مشکل مواجه است. همچنین گزارش‌هایی از قطعی‌های مقطعی و افزایش خطا در اتصال به خدمات اینترنتی به گوش می‌رسد.
©
IRRadar
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 94.7K · <a href="https://t.me/ircfspace/2486" target="_blank">📅 20:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2485">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DhUU7bfQuHxXiOp0Je_5bmfwSAuDlzwUHt_ld1q5KD7Tt2mlrBq-My6a_3-WhEXuQhjVAjgPNdFhUTup373vfGTEW1bO48Bf-fN2Cn3-eo08wJB2DygIANOLmDtISywaYi_JODlKxz7M9FRQzZAWL9D1x-_RC5VjZEE4_80SGKo7nhRubFl8VudXyBuntN-a15oCe7jbSchWfZEjhzr9Fv1ZRti80Dywv9bvPxxI0QMg_6-VDBA17xHBbAzmYQVvjAmJWTZ_1ICPc3GBxfz3RaXw82zWmD6HWh-2OKFTfyLKt_G1ZmqQ903NQKSUIXFVCAPsGcuxhlnJI-TnuNna6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن JumpJump که بارها نام اون در گزارش‌ها بعنوان یک اپ ناامن مطرح شده بود، حالا یک محصول پرریسک دیگه با نام SpeedTop VPN منتشر کرده!
این برنامه با وجود چند میلیون دانلود در گوگل‌پلی، طبق بررسی‌های فنی پس‌کوچه دارای موارد نگران‌کننده‌ای مثل وجود تعداد زیادی ردیاب، درخواست دسترسی‌های غیرعادی و کدهای مرتبط با شبکه P2P هست، که می‌تونه دستگاه کاربران رو به بخشی از یک شبکه انتقال ترافیک تبدیل کنه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 88.4K · <a href="https://t.me/ircfspace/2485" target="_blank">📅 08:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2484">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jDIkJ4DlqbmevjEJGz2XWVLftTZFFJpiLAmN0fq65rwJYZ0uyc8D2akmVqrmf5SmwvoJLSPHRXuYQVzBqa_nhmLwxOD_gKXttkb6JioXPiwvDEBpYOBowSgq_Eulk7zgfVMRLWXtNpyVknGQqXjXgkAtFSqNE2VlcdtmQwRckXLzScT0cJo91q_tPqf-jAnovt7Qrl7A5U_CDiFnsf7VEW0Vf76ZPp6HGN27ATtcmob1QwXMSEyjNLAmMHNYzWfTdqT-2U_nY2vuyT2h3GThPErdwGwi5xmWcbhOlJSVi6Fz6rQBlQSOmtt0xmZVHZlkNPzla4Ca7vAaunxm_C5R8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنل زئوس یه ابزار متن‌باز برای ساخت فیلترشکن رایگان روی بستر ورکر کلودفلر هست، که امکاناتی مثل آیپی و لوکیشن ثابت، دریافت خودکار آی‌پی تمیز، لینک ساب و QR Code اختصاصی، فرگمنت، شبیه‌سازی فینگرپرینت، بکاپ‌گیری و ... رو بصورت یکجا در اختیارتون میذاره.
👉
github.com/IR-NETLIFY/zeus
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/ircfspace/2484" target="_blank">📅 08:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2483">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V39m-X7oAzLwDlrKyYZ26lFPwrjWQ4EUzGcc_8QTF_JxqC-9lmugNQxryM7Uo596XvGeIDibhHRsBjsEnOVWHJhjnibR5RgogS9GRYcxE1MCL1cEVuNAmU1tqMZnqq7o-yXndaA-JlbjznhpYGvzhKmRrWmETR3A7yzlb_O_ww1GdxgEf16SlRkLCuicNeoIMz7w8nEPs1oNmv2q5Fh0z1apifqSDv2NghmmVYzxWcnuaXsRALV8MDYUeMCKxGxsjOizKyz53GBPhQfGwXUwihTbk30LytaZmwFJydiXrE2kEvCQUDneSg3tqroZxK3aH4pTfskFnd25UA3TY8bhLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکروسافت یک آسیب‌پذیری روز صفر در Microsoft Defender با نام RoguePlanet رو برطرف کرده که می‌تونست به مهاجم اجازه بده تا با سوءاستفاده از یک نقص Race Condition، سطح دسترسی خودش رو تا SYSTEM بالا ببره. این مشکل با شناسه CVE-2026-50656 ثبت شده بود و حتی روی ویندوز ۱۰ و ۱۱ کاملاً آپدیت‌شده هم قابل سوءاستفاده بود.
©
bleepingcomputer
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/ircfspace/2483" target="_blank">📅 08:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2482">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/H96Hv8B7H-fvfsZupt6TWj1FhJj-koSZmVwDsKEjcDRkyVugvFOWf9HOMsxyCd5gvKWnU5hkpRjIrPY6Ln90aOXna1-GCuL_Nl8TzQNVUs_qCMvV9XuZsyyGpltDTVLcRri7ZOIONTiMukJQAhigbAY8lPEoOSiSsOc7gFXfPoW1fP3uKUcEEKe85ipnhgB2NTm0F_IVDUuOxkPXczwLvJwtVpzRglqgofbR6fGv1xrlCJ05IAjhlbNAtOk7jdvSqHzvo6Q7xjK7pPZdrXe0d9wtoTn6oALK7b-V6Zpb9e5w1Dh9JhMyUzuyeo_by--GbgR9HbzvHSqSyvBU3es4vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت اندروید NipoVPN که برای اتصال به هسته این پروژه و مخفی کردن درخواست‌های HTTP داخل ترافیک عادی وب طراحی شده، حالا روی گوگل‌پلی در دسترس قرار گرفته.
👉
play.google.com/store/apps/details?id=net.sudoer.nipo
💡
github.com/MortezaBashsiz/nipovpn/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/ircfspace/2482" target="_blank">📅 08:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2481">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mKzWhkKLgzgauDKMbVEQihcGIvr-4FnFeOFpflcYyYPKMdUxDKL1Lv_XmuwotXMgEzBfpVuQduwX3EpQ59nAm1COAcZ079ap8d0oXDj7kO6fdJtlpKsLhFLXKwgPBPjBxXqda-se2LHzc5phsdNXBeneW4SbbKNFx5BoJyiBpVSGU-6Mm_AcljzLHN_a-vlpMOHRk1DBq49FJOnp80dyuYefn9tA43hyMv1WOTQ9V8yO5pwDo_8FSShn0egxkshd_F057VpS7S6yyWMaIaXbA8r4hYrwNNbd86OykSs6-DwHH40mNpSRECqvG0PQ69JwvqdR7f2RJtC1p_9UuiBrkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابزار BG Scan یک اسکنر متن‌باز و رایگان برای پیدا کردن و اعتبارسنجی سرویس‌های شبکه هست، که اجازه میده چند مرحله اسکن رو به هم وصل کنین و عملاً خروجی یک مرحله رو بطور مستقیم وارد مرحله بعد کنین تا فرآیندهای پیچیده راحت‌تر انجام بشن.
این ابزار از پروتکل‌های مختلفی مثل ICMP، TCP، HTTP، TLS، DNS، DNSTT، Slipstream و Xray پشتیبانی می‌کنه و علاوه بر اسکن، امکان اعتبارسنجی و مدیریت نتایج رو در اختیارتون میذاره.
👉
github.com/MohsenBg/bgscan/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/ircfspace/2481" target="_blank">📅 08:08 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2480">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VnNdS2WLSTuXt3oK64eKvYAzdYKhmrcSicRPaxF9i9_PKs-5hQTIgQDgOmH5cZnyEJlwU4n8Lv8lUztKLncj7CzftR_SUjcxyzxFQ62m7q89l1ceQv1sinHTbubJP7HYnGz8-rifO9Pk_WjrBXjMIaMGvlo7ATaNel3KprhRfiC88Sai6szELK6svPX3FJW2HtVSCHvNp4G1iyDHh_G2UvjHd5lqLD-tmIz6_d7SKNzkgP7_r7MxdDcrfiwiLzJSKS5gao-oUhtDf_n0h7tKCGzitXYe1UZSZ7zFA47sGcWA4qrS4Btd8DdpbtWPzTUUYvU5quY6-lFCZSUStoYZYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاوه یه ابزار برای اسکن، استخراج و اشتراک‌گذاری کانفیگ‌های فیلترشکن هست، که کار پیدا کردن کانفیگ‌های سالم و به‌روز رو راحت‌تر می‌کنه. این وب‌اپ میتونه چندین کانال تلگرام رو همزمان اسکن کنه، کانفیگ‌هارو بصورت خودکار استخراج کنه و در نهایت یه لینک سابسکریپشن بهتون بده تا مستقیم داخل کلاینت‌هایی مثل v2rayNG، v2rayN، Hiddify, Streisand, v2box و ... وارد کنین.
توی کاوه می‌تونین کانفیگ‌های خودتون رو با بقیه به اشتراک بذارین. علاوه بر این، حذف خودکار کانفیگ‌های منقضی و امکان رأی دادن به کانفیگ‌ها و منابع از جمله قابلیت‌های این ابزار رایگان هستن.
👉
kaveh.yebekhe.workers.dev
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/ircfspace/2480" target="_blank">📅 08:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2479">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/B6odvy0h69eMfmAyY75iAWdLsXw42iGF3Zw1P4oBO0lSBxG4Txty9mlBCSMA0NFy4cQd2gZp9CgohFojvyd-A6fqLxsCwAya7d51dfuulXmSm75sKfuHLHrSpZMSt3VfAbBmyGQ8-xZsHJZHiLn_tBLyO4dj5m7cAyDazeCWCCw1spEPTlQh-b-oOldCbKLFNgxZ_pOFnwzWF8ph-iaoMwj3X0XRfJVuSCzFw1aXRmJ4UMOA9vhk-ROciHvzNeHEapEd_lZtrp0NOFavQJw_RAgFQOFeDYKbr2ETvE48HVujBwT4K2u_HSFuZNM8Wqv5sFBdL8GKx5bEOhw7HTZLag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ابزار MTProxyMax آپدیت جدیدی منتشر شده که توی اون از بهینه‌سازی‌هایی مثل BBRv3 استفاده شده تا عملکرد سرورها بهتر بشه و مصرف حافظه هم روی VPSهای ضعیف‌تر کاهش پیدا کنه. همینطور در این ابزار که برای مدیریت پروکسی‌های MTProto تلگرام روی سرور شخصی هست، قابلیت‌های جدیدی برای مقابله با DPI و اسکنرهای شناسایی پروکسی اضافه کردن تا شناسایی و مسدود شدن سرورها سخت‌تر بشه.
👉
github.com/SamNet-dev/MTProxyMax/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/ircfspace/2479" target="_blank">📅 07:49 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2478">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S3J9BwC_Yj--xDVjLeahSyhlhOWAfjMOIRY942p8GgULWFGoOu_YDDmijFTAFoxnbwNqzv7gZPTreTKMdUl_oEixcZMuFJpNDvzI3uGFQXIG7uENN0CnDYha8G_8pzhNkbxCPUolKurti8jIYs6RuZq9vetrrhHObcSrUm2KT4x7gy5-4S9ozv0XMT1lfv_3tcr2KvavQL9q8Q8JhkBEQeN6tAOuKizmxzZ7uZoswyXKgf8duERN_lmQpa9RjFPQ5AAe0rQlWnr5ittIFpnqtFvCgKr5OMxhPKLiAFQK9oXqnBrr6iMB8mGZZMa3XZlRxEmGvcLnaNyhFXQy2_Wtdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Intra با استفاده از فناوری DNS-over-HTTPS (DoH) درخواست‌های DNS رو رمزنگاری می‌کنه تا اپراتور اینترنت یا هر واسطه‌ای نتونه آدرس سایت‌هایی که باز می‌کنید رو دستکاری، مسدود یا به مسیر اشتباه هدایت کنه.
این برنامه فیلترشکن نیست و آیپی شما رو تغییر نمیده، اما چون جلوی سانسور و دستکاری DNS رو می‌گیره، در شبکه‌هایی که فیلترینگ از این روش استفاده می‌کنن می‌تونه باعث دسترسی به سایت‌های مسدودشده بشه. علاوه بر این، رمزنگاری درخواست‌های DNS تا حدی از کاربران در برابر حملات فیشینگ و برخی بدافزارها هم محافظت می‌کنه.
اینترا توسط Jigsaw (تیم نوآوری گوگل) توسعه داده میشه و سورس اون بصورت متن‌باز روی گیت‌هاب منتشر شده. این اپ از طریق گوگل‌پلی در دسترسه و برای استفاده ازش فقط کافیه یکبار فعالش کنین، تا در پس‌زمینه کار خودش رو انجام بده.
👉
play.google.com/store/apps/details?id=app.intra
💡
github.com/Jigsaw-Code/Intra
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/ircfspace/2478" target="_blank">📅 07:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2477">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NhfQCHgSGuTkZd9Ty-SAVU7TOKSa_-AyVCQobaACaLHcrmWqxMp4h7G2idnKUeU_1gO89pspMZYhbkDqpsiLt7V_GEdMmXbmO6NVmsKo9TOFOP2cNuo7aKwbGB2_Fux_1kOIYQH17EgasaBNsgszO31qoMgtNkO3KIVZYJxCv1V2mKC6Xa3Auqb3C7Z1MIjeVSQK-MKf8t3u-1rNilQIr-ZOjZekcIQHyR5KHPYwTHG5ugc6hFNzxVRocB8GCkvqIF3cgKtnRIPKBUn5rO3bIguDPOJdoeCeBL3oEQKiKY96s0qcFi77mGWvkyRvBEI8ySwwGF-GuY8_wNXbZEnR_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محققان Datadog میگن مهاجمان با استفاده از بیش از ۵۰ حساب قدیمی و غیرفعال گیت‌هاب و توکن‌های دسترسی (PAT) افشاشده، از طریق API گیت‌هاب در حال جمع‌آوری اطلاعات سازمان‌ها هستن تا برای حملات بعدی آماده بشن و ساختار داخلی، اعضا و ریپازیتوری‌های اونهارو شناسایی کنن.
توی بعضی موارد هم تونستن ریپازیتوری‌های خصوصی رو کلون کنن. به گفته Datadog، چون این کارها با حساب‌های واقعی و API رسمی گیت‌هاب انجام میشه، تشخیصش از فعالیت عادی توسعه‌دهنده‌ها کار راحتی نیست.
©
thehackernews
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/ircfspace/2477" target="_blank">📅 07:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2476">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oexKBThL0i_upVW_JF2p5vJ-j2-5u9-2U_wjmjpNbqkhuTVlBZUZsrmsFtvWtpHOBtUntolHonaZvV5lVWrgrfT8Ryt0DP3s5-X6dhv45DCDiRJ82qZ0-gq_GUeUX12MI7n1mDIk03rMm4sdrTctAXC65OoUJMbZgZmUpP5WbLlMLWdcr2dcXGwfN05eMXKdSRkFT0TZsNMaJ-fJIJL6ELfSaKier166fx3TYxQ4rc1dVk76N6HgmyZ_CW1cQv0I9J62RRizwHjzqnH5WmS5dsUewkS37meMHS_pr-LXbmqG_RE0YtWHxDXOPyFkDI2D8Ofk_K5ELuD0mpXMX93UCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایک سنتوناس، مدیر ارشد فناوری شرکت CrowdStrike میگه خیلی‌ها دارن روی این تمرکز می‌کنن که "کدوم مدل هوش مصنوعی خطرناک‌تره"، در حالی که تهدید اصلی جای دیگه‌ هست. مشکل واقعی اینه که هکرها حالا با کمک هوش مصنوعی می‌تونن آسیب‌پذیری‌های قدیمی و جدید رو ظرف چند ساعت، و بزودی شاید در چند دقیقه، پیدا و سوء استفاده کنن.
به گفته او، هوش مصنوعی بیشتر از اینکه باگ‌های کاملاً جدید کشف کنه، باعث شده هکرها بتونن تعداد زیادی ضعف امنیتی شناخته‌شده رو خیلی سریع به همدیگه وصل کنن و ازشون برای نفوذ استفاده کنن. یعنی اگر سازمانی هنوز وصله‌های امنیتی رو نصب نکرده باشه، حالا خیلی راحت‌تر از قبل هدف حمله قرار می‌گیره. هوش مصنوعی لزوماً حمله‌های جدید خلق نکرده، ولی سرعت و مقیاس سوء استفاده از ضعف‌های امنیتی موجود رو چند برابر کرده و همین بزرگترین تهدید امروز امنیت سایبریه. /اکسیوس
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/ircfspace/2476" target="_blank">📅 07:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2475">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZkFfbLS-T41LCoDeE7iEz9KZAO5aIUfC1wnowXHlSomAi6DMpEdaVO_nTjacK5gY2mLmNtDUU1LhqVsGnmfNsjxB2dh4Q4X_7dIBAeEjmgwJd-pN2uEqHj0HecGSiTygS5Wd-_ZF9K1nwmhBqhBtlJ7wXGseh7TMCqEU2-C74Il_hiIBGzt1nEmpjsPUajYh1YhWS-35MHNo_Oom5JiOmu47-tp5oO6VDPy9gUUsb5RaD1lxdepIPlXITkpvLlbi4gVALm68PGx0ZyGeTQOYjVoivOniUJrpI2K8mI1GN1XAHGScyFuySsB_4iANlVYfCY8SHW-qh7g98xnsAX5JpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ GRoute یک کلاینت متن‌باز و رایگان بر پایه هسته ایکس‌ری هست، که امکان استفاده از پروتکل‌هایی مثل VLESS، VMess، Trojan و Shadowsocks رو در کنار ترنسپورت‌های مختلفی مانند REALITY، TLS، WebSocket، gRPC و XHTTP برای دیوایس‌های اندرویدی فراهم می‌کنه.
این برنامه از قابلیت‌هایی مثل اضافه‌کردن کانفیگ وارپ، مدیریت لینک‌های ساب با بروزرسانی خودکار، مسیریابی تفکیکی، پروکسی برای برنامه‌های انتخابی، فرگمنت، Sniffing، نمایش لاگ‌های Xray، اسکنر آیپی تمیز کلودفلر، امکان تست کیفیت اینترنت، بررسی پینگ واقعی، تاریخچه مصرف دیتا و ... برخورداره.
👉
github.com/SuOracle/GRoute/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/ircfspace/2475" target="_blank">📅 08:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2474">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">آموزش راه‌اندازی پروکسی تلگرام بر روی سرور شخصی ...
📽
youtu.be/pyvB6VSPhwg?t=176
💡
github.com/SamNet-dev/MTProxyMax
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/ircfspace/2474" target="_blank">📅 08:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2473">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s9OqfCdtXxrjO_7LSLXvwy5cY5sOjHscxTvwNrf4wHXcp0MwDogLnnuiHbWNVUGeslEdZw41nrVDj2WephbBI5sNSD2Bv7MFG_z_Lxw2xvw1azMlj9OZvpsxv_3WAsyxmJuB80n2fkCNu65_cIGeGx6OeFN97ZHTl45-dM-vzc2p2v1tdNTWTuSS3Ais2N0mE6QZwbpTdAIbI_WFPb3xvH0ROnjtqWyNqGJrRLwDEinrMpq91W-cMxUBINhwilv3VkXtYVF1JxvV0eRJ4Lqul0L7pO9eZfD3lNeQXhktKUi2rbd6VaLgQJAsPMt9Lic7ged6dawUkhlo3I_PV-DumA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکنر سیمرغ یک ابزار متن‌باز و رایگانه که برای پیدا کردن آیپی‌های تمیز کلودفلر در اندروید و ویندوز ساخته شده. این برنامه میتونه آیپی تکی، رنج‌های CIDR، رنج‌های دستی و لیست‌های آماده ISP رو اسکن کنه و بهترین‌هارو بر اساس سرعت و تأخیر بصورت رتبه‌بندی‌شده برگردونه.
👉
https://github.com/rezakhosh78/SIMORGH-Scanner/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/ircfspace/2473" target="_blank">📅 07:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2472">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IVTAa_73TnIRU4Y--HOIFwvW8sjyr-zLqZh6F_wMCMJ_adP0crEt6EADKHfFoOtwE_WpEgC5-MqRr8N2h1bdOlg0qPXiNiTkH_Leh62_Sa23UNyp_PlcnOxosAz0NfDhFOEd7KVkHmWBAg_f5baIHZlTobnKHeRNdVIKThE8JShtQzjr3mopaAinG7nXI80-p54y3-Nhb5ruCc_lTVSqLZVg3ZkV9KHtnMV4Z54wHjplxEGiW0YuQVa6aybQVPabtgPC1QXHAISqQCnL61CEJ7Wd33pDr6oOtBxuMM1hAjEtCzkF8uQcXgz_7Ighq-KWM9d6mjVTzlI3hwsIcS_1Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکنر Asha یک اپ متن‌باز و رایگان برای اندرویده، که با تمرکز روی پیدا کردن آیپی‌های تمیز و پایدار کلودفلر ساخته شده و کمک می‌کنه سریعترین و مناسب‌ترین آیپی‌هارو متناسب با شرایط شبکه پیدا کنین.
حالت‌های مختلف اسکن، بررسی لیست دلخواه آیپی، شناسایی دیتاسنترهای قابل دسترس کلودفلر، امکان تست سرعت واقعی از طریق پروکسی و استخراج هوشمند آیپی از وبسایت‌های پشت کلودفلر، از جمله امکانات این اسکنر هستن.
👉
github.com/ashanews9776-eng/asha_scanner/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/ircfspace/2472" target="_blank">📅 07:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2471">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">نسخه ۱۷ از اپ
#MahsaNG
منتشر شد و توی این نسخه هسته سایفون بصورت ویژه برای شرایط اینترنت ایران بهینه شده. همینطور امکان ساخت، وارد کردن، خروجی گرفتن و اشتراک‌گذاری کانفیگ‌های
psiphon://
هم اضافه شده و یک اسکنر IP جدید برای CDN Fronting طراحی شده تا پیدا کردن آی‌پی‌های مناسب راحت‌تر انجام بشه.
امکانات جدیدی هم به خود برنامه اضافه شده؛ مثل دریافت کانفیگ‌های ایکس‌ری از طریق نوتیفیکیشن گوگل، قابلیت زنجیره کردن دو کانفیگ و حذف کانفیگ‌هایی که موقع تست پینگ توی ساب فعلی پاسخی دریافت نمی‌کنن. رابط کاربری بطور کامل بازطراحی شده و جابجایی بین ساب‌ها با کشیدن صفحه به چپ و راست انجام میشه، مدیریت ساب‌های بزرگ بهتر شده، شماره کانفیگ در حال تست نمایش داده میشه و از این به بعد خود اپ می‌تونه اعلان‌ها، اخبار و بروزرسانی‌های پروژه رو مستقیم به کاربر نمایش بده.
توی این نسخه مشکلات مربوط به اتصال مجدد و کرش سایفون، ایرادهای ویجت، باگ‌های CDN Fronting، کرش نسخه ARMv7، بازیابی نشدن رمز عبور HTTP، وارد کردن لینک ساب در بعضی شرایط و چندین مشکل دیگه هم برطرف شده، تا تجربه استفاده از این فیلترشکن پایدارتر و روان‌تر باشه.
👉
github.com/GFW-knocker/MahsaNG/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/ircfspace/2471" target="_blank">📅 07:58 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2470">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">یکی از نکات جالب اختلال ادامه‌دار خدمات بانکی اینه که هنوز چک کردن موجودی از اینترنت‌بانک با مشکل مواجهه، ولی پرداخت قسط با قدرت کار میکنه. در کل هرچیزی میخوای از حسابت برداری، به خاطر هک به مشکل خورده، اما هرچیزی میخوای بذاری، میگیره
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/ircfspace/2470" target="_blank">📅 07:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2469">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">مخابرات قیمت اینترنت ثابت را سوسکی بیش از ۵۰ درصد افزایش داده و آن را به بدترین شیوه در محدود کردن کاربران و تغییر ویژگی بسته‌ها انجام داده است. مثلا اینترنت ۱۶ مگابیت قیمتش ثابت مانده اما در سرویس سه ماهه، بیش از ۱۰۰ گیگ از ترافیک آن کاسته شده (۳۶۰ گیگ به ۲۵۵ گیگ).
حالا شما اگر بخواهید تقریبا ترافیک همین بسته را که تا ابتدای سال عرضه می شد بگیرید بایستی ۱۰۰ گیگ ترافیک بخرید که قیمت آن بیش از ۲۰۰ هزار تومان است و در واقع همان کلاس ۱۶ مگ سه ماهه با ۳۶۰ گیگ از ۳۰۰ هزار به ۵۰۰ هزار تومان تغییر کرده است. انتخابها هم محدودتره و برای ۱۶ مگ یا همان ۲۵۵ گیگ را باید بگیرید (و بعدا ترافیک جدا بخرید) یا انتخاب دیگر ۸۸۲ گیگ است که قیمتش بیش از ۳ برابر است!
©
alirezashirazi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/ircfspace/2469" target="_blank">📅 07:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2468">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dU1iDBqmKkX-jE6SHKSGkmRWwrU6VwWXXlf71ahAn3KDsoWm8jS4BF2R0oe09SiJIzEUFQf1vUQZ1AyShUyycS2am-JLg-zuO94uWIDDhOowtg0DYhDxVzIRHOB93rno3J_B4jqRuXVnSKT-HAu4KRUp1w9hzuhZcb8M_rwbSi6qAjYSqdxOZsomtBdHVeAvKmHnwPDuaEz4xCq8Sew_SiejFEBMMRHqi90MKaIdBDQZO2zeUhTX1p91iZrj6Mg5N2Z9sSfuh8C1upzLnR3yYQk3g-FybRVFCDn-FL_PU8XL38WNZOHF1w6T_Rq942YgPDPdcINCbq91M2BGWvujOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات (که به تازگی بابت عملکرد درخشان وزارتخونه در دوران جنگ ازش تقدیر کردن) گفته "لازم است با وزارت نیرو برای خارج شدن سایت‌های ارتباطی از اولویت قطع برق تفاهم شود".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/ircfspace/2468" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2467">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">گزارش تحقیقاتی
HalcyonAi
نشون میده شرکت
ابرناک
(مالک جدید دامین ویکی‌تجربه) مستقر در تهران تحت پوشش یک شرکت آمریکایی به اسم Cloudzy مشغول ارائه زیرساخت فنی به هکرهای حکومتی کره شمالی، چین، روسیه، ایران و چند کشور دیگه‌ست. زیرساخت این شرکت برای ۹۰ روز زیر ذره‌بین کارشناس‌ها میره و مشخص می‌شه نه تنها گروه‌های هکری حکومتی، بلکه گروه‌های باج‌افزاری از جمله شرکت تحریم‌شده اسرائیلی Candiru جزو مشتری‌های این شرکتن و بین ۴۰ تا ۶۰ زیرساخت‌هاش به فعالیت‌های مخرب و مجرمانه سایبری اختصاص داره.
آدرس خارج از ایران این شرکت (که قبلا اسمش Router Hosting بوده) به دو کشور قبرس و آمریکا منتهی میشه. نشانی آمریکا به یک مرکز خرید در ایالت وایومینگ می‌رسه که آدرسش با بیش از دو هزار شرکت دیگه مشترکه. ثبت‌کننده کلادزی در آمریکا شرکتیه به اسم Cloud Peak Law که تخصصش ثبت شرکت ناشناسه.
گزارش تاکید کرده بعیده مدیران کلادزی یا همون ابرناک ندونن که بیش از نیمی از زیرساخت شبکه‌شون داره برای کارهای مجرمانه استفاده میشه. این شرکت در واقع به عنوان command-and-control provider به هکرها فعالیت میکنه و برای استفاده ازش فقط داشتن آدرس ایمیل و رمزارز کافیه. ابرناک در ایران در سال ۹۹ با نام «آلان فن آوری ابری» ثبت شده. دانش بنیانه، بسیار هم فعاله و در حال حاضر ۳۴ فرصت شغلی باز در سایت جابینجا داره. مدیر این شرکت محمد حنان نوذری به رویترز گفته فقط ۲ درصد از زیرساخت‌هاشون در اشغال فعالیت‌های مخربه. همینطور گفته نباید چاقو فروش رو مسئول خلاف مشتری دونست.
دور از انتظار نیست اگر اسم این شرکت و عوامل اصلیش رو توی فهرست تحریم‌های آینده ببینیم. ابرناک حساب‌های توییتر، اینستاگرام و لینکدین خودش رو غیرفعال کرده. نکته آخر اینکه غلامعباس نوذری که در شرکت ابرناک شریک محمد حنان (احتمالا پدرش) هست، دیپلمات ایران در نیوزلند بوده. حنان هم در پروفایل لینکدینش به تحصیلات در نیوزلند و در پروفایل کوچ‌سرفینگ به ۱۵ سال زندگی در این کشور اشاره کرده.
©
arashzd
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/ircfspace/2467" target="_blank">📅 08:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2466">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ISwI8yA2gxGKSt-wcrbWJK5AbaRHP2S-8D3HFi5p1CUQFyT36l1SybP4-3QUBEyKi34L4NqS4Bv2-N-Ts1yesuSgaISbEY_pNltxZmpk2-E_C6NGrERymlTVA5vwuzX16YgBa2hXohzeFQGED4G9FZXPFQZXGG6NNz3GqVWYaM4iMpE-e6zDeNrJK_5VxJ1pUVGwzmpArviEbHRqIOP-Nh7iM2ga9BvHieNa8_0WAKMq2gEk5rUByvUAoFjKJsnsWvUnPe8gXvoiF9oIPgVimUlFfBDTnIBLREdPTxMVe3ts-5PFhJ-lPfZOs1gWY3eNYPD1NpBeJtz92W1HTLFIxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران از رتبه‌بندی جهانی اسپیدتست حذف شده. شاید فکر کنید چون دیگه حتی ته جدوله، رتبه بدترین اینترنت هم توصیف مناسبی نیست، یا دیگه زیر ۰ و منفی جوابگو نیست.
نه، چون چیزی که داره ارائه میشه اسمش اینترنت نیست!
👉
speedtest.net/global-index
©
Mehrdadlinux
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/ircfspace/2466" target="_blank">📅 08:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2465">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Rejq14LNTJMl_lS7ybzODEFA9JX4brD2oDmfpRK5G3efgzJkHgZJUH47iayX2irWEtvg89xE7pKLPQBK4KbsIbkb7V6l0Bv02FW_fyFdXARS8Opz61VAppQrzWCFZkoDZY8SoJH0p2BnFa28XpbcjClGTIo1qvWBTrAkt4e_OntNt7CThK-FCqo4QOO0TMqcpv6O_9HI-zBBdROaMQsFYSW0_dQ-C6eLlQueMnJn04wGTX68sPwzYQfQkeTeWukshgDiYtrYuc9QpDn8eRkxSQjxWMLnYxT3JJ1RcXAbVz647a0udvbXWmh-2bKZDwVVuiUlCZlux5T5KMqEB8vhgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در این چندروز احتمالا در مورد اکانت ویکی‌تجربه و سرنوشت نامشخصی که برای مالک ناشناسش رقم خورده چیزهایی شنیده باشین. متاسفانه دامینشون رو در ایام جنگ و قطع سراسری اینترنت نتونستن تمدید کنن. بعدش این دامین توسط ابرناک ثبت شده و با یک پیام مسخره و کینه‌توزانه، صفحات سایت تغییر پیدا کرده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/ircfspace/2465" target="_blank">📅 08:22 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2464">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ix6neB35FS21edvYxrorph2htGNnJfH_4zmapn8Ph6YlKHLxfSq2ZDRt79_f8SSrRZP81oXZNwryd_ExBxq6wCq_5SG8YzX0EiAnkV0k2Z0VJZD_N2WAyRYTqNQgIXuH3Fja1nLmftPxM2kGjFR2zMh-9nXe-SXsDSczpzvPahokQW4tSNK3JZ9eNX4LtJXhzkrKgeVN9TVGDWa_pJl_Nl2j1LAVesQ2VC4DuGoP_qr6uHgIL50NYNcZ7N5Umi0-BNkAJKTPeLdgp4V9DOImRW3o7nf0IqCb_rj2lkF6MKe484x_E2GubJEMP_g8fa28oqMRD6CyWh9G7Es8Pmt8rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر از
#لینوکس
استفاده می‌کنین، فیلترشکن دیفیکس در جدیدترین بروزرسانی خودش پشتیبانی از این سیستم‌عامل رو اضافه کرده.
👉
github.com/UnboundTechCo/defyxVPN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/ircfspace/2464" target="_blank">📅 12:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2463">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QxPpX-Su2iWFf8od0YkZZjHNg8gwMzeKTeu_jebrQNAmf1Kjjt6fLN_ebsl-yLiZoOKnHtGCk012DFHfa-9MeyhMTk1jXEyB-DwePs2CjejG9pbZm0SFMflI9xRe7WEGO5toPrYZcoaSPX2syl4ylIUXs_RBk6FPLrhpX_o6ROqAjbh1vuFyTt7VuOKeB1G9xCIgKJSfGVNPRpeSVyaGzDawqNNaeXg3j5v4wuF3ODiJ8YpkqP6P0_nd-rYvU-uCn0f4Kl3YM3G5HHAotDotrCAszUQVowq6Pk6j-AEYNGvQlo5UMD_XOTEe7MzqfllZnvrvIXnMLQXiSJxwllRSgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ RedCloud VPN یک کلاینت متن‌باز و رایگان برای ویندوز و اندروید هست، که با استفاده از هسته Xray توسعه داده شده و امکان اتصال از طریق کانفیگ‌های VLESS، VMess، Trojan و Shadowsocks رو فراهم می‌کنه.
این برنامه تمام ترافیک دستگاه رو از طریق تانل‌های رمزنگاری‌شده هدایت می‌کنه، از قابلیت اسکن و سنجش همزمان IPهای کلودفلر هنگام اتصال بهره می‌بره و همچنین با استفاده از قابلیت Sniffing، ترافیک HTTP، TLS و QUIC رو شناسایی می‌کنه تا عملکرد اتصال بهبود پیدا کنه.
👉
github.com/Devtahas/RedCloud-windows/releases
👉
github.com/Devtahas/RedCloud-Android/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/ircfspace/2463" target="_blank">📅 07:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2462">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">بانک ملی از اختلال مجدد در خدمات کارتی خودش واسه ساعت ۲۲ تا ۲۴ روز جمعه خبر داده بود، که گزارش کاربران نشون میده این اختلال در روز شنبه هم همچنان وجود داره!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/ircfspace/2462" target="_blank">📅 07:44 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2461">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">الان خرید کردن با کارت بانکی مثل دستشویی رفتن شده. اول باید چک کنی آب وصله، بعد کارتو بکنی؛ وگرنه ممکنه گیر کنی.
©
shokhmatic
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/ircfspace/2461" target="_blank">📅 18:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2460">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">در حالی که با اعلام شرکت خدمات انفورماتیک اختلال خدمات کارت محور بانک‌های کشور برطرف شده‌اند، بررسی‌های کاربران نشان می‌دهد که همچنان بخشی از اختلال‌ها در خدمات‌دهی بانک‌ها برجاست. اغلب اختلال‌های موجود در بستر نرم‌افزارها و همراه‌ بانک‌ها برجاست و این موضوع کاربران را در برطرف کردن نیازها روزمره دچار مشکل کرده است. /ایسنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/ircfspace/2460" target="_blank">📅 18:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2459">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dmPNMY-aqbQqYO-onPY_bgbfgnb2-1qgnPYjV3MnQXd8AOY1HWhp6qthOfMozUK2LfHVK9q7JtLUuC9J0GnD9vz0LsKhXzuFrBFozNwX6ddq5x5H22y4I-erudeAdQCCFPk4XLFlT4E4Mxxfv1a9QMq71vcNeukUxR7jwo0n33EcPGaEjawONHg_hGqcSPj8WVf5H2L3BBiPyKptdDteqZdJqkY8FU-6WOkNPI1va9bgYr4WctCTKNGzcQTiMlCAd5Rv6pQMzBzC9jZwIJFX6cfILCTMVSQrR7FQKFYMhb_95DnBuAW9DL82qmhbm1rX-Lkh3gy1EQnVnzRdlihYiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کمیسیون اقتصادی مجلس طی نشستی با ستار هاشمی، وزیر ارتباطات و فناوری اطلاعات، از عملکرد این وزارتخانه در دوران جنگ تقدیر کرد. /دیجیاتو
بابت تقدیر یه کاسه دادن دست وزیر قطع‌ارتباطات؛ اما بابت ۸۸ روز
ریدن
به اینترنت باید یه لگن بهش تقدیم میشد!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/ircfspace/2459" target="_blank">📅 20:28 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2458">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">خدمات‌دهی دست‌کم ۸ بانک کشور با اختلال مواجه شده. شرکت خدمات انفورماتیک با انتشار بیانیه‌ای، حملات سایبری را تایید کرد و نوشت "شرکت خدمات انفورماتیک به‌منظور پیشگیری از هرگونه دسترسی غیرمجاز و صیانت از امنیت داده‌ها و دارایی‌های مشتریان، در حال حاضر ارائه خدمات مبتنی بر کارت را به صورت موقت از دسترس خارج کرده است". /iranintl
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 91.8K · <a href="https://t.me/ircfspace/2458" target="_blank">📅 16:44 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2456">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">اختلال خدمات بانک ملی بعد از چندروز نه‌تنها برطرف نشده، بلکه این اختلال فقط محدود به همین بانک نمیشه و خیلی‌هارو گرفتار کرده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/ircfspace/2456" target="_blank">📅 13:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2455">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">جنگ شد، اینترنت رو بستن، تنگه رو بستن، آتش‌بس شد، توافق کردن، تنگه رو باز کردن، اینترنت رو بصورت تدریجی برگردوندن، گشایش شد، مسابقات جام جهانی سر رسید یا هر نمایش و کوفت دیگه‌ای؛ ۸۸ روز قطع سراسری اینترنت، سرکوب، اعدام، زندان، شکنجه و کشتار ده‌ها هزار نفر معترض دی‌ماه رو به فراموشی نمی‌سپریم.
خون‌هایی که روی این خاک ریخته شد و نسلی که هزینه آزادی رو با جون خودش پرداخت، از حافظه ما حذف نمیشن. بین ما و شما دریایی از خون فاصله هست.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/ircfspace/2455" target="_blank">📅 09:19 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2454">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R5desuwnOq4JPevoqAEx_i8e6Ohritx6Cfr5wBYAjgFb0H20gOznkbBBF0PdVRSfVTxBgwTOwW5J4mjTj8MD65eBvQKDtvJsWR9jrWppws5buOx9Vyg__twZLVMmLg2BMDVW5rHGSYmBhStqgqp99bLGkpd_NSqzApbn1rxdg4vbTEmbQ0IuvnB8YTfQTqE3wy6nrtNzRsfOr3KlzFxNigEmwQn-p9WnDz_vuIHl-gxq6P_Lt2fyXMbYQ8EEREmflx2m-oudmcj74_fEcUIp1Xfc8tFe73lUbhrj3_dIuA658c24OlBvmp7xNFtjDPYvVEzwUr1YZuOLuGCM7PxnXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنل V2X یک ابزار مدیریت اشتراک سبک و متن‌باز برای VLESS روی WebSocket + TLS هست، که به شما اجازه میده با دیپلوی پروژه روی سرویس‌هایی مثل Render، Railway یا DockFly، برای خودتون و خانوادتون اشتراک اختصاصی با قابلیت بروزرسانی خودکار ایجاد کنین.
این پنل امکاناتی مثل مدیریت کاربران و کانفیگ‌ها، تعیین حجم و تاریخ انقضا، نمایش آمار مصرف، مدیریت IPها، اسکنر داخلی و ارسال گزارش و هشدار به تلگرام رو در اختیار شما قرار میده.
👉
github.com/SulgX/SulgX-Panel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/ircfspace/2454" target="_blank">📅 09:16 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2453">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tguIYRZW07j0rXByer_LO2g3Cfy5D_uPMHfQts_K2rRaIujL6trlk_pg-di1Q7f4YNr4fvIFbgb78Fw6O7THsemPovSYzxu4csipKA4CkiXxVDCQbAxoY2P-GpruGZEaM5HIkS8jcmjhdeIzjY6TKOOVHgCNbVnVF41JVK4b5b2nxSUjTu5lPMneNELqxp32LD_I2L6X4Id3K0IaMKvxyYfheuOyg3DqCK6Sn65nIy7aKRgRLDVLKWAMmKF6GME-DcBfT7N8Zuo5gOc6sRzAZpwMxvuFF90rHLlopB7YxWXwjYWActDsWvuHH4S63IKN7_imWjvSM1OPY6m-w78yyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از کاربران ایرانی به نام MrArrow دو مشکل مرتبط با فرگمنت در v2rayNG رو برطرف کرده، که از نسخه ۲.۲.۵ به بعد این اپ اندروید در دسترس هستن.
این کاربر توضیح داده که "چون تو شرایط فعلی اینترنت ایران Fragment نوع
tlshello
روی خیلی از اپراتورها دیگه مثل قبل جواب نمیده و بین حالت‌های مختلف،
1-1
معمولاً عملکرد بهتری داره و حتی با مقادیر پایین Length و Interval هم میتونه از فیلترینگ مبتنی بر SNI عبور کنه، یه سری مشکل در برنامه وجود داشت".
مشکل اول این بود که با وجود اینکه هسته Xray از Fragment نوع
1-1
پشتیبانی می‌کرد، اصلاً گزینه‌ای برای انتخابش توی رابط کاربری v2rayNG وجود نداشت. مشکل دوم هم این بود که v2rayNG عملاً فقط
tlshello
رو استفاده می‌کرد. یعنی حتی اگر توی تنظیمات نوع دیگه‌ای از Fragment انتخاب میکردی، موقع اجرای کانفیگ دوباره مقدارش به
tlshello
تغییر می‌کرد و انتخاب کاربر نادیده گرفته میشد.
👉
github.com/2dust/v2rayNG/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/ircfspace/2453" target="_blank">📅 09:00 · 02 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
