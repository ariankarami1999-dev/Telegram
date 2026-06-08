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
<img src="https://cdn4.telesco.pe/file/jwa-aGPNbzZ3bHB-Hhx__1Av4pwuR4mBTOGMKUVXnD3aZd0dNnj4uY4FQDnzBeYn7aplP0jhUpfHIrWY85IuIl0ph8s7h9Ka9KrOulKjt_qgl4nGo9rzNwmCUOQmRMxTFdCrFMbX8tvI0kv2--qiMuKeriVBoHynElbGYS1KOsZbXOuvny7cWIHeeqLNRDoFboiuy5JjKVmcDE1RqOuuN2dp3Fz9VA8di6p3xAGBBJEPvLnzY1ZVlYrJjAIPUyIW8Q_4Mo8jiOUgI93DyfL9TmXxepE6i-HjhxWhy6l1JBoYVT4X-Adifqa5nLHPtfMk09u3oJYSs-TlqcFdopoVPQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 228K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-18 18:24:47</div>
<hr>

<div class="tg-post" id="msg-65463">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
وزیر دفاع اسرائیل، ایسرائیل کاتز:
وضعیت در ضاحیه بیروت همانند شهرک‌های شمالی است.
هر حمله‌ای به شهرک‌های شمالی منجر به حمله‌ای در ضاحیه خواهد شد.
ارتش اسرائیل به عملیات خود در لبنان علیه سازمان تروریستی حزب‌الله ادامه خواهد داد.
ما تهدیدات ایران را به‌طور کامل رد می‌کنیم. هر تلاش ایرانی برای پیوند دادن لبنان و ایران و حمله به اسرائیل با نیروی عظیمی مواجه خواهد شد، همان‌طور که دیروز اتفاق افتاد.
@News_Hut</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/news_hut/65463" target="_blank">📅 18:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65462">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3210944dde.mp4?token=LqOyMTmALf683jCigscgJDCu_hQwwxlzyH4ABGsFcmWFGEjmTC6T1iGvuEmZiYzDVC4UlWPu-plU-NuiPKGy4YXOY8osSQkD55ceXX6LNWfI8E2yHUCGerhowC0CcVISWEmeoWcbtOa2j_crnwgAoepJ9x6Oue6zIPWQKrxHCalGFIphzO0ZqcKk70Hg-mon6w2ozwBb9mZQyEtQCsSHEbZxUG0eWb6UqFnz0s88AVqaofwPO9bk6KPISQjC078fYiiKos7bNJjxIDjt1TTwhqlOAe0pUWNOv64Of1k-ccxs24__yLAm0ryPJpYQUK0_7Qomxw_ZV8LRVS3XSQJOsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3210944dde.mp4?token=LqOyMTmALf683jCigscgJDCu_hQwwxlzyH4ABGsFcmWFGEjmTC6T1iGvuEmZiYzDVC4UlWPu-plU-NuiPKGy4YXOY8osSQkD55ceXX6LNWfI8E2yHUCGerhowC0CcVISWEmeoWcbtOa2j_crnwgAoepJ9x6Oue6zIPWQKrxHCalGFIphzO0ZqcKk70Hg-mon6w2ozwBb9mZQyEtQCsSHEbZxUG0eWb6UqFnz0s88AVqaofwPO9bk6KPISQjC078fYiiKos7bNJjxIDjt1TTwhqlOAe0pUWNOv64Of1k-ccxs24__yLAm0ryPJpYQUK0_7Qomxw_ZV8LRVS3XSQJOsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ویدیو ای از اصابت پهباد به مواضع گروه های کرد در شمال عراق
@News_Hut</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/news_hut/65462" target="_blank">📅 17:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65461">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
اسرائیل هیوم از منابع: هنوز هیچ محدودیتی برای فعالیت ارتش اسرائیل در حومه جنوبی بیروت وجود ندارد
@News_Hut</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/news_hut/65461" target="_blank">📅 17:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65460">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcc72e760f.mp4?token=HGNaLrWp2NgwV02F3f2xjZU_X8AZgxhSSXKVm1m44YKz871mcs9adVF9l7Rkv-dNbIKxodv5ZLlAtHmmDfycDZMwdrQxQuN5fLSFAfnPkKfAquj6ALhK8-wiTGaCAM7lUA-mStEkCYTCQOnbwudQ6Srqcw-S0mZzwQTQMpXhl1tns_1rDDZ35KqlbYixs1SIE5t1n6zsofbCf0te4fvbhzPGwPQvKVXgd2Fdf9vgIkK-87HwBhMgFzOtv_A4rgu177sRMhn9ITLDLKdqAbJCjPmLr9MFc7zMuY201yOfrd5VqUBXeOOQ9s0iNQO3mGKj67xWVKf-PbHFZy-P7Ehtkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcc72e760f.mp4?token=HGNaLrWp2NgwV02F3f2xjZU_X8AZgxhSSXKVm1m44YKz871mcs9adVF9l7Rkv-dNbIKxodv5ZLlAtHmmDfycDZMwdrQxQuN5fLSFAfnPkKfAquj6ALhK8-wiTGaCAM7lUA-mStEkCYTCQOnbwudQ6Srqcw-S0mZzwQTQMpXhl1tns_1rDDZ35KqlbYixs1SIE5t1n6zsofbCf0te4fvbhzPGwPQvKVXgd2Fdf9vgIkK-87HwBhMgFzOtv_A4rgu177sRMhn9ITLDLKdqAbJCjPmLr9MFc7zMuY201yOfrd5VqUBXeOOQ9s0iNQO3mGKj67xWVKf-PbHFZy-P7Ehtkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ویدیویی کوتاه از حملات امروز اسرائیل به اهدافی مشخص شده در ایران
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/65460" target="_blank">📅 16:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65459">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nnWEQtCdgFYInPfBcemqse7uYgMjeDtWz8XpI3r_XuN2ZuSNV2lqq4RIf78CYFKaJs47Hw3hwKtgp80tUpdvFkmrpyLm33L_2Tp0tJeZOvW30XbRkFcljQJALwJpK4gPAd_ODz-k2w-5p68Ya8BQG612ZrZziLEteemhEU5NjGQNlthq6ISkfdmNVuVn0LO9GzLw8pQvJnqHSAPe6190a2K2sWgwze8di6rDeXlWaUy_U7W3oflBVGfqUkLMlHCMnkv0tGyB94g6b1V7RNyj-64pGCgmIASA9Jv6ujgB8nzYiOr540ykLirMMGhL33eowKR3oQg_OrmTErW0_7lKfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تصویری دیگر از جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/65459" target="_blank">📅 15:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65458">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B7kjFsOSlvudLjrQRj3O7Q0gJ4178E0E49k1R5uZ8Gou62wUX5LhpgwNLEmBeZvK6xFuQnP9N55CtphDmdvhPmWVDVMvcXOolTeIKutmVpf7GMsDFv7Yh0Gl0lwyAzLuU2ACbvKobFDZZdyzjJLfLFHuPyEM7iqs7GzxtJi9KRsGPeuTTN8huzMExzutiIBj768ooR0_-A2j-we5FucP-p3haTl2XihRXfFKdObmxlR8hmXngy-PaaxFrm6uile0T4DuaIjQ1iPwDN259Ax6w0nZzwdEbnokFNcJIL3SG2umty-mFmssSlGqK8zQIM2p__PCk_NgGilTVG2NbWGHSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش ها حاکی از حملات مجدد اسرائیل به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/65458" target="_blank">📅 15:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65457">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UMNv4ysBae8bBTI5hjpRR0ty33AXtuxNUtmAfYn40nY4BLIw4edBdJHRZWaBkQL0O2vbTvEVzFNhOCP7j4YvyaG6Cabnmm9QVVTRia_tVstmP5l7xk5rMcNLnc9uP-hvB3qt_BHvB_qNyVaDKvqGALqXbXyIazSAH9M4vLz0PIcxBznj8mNdcGBSUPldpkUgRCqTdD2aA7LZ8E_C6kyfuwl6g5tXOAzOUv_o8ESuKEEyI2JM2KIhz5Hfw96hlxLnv75tCBEy-rR4DrGbhNd7pHTlEFG3sMIXYw_xfWpwuo4Q6c0KMQS_gn4qdZFfiMqvrIYkcPTn4ULJH7wQTn1bHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
صداوسیما پایان درگیری‌های دیشب و صبح امروز رو رسما اعلام کرد
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/65457" target="_blank">📅 15:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65456">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🇮🇷
فرماندهی قرارگاه خاتم الانبیا:توقف عملیات نیروهای مسلح را اعلام می کند. با تاکید بر اینکه در صورت ادامه حملات و اقدامات تجاوزکارانه از جمله در جنوب لبنان، اقدامات قوی‌تر، خشن‌تر و قاطع‌تر از گذشته در راه است
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/65456" target="_blank">📅 15:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65452">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VoltcB2dRwVE0_h56r2I2vudF2mFPSxNUm1pnf00z5syucIxtDMsQoj9p0h7Z190ofC4I4LTV5GITIvfDQp7g5gq0pzsrsd4CmNB4zV2BVNzqKesxtXqhgNLIzNIIo6yiD0fq1C67jno5oylWwGoIkKxilY4RH0dW52GBt-SoWepOxY1iuzQHI3NE-ifRuKMN0zgv4rMbabM4Pcnqzqzk1QaXexdPxYllh842NAD39WOas_xq_xM-oAKNbin_llIgNBCWP67WiwF7T3QfRLWUbedZckgqe9iMvKAx5VCD4SPp_QqG_Jf1dDE_GFONBuceu0bZUS3IQFcqX_l9xiSEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FN22t3xj6yzPBzLB93OhDnAb29rwZmhJMHSB609aXahQ67hG4de6hjQ5SsDI_2PKz3hnD_FU_po2yTUWek7RaWmhJaZjMuGGh3fTTPkDaygcucWxVNr9cJX7Dx034yqZzRRWDyOOd5D0dZ56rdYTnHpzrluOz61T9FOwKONhhPHNHzN2YHEM_HN5BaiR3F85_nsmj_4hxM5PJ5AJTgd6LbJRAQuskBaLnN_ZP17PcKuz2SdpLg11Do1DUCqz3qGG1hhcN5iu8ZhN_VwNJ10J2zgcVWwOsf9g940baFmLvv7F3FdPGZ4jXpJ83uiGmS2FVS23bbLOPV1hSr_jh-k2TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kjAzZ-qn0i08yO5pcXCKk8XPg8r5Hvi_pv0KyncpfSVo1Cw2lOTfwteJZr765samUOlp28LbJOT33v9HoEngquS8UayJS1fD6rSBhzra-6S7mEf4BhJr-Q6Jta0XM4KcplEEi6T0S4hZ3k383U5Mu8RGsM-0w-VZFwWzud4gnpjzsdAXQQ77-91v1Lse85TBUasJqD0Y8tB2ZqucoGl9oQgkNms34Y5hfaLCqVNpZc8gIChC0axfXc09LwQpGbfR0sy9Hs0m1HLM5WFQasCFUUCPQm82ILREBzeZxEe11dA_GaOA7uQLd-LkiS4meGnqxUtlpbAb4Hf13SChB5wGlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V0wAoZrZx-rsCyftKRq66dscVN67uix2mmx2xJLcnxkXbybxi2lA0bNfu_eOTafl6cW_fRAATR-nrRhqJqgD1jM8-hMHMkYrQdeC7OhfPj_8QZaNjEqObVnBTEsLk64yxQpkkaw66QuZNgrjC-xEuFFdExD6Vykz6Q9Hf1LpyvORsiZ4nQ2yFBTxQFBBKnm741FGk7qhHe41aGqn3XmBSSM7g3NFlSN4RTWxtB145_0KdmWxouemYacVQZQ9xCB6_nokIq9gfUdZDmOZkD63yFculVqonKSxd0kjF5iqivWfaJxPc5ENpLRZtm2Gzr3uWRaPu9skEGm-rVXD9MKw8Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عکاس
اسرائیلی
؛ رفته کنار یه پوستر موشک ایرانی که تو اریحا فرو رفته، وایساده و عکس گرفته
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/65452" target="_blank">📅 14:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65451">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗱𝗺𝗶𝗻 VPN</strong></div>
<div class="tg-text">سایت های شرطبندی به دنبال ترورش هستن ، به عشق مردم داره میگاعشون
⚡
https://t.me/+9ztzXKxhZkJhZTlk</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/65451" target="_blank">📅 14:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65450">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗱𝗺𝗶𝗻 VPN</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sf7gLoue2fl_hMpIhShAdDhetERg00nT_ylh5E21oeurHPvqK-Kq8_8m6v_Uxo3muWR8Y3yJ8Sevy2mq6P9nSeVEUQrUJFZnXP6bklz0UBCWJrml8Z-0NZEO57ydU4WHSyPyt5VWUq6tBZLAyS6Bx7810K9sFr47hN6QFpfxoaq3Zs_K5j3rIvfadyk97K9lEQfsK_u-AIpJ_Fkpt4Ec73CzDXnICDMnIiocxZ5l5Nb4uqaJvxsgiZfokXnobyI-iAB4_gkGy9hT96d9wnmtwMaNDMEWjjJ9SkK93vIn2Lyehb1v6_aOUiKK277DrSfmnqMZEFjG9uIOXEIHaHqS6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبانی
🆘
کامل در لینک زیر باز شده است، برای دریافت آن کلیک کنید و عضو شوید
👇
👇
https://t.me/+9ztzXKxhZkJhZTlk
https://t.me/+9ztzXKxhZkJhZTlk
https://t.me/+9ztzXKxhZkJhZTlk
1 دقیقه لینک را لغو می کنم
❌
❌
❌
سریع بپیوندید
🖱
سریع بپیوندید
🎧
https://t.me/+9ztzXKxhZkJhZTlk</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/65450" target="_blank">📅 14:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65449">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XD8cYoM2OEQ7nlgB0WI-GkTQ65gO-N_aVHncI7c98Bker6RQSOk1hDIHLDzhGPlvOXA4vDqAUTwYFB3qKWtonkPb8Qt83RCNOZsROXMnmjJjjnPvJwsNPkXUc8vQl0z_R5oMmNyFoC73V1zasOyxsHcN3ypo1w3P9OE1C5VGaKllp_em2tVsrLNXPHgM_RUpNl-iz6d75QVeTNANjb_7ZzbVxK4t76s2W0syXmqTLkyrStnJoqch5Aa2hieS9fqzDn3FOhYAVju1GPYbXCf0dTuzBEt6c1jVNBkBzn8_Yb-TJr7i3CHt2Uwcot3Zjxi94G6xyYu8L67_9lHmqM8bBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ:هر دو طرف، اسرائیل و ایران، به دنبال برقراری آتش‌بس فوری هستند!
مذاکرات نهایی درباره «صلح» در حال پیشرفت است، مشروط بر اینکه جهل یا حماقت مانع آن نشود.
محاصره با قوت خود باقی خواهد ماند و با قدرت کامل اجرا می‌شود، تا زمانی که «توافق نهایی» حاصل شود.
اوضاع باید سریع پیش برود. از توجه شما به این موضوع سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/65449" target="_blank">📅 14:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65448">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
یک کشتی هندی در دریای عمان هدف قرار گرفت و دچار آتش‌سوزی شد
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/65448" target="_blank">📅 13:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65447">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cty0FMP1N6CqCSDjz4dz6Do3tduzTItGQNUypcj7QzwhkTjBLVlmcjtFKlNPE0v_daIrrQ5YEv4jGBYBPzjbevyRdpBklSO3hBTiOXtfxm3t7231glP33mTjhnKE_y8WQ-kc9wMclzRfCTKQykAgy09y8jlZH_ZuCoruZJK3XgfXifjL3f5_fcWbV33ywZ5XS3R19Vs8B9WZqQPE1JvgFFm3FN3tZc0oe-POIuHVjjGg_tC8vmRsemzdLP3xdKASevuwWWg7I46-4gdTLmgBKeTzEtsWNSj2i8WQZra3V-XVT-CVWpwjezi0hokR8VriOY6IkTzWfXjxV_j3OvTkKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🚨
دیلی میل| یک فوتبالیست بین‌المللی متهم شده که در یک هتل پنج‌ستاره در ترکیه تلاش کرده یک دختر ۱۴ ساله بریتانیایی را برای «بغل کردن» به پشت یک پرچین ببرد. پدر این دختر در گفت‌وگو با دیلی‌میل گفت که دخترش پس از این اتفاق دچار وحشت شده و در حالی که اشک می‌ریخته با خانواده تماس گرفته است. این حادثه زمانی رخ داد که او همراه خواهر ۱۰ ساله‌اش کنار استخر بود و والدینش حضور نداشتند. دختر ۱۴ ساله که از دیدن یک چهره مشهور هیجان‌زده شده بود، از بازیکن درخواست عکس کرد. پس از گرفتن عکس، بازیکن تلفن او را گرفت، اطلاعات اینستاگرام خود را وارد کرد و از طریق حساب دختر برای خودش پیام فرستاد تا ارتباط برقرار شود. به گفته دختر، پس از آنکه او سن خود را اعلام کرد، فوتبالیست او را هات خطاب کرد و درخواست بغل کردن داد. وقتی دختر مخالفت کرد، بازیکن اصرار کرد و از او خواست به پشت یک پرچین برود؛ جایی که به گفته او هیچ‌کس نمی‌توانست آن‌ها را ببیند. دختر که ترسیده بود، به او گفت پدرش در راه است. به گفته خانواده، بازیکن پس از شنیدن این موضوع به سمت دیگر استخر رفت و خود را پنهان کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/65447" target="_blank">📅 13:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65446">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
اخبار جنگو تو چنل دوممون پوشش میدیم عضو باشید
😉
✌🏼
@Futball
@Futball
@Futball
@Futball</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/65446" target="_blank">📅 13:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65445">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kqhmfxynPMIWZ4a8DdPnvsqbEN05LNLI3iLBOgvQBnOTCvUIyMu5PmXr37l4U3w6pM0omKXJz85S8VdhxILxVZ4mb9XgHhH3x7sGw_2DhtrZ3Jws9ucIzaxLJ7KOIrN9Iq2boLJEM_am0PesFpTGuH1tUaZdE_jjs79JkqoOYf-P0CgPkUv6m6__JDAFbzaZq-a1G56AMxHsHZcNLGdZzCuITrJ7EO6anU5EHg9C5ICkgrlijNZQJOOjs4k4qEopeDGdv4iNu3LaiNmDYrY-_GQAvljBTBIzDzAv2zml4Zla8-Y0T0bmqcaY936H6XbJr57x23vN4gNNgw3f9fu4IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ: اسرائیل و ایران باید فوراً «شلیک» را متوقف کنند
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/65445" target="_blank">📅 13:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65444">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
مارکو روبیو:فقط کشورهای احمق وقتی به آنها شلیک می‌شود پاسخ نمی‌دهند
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/65444" target="_blank">📅 13:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65443">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🇮🇱
منابع اسرائیلی: حملات دیشب و امروز کاملا با اختیار و بدون دخالت نظر آمریکا بوده اما سنتکام در رهگیری موشک‌های ایرانی کمک داده
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/65443" target="_blank">📅 12:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65442">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8c5e38e196.mp4?token=lBVHEDHcMKotLLANHAUsuBKqjV75zInL1d2cfzFksy05_T03D8lp1wugs7aDe6wZNwAbq9ie67MI4-eRSZd3SMeK8ndcY9c6UjmYr7-9gSz-iS6q0yyq1Z8tJaVQwNQgEJINnPRyDXlNmgcapgnP6l4F8KYwIoWxn564ZLQAgDg0PjAX7apIn_c8OKbIXklLYBDIWZK_vVG989j5dJ12OIAR1GZjiOtLEdsKK29lPkkKMjlu1c1ylsTPDZbgRFdcOa3ZqkNdOBJbfTrK7wMl0oh83E0qJ5OvhfFCf2Fhn4rtI4Hf-tZ2IH4OKXqTa0UDVvEG6bt3Jatf-tJ3htQgvA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8c5e38e196.mp4?token=lBVHEDHcMKotLLANHAUsuBKqjV75zInL1d2cfzFksy05_T03D8lp1wugs7aDe6wZNwAbq9ie67MI4-eRSZd3SMeK8ndcY9c6UjmYr7-9gSz-iS6q0yyq1Z8tJaVQwNQgEJINnPRyDXlNmgcapgnP6l4F8KYwIoWxn564ZLQAgDg0PjAX7apIn_c8OKbIXklLYBDIWZK_vVG989j5dJ12OIAR1GZjiOtLEdsKK29lPkkKMjlu1c1ylsTPDZbgRFdcOa3ZqkNdOBJbfTrK7wMl0oh83E0qJ5OvhfFCf2Fhn4rtI4Hf-tZ2IH4OKXqTa0UDVvEG6bt3Jatf-tJ3htQgvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
‼️
‼️
‼️
بدون شرح:
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/65442" target="_blank">📅 12:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65441">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebb70e7631.mp4?token=rHoGH6F9KI7mPsjkWaMvjbX10xQBNOGY0nQ6QkfjtqCfValhLVqry_dCGaZpix9sml5byiFKxc0K4jeDO02OgSqUa51Frc_FH0nDsD_VtS-be6vPS-QOuw8dEcHDf4RDXTqTXrNPYtagHxO61qefE-s1GKuzJQhJbqJv6947JgRMGLSVJfJovzkSMdMpjYJ4NwxFdurzUd77G0XITJG8k8Bz3mpvIy2GtBSdUcbI4EIgJ5KlpaXtz2fV3eqU1bJ-gyPvw4KT0stZIKt0UHXn1snXwRhziXsp85DZqiYK9s7riVpNFzNje0aitFCSczmUO5Z656FaoKDxlJngXjbDw0lGEVOD-vWu4OeDs1tX7WEmCuPtaCRu3u20o3vNCyGYMm-cln_yIefPLxkClHgPWNq5G2J-z1TaAINEjAwzLg3oLcpjjD98UaHAfcY3pceTsxYeRG1I3rAkUY47pQU3gTVm4Gsnp4HvatyHlssamY5ZcQ9poCr-Vlxs8uj5wE12MNgLPTyYx33X0tTpoF6h1_hsCKq7qG2Oi29OQvpuKsa2f5_y41XAPHC1JDhi3DjOI9aiL9rUUkyk5iLa52MC8aROk-aJL-ORKn5sQUcPpqx24WRLwXs09756uNl-h9qaG-tETVDypWuWt4vzsU73BGDbnfec0nZFLZemAwPmVI0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebb70e7631.mp4?token=rHoGH6F9KI7mPsjkWaMvjbX10xQBNOGY0nQ6QkfjtqCfValhLVqry_dCGaZpix9sml5byiFKxc0K4jeDO02OgSqUa51Frc_FH0nDsD_VtS-be6vPS-QOuw8dEcHDf4RDXTqTXrNPYtagHxO61qefE-s1GKuzJQhJbqJv6947JgRMGLSVJfJovzkSMdMpjYJ4NwxFdurzUd77G0XITJG8k8Bz3mpvIy2GtBSdUcbI4EIgJ5KlpaXtz2fV3eqU1bJ-gyPvw4KT0stZIKt0UHXn1snXwRhziXsp85DZqiYK9s7riVpNFzNje0aitFCSczmUO5Z656FaoKDxlJngXjbDw0lGEVOD-vWu4OeDs1tX7WEmCuPtaCRu3u20o3vNCyGYMm-cln_yIefPLxkClHgPWNq5G2J-z1TaAINEjAwzLg3oLcpjjD98UaHAfcY3pceTsxYeRG1I3rAkUY47pQU3gTVm4Gsnp4HvatyHlssamY5ZcQ9poCr-Vlxs8uj5wE12MNgLPTyYx33X0tTpoF6h1_hsCKq7qG2Oi29OQvpuKsa2f5_y41XAPHC1JDhi3DjOI9aiL9rUUkyk5iLa52MC8aROk-aJL-ORKn5sQUcPpqx24WRLwXs09756uNl-h9qaG-tETVDypWuWt4vzsU73BGDbnfec0nZFLZemAwPmVI0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
🇮🇷
حمله شدید پزشکیان به رسانه دیکتاتوری جبلی
: صداوسیما هر روز شعار می‌دهد اما باید واقعیت را هم بگوید
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/65441" target="_blank">📅 12:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65440">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65440" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/65440" target="_blank">📅 12:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65439">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pmhkZW7JUc1y6LFWal6SvHPBUK_QqzL8IOfpoEnYsLaNqqpvx7zYfAZinMmbaSVWqUyxtGun69WO5w09Lo_SBNuj_mhxkRzvwZp1QNa93Uvv8SW852V4qPV_AgSkR9De5ylNK84tNggG66y1KlqwS0RhCx1EkMlzBl7ZVGsVeD5gBK6rHon3DMK8yiIeBfNTbYV18kuXYvhC9f8tyhHszHStVVZWcYdA_w_KIY2_unt_0ZtlDxUZREOgiajcr8i1c5KtDRxTKRXWHvixLjaSq06hoFTbaPxfuaZlRYo3dPlZm87cxEwl-DIVKvalDjIDyX88RVGIa0hmr6xoDGx5xA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/65439" target="_blank">📅 12:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65438">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🇮🇷
خبرگزاری‌فارس: سپاه دیشب در حملات خودش از آخرین نسل موشک‌های خیبرشکن استفاده کرده و تونسته تلفات خیلی خوبی از دشمن بگیره!
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/65438" target="_blank">📅 12:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65437">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8792984a2f.mov?token=tl7T0cq1VHB3nb81XKFClP0-jR4be1hoSCrftPuX-rBHOzDiTq0dhphA3ivFuqsz2jWLGOCgnDVAvpXqaBy9m5K8E9HtuCHzU2qKdiP-5iq4oxSu-bPljPCQT5fhF5AkDgqOITG7V6BULWKFEHMMOPE88zc_m49LmB3gzi95lmvbO2iR7ZO5gXPWzGjcYkf4ApJk4FvFUJbW01ajHNdssiyb7O9rJmTUyX7EIfKReH0fo0qzfl-_v7b5-Cpl4dxZbze9r13B0gW5bKTh33aPI_gxYsPIOYvH5d3OLxN9N-FXj2nusHrk4CHviFHOv8x6Hgo4DBGc35cDZeZ8hnyIunnKkkHdLPNbLCyu_BVyFR8GpfiQXIVvI6dxFrVlhsUXjKgww6XTJ8yXJbq98uRc4K0gTDaFSRoubLtTfuhWPr5KreodO7r9uFM07jx5zXxu1-vYKLSvbffrb4Yt-jpZCQYWt9JQQQ8ZEacqSGDh0QIsdSXUsOMvW-OkXkf9Hep9fSazjKalWyZxtCoAgaKBtLdbLQKt61JV_DEtiK3IjU_p0EAqsl_nbCTwljDPeKQ_am-DI1tSl39PRCh5-CUJTYtky3ksjvH2lixF0GyJ_hI2vM25xTQCf0TWDL43JZMNgB0rdVkqSKiSSHyRRKoJ2XUGftFjmCCccmu1pcKQVZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8792984a2f.mov?token=tl7T0cq1VHB3nb81XKFClP0-jR4be1hoSCrftPuX-rBHOzDiTq0dhphA3ivFuqsz2jWLGOCgnDVAvpXqaBy9m5K8E9HtuCHzU2qKdiP-5iq4oxSu-bPljPCQT5fhF5AkDgqOITG7V6BULWKFEHMMOPE88zc_m49LmB3gzi95lmvbO2iR7ZO5gXPWzGjcYkf4ApJk4FvFUJbW01ajHNdssiyb7O9rJmTUyX7EIfKReH0fo0qzfl-_v7b5-Cpl4dxZbze9r13B0gW5bKTh33aPI_gxYsPIOYvH5d3OLxN9N-FXj2nusHrk4CHviFHOv8x6Hgo4DBGc35cDZeZ8hnyIunnKkkHdLPNbLCyu_BVyFR8GpfiQXIVvI6dxFrVlhsUXjKgww6XTJ8yXJbq98uRc4K0gTDaFSRoubLtTfuhWPr5KreodO7r9uFM07jx5zXxu1-vYKLSvbffrb4Yt-jpZCQYWt9JQQQ8ZEacqSGDh0QIsdSXUsOMvW-OkXkf9Hep9fSazjKalWyZxtCoAgaKBtLdbLQKt61JV_DEtiK3IjU_p0EAqsl_nbCTwljDPeKQ_am-DI1tSl39PRCh5-CUJTYtky3ksjvH2lixF0GyJ_hI2vM25xTQCf0TWDL43JZMNgB0rdVkqSKiSSHyRRKoJ2XUGftFjmCCccmu1pcKQVZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
فیلم دوربین مداربسته از لحظه حمله‌ور شدن الهه و شهربانو منصوریان به حوزه ریاست فدراسیون ووشو و شکستن دوربین مداربسته و درب اتاق رئیس برای ورود به اتاق ریاست
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/65437" target="_blank">📅 12:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65436">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b744fd7fb3.mp4?token=FfXwfpeykLoe1J0hrQ2zpB2fbAelGKKWUmcWwaufouWMdNwjEiUEzGbLE7dCDc8Iyo7xEMrp_tP2U1gXLirHn60HvUwTw1L-tMVDmlCaQCacGdMGBo2uoGPrIB_TKPbo0BYZtkB-UKHGNGOjlhErfrlJ2tpC8mpih9SVMbsH5dgStF5n2jrVBrGXhBiv2MfNJN9HQvy8s1J2D9f-1Gc26lvcIYA-0NTvOeLa6cZaZNRyxGJ2wb-HoE86EyupQ2uyeaoPd5550qcngQCs9AwefvE2oHB5Cz19hvIwt2GDiUztp_4izPU0-WfDTOVuQY54BiJxdyHm-pODyHOdSgmwLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b744fd7fb3.mp4?token=FfXwfpeykLoe1J0hrQ2zpB2fbAelGKKWUmcWwaufouWMdNwjEiUEzGbLE7dCDc8Iyo7xEMrp_tP2U1gXLirHn60HvUwTw1L-tMVDmlCaQCacGdMGBo2uoGPrIB_TKPbo0BYZtkB-UKHGNGOjlhErfrlJ2tpC8mpih9SVMbsH5dgStF5n2jrVBrGXhBiv2MfNJN9HQvy8s1J2D9f-1Gc26lvcIYA-0NTvOeLa6cZaZNRyxGJ2wb-HoE86EyupQ2uyeaoPd5550qcngQCs9AwefvE2oHB5Cz19hvIwt2GDiUztp_4izPU0-WfDTOVuQY54BiJxdyHm-pODyHOdSgmwLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ویدیو منتشر شده منتسب به آسمان یزد
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/65436" target="_blank">📅 12:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65435">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S-At89nvIebyUt6P2YsI76aZV5qsd4AhzZ6CwoIyLsliKYxArahI4KmSWz7ehWHCYuUKtOfl6i7N6rabB74KLN5HkjWK4mqgzkYcMINjz67bWxMB72MAwMoKVvTwwMYQx5YdHxJ2RJDhaS0uxBVPPsMa7aEohy3dOTALmFmTjcbBFmpNbBOGhX6glloQlLO5K8hziNM0OAfKT8DX5MGD2cBK4ugR2ZNClaB2jnPx0ULUiHte_ZJ66SZEcy6nL_GncfqLs9jKfOEAWrvgIwZrjEDwiZX5TXtHVzXKsLsAGwQxasSxcaio3Y6tOGy3L061_1160aUl-mJNxxlFqvRs2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
مشاهده ستون‌های دود از شرق تهران
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/65435" target="_blank">📅 12:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65434">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
گزارش رسانه های اسرائیلی از هدف قرار گرفتن فرودگاه شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/65434" target="_blank">📅 12:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65433">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
🚨
وزیر جنگ اسرائیل: حمله به‌ نقاط مختلف ایران را آغاز کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/news_hut/65433" target="_blank">📅 11:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65432">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
صدای انفجار در اصفهان و همدان
@News_Hut</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/news_hut/65432" target="_blank">📅 11:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65431">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
گزارش ها از حمله به دانشگاه هوا فضای عاشورا
@News_Hut</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/news_hut/65431" target="_blank">📅 11:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65430">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
غرب تهران و کرج گزارش انفجار
@News_Hut</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/news_hut/65430" target="_blank">📅 11:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65429">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
صدای انفجار های شدید در تهران
@News_Hut</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/news_hut/65429" target="_blank">📅 11:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65428">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8514d8db20.mp4?token=cD6TkLreM_wy_CQGes_lpDXAfFHeX6Jt-fvUMsBQ5yW0lxFBhcOoZh5rr46lC40y5I5vcTsCZ827mCKND00ft-sUJWqrNKYhOzTX_XEh7LboTSwtdGZ_fdzlp11MNp9apc-5G_qOhe5rrSOqIHPU-mVCjL9qR3CNgR6iMkKUrzpQtKZrmEfCrX6NNjLkYCBmpGdaWqESlVjkRxJCWQrkHNLMvIZ0eBy48CSEJzuYot0b5FDoFLsgwA9e5L0MeSf_tAZ5EXuvfPkTCKCTMaljBeKSh6QItlQ-MdUqH5x4y6qxGYBWYY3orV8wC2ta0rUIXD9TgBkfbIV3MrjbiK2CJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8514d8db20.mp4?token=cD6TkLreM_wy_CQGes_lpDXAfFHeX6Jt-fvUMsBQ5yW0lxFBhcOoZh5rr46lC40y5I5vcTsCZ827mCKND00ft-sUJWqrNKYhOzTX_XEh7LboTSwtdGZ_fdzlp11MNp9apc-5G_qOhe5rrSOqIHPU-mVCjL9qR3CNgR6iMkKUrzpQtKZrmEfCrX6NNjLkYCBmpGdaWqESlVjkRxJCWQrkHNLMvIZ0eBy48CSEJzuYot0b5FDoFLsgwA9e5L0MeSf_tAZ5EXuvfPkTCKCTMaljBeKSh6QItlQ-MdUqH5x4y6qxGYBWYY3orV8wC2ta0rUIXD9TgBkfbIV3MrjbiK2CJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
در ادامه اوضاع بگایی آسیا، تو فیلیپین زلزله 8.2 ریشتری اومده و تلفات نسبتا زیادی تا الان داده!!
@News_Hut</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/news_hut/65428" target="_blank">📅 10:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65427">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b691d50ba0.mp4?token=TNBOQLvNg5Mo9ZhSM-p5tR7PswPpuJyfQY-D4DYZlZ1Yh7w6MU3hSJW_Mg9OvoPqaLM-hIaX9ETW-SDYkI0YyqARIZwqU-AJXgmf8kkh5lwm7UltSHNueuncalZ0VOD_f0d0PCE-ZxchfyoVbJLTTGcXxRNe3tfM_n6hNYVB0t0GYutUap6lRN35oAhHEZ5taFUHHa8nlnzeFOCj4yYOdRI8w0J1y99XKBOKl7jQlg0YIb6K9yn6ZGNqnbXDAkpy-qTyPeIy-yNFHRl5A7dZ27MKX9so07cmEJQaWpnm_fTFT6pW0Jfq6fXeOKWNKgqZRCm3sCrevrCyPA30R4WL-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b691d50ba0.mp4?token=TNBOQLvNg5Mo9ZhSM-p5tR7PswPpuJyfQY-D4DYZlZ1Yh7w6MU3hSJW_Mg9OvoPqaLM-hIaX9ETW-SDYkI0YyqARIZwqU-AJXgmf8kkh5lwm7UltSHNueuncalZ0VOD_f0d0PCE-ZxchfyoVbJLTTGcXxRNe3tfM_n6hNYVB0t0GYutUap6lRN35oAhHEZ5taFUHHa8nlnzeFOCj4yYOdRI8w0J1y99XKBOKl7jQlg0YIb6K9yn6ZGNqnbXDAkpy-qTyPeIy-yNFHRl5A7dZ27MKX9so07cmEJQaWpnm_fTFT6pW0Jfq6fXeOKWNKgqZRCm3sCrevrCyPA30R4WL-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
لحظه اعلام خبر حمله موشکی به اسرائیل و واکنش هواداران جمهوری اسلامی
@News_Hut</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/news_hut/65427" target="_blank">📅 10:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65426">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
فرودگاه‌های غرب ایران کامل تعطیل شد
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/65426" target="_blank">📅 10:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65425">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ANelUz2_GHLvqmljK_HKsCCGpLMI54CP1bt81uPs3tVUOA7K1HcORy3dCS5fvs1dsZv5dwGfr7N4Sy0dZFqRq1mcAwJEMfGibpKy3FOPoH5CY26FCVkRqYtwCY_WV787Wyhdzg5s1F3TglbmLwKqzVFOWJpsRhiHQ9rQqBJttGW9fzjztxamslQwDp2KjD2nvhAgqq8bhrAVJtI9vouCZ66w7JSCNsU0jZMeQ028tN0vovjbHmA-LvI5j1Eq4aStp8MriW1Oc-6fTw4D4_Kmeaq23W5DzaNvCbQCGwqJNvMPwQckyWII4wQm9PeZzzETpEnUxl3EvJQeI1DxFFNVgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
توییت ایلان ماسک درمورد ایران: « تنگه هرمز به نام اهورا مزدا از زرتشتیان نام گذاری شده »
@News_Hut</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/news_hut/65425" target="_blank">📅 10:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65424">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jaSTTQyrW5rHOBsdzQ82RaLgLhuRhVgcqV5GPtdBz27CWY0k7TQR2xQD1bUqR8pdru8m7oMLG5pZW3SXdQJokTDaCtVRXHzxy9cGWgnjGCND_1P18TCqSqVUQX7SHdhXavDssOZ22y_BAcQ4Y9F019HmAXMZ5OcQSZYzEV27udMPRw4lzFgu7AgtMGdDeTzNZtgeUb2EUQUdaqq3gecwPyQuuqiwxYNsmLDxnTGW3CDwUMccJsDAVtGjTDzQxW5nldfyJ_tbfcoQ0ueEtMnnTpuku_yegSKxVdzMfBq-nyVZTGk9ZqO9KUMXLmzBc2ZFKjvyCaM2aXE5P2zSbZWlJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇱
حمله موشکی سپاه به مرکز انرژی اسرائیل در حیفا و ناصره
@News_Hut</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/news_hut/65424" target="_blank">📅 10:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65423">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f56aa95f90.mp4?token=Z7qq56yE6roCZ-wBHB72QTD3boxo03CLhJ_o-36LpDjV32oTQ03N8YHEyAyIZxyXI9oLSdmDb56DdrW7L-K4yJu3q6iCN6vFtMYglXcFg0_Xun5BUxv-Mqn7Zn6lP-ng8cj3FEPEIWZrZ8lyKltJFYFCnshRsvbgwRI8lcYwxmn92CFmp34yXLbKYzhaidnIZFai69_2Vegen6b7g1RsM7yeNtLUq3HEhkmDuxlwr0SEYBbiJq9beGiXICQEtIWSpQ0OG7WkIJzbgA2MfX8xET_Tm92dFfCP-0ddgudBQNAP0MQez5V0xzkaicWT5gbjAkkS3AmmdmSPCpHP33ri7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f56aa95f90.mp4?token=Z7qq56yE6roCZ-wBHB72QTD3boxo03CLhJ_o-36LpDjV32oTQ03N8YHEyAyIZxyXI9oLSdmDb56DdrW7L-K4yJu3q6iCN6vFtMYglXcFg0_Xun5BUxv-Mqn7Zn6lP-ng8cj3FEPEIWZrZ8lyKltJFYFCnshRsvbgwRI8lcYwxmn92CFmp34yXLbKYzhaidnIZFai69_2Vegen6b7g1RsM7yeNtLUq3HEhkmDuxlwr0SEYBbiJq9beGiXICQEtIWSpQ0OG7WkIJzbgA2MfX8xET_Tm92dFfCP-0ddgudBQNAP0MQez5V0xzkaicWT5gbjAkkS3AmmdmSPCpHP33ri7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
تصاویری از پرتاب موشک از ایران لحظاتی پیش
@News_Hut</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/news_hut/65423" target="_blank">📅 10:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65422">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🚨
با اعلام انصارالله یمن تنگه باب‌المندب بسته شد
@News_Hut</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/news_hut/65422" target="_blank">📅 10:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65421">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
🚨
اسرائیل هیوم:
یک پایگاه آمریکایی در عربستان سعودی هدف قرار گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/news_hut/65421" target="_blank">📅 10:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65420">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f9d994e5a.mp4?token=op9ZWv8s3362TZj4mQ_4QQslXirncmIfQagQsnJpHoofI6XNU0ZHCHl0dHFtmfYkZP8nn-kThG6h42TZTy66sPiEktSmWhV_vE34ETwTPCE9NqREwKP7V_9SQnjWmRn38S78mz8ng9c0dsYj8UxavuAaIai4Hq6PVUDp3Y-ArRxJAymNrngU75YHHqEAL9kwyf2cwG8glsSQalD4EM3dtV3NJdaNng4hiTUUjq1OwR16h7zLBSh5EC3tJcNb4ejBNagus1RPt-aQ399P_PrW7qlbCjmIfQuEASkhSKMQBoZnuLTroJepRP_czv1LF938nfY-RDqTmM25WdxVnMIuEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f9d994e5a.mp4?token=op9ZWv8s3362TZj4mQ_4QQslXirncmIfQagQsnJpHoofI6XNU0ZHCHl0dHFtmfYkZP8nn-kThG6h42TZTy66sPiEktSmWhV_vE34ETwTPCE9NqREwKP7V_9SQnjWmRn38S78mz8ng9c0dsYj8UxavuAaIai4Hq6PVUDp3Y-ArRxJAymNrngU75YHHqEAL9kwyf2cwG8glsSQalD4EM3dtV3NJdaNng4hiTUUjq1OwR16h7zLBSh5EC3tJcNb4ejBNagus1RPt-aQ399P_PrW7qlbCjmIfQuEASkhSKMQBoZnuLTroJepRP_czv1LF938nfY-RDqTmM25WdxVnMIuEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
با تایید اسرائیل، پتروشیمی ماهشهر مورد حمله قرار گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/news_hut/65420" target="_blank">📅 08:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65419">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
🚨
پرتاب موشک از ارومیه ، لرستان و اصفهان به سمت اسرائیل
@News_Hut</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/news_hut/65419" target="_blank">📅 07:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65418">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فووووووووری؛ انصارالله یمن از آغاز حملات به اسرائیل خبر داد  @News_Hut</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/news_hut/65418" target="_blank">📅 06:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65417">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فووووووووری
؛ انصارالله یمن از آغاز حملات به اسرائیل خبر داد
@News_Hut</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/news_hut/65417" target="_blank">📅 06:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65415">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">❌
با توجه به شرایط خاص مذاکراتی و همچنین آغاز جام‌جهانی، حملات ادامه دار نخواهد بود  @News_Hut</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/news_hut/65415" target="_blank">📅 05:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65414">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">❌
با توجه به شرایط خاص مذاکراتی و همچنین آغاز جام‌جهانی، حملات ادامه دار نخواهد بود
@News_Hut</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/news_hut/65414" target="_blank">📅 05:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65413">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b906cb3be.mp4?token=m_vG9XLGhJ6vHZreeZLBF_uJUFLv2XzeHuPO1cy2D-ISba-NGBvwtGwE8ntdAvg-TBkUs29nipvukjlqxB0xRNx8gxPvGpqP1-BJs-UjpSH5Xhy4-6TcW5MfdtM-l_RGypqptmIk_i100CWhirGARiKcNK8MsOFOy4UTnnEzXqsVwRgg1XcNtFNpsLSLtS2Pj1vhhmb3Hi0BJIMhYbJET2Rayt6j_7Krlb98BV-zUVN_zuA0xjil-alIp0tz3Slsq6I-94PLnWpWwCntfdd_LqoAA6o0nbV0tBJrLDpi2YZ-_S-oX7OcJjLMISZAyLdKeEmGbWnVvf3fXzreFEQavw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b906cb3be.mp4?token=m_vG9XLGhJ6vHZreeZLBF_uJUFLv2XzeHuPO1cy2D-ISba-NGBvwtGwE8ntdAvg-TBkUs29nipvukjlqxB0xRNx8gxPvGpqP1-BJs-UjpSH5Xhy4-6TcW5MfdtM-l_RGypqptmIk_i100CWhirGARiKcNK8MsOFOy4UTnnEzXqsVwRgg1XcNtFNpsLSLtS2Pj1vhhmb3Hi0BJIMhYbJET2Rayt6j_7Krlb98BV-zUVN_zuA0xjil-alIp0tz3Slsq6I-94PLnWpWwCntfdd_LqoAA6o0nbV0tBJrLDpi2YZ-_S-oX7OcJjLMISZAyLdKeEmGbWnVvf3fXzreFEQavw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇱
💪
گزارش انفجار در ملارد
@News_Hut</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/news_hut/65413" target="_blank">📅 05:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65412">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
حملات به تهران  @News_Hut</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/news_hut/65412" target="_blank">📅 05:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65411">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FdgT7mDUONVN98JtHEgPgOPFSQ0tttFm9A2PMp1OvGmLeHLDd82_4m_RjNwsc9CkDgs0_HudcBerLti9XPCIJdKBgJR_H3QxwuFr-o7Y6wj6L_sMxBervICPD_MHhuzbAWdm_qg2XR4zYYDLwO0sSBoXV7o2lQwdlj7Pc2rHlLR3rPCGbA_H_HOImH3PglnfiaszRdzBSCuR1qaq1BmOJF9baPsviZfcCFPieDpD6QmvCcht9sRKgrdgFbia37XYaaK2hsH6g1rRxGHRjcH3oRx1O6--j1iqTtwMH95xLwR_Hp0yChu98dEcuQO5px6aM6ABa5xI7PLGXxMmTCd1eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حملات به کرمانشاه  @News_hut</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/news_hut/65411" target="_blank">📅 05:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65410">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k_BhU8iQcLM0O86yd5w3gxEwEWzOPVxTwV-51Yhbmt87dYKHE6J8fJIc1V5arL8aofK0-hj2H6p4SsKaETJwBdCezGaCKApit6l7FYAkXjGDxK0OwVRdqPOUZi6pc5AeOCn5psYBhB1RpkaqIlGziIMSC3-35D5oYdLdfqhmomhR_gzYdGgeuTXeKvZKP0zHghpxjphixEw2Ie2mcTumqaRw54QSOD4KvBxhidCCEUoGWAoeEElXg6FB6SIBk-88N7gGLJIXy6OzWL37WJzGbSrxHh_a8L0VYSEIIU0e4qsbwy4smubz-90TjU5Lbm6kOhVV03jrTcMSKm8OyU9x9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حملات به کرمانشاه  @News_hut</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/news_hut/65410" target="_blank">📅 05:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65409">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13951b2150.mp4?token=TyOUigZHhAD6dPE9qjxfd10lolQL2eiQpcOLEImY8-7ZT8tnplxpH2tIUthMuoPNbzBSFKVcpKzHM1089bl9YAy3cTwifCa_tEw8FQ2dmJ5Xvjhnfr_VG9BrvZEam9yRBSxyoJNuhwf7jSSMKVgk9S0YD7d0QkhKOr5jCNyfDDE6nuHMsvvgmwnVKcrlDEpPYigwkbecT9uLjbKWBQyXYDDCQyPt9jh38CM3adTscA5iMCo25SEhcywcNM2BWAzxvuiKLGywAPyd5zlFD3mL2NrUpv2EcSn2dfaVfsM24jw0xP6_wLnG7afZWrzQxKRPFwnQrLBkT9CYC8XiIjTQVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13951b2150.mp4?token=TyOUigZHhAD6dPE9qjxfd10lolQL2eiQpcOLEImY8-7ZT8tnplxpH2tIUthMuoPNbzBSFKVcpKzHM1089bl9YAy3cTwifCa_tEw8FQ2dmJ5Xvjhnfr_VG9BrvZEam9yRBSxyoJNuhwf7jSSMKVgk9S0YD7d0QkhKOr5jCNyfDDE6nuHMsvvgmwnVKcrlDEpPYigwkbecT9uLjbKWBQyXYDDCQyPt9jh38CM3adTscA5iMCo25SEhcywcNM2BWAzxvuiKLGywAPyd5zlFD3mL2NrUpv2EcSn2dfaVfsM24jw0xP6_wLnG7afZWrzQxKRPFwnQrLBkT9CYC8XiIjTQVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
انفجارهای متوالی در شهر اصفهان
@News_Hut</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/news_hut/65409" target="_blank">📅 05:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65408">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m1va763G8ChSfV4iyPBeqxQx3XmHnUHwW38tBB3UjSofbmf34J-JIDcbKKOmrPo1yZK-aBw65NF2N6tNymVHkCv-qsM7gjtEv_TwL12DXJnc7It23EZgic9xyyEch824qnL2B1kAOuKUgWzQGGjPxbnv17RqHQGtkCifcWF60X6rG3yRlqGyX8SL0oVVi0SZ3fap5GGqYugVek97vjsVgZuh6HxsgxCCgvA3P7LreieOjJ9r4LJL-MQS0bTHr2lEjE81Q6anYWTS5BCGAwXIs5croYyIdIEl5LIM6fziCKhyg0paRxXgZalK6AwJnKZ9QdL-UomGws2hDbBQNDyjEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇱
نیروی هوایی اسرائیل اندکی پیش به اهداف نظامی متعلق به رژیم  ایران در غرب و مرکز ایران حمله کرد  @News_Hut</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/news_hut/65408" target="_blank">📅 05:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65407">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/A1tkaKpBoAktLVUcYVEkcTq3HDfJYOpbXJ6MVUsdDRRWCW4fxxtRI_twksrUxPt-EmztY-QrYmuDse9hmOpRVOszX7XOfCCCyI108q3q9WLCWTb6CXJcLv_ceJDp4o2CnqFeCi10vb1X0B1fG7L9bZ6Xfw_VbfDhKO6AvMvzY3-t9Jf4x8Zto-dKTNicU1FYodlz6AMqnlL7hxYKGdTOGW6lFFumrEJ9aBcd5WOWmD_apZ7vzzQzQOylbdGLKOwlTuqiafZPMTXzQJWZy9PKH8nVCzDJdB39fe2qHF8Vd010zkAOm7wGlE6ayJWrlWRm-9avFnqkJ_3Au2ZLSx4wTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇱
نیروی هوایی اسرائیل اندکی پیش به اهداف نظامی متعلق به رژیم  ایران در غرب و مرکز ایران حمله کرد
@News_Hut</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/news_hut/65407" target="_blank">📅 05:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65406">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید  با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/news_hut/65406" target="_blank">📅 02:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65405">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eRBCHHaT5UzBAYxTeCEvxjN8BvlUvRcN9ymiXHTkhTg1r-ndefHs2xXF3jqVw4DDhhMABMPIS5_uZVhuYRf93QI8kMGHhmdIOQIbawJUe3eU7r-J1zOka1nU4BzlyxGwGjLnRVINdCpBwhcMhi8WEqzRyaPJS--zdwwQun0tCgPzUXEmoa_f9JgQy-CrVMr6fECWQ0iLl73L3V5rb5zgIZ1paHLxMXS53CAL4ONkxsIEDDVN-Jc4tfATov_cWKQg6bwAGk7CMLhMxysL5xdDb-dAxcQqxSvGUqmUtlPNPQu7I5rNRTZjSSNwvP_IQhtyxCJ0g-rx4mcmfJSLgP9wOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید
با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/news_hut/65405" target="_blank">📅 02:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65404">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZLpL-V_zltxeivcOoO5_9vRq0091SOkJggTzbiHLmiK6n40c6oM_1rwURKJuG_xfE94WOEX5RvGU7zeKbWtCKEPBq2QEpw9pu1qavRnS8_bdDKwhBRrLJ57C_RajFmQY17_VAnZ6bJhCI-sXSSoXeTL0SzwPeamuYIQ2PqwThT-xJEs_L3SpaqDz1qT6l2XAtV8H9sL12MNz-8G2w8eO40ECkElC55USL_e8P6bPPwGjN6Dp8ZBlZCpG-hPMoohC7amshCS10xz8PUFADX1l_cNYMHvPpL_h1QfGyXno9vq1lwh_mDov2TfHU7sAi3qYW0XXnrH-Qxzm-iTFjAeaGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
مراکش
🇲🇦
-
🇳🇴
نروژ
🏆
رقابت‌های دوستانه بین‌المللی
🌍
⏰
یکشنبه ساعت ۲۲:۳۰
🏟
ورزشگاه ردبول آرنا
🎲
با بیش از ۴۰۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
مراکش در
۱۰
دیدار اخیر خود،
هفت
برد و
سه
تساوی کسب کرده است.
✅
نروژ در
۱۰
دیدار اخیر خود،
هفت
برد و
دو
تساوی کسب کرده و در
یک
بازی شکست خورده است.
📈
میانگین گل در
۱۰
دیدار اخیر مراکش
۲.۵
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر نروژ
۳
.
۸
گل در هر بازی بوده است.
🎯
پیشنهاد پیش‌بینی: مجموع گل‌ها: بیشتر از
۱.۵
- ضریب:
۱.۲۷
🧠
وقتی از بازی لذت نمی‌برید، متوقف شوید.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/news_hut/65404" target="_blank">📅 02:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65401">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: نتانیاهو چاره‌ای جز پذیرش توافق با ایران نخواهد داشت.
@News_hut</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/news_hut/65401" target="_blank">📅 01:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65400">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frombetcart - کانال بتکارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LPW1OZOrSFaSo8cHv2ZDvUoveqCcYlns57jF_JkdDH5amvmZVgRrSJswJz1WeRwBpT7SP5WFViDSLVoOiIHkCj4eVtbmiDCTkU_VSkzs3TEIJU2ezR_QvaAOItkrFnrltPA9sjHFS23dj7u6sOnfq0aWIz7Bgir87NKMCoCWbnhFHA0PG1zXfc1YbQCluhV_5ZshRd5UF5YCvRPFwDeB2rkMJMqWTLiqZWKmDYYetvTrQnZplN6GovbqkxGWWLVff9PxuLsY14CCOWgn6DfWsJHLQmCY11SkdZUVygUwJL9M-Op0L8zwfr5D6lpV-7gJjMGOHQetnJgwz013rPm7fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
یه فرصت تاریخی!
💥
بزرگ‌ترین کمپین تاریخ بت‌کارت شروع شد!
🏆
برای اولین بار در همه‌ی جام‌های جهانی؛ جشنواره‌ای که تکرار نمی‌شه!
0️⃣
0️⃣
0️⃣
,
0️⃣
0️⃣
0️⃣
,
0️⃣
0️⃣
0️⃣
,
0️⃣
6️⃣
تومن
❗️
☄️
جایزه‌ی واقعی برای ۱۲٬۵۰۰ نفر
👉
http://bit.ly/4ep75qf
⏳
تازه لازم نیست منتظر بمونی جام جهانی تموم بشه...
🎁
بت‌کارت هر هفته جایزه‌ها رو مستقیم به حساب برنده‌ها واریز می‌کنه؛
✅
سریع
✅
مستقیم
✅
بی‌دردسر
⚠️
ولی یادت باشه...
این جشنواره‌ی بی‌نظیر فقط مخصوص بت‌کارتی‌هاست!
🚀
اگه هنوز بت‌کارتی نشدی، الان وقتشه...
⏰
فرصتو از دست نده!
👍
وارد شو و شانس خودت رو برای برنده شدن میلیاردی امتحان کن
👉
http://bit.ly/4ep75qf</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/news_hut/65400" target="_blank">📅 00:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65399">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
🚨
آغاز حملات اسرائیل به لبنان  @News_hut</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/news_hut/65399" target="_blank">📅 00:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65398">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
🚨
آغاز حملات اسرائیل به لبنان
@News_hut</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/news_hut/65398" target="_blank">📅 00:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65397">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
🚨
سخنگوی ارتش اسرائیل: رژیم ایران اشتباه بزرگی مرتکب شده، ما آماده‌ایم
@News_Hut</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/news_hut/65397" target="_blank">📅 00:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65396">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
ترامپ: نیازی به پاسخ نیست، صلح نزدیک است
@News_Hut</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/news_hut/65396" target="_blank">📅 23:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65395">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🇺🇸
🎙
ترامپ: به توافق با ایران نزدیک شده‌ایم و نمی‌خواهم اکنون در مذاکرات اختلال ایجاد کنم.   @News_hut</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/news_hut/65395" target="_blank">📅 23:45 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65394">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🇺🇸
🎙
ترامپ: به توافق با ایران نزدیک شده‌ایم و نمی‌خواهم اکنون در مذاکرات اختلال ایجاد کنم
.
@News_hut</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/news_hut/65394" target="_blank">📅 23:45 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65393">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
🚨
باراک راوید: ترامپ بهم گفت الان زنگ می‌زنم نتانیاهو و می‌گم به ایران حمله نکنه
@News_hut</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/news_hut/65393" target="_blank">📅 23:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65392">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ: حملات اسرائیل به بیرون هماهنگ نشده بود؛ اصلا از این موضوع خوشحال نیستم
@News_Hut</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/news_hut/65392" target="_blank">📅 23:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65391">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
🚨
باراک راوید: احتمالا اسرائیل پاسخ خواهد داد  @News_Hut</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/news_hut/65391" target="_blank">📅 23:33 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65390">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
🚨
باراک راوید: احتمالا اسرائیل پاسخ خواهد داد
@News_Hut</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/news_hut/65390" target="_blank">📅 23:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65389">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
📰
فاکس‌نیوز به نقل از ترامپ: چیزی که به ایران پیشنهاد می‌دهم؛ موشک‌ها را شلیک کردید دیگه کافیه به میز مذاکره برگردید و معامله کنید.
@News_Hut</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/news_hut/65389" target="_blank">📅 23:23 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65388">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ارتش اسرائیل: تموم شد بیاین بیرون
😐
@News_Hut</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/news_hut/65388" target="_blank">📅 23:21 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65387">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
🚨
ارتش اسرائیل: تمامی موشک ها رهگیری شدند  @News_hut</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/news_hut/65387" target="_blank">📅 23:21 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65386">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ارتش اسرائیل: تموم شد بیاین بیرون
😐
@News_Hut</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/news_hut/65386" target="_blank">📅 23:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65385">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
🚨
ارتش اسرائیل: تمامی موشک ها رهگیری شدند
@News_hut</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/news_hut/65385" target="_blank">📅 23:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65384">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
وزیر امنیت اسرائیل: امشب تهران باید بسوزد!
@News_Hut</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/news_hut/65384" target="_blank">📅 23:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65383">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d76423eea.mp4?token=RJG8rU1H0cY-YYqwrPkw5A-zepOihvcCZ18RQwJ9FqYPi0MWJdLE_v4S48DhUo2nCNGVQwgfB17nwPSdUX4ZRV4qCzrREQR3MKMhotuFt1ttXUUQ0Ze_aHl4qE7SIW2bwW6fm6cUq0QYlJKsCV0w_tOBO7ztpFOULpjoad9MyoMInxfNPGSxhv67aSCOWnbH5dxH47htwMhR2yhdZqdatKVdH6-rJl3NxRJHvLFDbD3zWM8edwcuMeCLLubAJf7J_XdKAxZdq5_XZUpUZgpJJXSH3ZIrqmef-2MP7qijjWPOeuudmmoK2PxUfaLVKHZ1kHHwcxhF0h7ajn2CpEhisg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d76423eea.mp4?token=RJG8rU1H0cY-YYqwrPkw5A-zepOihvcCZ18RQwJ9FqYPi0MWJdLE_v4S48DhUo2nCNGVQwgfB17nwPSdUX4ZRV4qCzrREQR3MKMhotuFt1ttXUUQ0Ze_aHl4qE7SIW2bwW6fm6cUq0QYlJKsCV0w_tOBO7ztpFOULpjoad9MyoMInxfNPGSxhv67aSCOWnbH5dxH47htwMhR2yhdZqdatKVdH6-rJl3NxRJHvLFDbD3zWM8edwcuMeCLLubAJf7J_XdKAxZdq5_XZUpUZgpJJXSH3ZIrqmef-2MP7qijjWPOeuudmmoK2PxUfaLVKHZ1kHHwcxhF0h7ajn2CpEhisg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حملات جدید از اصفهان
@News_Hut</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/news_hut/65383" target="_blank">📅 22:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65382">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k5aHhzlaxsABZgbrHI0oXmYPFNUFiE5ia1pG4L9qwlTuULHYDsDTativjkIrq0p0G4Y0XMRgVB3TfN-B26vbXgF0AX_XagalRCuU0Eu1py7pfz2eYMDhuCj46l6gG0D7G5SzQ_HD2fpkxrAg-zKv8YAJ5g5q6KCdhrNFztnImHfCk6FVsDLE76fCoa7a_gv79LKMj_UQkOl7rS_h6rz8iu2cxTNSjIDbjFsaO6dX4HPNbcT4Gl0hWWT2dFXn0DUcJ1cvcGBSmVb-dAJXoHtw8hspWIXs2dnDGvvbhACwI8ip8NCU8ZleALSMTStV6PMiKGFJXqMrktISnTe5ssRIZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حملات موشکی سپاه به اسرائیل
@News_Hut</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/news_hut/65382" target="_blank">📅 22:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65381">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
🚨
📰
#فووووری؛ خبر اختصاصی ایران‌اینترنشنال: سپاه پاسداران آماده‌ی حمله به اسرائیل است  @News_Hut</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/news_hut/65381" target="_blank">📅 22:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65380">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
🚨
گزارش غیررسمی پرتاب موشک از کرمانشاه
@News_Hut</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/news_hut/65380" target="_blank">📅 22:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65379">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
🚨
📰
#فووووری
؛ خبر اختصاصی ایران‌اینترنشنال: سپاه پاسداران آماده‌ی حمله به اسرائیل است
@News_Hut</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/news_hut/65379" target="_blank">📅 22:18 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65378">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/h4FcjbnicUTFRRSlO8R9jf9_0CIZ3OApYK6bvcx_D0c0-92NrtHIeSvkQeIup_BZnUKLQiI_fdBemz4vdusmHIcDkB3lsjOLpSVWXCbpMOJ0_S_G11NdIb51C8P_-mAu5_Tbmy6lkhDTWL--vVvXTXjKYyE7qvlYdN4M4XKmyEDBb0BFhy_vxzxPNNH_f-L7A5g8fwlFPtId7vpwF8lSgRXhPNkEDYI2GzYefoL93sydgDfNzjlBRQoWz-hJYCbixFIpgF0wMO9GRS6iqd4rD00MTnd9TJqVpiPQrx9jks5z2lO4yia0GkI17QljB7sjbD1Nq_4bP7beSbmPQMZu2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
پرواز تهران به استانبول به دلیل حملات احتمالی ٫ مجبور به بازگشت اضطراری
به تهران شد
@News_Hut</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/news_hut/65378" target="_blank">📅 22:12 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65377">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65377" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/news_hut/65377" target="_blank">📅 22:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65376">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eSmgdtCkVxir5UkPdGgo4S8-mLGv7wFw9FzxlTjHpkEmyE8sCzt1jLwmk-UuvxdRCR0P_JXAtNgeSfqfFh0HU2eOZvLw0qxwwsnlCK83Xp1CNZD5cq_EItRGWxr7sDLJFxH9-FRYhSPwjYGvWhs4wvTTBo71dN8Wo-x3qEgqsbmXvWZBaIW9xUAoU2zKyEoXF5dYh9mx0XclxRPaYXdYtZWpoBk7P0zJGBkX-FaMxdQz-FGlCmOH6L8FNSRaFsuy5uQ-MjYOaNqQTYXOvLMUzFm-vnk8z5CkQyebR9Q4nTFKGXqNK4iJU9K98HZbiLZmRTnkHlZs_87XvLSjF2eDQg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34K · <a href="https://t.me/news_hut/65376" target="_blank">📅 22:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65375">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/D-MeR3jQoeLt5GCV7IfkQm1pVrRLOxQzbUw337vNxB6NX77yLi8S88eLhDliFNrviRgAMfnqivonOLUGAj4dftaCQsaK5r7pbMPBnF8QjjT6L6UBejTxWOYdZ2-Iqj1xhEqu1UEiNDWbcM8fFKlNT-Ci9vRieJgs6jTuyUoLj8AhV-PyfG2xtdQKn0pBJfyM6hxp0rSOvT3uhkK6Wz7eV-ISpE_r6UfNEOoT321AF2rxGEfwaSBC9zOS9Kt8YNeGkPflsO7Z76zT3HYJ-92VVVDXuwbfeZcQktyKJmsF5J0OLQXmGyc8vdq5LO_EH1bfQhFm98VdcVME228lm8RZfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
د اتلتیک: نزدیک محل اقامت تیم انگلیس درگیری مسلحانه ای رخ داده و 9 نفر زخمی شدن!
@News_Hut</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/news_hut/65375" target="_blank">📅 21:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65374">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
🚨
🚨
پشمامممممم؛ اریکسن وسط بازی دانمارک دوباره قلبش گرفت و سکته کرده
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/news_hut/65374" target="_blank">📅 21:46 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65373">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rJdx1pW8yiA5d7JsF4uz5ASM384cRHPMgI9oOBB_UBJaBWGZjFWkSlQSzfeuq1t1uzIsG1p9uoHejDxdAd52aGSh_BFMdafeRB7Pqiuuu0yc52cOUYi5iuI05V_4b2MMT7-EqEZ04iVywj56P1FwTfR8aEhdUdNwdHxKyGlPyZnVKKqxX8A6yZEuOjpUk-tTHZrQJBHTCkmeJtDu-lT5zpHmkzjSlFshZwdTconCcoX893Jhqpk8h8bQme8e9y3IdsOtX4CTdp-QCBqLDvmY8p5I9lgDzw8EEAOuEvPpaQQbPpCgqO1Vvx3cl9ejk1VGK-12uAv2nmi5wahXKa7auw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بلومبرگ: ۱۰۰ روز از آغاز جنگ توسط واشنگتن و اسرائیل گذشته و به نظر می‌رسه تلاش‌های ایران و آمریکا برای دستیابی به یک توافق موقت جهت پایان دادن به درگیری‌ها با پیشرفت ناچیزی همراه بوده است.
همزمان، وقوع حملات جدید، فشار مضاعفی را بر آتش‌بس شکننده فعلی وارد کرده و دستیابی به صلح را دور از دسترس نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/news_hut/65373" target="_blank">📅 18:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65372">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">دونالد ترامپ در گفت‌وگو با شبکه ان‌بی‌سی نیوز گفت که اصراری ندارد لبنان در توافق کوتاه‌مدت میان واشینگتن و تهران گنجانده شود.
‏ترامپ گفت که به‌عنوان بخشی از هرگونه توافق، دارایی‌های مسدودشده ایران را از ابتدا آزاد نخواهد کرد و هیچ تحریمی را نیز پیشاپیش لغو نخواهد کرد.
‏ترامپ در پاسخ به این پرسش که آیا این اقدامات پس از توافق انجام خواهد شد، گفت: بله، بعد از آن. اگر رفتار مناسبی داشته باشند و به تعهدات خود عمل کنند، آن وقت گفت‌وگو را آغاز می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/news_hut/65372" target="_blank">📅 17:33 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65371">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65371" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/news_hut/65371" target="_blank">📅 17:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65370">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JVMy0FeFHhuPNEpWzxWk_XduV1EHJane5_kUGTCMfqLWieC1Zv4M8fXWjGCyVmpmMOhVfq-E2YG5NJUn1ylfz1a_E_EAbo-bR6-3MkPfAgL2s6-bVF3NmBFObcnxhnJ6ltLL65gIhn619QHDl-GR_1s9XlmzTgPutVCJt989yseohA2tDebjTcoQLY-kkKAaP66SxjCUC2KEMVg_JvSbghcMA9NlYM9irQ05EqBojw5AQtgEmLMHkSk8Sve2HQLQUa4Sd53-BD2fD7AGLCwXmpuCupDoOIx1MFQQYuYrXOCjogArLMU4PpMNLhTEfXx4CJgjWs8I7nexOq5NPfN2Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤼
روی مبارزات با 1xBet شرط ببندید و شرط بندی رایگان تا سقف 100USD دریافت کنید!
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
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/news_hut/65370" target="_blank">📅 17:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65369">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: احتمالا بدونیم مجتبی خامنه‌ای کجاست؛ اون از پدرش عاقل تره!
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/65369" target="_blank">📅 17:05 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65368">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
🚨
صدا و سیما: منتظر واکنش قرارگاه خاتم باشید  @News_hut</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/news_hut/65368" target="_blank">📅 16:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65367">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">‼️
محسن رضایی یک‌هفته قبل: اگه اسرائیل به ضاحیه بیروت حمله می‌کرد، آماده بودیم شمال اسرائیل رو تبدیل به جهنم کنیم   @News_Hut</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/news_hut/65367" target="_blank">📅 16:39 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65366">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">‼️
محسن رضایی یک‌هفته قبل: اگه اسرائیل به ضاحیه بیروت حمله می‌کرد، آماده بودیم شمال اسرائیل رو تبدیل به جهنم کنیم
@News_Hut</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/news_hut/65366" target="_blank">📅 16:33 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65365">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
🚨
هم‌اکنون ضاحیه بیروت  @News_Hut</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/65365" target="_blank">📅 16:07 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65364">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hDAAD1Q2D1oRMW8Hiiusxh0VXrO9uwtLrMgInINdZEjzMrCYZ5YtU5g1nkP2wsSFof3baS6wivr115mfo4m1JvBhF1Ine3Ghdv5IRic82vnQuS_nPqMBhXaZ1-cdkwzgJormEaP94flLSeQ7fJAzo14tlIx3WOV6Ej0hIV_8XmDV4rnSETWSaAGev_C7b4hUdVtzsiGTPzP9uJEVEQAge_HUtIhom7hWck_T_QLEgKmZ5bF9u0qdJKXHA8kPyJB6suBHzcv3mj9VdCS9Ze2y5fOg4RLEdWfrFy4TZ2NN9b-iGV-1LuRW2rCuxa0gRq-G-2D3xJ0I7SATXl8GvKfuHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
هم‌اکنون ضاحیه بیروت
@News_Hut</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/65364" target="_blank">📅 16:07 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65363">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
🚨
#فوری
؛ اسرائیل رسماً به ضاحیه بیروت حمله کرد
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/65363" target="_blank">📅 16:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65362">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h80w_NWXCQqucvhqdAlHT1Bw8lDUGJJF8SZaUcSnJNPZ5jb8n7V7hOIbSyp_fp1TUIBv3JtBlrv-zRuiA2DnmX5KAPv5CqnhgZsLTDmyHsbuXm8McWa2rc-l4ucg4urn9VF3djF7JjXBwY1Fkes0rjtnRAg3rI6InTRwswVyLq0TrneDkykLBkW9vgbA4zRjwdhtNYSP_ZQPnUA45hEveAmvprynFYab_qzS9gx57BBmewU1JV0OMeRMBgqnYz8sYbYUsZAAgZTFMZmt8I3CakQIBh9AgqrqbXjcLm2ycbRd5jYzkk13rNuOEgwpVqDKFGIM1e_AO_YGXpGhaO5IYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وکیل امیر تتلو:
توبه «تتلو» از سوی دادگاه پذیرفته و برای طی مراحل نهایی پرونده به رییس قوه‌ قضائیه ارسال شد، ولی هنوز تصمیم نهایی اتخاذ نشده
اینکه موکلم برای ماه محرم درخواست مرخصی کرده تا بیرون از زندان مداحی کند، حقیقت ندارد
@News_Hut</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/news_hut/65362" target="_blank">📅 13:05 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65361">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55cb33d933.mp4?token=IotiEdPodqK9CCP9Sgih0-J51S7JKamEDvJLeVE_Kzj-OX1gzhgmStM1FWN2UnuVsPh1MS-a7ALLtQRiJrXfr2K6a7OEWAI_cigQko8VytPVWYZ-To06F7a-xvzMsccOnepdU2ljUj2Nh3eWOMbVdd2MXzivsQtS3APOxjtJA5MA-GT8O_W4Nrj7jv269UpBYpdGfeNq8osePhf76l7uCle53M_9Lw0hR3isSqfXZ2E74aHY7E0BuSXu37CVF97GTKyBotSpXBXaEkNLMNGsw5h-fcaxxoVx5-ZFFsCvAEXf9YUbC6P9bfqWB3DFkUrWp9WN5cDTiadZ-TVX-0UqERw7UKeEml8PScetrDD9U__esHHoX5dVv-F0SOoBi1prlTA6W6dLtxl6ziHC4kV3LzUsBVWoEsmHccmEm3Yd8tOqtOsj-TPo9nBlhS-4CAfY-zUR9vSvXgm253xmk1jAvvXnZhOndF6nCk0pSL5MN5fsYye0h0rX70it1_66XGVkvhuZnVC05ay56YfajBwHWM_IiKlgaYR_q19Y2Pmgj7nY96wGeSV9PtTZRXOacBODROZtvY21Rl6-9Axt3pU5wWVvA1FoAzSm9fVP1pCd9gMPPGorMiWbmo9vGc-BrRPf1sP7UmJFB_hSlNv0AHvTRdjAZUsZfIfGb95tB2-ZmdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55cb33d933.mp4?token=IotiEdPodqK9CCP9Sgih0-J51S7JKamEDvJLeVE_Kzj-OX1gzhgmStM1FWN2UnuVsPh1MS-a7ALLtQRiJrXfr2K6a7OEWAI_cigQko8VytPVWYZ-To06F7a-xvzMsccOnepdU2ljUj2Nh3eWOMbVdd2MXzivsQtS3APOxjtJA5MA-GT8O_W4Nrj7jv269UpBYpdGfeNq8osePhf76l7uCle53M_9Lw0hR3isSqfXZ2E74aHY7E0BuSXu37CVF97GTKyBotSpXBXaEkNLMNGsw5h-fcaxxoVx5-ZFFsCvAEXf9YUbC6P9bfqWB3DFkUrWp9WN5cDTiadZ-TVX-0UqERw7UKeEml8PScetrDD9U__esHHoX5dVv-F0SOoBi1prlTA6W6dLtxl6ziHC4kV3LzUsBVWoEsmHccmEm3Yd8tOqtOsj-TPo9nBlhS-4CAfY-zUR9vSvXgm253xmk1jAvvXnZhOndF6nCk0pSL5MN5fsYye0h0rX70it1_66XGVkvhuZnVC05ay56YfajBwHWM_IiKlgaYR_q19Y2Pmgj7nY96wGeSV9PtTZRXOacBODROZtvY21Rl6-9Axt3pU5wWVvA1FoAzSm9fVP1pCd9gMPPGorMiWbmo9vGc-BrRPf1sP7UmJFB_hSlNv0AHvTRdjAZUsZfIfGb95tB2-ZmdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با زنده شدن دوباره دریاچه ارومیه هزاران فلامینگو مهاجر بعد از سال‌ها دوباره به دریاچه برگشتن
😍
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/65361" target="_blank">📅 11:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65360">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tUHk9l-np0abwahPyJHX1LwFC9VUYsosEooN71TUwMx0GhowTseNhbn8osxUUdT13RfoTfL7IKWsXkEG5sHsIQEoc_B3E4YYw2FLsodezbMr-2pg_PT4-Lizfv41A4fVAV5vwHu_1PC7DsIKS4pVKJQW3Vxv_fUfYUX0Oka7wG707VMJEJivDzzV8c9vFo6xZuHPRB19k750XKNGuvr1PyPxtImNUhgbu04Zbl5yDe_WeANYxtyaHflEItGA-m6-d5hOF33-cFWX9b1tbIMAQE9SVGfI8-PuLkHOEoJykGXTBKxXK7reUOUpW7BpFcwV65GHj5QW0unDkE15E_3SnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باز خوبه خدارشکر بعد از این دوتا پویان مختاری هم برگرده جمع نخبگان جمع میشه
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/65360" target="_blank">📅 10:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65359">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gM5imTyFb0jhRI3nbE9p9lHBAoMl506TGNFOkRgxj4e-vwf71Z1YbCSxjwVHfUMIonuZCoShiNKtSWb87hMJ2O7IYwCfetSSQhVN0jg7S0-peDEOTHPypaZizaey8TFboqAdcV9kIP40hihskdAGWu_1Y-OM2gbtd8z9AXr5xlWI0Xi5pUVOK5cfiyflziKMpzjfsX0C5uo_993pqUmWvsdlZTfK6P1bYNz3oPCvA5R2Hozsv0rC4tRs6kCJjvFoW9l3BOmBy9khcbvf6IbVrDo4Okr03PoMfHmJ9XwCytgs5Y_CP0FimgKCECHxGvzXHXTu_josUdsApEvNQZCd5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزش یک میلیون تومن وجه رایج مملکت از سال 97 تا کنون
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/65359" target="_blank">📅 10:39 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65358">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/884f21c214.mp4?token=jB-WLPrwny0ecKaOr3afZ1jTTucddTYshl4dTGT69cnNrpQ7RxuLannrZp9O8X9UqChxMFeR5mBgmJDvOj1upxHWSmhZMd88k3w-e4vWOWwBU6dFvxLHNmTaa03uI4jFIn98wzyY353pK_AhBxLZomxRP3Yw4NDg-6ARZR_qE2Ce41hMGY8YfUGMh09aEMoTzWy-VRFcNlStzeE7mw8gfK8phO6DGiJuqwHXvTI30pGxXhPgdd4haSMmJ2DEtVt3Qvzxb7qoYXo2gv__Cv5fYhmNksebIcnFsZYIyRU3TSqUm4T2_oFJ7wEX01H1Icfar0JniIthFi2p11Vmhqps7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/884f21c214.mp4?token=jB-WLPrwny0ecKaOr3afZ1jTTucddTYshl4dTGT69cnNrpQ7RxuLannrZp9O8X9UqChxMFeR5mBgmJDvOj1upxHWSmhZMd88k3w-e4vWOWwBU6dFvxLHNmTaa03uI4jFIn98wzyY353pK_AhBxLZomxRP3Yw4NDg-6ARZR_qE2Ce41hMGY8YfUGMh09aEMoTzWy-VRFcNlStzeE7mw8gfK8phO6DGiJuqwHXvTI30pGxXhPgdd4haSMmJ2DEtVt3Qvzxb7qoYXo2gv__Cv5fYhmNksebIcnFsZYIyRU3TSqUm4T2_oFJ7wEX01H1Icfar0JniIthFi2p11Vmhqps7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از طرفدارای حکومت تو تجمعات: ما تقریبا یک ماهه تو خونه دیگه غذا درست نمیکنیم و طوری شده فقط میایم اینجا میخوریم.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/65358" target="_blank">📅 10:09 · 17 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
