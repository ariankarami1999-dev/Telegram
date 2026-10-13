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
<img src="https://cdn4.telesco.pe/file/symKfrijcFxG8zN2dWOabAN-U7IFwZ-4dEsPi2Dr3P3ujuMrLTILq7Ol3Tf1TnGCOfs1izT-iU258h9vkp_UWGWbDiZCsuWHoeo2FlmaYRy5Y5toL8V-68tFLKLrblbrqqfy6wghxAMcs1UcFWGdIOVI1IscUBMtg1vv4S9iTwzKcRUONiLYIOhKlOqz07kNSJd9SPBWhjSib7Ipuxa1AuzD9FZIRhij_ccUwkuow2h-jSU8YVFsudC38guFkyd0ASE2suunN8oKoDQaQRl6YmLHsFc6BrePwhfwvaplZHNAVxcKIJxkNiwOMjwTPD54kmdDym-CKCl8WU43pfZ6Jg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.46M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-21 22:53:43</div>
<hr>

<div class="tg-post" id="msg-698215">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HvHTVc6aeKqljK6Gn6NfsR8kugJXsW6mKoewqn7Q-19YlN622ZqFJFaV9QNnqeltipup5DmsKDy8Z_KB75abmv6v2S1vqGYLfLUxJmlq5a6sqVQUBt8XGZrnpyafj-UN-J8RFW3Oz95cRf8ZA6Quhqy9feEJKTQOcce7GAv0bEBwG7gJTFHMc5Q8Ol6p-krYyiDHMTmowCQmCcXBYzYR68efBDtrdGsdKvKq23da9IJXEJAI5gFP7vksocqAu31Rpy5cW49CIHRu6u1J7TpMYCWvuNA17VRPhvru8iQHdyCMIW7Sj8ptQOmtnWvat140FDBa3a2JNQzss2Urgz3fFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بنادر راهبردی اسرائیل و ۵ کشور منطقه در بانک اهداف احتمالی ایران  رسانه جریان به نقل از منابع آگاه:
🔹
بر اساس اسناد و نقشه‌های منتشرشده از سناریوی پاسخ متقابل که توسط رسانه امنیتی جریان منتشر شده، فهرستی از مهم‌ترین بنادر راهبردی منطقه به‌عنوان اهداف احتمالی…</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/akhbarefori/698215" target="_blank">📅 22:50 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698214">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
ادعای رسانه عبری: نتانیاهو از ترامپ خواسته است علیه ایران اقدام کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/akhbarefori/698214" target="_blank">📅 22:46 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698213">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LpZSQgb39kWFR74DqoPPPNp4WX88o4uqTmQGvslnxdHGAitUr8HafPGM-UD889az9wBtUJeUzIWa60ac7JkxSD-TNDcIPWLWr32kmIPeJfc4qEOPEWVaNm8_1SpsE8pHxJkcZ5myarxddE1OBiX22wGgrTQh8VyNU9cz4eEdtSkb2toOCcKqUVz3k862GUSOvJu8rZDkcV8Y5ECeRhmjkPVVyneQvyH-UN_hFEYtabmuJ44D5os1XvewAFyofeGDthWzNe8b_P23ml4gWUvopskIyFIR6m9JeDKfOvy1aeiAqouTQcQkotq4zBYMPJKqQpMcY8dxh3ZlXQ4wtPMjBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هفت خان کالابرگ
🔹
۹ ماه پس از اجرای طرح کالابرگ و جنگ و جدل‌ها برای افزایش اعتبار این طرح، سخنگوی دولت اعلام  کرد که در مرحله نخست تنها برای سه گروه از افراد کمیته امداد، بهزیستی و خانوارهای سه‌نفره فاقد خودرو و مسکن با درآمد کمتر از ۲۰ میلیون تومان اعمال شده است. این افزایش در حالی اعمال می‌شود که رشد قیمت کالاهای اساسی، اثرگذاری اعتبار اضافه‌شده را با ابهام مواجه کرده و شروط تعیین‌شده نیز دامنه مشمولان را محدود کرده است. همچنین سازمان برنامه و بودجه با تصمیم دولت، متولی اصلی طرح کالابرگ الکترونیک شد.
🔹
هشتصدوهشتادوپنجمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/akhbarefori/698213" target="_blank">📅 22:41 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698212">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gm3lZQ5H7c-p77xYRCBtLbqlCtVXPLDEPvx9UIkvg2R91ulvdXLbFs3GmTCQrC6rIiytslR9XJEHDuxqUt83EMShCqENGU9SkezqoMP7qhdWf3SzArffbsIOFCZQ1wmFQGtL_uPMgmtM3QDT6QtKqY-vYjrPwWUdAL7WIY0NUu-Prtn5Bm5eEnnpviqsN8UAWTAutNul1ap70KWV1EaW5OUPhP5uPY5WL2cJzBG6pwfcBc0jfbS0Eakp6WzdKnVYEAfvv43EtL7xEQLQ7FoPjU8phacsTS3jaRfreYitUHeS8mZCnwihJHibDQsGZ3pNAKZIODKpC9hLvvsIjAKwbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سازمان عملیات تجارت دریایی انگلیس: یک نفتکش و یک کشتی کانتینری در تنگۀ هرمز هدف اصابت پرتابه‌ای ناشناس قرار گرفته است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/akhbarefori/698212" target="_blank">📅 22:40 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698211">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
وزارت راه و شهرسازی در موضوع الحاق زمین به شهرها، ترک فعل کرده است
پژمانفر، رئیس کمیسیون اصل نود مجلس:
🔹
امروز وزارت راه و شهرسازی در ارتباط با کاهش هزینه مسکن مردم کوتاهی می‌کند و این موضوعی است که قابل دفاع نیست و ظلم به مردم است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/akhbarefori/698211" target="_blank">📅 22:40 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698210">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59a2aff38f.mp4?token=gfvmaRD36EdBSezyYo4DdXkkwj2T-RrWbWTk_TbHubU9gOhAlQYscnPitSLGimiafnrKlKeNtYf-PEUnUt-8q_WllcPiWz3vuCRH9xKSPFV0dL2QJ9dhumwjI2Q8sJvORE4WKZibWD6IOcUB8hvnk3gnLxBnLGdSPh10UspxlbCByaAO7Ypw4a_I_IO1r7EmER6OXMrdf77aukX0zFbe9gSCqNLG5e3Z0SFOrAoHxnCqYZ6DYWDtvxXxLNkzITspE6DRGY2rtlhfsblu8lX0VTAT-vp9l30BIq3lVyuOmmH5-Cvrd1BR67O_QYxzvCECbiXJjnn8ve3-HjaaQp-9hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59a2aff38f.mp4?token=gfvmaRD36EdBSezyYo4DdXkkwj2T-RrWbWTk_TbHubU9gOhAlQYscnPitSLGimiafnrKlKeNtYf-PEUnUt-8q_WllcPiWz3vuCRH9xKSPFV0dL2QJ9dhumwjI2Q8sJvORE4WKZibWD6IOcUB8hvnk3gnLxBnLGdSPh10UspxlbCByaAO7Ypw4a_I_IO1r7EmER6OXMrdf77aukX0zFbe9gSCqNLG5e3Z0SFOrAoHxnCqYZ6DYWDtvxXxLNkzITspE6DRGY2rtlhfsblu8lX0VTAT-vp9l30BIq3lVyuOmmH5-Cvrd1BR67O_QYxzvCECbiXJjnn8ve3-HjaaQp-9hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پژمانفر؛ رئیس کمیسیون اصل نود مجلس: خانه‌دار شدن دهک یک تا ۳، ۷۰ سال طول می‌‌کشد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/akhbarefori/698210" target="_blank">📅 22:39 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698209">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd70803b81.mp4?token=nQa7yMWpo9I19qiGkxGXii81GYHkGg2pNitopp6DscLrfv8fL5J_5GBMIE0ppy6QRwTJP2_LyZ1u2mUYLTPKFQBfaTmmXWM3Gla8RdTSOmxLjwDeJyiO4sVYyt6oeBQZU1udLcDIPQCVlWmVEBmECLDkGbzIf-hUgX0e2TthIef0RQckL8XUFIIIDKTzVW1O-x1pP2-U50o0B7YqheP3VpVJTbliuKfyeiYTjxKX-FQq4qcyhgm8SrV_03H_es4ueuMkQ0-vsbuADd34IUL_vO57YyYZURffC2BoHWqnnvxBbpdqh-SrwgQqtwyl5OEkhnC1IrMGDBkYeJhDq-PvHCcs7536_7jq5Ur2OZ_UyeiKTHLg3JNp8WpLutyE3_bL5LuKO3lt7SrBiEvBM2RmLsCEQwDB9zhGhhJrZSOcCYLQVJG5izikwB_bhEDs6nkUyG08BDK2ovC6zWkl4ED6hDkDVOroInO5DlMgXip5HaP9qvrCS204crqbB1NF6gbGX6G5PSBwn5VBFJSX7Kco0Qw2-exzAQyCz6M9WjxWG8Bekcg9RztRGy6somqOy73ECGj5VUZ7IXO8lVYotsJmZzdgIb_kc1jKN61-VSrmxoh4Xdb5z3O3mkca67KoQo9e6VkHw4gkYxsCxCKhMEJ0N-ruxomPwOF7yG0mtVOQRqU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd70803b81.mp4?token=nQa7yMWpo9I19qiGkxGXii81GYHkGg2pNitopp6DscLrfv8fL5J_5GBMIE0ppy6QRwTJP2_LyZ1u2mUYLTPKFQBfaTmmXWM3Gla8RdTSOmxLjwDeJyiO4sVYyt6oeBQZU1udLcDIPQCVlWmVEBmECLDkGbzIf-hUgX0e2TthIef0RQckL8XUFIIIDKTzVW1O-x1pP2-U50o0B7YqheP3VpVJTbliuKfyeiYTjxKX-FQq4qcyhgm8SrV_03H_es4ueuMkQ0-vsbuADd34IUL_vO57YyYZURffC2BoHWqnnvxBbpdqh-SrwgQqtwyl5OEkhnC1IrMGDBkYeJhDq-PvHCcs7536_7jq5Ur2OZ_UyeiKTHLg3JNp8WpLutyE3_bL5LuKO3lt7SrBiEvBM2RmLsCEQwDB9zhGhhJrZSOcCYLQVJG5izikwB_bhEDs6nkUyG08BDK2ovC6zWkl4ED6hDkDVOroInO5DlMgXip5HaP9qvrCS204crqbB1NF6gbGX6G5PSBwn5VBFJSX7Kco0Qw2-exzAQyCz6M9WjxWG8Bekcg9RztRGy6somqOy73ECGj5VUZ7IXO8lVYotsJmZzdgIb_kc1jKN61-VSrmxoh4Xdb5z3O3mkca67KoQo9e6VkHw4gkYxsCxCKhMEJ0N-ruxomPwOF7yG0mtVOQRqU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کوچک‌ترین استخوان بدن انسان با گذشته‌ای شگفت‌انگیز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/akhbarefori/698209" target="_blank">📅 22:36 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698208">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
منابع خبری از حمله موشکی نیروهای مسلح یمن به ریاض گزارش می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/akhbarefori/698208" target="_blank">📅 22:31 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698207">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G5xOyW4Z6nLHBpcvgsQBX04xjiYEhp6VjB39pghPTOVcExmalW0osFMKMpemgJeS10KZSTbsnRGvG_CRPMQz3P4-VEuB6m2Ns5upeHtFlYJMbDcyeJFUfpjod5U6biYfbeNHkW0aYs08pC7wPHkPdp7aOSwdaKTJe8u4ptjwUWsNVVAh5MOkhbKp-CW6OG90X8Tob-cWGp9ppm1oWYzoevkP9yj1B5z3I2g1YYJTVW4HKgtkYS-zMctA4WGKvByVsP9A_e8hf2z2X6_QMhNzllfAh68yeQy5Xym4Qe_SAs2Dmk1oIN7POFSvon_vf2QVpJqZhwWpU7ANoSUIkJhIqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حسینیون آذربایجان: الهام علیف دیکتاتور و سگ صهیونیسم است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/698207" target="_blank">📅 22:27 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698205">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6377634077.mp4?token=deuWWOVeSKFzqcArVd9FjG2XxT5qv9X_NvABe66_YtLV9Z6yIG_HMhbI1ihy3wmcy8q8CN2bxiSA0VNcuv8_ucof6MQ7CL2k68lRcfJTx6ATi30eUFJdubwayX2ma0nHXXD6hiargqElp_Na9jKB6_pIZsPEIagYAhnpTvNnq9F5kFMvXgFX4_tvsXkpUhHRALZ0RVl9CQMPvF6jWGsYpUDj2leFe19e2Z0Mj1RENpCcsCV71f6A5XUYRe79snE26GDPzSgkYtvceczMOzYFHR7wTzrO-6HA_-OpKqdmrF3ehKC5hK_uDTmh1zfmWLCXldRNHNJWMqEiv6hQ-IHhZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6377634077.mp4?token=deuWWOVeSKFzqcArVd9FjG2XxT5qv9X_NvABe66_YtLV9Z6yIG_HMhbI1ihy3wmcy8q8CN2bxiSA0VNcuv8_ucof6MQ7CL2k68lRcfJTx6ATi30eUFJdubwayX2ma0nHXXD6hiargqElp_Na9jKB6_pIZsPEIagYAhnpTvNnq9F5kFMvXgFX4_tvsXkpUhHRALZ0RVl9CQMPvF6jWGsYpUDj2leFe19e2Z0Mj1RENpCcsCV71f6A5XUYRe79snE26GDPzSgkYtvceczMOzYFHR7wTzrO-6HA_-OpKqdmrF3ehKC5hK_uDTmh1zfmWLCXldRNHNJWMqEiv6hQ-IHhZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی ترامپ و پوتین برای زلنسکی تصمیم می‌گیرند!
🔹
ویدیوهای کنایه‌آمیز هوش مصنوعی از بازی قدرت‌ها با سرنوشت اوکراین در فضای مجازی وایرال شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/akhbarefori/698205" target="_blank">📅 22:22 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698204">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">‼️
حملات موشکی انصارالله یمن به تأسیسات آرامکو در منطقه شرقی عربستان
🔹
سازمان دفاع مدنی عربستان با تأیید ضمنی حملات یمن، از فعال شدن آژیرهای خطر در شرق این کشور خبر داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/akhbarefori/698204" target="_blank">📅 22:17 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698203">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">‼️
حملات موشکی انصارالله یمن به تأسیسات آرامکو در منطقه شرقی عربستان
🔹
سازمان دفاع مدنی عربستان با تأیید ضمنی حملات یمن، از فعال شدن آژیرهای خطر در شرق این کشور خبر داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/698203" target="_blank">📅 22:16 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698201">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/alF__fHk_l_edajdosFKim3GhFBW2TphjQmSi9pAe_J6cHhYdzUUkVTvasyzNCq-H3ZGCuyMcdaKOFHD-RJBMYIpdRiP9pmNqsRQL_MigYorNOYbJMifsoAlEzxcKxsimfaj9Ub7RNYPAJTfIcJts0sew5DbaSGbh6MGb5hoBMtnC21EJQTOu-sFEZwB55z-d6C7HcqrAj-cW0QGx9aNxepIYzNUaTHmbgCcvFF_nVxqgTCzCn233gvqJiJnPMODNFFPRdcJ8G4nwmsUyBH8znGXd4ABMtF7nkgWUK3JLxBV6E1MCyTLIfQdAe0WHbpS_ZKogdEXLnD5s4Uqz5TsLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای ترامپ: حوثی‌ها به درخواست ایران به عربستان حمله کردند
رئیس‌جمهور آمریکا:
🔹
حوثی‌ها رفتار بسیار بدی دارند. فکر می‌کردم یک سال پیش، وقتی آن‌ها را به‌شدت بمباران کردیم و به درخواست خودشان حملات را متوقف کردیم، درسشان را گرفته‌اند.
🔹
آنها مدت طولانی سکوت کرده بودند، اما حالا دوباره ظاهر شده‌اند؛ احتمالا به دستور ایران. آنها به‌شکلی بسیار شرورانه به عربستان سعودی حمله می‌کنند و عمداً تلاش دارند قیمت نفت را بالا ببرند؛ احتمالا پیش از انتخابات آمریکا. این رفتار خوبی نیست.
🔹
باید کسی برای آن‌ها توضیح دهد که من در انتخابات شرکت نمی‌کنم؛ چون پیش‌تر با اختلافی بسیار زیاد پیروز شده‌ام. اما پس از انتخابات به سراغشان خواهم آمد و هرگز فراموش نخواهم کرد!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/698201" target="_blank">📅 22:10 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698200">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GfzVzEFuZOKoL3psnNbkdB04pdl7gfj72Qu71JopIx9fHwOjRhKLcIj1Xxmy-Kj2bSbGxdqoXV07G6-ukmCoIZBdCuNcjZL3GbX3GBxvsHepYzV5_tms_ZjOAzAHbphZDKVKGfVMDpMngxLGErSEZni8xgto1xTAe-dNGeiEwYG8_qld7S8pqSwK7hSrSfpoAs9pHbu3r6MDXQ82boPjmQT2tBYmIoZ9Gyc88izJraTN7AjkxFi09awkVLrwDkwSaH1lS1sKE2BGzU0-J1acHZ8DHKeX50x1REC1DDzZBzbZz3SHCfUCMB4x6VgMTijH4RzePJCyKUYzIzVU1McDDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گزارش مقاومت عراق از پرواز هواگردهای ناشناس در حریم هوایی این کشور
🔹
رسانه جنگی مقاومت عراق در گزارش روزانه خود از تداوم تجاوزات و نقض آشکار حریم هوایی این کشور توسط پرنده‌های نظامی متخاصم خبر داد.
🔹
هواگردهای دشمن با استفاده از پایگاه‌های نظامی خود در اردن و اراضی اشغالی، حریم هوایی عراق را نقض کرده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/698200" target="_blank">📅 22:04 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698199">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff51b864e1.mp4?token=bk0n7KGfsrMHK2zU76lSs00FeU1YBT1mODR2jzAzxKO-A7Ojdxcth7oJHC5E8OTKHU3rHupVIR5jKlUSVCzqD0OeavVo4l6f-fK2e0cdVNvtMe_tHRmZ7QXDmhs-fGPgxgnGLjdrf3fp4GhbmOTYXQ7h2_b79_LIT2dc8Z4172JR6y_sG7ye1XPFnRnE7S1vNsD2FeeVNhg9NEa4Rc7u8oRvDZGUIm1zwwMA-eJxivzd0aTLIauIVztq0AnmEkwftEjg16RNBwg13fFisLDeRZitqn9MWKEndo9oAveLFdzM0ZLextWkgow0gK5tNHNECKfkMdIbRoaS-pJmnav8TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff51b864e1.mp4?token=bk0n7KGfsrMHK2zU76lSs00FeU1YBT1mODR2jzAzxKO-A7Ojdxcth7oJHC5E8OTKHU3rHupVIR5jKlUSVCzqD0OeavVo4l6f-fK2e0cdVNvtMe_tHRmZ7QXDmhs-fGPgxgnGLjdrf3fp4GhbmOTYXQ7h2_b79_LIT2dc8Z4172JR6y_sG7ye1XPFnRnE7S1vNsD2FeeVNhg9NEa4Rc7u8oRvDZGUIm1zwwMA-eJxivzd0aTLIauIVztq0AnmEkwftEjg16RNBwg13fFisLDeRZitqn9MWKEndo9oAveLFdzM0ZLextWkgow0gK5tNHNECKfkMdIbRoaS-pJmnav8TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حملات موشکی انصارالله یمن به تأسیسات آرامکو در منطقه شرقی عربستان
🔹
سازمان دفاع مدنی عربستان با تأیید ضمنی حملات یمن، از فعال شدن آژیرهای خطر در شرق این کشور خبر داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/698199" target="_blank">📅 21:56 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698198">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee41d205c6.mp4?token=HuTtOyBQsoSxijwn7ugbsJhv3JAIRRsavXs-Fs2ESJG_JLn-8-8zI8MCdvaqt5Fdv8-3WQWqBtF3pcxMCDzAIjbw6xAfq1vLi8ib8rRdZsYgsozDHNWlKwWCOcDc1FzlnMB6-RqWF-6FM9320e2v2bncc43ozkEADNMlkg1GVQGRfxqK0jvoTjX8qQfzFt3uFWGSEbKx-afo64UHYgTNcTEjBiNo41MADl4UrwtS9bDBgRUn0phxqqspzPfoHU90k2dNieVrdEZVokO-aS9iaBWuLNEHxKynxvOoGg2ZfDcd1h5Hy8QhucYvZbFuKp-ujIQwBti7ZBJQ_KRl9Ou-Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee41d205c6.mp4?token=HuTtOyBQsoSxijwn7ugbsJhv3JAIRRsavXs-Fs2ESJG_JLn-8-8zI8MCdvaqt5Fdv8-3WQWqBtF3pcxMCDzAIjbw6xAfq1vLi8ib8rRdZsYgsozDHNWlKwWCOcDc1FzlnMB6-RqWF-6FM9320e2v2bncc43ozkEADNMlkg1GVQGRfxqK0jvoTjX8qQfzFt3uFWGSEbKx-afo64UHYgTNcTEjBiNo41MADl4UrwtS9bDBgRUn0phxqqspzPfoHU90k2dNieVrdEZVokO-aS9iaBWuLNEHxKynxvOoGg2ZfDcd1h5Hy8QhucYvZbFuKp-ujIQwBti7ZBJQ_KRl9Ou-Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بهترین روش برای جلوگیری از حشره گذاشتن برنج
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/698198" target="_blank">📅 21:53 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698197">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
چرا سازمان هواپیمایی کشوری مسئولیت زمینگیر شدن هواپیماها را نمی‌پذیرد؟
دکتر کامبیز بابایی، مدیرعامل پیشین هواپیمایی آسمان:
🔹
درحالی که متولی صلاحیت و ایمنی پروازها، دفتر صلاحیت پرواز است و مدیرکل آن بر ایمن‌بودن هواپیماهای MD تاکید داشته است، چرا نظر سازمان هواپیمایی کشوری با آن مرجع مغایر است؟
🔹
چرا همزمان با اعلام اینکه برای پرواز MDها منتظر نظر شورای‌عالی امنیت ملی هستید، به نهادهای بالادستی نامه زده‌اید که مسئولیت این تصمیم را نمی‌پذیرید؟!
🔹
چرا ایرلاین‌ها را مجبور به خرید قطعات آمریکایی کردید، نه محصول ایمن داخلی؟
🔹
چه دست‌هایی پشت پرده زمینگیر شدن ناوگان عملیاتی پرواز کشور همزمان با تحریم‌های آمریکا است؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/698197" target="_blank">📅 21:50 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698196">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d92c7c633a.mp4?token=NjeAukmj0k-BpfvF4oRAMHdjIJPPMFe6_SsJXHjjmGc7qUgbV12gyo0uBAkeaRiwSCzmYv0j7MLHCc0OjBHH8B07YQVeHFqxr9jvnB6Cb6fFOpF_4TCulYQEE2HSG7uJn0WCXdvE6BcZSqFOj0avDKKgoZ8bZnTa_a-mDsDcjDpxJcigAZIhp8aG5uXHLZmrUWfhJUSsgbMXI1t6_lFwbXmUCj_8Lncmbk7sf8NNpAY2uMUCFxVFxFDl_78tFW2DXAzfHvvxI__pIfqextAwYxa-QrreyQ-vxz6m80LBW4tic0ios26tBgtPiAtUSmgljZTDnILN8SE5TXeAdJvzOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d92c7c633a.mp4?token=NjeAukmj0k-BpfvF4oRAMHdjIJPPMFe6_SsJXHjjmGc7qUgbV12gyo0uBAkeaRiwSCzmYv0j7MLHCc0OjBHH8B07YQVeHFqxr9jvnB6Cb6fFOpF_4TCulYQEE2HSG7uJn0WCXdvE6BcZSqFOj0avDKKgoZ8bZnTa_a-mDsDcjDpxJcigAZIhp8aG5uXHLZmrUWfhJUSsgbMXI1t6_lFwbXmUCj_8Lncmbk7sf8NNpAY2uMUCFxVFxFDl_78tFW2DXAzfHvvxI__pIfqextAwYxa-QrreyQ-vxz6m80LBW4tic0ios26tBgtPiAtUSmgljZTDnILN8SE5TXeAdJvzOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آیت‌الله مروی: دو بار با رهبر انقلاب دیدار کردیم/ حالشان بسیار خوب بود
تولیت آستان قدس رضوی:
🔹
هم پیش از تدفین و هم پس از دفن رهبر شهید، رهبر انقلاب در مشهد حضور داشتند. دو بار توفیق دیدار با ایشان و اقامه نماز با ایشان را داشتیم. الحمدالله حال ایشان بسیار خوب بود و هیچ جای نگرانی وجود ندارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/698196" target="_blank">📅 21:40 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698195">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VuAzSj-jji6QDE-3iwKTz1kp78am-Uuxdn3ob_68aw-4ey2eY6c-xsdYxbXq8r21QFd1lOa_l3IYW1Y26KQhO3LPbtBHFJTu5TPCXN3Xlh1u7-r0HAAhbYDXh0e5bRo1lYoBB8GzCkNnRK_A_gzexCGwLdQ6kWu0jpE--R3bzuaFlEjodRJYfPrlD1nPy55WhLubBo4IzBeOeBF70BflVAcWt1HhTRM_A6OJoEzb0VeH7JhD85MOdcOolaoyv_gLfQp8jj6htD_WkfyJ_TtI8mysYg-d1uKVUec0oUBXEIGmFfFqtMfP7iNArAhkdPGLDL5azIhze0xt5sIsxnI9zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
احتمال حمله آمریکا به مراکز هسته‌ای ایران در جنگ جدید / پاسخ ایران به حمله آمریکا به کوه کلنگ چه خواهد بود؟
🔹
اکسیوس در گزارشی به نقل از مقامات آمریکایی اعلام کرد که پنتاگون به فرماندهی مرکزی ایالات متحده دستور داده مقدمات ازسرگیری عملیات جنگی در ایران را به پایان برساند. بر اساس این گزارش، اگر عملیات‌های رزمی عمده از سر گرفته شوند، انتظار می‌رود شامل حملات به اهداف انرژی، زیرساخت‌ها یا سایت‌های هسته‌ای ایران باشند.
گزارش تحلیلی خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3252213</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/698195" target="_blank">📅 21:40 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698194">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در عربستان سعودی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/698194" target="_blank">📅 21:37 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698193">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nl7j05Srh9nmj3eQXJJWKCkIWvFpF14huvY6MBs1COBPVeCb4uOVv86u4z7VgZOX9b6WE83NYkX6_E3GjQ2-YPPFWSE37sZ8IGWgKnq6R6kx4u5ghBVrW3XLwFPRJEIGQGXWPFc8JsAULAevtg87c1z8XkHZv9Lv6H8ANU54gJhEwvnOtaDd0ge-iC6xETO3prpY8c6pU9a6HyvRg8o8hl4nkXkFs0pTIoADE1nsUIBu5CfaqhWAhIM2-v3UVNfTAjFI6jq6OoxhWjs2h2D0OAVLrMuN9yBlOJ8enRt6CNsQSAvi0GUcNAZkS0YO4mE9jPpwKBoYjWw510jxcyq8kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در عربستان سعودی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/698193" target="_blank">📅 21:35 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698192">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I6KdBG1SSMDtqZjPCxngG2cSxxQ_k7M6-OWzgiVIbolxCpHhkf8VFqLMFla8lku9-pB3L2yZoMO1XXYJf4TqzdfHEUvVd8QscU3MzjvZS1T8dmeVr4UHuGOWJX5cCaX_xPwAYYa0nxoxtEmFqMluAnobe7kuux-sGRTzXDD0jHv5J3Xfn4KQdnYFZ2stV-RyqTULnHdvAwuR3iUZR88MbZEIlrWg6hChZ6QqTq4l1wsJKzTiznG0zZfUhJ63Qi-JfphG4HN_GdVKCnPgDvBfvVfNqHJYYVZ5rDedAxfDH7krtHalTr-cG7rNu0-Ii_rcyvp1hdKFkFSPJUpBRa2jkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۱۱ خوراکی مفید برای سلامت میکروبی روده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/698192" target="_blank">📅 21:32 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698191">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک اقتصادنوین</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jO5PQZkOy2WJVP-Yd17vpM-i8UgF4nHNyqUbW4cz8Dgycurp1LYaqTqJEdRWPqhwnOF3b3vWsDUmCmtz9554UnHnStO8PpT-3rcRtxyRXkdvDJQKii904b4TxXp7aa1huB0QCeVb4-n07v0o4PxXvLTAMy70djXVUuZ6Xg9KJguyZDAcBhHjyRRkIlccPElAhNTD3vUxQP05Bkge3ISS4vmXAkOkx-Jvo6LhzJOXQ_cVlAADE3PJr0IFs8Z4nLhcEBgwxwe4D8lJY-IZYXN-liIdkPsjpezRAKFzbxPRse90b9PClV3MBpb3S9j42wioH3MOsgFtW55YVhoRvnRi9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
افتخارآفرینی‌های پیاپی «ونوین» در بازار سهام
🔹
بانک اقتصادنوین در بازار سرمایه دستاوردهای چشمگیری را طی نیمه نخست امسال از آن خود کرده است.
🔻
اطلاعات بیشتر:
🔗
https://enbank.ir/s/mfabbXL
☎️
02162740
🌐
www.enbank.ir</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/698191" target="_blank">📅 21:30 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698190">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fe6fa0a8a.mp4?token=M2yEstqu84CQLWX-C2dxZ4kMs0MTN6UVgJl8xGXdvcscu5QTvrb-ujdrLYBOwQF_xgHMxjRKLzIx2kEja41IWm7zFDb-zVKmN0IQk5ppZ6ft7mI4b4-T1-reCIW5FIQuopDH7us42epi89RsWT-AGDKxsFNIpAnNpdGR7BeQg0f08C1oeEcK85_pSuMqbmSvWCsfeHoqosD3rVrUdPUaysYArYkweOCwdP1AixfHWKoUHrosALj_9xvlQEUmoz3CliulyNzJxJpsbYavY01f0KX56XgSuj4eW1rBQ6jm2CcBNSXktjHR1BaA_7FROOsOE127oYbQ6nO-TMWlRqgyRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fe6fa0a8a.mp4?token=M2yEstqu84CQLWX-C2dxZ4kMs0MTN6UVgJl8xGXdvcscu5QTvrb-ujdrLYBOwQF_xgHMxjRKLzIx2kEja41IWm7zFDb-zVKmN0IQk5ppZ6ft7mI4b4-T1-reCIW5FIQuopDH7us42epi89RsWT-AGDKxsFNIpAnNpdGR7BeQg0f08C1oeEcK85_pSuMqbmSvWCsfeHoqosD3rVrUdPUaysYArYkweOCwdP1AixfHWKoUHrosALj_9xvlQEUmoz3CliulyNzJxJpsbYavY01f0KX56XgSuj4eW1rBQ6jm2CcBNSXktjHR1BaA_7FROOsOE127oYbQ6nO-TMWlRqgyRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۳ تست سریع برای تشخیص گوشت خالص کوبیده
🍢
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/698190" target="_blank">📅 21:25 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698189">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در عربستان سعودی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/698189" target="_blank">📅 21:22 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698188">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
فرمانده نیروی دریایی سپاه: ما فقط یکی دو نمونه از تنبیه کشتی‌های متجاوز را نشان دادیم
🔹
آمریکایی‌ها و همکارانشان در منطقه یک سکوت رسانه‌ای ایجاد کرده‌اند که مردم دنیا نفهمند کشتی‌های متخلف تنبیه می‌شود؛ برای همین ما ۲ نمونه از تبیه کشتی‌های متخلف را منتشر کردیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/698188" target="_blank">📅 21:21 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698187">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c4410ea68.mp4?token=jDbYMuv5tH8OzQ-KgAjzSmzfBvmQ7CzpR-x6Yz1TklA0nkgUm611cg1Dmejpr2ZRiT9iGoV4iM53mViEkv4QVxSAFa2hpgwkDeFobFCJfTBa3JG72JzBNk-bwYCEsMSEC74o3iRUB9eTWUCZOFhGqJPHvEawzVZ4fvzZ51gdiAM7hGRsBcHzcY3k2N-Ma1o0feaX4bQyu5kgAhRZvHO5fydKQ3YUVfxQg16VLhvvoasV-fG-qqDh3DDlafj9QB075TleWF0T-E9Yxf_5rhBVNPnQNgFt3a-LVB-y4slL3K5SZR4z_bHYvoBy6lyCIjXFyNhRzGq5zfORwJgyvASJzFg5uqhaXLpj4QkWp3pjsMgwylrxpU96RH3oU1F9M-83IA6It1RG_VHQhkxILPl0sL-U2b7cU75iguekuF8_8mu-uGKxZdrRflRxi1wA3g1TUr0XkrFdC36hE9CjO1hgPLfO4N1-I_wQT6XnYf_O2HeIXt4oH0PnJLQDnl9yH0f1ZY3AlWQQNJPwbnHhBQYInMedzKoi8vkm0jZuZDDW5PG6iXgUmtdcdk0aDFIK03KwDMEnMXTKO28Tw0tVBEkKcYi6xkHo3YDbZT4Qm3nhk6v3CVgPCCGok6RpGMJVcApzcFp1ZEIeIiH8eg1BloO3AQCfn0QgXW3vPpBJYTS8KwU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c4410ea68.mp4?token=jDbYMuv5tH8OzQ-KgAjzSmzfBvmQ7CzpR-x6Yz1TklA0nkgUm611cg1Dmejpr2ZRiT9iGoV4iM53mViEkv4QVxSAFa2hpgwkDeFobFCJfTBa3JG72JzBNk-bwYCEsMSEC74o3iRUB9eTWUCZOFhGqJPHvEawzVZ4fvzZ51gdiAM7hGRsBcHzcY3k2N-Ma1o0feaX4bQyu5kgAhRZvHO5fydKQ3YUVfxQg16VLhvvoasV-fG-qqDh3DDlafj9QB075TleWF0T-E9Yxf_5rhBVNPnQNgFt3a-LVB-y4slL3K5SZR4z_bHYvoBy6lyCIjXFyNhRzGq5zfORwJgyvASJzFg5uqhaXLpj4QkWp3pjsMgwylrxpU96RH3oU1F9M-83IA6It1RG_VHQhkxILPl0sL-U2b7cU75iguekuF8_8mu-uGKxZdrRflRxi1wA3g1TUr0XkrFdC36hE9CjO1hgPLfO4N1-I_wQT6XnYf_O2HeIXt4oH0PnJLQDnl9yH0f1ZY3AlWQQNJPwbnHhBQYInMedzKoi8vkm0jZuZDDW5PG6iXgUmtdcdk0aDFIK03KwDMEnMXTKO28Tw0tVBEkKcYi6xkHo3YDbZT4Qm3nhk6v3CVgPCCGok6RpGMJVcApzcFp1ZEIeIiH8eg1BloO3AQCfn0QgXW3vPpBJYTS8KwU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش مشاور عالی سپاه به ادعای ترامپ مبنی بر کنترل تنگه هرمز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/698187" target="_blank">📅 21:17 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698186">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/482cb77a54.mp4?token=SAQ6X2CdUFr5RX6X9TbhjquBTByFeu3O40ftOraFF-jyOsxMWMyGO97YZt6-AyexBI1I9JVLUZdmZGlxq950yTTMwx9hb9W2aWN3Cxo9PuzBdZMqAGoY73tCEj-FmgCxqHn9RE4J0BgtC_TCnsrrUmEyQ_FH15MYpQUCiS-bcmh1K_AAUXt_5oJenXwGibM41i8Qk8u8pDPFIPpMlHar7O6cHztiwt9HD0frDiTalCEfsk-a3eqk-U8yM0MWUDbzyj9bInoIx3A4JjJn1d8g7hoCg1G9PrPNXjdQYvYN_e9yuv_qTp0ng-SrY2yhPkM9_epmh1dLfKjr3FY3uxPNHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/482cb77a54.mp4?token=SAQ6X2CdUFr5RX6X9TbhjquBTByFeu3O40ftOraFF-jyOsxMWMyGO97YZt6-AyexBI1I9JVLUZdmZGlxq950yTTMwx9hb9W2aWN3Cxo9PuzBdZMqAGoY73tCEj-FmgCxqHn9RE4J0BgtC_TCnsrrUmEyQ_FH15MYpQUCiS-bcmh1K_AAUXt_5oJenXwGibM41i8Qk8u8pDPFIPpMlHar7O6cHztiwt9HD0frDiTalCEfsk-a3eqk-U8yM0MWUDbzyj9bInoIx3A4JjJn1d8g7hoCg1G9PrPNXjdQYvYN_e9yuv_qTp0ng-SrY2yhPkM9_epmh1dLfKjr3FY3uxPNHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آیا به خاطر سیگار، تارهای صوتی و حنجره از بین می‌روند؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/698186" target="_blank">📅 21:15 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698185">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
وزیر راه و شهرسازی: آمریکایی‌ها فکر نکنند با تحـریم حمل‌ونقل می‌توانند مانـع سفر ایرانیان به کربلا و نجف شوند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/698185" target="_blank">📅 21:13 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698184">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
دریادار عظمایی، فرمانده نیروی دریایی سپاه: آمریکایی‌ها اگر فکر می‌کنند تنگۀ هرمز باز است نزدیک‌تر بیایند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/698184" target="_blank">📅 21:12 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698183">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f65bad778.mp4?token=oqkyHIpCOKVFQRWsDO1rk47Dm7uc6yg9ciNtJXihdbN9imv4pEfFrK3frm5EkBW05nymW0HvUGunIeJWiuu2Gsuk4DoBVSUUZ7ec-Tek3WLXPP_IcalsZl5enSISLxZi-UPi9qCRCAe4qBS7EZbRGM2dqt4KARezqqm_lSahlkzwy5pCrMrPWLhLkxONIXQXIhObIsNzW7aJfvCF7QX_swdyrNjIefMRHqeXjx6WIdQzhVbwfGRc3uTSWKx0TZM49lXpvTdZD7q4ucJaxLGCI9tCq0lY3fn7w9e5D2Zh0C3KfjompTibzkog3FkFzgTHCpuI2NtuqDqkDgIyhMSsXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f65bad778.mp4?token=oqkyHIpCOKVFQRWsDO1rk47Dm7uc6yg9ciNtJXihdbN9imv4pEfFrK3frm5EkBW05nymW0HvUGunIeJWiuu2Gsuk4DoBVSUUZ7ec-Tek3WLXPP_IcalsZl5enSISLxZi-UPi9qCRCAe4qBS7EZbRGM2dqt4KARezqqm_lSahlkzwy5pCrMrPWLhLkxONIXQXIhObIsNzW7aJfvCF7QX_swdyrNjIefMRHqeXjx6WIdQzhVbwfGRc3uTSWKx0TZM49lXpvTdZD7q4ucJaxLGCI9tCq0lY3fn7w9e5D2Zh0C3KfjompTibzkog3FkFzgTHCpuI2NtuqDqkDgIyhMSsXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار نقدی: آمریکایی‌ها اگر تصمیم به حملۀ زمینی بگیرند آن‌قدر تلفات خواهند داد که خودشان تسلیم شوند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/698183" target="_blank">📅 21:10 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698182">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآیت الله حسینی طهرانی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jcbn89uxtIwCPTM-e5KjemBHhG7r5PENltY0h_UDwBHG9QhIjnSy-bboPW0Kk2fYRIDMWQ95YddZnAoDt302QY0MzjGzVYlvCuRWTyXplVAnpdHnYPJAqXsPlPUK4r8UBHc5KeMfo-H0UuVeX0lUk8RbDPOnuSKEvkleCupX-GskQBegh0SA3OHhfYSzT6kXN3U-2ciWUFJsigYXd4L7HxAQ7Eq7R9MD1LdbC45tJKcvx9vs4obqX2mChNOoNzEvoOSkztwbgFJZx_i5SnQpjZMmGuKFizwwrSCjdVcqr5VFnG3JAH3o7cjRHgB8iTExsi7yodLvYWC9_CbVTTWA1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسم الله الرحمن الرحیم
🔸
حقیر به اخوان و اخوات گرامی سابقا هم مکرّر عرض کرده بودم که:
حضور در تجمّعات شبانه در این شرائط، موجب رضایت مولایمان حضرت صاحب الزمان علیه‌السلام، و نصرت نائب بزرگوار ایشان: آیت‌الـله خامنه‌ای حفظه‌اللـه، و وسیلهٔ عزّت اسلام و دفع طمع کفّار و مستکبران از میهن اسلامی است.
🔻
و تا زمانی‌که فتنه‌ها و شیطنت‌های دشمنان باقی است و رهبر معظّم نظرشان بر حضور در تجمّعات است، شایسته است که همه در حدّ توان و وجود شرائط حضور داشته باشند. و البته مخدّرات در عین حضور، کمال عفت و حیاء را نیز مراعات نمایند.
🔸
نفس حضور در این تجمّعات به قصد تقویت حکومت اسلام مصداق جهاد فی سبیل الله و سلوک الی اللـه است. خداوند همه ما در تحصیل رضایت امام عصر عجّل‌اللـه‌فرجه‌الشریف موفّق بدارد.
و السلام علیکم و رحمة الله و برکاته
✍️
العبد الآثم السیّد محمّدصادق الحسینی الطهرانی غفراللـه‌له
🗓
۲۶ ربیع‌الثانی ۱۴۴۸ هجریهٔ قمریه علی هاجرها الاف الثناء
🔗
hoseini_tehrani</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/698182" target="_blank">📅 21:09 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698181">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87b5f17af4.mp4?token=qjuUS6JfFyXwdTIchVcHOBQKuiAqrwKc_-3KNeWzn8bb17A9_dEEu7NKVbWzZMfVBRKAUWW7Temb7aLuQ9GlOsxB78AgtK_gMIxrCel8OIpVyOXcKzVp1PmaFnNZ2Kv7ngIzBxD4SIemRRKvEI1GRPWRfOpqkpIeTTdOxq_7bByGd4cHcav06UWa8vo_7Pp8rBTbPvJC8Glmn70baMG_BfWYxjobw4rVDsOINQNnbXB2mN1e0mrc0p8WsfZeV-Xmtj_Z3iIj8pKdb8sCKooYLNlAsosnnD0RFMt7k00lIuMHqavG_t0WfgfL605CRTJZN5AFsuJ8TkO13xbniBUrSAT1NA6ebtnRgan_CB1A02PNsUauzQ14nJzd1B1Mj3AZhMqRcl7pChVVDAKctC3ScimCS5P5lGLhK4asBNZkiQkUy03q9vQ_GqtZAX-t0gsJ1tDrC-imkIVTpoLW9yRcBT4hgAi3PrEDUgOPKKStuEKpugPPJM-kfil9-PxUaEYbiHlKP-nvglFFp122oTjpAyAcIcp9mqBq7IskslQm8cDiHeIgHovWGU3c9bkAb3T6oACMagRMDQc2SHYIfEjyZjFDop2JEYa0KxkuXq4tpPfgsyhCc09EgwIMRH8RMyx0cKpqqczv2nQhHfOnPBa3iH6MBREKz7KPHbNaTFuaalQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87b5f17af4.mp4?token=qjuUS6JfFyXwdTIchVcHOBQKuiAqrwKc_-3KNeWzn8bb17A9_dEEu7NKVbWzZMfVBRKAUWW7Temb7aLuQ9GlOsxB78AgtK_gMIxrCel8OIpVyOXcKzVp1PmaFnNZ2Kv7ngIzBxD4SIemRRKvEI1GRPWRfOpqkpIeTTdOxq_7bByGd4cHcav06UWa8vo_7Pp8rBTbPvJC8Glmn70baMG_BfWYxjobw4rVDsOINQNnbXB2mN1e0mrc0p8WsfZeV-Xmtj_Z3iIj8pKdb8sCKooYLNlAsosnnD0RFMt7k00lIuMHqavG_t0WfgfL605CRTJZN5AFsuJ8TkO13xbniBUrSAT1NA6ebtnRgan_CB1A02PNsUauzQ14nJzd1B1Mj3AZhMqRcl7pChVVDAKctC3ScimCS5P5lGLhK4asBNZkiQkUy03q9vQ_GqtZAX-t0gsJ1tDrC-imkIVTpoLW9yRcBT4hgAi3PrEDUgOPKKStuEKpugPPJM-kfil9-PxUaEYbiHlKP-nvglFFp122oTjpAyAcIcp9mqBq7IskslQm8cDiHeIgHovWGU3c9bkAb3T6oACMagRMDQc2SHYIfEjyZjFDop2JEYa0KxkuXq4tpPfgsyhCc09EgwIMRH8RMyx0cKpqqczv2nQhHfOnPBa3iH6MBREKz7KPHbNaTFuaalQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کشف ۳۰ تن گوشت فاسد در کارخانه تولید همبرگر در شاهرود
#اخبار_سمنان
در فضای مجازی
👇
@Akhbar_Semnan</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/698181" target="_blank">📅 21:07 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698176">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D3ydcCr1O7DMiYTcwy2zkqi5bHWqFNme0DRRXIRg_QnzUV-xOqZ_Anc94pcfLrPglKoSG0-0zoRSrmlnwe18CkWH1OFyHdpw9FSJKrSXKv0C_XCVCpo6Q5Nnn0e_jxtoUfMbiaRtWS51MloEmealHEeniQRyJwAWYa-XvaJsBEYXh0DKW8bwzG00qd93AS3cje2SHkQDuagA6Q4Rs-Krfw-J-nsBGgNWoKPUAww_rLxnFAm2Oq3E3TGtWYihMWKwxhRHejBz1P7tFcvUgbJNADo7QDacJwyAwIlcn_mI-znd8OPXSv4fH3tQsG3Fb7BRGeRgJ_cR6QdQHpgSNlUU2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R2frgEgqAyD_ALTyJuMAhrvPdPN2cwPArSPuOda6LxKdz1kTKJks9ZHL3WFgASvi8bEJRWHzcWCt2-ld_xCtrN-jhjRX2KY-DJpthDIFiuORxrThuP6Cg20D03wUUFVgBcQ3yGf5241h1DoqsPo5j4WAhGdiuuU3Wqay_7_HcC9CosxoflcgZfgQm8X97KnVxZFnOYej_HBmPiEQ_aY5aXGxMOZaZImUkO4nTrmMUSSGUrwewVhq6WFidHmf9GmpbyIN49F5cseHUNy2dFjDOguCfc84HlKTCNyY1sZjYOwdZv0KmP7IefBuUmck2mGmR36_CdcQI2S9CEXa0Hh2tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e_4Nf71ljivqIlO52buHX5EbmJThZRWeF2DWkK-PXcGJarT3mBBG3YnZGnBw9ri-nTJBgi3F-MDPhCVgHIvZaSkCq1q-r5dw7qjoBvnQg66swgwgy7zZBSctK_h9WzL2ZQv6JH01l2bW9ONTYwQAVtneqeg_JEhTN4BteuUfG0Ig5AGsGu7kTu_q9wFTS_s9qOpwyMaY5PoCY24i9wQtaO_H1tPW1byFh2u7TOEGkiGqNzlJJrn-40W49jacJDVwJRXjrUIoXYztkffw7qxXPimj-dwYTJZBM6BpbpwdxSlGsJak-prgl2EUvmr4Bev9JN3HDpNKCfA9Fu4mKfsbTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hwoch3WO0Kq1OJkXId-LBvnZ8WMAULa4azR5GLZKNICR8_DnebZ3WlAbOT3Gf0APPrtxUn5mnQq7_-FlyI9LtZWvea1THg88Z-aL50by_kI8ZA8GQWfABaFearTDrqieGbLrSCFxxyZ_cvCmGa4aNr-UJ_vUx3nPFYUeUYSQIBjA5Upi_KkSKqN92AWWEUrrKTkrJ5dCDA3QX7XXy4Ds5-B5pQf5aBQMFyG3wY4wEyxXICxzoNFlBL4oCw09SBAiIzre0CBq9xICdUt-6AIWUnLCOzei5rp8RYG-u-75MDP88vSfrp1wP8h9BHGZR0dipzRZ_zAu4so_L9m2fa7xxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z0e5-LfHWLvec_Q9_51PBhZyzott4sPuxF3HwD8eE5rQ1cFpiPPPhL3bhqZy0h_a78db4uAOBQEEhgSNVZE4BlcTwRuEBLQSs6b6JPoc_OODsZha0KHcGcvlsaWvXc5foy9xbqRT1pmi50fub60w3QSgYsBTGcPep5akJ0aM7wyQlT706KyLzexnDonlNyXWIuv1Y54ypojEpDBK9-a3CtkEyaPxtKWJvohLiILt_4AgHhtzDqTX6MIGHNNJU9CzrS1pwDlAqM7P-6SS-uxs0ZtXVj8Iceu8QNbjbN38YVB-4PNFthKIlDa9NHS8qU2i8bRxOpFWvfs754jy9Ie_aw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۵۰ اپلیکیشن کاربردی که اگه روی گوشی‌ نداشته باشی، ضرر کردی!
#هوش_فوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/698176" target="_blank">📅 21:05 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698175">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ظهوریان: امکان نظارت بر کالابرگ برای این که دقیقاً صرف چه کالاهایی می‌شود، کاهش یافته است
میثم ظهوریان، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
مبلغ فعلی کالابرگ به دلیل تورم هزینه نیازهای اساسی خانوار را پوشش نمی‌دهد، با این حال میزان دقیق پوشش آن به دلیل تفاوت نیاز خانواده‌ها مشخص نیست.
🔹
با اضافه شدن فروشگاه‌های معمولی و گسترش اقلام قابل خرید، امکان نظارت بر اینکه کالابرگ دقیقاً صرف چه کالاهایی می‌شود، کاهش یافته است.
🔹
دولت می‌توانست کالابرگ را به سبد مشخصی از کالاهای اساسی متصل کند تا علاوه بر تأمین نیاز مردم، تقاضا برای تولید محصولات منتخب نیز افزایش یابد، اما این سیاست به‌طور کامل اجرا نشد.
🔹
دولت وعده داده بود اعتبار کالابرگ را متناسب با نرخ تورم و قیمت کالاهای اساسی به‌روز کند، اما عملی نشدن این وعده می‌تواند اعتماد مردم به طرح‌های اصلاحی آینده را کاهش دهد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/698175" target="_blank">📅 21:00 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698174">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
دریادار عظمایی، فرمانده نیروی دریایی سپاه: آمریکایی‌ها اگر فکر می‌کنند تنگۀ هرمز باز است نزدیک‌تر بیایند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/698174" target="_blank">📅 20:55 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698173">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11324dfbde.mp4?token=DTh6L4KSgUzrS8BawUCcSeqd4tLl1XG-ubQbadKGeIL6s8o_SKLx1SKR3s3xILz6nODryuB36xmKjdZlYHttc6_CjAbDbT-KOO8qqUz3lPdXKmxIv5bgdKCyfexJrH9QOsNsb1zksN7qMG1LC5DcV2R7ErhYlIrAlBNlvA2wCUkURK0ctNMixEXyKH_i-Wa3zwtpxWM1hD7l8HWlFpvjbRvmpA_LgqHajMDLDjFpMuOxwzj27Rv6glnrz97WXBUtOFQRmPYeZ3C8o-Bt5qlT0TsbRzkx5JdUr3KNbw_mFqKZalGuVz8zv6Aty9EZUGnLz4tc9ORmHkPNlUnszidj_kypGhaYbVDEUM8tE-PeLHp1BESwoxDHYLdQyHalyw3dquS8-5ycU3kaaOFoGr6nO5hq_FPw5cq0i9EGwIx0z4hpLKXB0TcmSc30KzXL--Yb361I-QDVfGOxCq_xOkILDYnoIveiyMP_0VH0EFDZ7PmrH5OgFXy-owd5kw_u7pDPyTcytfxgx_BJ80sDEuQVJmdiNCdXbp4rY3GoMJO3G6KdW8SS6ysGc1AKpvbgZ008H4ZPryfUDK1fF4hJcKen-pvXURRFU1sK_fsUDBiIZS5W0053Yth_OmX4Wd0u_OQ7zF10XPHBPMlnYUuv0PDXwlZaGyT8n8W1UYSh7S_6LLk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11324dfbde.mp4?token=DTh6L4KSgUzrS8BawUCcSeqd4tLl1XG-ubQbadKGeIL6s8o_SKLx1SKR3s3xILz6nODryuB36xmKjdZlYHttc6_CjAbDbT-KOO8qqUz3lPdXKmxIv5bgdKCyfexJrH9QOsNsb1zksN7qMG1LC5DcV2R7ErhYlIrAlBNlvA2wCUkURK0ctNMixEXyKH_i-Wa3zwtpxWM1hD7l8HWlFpvjbRvmpA_LgqHajMDLDjFpMuOxwzj27Rv6glnrz97WXBUtOFQRmPYeZ3C8o-Bt5qlT0TsbRzkx5JdUr3KNbw_mFqKZalGuVz8zv6Aty9EZUGnLz4tc9ORmHkPNlUnszidj_kypGhaYbVDEUM8tE-PeLHp1BESwoxDHYLdQyHalyw3dquS8-5ycU3kaaOFoGr6nO5hq_FPw5cq0i9EGwIx0z4hpLKXB0TcmSc30KzXL--Yb361I-QDVfGOxCq_xOkILDYnoIveiyMP_0VH0EFDZ7PmrH5OgFXy-owd5kw_u7pDPyTcytfxgx_BJ80sDEuQVJmdiNCdXbp4rY3GoMJO3G6KdW8SS6ysGc1AKpvbgZ008H4ZPryfUDK1fF4hJcKen-pvXURRFU1sK_fsUDBiIZS5W0053Yth_OmX4Wd0u_OQ7zF10XPHBPMlnYUuv0PDXwlZaGyT8n8W1UYSh7S_6LLk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
می‌دونین موضوع قدیمی‌ترین بیلبورد جهان که ۲۵ قرن پیش داریوش بزرگ بر سنگ نوشت، چیست؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/698173" target="_blank">📅 20:52 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698172">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cff0afaa5d.mp4?token=ERhU92RmgYwKMiBF4n_w6Kp4SiNKtxgRxSV9wjDJ0a-vI6vqYe1w80-ADlnzpC7-yGDQ_WFv8KXykj7d8uaBSrNG47IM6roPAhyr4YbOe6KyB4IwT-fP1GJK9Zy-WBUzeqGYaq4ZavM4LW0waD4oYLVNPIyyAy_TH7ii1QyHv9tZj1Utg2w6-W_qAv41sDHuyGzJIk9W9wvp8ttLZlm2IbfllrHSIn95azI07Knw3r4EVpZgue76hJHrLUWEpTvCii3kYsuH-cq78YLHkU0ufMAsNt-ZZM_rn_0Ma3zqPOAaQpFuBsGyJlcBKtjzRJuvMiXhLLYaDy1JTozmyjIp2ino1Se96g9HIdFcP0AEYgfUwdcA5JSyIkzi0Su0j9cWwjXq_wtwOkY_q67rlczmZefjkJLLdlFU_cdRLuV9qMDTF7tVkIeShV4_AEcLv0DY85DFmrH8eePMewyV6CYIdya3pNZzC62gIFe90toC25reZbcHv4oxtP0T1e6Z5iGOILB2OwQhHPt7e000yIuEWV6eKhbjoshwX2uoUhzcxuBxmM0om59OGJ_ARPJbqGuSA4258UmcD47lTWnXNMFyWqvrr45vyzEkEJipCmRB0EG-RabNP4gq5lBDDvAv_byXC_ptNgasETNNlazABrOFvQ7o-xRNqpq_Zfngq9Mr4E0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cff0afaa5d.mp4?token=ERhU92RmgYwKMiBF4n_w6Kp4SiNKtxgRxSV9wjDJ0a-vI6vqYe1w80-ADlnzpC7-yGDQ_WFv8KXykj7d8uaBSrNG47IM6roPAhyr4YbOe6KyB4IwT-fP1GJK9Zy-WBUzeqGYaq4ZavM4LW0waD4oYLVNPIyyAy_TH7ii1QyHv9tZj1Utg2w6-W_qAv41sDHuyGzJIk9W9wvp8ttLZlm2IbfllrHSIn95azI07Knw3r4EVpZgue76hJHrLUWEpTvCii3kYsuH-cq78YLHkU0ufMAsNt-ZZM_rn_0Ma3zqPOAaQpFuBsGyJlcBKtjzRJuvMiXhLLYaDy1JTozmyjIp2ino1Se96g9HIdFcP0AEYgfUwdcA5JSyIkzi0Su0j9cWwjXq_wtwOkY_q67rlczmZefjkJLLdlFU_cdRLuV9qMDTF7tVkIeShV4_AEcLv0DY85DFmrH8eePMewyV6CYIdya3pNZzC62gIFe90toC25reZbcHv4oxtP0T1e6Z5iGOILB2OwQhHPt7e000yIuEWV6eKhbjoshwX2uoUhzcxuBxmM0om59OGJ_ARPJbqGuSA4258UmcD47lTWnXNMFyWqvrr45vyzEkEJipCmRB0EG-RabNP4gq5lBDDvAv_byXC_ptNgasETNNlazABrOFvQ7o-xRNqpq_Zfngq9Mr4E0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حیوان خانگی وقتی دغدغه‌ات نان شب و آینده مالیته، شاید بیشتر از عشق، هزینه و انرژی ازت بگیره
برای ثبت نام همایش بزرگ استاد مطلبی در مشهد از کد تخفیف BMT72 در لینک زیر استفاده کنید
👇
https://evand.com</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/698172" target="_blank">📅 20:50 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698171">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
سردار کارگر: راه‌های جدید برای ارتباط اقتصادی با کشورهای منطقه پیدا شده است
سردار بهمن کارگر در
#گفتگو
با خبرفوری:
🔹
تنگه هرمز کماکان بسته است و نیروهای مسلح جمهوری اسلامی ایران بر این منطقه احاطه کامل دارند. گرچه دشمن ادعاهایی دارد، اما نیروهای مسلح با به‌کارگیری تاکتیک‌های جدید، احاطه بیشتری بر مجموعه تنگه هرمز دارند.
🔹
در صورت پایبندی دشمنان، به‌ویژه آمریکا، به شروط و تعهدات خود، تصمیمات بعدی در داخل نظام گرفته خواهد شد. جمهوری اسلامی ایران تاکنون تاب‌آوری بالایی از خود نشان داده است.
🔹
جمهوری اسلامی توفیقاتی در زمینه پیدا کردن مسیرهای جدید برای تأمین کالاهای اساسی و توسعه ارتباطات اقتصادی داشته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/698171" target="_blank">📅 20:47 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698170">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3713b696a.mp4?token=KjFMS-KATxP3AWF7IJrTTpaywPQSBnVovgEZh4wIJEPCBCXzgcEsDs1xf-FonBFXtaeTOweOIpjnX_l8675ba9Wa-qlXbJx-XCd_OCszst3GLPFlF2En_c4Lk_lCNJ1QvAnidX9gXq964WUyBksAkJwSHG8YpgRB-joxSVv1cOaWSwtu5LoztSsCHjx_WTmH27P6LyeEYlIbpZORPHImGdy_JMepy_ec286sLjgz6K4OMB7eoaPbqsGnim27JfKiapospZ5dvFZvhc2AE2Uw_DPxSgrsszPoKUnqMHsGw1eoEw3UH0yeE2vMw-KDClAXOKhDFBqUvkqRWCkRMM369A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3713b696a.mp4?token=KjFMS-KATxP3AWF7IJrTTpaywPQSBnVovgEZh4wIJEPCBCXzgcEsDs1xf-FonBFXtaeTOweOIpjnX_l8675ba9Wa-qlXbJx-XCd_OCszst3GLPFlF2En_c4Lk_lCNJ1QvAnidX9gXq964WUyBksAkJwSHG8YpgRB-joxSVv1cOaWSwtu5LoztSsCHjx_WTmH27P6LyeEYlIbpZORPHImGdy_JMepy_ec286sLjgz6K4OMB7eoaPbqsGnim27JfKiapospZ5dvFZvhc2AE2Uw_DPxSgrsszPoKUnqMHsGw1eoEw3UH0yeE2vMw-KDClAXOKhDFBqUvkqRWCkRMM369A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراضات دانشجویی به آلبانی رسید
🔹
تجمع اعتراضی دانشجویان در پایتخت آلبانی با مطالبه بهبود شرایط آموزشی و رفاهی با درگیری پلیس با معترضان به خشونت کشیده شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/698170" target="_blank">📅 20:44 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698169">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h5VG07ujR3l6-obc5LPrXdiO0-upWMx2_zQ9yymvMkAkSR9fhpIPoEcAVtA2yqoIHADCYASaEy4yHWLweX9ie_1ngz9gC36HSKkg5Zbfeq1qigG3aoLL1zj0Q3ckowpX5_iTC8rcszEniMIgzyRj8fWlyyYrRB2kCItIEHZa6mhg0QnrHyfWYI6CqDS6jaIpV92PYy_oXu2T6b29fvIFr5ro1cQFPcaH6HTsYAYe9FYqJG4lLUgIvcLrrJkqAXQVbDV-ffBC3sOl-yrzlGyar2PXGi8chodSvPFi9pxgbjgMbvgdMio_ERCTrk8dEaieZb5QvxSkES9qRpjXfpTaSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ سالگرد تأسیس نیروی دریایی آمریکا را تبریک گفت و محاصره ایران در تنگه هرمز را دستاورد تاریخی خواند!
🔹
از دیگر افتخارات نیروی دریایی آمریکا می‌توان به بستن تنگه‌ای که باز بود و بعد، دست‌به‌دامن دیگران شدن برای باز کردنش اشاره کرد!
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/698169" target="_blank">📅 20:42 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698167">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
نیروهای مسلح یمن به ۴۰ کیلومتری جاده ساحلی در خلیج عدن رسیدند
/ صداوسیما
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/698167" target="_blank">📅 20:39 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698166">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dS8AWCimRh98YXfoBZR6Ss8AAE19z6dWYE7roMDRDTxL9dFjNe_5XxvsbGyG7oMduCJjqI-Xrma-hDJXTAshO1cVYr2W8OFwnU9Dw6cAjjTck0lT5aJElChIwhuES2qiuBd_eXsy6jRZ9bVXpxbtV5FEeKC3orVArjGWw9nAZAJOtfddDQ9Xa28xeVAP3yi9F2Lwl6rHOLElTO3FkplFwjdtZ_u0gX8j8miMdjI3R3oJV-lDTvjrMw7kx9IgQYuWOxo8u2yABSUQaL9GrWv2Lg8ykLwSiZtQ-RuDS5uOkEwU7H4-njAP_oFKy1Fx364tIYjQmQQ_oKIo69zdIWr4tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مدیرعامل شرکت آب و نیرو در کنفرانس بین‌المللی مدیریت پروژه: مدیریت تاب‌آور؛ پارادایم نوین پیشبرد پروژه‌های زیرساختی در زمان جنگ و تحریم و محاصره
🔹
مهندس داود کامگار، مدیرعامل شرکت توسعه منابع آب و نیروی ایران در این کنفرانس، با آسیب‌شناسی دقیق وضعیت فعلی پروژه‌های زیرساختی، استراتژی «مدیریت تاب‌آور» را به عنوان تنها راه برون‌رفت از بن‌بست‌های اجرایی شرایط موجود معرفی کرد. تغییری که در آن موفقیت، در خلق ارزش از منابع محدود و کاهش «زمان افق طراحی پروژه‌ها» معنا می‌یابد.
🔹
وی افزود: در شرایطی که زنجیره تأمین با چالش‌های اساسی روبروست، اصرار بر اتمام کامل یک ابرطرح می‌تواند منجر به حبس سرمایه‌های عظیم و افزایش طرح‌های نیمه‌تمام شود. لذا راهکار رست، «خُرد کردن» پروژه‌ها به بخش‌های مستقل، مرحله‌ای و زودبازده است، تا مردم بتوانند از منافع آن زودتر منتفع شوند.
🔹
مهندس کامگار گفت: استفاده از مهندسی ارزش و مدیریت ریسک از همان ابتدای پروژه، کلید جلوگیری از اتلاف منابعی است که در شرایط بحرانی، به‌سادگی قابل جایگزینی نیستند. لازم است منابع و لجستیک طرحها با هم دیده شده و از انباشت دارایی‌ها جلوگیری شود.
🔹
وی افزود: تصمیم‌گیری جسورانه در شرایط پر ریسک کنونی اجتناب‌ناپذیر است و باید از مدیران پروژه در این مسیر خطیر حمایت شود.
🔹
مدیرعامل شرکت آب و نیرو، انگیزش، تأمین نیازها و حفظ روحیه سرمایه‌های انسانی را، بخشی لاینفک از استراتژی مدیریت تاب‌آور طرحها دانست.
🔹
مدیرعامل شرکت آب و نیرو در بخش پایانی سخنان خود تاکید کرد: معیار موفقیت در پروژه‌های زیرساختی باید از «زمان و هزینه صرف» به «میزان ارزش و منفعت ملی ایجاد شده» تغییر کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/698166" target="_blank">📅 20:38 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698165">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50226ddbc1.mp4?token=meO6CpTZJrkUN86onj0D6CQ84go8-dn5qyjaDver_QVeI9qW7d-iFOQnvoM7znyo58XwwgcCyexeozKlVz7092WdnUvd6Qf4s3qt81d0gtSfKjItQsg3mMAWBLCbsyNatYrq1ge6RvUAYSZ1yFnFZ1vmCinfsTrOC-3T2V2TK1tcGHk2G3akp-J0FQDmEmHx-0_C3jDF66M3LLOVC4YLOxQp-ulwKfkfn9wbBPWj8M6v4sAxzKyybiVjqaNr7Ozkml1Fi0MYIxdsiKqsaRfbm66GtlOUsLGW4iq3IcmGlnM23ozYTyCYI7dnv3Gklh4G60r5CD-zMkOD1KCIZ-WosG6GCRsr255kyDd8pAL_fQKyJ8scvp1Ym4vkL_9OE9U5iNa7oato18WkoOQdfJ7w55igiefZXepVEGp9LovenlnhAT90T97eA-yQvjeKqE1nrT4Iira3CIv64sLb0euwleomPsIrhTfd15Wt2BmbY_IIzXmlhHZO1jaX7VMVjMHep1ppGwdTQWEDHBF8hj2cw8vyTFGjS8yn1GRcRNuky7VDCbpTTfB3SRxmUt3_cMbRq_X6gW90SBApsH9bL551cUbyZDID4T-TXtjZIn-0qetjDj4XGpd7GXKDqwANxooq0ljYS_n0OZGN1CFxAUB8HgQIl_k9HB6Y5tO0joLm_lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50226ddbc1.mp4?token=meO6CpTZJrkUN86onj0D6CQ84go8-dn5qyjaDver_QVeI9qW7d-iFOQnvoM7znyo58XwwgcCyexeozKlVz7092WdnUvd6Qf4s3qt81d0gtSfKjItQsg3mMAWBLCbsyNatYrq1ge6RvUAYSZ1yFnFZ1vmCinfsTrOC-3T2V2TK1tcGHk2G3akp-J0FQDmEmHx-0_C3jDF66M3LLOVC4YLOxQp-ulwKfkfn9wbBPWj8M6v4sAxzKyybiVjqaNr7Ozkml1Fi0MYIxdsiKqsaRfbm66GtlOUsLGW4iq3IcmGlnM23ozYTyCYI7dnv3Gklh4G60r5CD-zMkOD1KCIZ-WosG6GCRsr255kyDd8pAL_fQKyJ8scvp1Ym4vkL_9OE9U5iNa7oato18WkoOQdfJ7w55igiefZXepVEGp9LovenlnhAT90T97eA-yQvjeKqE1nrT4Iira3CIv64sLb0euwleomPsIrhTfd15Wt2BmbY_IIzXmlhHZO1jaX7VMVjMHep1ppGwdTQWEDHBF8hj2cw8vyTFGjS8yn1GRcRNuky7VDCbpTTfB3SRxmUt3_cMbRq_X6gW90SBApsH9bL551cUbyZDID4T-TXtjZIn-0qetjDj4XGpd7GXKDqwANxooq0ljYS_n0OZGN1CFxAUB8HgQIl_k9HB6Y5tO0joLm_lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اجرای جالب پسران دانشجو در خوابگاه که در چند ساعت میلیونی شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/698165" target="_blank">📅 20:35 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698164">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
سارق مسلحی که به خبرنگار هم دروغ گفت
🔹
باند چهارنفره سارقان مسلح که با استفاده از سلاح جنگی اقدام به سرقت ۲۰۰ گرم طلا و ۳۰ ساعت لوکس کرده بودند، پس از دستگیری، در گفتگو با دوربین خبرفوری فرافکنی‌های عجیب داشتند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/698164" target="_blank">📅 20:33 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698162">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V4RsgORs_GruAi6WnSbjj1Okci_Ou9s8BiNwpkn-6MX-y6k-bRxFksseaWX79tZh6I7GI-nqr-Je61i4zrJ85G7HizCnXqnRx5p6VAUCdP_aHjIaWvgFfekY3avotHow0zvK4CkkwWjefX3N9EuvvL4TKpbPyB6sJIvy0hd3heVQXfojsHBGLYE7elelfYAa9S4nf1VTOa8UNKrYPlGwpHLhJT4C2MfolXjCd8h7H7di-Co_rPLunMboHNch8qs0NsZQEl4UUmS7ppq9iioiRfGcOrc8SY8SyYuaep7Q7v9dWT64Fen8ZHxeJ2hw-W23ceY1QL4zJ07klBpZ70EjJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ما منتظریم
🔹
سخنگوی سپاه با انتشار تصویری در فضای مجازی نوشت: ما منتظریم.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/698162" target="_blank">📅 20:18 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698161">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(El Nv)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ixLSFdhXg2Y-lRygn3A9TkYjRKGxGKqJ8e4l1hWu5E2MK8_Iua78uZ23G7eYBqwvCyqpb5M7A1CTiude5XrdgQNLt4gnD51aKfCBeLvse045z0OX_Nv3wUP6xS0ryY44vuLjNNh7rg2CuMleAZsxq9NK0lBKoLee69HO-A4IjaTm-5ZiGw_8Lj4uYkuEWTZIy1L5WgmXKHXy8RZSG0Nuktd3PvtIQoqVe7Gnq4bRiJaP7Vk5BILrtJzZeb8fdCsayFY2ay4kPoYYZKfug_L4Rurt9QOZy1j3pSmyqu1VQmnWcRNJgDGVuNAtKHKEvlrmYfdzQqG9yfwLCEEkJrYjWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⬅️
در بازدید سرپرست وزارت نفت و مدیرعامل بانک شهر از پارس جنوبی صورت گرفت
🟢
پشتیبانی ۸۰۰ میلیون یورویی بانک شهر از بازسازی تأسیسات آسیب‌دیده پارس جنوبی در جنگ تحمیلی رمضان
🟡
حمید بورد، سرپرست وزارت نفت به همراه مدیرعامل بانک شهر و جمعی از مدیران ارشد این وزارتخانه، از روند بازسازی پالایشگاه پنجم مجتمع گاز پارس جنوبی در فازهای ۹ و ۱۰ بازدید کردند؛ بازدیدی که با هدف بررسی آخرین وضعیت عملیات بازسازی، ارزیابی اقدامات انجام‌شده برای احیای تأسیسات آسیب‌دیده در جنگ تحمیلی رمضان و شناسایی راهکارهای تسریع در بازگشت ظرفیت‌های ازدست‌رفته به چرخه تولید انجام شد.
✅
به گزارش روابط عمومی بانک شهر، حمید بورد سرپرست وزارت نفت، در جریان این بازدید با اشاره به شرایط ناشی از جنایات جنگی دشمن آمریکایی ـ صهیونیستی و آسیب‌های واردشده به تأسیسات صنعت نفت و گاز کشور، از حمایت‌های بانک شهر  به  صنایع نفت، گاز و پتروشیمی قدردانی کرد و این حمایت‌ها را در مسیر بازسازی زیرساخت‌های آسیب‌دیده و تقویت ظرفیت‌های تولیدی کشور حائز اهمیت دانست.
🔵
بورد همچنین با تأکید بر ضرورت تقویت همکاری میان نظام بانکی و صنعت نفت، حمایت مالی بانک‌ها از طرح‌های راهبردی این صنعت را عاملی مؤثر در تسریع روند بازسازی تأسیسات آسیب‌دیده، بازگشت ظرفیت‌های تولیدی و استمرار فعالیت‌های صنعت گاز کشور عنوان کرد.
🔴
دکتر سیدمحمدمهدی احمدی، مدیرعامل بانک شهر، نیز در جریان این بازدید، ضمن بررسی روند بازسازی پالایشگاه پنجم پارس جنوبی، با مدیران ارشد وزارت نفت و صنعت گاز درباره ظرفیت‌های همکاری و نقش تأمین مالی در تسریع عملیات بازسازی گفت‌وگو کرد.
🟡
دکتر احمدی با اشاره به جایگاه راهبردی صنعت نفت، گاز و پتروشیمی در اقتصاد کشور، حمایت از صنایع پیشران و تأمین نیازهای مالی آنها را از محورهای مهم فعالیت بانک شهر دانست و اظهار کرد: بانک شهر با توسعه خدمات پولی، مالی و اعتباری، در کنار صنایع نفت، گاز و پتروشیمی برای حمایت از تولید و تقویت زیرساخت‌های اقتصادی کشور ایستاده است.
⚪️
مدیرعامل بانک شهر با تأکید بر اهمیت تأمین مالی پروژه‌های بزرگ صنعتی افزود: استفاده از ظرفیت‌های نظام بانکی و طراحی راهکارهای متناسب با نیاز صنایع، نقش مؤثری در تسریع اجرای طرح‌های زیرساختی، تأمین تجهیزات و بازگرداندن واحدهای آسیب‌دیده به چرخه تولید دارد.
◀️
تأمین مالی بیش از ۸۰۰ میلیون یورویی بازسازی پارس جنوبی
🔻
بانک شهر با مشارکت در تأمین مالی بیش از ۸۰۰ میلیون یورویی پروژه بازسازی پالایشگاه پنجم پارس جنوبی، در حمایت از احیای تأسیسات آسیب‌دیده صنعت گاز و تقویت پایداری تأمین انرژی کشور نقش‌آفرینی می‌کند.
🗣
این پروژه که فازهای ۹ و ۱۰ پارس جنوبی را دربرمی‌گیرد، با کارفرمایی شرکت نفت و گاز پارس و مشارکت شرکت‌های مهندسی و ساختمان صنایع نفت (اویک) و پایندان، در قالب قرارداد مهندسی، تأمین کالا، ساخت و تأمین مالی (EPCF) اجرا می‌شود.
🔹
در جریان جنگ تحمیلی آمریکایی ـ صهیونیستی، شماری از پالایشگاه‌های گازی منطقه پارس جنوبی هدف حملات دشمن قرار گرفتند که این حملات به آسیب‌دیدن تأسیسات و کاهش بخشی از ظرفیت فرآورش و تولید گاز کشور منجر شد. از این رو، ارزیابی روند بازسازی، شناسایی موانع اجرایی و اتخاذ تدابیر لازم برای تسریع در احیای ظرفیت‌های آسیب‌دیده، با هدف تقویت پایداری شبکه گاز و تأمین انرژی مورد نیاز کشور در آستانه فصل سرد سال، اهمیت ویژه‌ای دارد.
🔴
بانک شهر طی سال‌های اخیر با توسعه همکاری‌های خود با شرکت‌های بزرگ فعال در حوزه نفت، گاز و پتروشیمی، خدمات تخصصی بانکی و مالی از جمله تأمین مالی، گشایش اعتبارات اسنادی و صدور ضمانت‌نامه‌های بانکی را به این صنایع ارائه کرده است. حمایت از صنایع آسیب‌دیده در جنگ تحمیلی، به‌ویژه در بخش پتروشیمی، نیز در چارچوب رویکرد این بانک برای پشتیبانی از تولید و حفظ ظرفیت‌های راهبردی اقتصاد کشور دنبال می‌شود.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/698161" target="_blank">📅 20:18 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698159">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ead0dacf7.mp4?token=Yx0iAnYVHZrciHVbZg3qeeY_kqaSf9YWLfoe3ZITaQgmlKqp7ubZUW_kpKwMW4FyiONdbJiIcIKXT5fWuijQyoWUBvJR2-LOxrVPArI-Q5h2-3X9fWa1hrX6aJQh8aaasj9KvH3HgV3VFKxOE0Jx7StKKsLs2DhzmO9ErhQj3IGy7nruBUtg28yizq8ygVjsDajJVOaQo_zeueRRWRaTj9pZAdi_vSfN3tRGG6jC8l-GUeD2K8cG-euyD8We_P4o3OBt3LycfOWrw13dWbhJyV6KlvZ2ICDG3Tt9wWcQQhJUA15xX-RFE4AR_762UNM5K_PgJmoH3I2-K3fQo0UlyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ead0dacf7.mp4?token=Yx0iAnYVHZrciHVbZg3qeeY_kqaSf9YWLfoe3ZITaQgmlKqp7ubZUW_kpKwMW4FyiONdbJiIcIKXT5fWuijQyoWUBvJR2-LOxrVPArI-Q5h2-3X9fWa1hrX6aJQh8aaasj9KvH3HgV3VFKxOE0Jx7StKKsLs2DhzmO9ErhQj3IGy7nruBUtg28yizq8ygVjsDajJVOaQo_zeueRRWRaTj9pZAdi_vSfN3tRGG6jC8l-GUeD2K8cG-euyD8We_P4o3OBt3LycfOWrw13dWbhJyV6KlvZ2ICDG3Tt9wWcQQhJUA15xX-RFE4AR_762UNM5K_PgJmoH3I2-K3fQo0UlyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار نقدی: سفرای برخی کشورهای خلیج‌فارس از ما برای حمله به پایگاه‌های آمریکا در منطقه تشکر می‌کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/698159" target="_blank">📅 20:16 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698158">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
استاندار گیلان: ادارات لاهیجان و آستانه‌اشرفیه فردا تعطیل است
#اخبار_گیلان
در فضای مجازی
👇
@akhbaregilan</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/698158" target="_blank">📅 20:14 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698157">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
سردار نقدی: هلال‌احمر اردن به ما خبر داد که ۲۰۰ آمریکایی در حملۀ ما به اردن کشته شده‌‌اند
🔹
هتل‌های محل اقامت سربازان آمریکایی در کویت و بحرین را که هدف قرار دادیم از سر شب تا صبح آمبولانس به آنجا تردد می‌کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/698157" target="_blank">📅 20:12 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698156">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/991a002efd.mp4?token=WsxXFoOu092MhAYtsTe2HixSp17_DTOckjpZWf4K8-13wMWWVYKzH5RI9LzoXMbC8ci8WXLUd1SkyeuoXEHIjzthxoaucvVa2Sam-vmUkJk9rnL0WqL0wojtC3bC6fMfLF4oTGtelYtu40VDFNq5aqj6crBkf4ogaexmn3UBZyV6ChnBtMI2MLyQfLwBGNCGwEp-uiGd9K-G-qKGOlhpvmvAW2gqWyzZlT-0UHBJaWBGpQMkgswZYx0Z-AmkAJBZ7YnUBMHFago70yVwq2FAxqGKCCpOu3p6wGaUPfJYkfKUtvg8gs3CcXeu5KtrTAnXK__he-EijiuAVEQOhUYmJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/991a002efd.mp4?token=WsxXFoOu092MhAYtsTe2HixSp17_DTOckjpZWf4K8-13wMWWVYKzH5RI9LzoXMbC8ci8WXLUd1SkyeuoXEHIjzthxoaucvVa2Sam-vmUkJk9rnL0WqL0wojtC3bC6fMfLF4oTGtelYtu40VDFNq5aqj6crBkf4ogaexmn3UBZyV6ChnBtMI2MLyQfLwBGNCGwEp-uiGd9K-G-qKGOlhpvmvAW2gqWyzZlT-0UHBJaWBGpQMkgswZYx0Z-AmkAJBZ7YnUBMHFago70yVwq2FAxqGKCCpOu3p6wGaUPfJYkfKUtvg8gs3CcXeu5KtrTAnXK__he-EijiuAVEQOhUYmJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگه هنوز مجردی، این ویدیو رو ببین!
🔹
قانون تسهیل ازدواج جوانان، از مسکن و اشتغال تا معیشت رو هدف گرفته بود؛ اما بعد از دو دهه، هنوز روی کاغذه!
🔹
جزئیات را در این ویدیو ببینید.
#قانون_متروک
@Tv_Fori</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/698156" target="_blank">📅 20:10 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698155">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">25-2 Ane Manaee (1404-02-14)Shahre Moghadas Ghom</div>
  <div class="tg-doc-extra">@Aminikhaah</div>
