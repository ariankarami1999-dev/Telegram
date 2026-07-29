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
<p>@funhiphop • 👥 219K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-07 11:32:26</div>
<hr>

<div class="tg-post" id="msg-81458">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">هدف یدونه پایگاه آمریکا تو اردن بود فقط
💔
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/81458" target="_blank">📅 01:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81457">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">تروخدا اسرائیل باشه تروخدا این یهودا خیلی راحت نابود می‌‌شن بوم بوم تلاویو اسرائیلی‌ها مجبور می‌شن از دریا فرار کنن تروخدا پدافنداشون ته کشیده ۸۵۸۷۴۳۹۹۴۴ نفر ازشون مفقود می‌شه کلا اندازه یه استان ایرانن ۹ میلیون جمعیت دارن کلا تروخدا تروخدا اسرائیلو بزن سردار
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/81457" target="_blank">📅 01:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81456">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ببینیم از لپ لپ اسم کدوم کشور درمیاد
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/81456" target="_blank">📅 01:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81454">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z1P-jHLxqAqESux3Mlgz_UUo1cRr4nJFP4JuJd6i6WQrWLYj7LktWhXub0NAbzovyePXlh9ENamE6aLR-zyR_lm1_nflHtJXVwsfuXQGbs9GMWZaxf5tq-d0eeqDoqgJkshP-9ChBNAhwV0O1VSNb6XWLUMfQn5z98kZA6yUHEpEo_w-YDUmcOmvm1FxFYcmyWzGU6OYBimaIovG-2uVP8janqurh_UxguWfZVNECWWYpZJ3TepXs4f7mUXwSgX0FeGfx6JExpbjWz6_RArRt1yZseFLlrZuztpF0cvmWCeaoxpSiTp-SbezS363meG9ujZ-A1x3YlP4is-O6ANqzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/81454" target="_blank">📅 00:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81453">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Orsd9WHhucG3uH2dR6yyilDnVkxL1UDR7U922C4N5hHqmqhvmY_a0ZsPnefSQwWzkyD7cjXjGCbT0zexJDYKoJKyN8nJYURlvXlTQ5-Jxyl05zxddsSIVIGGI2mv2TKbMEOFBX8G-EPvvqcFmdhmU0_Q9gK1al13tnh0M0mmui-kHgYdzrx4JPWZ_yT2SHOGcVh_wiuMRhQMxejB2qT1Ed0GVqrEV6S6wT_ZVRU0ZMXSTNh5Xs_LbEHgQ2AnArcnrgKK4Uel6gxsMytjwDNI9B7BZrM2xnUYlWSFkK028Ik5PwsXbFgLd0_nZp0xSU60jVGrFEaYrksp0iRCfMZTfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچیزی برای تعریف ساده کلمه نیاز به یک توصیف ساده و فراگیرتر داره، مثلا خارجیا وقتی میخوان بگن بی طرفن میگن "من سوئیسم" تو ایرانم هرکی میخواد به یکی بگه "جنده" دیگه این کلمه زشتو استفاده نمیکنه، میگه "شیما کاتوزیان"  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/81453" target="_blank">📅 00:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81452">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DdfDv4SEstWKVn4oQCim5YZX8ZU8Zm8gpaq0M1uh7d2x1vW6zPfmvghbChes-5iR5uub-QGV2PnYSaXh3SMHRM84Z7dJihwOekBz48a0UkyTtYE8VtdPc3SMC-qDuTGuU16G0WRaROSGQXNJsd_2Q9GqEaVwvo_n_17pOezmApX-QVN0oSqgVNwQ3fh3dRVwIZWsN8Jdz_l6gyO2zP_iJ6CR2Cno2KGbWJr6f-utSSohb-srNZE1cbcbXgTYNmA-5ZtMc0u8XW36iObHQnH8LcjyB5GSWB222r61lipv3lQXb4HnWXmqHDVJ1TX6Jzb202-7IaTHo0U9K8mCQp2a7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچیزی برای تعریف ساده کلمه نیاز به یک توصیف ساده و فراگیرتر داره، مثلا خارجیا وقتی میخوان بگن بی طرفن میگن "من سوئیسم"
تو ایرانم هرکی میخواد به یکی بگه "جنده" دیگه این کلمه زشتو استفاده نمیکنه، میگه "شیما کاتوزیان"
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/funhiphop/81452" target="_blank">📅 00:32 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81451">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">#رسمی
داریوش ترک کردهههه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/81451" target="_blank">📅 00:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81450">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tvetXyuaYJBn2LR8cmxvn8Zolxm63BEt7sgn8cG6DDQ23hlxZEwQsPkmPTgdtHtVtLXqeMoFwyIYVbg_fd5SE7B_VvC_-FY06y2j8FFH6EcwzNp5bbF4crn6ECApqItfhO3el1teUsk9Zv5RbJQn5iI1Aq7CevDHPTXzQ7q4qT4EVkNc-gtZ2HCSvm4frFHv15Ea4gdmwciT50S8cZ7vH5HmaSh4_Jt4kEX7_IsEuv94ciGqYyT5F9zKh670u8u-4_f8oyjg4voYSoswhPLCMRPxUtuAyIGIgq6qbNVYuZiU4-w1Ngm7H5dPjb0ApADweukEF7wWfK5L1pBBMgaTDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور شاهزاده رضا پهلوی در مراسم یادبود لیندزی گراهام
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/81450" target="_blank">📅 00:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81449">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">یعنی جدی عملکرد ترامپ رو تو اوردن نفت از ۱۲۰ دلار به ۷۵ دلار تو دوماه ببینی و باز از گرونی نفت بعنوان یه موفقیت حرف بزنی نیازمند خیلی کصخل بودنه  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/81449" target="_blank">📅 23:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81448">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sz8lONVKIPB8szW8wugzURwf-HzFe2z-32Izj4-bSEUTIblhMzNjAL2tqUqMqmDrenNW8rWBkKyEaj6kcK1Vj1tuHeozozv_rC1SMRzObeNPCwY99YZDVb2hTprFkWoxyfFELHVb5Fehu_D9GIxz6qtspEh5xeDO8euNa1zvuDY6DXcF0JHly_02BVHNtDaN420P10rJfSk29OHSVzq-bqAmyu6TN-_5e69ndETmk25kMgg_5AXDmLp95FtFQU80GjMxrUW2Fn_Yy8xGwV16Wl27C8WN5Kys6n3jjBeqytrVy7BrfY2BbJLnntiCnrS9naOFKlYYj8hZvagn4XT0qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لاپورتا سکته کرده، اما اعلام کرده که حالش خوبه.
@FunHipHop
| artin</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/81448" target="_blank">📅 23:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81447">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">قالیباف: دنبال بهتر کردن
زندگی
مردم هستیم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/81447" target="_blank">📅 22:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81446">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cNb62683sueE3BuwpNZ0-uofFmigb0KWyYVWC4D-35QYXeQhljaJkTSQ0xHETkhEd8uyI11K5yVRwbVl0QdRc2WHxYEkhgFZ2rV7WQMdFjapfANjC1JSW8qfhau8OPy0KFICdebzGcmlrZs79HLV8mKIzxi68ldvyMR3E-1rELadHugldSzUXTJSJIYCruuoCkZ7U7rVxwH1y41W0nN1DPDLgjVFMj9QRvcJTnQt8jniuXpBC-CCLWHkrllEzjhPuIeLkQz_wGjNPWi7R5khQ3p5xCFzRFvHBt5mOPRED9aZDxDTza7PdBRMJuNZx0XyVYFQlDD4AeKpd7z5oBnNqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جعفری دوباره منیجر حصین شده، هم پرایم حصین هم شایع با جعفری بود، با هر کدوم قطع همکاری کرد بگا رفتن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/81446" target="_blank">📅 22:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81445">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/81445" target="_blank">📅 22:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81443">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YMX2digeWQgUyzhA0-IX0l0t9sOIKFeRpCi_l0jcM1yxGKBtQ_7EopPaD3kdYi4CuEUwQE03KZUTzuzqDIr3nQLdXA0Knb5LQG5Xu6hzC8uRXdlzHeNgISkk1uxfeIMii1b30elDtxqPbYl75b91w_-gaTp1FKuJf8PoqqNk7DjIlu3fVzdH7VCkcxmkoqtYLQflwYERlLCYObL-FQRUlDYbB-lwpaXpEfEKv5NdAniZUkfXTVK0HFWWZgUFalmscK27qYCI_RMf30PVO31SZbar-0XUVlje_TcJMUpgDijwFuntvaxn47TVfVcSwh2OjQPfq5gv4kcbFEIM5G7S8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BmcJpQ_rrEF4DQjhtvnNlwkUGitBweQluctv4fhxqVOP7oZAR3iMLbI2o9Zkz_rButoql25tEuqHPU4l8bxGOVZOOCZSUF456hErwLVfJsFxpSMp66uwACHq9wZhhMkol2z2_rk0KG5PdNrtIxu8K-odZOzYmrUQQBCmEedi7LgHiGI7nLKLcq0eMFdcI5ZVa3z2Pg3hnAxlZeECzLHhaqr3G3e49GiuDyiAnVHOk_XaxGNEMl9q8KIdaWi-Q3H8t9FO9MZDUUVc-RCudAbxgtmw28jx26nI6PMBN2rDxkkjHU9NYaDYsoJldnogqiIbUDOaJpUlKbCL_xmd5T0SLw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">استوری های نوید و بامداد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/81443" target="_blank">📅 22:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81442">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/81442" target="_blank">📅 21:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81440">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QJwpwxyDu3oQ2TTyyaUOb8_f0ohVWUwLHbdzNZOTLGv0yH7V64libAyEvFtuRkebnx6MKewiJtetWOPJYn7l6IkKs7x8HQZTDAC8PF7YsBRi8VTXwdBrtEJlQr_asem-bkJftzwNzL6hNHL6MnKFNVikp3Fuh0qSKAaSA0BdmFmr9JOPgz72-LZpZDJ5ay-4nOjyGo7cThkg86XB0W8BUK9js9t9fFoycxnieyVbgnQJQ-IQD9tEtZBw27SpwBy5pwr9lF8vRoLT7yYhycqvXX5-pqUvzqGM6pGbn2v6YsTItIcWOku-ckdbnRz5A34qRfwuWSV6u2nDdEGBptttwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bQdXWVsGqRyRU_4MeXuEsNIMCPIsq0uyWSXRTIj2KNFTwM-88mGG6CIqyM4cGqByoXRWa2WT7A0ZhsOEEoYVgu5plyJ1UiONGydhFnCgv0fw3xlL4H9Owa3aIzXT4BGvO17Xi86-y9GkDq59UkpvHC6Wn_eigPhzz1ieABiOm9F7ayeixY6bGYfvSVghiNEf0sXNMpx_2gM4SifZez_pWiE1ugL4NY2Tx4YwG4Tm-4s_do2oeGbjlZsE5O6nNHAIPmVnkuhdQWCJf9iAi1wgKPU9OoKPpmyjP1Mb0g1IW05mLtp3EnpjWgedp11Cw52NDjGL-SwFWJCIJVSAPYLOOA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کوکوریا قیافه دلافوئنته رو تتو کرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/81440" target="_blank">📅 21:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81439">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/81439" target="_blank">📅 21:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81438">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">بعد از اتفاقات دیشب شماره مادر سام صابری رو گیر اوردن براش فیلم سر بریدن فرستادن گفتن سر سام رو داریم میبریم
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/81438" target="_blank">📅 21:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81437">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">شاهزاده قراره با بی‌بی نتانیاهو در مراسم ختم سناتور لیندسی گراهام دیدار داشته باشه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81437" target="_blank">📅 20:45 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81436">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EAIzzXorNC-gzfWiaYzk191IdtteB2UuizGVcfC5iqBIT1JiZ0yMF5EmXDEstI3Fh9I-OT0uQO-1bUrms5xd9nIj0eX8HiU_tf6W_ybyP4w5I6LcaOjh6jc0aff6WkQyZMHjaQg1fKiGzVP6pN_VcqiR-cMWHyECO8S8vmzDQrtw9f3hS6ShrV-YrTf9GjpbdU77ixJNkengbRAWBcSEGo0G8dxmuzCRDdICaf04_JeVgQq6DKVc4J-iAYdiR1lHWvPUdvnuYEetSt1L6p6Gih3fuYf1T_KFqOd7bXyWA85Xst-FP2MKO5_cDKL_iwPwRUEZQjH-riu6U30_yGIJnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک ماه گذشت
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/81436" target="_blank">📅 20:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81435">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Numb 1 - Madoro</div>
  <div class="tg-doc-extra">numb</div>
