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
<img src="https://cdn4.telesco.pe/file/RB7jsSRsErKHaUH4E-YOuKK3iyxmnVoDJal7tEXsd31ndInj26JdZsN5DWeodzvKBtGxD6DhtlgS8hrJvD73NdOjjOLUKrbpTM_7XNfqmF5pTDPAjb4w_K1-hI9hVkJULmpqMaG-2IpysWUr_ayMm75Z9iXmgD5aGb8EYGGxzFCXqAlTDQoMP2jaY-iWdqYPqmQ85RhXJ-CwcpKVuk9pxOaWTVHApNaZuRqRlpGuS-QO0fYJOOTyuANU7zNNY0wOi4q3yznZSP2z-0UaOd5HOf2M0d_7jd-J0C2DbO3evPWQNHBazSG0QwoI9UVO3vqaB3S3IivPRDW2lFZJCLndWQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 161K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-29 00:42:14</div>
<hr>

<div class="tg-post" id="msg-68580">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
آرژانتین ده نفره شد.
@News_Hut</div>
<div class="tg-footer">👁️ 624 · <a href="https://t.me/news_hut/68580" target="_blank">📅 00:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68579">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
آژیر خطر در بحرین به صدا در آمد.
@News_Hut</div>
<div class="tg-footer">👁️ 929 · <a href="https://t.me/news_hut/68579" target="_blank">📅 00:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68577">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a67fe75354.mov?token=NNk1hCgzCGv1QUOlWVSC3r9xX9O1ruziHqplxxhcpa1doEn1mKirA39LbooX_15DNZpu8S1DTj2OZQwOwp9AZ4UqHK0M5OtFTeQD-gYc9J8Wl8MMbqkj2v2mp-IgltmY_ZOOIdEodb_ui3acHYLgiVjndVZu7yefx-oSrNTzM2bpHtYZdMC4PzQBIx6iHYH13rQ5s0L78AMo9RTxMBaeCkP3Q4VG4L5LCzLzGaDcUtYMa3CLDLOtUU7KUHfGt5pjqqsJjqJhwdriAq1DqxJCk6ge-gd1B7dFdgxSFtfFKZ1bBBs1CEKenAKqcpb7mWAjOvBbPnA1tYaF0NboxzTWmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a67fe75354.mov?token=NNk1hCgzCGv1QUOlWVSC3r9xX9O1ruziHqplxxhcpa1doEn1mKirA39LbooX_15DNZpu8S1DTj2OZQwOwp9AZ4UqHK0M5OtFTeQD-gYc9J8Wl8MMbqkj2v2mp-IgltmY_ZOOIdEodb_ui3acHYLgiVjndVZu7yefx-oSrNTzM2bpHtYZdMC4PzQBIx6iHYH13rQ5s0L78AMo9RTxMBaeCkP3Q4VG4L5LCzLzGaDcUtYMa3CLDLOtUU7KUHfGt5pjqqsJjqJhwdriAq1DqxJCk6ge-gd1B7dFdgxSFtfFKZ1bBBs1CEKenAKqcpb7mWAjOvBbPnA1tYaF0NboxzTWmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
گویا از قم موشک‌ پرتاب کردن
@News_Hut</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/news_hut/68577" target="_blank">📅 00:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68576">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sv8L5ykZdBgCBr_bGI4ObcrQ5vmCKrcFZH2pioJ0F0J2E3hwtU2Of64EhaHFLNpLa6dWmU-mUzRK06w7CvCjYfnQ5PTHNHqp_Zy07b2VrHYTvnTrEqldTwqJm6kl3qwKWrCe-uU0voScAOgu7THI-nUI9tkyGycW8wFTA-ZZMyWqq6soJiGIHPjpucz51cASqQweZrS6IN0_5XegwveVTuVVJeHQhTNQ5R_BwAYrniHnuugKdzBxReNa1gVPbUw74FrFeKkZaK4qvVMrSNoLhjGhAaCnp5srmvTBr84vzCkVcynuikS1niTwlDm6k3J5MxPJtzEjB6TVpwj-CKb06w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمو بیژن تو فینال
🔥
@News_Hut</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/news_hut/68576" target="_blank">📅 00:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68574">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🏆
اجرای کامل شکیرا در بین‌ دو‌ نیمه
@News_Hut</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/news_hut/68574" target="_blank">📅 00:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68573">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🏆
🔞
🇱🇧
حضور میاخلیفه، پورن استار اهل کشور لبنان در آمریکا برای تماشای فینال  @HutNewsPlus</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/news_hut/68573" target="_blank">📅 00:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68572">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در ساوه  @News_Hut</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/news_hut/68572" target="_blank">📅 00:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68571">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در ساوه
@News_Hut</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/news_hut/68571" target="_blank">📅 00:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68570">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/416fb2b432.mp4?token=G3M7TgIbjC9Qays5HDHYxfpn-NJfRIjbunyhFTeDvyZw8maFmIsVFPPBkHly3scxQpYWnGFa22vhK7_IUA9O6NvuNezh58lp6864FoAJjngm67fjSJiPHk2PO6CQ84aide7l4m3bNGZTV8mAcJSMCZVqzn3-KhxiHI9RFmcYN5HU--0mErRGC2xqC5nsIJFKkXM-vu3H1aygXdJLZS6E_HjhAxsIjgFScVJf4eyFsPuKO-Lgcgntl9Zd2UR0KNxH9TeadVuj1gAe7uM7dEUjipR1KzNKvdFGpK76USNJcky3nA4Kf1SaLaF-ArvUO4GaqvxhoY7CrivM21C7FDnT2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/416fb2b432.mp4?token=G3M7TgIbjC9Qays5HDHYxfpn-NJfRIjbunyhFTeDvyZw8maFmIsVFPPBkHly3scxQpYWnGFa22vhK7_IUA9O6NvuNezh58lp6864FoAJjngm67fjSJiPHk2PO6CQ84aide7l4m3bNGZTV8mAcJSMCZVqzn3-KhxiHI9RFmcYN5HU--0mErRGC2xqC5nsIJFKkXM-vu3H1aygXdJLZS6E_HjhAxsIjgFScVJf4eyFsPuKO-Lgcgntl9Zd2UR0KNxH9TeadVuj1gAe7uM7dEUjipR1KzNKvdFGpK76USNJcky3nA4Kf1SaLaF-ArvUO4GaqvxhoY7CrivM21C7FDnT2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏆
اجرای عمو بیژن
@News_Hut</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/news_hut/68570" target="_blank">📅 23:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68569">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jOb5badZYncXb2Ww-TKJpfTw4gPgy7i9PXEs6zlBd35rKBW0h2N7Ys3BY5wjIX9ubkdZkGzbZklHv06QfsvvnP1OAz2TedF16Ju3Y6VsSZ2rUMUEk9kLs9nNzWDzi0Q6hmv74vYuq0mv6g7EEDWL0Va0bdMAbj8K2utFqDsyzxyHEe7ns021zH4mv-7eJ5O0aTpntt3p_e2TsBQK8m9-90Jhu3ynhQAcxaeBHSgHqrELuT3ULh2ygpyEMz68LHV49Q-4Wc-vGxBl9gB5nIlD4RJgQkifqVnUdQ0FJnlSDVNsji_h2sEkCUtM5a3O5WWomWTogEbDQaCJZ93I7vUSDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوه آرژانتینا دارن کامل لخت می‌شن
🔥
👀
🔥
🔗
مشاهده ویدیوی لو رفته از دختر آرژانتینی
@News_Hut</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/news_hut/68569" target="_blank">📅 23:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68567">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/esWc0ZdpjBhjOcDMTTnxVMfV6eUBRIncutmrcCwA_mLRWyMj32dN9Uy5ruLGzf26a0ZPoc2HTOD9E3j0JayK3E-wsLb_-IgL0POINWOrx6_T5it2OTK43oJVQ_8x9tt9FEiWL4BMcmhXp9dQ16GCcOQBh9rIYrq_5yVftfs_fP2EVIjHpOoEV0wsC1qkFdmc4rtXYIeChl5EgpoMr4iwXSGvPmXwh7LwW2KKkO6IqwsZ3uHlS8Usv8bR5OKiySFvxJz5vRj6vFvgRSArM3PG_UgX7yMev0M9YbjNIpdosWo7gcev5NTEILnIvga-ZNBoKi_LG8eoYzmamLVlZN3miA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:یک نظامی آمریکایی در شمال عراق در تاریخ ۱۸ ژوئیه و حین عملیات انهدام کنترل‌شدۀ مهمات عمل‌نکرده‌ی به‌جامانده از یک پهپاد تهاجمی یک‌طرفه (انتحاری) ایرانی، جان خود را از دست داد.
روز گذشته، فرماندهی مرکزی ایالات متحده (سنتکام) خبر جان‌باختن دو نظامی آمریکایی و مفقود شدن یک نظامی دیگر در اردن را، در پی حمله ایران در تاریخ ۱۷ ژوئیه، اعلام کرد.
پس از یک عملیات جستجوی دقیق، نیروهای نظامی آمریکا امروز بقایای جسدی را که هویت آن هنوز مشخص نشده است، در محل حادثه پیدا کردند.
فرآیند بررسی برای شناسایی و تأیید هویت این بقایا در جریان است.
در رویدادی جداگانه، یک نظامی آمریکایی در شمال عراق در تاریخ ۱۸ ژوئیه و حین عملیات انهدام کنترل‌شدۀ مهمات عمل‌نکرده‌ی به‌جامانده از یک پهپاد تهاجمی یک‌طرفه (انتحاری) ایرانی، جان خود را از دست داد.
نظامی دیگری نیز در این حادثه مجروح شد و همچنان برای درمان جراحتی سطحی تحت مراقبت‌های پزشکی قرار دارد.
سنتکام به احترام خانواده‌های این افراد و تا زمان تکمیل مراحل اطلاع‌رسانی به آن‌ها، از انتشار جزئیات بیشتر، از جمله هویت نظامیان مفقود و جان‌باخته، خودداری می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/68567" target="_blank">📅 23:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68566">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uu8PiutGI_EWrL9qktMIUsHWvgsUR5iKA83wwmd6MCfrl35YjST_gEUNrupTgq_qiHdxngzhRVyxICpyH23TMswafWdShJzlbC4DlcO5LfJVtVwXummZwIpIOLZE2DOpMBJlj7B0JQ3wVRKviXSw6PUFDtPIpz-krKXqCb1yCInbbKB8A51sPGJk-LYYQoWdXGzU-OPReWjfIH58lEWqDCVHcgRJYZRA0Rh3mepAeLVknObenDIkEGuFuDdY4A1qNnk5V7gZZS85ABNhqp1le96H2OwZGDJgxnIlTX7njwGnsmataCfciWDDv-rdaLtLSi3giWQ53HaRIhZDsD-IIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا کاری به کریس‌فن‌ها ندارم ولی هرچی چپول، عرزشی و فلسطینی‌فن توی دنیا هست امشب طرفدار اسپانیاست، به امید باخت این تیم کثیف و سراسر چرک #hjAly‌</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/68566" target="_blank">📅 23:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68565">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce3cfd8ff5.mp4?token=a9e_uLNqd7cotZhRHuB0fo1cAfJYGvAl1vasSFBP0v34Tx1NMmq8wObwKt4tYHXibrUrnVcznKseE0BoJCKJM4YI9_MSG0Pis2riYqhfpmmQ0brUcD2uEva-09jpcw6UAZlHYUwlULRi6_9zFTNYWLhbau2dkavfw6sIS9QSkUFUBwbcDbBMSIaLRkY8E8F0aAUqgPy0s7BG_iWmkutrhcF90N6-k1PozO3NGeCaxrEcle9jsYcioxUcLxb8E9B5EAxdy5i7OSHXYpIzQjK1JkOkOS12NDU9TyacTvzBpxkvogDeMX3Kuu5O5NGBX93DhdG-OOm9JBRM4wWVvSI2NEZoCFiK5wk0LXg2f15OPbFbJ7pXVzhlglSlsZxnjS_h0dGYMIaJKpvQJdTiYwrUiEQ5XkiRjG0mAcu2kQ_Qyi_9ogJ43OSvWb9DAWtRJhKs88v_3JWs7-qLvseHHb77EWnMYjYm97xRyKvxm0s9023RLtX9fD8j3exQDfHCg9WNmxeKKAtjyeE3zQxf7BMBXnqzpVlFuVld8cwDAf1ytuV1TMuM4qHGjd3OZY9vD_gdyqQLnyl0BN07JBOMLSINeXlPUdWSubREIm1z0m1DlV388KMCjkhbVNfDST5qPKEqYJTAHXTXi4rdmeDilHZ9TA7A6iHwGBfbm3Q0fBtdJk4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce3cfd8ff5.mp4?token=a9e_uLNqd7cotZhRHuB0fo1cAfJYGvAl1vasSFBP0v34Tx1NMmq8wObwKt4tYHXibrUrnVcznKseE0BoJCKJM4YI9_MSG0Pis2riYqhfpmmQ0brUcD2uEva-09jpcw6UAZlHYUwlULRi6_9zFTNYWLhbau2dkavfw6sIS9QSkUFUBwbcDbBMSIaLRkY8E8F0aAUqgPy0s7BG_iWmkutrhcF90N6-k1PozO3NGeCaxrEcle9jsYcioxUcLxb8E9B5EAxdy5i7OSHXYpIzQjK1JkOkOS12NDU9TyacTvzBpxkvogDeMX3Kuu5O5NGBX93DhdG-OOm9JBRM4wWVvSI2NEZoCFiK5wk0LXg2f15OPbFbJ7pXVzhlglSlsZxnjS_h0dGYMIaJKpvQJdTiYwrUiEQ5XkiRjG0mAcu2kQ_Qyi_9ogJ43OSvWb9DAWtRJhKs88v_3JWs7-qLvseHHb77EWnMYjYm97xRyKvxm0s9023RLtX9fD8j3exQDfHCg9WNmxeKKAtjyeE3zQxf7BMBXnqzpVlFuVld8cwDAf1ytuV1TMuM4qHGjd3OZY9vD_gdyqQLnyl0BN07JBOMLSINeXlPUdWSubREIm1z0m1DlV388KMCjkhbVNfDST5qPKEqYJTAHXTXi4rdmeDilHZ9TA7A6iHwGBfbm3Q0fBtdJk4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇺🇸
پرزیدنت ترامپ و بانوی اول ایوانکا ترامپ در کنار اینفانتینو در بخش وی آی پی استادیوم
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/68565" target="_blank">📅 23:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68564">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zri1ytGa_taBkzXmFm4vw8n5Yl3WW7-QPBgvAkPuwEXzM4vWe6C8yyZxoxMErw_azdmkn9QexABHj4-km-qytlskNoEFipwlh5opj5ODg33cB-7O2c7EvVWDhseV7J9BuLE0EMNrlE1PCWxk_Kl-ODFGUwZ5XAb1Tj3cLBzvVBmx-lISXaEetnyU5UfdmhDTOMoBxHGzT3g4x-na0UJ_0ejIvi5Jas8Z7EUeMsQndnBu51mQH5XQrnUhAtkE8kWUYyrrGwmFkq5ucl5zpBT_xAR3i-IwdwT9jFHgn2YPX2t9bw02aL2OJAQp3NkboF0FkKZNYmsyN6LnheD1uxH_qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
گزارشگر صداوسیما : هیچ تصویری از ترامپ کودک‌کش و جنایتکار نشون نمی‌دیم!
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/68564" target="_blank">📅 23:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68563">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">حالا کاری به کریس‌فن‌ها ندارم ولی هرچی چپول، عرزشی و فلسطینی‌فن توی دنیا هست امشب طرفدار اسپانیاست، به امید باخت این تیم کثیف و سراسر چرک
#hjAly‌</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/68563" target="_blank">📅 22:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68562">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aOlji2n3SSKvNu3IYu_K8yj0hhNWizLcV_8i28grm8tlB6Sgs7Rn21Mfak9CzcYlqVaskW-DTBUiTMze3LGu-uv4Zc31Co1bNYdbZ63W3LBxZ7br-_JENUEj-1vAQHzyDwKSJRiv6kLnGk1WoV6-GijLgpDMUTCfglGBLYAjT7f6xl_8Bm_lW-ervMFLgGeopgevamgA1lP_b4Tvk7g1gSuev9cNfzXGefa23EBhllkS2mtLYo44BTxek7pneT5wRwdix31ze0vwfZAnRlVjeEgEMV-2bsQGS8IcS2YmME1bjXPsXX768SJxNRDL5i8nAL8Wz7C9mMvHObxeLPiRLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
هم‌اکنون ترامپ پشت شیشه ضدگلوله
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/68562" target="_blank">📅 22:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68561">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nup3XcAVs-cb_FEl4FHfV7rbkTE09WAxZIZFzQXvj2u2Vnd2n9k_dorSzv-W2_y5AWZhn1_DqX7cB3dFbFyk7N4AJ9QGRlIRcufJIyibFuTXDfzriNAGizvdUhjhAi17GPIVwALDM-EZjBGFmEZcTQEMRzawkT71FOpTA7lHhaCekCTbKaZvhF7FiQzpofJ2O3Kgol-LIgZyB3FuK1QKv3t9K4VKtRupX8BC8S_z8odOsb3q64tMJuSqxo4JKT3ZxwM--k5V9vYqeBUqaLJDfOpbzTChCUkhOqxGyZ6c3KjAyAGGf0PBW2WxKcw09lR5jWCGzplzjnOyuMfiqnRbyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فینال جام جهانی هم شروع شد
سپی
یه پلتفرم دست کرده به اسم چسفیل که علاوه بر خود بازی، تمرینات، ورود بازیکنا به ورزشگاه و… همرو
بدون سانسور و رایگان
میزاره
گفتم اینجا هم معرفی کنم شاید به دردتون بخوره.
هرکی خواست بازی رو با پوشش کامل‌تر دنبال کنه یه سر به چسفیل
بزنه
👇
لینک پخش بازی:
https://chosefil.com/fa/programs/318
ایدی کانال تلگرامش:
@officialchosefil</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/68561" target="_blank">📅 22:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68560">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c88de66012.mp4?token=aQVx_8A2mFN57TuBoxHHYmLFusGZOCSTfb2dp_IK3jYlwxv-KGJwoRv-ijOSdXxfKsLNWps4NK5KUjmxFMXMfiNzKGjxdZ4zjB6QCC3IaUmdJHl2oQz2kCCZs8QpSfhJIMK7k3cve_okWmXdqqLj4ey1cLwiQJwd910gORSRbbwE2vR5JfXNx3eNhJzruT1HwmqNKT3pZh0ZoPfIY3gXRbgZztN0y57pw6S8ZJV76EWFeFsFlGALZ4pw_4X4wkEFoknz7ycxCP322N1ui4fIygFzlp5icMpkV4Z2XrRYqF9EioqcKBP_aTDZ41FTg3Oq3c7ys2U7SQK-_GFuxCgWMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c88de66012.mp4?token=aQVx_8A2mFN57TuBoxHHYmLFusGZOCSTfb2dp_IK3jYlwxv-KGJwoRv-ijOSdXxfKsLNWps4NK5KUjmxFMXMfiNzKGjxdZ4zjB6QCC3IaUmdJHl2oQz2kCCZs8QpSfhJIMK7k3cve_okWmXdqqLj4ey1cLwiQJwd910gORSRbbwE2vR5JfXNx3eNhJzruT1HwmqNKT3pZh0ZoPfIY3gXRbgZztN0y57pw6S8ZJV76EWFeFsFlGALZ4pw_4X4wkEFoknz7ycxCP322N1ui4fIygFzlp5icMpkV4Z2XrRYqF9EioqcKBP_aTDZ41FTg3Oq3c7ys2U7SQK-_GFuxCgWMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مجری حکومتی:مشهد در18و19دی پنج ساعت سقوط کرده بود.
عراقچی: اصلا انتظار اعتراضات ۱۸ و ۱۹ دی رو نداشتیم، جمعیت خیلی بیشتر از چیزی بود که فکر میکردیم
.
مجری: ترامپ درست می‌گفت، من رفتم آمارش رو درآوردم، مشهد در عرض چند ساعت سقوط کرده بود!
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/68560" target="_blank">📅 22:26 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68559">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c26a9bf5f.mp4?token=T3zXlS3u3MLKh6h7tBPTODIsNAnUDUZkNxvH_eLvHnMaAvi_2WIiw1idNv-XIWTCNh0ISinbjNlkiA3PXur5WsIEwt6qpgCcgtV_NhXjcImW-CnW-WalDVRWL-ZForlqXsUU5VFjE_SIImw4Pn1X9AGtKnDEu9LZDzMXLt7gW3QiMGDQC85_Jw_pYMc37OiRIRSut-RTCpJN0sJR-oU1xmzRcnjoM6P9706fshyM_35M6LD7SzWKRPG_n0II-A2XavsUHohet8MZNzOn42jzd3yqIL9JpylKUaDDdqDYJaDFDYpDhwggp4ocj2RiKuXFmh5xgujxEFPJFn8NTcqjZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c26a9bf5f.mp4?token=T3zXlS3u3MLKh6h7tBPTODIsNAnUDUZkNxvH_eLvHnMaAvi_2WIiw1idNv-XIWTCNh0ISinbjNlkiA3PXur5WsIEwt6qpgCcgtV_NhXjcImW-CnW-WalDVRWL-ZForlqXsUU5VFjE_SIImw4Pn1X9AGtKnDEu9LZDzMXLt7gW3QiMGDQC85_Jw_pYMc37OiRIRSut-RTCpJN0sJR-oU1xmzRcnjoM6P9706fshyM_35M6LD7SzWKRPG_n0II-A2XavsUHohet8MZNzOn42jzd3yqIL9JpylKUaDDdqDYJaDFDYpDhwggp4ocj2RiKuXFmh5xgujxEFPJFn8NTcqjZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
پخش تلویزیونی اسرائیل؛مقامات امنیتی اسرائیل و ایالات متحده:
ایالات متحده در حال آماده‌سازی برای تشدید حملات خود به ایران است.
این هفته، خاورمیانه شاهد تعداد بی‌سابقه‌ای از هواپیماهای تانکر سوخت‌رسان خواهد بود، که این تعداد حتی در مقایسه با آمار ثبت‌شده در جنگ اخیر، غیرمعمول است.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/68559" target="_blank">📅 21:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68558">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
کانال ۱۳ اسرائیل :
دونالد ترامپ، رئیس‌جمهور ایالات متحده، پیامی به کشورهای حاشیه خلیج فارس ارسال کرده است که در آن تأکید شده است: اگر این هفته آتش‌بس برقرار نشود، این کشورها باید خود را برای تشدید تنش‌ها آماده کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/68558" target="_blank">📅 21:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68557">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
استانداری خوزستان:
دقایقی پیش یکی از مناطق خارج از محدوده  شهر و حاشیه‌ شهرستان آبادان توسط دشمن آمریکایی مورد حمله موشکی قرار گرفت. این حمله تلفات جانی در پی نداشته است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/68557" target="_blank">📅 21:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68556">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">مسی و نتانیاهو
🇮🇱
یا یامال و فلسطین
🇵🇸
؟!</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/68556" target="_blank">📅 21:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68554">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UHZGDWBfFOp0nbdHKExJN2qlj5qkVW5L4fzYbZOagVj3iIIwLYkPLLmDH1WKUq8AvrOrUrUftU8kpYe9c6daFwAsfPI5N3wjq7xF_0IgsWKuJS5z6vl2EfLLGhMHMllM5W6dTbGMDSPCo58V-VMCQUx5Ui_2szKDJ6HpEo6j3H9DVpN7mOd95i59WNXv48efG7PX6xB1GOtLbTrxDCZm73aYypKNbFZV2v01oMG0sgqOPNyE3lSt76cbTDunD9akA5hOtaXNUn2pOVmMwa-xeKZjZRPO1GPXDExyPfIMNVqj6m95dugMIlLbuPGcgj253l-ZIHdHI24jFMf7EfmIQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HakuTlevRBJq0prKzEmkh47d8J_wcDX1qaEt_aZfnhLiZ8RDqtULeZGzeosYZXBZB9piwP0d75Eo4xl2dj0ncHnfu6AKGbXNZy989nkhooL3Iw75eH6SnsD1zq9I2nYNMr5jluBHke8rpXLe4ZY_tTbOpZRgmUo73tWYm4E_FArJ7Bbhg3dmFXepV_X2-habVjV9_-3pCQdPCSbSLVqvfeXwkSFhhd_HAjkIksFtAiq_u4mdUmYnIcpQU_N7Ifza_EYU2P1hVLw7xwY4l68MAOzzvWXiFt2NDmPlIUt50CJhuoRPKxB-2doExCb4EjhJvF-aUSySiRnkq5R7ael9aw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💢
🏆
فینال جام جهانی 2026؛ شماتیک ترکیب دوتیم ملی اسپانیا
🆚
آرژانتین؛ ساعت 22:30
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/68554" target="_blank">📅 20:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68553">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
یک پیشنهاد جدید آتش‌بس ده روزه از سوی قطر ارائه شده:
• ایالات متحده حملات را متوقف خواهد کرد.
• ایران دو مسیر دریایی در تنگه هرمز را به مدت 10 روز باز خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/68553" target="_blank">📅 20:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68552">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e08df79c06.mp4?token=o7KsnWtyht46vQguGrQDO-wCDSmMhu8oPbBnznH63plHDAIgGO9Z03dk9d5aAfFSGjbk9RW9I8jVb7bdDjildaN7uh9kImyf84Mpdbk5OtPU2Ruef2wI_dSfU_mUCPJHUjhjgumAI_VZoL85SCe19KlM47gx_NJ3wOU06xPxti3IXsCqCgq61IzOTriuAzCoggw-Lri7OJ94n4B62im0yyD9kr3tKEBT_l0I5ls_u_Cph3zZ8sgQJNELcuIYQGCcyk4uWesa8NN5_kDanG8S_ijhDdSwMFW1CM57EjxOodaZsAhmK5Z9wLMe6_qLeEBQ3dEDZ_N2Bfxl5zoqpCu0Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e08df79c06.mp4?token=o7KsnWtyht46vQguGrQDO-wCDSmMhu8oPbBnznH63plHDAIgGO9Z03dk9d5aAfFSGjbk9RW9I8jVb7bdDjildaN7uh9kImyf84Mpdbk5OtPU2Ruef2wI_dSfU_mUCPJHUjhjgumAI_VZoL85SCe19KlM47gx_NJ3wOU06xPxti3IXsCqCgq61IzOTriuAzCoggw-Lri7OJ94n4B62im0yyD9kr3tKEBT_l0I5ls_u_Cph3zZ8sgQJNELcuIYQGCcyk4uWesa8NN5_kDanG8S_ijhDdSwMFW1CM57EjxOodaZsAhmK5Z9wLMe6_qLeEBQ3dEDZ_N2Bfxl5zoqpCu0Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
رئیس هلال احمر:
در تشییع میلیونی نه تنها یک فوتی هم نداشتیم بلکه شاهد چندین تولد نوزاد نیز بودیم
👅
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/68552" target="_blank">📅 20:30 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68551">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7091c7c4c.mp4?token=fMcJmR-n9nL1AG7Ro8GiM4CASjoXpybmIb7uVkrc0lx3aVNY243Aq78AxZV8yTyTnAhBWFZ1vHk7MSIMydoNsi0yc_0z_39mv6G2_23TyWf1ZnXc8wEwD4mHcBF255v-2T9yjkgrgRl3FDJqXRd0GBaJc6wICGzS6ALjMlTxoZ_mzX1dYAPCxPGzwDxqkWbjZGtPAcaCXS2OEIaZGCJuKNCdgk3Iy5xNUI7m7eafPMZAwUrujTaEBNQvRPTCB5Jjdjd6sckhGl_Orf7zauM3mgAv2G9a8-yVeGuBtJuhUQmPO5hQAbyawvFkJ-oqixXD1Stcj11Ph0S1Qgnfs_v7pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7091c7c4c.mp4?token=fMcJmR-n9nL1AG7Ro8GiM4CASjoXpybmIb7uVkrc0lx3aVNY243Aq78AxZV8yTyTnAhBWFZ1vHk7MSIMydoNsi0yc_0z_39mv6G2_23TyWf1ZnXc8wEwD4mHcBF255v-2T9yjkgrgRl3FDJqXRd0GBaJc6wICGzS6ALjMlTxoZ_mzX1dYAPCxPGzwDxqkWbjZGtPAcaCXS2OEIaZGCJuKNCdgk3Iy5xNUI7m7eafPMZAwUrujTaEBNQvRPTCB5Jjdjd6sckhGl_Orf7zauM3mgAv2G9a8-yVeGuBtJuhUQmPO5hQAbyawvFkJ-oqixXD1Stcj11Ph0S1Qgnfs_v7pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
نتانیاهو :
آرژانتین امشب قهرمان جام‌جهانی میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/68551" target="_blank">📅 19:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68550">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i732u5z9bGcueAGlw6d2-Yxh-54mFWH8SKQNafcf3MClOUovxwCP6iHRwVTcmACw1MqcH9H6O4GmhRqMmQhqhvWpwLNKMAhOdLyMcDaUr1LCroRohr_JvsJkRULsvgO_B6_cBaDyseTIZc4ZfdP4R35iyVb2LGl1dqLE8PZzeKza9eLNIzw_d7JPtMZ4rD1OZgOENO3CQsOM0ecqCsB-P4hqbNTzb43UhW1Ath38i5z56RJeko-cYWtil1_VCp05wXCPAtHxFH0o_lEsHjskEsVMFwNWVEY4NdCADt_3xuJP8cBfDQ8S7FwGdSSZOiA87aNVluK4FXTEtzZZp7LyHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه امشب نیروگاهی در ایران هدف قرار بگیره، مقصر اون فرماندهای زن‌جنده‌ی سپاهن که امروز برق کویت رو زدن. #hjAly‌</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/68550" target="_blank">📅 19:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68549">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">‼️
رسانه های عبری:
برآورد‌های امنیتی اسرائیل حاکی است که رهبری ایران دستور حمله به اسرائیل را صادر خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/68549" target="_blank">📅 19:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68548">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
هدف قرار‌گرفتن یک نیروگاه برق در کویت  @News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/68548" target="_blank">📅 19:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68547">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TCVd4eSeW8c45KrsrNTgu-NdrX27Cx_7mLPv-XHZfTVz9WWzX7l_WlFMIcUhZoLWNNZ4T8AAY6WpVvqkEyzwkh42ZwenKeDgAHAqiEn0oNIGSo5mr9TRVb45TwMCLQ2UkxaE7W3ZoWrcgwRS0g7OHGJw9ShXys2mVVAvEGzB5QEJ3bnsJWnm5oHcerMFMUj8VPKPwKDfwLHcEFQPlZTHasyAX60in_BaE8StAdsWH-mttPz8ZXEnDqx3VlO6zckJ1bw_3115QSkhtxNMxjx-_3OqDbRdyDIvTDYc9lOfn8HkHcTcIyClMMu34y9FLpWyQgt-BCRMJ8SBqkRrPT3EUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
فینال جام‌جهانی ۲۰۲۶ فوتبال
🇦🇷
آرژانتین
🆚
اسپانیا
🇪🇸
امشب ساعت 22:30
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/68547" target="_blank">📅 19:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68546">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/798b52eeca.mp4?token=aDCP6-4rUKXwrRnAgTAvGWpiAausihS9AY_-YJ1YwBWtaV7BmTPZgW-qOLwmeT4LIfSc4kGw4CaTLaXMSM1JUejo_n4bEGYQvuvz_GHIchns8gh0rQEEE_CzjEJf4po62r2rlDh8Hrs_57lJL64AbHeQ7Y1A8KMO96X6OWO0CRnqBrKbHnEQ0kDVDy7PDLTssnbbTC6HO08Ac3i1UlY8a3A72X6GYzOvU7BfVONrSKAxZ3hKi5srzPBT3GoOu7CuldjmzWieUk76v1golPG3Zq3Sh_H6tS3_k9qWWIEvy9w3aJe7tLGKD0c1GoAk5tDNS44Wvv8nUKkUMIrHT8cGxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/798b52eeca.mp4?token=aDCP6-4rUKXwrRnAgTAvGWpiAausihS9AY_-YJ1YwBWtaV7BmTPZgW-qOLwmeT4LIfSc4kGw4CaTLaXMSM1JUejo_n4bEGYQvuvz_GHIchns8gh0rQEEE_CzjEJf4po62r2rlDh8Hrs_57lJL64AbHeQ7Y1A8KMO96X6OWO0CRnqBrKbHnEQ0kDVDy7PDLTssnbbTC6HO08Ac3i1UlY8a3A72X6GYzOvU7BfVONrSKAxZ3hKi5srzPBT3GoOu7CuldjmzWieUk76v1golPG3Zq3Sh_H6tS3_k9qWWIEvy9w3aJe7tLGKD0c1GoAk5tDNS44Wvv8nUKkUMIrHT8cGxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
هدف قرار‌گرفتن یک نیروگاه برق در کویت
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/68546" target="_blank">📅 18:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68545">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
🇮🇱
یسرائیل کاتز، وزیر دفاع اسرائیل:
«ما اعلام کرده‌ایم که اگر ایران جرات کند به اسرائیل حمله موشکی کند، ما با یک حمله قدرتمند، بدون هیچ قید و شرطی، پاسخ خواهیم داد.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/68545" target="_blank">📅 18:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68544">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🧾
امکان ویرایش شرط ثبت شده
💥
برداشت سریع با کد پریمیوم ووچر
💵
شرط بندی بدون محدودیت، بردهای نامحدود
🎁
جمعه و دوشنبه‌ها، شانس بردتان را دو برابر کنید
100% بانس میکس ورزشی تا سقف 30 میلیون ریال
🎁
با واریز کریپتو، سقف برداشت خود را به سطح جدیدی ببرید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/68544" target="_blank">📅 18:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68543">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IkkThs2KygTF6VDJx5LcAyx28IQ9Qh33yWHn4F7vBrSH_E5Bglgo_ai4hMaL3a33n3MOMBc-iYvqpj0lK74-uMv5wZ3XjOMuXYW3mVIfFYrQ5zNNm_1UVg-8vUXNIPyOYbXF55JFkhZMRTgEyU7QaFSXAaLwpdbdxtlLKqeQbUHK-RHs0QnLiyzBIEFcByZDIZQQ0Hxn9Q2U2cq5jrBXdiADypfZ9iv3kNDHLLdaD6FgRLxyqKOnzSlouzm0pOncaWdi017SBFmrA44vOshFJkn9yvWl-l4NAVL0eO8x8eAqWw5Mvl5G-duqEOO1XIxuSgXZq5X1czBrhPTV-ExcYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فینال جام‌ جهانی 2026
⚽️
اسپانیا
🇪🇸
-
🇦🇷
آرژانتین
⏰
شروع بازی ساعت 22:30
✔️
امکان ثبت پیشبینی با مبلغ نامحدود
🫰
محاسبه نرخ دلار با قیمت 2.200.000 ریال
⭐️
فرصت استثناییی چالش‌های پیشبینی فوتبالی سایت یک توتو، با جایزه 500 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/68543" target="_blank">📅 18:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68542">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24db6b1462.mp4?token=Lv3JJaEQgc79Sex2luXshv9Ubx0-2seMLRqcz1O5gpc9kvD3COEH62TPzfMpMsZaiDcDYnXMIpBcAgEufggcEKguL-sR0TLZJTPWS2WVslxxH4r-O6fVQU7O6zCGMI4JA39kbTCfGHcBiy88OnOpRBSgHuKcCk4OEjAtGpXHwUk0EJtjXbC1muxjiSPBNCi0gRs0-Brut2JQf_mfFPTEID3FUl7ZLZixJ1M2sot0oZfQMEhN6eGRo0C8UU9LYOMTHGl-u33p3jkQ6eJ9HLcKct-sHUnaxLkA5VtAxftA1tvkqpAEH1uxqJzTA6Xp0Pl0oQitjGMbA9wAT8T92f17Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24db6b1462.mp4?token=Lv3JJaEQgc79Sex2luXshv9Ubx0-2seMLRqcz1O5gpc9kvD3COEH62TPzfMpMsZaiDcDYnXMIpBcAgEufggcEKguL-sR0TLZJTPWS2WVslxxH4r-O6fVQU7O6zCGMI4JA39kbTCfGHcBiy88OnOpRBSgHuKcCk4OEjAtGpXHwUk0EJtjXbC1muxjiSPBNCi0gRs0-Brut2JQf_mfFPTEID3FUl7ZLZixJ1M2sot0oZfQMEhN6eGRo0C8UU9LYOMTHGl-u33p3jkQ6eJ9HLcKct-sHUnaxLkA5VtAxftA1tvkqpAEH1uxqJzTA6Xp0Pl0oQitjGMbA9wAT8T92f17Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ستون دود در دزفول
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/68542" target="_blank">📅 18:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68541">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c53fd88605.mp4?token=XINpXbR4fE6oOnNn_s5z9eb5KdSJLpyOuxcuIrGEDQcx7t0UtVSsUGjbTWtIawuctb8SUw6yLKOd2fFrbBi54OabHsfnyQ31OnpmwrWN5woTJoaNn11ChsBxSBdygal9oWgKyckO5TT-uFqJagXKPK5NDn1bQ5RoMLGTTXaDCiF3QLckWhz2NFj9FT45KuKWRo-j9lTD_7hP4BkAmnxMuMjtQw3yfMM5-orjZzrEqKWVtYyyL9m_BBVlwmVAl10Rm-jhzgwZdJN1qr9zb5bKkMyr5UjmZVQl5sXWUCmeQ1gJ_p1XiGU0mhG7wayi_Gkgq98SB8q8cnlLJieNPyNUYAunlp42nCvqF3YUwlNQKzXK2iE7KMz6aQUlsUOtjLt2pczT_AM1F_DhXT-NprzPuSPMbx2StDjmdQvGMuxZ4Jzc-XA8pbIQqW2czA2lRAjKd9SjQKMgrbmwxU4Vqr7tw8kttoIwhFu5PwOcmFOtckXl5-CEU7vEYGc7HbL0VBOOSQVzX5Tkycd85hBp_8IHtP3ewS-HRON2eOO-HXnbyan6LSLqD3rrRwdDVrcfW9JLvOR8qv5s9P7pD8ivu9Zg7YeF-cS5AJWKJclETCo4iAYuL3zE5zyCLhr3FyAiEolZ3UYkKoNUurCbovJ58uqVgM-cbZiervDtAcIHGzTXquI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c53fd88605.mp4?token=XINpXbR4fE6oOnNn_s5z9eb5KdSJLpyOuxcuIrGEDQcx7t0UtVSsUGjbTWtIawuctb8SUw6yLKOd2fFrbBi54OabHsfnyQ31OnpmwrWN5woTJoaNn11ChsBxSBdygal9oWgKyckO5TT-uFqJagXKPK5NDn1bQ5RoMLGTTXaDCiF3QLckWhz2NFj9FT45KuKWRo-j9lTD_7hP4BkAmnxMuMjtQw3yfMM5-orjZzrEqKWVtYyyL9m_BBVlwmVAl10Rm-jhzgwZdJN1qr9zb5bKkMyr5UjmZVQl5sXWUCmeQ1gJ_p1XiGU0mhG7wayi_Gkgq98SB8q8cnlLJieNPyNUYAunlp42nCvqF3YUwlNQKzXK2iE7KMz6aQUlsUOtjLt2pczT_AM1F_DhXT-NprzPuSPMbx2StDjmdQvGMuxZ4Jzc-XA8pbIQqW2czA2lRAjKd9SjQKMgrbmwxU4Vqr7tw8kttoIwhFu5PwOcmFOtckXl5-CEU7vEYGc7HbL0VBOOSQVzX5Tkycd85hBp_8IHtP3ewS-HRON2eOO-HXnbyan6LSLqD3rrRwdDVrcfW9JLvOR8qv5s9P7pD8ivu9Zg7YeF-cS5AJWKJclETCo4iAYuL3zE5zyCLhr3FyAiEolZ3UYkKoNUurCbovJ58uqVgM-cbZiervDtAcIHGzTXquI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
صحبت‌های وایرال شده سرباز آمریکایی خطاب به مردم ایران :
اگه حمله زمینی شد بهتره فاصله بگیرید از نیروهای آمریکایی
نه اینکه بیان شمارو اذیت کنن، چون ارتش آمریکا خیلی مواظبه از سپاه که بعضیاشون لباس نظامی نمیپوشن
سپاه میخواد با اینکار به نظر برسه که مردم ایران علیه ارتش آمریکا هستن
سپاه اصلا توانایی نداره علیه ارتش آمریکا بجنگه
پس اینا می‌خوان پناه بشن بین مردم و حمله کنن چون اصلا نمیتونن رودر رو پیروز بشن
خداوند ارتش ایالات متحده و مردم ایران را حفظ کند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/68541" target="_blank">📅 18:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68540">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6029372426.mp4?token=a_T54Lk2j9b3Z-KZEgVKjXVxIcqejnOvga9qAKpLE6aZAAjg_bvBcsmSuRFZLINHGqdmgmoP9Fchowhu5mYWDgYwRbiWObnaKIbWAH7a3wASvSpK6hipVo5vmnqenL6Z21Gzlthiy8Abfx2AU3HqlQl2l9jMHQCAhxJAnkyLAsQn3xG3Ff_-jrCwAhZFvsbH9NTyoPalKysJFmfSjJrNy_2gfFB5m-28PXmvj8AWExTV6zDYY9sRmZgcRF2Qt6b7FpHhQryyG3h05Wg1p2yMRxV540WCKu8JSnRjBEwKkL29Qp9Vl4bJtdn9L0vI4hUPujPZHs01WTfzLVYcC_PRUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6029372426.mp4?token=a_T54Lk2j9b3Z-KZEgVKjXVxIcqejnOvga9qAKpLE6aZAAjg_bvBcsmSuRFZLINHGqdmgmoP9Fchowhu5mYWDgYwRbiWObnaKIbWAH7a3wASvSpK6hipVo5vmnqenL6Z21Gzlthiy8Abfx2AU3HqlQl2l9jMHQCAhxJAnkyLAsQn3xG3Ff_-jrCwAhZFvsbH9NTyoPalKysJFmfSjJrNy_2gfFB5m-28PXmvj8AWExTV6zDYY9sRmZgcRF2Qt6b7FpHhQryyG3h05Wg1p2yMRxV540WCKu8JSnRjBEwKkL29Qp9Vl4bJtdn9L0vI4hUPujPZHs01WTfzLVYcC_PRUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این مجری که اخیرا زیاد در صداوسیما حضور داره گویا اهل کشمیر هندوستان هست.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/68540" target="_blank">📅 17:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68539">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kCIF-HyGoYZTL5eZvcfuUW7kgUkh1lEou22awQ_nkAj_THz-ceGjQx7REAZ5pcOJWvsMRc3JKRSXhayRJTRHS6CSXJC29Z-lIK0t85JOlAXeUYH5WnZ-miNK8klqhz0d7yw-jxUkWSvUODjr-3WMTuE43kt8LzhynJ0N1fHCSyN-XevtizdXgYrYs2HDuvSf4YBhE5nLdRDHsrNOn-SZ484Ak98aazhWFlaMWzvhWMtWiaHDhfzsj6ohOwQujBVRVqHGU3AtOxxEiiJtUVRdlD7w53FAkAAhZTd_5OoaNOJRA5EPBRhcPBxNIpTMnJ_Lt5NONzjrWKMOTwxnTjlHHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سازمان انرژی اتمی جمهوری اسلامی:جت های آمریکا صبح امروز با شلیک چند موشک به سایت نیروگاه هسته ای درحال ساخت دارخوین در خوزستان حمله کردند.
ما حمله آمریکا به تاسیسات هسته‌ای دارخوین در خوزستان را که هنوز در حال ساخت است، محکوم می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68539" target="_blank">📅 17:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68538">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4472fedbde.mp4?token=dCGzH1B4QkrJnYEsaxwlsLUrSAXjnf_jrEjrfztGNvdvPfxU5SxyLq5ZTN4S5cxkMOMhcGbWgXBffAOxZ7XD_7s-dIAWiEtg4xG1vopygSaVO_oDncJq20S8TPCogxE9RZk507lWJlxO-VHwF5tG9icq3lFWuwYdgfNCyVrhjHwJ5m_Gs7XcitCsH8Y6l2xxUAwd_gm7utoSynC4_uAwWLasOVMQoSfLhbE8WXcElwpIXXj7h1JZoQPwWCLi5QY82oJImlY-z_dDJLqq9CphxNm63KRSPYYvyWii67kjXlk83Uu9lQ6KbdglObGWk4VcqufSMRIhyGHTlWkP9GVF9QOf8YKNj6WtPkApBDMH2QC-7D8zSotv_USj2WyrNh4kFqGNWN_KwQYAGA6YZfp2-1_IRk14yodkqAyzDgleTr5Vy2lU3egaLxreXtFaFysaE_K_IqqHbXQnZU3qdSzJOpODhfXUlQ8vmNcIH41RjlDMaw5l3JMO5K3Rq5FV9cK-qBKfteluym1115_wHh_NHo9zgYmaw3JXBoBvMDWNCYtitSvzitZt7_ARM9vCRV4ELLpKM06no8yEHBUjRXqRFq_NOs4E6AcMZXe25fPBPGQZvHkf4ZezBOm_tRyI1OZYWKBIjIO9W8W4uaKmt__ez6DfCx8ebopqRjyF-KyGmPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4472fedbde.mp4?token=dCGzH1B4QkrJnYEsaxwlsLUrSAXjnf_jrEjrfztGNvdvPfxU5SxyLq5ZTN4S5cxkMOMhcGbWgXBffAOxZ7XD_7s-dIAWiEtg4xG1vopygSaVO_oDncJq20S8TPCogxE9RZk507lWJlxO-VHwF5tG9icq3lFWuwYdgfNCyVrhjHwJ5m_Gs7XcitCsH8Y6l2xxUAwd_gm7utoSynC4_uAwWLasOVMQoSfLhbE8WXcElwpIXXj7h1JZoQPwWCLi5QY82oJImlY-z_dDJLqq9CphxNm63KRSPYYvyWii67kjXlk83Uu9lQ6KbdglObGWk4VcqufSMRIhyGHTlWkP9GVF9QOf8YKNj6WtPkApBDMH2QC-7D8zSotv_USj2WyrNh4kFqGNWN_KwQYAGA6YZfp2-1_IRk14yodkqAyzDgleTr5Vy2lU3egaLxreXtFaFysaE_K_IqqHbXQnZU3qdSzJOpODhfXUlQ8vmNcIH41RjlDMaw5l3JMO5K3Rq5FV9cK-qBKfteluym1115_wHh_NHo9zgYmaw3JXBoBvMDWNCYtitSvzitZt7_ARM9vCRV4ELLpKM06no8yEHBUjRXqRFq_NOs4E6AcMZXe25fPBPGQZvHkf4ZezBOm_tRyI1OZYWKBIjIO9W8W4uaKmt__ez6DfCx8ebopqRjyF-KyGmPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش امیر رولکس به حواشی ساعتش در جام‌جهانی:
به جا اینکه بگم فوتبال با ما سر ناسازگاری داره از کلمه خدا«داره مارو میکنه» استفاده کردم.
چهل چهلو پنج ساله ساعتمو دست راستم میبندم.
اگه یه سرمربی ساعت می بنده و لباس خوب می پوشه که اشکالی نداره.
اگر من زنجیر طلا مینداختم  و یقه پیراهنم رو باز میزاشتم آدم خوبی بودم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68538" target="_blank">📅 16:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68537">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oSsBCVPRuJapN6HZm4YSZJvmqekUsViBKdZvVhkSGHY97EvFGBOSD5RSEpdDOVix89CCZPn_hL89DT6HMNRAiMU1U6EQPKnNd53V5bqdVl2D8ZXJ8FobHPGqgR8yYxN21bC7V2xexsU2P9hGADosdcKHfK76rShX7ZpmlxUY_glHvqY1K_2BT69q-4VK4tddWHNEivtpa0IwxzqkWAWzovRDsFVAgsCm2FxC0Dq59_nt7uWbMRlYNZfdf0fuN7efaH-uMUqfaBL38h5DyRCnrx5C41qoOV_spwsbhXayVMSeZ_WjNM97JaJgCKvAzc2zBuawmCE2WfUjwNscDWT0lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
پرزیدنت ترامپ:
جمهوری‌خواهان باید ایران را به لایحه تحریم‌های روسیه اضافه کنند. این همان کاری بود که لیندزی می‌خواست انجام دهد و قرار بود محقق شود. مهم!!!
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68537" target="_blank">📅 16:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68536">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KeZQsFi1nNXCdPgkaEXxheJYYvKz59T9X2o90m1cHTLvhacYto9DDX_UtBZ8bnpk7uU1jpMP_8qFzfNjrF20laIAJ1QozNtqGFdBf3mZp3HptmgLUhpqtZTZuEhxBJea5vbVMp63z_K-kw7U6Ok8FpbGVwACe_I0-04DQbtXA5tjdtNg_CANaWr4rDgeURHJa6jCs1gSKbjhCw3OpArE155P2ieocz7vGknpOEYusJQ26g0YEuu1AHd0fGn8TeaVYC6sIqdZvTcr_D8Lzo25n1Hlk29uf0Q8xdmJoFqY-xFAO-cBLGnRW0xHcsfoWog9UiEd0mlTF7iSzhDYYHlT3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">14 زندانی تو زندان دستگرد اصفهان برای اجرای حکم اعدام به سلول انفرادی منتقل شدن؛ این 12 نفر از متهمای پرونده میدان علیخانی هستن. +پرونده میدان علیخانی مربوط به  اعتراضات 18 دی 1404 تو اصفهانه؛ اون روز بین معترضا و نیروهای حکومتی درگیری شد و جمهوری اسلامی مدعی…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68536" target="_blank">📅 15:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68535">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇮🇷
عراقچی:
بمباران بیت از طریق حفره امنیتی صورت گرفته و این حفره امنیتی همچنان وجود دارد
.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68535" target="_blank">📅 14:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68533">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3548648f57.mp4?token=EngxXc3kUSX1LTEMlUTksaOcYtwSgR2808WXiCIDYXwdZggdLPH5KFdKgpDDW8OCFR01I6ExCEPvUewQtRdzv296vbgKVJMeWDzm5nU7zIuefNVMq6kMNXV9mpPnui9MWX8u0tiUKe1lvYb5LLowGFvoZDauTxleldf8LOUkO6UWAeftS9a8qpWm-5EEyRp5lMPAaddkoeQqx-VZawR7BNHkL9GgL6v1JIfwgH93PXSJwq5IIoirC4HYsg3NOt-G6XVicKnsWtbfK6c16yOWQPCnaXQVc9f7qHbWqs0ss6btwmgzgCQlasGfwUzrE67P8qchS-VUmo2qxZSNSkvMfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3548648f57.mp4?token=EngxXc3kUSX1LTEMlUTksaOcYtwSgR2808WXiCIDYXwdZggdLPH5KFdKgpDDW8OCFR01I6ExCEPvUewQtRdzv296vbgKVJMeWDzm5nU7zIuefNVMq6kMNXV9mpPnui9MWX8u0tiUKe1lvYb5LLowGFvoZDauTxleldf8LOUkO6UWAeftS9a8qpWm-5EEyRp5lMPAaddkoeQqx-VZawR7BNHkL9GgL6v1JIfwgH93PXSJwq5IIoirC4HYsg3NOt-G6XVicKnsWtbfK6c16yOWQPCnaXQVc9f7qHbWqs0ss6btwmgzgCQlasGfwUzrE67P8qchS-VUmo2qxZSNSkvMfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
وضعیت ایستگاه مترو در کیف بعد از حملات سنگین روسیه به پایتخت اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68533" target="_blank">📅 14:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68532">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🧾
امکان ویرایش شرط ثبت شده
💥
برداشت سریع با کد پریمیوم ووچر
💵
شرط بندی بدون محدودیت، بردهای نامحدود
🎁
جمعه و دوشنبه‌ها، شانس بردتان را دو برابر کنید
100% بانس میکس ورزشی تا سقف 30 میلیون ریال
🎁
با واریز کریپتو، سقف برداشت خود را به سطح جدیدی ببرید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/68532" target="_blank">📅 14:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68531">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d8Bp7OGLF8aTFcEglXBjvn_N6KOp2UrnXExGDf18MqYdXiVbq9F6Z24i8K8ccMQ32WpNUkMY9Sahi0RPcgHNvkpDh_1qkKhzMECDcW6OF8lsgJigUiBHrm4aN6kFgEnlOElL9pPHlxlzm39UXyrUUzPxmI3WTmTN6O208vp2U0Bjcc96luzog67VU4HQH0m0G-Y-iiu8yspGTXBJaeyq_9X_-NHc2B0-wK8ndGjtEGtNgKQdFu2VBeMqr2ffKnnJra2eeJwoKPjKFlp9eHrTXh9xkWQrtMInRStTj6y_MpEXOTPlZtDCOD4ZZFFB7TZqFNQzJK3YM9-VLNtpkal17g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فینال جام‌ جهانی 2026
⚽️
اسپانیا
🇪🇸
-
🇦🇷
آرژانتین
⏰
شروع بازی ساعت 22:30
✔️
امکان ثبت پیشبینی با مبلغ نامحدود
🫰
محاسبه نرخ دلار با قیمت 2.200.000 ریال
⭐️
فرصت استثناییی چالش‌های پیشبینی فوتبالی سایت یک توتو، با جایزه 500 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/68531" target="_blank">📅 14:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68530">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/326d421018.mp4?token=C1qCpmQvgPCx1YNu-NiT5rDdQgZKhlWMadHgAio5Wrm4n3ffwAdljjtrVkjhkpRvMUBm8r93QKbT0jZvYhVEOAdow-dCgVOIw66BgM6Nb5jvkSaTw9Lre3YhDRkyfkIFWYhfkT0Q1ED8LMbaAORjwDygmh6cH6GaT49T6Sw3EURGIkj3WMx6r7Beu3FcQXJ6G1kudVmM_JU40Gfv2Cl_slDidOpwvO7SIhhn67ZzokK22hFMEIbo4ciAz9e_rlTWhJUzgDHPxy2VWrCT5-CSbmkVRht6KGM2StKlzoGHB8QGEF7lEkjBCooI9t9v3F07vvBsyq7k2YKNV06UPPxX2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/326d421018.mp4?token=C1qCpmQvgPCx1YNu-NiT5rDdQgZKhlWMadHgAio5Wrm4n3ffwAdljjtrVkjhkpRvMUBm8r93QKbT0jZvYhVEOAdow-dCgVOIw66BgM6Nb5jvkSaTw9Lre3YhDRkyfkIFWYhfkT0Q1ED8LMbaAORjwDygmh6cH6GaT49T6Sw3EURGIkj3WMx6r7Beu3FcQXJ6G1kudVmM_JU40Gfv2Cl_slDidOpwvO7SIhhn67ZzokK22hFMEIbo4ciAz9e_rlTWhJUzgDHPxy2VWrCT5-CSbmkVRht6KGM2StKlzoGHB8QGEF7lEkjBCooI9t9v3F07vvBsyq7k2YKNV06UPPxX2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
نیروهای امنیتی سوریه یک محموله تسلیحاتی دیگر ج.ا به حزب‌الله را توقیف کردند، این یک کامیون خیار بود که زیر آن ده‌ها موشک کورنت ضد تانک قرار داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68530" target="_blank">📅 14:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68529">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">‼️
ملی‌گرایی از نگاه خمینی، بنیان‌گذار انقلاب اسلامی:</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68529" target="_blank">📅 14:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68528">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93f8a1edf1.mp4?token=ZtwXNzN5iaF-61QroO-Nkcyd3CAaNkyTmTdBkqpFZJOFXHvuvUFBT4nxm2sBU4sDEAlS8SOWdH2bPKYdWy71xNxXqRkV4ETD_geGl3YT2G39ww9JrVGhaFA5REpTgMUBOz2mC7K7ncTETIiVpyqllHPS0QJHxIMVnQe6suLZTvvgirgYtEDUE2twU_KNvX-rM-Lp--sUujhayH6SREKkz8u8HwIjmCb10Xu1ZUaWjqQ81SiCPapYBNqs_AWFs-CRKh5XWa08x7gOkJ2sdtkmDWW2WfbTa3xs9UPW50ppkZ2YYDUOLqlWvpGiHSqeeRqHehxK210mZmMVZCg0YnX3Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93f8a1edf1.mp4?token=ZtwXNzN5iaF-61QroO-Nkcyd3CAaNkyTmTdBkqpFZJOFXHvuvUFBT4nxm2sBU4sDEAlS8SOWdH2bPKYdWy71xNxXqRkV4ETD_geGl3YT2G39ww9JrVGhaFA5REpTgMUBOz2mC7K7ncTETIiVpyqllHPS0QJHxIMVnQe6suLZTvvgirgYtEDUE2twU_KNvX-rM-Lp--sUujhayH6SREKkz8u8HwIjmCb10Xu1ZUaWjqQ81SiCPapYBNqs_AWFs-CRKh5XWa08x7gOkJ2sdtkmDWW2WfbTa3xs9UPW50ppkZ2YYDUOLqlWvpGiHSqeeRqHehxK210mZmMVZCg0YnX3Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری:
آتش‌بس با نظر آقا مجتبی بود؟
🎙
پاسخ
عراقچی:
این چایی برا خوردنه یا دکور صحنس؟
☕
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68528" target="_blank">📅 13:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68527">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🇮🇷
نیروی دریایی سپاه پاسداران:
ساعاتی قبل، دو کشتی متخلف در مسیر ناایمن تنگه هرمز دچار حادثه و دو کشتی دیگر از ادامه مسیر ناایمن منصرف شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68527" target="_blank">📅 13:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68526">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6daaa9359.mp4?token=T_hSw4SLoyPSYmfdViAX_IM31vMh5gftdR63pxhPnyb-0dgvsUY5WzCgxlrB7gaHHaHpkrtUVNsWKGpeheRbblSdOai6haYZPmfEKeUa8-QJ0MgfpeDC04vsMCTyFg2IuhiwgG2b4dFfgHAQqOdq6Igz5hZEYMRX4tdNlsxLKU4u-M5mhIoC7EJpu9ze5BNa491aX_lVtcFdt_vikJOuO5lNsvLalZlzzQfe7ULd5OGSFl_Iu78o-qmvgH9CgNWRc1cASSUMkJIz-KgnEEhSaFk-OsgvZlswyLxllzizm4GX4u8lr-jGLZoXNA9vKF_NzXVJ5aaICTnfVHRurVicsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6daaa9359.mp4?token=T_hSw4SLoyPSYmfdViAX_IM31vMh5gftdR63pxhPnyb-0dgvsUY5WzCgxlrB7gaHHaHpkrtUVNsWKGpeheRbblSdOai6haYZPmfEKeUa8-QJ0MgfpeDC04vsMCTyFg2IuhiwgG2b4dFfgHAQqOdq6Igz5hZEYMRX4tdNlsxLKU4u-M5mhIoC7EJpu9ze5BNa491aX_lVtcFdt_vikJOuO5lNsvLalZlzzQfe7ULd5OGSFl_Iu78o-qmvgH9CgNWRc1cASSUMkJIz-KgnEEhSaFk-OsgvZlswyLxllzizm4GX4u8lr-jGLZoXNA9vKF_NzXVJ5aaICTnfVHRurVicsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تصاویری از انهدام یک پهپاد نظامی مدل MQ9 متعلق به ارتش آمریکا در عسلویه
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68526" target="_blank">📅 13:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68525">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c817c7306c.mp4?token=BkZpSxO2uNFfpZeD02Kg5gxCGUq31puKF7oMGq3f92Y_IC7ZSOaYkgddn1gfgpFqpYiKrRYvLE4K2UrZdWo5SdmnLg4SL3E8YaQrijKDU2Cs-jRDJZweiSUMVj69Cj_sPIZ80Z-LekvenmTU1l0UMrQGsixPOPpqwF7a8GqZWkhYqSu8Jk_YkC_cy_utNE49XcAY4mpLx-Vreg1kDZH1m06Kh_XYVV_kda9QLZ0NPlnZFxK9tXmNjkdTXnzi2Eh1d9_9Y74KtUkRFFGKOtjDbpLBkV2bRd_g9TSUsQlRZ7YhK-L_-GYcbtWSNNV3Vh8EHSvd_veHlTGgjs8H5TkJpifiSg9WnPykkLPIZFcB7NkKtTu7vb5kEzMWkgL5dp-aOt6rVEYPsy63lNZ5VqY6lGMMWytTwBdvkkxxVGAGH90XXg7lnBpUceAJ_1x2q2Bq8MBe7IAIbQpQBRnZvC4h5So5aXQOcuuzAEC_XOEr7Bmq-dHXdSyYM4VmG9bmRMROPkufhDukRj02q6IstEB5WERcZtn_iJ2WUzYlLxWNRqOnrAHxL8IVi40wKHLZ4ZhW_6GhpOL4RoRtiNM1J2IqQpiPSbEMx5FfE9nFOvUWcqos4GzRbRmk4TqnKRVRU5zNsvKTC1nKN8RsNeBWh0uyGHjCe8a0E8QTQd52kT9CBGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c817c7306c.mp4?token=BkZpSxO2uNFfpZeD02Kg5gxCGUq31puKF7oMGq3f92Y_IC7ZSOaYkgddn1gfgpFqpYiKrRYvLE4K2UrZdWo5SdmnLg4SL3E8YaQrijKDU2Cs-jRDJZweiSUMVj69Cj_sPIZ80Z-LekvenmTU1l0UMrQGsixPOPpqwF7a8GqZWkhYqSu8Jk_YkC_cy_utNE49XcAY4mpLx-Vreg1kDZH1m06Kh_XYVV_kda9QLZ0NPlnZFxK9tXmNjkdTXnzi2Eh1d9_9Y74KtUkRFFGKOtjDbpLBkV2bRd_g9TSUsQlRZ7YhK-L_-GYcbtWSNNV3Vh8EHSvd_veHlTGgjs8H5TkJpifiSg9WnPykkLPIZFcB7NkKtTu7vb5kEzMWkgL5dp-aOt6rVEYPsy63lNZ5VqY6lGMMWytTwBdvkkxxVGAGH90XXg7lnBpUceAJ_1x2q2Bq8MBe7IAIbQpQBRnZvC4h5So5aXQOcuuzAEC_XOEr7Bmq-dHXdSyYM4VmG9bmRMROPkufhDukRj02q6IstEB5WERcZtn_iJ2WUzYlLxWNRqOnrAHxL8IVi40wKHLZ4ZhW_6GhpOL4RoRtiNM1J2IqQpiPSbEMx5FfE9nFOvUWcqos4GzRbRmk4TqnKRVRU5zNsvKTC1nKN8RsNeBWh0uyGHjCe8a0E8QTQd52kT9CBGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
🇮🇷
مصاحبه عراقچی با جواد موگویی؛
جواد موگویی: دست فرمان شما دوباره باعث جنگ شد.
عراقچی: دست فرمان من نبود.
عراقچی:اگه ده روز زودتر آتش‌بس رو انجام میدادیم لاریجانی رو داشتیم خطیب رو داشتیم عسلویه رو داشتیم فولاد مبارکه رو داشتیم.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68525" target="_blank">📅 12:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68524">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4be1f5800.mp4?token=ZpVAX_JYctCJEkT-r9QePZppSI18f-znEsy5wl__jRa9U0PPul4Nu-SGvhHyv5AP_UH5nLuhEXA9pRlQntBzFXEA2mbcBPL2eloxQ3Cei5UANJynj_XYrN6VHbpLQ8ymIh-3CFTJkNw2QglYxq_LnMctvL40Xniv2z_5ucvNwr6maU3kE9B4Odrmg8NZcioR82cqEH6oNTlY6kvZFQZd3NPV7RShG5azbvQ1s70XVPPWvpff334_lAnjK95h-j3wtep-O7KxMJ9YSEGP-uc9AF3KnWxiOruSdcCeNvSdRHcRD7HaaLNxCEuplPCYbkg2Uh20_Uft7iRm_GfoNbS67Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4be1f5800.mp4?token=ZpVAX_JYctCJEkT-r9QePZppSI18f-znEsy5wl__jRa9U0PPul4Nu-SGvhHyv5AP_UH5nLuhEXA9pRlQntBzFXEA2mbcBPL2eloxQ3Cei5UANJynj_XYrN6VHbpLQ8ymIh-3CFTJkNw2QglYxq_LnMctvL40Xniv2z_5ucvNwr6maU3kE9B4Odrmg8NZcioR82cqEH6oNTlY6kvZFQZd3NPV7RShG5azbvQ1s70XVPPWvpff334_lAnjK95h-j3wtep-O7KxMJ9YSEGP-uc9AF3KnWxiOruSdcCeNvSdRHcRD7HaaLNxCEuplPCYbkg2Uh20_Uft7iRm_GfoNbS67Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فعال شدن سامانه‌های پدافندی بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68524" target="_blank">📅 12:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68523">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🇮🇷
فعال شدن آژیر خطر در بحرین در پی حمله موشکی و پهبادی سپاه پاسداران
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68523" target="_blank">📅 11:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68522">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fkqWo86zgPhWm46RprttiFsAnfb-WluEQQeZuGhTOOsC7E5z3IsDCHOE-3qPj1QLnuhrWhUhaJPhykQnsa_unOULjEhPVSP8iMOAklHB1twW332MMgkw7edAeuINXk36FiOphSMYkxl_lkp9uvMMSj09_bOygqdbxqksNlth8MVeLfW7jWAyaPJaCgI2091DJVP3Tfv6Qnhy3Sm4D1867_ymPsKbcrUfEpGFRK9vk2G2x6yqs7J-l6dEZKchqUW38ATQ0_tlBo9Wij4PFXefbD8EQGyfUZIYzcjl6bUbnkCHfNBr18v5T60rvPPymmV6MwyitpfGXR3BI16l7CJsoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">14 زندانی تو زندان دستگرد اصفهان برای اجرای حکم اعدام به سلول انفرادی منتقل شدن؛
این 12 نفر از متهمای
پرونده میدان علیخانی
هستن.
+پرونده میدان علیخانی مربوط به
اعتراضات 18 دی 1404 تو اصفهانه؛ اون روز بین معترضا و نیروهای حکومتی درگیری شد و جمهوری اسلامی مدعی شد؛ چهار نفر از نیروهای بسیج و فراجا تو اون درگیری‌ها کشته شدن.
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68522" target="_blank">📅 11:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68521">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ef80c8768.mp4?token=AsjhMFu-IlvppITciFPTuZw5Kp1lwYag5b3hyvT1MbgzxMxlsWOaUIHMhxAkKTi0GaB_UTe3jFpZba4pN89vcdjjcl4dLZQgJoB1Uay8ItpN0elovcW4ymB2zASBlaUxvovh7RetOXAHzS0Q5zzOqRCy3k1esHa7dXC9bpoCmMYptupKhxNBAhpIcowHrE1ATq_CL9sPbPwor2LTTLQ64HdiIIQ_wr25IxqosOboPzZd9kHqraj8tI0HLSKCN0z_e6u0aVXpw57gFS8v2FPhuBxBEnxrMFrG3oN8H275J2rgMBWG4MXvwwTQYEnamkMTMbuBn5Hs4kLUoKX94Wzphg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ef80c8768.mp4?token=AsjhMFu-IlvppITciFPTuZw5Kp1lwYag5b3hyvT1MbgzxMxlsWOaUIHMhxAkKTi0GaB_UTe3jFpZba4pN89vcdjjcl4dLZQgJoB1Uay8ItpN0elovcW4ymB2zASBlaUxvovh7RetOXAHzS0Q5zzOqRCy3k1esHa7dXC9bpoCmMYptupKhxNBAhpIcowHrE1ATq_CL9sPbPwor2LTTLQ64HdiIIQ_wr25IxqosOboPzZd9kHqraj8tI0HLSKCN0z_e6u0aVXpw57gFS8v2FPhuBxBEnxrMFrG3oN8H275J2rgMBWG4MXvwwTQYEnamkMTMbuBn5Hs4kLUoKX94Wzphg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سنتکام:
در هشتمین شب متوالی حملات ایالات متحده، نیروهای CENTCOM با موفقیت به تأسیسات نظارت ساحلی و پدافند هوایی نظامی در ایران، قابلیت‌های دریایی و انبارهای موشک و پهپاد حمله کردند تا به تضعیف قابلیت‌های نظامی در ایران ادامه دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68521" target="_blank">📅 10:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68520">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">‼️
جدیدا تو جشن های تعیین جنسیت دیگه خبری از ترکوندن بادکنک نیست
الان پدر بچه رو میکنن تو منجنیق پرتش میکنن تو بادکنک و آب
😳
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68520" target="_blank">📅 10:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68519">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be0c1d5cc2.mp4?token=apzC3NspFAG7Th8nqSdM5dIvlQR7OLpIEFnPJ4clxkmLR-_ODOd5alxOhvkBZe2wLxliyhKdAHnYF20MbRjjs829TIkJbA_VNUhexgIxxr9A8hI_MjWnTzFPDYxpTonAReB4ERVHz2QN9MYz3FLVFId_udK7FLu-AnTSAiGgMbxtg4sQ1uiIqGcjuGmLxrYgc7eeXmews_O3t82jMv2Muhx5iBp3giU9uwbEBdOVg9bcYyK3tz7PJ0rMiYA-xu7iQ-f2QOABY2FWIH1ICHrcbVk-nw37olpQSMBxBz51PXOtNEvNxmDVw9Mf7xPnK31b9L8u_4GvBdTLD-j79P_y_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be0c1d5cc2.mp4?token=apzC3NspFAG7Th8nqSdM5dIvlQR7OLpIEFnPJ4clxkmLR-_ODOd5alxOhvkBZe2wLxliyhKdAHnYF20MbRjjs829TIkJbA_VNUhexgIxxr9A8hI_MjWnTzFPDYxpTonAReB4ERVHz2QN9MYz3FLVFId_udK7FLu-AnTSAiGgMbxtg4sQ1uiIqGcjuGmLxrYgc7eeXmews_O3t82jMv2Muhx5iBp3giU9uwbEBdOVg9bcYyK3tz7PJ0rMiYA-xu7iQ-f2QOABY2FWIH1ICHrcbVk-nw37olpQSMBxBz51PXOtNEvNxmDVw9Mf7xPnK31b9L8u_4GvBdTLD-j79P_y_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇱🇧
پس از ترور خامنه‌ای، یک گروه از حزب‌الله تلاش کرد تا پسر نخست‌وزیر اسرائیل، بنیامین نتانیاهو، به نام یایر نتانیاهو، را در خانه‌اش در میامی ترور کند.
⏺
سازمان امنیت اسرائیل، شین‌بت، این توطئه را در آخرین لحظه خنثی کرد، زمانی که این گروه از حزب‌الله به طبقه زیر آپارتمان او رسیده بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/68519" target="_blank">📅 09:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68518">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🧾
امکان ویرایش شرط ثبت شده
💥
برداشت سریع با کد پریمیوم ووچر
💵
شرط بندی بدون محدودیت، بردهای نامحدود
🎁
25% پیشبینی رایگان برای واریزی‌های یوتوپیا
🎁
با واریز کریپتو، سقف برداشت خود را به سطح جدیدی ببرید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/68518" target="_blank">📅 03:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68517">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4918cf32ee.mp4?token=C4_RwEuziP7AbpGCN8Pv8MwqB0zmnMQY2DIFxKlxPkJ3sy8uejYXiWUjV_qXOgKqoA83DdRmR_3KekSdjHjulf3RymwMNTCbVPW3iPUBuAW9UaS6BvRbBYgydSVFkSSthjwuCpnKB5dtBrZW97Mo5gnGiFDNYl5OfbGimHbnD6P1ceQYUEJBEsjsrVnI7pf0XYLHYdvl4cddQuHW3DvcnCMgwnIJSVT04sqxik7DC01hoAzGBe-f7EoWA3z5gkuDRxQzq6tCPnFWApyjDV22fa2miA0oLD_ZrcSIEAupV0AnUXcTBYtnM16u9nRLuU1s0bGYGh-PIwBnA4XeP44wIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4918cf32ee.mp4?token=C4_RwEuziP7AbpGCN8Pv8MwqB0zmnMQY2DIFxKlxPkJ3sy8uejYXiWUjV_qXOgKqoA83DdRmR_3KekSdjHjulf3RymwMNTCbVPW3iPUBuAW9UaS6BvRbBYgydSVFkSSthjwuCpnKB5dtBrZW97Mo5gnGiFDNYl5OfbGimHbnD6P1ceQYUEJBEsjsrVnI7pf0XYLHYdvl4cddQuHW3DvcnCMgwnIJSVT04sqxik7DC01hoAzGBe-f7EoWA3z5gkuDRxQzq6tCPnFWApyjDV22fa2miA0oLD_ZrcSIEAupV0AnUXcTBYtnM16u9nRLuU1s0bGYGh-PIwBnA4XeP44wIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام‌ جهانی 2026
⚽️
فرانسه
🇫🇷
-
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
⏰
شروع بازی ساعت 00:30
✔️
امکان ثبت پیشبینی با مبلغ نامحدود
🫰
محاسبه نرخ دلار با قیمت 2.000.000 ریال
⭐️
فرصت استثناییی چالش‌های پیشبینی فوتبالی سایت یک توتو، با جایزه 500 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/68517" target="_blank">📅 03:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68515">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TOzAiXithntPMSv3423G2z3ebyq5JWmPd9mRYYvgiZFe7sG-kHQs1ZWE3vaE9lVYsQZg1cN1rGoNCF1xN_lx42APz56Wa_fR4t8NqrnLMqYtPkLdXyPoygImesGwiG7KYwcoEpkE87r-XD5l7JBqof34OkqhNoPZ4NR02tFowjymVOe9UfnwCpNxjtw2w66P8AX_v1F9YTTLqplTi6KigJq_PYRffPvFBkNryuW73wJKYaAFAo5cGQt7P6nT3KwxNUnb3rrHyZgXahg2rZqbGujKuajW0EPZz9qLvI3KggUp7xqIgFuZu4gaN2uW3K0X2IYPJqBgZaCO4daTtDSLUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tsc9EQUf9o0qAMPgWrcov-J9H5gN-_-z-7hDt5jat4B4tTr8NX4VVdt7GNizYB5bGo7JExpCB75ZHztp9iF4maMhRff-nP8W2dzV5IDBTISuLCPBaTk0b1CqilAHol-304rTDBqCEgOvpXngW5c7XGLBQExYDrCE8cOAbAjye7zQhda0Qe6KwX0DeeSv-mQSYAPCimjioXkhtA1ti1moi25-hJcykfQDIKNFQnHhUBGW9hX-qcw4o3DLj7JNNgJ7AM11e8zGz_xiR0hqx2hrKnry8-j9hNbiIG2_gxMs0mDP_TEDB99qjoDrNptSDbiABMZWjOpAP95gAYy8MY_PKw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">❌
حملات موشکی روسیه به کیف اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68515" target="_blank">📅 03:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68514">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🏆
رده‌بندی جام‌جهانی فوتبال|انگلیس برنده جدال بازندگان در یک رالی تماشایی گلزنی؛ دشان و تیمش در روز رکوردشکنی امباپه و اولیسه با مقام چهارم با جام ۲۶‌ام وداع کردند
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
😃
-
😀
فرانسه
🇫🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/68514" target="_blank">📅 02:37 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68513">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
تسنیم:
حملات نظامی دشمن آمریکایی به حوالی حاجی آباد.
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68513" target="_blank">📅 02:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68512">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
بهبهان صدای انفجار
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/68512" target="_blank">📅 02:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68511">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
دو انفجار در بندر‌لنگه
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/68511" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68510">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
صدای جنگنده در آسمان کیش
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/68510" target="_blank">📅 02:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68509">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d71f9fb5e.mp4?token=ZS5vHU0gmJdMbRuqfFxMKm8Seodh-LkjMU9dWmR9G26Dd92zJP9J2gz4AqYJ9dBvCZ2MrAs_lq2lR9fv5H6EWzKzKZojggHgvDHzQvPth7C-QewXbM05UWCwT6H1qFbDUHX4YomWC1iDAZ8QOGKkwfMhi24_LVBaCayuMp9EuVmX4wUlmug38vygfQdeBmRoiIVITV-TC4C8ehZzjkO0MkqzD4JwhwZYXcWHy2qxSW5rYtwYJj62u9233lDYpZw96dsGOqEwJxQzTT8Bqzv6rChxcx0f4fHqKcUD6VYa3yFdXddh4_m0tYKXBdesDDCac2SVMO31DmRF-lPjtHyn4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d71f9fb5e.mp4?token=ZS5vHU0gmJdMbRuqfFxMKm8Seodh-LkjMU9dWmR9G26Dd92zJP9J2gz4AqYJ9dBvCZ2MrAs_lq2lR9fv5H6EWzKzKZojggHgvDHzQvPth7C-QewXbM05UWCwT6H1qFbDUHX4YomWC1iDAZ8QOGKkwfMhi24_LVBaCayuMp9EuVmX4wUlmug38vygfQdeBmRoiIVITV-TC4C8ehZzjkO0MkqzD4JwhwZYXcWHy2qxSW5rYtwYJj62u9233lDYpZw96dsGOqEwJxQzTT8Bqzv6rChxcx0f4fHqKcUD6VYa3yFdXddh4_m0tYKXBdesDDCac2SVMO31DmRF-lPjtHyn4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
اربیل عراق
@News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/68509" target="_blank">📅 02:08 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68508">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
گزارش های اولیه از انفجار در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68508" target="_blank">📅 01:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68507">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UyZccLO5OkMlCPXR4AH96_EW-2Nci4nw0p1lTTXq-c9ta7M0YCQJEitdw9ZgbvDiU1uj2Uue1Cay4q59wJ0eY03lyFfpt01DRjo5oqX_wXQaxkllyBrGE8ugQ15hY4zpJcArhq-oKmZcd1YC7woKLSNGw-c1RHPcsZzo77XFtx2dysnOTtHDvbRVhDVHxX8ko6nXASunfUAQBLmfoda9yJuV2LL7Pf9T3xhV4FrsUrBIJOfCne6RjJH90Sc1e5EjIA9exL9KeJbAhsLz9SaCkrECD0MP0o7-k1tpXf1uySBqzbHr1p-1eltK-K2A2Xmm_isTUjxo0RiM26sm5T_KIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
امروز ساعت ۶ عصر به وقت شرقی، نیروهای ایالات متحده به دستور فرمانده کل قوا، حملات هوایی جدیدی را علیه ایران آغاز کردند. هدف از این حملات، تضعیف هرچه بیشتر توانایی ایران در تهدید کشتیرانی تجاری در تنگه هرمز و تنبیه فوری نیروهای سپاه پاسداران انقلاب اسلامی است که شب گذشته به نظامیان آمریکایی در اردن حمله کرده بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/68507" target="_blank">📅 01:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68506">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
🚨
#فوری
؛سنتکام اعلام کرد دور جدیدی از حملات آمریکا به ایران آغاز شد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68506" target="_blank">📅 01:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68505">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lm9llfHlOia3Hzh2XeNhHNa8_JxSZUmcIU_sP5iPn1FcWTnyHNB5mByMQj8JNKL8my83wLFg5U1NdBCzzD9WU6-oCaI0gIYiSM3KjJUvOomXH3x9eLbBNxq8_4rnNp-qOSHDlmMCerLLQ0x7d1Dq3QnkgVR_acHCj4vvG7kls_P_Sx4No_44Ref_OmQhTt2s5Ny4e74YgSrQTch5H3L6-rs3pGZ0JYCjC6ZAqUxbsBUSsbJYrDVrZWb_qdKqSuiT8w4whyriu8QQvO0ivGEqkKX72EPayqUIK3HGyIne-ieLJ68hUQdIPfvh7W_682dNL5ONBj-hbqxIjhrtu_3fgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
حداقل پل صراطو نزن بتونیم رد شیم.
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/68505" target="_blank">📅 01:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68503">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/juBlnoteGskpMyquZyD5ZF60--MjqE5cw1_ZEO79LfRbyaZs-5kNauiQ6RaIOpbi4DHSdmECfcH1ntgPeDST9ShqFCQwntKk30kqmG5klmm9zjyYCXO0tl6FH1EYeftnt3lB4Z539CdT2Cyzm2FYTJgVRdaZWECNBRUyYeNjDRWGlQibMebi0ymP3E3r0XplOp1NLmbWI0H_qprqqbS1nVi13HZ_bLMLskYjJmq50To-Lvu4K5PDtr7g3e91e39Q4mgDel_ahtSXAmDcDTI1e5Dx9LAlu-52hTNjIYdDtew4hyBkhrIYJ0r0Xs8JUl-WXq3j-QqVJKOlIvcCax631Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AH3fDDa_YGwBnwuAWExoeuCRsH67mgtOm5SyEWgt6_AaYrCHT3vNOMaDb4DVXAUjQ_6We0GGDm0r-gy_iMuxOXRnsR0C50VFNTh956BuGOKQuiLVFBnLE7q1FPvR8qpYpZrK1TCnw0IQnZCBJkrMukOKSvXi-I75EuiKWeBUdLa5xvDlZeZT5LTaQDRVDtCv6-4hy7-jYeEXaq1sBEbBA2aNadABXpbeJFHAn3AiJbhOwm1Hn_pfCVIK3dcp-UAYHnhu5gcQxpw3HHiAnejXqOxQsTbYK0ZBCRagiitHejBbtPJ7xaIywd0BaXaIXItgIdGhqS2sHLDiMRHAAGBewQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
امارات خواستار توقف فوری تشدید تنش‌های منطقه‌ای، بازگشت به مذاکرات، حفاظت از کشتیرانی در تنگه هرمز و پایان دادن به حملات علیه زیرساخت‌های غیرنظامی است
🤟
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68503" target="_blank">📅 01:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68502">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">خبرنگار: ایران اعلام کرده دیگه به تفاهم پایبند نیست نظرت چیه؟
ترامپ: خب بتخمم
#hjAly‌</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68502" target="_blank">📅 01:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68501">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
دو فروند هواپیمای تانکر متعلق به نیروی هوایی ایالات متحده آمریکا از پایگاه هوایی العديد در قطر تخلیه و به سمت اسرائیل منتقل شدند، به این دلیل که از احتمال هدف قرار گرفتن آنها توسط ایران نگران بودند.  @News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68501" target="_blank">📅 01:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68499">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZyKbPIwTQg8Hql7oqtBkJtaoElTDG34JzAVf-3vym1MtVFw4NrJzuuEKRqmEQhYgzmMcHT4N133LhzAqL_tLWqfBOqQifzm8Gufv-uVzrVAmJT21IC9nlp8DLJ3iR9-SeJbVuZc7FEd8BPg5T2gLpTvjlU9A8SoMrZtRrf5VxmJbt-6ySjBbQNerSNcVdshsO-3FkNtk5U6JV2FFesY_YUzsYcf-g-W-xoXW_MzbTps1hVm3zSBHMjLD27RteIcIgDsZVznWZwZa75Ds1pzJU7E7ZAEKugt_hGIykfW8POgT5MrS6v-iGZkLKxEhjNzS2HMBIIF1HE5cLDg4u5Eg6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h367x-X-9o-FPxy99WODS9sgpQuy2Wtjyt3HmGR-at2F2pZMdH0FPgP-u8cuA7X6ogjH4VZyqKWY-r34EuNv3lC9HUXbUH4EhedDEq1e7eroJ8PR-j6EDEJnINX9KZLYWIvc4tk369OYiKQxT0i_OkAGrzz_dH422r5eqrBwK8VAFlujvyDpZCt0sa1rq4zrqidEh5762FbV7hkLsUnjBl0YcX6itWv2hIhzPECBsjpzMpDkMYrpUyC8nZPzZ8uh_8_vaR-jN--DOJUjSXQArTCdr8MogTkkLhSaEXTPnmvmHf17nMYW179Kp0uNo2J8Kt7R4mYv7uJxWLUBh_Y25A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
دو فروند هواپیمای تانکر متعلق به نیروی هوایی ایالات متحده آمریکا از پایگاه هوایی العديد در قطر تخلیه و به سمت اسرائیل منتقل شدند، به این دلیل که از احتمال هدف قرار گرفتن آنها توسط ایران نگران بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68499" target="_blank">📅 01:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68498">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CMAMMdtFtwduiLB_O3Gbs3sIsXpKcVIDVsPyMS8Oe98oYh516i-hW1RTMKWNxKDk57so7HoDzrlOe8JUQ5DlkYLL9N_S22hqw32eotYLJgiF4Sn799uEff_bbI5bnrmivOHPJipUSIL52FG5sUEfrZezA3MJmD8BJE8_gbB-YQaJ8iO_1Rm1MO14aOtKUIEhSUC46rVAeKlUgXy3qE1ROpkB9gNsWAur3zF6sHqvjW7OrGRO7Utwu60m-gnJMLZgdEbIJHZf_wOxRzSp0sFuMlWW4Otm2tpEJzygZ5GCun0g5atrp5jwod_GtAljSXKgsC7C3X6XzdISmBu1-VwEZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
دونالد ترامپ، رئیس‌جمهور آمریکا به «نیوزنیشن»، در واکنش به کشته شدن دو نیروی نظامی این کشور در حملات ایران در اردن:
«بسیار غم‌انگیز است؛ اتفاقی بسیار تأسف‌بار است. ما از وقوع چنین چیزی بیزاریم. آن‌ها در راه خدمت به کشورمان جان باختند.»
او بار دیگر تأکید کرد: «ما هرگز به ایران اجازه نخواهیم داد که به سلاح هسته‌ای دست یابد.»
ترامپ همچنین اظهار داشت که برایش «اصلاً اهمیتی ندارد» که ایران اعلام کرده دیگر به تفاهم‌نامه (MoU) پایبند نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68498" target="_blank">📅 01:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68497">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B4tJMtcc2u32CnNzUHGrKNQsl73_f9iKNpA3epguxtXNBbH9CAosbNAto-dsyt50e3YllZAWTO3nRZizK4riuXdasPksjTckcxJyZuMHxX72Ypx8S5RgfnAjydgbDw60K9oS55vWimb6CHEhaPaIRd3sCOkyX4TSYb433Nmk2YF4rqbli_bmcXUyOMDwMvOkUGoSsp410tNpgHZ8dUWYSwF_m3CxKFqEZrc7N1zmf1v_JOYFTQqTJKdE-SBBoYItC7l9l2BCZj6EedTTrnw1cfvjmImU2-8Uu7XL7c0uEJHmiz76NKQpaDA_PaaLsvA8ngJnde4OhquT12XAj8a6vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
شبکه المیادین گزارش داد که در پی حملات ایران در خاورمیانه طی هفته گذشته، ۳۰ سرباز آمریکایی مجروح شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68497" target="_blank">📅 00:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68496">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
بندرعباس زلزله!  @News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68496" target="_blank">📅 00:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68495">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
بندرعباس زلزله
!
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68495" target="_blank">📅 00:43 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68494">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mZJIi8HUIz8jTQqV-UqEpy_9PmJ61ZG7jIpJGZdcDMkCx8DzvuhKyucOw4QC6ROeBhPmk8fC2ij-1p-lKaP3V-zFfylBXLx9GoiRgiK5Zp9JntTwYFkKASrk9kM84pZuXPjdPbdArEwjjc4sXsgMh1fXELYAkuIH11bHfPHpTGQ7YM6y0Qhso1OaXZY_YSIs7C-TjZIIlrOZqgWHw6adeG_wNaqN6Df2GyvHNkrAQ81DnnBH6eekUHGDtmJ2Qp_D6v6P082s6yZdycQJqRTuSgUmexIMOcSE8e_AsmWa6uu0AWubt_ZBR3eONcYkEMKr-xAaYzP4yOuS_17VkW9AgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نیویورک تایمز: ایران در طول پنج روز، چهار حمله علیه نیروهای آمریکایی در اردن انجام داده است.
اولین حمله، یک مرکز مسکونی در پایگاه هوایی شاه فیصل را هدف قرار داد و تا پنج سرباز آمریکایی را مجروح کرد.
دومین حمله، یک پایگاه شرقی در اردن که توسط بالگردهای بلک هاوک آمریکایی استفاده می‌شد، را هدف قرار داد و به چندین فروند هواپیما خسارت وارد کرد.
دو روز بعد، موشک‌های ایرانی به پایگاه هوایی موافق سالتی در ازرق اصابت کردند و حدود ۲۰ سرباز آمریکایی که در پناهگاه‌ها پناه گرفته بودند، مجروح شدند.
یک حمله دیگر در روز جمعه به پایگاه هوایی موافق سالتی انجام شد که در نتیجه دو سرباز آمریکایی کشته شدند، یک نفر مفقود شد و چهار نفر دیگر مجروح شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68494" target="_blank">📅 00:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68492">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V74gzExxZ4_95T4rULV1ZMidubPFhK4mwSF77u687f9AlWyDsZApHx2K3It_F_FNk2NBYLjqeUPHeL2pvKVbJk1dDvmmXqeXy-mfVccbhPYek5OjTLl8I3iEPGSB7mUD7qq-mYRycPdzAqj2LDOSNydrCJgNZw_TkSJTJRdYX57kfBO3HBt38j5Lnww9AoxO8XDy7p0MvwZIyPR3vPaIikMfANIo_wDs04Df93fz1aXLI_CwONU5e8VuN-zkKogm5svndAAe19G7hgoPiyTO1FYyaHWNaTE7m-L2oypo0--Y337w252id5w35CdIJ4QWP5IfaZykrI8AratONPnlRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیومدن؟
#hjAly‌</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68492" target="_blank">📅 00:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68490">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JeCfnXP9YjOIeFEgjVhT7Fl6FnY6XYpQt8eKP1XvbOsdXUjaPiuHnSVfmazDBKoD-BhM1-d4TYop02hGq1VFj926pb23pYOHvg35XzFseFBN6_W-Kj6mkf8l1Dmkbp9ltzU7m6IAv54XooaWdZU27jIOspddaj22Y859Gk42vXLpdqlLmOlNUP1F3e-HXIDDO7ZNBAy94VAGFjnxTnUlDvY7na3bOZsTiVruVkz8DThjT7TnL2BP4bkmgwO72le2xqaKbz4SVpX2_egOj93AQiegSuMi_ogi4torzK2Cav13rbJ9lm_MSxF-CauxZVg5QjXtHTQIl1lw_FiZhvqYmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kB4M59A8EUa7GalShoZQIqPcU8MEOxJ0NJb_eLl8SEMn3QAJLg6_eg4P3GMScpwHzxm4mKXVtnxpjxHWbBIHAcWl18wYgE0W6tUUH_URZs0bw-Qm6tGfHwgYIjtZFZY6btOTO2vhlz1aNWJq2exBz1PljEWKb3VA5YkM0c4zAhsAPgSppEnGtg9IUYesaEel9XU-RNv0k6ziqjjYbIAh9N1aS-tGFBoV4mH6rMf1lVpZO7bB01mSywsdIB7EldWT3J6f5PyCngCwlL-9_INh37xyKvvqNdgRX6gUdW0OAZ-QU2vJMgl120IThhVwXgch-KqfALndyPVN--vCB6KySg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نیلی افشار دوست‌دختر سابق تتلو و پویان مختاری هم این وسط تصمیم گرفته پورن استار شه و یک کانال زده تلگرام که ورودیش 2500 استارز یعنی معادل 8 میلیون تومن پول می‌خواد، البته محتویات کانالش لو رفتن و کافیه کلیک کنید رو لینک های مدنظر پایین :)))
🔞
🔗
مشاهده ویدیو‌مسیج های لو‌رفته
(Part1)
🔞
🔗
مشاهده ویدیو‌مسیج های لو‌رفته
(Part2)
🔞
🔗
مشاهده ویدیو های لو‌رفته
(Part1)
🔞
🔗
مشاهده ویدیو های لو‌رفته
(Part2)
🔞
🔗
مشاهده تصاویر لو‌رفته
(Part1)
🔞
🔗
مشاهده تصاویر لو‌رفته
(Part)
🔥
🔗
مشاهده تصاویر لو رفته جدید
(Part1)
🔥
🔗
مشاهده تصاویر لو رفته جدید
(Part2)
🔥
🔗
مشاهده ویدیو های لو رفته جدید
(Part3)
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68490" target="_blank">📅 00:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68489">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">اماراتی های کاکولدزاده خواستار پایان درگیری ها شدند
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68489" target="_blank">📅 23:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68487">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3b7aa9105.mp4?token=AWv6eu-S9YhTGc9nMq7f-DWKhoVnovnUPUATKJ6ksURGSwJx8faMqyNv6FqRTd6byY6wMRKSA1k26dcnuXxhYf2R8VPWG-A0CaGAX6-PNQo9QyPE_Pnsa8Oc6L3dCHaz226o4kNsa_BIj8S8DOrp9WdpomgHtX1NPm-8XoYBC3CwbSeovEcPwitINuqCFTZchbn2wZCssgRfBV-3VKATLUcMN6Nnmn9b2zn9Hn5d91LdJzvKZwhWpI_AxNKb2copBv3UGHgdE8jkTG3TjfTK-Ae8ckCao79MW3N5eqXrrfHnDw6TtWs-gjtFKJIjItxYMJ2kAlCcXTPbmNQi5lP8kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3b7aa9105.mp4?token=AWv6eu-S9YhTGc9nMq7f-DWKhoVnovnUPUATKJ6ksURGSwJx8faMqyNv6FqRTd6byY6wMRKSA1k26dcnuXxhYf2R8VPWG-A0CaGAX6-PNQo9QyPE_Pnsa8Oc6L3dCHaz226o4kNsa_BIj8S8DOrp9WdpomgHtX1NPm-8XoYBC3CwbSeovEcPwitINuqCFTZchbn2wZCssgRfBV-3VKATLUcMN6Nnmn9b2zn9Hn5d91LdJzvKZwhWpI_AxNKb2copBv3UGHgdE8jkTG3TjfTK-Ae8ckCao79MW3N5eqXrrfHnDw6TtWs-gjtFKJIjItxYMJ2kAlCcXTPbmNQi5lP8kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ایونت ورزشی، ۲۶ تیر؛
پارک پردیسان پونک
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/68487" target="_blank">📅 23:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68486">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
🚨
یک مقام آمریکایی به شبکه NPR گفت:
«رئیس‌جمهور ترامپ دستور داده است که فرماندهی مرکزی نیروهای آمریکایی (سنتکام) در ساعات آینده، «دروازه‌های جهنم» را به روی ایران باز کند.»
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/68486" target="_blank">📅 23:33 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68485">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51feb96ae6.mp4?token=aM44CdhgQpmitNnfHw5DPTKUxDGQOswF9-6KGze4hv3yoAr6Eh5M0LAAc9oYF_93gGdmxMIANBtyFiKkIvhYXD8LFeM5t9W7f0bQqZeBspp7fwHfW7hKsUJCt3nfsEyiKqYyNmfDJ_3_ZHdj0bvzOOJnw5zhrJ1lk8iZPuXOHBbC-EwmQLAb_jXwM4VHDLMYiYOVE76RJM1NGBxDIHZb8JV9nj-d2kXAPKQBHYi4GPllb_v5q8L9VlKsfW7XMz29e4gY603uqhyqzMOUikGJWfZ7BRs23hVJ9d2EsGs-Fzx70x3grCaMJzNi6-ILQ6SIrooDLGiP12rbHt0JYjQVng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51feb96ae6.mp4?token=aM44CdhgQpmitNnfHw5DPTKUxDGQOswF9-6KGze4hv3yoAr6Eh5M0LAAc9oYF_93gGdmxMIANBtyFiKkIvhYXD8LFeM5t9W7f0bQqZeBspp7fwHfW7hKsUJCt3nfsEyiKqYyNmfDJ_3_ZHdj0bvzOOJnw5zhrJ1lk8iZPuXOHBbC-EwmQLAb_jXwM4VHDLMYiYOVE76RJM1NGBxDIHZb8JV9nj-d2kXAPKQBHYi4GPllb_v5q8L9VlKsfW7XMz29e4gY603uqhyqzMOUikGJWfZ7BRs23hVJ9d2EsGs-Fzx70x3grCaMJzNi6-ILQ6SIrooDLGiP12rbHt0JYjQVng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای که دن اسکاویینو، از مقامات ارشد تیم ترامپ در پلتفرم ایکس منتشر کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/68485" target="_blank">📅 22:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68484">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
🚨
سه انفجار در بندرعباس  @News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/68484" target="_blank">📅 22:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68483">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇮🇱
نتانیاهو شیرِ یهود برای آرژانتین در فینال جام جهانی در مقابل چپول های اسپانیایی آرزوی موفقیت کرد
@News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/68483" target="_blank">📅 22:39 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68482">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🚨
سه انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/68482" target="_blank">📅 22:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68481">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🇺🇸
#فوری
؛ پیت هگست: خدا نگهدار قهرمانان؛ فداکاری آنها فقط عزم ما را راسخ‌تر می‌کند
@News_Hut</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/news_hut/68481" target="_blank">📅 22:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68480">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝖄𝖚𝖘𝖊𝖋</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27909ab46b.mp4?token=tNhHr2qKQhTOPyD0kqkrSfbDCrUzhDPMX8obMWq02xB3CTUFKN-Kp3E6Oo5RBBBYE94Fdcxh697G893ImT_4BnqR6OshDNUJ6IDk9d0HIk-DKUNLYp5hly9j07XnnmSdefO3gpOtqAev2Xekquk6JJOCGfpYt7M2YnE5yX3dyrsU8EUrms3RsB5dL-rU0qwEO5Cub30gB246rIJrFLm3tFooD2oM070-ufrgT_tYo-KfMTBpzan8mI3kOfbHZq-gQ8aFgWWLQzDYevNod1wVIrfEa9Yn95148rYk6wT7Ohxt3AX4grF9Qp6wtC8bP3itvfphK5ToOu5tu1MBHkziYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27909ab46b.mp4?token=tNhHr2qKQhTOPyD0kqkrSfbDCrUzhDPMX8obMWq02xB3CTUFKN-Kp3E6Oo5RBBBYE94Fdcxh697G893ImT_4BnqR6OshDNUJ6IDk9d0HIk-DKUNLYp5hly9j07XnnmSdefO3gpOtqAev2Xekquk6JJOCGfpYt7M2YnE5yX3dyrsU8EUrms3RsB5dL-rU0qwEO5Cub30gB246rIJrFLm3tFooD2oM070-ufrgT_tYo-KfMTBpzan8mI3kOfbHZq-gQ8aFgWWLQzDYevNod1wVIrfEa9Yn95148rYk6wT7Ohxt3AX4grF9Qp6wtC8bP3itvfphK5ToOu5tu1MBHkziYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش پیت هگست به کشته شدن ۲ تن از سربازان امریکایی</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/news_hut/68480" target="_blank">📅 22:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68479">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f59058bcce.mp4?token=RjI2Z0BJWLTqeoYsF87wu87SNg_VTYzKODdXvRaOMnFkKv0VK4GmUhhEJ7yiPFgxnL5gkFRuRrs62MCjmPqUazu6htzY6hgqpMtVrFqIF46T2drPaqLFo7fuPZcFTemJsn98bQ4ozsJ7EZxYO179k5gPrq2sCjgrHRh5io0nppn0tkVLXhad3xBOpmPfflmAa9emGK6K6woXTalZRXmBCuT7BwL7RfQn7WlvIsRuDqh0cf9TWqfI0UOYNorE_jpGHU-HLPdfD-zhRZBexHqIQoLre7tvLzoPYpptutn-rXqYgKt_Zv_mQuQDIQxWW1-RkIW5E-3H7sSHOEAddwWWNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f59058bcce.mp4?token=RjI2Z0BJWLTqeoYsF87wu87SNg_VTYzKODdXvRaOMnFkKv0VK4GmUhhEJ7yiPFgxnL5gkFRuRrs62MCjmPqUazu6htzY6hgqpMtVrFqIF46T2drPaqLFo7fuPZcFTemJsn98bQ4ozsJ7EZxYO179k5gPrq2sCjgrHRh5io0nppn0tkVLXhad3xBOpmPfflmAa9emGK6K6woXTalZRXmBCuT7BwL7RfQn7WlvIsRuDqh0cf9TWqfI0UOYNorE_jpGHU-HLPdfD-zhRZBexHqIQoLre7tvLzoPYpptutn-rXqYgKt_Zv_mQuQDIQxWW1-RkIW5E-3H7sSHOEAddwWWNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
لحظه اصابت موشک‌های بالستیک به پایگاه موفق‌السلطی اردن که گویا منجر به کشته‌شدن دوسرباز آمریکایی و مفقود شدن چندتن دیگه شده.
@News_Hut</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/news_hut/68479" target="_blank">📅 22:06 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68478">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">پیش‌بینی می‌کنم که حملات امشب، از دیشب هم شدیدتر خواهد بود... #hjAly‌</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/68478" target="_blank">📅 21:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68477">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">همونطور که پیش‌بینی می‌شد، دامنه حملات امشب گسترده تر از شب های دیگه شده و حتی حملات به یزد هم کشیده شده #hjAly‌</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/68477" target="_blank">📅 21:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68476">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭𝐍𝐞𝐰𝐬➕]</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e4c6a7a84.mp4?token=HdX87JaMbqEAQtABc1QrTmiIWJ1kdiCZgrmspzLxeViH1z1Sm7DvtQjo5f8trd05ZIvzYqjOikGMB9wMHrNIv5qlMYFiMW4YMJIy0JDyTT3B29VbYEZJHFtlqByCzDmNAL1pV-UYgqyEHzmrR-GbmH6EVyyaIKfbZORD0vM5gWvRyK35kw6PqR0RiU0pqYAHyJPcBKEuTs8t-ioNULDjMzkXp4WlPcEicY0e8V6pgTzcMYAv8E-Tm0DB3_PVAw-7cd3OGUOe4BrQsEMAqa41yDAUDXK_AsZvZaKEw-drniEoVbilgmUSHIX4npMMe6YYorcouzjs6zr4q0rwN8tj5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e4c6a7a84.mp4?token=HdX87JaMbqEAQtABc1QrTmiIWJ1kdiCZgrmspzLxeViH1z1Sm7DvtQjo5f8trd05ZIvzYqjOikGMB9wMHrNIv5qlMYFiMW4YMJIy0JDyTT3B29VbYEZJHFtlqByCzDmNAL1pV-UYgqyEHzmrR-GbmH6EVyyaIKfbZORD0vM5gWvRyK35kw6PqR0RiU0pqYAHyJPcBKEuTs8t-ioNULDjMzkXp4WlPcEicY0e8V6pgTzcMYAv8E-Tm0DB3_PVAw-7cd3OGUOe4BrQsEMAqa41yDAUDXK_AsZvZaKEw-drniEoVbilgmUSHIX4npMMe6YYorcouzjs6zr4q0rwN8tj5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
‼️
یادی کنیم از این سکانس که ترامپ چند وقت پیش در تروث‌سوشال پست کرده بود: اگر یک آمریکایی را بکشید ما با پاسخ متناسب برنمی‌گردیم با فاجعه کامل برمی‌گردیم
این صحنه از قسمت «پاسخ متناسب» است. در داستان سریال، یک هواپیمای آمریکایی در مأموریتی پزشکی هدف قرار گرفته و شماری از آمریکایی‌ها، از جمله پزشک شخصی رئیس‌جمهور، کشته شده‌اند. در اتاق وضعیت کاخ سفید، فرماندهان ارتش گزینه‌هایی برای یک حمله محدود و «متناسب» ارائه می‌کنند؛ اما رئیس‌جمهور خیالی، جِد بارتلت، با خشم می‌پرسد فایده چنین پاسخی چیست؟ او می‌گوید اگر دشمن می‌داند آمریکا همیشه محدود و قابل‌پیش‌بینی پاسخ می‌دهد، پس این پاسخ دیگر بازدارنده نیست.
@HutNewsPlus</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68476" target="_blank">📅 21:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68475">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:  در تاریخ ۱۷ ژوئیه، دو تن از نیروهای نظامی ایالات متحده در اردن و در جریان عملیات دفاعی در برابر حملات موشک‌های بالستیک و پهپادهای ایران — که توسط فرماندهی مرکزی ایالات متحده (سنتکام) و نیروهای هم‌پیمان انجام شد — جان باختند.…</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68475" target="_blank">📅 21:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68474">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7N6aAozvyrATdwZX_lDWFyHDdrTjXEuyfcX3sJAw5fgw0tbp2-pIJlyh22QY1NVLcO5ZZJWdKPraIBuvlRlBlUK8sQYrRlK2sHSLZ9QfioolCsEG0-JJqU1PJVsj_y8qQMsP493gZLNQW4d1WqUAWnsqxwrFonYGlnZeQHcUPZHazJdWpOlOkpoWNeNn8oXJWcf_RM75vEsyjmHagLGvsNm51S6fJP6W-xO4LzcDUoxHz-eP2uJI5CgEVKeAtzMchoRn0OJnZUZd-VMXv1ekz2gc8xZsWJBy6AZcnALqfKHq8b1U457lu5JXhNhmaNqEX1Z0FyhMktZz3LVBzt6JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
در تاریخ ۱۷ ژوئیه، دو تن از نیروهای نظامی ایالات متحده در اردن و در جریان عملیات دفاعی در برابر حملات موشک‌های بالستیک و پهپادهای ایران — که توسط فرماندهی مرکزی ایالات متحده (سنتکام) و نیروهای هم‌پیمان انجام شد — جان باختند.
همچنین، یک نیروی نظامی دیگر در حال حاضر مفقود است.
چهار نیروی نظامی آمریکایی برای مداوا به بیمارستان‌های اردن منتقل شدند که همگی تاکنون مرخص شده‌اند.
سایر پرسنلی که به دلیل جراحات جزئی تحت معاینه قرار گرفته بودند، به محل خدمت خود بازگشته‌اند.
سنتکام به احترام خانواده‌ها، از انتشار اطلاعات تکمیلی — از جمله هویت نظامیان جان‌باخته — تا ۲۴ ساعت پس از اطلاع‌رسانی به بستگان درجه‌یک آن‌ها، خودداری خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/68474" target="_blank">📅 20:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68473">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7081b32d41.mp4?token=v1G1xsK8edHlu-WPqcd55osOpKhPaKmCvAmZgOXbBZj9Gf8eDx9vT-X6KnPkysXz673G-yc12VyXUq5uOQ9f8kw7LjcWmYe0fJWd4svVcvm04oqNQK2pzjkYeDrECFo0dvGUs8b-Yo2F8y_d2zEndkUfgU9tHYZq8BcPiJTt79rSOmlo2jafiQNUbMs_t5ZjvkmErX9S-pV062zfyj_Y5_RaApdJjCcKj8xGsUtaq1Su_agxsw0FyTcrWUCZ5tDPvlIfySLpg4X3rBFWrqWbY8QmrLYuUu9fE7VK219RPzJNC1ePIEaQ4XEQ9m5GZDLyosHIy5Geu4B-Q9CrfCKgFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7081b32d41.mp4?token=v1G1xsK8edHlu-WPqcd55osOpKhPaKmCvAmZgOXbBZj9Gf8eDx9vT-X6KnPkysXz673G-yc12VyXUq5uOQ9f8kw7LjcWmYe0fJWd4svVcvm04oqNQK2pzjkYeDrECFo0dvGUs8b-Yo2F8y_d2zEndkUfgU9tHYZq8BcPiJTt79rSOmlo2jafiQNUbMs_t5ZjvkmErX9S-pV062zfyj_Y5_RaApdJjCcKj8xGsUtaq1Su_agxsw0FyTcrWUCZ5tDPvlIfySLpg4X3rBFWrqWbY8QmrLYuUu9fE7VK219RPzJNC1ePIEaQ4XEQ9m5GZDLyosHIy5Geu4B-Q9CrfCKgFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
محسن رضایی:
اگه حملات آمریکا تا چند روز دیگه ادامه پیدا کنه، وارد مرحله تهاجمی کامل میشیم
اون موقع دیگه فقط جواب حمله رو نمیدیم و حملاتمون گسترده‌تر میشه همه جارو میزنیم
آمریکاس که ریده به مفاد تفاهم‌ نامه و همرو یکی‌یکی زیر پا گذاشته و عملا از تفاهم نامه فقط اسمش باقی موند
آمریکا از جنوب لبنان عقب‌ نشینی نکرد، توی تنگه هرمز مسیر غیرقانونی ایجاد کرد، به حاکمیت ایران احترام نذاشت، به سواحل ایران حمله کرد و اموال ایران رو هم آزاد نکرد
دیگه نه روی کاغذ و نه توی عمل چیزی به اسم تفاهم‌نامه اسلام‌آباد وجود نداره
اگه دوباره مذاکره‌ای شروع بشه، از طرف آمریکاست و اونه که دنبال نوشتن یه تفاهم‌نامه جدید با تغییرات تازه‌ست
اجازه نمیدیم نیروهای دژمن از تنگه هرمز رد شن و وارد خلیج فارس بشن، چون امنیت کشورمون به خطر میوفته
🌅
قبول نداریم آمریکا توی تنگه هرمز، که گلوگاه انرژی جهانه، نقش یا حضور داشته باشه
آمریکایی‌ ها منتظر موج موشک‌ ها و پهپادهای ایران باشن چون ما جواب حرف‌ های ترامپ رو توی میدون میدیم
فعلا سیاست ایران اینه که هر حمله موشکی رو با همون شدت جواب بده
انتقام خون فرمانده شهید و شهدای جنگ رو میگیریم
آمریکا میخواد با محاصره دریایی، مقاومت ایران رو بشکنه
ممکنه دوباره به سایت‌های هسته‌ای حمله کنه یا بعد از اقدام نظامی، ایران رو به مذاکره با شرایط جدید مجبور کنه
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68473" target="_blank">📅 20:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68472">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🧾
امکان ویرایش شرط ثبت شده
💥
برداشت سریع با کد پریمیوم ووچر
💵
شرط بندی بدون محدودیت، بردهای نامحدود
🎁
25% پیشبینی رایگان برای واریزی‌های یوتوپیا
🎁
با واریز کریپتو، سقف برداشت خود را به سطح جدیدی ببرید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68472" target="_blank">📅 20:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68471">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4918cf32ee.mp4?token=U_iAZibVXY8Q8bv7-djxVIMuZRBn0Yi3vUK12OUBYEDMfvZ_pZ1KzvFIkBdQZoqHMJ1y2sFYdrUxGGwd3yy9YyaJCQfXiTq54_CdjdvqFzzxS1kxsNeK1VjY0L8cDRls86fSw1TK7BvmHJr_ah1zHuGXU2bu2ey7C2VJRf0u2sDlyddcr07HCzBURaHx1Pd6IJbQ16fkFwJmtmnEck83pvdJx1DmyhdfVSwa7jq2DrByOhlzGh2GMYZh2_4NDDaRF8zbZ-ik4Yg1B3YkyMagjRyhc2ujaw5DYKO_98DB2syANjohlctxahBcG8Ki_VJJf2Hy-kPWZcxqJY0-RlkWpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4918cf32ee.mp4?token=U_iAZibVXY8Q8bv7-djxVIMuZRBn0Yi3vUK12OUBYEDMfvZ_pZ1KzvFIkBdQZoqHMJ1y2sFYdrUxGGwd3yy9YyaJCQfXiTq54_CdjdvqFzzxS1kxsNeK1VjY0L8cDRls86fSw1TK7BvmHJr_ah1zHuGXU2bu2ey7C2VJRf0u2sDlyddcr07HCzBURaHx1Pd6IJbQ16fkFwJmtmnEck83pvdJx1DmyhdfVSwa7jq2DrByOhlzGh2GMYZh2_4NDDaRF8zbZ-ik4Yg1B3YkyMagjRyhc2ujaw5DYKO_98DB2syANjohlctxahBcG8Ki_VJJf2Hy-kPWZcxqJY0-RlkWpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام‌ جهانی 2026
⚽️
فرانسه
🇫🇷
-
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
⏰
شروع بازی ساعت 00:30
✔️
امکان ثبت پیشبینی با مبلغ نامحدود
🫰
محاسبه نرخ دلار با قیمت 2.000.000 ریال
⭐️
فرصت استثناییی چالش‌های پیشبینی فوتبالی سایت یک توتو، با جایزه 500 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68471" target="_blank">📅 20:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68470">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
سازمان تجارت دریایی بریتانیا (UKMTO) اعلام کرد که گزارشی مبنی بر وقوع حادثه‌ای بین یک کشتی تجاری و نیروهای نظامی، در فاصله حدود ۱۰۰ مایل دریایی به شرق شهر الدقم در کشور عمان دریافت کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68470" target="_blank">📅 20:19 · 27 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