</div>
<a href="https://t.me/akhbarefori/698155" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
تفسیر سوره محمد| جلسه بیست‌وپنجم؛ بخش دوم
🔹
انسانِ بی‌خدا خطرناک‌تر از درندگان! جنایات امروز رژیم صهیونیستی امتداد شرارت تاریخی فراعنه. [00:00]
🔹
شباهت وضعیت امروز با دوران حضرت نوح، انکار مردم نه از ضعف دلیل، که از نفرت نسبت به حق است. [05:10 ]
🔹
مظلومیت‌ها و فداکاری‌های اهل‌بیت برای هدایت بشر از ورطه جهالت به قله قرب الوهیت.  [11:38]
🔹
عظمت حضرت زهرا سلام‌الله‌علیها به‌ مثابه جداکننده نور از ظلمت و شافی مؤمنان از میان آتش. [20:35]
🔹
وسعت دعای اولیای الهی؛ وقتی یک نگاه، یک علاقهٔ درونی، یک نور اندک در دل، رشته‌ای می‌شود برای دستگیری [23:43]
🔹
فعال شدن رشته‌های پنهان دل در بزنگاه‌های سرنوشت‌ساز؛ از محبت حرّ به فاطمه زهرا سلام‌الله‌علیها تا کینه پنهان زبیر نسبت به امیرالمؤمنین علیه‌السلام! [29:05]
🔹
وقتی حب و بغض برای خدا نباشد، اعمال دینی پوششی می‌شوند برای شهوات و خودخواهی‌های پنهان. [34:29]
🔹
مقام خلیل الله یعنی رسیدن به نقطه‌ای که هیچ‌کس جز «خدا» در دل نباشد.  [38:08]
#تفسیر_سوره_محمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/698155" target="_blank">📅 20:08 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698154">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWSoEdQCCQhSvSDMvn6GDwfQczhWeKNh71ncd2vKacxryrO831_f3ZtIV9yROz_HgdO5kPlpYCVYxeI2pyn37WMPAWDLWWqH0rp7HKW0HU6kh1EH1eWvtLvFXTlwffEw4J4n_oq4XKD89gF6_PLcTvUb7YwBamKIsrXiQYBT9p_DBOoZEv3iDAm1FqQtCE9w17piasGarbj6XpbsAB4fI8CpBpuvQJuy2g3CNpUAF4nkM5bGGWwm3Eh1z2QRlKQHHWkZUtuTN8w6_JjAifMFAe-bbfCaOAuc-0Myx6ui0qdQ82Rf9CuYnPFLpruU8Hw-IQjD6bXUK06ty8xAAVLMyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بنادر راهبردی اسرائیل و ۵ کشور منطقه در بانک اهداف احتمالی ایران
رسانه جریان به نقل از منابع آگاه:
🔹
بر اساس اسناد و نقشه‌های منتشرشده از سناریوی پاسخ متقابل که توسط رسانه امنیتی جریان منتشر شده، فهرستی از مهم‌ترین بنادر راهبردی منطقه به‌عنوان اهداف احتمالی و اولویت‌دار واکنش موشکی معرفی شده است.
🔹
بر این اساس، در صورت هرگونه آسیب به زیرساخت‌های ایران، گلوگاه‌های اصلی تجارت دریایی، انتقال انرژی، جابه‌جایی کالا و پشتیبانی لجستیکی که ستون فقرات اقتصاد و زنجیره تأمین کشورهای منطقه را تشکیل می‌دهند، در بانک اهداف قرار خواهند گرفت.
🔹
این فهرست، بنادر راهبردی رژیم صهیونیستی و کشورهای عربستان سعودی، امارات متحده عربی، قطر، کویت و بحرین را در بر می‌گیرد. از جمله این مراکز می‌توان به بنادر ایلات، حیفا، اشدود و اشکلون در سرزمین‌های اشغالی، جده، ملک عبدالعزیز، ملک فهد و دمام در عربستان، جبل‌علی، خلیفه، فجیره و خورفکان در امارات، دوحه، حمد و رأس لفان در قطر، میناء الاحمدی و الشعیبه در کویت و بندر بحرین و خلیفه بن سلمان در بحرین اشاره کرد.
#ساعت_صفر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/698154" target="_blank">📅 20:06 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698153">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AEv-C0NR-v8p5o0VIkaC2dZIEPFIptYu_1Wbp1aO--OJ2Fa38scF6ffQZGo-DuLZJM3c_ppXtganfdtTXNEJs0ogpFjPBpJw1j6EMbwN3FerpmnSH6pfPR0iew6e1AmCCZEGcv-XaVpfaymtVB2NB4CH2VatObqYFeTieHoQ7idhLpc3U8HFxVZxww5id09O3VXOUgiyI762E8_Y7ZjCeBM4j8DEqJs5sUJ24vGIyz1pDpKnXjmH-tEWAVrR9bZe7-IwYQPj6OLIzOVz-iWqBgrmXBzYu2tdmhvbufA0bRIcN15DFmhXLhAtiDNwKiCWTgu4u-Jzdk0Y82Nlo8076w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مشاور سرمایه‌گذاری ترنج و بانک سامان، اولین صندوق درآمد‌ثابت ارزی بخش خصوصی را تاسیس می‌کنند
🔹
صندوق درآمد‌ثابت ارزی، امکان کسب بازدهی ارزی را فراهم می‌کند و ریسک تورم ارز مرجع را کاهش می‌دهد. مدیریت سرمایه‌گذاری صندوق با مشاور سرمایه‌گذاری ترنج و عملیات ارزی و ضامن نقدشوندگی آن بانک سامان است.
🔹
تجربه مشاور سرمایه‌گذاری ترنج با ۱۱ صندوق سرمایه‌گذاری  و ۱۲۵ همت منابع تحت مدیریت، در کنار بانک سامان به‌عنوان یکی از ۳ بانک برتر خدمات ارزی در کشور، پشتوانه شکل‌گیری این صندوق است.
@AkhbareFori</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/698153" target="_blank">📅 20:01 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698152">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
گردش ۵۴ هزار میلیارد تومانی پول در معاملات خورد بورس!
🔹
میانگین هفتگی ارزش معاملات خرد در هفته سوم مهر ۱۴۰۵ به ۵۴٬۱۶۴ میلیارد تومان رسید.
🔹
این رقم در مقیاس دلاری، مرز ۲۰۵ میلیون دلار را ثبت کرد.
🔹
در بازار امروز هم مجموعا مبلغ ۵۴۰۷ میلیارد تومان ورود حقیقی ثبت شد.
🔹
امروز ۷۹ درصد خریدها توسط حقیقی ها و ۲۱ درصد توسط حقوقی ها انجام شد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/698152" target="_blank">📅 19:59 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698151">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G5cDo8j6Pbmm1IwssvYlf4SlFU2LLZxoprEosQWz1onULHo9KTbu6SHxGQ4oWOOQazyzZYIMEbYviOMmGQT_OMyWly7XFlXdpaqQIt4QPDJLIAhGTC18KNwrXd17PH5a8gXyrH4U8awaeKjt6R_cNW_c6e9-AxVS-GwXZ0iqA1KT7DMPCpFW0BDa8aXjJFjLROehOS7o73EXjVcIgpvUarDBA0xF3BKWjDyYVk3GSReY1x-eQCOmEuELo9GENAuWO1vEu3cJyjPupfh5-DeXAFt88mBoQ4xBUBObEdWFb2SAowRkkpLZeAztlE6g0hmiwoQyPl59m_8Nx3tvCaVy_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پایان درگیری مسلحانه در کورین زاهدان با هلاکت ۵ تروریست
🔹
درگیری نیروهای حافظ امنیت با عناصر گروهک‌های تروریستی که از صبح امروز در منطقه کورین زاهدان آغاز شده بود، با کشته‌شدن ۵ تروریست و شهادت یک نیروی حافظ امنیت به پایان رسید.
🔹
این عملیات‌ها تا پاکسازی…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/698151" target="_blank">📅 19:55 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698150">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D4vV4_4VWv8DbdfSZ68_zcivpoFQdMRio7276qiYpktNHJAOwlfcoGcujB0JqkhYk2OSnUwfDt1QknybfZ5Y40rs8P4nlECoxBWfPPVvk7zHA00pAya0-luXYKD8IjyrZ_DmtvqOsrqtmQnsdieXCciB3iIrl0fSnOWV7_4BiKdCDgYnrHJ_mEsbRKFAP7ZOAOZiNv7H0D3REFtW4MkVtP5ZCSV8tCmG1EtG5xmMSXfioicSj6NHXTNIXmAqzzUsaqaJvm0wSZ6_XWFzOyZXDiRBWvZEkg1UFeinSaVf0T84uPILxta3pVFqDuYyM8h10YhhrL4jyGZr9YC0w0uALw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شکاف کالابرگ و هزینه معیشت | با کالابرگ جدید چه مقدار مواد غذایی می‌توان خرید؟
🔹
افزایش ۵۰۰ هزار تومانی اعتبار کالابرگ، اگرچه می‌تواند بخشی از فشار معیشتی خانوارهای مشمول را کاهش دهد، اما مقایسه این اعتبار با هزینه واقعی تهیه کالاهای اساسی نشان می‌دهد که فاصله میان حمایت دولتی و مخارج غذایی خانوارها همچنان قابل توجه است.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3252082</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/698150" target="_blank">📅 19:52 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698149">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4c8a0dfe6.mp4?token=uoptXi_Ds3iTPeqWe_WZTjdLO04HF9YCN-wjrP1qhsE0gzCyrfNmvvo8cZtgSJZc6ruimbj1OYiT0MyrB05iOODdwtvrM9YPopTGVg1Zw4LfkK5Uu0-AZN9rVLX87RtRXgMS-OTfla70mehhzpj1-yBvdkyUchK8TjRJkTHbc9OW8jleFRbsr-ZKm1ij5nH5vKejZgzJzpH1N_mhHN7y8KajG1HTDlcsl-KXYYh3GVFWoMq_-Z9WYjytTiQc2baT1tV57N41QN9tgZQB_OKBQG2Z3KfOcemzSZ2R4eznBJKyhUHp0J-XAzsb4J1SqhntQP6OPAMuSxeW6OX0CF10VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4c8a0dfe6.mp4?token=uoptXi_Ds3iTPeqWe_WZTjdLO04HF9YCN-wjrP1qhsE0gzCyrfNmvvo8cZtgSJZc6ruimbj1OYiT0MyrB05iOODdwtvrM9YPopTGVg1Zw4LfkK5Uu0-AZN9rVLX87RtRXgMS-OTfla70mehhzpj1-yBvdkyUchK8TjRJkTHbc9OW8jleFRbsr-ZKm1ij5nH5vKejZgzJzpH1N_mhHN7y8KajG1HTDlcsl-KXYYh3GVFWoMq_-Z9WYjytTiQc2baT1tV57N41QN9tgZQB_OKBQG2Z3KfOcemzSZ2R4eznBJKyhUHp0J-XAzsb4J1SqhntQP6OPAMuSxeW6OX0CF10VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حرکت یوگا برای افزایش تمرکز و کاهش پرش افکار؛ قبل از مطالعه ۲۰ بار انجامش دهید!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/698149" target="_blank">📅 19:48 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698148">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
لیبرمن: نتانیاهو پیش از انتخابات کنست به‌دنبال جنگ است
وزیر جنگ پیشین رژیم صهیونسیتی:
🔹
نتانیاهو برای اهداف سیاسی و پیش از انتخابات ۲۷ اکتبر، به‌دنبال ایجاد درگیری نظامی است؛ برخی اعضای حزب لیکود از او خواسته‌اند برای کنار رفتن نتانیاهو کمک کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/698148" target="_blank">📅 19:40 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698147">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
عضو کمیسیون امنیت ملی: برخی با طرح استیضاح عراقچی، به‌دنبال مطرح‌ کردن خود هستند
علی احمدی، عضو کمیسیون امنیت ملی مجلس در
#گفتگو
با خبرفوری:
🔹
استیضاح عراقچی به کمیسیون امنیت ملی ارجاع نشده و وزیر امور خارجه در جلسه کمیسیون توضیح داد که مذاکرات نیویورک با آمریکا خودسرانه نبوده و پیش از آن با دستگاه‌های ذی‌ربط هماهنگ شده بود، با این حال برخی افراد این موضوع را بیش از اندازه بزرگ کردند.
🔹
با توجه به توضیحات ارائه‌شده از سوی عراقچی و شرایط حساس فعلی کشور، بعید می‌دانم طرح استیضاح به مرحله اجرا برسد یا امضاهای لازم را جمع کند.
🔹
به نظر می‌رسد برخی افراد با طرح چنین موضوعاتی در فضای رسانه‌ای و تبلیغاتی، بیشتر به‌دنبال مطرح‌کردن خودشان هستند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/698147" target="_blank">📅 19:38 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698145">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
چه کسانی مشمول افزایش اعتبار کالابرگ می‌شوند؟  معاون وزیر کار:
🔹
افراد نیازمندِ خارج از پوشش کمیته امداد و بهزیستی، در صورت تأیید نیازمندی از سوی این نهادها، مشمول طرح می‌شوند.
🔹
افراد در صف حمایت، دریافت‌کنندگان کمک‌های موردی و خانوارهای فاقد خودرو و ملک…</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/698145" target="_blank">📅 19:30 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698144">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15e26fba09.mp4?token=RgV3rQVP8HufZkhwQZ15kaQLdmZU0I12ynNiRunUZot0uI3PqZAk4fURj1trB9AulXtctJeYFUA8a4kNmANOIBci8rlbjkM-FOj-nYRJAukP1AYJyswh-fzEK_arszivbD96CE9Mb2-pbX4dTeMC7o8X6ImJw2bzhxKuHqxcHt1t-yvcMzfN3AD9EV68Pu8c4v74UsTW0_Jv1ewN5tjUZYPcTkUmcxuInfapVeBZnNFmHd-OfskIXIk5oaMYWTcWhxUx_HJ-fWtvREK3Y_SxocUlDUoi3KH0VdFJPXDdwnK3CfrZRNFII2WAsbg2p3n6UKzxQgso88ZkVVaRAoOj_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15e26fba09.mp4?token=RgV3rQVP8HufZkhwQZ15kaQLdmZU0I12ynNiRunUZot0uI3PqZAk4fURj1trB9AulXtctJeYFUA8a4kNmANOIBci8rlbjkM-FOj-nYRJAukP1AYJyswh-fzEK_arszivbD96CE9Mb2-pbX4dTeMC7o8X6ImJw2bzhxKuHqxcHt1t-yvcMzfN3AD9EV68Pu8c4v74UsTW0_Jv1ewN5tjUZYPcTkUmcxuInfapVeBZnNFmHd-OfskIXIk5oaMYWTcWhxUx_HJ-fWtvREK3Y_SxocUlDUoi3KH0VdFJPXDdwnK3CfrZRNFII2WAsbg2p3n6UKzxQgso88ZkVVaRAoOj_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برای هر عضو بدن، چه نوشیدنی‌ای مفید است؟
🥤
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/698144" target="_blank">📅 19:26 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698143">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
ادعای الجزیره به نقل از یک مقام آمریکایی: پاسخ به حمله به یکی از کشتی‌هایمان را با ضربه به کشتی‌های ایرانی خواهیم داد
🔹
حملات ایران به کشتیرانی در تنگه هرمز را از نزدیک زیر نظر داریم.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/698143" target="_blank">📅 19:16 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698142">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
ادعاهای تکراری ترامپ: بسیار به‌زودی درباره ایران تصمیمی خواهیم گرفت
🔹
ایران یک کشور شکست‌خورده است؛ ما کنترل تنگه هرمز را در دست داریم
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/698142" target="_blank">📅 19:15 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698141">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ocJ2aeK57AijJt9eQlr01KJYjdwqJzLrQgZxUi_CCOW-vEX8_hKkqbyd9DBmJS97VLQHOUhgLthsqyU3D31p1q4ED8rAjD4IoH6dRXR89b4ZfaVWpLQ-dQGsWAClkL3V99rzWN3x2YTkj0NujpxxwpGV5_yeJc6RzNNx-BjeMdtSVd5zpz2okpL-mLLICc5-CisaaCBCeZbDwjiDjZmpY-wBiG7Kc8zwHLVTtbbzWpKwENBludZfuuBfH1ThHIqVFhALyUXy6dNegk64au7Q_zYCm1fXdR9NRKp-otNnc8GyWJvJIe70nIpoQBkG1VmiJ2nsd9HDha8lSKBkS4aocw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سفیر آمریکا در آستانه برکناری؛ اتهام رفتارهای نامناسب و تخلف!
🔹
ترامپ و روبیو در پی گزارش‌هایی درباره رفتارهای نامناسب، تهدید یک مقام یونانی و تلاش برای استفاده از نفوذ دولتی جهت پرداخت بدهی ۱۰۰ هزار دلاری سفیر آمریکا در یونان، در حال بررسی برکناری او هستند.…</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/698141" target="_blank">📅 19:13 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698140">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
ادعای ترامپ: حوثی‌ها خیلی بد رفتار می‌کنند و ممکن است از ترکیه بخواهم در یمن مداخله کند
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/698140" target="_blank">📅 19:10 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698139">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
چه کسانی مشمول افزایش اعتبار کالابرگ می‌شوند؟
معاون وزیر کار:
🔹
افراد نیازمندِ خارج از پوشش کمیته امداد و بهزیستی، در صورت تأیید نیازمندی از سوی این نهادها، مشمول طرح می‌شوند.
🔹
افراد در صف حمایت، دریافت‌کنندگان کمک‌های موردی و خانوارهای فاقد خودرو و ملک با درآمد کمتر از سقف تعیین‌شده نیز در این گروه قرار دارند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/698139" target="_blank">📅 19:04 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698138">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vB570cO2qCyY20xWyPTejvTgj2eH1dmaVy50QX86mBaJjS6xg_ZZmQYOhzq1JoUBE8TInUGHoZq85GIo8b3s8LmYSoYgMV9YFLLysio0BxYTR76MGRbJRAkdIA1mc_ygK86d04wm6Y1TfR3-ClsJ8OLVEXVLftYDdfomzK02HCOIB2bXNUOWkFSWaPddYszJ1MLpgozhV0QtSl9YD_LNoOh0gb1QThs8YDVQWOwH3FtGrs_wl11Ng0ph4uIWbgDAvM_aGoAcgyHpMqSYlmX04A2B1kJk-bEvzAQug4TQjW_XgLGNttafgkNMqsORgbRNEPbtd-2V50cfpM6B60wQXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آغوشی که جان یک نوزاد را نجات داد!
🔹
در سال ۱۹۹۵، وقتی پزشکان از نجات بریل، نوزاد نارس، ناامید شده بودند، پرستاری خواهر دوقلویش کایری را در همان انکوباتور کنار او گذاشت.
🔹
پس از چند دقیقه وضعیت بریل بهبود یافت و کایری دستش را دور خواهرش حلقه کرد؛ این اتفاق بعدها به‌عنوان روایتی الهام‌بخش از روش نگهداری مشترک دوقلوها نقل شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/698138" target="_blank">📅 18:59 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698137">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
هگزت قربانی ترامپ می‌شود!
دومینیک میشائیل تریپی، تحلیلگر سیاسی:
🔹
ترامپ قصد دارد پس از انتخابات میان‌دوره‌ای، وزیر جنگ را برکنار کند و مسئولیت جنگ نامحبوب با ایران را به او نسبت دهد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/698137" target="_blank">📅 18:53 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698135">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f3530e82a.mp4?token=fCDXzemOxg4a_yLvBHP4T--ziTHV82UJvWAPb47qYqjhZOiMHN8KBuw12lXomeCF7oNvWf7poVAVOJvyJUwmfAldvUFPv_TP8ettXf6i0IVDBSwEdU9Ahg2geOTvGqebA-bkMOCaFdHy8QyrKLeVUOJm8CyEWnT9aohMdtdDg5nhd0FWcwbEpyRIT3x65S-3C7fCfrBBwZi0AoVV_MSQzPDTZcEK-JesOXJJxRztEz6FTgctwPrjO96HaRUEhPeUg9weEiesUyOiPzw5eZf7fGuDILtArKpmhsp5aYDyQO0HOQAPeILAjM7HwVYOaTvaGWy-9JOyu0xHdwEr5ovUWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f3530e82a.mp4?token=fCDXzemOxg4a_yLvBHP4T--ziTHV82UJvWAPb47qYqjhZOiMHN8KBuw12lXomeCF7oNvWf7poVAVOJvyJUwmfAldvUFPv_TP8ettXf6i0IVDBSwEdU9Ahg2geOTvGqebA-bkMOCaFdHy8QyrKLeVUOJm8CyEWnT9aohMdtdDg5nhd0FWcwbEpyRIT3x65S-3C7fCfrBBwZi0AoVV_MSQzPDTZcEK-JesOXJJxRztEz6FTgctwPrjO96HaRUEhPeUg9weEiesUyOiPzw5eZf7fGuDILtArKpmhsp5aYDyQO0HOQAPeILAjM7HwVYOaTvaGWy-9JOyu0xHdwEr5ovUWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
می‌دونستی آمریکایی‌ها به دلار نمی‌گن دلار؛ پس چی می‌گن؟ #زبان_فوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/698135" target="_blank">📅 18:49 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698134">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
عضو کمیسیون بودجه: محاسبات، تورمی بالاتر از ۴۰ درصد را نشان می‌دهد
بیت‌اله عبداللهی، عضو کمیسیون برنامه و بودجه در
#گفتگو
با خبرفوری:
🔹
افزایش اعتبار کالابرگ می‌تواند بخشی از فشار اقتصادی خانوارها را کاهش دهد، اما در شرایط تورمی، افزایش مبلغ آن لزوما به بهبود  قدرت خرید مردم منجر نمی‌شود.
🔹
برای اثربخشی بیشتر حمایت‌های معیشتی، دولت باید در کنار افزایش اعتبار کالابرگ، کنترل تورم و سامان‌دهی وضعیت تولید و اقتصاد را نیز در دستور کار قرار دهد.
🔹
تورم ۴۰ درصد اعلام شده، اما باتوجه به محاسبات، بالای ۴۰ درصد است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/698134" target="_blank">📅 18:42 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698133">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f241bb3668.mp4?token=W7YH-BNJ8ZRbkmuBdZ21S1T8NjOUqsWgGvnMbo-_vZkyDn9VBxiYPcZlz0OLsO2_iQ17rL_GS5W02ldD6ASkoOpYCnHmweJ3GcqTwZG6xQmb6LyLCxXNn3fLvBll09YUYbiz1ZGJSrsGhUMmrQnHGJAzVPLKIKQidq6XAG0k-uW77JE_OflLMgkqy--FIvTtOFVVzKr9ryNcY3c9pHGd9fVfG0vF_N2pUy3h2wRrdfZVOaSVIgT62S2rMKJ2elsNEraPzntGN_PC_aZJYkJjUIzBZfUnWQkkYV6Eq9nm23FSOG7P5AuK8cY6oHQPxSvYETw2LRRyeU2E2ik3k_8_AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f241bb3668.mp4?token=W7YH-BNJ8ZRbkmuBdZ21S1T8NjOUqsWgGvnMbo-_vZkyDn9VBxiYPcZlz0OLsO2_iQ17rL_GS5W02ldD6ASkoOpYCnHmweJ3GcqTwZG6xQmb6LyLCxXNn3fLvBll09YUYbiz1ZGJSrsGhUMmrQnHGJAzVPLKIKQidq6XAG0k-uW77JE_OflLMgkqy--FIvTtOFVVzKr9ryNcY3c9pHGd9fVfG0vF_N2pUy3h2wRrdfZVOaSVIgT62S2rMKJ2elsNEraPzntGN_PC_aZJYkJjUIzBZfUnWQkkYV6Eq9nm23FSOG7P5AuK8cY6oHQPxSvYETw2LRRyeU2E2ik3k_8_AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کمبود سوخت در جزیره بالی اندونزی؛ صف‌های طولانی مقابل جایگاه‌های سوخت‌گیری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/698133" target="_blank">📅 18:37 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698132">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
معاملات شبانه تتر متوقف شد
🔹
صرافی های رمز ارز معاملات تتر را از ساعت ۲۱ هر شب تا ۹ صبح روز بعد متوقف کردند./ تسنیم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/698132" target="_blank">📅 18:34 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698131">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d60bae218.mp4?token=XNbh61KloVJKDpGZD6ixWmyKeqs1NyY6bJIO7sjSiQf7yIwXrb92-VCLqr4Pt790QILC3f6HO2KQdAlcNUxwBu9waQUR4Qv695NQYiE-Bok-4u7zH2ktbn-KKe54CWMhafA78v6frO2VzWEzaVsFKPaVoFts735qf4Qs7WbSwzORkeHOJ9Tq-S67iddPRSIzX55YujTuFT57Vz_-g9HfK4k3JW59bpbpoVw87eVReCATNCSWH6zZh0ilbuVvmqDSMejbZrWQszM1QY3FBwvYo-jlXuei81xgyFBZD37A4BpiMXKGtmAV7hmX8AZBSUldmaHsgrJPsPvmvN8cWiDONA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d60bae218.mp4?token=XNbh61KloVJKDpGZD6ixWmyKeqs1NyY6bJIO7sjSiQf7yIwXrb92-VCLqr4Pt790QILC3f6HO2KQdAlcNUxwBu9waQUR4Qv695NQYiE-Bok-4u7zH2ktbn-KKe54CWMhafA78v6frO2VzWEzaVsFKPaVoFts735qf4Qs7WbSwzORkeHOJ9Tq-S67iddPRSIzX55YujTuFT57Vz_-g9HfK4k3JW59bpbpoVw87eVReCATNCSWH6zZh0ilbuVvmqDSMejbZrWQszM1QY3FBwvYo-jlXuei81xgyFBZD37A4BpiMXKGtmAV7hmX8AZBSUldmaHsgrJPsPvmvN8cWiDONA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۴ کد مخفی موبایل رو که هر کسی باید بدونه
📱
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/698131" target="_blank">📅 18:28 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698130">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cd2e3d250.mp4?token=Uxlmbvw-TEnGh4KVIi1S0TTkVVRFluY11w9L1C9wB3mMSUHk7Lgw2ToAOyufnp4StkE5EoVB_Ry9nPtyaKh9BpX7ZT4p3yXRDd2bbgk-n5mYec123s0w10x2swXcLZWSY5MnUX9wsdxoewDXRZKcnhy6WZFkij4GGNL-N6OhlaR78EmFzR6yiGHHR6YKwrByWoChE1oj2LbeEAty3J5RZB3YEOWXH9AGCR_G6rCmlohofcFQRWoQDdf8Q26vr89YjGclbSNGLM2uAF35XJi9gYVteMGoBlaiVGbzD-_CSDiWL4Fgr84GfY2Wc7s90wgbgP37x3alGPSbT3QxOQ-iUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cd2e3d250.mp4?token=Uxlmbvw-TEnGh4KVIi1S0TTkVVRFluY11w9L1C9wB3mMSUHk7Lgw2ToAOyufnp4StkE5EoVB_Ry9nPtyaKh9BpX7ZT4p3yXRDd2bbgk-n5mYec123s0w10x2swXcLZWSY5MnUX9wsdxoewDXRZKcnhy6WZFkij4GGNL-N6OhlaR78EmFzR6yiGHHR6YKwrByWoChE1oj2LbeEAty3J5RZB3YEOWXH9AGCR_G6rCmlohofcFQRWoQDdf8Q26vr89YjGclbSNGLM2uAF35XJi9gYVteMGoBlaiVGbzD-_CSDiWL4Fgr84GfY2Wc7s90wgbgP37x3alGPSbT3QxOQ-iUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترسناک‌ترین جاده ایران
🔹
اینجا یکی از ترسناک‌ترین جاده‌های ایران است؛ جاده‌ای که وسط کویر لوت کشیده شده!
😳
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/698130" target="_blank">📅 18:15 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698129">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
اسقاط خودروهای فرسوده نزدیک ۳ برابر شد
محمدصادق حاتمی، مدیر ستاد نوسازی و اسقاط ناوگان در
#گفتگو
با خبرفوری:
🔹
در مردادماه حدود ۱۱ هزار و در شهریورماه ۲۸ هزار دستگاه خودرو اسقاط شد، به‌طوری‌ که آمار شهریورماه با وجود کاهش بیش از ۳۶ درصدی تولید خودرو رکورد ۲۰ ماه گذشته را ثبت کرد.
🔹
در صورت تداوم روند فعلی، امکان اسقاط بیش از ۲۵۰ هزار دستگاه در سال جاری وجود دارد، با تولید و عرضه سالانه حداقل یک میلیون و ۷۰۰ هزار دستگاه خودرو و موتورسیکلت، می‌توان به تحقق هدف اسقاط ۵۰۰ هزار دستگاه در سال آینده امیدوار بود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/698129" target="_blank">📅 18:07 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698128">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
براساس اعلام منابع عربی فردی مسلح به فرودگاه رامون اسرائیل یورش برد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/698128" target="_blank">📅 18:06 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698127">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62841d418b.mp4?token=VnNW3H-hQMRm995roulSbc-orN7VMf_4aZ-jnX8WxZBdlIx1bfdhAO_XlHxuCxNatxqT4xsDyqoRbmL5LDkf2lcUoThyAE1s7tF5m8-A0Hi48Ni9hjjh1tykJaJy_He7f-1VTOI6vMvE-r5oz28ow8ftVF-l_VddS8AOMStkOHaNliaXuFmTpb7MVFwLtc8DO4DD7_OgqwXecXDjGS11EdKC1Cg0pZMvf5UNwCSJsBQ9fV4ym-hRYA-ALf7l38UP0Kpl4_OWafG2DZgg4rCgz5TA8osD8zTKCWDzTgMt9RO8et-rPqNbRC3lMbIR_vxLtr82QMNcABh2ZzPSMBaBkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62841d418b.mp4?token=VnNW3H-hQMRm995roulSbc-orN7VMf_4aZ-jnX8WxZBdlIx1bfdhAO_XlHxuCxNatxqT4xsDyqoRbmL5LDkf2lcUoThyAE1s7tF5m8-A0Hi48Ni9hjjh1tykJaJy_He7f-1VTOI6vMvE-r5oz28ow8ftVF-l_VddS8AOMStkOHaNliaXuFmTpb7MVFwLtc8DO4DD7_OgqwXecXDjGS11EdKC1Cg0pZMvf5UNwCSJsBQ9fV4ym-hRYA-ALf7l38UP0Kpl4_OWafG2DZgg4rCgz5TA8osD8zTKCWDzTgMt9RO8et-rPqNbRC3lMbIR_vxLtr82QMNcABh2ZzPSMBaBkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگه کنجکاوید بدونید مدادرنگی در کارخونه چطوری تولید میشه
✏️
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/698127" target="_blank">📅 18:05 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698126">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RYBf-EAFx-hF_DDPyYRZNQMKaWSBEAFqa_-4OpgbWyGK-diYWrYwPFz9PVYPXlmm_Fw9SiOm-llNwDobekcC1HEe2qw9w-mToLbxAJsrOHNz5v8UWY463Ti8WyWJnQDeFuczRLJTt26EU3eX3esE3xLsxzOc2Oc5jb4GCJXbj0guoADdQEv1zeo1zeWlmIxSOFbFXG3gXauqH2APbmieVW3jUjp82IVWk1hCfZ1OqRplfgG9fvGsWW99IYshtxhv-SpiLiVgF92x7tcJkiXG3m6ZZ64-iM8Dmasizpfi9EQduWT-XdksNseyY4Hy0OUDfuZzLD3-K1ope2U5akrOxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔷
ساده‌ترین راه اتصال فروشگاهت به اسنپ!
📱
با خرید کارتخوان هوشمند اسنپ در ۴ قسط، فروشت رو بیشتر کن!
🧮
سوپرپوز اسنپ‌بارکد یه کارتخوان اندروید همه‌کاره‌ست که تمام قابلیت‌های یه صندوق فروشگاهی رو هم داره؛ به‌علاوه این موارد:
🔹
پرداخت اعتباری با اسنپ‌پی و تارا
🔹
اتصال به اسنپ‌باکس برای ارسال سفارش
🔹
باشگاه مشتریان و ذخیره شماره و آدرس مشتری
🔻
دریافت مشاوره رایگان و خرید در ۴ قسط:
https://forms.gle/77f3J2oCbVsDkdqi7</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/698126" target="_blank">📅 18:02 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698125">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c128d83f9a.mp4?token=BLN2KC_OHyBBmhSx4hWumXEa39yeztrLcdPAXpuVMCYvkXXeuAOlQeLZAr6eqdoand7a8i18DAvSoci-LzOBQcvKLTuQ23_Nbx1ZLKKMrum6L65syitY4rFxhZBuAFyA1laRNUBDWg9VNthsQG9B-y09CkN2ckTEFW7baFvZzSUjwL3u_qP3FtKixWP2uGuJ_3xnHNvmckhZaAf-ls0rxZUvM2SGmqr7EwZKPsV2xpadXuHAaY72PAywhyMIIJ5JZDhP990hczj6CUCzzNE0MyLamsSaCfD0c5_-YKfUHsENHcVRxPg5L6SG4eV_aIfgMc6ItfKZAqVfhUZQSWnpNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c128d83f9a.mp4?token=BLN2KC_OHyBBmhSx4hWumXEa39yeztrLcdPAXpuVMCYvkXXeuAOlQeLZAr6eqdoand7a8i18DAvSoci-LzOBQcvKLTuQ23_Nbx1ZLKKMrum6L65syitY4rFxhZBuAFyA1laRNUBDWg9VNthsQG9B-y09CkN2ckTEFW7baFvZzSUjwL3u_qP3FtKixWP2uGuJ_3xnHNvmckhZaAf-ls0rxZUvM2SGmqr7EwZKPsV2xpadXuHAaY72PAywhyMIIJ5JZDhP990hczj6CUCzzNE0MyLamsSaCfD0c5_-YKfUHsENHcVRxPg5L6SG4eV_aIfgMc6ItfKZAqVfhUZQSWnpNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">درمان ریزش مو در کوتاهترین زمان
کشف شرکت دانش بنیان ایرانی در آنتن زنده شبکه ســـه ســیــمــا!!
😳
😳
ویدیو داخل لینک را حتما مشاهده کنید تا با تاثیرات عجیب این روش درمانی آشنا شوید
👨‍⚕
👨🏻
✨
🩺
بـیـش از ۳۰هـــزار خـانم و آقـا از این روش معجزه‌_آسا نتیجـه گرفتن
😍
روی لینک زیر کلیک کنید
😃
👇
https://www.20landing.com/214/2623
https://www.20landing.com/214/2623</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/698125" target="_blank">📅 18:00 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698124">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iin1VzJL2OW51EoJPpTGzvn8yK5lBM6LNMEkuHTcpSmtdGyo98MGrJBtMh69TvFaIMm_5LAJzhnAbo9ube976CtgznM-Mr8NZOFTJN6cTr-URnvjCbaBphqqAbFwo4_eHOmT6LRndov8YyMfvwS0Nxi4ni7EH7cXbzbcf63BIsJEFmHkuXLV_U6przZCqaj_fNgJvGJ9Pi-fFjvNi687WsAVYxuFtWoWW6s6IM-_5K7kWORsJFPyekW5nnGwiAtvcU_uXyUGXEqSZreithdsPwa0iTXW6udV77evuPDyafwteDPlegxXzorpnv7EXbk5WupHlWJwNBmeveHgTqdurQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نفت ایران بیش از ۲۴ دلار گران شد
🔹
جدیدترین آمار دبیرخانه سازمان کشورهای صادرکننده نفت خام نشان می‌دهد که نفت سنگین ایران در سپتامبر (شهریور ماه) ۱۰۵.۸۴ دلار به ازای هر بشکه فروخته شده است.
🔹
این رقم نسبت به ماه پیش از آن یعنی آگوست ۲۴.۵۹ دلار گران‌تر شده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/698124" target="_blank">📅 17:49 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698123">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
یحیی سریع: شرکت نفتِ منطقه صباحۀ صنعا از فرآورده‌های نفتی خالی است و هدف‌قرار‌دادن آن هیچ ارزش نظامی نداشت، ولی ما به زودی پاسخ این تجاوز را خواهیم داد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/698123" target="_blank">📅 17:44 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698122">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e1741c1e7.mp4?token=QH5hJU4gdeflFNoM0Hk5qZWmDDhi4-vebsoYJ8FSg9sP0bDl4h1hdz7gtkH9TBTNSye9EATLVw4s72CyHm7uIB9R02mDyrKJMLC33Ic2LfH2VF6JT_-kGGfMJjNKBlCSLRoizyavh5kIVoHsFL6aOzbCAnax63KZ6UWF548dLTpDiywyr_UwKa_Fpv6V5hPIuLOIYBLZwek0RvhuGk-XTen9iOJV6Aopd-yoByOcpY7iw8cFNvPWrh8GPBjcFMP8gfRvdpDI6vn0kPVls7sY0vqaGFmx293o_ZPfPwRNnoYWtFpr_zKcQsAFri1yKLh8shK93VJQcEf1NT9kwimgRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e1741c1e7.mp4?token=QH5hJU4gdeflFNoM0Hk5qZWmDDhi4-vebsoYJ8FSg9sP0bDl4h1hdz7gtkH9TBTNSye9EATLVw4s72CyHm7uIB9R02mDyrKJMLC33Ic2LfH2VF6JT_-kGGfMJjNKBlCSLRoizyavh5kIVoHsFL6aOzbCAnax63KZ6UWF548dLTpDiywyr_UwKa_Fpv6V5hPIuLOIYBLZwek0RvhuGk-XTen9iOJV6Aopd-yoByOcpY7iw8cFNvPWrh8GPBjcFMP8gfRvdpDI6vn0kPVls7sY0vqaGFmx293o_ZPfPwRNnoYWtFpr_zKcQsAFri1yKLh8shK93VJQcEf1NT9kwimgRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اولین حضور سخنگوی جدید کاخ سفید با ادعای کذب   کیتی زکریا:
🔹
ترامپ به هر وعده‌ای عمل می‌کند.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/698122" target="_blank">📅 17:44 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698121">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
جنگنده‌های سعودی تأسیسات شرکت نفت در غرب صنعا را بمباران کردند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/698121" target="_blank">📅 17:43 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698120">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
جنگنده‌های سعودی تأسیسات شرکت نفت در غرب صنعا را بمباران کردند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/698120" target="_blank">📅 17:42 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698119">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f213ecfac.mp4?token=LIthTF2kx4nWl6hyL56W2m8LshxHWQg0ATFcsE7ISVkpkZli71sblzGUV-RPh6eYEqYO5s_8S-xbgC66DmUShmxfVxXlzIF2ZaeEYuYzhnRf6cchMVAHLol0oxAJdOaAmD-VzGMMZop0DquNEWRld3cvgub150mbGkO-lCEqHWTfl9i8rf7gCSabR_r6F_DnPKNR2Zg3URg7mrppx7zO2mCOzz4QACi9HPDO6E5FnbFS27ZDkbln1A3RKL_7-AcdLkbPUCXgEdkVcJTrdjLJ6SmsbcnMKN1eCQsKT5bvMrM0HGILaGbVbcnn4Rm5KdGAqenRwpC2L5jy8-aQ-ToTEWAx6I6X9WLx_wEiYbazKhllyEOtd_0FFVhGsxD-WOa2Sri8Lql6r_DaQW8URBeI-QTbI32IgAxQxGpHn-cZIJFX5IO3fvKaIPPt-QQJHsC2GF2HPugq0uLSprCwWUeR5Mpxqyu-kU0khh0fbPpaZ83mWD1jMuUzw6jSn48ODjJmrez_D_SLar9NdvwAJQTmlN5J_QUimjAVoDwwulovDFxQN7DFQ2njmN-__DEVCsUIJW98woz7s-t84MLoBsNdA-EZcqJ2Cr9zRKenB97QZ9gP1GT8a_BLeTf5W7cRdOzMjU0cLOWBvCjk6r7t1_9tURwoxGDFh-_BgvczyR6tbbU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f213ecfac.mp4?token=LIthTF2kx4nWl6hyL56W2m8LshxHWQg0ATFcsE7ISVkpkZli71sblzGUV-RPh6eYEqYO5s_8S-xbgC66DmUShmxfVxXlzIF2ZaeEYuYzhnRf6cchMVAHLol0oxAJdOaAmD-VzGMMZop0DquNEWRld3cvgub150mbGkO-lCEqHWTfl9i8rf7gCSabR_r6F_DnPKNR2Zg3URg7mrppx7zO2mCOzz4QACi9HPDO6E5FnbFS27ZDkbln1A3RKL_7-AcdLkbPUCXgEdkVcJTrdjLJ6SmsbcnMKN1eCQsKT5bvMrM0HGILaGbVbcnn4Rm5KdGAqenRwpC2L5jy8-aQ-ToTEWAx6I6X9WLx_wEiYbazKhllyEOtd_0FFVhGsxD-WOa2Sri8Lql6r_DaQW8URBeI-QTbI32IgAxQxGpHn-cZIJFX5IO3fvKaIPPt-QQJHsC2GF2HPugq0uLSprCwWUeR5Mpxqyu-kU0khh0fbPpaZ83mWD1jMuUzw6jSn48ODjJmrez_D_SLar9NdvwAJQTmlN5J_QUimjAVoDwwulovDFxQN7DFQ2njmN-__DEVCsUIJW98woz7s-t84MLoBsNdA-EZcqJ2Cr9zRKenB97QZ9gP1GT8a_BLeTf5W7cRdOzMjU0cLOWBvCjk6r7t1_9tURwoxGDFh-_BgvczyR6tbbU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گاومیش‌کش‌های دیروز، مدعیان تمدن امروز
🔹
وقتی بهانه‌های جنگ بر سر مسائل هسته‌ای و تنگه‌هرمز رنگ می‌‌بازه و پای یکی از مهم‌ترین دلایل جنگ آمریکا و اسرائیل علیه ایران وسط میاد...
🔹
جزئیات را در این ویدئو ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/698119" target="_blank">📅 17:35 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698118">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
تصاویر تازه از نفتکش متخلفی که ظهر امروز با خاموش کردن سامانه‌های ردیابی و تلاش برای عبور از منطقه ممنوعه در حال عبور از محدوده شرق تنگه هرمز دچار آسیب و حریق شده بود
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/698118" target="_blank">📅 17:33 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698117">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/963d57b160.mp4?token=BM_lCCgloVz8hs9HFID5LBLWeivACbTAOdgM7BhnJOGWX43G91VQTdHIk0akvL0NI81uxiSX4lwGMB8m4jMMkmd1hy62OFA-QnQRuoOaMRIcU_t3XFE4JzfHs1WQ2nSRejYG3skPXBebTK7VHmRZg_5QC1DSAyGxB7Y6HE0yzHMgdg5ShvejvSPLzeJhEmhDN9IftNzU8YFcmud8ynVARsQJyX2mTEopCRMnP4tyE5XPpTz9E0mXxEUNDI8n_3XB-LodqYaKDUHj6FP7FlDd3Ou4qtNEF9_Ih3XSbNAJXpRu6iM4U_j6gKf0kE3bTpk3hmp8kJ9HLkyKbQ6FeVqxqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/963d57b160.mp4?token=BM_lCCgloVz8hs9HFID5LBLWeivACbTAOdgM7BhnJOGWX43G91VQTdHIk0akvL0NI81uxiSX4lwGMB8m4jMMkmd1hy62OFA-QnQRuoOaMRIcU_t3XFE4JzfHs1WQ2nSRejYG3skPXBebTK7VHmRZg_5QC1DSAyGxB7Y6HE0yzHMgdg5ShvejvSPLzeJhEmhDN9IftNzU8YFcmud8ynVARsQJyX2mTEopCRMnP4tyE5XPpTz9E0mXxEUNDI8n_3XB-LodqYaKDUHj6FP7FlDd3Ou4qtNEF9_Ih3XSbNAJXpRu6iM4U_j6gKf0kE3bTpk3hmp8kJ9HLkyKbQ6FeVqxqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این دمپایی‌های متفاوت، بیشتر عجیب‌اند یا خلاقانه؟
🦶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/698117" target="_blank">📅 17:33 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698116">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
معاون وزارت رفاه: حذف پردرآمدها از کالابرگ جزو طرح کلان دولت هست و مقداری هم به تاخیر افتاده/ پردرآمدها حذف می‌شوند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/698116" target="_blank">📅 17:31 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698115">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c88aed7af1.mp4?token=vp_ymbRZkuJP3hc9nXywCUhyKMq-zA5JxQpssr1wv-a35WDUVqZ2DX6ErcE-9exsg8dDgwt6mKDlOzrpEK-rLF4ASy_UcvlwpTy-SfDMJ0SN1gX8u1yGxi6QCqsFY8VbdPCFvWHWLnu1KQ4cxNMIfDoFgomrC6FFlGYt4cul9a2Gh7UtTFVV_lVdRHxMmZ1ZSXGsR7wUXnxqMoIWvd-sTsL8bprEL0-k5QKZgkTtBJidpbzdU5cAr63Ucsskcq03vxiSq3IBbR61pVLH20tJwsEbmdqn4XWYYZ4rO2tNJbfiv0MThK2EO5HQX481G-9GuIpWY0TtvraD-NEBkC9tvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c88aed7af1.mp4?token=vp_ymbRZkuJP3hc9nXywCUhyKMq-zA5JxQpssr1wv-a35WDUVqZ2DX6ErcE-9exsg8dDgwt6mKDlOzrpEK-rLF4ASy_UcvlwpTy-SfDMJ0SN1gX8u1yGxi6QCqsFY8VbdPCFvWHWLnu1KQ4cxNMIfDoFgomrC6FFlGYt4cul9a2Gh7UtTFVV_lVdRHxMmZ1ZSXGsR7wUXnxqMoIWvd-sTsL8bprEL0-k5QKZgkTtBJidpbzdU5cAr63Ucsskcq03vxiSq3IBbR61pVLH20tJwsEbmdqn4XWYYZ4rO2tNJbfiv0MThK2EO5HQX481G-9GuIpWY0TtvraD-NEBkC9tvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اولین حضور سخنگوی جدید کاخ سفید با ادعای کذب
کیتی زکریا:
🔹
ترامپ به هر وعده‌ای عمل می‌کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/698115" target="_blank">📅 17:29 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698114">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفروشگاه قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gXNwyOdO8XDhdJqfh-X_XxPPOWWdbk7yj1Q77WTYSsxDHjZTbzlppD1fGVKQt46s_lY6MgDC4lKRC3-vxW4Z3Lso7iin5Ss3QWAgncPjscaCaVH1yywEfslaArGVgRZg8AcTghiFjmqKynzn55HotOotKIIU9nOf6N9ikuemBXqbYYNioBUP7tKRBpS7im1T3GQSmiRCgqeLfFPEp81VH0708MNiJSuCPnBFeKG1FEvVQ16HI1km-0ut1Jwx-p1i8P2zXLvyMYaRu2xoYi_A1m9KfTW-FYC8SV5iZw2fkZUz42D7X_Zk07XGIIAd40ZKoJlnvM02MZOGILt670shRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕊
چفیه مدافعان نخی
نمادی از غیرت و استقامت که یادآورِ روزهای سخت و ایستادگی‌های حماسی است.
این چفیه با بافت نخی و سبک خود، همراهی لطیف برای روزهای جهاد و بندگی است.
✨
مشخصات محصول:
▫️
جنس: نخ باکیفیت و تنفس‌پذیر
▫️
ویژگی‌ها: بافت نرم، سبک و بادوام
▫️
کاربرد: مناسب استفاده در مراسم‌های مذهبی، پیاده‌روی‌های اربعین و استفاده روزمره
💰
قیمت:
رنگ سفید: ۲۳۹ هزارتومان
رنگ مشکی: ۲۳۹ هزار تومان
⏳
موجودی محدود؛ برای ثبت سفارش، همین حالا اقدام کنید.
📩
سفارش:
@gharar_order
🤍
هر خرید از «قرار»، سهمی در مسیر خیر.
@ghararshop</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/698114" target="_blank">📅 17:28 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698113">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iO6uPkw4mn2xuwZ7GbrwQfTb9BqHiAaWakg908fBrueDq_I6uTbMc_OxDeOKUWW2ZNPt42It3MFW6Ds0GkehbTOeZOfDxhmx5qoHFHMPwOCwRm7eRDZtzJBS2qX8SLLHliFLuP_d_66QDy33Q0uYMIV4aIWeS9wuUbVdfVPb9PPm_-vT9x-HecQs0oJfSNBtIj_VVBaTrXvZpd3mTecZ2E0vQvul10b94EZ_c_Gpip-3wOazPtkDgVymXwMLpYlP_N48qGSUhShiYSQAxgN_igchMHLzFHueUBNeU_N8f6LpZvwo4X02VNE-sZ1TplGNqEPqhUSSQ1f_xZPbqjLytw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصاویری منتشر شده از لحظه حمله یمن به فرودگاه بین‌المللی ملک خالد در ریاض
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/698113" target="_blank">📅 17:28 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698112">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
تلگراف در انتقاد از دولت انگلیس: لندن تا آستانه اخراج ۲۴ دیپلمات اسرائیلی پیش رفت، اما از ترس اقدام متقابل تهران، حتی یک دیپلمات ایرانی را اخراج نکرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/698112" target="_blank">📅 17:24 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698111">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
عقب‌نشینی دلار از ۲۷۴ به ۲۵۷ هزار تومان/ رویای فروپاشی اقتصاد ایران چطور نقش بر آب شد؟
🔹
در روزهای گذشته قیمت دلار که تا سقف حدود ۲۷۴ هزار تومان افزایش یافته بود با مداخله بانک مرکزی به حدود ۲۵۷ هزار تومان رسید، کاهشی که توجه فعالان بازار ارز را به خود جلب کرده‌است.
🔹
این اتفاق در شرایطی رخ می‌دهد که وزیر خزانه‌داری آمریکا پیش‌تر از فروپاشی اقتصاد ایران ظرف دو هفته سخن گفته بود.
🔹
حالا با گذشت چند روز از گذشت ضرب‌الاجل مطرح‌شده کاهش قیمت دلار نشان می‌دهد که رویای فروپاشی اقتصاد ایران مثل تمام پیش‌بینی‌های قبلی آمریکایی‌ها در مورد ایران با شکست مواجه شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/698111" target="_blank">📅 17:22 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698109">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z9R2PnvZyA9uPwK7k1R_fYY3WJGTciUNHQMOHFNI_5V6ScM4TgZaZTLGRMAXqepkAF2lmOS517f9Z-dMd5m8tyz7Cc8GFGo9jtD04KFW2nJYR2KQqYKU5LfcQWu6Fe8ajWRKDQbBvp9cD1F-G1Q4DIIEA9Ep0q_qqIVGNQMwAE5VTCtBLxnYae-VNGDqOZVQsDQVMSPxq1nJF6EhNNxrGfu87VgDlSp9bib2VLZ3bH9bPf3SQxBdlIvF3Ml-wMDYFfHte0SRtzoHkdg8fgpJpP0HT2P8fswMwyhTdm92CjG9Q5MCu3D00hWATknZQbWrfOzk_aUk6WTrvtoruibvTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر عضو بدن برای سالم موندن به مواد مغذی خاصی نیاز داره!
💊
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/698109" target="_blank">📅 17:14 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698108">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gtcEhVInlq0vs4UBkR2tuRmffkAg4BehVFL1-SblnTacXtXCiXe8JZ3dWtHUXXpu8gdNYzHOTt5eb8OTDQ3KRg9JsCWgevS0W27R8tAEUAlU4_o9AfJxI8JRoJ5DOxmyypNxxSgnrA7IJX2R7sw9uNZi8lbxLj3LqB1cyFDFu5AvIKxlPo2frQyNY6UyOxRUVuLcWTx_NNdLyu0bI9dbjcrZQEzfLD36fPaQZg-3z9DzBMif7DUiD7fbqptKuTsK83ouGW1joPynCrjqCzei6ar3SB0OkXBjTA_yDx0BJUXrq3qprlrgpMPUrJCkGyVdaFrD5Y33P0Yf76a1aVxcWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
فریاد دادخواهی صباغیان
از بی عدالتی در حوزه‌های انتخابیه کشور و
استمداد از رهبری
🚨
متن کامل نطق محمدرضا صباغیان نماینده حوزه انتخابیه مهریز در مجلس:
📎
جهت مشاهده بر بروی لینک کلیک کنید
1405/07/14
🌿
کانال رسمی محمدرضا صباغیان جهت پیوستن کلیک کنید
🌿
🇮🇷
@mr_sabbaghian</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/698108" target="_blank">📅 17:13 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698105">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xj1vp4IDaGJdjtagDmjix6FbMXPtdtb1oMBPrVi-gAZUWxwvxp2suSQG2btqATVZ53OzT1LL3gI4QYTiJNieqnR5AZW-4_yOxVI90qdrWsrMCjeYT7Ew5KD_8Je4tcVuipG8LA5bObThewofyITKFkwMT8cTnCPUSAdI31v1mQFAI8Z3zxGzj3kW74El1t0ocRSCYBr-e8SS-m6Pd1MM0H6vtfqNb963iV-5M6lo6MUmVoYB7cEvq9YzmFg4dsyGpf1QdEBkb6lj-nchUUi9nA42eRA8vJVQAEkL0BXlTCoQ3ltjtHndI1EEgTfcfB5ca8nLYKI7Vf_tY_wSZ82LGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YeDt6yj6V51qMQFuBsfsGWaIPAwW5-BYpOm5Di9wLpy4YmqeqBJIls8-SBjdW-SvqMk5UOKdfoWE5VzsxqZjx44XHcapUwDdA_BFB_j8EKxi-oueMjBDotignTvYNucUee1vCbV5uHuCdtdcYww_t1wnr0DLpVRDyhlWoqzI9LT7XnoSDd244JKZ21yBcQLDV_GN707_VlPn9RIJUBc4nOi9GhLMccHhGjRMVqnZMc7ti3RR85ZP7JLLUacMmwlK4AfnSUGTSGhQ5l6kO-bfv-vqrhY2erVdp6ZiQa4xE7SdpCD-FmLbc2_vh8Jjb_fofmHSBy-0zVcn2giT-Ko6tQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a40c6d00d.mp4?token=Tg7Xxs03Q-g5A_P0wirZHZ3ry7zmss2ooPXeZJFPNmGBulMkI6cPmLlaY2oKhZXiiemKS9lENbRUZ5zruWPfXosnNf3rugj7pA9MZvbj_VUb6Hv0Ibpa1z08Z6WK8pflCxk9_HCWJ6M6citzm-VQZzx-J3yx4ah83aKjCdW7hDoQ7U5dTeMKRY344DKmRG_lqa7VZzTjf7LA95J2JtPWMoOYC5fK36vbHyc9kOx4MqprZ9Zs94DIVulpMGfpopT1o7g0YyqLLU0RQrHD5HzoQToiyeR7_Qb6hg8V9Y-_S2Z_jrzc5RR2_OHSxMmG9hVQ3bXojlT9CTjXfQf8p3G5lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a40c6d00d.mp4?token=Tg7Xxs03Q-g5A_P0wirZHZ3ry7zmss2ooPXeZJFPNmGBulMkI6cPmLlaY2oKhZXiiemKS9lENbRUZ5zruWPfXosnNf3rugj7pA9MZvbj_VUb6Hv0Ibpa1z08Z6WK8pflCxk9_HCWJ6M6citzm-VQZzx-J3yx4ah83aKjCdW7hDoQ7U5dTeMKRY344DKmRG_lqa7VZzTjf7LA95J2JtPWMoOYC5fK36vbHyc9kOx4MqprZ9Zs94DIVulpMGfpopT1o7g0YyqLLU0RQrHD5HzoQToiyeR7_Qb6hg8V9Y-_S2Z_jrzc5RR2_OHSxMmG9hVQ3bXojlT9CTjXfQf8p3G5lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بیانیه رسمی نیروهای مسلح یمن: اگر ائتلاف تحت رهبری عربستان به حملات اعلام‌شده خود علیه اهدافی در صنعا ادامه دهد، این مناطق مورد حمله قرار خواهند گرفت:
🔹
ساختمان مرکزی شرکت آرامکو در شهر دمام
🔹
فرودگاه بین‌المللی ملک خالد در ریاض
🔹
پالایشگاه آرامکو در ریاض…</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/698105" target="_blank">📅 17:12 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698104">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
اختلال در سامانه ۱۱۵ اورژانس استان تهران به‌طور کامل برطرف شد
شروین تبریزی، سخنگوی اورژانس استان تهران در
#گفتگو
با خبرفوری:
🔹
با پیگیری‌های انجام‌شده، اختلال در سامانه ۱۱۵ اورژانس استان تهران به‌طور کامل برطرف شده و این سامانه در حال حاضر در دسترس است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/698104" target="_blank">📅 17:05 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698103">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سوره جن جلسه 2</div>
  <div class="tg-doc-extra">آیت الله جوادی آملی</div>
</div>
<a href="https://t.me/akhbarefori/698103" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
تفسیر سوره مبارکه جن| جلسه دوم
🔹
(00:00) سوره جن چه موضوعاتی درباره توحید، وحی و نبوت بیان می‌کند؟
🔹
(07:00) ارتباط جن‌ها با عالم فرشتگان و اخبار آسمانی چگونه توضیح داده می‌شود؟
🔹
(15:10) جن‌ها چگونه به باورهای نادرست درباره خدا پی بردند؟
🔹
(23:00) منظور از نگهبانان آسمان و شهاب‌های آماده برای جلوگیری از استراق سمع چیست؟
🔹
(34:35) شهاب‌های آسمانی چه نقشی در ماجرای آگاهی جن‌ها از بعثت پیامبر دارند؟
#تفسیر_سوره_جن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/698103" target="_blank">📅 17:05 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698101">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
تجهیزات و خودروهای مزدوران سعودی هدف پهپادهای یمن شد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/698101" target="_blank">📅 17:00 · 21 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
