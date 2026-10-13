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
<img src="https://cdn4.telesco.pe/file/EO0Bb_JHu0cFOZvaT0eEsTScVUdqID8C85REbE7mNDK9OQqx4b1nAgYtTMc-YT-g_3Sw0l88g3DXi8iRgQez8q5P_V70wsJM969k96u1aLl184wNPQ6MvxX315jGIhFxf6HaGCCDiIsDgcNQMlB_BsxNc7dh_M-0R3548TfZopx6mNlYWyUUJr5ZHbVgwRBIOkPOl2iARAmajqS-8EModarv48BvDp969nFclUzJoBCiTfNrmiPK045PeD4rbzhbDX6nBgQNDGasdpTZhYbr0jHBsQ3lty3r1Zrn31uCKtjELRmY4JgTpjrFJq8CzWsUpVP9tfNbGlGokP7IJ8N2KQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.46M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-21 15:51:52</div>
<hr>

<div class="tg-post" id="msg-698075">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
علت قطع سامانه ۱۱۵ اعلام شد
شروین تبریزی، سخنگوی اورژانس استان تهران در
#گفتگو
با خبرفوری:
🔹
قطعی سامانه ۱۱۵ اورژانس کشور به‌دلیل اختلالات فنی در شبکه مخابرات رخ داده و رفع این مشکل در دست اقدام است.
🔹
مردم می‌توانند تا زمان رفع اختلال، برای دریافت خدمات اورژانس از شماره‌های جایگزین استفاده کنند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/akhbarefori/698075" target="_blank">📅 15:49 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698074">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
معاون وزارت رفاه: تا هفته آینده بخش عمده‌ای از مطالبات را با فروشگاه ها تسویه خواهیم کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/akhbarefori/698074" target="_blank">📅 15:47 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698068">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XuqwSKDdpweqtwjUEecf2tc31AQXxuunkzO8oa_hpFqw4fnBoC2i_OBF7mxqwMboUSdVig1OCvNqb3qnn08mSrKR8ZIrJhosPYjxpu3k1GcsSyUZ2XHlK8dDD2Qbv6jFAtV1RyDS9MibGzMXtFfciSuBFXfng-nVYhJK86EdUCdSlfsg8aXDha0NCxf9HvwwRroxTz9jOEMOaYh9u11GOhS4FXgmR7LX8rNfS6qvSxb5itB0yNxSXci0PZqNTcgzcd91Y8xWfi8-DZOKlBe_L7WDhe8Sojcj8mVkiUE03NStv9Z77u_IVM9e6csl3WMTRylKfMC-YktK15S0BSCpLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vqraMdAWXL3BnBPZIar_xRVXIlTtJuGgK_gmEhRRahEZDwuEgsBWkKFKuC6KNFVjesOHu6TYRzllVXJCgrTonpl0-wY3HB_G09Hv-UaCSOv7DgGgo6vsAJeg_OSXVfiEvxpNDjKrnnkhXt0kUyGWMIyhvv1RDCmWOHBKapVjD0bx_wSpmKi17DCExtCmCZa_1SSX1WPsd4QWmCL2L4MfC2jb0E2mX86dmlmQGdjoE5qyTtZya2A_IVCxPZ8upSQCWRiLgK2FEI0GuBX2CZYaOwzH6BkhmAeQ6VsCe18EhzYSPlTAS2WdvoU-bb8Dy349xGEMrmydNNy8W28AGhCGuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ib_nd6oQBRzIoamzYkUp13XtUs9ln2-aGpASKF192VOV9JNadz5Myxefmqtej_1UsxQk8C7_7lhSCXoewwgbE0Ej5KMsZow_crPtSfX76bxgbrbfTVjtwSS5nk4OH1SAdSTUWsQZpZTOBGbmbpjIrv0ZtOJz2XI6xE93GHdATG8KRh9BJx1mWcEo1-rDdD7ndw2pG9q8_ML9svAWEdfugJh2_FwXQ018UbqlQhHNbh5sjyWlIMZOcYWjN_DYRtYS2CCsUbH4G14IN002tkoratLDSTIdFe8xbI-40zbNLKxgVkGcvp7oIGEATp7orpguk5NmcU82VAA12wjvYlx54w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KvbU-wBIrzAphfVZbdyYJDmtbs5R1i1J16SlCTIZyRz8sqUbouSYC3mayb4j6ZWWnZVxgNwd8Tz4LncvOo9NP4gHA9zSSCjwua1y33skp5xF-EMEW1nmeKHeJxfIJVnS9F3rn0vnnn1WeGYCTmnsaGodfhI2C62uxBw3iwuxLPVb0bY50lMlD0uRlPK8gPc_4PYEp152jtN9cQNFCoxpxA7YHbNn987qnHWa08f8H26Wppa49JeuqE2VRlDmr3S-bJpyz9N9-OpmkfrJoufQ_6BfzFPEU5q09qIgTKsb1vxiYgfYsUCSbGhGKed_-TBRRLwJQe8CmchRpRFk-n-m4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lxMzYErchqRpL_VQVR_Vb63MuTZ_3UcQ-JZRsKojUK4p6XA5kjy6ACdQWWIBVsCajYbj79fXsMlsNpg5TzDHcbnNoyA4taMEDXN9ntqD6PpJBqTimD0RFNp__kfmweHfkOkZtNcE2Dlvrqov0lj-ilmPLINAd-pzoFG69xZ2KpKW-7g5N2Vn3BqHYmE7qUJ3OjJipldhnNRh36HbsxHEo2Lp5kj0xQGr0OA_GFGeRe7JzzdDpUJZ6halQcEFcuai72xmq7yrp7bRAL1E0ETrl2Cia5MSpRaRtQcGVn_U5Ot4vHtJeLJ882N7KZu1qO-juc1E0cOOLntuFmvgvDDj6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VGfMA78BjvECSopxyJco1xvtigqEgcNM2ZhbfispM-TqHMorpO7a7Jp7j5qq2E6EMckdAH3-Jvzj7QR8rDO5eOjT0qfdseRa9BUg5oknh4KtajhNd9V1v2LBMDQkyB8C98jAjjtZuxzjbH7gFFLtgCPM9LUYvxWcxHoiiW9Xf9Nv-fFVQgU6jWywQ35MZ-hQ5I4HOY0EY1YhZBRCykXkJkdAMX3z2BdLQlZ9KmsFaGQsvD7tDkEbGo4k9qG2MmxsXy4ivcxLlveXMXvARaleizlcud_7Hi3Pou6R1G7rg6C5Q46UHj3zpd4WvFLc9fCW9m198N9QUvfQhHQzvbceYA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⁨ ⁨⁨ ⁨
♦️
قبل از خرید کفش، این تست ۳ ثانیه‌ای رو انجام بده وگرنه قطعا پات رو اذیت خواهد کرد!
👠
#فوری_استایل
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/akhbarefori/698068" target="_blank">📅 15:43 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698067">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
رئیس جمعیت هلال احمر: برای هر سناریو از جمله حملات هسته‌ای و شیمیایی آماده‌ایم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/akhbarefori/698067" target="_blank">📅 15:40 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698066">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
اورژانس استان تهران: از دقایقی پیش شماره ۱۱۵ قطع شده و شهروندان برای دریافت خدمات اورژانس می‌توانند از شماره‌های جایگزین استفاده کنند
02146015981
02146015619
02146015948
02146015734
02146015732
02146015873
02146015613
02146015703
02146015648
02144896391
02144891399
02144891525
02144896345
02144896376
02144896389
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/akhbarefori/698066" target="_blank">📅 15:30 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698065">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s2_z46sRNI6AiwY8Tvlg2058l4DjjxVRxmCg5cAp0Bw2EO6itPCYBiztAzHh2An1aMDIoGv8MPKetY9iP89ge7CZe7w2UIUReuqcZ8FjeWrplDYj5c3tQbsBi6QLbUuwILDMBQ4gTmeCr574CXjHSdDy0DifJ-XvK9GwmOOyFvVxFRmSPW8zrev8-9Xzp6COlEXBRwKanquFKwOI2bUIUnei0FHz9vaFdZQdFvZpGE7eIuBTp0PEbP1oq_ClpeY3ElZY34-Js3omkElJ02VNpKv99_Pgc1_RqIdR7NadgV2JkQgUWjTEBmVsI15hKCnXQmv4yUZ6B_PxkPu9eLQFtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تغییر محسوس در شاخص‌های بانک سرمایه؛ منابع بیشتر، مطالبات معوق کمتر
🔹
مقایسه عملکرد بانک سرمایه در ۱۰ ماهه اخیر نشان می‌دهد شاخص های اصلی این بانک با بهبود همراه شده است. منابع ریالی ۵۷ درصد رشد کرده و سپرده قانونی نیز با افزایش ۷۲ درصدی به بیش از ۶۱ هزار میلیارد ریال رسیده است.
🔹
در مقابل، اضافه‌برداشت از بانک مرکزی ۲۷% کاهش پیدا کرده و نسبت NPL از ۴۷ درصد به ۳۸ درصد رسیده است. کاهش این نسبت، یکی از مهم‌ترین نشانه‌های بهبود کیفیت مطالبات بانک به شمار می‌رود.
🔹
رشد ۳۳ درصدی تسهیلات جاری و جهش ۱۴۹ درصدی تعهدات مشتریان بابت اعتبار اسنادی و ضمانتنامه هم نشان می‌دهد بانک سرمایه علاوه بر تقویت منابع، در مدیریت دارایی‌های خود نیز فعال‌تر شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/akhbarefori/698065" target="_blank">📅 15:29 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698063">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13ec73489d.mp4?token=lANqTTnaHusVxzr_BmoiH2BysmIm1Q6pp_YoUX0ZHVZbxrWLNqe1lPFNa3qM0s33pJ5xV-besdRXY7fstQ7zECLwB9Jto-Tk31_2dXHcC6v1WWdwO5T4Or6PEF07DD-CXPeljgEL5rMCN6zjUj0sRVDoPMJHgKfpmYJNwqEl0NLHRSc1OM0QqHlo3sGj9Cq2Kgl5JaSlkxtSE_qM-op1grAMQQXhd7jQejkRq-Tv9m53Bx4Lw7_WS2firmKHxydpMpA1pI0__-352S-LXNQolzRdEnLZ4TLFMVeqxDJci-z-DQvMAuUh1i8i0EqoirXUju6cGfHAqig-lfySYtSJVFkfYMreqDrk25znnBRlNKHRrLj2IjdJ5PvPFI29nu22xR9TwJXVAyeWpN9VyufvqFgZNT93cYkSX4FwiVWC84_DKy4-Uwfvt1pey9zUBRpUaDynwTXO4lU6mLfizqJIb2pbKD9j-rZr-03Jb5ThSfHwXlN5FVjddZ_5rVeeuxs4hoCDYd5ApJB01vYgiph-UECzoyB9in4LoKpvL7qGb8Zkt4Mx7sW2tgtPs50RsE13Ix2TyP2pL87yQUZXC6hsF6cTaWx-wTq_IT_bsd_KbDPun5zYwmeZRvg2JX9i8kt0bYsVpY3ESM7hW9UGY_ZLfQdA_RZiCsIF7Bm5B8OBHpU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13ec73489d.mp4?token=lANqTTnaHusVxzr_BmoiH2BysmIm1Q6pp_YoUX0ZHVZbxrWLNqe1lPFNa3qM0s33pJ5xV-besdRXY7fstQ7zECLwB9Jto-Tk31_2dXHcC6v1WWdwO5T4Or6PEF07DD-CXPeljgEL5rMCN6zjUj0sRVDoPMJHgKfpmYJNwqEl0NLHRSc1OM0QqHlo3sGj9Cq2Kgl5JaSlkxtSE_qM-op1grAMQQXhd7jQejkRq-Tv9m53Bx4Lw7_WS2firmKHxydpMpA1pI0__-352S-LXNQolzRdEnLZ4TLFMVeqxDJci-z-DQvMAuUh1i8i0EqoirXUju6cGfHAqig-lfySYtSJVFkfYMreqDrk25znnBRlNKHRrLj2IjdJ5PvPFI29nu22xR9TwJXVAyeWpN9VyufvqFgZNT93cYkSX4FwiVWC84_DKy4-Uwfvt1pey9zUBRpUaDynwTXO4lU6mLfizqJIb2pbKD9j-rZr-03Jb5ThSfHwXlN5FVjddZ_5rVeeuxs4hoCDYd5ApJB01vYgiph-UECzoyB9in4LoKpvL7qGb8Zkt4Mx7sW2tgtPs50RsE13Ix2TyP2pL87yQUZXC6hsF6cTaWx-wTq_IT_bsd_KbDPun5zYwmeZRvg2JX9i8kt0bYsVpY3ESM7hW9UGY_ZLfQdA_RZiCsIF7Bm5B8OBHpU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کفشک تیز دندان یکی از عجیب ترین ماهی های دنیا با شکل خاص و گوشتی لذیذ
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/akhbarefori/698063" target="_blank">📅 15:28 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698062">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
منابع عربی از شنیده شدن صدای واضح سه انفجار در شمال شهر ریاض در پی حملات پهپادی یمن خبر دادند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/akhbarefori/698062" target="_blank">📅 15:22 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698061">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
تا پایان روز ۲۴ مهر ماه فرصت ثبت نام برای افزایش میزان یارانه نقدی تمدید شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/akhbarefori/698061" target="_blank">📅 15:16 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698060">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
یونان دسترسی افراد زیر ۱۵ سال به رسانه‌های اجتماعی را ممنوع کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/akhbarefori/698060" target="_blank">📅 15:12 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698059">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ahcSTKCI39CRSiU9aRxcgDjpe7ldqZY6QhoSXz6G0kf-fgwFS9szLbmeI4z7G_pumpB_zXm3bdUcz76YuR59YP0UZ0VeGRlldvuIIsXbtWJ4ahSu_HCTWZ8BoOCIRCLW_E0dOo_Ik_L5iDq1OC46JDkBd3gP1FTfSuO-YBnlayaDPX6EEJGK45o-eHQ45n2yOBDGkCY2x0Vy8gOY3L08Y4xnUxgxlfqVE--tg_aQ_eZ3UNiWx9DtU1PWCPGt2NsXA5mz4ps54gR2Mk-7LFaUXierTO3FWpKHuKlxw1zcfeKX-P78HxxmD8IAfhJC0qus3BkPzyDR7oU7dWg2bEzpog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۸ قهوه به سبک کافه که بدون دستگاه اسپرسو می‌تونی آماده‌شون کنی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/akhbarefori/698059" target="_blank">📅 15:00 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698058">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
ترامپ در پاسخ به احتمال کمک آمریکا به عربستان در برابر انصارالله به خبرنگار العربیه: به‌زودی خواهید فهمید
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/698058" target="_blank">📅 14:54 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698057">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">جامعۀ مهدوی/ج۴</div>
  <div class="tg-doc-extra">استاد علیرضا پناهیان</div>
