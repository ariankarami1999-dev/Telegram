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
<img src="https://cdn4.telesco.pe/file/JvI_Ll3TxU1S4dgjv-yKfbhgKeQ1kW4EJzo2BpOnaXOitQ22tF2S1qugbGUdO54sjjPIQ7qhph8JSPjGR0fL7Pzhd8RIRxhL_OEk6JixUToEWC0M-t8tHMOfM45Z-6kz0wcPApewsMJ8iOA7HB_cObaAOY_qe1Kycq_c6HbZEh861dncB0PWSuHULIDMw2mSQx7xOUiGQSuSJtahCwux5G5yS0_T4zM4PJr2sXnLFzyRyz_Rh1E1pXT0RUUzShMhgIACkWyBP2TLbrTlB1rp9QvYZFfSo245Qj9sIbBcqysWs5-H3P_I5IZwsfAa4CzFMCq3YlpavAxidq7zuq63sw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 339K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-14 21:30:48</div>
<hr>

<div class="tg-post" id="msg-16521">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">⚠️
ادمین کانال تلگرامی به نام
کیان ملی
در تاریخ ۵ خرداد(۲۶ می) دستگیر شد و  از تاریخ ۱۷ خرداد(۷ ژوئن) این چنل توسط افراد اطلاعات سپاه کنترل میشود و مطالبی ضد انقلاب شیر و خورشید منتشر میکند. به هیچ وجه به این چنل دایرکتی نفرستید و از آن خارج شوید.
⚠️
@withyashar</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/withyashar/16521" target="_blank">📅 21:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16520">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ترامپ در تروث : از فیفا به خاطر انجام کار درست و لغو یک بی‌عدالتی بزرگ متشکرم! @withyadhar</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/withyashar/16520" target="_blank">📅 20:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16519">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FD5KWA-5e7tJlxWw1DKA2uiJoHqkJzEvbeYUAn9ebT71X4I1IxsPUBz4HuYwLRQ9zUy6q8y6wR0acPQNlmKizHapRy64461T5_QR8UnVXVQfNbFg2uI9iI6v38p0136D3soZ8uwUA4sIQSSyTTTz5Wrn6zkGkwzQs7s_V_8KZ1MvsiC3FZ67TsRRz2aMeC9AtMrp_JVsk5aWlUtgzPD5lvGcwXvi-shCqA6aOeVAXXndJL8eam2bvSkF8dAcKSFaHWjcHH00Sv-RgKiseTDYR9OHsil6VXAo41ezrYl2XHEPdSjDLIB7IXS0OleEiMRgqWDxWY7truq2JuSvzxTwJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : از فیفا به خاطر انجام کار درست و لغو یک بی‌عدالتی بزرگ متشکرم!
@withyadhar</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/withyashar/16519" target="_blank">📅 20:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16518">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">کاخ سفید : ترامپ قراره تو اجلاس ناتو با جولانی دیداری داشته باشه
@withyashar</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/withyashar/16518" target="_blank">📅 20:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16517">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">گزارشهایی از مشاهده یک شیع‌ ناشناس  نورانی با سرعت بالا در‌ آسمان تهران
@withyashar</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/withyashar/16517" target="_blank">📅 20:51 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16516">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZU_O07BJO-bYjDWU8f8YN86Q_jkVIkDcpmOSCWhbBXN4agpsHUa_WBVDJDI-5jCXvG020eXsPp68XDZ4c2YzbQMF-p8jIyGmCTQi0YSKxhcm9WE4dhN2qGjanAVl2zefE8H73eU1pUn9o6Kl3OFjcIYWm0rMFD2UPEtoDUpv4yxvlcZ_idxXXzvY5zqozGZH5gyYq92mzcUW-g3AfymR021JYFbD1h0PH1-RL5UncItIdOaqDZjD9ML_Wow0G2nGQdghiVRm6Al4zWtcV0Pu-i_UuL0YmjyAR0GmIsF8qT7iIfuc0RiuRQcYxBMGyEtuG296wg8HuNFbqVyFx9kXzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صداوسیما : انتقام رهبر شهیدمون رو
توی بازی ماینکرفت
از آمریکا و اسرائیل بگیرین و فیلم و عکساشو برامون بفرستین
@withyashar
😂</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/withyashar/16516" target="_blank">📅 20:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16515">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">تنگه دعوا شد
🚨
🚨
🚨
🚨
🚨
گزارش انفجار سیریک
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/withyashar/16515" target="_blank">📅 19:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16514">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">هرجاى اين كشور بگى نور به قبرش بباره همه ميفهمن كيو ميگى؛ هرجا هم بگى ريدم به قبرش، باز همه ميفهمن کيو ميگى.
@withyashar</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/withyashar/16514" target="_blank">📅 19:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16513">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NNYiQ4uWa7fRvOnzsjm1I389CCaLqCtHY_HavjBrEJGemlObVlY7Tlino-Q_XzIyVCvOcBtWKL1rAVQh7pxwsYMnlJmc39KJnHccAd0cTLTfs7MOKlk0e4YW5vqIXvao7YBh4mDGBaVdV6B2ndShaKg71I8-CrZMN7Sk5d3YddhdYx-osWoH13NEPuortkfvpzlg5smPAb72jjg1beqWoGafNUf72N1gVspQKZQXKG6NeQzlvWuxIh0Eft3i0qI6Oic_2jEDYI7k5rULtolC5fcoNBJAvwG9pA5q7w-_6rVZmfrNYdAoi0mJHX0OUEg8J5qCDq5nj_xKLY5NMX6QRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن امير اصلانى سال ٩٣بخاطر اين نقاشى و توهين به حضرت يونس اعدام شد.
@withyashar</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/withyashar/16513" target="_blank">📅 19:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16512">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J9KjyHolQhzmq9OPAP1DQEaPys-cIOWoCKpAsrGnylYqhf2e_cnbKs07036zD0lpE1tyZDAGThFIyCrCH3xP-g5vrlYDJ50Cav649sw-WK2nejX_KZPRML6YjsLnO5qy8nZbObrULNf2z1cruLGQdE0e_ZUqmwSuVe83UKpLsdQyE7Hj-TRG2qUIOUnvOSsGQfJbqUU_w6zrpW-xpuLytwvpxZzIijZ7SLNInVGu6ix4Z22Xz-pT0iW7Jy-98SGQi2XLTrIunmmRx6l2fqrtSTyoQCNcjTV4anAKsaCjX2HKky4LbU_NXUNZfRmGeKrkinkZAMpQ7e5vcxhR7F18Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک حادثه در فاصله ۳۰ مایل دریایی جنوب غربی الحدیده، یمن. یک کشتی باری، درخواست کمک ارسال کرد و اعلام کرد که مورد حمله مهاجمان مسلح ناشناس قرار گرفته است. @withyashar</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/withyashar/16512" target="_blank">📅 19:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16511">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iBweKIFCYiASCuGW1ko7UCwXYLrL9TkUYZBChmM8sAbSq9UsrLNXlHnQ_OfnRR4h99nA0-5v7qLLywFQ7_rNOCgfLZHdDrQwOy_wPC0Myk9sXhCXRdU0jcqL2QUaT0HSVytER0OZ_Y0jCsu8Q5DFlIMgwyog4rKgRyoaKfwCf7k2za368jiIaxTy3UJ7IOPhE-9N2G4MDNfssP9PTJwTr2JrAUmyRNo-wj-VmVD9lUNifESxISkQP1MiglDrIET9s-dx-uLSAG95nQphMpB5ZQBdW6ZAE7mD21U5dV65K1JZtAURRilsSm31umDA84GGr9ftaJA3okyd2rSXJ3VTGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی با صدور حکمی، غلامحسین محسنی اژه‌ای را بار دیگر به عنوان رئیس قوه قضائیه منصوب کرد.
@withyashar</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/withyashar/16511" target="_blank">📅 19:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16510">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">نیروی دریایی آمریکا: عملیات جستجو برای یافتن سرنشین مفقودشده در پی سقوط بالگرد در دریای عرب در یکم ژوئیه متوقف شد.
@withyashar
یاشار : خبر‌ سقوط بالگرد دوم الان فیک نیوز است</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/withyashar/16510" target="_blank">📅 18:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16509">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">نتانیاهو به شبکه خبری فاکس نیوز:
ایران، چه با توافق و چه بدون آن، هرگز به سلاح هسته‌ای دست نخواهد یافت.
@withyashar</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/withyashar/16509" target="_blank">📅 18:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16508">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V1ppDMl_dMqlVqPUl4SkjvFCErHoBsLgo0zy1zwFT_bdyjYqvUAmRHNH1bYFVtcLsSKVya6cxOX3YwMwzOBVkHYQjeqRpdBWR9q-qJmIFgmfCEeBOaC1cDheZVc2ZqebGczkla5fQmrlp_cSOpjsxTr0g1XC6Eu8ElaiyCkueM2NC7Sd4ptvcsrQy0RF90EewRSCHv0VW5V6BtsTOyfph57W4Mi7LD8iRSiVz9b3HJN0ycZagadsUFc3CXhh_uTYAENEbmITb7AVC2tIZdw9Pj35RgFR9hj036oNfj1HxNbjyERHg5PGcNIfUKVWXTeoqxiNXnbNkOQvGYQJL3mQlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ناو هواپیمابر آبراهام لینکولن امروز مشاهده شد  به‌همراه یک نفت‌کش پشتیبانی (که در تصویر دیده نمی‌شود) و یک ناوشکن، در مختصات:
22.2521, 60.8321
حدود ۱۰۰ کیلومتر دورتر از سواحل عمان ، در دریای عرب؛ که احتمالاً نشان می‌دهد توافق برای کاهش تنش در عبور از تنگه هرمز با ایران  همچنان پابرجاست.
@withyashar</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/withyashar/16508" target="_blank">📅 17:51 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16507">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">خبرگزاری های اسرائیل :امروز ثابت شد که این فرد به اسم ابراهیم ذوالفقاری وجود خارجی نداره و با هوش مصنوعی ساخته شده. چون حتی احمد وحیدی فرمانده سپاه هم توی مراسم حضور داشت ولی خبری از این نبود
@withyashar</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/withyashar/16507" target="_blank">📅 17:36 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16506">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">اتاق جنگ با شما : یاشار جان سلام
امروز تو مصلی بعد از پایان نماز ، بلندگو ورود مجتبی رو اعلام کرد اما بلافاصله هم صدای مجری قطع شد و بلافاصله آنتن ها برای مدتی قطع شد...
@withyashar</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/withyashar/16506" target="_blank">📅 17:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16505">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">کانال ۱۴ اسرائیل : اطلاعات جدید نشان می‌دهد که نیروی قدس ایران واحد جدیدی به نام «
مختار
» تشکیل داده است که با کارتل‌های مکزیکی و ایرانیان خارج از کشور برای توطئه ترور رئیس جمهور ترامپ و دیگر مقامات آمریکایی همکاری می‌کند.
@withyashar
🚨
😂</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/withyashar/16505" target="_blank">📅 16:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16504">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">فرودگاه بین‌المللی بندرعباس عصر امروز با فرود نخستین پرواز مسافری از مبدأ مشهد، پس از چهار ماه وقفه، رسماً فعالیت دوباره خود را آغاز کرد.
@withyashar</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/withyashar/16504" target="_blank">📅 16:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16503">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d4a6d9f34.mp4?token=Z2eqyq7X2x8eDQdQhfY4OlxB4oj5XluAlaHi2EtDHxVH50P1_3BYDpk6fvtvUs66qVPXw0RsTFXIrDnq5mpODU2VQLk2QslbP8brSRA6RfDfQosnFnpWwET-69h3oqI0v4Xjj7OqvRMw4OJJokqN91NP9mZvuMzJfeQEas55D31QmdUpaFzXwK2MoQz5rSjWTNHVUlqCu2MobzkvwNy8-99k1I23rGWpILpea1MZdAhEpSU4T66enQ6kXUXxgJQxXqEnVMpLvjwESGOQcUGF61O5XJ4QIfEMrBTROVR6ywBmWxXfgJALshFzijiwHDgJbpSCM5VxgAHkfh8r8x7sww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d4a6d9f34.mp4?token=Z2eqyq7X2x8eDQdQhfY4OlxB4oj5XluAlaHi2EtDHxVH50P1_3BYDpk6fvtvUs66qVPXw0RsTFXIrDnq5mpODU2VQLk2QslbP8brSRA6RfDfQosnFnpWwET-69h3oqI0v4Xjj7OqvRMw4OJJokqN91NP9mZvuMzJfeQEas55D31QmdUpaFzXwK2MoQz5rSjWTNHVUlqCu2MobzkvwNy8-99k1I23rGWpILpea1MZdAhEpSU4T66enQ6kXUXxgJQxXqEnVMpLvjwESGOQcUGF61O5XJ4QIfEMrBTROVR6ywBmWxXfgJALshFzijiwHDgJbpSCM5VxgAHkfh8r8x7sww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همچنان حملات سنگین اسرائیل در جنوب لبنان
@withyashar</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/withyashar/16503" target="_blank">📅 16:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16502">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f20cf4d81.mp4?token=Ynk55h9yMrgweVROen7IorKN92PKpWa_FEbHI1-X7l66gaIb-nRYwqANcxzFcAZ4RE6w1bnIv1SGPwNm0kk71_jDeSzJOs5uoODX93RdF0bPgK5I4RDqmlstYJPWSzYsXsFu5ss_W01fG3KoNaeLpZxu7SV6xx6XtlRrOr66XWVETjmcPlO0kbtleN-XYpG9jirUP9nf9Dn4-HABi-Q0wvqcA69T99eEYLubbeWqQaAjBaDTf2uBCG8o_lh9XlAQnIpDbuojsHOeNhP9WyuXc8Zl-2RBQo0Yfl1fmQT5_B1GcSnVLA-8e384EZwH6Wcp1SYFRNSXalbhvEhlEG8H5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f20cf4d81.mp4?token=Ynk55h9yMrgweVROen7IorKN92PKpWa_FEbHI1-X7l66gaIb-nRYwqANcxzFcAZ4RE6w1bnIv1SGPwNm0kk71_jDeSzJOs5uoODX93RdF0bPgK5I4RDqmlstYJPWSzYsXsFu5ss_W01fG3KoNaeLpZxu7SV6xx6XtlRrOr66XWVETjmcPlO0kbtleN-XYpG9jirUP9nf9Dn4-HABi-Q0wvqcA69T99eEYLubbeWqQaAjBaDTf2uBCG8o_lh9XlAQnIpDbuojsHOeNhP9WyuXc8Zl-2RBQo0Yfl1fmQT5_B1GcSnVLA-8e384EZwH6Wcp1SYFRNSXalbhvEhlEG8H5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات اسرائیل به جنوب لبنان
@withyashar</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/withyashar/16502" target="_blank">📅 15:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16501">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7mDL43DLXTWW8WOfhKd9lFS9rtu1NpQRjGOFeOJ3rQN7tH40Q3avI4G8ocm665h0ZFMgtBMX0uFzNCqs1ZUSYIdqGNuzR3o4YKfiOuhRUo9aiXeKu97_uLjgeGfx11R4sRYVL50JSKHQ0UXjK6S9OsP8Aot5mBCN0ut1pWfbGHATrVzfpZ40Z_pE18Rv4DN6AjwZ-1UUT_yRaactyzW8ydWbrv8xjHf_oz6Nw9oJZBXs2TWlza9UCTzQUkbI5xFcqBKpi9MHMFLPPlMD6_Em8MROGPwIBrdPh5zUL8GvsvcV_6Rdu43KHLPbDOAh2WY5TJZ-OVtxiAzQd08qSLgPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست وزارت خارجه اسرائیل به مراسم تشییع علی‌ خامنه‌ای
@withyashar</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/withyashar/16501" target="_blank">📅 15:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16500">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oLUOtHDCnq2osnmSLuKItdOv8Vtdfijq18537w0yTd4RLI3aF3QFle1bXerXlp0LYFJbM0HhpYSoRZiFYJBYt9s0j5hQpyRgzZjR4UMFw_LlEtnobDWu3ldvLoX-Yq1UlzrZ4WCL9wyNd7QxScZNEk1HCT9UnS8dPMmCPq666BR8q0hVQaoKAZ_vnNj88fOOGKi5hdwezWRaBcucGGMrKr92AU-kjavZ7FLG1A8L5eKhMbXr2OtC9iILZfoGNbsxryRLrze84orAKa6OaSxJoGWEAslOEl2cFwapez_kDrnC_yw1pTTgwSl5Mf6eYQzeW1prIgljFonablkrRC5SQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : از زمان آغاز جنگ در ایران، بیش از 273 آمریکایی در شیکاگو هدف گلوله قرار گرفته‌اند
😳
@withyashar</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/withyashar/16500" target="_blank">📅 15:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16499">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b892031853.mp4?token=K-0Kh5gJztqZUAFRPOSCMl6IM3VQSp1CC1zMWVWCwpoXd9GuYP7wNhaZL3WMDAmc5FX0Nh7nPyVkVdZbvCSBMMaaM3Udlybc9OkQg_zh3F9AETZiaFIUSegBrqDlKCCx_vaIM1xj9i5ylKtdxOYDwwl2JK_KSzO1sgqBXTzmi7JaA2HP3R1z-QsryX64fjPueJL-zvdPgF2bzWdWs2MKFpC1I5HazPS6wjUkkU2KjRna8pDOMunXBfEpGeJAPgKWAvzvQyrMZ2PJ-KqiL_AiEF3KQh7nTCvr3ShNJ5hH6jgWxwottDGAH7DTeLc7klhV6D764BXO0kvZ3VerEdqfYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b892031853.mp4?token=K-0Kh5gJztqZUAFRPOSCMl6IM3VQSp1CC1zMWVWCwpoXd9GuYP7wNhaZL3WMDAmc5FX0Nh7nPyVkVdZbvCSBMMaaM3Udlybc9OkQg_zh3F9AETZiaFIUSegBrqDlKCCx_vaIM1xj9i5ylKtdxOYDwwl2JK_KSzO1sgqBXTzmi7JaA2HP3R1z-QsryX64fjPueJL-zvdPgF2bzWdWs2MKFpC1I5HazPS6wjUkkU2KjRna8pDOMunXBfEpGeJAPgKWAvzvQyrMZ2PJ-KqiL_AiEF3KQh7nTCvr3ShNJ5hH6jgWxwottDGAH7DTeLc7klhV6D764BXO0kvZ3VerEdqfYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خنده های زننده و گرم گرفتن ملعون وحید خزائی با یکی از عوامل مهم کشته شدن ۴۲،۰۰۰ جاوید نام ،  فرمانده کل انتظامی جمهوری اسلامی احمدرضا رادان
@withyashar</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/withyashar/16499" target="_blank">📅 15:11 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16498">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">نتانیاهو : حرف‌هایی که درباره درخواست ترامپ برای حمله نکردن به تونل‌های لبنان پخش شده
کاملاً دروغه، ترامپ اصلاً چیزی رو به من نگفته
منم چنین درخواستی ازش نکردم و ما تصمیم‌هامون رو بر اساس ملاحظات خودمون می‌گیریم
@withyashar</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/withyashar/16498" target="_blank">📅 14:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16497">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kIPeqSvT3v2QV5_4zBuMAy8luEskrtYTEf8JwEvEE25e1SjJdtT4Gts3YhgTgO3yZEsH5d-P8snb4r-O85OM9N3qG6PageyWOGYIApTzaqwLvmJltG16I8fARr4D4ZT-dRGUDaFauY96nO-BAaxjbjI9U5rgkZSLSjMFyb7p6hIPSs6ExCPywcVF92mnmL5GKHuzrn7OdSHbsJHhgqJWv8Am_Kt2eRfmVtQrm5IItnjDfkYAqx_XcEcKtBXoq35mF56Z1GCo8XC1kYGbdI372TLIK_kueC0ahRuOB_cTCeIsCsQPeAKrsyHwzYH_1qgKKlTlRS5J285hp2ElUTzWNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک جت دولتی ایران از مسکو برگشت و هم اکنون بر روی باند فرودگاه مهر آباد تهران به زمین نشست
@withyashar</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/withyashar/16497" target="_blank">📅 14:32 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16496">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZYpHd4VTDooC5AIEwzeutZLhEgeKvLlgwEBa-x8TTPZL0n77aXn58I83qVQUXy76-2mWy9mKlHsIeJufXLx4dCgHOYQvVlGxssOseZIG8Z21SP8l985wJpX_AG2_MMNOm4pTLfKQjwDKTGV9eagR30FAyqteJKFctF5cRl0WyLa1YAwP5_1m-1sOaiHz0W2KJq4CmlLRJxyyM71O7BxZVsELv7I0duKbUN03l2z9BFpjGkJ15QTXou8_uFUre3awwxoDC5pw71ab6Y5JdMj-QKGgyVAhvF0qCpDTLJXGbvNeZCtLa40SoArOSSuM6mASIaIRonqGJ_K2LKdHuwMmzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همونطور که در ویس دیشب اشاره کردم که منارههای مصلی یکسان نیستند، در این تصویر هوایی هم کاملا مشخص است که ایده طراحی این بنا کاملا از سنگ توالت برداشت شده.
@withyashar</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/withyashar/16496" target="_blank">📅 14:16 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16495">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">کانال ۱۴ اسرائیل : احمد وحیدی، فرمانده کل سپاه پاسداران، که تحت تعقیب اینترپل، تحریم‌شده توسط ایالات متحده و در فهرست اهداف اسرائیل است، دوباره در روز دوم تشییع جنازه خامنه‌ای دیده شد.
@withyashar
اتاق جنگ با یاشار : موساد این روزا حسابی سرش شلوغه و لیست جدید ترور‌ رو داره آماده میکنه تا هفته دیگه بی بی برای تایید پیش ترامپ ببره</div>
<div class="tg-footer">👁️ 74K · <a href="https://t.me/withyashar/16495" target="_blank">📅 14:11 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16494">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">شاهزاده رضا پهلوی : ‏تلویزیون بی‌بی‌سی فارسی در صفحات رسمی خود، با انتشار بخش‌هایی تقطیع‌شده از گفت‌وگوی هایم، تصویری نادرست و گمراه‌کننده ارائه کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 74.7K · <a href="https://t.me/withyashar/16494" target="_blank">📅 14:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16493">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">کان نیوز : در اسرائیل معتقدند وقوع یک درگیری نظامی مجدد با ایران در آینده نزدیک وجود دارد.
@withyashar</div>
<div class="tg-footer">👁️ 76.1K · <a href="https://t.me/withyashar/16493" target="_blank">📅 13:49 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16492">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g4z_QOqhHVx5OJ8tU3cQSPwN44pxWEXg11BxhXjb4RBPIUuHMaIqWi2HyU7V-dfjIddaik98NMwmWJdghuNkJhfqK5c-LsA5DU-oXbdAunMeZL4fh7GSmzr5Yq-FKKE2QxNsChEoacoWAjvMax5pIJnc2uS-JVuFDUWdMW6Y5YY3ctTCu1zWDgIk3KFU2srb0gRglwg38bz1dLFomjLrt2R6NwGmWLPhWjj0tBDuIhFj7EagdgW4mFjleRmsus0LRt-KlLgoWpE9aYczhDE4ojUZTiF3CEDX_zWWkKqwWzixVXCGPuta7uBUCeASInItovmv0OrepBhtU97B5TZS_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشت هواپیمای تهاجمی A-10C Thunderbolt II که در خدمت وینگ ۲۳ ارتش آمریکا هستند، از پایگاه هوایی RAF Lakenheath به پایگاه هوایی موفق سلتی در اردن اعزام شده‌اند @withyashar</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/withyashar/16492" target="_blank">📅 13:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16491">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ارتش اسرائیل : دو فرمانده حماس در حملات  هوایی به غزه کشته شدن   ارتش اسرائیل به عملیات خود برای رفع هرگونه تهدید فوری ادامه خواهد داد @withyashar</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/withyashar/16491" target="_blank">📅 12:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16490">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCJYqEiDNqYsfV1W8EG4s3fW-sVqn9RAfPNG_m0NAIkqNfIFK05a9K_Xjxr8bUxSNGgQK0-O3QsXBA1A8paOpO9gR6ooUWOZWgQr5C6jObj4Q5mNcqerqaHU_tAXwyH7Tq2aAeiIFipm7Ej1MPi6p2gd0t-Th64RE3g8-6W_KKU6jr0MGb8WB95N8-4bi3OMuVvtA_2jKrrkQKrB9LXzfI9_JZVgZCfHSMRHxnojdKOltZ4eyjXi2wymDSoFs2OhSUAnaOVvWidgsyoeUbN9wpv-o6P83lWTzWeovuu1oNpqInR2UeIjmU_bFPvtBeHLvHJ21P_3l_ThHcS2rBJf8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک حادثه در فاصله ۳۰ مایل دریایی جنوب غربی الحدیده، یمن. یک کشتی باری، درخواست کمک ارسال کرد و اعلام کرد که مورد حمله مهاجمان مسلح ناشناس قرار گرفته است.
@withyashar</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/withyashar/16490" target="_blank">📅 12:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16489">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">کانال 15 اسرائیلی: جلسه فوق‌العاده کابینه سیاسی-امنیتی به روز سه‌شنبه موکول شد. انتظار می‌رود جلسه کوچکتر کابینه امشب برگزار شود.
@withyashar</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/withyashar/16489" target="_blank">📅 12:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16488">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d92ffd63b9.mp4?token=ahs_AAG1AretrSeelRGTz7V_S_zlsCUCSt4ABA3zvcoo0QRXW2bhqneHX0CoVAxmGO-BI8gTYImfm98xlBXlTeJjyq34qR5nKzmFi09Damx8nqYcSp9_hzAxTHE2D5Iogk705Fg6dkiwSlEvQqIs1K1L3LPI1iigRwK3SwXCQMkAxXreprimL12zqh8D8ULgkS86uyhiUvXMdL7AyVIs5YJnOkL8FA9bxqY49bGrM2KYuoeXx2et4Pn64l0T6IruJOLaNe17MJWN-eXDAu-bDjWBlSPRsc6EF2sKfwHjjpBmRgzNLwFRFdneTEbGqJy3QRP7hfOCV3KIolI9bl3LgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d92ffd63b9.mp4?token=ahs_AAG1AretrSeelRGTz7V_S_zlsCUCSt4ABA3zvcoo0QRXW2bhqneHX0CoVAxmGO-BI8gTYImfm98xlBXlTeJjyq34qR5nKzmFi09Damx8nqYcSp9_hzAxTHE2D5Iogk705Fg6dkiwSlEvQqIs1K1L3LPI1iigRwK3SwXCQMkAxXreprimL12zqh8D8ULgkS86uyhiUvXMdL7AyVIs5YJnOkL8FA9bxqY49bGrM2KYuoeXx2et4Pn64l0T6IruJOLaNe17MJWN-eXDAu-bDjWBlSPRsc6EF2sKfwHjjpBmRgzNLwFRFdneTEbGqJy3QRP7hfOCV3KIolI9bl3LgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه های رژیم ویدیویی از حضور احمد وحیدی در تشییع جنازه نشان دادن. به نظر میرسد در صحنه ای که کات میخورد بر‌اثر هجوم و درگیری‌ بادیگارد ها  کلاهش می افتد.
@withyashar</div>
<div class="tg-footer">👁️ 79K · <a href="https://t.me/withyashar/16488" target="_blank">📅 12:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16487">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">گزارشی درباره یک حادثه تیراندازی در آمریکا
: طبق گزارش شبکه خبری ABC، حداقل هشت نفر، از جمله چهار کودک، در کونی آیلند، ایالت نیویورک، در جریان جشن‌های روز استقلال آمریکا مورد اصابت گلوله قرار گرفتند.
@withyashar</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/withyashar/16487" target="_blank">📅 12:12 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16486">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">زمین لرزه شدیدی شهرستان بستک در غرب هرمزگان را لرزاند
@withyashar</div>
<div class="tg-footer">👁️ 76K · <a href="https://t.me/withyashar/16486" target="_blank">📅 11:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16485">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37255614f1.mp4?token=NfzripWQvihxivf584_tnT4uLqtjU-bAu4vDyh6liHyrjSikQm2rdJfxzgeKs-lMvK00n14XJtZ310r8ghyIf2Zl336Vepwdl7g38EGGSh02xwLf-1LhuPNs2BEzZPOMw_7CvXtRYtxHBiwlDqyzhVtHaIIA7HgpabSbGYOcRshPKsdYwOzDXhd1ac69_fg4j5euYnAMqy7Z4B0QcRusQ-RyjthBRAvqbB_RSs5-EBwDeqhX_kI46dzQzjBBJRooYZB9o3-VDjUnV7PxbLsLWp1w-niW9H98D9y3ixDB7mM9ObNBBRZi0GJkbIvdzq6faeeDfq0ZNSx-aHqU4P0mUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37255614f1.mp4?token=NfzripWQvihxivf584_tnT4uLqtjU-bAu4vDyh6liHyrjSikQm2rdJfxzgeKs-lMvK00n14XJtZ310r8ghyIf2Zl336Vepwdl7g38EGGSh02xwLf-1LhuPNs2BEzZPOMw_7CvXtRYtxHBiwlDqyzhVtHaIIA7HgpabSbGYOcRshPKsdYwOzDXhd1ac69_fg4j5euYnAMqy7Z4B0QcRusQ-RyjthBRAvqbB_RSs5-EBwDeqhX_kI46dzQzjBBJRooYZB9o3-VDjUnV7PxbLsLWp1w-niW9H98D9y3ixDB7mM9ObNBBRZi0GJkbIvdzq6faeeDfq0ZNSx-aHqU4P0mUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل : دو فرمانده حماس در حملات  هوایی به غزه کشته شدن
ارتش اسرائیل به عملیات خود برای رفع هرگونه تهدید فوری ادامه خواهد داد
@withyashar</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/withyashar/16485" target="_blank">📅 11:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16484">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hnz0GLPHbMKB86Q2SN8KQCUjIndu5eNbZiBL98KJxHy5464fKpyJtmK9SmlgLOdi8qLWrfILpBCQsl4Gb8UPLo1bXrin4CYFqnogdlbRu--GSPoqxYn44KNchSFCO3NBARCbXJeT2GV0KZX3UY4gXPUlcBZV2fOlqZqfQCmobfzvozs2FTXalx-zsmYzo3jF4eYqRPG_Pah3osDm3kZCXc_XQX14Jd6rKv8bqddXWHF3ogL4G_zcf_wnf3kWl7Y6c2l2xm-ZhMSf7TydpR_8xIUbrvOQRBFYbIUf1B_xMSLlLKtX5om8d_xb31oHFr0P4xGbIl1392OrTWC3MHhY5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم‌اکنون با پوشش هوایی و اسکورت سنگین، ارتش ایالات متحده یک کشتی باری (با AIS روشن) را از مسیر عمانی عبور می‌دهد!
این اولین عبور امروز خواهد بود اگر موفقیت آمیز باشد.
@withyashar</div>
<div class="tg-footer">👁️ 77K · <a href="https://t.me/withyashar/16484" target="_blank">📅 11:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16483">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">قایق‌های تندرو سپاه، مسیر عمانی را بستند
هرمزلتر: نیروی دریایی سپاه با استفاده از قایق‌های تندرو، کریدور مورد حمایت آمریکا در تنگه هرمز را به طور کامل متوقف کرده و در نیم روز هیچ شناوری از این مسیر عبور نکرده.
سپاه صبح امروز از طریق بی‌سیم به تمامی کشتی‌ها هشدار داد و همزمان قایق‌های گشتی نیروهای ویژه را برای اعمال کنترل ایران بر تنگه هرمز مستقر کرد.
@withyashar</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/withyashar/16483" target="_blank">📅 11:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16482">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">کامیونت یخچالداری که جنازه علی خامنه ای را حمل میکرد، گویا خیلی عجله داشته. ۲،۳۰۰ هم جریمه شده. @withyashar</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/withyashar/16482" target="_blank">📅 11:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16481">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">فرمانده نیروی قدس، اسماعیل قاآنی، و فرمانده سپاه پاسداران انقلاب اسلامی، احمد وحیدی، هم امروز در مراسم تشییع جنازه خامنه‌ای حضور داشتند.
@withyashar</div>
<div class="tg-footer">👁️ 76K · <a href="https://t.me/withyashar/16481" target="_blank">📅 11:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16480">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">سخنگوی ارتش ایران: از فرصت آتش‌بس برای تقویت توانایی‌های نظامی خود استفاده می‌کنیم و لحظه‌ای را برای این کار از دست نمی‌دهیم.
@withyashar</div>
<div class="tg-footer">👁️ 76K · <a href="https://t.me/withyashar/16480" target="_blank">📅 11:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16479">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">قطر: فعالیت‌های کشتیرانی به‌طور کامل و فوری از سر گرفته شد.
@withyashar</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/withyashar/16479" target="_blank">📅 11:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16478">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">وال استریت ژورنال: ایران، روسیه و کره شمالی، در نحوه تعامل با بازار ارز‌های دیجیتال، ایجاد رمزارز‌های اختصاصی خود و پلتفرم‌های معاملاتی برای دور زدن تحریم‌ها، بسیار پیشرفته‌تر شده‌اند
تهران و مسکو از ارز‌های دیجیتال برای خرید پهپاد و قطعات یدکی تسلیحات استفاده می‌کنند
@withyashar</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/withyashar/16478" target="_blank">📅 11:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16477">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">گریه های پسران خامنه ای بجز مجتبی @withyashar</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/withyashar/16477" target="_blank">📅 10:58 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16476">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">نیویورک تایمز: مجتبی خامنه‌ای همچنان در تلاش است تا در تشییع پدرش شرکت کند اما مقامات امنیتی مانع هستند
@withyashar</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/withyashar/16476" target="_blank">📅 10:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16475">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e4z-P1VkAfRkUXZ2t9lHPgu9ogX7T-EVG1KaEHlKQ8gje1FwZkMKYNtaWhQLD3Ags65NTDV4GDw0QP09os51jGshFzwEs-mtn7eQLliiawLUohbrktP8VTJ-27cjTNZEH_cQiSWCBLrhVEACNi28M31fz8sM39aaaLsJyvDP8D_r3RUW1c02YNL0qUOPezKXTni4PeWzWco4rFqupM6xM98cgCKa5WlId2iXiQ6X6hEZ3C-RCjeKwSjQymTgvzIdtEFaxFtZG3uiUpFGMqk8-kRJVz7xs8FQ8QQXDSiA0mj-7gEUUZ3obFRHpOYnxk1e16CY7F65uVe4GFna_wO5ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شباهت امام جمعه پاوه ( ماموستا قادری ) با ( هاشمی رفسنجانی ) که دایرکت منو منفجر کرد
@withyashar</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/withyashar/16475" target="_blank">📅 10:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16474">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SV9N-bQbqishj43Z1vm96NsFvEnRCD139Wj63JfrVplB6n_TkaX3IcpBZa0FCE-CZDKAaTFcoHPNYmqheA-KqT5dMNInf1CyQKOUe5jIHcjkmb0uILOh9uUUeSNHO5kNxmPrKfZIyU-upRTfqHnwJCdLmB9ItmxBKk0Qn9crQYwwNa1JN-c36WvXJ3Z3E3AaTHwRi6gMvUkr10M5zvBfaIgwtbQL4JLxwG_nSsjqIE6tv7BxprBQ7vauCgrbHTVpH_2lWjmeHe9a8oQP_1t3tXj0YnZs1hBaebc0gVAN8ZyfQ22PBU9DymYE7KG4BeimTjBBQbJ04UMImJMho_mmBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور مصطفی،میثم و مسعود خامنه‌ای ، فرزندان موشعلی ، پس از ماه‌ها دوری از رسانه‌ها  در جلوی دوربین. مجتبی خامنه‌ای دیگر فرزند رهبر پیشین و هم اینک ،  رهبر کنونی جمهوری اسلامی ایران همچنان در رسانه‌ها دیده نشده است! @withyashar</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/withyashar/16474" target="_blank">📅 10:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16473">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2866a3ad1b.mp4?token=KHP04yA3iH0J8QRL08iwDK57lm-6n-ScnKHql6NaV8QAKu9OCCUS-LD-4UZJ4qlNAMRiBNvPAODNq4wZ9hlp-EUy1_C_AEJO1kvYH-s3AhA2DZAjtB33mFL7jL2IWWPu-t2lD5P35jrGLOwawOoonL1vMBUbDBlTfxdg78b5dQ7YopaELU4nxHz8SG5Rlx61M_75iE9mJwAm2uzLLL4ZspzJej1KnIH52uk0a2WphjuBV8reDNR4NaWRuHfBJ_z_ouyODJmY6bfDixw2PCYROAt0rRcKSSQwvJe5hcDhtWGi_VgwoPg6op57S9WeQ8u5QUSu81sEuzHRSH8JH0MoTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2866a3ad1b.mp4?token=KHP04yA3iH0J8QRL08iwDK57lm-6n-ScnKHql6NaV8QAKu9OCCUS-LD-4UZJ4qlNAMRiBNvPAODNq4wZ9hlp-EUy1_C_AEJO1kvYH-s3AhA2DZAjtB33mFL7jL2IWWPu-t2lD5P35jrGLOwawOoonL1vMBUbDBlTfxdg78b5dQ7YopaELU4nxHz8SG5Rlx61M_75iE9mJwAm2uzLLL4ZspzJej1KnIH52uk0a2WphjuBV8reDNR4NaWRuHfBJ_z_ouyODJmY6bfDixw2PCYROAt0rRcKSSQwvJe5hcDhtWGi_VgwoPg6op57S9WeQ8u5QUSu81sEuzHRSH8JH0MoTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گریه های پسران خامنه ای بجز مجتبی
@withyashar</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/withyashar/16473" target="_blank">📅 10:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16472">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">حضور مصطفی،میثم و مسعود خامنه‌ای ، فرزندان موشعلی ، پس از ماه‌ها دوری از رسانه‌ها  در جلوی دوربین. مجتبی خامنه‌ای دیگر فرزند رهبر پیشین و هم اینک ،  رهبر کنونی جمهوری اسلامی ایران همچنان در رسانه‌ها دیده نشده است! @withyashar</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/withyashar/16472" target="_blank">📅 10:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16471">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a4c290e0d.mp4?token=rcIiCTLvAVpEK-7Cnq05n5hfTDDER9roYLFYt_w7XhNTX1XcL5a3FpwE6_4ziGnQXDcnlx6x9b5RqamijHluP8LLTnRpMOpjg3JtIoOG4_LqyH2mltnuUT751JthOSPNuDBdkT9etBtTNIzhXkFzKlEx0f_xVog89tNVU-IASAENMRqosp5thtncv_gDbSKo0SukzqE8VtHj_cNIQ-Gixehx0vI1QPk9VeuWxAK_FQioZVIzcZG4arMHCA8YANySXCfttL_DzBxGC_-wQPamRafi-7b0MyTu8gHDGY4HUYySTMo6w9G7C6Q4FNRVOyJ5XjdI-gUBUjZFKHP_TqaFQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a4c290e0d.mp4?token=rcIiCTLvAVpEK-7Cnq05n5hfTDDER9roYLFYt_w7XhNTX1XcL5a3FpwE6_4ziGnQXDcnlx6x9b5RqamijHluP8LLTnRpMOpjg3JtIoOG4_LqyH2mltnuUT751JthOSPNuDBdkT9etBtTNIzhXkFzKlEx0f_xVog89tNVU-IASAENMRqosp5thtncv_gDbSKo0SukzqE8VtHj_cNIQ-Gixehx0vI1QPk9VeuWxAK_FQioZVIzcZG4arMHCA8YANySXCfttL_DzBxGC_-wQPamRafi-7b0MyTu8gHDGY4HUYySTMo6w9G7C6Q4FNRVOyJ5XjdI-gUBUjZFKHP_TqaFQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حضور مصطفی،میثم و مسعود خامنه‌ای ، فرزندان موشعلی ، پس از ماه‌ها دوری از رسانه‌ها  در جلوی دوربین.
مجتبی خامنه‌ای دیگر فرزند رهبر پیشین و هم اینک ،  رهبر کنونی جمهوری اسلامی ایران همچنان در رسانه‌ها دیده نشده است!
@withyashar</div>
<div class="tg-footer">👁️ 85.4K · <a href="https://t.me/withyashar/16471" target="_blank">📅 10:07 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16468">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Uik-_fd8AiqJefXtWIA_TebJyD4D3F3Rs_yYj2wtbsfcRu1Poxg1IupLzl9u0SPQJe557otqv7OrWYS7hjBD3rCIwG0TYVLVmk8Wt5tnqvNtUkrgqwcGF9-D8saRaTUODl08DqubtgsO3haKuodKa0y3FSenGgWhQhplirzcYkX2EeJjDOsWPLHpmD0S-k8WL5ol8IlfzH9EI3sV-Wo515XfZOc1JpewHZE7Ej-hh_Xpi-gcwuvSz_ShO5mEgsy4A_NBO-a-KC3m6hxzL_4Tjusrp9AYYBH0QCOKwcRZ66IyRSwWE1J-L9OJy-QJoLXkIb7V5ZeYu6iAPxeCSpHSvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U6R9RdIxQDkReLFAwpGwOitUsrWjK1puIM1QtqcxqlXdJLwiZ-7gyaxMw0f7IBBiuurlAIS8Us_8MGy6y0WrjPxfGH-fDatA9xXgA56jUNtYAftkZDxUhbDcpEIgQIwjKAJD0jBHBPjPXZ_xz5G1TbrOk2a-NMrCgwLBV5QMn32mJiK6Z1q0Zo_EyWKKsw-G0WAMlcqaHQ_clEXEnFtCKTY6jUeha8SbU7FPgxI_GyKJRifohku7_aDSc-wVZ4fZbKny4z9tzzuD-6CTe8BytFoRIbrxpqd2LSzPcBAOqlF_iAXQa34uzwmcmN1g1JIg4l0E3pxegl6ovQnpQ37S4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E45Cqh6uuj_fm48N8dCJdYnIvAYY4qhwMLgUSHPe5mGSn1M_TuGfJdBSQD3kpmr97B6XlsTDdQRJLsY-4lMUyqGwksmHw4l-gTEMqujCJ5-H7SRJ0uNhlfboYzu0gbEKrG1hXq8-sHLKZxspxO4ON44BOXxSmkL8hLUBpRzemJv-ZrFgmYHLLaJ99qh_wp2LZwojqr2WmclNJvZ0DstidKt2iMWUITTsAnwGldpHRypOQLtnyIDJkWGtBO56VCEm_upHDe_6juToG3bOLZJW4u5wriSjorTLeuSC_ph-sSzRqH6VxMzvDXhGNq7C2frzCKxeORJbDRoInVyGWjj9JQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شهستان پهلوی (ویس قبل رو گوش کنید)
@withyashar</div>
<div class="tg-footer">👁️ 97.2K · <a href="https://t.me/withyashar/16468" target="_blank">📅 00:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16467">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">شَهِستان پهلوی، نام یک مجموعه بزرگ شهری در زمین‌های منطقه عباس‌آباد تهران بود که اجرای آن در سال ۱۳۵۴ در زمان محمدرضا پهلوی شروع شد ولی در طرح آمایش سرزمین ۱۳۵۴ ستیران آرمان‌گرایانه اما ناپایدار و مخاطره‌آمیز برای توسعه کشور و شهر تهران قلمداد شد و با وقوع انقلاب ۱۳۵۷ ایران هیچ‌گاه بطور کامل اجرایی نشد. بخشی از این طرح احداث یک برج مخابراتی مانند برج میلاد امروزی بود
@withyashar</div>
<div class="tg-footer">👁️ 99.9K · <a href="https://t.me/withyashar/16467" target="_blank">📅 00:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16466">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">گزارشهایی از فعالیت پدافند پرند
@withyashar
🚨</div>
<div class="tg-footer">👁️ 99.7K · <a href="https://t.me/withyashar/16466" target="_blank">📅 00:26 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16465">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">کانال 15 تلویزیون اسرائیل: در‌تماس‌ امروز دونالد ترامپ از بنیامین نتانیاهو خواست اوضاع لبنان را متشنج نکند.
@withyashar</div>
<div class="tg-footer">👁️ 99.3K · <a href="https://t.me/withyashar/16465" target="_blank">📅 00:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16464">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ارسالی : یاشار جان درود
داداش همین الان از اطراف مصلا برگشتم ، تمام حجم ترافیک و شلوغی برای صف های ایستگاه صلواتی ها و مفت خوری ها بود
یجا مردم بخاطر یدونه تخم مرغ آبپز و یدونه لواش داشتن همدیگرو میزدن همشونم طرفدار اینا
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/16464" target="_blank">📅 23:07 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16463">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">اکونومیست: جنگ بعدی خاورمیانه بین اسرائیل و ترکیه است
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/16463" target="_blank">📅 22:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16462">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ترامپ در تروث : اروپا دارد یاد می‌گیرد که وقتی مجرمان جهان سومی را در خود جای می‌دهد، خودش تبدیل به یک کشور جهان سومی می‌شود. این اتفاق خیلی سریع می‌افتد، فقط در یک چشم به هم زدن. من درست به موقع انتخاب شدم!!!
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/16462" target="_blank">📅 22:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16461">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">فردا عصر کابینه امنیتی اسرائیل یک نشست
ویژه برگزار می‌کند
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/16461" target="_blank">📅 22:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16460">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">رئیس‌جمهور عراق:
عراق نه با ایران در برابر آمریکا متحد است نه با آمریکا در برابر ایران
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/16460" target="_blank">📅 21:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16459">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">نتانیاهو ۲۵۰ سالگی استقلال آمریکا را به ترامپ تبریک گفت و گفت:
«ممکن است ما در قاره‌های مختلف زندگی کنیم، اما به دلیل سرنوشت مشترکمان، به شدت به هم متصل هستیم. آمریکا بزرگترین نیروی آزادی‌خواهی بوده است که جهان مدرن به خود دیده است. اسرائیل مفتخر است که در کنار آن بایستد. زیرا اتحاد ما نه تنها بر اساس منافع مشترک، بلکه بر اساس ارزش‌های مشترک بنا شده است. امروز، این ارزش‌ها مورد حمله قرار گرفته‌اند. مستبدانی که با آنها روبرو هستیم، شعار مرگ بر آمریکا، مرگ بر اسرائیل سر می‌دهند.»
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/16459" target="_blank">📅 21:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16458">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">Bitcoin +63,100
🆙
@withyashar</div>
<div class="tg-footer">👁️ 96.7K · <a href="https://t.me/withyashar/16458" target="_blank">📅 21:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16457">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">گزارش انفجار شدید در سلیمانیه عراق
@withyashar
🚨</div>
<div class="tg-footer">👁️ 95.6K · <a href="https://t.me/withyashar/16457" target="_blank">📅 20:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16456">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">العربیه : ارتش اسرائیل شنبه 13 تیر با انجام چهار عملیات جداگانه، اقدام به تخریب گسترده خانه‌ها و مجتمع‌های مسکونی در مناطق شرقی و شمال شرقی شهر خان‌یونس کرد.
@withyashar</div>
<div class="tg-footer">👁️ 95.4K · <a href="https://t.me/withyashar/16456" target="_blank">📅 20:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16455">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ترامپ به آکسیوس : نتانیاهو خودش درخواست دیدار با کاخ سفید رو داده  - ممکنه همین هفتهٔ آینده این دیدار انجام بشه @withyashar</div>
<div class="tg-footer">👁️ 95.4K · <a href="https://t.me/withyashar/16455" target="_blank">📅 20:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16454">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ترامپ به آکسیوس : ایرانی‌ها برای امضای توافق تقلا می‌کنند.
@withyashar</div>
<div class="tg-footer">👁️ 93.6K · <a href="https://t.me/withyashar/16454" target="_blank">📅 20:38 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16453">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ترامپ به آکسیوس : نتانیاهو خودش درخواست دیدار با کاخ سفید رو داده
- ممکنه همین هفتهٔ آینده این دیدار انجام بشه
@withyashar</div>
<div class="tg-footer">👁️ 92.1K · <a href="https://t.me/withyashar/16453" target="_blank">📅 20:37 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16452">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ترامپ به اکسیوس : "از دیدن ایرانی‌هایی که در مراسم خاکسپاری خامنه‌ای گریه می‌کردند، شگفت‌زده شدم. من فکر می‌کردم مردم از او متنفر بودند."
@withyashar</div>
<div class="tg-footer">👁️ 92.4K · <a href="https://t.me/withyashar/16452" target="_blank">📅 20:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16451">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ترامپ به آکسیوس : هیچ یک از طرفین در طول مراسم تشییع خامنه‌ای، به سمت دیگری شلیک نخواهند کرد.
@withyashar</div>
<div class="tg-footer">👁️ 88.8K · <a href="https://t.me/withyashar/16451" target="_blank">📅 20:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16450">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ترامپ به آکسیوس:«همه آن‌ها آنجا هستند. یک گلوله می‌توانیم همه آن‌ها را از بین ببریم ، اما ما این کار را نخواهیم کرد، زیرا در آن صورت، هیچ‌کس برای مذاکره با ما نخواهد ماند.»
@withyashar</div>
<div class="tg-footer">👁️ 89.3K · <a href="https://t.me/withyashar/16450" target="_blank">📅 20:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16449">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">الحدث: دور جدیدی از مذاکرات بین آمریکا و ایران در پاکستان، در تاریخ ۱۱ جولای برگزار خواهد شد @withyashar</div>
<div class="tg-footer">👁️ 87.2K · <a href="https://t.me/withyashar/16449" target="_blank">📅 20:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16448">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KfXOZTT4WidVj6fRix9EN7WgIfAUCWia3Nj7ezE834KOB2dPSW40vVkiuSDWmvhlphJoSY_JObw5daYo0Gh9D_sEc3XycCdcMRvUhpW3gTbJ7g8-puDUQ5XZTUha44MEBXh3w2h8-pm1Boa1Z3_Cw3DENKDWYm10uyFunELcdQ_osW8sj5rzfiOBsaMBrtTjTkwbjMiFpEDZ-mrlOI3L9iqLsx1IPr5lJ5qPUhhlRW9yx5ObNrVfej3sIKJ-fdf0IYCmXnjg17Do6tgmJSnvnfS7U95eqPiz4P_DOFTrRDQJ56E6nAB85qEV4kOvzrXhSAuchH7LJTt5pOzTDjpFoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای…..
@withyashar
😂</div>
<div class="tg-footer">👁️ 90.3K · <a href="https://t.me/withyashar/16448" target="_blank">📅 20:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16447">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jWeilkgHSA0aVY9Q6FrF6xhwcNgjYgHYLaHOKAblYNKyxv1YGcWMgEOdgKVePRGMj99unyiG9VSwHeHap9lG3fHv2LbXL-GUlVTM7nYNUPrCt3dgy4qQQj8g667WNDt7LH4IgsxVSv3M3SoEzMmkFjoRSydtbrux9UrNMv0-3aOW_l7FE1FOOz2LU6HXrS4RFZw8If06S9PN2bc7LXr_ss_1PDvuEU5pTgQaAesdZ3I_1nUqE_Mqnqj5DKmyNdKEcZNI0yXXK273j8_MrlmwqBurPCWs9wxism69hM0aUxMSWakevibejnD1TpUZrW1Ho2BgS5_duKyKo6JGKOqDHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکورد جهانی علی خامنه ای
بیشترین فاصله زمان مرگ تا زمان خاکسپاری رهبران جهان، مربوط به الیزابت دوم بود با ۱۱ روز فاصله که علی خامنه‌ای با ۱۳۲ روز فاصله با قدرت این رکورد رو شکست و نام خودش رو در تاریخ ثبت کرد
@withyashar</div>
<div class="tg-footer">👁️ 91.2K · <a href="https://t.me/withyashar/16447" target="_blank">📅 19:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16446">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">تاکنون پنج فروند بوئینگ 777-268ER سابق سعودی به ماهان ایر، بزرگترین شرکت هواپیمایی ایران، تحویل شده. کاربر نهایی این هواپیماها، یک شرکت هواپیمایی مستقر در اصفهان متعلق به یک میلیاردر ایرانی است. از پنج فروند، دو فروند در حال حاضر در فرودگاه بین‌المللی مهرآباد…</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/withyashar/16446" target="_blank">📅 18:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16445">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">سنتکام : یک فروند هواپیمای HC-130J Combat King II نیروی هوایی ایالات متحده، سوخت چندین هواپیمای تهاجمی A-10C را تأمین می‌کند. سوخت‌گیری هوایی به هواپیماها اجازه می‌دهد تا برای مدت زمان طولانی‌تری به عملیات خود ادامه دهند. @withyashar</div>
<div class="tg-footer">👁️ 90.8K · <a href="https://t.me/withyashar/16445" target="_blank">📅 18:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16444">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C4vwSdG8yCqz01_EYGQi5xabwLZB1Q2XxpD1KXr4lFREHS4U8P-PFMzb6NaGmO7e9FHoSFmWpae4FXqA-CC_0jFatqLtqSZ0vvJMsZLXwhc4GmuwdaWwngV1TOH4NPYGmPs4HdbSzkf9EU6KQBjJt3VvXoq1gVpsTe408sqaYWi_cli56mzlC6mhUz9W7wc1IUVJxUW90_Lfa6bSY5amssHeYtO6wUPXBza3ikZOCl2sl8CJr1GWZVeK9t-BaZl4ukJ4Z06ybIPPpKMutC0ihbIA3cNIDlgYISxEWuBQlBR3JyAZnql-xui0TTh1neBhiRiu0zON-TxeLqXgKfG-CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشریه نظامی «میلیتاری واچ» نوشت: کارخانه هواپیماسازی کومسومولسک-نا-آمور روسیه
تولید ۲۰ فروند جنگنده سوخو-۳۵ سفارش داده‌شده توسط نیروی هوایی ایران را به پایان رسانده است.
وزارت دفاع ایران در حال حاضر هزینه نگهداری و پشتیبانی این جنگنده‌ها را در داخل روسیه پرداخت می‌کند تا پیش از انتقال به ایران، در روسیه نگهداری شوند
احتمال دارد نخستین سوخو-۳۵ها از پایان سال ۲۰۲۶ وارد ایران شوند؛ آسیب‌دیدگی زیرساخت‌های پایگاه هوایی همدان یکی از عوامل اصلی تأخیر در انتقال است.
@withyashar</div>
<div class="tg-footer">👁️ 95.2K · <a href="https://t.me/withyashar/16444" target="_blank">📅 18:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16443">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">الحدث: دور جدیدی از مذاکرات بین آمریکا و ایران در پاکستان، در تاریخ ۱۱ جولای برگزار خواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 92.4K · <a href="https://t.me/withyashar/16443" target="_blank">📅 17:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16442">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">نیویورک‌تایمز به نقل از منابعی در سپاه:
مجتبی خامنه‌ای خواهان حضور در مراسم خاکسپاری پدرش در مشهد و اقامه نماز میته، اما مقام‌های امنیتی تاکنون با این درخواست مخالفت کردن.
به گفته این منابع، نگرانی از احتمال سوءاستفاده اسرائیل برای ترور یا شناسایی محل اختفای اون، دلیل این مخالفته.
@withyashar</div>
<div class="tg-footer">👁️ 98K · <a href="https://t.me/withyashar/16442" target="_blank">📅 15:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16441">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hUuKIfgY21CrC01Zo1Py-67-Tao0pjb0n-W6A-OD5t_XARYhONJ_6wFkhegqfLmkWJnVlz634xUWU3bzAtOPEw9j71BfF7R-94sH6AJgizp2lVRz4gWtPJcYFXNRTX6o0Ktqty1-Rf2qxOO21e4OUQxdHMYKM7sW-aFk8oioklooDbXo_jEcPvOp_g3T6q2fwCxn6c66xn7ZXxNv1w12YY51A3hC7PVYo2k7n2ErPMoH_X08r_-FHPNDG_IclUsLy-qKHHLEx2WzjX0tMfQPdAPTaBrw-LsiiQz3C-ZibVwH3cB7zwsgjrdJYyM_VjQ52e06g1_xJkJpGcbVCg818A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار علی عظمایی امروز به عنوان فرمانده جدید نیروی دریایی سپاه معرفی شد.
فرمانده قبلی سردار تنگسیری بود که توی جنگ کشته شد.
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/16441" target="_blank">📅 15:41 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16440">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">نیویورک‌تایمز:  عبدالناصر همتی به مجتبی اطلاع داد که در صورت تداوم محاصره دریایی، ذخایر مواد غذایی و دارویی تا پایان ماه اوت به اتمام خواهد رسید.
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/16440" target="_blank">📅 15:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16439">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ada09162bc.mp4?token=EHyEmEY75bUKbheAotGMaSOIkYwjjpSP8U6Sq3oFut9OycEzQ35H3Ed0UPnnNMbD5BLu5Vgg6LL7SbvgZHvfcxCAuWIivw3Gs_mfWAUoWSAnS4lAcTbpxBWK4ZiXORYV1KcZqMweTRdYW5T1PxFqWVJ37HldKYSOT4ma0sybuw3YV7Ms_sZmKn2CT_nzqvnJJRR3msjtC_gfABPOyViyEtDRgGxQRQwUBE7r3V5MEXiXwUeANIPqrUDjMjdqAb1H2ADpGBnfS1nO3zYrXc2H2OSEHPKDVR2C_I-lCm-qTRPXfuTaUIoWVmeuT9-BrZWa2fo72ImP_KavCwAEbrEzkJ2gWnSSMAUuzCX9UeLoBoYkEBe1_BoKaSrXVc3Wh9aixE9f8TuyR8Ie4erb_rkW2frVPXCAisM7z46BS_cPy28FokdgL8Yp6F5YOQQMOejmV6UDuSrezvL0pO0Usq_bJEKtGde3CFHyoU0YJW-8FO-3mZvza-yVpHsnPe6LjDEUr_239I-27tYsKxp2Vu2dFxK3PvEgZo0g9T7Y0AMDIXQxx360xOGWXcTPWhucDrDuOlZLaac88-H0u0SD9zQag8v8kFfy1vr0yLy8sRaJXUC1Q6hG36L_rCUCJYvEJI0h8maz6fxOcwiCkkLVcrbR5MEmZuuRLtMzuayID05IC_Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ada09162bc.mp4?token=EHyEmEY75bUKbheAotGMaSOIkYwjjpSP8U6Sq3oFut9OycEzQ35H3Ed0UPnnNMbD5BLu5Vgg6LL7SbvgZHvfcxCAuWIivw3Gs_mfWAUoWSAnS4lAcTbpxBWK4ZiXORYV1KcZqMweTRdYW5T1PxFqWVJ37HldKYSOT4ma0sybuw3YV7Ms_sZmKn2CT_nzqvnJJRR3msjtC_gfABPOyViyEtDRgGxQRQwUBE7r3V5MEXiXwUeANIPqrUDjMjdqAb1H2ADpGBnfS1nO3zYrXc2H2OSEHPKDVR2C_I-lCm-qTRPXfuTaUIoWVmeuT9-BrZWa2fo72ImP_KavCwAEbrEzkJ2gWnSSMAUuzCX9UeLoBoYkEBe1_BoKaSrXVc3Wh9aixE9f8TuyR8Ie4erb_rkW2frVPXCAisM7z46BS_cPy28FokdgL8Yp6F5YOQQMOejmV6UDuSrezvL0pO0Usq_bJEKtGde3CFHyoU0YJW-8FO-3mZvza-yVpHsnPe6LjDEUr_239I-27tYsKxp2Vu2dFxK3PvEgZo0g9T7Y0AMDIXQxx360xOGWXcTPWhucDrDuOlZLaac88-H0u0SD9zQag8v8kFfy1vr0yLy8sRaJXUC1Q6hG36L_rCUCJYvEJI0h8maz6fxOcwiCkkLVcrbR5MEmZuuRLtMzuayID05IC_Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت نیکسون در ‌تهران ۱۹۷۲
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/16439" target="_blank">📅 14:45 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16438">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UpPqJBREdrKwKPT_wkzKNJFjiwO_6Y3Q1xXG6Nnzo1-9y7v6JTDvu-Lg_N6SCwC-jxoaDb9T3vkOemK1vub-xT6iGncVZMGW4OjpxrWxp0UCVE5wyyhvVrCFYhP9ghP98RV1KvxDfFI4PXStSoa74anw8tutS38BM3OfowE-9HgZtPPJjGb9FDR3LCjI9Tt9Kum5aj-V9H218SbMSqey_gVUlcYXsBUqOy6IvxGSXT_eA1Pp5Jt6vJ0Z_GngYsIQjb9OqfOJ9_xqHR5VB-MEbE5cb8Joq8L5s8gCsw0W6MKNtL0M3xo62ajaWc4kyzVmVbtUTzMWpRiVKRkc1n-CNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام : یک فروند هواپیمای HC-130J Combat King II نیروی هوایی ایالات متحده، سوخت چندین هواپیمای تهاجمی A-10C را تأمین می‌کند. سوخت‌گیری هوایی به هواپیماها اجازه می‌دهد تا برای مدت زمان طولانی‌تری به عملیات خود ادامه دهند.
@withyashar</div>
<div class="tg-footer">👁️ 99.9K · <a href="https://t.me/withyashar/16438" target="_blank">📅 13:09 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16437">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mC7E5vMxLTybQ0M7ZmiOgNQPvSf-aYLa1tyBBHVonq4vMYme6xRAzxa55VJxUsG1d-rRtVMf978GdmwSbaTcf1OCvtpDjUtuXlEA6rQ5gZTIZecYHgwfE3MqEhDS67QLgM6fGOIZnGH6LeC_Kj120ffnlKw8m_h85BPyptLfnokZZ3Jz6wNUXMQOmPDb9zwK8R4gDAf4Eu6a0pQXWOU0FYNCELMDJ6HjTWijxNR626T70Y9Bg1BaDMDZE3XOu-jc_lzYLx5pIoSVURi7DPyqjF-U3NIF1H9Hm_UpTAxpXUGvkxIDvxGcJYJq1-FiPgFQUiDt7HFi5aRg-7ZrJ2wNXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان درست شد ، عباس مکار و ممباقر نره
@withyashar
😂</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/16437" target="_blank">📅 12:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16436">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mwBgEEPpYfKblbq3Is_37oiWtWArnRfO5h6nWoBcct3T6dCEBqVBVudtZ_ZhF6kZGCDklvlpcJuZ8NMYZScpS-J7DxrUo7bXKg3fh5nfIf0t3GMjMlruLmtoHnXMCpXUEmrZABVEbXIcfgy3IpkzZEP1mgNCe9nx8Ze9sPF1UnHuUiT-TT_ZF0bIC-swTP8ypDQB1Wlfu5n9CxoTNh0eRNqriZAIHalXRp1JgG9wLlka9QOjl_CXqnCs9MWcfnl1Sf1IP03nq5WQ4yPVUMcH9E0YxXxQ4jvyd-8IIonuJvFXLXbNP62D5JJvvJVrZZlqXN0fqIwldbNmE6fO9mc2UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوباره حمله اسرائیل به لبنان
@withyashar</div>
<div class="tg-footer">👁️ 98K · <a href="https://t.me/withyashar/16436" target="_blank">📅 12:09 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16435">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ko5XL_YYvHw7-P-1n60FlrdqMDVZc8NLLKjwd4UnUYIg7W5U9mXYFGIkzaVOkrM5O1OXyCDSXUY_KSlePhOHXH8RooDThqw9CrVYm-LeYZuDzPGiCdPCVwb9fpmr6n82qXxF4ptDsHzcVytEx4fKu_vYRLVi7ZT7uUARX2qN6psgpA5ohr7PHENt63x-U1i36y-ReEQJICnVXYQluS0q0R-i-alfaV7Cm_RI8w3v-kMv-jJcOYzRTI7rrAN07Obr3UQeT17CbJ-oFYflsAqFyAMNYtNImFzgzh0QC1GSsBdyLjTEwYvv3HYoEr4lI1f3hoNtfe9D9o5yV8281wNAag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در‌ تروث : سری جدید ۱٠٠ دلاری با امضای ترامپ
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/16435" target="_blank">📅 11:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16434">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">افزایش تولید نفت اوپک با بازگشایی تنگه هرمز
طبق یافته‌های نظرسنجی بلومبرگ، تولید نفت خام اوپک طی ماه میلادی گذشته با ازسرگیری صادرات تولیدکنندگان خلیج فارس از طریق تنگه هرمز در بحبوحه تفاهم‌نامه ایران و آمریکا، افزایش یافت.
@withyashar</div>
<div class="tg-footer">👁️ 98.4K · <a href="https://t.me/withyashar/16434" target="_blank">📅 11:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16433">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ان‌بی‌سی نیوز به نقل از چند منبع آگاه:
آیت الله سید مجتبی خامنه‌ای احتمالا در مراسم خاکسپاری آیت الله علی خامنه‌ای حضور نخواهد داشت، چون در حمله آغاز جنگ به‌شدت مجروح و چندین بار تحت عمل جراحی قرار گرفته!
@withyashar</div>
<div class="tg-footer">👁️ 99.2K · <a href="https://t.me/withyashar/16433" target="_blank">📅 11:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16432">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">کانال ۱۴ اسرائیل : حسام حسن، سرمربی تیم ملی مصر که اولین پیروزی تاریخ این تیم را در مرحله حذفی کسب کرد و به مرحله یک‌هشتم نهایی جام جهانی 2026 صعود کرد (در مقابل آرژانتین)، از این فرصت برای ابراز اعتراض سیاسی استفاده کرد و پیروزی را به مردم نوار غزه تقدیم کرد: "امیدوارم خداوند پیروزی را به آنها عطا کند."
@withyashar</div>
<div class="tg-footer">👁️ 98.2K · <a href="https://t.me/withyashar/16432" target="_blank">📅 11:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16431">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">نیکلاس لیساک فعال رسانه‌ای نوشت:
"یک منبع موثق می‌گوید مجتبی خامنه‌ای در اواخر ماه مارس، پس از آنکه بر اثر جراحات ناشی از حمله هوایی‌ای که پدرش را کشت به کما رفت، جان باخت.
او هرگز نفهمید که رهبر جمهوری اسلامی شده است.
قالیباف و سپاه اکنون در جست‌وجوی افرادی با شباهت ظاهری (بدل) هستند تا آن‌ها را در انظار عمومی به‌کار گیرند."
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/16431" target="_blank">📅 10:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16430">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">منابع اسرائیلی به «کانال 15»اسرائیل اطلاع دادند بنیامین نتانیاهو، در انتظار چراغ سبز ترامپ، برای تصرف پایگاه «حزب‌الله» در ارتفاعات منطقه «علی الطاهر» در جنوب لبنان است.ترامپ از نتانیاهو خواسته تا زمانی که مذاکرات با ایران ادامه دارد، این عملیات را به تعویق بیندازد. برآورد ارتش اسرائیل، بین 30 تا 40 نفر از نیروهای یگان «بدر» وابسته به حزب‌الله، از جمله شماری از فرماندهان این گروه، در داخل این پایگاه گرفتار شده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 96.9K · <a href="https://t.me/withyashar/16430" target="_blank">📅 10:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16429">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">سی‌ان‌ان‌ به نقل از مقام‌های آمریکایی:
مقامات دولت ترامپ از نزدیک شبکه جاسوسی اسرائیل که در ماه‌های اخیر، فعالیت‌های اطلاعاتی و جاسوسی خود علیه ایران و آمریکا را افزایش داده، زیر نظر داشته‌اند
مسئولان آمریکایی تلاش کردند به ایران درباره این نگرانی که اسرائیل ممکن است قالیباف و عراقچی را ترور کند، هشدار دهند
@withyashar</div>
<div class="tg-footer">👁️ 93.8K · <a href="https://t.me/withyashar/16429" target="_blank">📅 10:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16428">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">حضور هادی خامنه ای (برادر کوچکتر سید علی) و وحیدی در‌ مراسم @withyashar</div>
<div class="tg-footer">👁️ 92.3K · <a href="https://t.me/withyashar/16428" target="_blank">📅 10:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16427">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64375e3a46.mp4?token=t-4gV6WziH6jyNDpvbCYcQeSOABw4x05lk8-4idaDfevc52eRNxoc3AX-fjd_S_u_Ijhf72oxlmngGcLCPrJqw0UbIR0RiJoDBZPhHlDmFSWL3v8vlAZugSCFVHvBZMLeihfv8Qn0fRb9Safqd2eVHkQYtfCI1dT8qe3j0mrRrOuUzob1Mb746XVsp2Ria2n8ZMxZ0oJPyOjJeesfM-o3Hf8mMfuMLKvARmbXegYnhwE3JNxwiHgqJkUO03j3SsCJ7fCfE_nOU82TKMK0qWG01dpN7BjPmn1vOILvyf7042_2w3QIkRwyHPoJy9KFHSYiFYf7PL973N2jzk1xqkIFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64375e3a46.mp4?token=t-4gV6WziH6jyNDpvbCYcQeSOABw4x05lk8-4idaDfevc52eRNxoc3AX-fjd_S_u_Ijhf72oxlmngGcLCPrJqw0UbIR0RiJoDBZPhHlDmFSWL3v8vlAZugSCFVHvBZMLeihfv8Qn0fRb9Safqd2eVHkQYtfCI1dT8qe3j0mrRrOuUzob1Mb746XVsp2Ria2n8ZMxZ0oJPyOjJeesfM-o3Hf8mMfuMLKvARmbXegYnhwE3JNxwiHgqJkUO03j3SsCJ7fCfE_nOU82TKMK0qWG01dpN7BjPmn1vOILvyf7042_2w3QIkRwyHPoJy9KFHSYiFYf7PL973N2jzk1xqkIFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بارزانی، رئیس اقلیم کردستان عراق، با قالیباف دیدار کرد  @withyashar</div>
<div class="tg-footer">👁️ 93.5K · <a href="https://t.me/withyashar/16427" target="_blank">📅 10:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16426">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">مکرون: ناو هواپیمابر شارل دوگل در پی امضای یادداشت تفاهم میان آمریکا و ایران به فرانسه بازخواهد گشت. @withyashar</div>
<div class="tg-footer">👁️ 91.1K · <a href="https://t.me/withyashar/16426" target="_blank">📅 09:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16425">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">کانال ۱۲ اسرائیل : مقام‌های اسرائیل ارزیابی می‌کنند که طی ۲ تا ۳ ماه آینده، احتمالاً تا سپتامبر، «هیئت صلح» ممکن است حماس را ناقض توافق غزه اعلام کند.
چنین اقدامی می‌تواند به اسرائیل آزادی عمل بیشتری برای فعالیت در مناطق تحت کنترل حماس بدهد و به‌طور بالقوه به ازسرگیری درگیری‌ها منجر شود.
@withyashar</div>
<div class="tg-footer">👁️ 95.4K · <a href="https://t.me/withyashar/16425" target="_blank">📅 09:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16424">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4efbcf8243.mp4?token=E8S_EpPWjwEgziwbhHKAkDGqmuLSjal5Hcgr3ZtIYm0u68rq1I4zxxabDzMsCY7-erG04GImjSNx1WL7h-XxvTx--imZrm2v438FrtzACOsV30N2LYdf6R2_csep0Yu-v_txMz6OqFfRy2ba9KXoi0-Aqh0wJnwL3VJoLaoWvUnkWvRZjnZtfErw9XM6UaJXl8h0hTv9yYAf0T6kBxoXDH5d82yNiWP4R0lqDpMShRHtoh9107QQiWigUBxYQ08fi1SZuhsbD5yCfgtHW_eIWmBWOfC0d5M22ITrX0TLJgtZCK7DMkiF89p27ndah47gVM63MazvRRZialUuIY5PRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4efbcf8243.mp4?token=E8S_EpPWjwEgziwbhHKAkDGqmuLSjal5Hcgr3ZtIYm0u68rq1I4zxxabDzMsCY7-erG04GImjSNx1WL7h-XxvTx--imZrm2v438FrtzACOsV30N2LYdf6R2_csep0Yu-v_txMz6OqFfRy2ba9KXoi0-Aqh0wJnwL3VJoLaoWvUnkWvRZjnZtfErw9XM6UaJXl8h0hTv9yYAf0T6kBxoXDH5d82yNiWP4R0lqDpMShRHtoh9107QQiWigUBxYQ08fi1SZuhsbD5yCfgtHW_eIWmBWOfC0d5M22ITrX0TLJgtZCK7DMkiF89p27ndah47gVM63MazvRRZialUuIY5PRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: ما ضربه مهلکی به ایران زدیم. آن‌ها مشتاق به حل و فصل [مشکلات] هستند. آن‌ها واقعاً می‌خواهند این موضوع را به پایان برسانند.
ما به آن‌ها یک هفته فرصت دادیم تا مراسم تدفین برگزار کنند، زیرا ما مهربان هستیم. این حقیقت دارد
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/16424" target="_blank">📅 09:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16423">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/16423" target="_blank">📅 03:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16422">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">https://t.me/boost/withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/16422" target="_blank">📅 03:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16419">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">@withyashar
🪓</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/16419" target="_blank">📅 01:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16418">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bp0u0QmCVhW5Hvn0j765re56J0Tyxz2lH0Bu0giKIZW-TbwsD3hgeqQW4ryAHxK6R1QNVgmy-EOPGVLb8vI5kQP2efqrTybSiz-YtciHbblFDwYLm1wbZoMlLDvkKecjaHNrvprncQ8pcsU3b29HvIF8-pNntbQk1eCLvUhMaB_W_LktxPhj0x6ffrLxirKKq7Bvs4v60Z7s9HWegGaSxIXmMgZB8WShhc49VzV3yiPXx9AJk1S45FjUPTldPHWf9uEH1fEIbQJEai-efLXK1SoAbxvHHnkDI6YcNVDZV8xCSETrgiuL1UWzGFlosDEAHQHxPSj15EMTYmWf5yLZDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همکنون عزاداری سنگین نیرو هوایی آمریکا کف تنگه هرمز ، قشنگ دارن سینه میزند
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/16418" target="_blank">📅 01:19 · 13 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
