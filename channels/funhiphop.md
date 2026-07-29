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
<img src="https://cdn4.telesco.pe/file/fNSKPssqGp-J022MFKOn5rqRsVxQHl1yuOtd7MXhLLqKrMZSt1y1C5rHiigsUaoh7ju0inEvlGOTLPwvkWfKTJGMw7YaKuCzQcpiFRqNQKW_58wj3b2kZ0H5vC6JkkSCsL-wHa-tvJJqxUZXuKLRhN4JQKVcwM3Nwze4HWh1I7as4e4EZFZl_oTvdZQEsMyZFEcaURr77igvhKkOg393_1d6Gf7VCHzkQsxSGuviq3Ar19EdS95pFgcexWsjAPfLCuHE-_E4ng1yPFxL0uTfIrlCqYdZX0idBW2I7PdRar2MZD5SHT-dPU2IJ889UIwJZYJucetctHuUnskSu06AZQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 220K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-07 14:29:53</div>
<hr>

<div class="tg-post" id="msg-81465">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اگه این با سپاه همکاری میکرد که الان همه تو صف اعدام بودیم</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/funhiphop/81465" target="_blank">📅 13:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81464">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">پاول دورف داداشم، به اتهام تسهیل فعالیت‌های تروریستی، از طرف سرویس امنیت روسیه تحت تعقیب بین المللی قرار گرفته.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 7.46K · <a href="https://t.me/funhiphop/81464" target="_blank">📅 13:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81463">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">دلار 193
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/funhiphop/81463" target="_blank">📅 13:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81462">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cG4Pl1c0zP6QUl9OhppNoEnf6F6fdaXWgM4fW4K5dqyMw6fcpw518-vksHU9bOOEzlxeT9BshU2f5hEEUgfTOFBCV0zyD6pHWt84ux-pB4R6JCxnac2_8utIuz9SRQaaRakH4scHFWmwzgUlsVQkgy7n-zFd4loOCKICPefbymVuQugd-zisiGypf9Lstz2ateZca4R8XCDvWWik7zAZ7McX4ZBp_0u62J7icCcCffcmtc83kEoBsbDdn12bMxRx8uKS4CJK8BUjfzL9oMv_TqvPm0cHnvmRsG-glMsvTFTsOCdP-nBI9Eh8c64r5Mo3y2aN8Z2Q0eS9SNth-7fpdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری پیشرو
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/funhiphop/81462" target="_blank">📅 12:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81461">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wBFaiatpi7OFEpgd7rWtvZ22aJrmCe6wbvsQjj3ctbr9U4P5Ns4vz0HpM8nQtYfHzyGAdnhCQJGvXnlBVTIf_6KnOun3r7s6Vvmkw-b5kaRPQFDQGnyR9EGbpll5FJYaZS2Q0DfEgvY0MLobCiieP_O1Yj2YwjugGGCJar5subyV5DtUu_Oo7SERHBGQqtlMa7iVK8tw7Len2k5tHd5EoNHD7XzhNxTcKuHLsmfNlCPvBlSBEvDxXnyhLsyruf8dqC-z_ui7urM6ddyTLWdtc4NiVnj2p9zZG9FW1JYddVEccNiyHTiTmzt8_5Sugw4djlZBw-XlldJIWtvAyWzqtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
اتلتیکو مادرید
🇪🇸
-
🇪🇸
ختافه
🏆
رقابت‌های دوستانه باشگاهی‌
🌍
🕔
چهارشنبه ساعت ۱۹:۰۰
🏟
ورزشگاه سرو دل اسپینو
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
اتلتیکو مادرید در ۶ بازی اخیر خود مساوی نکرده است.
✅
ختافه در ۴ بازی اخیر خود شکست نخورده است.
📈
میانگین گل در ۱۰ دیدار اخیر اتلتیکو مادرید ۳ گل در هر بازی بوده است.
🧠
تحلیل خوب، آغاز خوش‌شانسی است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r7
💻
@BetForward</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/funhiphop/81461" target="_blank">📅 12:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81460">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">از الان تا ۶ سال آینده هر اتفاقی بیوفته ربطش میدیم به جلد مجله اکونومیست
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/funhiphop/81460" target="_blank">📅 12:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81458">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">هدف یدونه پایگاه آمریکا تو اردن بود فقط
💔
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/81458" target="_blank">📅 01:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81457">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">تروخدا اسرائیل باشه تروخدا این یهودا خیلی راحت نابود می‌‌شن بوم بوم تلاویو اسرائیلی‌ها مجبور می‌شن از دریا فرار کنن تروخدا پدافنداشون ته کشیده ۸۵۸۷۴۳۹۹۴۴ نفر ازشون مفقود می‌شه کلا اندازه یه استان ایرانن ۹ میلیون جمعیت دارن کلا تروخدا تروخدا اسرائیلو بزن سردار
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/81457" target="_blank">📅 01:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81456">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ببینیم از لپ لپ اسم کدوم کشور درمیاد
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/81456" target="_blank">📅 01:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81454">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z1P-jHLxqAqESux3Mlgz_UUo1cRr4nJFP4JuJd6i6WQrWLYj7LktWhXub0NAbzovyePXlh9ENamE6aLR-zyR_lm1_nflHtJXVwsfuXQGbs9GMWZaxf5tq-d0eeqDoqgJkshP-9ChBNAhwV0O1VSNb6XWLUMfQn5z98kZA6yUHEpEo_w-YDUmcOmvm1FxFYcmyWzGU6OYBimaIovG-2uVP8janqurh_UxguWfZVNECWWYpZJ3TepXs4f7mUXwSgX0FeGfx6JExpbjWz6_RArRt1yZseFLlrZuztpF0cvmWCeaoxpSiTp-SbezS363meG9ujZ-A1x3YlP4is-O6ANqzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/81454" target="_blank">📅 00:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81453">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Orsd9WHhucG3uH2dR6yyilDnVkxL1UDR7U922C4N5hHqmqhvmY_a0ZsPnefSQwWzkyD7cjXjGCbT0zexJDYKoJKyN8nJYURlvXlTQ5-Jxyl05zxddsSIVIGGI2mv2TKbMEOFBX8G-EPvvqcFmdhmU0_Q9gK1al13tnh0M0mmui-kHgYdzrx4JPWZ_yT2SHOGcVh_wiuMRhQMxejB2qT1Ed0GVqrEV6S6wT_ZVRU0ZMXSTNh5Xs_LbEHgQ2AnArcnrgKK4Uel6gxsMytjwDNI9B7BZrM2xnUYlWSFkK028Ik5PwsXbFgLd0_nZp0xSU60jVGrFEaYrksp0iRCfMZTfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچیزی برای تعریف ساده کلمه نیاز به یک توصیف ساده و فراگیرتر داره، مثلا خارجیا وقتی میخوان بگن بی طرفن میگن "من سوئیسم" تو ایرانم هرکی میخواد به یکی بگه "جنده" دیگه این کلمه زشتو استفاده نمیکنه، میگه "شیما کاتوزیان"  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/81453" target="_blank">📅 00:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81452">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DdfDv4SEstWKVn4oQCim5YZX8ZU8Zm8gpaq0M1uh7d2x1vW6zPfmvghbChes-5iR5uub-QGV2PnYSaXh3SMHRM84Z7dJihwOekBz48a0UkyTtYE8VtdPc3SMC-qDuTGuU16G0WRaROSGQXNJsd_2Q9GqEaVwvo_n_17pOezmApX-QVN0oSqgVNwQ3fh3dRVwIZWsN8Jdz_l6gyO2zP_iJ6CR2Cno2KGbWJr6f-utSSohb-srNZE1cbcbXgTYNmA-5ZtMc0u8XW36iObHQnH8LcjyB5GSWB222r61lipv3lQXb4HnWXmqHDVJ1TX6Jzb202-7IaTHo0U9K8mCQp2a7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچیزی برای تعریف ساده کلمه نیاز به یک توصیف ساده و فراگیرتر داره، مثلا خارجیا وقتی میخوان بگن بی طرفن میگن "من سوئیسم"
تو ایرانم هرکی میخواد به یکی بگه "جنده" دیگه این کلمه زشتو استفاده نمیکنه، میگه "شیما کاتوزیان"
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/funhiphop/81452" target="_blank">📅 00:32 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81451">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">#رسمی
داریوش ترک کردهههه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/81451" target="_blank">📅 00:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81450">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tvetXyuaYJBn2LR8cmxvn8Zolxm63BEt7sgn8cG6DDQ23hlxZEwQsPkmPTgdtHtVtLXqeMoFwyIYVbg_fd5SE7B_VvC_-FY06y2j8FFH6EcwzNp5bbF4crn6ECApqItfhO3el1teUsk9Zv5RbJQn5iI1Aq7CevDHPTXzQ7q4qT4EVkNc-gtZ2HCSvm4frFHv15Ea4gdmwciT50S8cZ7vH5HmaSh4_Jt4kEX7_IsEuv94ciGqYyT5F9zKh670u8u-4_f8oyjg4voYSoswhPLCMRPxUtuAyIGIgq6qbNVYuZiU4-w1Ngm7H5dPjb0ApADweukEF7wWfK5L1pBBMgaTDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور شاهزاده رضا پهلوی در مراسم یادبود لیندزی گراهام
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/81450" target="_blank">📅 00:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81449">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">یعنی جدی عملکرد ترامپ رو تو اوردن نفت از ۱۲۰ دلار به ۷۵ دلار تو دوماه ببینی و باز از گرونی نفت بعنوان یه موفقیت حرف بزنی نیازمند خیلی کصخل بودنه  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/81449" target="_blank">📅 23:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81448">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sz8lONVKIPB8szW8wugzURwf-HzFe2z-32Izj4-bSEUTIblhMzNjAL2tqUqMqmDrenNW8rWBkKyEaj6kcK1Vj1tuHeozozv_rC1SMRzObeNPCwY99YZDVb2hTprFkWoxyfFELHVb5Fehu_D9GIxz6qtspEh5xeDO8euNa1zvuDY6DXcF0JHly_02BVHNtDaN420P10rJfSk29OHSVzq-bqAmyu6TN-_5e69ndETmk25kMgg_5AXDmLp95FtFQU80GjMxrUW2Fn_Yy8xGwV16Wl27C8WN5Kys6n3jjBeqytrVy7BrfY2BbJLnntiCnrS9naOFKlYYj8hZvagn4XT0qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لاپورتا سکته کرده، اما اعلام کرده که حالش خوبه.
@FunHipHop
| artin</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/81448" target="_blank">📅 23:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81447">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">قالیباف: دنبال بهتر کردن
زندگی
مردم هستیم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/81447" target="_blank">📅 22:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81446">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cNb62683sueE3BuwpNZ0-uofFmigb0KWyYVWC4D-35QYXeQhljaJkTSQ0xHETkhEd8uyI11K5yVRwbVl0QdRc2WHxYEkhgFZ2rV7WQMdFjapfANjC1JSW8qfhau8OPy0KFICdebzGcmlrZs79HLV8mKIzxi68ldvyMR3E-1rELadHugldSzUXTJSJIYCruuoCkZ7U7rVxwH1y41W0nN1DPDLgjVFMj9QRvcJTnQt8jniuXpBC-CCLWHkrllEzjhPuIeLkQz_wGjNPWi7R5khQ3p5xCFzRFvHBt5mOPRED9aZDxDTza7PdBRMJuNZx0XyVYFQlDD4AeKpd7z5oBnNqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جعفری دوباره منیجر حصین شده، هم پرایم حصین هم شایع با جعفری بود، با هر کدوم قطع همکاری کرد بگا رفتن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/81446" target="_blank">📅 22:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81445">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromApexNet Shop | اپکس نت شاپ</strong></div>
<div class="tg-text">🏳
سرور مولتی لوکیشن ویتوری موجود شد
💎
🟣
لیست قیمت سرور ها
⬇️
🟡
سرور 10g - کاربر نامحدود 90 روزه - 45000 تومان
🟡
سرور 20g - کاربر نامحدود 90 روزه - 95000 تومان
🟡
سرور 30g - کاربر نامحدود 90 روزه - 135000 تومان
🟡
سرور 50g - کاربر نامحدود 90 روزه - 225000 تومان
🟡
سرور 80g - کاربر نامحدود 90 روزه - 360000 تومان
🟡
سرور 100g - کاربر نامحدود 90 روزه - 430000 تومان
🟣
همچنین سرور تست موجوده حتما قبل خرید از ربات سرور تست دریافت‌ کنید و بعد اگر راضی بودید خرید کنید
✅
🟣
برای خرید از ربات زیر استفاده کنید
⬇️
🤖
@ApexNetShop_bot
🟣
برای ارتباط با پشتیبانی و مشاوره با آیدی زیر در ارتباط باشید
✅
👨‍💻
@mehdi_splus</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/81445" target="_blank">📅 22:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81443">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YMX2digeWQgUyzhA0-IX0l0t9sOIKFeRpCi_l0jcM1yxGKBtQ_7EopPaD3kdYi4CuEUwQE03KZUTzuzqDIr3nQLdXA0Knb5LQG5Xu6hzC8uRXdlzHeNgISkk1uxfeIMii1b30elDtxqPbYl75b91w_-gaTp1FKuJf8PoqqNk7DjIlu3fVzdH7VCkcxmkoqtYLQflwYERlLCYObL-FQRUlDYbB-lwpaXpEfEKv5NdAniZUkfXTVK0HFWWZgUFalmscK27qYCI_RMf30PVO31SZbar-0XUVlje_TcJMUpgDijwFuntvaxn47TVfVcSwh2OjQPfq5gv4kcbFEIM5G7S8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BmcJpQ_rrEF4DQjhtvnNlwkUGitBweQluctv4fhxqVOP7oZAR3iMLbI2o9Zkz_rButoql25tEuqHPU4l8bxGOVZOOCZSUF456hErwLVfJsFxpSMp66uwACHq9wZhhMkol2z2_rk0KG5PdNrtIxu8K-odZOzYmrUQQBCmEedi7LgHiGI7nLKLcq0eMFdcI5ZVa3z2Pg3hnAxlZeECzLHhaqr3G3e49GiuDyiAnVHOk_XaxGNEMl9q8KIdaWi-Q3H8t9FO9MZDUUVc-RCudAbxgtmw28jx26nI6PMBN2rDxkkjHU9NYaDYsoJldnogqiIbUDOaJpUlKbCL_xmd5T0SLw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">استوری های نوید و بامداد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/81443" target="_blank">📅 22:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81442">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5beb4b7c70.mp4?token=ro4ilP_rk6MiBOgm5XVHSoIVIdg6jJsG7V9CVrWK1k8sMV47sGQ6JyX2g82KCH_G8exSYg6DsUQCpFpwcB1smEapI0Cm2NuiHnXqD4-bn4pbHDX9U2tTnoETFQiG7Sk8APKe4eija9fjpyXT2D-kpIi2Ae21yaxdjw-CnbLFmSWF-Q4iXgXIbqWueUbGXMGnnMcEUnZ_Jablmzxy8dBUki288VPpzCXbesKgVmJOR7jy1AjKC591LQv68LIDA8VuInNrr93gcq02TWEuBXEXH69-UtmAjVnSksxcJcv0XrJseMjh2F27WDAO1X-_OwVdGMpg4HqzJmf5Rnin-jJLxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5beb4b7c70.mp4?token=ro4ilP_rk6MiBOgm5XVHSoIVIdg6jJsG7V9CVrWK1k8sMV47sGQ6JyX2g82KCH_G8exSYg6DsUQCpFpwcB1smEapI0Cm2NuiHnXqD4-bn4pbHDX9U2tTnoETFQiG7Sk8APKe4eija9fjpyXT2D-kpIi2Ae21yaxdjw-CnbLFmSWF-Q4iXgXIbqWueUbGXMGnnMcEUnZ_Jablmzxy8dBUki288VPpzCXbesKgVmJOR7jy1AjKC591LQv68LIDA8VuInNrr93gcq02TWEuBXEXH69-UtmAjVnSksxcJcv0XrJseMjh2F27WDAO1X-_OwVdGMpg4HqzJmf5Rnin-jJLxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهوی جنایتکار کودک‌کش تروریست صهیون:
آقا جلسه‌ی خیلی خفنی با ترامپ داشتیم، وقتی می‌گم خیلی خفن یعنی خیلی خفن دیگه، ما تقریبا سر همه برنامه‌ها و اهدافمون به اشتراک رسیدیم، از جمله همینکه ترامپ مارو پاره کرده که ایران سلاح هسته‌ای نخواهد داشت و یه سری چیزای دیگه که من گفتم و جاش نیست اینجا بگم زشته جلو جمع.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/81442" target="_blank">📅 21:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81440">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QJwpwxyDu3oQ2TTyyaUOb8_f0ohVWUwLHbdzNZOTLGv0yH7V64libAyEvFtuRkebnx6MKewiJtetWOPJYn7l6IkKs7x8HQZTDAC8PF7YsBRi8VTXwdBrtEJlQr_asem-bkJftzwNzL6hNHL6MnKFNVikp3Fuh0qSKAaSA0BdmFmr9JOPgz72-LZpZDJ5ay-4nOjyGo7cThkg86XB0W8BUK9js9t9fFoycxnieyVbgnQJQ-IQD9tEtZBw27SpwBy5pwr9lF8vRoLT7yYhycqvXX5-pqUvzqGM6pGbn2v6YsTItIcWOku-ckdbnRz5A34qRfwuWSV6u2nDdEGBptttwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E1NigoC4EMRqDavd2JIbhJydNXagD70E7OOrbYZ3z9EuHcFWLAf4erbNOZvbgseucRWs1l1k1x3972sZCdRiMvKv5XuPggLQ6HciJ2hrn6abi9BYRI82ZmUHXrsXbDBm8cWEZ7-kmwvxtJ4mNZj0CsNnWy07OAvCPEhjH33lHgx2fbKjdjLNEr5tlmKhPDRmbCAYWcAdccWtkgKSXCG8NCaTjTWtuyqmIMRhwqNU58yDKUmKZyIwB7Vgl8aN19c9YlixtA73XN9kX4DlCYJgZNpSBbLiFnO0ykK2jfYOVCJ8TiaoZ_TUMFiXpENzxue34tufRuKAErcNLZxMS3IiJA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کوکوریا قیافه دلافوئنته رو تتو کرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/81440" target="_blank">📅 21:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81439">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cg91LmHLx-cccJnTON43IiQRt1K-Sus-FFNDbAZsBAIL7vDBqiNou4GpA05cukj_Q4mrEvcceFzISoMeL_W6D_R4hfoDXY-X_i144g7ZJ1e4V2UqeIPNKCM6oLW0qldULagRYQtV0Kzc-Zw61KBH0-G9DAXfGQZOY-Mq34VhH_4uSJ6ATJ-rT-e_hYM9ZqdulrsoEcGYm-bH4k4eUpVetlsWVcLzttw3dWuRDWUFxQXNoTh7kQ0599ALAwvYx3LsFek8v6VkNPwzdHrGrJzFI8BDnnceeJ6Iprh-UY4UlVsiVF-o76m00tWN7IgdXLK_KJ9DeSTaeBFsc8Khd8rM7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشماممممممممم
😂
🤣
🤣
با هوش مصنوعی فیلم سوپر زن رونالدو رو  درست  کردن  اصلا ببینید پشماتون‌میریزه
🔞
یجوری داره میده انگار  ۲۰ ساله توی پورن هاب داره کار میکنه دهن سرویس
😂
😂
ویدئوش رو اپلود کردیم بات برید ببینید بدردتون میخوره اخر شبی
تماشای  ویدئو کامل
https://t.me/CONFINGMeliShkn_bot?start=3126b54d70f9</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/81439" target="_blank">📅 21:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81438">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">بعد از اتفاقات دیشب شماره مادر سام صابری رو گیر اوردن براش فیلم سر بریدن فرستادن گفتن سر سام رو داریم میبریم
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/81438" target="_blank">📅 21:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81437">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">شاهزاده قراره با بی‌بی نتانیاهو در مراسم ختم سناتور لیندسی گراهام دیدار داشته باشه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/81437" target="_blank">📅 20:45 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81436">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sm8RefDRcCKK5z2jKDuwtbQD9wthgxfrkFXIooVSaSa7wRB6QZ_hoIfAFBvOe-yHxrjugVaUOOwoecaS8kDZmejo3E96zevgjsAEbKuF4ZeEtUbmK08axin2DmJ5aS9d-XIVTB2Jn2HIjh_0Zmo2DocfGpehrJQcHXJ84lsN6mCdWbFGrQ8_b-r-hSIG5Z_fQ95ywa8-3OIp_gaAg08gVSHE67zQEYikNDvPogaXzyiucuMyENjlUctLeKLBHSYlBjz6Ku6cHWe1pZueAzpiIRPxQk_CRWrWL_O2OcmvFW6ZJLOXJfhBg3KTKd7J2DcCpGMrMoWm_1syEI276qUGow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک ماه گذشت
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/81436" target="_blank">📅 20:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81435">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Numb 1 - Madoro</div>
  <div class="tg-doc-extra">numb</div>
