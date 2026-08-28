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
<img src="https://cdn4.telesco.pe/file/Kya4ABReYZsIwWi-6zRoTsVVDH8_sFEWn6hRHp4U7eITzwr1PrQupzNWKMRqCgVp5i6StUi9TFg3VE-xic1TD7l65ez-NIwRp6gMAF8Q0OrkiO6o0xJf7kwZEBREjuCrmMuOChkcy7lSJF-BEuU5eQ5WRUOenKZadkffkIQ1TvQkKsXhZ1pqKb5gvW1oPiE8GcC8QLQ23GTYcwk21WYIBiltOHiVU8tz5q7xg_VOjVflzgr5MzxMn8xhyVm9L2Z6v1RkTaUpdK_g3uka7RIhMix5aG3tKTnq7TD1VXnZbszwcbSRPIH9H29USydH_26m81JEZCTLBwhgBJHGPqTtHA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.7K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-06 17:05:27</div>
<hr>

<div class="tg-post" id="msg-6653">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/quIH2p7q7uulcZXVgtAlhTWLOd5ZQbOUNWCHjnd3E-by6S0gyNT6Vy5NNt4-z4ey-MQjYa1KcGPxu97YjtgKpnFTW8KqETX35tChW8eI2x2oMvoPL6sSjDV57iPpc2OKP91qs2fM3cSUppn4EVQ8_kH4NOpHe1Tyiy7VR0hxHuYeWGer3GX-tjBC6K6vd9XaboS3QX6sKENCV0KFjqu_tXdi75SJiUAu1G9jcC95RZXtKYnPqV7cTb2bHjy4LCKn96zdSSYsjFcBvB6A-VoC51OUpZd3OkThQFCG9xDQYHgeYkojvRAserijl1XmV0304WYGMQQK0xEYjMJjnT-pNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از آتش گرفتن یک فروشگاه فیلم گرفته،
دادگاه گفته این اقدام «مشارکت در آتش‌سوزی»ست و حکم محاربه و اعدام داده!
همون حکومتی که با جنایت سینما رکس آبادان و ترور نخست وزیران و بمب‌گذاری‌ها شروع به کار کرد و قدرت گرفت!
بعد بگید چرا مردم در صبح ۹ اسفند
و شخم زدن بیت رهبری خوشحالی می‌کنید!
هزار بار دیگه هم شادی می‌کنیم
از مرگ و نابودی و تحقیر شماها!
هر جا که تحقیر بشید و نابود بشید؛
از غزه و لبنان و یمن و عراق تا تهران!</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/6653" target="_blank">📅 18:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6652">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_Q98O9pnHv1ov642DEwoJZYqVoCOkr10PfaAAVh98z26-3TbzVXUdOCuabokUwoGUMMP8NjNaZLXs2ZWmHx1dX73OZFvhG4ymeMUmyConsnzfHZy--ipzOUYYMODHi60RJ424KmwxgyCwnVPOC6qtjB4Sm5yFJTNxJ5qAVWGSJ-EHb_42QBqw5tY6QWVX5LGXmtfCboS_RDvTSyAZhFritnHJ-9gaQC5IGvgdexLy52ZwVNKnPw4GbQudRs0u45h8TMAilkR2nNSh0BTwvjXLyl9dDCBkftcZKnBGh7OomOQWr_KDLDKz8e9NVVvNTs81eh2cHREyRYZFrBJM55Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZduC-KD8JriO1xUY_5tEO-9HAp5CMQddPg_JFJOaKUPtJ-BIDo2IwJpHLv07h-ubQZyikFeZhQ1-7Rglru-buWEo2VpiWZCkq1GS27utBcY3s8Yov2r6D-uk0la6cJhYPu06zRNI0Ga2Mw6I4l_vnoqZEdziXFyUhYvFratv0LzQVvyRZCJx-SH1QuqW-dc0cqbmVT_xaJv6Z5Md6l-rluZXPW5fUr4rjEEaOLaPxXu4FdE79Vya2Dj1Qp_oMD8kFhZ8emiL6g46rzjY1eJ1nve__KIw6avFYGf1aeH_RsVsd0tczqsA85lW-KKjY9_4_IwtQNLIWWmqBE0OXkq75g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uDc6gHm4uRp9DV4BHCwmkcsOKqvRPuNeP_zdZla0OrIVFSsr0dhceyweVPiaDxBMD2BHJY1Qs1zFc09wW5YkyIjuCg6DqUBlgKz1whRJoZpJcwhnOJJJkU_NGjUivQrjet_5aaGBeuQDTUmOpquqygEaNXpeaHkvUXo1aMUQZ_N3CQ4ziAoqwWC2N5P2UPtKfYG9WNajraeyAPj0jV4C4LWGnd74TjJDItADrlPitVz8jmISyQhCVHibkATKhXvjrXaIrztnohbgYyW2odWvedggGbFfW_EQDZm7tKtobgOzDfyMxuGFavOBFovTrRoVpmdluwiXcfqsczKDP38VvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lkIQJPm5PxIz0bwAfioqq0r2nhYZGKLwTobwrFzcKdhGr6do_2N3tUd8z9KieBwhh8Rh_r7raNulAbHmqkfNBovMd5FawyTskBy6NC6t8B5YldhQ7q1qopdfTFJM9VxMsxG4senE7PHxwAp8Ky0M-sr4i1scXOfM5Y_dm9HN1__P0609E5vyiG_oExZkwzXK4bNrPxIbuctMphazE3mOP_UNjPy2dMUJsjRXEUb_9ML8DnNSkxq70WnGqnGZnCJfAjDqo_fhzVuJm6A1XSn18JNNuL776Nin-YOK0MsSoCElK1PDtxYSnE8PEhiId1P4QIKkLFIHy4ws9yi4GDcZVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RK7fsiDDyZuj_zGcIv4kiI4VuhOWuJW_DKtJPHHGjNX428ZpMkfXhExBRfqiLrpQJ-K901DoyR9crN-eB_KSqW8jWeQ_EbC_y7av8PN9gEy5or8_HA2mQKHKqdBjtg-icI8ygWVnOmTS2LRuR2xZ7x4qUIjjoPFLDO-GFliMQXQgKk9eaKQFw344Qq1FvSeo9iml1bWSdlfGy8c4yKtqQh0grNEro2B2vFs7_PDqkjsnrhm6HKazXg1N2HXqYfozA5uiz4ogYTXGSLOjO55qTh2YFR3zSYxzhHLa10InI13XuhM8UzoEqWFGAlUY42QIBJaPFNHRnaEDbdqNxx-cgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی،
دیروز به عنوان رئیس هیئت مدیره
دیجی‌کالا منصوب شده!
نام او با واکسن کرونا گره خورده،
او سخنگوی گروهی بود که مخالف واردات واکسن بودند.
رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و برای ماه‌ها
مانع از واردات واکسن شدند.
تحت هدایت رهبرشون خامنه‌ای.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/6648" target="_blank">📅 09:14 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6647">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=WjdPbyMKi7JhMZhuXugceKcqMsKszklly0h7CHtf1Gd7-MWWK_jZfMUgRte6-RjCGz695MMncJxqP7S5HCLOxZIO3dPz9a1x6lAVyuycmSLzVbPhW7icM152xqQL0sggfEUjytlSEh2K65Z2X_kcA5ESsofJIOAwybTu3nJji8W-M1B6GfwvBY7hFlYOznV8KKI0FZMny3i-ao4mcFT7_V_mUC5vTlO6Gd2cVFD_F2J5-4HuuRURt8OI_ChVyw4tLJQ1xTDRqQbLu71m6EfB8_dxfCVRE3lThXLDN5dfET7aIupiGsXe5wVcW9s5Do9orCK2SqzX9_VUuljlnaMKlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=WjdPbyMKi7JhMZhuXugceKcqMsKszklly0h7CHtf1Gd7-MWWK_jZfMUgRte6-RjCGz695MMncJxqP7S5HCLOxZIO3dPz9a1x6lAVyuycmSLzVbPhW7icM152xqQL0sggfEUjytlSEh2K65Z2X_kcA5ESsofJIOAwybTu3nJji8W-M1B6GfwvBY7hFlYOznV8KKI0FZMny3i-ao4mcFT7_V_mUC5vTlO6Gd2cVFD_F2J5-4HuuRURt8OI_ChVyw4tLJQ1xTDRqQbLu71m6EfB8_dxfCVRE3lThXLDN5dfET7aIupiGsXe5wVcW9s5Do9orCK2SqzX9_VUuljlnaMKlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UFQXfdYkxgTrGfyxJQ2d0u61ch6huSV43FVezH0B7bG6cJDExPthH6XTyo6czVONqbhMfdRz5DaMwXt_XTivrsj9gnv9gCgA3D0pv51baUM5JvAWHYoRxhDLmPceo2LJFEYC6ioIjyprFpCz1Etlz3kntaeJzIrwhyykHbt3ql7Iu7ub76NBW_F0gXfVIAoG7pSNVvyCP38Vn3IS_36xvig0dy_ofeILQg3ngIEdDxoBH0_woNWbKz5TRCElJIbThBPMRvM4_HbZAf2l1OJGyPcCUg_fUWlUiU30-MsQPymBoNE7Ve5_EychBWFidUIRGaxYLfBz4w3fsN8XJ5ehzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=ID7qmwQtpeStPX02JQQemH7oQbNDrPxkvlBPo4gBg1rCJ_nT0j2rd_fdMGQuID8-B7CUgVQmZW2CpAtdYJeMMCqCm8IZ-GY9kjMZOSMRV428dDIlhXlizwoZT7BRzur_obP0MC9kcwBwlMr7v3zhvhb4n_Qj1KJ3eb4ToByANVUyjfYeJlAMyIjNS4r7mEMoypbT6vbq50aq3CLSw_yIPWJvEekwjiZdhckjbrdNhxuDSxL0ySHmjukvui9ivhofPvyTLu3ALVApKRTzpMBP4QWpFJkpriemjybWRW78aDhwkBXzTOJGDIzebx3rNc0_3-RTkkpPquHwimYkJffkPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=ID7qmwQtpeStPX02JQQemH7oQbNDrPxkvlBPo4gBg1rCJ_nT0j2rd_fdMGQuID8-B7CUgVQmZW2CpAtdYJeMMCqCm8IZ-GY9kjMZOSMRV428dDIlhXlizwoZT7BRzur_obP0MC9kcwBwlMr7v3zhvhb4n_Qj1KJ3eb4ToByANVUyjfYeJlAMyIjNS4r7mEMoypbT6vbq50aq3CLSw_yIPWJvEekwjiZdhckjbrdNhxuDSxL0ySHmjukvui9ivhofPvyTLu3ALVApKRTzpMBP4QWpFJkpriemjybWRW78aDhwkBXzTOJGDIzebx3rNc0_3-RTkkpPquHwimYkJffkPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=jg-A3RSlKjJ5mGNUOOGVxIxRjXV9UOW83Ll6Q5HycptUm6oVUJrNt8-0xdsztBY5U9YIoEv7hMyalxWBG9Hb_pm899ALHuVaAwZe_hbVlT61yPtSOYt9iT_iEE62_Wjysr8kYxP0X8LkzOyeN5m83PktVjyvOu53Y1neZQBxj-KQRPk0kuf2XScrZtfJYgZBop-RpjIF9dxupi3aPXH9BwcZgfs2nTWyC5QacFZoggdDpCCrVGgyCX0s_RmeNp6uIPqShL_6qX17_BSABCuGzxMq5R_7AbTPr9NK71UsjakC2byKlrkbOp0BN0G2ypvhd5DbxMcavwxUXyc3AcUHMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=jg-A3RSlKjJ5mGNUOOGVxIxRjXV9UOW83Ll6Q5HycptUm6oVUJrNt8-0xdsztBY5U9YIoEv7hMyalxWBG9Hb_pm899ALHuVaAwZe_hbVlT61yPtSOYt9iT_iEE62_Wjysr8kYxP0X8LkzOyeN5m83PktVjyvOu53Y1neZQBxj-KQRPk0kuf2XScrZtfJYgZBop-RpjIF9dxupi3aPXH9BwcZgfs2nTWyC5QacFZoggdDpCCrVGgyCX0s_RmeNp6uIPqShL_6qX17_BSABCuGzxMq5R_7AbTPr9NK71UsjakC2byKlrkbOp0BN0G2ypvhd5DbxMcavwxUXyc3AcUHMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-KcQfgi1E8wgKCYwPQ5Kqhz6QBTiIlFdONhQGgKnPpDVpmIWk_czvbmD2LYjEQIm76P9EQSBU4EPXLTY-_jS-oUHJaZx53O0t5YE-WWavSH3HWWe3_-7LF8C6sh42oXH-jkaeaGB5nWharZdz_BPgGnJ5BzeCpHYjPsPnAteSSt1zyJQDM8GwWkKxAlr2usMlYLjZFXuelsU6eslq-Fs-Fmm7r_GouFB7u-TYS2uCjeuylZhHTfYJbjWJYtmnOawix58WFjTSGnvooJL_pU-3wJirCkxy1DBkpno2T7vlfL2uQbSbjSB1W1vuBNuwazUgEnejA-Dlf8BL4wTCaoeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارائه دومین هواپیمای غول پیکر سوخت‌رسان‌ به ارتش اسرائیل.
دولت بایدن با تحویل سوخت رسان به اسرائیلمخالفت کرده بود و مانع ارائه سوخت رسان به اسرائیل شده بود.
دولت ترامپ اما مجوز ارائه هر ۶ فروند
را امضا کرد و سوخت رسان‌ها یک به یک راهی اسرائیل می شوند.
نیروی هوایی اسرائیل، قدرتمندترین نیروی هوایی منطقه است [برای یک دوره کوتاه، در زمان محمد رضا شاه پهلوی، نیروی هوایی ایران قدرتمندترین شده بود که امام با آفتابه از راه رسید]
اما تحویل این سوخت‌رسان‌ها تحولی بسیار مهم در شصت سال اخیر نیروی هوایی اسراییل است و دست اسرائیل را تا فرای دورترین و شرقی‌ترین مرزهای ایران باز می‌کند.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6643" target="_blank">📅 11:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6642">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">رئیس سازمان اطلاعات آمریکا (سیا) برای یک سفر عازم مسکو شد.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6642" target="_blank">📅 19:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6641">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X8J8sxLtgGao6qrffvT1yHlpIbjS-1Qywkh4gANFda2GfgpuCLStV_VSQUQoynyW8Dy8D7t-Bo94gn8ex4ofYNs31k-ZfMeU_d6ZJO-ShaUZyOorAvekCZxO9oc7ytBSWFvkfXdZV5y_neyRBPJbDekkruXhxhpHbXKrsa6vrJKUA9GvHhegD4dqhmo94YWWSqth3PGDgSEtkm9eQVy33n_qg6dcFJUgWdj8-h_JJB-GpVFyHMN0K3ur2nZQbhZW2pT8W0rSkTmdXEAZGagE5sj5aaA6nFxMXbLQCLuUp37kukz0KYCI9oiTRlFCV5_YhFQCTbpUkQQWxFmS-a2AbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای با افتخار می‌گفت ما مشت
و سنگ فلسطینی‌ها رو به موشک تبدیل کردیم!
همون موشک‌ها و ۷ اکتبر،
قدس رو که آزاد نکرد هیچ!
غزه رو که نابود کرد هیچ!
مخفیگاه حسن نصرالا رو که تبدیل به یک چاه
با عمق ۱۰۰ متری کرد هیچ!
بیت رهبری رو که شخم زد هیچ!
رهبر فعلی ج‌ا رو که از ترس جان
به غیبت کبری فرستاد هیچ!
حالا بادبادک هم نمی‌تونن دستشون بگیرن!
اینها همه پیروزی‌‌ان!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6641" target="_blank">📅 14:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6640">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
اسکات بسنت، وزیر خزانه‌داری آمریکا :
‏
🔺
امروز «عملیات طرد اقتصادی» علیه جمهوری اسلامی ایران را آغاز می‌کنیم؛ هدف ما قطع تمام شریان‌های مالی و اقتصادی این حکومت و منزوی کردن کامل تهران است.
کشورهایی که به ایران متصل بمانند، باید انتظار انزوای مشترک با این حکومت رو به زوال را داشته باشند.
‏
🔺
خطاب به رهبران جهان می‌گویم؛ امروز زمان انتخاب است، یا آمریکا و یا جمهوری اسلامی.
‏
🔺
هر کشوری که با ایران تجارت کند، خود نیز منزوی خواهد شد. هر کسی که تصمیم بگیرد با ما همکاری کند، سود خواهد برد.
‏
🔺
به عنوان مثال تمام شعب بانک «ملی» باید تعطیل شوند.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6640" target="_blank">📅 21:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6639">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6639" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6638">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=EdsRmrhvcMhh3R5E14ZnozsLHkzHaXpVlnMSAjZCCvBN6L0cWR5SSgHv5BYApe396EdZUr3TESyPBaG8IfKoshSKCTeUY-8_fDFu2OaKbS_02uhWwSCtN7haor90uu8IEwcPEjTv132BhBYVKrJ0EsYoPR7d-O_SICJniulDHJjgWMKVF_KbBA6_calQ-DwmkTkQXUVFWDlF1fHn3asoH288Ovzo66uGunfwgQic79hiJX5JRdg6hbqoYp_vMc0HhGe2UTfUm8j5-dh5RDD682jJAW3M5OlCTs_1aMITKKqQX53oIo40nVx4TpeZWo8UHLsKvgqx3YQIxmEQK_cgUxkQ_ExWB2S9BZ2JiHDG3QAHsWckQtzwhVeYPb006mzmkEHMXiuZtlSk-YeyuTMOmnOLtOg5SXFEycVuZ5gnQNfBLZG-R0u2DQwlQ7t2QMyBBoBI-gIkObzaT8ZYv7p2jW5KJoJDky4LqsGEMKSoztcMNh8FMOG6YHWVegMGU78nUiKjtMSWj54PKhctb0WR5VWRT2bbBXh_zj0tAKRiRwldeSErbdk2BmfBaf6uko3KIBrW59RBAgY0fu3dDCGvyNXY_xSGSijGJCZw2A0bvkKQyLix4UzYZRwfJ2ihuNfdtFgUkdLOmMF6flHaQGpoeNpg3Va6g9FbcB1-XZSkCdo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=EdsRmrhvcMhh3R5E14ZnozsLHkzHaXpVlnMSAjZCCvBN6L0cWR5SSgHv5BYApe396EdZUr3TESyPBaG8IfKoshSKCTeUY-8_fDFu2OaKbS_02uhWwSCtN7haor90uu8IEwcPEjTv132BhBYVKrJ0EsYoPR7d-O_SICJniulDHJjgWMKVF_KbBA6_calQ-DwmkTkQXUVFWDlF1fHn3asoH288Ovzo66uGunfwgQic79hiJX5JRdg6hbqoYp_vMc0HhGe2UTfUm8j5-dh5RDD682jJAW3M5OlCTs_1aMITKKqQX53oIo40nVx4TpeZWo8UHLsKvgqx3YQIxmEQK_cgUxkQ_ExWB2S9BZ2JiHDG3QAHsWckQtzwhVeYPb006mzmkEHMXiuZtlSk-YeyuTMOmnOLtOg5SXFEycVuZ5gnQNfBLZG-R0u2DQwlQ7t2QMyBBoBI-gIkObzaT8ZYv7p2jW5KJoJDky4LqsGEMKSoztcMNh8FMOG6YHWVegMGU78nUiKjtMSWj54PKhctb0WR5VWRT2bbBXh_zj0tAKRiRwldeSErbdk2BmfBaf6uko3KIBrW59RBAgY0fu3dDCGvyNXY_xSGSijGJCZw2A0bvkKQyLix4UzYZRwfJ2ihuNfdtFgUkdLOmMF6flHaQGpoeNpg3Va6g9FbcB1-XZSkCdo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت دست دارند و اگر بخواهم دکان آنها را تعطیل کنم، شیشه‌های دفترم را خرد می‌کنند.»
🔸
در سال‌های گذشته آمارهای متفاوتی از قاچاق روزانه میلیون‌ها لیتر سوخت از ایران در رسانه‌ها منتشر شده است و برخی کارشناسان بیشتر قاچاق سوخت در کشور را سازمان‌یافته می‌دانند و برخی منابع رسمی انگشت اتهام را به سوی بخش‌ها و نهادهای دولتی و «خصولتی» گرفته‌اند.
@RadioFarda</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6638" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6637">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromeuronews یورونیوز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uK5u6XB_T_eV24in1yBq2CTND7aF8p-ukEt56pSkoYIUhFV9iZ1EPMyzhKVI9fkihm362Qzw1m0fljxMKW-dsUm04Ji-EpDbFCYLJyIj31d8HqWNYonPloTV9UQl-SbAE6zETvFODQA_u3vXQRS_yjQVrpG1qTPZd8856RD4fvHtwnB7rUBCp8APWy8a3YllMoLGezlWOYU_2h5nw-_qoDZ29cdV7RO9EOqnG5kRY4t8Erb-_zbqDjQvo8k9TVapJwuhvycVt6I_VTj8ltDQlMKPLFQdThwKjbEzkDckta6K3zYk0Da59NYsV0nkcEoYr3FM4Nvsu9a8CBCkBiNGHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
جایزه ۱۰ میلیون دلاری برای کشتن پسر ترامپ؛ بارون ترامپ هدف تازه تهدیدهای تلویزیون دولتی ایران شد
رسانه‌های حکومتی ایران در ماه‌های اخیر تهدیدهای خود علیه دونالد ترامپ و اعضای خانواده او را تشدید کرده‌اند. این تهدیدها از انتشار محتوایی درباره بارون ترامپ و ادعای دسترسی به اطلاعات رفت‌وآمد او تا طرح انتقام از رئیس‌جمهوری آمریکا را دربرمی‌گیرد.
تلویزیون دولتی ایران در تازه‌ترین تهدیدهای خود در خصوص گرفتن «قصاص خون علی خامنه‌ای و برخی از اعضای خانواه او» از دونالد ترامپ، ویدئویی پخش کرده است که ظاهرا مسیر رفت‌وآمد و فعالیت‌های بارون ترامپ، پسر ۲۰ ساله دونالد ترامپ، را ردیابی می‌کند.
در این ویديو ادعا شده است که جایزه‌ای ۱۰ میلیون دلاری برای سر کوچک‌ترین فرزند رئیس جمهور آمریکا تعیین شده است.
این ویدئو تحت عنوان «بارون ترامپ را کجا و چطور بکشیم؟» در رسانه‌های وابسته به سپاه و همچنین شبکه ۳ تلویزیون دولتی ایران منتشر شد.
جزئیات بیشتر:
https://l.euronews.com/UtiQ</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6637" target="_blank">📅 09:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6636">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=VPIRC-tswRP2rH1jvo2JZ00QwJXWZ17hITWDPRM0eMnfrot9oKJDmbnLqR00obC_XcGoVvihNTMC6C1iJW4_TxrySDc1HpomoVsQUtsRfjRygDqnY4FmP3Gl4FGgCMhpyNJY6oUp1YXj_LYBDwuBYT8WwhqTRC4itFkBvCJKBtvxBeqDaoZvU2fXOVmYKbJ30Y3hd7icUFw3SUspTqi01CZmMf4DXiGs3S4_mdcr_rvrT9dS39XLUzS0fkPpDUF54J-kSZpS7Gd_vr5fdyerpww-oB746Vvd6vdgoxFBSXzMvP_0YY4oSBCR3fDWdoN7JUjoiwTRDyYi5WLGfvJkyi0izkTarN8jCfyn_2l7UiJc5mbcRpYSlx5doy0jqxebGb-sd6ukvTLbCZKQe1rnClEqRDeNA4qIMqQgI-rJKUqGdTGI0wExs_zaEsPrahEQ4hpVtT73Glyshi9cqJ4OgQY54rLJqw3XgIQYQp7xruoqCYzLauLX49DOt4CVCXZiPbvwNIiI2uKBe9MNWY4lpemgOyrTTqWc3w8QrIVkze1x67DvGzkvE-o4AIh-3V0rsE_kdzBTKhtF_ie0BBravsg_zYTAxJTCV0wZqSofpJiY0OBlw3Bo0efHAJvuWurJ8DIepdIk1-4py4OLllQmAiwF7ZgmhnYmyYUMvC04hsY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=VPIRC-tswRP2rH1jvo2JZ00QwJXWZ17hITWDPRM0eMnfrot9oKJDmbnLqR00obC_XcGoVvihNTMC6C1iJW4_TxrySDc1HpomoVsQUtsRfjRygDqnY4FmP3Gl4FGgCMhpyNJY6oUp1YXj_LYBDwuBYT8WwhqTRC4itFkBvCJKBtvxBeqDaoZvU2fXOVmYKbJ30Y3hd7icUFw3SUspTqi01CZmMf4DXiGs3S4_mdcr_rvrT9dS39XLUzS0fkPpDUF54J-kSZpS7Gd_vr5fdyerpww-oB746Vvd6vdgoxFBSXzMvP_0YY4oSBCR3fDWdoN7JUjoiwTRDyYi5WLGfvJkyi0izkTarN8jCfyn_2l7UiJc5mbcRpYSlx5doy0jqxebGb-sd6ukvTLbCZKQe1rnClEqRDeNA4qIMqQgI-rJKUqGdTGI0wExs_zaEsPrahEQ4hpVtT73Glyshi9cqJ4OgQY54rLJqw3XgIQYQp7xruoqCYzLauLX49DOt4CVCXZiPbvwNIiI2uKBe9MNWY4lpemgOyrTTqWc3w8QrIVkze1x67DvGzkvE-o4AIh-3V0rsE_kdzBTKhtF_ie0BBravsg_zYTAxJTCV0wZqSofpJiY0OBlw3Bo0efHAJvuWurJ8DIepdIk1-4py4OLllQmAiwF7ZgmhnYmyYUMvC04hsY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتراف به جنایت در سوریه</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6636" target="_blank">📅 09:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6635">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6635" target="_blank">📅 18:06 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6634">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6634" target="_blank">📅 17:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6633">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PhT8yltWHxgt2hmOpofi3FTfj5Rzav8QNNMYEqsDzyHO3H6l_moVlmNo20OXE21LM3B77VqrRf66V7B2sltdDKnhG0S5nmRRXOhb6eeXggtxOUzUTsdZm75-5dHB_-RFLR5-_4wR8LK-kF9U38QZkyDorJo9iQuF-rgtK5npHKFMMczrxpJ7X50C9TBitl90_otfhX7UreENmhV9UdWr_bUqUxZ3HGNr2-K9EhKchsinGU8y67rIXZieaWHbXVL8NM7hXH0sSPKRy5qHI5iqLkrNNCdn3n7s-G2VAGw64fJ58i79beeDnov6Sjf3tWPqQjn-Yu2X9i0xbqyS9_0xSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vka4XW7fJtGlvdXFVITg6ocU5UA49RlT3C0S4O1mvpjIH-at358dTi65_g96sVEFH1ZvldxjKhZghFyloMBB-h7MhlJZs3UifHsMQnrhSi_YDGCMlvFE31hZoNLTqgzvN6HVtirsaUYbdTUi1ac4TN-pswTdbW3uBPjvX2IiJYYJxi5y6dTH5Wk3_PpMM5HvLNq0ScpPWG4SAufzifTyCBm0uwYVm1Xa7NmnBs7bIny_gWI1CizVdGj8vLHJOPCvztVQ2E6wDNuA6iukCRuvyYj022Qd86EJyGDkita3ZTg-2tz9EyV-44-lZZXXQgcNhEeIT5p_d8TEe32z3b4pqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از انقلاب ۵۷ و از آنجایی که مبارزات ملی شدن صنعت نفت، اساس و پایه «ضد استکباری» داشت، روز ۲۹ اسفند رو به عنوان روز ملی شدن صنعت نفت ایران  وارد تقویم کردند!  ( از قضا ۱۳ آبان و تسخیر سفارت آمریکا  هم رسما روز مبارزه با استکبار جهانی است!)   ولی آیا صنعت…</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/farahmand_alipour/6632" target="_blank">📅 20:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6631">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">مصدق برکنار شد،  چون مجلس رو منحل کرده بود!  اقدامی که باعث شد یاران خودش علیه او بشن!  مجلس علیه او بشه!   مصدق برکنار نشد به خاطر اینکه نفت  رو ملی کرده بود! ۲۹ ماه قبل از عزل  او‌ نفت ملی شده بود!  این دعواهای ماه‌های آخرش تماما  با مجلس بود! مجلسی که خودش…</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6631" target="_blank">📅 17:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6630">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">سرهنگ نصیری  وقتی مصدق به طور کاملا غیرقانونی  مجلس رو منحل اعلام کرد،  که فقط در اختیارات شاه بود،  شاه نامه عزل مصدق را داد دست  سرهنگ نصیری فرمانده گاردشاهنشاهی که ببره و تحویل مصدق بده.  آیا شاه حق عزل نخست وزیر رو داشت؟  بله! طبق ماده ۴۴ و ۵۸ متمم قانون…</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6630" target="_blank">📅 17:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6629">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rJQtzklbWEJWbGEefnwigM48tCLtWkZTujdnYIm_rRcK36V23lNyGtyjOk3C3K8T8YG4lmlFEpH_VTQTTMuM1edC_Vllabb_guGO37pKTnvgTJFeVaHiqwgPEpuOYknSiCY7xDi371nQiFiysn880kdey7S0BC_7FLIGvwb56LamqCs5xoFI5EdwR-PYshV68GG8ravNGvAix44BgOWkOjIbGvifrFrtNNNo8OHWdeYBO29KsPWRcj41G-vO-KrVJ_BXCPItK9R_X5ycUHTN0TosXYL8S2-A063JZzrzoDBVt65If5V5wfEjY4uP6HLhMoHlF_a1A_A_G5iyZTSGxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد هم یک انتخابات نصفه و نیمه برگزار کرد و طوری انتخابات رو جمع کرد که تعداد حامیان شاه در مجلس زیاد نشن!  و مجلس رو با ۸۰ نماینده بست!  شاه در عمل مانع این کارش شد؟  نه!  رفت رفراندوم غیر قانونی و مضحکی در کشور راه انداخت و مجلس رو  به طور کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6629" target="_blank">📅 16:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6628">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">مصدق با عنوان ملی کردن صنعت نفت  (که در عمل هم رخ نداد! و سال ۵۲ رخ داد)  کشور رو وارد یک بحران عظیم مالی کرد!  شب و روز هم سخنرانی می‌کرد که رضاشاه راه‌آهن ساخت به خواست انگلیسی‌ها،  مدارس زیادی رو در کشور راه انداخت!  (باور می‌کنید این یکی از انتقادهاش همین…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6628" target="_blank">📅 16:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6627">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">اینجا بود که نمایندگان شاخص مجلس،  افراد ملی‌گرا،  چهره‌های اصلی در ملی کردن صنعت نفت کسانی که تریبون میدادن به مصدق و  مردم رو جمع می‌کردند  در خیابان‌ها در حمایت از مصدق،  فردی که خودش مسئول خلع ید انگلیس از صنعت نفت بود،  شروع کردند به انتقادهای تند که…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6627" target="_blank">📅 16:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6626">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZHIfjcfGgaYxmF6_3Re0wqj8Im7mCrNP0cpgPiL6XoBbpmrm9LCo1if9jC7NMfKf_U7PRKjZxJ6IOobT41QpaAm51Re4tewejC6hmmhNMK-UQp4TRSR8EJpHIMuD4vsSu5XHy5JOQnn3zeaNQEnXXlHti64En--KjoimYB6GAf7Fz4o6vBNkEfQMs3tvlae6UeINViZv2BQZQ351qOyh_GctszH1o0v6iyKJveyZKtBJBJglWmZjpXReM0jtqgTdujjOcuR-7o6qVUzAahcsLPYYYeoUWZg3QJ2bwVkXV4kQ08TOtFgrvWNTcTe_v1ppokTpeMOsAA9_umX-k49pvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینکه مصدق با بیان یک جمله پوپولیستی که «مجلس همان جایی است که ملت است»!  در یک جمع چند هزار نفره،  رفت به سمت بستن مجلس!  اقدامی که اساسا نخست وزیر حق این  کار رو نداشت! و فقط شاه در مواقع اضطراری حق چنین کاری رو داشت!  ولی مصدق چی کار کرد؟  مثلا قانون رو…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/6626" target="_blank">📅 16:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6625">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gy-pcYDPX0s7ctf11AAZdVJb9SowPzC1Kajwv1kEcSw4BqOLJzYmv-hLlRmWEdCU5NM2kSvuqkK8RxHu3ii_77R2O7aXiv2vJLAnP8uSVS8llB8Pgx-mfeOQbqoUwKITFjdM_Zrr07Mn0E2fOqQhv4gnoFQCWD2GRN98FLxPgepsWQwI8qIewGioUiCHmhYyySgh8oMda4sPWh-5qqxktiNowyIM8VPSizZjdDn1aL_GuW9PBxqt6hOiaAr_EVrYn1uTHF_jiegXgE6Zv4PkfHkZjXM4nUoZgZ4EywIoYLyJbLjEOqDS0JQ4iLBiHvzTkgxh7ZXAr4a72BDtCtw4qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون پولی در بساط کشور نمونده بود،  مصدق از مجلس خواست که مالیات سنگینی   بر ثروتمندان ببندن و زمین‌های خوانین  و فئودال‌ها رو ازشون بگیرن!  نماینده‌ها مخالف کردن! گفتن کشور خودش در بدبختی و بی پولیه ما این مالیات رو هم ببندیم و با خوانین در هر گوشه کشور هم…</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farahmand_alipour/6625" target="_blank">📅 16:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6624">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O3J75Qwlzd6pdaId1j2IAAjjexAdULpt4sf-tEuFBy1Rtmr_LnhLEgLi-gllsM4uMK6WWpHqASPeykY55uiiW8TbBW2J3mcUGrM6JvmVoKx98DjloIfBZQQoVkDQCb_XWTIsRgZBO1I0BypRL2szs9B1E-g_ZtsAwzMfoMdkKcQTnFfYfj_yDXpTgu4ii4As2KN-mHgiG9rp7zn_VlgYucI3HDWHi_vDnakcxhgwfd8Rww13YN5dFOB_i_QtM-D-AoBpwyy0U1tNDNmV7pfNspc9joCcM911BhZjTp4m8g8q0qNhETt9pYMwhuEiP0Hd4StkCWW-pODsR6UkWnkE7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفتند نفت رو ملی اعلام کردند  ولی فهمیدن نمی‌تونن نفت بفروشن!  چون نفت نمی‌تونستن بفروشن، پولی براشون نمونده بود! وارداتی انجام نمیشد!  کشور دچار قحطی شده  و گرانی و تورم شدید!  حالا مصدق رفته بود و از مجلس درخواست‌هایی میداد از جمله اینکه  وزارت جنگ…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/6624" target="_blank">📅 16:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6623">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e8QOhZQ2HM40Dd-91e6lzDRvqX5jpEOLqb4iSa5dIHQfGbaKyB3vkQlu3xN1vflT41EPohhDn9WAPr6uBvVoUBFnO5VtA2Bo65vvhQt4P6uQG9WKdnklqQuZQgsGkedbq7lpi5QkRFswLhwxdFQDCk92cX36-7kYcPmMnI-T5RnCvskWruMXfL2oEFqwaKGzEhZI6nfgnrXh__YICtuuZdyyqUq7fhoEWNiFQZePHhQDOqN48KqjpDtUvAHVIsWFx354bZjUZFE7Zfb0yg7ORLk6JkIrpNxx-Fi9ZPogi5AswbfvAz3VdbXDtPRUBSkiSbzy9hPd8ODCXCkglT9RXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدق به عنوان نخست وزیر اساسا  حق نداشت مجلس رو منحل اعلام کنه!  بر اساس قانون مشروطه،  این حق فقط و فقط برای مواقع اضطراری بر عهده شاه بود!  اما مصدق چون درخواست‌هایی از مجلس داشت و همین یاران خودش علیه این درخواست‌ها ایستادگی کردند،  در یک اقدام کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farahmand_alipour/6623" target="_blank">📅 16:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6622">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L5eYFIH8MkFeJEd9-T8lycz8tWq4J3GtJIL02ltJGb5lkko_AlNCCHVAWA9j4EuufPuFTPNL0siky__nQ9CbOoYr2UisXFSYwhqsHzSLhCvImaM6n1rVtV7g3-QgLOGJ4b1z6Plxw1kcRiaUyLvxPD3zbdoPep23CAboHCr2q2iENUs6lyATnK9g7GCHEyPPKyMr71le9YqD7knytk2OkN2-fJRgFnAtd599KtXlLPaBr58eroWoPkN5mlcpsdTtWjHF9R41A1QxpffMTtNidyU0eZae_xpHVpYxl2N4sC_PQPhdtjXirE0XPqK4VvBLeQeEUM2fC75zsh8i53EWpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سه فرد که نام بردم  و چهره‌های اصلی حامی مصدق بودند  و نمایندگان بسیار شاخص مجالس مختلف،  نسبت به این نحو از برگزاری انتخابات اعتراض چندانی نکردند!  مثلا مصلحت بود برای حمایت از دولت مصدق!  مصدق به روشنی برای اینکه نمایندگان  حامی شاه وارد مجلس نشن،  انتخابات…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6622" target="_blank">📅 16:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6621">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vSm3bHYhx4_Hv12zcMN1An04PMsUVHUfMRY4XhauiS_B1NAS2ZUsqrpZlINVYzwJ0zJT1eMlL7toGFS--WDK7YP5kU-JmDh6mNi9caLjS0pyvwGKxXni13madC_u5vUwyCheFtC-VZdAIGIDMGhGWJSiaJIJqStpOuNccvf-WDgnEjBUGd8SVzMKNXoUBrETHRycsUc0Wb7rlNYMFwF9OuBiUWXqvh74EY3R-NIyoIIck3gLvlN8P1HOf_MBXGpiAzHkzdDyGWbCXA4H2OIVYhnMHIndx0fEysbZe47ICakoAADV-LvZ8Uv6SiMfbLsO39nOixrcKJ2QE6w2uhdrLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتخابات مجلس ١٧ ام رو چه دولتى برگزار كرد؟ دولت مصدق! ولى همينكه اسم ٨٠ نماينده مشخص شد، مصدق دستور داد انتخابات متوقف بشه!  گفت براى حد نصاب جلسات وراى گیری ٨٠ نماينده كافى است! قاعدتا بايد ١٣٨ نماينده به مجلس میرفتند! خيلى از شهرهاى ايران، در اين مجلس نماينده…</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farahmand_alipour/6621" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6620">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gdAgz0VN4K8-5Bh790mJxsedV3Qo2sVCnnthjSBHnIiHZOaywR7sNF86a1GnXgueuE_I-HoI5R91TGaSbSs-Aj70l4NppL7r7Ab3y7hZHSEvhrVXRz1u_Rio-M3phTnRsrM9nelPGgQ68fj3ydmDnDTt5HVK4okZ4oS0UBp6OnGxb5jTxdcIhTqT462WkVTWIHZ_xyZO5NPZfQrBw00b1n1XORlc4fMfKuIK1FncZP12N_STv6tnMl-AHrvKKHSpezx52GUvv2rUPfdgmvxDEWxsg-nf2ITLBR8OkhgHkOFNeEnWKa37RTBpb-k27WKw2LjwUMW5FXV9NhQtjQZYGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا ملی‌گراها، چرا نزدیکترین حامیان مصدق و شاخص‌ترین چهره‌ها در ملی شدن  صنعت نقد، علیه او شدند و از «استبداد»  و «دیکتاتوری» گفتند؟  خیلی کوتاه خدمتتون توضیح میدم!  با این یادآوری که این‌ نوشته کوتاه  در مورد بقیه حامیان مصدق که تبدیل  به مخالفین مصدق شدند…</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farahmand_alipour/6620" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6619">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lu3wIJvDs1qFzlv1v6QD22bAk15O6lK2htM_JohcqJDbHbEFhI7CnEvCOQObZOoK8jf32uvCsGu_W_EhaRuccSkAt7sb4vkoVQB7IIc6aUyrumVEPk2URYq7sn_8Y1aOzxAYAuoBW02rxCYL6UDjF_EPEu4Zr9NHcgT-Cpmwnx25jZF5WKZpPre02FYOER0Ro7Qd1iMw5lLLPWVH3K13JDXmsp3ePQEh_DFantvdzjvwCivLuaJ2ypMo-urN-4Hp72Y6I0MZ8ycVoQ4YzWz1ZuEeqHsWieZIib031LrPZ9UCUN_uVzhPGOwqH6RNvZcIdNU4ZpbUDFMO8RSDdJVcdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حائری زاده در سمت چپ مصدق  حسین مکی، مظفر بقایی دو چهره ملی و شاخص در ملی کردن [ناکام] صنعت نفت، تنها افراد شاخصی نبودند که علیه مصدق شدند بسیاری‌ها بودند! از جمله «حائری زاده»  نماینده شاخص مجلس،  از حامیان معروف مصدق که علیه او‌ شد و مصدق را رسما متهم کرد…</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farahmand_alipour/6619" target="_blank">📅 15:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6618">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FoV6fMf37LDjS08Z_sm_L-KOVsOD6AJNA-RSNSWh_-vaCn8TgtRl_nk1X_OuKLrRx0wiQMkLT8HSp0zV1gKZYs5LwgnpNJX634CRgV19AVyMLwk09DDMyhN9rPeE2-VI1Nu9_3goyixFelIh1hh0VrZrfybRa_RgLrfYQToy9m6cYqAkmYnPmZ3cpNmCy2hpHjVQJAk4gCWjZ5c9VXJZDk_uzRUXQeLY52ZAZymhSEp2q0-shHLWm4sF-UMzQb-1eXMv_lCcSB6EC9mHMqBFVP8wgbKTcnEiUo2M5EJP-g07xKC9Xx9SWvEZh1D4BGlIbtPwYeMNZdhpViD0aM7MvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه فقط «حسین مکی» که «مظفر بقایی» دیگر چهره ملی شاخص آن زمان،  همان فردی که تظاهرات‌های مردمی به سود  مصدق را در خیابان‌ها صورت میداد،  همان کسی که روزنامه‌اش (شاهد) مهم‌ترین  تریبون  مصدق و مصدقی‌ها بود،  همان نفردی که نیروی فشار و چانه‌ زنی در خیابان‌های…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/6618" target="_blank">📅 15:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6617">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gF16BZi8ZcQvrL3y7jW0lWKdSkNBnDWI_SC0GaJ7BkehIsOoSVDlBLSsYFEH3SxqfMXviiME7_IzmTAj1kFlzcAL9u1Rlx_finukS2ewpDN6XlZpEC0M9xuT-qOHt0WTc93tRJk30bhbBaJ_MlniEQRxKYvvt3dXHa3QHCbeaWc-YnBSxzsN6vQwSqJN7YI69XJtxTatsrdkwcELGXxMToEnoqErUbKGB26uQzhI9IsqvTLhFTBl0HJbfYLzbnrpxq4ZahEFUPAPuDYoFwEZabXH5GNo_wv56FCVSWVeWHqZ9FGEm_EcLD9-nS_d0sW7ou9aQuui7ZDrl3vy5CLRNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند  «مصدق علیه دیکتاتوری شاه بود و شاه علیه او کودتا کرد.»  ولی یه سوال! قبل از اینکه شاه حکم عزل مصدق رو صادر کنه،  چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟  بله! یکی…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/6617" target="_blank">📅 15:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6616">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dqflPYYwgXbUspoFg8GAfrMfe2U0VykrOAqym67qli9jruKecOCL3vWOBBrHvuF1skKfZi9CfF7c4qo3Y0sz6CLv5XWU93sb_Vdc__QqZc4oOii_O9epopSZ81PiMjlFjku2FKLl0Rcwxy3LZsaAS-ABLXbYAV-VBkAvfprgVmhfP1T2II_XZm1WmPsep8gAh_6BClYj11vOD-_Ypg4Ysyxf3OA0AkLdkfWv8s-Nx0lWslGqc7MwMf976VCompqntdcWDZAq8AEqHwB56kr70h4meYlbkDtXjnkDxgcdTPmgUWVrQD8PsoAdCnTQ2AgPQA16ucQFI57qgmI6z9SRag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند
«مصدق علیه دیکتاتوری شاه بود
و شاه علیه او کودتا کرد.»
ولی یه سوال! قبل از اینکه شاه حکم
عزل مصدق رو صادر کنه،
چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند
و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟
بله! یکی از آنها «حسین مکی» بود!
او نماینده ویژه مصدق در خلع ید انگلیس
در صنعت نفت ایران بود! به او «مرد پولادین» دولت مصدق می‌گفتند
به او «سردار ملی» می‌گفتند!
او دست راست مصدق بود! او مسئول اجرایی  ملی کردن صنعت نفت بود!
اما علیه مصدق شد! چرا؟؟ چه شد؟؟</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6616" target="_blank">📅 15:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6615">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g81Znu6KcuPIJLPa_3ZhAn4TslZgHvUuSTm_TTsgD9TdMwpIcHs05qXjRijVrSQ77O9Ad1NIkBBwQAOQ6VMEOCwE-yx8KWcR82uLfgwto4UEnPagYiHEIFnWjcZy3qCcfKH9mdt7UZ4ncwDRLoi7WjH8sleWXaKVgmdApU5Shy--DIXlG73ks-LYZ4u006V7WzEgCNkYLBpGjUaz9KHL8oHUJ0dJGgiLhkwxgV4SMrQSSzeDam06YlN96pGxDordWpbJdaITBBORJtHnr3RHta7KciyYJOOVdntJIF_87hwGMfQ6fh4RPrbsB1kiWOiMJIwc2TL_6lVlLsO1QMLfCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از حمله موشکی ساعتی پیش
جمهوری اسلامی به امارات :
وزیر امور خارجه امارات با صدور بیانیه‌ای اعلام کرد که تمام معاملات تجاری
و مالی امارات با جمهوری اسلامی
متوقف شده است.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6615" target="_blank">📅 00:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6614">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B6Tjt-TTM1k4MsYs5A5NtSj1VGrvr9c613CBsElAWx0FUIH9B3l7fQcGFPNt-oWryJXbssPDKeL6w_wc2WEb_CDFZRyGGImAEdJdKKjJM-XzhoZoRTaWLs53tnLL4HZ7tXWJZlRUCR--pyQHwYT8Lnddvp1x50BgUWa2npvC5szTBEmXr7CiBXaaVJ4qkOCxJ9CchIH8d-tz5pG2OPZYi5FkyfTU0UAmU9x20wzW8VYMLd5es5zjQKhAbylT1XI7G10tcYju_i38i7XsnSlTxtz4Ix2cZx7A8mcpZ9aTtbxMU531CNDK4LtgR70X61PnivQQ2lrt7iO0BYh79GXYDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخشی از درگیری‌های خرداد ۱۳۶۰  بین حامیان خمینی و ملی‌گراها، در واقع ادامه درگیری بین مصدق و نواب صفوی بود.  هر دو گروهی که ضد شاه بودند هم در سال ۳۲ به جان هم افتادند هم در سال ۱۳۶۰</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6614" target="_blank">📅 19:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6612">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KlgM8sXNxdEaQJEqxu61HTu8mBs2n3W_n9vXNs_-IL2EI7bKxBf32YT1gYy805ePblGilUICXFf6oOQoOgTfWtNNH2juP1A-u0VY0Jwn7fT2JHvRI8GSFOYj896vSwpJNDqmVc6N7mnRaZVQnF_5kKLMJ68tc3xRovUUEhNLfqgwklrIrTx4CMcBmqI0vUC5XAumDKMwBbbpHPwjNRUS7nK2bBatSeFUbZaFSKOXJal3ZXTimXtVO_B51NEpaxwSFxxt3CRkps6_1mBuNS15KlMevDHWJVm1aWgFMW66N1tdWoO6pHAghPA1cDyflqxwKasjVAwl3FyWBiKiKHEukA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lQ4xptC6uiLe_4N9kRp0ETcgEZ4ngTFRUySt_0YMeM4Sx3qVkG1dTzzMHnz5wIALA0NLzmf5IfRjBwKekJQj6Fws9WmHbCi7Q7UL7E_JCkHzZG25-kabo8faU5KMja0SFHnUht0MmB54NJfWTO67QKNWgqrKyYgiFOuzWglptW1HCDys_mJCXKvQXnKa2JFPJbExrxJh5cC83f302-3QKEXS_kpK0Mb65qIjcMzIgckZGq6T92A99000uXkXt29ZSI30iM2F0IEO3eWk9UlXI5cv2n4KXJ0WjHnWVoup0cxUmmXahVSLP0FsEvl7OOY-bGBlucR15RDVXgM_SkK4xQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این نفتی که اینها این مدلی  ملی کرده بودن رو گذاشته بودن توی کوزه  و آبش رو میخوردن ! حقیقتا!  مثل همین هزینه ۱۰۰۰ میلیاردی برای انرژی هسته‌ای  در ایرانه و خاموشی برقه!  هیچ درآمدی که نمی‌تونستن داشته باشن هیچ مردم هم چنان فقیر شدن که ظرف چند ماه از شعار «انرژی…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6612" target="_blank">📅 18:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6611">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QRZ50sRr05_jzZez9HUlpj8E7sNh6-6iWDKs_5UFbI853TRnQpt0Ydl1x2R2ObNLLsmAKy0jKmKzgqznLbM-ICidyCAGmaUGARvetpdMp0WOPAe96FGoMHyvs1QTlxHfhAE6uSthBbLrmtrtKQjy9298ARRpYYt7WPLKaKo0VS74nUfaaEe8pgAsxLAGGReTgK-k2rd6_gCRGWTZZwGr5ZCQx2ZWgGFojb4BEKj-K0Zvl8LpizSTuE2I55khZ89oeesWj8XBVZHyAdIWYfzo6kP3pDhES7ASUs_Tv0E3K7h7MuaiLwf40xGe_luLy2e3OuTDWfgrO9NXqa7Caya_IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران به اندازه مصرف خودش مواد غذایی تولید می‌کرد، ولی مشکل این بود که تقریبا ماشینی برای حمل و نقل وجود نداشت!  چون پروژه‌های عمرانی در سراسر کشور تعطیل شده بود، بیشتر مردم بیکار شده بودن،  دولت حقوق کارمندانش رو نداشت! پول نبود!  دولت توان خرید گندم و…..…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/6611" target="_blank">📅 18:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6610">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kSJ9J8aF7p7YdMUqB2UiE5xUyRbmjYTBn08omRqJ6aPna8kSpdBpL9ifipREwu9RbznYck9NfKplyDhPXDQUjh1Lkt1qr9UdNPIDFfqBlBNbmWcu2eEUogySWtt8ZuhWdbHPifGe5AqtLYWOuz8r5igV-JTIIxUgh2P0_ed_K2twz9xCzwpARoU3Qejj89j9hNtjQkuOKNY6Ew8mllsGecgWVyVHz5VHfgqf6_eYGuUCfakRmrGVFj3czx5zldrT2cSZ_yfgbfnjX-GQ5wEVZqCiPfXftXKQYDqNYZGcaF6oMcNh6k9oUymUZ66uritNN6hOmiFXhBOCiTkDRBqXIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران در اون سالها، کارخونه و صنعتی نداشت!  وارد کننده «همه چیز» بود! دارو، لباس، آهن،  ماشین، سیمان و همه چیز!  ولی هیچ‌ پولی (هیچ ارزی) برای خرید کالا نداشت!  کار کشور به جایی رسید  که دولت مصدق اومد گفت اصلا فروش نفت رو بگذاریم کنار! (اقتصاد منهای نفت!)…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/6610" target="_blank">📅 18:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6609">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F9Q0jQ3MKkd8ir-eshliTdhrtBkobuiM_7BXDzreODUaT-yIFUYud_thylhYMLkxVkw8vp2b579cE5QlSRKAfB5GnMnNaSN1YAgHq5YLrQYBaWBR6f1RcUlGjzuAEOK4vdKkQGM7DX83fkUFfhvtrHsE6n-iQLd4_hOyJYF0kxvA5edxFuCXfETumT8HchuCmaihO9pXgMH437qb72PdmLEnHiQD_v0kEAksPer0AMMxy3FroW2EaoKc8Gndeto5DI6Z4Qgmbc2t7ff0kOS-y6d0KzOSQfFrekHiqtJxnHmLXZgT2GjN-9rmhQgm2JkoA4m5FGiUEaJB2Stqg_ansg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صنعت نفت ملی شد، مردم‌ هم عموما بسیار خوشحال پشت سر مصدق بودند!  کمونیست‌ها، مذهبی‌ها، ملی‌گرایی از جنس خود مصدق و…..  میگفتن مهندسان توانای ایرانی می‌تونن نفت رو استخراج کنن، دروغ هم نمیگفتن! ایران‌تونست نفت استخراج کنه ولی کشور برای فروش نفت  و صادرات نفت…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farahmand_alipour/6609" target="_blank">📅 18:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6608">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HGZxXE6UwATxpYi_wLMHaGq8aayPsqmBGeIiwXCMGrvwfdjBh-baxORfLvZN-dc2OE8qP1jF5uiKxYATYRLMIpIFxqe02f_FY1xHe3uOp9lHf-RKNSakixIA6WSc0XjX84qe0i4uKpO00vYp0tSkUN_PdsmvDn4bCJbXbg_9J3kid7XVAfx-tpiJ2rErY5PGoEddjZFiT3-SQjGiDpRC3lQFC3EwLKTdiU3CtKKhGDH71nbAqOu9rLyPBHf_q9EW42Fb6LlAghEXnkkHoBBtv-TAEY9CxpJuUXwsQL9nMKlwml0q0tMG0ttN1kgJjCeyu6LRpr-ffh-ZL2X5Apw62g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رزم‌آرا، ملی کردن صنعت نفت رو رد نمی‌کرد ولی می‌گفت کشور آمادگی‌اش رو نداره!  و وقتی نخست وزیر شد، جلوی این طرح رو گرفت! تا اینکه یکی از اعضای «فدائیان اسلام» و شاگردان و نزدیکان نواب صفوی، او را به قتل رساند، زمانی که نخست وزیر بود.  مصدق که بر سر کار آمد…</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farahmand_alipour/6608" target="_blank">📅 18:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6607">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k2POWzNqhGHX_0-r-xnMNWuHsMmBgzFumu7hvBp2SuVYl7OVF6baQS3J1RQafGtZD0_hq7FYubOvndd_sY-9TiLPHde3jciHm3eRLBe9mTGyGP8hdaM9JVMHxVu54mUMqCjNCJAF3uErl5wWn0Tk-DAanRtXjfn2XzywC6F2wVNP1mrqQtYd1GCZnlTnjB4mp5fl9zA8c9LDJZctTNnOYl54ucwfQaznSsH876H_UOfCzkjmLWpVRyPcXsQFZKP48ohZDMsjkyRLOpOB7b1sZHMK8OrTb-jJR0DmZkEcqBlzcquv5NlMDIKzHsWq0sqyurbuudhgWUUYCed5Te7QTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب جمهوری اسلامی در یک کودتا و با طرح اتهامات کاملا مضحک و واهی  که بنی‌صدر در جنگ خائن است،  او را از ریاست جمهوری خلع کردند. سالها بعد شمخانی گفت نه!  او خائن نبود و اتفاقا دنبال پیروزی در جنگ بود و‌ گفت که سران‌ حزب جمهوری اسلامی  (بهشتی، رفسنجانی، خامنه‌ای)…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farahmand_alipour/6607" target="_blank">📅 18:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6606">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rZI5ii1yqkKM0lJNKYvEc0BgqoTgbYJyfn7GX9BKd6iFRIi6TBpYFwIrLpgUijTW02s5VuImEMGn1YcgIvyXSi9Robk4yqNzbTamLdAPTxTF8LvaiVnZ-hojgTX1CNMjP2SOtsSmjE595scShLpPFGBcl1-yGCkOmFgsU1FOajFM5GlpQ8JToD6sfGTpwpMxghQ5WMLT_PK3LvygVI_hca0ISpZWrXgbxss_UfEuELBPoBdD-RqXCVNFZpRy48W9NVS80XstzxqFmzABrz6zqQG1KGFLfG_FtG7A9d6mcQIKwRmxPm1Cp5m0rR9qCMPvRGOhajwRrmbcDqWHTSmDig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله کاشانی، نواب صفوی و مصدق،  همگی علیه «رزم آرا» بودند. مذهبی ها از مصدق خواسته بودند تا پس از پیروزی و ملی کردن صنعت نفت «احکام اسلامی» در کشور اجرا شود.  فدائیان اسلام و رهبر آن نواب صفوی،  اولین جرقه‌های چیزی را زدند که بعدها «جمهوری اسلامی» شد.…</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farahmand_alipour/6606" target="_blank">📅 18:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6605">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HiNPcC4AHBYYmVcE2X-blS5ZQqrCmAeF3M1rJOWKNPz_5XJVpxrTp2eSB6U_BNx3FQzWnVmT1Y1XE_4WUlB06eKx70j7CXGInZ_XBUUJz_eD7zB8HnSycu6EUxPhb3-qnhAyWixQ55h6kqhxWXgeEdEZvpbz74_KZTcgqSQgyQf6J3TfrfFFE7bizeWMX_jO915rYlgN3aqoFmVDEyDEQS95EXx7QAxGvtExKFpa5EDzxxWIF1Bh06P1qIAa6QK6sbzAugyN1dfQ5WAzu-Apdx_wCpAl6Dv5TnS5ImmHAfg5w0CM9UGLPxRnAMLtakYWb6JluDD7xWaNqwm7TcccZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر آشفتگی وضع کشور  پس از اشغال ایران توسط شوروی در شمال کشور دو کشور خودمختار ایجاد شده بود،  و کشور تحت فشار شوروی  توان بازپسگیری این سرزمین‌ها را نداشت،  مصدق ایده «فدرال شدن سراسر کشور»  را می‌داد! و به شدت با «رزم‌آرا» مخالف بود که می‌گفت…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/6605" target="_blank">📅 17:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6604">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1N8lGfX3uyIpyLULWS244qQKUttYQ0RMw4yOiRBuclUXL0hYIXOExnhqwwQ3vTGvqgCVnzztngXHHOnF5nT5i6hu8vl1CYOyI65XOQUC4amHhq07hzKPRDGFZg23O13Ek3XWqnKUBma45erUgdPMJQeYSLZP29LwaQJVH2JXwjH6-pMme-qVFHzV14O4ObVp_QqPdFZ8WiUNbQS_Vi5BVJD7c6agSmuyXmEfu6ROy9FrEKZHq2caBj7zq9xabkXI9jTs4OzAoCmDu1RR71TOmlmrtOpAmjExyUj8ZrROw8e_2BzXgWMkDMKRBxUuSxivxNFH44s8g1X6gAHxH-Ofg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنايت هايى كه جمهورى اسلامى عليه مردم ايران روا داشته، هرگز وهرگز اسرائيل عليه مردم فلسطين روا نداشته! قوه قضائيه جمهورى اسلامى عامل ٪٨٠ از مجموع اعدام‌هاى جهانه!! سيستم قضايى اسرائيل حتى يك فلسطينى رو اعدام نكرده! نه فلسطينى ونه يهودى و اسرائيلى! اسرائيل…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/6604" target="_blank">📅 17:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6603">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HnqyfOO5Z_5T5FPEKzSjgdV95VJJIFmABJul_azQicmhrrrFjeFSOH__eqO7ZxNcFH_ShzuoabTQMtpjNgVSxAIE_-6QfnUmTg4zF05mp-SZQjOriOTLhdR5I8TYHpfqtVw9TA5Xwkk0xOOfhJPiwRtZIyfFUWH7G5Xsl8k3PAdJpfxRS0qQ7N9Db2T0mIKLlJZaby8Z5P5_XT32foWMPw-txj6iZnhZXQSMwsUhJisyeox9rlcsuyaiTTJ7JSr1lIoSqBEHAUIxsepQ86K2qrztlBgi7bn8H7TKXSoZg7Emi70OVGwVo4x1clZ7lTm6-50gsvnsJREialEgIpbwFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتفاضه «قیام» اول فلسطینیان ۶ سال و انتفاضه دوم ۵ سال و ۹ ماه طول کشید هر روز جوانان فلسطینی به سمت اسرائیلی‌ها و نیروهای نظامی اسرائیلی سنگ پرتاب می‌کردند.   حتی «یک فلسطینی» دستگیر شده توسط  قوه قضائیه اسرائیل اعدام نشد!  حتی یک نفر!  اسرايیل ۱۰ سال در…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6603" target="_blank">📅 12:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6602">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJsjDnlynGGpYaXpppjQoH08omZKBVNOedUjLtwTExMmdWWdsK0IF3BJNE0aG8GwM69Rro6QmG99zEPzhpi4LmkyiZc0P9Z4FEUwLNs4t_yNIz1vz2oiGqZGoFEkOoNP_caRHcvxmCWYohz6bzaOZD-lwj8Xei4HlqBWUExcG9s8UAmKdOR6dNjorlWOvSY_YOf1BCVjzA6I-xvUE8GctOEYnS1bfN8yQkQu7uAG-yi9wwI-ZBIBFND93YUUVvSt96ib4kTBH-xm1B9ZA2dsCtPZ51IQOiImJUes7RBGSKrYZR-cY7mXOf8MtvqIh0XMWWOWZJn8vz097hfebzXEEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی «رزم‌آرا» نخست وزیر شد، مصدق که قدرت اصلی در پارلمان بود مانع از این شد که بودجه دولت را یکساله  تخصیص بدهند!  و بودجه دولت ماه به ماه! تصویب میشد!  دولت رزم آرا تقاضای چاپ پول کرد،  مصدق مانع اصلی شد!  همین مصدق بعدا نخست وزیر شد و مجلس را تعطیل کرد!…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/6602" target="_blank">📅 12:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6601">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GPUbXikkAnS6L7tIbt_MtFF5r3JZO6iqZ_chBMTPVuEiLBRoWLVlsG8dsCVgWq2kRiNUWCU51wNPaQpFhjEYVC-hDVgjJazJLdtZt2ghcJO1_BJ--Xff5zFIOrqdkxEtcdO8DV83B-8MtpRq_caCVhOzEaf0o6TGp0qI359VESFMQWWICQ84pe1tG_sF66AauGDJ5TyeDmUAi10KkOmBdVfw31V5uFhABcJxPrDshdguQwV2bOWRJyid8FLy7Srlw1ostHBid2peUs5rSxw35GZgedt65uHf6MKISd25YBxANjP9j6Tsq6LsVnN-9TyoacvFtabqreXG_hq0ZW8WQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپهبد «رزم‌آرا»، کسی بود که مهم‌ترین نقش  رو در سرکوب حکومت خودمختار کمونیستی  در آذربایجان و مهاباد انجام داد.  و چند سال بعد نخست وزیر ایران شد. مصدق از دشمنان جدی رزم‌آرا بود،  مخالف جدی برخورد نظامی با فرقه دمکرات در آذربایجان و مهاباد بود.  البته که مصدق…</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farahmand_alipour/6601" target="_blank">📅 12:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6600">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GR0bxTGoMzaNjUX8AhNJG5J3IaTE8I8k1nGNp0PcNfRb4NMcJ0FdrOyqoccuyLxKjuN4Q58niwpmnI73O79eACqBf3d9cXheOovAlUG0Fnqpsj9Zi7J4OZR4s1sFZsHJlZxzaS1ogz5texeJNIq58WQHssyujLmMHQN5BCyu7pq1OShdJCxcG6gMG9y-t2HQuxjDQGb9U9z-nIcTi07LoHzH7E3uhPHdSmiCykkUVdrZMdQesfIf7BCPS7EAgcDDYunC9EBOLarca1jm7crRtUqWgiBJZ5b1kI8EGlGtki-s9iBvr4ln_sd107ATUWCNgLrfgz0icH86X1Mz2L6L-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی میگیم بر اساس مالیات بر چای و شکر و قند، راه آهن سراسری ایران ساخته شد،  یعنی چی دقیقا؟   دولت در سال ۱۳۰۴ قانونی تصویب کرد  که بر روی هر ۳ کیلو قند، یا شکر و چای  (۳ کیلو رو اون زمان میگفتن : یک من تبریزی)  ۲ ریال مالیات گرفته بشه.  یک من تبریزی ۱۰ ریال…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/6600" target="_blank">📅 12:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6599">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AFeRixL-lGRxtJGrnncdTDYtzA6tm_0dESuS0_gyPlwgdtFNXAdcYlnfkGjLU-Yxl9tmucpylNFhu-BsmXmPyJTfHwJpI3_PCzxc6RuE-qrAjSGU1JYxnJC_Jyulo4pqL2TQ0RbwdpS3LMCXGArvDLnKmb7D1HSilNW-pMKTTR47YUnrk7MD7KiPbT_dBHGX4XM8CwQOXKzGdjiLzVt1CVo-POhSQuPlCRyhAD41JyT0-HUCnDkvEHlt-yCa6T-AoAJVFqxF5Wps_xepJl0l5ByC7qJQl23ycNZQ79O8gIDjkEoajMDkanxXog8WnU7f6rMskZhAHGtffHsgHdCyvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راه‌آهن سراسری ایران، زمانی ساخته شد که ایران راه شوسه  درست درمان هم نداشت!  زمانی که حتی قافله‌ها و کاروان‌‌های شتر از دست راهزنانی مثل «نایب حسین کاشی»  و خوانین عشایر در گوشه و کنار کشور ، امنیت تردد نداشتن!  هم قافله لخت میشد و هم افراد رو به گروگان میگرفتن…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/6599" target="_blank">📅 12:14 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6598">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">مصدق پیشرفت را در آبادانی شهرها نمی‌دید! ساخت عمارت و هتل و آسفالت و آزادی حجاب و…..!  خامنه‌ای وقتی از امارات عربی متحده، و پیشرفت‌هایش صحبت می‌کرد هم  دقیقا از همین زاویه انتقاد می‌کرد!  میگفت : این‌ها که پیشرفت نیست!  حاکمانشان «بی‌عرضه»‌ترین هستند!  و…</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farahmand_alipour/6598" target="_blank">📅 12:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6597">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k2-V7CZ--pQCPUx8-795f-dH24NFOAgCTntJTycQVaEjdREI7VsWCLMl2DeSOtPq_GR4n2A9yU0umsYIi13jgnhHb6BWSJWG68ti-DiglSL1T4xynf19_C7Co4Uzv7X5zAJb7lgJvzkDLxt3zxl8fF89cVnPoYZxwivTIDxoyHcpUUPaT7VFyjEU7tHRxf80DkqzncMzySSfpX4DLum3ZBu8qg1Ul4g31Drk16o_aoVOPMhOShPcirRkhIQJMn1kzQ9MuNKMU19lGxNAyZK14ANUpjlYrL8pID1q7xL2fBmmCpttl2cX7Rzy2UbcaiaVIiGC1hl-RVfmUGU5L2_uaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حداقل زمانى كه ما در مدرسه درس ميخونديم بهمون می‌گفتن که رضاشاه به خواست و دستور انگلیسی‌ها ، براى ايران راه آهن ساخت. ولى مى‌دونيد اين حرفها رو خيلى سال قبل از جمهورى اسلامى، چه كسى میگفت؟  این حرف‌ها را مصدق میزد. مصدق حتی اقدام رضاشاه در آسفالت خیابان‌های…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/6597" target="_blank">📅 11:52 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6596">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CuE8BKH4Jhkczmti9D612Pg_gVMGccdCnw65Nc3seL2On6qYHU_tD1NfTjwfu1H7Zsa9TF-5MiyQct_Q0pTv47OTxApfSfDG7kVj0pHhckSbMFFKLgrFeyBrH7aAFGXg1O-fXjeUgC8T03S5FcDdFd9_ZZLvEuCgdcI99CzAMuUx4OKpojY_l9lcq_SLZc_odgpmQ3CJb3UBlvzqpPEJmCZ8dHOsxAS-7eMuk87MBLhWEObFNuKbL3c0gDgd-iFPRP_05EvPYs6GD493DupZZGHKK-rVu9L2gbP3umXOWuqj2F7aEPawlsv6kvjNWa2tU-3nypZ9jpQtxAOhe2p61Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حداقل زمانى كه ما در مدرسه درس ميخونديم بهمون می‌گفتن که رضاشاه به خواست و دستور انگلیسی‌ها ، براى ايران راه آهن ساخت.
ولى مى‌دونيد اين حرفها رو خيلى سال قبل از جمهورى اسلامى،
چه كسى میگفت؟
این حرف‌ها را مصدق میزد.
مصدق حتی اقدام رضاشاه در آسفالت
خیابان‌های تهران را به درخواست
انگلیسی‌ها می‌دانست!
او ۱۰ سال پیش از آنکه با محمدرضاشاه در بیفتد، یعنی در سال ۱۳۲۲ ، نطقی در مجلس داشت از آزادی حجاب در زمان رضاشاه و تغییر چهره شهرهای ایران و آبادی آنها انتقاد کرد  و از جمله گفت :« رفع حجاب از زنان پیر
و بی‌تدبیر چه نفعی برای ما داشت؟
اگر خیابان‌ها آسفالت نمی‌بود چه می‌شد؟  و اگر عمارت‌ها و مهمان‌خانه‌ها [هتل] ساخته نشده بود به کجا ضرر می‌رسید؟»</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6596" target="_blank">📅 11:49 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6595">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQ9iCbcnI1ejRYArPi5OgzdmrrSQgt3U_vyxyabvxvPLr_vQWRm9zAk0tdKDxHDE7q05P7F3x2MIO9UPE-ouPeIS_PPjvtqpFdhJ6JkpltP_FEOqPqUx0Itp6MxQaY3eEvholmk-vdVZYSdp0z-yzpH4s1nSFqSqSxnqvTXZNafz1_sJinyfBG7QxmO2hVpujUrY99L2XTc3XnP-E-HUcQIcJpVIbWtm1EIc2UMWCMWfamEURVP7yghLk-sFJhAKZ2NYNHXXjM4haqFAtOCu2YuH-48iSvbtMLDwA3G4iDUj5CJwSrKMeY1ZPxe2vm6A2C5hep95q-Y8Gz2x5DgV2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز نچیروان بارزانی
رئیس اقلیم کردستان عراق رسما درخواست داده بود که بین ج‌ا و آمریکا میانجی‌گری کنه.
خوشبختانه جمهوری اسلامی
همون دیشب با پهپاد به دفتر نخست وزیر
اقلیم حمله کرد، تا یادآوری بشه چه موجوداتی
در ایران حاکم هستند!
کار خوبی کردید، قطر و پاکستان رو هم بزنید!
قطر رو ولی حتی بیشتر!
که اون شبکه الجزیره‌اش
کپی صدا و سیمای خودتونه!</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6595" target="_blank">📅 17:29 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6594">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپایگاه خبری انتخاب</strong></div>
<div class="tg-text">🎥
تماشا کنید: «۹۰ میلیون ایرانی متهمند، مگر اینکه خلافش ثابت شود»
🔹
این هم نتیجه باز‌شدن مجلس پایداری!
🔹
عقلای مجلس از تصویب جزئیات خطرناک طرح جلوگیری می‌کنند؟
🆔
@Entekhab_ir</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6594" target="_blank">📅 00:17 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6593">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=oJvyFYceV_NHFbCg2j1PpzZA52wbWpRd2CGfJnh8NrlWy2zoxy4544zUiKtccHr_UcmcDui0AnVjbY_88IN1GteKU2oBb00U3F0LuP4c3Rg-u5i7uA7Qb0jcN3DnGBy9IVexs8KGAAKHxs_pMI3BMgWDOZeDmFOGqN56rQ8uGZa_9Q7q8jqw0kK52fQHNXIR9FZMiAXgNB6KzJXqnHtZ5btz-eH1-iiYngTHq6jlitRZrYQaFY2FcYXGh3ralqnF5hbQURjGX34eMH9Bl5bpC4XF5pI4bDQqLwFJjQnd1nvbh25udlp-C1U9wdFo9lOGH5RV2fFrJYKwU-_1wV_WfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=oJvyFYceV_NHFbCg2j1PpzZA52wbWpRd2CGfJnh8NrlWy2zoxy4544zUiKtccHr_UcmcDui0AnVjbY_88IN1GteKU2oBb00U3F0LuP4c3Rg-u5i7uA7Qb0jcN3DnGBy9IVexs8KGAAKHxs_pMI3BMgWDOZeDmFOGqN56rQ8uGZa_9Q7q8jqw0kK52fQHNXIR9FZMiAXgNB6KzJXqnHtZ5btz-eH1-iiYngTHq6jlitRZrYQaFY2FcYXGh3ralqnF5hbQURjGX34eMH9Bl5bpC4XF5pI4bDQqLwFJjQnd1nvbh25udlp-C1U9wdFo9lOGH5RV2fFrJYKwU-_1wV_WfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنبش شعوبیه یه چیزی توی این مایه‌ها بود
اعراب فاتح، ایرانیان رو تحقیر میکردن،
زنان و دخترهاشون رو توی بازارها می‌فروختن.
می‌زدن توی سرشون و ازشون جزیه می‌گرفتن.
ولی ایرانی‌ها گفتن اصلا ما خودمون از شما مسلمون‌تریم!  و در اسلامگرایی از عربها جلوتریم!
انقلاب اسلامی در هیچ کشوری عربی رخ نداد، در ایران رخ داد!
جمهوری اسلامی توی قانونش نوشته بی‌حجابی ۷۰ ضربه شلاق داره، نه فقط نوشته که اجرا هم میکنه.
هر روز پلمب کافه‌ها و... رو داریم.
هر صبح اعدام داریم، هنوز چند ماه از یک قتل عام نگذشته. اینها اما برای موشک‌های جمهوری اسلامی قر میدن و میرقصن.
البته که مردم ایران آگاه‌ترین مردم جهان نسبت به تاریخ و هویتشون هستن! خیلی!</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6593" target="_blank">📅 18:44 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6592">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qe3uZJX93ns0D4dba-rVA_g3jEtxoywSdsPViD0phfyRQSJbMMFCylpUpUXde7ylQAc-lFuqtk9Ri3YDUs8sf3wAhRcfoIXWzkEI-_ERxHB-BiR4vj1c_4HINWcouDjicpF5JziCPWdg4vkLjJpvS5TVWfwbhOL9gVXlDlKG-5QAwpgDH5Q08y8UYcyDGEoqNtaKQp5hbIONFJ47B7btoyYA5Sz15inZzN5RB1ksFkjZn5EjUsmmf5uuDieJsRRKocVr-Zpaip9iZASlb4moy3Uk7NWELmBl0eeukb7dtXspJO7nMm_uX7HvrE2MB0BasYv-1voRLp4SAwZ_vOetXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه بقای شما نابودی ایرانه!
اگر اینگونه است که تسلیت به ایران
و چند نسل آینده ایرانی!</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6592" target="_blank">📅 17:11 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6591">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">اگه این موضوع به این صراحت در تاریخ اسلام و سنت اسلام وجود داره  و قرآن هم صریحا مجوز داده،  چرا در ایران این نمایش‌ها برای گروه تروریستی داعش برگزار میشه؟  پاسخ ساده است!  ‌اونهایی که این برنامه‌ها رو میریزن می‌دونن عموم ایرانی‌ها از تاریخ اسلام بیخبرن! اطلاعی…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6591" target="_blank">📅 15:46 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6590">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">این هیئت رفتند پیش پیامبر اسلام  و گفتند : « یا محمد!  در میان این اسیران، خاله و دایی‌ها  و زنانِ دایهٔ تو (کسانی که تو را در کودکی شیر داده بودند، مانند حلیمه سعدیه و قومش) حضور دارند.  ما را دریاب.» پیامبر اسلام هم گفت من سهم خودم  و بنی‌هاشم رو میبخشم!…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6590" target="_blank">📅 15:04 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6589">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">در جنگ با هوازن (جنگ حنین)  [که خامنه‌ای قیام حاشیه نشینان فقیر مشهد- کوی طلاب در سال ۱۳۷۱ رو به بازماندگان جنگ حنین نسبت داد!!!]  تعداد زیادی زن و کودک نصیب مسلمان شد!  مسلمانان مکه رو فتح کرده بودند  میخواستن برن طائف رو هم بگیرن که وسط راه جنگ با قبیله…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/6589" target="_blank">📅 15:00 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6588">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">آیا این تنها جنگ و مورد بود که در زمان پیامبر اسلام رخ داد، و زنان و کودکان به عنوان غنیمت جنگی برداشته شدند؟  پاسخ قطعی : خیر!  در جریان حمله به گروه دیگری از یهودیان،  در جنگ خیبر، زنان و کودکان آنها هم به عنوان غنیمت برداشته شدند،  از جمله زنی به نام «صفیه…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/6588" target="_blank">📅 14:56 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6587">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">آیا علی هم سهمی برد؟  قطعا!  از اونجایی که ارتش اسلام حدود ۳ هزار نفر بود، و سهم سواره‌ها ۳ برابر پیاده‌ها بود،  همه املاک، زمین‌ها، پول و برده‌ها، ارزش گذاری شد، ابتدا «خمس» (یک پنجم) که سهم پیامبر بود جدا شد و سپس ۸۰٪ بقیه بین افراد تقسیم شد. از اونجا که…</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/6587" target="_blank">📅 14:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6586">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">وقتی ثابت بن قیس (مسلمان) نزد زبیر بن باطا (یهودی - اسیر) رفت و به او مژده داد که از پیامبر برای او، همسرش، فرزندانش و اموالش امان گرفته است، مکالمه‌ای بین آن‌ها شکل گرفت: زبیر پس از شنیدن این خبر، از ثابت درباره سرنوشت رهبران و بزرگان قبیله‌اش پرسید و تک‌تک…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/6586" target="_blank">📅 14:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6585">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">پیامبر اسلام سهم خودش رو  (حدود ۲۵۰ زن و کودک) رو ،  که خب سهم «خمس» بودند، رو فرستاد که  در «نجد» بفروشند، و با پولش اسب  و اسلحه خریداری بشه برای ارتش اسلام.  البته این وسط یکی دو اتفاق هم افتاد،  مثلا یک مرد مسلمان به نام «ثابت بن قیس»  از پیامبر خواهش…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/6585" target="_blank">📅 14:30 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6584">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">آیا به بردگی گرفتن زنان و فروش اونها و یا ازدواج سریع با اونها اگه شوهر داشتن مشکلی داشت؟  نه! چون خود آیه ۲۴ سوره نسا صریحا اینو میگه!  وقتی هم قرآن بگه  هیچ آخوندی چه شیعه چه سنی نمی‌تونه مخالفت کنه!</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/6584" target="_blank">📅 14:26 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6583">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=hJVv8bHsIbbcqT1EPbl4p6_vI1G5-b_bCRekiTmZU_L3zXKBBRdVl61A6YBhvnReePsDO2b2MbmInSHZ-4nwiCQW4BKe_-N_2qMG5AfyYpJkMlSzT2HkVLWXGRxXDJ4zWg-d2nn1ER3JNuPGQOr2mnWATLW_9YNyh65_oiBuAD5DNlJMNThkx8MrWJwHIdCXxKxOW2jizdelzby-LbjwDv_Tcfb9La9ktIQEKvFMrMi2dSGg3rZ0_R6ZOyfne8jZqSEA3iGlYnIh0fwhSxc_A4OTJfL945-vntVpqKo6N5JCC1cNuEVKen3Rvpdka5IxcW88gjMfGWlY9BnFtcJsFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=hJVv8bHsIbbcqT1EPbl4p6_vI1G5-b_bCRekiTmZU_L3zXKBBRdVl61A6YBhvnReePsDO2b2MbmInSHZ-4nwiCQW4BKe_-N_2qMG5AfyYpJkMlSzT2HkVLWXGRxXDJ4zWg-d2nn1ER3JNuPGQOr2mnWATLW_9YNyh65_oiBuAD5DNlJMNThkx8MrWJwHIdCXxKxOW2jizdelzby-LbjwDv_Tcfb9La9ktIQEKvFMrMi2dSGg3rZ0_R6ZOyfne8jZqSEA3iGlYnIh0fwhSxc_A4OTJfL945-vntVpqKo6N5JCC1cNuEVKen3Rvpdka5IxcW88gjMfGWlY9BnFtcJsFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در روایات این دو کتاب، اومده که حدود  هزار زن و دختر و کودک یهودی از این جنگ موند!  که اینها رو به عنوان «غنیمت جنگی» برداشتند. یک پنجم کل این تعداد، تحت قانون «خمس»  سهم حکومت اسلامی و پیامبر شد.  چهار پنجم هم بین سربازان و فرماندهان ارتش اسلام تقسیم شد!…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6583" target="_blank">📅 14:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6582">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uVOaVMZVzhLALI4PTSrWSrsV6DLs39-hDSffZ7_2ByHMj3OlKNS_BQxpFp-kl4wEqaJSViYQ57oTfBHvi4ZqXykJ9pEsM6d11_tRIoo1TCpC_1lNTDk7QRybZH6ftuiZ6n9QjHlGuMzHx9yLquBGu8JrUaeZ4ehAs_9XwiG7Mg7GGvNNbERjeCUFv4dGwYjxZNeV-KrRySbradIn-K3AaHmZVvT2NXA8VNL2PETT0G_9xYDNPQdXMER74YkO94OPTNL-jfETSlvxmMLoh5fD0WiQVoQyMQ4gjapawxuHCnJhjiQAFVT0AQkohrYMwtXwRUb2QUyp2Vw9tDqZNgeoNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقاشی مینیاتور از جنگ بنی‌قریظه و صدور حکم کشتن تمام مردان و پسران یهودی.  مردان رو یک به یک کنترل کردند،  که آیا کودکه و به عنوان برده بردارند، یا به قتل برسانند.  مردان بالغ که از چهره‌‌شون مشخص بود که بالغن. نوجوان‌ها کمی دشوارتر بود.  لباس زیر اونها رو…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/6582" target="_blank">📅 14:06 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6581">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0KLZMrROxg8fjqe9X1CZtIBItmwBG4_7GeRESSB-Kc9X3i1snJqYNUccA3gii8Ga9Iw-tFkwvcGcdgfsLvy3LEeqYVZbUVvm7BPR_jB80FEP6Oq5EP_2AR_SFMeYjSKZWitzNR_AuQM6iCz8dcSZzEqkejgqUTxLISTBdclDJe4-5yKcqBwyfnJK4b-Uzv6JyCEk5fWMWCdOBm0GF6eyzqWu4YK1yJWBUghtIrgg_SjJLgxGDf3gLyhZ6YBcqSnDHQxs3hXQWAA5u0ovsMj6qclTJUEnv-jqfzTrYm3cpelUCO4VYzprl4RTvCZC_5Kp3c4GaXp7R5ex68HtOk_LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در جریان جنگ علیه قبیله یهودی بنی‌قریظه،  به فرماندهی پیامبر اسلام،  تمام مردان و پسران بالغ کشته شدند.  همه اینها تسلیم شده بودند و اسیر بودند!  یعنی در جریان نبرد و جنگ کشته نشدند!  همه تسلیم بودند!  کتاب‌های اصلی تاریخ صدر اسلام  مثل سیره ابن‌هاشم و تاریخ…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/6581" target="_blank">📅 13:52 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6580">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/201818ce22.mp4?token=nQdB-xmbLmaSAnFQILHmkl_uik6vNczIcpGmJN0cG6nx_AFZD8qNFLLOvQKCh0gKy4jMTWI4CmBc7oxkJiXaeeCBDi-PKQiHcZLbEUMO5T9HEomilzqQIMi7Q68d6c5gn5Q-MAoV3QqulVveJphHdNMzOs8kq8aYNpg3ALyX3zHOhSy3Jne6Z2cJgH162sDCpaiael3mRSTChguHdKVc3oGTStIUzZeCduMRYlhDyCTWoB4CAezK6jNEw_vZxL7sFsvZWl56fBQ-NGjkXe0pt16fV9smelFU74rBFop7gPSJowBuJlzY0rM1TpnQMoQ6GCj0ylvR1oGGXHyV81Aacg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/201818ce22.mp4?token=nQdB-xmbLmaSAnFQILHmkl_uik6vNczIcpGmJN0cG6nx_AFZD8qNFLLOvQKCh0gKy4jMTWI4CmBc7oxkJiXaeeCBDi-PKQiHcZLbEUMO5T9HEomilzqQIMi7Q68d6c5gn5Q-MAoV3QqulVveJphHdNMzOs8kq8aYNpg3ALyX3zHOhSy3Jne6Z2cJgH162sDCpaiael3mRSTChguHdKVc3oGTStIUzZeCduMRYlhDyCTWoB4CAezK6jNEw_vZxL7sFsvZWl56fBQ-NGjkXe0pt16fV9smelFU74rBFop7gPSJowBuJlzY0rM1TpnQMoQ6GCj0ylvR1oGGXHyV81Aacg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در تاريخ ٢٩ بهمن ۱۴۰۲ در متروى تهران نمايشى اجرا شدكه اگه گروه تروريستى داعش بياد ايران، زنان رو به اسارت و بردگی میگیره و اينكه قدردان جمهورى اسلامى باشيد. اما اين الگوی به بردگی  گرفتن زنان وفروختن اونها در بازارها، از كجا الگو گرفته شده؟ آيا گروه تروريستى…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6580" target="_blank">📅 13:41 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6579">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ArgSIFaYcQRZMyJfVIl5onRn_Z8BPaDhxKKzbUFKuQIJDNNaWN4fA0ZtLKxhXcFT86yUPLAUPYqb6uOuCGO_ZIA5abOCdsLxy7NOsYjfgYhm5vOOFFnUnxX_WrDcSIqqSlt4FnfaR4CgFXbnvHjY4BGP0B5QaZouCTvg351gNdcl9fFRvY109smFeIITw6dp1GCGckB05z0nmVkRCTp0nzEfg6RZPzAwC_kFGOcbZnhMCXf2_xkaYksOeP27sMLeWOLhsXHoqxX3AuUohE2oINhSiiPEfwh0AxC1euv3IB9SKJZpKJWOLixn7MYMdOaDazEpraMJcFh3MOIYuVugdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در تاريخ ٢٩ بهمن ۱۴۰۲ در متروى تهران نمايشى اجرا شدكه
اگه گروه تروريستى داعش بياد ايران، زنان رو به اسارت و بردگی میگیره و اينكه قدردان جمهورى اسلامى باشيد.
اما اين الگوی
به بردگی  گرفتن زنان وفروختن اونها در بازارها، از كجا الگو گرفته شده؟ آيا گروه تروريستى داعش اقدامى
ضد اسلامى انجام داده؟ پاسخ صريح : نه!
آيا مذهب شيعه، مخالف اين كارهاست؟
پاسخ صريح : نه! به هيج وجه!</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6579" target="_blank">📅 13:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6578">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIndyPersian</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FuHOC72xCefDfJNyhLxdSWuhrP4ogtkxMBYd846fEIm-o-JuOst9xREhSwLJX5tOuz8Q8PgTo5xN3eiVpLjxjqzQHw-RE-RTm0yzOZIUUBodDYCaSA-hhBflVbmSlznuT2h44tTjLc_1KCgX0ZJHehbFKY_KPfAtf-flEMZY7JAmqhVIwdi5gUuU8k0MAV33vY-8kr7ya5xlo9qxMdZAxmfL_frilHyo4Eq9S5f79j_AqinkazZRNlLlrilsjjWiy7dOJ6Sg3k_nSYn5Idkw2_HZlaewC84eMr13OELk_QHFqufi9iCCxK6EAoq9nhFwCEd7g55AK7FWun2gyvUYVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میزان، خبرگزاری قوه قضاییه از اعدام شهرام صادقی، از معترضان انقلاب ملی ایرانیان در دی‌ماه ۱۴۰۴ در کرج، خبر داد، اعدامی که بر اساس روایت رسمی دستگاه قضایی جمهوری اسلامی، در پی پرونده‌ای با اتهام‌های امنیتی انجام شده است.
میزان نوشت که صادقی به اتهام «اقدام عملیاتی» به نفع اسرائیل و آمریکا و گروه‌های «متخاصم» و همچنین اقدام «علیه امنیت و منافع ملی» به اعدام محکوم شده بود. این خبرگزاری مدعی شده است که او در جریان اعتراضات، در ۱۸ دی‌ماه، به دلیل «زیر گرفتن ماموران با خودرو» بازداشت شده بود.
قوه قضاییه جزئیات بیشتری درباره روند رسیدگی قضایی، مستندات اتهام «اقدام عملیاتی» یا چگونگی صدور و تایید حکم اعدام منتشر نکرده است. همچنین در گزارش رسمی، جزئیات مستقلی درباره ادعای زیر گرفتن ماموران و اینکه این اتهام دقیقا بر چه شواهدی استوار بوده، ارائه نشده است.
@indypersian</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6578" target="_blank">📅 08:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6576">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/euHp5FxdNDdYCWPYmvF-2rngJ03aDa4RyKvz7Gfnxd77YKzwXoDKNAzKO4OFHnxyK_0lLpLrP4ZhvOnLVXwokAepSurb0O1xwQOHHM_yEtLAYD4-84I5IVSHAbDxEomV1crhjtUTEgyZJx1f41H2xIWEfe7uJJSsuOst6t1FP5cAjURMvILWF9OdbUZ2HmUTkKCJst_rVpEQL9ddgwycKDMs8nrVNMoYOC3PtxL5IwHqAcGg-SvYuAjTDE08RQV8g0DWEehfNjTYgQZCk4tb2nae90z0PrYPxVItynrHzV-vDJXrwqJxwKwGpJnEBsYTOR8p1fuo0IIL_2_JMajifQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=RuCevV2UEI7wMnROF1hp2_-VfDj--SMee0w6mPfK4-J73lBO1b3rXxzjtrA5WSXMpGzSfzWm9_P2UT3fKYCxnw4wBV-aaP0MWc7NbuHRMVMd0dFxCSskZboNxM1AL-EOKZXVVV3hOH3Awl8vwfl0BTrYaxGL1q5yD4NSySq-mYVgR82tkVbqdEtz0pBF0LfjMNbPeNjOOFafngGZdy8vcBVkffZSPR-ZrWXJN01f-eGIIrLz-bvt3T21rTSnMYWkFJ3_ig7VUTIRjSfnRiijpJzuaYDVcdSjiJI13ZryW7pCI7mc5eE--XqLmxKXl4nepsIFL46BKB7d9nXNijm_5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=RuCevV2UEI7wMnROF1hp2_-VfDj--SMee0w6mPfK4-J73lBO1b3rXxzjtrA5WSXMpGzSfzWm9_P2UT3fKYCxnw4wBV-aaP0MWc7NbuHRMVMd0dFxCSskZboNxM1AL-EOKZXVVV3hOH3Awl8vwfl0BTrYaxGL1q5yD4NSySq-mYVgR82tkVbqdEtz0pBF0LfjMNbPeNjOOFafngGZdy8vcBVkffZSPR-ZrWXJN01f-eGIIrLz-bvt3T21rTSnMYWkFJ3_ig7VUTIRjSfnRiijpJzuaYDVcdSjiJI13ZryW7pCI7mc5eE--XqLmxKXl4nepsIFL46BKB7d9nXNijm_5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در پاكستان ۲۶۰ ميليون مسلمان زندگی ميكنن (از جمله ۴۰ ميليون شيعه)
اما يك آمريكايى رفت و اين خانواده رو بعد از چند نسل از بردگی نجات داد.
در اين کپشن نوشته نشده، اما ايشون حدود ١٠ خانواده رو نجات داد!!
اين مورد از برده دارى تا همين چند سال پيش در پاكستان «قانونى» بود. الان غير قانونيه اما هنوز رايجه.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6576" target="_blank">📅 00:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6575">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b59ed2e4aa.mp4?token=TVhTa6BdI9ASrIuGjJRzZ8oz8W0K_Rg5bZDjAAPPQ8Dk0PTZCbwCuWWI-yBd3fn6v2fJ31fn6410oHSQd28TtIGRgz68gicx4B1TBURH3cL1WcnFqw4HQ8OtP8pILNQXua0tlf-HUUV9jB6A5AENfhF-oQmS-uYLgM_h5AuLKm3G4FJZmDNP5HZ6G_jwaMhYkv-OPfWVU3WpCrEbXsX9ND5TYvrV_vC3G_NVCyU3BOPDIhCWHJI0CAoFGdw8vBBSmByVoornELPWbQv9Ptf6IymrLzbyMCS0zlID-qoZc29r8hplvW8zeK-wjVWx4mC8t_3VajwFYTHuEa6E3WcWOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b59ed2e4aa.mp4?token=TVhTa6BdI9ASrIuGjJRzZ8oz8W0K_Rg5bZDjAAPPQ8Dk0PTZCbwCuWWI-yBd3fn6v2fJ31fn6410oHSQd28TtIGRgz68gicx4B1TBURH3cL1WcnFqw4HQ8OtP8pILNQXua0tlf-HUUV9jB6A5AENfhF-oQmS-uYLgM_h5AuLKm3G4FJZmDNP5HZ6G_jwaMhYkv-OPfWVU3WpCrEbXsX9ND5TYvrV_vC3G_NVCyU3BOPDIhCWHJI0CAoFGdw8vBBSmByVoornELPWbQv9Ptf6IymrLzbyMCS0zlID-qoZc29r8hplvW8zeK-wjVWx4mC8t_3VajwFYTHuEa6E3WcWOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماينده ملاير با چفیه حمايت از غزه و فلسطين!
«مهسا امينى به درك واصل شد.»
مگه مهسا به شما چه ظلمى كرده بود كه اينقدر طلبكار هم هستيد؟
غير از اينه كه به خاطر يه روسرى و به خاطر افكار عقب افتاده‌تون، جونش رو گرفتید؟
حالا ناراحت و طلبكار هم هستيد؟؟
توى خودتون و دين‌تون و نظام تون
و چفیه‌تون و فلسطين تون!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6575" target="_blank">📅 21:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6574">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eRfH2U2Nj9M5PHFYu1gLdWl5_GTccll_InhZcLLcWKp6Sof380Sz5R1BsgElXEQymsTho8VOyeMNc9iqtWBUIZNfixq9p5z26ftUn0nzij53ER0Dusyh1ag75Bf8gKeZxFIlivkYiQ203g6_fL56whTyOK7c_43c0WkFG8p0xRG6VHMpHMpJ8WzgBYMA89LqU1HVgceMnskcQ8XOTjcsIElTlFRzc9wRZBKbNOImz9ttlNdUSEiob3_lSXaGrD_UBjjN6LBNdK1Ggr1qA_4aiR-89911C0wMsstaeNcnAFIdxvHthLFtn_yudhjLryrpt5DGcOlUHvrVaw2yyf3I_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا اون روز رو نیاره!
همین ایران و غزه و جنوب لبنان
که حاکم شدید کافیه!
همین افغانستان بسه!
میخوام ۷۰۰ سال سیاه گروه تروریستی حماس نتونه حکومت اسلامی در غزه ایجاد کنه!
میخوام ۸۰۰ سال سیاه گروه تروریستی
حزب‌الله در «دکترین ضاحیه» بمونه!
و رهبر شما هم از زیر گودال و چاهِ حقارت،
«علی الاصول» بنویسه براتون!</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6574" target="_blank">📅 11:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6573">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sbSxZ5KMBzIzH4D3TZzfGUeWwm6VaO7H-8z-pxSay1HEIKBQbcvWXR7cGCLIRKuybRVYgZmmDxJGCPHHQkJr66RydjqlvvMzCQG7e7pGLlaPEhi2BESiXn4f-m5ppwgVcYxubbZ-mK2EkwSQbyIiSpbyLtHqqO1v8XWJF7qOdmozoJGaDNdh4lBfzO4sV1CL91jnawzlTa1yl7o9TdGQ73Y6JgSVXMjMXdrC9V3gAy7Cj9ejJzgVE6e2Uj7whskkYgvwtiuIHi2vDYKhgn0nsvPrCMn7TLMTxM9BiVsVjNOXnC1E-zId5sZdEeLBazVAnJ5CwIX83sfdHXXQzL-ekw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از پسران معصومه ابتکار (سید طه هاشمی) به خاطر اینکه پول یک موسسه رو بالا کشیده بود (به ارزش امروزی حدود ۱۷۰ هزار دلار  یا حدود ۳۳ میلیارد تومن)  حکم جلب صادر شد.  سید طه هاشمی همچنین متهمه که سرمایه‌گذارن رو پیدا می‌کرد، یه پولی ازشون میگرفت و با توجه…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6573" target="_blank">📅 10:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6572">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sstYSb7EP7gebU11MgUGmJoQeI6UdBTfYelN_SAmtfGRXBJ9wM8nFVJSRAfuuUBtsAwf07BJjS-HHHAlijkW2-sC0qjoR0oaOekKjfhaiptSCed0Z3E1ld4tqACnuImkp59qPKuVw-O65zboin-bXGe3-0O9OQULEQbuAttqeQya4jst6rqEfAg5A9FY66oi12URE_hlN2PGRFrpj3jLe6DHSaJ7NS_723QXtLiPSk3lVI0-Dg04nyaoG8M51dm2Pxua18LVjdhkXRzghL8aN3frCu6EK5pnUUnowFBFUYOwEbekXQ6pmmX0-8IBIvSq7zDfM_XGFnlDCwsCIefpbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پرونده «املاک نجومی» که شورای شهر تهران به ریاست چمران، زمین‌های مرغوب دولتی رو با نرخ ۵۰٪ زیر قیمت، به مسئولان حکومتی فروخت تا اونها بتونن چند برابر بفروشن  (بعضا با گرفتن مجوز تجاری و…..)  و از سفره انقلاب بهره‌ای ببرن،  نام معصومه ابتکار هم دیده میشه.…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/6572" target="_blank">📅 10:24 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6571">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pxjKIQb7BPvvz1-piuqyBkNdXZ8RDBmHGOZ-jIv7Y0pQCoRL22OFg5qngo7VCvgHDJVALx1-vutcLMyKwAKLLXzPU0RRHFIXC0MW3JRBj86oG5O1NrxRICxnBkW00WRO47RcAIuF1NQNFK5oCc2zCHxCfApKZSrYrqTKDFAvbU_W2qJLWv4hozHv2Jnw_AEs7WlnmPm6dgM1HDtaDwY169TuQCMugJeiMFj1UIQz01lPQbKajOaOzP9ATh1F30vE3abOQQ0WPo8cM5FLR7xzUBOaCrgqMQEGyjkHw0xK1eb0-rAyjhre_z57wqUZRYW7UZnHnmnD_X3XZg5cu-od9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معصومه ابتکار، از زمین‌های ارزشمندی  که جمهوری اسلامی پس از وقوع انقلاب مصادره کرده بود نیز سهم برد!  او به همراه مادرش (فاطمه برزگر)، خاله‌اش، پسرش و البته «مهدی چمران»  این زمین‌ها و املاک را به اسم «موسسه زینب کبری» ثبت کردن! موسسه‌ای با زمین‌های مرغوب،…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6571" target="_blank">📅 10:17 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6570">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jQsyOC1kr_zPh4QiLMmhvQlBYycnzaU7xQlqQdZoDLHKuoFKUYF00n1yOgQKlCjVgorTnBPO-5bPPO7YFzYo_5iTW4NGHRKn9OJ_DPwqMkBb6j5dC9D3qbYj5HADoax46xv9-1WDc_0YGb_cmCv_Dd6JkUAQ9UKzx-uxRBmhMW_TZTAhVNDJEJx41w6Tdd3op0X0lKC9K1pdQi0h9f4gnjZrIr3ejLXgx2D3a50NYoHMxpGo69tcPpy9XMKtDNilvKH3Z3PvgHGQyXmMgEInSL36ycXnt7KwZ5mPskwmf4Bem70NjAlnE-Xu5jqQnr0otZFbLobI5aw6vghYx-7rkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تصویری از پرونده «چوبهای روسی»!  معصومه ابتکار همچنین در دورانی  که رئیس سازمان محیط زیست بود،  به «زنگنه» وزیر نفت گفته بود که اعلام کند که دولت «بنزین کم گوگرد» از اروپا وارد کرده!  در حالی که این فقط دروغ گفتن به مردم بود!  زنگنه بعدها خودش این موضوع…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6570" target="_blank">📅 10:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6569">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V6vGwxqwBAc_FG1G68BQW_3Abr9AkrVJUJwJCF-i_T3BWwRGbaX8WrDiInP1IaGFbN2TICkQY-MW_xJtbCsA5ldkHqYDsq9vkKP4DM67QvMCv6ltTa8hYpHrU0Tp-0kEoXFZmG39QdPtdxQef8sLXjGyoWJov1Et-2FX6ud9PUE9a3ZidYwSfiIU-wYOjliJ6fdJ-FO4sGvP9Li-G5f_xdHnvjrsHTkcz3NHn9E55WeZ2zzMpKpNEbXT2TM1u2-sgncx_ffLkZ-pPyn1PV-9-m7AEdqkigEXDrzUB_shHdgKc72qFJoM5OAu2rehDXOVzyaLieQ7z86JDbLh4EAAkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر سیاست‌های این افراد،  از جمله این زن و شوهر،  کل کشور و جامعه ایران درگیر یک بحران  عظیم شد، آنها از رانت‌های بزرگ حکومتی  برخوردار شدند!  سید محمد هاشمی، وارد کار و کسب شد!  از واردات قطعات سلاح برای وزارت دفاع تا واردات چوب ! از جمله پول…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6569" target="_blank">📅 10:06 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6568">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">معصومه ابتکار و همسرش «سید محمد هاشمی»  که او هم در تیم گروگانگیرها بود،  در همین ایام گروگانگیری، با هم آشنا  میشن و باهم ازدواج میکنن.  سید محمد هاشمی خودش فرزند یک آیت‌الله است!  گروگانگیری ۴۴۴ روزه موجب آغاز خصومت شدید آمریکا علیه ایران و آغاز تحریم‌ها…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6568" target="_blank">📅 09:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6567">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sSfQYgmi52tRVI6Cl-Pg5UoqksMIAGaqzUZypttM_pGE_g0bCgwkU4X9UB6hmqD4ztSGiys_PRGNiL9VahplhVJ2Ycqpne5Xjc2XYqGlAUG2OMKvNKziHfKYuFmaT-VUJU07_VttENJfclhbZSsZkaCaMzlNpdhnDPo6fZL9Ln-WxvN11oYjknpRoyxIWascLNdzK1RqXaxRmjNnjYJWH4eGasWDNzWbEWD6lGT8EthYG_-uwtxQn7GVKu9fXqlx5RRG0rlVDzfZa_1ZFuyff-x2k7iwsavzArfvFIStwxARREU7EDA5nzZ4YLQOZri3B4BkHXr-xme3Ef48vSbmpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مریم در این نامه به مقامات آمریکایی نوشته  کارهای «معصومه ابتکار» ربطی به ما نداره!  ۴۷ سال پیش بوده و…..!  توی این ویدئو که خود مریم گرفته ولی، خودش دست به یک مقایسه میزنه، میگه بقیه پرچم آمریکا رو زدن ولی ما پرچم امام‌حسین رو!  در واقع عروس خانم خواسته انتخاب…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6567" target="_blank">📅 09:36 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6566">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">این صدای عروس «معصومه ابتکار» است! و این خونه عروس معصومه ابتکار است.  که با لحن تمسخر میگه اون پرچم آمریکا زده به خونه‌اش، من پرچم امام حسین،  حالا نامه نوشته به مقامات آمریکایی که من عاشق آمریکا هستم و بچه‌هام حتی فارسی نمی‌دونن</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6566" target="_blank">📅 09:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6565">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc4aff068a.mp4?token=REd1wwCF_HsVs1Wor1EqJf5RLobVweMlWOycLicmxHF4D7Z8Ga0BP2VfQNJQQRb2ReXB8oz9ur-jXo5ghS5V6fANPgRH36nDGeRjyBA7I3Bv5o_PAWy4Xbe3YlP1fe0gDFt8kMxIxSi5RJpc_0_cInGYaDgvVLP39KdO4DpiOYDH05F4sT8vjSkYpQYRcVIhc0yD4z-Fidx91dD8xGab9lIzS-eQjNhm9-9Y6loWH1LB2MVu8tRZsPukR1u19t9PYaFtVqPdm660ySTPHg57Omj1P5KdCRgVAs3YmHhPPrPCveMAKZSsPJoNE8naxTB3qkKZvUlUz1WtWQcShNLIkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc4aff068a.mp4?token=REd1wwCF_HsVs1Wor1EqJf5RLobVweMlWOycLicmxHF4D7Z8Ga0BP2VfQNJQQRb2ReXB8oz9ur-jXo5ghS5V6fANPgRH36nDGeRjyBA7I3Bv5o_PAWy4Xbe3YlP1fe0gDFt8kMxIxSi5RJpc_0_cInGYaDgvVLP39KdO4DpiOYDH05F4sT8vjSkYpQYRcVIhc0yD4z-Fidx91dD8xGab9lIzS-eQjNhm9-9Y6loWH1LB2MVu8tRZsPukR1u19t9PYaFtVqPdm660ySTPHg57Omj1P5KdCRgVAs3YmHhPPrPCveMAKZSsPJoNE8naxTB3qkKZvUlUz1WtWQcShNLIkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مریم، عروس «معصومه ابتکار» در نامه‌اش
به مقامات آمریکایی نوشته که مادرشوهرم
[معصومه ابتکار] فقط مترجم بود!!
در حالی که چنین چیزی واقعیت نداره!
او «سخنگوی گروگانگیران» بود! که برای ۴۴۴ روز دیپلمات‌های آمریکایی رو به گروگان گرفتند
و واضحا تهدیدشون می‌کرد.
میگفت شخصا می‌تونه اسلحه رو بگذره
روی سر یکی از گروگان‌ها و اونو  بکشه.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6565" target="_blank">📅 09:16 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6564">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f7a1d6d2.mp4?token=JV5HSQtiH4Q1Po80GvwSFWO9Yu1XvgncODcVIX_YFhxl1pXy7Y7T4p_6F0m71WhEikB_gyHfFsOe2ohrYHC_etMgK8doSxhEDmEjJBjDKvBaMUzUNRuBwM-8iiAwaYc83RgXTPivYGymmlkifz-eTX3b6eWDKnn1G9thOnY_rMSGg70eAlxSnA865Zf4IXCTjKvh-hcbn4VLEpmdXx3eJd9n7MrP8qPwTtgxWGKy5nRc_hb3NdhkGkYSisBe0SXAOKCKgDRlnK4sG2i0B2BW-nIwIzfYur1DKDh_ZQxctrFRg6x7WjcRU88uiRDpgoot82b0ic3wxZn_rq7F4B7eVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f7a1d6d2.mp4?token=JV5HSQtiH4Q1Po80GvwSFWO9Yu1XvgncODcVIX_YFhxl1pXy7Y7T4p_6F0m71WhEikB_gyHfFsOe2ohrYHC_etMgK8doSxhEDmEjJBjDKvBaMUzUNRuBwM-8iiAwaYc83RgXTPivYGymmlkifz-eTX3b6eWDKnn1G9thOnY_rMSGg70eAlxSnA865Zf4IXCTjKvh-hcbn4VLEpmdXx3eJd9n7MrP8qPwTtgxWGKy5nRc_hb3NdhkGkYSisBe0SXAOKCKgDRlnK4sG2i0B2BW-nIwIzfYur1DKDh_ZQxctrFRg6x7WjcRU88uiRDpgoot82b0ic3wxZn_rq7F4B7eVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این صدای عروس «معصومه ابتکار» است! و این خونه عروس معصومه ابتکار است.  که با لحن تمسخر میگه اون پرچم آمریکا زده به خونه‌اش، من پرچم امام حسین،  حالا نامه نوشته به مقامات آمریکایی که من عاشق آمریکا هستم و بچه‌هام حتی فارسی نمی‌دونن</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6564" target="_blank">📅 09:06 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6563">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">این صدای عروس «معصومه ابتکار» است!
و این خونه عروس معصومه ابتکار است.
که با لحن تمسخر میگه اون پرچم آمریکا زده به خونه‌اش، من پرچم امام حسین،
حالا نامه نوشته به مقامات آمریکایی که من
عاشق آمریکا هستم و بچه‌هام حتی فارسی نمی‌دونن</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6563" target="_blank">📅 09:03 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6562">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74c1b28b15.mp4?token=gZTpFvOy59wuTnb7qYWx6fnE_n4SpaKnu_xxfL26Hyoe-HZPIEIy4V9DzbVpk6L2SQKNexHMH-LCASmQDgEvZXkKGSVPyHKwp_dQNkBlDnpwBOQOzExh9DE-4cKWbAR1BvwqyoF-pUtuNXvK3JZNxhyVXehahWWsDDmxeUGtjZvy8cbLOeIT-M3v7FBm6qB3tXqX8zbefLemR10UMLB0p6yMAuA0n2VeD9qyqbPoo8WvElWARyDz_USPGY02RP_rfAbR-3Ad5KXGjsB90t4TZs4sBDFnsbvNoYOvq2q-domybMDhYrLg9SffU5FZEk63l6d9Z1SQpWFCtuAQk4SdTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74c1b28b15.mp4?token=gZTpFvOy59wuTnb7qYWx6fnE_n4SpaKnu_xxfL26Hyoe-HZPIEIy4V9DzbVpk6L2SQKNexHMH-LCASmQDgEvZXkKGSVPyHKwp_dQNkBlDnpwBOQOzExh9DE-4cKWbAR1BvwqyoF-pUtuNXvK3JZNxhyVXehahWWsDDmxeUGtjZvy8cbLOeIT-M3v7FBm6qB3tXqX8zbefLemR10UMLB0p6yMAuA0n2VeD9qyqbPoo8WvElWARyDz_USPGY02RP_rfAbR-3Ad5KXGjsB90t4TZs4sBDFnsbvNoYOvq2q-domybMDhYrLg9SffU5FZEk63l6d9Z1SQpWFCtuAQk4SdTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نفت نمی‌تونیم بفروشیم،
راه دریا بسته شده.
چرا زدید زیر تفاهم‌نامه و حمله کردید به کشتی‌ها؟ که قیمت نفت بره بالا
و به ترامپ فشار بیاد؟</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6562" target="_blank">📅 08:43 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6561">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">دیشب هیئت‌های عزادار چوبدار تبریزی و یزدی در مشهد، پس از مقداری عزداری برای امام رضا، همدیگه رو چوبکاری و سنگ کاری کردند.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6561" target="_blank">📅 17:00 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6560">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2226555990.mp4?token=BQ37zan7-Jic3349R_Rcy_KAL6r1kz9NwNYliKAQo_gyyUmyp1NrpwS6zWxvZriKnDsWJ2vJAHF4TPjToyfo8XKHoXM7RdBFLzDM59KuUeVUcMX70kQHYyvCii61NkNkEspYVFtzKy_e-SrT6uEhcUICL7CuS_6Y7awj5eMWlKOLZDUdV7bQn7LnwWtNbd2qLnDEri5AUe7kYQ5Tn13UMnxg7BsJ8xkacbouxI_3h8ccqDdX8a3heQcEP7--nD5Kgdh9S68yF9MwY5q-JJcXv_cbNpJ8sZkeRXN4t_cAm5HiFnuagTRVwETKsbFzEuGIhj4opbo4Y4toprAPRa2yew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2226555990.mp4?token=BQ37zan7-Jic3349R_Rcy_KAL6r1kz9NwNYliKAQo_gyyUmyp1NrpwS6zWxvZriKnDsWJ2vJAHF4TPjToyfo8XKHoXM7RdBFLzDM59KuUeVUcMX70kQHYyvCii61NkNkEspYVFtzKy_e-SrT6uEhcUICL7CuS_6Y7awj5eMWlKOLZDUdV7bQn7LnwWtNbd2qLnDEri5AUe7kYQ5Tn13UMnxg7BsJ8xkacbouxI_3h8ccqDdX8a3heQcEP7--nD5Kgdh9S68yF9MwY5q-JJcXv_cbNpJ8sZkeRXN4t_cAm5HiFnuagTRVwETKsbFzEuGIhj4opbo4Y4toprAPRa2yew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">و تاریخ ثابت کرد حق با آرش و آرش‌ها بود!
فهم آرش از «شریعتی» و «آل احمد» و «هما ناطق» و «شاملو» و «غلامحسین ساعدی» و…. بسیار بالاتر بود.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6560" target="_blank">📅 11:22 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6558">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea4168e97.mp4?token=LLDSBLsRomRjUEAUYZgknLnAKWwcc05MDKlnfj9_jFremZ90GfljBCTgltZjTEEe98Z295vUZa-53AHSOsmnlp4Vsxep7wOEPGp4Qi8mAUYBguH5vHrwwqg0RJC3GjJWzfUVDNVylUGsTraPJ3Crq7MFXRYzYlsHf8n_VNRic6XRmJoyMxA_XhFafTz0N0jDGoR2HCx-1nwD_2ImV7EZO9A-FQ5SJG0AMSStXNoZmIDAPQd6HTysAyA3_f5vyLxnnpGdUwm9OuJRpJTD9sKJHNXIPeDrzgRB0IsmCHSUMy2dCLKYMRnEZv5fiGUwZ1VDI57zgnVWRfgP2IBbUJ_0dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea4168e97.mp4?token=LLDSBLsRomRjUEAUYZgknLnAKWwcc05MDKlnfj9_jFremZ90GfljBCTgltZjTEEe98Z295vUZa-53AHSOsmnlp4Vsxep7wOEPGp4Qi8mAUYBguH5vHrwwqg0RJC3GjJWzfUVDNVylUGsTraPJ3Crq7MFXRYzYlsHf8n_VNRic6XRmJoyMxA_XhFafTz0N0jDGoR2HCx-1nwD_2ImV7EZO9A-FQ5SJG0AMSStXNoZmIDAPQd6HTysAyA3_f5vyLxnnpGdUwm9OuJRpJTD9sKJHNXIPeDrzgRB0IsmCHSUMy2dCLKYMRnEZv5fiGUwZ1VDI57zgnVWRfgP2IBbUJ_0dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب هیئت‌های عزادار چوبدار تبریزی و یزدی در مشهد، پس از مقداری عزداری برای امام رضا، همدیگه رو چوبکاری و سنگ کاری کردند.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6558" target="_blank">📅 08:42 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6557">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08352cf997.mp4?token=fgliIn9BS30e6zxy5PS9UWRj608Me28Ck7bp5_kOMG4G7bGNUdtLSX5xXsLVVKb29SBFdElo4mJXw9Cx8Cv0f1YLXfH_SOC168Ih_gRlhEBr2sVP3NXErrAJWGH8AVjPgQjqxI12E7nGL4qPT-GSLlViRV2tfam5ljha1pCw6TanDMPZX7rCFEPnpj9jDXanBlDiLKOPaWAGuJYIKgQnGTCbAtV5ciO4gipJZk6O6RG7QdpiHOcdAhSHRiOO2BDDvrefijx1c5-a0crIuv_Nh1Y2gkT6pTX7sbLPFFZP6gmZCOr6sX3zq9pPhqqEqXY-egIlGgUGAPLNDWr_s_0v2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08352cf997.mp4?token=fgliIn9BS30e6zxy5PS9UWRj608Me28Ck7bp5_kOMG4G7bGNUdtLSX5xXsLVVKb29SBFdElo4mJXw9Cx8Cv0f1YLXfH_SOC168Ih_gRlhEBr2sVP3NXErrAJWGH8AVjPgQjqxI12E7nGL4qPT-GSLlViRV2tfam5ljha1pCw6TanDMPZX7rCFEPnpj9jDXanBlDiLKOPaWAGuJYIKgQnGTCbAtV5ciO4gipJZk6O6RG7QdpiHOcdAhSHRiOO2BDDvrefijx1c5-a0crIuv_Nh1Y2gkT6pTX7sbLPFFZP6gmZCOr6sX3zq9pPhqqEqXY-egIlGgUGAPLNDWr_s_0v2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از نتایج حملات موشکی جمهوری اسلامی در تنگه هرمز،</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6557" target="_blank">📅 23:18 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6555">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c212d95b13.mp4?token=DHq90lXYhYq5J_vvLuFQujqJc33JSDm6y0RruTrNHuB9Jf7jOq-MAwyvv8ZAFjXuvYjnC9SCpEnyxFpSFQKhYC_cd27dDAAr-81R08_wl6zSmDWlpAkEHjrppUwSZ_TvSz3aTu3IqBwqvm4EnEw0pITmsELnf-ZtkE0SkCKEFqNqd6r5jslwuFHtZAZoKWUS5CNE50NSGXUZaZerJ-k49eanpdGJaAeUj0xONNrFgDmMEOZAm27viZJV1Xzn3n0Rai86-VOsCitetM46wOIYHXtzDNz4NGb83qmeaBtHIhhMrjCp_zWXUHY1UPATZ2ZBCf5R8aYtWQ4gwv1cBZx5bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c212d95b13.mp4?token=DHq90lXYhYq5J_vvLuFQujqJc33JSDm6y0RruTrNHuB9Jf7jOq-MAwyvv8ZAFjXuvYjnC9SCpEnyxFpSFQKhYC_cd27dDAAr-81R08_wl6zSmDWlpAkEHjrppUwSZ_TvSz3aTu3IqBwqvm4EnEw0pITmsELnf-ZtkE0SkCKEFqNqd6r5jslwuFHtZAZoKWUS5CNE50NSGXUZaZerJ-k49eanpdGJaAeUj0xONNrFgDmMEOZAm27viZJV1Xzn3n0Rai86-VOsCitetM46wOIYHXtzDNz4NGb83qmeaBtHIhhMrjCp_zWXUHY1UPATZ2ZBCf5R8aYtWQ4gwv1cBZx5bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک نسل دیگر ،  با بیماری و سوتغذیه در ایران بزرگ خواهد شد.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6555" target="_blank">📅 23:17 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6553">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TYzlt-AROjfnTVcGR2W--GFMMS4ObGaG_gE5Ol8Xzl75CxKseO7w9jhyU2vWjdiXzbBg9LLD2LygUO4kOqTnRTJigLhm_hXHsP2fP87zevaiYalskj_1DxclqH9-jSkMfTNoJ4MgZkT4mogm9k5avIHpxvvaF-KfozetOkdD6fQ74z07BnT8AXshmjLhfo4v9qg-lBW_yiGo28dR538JnZ5ISqc-Tf3_O3gmxOKQKuoFbG9LPvPJTpwRSyZvc9S66B3DQ6cvGpExpfNyOZyejkhR1_gbYdMpTxYULAuvvaNhAiNOIL-AzRwNJ-TtmNWY7IrsFL-eXNL84Yh4ZDk3qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6253088b91.mp4?token=ZCWLpPDyT7HlzSEBpWP_B7SKzIMMRiLT7NZ9bkMlgjSL5Ws14bRlLi7r3Lhg44nfem9Bvq9gGCMv0lVjVnGp0NJCuklVcUlnavC-xbORO6tBZLy_CzpeXcERvCIvwAVq54GqHZjiAIFC8oLqTBbtSwyGIiDD1BVXAISXgx7pJY1IDzqRwfRc_D0Cr0a0VhOk9EzzGjZWiJsherYH7TEZ2jrTW0b6HFUghO6Bod5IzJcqR3lFLEJPKpq0uNm0PCPHngy_-v6mxIHsvgkl67_F3x_evn6emaNxoc-YvYlhFGjNr8CKNW2Ods9xvw1Muz0wM5u89G_rBvmZy0Wg_Ugcsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6253088b91.mp4?token=ZCWLpPDyT7HlzSEBpWP_B7SKzIMMRiLT7NZ9bkMlgjSL5Ws14bRlLi7r3Lhg44nfem9Bvq9gGCMv0lVjVnGp0NJCuklVcUlnavC-xbORO6tBZLy_CzpeXcERvCIvwAVq54GqHZjiAIFC8oLqTBbtSwyGIiDD1BVXAISXgx7pJY1IDzqRwfRc_D0Cr0a0VhOk9EzzGjZWiJsherYH7TEZ2jrTW0b6HFUghO6Bod5IzJcqR3lFLEJPKpq0uNm0PCPHngy_-v6mxIHsvgkl67_F3x_evn6emaNxoc-YvYlhFGjNr8CKNW2Ods9xvw1Muz0wM5u89G_rBvmZy0Wg_Ugcsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل در حال خلع سلاح
(محو سلاح) گروه تروریستی حزب الله لبنان
اون چیزهایی که دود می‌شوند و به هوا میرنپولهای ملت ایرانه که صرف خرید سلاح و تسلیح این گروه تروریستی شده.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6553" target="_blank">📅 20:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6552">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZK5rt8-cqXNXtyEmNFbv52QaVzgj6fgoFqRCYfe12n3kvGbD7IjOpiDEMMGt0TeSJwr6r2tdg_haAqMVqs8T0McEG1hZ0grddIbFkuQOXicmLhfOxEEiecuU10BST5wV2xh_tjL5SYpigP9mwqzUODCjKfZX4_3S49LgmjrVNtBgIU7a-AFhBstL_SiJ8OovNakhe5LbO7bYreGItON-isPF6-UGgZS90Y9lJGBLWj2BL6Kzf9fXFIl49FMw-vzUMCy1qs7cJXvkirXuRCUmjEy8R_0twADS0buYLFMN1v_vdur0744J2EU9NPmeQq7FoVDYlrj9q8bZz1guGyRiYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا اون موشکی که زاکانی گفته بود دقیقا به خونه‌ مجتبی خورده بود و خودش از اهداف حمله بود، باعث ناخوش‌احوالی مجتبی شده و گفتن پول واریز کنید  زخمش خوب شه.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6552" target="_blank">📅 10:33 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6551">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔺
آمریکا در آخرین هفته‌های سال ۲۰۲۵ (قبل از شروع جنگ ۴۰ روزه) حدود ۳.۹ میلیون بشکه نفت در روز صادر می‌کرد.
این میزان در ماه می، به رکورد ۵.۷ میلیون بشکه در روز رسید، یعنی افزایش ۴۳ درصدی صادرات نفت.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6551" target="_blank">📅 10:29 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6550">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">وقتی ترامپ در ترکیه بود اعلام کرد که با «ایرفورس وان» ترکیه را ترک خواهد کرد.  جلوی دوربین‌ها وارد هواپیما شد،  اما بعد از درپشتی خارج شد و با یک هواپیمای نظامی ترکیه رو ترک کرد!  نگران از تهدیدهای جمهوری اسلامی.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6550" target="_blank">📅 10:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6549">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZGfufQ0rvYiwdhx3V1eK4Mmoy4t2KifRwi46wfD_YMBAA4LecTA_GvBQT54Rn2rpvLmTG4g3zCAGyXq1LAkNlJcsQjbVbhv2sEygXXdGy_all3D1791ARiBQoT_nTJ1uFM_LSfFQXKg3vuFkSBw-_1cw1C56oqK_FULrIM7PS_F7wLZ_zITv-Xb3slwAeS7y8bPvFsrPKt7ZbkXLfLuJdGyp0U5WxD-gE-800TtumJF3UKFwLPFkqNcTXsInBuUZizE0kc0bKomBPbFm0mnCRigSRhC-Y96oYnz7xKv1MUqcYwUOuiM0fho0iAGfmlqvJ06eSfSqjGuEbr1LAi3Unw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لکه نفتی به جنگل حرا رسیده
و حیات درختان این جنگل به خطر افتاده.
اما این لکه نفتی که تهدیدی برای سواحل قشم شده از کجا اومده؟
جمهوری اسلامی ۱۲ مرداد (۳ آگوست)
به یک کشتی باربر (و نه نفتکش) حمله موشکی یا پهپادی انجام داد. کشتی داشت از آب‌های ساحلی عمان عبور می‌کرد.
پرتابه به موتورخانه کشتی «مینوان پایونیر» اصابت کرد و نشت نفت رخ داد. این لکه نفتی رو موج‌ها آوردند به ساحل ایران.
سخنگوی وزارت خارجه ج‌ا (بقایی) هم تایید کرد
که این لکه نفتی ناشی از یک کشتی‌فله‌بر است،
گرچه نگفت هنر دست خودشونه که برای بستن تنگه هرکز به کشتی‌هایی که در سواحل عمان حرکت میکنن، حمله می‌کنن.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6549" target="_blank">📅 10:15 · 22 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
