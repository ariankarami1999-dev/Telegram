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
<img src="https://cdn4.telesco.pe/file/Qeii4NzLuQgA_6lBU6I2ZtyLJ2l7QmCL4u86M7YoAzZmMw1veTiWwZ-YJKVcn4ji18kfdCALWBJpat8UZudBHejaNXtfcxcBHvIfPvYMeziRMd0sDEsV324rh7dA0UZHd1xzxfC-1wOvvHipJ_t0GawT46IwhbB4r_8j5DR4mwGbx-saIYaHWWxL_IeaNKd-qjGr4ea0HsJ-roIKKbg3btKQVoNfhbueDMV8__cUtfPZ_c5BJMmL5WngYUwVBvhVyk-gaoHa6fWpStJspbQEukYXS2SIHWZv1NG4exLWnRwbt3dlRhM9Rp3h84oaM8fKOvZk36mVwCmBF9dpyBvmEA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 616K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-09 12:35:56</div>
<hr>

<div class="tg-post" id="msg-28789">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vXJSoBrsmszdoVzI8ZT7Lo5sLGGHKvKL0XqqGgQNoHbbAZdfFIvY1-GT07rR_eIQQ7os6VdfReHXFVKZsQnoPdBbAVfpiLhp1-sMXkTUfiEZrxHt0Q-1btKQDZCJiCJXp0hDYd_Gdt5a6q8SIsE37dPemh9zW9_GF_bS4Us2mArrCTZPCsV7W_B-BKKbNaJfSRGvCMHbTbovHjis171gqe_Lz1E2sdYl4668LEhxLzeQBcGxv4j6B88LcX5Ke1FOy4PKakIfZ1nQdBHgq2EMyPxUl2mozij60C1KZikQrKnuJ9axEybkk6gsFtbiKkX0spnsV_dnQL4QL-IgkfabxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
هفت خرید بارسلونا دراین پنجره که بابت جذب شون مبالغی بعنوان رضایت نامه پرداخت کرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/persiana_Soccer/28789" target="_blank">📅 12:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28788">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OtqxZWBc8W2PPBYv1r_RD2PQ0O4FRQinjcSOtw5uCREeG-ZO4cg7Htuakw2dh8IeTZViRWvTCQ0GUgHrXniDs7HW6ut_9a6aJir9jBgzD7Ik0A2InFvUB3gcEYfaH6_yIv8vG1UV0sas0ep35CcejXcs9OHhWcYQAFLVf13AefZEmwtJee6ASXlH_924a4qE9Bg73JcgfCOjSuHrJIdZm2suDWb30W0FUTNbkUp-jaB8HDAzM2m2AQ-yHAfWKL0UAVdpvTDReeWH3h03WKs0itBPgAiAyfhEGnEIgt--cImbZ1VbjQmCPYn9jz_661CvKdFVUyGvli9ZFub7v5rLUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
#تکمیلی؛ درخصوص عزیز گانیف ستاره تیم ملی ازبکستان؛ پیشنهاد مالی باشگاه تراکتور بالاتر از پیشنهاد باشگاه استقلال است اما مدیر برنامه یاسر آسانی در حال تلاشه که گانیف 29 ساله استقلال رو انتخاب کنه و با آبی‌ها قراردادی سه ساله امضا کنه سپس بعنوان بازیکن‌قرضی‌راهی…</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/persiana_Soccer/28788" target="_blank">📅 12:32 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28787">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-sODR8ETopMqa89Aqz5SCDWAko1_ezVjrbln30TFayQuM3A1-KiUFy2P1WN30bkXfwdLR2ueYModry33sY0xNqgJ9QBnbBDYFjHVw9cDgDPJAEtiRWypB47HtVAfPGzR88DzJB6hoWaqkXHOSKCs-rcFY3fiF0Lkx-2wzctXP2QFuIvuCjz8wxtl0epNcUImEESGYcOAULckacKNi_NyHWC89ZjnYc-Bwux-TAn0UWriZu-XQ9G-2tKXKUsIAkqoY6GdKZezrX6GKk_sr2XpE3_KQD5z_6stqzTIR51sHThJWsAc77CFIve1UJWUXwAmyl64cAL3Occ-zeNu-8o1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇿
🔵
#تکمیلی؛ طبق پیگیری‌های رسانه پرشیانا؛ درصورتیکه‌هلدینگ‌خلیج‌فارس‌تاپایان این هفته 400 هزاردلارپیش‌پرداختی به عزیز گانیف ستاره تیم ملی ازبکستان پرداخت کنه این بازیکن قید حضور در تیم تراکتور تبریز رو خواهد زد و آبی پوش خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/persiana_Soccer/28787" target="_blank">📅 11:51 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28786">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cqYycztowjz-UV5T3EUQmg08CkDKAtNwuFP78fyxQdK_4qtAzwuGQeZXCUhiGQRoOawmhKD4h1J0CYS-PaLERNZZCYunEJnXkjGeSvwDZSjmoTxgI3C9Nk13bfY4h00zQSGWpPYrzqfVv6v72ReJuNoBwJP-wRwp5cEInuR6PDOMUu96Eynic759zfTe9_eyYnm130YH5nRM9R6uDdoHUslnsLeIsojHoAZnjFeHEGapFwwZ4z_9oieojFFLxcdjxWKnw76SIrMBL_cv0YimyTPbHrE2aY8NnSZPqIyM9FbratVzN4QNeHXC5MRnbkMco_cuNCNUlf5sLX5TXP-7kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ترکیب جدید بارسا درفصل‌جدید بعد از پیوستن گابریل ژسوس ستاره سابق آرسنالی‌ها به این تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/persiana_Soccer/28786" target="_blank">📅 11:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28785">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VRXVna7QKwHekkX3uumDSr-b8vmo7U90nWAdgD51AlnHbdwn1tP_wMxBUQ2OlfO0IlNEDSc7IQUAwzUfB1kO0uYVKy4Pq8at6rT0q36oUVqGCVLnlZAQPQvQlAhmJFGkZDClatWulEiosK-HZtEH78Kp0XkauuTin7DWgvoZlR9nVdAZX81FFKXMyB1pmyxGiMrllaQ4fgoS5XARr0yuq7cFCCYgYqNSTkmvnV2VDOTDRFIV6iViSou1CSDKdS9QJFJ3twDBMYIUnnNNnBzPgsqXUksrK1BsGED841RtUwKIR8Rj0BvvXYgAqs4I6zoXq99GAS5EGxXxVJA6kqLynw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
#فکت؛ 3107 روز بدون شکست در جریان بازی در دربی؛ پرسپولیس آخرین بار اسفند ۱۳۹۶ در دربی شکست‌خورد و از این‌بازی.تاحالا ۱۹ شهرآورد متوالی بدون باخت درجریان‌بازی‌را پشت سر گذاشته است.
‼️
سال1396:قیمت‌دلار 4500 بود، طلاگرمی 140 هزار بود، کرونایی‌وجودنداشت، پراید…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/persiana_Soccer/28785" target="_blank">📅 11:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28784">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pD7eMuLz62hgUbQi1iEbvA5V9B6aRzuW43WKBj_A52D8MhAxCytQw6YBRot1X0GRNZiiLzws3ncCyrz_av-zZHWYJ3xP-G7xaqpzyeuwwYo16aTNlfaJtJntyzVLKBx0Xc726Pgvnt-VFPbRwABuPRMINFOHKisLHqT_xofG3XEctzm4fiIvJTeyULqdHzXIZqit74-_L1Ms_LAEOABxtb4x25oxXkL9eorv-sCWrf8kS4IbccZAny24bK42KJaNWqC0kcSwKzCbgNlVWYrPDeBp3H2Acz3bzcmrQmmmzE1r65L7FnGnGMTdbjxPqBvpWla9gCbVyohk3qHd-ZDKxw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/persiana_Soccer/28784" target="_blank">📅 11:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28783">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UZNOi11T1lvhnrZwFV5sqeg8Rwkjsncjb_1TMb5aaJwOBb92A5g29eJ1Kx3O-T_hn6vUuJgHomL9luedIA33pFLMeyZGmrPYaIad4XcTJ2N5TM3DRfZ_V83Nh017kDguRLFjeOk9JE13th21Ur-vzGUwdeKvB2pPGu_toeDE3YN_S_H8Q-4bldenMpcfgmoF5F6F_xbAoIyjdITegPZeXTB1q6sTLP7SER-BF_ZLexT7yTjFu6L0TU18hBv5NGR0iNSSyLF8LNeR1XCAwZpw4ZUdo9R09qLAx1iNfwZD-Xgib59UDb5SBwdJLEgW7dizDuP-2JuzFfXcSA-H-1bgqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ قرارداد ژسوس با بارسلونا قطعی و دو ساله توافق‌شده. سران‌بارسا10 میلیون یورو بابت این انتقال به باشگاه ارسنال پرداخت خواهد کرد. تا کنون بارسلونا 174 میلیون یورو پول رضایت نامه داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/persiana_Soccer/28783" target="_blank">📅 11:18 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28782">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf70d43b37.mp4?token=Lu83kZMu3JYG6VlCPxcymR69Z9nO6qcliW4Yq06DtUUGkbB9Y3VCmLEhYqIqhe2iKfrD51zJt2fU_pzu30S6X-LWzGec_Qrm9Ix0DujhU3mFL6T2u4X-uNe3y7dOYVQBfNwByutKifU6moKFCIAEL8kUGlBV1ppM9aPg6o40HYy4_hkz3AC6gU9qN7a7n_NMMd1uqCOqoO76wlqbrcIUVtr8zgW4CWlYfY2TAZifkQVEBQEH3fLqf9m1yTlPfD4KVDB03M9F0TOfZCllmfNdeJ0m9uOfuXj-L-hdfDtT0raunXhGEsYHjNunE29iOGUPX2xBP1Y3WjcfFf6H74gw6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf70d43b37.mp4?token=Lu83kZMu3JYG6VlCPxcymR69Z9nO6qcliW4Yq06DtUUGkbB9Y3VCmLEhYqIqhe2iKfrD51zJt2fU_pzu30S6X-LWzGec_Qrm9Ix0DujhU3mFL6T2u4X-uNe3y7dOYVQBfNwByutKifU6moKFCIAEL8kUGlBV1ppM9aPg6o40HYy4_hkz3AC6gU9qN7a7n_NMMd1uqCOqoO76wlqbrcIUVtr8zgW4CWlYfY2TAZifkQVEBQEH3fLqf9m1yTlPfD4KVDB03M9F0TOfZCllmfNdeJ0m9uOfuXj-L-hdfDtT0raunXhGEsYHjNunE29iOGUPX2xBP1Y3WjcfFf6H74gw6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
ویدیویی‌جالب‌از سبک بازی خارج مستطیل سبز کول پالمر ستاره انگلیسی 23 ساله چلسی انگلیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/persiana_Soccer/28782" target="_blank">📅 10:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28781">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇺🇿
🇺🇿
هایلایتی‌کامل‌از عملکرد درخشان عزیز گانیف ستاره‌ازبکستانی مدنظر دوباشگاه تراکتور و استقلال؛ همانطور که شب‌گذشته‌گفتیم درصورتیکه آبی ها این هفته‌پیش پرداختی رو به او بدهند آبی پوش میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/persiana_Soccer/28781" target="_blank">📅 10:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28779">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‼️
هایلایتی‌ازعملکرد موسی‌چنپو وینگر مالیایی سابق استقلال در تیم جدیدش پانایتولیکوس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/persiana_Soccer/28779" target="_blank">📅 10:11 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28778">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aV7KEjGe79Xy_LdSWosC0tXtHQemej962xR2mAPxBYn_DTUNaApnWq0dUmGsaJ8PP0SFchgAdr5DHrDN7DoAIwaWVy9Er2KBFkIGVMTm_O9Mb9o42CDD3gVmWMtnKcpEMoFwZ0NIEp2NZU8Tp883h5juI2KxwqfDY-id9uppia2PdpFAlKmo46FKknW9PhojuXivfyz2E6E7Ug7gQWPkO4X6JNLhctCdrLAZu8-eFh-bJjqvzj4wPY37uEHiOxiy9tYPrTRad_ZEvvxjeMylNAMkjZv9UxbzhwMXlbysHU9MqZgLC-D2QIGtMC6dNRPKEC253bsXHJt-3vsrNRCIeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مصدومیت‌جدید مهدی ترابی ستاره 32 ساله تراکتور مشکوک به پارگی رباط صلیبیه و به احتمال زیاد ترابی 8 الی 10 ماه دور از میادین خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/28778" target="_blank">📅 09:44 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28777">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0edcdd5b47.mp4?token=ZDJz8jaCN6KhiBhiuGFZ01gnL4oBR89kPD9k0-Hno1NVSXlD_zb-wkoHyIHwFHvJPL-oGY8WJ-XqjeZS2qYQGQ-MyiRtEwPNiNmLHIvj0YAO9uR2U65rD6kOA8u1RRgQkqHE3yy-oa07bpsdonygcnSkzlBPFafrgyUPp43lz55UloZeepXXgBdI90FHB8A0MRNfke8YNyVkE3M5wFD6GOZYf5NHqk9SAEWgp-_k61KlQ7tACbGsyfYi7kY3Gg834PYS23QsWxSlPlM--ADmK9FwgK69iVXxXzyI5EXmnQWw2a8bljB3wqjgBzo0GvewsLJAf2SEBAjtQ0F3kleLmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0edcdd5b47.mp4?token=ZDJz8jaCN6KhiBhiuGFZ01gnL4oBR89kPD9k0-Hno1NVSXlD_zb-wkoHyIHwFHvJPL-oGY8WJ-XqjeZS2qYQGQ-MyiRtEwPNiNmLHIvj0YAO9uR2U65rD6kOA8u1RRgQkqHE3yy-oa07bpsdonygcnSkzlBPFafrgyUPp43lz55UloZeepXXgBdI90FHB8A0MRNfke8YNyVkE3M5wFD6GOZYf5NHqk9SAEWgp-_k61KlQ7tACbGsyfYi7kY3Gg834PYS23QsWxSlPlM--ADmK9FwgK69iVXxXzyI5EXmnQWw2a8bljB3wqjgBzo0GvewsLJAf2SEBAjtQ0F3kleLmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شباهت گل کیلیان امیاپه به مالاگا در بازی روز گذشته به گل دیدنی CR7 به یووه در سال 2017
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/28777" target="_blank">📅 08:32 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28776">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3785816e6f.mp4?token=c6g1EeNRIes_emmEd2QqQ522xNN5Le9SYygtP5eeU6J181OFi-60w-dac2fdKln47XVw-nROzhxL9ey2RwSaA5ZV__aMIPzOnPWLFC03ROsquXHmph9S-SPBwjYKX7p5a0an0fUeBFMPwPOnUtnjhyeWyKum1NWM8GKtaZQWsWDYXCKC3SjGBnnJ0v76R20Hb5If_Ri1xVWiHXiumA1lHggEFg7mzocTdXnltRz1e6cQnCFvZtiD2CJhQItoXJBUT5wlTS7HjCU90IuutMwyns8-y3x2yVE6mnHmW25MYCisDmlFFb1rIQNuKMeARZN0q8GzpZmZpJaqOf5tw-N0RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3785816e6f.mp4?token=c6g1EeNRIes_emmEd2QqQ522xNN5Le9SYygtP5eeU6J181OFi-60w-dac2fdKln47XVw-nROzhxL9ey2RwSaA5ZV__aMIPzOnPWLFC03ROsquXHmph9S-SPBwjYKX7p5a0an0fUeBFMPwPOnUtnjhyeWyKum1NWM8GKtaZQWsWDYXCKC3SjGBnnJ0v76R20Hb5If_Ri1xVWiHXiumA1lHggEFg7mzocTdXnltRz1e6cQnCFvZtiD2CJhQItoXJBUT5wlTS7HjCU90IuutMwyns8-y3x2yVE6mnHmW25MYCisDmlFFb1rIQNuKMeARZN0q8GzpZmZpJaqOf5tw-N0RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی‌بسیارزیباوارزشمند ازهیجان و استرس مادر برای پسرش حین کشتی گرفتن او در جشنواره کشتی امید سازان المپیک 2032. عالی بود واقعا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/28776" target="_blank">📅 01:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28774">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dc559k8gMYUsRPVJg1hh2Hlsz0uylS6WSg3XhgKQlrg_lMVouGvkrSqjDky_UOoComtVbrnYu6r2R_1oYl8zXM27Y7LyOd4J6bXOnHOjNVBorzxdM4GcGSagG4U1KmKf7OmcfO3BaaF0EmDf4zTLYF_fFb5Mpsr8Kc9W8gR7T6rPAaHuFMKf2DhyiFax7f-LLsDGsdGo_LovVtJ1EpZQOQnTNsV5q-L43f31PUiPBneahoybJ6FZ7Zzq46molPqsYZ59ENBhqcTgAvaZmghNFVNzCeECLPhoar8KovUU8HVU7h38DwjaIb_yGtJs1gyK4U1xgLX-3Ry1sZ6KhVnu9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
#تکمیلی؛ درخصوص عزیز گانیف ستاره تیم ملی ازبکستان؛ پیشنهاد مالی باشگاه تراکتور بالاتر از پیشنهاد باشگاه استقلال است اما مدیر برنامه یاسر آسانی در حال تلاشه که گانیف 29 ساله استقلال رو انتخاب کنه و با آبی‌ها قراردادی سه ساله امضا کنه سپس بعنوان بازیکن‌قرضی‌راهی…</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/28774" target="_blank">📅 00:40 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28773">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MA-r0dwY1xv4THZRrgzVzmtWHfPpJSXTSjlH5v2wrgLRi_jip4HsDFu1-rSUOW5e0TweBv8UITXsVI0IloA7Dv1Kz1MkGj0WZUwRywAg6uvLsTHtVPhFgu6iTE_GOxERILZEqOem3YgeD1TBc3jyvyKbPCMfanIsdDnHzUvmn0xWyP9gYUEzxzjatsh2IgBSNFPrkTHYq1da3DUdUtA2vNcS7_Hy6ABvIPi5XcNkimy8l_uRl1K_zGFfgjyYGNzlqRGmg4AkMAG3Q3c9wZGRP9KscrtpEKkIO_lybLUFZOW4IlRPgcnsno1StyXgP3wKYXJihcBiBpYhzWwCkbAvtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌‌امروز
؛دوئل‌شاگردان آرتتا و امری در ویلاپارک و جدال کاتالان‌ها مقابل رایو وایکانو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/28773" target="_blank">📅 00:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28772">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NNgMu_rvyCwf-6sbUxtEJh--h6OSToF2tb5DHAsuKG-jBRYl4U9ve6S3_65_rXjWBCIGNaw--cv_H4eowA2xgkFfVAOcXdVXTaRRh1K6PrC1vTv8CM8lVPDeH7zp4Cn8-yD0uYSI9XAQRs1TMyXXCRiowa2_pvIvMLEPWcPQjCqZ0bw4bXzHb1BAuB7tjtVkBhJJE8OoxGHxCJWzs1EbhcQO7GxZftmZ6uSZAldoCi6CiVq--JHlVjhQmaMTbtZwN0IhbuNaOKTDP1zEqVH-LZ3FfCPMhYv_ZT8kpafHfmyru238iYWU1nBPHZG9yiPSxlOE_B0fxe2BxO67PE_sNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌‌دیروز؛
از آتش‌بازی لئو مسی در MLS تا برد دلچسب یونایتدی‌ها مقابل ایپسویچ با هتریک برونو و ورژن آماده کهکشانی‌ها با ژوزه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/28772" target="_blank">📅 00:37 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28771">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X3fcjE_WCco4htmU1BJCrTUhCpxJxbBiAJTC5bx4Qehbmo-IzxGdP_70vEZFWWsnd7IvMrRG4O32BdIPst9vLgyDSzOZXB-iNCpPxObGSCPdjJJDiW53XmyDKnkgHSVPH2tnAtI4XKZcM_DaihDvisuD6g1DqowGrShNaJsE9bN9CTL_XP3l6nSrPkgMpJkbafTDD4a1UfG1qrnsUIBSkcQctadzafXrtzbh6-t-lVUmJGQsYLIPcRM1YGqOFFobw_4QW11n3Pq3cizAc9xjitwlfoxgEx78a5J_vn0aQxTZzka8RlISQN_gPrTHGtTDyLkEf3d_3e_xd3xPVk9lIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
#تکمیلی؛بعداز اینکه‌خبر از مذاکرات تراکتور با عزیز گانیف ستاره تیم ملی ازبکستان دادیم. حمید مریخ ایجنت‌یاسرآسانی و جلال‌الدین‌ماشاریپوف در تلاشند که این بازیکن رو از تراکتور هایجک کنند.
‼️
باتوجه به‌باز بودن پنجره نقل و انتقالاتی تراکتور فعلا شانس‌تی‌تی‌ها…</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/28771" target="_blank">📅 00:27 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28769">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TT8BzmYXX1Zw_D-1OI8iqGtpULm9CQJrny4YiPwqCV_FcplqGucp94ogIM3T_pp7VZNPy5wJP0XIPxys9CQBP2oMLSB2M6RW0OHEpEnKBUwqzTo7w-p1p5p6OefpqjzwbhNC1LYxFQkc5-0miNsk9frs00HWmbgeWgUal9oK7h93h00e1vVcgRFMWOb28fj-jef_4im0Vuq9b0EHCfBY8INV9IwhiZIlUHmwgqHTAIuDOf-6ZlZvbCkgsrXpCUekeMZMvgJU3Mw60qvqym6ewcrC2o3kZ8MYP-yqsiD9tcp4PQ5uxc9dJcc1NXse7dMcIouKxV1nYiNa9cuXDUqfUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
🔵
سوپرگل‌استثنایی و برگ‌ریزون هاکان چالهان اوغلو در بازی امشب اینترمیلان در هفته اول سری‌‌آ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/28769" target="_blank">📅 00:18 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28768">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m0iCcYbX2C9Y5W11vrVIrFjKGDAG9fGgph4N3SYl5JqxhB_HxVB3QbzBaqo8U6NcICTWtCo-poznLDdhdMIMWjii8y0-SHud6Mveyt3pNmmCBjR5Ts33mp_FKXAwKHe5QoE7dJCHmzVWF7cRzoNj1_TArlqJIZlfLASjcQXs7WXieHqOTF-BSfy1RCgje17wy2Mbp-M7biGh27UDGsukh1M_0arNiukPMvB_nWoxP65FuC04IJycqLEZK9oG0_hPYqgLkwXXR8yOe8_oqQpAEKSASyh-82zfnSTj8I17c2aboa-1zjSWAlwXZbWH1x_XHIPu_lgDw-ce_u6IAR6VoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مصدومیت‌جدید مهدی ترابی ستاره 32 ساله تراکتور مشکوک به پارگی رباط صلیبیه و به احتمال زیاد ترابی 8 الی 10 ماه دور از میادین خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/28768" target="_blank">📅 00:11 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28767">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RcO3EWTVkuDe8nn4Vc3dBudm1cIqQXRubH45fJ2Fp1qwqCnRiZEGGsMx17KkIJt39o49LHYZn5X5_WnIDX0nexRSiGNMmEobkN_ZkDIiDcqP_eXsSvAZKe6e5wDybvuHBStPvpJrl-Cqsa1BCqtAX1iOiM1qLGj9fIeHCij41zL39p-OVRN3HFqu49KxGi1oENeLG3TPzxt1ekOaTyQo3UYC3C7d9T02Aj628RyeffVohw_69cJDh7cEVXnBO47vPSHJ_zP1ucaA6Bmi46CrBQbRU_o2ZTmuPurrhsjUGoZJmBq5iwSTnM-E7gqNhJnM6zR4QRolkjSmqA8RujWX9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
هلدینگ‌خلیج‌فارس و بانک شهر پاداش ویژه و میلیارد برای بازیکنان دو تیم درصورت پیروزی در شهراورد حساس و حیاتی پیش‌رو تعیین کرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/28767" target="_blank">📅 23:47 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28766">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W8zmQ-gxwyqdOrjAqlY6ybZJUmNyL59ZDhoZVT_hNHbdf9ihZEUmJTg8R7LLArOu_UH4V0ypE1dPdcvz_MbZViiRJihVeB3Ok2sMoD0VGpKU2W5l1oBegqJqomgut2oHMNyjvHvdaDzLqNiEO-mCgHzBsj6igqu0I22sACl0KhW4rdl1ucVCj6pGysojqwbanS-PpCJclaGWoaIu4Nwcq6l-PM6iWVoMBYKhETx4qaI68PuUdeRpEPMvP3Yc7m0-LP1SKRDkyI4LOxeoRyzz36dbTblnBUziU44DHhqCJg-uO01UCH6kpuJW8dZwkwaks02_b3vSrH1Zs2jsHekSSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
گل‌ های دیدار دیدنی و فوق العاده امشب دو تیم منچستریونایتد
🆚
ایپسویچ درهفته دوم لیگ‌جزیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/28766" target="_blank">📅 23:35 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28765">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BuwsZj6QaKrAcnxsKS9IwBl7rpaY57PHvZr5luuNG4WsNt3tJQZis5hH4wMs9goCzGNqsfs1j9BRD--Bjbyqo4GUped0EgTnh5Y5MWpLUxvM8Ex8r6WMq4vYrv76nQpEa3lz5xLMB3o_Sqm9T2cuQc8sHSOdcbUB6wOYthsBAffGC8GcUaRokbf7w5g1Enoo-A5agm66zdsbBqtkT69aHzxbSmLWFfZhg7eeIXTfBWeJ65NQ1WYKIOQXjKSVe-blNGcSbl8wLbX0_1fq8LPXEMazI7JDpHd0EoHDJnwTizUvXPbT2BuNf4eStAEfQ_BchHoXNuxpj5tUBdNsenr_wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ امیر عابدزاده دروازه‌بان33ساله سابق تیم‌ملی به نزدیکان‌ خود در تراکتور گفته درصورتیکه جواد نکونام سرمربی پرشورها از او بخواهد حاضره درصورت‌جدایی‌علیرضا بیرانوند راهی تراکتور شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/28765" target="_blank">📅 23:18 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28764">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wt3M73TCZRK4j2XTG7Jv-lU5Gy3r68YPPaXOTy98q0mZd6cxI8lWVjQrptW65G6lWJwTfKwORSbdnjmyhzSR01iWCvZIvqLHrtBC7nbiO0fYg-mEcjaIg11KRW0gKnF4WWakNXYdS7Jv2tVSbkiMao2NTnht85F99ZmpyB2DW6e76nhKONb5_J9D3toq4Pntk__kQ592j5Q_52CeQH17DvX1AHq6Jq7gUZlhd6AUl0TLD9pB7IGBYwNdpcc_EM1RbRYTgBTnvNOwanNTeDNbFhF_u2_YPZv70EtfX7Cdm7UMAzWXGDj3Ig1_u1fAorONEolGj6bhBN74ZxF6kWotsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛ به احتمال فراوان موعود بنیادی فر هم بعنوان داور اتاق VAR شهراورد انتخاب میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/28764" target="_blank">📅 23:15 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28763">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/881c007350.mp4?token=ZfMt_1TBDyWecigY2621JeLU6G-5AJVdMTFdwmtIOC8Z1P03ipLU9-bwgprgCHkQgMZMHX1eZ53Uo6A7m0KhvGq1ddXSCcLaAmK3DnCxHsndJ8M-FRvDptVLSoZ8eMNislwJYOcL8uUG53WQ6-7eJj8umNft6emdNR_-xJrqvYdfX7PWIlzDPV5pSXPcZ-OUGHw8oX4Hr-iQm6Knk90jYYCXywYO7GMTEVIxIEOwNhnBlitvO0doyKEyNno2LdcPU-TyuZiXCJiS-uWNqRMQO5UXyhv5lpzvwdgheL4oXpJ4pilqhlgwrYGGo91rIAMgmUSDBXpkUmkH7LY0HRBLnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/881c007350.mp4?token=ZfMt_1TBDyWecigY2621JeLU6G-5AJVdMTFdwmtIOC8Z1P03ipLU9-bwgprgCHkQgMZMHX1eZ53Uo6A7m0KhvGq1ddXSCcLaAmK3DnCxHsndJ8M-FRvDptVLSoZ8eMNislwJYOcL8uUG53WQ6-7eJj8umNft6emdNR_-xJrqvYdfX7PWIlzDPV5pSXPcZ-OUGHw8oX4Hr-iQm6Knk90jYYCXywYO7GMTEVIxIEOwNhnBlitvO0doyKEyNno2LdcPU-TyuZiXCJiS-uWNqRMQO5UXyhv5lpzvwdgheL4oXpJ4pilqhlgwrYGGo91rIAMgmUSDBXpkUmkH7LY0HRBLnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
گلزنی‌دوباره اللهیار صیادمنش برای لخ پوزنان این بار در بازی امشب این تیم مقابل تیم کلاکسویک
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/28763" target="_blank">📅 22:51 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28762">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DKEFc-cRQ3wXklcI-LVMVwB2wk5ujgLyMjJpIgOf5V2wXwlH-NXHHxLnxcCfYDysbeHqlpYxLuLgHdCyl1dDoaILj4I5CdSncDWvrhDg6om9mBGQ4b3E9Cg8P_q5JWAxBke2BUuVtEZ8o3e4uEflLnK0z2ZFBEJMOY5rvCn6YDBWRLNar893pnWXcmNwk4hfUj2B87FB4UTBiD_MlKLWcjiSoC6a8twxajNpAl2JYWHvbU5jguRmZRIkiOf0O8J7R4rde0V4CYjsCqjnUSel47v-Ns_H2sTbPcIbdEW14PYEBhLIsn9IvOoa6WofsrTF9gBNgOR6_dIebxIRmo7jdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
درفاصله سه روز تا شهرآورد؛ کوپال ناظمی اصلی‌ ترین‌ گزینه قضاوت تقابل حساس و مهم یازده شهریور ماه استقلال
🆚
پرسپولیس است و اگراتفاق خاصی‌رخ‌ندهد ناظمی این دیدار روسوت خواهد زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/28762" target="_blank">📅 22:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28761">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LN1dN2uEwkVuDveWnhoOz8yX_W1rgTaxSaKKc2vJv1YpyPMtzg6PESkdxxXJKfw8XRvylDeKgRwiGRV8hkkehS67ZgGV2Gtyn_8VArWL0x9v4SzOI0qN2f9mYX-72SLOOeq9N1rvqOo4vXQqII_D0uHxeNSOEOfqQ2mcfM5JGYkpRjLCjrhjgF_AsZcbbPaUaP52eAxB0XXsXzN9GXc5yJMIWZFYv8sP3e9xI-I0jJNua17fSEo8CqVuTiy5ohCdjy87xSGlMK87rb8p0zwfzZPHSu_zyr8askL8b9zfplAsJu2uW03rWiM7cLXUW3vWMkHNN11AgOGsC15wC4R63w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باموافقت‌سرمربی پرسپولیس؛ پوریا شهرآبادی، دانیال ایری و پوریا لطیفی‌فر، سه بازیکن جوان تیم پرسپولیس، به اردوی تیم ملی امید اضافه شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/28761" target="_blank">📅 22:11 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28760">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53b5db2489.mp4?token=hk4dgdvhTHRvVgYMmgzxoYngsDQhB-KHq32rpDuCSugPcptDesUrArVsqDtzZ5pkbn8aSfQkFf7hAesU7kQ9hwLpYrH3ybU3ChcywIZIPhJkaxYO6KAPdJTySPM7Z68ya9lHBP5cKZagifrGPSTSKZrF5AqjeqfuY1Gj-3637FdtlW6ZWeoJCJDz7_L618PVAmj4TUrQ5fSEAuSFj0besu50IR8jW-maZSVu2cKA6tkTtvmbeQ2bbWsn8HIZxq1OJqu9qvPY5eYD0f9VWvxYu5TVvaMAFtbNDyHxPWrEGvyz3debaaqCvj7lGm0FH2PIcuWXV734C7pJv3iW7A-Gfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53b5db2489.mp4?token=hk4dgdvhTHRvVgYMmgzxoYngsDQhB-KHq32rpDuCSugPcptDesUrArVsqDtzZ5pkbn8aSfQkFf7hAesU7kQ9hwLpYrH3ybU3ChcywIZIPhJkaxYO6KAPdJTySPM7Z68ya9lHBP5cKZagifrGPSTSKZrF5AqjeqfuY1Gj-3637FdtlW6ZWeoJCJDz7_L618PVAmj4TUrQ5fSEAuSFj0besu50IR8jW-maZSVu2cKA6tkTtvmbeQ2bbWsn8HIZxq1OJqu9qvPY5eYD0f9VWvxYu5TVvaMAFtbNDyHxPWrEGvyz3debaaqCvj7lGm0FH2PIcuWXV734C7pJv3iW7A-Gfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔵
هواداران چلسی یه ویدیو دو دیقه از عملکرد سانچز در فصل اخیر لیگ‌جزیره ساختن فقط آهنگش رو از ثانیه ۳۰ به بعد گوش بدیم. این چه سمی بود:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/28760" target="_blank">📅 22:01 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28759">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZJbRrvzuUlXsETghSdfw3pFgA-pwVXS6FPPltsx6QOmRAuH07D0SwltD-wMhMoLoVNc0HNbQMqXTXrjjndvPiU-yzke4hpFtn9KKk8lWwlGkGJR3lksD6cjJXjYsWVKMsIoG7QIG0oVJGlaPzr5XZRngMeSvUqNO-sgT8ANwUrVh0IUoNwrmOUTLOb-z7TUXd4beqtFD2a12AFm6uXuLbQ34yT05jHbcwVozxDwz9ufMxum11AHfz6uJM6IPykhHmn22sVrMhpEMqs6_fBn7fOxBgSHmAwgCYG_hPjo-Kv438-LJQwxPuaiW92-HlmWSuD_M2SJUgeOpPHk0BRsAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📹
گل‌های دیدار امشب دو تیم رئال مادرید - مالاگا درهفته‌سوم‌لالیگا؛درخشش فوق العاده جود بلینگهام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/28759" target="_blank">📅 21:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28758">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s8ljpQmG0PmcjJg1EWUUFdTEyhBsz-tJ7Irwy1veeNWcwyOgQb_wgqc3pNRmhgYwH6uyLHnu8kGU7pFvjN9X-oMhWHgTJtkt0MPyjUgT1FaP4_4Z_JEqEc-VQS0JQ0r4nr0znnRG4uAiLhfjcPB7aI6wKbSAzRDXnubOZGCzugydzHZeCViVJgYFvK1iQ9bpjc6SPRkHya2kS0QCvsj5nxcQYoFs-Bnaa2CL_rEuxLWe4B3wxMAhNbNOh1ZI6MnGPO-a6ZnRp3xIN4QSGHBH4hqFcmJaREwQVM-hTWXB5ASDn0GjIAKAPeikyAIulOyB97DyibaSJCKbXB9IMnY_zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باموافقت‌سرمربی پرسپولیس؛ پوریا شهرآبادی، دانیال ایری و پوریا لطیفی‌فر، سه بازیکن جوان تیم پرسپولیس، به اردوی تیم ملی امید اضافه شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/28758" target="_blank">📅 21:13 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28757">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c3f6e0903.mp4?token=edVgMp_8Yc4niLfSasGHl9utvgs7fu-kOnSWwq5nVOgzwZNAbH03Ok7WR6XgGJy-8Modt2ksaqCFm_lFZID1nQ-VUqVhUKr3kHzE9m_BD6FQHFqSM5igHIdOigQw6minKBzVIKazeoK6dpsWW0RvzxQNL7x4I8S_dp4tN7uR-7kt4PrHgXsdvISsP2bLbjLulCBRCmYdhMX3DJ2iJlneN_M49CE5hUNiVJBC6xFHmoH7dmr2u2XnyVO9hf9uO3QE6PsXiKcNEOZiHQxysi-PnHYfI4Fc5eG6AwTHJVBzYvyQ6OV8JZzo6tbVvfkF1dL8LYHfzKKaKk9qGZh9SXj1nYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c3f6e0903.mp4?token=edVgMp_8Yc4niLfSasGHl9utvgs7fu-kOnSWwq5nVOgzwZNAbH03Ok7WR6XgGJy-8Modt2ksaqCFm_lFZID1nQ-VUqVhUKr3kHzE9m_BD6FQHFqSM5igHIdOigQw6minKBzVIKazeoK6dpsWW0RvzxQNL7x4I8S_dp4tN7uR-7kt4PrHgXsdvISsP2bLbjLulCBRCmYdhMX3DJ2iJlneN_M49CE5hUNiVJBC6xFHmoH7dmr2u2XnyVO9hf9uO3QE6PsXiKcNEOZiHQxysi-PnHYfI4Fc5eG6AwTHJVBzYvyQ6OV8JZzo6tbVvfkF1dL8LYHfzKKaKk9qGZh9SXj1nYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
درهفته‌دوم‌لیگ‌جزیره؛ من یونایتد در اولترافورد با درخشش خیره کننده برونو فرناندز ستاره پرتغالی شیاطین سرخ پنج بر دو از سد ایپسویچ گذشت. فرناندز سه گل و یک پاس گل به ثبت رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/28757" target="_blank">📅 21:02 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28756">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cKHipfXmbp8sZ-1dtpZUnYYFuH9oX8gpoX2R3DSyQH8ao0Gknkidi4PsOVoqdPr-Zho0EUoI4y8JyZA6_WK19pH5AniolvnMg2mpb_Bkn2uM2Nj5858nvRdSMt3gf5YKF25bQey_x6PWE8Vu6uiKzNxDmdEAIXq7Eu2mzA0ffX7sHz9rTroDHgRWoCnoEzjZnvaKhRpWpZToYfaT003Y-uoNcSVL_cRtEiMHYxMGYZx8pUtGW-zPyMo8mq39kLbr_QCI6EXjUZwAA_T_RzUHbDirf8BLmw8Gac-BEpS0cWAKcv9XK3WNbkFJ7ovML0AvMQ1igMfDedffMFAvjWcTIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
درهفته‌دوم‌لیگ‌جزیره؛
من یونایتد در اولترافورد با درخشش خیره کننده برونو فرناندز ستاره پرتغالی شیاطین سرخ پنج بر دو از سد ایپسویچ گذشت. فرناندز سه گل و یک پاس گل به ثبت رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/28756" target="_blank">📅 20:59 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28755">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1cd133737.mp4?token=XUzLDy4fQje7XrwN7jCbnBnLq2WoihiIM-GA_9Vn4-MdZDZyLkdxYPB259D30KrdSxSp-Zrb2pVWNh51b4li5UKj0PiZz_CVxjF_WtpDV4HU3GaVJTvzDuWYm0Vv_LodVFSMXVDwO1W4LU9_rwmkvUICIh_6h6pAXXn-srxkEQHscMejCAqZ4razByce_D7AZ8fvpYJ0HhpV7O-LKhw4ln-S1H30ypikvd8WLO3shcB7iPoHgEPXXBQ6Jxbx_10XdaBzDEbY4vYpXsHsVaysk6zbmEke2SJLygepPWKq2n-4fgqyLX1c5VoVO9oHo8vlk4HvWYnCuzo9cyKCWQygOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1cd133737.mp4?token=XUzLDy4fQje7XrwN7jCbnBnLq2WoihiIM-GA_9Vn4-MdZDZyLkdxYPB259D30KrdSxSp-Zrb2pVWNh51b4li5UKj0PiZz_CVxjF_WtpDV4HU3GaVJTvzDuWYm0Vv_LodVFSMXVDwO1W4LU9_rwmkvUICIh_6h6pAXXn-srxkEQHscMejCAqZ4razByce_D7AZ8fvpYJ0HhpV7O-LKhw4ln-S1H30ypikvd8WLO3shcB7iPoHgEPXXBQ6Jxbx_10XdaBzDEbY4vYpXsHsVaysk6zbmEke2SJLygepPWKq2n-4fgqyLX1c5VoVO9oHo8vlk4HvWYnCuzo9cyKCWQygOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته سوم لالیگا؛ سومین پیروزی ارزشمند و پر گل شاگردان مورینیو درفصل‌جدید با درخشش جود بلینگهام و امباپه.
🇪🇸
رئال مادرید
4️⃣
-
0️⃣
مالاگا
🇪🇸
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/28755" target="_blank">📅 20:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28754">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bm1b06vymIBDN_uPzNEu_z1AAzJqzS2ifRfu8XCzi1RfAQNQWLB_qpjiMIMeeCpXZIaO86Igne5UjGM8zmY8rwl6sht0PTLABJam2KGCMaNFDaxa9qgUOCzAAE05GRE2UgFeSy5RMsQqdr3sGRGLtEgBBrujxsn857U0lGB1kIs9oDZk09yycmVIGqT1mh-9etXzj8YO-dOwmYCudopLKOx24N3U5Ykeu7hjaEDf0HIC2m0DqRlpS5BIki-jPstgqbSc6Wl9rquisy01jMMtso4MzZm5AeeIbHlIWFVOgCBh1vbZywpWfNFFXeSzHdNzefbN_JWb1xFBEKmhI4Evpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ دوست دختر جود بلینگهام ستاره رئالی‌ها تو ورزشگاه برنابئوعه و قراره بعد بازی دست جود روبگیره اون روآماده مسابقه بعدی کنه. جالبه از وقتی بلینگهام باایشون وارد رابطه شده جود عملکرد درخشانی درجام‌جهانی و باشگاه رئال مادرید داشته. امشب هم مقابل…</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/28754" target="_blank">📅 20:31 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28753">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M1KW66FJC7GvgJKA9id_dmfAlMsefdiV3_aR18sFeNAqwpYit1wuY0AdzrJNJZE5CsEROqjog_HUlR15u-wBhbmvwc1oVudHCm-Z7Bw0hfMG9smVv3BYAR7b5dKwEFxvi0KnGXv8_m8x0Yrtu6-bIp31O_MwbfVjB_nex-RFi6Vz4aVhtxs1aBxAcwBClt7shRaTaW2uxwguAKA2rRFF3uTNQmrTqGzlNyHwY1Ke0KGwhMjq1QYCrNBiEtmbcy6DFTTC3XCmnxsbtstq4ZWvhvinl83OoRZnvB5Ca8gO3R8F9JF7kREKJoNOGluluSORWTYAm0E4Ubg3IMLFmQDGfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
دوست دختر بلینگهام ستاره انگلیسی رئال مادرید و یکی از دلایل اوج گرفتن این ستاره در بازی‌های اخیر در مسابقات ملی و باشگاهی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/28753" target="_blank">📅 20:27 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28752">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U6tlxeHm4tn_xbButMZAEb-LPQbqYL1jfCQKuAxUq8T5RZh2rZxvEf_9vm1kNAaHNkQ-7hDZYbYTTA6kfCLNGwrFaLCFpKlyWPMVHq2u9DKWU8eStg9C9WL6L5sAoFVO_YdswFQsW0oViG92evCqgEZVKCuS_D4CIk8BJcCEDXleyuOShYRp52LgLIklmFgzxQ-5uEzSlUKhzZ1wAwGzuYscimSrLGIlBemElVka9iFVIlCELpe0GsAlcN7NU6_9M10DBcvZBOfkgK0FMVtKVS1Y2PYaMCCVf4_yalLWI6ZkluHYp9V6AffDf1rTMnfwogmZvECbEEstpqawrWkcCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ اولی واتکینز ستاره آستون ویلا با عقد قراردادی سه ساله به الهلال پیوست. عربستانی ها برای این انتقال 60 میلیون یورو هزینه کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/28752" target="_blank">📅 20:03 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28751">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r8u1pLifQBI64VYVNeRm4pqVvsybv5XxFJEwErghky8va60oHwcryHkUqluBQK7TL0JOdIpclNReyxyDeZVPYmD1Gb1qHxdnWxEk4HKED8aQpJG33_Bw9DEDd8esl3ChZy915IHTSyFZbkYQq9vEdlaVOcoq-0dRVhrKLbIWEJQ_S0UA9Gl4LlFOaa9C4x5KYbqdIRzHkYAWN2Vya3elYndpKlTcGRpzF1IYlhD-e035TX598r9mOvAZ1-RAiMhgr0ohzz2FAemCe-hqmJn-1Kso90jNPzIdR_OdBYOBNwoyY9ah5O70zKcBHLhuQcnuQpPFnM9yC95BuqpoOzaT-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
#تکمیلی؛بعداز اینکه‌خبر از مذاکرات تراکتور با عزیز گانیف ستاره تیم ملی ازبکستان دادیم. حمید مریخ ایجنت‌یاسرآسانی و جلال‌الدین‌ماشاریپوف در تلاشند که این بازیکن رو از تراکتور هایجک کنند.
‼️
باتوجه به‌باز بودن پنجره نقل و انتقالاتی تراکتور فعلا شانس‌تی‌تی‌ها…</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/28751" target="_blank">📅 19:50 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28750">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac3859b36e.mp4?token=vJFe824170nJmZHHN7VSq7m7dRggJTV6MdhL72F_2l8wlxpWgBedpItOR6k1jF76NMwh4VZMwYiNtLIxPBv8p1m2Oh0TJ_nvdDAbZuhsLYZCW1PFrqZhZbTMhCoQJb9YaXBRwozO9zIXp61WvGmTJROEKRRvN7mmnYG1rYosD3ql-XUj6x1E4JCsXxS1XEbb8G23fTwo3bEUJl3whncDqscl9TYQoiBmNY-gMeNP1QF2lV3ZWk1x9FaOCO5tktB7yHYEvQ8gmEMjhl2h_jM0_IpC0tjhjSQdqh672OEWOvqFQQQgqORZ8uKye5WqpX8qTnapk6hD_3MvLC-mcC4eVTqKTGEHUeNDnQyxoc3CFWaHzcjPypiRFYMSzPECJlyXTYlHCT3npLOU31nE8dLNeGxTIlc_kPPhmNCJX4S7JKgGRK-f57ffz7o_t8kAK4cUf43ZOgVhwPovKZw-lwXp-pdToE32UPzVYYAQNJ01-ePzZ0ruLwNlbFEFnQe_vDhmhZN_2vHlVakwZbgEhNQUuOjy3TKa3zDHyK0-FwLyxEDWs4Qyg59yoP5DWxPAT0G94QnWqksMcJrKGEZtSsGp0vfseasUOLzHYgQdrdx2MZmEBGAMj7UF4mC4KcsPVsKa7MOSs6bDUPN94SgQUy9iyiyA-0t6BH5I5ew0I2XZWFc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac3859b36e.mp4?token=vJFe824170nJmZHHN7VSq7m7dRggJTV6MdhL72F_2l8wlxpWgBedpItOR6k1jF76NMwh4VZMwYiNtLIxPBv8p1m2Oh0TJ_nvdDAbZuhsLYZCW1PFrqZhZbTMhCoQJb9YaXBRwozO9zIXp61WvGmTJROEKRRvN7mmnYG1rYosD3ql-XUj6x1E4JCsXxS1XEbb8G23fTwo3bEUJl3whncDqscl9TYQoiBmNY-gMeNP1QF2lV3ZWk1x9FaOCO5tktB7yHYEvQ8gmEMjhl2h_jM0_IpC0tjhjSQdqh672OEWOvqFQQQgqORZ8uKye5WqpX8qTnapk6hD_3MvLC-mcC4eVTqKTGEHUeNDnQyxoc3CFWaHzcjPypiRFYMSzPECJlyXTYlHCT3npLOU31nE8dLNeGxTIlc_kPPhmNCJX4S7JKgGRK-f57ffz7o_t8kAK4cUf43ZOgVhwPovKZw-lwXp-pdToE32UPzVYYAQNJ01-ePzZ0ruLwNlbFEFnQe_vDhmhZN_2vHlVakwZbgEhNQUuOjy3TKa3zDHyK0-FwLyxEDWs4Qyg59yoP5DWxPAT0G94QnWqksMcJrKGEZtSsGp0vfseasUOLzHYgQdrdx2MZmEBGAMj7UF4mC4KcsPVsKa7MOSs6bDUPN94SgQUy9iyiyA-0t6BH5I5ew0I2XZWFc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته‌دوم لیگ‌جزیره؛ برد ارزشمند شاگردان ژابی آلونسو در استمفوردبریچ در دیداری پرگل و تماشایی مقابل برایتون؛ چلسی بامالکیت‌توپ 25 درصدی این مسابقه خانگی رو از برایتون برد و رفت‌صدر جدول.
🔵
چلسی
4️⃣
-
3️⃣
برایتون
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/28750" target="_blank">📅 19:35 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28749">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jXtrz9r2AGmQU_oic1FMlaLY-2wnKL9KyqJ9m-9jnrjx_XZdkZomarm7gW12WNGcaJyFAJyPi21sZXBlejNeMvBkmqjgzUCpFeKCLkU2ucPfkIG_sERgDmGFVUOxMMQcb87h3dePYcjv7kSIhIiGr97C33JDVC2MswwAKa6cInUVXDbwtmqkEUcm17wI-s-r_q7cJyN-42YwEbWiAfWiQ6jf_FGWG6aEIIwJxHZkCDutL9ohDRh5YsI9beRCm_-Vs2vbxXpX0_MtjvWpU0SP7QlweIyqqWt_sld8wwgq6Mbx3n-TpShYRyFmhr3Hzo6N4ijWlnLlHi9kLekHQf4GXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تیم منتخب هفته سوم رقابت‌ های لیگ برتر بر اساس نمرات گرفته شده بازیکنان از سایت متریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/28749" target="_blank">📅 19:13 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28748">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SFnt9OPRF1Cec18Nr-Ewq3CbemLOZqelsblybvh1x56hkl4b0CrKVgXIjc24OT4rHbHYWdvsyUMh8O9fLH7ZUr9Iv6ffXac_-cfVrDBC5ZJGg4p3U3_SfyONyazIc210qNcs_pXm0nmxmHq0FpeEEBFfJZ2aybzzxuITqf1k49JV5Izl84DH436E2oFtrwsZtXg1k__GGTFDYstULvoN9xh4LvB_XwQ9i9NqoCpyoljkflLKVeilXrHLa7kRVM-EfKi5B3506XO8Skk1ogdEKkC4nIrPvMxEliS_yNZsTTWN9v1n8_NAZcdhsHeUnqdkwu-pvlSJZWUTnrKDJedkMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇫🇷
رسانه‌های عربستانی: کریم بنزما در لیست فروش الهلال قرار گرفته است و کادرفنی این تیم به مدیریت باشگاه خبر داده ستاره فرانسوی 38 ساله سابق رئال مادرید رو برای فصل جدید نمیخواهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/28748" target="_blank">📅 18:45 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28747">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GeAYs4uY8JGobQVcMEGcFdUE4FKmD2fnXJdReN-USDp246QIHGJP239IYHQegVh_NevvKR4YHBUp7KUaLWxvJrBhwdycjqBnXhfLkt-j0mIklOb2w3trQ3hPZ971XI0L6bdHV1V6rNK8k_w9hyngq6b4dPW8anGV938c2doEySSyGGyrqqLcej7usafv1Z7AT_9JsKgvdFr6RFJksNkdbhEac8A9Mi4aKvxt2wC57zzLNFZaUDC-jQVDgcqS4M6tAghmGMPYzi-HF85QI_47aJcmvk-ykASd_TycA4IS9fbb_UQp84CQKLuGCzqKlmXNg_r14lq4P34Q5tPSrK-nOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم لیگ‌جزیره؛
برد ارزشمند شاگردان ژابی آلونسو در استمفوردبریچ در دیداری پرگل و تماشایی مقابل برایتون؛ چلسی بامالکیت‌توپ 25 درصدی این مسابقه خانگی رو از برایتون برد و رفت‌صدر جدول.
🔵
چلسی
4️⃣
-
3️⃣
برایتون
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/28747" target="_blank">📅 18:32 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28746">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ad7e62a7d.mp4?token=EKaes7_lg3zhCdLevNN67dKGkG91OIwzDJ-foLfmEjdBjOXouskk09OEA299wLoSmGvNFG-hfuOBcia1tmQuiEDb7nigIVA0FXXgFBR-dBsyGLP21L2S9k7jSS5-VLgIzOsLyZ_oEyEDavz-fpTVYtgilCH-4itj8xrl90dW4rUqgsPGOLOleqw_tRyz8RjZEqH4HfqbcagdYG13HODxJZeukBqeYBSAGrTMbMGPFMMeP_NrhB6t2f3avbQKItFsAfiGctPjopZpnOJD9f-Ji5ciHsbpYcyv26SlpEU_zRoZOcj2QDm-_90LOJA6_sQ2NoP_M4J-d_RSMEfhz6uEAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ad7e62a7d.mp4?token=EKaes7_lg3zhCdLevNN67dKGkG91OIwzDJ-foLfmEjdBjOXouskk09OEA299wLoSmGvNFG-hfuOBcia1tmQuiEDb7nigIVA0FXXgFBR-dBsyGLP21L2S9k7jSS5-VLgIzOsLyZ_oEyEDavz-fpTVYtgilCH-4itj8xrl90dW4rUqgsPGOLOleqw_tRyz8RjZEqH4HfqbcagdYG13HODxJZeukBqeYBSAGrTMbMGPFMMeP_NrhB6t2f3avbQKItFsAfiGctPjopZpnOJD9f-Ji5ciHsbpYcyv26SlpEU_zRoZOcj2QDm-_90LOJA6_sQ2NoP_M4J-d_RSMEfhz6uEAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🔵
#تکمیلی؛بعداز اینکه‌خبر از مذاکرات تراکتور با عزیز گانیف ستاره تیم ملی ازبکستان دادیم. حمید مریخ ایجنت‌یاسرآسانی و جلال‌الدین‌ماشاریپوف در تلاشند که این بازیکن رو از تراکتور هایجک کنند.
‼️
باتوجه به‌باز بودن پنجره نقل و انتقالاتی تراکتور فعلا شانس‌تی‌تی‌ها…</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/28746" target="_blank">📅 18:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28745">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y4JMvh6EQKfwQmKuv0i0EZqbx7VuQiM2EeuS8xalbWjTPBbTYh8gVRVBdbFel27jxwMJUPSoMKG6CbJz7x3YBmqdX6Y5RsB_ClI3wCbizxRjJmTmguYf0uXwTTOHa0z8HUGAbtEmn3vboejW9PU96c351xGRb4pYGrCoeIyZaef3Xw6_C9Lj9XVxpF8zzYvDmLBWzKwh5wQG2bqaKsFa5EjrR0U7bIhinzvcNfmIskratXphUu379ftgg1pzNPWX1iYnhORzmYyA3K9gEDRZdDKmRfPthAj2P0Ps3xwQ3Z3NSJELaAYjUfHReseRkMp-waT3BXEmut16eJTZRr8uQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باگلزنی دربازی امشب با ملوان؛ علیپور با گلزنی در بازی ملوان به رکورد تاریخی علی پروین رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/28745" target="_blank">📅 18:16 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28744">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EKUjyAQGtlgj2aS5fuqwDSvq2VbF_PSprt0x4MTVcRsSzDsdqMkpl15Tk9UA0AyFXWuU4-xOY148CSEfqmosmV3d5Pf3KrVXmTi-kGRcaxhea_yUB8NDNPNcKRlq53TVIMqKM_EE1hvA2yaheoI9xlCWQZz4OrT77rOJ-QDNX_jrqSggTtO1ihQEhoIsjwbyMIwhsDhoQd-8N-4ft7RfHK9y55XQZh-RRKd6A2hvL7jZOs_V-ptIq1sKfxfEbfxT4bnus6WeU9U_6ZmaVycrMYleJj6cDcbMvyCGGMTOTQPlDsRZ6jQzaaFaWPp37EP_v8UNTTmNgOFsBuFuOnRO6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
باشگاه‌تراکتوربدرخواست نکونام با عزیز گانیف هافبک دفاعی ملی پوش سابق البطائح امارات وارد مذاکره شده تا درصورت توافق نهایی با او قرار داد امضا کرد‌. گانیف در حال حاضر بازیکن آزاد بشمار می‌اید و مشکلی برای پیوستن به تراکتور ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/28744" target="_blank">📅 18:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28743">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s91bSX1tFbzamGh5sxnCb4-jriA3W3DS55WMOJw2TZiqcssEQDHYo-kGmzA53YoGLs4Uuo-mdwE9DXHR_m-3v3JvRyz3cR5qoxfSocz1A47b_RwvZRdKPCpLuchRc9P769DpblrUZJ2Qyr2LSYeWrrYkqWTF6pY1B68R6aZ58XES_uZXSWbULkE6nh66wB-7Vs3F7ZiL-Kqy42TKQtj-1YzuUeFROhnfoS12VCtHN3z8FQXDShLWbIgCFJ4zo5q0DaP-u-f-7uMPxExlPASqxSHBfQ8Vp2Fr5soqmTKwhMhyneSIGtDwfwdISDoVID_0BN63R99IHhgUpOv_XN9HOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
مریم یکتایی دروازه‌بان‌شماره‌یک‌تیم‌ملی بانوان و گلر سابق باشگاه بشیکتاش با عقد قراردادی به مدت سه‌فصل رسما به تیم بانوان استقلال تهران پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/28743" target="_blank">📅 18:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28741">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ob4kxLlWUjOKqYVcWvr9b90CPla6Ohdp__wPiclAVZDckxYKxSkP_NqLy0xqOh8Wf2TH9Qpf8Eqm4hm2vPC9SlNrgwFZSFut1I4DmnyxSE-7GJ7e00YMU1hZDSZbtoyYUuzHLEDDOshgVX5iRuG-U0rxxfrnoPwzUEicfewvgQkGpRH1XGmd1T5AgEtagy6gKMOYMrRCKJ1PdQ1cVZf2D2jbqxefvpTownqQfBDnFcQ1LrvJIwLFon1TJnZ1vRicrk-PlkExWBY7y5hM1Kq0LtfFloMgBMIqM-U7yCRKr6xc8id9lUtU0r6F7MtAoN8YWiLj7N6BIa7Bl33dcuwzmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سوم‌لالیگا
؛شماتیک‌ترکیب رئال مادرید برای دیدار حساس‌مقابل مالاگا؛ ساعت 18:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/28741" target="_blank">📅 17:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28740">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E9Hswb_cs0CVj2XJq-v_Qjif5FI25kNKj5PnSqhwFCd2Tco2h_FFdJOk-ABW3DWX8eLwTUYgtic7aNEWUROU9uxoI4FzOpKyzffatrWiNGA3qqamYIRqcSZxz5hYNUgzGhtUIPsVSFfGrHp1kSmlBpjCzOwFWs5xPL1Ns5xX4ygbYPA22mPuqmqNJWu3HEv1lqRhdVuxTjvYAObNbdAtnn6KJpRKmp3SaJ1DkFtmc4Nxs6sMqAvyiyNL7beIfQWtAO64DGt7zlGfYc4oBSgAe6a-CQqVHK84ylGX_qEBxU0tXljsBt0hAKi7_HOKnYpLwhmOOSRWOIcCBuIzuO_DNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
#فکت؛ اگه حبیب‌فرعباسی درمسابقه این هفته مقابل پرسپولیس موفق به‌ثبت‌کلین‌شیت شود رکورد وحید طالبلو رو خواهد شکوند و به اولین دروازه بان تاریخ باشگاه استقلال تبدیل میشه که در پنج بازی ابتدایی فصل موفق به ثبت کلین شیت شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/28740" target="_blank">📅 17:35 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28739">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZGkPBIcmRpQmQ2S8VlJs7UumaMA8m5mmz_MI0YDZl1DICSTRGwBb6RemJcnwReeGbiCQS82Sq-e0hq-nZHCbA__U6w1MOBKOoq8mMbL9euW17WH_L7ISbR4X1z0tjjp4P2kV0PR0uX2tNjDGIB42p0z62aWO5j_-WXN90Em4ghMM1lGnXCutYBrCXwBMELbhKjqBDHnwtB1xLyWIEFEoKE0g9PsxLcr0bpPbWI5TRixglAQ-V83g7Vgp_b5pMhnU-aYAdqQyc9X-5CUBD738Ws24TfIdegePFQbx9cYWYrP1xTf3mcq0VXNjtBqUY07Y6-yTYCM8jdZqdriavZxcqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکردحبیب‌فرعباسی‌دروازه 28 ساله استقلال دراین فصل: 4 مسابقه، 4 کلین شیت، 0 گل خورده، 14 سیو در 4 مسابقه، نمره 7.7 از سایت متریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/28739" target="_blank">📅 17:12 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28738">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cTi0AxeliMdmRBQyZwCsuLEhYiHCTjxQ4RXGBVF98Iic_1nKkYUCchPxG05Tax2uk_a8bWx3qOUSFLMOSzSPLexCMFXOU-6qhV5T4yEPfsUQe99Wm2MbbiccCtA__qbM6Sl2rEMXRIUFBKGCMp8Omr3hBs3JlDaiTaFm72XQ4pft2mWXEeqeb_zaW8qxF8OYppwM-A-atT7CMuToOSP3C_xhAK8bpXhL8eOaN5e5iCwEU986YB4pktgB8G0GpNomfKu4ingHTuj2JP624p8k8JFq8L-qmWyFSrgxLftsgbXfbQYemZyHo1zXkxRq6JXGcZBhfAp8Vp5icyRjL8RWLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ قرارداد ژسوس با بارسلونا قطعی و دو ساله توافق‌شده. سران‌بارسا10 میلیون یورو بابت این انتقال به باشگاه ارسنال پرداخت خواهد کرد. تا کنون بارسلونا 174 میلیون یورو پول رضایت نامه داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/28738" target="_blank">📅 16:56 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28737">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FduZJIrKNGm7YO_w_RFXDWE4Pf8mpsaiQUCoSKQlNmQ5a3XskAIl_OWCIG9xWab7KzrieLcVtsvKl6fbUPxJokhQf8rSrbCTZr03yAs0NTh7vGoVD3C5fhC-0fozjVrLpw3qQo45F3nQGs9t6twFiuH57vGn3nVYbiRlqCjGfNZ-P_mgPTy2Oyr6iy1YAs8qsj5MJUU2qLPnlYRgXSBRlsZyBgZfpdhWO-jwMkS1W2yoM5dTP4uvIG0CGn5oBnGLBVluiIdyVWyh3CHo0exGMXw7aTk9QNUE9ik362wq8doI7vN0_8-5EAGJ4TpJN8LYY0D8Xi6Bsh7T6aejRZ-jYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
#فوری؛ با اعلام فابریزیو رومانو؛ گابریل ژسوس مهاجم 29 ساله آرسنال با عقد قراردادی به بارسا پیوست. آرسنال موافقت خود را اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/28737" target="_blank">📅 16:21 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28736">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WG7QOVvVFjpf5SecQsDXPuO78rYPAsg9r_cBz38UlDzGQscs5-lowAHgV3oH3VFm2LWupKv0duL212Vd6kg0F5y5zEypYk9UYGE04M1jUWiCBSSSLmMZvVuGS1gMiuiskE7frNgRf1k5J1zSdB9waAtIgKDbIE60VKJFPMSoBxo_fnpjm_adTxQNt6Un6EiZzKRDuf_86SsCODsTJ7XwqpjT7y5Ac02YyQYHnYnsGLLc4UUURrjhYTs8ANcPasG5NzJuDMfn3z36i0PsIxev8aHAaq5IQ6DiOph7Zlec_or-gfUsSvldtQ1RhqxHvbheN7aglYl5U9IqxJr8LMeM_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
فرناندو پولو خبرنگار اسپانیایی: بارسلونا مذاکرات خودرا با گابریل ژسوس مهاجم برزیلی تیم آرسنال آغاز کرده و میخواد درصورتیکه آلوارز جذب نشه گابریل ژسوس توپچی‌ها رو در واپسین ساعات نقل‌وانتقالات جذب کنه و شماره 9 آبی اناری‌ها بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/28736" target="_blank">📅 16:15 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28735">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GMlEWNOa_oLXKceQEb4LF00qHjF3_Aq3LX2qnZJiP_zY_S6eJM1M1yZ2xiicJgxNDGs-_qmWsiMRIbtvyVr_eW-iIWxUC3fCD9m4BTxHFhA6gLw8_j_PrVWkYDLY679EHVmYgbB6RHX9sJaz1cFEtOY-LQAeJUworLDqo1ul84fQI3E_3Ka8J5ixTy5g2QczSaUKKDu5LQU4QGHiewajWIyV5KC8nTie4Wuzf5HYbUDyqqAOuFpblQ8CCpa1Tki6P_b7q9jZncxsLfRTRZGsbyIa9eBRt2sHQ66dprHqAsJzxr7alo_EQZGH-q-oQCfykeZ1sm_sDjjfp8WlaWoW3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
فرناندو پولو خبرنگار اسپانیایی:
بارسلونا مذاکرات خودرا با گابریل ژسوس مهاجم برزیلی تیم آرسنال آغاز کرده و میخواد درصورتیکه آلوارز جذب نشه گابریل ژسوس توپچی‌ها رو در واپسین ساعات نقل‌وانتقالات جذب کنه و شماره 9 آبی اناری‌ها بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/28735" target="_blank">📅 15:59 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28734">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FcL5luusWLMPakiJVWKEYeHO4jTiilI7HtRvm4O5ySTwJ5RnN5vblZ7veTZ7SnFbtxZd8IDVH7pknd46Oiu6BlVkyWzsMKVSHoVfY-R8I0Q2HIf3DtYlsrc8BYuLFNJn1vK030tzRB3xpq_WwOvrplLx0adHhUaznVTWn-rTUu-eRQPObwgiwnK9055uP6aA5LuE3ZKfOaqaJUGKwZuuCrjxsfF0LBteJcsnT2jJ0EoAa-bVeFRcgWFuuTuyll6lhABPE3-lqbbXH-yV1uIfqBhMLt6xe6ux37Deo0JfXgytCN4ba8KihVZK0SPLFKC9N2LUv0-dxxqOY46wZMBOAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مهدی تارتار سرمربی پرسپولیس در استانه دیدار با تراکتور: به جز تایم فیفادی به هیییچ عنوان بازیکنی به تیم ملی بزرگسالان و تیم امید نمیدهم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/28734" target="_blank">📅 15:34 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28732">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UFXiB_JfoSIZ1VhdHpx6m8ccPBZTft0Tq2jh_pZELOfeLXAFT5k567KPktvsean9EMZixxpE3HGw1cJjVLRRj9QdDxPRo2estOCXg2xTtMoNooDMuzdt3-F3wzvPyAKecgPlBcsEVrmfeq7d3XJPypr6mAL1BoyYtYyl3RLl9Lo5dNEGbM232ZpVMjpTnP6Tddl7CPxCr4rfBSF9nLyFkBVJfAe_z2H7x0tK0VNkJNqwIT7V5h2FZSOCKzkzbOQ5kR131EX9a-k-qfIOR1fHIfBsZQbzaiMOnSJLr0UvO3CpWzDCMTJ-_uuzx_xTLLYEmj2OO-chlh5KK2_DdNzidA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HyAjQV-wSMAxg88CmJ_wVMRLP1Q-kDZU_CaTsIwFUi9KJByH4SjAAL_p5vkeBuQTEgMD12J8xdVzb0WMdtL2CSufq5A2XS5wBJYQYg3w-WowePAtFmiW7f8aWpQHxeI6eEdTcaHo5AuekPFy4lG0Dee6rknbUzAo1eCjU5TCdk3Xx2bbGIQN28Iv_d_LP9pvwfGHOTxv6RbaBuJjOHd00Q5JxvZYqSVxicnEKwhsJhDZseYkYO9dh5G1RT4nHvlCFVkEpSuuUYMx7qb0Cjy3lSTfiFxUaQA2ElBgjhajr5ijJD0mBa2l1jun0EI5845WpBg1y1BDWD69E1YA9zpsZA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚪️
بانوان هوادار حامی باشگاه ملوان انزلی که در تمام بازی ها برای حمایت به استادیوم میان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/28732" target="_blank">📅 14:50 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28731">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VLXutr9FLDq5jqqEABaE9qA8VawKrYP_AHbJftGZFZuPP0-JbiqXYq266SFDuQZsv39cyFgnN0FEhbXL5H2yXHGQNKxbK8nMPTlIhOsD8GhzZ9Uul-Ht1kzhF49vZuBp8Au1MvcY3v0zhCwoiqK1040R6kiCUv5FXK24lJJoMvjhCfuNFDzBnV-f4IrX2vKiW9KXh0mA6QSDOihz_PLlQSLsCgv073xELPSroi6cyuRTHhO9t84ydpp1Ctk8K55B_TomDOiIiDMCVmgFGL3JG-aMwJnS34CTKWH1om8XSKrIP0QeyczUowmMEwszDi3EiSxcza_rsEjZErT8uE4ViA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قیمت‌انواع‌کنسول PS5 درایران؛
PS5 PRO که بهمن ماه 40 میلیون بود شده 251 میلیون تومان!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/28731" target="_blank">📅 14:29 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28730">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pKgg7YPJh0HOiKuS3X5joGzgDnPtbdmitUIpOSIEHnZcMLL2KeVlbtlY7Nsc5GZixG6ycI88TYOw_zC5BHPes4Z4CIQRZZfu5RbMUrA-kdmCSDpjs_QQwkXKnDrN-txTa7szsoXKLFWHcm8c_9QQJ7NOKUprSqNEMXIIS_p3p-GRoxuKNunuRG2CKJvWCQ9_JWk-RGlyHo0m6pzfiJ3tILnuN-QZRDjrkGvc1nIf5uxMB_Fpc-fBfSCjNfhMEc_glHBZ2ilIFSQaV46lJh1qZqOkqbyygwxkgLhMRzu8WIgUS2ymawn0KrfnetJ3Jp23tFFaZJHKm6hPwqlf_51dBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
مریم یکتایی دروازه‌بان‌شماره‌یک‌تیم‌ملی بانوان و گلر سابق باشگاه بشیکتاش با عقد قراردادی به مدت سه‌فصل رسما به تیم بانوان استقلال تهران پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/28730" target="_blank">📅 14:11 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28729">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HgbbL7Ky8eNSn9WqZ9m-zTeSuSLMlEpbWcV_lps2tqSTVopKCuDkYBbMdNqTGNOMh-zMmt7dJyVVCpQMWWJtKp11Nr1rg5zLDeGTppnIvpebl0bXJQKD70wpdrMpDgj4_vYw3e1etIByDKo9PaEid_QXmQq_0VgiSTIoFvldeJeoYz4-BQij8cw5dfBE5PyhcIiBPcMSsmmgnXq-p0q8AZdaQx00RvV_r1YZlb7kNROyM8srJE3UA6t1RFDmlSHT4zS1OyWwg8kGlpQCT-fKLdq7cwPyBN57N3uu9CtLAjsmFJTiw76Uq4XLMyyECx38DXgSjwdGpils8SL9sjlbUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
از همسر عثمان‌دمبله درخصوص پوشش که هرجا میره ماسک میزنه‌پرسیدن برگشته گفته این یه عقیده مذهبیه و دوست‌‌ندارم‌‌چهره زیبایم رو جز عثمان کس دیگه‌ای ببینه. حتی کنار فامیلامون هم ماسک میزنم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/28729" target="_blank">📅 13:52 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28728">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/520eadae82.mp4?token=mmLBso4Gq3_L9g__XyIVBZdxXF82z8V1wW9UbcBCJUGFWoHsTtuih_uLEuN7frirsldPS5mnWnxT9oxmjSxT8G84EfVn9vmtixsBFUG0ty4m4szT9Usadx9gi7gFBBjTZl6w4c5rrTWRzfcQBViJVrP1dwa-OA0kI3C6aqbyNAj3dXGYMe7h290V_PLf0OhrHMDnsM4Xc6VLyLlNB13awPlBRlRPsNdvB9DDBgpT5MqSkqH8bJt8tQMEG3JGQP85LgjhW9_cZS8Qp1hL4WcW51t4YeLDLIRIAGt-P_fXgF1RhWg8UFtM6iy0ZgGlj2CZBPhKWnneYT3kre0GyjxE7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/520eadae82.mp4?token=mmLBso4Gq3_L9g__XyIVBZdxXF82z8V1wW9UbcBCJUGFWoHsTtuih_uLEuN7frirsldPS5mnWnxT9oxmjSxT8G84EfVn9vmtixsBFUG0ty4m4szT9Usadx9gi7gFBBjTZl6w4c5rrTWRzfcQBViJVrP1dwa-OA0kI3C6aqbyNAj3dXGYMe7h290V_PLf0OhrHMDnsM4Xc6VLyLlNB13awPlBRlRPsNdvB9DDBgpT5MqSkqH8bJt8tQMEG3JGQP85LgjhW9_cZS8Qp1hL4WcW51t4YeLDLIRIAGt-P_fXgF1RhWg8UFtM6iy0ZgGlj2CZBPhKWnneYT3kre0GyjxE7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مسعودپزشکیان‌درحضورجبلی‌رئیس صداوسیما:
دیگر تلویزیون نگاه نمیکنم وقتی من این نگاه را پیدا می‌کنم. ببین مردم چه نگاهی پیدا می‌کنند. هروقت تلویزیون رو میبینم اعصابم خورد می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/28728" target="_blank">📅 13:40 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28726">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lWKxLrbeO5EhzxnBmpFnwKhS484hKeB7vYt1owwg9l4r35vlou1PMzbfKkhDN61MId7fqqncA_gnD2U1SJf-EHp0R28awYH9-M7ztyuUadoL9e2ZZJnJuVUli7ZbvjfQiAOsFca7RLlWFe63p7LnU1n_ZRAy9hDwcOxOoPzh5uvFlCjIXd7-r6Z8CKnH8Xsg1P-K3Jkd6LnVqeRwooKBas4Y6zoiUnscMHvaVRTG9Df79DxEyXyMchd5EzERwleZ22AgtU41eZNYIyUS-8Ok5bNlOs43vN7-Qm7bod5TiTzrS-qjAh5dDZI3ptvj5ZAAcTsDxCpbTBki_-6iWv3ZWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
جوسکوهای ورزشگاه فولاد آرنا دربخش بانوان؛ هواداران بانوی فولاد بعد از سال‌ها بالاخره از فصل گذشته مجوز حضور در استادیوم‌ها رو گرفتند‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/28726" target="_blank">📅 13:21 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28725">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">📊
تمام گل‌های هفته چهارم رقابت‌های لیگ برتر جام خلیج فارس؛ سیزده‌گل‌زده در 9 مسابقه هفته چهارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/28725" target="_blank">📅 12:45 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28724">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oIiNAhn5U0be7HvkmGyDDCVgQOmfRYfVHDdc_FMWF_22Bu7ahDz8whumTpT4MFBk0gTuLukhaX3v6CKRdgblmr-bpJM35CX8m_dMEGaxU2iOpAZE6_tfTtIzJGPgYfXtZpImj24ZqKoLVYlS-jyX-MCtznuk7FhECbwQySPk0CHp2m4Mv8D-sFXqkmizPwSvtGCi2g0cgaUGdDBaSgqpo_o5ZBFsWiwnGZP-1ybmCkF7Ucn-T6Q82w_gT7E8BzrUglfBTGt7AEo8yNHSEU7k3JReYpRnrjecy-1GiEjBmMGswNJYGMAERKAYs0DxXfdEFFpDqUr1LuevS9xTBy5cRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
درفاصله سه روز تا شهرآورد؛
کوپال ناظمی اصلی‌ ترین‌ گزینه قضاوت تقابل حساس و مهم یازده شهریور ماه استقلال
🆚
پرسپولیس است و اگراتفاق خاصی‌رخ‌ندهد ناظمی این دیدار روسوت خواهد زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/28724" target="_blank">📅 12:21 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28723">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cc627927f.mp4?token=DxmJELycmJNKR10km1q3P_2jREz6wiQSA25JQgMGcvhjtzRRx3fGVSyH2_rHvKFcb-otArigSz590r3X3AXt4MQoeljmCgbOQyzs7aUCr31kut7B_mNMIMW1VmTzBDH6Qtz4LL64MMMpnNCjPW9zSUWh1HRRrYM8FEB8mQCl7tLK8T-kXE4xUN0Eq09G5K9JDN9rv0XVgqko8-vXc_GPadp985wySGtCkyiShEANCTUmg-4IW6iOvr3F_Sc-UaM-kTSRCoABMJX3i2cqcHRe0BZJWBkXy23eWl0aKGIZlZL46Ai0pUFmdu6dE8hQoxBnsBGmbFvAZGba5rRnzlS_FYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cc627927f.mp4?token=DxmJELycmJNKR10km1q3P_2jREz6wiQSA25JQgMGcvhjtzRRx3fGVSyH2_rHvKFcb-otArigSz590r3X3AXt4MQoeljmCgbOQyzs7aUCr31kut7B_mNMIMW1VmTzBDH6Qtz4LL64MMMpnNCjPW9zSUWh1HRRrYM8FEB8mQCl7tLK8T-kXE4xUN0Eq09G5K9JDN9rv0XVgqko8-vXc_GPadp985wySGtCkyiShEANCTUmg-4IW6iOvr3F_Sc-UaM-kTSRCoABMJX3i2cqcHRe0BZJWBkXy23eWl0aKGIZlZL46Ai0pUFmdu6dE8hQoxBnsBGmbFvAZGba5rRnzlS_FYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سکانس‌جالب‌ازسریال قدیمی فصل دوم ساختن ایران و رفاقت باحال امین حیایی و محسن کیایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/28723" target="_blank">📅 12:03 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28722">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gk9SU85ZoUJ5VNuH3iHbt7tI_yurJUBsgwzegqP4skiJKKlnUIYXvLm2lOCxKS5ixN4YUBheeELGS9S2Nt_C6RTqQjeHiIKB91I7pLNCruG5ZZdgosLFAtW1HJZsCn4lxuVG8HwcnXsewIt4pTUWWk-SEsxiG5I0tdYv8_RVzxzVo7w1pwdkS4JxWlJ8UiyDu7mJTvUuJTKugTorc1DVmsKMYBO-ene0VP36YuK7vu49EeGzVr1PbXDcZPxRhvox87IY0zPaUnBTNXdzEZlhePr6U8AeQcNEIXf3L9aywuBn8zm_KD-ceq6UZlWbu1BiaqRkGmH7CE5E0-gPmWoM0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
ویدیویی زیبا از پوکر تماشایی لیونل مسی فوق ستاره آرژانتینی اینترمیامی در سن 39 سالگی.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/28722" target="_blank">📅 11:51 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28721">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gPr8Al8vW8a9Mf3q4sZdX1n9KN5A-ggfxK7f6hzmuUqZ5Gy5YVW0SFxsuwJskCal2rSNJ5qML6Efq5TppW4Ls4XDju9Liqfqduh7y9mAJq6GyLuQXGjM0OHMi1x_KLGDWpDl6r3GvYqS39Mqbex3qpNi878kwpbrMZqqOTRQGzmFjRN81-JPEbqkj4C9f_oW_k7eaycQzqxmnUGTGu8gkj3ZO1nIRu25iyI5mKTGkTn8QNLVdTNZClZKtbcghDeQfGzQPQD8xvUlDwm9aYfabxrI0mOoCsh8uNrR1sgCwomjG1utbt3LOXBxxfb3Ci_sTuTOMOaetzuVo4vTntJxsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بعداز جذب دنی ولبک و جردن هندرسون؛ چلسی به درخواست ژابی آلونسو امیلیانو مارتینز دروازه بان 33 ساله آرژانتینی تیم آستون ویلا رو جذب کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/28721" target="_blank">📅 11:38 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28720">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N3NVcre_iT8Bbnkntj-ip_eduzX9TQcgpmoR-tLbvrO9Pty7RW9Yt2QZ7rtkiRXY7nbMfx3WSvKCdwQXKvudI-7KDFB6Sbc9iUDuFDG3GnsbEhjeRVFrCxPlay7rSdsJXHhtBBs9PZXLSm2wOGlLzKw2T6hhKniFUj7C3iiqOUyg5SQ61apixkD_wgeFZTjmOpx4v9U8A6Bmz1jeI2pnOAWt9ABRy3im05kZtoTB8LtakV7H0gdW-zb2Zx0LmTdJPSFb-5b7fvqK6XWI6OgYa7DNaCA_lBv1veWMdlRRIc2vqVa1Owbac1VoXFyMfrsqIosKpx1tkKiQuj_ChYRbsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
منیر الحدادی ستاره سابق استقلال: هیچوقت دوست نداشتم از تیم استقلال جدا بشم اما شرایط طوریکه مامیخواستیم پیش نرفت.‌ از تمام مدیریت باشگاه و هواداران که این مدت به من و خانواده ام لطف داشتن تشکرم میکنم. امیدوارم در اینده نزدیک باردیگر به جمع شما برگردم. تا…</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/28720" target="_blank">📅 11:31 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28719">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rYsgj_grYf9vksvWSHSJxqqiGiNClWNjkD4GBA6W90WJlEJ0clOL1nNEn7IOFV5-6m2wcI6NuJmsj7AFwVQFcoK8V4XzrTLpDbS0va9u0QA9tgrfCHXsBS3ZJV-RRNmFw3gKfy0NtvQaEbWgtQrZeQi8zfgQ1x2EVpCQhCmm6EW8DYYs1MOwlXp0SAMQqAmPdMLGNgth-K9FTuthKBlqD-uFLekd76LoWtd85TZU8_EnVRIXezxQ_CGYqEjsCtTwZA0ZZqB23tkKi-BbungHhLkrRmdyItGC5k71pKpuZWIQVb1kwMSHt20Pqn6mIO1ef2zpQuji8vsLOUVKHeWZ6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درشب‌پیروزی 7 بر 1 اینترمیامی مقابل مونترال؛ لیونل مسی‌فوق‌ستاره‌آرژانتینی این تیم موفق به ثبت پوکر شد و نمره درخشان 10 از سوفااسکور گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/28719" target="_blank">📅 11:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28718">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4635dd1d8.mp4?token=Rs78qLjB6-aDJMjTkvOtZwnlS6SlXpr9HAWAbkbzMWBK6N286Gt7OwnQFVs4Gr2HssjvYvTHFCxi6oTcukZcPB2P2FDg21PeYb5GXwOhzlgHrcA1d9bHzJZazfYZT9eIQYZfsWnCXnT9H6fzNfxsNqGy5bbVKQeU2NV_UyHkyWnF5yUxUeoQyc2x-L_qi-D6Rz3VpU2gHBETZ_-T_QFztzoOhFEenAXH6BSdVw8sKgJPG8gYCh7UevBspizqief7Izc0gYu93CTkfcRxbDzJwb-bmV17iQmVa-wsOKrEM9JXwPJ9PB4GcOgPM-kPrSN6g3yLbuyQxqGdjLB8Ynyn9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4635dd1d8.mp4?token=Rs78qLjB6-aDJMjTkvOtZwnlS6SlXpr9HAWAbkbzMWBK6N286Gt7OwnQFVs4Gr2HssjvYvTHFCxi6oTcukZcPB2P2FDg21PeYb5GXwOhzlgHrcA1d9bHzJZazfYZT9eIQYZfsWnCXnT9H6fzNfxsNqGy5bbVKQeU2NV_UyHkyWnF5yUxUeoQyc2x-L_qi-D6Rz3VpU2gHBETZ_-T_QFztzoOhFEenAXH6BSdVw8sKgJPG8gYCh7UevBspizqief7Izc0gYu93CTkfcRxbDzJwb-bmV17iQmVa-wsOKrEM9JXwPJ9PB4GcOgPM-kPrSN6g3yLbuyQxqGdjLB8Ynyn9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟠
جوسکوهای ورزشگاه فولاد آرنا دربخش بانوان؛ هواداران بانوی فولاد بعد از سال‌ها بالاخره از فصل گذشته مجوز حضور در استادیوم‌ها رو گرفتند‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/28718" target="_blank">📅 11:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28716">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p_qXKLM87jOk1JVxt_hLdtnmt7y9lFg5Tngef-VUNVlbiBNK6hN8T87L-IyLNMOt6AKmpzKn_jnTkqqGWYdSpcXHDNm1ti_jlC3Met-rp4AMJ8pdPWi5R_kHx9iZL1FIaQeGRGxd_xpIU8j0Dft5laylKNjJ6_3WhjhUBoPG1g7IG1WHd5db3JgoLshf6D84BYvqots8rK9s7qr4jw5U-WqUmbFBK1eOxEGOQn_fylkhs72BXyOD-G_TRj1oFCgXKrzuKTNsV6TFIzcG17AdbfP4w51rkCyi31EnKtR-jnURbuAzm0CSAQLk0Zi1uu7xaUBfM6mLo-vKO4C53tbfiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شایدبعضیا یادشون‌نیاد ولی کریستال پالاس یه بازیکن داشت به نام کریستین بنتکه تو اولین بازیش مقابل لیورپول دو گل زد . بعد دوباره در جام حذفی مقابلشون بازی کرد و دوگل بهشون زد، دوماه بعد تو لیگ مقابل‌لیورپول بازی‌کرد و بازم دوگل زد‌. لیورپول ازش خوششون اومد و خریدنش یک فصل بازی کرد عملکرد خوبی نداشت فروختنش به پالاس به محض اینکه برابر لیورپول بازی‌کردمجدد دو گل بهشون زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/28716" target="_blank">📅 10:59 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28715">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d907216599.mp4?token=N8PVLh0YO-1tqqyUXlry-IXUVrXiFX9pbXGWNxejtPJZpYJtEWjO0KaJfAO1V9vQFQcOiiaFMAXFb_d-ncmON196K24klXYYYUllgs11W5KlyANUQdvQoNpmeyRd8OIkq5rvHVuhEOztDF8NMJQovb-iYhVCEuhPd7yKVVj6KuIYGjExOC5b2M-qQZzJqtkdUzQYxqKJmlN-XRVUMTOIt9pNHQOez3LiqRRXb6WIhYQER9bQyb0U0iHeFV3R47KCMbLt3fFEIgsnUdPVxXeoOGXe6vM56Q4kXPTRbX4dXU-6A3EYyZmCHtgc_IawikjZn4e448CQav8sN11NiEa3Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d907216599.mp4?token=N8PVLh0YO-1tqqyUXlry-IXUVrXiFX9pbXGWNxejtPJZpYJtEWjO0KaJfAO1V9vQFQcOiiaFMAXFb_d-ncmON196K24klXYYYUllgs11W5KlyANUQdvQoNpmeyRd8OIkq5rvHVuhEOztDF8NMJQovb-iYhVCEuhPd7yKVVj6KuIYGjExOC5b2M-qQZzJqtkdUzQYxqKJmlN-XRVUMTOIt9pNHQOez3LiqRRXb6WIhYQER9bQyb0U0iHeFV3R47KCMbLt3fFEIgsnUdPVxXeoOGXe6vM56Q4kXPTRbX4dXU-6A3EYyZmCHtgc_IawikjZn4e448CQav8sN11NiEa3Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
عملکرد گلزنی لیونل مسی، رابرت لواندوفسکی و کریستیانو رونالدو در پنج لیگ معتبر اروپایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/28715" target="_blank">📅 10:48 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28714">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qbpRh5I5iLPmAQ8ZMJAwlJqIzwlogDaWt7717z6Z-OhLOHg8uUwZZb02QF-Ybv-VaWL-TTP1q89rCkgZ7Q422kFz_1iojv3rhKgv0ySMuaJKIRRO1ZkXwJDO3tDXy-HfPtPsYMID40evft7E71MMEKDExlvbNhcXtBfcnXQJcCHkxzTZ_kQZQQV8A2EfSVJ1Cm4pkbS7bkU0iFVmV7Y5elAj5m7my8qjD8zLKcQeodW89pAxFR1Ulf0oGFJhLHELvikaO3qBixOfl7_htJhEGNvqN8tgZ1AeVVA-KoAT-8mRh-Eewsbrz_eUw4e-tgXbrkKa-7bhXARpVjm3lOEhxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درشب‌پیروزی 7 بر 1 اینترمیامی مقابل مونترال؛ لیونل مسی‌فوق‌ستاره‌آرژانتینی این تیم موفق به ثبت پوکر شد و نمره درخشان 10 از سوفااسکور گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/28714" target="_blank">📅 08:40 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28713">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‼️
درشب‌پیروزی 7 بر 1 اینترمیامی مقابل مونترال؛ لیونل مسی‌فوق‌ستاره‌آرژانتینی این تیم موفق به ثبت پوکر شد و نمره درخشان 10 از سوفااسکور گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/28713" target="_blank">📅 08:26 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28712">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OQiydKcBqSpg6mxuQRhKqqVO3X7C1HM1qiaztsMl09EZQEbQzLQCxWrFAdEh4GS_zSbza1Co2pphzwxe5hfV0WwL3QogdFjNW9ji4yYIckEk5K2vGuHf8G0lFqXZljaSp_lHmM71qHXhrTHsQVt8dFgUlikNCgFhJyGH2gGo1DVwC6c2lAESBNFS_ezClKYGvzzeHCTB4xCpJ_11S4B_Io_8pspgY4BYIHWCkyRGKV6Zv05q4BdGb4CBq1PUQE2cPljytPEuabNpMXe9iqxW8dEMeWQ_fXkBDm5ieidL53tWiVYv2fUj0MIj6uCPFOsjVgjRgKehRzLU63vZtKYFGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛اسپورت: دو تیم اینترمیلان و بارسا در حال مذاکره هستند تا برسر معاوضه فدریکو دیمارکو و الخاندرو بالده در روزهای پایانی نقل و انتقالات به توافق نهایی برسند و این جابجایی انجام شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/28712" target="_blank">📅 01:46 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28710">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/csCIg54iMDPB8toHTXJe9T4lPFV0eY6tgZga1mL46n427GugH-GTpgBXCyMS8vodLGNO5hmP7szMwVbiq5-PrIc4aGI7jBrP2tQQYazTLM7jEddBiw9vZUdfUO3MknvuU_cOKO1wg3PJdqkLEZ3rYc7jg4JtVFQZi6UcpGfTjMjtmuvL93FQ8JH2I546gLSb_vG7AKgl8IOgblv9dQpjqCrI8UcoXuAhiEEcn4-PIZCg4_tn6p-sPlpb9QhmcFrntVV8fQgZeu4PJnjSKSKQ2TQStbHvKq1ZIUuOU8LO4V6-HSpnnwwMHAsuQPJmv74SvafDD-fpOi6_RkOZ3rLKng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌‌امروز
؛ نبرد رئالی ها با تیم سابق ایسکو و مصاف شاگردان کریک برابر ایپسویچ‌تاون
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/persiana_Soccer/28710" target="_blank">📅 01:34 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28709">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mRHlpOYzknjQaRvt_AdHsMvGIMmUhp0rOYll3KKccWq1Thups0_N9ifM4S6zi_p-4Kfn9QSZ5-IvOdJKmZ_0_I6Du6CSg1D6WMn3KmAlfYdYeWaY6AmquSOL1o_spvgzu-HoW1fcaWD6a40sNTXxT8m7Bp9BqD_qnBciQnif18cC_Ny20U3A--dE-tSSmFN-rtE0CPxrtGqMBvdI7H_C60y14rdwKs7L5BBaZalD1Z2-OOto2M0Rgr5MVfL7CnWsOYJ3RITvRPCXyKNklV7So3Z7r29VxABzorpgMiJDN592E_NyxxRdB8a6rYolPjLnGsHoMGYF1r9xa25Gp6ZObg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌‌دیروز؛
برتری قاطع پرسپولیس و استارت فاجعه‌بار شاگردان دی‌زربی در پریمیرلیگ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/28709" target="_blank">📅 01:34 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28707">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QNDb6SyyxfyWkOeVm7kdEaO6EMEFqsjZsCuC4qhqFku7o_lEtC2epR8mpeI5jQBDN78damA5DqBhDadNl9KfWmuMUmnaKjAPwAQtLJn2UYzrSTW2AG1keRreVx7pO-m3KF5-DLLp_Qs4pJAmTieRZ_anW9z35zcUCNLmZd373X5NzWnIc9JAbd8jbajzqquzihjbVZqapxc7Z-3A5PVHOhFVba6W-ucYhfE2wh6nbGuJ9WNBC3zGF4vMchitUi82w3h5HEgoZB3fb0P8DLBvy5x8Cs-3DaGA6hIxgUrBxQVeVzASSsSTW_ZWrNj7CwQwLFs90xQydtO2omZm1gxktA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍁
پاییزِ زیبا، پاییز خوش آب و هوا، پاییزِ دلپذیر و جذاب‌از رگ‌گردن‌به‌شما نزدیک تره. این گرمای لعنتی بره که برنگرده. با قطعی برق دهنمون سرویس شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/28707" target="_blank">📅 00:58 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28705">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oYY1FjU5YMN9ycuGj63wETViedcAL_eD_3g1sEHE_T4ppSzTzKYc0lAdVYm8UgAVPw_T515Yl06ItLfHCIDJZKK0vniHvxlmOX6tpHKfEgknmkdU-18KGSulzNBlG2CabEuRNzV9zecrMGWtMS_ii7gJrBWHO0Q6Dkh6bH_7ifjxcyfSFUTFdaPEF2DrWM7LVi68KsVnTf_F9Lao3ZZD0tUilU_6_NHe29Z86riCt78tk3PGt2eN-lcGbbxCYG0aYJtrmoHcxbQ-vYlUPjc5GiGlNdfeP8biMgatqcuW_zOYWeLv5pM1p4qgLVW87EmbAc9pFNvrbCHlHpOsTodEEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمارنهایی‌دیداردوتیم‌پرسپولیس
🆚
ملوان از نگاه متریکا؛ ثبت‌امیدگل خارق العاه 4.02 و انتخاب علی علیپور بعنوان بهترین بازیکن این مسابقه یک طرفه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/28705" target="_blank">📅 00:48 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28704">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fmsO2VgP-o8Xn0BjxHJxI9-36AwEu089Ee8igWqeWc3vmMPADqCtjzPHor7xsgjTGEC5bBEamij2A2F_xs1rs9dzXLjeCf-wt7PsGETD4zXJ1Zs8lnnVLb5EW22DjwrlGAhXN0Hp58wP4JvkuhZQpm77yZT_Dw8a--PKPW6Sp9iGd9zniWCOU-XcvoFFZqdqqkhb7JzaisSZIXnKotaho_8qSqQEEKRkr3XU_lId1SmbXyVvuAQccK-SDlpngZx3BqE38q4v5b0wDG-7kdRS3Syhpdo58txFiHCrlDYH70kPN-abkMqdVhoQxLzcYAIeWYch2f9ZLRqdf-noQAIxbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روزنامه«Novi list»کرواسی‌گزارش‌داد که محمد محبی برای‌انجام‌کارهای‌نهایی‌لازم در راستای پیوستن به‌تیم فوتبال رییکا وارد شهر رییکای کرواسی شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/persiana_Soccer/28704" target="_blank">📅 00:24 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28703">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uwa1p8q92TpP9dTpKWczpXa3bkBAASBTkPxYCOuDTYVxhJ2xcb-0ShdNb2khv1l0aWNs-WCuMrSY393MwqYtOfuOaxWt3obzNyOoGjaU7H0SSU52tj-29x0e1f0giprsiqGJGR4_zmgzGdTuDrvg6k9bDLFoKyHMvN06n3-RRfYG_IRKsbrBkaKn1LUlSUL_z72NdQ4o80_NauudvSGQJ0JUniixXMYykRiEnhpIHKCw-l-IrJS1334I3S4eYyVZ6DKHafVfJ423s3Of6XUPPH6ACsB-v486oVn6keDZ6anFALnpsbd2OkdmpSuGaokWdYfrOrmSdiad16UzGUm5qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ اهداف مهدی تارتار درصورت‌ماندن‌درپرسپولیس در نقل و انتقالات نیم‌فصل‌لیگ‌برتر:ابوالفضل‌رزاق‌پور مدافع چپ فولاد، محمد قربانی هافبک دفاعی الوحده، فرهان جعفری هافبک تهاجمی ملوان. جذب یک مهاجم جوان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 82.2K · <a href="https://t.me/persiana_Soccer/28703" target="_blank">📅 00:09 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28702">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rOm12prjAThuXup12aFkRstHleVV3JlGmArack_BLimb6zpo1l1P2ZB_Ym-TNF81wrZ2zVVmckMIS9jSb8b88-51U7Bs9HSHijVChL9eUQB7IKd5RRDpQEkiQYYNIa85jMBy5FG37kTXMjKhPPlHLyT3QMvO-flJlTXUxgOQ-ugo9fUfsqtVtvXa8zORR7yVF2r637sJDeu1eUdxhBuShXWi9SbnJrY73S_LpdR7GQLTlbkXpPnx1jojfYWYUioKiHU0RhZ1D6hz-6V3opCFA9LZiK6WpMMB-p4-bGgKm3qRiJGKFDQGPDrMu5KMbyFsWzr6ndApIULyXPamwpVHuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ اهداف‌ باشگاه‌استقلال درنقل‌وانتقالات نیم فصل: مسعود محبی یا مجید حسینی، ماهان بهشتی وینگر راست‌ ملوان، مهدی گودرزی هافبک تهاجمی گلگهر سیرجان یا فرهان جعفری، محمد محبی وینگر چپ تیم ملی، محمدجواد حسین‌نژاد هافبک تهاجمی ریوآوه. جذب…</div>
<div class="tg-footer">👁️ 87.1K · <a href="https://t.me/persiana_Soccer/28702" target="_blank">📅 23:53 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28701">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J9R6THR696tA68cVkjH45nEL3ZTxxO74hiHSulGfcpt58BmfHCUphfKuGP1yMQHrQPzlUWMdczhcgSjTGhov6lCbFrYMcUcUah9QLPdXoLuJENobqVRdVXeBm8WyEv9x60ezucaBRK-24v9t3L3bKNRIhN2vatraLd8NDL6TC3Ntm3ZSNnbr4sQaSwOxsR0VLDmxhv2WvFWLDxrrJqYzrj1EELHDZMLxixtBDDY8I85WQhe5m9QbmNjJOpV6iKhrragUA-xali0oZjW-Y5IXvHsOUFpTpALKMxl8jio0HEr1c2cJKtUkFYpBqb-ILWeSuR8J7Og6WXMT0mfdJKJf6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام جرارد رومرو؛ الخاندرو بالده مدافع چپ اسپانیایی بارسلونا تصمیم نهایی خود را برای جدایی از بارسا گرفته و بزودی از این تیم جدا میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 86.5K · <a href="https://t.me/persiana_Soccer/28701" target="_blank">📅 23:41 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28700">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s6SGe6Gdds4JZs94aQP9UdVJRhXxvUXVc0uL9G8kX6-DYQyNRcvKtGbiAFLpMMSnOWVjm3eMMNgp-H5RRKFgn4zgKYyXYx93sgkTIv14wnH9X2mVSA_z-IB7STBxERN0D_DUiRhWAoGAhNm__Z1HS_hM6Sp8P6NshPK5799tJ7vwKz0UNSPwBv-v4Gj9gMvAUCsQyGLV-NDnNxivLjCyKjHQ3XirVcbFZC69YGIWNoo3MIGcv7-cq7IgCetylP_ZnMKg3UWF7z4W9gDGODgvxrZso--9qXv-2jCoEZn1HWyTGBH2867z5gtq9yRR_rAwYl2Ls-0a5H-NO-nBWaRotg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌چهارم‌لیگ‌برتر؛ شاگردان مهدی تارتار با یک پیروزی پرگل و قاطع به استقبال دربی رفتند؛ تارتار بالاخره به ستاره ازبکستانی سرخ ها بازی داد.
🔴
پرسپولیس
3️⃣
-
0️⃣
ملوان انزلی
⚪️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/persiana_Soccer/28700" target="_blank">📅 23:33 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28698">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AIKz8Y6YdKK6OMUU90VXMKyRw-hpRsvfaseuUfQyGFRt5doXEWGsFEpBPLbbMCftJbZRTlwf1Shj0HMC_lYN75a27SWsVeln7xChB4Ylklb5sNQ3cQuWJPv4utRWdWdgu4ikRZEg8JAUCF-sUPjjRi7Gt0ocByXoqbTUI1s1sgR_rBimZ4NvbbWYkKcAd8dcWPBCCouszrSvPC-CNOpO6Eu4QPjrfhH1fjTb5FVNdjNcgJaOar22PWBbXdjBlM_02VIRX1gFiJfauKhS6fj2uDFIHq90sAgBSWo6O3x0LGS5bgeTjBYnWDGXeJ5PM0aSsM5ML0cQ8G69UH_dhD2DPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇳🇱
#فوری؛دیویداورنشتاین: کودی گاکپو ستاره هلندی لیورپول تصمیم نهایی خود را برای پیوستن به منچسترسیتی‌گرفته و این‌انتقال بزودی انجام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/28698" target="_blank">📅 23:22 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28697">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90f3cfd1b0.mp4?token=X2NvZF-85cxrNH8euDaOd7JRD8XYZjf34eNu5v59ezomuSnAb5n4uQ6ClOHeh2qBwoBCvVKu8JeOEr5lMkWuuMUHAmsUHv5pxHGaIOK1sl4dnMD48DnCiZUUlirIQiO7yUJVU48RthEDeC5E5FaFRJw0yhg0uqtOXUJdiRr05XgyvQGkkTYJVMxnpBcp_qHyzyMSaFhOAncOGokuL65Ya6aFsOAADCKQsJnOO2uTESyJBKus3Sfgb8RaMPEeJy67Vb48gl9Pn796Loolx9rbPOOU9SF91RijwpbLE5-wlkNmFle1KUj7Xu02tIjDSVF4yqwo2zsX5xnYaBwIxZIQWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90f3cfd1b0.mp4?token=X2NvZF-85cxrNH8euDaOd7JRD8XYZjf34eNu5v59ezomuSnAb5n4uQ6ClOHeh2qBwoBCvVKu8JeOEr5lMkWuuMUHAmsUHv5pxHGaIOK1sl4dnMD48DnCiZUUlirIQiO7yUJVU48RthEDeC5E5FaFRJw0yhg0uqtOXUJdiRr05XgyvQGkkTYJVMxnpBcp_qHyzyMSaFhOAncOGokuL65Ya6aFsOAADCKQsJnOO2uTESyJBKus3Sfgb8RaMPEeJy67Vb48gl9Pn796Loolx9rbPOOU9SF91RijwpbLE5-wlkNmFle1KUj7Xu02tIjDSVF4yqwo2zsX5xnYaBwIxZIQWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
فرصت‌سوزی‌عجیب‌وغریب و دور از انتظار طارمی 34 ساله در اولین بازی خود برای الوصل!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/28697" target="_blank">📅 23:13 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28696">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PSLXm9g5U5lF3dSy5xxiwa6nr1Hg6RjDp1yT6y1PSfYyLkRET_lUHZsw28n5PChmNLvfd8WXa6sdLscUAKUUi4k02BDceLooHi6RW4VcpWv0eDNbRhIUJc-qHvOi6_s-Mta1Db6ZbhdVUDWxSSm9ABt6bv-j7mymDQYONPUFa9B1m6qwD58FO_HQZmEmZHdCbBQ5pSCBnCm0KbCRJk1YilP9xbeSflnFLfuqN6-a3_ZqgLfLI--hV1gIbL2kNMoQz8_bbX2BeAfGsUkI_7O7PxYYlgwXko024RZndbqPEqtTQ6qUn_Gixb-ZXqi3dRNVzx4PQTK06NuKt14ki8G4tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇳🇱
#فوری
؛دیویداورنشتاین:
کودی گاکپو ستاره هلندی لیورپول تصمیم نهایی خود را برای پیوستن به منچسترسیتی‌گرفته و این‌انتقال بزودی انجام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/28696" target="_blank">📅 22:55 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28695">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bYanpoOmA2jgIpfJOyOcwdFU-GxdLCF_xXxgWMuB4_Wx8wkM-vNPrf7IqgXBcfdmyzM3wOa1AolplahuZV9PQ9RUCnE97WQal3pZ1kNKUCEgXFri3JvpFvdG0bnmPXGKo7Ns0o0E92Y-ijOJpvKc13pODDJEwAz-9L6D7YIRV6q7iDYrmQOyI7K7vGQmp5Z41L_BN5XqJSZJCDpUiljDtW8mchSP9kcrGJkxyRBUIZ_0UHQLWfTmnTOKSUKhCzmjQRrFE6qKlH_DqMEOFqum61NWkpZg8o28WXOwurQzBte1_Mmyff4qkgkXlqDaXSlF3LeOyfl-CB0Er3cfA0826g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ مدیربرنامه‌های محبی قصدداره بعد از بردن حسین‌نژاد به‌پرتغال، محمدمحبی هم به پرتغال ببره و نیم فصل با رقم سنگینی به ایران برگردونه. فعلاسر انتقال حسین نژاد به ریو آوه 250 هزار دلار به‌جیب زده قطعا سر انتقال‌محبی‌هم 300 به جیب میزنه بعد نیم فصل‌ 1…</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/28695" target="_blank">📅 22:24 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28694">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b98c0d9b2.mp4?token=FnraJF3N7LPHiowKts-me_wCtdzX6wuvRUc6mQlu2ifaMkwqyRyG6-aOr0PXAk6Uhi8An2ju_-S4HkBCECUM3poEzU6MUMemQuG0r8GU9CpdVMY4ZtE00XZn8513mJWnNr6C-iOw_NHiF3mJ59cIxOO47kW_1shE5pKwYk-DVLLgWCsGOng3OCUR7u3fYYSSSBnCsxE7I_DNiHKTmV3T2h_3IxEyqC4QxonHqL8rudClrSsg4HJ7gK9iCBhxyaHsIuQh--GrjW7Kbsl7pgZ7j8FKgHJA7D-hw-TGH5g3hayM4PPJOSo_IlP_RJuWlycjb7jtgnYTL-vtBSHO7gehNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b98c0d9b2.mp4?token=FnraJF3N7LPHiowKts-me_wCtdzX6wuvRUc6mQlu2ifaMkwqyRyG6-aOr0PXAk6Uhi8An2ju_-S4HkBCECUM3poEzU6MUMemQuG0r8GU9CpdVMY4ZtE00XZn8513mJWnNr6C-iOw_NHiF3mJ59cIxOO47kW_1shE5pKwYk-DVLLgWCsGOng3OCUR7u3fYYSSSBnCsxE7I_DNiHKTmV3T2h_3IxEyqC4QxonHqL8rudClrSsg4HJ7gK9iCBhxyaHsIuQh--GrjW7Kbsl7pgZ7j8FKgHJA7D-hw-TGH5g3hayM4PPJOSo_IlP_RJuWlycjb7jtgnYTL-vtBSHO7gehNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سکانس‌جالب‌ازسریال قدیمی فصل دوم ساختن ایران و رفاقت باحال امین حیایی و محسن کیایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/28694" target="_blank">📅 22:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28693">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95e895367e.mp4?token=CdMJLtiKON6OCdGtugWuAJ0GE013ptckPDgQbxb8dw3oEY_7OJN1cdBK4KF8-UVU_-TGj-k-DQUs3FnEN2nWc1DnSdvQsp3EOWtlEgeZPQMqWaUz2q1l4OP6NYvTAyVRgFsrd5DeJoJfvL2bPj65sNRmh4FkKTTn4YWfZsETA3SA52S4tbQKToRkLu1K1Nv6Tg0Ty2PfKK1wTtok3HIYk55IJa2KRTB-aYzI2lmBpR-4hkO1-ZV5M3sXB7oNBMHNG7rmc2bWerN_gi0huBZoXJP6OYeTSDvv12kyW-My9HvtJVD_VGimcBVs6KbQCofUt_g0Q6Rd_sed9j1IONYXCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95e895367e.mp4?token=CdMJLtiKON6OCdGtugWuAJ0GE013ptckPDgQbxb8dw3oEY_7OJN1cdBK4KF8-UVU_-TGj-k-DQUs3FnEN2nWc1DnSdvQsp3EOWtlEgeZPQMqWaUz2q1l4OP6NYvTAyVRgFsrd5DeJoJfvL2bPj65sNRmh4FkKTTn4YWfZsETA3SA52S4tbQKToRkLu1K1Nv6Tg0Ty2PfKK1wTtok3HIYk55IJa2KRTB-aYzI2lmBpR-4hkO1-ZV5M3sXB7oNBMHNG7rmc2bWerN_gi0huBZoXJP6OYeTSDvv12kyW-My9HvtJVD_VGimcBVs6KbQCofUt_g0Q6Rd_sed9j1IONYXCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی زیبا از تاریخ سازی دختران ایران برای اولین با قرار گرفتن در بین چهار تیم برتر آسیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/28693" target="_blank">📅 22:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28691">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3d295e52c.mp4?token=nQdary7-wjHUwGKOxhLR4a4LNeK4mviJCa3a7G8oCTS9bJS1d2BreJlISrVGx79IXNe_wou51W5L6cwRGmdElmrX-NZV9Netyhk7PHI753wvfwqhlDyqkvFUGy1wq1SXHxuXZGRyuXFStgsSeHYDNd8Y9sJznK6qHd_Z8_l4yBzvBYfoQ59KV27M5fWASV3n6qW-LuuS-y8YOWj_Lznrw_ihL6Wagallf8eOZsP4HN6qBLDKDKsrnh4wXmYShAliR5NCy79Zg3wPf5llnzpYtwJHmOhgUf3VRCIENnfVQzeafyp37btA0_pqPk0o0kLL5ihNfPhCTln1nIld5LwZnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3d295e52c.mp4?token=nQdary7-wjHUwGKOxhLR4a4LNeK4mviJCa3a7G8oCTS9bJS1d2BreJlISrVGx79IXNe_wou51W5L6cwRGmdElmrX-NZV9Netyhk7PHI753wvfwqhlDyqkvFUGy1wq1SXHxuXZGRyuXFStgsSeHYDNd8Y9sJznK6qHd_Z8_l4yBzvBYfoQ59KV27M5fWASV3n6qW-LuuS-y8YOWj_Lznrw_ihL6Wagallf8eOZsP4HN6qBLDKDKsrnh4wXmYShAliR5NCy79Zg3wPf5llnzpYtwJHmOhgUf3VRCIENnfVQzeafyp37btA0_pqPk0o0kLL5ihNfPhCTln1nIld5LwZnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
👤
مازیار زارع سرمربی‌جوان‌تیم‌ملوان با تریلی از روی برنامه فوتبال برتر ممد میثاقی رد شد و گفت تا دوربین خودتون رو از سالن بیرون نبرید، مصاحبه نمی‌کنم. دوست ندارم تصویر من رو پخش کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/28691" target="_blank">📅 22:04 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28690">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oL1mKVg5VdSgMstqjz_Rw2ZZHJLC7PgmZr9PY9-D0pfCmwC4FQxQhVzet7FWasCpSv_XgAnUhmHYud4vKCH9z4A3X_fBWjdGiasZJ5vV-yPjaCndaSQMYOhPUTGExLK0BHgWACG1wonxJkkFQfsbL1Z8FTNtpFPv3h1ylLXZU_Y4QofxW8-MH2C2NpFRr-btXXmgT6YXc1kWBRSpR090pL8S11-mMwjSexCvygCYPEkL7cfm100JgumU3XkidYsT_uOqWKDaTpdcPWKkWGsmywK3D2W-7nfjoz_uByEHovqdKZAknfWF2ESp44kMgvNy9uOEuYEKLfF9-T3AFLOfjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
سید ابوالفضل جلالی، مهران احمدی و رستم آشورماتف سه‌بازیکن‌مصدوم سرخابی‌های پایتخت به دیدارحساس‌شهراوردپایتخت رسیدند. تقابل‌ بزرگ دو تیم استقلال
🆚
پرسپولیس یازده شهریورماه ساعت 19:30 در نقش جهان اصفهان برگزار میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/28690" target="_blank">📅 21:49 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28689">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LPLEYd1hKFLJmENV1Eya836yMVWyTG6WN5P9gsACLj5fFQUGvbtddijt8EvaNc9GqhMY5TjZE1k-e7wXysWMMAo9PLedjllyNi1wrPYHRYd5G9MjOWHosK27cXpn5SVel-7DMdtIlaBhIbZtilIhXF37-Rh-79LYM2F8BNH75K2lktX-zmiqO1VnjCbGgcfAmIcxvD-UnFi5MxYo81WW7Z8GDVAk7XHEXf_7RN8okVe30qDFfMyiQgAa89P1hdrMJPjmBmypilOlvTFG6PMMDnIZCzBf0qk-A9tdKrQTDqGNN12gplyxk2-vN2hjcVitUtif5SyoAhP5RSK_c3_YLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌ونتایج‌کامل‌‌بازی‌های هفته چهارم لیگ برتر؛ تراکتور با جواد نکونام همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/28689" target="_blank">📅 21:42 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28687">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wbyh7FchLOrjLQbLylprV0Zdvq43yWbdayYDAKNzNUqfc-OhIiyIlAXTwCQCgksiPWBYCtQ997s51SH8Xi2mP0xayxotKlr87Wx6gWQNGmCEf9GdWSukwFgq-a0nFYbHgjJm0KH9NwKsbdljZHgoVsrVxOsEpWM4foCtoXSR50Q5JDXNDr_86fs71hVb1CP5p6rfzdD6-gWUCcG4eHCNEhXMFqlyQq5pPgDCCvuqU_SKDCxk4getf0EDxXjfndmkQGLFdd7Enge6wnpstUSaB6j4Uc87qn4atVDAjJDtZKajfn0rv8oXhmt1p2qsRatdNd8cl077-Z-jZwIFWzZXLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LDnbyG1A-tUgEw9-0Khp68OhJEZ5ezASjDxm7erLZtvRoKmbDI8IcHMnGTf9_t2E45FAbvf1S5z8zd9174McWn-Iu_NWWoH3EfYbhUjTJruA6SU3dVkyGaxh3bCRVtlWkGWlvr93m_qoKV6rFR3Exjq0W0r6zC3mDzW-YkDEzySC8kf3WnE3vss59p-sB1_LbsIDXJF2CPTKJDYqIP1Albs_c1TAFYOvMC1zQmwB1N_vYG2FH8z0QpD-XaA13Jf6_ghgQ1A_JGHstKvV9pNFs2I0U4jQTBWIRS7wCjDiLUan-SoqOKOK0QaUrHP-2YiQ_3yBUxcpR9albQdw7cLTTw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته‌چهارم‌لیگ‌برتر؛ شاگردان مهدی تارتار با یک پیروزی پرگل و قاطع به استقبال دربی رفتند؛ تارتار بالاخره به ستاره ازبکستانی سرخ ها بازی داد.
🔴
پرسپولیس
3️⃣
-
0️⃣
ملوان انزلی
⚪️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/28687" target="_blank">📅 21:24 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28686">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y0oln1Jx8pF_wsogss5b8jwhUKnJzRwV_2knDgEeKBEeofzbH1oAbS5Q5fADY3mBvDeoUi59AMUFBo2iyzrZlQ6ZW90OZACtKYb5WnNwKFkYHzD-88t8Ut4Os8HigPthW_9trOOZp504ka7PMDtlt28wL_M1zngOJd3iglqs17RFOaK9TsuXo3BvFHQNA7skuJ7DD1oSb3LQDoVhNPrVGqErvf2RptSFIm6TmQcLBq7bat9etD2T3S_sSlgIs3kgnTUJZjvsKfp4tubT4EEViL20PeVowJ2aAESRBKAzWTZqc-jAi5AYzWJuMWBMQ3jRW1fJspm6ZfKKoizY-0aT2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌چهارم‌لیگ‌برتر؛ شاگردان مهدی تارتار با یک پیروزی پرگل و قاطع به استقبال دربی رفتند؛ تارتار بالاخره به ستاره ازبکستانی سرخ ها بازی داد.
🔴
پرسپولیس
3️⃣
-
0️⃣
ملوان انزلی
⚪️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/28686" target="_blank">📅 21:20 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28685">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dCLuCrCUhJ3CRCbE-TDY0aHumd_Coe0W7gxPE7o40I71mdxzqtyGRzYQlQcpsJgp43ISvUPqUzRhf6-FnTSwW--BAEcoWLot8DqVr5jrYIWg6I8E39-O58vZ9ja4ShAmF70BSDKb3mNVtOzVjGEH4uZAZTC2RmOhY83ftyasHq-NONuhDjX2qb70cCgZXikv8fXQ--DV0qKHlX7eiMh4myluZhFn6l6TNdOue24QiL8f-QZLD0yx0je1BFsoHlC8Now_3oCEDV9J2E5-2UixhVsB3nIizEhoSmMM6o2UOk3dPQgFGmNOMev9MWsw-aCwhlud2Dga-3xwgXYLxLghGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
آتش‌بازی‌سرخ‌ها روسوتی‌های عجیب انزالی‌چی‌ها؛ گل سوم پرسپولیس به ملوان توسط علی علیپور '56
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/28685" target="_blank">📅 21:18 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28684">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0430b06fb1.mp4?token=D8qNfyNX_zAZpBJ-86eeSbS8HqWwFupcXS9FKqIGoolvX9PM5tbwr_0dKRz5o7apzfZXo_u0w_Kb7IO7AjWyWYf4wNSGtLGUt9BTR-b_4NK9U6IeK6TnXDj9M5wbXkEhVu1UzNcAcMZ8jgo9QLeUI5pk0dvX0DEblkKVQqSYfk16XGlEhfqhyUkEYT439pOOZLq6XDI3HlSfFbNGsvbGVYhDvBBH1EKPAHfrkGa2G-Qv9_I1hKNy6uL4jLethcK7o9MESIErvuXVISGd2PrBxVX28_5uOSTRS6Msn72YGRzTXHOq0sK4jAfWD3q4XvyxnsOo_Iw9PIOZ4zSXc5lXjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0430b06fb1.mp4?token=D8qNfyNX_zAZpBJ-86eeSbS8HqWwFupcXS9FKqIGoolvX9PM5tbwr_0dKRz5o7apzfZXo_u0w_Kb7IO7AjWyWYf4wNSGtLGUt9BTR-b_4NK9U6IeK6TnXDj9M5wbXkEhVu1UzNcAcMZ8jgo9QLeUI5pk0dvX0DEblkKVQqSYfk16XGlEhfqhyUkEYT439pOOZLq6XDI3HlSfFbNGsvbGVYhDvBBH1EKPAHfrkGa2G-Qv9_I1hKNy6uL4jLethcK7o9MESIErvuXVISGd2PrBxVX28_5uOSTRS6Msn72YGRzTXHOq0sK4jAfWD3q4XvyxnsOo_Iw9PIOZ4zSXc5lXjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درد و دل‌های علیرضا منصوریان سرمربی الطلبه عراق باخبرنگان‌عراقی بعداز دیدار این هفته این تیم در لیگ‌ برتر عراق که با پیروزی تیمش همراه شد: 8 ماهه که هیچ دستمزدی از الطلبه دریافت نکرده‌ام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/28684" target="_blank">📅 21:02 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28683">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ebe211786.mp4?token=q3u9y-eV8k0DAyuqQQS6n-dDeyKDz2ekkBn5QZ_HAlFIroKIb6qYQRYxgttxexsCoAXW3d_6LqElqU0pDXxBBDL5d5srcOsi_AysrjeVN6DzF9gnGaLGG_H-HkmnX0J_oGvM4QBSiIYkWfISCclgtWuufuVs3wF7plU8TCyU37evY7_KP5KjRGxjuo_PSRBfTVN13js0in5O9o_0pI7rWA2BoUf1t4o5JwUDV3eb_Iazfrls7mL9YujnEZdWULjLV_VJD1mYUpxOTYDzDOVM0zWt5ypq1ofmalCWdwmee_ns2cr6pqDkEGjidBN05kQ3X7SM7UGYEGlwDlU2fBbgig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ebe211786.mp4?token=q3u9y-eV8k0DAyuqQQS6n-dDeyKDz2ekkBn5QZ_HAlFIroKIb6qYQRYxgttxexsCoAXW3d_6LqElqU0pDXxBBDL5d5srcOsi_AysrjeVN6DzF9gnGaLGG_H-HkmnX0J_oGvM4QBSiIYkWfISCclgtWuufuVs3wF7plU8TCyU37evY7_KP5KjRGxjuo_PSRBfTVN13js0in5O9o_0pI7rWA2BoUf1t4o5JwUDV3eb_Iazfrls7mL9YujnEZdWULjLV_VJD1mYUpxOTYDzDOVM0zWt5ypq1ofmalCWdwmee_ns2cr6pqDkEGjidBN05kQ3X7SM7UGYEGlwDlU2fBbgig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
گل اول و دوم پرسپولیس به ملوان با گل بخودی مدافع حریف و تیوی بیفوما در نیمه اول مسابقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/28683" target="_blank">📅 20:38 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28682">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b26514a40.mp4?token=vSI0t5Ur2OlpJr1UyA6FKQfN5AWUKN_whbyFj7a2fpx_D7twhqXDOJCkpnSucMbHZrCW5ZcvZOyuOvHjk63saknGN5v_h-RhPVSNc_nttFQD23V3VgZFGyG8_6kiBoV6f5xX9jMhyyAnS8LIkzVbKWceXNwj2hYiGG4sbrKotb6GDoL8DvMxmj4PoTPSQJCcqgIb__fjUBJVCBShT4AcTdjnVamARyTNqRaIqfPiZeZKpHW12cZVCb40FL_7WGiriuVArfRiQbeONFGdqoek0QmfGCpYo1wUabtP76u6_zV9DtEI9DsfXGqBQSi4r7zXVi00c6ZN1vABoB0nXWsSjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b26514a40.mp4?token=vSI0t5Ur2OlpJr1UyA6FKQfN5AWUKN_whbyFj7a2fpx_D7twhqXDOJCkpnSucMbHZrCW5ZcvZOyuOvHjk63saknGN5v_h-RhPVSNc_nttFQD23V3VgZFGyG8_6kiBoV6f5xX9jMhyyAnS8LIkzVbKWceXNwj2hYiGG4sbrKotb6GDoL8DvMxmj4PoTPSQJCcqgIb__fjUBJVCBShT4AcTdjnVamARyTNqRaIqfPiZeZKpHW12cZVCb40FL_7WGiriuVArfRiQbeONFGdqoek0QmfGCpYo1wUabtP76u6_zV9DtEI9DsfXGqBQSi4r7zXVi00c6ZN1vABoB0nXWsSjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
کریس رونالدو کاپیتان النصر پس از برد دیشب النصر، پسر سامو کاستا را هم در شادی اش شریک کرد؛ قاب زیبایی که حسابی‌مورد توجه‌قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/28682" target="_blank">📅 20:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28681">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/esMtw1tDv5ihIuqymJ-qkECjZfu7OoHr_I31VvcqJ2YCeqRZhx-lN8QLB-_ThHQOSmVy3asTZ0nWyHGTkSyc2ujrxniU6Gva8EJ6UAtPUe-mfI6otfxEhRO3h7m2SAOZGRhMchB8txb_-r8xJlH8ZIytWY4a5h_YLFy8rdr3yiBi-zuKD2Wg5bFtabwhKFQvrd9PuUsT79QysKQ6igDmJa9QUDGEeiWymX5azhOO-p8gRFnv01Yc0jwHVvIZh86D77nbR2SpE-1fn0l2bc5w9PL1i2QMn4xPfraW174vDf8QC2u2SclGblZLeDhkckUqb-dm0n99Ijbyw9pgSc9S1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
دوخبرنگارمعروف و محبوب شبکه DAZN ایتالیا برای پوشش رقابت‌های فصل جدید سری‌آ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/28681" target="_blank">📅 20:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28679">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AWnZTtWc5V0Ql7zmvY1HFOrpv8_rqwkEsG2gr1LHxRVpeQmNnB-YI1tLBF0objDgaHKvQl9ohvgvqyyWpGpcDHKqZH23-VvljnIM_7W-NZ1aZn3Qrb91QsZFDHYfinrFTnCr9ognkjmZLrlWWcN09-xO9uEUrpzNz2IFnnbBOeW-f-F9n-9vIt8s6V36RXkieJ7TnM6oxf0bmoD32YimjWCgmVfFmvZ0CwBRZY_LMxkQLGo-RXTKKwXrfMD24yARFOcRNoUsG03ge7FvaP-pV2M99okKfpICfMBA7cjxqqWSSN3Z3tuMnUKX7CH-ountr_4jKYbsO88ANbERCcq-MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
گل اول و دوم پرسپولیس به ملوان با گل بخودی مدافع حریف و تیوی بیفوما در نیمه اول مسابقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/28679" target="_blank">📅 20:11 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28678">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">✅
هفته‌چهارم‌لیگ‌برتر؛ شماتیک ترکیب پرسپولیس برای دیدار مقابل ملوان؛ ساعت 19:15 از شبکه سه.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/28678" target="_blank">📅 20:09 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28677">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mn1UAKiUBrq_JkHMODVdxVte-8Ihuf16cDbQ95tVeHkjYNbgwqqjkRAzWpwYG2Cj9A0yQoa4FFlkTLHRgFI2-K9RHXtcYxD4juoNMD4sln2H_uwasP_ucs_4jDakpuhyAmk6jWwlNL01TfsO1bTLe1MFsmM4yDg9Kjpm-zv__AJlEr_2FI7-8LFHBW6ZjZlODDEGu8YOFRDKw0mi0_fRwNSvSW3yM7vmaPIzARpOEspb5C_DlLaq22ZqbFUTUzVKOWQsxwf7qw9KpOEZjpFX60XX_ZtqEEZgn88kR6NWZQtcpAlpNL4kaHEkyMJonL-YtxjUlaJT5SKRWjfeqmPRRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌چهارم‌لیگ‌برتر
؛ شماتیک ترکیب پرسپولیس برای دیدار مقابل ملوان؛ ساعت 19:15 از شبکه سه.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/28677" target="_blank">📅 18:18 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28676">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9cce8d93c.mp4?token=ge22Sf9gh14J0ltPSfBww2FKM2SGxCxlMM_a8ANvMTX9gG-AOmJDAIsHYS4qWQGr3FbRe5Rf9JK4-ow0rgdfd5vRJI0u9o7AAiejM9-se2TQctypnk6hYiCrTMXaIoTUVRvJuy-UPAVSPMXA2Jj3FZjNJ2XWIyZf5FjAokYsHqTCPBj8CYzU95sZ133gX_-WDeJSdOPUDnGMnVA-2UtlsLWe5rb6nkaCNL1cPEWDAnMUQk_sYF5Vn8odDdyuyzgfPfQ_KH8-SClzMIV-sfg3JrN6Bi9zmbipqH2bEORmoy980vS6VmvOxI2Z53ebNOLWn5IM999buKhoiMMqFihlyGEm18X6BYmYCau_O4PVQO0XYDFIwhVnfbHpTxu_AF5-DLoxV1ZAH5K6sojBngROoihAzQNlYYpSuvZwikF487Fh0pzGcN_RvH7X3QIvD0kGnp7tOiHkgByH4BnREtuTY3osn4DFMLcxkhS0DiCabECFcfynpnUpQMbQO2k8Eoxfov4aTl4tefjxY0xnCYre057MZpOGHMA19Rtsy6i5VIf1QOINsaN5dGxe6v4zJ2f2q6XK5xQhX5PU7oQgrBoBnw8YKOjzpAv19Qw55sVj0bhS7zgqfZQPoV1n4pdToupZDkXxBiq17GoQ21fHZ39-yk8eB3BmKSpL6LtNYjKyLmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9cce8d93c.mp4?token=ge22Sf9gh14J0ltPSfBww2FKM2SGxCxlMM_a8ANvMTX9gG-AOmJDAIsHYS4qWQGr3FbRe5Rf9JK4-ow0rgdfd5vRJI0u9o7AAiejM9-se2TQctypnk6hYiCrTMXaIoTUVRvJuy-UPAVSPMXA2Jj3FZjNJ2XWIyZf5FjAokYsHqTCPBj8CYzU95sZ133gX_-WDeJSdOPUDnGMnVA-2UtlsLWe5rb6nkaCNL1cPEWDAnMUQk_sYF5Vn8odDdyuyzgfPfQ_KH8-SClzMIV-sfg3JrN6Bi9zmbipqH2bEORmoy980vS6VmvOxI2Z53ebNOLWn5IM999buKhoiMMqFihlyGEm18X6BYmYCau_O4PVQO0XYDFIwhVnfbHpTxu_AF5-DLoxV1ZAH5K6sojBngROoihAzQNlYYpSuvZwikF487Fh0pzGcN_RvH7X3QIvD0kGnp7tOiHkgByH4BnREtuTY3osn4DFMLcxkhS0DiCabECFcfynpnUpQMbQO2k8Eoxfov4aTl4tefjxY0xnCYre057MZpOGHMA19Rtsy6i5VIf1QOINsaN5dGxe6v4zJ2f2q6XK5xQhX5PU7oQgrBoBnw8YKOjzpAv19Qw55sVj0bhS7zgqfZQPoV1n4pdToupZDkXxBiq17GoQ21fHZ39-yk8eB3BmKSpL6LtNYjKyLmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بجای‌مانده‌از دیدار روز گذشته فولاد و استقلال؛ دوئل علیرضاکوشکی و رامین رضاییان درکنار زمین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/28676" target="_blank">📅 18:08 · 07 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
