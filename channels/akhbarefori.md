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
<img src="https://cdn4.telesco.pe/file/ei9NaVnKPmeXN0n2nZKXXwmOnxMxfDo3DM976HcReRA3IYQBaccEQi_YsqcSwO_Guec-UEkb8Ydp6bFbpKfHD-qz7olP0bMai7aXGiGMX2dwSeLm4Xhf384OXB4cjRo6Mbsm5fYMdakqIPJo84fLctKrhftAaO7Exp21nZSdohzQ1Mt9mwMytmfmetrx7_-kBoaywBlg0pqIxM2t1r8Lt2Qkv1wjHkNsJW9s6tIRBY6BeiLSbJP3VU9nzbO05Ump7MHs0kSQnY_XNGI5MQZKtD8dYFeVfGZm7qnAphmISZxl6m29IdvYgqRxurLcRs7UTvV1LdkyrV05HdTovpYJCw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 3.91M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-24 16:43:36</div>
<hr>

<div class="tg-post" id="msg-652280">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S6IHSLr6mGecTfXsxJ1R0d8FuFbckXkfGpsPzKS2mD6qZItWZQUL6RAh_VP33W7GpyPtjmN6lYcutZRpQ8QcrVjIVK-CVjPM_EOErJAzUYS5uSwUob4NwBzJURCmAAyXyki4uOcvIDlW5p8A31KF250BjUbWNbKq57o7whgWyqkt8KkQfAWOhHP00QWFT9c0ZNVbjwPc7I0L9kmZRNjmIhbm4d65JJziACFO32SYJvvCqG1UyIwr3mW9JMhgMuXn_17Jh8BEN1MA5Yx6C0r-ZdZoCAihhIJ9PXdOMpkp7JVoq159Hqib0MdREmqR0_bE6g83NxzugEiLE7_1O5Cf-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تهدید تازه وزیر جنگ اسرائیل علیه ایران
🔹
وزیر جنگ رژیم صهیونیستی به رغم تمام ناکامی‌های ارتش اشغالگر در مقابل محور مقاومت در تمامی جبهه‌ها، ادعا کرد: «مأموریت ما در ایران هنوز به پایان نرسیده و باید اهدافمان را در این کشور کامل کنیم».
🔹
اسرائیل کاتز مدعی شد: «ممکن است به‌زودی عملیات نظامی در ایران را از سر بگیریم تا به اهداف خود دست یابیم. ما برای هرگونه اقدام قریب‌الوقوع در ایران آماده‌ایم».
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/akhbarefori/652280" target="_blank">📅 16:14 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652279">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b95Gw0IvsR-wvIdDXw3SOZmgC7fweHNwwYM_u-q1Hm8MYtEbcRIo30MlUN4ypNaOSlt6TcuASMXXPGBgmMn1T01USvb0zqaF4h38nwKygNx80spxU7hlpirBsI6ElZ97rHdouwLKlNJbBL-3gmAbfh7Feynr2JB53nioIZHcOcCYcqqMFYU_zO1fkAK-fRnFFdgGkEw-W4y_HVBKUWxyx0bKHi8EZmTQ8U3rKql8lTCF1MtCdCKSXjEKcmCqBFSZYYZikjvw-v0XrcnrBKXiBhmtcOWBFzXMJS3qSrllHOueeDcN6Y5slplzUdK_iaI95gJ87nALd-StGfazPmEYNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تریتا پارسی: امارات با پیوستن به توافقنامه ابراهیم مرتکب اشتباهی بزرگ شد؛ توافقی که هدف اصلی آن ایجاد ائتلافی عربی-اسرائیلی علیه ایران بود. حالا به واسطه جنگ اسرائیل و آمریکا علیه ایران، آن هدف اصلی به وضوح قابل تشخیص شده است
🔹
این اشتباه از سوی امارات بود چون به این معنا بود که امارات خود را به دشمنی اسرائیل با ایران گره زد؛ دشمنی که بسیار عمیق‌تر از تنش‌های خود امارات با تهران است، با این که امارات در همسایگی ایران قرار دارد در حالی که اسرائیل حدود هزار کیلومتر با ایران فاصله دارد.
🔹
اما ابوظبی حالا در تله افتاده، و تا حدی به نظر می‌رسد جنگ ایران با هدف وادار کردن کشورهای شورای همکاری خلیج فارس به نزدیک شدن به اسرائیل برای جستجوی حفاظت در برابر ایران طراحی شده است.
🔹
به همین دلیل در میانه جنگ، نتانیاهو مخفیانه به ابوظبی سفر کرد و حفاظت گنبد آهنین را به امارات پیشنهاد داد. اسرائیل این را یک پیشرفت بزرگ در روابطشان می‌داند.
🔹
در واقعیت، این تجسم همان تله‌ای است که توافقنامه ابراهیم برای امارات تبدیل به آن شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/akhbarefori/652279" target="_blank">📅 16:12 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652278">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rV5CUn04TCaEC0lbMybJbEyTiYdD1RzOUSVbnHJHMCkVW054bSs4rrhgSCo-Y6AlGtHnXAm3QtY9zGgTfqzgELYuE3ViCvvqZWrOl4osNE14tHiB4oTOhjn_WhnAcL6Ty_ewGVdjoP2kIyJT5ply7Jus35a9WkwRZ-aSan3Q3mTMjNbIl5JRe9Nzo-IJGlll5Kiq2_nZ0P_HpOXdohSSlIVS8KGTCutQ-KaujxhEq2I3LCIQ9h27-u96dRPvB2ZingbpsfDl8UQmO-ATl2n4ylt_LQnf98G3M0dvEfMsZASbO5Zn7uW8s4tEemnC7YdhWJ70MrlZqPPdJnhOTPDS9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یک ترامپِ بدون موبایل | قرنطینه دیجیتال تیم ترامپ در سفر به چین
🔹
همزمان با ورود دونالد ترامپ به پکن مقام‌های آمریکایی تحت تدابیر امنیتی کم‌سابقه‌ای قرار گرفته‌اند؛ وضعیتی که برخی آن را «قرنطینه دیجیتال» توصیف می‌کنند.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3214792</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/akhbarefori/652278" target="_blank">📅 16:11 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652277">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30a27ad55f.mp4?token=MmzOxrpX9_iB-QAdBCLhvsDqIjuSO8_2LtRTH_1EuPP2Kq8PPLh-3kaPWidx1OeT8aSpIAVUd3wtQvb_leXL4rAf15a2cim9YCmu9OHld2Wfj6qRMal-wYNUxhtxdGIMlkYZBOAHqz3FzANhkVyhrLdg7E-YUDhYd9jf2DkKwejQu_4axmOMchdaoxWBA6OcOVMziWoPPCM1g32jIeO_PEhVC_o_lZAFRjZ-s8Kuo1XiqjXaUDFz7DAhaA_3jMatUvq9-Cv_AZKmnwoRu8EezVCVGZSblyQQFV5jYFrg8lMOlwdvytGs83hYQh8fLdBnxJxhMOaifNKEZBrvs11xB3Dm8Kzq9ndqEKFhgHkbpGGxEki9lue9KtuSuUrldVGPR32k6lruDP45ZGmighkQHWPf31XyaNb4BVxCpgS5bg3xFFXBXU17yI9DIpf3GbjEx1-DnPKXEHKnaXyJNcDPxHQ-oR9GwCPgVpQdzHM5Y-f02OVKSGW7_35qDs93TFiR-hD0fkhWV-yQYf_a7bE9BG2ti7xiaoeMB-gDBDS-wUpEWutIaQ_8EPcmgRtL3tUfzR7jGqC7AvRaBES7cFSFKEGzGbxZrN085EP4mmsRr1DxRbxwHs5b-Ns7qiPkduEtn3Z7UwfJ0e4UF6O2Gs1_QbjCHmBMaMwqt4bpD44raSU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30a27ad55f.mp4?token=MmzOxrpX9_iB-QAdBCLhvsDqIjuSO8_2LtRTH_1EuPP2Kq8PPLh-3kaPWidx1OeT8aSpIAVUd3wtQvb_leXL4rAf15a2cim9YCmu9OHld2Wfj6qRMal-wYNUxhtxdGIMlkYZBOAHqz3FzANhkVyhrLdg7E-YUDhYd9jf2DkKwejQu_4axmOMchdaoxWBA6OcOVMziWoPPCM1g32jIeO_PEhVC_o_lZAFRjZ-s8Kuo1XiqjXaUDFz7DAhaA_3jMatUvq9-Cv_AZKmnwoRu8EezVCVGZSblyQQFV5jYFrg8lMOlwdvytGs83hYQh8fLdBnxJxhMOaifNKEZBrvs11xB3Dm8Kzq9ndqEKFhgHkbpGGxEki9lue9KtuSuUrldVGPR32k6lruDP45ZGmighkQHWPf31XyaNb4BVxCpgS5bg3xFFXBXU17yI9DIpf3GbjEx1-DnPKXEHKnaXyJNcDPxHQ-oR9GwCPgVpQdzHM5Y-f02OVKSGW7_35qDs93TFiR-hD0fkhWV-yQYf_a7bE9BG2ti7xiaoeMB-gDBDS-wUpEWutIaQ_8EPcmgRtL3tUfzR7jGqC7AvRaBES7cFSFKEGzGbxZrN085EP4mmsRr1DxRbxwHs5b-Ns7qiPkduEtn3Z7UwfJ0e4UF6O2Gs1_QbjCHmBMaMwqt4bpD44raSU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیام ایرانیان وطن دوست مقیم نروژ به مردم داخل کشور
🔹
گفت‌وگو اختصاصی خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/akhbarefori/652277" target="_blank">📅 16:09 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652276">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
وزیر امور خارجه آمریکا، در گفتگویی با ان‌بی‌سی نیوز ادعا کرد که ترامپ در جریان نشست با شی جین پینگ، رئیس‌جمهور چین، مسئله جنگ با ایران و محاصره تنگه هرمز را مطرح کرد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/akhbarefori/652276" target="_blank">📅 15:50 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652275">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
رسانه‌های رژیم صهیونیستی از وقوع حادثه امنیتی سخت در مرز لبنان و زخمی شدن دست‌کم سه نفر خبر دادند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/akhbarefori/652275" target="_blank">📅 15:29 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652274">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n2xkwAKwG6WbAFXgDlwkQ7hcXTY6K64UCvJx_Vyz70WEdmM8JNwaFXsG-2MVxkA8q0Qgy3fa-jKwvzVxtRreSKGyMXsBEQMAm5tzV9CgrN2-AqxCL5QF1WfX-nWdTjGWq7db46qKgqdtGqeh9XeM3vO3ebgoZ3jlJuMJeu20jR2x0tt__NNTAF85tqeg-U_8qgJMkjLEgv1Dt0wMUZEHL2FE_MC40C9Jk8DIQOLwNOTFCiRjlTTDTDLXq1iJy9ETGsjJLcMVE-lrPXuWDBT8e8epHqMXLrBneC2AL7zk-c_0h3O-XHbduhFTgP7au1FwD4V0fXbrLLo7izDbMvkTpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آتلانتیک: ترامپ برای یافتن راهی جهت خروج از جنگ ایران به تقلا افتاده است
🔹
ترامپ در حالی که با فشار فزاینده‌ای برای پایان دادن به درگیری‌ها مواجه شده، اکنون به دنبال مسیری برای خروج از جنگ با ایران است؛ جنگی که منتقدان می‌گویند از اول هم بدون استراتژیِ خروج آغاز شده بود.
🔹
به گفته مقامات ارشد آمریکا، ترامپ به‌طور خصوصی از هزینه‌های فزاینده و پتانسیل یک درگیری گسترده‌تر ابراز ناامیدی کرده است. با این حال، هرگونه عقب‌نشینی نیز در این مقطع، به عنوان ضعف آمریکا تلقی خواهد شد.
🔹
کاخ سفید همچنان برای تعریف «پیروزی» در این جنگ پیچیده، با چالش جدی رو‌به‌روست.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/akhbarefori/652274" target="_blank">📅 15:03 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652273">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5fee3b23f.mp4?token=ZAwuvWm_yq3RT0B_-ncU21tRcwbEV0Xyq7E9d2Vclad9j47DtKPE3k-i-31nqu3k1IQs4I3IFzYriynMqzFoRgMfa1R0bTUMtRuDnk_EQmjjpvogntbVjg2WK2f2R6GoJyPyQxfwT3SEytxf6GJBLdqxp4oVPcI-wMNRSR9ELDeyhcVnuvCFDu-BPnnCRYEajG1iXiYzVWhy2dqRle6CKdHvxnz2FCHTc0gFCEsVcxP3ySiOsqHVPKLqb4C6FuFi7Mh0uAMPrGagQscyuHFNzV_U0947i1iHEGCTnIy93yiL0kC75bIaQ9JZpLjLey03pWoKs-GxamH_NrJTejsK1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5fee3b23f.mp4?token=ZAwuvWm_yq3RT0B_-ncU21tRcwbEV0Xyq7E9d2Vclad9j47DtKPE3k-i-31nqu3k1IQs4I3IFzYriynMqzFoRgMfa1R0bTUMtRuDnk_EQmjjpvogntbVjg2WK2f2R6GoJyPyQxfwT3SEytxf6GJBLdqxp4oVPcI-wMNRSR9ELDeyhcVnuvCFDu-BPnnCRYEajG1iXiYzVWhy2dqRle6CKdHvxnz2FCHTc0gFCEsVcxP3ySiOsqHVPKLqb4C6FuFi7Mh0uAMPrGagQscyuHFNzV_U0947i1iHEGCTnIy93yiL0kC75bIaQ9JZpLjLey03pWoKs-GxamH_NrJTejsK1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عارف: به هیچ قیمتی تنگۀ هرمز را از دست نخواهیم داد
🔹
اصلا تنگۀ هرمز مال ماست؛ ملک ما بوده حالا مدتی از ملکمان خوب استفاده نمی‌کردیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/akhbarefori/652273" target="_blank">📅 14:57 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652272">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
دو راه‌حل پیش‌رو برای موضوع بنزین
مصطفی نخعی، عضو کمیسیون انرژی مجلس در
#گفتگو
با خبرفوری:
🔹
هنوز تصمیم نهایی درباره تغییر سهمیه‌بندی بنزین گرفته نشده و سناریوهای مختلف در دولت در حال بررسی است. ایران پیش از جنگ نیز روزانه حدود ۲۰ میلیون لیتر کسری بنزین داشته که از طریق واردات جبران می‌شد.
🔹
درحال حاضر یا سهمیه باید کاهش یابد یا از ابزار قیمتی استفاده شود که حداقل مجلس چندان موافق این موضوع نیست. ذخایر بنزین ما نگران کننده نیست.
@TV_Fori</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/akhbarefori/652272" target="_blank">📅 14:55 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652270">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KxIbhS4VlCNa5ZTRVkL8RIUd0tYOK4PHcdz21e1U3gLazgissmc_fQkYwAbKg0585E03feTj4HfSMVG1rWjPXeSW44rllA164yLVZPzIgdZoRHh3W1wCRX7aP86VognjJE6bmucMdC3lsw9YGweuoUJXwh_2NwDbd66sGiODumGDvlPmr73uTWC68qWqP2-XCKKtQu5mEiho0EGcKJ1TjbF26x1J7EVdZ1WmKxNFVIo5cMYpkojaSsPYMNq6no5ZTWpALrVVlnEwksapUSbJg3lLlsLtEFZgQmVH5cGz5Hx2qR85JfpldHPCNPf_A68RBsku6szuOru6dWX0m1zRYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سانسور تصویر زن ایرانی در رسانه‌های بین‌المللی؛ تصویری که شاید به نفع آن‌ها نیست!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/akhbarefori/652270" target="_blank">📅 14:31 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652269">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c38ac5d731.mp4?token=Nb9EhxYbuE5Blzbi4xWsPdKfPY9xQ0trIe7BlgQt8uUzkz_pb9FkYf8tAtXn2po637dYsPADnjy15nqcFDytobn7QI0BZrm4ak1lFgrdrcFARBpBtg9qY_RYpKovDY-GM-3Bfc-o_BTvw7ECW4jTI1HEr4MPwTpcNzc-UnWdOxBtXazrWjhI-msBz-iF2E2BFeH_XZq8WQlC8GgzrpFl22a9sM7EdVzYk6zPL_VPe5raC0wmW2juHkuq6zANN_79WGahuHiUP3m_i6uUXPv7uXwuqUvopP9lqpSqOp4eCw8q7dqHfmYNbvc7Fu9iX5GB_GmZn3XlaYpPmLzRTvE0Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c38ac5d731.mp4?token=Nb9EhxYbuE5Blzbi4xWsPdKfPY9xQ0trIe7BlgQt8uUzkz_pb9FkYf8tAtXn2po637dYsPADnjy15nqcFDytobn7QI0BZrm4ak1lFgrdrcFARBpBtg9qY_RYpKovDY-GM-3Bfc-o_BTvw7ECW4jTI1HEr4MPwTpcNzc-UnWdOxBtXazrWjhI-msBz-iF2E2BFeH_XZq8WQlC8GgzrpFl22a9sM7EdVzYk6zPL_VPe5raC0wmW2juHkuq6zANN_79WGahuHiUP3m_i6uUXPv7uXwuqUvopP9lqpSqOp4eCw8q7dqHfmYNbvc7Fu9iX5GB_GmZn3XlaYpPmLzRTvE0Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خسوف اقتصادی برای دنیا با بسته شدن تنگۀ هرمز
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/akhbarefori/652269" target="_blank">📅 14:19 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652268">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bcc3a2430.mp4?token=CHHgLC6fUoIp1kXPexrUmnitPyemk1V0w9uhZ31GySvNJU7ng6ZmZmEZzJwYZdOpLDjvnthjd7sRS7si8vWd9hO0tR-F-p8UzLd6CJSyTVhtaJwCFkrHzbWdphJ7b26EZYg6rswsgmM6H0W-tF7GADBECYbDrdxZgkIiHSX3bo29jD6yuv8iQ64-RRsCA3CXz8De4m923Hm4whOjdjcXlv-73-Ml1AmltAw5jqYBStxUtPvu-5YjSJ8gCAtaK9xZcAgpZ9V_OQvOxZ-xyXQA2-iyAnvqB2CMZC57gkqy5HU3gCY8cHOJrb6mJb41iYOe-3k0wJvAJR9FHVi04uNmMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bcc3a2430.mp4?token=CHHgLC6fUoIp1kXPexrUmnitPyemk1V0w9uhZ31GySvNJU7ng6ZmZmEZzJwYZdOpLDjvnthjd7sRS7si8vWd9hO0tR-F-p8UzLd6CJSyTVhtaJwCFkrHzbWdphJ7b26EZYg6rswsgmM6H0W-tF7GADBECYbDrdxZgkIiHSX3bo29jD6yuv8iQ64-RRsCA3CXz8De4m923Hm4whOjdjcXlv-73-Ml1AmltAw5jqYBStxUtPvu-5YjSJ8gCAtaK9xZcAgpZ9V_OQvOxZ-xyXQA2-iyAnvqB2CMZC57gkqy5HU3gCY8cHOJrb6mJb41iYOe-3k0wJvAJR9FHVi04uNmMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس کمیسیون جوانی جمعیت مجلس: وام ازدواج بعد از قانون جوانی جمعیت ۱۰ برابر شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/akhbarefori/652268" target="_blank">📅 14:00 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652267">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k58fAw1UR5FbTf3Yijj-NVHk3GRJajwrw15KSrW7tyhx73cHwn7CePNVwXj5hUITjnHigy8bdvPaToepjp0qz1dsTBohIUfqJwXdD5yeEveywZR8M26HWC7a2OU8bJCGZ5B-Vbs8WY5pQykxicWmcDVZM-1NZR80E0xoRExHcLW6TuU64k2854h262RcPzFKMSpgGDVW9NsIIh5RT6IZNz_J6mAtpPJwvW1qSbhfMoI9AALJfQDCki7EvmsTYI3QopUlW1FtzP-kq2jsrTO8hXPKgYhcvF9UM5kbJmaMzltEsbXzvXeskIqy0Ag6Bm4248n1ZWG79pVWhxYFKwxJIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کره‌جنوبی: به ایران حمله دیپلماتیک می‌کنیم!
کره‌تایمز:
🔹
یک مقام ارشد دولت کره مدعی شد که ایران به طور قطع پشت حمله به کشتی باری کره‌ای HMM Namu در تنگه هرمز است.
🔹
او تاکید کرد تحقیقات هنوز در حال انجام است و قول داد که پس از تأیید، «حمله دیپلماتیک» علیه مسئولان انجام شود. در آن زمان هیچ دزد دریایی در منطقه فعالیت نمی‌کرد، اگرچه تحقیقات هنوز قطعی نیست، اما بر اساس عقل سلیم، بعید است که هیچ بازیگری غیر از ایران مسئول این حمله باشد./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/akhbarefori/652267" target="_blank">📅 13:56 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652266">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94b74446bc.mp4?token=jcUhzEwhKtNLQn384a77DjcRyIciqlv_ccI1ETosfB1eDojyTOPan_2PeJbMH6Rkh76mQfoAuLtWCIhGYBw07MUWXN0rvSWIyV8kOgt51crjdFxojvChVCuWsRTXno_e2EoLT6ppIUE5RZpQ3h1w7fZGWjtnk0p91MdMg9WTNaB_xgcCJLcoAwPcdcakN1ZIWJj60G6Q1JutZ8QZh6N3KZ3w5xr7dFgusG0HXsg673U3lt31g3LeHDdm0_nZYJ9z4KP3bjBx29iu0R2Bal2uTpo0LS4kGJNCp0aXS6WfMv_hhXJhxCNdUtcTsI6eWnSnyK3Qrvkdh6km4YJ2lVfq2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94b74446bc.mp4?token=jcUhzEwhKtNLQn384a77DjcRyIciqlv_ccI1ETosfB1eDojyTOPan_2PeJbMH6Rkh76mQfoAuLtWCIhGYBw07MUWXN0rvSWIyV8kOgt51crjdFxojvChVCuWsRTXno_e2EoLT6ppIUE5RZpQ3h1w7fZGWjtnk0p91MdMg9WTNaB_xgcCJLcoAwPcdcakN1ZIWJj60G6Q1JutZ8QZh6N3KZ3w5xr7dFgusG0HXsg673U3lt31g3LeHDdm0_nZYJ9z4KP3bjBx29iu0R2Bal2uTpo0LS4kGJNCp0aXS6WfMv_hhXJhxCNdUtcTsI6eWnSnyK3Qrvkdh6km4YJ2lVfq2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قصه پیرمردی که از دیرباز در کارهای جهادی بوده
@TV_Fori</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/akhbarefori/652266" target="_blank">📅 13:50 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652265">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mAfaRzb9Ko8Wju1tJT2WPImeQbQ5LVM3I88xb2jHFV21YE_JS0Je4CJWkI7J7ljInJBKRO5MMiSGZIaSjE9sXO4CXUv5n6U6OiFsRM3sOq2J9YQUl6bEBENGhtXqm_SMk44ktuNrouai8wLyRLYws00hEjg6_HpnjFpsG9FA9qZ4xnosIicD_-455b0CjMcn4SmgtcXecQUUEdyWApxy_JPZx9cscVk4e9bDDDz-oxLWYo6PdyWKlbd7c9py2QonKRLRTrFidnOqE2pwsaZEAsJ-BTVxuZPj9jN4Sxubatt_tabKWHgBmr_fvawU-iSEqj9yFU_TW3oxB0Lgv_KZ_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
باقری: هدف آمریکا از حمله به ایران، ضربه به هم‌گرایی آسیا بود
🔹
معاون دبیر شورای‌عالی امنیت ملی در نشست دبیران شورای امنیت ملی کشورهای عضو شانگهای: شخصیتی که امروز می‌بایست در چنین جایگاهی از طرف ایران قرار می‌گرفت و به گفت‌وگو می‌پرداخت برادرم آقای علی لاریجانی بود که ترور شدند.
🔹
در طول چهل روز تجاوز بی‌وقفه، شاهد ارتکاب جنایات وحشیانه‌ای از جمله ترور مقامات نظامی و کشوری، حمله به تاسیسات هسته‌ای صلح‌آمیز، زیرساخت‌های صنعتی، آموزشی و بهداشتی بودیم.
🔹
دقیقا هدف آن جنگ ضربه به همین هم‌گرایی آسیایی بود. جنگ با ایران آغاز حمله به جنوب جهانی است. این جنگ برای توسعه‌طلبی و اصالتا امپریالیستی است تا با ایجاد حوزه نفوذ و تسلط مطلق بر منابع انرژی خلیج فارس مانع از رشد آسیا و ظهور قدرت‌های میانی شود.
🔹
لذا این جنگ اگرچه با ایران شروع شد اما محدود به ایران نیست و در صورت انفعال و بی‌عملی در برابر آن، تسری و گسترش می‌یابد. هرگونه پاسخ ضعیف، دعوت به جنگ بیشتر است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/akhbarefori/652265" target="_blank">📅 13:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652264">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NPAB7mhXNIfuSLpX3TIjIMnM5pmE31W3WHlEijXoedYeMswTRn_quP4Q2jxuYH97tVYFgsgLrEJ-tNJ9x4FCXAGESVZ3C9zvGUVCbScDuxcNpsKYGfbvyCs3AkUg0XvTwAGRHZoe4HkQRYWkxvQIcw71ydKGODcAxiAvdaAL6EFHTs3iCsPiAOTdH7YLtoUWORf9uNANcjeJhvDq8pt5K9sQzjVmrS9SaBHCDadfk-Doj48chIs7KeZzVWiIOWwGKgmjFRROwTTyLXyGswdjVfbqd4Fl3TnuOm3GuuyBiTpcBx7DI7rsoTO5Mzrv8Jyrmyr12XVnBvMebTpgIVvNPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اسرائیل هیوم: در حالی که توجه‌ها به سمت ایران معطوف شده، حماس بی سر و صدا در حال تسلیح مجدد خود است
🔹
گزارش‌های میدانی حاکی از آن است که این سازمان با سرعتی نگران‌کننده در حال ترمیم تونل‌های تهاجمی و خطوط تولید راکت‌های خود است که در درگیری‌های پیشین آسیب دیده بودند.
🔹
منابع اطلاعاتی هشدار می‌دهند که مسیرهای واردات از طریق مرزهای جنوبی دوباره فعال شده و قطعات الکترونیکی پیشرفته برای بهبود دقت موشک‌ها به دست حماس می‌رسد.
🔹
علاوه بر تقویت سخت‌افزاری، این گروه در حال آموزش نیروهای ویژه جدید برای انجام عملیات‌های نفوذی پیچیده است.
🔹
تمرکز بر توسعه یگان‌های پهپادی و دریایی نیز بخشی از استراتژی جدید حماس برای ایجاد تنوع در جبهه‌های نبرد علیه اسرائیل و منافع آمریکا در منطقه است که به شکلی مخفیانه در حال پیشرفت است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/akhbarefori/652264" target="_blank">📅 13:32 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652263">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E7LqBHqR4vh47S4q97IJzYqAoorP8aIJu8Q3HWk0j3KMau0zDlFLRDMcQZOnapEDGRYxso1geWf-TalloDuDDuszMpn3H0UHzE_t3APJuLrJz0xIku6TMkuScux9gP3lJPt3LBnOrLIBYiAcoyYOiNxlY3dBRtvjYNABTOGhGjBA3vUgBTjmfuFP_K0pVPqFIrywg7syyII3aj93Q60OzQWidizn0ecOifKAGBnp5MUGH_WJV07NZ42fmmaQyIXxs7wKYqgonIwK3TOKf5ZXGLF_78CvjpXXJHIb_khuwz_EQQibLZcCki0RSttHCQtNP5dx1inYY04GPGnvxTtxfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میزان بارندگی در نقاط مختلف کشور
🔹
طبق داده‌های رسمی، از مهر ۱۴۰۴ تا پایان فروردین ۱۴۰۵ نشان می‌دهد که در سال آبی جاری بارش‌ها نسبت به بلند مدت ۲ درصد و نسبت به سال گذشته ۵۸ درصد رشد داشته است.
🔹
نکته جالب اینجاست که بخش‌های جنوب و جنوبی غربی با میانگین بارش ۳۱۶.۵ میلیمتر بیشترین بارندگی را داشتند. نواحی شرق و بخش‌های از جنوب شرق هم با ۹۴.۹ میلیمتر کمترین بارندگی را تجربه کردند.
@TV_Fori</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/akhbarefori/652263" target="_blank">📅 13:14 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652262">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RDnuQw4wHAFzDXbxrzqXfNYVOu9eVviG0fGwRYbMT3z12ejhWoHHyFo40Du8Qa20cO5j_Ec2-Fu15R2tqSqUndJRu1KP8KsRQveWJiI6BpjHX2GQAPeftJ8tynpv60vlX8YGU4XYVSo9owEyEgHDCbqPiVeb4irgu76V5nvcvJRACH-TKqymgdltIBEmFkH0qM8am91cjMsCwiQknwRR3_jbBaGqReQH53okaTSmpcJbcPjm2pdYX2VFmO9CE7V1Skipxh3i0ZPU5ii4ZrCFJU1jyEHQ4B05E5UHtAAG7Kdj42eEBl9a7-L6d8ty1gjDZr3Th9ts9L5zWYSY359SVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زمین نفس کم آورده...
🔹
پلاستیک و آلودگی همان لوله‌هایی هستند که راه تنفسش را بسته‌اند. وقت درمان همین حالاست، نه فردا.  شما هم به کمپین #نه_به_پلاستیک بپیوندید و تصاویر مربوط به این کمپین را برای ما ارسال کنید
👇
@Na_be_pelastic #نه_به_پلاستیک</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/akhbarefori/652262" target="_blank">📅 13:10 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652261">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
واشینگتن پست: ارزیابی اطلاعاتی محرمانه آمریکا نشان می‌دهد که جنگ ایران برای چین در جبهه‌های دیپلماتیک، نظامی، اقتصادی و اطلاعاتی مزیت‌های استراتژیکی برابر آمریکا ایجاد کرده است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/akhbarefori/652261" target="_blank">📅 13:10 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652260">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
عراقچی: امارات مستقیماً در اقدام تجاوزکارانه علیه کشور من دخیل بود
🔹
سیدعباس عراقچی وزیر امور خارجه امروز در نشست وزرای خارجه بریکس در دهلی‌نو در پاسخ به ادعاهای بی‌اساس نماینده امارات در این نشست طی اظهاراتی بیان کرد: من در سخنرانی‌ خود نام امارات متحده عربی را ذکر نکردم، به خاطر حفظ وحدت و ترجیح دادم به آن اشاره نکنم.
🔹
اما در واقع باید بگویم که امارات مستقیماً در اقدام تجاوزکارانه علیه کشور من دخیل بود. زمانی که این تجاوز آغاز شد، آنها حتی از محکوم کردن آن خودداری کردند.
🔹
آن ها حتی حمله وحشیانه به مدرسه را در همان روز نخست تجاوز محکوم نکردند.
🔹
نماینده امارات درباره حقوق بین‌الملل صحبت می‌کند، اما لطفاً به من بگویید کدام بخش از حقوق بین‌الملل اجازه می‌دهد از یک اقدام تجاوزکارانه بی‌دلیل و بدون تحریک قبلی حمایت کنید؟ همه می‌دانند که ما در میانه مذاکرات بودیم که آمریکایی‌ها و اسرائیلی‌ها تصمیم گرفتند به ما حمله کنند و ما شگفت‌زده شدیم که برادران ما در امارات تصمیم گرفتند فعالانه به متجاوزان بپیوندند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/akhbarefori/652260" target="_blank">📅 13:01 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652259">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rhT4RMRwN8Flr55opFdUk3cmZt6TmIJpXJyIp63LAjIvKxztAT8mHGTC4MVS8nsqdwdrdVH1nu1I7eUxcf9TJyPGX6XfJ5Bb1gWh4hnY6wd5U28ZSWjYnGY7h7byQeYG4Y16VmlVZJ5dEtw6s-61mOna3uamuxK-b30wbLKRW6E237AI3210rq0BIJlc-50IGfzzl4CD29Dba9EJof1ZNCbDVfcbWaFyKz7QZSCXvaauMlzL0hgjp8pFpS0WB2JkUu-VIt-_BpZKznF4Y7ECI0iqHDKfWfYWazX1XtCHumTukYgVBKvz1jMsR9Ocw-ELO-YsKJjU91nqeZv_EbpPpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عراقچی خطاب به امارات: ائتلاف با اسرائیل هم از شما محافظت نکرد
🔹
وزیر امور خارجه امروز در نشست وزرای خارجه بریکس در دهلی‌نو در پاسخ به ادعاهای بی‌اساس نماینده امارات گفت: ائتلاف شما با اسرائیلی‌ها نیز از شما محافظت نکرد و در سیاست خود در قبال ایران بازنگری کنید.
🔹
سیدعباس عراقچی افزود: من در سخنرانی‌ خود نام امارات متحده عربی را ذکر نکردم، به خاطر حفظ وحدت و ترجیح دادم به آن اشاره نکنم. اما در واقع باید بگویم که امارات مستقیماً در اقدام تجاوزکارانه علیه کشور من دخیل بود. زمانی که این تجاوز آغاز شد، آنها حتی از محکوم کردن آن خودداری کردند.
🔹
وی ادامه داد: آنها اجازه دادند از سرزمین‌شان برای شلیک توپخانه و تجهیزات علیه ما استفاده شود. همین دیروز فاش شد که نتانیاهو در زمان جنگ به امارات و ابوظبی سفر کرده بود. همچنین آشکار شد که آنها در این حملات مشارکت داشته‌اند و شاید حتی مستقیماً علیه ما اقدام کرده باشند. بنابراین امارات شریک فعال این تجاوز است و هیچ تردیدی در این باره وجود ندارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/akhbarefori/652259" target="_blank">📅 12:53 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652258">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
پزشکیان: هدف قرار دادن اماکن ورزشی نشان‌دهنده دشمنی با عزت و سربلندی ملت ایران است
🔹
رئیس جمهور در بازدید از آثار حملات و خسارات به مجموعه ورزشی آزادی: دشمنان از هر نماد امید، انسجام و افتخار ملت ایران هراس دارند. تسریع در روند بازسازی، احیای کامل زیرساخت‌های آسیب‌دیده و حمایت همه‌جانبه از فضاهای ورزشی کشور ضروری است. چنین مجموعه های ورزشی بخشی از حافظه تاریخی، هویت ملی و نماد تلاش، امید و افتخار جوانان این سرزمین هستند. دشمنان ملت ایران، نه‌تنها با توان دفاعی و پیشرفت علمی کشور، بلکه با هر نماد عزت، نشاط، همبستگی و سربلندی ملت ایران دشمنی دارند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/akhbarefori/652258" target="_blank">📅 12:50 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652257">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BvbKji7KUt8Jvs6J1-4oOrrHqCbgdF6GG0yx7htRE5y4p5ifjVM___WYoYGxDHEPWtPsN-KImC_MIQmd9G0aYc-Vk5vAzFg_fyT-5wRCp00PXr0oWRYya3QljPQB7SkFg4C5IYmAyYnFIoDPkahPwZitJTWiXZDRxiUxLbZ5HvZDPBwxa-_0tBzTzyvTvfI3hAHuBOgW9MLXP4A0z0hITbA7V-Td5rVpDAIobnvM3sALwQxbRL33gEUXAmEo5QagNsnhZHoDDl4nMLcOkIXWybCop6N9cbCYP8wrDlAP8FqeTjB2RXvapDwOfpbgH88Zy4Q3cG9NT1mYurLEw_n5_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فایننشال تایمز: بستن هرمز باعث افزایش هزینه‌ مصالح شده و پروژه‌های ساختمانی را در جهان متوقف کرده است
🔹
طرح‌های عمرانی در جهان به دلیل کمبود مشتقات نفتی با تأخیرهای جدی روبرو شده‌اند. قیمت موادی چون قیر، عایق‌ها، لوله‌های PVC، رنگ و تجهیزات گرمایشی هم رو به افزایش است.
🔹
در ژاپن، شرکت‌های ساختمانی از تأخیر در ۲۵ درصد پروژه‌های خود خبر می‌دهند، نبود حتی یک قطعه یا چسب خاص کافی‌ است تا کل یک پروژه عمرانی متوقف شود.
🔹
در هند، بزرگترین سازندگان املاک از افزایش ۵ درصدی هزینه‌های ساخت از ابتدای جنگ علیه ایران خبر داده‌اند.
🔹
در استرالیا، افزایش هزینه‌ها تا ۵۰ هزار دلارِ استرالیا به قیمت ساخت هر خانه جدید افزوده و تعهد دولت برای ساخت ۱.۲ میلیون مسکن تا سال ۲۰۲۹ را با خطر جدی روبرو کرده است.
🔹
در انگلیس، پیمانکاران با افزایش قیمت ۱۰ تا ۳۰ درصدی طی سه ماه آینده روبه‌رو هستند و کارشناسان نسبت به موج ورشکستگی شرکت‌های ساختمانی در سال آینده هشدار می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/akhbarefori/652257" target="_blank">📅 12:32 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652256">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Eshghe Bi Karan</div>
  <div class="tg-doc-extra">Parvaz Homay</div>
