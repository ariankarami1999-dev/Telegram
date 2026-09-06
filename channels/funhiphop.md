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
<img src="https://cdn4.telesco.pe/file/KTCIgV_x2mu-Q8PkexSb_7PT62D8pPPw8clpksNsW4dGuMwta6MLaUn-RMqUyyNV_CsiizrSIj1Og9XCkOHzF1es4D2U5XVBHftJypHVvtnvXOkLooDHP6KC6oq7RM2FOFvJWW2FgiBJhSiY_YPM_gk0Mb432sWvBkQC8RtVprqPAi7gf8sgm6AT9reQFu1sYBPksnaa_Fb-1oGLAjiJbAljYPdMKLAiQ9qdla-kf-LOXekAHVA5S60IgIlWIWtJ3gm0LIxlkTMo2OvAo5lmrcHNLCnKf4Fd4UCleptLYYXr0eQDef5F2WcwfFKqaqJOsXYCmrNIwPeQgU6_bdEpWw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 226K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-15 16:29:26</div>
<hr>

<div class="tg-post" id="msg-83061">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">با گوشیاتون تو شارژ کار نکنید که وضعیت بگاییه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 32 · <a href="https://t.me/funhiphop/83061" target="_blank">📅 16:30 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83060">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b309c1c56.mp4?token=ks1qYYFZ4YAImxwe4Wv6GQciZSgs_enKOs-unbGwrqhLdAn3Pn3D5FEjky3sbXCrLL7SnlJ5boHOs5hfPFnIAd8cNUS0-wP8rSCaZXmtGstqtclyiqDUKLf_-YzqIlfLddoulKG322Q_ZUL_sgSzcGM3X0by_HSJoTyX86fQxdAUG8klgP8yjy0gXOYfkh1OcGi_qQDPfsV7C_5u-c_m38rqPI8g5wFydvoLZRVaAAoyTRpPqXjdnD35XmbD1dZjVBPrs55WBPFMP45bFUlOLmlW2QhebrQI744qiqpCpKgefMzmWziHjw8dnnGt8MOi6PUeHi7ZBCIW4nT_gnl14w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b309c1c56.mp4?token=ks1qYYFZ4YAImxwe4Wv6GQciZSgs_enKOs-unbGwrqhLdAn3Pn3D5FEjky3sbXCrLL7SnlJ5boHOs5hfPFnIAd8cNUS0-wP8rSCaZXmtGstqtclyiqDUKLf_-YzqIlfLddoulKG322Q_ZUL_sgSzcGM3X0by_HSJoTyX86fQxdAUG8klgP8yjy0gXOYfkh1OcGi_qQDPfsV7C_5u-c_m38rqPI8g5wFydvoLZRVaAAoyTRpPqXjdnD35XmbD1dZjVBPrs55WBPFMP45bFUlOLmlW2QhebrQI744qiqpCpKgefMzmWziHjw8dnnGt8MOi6PUeHi7ZBCIW4nT_gnl14w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایلان ماسک به قصد پاره کردن کون اوبر، تاکسی های خودران تسلا رو به بازار عرضه کرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/funhiphop/83060" target="_blank">📅 14:56 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83059">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eYU9vOzKIhQGObRKK41jt4QffUw56g40v26mSAfVgX8LU8nTgqXm3FbYPIpdzDnqNwLGGUa3Q_ZfCmf0lfmvDchZLorEBdb7pz1EqJYThnv1Bm32jz602ZksAgeUECPEAj_TUcabI6F628TIv8-L3OLfFtnSB3d1-8TumCKWMUJa_tDuGF5o-DkT-qyiOlxukGEF2eLJkdxNZVsAqsofybCsvJP_HiEwzO63J5LBnFAv_VcdyQVNQjgtrIijqa3YlAkoZQcQfh0Hw_btpWOEBn73jwCn5lCOBAyScwVsbAyTl-BaieX8RkmrFl5u1zK64y3fs3SULhQBLDTq9XA3GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادمینای خبرگزاری فارس واقعا سطح طنز بالایی دارن.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/funhiphop/83059" target="_blank">📅 13:33 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83058">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">دلار شد ۲۳۰
ایرانخودرو هم اعلام کرده میخواد کصشراشو گرون کنه
عالیه وضعیت
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/83058" target="_blank">📅 11:00 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83057">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLcQHDz9EajinsXF23iED2F-M-nOxMR3e7WTR62asvvz-kKqafNp_DolLWbVquY6T_A10flEPw6W97dvgHKbdY3eTlv-qvGHYMfksw0sjJX8jhg9eJUPOcoNQHoq43HZyZNsL61eKpkKrw8_dSzUFGJ57pzMCE-4lyYfnW6ZIkLA5o4GMVojP-UZILX7vr19liZAEpTACFVN3xMugzDIbqHXKMbd_g1ykdZCxm8lHSNcqOrAJmae_1rUYlNfLfqfZv8BumxHoCd7vcN3kLL8v1hwS03yR6f-224kFG02GbFvhIgxmfwp8JC5OfavQFPHl4uO2ywTIkh53Zmmfify1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گردن نگرفتن همیشه از صفات بارز کیم جونگ اون بوده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/83057" target="_blank">📅 10:51 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83056">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-U7mGuz_XwvbxQoS79f9G_cuXe3pQgSaqc0K4fefmbTItNkz3H3rpy7AG9DJkDRAD4xu8zTW7VJWSFvUWVIPmcbDBFPmh99a_gvJFnTN3sSfHUlN6ezEpqn-JDt1D1ngAbd3Yb0FWpqvs9cJwr6y-bFHSbtyPGfX_jQaphOYx7NMxQFJuKTDVuhKXTzlkPj1EGBLOSCkrya8Qd1aMduxxI2LArW6zNVXYud8JsnIa2Aqx2TIYf6ambx6I0CJc0W0gS-EyuDIScWao-HmSYni5zwEwnLq0eJDmyPePlR_u5dmYnjE4oMl1dLEezaQIGkjaQXwjiXoXO0WyCvd5XC8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
آرسنال
🏴
-
🏴
چلسی
🏆
لیگ برتر انگلیس
🏴
🕔
یکشنبه ساعت ۱۹:۰۰
📍
ورزشگاه امارات
🎲
با بیش از ۶۰۰ نوع آپشن پیش‌بینی
👆
با بالاترین ضرایب پیش‌بینی
📊
نگاهی به آمار دو تیم:
✅
آرسنال
:
۶ برد، ۲ تساوی و ۲ شکست در ۱۰ بازی اخیر.
✅
چلسی
:
۶ برد، ۱ تساوی و ۳ شکست در ۱۰ بازی اخیر.
📈
میانگین گل در ۱۰ بازی اخیر آرسنال: ۲.۹ گل در هر بازی.
📈
میانگین گل در ۱۰ بازی اخیر چلسی: ۴.۴ گل در هر بازی.
🧠
آرامش ذهن، دقیق‌ترین ابزار تحلیل است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r15
💻
@BetForward</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/83056" target="_blank">📅 10:51 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83055">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dba858a3ad.mp4?token=F-0vOvhYVlCbEc3fjw__l6cCyHVWURqZhHXtYJ0NKxOPIQw68sgsIysZNVZVGqu4JBGOEbkTAicdi3cksZfFBWGqc0HpFrB-qZasaQwF9p-ZrDnNpAfEQhGr_vWCw4Y4ZDbOcyMCw4_31y7xaXJ3XNv1Xfxt4jkwBd-3aOfiXPnAOuR9NPu1h9lK-nzjr1kdUOIahniyZIh3ajn1NMB_DkhvMG4bK5tH-zA26RwctqiyrY0qwCfH9Zsl0qmnPWhRD1EHBTtifJbW1YO4vDImsHcz9lPoKngLziWveYoblzn6qy3Ngm8oQUGqODW0ENDALxJadv3sgm3ph7hw9_KjtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dba858a3ad.mp4?token=F-0vOvhYVlCbEc3fjw__l6cCyHVWURqZhHXtYJ0NKxOPIQw68sgsIysZNVZVGqu4JBGOEbkTAicdi3cksZfFBWGqc0HpFrB-qZasaQwF9p-ZrDnNpAfEQhGr_vWCw4Y4ZDbOcyMCw4_31y7xaXJ3XNv1Xfxt4jkwBd-3aOfiXPnAOuR9NPu1h9lK-nzjr1kdUOIahniyZIh3ajn1NMB_DkhvMG4bK5tH-zA26RwctqiyrY0qwCfH9Zsl0qmnPWhRD1EHBTtifJbW1YO4vDImsHcz9lPoKngLziWveYoblzn6qy3Ngm8oQUGqODW0ENDALxJadv3sgm3ph7hw9_KjtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بابک زنجانی یه ربات هوش مصنوعی ساخته بعد تو یه حالت مثلا ما خریم یکیو گذاشته با کنترل کنترلش میکنه، یعنی در اصل اصلا ربات نیست و اسباب بازیه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/83055" target="_blank">📅 10:15 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83054">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ویس فحاشی خداداد</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/funhiphop/83054" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">فحشای خداداد عزیزی به امید عالیشاه.
کصکش پا پرانتزی
😂
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/83054" target="_blank">📅 00:58 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83053">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">قالیباف: بستن تنگه هرمز به ضرر ایران شد.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/83053" target="_blank">📅 00:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83052">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">اگه میخواید عمق فاجعه رو بفهمید باید بهتون بگم که قیمت دلار داره دو برابر قد کاگان میشه در حالی که پارسال همین موقع کاگان ازش بلند تر بود.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/83052" target="_blank">📅 23:40 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83050">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OxMUNY9UuAsvsE6WKYNC8DNTKhzbKe41enMkIEyVX3HvikamX4QZElQQFC2gWpWT1CiK_vTEGecu5VQycJmfkPAnxsJIuVS5-yg9E7wx69fYNO35iQ4YrjgUwZPnowz5wqsi4Nnm3Vb0ZtoO62yD1DHEWUfKfxvmvmEckagIp_GXZrKF1M3W_NtALscfuDLddUdGOkAKHn6wW697IvrlCcfkfNUyvJNr_dIC9B2UKdlJm9cjL9QfvQxEoh284prS9F9oLTdS5BHsMsFfEt04TiXEqYZOrgdjfEl0ruDl_tkNpGIDM-wiiNMR_FTPa7uZtclc8YKN1vdoRWQ51r1wQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EBkMLPlScCSiyfLcMqzDONc7Sd8NAlXISbiLgHc4EWEjBTzOzUN8ZSVbzaCcJbAmlb-o0FGwN6QSFHgs6TMMuMAz9PD0j7nbygitDcG2RfE0ensOhqzPoCpjFqHhWcH1by3ukVeSuCTLZBNkqhLx7kt8Tw6Te5Li9BmsFrhhSJdl9XURPDrEWD1QCuEqXu00bJkPPQBp_sNdts9-QzvW0PmMyhRMFa5iLqaqI12BerdgqaBh8kIEvSnKugLczqv3mVU7z0B0lBTascaXJ8_-3pSI29HpyKBhTNW3-85qS3x2yTeq3RXAzVdXs4txHqZXRmgRHWGKJjtp72JpJOvLww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسین تی‌ام و سجاد شاهی دقیقا تو کدوم زمینه یکن که دارن سر اون یک بودنه باهم دعوا میکنن؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/83050" target="_blank">📅 23:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83049">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">درگیری بین نیرو های انصارلله و نیرو های دولت یمن رخ داده از اون طرفم شبه نظامیای تحت حمایت امارات ریختن دارن حوثی هارو قیچی میکنن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/83049" target="_blank">📅 23:11 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83047">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">رم عجب تیم سکسی ایه</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/83047" target="_blank">📅 22:56 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83046">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">همین الان برق ما رفت
وزیر نیرو : خاموشی‌ های برنامه‌ ریزی شده دیگه تموم شد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/83046" target="_blank">📅 21:56 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83045">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔖
ایونت دو برابری (Double Gig) فعال شد
#⃣
با کمترین قیمت بازار، این چند روز هر چقدر حجم بخرید ۲ برابر تحویل می‌گیرید:
❤️‍🔥
10 گیگ بخرید
💎
20 گیگ تحویل می‌گیرید 20 گیگ بخرید
💎
40 گیگ تحویل می‌گیرید
❤️
سرور اختصاصی، پرسرعت و پایدار فرصت ایونت محدوده، برای دریافت…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/83045" target="_blank">📅 21:51 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83044">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">پویا رحمانی فایتر کار درست و مردمی حریفش مالیخین رو تو سازمان کشتی RAF شکست داد  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/83044" target="_blank">📅 20:56 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83043">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gU-CNIty-ED6_qIdV2NrKPeItn3qzQc6UA74oxxAJ9r8SumShOBfE6kQBGQXecxVeaLji0sxCGDlNnIgSdyp2Zru6WK3py3XpB1d8J-c3A_I6y4PEZaRoTUybvsyRoEaN6Cisk6qDeOOdUw2XJI1eboZ2o01JpWXhJI7VlCcTkK4wp450WyiZSFdDTigF1oRom9SPquTle79oMMFUJl6Cy7gNDxkyWux7H_pWiSh8fmgVtM2Rc2fCjpMBgA4BS58EDJlFSauAz-s7n8T_WhrgpgS-6lINbtEekZEdTzFAFbp2-8odX4b8cans9R4nfZBC_etq649oYElg12tIktgwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پویا رحمانی فایتر کار درست و مردمی حریفش مالیخین رو تو سازمان کشتی RAF شکست داد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/83043" target="_blank">📅 20:52 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83042">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">دلار از تعداد ممبرا بیشتر شد که
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/83042" target="_blank">📅 20:37 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83039">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EA93Oas7fVF9yd4nyYV9_V9Va0kQQVj9g-CjlZiVCjDAOP5LUZqKJpf8YeimSCKCRW9drmQ7tHBnGRrPf_cuaR5-U6rGyaq34noaUlHfKhGtLG18IZ-ZkE33qqsvMpG2H4-FXnapcSRwawR5SHo4pWjtVu6X5Qr3h7-oqvxnHqCf9RkOK5OGtNbsby8-WWpZRC6vGVNOcBilRxflPxwtW1nX1vSH3M3w8kMf329fvX66RtDMHub2m0gfiN4_VjwKhgREcybjNCdeex0KCfGGcSrNW6pGe2u9s30yoNtt04vyLSQbkWRuVOLXqaucno1ZtuyvdJFCtSNTS72AXTK4vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JejyLklXjAlX7ornSvN41e2Sm1OuwwVzBmpfHAUaZeQ6jhbuEYRLabz_YgonfgJsbpw0eh8UXXyFpjby5lyIjipxdIwUHLwb0MZ9VhSNFcjKx6w3Ql4YMc2ENEcmg6O0lwMa1UBuMF03DLzHjxMmfinCv8bl-BcLNrwZKUdRp0ruvIo3g9Uiw610JARIxaK43OisIWe02w4sHD6iswaJozPno05Aah0fzA81FBfS1JWDbA2gehktEkK9UC2GYjNvJTVZ33PGGTen0HBg6dWFl-QyYsZmWYKtsIA6dVwMi1Deoy8l1SgpPATcQ40uXAo_jn09jDgG-7CRYolY6PuUag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GeI6o2rlM1lLe1zc70RjRQvo6VXYh37BvaCguCFF5VdW-FIol5LwrrJJJP5UFlPXRpCvirfmdkvsqCps0SpckFlnEh1WcFsdrtwQTfZTqr87nr5rjhnXnWLurzHYLO7ekc3l2i0VTvm9jpfVXWwlVIEB-cFhMtbq6Wvjm78wggYhivWQb-_wP38WxshaRtpaup_z49GGOpZQVd_jCLHY5IrHTxch-uC38MjQkAN-qmhJoRi6bmmPSU58XlotnioeZcO4kQ5_1CDeF224gIE0VN4DWpiHL6Eg0wbCUTTNOEKy8OkLa9WKJlNcA6GXZE47GOKRbvztmbBqbY5XqJ_OYg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تبریک به فوت فیتیشا
ترند جدید توییتر اینه که دخترا عکس لاک پاهاشونو میزارن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/83039" target="_blank">📅 20:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83037">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔖
ایونت دو برابری (Double Gig) فعال شد
#⃣
با کمترین قیمت بازار، این چند روز هر چقدر حجم بخرید ۲ برابر تحویل می‌گیرید:
❤️‍🔥
10 گیگ بخرید
💎
20 گیگ تحویل می‌گیرید
20 گیگ بخرید
💎
40 گیگ تحویل می‌گیرید
❤️
سرور اختصاصی، پرسرعت و پایدار
فرصت ایونت محدوده، برای دریافت سرور تست و خرید وارد ربات بشید
🤍
🐶
@MaMLiNeT_Bot</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/83037" target="_blank">📅 20:14 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83036">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b8b1d6558.mp4?token=vcrWN8IXBCTQyFq0mn-UuV0KaSbv-4-YU9CGVq0yQ3BpW9dbfG4mgMF4kUWtBinIMls0otEHkTpCDzgsniObsreods7wI8WfpdBfiQUCrXfCxM3hK-hUZk_dBysO4usAK7xoTEr1Sa519qU8rwK7iq_VxqgBsLYE2CUQH_6hwYYm_TaIEx8u5M5XUFNxrln0XfyBy6sbbWK1PukqO8sGe3-IAJcs04s-T6RBecWoHav2Jv9Cln1IhZ3doHsZijQCuTu916_S-Pzv1BiOHEbhKnqwfdwIuE4bLF2MHjaPuQmUXyKReAq0ebVAd8zpzPV10LmyyItxY8utpYHsC7h4zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b8b1d6558.mp4?token=vcrWN8IXBCTQyFq0mn-UuV0KaSbv-4-YU9CGVq0yQ3BpW9dbfG4mgMF4kUWtBinIMls0otEHkTpCDzgsniObsreods7wI8WfpdBfiQUCrXfCxM3hK-hUZk_dBysO4usAK7xoTEr1Sa519qU8rwK7iq_VxqgBsLYE2CUQH_6hwYYm_TaIEx8u5M5XUFNxrln0XfyBy6sbbWK1PukqO8sGe3-IAJcs04s-T6RBecWoHav2Jv9Cln1IhZ3doHsZijQCuTu916_S-Pzv1BiOHEbhKnqwfdwIuE4bLF2MHjaPuQmUXyKReAq0ebVAd8zpzPV10LmyyItxY8utpYHsC7h4zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ بیناموس این بمب اتمو کی میزنی راحت شیم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/83036" target="_blank">📅 19:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83035">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">تاتنهام کصشر ترین تیم فوتبال تاریخه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/83035" target="_blank">📅 19:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83034">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">حاجی یه سر داروخونه برید قیمتارو ببینید دیگه خایه نمیکنید سرما بخورید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/83034" target="_blank">📅 18:43 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83033">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UWCkCGLNOHEr-MGp87N8_AvxmmJlIOMKZcadFx5LPtbUG68fwDurMPpSYFL9LVG2xLB5SUCugMMrbNe5R_GNqDc4q-BsYcCU1IzmhY_479MEtWm79ArxhIblhx_ed38pzHE09e4BrvJ--lM7zHusBcM8pdLpHXi3Do1W5Lln0V3rxw6j-_kJ6_bTo5yyU1etwMdHyYbyss5lBGgNyB1csRvz6BBSbAFLFqew71cvNFSA5gQpSNkUK-4_8d-oYXYXwB8QoSc1pkcc7yBEj3Oib_Ijg9jBKL0SziuRWP1t1K__3lugD9Z5IKjc_4ERSTyVAY1Vh5FV22MacJ9984hyuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدایا منو بک
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/83033" target="_blank">📅 18:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83032">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uT3IcLr00EJF8lojoXiCUINIp0MnKXa9eJ9eWctRwjBwO1Fr_LjOeMhXkuaXn_JEKVGCNvP9JBVGaiY7J-e54Cklc3HeeQGH8I_mOHHqEDIR4HcDaMpSQd93v5PD5zJmp3GzN7o9bZCA7yZfbf6OO26gvU5d-wJ4ySu_Zs3WXOPLuX0GTiQK_D8R41u8hhilbHXxJXsnJ1MMvkWW4vr_NTDgv532Yt8O4mBHO6420RPqDAR7VXitbRNWh_2WEr_F9pb8Ecf8DvISe1gOml_hCuiabzyFlVLAqctWUeC3Ez_bWwnv0wXX2Mj51bSv5jdq_Nvu0iIvUutugyMu9HCIYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
صد درصد بیمه ویژه پیش‌بینی لیگ برتر خلیج فارس
🇮🇷
⚽️
با ثبت حداقل ۵ میلیون ریال پیش‌بینی میکس بر روی رقابت‌‌های جذاب و تماشایی لیگ برتر خلیج فارس ایران، در صورت ناموفق شدن نتیجه، بت‌‌فوروارد در هر روز از رقابت‌های لیگ، ۱۰۰ درصد مبلغ پیش‌بینی را به عنوان اعتبار پیش‌بینی رایگان ورزشی به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bfrd.link/PERG100
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
g14
💻
@BetForward</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/83032" target="_blank">📅 18:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83031">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">دالی  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/83031" target="_blank">📅 18:10 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83030">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">گیمرا قراره به آرزوتون برسید، شایعاتی پخش شده که میگن تو GTA VI سیستم قطع عضو اجرا شده، مثلا با شاتگان به سر یکی شلیک کنی کلش میپاچه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/83030" target="_blank">📅 18:04 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83029">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab1d45c18d.mp4?token=cQOWfaAhNlG-iHWxU9AZxJqjeLTnCpj3wJKgQg8kpqu2GCwevDVZD4QLAERArx0mkdt1NcMKhJms2hiv80eBP9uJAjstBq-ipBtLS_ZFzg1kTajMPMlSAnr2HMkN9ClmfvDNGpDtVb1PCY_KAG8yo5XNnZe6Fv1dH4BVpw_5hf0bhCKRQ41c6FQLJsDbkxkP5n3q88LVu7ghPX_cd3fCOtbV7L8retPwzv6qcmyJ0WFLUCaW-nD74nxcS9ku9p35erfJuqI6goO5ElgoVBl6hnwZjgGp1Rj0426ozntIP5R94ETLWV342LeHZdgl9PCWdiWTqvVQSPAA09aYIsdiIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab1d45c18d.mp4?token=cQOWfaAhNlG-iHWxU9AZxJqjeLTnCpj3wJKgQg8kpqu2GCwevDVZD4QLAERArx0mkdt1NcMKhJms2hiv80eBP9uJAjstBq-ipBtLS_ZFzg1kTajMPMlSAnr2HMkN9ClmfvDNGpDtVb1PCY_KAG8yo5XNnZe6Fv1dH4BVpw_5hf0bhCKRQ41c6FQLJsDbkxkP5n3q88LVu7ghPX_cd3fCOtbV7L8retPwzv6qcmyJ0WFLUCaW-nD74nxcS9ku9p35erfJuqI6goO5ElgoVBl6hnwZjgGp1Rj0426ozntIP5R94ETLWV342LeHZdgl9PCWdiWTqvVQSPAA09aYIsdiIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اژه‌ای به هند سفر کرده و مورد استقبال مردم هند قرار گرفته که یکیشونم رفت و دستشو بوسید‌
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/83029" target="_blank">📅 17:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83028">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ترک جدید حسین تی‌ام به نام "ترور"منتشر شد.  Youtube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/83028" target="_blank">📅 17:13 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83027">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hdBhi9Fk_4tKpyRkNR4LFS4hha4RJFKYzjc3ztXj4maAXYMiQ2ebGfiKRU_qqiv3awuAmkKtqygPMvuwobEI-lbnKLktohHNXdOVAB3C35LXnoPlgQPJuPKeFs3LrAGv3jaOn1nTFlKURRziFW_nS8c-qyrVYJXfZFTysBFdFhTvvPRvfps0ReAlhj2t-Fsc3tNgLuD-Rnk8fcOZAul5tXy1ZwcasXcj82IjJMbVIbNPgT23c9cHxAzhSazWE9tzw-JqaDnN8UnKg1yOYMXuzw9aXnLDPM7s0ib5FKoLi7TVrHdWfsCe9v_1iIdtCi0fnRXGp3KY7k2sdcc1kJh7OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید حسین تی‌ام به نام "ترور"منتشر شد.
Youtub
e
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/83027" target="_blank">📅 17:13 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83026">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">پسر میدونی چیه مملکت از همش عجیب تره، خبرگذاری های یه کشور با فاصله هزاران کیلومتری از ایران بیشتر از آینده اقتصادیمون خبر دارن تا خبرگذاری های داخل کشور خودمون
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/83026" target="_blank">📅 16:50 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83025">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SuKZ3i-lUlRd12DPpxsoH15H0GxKUsfQDBuxNE3zDOVAH96NJME120cVxNk-Kyw45XxVYGx6P3lUaoAcPMleqWSRLHf9hfqY_6VEfD-8tjosERa6p93qScwbwS4vgpg5PAl8VoJEAR7_ucyS29CNPLYsVr5TneDr0rUjiB8WKa_hIOn0Er3Dt7qRsUgSBAPpdC3r3E-NAKxVmlIytGcGORkhwnPURzYUlLuD2i38p8Ss91ch_EGtIfQjn7ugC3X5HQKiWh_n2BPQze4oV6CedddS1GR-RXUT6s052hx3TM3noUd5pxlSqc4hG1uLA80ycDDZ7xuxdVN4cF6YhOq6Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محکومیت دیدی بازهم کاهش یافته و حالا ۱۵روز زودتر و در تاریخ ۵ فوریه ۲۰۲۸ آزاد می‌شه
دیدی پارسال از حبس ابد تبرئه شده بود و به جای ۲۰ سال، به ۴ سال و ۲ ماه زندان محکوم شده بود.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/83025" target="_blank">📅 16:03 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83024">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ISWLYx-AQok4zSfyFR79FarPcMBkDPEZdErXi03waTI7VIAFHGqWuIwl23yQTYYfdJyUyhP78P2UHrpreXrqKKXDkppPBmgUgBS768ReDX3RA15U4xW90-AibRMHUv1D01vOBZbnjcJM_YruVJYvOyeAStY7uRRXSNzeZp9qeKXuMzvxkMiTh-RynuIUc8ao97mqk95QOZ80oJ1AxmB0nE0G3ZCex31oMmpc76HEBLLkAzclcREmGbgtOgYhX4s2Ka2RMY5SsFFW8ruwbU-7Vw2CItXyyorv4BmrvMXJKMqfsIhVV7ZHcVGzjv9vO5UO1uOUVXY0bOZKL4UPVPgCZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
😂
😂
😂
😂
😂
😂
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/83024" target="_blank">📅 15:47 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83023">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">به مناسبت 200k شدن دلار بهش لوح طلایی ندادن؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/83023" target="_blank">📅 15:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83022">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A1JSxZpGphkiYgeE7Leoy--o3XV5Ds212FNMz1za3iW95285BxnwUcsVXgPEr-Sei-GKgrX3sQOM0PAuhPcemV9T4rjV1yVy9yAE9SnnWXTNURaYck4HSg5SbLh4zIWSdCyGOUgETL-rIKeaiz8EJTeDBeO1qlTJBNCrcXE6QpbCxBjEI80d0Elaqxcb-kpHicT2MCJuexfE30MKg__Hb55mZ3oFCkfIDyBqbe2Xi4Rs7Ahf5pGx4cG0Ol5orbNkQZMRHscfJ82-t5fbY4gsfckCD8si5VHUPBWxKm6PHsioVlhsIsyEvrlD76OWufriNDJaBEcViosnHZoRkImSAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دالی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/83022" target="_blank">📅 15:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83021">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">البته در نهایت این دختره کفشه رو خرید و به آرزوش رسید.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/83021" target="_blank">📅 15:11 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83020">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gIDJHTTXAFFpr53TVe7PG2DdnOJbe0rNvaxvqQsLqeYjsNmpcJirKzW5Q99ltQmTmm9AVqhXpZhjhdZnDcfHgC99KJbtcXPB17VWjRo0uGAZBuEg0wVbw6jObfxVk1EkXhWQWwKeD6Dv-pbihmtue-KPRO_XSoe4ljlbnpcBz7qW3TEyQwAF5q2jOA4r071mzIWamAcgaQnQvoBbo8VSoKfKqmNdjdyaU412oQ6JPgf5lBt_IeM304cxPQBIV2PfV_cH-HkAwQkh9eiftab3PWOO_MMr5zstRO8Xo17Yiv83uiofqh4_rObjoATK83faAw42H-zS3M4lQqYFa5oupA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئو این خانم از دیروزه حسابی وایرال شده؛ داستان از این قراره که ایشون واسه خرید یه کفش به قیمت 14 میلیون حسابی برنامه‌ریزی مالی کرده بود ولی بعد افزایش قیمت‌ها، کفشه به 19 میلیون تومن رسیده!  اینم دیگه طاقت نیاورد و پشت فرمون زد زیر گریه  @FunHipHop | چمن…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/83020" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83019">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbd895d17e.mp4?token=qnJSdxNW3swBwyIxmqNmQqb8fp0XcGkaiyuzu1HsVdJA7Il6jBgL9DwhRh7zvDQPQgGsoHUOpKFnEdKtDIet-tyo70dHSO8jICiSTRKsh1x7JyITOnqO97DeMV8joHw9Q3MrhAha0Nua0K_Wqk3MKE77D_1S8IOQcyxRUnUbmwZ21OG2QB62yU8FBNoCN3dkSm7QU_bz5VS3G5O7aMnpDw35ZiDC4LoK-aavyonBgA6QSjCnHToBZ_sw7UL5nNqaioxyRzuVd5eJh7tDcWCqlho7q4w56nDfFfVnGN39llDO-c14e8-e0akEGxEvOfq4GwT5E6XG2qVSORWzbzv_yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbd895d17e.mp4?token=qnJSdxNW3swBwyIxmqNmQqb8fp0XcGkaiyuzu1HsVdJA7Il6jBgL9DwhRh7zvDQPQgGsoHUOpKFnEdKtDIet-tyo70dHSO8jICiSTRKsh1x7JyITOnqO97DeMV8joHw9Q3MrhAha0Nua0K_Wqk3MKE77D_1S8IOQcyxRUnUbmwZ21OG2QB62yU8FBNoCN3dkSm7QU_bz5VS3G5O7aMnpDw35ZiDC4LoK-aavyonBgA6QSjCnHToBZ_sw7UL5nNqaioxyRzuVd5eJh7tDcWCqlho7q4w56nDfFfVnGN39llDO-c14e8-e0akEGxEvOfq4GwT5E6XG2qVSORWzbzv_yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئو این خانم از دیروزه حسابی وایرال شده؛
داستان از این قراره که ایشون واسه خرید یه کفش به قیمت 14 میلیون حسابی برنامه‌ریزی مالی کرده بود ولی بعد افزایش قیمت‌ها، کفشه به 19 میلیون تومن رسیده!
اینم دیگه طاقت نیاورد و پشت فرمون زد زیر گریه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/83019" target="_blank">📅 14:35 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83018">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7770ac79f.mp4?token=GjFqrgqOYS9f5c90QaSMqi0p1NiuGnhlCpBt2Kthv5SIIKYnTk8XWnHfhmsnJXmM3bFGS1CyIwInQzY_4AOmHvEVo-rSJqaEkrnj_jluhSTAt84P9DcbgnbhLk7K8QeET-d5X3q2OTEQBoX_TgBTX88bxHyep-pgrQMGScZA3Y5blcavUjvyARFHdSPQNM7-PCFLOIMX6r9r8y803x3zAv4uXmWLWdFKFyNI7pg6q65uXFVEa6LC1iUx5ZrAk_fHwshfeUgiqq8maz4Z7G4xPrs_HqEfgCq9UNo5_8t3rmI555OmVLozL2pO0bUjc4TUxmssejeQaIdOCW4mKcY-3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7770ac79f.mp4?token=GjFqrgqOYS9f5c90QaSMqi0p1NiuGnhlCpBt2Kthv5SIIKYnTk8XWnHfhmsnJXmM3bFGS1CyIwInQzY_4AOmHvEVo-rSJqaEkrnj_jluhSTAt84P9DcbgnbhLk7K8QeET-d5X3q2OTEQBoX_TgBTX88bxHyep-pgrQMGScZA3Y5blcavUjvyARFHdSPQNM7-PCFLOIMX6r9r8y803x3zAv4uXmWLWdFKFyNI7pg6q65uXFVEa6LC1iUx5ZrAk_fHwshfeUgiqq8maz4Z7G4xPrs_HqEfgCq9UNo5_8t3rmI555OmVLozL2pO0bUjc4TUxmssejeQaIdOCW4mKcY-3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوزجان بیلان یکی از میلیاردهای ترکیه‌ای و مدیرعامل شرکت موسیقی «Muzikonair» امروز وارد ارومیه شد و قرارداد همکاری خودش رو با امیرمحمد امضا کرد.
طبق قرارداد، این پسر به همراه این شرکت مسیر جدیدی از زندگیش رو شروع کرده و قراره برنامه‌های زیادی خارج از ایران انجام بده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/83018" target="_blank">📅 13:47 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83017">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JUT5PWmL0DRv12uvY7ER-ltlXh19U29tQHyHuWg4kcSSBK-7NxklAADjH9wlktaicSACa21O_GZBbnSut5U7nHYgW7pXF_8dIgt4stKeWuJx-c_CZRsBGMbSkLPRnz0ScoXjvR4fNAqLKheO3JOn8HktyYZn4mX8P-Pb7ZAc-KURFfrRw3ixiOOs4KaPpdBTRRGJX4y-rbbSSyAeT-zPoPNF5tNKhFdBYAdY96re0GLvTIPOliEfscxgQBAWNIc9PSHc3aA8Weku5SA-bjFyHKKYPLNS2R9QtEyCR-y7rcsRgk-sCSFuTB-ZOXitXBUpeZeETRC5tsSLzjLsdQKCig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
صد درصد بیمه ویژه پیش‌بینی لیگ برتر خلیج فارس
🇮🇷
⚽️
با ثبت حداقل ۵ میلیون ریال پیش‌بینی میکس بر روی رقابت‌‌های جذاب و تماشایی لیگ برتر خلیج فارس ایران، در صورت ناموفق شدن نتیجه، بت‌‌فوروارد در هر روز از رقابت‌های لیگ، ۱۰۰ درصد مبلغ پیش‌بینی را به عنوان اعتبار پیش‌بینی رایگان ورزشی به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bfrd.link/PERG100
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r14
💻
@BetForward</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/83017" target="_blank">📅 13:47 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83016">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">دلار نزدیک 230.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/83016" target="_blank">📅 13:34 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83015">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZOSWsC3yqbQ7EEdxraaSzON5P9827oCN_TQMyP3dzOpZvKn2P82ezJ10hq-OIv-Ra9dNMhWEV5mSGe32wzPJSFbFX7vX0LuzilhtOqxMDyxpBDCUuttCtNjNXViPLhpVVcm63seHAWFfP1eK1O4xk8JKNgedoqKHewiC_xb8r6rDAk-RGRb8Z9obxxWohJfkfTFlmuIRS2F9lwcxr-MQ_UMN39LUNWMuXCc6dZgof9iYd88LBpG1eEyhGR_z7ZCksMVYY_ETTGmLYP_bSuuHZ1UEygRs4cwGlyt1aPihQc753FxaKDRxzltoJ7sC7J9GMz7gxTE8W2FWVbuyuQ34KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جیبارو سفت بچسبید شاه‌دزدای اصلی دارن میان
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/83015" target="_blank">📅 09:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83014">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">چرا هر شهر کوچیکی میری اسمش پاریس کوچولو عه، بخدا دنیا شهر های دیگه ای هم داره، یکم تنوع بدید مثلا یجارو بزارید لندن کوچولو.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/83014" target="_blank">📅 08:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83013">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ادمین نظرت چیه هیپ هاپو برداری فقد فان رو بزاری بمونه؟</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/83013" target="_blank">📅 02:35 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83012">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16cac9fdec.mp4?token=URwC2Ze5fXbKXgASbrkBA6km8qqNRwcZalk2Ok5jL3eorj0xMXCX8euzYi8xdU7AZCaTvA8EPTrzPIm495aGaW22uB5udji9CaM0J0z1xCBfjRdOoUF9M3kLOVBWXSqD7mwLVJECreQL09DMY6aD3oIe4AKy9nsIL0v7depJnnxxCNTdiigwvMIPbDGkLf9MsFeBpvI_H_1GG4DD_nHjr-GGgOsbPJVbojVW8JH1eNWAyCbsuPIR_tSL5dpNk3MAWZ4pjcXVFk4rY43hBLIruXYI_2yqrSW5WaOdLdv0SKa87Bqz1qohcn2Hh_AiyGgv51Ph6tF9dbmRZyvUvr1EY2gYFdycUch1tq_1Plzseh9HISa3mBom6tla60M9Oz-9anrJ2eVudTL-TYxAGMGOfDIMBu9LLBHQbUyYopVdLTLNg5sfhffw_X_hdKmuJghX5fuyZ5uNr3ANr5efK0dffm61Sn4gutzl4P6Au7n5pDz-f5Mmrq_8Ik0iOh5iBWUOUIZx1xBv7nq2QzeHE-hCAj7do2m_bZQl1QguvFXaYGHQVhCLBqBPodRoAUW6LJstQO-Zo7CBY5I6_S416Pk6GQdtZQiqTnhaXF8Wr9QNlD7x6GeLW5U4N4D7sdfITlS0c3EoVdxP9bQw66AiT7MlO0m866QoT0iNj3BvbPSmmrY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16cac9fdec.mp4?token=URwC2Ze5fXbKXgASbrkBA6km8qqNRwcZalk2Ok5jL3eorj0xMXCX8euzYi8xdU7AZCaTvA8EPTrzPIm495aGaW22uB5udji9CaM0J0z1xCBfjRdOoUF9M3kLOVBWXSqD7mwLVJECreQL09DMY6aD3oIe4AKy9nsIL0v7depJnnxxCNTdiigwvMIPbDGkLf9MsFeBpvI_H_1GG4DD_nHjr-GGgOsbPJVbojVW8JH1eNWAyCbsuPIR_tSL5dpNk3MAWZ4pjcXVFk4rY43hBLIruXYI_2yqrSW5WaOdLdv0SKa87Bqz1qohcn2Hh_AiyGgv51Ph6tF9dbmRZyvUvr1EY2gYFdycUch1tq_1Plzseh9HISa3mBom6tla60M9Oz-9anrJ2eVudTL-TYxAGMGOfDIMBu9LLBHQbUyYopVdLTLNg5sfhffw_X_hdKmuJghX5fuyZ5uNr3ANr5efK0dffm61Sn4gutzl4P6Au7n5pDz-f5Mmrq_8Ik0iOh5iBWUOUIZx1xBv7nq2QzeHE-hCAj7do2m_bZQl1QguvFXaYGHQVhCLBqBPodRoAUW6LJstQO-Zo7CBY5I6_S416Pk6GQdtZQiqTnhaXF8Wr9QNlD7x6GeLW5U4N4D7sdfITlS0c3EoVdxP9bQw66AiT7MlO0m866QoT0iNj3BvbPSmmrY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این یارو زیر یک ثانیه از ناله های پورن استارا تشخیص میده که کی ان، زن و مردم نداره همرو میشناسه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/83012" target="_blank">📅 02:26 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83010">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d117c4a49.mp4?token=oXELTR2Q10QR8IQfSmKdpcRwHiDPjPh3HsHE8NM7SAJlngfD4b0ZfFCBi_Ra1XmJgWU6Q1XLeWv_X9xa-zqDWDEeWmI2u4EYqNoy3_bcHuVXu8YEFUv0YcKeGNuExSNCu85cS6y5h5wTPgcu8vef7UsDKrquybBdC7KJOeO81XyKzt0T6DoYBaAKsvtVnKloysX_UZhw-Ue2_uT06bLrGBi082D7jlP1TfRO-XoRzzrDZCkrgxN2JmFxcVzssncR342yYX5LqQQQoZcaxIX4ojpB-CWUJx8IXNK_M4JUBdkRjHPbrb0k8vrjIqvn48W70uEP3TFhMmvIbHVyiFMdLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d117c4a49.mp4?token=oXELTR2Q10QR8IQfSmKdpcRwHiDPjPh3HsHE8NM7SAJlngfD4b0ZfFCBi_Ra1XmJgWU6Q1XLeWv_X9xa-zqDWDEeWmI2u4EYqNoy3_bcHuVXu8YEFUv0YcKeGNuExSNCu85cS6y5h5wTPgcu8vef7UsDKrquybBdC7KJOeO81XyKzt0T6DoYBaAKsvtVnKloysX_UZhw-Ue2_uT06bLrGBi082D7jlP1TfRO-XoRzzrDZCkrgxN2JmFxcVzssncR342yYX5LqQQQoZcaxIX4ojpB-CWUJx8IXNK_M4JUBdkRjHPbrb0k8vrjIqvn48W70uEP3TFhMmvIbHVyiFMdLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش نگریرا وقتی میبینه ده ساله از فوتبال خداحافظی کرده ولی هربار که رئال میبازه اون مقصر میشه:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/83010" target="_blank">📅 00:56 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83009">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">دوستان رئالی نگران نباشید
از هفته دیگه که رودری به تیم اضافه شه اون موقع رئال واقعی رو میبینید
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/83009" target="_blank">📅 00:37 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83008">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ha80NuYpsJupAGaA6dKZmmb-S_GAhPp-4rOezhHUHYmKZ0W4XQRAxlrvO_NMjutMrcuzwH85d4fqQEb7lD9hakmKLKG4TNl1cEcaViet3qjnbP9rEMt6aPOXtyMWvH-xy3XvGnWBWrsgyC2Ww_nuOrdbCCJ_iQ8m_njOgptELyEad49AOMUqdePgWOvhoVjxwi9gCXS2yQKAYXG4rhenypp4YxJAvN12YxwpxcZhOGD8foPklmzrxtoz1XvRtu-qWz_02-BkDjasL5MG1YqdSicS-Pnsr41I1Ath5Y4NHATfR8SvLpgJEa_MmP1WM7GI6cellFI_r11rtsZdNJ5XyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چنلای عقب مونده ای که این شات هارو میزارید چنلتون و میگید ترب فلان شد بهمان شد، کصخلا ترب یه فروشگاه نیست صرفا یه واسطه اس که مغازه ها جنس هاشون رو میزارن توش و میفروشن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/83008" target="_blank">📅 00:02 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83007">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ولی لاشی با اون صدای بگا رفته هم بهتر خیلیاس
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/83007" target="_blank">📅 23:38 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83006">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">امیر تتلو از زندان بیاد بیرون ببینه حسن بابا چه کسشرایی ازش داده بیرون مادرشو میگاد بخدا.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/83006" target="_blank">📅 23:32 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83005">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0641a73955.mp4?token=vjLrUowsYhv7XUh3Dr4hNZyMqZheyk83zTl9CaWeczBn9wu07NchD6OsoT06vA6ZEIflf236CswoaiwH2uxKi4MqA354AltPLijYJHaEutdN7-y-pD2hhRmrtbbRFmK1qaS-ZDplk3TuAM8rgIzsK4V1BvkD_naXDFxrR-yZ31mPAop3c3WKzhy63xQNLvqWo2Run5SP9dO0oaKkwuwYuUDrisC8JknzgvO4mXEMlb7gMN60UsatCdJ_12ihkS_SWfZLznA1K83ttKc2ddI8Zt2pOm7lckgjqF2yEv6zKqCYnN73SNwtchgKUUpb87DsX7zXjd9Z18lGtJRA5IcSzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0641a73955.mp4?token=vjLrUowsYhv7XUh3Dr4hNZyMqZheyk83zTl9CaWeczBn9wu07NchD6OsoT06vA6ZEIflf236CswoaiwH2uxKi4MqA354AltPLijYJHaEutdN7-y-pD2hhRmrtbbRFmK1qaS-ZDplk3TuAM8rgIzsK4V1BvkD_naXDFxrR-yZ31mPAop3c3WKzhy63xQNLvqWo2Run5SP9dO0oaKkwuwYuUDrisC8JknzgvO4mXEMlb7gMN60UsatCdJ_12ihkS_SWfZLznA1K83ttKc2ddI8Zt2pOm7lckgjqF2yEv6zKqCYnN73SNwtchgKUUpb87DsX7zXjd9Z18lGtJRA5IcSzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترند جدید فضای مجازی دنیا چی باشه خوبه؟
شکستن گوشی و تلویزیون هایی که عکس و فیلم نتانیاهو توشه.
حالا پول اون گوشی و تلویزیونا رو کی داده؟ خودشون.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/83005" target="_blank">📅 23:26 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83004">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A54gYKTWcQ5IgMCip36VnxDzueXqh7AVzIBAWqLMO0awPaIJnwNwbbYnf7lqgO4dNay7TIaqY2i17P-lHcgx81DIjU-VBwExVTj2F-cq4BuRs21r4BEOBpBX-_FdfqUP9M3XepBq6tYHJZONeF4OyxS1Bp5cNPPakLp7AR-VHwZGwmRMtCBhLrL2sZqkFVHIWFxF_2f3nfutKEzDYwk3tcXqBPzR9O7R0X3wrELVHtpoaoknB9iL9GTXYnFMvR147z5b_6tqizY8RpCUQtRaYrLDWo7oA5cXzewvElXebPJL1VGIL36LMo914DRs5sf_8L2Ru7teo89wEXR-Qkefqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا امباپه یک ماشین گلزنی ها اینو گل نکرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/83004" target="_blank">📅 23:21 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83003">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iMx7xEdm71f5N2KhfmrxOrVvBuTfCcdIONdiH2zFOP0kDrdNScI0Au7SPFKoBqXHs_KlFVrThEXKizYYu_lHbx3TRGPyoNZ48XARD_ks4WQnmJBntxVwRaR-8xwRS_1ojjDZZgm8FBiHUQnwPFjZjM2EvCf8GoiqXGGcrGEiAIhBYZ9QeNdw-EvKG3zlMC-t-vYMJdNILrtlw-EoXANpU7pWCQQ3PUACnWHlNvMxriHsfR78J9FpE1PkY297LEMUfMrV4gChLKvCqz5kwiDEeHNHUUssps01fWdDdPupxntts4y24oLx0WtF_Zmm5xRNQ5GUmxR1YtpvN3UdSy9ICQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خستم کردید ناموسا، کیرم تو این زندگی که شما میکنید و ازش راضی اید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/83003" target="_blank">📅 23:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83000">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXX3F5vUotART41UI0rXBdrc0PkRxIh16BJKRZgDSW9ubsI7v1FfBu9scZrGGA4TqP9wcuDHq8OrPQceL_WrTPZiRmEz5gFFbmmsH38_qxkivC2OFsWIo99sZ4X0letqeb_kRJno0xiSVSBlpjWQd0VbrwF56_QLNsKSq5ebN07mjjoDTSWP05knMMkw8UxTkSa3dpVxt6h6jEYOoik6oViWIIWKrwbgx2T95tS70xeVP2RtzHtDPz-KtZxCRyiZbIHQHwxkhsvWwbHJ0prpZ8kApNK1jrRCy42y6OsPp7D0JkPBHxIEO6ILLzoMHXSHKH-X_ZBfv6Q3NT8h95OONQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گاس فرینگ تو مراسم اکران فصل دوم سریال جنتلمن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/83000" target="_blank">📅 21:40 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82998">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">یا علی اوتیسم  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/82998" target="_blank">📅 21:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82997">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cfb0d4b2c.mp4?token=P92zyG5WVaE0dwL4MlQSEOrhmdvUXQkut3Te8CEPDkB-1aRUmI-4j4r6YzFJVVJqelucEJ7tqCCOONg6SxAvg5BKYaZVa7fqTzRTKgELWFSnCKHpUuwWTDzDzwAickQ2VEMw9ePYvMfuizb6i1oaRI2hQz0AsiRKzObKFYRdmh7eG9dMEqxg-RXqaBAiLDM9_mgIjfiyxQFJEiTNvX2fcmRPO0Nl5AzonNwJa69VMNN4WwzXMAwpio-4D68cRVn_Q9WOFrJOHzF6XgREzPz1Rj3yj9pfdEg4xWbjoCOGSm_n8sCnzLUpAzagCwpRR3cpTtGv0oFudaj-nukMTHN7FA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cfb0d4b2c.mp4?token=P92zyG5WVaE0dwL4MlQSEOrhmdvUXQkut3Te8CEPDkB-1aRUmI-4j4r6YzFJVVJqelucEJ7tqCCOONg6SxAvg5BKYaZVa7fqTzRTKgELWFSnCKHpUuwWTDzDzwAickQ2VEMw9ePYvMfuizb6i1oaRI2hQz0AsiRKzObKFYRdmh7eG9dMEqxg-RXqaBAiLDM9_mgIjfiyxQFJEiTNvX2fcmRPO0Nl5AzonNwJa69VMNN4WwzXMAwpio-4D68cRVn_Q9WOFrJOHzF6XgREzPz1Rj3yj9pfdEg4xWbjoCOGSm_n8sCnzLUpAzagCwpRR3cpTtGv0oFudaj-nukMTHN7FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یا علی اوتیسم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/82997" target="_blank">📅 21:15 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82995">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EaTTFfmjzjn3rIjfOUsuHuBk4hOllHQW8FjzKSvfIU5GVC8eV28DyD_1uMNOxl40QY5PP8QhViRdjomCDMMy9BL3ien4lLSoFvdtlE63q6Ir46fwKGAuu9ZkjmoWsy5VAv5Hl7TW33Ps1XzKCrvy03NEiyiJDUetKeH_9NDcIDgqEcOt6VpIzsMC8VI4B39iumMWNbXLmX476n5W30-M66rNaaP68sUHQ73UkJOcxAz3qkuPB9J0gP1PzcqAqd9vlfkmys4bsyTVYX2DBNEsaX_40vMXEY9ypZn52uwgg_pZsmZdo6s2R157iSkC5r3bWSmn9a_5tC88wThy4q8CxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oYBmDHcFQF4M69AVkIYHB--3xAMwUxEg1X4bzDD-LxIJ_tkNnJQEiFV3t3broHXfQtv-BnguPl0UMBknVO_v1USBQ4DJOWvN8CFUd8GggljvIljIUhaHamD8OAFm3UTubvP7dkwlx-zy3U2e3E3Pm-tBD3srvqW84x3y97U_yYLYu-jqIYTGGzlROjsLjsvOGPgvpO6fyA-iw8rDwov4OTHnyCBYrAjhSUNMPpBLP-47QFCz8T-UXRtbxW8pleartcKciApr2GQOeL2vAe5EDYKI0DbrqNQHirEJg4mtsXs55oMhBAoWCUOKUTXVM9tazr3obDTfl3mgwQdHqt73Lg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کاگان این گیفه رو گردن گرفت.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/82995" target="_blank">📅 21:05 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82994">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce693d467f.mp4?token=GAT-Heuqxp-QUDjZ6vUjLu7EB51nZAvF-wUp1laAr24rNHQ-4hsImsNMlnaUPcNVGGM7iEMCVBVm3kKU8zdgjhJQoFuhOjU4YL1eWu-xS3pR02LtfCxRBwyvCXUttLrPhbqaRgX_lkrwnjPRn-OGd0qzwWQXQPDnaVQCNwQZhzqeruSo7QWI0-fBGIfYQasbNcnN21ZJP4ozI3KHUQO8vx22mqIDR5YKbg_UTmhWzMm4gK4D7TVfVeMazD5upbVnYX2IcH26FRmIW0Zz-mLvmsetYmaHC-sdCVKExzY07KgFWXRoK4xz1XJ6EqtuZD9BTJxk70H8t63z6fOYKloEKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce693d467f.mp4?token=GAT-Heuqxp-QUDjZ6vUjLu7EB51nZAvF-wUp1laAr24rNHQ-4hsImsNMlnaUPcNVGGM7iEMCVBVm3kKU8zdgjhJQoFuhOjU4YL1eWu-xS3pR02LtfCxRBwyvCXUttLrPhbqaRgX_lkrwnjPRn-OGd0qzwWQXQPDnaVQCNwQZhzqeruSo7QWI0-fBGIfYQasbNcnN21ZJP4ozI3KHUQO8vx22mqIDR5YKbg_UTmhWzMm4gK4D7TVfVeMazD5upbVnYX2IcH26FRmIW0Zz-mLvmsetYmaHC-sdCVKExzY07KgFWXRoK4xz1XJ6EqtuZD9BTJxk70H8t63z6fOYKloEKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به لطف هموطنای عاقلی که سطح IQ مثبت هزار دارن، لبوبو ایرانیزه شده و وطنی هم وارد بازار شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/82994" target="_blank">📅 20:43 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82993">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">از اصفهان موشک زدن  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/82993" target="_blank">📅 20:30 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82992">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">از اصفهان موشک زدن  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/82992" target="_blank">📅 19:32 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82991">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">از اصفهان موشک زدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/82991" target="_blank">📅 19:29 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82990">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PDGwNOIPz0WDh1rUJ2l_3R9yhbwHbWG8Q-l_LacgcWJRojocRUy4f_4dFc9q2n17yS2I-gkgIOhIckPAwbkTNVWlBlV7ha9rdynBAk4RfPhpig9RQbOQ9IXBydDm2R6TG_MvB5fFeTjN88cJNb3j6U_evCZqRkLtUD4Y57vADxlNFR3TFTRyqvdgft7-p5FCRnZjLHGDtzqMxHsyl9AvOAHaMCilT_cKYlTYWrP5ohE_ZpxILUozHg3GhkOjLnI45H33ZB3R9YjBaVHoysGf7EDs2m3kPt2mHpPS2SJIzlNCmFqFLJ39mJ5F4aTQFifkkbjqA72umjGyVbVHwviANw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوید محمدزاده از تئاتر "آرش" به دلیل استقبال کم مردم اخراج شد  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/82990" target="_blank">📅 19:25 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82989">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">برو مارکت ترکیه خب مشتی، یکی از رپرای خوبمون رفت الان یک اونجاس
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/82989" target="_blank">📅 19:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82988">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kgQOHVlmjCOc1EHh-US9enHvMFAW3UlfvSY42va9KvqC90-UwZ7PD9PrFQSPZeMJFmBfrbnhyhhKGyY5FM60l_SkD3-jVFMtxvCcQ92SwLuTjKraNivGnjzuiAdtK-53B3qmjjoQYe_FNgu8_wsM-ECoiEjax4pLaQYIss-Q9luvwLDXdzfi0ADYRKsSWElKXyiYno46nFshopuWF6TLEzcJeDGld192NtomdDXd7HJOIRTXmriAsH7Fdu8ENFct5migZKI6hOAWH6M-xYUr4LAKOTUMElJ6WVbJt7Xj34ksjWqswPCcZJebRw7_YReY3ErtOyuafMRYBSvw3o8BGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادمینای چنل کوروش
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/82988" target="_blank">📅 19:05 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82987">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6ed68f76d.mp4?token=D030hwg-qer7uUg0bXdOAGQtDlp7--zB9nwOd8OhpET6eBw2l2i2xL-JbUwWw2wDnQunu2CadFfvpmZEyKeDwBjQWQFysdMZTxS0-0GkjgLQmttB2r9m2ZdFwPOKQPwcsUia1MW_bl5ZbLtTFY9bx1f6aVnBZaKwJnJzLefbwtQ56ZDxI-4lWMhlgcbIcJKBtDo7Bm-KW8d7t7RH1iIw0EAvLGmCR60N4Xo25ZammEqNq48hT6BzI7iVtG_II5f0loJBdShzrv_inyYDB5MYhXa6PuH_rFKPH7UTKgO5mbxlI2drw-XiBRVxmep4e7vgw8Yk-x9EAkLHNrNU6e3tEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6ed68f76d.mp4?token=D030hwg-qer7uUg0bXdOAGQtDlp7--zB9nwOd8OhpET6eBw2l2i2xL-JbUwWw2wDnQunu2CadFfvpmZEyKeDwBjQWQFysdMZTxS0-0GkjgLQmttB2r9m2ZdFwPOKQPwcsUia1MW_bl5ZbLtTFY9bx1f6aVnBZaKwJnJzLefbwtQ56ZDxI-4lWMhlgcbIcJKBtDo7Bm-KW8d7t7RH1iIw0EAvLGmCR60N4Xo25ZammEqNq48hT6BzI7iVtG_II5f0loJBdShzrv_inyYDB5MYhXa6PuH_rFKPH7UTKgO5mbxlI2drw-XiBRVxmep4e7vgw8Yk-x9EAkLHNrNU6e3tEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست پاشینیان نخست وزیر ارمنستان تو اینستاش:
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/82987" target="_blank">📅 18:50 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82986">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf87a5e3b1.mp4?token=aBErPgNiY-6-ra66YQ5QHTlOFJWegqSsP18hEnedupnircRbN44yWG5G4_Ubxp6P9WCku_cL0i3Goue62BilybCCYJJiLqx4qMVXnewNaDG6dUxp-ndDxb2F7Eriw-8iRY6Nr13CYEhhXaoBqq8ShjqZpUzslIR1LDb5L0D9SaKu9TPXvk8aCdVd9n3-blKtVgvUJkF6qdI8lp86s1YNqVy-W_h3iJfSBZfsLRI0_acsm97KGI-nMqn3nttthbDTJlIX2KIHlXDTNcYAbKlk1TjfBBOiMYy8Izg_7N_mVZLiUv9filR9yaKbjn0kI0FwwNGOz3rlXyDAHgC3q2n1Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf87a5e3b1.mp4?token=aBErPgNiY-6-ra66YQ5QHTlOFJWegqSsP18hEnedupnircRbN44yWG5G4_Ubxp6P9WCku_cL0i3Goue62BilybCCYJJiLqx4qMVXnewNaDG6dUxp-ndDxb2F7Eriw-8iRY6Nr13CYEhhXaoBqq8ShjqZpUzslIR1LDb5L0D9SaKu9TPXvk8aCdVd9n3-blKtVgvUJkF6qdI8lp86s1YNqVy-W_h3iJfSBZfsLRI0_acsm97KGI-nMqn3nttthbDTJlIX2KIHlXDTNcYAbKlk1TjfBBOiMYy8Izg_7N_mVZLiUv9filR9yaKbjn0kI0FwwNGOz3rlXyDAHgC3q2n1Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آزش آنالیز ببین کاراتو تروخدا
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/82986" target="_blank">📅 18:35 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82985">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ویدیو جدید پخش شده از نازنین بیاتی کف تهران.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/82985" target="_blank">📅 18:22 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82983">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bLzicaU6wTrehAY9-vnzt2AFdZTVsvqvmcTT4mjHdB8G0SWZJRYpTUpZalQ_Ts7tIlU_bvSnb2Kf52kuMnvIXVQf-Loi2LmexWo4UvfI9dVOtXkNCN_q4EhrLrRlST0pZdz6SKfjJr9_kbl3fT629qW-ktLqxJojtFSXdq5gMjwDm1S9XKmYtRS8QgQef0UpIAYgJxwUvjmRSgIa8BB-aPPHKa7r_-3P7et3QTHd16dpWgBzn2yZC-Kl6KEA48VSxtOpw9j1bL4vbQZAYThk3qaE14kjB0_Hsf0Gy_fdBasJyXp1fS9mf_-OiabrScmDmyAFdRUqQ_QxjAGYEV6zog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c34b684e1d.mp4?token=TzWJmChHjpA07lrjA_uI8DDWsOauDSOFwvIVorkawOShCz78BbS8QvrqdEx0Eoakl1NZRXYDLPC1xFkuF8patrBUVdbRhZmEDL_GuuQlZm5gpwnx0ChykYCtaDjYxxj88fOaeaEZ7CmfuxRGwaPYtTdKnEmBWpm1Z0mAVawRrlE3aNJ2vZ2ut16Bhjm3lbtKBIN_9uGT1MSXQQJtihcToXFoMwLH-GJjpx4WQ1YjU8_tfZN81BA7p3cX534RPHm3Ayx8D9jPh1pewFuhp8gSR_irqpkd1sa2LZa3KAyG-tB9aOao3bAbSk3_lLB9v_mf3siJmOdareFlacUn8HB-gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c34b684e1d.mp4?token=TzWJmChHjpA07lrjA_uI8DDWsOauDSOFwvIVorkawOShCz78BbS8QvrqdEx0Eoakl1NZRXYDLPC1xFkuF8patrBUVdbRhZmEDL_GuuQlZm5gpwnx0ChykYCtaDjYxxj88fOaeaEZ7CmfuxRGwaPYtTdKnEmBWpm1Z0mAVawRrlE3aNJ2vZ2ut16Bhjm3lbtKBIN_9uGT1MSXQQJtihcToXFoMwLH-GJjpx4WQ1YjU8_tfZN81BA7p3cX534RPHm3Ayx8D9jPh1pewFuhp8gSR_irqpkd1sa2LZa3KAyG-tB9aOao3bAbSk3_lLB9v_mf3siJmOdareFlacUn8HB-gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو جدید پخش شده از نازنین بیاتی کف تهران.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/82983" target="_blank">📅 17:57 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82981">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PPnkCzNBtTtlv7SDo1v24WUyAXFXihT80motV7OhDMfu_Jv3teYjWdF3GPsQOg26tl2Xvfe9D4tJqfC8r-F3eMbzmL9ih3KdqvJDgafAA7LlCa8xpzrDXeE6-kKYw5R3xR-NOBFy5LpBj_TteqhWskxkBvCLwB8F-SExf2l4hHYQxlGUatHt1i5xNWJ5LSfn1H-1tbtJs1hn14A0xLKsPOzMCMwijoxbCk7nufTZxCHWJ1HzHn5kMoLWU8yHqv5zze43_HN_7f9xR95zey_kGaUBCYnpCutttjqIkWfbLgyRcYcNdG_aNwbn7yUBix7NHhn0NT7nr-WXuVUcJ1prvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید کوروش و سیا به نام “چندتا؟” ریلیز شد.
Spotify
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/82981" target="_blank">📅 16:38 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82980">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/575bec5ffb.mp4?token=WypdSiPb_20mgN8OnR3nIPuMgD4symSmBQSQOU8b8xIcwfbjaYNVSB0c28L5BUuPmYyAj68DR-_lhmCAfoLjGgjv0KFGBSlXUtH_Jkma_-EFYXHd3lthgOAN1VnjsU-vbNsB9T7ikfN-rDmW7iysedbgio6GwToORmJrw3jjTV7Tr9vbB9YecwZgJA5fFD8O0jyYaYz_JsHhEBO3Dqhunl-vKYj0xRGBsmiFda0C12Pep6yucrQAnDG_IBYZrye0hBXAzjc3vKrYbBeDv-Cx8TbUDyH8AI6mSyuoKUS2Qlmdl0Y51NjTjvvRM1cmA9k3BeHvNG3dNH6aWOCKi6aq-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/575bec5ffb.mp4?token=WypdSiPb_20mgN8OnR3nIPuMgD4symSmBQSQOU8b8xIcwfbjaYNVSB0c28L5BUuPmYyAj68DR-_lhmCAfoLjGgjv0KFGBSlXUtH_Jkma_-EFYXHd3lthgOAN1VnjsU-vbNsB9T7ikfN-rDmW7iysedbgio6GwToORmJrw3jjTV7Tr9vbB9YecwZgJA5fFD8O0jyYaYz_JsHhEBO3Dqhunl-vKYj0xRGBsmiFda0C12Pep6yucrQAnDG_IBYZrye0hBXAzjc3vKrYbBeDv-Cx8TbUDyH8AI6mSyuoKUS2Qlmdl0Y51NjTjvvRM1cmA9k3BeHvNG3dNH6aWOCKi6aq-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقال تانک‌ها از ایرانشهر به سمت چابهار
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/82980" target="_blank">📅 16:24 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82979">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ترک جدید بهزاد داورپناه و آیسم به نام "تا بتونم" ریلیز شد. SoundCloud Spotify  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/82979" target="_blank">📅 16:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82977">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hYIWgEMz5YnbEmKq9OKM8J7R1xuC0AbwE1T2smrbDcCzIKXlMDS-Q2rF8W5ocIHZqevp-ii79XutWSt6MVFjPVAcao51Q-J8edPz3PrCGd2fJmR8_l7_XEEJOJ8RuBOVqGAlDEMEGWTXQiw5KU3BZkk5ICn3qQJqS2yukPdoGhGTAIBNeYTs8_6QGUnUtMCEclkgLeMdZqumCBluaWliwdLuvTerczYcdl5rYdJVtNLvFaTZWbYEj14-2f4KouJy1ouvbthwE90fF3xbReNMeM52Q_r69BaLYBNaEWw-kH9WSPGX-CIWpu9D2ePanP9daADHZJJe0qA4rMTZxDP9Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید بهزاد داورپناه و آیسم به نام "تا بتونم" ریلیز شد.
SoundCloud
Spotify
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/82977" target="_blank">📅 16:07 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82976">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BahXJ3bW-9_HJbb6snPpzUTpjOvX8UMhueh8PnM_QyBeRuy7dvBlu-wylHOcd8_qv-Nesgkmx1g2zNMdQYD5MawmFQbyy2HtqZxDybXKTsV75PpYrb_CR5CmSl1kRioRhzJzzNFuB2pNj_XLhlhQdpBG0v_gYf0--6i_4mltDX8eZrZXHHt_IimK-3oAzJGfWzuFYMmXMrzSUjK7mTEtNKwFFtxaBwbbfzA3XNkiexrVxiZh01IAja3C0VuS91a22E6Ae9zNgf_DPU1EVvPmwS1biuCofB8DOj2DMAOjpUqXAZl0g3gpQ0HejwPSeZoz8RL3co4MY7EP5r7XhhiUNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهیار و خار مادرش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/82976" target="_blank">📅 15:49 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82975">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lYGDjhzXulddD65g08_FAmwH_wD-XUr8c8TUEEIWU1VFyOVsvP6mhVjlbVLOGA2Mvcj6wWCXb8ahXloKpckEWbYwR57e9ETp2isGw4vRlxZw7coI6ewxDh_z-9pl5g0AynRy88ScWr4p2Qbx0EfhMwulABYysdBmC8ZWHVCzWWd5pL8MV2kjAWCfmMK1Qz83secgFczdx_iqZaAxG8UOaOYyDtoBDkclPqKQiewICcUZ1keTf-maRNSLtV8JSfvRZrGtA_eXgGseCjH5ZwHknGLKtQvMOKqQcVlb7hBcDH1l-hUlsfg2cOlU6tqTgPcKZqxujnT9ILwVRAUlKUrauQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برا دکتر حسام خوشبختی تو کیر خلاصه میشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/82975" target="_blank">📅 14:37 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82974">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SgrhAA2VWZULoP__IVoKM3eg-4rP4swLVCCdMapfWaG2JJDLIY5ZejwofTMuMduiE4oCbQevj2-j8IyzniovaneGbCeQIPcJuHCa225ZmfskWr2cPKJa1s1GIZIJfeud3oDEqlSViMJ6iq8vmcf3E2df5NbfX9j6fhQsZ1VfwiTnunuKQKL9GlVhPT7dPDPKNUf_KgXcHBMELUyhnqsi0eiL9PQt2y5NwFSmy9-5QtYUQAthpgU96bMt7XsUy5rlE0mPzn7Z-b-S07k8ZrvV3nhoAhpLZOdqUHtKAyWK3x1lr1fqCEZ1Kjhn5PtEzvYZRB928Z7Tnew5eKX4CV8XMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ببخشید عزیزان، کمبود محتوا تو سطح فضای مجازی و رپفارسی واقعا بی‌داد می‌کنه و ما چون دوست نداریم پرامپت و کصشعرای سه سال پیش رو پست کنیم، مجبوریم هر روز به پیج این اسطوره یه سر بزنیم، ممنون از صبوریتون.
🙏
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/82974" target="_blank">📅 13:21 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82973">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">خبرگزاری مهر: موج یکی از انفجارهای ناشی از حملات آمریکا به یه مراسم عروسی تو هرمزگان رسیده و باعث ۵۰ مجروح و ۴ کشته شده.  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/82973" target="_blank">📅 12:50 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82971">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IOory1OydaERdScBRWvDzi3oIt3ND9vDjcPetcX8vDiGtxNUxI6ldDiOC5sY1HRlUNKH8ZSpeonQRdJgprXK1BzSlTLh47B5O74GVFB0PENHv7m-N1kSCucQUI7IXBiAJJ8zWQDdOpE2e3VQUqy-4X9xhgfVViB2bqT1IPhjCZeQw-olnaCNTw3UEHAgBypoXZBOjE_jnzwblp-QuXhjEat_Hn-7LRc6mK7Q7K9zQKMznGAXfFy40slXQoVaE7rTE4K6mo6gUJ8tMZOwxTrqNftT3qAcS8T-pkWc9uF4HNouzBWyx-ipJlAba_kJIIPk6Oq-HVoHrIa0KkGI6n9SZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ad8899803.mp4?token=Lg8u3w6DpnAo8dSjNHcXCNImk_KQVMgMxbSBZp1wGpHOOQu3_-XMyq1fY1fbqzuJlVS2bw0KKQCPFW4QcBlQd_AbK_yjVAfUlfAW4BrrzZScKuxjCGqwZLo4F1nzJrWSjUOEdJ2bXTB_w5M8O5QMBUxWPGupJeCCCgaj4jhk51AUosUFjtsK7gfGPJfJogfYjZ_gKml44w8QdH-q2mi77N0r_aFf23foCqAGqC-oVrmKDi0Iq-LfVpRe-Ce91-rcarJ8bkiXW9xvjE9m6hwVlCz93eWkTWZHGrXUPFL1oQ5TmrxBeCSI7x-Vb4y8DsaxITqoZRJ7vyffuB5fGvQtZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ad8899803.mp4?token=Lg8u3w6DpnAo8dSjNHcXCNImk_KQVMgMxbSBZp1wGpHOOQu3_-XMyq1fY1fbqzuJlVS2bw0KKQCPFW4QcBlQd_AbK_yjVAfUlfAW4BrrzZScKuxjCGqwZLo4F1nzJrWSjUOEdJ2bXTB_w5M8O5QMBUxWPGupJeCCCgaj4jhk51AUosUFjtsK7gfGPJfJogfYjZ_gKml44w8QdH-q2mi77N0r_aFf23foCqAGqC-oVrmKDi0Iq-LfVpRe-Ce91-rcarJ8bkiXW9xvjE9m6hwVlCz93eWkTWZHGrXUPFL1oQ5TmrxBeCSI7x-Vb4y8DsaxITqoZRJ7vyffuB5fGvQtZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بالاخره رسمی شد بچه‌ها، آه از دل‌های شکسته و حسرت‌های ما
💔
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/82971" target="_blank">📅 12:40 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82967">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ای یو علی هستم، ۲۸ ساله از کرج  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/82967" target="_blank">📅 00:56 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82966">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b02f59615.mp4?token=KPtzs1IUkn79bjvISQ1ULmFigrQZB74caQm3R-FcxSRAEm2hpvCN_WMdeFphPzzIAldcDSrURf7J4v5wcUkUIttDEqXJhC9QbY0OsDARybUqA78PFcvWdA1aiBk53z_2GmDmbO2EKMko_yAqhVrJ3ebhz9x0aBLPSKKN4ex_m1zRKa4NbxeZaNkvMHU1T3WUr3zrcEO4ydoWmBuBiPolrffpGOm-X47YCcYy8FWTX32L06JNdxD_geHXuT8k4MBc6xHqzn4r7z8IkwHm76EbibzClcBPV-RngB3-yRN7uHI25swObh9-UqG7Va5WLNuvxECKztaY5bFtpWtR2Bk6bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b02f59615.mp4?token=KPtzs1IUkn79bjvISQ1ULmFigrQZB74caQm3R-FcxSRAEm2hpvCN_WMdeFphPzzIAldcDSrURf7J4v5wcUkUIttDEqXJhC9QbY0OsDARybUqA78PFcvWdA1aiBk53z_2GmDmbO2EKMko_yAqhVrJ3ebhz9x0aBLPSKKN4ex_m1zRKa4NbxeZaNkvMHU1T3WUr3zrcEO4ydoWmBuBiPolrffpGOm-X47YCcYy8FWTX32L06JNdxD_geHXuT8k4MBc6xHqzn4r7z8IkwHm76EbibzClcBPV-RngB3-yRN7uHI25swObh9-UqG7Va5WLNuvxECKztaY5bFtpWtR2Bk6bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ای یو علی هستم، ۲۸ ساله از کرج
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/82966" target="_blank">📅 00:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82965">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c3f3bba65.mp4?token=Ul5t1V0ymlxm-hJd_ChgvPQZBV_m9FjLPW2Y7QhjmeH1bBHZPfB_i8Zd8pHvSQ3FiUO3raV2Ge2SzeoDPxbPNU5gJoo0ru6NFokGFSuW6TqIcG0HfTWKlLaOehcIiXlI4rsXdnrRiN1jXXfWeIPmd_a8gD1EA5-NfEDVJT5pD9S5EdZ2VphS8sQVSBIJUsLdNVaXUGowN9_VzRVVrgCoMEyeQi54fS7J2ZZhdIva-Ku3i80SbGzpBUc77gLkroIlTCImZ5xyULpRX3Gh1IOxWniXkpwSppULKt8e6YSj3mgDG3UJ3EhoiQI3PVnbN3-K2-AlDOadho-m2mcGqEhmWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c3f3bba65.mp4?token=Ul5t1V0ymlxm-hJd_ChgvPQZBV_m9FjLPW2Y7QhjmeH1bBHZPfB_i8Zd8pHvSQ3FiUO3raV2Ge2SzeoDPxbPNU5gJoo0ru6NFokGFSuW6TqIcG0HfTWKlLaOehcIiXlI4rsXdnrRiN1jXXfWeIPmd_a8gD1EA5-NfEDVJT5pD9S5EdZ2VphS8sQVSBIJUsLdNVaXUGowN9_VzRVVrgCoMEyeQi54fS7J2ZZhdIva-Ku3i80SbGzpBUc77gLkroIlTCImZ5xyULpRX3Gh1IOxWniXkpwSppULKt8e6YSj3mgDG3UJ3EhoiQI3PVnbN3-K2-AlDOadho-m2mcGqEhmWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدیو از صفحه رسمی فدراسیون تکواندو ایران منتشر شده به مناسبت گرندپری کره جنوبی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/82965" target="_blank">📅 23:31 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82961">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">اون قسمت از جنوب لبنان که میگفتن اسرائیل حمله کنه میزنیمش
کنترلش دست اسرائیله دیگه</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/82961" target="_blank">📅 22:59 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82959">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HRIR5b5Mj4R1LRXtsLvr8pcoKEKRqBghUr9eif5T8oXD1XHeBuUqtP2W0bQNnPeyirAlWjedCZWK3h-VyOt5rAAuuiPtnaJ9GL2eGHZdUn0QjfqsgeJA0UoaqLwNmVDCvlM8nZ9hBCpfjjUBs7VfkCUmTFPw9Ot96kZCto0hqa55L1lMRMdgeoKBXo5tGRX5ucg_KM_Kp_q9qkJmk5GDn6rEKwls7IeycfRJ0GEnjubHJlTJXp--Ml0MDxMTNGp7m6lwefNerbKGqTKN1yOl7XyQ5bqZsWP-UyrcEbBcEw1LSI2k9ClKozRtTWYlM-HfdiYe0Un0YzZqBRLJJU_hfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکوندی شاه عالی بودی شاه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/82959" target="_blank">📅 22:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82958">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7a86445b0.mp4?token=nZJuxQN35KudMG_AV-ybDyY8j5Dq2z1YnF7-e1kZ-JYphmns_7eE-FOPURnH2Uz3tNnp1pAIzPc-VFjqL2YYxJf9dBYizNeWnMuGDHBmviBVhrpfEGZGPnVOzHrXJKVbwK1PxvVBLW26SzSdz0-F5moDj_joBQnPbQYDWzFk5a4zBHvCtZ7VnLrBKaVDTlU5ZgdpZnVjpphUqux_zY0mJVFWEskxFMKMzr8X9z4l_AAd9hVhIhTelK8Mjg6S6hDksPzWGmfbBlCqDcOsSimygQwYK0Jh4O5q_XBOOcIAyXV3a4DGxXjv9Xxd8LncGL4e18l9Se1ZMNVbyEMXiNckMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7a86445b0.mp4?token=nZJuxQN35KudMG_AV-ybDyY8j5Dq2z1YnF7-e1kZ-JYphmns_7eE-FOPURnH2Uz3tNnp1pAIzPc-VFjqL2YYxJf9dBYizNeWnMuGDHBmviBVhrpfEGZGPnVOzHrXJKVbwK1PxvVBLW26SzSdz0-F5moDj_joBQnPbQYDWzFk5a4zBHvCtZ7VnLrBKaVDTlU5ZgdpZnVjpphUqux_zY0mJVFWEskxFMKMzr8X9z4l_AAd9hVhIhTelK8Mjg6S6hDksPzWGmfbBlCqDcOsSimygQwYK0Jh4O5q_XBOOcIAyXV3a4DGxXjv9Xxd8LncGL4e18l9Se1ZMNVbyEMXiNckMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کافه ها هم مثل طلافروشی ها و صرافی ها جای منو مانیتور گذاشتن که هی بتونن قیمتو عوض کنن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/82958" target="_blank">📅 21:13 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82956">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IGROa3uJ4e5hrDpKMd-yIuaanwmq0AmAa4cIfQUAcXZpzt1x596gM2iTH0Sv0mqN58udx8xfDKFccrvJRsKeh1ecYnvHweXltm7o2k9wd1T6e7e76iD96HJ267gMZupzhhSMraG_V8Pgu7BhM6sN2IZv8BaCw_bPMFCJgIvA44LqnMVbvCHMIEh3Uf5oHjFVIkP98Zl5J3SwUNojWT4HIc4kRsNE9LVY0gllS0HXaHRl__3BE7_BXmEpyReedFJ19Fy8tuGXhrSJ6VVUobXyrJn-CLsGpewMyjjmeHA1TlldowFpFibo9zB1iSFzgv-aIUue_AASJrqx0bx9lYXEIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید دانیال و پیدار به نام "Bipolar" منتشر شد
YouTube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/82956" target="_blank">📅 20:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82955">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gr5qDWsYvMKmuw6PE2fZI3NZH2Dnvd8pdZR29KUP6lFmKo7tHbA2TVVCzhvNj70JzXXL2aJ0f589Z_WJlX7LWU7opG6FxeboQS9nLbm1MX2BjWocQFuu4na5nX4-NEKmpeLdr2A2wAHA0W0rcmGCy4XTNgxGzYl_aipPBUu37ecSrLbaa42NUu9qXurS20SHM9ElnmryLmE7mc8Dzu9nbGj117brVJ-m9Nk45XWjNjhhSl0DuPxL1g0ovDbECE3VXAyG8GLPiSpAcqFA-aP9-ApN-tgObpi3poiSA1ZLjvWax09KzcgHkMyW-bIZ0Ehwt52HwnXftF1fAwULSMY0lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا رامین بد سلیقه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/82955" target="_blank">📅 19:42 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82954">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mTEVZF9WP6ztrH_uKh_y4B0rYLB2JNfxW2K9p7bGk21l2YtOLPXNFaoMRz7GyaHww1uw48P-p-59sGxRRrsa_yV9i6ulvMK25EdFtFigrlSxTJ-T-9IbRRXXo4VhZfYbtKL8o4ZyhOUtYB3RWY7HwvDhR4Y09p5kNUD3pqkuCtNdfPRbn1OSw15saprBUfpvKb5KNjc4nwj3xqZDzuzVbjULBG4GLK41A-5mMDVbJhUv8op46HYVJxAqDDQNTNTmYBmAvyP3s-J4qFKYaC2N2dqow48JcBiKtM4C2hvSLrPT-VJhtw3OB3SU-xQUueiUYBUD_GJFae9LG-ZCI2rbTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینی و پسرش.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/82954" target="_blank">📅 19:12 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82951">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UDsBsL4eBVqO5czkRZ7IprqHfSHVoyBpfu8ddI9zciNEhKoZ6UNzzNWrFt1kTqVVn3iKw8M74P2qE7D6CX4Ggh2Jmt5kf4dSvofxCSEv6yMwk8hlRE-zmNy4rUtAY6dGc9MEeD1xOmL9U_jIzFreJWjNb95hiKhgDukNrp1lp9vSPr8vIBdznRDSDjR0TmJIKEVAsaeoKiVi5w6GYf6S9QK29VegPwd3CMag17buO62su-kHmZeiAxYwmzp-unWKfGQ88OOOxBJvM3QJQ-XD01XPB3Dl6_KoTfbit3q39mEx5hIIHTePXz7LorfV8l6JhwrZCjb_b6QfUrNgqMqCtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4876dd24fb.mp4?token=ZcHTpS0lNCWqEwSg0WUjGpYb0hfLKOYdIv_spHWeoIXXiRZLeALobMyjE6aw13DE7a4RFNEELnLbvz992ZG0t6o-uoDLL0rxLsri8V1pb5S86j2sk0lFoB9XJv8V324VMe0v7Tp4jiKOhmD5ySYoVM4R2QzTPCz329pBrVRZdVlF5eD0LmxrBtTSvf7NkugS0yaWErfAS5QauxXlsZjQUloseIONSwoQ8OizzTp_eTRyK8vgEJAost2dFBjqyjNraqOGoEi-U0geteFTSjHTdSO5XLpWscClNR2rLpMGs0sB2kTSeRr3PvmSuysVDFtyeCnyNDXSvZ4kmeALF4zDEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4876dd24fb.mp4?token=ZcHTpS0lNCWqEwSg0WUjGpYb0hfLKOYdIv_spHWeoIXXiRZLeALobMyjE6aw13DE7a4RFNEELnLbvz992ZG0t6o-uoDLL0rxLsri8V1pb5S86j2sk0lFoB9XJv8V324VMe0v7Tp4jiKOhmD5ySYoVM4R2QzTPCz329pBrVRZdVlF5eD0LmxrBtTSvf7NkugS0yaWErfAS5QauxXlsZjQUloseIONSwoQ8OizzTp_eTRyK8vgEJAost2dFBjqyjNraqOGoEi-U0geteFTSjHTdSO5XLpWscClNR2rLpMGs0sB2kTSeRr3PvmSuysVDFtyeCnyNDXSvZ4kmeALF4zDEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شات های جدید سیدنی سوئینی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/82951" target="_blank">📅 18:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82949">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/shYyywnPVRTNWCI0AGbY26d448Y4Vx4fiysNqyRoLYq0-OY_5CibXRe99lTIHUCuZLnGd96tqVAgumlXfudWfCVAhofmgXZh6RgEdgN5-bNFnWGOCWUfW-T-4x8gr36V9UCCOVobB_WSyojyaoYzSHSjgJng8rhAF_ROMCiq424LgNKFiA_zGamG8U--spCOzcyX1FnNPMCg_wXinUk3ZKdLWY99edsAr4jsA4IsWe6HQkG5tBa0v166rzW8jjmr4h1xvTvbCqajdlPzDQnFYxp9az0WWL-8wxV9xPIxes74wN6ujHW97odJ4CpCUTokOV6ru5Kyg9MqdumfSmdnLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید دلو به نام “منو میشناسی” ریلیز شد.
Soundcloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/82949" target="_blank">📅 17:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82948">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">خلاصه بگم کونمون پارس
ترامپ میخواد پایان جنگ رو اعلام کنه و بزاره بره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/82948" target="_blank">📅 16:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82947">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WPbmZ_ePaTlLlrydzAFUlligl2r9RbG2udCWYn9fGg5x-loNcb8nsvyslN2PmBkwX_oZrlHuP9IavdAExl3vybpQ3TeYZ1lOimLkj5BXMqVNmZx3NKiUf_hcBSG8DMf5-dmgVtJZiA_V1k3n06Qosy8mxUueaoYQ5OBP1HqfTerM7A-YWNyVixZh8yuOZw4dgrisSkYlnbJdz-pLRyqkzuqvmW3EpZzSe7mD_6tD4J5MrWhbRdWioYguzmhsj98bk65orQhzQkKYkQlRVL7kujWOQfqaPYgDD2994JuIrBgY-NQ-Dh2nN2i34u_szq_9-gaKYGBbr0O_BL3MeAGwcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فصل دوم این شاهکار اومد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/82947" target="_blank">📅 15:53 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82946">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c808b4326f.mp4?token=hQQlX92CMSjpVQ4Hq-1h-_QxmimMqnvw8ocUQjVsCRZcmxRiSCFmpgO2d6uwHyRtxOINGHRlD9JduqJo5Ruva1nh4LJ153Bj979Ob0OOlOxrznIsrg9Mc-V0ag4l-UBGHUdXkW22ik4T5rtW2tkY7K0t5iwhX2_J71GBzG-fNWD_wNR4SFW518eZz10OOQQ5rwCQ2aBhTD7B5jxiYsWJhugGXK9lvZUBsShICpPTED9aDaAOhXwwSdxukswXRLOAzcHEdPu5gfcuOBkEZPL79djPaz_i4pQlR3NC10u1_Uxg-ZG97gLMggKGydNINEUgGf5H2G4Uq78n3A3_OsoO0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c808b4326f.mp4?token=hQQlX92CMSjpVQ4Hq-1h-_QxmimMqnvw8ocUQjVsCRZcmxRiSCFmpgO2d6uwHyRtxOINGHRlD9JduqJo5Ruva1nh4LJ153Bj979Ob0OOlOxrznIsrg9Mc-V0ag4l-UBGHUdXkW22ik4T5rtW2tkY7K0t5iwhX2_J71GBzG-fNWD_wNR4SFW518eZz10OOQQ5rwCQ2aBhTD7B5jxiYsWJhugGXK9lvZUBsShICpPTED9aDaAOhXwwSdxukswXRLOAzcHEdPu5gfcuOBkEZPL79djPaz_i4pQlR3NC10u1_Uxg-ZG97gLMggKGydNINEUgGf5H2G4Uq78n3A3_OsoO0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/82946" target="_blank">📅 15:23 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82945">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H4igO8YUUAM0rr_Qr8zvHZv36rTp1q9xbU31M3CNyVGRruX206wSuyLkWWVXcJ4CWIgreGICqzOXAAafSIEhQXtXWBnDXXVTM8couVVRI9hX6w48pMwh4GbRPvXa-Nps77H_Dv_2BG5d93vDo4YcDCsCJdNUrjDloG8mu09KllfT25iTsVnsKL95L3ncOErry9kLQiTCr3CasuxmHP49M7TwpcPU1NJX6ljB3E4y1i86Zit5OPJL1ZSNbY9bFXDtX25_oqcSXElPpKaizJXGngh6QOPTEUxh917uOVsNKw-pVHdYTojll9x6M8ov7WrlEielW44ijJ22qZP00Q7zhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست اکانت تلگرام تو توییتر: امروز احساس میکنم خیلی کیوت شدم، شاید بعداً عکسای نودمو براتون بزارم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/82945" target="_blank">📅 15:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82944">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F7aAXoDIAL0RJpOjzfjCzakaryuDu9J11d9vK2re7xxHFVPsAOxua_gJzP2cX9UHj3m3pinvMmRz6etqbxGo8WJ_c_9ihoqZQnheSOiYfHahrjGMRLH6Y_gYyNd1Dmr7pjpVXuM8MHlkrarJWVad7_mziVqrtY_TevYZvtUF2QILaUxmYulEMT8-lj43dcghsQCN1PsV-eHeae1RAoslL2Z_3I_47fxVYo6mc-UypDRy6VmPoXTpiemC_BYlDFiw1iMF0ypJKRP_IR2ERBVVJXVIyg4Tne6s1KinINJTOQcEXHTE6GvubRN6Mm10BqgoL2t5NoNXq4yYJmte4tfprg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد توافق ونس رو دعوت کنید برا تحصیل بیاد حوزه علمیه قم حاجی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/82944" target="_blank">📅 14:50 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82943">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70a5ddace4.mp4?token=b6nF6wTO7Kwf04vJGzMLe5Kz0VlxGozM21rnIc-YvjiTAZhAkF3X8LnY268NVxJmJjZpi7CKC4IXlldXZzQEhveZVjtYcrany6TnH--3KbWpnBLSN5o9NDf4XIZ2IKcuZV0aLG6LSKtMGf0zYQncsEeU7HV266wiDN30a0aSLilg-bJWVKsi1GwxdI1nSTZia_Mf96dNgakIIjsYb6tYHlRPl2JQ60zWr67N8KRyKLDvNaafW860i3QRw0oj_xyVhrlYtzM1JNm0_igy4xymdRStVV9jUgCoTdKSveb9Y9KVBHl3RpeAG9oEdK2uix5SUswhQopY79Hg8fJgZf0J0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70a5ddace4.mp4?token=b6nF6wTO7Kwf04vJGzMLe5Kz0VlxGozM21rnIc-YvjiTAZhAkF3X8LnY268NVxJmJjZpi7CKC4IXlldXZzQEhveZVjtYcrany6TnH--3KbWpnBLSN5o9NDf4XIZ2IKcuZV0aLG6LSKtMGf0zYQncsEeU7HV266wiDN30a0aSLilg-bJWVKsi1GwxdI1nSTZia_Mf96dNgakIIjsYb6tYHlRPl2JQ60zWr67N8KRyKLDvNaafW860i3QRw0oj_xyVhrlYtzM1JNm0_igy4xymdRStVV9jUgCoTdKSveb9Y9KVBHl3RpeAG9oEdK2uix5SUswhQopY79Hg8fJgZf0J0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی بهت میگن اگه ناراحت باشی عامل خود فروخته دشمنی:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/82943" target="_blank">📅 14:36 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82941">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">حاجی دوران شهید رئیسی، یادش بخیر</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/82941" target="_blank">📅 14:19 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82940">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XaU4IAmSOLCvKGzJa8L_BqumfI61VWkj0Qdk-ZcKWnOzJmD1emLise6LHQgyiJrlwRpV1tlP8eti9JAwc3cUNTfP0PjfD93kj28QbFIt-jGPi-RLFKejpYv55znhDfjqW0ryhPZAiRgTfSEnJij44UOjfveb1uckYdnNIBxHptxvTNLnIKvBYGNW4BpXBU2u3kwa-huxznXS_Lu36t8T-OLOBUXsdX1qGgZvzvVJ_Ex7kc0s9LEe2c7qrYHtfWGLfYoA2BHyDnoAYnPbATg_yMrHk9b6nd2AT17kq7AVmWjVtdht16TB7pcsjYIgKNhCcBY2XXOSsUL84vZGdm2wrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشتی از سنت خجالت بکش این ایموجیا چیه
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/82940" target="_blank">📅 13:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82939">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">یه گدای ایرانی تو ترکیه با  ۵۸ هزار لیر (۲۷۰ میلیون تومن)  پول نقد گرفتن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/82939" target="_blank">📅 13:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82937">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Msa0jjnP-uZSiw6OP-6KnhGXH8qmWa1ged57j0tKB5xSoiiuhYqs2wYrRwkeWQMqizhI4a1G6eUqNhK2eORNYCYre6WMG6dUO4dNqE2kwFvkM263u6wXSCoG0JJb12w4BpVFn1Sy3ZetjJM87A0Ot_rVJF-msJXtBAQrt0g4yNA5nMn2liEGMaVVe2HiCgFsKegwDlwNF3YOMFf8fCVCLISZ-1Mv4tkl3FNnWe7KNEmuGrrARargZ7Cxk_cCsMyPjkoJm3iX-BXXsFp0FI-bwrCaRBd5Tjimk31gkbjACdZsPFT-nx73XLcs7-duBR7vBBotOQJg0o0bPxWUxZfjgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa3cc88bd3.mp4?token=LM-8ixaCXaj3QAXdnwiH4t9dh0-N_MGCpXLYtRtp9Qk1y2XtJz31FctZSBVsCp7bQ46fP_jyUnctD4hp6GGSZ6Su4IeBGVy41u7RgFG9GBT_klyrwxRq3AqOySrX5L5nR6Jq7MtCYEdTSYwlIP1fWhb8UUsy40bDkG5DYy6zdVa7vdJxhu6V8Nyn14yUDPHMuonntyJyB7RsjbmBpGjy2vScvl4XnsUqizzuUgVHWhP_PzBOR4g-FOcbxyws7RTvLq7jXQmwok16l_y0GGMjXJ0ZVOWJqfQJSsdScdCu5Yi5291hl3SPF64aHJiIB13H6zRGDRrw95xHlqxTE6b1nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa3cc88bd3.mp4?token=LM-8ixaCXaj3QAXdnwiH4t9dh0-N_MGCpXLYtRtp9Qk1y2XtJz31FctZSBVsCp7bQ46fP_jyUnctD4hp6GGSZ6Su4IeBGVy41u7RgFG9GBT_klyrwxRq3AqOySrX5L5nR6Jq7MtCYEdTSYwlIP1fWhb8UUsy40bDkG5DYy6zdVa7vdJxhu6V8Nyn14yUDPHMuonntyJyB7RsjbmBpGjy2vScvl4XnsUqizzuUgVHWhP_PzBOR4g-FOcbxyws7RTvLq7jXQmwok16l_y0GGMjXJ0ZVOWJqfQJSsdScdCu5Yi5291hl3SPF64aHJiIB13H6zRGDRrw95xHlqxTE6b1nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست جدید مسی که قبول کرده GOAT خودشه.
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/82937" target="_blank">📅 11:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82936">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TwposS_ejvhUUNu4tPVSJYsRX6SxkAiUFVXXweH-XBQ9coixRRhZkdRQ8dj03cC481mXFoN7EJhH98-zmdVx_5AGBk0PgKhlYIBbquCwpvuC7B_bu2LyI6Lep8LuOtYGHCRsWCxAuNcYR6z4QAjAMQsH5I7_L-HKOeheLHB2b9pdJGG0AN9ixCMlZqB0oTSe5_h7-XSOhZ6GYkgZ4_ud6o7LWYElKUYtC_JuLgT3ScbTLBlcL9FsOKLv8B6OAsnYlAfLjMi4FjdwFD3F0nsuDHVGH9s6johTpE-OxdxdibwX_5yPc3R6WwfDDo0V3iDCODa_qQUU1W_FH90C40HsdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیوید بکهام اینو توی باغچه خودش پرورش داده و به زنش کادوش داد، ایشالا که خیره
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/82936" target="_blank">📅 11:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82934">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TG4XtjCuHavPIJV-Kf8nPp61MvWz8ZcckX1piKoMl7x_NMLzSgZAAAJMnYK22hBWX-J2VBQ9fCP4ovjUUkFIle6qcN7wf5xYTrrT_haapHhFyNQJHzoRfACsQ_6g4IFzWcBWPEN_Y3Yj3pWaLXXIKzUM1WUCvNZTO7eg8157kuz6qajGazzSEzGArmcBqBfP7HPMBGSyaCPnMtaBhUrzG-Q_cVMKkGa9UF3Qr0KMFexuOl6bz_e8jU6FQQlRYdfflU6uLlCioksKOJs4aKfLGCW9oe4jtTpgu3jcZYfdgMlx9LTMmkduz0h0bTdHyPTVhv86C4MCRDTxcGM-kOBFmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرسی نکن پسر تو تازه ازدواج کردی
😐
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/82934" target="_blank">📅 06:19 · 12 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