</div>
<a href="https://t.me/funhiphop/81435" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/81435" target="_blank">📅 20:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81434">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GtlcMQH8x-TWT-M9kBkxYk4na2YsYh2VWQelZcDy6H3fW049HoTZSs1dWBifHetbNuuqNP7MNazkcl-jzErffoBSSfTJlkZbAGuRf-Ag67wmB1q2iAbVg32_WZ9v8_zPySTyEF-NzWiWMSL1l7OtVHfAvDtb8SNSp7KbuWHS4Kr_kxt1X5RGOVzUgl2FqHZSBK7x2T4Zhit40n2Pe4noubRTvBm0un-9bHP5RyU6vnUoKTg9VLBaR1_YtgeWKqeF1NZTmC4tN5So-38N_rZ7SfKDTtoIY--AzgowG1xEGrKPftMYhJNHgwr2u7so-q_K072HElQOWSTI1wV_LrAcsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آهنگ جدید numb به نام مادورو منتشر شد
📺
Telegram</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/81434" target="_blank">📅 20:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81433">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">این که ترامپ دوساعت قبل جلسه با نتانیاهو میاد میرینه به نتانیاهو یعنی یه کاسه ای زیر نیم کاسس.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/81433" target="_blank">📅 20:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81432">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YkErnUyHBPx7VRtRLklZH1_TdAUtdR_GpB4SkRH9rqAXjoZSYsuipKxSWooI99x_EpquOxma3V4WUCqV-RBmUnj79Va56mTIK9Gxm4fJxHYhcKhCYxQiMDj0RVHmixWT_oyIk43TlhCoiGP6_6m3bLMaBNfVqEYjhWeocg5Wn9jrRa3fGUzg5sDC2lQ7D_c3y1NozcIo5sHB59y9c-A4Vj6_G9rK7FKs9nxBpxhWFXfmxrBkK3gSWUqB9MOlOM_QrDdmpmc6wUnEHls1LKArmUJxi_p77OPerYIX65Tk2eVxRYyAua_epMQj3y-HAO5Ty2-oMbtxjuhVW8mKqnNyjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این یارو تو فصل یک عشق ابدی رفته صداسیما
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/81432" target="_blank">📅 20:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81431">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kfoe--PfAIMDjPt3BP7CqHOlVjQS3svJSMssSEW0Y80TgrYsKebR2l6dpld8w6FCxvr25jPkGH77Lp0S4N7dreNOm_gBp81vpj54-oGRS2uW91sMEm_MAsLwBvnMHzXCi67edu87i-9qKvWjHFUqQJfOMTWqLdpEK2fiDyWEeRBmJ5NggUtrj9I8rgpP6ZMqidbR6gVKpUa4O4OgAPieVJY0nhtnTs4paFLXMVnTKh_3r8jByQWx8c2KEGDw0Iy7Z_wvyueJDnG4wmMxfvzgXC5TpOXhF2kgkZreuS-kKIIVgZH3U7lRacuUPjyDDwO5sKN-i_Pyw5RmdkHAhL2LPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو و دو تا از طرفداراش
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/81431" target="_blank">📅 19:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81430">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MSave6mVqg9l8K_IsFpKCvEFnocSotlySeDT5pJJS2MItorEKUJovTg6OWi5mrdT_mW-j2sAbdLXgbE9P4SLKhI93G22jFv-_7JF77meGq_u-y6jON2A5QMoJ6WO1ZiHRimSp7K-zVJL2CCugJEO2q5EzUH_TBoETF2D8b3cr5Dz0EZyUH5Brea9zh8SyPBDFBeaMBG-ZBkVTAjNLR3-sY8AeIEioEPI808APOtF9m_s-Gk1JV9GOidAbUbTc5tOdR9Z43K9ufjZoAU1TSBa39-a8pn6uhY19SjEHszt5LZuq-Zjo4uAKVg7AbC1qnQ6fTKh8RC6nSV4ZcqKLrk9Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توپ فصل جدید لیگ جزیره
🔥
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/81430" target="_blank">📅 19:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81429">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G0QmE2wsgMdYQpVSVsevRNDmsNaBk8Vh94T3JGR68QOA0nKD2sb4zCbRWQPCSOocuBst9HrwSP7LRQ30myhYYD0aVs5Ji3gGO3GNImzM3AuOSt-9476gdwhh8Nq9DBfMEq81WwAhg1WncCEnNKtSR6TsdmJksUMMRWZawIwyWRbcOpeYLZfmYPMgJzbzwUdNMvJt3HZnJkwN1t1_yDgo0gLWpST9GXlysivGtYxBz8pUhvUVTdZrlR3AXEK1i8zG7_rifDFrcGGI7S6zXKM5SbEv9-thXOMK2YEPxwfaZ8EUhdfFQM51Crni1OP19_s2R2JQ99Ap2LO9aCGBNRkwDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچی بگم از طنز ماجرا کم میشه
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/81429" target="_blank">📅 18:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81428">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NfHtRe6TxKdNsLhu0QBf1hjeoFSoOkfvCjuztTyKsKKVmchV-LIYWbYVJ-0vVP5H7TUqlLIUEVyjgJifo3AdjGIj-dmS9OpTxWIv1xOizJwusjBM0pkRkLA41ItBAtIDdUHN1KTbSQzviiEXZxolOIK6hOFt-7K7nRMN9PhKpd668ZoWLWxm_88OU6gwQLUmzOM8VmA43HVhJh6ORqYrSQ9al38uHJdVScMP23glcLWw7m3hO00tKHmyuQvrkbJ3KSatluiHTpUAUcAAb9lVlq5iOGrDz-i4mkXmx4g5lzuLMaczzBMY24Mmv4FJfbtGJfD2r2JUSolS8eiSPinkmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
رئال مادرید
🇪🇸
-
🇪🇸
لگانس
🏆
رقابت‌های دوستانه باشگاهی‌
🌍
🕔
سه‌شنبه ساعت ۱۹:۳۰
🏟
کمپ تمرینی رئال مادرید
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
رئال مادرید ۳ بازی اخیر خود را برده است.
✅
لگانس در ۳ بازی اخیر خود شکست نخورده است.
📈
میانگین گل در ۱۰ دیدار اخیر رئال مادرید ۳ گل در هر بازی بوده است.
🧠
برد، همیشه عدد نیست، گاهی آرامش است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r6
💻
@BetForward</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/81428" target="_blank">📅 18:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81427">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">احتمالا امروز یا فردا سپاه به اوکراین حمله میکنه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/81427" target="_blank">📅 17:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81426">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">به گفته ایران اینترنشنال,
قائم حسینی ، امیرحسین ملکی
و
علی دشتی
از معترضان پرونده‌ی میدان علیخانی اصفهان، به زودی قراره اعدام بشند
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/81426" target="_blank">📅 17:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81425">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">احتمالا امروز یا فردا سپاه به اوکراین حمله میکنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/81425" target="_blank">📅 17:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81424">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vmyUyW_QJVhhvhCxZ7rvevNsmYAMg3NG26WQy4L6FooHMe5Dtv2Zu9rREpdKTXkG8Qa4Hvn19VXKNyIpHpPvKY-qE75ghm_g4ySh43pTXdxzHilBAycZMnkQJucGtS8bKEc08igMTdWPgXkmPiZkAiGQKgYT5kHnhQhdedG8HAjDXeYL91-XXjy6Aec6O3_Lu5RNXxnHYgkPTJtC8iN9ExOZF3a1QeoIwo8DpswhR7y1tw9XbiATW2laSDuoGcMTsmVPg2RmavXFqXaOgA-BRY48IUlD67645bv8M92La-ClaPPHwsLsFaL7ZU4WRfD6DXdW-tqxfm3sCfnJlImHMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو خود سایت کارزار، کارزار را انداختن برا بسته شدن کارزار.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/81424" target="_blank">📅 15:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81423">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">اینطوری که روز به روز اطلاعات جدید تری نسبت به زیرساختایی که از ایران زدن و زیرساختایی که از عربا خورده میاد، فکر کنم آمریکا رو فقط در جبهه کری خونی با AI شکست دادیم که اونم ترامپ اشتراک طلایی گرفته داره همونم ازمون میگیره</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/81423" target="_blank">📅 14:23 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81422">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">سخنگوی دولت: در طول جنگ ۴۰ روزه ۲۳۰ میلیون متر مکعب از ظرفیت تولید گاز خود را از دست دادیم.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/81422" target="_blank">📅 13:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81421">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">از سر شب تا صبح ۱۰ ها موشک میخوره تو خاک کشور
اما به اندازه ۵ دقیقه اذان صبح کشته نمیده
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/81421" target="_blank">📅 13:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81419">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MGpVW7tNTFcmA8qyYQ4brL0N1tzI6a-gQwr1MIAutN_w4k6cei-76jfKd5AXNpDSIJNAQJ13yvuz6MN-gTHFH0IAga31nIolwL2MLvZ0PdIHBYqa6XTZzvssLhu6ve4tgEgxw2HS2yk419pNic4a_POomCQXLiu-K8_Z6FKXiAIaPHUVDGhFU1VVFNxmd4SXcT0XpRXcJCqXnzLx7_6hJUOZuQAMH6ff0clDKpVvBX6_89H6xk0lUtDdUQWQkfjU2ON1oRuEcuyigSI1lEaXxhblpVg71E_VicgasAwSlN-vpk4U6dDOgtpxTe74Tzdtgu3PLx0jo5XsN4jslU25Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qx37v-XVHZ_GsH9L1417d2XqMBF35nL_Ih1NlZWFRFj_apaFDDXULUgLtS1QnDEeXNhp1vVunpeiwdJFrPyhCzxL3qsJFFfrBn6Z0oN4zohRNrdwZQYeSLr1jpsfiIJIWURFRF3aOQktqnuNmbmCn2GxAo36LNTeMPhv9rRi5yTCJLpcl6597uB4iDuQvPk23Ks9b1q8-ffGap3Mix2mCiTq5dYYzuTgvWjPozC_1PL2vByF1p-tk50OqLo-icguRSzJzMhrwCwH_OJ1m6G7XmAh9ICRg-3RIrSyBrhVvAZmXVvqnt6ZiNkIk8JEPLXQ_MEM6WpLMnM5WVOvoPc9QQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یکی دیگه از پیش بینی های اکونومیست درست از اب دراومد.
زلنسکی با دوربین کنار یک کشتی ایرانی که داره کالا حمل میکنه، و یک پهپاد هم بالاسرشه
چند روز قبل اوکراین با پهپاد یک کشتی ایرانی حمله کرد.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/81419" target="_blank">📅 13:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81417">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lxLZyCGQgsF1MoXr47wy2iAHw2RFyTg2sGRzlcHNYF71PuJi9vDKReG1AeV_CBhPHuyBf4R36HBzN4q3qnLpvQBZRw2MbBDiSF-ocXNoLBZ84cvYNFTILyccGrEYo8U8xEn0jPgWR0YoTZdDeucjMtKqGwTcGygtjPqje-F3jRMQwxak2IheIERi2kHru8RzNnIL7vLrqOLkKuNsAKiRSpIyWwn_NxzRX_waUuuenvQDkVEeqoCIOE4cEfBa00yWGwGTAp-8T3tFYYk3r3XZ30mzIxqNJBtDnvwDGEpwvUG9quiedilR8zUHjBprgth8XT-DH7oMAQOhuhWocpBDJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f171036de.mp4?token=N-pKXVr1zR3Yc4dOjM36IdaTNozB2TcbLKdT2QYehfohuQMhnETBYZI5B9Q6Fuv51WemPstpWJdGN9C6HtWluVVTLl59HtNvEW_6HPUrP98-eyuYh_mnfjcRlNbkKzN4_yoq0Y73heUNcCzpnNWz4wSxpV3ZDHwnhCpjNIQI3kGrUw76Ls7fBMg1_sk228cSsJBqrP64fLcsLhop-YYtglJMu3ZOVqSOyZd8SpSpN8W7k1vgQaQMcIswDtbDK65MlZMMV7_1eJQnjGuGHPitED2CEhpv-L9O_Qep4-1Avzx5cwYsGiGtOl1JoJuyviOBA12z-5B8bT4IkOBmF8exWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f171036de.mp4?token=N-pKXVr1zR3Yc4dOjM36IdaTNozB2TcbLKdT2QYehfohuQMhnETBYZI5B9Q6Fuv51WemPstpWJdGN9C6HtWluVVTLl59HtNvEW_6HPUrP98-eyuYh_mnfjcRlNbkKzN4_yoq0Y73heUNcCzpnNWz4wSxpV3ZDHwnhCpjNIQI3kGrUw76Ls7fBMg1_sk228cSsJBqrP64fLcsLhop-YYtglJMu3ZOVqSOyZd8SpSpN8W7k1vgQaQMcIswDtbDK65MlZMMV7_1eJQnjGuGHPitED2CEhpv-L9O_Qep4-1Avzx5cwYsGiGtOl1JoJuyviOBA12z-5B8bT4IkOBmF8exWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طقه پوبون رو زدن
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/81417" target="_blank">📅 13:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81416">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M2tBAYa2asqtq9l-oXeVypPwwL7WKVZ7f8R5Wa-Bb6YJAr6IzFyw5EGJc60cshTFnq9YQP7yxAscmH2Isy2hK8LNQBIxIlGYmh-jaWmiCib6m665vKJTsjC1IqsdHoUCYDZsXXnBQuqLYWdgEFby0ckzE8Zb2zgqahksXNasRs8S4IAG9npEBS-HGIwo1JYwuHYTD6NL6MjIhCs-mtXRz4cRMmoFUnIZ36qYnFI_yNf2ybUkfa6mFgEN3YXmVtEK6zqOBxYZnBUJb9qWyL1mYwx42UWXbrgCDJydXa081VKmk7XWDdb118nPS_AF1kqi3IXHIAuC8JDOzWKLbZ5WiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
رئال مادرید
🇪🇸
-
🇪🇸
لگانس
🏆
رقابت‌های دوستانه باشگاهی‌
🌍
🕔
سه‌شنبه ساعت ۱۹:۳۰
🏟
کمپ تمرینی رئال مادرید
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
رئال مادرید ۳ بازی اخیر خود را برده است.
✅
لگانس در ۳ بازی اخیر خود شکست نخورده است.
📈
میانگین گل در ۱۰ دیدار اخیر رئال مادرید ۳ گل در هر بازی بوده است.
🧠
برد، همیشه عدد نیست، گاهی آرامش است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r6
💻
@BetForward</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/81416" target="_blank">📅 13:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81414">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce9ff43bec.mp4?token=DU4VsX81TM0G3pF23DgGZiiNAYTwzO0uN0H9Y-UJ_TaaudIXIgvGMf_8397MnpFCuTuf84MGWS4CKGmjG3pDDlxMuOgU3rdAiiD1lqJVfAK9-XrjbypttThvlExjp3ePQJpu1sTiSsh8O3f4JY1B5i-HqDitJLxMok5ylbvjzAsmnqNAWwNasQwb3f5-HyjRDXH7rpDhn0tkhbgS9IcShnRZbb_nE4jI-LQ-xSPiZ4P5b48ofONAm3zzLBlSYgfj5ytb5G_TUkltpgTwil7KlJjUkFVcrj5HCeeZ5rLWLQQ4toYTctmDtpQwoYe1b9bIBrEzluZRg6t_h1JPtw5q8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce9ff43bec.mp4?token=DU4VsX81TM0G3pF23DgGZiiNAYTwzO0uN0H9Y-UJ_TaaudIXIgvGMf_8397MnpFCuTuf84MGWS4CKGmjG3pDDlxMuOgU3rdAiiD1lqJVfAK9-XrjbypttThvlExjp3ePQJpu1sTiSsh8O3f4JY1B5i-HqDitJLxMok5ylbvjzAsmnqNAWwNasQwb3f5-HyjRDXH7rpDhn0tkhbgS9IcShnRZbb_nE4jI-LQ-xSPiZ4P5b48ofONAm3zzLBlSYgfj5ytb5G_TUkltpgTwil7KlJjUkFVcrj5HCeeZ5rLWLQQ4toYTctmDtpQwoYe1b9bIBrEzluZRg6t_h1JPtw5q8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی گرامی کار قبلیت چی بوده؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/81414" target="_blank">📅 11:11 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81413">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">مگه نمیگفتن هر زمستونی یه بهاری داره هر شبی یه روزی، خارتو گاییدم چرا تموم نمیشی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/81413" target="_blank">📅 10:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81412">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r5Rc7KcMtbPsKOaxi9zPGQS4aB85kaMyS0vURTZjmQ531ontX3HqBLJ6oy6NLjWVQrP7YO_6AXm22BxB2AqDCe12kh0Gvm1zeeiH_D4dnQNBdxpXV7a15T8G3hP_iGlbK0C5f_k5JbglB6oIAnA3HbI3Uirk6oKawD2l3aBSWHt4p7Xm3WAQ-sywcqkKak2Rf4pniW09x2BV2ITQlEbbSE8zFgN5j0fqFkysJFlWFxUMtAoSjPm9FyYPz7XRPGcqqsfOL2ax3mroGLbwkTSxZ8FiyH4iULHH8-36zHk6sKySxGehEYNXlRqqF1hoZFIl58Q3PAanzt5MuDxJPa3gOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/81412" target="_blank">📅 10:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81411">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">تروخدا فرزاد قدیمی رو قاطی زیرزمینیا نکنید، فرزاد اونقدرا هم کیری نیست
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/81411" target="_blank">📅 08:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81410">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">خبرگزاری فارس:  هر سه نفر اعدام شدن  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/funhiphop/81410" target="_blank">📅 05:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81409">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">خبرگزاری فارس:
هر سه نفر اعدام شدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/funhiphop/81409" target="_blank">📅 05:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81407">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">از میدون صدای الله اکبر میاد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/funhiphop/81407" target="_blank">📅 05:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81401">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">درگیری گسترش پیدا کرده میگن با ساچمه چن نفرو زخمی کردن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/funhiphop/81401" target="_blank">📅 04:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81400">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">اقا یسری گزارشایی رسیده که مثکه مردم و نیروها درگیر شدن و فعلا بچه ها اعدام نشدن
تایید و تکذیب نمیشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/funhiphop/81400" target="_blank">📅 04:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81399">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">مخم کار نمیکنه نمیدونم چی بنویسم
فقط میتونم بگم تسلیت به خونواده داغدار و ایران عزیز
شبتون خوش
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/funhiphop/81399" target="_blank">📅 03:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81398">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EFG_72URzLL39XILgOWvqTzFa_-PnpgaiFxEmxgVKIjaPeaykxGXWbpCaNxquhX1WGf9VRljNx_WhFi0qbKoQ9mTO5bH3DTnzTiEd1Jjtz7jn6BQAsDbPTFawpVU3JYqVikS-7SBOIagvgNFntfkR_m5zI_onygLks4PcnApfHgdZmGg2rAyoxP3zC7yUMlF8euCyGcPdsdhrrCD4Gytgfn6qjmKwTbzn5C9ijP1ugSOJk9KztW61yMi3KW_2bOHceMK0VcmV5ESA7EhRCt36OpoSc7Rq2O1r_pLr6dhlVV3EhcLS4pRsx5fOfCUA_PXHiSbhNVZ4mGTCHx2E6FkbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کپشنی به ذهنم نرسید کسمادرت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/funhiphop/81398" target="_blank">📅 03:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81397">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">اذانو زدن
🖤
@FunHipHop
| artin</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/81397" target="_blank">📅 03:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81396">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oe2BExkaBm7sOxrveAE7O_ajos9-slE4sw0lqv2FJ-H4GkHY-5IUw2e6fX20RrST52-idy1bjhpuBAd6IAdIWP5hdl_51m91qJuXngeBRXd7fNNBaP1LksWwPrBGmjl8Uz-rj-hwoa29lvq-UlCfOorMkwRg0chq2UoMNFiBr-P6NbEVC1ObxvVw74vmPFClwCDDFPGh7VZcdN3tYgNxEY8SNHj-2uzWDwfaiCwgGY1TPfVH8TGY5ib69ITdosqhBQ8tprW5kAGmSvEQT5bmMHcaJPywqIGIizbEiY7RnO9FrEB3u12N2728Yn2B_mf8uHfw_DxidLNNF9W1rNshRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/funhiphop/81396" target="_blank">📅 03:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81395">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">اذان صبح امروز اصفهان ساعت ۰۳:۴۲ به افق محلی است.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/81395" target="_blank">📅 03:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81392">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e358934688.mp4?token=ZuDrwren5kAQlxNBi5GXoxkNnNh8BVCTdW2O1A319mi_53X6VZN7rzk3KuqT6m7QWyRBBOhejjJOBiNkl6mlb6i6nah71xeg3xMMM0u9xeuOYT9FnR-GyqpR2cleQ2WKuejz-YKULB8Pie9BlY5l7wgplig99lIOQnMlE-FUc3gXyf5GiwPxRL67oAeLzCyVomGmgUI0epsfwIq8y0XhMYi5qyGnu-aD5UM0I7gaTkgaH0ouLnQ-8DWvmFXDaJTmvglIuBeF26GXUOgiqq8MRSZMd3j7OS0GtN87vOjMP-xSlo5uIGyvNYoDK2rhZp1O8YalzpqTCOcJL_DsBzINqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e358934688.mp4?token=ZuDrwren5kAQlxNBi5GXoxkNnNh8BVCTdW2O1A319mi_53X6VZN7rzk3KuqT6m7QWyRBBOhejjJOBiNkl6mlb6i6nah71xeg3xMMM0u9xeuOYT9FnR-GyqpR2cleQ2WKuejz-YKULB8Pie9BlY5l7wgplig99lIOQnMlE-FUc3gXyf5GiwPxRL67oAeLzCyVomGmgUI0epsfwIq8y0XhMYi5qyGnu-aD5UM0I7gaTkgaH0ouLnQ-8DWvmFXDaJTmvglIuBeF26GXUOgiqq8MRSZMd3j7OS0GtN87vOjMP-xSlo5uIGyvNYoDK2rhZp1O8YalzpqTCOcJL_DsBzINqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/81392" target="_blank">📅 03:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81390">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">معترضین بازداشت شده با اسکورت شدید مامورین برای اجرای حکم وارد میدان علیخانی شدند.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/81390" target="_blank">📅 02:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81389">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64626deb37.mp4?token=F2rD_wOb34rnGg4qTI0I7Mbc9m7vnhuP6SQ85jml2HxiwXZ0pxgBZsHSjBPGzZ1AJkjAEFUASOmhiCquh-xRJLCm6J4_F12pXWmXtWcenN5O3hkQoMLtIBLPDqofScDqAXNPI236xkXy4WfsGaeKMVplvYiByE6ppwe08ErI9hxdhweRkoxouKUTzQf1fAHI6EUA6nh8hzFJlxerK9sQiuqtpkn41KvZCHzsop0bz-wKXUMP3IwBxbF18Z9K8KANs93IbGpDek5sIBPvPt3pqCO8i5K7xO3WsjR09q40zIsv-7uLI6xfIw7Ef_oxo3bUCO2SsOG671lY1XD7k_00Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64626deb37.mp4?token=F2rD_wOb34rnGg4qTI0I7Mbc9m7vnhuP6SQ85jml2HxiwXZ0pxgBZsHSjBPGzZ1AJkjAEFUASOmhiCquh-xRJLCm6J4_F12pXWmXtWcenN5O3hkQoMLtIBLPDqofScDqAXNPI236xkXy4WfsGaeKMVplvYiByE6ppwe08ErI9hxdhweRkoxouKUTzQf1fAHI6EUA6nh8hzFJlxerK9sQiuqtpkn41KvZCHzsop0bz-wKXUMP3IwBxbF18Z9K8KANs93IbGpDek5sIBPvPt3pqCO8i5K7xO3WsjR09q40zIsv-7uLI6xfIw7Ef_oxo3bUCO2SsOG671lY1XD7k_00Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس‌از اطلاع رسانی کاربران توی فضای مجازی، جمعیت میدان علیخانی اصفهان هر لحظه در حال افزایشه.
@FunHipHop
| artin</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/81389" target="_blank">📅 02:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81388">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dp6hK4iHrbgyE0OPdPS_JdtwZNgjbtSFuNSCVSseDqMt__oqO6fZkdeuCI2YQEVjmYMp3OEMuL-CQvpqX9yGL4wSPSKMXXAg0PxZe6POVQ-SfBiADJgDcKgtuPvbvTwc-IseKwK8J12m8lOYtzdesVrsLQhKtfkF0SIqz21ogp34soiYSZcda1uF10aXsiQ4FoTVw-qsGREXcDBoFuf4cApF0grBOwESaTHqaVCE6rdVFkbU5Yfg0alUGRNH0cag35TOR7ugJWpZ2CiWARL0PHZCbtl42mMYwuKv5T7V-qq8Mbx3U7jXpk8IFKpsPPR-u2vPVICsllRlRjCekpSANw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این لیست کامل ۱۲ نفر از بچه های معترض اصفهان هست که ۳ نفرشون قراره در ملأ عام اعدام بشند
۲ نفرشون هم در تاریخ ۲۸ تیر اعدام شدند
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/81388" target="_blank">📅 01:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81387">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VTEwx1l-8rW3q-E_keo_hpwiy_i9yU2TIpit8tFuNcA6Ol0vm6MRCvRYnC0IGOf4MQqAFp08vYeV3q78aXTVGUeQ80PgRpEy7-5IbX_FSuz8bEgLGJP4OlsfNj3XsiTUi3TiqACkm_OqBljfeCBSFxHML0ZYCPIJHEhyIxO5WSKM1KwezxcBQnuGNhBaya7cYPFagJIsS0xdNwPkN30lQ6V1G12KzGgzdmGqergCnDStpcg0S1_JtuKqiEf7EQkIzF0R5pcvYJtAHy-IhpCg8wRCiGs7oXE4Ts_ZTp39PgEYy1yJmRmgMzLByRcFV74jTlru7egxKt4MhZELD9_qiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بنرو تو میدون گذاشتن.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/81387" target="_blank">📅 01:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81386">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">نیروهای امنیتی رژیم تو میدان علیخانی اصفهان جمع شدن  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/81386" target="_blank">📅 01:24 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81385">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B2t6jzI6zz1WYvZCwFlGOYOG2H256qq5OQOno4nXCbMgEyDoaSVAVXntqNAqeb1qJ_j6_wq0UfOk76Gtsytq3sqDlXsaYlP0Eo7TtmmVEEWoGDkkEyGw9f8PJxGcsRwOELT8_hluYxcti6GWmcP_roQNIwb1o8-Fe3Q4024MzONDuABcQADhU3L3h2znC3l0yUwRGR0vuE08qj5RKnknnvRYzmQSdZ09dwl91hQzQ-u_4We6eTcbHcN7a2OUszP1d-CJiSVOMlm3x4JfcyKD2hCvW74B1ue7LaYNpILjHo78yQ_YI4_5e48w8wYYWZwaNNES5ypUw9dXJsjgc2VowQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروهای امنیتی رژیم تو میدان علیخانی اصفهان جمع شدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/81385" target="_blank">📅 01:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81384">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">از این ادمینمون فریب که شاتای پستاش تو جنگ ۱۲ روزه تو کامنتاس از ۱۸ دی خبر نداریم  @FunHipHop | Menot</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/81384" target="_blank">📅 00:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81383">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WX34v-3SklVvNq3VKN8o2XWyOWg4KBPq2zvfYp4E5zHzBZG417-e00And1m-wdw4d1b6QgXyOgvi-Nj-RCriEfQLH6-ipRblgStOKJdVQBY2_r6V68rteyunfF_6PIyt5VdLoqmuMielIQk1ZOQZA2uicsm_gnNA-Wgp7_NLXCeMoar7BNMvj5el4djbY4RCrTWCtqBnZk6Qb2bJ78gC5EF6IqMTRZ8RJsF7Mockv2YaOLZ_EkpETcceXhS1k-NYONvTlEvAwN3REoWfgsYgNQeDVwLRMcSZfY4_I4olmSf9XcTcMS4apEcyTuIJHZqEv45Ma_8XM6fOV_z7059iEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حاجی این دوس دختر علی سورناس
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/81383" target="_blank">📅 00:44 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81382">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q13i718Jj7CAijAE5zz-c-xJ50kfn3LJvyfXT7XEs_9f1q3JHjytAZElpj-BwEPer7Gd9bWJF_AWEQ-GY0hud5MHC9JmBji49vUbeDsHczwcTIKbKqCQf8xcM9tP7KwXnEcbY6m7_4f2ObGOO5kLMtphCKpsPUQT8rySOzEffjKf2eEPw59vO85tth8WORFU2NJhmnDO3F3tMAuZnGRq1BgacF3RL2C03XcjkxEjpqsf3iESbYO3JN67kBrcAkNmfjOORXHLPC1S9QplCXiTk1Cv45ZKAqvwr_W4ocAGHpqEyhnjnkeZJAi_F90PUOQ7_NdcNa5tcRXchJN7UZnjGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم اعدام ابوالفضل سپاهی، علیرضا سپاهی و امیرحسین صفری، از معترضین دی ماه در اصفهان، متاسفانه فردا قراره در ملأ عام اجرا شه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/81382" target="_blank">📅 00:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81381">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XyTlcyLe9VMkCZDoW350_ygYiZAa-C3uGBYIAbWuTRCg1YT9Y5ZJTnuLqnqkoueQMX9Ampn0S2uPCoKorQoupFrvgy6Vlai-rYA5McAVMbea5UlEguOE9_yyU74tTFJrWrPCiS9jwXTpwQcQbeSzrRdm0qwh12m3cTWq9H_T4EtIbcPmX2yeQDnwgbHGO7mL_n6SknCDa-1S_KFwI-bsjagt8Z-W0yC1tbRB-C3pDFBYHn-wxH9W_IZy94wSaE2zwOomEGrSirJI8tmgMcU7dCo5LSf74MY1vi1OV_xwgDxcQaNw7Bc8RekrM1jQ1LCoiAi_3yHx4ti5w2qQPmqmpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری یانگ کید
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/81381" target="_blank">📅 23:37 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81380">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CsfqDQg-fVgbw_E9oWrxfxo70hQjVeBzumBlb_5u1gH6vuzNzRHc5LISWqloluz9a_8SlZjEYbJ97raQALhtGZGDyDVnQNGwsOZDA6-RRwGCVTDyD0R9U-i7vkD48RM6CB1ypvVGiygOPAlJer-FA3o5rCSG5qEBE8h7oxplh6Gtls5LOn7Ahi4Z41wkXPZYu4jYBbERfn9f8qy_vzYkPDhZQdPfONMI1Lh73xqWKVF_L12jWtHMAk1HTQDsczUi5C0GJdf0kRIB6vByecEDcPc7_C4V8UkyHyUL_bFySCkg3BAjyvHf2G6j8nsXS9_jDjac9nSvS_WqUEoOfN-qvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراد ویسی بالا باش داداش کلی تحلیلِ نکرده داریم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/81380" target="_blank">📅 23:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81379">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e-r2CqGMFsaBLwq-2ctnXou02bpV4eDO3kqrOv8Pa_RKWb9oBxdF6S6EnZ8ZXK20cfIyzC38kcd338dD7w3FVxb44mgG_lOlWzL3RgnXmZgHeZotFWzjC5f_VVPFM-FQKJFPeM8CZkEHoAS7NlaZ0kFkUUnMgENRuUpvNNtMYnw435TcdBO5loQptijvfcNL-5TP9SUMPHGuE2pcoirK3czjZp-uNsdPY04b_5O4D5OmoVJrOgFDxVjDLpuv71q3fnkU7DyR1K980y89X1DEGKBKxaVcC44N4G_LzSHNAEKQxhdg2Ci3rQkIQwjAqqw770R-Nf2ZQffBF-x826GXYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلبوم جدید فرزاد قدیمی به نام زل منتشر شد.
SoundCloud
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/81379" target="_blank">📅 22:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81378">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">نوشته تابلو توی عکسو  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/81378" target="_blank">📅 21:56 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81377">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vpLvsZnpr0jG1i4W7fb9aI4vWWtslB4QWUbQi_a906Fhvhxfj-ajnu6EH-c7W1TaAKSgsGy8XAaL4qQpcUknrN77Ikb-NVlDMIAl2ui0ihI_qD4thk44DvKQS8_1SxMk5NsqangoP_NJN3ph8wbLs8t2-SLZUy8nRItsz0PUgNgt4e0gtoLQ4H4ygS-O6iZuOWj_IlMYNwlOZoWagZ7XeiF6vqMX0UuFG0tj2T9llLQ0mE3XMbyh5t8EzFr50uM7hQZ4DccQh2lSzpLWSASehh5g8FOE9FVf7AwCBvoAJ_Pfmr_oxmuA3yFsK5wy6YrKhkgSWUVl96QoHEUgtP4bQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکا وقتی غیرتی میشن:
Gay rat
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/81377" target="_blank">📅 21:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81376">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AL-Uc77Af88wBd3ZQe6ZaIigThKzBsEyIk79spM3WDwzub7bkEvHnMNQu1gJ6-2ezT9VJhSwVnBDDeFSFakNpQNqpNm2j9gusOJU-YF23XZcTybKl889nITpY1LHByjpoTDxBi7rmlQVNAUoV2znwxNwTNOw8a5lSn_i9gxCyHSLeNKXbblLq3SfNcPVmSJSdjm5t4Lh3sHQFe9OVXT61iIMWmdFcfr1CoO8nsRknEK8sFHLHj7LvP8c2kfIucNSpy02vAAYL7TdlWFTmaxUEbIV97FvxzLDCgFsxxAvGufrGvx_19TB3djAn7BJCVXEFeNuPGGbF6dbEDg0eZvfGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/81376" target="_blank">📅 21:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81375">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S0JQwwBp1RqKRJ2mVZN5LhKliY9X6sk7NlNC6700JzXwUwmAcw5VoAGDMQR69XNjDJGpy5FYQoxJYw_PfMfc2_KehqPcEKkKcytK5OHN_WfSTjc7Ks1RXK9_iwMtuo3KFh_lTuOxMOGgYXqUEcD9gOVUxlxNb78ld-x9-V6JZ0KYVVX2eaEj-Wjf4cIEhx5nOVUAsIavLTl9io6_alJ34aporj-88Lv87ya2Vbw6JmDeE8OWUT3GRdaRwKF8NuI2C3vbYjavSYZVwgiXQzXlowtJpAROEFOS-xu-hKZu-QXuo6PPQHJ9ldScdrCG8ROwuEhDzvYJJdV8fUWH3uuddg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوشته تابلو توی عکسو  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/81375" target="_blank">📅 20:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81374">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rKRTRZB7anrf6efJtKZpCMcPqF91xHsS4QpB2uANGC7WpaowrjNu-6KUqiAjPXK6xEwjKtP90VqNyPX4KiVAVXj49wp2_HMCF1QXBi_G1zQ7aWuvUZQQb8e5qnriudWfg3kU2iNgVeac8EvBxXftZiry_u_vI4CUGhF3NOyW6w7TxWQPniPgUZ9SFrfvgtljKX6clqDiccqYXdow7TqR2SbTWbQp9_nkuw_1ryCknYTxbTAj-qLuLnmAC6fqMZql7adLwT4zsFlfogbOicx7PbUhug7-A70aJnL6NB23i5_yujB6zjpAHjpbFPFGIJOi0OJdA1W0LNQZdnU6-MKpNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوشته تابلو توی عکسو
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/81374" target="_blank">📅 20:48 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81373">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QOFDYMIxjFjWmKGFKycG4kahvFttPwswtIXmVDbfFqYK0qKsvQqGOkI5DduxmqONlN98fnTJ9qN22lT9wC_eMaP3aQpNz8_RLT4YawzgP9hnEvg1WXmbx7L0Lwrk84E8snELh6a8VSYTRuzyk5G7uoYwu4sT8L--Xlnlypxs-_AXUcixm2fwux7lmUX6-fQ3AOh-MGLV7A5wk5okf_3Fa9BBVj7noXvJ5lhrDB4gSMiFc0zvHQydntKK_EMOldYcW4Tz7kzg2q1LiuuzFjSZtONdYGGkkCMouiJNXdM-U7VVQqOiFCXuMKWGV5UCwOU_G6t4ZckJtDStWnJPWha7Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشمام پسر
خلاصه‌ی مصاحبه‌ی جدید ترامپ تو هواپیما که همین الان پخش شده
عجب حرفایی زده کولاک کرده این بشر
👏🏿
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/81373" target="_blank">📅 20:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81372">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fxbTcsEI33t1hDKLREA363KQVz044GFo7u3eibsR9f0CxGVPwDvJh0ibQGzuT8NEYT42Bfs-yGfTQ5YnHX9SNpKCAVJ3eITaqSKuDesAs-3FNe0jf7dc22m0Ky-zAsSQcMazmB1SAZ-nvF720kZ7fqBbbU5XjGhfal3FwMvrmiilkrVsTWEziT9T1onHHO0UgkBoUoonMP69nwJbnaUqDSU6OodXiORiCGvVbIyX55DlSvDYR9323JOufbA069NuBr2C4PqIpdkM_bDaL_HM8N5jxTkvlGaJEVsiI8cWZy5OoSWzk_N9DareFeH6Xx1madNACe4LbGMH9ALXz0uWtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیما تکیدو رو بخاطر برگذاری ایونت تو ایرانمال گرفتن.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/81372" target="_blank">📅 20:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81371">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">خ
دونالد ترام به شبکه‌ی ۱۲ اسرائیل گفت که آمریکا درحال حاضر «گفت‌وگوهای بسیار عمیقی» را با ایران انجام می‌دهد، اما اگر این گفتگوها موفقیت‌آمیز نباشند، ما به اقدامات نظامی بسیار قوی بازخواهیم گشت.
زمان زیادی به دیپلماسی نمی‌دهم؛ یا این روند به سرعت پیش خواهد رفت و تنگه باز خواهد شد، یا اصلاً اتفاق نخواهد افتاد.
تصمیم به توقف حملات آمریکا گرفته‌ام، زیرا همه کسانی که در مذاکرات با ایران دخیل هستند، به من گفتند: "خواهش می‌کنیم شلیک نکن."
ایرانی‌ها شدیدا می‌خواهند به یک توافق برسند و با توقف حملات موافقت کردم، زیرا هیچ چیز برای به دست آوردن و هیچ چیز برای از دست دادن وجود نداشت.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/81371" target="_blank">📅 18:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81370">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EhdvD8c6BwgwcqP_1FdI-apnJ5i43JfZIclTjE1NkVbx7U74rOP24CzXOebSSxAzJB_vh0NdDhq6BTEK8CiPZvnwfYLiHw-kglP-MHUMyYYeMykAIbR1BaHxrVf_tWzAQTEIs6QLwmqnvFk2d6kBx3vzQYxsKViYCC7wnhls1jyXrkJRpSTyzQToT6L07Ewz0S2487WsieEH9-NHvqjrvnFEdGOo7nqiMWT0zUnaF8cpikoecsGEtttzg8Kl5vqp5gOBLf1FwRwWSZsEX83yWXtgHYKztPiOr3GECKZaGci3GcBvQ9si4Q8azlWIPxnZDUjejQnV2eqSdDsMug0dEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اندروتیت
دوباره به جرم تجاوز به کودکان، پورنوگرافی، قتل، قاچاق اعضای بدن در میامی
دستگیر
و راهی
زندان
شد تا بهش بگن کصمادرش چه رنگیه.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/81370" target="_blank">📅 18:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81368">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sszVc54XPY9X2UvbXB8X6tPUaE4clThqEfv16ZIjrqqT1TrQZ5vV1yB8dKiCvlKIm6P85i49XOl_xsJglL5CfP_LIHSbdD2IXO8fHO3E1i3CJIrDjHb7MWVBf_HXFXNPXbzqkfds3mS9LGrKTDI9VdX8XLD6OTc6wjC-tMTD14hM_v38wsSa9hVVygzpNs6wPmY4KcQepNp4-9wo-cpy6xGUio0CKFWgftOeeBReX22yYS185W8TNLYvrvf7ODHmCOx0YUzmQjTJNNjxtDblk1bVfWNajwUTG35Z9MjqdL-9axny39hIaQxzel_MiPQ0crMYbZHN3T3pWEopsbU5Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nw5m3J9VtkvanR0bAqz1_fW9F1gS-3ZwmwGHgix6nR4o1yU9c9rRZIiy5sG90znapwt6qyqsU_ZHO4awRJtv_uupbTFfUh-xxNJhEfnGPK_FP4JhfowT9tgzhg9gdQ1FVpbtkH5nwfD4DTiNVFsB6Jz4uV2YEPW6Gxnm5y4V5-DbULPOBwdUIDHos-vHZ0oBuljw5_O3H1kdxeNaxVsPSXaIjqmx78jhX3VWr_KEUmVo16FuoFMcw_GB8l4uBuFupFCE76-EXmH4I6k2zQxIFq8hzM5gymxmak8LMSWOjN77k_B6I7XR_LpofJu1B0aXFxGJ9Er8Yf7ea2IPahTKIQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رومرو درحال رقابت با صدفه
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/81368" target="_blank">📅 18:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81366">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">کانال ۱۲ اسرائیل :
بنیامین نتانیاهو با چندین پیام مشخص در دیدار با دونالد ترامپ حاضر شده و قصد دارد تأکید کند که جمهوری اسلامی، به‌عنوان یک هدف راهبردی در آینده، باید از میان برداشته شود؛ زیرا آن را منشأ شرارت در جهان می‌داند.
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/81366" target="_blank">📅 18:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81365">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b69a6c155e.mp4?token=WaZIN4Vf59WWvXpQwqOTutv0bkHO4vQjCf4VZmS8AoK8moqdME_Dah60QxMSEpaui7M7u43inOjXPcxNERpCc449YlVo25xV9zVEzhaafx4AXsaI_uPqUfwZ_XU3sQr3-mZC4eflpQCDPtLbCHr_e6LT3X1WmpEaeBuaer_i9XsOYWNxfLH1APJVmbMLDfWIExT16kHHUojFBggcKAutACSPVgGw-QoSPj-uOgcuGRjtcN_Ypb1uDhSO9QTE3dEEDmdcCFCt56kt-92w8xB3dWUkIq9ISZtbPFZbRq_gVXG9fuUDTYiDgo-PoBLn9BzEsS5JjvdASM0l92Iy7Z35jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b69a6c155e.mp4?token=WaZIN4Vf59WWvXpQwqOTutv0bkHO4vQjCf4VZmS8AoK8moqdME_Dah60QxMSEpaui7M7u43inOjXPcxNERpCc449YlVo25xV9zVEzhaafx4AXsaI_uPqUfwZ_XU3sQr3-mZC4eflpQCDPtLbCHr_e6LT3X1WmpEaeBuaer_i9XsOYWNxfLH1APJVmbMLDfWIExT16kHHUojFBggcKAutACSPVgGw-QoSPj-uOgcuGRjtcN_Ypb1uDhSO9QTE3dEEDmdcCFCt56kt-92w8xB3dWUkIq9ISZtbPFZbRq_gVXG9fuUDTYiDgo-PoBLn9BzEsS5JjvdASM0l92Iy7Z35jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عادل فردوسی پور:
من فرزند رسانه ملی هستم
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/81365" target="_blank">📅 16:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81363">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a47aTcl6Kd2DJ3gl8MElGd0P-IZ-AdkLYutqFcRZ06iFMGW9ZpN25xrokgT7dl096npcxYeFvre5SbpdgRhKhI2YwRrjEvburpr3KHsRqHEXlBk1_iAPdSnynUvbtoBIcxQgdUbuzEsEeDzXOUii1ISCHaeHENFkCUwmQWjNIwSB7SsuFZKbenG9PZcPCzTGDJ8UrcWOgzmA7ZJFxxJUvY1_hJLr4-LiwJ3uj-1cFhK9SQLdmeGYl119hCC_jcdD86KyQ6wtWfPIzfC9034sSTKFqW31YjscauFQeAhM0JXS7KgcQHXs0W_KWF5_utgVw5bLyZGoU3QkeSUDYLvOjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام از این جا سیگاریا برام بخرید لطفا.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/81363" target="_blank">📅 16:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81361">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HF_-hhnjUslZySOFK1PfndcpuTGX-ezoU_AcjsFg0ehvh4sDjxk60c3zUa1qtryRKlhTXeMulXJZO8P-b7xSi7EcpmFu2dazIV7bIChk0olL-4yWyjez5p-AJaDMBxQtiiK3UjpIct2gJSkHKoR56kbkh4h1aTpRvvpwHlVdfEnp_Hco5qJKpoPMTtUeAELQdGUOykFQ45ZZ8nQqIa8ceN7ts0St8BrwQcrfoziU4tVRGireJEm7Z2r1-_L1Gn1vDIX6DI6XRdnBTYshheIR8fOi7nx97QgnZ2jfUlIuop4gjw-LmAd7ksTcJvo-UxGyiOGplJAYke3i8Xll_bj_HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای کاش پنج هزار تا استارز داشتم همشو روی عکس شما میزدم بانو.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/81361" target="_blank">📅 15:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81360">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">تو 5/5/5 تنها کاری که میتونم بکنم خوابیدنه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/81360" target="_blank">📅 15:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81358">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">نیما تکیدو رو بخاطر برگذاری ایونت تو ایرانمال گرفتن.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/81358" target="_blank">📅 14:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81357">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SJdUpUEA1jRsT-G3w_lQqTTkGQJk3dIDHLYA4UzRo8-SR-u-aSTmvfML7i-kuKOkr0Jk6GBtut8dsFYEeJGSLirJnbGyipfsMGahDNbORhsLAcewDbo7GkYS1ZbqGRGEMB5KhNRaVC9KrqVo9Nwg7OpfiwduWAzCQ7ApdW1xGAND2UCL4AaHoK1E8h1EO-bngSPWH_gHWbdwqL9edwU3zPiC03Uqk_xwBzZQ1IHY0XYyHJ88x9ycbJFQzh3MKoM5TklcGu1MJM4CO_aELjtwD_QH6OBsTp9164r3tgQrYIOGE3GKkgGc66VDkAC5ttzeI1XWVXJm3yqXxUIbbqan2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیما تکیدو رو بخاطر برگذاری ایونت تو ایرانمال گرفتن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/81357" target="_blank">📅 14:47 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81356">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lJSKchFY3kwh1lGjllRXeQIUsOZKpxAlXr2xtNI0S5Zsy_Uqw-ivF7f8YimDv8Vu-aiAdOzSexiIfZakgvhAM2lH5udjpkYyq3QTw_Fskn5N8l9uCDNET9nV-9KVERFa6X-s_NTjX69ZQ85nY_-3Ywe4fjhjnutFMNOlRt8HmedRv2nq3ZysvF0WDFsvrAAAxtQwqDJjstGfqHTPisGG4y1v35JdUEbsQDPH9O2Tt2qlstSgPBdAOixJvuOES3htIxVgB4BRdsINAW67QzS0iQeKPy7xoFdRY6C6_pNHMuXTWcr6oQzz3p0gergM61jVGwS4mRI1LNFk1WQNYoQNPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
@FunHipHop
| artin</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/81356" target="_blank">📅 14:24 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81354">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">خیلی دوس دارم بدونم اولین نفر کی نشسته تو فلایت رادار که رصد کنه نتانیاهو داره کجا میره عراقچی کجا میره فلانی کجا میره گاییدین</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/81354" target="_blank">📅 13:56 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81353">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">خیلی دوس دارم بدونم اولین نفر کی نشسته تو فلایت رادار که رصد کنه نتانیاهو داره کجا میره عراقچی کجا میره فلانی کجا میره گاییدین</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/81353" target="_blank">📅 13:53 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81352">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RF91yXg42gszVBV1PJmOINUCMvoNUnAjT5ZJ7T0sb3ObMfab66vWqXcvCW09xflnKYo54QSgtqV_brokjGQSeRkBp58ukvJdEykSV-E2y78_Mg5Jo3hFcHj8jsHN3WvXINFAcNMULHRuqXvZA2vqjS3rYoRfpCz9fqoBkbYruiPTRqVdBFo1zVnlAI3QxQhAV1rYxd87BwEg69QaW0R1OUeFOR-E7SoSboXCujsVUYic4igcz1W8-OIG1x5L1yDetIu3l1V5ajfCDO-ol_WH_-VFW2knfZGU4-arMcgANs7jxe0e8nBbyBwKCdRO0Smo2Ij2NjCRP6mmeEZGCCb6-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هعی خدا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/81352" target="_blank">📅 13:27 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81350">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qRromfAZ8KmHcm1ThVjuiNSUYu-LAR_KYYSjgl_BQ59UAciTkOiQnptJ7qMq3hLOHerynUn6w35h1N38WWQQZ32K4Gab5McHztYucwXssQKCxBJ9pn0a0dnnzVD-zIhzw97eCxOWHJooJ59zqUMU1SdKeVq69518IbIXkeFFJeQ8FQNkEZ8FAtbg4slEL46PiyclAwogo90ow9pKABrA7oHMysqCmJ_BfeOMwiPFDp6UdlZv0hXF5d_G7QJELQTm7_8XunmLXOAvub0dy-nXEQTaJTRgIUznmF0Pl5W-ezGeWZIFWNOZQOwmN__cgto-EmtJMMU5TzSYAHyRd1Jl3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد دیدن این عکس حس میکنم تهی منم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/81350" target="_blank">📅 13:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81349">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">این میمون چرا این شکلی شده.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/81349" target="_blank">📅 12:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81348">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eEWYR8WTVLjOZ4azw66_Ga3OqN8udb_6b88iAvUVVu7csvlcKmj_bAdlfWnC7r42FA-qzT-7fRRev_0U8iaRWoDKhuFJRTh24rgFFpzINnGbAuu_n1Fx5FQL0gnt-RR89I8lzWjXhyj5HewOyLJy49vge7G77mU2kL5PNFa4akrvssfoKJ6Jeg_PxtQmt1dBuA1ro__g0M6I6k7C1MyJfSufdYjJxiTGJtP9XFpFxMnwl4Tk-GW6hx1hmvvEGdE86Al6t_iX2vsPW3qrSOZeeJ2SREfy8rOYgflYNk1q9fa6b0bDM54C9gmeV0_hoRVtsNF26s-qPv9aJJM65JNmSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این میمون چرا این شکلی شده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/81348" target="_blank">📅 12:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81347">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">هیچی دیگه، ملت اختیار لباس پوشیدن خودشونم ندارن.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/81347" target="_blank">📅 12:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81346">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eSssz3HbNGItQJPC7BI7Bcn9C1WkkrS67Ui5ysKccNjv3Nk2ibSG2VA3Ps_aL9LBzomwvEqamJWsbkuxTT_ExSu-vnERwJ708pGnP_lgvhEgHUIqDkkCgpJx5ag8Nci3TkV9GUkabNtxlD-hqVSrSMGsrP9p1psnkOiy1vTnSCNTJdy7sOl8fRc0X8CPN7ccow8DZUZ9I_TLHh8vXdTamh8atHMRi1xeCOU4gr-DWSsIyQvji0WBZr6A8dVWfq9rIVLUYIHZO3Juy41XWfzZB2E1v3zFpfsQT-dYqA-87NtHnS-KH1yWlfGb3hj6ejY4Xm8E5EhKA9V_cT2WQCv2gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچی دیگه، ملت اختیار لباس پوشیدن خودشونم ندارن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/81346" target="_blank">📅 12:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81345">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
نمایندگان مجلس جمهوری اسلامی طرحی را تصویب کرده‌اند که طبق آن، تمامی نیروهای سنتکام و حتی تمام شهروندان ساکن اسرائیل، چه مسلح باشند و چه غیرمسلح، «نظامی» محسوب می‌شوند.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/81345" target="_blank">📅 11:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81344">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">سجاد شاهی پول ویناک چیشد</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/81344" target="_blank">📅 11:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81342">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nZsf32w_Now5Tt06GUtCLYeoJHhvWxqJDRAsqqUIvqFC6d4XKMFuzKXt6jtcqMTb0E1wYqU63EGyDnhA8l17jlxmRsoHHhWlevCiM7s77aSlmJQj__cHlS9nij-rL_aWbmSUy_XVrQBu2Gn82X1X0qPsa9IuRZ7xt-re3KyiQmRdJGqO7Hu4S4JESLrbXLBctoDm4l0Ym7VfbYQUmZhzjyIp_sdvcbW86WTLDB-G0AcBrhjChN_tiwQ9Qdh41ENGWDS51Pp5nd2NjsJWIqlYVRZaBkTqJsk6h5DElM0rhwqZ-vNDjj-TW-fg2V82fEsuCfjU8mGoH9I359jmv2vI8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hfz2lSpGoQJgl4DdCZXmKhOID1BUUVIX0kmMqvtKbFND8SdEJcxJa1Pq-uvibg1vsmOvJBQpXhzkVIhchOsEZWTLKqFx3xZi1EHD8uuQKG7Et8etzSjv96xz32Fdlou1fQatN0UcNBvQUKNdDi4HDXI_832oyFrbzMzaIdEl8zLTZ78XjAZ3qK8LtLO8rB3dgtPxYq6TQXvZkHfy0XI8mgCiCaTwBIBMkrQzLtz9Roeo-ZHSiHYFLVzTBrmXJusdnyOfb9zj_caR-Hl52C21YsFRSvtEWvTevp0uUOluMV-JrOam72GkxbVX3nf2BCPUB5Rg4O3IN_ybPTBM3CExHw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رونالدو در کنار چهارتا کاپ جام جهانیش.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/81342" target="_blank">📅 11:34 · 05 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
