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
<img src="https://cdn4.telesco.pe/file/c93T5aOxeOxda--YV0PfwAmMI3VG90sNuUJQHGnLw0a18UJEdAHWL2-KsS5XoFBVRLuv0U3tXPbZ3W1KyoAbJAv45W3GL-YOXFXJwodMZTp9MmqbFTcJhXTvvTgVYGOXPTXF1LYFODHPXoF92Wd58sCCJAbICrfZZfdiC6vTEUGXtDIHRKsnGNfUNjTj4tqBe9pv_JW0qGioeLvCWtIXeDlFbUj-fpyBYI-bGSl8RaF4DectMLiDLRyUzBykr0Os8BB-SZ8ZtmrWepHEq76C4-5GjqjmOx89JniJ8STXEfFzKCLe6btcGwWuOzlJt3x5vYxQcyK5yI-Esy89vDgChg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 105K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-13 22:09:04</div>
<hr>

<div class="tg-post" id="msg-72795">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60d10955ac.mp4?token=Xg3_DFIimTTSOgnSrzqhj3CKZBY6eqbNE3tPox0TbLzB-5vLmLCZl1sAsOSr8jU8MbldEqq1Uz7nBlXCdlDwxAXAy6uPl42ucaWvW-cpswfAX7lXqG1aJ8eAYyY6I-IJ3SP_WvSqqmlHEuh29Q0qNqsIf9xFwkb4f3GUr-i5pxwZmsEodAz2WDX2uT600b3G5YCwnQk7Dj1pG51ySyHF7OlSG9OnCsztQKTlkZQ0EIn4-iN24vunycbPJjgN0H6tb39QzAVgy08WJHZDnjtq4F6RCu-GSQQqZ9Qdc0PVaFOw9PM7o2y6HZ-kJe3ITrce3Euao6kgM9ig5j2b6htOFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60d10955ac.mp4?token=Xg3_DFIimTTSOgnSrzqhj3CKZBY6eqbNE3tPox0TbLzB-5vLmLCZl1sAsOSr8jU8MbldEqq1Uz7nBlXCdlDwxAXAy6uPl42ucaWvW-cpswfAX7lXqG1aJ8eAYyY6I-IJ3SP_WvSqqmlHEuh29Q0qNqsIf9xFwkb4f3GUr-i5pxwZmsEodAz2WDX2uT600b3G5YCwnQk7Dj1pG51ySyHF7OlSG9OnCsztQKTlkZQ0EIn4-iN24vunycbPJjgN0H6tb39QzAVgy08WJHZDnjtq4F6RCu-GSQQqZ9Qdc0PVaFOw9PM7o2y6HZ-kJe3ITrce3Euao6kgM9ig5j2b6htOFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی: اخراج ما از آمریکا مثل اخراج تیم برنده از المپیکه!
پس خبر درست بود.
@News_Hut</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/news_hut/72795" target="_blank">📅 21:35 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72794">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d035f07a6e.mp4?token=PUcEA0i-MYR1_ec4epANSrl14qaiZlOTHwKOK-vodbU1UmuyrnFjfx2z97uqlBH__ihEzq9hQaQjh3tg1SNguWRhpBaqniBnOVqLkiRWJXdEcOBEjHIiH4muEsln-u3C9TSEw63JGvlOuro7v4s6TLTw3L__zIvc_DZnfC8EAanD_oP-AYH5XiDYOpq-n5bzSzgv15Jo_Zh8HCsyM82fJbvcTsPynR8ZpUlkAKz9qQz6vxl5z8uwWpQghgPuDXz8OaCE2n-Bprn2gBgNhsReJhYYUFOIlGrXZvK_W_caFNqzs7tEnsNv62nsm0EkJtUXUPWN0gQiA73_FsHHAkbX1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d035f07a6e.mp4?token=PUcEA0i-MYR1_ec4epANSrl14qaiZlOTHwKOK-vodbU1UmuyrnFjfx2z97uqlBH__ihEzq9hQaQjh3tg1SNguWRhpBaqniBnOVqLkiRWJXdEcOBEjHIiH4muEsln-u3C9TSEw63JGvlOuro7v4s6TLTw3L__zIvc_DZnfC8EAanD_oP-AYH5XiDYOpq-n5bzSzgv15Jo_Zh8HCsyM82fJbvcTsPynR8ZpUlkAKz9qQz6vxl5z8uwWpQghgPuDXz8OaCE2n-Bprn2gBgNhsReJhYYUFOIlGrXZvK_W_caFNqzs7tEnsNv62nsm0EkJtUXUPWN0gQiA73_FsHHAkbX1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه آقای آتش‌نشان در مورد ساخت پلاک مشخصات برای دانش آموزان:
امروز رفتم یه دبیرستان دخترانه برای کنترل مسائل امنیتی بین حرفامون با مسئولین مدرسه متوجه شدم که دارن برای دانش آموزان پلاک مشخصات فردی درست میکنن مثل همونایی که زمان جنگ استفاده میشد؛
از این پلاک‌ها که زمان جنگ سربازها مینداختن دور گردنشون که اگه بر اثر بمب و موشک چهره‌شون دیگه قابل شناسایی نبود، از رو پلاک شخص رو تشخیص بدن..
وقتی پرسیدم برای چیه؟ گفتن نمیدونیم فقط از بالا دستور گرفتیم و مشخصات فردی دانش آموز رو دادیم تا براشون درست کنن!!
@News_Hut</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/news_hut/72794" target="_blank">📅 20:40 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72793">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/unmr_ge4zKI1yBvHZlfOGpJZGMVjsqke3FFqv_9uJZ8aUiI5SoxjexZzFO1uVset4HeLCIPp6Ybw6CI8zRKJ5sNuf8vSxBWwwAFzylxWxFu56skFqp4behyjaAJoV-Vi3K5q-ZC80vPI-y1HgQls0Ruj-7hJIKYf5rcGYIf5Uirp26JKoDWmkDqpEirIyM2iUmbjKEqV26Rwoq2_JCAmN6Xq74n7pgjDe6cJ3a_IIsi3BiZTkwSG7aRXTRgaw-qPQDVk3WBzdtlzizgV13qGgROrygo-BIRfONQsZwBFefhLR8toE4QXNxJd6_bAkgERkoMehwh_TJl4vKtf62ZDlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
آنچه باعث افزایش قیمت بنزین می‌شود دیگر تنگه هرمز نیست — چرا که اکنون حجم بی‌سابقه‌ای از نفت (بشکه) تقریباً به‌صورت روزانه(از تنگه هرمز)عرضه می‌شود
.
بلکه مسئله «پالایشگاه‌ها»ست؛ جایی که پالایشگاه‌های روسیه توسط اوکراین منفجر می‌شوند و پالایشگاه‌های ما در ایالت‌های آبی (دموکرات‌نشین) مانند کالیفرنیا، توسط «دموکرات‌های احمق» تعطیل می‌شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/news_hut/72793" target="_blank">📅 20:17 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72792">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/902f67b684.mp4?token=SQf3A_PTHjal1mIgZrHKa6fjebj7QPPsLrTnJlFjSUC1t67wtWrgtoMMcJXiGTqy1cQih-oGdJXsMNCYC1_VVyTqV9rWqLkCIziNlxObuv9nQa8JYFZx4pzb22gFMg7N228GNs60T7B2zxCrfzSlLVtqGtnuzHi0sx_lh8J_O4v9Mftw6T0LOuoBOLzI8HPJYQCOYB729GJpWi-Kee7SCj7Pmj-VhZ5LghuKmDtq7Z0ndY0DmmQeHG3Tsm7dxAcRdwgpffM-jMls6Dmg2dbBfv6p6HMqXmLrKQvK71PtLkvZuuTsGYnwIrdMYEIpHD0jMks2HgInFnJncRNGkWJBZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/902f67b684.mp4?token=SQf3A_PTHjal1mIgZrHKa6fjebj7QPPsLrTnJlFjSUC1t67wtWrgtoMMcJXiGTqy1cQih-oGdJXsMNCYC1_VVyTqV9rWqLkCIziNlxObuv9nQa8JYFZx4pzb22gFMg7N228GNs60T7B2zxCrfzSlLVtqGtnuzHi0sx_lh8J_O4v9Mftw6T0LOuoBOLzI8HPJYQCOYB729GJpWi-Kee7SCj7Pmj-VhZ5LghuKmDtq7Z0ndY0DmmQeHG3Tsm7dxAcRdwgpffM-jMls6Dmg2dbBfv6p6HMqXmLrKQvK71PtLkvZuuTsGYnwIrdMYEIpHD0jMks2HgInFnJncRNGkWJBZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیت هگست وزیر جنگ آمریکا توانایی خودشو توی بسکتبال هم نشون داد و تقریبا همه توپاشو سه امتیازی وارد سبد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/news_hut/72792" target="_blank">📅 20:14 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72791">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0b5a00bb1.mp4?token=DLdWEpJzFCvGf29TfrvSOQCYia688RXPdhGL90rRz8hyfz5v3wC1VPK2KDVedjP35GkixJ3LA-9L9kHQy4sKaFxyZ3XBEwpCSBkRmPaovkpV72lPtd6rUOqw3EB9NDaDvDMsEpVFWZ7ip1t75ELo7YTsxVgVroqcUAbJL-arzO1nOi_chOTmyTag0vUUVagF64KGT62fPL7MT_R4huxmT8oGmxeGgvsznu_1zSlG4yfodjtO9YHeyySLasjQw18v_AVVV6DJzcY9Nx-6CjuwBZH0gCgiHaAEvzK5SBuZAOKQIMZfsLX7a2oj5iPADf5q4a3Fuw9EVChbU5ZZ6dpo7wvNPqml1TB0BKx427e9FE_nNIQvCbnzD9AkumeaNHiONTNmCY_21Hlq2NOGeBzKQlQ_KlyMAG1H4NoeP1YXY0yeumELf3VK-m8rMM0_Ab9S5nsiQneyWfn5MfhVhsyb0ngBi5K-L0UYq3NzVzbRxskNLv_Ayq8fVz3_w-XuP_hCbIDMJv0UCic6r2LU5TfoyfUg3R8BYgRxkk67QfIpFRDHwM4QgFMKWwGJuqc4Ltlk4yYyHI2kiwxho_KzVPdgpr3vBeZ7tDkNuLAh0pVoh_RnGTraBKY1P8CFBmZNt8SHc4NXAg-FmMia5aUuGNhbOLsKk3u_nyyJmpKfQrsxpJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0b5a00bb1.mp4?token=DLdWEpJzFCvGf29TfrvSOQCYia688RXPdhGL90rRz8hyfz5v3wC1VPK2KDVedjP35GkixJ3LA-9L9kHQy4sKaFxyZ3XBEwpCSBkRmPaovkpV72lPtd6rUOqw3EB9NDaDvDMsEpVFWZ7ip1t75ELo7YTsxVgVroqcUAbJL-arzO1nOi_chOTmyTag0vUUVagF64KGT62fPL7MT_R4huxmT8oGmxeGgvsznu_1zSlG4yfodjtO9YHeyySLasjQw18v_AVVV6DJzcY9Nx-6CjuwBZH0gCgiHaAEvzK5SBuZAOKQIMZfsLX7a2oj5iPADf5q4a3Fuw9EVChbU5ZZ6dpo7wvNPqml1TB0BKx427e9FE_nNIQvCbnzD9AkumeaNHiONTNmCY_21Hlq2NOGeBzKQlQ_KlyMAG1H4NoeP1YXY0yeumELf3VK-m8rMM0_Ab9S5nsiQneyWfn5MfhVhsyb0ngBi5K-L0UYq3NzVzbRxskNLv_Ayq8fVz3_w-XuP_hCbIDMJv0UCic6r2LU5TfoyfUg3R8BYgRxkk67QfIpFRDHwM4QgFMKWwGJuqc4Ltlk4yYyHI2kiwxho_KzVPdgpr3vBeZ7tDkNuLAh0pVoh_RnGTraBKY1P8CFBmZNt8SHc4NXAg-FmMia5aUuGNhbOLsKk3u_nyyJmpKfQrsxpJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس، معاون رئیس‌جمهور، درباره خروج هر ۱۲ فروند بمب‌افکن «بی-۱» (B-1) از پایگاه نیروی هوایی سلطنتی «فیرفورد» (RAF Fairford):
آنچه در آنجا شاهد بودید، اقدام وزیر دفاع برای محافظت از نیروهای ما بر مبنای احتیاطی مضاعف بود.
ما با اطمینان نسبی معتقدیم که ایرانی‌ها در پی انجام همان کاری هستند که حکومت ایران طی ۴۹ سال گذشته انجام داده است؛ یعنی ارتکاب اقدامات تروریستی علیه ایالات متحده و همچنین علیه بسیاری از افراد دیگر.
ما نهایت احتیاط را به خرج می‌دهیم.
@News_Hut</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/news_hut/72791" target="_blank">📅 19:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72790">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZMRUtVpSssXKddJ815powt2pM3APVTs5eIlY2qsvLw-7zgW-ailHmyCS8SW7IY4maMs8mmfvdzkMryVcZhGT9N-g-OQgc7qFOTqTD0ZMzOQ71jbW1LCa_AEESt38xmu_PldNxg8DYWDctPv60BG8UCsL7-YAAyfpNx_3HgZG70N5XUTpaO9GOoe00CQtnBZNYpQXu0UNoCYpAEE93hXQ6IP3t1bxfvujZclcb8LoCQHzhp6pEfIRT37xP3kANHGBoggW96iLaHFof7u_xxhlwD43h-4hda1hSR9GrbdtdEhsgeCi8ncK0yieLWohm7YqnxbDYXnZ9DNmz10_0K4yYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز:
ناو هواپیمابر آمریکایی «جورج اچ. دابلیو. بوش» به همراه حدود ۴۸۰۰ نفر از کارکنان خود، پس از شش ماه پشتیبانی از عملیات‌های ایالات متحده در خاورمیانه، برای یک دوره استراحت وارد پوکتِ تایلند شد.
پوکت نخستین بندری است که این ناو از زمان ترک ایالات متحده در ماه مارس در آن پهلو می‌گیرد؛ قرار است کارکنان آن از ۴ تا ۹ اکتبر برای گشت‌وگذار، فعالیت‌های فرهنگی و برگزاری یک مسابقه فوتبال میان آمریکا و تایلند، در خشکی حضور یابند.
@News_Hut</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/news_hut/72790" target="_blank">📅 19:07 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72789">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d3aadbf79.mp4?token=QxL3s-Q0QxjTMFEcqWp7cg8BUtzKhT5GyyTMMn7s6RdWy3nCUg6Ca_egGVKtXfbgldMl21SxTQy3dYAxLyCtNs2ZLoxGHKZASrkSvbH01WQ9u0dnjliciEehcNOnWeL50o3mDM31mh8u8rjeqzN71cMcOFBMjOZBwTf_ys9lYqN44HR3wT91MaoxJKdQhVxC4zKB_j2KJLRVJrjJAklucv69q1eZzn8D2_iDGUCFZIYMPJQlBqvPUQEtT-F97Gbx05U0jkb4oB7OOYuXc-kDEb_YejZz7YgWs8Zk_178L1XAdt4i7xLF8elnN6l4l1MSi5Euj00VkitMoe54VQvN_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d3aadbf79.mp4?token=QxL3s-Q0QxjTMFEcqWp7cg8BUtzKhT5GyyTMMn7s6RdWy3nCUg6Ca_egGVKtXfbgldMl21SxTQy3dYAxLyCtNs2ZLoxGHKZASrkSvbH01WQ9u0dnjliciEehcNOnWeL50o3mDM31mh8u8rjeqzN71cMcOFBMjOZBwTf_ys9lYqN44HR3wT91MaoxJKdQhVxC4zKB_j2KJLRVJrjJAklucv69q1eZzn8D2_iDGUCFZIYMPJQlBqvPUQEtT-F97Gbx05U0jkb4oB7OOYuXc-kDEb_YejZz7YgWs8Zk_178L1XAdt4i7xLF8elnN6l4l1MSi5Euj00VkitMoe54VQvN_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حوثی‌ها به معنای واقعی کلمه به سعودیا دارن تجاوز می‌کنند، یعنی شما کاکولدزاده تر از ترکیه‌ای‌ها، پاکستانی‌ها و عربا نمی‌بینید، بعد حالا فکر کنید این سه تا پیمان دفاعی هم دارن =)  تازه از خواب بیدار شدن گفتن عه بهمون حمله کردن بزار یه گوهی بخوریم وگرنه شرفمون…</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/news_hut/72789" target="_blank">📅 18:58 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72788">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">حوثی‌ها به معنای واقعی کلمه به سعودیا دارن تجاوز می‌کنند، یعنی شما کاکولدزاده تر از ترکیه‌ای‌ها، پاکستانی‌ها و عربا نمی‌بینید، بعد حالا فکر کنید این سه تا پیمان دفاعی هم دارن =)
تازه از خواب بیدار شدن گفتن عه بهمون حمله کردن بزار یه گوهی بخوریم وگرنه شرفمون از دست می‌ره (کنترل شهر مهم تعز همچنان به دست حوثی‌هاست)
#hjAly‌</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/news_hut/72788" target="_blank">📅 18:52 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72787">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">حوثی ها دو موشک را به سمت منطقه ای که تحت کنترل نیروهای دولتی یمن بود شلیک کردند.
در همین حال خبرنگار شبکه العربیه در حال آماده‌سازی برای پخش زنده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/news_hut/72787" target="_blank">📅 18:28 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72786">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/crQrINOsqdz3mOHl3ddlXHzMIEWho8qdF_HMwbARIRBChwbZVzAZcjiq2nIkkV_MA5UBAYWkZOGts_wNxYMJjsRfa9EL4KzxigHzbiY8Ivv43HYCDLC_4AaVVMYP4x7dBz3i3FknzvBmc8u4mzZGSuMi8hN4jkKPDYq3aDhmWdaYD5KeMAwVzF5BEN7_Gf0Wc3vcSFEnmy21O7aN2337Bz0mbLLOzXbU09JTErcnEB5f_R21AvrnN67fOzqFuggsRpujq6_O2AkXzjjEk-sVEM2JnBmZNwgASQfJuymkd3VU9d3FrjsMy0HsIpoSaldvGiljaQsdWJ8pZVw3IYedIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#مهم
؛
مشاوران ارشد امنیت ملی ترامپ نشستی محرمانه و چندساعته را در «کمپ دیوید» برگزار کردند تا درباره احتمال جنگ با ایران و درگیری میان عربستان سعودی و حوثی‌ها در یمن گفتگو کنند.
ریاست این نشست بر عهده معاون رئیس‌جمهور، ونس، بود و مارکو روبیو، پیت هگسث، استیو ویتکاف، جان رتکلیف (رئیس سیا)، ژنرال دن کین و اسکات بسنت (وزیر خزانه‌داری) نیز در آن حضور داشتند.
یک مقام آمریکایی اظهار داشت که در این جلسه درباره مسائل عمده خاورمیانه «تصمیم‌گیری شد یا دست‌کم بحث‌های عمیقی صورت گرفت.»
@News_Hut</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/news_hut/72786" target="_blank">📅 18:12 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72785">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72785" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/news_hut/72785" target="_blank">📅 18:12 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72784">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YaH8oI4A7bW_Fn_iOpCPmoZYl8q1tqWBaPNxyeBrMwCOCrZ-1e5lV2Q8qakRMjZYhOLkKWmzzkuEzgRGsVJO6in63uNjtoLuLtmptBsPbR9Wywuc1AR1yYHek0i27hlJqkHq3mR5QjsDuuivpZoNw9Y7uPrXsPZiJKNNq4-yy81Sn35N6bHGcaV-Vzu3A6C1Fi9WzieNMZx3ZC8FCJZId7ZE5RZDGQLT_zoMD54jiQDh6gulnwmC89PSmdcMr0gusMhKt5vkFEn2XSylm_2gvKvlS-VyGHVjKYWxFtM9k9BcUSsvi8pNW1N5uxPQGESJN3Cemis8FPpheoWmXLj0AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز بلژیک
🆚
فرانسه را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
بلژیک: ۳ برد، ۲ شکست و ۱۰ گل زده
فرانسه: ۲ برد، ۱ تساوی، ۲ شکست و ۷ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/news_hut/72784" target="_blank">📅 18:12 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72782">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e7b8e8d5c.mp4?token=kCxHKeFtyD3exLNmBLbDPuaieM-v5NjVcIYXZr0ApGUlO3nWOL6pIteQ1QUDTibs0QiVv4dsQpusLKPOjh9r8_1yo6PVYpjriznsgdSSO_58w-lRO-5lsvK-RQADgGtxJJ0hLG0btb0dyqdacsxcwc35YlNRNJfSU9EQZhrElpd_znRhUpK9BSR3BYvtuvgqqiBDZcEMBhXhj0dGTCkzt7jPzpoiIzhaI_MI7-bX_lRQ6Y4U9csL0f_GzMBU5AHI4d0fv4IgcD3BDFl3t7MFQpr0kOXXzv8VzfMu9yJNDq7qwTCHuVmJ9eGU_RjtcXz0x3MPjrJyuhpW_RUPRqaXPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e7b8e8d5c.mp4?token=kCxHKeFtyD3exLNmBLbDPuaieM-v5NjVcIYXZr0ApGUlO3nWOL6pIteQ1QUDTibs0QiVv4dsQpusLKPOjh9r8_1yo6PVYpjriznsgdSSO_58w-lRO-5lsvK-RQADgGtxJJ0hLG0btb0dyqdacsxcwc35YlNRNJfSU9EQZhrElpd_znRhUpK9BSR3BYvtuvgqqiBDZcEMBhXhj0dGTCkzt7jPzpoiIzhaI_MI7-bX_lRQ6Y4U9csL0f_GzMBU5AHI4d0fv4IgcD3BDFl3t7MFQpr0kOXXzv8VzfMu9yJNDq7qwTCHuVmJ9eGU_RjtcXz0x3MPjrJyuhpW_RUPRqaXPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت های جنجالی کوچک‌زاده مجلس :
کدام کارمند و مردم عادی پول دارد ۲/۵ میلیارد تومان بدهد ده هزار دلار بخرد، این پول زیر متکای امثال همتی و دزد‌ها و اطرافیانش میرود.
آقای قالیباف، چرا مملکت اینطوری شده که راننده رفسنجانی هر کاری می‌خواهد در این کشور می‌کند؟
طرح جدید بانک مرکزی؛
هر ایرانیِ بالای 18 سال می‌تونه تا 10 هزاردلار (۲ میلیارد و ۷۰۰ میلیون تومن) از بانک بخره!
@News_Hut</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/72782" target="_blank">📅 17:33 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72781">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f1c650a97.mp4?token=VL_WkK8jjAGqWinQml6_1lvZC9mpug9YCH0-2Sm349Zj-6HZTHLroFTg3wrguGMzKL9cd_QZ5ubpKttOJDQiyB0-EP4UNerjcSaIOWKeFNxib1yK_oDjNoPayIvLP85V5wKw6uaxv7BkvsGSzW_OZMOMhnkQHLGbI4yB54KUcUpMh6SO9eD92Ig3bpXLdKWPoqEvwm-1dS8BKOFsFemEMx-X4jX3x6RZWz3z6JUIjNEm9wI5r29w3_5m3qEw2ZxG460WTLDm5b58Eay-a16ATyizeyRgnVbc74fSIO0Oe2v8ju3_6rddLuktWhl5kkM9WJt9f2fX9bTwZfAYu0iX17G398jv5NhgJtZla8idDUYKUxJOTvqMetPu9hAIzNY6qKH9Y77p-ePgL0xac_HBidXp5pvn6a2PL63neVk0EAwQXuFjvLREO6V57ipZpEm1nN-u-vOq7tX4gJTsW7myOmnUQl97R2DCXVZ7bmW8SQgyR83Cxx-PmwaMe-b1JmVd-xDkIHq_pAczLV8Wvzdd3Hn2Dp_ORY9MPcXTI1iAGOTyXm95D_1nWfIGVsWmY7XJ8_aAz6E7vfMJUJ3GRM8AEQuX7Xx-RFfKgAYanR819w9KrWLGN2gsxny6CpnMnm6GrcIsvE8H0ppekmMoPQL-tS-msMY64cvuJAzzsQW9kQE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f1c650a97.mp4?token=VL_WkK8jjAGqWinQml6_1lvZC9mpug9YCH0-2Sm349Zj-6HZTHLroFTg3wrguGMzKL9cd_QZ5ubpKttOJDQiyB0-EP4UNerjcSaIOWKeFNxib1yK_oDjNoPayIvLP85V5wKw6uaxv7BkvsGSzW_OZMOMhnkQHLGbI4yB54KUcUpMh6SO9eD92Ig3bpXLdKWPoqEvwm-1dS8BKOFsFemEMx-X4jX3x6RZWz3z6JUIjNEm9wI5r29w3_5m3qEw2ZxG460WTLDm5b58Eay-a16ATyizeyRgnVbc74fSIO0Oe2v8ju3_6rddLuktWhl5kkM9WJt9f2fX9bTwZfAYu0iX17G398jv5NhgJtZla8idDUYKUxJOTvqMetPu9hAIzNY6qKH9Y77p-ePgL0xac_HBidXp5pvn6a2PL63neVk0EAwQXuFjvLREO6V57ipZpEm1nN-u-vOq7tX4gJTsW7myOmnUQl97R2DCXVZ7bmW8SQgyR83Cxx-PmwaMe-b1JmVd-xDkIHq_pAczLV8Wvzdd3Hn2Dp_ORY9MPcXTI1iAGOTyXm95D_1nWfIGVsWmY7XJ8_aAz6E7vfMJUJ3GRM8AEQuX7Xx-RFfKgAYanR819w9KrWLGN2gsxny6CpnMnm6GrcIsvE8H0ppekmMoPQL-tS-msMY64cvuJAzzsQW9kQE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سؤال: چرا بمب‌افکن‌های آمریکایی پایگاه «آر.ای.اف. فیرفورد» (RAF Fairford) را ترک کردند؟
روبیو:
مشاهده چرخش نیروها و جابه‌جایی تجهیزات، امر غیرمعمولی نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/news_hut/72781" target="_blank">📅 17:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72780">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cde1d0199.mp4?token=s6fbKzWD3tFPIplWY3wBOGX12Eus_BRICBHzcFDXsQJ2wJ_jq5Am8zGHmnZrvAjKPkOo5lV6qSMet4pA1UeYUenNvzS7467ZxslroDBOgoIk8roxV8vao6aflQqOBqlkE4lPgalotlw3hCxO-_aOkDrWH5_XWJ_hyCC7Iv5nvE8JfUKylwtWEtLtQnQvAVtZgNAxAPrX1KbfTvPYItlfSN_j3KglFSgzpUq0TWZ5srOk1bdYP9gwkxAaiJkFMf5yMnctQcQvqHeFBtaHGRPRw2-N3M-6Bi2k-Es19zity1k-ixB2GyKhnA8uXuq6pgvsmWo9OjoR9JBEbi3PAiYuXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cde1d0199.mp4?token=s6fbKzWD3tFPIplWY3wBOGX12Eus_BRICBHzcFDXsQJ2wJ_jq5Am8zGHmnZrvAjKPkOo5lV6qSMet4pA1UeYUenNvzS7467ZxslroDBOgoIk8roxV8vao6aflQqOBqlkE4lPgalotlw3hCxO-_aOkDrWH5_XWJ_hyCC7Iv5nvE8JfUKylwtWEtLtQnQvAVtZgNAxAPrX1KbfTvPYItlfSN_j3KglFSgzpUq0TWZ5srOk1bdYP9gwkxAaiJkFMf5yMnctQcQvqHeFBtaHGRPRw2-N3M-6Bi2k-Es19zity1k-ixB2GyKhnA8uXuq6pgvsmWo9OjoR9JBEbi3PAiYuXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آترینا فرحمند رتبه یک کنکور تجربی ۴۰۴، پارسال همین موقع:
دخترا خیلی خفن‌تر از پسران، من مطمئنم رتبه یک کنکور تجربی سال بعدم دختره.
نتیجه:
توی کنکور تجربی امسال از ۱۰ نفر برتر، ۹ تاشون پسرن و رتبه یک هم پسر شد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/news_hut/72780" target="_blank">📅 17:04 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72779">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35a05bc751.mp4?token=iVIN_pYP7hCgxJRebRlSVLCOVniLmR3Jpnjf-h3kJx6wOSeepg5wA9yRlUSyHoL39ZFedLfI9xDkhyeFy1FDmosvowAxwDy_WBLvFF2FlrRr_bPBcTnKtC-Y-QErUvXPCCf8KYFTR9BZXiPSyRwjfghn0F154GXNn3zbNhSI0BVtWkDZ0AYfIqXQVMxDzSWSEwpvaXp7kEePZ8OlvX2E6LJ2-T7rP49t0Hs2ST9zBmjvfS8-143wEdwKioup3--aUi39x5_4W-Eo0xHwmxguNQ0q2tBNZqEY9DvVl8-5anOUF8n5drhacbqcaCaeJYfT-sYyK5qmwh5frxHhCBTySJ8k09wgMf8hXHPILRBJAIh44bqXB-NoIso-K4dgc0qYelc_67KZ-qE--ED5azFi1GMNwKlA0IlJgHKVEyYK3j1Fo_p_xQfKuDlC2Lbd4bq88kfGi-7uwnWQa8yWGDIuxQhcM2ysfQ6C51jVv3ueTqxr7Hi4TuKZZtp-LFOgH7BisbFQZbO5iQfHvCd_Zu99LfgpNwm6fsNyrc7G1SrVJdGVZqnFOJFL5rEfzoNsUUcHbq5OH1X3RCr-ekagIZlcCfrVlpaekGKD2DNDIYX4yrzjSNNFNm2sIOMmdqZ5lNSDsss95xuK7y1iQjzpvxWsNEGSqhqlziJk6Z4gMQbz-fs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35a05bc751.mp4?token=iVIN_pYP7hCgxJRebRlSVLCOVniLmR3Jpnjf-h3kJx6wOSeepg5wA9yRlUSyHoL39ZFedLfI9xDkhyeFy1FDmosvowAxwDy_WBLvFF2FlrRr_bPBcTnKtC-Y-QErUvXPCCf8KYFTR9BZXiPSyRwjfghn0F154GXNn3zbNhSI0BVtWkDZ0AYfIqXQVMxDzSWSEwpvaXp7kEePZ8OlvX2E6LJ2-T7rP49t0Hs2ST9zBmjvfS8-143wEdwKioup3--aUi39x5_4W-Eo0xHwmxguNQ0q2tBNZqEY9DvVl8-5anOUF8n5drhacbqcaCaeJYfT-sYyK5qmwh5frxHhCBTySJ8k09wgMf8hXHPILRBJAIh44bqXB-NoIso-K4dgc0qYelc_67KZ-qE--ED5azFi1GMNwKlA0IlJgHKVEyYK3j1Fo_p_xQfKuDlC2Lbd4bq88kfGi-7uwnWQa8yWGDIuxQhcM2ysfQ6C51jVv3ueTqxr7Hi4TuKZZtp-LFOgH7BisbFQZbO5iQfHvCd_Zu99LfgpNwm6fsNyrc7G1SrVJdGVZqnFOJFL5rEfzoNsUUcHbq5OH1X3RCr-ekagIZlcCfrVlpaekGKD2DNDIYX4yrzjSNNFNm2sIOMmdqZ5lNSDsss95xuK7y1iQjzpvxWsNEGSqhqlziJk6Z4gMQbz-fs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آیا می‌توانید آخرین وضعیت مورد مشکوک به طاعون در روسیه را به ما بگویید؟
مارکو روبیو: ما به‌دقت وضعیت را زیر نظر داریم. فکر نمی‌کنم این مسئله جای نگرانی داشته باشد، اما نیازمند توجه و تمرکز است و ما نیز همین کار را انجام می‌دهیم.
@News_Hut</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/news_hut/72779" target="_blank">📅 16:43 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72778">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a15378585.mp4?token=uAuvo9mTESrDD6OgoZtmZQGPYUXEDn3l_DpkcoZa0ygz8SFC8EJ0zkV2If8iv7z5UBIP-LxWBFPncEW8BUGfNg3mWS0HDtVaf7dGk9nF5yiJLJumhB6d4cnllk_D2Q6YQXoFaGFqvpk5hK98JPaoiIkH4BZCPuVokxOCKh-O-wrq3V8vPdrWgDIKK1-ekCrsDaGoJWauqagHbtAZD_Ud5fxfC61MCyM9QuH8hTyCVPYkcVtI291VMBGL6qQnfJUMZNYiDr3JGZy4AUJLyi4y9qnP6nnEMaPOK8e-_ATivf4g7xIVgGlOu3G50H97iZaJGyLDgNRM_AmMmZD70aEDV4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a15378585.mp4?token=uAuvo9mTESrDD6OgoZtmZQGPYUXEDn3l_DpkcoZa0ygz8SFC8EJ0zkV2If8iv7z5UBIP-LxWBFPncEW8BUGfNg3mWS0HDtVaf7dGk9nF5yiJLJumhB6d4cnllk_D2Q6YQXoFaGFqvpk5hK98JPaoiIkH4BZCPuVokxOCKh-O-wrq3V8vPdrWgDIKK1-ekCrsDaGoJWauqagHbtAZD_Ud5fxfC61MCyM9QuH8hTyCVPYkcVtI291VMBGL6qQnfJUMZNYiDr3JGZy4AUJLyi4y9qnP6nnEMaPOK8e-_ATivf4g7xIVgGlOu3G50H97iZaJGyLDgNRM_AmMmZD70aEDV4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو درباره یمن:
به‌نظر من، سعودی‌ها و نیروهای یمنی به‌وضوح مخالف آن هستند که حوثی‌ها کنترل آن منطقه نزدیک به تنگه را در دست داشته باشند.
این منطقه در پی تهاجم حوثی‌ها به تصرف آن‌ها درآمده بود و اقدام کنونی، واکنشی متقابل به آن است. ما انتظار چنین اتفاقی را داشتیم و همین هم رخ داد.
سعودی‌ها هدف حملات حوثی‌ها قرار گرفته و متوجه تهدید ناشی از آن هستند؛ از این رو، حق دارند که از خود دفاع کنند.
نیروهای یمنی تلاش خواهند کرد تا مناطقی را که از آنجا بیرون رانده شده بودند، بازپس گیرند.
@News_Hut</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/72778" target="_blank">📅 16:40 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72774">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdd09dcabf.mp4?token=mUGEm8qkuo7EDXulXxG0NBlp8GvzGN50I2EZHMmev-6-AeSkCuShOo4njIi2UMxRGWTkBouUFSwcx4ISfm1BIh33Rv0fu9m_dPp-7WEBZ-xUwTyiGuFFrmTvtj2ECu-4gysIFy5mXOxH_5X90OKSn-CLd-AMygQvuIFkRiL89_vhMEnkvUMaDq5D8iVE-AK0QdDe5WC1IHmgtBwG5gnukNFBnqcAjrqfBlMgKsHLGBwPkg-h6r3d9D7kevOv0_O2bwZZA_-o4PLFtdWuWzDQjfJcar822XIwUJtQJ62idc4NgKb8PQay7-i4jBq_42c1tu8GCUqDX-7LvGp4OmR7UwQtFOdQBrxN1CnW-jyKi96XTtVR0xl68cPM_Z3I89bi_00W206q3Yvnr-YwYKHqOdiDdz2VqxCLaSBmzpWHJAVAGFHI0tC77vY2nWkNRrvSKxRiEPMtpbYuOx8XIW6sC-KBo6eZ9MaUIIwcWD3psiFHLVhSKhjT0x4iNDFqZZFvVJunjVHILSuT2u-rBQNzvARUmB7Ua_QjwtY0gzCKHYj6RJszjpzEa4YE_gs9Nk7_PTMgxGrQips4zRmfUfAbn6_cMOqHVXZ4q96LNjnoLKU2tXYq9IsW7RIbdg36cbnC6rBAOfDJeyBm-YN-CKLmT6Fnh8j7XfoF62KswGJqQ0U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdd09dcabf.mp4?token=mUGEm8qkuo7EDXulXxG0NBlp8GvzGN50I2EZHMmev-6-AeSkCuShOo4njIi2UMxRGWTkBouUFSwcx4ISfm1BIh33Rv0fu9m_dPp-7WEBZ-xUwTyiGuFFrmTvtj2ECu-4gysIFy5mXOxH_5X90OKSn-CLd-AMygQvuIFkRiL89_vhMEnkvUMaDq5D8iVE-AK0QdDe5WC1IHmgtBwG5gnukNFBnqcAjrqfBlMgKsHLGBwPkg-h6r3d9D7kevOv0_O2bwZZA_-o4PLFtdWuWzDQjfJcar822XIwUJtQJ62idc4NgKb8PQay7-i4jBq_42c1tu8GCUqDX-7LvGp4OmR7UwQtFOdQBrxN1CnW-jyKi96XTtVR0xl68cPM_Z3I89bi_00W206q3Yvnr-YwYKHqOdiDdz2VqxCLaSBmzpWHJAVAGFHI0tC77vY2nWkNRrvSKxRiEPMtpbYuOx8XIW6sC-KBo6eZ9MaUIIwcWD3psiFHLVhSKhjT0x4iNDFqZZFvVJunjVHILSuT2u-rBQNzvARUmB7Ua_QjwtY0gzCKHYj6RJszjpzEa4YE_gs9Nk7_PTMgxGrQips4zRmfUfAbn6_cMOqHVXZ4q96LNjnoLKU2tXYq9IsW7RIbdg36cbnC6rBAOfDJeyBm-YN-CKLmT6Fnh8j7XfoF62KswGJqQ0U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دولت ائتلاف مردمی یمن می‌گوید نیروهایش باب المندب و فرودگاه ذباب را طی یک ضدحمله با پشتیبانی هوایی سنگین عربستان سعودی از حوثی‌ها (انصارالله) بازپس گرفته‌اند.
سرهنگ ماجد النزیلی، سخنگوی ارتش، گفت که تیپ‌های غول‌های جنوبی و نیروهای سپر ملی، این مناطق را به عنوان بخشی از عملیات «فجر یمن» ایمن کرده‌اند.
نیروهای تحت حمایت عربستان سعودی در حال پیشروی به سمت مخا هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/72774" target="_blank">📅 16:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72773">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69ab7e166d.mp4?token=GdLzSejaA45pzzMZxFsywcUBVitXAz9A6StsyTiQCgeUJL290WNRKrmXQ9UmwkAcbTHWr--lZXTw47vV405PY3EizrftF4JdoXoLUxL61u4mcdWDMKlJR_fuhXwq6WnUI4MMna_lVVQd0fncB2wZ8MkbaJtTu6tL6Dlz5lybmOGXoiwh_Mnp7xdXHe1GXwCK7heKVPl0JYPPr6btubJXKC893zsQpHvc_o-mviEqBlPfMhCXOGiau2G-Y4X88QmiyHeFa5833Xwq3bJaaH0emlMIPK1skPIQuKdkFOctsGYW4kqiI7gSHO4-74ha71-tTsdL5DWrBI1lBr8z_FGUkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69ab7e166d.mp4?token=GdLzSejaA45pzzMZxFsywcUBVitXAz9A6StsyTiQCgeUJL290WNRKrmXQ9UmwkAcbTHWr--lZXTw47vV405PY3EizrftF4JdoXoLUxL61u4mcdWDMKlJR_fuhXwq6WnUI4MMna_lVVQd0fncB2wZ8MkbaJtTu6tL6Dlz5lybmOGXoiwh_Mnp7xdXHe1GXwCK7heKVPl0JYPPr6btubJXKC893zsQpHvc_o-mviEqBlPfMhCXOGiau2G-Y4X88QmiyHeFa5833Xwq3bJaaH0emlMIPK1skPIQuKdkFOctsGYW4kqiI7gSHO4-74ha71-tTsdL5DWrBI1lBr8z_FGUkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توضیحات خلبان هواپیمایی زاگرس در خصوص نبود رادار و تاخیر پرواز
@News_Hut</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/news_hut/72773" target="_blank">📅 16:03 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72772">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ea9911386.mp4?token=IGaAFmItQXUBNC1BFMQVfPFX5loXdueo9Lx7Vw5yFciAdDrtQqAcIJ_93TfKIgGNCLYWtgOOTCmGfzju5L3ESPiobAsjmJ-lu-w6zb985Ue7Bq4EZER9kmEhZz01F3Q9bclfef9JzwMKeogqSqv8gj04orhhKxzuL9iq--LK34tepcBp7xJWjOJXmR4_RepIghQViMJgJjASL8YQEDcxn9iIrQxvqscM5Y4n7JLbC6CM9W9AAqobnSLijDL1p1kCFAT4VDmSIddUk_Wr_1rqy8JcpE8tl69Xw1xPGLiBZg05vNvJXMWa-0hJipqL0gWASRdqujI7TKSxVWz9OJO_IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ea9911386.mp4?token=IGaAFmItQXUBNC1BFMQVfPFX5loXdueo9Lx7Vw5yFciAdDrtQqAcIJ_93TfKIgGNCLYWtgOOTCmGfzju5L3ESPiobAsjmJ-lu-w6zb985Ue7Bq4EZER9kmEhZz01F3Q9bclfef9JzwMKeogqSqv8gj04orhhKxzuL9iq--LK34tepcBp7xJWjOJXmR4_RepIghQViMJgJjASL8YQEDcxn9iIrQxvqscM5Y4n7JLbC6CM9W9AAqobnSLijDL1p1kCFAT4VDmSIddUk_Wr_1rqy8JcpE8tl69Xw1xPGLiBZg05vNvJXMWa-0hJipqL0gWASRdqujI7TKSxVWz9OJO_IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی پویش جانفدا: در میان ثبت‌نام‌کنندگان افرادی هستن که اقامت آمریکا دارن!
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/72772" target="_blank">📅 15:32 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72771">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6bbcade1f.mp4?token=n4qNHRjgfnfZA2DnyqBE2HGmwCzCN-XOLZclniK4sa3vy43soLb3QnqJEQs2KppZ7d06cPS9yduDKYFFaUea27uNblZ6gRPptq-ipJJy_4P1MIcAljIqWtzNb0CFM8zMKrd1GW8Bnn6wQe_zFu7DAAbf6cAp55d9uYalWxxxwBaoJWmVF9s3PxrjEKc-nGj75dXpoffADGToNQC98p5J0844L_ZeFPisvlivGX8Sfnt-24MPy2EYpaM6rdltRYHIYI1VxpC9M5SvGhxyCDhaK-JE0md-vqw_EbExwgAayG-fawWw6menz4Jjku2gJ6hVeItbkbqmdMR_kh-DjxMygA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6bbcade1f.mp4?token=n4qNHRjgfnfZA2DnyqBE2HGmwCzCN-XOLZclniK4sa3vy43soLb3QnqJEQs2KppZ7d06cPS9yduDKYFFaUea27uNblZ6gRPptq-ipJJy_4P1MIcAljIqWtzNb0CFM8zMKrd1GW8Bnn6wQe_zFu7DAAbf6cAp55d9uYalWxxxwBaoJWmVF9s3PxrjEKc-nGj75dXpoffADGToNQC98p5J0844L_ZeFPisvlivGX8Sfnt-24MPy2EYpaM6rdltRYHIYI1VxpC9M5SvGhxyCDhaK-JE0md-vqw_EbExwgAayG-fawWw6menz4Jjku2gJ6hVeItbkbqmdMR_kh-DjxMygA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاظمی وزیر آموزش و پرورش:
ما در آموزش و پرورش تمام هم و غم خودمون رو به کار خواهیم گرفت تا اقامه نماز کنیم در تمام مدارس کشور بدون استثنا.
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/72771" target="_blank">📅 15:04 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72770">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/chwUH2q4FtEgV4Fb3_2H59nPx5O0cKdiHV1wsPgAqcSEOprwK6dQvEzCoAPjjDLKFGWYdTGHvd_YITwbGTJkuijPPIBIbcRUMls2goZGYoDdiGbk4VPgdde2tU2hxnRRHb1tf7WuvXk_i_a74TKzbOrYhgLHKPiq2kQluKAbq5JqdsiVny3Ryllr4zeslPdhZYxvpLaazKIggvrkpeJkj6WubwhWOUfyREeCEQazHwWqTbGKu6kCPbL8JAU7Zje3xkV1946zTjJ4soJdlwV4w-xB5cAEoAXGt-5aIV43E4oxIcYj3F5rDxAOaab5y6JnSRzDmIUpH3Cuv9YVA_Gvyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO):
یک نفتکش در فاصله ۱۱ مایل دریایی شمال «خصب» در عمان، از سوی سپاه پاسداران مورد خطاب قرار گرفت و به آن هشدار داده شد که در صورت عدم تغییر مسیر و بازگشت، هدف قرار خواهد گرفت.
نفتکش مذکور از این دستور پیروی کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/72770" target="_blank">📅 14:14 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72769">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CWxYpPNECRfLKLK-JkpsbfSVozUx1SQPkPxWpsb8h9HM5-K_mikGGG23x20F6pbkRTBul9TYJCxRStYqxJN4teAPhx6ujmvPslFnbsJiD3oHFGGPImv5JQeqgAe3PIBszVIGRYA22GdVvLAeruEyYDs1GXv8B26iqTdoE_27MRu7hNzgNLAdhYgLT9TbI2AwVhL0FY-eoXSJYAi1yHKFJoh2xenNugfraLGTJU5uG5Vhu7zHoVbWAxcHy-Z3Eas8aOzySmmeurx0WLySJW98H9178yeDrJrooCxDwba76oLrz4Td7_pDcnsUBn__OYAK80HfffkO8QeT-rgM-pppOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛
هشدار در روسیه؛ قرنطینه نزدیک به ۲۰۰ نفر پس از مرگ کارمند مؤسسه ضدطاعون؛
در پی مرگ یک کارمند ۲۸ ساله مؤسسه تحقیقات ضدطاعون در منطقه ایرکوتسک، حدود ۱۹۷ نفر از افراد در تماس با او تحت مراقبت قرار گرفته‌اند و برخی مراکز درمانی نیز محدودیت‌های قرنطینه‌ای اعمال کرده‌اند.
با وجود انتشار گزارش هایی درباره نشت طاعون از آزمایشگاه، مقام‌های روسیه تاکنون ابتلا به طاعون یا وقوع حادثه آزمایشگاهی را تأیید نکرده‌اند و علت مرگ را ذات‌الریه با علت نامشخص اعلام کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/72769" target="_blank">📅 13:58 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72768">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">یکی از طرفداران پروپاقرص رونالدو:)))
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/72768" target="_blank">📅 13:48 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72767">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">مسلمانان در انگلیس با برگزاری تجمعی خواستار حکومت اسلامی در این کشور شدند.
جمهوری اسلامی بریتانیا!
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/72767" target="_blank">📅 13:19 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72766">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abcebd0dcd.mp4?token=ES9TN1bGEK5_exO8cGq90XvxbwLKruhG5U1qCR1IJarZ3m2UMEfS65iwvIkJtquvJi-IkIf00-92b9U9YjTO-Ad4M8SA4on685RGfNEg5B8I_IwaeebaJln65W0Sc3FAx1vP6fcgeRIhGoELXyEHHD-VnSs9O8qTXemDSnMPAXCMouLZuB2_eyojCFnZChvgODzm7L3W_3hEYoEZ4_8v0OetI_k1Vj-lPuy3H-QoFQSuvmRN1M1asW4P4rTXW2_M6Uujn8-o8HLDL0ieXBD8fSqH1CRqc7QJdaobfge6AYXUVVUaWzz9SDnK880gmnpinutuM9eefndc6AjoK1c-OhX9H4vAJqj7rL63U09SAvNPbib6sGH3mzmGcCSR-FIr_fZmMUd_Xwl_ZbO5SteD6QMQSwR8oVVXv13sh8aRJM2n9e7xppg4U0e1FCkDcvucB65Ku5GnUNRxubNj1xNtJuN4xRZR-eUmvcB0WeKlf5jKQ01TpJ9H0Akqgov7-mAeZ3MvNAfP4jaAiVTqXF5Pco7BjIQuY6zDI1ElORvnWgjGP2Fs0KDONryDPEbqmQkPu1DNPYkIAMbfbFVM8Sb28SuhRBY7pXMEthWqZLMWKHfYowEmr4JeCiKc_1l3YIpsNTyH5JY6Tka09-GVBm6D0L3l2Y2yinCKg_T3ZmDUA1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abcebd0dcd.mp4?token=ES9TN1bGEK5_exO8cGq90XvxbwLKruhG5U1qCR1IJarZ3m2UMEfS65iwvIkJtquvJi-IkIf00-92b9U9YjTO-Ad4M8SA4on685RGfNEg5B8I_IwaeebaJln65W0Sc3FAx1vP6fcgeRIhGoELXyEHHD-VnSs9O8qTXemDSnMPAXCMouLZuB2_eyojCFnZChvgODzm7L3W_3hEYoEZ4_8v0OetI_k1Vj-lPuy3H-QoFQSuvmRN1M1asW4P4rTXW2_M6Uujn8-o8HLDL0ieXBD8fSqH1CRqc7QJdaobfge6AYXUVVUaWzz9SDnK880gmnpinutuM9eefndc6AjoK1c-OhX9H4vAJqj7rL63U09SAvNPbib6sGH3mzmGcCSR-FIr_fZmMUd_Xwl_ZbO5SteD6QMQSwR8oVVXv13sh8aRJM2n9e7xppg4U0e1FCkDcvucB65Ku5GnUNRxubNj1xNtJuN4xRZR-eUmvcB0WeKlf5jKQ01TpJ9H0Akqgov7-mAeZ3MvNAfP4jaAiVTqXF5Pco7BjIQuY6zDI1ElORvnWgjGP2Fs0KDONryDPEbqmQkPu1DNPYkIAMbfbFVM8Sb28SuhRBY7pXMEthWqZLMWKHfYowEmr4JeCiKc_1l3YIpsNTyH5JY6Tka09-GVBm6D0L3l2Y2yinCKg_T3ZmDUA1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروهای دولتی یمن مورد حمایت عربستان سعودی اعلام کردند که کنترل تنگه باب‌المندب را به دست گرفته‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/72766" target="_blank">📅 12:42 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72765">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N7zBafQ6AX_eG409viOk0OSmwVHsKyU52sSKA97wSWa_5jniIeDqEZStm58iTRYzh3guqan_OYeWT6OnT3dCbBU96eqSGV1JMG8oxS-HBkWUq5q-1PrM0fa23Y01rCUdwGUY5vIZ-5PZTs8I2tQjnEt5X5CTLl2iJZOX1KuVKullQqznKiImgKntdKmlwXQrQcjrbCqUdHN3NxAo5MHWJ0AHgtcZSGyiZPpKKk4AhOW8HbRXIavenFTSIFVRrJyKt08qL_k6uCYrtVI4f5whKWdhICQXdwTmgadI0pmWqsKAru9_bvM5tOnTyU2e4Uea26umSZjfS6WI_zdKK-prTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علیرضا سپاهی به انفرادی منتقل شد؛ نگرانی از اجرای قریب‌الوقوع حکم اعدام</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/72765" target="_blank">📅 11:53 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72761">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e88e1de928.mp4?token=EbuduhHrGz_KyXZJaorsAls1DkG4lhO1Xn-m2gm8L7hKX4fryFLyB52QP2HyT6vubw9sIRfOCv-aa35nCzdGiauOVjT3nVWKPJM_P26BP2ZrcZsoWEd0ZORITpsLvAB3UJE1-ecmnVBT77SkS15kojo_k3fF_mwnSeCIDbYDGMS815w9A0qYbNkyy8ZGWnucN2ByyU76c5kLjeuqstOBGEcPNJfu4QR7Y7Fdhvy2BVD-0jAPq7wmyPEw3G7Idaatv6xfQzQHQ5lgu_go_R9PdkM9sqp8wWXFp519wRESZiiP3kvPH_7WxCH0MCco1MADxBb8nMUq7CwZT0KkUwY8qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e88e1de928.mp4?token=EbuduhHrGz_KyXZJaorsAls1DkG4lhO1Xn-m2gm8L7hKX4fryFLyB52QP2HyT6vubw9sIRfOCv-aa35nCzdGiauOVjT3nVWKPJM_P26BP2ZrcZsoWEd0ZORITpsLvAB3UJE1-ecmnVBT77SkS15kojo_k3fF_mwnSeCIDbYDGMS815w9A0qYbNkyy8ZGWnucN2ByyU76c5kLjeuqstOBGEcPNJfu4QR7Y7Fdhvy2BVD-0jAPq7wmyPEw3G7Idaatv6xfQzQHQ5lgu_go_R9PdkM9sqp8wWXFp519wRESZiiP3kvPH_7WxCH0MCco1MADxBb8nMUq7CwZT0KkUwY8qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت خیابان های فرانسه پس از اعتراضات گسترده دانش‌آموزان و دانشجویان به دلیل کمبود معلم و وضعیت بد مدارس
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/72761" target="_blank">📅 11:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72760">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72760" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/72760" target="_blank">📅 11:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72759">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oy2VZ6EHa48LKBtRlFTPc84wkhoWABqXtK3QIrQn7lLDKkn1-4JS5lMN1q9PVu8NpUyn3-_tSk7xxVhweDQXZJNx6UnZ87G9nXxlOL5bC7CZ6FXiztMMG0LcRScVfRYb7fMAq08BZI_lq7M6z5bGkZsGbo_Q5SQFPexpr3S8bsKiZsgJEGLUMEBT4WslO2pbFHozYHTlhFUVj_0tBU0CSYsNbZmEoDRrWWgNIFn_mY78yJF6yXBUPRh6J75wlEoQHybECICJw2LN3Jb8aWfM1H8tpOmpBTylIsRUTDImbp7bjqgsuZUtAKMZRhWNzyT8yw7IM5ACEICe_A6_rwbFKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
بلژیک
🆚
فرانسه
ترکیه
🆚
ایتالیا
لهستان
🆚
بوسنی
سوئد
🆚
رومانی
نیوزیلند
🆚
ژاپن
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
http://T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/72759" target="_blank">📅 11:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72758">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e436b8c05.mp4?token=g9hOdj-r-KH9UrpYsuDHnT2CvN7tkp4EYrizgVu6sxxrr2BL6zwaUQmilHLAqKEBtNOYINrSfQwELQ2INRwGQ7RDtcZqjZK82E7oMEi_Uu1kghObKgWJVt0gCQkjmuekT23XckAqhuGmJNnQkGNOnqNKJ8o6J6C2aS1L2FuTfcu62v3Bea2-C4MMgbwM28lAGdGXV1UyrrsSnzjqM4ZwbkeDWi8NCfh2qIt5HMFFQTw7oRtq5kUIJocapwp9aFTfo2NmzHoH4HMvaaaGP__0GYspxN6r5aDNkCNTDkT1975pjkS0s3pqxPLgtFk-wjwJ9_ncECuO6xJe0ueYRCjE2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e436b8c05.mp4?token=g9hOdj-r-KH9UrpYsuDHnT2CvN7tkp4EYrizgVu6sxxrr2BL6zwaUQmilHLAqKEBtNOYINrSfQwELQ2INRwGQ7RDtcZqjZK82E7oMEi_Uu1kghObKgWJVt0gCQkjmuekT23XckAqhuGmJNnQkGNOnqNKJ8o6J6C2aS1L2FuTfcu62v3Bea2-C4MMgbwM28lAGdGXV1UyrrsSnzjqM4ZwbkeDWi8NCfh2qIt5HMFFQTw7oRtq5kUIJocapwp9aFTfo2NmzHoH4HMvaaaGP__0GYspxN6r5aDNkCNTDkT1975pjkS0s3pqxPLgtFk-wjwJ9_ncECuO6xJe0ueYRCjE2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مراد ویسی:
جنگی که توی راهه، آخرین جنگ ترامپ با جمهوری اسلامی خواهد بود!
اما به قدری این جنگ شدید و گسترده‌اس، که جنگ ۱۲ و ۴۰ روزه، پیشش یه شوخیه!
شدت بمبارون‌ها خیلی شدیدتر خواهد بود، کشورای بیشتری درگیر میشن و این نبرد آخره!
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/72758" target="_blank">📅 11:06 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72757">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cf7a6e5830.mp4?token=M63rcixEVrWcV2jjlFRtcv60P-PC0eMFG51AwGLZzzyBf9bB2B-vBj7DRDmdiVGnLsl9o-Uy0ohKX16bxPXu1eazeK12jH6GmQe7IeUJzBxULrEHcewBn85tVKLrPulW6F8I_KXZeN-GmJaNXVm1suDsMv8tePkVGz3lwVxDOYez2uHZQGuBDX3XPJg9Gf2il50JRxDzaJAfS_vC3mji39l-VsGlYgzAyxXVJ5DlboBKKhomKfAMETGLUVSFbMZc7AhqNvQxqmPfGRIHMQlKLr-OQbRcMbmmYmzLm6V0CHYL0g8sdyYwkM4PjDSeK2inF0FmXj4sEtmLm49LuVVdwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cf7a6e5830.mp4?token=M63rcixEVrWcV2jjlFRtcv60P-PC0eMFG51AwGLZzzyBf9bB2B-vBj7DRDmdiVGnLsl9o-Uy0ohKX16bxPXu1eazeK12jH6GmQe7IeUJzBxULrEHcewBn85tVKLrPulW6F8I_KXZeN-GmJaNXVm1suDsMv8tePkVGz3lwVxDOYez2uHZQGuBDX3XPJg9Gf2il50JRxDzaJAfS_vC3mji39l-VsGlYgzAyxXVJ5DlboBKKhomKfAMETGLUVSFbMZc7AhqNvQxqmPfGRIHMQlKLr-OQbRcMbmmYmzLm6V0CHYL0g8sdyYwkM4PjDSeK2inF0FmXj4sEtmLm49LuVVdwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاطره یه دختر تن فروش: یه دفعه یه سید بهم گفت بیا رابطه داشته باشیم، فقط تو زود بیا چون ممکنه خانمم بیاد خونه.
رفتیم تو اتاق و شروع کرد صیغه خوندن، هر چی قرآن، آیت الکرسی، تابلو و کتاب دعا بود برعکس کرد و گفت زشته، گناه داره.
یه دفعه وسط عملیات زنش اومد، گفت سید زودباش درو باز کن خیس شدم زیر بارون، سیدم بهم گفت تو فقط چادر بنداز سرت شروع کن نماز خوندن.
خانمش اومد به سید گفت این کیه؟ برگشت گفت این خانم مسافر بود، اومد گفت نمازم داره قضا میشه، میتونم خونه شما بخونم؟ منم آوردمش نماز بخونه.
آخرشم خانمش بهم چایی داد و کلی پذیرایی کرد و رفتم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72757" target="_blank">📅 10:30 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72756">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de6e0dfa99.mp4?token=dYZY7ljjKsAbVn8VvD1dKBDFgZ4hQkA23GMd2L07sjy1ERcRB24_ATDK6KpvRiCihZuP0wUYiipuKiyPHcGA9ojmupaaXKnar1aEVtSt3XLhHzD4nshzBoi3xIelYQrod0EKerG9QHNW8q02WTznonLsSuQ0dmpr1cvR-J1WyUX5DbTNSb-kJjqhgGTkscwBPSdqTWSRWIha5RCJdS7OHmkoyTuMtpB-YmlBmxaVrHROlfc2Y0RjXHda5838eGzmlpkvvHTTDi2w2tu_QlsXEJ2mBKClr00ibzdXDKbJtJRbBPls6HRPA372407duEmwrXe6e5kW1rqJidsgAi2vuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de6e0dfa99.mp4?token=dYZY7ljjKsAbVn8VvD1dKBDFgZ4hQkA23GMd2L07sjy1ERcRB24_ATDK6KpvRiCihZuP0wUYiipuKiyPHcGA9ojmupaaXKnar1aEVtSt3XLhHzD4nshzBoi3xIelYQrod0EKerG9QHNW8q02WTznonLsSuQ0dmpr1cvR-J1WyUX5DbTNSb-kJjqhgGTkscwBPSdqTWSRWIha5RCJdS7OHmkoyTuMtpB-YmlBmxaVrHROlfc2Y0RjXHda5838eGzmlpkvvHTTDi2w2tu_QlsXEJ2mBKClr00ibzdXDKbJtJRbBPls6HRPA372407duEmwrXe6e5kW1rqJidsgAi2vuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو وایرال شده از یه عراقی :
به حضرت عباس اگه بگن بین پسرات و جمهوری اسلامی یکیو حذف کن میگم بچه هامو حذف کنید تا فدای جمهوری اسلامی بشن
ایران از بچه هامم ارزش بیشتری داره
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/72756" target="_blank">📅 10:01 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72755">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aaee08d663.mp4?token=Eu2nEPSnLaqeu2SLg5Qyz3GAW6uYKvkXZwEyJxGRylR31P3SiOEuspSqqFozPbVC1rd6Z-tNaIcMtx4gP93lJu9u1f0JmdnBYRzgpV8ct7J6O1cPob39uuIP43m3yCBWbuyrnhQFERpIb-WNRIvJzMrnZ0NnhOMKqPw0YY0pw_IglggBXwAg1GuPGHNNMAWdb2ILZIypE6L4_ELirxsSqRuulQnfJ-6kpva6GqSgC7dKbjBf8sEiQPh7fAnDKnEGNq9sf4wFOMeLFhHb-z7u5aQT3TYgRd1PtiPLGiYqgjhQ30zkl0gq31wN9wgWj9E3FfstqB-2_6OMi5nleht7FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aaee08d663.mp4?token=Eu2nEPSnLaqeu2SLg5Qyz3GAW6uYKvkXZwEyJxGRylR31P3SiOEuspSqqFozPbVC1rd6Z-tNaIcMtx4gP93lJu9u1f0JmdnBYRzgpV8ct7J6O1cPob39uuIP43m3yCBWbuyrnhQFERpIb-WNRIvJzMrnZ0NnhOMKqPw0YY0pw_IglggBXwAg1GuPGHNNMAWdb2ILZIypE6L4_ELirxsSqRuulQnfJ-6kpva6GqSgC7dKbjBf8sEiQPh7fAnDKnEGNq9sf4wFOMeLFhHb-z7u5aQT3TYgRd1PtiPLGiYqgjhQ30zkl0gq31wN9wgWj9E3FfstqB-2_6OMi5nleht7FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار :
از آقا مجتبی (خامنه‌ای) چخبر؟
حداد عادل پدر زنِ مجتبی خامنه‌ای :
سلام میرسونن...انشاالله خوبن...همیشه...خوبن الحمدالله
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72755" target="_blank">📅 09:32 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72754">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32e173a359.mp4?token=JxluhMZLxVMHeI5rjSmfIkHXqv1Iah_cla1E6YIkzzWIDfTnO2yoamCW7Snm4YxJhxHWU17Q4pQmWSW80y4wJtdIeoViGn9RV0FpVs2mu2ROyUyBMUqBuZxyqD8EhCvhaXAs_7gMCxiGo0l3bJY4xPFkUB26VqVEbq_DGcvsvk0GUKfwI0PcjqHgw6gRawSvm0rgkbu2u-06-emixlAHuURc4K-CCVnudDHbzPdBekCwycEw634nriqkldneJqvQarz9riwqx9dhrAzjV8dZPrJOeXT9gJOLMyC7bpNQoBi_wgVrXyMXZDBEp1UI6Hw4JqlLR76gKjDbCjin2GJArQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32e173a359.mp4?token=JxluhMZLxVMHeI5rjSmfIkHXqv1Iah_cla1E6YIkzzWIDfTnO2yoamCW7Snm4YxJhxHWU17Q4pQmWSW80y4wJtdIeoViGn9RV0FpVs2mu2ROyUyBMUqBuZxyqD8EhCvhaXAs_7gMCxiGo0l3bJY4xPFkUB26VqVEbq_DGcvsvk0GUKfwI0PcjqHgw6gRawSvm0rgkbu2u-06-emixlAHuURc4K-CCVnudDHbzPdBekCwycEw634nriqkldneJqvQarz9riwqx9dhrAzjV8dZPrJOeXT9gJOLMyC7bpNQoBi_wgVrXyMXZDBEp1UI6Hw4JqlLR76gKjDbCjin2GJArQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در حاشیه ختم خواهر عباس عراقچی، وزیر اقتصاد از پاسخگویی درباره وضعیت فروپاشی اقتصادی و کاهش ارزش ریال فرار کرد و خبرنگاران را به همتی، رئیس بانک مرکزی، حواله داد و همتی هم بدون پاسخگویی فرار کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/72754" target="_blank">📅 09:02 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72753">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72753" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/72753" target="_blank">📅 01:41 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72752">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MEk0NL9jPB5wBxa8VGQBd7KmpFxuPyEZWu-0JmI_CF-hY6XsmwiwTdOgQKlj2Nm1mxkH2OJAKTHKNYh1WisJdB-wys79f9D3JhXNfX0btbWKrTT7KEr-wLYvs_XC2OeNM13nLUC88g63e8YXD3PQebVwyiQ7gYDLVLGZg9YXauNoIpkux-Pb6Uh7kxYwOJM3OuXTm0uTIo46LYT5rQIy7b7qU43MHrKT_XjDBljAxiUN0I3EhBlNf-gTMISThkU2SVeX-FsPqX-nwANU9HiKitqLmZvplOZgtuNxqwa_oVN0TsHZdBQ49o9cMLlSAWj97mNN_TblMO83us05Acj1Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول: ۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم: ۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم: ۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم: ۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/72752" target="_blank">📅 01:41 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72751">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MY3t79AO46dQLVpoStj5UJvn26ZLsd03k89a09KWInga4FHzoPLQwD4HTI6Xftkb0QGadFIq7pfNpzpd5RrUeuiRN8-IpNRdey1JuWX5kpmFKXfINL6qoUF1REgxKw2m9POVsvtl2UFb8ZxkVpvInWUyI1wHSxZY7_qzPorYdHWPZQynw5MEjPmbxpoN-YlQYk0aFAum1nUnBILglOLnmTWDDGd0mF9b1imbZrxVhRJx8gbNWH3vOH50b-mYIscba8DAeeirAe52OxoKNxAkx0xHgCqsRLuHTu1laBimzoSNbQGzjqAhDkp0xJrLcilY_Gr35_CsJiP9TQkJEz5OLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وال‌استریت ژورنال به نقل از مقامات آمریکایی گزارش داد که بمب‌افکن‌های راهبردی «بی-۱بی لنسر» (B-1B Lancer) در حال خروج از پایگاه نیروی هوایی سلطنتی بریتانیا در «فِیرفورد» (RAF Fairford) هستند؛ این اقدام به دلیل نگرانی‌های امنیتی و در پی دریافت اطلاعاتی مبنی بر وجود طرحی از سوی ایران برای حمله به این بمب‌افکن‌ها در پایگاه مذکور و کشتن کارکنان آن صورت می‌گیرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72751" target="_blank">📅 01:32 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72749">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GvLvvfo-u5wTWMqExJswkCNY5bFDKxhmnaPdzaeYQu8axYz2zx1InIrQRfh6XPW9ATaiW3PDLEX3OJy-lDQPblXO5HRXjtXzVCzBzg-7FoBpRfpVMkiXFVd-gWVmIKCmu1GsnvqA7XG2RJqTf7rk9JnbPsTx0S2Nxm2m0RdqOX6glP3mmM3F2a60uK3MrEtTZFK0Pp31ceKo9q7P5KSQz6r9g-pXa9VxPcQ1keXeZWxGZuXOA1yb4syCGAYZpZs0sUEFSy7NZ8Kj81phJ2Bgaq1ams-AqWJKrNcJFtFq5aYq6jYcAwokvoStfO0x5hudDSQlOugGhkLJqlMrUwtcZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5cef955dd4.mp4?token=k0XHTzx5mYB2lmriUWEhwUm1PPpg1s1y7K_yLeHF1T9Drj5YM7r3iHbDScUU2D2u31S_7M8HKozOjaQcG8KiYF-rB1Z0_2JDys-cmqFtaQIt9CW9EI8FC78BLNqHrEAUsgwQy2pI6gFrGD-yuRPrLafEYGzTFI4i2MV34DC5hB1e0uQJsrotBHqUxJ4Co0T4KtWB8jaR8WTlO04WqoAccCpkk373dz95aKK3BSZzkUsOmKXyqxR4jE33j8hoAXmt4lUyqM_YE7qcYdml4lzNwunT9WudQg2yRsb8GlsxTd_eyILNjaMeYKFEESsHyf8rHbTBpv0rmle8rpc4l0QY9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5cef955dd4.mp4?token=k0XHTzx5mYB2lmriUWEhwUm1PPpg1s1y7K_yLeHF1T9Drj5YM7r3iHbDScUU2D2u31S_7M8HKozOjaQcG8KiYF-rB1Z0_2JDys-cmqFtaQIt9CW9EI8FC78BLNqHrEAUsgwQy2pI6gFrGD-yuRPrLafEYGzTFI4i2MV34DC5hB1e0uQJsrotBHqUxJ4Co0T4KtWB8jaR8WTlO04WqoAccCpkk373dz95aKK3BSZzkUsOmKXyqxR4jE33j8hoAXmt4lUyqM_YE7qcYdml4lzNwunT9WudQg2yRsb8GlsxTd_eyILNjaMeYKFEESsHyf8rHbTBpv0rmle8rpc4l0QY9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علیرضا سپاهی به انفرادی منتقل شد؛ نگرانی از اجرای قریب‌الوقوع حکم اعدام
علیرضا سپاهی، از معترضان بازداشت‌شده در جریان اعتراضات دی‌ماه ۱۴۰۴(پرونده میدان علیخانی اصفهان)، به سلول انفرادی زندان دستگرد اصفهان منتقل شده و خانواده او برای آخرین ملاقات فراخوانده شده‌اند.
وکیل علیرضا سپاهی نیز انتقال موکلش به انفرادی و اطلاع خانواده برای آخرین ملاقات را تأیید کرده است.
بر اساس گزارش ها دختری که عاشق علیرضا بوده گفته آرزو دارم باهاش ازدواج کنم و امشب در زندان خطبه عقدشون تلفنی خونده شده
💔
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/72749" target="_blank">📅 01:04 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72748">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RLVIRV-0tkqgKCapL03_eT7EbLbT1s7dTP8tonl_Y7EyGMZYs67Pt64S06zpgATO0yvcwBOsfr50xg1Qd8QObbVT8F-sLk0IE8UbDt-5nQWcBcVZH2_R6-FYQLJqk6BQk7qoPdjih-JZcYKxM6ejBUEdECpbPLpiUb4vd2P0RJa9ey8Pc6o51ODB-vNMz3sdeNCU45onSOk7O3sNiFjhex4V9ng4vjOqy9N6oy0h0AGmGfEAnYfizMorhWCCAXQqBKiz9dc_kEpNIS5yBDJMzgode8hgk1IPZP87swMmDIl5vvCFSo0yL90XaAUT3RNlbyy-iFfNtgORSf2sh8z5NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید صفحه یوتیوب امیر تتلو:
امروز دادستان و رئیس کل دادگستری صحبت‌های خوبی با تتلو داشتن و اگه گزارش خوبی هم رد کنن، امیرتتلو فردا آزاد میشه و به استقبالش میریم!
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72748" target="_blank">📅 00:46 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72747">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">۱۰فروند از ۱۲ بمب‌افکن راهبردی B-1B Lancer نیروی هوایی ایالات متحده که در پایگاه «آر.ای.اف فیرفورد» (RAF Fairford) انگلستان مستقر بودند، در حال ترک این پایگاه و بازگشت به خاک اصلی آمریکا هستند. انتظار می‌رود دو فروند باقی‌مانده نیز امروز این پایگاه را ترک…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/72747" target="_blank">📅 00:37 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72746">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec28377bbb.mp4?token=PpNL154UV1JUDgHXv0ool0F6lGxlwjeCv3osYnexhcCfprD7-85Ero6_F2hWrAUli6oTM5GpseC2Xfrd6kWOME0zIP2jXI5nwkA9YjXeQq4cpqan02dQcWjZpXFutjghql_oV_va0_i6qCY-p_lA_xrIPVixZC6Sfwl94r0nLWlPkjWMU0lROTY9MlaIs8xT_Hl2TdWgstAJG_jZ027qFbT_dQaCizK_Z6GHb8ocuWckCKRoGnv0daSgN3GK4aQa5quA-9b2V6uzHF7p2PByXCrGUP17rxbZ39FFqoSGZJA3S8gm3a8AvPiTwxM6ehftP5LiF1rv8A2wmxxNf-2mcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec28377bbb.mp4?token=PpNL154UV1JUDgHXv0ool0F6lGxlwjeCv3osYnexhcCfprD7-85Ero6_F2hWrAUli6oTM5GpseC2Xfrd6kWOME0zIP2jXI5nwkA9YjXeQq4cpqan02dQcWjZpXFutjghql_oV_va0_i6qCY-p_lA_xrIPVixZC6Sfwl94r0nLWlPkjWMU0lROTY9MlaIs8xT_Hl2TdWgstAJG_jZ027qFbT_dQaCizK_Z6GHb8ocuWckCKRoGnv0daSgN3GK4aQa5quA-9b2V6uzHF7p2PByXCrGUP17rxbZ39FFqoSGZJA3S8gm3a8AvPiTwxM6ehftP5LiF1rv8A2wmxxNf-2mcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ادعای عجیب در تجمعات شبانه: حسن روحانی در یک سفر استانی دستور داد برای دستشویی‌اش کولر نصب کنند!
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/72746" target="_blank">📅 23:33 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72745">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7673e09822.mp4?token=bNbZhwHC45L1TiJGzLu_cqu9TI3o8vqpKVMmO5F6K-4ORU82NmyHV5JaQ4yyLu8-R-rLdP8lqELGiuCyDK2__jU1Cjs62d2_EZ1l5LDi2yF5teYJ5sT1IsL8VRsIc2ZaWrwE2eMv55hrU22mSn3X-aQCXQd579h8dutVj9bxmMoBmvsBD-EsmWP4lHRaZEtdwRTfiFq-G5o3fGJAhFW97qFcb48CKHcCM4jCvbhEG4WB8LTOeXqcJjEOy3XMgHBgAXgsW9aePx0I58HlFny7luQNETgwutcx2qEzM9XknRokSggx2q2mV0VdDpR6EOV-sVObIE-wS5_v3TivCyaG2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7673e09822.mp4?token=bNbZhwHC45L1TiJGzLu_cqu9TI3o8vqpKVMmO5F6K-4ORU82NmyHV5JaQ4yyLu8-R-rLdP8lqELGiuCyDK2__jU1Cjs62d2_EZ1l5LDi2yF5teYJ5sT1IsL8VRsIc2ZaWrwE2eMv55hrU22mSn3X-aQCXQd579h8dutVj9bxmMoBmvsBD-EsmWP4lHRaZEtdwRTfiFq-G5o3fGJAhFW97qFcb48CKHcCM4jCvbhEG4WB8LTOeXqcJjEOy3XMgHBgAXgsW9aePx0I58HlFny7luQNETgwutcx2qEzM9XknRokSggx2q2mV0VdDpR6EOV-sVObIE-wS5_v3TivCyaG2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سیل اخیرِ گرگان، یه
موش
برای اینکه جونشو نجات بده، این شکلی داشت تلاش می‌کرد...!
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/72745" target="_blank">📅 23:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72744">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bffb33370b.mp4?token=MEJEPqLoxYsWoGn99EoqLFrIu995HuFPS0ErusrMdzt31TVM66jq5O-w6rj_7qWa7nHaV7XIt8bcvtm8fQfZBnHYyPZiO_3dRa_eush0vY4mXkdQaQ1TLfS9i-JV_hf9_PAAEGV4vuCc183Avr1dU9d5pjIHE4vM6a0uLNN1eAi0KEL6BUoIGRJv0ikzCIfCeABhOW0YxLsKOSCek3iVtoATWMadSVGuCq_ObFXE3rXEjzqav5fHRjDwLzYDAebFcAOxONTOFDzdARVmZO6BPNBCvk7n9qNFRB03ZnShSpmt4sS9A6Xx5EOxl-hTDlVBLvMK0TkA-makNyOMKhCKow3M72cF4HnqZkEmmstDnCkmG5h8sW1FhtEYgg_QI1SGoaK6QDzZU04l_MTx74XKFj3nPtuuWK9YS9wZL8hKCqjB6kSeYUfhwb3k-SLnSA9N-4Qjn_3gHqSGLHu7ltfX0_f48IUM2yCvg5hPwY5gi0Ced1M9AMcDzeRO29vrAC_DxdcQRv2q3pLGeW6mdkDApUYZ6VNdEq9J6v3RLO2YjuyAKi0D5DDTROJ-yHzOzgHFCZRyVkAgioWuNdgUNpprwqad7wyOLJQ3yVWSdK88SWq_gTO9HhdjBI_sbNCgDIwfK9ziaISW_tFIUAJ-WPU_kZzROG-yxuTWuLnVLqb2d7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bffb33370b.mp4?token=MEJEPqLoxYsWoGn99EoqLFrIu995HuFPS0ErusrMdzt31TVM66jq5O-w6rj_7qWa7nHaV7XIt8bcvtm8fQfZBnHYyPZiO_3dRa_eush0vY4mXkdQaQ1TLfS9i-JV_hf9_PAAEGV4vuCc183Avr1dU9d5pjIHE4vM6a0uLNN1eAi0KEL6BUoIGRJv0ikzCIfCeABhOW0YxLsKOSCek3iVtoATWMadSVGuCq_ObFXE3rXEjzqav5fHRjDwLzYDAebFcAOxONTOFDzdARVmZO6BPNBCvk7n9qNFRB03ZnShSpmt4sS9A6Xx5EOxl-hTDlVBLvMK0TkA-makNyOMKhCKow3M72cF4HnqZkEmmstDnCkmG5h8sW1FhtEYgg_QI1SGoaK6QDzZU04l_MTx74XKFj3nPtuuWK9YS9wZL8hKCqjB6kSeYUfhwb3k-SLnSA9N-4Qjn_3gHqSGLHu7ltfX0_f48IUM2yCvg5hPwY5gi0Ced1M9AMcDzeRO29vrAC_DxdcQRv2q3pLGeW6mdkDApUYZ6VNdEq9J6v3RLO2YjuyAKi0D5DDTROJ-yHzOzgHFCZRyVkAgioWuNdgUNpprwqad7wyOLJQ3yVWSdK88SWq_gTO9HhdjBI_sbNCgDIwfK9ziaISW_tFIUAJ-WPU_kZzROG-yxuTWuLnVLqb2d7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیرک جانفدایان در اصفهان، سازماندهی اراذل و اوباش با قمه و شمشیر و چاقو!!
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/72744" target="_blank">📅 22:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72743">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cB6s069vapNfkG0sVV2N9ZuKcwWxGUCpC6C7zspg8T7r4QGycvsTvfrpUVS9Wc3v3MUwoJUDwrM3FMrKiR8YhO7K_AzVkSqcg-vPszvcyknzJ6cUMyiqzSe-MGHidpL97XeXv6iEvk0SGpXvEFhHGdqyywIOs2uwQjguo1YFL1b7IFwFXteiBN2y0eM7foFAOR3YvT1SscLzZgRjhBW__7ZoxS3u5hqebG8sNVHtmVCZpb-jVUPx-HkrVKn_3xLbhJ0t7Ig_Tt6Gjs_WJhguYktRKNezdYORSgzeMmD1wIuPVwZ_8nzbQZkt07W7XPMrQMyYxNkhu6qy9VoBOClp3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ تصویری از خود به همراه پنگوئن‌ها در گرینلند منتشر کرد.
پنگوئن‌ها در گرینلند زندگی نمی‌کنند
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/72743" target="_blank">📅 21:36 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72742">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">شنیده شدن صدای انفجار در جزیره قشم   @News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/72742" target="_blank">📅 21:03 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72741">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">شنیده شدن صدای انفجار در جزیره قشم
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/72741" target="_blank">📅 21:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72740">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d25df363a1.mp4?token=GhA13tQnLq3eNvBP0SSOzPT9o1Hx-p2T2eS6gql357U5oz3hmsuVWhxURW0qDIuScRqkSPUTHDW6nge_D2h9gkvcAJSci0j8vhQfUk-tmR71P7YPuYa-Pc2chJ_wat7JtX-bQT3pqmBbZK3NxsfgRUbXue0R2ndzTVsgOsN7MDb8mCPy0jPhiDx0P7yWY48gnK0hAK6DRGh4tIvI3QHspyi3sAcMFxULd7RSE3EqeH5x0heTd1ULRyNwp3_A_ieZqWn-PpTYDVnyyRGjv24rd0bzq6tzwR_tG6tud6r9MstfByhYgcvm-hFCa5VUkUYv1Ua4Jqcv_sF-_nJyjyF10A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d25df363a1.mp4?token=GhA13tQnLq3eNvBP0SSOzPT9o1Hx-p2T2eS6gql357U5oz3hmsuVWhxURW0qDIuScRqkSPUTHDW6nge_D2h9gkvcAJSci0j8vhQfUk-tmR71P7YPuYa-Pc2chJ_wat7JtX-bQT3pqmBbZK3NxsfgRUbXue0R2ndzTVsgOsN7MDb8mCPy0jPhiDx0P7yWY48gnK0hAK6DRGh4tIvI3QHspyi3sAcMFxULd7RSE3EqeH5x0heTd1ULRyNwp3_A_ieZqWn-PpTYDVnyyRGjv24rd0bzq6tzwR_tG6tud6r9MstfByhYgcvm-hFCa5VUkUYv1Ua4Jqcv_sF-_nJyjyF10A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۱۰فروند از ۱۲ بمب‌افکن راهبردی B-1B Lancer نیروی هوایی ایالات متحده که در پایگاه «آر.ای.اف فیرفورد» (RAF Fairford) انگلستان مستقر بودند، در حال ترک این پایگاه و بازگشت به خاک اصلی آمریکا هستند. انتظار می‌رود دو فروند باقی‌مانده نیز امروز این پایگاه را ترک کنند؛ بدین ترتیب، دیگر هیچ بمب‌افکن راهبردی‌ای در «آر.ای.اف فیرفورد» حضور نخواهد داشت.
پنیک نکنید!
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/72740" target="_blank">📅 20:59 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72739">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PDiqPx5qTi6WIAG4Z30XAvW0qaKqr4i-ob7VbBIRcCRqKwewg3s4kk3hHqe-zjTx9r6iOA2o2aQDQ-g8cUTkLh9-EfpABK6ksOkGfnWstg3UbWc6ORazdHwZX_iRFjtbGvXqszrAfHypMAzQbPvijN5Z1TUK2MEsSV7PmIsULvlkVYhj5iVtwydw1ZTnJSii9_3vTuUklOKi5vys63OcKKw9tcLbKNHfzamYks3L6D6Fb9qIK5YODxiVSZB866XiLs2WLz7UcCe2O8AekInizCVACrW8OEHHimmDkeKb3Ja29LHY2MFW1g0zwpMkcVMQULfc2X-Th13ipduHmEnPyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛محسن پاک‌نژاد، وزیر نفت جمهوری اسلامی، استعفا داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/72739" target="_blank">📅 20:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72736">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1dad032a8.mp4?token=Auu9gaK3fiptykzef35-xVmrGpUGqyct-lJ7wajacyp0VvP453xcrzaGi8hAlmm1xS4v_znkgMAG2YWhyDW0E1qenAW7xPFik2UtGiNdlAnDgQW70mT8_8GDwRNgcFP2rHlseyBj51wIRRpgAOp3M9b-YJZRMG7G9Hp9o0DpAxKAkXH37GyEjaeV3SMXAkq20B5BRIH9SSc_jZiQzbcFwsBCweFIykNgOc3DvYJzGuyHk7AieSGvhmeDjBdHJUx9ZCF8fJ5Sp9rqnzqjBSg8Hwmc85Fb3YP5Yfl3BCIi-KikPhfVJwx7m6CDXYqcwkmXPTqqS_KchW0SpdFMpJTpbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1dad032a8.mp4?token=Auu9gaK3fiptykzef35-xVmrGpUGqyct-lJ7wajacyp0VvP453xcrzaGi8hAlmm1xS4v_znkgMAG2YWhyDW0E1qenAW7xPFik2UtGiNdlAnDgQW70mT8_8GDwRNgcFP2rHlseyBj51wIRRpgAOp3M9b-YJZRMG7G9Hp9o0DpAxKAkXH37GyEjaeV3SMXAkq20B5BRIH9SSc_jZiQzbcFwsBCweFIykNgOc3DvYJzGuyHk7AieSGvhmeDjBdHJUx9ZCF8fJ5Sp9rqnzqjBSg8Hwmc85Fb3YP5Yfl3BCIi-KikPhfVJwx7m6CDXYqcwkmXPTqqS_KchW0SpdFMpJTpbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رتبه یک کنکور تجربی همین‌جوری داره بین موسسه‌های کنکوری دست به دست میشه و تو همشون میگه که من از بچگی اینجا بودم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/72736" target="_blank">📅 20:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72735">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/112f06092b.mp4?token=aLSq3-monHuHXEztNh02HYJiOBQF4kXe_zEhwH_DGCB9Rx7b1rLKEapE1omAhuCTDC0zQe9N2ILg5klWwtnC-3bQfw3SlmIMTMrV0cBK1V9XTmz4_mjWnIh9mM9Ratc2c2GR5dGHLLAnfJ-eIKXVvnWfYmnzpp6tbzz8zkkg191vg_Th0LRLQjzMpXjLW1HgYNIlkoui9ygSHgWKq_7ev7YtwUIZ53lu8Z31QTkjpPMPNmI7kZCv5bkXb3_s70N8EQGwnbo18mWxttLG2Kkf6gBjrU9GlHt52R1S1qzEfulZFsTh-TznTQJMxLqSkeHQqOQlsmLFkzpWtYf-4eOK83N8Dqapgt-JntKD-NfvYgg3i1sAtFp6YH8G31jkquchd0wu99OP0l8PNvHmfaRHm8g-zsN0Wn0A087fzdfRXWZcbWROOTM8PnMa_L1c6KGonoVA3FvpJiMXj1QggX08xcCf3-5NhtFMkfKK93TViyjQJkiTZ7Cm5e0mNBZYF9CZxpDMpIUNyoRHOk5KZ1hcXP4ePcgDnnwCBkmMzomVd5VkgDLZCzBpgVoxsWUcnZAx9SynzDnAfwj72SD6HvDct6pcegRBo3wolhr2qx_ls9IzU4nBGCveU5FldMR2XB_RPl_9umnvGcLXEHeff--bERNS0o_vmUrphr2NAKH9NmY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/112f06092b.mp4?token=aLSq3-monHuHXEztNh02HYJiOBQF4kXe_zEhwH_DGCB9Rx7b1rLKEapE1omAhuCTDC0zQe9N2ILg5klWwtnC-3bQfw3SlmIMTMrV0cBK1V9XTmz4_mjWnIh9mM9Ratc2c2GR5dGHLLAnfJ-eIKXVvnWfYmnzpp6tbzz8zkkg191vg_Th0LRLQjzMpXjLW1HgYNIlkoui9ygSHgWKq_7ev7YtwUIZ53lu8Z31QTkjpPMPNmI7kZCv5bkXb3_s70N8EQGwnbo18mWxttLG2Kkf6gBjrU9GlHt52R1S1qzEfulZFsTh-TznTQJMxLqSkeHQqOQlsmLFkzpWtYf-4eOK83N8Dqapgt-JntKD-NfvYgg3i1sAtFp6YH8G31jkquchd0wu99OP0l8PNvHmfaRHm8g-zsN0Wn0A087fzdfRXWZcbWROOTM8PnMa_L1c6KGonoVA3FvpJiMXj1QggX08xcCf3-5NhtFMkfKK93TViyjQJkiTZ7Cm5e0mNBZYF9CZxpDMpIUNyoRHOk5KZ1hcXP4ePcgDnnwCBkmMzomVd5VkgDLZCzBpgVoxsWUcnZAx9SynzDnAfwj72SD6HvDct6pcegRBo3wolhr2qx_ls9IzU4nBGCveU5FldMR2XB_RPl_9umnvGcLXEHeff--bERNS0o_vmUrphr2NAKH9NmY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهنشاه محمدرضا پهلوی:
"همیشه تلاش میشود ایرانِ دوران من با بهترین دموکراسی‌های جهان مقایسه شود، ایرادی هم به آن ندارم.
اما درباره اینها (ج.ا) که چنین قتل‌عام میکنند همه می‌گویند بگذارید درک‌شان کنیم، بالاخره اسلام وضع ویژه‌ای دارد، در حالیکه آنچه اینها (ج.ا) می‌کنند، در تناقض با اسلام است.
حتی در لیبرال‌ترین محافل، دوران من با بی‌نقص‌ترین دموکراسی‌ها قیاس می‌شود اما به اینها که می‌رسد می‌گویند بگذارید درک‌شان کنیم، اجازه دهید با آنها دیالوگ برقرار کنیم.
این چیزی است که برای من قابل درک نیست."
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/72735" target="_blank">📅 19:32 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72734">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fe642fca6.mp4?token=Ibo6l7fem0hrdXfvlT0oA2vxFSOpEumrM5l6088ntQwoC93RDHv1AmBHp9qqquESuKKQpjLSBcW_RneEwQfWqI0loDWcEjHpq4S--QTyzaO-8aLG57WzIXCwHzDh0y118b-H2L5DOBX0hp7ZPLFqbpsLwtAjhBaVHWTqgJaAmv20PmpxtLdUVJpwsZvqProbyW_qSUuWv4MCVjoddbofDZYXdfLEKnBhddJEa-e12Mr6BRXpe7ANcjU1nfkf4rT7vrRkC5JECUIVJzY4IYlIjBKW5__VdR7yk9o5Zo_7wfJ1f6jFUxWhgq4n8LLDK5P7eVrU-T1jfn2Cy7NSOxGN9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fe642fca6.mp4?token=Ibo6l7fem0hrdXfvlT0oA2vxFSOpEumrM5l6088ntQwoC93RDHv1AmBHp9qqquESuKKQpjLSBcW_RneEwQfWqI0loDWcEjHpq4S--QTyzaO-8aLG57WzIXCwHzDh0y118b-H2L5DOBX0hp7ZPLFqbpsLwtAjhBaVHWTqgJaAmv20PmpxtLdUVJpwsZvqProbyW_qSUuWv4MCVjoddbofDZYXdfLEKnBhddJEa-e12Mr6BRXpe7ANcjU1nfkf4rT7vrRkC5JECUIVJzY4IYlIjBKW5__VdR7yk9o5Zo_7wfJ1f6jFUxWhgq4n8LLDK5P7eVrU-T1jfn2Cy7NSOxGN9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنگنده های عربستان سعودی مقر نیروهای خودی را بعد از اینکه به تصرف حوثی ها درآمد، در تعز یمن بمباران کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/72734" target="_blank">📅 18:47 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72733">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aJ9qshcRc3yJ-7QuoVXEJDxQPsQ4hl-DDKnpYCSAc_vuGCETZ92z6REKvd82tzXYIMFY7JqsSan1TsNC0MjkLop7uFtzaL0TrFnwtIQ3GMqGOmoykjqTqXYwRVJ1llUegVgO6rUkPmxj0vDzNKcFXYhGn_igtHqtBJ7JNjALGvKIF5TFC80gVZ7J2-OGpY1ZoTZZLPskCHVlCrDY1ZmLy6vGuPmecoPWBHISggibJu14blYopQgRQS47xECccCZkZzGHZjwW_SMXuyduQgCBzYHWcnE-wXUn6i8L7F6MQD1qwOhNGc-HmJmVTX_EjPK3vug31LujjRVFDHFx_OCp6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایالات متحده با ارائه کمک‌های اطلاعاتی و پشتیبانی در تعیین اهداف، از عملیات تهاجمی تحت حمایت عربستان علیه حوثی‌ها پشتیبانی می‌کند، اما به‌طور مستقیم در نبرد مشارکت ندارد.
شاهزاده خالد بن سلمان، وزیر دفاع عربستان، از پیت هگسث، وزیر دفاع آمریکا، درخواست انجام حملات هوایی کرد؛ اما مقامات آمریکایی اعلام کردند که واشنگتن فعلاً قصد انجام «اقدام نظامی مستقیم» (عملیات کینتیک) را ندارد.
گزارش‌ها حاکی از آن است که فرماندهی مرکزی ایالات متحده (سنتکام) با انجام این حملات مخالف بوده و یمن را عاملی می‌داند که تمرکز آمریکا بر ایران را منحرف می‌کند.
@News_Hut
| Axios</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/72733" target="_blank">📅 18:29 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72732">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9ee58a69b.mp4?token=qXnlqX_0I6l5eSbXc_nTLwYMS-Hcsx5jmdTyW4X-vXkagGD05MXyCvV3SUrTJXQ8HgZOx6aNu65Zo1PquzfmPF2YS0Q39d-3g6kRzYyMYWE0XIMmHQrvWNJglxHMRb1IJuG1jNqvMVaKgxyjU0pzvk9JdwYE8J0kMd5HYe2co8leN9ZeOq8MsDqgbZkdP-xIqnFhcVf4ClZwYL-YzzZja-bNYbL23kU_URGaRNe5BqonBIrigAnMZeUX5V7DuKe36DXKAmBjcB2M9ws9DFMLUe9cwI3-_gcR9eSK0zaabjCSFh0Hv-ItRBGpZZZnKu96NB_mwCw-h3ksTQvnVkEV6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9ee58a69b.mp4?token=qXnlqX_0I6l5eSbXc_nTLwYMS-Hcsx5jmdTyW4X-vXkagGD05MXyCvV3SUrTJXQ8HgZOx6aNu65Zo1PquzfmPF2YS0Q39d-3g6kRzYyMYWE0XIMmHQrvWNJglxHMRb1IJuG1jNqvMVaKgxyjU0pzvk9JdwYE8J0kMd5HYe2co8leN9ZeOq8MsDqgbZkdP-xIqnFhcVf4ClZwYL-YzzZja-bNYbL23kU_URGaRNe5BqonBIrigAnMZeUX5V7DuKe36DXKAmBjcB2M9ws9DFMLUe9cwI3-_gcR9eSK0zaabjCSFh0Hv-ItRBGpZZZnKu96NB_mwCw-h3ksTQvnVkEV6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی ارتش:
در جریان این جنگ به این نتیجه رسیدیم که قطعاً باید برد موشک‌های خود را به ۱۰۰۰ کیلومتر افزایش دهیم، زیرا دشمن در حال حاضر در فاصله‌ای دورتر از سواحل ما مستقر است.
اکنون در این مسیر گام برداشته‌ایم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/72732" target="_blank">📅 18:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72731">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72731" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72731" target="_blank">📅 18:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72730">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dHQJdMzw4whWgfZrr8jfvI1Cn3HAF2_Gzm6hlanX4_e-yxF_30DGAROmKWZbBbAY8FE-9lIxLMXSW0_icnb43CqhQ87qog-9iEgRdO28UX_JO_ck-iqVCVSbzCtwDcI2lJ90TquD3mWpaP9oRzWaSFyEhrR46JS7t8t4EZgAMIn6aULfGRfYiJhdUPTbFsbQeVqXeZCG_sCPkTe39nhZ1Vxon9Emm9vsBJ2AOvjR7tJasswwx5in6q0vrJMJ1rdJzVNwtFFC0ouqjgzQX01LBygH_EhzQeZf8oNmGa8QvOCqfWeGf3YjBc3d0vR6AP0o9EulJr2kzqK8lXmEPm-S6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز نروژ
🆚
پرتغال را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
نروژ: ۲ برد، ۳ شکست و ۸ گل زده
پرتغال: ۴ برد، ۱ شکست و ۹ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72730" target="_blank">📅 18:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72727">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bu4VvgU29rHBBxCM9mg3FfltJhmVJk02LCjCYxKgqHklugnXRKYbdV7JZWHR6hSLTpkyrEN_8-aJsao39mZ8QWkMt4eGMXmmkEHaFPL7Re49llN7w0VPdM20x5wzkBy7V02EUIhznO8-jzJgVhTrRj7hfrycViir6Jzwcp7GpsBzQ5PHoHUOOT60J474k8LU7uMrZ72q0cIDc-i0evmIfg10h26ZFhMjqvDBmavgi-D2-0jQUsTGSyVPyVGSXFV2tS2WZw1s5SCe1BYrmOD7oWQSAGroO6HvYfcpD0GEJHs6kT42jDhAXBodTVv5WuLia8sJbOezEW1lAhRjDCLDJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0214da517f.mp4?token=LgqlFhyuoD4Ebl3uHhfsq_Nlf1tezs-t2gQ3Ah6hicR9MYghRDqS8HMSQtlV8YEkfsv96kkq50yGVGD6TGUziwqMZK-UCtr5tPhajF0RfmotmM1qs-ghQ1c1jt-oWPmJPRHgfqdLM8JuxFXuVAp4N6CRw8651Ij_7L2o2eElzPdmGpR6GzE3wr0lhVNh3Uo_KbGLWIHI2uHmfUtuPEZpZzXYS40-NxFhL_rTN0ZOorEKQZPCwzNVTyo5gIBstFGqlWaicPTdQt1qRNkCZeTlOS3DnknCkqBUn84l2ds49NV9X1dLEbVPM6uik1urV9TRdJDEHc1GaaxPbsNbSVg-7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0214da517f.mp4?token=LgqlFhyuoD4Ebl3uHhfsq_Nlf1tezs-t2gQ3Ah6hicR9MYghRDqS8HMSQtlV8YEkfsv96kkq50yGVGD6TGUziwqMZK-UCtr5tPhajF0RfmotmM1qs-ghQ1c1jt-oWPmJPRHgfqdLM8JuxFXuVAp4N6CRw8651Ij_7L2o2eElzPdmGpR6GzE3wr0lhVNh3Uo_KbGLWIHI2uHmfUtuPEZpZzXYS40-NxFhL_rTN0ZOorEKQZPCwzNVTyo5gIBstFGqlWaicPTdQt1qRNkCZeTlOS3DnknCkqBUn84l2ds49NV9X1dLEbVPM6uik1urV9TRdJDEHc1GaaxPbsNbSVg-7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به نظر می‌رسد نیروهای انصارالله موفق شده‌اند کنترل منطقه «البرقانی» در شمال «الصفیه» و در محور جنوبی تعز را به دست بگیرند.
در ویدئویی که منتشر شده، نیروهای حوثی هنگام ورود به خانه «سلطان البرکانی»، رئیس پارلمان شورای رهبری ریاست‌جمهوری یمن (PLC)، و تصرف آن دیده می‌شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72727" target="_blank">📅 17:42 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72726">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad9e96757a.mp4?token=r6oGBeEJopDanju_W0dIU-hw0NuWUhj_A-9e2hcHhP2Qkfa5cJQ-2eXdRhDm0Wc-Ge8rKCS8_rVRszOeYUYPVnOq9EsSj7T85L7JTT_zhJ56F8WU1i-TSUD1DuNsPpBnMb8oZ9WuyvKfJUTYEcktJfjxLpJ3mVcvyjpDykRfPMfsMcOlihbahbm9UEbQvls41cZyLyP4jl_9-JZDpHJclMjU4XKc6X8OjQNZB1Fnm7MFkNBvl7fHt6fiPeX4r9zp-hACidsKxhaVB5uHSukHPyj0iaflNQ51RsgW_U0WLUJjiRpUpAnrIcYZ2Zz1fwO3Q7maMUkDRcMxXYPa3d9c671p3RjfJgrWifZJkeqByERqg6RX0cMNrp4MIW0Ko_o1CaUWF1wy5IGhHGMICJm7urBDwMf4seRGeHTHt6HbTvOg3NlwVbefvWa3xO7MaCDVvK8i88xPCoyAnWbZoemuqskelv3SoNWwOuntR1FivjXnAbPss0YHxpmS6h8W2PhtHb8AM1cQWS87AV6wRvxgKNHmRQNCEmNMotddX4UpzY-bp2cQVT9pmihBPf-tIIK-09-HYVu2LHz7OWzCBULgJ7eLpjWY9LkPZ4AFlKUPXxpssAiP98wpDN0fedFlwY183XJhaAA-H5m82A6VnRfwF6mL_aqy-rdT-PtbIkGIvcI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad9e96757a.mp4?token=r6oGBeEJopDanju_W0dIU-hw0NuWUhj_A-9e2hcHhP2Qkfa5cJQ-2eXdRhDm0Wc-Ge8rKCS8_rVRszOeYUYPVnOq9EsSj7T85L7JTT_zhJ56F8WU1i-TSUD1DuNsPpBnMb8oZ9WuyvKfJUTYEcktJfjxLpJ3mVcvyjpDykRfPMfsMcOlihbahbm9UEbQvls41cZyLyP4jl_9-JZDpHJclMjU4XKc6X8OjQNZB1Fnm7MFkNBvl7fHt6fiPeX4r9zp-hACidsKxhaVB5uHSukHPyj0iaflNQ51RsgW_U0WLUJjiRpUpAnrIcYZ2Zz1fwO3Q7maMUkDRcMxXYPa3d9c671p3RjfJgrWifZJkeqByERqg6RX0cMNrp4MIW0Ko_o1CaUWF1wy5IGhHGMICJm7urBDwMf4seRGeHTHt6HbTvOg3NlwVbefvWa3xO7MaCDVvK8i88xPCoyAnWbZoemuqskelv3SoNWwOuntR1FivjXnAbPss0YHxpmS6h8W2PhtHb8AM1cQWS87AV6wRvxgKNHmRQNCEmNMotddX4UpzY-bp2cQVT9pmihBPf-tIIK-09-HYVu2LHz7OWzCBULgJ7eLpjWY9LkPZ4AFlKUPXxpssAiP98wpDN0fedFlwY183XJhaAA-H5m82A6VnRfwF6mL_aqy-rdT-PtbIkGIvcI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛رشاد العلیمی، رئیس «شورای رهبری ریاست‌جمهوری» (PLC) یمن که مورد حمایت عربستان سعودی است، از آغاز عملیات نظامی تمام‌عیار در تمامی جبهه‌ها برای بازپس‌گیری مناطق تحت کنترل حوثی‌ها (انصارالله) و احیای حاکمیت این شورا در سراسر کشور خبر داد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/72726" target="_blank">📅 17:29 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72725">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05733ed2f5.mp4?token=Rfr-rw368DETs8YFxdHNI5s9neOLPGya0i4NMVaPIXHD94fe8uAsefpDAAfXzbHCZ4xoq1yUrvGCUYoxQrQP_6I1MpBvv1DAoOOKbmTp4wm9kTB0YyMzMu2FLMCHNsZOdQ9LJQAfTvYEtYwWBMS6oawzEiFZjG90pKLbBE1j7pZez_Jkc6MYOpJDqpc6G0jPz2coFxj8WfAzJE0vR24AuoixwmJuJLG3AKRpvGn_-HQNdsYqXjypr_X1KlpuK3Q2az1EHEOSYFTvm4KsSxkckzEIxkcM15cmpn1X25eaJXuuPFUVRSuNdbwcTyM9Bo7ishBqwiE3-D4vTKXPzEI2gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05733ed2f5.mp4?token=Rfr-rw368DETs8YFxdHNI5s9neOLPGya0i4NMVaPIXHD94fe8uAsefpDAAfXzbHCZ4xoq1yUrvGCUYoxQrQP_6I1MpBvv1DAoOOKbmTp4wm9kTB0YyMzMu2FLMCHNsZOdQ9LJQAfTvYEtYwWBMS6oawzEiFZjG90pKLbBE1j7pZez_Jkc6MYOpJDqpc6G0jPz2coFxj8WfAzJE0vR24AuoixwmJuJLG3AKRpvGn_-HQNdsYqXjypr_X1KlpuK3Q2az1EHEOSYFTvm4KsSxkckzEIxkcM15cmpn1X25eaJXuuPFUVRSuNdbwcTyM9Bo7ishBqwiE3-D4vTKXPzEI2gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پای رپر ها هم به تجمعات شبانه باز شده:
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/72725" target="_blank">📅 17:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72724">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f15ab8539d.mp4?token=VhFGHncqqE24bZoTLPfJ0tiW92lgibC2UvdZg8G8eu_KiQvmwerSUKytnGzo91nG4MtAgpHlvmEyp51ad0D5Awlkl_V4cIwFr1yRRPj-Vw1AUV7-u7iRi2xYp0J_xRYGw8a_STsUMISR2iS84vOdIbM7bXkz741SeHKSUF3TjrgaHAuba_re7idlrKMyaFDgC5plNXmUpxJwn3EnxwMCl5Lxe3DjErPwFxGdFT3ackh-Fh4lBfyAaqNWgw9qARGOYfJZXx0d49IrGePhMrbsveSu3j1cw00E1RBdgDBU3H8JAFo1EHqy_5jIb-d5j3xOIbGN5OYVehjuavnB4CZgwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f15ab8539d.mp4?token=VhFGHncqqE24bZoTLPfJ0tiW92lgibC2UvdZg8G8eu_KiQvmwerSUKytnGzo91nG4MtAgpHlvmEyp51ad0D5Awlkl_V4cIwFr1yRRPj-Vw1AUV7-u7iRi2xYp0J_xRYGw8a_STsUMISR2iS84vOdIbM7bXkz741SeHKSUF3TjrgaHAuba_re7idlrKMyaFDgC5plNXmUpxJwn3EnxwMCl5Lxe3DjErPwFxGdFT3ackh-Fh4lBfyAaqNWgw9qARGOYfJZXx0d49IrGePhMrbsveSu3j1cw00E1RBdgDBU3H8JAFo1EHqy_5jIb-d5j3xOIbGN5OYVehjuavnB4CZgwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه زنه داشت از حس و حالِ ناراحت پسرش تو روز اول مهر فیلم می‌گرفت که یهو یه مرده اومد و این شاهکار رو گفت:
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/72724" target="_blank">📅 16:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72723">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5caffe71ff.mp4?token=aWYuPy5Nt5CHrDKJv4wf-KlE9K38wcgHaifAWE19tYRA-ikNbE6bd8phC6SENCSfbNY_th8mVMjwM-uk2V0XiDSWtn0b440PnQP5rXz5gKg20_PUQ70gckvOsaCsSCKP_VYJnMiQG9eunq6Kn7w0_kNEXTS0pK7OI0Re1pvkJwAGERcv4JloGwYFLUCc4BJgG5qVKJ1NbleL-wQQy895WXyMA_xnknC9UAL4mW7XFt83cr41gqBeG5Sx4WoUbKogbmmMw_uVjhLjM-RzIXrDutSGibMPQskcOvJtUuuAf1GVFzaIJ_EOLlGhqzT9rEsoEsYVZqYD9PGG8cdCm0ui3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5caffe71ff.mp4?token=aWYuPy5Nt5CHrDKJv4wf-KlE9K38wcgHaifAWE19tYRA-ikNbE6bd8phC6SENCSfbNY_th8mVMjwM-uk2V0XiDSWtn0b440PnQP5rXz5gKg20_PUQ70gckvOsaCsSCKP_VYJnMiQG9eunq6Kn7w0_kNEXTS0pK7OI0Re1pvkJwAGERcv4JloGwYFLUCc4BJgG5qVKJ1NbleL-wQQy895WXyMA_xnknC9UAL4mW7XFt83cr41gqBeG5Sx4WoUbKogbmmMw_uVjhLjM-RzIXrDutSGibMPQskcOvJtUuuAf1GVFzaIJ_EOLlGhqzT9rEsoEsYVZqYD9PGG8cdCm0ui3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیروز تو مکزیک  یه گزارشگر داشت از وضعیت خرابیِ کنار جاده گزارش تهیه میکرد که همون لحظه یه ماشین لیز میخوره و تصمیم میگیره گزارشگر و فیلمبردار رو با دیوار یکی کنه :
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/72723" target="_blank">📅 15:48 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72722">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf8cf90e0c.mp4?token=pr87DUh4A2tqLoGXC3z8nUwGHPTtXnglwh6xegd4Q3TcVH2kfCnq1fuwv2VAqUdlaxUMyXJuguMgTmwI1iOA9o80dAfr9s5BmPlaPzM3Wt9MjeeSsiKVEjzU1Y8aI65WRqN7LInV5iZ91Z3UGSIXohvL5Vr6dp18oLv1PXek3ZKVHky-9VRrxyGj__y6vV57L-XcDCjSR066wAZAd-zQu1BjDUxrEkxBuH07BStpvbg6DUh6siSEPlemFAKjTGLvRsKEtOpfrOInhmNqPNYJ2RmoU5qxARvUgj9Xloel34xRtupdZKniP7isjECBdkOaWhBGJygT0bH6ZsEc8WPLWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf8cf90e0c.mp4?token=pr87DUh4A2tqLoGXC3z8nUwGHPTtXnglwh6xegd4Q3TcVH2kfCnq1fuwv2VAqUdlaxUMyXJuguMgTmwI1iOA9o80dAfr9s5BmPlaPzM3Wt9MjeeSsiKVEjzU1Y8aI65WRqN7LInV5iZ91Z3UGSIXohvL5Vr6dp18oLv1PXek3ZKVHky-9VRrxyGj__y6vV57L-XcDCjSR066wAZAd-zQu1BjDUxrEkxBuH07BStpvbg6DUh6siSEPlemFAKjTGLvRsKEtOpfrOInhmNqPNYJ2RmoU5qxARvUgj9Xloel34xRtupdZKniP7isjECBdkOaWhBGJygT0bH6ZsEc8WPLWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فریادهای مهدی کوچک‌زاده نماینده مجلس بر سر همتی رئیس بانک مرکزی؛
کوچک‌زاده:
مملکت را دارند به آمریکا میفروشند.
«به خدا اگر از جهنم به خاطر کوتاهی‌هایی که در حق شما مردم کردم نمی‌ترسیدم، امروز خودم را جلوی بانک مرکزی آتش می‌زدم.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/72722" target="_blank">📅 15:16 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72721">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d26538e463.mp4?token=DYsFC0QMuJdaYYklzhGd8hp4X7wejhKFEGD6UybfLD60o7GHNoLwtNIxS-1TRwGr2NeW-2qc38-DRcFwAZD6Ep65yzcC7iVXkuMAGVAkreJ3yeM5-eFPadIKhledRMPmOHjKOAHYFReqXCk5etFHbqnOBoax56p_sQPdOYrgp1iyzzbqr_61shYMyUiChPLTOLO8FtsgMTXrnDC7-iP0yM-MxAFJA5E-bFcr9jg18H7CJHt3EY2-3wjwgvMf4jucGLbcTe0Atpy7nQrhPcbVqJmCpKeH0JNwIVjueobwV-ejzdLupS4ucqpGYx5iz4fh6q3DDz8cAlDYxXHLqKSgVSSEVLC2WE9pxysOOs_SZqW1IliozLivMOvcDcy1xUBud7FB1m9EtupNsVZbGRWojmAmxSxDNMzrSthdEmo4nyh0gXnkgjC1xrf649XVpfYj4FTWF8ZQGHVa4DJn9EhvpC9I7ovX6YE3-5Tv_UmZwJlCy4V4LE1kUZ1jB9ba6wbmLdmhOGS0BSxHO8pXo5-x7HIZWVm8rF7Kc-wv88UWvl4HaoJbR35dlfE1cdH_zI4Zz6JBF76zjvNBXhJFsSZI9YNNT5m5ytiJqcvSPQJcwpgYRv1f20LFGDiWYjCYVVj6BoRAqJ3yMuf5ECUoRB4IGbaLbS7qmziiQdIrYIUmsVM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d26538e463.mp4?token=DYsFC0QMuJdaYYklzhGd8hp4X7wejhKFEGD6UybfLD60o7GHNoLwtNIxS-1TRwGr2NeW-2qc38-DRcFwAZD6Ep65yzcC7iVXkuMAGVAkreJ3yeM5-eFPadIKhledRMPmOHjKOAHYFReqXCk5etFHbqnOBoax56p_sQPdOYrgp1iyzzbqr_61shYMyUiChPLTOLO8FtsgMTXrnDC7-iP0yM-MxAFJA5E-bFcr9jg18H7CJHt3EY2-3wjwgvMf4jucGLbcTe0Atpy7nQrhPcbVqJmCpKeH0JNwIVjueobwV-ejzdLupS4ucqpGYx5iz4fh6q3DDz8cAlDYxXHLqKSgVSSEVLC2WE9pxysOOs_SZqW1IliozLivMOvcDcy1xUBud7FB1m9EtupNsVZbGRWojmAmxSxDNMzrSthdEmo4nyh0gXnkgjC1xrf649XVpfYj4FTWF8ZQGHVa4DJn9EhvpC9I7ovX6YE3-5Tv_UmZwJlCy4V4LE1kUZ1jB9ba6wbmLdmhOGS0BSxHO8pXo5-x7HIZWVm8rF7Kc-wv88UWvl4HaoJbR35dlfE1cdH_zI4Zz6JBF76zjvNBXhJFsSZI9YNNT5m5ytiJqcvSPQJcwpgYRv1f20LFGDiWYjCYVVj6BoRAqJ3yMuf5ECUoRB4IGbaLbS7qmziiQdIrYIUmsVM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
من با کیم جونگ‌اون، رهبر کره شمالی، رابطه بسیار خوبی دارم.
وقتی طرف مقابل ۱۱۲ موشک هسته‌ای در اختیار دارد، خوب است که با هم کنار بیاییم.
اما تفاوت اینجاست: ایران هرگز موشک هسته‌ای نخواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72721" target="_blank">📅 14:56 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72720">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbe93c3478.mp4?token=qY_AQNEudOxo0Efx6X-GmwNdnRzNYngg91uH6yF05FEpB4fHEYyzgywYM7B8mTnyFE1CK7IuC8egQuEp3Nsm7AFqiec-NwIZlfuKkCAz3-SgeQTjtDqevnsjzKzp_9vu60zmH1QioDxYyvwa-ikMJJB6dtS8Fww0ngL4urFVeKZbqJt9EPagOQ82s32CYajnthQzu1k02FnTLRWXkiVBUaccy71cNozuj19uFdcg59Ttqk171Sdk8L5lySJxavcAcN5lSp6iwpJ4JEckEymacmKg3JULUmuh1pUwQRAeKM3_xozQNcT59h2XadhrGG-S9HXyxdW8EZhi_6wiKXOi-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbe93c3478.mp4?token=qY_AQNEudOxo0Efx6X-GmwNdnRzNYngg91uH6yF05FEpB4fHEYyzgywYM7B8mTnyFE1CK7IuC8egQuEp3Nsm7AFqiec-NwIZlfuKkCAz3-SgeQTjtDqevnsjzKzp_9vu60zmH1QioDxYyvwa-ikMJJB6dtS8Fww0ngL4urFVeKZbqJt9EPagOQ82s32CYajnthQzu1k02FnTLRWXkiVBUaccy71cNozuj19uFdcg59Ttqk171Sdk8L5lySJxavcAcN5lSp6iwpJ4JEckEymacmKg3JULUmuh1pUwQRAeKM3_xozQNcT59h2XadhrGG-S9HXyxdW8EZhi_6wiKXOi-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسماعیل بقایی سخنگوی وزارت خارجه جمهوری اسلامی :
بحث‌ها پیرامون خروج از پیمان منع گسترش سلاح‌های هسته‌ای (NPT) در محافل سیاسی ایران بسیار جدی است و وزارت امور خارجه به تصمیم مراجع ذی‌صلاح پایبند است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/72720" target="_blank">📅 14:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72719">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7872ea066a.mp4?token=Mc1pgUMvy2h4d3YyDl9WVXbNIhRnbwOOQNz3s0EyeHRj_WJgyI1Nuv8W_H8RbRLQBVJx3a6pe4k4aZwhS0x7W1eUUNF_l1rgCT_qgGq6DREOX3whjfuLpJjNWtefoE8dIuQMU-ufanITnLkNS-Dp3ahZV2g77u6sMX24LBUewGQYXFjae5WOJrVVWS-Q2LZQTs9uGGhQASIu4iqurNwpoZV__-rJiHY-Kx-kqo6ma_XBmM66pZlagVoVpE6msaRpCP_x1_Lk7oGKIwVy9Kd_6W0cOlEDQCYn2aX8RqYNbliOL61N8YO3WiPz3rJowol8oadBTh6BkFK-MErt89F8Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7872ea066a.mp4?token=Mc1pgUMvy2h4d3YyDl9WVXbNIhRnbwOOQNz3s0EyeHRj_WJgyI1Nuv8W_H8RbRLQBVJx3a6pe4k4aZwhS0x7W1eUUNF_l1rgCT_qgGq6DREOX3whjfuLpJjNWtefoE8dIuQMU-ufanITnLkNS-Dp3ahZV2g77u6sMX24LBUewGQYXFjae5WOJrVVWS-Q2LZQTs9uGGhQASIu4iqurNwpoZV__-rJiHY-Kx-kqo6ma_XBmM66pZlagVoVpE6msaRpCP_x1_Lk7oGKIwVy9Kd_6W0cOlEDQCYn2aX8RqYNbliOL61N8YO3WiPz3rJowol8oadBTh6BkFK-MErt89F8Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکشنبه ۱۲مهرماه۱۴۰۵؛آتش‌سوزی در پاساژ خلیج‌فارس عسلویه به دلایلی نامعلوم:
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/72719" target="_blank">📅 14:36 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72718">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OE6PIZE8RUJVZ7901_mlo3pw2WaDKEsNjQPQnYZzPcmuT23of-Vx1t9pR7cJgifOKxr4OIj7Tta7BVbEvLh2zQGuFDgw67McdDYGzMtZu9KdDTWlWpRzXcvpXzeyMe0u9c-4eR5si6EFe5-fItWQTykn8K6vKyPPMXyGgeRBjhCmEoNbuFPJ_ObkYYTbBhe5z5ZHxO3kTjVE-u-t28_6Ea1L2qVpwZ5Uy6IY5Wone9TCDblFI0zkT1ofGMYIwx15yvWXtIuDHmNq1Xn7rFKdhta4aPkP13xtKBkXnURvRdIh3zqDleIDgglwB-ZrVbPMFSMUwOpVsSeb6SBu5z7Vfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرواز تهران _ نجف که قبل از محاصره هوایی حوالی ۱۲ تا ۱۹میلیون تومان بود ، دوباره برقرار شده اما بیش از دوبرابر رفته رو قیمت و شده ۳۰ تا ۳۸ میلیون!
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/72718" target="_blank">📅 13:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72717">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3330937cb2.mp4?token=k0ed1GMBLWjg0jr9d9N2u-bSrmI9m5AEpr7Y2Id1FydzPbQXiy0yhbVRukTXwHzxHI4xMA-jOXSt-HzSGEGUiKiHB4Q3LVbKmIR5hgISW9IFuC1qVv3dlIdr8ykpDl3TX-r5CK4UK8duKHEanv3Fof4ZdqpNz21fsxM-g_PL-CbbmCLFkAi7vqoEnibUytGVZFPEYVX7yq8m6y_QCED54wL8SYMYJoFLMsiuv00GPFW9WETB3iZNTzUdXrKgNnQXH8jYDuDjD-NWN5Ax60WdYItEqo6F05PQmb8Kef4M75SzIlpHXRv5NYtkHWCTevlsFIn9HDUxJQiPUnZVDi_Ueg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3330937cb2.mp4?token=k0ed1GMBLWjg0jr9d9N2u-bSrmI9m5AEpr7Y2Id1FydzPbQXiy0yhbVRukTXwHzxHI4xMA-jOXSt-HzSGEGUiKiHB4Q3LVbKmIR5hgISW9IFuC1qVv3dlIdr8ykpDl3TX-r5CK4UK8duKHEanv3Fof4ZdqpNz21fsxM-g_PL-CbbmCLFkAi7vqoEnibUytGVZFPEYVX7yq8m6y_QCED54wL8SYMYJoFLMsiuv00GPFW9WETB3iZNTzUdXrKgNnQXH8jYDuDjD-NWN5Ax60WdYItEqo6F05PQmb8Kef4M75SzIlpHXRv5NYtkHWCTevlsFIn9HDUxJQiPUnZVDi_Ueg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش روسیه به پل شمالی در کی‌یف حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72717" target="_blank">📅 13:10 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72716">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42b7e86ab7.mp4?token=d6q-zmb9YTipfwOh8Mbn9XV9d7xt-wmnwsDu_gQcxi_ksoIukQ3kkVTsmGytEJLbT64sSdrzMdltZkSq4e99AcUGLDKDLskCvCFHV8c1cgxLOQM6Dg1huHhNPhbc50gfxP-O-IAYmDsA1mKn8oYgPrUQTih-We9re6bL-LQibmENvo-YQCQsXGfyy6j0Rz_j3cL6ZU0oQAg6MHWJat6zu7Sa-ML4HHStMc9DMpRbrRKdcYv7-ZArxRL_zCLdhXHwRdNdG_oRdRvrtklsUGZzwXsH3nmEMPs4iwkHI-c1jT92i2ZmAlUAZnHbuLesASUkkpxeoVfMygcSjuec18H1_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42b7e86ab7.mp4?token=d6q-zmb9YTipfwOh8Mbn9XV9d7xt-wmnwsDu_gQcxi_ksoIukQ3kkVTsmGytEJLbT64sSdrzMdltZkSq4e99AcUGLDKDLskCvCFHV8c1cgxLOQM6Dg1huHhNPhbc50gfxP-O-IAYmDsA1mKn8oYgPrUQTih-We9re6bL-LQibmENvo-YQCQsXGfyy6j0Rz_j3cL6ZU0oQAg6MHWJat6zu7Sa-ML4HHStMc9DMpRbrRKdcYv7-ZArxRL_zCLdhXHwRdNdG_oRdRvrtklsUGZzwXsH3nmEMPs4iwkHI-c1jT92i2ZmAlUAZnHbuLesASUkkpxeoVfMygcSjuec18H1_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در حرکتی شاهکار نگهبانای ی شرکت رفتن با سلاح برنو بالن هواشناسی رو زدن و بعد زنگ زدن به سپاه گفتن پهپاد آمریکایی رو زدیم بیاید همین الان جایزمونو بدید
😂
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/72716" target="_blank">📅 12:49 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72715">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">دلار ۲۷۱.۰۰۰تومان
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72715" target="_blank">📅 12:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72714">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7da8647691.mp4?token=dcKOHM7WVubZ_7TB7o66Yk8Rlnojp6PwLPiwsfx8FQgIxwKHulajhfBZef4AmBy9aj34-WC2KWodlW1hpHMNFyBlyt4W1pWkpdS7cYCZXZwxgxrHspAgaEkVy-US8gsxew91CvBn_88pkKz3UHnbFuAxlo2Go0xGjOSzW-1rjNoR8qS6hKuS1r2OhF9zEvtpvTgtyKlgEqvnGQUZaGKaZ2Xg44BhV6PZ3G0O3Pg6hZlZmmDFZYr3QyGkRF5OHDfoZAvdUHxMhKQG75raTsfkz9FBDy_zuyV_NctS8dyrIJ-zD3h-z02pAQYm5kRmk8kt3vPpDkF0gWHZDQmL6Y6XDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7da8647691.mp4?token=dcKOHM7WVubZ_7TB7o66Yk8Rlnojp6PwLPiwsfx8FQgIxwKHulajhfBZef4AmBy9aj34-WC2KWodlW1hpHMNFyBlyt4W1pWkpdS7cYCZXZwxgxrHspAgaEkVy-US8gsxew91CvBn_88pkKz3UHnbFuAxlo2Go0xGjOSzW-1rjNoR8qS6hKuS1r2OhF9zEvtpvTgtyKlgEqvnGQUZaGKaZ2Xg44BhV6PZ3G0O3Pg6hZlZmmDFZYr3QyGkRF5OHDfoZAvdUHxMhKQG75raTsfkz9FBDy_zuyV_NctS8dyrIJ-zD3h-z02pAQYm5kRmk8kt3vPpDkF0gWHZDQmL6Y6XDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان حکومت بر سر قبر علی خامنه‌ای، علیه مسئولان نظام شعاردادند؛
«گرانی رو آوردن، سازش کنن با دشمن»
«مفسد اقتصادی، سرباز آمریکایی»
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/72714" target="_blank">📅 11:59 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72713">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BYy7jqiKAth_Kpdd8hOFimMpcvKOe-o6MUixtfdKbfwJNJX0PS74xll104lwE76GjinPly4J-u0aIyUOAocOulZHf-N0TLOYym9Z1K6pLPG00xuJsbdY6jNm8FSMMwvPky-lnzgPLZbVOm7BQ2nP1M_XvM4QJNOdGKizEW95km6Q1Z_GQaZT8QhvbT8esvRyIDKoUky1cqPAFR_p9Th_0HGQXGVZtJqEZiU7XAoWZiyJ6UbrNbeod_1KAWRBPiik1x5ZzJkOJAMGtuwcdK3aaEEn-2WZq3G5KnxSi3smGvONmqJUjjhE6EKU9qSg0IuijMRgTk7ia8ybEqNDztG6Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا: یک نفتکش در داخل تنگه هرمز هدف یک پرتابه ناشناس قرار گرفته و موتورخانه آن آسیب دیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72713" target="_blank">📅 11:37 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72712">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72712" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72712" target="_blank">📅 11:37 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72711">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mZEr3wib2frKqVVYQTKIp4Y0Y4laa2CSR-atlX6I_nkv33LxeCHn1HpOOzP1vvea9V2mDMxoOV964Upy5RO53iQzM7qK7w4bcdTEmJpzGenS1JdkY1tuBOKZWyHRdVROa-6dwOyZ3vGdjjQQFdJB7q7rESbKRI_O2yeMTZSzv9RhHaBe3oyb2OXUmfMOdvu-9B1dIqN2kWCHf9KWv169t9qyxDCk6sDI2sx06XMfubXY5aBohSPuQC5cuvqzcBIS9RMoSsRDGNTvglzIfDHk0nDvgpOSLkRJJydmsYSt5ZUtCFANXIFTaRPabQhQrBIUwaZSakQWRTQgfniNnHcbnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
آلمان
🆚
یونان
صربستان
🆚
هلند
نروژ
🆚
پرتغال
دانمارک
🆚
ولز
آفریقای جنوبی
🆚
مصر
مالی
🆚
مراکش
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/72711" target="_blank">📅 11:37 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72710">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50e9a4b7ef.mp4?token=ZMdVQ9ZMjNyPJfnmbRrgAvBXkY_QAt5eduJnq5u4-y5SEStCuw8ECGGGHlDpNDn0GsNaELrX8rt8chhA4c9rSbKItu4SobAP8z-OhXepwEBkqKz_NZNr4khvxP4cBuaMrTtoGxACxMEmaP4bWgFYPBWW4AKGr3jzqAz02s4rfnF-_KuJmH-n9sOn_MH4bjXntoA7gwgyQj9fgkTZVrqwME8_C7AoqDpCJk_1Plego3xPgLaUoXDrArDSca-CmGsQfz0QvMBaNdi9MM9CZtWdLhz-DNrS1l_WjZm7bhxjJdzJXo0l0SNEO1p3ddMDvHnvyFESoXbZDcCIumdHZRPH3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50e9a4b7ef.mp4?token=ZMdVQ9ZMjNyPJfnmbRrgAvBXkY_QAt5eduJnq5u4-y5SEStCuw8ECGGGHlDpNDn0GsNaELrX8rt8chhA4c9rSbKItu4SobAP8z-OhXepwEBkqKz_NZNr4khvxP4cBuaMrTtoGxACxMEmaP4bWgFYPBWW4AKGr3jzqAz02s4rfnF-_KuJmH-n9sOn_MH4bjXntoA7gwgyQj9fgkTZVrqwME8_C7AoqDpCJk_1Plego3xPgLaUoXDrArDSca-CmGsQfz0QvMBaNdi9MM9CZtWdLhz-DNrS1l_WjZm7bhxjJdzJXo0l0SNEO1p3ddMDvHnvyFESoXbZDcCIumdHZRPH3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بابایی، رئیس کمیسیون اجتماعی مجلس:
می‌خوایم حقوقِ کارمندان دولت رو 5 الی 10 میلیون تومن افزایش بدیم!
قراره «فوق‌العاده خاص کارکنان» تو کوتاه‌ترین زمان ممکن و با امتیاز 2 هزار تا 20 هزار واسه کارمندان اجرا بشه.
این افزایش از اول شهریور محاسبه میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/72710" target="_blank">📅 11:30 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72709">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a343c0ae1.mp4?token=UZtShaXJhMBM51QazfJEmDUeMI3XpZcF6pznvXuNhuqt4wpSgJTQs_3aqA258swgH0kRJKbTHCFDhQCWSZnVdjG63CBdWNRHcTfYxb1pYAp3x_6f5T8TvsH24Jb0npFeEripq-NP62fIuig_HxnA0SUz31kOTa_mYejHtI-YSPCkOimXJVgYETu3djurBkPCWg7ofsDuwK2zSs1rXKy6HqXfP8ezW8NyBk_TwfZTUNlCrB6Pok0ulVNa4ne0UsHQXiSnUVOnV0X-DGtz3WvRUJ3tqEFWh93Rj8NZ4I7iOawFnSuSyOGd1Jdpogyo8zLsarhC3vbM4ACiunIo1t_XRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a343c0ae1.mp4?token=UZtShaXJhMBM51QazfJEmDUeMI3XpZcF6pznvXuNhuqt4wpSgJTQs_3aqA258swgH0kRJKbTHCFDhQCWSZnVdjG63CBdWNRHcTfYxb1pYAp3x_6f5T8TvsH24Jb0npFeEripq-NP62fIuig_HxnA0SUz31kOTa_mYejHtI-YSPCkOimXJVgYETu3djurBkPCWg7ofsDuwK2zSs1rXKy6HqXfP8ezW8NyBk_TwfZTUNlCrB6Pok0ulVNa4ne0UsHQXiSnUVOnV0X-DGtz3WvRUJ3tqEFWh93Rj8NZ4I7iOawFnSuSyOGd1Jdpogyo8zLsarhC3vbM4ACiunIo1t_XRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه دختر خانوم 15 ساله به‌خاطر اینکه هر هفته پریود میشده به دکتر مراجعه میکنه تا بفهمه مشکلش چیه؛
بعد از اینکه معاینه میشه، دکترا متوجه میشن ایشون دو تا دهانه رحم و دو تا سوراخ واژن داره.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72709" target="_blank">📅 11:03 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72708">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2aed172c29.mp4?token=XGCf0-KYcGg6nPcCSCFeeksQT7hiW609xlZcOD3nDKN4zMU5ymr-5AolN3wFY_hj1fnqOVQrNXOx_JASxgwyW0UxDd-Fz9LvltAv75jUpayaPYT5Qj1zH5imzx_hfQtE3fAI4NX_d2dQbl93C1cYnND-CW09t2uOgp4jTy5UhOMlCwRkJT02BwlV91Zz8vjXruHPzzw7hdWlWmspV3cmzTDORlb8h5rHrxQlpDFZv2odJkeK8qF6nbul2k0f3NUzGnSTcf5XStgHGRkuatx9-MsK6oyY_7Ikx5g0hQ_b4ZxSdYluVBGXkDIVX8PGrOq5NFwXfGGqgVOgUN0rXKG4Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2aed172c29.mp4?token=XGCf0-KYcGg6nPcCSCFeeksQT7hiW609xlZcOD3nDKN4zMU5ymr-5AolN3wFY_hj1fnqOVQrNXOx_JASxgwyW0UxDd-Fz9LvltAv75jUpayaPYT5Qj1zH5imzx_hfQtE3fAI4NX_d2dQbl93C1cYnND-CW09t2uOgp4jTy5UhOMlCwRkJT02BwlV91Zz8vjXruHPzzw7hdWlWmspV3cmzTDORlb8h5rHrxQlpDFZv2odJkeK8qF6nbul2k0f3NUzGnSTcf5XStgHGRkuatx9-MsK6oyY_7Ikx5g0hQ_b4ZxSdYluVBGXkDIVX8PGrOq5NFwXfGGqgVOgUN0rXKG4Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صداوسیما:‌ حتی اگر بمب اتم بخوریم باز هم نابود نمی‌شویم!
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72708" target="_blank">📅 10:32 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72707">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9499513e9a.mp4?token=ZAWNk7gaPwL9y9HHylk_bCJZCJzpXVCKBKu08zJmlTcd9WMsXRsIW6_LABCUD86KY_sxgRKrMjT3rUxXKqhzkK_Mzhj7LAadL79u4niYGqrPRchOF6UVWONDGYAHWC02N_vTyD6q6-mYq-WUY5sxan-EJnQEa8_vTsiYBki5OULdSCy5bwBkFphM4dl7BTObjzfZ3hAfTWax0OZbDU94asPG3GV1ZOl_0pXIldBZ1eRJHyZzP1TZjpatsZ73vbXfKCb5gyoKHmn0zrPao1ZlBX9khZU9UK0BGaIb1EgSaXRUv4nQVBk-gc18BK-_kbgHJAykIUykGsmXxoFPRBryJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9499513e9a.mp4?token=ZAWNk7gaPwL9y9HHylk_bCJZCJzpXVCKBKu08zJmlTcd9WMsXRsIW6_LABCUD86KY_sxgRKrMjT3rUxXKqhzkK_Mzhj7LAadL79u4niYGqrPRchOF6UVWONDGYAHWC02N_vTyD6q6-mYq-WUY5sxan-EJnQEa8_vTsiYBki5OULdSCy5bwBkFphM4dl7BTObjzfZ3hAfTWax0OZbDU94asPG3GV1ZOl_0pXIldBZ1eRJHyZzP1TZjpatsZ73vbXfKCb5gyoKHmn0zrPao1ZlBX9khZU9UK0BGaIb1EgSaXRUv4nQVBk-gc18BK-_kbgHJAykIUykGsmXxoFPRBryJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه این مدرسه اس
پس ما کجا میرفتیم؟
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72707" target="_blank">📅 10:03 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72706">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8589525917.mp4?token=l0h2uIfOND6NdN_JhuZemfPuAitGiMHmcsqERLaYSACpha_Kgi6zq9O9fNS571a1GDOGR-55uKhuvjA1fXG2p7knEsjPFU172y5CqU7bX42UsZn8DEx0FDe2uAov7LEN4gzv4j0LxWwqnMna0zSLHZQwr-niC487xdVA4kE4r3WWQ2pqN2cCqYaz7p1JS2KKAJjphkb0YJwO5OFKZKzPuCegQ56y1-T1_VCC3fW6QDMCglsWHkmLukP3wXFgL5mK_1R5fI_b5vRu_gGUgRl7ekGgQ7nWw-xVRNGrTMpy4HMEWavBAi0Vu6xyHfIlzsmyhEHaFS5i15jltCTDagDGGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8589525917.mp4?token=l0h2uIfOND6NdN_JhuZemfPuAitGiMHmcsqERLaYSACpha_Kgi6zq9O9fNS571a1GDOGR-55uKhuvjA1fXG2p7knEsjPFU172y5CqU7bX42UsZn8DEx0FDe2uAov7LEN4gzv4j0LxWwqnMna0zSLHZQwr-niC487xdVA4kE4r3WWQ2pqN2cCqYaz7p1JS2KKAJjphkb0YJwO5OFKZKzPuCegQ56y1-T1_VCC3fW6QDMCglsWHkmLukP3wXFgL5mK_1R5fI_b5vRu_gGUgRl7ekGgQ7nWw-xVRNGrTMpy4HMEWavBAi0Vu6xyHfIlzsmyhEHaFS5i15jltCTDagDGGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در بخش‌هایی از کرج، از جمله باغستان و جهانشهر، روز شنبه ۱۱ مهرماه ۱۴۰۵، پس از بارش شدید باران سیل جاری شد و خسارات نسبتا زیادی به شهروندان وارد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/72706" target="_blank">📅 09:33 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72705">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c198c4452e.mp4?token=uBnKc_phbFjSDwsFfcJQjz5s3ZQIIrRlLG1keamHvHWk-exxfFT6ai28ZPhpTvE_d4C211CAU46Mh6RLgMCSnS_6E3EKzAjb2DVa7V29u2Xen-v1sdI9wYZGEBUpCoPrZDuRDW2D5a4HBT55cK9UVbc76JVPIjZXYb5Ifj3fFYp7zR9uYWB6PptOCwbJ8AKIbEKgrJ5HPShEAefxFVwyYM0XrWpoew7INzbTcGD_5BXPDka0n-Qda_yeo4W0PAzosROXiJaVf2wavXH3dIXmGAe8LxfKIFVQDHZuqoRjim6eE0Gvu4Tse9MSB16blXCudTUeNquKf9Qz6l_eqNtl1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c198c4452e.mp4?token=uBnKc_phbFjSDwsFfcJQjz5s3ZQIIrRlLG1keamHvHWk-exxfFT6ai28ZPhpTvE_d4C211CAU46Mh6RLgMCSnS_6E3EKzAjb2DVa7V29u2Xen-v1sdI9wYZGEBUpCoPrZDuRDW2D5a4HBT55cK9UVbc76JVPIjZXYb5Ifj3fFYp7zR9uYWB6PptOCwbJ8AKIbEKgrJ5HPShEAefxFVwyYM0XrWpoew7INzbTcGD_5BXPDka0n-Qda_yeo4W0PAzosROXiJaVf2wavXH3dIXmGAe8LxfKIFVQDHZuqoRjim6eE0Gvu4Tse9MSB16blXCudTUeNquKf9Qz6l_eqNtl1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خراتیان، کارشناس صداوسیما: چین ارسال تصاویر ماهواره‌ای به ایران را متوقف کرده است!
مجری صداوسیما: چین به ایران گفته ابتدا مشکل خود را با آمریکایی‌ها حل کنید و بعد به سراغ ما بیایید
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/72705" target="_blank">📅 09:00 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72704">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72704" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/72704" target="_blank">📅 01:59 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72703">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dvNySk9KxQbMCmBGt8sUm0EPbEt0vNtq0Z7aMACoDgzILYn-w_PUGqJeWQzPd_qe7b5pe5gRkHSsFivoud2LbxcCzWwcg1hBC94zeh57uiyoiBIn9zCYkcHR6w2wCnX6YNCdNzkOzYs2phd5kgJWcyjkbaSXKPdVeOXc764E6CdNKorfDMiql7KiZj85BxT-gkX-G1M0_ONSA-eUnKdKXstovBVk_Bj5ygHs9ji1S20n-2Jql0zuQVQ8eU6fa9z3C8hjTKjBhdQLCmPCeeT9bO-ccay90yV4k5OMNSlSqMlRgVzXkf2cGbIUw3__0P3q-xi_ebZNgfU3Li31CtESPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
🦖
قوانین رو در سایت مطالعه کنید
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/72703" target="_blank">📅 01:59 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72702">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af2d851559.mp4?token=Qkf2igdCOAn-1QuMLtGFjYO_r8x0LuAW5QgMKgthnE35Dwe11gXL_0WkOkr71IcAyhkGaN4gGN-1tvnV0wShYzGmskbflkzoHACtd2IkTp0wmWfWYuNd7ZtdbWIJVKAE7d5vJnlDRc332V9JQ0Gd9m6SJiXNb_uSlr9zhkqBf1RYiPlvRRJlCYm_QZCFub74yxuX0rN7Zmrs37IcPov6Pwt9y9ogO9BN8tXGH0ZStU45sd60eXoXM2c3D74kKg5a8UZOUk7ChTP9KLt9_C4a1dh5MOSg-G2l6QUyCgtY44vIYafX9iCE9-cpTHf2sV3XPi4MaT7Yr47v17XRNEtwnw0a0jvBvuPalxvXt_5PtnFvPeKeuNoEiRvhe0Ht2-HiFwEYqbH7vnMTO5S9ZgFjQYoBimVGFCaUPXaY3mKzOL8S9MOd605vHlFBB7EoBTg3bl_eY3Yh1QEq4YY1E6GBNmhGZaCxKWFiwtCktfFLDB9Pz3P00gPNYy0mQaGH4o-qSX8OtKsqpLssIXs7yV1rywSB6yt-ENRo1dX6qab_nGBOu-KhSpS7Kb4svyLLKjAwzh3byfzcXOeJVf2fwomolFtjDPZC8ZHDArPC6ijJ6FdCjRV3E5Ex4_x7NEhzJo6QomjgnW5nivm4uUCyoRJfLuPawfEoO8q6JQAspC_Quvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af2d851559.mp4?token=Qkf2igdCOAn-1QuMLtGFjYO_r8x0LuAW5QgMKgthnE35Dwe11gXL_0WkOkr71IcAyhkGaN4gGN-1tvnV0wShYzGmskbflkzoHACtd2IkTp0wmWfWYuNd7ZtdbWIJVKAE7d5vJnlDRc332V9JQ0Gd9m6SJiXNb_uSlr9zhkqBf1RYiPlvRRJlCYm_QZCFub74yxuX0rN7Zmrs37IcPov6Pwt9y9ogO9BN8tXGH0ZStU45sd60eXoXM2c3D74kKg5a8UZOUk7ChTP9KLt9_C4a1dh5MOSg-G2l6QUyCgtY44vIYafX9iCE9-cpTHf2sV3XPi4MaT7Yr47v17XRNEtwnw0a0jvBvuPalxvXt_5PtnFvPeKeuNoEiRvhe0Ht2-HiFwEYqbH7vnMTO5S9ZgFjQYoBimVGFCaUPXaY3mKzOL8S9MOd605vHlFBB7EoBTg3bl_eY3Yh1QEq4YY1E6GBNmhGZaCxKWFiwtCktfFLDB9Pz3P00gPNYy0mQaGH4o-qSX8OtKsqpLssIXs7yV1rywSB6yt-ENRo1dX6qab_nGBOu-KhSpS7Kb4svyLLKjAwzh3byfzcXOeJVf2fwomolFtjDPZC8ZHDArPC6ijJ6FdCjRV3E5Ex4_x7NEhzJo6QomjgnW5nivm4uUCyoRJfLuPawfEoO8q6JQAspC_Quvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفنگداران دریایی ایالات متحده در حال سوخت‌رسانی به یک فروند هواگرد «ام‌وی-۲۲ آسپری» (MV-22 Osprey) در خاورمیانه هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/72702" target="_blank">📅 01:49 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72701">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f216caf4ae.mp4?token=FEB4VjVI8dWvq7BZZAItB_NLG-oQylQmN8YEVI0y6E75esrii-4l7M30WMYBAMHJxgdWIzUMgiB1vT5nagmajN4MDVjD7B-cWJIOmEpN0aq1HwfVxfE4ERnG8c-dToUPY2YpgnUCcrthqK6QwTblu8dxFJugE-lybGLhhNOZMxfAAvaA8q6FowEKKhFJZJVttxMdmuM5z5paaWAL3F0GzXSqDlnJ7y3ibJ4e9B9eEgMqRxs7qfvrEn_ciNtKvTohTUcZSYl1LWa-qo9PukD6YpL8m4YcbjM3DR_VOOiRpUFex7Q-5sUg13KKUPEUuvDL8bCv6OCIfU2j1t-auYxq1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f216caf4ae.mp4?token=FEB4VjVI8dWvq7BZZAItB_NLG-oQylQmN8YEVI0y6E75esrii-4l7M30WMYBAMHJxgdWIzUMgiB1vT5nagmajN4MDVjD7B-cWJIOmEpN0aq1HwfVxfE4ERnG8c-dToUPY2YpgnUCcrthqK6QwTblu8dxFJugE-lybGLhhNOZMxfAAvaA8q6FowEKKhFJZJVttxMdmuM5z5paaWAL3F0GzXSqDlnJ7y3ibJ4e9B9eEgMqRxs7qfvrEn_ciNtKvTohTUcZSYl1LWa-qo9PukD6YpL8m4YcbjM3DR_VOOiRpUFex7Q-5sUg13KKUPEUuvDL8bCv6OCIfU2j1t-auYxq1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
ایران نمی‌تواند سلاح هسته‌ای داشته باشد. البته، همان‌طور که می‌دانید، ایران عملاً از هرگونه برنامه‌ای برای دستیابی به سلاح هسته‌ای دست کشیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/72701" target="_blank">📅 00:42 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72700">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e33db7c818.mp4?token=LC0ZuWSgFAERTtLqRqSPdmLLXUb7sPfWtAkLFTJov6x6hq8b_aMkwy1s8BL09AagbRJLCLy8hXD-AK65aesvdgdCsgawbDKTnyU9nrMXRwBRIkhUQuJ1rwrjsK2SroDQ6v8xJ2AILKwgA2uOzWPmKR4WPV1Wyl_XQYDFKYRbUOPSJFSsl2wiv3Zb_VlsvugHlAuXv544ZcKHoEpMl-KDHTLCOoVvfo4rJIkKW_nrN7a8Tr88XlY9FyQnRK3_H2bFUytwPH0-zAdf98iIyf7jp7XULkVm4VHrUySDCvO12GcAQQwJy1GCT4QTdk3iZa8hhybs-hfuZm9sRIRZZFOt0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e33db7c818.mp4?token=LC0ZuWSgFAERTtLqRqSPdmLLXUb7sPfWtAkLFTJov6x6hq8b_aMkwy1s8BL09AagbRJLCLy8hXD-AK65aesvdgdCsgawbDKTnyU9nrMXRwBRIkhUQuJ1rwrjsK2SroDQ6v8xJ2AILKwgA2uOzWPmKR4WPV1Wyl_XQYDFKYRbUOPSJFSsl2wiv3Zb_VlsvugHlAuXv544ZcKHoEpMl-KDHTLCOoVvfo4rJIkKW_nrN7a8Tr88XlY9FyQnRK3_H2bFUytwPH0-zAdf98iIyf7jp7XULkVm4VHrUySDCvO12GcAQQwJy1GCT4QTdk3iZa8hhybs-hfuZm9sRIRZZFOt0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوووری
؛ترامپ: تصمیمی درباره ایران دارم که باید بگیرم. کار را یا به روشی آسان پیش می‌بریم یا به روشی دشوار.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/72700" target="_blank">📅 00:40 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72699">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b62816af7e.mp4?token=R3YxYkpaVpjCR0_W7tsWmovI7li60vmTPr23R96iDeePTXx8YDhYnqAUMxjI1RoeSvwZVQQdGDHER_zrascRJ9wjG5HusxOkEuVsjV_r-z31sEZV6guoabRpExWZrh9ZPLWgaoHjsR-1T2k-w2yahHuPThwU0Cvtksn5dETvHdNIIV099K-QGoAwlisv73OMpHju3RGcVs7QWUR7YXXa4w7NwvFs2UttWhWajQePiqQRK0lNvZz0wexU4RubMIr8_mBonw7CF7KVgRYwlM4X2EjKCwAvz6qE6CKssLEG6B80nmsimgst3JT5B22Z8AJwvS3-I253lajLsDwjeujeSqmg3S6n13naTnt8wlSWMlkZiV5ZBGNDMVfOdGZFQoUrfCvnfta8avEX4_dclDGA2PzksifxO_a3u6VI2TNgaIhLfJbhtN43xkmt3qX7oopQTVq8z2f-WdTToeOaoQoUE9QIUXI9zrBJBocN7mwhXlTzOsH9QJTrCrNgOGw5BFC7sJixFYt4gQwTFoN7x2kqFVoihiLmBqeRGeQNAMtXQioQDpOeCx4X9Kz-VI0RH3ubTXFhu5kd05gGi76FZ1PO6PYiWG8ickqwmcNCCZJRbH9An27C83iLmuObEbIxb_d5Pijt1SSM1CEt6H-3fLkbEnA_wf00HETeLnq_XoHbiy8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b62816af7e.mp4?token=R3YxYkpaVpjCR0_W7tsWmovI7li60vmTPr23R96iDeePTXx8YDhYnqAUMxjI1RoeSvwZVQQdGDHER_zrascRJ9wjG5HusxOkEuVsjV_r-z31sEZV6guoabRpExWZrh9ZPLWgaoHjsR-1T2k-w2yahHuPThwU0Cvtksn5dETvHdNIIV099K-QGoAwlisv73OMpHju3RGcVs7QWUR7YXXa4w7NwvFs2UttWhWajQePiqQRK0lNvZz0wexU4RubMIr8_mBonw7CF7KVgRYwlM4X2EjKCwAvz6qE6CKssLEG6B80nmsimgst3JT5B22Z8AJwvS3-I253lajLsDwjeujeSqmg3S6n13naTnt8wlSWMlkZiV5ZBGNDMVfOdGZFQoUrfCvnfta8avEX4_dclDGA2PzksifxO_a3u6VI2TNgaIhLfJbhtN43xkmt3qX7oopQTVq8z2f-WdTToeOaoQoUE9QIUXI9zrBJBocN7mwhXlTzOsH9QJTrCrNgOGw5BFC7sJixFYt4gQwTFoN7x2kqFVoihiLmBqeRGeQNAMtXQioQDpOeCx4X9Kz-VI0RH3ubTXFhu5kd05gGi76FZ1PO6PYiWG8ickqwmcNCCZJRbH9An27C83iLmuObEbIxb_d5Pijt1SSM1CEt6H-3fLkbEnA_wf00HETeLnq_XoHbiy8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیت هگست، وزیر جنگ، درباره ایران:
ما از همان ابتدا اعلام کرده‌ایم: ایران هرگز به بمب هسته‌ای دست نخواهد یافت؛ تمام. این موضوع، یک منافع حیاتی ملی برای ایالات متحده آمریکا محسوب می‌شود.
ما این مسئله را در جریان «عملیات پتک نیمه‌شب» (Midnight Hammer) به وضوح نشان دادیم و در «عملیات خشم عظیم» (Epic Fury) نیز آن را آشکار ساختیم.
ایران می‌خواهد با مسائلی همچون تنگه هرمز بازی درآورد؛ اما کنترل آن در دست آن‌ها نیست، بلکه در اختیار ماست.
آن‌ها عملاً هیچ چیزی به دست نیاورده‌اند؛ چرا که محاصره ما آهنین و نفوذناپذیر بوده است و ما هر شب تقریباً با همان ظرفیت‌های پیش از جنگ عمل می‌کنیم.
ما احساس می‌کنیم که در موضع بسیار قدرتمندی قرار داریم. ایران باید تصمیم درست را اتخاذ کند؛ در غیر این صورت، رئیس‌جمهور ترامپ تمامی گزینه‌های لازم را روی میز خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/72699" target="_blank">📅 00:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72698">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6316faf3f3.mp4?token=rvU-iHxwHaoiGjHkMuk7lfDUoz6bCDFOFoWYu5x2Ff5u3HNcBCBO9bS5XYAKAtrFewUzU89lf5aLPjAz9YzDgVOnbWEorzydKQ2coor0V1R93PCWKeWXQ34rN2r_BLYl4pjkwXxXzoQ6oPaFiQGCfzKAjeM4LrZlcpy0Wn2aNBbSnmIWIINXZXK6Jlp32NwQ2w4ZW_CctySowDxIdhxdGiVcZV1FnBTcSuej7JYc2EX6GOENCvobk9xB3gzHqPUcZfiLMjPcLTHy7l_iam1NWqOhq66Av7SkUpKa1D1O9q7UqlAqcb4b5jgyOy5rboN9ES2MjQ9sbogeb4-itzDOPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6316faf3f3.mp4?token=rvU-iHxwHaoiGjHkMuk7lfDUoz6bCDFOFoWYu5x2Ff5u3HNcBCBO9bS5XYAKAtrFewUzU89lf5aLPjAz9YzDgVOnbWEorzydKQ2coor0V1R93PCWKeWXQ34rN2r_BLYl4pjkwXxXzoQ6oPaFiQGCfzKAjeM4LrZlcpy0Wn2aNBbSnmIWIINXZXK6Jlp32NwQ2w4ZW_CctySowDxIdhxdGiVcZV1FnBTcSuej7JYc2EX6GOENCvobk9xB3gzHqPUcZfiLMjPcLTHy7l_iam1NWqOhq66Av7SkUpKa1D1O9q7UqlAqcb4b5jgyOy5rboN9ES2MjQ9sbogeb4-itzDOPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدت زمان حضور رهبری تو جنگ:
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/72698" target="_blank">📅 23:53 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72697">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26e8309253.mp4?token=hKajEJy9oumOjRKLg-mfi-0uITXoqkZsAn9r6ngvVKMuwqBe8-JgSMEcHEvZhXmoXl-9fZtRVoprtzm5QRabZuFxjh7OS7G9K94p30KkkXC6CWnKk5ThtvTwM_KzkhWJ4K8eeQZ-0xYCqzc6GBqmZN0oy7VbPqAUMFkDsSN9SuhMgo5SYUWy5fh3acHR6-s_-0qTkAs3tVJXGby0ZXKKc9ePT-GjD1W1Y8XQf6GzyoyDqs86Ql6MM1ViCaRTiUtGkBKxAQQVRQoFTbOR_hcUzHAqN1PAsDayXaX6rJivMjSYj-Y4okzh9qUupO89ga277klnqL71R_ZkODtBRUSo5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26e8309253.mp4?token=hKajEJy9oumOjRKLg-mfi-0uITXoqkZsAn9r6ngvVKMuwqBe8-JgSMEcHEvZhXmoXl-9fZtRVoprtzm5QRabZuFxjh7OS7G9K94p30KkkXC6CWnKk5ThtvTwM_KzkhWJ4K8eeQZ-0xYCqzc6GBqmZN0oy7VbPqAUMFkDsSN9SuhMgo5SYUWy5fh3acHR6-s_-0qTkAs3tVJXGby0ZXKKc9ePT-GjD1W1Y8XQf6GzyoyDqs86Ql6MM1ViCaRTiUtGkBKxAQQVRQoFTbOR_hcUzHAqN1PAsDayXaX6rJivMjSYj-Y4okzh9qUupO89ga277klnqL71R_ZkODtBRUSo5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#مهم
؛
سؤال: آیا ناو «یو‌اس‌اس روزولت» قرار است جایگزین یکی از دو ناوی شود که هم‌اکنون در آنجا حضور دارند، یا اینکه قرار است سه ناو در منطقه مستقر باشند؟
هگ‌ست: سؤال بجایی است، اما من هرگز به آن پاسخ نخواهم داد.
ترامپ گزینه‌هایی در اختیار خواهد داشت؛ بگذارید این‌طور بگویم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/72697" target="_blank">📅 23:03 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72696">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e6961bcdd.mp4?token=eCNU9cCvkc6zlBJTMnj6aRWaVFY1R_nK56PJfwgS0hhjWS8b-7OtJ5HdiEbOo--VZ8c0_ohI8LnnOEzMFAqzUPZULEq8gm_g9C4aLQhvb666YMU2iIYre5LXIBe5V2pYzEARgwb0lSkKmTC5VxuA4sI6azpR1nq-qL8-4E4xpOJreDMD6aSIfzRTjqs5c5LizVEb7wR2Koki3UVlj6wSmpGd2O5ZttQG6onClJSAnYa7QFfrD1WdZaFaiFPUivlvVddG819zNp7L4YMw0Czij-p6JapvV_EDPIHyLDDhAmyPWGh5hme2HHLrDKaoYXL0UZ-Ibo81a2vodpA8CkviwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e6961bcdd.mp4?token=eCNU9cCvkc6zlBJTMnj6aRWaVFY1R_nK56PJfwgS0hhjWS8b-7OtJ5HdiEbOo--VZ8c0_ohI8LnnOEzMFAqzUPZULEq8gm_g9C4aLQhvb666YMU2iIYre5LXIBe5V2pYzEARgwb0lSkKmTC5VxuA4sI6azpR1nq-qL8-4E4xpOJreDMD6aSIfzRTjqs5c5LizVEb7wR2Koki3UVlj6wSmpGd2O5ZttQG6onClJSAnYa7QFfrD1WdZaFaiFPUivlvVddG819zNp7L4YMw0Czij-p6JapvV_EDPIHyLDDhAmyPWGh5hme2HHLrDKaoYXL0UZ-Ibo81a2vodpA8CkviwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند روز قبل تیک تاکرها باهم دعواشون میشه؛
چندتا دختر ریختن روی سر یه تیک تاکر به اسم ستایش و اینجوری همو کتک زدن:
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/72696" target="_blank">📅 22:30 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72695">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4df7e241a.mp4?token=oicen18SolTbHTZIZC9e9S9IHykfGhaX6FIBGfLaFCl11idsiSO-ahx9PTXJODTMfGLbfgn7eT_c6tnDjCA4Pn6MKXTsgOGfG8rdRnhbYzz293H5U9b628aPJi1SoULU2dWaGNoib5gZHvrE1eGajSLkKgpAB_quwpXSKDuFbea4YHEU9Lqr-9RlzwPv1ExSY1iiqU8R6RsFTHwNy1AlmO0HBv6Sr3MdVCGV3PRYukWQdLXl2WqYOdaWNBR_MvvxfjRk3miLRiwUK3smxesSlLPJxlbZsnQvnT85OKEjEePKvy5S5b8k8X8Fh_xziPbqarxOVecANqV5ePCGOJEKDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4df7e241a.mp4?token=oicen18SolTbHTZIZC9e9S9IHykfGhaX6FIBGfLaFCl11idsiSO-ahx9PTXJODTMfGLbfgn7eT_c6tnDjCA4Pn6MKXTsgOGfG8rdRnhbYzz293H5U9b628aPJi1SoULU2dWaGNoib5gZHvrE1eGajSLkKgpAB_quwpXSKDuFbea4YHEU9Lqr-9RlzwPv1ExSY1iiqU8R6RsFTHwNy1AlmO0HBv6Sr3MdVCGV3PRYukWQdLXl2WqYOdaWNBR_MvvxfjRk3miLRiwUK3smxesSlLPJxlbZsnQvnT85OKEjEePKvy5S5b8k8X8Fh_xziPbqarxOVecANqV5ePCGOJEKDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه اخوند تو تجمعات شبانه: در پیروزی ما توی جنگ و ابرقدرتی ایران تو کل عالم شکی نیست؛ الان دعوا فقط سر میزان ابرقدرتی ماست!
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/72695" target="_blank">📅 21:56 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72694">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7af7d5f80.mp4?token=NGT9JZldAIbdIXy_7-WbklKloserPTkr_-u5__cHl5ExiZBx_G7P5YPUmyJbYHHy4AMh35rlnSH_8Zd3E2h6GgX8DEA7Y-8T3N8KBwBD2UAejtwMYatst36e_0vS81XkJjWWSP1OjpyZsst0EcT-x_rEOK0BEfzETpqnjMTgT5CPuEAIitsVXGjBCuXg-4olerIuX7fh49HtyQjxTTt6g6folD5eCLHieWKQcvdh5qRE_9Wb-47RcUR6gGvfp6FUP6FQBH5EcWESeAdxoq2JV2IC8rMFa5hQcOuHHtHpUnIZ4VouZelGuttfbrq9n9GveaAmfqy0hvPd1Q51DdFCeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7af7d5f80.mp4?token=NGT9JZldAIbdIXy_7-WbklKloserPTkr_-u5__cHl5ExiZBx_G7P5YPUmyJbYHHy4AMh35rlnSH_8Zd3E2h6GgX8DEA7Y-8T3N8KBwBD2UAejtwMYatst36e_0vS81XkJjWWSP1OjpyZsst0EcT-x_rEOK0BEfzETpqnjMTgT5CPuEAIitsVXGjBCuXg-4olerIuX7fh49HtyQjxTTt6g6folD5eCLHieWKQcvdh5qRE_9Wb-47RcUR6gGvfp6FUP6FQBH5EcWESeAdxoq2JV2IC8rMFa5hQcOuHHtHpUnIZ4VouZelGuttfbrq9n9GveaAmfqy0hvPd1Q51DdFCeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو بمب‌افکن راهبردی رادارگریز B-2 Spirit نیروی هوایی ایالات متحده بر فراز محل برگزاری مسابقه تیم‌های نیروی دریایی و نیروی هوایی در «کلرادو اسپرینگز» پرواز کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/72694" target="_blank">📅 21:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72693">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/24bef6628d.mp4?token=DNVytZz8Qfk-imWIfVQ_-fSkZCR7NgPriaS1FJmen7mVPWvDRE4g4kNmdYlstfcnhS--fKzsqve2Cqf19RGxTXGd1CoFg7ARJXOl0OGQcgH6SRD3UpeWae8iUufMaUYouSxjCM9zYJiQXuKuW4wJ6tav8TYKtSIfx0uVKPEN9GNaYYEVdLvzAcqbjx2EZZmBELvWamUUugLZOA6F5nZj4Pp6iZHJ-ONV6QXebg0UqCVZ32b-qjw5M7CdQqM63Gpl_4yVpGUGViTQFc8AYcdqYB8oDf1LSHK8q9_PiuTB6zvtWPK2EugIvvRd_o0_IKtNGcVS4j3NV5EL8qdQnL6LPw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/24bef6628d.mp4?token=DNVytZz8Qfk-imWIfVQ_-fSkZCR7NgPriaS1FJmen7mVPWvDRE4g4kNmdYlstfcnhS--fKzsqve2Cqf19RGxTXGd1CoFg7ARJXOl0OGQcgH6SRD3UpeWae8iUufMaUYouSxjCM9zYJiQXuKuW4wJ6tav8TYKtSIfx0uVKPEN9GNaYYEVdLvzAcqbjx2EZZmBELvWamUUugLZOA6F5nZj4Pp6iZHJ-ONV6QXebg0UqCVZ32b-qjw5M7CdQqM63Gpl_4yVpGUGViTQFc8AYcdqYB8oDf1LSHK8q9_PiuTB6zvtWPK2EugIvvRd_o0_IKtNGcVS4j3NV5EL8qdQnL6LPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی از سیلاب شدید امروز عظیمیه کرج:
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/72693" target="_blank">📅 21:06 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72692">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">به گزارش نیویورک‌تایمز، مقامات بریتانیایی و آمریکایی معتقدند افرادی که در نزدیکی پایگاه نیروی هوایی سلطنتی «فیرفورد» (RAF Fairford) دستگیر شده‌اند، با عملیاتی تحت حمایت ایران — که یا به سپاه پاسداران و یا به یک مرکز فرماندهی نظامی دیگر در تهران مرتبط بوده…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/72692" target="_blank">📅 20:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72691">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jEWMe20hsjC5oC7MEIcZOIsTSLZlR2EYZSqx7YU1L6EIaP35twVoqNT2tO5eta-PLTIk9v-E6iFpwNbOZ9tiz2Yzs0K16OZ-77l95a8XY-RMCwM4Qrk5dESwBA80NWVGgwTtd9oGkxaGj2DxvYExlSJ65-tEhfjE1hEY5FBmg3m_J5iRJKA_4XBXV_nPfMU-LIpiBTPgLuASVvpvs0WeHNvt93tjx-PKKol_uqObMU6AHXyrGgt8rqMzlH0kZZ6fgj_wsBMTruQaZZpV3zIh6lXSJ-Lr5FSATDB0GzyPaAOTK25qQ2xJD2dLzggdlxoVx5arK_9m8Zsa_aOW7kyJdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش نیویورک‌تایمز، مقامات بریتانیایی و آمریکایی معتقدند افرادی که در نزدیکی پایگاه نیروی هوایی سلطنتی «فیرفورد» (RAF Fairford) دستگیر شده‌اند، با عملیاتی تحت حمایت ایران — که یا به سپاه پاسداران و یا به یک مرکز فرماندهی نظامی دیگر در تهران مرتبط بوده — در ارتباط بوده‌اند.
بازرسان در تلاش‌اند تا هویت فردی را که این افراد را به خدمت گرفته، شناسایی کنند؛ کسانی که یکی از مقامات آن‌ها را «افراد ساده‌لوح و بی‌خبر» توصیف کرده است.
با این حال، مقامات اذعان کرده‌اند که جزئیات مهمی از این توطئه ادعایی همچنان نامشخص است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/72691" target="_blank">📅 20:18 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72690">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">دونالد ترامپ به تمام شهروندان بزرگسال ایالات متحده وعده داد در صورتی که جمهوری‌خواهان در انتخابات مجلس‌نمایندگان و سنا پیروز شوند به آنها ۵۰۰۰دلار خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/72690" target="_blank">📅 19:56 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72689">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a49047dbc.mp4?token=H13V44NoUsl2gehIE6YjTum7zNZX6erH4BE9XkmKMfyaHyNmphbuNOMyqA09jMNV3hLd9jap0Ar35DJDNnsmu605JQA8JVcZc0pwmtQyi15bEo7Trhf7Hm8fmcnNVGnWAzE4hrX73TWmY1zoCvmIAIY5dXWIYM1N3l_WsPtua1leipeb4GoHnAH8q2bv0BhMa1PdFf6W-l_Qc-qSsqWrtm4hbQwIWvEra5hmZelSRoEE07JB-RkYVRb5rdHMlDRG0IWPAWx3xvsSg-lvRBVvz2zdkSDMtxVrWJIoj4B_D9bVvBDXpRtuh-LU81c0zSXVJ5vMxwR01YCY4LowCoLcx1q7bc_vuQVIVLocgvu0kxvPdAm7jP7jZhpXHvZRq_C4SEPTgbvwzzLMg9Tq3DNVrf1obu1Dcb4LoZ3B_NAQKMZGw8rCbU_PHT9B2hCF4OcCs9zBlw3UIrDaugjoTsUSEfSI7tb3WZ_WgEOzduOcZ7wZjkXV2ajbSqnV5_h5iUSeNfXmUOETsRMwzAHTpoAoqtJz-Hh2RkufAGEpgoa-VoQJ3Wi4nwl3iU0Zw3SrcX2oJXvMqTlGHfkE-obtogx_EaIj74qQKYxGDNw_LeMMV_FHCM8VOi-qa2xHzcMs2eAGElFt_IF3v8KFBOsCOKN41dmGqVCZr5idUG8o45L__Vs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a49047dbc.mp4?token=H13V44NoUsl2gehIE6YjTum7zNZX6erH4BE9XkmKMfyaHyNmphbuNOMyqA09jMNV3hLd9jap0Ar35DJDNnsmu605JQA8JVcZc0pwmtQyi15bEo7Trhf7Hm8fmcnNVGnWAzE4hrX73TWmY1zoCvmIAIY5dXWIYM1N3l_WsPtua1leipeb4GoHnAH8q2bv0BhMa1PdFf6W-l_Qc-qSsqWrtm4hbQwIWvEra5hmZelSRoEE07JB-RkYVRb5rdHMlDRG0IWPAWx3xvsSg-lvRBVvz2zdkSDMtxVrWJIoj4B_D9bVvBDXpRtuh-LU81c0zSXVJ5vMxwR01YCY4LowCoLcx1q7bc_vuQVIVLocgvu0kxvPdAm7jP7jZhpXHvZRq_C4SEPTgbvwzzLMg9Tq3DNVrf1obu1Dcb4LoZ3B_NAQKMZGw8rCbU_PHT9B2hCF4OcCs9zBlw3UIrDaugjoTsUSEfSI7tb3WZ_WgEOzduOcZ7wZjkXV2ajbSqnV5_h5iUSeNfXmUOETsRMwzAHTpoAoqtJz-Hh2RkufAGEpgoa-VoQJ3Wi4nwl3iU0Zw3SrcX2oJXvMqTlGHfkE-obtogx_EaIj74qQKYxGDNw_LeMMV_FHCM8VOi-qa2xHzcMs2eAGElFt_IF3v8KFBOsCOKN41dmGqVCZr5idUG8o45L__Vs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیت هگست، وزیر جنگ:
مرا بفرستید تا با «کت‌قرمزها» (نیروهای بریتانیا) بجنگم.
مرا بفرستید تا با کمونیست‌ها بجنگم.
مرا بفرستید تا با نازی‌ها بجنگم.
مرا بفرستید تا با اسلام‌گرایان بجنگم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/72689" target="_blank">📅 19:30 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72688">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bc7b08156.mp4?token=FcyvqnSWSi2G_W4bzF5eWXG_xg_5IwAWGl7WPwNz9ARn6L63ceJ3QxfTmrDFC6he5ohxoqHxYYjWHhzzng6_2Zz4hcPfHmHmuh25poXViaIf-5Tr2CzPxmpEJZ6QW4E6TMYCjOjI61BB9XJliphJv8aXraBFmrmEArnDLWAdumyACog29Tdfi9xenZBBOtPLG6JnRrt3EIERhj2HmLvPVybW4_IJw4ViIBAvfDrc0Psb0KO-uvUxd0Q_LmBGmri3DUGu4VhnWNRDPOI2F750iJSYYIKsXi-ap-GXw27koO79rfgNi6vmmJFVtSSSEViHdfgOtYaShtOqCT-bUNbOrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bc7b08156.mp4?token=FcyvqnSWSi2G_W4bzF5eWXG_xg_5IwAWGl7WPwNz9ARn6L63ceJ3QxfTmrDFC6he5ohxoqHxYYjWHhzzng6_2Zz4hcPfHmHmuh25poXViaIf-5Tr2CzPxmpEJZ6QW4E6TMYCjOjI61BB9XJliphJv8aXraBFmrmEArnDLWAdumyACog29Tdfi9xenZBBOtPLG6JnRrt3EIERhj2HmLvPVybW4_IJw4ViIBAvfDrc0Psb0KO-uvUxd0Q_LmBGmri3DUGu4VhnWNRDPOI2F750iJSYYIKsXi-ap-GXw27koO79rfgNi6vmmJFVtSSSEViHdfgOtYaShtOqCT-bUNbOrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیت هگست، وزیر جنگ:
اطلاعات نادرست، اطلاعات گمراه‌کننده و تبلیغات عامدانه‌ی بسیاری پیرامون ناو «یو‌اس‌اس آبراهام لینکلن» وجود داشت، اما ۸۰ درصد از کارکنان آن گروه ضربتِ ناو هواپیمابر، برای تمدید خدمت خود اعلام آمادگی کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/72688" target="_blank">📅 19:22 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72687">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cee4b7ed20.mp4?token=vtUR1HbiJJ1JKLcIa4TXTGRK1fPf0dGPXJ8EkvNukO996p5_BRIMyYqageu9RzhSN8npB5Ci08uOZQMkTRWbRDyDnQ2hX6c7bbKlxkKQ4c3gzkHyiblM8kKWNYN_PrxXwI_6OrUEe4lB-lgk0t8usqnr9VZeYWzfv3rH9ziSs-kGJro7FrOziRfHZdpgKiXcHPXBesKw4t3hxKdd7vmHrFKewYZzIbfZB-yPpX0h7HnYNGPYO95QzBuhBwrOkd3uCvWr5sNC2fY8Ug1P-rxE1uyKw8Y65Lo__eUMoq2yZ3FqRS0mM8EMLiOKjsWBXnoUBLnbBhXnqQ7Bbzdtc_mqIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cee4b7ed20.mp4?token=vtUR1HbiJJ1JKLcIa4TXTGRK1fPf0dGPXJ8EkvNukO996p5_BRIMyYqageu9RzhSN8npB5Ci08uOZQMkTRWbRDyDnQ2hX6c7bbKlxkKQ4c3gzkHyiblM8kKWNYN_PrxXwI_6OrUEe4lB-lgk0t8usqnr9VZeYWzfv3rH9ziSs-kGJro7FrOziRfHZdpgKiXcHPXBesKw4t3hxKdd7vmHrFKewYZzIbfZB-yPpX0h7HnYNGPYO95QzBuhBwrOkd3uCvWr5sNC2fY8Ug1P-rxE1uyKw8Y65Lo__eUMoq2yZ3FqRS0mM8EMLiOKjsWBXnoUBLnbBhXnqQ7Bbzdtc_mqIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگست لحن و رفتار ترامپ رو تقلید کرد و چیزی رو که ترامپ هنگام پیشنهاد این سمت به او گفته بود بازگو کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/72687" target="_blank">📅 18:36 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72685">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdd7350ab9.mp4?token=ZF9tTykpkh1GRl1qlZfhZvFYpuNAjmezC7KsnFgOznVVI5-Qjirnz4cNsPry_pKHQIMJzSu7uxF0HgqbecNVyVpMZhZ3xAkIv_5ET9asKIj65joWjNj771MN5BjIuhwa00uYOAaQ14ZVsr3dcXiEiHRXYrzN6a0y_XilZKl56bCODgS27tMn4s8W1vi8QurY2-0pFkRw34sCbGg6tyh25bFF5wRehOlfmtEOy4aSxxBKyEtCH9k7dTWrS-DnWyina2nTODxr-mKf0Ma8h-_H77KQ83-UM30SG21OwYh_yV0I-wdo69VA_McxBhlCDr4SdSJqMKC99ZGRBEcoAAGU5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdd7350ab9.mp4?token=ZF9tTykpkh1GRl1qlZfhZvFYpuNAjmezC7KsnFgOznVVI5-Qjirnz4cNsPry_pKHQIMJzSu7uxF0HgqbecNVyVpMZhZ3xAkIv_5ET9asKIj65joWjNj771MN5BjIuhwa00uYOAaQ14ZVsr3dcXiEiHRXYrzN6a0y_XilZKl56bCODgS27tMn4s8W1vi8QurY2-0pFkRw34sCbGg6tyh25bFF5wRehOlfmtEOy4aSxxBKyEtCH9k7dTWrS-DnWyina2nTODxr-mKf0Ma8h-_H77KQ83-UM30SG21OwYh_yV0I-wdo69VA_McxBhlCDr4SdSJqMKC99ZGRBEcoAAGU5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت آب‌و‌هوای قم رو ببینید
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/72685" target="_blank">📅 18:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72682">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/h47xTHM2ElnshdtblfHi_-TqE6HlRLdig2S0hiMey1vwFbE9UK3RQ39h6lIcDeM3Xom_mSvxNyAg1d53KPGZBnUMyPZ4YahJrCE-IteW9wsq5SQNh2MKjLquJ59kGUuWjRV__HBlY4tngwPgBPhOKIYbjcXYBj-N3cDOVMn7ewQLyYxaxHIXMRzhxVOVi0mXh3KeOpsxQKtXgrmgs9QWYRTQh2bMnrEsWA-aXGBHnTBWy7X-MCs5t6GYIYuL-sgMwCJGDjYazqTggtAgxvBnissStgZCkiLfoGxCPQ49ENNDAj4Ec0LUKO78PzsEgE6Qrm4Bs9DulSBV56gTevpiaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VvxonarrVvwoUUOBYROYniCBqaOtfQ-QU2-uBLSS-lG3r_MN4Dj3ZZ8nTgNtb9RCBoGJoy9J0-wz2cPYJDXaVp0tHsJpiKKF_rUo0SDZHG7ekg0aORimXLfxgwKgrieNnq6RcHro-yTbKxmuGgqgX-PWmv_7on72QKmdfedb9G6GOydRhcreviDOZl9HiNxk3md6W7DLGQLJzvBOIuj69W5ANeC8KmRTep_swi8UmJ54zpsFsz6dZOkPSBfvpY5nFjREls0D9jKr1rY5181HwK0SIvgDayFuWM1TIBDohTC88LbK8FL1RYz_zvmCdxUINCawiQhnfZvlV5klX9K8kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/R1WUHVhK9zPfv3wHM__KklvW5yvlpltFdnXjDpcPo57vJCwmdnYuXCOWRAtJ7BQcO3vcN9_aelRwqnMDL5Fw8ewUg90NsgIJ2zl4B0Gvnog_PDliLJLhS-6fsW-qUTVwfiUcOAtEVAbtStA3gG5AeBNEpWNQIHgct6Q3SmQM4iBC-TV6-43_4wR4o_JJYcZFC_q5Djm3nwjf9fD2gaderGAbWBHiuU1Zj7eBL0pwiD3ClHFHqnrnXqnL7Xkdhm_6XufKCypSpvRcC23glzT6PykitiXvo8xRA4ycEnCy4W56L7L6oisxvEWf-puwTZg7W9gIdmh73t0jv7Z-v5zZ_Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ایلیا هاشمی:
ساعت ۱۶:۳۵ شنبه؛ ابتدا صدای جنگنده در قشم شنیده شد و سپس یک جسم مشابه با بدنه موشک، داخل شهرک بوستان قشم
سقوط کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/72682" target="_blank">📅 17:57 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72681">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72681" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72681" target="_blank">📅 17:57 · 11 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