</div>
<a href="https://t.me/akhbarefori/652256" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سرود رسمی تیم ملی فوتبال ایران برای جام جهانی با صدای پرواز همای منتشر شد.
در مراسم بدرقه تیم فوتبال ایران برای جام جهانی از قطعه موسیقی "عشق بی کران" با صدای پرواز همای  تولید مرکز هنری رسانه ای نهضت با مشارکت فدراسیون فوتبال برای نخستین بار در میدان انقلاب و حضور گسترده مردم رونمایی شد.
@Akhbarefori</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/akhbarefori/652256" target="_blank">📅 12:32 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652255">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
قوه قضاییه: توقیف کشتی‌های متخلف آمریکا طبق قوانین بین‌المللی است
🔹
سخنگوی قوه قضائیه با انتشار متنی در فضای مجازی به روند توقیف حقوقی و قضایی نفت کش های متخلف آمریکایی در آب های ساحلی متعلق به کشورمان پرداخت و در همین رابطه به راهزنی های دریایی ارتش تروریستی آمریکا و زیر پا نهادن همه قواعد حقوقی بین المللی در این دزدی ها اشاره کرد و نوشت: رئیس‌جمهور آمریکا صریحاً به دزدی دریایی اعتراف و حتی مباهات کرده است.
🔹
جهانگیر: توقیف کشتی های متخلف آمریکایی با حکم دادگاه صالحه و مستند به قوانین داخلی و بین المللی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/akhbarefori/652255" target="_blank">📅 12:28 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652254">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
یارانه اردیبهشت دهک‌های یک تا ۳ واریز شد
🔹
سازمان هدفمندسازی یارانه‌ها: یارانه مرحله ۱۸۳ مربوط به اردیبهشت ماه سال جاری به مبلغ ۱۱۱ هزار و ۶۶۸ میلیارد ريال به‌حساب ۱۰ میلیون ۲۳۰ هزار و ۶۸۱ سرپرست خانوار دهک‌های اول تا سوم در سراسر کشور واریز شد و قابل برداشت است.
🔹
بر اساس دهک‌بندی اعلام شده از سوی وزارت تعاون، کار و رفاه اجتماعی ۲۷ میلیون و ۹۱۷ هزار و ۲۶۹ نفر در دهک‌های اول تا سوم قرار دارند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/akhbarefori/652254" target="_blank">📅 12:20 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652251">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XOqu-vU2I0rht-dSUPVwKtoFriajVVEpnYsjdkhpeFTQOAvInd1dHfIP6fLYwnZsgQ6RbFJxTXAloQPq7lCsBEPiKhZdoPiVWrQeXRrDsky81IoFBJ3dis8pFZbuo5gsXrawyMN4BG317aFLJzty9cdwXD3DwzsIYnxrTTdQKfVDzoHfKKHLPHwFJ6idMoks577FF-QdKZE_ZGQSNUMVZ8DecnhGZVDGrFGlJPOtb2J67FjhyhUelDlSEvI2C91JT_ErYm4RlKSr_ivHegeyM1SXfiD7-iJfreLWkRvaIlzihgedsyB_-zgEQsy-C_XtAN_awOcP0q2w3F_1GkYP-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YF_KhMWCfBNkDIl2Y9FeuzS908Ddv5Flg5JPoymBT1YPPIxZzVbTnoLB654k20fs-fdzqb1LDo_nG7Y1Wt2IX04m-LzsOJMrWo_AayusfKAmP0U3V0urW58H9MRZeUDPll9BxPp48wHqwTh5JHEPKOPwWSuEcbmImWo2iVS0FIgG7phMqMfWvHe7QxtN5HcXjiRWmy1CD3X7eCrfoF_xkhU65GMISrKZ1Vdw0voyVdTVe8kbfu7149CIJMI6AgmH5Dhlu47Bd0opY9tcX_hAorAjtu89ojqkIytwb_ARc4RHny-2AcDbP9CcNxIZ_GX-XsWrOZv5ygFDZMt6utecyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y6Ju-QBF9WOdnDQvDuTdc9bs46B-yrn-Qd454ni_va1GFV8uAxV1jB1HDpnHsmic520Eu4qoM5B-RSwCVT_bMNtPbJiIqPE2tfz-l7kc9pMkNQJ7ryJvHC_aeVK0nsKj0OoWnWFHt_zRDXgI0ylfyyqfKo2QZqvwz4hDX2CyGFJA3Vk0gef6YW0mHYoCUFxeIL4tU2s3SvPUyKZn6LIY5mFt_Rx7U1tHyWS73vxO302azF7XxcdaRAXVl4f_t98eVePgAWbe2pFZnwMJJDswDuu59h97uF8aHz0-4sm9N4hFXhbOkJqPM-f3EX2fBqvS8fKqMzrdi0XTtVkLhjNwsg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
بازدید رئیس‌جمهور از آثار حملات و خسارات وارده به مجموعۀ ۱۲ هزار نفری آزادی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/akhbarefori/652251" target="_blank">📅 12:06 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652250">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JTWz8GWcOkMKaD9lkyEDfXWcocTJE3ubIUVnHYuLcR2lbKb4PJQt8PcDXCxTuc7InFbTDlonlyduDe3xZy0zlKsLrnWaymqQgU9gJGhe6eyuQ7VLI0tvQGPuL-gbzKqyVrelAy5idVpg4kp3t2KOGuuc87pYZBiNe0PPJ3TzbLSPX4XGQNfpL2HrmiTmW4Y90YHfc20tIwIxcZqo-rh3RcDlIXbziScJMZN2KGY8hsAc0EEk545hKMji_HIy-6JcHsiro8iFI7mWbZD4L5gSv1CHk-i1kq4OhqPFaVtOn9RBy9m3pf4HHdt1-ugRI2e4flbqDjSTX_eTNsNotom74w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مجله آمریکایی نیشن: بحران هرمز با تمام بحران‌های نفتی دیگر متفاوت است
🔹
اسرائیل و آمریکا با حمله به ایران، ثبات خلیج‌فارس و عرضه جهانی نفت و گاز طبیعی را برای آینده‌ای غیر قابل پیش‌بینی‌ برهم زده‌اند.
🔹
این جنگ غیرقانونی بحرانی بی‌سابقه را رقم زده است. در حال حاضر، بسته شدن تنگه هرمز، روزانه ۱۱ تا ۱۳ درصد از نفت بازار جهانی را حذف کرده و باعث جهش قیمت سوخت شده است.
🔹
کشورهایی نظیر فیلیپین و بنگلادش به خاطر اتمام ذخایر سوخت، وضعیت اضطراری ملی اعلام کرده و با تعطیلی نیروگاه‌ها و فلج شدن سیستم حمل‌ونقل روبرو شده‌اند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/akhbarefori/652250" target="_blank">📅 12:00 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652249">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
۱۵ شهید و زخمی در حمله اشغالگران به غزه؛ هشدار درباره بحران‌های آوارگان
🔹
منابع بهداشتی غزه اعلام کردند که روز چهارشنبه در نقض‌ مداوم توافق آتش‌بس در نوار غزه یک فلسطینی شهید و ۱۴ نفر دیگر زخمی شدند.
🔹
مقام سازمان جهانی بهداشت نیز تاکید کرد که آوارگان در چادرها در میان آوارها زندگی می‌کنند و برای تأمین ابتدایی‌ترین نیازهای اساسی خود به کمک‌های بشردوستانه وابسته هستند.
🔹
با وجود برقراری آتش‌بس، «حملات هوایی، توپخانه‌ای و تیراندازی همچنان ادامه دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/akhbarefori/652249" target="_blank">📅 11:51 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652248">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b4b7048ea.mp4?token=UpDx-rOElOilR2QmTeowIa9OPIXADq7Aj00SGpYXTLzN5n9eb6RZyAaQzH4p5Oid33VoJcV8VOzplRw6oLh2uO-eaiP80iQAYryvhRplXJZzcFq-igB5253--QyYmLA_oE0FHslmHbfMl0U-fMxt0bDBBKL31-6wzPW_5XIbVwXAWQc1N7mQjDFFFdUxJsnPWTjukqpQcRF5ePFtgaGg18xhP6fDul9hYaDE2G0PhN7Mb-EHX92KmBhMt1JJT01KiBci4T1x4TMsaNBZ7kebfc3WwZepUbRnW1rfpYN3Q8lPXlUuQ4HsWBAYgdnKek6W7qJRxh2er9CK-GHxzmC-vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b4b7048ea.mp4?token=UpDx-rOElOilR2QmTeowIa9OPIXADq7Aj00SGpYXTLzN5n9eb6RZyAaQzH4p5Oid33VoJcV8VOzplRw6oLh2uO-eaiP80iQAYryvhRplXJZzcFq-igB5253--QyYmLA_oE0FHslmHbfMl0U-fMxt0bDBBKL31-6wzPW_5XIbVwXAWQc1N7mQjDFFFdUxJsnPWTjukqpQcRF5ePFtgaGg18xhP6fDul9hYaDE2G0PhN7Mb-EHX92KmBhMt1JJT01KiBci4T1x4TMsaNBZ7kebfc3WwZepUbRnW1rfpYN3Q8lPXlUuQ4HsWBAYgdnKek6W7qJRxh2er9CK-GHxzmC-vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی: تاریخ نشان داده است که امپراتوری‌های رو به افول به هر چیزی چنگ می‌زنند
🔹
وزیر امور خارجه در نشست بریکس: کشورهای دنیا باید این تجاوز آشکار را محکوم کنند. کشور‌ من در یک سال، دو بار مورد تجاوز آمریکا و رژیم صهیونسیتی قرار گرفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/akhbarefori/652248" target="_blank">📅 11:42 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652247">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GyrpqvOn73WWlSZwU_mdVarzKKJkymb9tm_RYy1VpJhC83XE3apJjrEc8B1nY838UW498L5lJN_Bdfqz5YHNicrzvMsGrnGiG-Yzq0dTBfp7dJY3vRKyP6vGobOywJ1xMnnPtupJGWDpiVUNFT8TR8LgPLima8k5NXQs43VYkOvsdISM3v6wKF8_YWE4LDd6iPmlZVtjs9YcO-obG_yc9rOfQ3acUzJ0BCPMM_AC0Wws68VZMoDZo5mk_IG6y9Wph0LveX9NuskxMeWMRlTEeFsDB5BeCu6rJ8QMWzQgGDWL5o6PgP7Va9xGA9d3DknyOOCL010pZdzgEqpw7gQ4Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جروزالم پست: حوثی‌ها [انصارالله] همچنان با استفاده از قطعات ایرانی جدید در موشک‌ها زرادخانه خود را توسعه می‌دهند
🔹
براساس گزارش مرکز تحقیقات تسلیحات درگیری (CAR) قطعات الکترونیکی به‌کار رفته در حملات اخیر در دو سال گذشته تولید شده‌ بودند؛ امری که نشان می‌دهد شبکه‌های تدارکاتی انتقال تجهیزات قوی و مداوم هستند و حوثی‌ها با سیستم‌های جدید تأمین می‌شوند.
🔹
موشک‌های ضدکشتی، زمین به هوا و بالستیک از جمله این سلاح‌ها هستند که نشان می‌دهد حوثی‌ها اکنون دارای طیف وسیعی از توانمندی‌های هجومی پیشرفته هستند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/akhbarefori/652247" target="_blank">📅 11:32 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652246">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c5cba69a2.mp4?token=g99VaY6HhlgwSZ5ZTXNuo-BwhCsVJdWN248Gw40hvARC9CZZYy4Rzvm_TGvZCTV6YfjyJEo_Fj-kJNMLENkJ5fHZoPONzWFrcaE-AA35UCcjNOZ24wy0FDxySoHYgNZN-7c8wrfhbH-1s-Rh4jWnwNs_tPpx7JMjYV6YIQGGJVMS-63GzH3JN3M5gjQTlAitLlWe9MWx73s_RS8Kwh71cVy2bK0q_CWSezbiW5TW7aApzEOcrCvsGEnTP6fUIL70tpAE504IJdPWT5gWbMwJwVPSj5yXlqMtEdX9mbpmfJ-fVapo7OLNs-INvf4inLkEfmUtAQeC8Cbd8VcKy2zMo4KXzCyqfx3INnRlLA6t0DoVcJdaOm7VUowEj8Hxiqm2Bl9gtbQMc74Eb8V60n--QX_9PqRalbYob5VEmLH6W2I_G0SxAEW58MvEpFO0fOO2JiXcdByx1C7hprqZeqzo3ovgSrMjXcjuiSjr0sOI8D800N8ayIM8i3G7R9-hJh72tTxOHPoog4tC7vdCh9aWovlQcBIgaKQivlasUlbk1C_1-aAaNlM85IxDcrdzfXJv8m8k0BHbL1cH0UhU4kNi2_RA2eOP91EhMyYUbXx9Q2FZAcF6ZRsvKc7IkdUhDwC6xuWHSRzNO7QcYCy2rA_xeZ96kFZY6NrvMbQAVWvVBHo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c5cba69a2.mp4?token=g99VaY6HhlgwSZ5ZTXNuo-BwhCsVJdWN248Gw40hvARC9CZZYy4Rzvm_TGvZCTV6YfjyJEo_Fj-kJNMLENkJ5fHZoPONzWFrcaE-AA35UCcjNOZ24wy0FDxySoHYgNZN-7c8wrfhbH-1s-Rh4jWnwNs_tPpx7JMjYV6YIQGGJVMS-63GzH3JN3M5gjQTlAitLlWe9MWx73s_RS8Kwh71cVy2bK0q_CWSezbiW5TW7aApzEOcrCvsGEnTP6fUIL70tpAE504IJdPWT5gWbMwJwVPSj5yXlqMtEdX9mbpmfJ-fVapo7OLNs-INvf4inLkEfmUtAQeC8Cbd8VcKy2zMo4KXzCyqfx3INnRlLA6t0DoVcJdaOm7VUowEj8Hxiqm2Bl9gtbQMc74Eb8V60n--QX_9PqRalbYob5VEmLH6W2I_G0SxAEW58MvEpFO0fOO2JiXcdByx1C7hprqZeqzo3ovgSrMjXcjuiSjr0sOI8D800N8ayIM8i3G7R9-hJh72tTxOHPoog4tC7vdCh9aWovlQcBIgaKQivlasUlbk1C_1-aAaNlM85IxDcrdzfXJv8m8k0BHbL1cH0UhU4kNi2_RA2eOP91EhMyYUbXx9Q2FZAcF6ZRsvKc7IkdUhDwC6xuWHSRzNO7QcYCy2rA_xeZ96kFZY6NrvMbQAVWvVBHo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
منوچهر متکی: آمریکا دو جنگ را باخت و سومی را هم قطعا می‌بازد/ گزینه ای جز مذاکره برای خاتمه جنگ ندارند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/akhbarefori/652246" target="_blank">📅 11:23 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652245">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IXh5hyqE4GZfcFbvf_RWyeif8yIplm-TLR8UqvP26yxGEFyFk6hy-pzvzD2jyTQBJJZ5qI3--m0PxLOxAdZ0l3N0Jp9Z9TnjmELOx3v4P7rhQr-DcfchC83xUiPt2KM2mJ8DhkblhILtrta-ZeBluArv9aYxzDNtaNd0UGIh9PRO6gkxERKrz2NXsYRnjzWABI6DMO1WsJUoJqI3EmStqW0hMbQQs4cPeZzAo-sEnSEKw6cUC6obsO0nxLJK32MfY68jPGOCcR7tOQQpInSGyCFE-NMZvnA4mGmQzQmLkZccS0v7RxUUhzzmGYMIDrspHGhao0qY2qrNMB1JxAVJPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دریادار سیاری: آمریکا در جنگ با ایران شکست خواهد خورد
🔹
آمریکا در جنگ با ایران به خاطر رشادت و ایستادگی غیورمردان نیروهای مسلح و پشتیبانی ملت همیشه در صحنه، با تمام تجهیزات و توانمندی پوشالی دفاعی‌اش شکست خواهد خورد و این در تاریخ ماندگار خواهد شد.
🔹
حضور مردم در تشییع جنازه شهدای ناو دنا، بسیار حماسی بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/akhbarefori/652245" target="_blank">📅 11:21 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652244">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FQzC-iszURC1BkCHPka4q553NqdI8D-1S8AlCT3Uhof5ThPJaAmDua3pYlJwACwljWrkCxUvNTvQNdttaIF4ySCJpyedA5Pt8qUMShemqF9mqc5Uaa4RKZA7ZiSlUVhm8juzHT4O56jKRJm2XFvPpKRRM222XnFeOEby5GlqVk_1J_zBjy8xptbh3zxbPApFbzkS11G0qaQeUKO0DrDB-WZoGRmOyG9q0LIDgeWRU4ZO1oioqvHtu-rRjW-M88SnEn9DES7vXRno-m95FFqtZS3VfiuUHY9G3U_vpLJxYrzqAi2x-iJMn6UGG4S5SD7ylK4hHSqWTmLzbLmAHcfgSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وقوع یک حادثه دریایی در نزدیکی فجیره امارات
🔹
منابع رسانه‌ی از وقوع یک حادثه دریایی و وقوع انفجار در پی حمله پهپادی به یک کشتی در سواحل فجیره امارات خبر دادند اما چیزی نگذشت که مرکز عملیات تجارت دریایی بریتانیا (UKMTO) اعلام کرد که گزارشی درباره یک حادثه در ۳۸ مایل دریایی شمال‌شرقی فجیره دریافت کرده است.
🔹
این سازمان ادعا کرد که این کشتی هنگامی که در حال پهلو گرفتن در الفجیره بود، مورد تصرف قرار گرفت و هم اکنون در حال حرکت به سمت آب‌های منطقه‌ای ایران است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/akhbarefori/652244" target="_blank">📅 11:07 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652243">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baacdf786a.mp4?token=pvXHj8WSPaWW5dvy9edyqeij3gVEBVmaJVKGh9BqKxR7tER4ZKXsMuDFVeYMUwrWve7TothoQuiSxfvN17cI0gIgPqPtaSFVHobVzHr3FAD0ZkwO5pub2ijSZ17ipyB9xKvHtADmbvhNWKCfj7EIvQaYJR6iRk8p3OflTlgfr-3JYlf0qPblUV0vJZkqpdyTqfvXwnDAYs1iXeO2j7NPDSY3PaZfuby-em7YoJoGps_cRR7VamCKu75gI6nNDUM3H2pRec0JSBVvZAsuEr5ByTv5rc-teA5BmG1nAKl2nSy4rx9pCoJnpWZc9Ky63JPd27Rlw3AjJVn6pgiy6HHxlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baacdf786a.mp4?token=pvXHj8WSPaWW5dvy9edyqeij3gVEBVmaJVKGh9BqKxR7tER4ZKXsMuDFVeYMUwrWve7TothoQuiSxfvN17cI0gIgPqPtaSFVHobVzHr3FAD0ZkwO5pub2ijSZ17ipyB9xKvHtADmbvhNWKCfj7EIvQaYJR6iRk8p3OflTlgfr-3JYlf0qPblUV0vJZkqpdyTqfvXwnDAYs1iXeO2j7NPDSY3PaZfuby-em7YoJoGps_cRR7VamCKu75gI6nNDUM3H2pRec0JSBVvZAsuEr5ByTv5rc-teA5BmG1nAKl2nSy4rx9pCoJnpWZc9Ky63JPd27Rlw3AjJVn6pgiy6HHxlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جعفر دهقان: بمباران مدرسۀ میناب توسط آمریکا قطعا عمدی بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/akhbarefori/652243" target="_blank">📅 11:02 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652242">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dy8OOefFItz3wtQcesVn--6Ij34Y7r-H7ktZrS5Eg1dbvlLZDSmmnYx2CClYMDCOJc9rj8QzVDyWlrLkvVfs7Jhz-wNmaLdWGEJyAs0dZmw0IJN1ZnqP6wW070zCad5apP9x419URni7RLAbr3qnKPOeteWtQR6hS5RAgXRvBITXbEnY-OC-YWWErjrKVr30WCXUES0oJDDVBobdpfNqte5fTKQf5AvHwWjRIBLhlsrC9a7jeHvFRIBSShX_E2i43Dnw5dYNH9Z1h8oMoftjZ20qQYLmdFVXasS9efe95dUlnz55Mn-Gv2UZptfN7X3mkCtMWwhgRabCoh7wtlvLgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شتاب عجیب اسرائیل برای بلعیدن جنوب سوریه
🔹
بیش از ۴۰ حمله در کمتر از یک ماه و افزایش پایگاه‌های نظامی اسرائیل به عدد ۱۰ در جنوب سوریه، در کنار نفوذ نرم میان دروزی‌ها، حاکی از شتاب عجیب اسرائیل برای بلعیدن جنوب سوریه و ریشه دوانیدن در آن است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/akhbarefori/652242" target="_blank">📅 10:58 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652241">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
منوچهر متکی: در پاسخ به گستاخی مقامات بحرین گفتم چنان می‌زنیم که نامتان فراموش شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/akhbarefori/652241" target="_blank">📅 10:39 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652240">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQH86Qbv9yMDmhDkPJJloml3CLHAYPMO5LYiT8fUL3M-7UMboAVjJPIqBYFWhM-pVVGtEPZiTQX4rYqr10Bjw778RLLwlUemjYU9mgRUyR630f9x9zj4XLFD4JuGk5UqJAyDzDwrP24J7rHRtVjY-6aj9cDVZwe7ZtRT0wjEcwQQ4JN-bAeXyhQiNJqdLwpYIcAkpln7tj4eu4IQNKcWskYMNFmJtHkHSxOMZRFO4UihMDEugVzJ_ftVJguO5v0quZcBVFwaNrmszQe-C8vdwninEq_tPOsFBFLH6ahKMJs3gS4egpgjTpp9go5I05u5pKXUYhxjMg9ScARemcnX-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
موجی از زباله، دریایی از درد
🔹
پلاستیک‌ها تجزیه نمی‌شوند، فقط خرد می‌شوند و وارد زنجیره غذایی ما می‌شوند. برای حفظ سلامت دریاها و خودمان، وقت آن است که جدی‌تر با پلاستیک خداحافظی کنیم.  شما هم به کمپین #نه_به_پلاستیک بپیوندید و تصاویر مربوط به این کمپین…</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/akhbarefori/652240" target="_blank">📅 10:36 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652239">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99e7e5c17c.mp4?token=s_IN1nwlh5-GntJveYGhT4ZXkSwawLMaoV59bP0S7mPKaHT5mIGUs2iMobSPFdtkq1V3RFLW1VDjNJBT6XWMbPYcpitDJdDuS-SjpYkxvclaf2yk8FXwvt5hVxXvWcbSRZDJKqjXyGaFNQhAq5Q1OxK5TToNruLRsVCdcf2w9M4W6MocMHN5CDFlQYFrlOqP7qwawWdBTUaxalvd0ixU6SIZl-I9_pOR2e8W_OR_p6nWUvXmiIialQOJv-QH-mneg4XZlc3aSWb-_Xs5nkf-nYW8V7KdKFoLXiBVdT5YpK5JmwnxYdGspS__7QtJSaoFPXyUHeq4AWtPJzRAKpFaJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99e7e5c17c.mp4?token=s_IN1nwlh5-GntJveYGhT4ZXkSwawLMaoV59bP0S7mPKaHT5mIGUs2iMobSPFdtkq1V3RFLW1VDjNJBT6XWMbPYcpitDJdDuS-SjpYkxvclaf2yk8FXwvt5hVxXvWcbSRZDJKqjXyGaFNQhAq5Q1OxK5TToNruLRsVCdcf2w9M4W6MocMHN5CDFlQYFrlOqP7qwawWdBTUaxalvd0ixU6SIZl-I9_pOR2e8W_OR_p6nWUvXmiIialQOJv-QH-mneg4XZlc3aSWb-_Xs5nkf-nYW8V7KdKFoLXiBVdT5YpK5JmwnxYdGspS__7QtJSaoFPXyUHeq4AWtPJzRAKpFaJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رییس سازمان هلال احمر: دشمن جنایتکار حتی بیمارستان هلال احمر دبی، که کار بشردوستانه انجام می‌دهد را تعطیل بیماران را به زور جابجا کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/akhbarefori/652239" target="_blank">📅 10:26 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652238">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ba92bad61.mp4?token=KbeIgvkN889J8MNb8m7IkO6tiEDY8cYk5fZyvdCdL87k3tIa7txeik5ohgfLt3I_Lb8IRG0kciM8U1JFZi4doBzkHjrKwWIfc9rzwx-GDP6NBuoSkf5wQNN1G0hBJUkBAmNyR1OK3Wndrm4RtRn_ZMN5teHGIZr85WssCCkbYPFhcbbg_X8B5dl4tzUa0UWCi33HGBAKDalYN3TYGvhAokxL0kagUu3sLGHydfjMhLdyl1FxXDXwFOkDEi7cLNIUuXCCgs3oOYPXLNtyJK76BH6MgB5y2PmSY9DmEDZZRbmcZPu00QNPzKjm6UiOpClNqxVwigfLp0mitzz1O1qy3YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ba92bad61.mp4?token=KbeIgvkN889J8MNb8m7IkO6tiEDY8cYk5fZyvdCdL87k3tIa7txeik5ohgfLt3I_Lb8IRG0kciM8U1JFZi4doBzkHjrKwWIfc9rzwx-GDP6NBuoSkf5wQNN1G0hBJUkBAmNyR1OK3Wndrm4RtRn_ZMN5teHGIZr85WssCCkbYPFhcbbg_X8B5dl4tzUa0UWCi33HGBAKDalYN3TYGvhAokxL0kagUu3sLGHydfjMhLdyl1FxXDXwFOkDEi7cLNIUuXCCgs3oOYPXLNtyJK76BH6MgB5y2PmSY9DmEDZZRbmcZPu00QNPzKjm6UiOpClNqxVwigfLp0mitzz1O1qy3YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جزئیات برگزاری امتحانات نهایی و کنکور
🔹
وزیر آموزش‌وپرورش: امتحانات نهایی ۲ هفته پس از عادی شدن شرایط و پایان جنگ برگزار خواهد شد، ضمن اینکه در استان‌ها تصمیم‌گیری دربارۀ نحوۀ برگزاری امتحانات برعهدۀ استانداران خواهد بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/akhbarefori/652238" target="_blank">📅 10:26 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652237">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7e782c88f.mp4?token=JU51pI1d_Sq_kXqKzavISXLH5Jo5EdVIZH6b5fhTIvnR-VeEYc67XR-tktZFOVT_RewsRjWsoQa3XW9TJWdyFMc_z9Rk6ibSocb_2UFMaOVNTsKtlWCYcHZBNeZAGroZDCyIXpI1YFO7VizMWl1EFOj_l8_pzZ_tlDxvGURftElx9QPRXyqXxfy3Aa1H24cHPy2idKatvYKhd1oP3w8DHXbi8rqmt-KSTBD15NtRONYANV2Y9rWEHDkTEWuF822qN2SWs7CRkaEGayEcxPN_yZW8HxXN6yvv1tFwIVAg25qIPKlVVbhdJm1r3kVntU43sX8QdvEWbxFMAgYfEG5Tkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7e782c88f.mp4?token=JU51pI1d_Sq_kXqKzavISXLH5Jo5EdVIZH6b5fhTIvnR-VeEYc67XR-tktZFOVT_RewsRjWsoQa3XW9TJWdyFMc_z9Rk6ibSocb_2UFMaOVNTsKtlWCYcHZBNeZAGroZDCyIXpI1YFO7VizMWl1EFOj_l8_pzZ_tlDxvGURftElx9QPRXyqXxfy3Aa1H24cHPy2idKatvYKhd1oP3w8DHXbi8rqmt-KSTBD15NtRONYANV2Y9rWEHDkTEWuF822qN2SWs7CRkaEGayEcxPN_yZW8HxXN6yvv1tFwIVAg25qIPKlVVbhdJm1r3kVntU43sX8QdvEWbxFMAgYfEG5Tkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی: ما هیچ مانعی در تنگه هرمز ایجاد نکرده‌ایم
🔹
وزیر امور خارجه : تنگه هرمز اکنون بیش از هر چیز از تجاوز آمریکا و محاصره‌ای که بر آن تحمیل کرده، آسیب می‌بیند.
🔹
از نظر ما، تنگه هرمز برای تمامی کشتی‌های تجاری باز است، اما آن‌ها باید با نیروهای دریایی ما همکاری کنند.
🔹
ما هیچ مانعی ایجاد نکرده‌ایم؛ این آمریکاست که محاصره ایجاد کرده است، و امیدوارم این وضعیت با رفع این محاصره غیرقانونیِ تحمیل‌شده از سوی آمریکا پایان یابد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/akhbarefori/652237" target="_blank">📅 10:25 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652236">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
شهادت ۱۰ شهروند لبنانی در حملات وحشیانه صهیونیست‌ها
🔹
درحالی که رژیم صهیونیستی همچنان با نقض مداوم آتش‌بس نمایشی در لبنان به حملات وحشیانه خود علیه این کشور و هدف قرار دادن غیرنظامیان ادامه می‌دهد، وزارت بهداشت لبنان شب گذشته از شهادت ۱۰ شهروند لبنانی از جمله چند کودک در تجاوزات صهیونیست‌ها به جنوب لبنان خبر داد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/akhbarefori/652236" target="_blank">📅 10:25 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652235">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qQ2U8PunJt7UfsyLAz_VCSf5HdOaZHiiFjXDS2SFLPppsTD0gl6t90N1PBnoSB0W43PXdvwFi2mtN2ntk5AIT1i6HZcssLchsY9kcebeDXQXbwAyVTEpAaIfB0VIaoeA8PljqaX-1rR1uwR4PkmLRdMzec-ZzFNe8Eo6E9wanhXM1OZInizit1ZteH_XpTmiNibAeahOPVKSZPenmQFKxy7Fky4o6xeWzYUBNHC4qQvT3Mhg5IBpGR_1_KLiDaq53HxtPozj9_msl33MfawGVYy7CiM_uW2EjdpQF9Y-M91XQovJftUzWzGKDdjfpfQFDFeZaSW9lUhlVY2ZjOWvzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دریادار سیاری: آمریکا در جنگ با ایران شکست خواهد خورد
🔹
معاون هماهنگ کننده ارتش: آمریکا در جنگ با ایران به خاطر رشادت و ایستادگی غیورمردان نیروهای مسلح و پشتیبانی ملت همیشه در صحنه، با تمام تجهیزات و توانمندی پوشالی دفاعی‌اش شکست خواهد خورد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/akhbarefori/652235" target="_blank">📅 10:15 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652234">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c315d2d0bd.mp4?token=UUr0TDmH0F2lLyABqf_GU-naLJXqIKEFfXPk7Xt9i9wujgWoB8HLN-gf-gSGWDfl_wnqB8dXFZ5N-xzn_OBrBHuXyfHFtDbwWZJe1CVrcvHWEmX6G1rbJIliOb-ChZahUw8fRb--b4_q6KRrHeMn2Q9M3MVr-vYm4O4_lWEiIf-DDDKWoUIo48Qc-XnL6wEwp4yRSykKNE5llOtrShlnnb-BcLaddRk1-zbNddvkaP-ImMyCqD9vQA8oHcxcV0Y8DvDNmIOxrwK6NEkQeC74jr5gY5H0SwKaQJIk6JBcvVpWRsZ1rC-KGuaIE01J994ZlZHQPl2KiWHP5c_LE7wh7jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c315d2d0bd.mp4?token=UUr0TDmH0F2lLyABqf_GU-naLJXqIKEFfXPk7Xt9i9wujgWoB8HLN-gf-gSGWDfl_wnqB8dXFZ5N-xzn_OBrBHuXyfHFtDbwWZJe1CVrcvHWEmX6G1rbJIliOb-ChZahUw8fRb--b4_q6KRrHeMn2Q9M3MVr-vYm4O4_lWEiIf-DDDKWoUIo48Qc-XnL6wEwp4yRSykKNE5llOtrShlnnb-BcLaddRk1-zbNddvkaP-ImMyCqD9vQA8oHcxcV0Y8DvDNmIOxrwK6NEkQeC74jr5gY5H0SwKaQJIk6JBcvVpWRsZ1rC-KGuaIE01J994ZlZHQPl2KiWHP5c_LE7wh7jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر هلال احمر از بیرون آوردن یک کودک از زیر آوار در حملات دشمن آمریکایی-صهیونیستی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/akhbarefori/652234" target="_blank">📅 10:11 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652233">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ce97e1e5e.mp4?token=GPEgMC5p-Q92KHru7c6RmukcsLSvann72bTYRCwz1HfHRfZT-Uwi7LfZ98Nh1LR_rg4ZCp4QnA-6Wxj_kGKcbf_cgiPvAedFcYnpzKqtABd8j0CZ7xExq_u3ai5yupWuhE8lg5IhbU2ZpcZ9IK1TQdRFFSDkEbuFJyAB0o3alY-7-nzcECmqV8uhxvi1-xzkjhZvqe1ebwmgkFhHwSN3vb2MJgJ6SxfadHKxNMkS571Tkr81RDSkZQE7omWniKZR1DbU-XERambB3jwo6abJXM6shehiM8H75n6Vs5jkmtoFGzjOrAKkKgox-khLrX5aFd5CJcZYWqZHNz3kBrC1aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ce97e1e5e.mp4?token=GPEgMC5p-Q92KHru7c6RmukcsLSvann72bTYRCwz1HfHRfZT-Uwi7LfZ98Nh1LR_rg4ZCp4QnA-6Wxj_kGKcbf_cgiPvAedFcYnpzKqtABd8j0CZ7xExq_u3ai5yupWuhE8lg5IhbU2ZpcZ9IK1TQdRFFSDkEbuFJyAB0o3alY-7-nzcECmqV8uhxvi1-xzkjhZvqe1ebwmgkFhHwSN3vb2MJgJ6SxfadHKxNMkS571Tkr81RDSkZQE7omWniKZR1DbU-XERambB3jwo6abJXM6shehiM8H75n6Vs5jkmtoFGzjOrAKkKgox-khLrX5aFd5CJcZYWqZHNz3kBrC1aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دشمن ادعا داشت به مراکز نظامی حمله می کند اما کارخانه رب گوجه فرنگی را هدف قرار داد
🔹
رییس سازمان هلال احمر: حدود ۱۴۹ هزار واحد غیرنظامی آسیب دیده یا تخریب شده‌اند.
🔹
از این تعداد، ۱۲۳ هزار واحد مسکونی وجود دارد که حدود ۱۰ درصد آن‌ها به طور کامل تخریب شده‌اند.
🔹
۳۵۰ مرکز درمانی شامل بیمارستان‌ها و مراکز بهداشت در حمله آمریکایی صهیونیستی تخریب شده‌اند.
🔹
۹۹۳ مرکز آموزشی، از جمله مدارس، مورد حمله قرار گرفته‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/akhbarefori/652233" target="_blank">📅 10:06 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652232">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1B2K5g03ZNYs960_teCTOZj4nNj9YXHcyBIGmjyr0OXaB9YpTVISDl_K9pWGuxt5mGC5826pWpbPUlGfwxhavATjV7brpM_FsYn42a9iZ7JrckoIDLyRDkcGJUa8v8D2M-_8Ck9pz_KJ3uTFQDxnEtGvSkYoAwOze9vP-BIi7IHBRE41IcCxs8NXe7Rd3aQEr8MyKoI7DKSDOusHeY2WUJqZbceX9FzEz0NWZH6GDqXE5oCttguJO-lOOeIvQZySN6UxMPtPSgRV5vKpU1q6gYGlhvTWsCQfYTIGhPZyvpd1uL07CwDyK_icTFH66w2bG69TPViMD8QbvUXSo9WJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استفاده آمریکا از جزیره بوبیان کویت علیه ایران در جنگ تحمیلی سوم
🔹
ارتش آمریکا با استفاده از تاسیسات گارد ساحلی و تاسیسات نظارتی و لجستیکی کویت در جزیره بوبیان اقدام به استقرار سامانه‌های متحرک پرتاب موشک‌های هیمارس در جزیره بوبیان و تعرض به خاک جمهوری اسلامی ایران کرده بود.
🔹
این عملیات تجاوزکارانه از خاک کویت در روز ۴ فروردین سال جاری انجام شده بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/akhbarefori/652232" target="_blank">📅 10:01 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652231">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
اموال ۴۷ نفر از خائنین به وطن با حکم مقام قضایی در استان همدان توقیف شد
🔹
با دستور مقام قضایی اموال ۴۷ نفر از خائنین به وطن و کسانی که علیه امنیت و ثبات کشور اقدام کرده‌اند، در راستای حفظ حقوق عامه به نفع مردم در استان همدان توقیف و ضبط شد. رسیدگی به پرونده این افراد در جریان است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/akhbarefori/652231" target="_blank">📅 09:54 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652230">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UurBURZTt-Ct03bgppN6GXX2Hx1ATCJPIVI6l3Qs6XE5QIhnXPUhtT76OKVopbWnkdCI9moF3gtjqamN4nVzJX87PunMoh4WNz0ib0wUD7TMFAcAMz9hvvR0daXyuF5Lq52rPevsvsgInOChL6qhVA3dqxMOPwim997QtPazgI_eOh_J5_8cELz1qFuZrfVBMgYi1g18XHV8_DXK6bNR6wtF5sq1dFk5b9wXV-94AwDcdaqBJl_E7LhBnkKVNp65iGzWcllDN9B8oj5M3w4MtW4f0aBziKMre3sj-Kc0fyqserq-bV2KPSlCFabsm9qF-GeIqSuwusrNvCEKFCgbhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روند مورد علاقه ترامپ: وقفه‌ای کوتاه پیش از دور بعدی خشونت | پیروزی سریع تبلیغاتی و عکس یادگاری سیاسی | آتش‌بس هنری است که ترامپ ندارد
🔹
سودارسان راغاون، تحلیلگر باسابقه و خبرنگار ارشد سابق وال‌استریت ژورنال در تحلیل تازه خود در نیویورکر استدلال می‌کند که سیاست دونالد ترامپ در قبال ایران و بسیاری از بحران‌های جهانی، بر ایجاد «آتش‌بس‌های موقت و شکننده» استوار است، نه حل واقعی منازعات.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3214576</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/akhbarefori/652230" target="_blank">📅 09:48 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652229">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lK_i6x76ACeR9RfsCo67OhM0eN4_vyAc3uOzEvOqZV9a0Fl6aOMj-_BV-eaG3gGQv314ZoYk5h_qtWEYdbYwPd1-DIhCfE1JNWsgemJwqXVQqNeiK7qPrCn_jIOC2VSrG3K33OKS5RVfTNdYMR9wSKH452PYW9i8ni__-tDF2y72ED7efQV91nfJi4ZTq441p0wjcCMNWwBe36BocxJmNTQiLRi9SsBQCN44QzHmEq_DSdDQltpsitqv8hAQjatnzGq6Vjtw1hfsqA9lZMrt-Im0IWDu0dA-QT7NBQGi6CB7T6r3WEIlLf-CpHLcuhjHEPeVpuzg--RHO-wc2Z-YzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عراقچی در دهلی‌نو: هرگز در برابر هیچ فشار یا تهدیدی سرخم نمی‌کنیم
🔹
وزیر امور خارجه امروز در نشست بریکس در دهلی‌نو گفت: هیچ‌گونه راه‌حل نظامی برای هر موضوعی که به ایران مربوط باشد وجود ندارد. ما ایرانیان هرگز در برابر هیچ فشار یا تهدیدی سر خم نمی‌کنیم، اما به زبان احترام پاسخ متقابل می‌دهیم. هرچند نیروهای مسلح قدرتمند ما آماده‌اند پاسخی کوبنده و ویرانگر به متجاوزان خارجی بدهند، اما مردم ما صلح‌طلب هستند و خواهان جنگ نیستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/akhbarefori/652229" target="_blank">📅 09:46 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652228">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EJgZTziQF8gOIOU0UdUOzA6AIVMFAJ2f2hZI3rvP1naAn-oAMbxm8xEVM58kPt1SxNPeN_Trc_tZnuaYkDhmLoedOay9ZoA47DrASEUk7zTPxj2onJzdQ0LUOFd1WsuxQW336PNPCRj1OG1zrIl_Ldfp9wf91iUBXUL_lSby7RSayVRCok_Z5nirDjGrQY_BUqqQiVYKa7nxM4XqcIqloqUQmNzzjeLB1lTrSeIftPY2BWYEjsaoHIMJIE6dimEeY3NowL2FYK8Z6_AGeicCV04Vlka-bBNEP-qAFrZr107cC5BRcxrZI0MJe-ECiXqnwtfaRXcVLEZr0yL0wX5XFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شی جین پینگ: مساله تایوان مهمترین موضوع در روابط پکن-واشنگتن است
🔹
رئیس جمهوری چین، موضوع تایوان را مهمترین موضوع در روابط پکن-واشنگتن اعلام کرد و درباره حمایت آمریکا از جدایی‌طلبان جزیره تایوان هشدار داد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/akhbarefori/652228" target="_blank">📅 09:01 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652227">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52781fd6a0.mp4?token=fAtWUbITRu0dubOHFu2EsrbGZwmT81Qbtjj-theTlzSkznzTugxU42GMUJDpXnJvU0A_FYhss5zt_oHBwWHimRZmE80Xsu8SubeMxGvTRVPkSIzDjS3qWWsyOFZc4ojiFGmrH5rnPqN4DVTUSEjNPMhljuPFDmCErcLfS_clfdRcdj4JTZBt50EI990o261I4nG_O3n13OgcL2N3BfEjxg0p0XHin1_N6035-6wSOVmSbYiEm-n4rLhy6iFHauTABRPowsEDpyilrjhJeeFEb_ztb1jAqnjyEVfR099KYBkkT8zawgGYmDwpaVkyJ3uxqdVwGm68vceJaoHYB5Ky4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52781fd6a0.mp4?token=fAtWUbITRu0dubOHFu2EsrbGZwmT81Qbtjj-theTlzSkznzTugxU42GMUJDpXnJvU0A_FYhss5zt_oHBwWHimRZmE80Xsu8SubeMxGvTRVPkSIzDjS3qWWsyOFZc4ojiFGmrH5rnPqN4DVTUSEjNPMhljuPFDmCErcLfS_clfdRcdj4JTZBt50EI990o261I4nG_O3n13OgcL2N3BfEjxg0p0XHin1_N6035-6wSOVmSbYiEm-n4rLhy6iFHauTABRPowsEDpyilrjhJeeFEb_ztb1jAqnjyEVfR099KYBkkT8zawgGYmDwpaVkyJ3uxqdVwGm68vceJaoHYB5Ky4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آیت‌الله نوری‌همدانی با صدور فتوایی، پرداخت وجوهات شرعی مقلدان «رهبر شهید» به رهبر معظم انقلاب را مجاز اعلام کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/akhbarefori/652227" target="_blank">📅 08:18 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652226">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">پادکست کافئین- داریوش بزرگ -قسمت هجدهم</div>
  <div class="tg-doc-extra">داریوش بزرگ</div>
