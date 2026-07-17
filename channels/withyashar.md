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
<img src="https://cdn4.telesco.pe/file/dL9sMLxqA4yDGGTsZhOrp9saIv2hCznBtK5sqbXZUHHLYRfW7Sa7-BvTY3nQz_tTNWeN52cYqShsiJjEPTlyXiDt0LLAoeItlT021Q9U5CYHb8E58HbvVcKiCD17jy-XDd0UbXrtTd8StZffNfVq2Y5rivJNvEdPPSEfNACBkhDVF10voTlYota7a-qR3UqpIzfHiTFPaXtxGP8xEckVMDXkhW5A98CqV0cj6_QRHIyovEwHA9VkTgGHjUbARCLMq1BHr4pLaHYgBPFMPP24cOeGnMAQsrOov_pbUxQOlstxQufGyoLGpKQTBxKP1Ovd9XFi3dV-FFrr_2CI0GYDAg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 404K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-27 01:24:32</div>
<hr>

<div class="tg-post" id="msg-18651">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">جنگنده ها هم ارتفاع پایین اومدن خیال راحت بندر رو میکوبن
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/withyashar/18651" target="_blank">📅 01:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18650">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">حملات به یزد و بندر عباس ادامه داره @WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/withyashar/18650" target="_blank">📅 01:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18649">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">حملات به یزد و بندر عباس ادامه داره
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/withyashar/18649" target="_blank">📅 01:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18648">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">تسنیم: حمله  آمریکا به مناطقی در لار و داراب
@WarRoom</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/withyashar/18648" target="_blank">📅 01:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18647">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">بندرعباس  ۳ تا انفجار سنگین الان
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/withyashar/18647" target="_blank">📅 01:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18646">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">جاده اندیمشک - اهواز الان زدن
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/withyashar/18646" target="_blank">📅 00:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18645">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">صدای‌ انفجار سنگین الان در کویت
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/withyashar/18645" target="_blank">📅 00:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18644">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">بندر عباس ۲ تا پشت هم الان
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 74.9K · <a href="https://t.me/withyashar/18644" target="_blank">📅 00:55 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18643">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5667848bf1.mp4?token=KwJkKVa45MgrY87FAk5tUKy3uY1ydjm-veLumLsaq03ZCVa7_YA_gRYmjixOI1pBDrnP2AIIU5ZmisLTpW5jB0hv0qD7uP3U7yYTPWEze6aiJwLSdTam_PdGdBn154wOU9r_xFvsKNuzBQCkShWQn10v7UlUZSTsJZIhTNZiAj5aycgB8TnKYTYc9k2_acfaSJRXyib199mFDkaeUgTvhSBftKwdyWdTssRd-dSiebkju65N_qYnKywvNw0oTnv6M-IoH1nYoaXXK9r8vr9DKrG7Sva_c-LIq9clDeKIYKXTIBAKuAS_9p9PhyaujXreB1zNe8gGNgRrGbJ2KM25hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5667848bf1.mp4?token=KwJkKVa45MgrY87FAk5tUKy3uY1ydjm-veLumLsaq03ZCVa7_YA_gRYmjixOI1pBDrnP2AIIU5ZmisLTpW5jB0hv0qD7uP3U7yYTPWEze6aiJwLSdTam_PdGdBn154wOU9r_xFvsKNuzBQCkShWQn10v7UlUZSTsJZIhTNZiAj5aycgB8TnKYTYc9k2_acfaSJRXyib199mFDkaeUgTvhSBftKwdyWdTssRd-dSiebkju65N_qYnKywvNw0oTnv6M-IoH1nYoaXXK9r8vr9DKrG7Sva_c-LIq9clDeKIYKXTIBAKuAS_9p9PhyaujXreB1zNe8gGNgRrGbJ2KM25hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یزد
@WarRoom</div>
<div class="tg-footer">👁️ 84.1K · <a href="https://t.me/withyashar/18643" target="_blank">📅 00:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18642">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">اهواز و زدن
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 85.1K · <a href="https://t.me/withyashar/18642" target="_blank">📅 00:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18641">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-footer">👁️ 85.1K · <a href="https://t.me/withyashar/18641" target="_blank">📅 00:47 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18640">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-footer">👁️ 88.2K · <a href="https://t.me/withyashar/18640" target="_blank">📅 00:44 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18639">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">یزد یدونه سنگین زد الان
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 92.3K · <a href="https://t.me/withyashar/18639" target="_blank">📅 00:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18638">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-footer">👁️ 91.3K · <a href="https://t.me/withyashar/18638" target="_blank">📅 00:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18637">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">یه سلامی کنم به مهراد جم که تو چنله
😁
داداش شهرتو زدن</div>
<div class="tg-footer">👁️ 93.3K · <a href="https://t.me/withyashar/18637" target="_blank">📅 00:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18636">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">چندین انفجار جم در استان بوشهر
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 93.3K · <a href="https://t.me/withyashar/18636" target="_blank">📅 00:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18635">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">بندر عباس صدای انفجارررر
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 93.3K · <a href="https://t.me/withyashar/18635" target="_blank">📅 00:39 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18634">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-footer">👁️ 94.4K · <a href="https://t.me/withyashar/18634" target="_blank">📅 00:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18633">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">یزد یدونه جدید زد
@WarRoom</div>
<div class="tg-footer">👁️ 93.3K · <a href="https://t.me/withyashar/18633" target="_blank">📅 00:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18632">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">انفجار شدید اهواز سمت پلیس راه و انبار نفت
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 93.3K · <a href="https://t.me/withyashar/18632" target="_blank">📅 00:37 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18631">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">اهواز تایید انفجارررر
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 95.4K · <a href="https://t.me/withyashar/18631" target="_blank">📅 00:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18630">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">اتشکده خراب نشه حواستون باشههههه</div>
<div class="tg-footer">👁️ 96.4K · <a href="https://t.me/withyashar/18630" target="_blank">📅 00:34 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18629">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">یزددددد
🚨
🚨
🚨
🚨
۵ انفجاررررررر
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/18629" target="_blank">📅 00:33 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18628">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">یزد صدای ۳ انفجار
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 99.5K · <a href="https://t.me/withyashar/18628" target="_blank">📅 00:32 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18627">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3945766522.mp4?token=r5jJYKY_Vg81o25td3vtEJbdEkEMfhSFvIO0l4ti0DIJAMxO3vJviMxpyv4d7D0XearvKlXjH_9jeWPGUjpvD7H8pIUsC7zPRn--rjQANv0s_lAt65-HXMX99EYFHh3mDuHPyuGqXdM-QOB_F5zqWPx-6NIV-L-BUP-0TU6ZNBQlTDdxJ0ehfbEB8lVVS5zVLV554rCItI7U8zy51VLKjTxZJnH4dgkHolWABu62vb1uIdO27gorhscnoIOKOP_K3PHIKIRLdBrzvl1iyIGMSRZybKpiDmPvrH_Ur4m0zpZg7sAxMsO7jAIsYOguGgKHPTNZVn2tDuy9FBChgZyDJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3945766522.mp4?token=r5jJYKY_Vg81o25td3vtEJbdEkEMfhSFvIO0l4ti0DIJAMxO3vJviMxpyv4d7D0XearvKlXjH_9jeWPGUjpvD7H8pIUsC7zPRn--rjQANv0s_lAt65-HXMX99EYFHh3mDuHPyuGqXdM-QOB_F5zqWPx-6NIV-L-BUP-0TU6ZNBQlTDdxJ0ehfbEB8lVVS5zVLV554rCItI7U8zy51VLKjTxZJnH4dgkHolWABu62vb1uIdO27gorhscnoIOKOP_K3PHIKIRLdBrzvl1iyIGMSRZybKpiDmPvrH_Ur4m0zpZg7sAxMsO7jAIsYOguGgKHPTNZVn2tDuy9FBChgZyDJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو حمله به سایت موشکی در جاده گراش لار شرق استان فارس
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/18627" target="_blank">📅 00:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18626">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">پدافند نجف آباد درگیر شده
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/18626" target="_blank">📅 00:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18625">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">پرتاب موشکاز لار ، جنوب شرقی فارس @WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/18625" target="_blank">📅 00:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18624">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">گزارش‌ انفجار لار
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/18624" target="_blank">📅 00:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18623">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b90e84e1a0.mp4?token=IBbMdNRzMgwOomU5pct8VT3Krb7RoYtC42zTQUjxHZ0jzMjJZbApOxDGVsWpmEqIPWo54cWbOheRASpRNx_UngoKKaHD6s9RPjx-nM5PUkrgZoaQ__WDu1EHz9TCeYxAsu4PBJhHo1rO7C9N-aGqB_ytQ4GS-BMpX_gLMz_adpjIaOpEkZ7riUW64CA08RJK-ktRDx_l573uCnKnX8hASpMROEItu9YalxfpvKlzeYBWqmO4FFA0JY_7pnzzmt6bnC5CSlHXTyHXdsFpZbljQNSjKffwqAAczbArpsIRddWNZTc8KQIPxWdP3R8Qx6-usaASN18eWGZnPGfmaj5irg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b90e84e1a0.mp4?token=IBbMdNRzMgwOomU5pct8VT3Krb7RoYtC42zTQUjxHZ0jzMjJZbApOxDGVsWpmEqIPWo54cWbOheRASpRNx_UngoKKaHD6s9RPjx-nM5PUkrgZoaQ__WDu1EHz9TCeYxAsu4PBJhHo1rO7C9N-aGqB_ytQ4GS-BMpX_gLMz_adpjIaOpEkZ7riUW64CA08RJK-ktRDx_l573uCnKnX8hASpMROEItu9YalxfpvKlzeYBWqmO4FFA0JY_7pnzzmt6bnC5CSlHXTyHXdsFpZbljQNSjKffwqAAczbArpsIRddWNZTc8KQIPxWdP3R8Qx6-usaASN18eWGZnPGfmaj5irg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پهپاد دیدبانی رژیم در آسمان شیراز
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/18623" target="_blank">📅 00:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18622">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">اصفهان صفه کوه لرزید
🚨
🚨
🚨
🚨
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/18622" target="_blank">📅 00:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18621">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">گزارش انفجار اهواز
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/18621" target="_blank">📅 00:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18620">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">صداوسیما: صدای ۳ انفجار در بخش بمانی سیریک شنیده شد
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/18620" target="_blank">📅 23:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18619">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ma_wnLdTPUarvlfkjvYrNJhuy1jVHcA4bwuFEspYQj-uqJPwt5tXLVNM52wyzm2aDQ_HJJDCbTKyxGaFRXCpFZK7s11D1MD6NeH1Ta0szfbQsuDslztfwWI8R9LFwVCxLJbTFHscRRq4Mu7DG9pRP1QtPk8jB3RtOquVGsKkjlMOzMuvof97VQJpl6gqa0Z3o1J8Vje9_lzwwbrYsos3yRREr-eHWHAftvDk0pdiLOOoxy6HFs-ZZqD-He0qMUod7u8Dfbggy5SZ2EaOgpO7OOlPP1cpwEC_lW9iEqDx342vCJ8m1ZSAA4bl7kuXGWkCbr1bg943uOzX65o0o4-XMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایگاه الحریر امریکا شمال عراق در
آتش
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/18619" target="_blank">📅 23:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18618">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">انفجار بندر عباس
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/18618" target="_blank">📅 23:46 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18617">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">صدای انفجار اندیمشک
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/18617" target="_blank">📅 23:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18616">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">صدای انفجار چابهار
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/18616" target="_blank">📅 23:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18615">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">سیریک رو همچنان میزنه
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/18615" target="_blank">📅 23:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18614">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">صدای انفجار اهواز
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/18614" target="_blank">📅 23:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18613">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">گزارش انفجار کنگان
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/18613" target="_blank">📅 23:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18612">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">انفجار وحشتناک قشم
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/18612" target="_blank">📅 23:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18611">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">سپاه خورموج رو زدن
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/18611" target="_blank">📅 23:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18610">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">گزارش صدای انفجار ‌اهواز
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/18610" target="_blank">📅 23:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18609">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">انفجار در ‌قشم
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/18609" target="_blank">📅 23:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18608">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">بندر عباس
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/18608" target="_blank">📅 23:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18607">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">بوشهر
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/18607" target="_blank">📅 23:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18606">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">دوباره سیریک
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/18606" target="_blank">📅 23:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18605">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">سیریک زد الان
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/18605" target="_blank">📅 23:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18604">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">۳۰ دقیقه پیش ۲ گزارش از انفجار در اهواز داشتم
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/18604" target="_blank">📅 23:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18603">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">سنتکام اعلام کرد
امروز ساعت ۳:۰۰ بعدازظهر به وقت شرق آمریکا (ET) (۲۲:۳۰ به وقت تهران)
،
هفتمین شب متوالی
حملات خود علیه ایران را آغاز کرده است
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/18603" target="_blank">📅 23:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18602">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">سنتکام : شروع کردیم
🚨
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/18602" target="_blank">📅 23:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18601">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48b7df7221.mp4?token=p9OGaNHGYZc6_R5IIFd5dpRODe1AHz1KtxEmKhTiFqQlbUtkuTWeWhC2-9gQi23yonqY43dVHNesg0qD_TdaSMb0NjYDoedM5kVW_9rXqbFEgMIskTI_TB_6X06EGxrHXbkX2bL7Zl1XXadmt9aSeKem-UZCK8dgpIwxbBefhqqSLV5isG_e2d-kkdyHJjVp7-wbM9F4h9C-dODT1xml3p_6l6T85FoPuikNMVstF-lg7AChbLZbsrPySfFZHR0aNp3NoHd9bPKKVBM63FQH-j8_2MKyUquaHQwOy0DEPokzGbzq3Wzy6wiK0_6tp3yKdV4Y6iF-kM4T6d5oNmEFoaZNsjxz0ZYOmiysYntoFfdczobR8V5Ey-x-Ked4G-Uk4keR4FRxpnnI11mDviQCa2M7DbUCxIfZvCWihxo16n16cZdgyTHD5AlSEG3v4Fzu7CpXn63KOGadL_EGqDa_v3uNQUIpTc5q9O9DRYWdmfw1PAIc4DhytFOEXCVXp8Rg9tz8D5GCwz_rh0TtZHqX_psenMjrtM0-k1ohq8pwIrGIXp1_3jfzb8kqnaLTf43eb6AXh2DSEC0_BecteZObAuVxcG34y_i6hLeWkVsZKdpZOXGkfvNSKBUfbjxcY3fl06skJvapA9LO8wUN3v2Jmg_sSKttoJrhuT9zTarMHwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48b7df7221.mp4?token=p9OGaNHGYZc6_R5IIFd5dpRODe1AHz1KtxEmKhTiFqQlbUtkuTWeWhC2-9gQi23yonqY43dVHNesg0qD_TdaSMb0NjYDoedM5kVW_9rXqbFEgMIskTI_TB_6X06EGxrHXbkX2bL7Zl1XXadmt9aSeKem-UZCK8dgpIwxbBefhqqSLV5isG_e2d-kkdyHJjVp7-wbM9F4h9C-dODT1xml3p_6l6T85FoPuikNMVstF-lg7AChbLZbsrPySfFZHR0aNp3NoHd9bPKKVBM63FQH-j8_2MKyUquaHQwOy0DEPokzGbzq3Wzy6wiK0_6tp3yKdV4Y6iF-kM4T6d5oNmEFoaZNsjxz0ZYOmiysYntoFfdczobR8V5Ey-x-Ked4G-Uk4keR4FRxpnnI11mDviQCa2M7DbUCxIfZvCWihxo16n16cZdgyTHD5AlSEG3v4Fzu7CpXn63KOGadL_EGqDa_v3uNQUIpTc5q9O9DRYWdmfw1PAIc4DhytFOEXCVXp8Rg9tz8D5GCwz_rh0TtZHqX_psenMjrtM0-k1ohq8pwIrGIXp1_3jfzb8kqnaLTf43eb6AXh2DSEC0_BecteZObAuVxcG34y_i6hLeWkVsZKdpZOXGkfvNSKBUfbjxcY3fl06skJvapA9LO8wUN3v2Jmg_sSKttoJrhuT9zTarMHwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افزایش گسترده تحرکات ترابری هوایی نیروی هوایی آمریکا به‌ خاورمیانه
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/18601" target="_blank">📅 23:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18600">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ارتش کویت: حملهٔ رژیم ایران منجر به هدف قرار گرفتن تعدادی از تاسیسات و اردوگاه‌های متعلق به ارتش کویت با استفاده از پهپادها شد. در نتیجه، تعدادی از پرسنل نیروهای زمینی کویت در حین انجام وظایفشان مجروح شدند.
همچنین، تعدادی از تاسیسات حیاتی و مدنی، از جمله یکی از ایستگاه‌های تولید برق و تصفیه آب، مورد هدف قرار گرفتند. این امر منجر به وقوع آتش‌سوزی و آسیب رساندن به تعدادی از تجهیزات ایستگاه و واحدهای تولید برق شد. علاوه بر این، ترکش‌ها در تعدادی از مناطق کشور پراکنده شدند.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/18600" target="_blank">📅 23:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18599">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">اگه ویس های چنل رو گوش کرده باشی امروز سوألی نمیکنی
😁</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/18599" target="_blank">📅 23:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18598">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">دونالد ترامپ، در دفتر بیضی شکل خود با دارلین گراهام، خواهر لیندسی گراهام که موقتاً جایگزین او شده است، دیدار کرد و از او خواسته است تا در انتخاباتی که در ۱۱ آگوست برگزار می‌شود، به طور دائم در سنا نامزد شود و گفت «امیدوارم این کار را بکند، هیچ کس بهتر از او نخواهد توانست میراث برادر عزیزش را گرامی بدارد. دارلین از خانواده‌ای فوق‌العاده می‌آید و در تمام زندگی‌اش برنده بوده است. اگر او موافقت کند، از حمایت کامل من برخوردار است.»
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/18598" target="_blank">📅 23:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18597">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">وای نت عبری : تاکنون بیش از ۶۰ هواپیمای سوخت‌رسان آمریکایی وارد اسرائیل شده‌اند که ۳۳ فروند از آنها در فرودگاه بن گوریون مستقر شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/18597" target="_blank">📅 22:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18596">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17da528eaf.mp4?token=dZWSjIoJl4BkIYA2Oa7GdbFiD1uK4jnacwW_CCnsaPCldrxid3TB2No_-94yCymHe9JiTBX4IpG4eCEqzX0tN-BRQ6esUtxCdYM9r9E2lmRJIeGgfKAefHpEQv_Dotn2OoTYhpJ65uQKEvS1sN9DD3Wid3BnPH9MBJcUY3YgXryrbZYxplcv0Bkxb54tDdUIPISzTak24zXvQ8BSOoSWAAJNT8PBTFswISPy0iHS0nU1TJ1Mdyn9HNV18OzVrXlZ5DR-5x5pCHnuCAtJwsBYepIVxpwd8Ns6H-xBNo0xxc6PWYD6og8noomj1OQSxhkr--bcZRaRNbQ1JcYKH7vxTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17da528eaf.mp4?token=dZWSjIoJl4BkIYA2Oa7GdbFiD1uK4jnacwW_CCnsaPCldrxid3TB2No_-94yCymHe9JiTBX4IpG4eCEqzX0tN-BRQ6esUtxCdYM9r9E2lmRJIeGgfKAefHpEQv_Dotn2OoTYhpJ65uQKEvS1sN9DD3Wid3BnPH9MBJcUY3YgXryrbZYxplcv0Bkxb54tDdUIPISzTak24zXvQ8BSOoSWAAJNT8PBTFswISPy0iHS0nU1TJ1Mdyn9HNV18OzVrXlZ5DR-5x5pCHnuCAtJwsBYepIVxpwd8Ns6H-xBNo0xxc6PWYD6og8noomj1OQSxhkr--bcZRaRNbQ1JcYKH7vxTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن کج بند : اگر حملات ایالات متحده در دو تا سه روز آینده ادامه یابد، نیروهای مسلح جمهوری اسلامی از مرحله بازدارندگی و پاسخگویی فراتر رفته و وارد فاز «تهاجم و نابودی کامل» خواهند شد، به طوری که پایگاه‌ها و سربازان ایالات متحده فراتر از مرزهای سیاسی تعقیب و مستقیماً هدف قرار خواهند گرفت.
ایالات متحده باید بداند که استراتژی فرسایشی «جنگ و مذاکره» به بن‌بست رسیده است و در روزهای آینده، شدت حملات ایران افزایش خواهد یافت.
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/18596" target="_blank">📅 22:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18595">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">فاکس نیوز : یک گزارش محرمانه که برای ریاست‌جمهوری ایران تهیه شده، نشان می‌دهد تنها ۹ درصد ایرانیان از حفظ وضع موجود حمایت می‌کنند؛ در حالی که نزدیک به سه‌چهارم مردم خواهان اصلاحات عمیق ساختاری یا تغییر کامل نظام سیاسی هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/18595" target="_blank">📅 22:41 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18593">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e2f05b5ce.mp4?token=SRPNGrvnYJzD96l-l7Rdnk07cg7WEJPk_Yfc93U4AVOYtiFEeFUoPWDbA5QYenB35wJzK6ejnFCesCzXpYo9QmAfje9eWFRZU7kS9iSUKcs5jlbO1h69mHD6UsasNQK0leUZtY_X944WQqmm4Rw-yoWO6b-FSlEUbBaryyxfip4nxoELkvYtxHDRu0xuNKAR98sd3LxbCcfwxZ0t8lbmXhyTpgUeGF6iywB0PH0a-D6sl36e_ggfXcvWZuTCSALeyFlxya1YmW2QeR2Q-8gZsuZiNnzt2L7zT2p3PN9UmwRaKb0bT_4wpeeFRjrFt3F2TAVPH8bG3tnSVQi--Rc7KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e2f05b5ce.mp4?token=SRPNGrvnYJzD96l-l7Rdnk07cg7WEJPk_Yfc93U4AVOYtiFEeFUoPWDbA5QYenB35wJzK6ejnFCesCzXpYo9QmAfje9eWFRZU7kS9iSUKcs5jlbO1h69mHD6UsasNQK0leUZtY_X944WQqmm4Rw-yoWO6b-FSlEUbBaryyxfip4nxoELkvYtxHDRu0xuNKAR98sd3LxbCcfwxZ0t8lbmXhyTpgUeGF6iywB0PH0a-D6sl36e_ggfXcvWZuTCSALeyFlxya1YmW2QeR2Q-8gZsuZiNnzt2L7zT2p3PN9UmwRaKb0bT_4wpeeFRjrFt3F2TAVPH8bG3tnSVQi--Rc7KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت جهنمی سلیمانی عراق انگار که آتش فشان فوران کرده ! بی شک اگه کرد ها تو پلن نبودن اینجوری نمیکوبید پشت دست خیلی خبره !
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/18593" target="_blank">📅 22:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18592">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">چهار سوخترسان از اسرائیل بلند شدند @WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/18592" target="_blank">📅 22:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18591">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BbBWPYjLLwmdeFJ1Txn1mq7S0PSzfBpCMFYFBGJ9sSNZIH9AtfTkvgDBs0tM0LcLU3c4yz4Ba7mIDjfsDsB4ihWVYdbbhImwGANGsMqCc9zDucjzTrq8sHGB7gNQCHNnbz-HB-ntGM6G3aViJaDeR45LkDrQV7V27gsL3_O3HcIDu7RuvkhW6JtYXh9tzAfc6j99yMEGhowF_V2IcZm8BV2ejag6hzg9vwMRGtEa7Ys7AdjEeFEDuDvafAJU84oSnBUMIjO18Qeaoe2ap3yW47J9xrrwi-hD41SqYY-GWWCvKoex8D4APiSgOKbVHoVH0a8ugxy8mnF8bNTKJCF5qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چهار سوخترسان از اسرائیل بلند شدند
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/18591" target="_blank">📅 22:05 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18590">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N3z35BVT_8b1i2q6bwvT_WLB0oTg6FvKi78nQKuJ5fCsMZE6kxTyxc7AlIVqREEZjtEo09a0NGA88UN9RsHplYAz9f01bUqc-4odU0x9vGawY3btAyZr1c5lDS7KK2KWSCCsTovs9KiCTyfr9cNW3F-yFrTlrF05FsBok6826GDzfk4tx2p5posqbkmCg5U-Rgcch6cfesvxwDOVM22B0NjlhyXWFZ3RNu7E_tuCaqRESzHEFP5GidMCuPXvQmXx18HzrfWhHec9AK-ogbrbTyCSZHfHrb6h0QnKPiYt-ejChRx3PvfblINhO4_g26dlyzQyqSinGxKW2AkTmk1uFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستون دود در سنندج
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/18590" target="_blank">📅 22:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18589">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SC6aWuQj8uIxCIfBB0StMYfSgQnbhcrbsoADlMD1SKctTS7JI3mbt9OHFG4mhOFZyVWTzl2MJ7cUqQk-NaMEb7OakEP3JZKxZpQvncJo0q-5PhFKRITLR-wp2aa4KW2a_YwVOqKCxpO6Xj9PJpgVZ780Q4gv4IVE-tsGtxl1Y45cmhTlYSNnPrT42soohU2D40L2l7ucb_MY2hcJdclqplFZ7lwPtXsqby47PWtXAfJKVj7PlEeiv_Cq7Z5k_PlNRfH2Y3P4URD1alfGRC4TwGzQ0f477k0v8GmY40xNsZ_yFbbOeXMPOmrfxjMhm9uFKcq7Fy1jTvgG8689V784sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجم سنگین آتش در انبارهای مقرهای گروه‌های کرد مخالف جمهوری اسلامی در اربیل و سلیمانیه عراق ، کل کوه در آتش میسوزد این گروه ها از مدتی پیش به کوه ها پناه آورده بودند و پایگاه ساخته بودند
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/18589" target="_blank">📅 21:42 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18588">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/18588" target="_blank">📅 21:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18587">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">حقیقت یاب اتاق جنگ
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/18587" target="_blank">📅 21:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18586">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">گزارش انفجار جدید در بندر عباس و یع صدا هایی‌در ‌بوشهر
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/18586" target="_blank">📅 21:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18585">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">خبرگزاری تسنیم: هم اکنون حمله موشکی سپاه به یک کشتی تجاری در تنگه هرمز.
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/18585" target="_blank">📅 21:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18584">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">با حملات پهپادی/موشکی آتش‌سوزی‌هایی شدیدی در پایگاه‌های گروه‌های  کرد مخالف جمهوری اسلامی در شهر سلیمانیه رخ داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/18584" target="_blank">📅 21:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18583">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">اتاق جنگ با یاشار : وضعیت انفجاری ‌منطقه
🚨
🚨
🚨
🚨
🚨
💥
۴۰۰ هزار نفر در اتاق جنگ با یاشار! سپاس از همراهی و اعتماد شما. این تازه آغاز راه است.
🎉
400,000 members in @WarRoom with Yashar! Thank you for your trust and support. This is just the beginning.</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/18583" target="_blank">📅 21:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18582">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‎ وال استریت ژورنال:آمریکا جنگنده‌های خود را از اروپا به خاورمیانه بازمی‌گرداند
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/18582" target="_blank">📅 20:46 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18581">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">۲ انفجار بندر عباس
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/18581" target="_blank">📅 20:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18580">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">گزارش انفجار بندر عباس
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/18580" target="_blank">📅 20:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18579">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">آکسیوس: مقامات دولتی ترامپ به اسرائیل اطلاع داده‌اند که
ده‌ها فروند هواپیمای تانکر سوخت را به این کشور اعزام خواهند کرد،
این اقدام در آستانه یک گسترش احتمالی عملیات نظامی علیه جمهوری اسلامی ایران صورت می‌گیرد. سه مقام آمریکایی و اسرائیلی این موضوع را تایید کردند."
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/18579" target="_blank">📅 19:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18577">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SsKoFAfa67d_K9ykYfbQQrqg-n_KE8i9038JVLaWpkjtCqq6PqS7gfVrissO0u4nUdspdLYMP0mtz7BvDwNfFr2ABU6UWhapaYB1eiyUMbm4-dEqEspq6m-nHaCmltGdVu6gK5Oo2ZQvSmU1O1lyk5FJWeDPKFhDnQjFk5EQHuRTIpLxQfga9hhV6yR1OGs8-yK3Ww7xCzM_dYkz8HedrFfdQStaxy87_5hTCcJgYljTb33v_2xn438UGIpzAKsKxZgtRV4MbuYJUAmA2i2trBQjPvIQDgAJO8zjlQWBkMH9LZzv9mdqXetz-AmOxcotTi7x2zQGAyEXUt5OvaYsQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57565771c4.mp4?token=O0UX4C2dUg5Y_WgN6w8yuyzxiYk--3UEjtFBpd24DDEfhgziQ5C2-88GXmPuIvacJlyJ3OvWyYwhYESzqzptMUw2w0oqFsMb3HOtG55beXZQ1DBqk7lECl0fy-czFRDXJfzZy1WwTlFyCdMUdygifsjz0KUS9LGI0t--7bJPfmQhhJBCVExZpC9QN34mV6i1eEG00V6oq8bmwmRy5Aaa4oLG1YRZcL9Wa55Jha36C2sU4jPP-yZ9mdMo7KbejRchVX3lJxg2Ovp8-elJyNpp-yX9FAdibmQx1E9wqpjNYCFG4s0aBc6aLdmC3J_HyQyKj5ZYqRVqhJNYtYSzzzcYhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57565771c4.mp4?token=O0UX4C2dUg5Y_WgN6w8yuyzxiYk--3UEjtFBpd24DDEfhgziQ5C2-88GXmPuIvacJlyJ3OvWyYwhYESzqzptMUw2w0oqFsMb3HOtG55beXZQ1DBqk7lECl0fy-czFRDXJfzZy1WwTlFyCdMUdygifsjz0KUS9LGI0t--7bJPfmQhhJBCVExZpC9QN34mV6i1eEG00V6oq8bmwmRy5Aaa4oLG1YRZcL9Wa55Jha36C2sU4jPP-yZ9mdMo7KbejRchVX3lJxg2Ovp8-elJyNpp-yX9FAdibmQx1E9wqpjNYCFG4s0aBc6aLdmC3J_HyQyKj5ZYqRVqhJNYtYSzzzcYhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصویری از حملات امریکا به مرکز توزیع خط ریلی بندرعباس
@WarRoom</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/18577" target="_blank">📅 19:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18576">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">بیانیه ارتش : نیروهای ویژه تیپ ۶۵ نوهد با انجام ۱۱ عملیات و ورود به خاک کردستان عراق ۸ نفر از فرماندهان ارشد گروهک های تجزیه طلب رو با موفقیت ترور کردن و ۳ مقر مهم نیروهای تجزیه طلب رو بصورت کامل تخریب کردن
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/18576" target="_blank">📅 19:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18575">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cdac5e1f0.mp4?token=gbpee8JwsBXPBFKifNV2an2tHHeGvQitKZOmMxhL-BYqzwHIXwTsSwLcPDasE25xFNNQeigeunkynVaUROyLMmUuOYDZ2QJqFZ6ZluF2ufLqOB0BJwh2YU9xi-I8HhQ0aFUjCBhu7WY7gfGW-A9H5Xa4OLBpSDB5d-TIHKVMe5r1yYGscUCD9IXZeZwZP2U_CGK4I8sdNQ8Bio_7waYGqutH_Wkt5DYBGc2ocT5OnqmR-jjmty1t5iKouGn1SNFLqCMKnyY9kisa9K87iaObjGBbS4hMVazT3bJeCb0xhghdbGrvI1lxxpief9K6opURWGSLAextnvXgp8mnj4T68Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cdac5e1f0.mp4?token=gbpee8JwsBXPBFKifNV2an2tHHeGvQitKZOmMxhL-BYqzwHIXwTsSwLcPDasE25xFNNQeigeunkynVaUROyLMmUuOYDZ2QJqFZ6ZluF2ufLqOB0BJwh2YU9xi-I8HhQ0aFUjCBhu7WY7gfGW-A9H5Xa4OLBpSDB5d-TIHKVMe5r1yYGscUCD9IXZeZwZP2U_CGK4I8sdNQ8Bio_7waYGqutH_Wkt5DYBGc2ocT5OnqmR-jjmty1t5iKouGn1SNFLqCMKnyY9kisa9K87iaObjGBbS4hMVazT3bJeCb0xhghdbGrvI1lxxpief9K6opURWGSLAextnvXgp8mnj4T68Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام : در
۱۶ ژوئیه (۲۵ تیر)
، نیروهای آمریکایی با موفقیت
برج دیده‌بانی بندر شهید کلانتری چابهار
را منهدم کردند؛ برجی که بخشی از شبکه نظارت دریایی در امتداد سواحل ایران در
دریای عمان
بود و به ادعای آمریکا،
سپاه پاسداران
دهه‌ها از آن برای رصد و هدف قرار دادن کشتی‌های تجاری عبوری از
تنگه هرمز
استفاده می‌کرد.انهدام این برج به‌طور مستقیم توانایی سپاه پاسداران برای هماهنگی حملات علیه خدمه غیرنظامی کشتی‌ها را کاهش می‌دهد
@WarRoom</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/18575" target="_blank">📅 18:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18574">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">دقایقی پیش فرمانده نیروی دریایی سپاه به آمریکا هشدار داد:آمریکایی‌ها با هر لحظه که می‌گذرد،به لحظه سرنوشت‌ساز برای عملیات علیه یگان‌های دریایی فرماندهی مرکزی ایالات متحده در آب‌های این منطقه نزدیک‌تر می‌شوند،فقط منتظر بمانید،
ساعت صفر نزدیک است.
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/18574" target="_blank">📅 18:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18573">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e9ed530a7.mp4?token=dbOmx9-PbX-sQlO3uP6YUXrp0UwHEe3hVKZInVPX-Ww819KVX5LszijW3EdtqtHUN49h51fzo4TWFFOzbsBp0r7AFWvYgNg2MDMQeh9KOH45E5u0RtiZhny-rMUIqOB-rQtI0lOVlHXX6u2j8LHfAsnhOvjMDHor-LVRA4H4gHCL87Xhx38BZHnEOUaVf4RyLzPjqTMw5IJL4GsWNWrZl2znbbNE2UfiiFmr7q9rw6y5-4lniEiYVlW-BqJs8bZkT-9vmKgTx5NS2jqBH-6pFAxQMU2Fcth89AcX-EkPYtQzalxL5_gnqEq81abWmc6zUt0FwaYki8GwGoTR_-A5Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e9ed530a7.mp4?token=dbOmx9-PbX-sQlO3uP6YUXrp0UwHEe3hVKZInVPX-Ww819KVX5LszijW3EdtqtHUN49h51fzo4TWFFOzbsBp0r7AFWvYgNg2MDMQeh9KOH45E5u0RtiZhny-rMUIqOB-rQtI0lOVlHXX6u2j8LHfAsnhOvjMDHor-LVRA4H4gHCL87Xhx38BZHnEOUaVf4RyLzPjqTMw5IJL4GsWNWrZl2znbbNE2UfiiFmr7q9rw6y5-4lniEiYVlW-BqJs8bZkT-9vmKgTx5NS2jqBH-6pFAxQMU2Fcth89AcX-EkPYtQzalxL5_gnqEq81abWmc6zUt0FwaYki8GwGoTR_-A5Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قرارگاه سپاه در راسک که در اثر حملات آمریکا ترکیده و فقط تابلوش باقی مانده.
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/18573" target="_blank">📅 18:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18572">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">سیتنا: با پیگیری‌هایی که انجام دادیم، خبرِ "آمادگی دیتاسنترها برای قطعی اینترنت" که از صبح داره وایرال میشه صحت نداره.
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/18572" target="_blank">📅 18:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18571">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VAp12P558Wh4gApltgY6aQ9XnCiqWrBVDTm7ndCkguufwjxPDEzmgU9_2pI__MVnHlpsuRvhmy1hwnb-UCl7FbttJo8hPZw3DCKetLAE5KgOOcv4Cckssfh_Avy3nwQnKhoQOOt-3cdGXK036475Dt1ncRnAF9Ha6dfpA6KUAuQ0m4Wg9-1RYtYuODxxAK900CtrFM5W3HNQ0OfEaDZW7kkShNWU9YKoM1B_FmBXj2L-Lr_Z4XTyFzj3N6i-wxLWW7DA3fr4GvSG_7ByabpDNoqCYZuplQDiUqYg7PCOVcVcIQkBtikBjVli6TuMDXDgjMB6CCjmuD7IVliRTcByog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل : «عملیات همچنان ادامه دارد»
یک فرمانده گردان حماس که در نگهداری گروگان‌ها نقش داشته و دست راست مقامات ارشد این سازمان بوده، به هلاکت رسید.
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/18571" target="_blank">📅 18:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18570">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T3z2Fqcu-rcN2djclJI6YCosBLXrykGY0pFsg1I3Sv7e2hQHH8J7MQhNPvuevgEXEjKZf8rUkljIK_AfbFTAdNcaAcHkxkvQ_9XreMmO7NmUi_oSqrSC6I8QlxQjt_NrD6STnF8gvnlRxP_i271hoSk9iqsEA8ZJJq2izIXekLogUB44rpUdJ6ayOfBeEN6u2YWT2WrlgZ137FfbAbOzQsRopTezx0BfT49jzxoqRHNeUxbpvVmVZyqZFTo47zhQL2ThxQTh-qa7HoYWdTaGrOiCjtx8kzHq35KplYh9tVH5SYb3PwP2XKA7TQc8oKVDBpyPVxi5Pp95g4-_fjObXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏۶ فروند F35 طی ۲۴ ساعت گذشته از پایگاه هوایی اندرسن در گوام به خاورميانه اعزام شده اند.
@WarRoom
پایگاه هوایی اندرسن (Andersen Air Force Base) یکی از مهم‌ترین پایگاه‌های راهبردی نیروی هوایی آمریکا در اقیانوس آرام است و در جزیره گوام قرار دارد.
گوام (Guam) یک جزیره در غرب اقیانوس آرام و یک قلمرو وابسته به آمریکا است</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/18570" target="_blank">📅 17:49 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18569">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">حقیقت یاب سنتکام: به‌دنبال گزارش‌های رسانه‌های ایرانی مبنی بر اینکه نیروهای ایرانی به پایگاه التنف در سوریه حمله کرده و نیروهای آمریکایی را اسیر یا کشته‌اند، ستاد فرماندهی مرکزی ایالات متحده (سنتکام) می‌گوید هیچ‌یک از نیروهای آمریکایی در منطقه اخیراً کشته یا اسیر نشده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/18569" target="_blank">📅 17:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18568">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">بر اساس گزارش خبرگزاری رویترز که از منابع مطلع به دست آمده، پاکستان در حال مذاکره برای یک توافق دفاعی گسترده از کویت است، در ازای همکاری در زمینه انرژی.
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/18568" target="_blank">📅 17:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18567">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">قدیمی‌ها یادشونه من اینارو هر روز که کم میشدن قبل جنگ اعلام میکرم
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/18567" target="_blank">📅 17:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18566">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">استوری روز قبل حمله !!!
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/18566" target="_blank">📅 17:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18564">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a267a27341.mp4?token=Hr-9yNFWeUtsRvjTmRo8ZOlZ0pfO9BsKmfWzIh-K5tvpPTFWPAO9ySNz7bwsAOsfwUaHAiEzOYiR8VkXAOxI2bR65FybgcuBWPYsCEYU2e2-Z1Yqvenc7_dvW2UW1-t1hKMk3wGdicfiJx6OtsX7y0ZYgQcl1ln2fdGFWiA6VkZxi310seH0jtP8CEB-aqBTFXz3cIFNl1cZxKSMvrKU46SQB1YKR4tZWab-tuxdPLJ0seoDRZ_TcrkwpBbVhbSz8ZgOYTHhaRmC2hmaJxmP0jVYNHhcChaArCnKvim-sTC5pGbMSbg9zLqwac3Ejh0Vusgz26HaznE4BQdemQ1aCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a267a27341.mp4?token=Hr-9yNFWeUtsRvjTmRo8ZOlZ0pfO9BsKmfWzIh-K5tvpPTFWPAO9ySNz7bwsAOsfwUaHAiEzOYiR8VkXAOxI2bR65FybgcuBWPYsCEYU2e2-Z1Yqvenc7_dvW2UW1-t1hKMk3wGdicfiJx6OtsX7y0ZYgQcl1ln2fdGFWiA6VkZxi310seH0jtP8CEB-aqBTFXz3cIFNl1cZxKSMvrKU46SQB1YKR4tZWab-tuxdPLJ0seoDRZ_TcrkwpBbVhbSz8ZgOYTHhaRmC2hmaJxmP0jVYNHhcChaArCnKvim-sTC5pGbMSbg9zLqwac3Ejh0Vusgz26HaznE4BQdemQ1aCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طبق تصاویر ماهواره‌ای بیش از 20 فروند هواپیمای سوخت رسان آمریکایی حاضر در قطر این کشور را ترک کردند.
چنین اقدام مشابهی در روز های پیش از جنگ نیز مشاهده شده بود.
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/18564" target="_blank">📅 17:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18563">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/18563" target="_blank">📅 17:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18562">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">هم اکنون جمهوری اسلامی بازهم به اربیل حمله پهپادی/موشکی کرد ، همچنین شنیده شده چندین انفجار در این منطقه گزارش و تایید شده
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/18562" target="_blank">📅 16:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18561">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">آی 24 نیوز:ایران از حزب‌الله و سایر گروه‌های متحد در منطقه خواسته است تا در حالت آماده‌باش کامل قرار گیرند،زیرا درگیری‌ها ممکن است در هر لحظه‌ای تمام عیار شوند.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/18561" target="_blank">📅 16:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18560">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f38997170e.mp4?token=rINYAtLkbnkDJwv3AieCWmx3D59kcLDXO2oo9ntuDw-wEBhoY2T5UV7nq9QEXbAkNDY3DYaG1fKdYCBegauTE9xziOobaP4rophezv1dW9etPzO_bBuSz3841JlHt5eO_hpDY6GQIXYoiqhYKxAKMf_hGKrU6DJCaQn3ycP7bnIUrHCGylZHdMoQGiLuL7RmofmQzE5hlnl2rA-Oj6rIACOFGSTZjS3ZH6NKm9SeAHa40oAGEGwYLo8Z7fuBbbAUHRuRvMRr3LPCMh1r2JhkYT6imcd5-iPeHGsY-Qi4Ny2tRsmfd0Q_nFM0sgHiibGsZRwI0HiSvDKzmSAIw0ia2pqQCbqIV4iP9u2lLo69Nn8OIA0TOwLmdGMR7DdIh3G2gMxV8LtOwiWaJbUrpzuRoBLI8nMcFYZJBJqXAlvL0onh6_ew2emp4FMy2l9HVVy9OpuCZxmw08ieLD4cAuXmMd398vMI4g7gfac6F28H1-W9g_sbWGCJ0p_ZT9cOGohG4f1ItI5zI3jgRNbW9tQgkUO7seqxUVMUM5GSmaT1mvcx3ZNmhh614oA5N1to82KoWJqX0RN00NcjE_As_SPRhiuoAQgFR3TAhHvJPoPO2hNDAZc6jpu-odrAfnx8kFLXjdNALy2WXEq8oEh1LAt7Mg8f7egJj7rejESVjVZrb7s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f38997170e.mp4?token=rINYAtLkbnkDJwv3AieCWmx3D59kcLDXO2oo9ntuDw-wEBhoY2T5UV7nq9QEXbAkNDY3DYaG1fKdYCBegauTE9xziOobaP4rophezv1dW9etPzO_bBuSz3841JlHt5eO_hpDY6GQIXYoiqhYKxAKMf_hGKrU6DJCaQn3ycP7bnIUrHCGylZHdMoQGiLuL7RmofmQzE5hlnl2rA-Oj6rIACOFGSTZjS3ZH6NKm9SeAHa40oAGEGwYLo8Z7fuBbbAUHRuRvMRr3LPCMh1r2JhkYT6imcd5-iPeHGsY-Qi4Ny2tRsmfd0Q_nFM0sgHiibGsZRwI0HiSvDKzmSAIw0ia2pqQCbqIV4iP9u2lLo69Nn8OIA0TOwLmdGMR7DdIh3G2gMxV8LtOwiWaJbUrpzuRoBLI8nMcFYZJBJqXAlvL0onh6_ew2emp4FMy2l9HVVy9OpuCZxmw08ieLD4cAuXmMd398vMI4g7gfac6F28H1-W9g_sbWGCJ0p_ZT9cOGohG4f1ItI5zI3jgRNbW9tQgkUO7seqxUVMUM5GSmaT1mvcx3ZNmhh614oA5N1to82KoWJqX0RN00NcjE_As_SPRhiuoAQgFR3TAhHvJPoPO2hNDAZc6jpu-odrAfnx8kFLXjdNALy2WXEq8oEh1LAt7Mg8f7egJj7rejESVjVZrb7s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو شبکه خبر مجری زنگ زده به هتل کرون پلازا عمان و داره جاسوسی می‌کنه ببینه  چی شده
@WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/18560" target="_blank">📅 16:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18559">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">رحیم پور ازغندی نماینده خامنه ای اول در شورای انقلاب فرهنگی:
اگر جنگ نباشد اغتشاشات شروع خواهد شد!!!
@WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/18559" target="_blank">📅 16:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18558">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">سخنگوی سنتکام، به شبکه تلویزیونی الجزیره گفته است که حملات ایران به کشورهای حوزه خلیج فارس «هیچ تأثیر عملیاتی بر نیروهای ما نداشته است»
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/18558" target="_blank">📅 16:05 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18557">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TgovY54a4x0TJeC666iRV9qT6wgnTGEBkwelFlCqm1KkKExLNFV_QbQR4NzYxBaL8r-6P35boQxcJtE9_n14ft5CT0DZpW6QEDxsiHia3zYm40xvXSGjM77xUxn7LhaFdhiCuVc54OKdBYjQMob-M23suVbX4tijGenLi-58OS-J4Ku1u9FKl_m231xSpmBVqbFliDt5qPswJrM_fo1UyUWWZLBem2Fm2JStODTozwlfz3TGjjm2PlJZe9st_Mqp0WKPlLHCr33Mvf6HsSvFtRNCpb9RE_SYYFlJHgS0em8bcfTItVT75On4L2F9hkI-_zq24MRvW_EO5FyByYQ1xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :سخنرانی دیشب بازخورد خیلی خوبی داشت
لایحه «نجات آمریکا» رو تصویب کنید، ممنون
@WarRoom
لایحه «نجات آمریکا» ترامپ (One Big Beautiful Bill)
است. این لایحه حدود
۳.۴ تریلیون دلار
اثر مالی دارد و شامل این موارد است:
کاهش مالیات‌ها، افزایش بودجه مرزی و امنیتی، تقویت ارتش، هزینه‌های انرژی، تمدید برخی معافیت‌های مالیاتی ترامپ، افزایش بودجه اجرای قوانین مهاجرتی، و تغییرات در برنامه‌های دولتی مثل Medicaid و کمک‌های اجتماعی</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/18557" target="_blank">📅 15:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18556">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/18556" target="_blank">📅 15:41 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18555">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">⚔️
💥
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/18555" target="_blank">📅 15:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18554">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">آی‌۲۴نیوز: طی حملات دیشب آمریکا، هفت پل و ایستگاه ریلی قطار در ایران موردهدف قرار گرفتن.
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/18554" target="_blank">📅 15:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18553">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VPJ8fBmOHva7fZWCNaKAmwU8P8KxSOGNsSIGtISkBaoZejUGiusMffPnXevBD-gKhlKI6nRzrvdYnLS_x_1Aj2Eq47zX3nF28ebPb3G-tqH4CPDmXPELWZ__vyAjHrkw5dJ4PedVTohUM59d2nyPS_oeZNHFv1NdwRcFgE28rrjFGTtOhmYHP-WZBGog1FERjvdvN74Uv5-dFPBdDIrb61s-NjoSsBrLR08-0MEfpsLtWT1G2Bt_2SYSCq5rG6m_G81QbaRluSIVOKzkXVGrcFhmtjCJqqz-IiyFeF8c_Wu12jXg9RuKdpJx-HjNqPOV-m_q-ra6WmwSit1F_q8Law.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در بندرعباس مردم قایق‌هایشان را از اسکله بردند و جلوی در خانه پارک کردند!
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/18553" target="_blank">📅 15:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18552">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWarRoom with YASHAR</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Remix Az Asemoon Dare Miad Ye Daste Hoori ~ Otaghe jang</div>
  <div class="tg-doc-extra">Yashar</div>
</div>
<a href="https://t.me/withyashar/18552" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📱
@withyashar
📱
https://instagram.com/yashar</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/18552" target="_blank">📅 15:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18551">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">دولت انگلیس بعد از اضافه کردن سپاه به لیست گروه های تروریستی:
از این پس هرکس در انگلیس از سپاه پاسداران حمایت یا با آن همکاری کند، ممکن است به ۱۴ سال زندان محکوم شود!
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/18551" target="_blank">📅 15:12 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18550">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">المیادین: بزرگ‌ترین شرکت گازیِ طرف قرارداد با یک شرکت گازی آمریکایی در عراق هدف قرار گرفت
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/18550" target="_blank">📅 14:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18549">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">چند گزارش از صدای انفجار ‌در ‌اهواز
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/18549" target="_blank">📅 14:54 · 26 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