</div>
<a href="https://t.me/funhiphop/81435" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/81435" target="_blank">📅 20:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81434">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GtlcMQH8x-TWT-M9kBkxYk4na2YsYh2VWQelZcDy6H3fW049HoTZSs1dWBifHetbNuuqNP7MNazkcl-jzErffoBSSfTJlkZbAGuRf-Ag67wmB1q2iAbVg32_WZ9v8_zPySTyEF-NzWiWMSL1l7OtVHfAvDtb8SNSp7KbuWHS4Kr_kxt1X5RGOVzUgl2FqHZSBK7x2T4Zhit40n2Pe4noubRTvBm0un-9bHP5RyU6vnUoKTg9VLBaR1_YtgeWKqeF1NZTmC4tN5So-38N_rZ7SfKDTtoIY--AzgowG1xEGrKPftMYhJNHgwr2u7so-q_K072HElQOWSTI1wV_LrAcsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آهنگ جدید numb به نام مادورو منتشر شد
📺
Telegram</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/81434" target="_blank">📅 20:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81433">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">این که ترامپ دوساعت قبل جلسه با نتانیاهو میاد میرینه به نتانیاهو یعنی یه کاسه ای زیر نیم کاسس.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/81433" target="_blank">📅 20:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81432">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JzUBxY0DcoXQfnHLbLV2JY6pJtr6IYNTgwRoUGgJT7uRSufUUH3R5B_moRRwHY-ac96HjOoiZlNCw2lhxBjvoVrcpxp1Lj8_sRaadQOpqQAgjAUnPC2ZJGHyf_fVzCoLKzHN5WLweiYmsi1STipfvf40BLaIzaCTt92qBh9coUkj6NOy2VWAMWymPnPtMj3D2Cczbw7iop5VltK1Z3rTU1KLT6FyyxEOXNxGSMp2GMN1uLmmLUKT51gVuiTrjWGR8elSd41B5JSjfo3r00XJHlCcov8i4-p_noDqxno892xpYZKoi4L6HrSKWTrMfy5eg6j5955qewC_SfRmKq8Emw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این یارو تو فصل یک عشق ابدی رفته صداسیما
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/81432" target="_blank">📅 20:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81431">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ty-yifV0hRyH-RMpk65AUMmZqfztz-VIomMITjp9HgYlI3IHtbS239xe56qaY5gnV5etfdP2UyeLvj6En58ZhRISK7YefH_RS8gp8R-ioNAU6YSTpGUGPlesG_P9ggEDKjQW1s5klRdIAOv6zoxJXRbaoAq5mjyXPtV2K3IyqnKZiWlFqGPuxb9iKJ37y2o8KO79teQ4WYDmzAoZCps0hvvUAJfO8TdkJxXw1Zb8DIUF6Yz0lA9f3VgAh-2bY0b94tzvd6NbtQwepq3BYtA9VC0Qy4ZgyQlGlSGkyirJ4J7Z-6udqWI9iGOaW0fUm9OG9A2uIesjtka6Br1ABsCyEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو و دو تا از طرفداراش
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/81431" target="_blank">📅 19:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81430">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NIUzk7OZgyOjQZcIr4WfikJ3Bs5sLBx1JzDpjGSPjFZpS4bTR0ZCmX0lXl4pLGzQ-WaHzQU7wTmrjAJvvfBq4vQ6XkwByca5WjNnmWRUMPoHHqajYdLiP6yVqPcsKd19M-kqOhYvYk6ZySQ8689Gwxs-MGl4lIEIYT7nbJhHvcB4A3HUj30Jk4CRAvDgv-8f6SgdgQRxRaI7nLjPTkOkRhAuX594694CTM7wA15LxnISfM8Qa8Rlx_GHOdDOOJuGlaHOWdxaFceTw-oaOHcwpQWTQRjPP84AQ43QZRr6n4LJImnZ7QU_ihqAdHQa1FOE1BAqKxzWwDgRg47M9wtwqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توپ فصل جدید لیگ جزیره
🔥
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/81430" target="_blank">📅 19:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81429">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fsiR5q2b4hZdsQJbbhAGkwImeKiRqwuAPKF-EeB7JnBzwD0Ae9HacrIEa9__4cOPdKmJIT7-IeAMx5otwTsaqKzt34FzlA0dEBUmTffJGIA8JdMasD6mzKjSBrN0BXLfZ5ClCAtOFsTyyVpxMkyMCOTAa8DsvOxEOH1TacPJ_Stk76FFFJbAR4_jHCQWgPxvY_7IB2vBjVCTshbD7dEuaGXPq-NikIXRyuXRHSyGn3I9athbWFqv3zpRATAu519u8343QIATyiOcv4d6-HK8IbMWVU5-TMUjPLl_mfgYE_XUq2lkZfc4vFKVHU8GeQ_uommcNfaLI9KGrIAtGcM-TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچی بگم از طنز ماجرا کم میشه
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/81429" target="_blank">📅 18:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81428">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nrcGJUPZ5yC6GMZj4gne36We1VVaV1X5I8JWTUmwycnLP5iayefnlL3v7BIAc6Mj3HjyrqHeffMHmlk-0EJ6WN4IBixIRwsmCtNfOLzov_ADlMnJGl2UtazhSB8DDZAIpxFojQwjZMlfnvKnpgfHdXeDnj-WWw6063LoEKZQwdUwjF88yjTi6M667i0mGfVDPPyOL87tZyiQN4Tj5b9m_0uCG4AKI_YK0YAFZz3Da958nAkVBOecmeGQTmoyVHUyVM2B3uEsJTz6dh-BAi-gGKEKj6Zja6_k-sKxfAgDVuhJmcRD9058sfdpKmeNKHNB1VfIakvQYO-oVGV2PSQg7w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/81428" target="_blank">📅 18:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81427">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">احتمالا امروز یا فردا سپاه به اوکراین حمله میکنه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/81427" target="_blank">📅 17:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81426">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">به گفته ایران اینترنشنال,
قائم حسینی ، امیرحسین ملکی
و
علی دشتی
از معترضان پرونده‌ی میدان علیخانی اصفهان، به زودی قراره اعدام بشند
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/81426" target="_blank">📅 17:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81425">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">احتمالا امروز یا فردا سپاه به اوکراین حمله میکنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/81425" target="_blank">📅 17:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81424">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PbLp6rHDuT8UrC3L9IvsT1hbR_40C0Th8hUoDTXYkZ_z15X-80fkBc8VX1f_0IRIQHlh_FCUQjz1klCDz5CcsGqiSEjHu6HY4_hu1nuV8uT4m9qCLudUDaY2MLkmc6NHo8KuuZb5Uvea5YokrNTMKYeetg-vHV6cyYxhOcr4oF4kwGJekMJIIDbeYsYB1gNeBJIilbP7KWP7OXmyYjD3-np90CrNsSSD6be8wh533xxDbIl-941fyhWlvlFKpcuLvIWqPJreaw4urrSvzkOscLZjdg2OSYuy8YZjIT0cu9vWchsQNz46txIBudsqfqOQulbcB-oQaZ8WHROaYn9UjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو خود سایت کارزار، کارزار را انداختن برا بسته شدن کارزار.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/81424" target="_blank">📅 15:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81423">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">اینطوری که روز به روز اطلاعات جدید تری نسبت به زیرساختایی که از ایران زدن و زیرساختایی که از عربا خورده میاد، فکر کنم آمریکا رو فقط در جبهه کری خونی با AI شکست دادیم که اونم ترامپ اشتراک طلایی گرفته داره همونم ازمون میگیره</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/81423" target="_blank">📅 14:23 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81422">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">سخنگوی دولت: در طول جنگ ۴۰ روزه ۲۳۰ میلیون متر مکعب از ظرفیت تولید گاز خود را از دست دادیم.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/81422" target="_blank">📅 13:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81421">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">از سر شب تا صبح ۱۰ ها موشک میخوره تو خاک کشور
اما به اندازه ۵ دقیقه اذان صبح کشته نمیده
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/81421" target="_blank">📅 13:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81419">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AVYrDhrCCdmSILEjEu7H4lCs7jyM1BncH5nqILB3xTm2lVs5YeIPj_oqmR0UQnB3nHlWqyFZprFgeXlfqUzFzT_0BooHGThWU_-vq-a8XFLYK_qcBTJOqbG3jS_9qpAC37ueG43LoDXztUTwUj229XRi9dW30sGCL1pcXd0ANypyt9KByKIfk6xNhqAfKhcBvzCZJBX_Ykzs5XHr8x08J0KeDZYalwsqEhD2SSniUwOT_C_oWRWoUIDlH-kM7UeZzxC2zfrO_B01scOrOZLX4Af9w1j8ybr9qsgYg939h1YZKWQCRkYW-Ua53bq3ssJsjMHbxjzmP5idCNAeNirX-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/buUxR3gwE9zA95LYOMag5S9vM_lWGjXel5Y5CMpZsYNQ-K7TXrFjkRvR_sZifSa3gRPVn4nMklDyC_cYcZ6PsrB8OV_iO8CBy9u-w1U9LrlcyUEPP1HabNO6n4g7XiCjZk_NBl4qPvDd_dVngfgUi59Q8pDHqPClB9oLbfVMUOLR1kLHBs2Y-qbR3NX1mB5H48QazsoifbvkG1UWndAB-i31r9n8OmwGDZ2wuXyEdqhZHN9903TsIza7OEfR9ihcYjDw1WoeUSheRK8I9HUiWhOTKLK3Zs6nT6iRz4GWo0JkggB1I1bZ-qZ9-HxZBpLrj8yTukw1fgCTUYP1s9UYog.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یکی دیگه از پیش بینی های اکونومیست درست از اب دراومد.
زلنسکی با دوربین کنار یک کشتی ایرانی که داره کالا حمل میکنه، و یک پهپاد هم بالاسرشه
چند روز قبل اوکراین با پهپاد یک کشتی ایرانی حمله کرد.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/81419" target="_blank">📅 13:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81417">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rbN0Xs6R-2Rsm0RC44A9Trgb788k2nNVcXREtZtgceGfI2vOrJ434q0Sbonyo0fD7Sti0vCIgW9zdKhIEFozOf4Zpx-sBMmkZbcZeOxlURRA2ODXGFhd1N__cOoDyKEEUAEqpd9s-c4y03304zLSM41MJ07qLPdyqi0l-wuzKLNJKx4mp9YafVe7e86l2mkclYxKttQnTN7NkfLUgJGefD0I2kau5vmhZbD5Z6_BEQJHUcz8YXy_Mavns0LyqLo4GlxtdDa0QsNzvx3S7RYyruILAKRViFdeqjOh-V4oBWttH5lgjgIfd2WheqJH8pRWeWH7nZ1Gk0PWe05vRcE8Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f171036de.mp4?token=oVnnp50UQ8rNkHEBCcrbIVDmI0_49aHrnVriAhyeqVDSpDefd0-jsxyprvkTfiPJ30nLrp4tM1IwtNijeYCQhzNdj2CJwpDBhI1cLefNRmu-FUgb4ld_2gutahzD7GoluVyFygst-0u0wFSOzL3ghJJcxiL5ZKGnsIMROICS7s-WN_Bmw2QdYhm4__rFDNLUQdPC9XqXeCR7RggitFcjO2keVv48Zs7i5ODm9WS6n5JARjLTYyDSp_db0FJW2O9X0CIOEb9gbJXFRCyfoaWIzFBeLj6dWYcUm-ETB8WH6otfDCKDNonPG3bP6wum1Y7amPq_-glFHJel4xvScgcxqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f171036de.mp4?token=oVnnp50UQ8rNkHEBCcrbIVDmI0_49aHrnVriAhyeqVDSpDefd0-jsxyprvkTfiPJ30nLrp4tM1IwtNijeYCQhzNdj2CJwpDBhI1cLefNRmu-FUgb4ld_2gutahzD7GoluVyFygst-0u0wFSOzL3ghJJcxiL5ZKGnsIMROICS7s-WN_Bmw2QdYhm4__rFDNLUQdPC9XqXeCR7RggitFcjO2keVv48Zs7i5ODm9WS6n5JARjLTYyDSp_db0FJW2O9X0CIOEb9gbJXFRCyfoaWIzFBeLj6dWYcUm-ETB8WH6otfDCKDNonPG3bP6wum1Y7amPq_-glFHJel4xvScgcxqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طقه پوبون رو زدن
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/81417" target="_blank">📅 13:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81416">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DXOgsxjLY4At1lCusUconxcMrOY_UdSC0P-UDbaNk4EPcM9mt_EsvqhiEnAjlXRQHCV0Dw5sqJRMURk8vdtx-bizWhrgqB5P_lGQpTHm7UuOz5a118n462OqBe-JzEt16WI3d2lYqq6VOxNYxTfzx2Dj05diasZ6PHAvjDx3-tNU6f5fQCHeroxnSiNRqS1x9kVhDEThE-QQM_ogoOmUAj7ERIaR6IMuiptUX-Mmk5DPc44IIrwGBREjkZBhitKFdMVnII3wkNLZplJgnsfZLJxw-Mpy5SME_jb_T4sUwXSLOfoH4c0YfJIIBjZNZisXCwajjiRhBmzLCWkkpk4xag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/81416" target="_blank">📅 13:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81414">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce9ff43bec.mp4?token=vYSVSeRhBe8h14spI7EnOTf736W_rj3Jx3J9H7ozH7fWHA1YVoxa-33VE1U42_ubps0cal-jjQjwOk0VukJ4srOJRx3fUKFJ68nWX0M54J4mDWPvKFnP7x4mbjaBRxy_mojPa3NbDhxD_562C5N7Gw6Ex3mHzJy7vCWmmthdLcGE7jJ4mql_sFt7JtRECMi1X2PyzeGO5g_nvH67Qv8TDIR0TtpIIISO_I58BdmiVNbHb_llEUpR0443STjO4YBzO4tsCdsMIba-_M3UQ31MrNpgcXv72o35dx-Wr0n2L7MgroY57luvVpmiKjWYBpwOpSExqgaH0A6tvFrLTasMUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce9ff43bec.mp4?token=vYSVSeRhBe8h14spI7EnOTf736W_rj3Jx3J9H7ozH7fWHA1YVoxa-33VE1U42_ubps0cal-jjQjwOk0VukJ4srOJRx3fUKFJ68nWX0M54J4mDWPvKFnP7x4mbjaBRxy_mojPa3NbDhxD_562C5N7Gw6Ex3mHzJy7vCWmmthdLcGE7jJ4mql_sFt7JtRECMi1X2PyzeGO5g_nvH67Qv8TDIR0TtpIIISO_I58BdmiVNbHb_llEUpR0443STjO4YBzO4tsCdsMIba-_M3UQ31MrNpgcXv72o35dx-Wr0n2L7MgroY57luvVpmiKjWYBpwOpSExqgaH0A6tvFrLTasMUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی گرامی کار قبلیت چی بوده؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/81414" target="_blank">📅 11:11 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81413">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">مگه نمیگفتن هر زمستونی یه بهاری داره هر شبی یه روزی، خارتو گاییدم چرا تموم نمیشی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/81413" target="_blank">📅 10:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81412">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m4GD9C-ctPIZP8LZ9ID-dvAt-s3uDta5BQAD21Jr8VvEXIHBmGeOSQFOqpZ9-TYhWnVMQZH4zgi1fErq0Q6Ajq91OgH3Xlw9GAGvaZMfEam82T2KYSODgBT4s8VmT1dHdZMcp-IQFpJypenHuWyj4XOLQ2V8TQVkAZCZwAbA8orLqIEd_8EwSdRIAi0HiifnVMswKAeqWj7CYA9zzpLRQRTwffgmbQKNYJIyl5p1Jy1P9xsOFS2kiLyFA2eCS4fgL8e_K95qBVli1cfoA9-Rv9H5-ooFA5__qqRhKxH__EuY6wopmbssWxDGVT7SRycUnvYl1aaSwree6XqeAVqzZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/81412" target="_blank">📅 10:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81411">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">تروخدا فرزاد قدیمی رو قاطی زیرزمینیا نکنید، فرزاد اونقدرا هم کیری نیست
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/81411" target="_blank">📅 08:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81410">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">خبرگزاری فارس:  هر سه نفر اعدام شدن  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/funhiphop/81410" target="_blank">📅 05:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81409">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">خبرگزاری فارس:
هر سه نفر اعدام شدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/funhiphop/81409" target="_blank">📅 05:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81407">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">از میدون صدای الله اکبر میاد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/funhiphop/81407" target="_blank">📅 05:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81401">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">درگیری گسترش پیدا کرده میگن با ساچمه چن نفرو زخمی کردن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/funhiphop/81401" target="_blank">📅 04:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81400">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">اقا یسری گزارشایی رسیده که مثکه مردم و نیروها درگیر شدن و فعلا بچه ها اعدام نشدن
تایید و تکذیب نمیشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/funhiphop/81400" target="_blank">📅 04:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81399">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">مخم کار نمیکنه نمیدونم چی بنویسم
فقط میتونم بگم تسلیت به خونواده داغدار و ایران عزیز
شبتون خوش
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/funhiphop/81399" target="_blank">📅 03:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81398">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lRHYA9ZjH1PT71shHf6v788Ctg1UALAolCetv-2zJ0LYcIUM6X1FZajODz1WrV-813XfpW7gMob3r6e8fb0O_xaNUoe1E-Nd8fQjpVvvavnfm40SDUvo_ONi1NvQgEXu2UWule15pbB5PYy14QiCzy0wK91GS-68Hf06x6VPP8Y0Pg1DyeB7PcOJmQou_-9A_SumKm5agJt1J-_j1cqmo7Ok_BAlbcdvZEjVaY4wPWHuOka0cMk2ctHqpeLbcPTB8hB1z_-DMmDS1866Hoop6n5yX4OW7lRux_Jz4mp9Wpm9XMlScdT2cXc-9h9n_nQl-rpGRP4Qr7hzC0G0IxnCbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کپشنی به ذهنم نرسید کسمادرت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/funhiphop/81398" target="_blank">📅 03:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81397">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">اذانو زدن
🖤
@FunHipHop
| artin</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/81397" target="_blank">📅 03:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81396">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IuqrGmK3ixg90GXVPEH7WYg8T_xr9Oo_Ve_1a2PjHBRxNQn9PHFb3G-2NBgoESEpmB_3DZPIsDol_jq9_r5a4CewGy7lOkSe5rNe8Ks4mwnnat9gKhsTiF76IPXBzjuLU5-jOvIKagY3rCxkD1Suk9vu3hyYiOdhMqdDzvMwamedvknWz1QpwygDN-3MXR4rEk1sTfCVGSjj1S5yxrvTmm3Iz3Ns0Akc0Y3qn4lb3K-5rKkXUOuaZg4gfJB4wFhfgFr03PXGkvv9x0rVtkYAGvvid3SQP4UC_30ijUV1Mcjk6zao7YYyBdidHL7kKcMWS2L-KIS8eZJBwmNpvmVeUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/81396" target="_blank">📅 03:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81395">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">اذان صبح امروز اصفهان ساعت ۰۳:۴۲ به افق محلی است.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/81395" target="_blank">📅 03:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81392">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e358934688.mp4?token=eHrotbkjvC9BxxigpmT4UqG_sCKin2E454yal34WbfZOwljPgEunXia6icXvB4nOlx8_IrSRSCV6KwfK9uq2Ihz-cJ6tlkcKvYWV0rk7QEyeY4s9Krg3lG9AkmM8PE80ivmY1FQXV2df-la1rqnDyHpCY8GQasYKFsmtM8JRPyzSNIZPFo2lBc-RQeBpPzFi_YGCl-n5CzA1R8yMV9mIekEwJLeieSNfECU5FzaAuvFchu7ERnVdOX1kQJrjvtjolVY_in1UWDh3d6ivGLCd4yTgwRVoJgPrJWD6k2WQf3hmKUQckvF8MjAsACUzzEO5d8zwAoNucIVmWQkPKL5Aqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e358934688.mp4?token=eHrotbkjvC9BxxigpmT4UqG_sCKin2E454yal34WbfZOwljPgEunXia6icXvB4nOlx8_IrSRSCV6KwfK9uq2Ihz-cJ6tlkcKvYWV0rk7QEyeY4s9Krg3lG9AkmM8PE80ivmY1FQXV2df-la1rqnDyHpCY8GQasYKFsmtM8JRPyzSNIZPFo2lBc-RQeBpPzFi_YGCl-n5CzA1R8yMV9mIekEwJLeieSNfECU5FzaAuvFchu7ERnVdOX1kQJrjvtjolVY_in1UWDh3d6ivGLCd4yTgwRVoJgPrJWD6k2WQf3hmKUQckvF8MjAsACUzzEO5d8zwAoNucIVmWQkPKL5Aqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/81392" target="_blank">📅 03:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81390">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">معترضین بازداشت شده با اسکورت شدید مامورین برای اجرای حکم وارد میدان علیخانی شدند.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/81390" target="_blank">📅 02:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81389">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64626deb37.mp4?token=S62N9cvLgyuEVxhtH8NLuFSWAFIleCduM_KFspIRaLdeIgXetC2LLZNcouovDJaGiNw2oAdi_bFGNS1lWDb_1ptcyHd-J4P2M1OXXE__F3A7Jaj9OyK-HnzAps-RfzdepvFDeDGOo9U5CsXoTuyUvCszOqiugTEpwi4GVF5t4RKoPYRAMwqzkavM7jtSqOO8zjnyDIX_lwzQ0VeSi0N5nN8aytFWr38FM0JMCOmsXp7mxXpnOYP56tpcBPCgLmU0aIOZRdlNg5ZxyB1hFTr5vWeVSgVS-Xx5LibxkKNVFtol1hvpay1wB2C1fmkgXo2N7QsgSlmKVov4y6Oc7761Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64626deb37.mp4?token=S62N9cvLgyuEVxhtH8NLuFSWAFIleCduM_KFspIRaLdeIgXetC2LLZNcouovDJaGiNw2oAdi_bFGNS1lWDb_1ptcyHd-J4P2M1OXXE__F3A7Jaj9OyK-HnzAps-RfzdepvFDeDGOo9U5CsXoTuyUvCszOqiugTEpwi4GVF5t4RKoPYRAMwqzkavM7jtSqOO8zjnyDIX_lwzQ0VeSi0N5nN8aytFWr38FM0JMCOmsXp7mxXpnOYP56tpcBPCgLmU0aIOZRdlNg5ZxyB1hFTr5vWeVSgVS-Xx5LibxkKNVFtol1hvpay1wB2C1fmkgXo2N7QsgSlmKVov4y6Oc7761Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس‌از اطلاع رسانی کاربران توی فضای مجازی، جمعیت میدان علیخانی اصفهان هر لحظه در حال افزایشه.
@FunHipHop
| artin</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/81389" target="_blank">📅 02:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81388">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Svv5YwJwuOdXLmMBx75djX0fSw1e69BSuMlUeePX0-UhCIhKx0I8svRp_uGz2JHBB77hQemQ-6Yvx1yc_htopiyq6DBeRZbA-k_8u-oTrCQXajo8mGFBX5OajspknnkFqcom_lKKNGqtCMIgKNFSnG-PsKYL7vUV1BiTjqyVrKgbaL_NrZuiO8joANFpOEwFDuRixZoFSt4jtRXBA4Awq1DLLy8hQ8c_mjzysHg64L-cuGtRnmSvNI3VcRzaNRLziyxdqv49XHJmg12IUuyGBBYdh-eldHIWtps_rZrE99NaR1F8UyvNbpeL1gD31RkoHYeftAK4JRJeBx8pyCRMug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این لیست کامل ۱۲ نفر از بچه های معترض اصفهان هست که ۳ نفرشون قراره در ملأ عام اعدام بشند
۲ نفرشون هم در تاریخ ۲۸ تیر اعدام شدند
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/81388" target="_blank">📅 01:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81387">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S1DEZc0dtMU5pXHhYHboGeAFli4Rvpv2eMcgDDFyg1Hm3ben1C3CHee4q0W6SeagDkNf0jq8iRvcAjmMV1IxOqYpKkLj5u0Sq-yPTFdTv_fcx9NnMbmRg7Wd47mgz30TgxvJO95UFM9jD0UwYGZjTbt5ct6D1pUVJAjBLXt1n14l99s5OWyiaaM6yvQqTeELsVNApEuU1Lq9Fl-_sSekdG9UgQCIIvt7I3jKc6UzihJ0kd79KdaAJM86bHI_UyHqGUlE7erMfrErychCO7wT7Y9O2aBtfED8MVuYmVevpUyZ553Pj2tqhtq5-kahVqfMpDNtGPhIKe2fo9c0Dddi1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بنرو تو میدون گذاشتن.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/81387" target="_blank">📅 01:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81386">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">نیروهای امنیتی رژیم تو میدان علیخانی اصفهان جمع شدن  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/81386" target="_blank">📅 01:24 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81385">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aHhjrD2vEJSKGhcN0ZtvttobqwUMgzIhbgA7e61wnDoMPhVwFaQphTf1zxt4tHmnV8cy8nuc8iTDjmccb26aP8N4BgoiNxf1WAcvEZjI3tfMR989si46GpJ1lKbhHlQI_BZp2Rg8M10aMHxnhxNWDB49zWja9sv9UmSpmbgsTsPMukqweP9Aw-8wKCzTOnV5gp3FOKGZPJ4JuDJWO-Hq4ULRZSil7QYbIcYltD6dMKQ_GxOS-cAsrhJH1jtuhkrd9OJZxomKDrc8ntmLO0Z5zyKEuM_E4AY0S6vAyKadu3gIQXqRaVtHVOBwI-khbdAIgua3Zk8Dc5Temcugfzm-Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروهای امنیتی رژیم تو میدان علیخانی اصفهان جمع شدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/81385" target="_blank">📅 01:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81384">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">از این ادمینمون فریب که شاتای پستاش تو جنگ ۱۲ روزه تو کامنتاس از ۱۸ دی خبر نداریم  @FunHipHop | Menot</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/81384" target="_blank">📅 00:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81383">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SOfExcydHbexr4Xkw3Cep2ymqy7fg4Cs3objl_ei-hRwiHvj90xC61V0r7B6KNE2VPaReqFuAcIno9WR56HNfMl71dVi1uqYTKMImN3Yxdlfs1BjK4lbmnhVlV47NU60DnLmYTAoOVXvT8tsWMIPfnzbPCeCHvt0R1vEasyt8TVpxcIhawjmRsMtQp0GIOXzzN-eLYu36RsC5AvC7r3vhLVVeVC3oVLjZmForDG5cPRFM7-9jzUEbjZqZ8CCitgZ0N6Ehi8WcSGIY_sQF29fQeUQF4C19oPZ2iYkXf1tQ8HQwU3GaZvPESmz_Yu0rwcc9ocF-JbJizOTrK2D742Iow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حاجی این دوس دختر علی سورناس
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/81383" target="_blank">📅 00:44 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81382">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AmWFYsKt5MFGMKGX3DCt34alatrP0e9B94BgFSmn7ye64lW3C7JyG6nu8F_z-cuIEsiZyTH8MzMP9ikrnyr797YbTQhwwcHNQazJ5j5jhvYyiUulnjVhV2DQ7D5vshVhJW7kBzc4QuTSMqY4qrDcxqxeTOiWsqQXTWIyT9VdyfHG5SGMa5Dlb-ON_-VeBIx-8YJuHli69yXRmGqmnAlq5l1AWQD040vmhn7TUXYh7tFO4jbHJr9SkkiGge8c36qFH6fU2Iw0HUBXgpUhcDM1KK9FAKwI6as5ELlQmtWv2TVuyW9iJeHOA0nLCGIh_4voolpcJzMadg3y4KkBgjQvLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم اعدام ابوالفضل سپاهی، علیرضا سپاهی و امیرحسین صفری، از معترضین دی ماه در اصفهان، متاسفانه فردا قراره در ملأ عام اجرا شه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/81382" target="_blank">📅 00:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81381">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SWOkgSb_ysXm8zxrQaZnJHZsh6tFZvPI180D52_Pg0YUeMobvy7EhzK_7hKjI0_VeeADYj3uzNlICZh6iwJICXAclzVcNwq6GudvMu2wkwFBQ3PXKJItQoUCQXbBqH2WfxMNGbg6cwcaRPmQi1XpWkq1OXpJkuVx_YE7vfaZ0_37u0DPpyvSZ-nqyFXdXxBXZAqnVPPGAmdsuyNLzaiKrKNozfS7IrEYKZjRz7OuYja6zaVW-GexfTzJXEUFjh07fJEwj9qiXPfbmi_i5wRQKCD-oUgCTQJxofl_KbiFqiVkJXjU9_XI2Xx-ss5L0i4H1TsawBjg1eljw23L_MWT5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری یانگ کید
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/81381" target="_blank">📅 23:37 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81380">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GWv_AxNtdQvRxQd30AOmwbNT381BumF1-9JiuL7dW5mrxOyirGlA_oXtZPfkOSH2xfoNVURYPovepAxEoEUNXpzlvadC9dfzZJNRSw7KSZL2YMivsy0XtDEIg9aK-aaZ5GFAUFgRk0NtodFUfJtOgvWGBeYHux197DMgQalJLVwSPxKOZE4NRN86AwIxLjVCpfx_eqrjZ259qqycVx437gf6rZ3V7tuZP3jRMtUp2xKBgxYRzuOBfNmSnkzBm4iNtXEeVuj8CyfVDaShtSn9KLz0I9Dj1l3MP8oxGCdkcUX2L9O-FHsZzNYEYeKqXujGCrjtMGv_yQ4A_w-1g2aYxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراد ویسی بالا باش داداش کلی تحلیلِ نکرده داریم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/81380" target="_blank">📅 23:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81379">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bQ6BealWwZnMJy1i3_ID31aCMH0096LwEu-tfDOBbAck3CUAp97jgbR8_lmDckQcJDH6PMZHGxPQPjFBcHuGXdg1cYKuGpNXEniSk1MjDBRDxseUypMHvMezw73dKMq8qr8-j17c7a_XFkozvuE0g8-nnrBBsh4MhCH2SrfCmKpxh8yySc_frOlFGzCeKKBPPRkGmIbTr03vTOkqNLxfCdLUf0TwXNBqEr8eSdpT22555KDX59tY4Ag-2QYME_e4dxfOJ1P5zLbQEfR-J62dD5DwxIZIm2nFGRcwxx8FgI3MSIlwRzBNzxfqTdfLgjusTPwQmodszh_3ReIOc2xiZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلبوم جدید فرزاد قدیمی به نام زل منتشر شد.
SoundCloud
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/81379" target="_blank">📅 22:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81378">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">نوشته تابلو توی عکسو  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/81378" target="_blank">📅 21:56 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81377">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o4LAxFPTQYS4cdJB3blvapb3CXuJipxtWupxr4S6nxSmvm-5sWwr4M7Y2QTauz5TvV2VLBf7C4sNqm-uSuAr29a_rKcHnt4GmSklVra1nAqVvrNJSrqzhq8QWUJpgqHlDD1ipPkbD35kccsCcS8nmVYANJ4Gk-Icsz2Isy2lw-sjPPg0XPTS3VfdPc4VWqYzS8JQB6o6WP9j7YDadS_WBQZi3VawQhLugiXi6kUBx1A9cFdRMhh_u1-70LxtY4yeo5cGC8RlmvWCxtcGJqc1mKDHD1fXuOonNiAkL1rBCsVS0ILOSEhQRAqmjUWBNn9RchBa6fkFSFt7gaXZ_rIA5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکا وقتی غیرتی میشن:
Gay rat
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/81377" target="_blank">📅 21:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81376">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fd_lXiih4JZFxxwDl2lQdNNzadY0EhQg1JEVFZVmzGXld0PbjSxfw7WmloQXMUpNp5JYdesXumXgYi7l6x-XlAp_IA4khWKLWO9g_XuVNtiJz5vcqEM7RjN6ERA0QKFFIQqNvYvApGNnOHgvwpTznRhLst4Ylzp5K98eMwL9libK2289wnZkI5G31KQofeT7Dox-rqmyavGVNeCzxXgqhOLA494F2wOsp-PoGS6GCNaOx2SiQYC_gK9WtrN1St_v6DMKdVIHD9D2kEHTsTTv5452GYVZG5qN4nfCt-kPAT8THz7W_ZM1gwfMRF5i9816kAXfgsI1pWvEFx950WFqwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/81376" target="_blank">📅 21:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81375">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bVw2Nd_3N6glwxZoSVl4LFr9PpX0qmAihB6ih_Lhy0UQ922NP7AWSETUmtLzGP4TO9cEkCdWWqiKvMhDVT0hI7qC6rbJS2IML0c1DwLKY97SUV6KZ4dFowLEfmjDnrJxmXE_bltTXGWw-vqNjEF9N2BfOS1x-rts-Ik3rnGN0nLo7gilCNlgSU1nM3JrHXE7FsXwWRe9qGB2Q0F2e_g9gPSgAZvkdGN2bhH-o9ImJryHOuvdel7MNU3ovGGKTbDTXLn7ZBxsri7JBRAXgixe16iA4dazt4S6nRiWU65P_wDgezezenosMq2OTLMz8pmacQenZlwX-aSgzQWgw3Q8Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوشته تابلو توی عکسو  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/81375" target="_blank">📅 20:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81374">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S-TIpzJCXcxYzDXo8M_KBBH-f6U-hfxcthxVOdebJVL6e5_zUoEVutrDOC3d8lyBko9vts5zjFbefXWYu9wURbXly3U927oS_MTb5Xab-LQk6UDa4VWbSws5uWrZZdi9tV2J4fuss_L_7GDjnBsdrJZctDJ-pv7UPqwqrEMlEtvAkTaHieUl7N6Pc_vYBI4e9YG9yZRKaGaJbGG9aYIqntteGfyhpz3o23gr6TiaZEDdRMTV2PoasvGxxkeX88jNQdYcrEbmf-AUSOOPTYIr2KzfTLEQNFioYSdApA4bqdt0f3WV9Loga4JBJgyab3XbC9KIwGBRfLJAMLNxva0uDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوشته تابلو توی عکسو
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/81374" target="_blank">📅 20:48 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81373">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFX5GkiNcaztKCwfVjHq0Usj0BPSC-SabH02nHonfiKKX8GJKQ-Q8D-XOPbYz6FnuOL8aYdVQG8aJxbgdNgB-koi_cNIvzofRtUJOwtzNEn68qI6KnHRZr0GNWL8WXwQ2zYaGKrlPdtKsES_RS5hWfWzLIkAeNLrKcOoKxM221MKirF3WIUKC8X1Fh_YDhgPQOckp7HuNizoVzw23Ylm9fx09Nwqel9QjNrfsYuMgBmYepKEGfIdRqPXl_mFe3zMM3ZaLr7yOFz6INICB49_GhQgXStvL97OeboxUpYAqxmmjN0WWNEb4X--2JoJYqgTBfhlrnotQkkh__mIGwSI9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشمام پسر
خلاصه‌ی مصاحبه‌ی جدید ترامپ تو هواپیما که همین الان پخش شده
عجب حرفایی زده کولاک کرده این بشر
👏🏿
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/81373" target="_blank">📅 20:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81372">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CEGl426BpiW1pHG77LH4_FsJzF3nrOzfufFuTiPK5c1buGbsGdYnDbvsu6R5vth-3_yWBTtmcdhsr0R7D7OQUgSciRnlwm1BBwlQ_KR2CakPAbpfZsfNvykBPqrtsd1Pf2vt2pHvR0KGElvArQE5t9SrMkpSs7M9siW4eykuQdHWSupgOet1vlDY_DTxGNM2bNpqjDclE4Dq2_WQtdpVkdmjOyrWjWUhpfw9NRUOB4kgw5XxpPjfcANLviYodfroV0ip05_yrNk1N2KVl97aRlXoHBcp_9sFvF--96gRa6aGU3rOaCjvvkCzONGZu1CPjJI_0gm9Z3mgFCJcCyoLhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیما تکیدو رو بخاطر برگذاری ایونت تو ایرانمال گرفتن.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/81372" target="_blank">📅 20:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81371">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">خ
دونالد ترام به شبکه‌ی ۱۲ اسرائیل گفت که آمریکا درحال حاضر «گفت‌وگوهای بسیار عمیقی» را با ایران انجام می‌دهد، اما اگر این گفتگوها موفقیت‌آمیز نباشند، ما به اقدامات نظامی بسیار قوی بازخواهیم گشت.
زمان زیادی به دیپلماسی نمی‌دهم؛ یا این روند به سرعت پیش خواهد رفت و تنگه باز خواهد شد، یا اصلاً اتفاق نخواهد افتاد.
تصمیم به توقف حملات آمریکا گرفته‌ام، زیرا همه کسانی که در مذاکرات با ایران دخیل هستند، به من گفتند: "خواهش می‌کنیم شلیک نکن."
ایرانی‌ها شدیدا می‌خواهند به یک توافق برسند و با توقف حملات موافقت کردم، زیرا هیچ چیز برای به دست آوردن و هیچ چیز برای از دست دادن وجود نداشت.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/81371" target="_blank">📅 18:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81370">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SR5wG5Uo60CcNFC65fbWh1Mf6BME6xvwTQ9UsQVa2feQaFSPSjgarMW79qa44R9nkezRPv1igpxl8D0Ps2xFthAL-OQWDCefqebXC4_wCr-KN2mJ8WIBrYSdZftZDpn65Hw6jnK7CUmD613mcwuE9THHtdxZtXsIpIgVdgk0YGo8eUaGjS1DCRD43ndTzrcClMJ5Mf-h5fOEQYC4olwlFy_5S37zxIJVuZCV4B9a2qQX9RZOxy-59RyEm7_xU71ti8dVT6rHzEVYxtNW26ZgydMipChOUIDu-uMxmuOaSW8Kdn7cycMTwzmaQXOJDW9u52-zlu2vfNAuF1SbwroB1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اندروتیت
دوباره به جرم تجاوز به کودکان، پورنوگرافی، قتل، قاچاق اعضای بدن در میامی
دستگیر
و راهی
زندان
شد تا بهش بگن کصمادرش چه رنگیه.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81370" target="_blank">📅 18:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81368">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GtSTIVX_D_2-iQ0fTyPk0s5vm7fBPkJS8AOt0mUnJukbInkDwmVSGr09jyVD20h4ivGRjCfpAyoL4dcvWsCi4Or0KDrVQsHFVx5G2ap8Z_OBiSsiZsBnfEG8vCbjF_J3sQWkNyM01yF6_Ky3U_qpK2EqaEUuOW6uHbffgbgEUXkZkPFIcxEfmRqPt0piRtNUIex_VC_d_iCPlr-sexzBmemAPiTjGpU9GGi09LC9IvZ412IZ6r5pK7TY1mCUsmhv6zid6C3OsPkpF2L80ck-9thP5Gj5RfqqR89FopbhRfJfkghB4Oc2LGYFh4nreK42_pUhxJjtOUVB713RuMGk2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I0EcLl-UKN1JWiiO-Xk8YdEOhh40Ucj2Y04JgGlkET9BfyIAn4-awNb2z1J_aBXTQ3y36PDNkIOOdkZZo_9qmeuFUQKbHUuWtsTxJSGK0m7FKk0uv5rYrKiSVpnPcXahCPZpFJ71fWajL7S6xkCKVUIFXqcL9jia7UEkK7uUU2VcI5k0M7oCtpc46QVYHqpqSB8POJIJEkgopezGJAT6Jr6qfKY_SyslpGxJFCY2WmzHy9TW60NQGBqu4SoICUgmTrMNe82370ioJ1eto9nqhZaAkIN9xvt-K822qyGaxMbyPA7cBfkbvtLK0BJk7SW-gH58lA1josIUhjYTJFo_bg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رومرو درحال رقابت با صدفه
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/81368" target="_blank">📅 18:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81367">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q_UjSAy2Vey-GS5OgTH8wbDL-r3KmjrwOtlQnEcczaoLDnK3OjqBTrM0Iki965MYCisEapSiHiznS-S7_XP28Hg0QJi1KJDZZFe9_9_sXMgRJNGO62vfPNdhKNxyL5YrsS9KsJroK_go7mQ_F2Ns1U-TPKTspyhW8wEWWlN-ndqUp1tkaF1zLc2665-T9v9QdH6P6NwOjO96AwkELZfbc80PCvqc0HkOHBBCZ2FlXaCji-aS8988Y6gbtt9i9eP2vBYpdnI5tHB4EC6BXcHfMaHoCYFSbjcXjzwB6jcVkV4kzHg4xduH1VnMFIXZEdfHWUrGObWs-XjUhCy3ywujpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
گالاتاسرای
🇹🇷
-
🇮🇹
ونتزیا
🏆
رقابت‌های دوستانه باشگاهی‌
🌍
🕔
دوشنبه ساعت ۲۱:۳۰
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
گالاتاسرای در ۸ بازی اخیر خود مساوی نکرده است.
✅
ونتزیا در ۱۶ بازی اخیر خود شکست نخورده است.
📈
میانگین گل در ۱۰ دیدار اخیر گالاتاسرای ۳.۴ گل در هر بازی بوده است.
🧠
به ساعت احترام بگذارید، زمان هم بودجه شماست.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r5
💻
@BetForward</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/81367" target="_blank">📅 18:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81366">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">کانال ۱۲ اسرائیل :
بنیامین نتانیاهو با چندین پیام مشخص در دیدار با دونالد ترامپ حاضر شده و قصد دارد تأکید کند که جمهوری اسلامی، به‌عنوان یک هدف راهبردی در آینده، باید از میان برداشته شود؛ زیرا آن را منشأ شرارت در جهان می‌داند.
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/81366" target="_blank">📅 18:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81365">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b69a6c155e.mp4?token=hUjM-3m5GK29Nv1BEYpIVOwQGNDgUuUHOrm97kU2KyWKPqf0tTJwdep0jfhd0rFVsD9HiOr6n28aX6TAyRqSEDprSRPUF7-BiJxuXKtac-uVf4m0AP747acgGKdEgLcDQJ6IhY0KZgjcwygBnkfDKyf-5yt0Idh79ok6aASfGRcEnykM4UVV8p_Fm_xQ8unNCHPknNJDYWkRjq6VVKriXqN3T6sLaGqJiTU1rBiIMdQRA7tq-YGUesskMnGX3xkBah81YR9aAuX3CcyoClmd6oBoFD-4FnyTvwzONagzH6bOdASg2DhEfVursFxPJlhWK92H2saafcNtJR6MkolUhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b69a6c155e.mp4?token=hUjM-3m5GK29Nv1BEYpIVOwQGNDgUuUHOrm97kU2KyWKPqf0tTJwdep0jfhd0rFVsD9HiOr6n28aX6TAyRqSEDprSRPUF7-BiJxuXKtac-uVf4m0AP747acgGKdEgLcDQJ6IhY0KZgjcwygBnkfDKyf-5yt0Idh79ok6aASfGRcEnykM4UVV8p_Fm_xQ8unNCHPknNJDYWkRjq6VVKriXqN3T6sLaGqJiTU1rBiIMdQRA7tq-YGUesskMnGX3xkBah81YR9aAuX3CcyoClmd6oBoFD-4FnyTvwzONagzH6bOdASg2DhEfVursFxPJlhWK92H2saafcNtJR6MkolUhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عادل فردوسی پور:
من فرزند رسانه ملی هستم
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/81365" target="_blank">📅 16:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81363">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/faGcaOEbfonxGHR2L0jVys3rYqr1Q2gQbdA3VIwd6eRj92HEG0k41xXaJG7tOtfQXkbB9to7slz-DU3MB9FCRJ27JXCAZKywPArcjytAk8vk2knO61ZDLUQVYVAoRp7Q3P2BGa-WNcKPg8a-npssCSUr2x-HqKAzl9FYuJBNq0HrftIgGL-NX3dOb0c5nh6x3t03BJOaFQNit5HQ3_bRoy_E8MZQ_9fTIpY5NYeEiMn2DTe1YZS0ml1eB35QsfKXcKsXGlvBHrEeeY1Y6MrdJ5egKyTX-oIC43PdSziSoickyIzMNDx12EpHt3RJo6A2xM0BQp6y_2fbJ140re8mvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام از این جا سیگاریا برام بخرید لطفا.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/81363" target="_blank">📅 16:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81361">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DYw0MuVKPOIgaTTv9eejSdTsr5R9cZjUOUCjdoi_0pdLhBr8jrJBcyIVL4NNxYgdW-DIqIy2R8NYIxqGJhiF3acXJ5O1wbhW8zdeaevCTZvtO20ZWKlk4uGd3nQCdqGNgq65QHOyfQqPPf1M8dICHp1tCdYxE94HacIL3wMgcaBg8N9oh5C6PbpTNLEeKPqLjUsVfp2eVYviBIy2YAkJ4ykFYGZ26Zrt3NxKLJF7yRQvDe3y22iPUHig2YmK7ILrA89E6UxXmIqL0rp3ECYesoeR59dJLTTpnKDsLqpX8SLv_9WuNOukRqtXHw5f0cFx3dTpEq24jCvnTn5ELi9lww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای کاش پنج هزار تا استارز داشتم همشو روی عکس شما میزدم بانو.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/81361" target="_blank">📅 15:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81360">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">تو 5/5/5 تنها کاری که میتونم بکنم خوابیدنه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/81360" target="_blank">📅 15:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81358">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">نیما تکیدو رو بخاطر برگذاری ایونت تو ایرانمال گرفتن.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/81358" target="_blank">📅 14:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81357">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F-vjnrYmUwXTvWr98sHJ5VSUpRRiBUh9kGATkkgipU9qwUOXM2PpFbEfDZzoWNvB5dnyu0AnWPAS2vZn7kB_n4p5ptjIWrIzFTCxkoOufaEZ8ULhN-VtUGbo-XliU22Z2ASNbfe8x_oyJxdjEj0PKIw10MgMLExMNz8-98KW1DAj-ZSz4MYaMGZVZYC96o0hhdc3sbWKADHGblTd7LYt_k0MYJCUQHY-qp8ch96CatePFUhmmgHwn4uHSC3vEd4UIb2KHL-0IvbYGlbJAOxVR4LsDXlHuAKgGz3Db2KYKq180rTE6NWoVBw-pjjzNIbpraNHxyWHHsE4X3cXXM9NQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیما تکیدو رو بخاطر برگذاری ایونت تو ایرانمال گرفتن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/81357" target="_blank">📅 14:47 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81356">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f7BcSN6sCOwBfCqc1t_JI5bLZsTVHjrjr_1yKX20wZGl-h8CzF-W_u1gjKaWvWMRoedfWhuuPcVdLf0NGS6Y4RKoV7Ch9dqYhhwuuTEzhiuKX3Ff-ydW4jA1iZwRQe-3fx5pR4ws7jGE9xmDnIoKgAWOxOXq-mNQaW7ioN9xaneSlxBQWC38pRW_Id_Rr9uMCVRI3qsQFJSg9820aTC8FlRffjDRASQ-8Y0Nb8ZB1wsfYW_Ns8UvbddMyu7DbAEpgW_p9MZnQ_IV1Yvhg8zLlATcqLMhTSHWE3idrxBDCl-cYnc6IGoBooK6s7gJbzFzuqRrvZf8jm4EQvbivWIAgw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">خیلی دوس دارم بدونم اولین نفر کی نشسته تو فلایت رادار که رصد کنه نتانیاهو داره کجا میره عراقچی کجا میره فلانی کجا میره گاییدین</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/81354" target="_blank">📅 13:56 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81353">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">خیلی دوس دارم بدونم اولین نفر کی نشسته تو فلایت رادار که رصد کنه نتانیاهو داره کجا میره عراقچی کجا میره فلانی کجا میره گاییدین</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/81353" target="_blank">📅 13:53 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81352">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B2M2IIETjz7rRz1vjCLhLHt1XeG9RHSu0K3PlAGIyy9Nl5fsFa1erbj2a_dSA1e44fb4HP5M6EoJ2ASfd6cq4esH0Llj6VtugxtYZr-24xrYRseY3VnleDGaY6nIDIGtZ32ug_hkSseDzD5NxEQvPvKxRJ5G6iZIyFHg-zq9c2bElRS--LGF3A0cOjutUA_JkMkAx5k7-vTM9HfkklNPIKnKBg_-z5Z3XyjPwHgP1hv7x2UkycyVBbbx_SDtFrGNCgBClClzwGsaSP4BzQCY10aj8iU4yzhmOwVH1UEfHTGrlY0rojE4dD95AuhaVgfNBFthPIwQGQMMs7bIdj_Aeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هعی خدا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/81352" target="_blank">📅 13:27 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81350">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qrkahtuAREJVI7SOjj-pLwq0g12jK0HQO8SjVc1U8yBxt2pq0wd6DtfdxqnYtTEkZojFoOyPFdiMNz4iWtpn9_7YiIHx-xfFyn653WcfDMbtMGUwyBTz9KGxy_ldoka9g7RzWCPnfNsh4kfaPYXmwCSj6qIuUHyWgI58lHxwC0ZhOH1Vkh_nN7PpYkulKmw3GN5brnHAQluKTfg2vTB8OTl-8H2GEk1RCmHTzf6CGFJSrevH7xvQJ_pw5NpA3K-_QXAozpzavRMtp5y3DijReUZ5ec8fuf7rkUaimOhpqSVg0vZwJPA9VuCv9uqJ2WvA8vFIrMfRCuvWOQBmGO8nOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد دیدن این عکس حس میکنم تهی منم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/81350" target="_blank">📅 13:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81349">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">این میمون چرا این شکلی شده.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/81349" target="_blank">📅 12:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81348">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nHWQvwY_xi5SwpiHEs9a7-kYdLt38lvHLyOQUbXtsqtbtXEUYRPikpVie4ZHkeoqXsYpFo-29-8c5P-Fil0GrCxl8zi_un5rHDotJsdu99yr4VDLh6ITDMdaaA1NCBcikR-QGpK3L5cwJ-4p4mFwqJtTIRy8F9LKfEXu-NOpU6GYkMxjKfbKSHUlbZNu18FgdKIJn4LyG21E6Eh_B6jfEszhpQ5enLyLUXOQqL0F3FJQ30NuxTGObcaYVFohNbLh97G8Jw0Yu8GanCZoBZCQMG8Mv-JICCIJLbMwpXC7n120eHTHwESB12P08R7m_fj38agqbimQY-HGXyKQbJrLTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این میمون چرا این شکلی شده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/81348" target="_blank">📅 12:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81347">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">هیچی دیگه، ملت اختیار لباس پوشیدن خودشونم ندارن.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/81347" target="_blank">📅 12:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81346">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UN52UZYGdAmeqS-QS2TbplMLFksdzez43JK_6fN_QyvhCP_m8iVFByFYzCnBaDRIV18alAoqYJoI7g8aI6wlR1jp0F11oYLWogiCUiJNQhpJ3RUZGFtk1ne7gKOFowMhc0mZnVY55FG26XksCYgzXKgO_8B98XhtstM5Zsg27vDty_N9LjoQ13y26c2BV2hyfPInAF6i3qn_K2NW8IV1Hz2kYwVid_Uue2zfuZTrUiJh0YpB5EOPv0oskVl-gl-HDfzoHRBmq0WRcmTlDhc5jAR6ja-Betiw4OPxJgSZkf8b_HmCTuTN_GUBQXRvS2SkUKin4OufD4t85Oo_6f761Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچی دیگه، ملت اختیار لباس پوشیدن خودشونم ندارن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/81346" target="_blank">📅 12:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81345">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
نمایندگان مجلس جمهوری اسلامی طرحی را تصویب کرده‌اند که طبق آن، تمامی نیروهای سنتکام و حتی تمام شهروندان ساکن اسرائیل، چه مسلح باشند و چه غیرمسلح، «نظامی» محسوب می‌شوند.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/81345" target="_blank">📅 11:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81344">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">سجاد شاهی پول ویناک چیشد</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/81344" target="_blank">📅 11:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81342">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QGIGiRVq2WGXk4lAqIXcDBQp7s0rQt0uzOFTr7i0AbjwtAYuNUXRWIWZuRFHVgJXYme8K_ujdf1kUHokCsUHHeWXq3X_qMMddemo_bPCM-PzNGda4JZODWj1kGSbMIFVRPB37lrNgZ5M46CEctR6tcIM9VweHb-6IkmVfvaBFzmb4Tlqxl6asqvv8SYWK7UYzkWg6R4TS0l1U-ubxkpyADddwdJoFJidyyoYL0LLnn6Xt5fwj1P_x28YhsR_visUQXnxDrX0cqqHfwMWuLQ3lFLwH_EK2KHOFTNTb-SuYK3ps-xBawWzuN3L3KuYLUvcqyTF0v3azZOawVe9eDVqfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L8uGT4pU32230JLYMxAR5KOmrBCcNedum1jRtZkEImP9KolnmNleX3aWNxBfhmqKwoK-b83N_10DwI65rlZaZ0NK_1qrFsLEQkKbegJEHge_3Xo34ZyV6i2zF9LQPUPJHkSLAXQPWIxotCnS5dnDS49jqAAEp1O60GsWBFBPB_zMZ6fBdysOmssQIaVmfcWEBZoUrj3BKJ4ucp8jZFqpw1W4dtdEv-yCIOpMnENBjquI6naZZQ9m8XlU7CqgmOIlBB5m0h5Z65ydPDJlZTKuk5Lx79rCKKN5ozS85IxCsrCUVeRoJ_tukBkoqaw1XJKDgUuKP85k27Pzoa2sR4qtdA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رونالدو در کنار چهارتا کاپ جام جهانیش.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/81342" target="_blank">📅 11:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81341">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e5hRgLJcYUioD6gRGOWlPlHTspplVS1wNKOOFk4zC4J30l2YVSgFeTuLKUamXUPKXjoy5vld54cjTuX9OO3V7HxHUjpHS7QCan-aOwpfnbXVeYUg2Fo8QdHgBPz0oZV7zhxFs96UA4h-6gfD_g6CxwHZ5WvVpDR-twBsYyZsVRHDn_3UE2E2Y0rzr7DrvQwO_VnUzxCQWRR6Z2xgErfbvCwtpTFVZYMiMKsMGtjWLqI_kGRwgLcw8vd-HGrGGQB9BfDdb8SpibDXbLlUtwwDPtBFfQA78RAGLJ5GGQoC9f-FDPwp5VipSZ3SXdDaGkV9SJcrh1CXtKvDve1qx2b4IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
گالاتاسرای
🇹🇷
-
🇮🇹
ونتزیا
🏆
رقابت‌های دوستانه باشگاهی‌
🌍
🕔
دوشنبه ساعت ۲۱:۳۰
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
گالاتاسرای در ۸ بازی اخیر خود مساوی نکرده است.
✅
ونتزیا در ۱۶ بازی اخیر خود شکست نخورده است.
📈
میانگین گل در ۱۰ دیدار اخیر گالاتاسرای ۳.۴ گل در هر بازی بوده است.
🧠
به ساعت احترام بگذارید، زمان هم بودجه شماست.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r5
💻
@BetForward</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/81341" target="_blank">📅 11:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81340">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ucuNzwM0zlYnL9ZTmFMqh35BZJ5PJIFmz-QOi-938sY2LaUtW_hOw60oPtRC0nonuKinyqdrESlkUMKlu1Dy9ivWoiHxWegQLL9ERITcPtIFkC2PneC_ySb2rC015Jd23YZachb8W-DiDG24B-DPSsH-UNVgnoeKz-e8nlgxEL5BeL1MuD9dXiC2mxJn7SueVVuW9sVUeTGLliGT74tPDy5su1VhmsRrRSbRITHppGtzjjiuZgROSc8Ggqqy0cWCFreHqYiC5ySpMEhjRLqsoixZFKkS5ojqeohrpe3iA4uxSkBxgxXlGwfhfP1yXHvsSrSU67-3PGeyw_-CnylSJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز، چهل‌وششمین سالروز درگذشت محمدرضا شاه پهلوی، شاه فقید ایران، است.
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/81340" target="_blank">📅 11:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81339">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ناموسا دیگه کلماتی مثل "آمریکا،ترامپ،ایران،جنوب،تنگه،پسر عموی مهدی،دیپلمات،میانجی،جنگ،پهپاد،جنگنده،زیرساخت،نماینده،مجلس،اسرائیل،وزیرجنگ" میبینم کهیر میزنم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/81339" target="_blank">📅 10:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81338">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XJ82jKCOJxyPvOVFdAa4l8Bop80ET4yBL2l2kkFrJ4QG-rn4LeMcjc8-Z_JJ0iGRaLQ8o-eQPzdKODgfhcZ3n-N4WhEyl1MGLF-PJQM12VHoYMGpaTnLJmBAuli4HFRiUh5mczvubsCobVrcrUjwpLXRMZhcg3kPbp0nbiT1AJviFQP31D6v-kGSxLbSLHO6wWExtyPs5aEiuTG1OaqJ420ZOWIyGBo4IOqCIuXoyZNwaN3VT8x8YmyEWWRPdfhRS_53zxMor8LhRrtANNFliVStgzq-bCsLyHpHnbRtQ93ldY-BIc7guCFPwn5lEpR99e4CMXHK-69NHZvJ99eVWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به به مگاهیتِ تیک تاکی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/81338" target="_blank">📅 09:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81337">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bd0a311a6.mp4?token=Nfd6HbrjkdVSzgNsn2LfhZ6ImDhFiUx_bEQwJY85K5jtju4pr6SP8ujuSj1jn6BHj6_nQkqN1mCulV0E7YxylArkjIFzrkni4BvPPL0kaPyp6eHIK9U6wVhYqpEQ4G_bHURjYnf9XxeDI1PJbXv-g4qSo7reoM2SGJYbcHIa4wfov43onxZLGZW8105RxSMIgYjVzbrLYEO-gww739pNJlz3Z3luN49axRf7gRFyCBi_8Efu0u6GaUZ6bsh09WLUHbRVakVokf1m83nQtgPjSUM4-em80GCwI9rgXoc7xVhu-sVJGo24Gf6VbugQLxwNBPZgOYi6eDmizAs-KcuPtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bd0a311a6.mp4?token=Nfd6HbrjkdVSzgNsn2LfhZ6ImDhFiUx_bEQwJY85K5jtju4pr6SP8ujuSj1jn6BHj6_nQkqN1mCulV0E7YxylArkjIFzrkni4BvPPL0kaPyp6eHIK9U6wVhYqpEQ4G_bHURjYnf9XxeDI1PJbXv-g4qSo7reoM2SGJYbcHIa4wfov43onxZLGZW8105RxSMIgYjVzbrLYEO-gww739pNJlz3Z3luN49axRf7gRFyCBi_8Efu0u6GaUZ6bsh09WLUHbRVakVokf1m83nQtgPjSUM4-em80GCwI9rgXoc7xVhu-sVJGo24Gf6VbugQLxwNBPZgOYi6eDmizAs-KcuPtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/81337" target="_blank">📅 09:41 · 05 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