</div>
<a href="https://t.me/akhbarefori/652226" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
پادکست
#کافئین
▶️
«داریوش بزرگ؛ معمار امپراتوری ایران»
🗓
این قسمت روایتی‌ست از پادشاهی که پس از طوفان شورش‌ها، ایران را یکپارچه کرد؛ از مردی که با نظم اداری، قانون‌گذاری و ساخت پارسه (تخت جمشید)، پایه‌های یکی از بزرگ‌ترین امپراتوری‌های جهان را استوار ساخت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/akhbarefori/652226" target="_blank">📅 07:37 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652225">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ac1de98ac.mp4?token=E61yxjsbp1iRuB46HYW4D6RJJ7JkI4gkOZ1U_DIt60S1Qd9ef46BNEw_eIxfun0lxf4rh6ee_vgZs811bQ8Iw5dtRNG-nCRx59F0HQT89Zvt_JFgkhXGzgdl2_ZWBwVwXClnB5rHDcpaagFe1EijFlgP7avOOQ_sedLqKegM4ARXHpJ5rP1sV357h1JidVjaijO2RDmJS00ygpGh_Cs5yQqpuL4CoUYnoE35sm61A04iZQGmVMmzG-o-UB4mXFevP8Yu5ON1aLBdJfTIJ-aCaBy33_mbFjALNFtNg32bYDisZyRspgz1EgRcELTBPb73G6cKHAINsLnvduMTkJCZ_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ac1de98ac.mp4?token=E61yxjsbp1iRuB46HYW4D6RJJ7JkI4gkOZ1U_DIt60S1Qd9ef46BNEw_eIxfun0lxf4rh6ee_vgZs811bQ8Iw5dtRNG-nCRx59F0HQT89Zvt_JFgkhXGzgdl2_ZWBwVwXClnB5rHDcpaagFe1EijFlgP7avOOQ_sedLqKegM4ARXHpJ5rP1sV357h1JidVjaijO2RDmJS00ygpGh_Cs5yQqpuL4CoUYnoE35sm61A04iZQGmVMmzG-o-UB4mXFevP8Yu5ON1aLBdJfTIJ-aCaBy33_mbFjALNFtNg32bYDisZyRspgz1EgRcELTBPb73G6cKHAINsLnvduMTkJCZ_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داریوش بزرگ، پادشاهی که امپراتوری را از نو ساخت…
​قسمت هجدهم پادکست کافئین منتشر شد
☕️
⚪️
با قانون، جاده شاهی و نظمی کم‌سابقه، ایران به قدرت اول جهان باستان بدل شد…
​
هر روز صبح با یک شات غلیظ از تاریخ، آمادهٔ شروع روزتون باشید!
​از اینجا ببینید و بشنوید
👇
https://youtu.be/Qfgg8RqcuBg?si=5uXMp7EKJBtDtAjp
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/akhbarefori/652225" target="_blank">📅 07:36 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652224">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H6URnY8s8A-JhAF5EAmCGVq7PGTNNBWfXwvM7aWTxsQ7Qd5pYTGCL7ur5CL2FQg3Qx6FPmr0Bbx-AfL74HsAivRjTO7wp6n8Rfw9NbgNBiA1g8O-U-rco-mDxr3Z5hqwsXrZ1z1LF56_CE7-hgFlM_xQC1_XdvbT42tm0SC1hnyTbHvlyFnaGlEr04OzfE5pGMJTpLrd-YIKdRNFohqnqy3ZwRlRrFDrKXCbHN4hMwaCEjA_h0Z1TOeoSsQzsvGcvJbzFL-eoEwOik7BJPifee1UiN2U9eO4DPkrmwXhhqg0LP6hURLd65-axfLJu9UPPmDPzx6MbIDD-JxZoZUCXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آغاز ثبت‌نام وام ۷۵ میلیون تومانی بازنشستگان کشوری از امروز
🔹
معاون توسعه مدیریت و منابع صندوق بازنشستگی کشوری: فرآیند ثبت‌نام وام سال ۱۴۰۵ از امروز پنجشنبه ۲۴ اردیبهشت ماه آغاز شده و تا ۲۰ خردادماه ادامه خواهد داشت.
🔹
مبلغ این وام از ۵۰ میلیون تومان در سال گذشته به ۷۵ میلیون تومان افزایش یافته است.
🔹
وام ۷۵ میلیون تومانی در ۱۰ نوبت به متقاضیان واجد شرایط پرداخت خواهد شد.
🔹
مطابق با ضوابط و شرایط اعلامی از سوی بانک عامل، مبلغ کارمزد و نرخ سود تسهیلات برابر با ۴ درصد است‌.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/akhbarefori/652224" target="_blank">📅 07:15 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652223">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dw22DznoiHs4dtHVNVOe_6gUn2XTL149FLLv1mGhZU0XxvZOaycFbKPfqJMx4W5nwagg3uYLR_zcXGPP1JXwNRdcgupQAB7nTSTQWGfBWYEsdUdV_nndagkuVS9fDOOM73W79vimTiYwqsvfjy0jT5-2U5ApbksNJOtMCrLawbJuecYptjESvK2Soiaj4dmx9a5zAP7ikf901nn5Hm7jcm23anuC4raC-_9Ov2yrR7adblrPPpk_YbrWTXpvDo9buZrZKG3VvDfv8c4_246AJZLQ80tznle5-d1mBa34f_lJfKQCJAcLCnFSbfPkueOCPEcU5_p6zc3KXQnimb6UAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز پنج‌شنبه
۲۴ اردیبهشت ماه
۲۶ ذی‌القعدة ۱۴۴۷
۱۴ می ۲۰۲۶
پنج‌شنبه‌ها
#دعای_کمیل
بخوانیم
⬅️
متن و صوت دعای کمیل
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/akhbarefori/652223" target="_blank">📅 07:02 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652222">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
اسپوتنیک: حملات ایران به پایگاه های نظامی آمریکا، ضعف نظم منطقه‌ای واشنگتن را آشکار کرد
🔹
حملات ایران به پایگاه‌های نظامی آمریکا در سراسر خاورمیانه به گونه ای بود که بازسازی آنها ممکن است امکان پذیر نباشد و «ضعف اصلی نظم منطقه‌ای واشنگتن» را آشکار کرد.
🔹
جنگ ایران مجموعه‌ای از چالش‌ها را برای آمریکا آشکار کرد به این معنی که ایران از دکترین نظامی مدرن با تعداد زیادی موشک و پهپاد استفاده کرد، پایگاه‌های پراکنده و زیرزمینی ایران حملات آمریکا را بی‌اثر کرد، قلمرو و جمعیت وسیع ایران مشکلات استراتژیک دیگری را به همراه داشت، برتری هوایی آمریکا خنثی شد و نتیجه جنگ به تساوی رسید.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.45K · <a href="https://t.me/akhbarefori/652222" target="_blank">📅 06:55 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652221">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
مشاور ویژه در دولت ژاپن: ایران فراتر از حد انتظار در انسداد تنگه هرمز موفق عمل کرده و تن به هیچ عقب‌نشینی نخواهد داد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/akhbarefori/652221" target="_blank">📅 05:32 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652217">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DEMUYOnF8ShKK6naScBkeQ8hBV1vjn3wrF-tUmjU98rnTut6eduOV846qVqAL7NXkpQQ1XndTsBj839V5SgBaKrpVaKEZzHmG-1Yom_6fztUbw6l57e45XqWPvt6PIMsk27u-k7ZE0bNyyber8oZ4lDP-Sje6rqgLgd6oFY8v_OZf35gaEFQjp5bD6GWFvKrESzXNg2LnaTMWkjY6VClFqsE020UBmrtKbLm0tzuV9q-mfy-qEByHqNShiZx53zjdvcfax9YSpqjYa_iEta-pfnkaozHo2foAqjvgl87ldRPPaqq-5Ow9aONiC8cMpb1HPwD9Yxd0XWicf2WyiEvDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5606f153ba.mp4?token=knbZGaBtpUcdPAJATd6n_V3TDzgakHTTHErav814gOCbtDScUqv4b8POI4FOIzTJzNPQeoTBD3JHNyJktG3IEKt-HOcMmOtd4MtK13h5nVNYccGA856hiATgQy3Cvmp76qIGZG-t3caHj4DCTC0TM3KutCSMFdSI_fzcgBjg1CtvyV8YzYMmgu7dyZXqGujtS05XhkS5RG2EdxGf2ZpU4xCpppGW-Dm8-Kz_WQeE9uOpYD8T4n0cIZdJhzK4B49mMEYXNeCPUa_66TOi3H30m17i71yeqkwCXfDHhwkixf4pzhRXsFkG1wlNfXTi_hd_9wU0Pzj4KcdYfgo9R1CmBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5606f153ba.mp4?token=knbZGaBtpUcdPAJATd6n_V3TDzgakHTTHErav814gOCbtDScUqv4b8POI4FOIzTJzNPQeoTBD3JHNyJktG3IEKt-HOcMmOtd4MtK13h5nVNYccGA856hiATgQy3Cvmp76qIGZG-t3caHj4DCTC0TM3KutCSMFdSI_fzcgBjg1CtvyV8YzYMmgu7dyZXqGujtS05XhkS5RG2EdxGf2ZpU4xCpppGW-Dm8-Kz_WQeE9uOpYD8T4n0cIZdJhzK4B49mMEYXNeCPUa_66TOi3H30m17i71yeqkwCXfDHhwkixf4pzhRXsFkG1wlNfXTi_hd_9wU0Pzj4KcdYfgo9R1CmBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حملات گسترده روسیه به کی‌یف، پایتخت اوکراین، با پهپادهای گران-۲ و موشک‌های بالستیک اسکندر‌-ام
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/akhbarefori/652217" target="_blank">📅 05:30 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652216">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ijI6GZ_SLBo2Kc6HBHX59cXkcM-PTLDE4-qZu9q4zshiXPf7z3K70_Rrc7SFXysC1U6J8Hq4ZBSzzcHBXsXsWROpempDKmUqnOqfb-xFUdoB8Doc1oU8ehbCnjmjR8fcm55xe8OiPIOeDoPj2hK0z0fLO75lGYH-i7Yao4IFOOrrTWWQ0EYsC9-Yh4ND3k9g7RDGz9II86J_c_XuuqoVwOdqGVc5Ap00A_Yew0lLX6WaBwiP0w39PaK1kHs5tln7tEeeJzJg3CMfNOsA8zHpvdd8hJXAi0bWGNPcVr8juPjnCVlsu-7nCpJwjDyJxalkfCqT3g1XRwlz4vJQx8of_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ناوگان اورژانس کشور جان می‌گیرد
🔹
معاون وزیر بهداشت: در سال جاری، ۱۰ هزار و ۵۰۰ میلیارد تومان به حوزۀ اورژانس کشور اختصاص‌یافت تا فرسودگی ناوگان و مشکلات این حوزه مرتفع شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/akhbarefori/652216" target="_blank">📅 05:20 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652215">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6Yst4EfJ6YsmKUiRCccNqa-E6C_UlE_EgVUr7ryMFYhuqSvK9VqZ6XFQr-VRkicNhgPt4UevpBTylvqJrLE1Vhw-youwRhZL_XKaurXrSK9Atd8UFvI9Kr21zqXIWFXBAiuVU0XuPQDnzWN6zk9ZIZgSbTxgXxHyq-7dsFJ8oZmwNjEQxCPzPFldn3NyANhoXtBP7oTeVJx97CmszRLPUfr3T5ucTVIEyYNu7jA0WVJBIVC5Zrqk9Q68-nlkJ_0usIQH_mGAOp1t4-eZX9hi9EgBNafl9i-juq5gVBtiHl_KOXyXsRucpQiO_GKATGpRjZ_ZDeDlRMQbmhHFyZ6lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمریکا در فکر تسهیل خرید نفت ایران توسط دو بانک چینی
🔹
انتظار می‌رود وزیر خزانه‌داری آمریکا موضوع تسهیل خرید نفت ایران توسط دو بانک چینی را مطرح کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/akhbarefori/652215" target="_blank">📅 04:28 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652214">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
تصمیم اسرائیل برای عملیات در عمق خاک لبنان
🔹
نشریه «اسرائیل هیوم» بامداد پنجشنبه گزارش داد: «کابینه امنیتی اسرائیل به ارتش دستور داده تا طرح‌های جدیدی را برای عملیات‌های عمیق‌تر در لبنان آماده کند».
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/akhbarefori/652214" target="_blank">📅 03:35 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652213">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2da36df3a.mp4?token=j8Pa3pYzoHzzs0tnHGQb64cDEW2lVN24zgjp5IVhn5gBwuxuel0JED4gvO6WsFtCpOjhRYoYh5kZr1z-52vz4MwrzkSYqxyXsGtBlBuMV1tOB5mYPcC_2ffcgy8is7KCthB1T0xPLmFrtSIvFY6wQ7AJCvjIn3rhfDWBKFRpVtOc6JD4ZFNSVkDRpvuUMLvVXxyqu96Z771fqc9VnuaHcEy1R8bY3Lgz1DEgzx8hSkXeQwmnkgqNldnCjysayDwlgQ7Tab1DNZtIJ1BjGHOZEW1TtMAFuP_iinyjUnHTjc2EXO28dEA750MTmlWzXaB45v9Nn6OeEhK7otHOwrOcAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2da36df3a.mp4?token=j8Pa3pYzoHzzs0tnHGQb64cDEW2lVN24zgjp5IVhn5gBwuxuel0JED4gvO6WsFtCpOjhRYoYh5kZr1z-52vz4MwrzkSYqxyXsGtBlBuMV1tOB5mYPcC_2ffcgy8is7KCthB1T0xPLmFrtSIvFY6wQ7AJCvjIn3rhfDWBKFRpVtOc6JD4ZFNSVkDRpvuUMLvVXxyqu96Z771fqc9VnuaHcEy1R8bY3Lgz1DEgzx8hSkXeQwmnkgqNldnCjysayDwlgQ7Tab1DNZtIJ1BjGHOZEW1TtMAFuP_iinyjUnHTjc2EXO28dEA750MTmlWzXaB45v9Nn6OeEhK7otHOwrOcAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراف سناتور ارشد آمریکایی به شکست و تحقیر یک ابرقدرت نظامی با بودجه تریلیون دلاری
🔹
واشنگتن با بودجه‌های تریلیون ‌دلاری مقابل ایران با بودجه‌ای بسیار ناچیز به گروگان گرفته شده است!
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/akhbarefori/652213" target="_blank">📅 03:10 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652212">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X7dV017WBlwOe-QDubMm53jTtXxT0bquIZF81ukTIELDjR18lXkVWGVw-SjtItcBQq-tGQEg7SR2peaNx2JXb90T40s6i8G8qIm_6fSszrcQTzUmAxfpSACG2Z5nqQeakzCkEsApCiVMqn95q72ZViRMUHr8hyNJKHToG_0oLJZ7N9oWrm1o83DtEOPcWnbBMRyrg-alftyXOWK6-apH6OiiFcHfHnuNA4_i1FQgu2AmxFw6_yUQAWesf4VP2Yq7D5r_YUyrS_Q6fCGPRAgzy7HPIli_qGKTFuvkej5gG83374GPK1BtLDA7-fEezzoYYhRFR6MT-gS5qCMUTnnkCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لغو استقرار ۴ هزار نظامی آمریکایی در لهستان
🔹
مقام‌هایی در ارتش آمریکا می‌گویند که وزارت جنگ این کشور برنامه استقرار بیش از چهار هزار نیروی نظامی در لهستان را لغو کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/akhbarefori/652212" target="_blank">📅 02:53 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652211">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
شهادت ۲۲ لبنانی در حملات رژیم صهیونیستی در ۲۴ ساعت گذشته
🔹
وزارت بهداشت لبنان خبر داد که طی حملات رژیم صهیونیستی در منطقه جبل لبنان و جنوب این کشور طی ۲۴ ساعت گذشته، ۲۲ نفر به شهادت رسیده‌اند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/akhbarefori/652211" target="_blank">📅 02:41 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652210">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
وزیر خارجه آمریکا: تلاش داریم که چین را برای قانع کردن ایران قانع کنیم
🔹
مارکو روبیو، وزیر خارجه آمریکا: امیدواریم که بتوانیم چین را قانع کنیم تا نقش فعال‌تری برای قانع کردن ایران جهت توقف اقداماتش در خلیج فارس ایفا کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/akhbarefori/652210" target="_blank">📅 01:32 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652209">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
رئیس ائتلاف حاکم در اراضی اشغالی، با مشارکت تمام رؤسای فراکسیون‌های ائتلاف، رسماً لایحه انحلال پارلمان این رژیم (کنست) را ارائه کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/akhbarefori/652209" target="_blank">📅 01:03 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652208">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zf6sWzwHurecJNQJSWpzhPQIRMzBHOb4M7PqoVZ5RCi9ZE84l4lD1qX8K39sLhre6XGNLPGZvImdu6SexY0zzV_dy__xn5q3aFEQ2uBNg1A58i7jnHgOODQmJ72v2WOY2UC2AzOPn-fYaDY8kq0zdKwEvCJAsJBTKWQ4WNwdKEThYshSWrpiBW81BF_28-CIhMem7jboFdIiiaaNR9UeWQEcrCVgC0ZVAEOGzjr7NRP7je466NKe3tRagdT1uAldcbv5BwQt-DiuRr9aoiOPEd_mskwo7MWrMy7pki-PClAOtIMo1fZm8EpLeKvA5GIOU60tn1FXMRNTIR7O2PLneA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بجنگ برو جلو
🔹
تیم ملی فوتبال کشورمان بیش از اعزام به مسابقات جام جهانی امشب بدرقه ای خاص و متفاوت داشت و در میدان انقلاب توسط مردمی که بیش از ۷۰ روز میدان دار خیابان بودند بدرقه شدند. ملی پوشان ایران میثاق نامه ای قرائت کردند و گفتند که قول میدهیم تا پای جان برای موفقیت و سربلندی ایران در جام جهانی تلاش کنیم
🔹
هفتصدوچهل‌وهشتمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori
,</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/akhbarefori/652208" target="_blank">📅 00:46 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652207">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
در لابلای خبرها، داغ‌ترین‌ها را از دست ندهید
🔹
توافق محرمانه آمریکا و چین بر سر ایران
👇
khabarfoori.com/fa/tiny/news-3214648
🔹
سخنی که گور بی بی را می کند | نتانیاهو به زودی ترور می شود؟
👇
khabarfoori.com/fa/tiny/news-3214727
🔹
حرف‌های منشوری پشت سر امانوئل مکرون و گلشیفته | سیلی برژیت به‌خاطر بازیگر ایرانی بود؟
👇
khabarfoori.com/fa/tiny/news-3214825
🔹
روند مورد علاقه ترامپ: وقفه‌ای کوتاه پیش از دور بعدی خشونت | آتش‌بس هنری است که ترامپ ندارد
👇
khabarfoori.com/fa/tiny/news-3214576
🔹
تمام قاره‌‌ها درگیر انواع‌‌ هانتاویروس | بیماری که با آنفولانزا اشتباه گرفته می‌شود اما کشنده است
👇
khabarfoori.com/fa/tiny/news-3214245
🔹
ویدئوهای جذاب را در آپارات خبرفوری ببینید
http://aparat.com/Akhbar.Fori</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/akhbarefori/652207" target="_blank">📅 00:37 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652206">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
حال دریاچه ارومیه خوب است اما تو باور نکن!
محمد کوهانی، دبیر شبکه ملی محیط زیست سازمان‌های مردم نهاد جوانان کشور در
#گفتگو
با خبرفوری:
🔹
بیش از ۸۰ درصد بستر دریاچه ارومیه زیر آب رفته، اما کارشناسان می‌گویند هنوز تا احیای کامل فاصله زیادی وجود دارد.
🔹
با وجود بهبود وضعیت، تراز دریاچه به رکورد سال ۹۸ نرسیده است. سال ۹۸ تراز دریاچه نزدیک به ۵ونیم میلیارد مترمکعب پیش‌بینی می‌شد اما در سال ۱۴۰۰ بدترین ترازها را ثبت کرد و برای رسیدن به تراز اکولوژیک باید حدود ۱۶ میلیارد مترمکعب آب در دریاچه وجود داشته باشد.
🔹
کارشناسان هشدار می‌دهند کاهش بارش و مدیریت نشدن آب در تابستان می‌تواند دوباره تراز دریاچه را کاهش دهد.
@TV_Fori</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/akhbarefori/652206" target="_blank">📅 00:35 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652204">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LYm3wHn6dq2R5zklL6mTEixvv72C8RIW2Z_nfh8kR_c6p6aIrv4CDJK8JSb9qpzIcAzCN7AFQAbbiEyNNp-9gB3uU_T6jSiylEn91t5OTWWh7PYGYMf4gdJa1IKQJyS0yHsMgwewz3cmp4AL_Bfa0moZ5wVK55XbNg9KUh4wb5MZ1ez7X3Z7bbRC0eK_r6GqRtN1MpN6nuDd7iJHcBgqwDImimslP787sQBeciSeUd8IeJbUd5RjIqeVt96uNHSi1JHgUWutujFMCAXp_O_P1_DBIIvxkx1dK9bG-yrphr35p3bg8YIBjy7HlyJGQ0PE_mgHOGsq98zUPz4ZYIEmgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رسانه‌های اسرائیلی: حملات حزب‌الله شمال اسرائیل را فلج کرده است
🔹
مقامات محلی اسرائیلی به رسانه‌ها گفتند که حملات حزب‌الله باعث شده هیچ فعالیت اقتصادی و اجتماعی متمرکز و ثابتی انجام نشود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/akhbarefori/652204" target="_blank">📅 00:19 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652203">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
کاهش تقاضا قیمت کاغذ را کاهش داد!
نیکدل، رئیس اتحادیه صنف فروشندگان کاغذ و مقوای تهران، در
#گفتگو
با خبرفوری:
🔹
قیمت کاغذ تحریر و کاغذ A4 کاهش یافته است. کاغذ تحریر از ۶ میلیون و ۲۰۰ هزار تومان به ۵ میلیون و ۷۰۰ هزار تومان رسیده و قیمت یک بسته کاغذ A4 نیز به‌طور میانگین ۸۵۰ هزار تومان است.
🔹
این در حالی است که کاغذ A4 در هفته‌های گذشته با افزایش ۵۰ تا ۷۰ درصدی قیمت مواجه شده بود.
🔹
جنگ بر روی افزایش قیمت کاغذ موثر بود، اما دلیل کاهش اخیر قیمت کاغذ، افزایش عرضه، کاهش مصرف، کاهش تقاضا، نظارت سازمان بازرسی و کم‌کار شدن چاپخانه‌دار‌‌ها بوده است.
@TV_Fori</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/akhbarefori/652203" target="_blank">📅 00:05 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652202">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔹
در لابلای خبرها، داغ‌ترین‌ها را از دست ندهید
🔹
🔹
توافق محرمانه آمریکا و چین بر سر ایران
👇
khabarfoori.com/fa/tiny/news-3214648
🔹
سخنی که گور بی بی را می کند | نتانیاهو به زودی ترور می شود؟
👇
khabarfoori.com/fa/tiny/news-3214727
🔹
حرف‌های منشوری پشت سر امانوئل مکرون و گلشیفته | سیلی برژیت به‌خاطر بازیگر ایرانی بود؟
👇
khabarfoori.com/fa/tiny/news-3214825
🔹
روند مورد علاقه ترامپ: وقفه‌ای کوتاه پیش از دور بعدی خشونت | آتش‌بس هنری است که ترامپ ندارد
👇
khabarfoori.com/fa/tiny/news-3214576
🔹
تمام قاره‌‌ها درگیر انواع‌‌ هانتاویروس | بیماری که با آنفولانزا اشتباه گرفته می‌شود اما کشنده است
👇
khabarfoori.com/fa/tiny/news-3214245
🔹
ویدئوهای جذاب را در آپارات خبرفوری ببینید
🔹
http://aparat.com/Akhbar.Fori</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/akhbarefori/652202" target="_blank">📅 00:02 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652201">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cfHqeolspBs83CbWTvzIKxx7RKTd5z_PCLQlhzchWmydlfE7OFCrSC_lNGNVEPuLsNjC-19z1_U3J_pZBd5650ll4qr9rpSZU9kx8GlLOocLocnTOZXK8QV7R1UVguOzDZl_lGl99aifzuVbFxENrp-25t5bcfW6KSVmBuK5t3FpvuMrgxFO4YxCCUefdscM54Spx5QurYzjpOT8xHF6p93-i5hVvHeHftcVYvnYm4KCeTXLtyq5AKyriux0tVUdS1gAg7cFNX-gtQ1aczwITKJiERInppMM8Cdzuskf9r4i5_X5l00Cj4o4km_X5TXU3Ri2-gcR5ulkF4CuMop3oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش عراقچی به اظهارات اخیر نتانیاهو؛ همدستی با رژیم اسرائیل غیرقابل بخشش است
🔹
نتانیاهو اکنون به‌صورت علنی آنچه را که نهادهای امنیتی ایران مدت‌ها قبل به رهبری ما منتقل کرده بودند، افشا کرده است.
🔹
دشمنی با ملت بزرگ ایران، قماری احمقانه‌ است؛ و همکاری و همدستی با اسرائیل در این مسیر، غیرقابل بخشش است.
🔹
کسانی که در همدستی با اسرائیل برای ایجاد تفرقه نقش دارند، باید پاسخگو باشند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/akhbarefori/652201" target="_blank">📅 23:51 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652200">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WtvmL3zNdsef4ep7CMhLHTBlmY6SG0c1fpYCTJfb_B5rvAFRmIE-IavWDqshBHeJB6t4FJPO3Ylq_o0QjxLTONWgQhvQC4XrJenOBaJ0K1F9dWjTBoo1S8b67Z3CEzCVutLysidQv_hcaawHaYc5kgMBUG7JXntQ2DyINgHJu9gPrA_3L6oVCgEFFRgiCRKlxa4lGfN-k3DA4KGKw1gKuPkbjjDcrlLOT6ghMJrkGg5rgYZjOT_xuZCVguPqXmfg4TKLHX1dJq1p1sZMI5WSMfSZ5v23Om76iroRcj78MZwxe5GHNjBKL9hSrBexfBVsHh2lIcJcdmz3eKzIXdt1gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روبیو در اقدامی معنادار با لباس مادورو راهی چین شد؛ او چه پیامی به شی داد؟!
🔹
برخی رسانه‌ها و کاربران این اقدام را غیرحرفه‌ای و کودکانه و دون شأن یک وزیر خارجه دانستند؛ رسانه‌های چینی هم این اقدام را تحریک‌آمیز توصیف کردند، به‌ویژه با توجه به اینکه روبیو قبلا به دلیل مواضعش، هدف تحریم چین قرار گرفته بود.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3214685</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/akhbarefori/652200" target="_blank">📅 23:50 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652199">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/611faee3e5.mp4?token=FOrm-NE4ZKUdYLsVFtN4FcR0ZylQU-LeA6xdGZsLryx60WiPhbqeI0j28Ct7NjICam7zX72KBGOhi_mQ_S4tOPPULtw6wXpOb-znP9-QTZRWemyIkJtscxjo_DT7-bHmcrJaT3M07mV_afls4dvRX_Z3H70qPWmTRuUMJpxX_DU_KVZ4MUzMdOAP06g9HNZTbVkQiRkrRN7-PAMCfRZRcOCWZVHV_3bdiRrk5SAeX_2m728RIpQVZzCT9ovOQ1Mu6v1iz_cW9kE1h29JyZYnhVPGUNG-mlHaq7MxetUPkIw04U4uPrQu_X6QJckjeQLK2zj9oiYtnUw1aKhtNUGPDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/611faee3e5.mp4?token=FOrm-NE4ZKUdYLsVFtN4FcR0ZylQU-LeA6xdGZsLryx60WiPhbqeI0j28Ct7NjICam7zX72KBGOhi_mQ_S4tOPPULtw6wXpOb-znP9-QTZRWemyIkJtscxjo_DT7-bHmcrJaT3M07mV_afls4dvRX_Z3H70qPWmTRuUMJpxX_DU_KVZ4MUzMdOAP06g9HNZTbVkQiRkrRN7-PAMCfRZRcOCWZVHV_3bdiRrk5SAeX_2m728RIpQVZzCT9ovOQ1Mu6v1iz_cW9kE1h29JyZYnhVPGUNG-mlHaq7MxetUPkIw04U4uPrQu_X6QJckjeQLK2zj9oiYtnUw1aKhtNUGPDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجری سی‌ان‌‌ان‌: براساس آن‌چه به ما گفته شده بود تا الان ایرانی باید تسلیم می‌شدند و محاصره آن‌ها را پای میز مذاکره می‌آورد اما نه‌تنها این اتفاق نیفتاده بلکه آن‌ها توانمندی‌های موشکی خود را بازسازی کردند و مواد هسته‌ای نیز در اختیارشان است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/akhbarefori/652199" target="_blank">📅 23:45 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652198">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HvGNy3dillNJM8e31Hzb1be1Q0gVbrkmQkdyrHZSTVqVf1W-gA1udbYuBauOXsKwGy0hZW_UhAee20xDjkqn6Agsb_I9NpDo0602YtOCWV02JtSCK4pylUeiC9En2VQ5zQY5bslirG9PgwEke6gAEVejupaPmEggDYunU5MN4K3She1qRrETaIksJHDtioUnrZvaqd8yQobeblmCQwGtp6LlOa258HCnu1hJM0ySeLQpYahTNIqQGA96mUlimyab06ml191kwAHTx9CTi4DgT5G7K34HoJwfpTVn8JMVSck9BkBEteLKGMQV8AI1IGTjCbGF_7obBqfZafuf0gKQ5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سفیر روسیه در پاکستان: مسکو آمادگی خود را برای حمایت از تلاش‌های دیپلماتیک اسلام‌آباد با هدف اتمام جنگ آمریکا علیه ایران ابراز کرده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/akhbarefori/652198" target="_blank">📅 23:40 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652197">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4bb06e773.mp4?token=ea1s5ItNb1kKruk1CLqpOWdDnMypRS5SokcsiEvYYWyxkhOACTJjWKb6KqICeSm1BDYyceuyEMUnWMetMhbgkYi3VDp_Mf62A-LbpNyDiCHlW969ldrYA-iJljPASxWMaLW0fPPujx5ZxgmBcylhVX60zjmwUf65xTfJZSlrQEEhzOWM6gotXMPm_4irVSiTS9HX0CRqWS86ImkiMUY3wjFotguR0pubSosFTwUx-yGJHlJEjS9WDeG3mytEx22DszxltWeHl6c0GhDOEcTyh0U3Gfwz6_RclNL8VhvaGNbtJ6tsJp5jQokI4kUb8HO2_hGWEXylzQfhWNDF4kl1Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4bb06e773.mp4?token=ea1s5ItNb1kKruk1CLqpOWdDnMypRS5SokcsiEvYYWyxkhOACTJjWKb6KqICeSm1BDYyceuyEMUnWMetMhbgkYi3VDp_Mf62A-LbpNyDiCHlW969ldrYA-iJljPASxWMaLW0fPPujx5ZxgmBcylhVX60zjmwUf65xTfJZSlrQEEhzOWM6gotXMPm_4irVSiTS9HX0CRqWS86ImkiMUY3wjFotguR0pubSosFTwUx-yGJHlJEjS9WDeG3mytEx22DszxltWeHl6c0GhDOEcTyh0U3Gfwz6_RclNL8VhvaGNbtJ6tsJp5jQokI4kUb8HO2_hGWEXylzQfhWNDF4kl1Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئویی پربازخورد در فضای مجازی از تشبیه فروشندگان vpn به خوک
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/akhbarefori/652197" target="_blank">📅 23:37 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652196">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
نسخه نجات بورس در بحران؛ چرا بستن بورس خطرناک است؟
🔹
بورس بیش از ۷۰ روز است که تعطیل شده، اما راهکار واقعا تعطیلی بود.
🔹
در این ویدئو چند پیشنهاد جهانی برای عبور بورس از بحران‌هایی چون جنگ پیشنهاد شده که می‌تواند به بورس ایران نیز در صورت بازگشایی کمک کند.
@TV_Fori</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/akhbarefori/652196" target="_blank">📅 23:35 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652195">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31dde9b497.mp4?token=gP-yAHa9tDgb9LCgWcbz9gx8uIlpZG5YxFtnAQbKdkf4A5_W1minVl_Ajwd6eZ4Le6itberPX3PrsNaAaGZEXQSMxRJ05wmMH8FcqFpxhFlqHhCdK2tIoBbMWJtc55FKyzhFdEToDAfnkUAn-WTiM1NV-8_I5u6OfnzcvwQqx0Gu6nwLhoOBWadb2sMj4tT8DcPBukHnom2rFqnAc83rsmwwmIM3oxfvrceQpJjjBn1UXiqz8-nC9yHuPzzvJWJwZRUM9mYRf2MLiu0SN4dYrch8lCE8EOHkgEoWCRVkTTdMWk9gQiZVV4DrkoFpnAKG-0j0uhquQzLPErj4jKYVWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31dde9b497.mp4?token=gP-yAHa9tDgb9LCgWcbz9gx8uIlpZG5YxFtnAQbKdkf4A5_W1minVl_Ajwd6eZ4Le6itberPX3PrsNaAaGZEXQSMxRJ05wmMH8FcqFpxhFlqHhCdK2tIoBbMWJtc55FKyzhFdEToDAfnkUAn-WTiM1NV-8_I5u6OfnzcvwQqx0Gu6nwLhoOBWadb2sMj4tT8DcPBukHnom2rFqnAc83rsmwwmIM3oxfvrceQpJjjBn1UXiqz8-nC9yHuPzzvJWJwZRUM9mYRf2MLiu0SN4dYrch8lCE8EOHkgEoWCRVkTTdMWk9gQiZVV4DrkoFpnAKG-0j0uhquQzLPErj4jKYVWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
غریب آبادی، معاون وزیر خارجه: موضوع تجاوز نظامی رژیم آمریکا و رژیم صهیونیستی علیه ایران، در گفتگوهای وزیر خارجه در هند مورد توجه خواهد بود
🔹
البته با پیچیدگی‌هایی نیز مواجه هستیم. یکی از کشورهای همسایه که عضو بریکس است، در طول تجاوز نظامی علیه ایران سابقه خوبی از خود نشان نداد و قلمرو خود را در اختیار متجاوزان قرار داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/akhbarefori/652195" target="_blank">📅 23:32 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652194">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
چینی‌ها از افزایش قیمت نفت ناراضی هستند/ تاکید برای بازگشایی تنگه‌‌هرمز در این دیدار
عرفان حمزه، کارشناس مسائل چین:
🔹
با توجه به تنش‌هایی که بعد از روی کار آمدن ترامپ پیش آمد، یک نبرد مخفی میان آمریکا و چین رخ داد.
🔹
ترامپ می‌خواهد چین نفت را با قیمت بالاتری بخرد و از ابتدای جنگ نفت ۷۰ دلاری به۱۱۰دلار رسیده است که افزایش قیمت نفت سرعت توسعه چین را کاهش می‌دهد و چینی‌ها به شدت ناراضی‌اند.
🔹
ممکن است این تنش‌ها جدی تر شود مگر اینکه آمریکا و چین با هم به یک توافق جامعی برسند.
🔹
پرونده ایران به عنوان یک مسئله اقتصادی و سیاسی برای هردو طرف مهم است.
🔹
احتمالا در این دیدار هردو کشور به بازگشایی تنگه هرمز تاکید داشته باشند.
🔹
توصیه می‌کنم سیاستمداران ایرانی لحظه به لحظه این رویداد اقتصادی و سیاسی را رصد کنند تا در صورت نیاز بتوانند در پاسخ به آن اقداماتی انجام دهند./جریان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/akhbarefori/652194" target="_blank">📅 23:22 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652193">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/856039f6ff.mp4?token=FNo9CYcsv-HbnRwSJ9Fl-b85uthyqnhlTeVxS2ZTwYKvxJntB82g5Ypt6q2S_QIfiyF5kjfTPlE1PG7qv68icm1GaoGJXvSS0PxfihwT0J-uiYPFo8J4_Gh7URQLMt-Jva2yOhpVHVRPU72Z0ljBlffDo6zqALzcQ462nHvnGZGYsYy7niYWaKafeThnSwFO3PhPLZ0R8ZUdt1w7qrh7du9pDlzvA7OLXcvrkQHXaPKfv5okiuIvdwkfyyTkXtHu9RIjpcamBx00Xt1EvsHG-DyG6YhcMAwK_vzzA7jMAHWzM2_Khca6g6tN5yWVyqje2F7nkbx7vKz72bEcaKyfzzUACJ1G2aJUyiML7opbrbCYXBwcC0eGP0-U59SG0KF6rBiEAbBP3h0NxGErmsd6y8423mm9JvdZBiy4De-WWw_wMYszMm2vX58vJMQxBd2I9lnPFlO-CB7OP82nVJMGJU066biib6h8U_CfkAJWRosqWFZu68tSJBAFQE0lQkJ-ETLwBX0jnzJqmGS9zhnQSHeXCVRVeOMPrAmiiJmtafurOoArx19bj3ECglTrs0jU8v4e_XsBGYKdjSwuwz9xCxyfZcQwcwE3E9V3DojjcRQRVzAgx7F_TiT3OTJtJqPj_ghK_DZ8bZ7QyLHvwtmH1jmdqVAfPx7cgqAeJ4hiIG8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/856039f6ff.mp4?token=FNo9CYcsv-HbnRwSJ9Fl-b85uthyqnhlTeVxS2ZTwYKvxJntB82g5Ypt6q2S_QIfiyF5kjfTPlE1PG7qv68icm1GaoGJXvSS0PxfihwT0J-uiYPFo8J4_Gh7URQLMt-Jva2yOhpVHVRPU72Z0ljBlffDo6zqALzcQ462nHvnGZGYsYy7niYWaKafeThnSwFO3PhPLZ0R8ZUdt1w7qrh7du9pDlzvA7OLXcvrkQHXaPKfv5okiuIvdwkfyyTkXtHu9RIjpcamBx00Xt1EvsHG-DyG6YhcMAwK_vzzA7jMAHWzM2_Khca6g6tN5yWVyqje2F7nkbx7vKz72bEcaKyfzzUACJ1G2aJUyiML7opbrbCYXBwcC0eGP0-U59SG0KF6rBiEAbBP3h0NxGErmsd6y8423mm9JvdZBiy4De-WWw_wMYszMm2vX58vJMQxBd2I9lnPFlO-CB7OP82nVJMGJU066biib6h8U_CfkAJWRosqWFZu68tSJBAFQE0lQkJ-ETLwBX0jnzJqmGS9zhnQSHeXCVRVeOMPrAmiiJmtafurOoArx19bj3ECglTrs0jU8v4e_XsBGYKdjSwuwz9xCxyfZcQwcwE3E9V3DojjcRQRVzAgx7F_TiT3OTJtJqPj_ghK_DZ8bZ7QyLHvwtmH1jmdqVAfPx7cgqAeJ4hiIG8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا جلسه اخیر هگست برای افزایش بودجه نظامی آمریکا اهمیت دارد؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/akhbarefori/652193" target="_blank">📅 23:20 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652192">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
رسانه‌های عراقی از شنیده‌شدن صدای چندین انفجار در اربیل خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/akhbarefori/652192" target="_blank">📅 23:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652191">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
سخنگوی جنبش حماس: آماده واگذاری اداره غزه هستیم اما سلاح مقاومت در مرحله دوم بررسی می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/akhbarefori/652191" target="_blank">📅 23:10 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652190">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
آخرین تغییرات قیمتی روغن، برنج و حبوبات
کنگری، رئیس اتحادیه بنکداران مواد غذایی تهران در
#گفتگو
با خبرفوری:
🔹
روغن در فروردین ماه، ۱۶ درصد و الان ۱۵ درصد افزایش قیمت داشته است. قیمت روغن ۸۱۰ گرمی در بورس کالا ۳۲۷ هزارتومان می‌باشد اما در شبکه‌ تنظیم بازار این محصول ۲۸۱،۹۵۰ تومان به دست مصرف‌کننده می‌رسد.
🔹
سایر کالاها مانند حبوبات و برنج روند کاهشی در بازار داشته‌ است.
🔹
روند عرضه و تقاضا به طوری هست که انگار در شرایط جنگی نیستیم. زنجیره تامین در کنار زنجیره توزیع قرار گرفته و روند عادی را طی می‌کند. تا این لحظه مشکلی در راستای مواد غذایی به خصوص کالاهای اساسی نداشتیم.
@TV_Fori</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/akhbarefori/652190" target="_blank">📅 23:03 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652189">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
نخست‌وزیر انگلیس در نخستین جلسه مجلس عوام پس از بازگشایی پارلمان، بار دیگر ورود شتاب‌زده به جنگ علیه ایران را خلاف منافع کشورش دانست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/akhbarefori/652189" target="_blank">📅 22:55 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652188">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Muq37frzlYQHtSFbjFA-u2dG8iPIu8KiHD6wTY6xplPZdlC64CdOjJgCopPU9GLuuoOkjaEAK9rxPZBLWMKHcrHQKsWEaWtU05CjDCJfBGyBhY_F5weoNOM66U3_CHuBCY9I0NIuZashMZFWkeAbBD6K-k9YIjQijStuPtsU7b7mXo4AGLx-C0SmuIsn3mwzNCiHC-90w2lnFJCnxdYFWQ2XvEPUSHr4zyW0Uf8Pj3rxhWcHTUAm8V4if_UmJi0kb1wBoLNwQz-Ywe7jcofjUPrTWlf7kxQ28sQ4jEj4eh6lgvJj_h2Xz9K2IlepdkQlp1gwM8XUtsifDon28J6gEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رأی ۵۰ در برابر ۴۹؛ سه سناتور جمهوری‌خواه مخالف جنگ با ایران شدند!
هیل:
🔹
سه سناتور جمهوری‌خواه از رهبری خود جدا شدند و به پیشبرد قطعنامه‌ای برای توقف درگیری با ایران رأی دادند.
🔹
سناتور لیزا مورکوفسکی، سوزان کالینز و رند پال و تقریباً تمام دموکرات‌های سنا در رأی‌گیری برای پیشبرد قطعنامه‌ای که به ترامپ دستور می‌دهد نیروهای مسلح را از خصومت‌ها علیه ایران خارج کند، پیوستند.
🔹
پیشنهاد لغو قطعنامه از کمیته روابط خارجی سنا همچنان با رأی ۴۹ در برابر ۵۰ شکست خورد./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/akhbarefori/652188" target="_blank">📅 22:51 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652187">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
نیویورک تایمز به نقل از مقامات آمریکایی: شرکت‌های چینی در حال مذاکره با ایران در خصوص فروش تسلیحات هستند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/akhbarefori/652187" target="_blank">📅 22:50 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652186">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
«ناوگان جهانی صمود» فردا (پنجشنبه) از شهر مرمریس ترکیه در ساحل مدیترانه، در تلاشی دوباره برای شکستن محاصره تحمیلی رژیم اسرائیل بر نوار غزه با مشارکت ۵۴ کشتی، حرکت خود را آغاز می‌کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/akhbarefori/652186" target="_blank">📅 22:43 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652185">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fc80f2a9d.mp4?token=uk61O8B_lRNT323cNJt0WdEtYDDg3WqSsxyxdz09oALKYY3L-mH9saNkTkh4Brtt9rrvWivk-9XvCV2_YjwtwzNX-My6rDE08ywfC-E0Ehw-ydQ-xkG9CzOY_hF_LJSLOyB4DO7oFfVt3prkACCRNjT7evIze0M76Ub99dNHqeVQIr59vbC1x0t2wIOa5q5Kl6keT-l7YBODGrEOnE0pgWcQmFMRJDMMx16RjbIHFaPX58XATMTPn16NK7B7WBmZWsIkyCPN-TLgmKrbkigd1V-qDDhNtDoRbLjQWxD7hN63S_zHwZkGArBvUTpxoD3oq3ow2TzGnT2IAs5E3q6DbEgh2upbf1l57GRu0bPTX6OqRpfN5WKy-VK18-5C45m-jmOXkxY4wJTYamOXjPHmnsTFl6YA1WoV2a1iS5TIB9HSlRvx1LpstM8A7ZrgBPC__y2OcPN1Fd9I1ut8Z1ru3-9lvyuPN3bTOZvHfTg6TPKXINqq5H_IcYF92iEqudHe-yjvFGzJu2QGmRFQqnUaRhspfA2N5ZQ7-rmRLArVqaeSST6fZxcz-Nw52hYr5wTSrikD9sQPCAdjclfxS1IEXEN2jJ5eYKKg26DfcVO40h6kP8JR7njVPV84y992owqg6GeeUmRpS75pDtG2tWo6-BiJE1oGrnqFRQ-fBS_EnwM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fc80f2a9d.mp4?token=uk61O8B_lRNT323cNJt0WdEtYDDg3WqSsxyxdz09oALKYY3L-mH9saNkTkh4Brtt9rrvWivk-9XvCV2_YjwtwzNX-My6rDE08ywfC-E0Ehw-ydQ-xkG9CzOY_hF_LJSLOyB4DO7oFfVt3prkACCRNjT7evIze0M76Ub99dNHqeVQIr59vbC1x0t2wIOa5q5Kl6keT-l7YBODGrEOnE0pgWcQmFMRJDMMx16RjbIHFaPX58XATMTPn16NK7B7WBmZWsIkyCPN-TLgmKrbkigd1V-qDDhNtDoRbLjQWxD7hN63S_zHwZkGArBvUTpxoD3oq3ow2TzGnT2IAs5E3q6DbEgh2upbf1l57GRu0bPTX6OqRpfN5WKy-VK18-5C45m-jmOXkxY4wJTYamOXjPHmnsTFl6YA1WoV2a1iS5TIB9HSlRvx1LpstM8A7ZrgBPC__y2OcPN1Fd9I1ut8Z1ru3-9lvyuPN3bTOZvHfTg6TPKXINqq5H_IcYF92iEqudHe-yjvFGzJu2QGmRFQqnUaRhspfA2N5ZQ7-rmRLArVqaeSST6fZxcz-Nw52hYr5wTSrikD9sQPCAdjclfxS1IEXEN2jJ5eYKKg26DfcVO40h6kP8JR7njVPV84y992owqg6GeeUmRpS75pDtG2tWo6-BiJE1oGrnqFRQ-fBS_EnwM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسین پاک، کارشناس جبهه مقاومت: امکان ندارد ایران به خاطر واسطه شدن چینی‌ها از شروطش کوتاه بیاید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/akhbarefori/652185" target="_blank">📅 22:41 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652184">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
وزیر خارجه کوبا: حمله آمریکا منجر به حمام خون خواهد شد
🔹
شهروندان کوبایی و آمریکایی کشته خواهند شد و تنها سیاستمدارانی که فرزندان و خانواده‌های خود را به جنگ نمی‌فرستند، جرات اجرای چنین سناریویی را دارند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/akhbarefori/652184" target="_blank">📅 22:40 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652183">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
حکم قصاص قاتل شهید دهقانی اجرا شد
🔹
سرهنگ دوم شاهین دهقانی دی‌ماه به شهادت رسید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/akhbarefori/652183" target="_blank">📅 22:35 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652182">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FApJDKowJpH9q0Tmco8nlq1qKYfVTU9iN2PzN7UnwgU3gX6gHRtuRE6CjAbQiGuHrfLJHEkCvKgBX6_y8-HqPNVKDjwEQv2F_4zetRmQBVj-4kL-KSfKMaE5cGLCBWOA2IDuwu-febYGEZ8rKtL2oIptV1xtBrhpJDeaSt2HghxEiqUlS8cjOIIFWTHch-o2pnRcJWy413_-fAlgE-jD5WwaZd4ZsJ9pBmNJy6LkVOA7Zpp1nbt2BM3vJdgxA8ByFHgIoF9dp9WoBUObuK6P7V0Se3V8_8aRl0jyetVjXMcd13jja0Zch4zotzth4ioPPcBw23IDZFtisJiCaMLqAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یمن: عواقب جنگ علیه ایران دامن تمام دنیا را خواهد گرفت
🔹
معاون وزیر خارجه یمن تصریح کرد حمله خصمانه علیه ایران، امنیت و ثبات منطقه و جهان را تحت الشعاع قرار داده و تداوم آن، منطقه و جهان را به جنگی خواهد کشاند که پیامدهای آن گریبانگیر همه خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/akhbarefori/652182" target="_blank">📅 22:32 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652181">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6670d6dcb3.mp4?token=NHhhe0mi3P_zckoq2OqhyRBr7lmpzyfPffgQJdhx4lqX8Zdz7yNFHVemsjCCefa3Trt-GBEX3ReEGHMbQMDKlyXV9Qh53LQwt3lGliOenHOz611kIrsGK7fnAYx27Wek5QhSu6PfBdE8Y9k94NW4HkYmRaNUZ98HetVOkG_D6DmbvsGYJ2aLzCT03QaEOwwOMip0IaRwxBjQV82mbbXXWpSN8TgtGkCZDczi7ruXgSUchkq7KYkC8ZgGauK8pBew4ATqBAqBqr56NdCBnBIt5B5KWgVasMpLH4yqNT5Ifqfs4r3TH68eBQynppcu9lXUGgOCLcfQw0SGXyW3uCZqcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6670d6dcb3.mp4?token=NHhhe0mi3P_zckoq2OqhyRBr7lmpzyfPffgQJdhx4lqX8Zdz7yNFHVemsjCCefa3Trt-GBEX3ReEGHMbQMDKlyXV9Qh53LQwt3lGliOenHOz611kIrsGK7fnAYx27Wek5QhSu6PfBdE8Y9k94NW4HkYmRaNUZ98HetVOkG_D6DmbvsGYJ2aLzCT03QaEOwwOMip0IaRwxBjQV82mbbXXWpSN8TgtGkCZDczi7ruXgSUchkq7KYkC8ZgGauK8pBew4ATqBAqBqr56NdCBnBIt5B5KWgVasMpLH4yqNT5Ifqfs4r3TH68eBQynppcu9lXUGgOCLcfQw0SGXyW3uCZqcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌های طوفانی مردم به توهم ترامپ!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/akhbarefori/652181" target="_blank">📅 22:28 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652180">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/084593e8e6.mp4?token=gy46WyZer1gwu8zbvj7wklzJJscFBZlZwPSiPVg7FH18IqP9Bu7o6uwT8Ew0c3B3Muxd-RjbjiYBzHLmKzTA0aVgV8vnv2M9w-KG_l6w9Tla8I9HdnOgi2Lha-xOwb_Hpa_x16E3V-fQQiuCTUFRKDf6g91b6Y31PBGMMwnoKX3-1Ezx6sIMiAkEbUuHShlEPSKDyg8jMzbFNumGuHE94h4og07A3kt84GG0O9w9VjR3hb2wUwD6KwZANc7Gwrod5lw3cUsKYvE6ggCRqPtPYs2Aaq0ChNnlRblK3wWKcCrwd7uLWcyw1QhvvyI2Xr_6qzfWoUinI72dUYVi2iftVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/084593e8e6.mp4?token=gy46WyZer1gwu8zbvj7wklzJJscFBZlZwPSiPVg7FH18IqP9Bu7o6uwT8Ew0c3B3Muxd-RjbjiYBzHLmKzTA0aVgV8vnv2M9w-KG_l6w9Tla8I9HdnOgi2Lha-xOwb_Hpa_x16E3V-fQQiuCTUFRKDf6g91b6Y31PBGMMwnoKX3-1Ezx6sIMiAkEbUuHShlEPSKDyg8jMzbFNumGuHE94h4og07A3kt84GG0O9w9VjR3hb2wUwD6KwZANc7Gwrod5lw3cUsKYvE6ggCRqPtPYs2Aaq0ChNnlRblK3wWKcCrwd7uLWcyw1QhvvyI2Xr_6qzfWoUinI72dUYVi2iftVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
زیباترین پادشاه ایران در مقابل هیولایی مانند محمد خان قاجار ...
نسخه کامل را اینجا ببینید
👇
https://youtu.be/IpMt8R6uBX4?si=-7JMsyhn60BXSofd
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.25K · <a href="https://t.me/akhbarefori/652180" target="_blank">📅 22:23 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652179">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e72a4aeebd.mp4?token=in8Iie36dp1BN0n3PY6oOlvbos5ubxFox4R_qPUCs7BaOuS0sWqtlPWdmQ3RRqNtXzCDijDqgmEfZtlN6NrL8ytNcxjoMAu4uxGAn8vwPnluM_xHXfkKxCOL4-Iz-TsAueYFrqDP-nkXfn5MxRlxjTgCpWlbBcmkTA1UkRT2KCjE997o2HI9bnUI54D0T4pw3hzle8D-jWqoMx4-MsF04d7vcuWIwXZhZWOI2uJYoMdCL_-NUCYnVhG_BdqeY0RbkaVuv8Y6PUYsbf2rcSZ1OOC4RV4XYWnqTY8Dms8OJ3Fc0La6lT72A3qXYZak7NoaheTAKlWExHmdGsZAlfvr84i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e72a4aeebd.mp4?token=in8Iie36dp1BN0n3PY6oOlvbos5ubxFox4R_qPUCs7BaOuS0sWqtlPWdmQ3RRqNtXzCDijDqgmEfZtlN6NrL8ytNcxjoMAu4uxGAn8vwPnluM_xHXfkKxCOL4-Iz-TsAueYFrqDP-nkXfn5MxRlxjTgCpWlbBcmkTA1UkRT2KCjE997o2HI9bnUI54D0T4pw3hzle8D-jWqoMx4-MsF04d7vcuWIwXZhZWOI2uJYoMdCL_-NUCYnVhG_BdqeY0RbkaVuv8Y6PUYsbf2rcSZ1OOC4RV4XYWnqTY8Dms8OJ3Fc0La6lT72A3qXYZak7NoaheTAKlWExHmdGsZAlfvr84i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چی این چمدون رو سنگین کرده؟!
@TV_Fori</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/akhbarefori/652179" target="_blank">📅 22:20 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652178">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o2AoVpbWvi60N0_O6NZ-f9r4bGF9zIDKOXOrFv0UUvUXr_zT1nFD9ph9SYLRu5AiAQWVsdyCbrW38MMGtOKVLqCQZChxarmWIbAACdSSPXMspB4VAjHhq_uXOlO40yFOUVUbHJ6h1Thg4A2V9r3qhMloirSABU3fhy1rpbV0jZv9xSNCZ-3b497lrgRyHRiDqz589LpyftJJ6mTLEyvL5DtBjQVAoIXskQAfqlWY5SDpqokqW9DnDX0nf4L7G1d1yIydHx-v7ZcEWO9EGJD-WqNPA7srK4Oj6E8vvVjl8dtWN5WwP6dr34ycgbf1Sy_GT2oleo_ab1Brg6CeUGrtIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محمد عباسی، قاتل شهید سرهنگ دهقانی که در اغتشاشات ۱۷ دی ماه با ضربات متعدد سلاح سرد به شهادت رسید، قصاص شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/akhbarefori/652178" target="_blank">📅 22:15 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652177">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
رسانه هندی: آمریکا جنگید، چین برد
تایمز آو ایندیا:
🔹
در حالی که آمریکا موشک‌های خود را شلیک می‌کرد و اسرائیل زیرساخت‌های ایران را هدف گرفته بود، چین بی‌سروصدا درحال برنده شدن بود.
🔹
پکن بدون کوچکترین مداخله نظامی، با محکوم کردن حملات آمریکا و اسرائیل، دفاع از دیپلماسی و تثبیت روابط انرژی با کشورهای مردد در قبال واشنگتن، جایگاه خود را به عنوان یک جایگزین آرام و قابل اعتماد تثبیت کرد.
🔹
آمریکا سرمایه دیپلماتیک خود را سوزاند، چین بدون هیچ هزینه‌ای نفوذ خود را از خلیج فارس تا اقیانوس آرام گسترش داد./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/akhbarefori/652177" target="_blank">📅 22:15 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652176">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D--FPf4f4baA4p7vVlFLo5A72Wg76-g2PxUJFnzIa14MIeuqbDrUaUMKPutESjjVuwYvtkloIkx5T1qyE5TyW6RUU9babKr3NmNafv5SK-e3aLvQ4NUANZnwEh9dcEFK4TfPBSXyoqXSR0m7gje_8NcHEQAIz4wNLILDTwnAsFlv53zLyRpviGGfQD2SFEwratJS8wJglZXosn965tan92gtWmwYef8rXoti0EOVhirqWxkhGN_IGsqmFNid8dt7lgF9y27xg-FORVteeXuc1-hOAMPS-0nA0f484ViR9MtyKwXCcXFnyMvgBrlbwZi8sf8iZ-Qx-QBcUzKYq4F9CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی ارتش: کنترل بر تنگه هرمز، دو برابر درآمدهای نفتی برای ما آورده اقتصادی خواهد داشت
🔹
امیر سرتیپ محمد اکرمی‌نیا: نظارت ما بر تنگه هرمز، هم درآمدهای سرشار اقتصادی به میزان حتی دو برابر درآمدهای نفتی برای کشورمان به همراه خواهد داشت و هم قدرت ما را در بعد سیاست خارجی تقویت می‌کند.
🔹
پس از پایان این جنگ، دیگر جایی برای عقب‌نشینی وجود نخواهد داشت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/akhbarefori/652176" target="_blank">📅 22:10 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652175">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">مراسم دعای ندبه_جلسه 48</div>
  <div class="tg-doc-extra">سخنرانی استاد رائفی پور</div>