</div>
<a href="https://t.me/akhbarefori/698057" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
جامعۀ مهدوی/
جلسه چهارم
حجت‌الاسلام پناهیان:
2:30 ظهور امام زمام مهم‌ترین مسئله کل تاریخ بشریت است
🔹
10:20 ضرورت اتحاد مسلمانان و مسیحیان در آخرالزمان
🔹
17:05 ایران امروز، عامل بیداری تمامی جهان
🔹
25:00 علت پایان نیافتن دشمنی غرب با ایران در طی این سال ها چیست؟
🔹
31:00 آیا ما در جنگ با آمریکا پیروز خواهیم شد؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/698057" target="_blank">📅 14:49 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698056">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
پیرهادی: بگذارید طرح شروع شود بعد نقد کنید/ طرح تورم صفر بار روانی خوبی برای مردم دارد/ هجمه های برخی رسانه ها جای سوال دارد/ موساد پشت هجمه ها است
🔹
پیرهادی، عضو شورای اسلامی شهر تهران، با انتقاد شدید از هجمه‌ها علیه طرح «تورم صفر» شهرداری تهران گفت: هنوز این طرح آغاز نشده که چنین حجم گسترده‌ای از حملات علیه آن شکل گرفته است. اجازه دهید طرح اجرا شود، سپس نقاط قوت و ضعف آن را نقد کنید.
🔹
وی با اشاره به بازخوردهای مثبت روانی این طرح در جامعه افزود: مردم از اینکه اقدامی برای بهبود معیشتشان در حال انجام است، احساس امیدواری می‌کنند. چرا باید پیش از آغاز اجرای طرح، این حجم از هجمه علیه آن صورت بگیرد؟
🔹
این عضو شورای شهر تهران با اشاره به استقبال رئیس‌جمهور و برخی وزرا از طرح «تورم صفر» تأکید کرد: این طرح سیاسی نیست، بلکه اقدامی معیشتی برای بهبود شرایط زندگی مردم است.
🔹
وی خطاب به منتقدان سیاسی طرح گفت: «چون آقای زاکانی این کار را انجام داده، می‌ترسید موفق شود؟ به خاطر مسائل سیاسی خودتان می‌خواهید معیشت مردم را ذبح کنید؟ وای بر شما! چگونه می‌خواهید پاسخ مردم و خدا را بدهید؟»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/698056" target="_blank">📅 14:47 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698055">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S-vqti_GzidsR3PXhK-2Q_p6GRrzzqN1q7_IM9xjqdtrPr5ZxQf8KT30lTSxiyAkT3Ldu7Mx5FvUe-_m8rb20pl6tlrCvlsh8ApKHQAKmjtJCDEDfugLsyrLflhuHQsXYmQ3GKf5KESFVKIyjG9xz6kVdOqPxvnPC7loiGHOHGSOdQWBNgKQSPiddI0v9ilFaqozHgF15i54P5Cb2h_Co0iTFSQh9sA8slhwSZm0hvfHBO3poE_hM0y7u6ucdnjh_x1zLDndJ8-MDPun3D62MEvl74uggJxY3iKYKWtTQ5aLI49lO2Ejyapk1XFiIw1gUFuyGZz4_Tfv9cofeDxvVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انواع خرما‌ رو با شکل ظاهرشون رو بشناس
🌴
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/akhbarefori/698055" target="_blank">📅 14:42 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698054">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
انفجار کارخانه در رأس لفان قطر ۱۳ کشته و ۶۶ زخمی برجا گذاشت  وزارت انرژی قطر:
🔹
حادثه انفجار در یکی از کارخانه‌های منطقه صنعتی رأس لفان به کشته و زخمی شدن ده‌ها نفر انجامیده است؛ این رویداد یک حادثه بوده و نشانه‌ای از خرابکاری یا حمله در آن وجود ندارد.
📲
🇮🇷
…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/698054" target="_blank">📅 14:30 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698053">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
وزیر بهداشت: در ایران سالانه حدود ۲۰ هزار جوان در جاده‌ها بر اثر تصادفات جان خود را از دست می‌دهند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/698053" target="_blank">📅 14:22 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698048">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/U_BUOsH6FFzdjUy_-DBeGL1noJzk7QSgX5r5M_5w-Zlro2y7tnE5TmJBakgFn9PNtmwWtA-mkswwhOSqxh08kb7ZbuxTEt-6YPWbCezNtVzS-oALIYh0Of2ekg-hgLUBm1aX8ojFNQsZtvGvRtu4VBsfSXvo4GqPaYQfY-8x7lE3L-hwAa6VjR5C8ri_pcPLCWdx9zfvQuga3TOJOA2JoBtbp_JSRFBnWralF6oWhRVUHDvqhNvX1Wg8KJUw3-JSkGH1jlG2QhBDcHXGxdeUiVaygTUumreKqUT6JsLjMELpNni6YJzlIJ4Gd71EXY8wKrx9QnE3UmT5tBFyw-q1Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UxUfVI4ZBAlabeNH8DKlnyqhRuHvWQ7YA3LQyrsbAt2i9hfuUZCRtX0gSPNRBbpnyPFtG1KISFOLlrgTodmB27xKuWCqMvVUPPqYIPvSInCDcR-2rfh2rI6jZGonHvoO4NW4hzlHALYxoceppMkL5EdmvajysBwh4g1a15z87VDfLhrulTJQSoZFfcJvm0xFnO7qlf3xSi4mitPfNxeGqtuzUxNBXeKCkL8TqXeALgvuOfYVwYTfjfWF5vkOjLJe2yLojtfXMQF3lUyBfTzOPXJQEWB5akXDnxO5jt3TcARB2XZ6ehFWUFFbZ3Y0RJrGDLp-FvxLJSZgCfl3Mm8rcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pBgrYbitL-8Ws1nWwlmxlyDwrm2CMTsdJsdPrbAu8PkQ1jKaUfoBfWK8GNywMKWxHwXp7Oujz65Sq6S_XmibyH_YdSBrEdic7EDAsaISvLA6gofWPuUCw07jtZDae4VPiI1y0KhzHLpOB8KTqwbEy9zQlfLFT--NjvSVStSTpWZmQGpmzFc6FtyWYT_OX2qM9ukGJ8J1IDjzCglc7tRGd-5qJrBQUpuw2UNLmPhwQ7s8dwsa51OOQ-1moDCE2r3J9kwJM9F04HF5AjgAHCP4P0RsEGCJCRHJFWsORKYECpTKv8Bv16kz2D44UAADPmuP2pluFH8B8sJriVtQ3hh6bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QDpMKeLcmEFeA-FRg55T17IX_SnAymvMi8SeFu2CnpxCi4T7OwVvIhETOff3SbAqxR3j0T0PPfQoQZZza4ivS-2ZMA4PRRvVOYmGWFfx0vPpqT4ZUMJPigiHRPceAK6wKbHvUJVZAG7cro-trW9zdc8tVbBzh0FTnNXVzidndqTdhFKRUBJQWJvnyY7itKX7A12HEJ9Gunw2rR8ECOjmNFPLsCc6uQNZuaGY_WTF3XxFywssCeEUL4CGUOE28DWBhnYApmliESoAv__mYCYm745rrAr0W1J34aqssWnRE7apo-vg1-5SbwU8cwR_A6sTGmwF698iyMuOjfQB6N_pxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WANJZNQtwO0h21sPecT7nmO3QbWz8vN1MGwU-WsYZrM8P2EPOQuYbd6hnjKeMzEbxcIkSNxETzFz64BaT3W1pqQcAED17FAmHOv4lPRc4aE2DrX50YRtLA-vF7htqsJRyIv3_TEHQc0jP-qONzsG8z_v9Oyu2v2zZXOnRu1mWkTOTvUV3yA8QpQJUjldPswioD_hubTk5yWKW_IxQ8EQltBX8zQgtnKd18wafkMBbnKWUm87cEe2GXjpRXUrYTpGeyMBPj5ndLwcEB9nLSU35ANV6CIVnmmNQhcRFprXY8WaYZiOBvD8aIpIbygGOvAMAA8TwSRN3TsmcBs_B_AIKg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
معنی برنامه‌های ماشین لباسشویی؛ راهنمای کاربردی برای شست‌وشوی بهتر لباس‌ها!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/698048" target="_blank">📅 14:20 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698047">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FLo6lLFM7b54oifnznrmR22CudO5Tq315kArqSQZkTqjrBC48WBfZf6Sw0q-VoSVXvxNA7KO4-IrzqstTufU3lVfqzNR3Hp37JRFIQwN3HRcbhuOOoqBL6HZDubf-1JTYoq_HiTjXS_GdiL6g8SxuZqef5-Q7GO5L1yCCEN1yPeFKqrs0FKmbDxgPebsh8pFV1d4LEckKc_EQkII1ve7IKE0QuLNoAjBmaii8pwEzDcHpVgJ-w-tmTgM4KybUtzfARUeflXskLjFFMigLPsoqIk_mMIqZV5crq1g4ngvnbahSHsCMtI61_oMwz1AvKQ6fPg5Ha9qP04zvApcS0nwIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خانه دیپلماسی برای شناسایی استعدادهای حوزه روابط بین‌الملل
🔹
خانه دیپلماسی از علاقه‌مندان به حوزه روابط بین‌الملل، مذاکره و فعالیت‌های گروهی برای شرکت در رویداد استعدادیابی «مسیر رویش» دعوت کرد.
🔹
این رویداد با برگزاری آزمون‌ها، شبیه‌سازی‌ها و فعالیت‌های ارزیابی، توانمندی‌های شرکت‌کنندگان را بررسی می‌کند. عملکرد افراد در طول رویداد از سوی هیئت داوران ارزیابی و امتیازدهی می‌شود و در پایان، افراد برتر بر اساس نتایج ارزیابی و شخصیت‌شناسی برای استخدام به نهادهای معتبر معرفی خواهند شد.
🔹
علاقه‌مندان می‌توانند برای ثبت‌نام به نشانی زیر مراجعه کنند. اطلاعات تکمیلی پس از بررسی سوابق و رزومه در اختیار ثبت‌نام‌کنندگان قرار می‌گیرد.
🔻
لینک ثبت‌نام:
https://diplohouse.ir/?p=9343
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/698047" target="_blank">📅 14:18 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698046">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
اگر آمریکا تضمین امتیاز هسته‌ای و عدم تکرار حمله ندهد، مجلس با ادامه مذاکرات موافق نیست
عباس مقتدایی، نایب رئیس کمیسیون امنیت ملی در
#گفتگو
با خبرفوری:
🔹
هیچ اعتمادی به آمریکا و مسئولان آن وجود ندارد و افکار عمومی آن را پیمان‌شکن، زیاده‌طلب و غیرقابل اعتماد می‌داند.
🔹
اگر آمریکا حاضر شود بخشی از تحریم‌ها را رفع کند، اما درباره تضمین عدم تکرار حمله یا مسائل هسته‌ای امتیاز ندهد، مجلس با ادامه مذاکرات موافق نیست.
🔹
اشتباه محاسباتی دولت‌های گذشته درباره اعتماد به آمریکا پس از یک دهه برای همه روشن شد، اکنون حتی جریان‌های محدودی که پیش‌تر به تعامل با آمریکا باور داشتند، به این نتیجه رسیده‌اند که در گذشته اشتباه کرده‌اند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/698046" target="_blank">📅 14:16 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698045">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
مرگ دختر جوان در ژاپن بر اثر سقوط زنی از طبقه یازدهم
🔹
زنی ۲۹ ساله که قصد خودکشی داشت، از طبقه یازدهم یک ساختمان به پایین پرید و روی دختری رهگذر سقوط کرد دختر جوان جان باخت، اما این زن زنده ماند؛ گفته می‌شود این زن به اعدام محکوم خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/698045" target="_blank">📅 14:11 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698043">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd2b4417c7.mp4?token=cUJFYcHvoifcvS_6d9HbS5oNb71xh7iU7S-ylShp43Zy_rb99V6kQhBBE7-hN9s51f8sDq7dA5fW5guUqjvflQKWOOWjYApK6GjePTy1JSGr6JDEWDCABBH2mCEqJhsuVE1vOhVXA1MylWfWrSHWUniMYoLrixFQfpI0lqAgFae4wdDGpoN50q1zZU0uOvxSBQaG3LXP0Dqv8z6L9MlLoo_1Re1woz1tIfGquw_BZUzSNH4yQf6krBYARy2EMfeqADtsaIPeDg_6rSoE_A5rTu-VFsix_exVpe2_XB19vm7J1IbT0O_cPeFZMlRCBx7D9SFBlBs7U70XWVVZ_Al_Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd2b4417c7.mp4?token=cUJFYcHvoifcvS_6d9HbS5oNb71xh7iU7S-ylShp43Zy_rb99V6kQhBBE7-hN9s51f8sDq7dA5fW5guUqjvflQKWOOWjYApK6GjePTy1JSGr6JDEWDCABBH2mCEqJhsuVE1vOhVXA1MylWfWrSHWUniMYoLrixFQfpI0lqAgFae4wdDGpoN50q1zZU0uOvxSBQaG3LXP0Dqv8z6L9MlLoo_1Re1woz1tIfGquw_BZUzSNH4yQf6krBYARy2EMfeqADtsaIPeDg_6rSoE_A5rTu-VFsix_exVpe2_XB19vm7J1IbT0O_cPeFZMlRCBx7D9SFBlBs7U70XWVVZ_Al_Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مشاهده دود غلیظ در نزدیکی مخازن سوخت فرودگاه دبی
🔹
تصاویر ماهواره‌ای از مشاهده دود در نزدیکی مخازن سوخت فرودگاه بین‌المللی دبی خبر می‌دهند؛ علت حادثه هنوز مشخص نیست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/698043" target="_blank">📅 14:05 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698042">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
گام‌های تازه مؤسسه اعتباری ملل در مسیر اصلاح ساختار؛ از واگذاری سرمایه‌گذاری‌های مازاد تا بررسی افزایش سرمایه
🔹
مؤسسه اعتباری ملل با اعلام مزایده عمومی واگذاری سهام شرکت‌های تحت تملک و برگزاری مجمع عمومی فوق‌العاده با دستور کار بررسی افزایش سرمایه، دو اقدام مهم را در چارچوب برنامه‌های مرتبط با اصلاح ساختار و سامان‌دهی وضعیت مالی خود در دستور کار قرار داده است.
🔹
بر اساس اعلام روابط‌عمومی مؤسسه اعتباری ملل، سهام این مؤسسه در شرکت‌های اعلام‌شده، از طریق مزایده عمومی و با شرایط نقد و نقد و اقساط، به متقاضیان حقیقی و حقوقی واجد شرایط واگذار خواهد شد. این اقدام در راستای واگذاری سرمایه‌گذاری‌های مازاد و حرکت به سمت تمرکز بیشتر بر فعالیت‌های اصلی مؤسسه قابل ارزیابی است.
🔹
همچنین، مجمع عمومی فوق‌العاده مؤسسه روز سه‌شنبه ۲۸ مهرماه ۱۴۰۵ در محل ساختمان بانک مرکزی جمهوری اسلامی ایران برگزار می‌شود. بررسی گزارش‌های مربوط به افزایش سرمایه، اتخاذ تصمیم درباره آن و اصلاح ماده مرتبط در اساسنامه، از محورهای اصلی این مجمع اعلام شده است.
🔹
مجموع این اقدامات، بیانگر پیگیری برنامه‌های مرتبط با اصلاح ساختار و بازنگری در ترکیب سرمایه‌گذاری‌های مؤسسه اعتباری ملل است؛ برنامه‌هایی که نتایج و مصوبات نهایی آن‌ها پس از طی مراحل قانونی، از طریق سامانه کدال و وب‌سایت رسمی مؤسسه به اطلاع سهامداران و ذی‌نفعان خواهد رسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/698042" target="_blank">📅 14:03 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698041">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
پایان درگیری مسلحانه در کورین زاهدان با هلاکت ۵ تروریست
🔹
درگیری نیروهای حافظ امنیت با عناصر گروهک‌های تروریستی که از صبح امروز در منطقه کورین زاهدان آغاز شده بود، با کشته‌شدن ۵ تروریست و شهادت یک نیروی حافظ امنیت به پایان رسید.
🔹
این عملیات‌ها تا پاکسازی…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/698041" target="_blank">📅 13:59 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698040">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UTB94D-yElbllsLDYJXfsQgTrGf2WHc2QV4jm6msUQpEgdBr41tjP1wusHWoPs2Wa_JX0l_yvXaWDBvBVRHG2M0z5seqLB6Zc-Uo_lBMh9rAnF2jIA01L2OKPc5D3NTU3xw4ZpiIbESeDITVIlRTovuUkXkiAaqU3vec2WS_fod5hMhMN59JGxmfmVkY-m-4G5Nq3io0b0kzSniobX1JsdRUGzicGS8GvU6Gd5w3RY_2qqBngoeREoBj1rSFvLWFaBWe1CJeIdjR1Q40ZoSZMmfZpxA94fU9SPF014gtINg2MhdsgyMnHqciTNk3DSkC6Cj8B97MBB1ER8SUejGjIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تحقیقات موسسات آمریکایی نشان می‌دهد جنگ ایران به‌طور میانگین برای هر خانوار در ایالات متحده، بیش از ۲ هزار دلار هزینه داشته است!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/698040" target="_blank">📅 13:57 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698030">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاقدامات هیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bLmDLI8aE-yf5qg9txT8kc-rQjEopsb5Q-T7rAPW5CWN6FMUd0mpL0BEzL-tbSXQCvZxDo16rfH0zEOU_Y-GckaaEKwBysPp0liAPmPmGFu1Nw9Ph46yJZEiuZtCtqu-4vWcclr73Ir4FMG8FljA7um_6Q2VdKD0FTg12Zg37BeYo7BJBwY7Gb8Il479U5iDMPEZR5HQ0aS7EmTIGd_lC1GoQCKKhIhTr1ze6q24S_Jvovy_OM5s0PFI1d6CZ85rVUWRez--erS0FyD0_L91rID_G_cra-3RtLWTnNciJKWDIiSQJr8Vfrfxbh3FOD5QWnsjIHrN_MIEamByzwYMuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m38fEaig5rZheRL5xUTXxP3SIpHDeGPJPjtZQrEvKZKZQM_Q9NCMtfZjBGFGN1BdO3l4PfA4eWA2oHPaR6wkcuG_9s6DbNl15oOcdtWGhtMsFVZeeMdx3BULzOJllxX8Kavi5WTZxvyxoRVpRlVExXwh_DZ915IuDvkuu-IeqdwZyTMfUwivYOxZRse0wt97E--D0xKvpYZw7TwLzRUKzr8PQ_jSv6108txeU60RArU3PjAxiv6iRZs1mnnWfpot4WvNpoKryRGtUxTkMywf7R5OwWYA465VYAsdcJxBcOcX8Wfon_lE6Io_l0xlxvfndYh6e8RjMBLmipfSwcL52A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CBkU30Yg2Qa4ILrZZL4h93chEBjQKTQvq62vLDrfIXTY4L0TLB51RSxCg_iOMILY8SG4ryDM27VKWjdGaDBknA3EsFdoikNnZr1qCljvse5kdJcAndNPLM3LOUkXqFOgtMWMYjd41AKwDcIvmDdst7eXsw3Cfv0Qgje91CmsRvuUPyh1mieIPlF562mcd1WcQR-UsNfFmER9DQwICE1tMDEEnACsLksMs394f71sqb4lrfDd09MBn5FQqv9zbIH1tGNri7qGqw99KGxydzaauE4Jh1tHanROFONL5N9LeL5cqvyM8q415bfCgV_OgdyWc6FMEQM_JxB7as66m5y3Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CZ6OTtQnQ3YKL_wJLEbV41wBH5sZsOfwmF0p3ewm6UXteCYpk5xSSW3v-SmwMGB-prpKfKdFYV0E0NrKwITIKFk-5n8LyIQZIY0sIjKsCAqyTJGW0Z8WHzfSoGqbvR6IZnj2_bLfbC3zERb7n9wN8V7c5kAnJXt4_3mPM4czCqePkOKsK5ddxjc-ZR42KIramjXpOxLkRABGrMzmwwHsnny3Ztye8wpl0XwMNIHXzw4dCPiwXGo-0T71PoSJ0HYQVDWYki7WOywbiY33HcQffuPYjkAk3gB9rQa0y-IKXgA6cOECoTFLGnrF_qVC36GGPx9-qhdLREV1_VRftSldng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LcS6OvfVKU5S_bFDzgqLTULaHRJ2QHJ78tKiGuTK3zr1BDym2fY-SZUfkrGE_eLIoML1mynH2s-KsZB6rUL_CDiJwCG3UyoSyY4xAIkMzBG9t0N5lDIpguK9svzIKyMSjwI39DJqGx92qwAP8vkZ5N6bU54GL4kRbusSO_QfMhLVPC2AxY2TBpaIR0rI7d-eT7EMAaGeSW4nn3FrK4ABSZkAYrVd5r7DF7wtCWIIBgxgSN_AJ5X9mjWXpoklXVK7-XdrkgX1V6-kApaRpbAnL2SpmRz_3gvaB3G4OTA0-gWQ0MHk0w-wriEEO5DmiQPP7KMX2cBXaPcVv_khuB2sLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JjPtgeWUBKjKmL9n86M76q_7AfSPLJS_n8oH3JQFr8FaiJN9l3NBsXBkwryyg5p9x6Z-4TNhJgJ8cB9GAnXKQzuMmAC0JQVPoT5UbqdMV88EMp98r6AwgV6BbifINXroDNpowSBaGDtdIQOqs3mmb_HaJO_zrYcXhPxBfj8TJacLrFE_BMxvMeXhl1YwtqXGJ9UdNoKL5AmQvFcQC2Oo9W7h7thpApJeg1UXYEwII74dVl87cn1zVof0E-AwE2pWXp268r32bIuV8nUHHeyZKY74ZBEOxClF9aLWLXjF991MAGCqId_krrR6iXemzGJ8FKZYJWwd01BccrkfGu_8CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oJPjzgVvgTFGwzRZQP0sIhxRsVriE85OXQDi7qDPPOcDFHQSix_81vdviVTMSvy2EJAOOdZGqsWbKHBtEwoDBZi_VXszdg8v_7jinEApT0zkP3lTi7BXWWd22pvq3QH5-CSuS86SrZybglFJKYBarQmtDuvZFSoIeit5B6Kaa3qL3zf2hTi6ECnPkf-oHA960RaTMTN6x6gnzA3xDDqm2ihQPKw64eXPB5JDPNRuYCxuoIbmept-2sxIyfkJIOqh7sBUU1L8of_D-h9itj_6vOMNtRdIeWmWodySfQbE5c5-I99qQhlSLBy3cedYvZWWZzcKF1vrpJYbbv9tQus7Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AZH3vJ_Frt65pqqcui0a3ZhXn3oYmnCZzkUUQI21iYwwqrIFHr6ErXV3xn_Q2_kMC3URanZ3gJKDvivtcNgf1qFSKwAynu7Q17_PbceVtdIM1uNs5oFa6j-4VPNhksHhyulM4hm_zaOXyQcc88JtC2PpeWnN0WC90qX0TEfYuvBAjuYPsU9-gAh4pPbI7x36WyX4-ICpR9_t-BIEuGhFMbKe7y-SCGRZdguCLRUUmFMN4nx8FtXpIqSUMCyA2tR3Be75o074TfhbYbmrKMx0ASAnGXmDoCuugrJIUru9Y_K1l0nh2_KoaA-O45Xm8iPVVIWEwR8STSr2B6l_asEDSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kfVLPy67MJ9TD4tx0G2SZpAdxaHODuy59TZv0xHKAa7QA-m5CeeobQ9EJ-K9fvuSDaP3DpLMW0-4Xso-SYDXjCZwXPTaTN4DPoZDatvvUMHh5V3fxV34qKjxrFZT5UIRvKfyxgwBAGQN7OVdPIvvG0XMqm2FikHVB7q27Sw7MItjZ1KrQcvqnpJsFRtRtTH07cu1IveZzv_wNkBibQ2CE0maUT2GyL_pJoienQ5Ro5uAXVA2vd2NK5ZnOudP-f0jWku8Zq2gICfWCqn7sdfip2-1HFY03ym25tUn-MILXEHsgYZLbY-sRXM8FPzUXVH5HzBo2wr14H-bRG0c-l2xUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KUhQeKa5dYivbeO7FQYoUoksFTDZt4xahrOiUCWruhk3aQzFJGLP4zWHtZ5GPw_A60ZeyQktxIOboNGHl5rBP8Kpw-FdjFC2fruvnsbTSNojl9MHVZQA6kSR4ZYfMTf-faHpuAh-LtiQYWsFvgHQaKDyV8NJ2PFMya18NcmHvVYyY1kNBiuxJzj0Ys_XqC4jpSITJWO4LCQpDBlDoD0q89pvjh_rgr10EmE9S3PqAV0EEE4tQr6o5Zxx04TQOOp9q2qufJ0HZo_iLjR1FYyIT44k9scdAmtccbrS6OJrrCysSHkyDl2tIUM4dLaxfOfu3JeGbDEgZ_rUgybK0fQxKQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💫
روایت برکتِ حضور
💫
✨
برکتِ هر نذر، به حضور دل‌هایی‌ست که بی‌منت کنار هم می‌ایستند.
🌱
#هیات_قرار
با همراهی شما مردم عزیز، هر روز با نذر و قربانی و توزیع گوشت قربانی، در مسیر حمایت از خانواده‌های کم برخوردار این همراهی را معنا می‌بخشد.
گزارش اقدامات هیئت قرار را در کانال زیر ببینید
👇🏻
@Heyate_gharar
شما نیز میتوانید در این کار خیر سهیم باشید
👇🏻
5029087002135690</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/698030" target="_blank">📅 13:55 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698029">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c327399872.mp4?token=a2UQml_GHLfay6zxeq5fMFfvTUYXTLOk1HcTwCTkwpInxtQBGBQ5j5Omdpl5pLJr0NBHGaQPMykXZ8Xe9rqQGPrh23KVtklZ2X1YvMN15tfcmZBaQla1OiibkUQmPOxxKSUeKCo9Jtx7bdbBk1UhURtaA9BI4qSGlHW1SHHiBeASsO2jWnhZPZcz-SjFnTY-KMomhkEzN-Ft6KZ7w5nBl1CV26QJwm3gK8EPDWHOmF3aH5E8MJp6biHQcK4ykMu7zwX7YfwkNwDFWHVpEaNnwG1adKEXUV7SRkhh7YpfR5y42ZbaAbem6X3GtUBIN2lvm0d_5nZeKcyWLL1WApVAbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c327399872.mp4?token=a2UQml_GHLfay6zxeq5fMFfvTUYXTLOk1HcTwCTkwpInxtQBGBQ5j5Omdpl5pLJr0NBHGaQPMykXZ8Xe9rqQGPrh23KVtklZ2X1YvMN15tfcmZBaQla1OiibkUQmPOxxKSUeKCo9Jtx7bdbBk1UhURtaA9BI4qSGlHW1SHHiBeASsO2jWnhZPZcz-SjFnTY-KMomhkEzN-Ft6KZ7w5nBl1CV26QJwm3gK8EPDWHOmF3aH5E8MJp6biHQcK4ykMu7zwX7YfwkNwDFWHVpEaNnwG1adKEXUV7SRkhh7YpfR5y42ZbaAbem6X3GtUBIN2lvm0d_5nZeKcyWLL1WApVAbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئو پربازدید از شعار علیه مسی در میدان انقلاب تهران: خوبه که فرد ذلیلی نباشیم مثل مسی اسرائیلی نباشیم
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/698029" target="_blank">📅 13:53 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698028">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
درگیری نیروهای امنیتی با تروریست‌های جیش‌الظلم ‌
🔹
یک خانه تیمی تروریستی در منطقه چاه احمد کورین زاهدان طی عملیاتی از سوی نیروهای امنیتی منهدم شد.  #اخبار_سیستان_و_بلوچستان در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/698028" target="_blank">📅 13:50 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698027">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromFAKOOR | فکور صنعت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/595bed7af2.mp4?token=XuEJ7sbC1_TTE2hWIUpa8A4YSTxIum3ETyACMA_a3DrQq2sfqAMwawCsHecTw0pdndsPy1vktWQVgNNL28Lg13FeS1dCNpFyY3-WjukBxNyjELubhSsJAQpND0dO75-TluR2pQd0wQB9jnqRFEcA8HJlWP56L5er23LlfHNjARTAv1Hd6oh347pD0J13XMCOrZKCVx9uY6CMh1Ysy17U3wvT2vkSVvyaxsjZ1t-sDcwWYmoEj4Y4-Z5JuXm4l-3xzf_CUUZSJ4PgoEBjwjkruV3z0vEqtP50T0Svl42vzR6EdhGFYfdmAC26DrwJUYkiveHYvM9GpyT67Qt6mt2feXD3WVrwqQFvVZkc62RxNYAyKnZ1Eyo-Pmcq9JJXh5CPIQ4Du43bPwtS4Kt3vN9I2JTlxSRhBxrLOA_EYp2W0SGv7hunY6akxEJcF004SZnCBym1QWqB3eqHY60YkA078wnx9vyII0VJrn3Bs5-8X0hde7vyeX5WLiI-3VOvj4AqTVnwzhyVHGI_7WsCDIZdh0EEZ1m8cGvikcthYywtP47HbtddVd9XKPWtt7NAXHa_JZ91G_gC5-b0-tEhduFtkWdKjAXl21iEonrJRXlIg0a7Z90-4JlNAAmatfKTypP3Pysk3WLep3F9fEaLKC_BPTuOmwPKZSD6XoDKgrv_Hog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/595bed7af2.mp4?token=XuEJ7sbC1_TTE2hWIUpa8A4YSTxIum3ETyACMA_a3DrQq2sfqAMwawCsHecTw0pdndsPy1vktWQVgNNL28Lg13FeS1dCNpFyY3-WjukBxNyjELubhSsJAQpND0dO75-TluR2pQd0wQB9jnqRFEcA8HJlWP56L5er23LlfHNjARTAv1Hd6oh347pD0J13XMCOrZKCVx9uY6CMh1Ysy17U3wvT2vkSVvyaxsjZ1t-sDcwWYmoEj4Y4-Z5JuXm4l-3xzf_CUUZSJ4PgoEBjwjkruV3z0vEqtP50T0Svl42vzR6EdhGFYfdmAC26DrwJUYkiveHYvM9GpyT67Qt6mt2feXD3WVrwqQFvVZkc62RxNYAyKnZ1Eyo-Pmcq9JJXh5CPIQ4Du43bPwtS4Kt3vN9I2JTlxSRhBxrLOA_EYp2W0SGv7hunY6akxEJcF004SZnCBym1QWqB3eqHY60YkA078wnx9vyII0VJrn3Bs5-8X0hde7vyeX5WLiI-3VOvj4AqTVnwzhyVHGI_7WsCDIZdh0EEZ1m8cGvikcthYywtP47HbtddVd9XKPWtt7NAXHa_JZ91G_gC5-b0-tEhduFtkWdKjAXl21iEonrJRXlIg0a7Z90-4JlNAAmatfKTypP3Pysk3WLep3F9fEaLKC_BPTuOmwPKZSD6XoDKgrv_Hog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت فعالان بازار سرمایه از عرضه فکور| میثم فدایی
میثم فدایی، مدیرعامل اسبق فرابورس ایران، پذیرش فکور صنعت در فرابورس را نشانه‌ای از تغییر رویکرد نسبت به شرکت‌های پیمانکاری دانست و گفت پذیرش این شرکت به‌ عنوان یکی از بزرگ‌ترین شرکت‌های پیمانکاری کشور، می‌تواند به تقویت بنیه مالی، توسعه فعالیت‌ها و ارتقای برندینگ شرکت‌های فعال در این حوزه کمک کند.
🌐
www.fstco.com
⚙️
@fakoorsanatgroup</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/698027" target="_blank">📅 13:48 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698026">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
بازداشت ۲ عضو تیم قاچاق سلاح در کرمانشاه
🔹
وزارت اطلاعات از بازداشت یک تبعه ایرانی و یک تبعه کشور همسایه هنگام ورود از اقلیم کردستان خبر داد؛ به گفته این وزارتخانه، ۱۰۹ قبضه سلاح، ۱۷۰۰ فشنگ و ۱۹۸ خشاب از این تیم کشف و ضبط شده است.
#اخبار_کرمانشاه
در فضای مجازی
👇
@akhbare_kermanshah</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/698026" target="_blank">📅 13:44 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698025">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NZkkzfPcfu-bvhUQBcaFS1Qi33Xl82a8-elDWilHB6o9idzNGv0frzmMDDmh0vEvEz_J89kAuFtHwTqocoBoHODwLrvXAciOdkUNSBf4p-yV-_IJxfTYmwAyUuMB0maEHCjln57EdUJjv8XLVnz99cColIrX4wCq6pIz53EKD0lr7-gHUWpWcxJOKqmBn_hkrfw-REkEGhWd7Hux6UrJW_dfO6-aarG8kFSQMq7W2oLz34nSnPJp9vF8ZshPXwVHIl5udme8fYpCIwhmRbS7mwaoQb-XZBdfMpouVhWwX4z6qusBqvBXYcxyjtU6AkvaG2IWGjf2lt-LUk8Ei5hyQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای
محمد میرباقری: امروز ۲۰ نفر از عوامل موساد که برای یه جنگ شهری آماده شده بودن، دستگیر شدن؛ که هدفشون ترور ۳۵ نفر از مقامات کشور بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/698025" target="_blank">📅 13:42 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698024">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d14088541.mp4?token=KEw0WsZ032n2-eZwuJsq3IQ48aUFBI_J1-41uX7QhRkR3kzL8dt6c-BGK9mCg5GIp9s6Ih5rkhbndoQdxGJ1lN4v7QphvUiOxRhjpcj1Vk9C0VNawbu2ljh_q8BLN-b0WmHdKuDXA8qCXB29tSRd0M3IgRJY1BLr_gcLYaIkJrkqc9xfUo1ul0HwvSqzc7xQLJQCbacJHPIjKtv31kGFeqU94n7Y4Sh8smrrp1SvYEAIdDMs_n2wR9vSZ0zhO9mc1R6_dscy-wrAMBjLioj5p5D9gX2Zown3WyxP088iIW1_QWh1KxRxcUbNnDpR-0UfBLHlKDPeYQ3pLYXyueAQlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d14088541.mp4?token=KEw0WsZ032n2-eZwuJsq3IQ48aUFBI_J1-41uX7QhRkR3kzL8dt6c-BGK9mCg5GIp9s6Ih5rkhbndoQdxGJ1lN4v7QphvUiOxRhjpcj1Vk9C0VNawbu2ljh_q8BLN-b0WmHdKuDXA8qCXB29tSRd0M3IgRJY1BLr_gcLYaIkJrkqc9xfUo1ul0HwvSqzc7xQLJQCbacJHPIjKtv31kGFeqU94n7Y4Sh8smrrp1SvYEAIdDMs_n2wR9vSZ0zhO9mc1R6_dscy-wrAMBjLioj5p5D9gX2Zown3WyxP088iIW1_QWh1KxRxcUbNnDpR-0UfBLHlKDPeYQ3pLYXyueAQlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در پی نشت گاز در ساختمان دانشکده علوم دانشگاه علوم و تحقیقات تهران، این ساختمان برای رعایت نکات ایمنی تخلیه شد!
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/698024" target="_blank">📅 13:38 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698018">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CP8iUxvBkb6jgGgp67VWIh7oTztvngfrPXq9g2ecTtfEx-i587y0Sn62p7Mf8rUNUeZDSxWAvqs8aOPbZFI39HNyVLCfCmF8-vlHqzbtofpuk7KhEKe_avNikrWlibt_92JcoTGM67TXKt8nsLvv866R-SxV1givaChDwUXF0MTHxTw9td28CaO5iD7QDD_VPGd-OSXIWCDezgYxCM7Mv5siSEzpbGCUrDhLnLkbfoy-5qJN6UsrDZm5tEgI_Ua0Bg6x9_d4gpEuAR2IlTRJA8gYQthQ2MEAVBPArNy40iRc_ChKDLFa-V8Yo2H6egrlKBrRq2k2IDK04MkPqWw0xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UAIncJd6loieatjlREff3QxOy0Yd55qC9GeV3XlnTiCynYsoTrC9a41zGD-pYP7y6UOeTas6sFei2sAtb5k5YxZyfavn1i8ZreB1gJ4R-OM9X8Gq9NtNLI2rxXoVnq5MLb_ZdQ2r1m_J8zanaVXC6J3OONX_urDhwyjY7nLCrlqFndEj8_MulaKCC1mLDNMtWHifrOlWlY3SEzjQ8Ha-Jd-qftv5xKQqRFWJOGvqw233fPnsuzaf6HJqTmK0TVeDyWYbOlWLL_pquiMPE_3oArmqPEclf_bWSnMhg7g-a9LqCaCgQKznIyFjOyr3uQyX-RFw_HBGalXhkI-yv0RSYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h-OChPhluXxnWhY_srtNdkn9CUdqZSdTlcPpzN3zCr1w7dpAoIi6RamkuF0qOzEzuYoT28F6JqqX4iP1Vgfmq0EVY8v-pDnFtCdtrvaJFKp3a7CAIP42372FGmEuD3ekcxfUlgfEzTxeFRjV2_hSGnb0YpIf0EDOtoywBu0CxVXA0M3ZsdlblMz9tklBojF9XQp2RQ8LOMIduFkc9x1Fb-X6Yoc_9n4QkMEY0QoUEx4ku7Hm1DcKV-uPM-5HfVOCYva6RKR8L-l3rQydcSlXXMamTilgQDEXIVrwPZIlrr4RU1dnn2pnnaBrOFdEfrWhWpIP6LRkdo9IfGvmRKXfiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e8PsSIWhMYD_uJXrYucku2sZ_eyOxiHZ9D7hgByTijAVk5sCoRLnsnlTpZIjb_5iL249UCQIbV5CnDzm-noOYDjOKS5A-5CTA3TeWHwfUnJPwLChNDzU4C5auUgx0KcUrxE2SI4lbK3tci3XIJkJdvH2vBDXfuZo0YOvBDsnAIX-cj2OAEptRtRJ-Ti2OM74Is0zFpsr57Bw-NbujtF9Qir3BWHNzN80HTTBt6uInN4jqjuA8xpbwxWi_UlbzsqmlqZprZDmPwg3XBLpD1naWWQmbld0ZBL44BkU0V8msGW9cjbYD1cH7VrOln6BN4to6bCgBAQMEUiarZUWxzGdBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v8ynj--Ixr7tXXOwNsngYP7rDJ0Ed4pz8vcoWDALenheL8cPZBYJ9mpT9_1k0iAjXFZ6mm2nfAkQ2gTxcA0NHg9UMvq5bfEBpvnxVXOjmUEU0yrDc7TvJ2CRjhIJXsQ2Kwbzko3QKxxciJxa5LA-tvFLjffxpxMWH14RLf4d2T8JEjthA_gJB5zZQWAnEWmdx8uS7e1hxaNgmbMFl1PImrJ50bPYID5LsLl_WQ-p2-DslekI_qq2mhrpkwYBaV3XPOTwTX_Dsrk_8iDa9XC5THpBdIUf3JP9FCD6fXjIjR8o8C2XFi-6J3gLJSzSKKz2CEYhpT1LUtNIC5RyHYOblw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZB7PWBS5xYsaOsHAnNifuNqCyK0iv9EeEiHSB-xUEqoAVoJclGRsaUvZhbgLP0-IQa6PsUYwwuyI5KVpWfoy0eHLdkK9-q-0fnpeWcidW8m24hmoKt3A0hIp6dL6d59VHRvDO0AEgQKt_tevopzaNVWDLWR_5wRnlUJhl0XQEyjgQvXSrnlNt0gEaRdxNInY35-VVlPwum5vrbIY0jPHbNJ2le25vRALaKJTv-YGCyBkZVg2yPsLB-KnK4WivDPgC7Sbz7u3gRc-7xmegvePV_E62QhVhP9DWFtav1VHvrxBpVjNozE_4vtBuRrxIxVJASx4koZRIfvtJBuF5FzU7A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
دنیا از نگاه حیوانات چه شکلی است؟
👀
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/698018" target="_blank">📅 13:37 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698017">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
ادعای وال‌استریت ژورنال: هشدار ایران به کشورهای منطقه درباره احتمال حمله زمینی در صورت حمله آمریکا
🔹
مقام‌های ایرانی همچنین هشدار داده‌اند در صورت ازسرگیری درگیری‌ها، ممکن است اهدافی در منطقه از جمله تأسیسات نفتی عربستان هدف قرار گیرند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/698017" target="_blank">📅 13:36 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698016">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
وزارت خارجه: ایران و عمان درباره تعیین مسیر موقت کشتیرانی به تفاهم رسیده‌اند و جزئیات اجرایی آن در دست پیگیری است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/698016" target="_blank">📅 13:34 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698015">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bda0e8e81b.mp4?token=h1nsz6_j19SIjlV-87Z17b7dJS0xWD_NnCgstJaIqRPhtfHaBZqMPJFxJnII43r3EqdjqObJU_IBb-urV2QKGy9oZ-tqPSSylzUrfoCVbBeTGRxCvvEtfFTfepO6-AOcZrbZLDHrflv85ZtpLp4Qgo4EHlzctRpCRehGpRyfR60KqQ5LFFc0VOHC5E0t69w88vYMfwWYNMYCnOuQgehjnfnzakYl26zxDS0gT3K54-wrkZ-oU67aRPxuq8C_AsAwPM2A5EE9sbpZIiwxFm__WzXYmLAhaZ6nQxwzM49S3O9Jr9gNFZO7f-B8vBX23qSy1jUhYpXfnqZHYnuEZ4XD_HJLnpfOij-J2HIxKQu_AJPs5Rq5YvYOltZrJ9QoCOF4HzYlTnZfUa0dpbyXY4vV0kcZjZ7Bac20TdyL485tv7BWLa-6n2yb-me3voxxT8IfqwJHgVviK2zw_0Ue5zRLWvgSSZX-Y5oxnRdxw5DqAYAbwFni-poRRIp3jlhIzaW90SEdST7ezJvZbj0Z-UVSqdhIKi7r_CRKq4Jxb25kBUh5kn8A3Hxr3R6VQUzLy4-jBrf5T0ustQaOyhZAH1BjK_UzXNkzW3gePa_0_xavGH-2DReCi826WCOGSl5xIvMUnq9Vv1pi1h6vYM0cLKCx69mDLF5EJvWJSzxGovFDdNk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bda0e8e81b.mp4?token=h1nsz6_j19SIjlV-87Z17b7dJS0xWD_NnCgstJaIqRPhtfHaBZqMPJFxJnII43r3EqdjqObJU_IBb-urV2QKGy9oZ-tqPSSylzUrfoCVbBeTGRxCvvEtfFTfepO6-AOcZrbZLDHrflv85ZtpLp4Qgo4EHlzctRpCRehGpRyfR60KqQ5LFFc0VOHC5E0t69w88vYMfwWYNMYCnOuQgehjnfnzakYl26zxDS0gT3K54-wrkZ-oU67aRPxuq8C_AsAwPM2A5EE9sbpZIiwxFm__WzXYmLAhaZ6nQxwzM49S3O9Jr9gNFZO7f-B8vBX23qSy1jUhYpXfnqZHYnuEZ4XD_HJLnpfOij-J2HIxKQu_AJPs5Rq5YvYOltZrJ9QoCOF4HzYlTnZfUa0dpbyXY4vV0kcZjZ7Bac20TdyL485tv7BWLa-6n2yb-me3voxxT8IfqwJHgVviK2zw_0Ue5zRLWvgSSZX-Y5oxnRdxw5DqAYAbwFni-poRRIp3jlhIzaW90SEdST7ezJvZbj0Z-UVSqdhIKi7r_CRKq4Jxb25kBUh5kn8A3Hxr3R6VQUzLy4-jBrf5T0ustQaOyhZAH1BjK_UzXNkzW3gePa_0_xavGH-2DReCi826WCOGSl5xIvMUnq9Vv1pi1h6vYM0cLKCx69mDLF5EJvWJSzxGovFDdNk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علیرضا مطلبی: گاهی چیزی که حال روحی‌مان را خراب کرده، نه یک اختلال روانی، بلکه فشار بی‌پولی و مشکلات اقتصادی است؛ گاهی برای بهتر شدن حالمان، باید اوضاع زندگی‌مان را بهتر کنیم
برای ثبت نام همایش بزرگ استاد مطلبی در مشهد از کد تخفیف BMT72 در لینک زیر استفاده کنید
👇
https://evand.com</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/698015" target="_blank">📅 13:33 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698014">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89438f3e4b.mp4?token=ut_ZmdQuEAUBkBuV5Ho1SpZmDvK3Ydu13BWsPZ5y3VqpSF3I6xPxWT-3EIg3VrniH9sCt2nURZNh49CimzWcErdG5ZGQVXJnWfvCnpZ13_DohPKsN7YfxrwdjgIlIwzaMKIyTMAqg_IrNW3KdMre6KhVSh6oN1KeMIGujvXcG6THy1La3kg-ikB0YP930cFtch4RLmGn7RxtHq6E0nNfHbzY7eNMSRigsEf4Mftcy2pAW2wgn9B6JoiGdda5s9OIWcRMAg5EdwsXFYRneCDyfrreob5o5cCkI85qvtaDHPhKhovd5BPtWa1vhexN_8Y0i1_TlYMqbCtOK4eSJPcyzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89438f3e4b.mp4?token=ut_ZmdQuEAUBkBuV5Ho1SpZmDvK3Ydu13BWsPZ5y3VqpSF3I6xPxWT-3EIg3VrniH9sCt2nURZNh49CimzWcErdG5ZGQVXJnWfvCnpZ13_DohPKsN7YfxrwdjgIlIwzaMKIyTMAqg_IrNW3KdMre6KhVSh6oN1KeMIGujvXcG6THy1La3kg-ikB0YP930cFtch4RLmGn7RxtHq6E0nNfHbzY7eNMSRigsEf4Mftcy2pAW2wgn9B6JoiGdda5s9OIWcRMAg5EdwsXFYRneCDyfrreob5o5cCkI85qvtaDHPhKhovd5BPtWa1vhexN_8Y0i1_TlYMqbCtOK4eSJPcyzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ما به سوی میدان جنگ پرواز می‌کنیم
🔹
رجزخوانی شجاعانه یک ایرانی مقیم آلمان درباره تفاوت پویش جانفدا و اعزام اجباری برای جنگ اوکراین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/698014" target="_blank">📅 13:32 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698013">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
جزئیاتی جدید از نحوه از کار انداختن اینترنت استارلینک در ایران از زبان رئیس مرکز ملی فضای مجازی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/akhbarefori/698013" target="_blank">📅 13:31 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698012">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
فوت کارگر ۲۲ ساله مشهدی در میکسر کارخانه سوسیس و کالباس
سخنگوی سازمان آتش‌نشانی مشهد:
🔹
یک کارگر جوان در مشهد در حال نظافت داخل دستگاه میکسر کارخانه سوسیس و کالباس بوده که دست وی در دستگاه گیر کرده و منجر به فوتش شده است.
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/698012" target="_blank">📅 13:30 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698011">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c1vVwGJwiQYx3XaGulkzXNd1G0cuY9gbT-rOwlT_uuSn8mFlzeSKMVtPhP6_PY3to1xSqNeg5SOc79-1uMPEbb89mWhXXvJC9GwVo40oJgbGd8deCuaXwGY2nuhJqTZrg2z08_DsnQeuTAJ_eEE7X0tSknDlyFTwSRgcxzvvn2ffWnyCOqv-zgjexp5kioX1IvN0AFNFHe8N_DwxO9TVo0JQtnYo0s8ZW5w6ilpRBeiMaQ-B_S0ZOuYDnp5zu6z6Q4lQT9hMJ4wgd9Ev3doWpUl2DlbjXIbL4HTDuDnzi5Fk89omfq5i5s53RauEKGHmfeesjHA7W7kcdGBZ6t3qcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
افشین معاون رئیس جمهور: صنایع خلاق باید مزیت فرهنگی ایران را به قدرت اقتصادی تبدیل کنند
🔹
معاون علمی، فناوری و اقتصاد دانش‌بنیان رئیس‌جمهور در افتتاحیه نمایشگاه صنایع خلاق مانوین در اصفهان، بر ظرفیت خلاقیت ایرانی برای نقش‌آفرینی در اقتصاد تأکید کرد.
🔹
ایران با برخورداری از پشتوانه فرهنگی، هنری و سرمایه انسانی توانمند، ظرفیت قابل‌توجهی برای توسعه صنایع خلاق دارد. بهره‌گیری از این مزیت‌ها زمانی به نتیجه اقتصادی مؤثر می‌رسد که محصولات حاصل از آن‌ها بتوانند در بازار رقابت کنند و ارزش اقتصادی بیشتری برای خالقان و کشور به همراه داشته باشند.
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/698011" target="_blank">📅 13:25 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698010">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73511ed3cf.mp4?token=gFYPQKuu_REPYzVtOnGUOy9Lg4gosiuZ7uKncizx1NnzApN2ky_ekypDvjwuTT95KI3ywMEen27-pl0y9QINhbdJkboc-OJH1N2RDWh8SxI1k0eyiGw5zSShAKx1pOxIIqQCop0E_05ipiEOUQHRxptnS5hnoLmZcIrnMw1OHjSTavoLO9PmtCYAUMJhTZGRhf1GDDlMJ_TMZPqnOivUUp7Ej4EJ1-xYyC2ceNa3hUebznXlh9eBQc0uBvNS86A5-jpiH6DGQ8CxFYtGvE5AVBMRid0yCz0wnhVV3LbfcfH6ybzbxNZHsKuXiiHB-e1SMsdD36lNs2PLACp2jlaE5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73511ed3cf.mp4?token=gFYPQKuu_REPYzVtOnGUOy9Lg4gosiuZ7uKncizx1NnzApN2ky_ekypDvjwuTT95KI3ywMEen27-pl0y9QINhbdJkboc-OJH1N2RDWh8SxI1k0eyiGw5zSShAKx1pOxIIqQCop0E_05ipiEOUQHRxptnS5hnoLmZcIrnMw1OHjSTavoLO9PmtCYAUMJhTZGRhf1GDDlMJ_TMZPqnOivUUp7Ej4EJ1-xYyC2ceNa3hUebznXlh9eBQc0uBvNS86A5-jpiH6DGQ8CxFYtGvE5AVBMRid0yCz0wnhVV3LbfcfH6ybzbxNZHsKuXiiHB-e1SMsdD36lNs2PLACp2jlaE5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۳ قابلیت کاربردی و کمترشناخته‌شده گوگل پلی‌استور که احتمالاً از آن‌ها خبر نداری!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/698010" target="_blank">📅 13:24 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698009">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UMUvDZHmiLEEb0ncS4plIsVEYlEIaWZZW-POR86rGIhqMN8qcPvOEiBdpVad2hB4-tcreiw8io8e5iwpJbnVB-GPlc899eKagDpILCxdE2u8_3Fx4eEDPVQ7ksriOQ-4NwCsrAI1ImJbqObvF-8h5cuAbme1emuKZZV7xNNenPVuZ-eIWrwR477EgMdhuolG4o7qGXJE4834a_j6KhrJNRhz-mlC9OSeEve3hgRnKwk3yDXNzd2JGiPHQ0z7t9OFZGOEM5NETcEdpVb1if358hA5ZP4xBst8GfbvRL7XnBk4WSNl4UR0c0GQWWvl9Y_9uYzSH1yGp5bbBHsWCpGOWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تنگه هرمز؛ گلوگاه حساس اینترنت جهان
🔹
طبق نقشه گاردین، دست‌کم ۷ کابل مهم زیردریایی داده و اینترنت از تنگه هرمز عبور می‌کنند؛ از جمله کابل ۲۵ هزار کیلومتری AAE-1 که جنوب‌شرق آسیا را از مسیر خاورمیانه و آفریقا به اروپا متصل می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/698009" target="_blank">📅 13:24 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698008">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efb0f8667c.mp4?token=ortYfs-5dlBL_T-thxmr35W7XkXob9i6OQav1RGbAcn_E_Yc1M47eLRaDH_Ve9WfnmF79yfi92eqyOzv-39ZPwzm_C1x2ErUiFQsU6m4l60H3c0evgdZhDw4Y2ngpnxv3vuvKbvGD38SLddaE4o7AcBsWlLgXPJpGEeu8vAhz9D9gqx-CLO1kDKH8TSnhcEGSUaS7sEeoZJdy9Zx7P7-9cHKVaBnUaH5Zjkl34B_2IgO7714VBzO5APAB5dGpSxD5YSWjf0YpoCYpzlWkPY8OZn4cUvRawknjoZZ4n9kVmllQrD5zVJc_nNb137lRKP0EuzDWxselIRIdNFHxvSU_XUEg0c0CF4ATWD4-XT9RUWIUaIyp6tiKjYqAyNyTcigwd-YXc8l5AsayiXrJExAq_TfauURsZcUhH1150fIeE4zUFTbAqb7tMKpWE0Ow_IKBbyS1a6MwXuJYsLGGimyq6CKyUkxPi2WJoiOZWJbJxQAF_neizfs3HkHhqICidTJS-eRuPZ0FA8uzwJoqchQW3eq8apb2NRCp97R-M-YVGlhQhCWavn1aAJE3J-JyjoiU0EAPnc0bKtT-BNx6DWqe5C0OlG4VTutbKpizVtlWAs3qTmq_5_O4Eg5CL2cXEGvjzX1Tjl40qtS_ErvB_ne1Ao56O82ym2Cm7sTvuWLToY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efb0f8667c.mp4?token=ortYfs-5dlBL_T-thxmr35W7XkXob9i6OQav1RGbAcn_E_Yc1M47eLRaDH_Ve9WfnmF79yfi92eqyOzv-39ZPwzm_C1x2ErUiFQsU6m4l60H3c0evgdZhDw4Y2ngpnxv3vuvKbvGD38SLddaE4o7AcBsWlLgXPJpGEeu8vAhz9D9gqx-CLO1kDKH8TSnhcEGSUaS7sEeoZJdy9Zx7P7-9cHKVaBnUaH5Zjkl34B_2IgO7714VBzO5APAB5dGpSxD5YSWjf0YpoCYpzlWkPY8OZn4cUvRawknjoZZ4n9kVmllQrD5zVJc_nNb137lRKP0EuzDWxselIRIdNFHxvSU_XUEg0c0CF4ATWD4-XT9RUWIUaIyp6tiKjYqAyNyTcigwd-YXc8l5AsayiXrJExAq_TfauURsZcUhH1150fIeE4zUFTbAqb7tMKpWE0Ow_IKBbyS1a6MwXuJYsLGGimyq6CKyUkxPi2WJoiOZWJbJxQAF_neizfs3HkHhqICidTJS-eRuPZ0FA8uzwJoqchQW3eq8apb2NRCp97R-M-YVGlhQhCWavn1aAJE3J-JyjoiU0EAPnc0bKtT-BNx6DWqe5C0OlG4VTutbKpizVtlWAs3qTmq_5_O4Eg5CL2cXEGvjzX1Tjl40qtS_ErvB_ne1Ao56O82ym2Cm7sTvuWLToY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بلعیده شدن کامل یک بز توسط اژدهای کومودو؛ تصاویری که در فضای مجازی پربازدید شد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/698008" target="_blank">📅 13:12 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698007">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
هشدار نماینده مجلس به فروشندگان کارت سوخت: متخلفان با جریمه‌های سنگین تعزیرات حکومتی مواجه خواهند شد
منصور شکرالهی، عضو کمیسیون انرژی در
#گفتگو
با خبرفوری:
🔹
طرح استفاده از کارت ملی به‌جای کارت سوخت هنوز اجرایی نشده و در شرایط فعلی، صادرات سوخت نیز انجام نمی‌شود.
🔹
فروش کارت سوخت تخلف محسوب می‌شود و در صورت احراز تخلف، متخلفان با جریمه‌های سنگین از سوی تعزیرات حکومتی مواجه خواهند شد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/698007" target="_blank">📅 13:07 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698006">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
گرانی بد، ارزانی هم بد؛ یک بام و دو هوای حجت شفائی
🔹
اظهارات اخیر حجت شفائی، رئیس اتحادیه تولیدکنندگان و صادرکنندگان طلا، درباره قیمت‌گذاری پلتفرم‌های آنلاین با پرسش‌هایی همراه شده است؛ او هم افزایش قیمت در برخی پلتفرم‌ها را نقد کرده و هم پایین‌تر بودن قیمت در این بازار را محل ایراد دانسته است.
🔹
منتقدان می‌پرسند اگر قرار است از «قیمت‌سازی» سخن گفته شود، مرجع قیمت، دامنه مجاز اختلاف و معیار تشخیص تخلف دقیقاً چیست؟ بدون چنین شاخصی، هر تفاوت قیمت با بازار سنتی می‌تواند محل مناقشه قرار گیرد.
🔹
این اختلاف حالا یک سؤال بزرگ‌تر را مطرح کرده است: مسئله اصلی نظارت بر قیمت‌هاست یا رقابت میان بازار سنتی طلا و پلتفرم‌های آنلاین؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/698006" target="_blank">📅 13:05 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698005">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
مهلت ثبت نام و انتخاب رشته پذیرش دانشجو براساس سوابق تحصیلی تا یکشنبه ۲۶ مهر تمدید شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/698005" target="_blank">📅 13:01 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698004">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
ایلان ماسک: شکنجه هوش مصنوعی شاید به انتقام‌جویی آن منجر شود!
🔹
ماسک با ممنوعیت آزار بی‌دلیل مدل‌های هوش مصنوعی موافقت کرده و هشدار داده است که فشار شدید در آموزش این مدل‌ها ممکن است پیامدهای پیش‌بینی‌نشده‌ای داشته باشد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/698004" target="_blank">📅 12:56 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698003">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
قطر و امارات پروازهای خود به عربستان را لغو کردند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/698003" target="_blank">📅 12:52 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698002">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q1cdpVEomvVSbyALYCXFcMyf_HIt2lRQNclyCatkPSxHwN-Vzfy-g3runsjhFNe8T_j_XAcdhlkPvnaRYebTycxN8OiktpSuITatS2tIcpREQLC4H-Vm6vrYQMkqWbKNIf_1Qyyg0EeXCiAUCnnvBRFZZfO9a4NHaNg4MrTEwv4jKeXl2CwLTSK_Yr-Zk1VEv4aZTzppXVFP8sCwiAFKU27hl4aTFJ9VYcHrBxWKDzOE7TR-GF6Ywi_splSfkaGCl4LzMnHYYD3f4SlDYfUc-txDb6JanVnRBBVUTbXdxJI_-YZWYZ5G6TpaD11LLI4a5MefmxL1NDjvo_bCWd8d3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پاییز تماشایی روستای پلنگ‌دره در گیلان
🍁
#اخبار_گیلان
در فضای مجازی
👇
@akhbaregilan</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/698002" target="_blank">📅 12:47 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698001">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04c3acce82.mp4?token=YevNEc6aC2W5TOoBYT7x3jkXmkChfk663j6wGFKH-M3HfYpbdYk0ObJAyAlxm5EJH_CUXwL0icBAhVImwIWUdCS9xbYKP7iNFTROYK8eLF9nbqfiY-JDwfAwyWi1oFPl8b9Gem6ATBFrMJlhr0o0eoIvVGjSND8wowriWI6VWO9u75czmWifuOcHz2uHjfOMhI5JrHy7jGwXeKH6ehuKrmH0Du_dK5UeDTueM9CBRL9qC3SuNBmKh2j76OT7pn-ED7np9M0dfmXEEM2dukO1qAMJ4poS8qWm9wz2jYABuiGg2N5c1mb9MlqinGf8FXq6PJguj1ckDz2GIXTXXD4D2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04c3acce82.mp4?token=YevNEc6aC2W5TOoBYT7x3jkXmkChfk663j6wGFKH-M3HfYpbdYk0ObJAyAlxm5EJH_CUXwL0icBAhVImwIWUdCS9xbYKP7iNFTROYK8eLF9nbqfiY-JDwfAwyWi1oFPl8b9Gem6ATBFrMJlhr0o0eoIvVGjSND8wowriWI6VWO9u75czmWifuOcHz2uHjfOMhI5JrHy7jGwXeKH6ehuKrmH0Du_dK5UeDTueM9CBRL9qC3SuNBmKh2j76OT7pn-ED7np9M0dfmXEEM2dukO1qAMJ4poS8qWm9wz2jYABuiGg2N5c1mb9MlqinGf8FXq6PJguj1ckDz2GIXTXXD4D2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌐
📢
طرح «فرازش» بانک رفاه کارگران آغاز شد؛ پاداش نقدی برای مشتریان سامانه "فرارفاه"
🔹️
بانک رفاه کارگران در راستای توسعه بانکداری دیجیتال و ارتقای تجربه مشتریان، طرح امتیازدهی «فرازش» را با هدف تخصیص امتیاز به فعالیت‌های مشتریان در سامانه "فرارفاه" این بانک و بهره‌مندی آنان از پاداش نقدی راه‌اندازی کرد.
🔹
مشتریان در سامانه مذکور (دارای حساب/افتتاح حساب) می‌توانند بر اساس حجم و نوع خدمات دریافتی خود، امتیاز کسب کرده و متناسب با امتیاز از پاداش نقدی بهره‌مند شوند.
🔹️
در این طرح، مشتری بابت هر امتیاز پاداش نقدی دریافت می‌کند. این پاداش در صورت درخواست مشتری به‌صورت سیستمی محاسبه و به‌صورت آنی به حساب وی واریز می‌شود.
#خواهیم_ساخت
#بانک_رفاه_کارگران
@refahkhabar
|
بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/698001" target="_blank">📅 12:45 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698000">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
جریمه تا ۷۰۰ هزار تومانی تخلفات پلاک موتورسیکلت
پلیس راهور:
🔹
نصب پلاک متفرقه ۳۵۰ هزار تومان، نداشتن یا ناخوانا بودن پلاک ۴۰۰ هزار تومان و پوشاندن یا مخدوش کردن آن ۷۰۰ هزار تومان جریمه دارد.
🔹
دستکاری ارقام پلاک نیز جرم است و ۶ ماه تا یک سال حبس دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/698000" target="_blank">📅 12:43 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697999">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
ترامپ قمارباز: دوست دارم برای سومین دوره رئیس‌جمهور آمریکا شوم
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/697999" target="_blank">📅 12:37 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697997">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WjS726-QAf6CI17kxFM1Uow7XXPDZkGvbkmQfmLy6e3m31mP6Z49kDTyLSIXv7cDs_-XtAXlt_e3UQqlTcVn1gSt2fiDs2iCEV1ydUqz_aq8EJrR1Y7KEMwoXOb36z0MfUm2K9N0OUShMqlWKIsShMTfbVrkKdqZAneEljppjOBvFgtIgxSLInHNgBuXBxZOcBQbz6CjzhS9NcTqSFhvw7iF9tFowo1_lyUyV8SA6caBC1dBpJacCnd4bw3baelNFxqeKWKaX3V6Ckvwjmgsrgy3NQV3aZ4Wb0q3JcGseNIh3yBM-CfJMNQT41jaV23W4lu7HUTziWNE8xa6r4eI_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شرکت تسلا خانه‌های کوچک ۳۰ متر مربعی تا ۱۰۰ مترمربعی ساخته که با انرژی خورشیدی تامین می‌شوند و ساخت آنها تنها ۳ ساعت زمان می‌برد و تعدادی از اینها به کالیفرنیا فرستاده‌ شده!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/697997" target="_blank">📅 12:26 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697995">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddedbe3fb5.mp4?token=hN0uRDinKtiO01We3NqtPL6jDnz1C-67uUvR62CAB9JQtEbk0I8l_9EUACky14OWH14oco57hNwfSUfPr818SXXfs1rDDS3QjGEzFTMgfDAMEnn102YBNCqXoDbYnjNtpht0a6jPnZTFEa0w5TGc4gZrXQryIq51QY7Rl7XnuUyInNEyQPMcfpi5kYUHwMOO0If4Y_Z2SxaGO8w0nsoWh9xWgTJQ2CBdGINyrWZ0fLuAjZByJBQDluAWyu14iKMCu4CAFjBFXp8UIVFJfqElgaQdtJ2e_y27KNRUe8l8nbi8OtT7IN1jXpM9KekxnIjftiCEjW53ThFTpTmVv0y1Jb6Vgr47ESu3X0E7xstjdZA5ZmgaFc37ORsUktAX9VknQjJ62X707QX6fyCgPiqrCvn_WZBgXA-vXb6oWu6jmCJs5FKi54qUi_ohoKk5UMJXgO663FvfWrtUYRoxziwtP_KsBKSOwPAG2_EtCQcot8vewz1G52YpAIyfFBXZi0AsWxPLBMjJyNOvecC2eeeJJ8EtQNbw_aHWNAF_495eARTMnelk68568SnPu0e5QC_NnPCwprIYzwZicqleBrXi54VIx8f8zJ4CmpryzBiOT1lQUC0ps6N-JFZg1DYvMDSdwpt7gofImo9RRZ3hXpAT_sqVdiqyFBV6LZIOp-Yq-j8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddedbe3fb5.mp4?token=hN0uRDinKtiO01We3NqtPL6jDnz1C-67uUvR62CAB9JQtEbk0I8l_9EUACky14OWH14oco57hNwfSUfPr818SXXfs1rDDS3QjGEzFTMgfDAMEnn102YBNCqXoDbYnjNtpht0a6jPnZTFEa0w5TGc4gZrXQryIq51QY7Rl7XnuUyInNEyQPMcfpi5kYUHwMOO0If4Y_Z2SxaGO8w0nsoWh9xWgTJQ2CBdGINyrWZ0fLuAjZByJBQDluAWyu14iKMCu4CAFjBFXp8UIVFJfqElgaQdtJ2e_y27KNRUe8l8nbi8OtT7IN1jXpM9KekxnIjftiCEjW53ThFTpTmVv0y1Jb6Vgr47ESu3X0E7xstjdZA5ZmgaFc37ORsUktAX9VknQjJ62X707QX6fyCgPiqrCvn_WZBgXA-vXb6oWu6jmCJs5FKi54qUi_ohoKk5UMJXgO663FvfWrtUYRoxziwtP_KsBKSOwPAG2_EtCQcot8vewz1G52YpAIyfFBXZi0AsWxPLBMjJyNOvecC2eeeJJ8EtQNbw_aHWNAF_495eARTMnelk68568SnPu0e5QC_NnPCwprIYzwZicqleBrXi54VIx8f8zJ4CmpryzBiOT1lQUC0ps6N-JFZg1DYvMDSdwpt7gofImo9RRZ3hXpAT_sqVdiqyFBV6LZIOp-Yq-j8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رییس مرکز ملی فضای مجازی درباره نحوه قطع اینترنت استارلینک در ایران: حاضریم این تکنولوژی را در اختیار کشورهای هم‌پیمان قرار دهیم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/697995" target="_blank">📅 12:22 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697994">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LpqyGlyqpA3HQkvN-y3ShaNP6pnzTa5dKqWw3VhVSJpqtsyd9XIfvyz3CBVnIt-ZAwfeqTQCKqIo3_ZBbWvbJP54f7IMQK9I-gwOIVT_otX27HyDLIOaOX6kSfwRceMvjvg4f8utSLsRVNys0foSzN-vL7on6Qh7HcfBWZgBrSAbzRTvSaigwPjS7FhSyBJVeA4C7IgJAlfOgEISlO80f9saXqYP7KTyEZ_X4eRy3OYZK-7ieS-Zkarz2PJO7G1KrSuZMU76HldgvQnGbLcyfsywVnWiY_MxJjaun17HsoC6pvpPzT2QqQpEmNRs51O-FAJzqNSz1_IM58SroQKOIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عکس وایرال شده دو مارمولک خندون و باحال که حسابی با لبخندشون معروف شدن
🦎
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/697994" target="_blank">📅 12:18 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697993">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
وال‌استریت‌ژورنال به نقل از منابعی مطلع: مقام‌های حکومت ایران به برخی کشورهای منطقه هشدار داده‌اند که در صورت حملهٔ آمریکا، نیروهای نظامی ایران ممکن است دست به تهاجم زمینی به کشورهای همسایه بزنند
🔹
تهران به‌طور جداگانه به مقامات عرب هشدار داده است که در صورت ازسرگیری درگیری‌ها، می‌تواند اهدافی در منطقه، از جمله تأسیسات نفتی عربستان سعودی را هدف قرار دهد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/697993" target="_blank">📅 12:17 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697992">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
اصلاح سهمیه‌های کنکور با ملاحظه شهرهای درگیر جنگ، تا پیش از اعلام نتایج کنکور اعلام شود
رمضان رحیمی، دبیر کمیسیون آموزش مجلس در
#گفتگو
با خبرفوری:
🔹
در جلسه کمیسیون آموزش با حضور دبیر شورای عالی انقلاب فرهنگی، موضوع اصلاح سهمیه‌های کنکور و در نظر گرفتن ملاحظاتی برای شهرهای درگیر جنگ مطرح شده است.
🔹
قرار است این موضوعات بررسی و جمع‌بندی نهایی پیش از اعلام نتایج کنکور اعلام شود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/697992" target="_blank">📅 12:13 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697991">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb6a667967.mp4?token=CWkMQWbjrLWnpdmx96G-vjewef69ipw_8rg13FI7lWeS18q2ZPo8ijkmCAFypbpxyYqj4s6Ibb-FVfZbnPwNLeTEw6rk7bl6PMngc-rutLwF5EPHrvG7V3dOUqUdIfC9q7FrmWr1bTA4g81uvl-2i1GmVBbcVvp7ZzG1Pruv24YFemnurARa9L8ZRUx3i-vaGvRJrWsftJ-1fULAI0oywvb7Wrahd3zVfNIR6h43Uv3XOIXZCC74z9RkPkXWhK7dgqQrhbIjhJ5LY-tyEyHuZT6AQR9QdeBlSZygqOUN9oNjSSMJ25vQeL1SEtoTCaET7cRhjH1iJhWhfJVHVKgPmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb6a667967.mp4?token=CWkMQWbjrLWnpdmx96G-vjewef69ipw_8rg13FI7lWeS18q2ZPo8ijkmCAFypbpxyYqj4s6Ibb-FVfZbnPwNLeTEw6rk7bl6PMngc-rutLwF5EPHrvG7V3dOUqUdIfC9q7FrmWr1bTA4g81uvl-2i1GmVBbcVvp7ZzG1Pruv24YFemnurARa9L8ZRUx3i-vaGvRJrWsftJ-1fULAI0oywvb7Wrahd3zVfNIR6h43Uv3XOIXZCC74z9RkPkXWhK7dgqQrhbIjhJ5LY-tyEyHuZT6AQR9QdeBlSZygqOUN9oNjSSMJ25vQeL1SEtoTCaET7cRhjH1iJhWhfJVHVKgPmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اظهارات جنجالی حامد کاشانی دربارهٔ ثابتی و رسایی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/697991" target="_blank">📅 12:08 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697990">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ad1d75fb0.mp4?token=rRlcZ6Yp_jV8aZuysM_FduCZPyrybSDnjwMJzcwAjvhSP94NgIxyiGo6CAjakOrMCRnVGSZTQK-KRQy8YpQ5jKlF2VdQAEQ2UXtO7DHq2I6RP0-3aau21R_Cdrae_wXFsf5xKoAmFgCQAUo4iA3CoSWuTTeFqGCvAWe9jwl3d6fH4cbpw63zkoBvxmb-hcn4EKFKr4dosB-VyWNBK0xMDwj9txjzo4ZiieRPkWVrknKddd3-DTLvrGn9rQ_mxaas7VKkiZ5hq3SvpzgMLrxh-yG0J3TZcb2rNBjxGGp6_oZZVkpOgusFIMN2nTz8cusXFFrXM0cKAcoRED-a1Rrgeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ad1d75fb0.mp4?token=rRlcZ6Yp_jV8aZuysM_FduCZPyrybSDnjwMJzcwAjvhSP94NgIxyiGo6CAjakOrMCRnVGSZTQK-KRQy8YpQ5jKlF2VdQAEQ2UXtO7DHq2I6RP0-3aau21R_Cdrae_wXFsf5xKoAmFgCQAUo4iA3CoSWuTTeFqGCvAWe9jwl3d6fH4cbpw63zkoBvxmb-hcn4EKFKr4dosB-VyWNBK0xMDwj9txjzo4ZiieRPkWVrknKddd3-DTLvrGn9rQ_mxaas7VKkiZ5hq3SvpzgMLrxh-yG0J3TZcb2rNBjxGGp6_oZZVkpOgusFIMN2nTz8cusXFFrXM0cKAcoRED-a1Rrgeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صدای اسپیکر گوشیت ضعیف شده؟ این ترفند ساده رو امتحان کن
📱
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/697990" target="_blank">📅 12:05 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697989">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSpadcharter.ir | اسپادچارتر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jnV7kbOFIq4uxOf62C8HufV1CObUTWsGiN-CMcUHwuq-HpAQJyUSdjkulFLp0YSnwJJ--JmZqFRYTtdQFOX9aLXEECitoBuxtXMJKMcw-bOknwrQ6qot_yVU4ddlkZJWt1JwjbnF35H1lnunuJczwOdneVFKSnNreMVjjWfSPsPVej3NCqFYXQPOgYFZaE8f8Qz7GVc0x3Cy89QFqCBs4pfbI3UwmI6VKnP7hAGIg2KJ_BnjsesfMuuIeXL2bKQI3HA0XCRTlz8GZNXK1sll4IM8OlDSKb_u1kZIJtt6azVu0xb-9FVJxQI6eTrE0fMXw6tUiyJIOPLtP7cTq5B9Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
خرید بلیط هواپیما ، اتوبوس و قطار از اسپادچارتر
💢
همین حالا نسخه جدید  را  نصب کنید و از قابلیت‌های تازه اسپادچارتر لذت ببرید.
✈️
◀️
لینک مستقیم دانلود از مایکت
⚠
https://myket.ir/app/com.spadcharter.app
◀️
لینک مستقیم دانلود از کافه بازار
⚠
http://cafebazaar.ir/app/?id=com.spadcharter.app&ref=share
◀️
لینک مستقیم دانلود از سیبچه
⚠
https://sibche.com/applications/aspadchartr-blyt-hoapyma-htlktar</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/697989" target="_blank">📅 12:00 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697983">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gkX8sb1To-eXFP_f3gK0Ax75Z8rQoKsXWSDGTqT81uBnLnN2R5eVuWef7EdDZgBtaMhUxCZmV4ay0z3t7sY05FD-XMdjfTd0uaLEoYb5cIAL8k_SjbUFUzU9nO3ytp-MVq0y0zMVZcLxSUj1LqD89jP7-HKUHBhJdMtHA-Z9ON8M3CTyduR27wSGdlByNz0LbEUrV2RnzSIHOhHrRM_HQN6wKpGFxS8-pkq4btm1f20-htAUQ8cs1skb9G047pwkt5tSRw8X8mJR5hZKxszWbvLHk1V_rIZx6DzaqVrIY5xKRANZ1e4Lldo03hB8e4DzZDBOb7l_SzNgxwy9wjZIlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TacixEVMbgGIKxAj83G7D8uDXl-rCnyDRm5IH_6RzBDPL3gi8bA8rtbn-55_fIyjfK2amn647Nqsjue0sbvz-SJDg4DMeBIVGNFVnpaFu0Qd1hKccNBKbZEKK1fHX8zVQuttsAEeZXTrej3i1VW5npbuPq6vM2rft8idOfWE3SbYQ2qmQlecgQuPscY9XeUJBNyQPEmKBaDdJ8S4WytZ-qO22Bd1QudnBr5qDa7twVrsDeK7ev1VoT1nryS_ag-M6bxt_R4MR8INmgGHQf3XCEzh4OG4N_xVrsJazsfPHDPL2-JeJzTfIWHy3tPwf9eQK4FmzHhdk_x_t6xcwUW7nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gure6GQJS73_YBs7ZqKXG9K0x5_I4KXonB8xQQ5cCvgSzxG7eFAv1boCWmyGZIyplBP-fmDw2dGqf4QByIVn9g_aF3iUyIW5gLn_qvU8mMrmxB_b9DfhAx-pZ9oyuvL9LTuHfPGTN9uU_i6HbdFU6XE_f5BrYts_e1mjrAz4r4kUOE9sjxec5AMnQU1iHwIa3vVGDu00QMuGM3L-ZrpH907ZQPbQjCOcuzyj8mEMhFWiXulLHfY-QNy2y1eDjBFpA9fvrgFOCZcCNdkxItfln8PbO7Sbt8gUzFElf0v2xJbFA3fLcye7LQQQ2K5LPhUFPccMFRgwqIXTuk5iJz5v5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FUoGfdaBwG4G9ZhOp-0extQTA_hEiU6fY2XEq98egvPV0psv2s8wSsZJSNtrltPcUWRestsooB-PZg_i2sOpsK0ARQsENiXUyjBS8mvCBDGW-KW7VKmQwPsy6G16ApbLVW9M1IdpP2yGWwEv1u0OOyKb0ZSHqf3TPgTXfcCKCATYz2ByfLDJqYNcwW5GlzPucjJ1sBwUcfoGlxCF7kNJ-f1V4K82thpNUmxFVBCnOlv9VkQYKQ14EeaJZiGA9q-REMfHWhSc1FKuJDnoN9NVNb8DDjekvLpsdXlEF6o0KBkA7yt3osixjKXJR5s0v8ek_bvK-kCXRBOa1kk8ng1NCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WRjR506dJJTD4SYcgTchMajuR_K8VRAgxEIrxGUbl_MEeYqBEOSbiZZn6JXV928fa-Mj9UalNb5ygynlu-QbTq1E1X_SNqtmhCH4fT-iyIb4WlZY69KBzifeNTYzTCsCD8ZkvFRo18Pf05sGKrNddMnJeDqCgJWOPzUxJK2v2t3RiDDlxVWnwGeOnIOm9g1ikQzC-lPlg06Y8wp3hdiHptpVx-LDce92UoPQPy-nd8oOwCjZKCicoKSj92jDABgzdD0woLSQY4lGyTGU2kLOA-Pr2XenoxZJGt5fXUxMWpfcLFBvKbDuETpwMxJoTb4DL0ys4kp9BE6uCqF5xrAGJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QYDUfzQ5-EJtRV-D1XucJBhCl46BxCKrmbee7o6vi466T4BJGuzvDvBLJwhXEVSCA0uSM6yKJce_2uPU3UKiUeTg1BtE6KdY--g4PiA_Lid0TKnlgSG-J3kwvBd8KNb9bHnO8z6d_Q85wxSzav_wVPpZeTQ_uIlTdgrKq_wuf8QRKu05YOFV_FvvfaIXDvxfuURidbpT3oYpqpGQNjFLjfFIy97D9Z1l7dgoeGAgSNDO-ezEhGxyMKSAbHYR0O_hJeKQuqoIBCDsWalvPZqmcTpR8Pn4qfUh1RFmgX-A6TRWGqChmdOacIUK4MFSEJANnGZxZxMzDLn40elZcgffxA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
افراد مبتلا به مشکلات مختلف بینایی، دنیا را چگونه میبینند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/697983" target="_blank">📅 11:43 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697982">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
آقامیری رئیس مرکز ملی فضای مجازی: استارلینک علاوه بر ارتباط‌رسانی، در جنگ‌ها برای فرماندهی و کنترل، هدایت پهپادها، جاسوسی و انتقال اطلاعات به کار می‌رود
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/697982" target="_blank">📅 11:41 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697981">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
شایعه درگذشت میرحسین موسوی بار دیگر تکذیب شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/697981" target="_blank">📅 11:39 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697976">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ou6qG8UST5BSS0893sjMw3XHb3VR2mJVnzWIpxOfD5EBuQX53hpEV4ALURfDLz-T-HkgtEO1b51TDWvxgs4P5ZP-Doeys7EWtteHZvPcWCdDHsYsaMQxbQpb_iDBUPlgvhRbSQPIQdIgAakx-5XWODsNGbOFVHPO8A3I0gXElXulWu5uyUdGfX_61xj_LWcfSGW8Q4ox9r2n9CmjpB7-sgyJrteH-j-TU8Jf3LFDBZ6WwiIZZOf6leLKGFM5x1NTwFT7Hd542QIE8nxT8zdGlEm0D2gvuI7ioe3tvwTnQBWPfJZ_DASDmAyiIyVVHbPjx2v8T63k7kIWA3MZgtyU9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kb7aNg5Tlh1TA9E8LRfjyA0Lq1WI1yBPSGB0w_vpdr90pKYGLKD6tSCL91EoHzbHXFJrY057SErIQ3Y2on_BwyJrxeMAY4qzct8D5TS1PJM2ZKlRi_0ZpgWtYXUj5aj6stGzkjOS5vndxnFntG_US-Lka0ZkhmpC-nxpqUlXx8aft9VdIKrypdioZLoZ8k7Mwh97UafHLTXdmcR_X2W1BLTCevbNIo_Z0PZZIOwO-FfcO-wloZeT0qmcURvYCHF1-yC4fW3WgU5WdOjrs-4p7pGKD80frCC-EK3TVzqURi3MxGDCuG_n8BnXrmsBUEWdN1_-_Pi1nRjOnlfbTDHOqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c0f3x6LY73FhzFEA965dQUfcGKttRlB9BgWpAf1g7JAEYuZn1qA5ECGlvR6Z7g3SXSs7ODFQu_F91Am-FBiTzXhhvfTR4jUyFMhzIY8qbMYXtWnZxOlPk23gMmU_UpIEOCj_AHmm2jPm3Tj_9B6ittrsoqSfrmazTzx-4wOAI_jMZLGRhK-RUVSHqTrf6X4vPSMdaSetH8qRos-SFCwNZD6OVRdE43q-XEoMb-BtJmXJul1Xgh6EVTBDtjq8zKrNbZpqaZrEQw_2ZqFt5nv-2xepx_90C7dNd3WC8rXfjoZcvOSURRupcPam0yXio02WgmbPzGD_lV-c_si1Dty9wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iiNCTAUkv9bGO58otGogrI1mGAqeEnkTTsUh_j3msw2VTdDGOgiyC-fpaQP7iaAI1PoMGGPtv45DI_wEOV39QK1fs6OAvcUIw4o6LdkF-uLKdkqQ4_csr-WErZ5R7oaEv75S8ac5sKT9MQ71eGEpclMSjGmvTh2dLMxEMxBeOkF_PvtNFUbm5XBUMXSEQrwREs2UcJlPR4WCklQNyipbaVLbXYwaCvAXvf2TiAZH4LF_1blsgiXDBIo-4EH06A6K7BMpvUG3C9Rd8gCbRjKC3MeZCTqwJ1w47FIAQ-dgUi7OU7Hsue41bhjaw4aVXR6LmdJf_yYrdWozu-SuddeHzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vx374LMd_EDq6SkyuhmB0xEhlxNxN-W36LdgKuwxVHOGsi3X2sXY9u_7bi2sWMlmGVqtTYW0ApWNzUCCg8zn_zItntvwv9tWzzymoq2vRyRJH5VSz4urVmO4YGMIO5y_7sqlYiznK2ihFk2EP5_UjFHFn0kGYjqDWrLVHtNrJLtCYmoN__1IrgOfBmS0e76TpW6QPybKolJMre5sBSrrW3K3tNLplBCQ6M6COhFA70lTisHpjgHdiyt8c_jekbkDeugiV3VyY6liHi1ngUh91E9ycXVYQJ37WtDndjcYAzMQ1peZu1T0dDdcMtxGTFTI-eliTllEj0LX_Otezf7slw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نفوذ هکرها به شرکت تأمین‌کننده تجهیزات ارتش سعودی و انتشار ۲۰۰ هزار سند محرمانه
🔹
گروه هکری «اویس قرنی» از نفوذ سایبری به شرکت «محمد هادي الرشيد وشركاه»، تأمین‌کننده تجهیزات و خودروهای مرتبط با وزارت دفاع و نیروی زمینی عربستان، خبر داد.
🔹
این گروه مدعی شد اطلاعات شرکت به نهادهای اطلاعاتی انصارالله منتقل شده و ۲۰۰ هزار سند محرمانه نیز در وبگاه آن منتشر شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/697976" target="_blank">📅 11:36 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697975">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
آقامیری: چند سامانه برای قطع پایانه‌های ماهواره‌ای و زمینی در زمان قطعی اینترنت داریم / فناوری استارلینک قابل مدیریت است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/697975" target="_blank">📅 11:27 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697974">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
آقامیری: چند سامانه برای قطع پایانه‌های ماهواره‌ای و زمینی در زمان قطعی اینترنت داریم / فناوری استارلینک قابل مدیریت است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/697974" target="_blank">📅 11:25 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697972">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HL92zGBtTpp_Vn0Q2kzAuWPak3-l_1ZryRpSWvFquKAwcQG0YXLsq7QsD7N5QQSPnUi_5SAslxuvNJZ3ZH5M9WpGD-Npoq4ZAd8U5zbMWJ1nKePKbFE59sznxGP7kWPbta7JaT1wsGcPqnaC3fXYd5UaiVrpExNYgmXIJAxXZuB0Sd3FpMWPrD8XZpg43yy56ts5YL0-hMAJTBS8zpT-0XcOXKFdl72inaMsj-vPZzFlOtcpg6GohCpaP7ApL0MIx6k35FiT6mBE5QdV2cDF5m2JgB_gclm0mVr0SSSy4YUwxnfHbe6G1nLF-itwZbdqY0sj7HBFSvTBSlE4p4sLGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VZsWt3EEzLwxGLLF8XkNp1O2A0-gjGHLElpfCZCe-lqIJ8ofU_8HPfVM79idv2Szyupo2QvjprnGaCJsZ7IqCRnn2nOmzpwXC9pbeGzEoG6VYKozRTGPewwQHjH-arvVjmQORQYbkyl27YMNrcODBnmL56tXlmHUAS5vKCDrryrXVEn-TezTOXYpvohZzuTy90IT6c8xE3lK6FT_Vh7noV_ASrWGXjrGS0eERxgI9gfiePVNosSUeDrPR9l9yCv8My8gKYo3eMI5-olYHr83IJAdIsBfYMrJROMjSQMMNPYaHFgV3T7MdoCweHl497v5ZMR19MUM6ZZqEVpkh3ElXA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
محمدعلی ابطحی فعال سیاسی اصلاح طلب، تصاویری از سید محمد خاتمی منتشر کرده که مصدوم شده و با عصا راه می‌رود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/697972" target="_blank">📅 11:18 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697971">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/byCmgzZyIxbB1EpcYpOjQszyKykY2gUZxLZ2JTdbx-uNV5qzfkda5FWvsG27OjMJ4E8fdMFQEUkdFhzwZku3eUEbjL9y-7Xr5YxVRShcFwFZ-PWs0D6VRhHOgsBHs64cmCYTIRWmYh9-m3rQp8VlvbM-QzP1EauATCPXPcPYKzlojCj_ePMXxhuWycL9NUnV_NeRDPea_hmH3wj_lcrX_weFG-zxXCgd8muzoZBZMUEz2JFjgWJltUwPTTSQxydMN3BJoboBs6c76FtYCtk2NmnZja-bl50wn-KtnwWS2X955fWgXWlA8HMv616l8ltq0E-XNkVQPk1_zd6Czxz4Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با اثر پرفشار جنب‌حاره‌ای روی ایران، روزهای پیش رو هوا گرم‌تر از معمول می‌شود؛ دمای تهران به ۳۰ درجه می‌رسد که حدوداً ۱۰ درجه بالاتر از میانگین این فصل است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/697971" target="_blank">📅 11:18 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697970">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
مهاجرانی: رقم افزایش کالابرگ برای خانوار سه‌نفره‌ای است که زیر ۲۰ میلیون تومان درآمد دارد و خودرو و منزل هم ندارند
🔹
مبلغ یک‌میلیون‌تومانی کالابرگ همچنان برقرار است و تاکنون کسی از دریافت آن حذف نشده است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/697970" target="_blank">📅 11:16 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697969">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4101438149.mp4?token=DJ9ZPtC_4UUeu408EzTOFClHVSpGDaYGGbbqBj4o2OgmHgdUUi16PeEAxs5UW-2CUTDbVBsY2JcFzLNJdCsyDwklxCn0Cl8LlT0n5vVTlfoU3ZzlFQKUBqvOqE1N19UceIqYsoHJ2KZ2IEoWQUP1yjMRajyijAq0b-bT9FBkg7SM49bKmPHqTEj9CcVbmDAHSO2JJLY89S1V5dYwMe3TvWJrbpbV5FCrJjXvqRZClAJLzNdsPSLsxMEqRfZaFjyhf9XqKg5OLZwBd3JZg2Uh30sI7haCRU3FfVWDYP3msRemJA-tlEO__RL5-lo2U4Hf0ebRYm71ZHXYflw-4qn7sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4101438149.mp4?token=DJ9ZPtC_4UUeu408EzTOFClHVSpGDaYGGbbqBj4o2OgmHgdUUi16PeEAxs5UW-2CUTDbVBsY2JcFzLNJdCsyDwklxCn0Cl8LlT0n5vVTlfoU3ZzlFQKUBqvOqE1N19UceIqYsoHJ2KZ2IEoWQUP1yjMRajyijAq0b-bT9FBkg7SM49bKmPHqTEj9CcVbmDAHSO2JJLY89S1V5dYwMe3TvWJrbpbV5FCrJjXvqRZClAJLzNdsPSLsxMEqRfZaFjyhf9XqKg5OLZwBd3JZg2Uh30sI7haCRU3FfVWDYP3msRemJA-tlEO__RL5-lo2U4Hf0ebRYm71ZHXYflw-4qn7sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چگونه بانک مرکزی نقشه‌های خزانه‌داری آمریکا را نقش بر آب کرد؟
🔹
اسکات بنست،وزیر خزانه داری آمریکا چندی پیش مدعی شده بود که
اقتصاد ایران تا دو هفته آینده فرو خواهد پاشید.
دیروز موعد دو هفته‌ای وزیر خزانه‌داری آمریکا به پایان رسید.
🔹
تمام این اظهارات و سیگنال‌ فروشی‌های متعدد آمریکایی‌ها با این هدف مطرح می‌شد تا
با ایجاد التهاب و ترس نسبت به آینده، روی وضعیت بازار ارز ایران در ایران اثر بگذارد.
🔹
در این وضعیت به گفته رئیس بانک مرکزی
طرح عرضه ۱۰ هزار دلار به هر کد ملی
به بازار این پیام را مخابره می‌کند که
وضعیت ذخایر ارزی کشور پایدار بوده و بانک مرکزی می‌تواند نیازهای ارزی مردم را تأمین نماید.
🔹
جالب اینجاست که در مصاحبه‌ای که اخیرا یکی از
معاونان وزارت خزانه‌داری آمریکا با بی‌بی‌سی
داشته، این موضوع توسط خبرنگار از وی پرسیده می‌شود که
چطور اقتصاد ایران توانسته‌ با وجود ادعای مقامات آمریکایی مبنی بر تمام شدن منابع مالی ایران، در بازار ۲ میلیارد دلار تزریق کند؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/697969" target="_blank">📅 11:14 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697966">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V43aAD_12fr3LlFdng4lb3jogFBWcBc0_zhD7T-I0qbgOhKRTv61yuwVndAh9_brwLOFnI21QZg2bcyIOyugieZPiObYuqHDCXU6JaJ5mnT_PpZKwa_w0m1rsDIZoy4TqGJQJARVPXuRb7-VOePffGlb2unk-Db-JeMhU47OKLg-RjWJioz6jfx04J_UTRqHSbD-uu_IZqAbxzNfXlQ8nr3YOyWIBd-kXPVe4aAUG8Pvpzwj1jlOUNng9bZ1VdvfIofnTzq-zembHdUYCnWd7j73OQcQPdsRRdGg85_6Ugkgy9Ve16TpaDPJoxd4Dd_Mz0tgDBuBHa3waGL_o3Yn3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/chylsfEuJfL_k7woQS66jx8Y3JaCuQVU4EHmgR6NfmIZNCxuftRsAn75JhkFcklTJiwLJTjdP6eMmljJUcp0qMsdD3_WhVyfMDwc0WIV9sy5xBloT8ZuhO5weSnnn_qXDXLEgCMFxIsy1xjfzg3015uIDuHB3QDUxinemXDZlgvVTH0S8XSHjU_t-w31hNWrfPpe4sgWwrGYGWZIr7U0qsxddzCr5iql4SYh-QtySdgmY-JVmxHGuMKVA21gVSonzjDtFTR972IgBRFhydHIzwrxTgWfqc0gX8kZYqCRIrxgSQArHwmjuYA3e1e-3M3pe04pugak2OM7aRX8u3WWvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J9mqaDAFg7YJPf6qMItJpJPWiPod9yr4WqHUMk-Kz3LPXcUb5EPBR-6HBZtChhntGHd8rbz5CkN0k-cx9PmbrX7WHRfEt8KfwcsSzffoIk0BUpAeIjW6iggQfiYePAjhTKKtvtg_fsVh2HpFrrbV-9gcgG3PjxIuPQjQKhSuWmW65NfSsCpJfsqhnmx55fOtnECJkYBplNnpkBSaX3-_UYsfKXKGRg4hLItu0ixIDIxH39pD2IH_ebzgGTU7SiS1W-Idk7JTc9cvH_1eiwq0zEujS-5pcIqQEF6fPPzlTycGM32R53Iw6akxHOZDPm_KhzRSd8FsEML3ssGb2NAolA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اسمارت ۲#؛ خودرویی فوق‌العاده جمع‌وجور که با ابعاد کوچک و طراحی برقی، توجه‌ها را به خود جلب کرده است!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/697966" target="_blank">📅 11:13 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697965">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
خبر خوش سخنگوی دولت به کارکنان: ترمیم دستمزد کارکنان دولت در بودجه ۱۴۰۶ دیده خواهد شد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/697965" target="_blank">📅 11:07 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697964">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
پرداخت وام ۲۰۰ میلیونی خوداشتغالی با کارمزد ۴ درصد  سخنگوی دولت:
🔹
برای حمایت مستقیم از شاغلان و متقاضیان، وام خوداشتغالی ۲۰۰ میلیون تومانی با کارمزد ۴ درصد و بازپرداخت ۵ ساله پیش‌بینی شده و سامانه ۱۴۲۰ نیز جهت پاسخگویی و ثبت درخواست‌های بیمه بیکاری نیروهای…</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/697964" target="_blank">📅 11:07 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697963">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5471664670.mp4?token=JxDc-cq4Rlvt7GYXuai6gaAzVZd3XDaECiXeuWsTq0RtN5WC41zduKjKb3sPv0eNl6xeyv33yPFnlvIRNuKEVmVWgOOP4pV7FsC0EFZd5hnjLg1koZySKuhez__hZkswJ6sWUxo55t5lYNLxBnXqK8EF-u3KmtWlsSXm4iKTFxuBQmAOTW65NAmZylUjNwr_-e79XAlLbMar9pYFM1SSY5-qJoab4Wtnz7ONZbXe5mMkAnT49gOVsIIC5S2coQA44IC-p03dwpSV-fsvCNadsserl_m782oTNWBA5wi56RiQF3TKOfiueTOHQadeKyFf0iVvECsshHIaIZGK6a3b1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5471664670.mp4?token=JxDc-cq4Rlvt7GYXuai6gaAzVZd3XDaECiXeuWsTq0RtN5WC41zduKjKb3sPv0eNl6xeyv33yPFnlvIRNuKEVmVWgOOP4pV7FsC0EFZd5hnjLg1koZySKuhez__hZkswJ6sWUxo55t5lYNLxBnXqK8EF-u3KmtWlsSXm4iKTFxuBQmAOTW65NAmZylUjNwr_-e79XAlLbMar9pYFM1SSY5-qJoab4Wtnz7ONZbXe5mMkAnT49gOVsIIC5S2coQA44IC-p03dwpSV-fsvCNadsserl_m782oTNWBA5wi56RiQF3TKOfiueTOHQadeKyFf0iVvECsshHIaIZGK6a3b1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
راز مغز استخوان
🍛
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/697963" target="_blank">📅 11:07 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697962">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/569f2c20bd.mp4?token=K6oOFFvaM66-qnHjkV0ZJI6RxCriN63luBNTMZI19qCNzET4DmQT8PV17pLfazuzFOnN6ufZEgESOpfjkJUiN1nDly4oY6nEP4DRqKqLURrh-VTkkv6eNOCYE0iOj68JmUWZeFcfAiLzlaCgZf86fgSMFGEBRnJw0RDbh92XFkS1Ji_5DXas_U1XzXSR6Bze7O1HgmO13dJTQDfrDq06B3xJ3eW5iGGECS9UkLigpt0urM3Lz7zLeAubDgGN8okMkFu6Pn4xZN1FVwUhwDDMLRiACTyH82xi_P65tkk6HzoPUAP4h7hsFRv99uj-p6G5OQG4-ZcQ8UwgxyLpu4haNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/569f2c20bd.mp4?token=K6oOFFvaM66-qnHjkV0ZJI6RxCriN63luBNTMZI19qCNzET4DmQT8PV17pLfazuzFOnN6ufZEgESOpfjkJUiN1nDly4oY6nEP4DRqKqLURrh-VTkkv6eNOCYE0iOj68JmUWZeFcfAiLzlaCgZf86fgSMFGEBRnJw0RDbh92XFkS1Ji_5DXas_U1XzXSR6Bze7O1HgmO13dJTQDfrDq06B3xJ3eW5iGGECS9UkLigpt0urM3Lz7zLeAubDgGN8okMkFu6Pn4xZN1FVwUhwDDMLRiACTyH82xi_P65tkk6HzoPUAP4h7hsFRv99uj-p6G5OQG4-ZcQ8UwgxyLpu4haNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚗
🧹
جارو شارژی خودرو با مکش ۴۵۰۰Pa
سبک، کم‌حجم و شارژی با ۲۰–۲۵ دقیقه کارکرد!
⚡️
اندازه جعبه : 16*16*6 سانتی متر
مکش نیرو:۴۰۰۰ - ۴۵۰۰Pa
ویژگی های خاص:قابلیت استفاده به صورت خشک در خانه و ظرفیت باتری ۲۰۰۰ میلی آمپری
🔥
قیمت ویژه امروز: 1,389,000 تومان
🏠
پرداخت درب منزل
🛒
خرید
👇
memarket24.ir/product/fast/26903/180124/</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/697962" target="_blank">📅 11:02 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697961">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
مهاجرانی: دستگاه‌های متولی گاهی مجبور شوند سرعت اینترنت را پایین بیاورند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/697961" target="_blank">📅 10:58 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697960">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
مهاجرانی: بخشی از صف وام ازدواج و فرزندآوری ناشی از حملات سایبری به بانک‌ها بود/ آخرین آمار تعداد و مبلغ تسهیلات پرداختی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/697960" target="_blank">📅 10:45 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697959">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e1979dacc.mp4?token=YHO1DK7u-WkJBTOjFjpnWtpQHhTkc2oadq31hME2RlSXQ1KifebEkdTafxcKICEpcR0rVdhe7mm8dSHAx0SsxBClrZa-J-6mbAqK56iCfLRdEIErcqRBQz6iWtooTUxFgxyi5HG617b17LA33knqSDqL2H4ivJOul4D3hsu3-CeSLwT-Wh_OOEbUXnAKYnTfL7IRMMFsyX1Z5Xt9LnvdiE3T7PiGQLzJcJFZFM8Gz3uNRC7daXcQ_UV4h--L2MQ1yPOw19lCu--a5Sp6vTw4TVeW5VeSZu8FrdhpIlcBW1WIfThb4Eg-tdmVBJZvijfc4h8Z1NyujQ14bqwwkXGbgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e1979dacc.mp4?token=YHO1DK7u-WkJBTOjFjpnWtpQHhTkc2oadq31hME2RlSXQ1KifebEkdTafxcKICEpcR0rVdhe7mm8dSHAx0SsxBClrZa-J-6mbAqK56iCfLRdEIErcqRBQz6iWtooTUxFgxyi5HG617b17LA33knqSDqL2H4ivJOul4D3hsu3-CeSLwT-Wh_OOEbUXnAKYnTfL7IRMMFsyX1Z5Xt9LnvdiE3T7PiGQLzJcJFZFM8Gz3uNRC7daXcQ_UV4h--L2MQ1yPOw19lCu--a5Sp6vTw4TVeW5VeSZu8FrdhpIlcBW1WIfThb4Eg-tdmVBJZvijfc4h8Z1NyujQ14bqwwkXGbgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مهاجرانی: واردات انواع خودرو توسط هتل‌داران و ایرانیان خارج از کشور متوقف شد  سخنگوی دولت:
🔹
به دلیل شرایط خاص کشور، تخصیص ارز به تمامی امور غیرالویت‌دار بر اساس دستور رئیس‌جمهور متوقف شده است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/697959" target="_blank">📅 10:39 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697958">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
مهاجرانی: واردات انواع خودرو توسط هتل‌داران و ایرانیان خارج از کشور متوقف شد
سخنگوی دولت:
🔹
به دلیل شرایط خاص کشور، تخصیص ارز به تمامی امور غیرالویت‌دار بر اساس دستور رئیس‌جمهور متوقف شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/697958" target="_blank">📅 10:38 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697956">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aXylFOZidh4QXgt6guiUTRiLDE9e50DdqNZzJFBWKgLsh3ZRbRO9vkX8G-jEJ-q6EThodHF6uIyY7sUu8bvPk7Nqm8ZlUbpu_rLI9cg0OtpbBocI6wmG7a1Eiq1o5adY7b2gKpA6OqXDxRpCXCja_KjlEf2kGpfnBAVJMwN8g-_xkP0RaUdDm_Fbm4oWIzrs-C-cqMOyfISORnkzsCEOOdB3p4rrGlvrChPou0RA5G42I_hrQatAtpzAha8ubXW1igky45fGkg5AUCav5nerlPGhh9kbBlbfKvB4C0ILXY_VnsEvNf-cVW5fDK5uEyk6jZwC-C5kQv9vt0WCLvG2tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
همزمان با ابراز علاقه ترامپ برای دیدار با کیم جونگ اون، کره شمالی ضمن آزمایش یک موشک بالستیک، از موشک قاره‌پیما با قابلیت رسیدن به خاک آمریکا رونمایی کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/697956" target="_blank">📅 10:33 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697954">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lKn7bt7tr0nl7tijzS5roafoLwlnevoX5Npian8WR-HOV9y2G-96NuhvdexGpeIFkMvmk1MzC11SxSMMyrrPis2hCmBQFFQy0K8ovxwTrJ60VLC3BgotZdSos1VeQo0pUIxTzzSj-J-8XNFDt6DM2V7w_LX-vCG-jJ4cr8i4v7ckcjR_qrZ7cQ0dd0zoO0ieDHZuX2jfSL7PYOFnvRIx0MOjcTKYem2KVvjXzAldk1sS1IO6pr7j36x-DsC32rc45X9dMVs_qxfAlzWwvsGVSdf0Aj3XlPrvaCNDqd2-UxoLxTL1i0vIHu-IvJi8N8p7w0evyvwInTPa_226xyc54w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X_kWdn3F5PAmI8X-xL7L_ne5QXVnBN23fRJqHPCNTltfnRD0qnI7hpBMajEe0JBKVyiwwmsl9ACg9nbBzPvcLWUGue0N0IODn2krB7XuxODVP9wwBiHVOaWDmvAPWe2yh0fnJ7ay33K4bQz9Hb0ETp05JJShaSHLQOGjiIMcIBwj4Ya4rWA7FC0x6bi5sPKJdqSQOMFtRjHIvprNyT5wtp3cAIw0bDCEt_09MFgd4Sr--dNTke5eWFRsjoKI2nv7zARO5onvrsY17hNaLHTiXxG7adbKphXC4ztAXt3mx8pHAdSPjDNgY9oRMxFWnnK92LYTcHYVpgXD3ZK4hrMn9g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری از وضعیت صندلی‌های سالن سخنرانی دونالد ترامپ در ایالت اوهایو
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/697954" target="_blank">📅 10:23 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697953">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
حمله سایبری به سامانه‌های سرمایشی فروشگاه‌های فرانسه؛ بیش از ۵۰۰ فروشگاه آسیب دیدند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/697953" target="_blank">📅 10:22 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697952">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f4eb8f82c.mp4?token=FXABoTmhde5i1kaGz2oed3N0KCQ_WWkFfxIJmVdAzELkbY0_cCUJzRFcsPkG_IVuqWl8q4IdOR89-PS9KyX6bRApMizjZJeSBYOaU3YmFzF03AN6bnfb8Y6LPWeiQFyPVPTmxwsMqIJmxwe6lI-Me-lFW6rtvIUnMIzSQUdzt1Qar_YHR5bU07-xSedEC9z1re4Ccp2oEDYZa9Ow5lrnACsFEyVerl2DoioKgPCX9m7tGptJRe9J1f0T_ErhxnQfMdgK-9rVUKS8Ta9uZbHwACx68Qzpb-nhZgjHZ6OsUs_dpWeqAta3T18kgIFEA_pmIQUhKnWFG4LLRtss9OVY0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f4eb8f82c.mp4?token=FXABoTmhde5i1kaGz2oed3N0KCQ_WWkFfxIJmVdAzELkbY0_cCUJzRFcsPkG_IVuqWl8q4IdOR89-PS9KyX6bRApMizjZJeSBYOaU3YmFzF03AN6bnfb8Y6LPWeiQFyPVPTmxwsMqIJmxwe6lI-Me-lFW6rtvIUnMIzSQUdzt1Qar_YHR5bU07-xSedEC9z1re4Ccp2oEDYZa9Ow5lrnACsFEyVerl2DoioKgPCX9m7tGptJRe9J1f0T_ErhxnQfMdgK-9rVUKS8Ta9uZbHwACx68Qzpb-nhZgjHZ6OsUs_dpWeqAta3T18kgIFEA_pmIQUhKnWFG4LLRtss9OVY0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کیک قاشقی، خوشمزه‌ و آسون‌ترین عصرونه پاییزی اون هم فقط با یک تخم مرغ!
🥧
موادلازم:
🔹
تخم مرغ ۱عدد
🔹
وانیل نصف ق چ
🔹
شکر یک سوم پیمانه
🔹
ماست ۱پیمانه
🔹
بکینگ پودر ۱ق غ
🔹
آرد سفید یک ویک سوم #آشپزی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/697952" target="_blank">📅 10:21 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697951">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
درگیری نیروهای امنیتی با تروریست‌های جیش‌الظلم
‌
🔹
یک خانه تیمی تروریستی در منطقه چاه احمد کورین زاهدان طی عملیاتی از سوی نیروهای امنیتی منهدم شد.
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/697951" target="_blank">📅 10:16 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697950">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MLl2xvjP1AZTfhVxD1qJ1xJtHsB2jn16I8d5kRjEaOqpg2yhI6Gb0cF7hZLFoVRA9ctKWkt-0uRvLysBlLSYJrKkP35kPev9Jsd6I_BG9HUJcPF1v-Us4IqAoGpsr3Vr6h0EIc3-OOCAr-3oWSpkOtH7HQ8ewcRrd7O3GIMqoJoFxPc14o2sdZIaP_DBtmkbjimTjOpVzGknV5R4v9fMlhuohEpRa55A6g7RfTMYBLr_Hwx_WoDZ-5DiNqnBzAUFhDP_mCpOKcQza_lO4T1OU4xSYfe6PkLU74pWbZsvzf1MoFg_lre1F8LI_S7ELmkc2eBe8SgGETdysZ2bDQmj7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگاهی آماری به دیوان حافظ!
🔸
دیوان حافظ شامل ۴۹۵ غزل با مجموع ۴ هزار و ۱۹۳ بیت است که یکی از برجسته‌ترین مجموعه‌های غزل در ادبیات فارسی به شمار می‌رود.
🔸
میانگین طول هر غزل حافظ حدود ۸.۵ بیت است و غزل‌های هفت‌بیتی با ۱۴۳ مورد، بیشترین فراوانی را دارند. همچنین نزدیک به ۷۴ درصد غزل‌های حافظ بین ۷ تا ۹ بیت هستند.
@amarfact</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/697950" target="_blank">📅 10:16 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697949">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
پامپئو، وزیر خارجه آمریکا در دولت اول ترامپ: تعجب نمی‌کنم اگر ترامپ با ایرانی‌ها برای توقف حملات به فرودگاه‌های عربستان مذاکره کند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/697949" target="_blank">📅 10:08 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697948">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cb65d802f.mp4?token=ocoZyKO6LxPeSCfv-2QxrIRmmSbEG-Cy12nnsf5YToNFvp-6iaMmAMUEQDGPOGJAeUZ9J_42BDbJTnGtkzeFZQZtANeiAfKNhM-cmY4fIHH4WuHwrM5E3_H55OwHvOXwK5x6yJOgk7aC4oHlkN95eKNmdHadX3jxlND_3Cmm3lPiixGjumbo9D84I4kroaztNUZ59_saZEVvmTcb_sS0SPjWpe-3wenGyxVgJI90thUEK2TvfigxWTIKNRw6QZ65sMxjxEkGh0bOA1ITuGszenWQH4cANoqg-GIWFa9qcUIqqfUthJxloLP4qW0MOqSZr4WfjYD6Ys89YLtj2GV1Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cb65d802f.mp4?token=ocoZyKO6LxPeSCfv-2QxrIRmmSbEG-Cy12nnsf5YToNFvp-6iaMmAMUEQDGPOGJAeUZ9J_42BDbJTnGtkzeFZQZtANeiAfKNhM-cmY4fIHH4WuHwrM5E3_H55OwHvOXwK5x6yJOgk7aC4oHlkN95eKNmdHadX3jxlND_3Cmm3lPiixGjumbo9D84I4kroaztNUZ59_saZEVvmTcb_sS0SPjWpe-3wenGyxVgJI90thUEK2TvfigxWTIKNRw6QZ65sMxjxEkGh0bOA1ITuGszenWQH4cANoqg-GIWFa9qcUIqqfUthJxloLP4qW0MOqSZr4WfjYD6Ys89YLtj2GV1Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیو انصار‌الله از هدف قرار دادن نیرو‌های ائتلاف عربستان توسط تک تیراندازان خود در جبهه تعز
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/697948" target="_blank">📅 10:05 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697947">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f04905ab9.mp4?token=NmPH0PNiyL9eE7PShxt81Br4EJ8cbJBk_kWM7zOa0G5CAuwRhaH224yj7AWlaC7j-NEJ4VHem_vCKMynVrDkRlSOVpAdnG8SqG-6RX4bTkJd1MVzmRQvCr1-3SpTvFERm-hQDg9AefCZjIPBuUmjUgtGvvp00krjrpRXRAV0b_HJ43Noq5fqp218JV-2ioODo4GW2ui_GraGoAKVXTKCmROhZata-e9XWvxfCm3of0IA9m6ErDtInvgRqEvFdzp_DaXQxOs1vsmoohZeGtuIYs1E1YcQIYE8HYTTOJi3WXJk6DYdnHiRGNeQfB8_Trz07_jZC2YH5wZMhJAHPE7xwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f04905ab9.mp4?token=NmPH0PNiyL9eE7PShxt81Br4EJ8cbJBk_kWM7zOa0G5CAuwRhaH224yj7AWlaC7j-NEJ4VHem_vCKMynVrDkRlSOVpAdnG8SqG-6RX4bTkJd1MVzmRQvCr1-3SpTvFERm-hQDg9AefCZjIPBuUmjUgtGvvp00krjrpRXRAV0b_HJ43Noq5fqp218JV-2ioODo4GW2ui_GraGoAKVXTKCmROhZata-e9XWvxfCm3of0IA9m6ErDtInvgRqEvFdzp_DaXQxOs1vsmoohZeGtuIYs1E1YcQIYE8HYTTOJi3WXJk6DYdnHiRGNeQfB8_Trz07_jZC2YH5wZMhJAHPE7xwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک هموطن پس از بروز مشکل در سیم‌کشی ضبط خودرو‌، آستین بالا می‌زند و شخصاً دست‌به‌کار می‌شود؛ نتیجه اما اختراعی است که ظاهراً مشابهی در دنیا ندارد!
😄
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/697947" target="_blank">📅 10:05 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697945">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WS2WaT8E66krNztvmNG70a-46vYEs8ux2HUpJ4vUjfAHBgMVkxyxCYb-wiZvYaQpOdaCxRoR54oREKHCLXzWRnpRKyjKIRD0NQSZKLU_ZK9q5JsQoxY8VCpuH9rowHC6QDMUpiBG-J3t82e5HyPqOjRraqkXu2fraAELb2bvBVorY1l7Gb1srUgvoINiGHcTG2GRRYuzprJuhVwJlvd-OkPCr9RHMeP5Fx-zd2Y0wAa7MZqVky_54m3MZ73PpLwv72GtxOmxRHW_KPjPw0MiQ0gCeWWbMA3Y1oftX6xA62N55XU3sDoSflouGFj7JwvKF4KbVzazhklUi-b2IYLF9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرصتی شگفت انگیز برای کارجویان تهران
شرکت رایحه گستر بینظیر شرق(اسکلاره ،نایس پینک اولترا) جهت تکمیل کادر فروش  سوپر مارکت و گالری  تهران  بازاریاب فعال پر انرژی جذب  مینماید
-حقوق ثابت وزارت کار
💥
ـ به همرا ۱۳ میلیون کارانه ـ به همراه تا ۶/۴ % پورسانت از فروش
💥
💥
💥
💥
💥
دریافتی به همراه پورسانت۱۰۰+میلیون ماهانه  بدون سقف پرداخت
💥
💥
💥
💥
💥
ـ سبدی کامل از محصولات ادکلن شوینده بهداشتی
ـامکان ارتقا شغلی
💥
ـ پاداش ماهانه و فصلی
ـ امینت شغلی در محیط دوستانه ـ پرداخت منظم حقوق
ـ داشتن وسیله نقلیه مزیت محسوب میشود
ـ فعالیت در محدوده جغرافیایی مشخص
ـ پذیرفتن افراد با تجربه و مبتدی ـ حمایت و آموزش
ـ بیمه تامین اجتماعی تکمیلی عمر  مدنی عیدی و سنوات
۰۹۱۰۴۵۷۱۳۶۸ شعبانپور
@hrs855
تماس و ارسال رزومه</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/697945" target="_blank">📅 10:00 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697944">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbf9c5fb26.mp4?token=sW8XtfKgQjzYrfpxxgdMNgPlSX2dh9Djdsyr45giDTkiFGx2sF_sDzerj7N5ZTjkx5kK_NcZ2Wp6YAISp3scjEcdWmmBYzqi4up5I-PQIkfqvLywjLDeyjQU_53zKIANo6Z24rN6tccHngjdSJMrCZFkB1a-UgZGLghIoTrYDsdqvJuKWyEji1qz98rmQD2j3yL5UYBBxh2cwgphIFmpfR3pDm-L7WfjtxJbtwaZuJOumxujA_3UsRyZG_sQEmxJA9MRy4BzDdAlKuZEXPF8xRDukBgTgdCgwSHTSBcvzCy4Vn8JztQWhL2h1tShc1E1TTn5OdnPgnq1cMvdRoGXdRsLPZa5vpGZBlm9NjfHX9d_3N2UpP8t1vMd4VN3PJpJZ_DSehlgjOOlFonTLNlMN5qBJY6dB_DJp0OgAdEUJlC1e-dPHSnYHgbe2m3J-wIoPrPEgQuu03D3c19MBeGlTVYpQ275X0S6ps6djJeb2MeFmQdTWfK0EBl06Iqro94tbA0ta0QhZVmhxremZUrHHaYVNH0jkw_Li8CDT7cc3cRyVDKB6S8y7FEnctoH3jjzvgW30ENn6M-7-6ZdxyiBkduTczTONKHA3NbsALpTWKz82xkwZh7Rnagv_JmmqNJfnpVJ9D3DFm2WpdbPQ8tbpYQKVNUWRIoDEgrf5E-f_VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbf9c5fb26.mp4?token=sW8XtfKgQjzYrfpxxgdMNgPlSX2dh9Djdsyr45giDTkiFGx2sF_sDzerj7N5ZTjkx5kK_NcZ2Wp6YAISp3scjEcdWmmBYzqi4up5I-PQIkfqvLywjLDeyjQU_53zKIANo6Z24rN6tccHngjdSJMrCZFkB1a-UgZGLghIoTrYDsdqvJuKWyEji1qz98rmQD2j3yL5UYBBxh2cwgphIFmpfR3pDm-L7WfjtxJbtwaZuJOumxujA_3UsRyZG_sQEmxJA9MRy4BzDdAlKuZEXPF8xRDukBgTgdCgwSHTSBcvzCy4Vn8JztQWhL2h1tShc1E1TTn5OdnPgnq1cMvdRoGXdRsLPZa5vpGZBlm9NjfHX9d_3N2UpP8t1vMd4VN3PJpJZ_DSehlgjOOlFonTLNlMN5qBJY6dB_DJp0OgAdEUJlC1e-dPHSnYHgbe2m3J-wIoPrPEgQuu03D3c19MBeGlTVYpQ275X0S6ps6djJeb2MeFmQdTWfK0EBl06Iqro94tbA0ta0QhZVmhxremZUrHHaYVNH0jkw_Li8CDT7cc3cRyVDKB6S8y7FEnctoH3jjzvgW30ENn6M-7-6ZdxyiBkduTczTONKHA3NbsALpTWKz82xkwZh7Rnagv_JmmqNJfnpVJ9D3DFm2WpdbPQ8tbpYQKVNUWRIoDEgrf5E-f_VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کَل کَل ابطحی و مسعود پزشکیان در مورد قلیان⁩!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/697944" target="_blank">📅 09:59 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697943">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59057b7ed9.mp4?token=Te5iSlcJgJWrHfVfYE2cHlEwjAT97w8sNhRfchMVF_mhDnBufS6lb_BYK7FjRW09Yj8d1XtjpaB9x6PdJERcDc5FzHMyZfJ_EyTe_kzCMReUGfh2VrUUOKMKVuubDxmuj5ifLWTSIvdhizbPf1GoYBU_tu-heMpt4b1GOjdg9T6uY2KK5BFEaR6zklmRT3NUlgzRjniKZdC7uW1ANCzD_mbeQ9pGWaxj3OZllWhm589M_q4ZRxpslhMQsRVzQCNQJZaRkr9MR-l-wmHtkrjGIoKXZtnmYZ7nnH1X9DV1Lcg0Twk2t7ic922v5xkCoYojLkWA25qL9aEBAbYJOzZKQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59057b7ed9.mp4?token=Te5iSlcJgJWrHfVfYE2cHlEwjAT97w8sNhRfchMVF_mhDnBufS6lb_BYK7FjRW09Yj8d1XtjpaB9x6PdJERcDc5FzHMyZfJ_EyTe_kzCMReUGfh2VrUUOKMKVuubDxmuj5ifLWTSIvdhizbPf1GoYBU_tu-heMpt4b1GOjdg9T6uY2KK5BFEaR6zklmRT3NUlgzRjniKZdC7uW1ANCzD_mbeQ9pGWaxj3OZllWhm589M_q4ZRxpslhMQsRVzQCNQJZaRkr9MR-l-wmHtkrjGIoKXZtnmYZ7nnH1X9DV1Lcg0Twk2t7ic922v5xkCoYojLkWA25qL9aEBAbYJOzZKQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای رسانه‌های صهیونیستی از بازرسی یک فروند هواپیمای مسافربری در پی گزارش‌هایی مبنی بر احتمال وجود بمب خبر دادند
🔹
این پرواز از نیویورک به فرودگاه بن‌گوریون آمده و تمام مسافران از آن تخلیه شده اند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/697943" target="_blank">📅 09:53 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697942">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afc99cc0d3.mp4?token=tq0avlVtDZK3JXBwL5_j0qz_lcZnu5K3zkTdXEzomHzDxImZH-cBHENCOboFGx7-XU7if3lUsWrtVqFGnloDOWFpj4ZB7mpiHudbVDKCH6O3v9YZarsQiyQSrZQUNxoCWRg_2ypYb8v5nTaW9DbdzyEXrz1FKVTIRhuJ93vJo-IycfLQ-VtADcbogL7qCFdxQrh6aA_6wAKfuNh4U9sQs5HpakNsrATJ56JffoXntPepYADttw2xvbdDmqn189-tRC4Pj4OBPkjpcsPPLjoJznIAqfOHcDlt92QxAaPHBKN9wHsV3xOthZhdGuZWX0b5-9s9SwMxdIzYo9e18BaeegI3qQvCOIRHGcYRUkZCZUYGv0PvZM1eilS-0S-FqW-szfmbEkpf7-myQBbO987tJio0tJmqdEUH4w3UWfDgcbgmfNOgIXWr5CiSklsmilmQlpwR7fbPdxdegwX7eAjEfDnCRocpYXldloGEnkhe8VZfgYXIfKo50WQOKofl1Dh0f4IeRktFR298Z0QgR4m9lmFiKGLpx5ulBCMqomwowddO6c3uk4IlYn-l9Bi2oThxtXvpGeBvc3WD2pXzZFKlbuQMlaOvrJUGAIYvcAqBVnPzPFymajl4tFEkqnM7WueVdzj-AKRDx-S5qvmJLtOhBr8D7n7Bh0-A3V4sNCfZdL0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afc99cc0d3.mp4?token=tq0avlVtDZK3JXBwL5_j0qz_lcZnu5K3zkTdXEzomHzDxImZH-cBHENCOboFGx7-XU7if3lUsWrtVqFGnloDOWFpj4ZB7mpiHudbVDKCH6O3v9YZarsQiyQSrZQUNxoCWRg_2ypYb8v5nTaW9DbdzyEXrz1FKVTIRhuJ93vJo-IycfLQ-VtADcbogL7qCFdxQrh6aA_6wAKfuNh4U9sQs5HpakNsrATJ56JffoXntPepYADttw2xvbdDmqn189-tRC4Pj4OBPkjpcsPPLjoJznIAqfOHcDlt92QxAaPHBKN9wHsV3xOthZhdGuZWX0b5-9s9SwMxdIzYo9e18BaeegI3qQvCOIRHGcYRUkZCZUYGv0PvZM1eilS-0S-FqW-szfmbEkpf7-myQBbO987tJio0tJmqdEUH4w3UWfDgcbgmfNOgIXWr5CiSklsmilmQlpwR7fbPdxdegwX7eAjEfDnCRocpYXldloGEnkhe8VZfgYXIfKo50WQOKofl1Dh0f4IeRktFR298Z0QgR4m9lmFiKGLpx5ulBCMqomwowddO6c3uk4IlYn-l9Bi2oThxtXvpGeBvc3WD2pXzZFKlbuQMlaOvrJUGAIYvcAqBVnPzPFymajl4tFEkqnM7WueVdzj-AKRDx-S5qvmJLtOhBr8D7n7Bh0-A3V4sNCfZdL0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیوی وایرال‌شده از سگ فلجی که به کمک چند نفر توانست حرکت کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/697942" target="_blank">📅 09:49 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697941">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2225ffdb56.mp4?token=SVSjA6hRZrPNaop45awdtO_C3K_i3xl47LG2ToMgqO21bQelulVL9NFhWESjMUfEze9ljlFxHJ7vfoPRzJ7SCR9GlEdh_5Q5LRyR6qvleRcnoNtoS9prNp34iPV3Vw_gXQzptDh3RJobfG5qbfZ45bGhq3lthIAGzJGmmYKbF-LY5SmfCvdgD6iBMPp5V3ZjizYwdK0k0q94J33JbSDEMzyp2AUrDp2FKI5MKXAmYkCKkGs3S0NoAdVpfHjQSap7UlaAceMRWt6inHCWpl-bEdJtMHXvXv8MXjWDJWNAz0Vdl23ishWL3X71Zhdd45wkCP4Z5MItl_vCDafc09G_BjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2225ffdb56.mp4?token=SVSjA6hRZrPNaop45awdtO_C3K_i3xl47LG2ToMgqO21bQelulVL9NFhWESjMUfEze9ljlFxHJ7vfoPRzJ7SCR9GlEdh_5Q5LRyR6qvleRcnoNtoS9prNp34iPV3Vw_gXQzptDh3RJobfG5qbfZ45bGhq3lthIAGzJGmmYKbF-LY5SmfCvdgD6iBMPp5V3ZjizYwdK0k0q94J33JbSDEMzyp2AUrDp2FKI5MKXAmYkCKkGs3S0NoAdVpfHjQSap7UlaAceMRWt6inHCWpl-bEdJtMHXvXv8MXjWDJWNAz0Vdl23ishWL3X71Zhdd45wkCP4Z5MItl_vCDafc09G_BjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مشاهده پلنگ در بندپی نوشهر؛ محیط زیست هشدار داد
🔹
در پی مشاهده یک قلاده پلنگ در منطقه بندپی نوشهر، حفاظت محیط زیست از مردم خواست از نزدیک شدن به منطقه خودداری کنند.
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/697941" target="_blank">📅 09:41 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697940">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">Live stream started</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/697940" target="_blank">📅 09:41 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697938">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
ادعای رسانه‌های صهیونیستی از بازرسی یک فروند هواپیمای مسافربری در پی گزارش‌هایی مبنی بر احتمال وجود بمب خبر دادند
🔹
این پرواز از نیویورک به فرودگاه بن‌گوریون آمده و تمام مسافران از آن تخلیه شده اند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/697938" target="_blank">📅 09:39 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697937">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
مشاور رئیس‌سازمان برنامه و بودجه کشور: مهلت ثبت اطلاعات کالابرگ احتمالاً تمدید می‌شود
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/697937" target="_blank">📅 09:35 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697936">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b03808fb9.mp4?token=E9ywTSKABv7pWff5SFDWHGULyHoBoGc6ThP6GDMUiY3VSgb1tGn30UvfJcyDNQCdlwqxBBYElv6hd0t7DV_J0YiTU2l3YfzbpIoDIQ9LYdncKiMU9X9E-HfaWAOf-hGeFgqq47Dh0rQgCDdANrMfb7jAlH4jKwQL-eB0hidw9G0-wEeCcjPWxAyldSSH1dt4Z4omFBBII11xZARhudj2i25jpcq5VpkEoiKMruN64T8fidZGTPaB8u-QCxuWj57ctRLOpKIVlxfN77ed76F6Klb1Lvf_flJJH9Y1viOqGlf-AqWa6jbpnFz6AfjIyohB8D7oXt6ZOIjmrGuxnRrAZYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b03808fb9.mp4?token=E9ywTSKABv7pWff5SFDWHGULyHoBoGc6ThP6GDMUiY3VSgb1tGn30UvfJcyDNQCdlwqxBBYElv6hd0t7DV_J0YiTU2l3YfzbpIoDIQ9LYdncKiMU9X9E-HfaWAOf-hGeFgqq47Dh0rQgCDdANrMfb7jAlH4jKwQL-eB0hidw9G0-wEeCcjPWxAyldSSH1dt4Z4omFBBII11xZARhudj2i25jpcq5VpkEoiKMruN64T8fidZGTPaB8u-QCxuWj57ctRLOpKIVlxfN77ed76F6Klb1Lvf_flJJH9Y1viOqGlf-AqWa6jbpnFz6AfjIyohB8D7oXt6ZOIjmrGuxnRrAZYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیو وایرال شده از ادای سوگند قانون اساسی بر نسخه‌ای از قرآن در مجلس عوام بریتانیا، توسط «سغال عبد الولی» به عنوان اولین نماینده زن سومالیایی در پارلمان بریتانیا
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/697936" target="_blank">📅 09:32 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697935">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3f1da4b81.mp4?token=lIpYJfxHW1jxzYFcQVdb8erMN8BVS-WD6HuREhtqNIrfGJlWWDfMB8zZvUMlf50Q9NWw-ROVFy59Hd2XmMVNNFA6RtTtHXBZWgfI4K6XMm3wXuA2A3wtipXh7twT8-HwGA7CWXGmzXg3OQ146KAKmTq9nabfrYXb-GyHsru-jfQIoTOdDTVqq8ZOyEMP6cm01CUg2RmEIZypnbTNEtp3KOa10A0rYyj4SXOX11petV9VhBcE38Acu6QEqx36g7C9CZdZJ3blOwmjQ4FJOEejPLXy5lKuPePJbhsMGsMHsGGaD8yiiL0Eqt6mXPbFNt4SvMZyUxOdMQ7ANZH69-XsEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3f1da4b81.mp4?token=lIpYJfxHW1jxzYFcQVdb8erMN8BVS-WD6HuREhtqNIrfGJlWWDfMB8zZvUMlf50Q9NWw-ROVFy59Hd2XmMVNNFA6RtTtHXBZWgfI4K6XMm3wXuA2A3wtipXh7twT8-HwGA7CWXGmzXg3OQ146KAKmTq9nabfrYXb-GyHsru-jfQIoTOdDTVqq8ZOyEMP6cm01CUg2RmEIZypnbTNEtp3KOa10A0rYyj4SXOX11petV9VhBcE38Acu6QEqx36g7C9CZdZJ3blOwmjQ4FJOEejPLXy5lKuPePJbhsMGsMHsGGaD8yiiL0Eqt6mXPbFNt4SvMZyUxOdMQ7ANZH69-XsEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یاد بگیر هر نوع پیاز برای چه غذایی مناسب‌تره!
🧅
👨‍🍳
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/697935" target="_blank">📅 09:28 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697934">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CjDN6WXtramGPSquF0Ihn70__l1YS-wS6cDg6rPGjN7V0IYVvjAjmltERKcmRejQnuMZUdL1IQfYliQ_zmv_0k9J4wDMxZ-fwtMX08LkmMai4nYPUGxWtZh0miLWVRk6vRgJ3Tb8e-QPnUDI_maiZAPC1-KhHCXGfc2JnK-3p_QS9wmtDAmoOqrNWDdlyGAycc4O9fj4YkZwd3cdvSXt2eZFYiB3QZyYliMad9pNkmefAcjMKjRnDxpONZ5DgGRHQvkJ9gnWCaUbBDdwfdnB1seP3OQc0Pn0t3KiwjnNsJIdPDWfzBZ5NZ78nMqXyHDMh2PQ-LTMFhuwiZG4sylqlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جایگاه شهرهای ایرانی در میان هزار شهر برتر جهان
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/697934" target="_blank">📅 09:21 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697932">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UrFGD9bxkHOpOZVFM4RO1Fst1QzFnBZel93qOXewZ4i3D4AXgUXwAIprL62R2g9Z8HVtsOWTpJbFHdEY0qaOjRwzqoEXldlCWsLeXLU7eEWTiA4KUQ-23GwydRxlDrPhiwdIrjBIESssaS8AKnyipuqaMP0WMJMwrnJ1eegac42qUr8T7Wmdl45fUfEsM4vsyZUfOOAU2Br4ZKF3Lruw6awEYh-BObEhwMyoII-Tk53oOsG12B8c63cqI4tGfKM4NltcxGmXfko96gzLLhiVbpC3vGBH2pjNZExH6AVGyOuH2bmuWnF0fjyGehteU_n5jFc0kIRpQ3e0iL76JkzRlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cff7a0ac5a.mp4?token=AEFNTRIucXunZRqCZKvwo_S_31GJlFitIfax6LlEU-qjxndpriUjvPeBjirZeNbNS1iZ3Y1c0zWcHyfgKdDF2cYS_r26QNwo-qzfj-aEJYdwWvv-MbC1EcWcjvFMSlttxijgAarUQIgda2w7G5NAtDrz9owN-NylHayep9Gc9svfd2Y_Yskv0KH9e1jZ9DIRtcxNJAHy2VUR_arDLPQLz8BP_VeAUaZuCvnRmpnFbgAlMX-cQ0kBEbtJdF38YEo83l2RZGaLRmrhn8G3EOOubDyd6isLqDfYv-L6OfsnH7PGIOojqQPc5zZlbMD89V3wJkGNbd1Z7k7XClfawkx-rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cff7a0ac5a.mp4?token=AEFNTRIucXunZRqCZKvwo_S_31GJlFitIfax6LlEU-qjxndpriUjvPeBjirZeNbNS1iZ3Y1c0zWcHyfgKdDF2cYS_r26QNwo-qzfj-aEJYdwWvv-MbC1EcWcjvFMSlttxijgAarUQIgda2w7G5NAtDrz9owN-NylHayep9Gc9svfd2Y_Yskv0KH9e1jZ9DIRtcxNJAHy2VUR_arDLPQLz8BP_VeAUaZuCvnRmpnFbgAlMX-cQ0kBEbtJdF38YEo83l2RZGaLRmrhn8G3EOOubDyd6isLqDfYv-L6OfsnH7PGIOojqQPc5zZlbMD89V3wJkGNbd1Z7k7XClfawkx-rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توییت جالب سفارت ایران در زیمبابوه درباره ترامپ و تنگه هرمز:
🔹
«ترامپ در حال انتقال نفت از طریق تنگه هرمز است.»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/697932" target="_blank">📅 09:17 · 21 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
