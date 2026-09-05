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
<img src="https://cdn4.telesco.pe/file/fK9E2iL09PAcfkBnyrTi4PSNrmDCnb6pBZolFUEdYxRLFkQVg5xVmPK4Ab0-PgcqjBDnhSO9aL1iMsLOzNRF7kp7iCgpebXVMz1GubhEmOQOIjIf4oMLbWH_g_VGM0iMHXByNIapYX49KnM_5mXVEssh8T-Ph50pfQ6Twjg5z4Kk2wOSkfzeFtoYltdQ1aQ3j5lpi3BysBLpOxQh0jU83AFh_DAXpj0BJfDLv3k2MYTbYOfQHvVG_7sYVdnwgbsz8wRpd4UOoOsfgf4cvXNe2cqWbpkY3G0sqtTq2LpQxPZk6saOrrBFNBZOyJhdONF12aZ3j1A0x7KgOU5UZf-DmQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 605K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-14 14:49:11</div>
<hr>

<div class="tg-post" id="msg-29101">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HrRN1aoF4QRFzU2btr8ZESIigV4i4M2sWXUfeA5jKehMLq2uQEAXQbRB-zIsiylgYefjucPG8sFv6_g1w0a4QZ8k8mEG6YGVgvSoWXTn3KIpBnC_NLxk7LdSB_uu0cjcvPyWK7q5oA4e7gE0I2PEcFNOceNJcmJa9dGgyn1aW8X4bYxtbAacMtc-zDmK1vp6JCYM02B-sdUg73IZ76fE5ybP-0I_Hq6MLu4y1ZqGNtdluGv1orCvWOiloRXd468-zNriBYdI62kYp6ZFnKRwGsM9zK-8kxo6t9jP8I6-L6ph-89KtwAmc5_s7hHZ0mpl0gTWgB-uE-x_POxqt2xN4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌رسانه‌پرشیانا؛ صالح حردانی مدافع راست تیم استقلال بعد از دیدار با آلومینیوم به تمرینات آبی‌ها بازخواهدگشت و کنار گذاشتن او برای همیشه توسط کادر فنی آبی پوشان صحت ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/persiana_Soccer/29101" target="_blank">📅 14:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29100">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pMBSmK1qO5Kvb5lgx3F6sysW6PdY7pbX1b9fjAphnh62_N3XcpFtusDF6fiStpkG4NnWPGgws02Y5pHRuh9PBHyIGs4Fs_iiqWeCxeHa69Qt2jx3d24gtyK-Fos1ep_uf4eFHiYrcIaTk4pTsB3SlRZtQUa9PYeXeCPHYDzAfRHizapNKFwh-mMa2f_jXwWJbnuMKCLlYw2AgAh8PLvlJaWMKFodjl2tH1_Zid3dpZyzg522ZFppDFQLupCZ0d1PBYPoApE7RY6NdOmNS2qxtwIcVaFmcgLXlfMQK6v5xXE4A-x82ea6T30FCRnxceHU6ErarwSl6bCFDQx_TgGqKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
همانطورهفته‌پیش‌ازتغییرات مدیریتی باشگاه استقلال خبر  دادیم و امروزهمه رسانه‌ها این خبر رو پوشش دادند. حالاطبق اخبار دریافتی رسانه پرشیانا؛ مالکان باشگاه پرسپولیس درپایان‌نقل‌وانتقالات قصد دارند تغییراتی در مدیریت سرخپوشان ایجاد کنند.
🔴
طبق‌شنیده‌های‌مو…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/persiana_Soccer/29100" target="_blank">📅 14:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29099">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WFd8RE17VbsAEIaIpIaq9gedMts79L09eI4CZM8He0ehfJOqdw12veZFXcq46UDxJ17NwV3ODw9d07xeL4agQaxBdOIi-JqMnd3wDXfVVOgLX2sS2Q0eAAFOjIOZXLGZZIssIMPkoAp2WuU54aXXd-nvZpg_K4OZk_syTYCcChKKMk55fZg82L2nQWmipNSWkFlHOHUAV5nwUtKlMqwlaEFZNSP1-SSh2orF6rDVV-dv8uIMKogymZIdCOZu75kRXi5fLCDJOftaAh3tGX1-ZmoYVG2VqpKeaaAruEkM4qKpAf9LBstmDQr-ib4aPxvEybG7j3APUXOPhO8UPMfP0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
ریکاردو آلوز ستاره پرتغالی سپاهان تا اواخر هفته جاری به ایران خواهدآمد و در تمرینات سپاهان حاضر خواهد شد. او مشکلی برای همراهی طلایی پوشان زاینده رود در لیگ برتر نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/persiana_Soccer/29099" target="_blank">📅 13:41 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29098">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yp7XI74rxJ9Lc-LsoyZDm1YVeA4G8nuFPxcLIBDhDSSh2adAXIKAyXSfaR-6NngiVecR9xTcIQh_NAh8mWfKuEpOqYshUcLHQJzpSWEOfYZ1fSGsttr6TxfobKIMeKIZrMf-4lgGCf-0BO7XHjZxYU-PISzGv30C8n9kzVdM-RrDSbp44zhysAKXTPoUHNuSus3SXHVGdoqR0MhOgtOyxHlnwgggZeepK5AHHBNKsHEWZ7lVnNylftbmk3yhPt762tw0SMz6770-0_vDbhXrkA4LtDNxbwJv0d2bqDomAt23a3-WN2tNm6RrOqb7k3D_GOCdPwomDN1q9BKrNgF0Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ سهراب‌بختیاری‌زاده سرمربی استقلال به سامان تورانیان مدافع‌راست 23 ساله این‌تیم برای دیدار با آلومینیوم اراک آماده باش داده و به احتمال فراوان حردانی از لیست آبی‌ها خط خواهد خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/persiana_Soccer/29098" target="_blank">📅 13:16 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29096">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MrDLGju7TEh3LWn_SdKWjgrxj3oeiRymg_6okDX3syRncVRhDs1UU9EN5U2gFbWSezVM9Qp0ifyW8y59zXej8T2WRUMCfKNRV6ldBv3C45mNhnhf50BYQod9ItLi1oxlYGHaup4leLC5H2rptwP_rGLiuT5QVqlPn9ncbJFtFXvovX08cUkioayF_qAbrYhggH40GsVH4q6oh_XxDILorc86rR-bQ8eP2LzdidyygksKjXzV_JjhxOmvCEfb-ss-oY-Vl7XuXRV57csWPMuacfOk31Mx7-1Iu71BhzYt_P58co31K7Yc77VtzH71M4W0mXmv232st5fTshqPvTyHaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uhnzDyrgfACZsLQTLTsxBYQ7047zzZnITE4DmVfp2ngSTecLVYLLQBEuv2aIFNeQyC4se9XRYltxxvjA8ryl9ZlLHhQih-1cRFFqhYjcpGJMFw62FjqmyCRGXgArVcCB5tEoG4ySVumQq7y9v1MTbRRh5TF_nt3K-J58hvGD_voR8TN71qeUHVc058xhe0rh7SyrO6cQuMitKSDx75tUNDwfVeBwZevMk9uFrOTVc2D44r3viywKuO65u2LlzokI4AQiMuGk0ReaAA4hjBrsVy92RHlNr4KvgR3vZeu4414Vd35OZHffh1l8BFa51kGgJJeXmSMNPVkYPNkg9MNJ_Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
دوترکیب‌متفاوت از تیم منتخب هفته پنجم لیگ برتر بر اساس نمرات سایت متریکا و سایر رسانه‌ها. بازیای‌هفته‌پنجم امروز شروع میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/persiana_Soccer/29096" target="_blank">📅 13:00 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29095">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VxsPp5cIEG9K2MUADSx-jihMd1AuDopsrSKOSYP6B_Uw3nkgWFU7dcXeh-Wur36sd6BA1TjbB6UpdYQIR1_Z5dlCP64YDK6Vgylm51PoyX03aZ2BcfOKQ9sVMgBXi-Qw_v_o9e0T87RqfgUEkX8XgEsjF2cv9HRNcIwg0rHIr9hMf6iBWXEugEx1z3DDH9pP8vocTdlPEN7ouav2tqcFI9uHMsEgi-JGqZVUWYAoc8wlCmAcVSFoOL6GaBoNkSyorGUqwMy0Y9pb_oApRAbuuRLVZhyfnaD0ptp_jrUF0q8GTNiInojnE225Bo0Fm3pEiuZv8ZuwMmMVkF6pVQkBuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویدیوکامل‌قسمت‌اول سریال جدید "مرد سه هزار چهره" برای دوستانیکه علاقمند به دیدن این سریالند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/29095" target="_blank">📅 12:40 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29094">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bba3aff6a2.mp4?token=Gj3jS6zpzoEnH0xIdwl2f4tmJZxCd9bqXrtCR8TwZWQoluGD5bB7Cdpg-xfgCNNpBI4Lg11EONKTUoUmsAoJZNuCQVnOFttMNbK52ZCA8shAAphslN0EP4KHI5df9MTSKA8IGzxZY15wREAFabE5Dua4r14G4QqqqgatUaXMoWyBBtH_qGXDXVFo2k-u00jg3__IaAnqmwD91l4o7GIdaGM8Apl03RKq4yM5CwJnOqQtn07wji5JcChg5LSaoEricf5KwovEgpXvlXaUWor0sKFMHc0__sCE8upBr89kVVQ6LpjFNkCjVnufWFrk92nmJE5XMIlhS6A20Laj5FlnPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bba3aff6a2.mp4?token=Gj3jS6zpzoEnH0xIdwl2f4tmJZxCd9bqXrtCR8TwZWQoluGD5bB7Cdpg-xfgCNNpBI4Lg11EONKTUoUmsAoJZNuCQVnOFttMNbK52ZCA8shAAphslN0EP4KHI5df9MTSKA8IGzxZY15wREAFabE5Dua4r14G4QqqqgatUaXMoWyBBtH_qGXDXVFo2k-u00jg3__IaAnqmwD91l4o7GIdaGM8Apl03RKq4yM5CwJnOqQtn07wji5JcChg5LSaoEricf5KwovEgpXvlXaUWor0sKFMHc0__sCE8upBr89kVVQ6LpjFNkCjVnufWFrk92nmJE5XMIlhS6A20Laj5FlnPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
والنتینا با اجرای سه حرکت یک‌ضرب قدرتمند و تماشایی با وزنه ۷۸ کیلوگرمی در رشته وزنه‌برداری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/29094" target="_blank">📅 12:14 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29093">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YxGc7ygGBFd5B-VCGJ7H6orZtz3MD1R_QxxgMb97y0We2siU4PIrfe8SVD21tJ3znmrI7mzGEZFsPovXfkMeU67w5Hsg3LawVHyta0bPAifQ5EyrYTo9W2xHioGKJCuKIhG4WMrRUa-Ml7VcEPgsllSKKWzoYL5L6imBsXJr7CYUCgsNH6NVSdGftTh_R1eqRH9E_VA7JB3pH-rQn1sF6GUYLLmBtmKPGDwIxk_xuJVinTRwx4aeT0jelaSTnmdmDlIbuwt6138h7ARRZcCYIizsVv85qv1ejMeHh4kMjSv5-XJrzd_l-emeQoIp7zT1nCU-sjrenZZBhhhTmWvjhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دراتفاقی‌جالب؛ فرشته‌کریمی‌کاپیتان 37 ساله تیم ملی فوتسال از دنیای فوتسال خدافظی کرد و با قرار دادی 1 ساله به‌تیم‌فوتبال‌بانوان پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/29093" target="_blank">📅 12:07 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29092">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lgu0xdBPj8jweTlCoxVX7CxZoAZ79MZT-hJdV865B4cXkQlKtgGLYYFDXeaTATnu5qoqYUZ-upi2uqg_mcrm3JMJ5L37BFlMz7e1PHepdGPAEaUEvV37NtuTmN_FbwQtSR917KIc6ASBih8RYA0XGcP5OsyTT_ldn3P1Z7ANMjdpJ-MThIDYmJBb6vLCHNIQnsOSjIoufQFz9v7HIL54S8-ZiCFNJPLsQjiEMXzpQFecPscIaAobj8vm4nIYac8R961BseapEFB-UOyMWOpw7JxjjeAIwCQSj0jqajRG-pru5cs05tipZSOnSFiBkqvSMALvsd4iWxTn2G8PVHnV8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ سهراب‌بختیاری‌زاده سرمربی استقلال به سامان تورانیان مدافع‌راست 23 ساله این‌تیم برای دیدار با آلومینیوم اراک آماده باش داده و به احتمال فراوان حردانی از لیست آبی‌ها خط خواهد خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/29092" target="_blank">📅 11:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29091">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iAtrAP2T43sUJ4WNda-6f78fIX-sNOoXxSC-93mGvqFs_8w-_IwnZaItIyFUkbKVr11zpBSpxmSLoa-9pdvcRzcpqBcXfCxDIax2mcZLnSFRNvNRXzNS2Oh2Vqdj8cS9oQHspsPtK6oo3RnWvmwy4R88_V3JTBnyNWqm3w00RH4Fn6iolIvMogj0sO4rwshbgiKlLRThwLlQP3QEXI1DquL0VtPw1h6zgbyDot9XyBA5HaZzAKWcmEJ3SA8hXwrq7xv2eKfHqNZUwoLu3MYMUYFqvxLgJSYK2T6Eh_B7PxZ73P3r8gL6XFZT8XriyghupQcT0t_AshjcZa7CPrRyUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ محمدحسین صادقی وینگر پرسپولیس اصرار به جدایی و گرفتن رضایت نامه‌اش از این تیم داره اما مدیریت باشگاه به نماینده او اعلام کرده تنها اجازه جدایی قرضی به او رو خواهیم داد. ظرف 24 ساعت آینده تکلیف صادقی مشخص خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/29091" target="_blank">📅 11:35 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29090">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇮🇹
سسک فابرگاس سرمربی‌موفق‌ باشگاه کومو درکنار خانواده‌اش؛ از دختربزرگش که در تصویر مشخصه‌ پرسیدن رویایت‌ چیه؟ گفته روزی بابام بشه سرمربی تیم بارسلونا و تیم ملی اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/29090" target="_blank">📅 11:21 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29089">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iKAOVERMi-DFh47DzMejzwLLS2smWs13A4W5htXfVzINHHjNzasd2Ro6uc8r_4zgp5IXBU057ggMFnoZVVIXo2rxEcc1x5aJk7yJ8gFCmJ6e1aKVN3dy-FqHmpmnlAoU04nwZfZ5PcMAKhuAt8mDkU9LGGVExbx3IswsggQ6Rc4BD6zkTkaOcK4T9QL_37wWz4ockOMCNy2blUur6inR7cfPyopPAKmJHc1N_ulkuuGY6T5ZqATOZ4CxjdOA_BRWnDhiFVdNDMpGhf0FRnOg6HbMHxS2XP8wGs8YShuhDDp8a3HFzaxdHME7QA2mlMHzjk2bjQaEfWKnrZJDhscvug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
بعداز تنبیه علیرضاکوشکی توسط کادر فنی تیم استقلال؛ سهراب‌بختیاری‌زاده سرمربی آبی‌ها این بار صالح حردانی رو به خاطر چند مورد بی انضباطی موقتا از تیم استقلال کنار گذاشته و احتمال زیاد در بازی با آلومینیوم سامان‌تورانیان فیکس خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/29089" target="_blank">📅 11:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29088">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/527972a3ec.mp4?token=TnPg-gCPtpiHL-KsNc8RDupqSfG03TBWwM5h7bxsqOY2ldKMbRc5QonlDfxzmAWQWmoX-dto3H853AGx5ttFJqEPt3BYBUzlN8yvTauzov6k3tZoEkgLvea8bAYxpji-r8DBaqP_ed6oTKIEdiYBJXEF1fIFk_JnSvHct7taIR8y1SDub_a4jb-f-So_JVWALsLk8k2DHGekx6FhfbZUMwUPCY9N7EoUnE_z3Q8QC4_p_tf9zIIyySqxefj0U_HQQ1lEG2MaS2WD7J9GUFBEa75ezHt2PziU9etBaFQ3xRNIi-u1wq68bEZ_tfzJPdhRLJcbzJ4RbuuEeFuSdSrdcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/527972a3ec.mp4?token=TnPg-gCPtpiHL-KsNc8RDupqSfG03TBWwM5h7bxsqOY2ldKMbRc5QonlDfxzmAWQWmoX-dto3H853AGx5ttFJqEPt3BYBUzlN8yvTauzov6k3tZoEkgLvea8bAYxpji-r8DBaqP_ed6oTKIEdiYBJXEF1fIFk_JnSvHct7taIR8y1SDub_a4jb-f-So_JVWALsLk8k2DHGekx6FhfbZUMwUPCY9N7EoUnE_z3Q8QC4_p_tf9zIIyySqxefj0U_HQQ1lEG2MaS2WD7J9GUFBEa75ezHt2PziU9etBaFQ3xRNIi-u1wq68bEZ_tfzJPdhRLJcbzJ4RbuuEeFuSdSrdcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته چهارم لالیگا|اولین شکست فصل شاگردان ژوزه مورینیو مقابل‌ گربه‌ سیاه خود رقم خورد؛ رئال مادرید باز هم نتوانست در خانه بتیس برنده شود‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/29088" target="_blank">📅 11:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29087">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hksjnNB2lERVmlVx_lI20VIGOsHBcantPaPW1eVtwZLKB4hqMipX7upvzAkF7kXlgBRpbVSiR3I8syWMabhEDGKgtTnLq2SATe2nh5zNifLDRgEkpcJzQGRg3X4dlygr9b0uZde1Yu3oWAs07NPuw9fOpSeKiH7SF1aBa7ZDc9HBG0pjVgkhhkPsCTiCpy_YzdJLrK6IF2J51enkEuewxw2tEVbEfrA8xILBnqDPOAC44IsOADu9F6DFCRcgZuGVcCWvhJ7LMSx-qqlVU1cReZ8hk-TlSmkC3QxfP0GOBd0AGc3xHehX-KccqDi49twM1RW-uQrZeEvA8XOsejLf3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
سایت جهانی WePari
🔥
😃
😃
😃
😃
😃
😃
😃
😃
🔥
بازگشت باخت به صورت هفتگی
🔥
پرداخت جوایز سریع و امن
🎰
شارژ حساب از طریق ارز دیجیتال و انواع ووچر
┅━━━━━━━━━━━
🎁
کد هدیه ثبت نام: Wepari2
👽
ثبت نام کنید.
👇
📱
نصب اپلیکیشن اندروید کلیک کنید
💳
آموزش شارژ با کارت بانکی
💸
آموزش شارژ با یو ووچر
💰
آموزش شارژ با ارز دیجیتال
🌐
آدرس سایت
👇
til.ac/0L4vyJf
til.ac/0L4vyJf
📲
کانال تلگرامی
#وی_پاری
:
✅
@Wepari2</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/29087" target="_blank">📅 11:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29086">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B5nUS8EAuI8Q6gsicYED3HeQTzJxsiwowlxGqpVG8yPIoEXpdlfU187tdOiv_yn3xvzny7RizC-rsmq4p5Q9Ic5X6CkuK8P0ATvJl6EH8Vtr-Kns84Qmo32P1IhHH5Bn9Y8HnfxIKeVa4wHq154deNvH0CJBj-oIZUp14lzis_wPWDLC_bFeYow_zfdkZuNlC2xw2moSmqWRtW8JEBB4eiXgCF5uerFkKQdljOvbZh2UVvd3OFF--CmNWpJJqxdN5hp-XlPX45XVTUBysytP-V9sl9GVVHQrVEkBjrxFuJ6oBYXX8OVzl5pmrWIAcjSC_pnn3kzh_5LMSfqWlVassg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
عملکرد رافینیا ستاره برزیلی بارسلونا در این باشگاه وقتی بازوبند کاپیتانی روی بازوش بسته شده: 29 مسابقه، 25 گل زده، 12 پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/29086" target="_blank">📅 10:40 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29085">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KyEKdvvS1w2qrJ0LiAZGYgZeqZHLl66MLv0y7663aYvmo9lMs7TOz3_1DcPLzkvCuAifJHDipMFrk3F6Uy5K1TKh301_LRY31hiQ4PosQTrEkCycVrwfkXa0LUjRjywz19yCxqvfkUuK1UrAicH5_Rc4oD5yiLgshpvzw-VdpyzYMFJbluFlUgi5HyBKHZaCdAlWMNWS57mgGa2YeIJrdYl5wFFKyBww9iN1OpLouUjsolm6cghgfDpUuh3h81BknpTl9hqRS17Fuhef5NhJNB7gNixn7hY2dhBJv4DZWOrq3_3NI66RpL5uPhTGBiLrKHDxF-UeIQrEwNPQuXKMtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی #اختصاصی_پرشیانا؛ درخصوص فرهان‌جعفری هافبک‌تهاجمی 20 ساله ملوان همانطور درروزهای‌اخیرگفتیم هم مدنظر کادر فنی پرسپولیس هم مدنظر کادرفنی استقلال؛ درصورتیکه حسین نژاد رسما قرار دادش رو به استقلال امضا کنه به احتمال فراوان فرهان جعفری راهی پرسپولیس خواهد…</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/29085" target="_blank">📅 10:27 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29084">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kVCrUfGaqoWnk9jrsM_xAEZBrKkK5uwsTgl7MALpUaAOS20jXemnO-p6kIx6DKrLtPx1H08R0PTkA49aGp9XBfOH_WkohoRUxEfJ6BfTu-NcMQXX57drGP7IDe7yxhuv3hIG__dk__jA79ziOjLogS32jfcXVEZRKS-aj8l9raPmUZeIApInsEPovDdlWdz4Gf7_pJC8DBkq5bbyhhOONjmVMx9wiHlrP9ZsYydqYwtNmff2K4FwRjzxAwkiAHo-kK-2zgOZO9kakTQIOjsFOyaGvXkjl96C23qF9YCEZL8Z_RHoAxKaOYyB5AZfvgvPW0ztRFrx5I0OV2EA8G4p6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اعلام اسامی داوران هفته ششم لیگ برتر؛
پیام حیدری داوردیدار استقلال‌شد. میثم حیدری هم داور بازی پرسپولیس. بازیایکشنبه و دوشنبه برگزار میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/29084" target="_blank">📅 10:07 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29083">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TLeAePrSs5JA5C7AFnmIs957Kp41Q95SiX9pfZpoRGf6-tWL4F3EnG8MxO6-akPEGbls4bkIVc9MuFscLWpFau0Vp3yHCv9gBIkdFoSvaYWNFldFjpNfJLacy14oOVMt_e1PoEUF0DKzSkiYaBM-der539UdO3rzqI8AM7RtWoD9uS9pZgLN8uizU96rcbMJvY0vYhxCszd-pUMkXvngIfGrfo_Mg6Qy9mTjuQU4qf8ogBzQQpfGbqvRYa1URUuoxzbnC4z0EgkdiGLZ7QnOOR1HUnaYGn8IxQK-dYor0lBy6fbVtF9NCRYzXFpf0zqImbtzM1NDblOdkM6jS5LP-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
معاون‌وزارت‌ارتباطات خبر داد: حتی اگه جنگ بشه هم اینترنتمون‌قراره‌برقرار بمونه و همین که الان اینترنت وصله‌نشون‌میده حاکمیت تصمیم جدی داره دسترسی مردم به شبکه ارتباطی کشور حفظ بشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/persiana_Soccer/29083" target="_blank">📅 01:53 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29082">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CAhHO7y2F7U6-QoTjc7DktF8xgDD7xe4RT0p_g1GS5PbgaMlt4yX4FhCb4KFQWcejMk8vmVDZM_Du64kDzDx5nGW1-UwY23qScbyYl1EXcjOtq7lR9g0H8iBFbHGFUy3GscA7Mh9TT14HWtHkMeH1vTEJKcSQFXs3OpslbLCki4SyE3QfbGLiqeOqZGOPXTY-kj_WZYgWqRLu_DQpv4Ln_7IO2KXvbUHbu23NuXDeRWUHsFFk0BRlqNrWPq3A6dmk4EndIt9BHy1TG0p50r_1_HwZEm9xUQsN6Bv0Wnl0pF78mozKLjD1zqu80iqPI8LKcdKanilDFPrHJRGsdnwWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ اهداف مهدی تارتار درصورت‌ماندن‌درپرسپولیس در نقل و انتقالات نیم‌فصل‌لیگ‌برتر:ابوالفضل‌رزاق‌پور مدافع چپ فولاد، محمد قربانی هافبک دفاعی الوحده، فرهان جعفری هافبک تهاجمی ملوان. جذب یک مهاجم جوان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/29082" target="_blank">📅 01:40 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29081">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pfq_zW4UADcp7eWDJN3k4fwBqMC08Ml8dctsjwy-871-obAwxDG21gEihOjl118RzNXHaqCtPHiJvKk2JIJijVHkjp6kU7UY4SFmzoS5gv8FqBO7b8p5kWLqZ2MaKJ-e3jLLfY3YEvwHs9EH7ooam4gnKvp2LV67CFMJ_Ygxo2GOXv4uWyBePwm3zne8pPly2GM7O5WH0riNt_CBL3P83Ikr7-QHcHU0cgvZ3KCHOFYndcnE_zm2shzIr-uSEcGMRaOo9NrPHdY6YOSEDBdPYUyb0uNn8lcXZMupi7tNH_D7tGpXQPEv5nW9uHP0Q3X2p_OsRm2cChMh596IisK3pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ماخاچ‌قلعه‌روسیه به ایجنت‌ محمدجواد حسین‌نژاد اعلام کرده که در پنجره نقل و انتقالات ژانویه "نیم فصل" بادریافت یک میلیون دلار رضایت‌نامه حسین‌نژاد روصادر خواهند کرد. سعادتی این موضوع به مدیران استقلال و هلدینگ رسانده. حسین نژاد درپایان فصل…</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/persiana_Soccer/29081" target="_blank">📅 01:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29080">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XNo-x4s6CtzWhCcXc9pxiyGQWdb6I33NJkZFMeav45OEUNhE4vXfb3YCOon9MINysawdRXMxBg7hvpqhMhJCsbFDYcdQ-uZx5O8CUTAVJ4AUOtLP7r-JsTi7dgO5QIjwkt6q3B77HQi-QHeWkFGWYJPr5NMeE12ffv3oXFdcPCAmF5m5PrOoVVhmQJJxDIpwlqmOHIHBo-C7ShkdDI9nerphIq42ByeZshkcfYIk3JyMj2x99TvBzSc-X9Efcgr4AiniMyT-YjiYCA36W891Qq0QMOWXbVx8tIg5pMdzoKeTVWrpZZiGWpSliIkwAB2rojteGvOOKURPLPlDj04UDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ اهداف مهدی تارتار درصورت‌ماندن‌درپرسپولیس در نقل و انتقالات نیم‌فصل‌لیگ‌برتر:ابوالفضل‌رزاق‌پور مدافع چپ فولاد، محمد قربانی هافبک دفاعی الوحده، فرهان جعفری هافبک تهاجمی ملوان. جذب یک مهاجم جوان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 84.9K · <a href="https://t.me/persiana_Soccer/29080" target="_blank">📅 01:17 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29078">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UL3IgvPq6xfiffTvwianQXXMEH283d5nmEJ2upohcPY8kIOfHgY9Upj8efU47R_-LbOr38QEfTX0YRy-lAfG1A9V5f353dpf2ZUaWOEMdyhPYyrIsYsgaLmQVHCe2s6lewlVMGbhDftucDLGuTQSivNwCZMokFFtCy3jHUL7uFqtLyUVz3ZXCbIvFLiwDLR1nZGFwUrEGQYy-Ljy9JrYnPehnTMTql7wvhBmzrQfNDW4RNZGpyMAJV2ig-MsLlNJ5dypbSMrBlUyIige0Qgb8bmVreUGHIfrw16-noDsNpCw8WHJ7NrEz37MP6Xlfimh9BcdDV8HM5CVNU9gevz8sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ اهداف مهدی تارتار درصورت‌ماندن‌درپرسپولیس در نقل و انتقالات نیم‌فصل‌لیگ‌برتر:ابوالفضل‌رزاق‌پور مدافع چپ فولاد، محمد قربانی هافبک دفاعی الوحده، فرهان جعفری هافبک تهاجمی ملوان. جذب یک مهاجم جوان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 85.4K · <a href="https://t.me/persiana_Soccer/29078" target="_blank">📅 01:07 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29077">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eEWaUkdesOqXtgBMxUxxSQ9oH3DMxX-CRLh40ZU0ZLx8Uxx8w_zZP71wfRYjH90JaDAyCgAuWlq8OWfP77kpo30hR8R3QobXpftdObILLECsmvdZbicLazXFimS2SDrWwrVHNiGuH4TW39w6l5P__7t77BRCCXo3rlfiz_dGfeXmVoidc-6Fhr-HHtmdXooDqj-gpWaOBmZ0mLfEgdBRVrK20rTRZjs4cXNFMjc_f4DN86iheZtOSyk4amnOSghhhe16GCScWcmLT3tGJLDBm3Q49Hpmw1F1OftCBWDnGLW-wLvD2l2DxTXKNDyp1vvmXwMOvr-cJXtQ6_G_QQjSdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌‌امروز
؛ از جدال مهم سیتیزن‌ها با کاونتری تا دوئل شاگردان نکونام و رحمتی در تبریز
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/persiana_Soccer/29077" target="_blank">📅 01:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29076">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CYrQBjCz6HX-SHvdTr6iPrsEItSyBSzzsSTtkGEmJirzr7DuivsoUGJzpGF5LX6x9kOhC2fM-M5okdklI2UndI0x3PYQ2bjxqULdTr0cVNBeYuqZRrC0erU5BhL_PndJunuMTukTit16eaQmb6ChNcw87AL2A22MJMqSLp74ErodRDCrzMYd7j1BCy4bHHjiJTxiQMrysCap8rKGPYBpu0WiX9LGY8hDfecaGF5KufKBxf18_MKrXVume9dXPjtQKas2LvsnzoXJbNc4b8kvhDbm9ihUbmh2NmRY14IXrdUNS2itSTylyJ64hh_c5UGmzxYDb4Q9ZlNqxitHhQgTEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
ازبردلک‌لک‌ها با دبل ایساک تا شکست همزمان و عجیب رئال مادرید و PSG
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/29076" target="_blank">📅 01:00 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29074">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qlav1IT0-570124oPYtArymsDlKHpk5ml-8nSwc_VWgFBT2Svgwa2XIFNEz2_PYaJYO3oJ8TiM5sx5aeY5xiHz81MWTI6FrobCFP3xADKL1A8GLUNmllEQMYEX06uYIa3fmLjYqL5_KFzOJ7I5Jl3CvOXv13AhlGI6poGE2FVTOzK7NoPwk1ZWR7XpMQBlGwpKWKmuTo9JDySOLt1SmWnriNb7grMYO4MqvOKh84wl3lnG2_VZxNYR8yl3XvZ9rqDKmrYB-XYw3_spUZJs-hP_tFjQFz9UeqqlCYhKpKVf6twWWTefO9xxkANkyesqc2Yxvv_LCjY1jv5_25Qwvopg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
عملکردخیره‌کننده لوئیز انریکه درپاری سن ژرمن: سه قهرمانی لوشامپیونهه، سه قهرمانی جام حذفی، یک قهرمانی سوپرکاپ فرانسه، دو قهرمانی لیگ قهرمانان اروپا، دو قهرمانی سوپرکاپ اروپا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/29074" target="_blank">📅 00:49 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29073">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cRhqNyBEtqY6E4OkYgbiGyMTxgySm2Vfa9Q3hsxpH3zkal3vkBQeAdUT7BP0FABr4VCludKo2jY0pOQzmn2v7qqd3nVyVPAEx5rZCjCgamDTEiGz9p0eZuqiGbpiSU33i5EcO4bqyDqzr8H_dVDszRggDag8_IVFTv0DGq6eA1jSNykX5d7YHWuylGn9tXpDBA5YZSR3ykeozs2hwDY8CvjMu8NrFE8h5wKSJIc5jv96a0iD9822gOlKw-5mTBLhDUatrwR0QJB-x6fC29eaGeLfvQXSm_sG3vZ5lSmWnbGk1lN3U_d8-asGb31Lv06F2Istn8i-1tq0HITDWAsjOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته چهارم لالیگا|اولین شکست فصل شاگردان ژوزه مورینیو مقابل‌ گربه‌ سیاه خود رقم خورد؛ رئال مادرید باز هم نتوانست در خانه بتیس برنده شود‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/29073" target="_blank">📅 00:43 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29071">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HRbVZxgLlH8kfuowAFTzBZFNPgFsZUv3iGb6MlMw7ASEmo816oZLKVObPpJ6G4Mz5xiKmtSJHajEEYhpnlS6EX4zB8crHV8mc1b0uLyX8ntNNyaGkiKZ_LcrWF4iii8tSA_VKau74VvmxRtukbbCZ3qNpb0-fgfFF14OAUli0E93Q1oakwiiHrlB66C9zNV1n_qdc4iyQ8Wuq5t4sUp2U7k4rgmtPRN0moXljeWCIJt2S_J2yE79HyMioNVKzqgbC1SIZvoIITabIHE5ZTWdthIJWiZI1IWBC2x23BGTXcL9jhNSV7eWtQWgkVT1_1IwJRhRA7yQXgsjtScSAljZGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
شاگردان آقای خاص بالاخره طلسم شکنی میکنند؟! رئال‌مادرید از آگوست سال 2021 تا به الان نتونسته تو ورزشگاه بنیتو ویامارین، ورزشگاه خانگی رئال‌بتیس این‌تیم رو در رقابت‌های لالیگا شکست بده و امشب هم تو همین ورزشگاه با بتیس بازی داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/29071" target="_blank">📅 00:37 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29070">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dGp8U5NsWlckF1XA5Jr_lNg3yoAKkXqo3zSYXVzPiojsEgF3lza2vOhn4cuwrgveVjx_u0IfpHzVF0f-7oZ4Q7VDSgM2haPK6jucz9e59hv6qGnoUnysld5QM41Il-Xgyakt3grZ1e8w1F870fThpyTWSvnQp5CCId3ekP4kWBL7Nja0kPdUyYSdPBbBpbO5KlJ6tzIuFlZdexKBeKr8cYaYwlXQ6Hvtb5PhRkyu-M5B0iSXaGXt9K_7NNUMf2_r3mZ1KdvrC1c2Cu3r0Octxt8gNK8kxPr4KkSG9o5QvEErgTKBdH0PlMdoKeBfvJuLZLCillXqMLnLZIBO2jeP_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
👤
طبق‌اخباردریافتی‌رسانه پرشیانا؛ در کنار جذب‌بازیکنان‌جوان‌لیگ‌برتری؛جذب محمدجواد حسین نژاد و مهدی‌قایدی دوهدف اصلی‌هلدینگ خلیج فارس درنقل‌وانتقالات نیم فصل لیگ برتر خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/29070" target="_blank">📅 00:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29069">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">‼️
سوپرگل‌دیدنی‌عبدالکریم حسن مدافع چپ قطری سابق پرسپولیس در بازی امشب تیمش الشمال مقابل الشحانیه در هفته اول رقابت های لیگ ستارگان قطر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/29069" target="_blank">📅 23:57 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29068">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pd1FM-Xki3P5h6oDYqg_zU-GGkK-2r9QErn6S_v9uXCCBmIzQls0UnbvjpipgzD4g6Xlf7r46-4xd4G6tfJ17FTh99ebHnSLe0NHP_5z3jo0FfmND4KnOOxDItgiIB1s_XeetcveSFUgO9PIhp4HrGCjDisEAfo43q0FqDiv4qOKVpM5HmucCM8CD3rtRXaE6YKcmWvP11XqEyXbW7NSg98JmJIVf6_bBiaEsbLERUrib-_A1dgiOMD4wW14BBfDGsVw0YZ0PiZrdBOXdzXEgxxciRwr3DjFd3FqUYp5Zi47gonQxLYOaBhxhmPrrgj0rgFgOmHvd86DU5suGxMC-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پاداشی باورنکردنی برای نمرات خوب؛ یه پدر مادر کرمانی به پسر ۱۸ سالشون قول داده بودن اگه امتحاناش روخردادقبول بشه دوس دختر ۱۷ سالش رو براش میگیرند. ماشالا پسره هم کم کاری نکرده و تاتونسته‌درس‌خونده و همه درسارو با نمره بالا قبول شده و همین چند روزپیش‌رفتن…</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/29068" target="_blank">📅 23:41 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29067">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IGlmelvZxmQll7e8gnZiQIBXmotLVVWT532fAQnneVDYqCMUd9ejSFM-wkIm8TcJmLE7H9FqcYJ4vQ-jB4tRBgr00oBcpARYBIG546_eEiZq_VCcNl8A1V1ZK6kkakxNWcatDr-rDtI9k9R6j-4EtYsXy6sCBMfbaZGw2TFbSkEkpMGe5K-iGf5ZHvUcez8oHqnEkuHooZqZgwLP9qjT1bWlf1s7Z9Olh0gai69Qm2iURUjJTnLj3z7yQm4_aSBMTs1RNe8-N0s8MIWTND-Fvo8DCge__HCXxlKK8xfq0DvvgeaLepAfhHIr4asfEs7v91WMJP2vvmsua30pFhEQbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
پرافتخارترین باشگاه‌های ایتالیایی از حیث گرفتن انواع اقسام‌جام‌ها؛ یوونتوسی‌ها با اختلاف در صدر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/29067" target="_blank">📅 23:25 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29066">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PRSRmuqrKlK5E5sN_Y797B5Pn0Gs64b5mI4OrpsCTsjmWGCc5qdiIeADWFbbyi9F0gIjBAcsNUn8oMrGRRxjoztBaySOy_73l75a7S3rN0ZWlve5tS1Y88_Ja0-LjWKZyT9hYB5keI1Cva_KVa3FfDQHOBPZThBSM0yytcr64J1IJzUPXfcvMpa_PG5whQkhVwMDK2Q7_GX3hoRl-T9kur1D-sE2BHMhT6NEvo3zJnMuxgCwZhJE62t6jYhFRGlMxbat3ZSSpiFaAnIOOQj2wD8xlHcFLRZT0pGZFhituN2JY20grYSn2iHvOADwBQZYQ9aB6f5vpP2FkT6kYbbFog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رگی لوشکیا ستاره فصل گذشته تراکتور که با قراردادی دو ساله به این تیم اومده بود بعد از جنگ قراردادش رو فسخ کرد و با عقد قراردادی رسما به الظفره امارات پیوست.  این هافبک آلبانیایی در ۲۵ بازی برای تیم فوتبال تراکتور ۶ گل به ثمر رساند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/29066" target="_blank">📅 23:05 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29065">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UWvSRcCICRiskRIHH_E3LOUgTAvhTNZyT_9hyiW8t1x6rPD_4UsOgAfdSs_U3jtoQkQHvQPzR7EDb47mrJcftCo3t-IZsLUTWvVVueIM4h0BsRNbibImzsaw-RUK8dClQVA2-KnLhuivcStFleJVNo5QT51heNhkBPKzu_z2O9enngJC1pJR5RlEPVxn4-geqAJLOnnth5tMwgW8oJmEfue9Tiwm5UMe7Q6ChuwX222luNOHuWNhpq0Z4Fng0FrIQnzbZkQHLxJ8Y2sojyf0efIxXm3_2g0GVeQCNvMfpl3IVoYTsN5d3oYVfajW7ti8W1h1M0RJJyPxfwotnymOAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌جنوا ایتالیا به‌این‌شکل‌از استفان الشعراوی ستاره 33 ساله ایتالیایی جدید خود رونمایی کرد؛ الشعراوی یه زمانی در میلان فوق العاده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/29065" target="_blank">📅 22:54 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29064">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KXOBGBkOXNA5VaaRiQj8REq_B98Dz-bTnicnvw3jr6BiguV1QNzpcuy98KiFg6Q60114ezuBVHwKk-9QxrC5lSf-dn8h4-YDvqcZOve3lmbN8G8kTm1_ntqtZBW-3DPqSmG_CHFIKoDQxF6TPVG3KQC6iwH4uw8OrmzXre74D03jPkm6bI9DEx-tLmeYWZmjnE91BXvdRr87ikXUDVe0zeoalsi9eGEl9kuP7R6LeeFh9vYy-RKLx-GXsmU42VZ-NssRmg_Q2zM2wn2RZYxi35200MuBZsPKa-4cvkBDE46tmFbWekuOlIS7e5QijGROaUyRMnmdg-I8W3_Zg91n7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
میزان هزینه لیگ‌های معتبر اروپا تو فصل نقل و انتقالات؛ لیگ‌جزیره بااختلاف بیشترین هزینه کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/29064" target="_blank">📅 22:47 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29063">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJGalCUD8dQ8Eo39gyQQNaLEgyWykLhrhsk23sfNpv-1L4ytPORwgxZMRucHomfyokENOW1CiL-B8q9VoRNw2Y1Im2Xu9ty2WwXXPUObNy6xscZ5osbjUmWuG-AIZVn7VkE1lkts8JBxBYXo5eNviW8smDcrjB5wnIEwQS1kT_EWvWN_IecC5djEfQKY-lyNTW_VqP9P3upeDxQzt4GajpZSEwreRONUz5yFafcDOEBi_B40723wUTlrCexyM4KPHiEDNHWatQWpyv9l-FUHC6DAGkJNf64WcOcr6DXBBj95UB1X2o1GkSAlSlVri9uYnDWpy2f1xWb-5RIFLV4Zag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ ویدیو صحنه‌ای صالح حردانی در بازی با پرسپولیس اصرار داشت کاشته بزنه اما به توصیه سهراب بختیاری زاده یاسر آسانی پشت توپ وایساد وباعث اعتراض‌کاپیتان آبی‌‌پوشان به کادرفنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/29063" target="_blank">📅 22:38 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29062">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SsjCYlvdTcIJd8bPpmthLRiVHKd8jYdLZrvNaHlyxRBXurMNCS2xkzXP8xT917CyC39zBIfWRLCmG8C7PiFxMOXgcxz5imp-R-Krh9oexDiQPcjweH2xfZy2C96MOaLkmPPoe-dB96Y2GKvFnLmVy4aauamDwxPvSW1LTtcK-ecyW4eiWjGUXJYIR9HllDiEWd_26sDB-e85x4mHqjgwSeGnKT7MjIn5iA2F_cMnssO-Jw8KqylgLNrnPGcPsLAFKCB0ConxUy5tlVWfeAJ5YCYaPGqKnnaiX9jHQMw_CxZBGiHHVScqQqpOBTmtIfxEVZGSuMvDsVtgdJqHHwurKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
فرصت‌سوزی‌عجیب‌وغریب و دور از انتظار طارمی 34 ساله در اولین بازی خود برای الوصل!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/29062" target="_blank">📅 22:19 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29061">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZSiJHjTOy5GxfFw7O7zNRNZ1H656WL6mfBGBwUTcg5QZqu6FrI55YngdxTTm2J6YibzsqRC2BgT7I2iXB4vphHNA9VbzOr9l9JbWW_P2bpCJZFnl5Vb-4D4OunV4bF6WXLfLxahXKrK1Frn-UPgrAYIysGXRvzjLVMhLiFmUOnDYTU8_UjVdFgkgkWLeGMWOAL9vFsG0_qgyOvhYzsE_NHrHGYB_PFOLOxf3s6CzoWRGAbEM2vmq3U0zKX6EcXDIgOXXd3h0FRA4B_XO7gAMeptZHdspnt7cOyj9oky4tnE4rnSkTlT2i3VIkjmArXGfMSCSLc_yRZ-VHx_qtCMsJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته چهارم لالیگا؛ شماتیک ترکیب رئال مادرید برای دیدار مقابل بتیس؛ ساعت 22:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/29061" target="_blank">📅 22:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29060">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34787ce1a0.mp4?token=bsgZlKmSrpDtmtF4FNtXOxFck1bhOMVF1ygx6CwXX402YuEvZweRnnlP6aVFrlKIFgjkRBmDIBVXvbnfVqsTmyJsQpSZw1FEMqgg4ITq0eyFmrQG_xr-3LlSehsqImG8WWL3Za6_stxXFZ-ATWJh3y3kZeKIAjlmSEAFF3Wxg1ftS1dLBoNmCr3KRbeYNWHSIXADLw2SfWe_yAjXdFV2Cpzka3ka0crl-tGvfIY-DzLK9dYigyKppd15qVOdWKGaPfRNfWnBeMY05Cr7lrbmOYMDEL3y56Xcawwg0GIAJIObOoIycBjBbH9brmhMqhoJdTnsaUTtECunSkIpxl0Q0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34787ce1a0.mp4?token=bsgZlKmSrpDtmtF4FNtXOxFck1bhOMVF1ygx6CwXX402YuEvZweRnnlP6aVFrlKIFgjkRBmDIBVXvbnfVqsTmyJsQpSZw1FEMqgg4ITq0eyFmrQG_xr-3LlSehsqImG8WWL3Za6_stxXFZ-ATWJh3y3kZeKIAjlmSEAFF3Wxg1ftS1dLBoNmCr3KRbeYNWHSIXADLw2SfWe_yAjXdFV2Cpzka3ka0crl-tGvfIY-DzLK9dYigyKppd15qVOdWKGaPfRNfWnBeMY05Cr7lrbmOYMDEL3y56Xcawwg0GIAJIObOoIycBjBbH9brmhMqhoJdTnsaUTtECunSkIpxl0Q0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سکانس کامل مخ زنی به سبک مهران مدیری در سریال جدید او بنام مردسه هزار چهره که از امشب فقط جمعه‌ها از شبکه سه پخش خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/29060" target="_blank">📅 21:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29059">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kEXEEVADXqmquCQ_Wg-jKgCkJF_OvfcsKq7PSjhBXf5dFy0JR-2vr6pS9sYkX4byCvaYRu3pgwfFEe42o_J_jMmUzsLInGSl-APFqu0080FI27A5mDnHhWxEI2rMGfRFIfgYvP-BYuIs6erBnfno2R09ivdhrojCoviUCpDZ9Uaz73PoL9gXk6CpXcjyHbuFmmDP1MZ6wXlSNe29M5jrKLhtKy_WhfoBOutrVG35H8thW7p0YQgyePDoy9pFiYmezckyW-MM5TB-CXU_XZSfvcGYKbVAWl73vfiuLKoBEFUnv7kk2RJXev72bkMXooxIzXZRdmcqspW6kZRE1jUq9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته چهارم لالیگا؛
شماتیک ترکیب رئال مادرید برای دیدار مقابل بتیس؛ ساعت 22:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/29059" target="_blank">📅 21:14 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29058">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcf2bf71bb.mp4?token=E_Ry246ESrQWAxLG6-f8J6NY68dGI0ageYZmA70EVVBXjQAH_bSIfSh3Sk3E9Pg0nv0T47rEe7MBAMYxyJjaXdng2lsIcGRq8sXBo6I4qIxXx04_VhHiCYvE3o869wp4lmK7gm2C0N3KDc3-eJ2wx0bE0sdOHisQU81G-MModjWTPAEcCUufRFgoIq9YP18PCKS_34vDodJgqF6uA_3vcf8NWVNhn8FLiUoyfDlBf1KGW6ifQYylgBu3WmAxUq0uU2v39Z2N9bAUMeSyelPoY4kARSzgQAzrFkI3VZ_U3x9ffgq8CbqbhQIq50Nb7sutfIiA1uG2TGggXQ36JOUjGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcf2bf71bb.mp4?token=E_Ry246ESrQWAxLG6-f8J6NY68dGI0ageYZmA70EVVBXjQAH_bSIfSh3Sk3E9Pg0nv0T47rEe7MBAMYxyJjaXdng2lsIcGRq8sXBo6I4qIxXx04_VhHiCYvE3o869wp4lmK7gm2C0N3KDc3-eJ2wx0bE0sdOHisQU81G-MModjWTPAEcCUufRFgoIq9YP18PCKS_34vDodJgqF6uA_3vcf8NWVNhn8FLiUoyfDlBf1KGW6ifQYylgBu3WmAxUq0uU2v39Z2N9bAUMeSyelPoY4kARSzgQAzrFkI3VZ_U3x9ffgq8CbqbhQIq50Nb7sutfIiA1uG2TGggXQ36JOUjGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
استامپ‌من‌کیه؟ بریده‌ای جذاب از سریال مرد سه هزار چهره. امشب‌اولین قسمت این سریال پخش شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/29058" target="_blank">📅 20:56 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29057">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e99ae53e7.mp4?token=uxfSwWmGja7HpRkuxhXIdjI5B1iImTvqZ8N348Qs37TwrPyPmnGnCIgnT9unvEUgtwGcgOjd27KEbrKCXSJ8ppHeIPI6LdfCqV20u8BY_mJLLeodUklrgnLHLwezov1yAJz5MhLQy2WkS7xB_b1kG5YJ6r3VsUR9OIgyWtWSYiP77V6K4mNi2NSGW1SpTAyhKVFmAvhjTzUwQOs_FzMMQfy5Y6_YVL5UcyhrQkIgYK4oI0v9wxSKWaGg2Pis6BfCukp7r1mjaWIST5NBfJK1pCT0zSgqxnba0dVoWB82klxwqBnivGvypfKl5B62hvGW12Ki3Qi3m4GYRG06gihyAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e99ae53e7.mp4?token=uxfSwWmGja7HpRkuxhXIdjI5B1iImTvqZ8N348Qs37TwrPyPmnGnCIgnT9unvEUgtwGcgOjd27KEbrKCXSJ8ppHeIPI6LdfCqV20u8BY_mJLLeodUklrgnLHLwezov1yAJz5MhLQy2WkS7xB_b1kG5YJ6r3VsUR9OIgyWtWSYiP77V6K4mNi2NSGW1SpTAyhKVFmAvhjTzUwQOs_FzMMQfy5Y6_YVL5UcyhrQkIgYK4oI0v9wxSKWaGg2Pis6BfCukp7r1mjaWIST5NBfJK1pCT0zSgqxnba0dVoWB82klxwqBnivGvypfKl5B62hvGW12Ki3Qi3m4GYRG06gihyAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇰🇷
🇰🇷
سون هیونگ مین کاپیتان کره جنوبی:
من همیشه‌گفتم‌که‌کریستیانو رونالدو الگوی تموم زندگی منه اما بنظرم لیونل مسی بهترین بازیکن تاریخه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/29057" target="_blank">📅 20:41 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29056">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QY7IlKPtSdQNmr_J9trOT__ZqZvFa54XR453mFz7HEE2FWOExq7uQOsW3OTYU9dEOP34o6OM-1ZCAYsoaOZu7Ew2KqFBqwgA4eYpSCHTA9-WyG40bLPPhY-tYXdNIzbb8-xGdx6h1hvCFRCxf3vU13HNS8QLQfhnnPwg6ceH0rWl4V70IjtsN0UJQ9X8w1jz7A0mnQpVgD2L_qx6o3jw0jlTxOb4k1tD1XFnJjz5EuRBRcM51h5WWC3xs0apMEBPdpWIScrJRzBqAPXA-ELA51L9taamX1VuBlb4r-pEbW9uzm4xgMAMDsR4dmGexpHL4yakKjaNlbLWXkxoN7KDMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
👤
طبق‌اخباردریافتی‌رسانه پرشیانا؛ در کنار جذب‌بازیکنان‌جوان‌لیگ‌برتری؛جذب محمدجواد حسین نژاد و مهدی‌قایدی دوهدف اصلی‌هلدینگ خلیج فارس درنقل‌وانتقالات نیم فصل لیگ برتر خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/29056" target="_blank">📅 20:05 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29054">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D01OmTvvurkuwYCpvZQPbOb_Te7yJ1ytlda0HOa6PJUqzoQqdQQypl9ITAD8J8X_TFi9s6KAmrFtT5kvQZquf132ZJWXTnpckm9HM_UhegQMfmmGx_roIvnn3ZD3akX9EhIZ2Mlj_TcdHnLJ8QlbHxVWVxesXBrYYNys1uylAR1EmFe9ettmwoVFwAvccmL9YkFB1MVgm2nnQbzvybwuUnQJV89KJa1uoNmm_idv_iAb_sCAIWS0AZuELejs0lOsIAd7OMuZVMSeUlP7wRJY81HR8pI2a4ymFzLZLrOviV_ZNYC1KBnbcRXWXOnEJZs4VxKLnGtLNwb9K0CqzAZT9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jlgsVPOew2D8smBbRzNvSFqLo-gmYL6U8Q4C0rMGLJ36YHVLjSaCVBsatkTPRsBy1OvuRqzmcJiDsRsvTjnSC56xLtM9_vCZXiKQyiu_e9IvAR15LAMzerTK9MvsVcYMbN43_WaZjZZEa6NQYTk_PR1aN1ZJepcOe2zelVy1Y_QTPMehpv_ICOV0nTOldjJcjQLZW34LPudWbQNq3c9sId1CcsGDO9easfhsZLgBmylCHYz5qGJRcrviGAeis3TbCDM6HK9R9_KufvDj9hBUDhkBm88ULDr3Dh_BMnuxXQJ_KMkLiF9LmNxRDLyeirWya-TlWpDJai9i_kE3uEl0lA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
نادیا خمز دختر خانوم پاکو خمز و شوهرش برای ماه عسل رفتن توکیو ژاپن؛ تو کامنت‌ ها ازش خواستن یسرم به شمال ایران بزنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/29054" target="_blank">📅 19:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29053">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a2OY8s2DwI6iyJsKFMbUe26xN5nQKUm-ZCyhjqY0jQlHO-NjJzcxYlyyaP_rP3c031tFCIY4dRWq3O8p3WPTrEwWeH2vUxOFvKWjGyHAY063bRGrwIjGSamAApJ--_zccqQ74aGSNV81IB5sre_B7CFaVji5bdoGT30oOYJjVlXAmpJSYZWcTDxaYVqRWIPTZu-DSCICkeiISTFxpZthf-dJVlS_GXIzQO-X6PsyN-KHkzcuxsE3QhxDQFy-iLB8anyYAyGcu1b_foO54c49B2NP11ZxwVQOGdrqI5rYpNnvO8bS-xDA4OJyHboPKQ1I23awlNue_I9fqWgvjGuQLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌جنوا ایتالیا به‌این‌شکل‌از استفان الشعراوی ستاره 33 ساله ایتالیایی جدید خود رونمایی کرد؛ الشعراوی یه زمانی در میلان فوق العاده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/29053" target="_blank">📅 19:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29052">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef0797e3.mp4?token=Y4A6UeEOXoIyEyWBkcqLI_GrmQnX6rpm2-AjjLFOMrk2KW7LwkmPS6_i7kFR8RJ0hSpd2FRfOwkG_96vlaPI68D8o4lBQQmf9ihlYAyUeM0iT-KUxk9at60OBslDSx_21Af0iBfinBnrHhIls--GGQqarF3aTbjzSbRVFGN-qFz1UJcLGLBqmxAMo-e5LYNkmfUhEXCNg0oZnQNe7HHqYS0fPYss5fBOolearWoADYMfEgl2yi-cSKnMAMzH1qCbFBMsQGtPl0PN3rBliYR1aREYDTHYJ6knXpm0ulFxDE8z3wOt36Nry969Tq52Wc3M_NGIbnIBWzlT6Lojs_rfrKraWgyOb6hT8HneA4BoQFIw7y_p5qFhaSA58X1K6qV3tm7HJ8V11Suw97Qd4zcS24R4Wdu-fsdnITb2jmiyzHTMaItGEkfJORksiG2h0DFSJ0kZrhz0avGEKbHJRgJ3oPsjA7JqydvpnYjlDdaCUSPjMoMpdrdJLaq7NDtqns81QRyrqMurieQFr3sY8nugIDGux04trLHk87jDd5c6RZ8Gm2kVXsUZqfOMNLJV9cutZpToLDGQiov3uqTjikgVwJLpqy_-uTwGXClVN7LTJYGzKYLZu2ltpymKmKMURnLgSHGxWjUjbs5JpQ95hPEWYmWHfI1P7RAldMDAJcpGtCo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef0797e3.mp4?token=Y4A6UeEOXoIyEyWBkcqLI_GrmQnX6rpm2-AjjLFOMrk2KW7LwkmPS6_i7kFR8RJ0hSpd2FRfOwkG_96vlaPI68D8o4lBQQmf9ihlYAyUeM0iT-KUxk9at60OBslDSx_21Af0iBfinBnrHhIls--GGQqarF3aTbjzSbRVFGN-qFz1UJcLGLBqmxAMo-e5LYNkmfUhEXCNg0oZnQNe7HHqYS0fPYss5fBOolearWoADYMfEgl2yi-cSKnMAMzH1qCbFBMsQGtPl0PN3rBliYR1aREYDTHYJ6knXpm0ulFxDE8z3wOt36Nry969Tq52Wc3M_NGIbnIBWzlT6Lojs_rfrKraWgyOb6hT8HneA4BoQFIw7y_p5qFhaSA58X1K6qV3tm7HJ8V11Suw97Qd4zcS24R4Wdu-fsdnITb2jmiyzHTMaItGEkfJORksiG2h0DFSJ0kZrhz0avGEKbHJRgJ3oPsjA7JqydvpnYjlDdaCUSPjMoMpdrdJLaq7NDtqns81QRyrqMurieQFr3sY8nugIDGux04trLHk87jDd5c6RZ8Gm2kVXsUZqfOMNLJV9cutZpToLDGQiov3uqTjikgVwJLpqy_-uTwGXClVN7LTJYGzKYLZu2ltpymKmKMURnLgSHGxWjUjbs5JpQ95hPEWYmWHfI1P7RAldMDAJcpGtCo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
#فکت
؛
رودی‌ژستد،کوین‌یامگا و یاسر آسانی سه بازیکن‌خارجی‌تاریخ‌باشگاه‌هستن که در شهرآورد های پایتخت موفق به گلزنی شده‌اند. جالبه هر سه تاشون با گلزنی مانع باخت تیمشون شده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/29052" target="_blank">📅 19:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29051">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8c83a1c1d.mp4?token=XxvkLKM3UQPYDnPJjFHtUzC-7n_biSIO5-I2jk51Oe0lrX0POCBB_XzMzfGBbRrvTsseLWSp-8PB6KYurBTlAZ66ckDCNChsbNnay6mvXHz3GOYy0APr2UeGoTp2APTRAHT3ew-teOYf46vxIljG1HuTx_anGvQdJtRJgy6WuwHEXher3FQ66dgd_RZse6-_xNnbfB0yfK-62kt3S6sGWhArSZ6jEFD8bWc9qg-wEUh-iZBMWF29eFiBqGydXM1duVl__0qgGOWIoZq8h7HiK1TSWn6OqcmyWYuvm7r1A3N6HHgVijTrgcXAu7czXyVNfl41puvHe80qLcwGmNaVyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8c83a1c1d.mp4?token=XxvkLKM3UQPYDnPJjFHtUzC-7n_biSIO5-I2jk51Oe0lrX0POCBB_XzMzfGBbRrvTsseLWSp-8PB6KYurBTlAZ66ckDCNChsbNnay6mvXHz3GOYy0APr2UeGoTp2APTRAHT3ew-teOYf46vxIljG1HuTx_anGvQdJtRJgy6WuwHEXher3FQ66dgd_RZse6-_xNnbfB0yfK-62kt3S6sGWhArSZ6jEFD8bWc9qg-wEUh-iZBMWF29eFiBqGydXM1duVl__0qgGOWIoZq8h7HiK1TSWn6OqcmyWYuvm7r1A3N6HHgVijTrgcXAu7czXyVNfl41puvHe80qLcwGmNaVyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇫🇷
تفاوت‌تجربه‌بازی‌درپاریسن‌ژرمن و بارسلونا از زبان فران تورس فوق ستاره اسپانیایی جدید PSG!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/29051" target="_blank">📅 19:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29050">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b4yGZSslhzedIsa-94Jf3CHIvtXnaG8EZMTRkAj2tp2j_CS5bwpXSe8_I5vA9NE8Jb7ELPnsTtj1l3HwpOpOFRCvqpWrJUxk6h-GveOWMOKItlgkunKJFFdGIU_QiXSAAQJK9vwyxjpaXedwKRLjFgIRVyXdEhnZCY8DaLYkTOCbR1GLxrs6rs9vDmfBdLLOUNAzRw8nfh2wVwyLwUqGC_4ivhl5dAJsLyKKonlvf_3vn0VCx2ZXJN7NNHiKjgrkoJsvB1wST5NSDMl3P5itbFMl4EKZ4hJX4pMo3hHYV84BK6APVSL_EfWB2gKZHhJlyeIlR0PdlhuejI5Bh1R--A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
هفته سوم لیگ فرانسه
🇫🇷
پاری سن ژرمن
🆚
موناکو
🇫🇷
⏰
ساعت ۲۲:۳۵
🔴
بیش از ۵۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ بونوس رایگان بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔴
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/29050" target="_blank">📅 19:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29049">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bDfjRQ5rSZ58Nq4qLb9oytctivx37WM9Vpn3QIOaUZ2QcXpiDh9ZBqJwpxXgZz43MTht-SgoFkoTHMFBJVjuS-Q0nCSrjJ1SiqcbqM7usESJ3LuVnyNq5TO5dVwtv4jbArAjlcTyS10p8cbtWSjNV5ME8Gc9SIp72UBg-y3acxdXQ1NW6kTHdH4_0Zp3Djky0hJbHNOZ4s5tX_oh1k00bkUsr5X6eEF_oeIYVEEcI8pmv5alk1s7mnoao2rIGFWgePq-RtQlcQdwARI00D7DcUmjmfiXkQmb5MUlvCGkhPHKE6NIrtlq2TSTb27q6qYsacykrSDJnZozQhh2VU8lZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
عمق اسکواد بارساِ هانسی فلیک در فصل جدید رقابت‌ها بعد از جذب ژسوس و اتمام نقل‌وانتقالات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/29049" target="_blank">📅 18:48 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29048">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SldhEvyIPDVjBPERRH-XJyvo8_EKt7XeNVF8HqIIsNJgae0VnH3nSRxncpzDPcNnBjVS4iI4p1xlhYLwjVLXOsn3tUkvIPzKrUvcpLpqL16fnI9RCB06XGwy6rpkdrkNWm91nMgmtFvnjOHkA2rQr4KdYaeRMMch8v9gzFTIXqwXd7ghonO3QbKQsIOlP3Jn97uh8AA9S5IpzdBVZ_e1pOw6Z2rIZZjSXnZtzCEbmbWzId7ih_AdRQ78XnC9JvduH4kvik549LtUuc_0YBXs9FWXcnVCEQlCFfhczNJspk246XFtMBjTvVp-crYHnX7QKLxZy3s8jQWL5eEI4DHOcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ یه‌موضوع پیش‌پاافتاده‌ست ولی چون زیاد پرسیدین لازمه یه باردیگه‌بگیم؛ استقلال در سال 1399 و 1400 دوبار درضربات‌پنالتی پرسپولیس رو درجام‌حذفی شکست داد اما طبق قانون فیفا ضربات پنالتی صرفاً به‌معنای‌تعیین تیم صعودکننده به مرحله بعدیه و نتیجه در آن…</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/29048" target="_blank">📅 18:39 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29047">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CivBzlwqclHTT2X-4T3JUS4XNRpRAGc6Xm9C8UbAVhvuI0M1qPlDbGKX4gPGaTpdk7tdNLGWL3verqXOEy3qbW5x8hYc65Lve9mw1dMgTZkj29mCeBbtd8tmYu1wG2lysKZvY9hJt1tpkghttDdvLREp4AJTwDuq6Fm2QmcOfJ3LtplJFTgYloSI8WwQfHTUexiktHv-66USneUbIR2YT9BN0OK-UjJ2LLQL-msndLhPuCWmLX5xGUipgiCz9rVecpZYxhbP9YC-S_GZe88zbCPsBo2lgl9nhLW1vXXfNBgU1wsvOkBMXpi8uq0oIvef5xDqf2uiFqi3m0Jj3N8IqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اندرسون تالیسکا ستاره برزیلی سابق النصر که در لیست‌فروش‌فنرباغچه‌اسماعیل کارتال قرار گرفته بود باعقد قرار دادی دو ساله به الجزیره امارات پیوست. تالیسکا سالانه 5.5 میلیون یورو از اماراتیا میگیره!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/29047" target="_blank">📅 18:31 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29045">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qNjeS2Dk0uuMutyUYK9HL-9e6ieaqCywlM7dnNDoF4zhMmeKLD2qIECx9v4AGjkmMPK62BdW9cQRYleD3XDST76cdZwdITK1MMpFCQk-R-6ZYQvn8NBcsUDVgm_a-HcbOiD_wUMZMG_QauP0NRNOszVzzQqi4uqoNENFmqbe4OuUTWsYax4X7ZwXjf9lqMfWaZWMWmtTp67SAf4R0p0Yw7U9NLctXGD0tkMh_3KvPbuWuFoK3HgPOwa7e-lE2BMv1gudcgURCGquano7mFsAv0TBdS8oSpRq1jsL9VY8j7wmM2uA_bFAQ4mFypjk68-ftsGrjzN3Ggy1q1qsfQQ_MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/656f3ff7ee.mp4?token=H0-w4zbptGKoEvCtUiZM_j6x5XDHufbtD9MnMyORTsjpCHAHfSEPKfUYmnz1Yc_yLWxoBCyQ0880XhyaElWDoA5R4pErFlXwZwx2yWR8zv2QCBZbhIHp751fL10sjx0iSHqJzhdKgQvmW51xL9uwM2-Z4z29ndzTrnqsBgI8JMcF3gtJ8Dtj2-H7qXfE6ICgwx8sM89L9AGKKJxP82BstxVty1aotyUepi0-nFQWmizQq7xNiV6vTltWJ-XAPw6-1AGDshmHxXrdJbMlm3K8jTNnkBYjEBZmrJRnGyIilHJXcr5WwUxtEM-Y5_1sa3iSVlprLy4mOZG-0XQ5-wLxIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/656f3ff7ee.mp4?token=H0-w4zbptGKoEvCtUiZM_j6x5XDHufbtD9MnMyORTsjpCHAHfSEPKfUYmnz1Yc_yLWxoBCyQ0880XhyaElWDoA5R4pErFlXwZwx2yWR8zv2QCBZbhIHp751fL10sjx0iSHqJzhdKgQvmW51xL9uwM2-Z4z29ndzTrnqsBgI8JMcF3gtJ8Dtj2-H7qXfE6ICgwx8sM89L9AGKKJxP82BstxVty1aotyUepi0-nFQWmizQq7xNiV6vTltWJ-XAPw6-1AGDshmHxXrdJbMlm3K8jTNnkBYjEBZmrJRnGyIilHJXcr5WwUxtEM-Y5_1sa3iSVlprLy4mOZG-0XQ5-wLxIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زهرا گونیش ستاره تیم ملی والیبال ترکیه که بخاطر علاقه‌اش‌به‌کشورش پیشنهاد لژیونر شدن و حضور در رقابت‌های‌لیگ‌برترایتالیا رو رد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/29045" target="_blank">📅 18:17 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29044">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40fd4582cc.mp4?token=NaZgvd0PBTHFVUlWlzMQwexTHwXtmCvWiNBi9DC6vSUYkNw6vVkUT4r2Hl89mFbmAM0ay-PEb4KfXrY1V7i8ibpBnBgc1BSvFKAdF5SkwOmM6NKgxE1jsLC3SzJvixSL4ueX9xuZgPUgtgpS3ZrjZZqHupIYaXsjAgIw5gUX6Fz4541TE4UzG-iVcanX7_PRCa4VzLuBEjuktXqiWRB2rI0v8YKyLfbWCzaB4a0EYPmI7ryuRvfRkmsZsk5yEfcrwdaJ88vQZNaztSYZPmLSWKs5jFTRXcg2-mgegFYNc5AWh-Rut0ZHba93OK0taBX8SvvoL0OAr6G8a1y9eeNw9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40fd4582cc.mp4?token=NaZgvd0PBTHFVUlWlzMQwexTHwXtmCvWiNBi9DC6vSUYkNw6vVkUT4r2Hl89mFbmAM0ay-PEb4KfXrY1V7i8ibpBnBgc1BSvFKAdF5SkwOmM6NKgxE1jsLC3SzJvixSL4ueX9xuZgPUgtgpS3ZrjZZqHupIYaXsjAgIw5gUX6Fz4541TE4UzG-iVcanX7_PRCa4VzLuBEjuktXqiWRB2rI0v8YKyLfbWCzaB4a0EYPmI7ryuRvfRkmsZsk5yEfcrwdaJ88vQZNaztSYZPmLSWKs5jFTRXcg2-mgegFYNc5AWh-Rut0ZHba93OK0taBX8SvvoL0OAr6G8a1y9eeNw9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درخصوص آخرین وضعیت اوستون اورونوف در پرسپولیس‌دیروزتوضیحات‌کامل رو دادیم. در این حد بمونید مهدی‌تارتارمیخواد اونقدر نیمکت‌نشینش بکنه که خودِ اوستون اورونوف درخواست جدایی بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/29044" target="_blank">📅 17:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29043">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VBfNwwWchQVLp9ccFmTh5sj-n4FNMUryzoRTEb0WMn6rm-Kmjg8auEhJdFn6-_Z_rOCpGpk3WT89-UY9511y-SAN1M7wA2faGyKa9wC6nxLfW733jAOFo_xT10opoYRqaJI9VLVsXQLjfsO9w4w54j0awC3uMD8vMamZc4B5byw44qm8DyQm4B9516_S5lpfB_UaI7MMkAEf42gpQdDP1bE9hZDSSTJWpCVpv9B_-R5UKUqfRQFOkAoEhszj_3DZN9TAWy_0ms1CD55ZkLQwphlrBOoSG90XKwkjK5KzwgcBAmIONsY6ImFxWdVzHuqqPQB4Y9Rk2LTOLQXRP_dHbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نظرسازمان‌لیگ‌عوض شد؛ دیدارهای هفته هفتم لیگ برتر براساس تاریخ قبلی در روزهای 19 و 20 و 21 شهریورماه برگزار خواهد شد. پیش‌تر اعلام شده بود به‌خاطر بازی‌های آسیایی تیم امید دیدارهای این هفته رقابت های لیگ برتر به تعویق خواهد افتاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/29043" target="_blank">📅 16:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29042">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔵
👤
بعداز تنبیه علیرضاکوشکی توسط کادر فنی تیم استقلال؛ سهراب‌بختیاری‌زاده سرمربی آبی‌ها این بار صالح حردانی رو به خاطر چند مورد بی انضباطی موقتا از تیم استقلال کنار گذاشته و احتمال زیاد در بازی با آلومینیوم سامان‌تورانیان فیکس خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/29042" target="_blank">📅 16:41 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29041">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ep8dSMgq7bvHi4fUu_8KOfajXjY70OYKxOojRC5ObcriY4wGAbUf3jYaO-mWiDGTxd3Om_iphAc1k1vIsGcQQZwLcbzBS1iZYOy_nAZP8i48oi93fx3MPSYXL65vhb3txdRXV0_Js7NeRUnZrvV9oZxjCH0ktjcZGJErqRHSRDYsvrya2RSUhmvZDQuumkWiMY30FV0niwgE04Vd9CXrbluRtWP5-4s9JFtx-dIgZv1Gu4poOKhPym0vVqOmWcSv0I1pK32Hm2llnenQWcONKX36GW4RQdWaUWkUG3EFFRiKYN0xXpU7X2wJqOxy39o8njP6nf3FUiKJqGX7IEaz9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ دلیل ناراحتی سرمربی استقلال از علیرضا کوشکی این صحنه است که وقتی دربازی با نساجی تعویض شد با بختیاری زاده دست نداد و به حالت غرغرو رفت نشست رو نیمکت تیم استقلال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/29041" target="_blank">📅 16:22 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29040">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JLfaVjO1L8Zjzs8mXJ0-lmW39HFe3lOJJWh8ZJ8ajhKAJSkle3pmyxssmn3DZu6n-KZmIJ_61EiHa-pxQ-kF5C5zHLwwP5qP6t1vgyukdwzEvwyj8vE3ccWoNiw_Pvo_ChFkJbbOKczCQJ3syW1cl77ge-W2xm-9IiSiMFBZ-ee9ZQ1oUTIxV6bUOOomiHHJlZ808C4cfF6i84FlDmtSsCY1xwhCTBDW8kECvLkxPk0WPRpqUt9-iPSTvToj8HXSAbsZ9bFsajWXK4OWKz6h7y0l8jQRpn-xsU9FuAqViVxySB_d151EujhcublY-vyyVAQsJ6JOssmyZcEA8sRreg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای هفته ششم رقابت های لیگ برتر؛ بازیایه‌هفته‌بخاطربازی‌های تیم امید به تعویق میفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/29040" target="_blank">📅 16:07 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29039">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fa8ecb976.mp4?token=MP9jt5SqBgW3m0J_GHFOk0ZZbHyityri-N6f__648WuhqZvrxUJss4ahYzxAfeg0p7IQWniUr4L1XLYVZnR2yJBFqWk3hOVgN9gzSJ29OKUWlUNU7d-cZ74tyvgkgjq3DyJJ2OjWteQOBWfiJq1iHR9l98s8i2JP8xK6K9iQpgfAb02X1rZFDOG8lvOcKkw0of09icWms1XMzeCBv5AC4HLWBY5orKZ2JWT6ktFxtQj7NeHxIFfLf1ALfEbBtxsWdkYIoCDvtDL9Jj0Sg3IW10-0K1_cyViOHvEoJ0hwjNDL3MHfz_wwpYffq-4LbiwajWh55x73z61er1zf84__iI-YqPQxyZsAejp3JCN3I6u8kRTKzyhES951DjGOr5enFnPRyijJdQfBwbY8ggtLDsp5FPSnksqD-xAaysVsWb6Hr_eB5VfcMtxrloUrIkOoMoWQkMcTPgW-idAOGybmNpDUm7r23G66pnZqTf8oDjVSoFQcdrncGSHmcxnxQk5GoCrtmTwX8T5_sVImwtAQLNNVbjJdCFgv0g1X9yCwWEcAWbwlfA7DhrJczmMESHHNdCwHRFoS2DUu25BfCNrne5CSyvxmBQRDZ62_7yR_TMNr0KFE-68vbiAsBluI5o5KsGL4Ay_elyh8A-x6a3ljBl7Ri8CXGF5mJbKkJwqs054" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fa8ecb976.mp4?token=MP9jt5SqBgW3m0J_GHFOk0ZZbHyityri-N6f__648WuhqZvrxUJss4ahYzxAfeg0p7IQWniUr4L1XLYVZnR2yJBFqWk3hOVgN9gzSJ29OKUWlUNU7d-cZ74tyvgkgjq3DyJJ2OjWteQOBWfiJq1iHR9l98s8i2JP8xK6K9iQpgfAb02X1rZFDOG8lvOcKkw0of09icWms1XMzeCBv5AC4HLWBY5orKZ2JWT6ktFxtQj7NeHxIFfLf1ALfEbBtxsWdkYIoCDvtDL9Jj0Sg3IW10-0K1_cyViOHvEoJ0hwjNDL3MHfz_wwpYffq-4LbiwajWh55x73z61er1zf84__iI-YqPQxyZsAejp3JCN3I6u8kRTKzyhES951DjGOr5enFnPRyijJdQfBwbY8ggtLDsp5FPSnksqD-xAaysVsWb6Hr_eB5VfcMtxrloUrIkOoMoWQkMcTPgW-idAOGybmNpDUm7r23G66pnZqTf8oDjVSoFQcdrncGSHmcxnxQk5GoCrtmTwX8T5_sVImwtAQLNNVbjJdCFgv0g1X9yCwWEcAWbwlfA7DhrJczmMESHHNdCwHRFoS2DUu25BfCNrne5CSyvxmBQRDZ62_7yR_TMNr0KFE-68vbiAsBluI5o5KsGL4Ay_elyh8A-x6a3ljBl7Ri8CXGF5mJbKkJwqs054" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نکات‌طلایی‌درباره‌قطعات‌مهم‌خودرو؛
این پست رو یجایی سیو کنید، رعایت کنید که هزینه الکی رو دستتون نشینه و برای دوستانتون هم بفرستید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/29039" target="_blank">📅 15:24 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29038">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PyQi5g2en-5YeMIbJupz-d8r2bqeYEenNHRQqHxowg36bzIeSqylqONBrRci9p1x5iO6XFL_U2cY4YNI1gaDYTPiLRxd117lW3qlmkbDmrbXr4jxy3hyosHN770_f7iKc_61AD7G1J5igQs3yS9vw9lf5enTDtINw8Inbw3ZKKXSTV5Odm_aOyT7ee4YHGk8p5EJwUIGeaj5m3tgU6jkd4FrApdO8PX4qqzxjDjAPtBeyF7UNCN11hgTOo-q_RTcaW2xIQYUd_c36s5obJpkiFv1mpJLt7cQ1GZO4-nKCUAk2EXYenRlhr_HxtB3nO4w7B-BMejLpzakfrKOJe6d6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ باشگاه پرسپولیس قرارداد زینب عباس‌ پور مدافع میانی جوان تیم بانوان خود را تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/29038" target="_blank">📅 15:06 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29036">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GZq3js_O0CPK556rqMdpzT6PKsPzAtyMwVjU1qGhx8t7WfBa8ItttFX4H1O-RvWdFbaY4nfChwqUM82H5_L0BNcw8s3bTpXDamO27mlF-kjogKAQak48mXRZqeYO7lI0EaKnnprqgDCQzPv15XffMcG0z0HQ6MMz_PtXE6S6neK6xv3ITm2A-tv4V9uXUXvx4atvFFXaVmgM7C7DKw9AGiN5uXTnU7qshGMB-MkidujtPbmIkXz5J8MaAxqyzT9wxBpLmkMEn03qezqrhZap4UOJXSZ1hJ-n7MjEAUd63av6FYy3u21SCmJPeJZAU-7aP3d8XiqRr75hS8WMtoLJ8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r8pIULDJB1yPPRJnC1wVtNRPQZWuIa8G5fUvdGJYMjEip28URldrOlpoLy5Hhv0pYmprIpCiSZMzv3fgDeO1WPG53HkI6VH6GT8j_fTRPg8fTKmqm2x3q6coTlb9SDcSVSbVNqD4Gl1oIpX3SWZkkCWvO4JAeOqSoUymm3rzMx2b8NLyOXRRQpQDD2yiBhaCtNgADLq3YeGOhMMe4t4UsiKPBefUZFHrdRVZhGwu3qebW87iTCvVq6LEF_QqIjdlTEbYboPt2cXgMOvVk3k7Rz30QHvyQT4nXPSH7q4LBGFgQ8jAxQkvwz97T_6NC4suM7RzUr_yy6sXUZhJxjlfzQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
دوستاره‌‌جوان‌تیم‌ملی‌والیبال و فوتبال ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/29036" target="_blank">📅 14:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29035">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75386b7e5a.mp4?token=oS-UlZnyWjAWuoX3Xgo6KKTMMI0ThoLQV1l1gbQEzoKv_kHNUOU9vr5_-gfW5tBMI7jPBeP1Dh_cPxNvJc5cmabtB7yXcyhjWgQMyRQkQZFAUlSZPmkPefIjIgP2igvhOzQcdPWYfNoKHY5gwvk-1_wfR6PqVuu65cnFipKvXi1rDKiyUxJQE6AWdJVFdw2Hy8Mco4JjjhQsAEbt1GPcvyFSlpbmDxzIAZWTq3K-raMDdOerDdMqm_slxChOk2TtY2TYZSmHoVPxazhgP8f3EUX5njjwIiTW7lK0bj3KCjxvvY6k-px0vi5dx07rvv3I99cWBmERhoOKOc73B1jjQ26hZ20-kmtgRfgjZLDhhxAYlQOamkb9O3JQ87dCxTSlKNuqGuYRqIVuY-EtIt81CJBJQiMij7ehHAvb4splyRr1mZzU5u32LpRG4nzCtqMFqHk7okEAxz26bLEC4z4Hcx1SC6YmhJYOpP0c6gOaavdxJkXrWtvJR2CQTxKvUFZ0fBehyCAX-vz9jWtjLNQE-hFE0t1FZA3KMwpTzukWlcnN0mNxUKVUY-6FpKkngZE0TqIqJpvx_f2J2QeKqkG6o0zyOUfMLkzbFHOoqrOx9HDz8f0EY1xGvlahllm6wyW181FyprvC0cUxKLiZvczu2JQ2VmoyuKrqfp7ayMhLb2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75386b7e5a.mp4?token=oS-UlZnyWjAWuoX3Xgo6KKTMMI0ThoLQV1l1gbQEzoKv_kHNUOU9vr5_-gfW5tBMI7jPBeP1Dh_cPxNvJc5cmabtB7yXcyhjWgQMyRQkQZFAUlSZPmkPefIjIgP2igvhOzQcdPWYfNoKHY5gwvk-1_wfR6PqVuu65cnFipKvXi1rDKiyUxJQE6AWdJVFdw2Hy8Mco4JjjhQsAEbt1GPcvyFSlpbmDxzIAZWTq3K-raMDdOerDdMqm_slxChOk2TtY2TYZSmHoVPxazhgP8f3EUX5njjwIiTW7lK0bj3KCjxvvY6k-px0vi5dx07rvv3I99cWBmERhoOKOc73B1jjQ26hZ20-kmtgRfgjZLDhhxAYlQOamkb9O3JQ87dCxTSlKNuqGuYRqIVuY-EtIt81CJBJQiMij7ehHAvb4splyRr1mZzU5u32LpRG4nzCtqMFqHk7okEAxz26bLEC4z4Hcx1SC6YmhJYOpP0c6gOaavdxJkXrWtvJR2CQTxKvUFZ0fBehyCAX-vz9jWtjLNQE-hFE0t1FZA3KMwpTzukWlcnN0mNxUKVUY-6FpKkngZE0TqIqJpvx_f2J2QeKqkG6o0zyOUfMLkzbFHOoqrOx9HDz8f0EY1xGvlahllm6wyW181FyprvC0cUxKLiZvczu2JQ2VmoyuKrqfp7ayMhLb2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لبخونی‌صحنه‌جنجالی شهرآورد 107 پایتخت؛
کاپیتان تیم پرسپولیس غیر مستقیم به سامان فلاح میگه من کاری میکنم به تیم ملی دعوت نشی‌ها!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/29035" target="_blank">📅 14:17 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29033">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lAUi17y6bg4jQ-z1H0w-q7BPY59EJy435cUO7yxT91IFGwwZzYmax4CPUwcjYQmzv9cSEc8LM34GXkqJH6coL0kSLwP-_bqInhvx6DL7I-zshaOqhx2Anacc-2R4Uj9bRqYKq9d--RBc3TPAT5BWRC848UyKsnK9UBCMpG1h1elrIiOz0PulKlE3wp34dxaUir9AwMUNm04fL4UYOIkLLSIh6-p1fyIw5ABHsZklMTdE0lNq3mC_FdQQDwhpiDfRoNBcvW5Hxw447PhdK28zzbq5NChsfXulWFe__hgmZbXnQC-W_qk-M-JU581ETooqjeiknDVY9wATHdY7OE_KCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jh5jayyp82Ahf1I-NbJz1BbFamniJsGXPwXxzCUIya0Wdai6e6fbxThBuV78HLm74k7UFM-qFrr3NQy0sZUxodG22L4SJXb5vKR4jqI3faEroieWsWxJcrYdUYEH9fY1WioDxYXaG14Wcp_LUsRJ-sPpYcE6ki8KyA2e9eolx7js5SR6SZsjaN7ZwuoybKq5BH-l4rHb8eIe3VHoAc8AZE7glQug-OuJl-AVpgwiJqrrkfjPUVgyriiWj2iExsBFo0VK9TdEnXFYlSpFnwffN-iUlpXrt_IufpNThPz91nSmRX97oGQe6ghAdAX43ELFyb3-voirBmFpcA1CLFkkgA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
ترکیب تیم منتخب بهترین نقل و انتقالات لالیگا و لیگ‌جزیره در این‌پنجره؛ باهم اگه بازی کنند بنظرتون کدوم ترکیب خفن‌تره و میبره؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/29033" target="_blank">📅 13:55 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29032">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bhJjujtTcEKyCpIH2MzFsvW3yP3W1gTe0sqQTP671qrcH0F0uWVR7f0mwMAre6levQqgl-eOv8YhF-F17UPQad8H4DYnLaWBG0Qt8jOOyxRp7GZ0nnrBHQv7maqWmGkDbNIUoZrp3xLqLvKRDHM2moBSwiYg0wIGMBWblkrns8mY049lp4LOV-E6PicLROrSD3guHH-zsHng7qykOTCewbV2KeSizV10MGM-6V9BptSsfJdkasxGqJ473liKGhr0ExDZrKyDdHePQQhTa-7sZlov8iMRMdKemd21x6F93hqHT7qD3_s3kV1beuR64CLGRENJ96iyIvBaNCe579w3iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🤩
دیگو سیمئونه سرمربی‌‌اتلتیکو مادرید:
3 بار درآستانه گرفتن کاپ‌قهرمانی چمپیونزلیگ پیش رفتم اما هربار کریس رونالدو اونارو از من گرفت. قطعا اگه رونالدو نمیبود من الان سه قهرمانی UCL داشتم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/29032" target="_blank">📅 13:47 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29031">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/989a5b2f6a.mp4?token=IMD70inGj1HEn_2r4GUo1CGg6xOPLPd-EWHb-j3RfL4I8A_WqvCPrwgtXMTSg5HGVIp5DDW5tRAK-49M8iL0HeKsM-CRqW4S29KzznbW_V9KSpprjKNTbhHmuggUVZBxRdlN0jWB4DeSuXqhikNUaeOrh2nScmAUqANgT-MClk3KmPQkxHizRxgTVOr6L7IgPOen_WXWjCq1Br265cBcQFVqsr4ZyfLbyPFM1iKtNMN3wAs1GJ44vVEYVRqQg5fKiUyplW1nO25PpGBf2OAg2rM8LfNllO0xARN3fzMf_bm004WbzeZzDT31GdLlcgtCyKcBmhr6udKPwpGNKDD02CnwPz8sK2jEVEDw7CviMPE6Pgt-1ElEvBVBdv_RlJfT1xll5Sj4u5HiUvlu5PL4jywUYjucwRQ7PDOibtrgIQUppU8NBPX26EsU5_7Xl5ai3xYapAdkbBMYayw3HSPihghHnMyCUSkJmdQ_2HDJu1rfYK0zjeRVvjyyq5tPtw6MZC6IH8x28b0MyFa-4vBKErPfG-YtJdn28TPANn3B6WxzXWY-q-eIJln2JKE9bnXqIBlxldrQ6uwxkpxpN4_9BynGQbuRf9Of1e6Z6wzmoLxOkV-UeWs_OBt9Jpy685Gr-uVi25VvjIFJtvD7RvJCSHegcBc-1h4504Tp3BIb_hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/989a5b2f6a.mp4?token=IMD70inGj1HEn_2r4GUo1CGg6xOPLPd-EWHb-j3RfL4I8A_WqvCPrwgtXMTSg5HGVIp5DDW5tRAK-49M8iL0HeKsM-CRqW4S29KzznbW_V9KSpprjKNTbhHmuggUVZBxRdlN0jWB4DeSuXqhikNUaeOrh2nScmAUqANgT-MClk3KmPQkxHizRxgTVOr6L7IgPOen_WXWjCq1Br265cBcQFVqsr4ZyfLbyPFM1iKtNMN3wAs1GJ44vVEYVRqQg5fKiUyplW1nO25PpGBf2OAg2rM8LfNllO0xARN3fzMf_bm004WbzeZzDT31GdLlcgtCyKcBmhr6udKPwpGNKDD02CnwPz8sK2jEVEDw7CviMPE6Pgt-1ElEvBVBdv_RlJfT1xll5Sj4u5HiUvlu5PL4jywUYjucwRQ7PDOibtrgIQUppU8NBPX26EsU5_7Xl5ai3xYapAdkbBMYayw3HSPihghHnMyCUSkJmdQ_2HDJu1rfYK0zjeRVvjyyq5tPtw6MZC6IH8x28b0MyFa-4vBKErPfG-YtJdn28TPANn3B6WxzXWY-q-eIJln2JKE9bnXqIBlxldrQ6uwxkpxpN4_9BynGQbuRf9Of1e6Z6wzmoLxOkV-UeWs_OBt9Jpy685Gr-uVi25VvjIFJtvD7RvJCSHegcBc-1h4504Tp3BIb_hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔴
👤
👤
بوسه و درآغوش گرفتن کریم باقری مربی‌پرسپولیس‌توسط‌سهراب‌بختیاری زاده سرمربی جوان استقلال در پایان مسابقه جذاب شهرآورد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/29031" target="_blank">📅 13:47 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29030">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tYYJ1cTfUnolB9auxzgEWeFSchRTAKBNNA6rKzSKieduOlrg2RociWZ-od9BeUxrLYKS_jZZ73BKg_hogXwwiiLdBNgO2yU0KnY3ouddSxV_MguVkZfFBBiqjI5xaB4cvflfql4LCWF8eeDWUleEJkNdz9pbZI3J-SF4f-WYPDor7eF0ugNGjpfaBcnPzFO6idjTGLW8xk596P3v6c8ZOMUnd1jKyNHnxWPpUlly_1IxbeKNSgm9K9dORMRlhg7hxaQhz74PHLVGluu59Q9_HvxUUkRB6CyFS6LuTIZFpVR9AED0awrANo3RVOaw3IpGsSy0R7b2s8pqO-sfUzqJOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
هفته ششم لالیگا اسپانیا
🇪🇸
رئال بتیس
🆚
رئال مادرید
🇪🇸
⏰
ساعت ۲۲:۳۰
🔴
بیش از ۵۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ بونوس رایگان بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔵
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/29030" target="_blank">📅 13:47 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29029">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n0Pd-Cz3whkIYzr5Ey7tv57g4bL4iyywZCTsFzG4LMLLVPbUpOV8ia1kgkiNYZmIkKLp7g_B-oz8-1b2lYDGxbqjQEW2jNmsscDtwYr3rZRg4GSi1_VUoJFCzlWu5YHWH9qrMj6VXoMDIgExN4P5PBrCKK8APnRnrhNsUIYqhir545_Lf8scUDk9eBlnJ30DWyWuMKVnlJATJwFLHnbbi5yehxoRnLIH2O5clq6m9eK8XaalEgkfiXh1rkei-ylnbd33zWpvYP0x11eiRX8NHFYKp35GyFUK7CcY5pHq22S2m_F9Y3kR0mEJgiLdZzCDcQOUgGdCUQWa1n2qdWcZaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
نشریه ESPN: احتمال اینکه لیونل مسی و لوئیز سوارز درپایان‌فصل‌جاری رقابت‌های‌لیگ MLS ازدنیای‌ فوتبال‌ خداحافظی کنند بسیار زیاد است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/29029" target="_blank">📅 13:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29027">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t5sgq8yUKHIWlvFXNn47N1nGyHzN8pMkFH978RPfSVrF7m3OMqqg4h3NLeTSlh4xMOtiNZaOJdpmV978nMmjz3WU_SITPa5Bu7485Pb-f9R53WeHb6sRFr131BaTYcPjEVppxdN_X_4cmI-r0zjrroFHlJ9tzHx2Z8HdiBMSYe4dvM19eKhn_3LopwH-2K_008Uj-ZJcPlKlbPXPIXip__Kc7zyjEvnGytTWqbqnBjxBpwXTMCcU6jsIWiM9dlrXxpgvDCKW11tOHX79tpy7y0EKJbhnR2XL-Ara20GvprQbY6Airq5krC5D-5AF039yrhvJ9n1ONz7t2ueLj8JepQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EEeGanDhTf03jy5U7nzQi8ZE5KR5qELcVLOqgiDGr5iABcFHI9D4zuejj9bUEXxCxPNzJectlPLnQXvmvtgnnk8IX7rrLDy1cYnIUGk288CaPpia_mNa5HS810vHB4DHNn933neYh32OiviHNNWKY5Vi-KP_S6icskqtrEjBUH9eqa-saNbzI_srtr5PcGz7-IH3Iahx3-K72Yc_Tn_2S4YIyR0XiknS459Qb2aEffWW27hcKCVOHlBLqeSn7C_44JN5tQdNWfhGBjcMs2GdWaTdn13TN91LtdRfVh1p4H8kDlg0JrOp-uF-JSdyQ8WXeQYpbRbJpf5RZxycPjhFAA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
ترکیب تیم منتخب بهترین نقل و انتقالات لالیگا و لیگ‌جزیره در این‌پنجره؛ باهم اگه بازی کنند بنظرتون کدوم ترکیب خفن‌تره و میبره؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/29027" target="_blank">📅 13:06 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29026">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nSxELYevRrnnsPsegMjGd-QIBXKj4zm1FvsnnzG0f2hXDjQdq031h49dnBMlp_zpM65RuEkWT-OLaUM9JzlK4byg_lR_GZqTTFynf619J_6JbNMzcgE-JClsZiwjx3Sob-vb7xrKKANqPZstxD757Elnz3Xb2giUofmHGt8MNcLofmWFdJylcgiwrKQxzJg-64cCVEPemE0ivfcX4fWdSQHMAdja2l98ljmathMHV5SPhWD6gCR7oK4Pip9kzkecsGxJ8MykWDIv8z7VPJAyzeobizQY4kCqjGmERDVkBtQK7w2WnO9jHKnD_Pi5aK5kJNS4q9vbDAovECDoGu9NRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سمیه‌اسماعیلی‌ستاره‌کُردستانی ملوان با عقد قرار دادی دوساله رسما به تیم بانوان پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/29026" target="_blank">📅 12:31 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29025">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ae7_CnDg29pU8cns8M09IiffgfdQVxZMfAuEa1tNDqnL5d0p_ZN1SD7mmXn54oFwqrU07Jqh5OpiHcR19Cz7eCjYBN2gpfaGXbPgfr0QEXKUM-mvDFIV6CV8cQgsWyldDnxVAq3h_3ZxV2-3ROpeXAgFc51sn9PrHlawBpM7lx1esbRAycYwNKcbV_9QkVO3mgMp5PKDdhTg4FkqITbDqEgDoNcoVerEPQSR0C1dVE68BN5n4Y4RJ6jI0ccXlRx-5YAkSx4DBDzj5q4KQVAdms_6qPMz6lrs9DTKfdlhDJtg07afSRwAiKvpMO8QlnP4rjnTglzk4rMpeQihgMsaew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
👤
👤
بوسه و درآغوش گرفتن کریم باقری مربی‌پرسپولیس‌توسط‌سهراب‌بختیاری زاده سرمربی جوان استقلال در پایان مسابقه جذاب شهرآورد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/29025" target="_blank">📅 12:27 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29024">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5yRrMGSf7-H-ysb01406uQbWm1DvfRmoEoFY3OkWZ2Xd__4cG9tZkwbY7Ure3rrbXUqnwAboNpKEsHntWdmm2X6Ar7tMG9mf54qojoqTB87QTspG9wLnBdfS8jeklZEw4j6NtDsDHzSx8UNazQCMV_GI79bSpILAuwxOzka72KMdS1FvBg2SwPhdMRt_0WjgcrZaRRhrQFCM3nDlMA_bik5WTllyivKtGaXQVaL3tE0e3ks_ymsu6Sb6-cyHUet7Il_xm75nnLeaORA-PHhWvDS75k-O4S8jeb1g3G-pl1ZDdESoAVf2XE5Og9ZyATCRfa8iJrxJ62bXsPJDrVCCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سه‌نفری‌که ثابت کردند که هیچوقت برای شروع دیر نیست با حضور علی‌آقای دایی از ایران؛ اسطوره دوست داشتنی مردم ایران فوتبالش‌رو از 23 سالگی شروع کرد. ماهی رو هر وقت از آب بگیری تازست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/29024" target="_blank">📅 11:44 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29023">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6ebccea1a.mp4?token=uRaiYqUl5XjpeNEd-dew8X0v4dcFisTz4GjKE_TD9mx-_xnXbsqBmEelowCe7hE8hpfxWf2PmRXg3X7cufOaTodLAPrNi8dx9G6zKfs9p44QVJ5gozNMwrd0okwbCg6Q2899WTdGgnj3BeOUitWs2ZNUGheqxs538Uy9nd4SICOkG-MpfYPISmn1_KHoRxRvwkagsw39OrR24_2kN5g31tAQ2gEBeqI1PVdnRsHPhbDvaHpIz3Z_N0BhmC-eGMyXBvsj8lwY_tK9RlQzgLvcxmiA-GIDV-ka2yvreJOssSShMEBLZXrhtC-0i5FxmoIgM-EmHtwt6V-Kdqn_HwReTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6ebccea1a.mp4?token=uRaiYqUl5XjpeNEd-dew8X0v4dcFisTz4GjKE_TD9mx-_xnXbsqBmEelowCe7hE8hpfxWf2PmRXg3X7cufOaTodLAPrNi8dx9G6zKfs9p44QVJ5gozNMwrd0okwbCg6Q2899WTdGgnj3BeOUitWs2ZNUGheqxs538Uy9nd4SICOkG-MpfYPISmn1_KHoRxRvwkagsw39OrR24_2kN5g31tAQ2gEBeqI1PVdnRsHPhbDvaHpIz3Z_N0BhmC-eGMyXBvsj8lwY_tK9RlQzgLvcxmiA-GIDV-ka2yvreJOssSShMEBLZXrhtC-0i5FxmoIgM-EmHtwt6V-Kdqn_HwReTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔴
👤
👤
بوسه و درآغوش گرفتن کریم باقری مربی‌پرسپولیس‌توسط‌سهراب‌بختیاری زاده سرمربی جوان استقلال در پایان مسابقه جذاب شهرآورد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/29023" target="_blank">📅 11:12 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29022">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">▶️
تمامی گل‌های هفته پنجم رقابت های لیگ برتر؛
دیدار هفته‌ششم مسابقات از فردا شروع خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/29022" target="_blank">📅 10:46 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29021">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JcilI3mkNLe5BjG1gyG3J-gyNgszdhtfOyaazkkiG66SJrhsC-zzuC-76GiY8QYxkrbstWqJmqV4KYwIrA4L08M40DLkn0jUGg3kJq0i6DTCzhc1oYgK4rDjG_w_-c5xWRUCMsue-vMEI3Thvg149fQsKzo995xAvp_s1up6YGyB_qMFpMOFUlT-dbK64CtSZfR00GafQ-wCCscabubiIAPRsINq5Un4l84tAdd3GVQZvGdSCpadmcJTigztfmMmQj6dvFripfC1ESSG99nLvJ-sw46PTixgyylJ_Sz-QwjIN-LRMzIB8lB7SMr3l7ji_ptQ0m7qvCtv2gZO4CdKtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق شنیده‌های ما؛ باشگاه استقلال در نیم فصل تموم تلاشش روبکارمیبره تا رضایت نامه مهدی قایدی رو از النصربگیره و این‌بازیکن‌رو به استقلال برگردونه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/29021" target="_blank">📅 10:30 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29019">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dvRTd2Ej4JBslH4Yj6xDeW99UcRzY0vr69uFEkpV4hHRxjfDU8ytMyWkInGTfTrO7C_IETHkY657CS3-M4N4Qee_Gr_sukMUVkjVq1YkBXqkfnlPVoz4upZxs5iRe20UOMJOQjl5tfsdqepq1rH4esgatVIYv7hcJMjq-SUVzrSrLTXLIZeeienWXvzP-Oh9h-Z_qC_lDw5WOKTL77KU8KnxdqUNsQLMGmNMj1gDBF-mDdNIURWCZvJwmFQT0a7T949GyFfdXYp3afS7c3d_5zDUpK5ih1eaqvKMhrqZYedx3h2QPRBKsTnIVeswP6svkAdGifjkzbs_i0jetLT3fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V5gIz8oVZ5bZbyyuakPRAyl4n6o5KSr6u8k5wSDlhjE2p6TLWwTFyEtYAO4TRwkGO08psdOQAxE6c1-lFAjO1Tjiwvb-8GNCm-VMcD8vCSEbpJ9-eHibsinURhJRCxRlca1L6DiELwO9R3WXVlJvTOIav4hZpSSYY3vEzXQOxwJpNJ5mXASVvWQExQt4bhjCP1krWcGPCYa2LnpXDVzRHqcvkBffuVMP6-8v0j0OkPH57DDSD148k_gi5a3YlhWpezhyya7vfUMOUq_cj8DAcbgLYqM2NxP-g6MKGn2KxoiaeefXUw8GSiMJZf9KJXCxPEQCa3IguWz90I6DOSHEDQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
دوستاره‌‌جوان‌تیم‌ملی‌والیبال و فوتبال ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/29019" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29018">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AHZ0wK7QVDPMB-OLTMMuTHz6fSumiQJYbxUgbOVmv4hyssyfM7lVZDGZetuuIQcrfAMIl4qH4MP9ZMaUK501DGtVicD9LelpytAFCqkcNZbCkvDZqQxxXcyZZTJ3kvRVxTATBRZfsmJm7o2MY8HWB71u4eGn3Yim6_ATEuRlEb744kKa8UoRG5PHvzkFQFTWc8HEIq2u6nTp919H8GLQnLlG5gfiLMYv10-cDENleE-Q1cckFJU-BPEhZtc6_wQ381k4YAD3Z6yXi6E1RvHmPDbwA0pJb3Hmz1TxhjOrwH1eIsy7LdFpTh7PLsVwDgmKSDy54QAclVDzdc9sFxsZuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیزری‌جدید‌وجنجالی‌ازسریال«مردسه‌هزار‌چهره» باکارگردانی مهران مدیری. مدیری درنقس عراقچی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/29018" target="_blank">📅 09:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29017">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ks6c9jAYOUjsSaOYkbbP_kTqbnDvk7yN4uJo7Zg4IqiFW_MEaXbTBBBPfRt_-wFQJAf4VKXLe2q89SPgR9zdVf2zQvbFOZST0H9m9ijzgIQYZo6dXOfYa3ZRbmv4I_qD0iJ2l2FxjIBeWLTjEQ3HrGNjlrtLVEb4yIEIDDAw0wPkwiGb6ocCHjUJeqMjr2FM37_3hPhd2TYZP4oNgIPpfFEWovrXYeuj1CNNx0Ap5kYknk6W_oeqBpe5G9hucJII2aIQbpCVOzT_dtb08L961ID4cgNH8Lda9mVORk3LlQ1pG4W9RPoKcaOWapEvYBK2gOSATwbKjW1GQEVukrQlXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇧🇷
گابریل مارتینلی و همسرش بعدِعقد قرارداد رسمی با باشگاه الهلال عربستان؛ مارتینلی در الهلال سالانه 22 میلیون یورو دستمزد دریافت میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/29017" target="_blank">📅 09:32 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29016">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iIc58qBzwi8ojchU68_gfJ9xkamiu5FCCPqWWCsTw8tdyJyErkHvEcbm3PTo4v7XMWc4ohMWK91JSssDrEs_ynRwKFRbOGeC37EjY4NmWFWk-eLT2m_KpsOkwfj8sAvyj48zY5640qGTm5UfHclr2yTF3nbZ9WIgaGYbF3R409o9UoqcmDXi0jKMVR-rT5onZM-b7OBlevkE4rEzOAYOjjs_1-RvqMSooGbEFp5NOHfYUbmPDB7rkM_QHaxy3LEnb6hMuutUYZbvDiSEecnxvoTTTfpCD0gcUAu6nqLJaSeGHmhr9NiUQ5OeAmZlzmDdLK3xLSCSkCsSXBhxdwJ7RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لوئیس سوار: من قبلا با لئو حرف زدم و هماهنگ کردیم که با هم تو یه روز از فوتبال خداحافظی کنیم. قرارداد سوارز بااینترمیامی درپایان‌فصل تموم میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/29016" target="_blank">📅 09:17 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29015">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-HGAQlZP2ApYc5N7Mqlct2RBYh0FiP1IvHjoqpAxfHPQNjl0RhsI4fBpB8c3xRAX1n2NT45HiUA2H6OBhB4vQN7uly8PyOe1e_1RoJbIVcVx27ot2L_Pc47QH5jWfarllamwyOa_6NUV7txBb-UJn9UwkOHj-HLfPDoXuAqxChTkTtyV4Wqbif1Rh7Z6pce1tEzsiDlQVkKXz7UvQZs6aYiVlnvVamBl4DvmMls4pnbT8kpi3ZYHtQ5zrAomrEHE4IUzwhPmtJVWWCYcM3IMdbZttfcsNnOBPhkMZc5UZHr2UtlTbuWUiXEkYnTqNGHO28n6ud0kjQQVsYe5znJVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب احتمالی دو تیم رئال مادرید
🆚
بارسلونا برای الکلاسیکو حساس دو تیم در روز سوم آبان ماه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/29015" target="_blank">📅 09:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29013">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rHmCm8oVm65MegBPh6F6FN8U4q0O1yq8Cw42MJ08RycMMMt7f4CH_TOaSpeQlmZLEQR8L2SymyJV4xkdC8KcrMLuiu2Dz5SiJihFN0c2l6JnEhezGeCZU--FGT2lzO2k0I1d0vGMOlSeME5wZPZVieaJGz2J-yP1sXhkGxHVpEEyioztoKeYF9QSwkTCg0RtE_HoV4U7KXncVzILB1Z77YeqHVh__-KrhuoBO2uE5ew63AOup2tFr-7-jVjTtL05OE23bkt3snafgWr0_T1QaEZ_9x5iuKBVZoza7TXk3npAl5lqUub7UBpNARlkV3C9_HdCXTwP_Yk2nVMQGSlmUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌‌امروز
؛از دوئل‌شاگردان مورینیو و پیگرینی تاجدال‌لیورپولی‌ها باتیم تازه‌وارد پریمیرلیگ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/29013" target="_blank">📅 01:01 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29012">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hjtk3dPjXxbZDJr3IHffneSpxUo_xbM-vWLN_68Zy5ihSjaDPZoQHw-IyBQliyyXuS2eSP-_5USIhguXvX1RRh0Ky2NnOA2JKgbx6aFA_mKhVqi-zcPP28pv42lUpNOGLN1p3gHb9fa024CDSqobwhwjmV6gQKNyoCHoJAyTJJbM74hhqwCRvGWpcXcuoyfyir_biDJxSUZatMlIMofbdOkliDNhgGouBKdr9m5E9ik_gGmwOiRdHJcBroPmJLYOVmrUbr7f_FQxebBzMBO5kcUbfJHzLybqQT9Z2T74OZcprJHVAHvDIOxXj2vxcN9aJlJe6RHHYt2P8DmSJZ-rkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌ دیدارهای‌‌‌ دیروز؛
حذف یاران نیمار از جام حذفی و برد لخ‌پوزنان در حضور 64 دقیقه‌ای الهیار
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/29012" target="_blank">📅 01:01 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29011">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bfa115327.mp4?token=YKTBAJ20SMbpzmtteVsFrS_u6yi8Xd_aKPYRe-7mRhNx0EVmJOipYfKqnR1Uv7yrmxerno794slRtacJb5Wrq2l7H2kpSq9GxVRbtpU7vCExRzIDdlFJbAUJyZU4vhii5kkRisS47901XGDegjJBKjC5VsJ6JyFFlARERzFQxoEfhlp-l8JM76CXXyI0V012S4iJrRJVoPG-wLvkzo1a7hxPk08GAg5-sN9rVumgXkYPDOv4BPL4ljoOH6SRj2c2uPuwQx3t0-155dJ2sSX2nY3H6Jga0oVb4pB_Mtiauyds7fvgGIR3pRVeKDIoG135h5FbaiDYC-WXxgZ7oFYFAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bfa115327.mp4?token=YKTBAJ20SMbpzmtteVsFrS_u6yi8Xd_aKPYRe-7mRhNx0EVmJOipYfKqnR1Uv7yrmxerno794slRtacJb5Wrq2l7H2kpSq9GxVRbtpU7vCExRzIDdlFJbAUJyZU4vhii5kkRisS47901XGDegjJBKjC5VsJ6JyFFlARERzFQxoEfhlp-l8JM76CXXyI0V012S4iJrRJVoPG-wLvkzo1a7hxPk08GAg5-sN9rVumgXkYPDOv4BPL4ljoOH6SRj2c2uPuwQx3t0-155dJ2sSX2nY3H6Jga0oVb4pB_Mtiauyds7fvgGIR3pRVeKDIoG135h5FbaiDYC-WXxgZ7oFYFAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔴
ویدیویی جالب از آنالیز کامل و دقیق دو گل استقلال و پرسپولیس در شهرآورد 107 پایتخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/29011" target="_blank">📅 00:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29010">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mhZOpXtav9Rhz1JWuqTz-JbURvL5w7OplyLkj9JVzk0ZlDFtmtEny3v06Ms_uBZZG02K_a0k5cE03GJVwYAI49-B3KoOAhOCNn1XSvzrV4GD39zjYjppaTAd-3NKmtp-Qj5j0ISERdMV8xqAzhLvwkA4kAP5dU1JSTg5Yy7rnDHZ28KgzEEXKMHuVshjplOj0Tif1G14Erb0bUUJ8BUm3GhQm-xr85B3y0bOSMHd0Q0etFRP_xwQE1M6YT3xVI0t_bNOSeRw08P65cF2OJaPS5MSIjW3yOFmmEV50rSKhUNqSpu_6dU9slsPd9hsMx3jiUF0R3TnOJC3HKkIuQnRXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
پاختاکور درپلی‌آف‌لیگ‌نخبگان در شب گلزنی بشار سه بر 0 الحسین رو شکست داد و راهی مرحله گروهی لیگ نخبگان آسیا شد. این تیم اخیرا مرتضی پورعلی گنجی مدافع سابق پرسپولیس رو به خدمت گرفت و با این بازیکن در آسیا حضور خواهد داشت. پورعلی گنجی به بازی امشب پاختاکوری…</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/29010" target="_blank">📅 00:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29009">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ak1pFFu3lfHl-hTh3031dtcnV-d2_oaIVuTVKQz5VEX4iWWdUlIh85Jb-gVzYyhWIGDhv2MPclGIVcS5ehtKwDpzzNYoo3CAO83iO-z35_TWSmvXN-tX4a03YFUr8WjDyeYJTDPmcbZ4UTfJjmcbz4TRlWNQaYJpaNC2cq1qS2BKmXwODPI5eIhXq4kwaOfYPTF0eV64sAbirXpD2vXXo-vjVLEpo2wSNw4AthBTrWy3WZMZrWdWPtFcsIWkWAPiVwMM98LV2qstp6FAmt_vj2aF4jjqsEP8PUN2jtl6i_f7u2zR7sTyBn2kcCbMO5et-HKlrraDCPF5120yUIcNnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🔵
#تکمیلی؛ طبق آخرین اخبار دریافتی رسانه پرشیانا؛ روز شنبه هفته پیش رو باشگاه استقلال 70 میلیارد تومان به‌ملوان‌پرداخت خواهد کرد و با ماهان بهشتی هافبک تهاجمی 17 ساله این باشگاه قراردادی به مدت پنج سال امضا خواهد کرد. تمام توافقات بین طرفین در روزهای گذشته…</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/29009" target="_blank">📅 00:29 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29008">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jai8jYHGBdrlXuboAwS7VgtK9pziWBcmACrlibDj6Jdr-2FTBu-1tVrSLninRqJAEna058SRIjkkFN62uQxLR5oVrTMcbDx5zEe7N1ZOt-ZzftxSdPqS5xvT0Z1jxCHXPzWTopl-pOZIBVOZM1LKrGuZgxl3M--8LTokpTEcmWJMxPybwANizAQlqIe_vk0LOt5PomU-UbJ9BvwBVjCEq_BpF5j_euYTxGWGW2_GuqqHopdNyPJaQhAn4q_Z3A6-JUMqlmSKKFUVjrUdYIsYE1gvvoH0z6Uc6HB0vWs6xkcYNkNm23OxVCpWSw8XftEBUnaNRJ3ggBPthhiGAnXUFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
مجری‌ویژه‌برنامه‌چمپیونزلیگ شبکه TRT SPOR؛ که گفته امسال بارسا با فلیک قهرمان UCL میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/29008" target="_blank">📅 23:53 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29007">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r4tJozx-OHIZCv44aPujr9-KRIpWW8dGOj4QXK5MsbS2yrSDR0qFxYZZ5KKv4HV0iSDRGHwhGZvPDAu1qM-P1Gy3A6EPdnp6g6_ssGmvty8L6rZSD7Rml8a0nJHHSNp0OW9W5xigZkoRGsV5XnEWTtgElMRMOImHXhs9MavuIbEb8GOJpme_rckissmeJr3ww_Cczp6EWfBYMyM6dismHXOzOyoGTBgA5tdAyZ3JnAqKigQVdlT8rqNl9Jq-6SRBUFh0pooH76En2j6ikdoKgxvdfB4FIHfraVplDZtthLA-IhCVNQDFRcGpB2knvNBrEknSVIu_axXHSlELoLedRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
بااعلام باشگاه بارسلونا برای نخستین بار در تاریخ خود به درآمدی معادل یک میلیارد یورو دست یافت. این میزان درآمد عمدتاً به دلیل افزایش درآمد حاصل از استادیوم است، باوجود اینکه تیم بارسلونا مجبور شده است تعدادی از بازی‌ها را در استادیوم یوهان کرایف و با ظرفیت کمتر برگزار کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/29007" target="_blank">📅 23:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29006">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZvBXAqxrV9DHS_oCqhM0MFNUQIt4PvYfoRu4howqL5Qw1CLMM090h73c7pgKbDRf3oqiUc7U8TuOraMYJGa143Oug93wQ3WCv7LRJL3gPJ5NZHKNjrnbZoRJvxVJ9OTNBZUWJBmNYD7qDLUftjxT_2EWdyDFhCdXZfbuImIrGnQ2ZQLjTh20u8t4XUJvVKCd0WnCXvSbH1D5otvObHbi529inkHprBMSAj6tgv_FX3wJkAlMpekK6uTKM1grUERRF5x9EDX4fChChUuSEhIugktKAxaMZFelO1jm-azzY8yv3ESZuYa06wZiBDyST6WyLY8tUmh36N6iHWxLW_rqJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
جورجینا رودریگز همسر کریس رونالدو قبل و بعد از آشنایی با فوق ستاره تاریخ فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/29006" target="_blank">📅 23:06 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29005">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kAaRAHao0rCzvasLrYNHHjKIF2xDg11RL6VdhZHOH4WwYu8oS2j6S8soeAHK1t-vlTfLfUyGSZ6ZOrmGEyASYi-kr21btuGSITAvbfgA2HHtUp7xCDx6FVqWkxefXtgjFmu0RCAylMItg1Y0dW7RMztKBviTw8Su24HN86vrAgY9l2qojt5ROGibF6MycuYwP44Cvp-exIet6nt2BeAsiGMth7RSNV1mlbvNSBPPUGg2S7X6bXbq3mwKnVyj1JwlItbe7137GN_7y8M4MomPLolo1ywoZ4G-rp0MpFd-BQ3MEFn50hItTvFKaqaONURSU6SSoj1AevUqtVrFttAYoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇾
👤
تیم فوتبال پافوس قبرس با هدایت ریکاردو ساپینتو امشب در بازی سوپر جام قبرس به مصاف اومونیا رفت و با برتری یک بر صفر قهرمان شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/29005" target="_blank">📅 22:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29004">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H5RpqobieSKugBUB16UCrNBoR1YC66MJoq434DU5MGuBF3bnAAt3crbkKCovS9WP_fR_4eWb-S74Da6yrRoLTcGpGcZ4QopHkJd9Ip6pMa1vuNOrT7eIeSFWFggD2ymbb4LVrR2TzdPhwMFbS4V82nmXBRZM2RxCrv8EpKnWI2bLR2i-mAdbMpthcPKGBBWwZZ--xqWCyZbJ7deSjifN8y0OIO-8sAKSFUXXY3PLTmqO6C38ZcoJeUXXMHPoMll1JcTmK_5fbrzWsZbmpK5tXYvO8d1EtC3FQqqz1mnfiU8mS9KkrVD-Qr9Ap6AbxXWa_bBUsBjdIvOrXpRGD1fWNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
دیدار برگشت شهرآورد لیگ برتر بین دو تیم پرسپولیس
🆚
استقلال به‌احتمال‌زیاد 20 اسفند ماه در ورزشگاه صدهزار نفری آزادی برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/29004" target="_blank">📅 22:24 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29002">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VqqHCx0qQPdu1vGy3FkMSvqAJfNLYfREjhDTxHNZ63vednqhn1j-mESlB9eCpeGtAL9uAkH96TByghY6rhEsmZZAHodxv1wDgEd8rD5gEkH3HsmLgcdpJ1Ytp5tjvTlC4xZLrbGRR36tf7fdV8PBFakFCrmufnzEnjuym8N1MaUmcJNuiGWy4zKwYlCYc0zzsmKS7lMRx5c-uMQiXVuE82FAHnfM6dag8-nun4Ni8xnlVN3dI7gNUcKElEQfgL55uLuo1dZdKLu-LeCLRnkDXZ-eQMUOIsr5axjiSUoCkpepboUWcnAVOB1393PthgNYpNVT9rF7Sy9vKUIO0F5g1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eCzMjOeFNkPE5lbS1Ebc3ZWYHol0qNfvHwv9tJqwgQRVYel7rI34ndG9SjhJzNNyXvrFMrZ4uVfp_mweEw7lEKrFsT0X2Kk6B7SEtmQzwsSj3QuSUTKIU1WfEKeJ6BbPe7Gq9OxiysXRQrYYhVp-r7ZYe06GO2rVP_E2Db6U2zgnXJFRXmFVPshAiicXZEnCTMgtdrREnPCAngXJy064S8i_-zxPBQPuBHm3QBDFF1ONZG-eGvEBgnu-4cepZuhea0G2CH5FLtuzsiuyU2MZmoDHrG5FRHw4UNJqRviMo-KCTZLAxptll3WLJGd8-CzRcOtnbL1nahs8koVu3gyHDw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇹
سسک فابرگاس سرمربی‌موفق‌ باشگاه کومو درکنار خانواده‌اش؛ از دختربزرگش که در تصویر مشخصه‌ پرسیدن رویایت‌ چیه؟ گفته روزی بابام بشه سرمربی تیم بارسلونا و تیم ملی اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/29002" target="_blank">📅 21:59 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29000">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b2K5LQ2Eyx9KSOsyGE1JJi6XGuwpKZrPu50EeSlRiu0THQEn2AO7j_TkbpvwALVezy2VitbAo2ySZkE_q97Iz6Mc0S_mLBfSmTMr2sbNlgucSgXPWvfoHyv_H9tCoVjLGfe9ycCNsAKwi_6XebWA2k8lrphqHmikCcBY6aSBRScmCOoHUIFPTnoy_0xsclu0lSe4ntiWT7dVCcgIK___GEHcX7r6H2InVlJVb7NtGhG_z6Ccl7JQotfPaj-ypT7rTBN-NdTzEGUkY-F1RMg_soDBfpTj-5K-CZgJGj1DB4COyJe5Be3cSypZbKRtXzAPoCCPhQrHUJmn5zvef9XcEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eILuA7acWIpJVBweoJ2oaSxUerDokuPv9WeIEhvVuSJDpiCa361Uuk5ZkLEpJj1Nw7dLGsS0M0Rxv5sIa6GPgZMkk-Cr_RpROwbO_f97K-8H3hXby0nRBRVhoOiZJAeu_PsbDpVsMPTCO9GW3Rlple6Msf3RLVeW2eP4rEZ2IJRga-J8VZZ9Nl9Wsz8YLt67p90ll6ggmkJZA1wyVvB3my4jMkR1wF_DUP9CpQb2QjQ2O0IGrj-KiNI3EAYNUZPGwgPUioh4V9STOHOJ2rcGYEmd-GwyEVvwE5D1Td3fVyW4S_HLXTu5_O99n-nyjEBuGa2KiWS35qX3ElOXCTHJsw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
#تکمیلی؛ جالبه‌بدونید 3 باشگاه بنفیکا، منچستر سیتی و چلسی روی‌هم‌برای‌جذب انزو فرناندز ستاره تیم‌ملی‌آرژانتین 282 میلیون یورو هزینه کرده‌اند که خودش یه رکورد برگ ریزون و بزرگ حساب میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/29000" target="_blank">📅 21:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28999">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QDUZodvYJK12bLwKZ_8mrnqsnxwqd-DuesFUimRJOVWt9UHB6kYZkiCDZXV6Jw9Qd30AdZClSt4mbaDQWeRtx_jptzxf2vABjhnQO82CQKgH9UBI-XjQGXZvLJPhkhFYmPfFegHuLV5OK6ijP6SlCi10o0PuRviJqO70fvMeWzidkg2Gb-y7tc2qTPkmOfSslhDhrZCwnbUWeWKApXNdE1awT5AkXshMogO4SI5f7Tl9FoSfmef1lTIeY7RuzN_dNz87xlQhIqdnjS1qUylDNo3uvpQv2WkBrdcVfiNRm4YDyafq0BYStD6k_3dRgvTqaC1y1c2oZC-HCMyxpZTNOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇧🇷
🏴󠁧󠁢󠁥󠁮󠁧󠁿
درکمتر ازیک‌هفته‌باشگاه الهلال از گابریل مارتینلی و اولی واتکینز دو ستاره گرانقیمت و جدید خود رونمایی‌کرد. عربستانی‌ها روی هم 150 میلیون یورو برای جذب قطعی این دو نفر هزینه کرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/28999" target="_blank">📅 21:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28997">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BbhqmqFNwxklxs8_nVRxfs55UHHCeDE9QoDpT62ODG6jtg8pIDWQk4O8NarvK4N6eFAP_NlGT1hLa5NU6BUfW7kA-BPj1I_dsU5Hu9ZiKmGXMac6lI1w6V_NqaooqVKbZaz7hCFPLdc9yOCd6kjjZLpYohMcvh2fxuKYn_lgLXjKy7Z_tDVQNZfoMEHfqYNG0T6UsXluVfAtqQtAn8RQ75zM3oPDeACFQSvzmxqUrOBX66Pdfi63Njm133Tjj3I2suKHJbBfqOywJP_NC4HngczMci3bbtzCccFmYuk4gdITzhc9jjOxZ2iRx7mp5yvQoNLrv_kl7d98sDQCuUR46Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول و نتایج دیدارهای هفته پنجم؛ تراکتور با جواد نکونام صدر نشین لیگ برتر باقی موند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/28997" target="_blank">📅 21:18 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28996">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UuTseTJExtgjr5SRqbQI_HTrOr-GCmKsIoiyGYQn1N9gNvalniM_SCwWlJSY76kiyW1GKSXImidEcQXON8wQw8S9sQQ26wBPtXFgl32L9tOU6QE-dW4eMIpwyBwYcLlaU9LJo0Q_BhIS3m8Bbu69-H0oDgviSdF9bQgekHWaWY38102BFwGJNcXBfPtNMj-WRnNVeSqlhHnTNS-g9xfBG85En-tvyic5urP_ahdsA8GUG9DkEoEwBI39AbujpLgewZSNkJoxrMJsm7ukYgP1MLP3xMXac6X79fXN64vHWnIEQvjl2A8QntVJnhtqINqOnomPBzc8n1WwW2kFMzEFxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
افزایش قیمت وحشتناک محصولات شیائومی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/28996" target="_blank">📅 21:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28995">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a1c45db64.mp4?token=MMOsIw2x02gvKFcFiqIaJiXUNONQmbnh4ZlqD7OzWwn3e8_2J8X4xY9ZV-T3imxKElkpNJB9as2iZxMAHt2cRrE1C6eOFNmjgmgNNetOqHo59gE6TJK97GFQQOZUM1DDlkSII0p9lussAK4asOWQxJmJHW_s5BzDgXvHlAPsr_PgYskjV1RoBOAX7fIOFYSRZJOveKF302o3oIecJJb9-vJNzRsQ9S5nAeHjpsYI9uQKZriDWXBvD9FCR-uxI6wV5rnZjrdUb8AgF9iWTCo1jD7FFdvzEOjmXqMtQ3StAuEnzJHfmTpnNaeiKRFGFHHLelEDAgXmilfVVl7C71LTFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a1c45db64.mp4?token=MMOsIw2x02gvKFcFiqIaJiXUNONQmbnh4ZlqD7OzWwn3e8_2J8X4xY9ZV-T3imxKElkpNJB9as2iZxMAHt2cRrE1C6eOFNmjgmgNNetOqHo59gE6TJK97GFQQOZUM1DDlkSII0p9lussAK4asOWQxJmJHW_s5BzDgXvHlAPsr_PgYskjV1RoBOAX7fIOFYSRZJOveKF302o3oIecJJb9-vJNzRsQ9S5nAeHjpsYI9uQKZriDWXBvD9FCR-uxI6wV5rnZjrdUb8AgF9iWTCo1jD7FFdvzEOjmXqMtQ3StAuEnzJHfmTpnNaeiKRFGFHHLelEDAgXmilfVVl7C71LTFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گل بخودی های فصل جدید لیگ برتر تا پیش از شروع هفته پنجم؛ هر هفته گل بخودی داشتیم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/28995" target="_blank">📅 20:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28993">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TBZS0CAIaHO2BEAxmdALiNWBjm4iB5OEwV14Bz-kGyAKFKo4VTiJ7lPAzioktUjSsNVKGf6_PIZv0gCFDG2rVsbXuY3Km3_yknIkMmYklYURRe8Wh3WK5Q8gOn4Vgv3bGxYOmz1O8XpiBvlu6oMeTM8KtrBizQowob-wyDpWZyP-0SN9vEKkspZhfGBOBrJ44T1n1SpsuPbgvnoRTG0-fBgN1YXSBfViqwPBwdymkaVPF4IESHDwKsxT6wpgR0Swg4sohzefsm6liHEq_XFWJwN0VuHh8mJR5D30C5p4rAx8UNHX7soyqmvvVh_qFuqDdFlmF5yntXDv35-bm0tdlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پوستر رسمی باشگاه الهلال برای اولی واتکینز ستاره انگلیسی جدید خود؛ قرارداد سه ساله امضا شده و سالانه 20 میلیون یورو دستمزد واتکینزه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/28993" target="_blank">📅 20:14 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28992">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CQMGD3EghAjjtTUR4vOYrFq1iUkYRAt117KhZMeyVbBc60vKR6tKmnlvePNfuHuChitnmrnHDRj3Uw1K77EYxU8HU6jsUZdkncNS5gqj2FGMfY__MH4BDyFETURFf4UFFFXSbt3aHh6uMT8oeDYwvZ0qLsys5QrMJOWexs5sNJ9qJ7qmmilITCcdRn8stkWje2DPBWrWQiNfFAICNCMUesGCJLlvXrHKpP4i8RV9NE1ulalryRAa_HXabcOU826Q_VUCGNzRXN8a663zDdtsunSiG4Qp8JSGyhqAV4V5Ws0RWtFwYHaa2T-D74RPxp-TLO0SUhXds38jAnI-CevENg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بااعلام‌پزشکان پرسپولیس؛ ابوالفضل جلالی مدافع چپ پرسپولیس به دلیل مصدومیت از ناحیه کشاله ران 4 الی 6 هفته دوراز میادین خواهدبود و دیدار با دوتیم تراکتور و استقلال رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/28992" target="_blank">📅 20:06 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28991">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k-jJihyQx35W5ke4DSJhDNzrfRd2_PId70VVXTAdtO2SwTNi1mFkW5dVx_kvNZkSjNh_D5GVP5GG0DT0kRl1rVb8GUgw8Da0KpBqUhwt4KYBU99lKLzpC45jW0NIxjufTav_DtQWP3ldWoITFluoXNGwtq-klwJdbKmmav8lAjLlTXkZomfRJfSijvTMRBHx8iGLHlqucAHubb8tO7wjtah0MAm61gN0_qpCuT_ehu8XZA4LtCVQoKh3xd8L3X3hLf70NDZn8JPv2wUCOhjX6UXk5Xza1gZOBkEXBpoF2EWZrKhI0fGIWp2VfglINaBkCbN1qsVjtf8nTyw9Sd9I0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌باشگاه الفاسي مراکش، کوین یامگا وینگر ۲۹ ساله فرانسوی‌سابق‌استقلال به تیم کنگ آن هانوی ویتنام منتقل‌شد! کنگ‌آن هانوی فصل گذشته قهرمان لیگ ویتنام شد و با پیروزی در دیدار پلی‌آف مجوز حضور در
لیگ نخبگان آسیا
را دریافت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/28991" target="_blank">📅 19:50 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28990">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇦🇷
ادای‌احترام‌فوتبال‌آرژانتین‌به‌مسی تو دقیقه 10
🤩
بعدازخدافظی لئو مسی از بازی‌های ملی، قرار شد تو همه بازی‌ها‌ی زیرنظرفدراسیون آرژانتین، بازی‌ها تو دقیقه 10 یک‌دقیقه‌متوقف بشن تا مسی تشویق بشه. اولین بازی، دقیقه 10 ولز سارسفیلد و بوکا جونیورز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/28990" target="_blank">📅 19:27 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28989">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hn2g-nvh1lr3rBxjOEa37UxuezfaDze5h3KBvz-FRFoXafnDgXpaYVixsSm7Gi9RefXeEE6pYSixlReucxZuvblY6X6QXH9WUJHeco2pU9emQa6jwC3Ip5UYV-3xlcfTVYfIddROQlLWsOuawiDLS6P3r9y9NSWsIOH47pJFZiMw_FHmyS6xv1eTuLHwvMODZpefW1BsHGe7iTyu2TMCbDUduG-qUIpTtBzUVuGSpALdkzFtsLtJwMDp8kMhY9UYfLMQjtwit_NWZ-GF79BScMX3KIkhUBjh6SzH1TRriBupDQInBWuhf9iiwQe0havvpdhsgiW8T7iVXq7dlaDxAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بانوان هوادار پرسپولیس در ورزشگاه نقش جهان اصفهان در بازی روز گذشته با آبی‌ها.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/28989" target="_blank">📅 19:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28988">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b51bad968.mp4?token=UgPiYlfpOeh_vhXF1yFu-FZdDZFm-hp3XW5abrJXYGiJ83KGiovTogvhkUZH8DDHmNWyTZIJaHfFj4sLiuBQpp1eRUVwoa18wyVkqeU8S3DYAsD6U5vGZG4r76LVhOxzXz1RHG5gx6_TqdNWKHJ1Yk-iPuuHXdDwBjV1316_qPCeovkmAoBa0vGVitLJY8vV1lzV8H70Ukd-Gn3gLBioqB04x5mPKfnAjFs-YPYwZq6p9bbAt5Y3vjwrZMIG1rDEhJ_584FL7boup2DPs3kIjtZz-qPEMu3TrNw1G5ylNamhTtn7asY3a11PKcuPsRuOTyIjS5jbjXYvO8Uqi1nSZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b51bad968.mp4?token=UgPiYlfpOeh_vhXF1yFu-FZdDZFm-hp3XW5abrJXYGiJ83KGiovTogvhkUZH8DDHmNWyTZIJaHfFj4sLiuBQpp1eRUVwoa18wyVkqeU8S3DYAsD6U5vGZG4r76LVhOxzXz1RHG5gx6_TqdNWKHJ1Yk-iPuuHXdDwBjV1316_qPCeovkmAoBa0vGVitLJY8vV1lzV8H70Ukd-Gn3gLBioqB04x5mPKfnAjFs-YPYwZq6p9bbAt5Y3vjwrZMIG1rDEhJ_584FL7boup2DPs3kIjtZz-qPEMu3TrNw1G5ylNamhTtn7asY3a11PKcuPsRuOTyIjS5jbjXYvO8Uqi1nSZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
شماره 17 منچسترسیتی که سال‌ها بر تن کوین دیبروینه فوق ستاره بلژیکی سیتیزن‌ها بود به انزو فرناندز فوق ستاره آرژانتینی جدید این تیم رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/28988" target="_blank">📅 18:46 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28986">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lbATrrQmuW6Vy9EYgQQZgdM30NXzdJXHiB6zUQB-YnFAsZXSksDa0JiQbwD_sNo-OUnvbzYKV0kBO7JSwTaEj7ttrrNqBy_79ygjkweFBlUsqCS99o1Kzdk1KMYK1l1hVDd0p2IAChLntvdwp2PxzchxgqzvvCpErySnbjA3ceODL1Av5DLW0iJ8nOeF6oAj14xLr8QI1148wRaXDfGXS2VsH0nMw8rc42fjNGHltoaAeTl1zsWManq-2WkzvMgydaLr4MfpJ_Owz09fB-O8qEAFnqjzJduiR5MFKIZWT78fazhAPttSexi6cYNRPFAy8k7yZe0Wg0Ohffm7rKF6Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0d340cfa4.mp4?token=hMJ8fJKvQ2OmWHlly8-nRrpoY3pqEITT18h-L8ndiweP3GrR0ENvXBuk3dFRhmyI9V25jZZ6eP-jd0LQf5I76QTgjeDuh-aXafR2rh2d8iIRMa6v9yO7dlUyT7MnRrSYdHRgjXtTX4L9hIzktKnxJUK9l04T4H9m2nzpZqAEDbQD4bnI__FXpcEw25M2aD7lJMR-bVr57K7LpGcagnuDAUSg8G6L93iL5K4ROPG-6iMQ4vSbZGVyep_dL4jcnt4fAjhbs-0TzaD7M6snEOx21TXBXz7V-RkAMCPbeOHer_9I_3Mfb8-3yqAdh8ZxvnSzKZT-HSuVgfKywFyID-cgCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0d340cfa4.mp4?token=hMJ8fJKvQ2OmWHlly8-nRrpoY3pqEITT18h-L8ndiweP3GrR0ENvXBuk3dFRhmyI9V25jZZ6eP-jd0LQf5I76QTgjeDuh-aXafR2rh2d8iIRMa6v9yO7dlUyT7MnRrSYdHRgjXtTX4L9hIzktKnxJUK9l04T4H9m2nzpZqAEDbQD4bnI__FXpcEw25M2aD7lJMR-bVr57K7LpGcagnuDAUSg8G6L93iL5K4ROPG-6iMQ4vSbZGVyep_dL4jcnt4fAjhbs-0TzaD7M6snEOx21TXBXz7V-RkAMCPbeOHer_9I_3Mfb8-3yqAdh8ZxvnSzKZT-HSuVgfKywFyID-cgCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لامین‌یامال درمورد دوس‌دخترش گارسیا:
هیچ دختری تا به این اندازه منو شیفته خودش نکرده بود؛ این هشتمین دختریه که لامین یامال تا سن 19 سالگی باهاش وارد رابطه میشه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/28986" target="_blank">📅 18:01 · 12 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