</div>
<a href="https://t.me/akhbarefori/652175" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
مراسم دعای ندبه - جلسه چهل‌وهشتم
رائفی‌پور:
🔹
0:15:30 عاملی که آدمیت را از حیوان مجزا می کند
🔹
0:22:00 دنیا برای مؤمن مانند قفس است
🔹
0:26:15 عاقبت جامعه‌ای که در آن امربه‌معروف و نهی‌ازمنکر نباشد
🔹
0:41:00 معنای اصلی کشتی نجات بودن امام حسین(ع) چیست
🔹
0:46:50 ارزشمندی اشک بر امام حسین(ع)
🔹
0:58:50 مخفی بودن قبر مطهر حضرت علی(ع) تا زمان امام صادق(ع)
🔹
01:13:00 حضور امام زمان(عج) در روضه حضرت عباس
#دعای_ندبه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/akhbarefori/652175" target="_blank">📅 22:10 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652174">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
نشست مشترک مجمع نمایندگان استان تهران در مجلس شورای اسلامی با جانشین فرمانده سپاه پاسداران انقلاب اسلامی برگزار شد
🔹
در این نشست مسائل مربوط به استان تهران اعم از نحوه تامین انرژی، آسیب‌های ناشی از جنگ، نحوه خدمات رسانی به شهروندان، وضعیت امنیتی و سیاسی مورد بحث و بررسی قرار گرفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/akhbarefori/652174" target="_blank">📅 22:09 · 23 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
