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
<img src="https://cdn4.telesco.pe/file/NQvxoefCyNHsxAdMFoSUUiQn7dEeOULtu6x-5LPzHeJdXXyQZOgefg67Ms2O7RIY8CAwShz_XwFsHCKkJrAnComUeu6E4hGArWatRH6gkx-peJm1iCfldMTsfQ1xONhjhfj0XSe0OuTCwRlE4XuMblB_XxQBLJ0EQb_HcVCqJ0pzhbxe0gFtQg8F2ktWG1vPJdmRm71z_fCqY7bS-zRxQcJy4FDBjINU88YQhvyloydKF1ndIUN6SphBt0rSEkxIlRF-609khjJ00THT-X9eC-H4pUIH6k5K0_KBc9OPTtP5oIlDK2Rovcycf7IpvZF-VEng0oMzpfQYAf1_j6mZpg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.5K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-15 22:28:18</div>
<hr>

<div class="tg-post" id="msg-5310">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe3f82fa44.mp4?token=nP_La9j_erUbbnS6bsVHHe_yVZb4OAOrQQZ00hg8Pe_kwXk2YCsoHvXgm3fyYjz-ELK5I9B48CLxmO0noOwKcafetiDQXwuFk7Y1qtT7eF9Q7oZNS4cjM95wTU494VdW4xccdSSjFKqab_lVTqzqfWnzYiTVlKkliTO8ZlxC3SFT0UEdFI8zDFTm6hoXnMlwR5HBtmqIZeJhURAo36Te15_xatQ2HoeSzJyoB6T2qbNTeFOusZ8Fpjr5PAz1yb5Jm_mzKN951VnxvqfD804tmX_l_KoZc7ij_LIYAEOzU53Ut60oHT2kmAB_9YjjGYFOzRDnbctMJmx7nK61aSnE2EbpBzoZ5dr2eHPg0Q5jWR67gSL1-Au5SmBHs5C2h8C17uUud1C0ePWpE36rBrCkljsIxHA9LfALWEQsLvXfyqPUEuLik1scJ4rPYPATewr1sqZywBB6cnQ5VSf-jrRheRb0FyT6-IykhUehRUf_eGHge9OuqJLGOGgJ3Oa63yCc1pXaBNA2gPREK7EruNqnDzzww1jCiZpHm4GZR0g-kf1N21D3rPGJwD9rr7QmDEyVkVH2D2EGk-S-sJbWXk1js59-MSGV-YrJk_GpANjTMjZnYqz6GFVv7SXEim6l-S7WcTAhgQcPO1druBIJUM3YqdDXwspPFqmBXluqBiWEEWE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe3f82fa44.mp4?token=nP_La9j_erUbbnS6bsVHHe_yVZb4OAOrQQZ00hg8Pe_kwXk2YCsoHvXgm3fyYjz-ELK5I9B48CLxmO0noOwKcafetiDQXwuFk7Y1qtT7eF9Q7oZNS4cjM95wTU494VdW4xccdSSjFKqab_lVTqzqfWnzYiTVlKkliTO8ZlxC3SFT0UEdFI8zDFTm6hoXnMlwR5HBtmqIZeJhURAo36Te15_xatQ2HoeSzJyoB6T2qbNTeFOusZ8Fpjr5PAz1yb5Jm_mzKN951VnxvqfD804tmX_l_KoZc7ij_LIYAEOzU53Ut60oHT2kmAB_9YjjGYFOzRDnbctMJmx7nK61aSnE2EbpBzoZ5dr2eHPg0Q5jWR67gSL1-Au5SmBHs5C2h8C17uUud1C0ePWpE36rBrCkljsIxHA9LfALWEQsLvXfyqPUEuLik1scJ4rPYPATewr1sqZywBB6cnQ5VSf-jrRheRb0FyT6-IykhUehRUf_eGHge9OuqJLGOGgJ3Oa63yCc1pXaBNA2gPREK7EruNqnDzzww1jCiZpHm4GZR0g-kf1N21D3rPGJwD9rr7QmDEyVkVH2D2EGk-S-sJbWXk1js59-MSGV-YrJk_GpANjTMjZnYqz6GFVv7SXEim6l-S7WcTAhgQcPO1druBIJUM3YqdDXwspPFqmBXluqBiWEEWE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏محسن رضایی امروز به CNN:
‏اگر ترامپ مذاکرات را جدی بگیرد غرامت ۲۴ میلیارد دلار برای آمریکا رقم بزرگی نیست. اگر او واقعاً بخواهد با ایران به توافق برسد، این ۲۴ میلیارد دلار آزمونی برای اعتماد است اعتمادی که ایران می‌خواهد نسبت به ترامپ داشته باشد.
‏این آزمونی است که آمریکا باید از آن عبور کند؛ در آن صورت مسیر توافق باز خواهد شد. این پول، پولِ ماست، نه پولِ آمریکا!</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/farahmand_alipour/5310" target="_blank">📅 22:22 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5309">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZY99gAqmpfiE2H5fH1NbbcJdbCNKU1rLFCr6H-ZPrh-jxzqYliRgE_9fKPG3oPjiT1tUqu-sZ4yegwnJrr2FQCS2xG75FeV04OPOXvb0i0nP932ie1QqKYbDKygi_JNHPkVqncZoIp1Pp2yunnGYmjnSotn78rLxXn03YY4G3JJtYF_Yl1pG2vfr6KkuWpsfMc5SV6yRxXGFd-ZErHFnGPyTO4TxIxFJ_iPgJPq4MX6gwxgHr1Re6YmWMjEFswPjZW06wXgIdnItb_BpRVBz7EU-yxhs37xMI9jOcgzHm_TV4ucJbeALFQrhKE9SrLAlpi25jB_RByDQwjrfyV7V7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلیسای انجیلی مشهد
که سال ۱۳۸۴ به عنوان یک اثر ملی
به ثبت رسیده بود، سحرگاه امروز
توسط بولدوزرهای جمهوری اسلامی نابود شد.
مسیحیان انجیلی، اولین بیمارستان در مشهد رو هم احداث کرده بودند.
کلیسای آشوری تبریز هم چند سال پیش ابتدا مصادره و تعطیل شد.
کلیسای جماعت ربانی مرکز تهران هم
توسط وزارت اطلاعات تعطیل شد.
کلیسای کرج و املاک اون نیز مصادره شد.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farahmand_alipour/5309" target="_blank">📅 18:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5308">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec2d5c99a5.mp4?token=YK7oNkjBBHmEWS9Z-t0pN5qLAjl_YhU03RQ0USe6YrZAhYUn5Ut196_IKfeKYGBg7LddrUGPjhXdlNsJOXSKaCIU8vgv9OIvBc3g9vX9_IbzT-BqbqhZOQ0nUTIKrNM6tjdlGgjoOtaRPh6851gxY3fufhtbhrS9t7fn6ssLGvL3L-bE4Hrwy63ELR6IOS3JU3EVFntk7J8fT183hwFBpbz0TtJv0CemP26LQpNbsqewqlMzNXhrJWjaX04J3iylJ1gbYaH0q94j46opcaa8VMwr6yv1wSb3LGqb4545SOBjpLr7bXGWN13uyQgjKgcAtyiPnMnwCfD4qfb1jzlL-TmaYvA0vaMIHGmdW3_JhFhcnVZ_G09WRy5NQelnzEFkgXi8y7eU8ttmlRd42UPwIcM6-1VgDaySv4rXCtS8Z_iAIJ5tQ0aPEmeW-D7gIcaSrvPB74P2m8f0CKE7Sre4YlREw_B6HcHW1m8S5HncVcxQBctyCqothvpdt6ntP8HRLLffd4p_mOrk0FyMRBSrsJdpyCXyE6mCXPtM9tgGiFoJbXaPLFXqodEbYliUqqRnzmKZARIfwC4jmzrg1ksN6ZjA66LEPK4Y9BepiPS3CY3FZVCf1x3g4uZKMHUngxlGIwBaL_dVcgnrknA_YcvyH9XdiRtVAmD19zZZqKDZevk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec2d5c99a5.mp4?token=YK7oNkjBBHmEWS9Z-t0pN5qLAjl_YhU03RQ0USe6YrZAhYUn5Ut196_IKfeKYGBg7LddrUGPjhXdlNsJOXSKaCIU8vgv9OIvBc3g9vX9_IbzT-BqbqhZOQ0nUTIKrNM6tjdlGgjoOtaRPh6851gxY3fufhtbhrS9t7fn6ssLGvL3L-bE4Hrwy63ELR6IOS3JU3EVFntk7J8fT183hwFBpbz0TtJv0CemP26LQpNbsqewqlMzNXhrJWjaX04J3iylJ1gbYaH0q94j46opcaa8VMwr6yv1wSb3LGqb4545SOBjpLr7bXGWN13uyQgjKgcAtyiPnMnwCfD4qfb1jzlL-TmaYvA0vaMIHGmdW3_JhFhcnVZ_G09WRy5NQelnzEFkgXi8y7eU8ttmlRd42UPwIcM6-1VgDaySv4rXCtS8Z_iAIJ5tQ0aPEmeW-D7gIcaSrvPB74P2m8f0CKE7Sre4YlREw_B6HcHW1m8S5HncVcxQBctyCqothvpdt6ntP8HRLLffd4p_mOrk0FyMRBSrsJdpyCXyE6mCXPtM9tgGiFoJbXaPLFXqodEbYliUqqRnzmKZARIfwC4jmzrg1ksN6ZjA66LEPK4Y9BepiPS3CY3FZVCf1x3g4uZKMHUngxlGIwBaL_dVcgnrknA_YcvyH9XdiRtVAmD19zZZqKDZevk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس جمهور لبنان : این کشور ما است!
کشور شما (جمهوری اسلامی) نیست!
به شما ربطی نداره که دخالت می‌کنید!
این خونه‌های کشور ماست که داره ویران میشه!
[ ج‌ا ] کشور ما رو به گروگان گرفته برای
مذاکره و چانه زنی  با آمریکا!
این غیر قابل قبوله! حزب‌الله هم باید بفهمه که هیچ راهی جز گفتگو و مذاکره و دیپلماسی نیست.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farahmand_alipour/5308" target="_blank">📅 17:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5307">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">رئیس جمهور لبنان خطاب به جمهوری اسلامی :
شما در تلاش نیستید که به ما کمک کنی،
مردم لبنان دارند هزینه‌ سیاست‌ و منافع جمهوری اسلامی را پرداخت می‌کنند، منافع ما مردم لبنان با منافع شما (ج‌ا) یکی نیست.
رئیس جمهور لبنان خطاب به سپاه پاسداران: این کشور شما نیست؛ این کشور ماست.
سپاه پاسداران از لبنان به‌عنوان یک برگ چانه‌زنی در مذاکرات خود با آمریکا استفاده می‌کند. این قابل قبول نیست.
مذاکرات با اسرائیلی‌ها سخت بود، تا زمانی که به یک پیشرفت بزرگ  (آتش‌بس) رسیدیم.
این توافق می‌تواند راهی رو به جلو برای رسیدن به یک «صلح عادلانه و پایدار» باشد.
یادآوری : دیروز حزب‌الله لبنان توافق آتش‌بس میان دولت لبنان و اسرائیل را  رد کرد.
جمهوری اسلامی عملا لبنان رو به گروگان گرفته.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farahmand_alipour/5307" target="_blank">📅 17:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5306">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sn4rctaDdCBmGggT9sFib7X1aYnGvMuyw-58TkfHSN3H0qxf03rRMgsCgptYbw1uAGnpmnk-1cfVMcXkLKOB7eagWV3Cu5GnP4Igwpa_LmkVn9-SSy6kykNn9RmdyAf3NUdMqrjKEKZyxQArH2IY41UM8v4L7mw5p01Y1FmBm4PBAGi2gj3VC8YnC0F_zJYEiqN2MBFPO565xCuopu_GV19NT65jW_Bnr8TR6x9Nb0jEoZj3Ra7Q4yV0of-r8oHK4mHtYd_VWu2y4ZF8oPlzVidaXPA6VSDn8pUDdVndSKYj0pmLWVNJC95Ns3BImZ4mrYvzaQ6FwV6NEnCu0h0Brg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب‌الله لبنان دیروز توافق دولت لبنان و اسرائیل برای آتش‌بس رو رد کرد.
اسرائیل امروز دستور تخلیه ۹ شهرک و روستا در جنوب لبنان را صادر کرد و ساکنان آن در حال فرار هستند.
چرا اسرائیل با سایر مناطق لبنان کاری نداره؟ چرا با سنی‌ها و مسیحی‌ها کاری نداره؟
چون این گروه تروریستی فرقه‌ای‌ پول و سلاح از جمهوری اسلامی میگیره برای جنگ‌های بی‌پایان با اسرائیل.
عملا برای حزب‌الله و حامیانش، این یک نوع شغل و زندگی و هویت شده! تبدیل شده به هویت و شغل روزمزه‌شون!</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/5306" target="_blank">📅 14:15 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5305">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">امروز، چهارم ژوئن، سالروز آزادی شهر رم
در سال ۱۹۴۴
۳۳۰ روز پس از ورود نیروهای آمریکایی
به خاک ایتالیا، رم آزاد شد.
موسولینی در یک سخنرانی رادیویی از مردم رم خواست علیه سربازان آمریکایی قیام کنند؛ اما مردم رم از آنان استقبال کردند و آن‌ها را «آزادکنندگان» خود می‌دانستند.
رم در عرض یک روز آزاد شد.
شهرهای شمالی ایتالیا، از جمله میلان، تورین و جنوا، چند ماه بعد آزاد شدند؛ اما در بسیاری از این شهرها، آزادی پیش از ورود کامل نیروهای متفقین و به‌دست پارتیزان‌ها و مردم ایتالیا رقم خورد.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/5305" target="_blank">📅 13:42 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5304">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">« سد طالقان را یک شرکت چینی صفر تا صد ساخت، بعد به دروغ
به مردم گفتن که به دست مهندسان ایرانی ساخته شده .»</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5304" target="_blank">📅 09:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5303">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J-t4WT33XzNrlUV5DtzjTHNuWzOwx_lTOgpD2L5QMw-Wxsb3gj3DjWQXKXsPgF0D20YKN7krXzqBcDAIPpibXVtZuwyReefdzWobhDNr3OP8B5OTby4G4GvZ_8Pp84uxCHXUYjemX2OER3bJd6eMHtqcNX5jio6Q7CCyFfc0ZYZSpHwV9McnAi0JP4Rgx05ZXqEj4N9qBMB7tKcrcEMIGLU0XOOU_gLDVsb8hUTChnHzaH0u3-6alcFbTMOKO3JoO7AZkCmTtCKZ84BtUrWjLBfvyN1CP5UjxVDK2KrlquVUMS8VI97k4p3gRqZVyVAIepzm9V4OmMeq7XFV6ffWOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5303" target="_blank">📅 15:50 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5302">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BHvkA2-Dj3tUl7FSvylFdSQv1bck_z2znJ81R_9TNImi1dwvK0N2dWN5M56XZWuNR5KL5eI5XaEDVKGzKqItANR5uJrx4hbjT8scl1Lmok_dU4vhXqdGk9qcAfGiB1VI14dE7nuDIL5xZ2u6DQ1Gc7G_D0_rsVZ8mDMBuYh_Yu_BwV88LSnYq1WdoBNwKgbOEQ6dR3peSyeszuo51UmWBQidFKy_ojrdPwyKns9-64bCparJVEHjh77Fi9k2InkzmelO0vfVUQY5Gh3Yh5x1DtPJPdF6BiUDisG6cnvgGzr2eyesoQSEQFrpwOjFSaq7Kgbf3kpN-C9XLD5N13jIFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پاسخ به این بخش از نوشته نادر سلطان پور که نوشته بود : «فقط ایرانی می‌خواهند آن‌قدر ضعیف که هیچ‌گاه تهدیدی برای اسراییل نباشد.»
پاکستان یک قدرت اتمیه! ترکیه ارتش بسیار قدرتمندی داره، مصر هم همینطور،
چرا دنبال تضعیف اونها نیستن؟؟
زمان شاه هم ارتش ایران بسیار قدرتمند بود
ولی مشکلی با قدرت  ایران نداشتن!
بهترین سلاح‌ها رو هم بهش میدادن!
پس موضوع «ایران» نیست! رژیم حاکم بر ایرانه!
چرا با جمهوری اسلامی مشکل دارن؟
چون اونها سیاست شون رو جنگ و نابودی اسرائیل نگذاشتن! افتخار نمی‌کنن
که به گروه‌های تروریستی سلاح و پول میدن!
این چه ناراحتیه که ما میخوایم تهدید باشیم برای اسرائیل و اسرائیل و حامیانش مخالف این هستن؟
بیان کمکتون هم کنن؟؟</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5302" target="_blank">📅 13:26 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5301">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FRcepXoxx_9gwFjZdTfHPXcsUjHHg_L1Ce_LnoiOeRDWdmLT07fcmHPLEho_-eWN2CxUuLstnEAgAjO4PKhRATOYjZ_YjAN8yRaY51VP6VP7O1YMg7wSHXiYA5Wtr5HJlbqDmwFEvMPI9LIBl3tPWdhnlHve0JAPXLGSvu83sr488GJwilbD0d16LmQ-tNxko8aQwYH_V7vy6td3l4J0iTYzleInsbEP4izVLO9p6d9Pns4lCZNGLCDcd3uZbVMm4ZkI4CoxbUMG_JoHwjp1bsojskGbjqOQc_y2n419-6B2ssY5tvZEGxOG0DmMF8L2OVLgY6dL3A4aIMRbcPAxdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرجان ساتراپی در ۵۶ سالگی درگذشت.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5301" target="_blank">📅 12:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5300">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">تصاویری از فرودگاه کویت
پس از حمله جمهوری اسلامی</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5300" target="_blank">📅 22:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5299">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sDLAmLMqntkWAq4FiR4rftfLoSrCB-Y0gRVwASiMkYwNmoN2HtxDA0h8969Q0pEz_yXE7XzwgA5cLy6SaDdKIfxpFHBUf-xm_fLJuAFGfwfnfuBtAm6qT3sAn_7nG2oWl8Ps6hcnCji2nWrX9YCk4NHDb9jq104sfye91pbNRCGfdiDo8nw60xfPsjiyMRNmnoadADlvppFLNLvyEjcQYOTLgthuVpMbhEu2qM8T-49_H9GV_k7abPe_wHF_QCDpzBBv2KZBef1XQigbehFX6sle8iA0FOBoRwZvebejUFfjyRkLQgUaS1JLl1LnPZHsKJqCUT7aIiVbxdAtXC__6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5299" target="_blank">📅 19:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5298">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vyPPFuosB7B7NFMW16cRyhpD1360JavBG1BGsedE7lpypkZRH_ZFvDygBxjP3004LCec-rW2D4tSGiZlt4AZPh4oLTAaDtDotz6us-ts3TVg0GKzWD88fJ6Cvr-2LZmQI6TSRpnXKh29pk0rjKkNXuo6tECw_pTr1xbjadXymp9R0Rqb0re-_mMHA1FGWxR-ut7-Y8pc4qDQUhHQZ1AfZBWlhKzNBgPKY2VTqMcMUI0_uF9zpL7svUdL6Gfn9988RfR3Vc-hKOhPW1nl4xVaoVKZ0wZrXL6zEJb02r5eqF8apy6bTWxld5hAhypgb5P5ISYWeBoLeEIl8t63iISMBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
کویت ضمن احضار کاردار جمهوری اسلامی، دو دیپلمات جمهوری اسلامی را به عنوان «عنصر نامطلوب» اعلام کرد و از آنها خواست تا ظرف ۲۴ ساعت خاک کویت را ترک کنند.
وزارت دفاع کویت: جمهوری اسلامی امروز ۱۷ پهپاد و ۱۳ موشک بالستیک به سمت کویت شلیک کرد.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5298" target="_blank">📅 16:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5297">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d0b8905a2.mp4?token=MCKgAEQguAIld1A_9WoBR8dvN1VLtRd3ZEjvPj8JTU0SzHrQtsIoJ20-LvvETRmDPEIHehFCwxt_28PMF2auIjN6CxqRO8f0jGDe3GiekRWTIGkFENiLq26TTcZ8W8kT2ajG8Ils91owdcmRGhiDbU-i4S-H5G8FgIOWqfVBtT5-6-zsoIFcRr_Vjy-XNTQ6EiR-xtxgtccrc3C7nz_j2skiUvYgA3gTgUbNqJsJBu9-oPiKwOpob1-oxa7SOMIaNbWAzj23-5ofvNwX6wNe56EasTY6tyyieGUtLHTTGCmpS5WN5k-jo1Q3IybXhVM_YyFD3QviT08eJ4z9-quplQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d0b8905a2.mp4?token=MCKgAEQguAIld1A_9WoBR8dvN1VLtRd3ZEjvPj8JTU0SzHrQtsIoJ20-LvvETRmDPEIHehFCwxt_28PMF2auIjN6CxqRO8f0jGDe3GiekRWTIGkFENiLq26TTcZ8W8kT2ajG8Ils91owdcmRGhiDbU-i4S-H5G8FgIOWqfVBtT5-6-zsoIFcRr_Vjy-XNTQ6EiR-xtxgtccrc3C7nz_j2skiUvYgA3gTgUbNqJsJBu9-oPiKwOpob1-oxa7SOMIaNbWAzj23-5ofvNwX6wNe56EasTY6tyyieGUtLHTTGCmpS5WN5k-jo1Q3IybXhVM_YyFD3QviT08eJ4z9-quplQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«وطن کجاست؟  عقلا منطقا نجف»!
وطن‌ پرست‌هایی که وطن‌شون لبنان و غزه و عراقه
و میگن برای غزه و لبنان حاضرن ایران بمباران بشه!</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5297" target="_blank">📅 15:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5296">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">کویت : در اثر حمله جمهوری اسلامی به فرودگاه بین‌المللی کویت ۶۳ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5296" target="_blank">📅 14:20 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5295">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">بخش بزرگی از انگیزه جمهوری اسلامی  در حملات پی‌ در پی به دوبی را باید در عقده حقارت جمهوری اسلامی جستجو کرد.  شهری که برای ده‌ها میلیون ایرانی  نماد پیشرفت و توسعه بود، که ظرف ۴۰ سال از هیچ به گوهری درخشان تبدیل شد،  و مردم ایران دائما دوبی  را با ایران  و…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5295" target="_blank">📅 14:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5292">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RXAg4d9m3z2fildsIFEeiF_hxvaCXPfhNuCe1kpgf1CtsIur_c-10yLssnoGsAllr2txX8Nib4gl_bmXHLlYsoE8DRgsrRPiOi5bQYoL93M_dD0Y55vS8FEPD1owpetQ_0CjpnrOS0mQYM3BQ8CxxuzZ1hbZWo2lLCeJgirtWh-xTdJa2CmkLOHWI4PDleBXQzSy5k1YrQua53DMGPzzPoKsiXdubji8yv5sGS7Ji5gqpPYEb2E-p6oeJYhy3Lt61pNJkUaoWiD59zolz3i0JNUAVrR2dnWuuz1Gcab5haxgivDgnbky6PqOoPmHg3_kDRvh3CaK3TAOvMDanjGdew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e1734ESwsqR2o5BfnS3oqPFzI_AM7D9UotvMeaNmmjDKK4H04dH8YztKNgBT-0Q5MarEpOhBSYlxJuZmatt1OlKfKrrswm7XGShks5gbHiaga3G41Pmsh3X1EQgBGwVwxJuEBniWmEWfJlEwnIY2CrnbHdERtBwPhhhhVSMXJUxZc7yDMwlGhkrwvsCwJuK1Zl5xUtZiuCDsJ75LbVvu1Nri55Wy13HJU9R0t9NNMMyPB7z5oCbKMWbsPuvPufs8fI7f4TSaPPhE7mAhzFlIxR4hiQoHXnj57gMwZ0MVYytEufX5TrBo1OkVLlzF6-eXBq42lL5hqHIHf61zuJUAbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZQg9UrjkJUsJkot8EOtdanfFoBF-KAJOxXJX1hUv-2uWDUIeNIQaKdskVhAraneTbP7JL0EMcSbvVGtP8Y8WMkXgepV-I22IXgSLxd3ptcfZ0XIE6Cu_Xk7KfLxipqgL-zZRZd5s6FYoTS2sUOt8t_ghSY6bRkg3HfTtKIqHcCWtKPegkzEfRe3vBUq8n13QsGFzZ1m1dpTCz24jflgdowjSPtiz3s23AxOEcBHKBwd8MZl2jOz6by0wIDtMT2d1io3Ueuo8uhXS9jsfvxuWuhMHdIc-xh3uEOP_DmYeeow6Dc6uMHzVclCFPKoBWB9NCCWq8Ito7-_5GLypEXGFgw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">درست ۲ روز پیش کویت ترمینال شماره یک اش رو دوباره بازسازی و افتتاح کرده بود،
که جمهوری اسلامی دقیقا همین ترمینال رو دیشب با موشک زد!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5292" target="_blank">📅 14:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5291">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d4bd44367.mp4?token=h-2Khub8dwuLU0mtdtQybAEMgMcGadUHctvcwaA00FjjAlN1tPXDzsbV2LSDlBZFqajGnJkH0jkAJi4ZvHOt_X8fCM_KLQUUPHCe5kNylJAwvBXfQLHjzz_nuPXcKzYRos9k_7ZzU29lZjE_jnGqIpVSMN6vYApZz0u4--2Qmxr6HH8O4ejUfsLiBWC5Rhw_Fnqu0DxPE7-S-PFrSRw2pY0GAeK8GA4nfbII8B8thjmv5HEhIxmZeBvh-Ydv5tGuw8jZiSBJXe5DmkhfvkfFMni4qNva3-dTgFiRXTjzg1vK0KsLXg8DVY8HMIc8PLOKTri__U7Rt1Jaq6Y5Gi8LpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d4bd44367.mp4?token=h-2Khub8dwuLU0mtdtQybAEMgMcGadUHctvcwaA00FjjAlN1tPXDzsbV2LSDlBZFqajGnJkH0jkAJi4ZvHOt_X8fCM_KLQUUPHCe5kNylJAwvBXfQLHjzz_nuPXcKzYRos9k_7ZzU29lZjE_jnGqIpVSMN6vYApZz0u4--2Qmxr6HH8O4ejUfsLiBWC5Rhw_Fnqu0DxPE7-S-PFrSRw2pY0GAeK8GA4nfbII8B8thjmv5HEhIxmZeBvh-Ydv5tGuw8jZiSBJXe5DmkhfvkfFMni4qNva3-dTgFiRXTjzg1vK0KsLXg8DVY8HMIc8PLOKTri__U7Rt1Jaq6Y5Gi8LpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرودگاه کویت - شب گذشته - بعد از حمله جمهوری اسلامی حالا اینها برگردن فرودگاهی در ایران رو بزنن میگن : «دیدید اینها مشکل‌شون با خود ایرانه و زیرساخت‌هامونه و نه حکومت؟ »</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5291" target="_blank">📅 12:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5290">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c026494834.mp4?token=Lr1ROb7msXrQXpyntWm4JY8JNEtdgFfBrRdW6ij7WLcxpalWZNxxnenV_okpWVpVuwcrUdn6yjy1OBVyhWv1BZAY9hqxZBAo1AlE6VxLUbL4g51r8qrSF5fGTv5VoRhHHFtvC4PoKyITg_7CjTGWUEKK1zocrShIvF78i8Bk45lWb8BuQ6zGcdr8drbAlpeY8exftXYkofH2aURb24Tmpw1Heb8pyLh25IzwIZlBYStVWjvqR5i5CjuNgFK0nCZrcxdS0k-IU3eAeozTW2t_8O3r0lNg5vQaIpBr0aBLiV2Tzu8jCAq1VZTTaIBODOPH3CKYTdJza0WonKbauktR6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c026494834.mp4?token=Lr1ROb7msXrQXpyntWm4JY8JNEtdgFfBrRdW6ij7WLcxpalWZNxxnenV_okpWVpVuwcrUdn6yjy1OBVyhWv1BZAY9hqxZBAo1AlE6VxLUbL4g51r8qrSF5fGTv5VoRhHHFtvC4PoKyITg_7CjTGWUEKK1zocrShIvF78i8Bk45lWb8BuQ6zGcdr8drbAlpeY8exftXYkofH2aURb24Tmpw1Heb8pyLh25IzwIZlBYStVWjvqR5i5CjuNgFK0nCZrcxdS0k-IU3eAeozTW2t_8O3r0lNg5vQaIpBr0aBLiV2Tzu8jCAq1VZTTaIBODOPH3CKYTdJza0WonKbauktR6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرودگاه کویت - شب گذشته - بعد از حمله جمهوری اسلامی
حالا اینها برگردن فرودگاهی در ایران رو بزنن میگن : «دیدید اینها مشکل‌شون با خود ایرانه و زیرساخت‌هامونه و نه حکومت؟ »</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5290" target="_blank">📅 12:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5289">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd4e6c7c91.mp4?token=D0KTsGT8zvJ1IlNUsMEcAmpyOzblecWqAO24rfYd476VNLPIZWeqtbXmon_lATmhYhSvF0gZiaX_7N3ImmlBaIGGnGcuLGZY-c0DdvNGNYsjsSO0tWPAqd6WQi2VKFji68fYxUN-IbLkKrBo4VpAsJ-E8zvspg_gfqDIs7ejeeKWW27zzURSxkrwAQ9U8WqNTQ3CGY9aJcyRHjHjLJINA8JqyhX7lrQlQW_LUPxbm6ip6Vni-Cds-6c2eVd0nlGX4DPLKCjUpJZD0z8htNh_5Poe735cusPOniHjCfw13BO9Mi9acvJAR3h6H_IucJRYjbq9OZoooN66qRatvSxcxGzUi33uUp3hpC-a7TyAl4oEh5II4hSyGEq-eBaPXngsWbsgCdc4ojK-YU-RK5whWyDtMRO6M-WWJ23NYxHwqlqOHrmuIX6fSaWc6oyJ4d7BqA2lx_Bs1M4kzSFRfolAj2WJ_cZS7fQXeph5BLgS79JBFgUP1tfNHoKCEfemp8N105vmqTJnS_lMmIsEaIv5eozurPPmJmuQ1zDqor4mC6p2MTTg32TCbIq7I1NK2E5ebUPAA98UwAAAJldIJt3Q5gzR0aczBOqJyhOqGCy5GhqluWBCXQc8LfMPYm0SAoI5aupa9UabHT8o9Mod2LOmA3rWSr-82-sk1bIc72m3xG0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd4e6c7c91.mp4?token=D0KTsGT8zvJ1IlNUsMEcAmpyOzblecWqAO24rfYd476VNLPIZWeqtbXmon_lATmhYhSvF0gZiaX_7N3ImmlBaIGGnGcuLGZY-c0DdvNGNYsjsSO0tWPAqd6WQi2VKFji68fYxUN-IbLkKrBo4VpAsJ-E8zvspg_gfqDIs7ejeeKWW27zzURSxkrwAQ9U8WqNTQ3CGY9aJcyRHjHjLJINA8JqyhX7lrQlQW_LUPxbm6ip6Vni-Cds-6c2eVd0nlGX4DPLKCjUpJZD0z8htNh_5Poe735cusPOniHjCfw13BO9Mi9acvJAR3h6H_IucJRYjbq9OZoooN66qRatvSxcxGzUi33uUp3hpC-a7TyAl4oEh5II4hSyGEq-eBaPXngsWbsgCdc4ojK-YU-RK5whWyDtMRO6M-WWJ23NYxHwqlqOHrmuIX6fSaWc6oyJ4d7BqA2lx_Bs1M4kzSFRfolAj2WJ_cZS7fQXeph5BLgS79JBFgUP1tfNHoKCEfemp8N105vmqTJnS_lMmIsEaIv5eozurPPmJmuQ1zDqor4mC6p2MTTg32TCbIq7I1NK2E5ebUPAA98UwAAAJldIJt3Q5gzR0aczBOqJyhOqGCy5GhqluWBCXQc8LfMPYm0SAoI5aupa9UabHT8o9Mod2LOmA3rWSr-82-sk1bIc72m3xG0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسام الدین آشنا، که قبلا معاون ویژه وزارت اطلاعات بوده، طوری وضعیت رو ترسیم میکنه انگار ترکیه فقط یک فرودگاه خوب در استانبول زده،
بقیه کشور رو رها کرده! اما جمهوری اسلامی
در همه کشور فرودگاه زده!!!
ایران ۹ فرودگاه بین‌المللی داره!
ترکیه ۳۷ تا! چرت و پرت!
یه جوری میگه ما همه جا ریل و قطار داریم
خب پس بیا بگو چرا مردم قم، اصفهان، شیراز  و…..
برای سفر به تهران باید یا اتوبوس بگیرن
یا خودرو؟ چند درصد با قطار میرن؟
۵ درصد مسافران با قطار میرن؟؟</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5289" target="_blank">📅 11:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5288">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vv6xYzMrsogqnhAhQ78_oe3airE5CkaAMjcVgqQGogtJRrv62_1DWZhIJMWDTQR3HI1BGaZrY2lqpXow-AZxrhDRLinrrDik_P8jh_NrnM9D25d1a1SeG7Nw951-qmn-4anvSyQjUsZ_v9uDboMPZsfUlUaLH5rA4-mmRbCn1HsH6vr1LKIEcJ8s1n2-XEO3KqenQsxm46wkmrgvQWax-iHOYOC0eONZ_AUHzwSXk8gbL7krB_UhyjA1x6MKk9DORrGShJzPlj8m4Lt55njFkKhJ1XezEUlirktPburLbufh1_6C29etydq1IBO4vyrUHdW7AhA7GsH8aMu9I6TQ7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساعت ۸ صبح حمله صورت گرفت
(توی روضه‌هاشون هم‌ میگن رهبرمون گشنه و تشنه بود! ساعت ۸ صبح!)
اینها همون بگیم ساعت ۱۰ صبح فهمیدن! اما دائم تکذیب میکردن!
نیمه شب به وقت ایران تایید کردن،
اونهم زمانی که ترامپ و نتانیاهو با قاطعیت و رسما نوشتن که حذف شده!
اگه این دو نمی‌نوشتن هنوز میگفتن خامنه‌ای زنده است و «کمین» کرده
و داره رهبری میکنه و…..!</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5288" target="_blank">📅 11:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5286">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OigSaaKTJDYsBje6RZ9_pH8MIjRSRrK01-zF6kvTQkSSnp_a66h4gfu12G70depLougWvEKQApV7X-6_bTpaW14pg0eq_2waD8yaSStuwgky1SGou5rvq8A-RoVJlil0UxZqk46MowPBVpC2KaZgrngkx6a3cuCTNYMW4athCPqV20lOhgxs5eIRuZzX4myUbonQKfGRT4tvQThTj0IRMKY59INMSWYVIr_s5lZSLobm6Skme-zVdqP3kJpix77eMqO_RDfiOZoD8ZI-8sdzwKV2lXBBOonbGDuMzHsC7JTAXosmWbgJIpz-faoB5HVByqKWyhhkQrSP1sYvKgy0HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/015500535c.mp4?token=OPQMeR3Zh3J8k56fvUVPnvYaE_P5s8sTsE-BUXNDfJkvXjqL9wxeQYLewk2krk1HZL-PyD_y0q-er7iuwhHoJc8xCNqQWvJrzKnYya-UpnscCGV3Zekuhq4rCBX6U1lDbvZmLEVOXDm9oXIG6bx0ImIOdGWfHEHobRhPq8UTYN6Rf9BNqaO7cZzbK8lXY7KQ_Akydbnvx0hVjBcHHRbYU8WfQXZz9qIFReuhU5zSGBW1fJhcxTaY_hPmWWWSglj-KghtdP91mc60zTbjojQUUqS_vURbOarP6jQf0jyqmaekgvwzq3BeQtAF2-1hIfiunEaqtjtgTNo7gMCt9LM42A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/015500535c.mp4?token=OPQMeR3Zh3J8k56fvUVPnvYaE_P5s8sTsE-BUXNDfJkvXjqL9wxeQYLewk2krk1HZL-PyD_y0q-er7iuwhHoJc8xCNqQWvJrzKnYya-UpnscCGV3Zekuhq4rCBX6U1lDbvZmLEVOXDm9oXIG6bx0ImIOdGWfHEHobRhPq8UTYN6Rf9BNqaO7cZzbK8lXY7KQ_Akydbnvx0hVjBcHHRbYU8WfQXZz9qIFReuhU5zSGBW1fJhcxTaY_hPmWWWSglj-KghtdP91mc60zTbjojQUUqS_vURbOarP6jQf0jyqmaekgvwzq3BeQtAF2-1hIfiunEaqtjtgTNo7gMCt9LM42A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت ایران از عراق بهتره؟
این روزنامه جوان متعلق به سپاه !
در خصوص زنان ایرانی بدون سرپرسته،
که مجبورن برای سیر کردن شکم خودشون و بچه‌هاشون روی خط مرزی بین ایران و عراق «کولبری»!! کنن! در کوه و دره!
چون به این پول نیاز دارن، بیا بگو چرا شهروندان عراق، که روی همین خط مرزی هستن،
نیازی پیدا نمیکنن که دست به چنین کاری بزنن؟
اما زن ایرانی بدون سرپرست نیاز پیدا میکنه
که دست به این کار بزنه؟
تازه میگه بهمون گفته بودن به روستاها برق نبرید!
دستتون درد نکنه چه منتی!!</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5286" target="_blank">📅 11:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5285">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">وارونه گویی!
به خاطر دشمنی با اسرائیل رفتن دور تا دور اسرائیل گروه‌های مسلح ایجاد کردن، پول و سلاح دادن، حماس، جنبش جهاد اسلامی، حزب‌الله و… تا دائم با اسرائیل در جنگ باشن، خود خامنه‌ای بارها تهدید کرد و گفت «کرانه باختری» رو هم مسلح میکنیم علیه اسرائیل!
حالا که اونها برگشتن حمله کردن، میگن ما اونها رو برای دفاع ساخته بودیم که بهمون حمله نکنن!!
نه خیر! ساخته بودید که حمله کنید! نه دفاع! که هم اونها رو زدن، هم اومدن سراغ خودتون!
و الا اسرائیل زمان حکومت شاه، با ایران دشمنی نداشت! جنگی با ایران نداشت!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5285" target="_blank">📅 10:25 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5284">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">‏روایت سی‌ان‌ان از درگیری شب گذشته ج‌ا و آمریکا در خلیج فارس
‏ایالات متحده و ج‌ا در یکی از سنگین‌ترین شب‌های حملات از زمان آغاز آتش‌بس در آوریل، دست به تبادل حمله زده‌اند
‏به نظر می‌رسد درگیری‌های شب سه‌شنبه زمانی آغاز شد که ارتش آمریکا با استفاده از موشک هلفایر، یک نفت‌کش با پرچم بوتسوانا را که به سمت بندری ایرانی در جزیره خارک در حرکت بود، هدف قرار داد. به گفته فرماندهی مرکزی ایالات متحده (سنتکام)، این کشتی با محاصره دریایی بنادر ایران توسط آمریکا همکاری نکرده بود.
‏در پاسخ، ج‌ا اعلام کرد به یک کشتی با پرچم لیبریا موشک شلیک کرده است.
‏اما تشدید خطرناک‌تر پس از آن رخ داد که آمریکا یک ایستگاه کنترل زمینی نظامی ج‌ا را در جزیره قشم، نزدیک تنگه هرمز، هدف قرار داد و این موضوع باعث شد ج‌ا به کشورهای کویت و بحرین در منطقه خلیج فارس موشک و پهپاد شلیک کند.
‏ج‌ا اعلام کرد که «یک پایگاه هوایی و بالگردی آمریکایی» در منطقه و همچنین مقر ناوگان پنجم ایالات متحده در بحرین را هدف قرار داده است.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5284" target="_blank">📅 09:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5283">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">خبری که ایتالیا رو شوکه کرده:
یک پاکستانی در جنوب ایتالیا،  با ریختن بنزین ۴ نفر (۳ افغانستانی و یک پاکستانی) را در یک خودرو به آتش کشید و کشت!
https://www.instagram.com/reel/DZF42fzqtho/?igsh=aTJocnQzcWw5dWVj</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5283" target="_blank">📅 08:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5282">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">سنتکام : حملات موشکی جمهوری اسلامی به بحرین و کویت ناکام ماند. موشک‌ها رهگیری و منهدم شدند.
به اهدافی در قشم حمله کردیم.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5282" target="_blank">📅 08:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5281">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RKQztmKk20Sctl5vCCFyiRhcuaO26fionP3yaF-xwXaimkju-o-jWPbl6vW5Z0gPCgKXONbVK9Jh3T1vzXBu0pUVHqHveaZsY4Mh0FpPvCzyGRp3T1FUSN6jhmP4fmZ2K9GWgJpFP2Wj-ws_uqX9kcmlZ367CzH8JZhfRneafja0IcU00jmDWXrNPyOVjk8I99Ct6N5kzW1x9mx1WuzVg5N8tNU5kguMeTOT53YA_yuhTagQD7ugxR7ZoJEJHpngcmRsdud4_aLkIXq4pRZfkl_TaQX2DnZk2cK1aCdUjZFmEXQj_nq13qkmb2I5OswbczX90wI8-5GUdpEl1AsXWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدور حکم اعدام برای دو برادر دو قلوی یتیم فقط به اتهام داشتن تصاویر ساختمان‌های تخریب شده در تلفن همراه</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5281" target="_blank">📅 08:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5280">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
شنیده شدن صدای انفجارهای تازه در قشم
🚨
فعال شدن ضد هوایی در عربستان</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5280" target="_blank">📅 02:53 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5279">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
گزارش‌هایی از حمله ج‌ا به یک کشتی در تنگه هرمز</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5279" target="_blank">📅 02:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5278">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
حمله موشکی جمهوری اسلامی به اربیل در عراق و به بحرین!
حمله مجدد موشکی ج‌ا به کویت.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5278" target="_blank">📅 02:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5277">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/767a4036f8.mp4?token=fREmvhdCSrmk5gC7jldNky1yDz_giaAtYpVQKvLjJ3uj1EYNJgEsVdb0JGHQ0oUNlSjWTkUP46yf08p3y89qdN1N_xdlwWeqAIZ521r8SkTaiqPryBI4mImb8_AB0Iep7_Yw1Wqer8zjfb1ka0do4pGAn_uVLYLiKaLvLEpjJi3BcvcXSLKDfKDewB31eBm1nXhTROGxXhfSnGA6vOkdFaxGIDx_cfjMw_JgwMvoK4whZZcUBhXpKRJyE-y_60OPX3nqhI7nvHifY8KJJMcF-ebVuf5vAUKw0G3V3_oRuccBYvqAG7cIfNtm93IOlWwLt3PiF9OlwdGPI5wBCUhYMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/767a4036f8.mp4?token=fREmvhdCSrmk5gC7jldNky1yDz_giaAtYpVQKvLjJ3uj1EYNJgEsVdb0JGHQ0oUNlSjWTkUP46yf08p3y89qdN1N_xdlwWeqAIZ521r8SkTaiqPryBI4mImb8_AB0Iep7_Yw1Wqer8zjfb1ka0do4pGAn_uVLYLiKaLvLEpjJi3BcvcXSLKDfKDewB31eBm1nXhTROGxXhfSnGA6vOkdFaxGIDx_cfjMw_JgwMvoK4whZZcUBhXpKRJyE-y_60OPX3nqhI7nvHifY8KJJMcF-ebVuf5vAUKw0G3V3_oRuccBYvqAG7cIfNtm93IOlWwLt3PiF9OlwdGPI5wBCUhYMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات امشب جمهوری اسلامی به کویت
و انهدام موشک‌ها در آسمان کویت</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5277" target="_blank">📅 02:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5276">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">سنتکام:
نیروهای ما یک نفتکش خالی را در خلیج فارس که به سمت یکی از بنادر ایران در حرکت بود، متوقف کردند.
نفتکش توقیف‌شده توسط نیروهای ما، پرچم بوتسوانا را برافراشته بود و خدمه آن به دستورات داده‌شده تمکین نکردند.
یک هواپیمای آمریکایی با شلیک موشک به موتورخانه نفتکش، آن را از کار انداخت.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5276" target="_blank">📅 01:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5275">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ارتش کویت : حملات موشکی و پهپادی به کویت.
برخی از رسانه‌ها از شلیک سه موشک از منطقه‌ای نزدیک شیراز خبر داده‌اند.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5275" target="_blank">📅 01:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5274">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
شنیده شدن صدای آژیر خطر در کویت</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5274" target="_blank">📅 01:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5273">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
خبرگزاری مهر :
شنیده شدن صدای انفجار در محدوده جزیره قشم
‏بامداد چهارشنبه صدای انفجار‌هایی در محدوده شهرستان قشم از سوی منابع محلی و ساکنان این جزیره گزارش شده است.
‏
‏بر اساس این گزارش، هنوز ماهیت این صداها به طور دقیق مشخص نیست و هیچ‌ یک از نهادهای رسمی  نظامی و انتظامی تا این لحظه درباره علت وقوع این صداها اظهارنظری نکرده‌اند.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5273" target="_blank">📅 01:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5272">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e42bee8bd9.mp4?token=SmashrtQqTO8A6MItFgiGzZQHdsQ80YiKldWdyuX1K2w_siDCWjvwTOzjWo02ttOPH1Yn0vJIOj4Gnyav2FRCBXdZ_OXwfBY4fxwEY1cJry9T9eCY7b7QzBBjB5cVpuHcleOohB5U7y6CYAyOkpR6LHLf597wdvj7KwtvRHzhVU45-lEuQ9kVoS2os-eZbhKyO_aMdh-e03j_P5ShRC6bwq29x7NthG1cdki2K3aaRvHxomRnYjFcMmJUwPLdNtFSCfrz8qZh8JShGkY4u7uK3ROZa7rIB3br7HBw8rHckb80CFof7W-khcAL5kqgHzpxmsNy0CBLGApC18XTYEKjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e42bee8bd9.mp4?token=SmashrtQqTO8A6MItFgiGzZQHdsQ80YiKldWdyuX1K2w_siDCWjvwTOzjWo02ttOPH1Yn0vJIOj4Gnyav2FRCBXdZ_OXwfBY4fxwEY1cJry9T9eCY7b7QzBBjB5cVpuHcleOohB5U7y6CYAyOkpR6LHLf597wdvj7KwtvRHzhVU45-lEuQ9kVoS2os-eZbhKyO_aMdh-e03j_P5ShRC6bwq29x7NthG1cdki2K3aaRvHxomRnYjFcMmJUwPLdNtFSCfrz8qZh8JShGkY4u7uK3ROZa7rIB3br7HBw8rHckb80CFof7W-khcAL5kqgHzpxmsNy0CBLGApC18XTYEKjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد عمرانی</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5272" target="_blank">📅 23:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5271">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">به درخواست فرانسه، امروز شورای امنیت سازمان ملل نشستی اضطراری در خصوص وضعیت لبنان برگزار خواهد کرد.  پایان این نشست قطعا چیزی در حد صدور یک بیانیه خواهد بود و یک محکومیت، هیچی نخواهد شد!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5271" target="_blank">📅 22:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5270">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d52501c2e8.mp4?token=iUOftqVIUY_HOIO5mXON3JLdlOHf5TOd-ojDQwP7eNiJiAPOm-hY-ML8oj1Kr4ljiD7WQ1SCL8BlzsY9CwQSY7MZ_Zc740cxUi9u2xLcTeUPqMlstGFdudHV2_sc6T1hFu5Agv4vkrf-_R7Xiasb4xs-OEpu2bsBE13433ogcuHgY6Oi7KWsNLmH96qn2uUw9fOrxQ3JJZ6PIOcTN1aNa8AxSzVVV7fNi4wHdKGmSb6oUJK3ijWAukN9XlEkwEwefUjcHzgDvKn21jfaF8t6aShH3Iwg1p7i6DB3rlzJCIkGw3won9UI5rKbFPb1CyhQpfx4qX_sfpK1Lsj0U14JgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d52501c2e8.mp4?token=iUOftqVIUY_HOIO5mXON3JLdlOHf5TOd-ojDQwP7eNiJiAPOm-hY-ML8oj1Kr4ljiD7WQ1SCL8BlzsY9CwQSY7MZ_Zc740cxUi9u2xLcTeUPqMlstGFdudHV2_sc6T1hFu5Agv4vkrf-_R7Xiasb4xs-OEpu2bsBE13433ogcuHgY6Oi7KWsNLmH96qn2uUw9fOrxQ3JJZ6PIOcTN1aNa8AxSzVVV7fNi4wHdKGmSb6oUJK3ijWAukN9XlEkwEwefUjcHzgDvKn21jfaF8t6aShH3Iwg1p7i6DB3rlzJCIkGw3won9UI5rKbFPb1CyhQpfx4qX_sfpK1Lsj0U14JgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی تازه منتشر شده از ۱۹ دیماه - کرمانشاه
و تیراندازی به سمت مردم</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5270" target="_blank">📅 18:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5269">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1239a4e0f4.mp4?token=EnbtxzOT61mgXdc2stqkzCtUAiskEdnHKyZXGsKCD5efzDJ-p3kE-p6Ct4PyshyJs7-mrtNUb3KX2Wp5nIDgTB3Wi_FT1C4wXwcJmbAgzwoLzXaICxmB6J_F8qIYnntn8khIX2lYgnhTn4yHLzROv4Zn2832ou-VKd96e5xHzfg8iVBlWS9E9NVN9YKlmJjI4zEL4tMqz-FREk1HS0-e4xXio7oatRSr3NdFbeALvA7YXkhjg9srsJXMjJK-pIkb_BFfKNlRDDgoNgqSN5K1ouD0ziYdd64r7AoPIEta4I_nKjHQE9gr42I-e3mkDw0brQjtKNzjt9Tz0BlcxaBQGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1239a4e0f4.mp4?token=EnbtxzOT61mgXdc2stqkzCtUAiskEdnHKyZXGsKCD5efzDJ-p3kE-p6Ct4PyshyJs7-mrtNUb3KX2Wp5nIDgTB3Wi_FT1C4wXwcJmbAgzwoLzXaICxmB6J_F8qIYnntn8khIX2lYgnhTn4yHLzROv4Zn2832ou-VKd96e5xHzfg8iVBlWS9E9NVN9YKlmJjI4zEL4tMqz-FREk1HS0-e4xXio7oatRSr3NdFbeALvA7YXkhjg9srsJXMjJK-pIkb_BFfKNlRDDgoNgqSN5K1ouD0ziYdd64r7AoPIEta4I_nKjHQE9gr42I-e3mkDw0brQjtKNzjt9Tz0BlcxaBQGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب در میدان انقلاب تهران چه شعاری میدادن؟
نحن جنود الدین و العقیده / لبنان لن نترکها وحیده
ما سربازان دین و عقیده هستیم،
لبنان را تنها نمیگذاریم
(همون لبنانی که سفیر جمهوری اسلامی رو اخراج کرده و میگه این جنگ رو جمهوری اسلامی سر لبنان آوار کرده)
فردا که جنگ بشه میان میگن :
موضوع ایرانه! تجزیه ایرانه! برای خاکه!
رستم تهمتن و آرش و شاپور و…..!</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5269" target="_blank">📅 17:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5268">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">حالا اینها با همین سوابقشون!  بزرگترین حامیان غزه و … هستن!  دوستانه بهتون میگم، روایت فلسطین و مدلی که جمهوری اسلامی  به خورد همه ما داد، و اینهمه براش هزینه کرد و پاش پول میریزه تا همیشه جنگ باشه و خصومت باشه و…..  نه تنها از بزرگ‌ترین دروغ‌های یک طرفه …</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5268" target="_blank">📅 16:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5267">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bLWoHvqzucNa40gZkxtjdG-jrU-yoakbrQSrp2MhcENPoQLZ3MBpqD2-GCJoECEYsayrdBEjrJa5m-WbvEsYYHQ0ljjQzen4lbvnmd5M0yoUZjxvUf8lmhZhg9wsljas12Jjb4KWdRCCzLHGpsk3hnEbO1lI0fIgf9Q1zdQklNbjot8w1s8kWaQ0jlok7221guhXN0OA7Zdq7HFb_mcRBLmJSQdqQ604GZ-RPvsd_0wTWrDzRLy4ubSMaGtF5czXUsjm7Nlo5e7G6jxF2DZdExD6nyvduQ8CyFpQ7oI77ZQMzzrAGEiXr0_m6NgXU6wLE5cOKNYL-h4GIMnEkwhf4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۰ سال بعد، در جریان جنگ ۶ روزه شرق بیت‌المقدس این بار افتاد دست اسرائیل!  ۳۰ تا مسجد اونجا بود!  حتی یکی از اونها هم خراب نشد!  همین امروز ۳۶۵ هزار مسلمان در بخش شرقی بیت المقدس زندگی میکنن!  در حالی که بخش شرقی بیت المقدس تا افتاد به دست مسلمین اجازه زندگی…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5267" target="_blank">📅 16:05 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5266">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i3v_hk_siLD41AARmjjiShuWqX5-IJh6tyBeI04G2JYrN_qS4t1UQDsoIZsPNdQADY3SGZmWxTqSr7qPH8sYQa6-4wQZ7ZxVyeVtz_t1Ngd1AvG7sp3eZTWuKGMG-dUSKsxrUtTIMAqeremTacE6oiTENLAo8t7xOGSdWuFlA5iZnwRmQQloZJXAh5dnYA-by_QlFMmBWciiYN5P-w67DqVAX0aWxUIpd_jkNNZ52SvvfLuzn42ZlSuEXEgDSXwLynQ6CaS2ctN0vwlq-mON2VcqjweSVctb1mDovdVTl-Wefj6ollkAQeqPZ7U8dxymHs5u4KLunMpErRVD0Y8t4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۴۷ در جریان جنگ اعراب و اسرائیل،  وقتی اردن کنترل بخش شرقی بیت‌المقدس رو به دست گرفت، دست به اخراج «همه یهودیان» ساکن در این منطقه زد.  منطقه‌ای که حداقل ۳ هزار سال یهودی نشین بود!  یعنی از زمان هخامنشینیان این بخش  یهودی نشین بود! و ربطی به اسرائیل…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5266" target="_blank">📅 15:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5265">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pPauDibe4llyiWKHaRpMyaSM2nE3vihMqtqOVqMUPeV9K8DaUzpMGGd8NCPccjoITGca_ztSiqrsSUvg9lDf__Y0BuM2Gsim9nDvkPVYMFoxR79t2XLr9_9c9LqBKNTueLJDshmvrxf1mr2gYpFykk0wiJAuWyxz_bB5LQPLfJiQYfMBtoZeXAd6dp3d-MgRGwYV_W1h-v9RJoR5SbYNOBxXVO2RSv1X0dJEsNyIrKgoTNGpZxWIpKh7bq6tmHC73UMmWHYhBt03p7yP_LG3c0iOC1lPt893GgRbt4rXUw1Sni4oOC09KbS9_I3vT16kTCeg0eKaNg5Vc37YboDUvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۴۷ در جریان جنگ اعراب و اسرائیل،
وقتی اردن کنترل بخش شرقی بیت‌المقدس رو به دست گرفت، دست به اخراج «همه یهودیان» ساکن در این منطقه زد.
منطقه‌ای که حداقل ۳ هزار سال یهودی نشین بود!
یعنی از زمان هخامنشینیان این بخش
یهودی نشین بود! و ربطی به اسرائیل به عنوان یک کشور جدید نداشت!
دولت اردن نه تنها همه یهودیان رو اخراج کرد
بلکه ۵۸ کنیسه یهودیان رو هم با گذاشتن مین
منفجر کرد! فقط و فقط «یک کنیسه» رو نابود نکرد
که البته غارتش کردن و فضای داخلی اش رو نابود کردن ولی دیوارهای ساختمان سالم ماند!
۲۰ سال بعدش چه اتفاقی افتاد؟؟</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5265" target="_blank">📅 15:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5264">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mRx9F-rQUHkUnLjcurnPCIbobOVCAcBDuRvYvzAjfGaO_0Tk87AQPtW2CGJOsZZXP7nQDLNB-tknnv--AnHytCrcZOaRCacSHC2gx3TzEoyeybHcbTu0g8zOVl_oM2rwMXsbuycHxF6KYZOgdz_-PokmzL9jBZ87K5Q0oWnfMMBxkNrLjK_xMpsQ2ydZyFTD1W4aJN5iidipJ3bGvHSZD_YJ3yQX8p_SLjNcr4t-cwvDSLRtI-cdDG7sycoH6wN63CWDnnRoOXBHuKuJt8jdqxrxmlL-iDAz8fRqHmjuzIYc0e5vYWYXUHiFzY2-N3UF5nKe-zbdl-zCjoNgzfDD_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرهایی چون «ازمیر» و «طرابوزان» و…..  کلا مسیحی بودن. طوری که ترکهای مسلمان بهش میگفتن  «ازمیر کافر»! جمعیت ازمیر، که یونانی بودن از جمعیت آتن! پایتخت یونان بیشتر بود!  مردم همه این شهرها رو بیرون ریختن و یا اخراج کردن از خونه‌هاشون و فرار کردن  یا اینکه…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5264" target="_blank">📅 15:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5263">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hw2LGOA8ou-ItNecbtIegEHXAqkSf_XVncsTx34yN-wURYZx8vv2Nl9JzxgsXqPmGB3ajwQld6ZdPB-DKdgTktZlNf-ic9rrDHeae3uijDBK-4tt9B1nXN3krhMpdoMLjJxDOBKubvflcved6YIQbxjYqZwMEVOSjtBLqhnTqRxH8pkBU2ARHQsP3QP3VK6GRuH_5qOKccZJLLuxPEaWzCDKKXw-C8o2NxpqnpAVoRoGhvp5su6Bm6-b-HFYZytxrBZs3yhrdV6ybBN9hT5hlcGNxmWcZYcaMMdxrxf47zbWE3tCdKPJYJT_0L64nZdzLGCls8l_SR6D3MOwkvu0qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمر این بنای باشکوه و عظیم،  کلیسای «ایا صوفیا» (صوفیای مقدس)  از عمر پیدایش اسلام بیشتره! ۱۵۰۰ ساله است!  همچنان باشکوه سرپا!   با وجود اسکان گسترده مسلمانان در این شهر، این شهر تا همین حوالی ۱۰۰ سال پیش (تا ۱۹۲۰) نیمی از جمعیت آن مسیحی بود،  ارمنی و یونانی…</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5263" target="_blank">📅 15:26 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5262">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nypp1ovGoMy1YsqLrws8Vh-1TQS5nZ2TT47bssHsaBewEf6WpgWHgDF6zTL0DWDDC-5m5XytwtqpVOn4tvyKdfk8-cGx8HZ5l5rceXKqBVHUiBHZFcfGzdFK6SOZkkcCtJn6w64_uq1Iq4OQlUyqUnYGDjJP0YjST7d5tp2_cjSlcqQyEDAd-2AVV9D_8jl0CASQ4_zHObZS_qXKZvdzTdceqJj6O2tzeSf2xBS313422C6K5OTF7F1WDumfVnEQCAsCOPJGkzVT66lCs59uzDRyOCNctTPosCpXOKNTZ5Q6pifA41tuKMi8ljq6vMdJG_yPyHoIwb5hMmqQgDLNDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استانبول برای ۱۲۰۰ سال یک شهر مسیحی بود،  برای حدود ۹۰۰ سال در برابر حملات مسلمانان مقاومت کرد و تمدن رومی - مسیحی - یونانی‌اش رو ادامه داد.  تا اینکه «سلطان محمد فاتح» استانبول رو تصرف کرد از اولین دستورهایی که سلطان محمد فاتح (لقب فاتح، که اسم یک محله در…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5262" target="_blank">📅 15:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5261">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M3QDbvvgWJjXSO4A6tEr4X5l7e1n-J9824VTk5Twm7Z8_1WN6L0IJMLkB4b_wzQUmWfJ9hzHf6C7gWtGPlcigdSO0jBBWqCyryo5gqmLGZ-d7I9T-MhKGXrN6qc7zjqI6zqqrubzHGCrqSLFRVBfTOWdUR-r7sHynYT0dR5FWFOLb-X2z6SZTy4TsE7F3qI9iHyh6V99xjYPzZe6Jd166HobWXjS1dIM0DWVBzANJ2SgCZTp0vJJVFCEMN4i3bUzvIFfZV1V1hI9dp4OskWcTHOZMXAK8GaF5ilF5V1EZmG1867kDcxp7VpApf2ZYX0V9SB96oFl7KQNwcr8t1ffkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اردوغان میگه :  «استانبول  تا قیامت یک شهر ترک  و مسلمان باقی خواهد ماند ! » به نظرتون چرا اردوغان باید چنین حرفی رو بزنه؟ در خصوص یک شهری که ۱۷ میلیون نفر جمعیت داره؟ ۹۹٪  مسلمان!</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5261" target="_blank">📅 15:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5260">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64175a1cdd.mp4?token=bbaExRMkvGOccis42tlAP6PGhR7Ar_1odKV4A8z-AbIspYZ1EltRi1X2ejhNSpqcBCTFHdDzOLmH33pVdJAT0mEAS57KvfCTPgksRli9C9n_8XFmNrupdlaBBmuWRhC_MGk-EHKgqRweB7WUfRnjKgrWtOX82Uxj_cs0gOqHjjyhEJ3inh-YT66XE4zLWOw8skxft5kWGPtEpIp3vFZWhc8LtdcyDaNjkxX_IB7NBo4pdCMb9-tlvFf5B6YcQg4L20EBnipZPZimB02gXgekHAXFgvDvJm66vRjyCrZdAzRuSUbCWitpfrxEmZWbVCmrBKjPryCqMtRyzHl3qw8xpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64175a1cdd.mp4?token=bbaExRMkvGOccis42tlAP6PGhR7Ar_1odKV4A8z-AbIspYZ1EltRi1X2ejhNSpqcBCTFHdDzOLmH33pVdJAT0mEAS57KvfCTPgksRli9C9n_8XFmNrupdlaBBmuWRhC_MGk-EHKgqRweB7WUfRnjKgrWtOX82Uxj_cs0gOqHjjyhEJ3inh-YT66XE4zLWOw8skxft5kWGPtEpIp3vFZWhc8LtdcyDaNjkxX_IB7NBo4pdCMb9-tlvFf5B6YcQg4L20EBnipZPZimB02gXgekHAXFgvDvJm66vRjyCrZdAzRuSUbCWitpfrxEmZWbVCmrBKjPryCqMtRyzHl3qw8xpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اردوغان میگه :
«استانبول  تا قیامت یک شهر ترک
و مسلمان باقی خواهد ماند ! »
به نظرتون چرا اردوغان باید چنین حرفی رو بزنه؟ در خصوص یک شهری که ۱۷ میلیون نفر جمعیت داره؟ ۹۹٪  مسلمان!</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5260" target="_blank">📅 15:08 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5259">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EptsL3xV3B8Sh2tnGYERvUQWemJ3DYGzvLN0NyvrwDMZjUgmA50ZGZz_9elEWUQqxzXYegG_Wc2yqftyCakHFFmHFsibap8z8oXy24feuuqf61TgFD0zBFM-WarsNxzTIfxAp78aOmTtRjyECviNix9_tV_e3QUcXrs20b3l56HMCRb3VCn6t-X5QECN2zDqViDw1zcEukLNMiKKQu21XA_DYf0WBOvSCWaoSYKuIywHbC2EX1a3cpEZFg7cDPWZTPb51fXOg63s5m96Mn5KL-U-CEkQm-8qx2rxj85wxNi0PyqomihE9hiUjwtA8nL7mYqn8wJy8K4wAjNZsKF83A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمالا شنیدید امروز در تهران و چند شهر دانش‌آموزان تجمع داشتن،  خیلی خلاصه میخوام یک نکته رو خدمتتون بگم بیاد دستتون جمهوری اسلامی چه موجودیه!  در حالی که رئیس جمهور و وزیر آموزش و‌ پرورش به نوعی درخواست دانش آموزان  رو پذیرفتن،  اما «خسرو پناه»! مخالفت کرده…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5259" target="_blank">📅 13:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5257">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gY58HqD-keRRNzW1Bf3lyDd3xl1JvFznYI-UIpFshSZKoDoX3VkpDNlJs6KknwVW5D9p0AqKLYgs1okHFWd2H0j3oz-cps2Y8WLqvYcMYENSLTqvrtZe4oSJiQ5H82Ym-IBhKE730SermqXzPdyfJzBRphfv2BoUc-fqJoKyJVEQt0_JcbK47Rk5rxoqlvVvIIHQca9pnb3-3GybVuEM3QW9OilXC-t2IAmskHfQA8ol_qcQtCokse6fKSnBMCbuTPL-cCMTQw1FFrkk1Uu1n_xgXfpkvd4lAI7GX27mpwzhAvELdwcca18aeIsAXj8Qr99pl-C9F_uOjzeOF18s9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U9ZEeNfDk6tl2hM6NrEXdgEjgwd73qejyEOsfe4dIQ5EH9re2_lGyGlt7pbxgHwB-XYHBvYFN3i59InRL9_IRLOOhFXJwThEPGkSUbUEp_x8ni39a-LOtHQ1sSeH6X-sBhxBb3MkmjqtaUBxftSzh4JII_ytj3GhcAIBlFFS9_YRGNFH_6dzzwiJsDugGyo06-els_uB3SU2l5OW35RJ5AxqiyrZS6Mc6MKGotgswN5Sl3he4bXWQKw4szToQCczryLVpWvU5zPVwbpNlB2yQvWaKCu_mxIrwMjhcLJOJpkJgBoopdDGZuIKFHTjsBm41T_1c6MM83t_o8GG97RsYg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">احتمالا شنیدید امروز در تهران و چند شهر دانش‌آموزان تجمع داشتن،
خیلی خلاصه میخوام یک نکته رو خدمتتون بگم بیاد دستتون جمهوری اسلامی چه موجودیه!
در حالی که رئیس جمهور و وزیر آموزش و‌ پرورش به نوعی درخواست دانش آموزان
رو پذیرفتن،
اما «خسرو پناه»! مخالفت کرده و همه چی قفل شده!
خسرو پناه کیه؟ دبیر شورای عالی انقلاب فرهنگی
که توسط خامنه‌ای انتخاب شده و نهاد به قول خودشون انقلابی است! و قدرت و نفوذش در مدارس و دانشگاه و….. از رئیس جمهور و وزرای آموزش و پرورش و آموزش عالی بالاتره!!!</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5257" target="_blank">📅 13:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5256">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JSYpBU0N07ib06bhfAgOeUuYs6iG7OzWzx8sns-G1fskPhKge3ITX-8PKwfWV96bNkYHb8G99B0gu5tstoMukjx4rfk5jgMwjGryUzbp8oU4a1CL-cZzyisePte0wa_Cdj7-YI1WVSvMDVRSLKELOJ2XgAQB9e-17RprPk6-YwW0c7Z1tFQ1YGw-3TkdpW_CjRw-IGtFcxB6iRInmhIKdId2E5FLUZ94RlTX74gctyY2kuLrhznVKCO9M42dtDBwoALEgimLLWhZgcdyY1T-IDBN7G3IsZc7e3KRBPRZ_Pk_XGN7Y4QNKtLrBrAhv2WaVua0C84vSUz_ezuUTb-2lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئوی این گزارش به تاریخ  یکشنبه۲۱ دیماه</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5256" target="_blank">📅 13:06 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5252">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DFflQ4ojLuvnN_VwMBCI5TNjgo4xij9_91_TzYNYAK9mFuVN0mDOUt7m6gR30oa98SJZLOc9_Vofb394_7HI9ByT0GcDn9mVRT9_Bvnvox159sRHAsg4rCYeQKZwUSYYctjaN3g-YBwQudFDJ36UEh0OTc4KZ5BHrn5ISb4o2eSHT0qUtAxvO3Y4-5sBcZ6BGXeqrjO9n2-_o-rpMGhXuatLmHpC6xLVY_4trQ5njZugVZZkenw53FnrGB9CpiBe9h3y6gycyhdyUxgegKhGBn0rbLRWSNn2zInbfXOK_H57w2gJmp6o_3k2gzpCx4ZIxYsOsh7aBJNuj8m350QRLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vCI6fwPOTDZuEEe0Ns92HmQ0me0phBW1NAHcVKLyuyS9VLac-4YzOO7Z9rto1jnwmB55xUUsTmRZTw2ka5U2bPsRye6D5ER71zJIfSmPwAqW_nbeEciWf2tCA6ghEjHFbdlic9blZYumAOer8jh_E95qISP8394aLtPdICNEHZEnM1E_1CfrIg_LeltjR_1MTwZtmsxR01rqE5YGNrK7fwo5b13Q-Dix3VBgNKPIcT1dgfBpw-_AvueMJNRI-PmsCTfqnKc_fQigMnuiaukY6z-HNlv2ddZcv8Opc4GrH3j0Zct9Nj7TBGSVbVWYXtYHInQ7SnSnJ6FvSx12LRcwMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I98eVln9pJ8edT0s-es-5q1FpBfzfBaQdKe3FR3k6X-LqpNOELDAygVjr0aDpnt5T8opK9BerROqCs-9w-_Byqy6wvIe0UC7yg6PM0kKyYNIpEBDFrdzQb2JeRvZXLcwaAkw-GyBDIskxI_btSwO146f5WdbUWUd5wZX5BWwfYKEsbBp4xw4sz1WsRDEdhEVa1wj5xZW8lnJlBSF_EbEkDhG6bGmD2Agx2LgScGjp-EMhMRL1XJIli_3fCJCd1qdAXlUwm93-__WnKwhewo3tlFdpQNs49l5GRhNnumRXVV-McaC64ELUscXmIWpZpbmzyO0eIMSnWAjAu5G5kqrhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P9nw0vlQOjmj0IPSZ-5ASw_aMZgAGWzebQjRIIjhiE31pnXGOwt8GhYpSu5VxgzBws_bnpRO2X0M2Tb3I4O1SZXpSDopEooagj778GshEWkDNuBYEwNbaTbcKp2TJIYfvXICajNVv4pDiR_oWgUmnFV6WMKZ8NJdUrCZ9fGNrL25g0wA6CkGn9-ltDwt269SfUwCW8BkLDhxELDj2q0LfV-NjVBpt7k13VxES7Uuft7zi56tfVR0dD-VvYRdCOS9Ku14Wvj4mZG7RilcyqGBIw2S-mjoMQQbTO7ah6D5-8HXQNSxVRAXFb6I149EVmy8f1yeE26JWpjNgGYUvy1KXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">و بعله! خامنه‌ای و پسرهاش
خیلی ساده زیست «بودن»!
فقط در زمان رهبری خامنه‌ای، برای خمینی مقبره‌ای ساخته شد که هیچ کدام
از اهرام فرعون‌های مصر،
حتی فرعون‌های مصر!
به این  هزینه و گرانبهایی ساخته نبودن و نیستن!
این فقط و فقط «یک قلم»! از ولخرجی
اینها از اموال ملت ایران بود!
در کشوری که هزاران مدرسه‌اش توالت نداره!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5252" target="_blank">📅 12:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5251">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25938e5740.mp4?token=sZWP7bgIwyEi_YfZzjt5VOMlPdqU5OgY-DCqjSsMihUZB_KXJoMHz_Q7UwgltQBpbbrbi5RaWfqQ_eHtN3e07IeC1opggmRb2yqTCCBN5ThLXSn9rcj69hMXyVk1FGqbvREGAR4n1xvRpf5h8KcQUgz0dBIP70_6D47GzdIT9ILQq9Q1M4vki3go04Zy2mU5p9etOXlCtCqiQNXE_G3s9hTu5Um204Gc8io-RunCgKyOGcYrjvTgPthjgQLQ-M_bpaSJHYEfv3tRE42lLcuv2NCawPIwq-XO_r4TnYtKHzd2nzaxJtRsD1E4mcfAPVPu_1eQycrnvC1y73vgwyQx4gv-1nXhto5Csl3qLBCw74wnmjDOsMH3qU1ujr6TkYMXLpXo9za3w2tnXDOcnaXdEZBVcT8NiG4Mx1TWLkkOHgWpVc-M0nTGZ8Q6i3MUsaU-sBRSYDVTCyYqFdimiJ3aKy_L-_e_xjUtEgCpUszu0frBqINHAiY4sGgsWQz0kSXEDbKUbrbMgTyMhmrXaICIvpf9Sje_TJL0-Xy6AMVFrP2PAWCxPi8-cyLpsp1W3Tydbgjtejn-GkLLCVvzVW7fkShNEf_7TSqeDCu6OxTNMur9mE3JICxqd3eQ260G0YxGaoxVxgjJmNLKQgxVpIV0_bQ6oR6pEi9hbzzmFjixRfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25938e5740.mp4?token=sZWP7bgIwyEi_YfZzjt5VOMlPdqU5OgY-DCqjSsMihUZB_KXJoMHz_Q7UwgltQBpbbrbi5RaWfqQ_eHtN3e07IeC1opggmRb2yqTCCBN5ThLXSn9rcj69hMXyVk1FGqbvREGAR4n1xvRpf5h8KcQUgz0dBIP70_6D47GzdIT9ILQq9Q1M4vki3go04Zy2mU5p9etOXlCtCqiQNXE_G3s9hTu5Um204Gc8io-RunCgKyOGcYrjvTgPthjgQLQ-M_bpaSJHYEfv3tRE42lLcuv2NCawPIwq-XO_r4TnYtKHzd2nzaxJtRsD1E4mcfAPVPu_1eQycrnvC1y73vgwyQx4gv-1nXhto5Csl3qLBCw74wnmjDOsMH3qU1ujr6TkYMXLpXo9za3w2tnXDOcnaXdEZBVcT8NiG4Mx1TWLkkOHgWpVc-M0nTGZ8Q6i3MUsaU-sBRSYDVTCyYqFdimiJ3aKy_L-_e_xjUtEgCpUszu0frBqINHAiY4sGgsWQz0kSXEDbKUbrbMgTyMhmrXaICIvpf9Sje_TJL0-Xy6AMVFrP2PAWCxPi8-cyLpsp1W3Tydbgjtejn-GkLLCVvzVW7fkShNEf_7TSqeDCu6OxTNMur9mE3JICxqd3eQ260G0YxGaoxVxgjJmNLKQgxVpIV0_bQ6oR6pEi9hbzzmFjixRfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداد عادل پدر زن مجتبی از فعل گذشته برای مجتبی خامنه‌ای  استفاده میکنه.  مجری : رهبر جدیدمون آیت الله آقا سید فلان!  حداد عادل :  ایشون از آقا سختگیرتر «بود» !</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5251" target="_blank">📅 12:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5250">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1710c62683.mp4?token=vGX0x5tcomRSYdTqo9TEhyJAFHMlx6WDr67GD6avxZplSeyXkfgRKgK1IyFMPSNimVL26GSFtKjiinsJyXVUAfRnxCzTWRvZ39SsDX21dpBY36YlN1PyBJwUbO9dn3q8qw9ivsxueV8MQUfyu6dWDUndAMBoF6IXjn2YBLI4UdT2g-aEmQgMyuQxD4ilmJK9sOyzIQK56SnBq3sAx34GOS6Qq4bosRoN8ONomaI5Oele9_P_68BZwMW5AljzLFLslqXv9QDVLUK2izyelmbmnW7RXZ6rdOoO9um4nwDuiZAavBQT-1lgWm9BK4FHRSnC-dz1bicUdH9iwc-qKyuCgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1710c62683.mp4?token=vGX0x5tcomRSYdTqo9TEhyJAFHMlx6WDr67GD6avxZplSeyXkfgRKgK1IyFMPSNimVL26GSFtKjiinsJyXVUAfRnxCzTWRvZ39SsDX21dpBY36YlN1PyBJwUbO9dn3q8qw9ivsxueV8MQUfyu6dWDUndAMBoF6IXjn2YBLI4UdT2g-aEmQgMyuQxD4ilmJK9sOyzIQK56SnBq3sAx34GOS6Qq4bosRoN8ONomaI5Oele9_P_68BZwMW5AljzLFLslqXv9QDVLUK2izyelmbmnW7RXZ6rdOoO9um4nwDuiZAavBQT-1lgWm9BK4FHRSnC-dz1bicUdH9iwc-qKyuCgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداد عادل پدر زن مجتبی
از فعل گذشته برای مجتبی خامنه‌ای
استفاده میکنه.
مجری : رهبر جدیدمون آیت الله آقا سید فلان!
حداد عادل :
ایشون از آقا سختگیرتر «
بود
» !</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5250" target="_blank">📅 12:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5249">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XtNrICEG-v7ORqcwJjgPkPVMApvQGDR_viCx-gplidAs-Yq02EzGp23Lw8zZ-pcTU4aKg5hooRv91wIeIv9iF66iY2GkTFXowcCNS9IlGMDNbxv9zz4TCaxPaDc8-doxL1cznczTf6-88TPeszov2kVza8fzJI9SV6NuR4nrs5xVEqAVc0danZPI27zenVjCeLoxp0ZZEzPCWfBd_j1hwyxwvPS3er6sK6huexafHwyT6bDyE455TQgJMh85ZL722NKGBae00CLJckhrv7ICPTQ24Uoo6o53A55xnhb-c0dbcR9sDfAOLw12RsmtOG37EGm25a773ATWC1FueJYDqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف گفته که اگر حملات اسرائیل
به لبنان ادامه پیدا کنه، در مقابل
اسرائیل خواهند ایستاد
‌ و «زنده باد دفاع از سرزمین مادری»!!
میخوان وارد جنگ بشن
برای دفاع از سرزمین مادری!
حزب‌الله برای چی وارد جنگ با اسرائیل شد؟
برای خونخواهی خامنه‌ای! که
هیچ ربطی به لبنان و سرزمین لبنان نداشت!
اینها فقط برای فرقه خودشون میجنگن!
نه ایران و نه لبنان!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5249" target="_blank">📅 01:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5248">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">قالیباف در گفتگو با نبیه بری (چهره شاخص شیعه لبنان و رئیس پارلمان):
«جان ما و شما یکی است و پیوند ج.ا و لبنان ناگسستنی است.
در دو روز گذشته، ما به طور جدی توقف حملات اسرائیل را دنبال کرده‌ایم. اگر جنایات ادامه یابد، نه تنها روند مذاکرات را متوقف خواهیم کرد، بلکه در مقابل اسرائیل نیز خواهیم ایستاد.
ما مصمم به برقراری آتش‌بس در سراسر لبنان، به ویژه در جنوب این کشور هستیم.
اگر توافقی برای پایان جنگ بین ج.ا و آمریکا حاصل شود، شامل توقف حملات در همه جبهه‌ها، به ویژه لبنان، خواهد بود.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5248" target="_blank">📅 01:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5247">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
به رغم گزارش و خبر ترامپ : حزب‌الله لبنان چند راکت به شمال اسرائیل شلیک کرد.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5247" target="_blank">📅 00:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5246">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">بیانیه سفارت لبنان در واشنگتن در خصوص توافق
بر
سر
آتش‌بس
متقابل
:
حزب‌الله با پیشنهاد آمریکا برای توقف متقابل حملات موافقت کرده است؛ به این صورت که حملات اسرائیل به ضاحیه بیروت متوقف شود و در مقابل، حزب‌الله نیز حمله‌ای علیه اسرائیل انجام ندهد.
اسرائیل به ضاحیه در بیروت حمله نکنه
حزب‌الله به اسرائیل!
یعنی : اسرائیل می‌تونه به حملاتش در جنوب لبنان ادامه بده، اما حزب‌الله نمی‌تونه به اسرائیل حمله کنه !</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5246" target="_blank">📅 22:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5245">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
ترامپ :
«من تماس بسیار سازنده‌ای با نتانیاهو داشتم.  هیچ نیروی نظامی به بیروت اعزام نخواهد شد و تمام نیروهایی که در راه بودند، همین حالا بازگردانده شده‌اند. همچنین، از طریق نمایندگان عالی‌رتبه، تماس بسیار خوبی با حزب‌الله داشتم و آن‌ها موافقت کردند که تمام تیراندازی‌ها متوقف شود؛ یعنی نه اسرائیل به آن‌ها حمله خواهد کرد و نه آن‌ها به اسرائیل حمله می‌کنند.»
🔺
ادعاهای ترامپ شبیه برخی ادعاهاش در خصوص ایرانه.
اساسا اسرائیل قصدی برای ارسال نیرو به بیروت نداشت! بلکه نیروهاش در جنوب لبنان هستن!
🔺
دوم : بر اساس قرارداد آتش‌بس اسرائیل قرار بود که به بیروت حمله نکنه! ولی داره حمله میکنه
و در نوشته ترامپ هم اشاره نشده
به حملات هوایی اسرائیل به بیروت!
گفته : نیروی زمینی به سمت بیروت نره و برگشت کرده و…!
گویی ترامپ دست اسرائیل رو باز کرده که به‌ حملات هوایی‌اش به بیروت ادامه بده و به پیشروی‌اش در جنوب لبنان ادامه بده.
همزمان گفته بله من مانع شدن‌ نیروی زمینی ارتش اسرائیل به بیروت بره!
🔺
سوم:  ترامپ گفته با نماینده های حزب‌الله در تماس بوده و… عجیبه! بعیده!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5245" target="_blank">📅 21:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5244">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Om90Te72SuLxv-iQLRaieW45-JVQQQBoGwzng0l7vzfT87nkyl50obm66_kknapdoTTcXFqlQ0ODHcNu6mf-bDLvAz11GFxXfIHy0RshsxDORh4tn8lyX2pAIVekwIBef03gHtW71TeJqbEeDvGU_7enyoBwmHZz0z9Jn0KzPH7uEkHkGCBKF_tW0ub8dSvtBSFkpZQJ_CtVUo1rMjL3loiQFeiO2cnq4zc8Cw63sZNfb_myCM40zYFTbkDcm7qzCkgLZDrlvhRZJ_DDyMw6JHAIW6ne-3aNhO2WWMRLZhxbdAx_T-DmxEnmyU-U-iSByD-9UNjYVrX6ykSzWeywnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه وزارت خارجه جمهوری اسلامی اسرائیل رو متهم میکنه به «نقض حاکمیت ملی لبنان»
یادآوری :
دولت لبنان سفیر جمهوری اسلامی
رو اخراج کرده و گفته مسبب این جنگ جمهوری اسلامی است اما سفیر ج‌ا
لبنان رو ترک نکرد.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5244" target="_blank">📅 21:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5243">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
🚨
به خاطر گروه تروریستی حزب الله لبنان: جمهوری اسلامی روند مذاکرات با آمریکا را متوقف کرد! سپاه ساکنان شمال اسرائیل را تهدید کرد!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5243" target="_blank">📅 21:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5242">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B_ZJGQOxQGXNN7iDrQapsSZ5jMac5HBtLL69xgV07MSI8RJHrWnugXHdw9uhK4Ki7tc2xPVWhocB4gWkRvZ63QMKkeVXFXtfhDFExbIwcIkX76qf-uBn46TkGOhxXOnVlw-7s8-H0puR3XcsuGorlQpw60cd1Ywd8KCzeRDloXWzxmDOrVc-E6Txvc6NNkJ4ORscLqPcgMvXofNymEOrSuHMDColGcEz2VdF39u0PtAv5uACtVYzbaM5KG-vqsjG2_Q2eEtFHAntZgRp1WBQDUCaC1IQ-pk1jdtmVzyv-6kaHJMUYbTEY93c9bLpr6wN28nOaKAx3ku2zVfwDkqd6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجید موسوی فرمانده موشکی سپاه</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5242" target="_blank">📅 21:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5241">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X7JfNA728DK5S2MHn-34NXckDyHTnt25LuTOsrKbjVxFEvd9csAgPqA-bjgYc0WOoUNPZ0I3xqzg5XkC79mvfhCrguzjDfjR77MQ9esJRgPx_yQ_NSWYcVB_Fl0rMSyKAFduyfYH7E2zPMaKJ5GWi69jUk-pvgap6h_HkC_LqocZLrigDj6mHtH_YDggsHAmsLGDkD7cY6Z3lu6IGGg9xhlWW3LlAXSpWsT0-AAfZG7ea_T5g1zD29MuIW5s3GqXw6hqEhb81AbDX4poNbKh_7bXK_TyLhPpm2zSqrpI4zLJ1csSpFmIhY_WLlJmB_QY2jSF04yvEwZ31E4LrfGG0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار اسرائیلی :
یک منبع بسیار موثق از فرودگاه بن‌گوریون به من گفت: اتفاقاتی که داره تو فرودگاه می‌افته دیوانه‌کننده‌ست. تو این ۳۵ سالی که اینجا کار می‌کنم، تا حالا چنین چیزی ندیده بودم. ارتش آمریکا حداقل شش ماه زودتر از برنامه زمان‌بندی‌شده وارد اینجا شده. اونا قراره در هفته‌های آینده هزاران پرواز مسافربری رو لغو کنن؛ تمام مسیرها و تمام مقصدها رو.
تنها جایی که براتون می‌مونه تا بتونید یه کم از این اوضاع خارج بشید و نفس راحت بکشید، یه پایگاه بزرگه؛ پایگاهی که می‌تونید برای مدت طولانی توش بمونید.
آماده باشید.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5241" target="_blank">📅 20:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5240">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NILZ0TMUbmyNmH87ySaND-eVBVG_Qndv45L9nQ92m4KnKbsf00B-zaGu2TOtszuy6I_zk8sGqcRG_FfzZV2XLfgtvLQkNS84wXVFtIhk8nEdcCu2Z6TZgh5IzZ7F-Cu1Gvqe08UONXxXfEBzGFvxawJMhOYw0KcSgcipZBqO8KbQKLUgBRFNRVkQj9gCPeJoWC6Z3hECdHfOyxQ-QkkS-UgpK40rAm9FB-PFPZtEq6TTsWPeSkAvRf2o_ZcOcHDEidBNGwLi44s1xgmUl28hBBIqNzWn1WzVr-DGCuv-c72z6JhmqBgPne1VLORmSxQaYpSyU6dcRXaJ35SVnFW9Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه خب ! اینها «وطن پرست» هستند
دغدغه‌شون «جمهوری اسلامی» نیست!
حفظ «ایرانه» و بحث «وطنه»!
فقط اولویت نخستشون
گروه تروریستی حزب‌الله لبنانه!
و توی مصاحبه‌هاشون هم میگن حاضریم ایران به خاطر حزب‌الله موشک بخوره!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5240" target="_blank">📅 20:28 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5239">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
🚨
به خاطر گروه تروریستی حزب الله لبنان: جمهوری اسلامی روند مذاکرات با آمریکا را متوقف کرد! سپاه ساکنان شمال اسرائیل را تهدید کرد!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5239" target="_blank">📅 19:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5238">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H2BKOlyky-rV2ujIeF6ZTyd8VWLjA1TkXB-hKkBYa2CRtYCKJh-12bbI-dx6MOMXc0m_-hAzmcE2_9wF5V9jNKxaagR5nFRldKnzc9NqalsWXXWdrFv7e0dU8Rx7gJV0uM1td7jtaodQY-GeTVRg8EWpUZKNRbqtDmSteKvnFOfnAz0YRyW8kXxV4YJQjr7UmHHlYwVoGONLoDW4lJVwAGbcDYAyUoeGfMWPWiAGQe3qqygN31J_vyGrhheEDvq0blsf0SgTUGuHEQ0bZwGHJCjUZMUDmfgluxczniaI5wFDq3h8IhnjM57U3YWsBton8w6v5Ko5aY4pYqzUVgi_TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کتابهای اسلامی برای کودکان
(در مصر و تونس و….)</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5238" target="_blank">📅 17:14 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5237">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">این دو سال رو یک مدلی با ترامپ راه بیاییم و بعدش بزنیم زیر قرارداد!</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5237" target="_blank">📅 15:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5236">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ODBAS2Ca4TLlQ6f8ndPGCJ4irlhDYST2QalMEum3F5f3miQu8TjcuHd22lBaa4b7Vv27EqLfRrhMgGGriTUYb6G9lFn3UrFNlk6OYJojHYbULNKfBY9cQTr0rZzY_0CtSVFiJMERCKmiUYPkrYf3mhX6uL0eaRGzeoxu8hKk0m_AeoTyz9SQHeGapCU4JQFSK0_KYup2xF1ujpfmIkh32dYVOPJezAIO30c_zLXys4uf_pJonN8mW1mNtjGeg9QImB3H8oZhKx0s5PpPqjUzYOMP6p4qxPo4_H431Wg2GDis29T5mUAs6lL2cFxhXHafaQfwYY99NlhOMFPoIywPlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نتانیاهو دستور حمله به ضاحیه (بخش شیعه‌نشینِ بیروت) را صادر کرد.
🚨
بلافاصله پس از انتشار بیانیه نتانیاهو، پهپادهای اسرائیلی در ارتفاع پایین بر فراز ضاحیه به پرواز درآمدند و خیابان‌های خروجی این منطقه بند آمد؛ هزاران تن از ساکنان ضاحیه که پس از آتش‌بس نسبی به خانه‌های خود بازگشته بودند، دوباره در حال فرار از منطقه هستند.
🔺
نتانیاهو دیشب نیز در دستوری به ارتش اسرائیل خواستار  عمیق‌تر شدن و گسترده‌تر شدن عملیات زمینی ارتش اسرائیل شده بود.
باید دید واکنش جمهوری اسلامی چه خواهد بود.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5236" target="_blank">📅 15:11 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5234">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DwUnpdrz2bOIqxu9whWLMO28l6jyuOxkRjQ_L7DDiYKXWkH4uhOe4vWmkK_7ix_ckCRqYMrFHF_mGU2hVOR2BI0Zv88-APERKKB-bSkYz8ObXIgClFNr8rvShOzw_nWV_FY9cW3UQTK8RNzQj6UJwmD3v-xO5WOrruC1DVsl5my-oyU7ZdGlxlO_SsFKxpeCejAqUPGpMWCbLy-ZFRvcq2whvC5IVdWVUj8yLsK1Cu9Z7r7SyuBuuAtwVv5cMMeK3YvVgc38LHIwuurmCrYoyLR1H8CFYNwin1asyGjiSAhPo9gyKefUmprIDUSC386G7Aq4jf5mpvgwmTi13Gonew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vg9XwcorTGQMdJtjEPA0ChbHQ4wgvpU4CU_S69LT-mmZySgV7jJ095XCRvgg6CyjCGRQArzK69-xp6iH-QF6sATvEsVUJSG3-C4J0F-SSNpGvEeESTmMjcB67r1hyY8FAdqUWluWv2RtPS0zDhIakWa3uCl--VInh5mN67APIcPZNLGegfd2QixGgBRzD60GIfwv855taAMwCJX4HUa2nQPgAtzsazcLCCGrdxEjijGdM7WlVJWkIh1F7R68SyOl_YtGc89Vtiz3agRAFbtdvnrolh7wKZz4rEIn2wPj6GPXSkrqPeVvwwZqg1RIvDGVaReUSThr5xeBNIsRi54qQA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسحاق قالیباف
فرزند سردار رشید اسلام محمد باقر قالیباف</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5234" target="_blank">📅 14:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5232">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6befcc9146.mp4?token=G_M9q_Vkwg49K6g9ca0nNOXPtIC-ciUG1qjb_B8Bx93wBUKdmei9FXMjJozVhw65Dr3dI4PG1PeA_fH_a1Gy2pTAkdXk9wK2_4W4S_7t1biSO7kv7m1UDX3JEjcze7PABnZOix3HP7dOeCEMSlW_CkLzzZqGdQBe1tz6ZZdXsgxm7dHVFKsZvFmx76diV2ljuJMkLyBNHfW0AhVcr6wPydR_TyBeTQb3XFm0eQjcBC_dcsORdCM8ZS6Y6coSOUJVbfGN7oh_OcXoWcjov1oyjORe9epl13uQ74CCiilNOkD_5fh8AwAuiDliRpOBsDPhhM_sdJN0plR7LvI-LTtFHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6befcc9146.mp4?token=G_M9q_Vkwg49K6g9ca0nNOXPtIC-ciUG1qjb_B8Bx93wBUKdmei9FXMjJozVhw65Dr3dI4PG1PeA_fH_a1Gy2pTAkdXk9wK2_4W4S_7t1biSO7kv7m1UDX3JEjcze7PABnZOix3HP7dOeCEMSlW_CkLzzZqGdQBe1tz6ZZdXsgxm7dHVFKsZvFmx76diV2ljuJMkLyBNHfW0AhVcr6wPydR_TyBeTQb3XFm0eQjcBC_dcsORdCM8ZS6Y6coSOUJVbfGN7oh_OcXoWcjov1oyjORe9epl13uQ74CCiilNOkD_5fh8AwAuiDliRpOBsDPhhM_sdJN0plR7LvI-LTtFHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم فوتبال «پاریسن ژرمن» قهرمان شد و پاریس و فرانسه رو به آتش کشیدن
قیافه‌هاشون که تابلوئه!
توی یکی از ویدئوها شعار الله اکبر هم‌ میدن!!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5232" target="_blank">📅 12:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5231">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">به درخواست فرانسه، امروز شورای امنیت سازمان ملل نشستی اضطراری در خصوص وضعیت لبنان برگزار خواهد کرد.
پایان این نشست قطعا چیزی در حد صدور یک بیانیه خواهد بود و یک محکومیت، هیچی نخواهد شد!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5231" target="_blank">📅 12:24 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5230">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XcHw0JNyzj--uQhTY5q3wdxSDyunYqHmYZdLNgNVCKWNPz5kOwe4RIiaQvGKrxqckRQIaJKg4ZyCRiGVMuYeumOvgIr53Im_LEiwgHMp9LKY3NJQdcyDSyN-m530Jc-X-phCjIKqpjzDgn0Gyrorftr6lXii2iNBcPp2oCk9cyF3XjFWf4AUyJ6whADP3rULG9THo1qT0TFMg19m7ktqnqj0ZjMug-cZ6M4Pv_AG2UzfqOpk2rzonqGw1ySlX2uj1c2ZZA7q0IkGcBwbSyEBDnT3C8xQNlXdn1IXtrfoKUxq20eGG_C9ZxbS3BLr0V03z5mNjLUOkW1KQRprry0sUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ارتش آمریکا رسما اعلام کرده
که چند حمله در دو روز اخیر به قشم
و گورک در نزدیکی تنگه هرمز انجام داده!</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5230" target="_blank">📅 11:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5229">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a58623f2eb.mp4?token=OghIOBcFXMRilaq1XZJCiuJfZKT7qObRwJuGVge5xSnbd7W8LCd8OG5XUoj1Pnq9_8b8mfDVam_UkW4ieSs_PywicLQzvastq1xA2yhdsaOPYt7O64RcoQUvuYzq7TbwfO0__JFiEk294Sb7OKe_qy02urnb0WaPjH8ZnMER1PqfaA8aRg9xJ4UPXbpI-gkYoeD3j3mJfe9SsqP2W2hk6Gle1YJNR5X5-DsR2Dcf6ZFt6ppeK3C_fiShBqBRxETlFZuXif8FG9Zt_kZaIosLgSv7brGEIWk8knf4PR1GFUyMsfnHLPjJY2xonVuT1qDKeG7rrt67IXoRNeuTV3SOdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a58623f2eb.mp4?token=OghIOBcFXMRilaq1XZJCiuJfZKT7qObRwJuGVge5xSnbd7W8LCd8OG5XUoj1Pnq9_8b8mfDVam_UkW4ieSs_PywicLQzvastq1xA2yhdsaOPYt7O64RcoQUvuYzq7TbwfO0__JFiEk294Sb7OKe_qy02urnb0WaPjH8ZnMER1PqfaA8aRg9xJ4UPXbpI-gkYoeD3j3mJfe9SsqP2W2hk6Gle1YJNR5X5-DsR2Dcf6ZFt6ppeK3C_fiShBqBRxETlFZuXif8FG9Zt_kZaIosLgSv7brGEIWk8knf4PR1GFUyMsfnHLPjJY2xonVuT1qDKeG7rrt67IXoRNeuTV3SOdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا این خانم از فرقه گروه تروریستی حزب‌الله لبنان، میگه در برابر اعتراضات حامیان حزب‌الله در لبنان که چرا جمهوری اسلامی ما رو رها کرده و کاری برامون نمیکنه «لال» شدم !  داره میگه حامیان حزب الله لبنان از جمهوری اسلامی ناامید و خشمگین شدن!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5229" target="_blank">📅 11:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5228">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6921e12e46.mp4?token=Iu6cmSfC3zdqL1w8AS53uV1PIoMmkFhTUee2_HpXLbMqAMcVhXKAyAnPNNmprwKy6R52wludl2CryFydoo7Qvrk_A8MEljTpKHN2nxuNCIvNauvzUiOHHludqmeJoOtiANsWB6jyYW5mjOBCqy1f5pI0zWJQNfB77nSBYwRwoVkPStAZfwbnDcSGLOAT2b5enwpeRIwDNrbZhLagXK36l4OgLsZSk52Fz8sBtb0UHZTa307v2xd4B8Sz9gEa0IR77gUmeBBgh-Qabvne5wQguujSUuecFAW5Q2gGmHq086UvIzrhC50ogWBtaK3MyO9mT1FeqOss1Z2cZIGpVpFXeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6921e12e46.mp4?token=Iu6cmSfC3zdqL1w8AS53uV1PIoMmkFhTUee2_HpXLbMqAMcVhXKAyAnPNNmprwKy6R52wludl2CryFydoo7Qvrk_A8MEljTpKHN2nxuNCIvNauvzUiOHHludqmeJoOtiANsWB6jyYW5mjOBCqy1f5pI0zWJQNfB77nSBYwRwoVkPStAZfwbnDcSGLOAT2b5enwpeRIwDNrbZhLagXK36l4OgLsZSk52Fz8sBtb0UHZTa307v2xd4B8Sz9gEa0IR77gUmeBBgh-Qabvne5wQguujSUuecFAW5Q2gGmHq086UvIzrhC50ogWBtaK3MyO9mT1FeqOss1Z2cZIGpVpFXeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فراکسیون پارلمانی گروه تروریستی حزب‌الله لبنان، چند‌ وقت پیش رسما  از دولت لبنان خواسته بودن  که برای آتش‌بس، مذاکره نکنه و…..! به دولت لبنان گفتن که بگذارید جمهوری اسلامی با اهرم‌هایی که داره از طریق مذاکره با آمریکا برای ما آتش بس بیاره (که بعد بگن دیدید،…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5228" target="_blank">📅 11:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5227">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I4BtshwmIlCAA1z_SCMXOXFnIUPmG7UzGsZz3AZbS_oGDKI094K7aG0mnLZRoQeBoV2l-Fe_-TcG42xKGwGfvdYsd_ay_6aSBTciL6sMEWjYSY2mFvEKv4V3Tm4nE4WBGXRHk7l5xuaVe-bHl4goSM0s6Ac5IyU3DvGRWEuUMchiUKnVt1fz7fuEseu4fkE0szyT1iruap6f5i8yoYwD68iE784A5brD1v4MbjWTDh_I5-ILWmFnys3LcnLIDf1CR4NxpE_Kl6sgnEXJkM3tf09X5Wk-SbcbMRnQrqS4OeQrFA90ZCEalhQ1fAnDRsy306qZWav_Cpbv1-WGPxmpYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فراکسیون پارلمانی گروه تروریستی حزب‌الله لبنان، چند‌ وقت پیش رسما
از دولت لبنان خواسته بودن
که برای آتش‌بس، مذاکره نکنه و…..!
به دولت لبنان گفتن که بگذارید جمهوری اسلامی با اهرم‌هایی که داره از طریق مذاکره با آمریکا برای ما آتش بس بیاره
(که بعد بگن دیدید، همون کشوری که به ما پول و اسلحه و….. میده، آتش‌بس رو هم آورد؟)
ولی الان می‌بینن جمهوری اسلامی توان چنین کاری رو نداره!
ترامپ اساسا داره لفتش میده و سرزمین‌های تحت کنترل حزب‌الله هم داره می‌افته دست اسرائیل پ یک میلیون نفرشون هم آواره شدن!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5227" target="_blank">📅 11:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5226">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">وقتی ایران ساسانی به دست عربهای مسلمان سقوط کرد، حکومتی‌های عربی دست به مهاجرت و اسکان جمعیت بزرگی از عربها در مناطق ایران زدند.  به طوری که مناطق بزرگی از ایران برای همیشه عرب زبان شدند.، مثلا تیسفون و بغداد که قلب تپنده حکومت ساسانی بود!  یا شهر‌ نجف!  برخی…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5226" target="_blank">📅 10:06 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5225">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e458969a1.mp4?token=v3YzXvv_N_EmC-ah0nqVN6G1QCW53wIBdYgb3x4y4ZNg4D_yN2-MCF93Lfwqj2olLsm0cXYCBPY6NuSbCcAUyaBDhZZNtMbbY_a9DK0LF9EheRwIUbfktvsfDAGW5i69e9YYCBrihWe4_76PfC4dotBzLmABMuo_hBJOd5zEyNMN2GtwY8X32qNjojFN4E6w9b9pMMMhMemMS8u0seKlKQxerknLgqh_wCGRCuPjEWtqePZqxzsEdVsh7L_n6z8-QNltpetu3Ga_k9HW6laF8VQ418huqWLPD2UMiXk_QOKNQ5B6X9pA8-fb00nBHlafuqFRhXrP1rMBPcUHxIIJJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e458969a1.mp4?token=v3YzXvv_N_EmC-ah0nqVN6G1QCW53wIBdYgb3x4y4ZNg4D_yN2-MCF93Lfwqj2olLsm0cXYCBPY6NuSbCcAUyaBDhZZNtMbbY_a9DK0LF9EheRwIUbfktvsfDAGW5i69e9YYCBrihWe4_76PfC4dotBzLmABMuo_hBJOd5zEyNMN2GtwY8X32qNjojFN4E6w9b9pMMMhMemMS8u0seKlKQxerknLgqh_wCGRCuPjEWtqePZqxzsEdVsh7L_n6z8-QNltpetu3Ga_k9HW6laF8VQ418huqWLPD2UMiXk_QOKNQ5B6X9pA8-fb00nBHlafuqFRhXrP1rMBPcUHxIIJJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی ایران ساسانی به دست عربهای مسلمان سقوط کرد، حکومتی‌های عربی دست به مهاجرت و اسکان جمعیت بزرگی از عربها در مناطق ایران زدند.
به طوری که مناطق بزرگی از ایران برای همیشه عرب زبان شدند.،
مثلا تیسفون و بغداد که قلب تپنده حکومت ساسانی بود!
یا شهر‌ نجف!
برخی از شهرها را اساسا به صورت شهرهای پادگانی عربی در وسط مناطق فارسی زبان و ایرانی ساختند،
پادگان شهرهایی چون : بصره و کوفه!
در قم اینقدر عرب ساکن کردند (از قبایل یمنی اشعری و از کوفه)  که برای چند قرن یک شهر با هویت عربی بود!
اصفهان اغلب یهودی بودند، یک شهر تجاری، عربها حتی بهش میگفتن دارالیهود
عربها شهر «جی» رو کنارش ساختند و اعراب رو ساکن اون کردن. تا نیمی از منطقه شهری اصفهان عرب باشه.
نیمی از قزوین، محلات عربی بود.
این حجم از استقرار قبایل عرب در قم، مرو، قزوین، اصفهان و… اغلب به خاطر قیام مردم در این شهرها علیه حکومت عربها و مسلمین بود. قیام های قم بسیار معروفه، اما اینقدر عرب ساکن قم کردند. که شهر برای قرن‌ها هویت عربی گرفت!</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5225" target="_blank">📅 10:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5224">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XlPjhifBM19M-K-3M3ZzOVjRt8GSjmDJ-PLBIbevaaCKj3o7cUvD3dQk7h_hR8pI-7bwL2XANztU6rO4CYW_zdw1sy9tXfPDnfO25WXX__AewZ2LRNkGExcG7NjpY_9BO_-5YOEi6825eT-qiuej4G7PIr_onjKcR0atWEC114exzJoxCjvtpJaO38aKiAVi7NH-jAt7bjZl_K44CDsfI8RGDyYsf5qt5hacl0PAUWD9TU41qBgbX3hUwG0wqzs9-xW-P9UWmnwsF8ZAlSA8WbGMqmXWUMb8eOHO7L05tmrtM9D1SwxSkfwkirl6C8gRiVxqgUmdb4aHVh1H2bCi-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چطور تریتا پارسی در آمریکا
متوجه یک «طرح پنهانی» برخی نهادهای امنیتی در تهران شده؟!
معلومه یا این طرح رو خودش داده
یا با این نهادهای امنیتی رابطه داره!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5224" target="_blank">📅 02:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5223">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
مایک والتز سفیر آمریکا در سازمان ملل : جمهوری اسلامی با حمله به کشورهای عرب همسایه‌اش اشتباه بزرگی مرتکب شد و تاوان آن را خواهد پرداخت.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5223" target="_blank">📅 00:41 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5222">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gW4mOsUst6pPcoKLkHlpejzr33_JXzavctQ_jnB6Yfz8W-m4zHCWT7q1QgSkS2cEh8YL2yixyYz-eNLaDaG1XuESBnw7CoLloQxr58RtLuhTfxDE01p6r9Y3IAHn_vfdM27tF_PaUsqeASHy10sRYxcr9RSXX-xfUtTKepzHaS_U8xik6e49Od6KLCBxf-E3qq1z36DiZ6kFNMDZwbL3-Fdmwiv5wQfvDwAhyWzShYUCwf6UDytKJl9sx_zUFBEKU6i713IuID1sGngHLzQwiW8zBni2scnrm9GcGXAqmMNeHWYmb1XxtgRhVhk1hcezpQYlM_OIwXavAQwDVSBMnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌های ضد و‌ نقیض از استعفای پزشکیان از ریاست جمهوری</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5222" target="_blank">📅 00:37 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5219">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i8oqUfqTJQZLCS8acRSDh1ipdqtmFXte-lZEpFEPpMX0Foi6hpLvpjiTD7CZJCm2MtZK_WIkwwDT6OvH4lQPsuRtzQin9_SCByMf6d0XmESRLKTVJUNPohOSGitBTrOoHWoun9nbL_n7ncuTTXAc0mZ3KJf-abwD93MFvAlwjDGVI7r6BCmsuuZS3v6R-oAFi2A5ivI35FXygSsyehwFLRnkUdu0vJKsmMgVpZXYAsToJdwz_6Vy5kNI2tKiRbIxyYCXfLnwZzi2BS0Mr0rQeG356Pjgsvk9KllpNOG5SpyTrBZKhLyqb7pMpU2yXyvZZKG5m3_6cGKUPoq7L49NWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N0fV3MguI1DvK-xN3bV2DoqoalyvN-3xo3Vw7hUnl8pNfB_WhzZ4nTROzkYHFy7DMXnV3d5WxRrrSHklEucrR6wYpDHR92svIKmO8fMqowuj2uL6xesobh2p9t9HylsNBhcNWjcnQSS5yqsRaPicCpXQN7bcRdR6D39rUpbiW3vjapTqSSQPIP-5o-i3dP6W2IDJNf2faslCw7n8lo_7RHaK9xNBnI-EFPB77nbrtSmtI6r_miBdP4yCbNYPf97vpiLNqblrlhD94yNnJ4aEzPIH-JtwC9uHlOn5-Vz8o8UhT1qsed_fMvKnzldlVCKp0AskQvBNTztEuaSTRM7OJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UZRgWcBFu46a55KE1JAuWpypr8ZT0bZbVrWTkaa-8axInoN0eEDdR1n2WO0MwneT41gq-izA3o1O-FrtEoX2DWcfnlDiTXMA1wvBbbQx24J96rM_9JwkZbb1L2-Lh-MBnObY12Tkv_dlvt1X31SG1caxhgSOiLYpnBn7hvbYGMSQTcWWJWSRZY3WLxXSrOg9sh80MNucF35ul153piTlSpeSafSxIwRh9bP4SlF1Xtacos8rpFaFmqSWI5f7D8IuFzYnib_ndZG0OcDiD9_HYfMfziqRCAl9fEVypTGQ15Aeh14gYvgeW_HkxMlEF-szXVI0YNQpdmFwDQDJCQlxMg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یادتون رفته میخواستید برید
پشت سر خامنه‌ای در قدس نماز بخونید؟
که شما تاریخ خوندید نه؟
تاریخ جمال عبدالناصر و صدام و قذافی و بشار اسد رو لابد خونده بودید
که همین هوس‌ها رو داشتن!!!
و به همین نتایج هم رسیدن!</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5219" target="_blank">📅 18:19 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5216">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ly64d5vYZx_LljyqaKUu5nCcwDfuxTi-TMTGWoCcbqrk9N9X4Xnp8mU3L3hkTnh_E00N9JZ42kkGchLtU_r_BrdNc4G1Zrxyk2q6ReeUDij2hY1Abobbl5veLB5rLw_PBPAAZS8Sdf7v6Pwp3uGzXLb9PDFlOeuWvXpsz63rHlr11ndMPh9SwuW6uCCPC7CT_WLL7DgBI7sydj96yKs11MtDE5wli5izdcxsjngr98n-JOBDUbXZzrlEscB6tDCv24nAiSKf-WLCemkY4uaSvLZ31IFqsicT9lt0dRUSmsVXJXvtISYmTKeDeUDZe0Hoyi_1IZFc_jlCm3i_juw7JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MJ1xMHADhhMIHeMf5Vuk9smiPuddWo3K7Q8y32jvgkRM1uExgTD0f0cfrs9-QuSff2PecKPQOZAq-KtdJDenPRFZQCc4OXwRJW60BlOK0lW7mtXCRvrw6ueU1fiQp9fcLcEnnBz1aRj8-NUj-u_787Lze2OKUYeJoGIfm60estnXud1hFqWj6qQhvIgqNEe_wJF2aIEB8D4mVyeubosEcDwPvfNn8UtVMFaGyXCIzFeJh0jEwc27sl2ISAetaNMVa4oks9oN02_5yvATX3ibyZixZPG-mD_T5k13Jqc-IMZtPpousOZ4G9tkCpd6AEcsKXWNQ-jzSfydyR2Cau6giw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X1_RW4bFaRItX7j2KGs5-pUVthqAPEGcZlCE9hpQ8lZ4GWeTuqnWeFhJttO3qbJUngJHEuKKB7UUG25_TJEyC4YpPrD98BpF1ndjmZ8nZ3ScQQ8pwkSG0yBrpFFsFvQjfWjniT0QVQZ2G4khYdaHD2jGQ_gkoNjZSoQtOw4nYU7iVmh-Z4SsITcyE2CNNQRn18J7nus6UpSSREBkm4mMGURAmHdXJdiW-eDvjBxkoQIR4FOR9AmpQ0XZULv3nT8fzgKFbd_ssKR8y5x7-jTqtum2lJHVtQLymNuA3Hp_kKOui2RfK4q2bkPH9BH60yAS6uNlEkD_p5Yf8KKkHKpbTA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رفسنجانی سالها پیش گفت من به خامنه‌ای گفتم پاسخ این همه ضررها در دشمنی با آمریکا رو شما به عهده میگیرید ؟؟ خامنه‌ای گفت بله! جواب خدا با من!!!  و خب این جنگ‌ها و تحریم‌ها و آسیب‌ها و کودکان میناب و... همه همون مسائلی است که خامنه‌ای گفته جواب خدا با من! یعنی…</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5216" target="_blank">📅 18:01 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5215">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db68225cef.mp4?token=DbIu8bcCvcO7zyw58c8oH3KDisR0EHVowWHSc6xusXV2Y8CndixxAOBYzCfDoHW2oNhx1w9DYnRYnc-8Yck2F60KOXVS1hes_W_acZEuGoJ0R3gW80jgJnLn7TOqGRpIPe-RhXJP_zm9OaEGUv3pZM-ktSfwBl1mS7qzdNGxPxEbnKfyirZf8PoR79QzXowZ8PBrh7_UNI2KbqCel8eCeQalE-bKjUq_17w8p5HggoRvohKGEgiAht8bkAEQmGV6A7EpDG-mC6ANUI4X_XnB5m5k2CxiErFygwPvmNQU7NJ0SdeCXVUXyDhZN2CH395WiJGr7vFqb-nw_PzxFoWfDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db68225cef.mp4?token=DbIu8bcCvcO7zyw58c8oH3KDisR0EHVowWHSc6xusXV2Y8CndixxAOBYzCfDoHW2oNhx1w9DYnRYnc-8Yck2F60KOXVS1hes_W_acZEuGoJ0R3gW80jgJnLn7TOqGRpIPe-RhXJP_zm9OaEGUv3pZM-ktSfwBl1mS7qzdNGxPxEbnKfyirZf8PoR79QzXowZ8PBrh7_UNI2KbqCel8eCeQalE-bKjUq_17w8p5HggoRvohKGEgiAht8bkAEQmGV6A7EpDG-mC6ANUI4X_XnB5m5k2CxiErFygwPvmNQU7NJ0SdeCXVUXyDhZN2CH395WiJGr7vFqb-nw_PzxFoWfDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی در تاریخ ۲۹ آبان ۱۴۰۴ در تلویزیون جمهوری اسلامی میگه ترامپ به ما نامه‌ای داده و صراحتا نوشته «دو گزینه بیشتر نیست» یا جنگ و خونریزی یا مذاکره مستقیم «برای از بین بردن غنی‌سازی و موشکی»  این مصاحبه چند ماه بعد از جنگ ۱۲ روزه بود! یعنی در آبان ماه، مشکلات…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5215" target="_blank">📅 18:00 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5214">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65778ca5eb.mp4?token=eDegz2g8LJ5Nx2RQi3qxYR7RBB-SsalNiKREA3ivwkGDbljkIP8EmzxfogphPRSbUsIEMefHsuAW76SJLaJkK2hkCpiMQCHqnAyap4WGxcasV1XMb2J1NIZGQe6skT9FQTAfbUf--3q8aBV2zaRV2X_AMHVKikXU3HupAg0ejpKVtMECzfn1XGpxaT2vwa29MT1cCD0qRw_Z7gKwIGIT_so4QjM5dCnnv-WHfQ8dgvEfBtYTVCBCKIQMqBQ3mJkiiwsBaC2KCGiZEV9qQpgOIsIyhXZVBxTzuyrdmihfgHHYW9LJi2gaTU1FknEun1F7-72Z7M48vw3RwBTwj5BG3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65778ca5eb.mp4?token=eDegz2g8LJ5Nx2RQi3qxYR7RBB-SsalNiKREA3ivwkGDbljkIP8EmzxfogphPRSbUsIEMefHsuAW76SJLaJkK2hkCpiMQCHqnAyap4WGxcasV1XMb2J1NIZGQe6skT9FQTAfbUf--3q8aBV2zaRV2X_AMHVKikXU3HupAg0ejpKVtMECzfn1XGpxaT2vwa29MT1cCD0qRw_Z7gKwIGIT_so4QjM5dCnnv-WHfQ8dgvEfBtYTVCBCKIQMqBQ3mJkiiwsBaC2KCGiZEV9qQpgOIsIyhXZVBxTzuyrdmihfgHHYW9LJi2gaTU1FknEun1F7-72Z7M48vw3RwBTwj5BG3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">می‌نشستن و  با نخوت وعده «دردسرها»  میدادن برای آمریکا و دنیا!  «حالا حالا دردسرها» خواهیم داشت!  بعد که جنگ شد تقصیر مردم ایرانه که تاریخ نخوندن!!!  تقصیر تلویزیون اینترنشناله!</div>
<div class="tg-footer">👁️ 358K · <a href="https://t.me/farahmand_alipour/5214" target="_blank">📅 17:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5213">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab893ceeae.mp4?token=ZmnFZjKJDZchiEcug1FVFhpqbK_rpUaUpoDzw7CdA-HV9A8ytnf8nriQ4jsRQUMNQdtvkWAm7F3yzbhBlZexRUBXxK1mxRhGk-MU5_iZLWxlLCRbWOMiJxlQu1EbYvtLqzxLgzkPTRBc6ne2ehu4DtOhHrb_z-Fi6uRiTYI1o8KisvP5qPNY2aQAXrRU-TOGAZnKGW5K3KMweell-jBW9dzg7x4RmW0xC4IuDEPS7eOgsTVXkpwzEI95UV4ttydHPQRcnTs_FLjWcMLB330DxoLuK5GCxIyYrGyHoiIny9eTs5BoNJZ84AcKKnB28QGLimSdwaH9dsXX8MSafTSZXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab893ceeae.mp4?token=ZmnFZjKJDZchiEcug1FVFhpqbK_rpUaUpoDzw7CdA-HV9A8ytnf8nriQ4jsRQUMNQdtvkWAm7F3yzbhBlZexRUBXxK1mxRhGk-MU5_iZLWxlLCRbWOMiJxlQu1EbYvtLqzxLgzkPTRBc6ne2ehu4DtOhHrb_z-Fi6uRiTYI1o8KisvP5qPNY2aQAXrRU-TOGAZnKGW5K3KMweell-jBW9dzg7x4RmW0xC4IuDEPS7eOgsTVXkpwzEI95UV4ttydHPQRcnTs_FLjWcMLB330DxoLuK5GCxIyYrGyHoiIny9eTs5BoNJZ84AcKKnB28QGLimSdwaH9dsXX8MSafTSZXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بله جنگ ۴۰ روزه به خاطر ایران اینترنشنال بود و دیاسپورای ایرانی! جنگ ۱۲ روزه هم تقصیر افغانستانی‌های ساکن ایران بود!!! یادمون هست!  فقط فعالیت هسته‌ای و موشکی و نیابتی‌های جمهوری اسلامی و ۴۷ سال سیاست آمریکا ستیزی و دنبال نابودی اسرائیل بودن ، بی ایراد هستن…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5213" target="_blank">📅 17:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5212">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mpe-5sdMXO5IaERP3vy1n6IGdNHnUU-H_Jh3M8PiulRRIONjXVOGIG-udZEbsKt32WmhItxwseOkbBR-YWa4UGQWaBwJILBOEzNzeIYnmbKnUQbkDe8n7WVL_I9Sij3agG1OOf-PPb_g4MvfgOswcaICW4B0tubeDzDio1JaAbcz0sSUian-kcdbKgSn_fIWzxfjVOVWm9GfMXGwKXn8IACU7cuM_p8AeURYN1wdV7lDPzGL9fPMRpExElJHM8K9Tqvp_z3nFrYWmMN9PidOKZDasXq3o6b-UuQoRUufY9Oc5I87MfxN_TxqnBHmaGZ15R2eoZ3BXd_WQs0HF68KVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بله جنگ ۴۰ روزه به خاطر ایران اینترنشنال بود و دیاسپورای ایرانی!
جنگ ۱۲ روزه هم تقصیر افغانستانی‌های ساکن ایران بود!!! یادمون هست!
فقط فعالیت هسته‌ای و موشکی و نیابتی‌های جمهوری اسلامی و ۴۷ سال سیاست آمریکا ستیزی و دنبال نابودی اسرائیل بودن ،
بی ایراد هستن و مشکلی ندارن!
و همونطور که می‌بینید روی میز مذاکرات هم بحث ایران اینترنشناله و افغانستانی‌های ساکن ایران و دیاسپورا! مشکلات و دعوا سر اینهاست!
خوش به حال آخوند که چون شمایانی رو داره! هر بلایی که سرتون ببره، آغوش گرم آخوند رو رها نمی‌کنید!
شما اگه تاریخ خونده بودید راه شوروی و کره‌شمالی رو نمی‌رفتید! راه
صدام و بشار اسد رو نمی‌رفتید و چندین هزار نفر رو دو شب قتل عام نمی‌کردید! بی‌آبروهای تاریخ!</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5212" target="_blank">📅 17:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5211">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wAYjGQAO0M9579n4GXDSSeO0FXxO_SCCG1ekkyXUYFN34V_OrdbaCQ3f5sDjA-n418x-jS5P06QhPaQqFgosVrL6eTlQ5Z_yWwzIZyMzcplfc3BV_PrbSplEIxoyp5jDQAgrGhjamY8XN__OsQYc13zL3fEk6Vhy9Cn1I4S_EijgDR7HOd3jW2Tzn_v_1IBt0zgkFN8KjPF7rYNuN2BTdMUY4WJU35bENJU_R84NaiO69l8SzfQWfRlkSi7kY0i6hJ5lK1EIYDt13IYOPsq05nigi2NAaw2_fQBAFhLX_z-2le7uOpQZap48Sz0v1O4p9_1QXNY8KDvB6QUlD4khcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بله جنگ  ۴۰ روزه به خاطر ایران اینترنشال بود و‌ دیاسپورای ایرانی!
جنگ ۱۲ روزه هم تقصیر افغانستانی‌های
ساکن ایران بود!!! یادمون هست!
فقط فعالیت هسته‌ای و موشکی و نیابتی‌های
جمهوری اسلامی  و ۴۷ سال آمریکا ستیزی و دنبال نابودی اسرائیل بودن ،
بی ایراد هستن و مشکلی ندارن!
و همونطور که می‌بینید روی میز مذاکرات
هم بحث ایران اینترنشناله و افغانستانی‌های ساکن ایران و دیاسپورا! مشکلات سر اینهاست!
خوش به حال  آخوند که چون شمایانی رو داره!
هر بلایی که سرتون ببره،
آغوش گرم آخوند رو رها نمی‌کنید!
شما اگه تاریخ خونده بودید راه شوروی
و کره شمالی رو نمی‌رفتید! راه صدام و بشار اسد رو نمی‌رفتید و چندین هزار نفر رو دو شب قتل عام نمی‌کردید! بی‌آبروهای تاریخ!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5211" target="_blank">📅 17:30 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5210">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jqhQRD8kKlQKMeuOO29eDlqV-qjR4kKX-P24biMoMOZfwnjw5fAbVsUeZS3wKdwx8mRBfjrgdEGtOShbPWdamgV8APPdYPJKO7n1bmqt_bQu_mcYnKQmR4iXzBbxPKKAvgVZwSUTRYydt9K5WIiFNLmJEqjv5sfrC2nhNiJ_AZN11T8BgosZ1MVkfTzUiqM42I0OQxsIK0KKW3AXLSXW1NL2D5tcou4ORgtKqbNc7lR1BdbuMNiq-oT2Qn194rU7vgHmvCXwcvDoTVlKQfAfKN5dzZRSCQxhHnR9qKOXoP0XSEf93tPOCdSiZFsC1h-clIWAQOwSLmcvj7U8bhSSNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما:  آمریکا با ۱۰ شرط جمهوری اسلامی موافقت کرده   ‏۱. آمریکا متعهد به عدم تجاوز به ایران شده  ‏۲. استمرار کنترل ایران بر تنگه هرمز ‏۳.پذیرش غنی سازی ‏۴.رفع همه تحریم های اولیه  ‏۵.رفع همه تحریم های ثانویه ‏۶.خاتمه تمامی قطعنامه های شورای امنیت  ‏۷.خاتمه…</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5210" target="_blank">📅 15:29 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5209">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rhW5r78GKt6VxjqnFTFAhB4aYyykqorJjsiD55l_l5OXmEHUUtGapMPMGQUVp4gd8DiLlCYFNFC6zez8wQr8ZUOpcz1L2oor3btBAxF0kUqfq2CgKZ-aHhE0_f_PPnTss8tCD8P0nsDMm4GrsSJ_76C-gXkfqnAgJWtnVeACriL2JB9TqgqWF7l1n2wELq3GsWD_PVFcKsPpWlCsViPz-sPwnSH9Z58CshfsKWZDRo2KSEbezLOckA24wZU97m5J6FEGBXfJr8mGMDWUoNNU2z20MqtgX0dXhBIJFU8sEmefXgKUc0Avh3rnIRTQk8n3BNLpUndp_R3I3DwUI0Vp8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل قلعه شقیق در جنوب لبنان
را تصرف کرد، این مهم‌ترین پیشروی ارتش اسرائیل در جنوب لبنان از سال ۲۰۰۰ میلادی است!
گروه تروریستی حزب‌الله لبنان،
بدون اجازه گرفتن از دولت و مجلس و ارتش لبنان و در خونخواهی خامنه‌ای،
به اسرائیل حمله کردند، اسرائیل نیز در پاسخ دست به حمله گسترده به مناطق شیعه‌نشین لبنان زد، بیش از دو ماه است که حدود یک میلیون شیعه لبنانی آواره شده‌اند! بیش از سه هزار تن کشته شدند!
چند هفته پیش دولت لبنان قصد مداخله داشت و تلاش برای «آتش‌بس» اما این گروه تروریستی و حامیانش مخالفت کردند و گفتند که جمهوری اسلامی باید این آتش‌بس را برای ما بیاورد!
(که بعد تبلیغ کنن قدرت ج‌ا بود)
جمهوری اسلامی نیز توقف در جنگ لبنان را در صدر خواسته‌های خود از دولت ترامپ قرار داده ولی هنوز به تفاهم با آمریکا نرسیده و اسرائیل هم داره کار رو ادامه میده!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5209" target="_blank">📅 12:09 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5208">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c1b13d62.mp4?token=n861_-ZK_Dv_wc0rNmYTg1DU-qAsdlQaHJg1-6AJsURCxvAN0kNbW9ztk1NgdqZJy-3ixNVQGmTGN4cbagQSOhl823tAK7kSjhbPE358CGc_QZxToDmXq_0wMaQscrcYdnfUOy1pKQMql9gTf4FeJ8mc65Z8Aiybwwi7-vpa4eBJLVZ1lykOAoARCK5jqaXiaKuDtL9-lihNsMBsKdBApkHJZOqmH3GKhLCbfRP0j4Z-08c9KhyBwNZod1-newpcQLuV_sE15YW18yuyMjct1kmxUc2QyuC7vLx5IKsDqgLS6n9p4MOuAVlSCKkbD2ctVEhLxehqQ2pTRGj995pWPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c1b13d62.mp4?token=n861_-ZK_Dv_wc0rNmYTg1DU-qAsdlQaHJg1-6AJsURCxvAN0kNbW9ztk1NgdqZJy-3ixNVQGmTGN4cbagQSOhl823tAK7kSjhbPE358CGc_QZxToDmXq_0wMaQscrcYdnfUOy1pKQMql9gTf4FeJ8mc65Z8Aiybwwi7-vpa4eBJLVZ1lykOAoARCK5jqaXiaKuDtL9-lihNsMBsKdBApkHJZOqmH3GKhLCbfRP0j4Z-08c9KhyBwNZod1-newpcQLuV_sE15YW18yuyMjct1kmxUc2QyuC7vLx5IKsDqgLS6n9p4MOuAVlSCKkbD2ctVEhLxehqQ2pTRGj995pWPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امیرمحمد شاه‌کرمی، نوجوان ۱۴ ساله، ۱۸ دی در جریان اعتراضات شهر قدس بازداشت و پس از ۶۰ روز پیکرش تحویل خانواده داده شد.
امیرمحمد ۱۸ دی‌ در اعتراضات ناپدید شد. خانواده‌اش به بیمارستان‌ها، سردخانه‌ها و پزشکی قانونی مراجعه کردند، اما هیچ اثری از او نیافتنند.
پس از دو روز و در ۲۰ دی، تلفن همراهش روشن شد و ماموران حکومتی از این طریق به خانواده اعلام کردند که امیرمحمد زنده است.
خانواده پس از این خبر، پیگیری‌های بیشتری در دادگستری انجام دادند و آنجا نیز به آنها اطمینان داده شد که پسرشان زنده است و حتی برایش حکم صادر شده است.
امیرمحمد دانش‌آموز مقطع هشتم بود و خانواده تلاش کرد از طریق آموزش و پرورش نیز این موضوع را پیگیری کند، اما در آنجا نیز با پاسخ‌هایی مبهم و با برچسب «پرونده محرمانه» روبه‌رو شد.
این بلاتکلیفی و بی‌خبری تا ۶۰ روز ادامه داشت؛ تا اینکه در نهایت پزشکی قانونی با خانواده تماس گرفت و اعلام کرد پیکر امیرمحمد شناسایی شده است.
پیکر این نوجوان با کد «ناشناس ۱۱۷۵۴» به خانواده تحویل داده شد.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5208" target="_blank">📅 10:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5207">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8afd0458a0.mp4?token=JXo2MlmmZM5Uz_OBDM5cK3KWST9HEpqyju2sYC6G35E2OeNVtc0_2kdJdwYTuiEmXlJShztknhQfIih0LuuwsqPRnAbZ1xn-TBfyX7lJF7caT1kL3Dw8r67whRSk7eb5QUi4oYeoeL-JOVYcvJNr2oBRyFQJXd2tVuxsC96J6KIN8qBf3RkUCXO667M-4OfIx7d_Ny1A5HCdP6lNnHruSH0ZhS4DKlNO_9oycpdlQe-5dz5WJaAqyzEGN3lE-mKC9kPbEDwMZ3rEiBxmQcVLVhZ6puAow5fZCOiVvrQSysQrLX6XPcutftLrf-HK2eFwqfvjSsGGImASX1G1v8J_SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8afd0458a0.mp4?token=JXo2MlmmZM5Uz_OBDM5cK3KWST9HEpqyju2sYC6G35E2OeNVtc0_2kdJdwYTuiEmXlJShztknhQfIih0LuuwsqPRnAbZ1xn-TBfyX7lJF7caT1kL3Dw8r67whRSk7eb5QUi4oYeoeL-JOVYcvJNr2oBRyFQJXd2tVuxsC96J6KIN8qBf3RkUCXO667M-4OfIx7d_Ny1A5HCdP6lNnHruSH0ZhS4DKlNO_9oycpdlQe-5dz5WJaAqyzEGN3lE-mKC9kPbEDwMZ3rEiBxmQcVLVhZ6puAow5fZCOiVvrQSysQrLX6XPcutftLrf-HK2eFwqfvjSsGGImASX1G1v8J_SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔈
🚨
چرا خامنه‌ای در پناهگاه نبود ؟  چرا خانواده ، چرا فرماندهان؟  چون «اطمینان داده بودن که کار نظامی در این چند روز صورت نمی‌گیره و اتفاقی نمی‌افته لذا شرایط عادی در بیت بوده»  صدای ناصر رفیعی</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/5207" target="_blank">📅 18:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5206">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Td0bKWpaBGoZRZDOoNJ7iyS_W_1mFBQkK_ocdL9QLKifHUoNWW-p8EmYPeqOWU-BNkakpKRCKh9cp0kNftu6FhCuP2XlZA0ctqiQMwV969iy98DgXrEWkQhBHkQwe17-ea0iDd8arq3JuaZD9-_pNqTK3TZstKHBEiG9i7Rz2L6CwKG90T-nO-aWkvXSZwPypWHvlISj5H0DYsixuq5llwGkjw8ZrsS9fItSt_XC0hbuTxlEObBW4nuHQ-OEpDFfd6x6B9dRif38HXME039tlYwC1KTnU1DoOO_ps0NssnjPMpkSGa4sPvARh7GJwaX1fWZzxydpb1dLH93dQECAew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی با آب و تاب می‌گفت
به امارات حمله موشکی و پهپادی کرده،
حملاتی که ۹۵ درصدشون توسط
سیستم دفاعی امارات خنثی میشدن!
اما امارات در عوض پنهانی با جنگنده‌هاش
حمله می‌کرد و جمهوری اسلامی هیچ سیستم تدافعی نداشت!
یعنی اگه به ایران ۱۰۰ جنگنده، یا ۱۰۰ موشک حمله می‌کرد، میشه با اطمینان گفت ۹۹٪ ماموریتشون
رو انجام میدادن و اهدافشون رو میزدن!
کما اینکه اسرائیل ۸۵۰۰ سورتی پرواز در آسمان ایران انجام داد حتی یک هواپیماش آسیبی ندید.
آمریکا هم ۱۳ هزار سورتی پرواز انجام داد.
آمریکا همچنین ۱۰۰۰ موشک تاهاماک به ایران شلیک کرد، جمهوری اسلامی قادر نبود حتی جلوی یکی از اونها رو بگیره! یک در هزار رو هم‌ نتونست!
جنگ با امارات رو جمهوری اسلامی کلید زد
و هنوز هم کامل مشخص نشده چه آسیب‌هایی
ایران در این جنگ متحمل شده!</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/5206" target="_blank">📅 10:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5204">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cUYwL9tY2CbCUxVyL_efjLVktp4862ZtMTNGQ1PfoagX9DhxSKKRjKmAt23bLthjddI_HkwarxfZJRGLMxgXhE4v8F9if33SR4IoJYTywQdGtDQKeJOaqq-59vQxVuhqQwe949b9AbOstGfKklbPIR7s9r_1XQ84VQJ-VvX4uANWrv6bU6QRu98CBf8T0kg4Y4g2jN8L1J4Gs-DoVn24R5pG7MLK1DLol5NnrEPMPx6l3D7bWQjh04FP27AucKwOr0DZFoIh_Cs4RTayUejFJWgxJJ9AJxEJFL9ZGs4pcsaRT2H5YrQSP0ufXIb1LpqXJzVujONpJwalZXnxR90KWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح یک دیوار در تهران و گفتن از نابودی اسرائیل در ۱۵ سال آینده!</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/5204" target="_blank">📅 21:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5203">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C6I29_cPAXONcEKLSix1jxvnGQh9PmEYVOATxce1ybtJeS73INGrpjqvSiZ1Y15kFuaGsDA80bgOqppOzZ3GcyJ-QIxewHJ_bq_aQOIPsXffeKLau_vGgctnu462bANMzXfT95_eDRkpZZZm-C_dAOdP1Aj62QQt5p-Hisf-NPO-iKaG2H8mK7J9eBwAHFah6B5JZyi5TBpnr4gUv5GIR-67vlYVruHWpYjyr04E2sIS59nvm08-Ltf1zPoo9mdvidm9r7JGTGZo5S_Sb5lIFxjc51-6IvcqnFuXZnBr8Ovaen_n2JnbGnvXu4exksAHZE98VQK49rx3HFXtbVRKgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح یک دیوار در تهران و گفتن از نابودی اسرائیل در ۱۵ سال آینده!</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5203" target="_blank">📅 18:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5202">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TQUaL7gmxkQZp4mU4hjOVIiivfyaraDHFIbfTJq0XtJgkNDixvqFw6ZGFjKGtXyw0BHQamd9DKyqdYL9p9shLLt8Vi23AmTg8fz3B3LGJjHGzsVSmNsvmHER_6EqHbbfYZ2om15DpeXYQECX3qRCCYznNjMWghic1s1HcJanKEEuF-5EgMojzCnjlFOnVfcWjrxYuMUu2njHC9RJ-j1eJ_pcGHp0QVtEwJUs8XsIin4rrbyeapufBLAtfkuF733Bz4GD4afyrk6mQ1HO201ZLXyAiAhkGfsCWwRW4fxdIHyCsGyZXOCtPgq3MTxuuzCQJZaCHVUB69zBf7x8Ok7PTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمادگی بهتر برای جنگ بعدی …</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5202" target="_blank">📅 18:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5201">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : برای اتخاذ تصمیم نهایی اکنون به اتاق وضعیت می‌روم.
«ایران باید موافقت کند که هرگز به سلاح یا بمب هسته‌ای دست نخواهد یافت.
تنگه هرمز باید فوراً باز شود؛ بدون دریافت هیچ‌گونه عوارض یا هزینه‌ای، و رفت‌وآمد کشتی‌ها در هر دو جهت به‌صورت آزاد و بدون محدودیت انجام گیرد.
تمام مین‌های دریایی (بمب‌ها)، در صورت وجود، باید از بین برده شوند. ما با استفاده از تجهیزات پیشرفته مین‌روب زیرآبی خود، تعداد زیادی از این مین‌ها را از طریق انفجار نابود کرده‌ایم. ایران نیز باید فوراً هر مین باقی‌مانده را جمع‌آوری یا منفجر کند؛ البته تعداد آن‌ها زیاد نخواهد بود.
کشتی‌هایی که به دلیل محاصره دریایی بی‌سابقه و فوق‌العاده ما در تنگه متوقف شده‌اند ــ محاصره‌ای که اکنون لغو خواهد شد ــ می‌توانند روند بازگشت به خانه را آغاز کنند!
از طرف من، رئیس‌جمهور محبوبتان، به همسران، شوهران، پدر و مادرها و خانواده‌هایتان سلام برسانید!
مواد غنی‌شده‌ای که گاهی از آن با عنوان «غبار هسته‌ای» یاد می‌شود و در اعماق زمین دفن شده‌اند ــ زیر کوه‌هایی که تقریباً در نتیجه حمله قدرتمند بمب‌افکن‌های B-2 ما در ۱۱ ماه پیش فروریخته‌اند ــ توسط ایالات متحده از زیر زمین بیرون آورده خواهند شد. (طبق توافق، تنها آمریکا و چین توانایی فنی انجام چنین کاری را دارند.)
این عملیات با هماهنگی نزدیک جمهوری اسلامی ایران و همچنین آژانس بین‌المللی انرژی اتمی انجام خواهد شد و این مواد به طور کامل نابود خواهند شد.
تا اطلاع ثانوی هیچ پولی میان طرف‌ها رد و بدل نخواهد شد.
در مورد سایر موضوعات ــ که اهمیت بسیار کمتری دارند ــ نیز توافق حاصل شده است.
اکنون برای اتخاذ تصمیم نهایی به اتاق وضعیت می‌روم.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5201" target="_blank">📅 18:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5199">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Emy13ctoIFagjasAyRQ4Qv1IXeLjxEt1jm4uJu18sHmRwUl2R9iiBUD4AeXppHFALwe0a8SJkpRAmbueU0su3TmiRkHB4OmOxbpRdSaCpBu6wccvuGRtnNmO7Bh0FAkK2A2VewkdrQzDa-8_xb2A3FuAElK4ZkSZrXCISGSOHV8-0xY7tWv8-9M33xZMC-pNsbPwPjhIvkgyC7FNqFOcnngfc0Ij5df-_uz_Abnhxt5O31GDwyZtoU1CQ3rSMg2wq87cWVgmPrAjX_8TrvwUW7SkrdefIYKEGaCid4idxqNXKUosH2VcTTo78H-_cx2o5ZSvijxxBrfTUeSA5_0RFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mjdY7LIjgW7GO9csDAyLpEF0jQN_J6gYwoNfsPj-VyTeUMZyktRogB5oW2k6vUqUAhiyBKju3smCmsrOS-J5tqWCdOVOSiM9zIxyjGWIdMCQIOeXiGNUf5LpfzUAMeIrlxUHuqTUCtXPPH8uecuPttTGepJrmLHz6rde3nKEmHMfxoW-GQWt5w3jhmCk4BcUWUFrSV-0eJRHaTlRFPOC0tv2ATB5dmV2p1xUhdYXOEQBJVQRqtAU6DLEqHnZjO24paQafNRhn72J4Dead59JCVQmEjIRvNSDYldYfg90CUrFekDFT5pG0VWJRa5a6VCCwbUp_sQrMDS_guJc8D1CTw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی شما نبودید
لبنان سفیر جمهوری اسلامی رو اخراج کرد!
گفت «عنصر نامطلوبه»! گفت که جمهوری اسلامی عامل وقوع جنگ در لبنان شده و جنگ
رو به مردم لبنان تحمیل کرده.
اما سفیر جمهوری اسلامی در درون سفارت خانه موند و گفت برنمیگردم ایران!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5199" target="_blank">📅 18:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5197">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AwAiWRCtR_nfQb2r9kUbXuMTcD86ZQRxB7DbU5PRLS2ANBIv-IiI5M1bWClp1PdnSnKC9plEU-WJKn-AP90S879vsEuwnbdOhfQJ10rSAl3zn5MaGDXmoklQSFxuCXoOmY60Uvk9POcR2-ZxG4gDgK_M3xjSnPAuhAXCEPsnlc7aTs20nePLKi_0VBJQ8CGSnIvgrgSuDTdZTC_LmjFRKmAoWiRVs0Tng3EysI8NnQGm4MU7hg6pErI2iM-E4CdNSf9lHkZ843dxoV4WOaBRAtxGbd99foksNQ2gz1BVumFOesi1n8IijkCNdT8MRFt-pKrWNGaZyNct9q-LUp4U9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nHA7SWkvoLd8TmlD8lA_KfMjt2tTDAx26dmuZ_zVDdwCK9bskUpxvWKucMESUvo4FVAhzLOsrw-wau6cdFf5W8FDDf2lLdyXVSvTYUyBdL94bzkZV2Bw8BmkqyreYAA-ed4045RFZmWt7DWhZ3c39PkKyVlBkHo1C8QW6xxsUSIMwo1IihMM__vPT-o10a_z0quJRFlmqL8P__h-Nbdym6rvuH8LbiRzHhcZEm5J1Af007XeQ8VdUGiAouENz12JJWfOtpN2fTdEIOTaxNZIVOGWv2Klvq6WpoNmYS23PFekV79xp0uWolLvbDqtJYMtFhPYneG1hnjYjCz_xlmMTA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی شما نبودید
درسته هر شب توی خیابون‌ها بزن و برقص و عروسی داشتن اما در افغانستان گدایی پول میکردن :)
سفارت جمهوری اسلامی در کابل در اواخر اسفندماه رسما تقاضا کرد که  مردم افغانستان به جمهوری اسلامی کمک مالی کنن!</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5197" target="_blank">📅 13:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5196">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07fac9d6ff.mp4?token=YmpXWP8VtYXDSsL8VsrjiphZK3FALRVcr_by4Bpfe6rlsQPx29U3Yjxd4ZAeWt0DYGobjVfactDQmyBDtjsP92TBF59qlJFxRp0BKgO_G-7nT3ktuQhLugk9JnwpbifgNga03Tbm4T0S3eyt2U2PWxDObTg6YQ773ej5OO9ABum__b-N8gNWur3AFQTV3vJysPBhwHXd-WU-LQELW8lV5VPpxKTTGY8iEny53g8uN-OJER9QwOOgk8wJltbNFQJnnF1weN9IbHLz7MQtbmMWq5tVKmA_yoXUJO9cRYfgfgoBU_Uca0wUaUs4k9yj1W1W6Nq2XMlT-vqb1PfpzaovFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07fac9d6ff.mp4?token=YmpXWP8VtYXDSsL8VsrjiphZK3FALRVcr_by4Bpfe6rlsQPx29U3Yjxd4ZAeWt0DYGobjVfactDQmyBDtjsP92TBF59qlJFxRp0BKgO_G-7nT3ktuQhLugk9JnwpbifgNga03Tbm4T0S3eyt2U2PWxDObTg6YQ773ej5OO9ABum__b-N8gNWur3AFQTV3vJysPBhwHXd-WU-LQELW8lV5VPpxKTTGY8iEny53g8uN-OJER9QwOOgk8wJltbNFQJnnF1weN9IbHLz7MQtbmMWq5tVKmA_yoXUJO9cRYfgfgoBU_Uca0wUaUs4k9yj1W1W6Nq2XMlT-vqb1PfpzaovFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی شما نبودید در اجتماعات حکومتی شون هر شب عروسی داشتن!  «صیغه یک ماهه»! در برابر «یک سکه» :)  با کسب اجازه از امام زمان</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5196" target="_blank">📅 13:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5195">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8f5663381.mp4?token=jfwA3Ig5dRjP_TuKO-zloavowBoUsS3ENm7fTG5V9zJH8n_b6nLnf76dJZY1C38vK_SSW79oGsj63vvKK4KQ_Z7QlgJQYaLMpwqfI0jSCsg2r82UVDeYdU1rIB89pRipDHcRNPCId-Z-vsUpouQnNouXPQ7RcD2a4lmMTcUjmiZJzy5YFOiUhWvNg1wpPSh3W8R9_E7e_KI0ThMk5OlsT7RX5shDy7wS1H1twPa3u9cop3GDC5EVFyxhqaj6y2TqPgYQg_Bzb4BTsPLA79a-E5bE0zn2isFIjUeYJtLPgyaeF-XmnpZT3XoLRktvTjRHknsHR1vtlJ4UanyaFZBlig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8f5663381.mp4?token=jfwA3Ig5dRjP_TuKO-zloavowBoUsS3ENm7fTG5V9zJH8n_b6nLnf76dJZY1C38vK_SSW79oGsj63vvKK4KQ_Z7QlgJQYaLMpwqfI0jSCsg2r82UVDeYdU1rIB89pRipDHcRNPCId-Z-vsUpouQnNouXPQ7RcD2a4lmMTcUjmiZJzy5YFOiUhWvNg1wpPSh3W8R9_E7e_KI0ThMk5OlsT7RX5shDy7wS1H1twPa3u9cop3GDC5EVFyxhqaj6y2TqPgYQg_Bzb4BTsPLA79a-E5bE0zn2isFIjUeYJtLPgyaeF-XmnpZT3XoLRktvTjRHknsHR1vtlJ4UanyaFZBlig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی شما نبودید
در اجتماعات حکومتی شون
هر شب عروسی داشتن!
«صیغه یک ماهه»! در برابر «یک سکه» :)
با کسب اجازه از امام زمان</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5195" target="_blank">📅 13:18 · 08 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
