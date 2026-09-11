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
<img src="https://cdn4.telesco.pe/file/kq-TLgnxTQKix_8NehwwZtXcnZP_ybdflKCc8zOrPVDPYKKu5sQOM6-OkvAS52GTnX-vdvvD_DjZL4VNgk5QunWhmJr7gZePtOqJhkO2mUd62yB3dk4UrZ5BYMBbEr_F4FK846amyD9xcCxNMI7B_RV7KLapgT18xVQfuaivOrQ_aLAEKE2NDjjkWvuKAeAp89rNWMjGwE3eNJTg4pT9EYYLLc4lvZvzVSLH2trSV4YGSdJeR2LGeGe0g19UBceP-wYSbqAURI2DBZUUOddj46Ve8WQM7P6xtw8HRG57ef3sG9blqzX1wy0ldL-0l2puCW8FwPq2-JdtA873C3QWbw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 925K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-20 15:07:06</div>
<hr>

<div class="tg-post" id="msg-146873">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=fWYyb0FJ5YhRwM-VxMFA9Ut_Lz753GdsE8kUfI7oyhnglW9JNs3XMulcE1FaIQGctUjg1we7JbU0TrNveknb3gGEGWwp0ghtJ36oynrPztYfTIifLBVS10JRr8xtNLF-ecrtLyBSQHNrH1qe-63zGKLQAm4gW931NkRSljDmCO8y_GyicEWVz8phPRbLddD0rKfJI2qm5mZbCo2V3nrOIINQQme78DO_rsI7Q_93-g-buRWAwNPr6GzfHjULWG4UFrQcGOkAetu3zGM_Nccvk4tPH2OmmfzKyag6EOYPC9DQ-qRyRrb_DK9I8M6Er9oqmgB-N3AIwX7g-FZGGYS2qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=fWYyb0FJ5YhRwM-VxMFA9Ut_Lz753GdsE8kUfI7oyhnglW9JNs3XMulcE1FaIQGctUjg1we7JbU0TrNveknb3gGEGWwp0ghtJ36oynrPztYfTIifLBVS10JRr8xtNLF-ecrtLyBSQHNrH1qe-63zGKLQAm4gW931NkRSljDmCO8y_GyicEWVz8phPRbLddD0rKfJI2qm5mZbCo2V3nrOIINQQme78DO_rsI7Q_93-g-buRWAwNPr6GzfHjULWG4UFrQcGOkAetu3zGM_Nccvk4tPH2OmmfzKyag6EOYPC9DQ-qRyRrb_DK9I8M6Er9oqmgB-N3AIwX7g-FZGGYS2qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صدا و سیما:
گازوئیل تو آمریکا ۵ سنت گرون شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/alonews/146873" target="_blank">📅 15:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146872">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5db101496.mp4?token=hHZ7U2x5cFHVLuyh-XoCGVhv8e7q6ElCNUq9SdjFWCFFEjfhf511Wtt2IXP7FrXjZ9jpulVkcJXxtlO_9U9F0bWXppLV1PWx_PbNbN-SvLlmZ3S5IBAOcg3Xs2NYWzwHOorkOinGmlf7GfCfWforF9L9_SIFb6vIL05V0tIIc7rOZzGupNU7frB71OxLs9GObcNF_WSyam7i5zTkH3UmIAl8kbRMc9TglaMa0L33-71zAiiBiInrwRq1Y7ON2VmE-D8jsMq-QCDNHfkFJXAEVhiZktA1faa3kVK7NQVH-08fPszfVYoG9fZAebIIkPXz7seRWsFikzHDgYx9eSPtp2lGTqC2_jMUp7OP21YOFCorcGu0lw9aJBPCOD6XGiZjzj9pxNAG-11wsVzgLzNX3YPfOH7Q8pybAfKUS-cxbawtlIrRvQBxHOnWKYLhMBi4exuM6BApo3NPtp98DMC3rJAOpJn83sbAWurfl0QtLIxpVP568ezHhCiW5J3itLOjx0OuEjp2dpcs-7PcZmBWfuQhdP_YwB9bXdDGzzHUbcq2rzpiVtEYn5lpCTZF9kOLmyMnU9rbtgLW1z5SqZOwpcPNaYx_v1ZvCAcjX03shgYFQ0ZvbUAYygRVlKd4ZV8S1KrF41gw55JQ3pfkbbSrRLqe44mtTyXCplqM15g903k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5db101496.mp4?token=hHZ7U2x5cFHVLuyh-XoCGVhv8e7q6ElCNUq9SdjFWCFFEjfhf511Wtt2IXP7FrXjZ9jpulVkcJXxtlO_9U9F0bWXppLV1PWx_PbNbN-SvLlmZ3S5IBAOcg3Xs2NYWzwHOorkOinGmlf7GfCfWforF9L9_SIFb6vIL05V0tIIc7rOZzGupNU7frB71OxLs9GObcNF_WSyam7i5zTkH3UmIAl8kbRMc9TglaMa0L33-71zAiiBiInrwRq1Y7ON2VmE-D8jsMq-QCDNHfkFJXAEVhiZktA1faa3kVK7NQVH-08fPszfVYoG9fZAebIIkPXz7seRWsFikzHDgYx9eSPtp2lGTqC2_jMUp7OP21YOFCorcGu0lw9aJBPCOD6XGiZjzj9pxNAG-11wsVzgLzNX3YPfOH7Q8pybAfKUS-cxbawtlIrRvQBxHOnWKYLhMBi4exuM6BApo3NPtp98DMC3rJAOpJn83sbAWurfl0QtLIxpVP568ezHhCiW5J3itLOjx0OuEjp2dpcs-7PcZmBWfuQhdP_YwB9bXdDGzzHUbcq2rzpiVtEYn5lpCTZF9kOLmyMnU9rbtgLW1z5SqZOwpcPNaYx_v1ZvCAcjX03shgYFQ0ZvbUAYygRVlKd4ZV8S1KrF41gw55JQ3pfkbbSrRLqe44mtTyXCplqM15g903k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از خودروهای متعلق به نیروهای سعودی و اماراتی که این نیروها در هنگام عقب‌نشینی خود به سمت شهرهای جنوبی، آن‌ها را رها کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/alonews/146872" target="_blank">📅 15:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146871">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
خبرنگار صداوسیما: یک شهپاد آمریکا امروز توسط نیروی دریایی سپاه مورد اصابت قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/146871" target="_blank">📅 14:46 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146869">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jBPb8Rt6BD7YL6f-hRTYbYLW-JunmnxJrJaT05uxj_eZso9wCFfGoFjt-P45-zUj5ovh3KeZ0WBgRX-FXPR_4MHFiCuxTVcN4btln3iJXZw9hwN-GiZVl08Bl6BeTrX-bqcXFe44r9dJfm5fvLcst1_U84yNiM4ooBBRwpTSJf-vVUSQZ1EZS2DKR_GJ8lfyF_9-ovykyga-uw9Szd4uAnM4s9AgzDXV6sAYRUU6utaijuX63b1zfTOKbUmSA2C5LJRGVqsh7BC51Gf7BQpUq1ZXxGy0NntP8uEIYIDQ-QMrEvaD5RWJWyi7pm_v87ISX9rBHr-thivlfIpMRkwABg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KUy0O0tWLkKEUAFnA04JCp2q8y9N7bb3zQX29B8NNOXnKzWldtQMq8wMqcgj8COM-GCLOYm3wGr-_mGN-fsOP6b6wSRLwqrWG2bpHMXr6es6t8P4t68PMBGg_pYlsbulS35wOH9Ze9L2e4wpnWvbhQJYcXRqDtFd3ycIVGjGBAnxmDl8dXvQ62MzbEj0rs-UkFe83Lw3tvLyuZb1roFXVzD0w-wWUlS-1ahwVHORZgd7nZf0ZLAX__i7h8nGr3EmC2OtYQclN-HyxG-Nsj7yIjHo0veo_jUxOBA9g4KRRlRcuwmZg_bKfzfbmPyWoj7vdqstRU4nFxxiqVoOG-DG1w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
انفجارهای ناشی از عملیات اسرائیل همچنان در شهرک اشغالی المنصوری ادامه دارد و از بامداد تاکنون بیش از ۲۰ انفجار در این منطقه ثبت شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/alonews/146869" target="_blank">📅 14:42 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146868">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/faeb6ddc51.mp4?token=m11n1amkcNeAwpLQ5Sn8PcU7cePKhHKNMbRG8oE78PRJU_Dd7W6eni9J1rpAbswHsvvwRx_9xzNimfRAJZ_9XKzBr6Rw0vRNsEyqHsgN-uRMxMuRweFlgwDX3JR2UjQTHYgcotsUiUj2NCZQwlyt8L-52kgELUC9WwQvhzzauIT0eufy0Zxf88wpX2sDGHaXiPVE7LgejwBYViQzzu47XEt3ZHm1Zi6FiHfSfqJK8bLQaEkz0bF4XpRJNP52-DlciZcAK353WvhF8OFwXPfI0YBw5OlvuWKZLSAEl3rRSz3motfIaHlNd1ox-_EigVGU2KDYQ8HJQiWskXav5gqr5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/faeb6ddc51.mp4?token=m11n1amkcNeAwpLQ5Sn8PcU7cePKhHKNMbRG8oE78PRJU_Dd7W6eni9J1rpAbswHsvvwRx_9xzNimfRAJZ_9XKzBr6Rw0vRNsEyqHsgN-uRMxMuRweFlgwDX3JR2UjQTHYgcotsUiUj2NCZQwlyt8L-52kgELUC9WwQvhzzauIT0eufy0Zxf88wpX2sDGHaXiPVE7LgejwBYViQzzu47XEt3ZHm1Zi6FiHfSfqJK8bLQaEkz0bF4XpRJNP52-DlciZcAK353WvhF8OFwXPfI0YBw5OlvuWKZLSAEl3rRSz3motfIaHlNd1ox-_EigVGU2KDYQ8HJQiWskXav5gqr5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ولادیمیر پوتین پیش از برگزاری نشست سران بریکس، با نارندرا مودی در دهلی‌نو دیدار کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/146868" target="_blank">📅 14:36 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146867">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
اکسیوس: فرمانده سنتکام برای بررسی پیشروی‌های انصارالله به عربستان سفر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/146867" target="_blank">📅 14:36 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146866">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YGD6K2A_qB05pbUyd7ZPu-U71Bbb71zYTCBiTmge7IGrEd5BMmePSp511OFeeRMLQpUL5dKCnvkFMyJmJ43ckYEYgyJDgAoGhowWNqGN9_XWlNfx83-NI9t_hUVKC_TCC6yWeqwZj-rGDWLknxiYShj-Tp8Gmb2pQrXh2_PbneigJwLYOnI_d1h5WbspRM7_JmuUb3IZh3oX3BOefKxdYCu7irTmN6pdkwQGG9WMLpJqdfHyT-ZtxzJhqLFotUc0CHYyKCPmTNoO86kdSqCsyKsQVZCZsn_m0kv5yPOsXL1oWYVG-tiBPIsiR313pssNncOtVns9WqLv-Djd9JZJ3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بلومبرگ: به دلیل جنگ‌ های ایران و اوکراین تولید نفت خام ریاض و مسکو مجموعا در ماه گذشته حدود ۵.۵ میلیون بشکه در روز کمتر از ژانویه ثبت شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/146866" target="_blank">📅 14:22 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146865">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b97ba68995.mp4?token=QktY6uGqeRobWrD82S1zPOKj7H1K6sKCUUKkyI8ZE7FRR9I9yuF2ejeZpZlSgxKsYMPx4_F0ynDIsg-NAz5kgyFWADdSvngbiOBIbNcQ3EltyhCRXzix-ZIKwN-vehY-KSWpkuEE22yziHwREe6AhJy9slA8gnuUo0nEkK1f4M5QtjA4zkHjlwjmOuQHBLTh0goCBJsIcgnLFpPuvcm3z51OKSI8oM9yH48UANR784bu3S_LnM6FOms81fA6Ny4A_gsXm26ickq68L7cBht1T0A569zNfqIu312h2wO2V3L0KZmArpbhi1-lzzE6icSTVQk8WUz2G9PMQtdwEmRV4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b97ba68995.mp4?token=QktY6uGqeRobWrD82S1zPOKj7H1K6sKCUUKkyI8ZE7FRR9I9yuF2ejeZpZlSgxKsYMPx4_F0ynDIsg-NAz5kgyFWADdSvngbiOBIbNcQ3EltyhCRXzix-ZIKwN-vehY-KSWpkuEE22yziHwREe6AhJy9slA8gnuUo0nEkK1f4M5QtjA4zkHjlwjmOuQHBLTh0goCBJsIcgnLFpPuvcm3z51OKSI8oM9yH48UANR784bu3S_LnM6FOms81fA6Ny4A_gsXm26ickq68L7cBht1T0A569zNfqIu312h2wO2V3L0KZmArpbhi1-lzzE6icSTVQk8WUz2G9PMQtdwEmRV4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: آیا نگرانی‌هایی در مورد این دارید که هوش مصنوعی ممکن است منجر به انقراض انسان شود؟
🔴
ترامپ: خیر، من هیچ نگرانی‌ای در این باره ندارم. نگرانی من این است که اگر ما در زمینه هوش مصنوعی پیروز نشویم، در موقعیت بسیار بدی قرار خواهیم گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/146865" target="_blank">📅 14:18 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146864">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
ترامپ : لطفاً دست راست خود را بالا ببرید: «من به بزرگترین رئیس جمهور در تاریخ ایالات متحده، که ما را آنقدر دوست دارد که حتی نمی‌تواند نفس بکشد، تعهد می‌دهم که من با خانواده‌ام، با دوستانم، به هر شکلی که شده، این کار را انجام خواهم داد - مهم نیست که آیا ثبت نام کرده‌ام یا نه، من تمام تلاشم را خواهم کرد تا مانند آن‌ها تقلب کنم... من خواهم رفت و رأی خواهم داد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/146864" target="_blank">📅 14:18 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146863">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ca989d528.mp4?token=AicuX37NC4mcoG2gj7TyfIcUVxGSPcHWimF4EcN-LzScGV5QpUrUeLN3ZuhKA2r9ovHorYUgf1KfwmFSPlwiQPSbERIW3ouWZGw6F73U6oTZMELiDk_YcagjX0lE7uACLKxqDIfi0DUrHO5egeugh2Eo-PRrHPnUD5A05b4F1Zfh3vG9_VLj_nWW9L7dg5vN1EKpmxZqXFUyClxoCd-wl8_ekeUnxfgc2bu9wpFyKVIhuY19HIQ13_5xNuu8BqguZX-Yh9wlN_z3q3y4bUc9upitEWuLvKE5IWxofMtT69xjh_fyey9ROCZ-UVTacVDyYRSERQYSlCth5qREUaGjlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ca989d528.mp4?token=AicuX37NC4mcoG2gj7TyfIcUVxGSPcHWimF4EcN-LzScGV5QpUrUeLN3ZuhKA2r9ovHorYUgf1KfwmFSPlwiQPSbERIW3ouWZGw6F73U6oTZMELiDk_YcagjX0lE7uACLKxqDIfi0DUrHO5egeugh2Eo-PRrHPnUD5A05b4F1Zfh3vG9_VLj_nWW9L7dg5vN1EKpmxZqXFUyClxoCd-wl8_ekeUnxfgc2bu9wpFyKVIhuY19HIQ13_5xNuu8BqguZX-Yh9wlN_z3q3y4bUc9upitEWuLvKE5IWxofMtT69xjh_fyey9ROCZ-UVTacVDyYRSERQYSlCth5qREUaGjlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: ما تنگه را کنترل می‌کنیم. من آن را "تنگه ترامپ" می‌نامم
🔴
ما "تنگه ترامپ" را کنترل می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/alonews/146863" target="_blank">📅 14:17 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146862">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64134abd7d.mp4?token=aI01aiGeIoNlyqenuQVm_02r2LYJIhI96e5AyLuVcuFfDb9ULPaTpBSYkTujV1wRUixh5ssHufEiBoOFaelm8wMctxAgl4kenFm9hvJbWvsWMFGX6l8fVcDIrABCmheNvsfUXRS7KcyX3UJkhCMxbVIIECDcXNQDRXtzIL1qhSQyzGFORZevchTjNWVUW9gtTqAbUMLwsCG3YMLUPiX1btBxRIhdjTwokdh5VFGvGH8piAnkg6411sZRUzZVMHyfdQHMpou5pfbUAT2KoW8gwJ2qf6wWUuV6IajyJ5y42Gs21t1sZYdedemocTJg5-NFINIifZEfn7K4L2U8tnQEgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64134abd7d.mp4?token=aI01aiGeIoNlyqenuQVm_02r2LYJIhI96e5AyLuVcuFfDb9ULPaTpBSYkTujV1wRUixh5ssHufEiBoOFaelm8wMctxAgl4kenFm9hvJbWvsWMFGX6l8fVcDIrABCmheNvsfUXRS7KcyX3UJkhCMxbVIIECDcXNQDRXtzIL1qhSQyzGFORZevchTjNWVUW9gtTqAbUMLwsCG3YMLUPiX1btBxRIhdjTwokdh5VFGvGH8piAnkg6411sZRUzZVMHyfdQHMpou5pfbUAT2KoW8gwJ2qf6wWUuV6IajyJ5y42Gs21t1sZYdedemocTJg5-NFINIifZEfn7K4L2U8tnQEgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : ما کنترل منابع نفتی ونزوئلا را در دست گرفتیم - ۶۵ میلیارد بشکه نفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/146862" target="_blank">📅 14:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146861">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/566fe0667f.mp4?token=lXp12xOEMGOoS0pada7iNmlRJJbfabMeEJOKy5tN7nGw0mncyMOfd44bPNYoyx3vAetwsTDW0tPMCy9h1hzzcnrs6buoatj5SgyjY0KXkwd2PFQG7-u_vyjQokjs3D2pjk4jutVzebRHBIL7REVpoN1KkfiABeFxmp1JP4L-KEewYGO5wDM5zRaRBfcTzExUws8glMj_szBGzi8eQyHfZlxLkyoC61Gc05IlHly9saoM-8AqWrE3fZrM0XM99yySosuD7tH6iSv1RcVdnoFuRFxWTopmQ7ae_rNpMpL30JlMiuCqYCsFzU2xJP1XNukAm70T9cv6jxdR6n_SQ5HOSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/566fe0667f.mp4?token=lXp12xOEMGOoS0pada7iNmlRJJbfabMeEJOKy5tN7nGw0mncyMOfd44bPNYoyx3vAetwsTDW0tPMCy9h1hzzcnrs6buoatj5SgyjY0KXkwd2PFQG7-u_vyjQokjs3D2pjk4jutVzebRHBIL7REVpoN1KkfiABeFxmp1JP4L-KEewYGO5wDM5zRaRBfcTzExUws8glMj_szBGzi8eQyHfZlxLkyoC61Gc05IlHly9saoM-8AqWrE3fZrM0XM99yySosuD7tH6iSv1RcVdnoFuRFxWTopmQ7ae_rNpMpL30JlMiuCqYCsFzU2xJP1XNukAm70T9cv6jxdR6n_SQ5HOSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: شما می‌دانید چه اتفاقی می‌افتد اگر رای ندهید: شما به جهنم می‌روید.
🔴
من نمی‌خواهم این اتفاق برای شما بیفتد، پس لطفاً بروید و رای دهید
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/146861" target="_blank">📅 14:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146860">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
اکسیوس:فرمانده فرماندهی مرکزی ایالات متحده دیروز، پنجشنبه، به عربستان سعودی سفر کرد تا جلسات اضطراری درباره پیشرفت‌هایی که حوثی‌ها در یمن داشته‌اند، برگزار کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/146860" target="_blank">📅 14:08 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146859">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
وزیر دارایی اسرائیل، درباره ایران:
«در نهایت، ترامپ کاری را انجام داد که هیچ رئیس‌جمهوری پیش از او انجام نداده بود. ما در این کار، شانه‌به‌شانه یکدیگر پیش رفتیم.
🔴
او این کار را در شرایطی انجام داد که تنها ۴۰ درصد از مردم آمریکا از آن حمایت می‌کردند.
🔴
من سیاستمداران زیادی را نمی‌شناسم که حاضر باشند برخلاف پایگاه سیاسی خود عمل کنند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/alonews/146859" target="_blank">📅 14:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146858">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebf8674ee4.mp4?token=TovOl9SlEXmUKuiBszxOFtMjrFymW45msc81w_UmJokIcEBuJv0BDSTWtOnOLnWs811qisV-s2IOVyOGSXkLMeaAVntClPBYroXAuZs8HYxX4fipZNtk5iHtEB3Edd97wVtTCMnQWWudq2MGCw-ryXwbiWhxXHtJW9KUE-cydH6upG9Aw97rggC8X8vFcJcEPMAWQ4dyP9AB7eTKDoA4XWKmaQ9RfK77s5HT5og7GPSn_AdCKqamjicuJvynWDtaUK5yF3crNOJ-J9jx6qkcEXOP-oeo_rH2GG9gPYL4J972y9PH6lf7SoLZ6NhYy648jv27nzCBaXW8-i2PniaMsnx6CaLYEWCzZWOvUhDOTMtOBDGJRmvwqa7cJA797FBgVcDkmpMF4dIyMF5Jnol-nq9q2naKrJkh4_4b23-Qc1CXh_vXK2ggDQh95z5bcp6OyjzliKASiK8AIYpdtu6kf-DHYO-OJDV_agqWBOAoO9d1k6TvFcO_oWyRDi1ct-CcT6Fkp6DTJLHl-vo4bBZvPQ5Gxy2BOd2HompUU-mkQs4Nh-xB66asai1aMYicfdaNd-lSH_-kmfGj7b64X2PYqnCl3Wf9rCRRoxOupnnOseDl43jPfS2itxo-MsymU4twKVZvWJ-xdnRRD34Bjoot__j6S-HVKZYhi4QGmOUoWts" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebf8674ee4.mp4?token=TovOl9SlEXmUKuiBszxOFtMjrFymW45msc81w_UmJokIcEBuJv0BDSTWtOnOLnWs811qisV-s2IOVyOGSXkLMeaAVntClPBYroXAuZs8HYxX4fipZNtk5iHtEB3Edd97wVtTCMnQWWudq2MGCw-ryXwbiWhxXHtJW9KUE-cydH6upG9Aw97rggC8X8vFcJcEPMAWQ4dyP9AB7eTKDoA4XWKmaQ9RfK77s5HT5og7GPSn_AdCKqamjicuJvynWDtaUK5yF3crNOJ-J9jx6qkcEXOP-oeo_rH2GG9gPYL4J972y9PH6lf7SoLZ6NhYy648jv27nzCBaXW8-i2PniaMsnx6CaLYEWCzZWOvUhDOTMtOBDGJRmvwqa7cJA797FBgVcDkmpMF4dIyMF5Jnol-nq9q2naKrJkh4_4b23-Qc1CXh_vXK2ggDQh95z5bcp6OyjzliKASiK8AIYpdtu6kf-DHYO-OJDV_agqWBOAoO9d1k6TvFcO_oWyRDi1ct-CcT6Fkp6DTJLHl-vo4bBZvPQ5Gxy2BOd2HompUU-mkQs4Nh-xB66asai1aMYicfdaNd-lSH_-kmfGj7b64X2PYqnCl3Wf9rCRRoxOupnnOseDl43jPfS2itxo-MsymU4twKVZvWJ-xdnRRD34Bjoot__j6S-HVKZYhi4QGmOUoWts" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بزالل اسموتریچ، وزیر دارایی اسرائیل، درباره ایران
:
«اگر ایران به ما حمله کند، ما به‌سادگی تمام تأسیسات انرژی آن را نابود خواهیم کرد؛ حتی تأسیسات داخلی.
🔴
نفت، گاز، پالایشگاه‌ها؛ ایران دیگر چیز زیادی ندارد، اما هرچه باقی مانده باشد.
این کار می‌تواند یک کشور را به فروپاشی بکشاند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/146858" target="_blank">📅 13:56 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146857">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2ae746b81.mp4?token=FNOeic67WzFiIru0DCIVArcIcxkLLMYmLJu8G7GvDbhnv-onCv8anPId6A7-E-TSvh3OVNKuDoIGUZil8sEJxmguIrlKJWAJM2AhZeam7azX24wwx3GvSvr5lTDSepMQupYQ2q3cwmBxhRKCUViw0zfUXupXDYIjrDK8nrybl6izwQsLNjZlm1TjMQceeYjl6m9U5g14CIEAeB7iM6Gb7KbF3nBYO_jDRWnp4vMTtPbPhkX0pua2lCn9Qs6o6waEh9XOwkzhdglWxJkmXCkQhXNWuNEaCN1xm0qNia4finuyC8D0NoWiLWpnI07ETAfiwQtH3gilhBGLi27nWuOx3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2ae746b81.mp4?token=FNOeic67WzFiIru0DCIVArcIcxkLLMYmLJu8G7GvDbhnv-onCv8anPId6A7-E-TSvh3OVNKuDoIGUZil8sEJxmguIrlKJWAJM2AhZeam7azX24wwx3GvSvr5lTDSepMQupYQ2q3cwmBxhRKCUViw0zfUXupXDYIjrDK8nrybl6izwQsLNjZlm1TjMQceeYjl6m9U5g14CIEAeB7iM6Gb7KbF3nBYO_jDRWnp4vMTtPbPhkX0pua2lCn9Qs6o6waEh9XOwkzhdglWxJkmXCkQhXNWuNEaCN1xm0qNia4finuyC8D0NoWiLWpnI07ETAfiwQtH3gilhBGLi27nWuOx3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بزالل اسموتریچ، وزیر دارایی اسرائیل، درباره ایران: «ما تحت فشار نیستیم. ترامپ تمام زمان دنیا را در اختیار دارد و
ما هم تمام زمان دنیا را داریم
؛ این آنها هستند که تحت فشار قرار دارند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/146857" target="_blank">📅 13:55 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146856">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f2c659dfc.mp4?token=r-Ehke8FTBtGccbw7dbYQOxV3HXNBpFKnWXOYHkvvTnzNC2gV7pKy9Q-eN0_xy8W9vuRaOaV1m81aoVpb4ydg3vlZ9PqDlOZ3xpvYQk9qsfbegNIWnk68eJYQQdChmmVx9EuGpBPd22-rIDYz1ygvfyEG6uFtXp60w_BYtOWxTBjuLAXCAOnv0wJ7TrUhOyCY-8A5-rxhnZCc7B7kSo40D_5j23cDckAaU55m7K2MTaYPa6bz3I6I5DqMOHx03X2sJwIX7D3sXEvJnX9Qv3gqYvPbl43vF4xXdYHIYh64xVahIF66Y2ujP50vagVIhIxZ5lZcf2sRkmjA1lyUCTXVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f2c659dfc.mp4?token=r-Ehke8FTBtGccbw7dbYQOxV3HXNBpFKnWXOYHkvvTnzNC2gV7pKy9Q-eN0_xy8W9vuRaOaV1m81aoVpb4ydg3vlZ9PqDlOZ3xpvYQk9qsfbegNIWnk68eJYQQdChmmVx9EuGpBPd22-rIDYz1ygvfyEG6uFtXp60w_BYtOWxTBjuLAXCAOnv0wJ7TrUhOyCY-8A5-rxhnZCc7B7kSo40D_5j23cDckAaU55m7K2MTaYPa6bz3I6I5DqMOHx03X2sJwIX7D3sXEvJnX9Qv3gqYvPbl43vF4xXdYHIYh64xVahIF66Y2ujP50vagVIhIxZ5lZcf2sRkmjA1lyUCTXVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بنیامین نتانیاهو: «هیچ زمینه و توجیهی برای زنده‌زنده سوزاندن خانواده‌ها وجود ندارد.
🔴
هیچ گلایه یا نارضایتی‌ای نمی‌تواند قتل عمدی افراد بی‌گناه را توجیه کند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/146856" target="_blank">📅 13:49 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146855">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0f323683f.mp4?token=BGGELqsJMdokj0p5ttgKxWkyYSSfWGMSF-6hSbNI4yU9fnHoQLQLU87uRUyMQ4IJnp5jpgva-6cKXm1vlCJcEgvCudo-jokABX6uG8pOL3_D6CMX_ZZFETmm2Zy6dPVWH-0cV9qIzyboghSrTfvQapmIZK244RsEJTDVj-h4nQPHTjoeddMMdC96q14dJkSQbu9aL2hCkyZUtmGtGZjD9mX76Vq-TIJLqGJaQfdhf7Mb0YVf-tOOJ8m62yro1W5AaI25qjupMQ3qpYp6I9JLDrc_if5XNNOb-01BvVg10TMQfgg8EZCmxLjfwnRrpdoOzbzrN9ryfaKddzQkNovINA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0f323683f.mp4?token=BGGELqsJMdokj0p5ttgKxWkyYSSfWGMSF-6hSbNI4yU9fnHoQLQLU87uRUyMQ4IJnp5jpgva-6cKXm1vlCJcEgvCudo-jokABX6uG8pOL3_D6CMX_ZZFETmm2Zy6dPVWH-0cV9qIzyboghSrTfvQapmIZK244RsEJTDVj-h4nQPHTjoeddMMdC96q14dJkSQbu9aL2hCkyZUtmGtGZjD9mX76Vq-TIJLqGJaQfdhf7Mb0YVf-tOOJ8m62yro1W5AaI25qjupMQ3qpYp6I9JLDrc_if5XNNOb-01BvVg10TMQfgg8EZCmxLjfwnRrpdoOzbzrN9ryfaKddzQkNovINA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بنیامین نتانیاهو: «در ۱۱ سپتامبر، آمریکا هدف شر مطلق قرار گرفت.
🔴
در ۷ اکتبر، اسرائیل بار دیگر هدف همین شر قرار گرفت.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/alonews/146855" target="_blank">📅 13:49 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146854">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
علم الهدی: اون ۴نفری که کنار خیابون ماشین بهشون زد شهید هستن(چون سمت ما هستن)
خدا:
😐
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/146854" target="_blank">📅 13:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146853">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
نتانیاهو: مقادیر زیادی تسلیحات را که ایران برای حزب‌الله فرستاده بود از تپه علی الطاهر استخراج کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/146853" target="_blank">📅 13:43 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146852">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73948ccb6f.mp4?token=gPuL8OD8aP1gU8w4kqvGoI0pRMf9lVkIeYmslXm227jyQM3Zboj1PS4V1xEOmi0v7kZsZHSw7GAsjonZYe9VoCOn7LoEwvsV5tEvLHFDT0ZhzFUuLY6I1eFw3JzTNjlYczJZcSLFgebwNcksUnm_VJvK4qb-Fv_khuK5-VqHgwhdBfjeNfV-5hC8hRFMFtxSIPRj3PsvT3aVk7w7EorG-Zjc8HKP-hfAZbEBjWEMKUPN2CfSUioN3dpeCt7CMW5b1NkNig7EmmihZPN1pI0iOaz2jbdN69fy3GSR2JzuOdT8KfRMW7hTqzPoYfy-iwwtRJ5KXl7RFX5WKDI7yPYwjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73948ccb6f.mp4?token=gPuL8OD8aP1gU8w4kqvGoI0pRMf9lVkIeYmslXm227jyQM3Zboj1PS4V1xEOmi0v7kZsZHSw7GAsjonZYe9VoCOn7LoEwvsV5tEvLHFDT0ZhzFUuLY6I1eFw3JzTNjlYczJZcSLFgebwNcksUnm_VJvK4qb-Fv_khuK5-VqHgwhdBfjeNfV-5hC8hRFMFtxSIPRj3PsvT3aVk7w7EorG-Zjc8HKP-hfAZbEBjWEMKUPN2CfSUioN3dpeCt7CMW5b1NkNig7EmmihZPN1pI0iOaz2jbdN69fy3GSR2JzuOdT8KfRMW7hTqzPoYfy-iwwtRJ5KXl7RFX5WKDI7yPYwjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از ارتفاع دود ناشی از آتش‌سوزی در منطقه رأس العاره، واقع در استان لحج، پس از هدف قرار گرفتن آن توسط ارتش یمن
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/alonews/146852" target="_blank">📅 13:37 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146851">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
گرجستان اعلام کرد تحریم‌ های جدید آمریکا علیه شرکت‌های هواپیمایی ایران را اجرا می‎کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/alonews/146851" target="_blank">📅 13:29 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146850">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
فایننشال تایمز: به دنبال گزارش درباره تلاش‌ها برای دستیابی به توافقی موقت با ایران پیرامون تنگه هرمز، بهای نفت بیش از ۲ درصد کاهش یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/146850" target="_blank">📅 13:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146849">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
مصاحبه جدید هادی چوپان: هانی رامبد بهم خنجر زد. بهم گفت پشت ایران نباید باشی( منظورش جمهوری اسلامی و حکومته) ولی من قبول نکردم و اونم همکاریشو کامل باهام قطع کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/146849" target="_blank">📅 13:21 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146848">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffb4e73a23.mp4?token=TvJ0WewAWMoaXy0XO8qqOnVOZMUDalXplnhnnIL-rEwgfB9CsgY9b6spAAQyBGNyA0Lqfgn8AuiDpdi54uT6fpPVuQvbp3XqI0OPJPrOwRFWuWbHd8SHP3LQbioGNsxuFiminscsqBmbpfNX0cl6igKYmFiMcHjmOQYpzFSrKChT7QV-mx4cKIZUPFzDcsJU_elOzhxNhHNYWoYctkQyOQjjCW_KrrH-V1zEcWfE92wH_vcv4DPxwjKdby5cLw7NSZlI_NZHgH0-NYYro1EF_vHloVEKT6v0QaHrSMfIKQGl5qWTUshFYiG891SkPDjgKPLdw8stkn1SLjhNXrFphw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffb4e73a23.mp4?token=TvJ0WewAWMoaXy0XO8qqOnVOZMUDalXplnhnnIL-rEwgfB9CsgY9b6spAAQyBGNyA0Lqfgn8AuiDpdi54uT6fpPVuQvbp3XqI0OPJPrOwRFWuWbHd8SHP3LQbioGNsxuFiminscsqBmbpfNX0cl6igKYmFiMcHjmOQYpzFSrKChT7QV-mx4cKIZUPFzDcsJU_elOzhxNhHNYWoYctkQyOQjjCW_KrrH-V1zEcWfE92wH_vcv4DPxwjKdby5cLw7NSZlI_NZHgH0-NYYro1EF_vHloVEKT6v0QaHrSMfIKQGl5qWTUshFYiG891SkPDjgKPLdw8stkn1SLjhNXrFphw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مصاحبه جدید هادی چوپان:
هانی رامبد بهم خنجر زد. بهم گفت پشت ایران نباید باشی( منظورش جمهوری اسلامی و حکومته) ولی من قبول نکردم و اونم همکاریشو کامل باهام قطع کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/146848" target="_blank">📅 13:17 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146847">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
رویترز به نقل از یک مقام پاکستانی: اسلام‌آباد تلاش می‌کند از کشیده‌شدن به درگیری میان عربستان و انصارالله اجتناب کند؛ زیرا همزمان می‌خواهد روابط خود با ایران را نیز حفظ کند
🔴
هرگونه مشارکت پاکستان به دفاع از خاک عربستان محدود خواهد بود و شامل اعزام نیرو به یمن یا پیوستن به حملات تلافی‌جویانه نخواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/alonews/146847" target="_blank">📅 13:12 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146846">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YP7QWEvlIdyf19ddYjrh2KVCK_nmrUVH3QevyzUcPqxomZf-MM2ij-2OM61VJA1MGUvuKcT6vcniol533wbCV8cGdKkBhgTMiQFdEyuvr3DxTaEPRPvJwc6Pk03H2EU48u0Iy-Bd4wGTMOtob2QqTuSZZJCKv1c4W417GZPR7zzhVhBhbJUNjzfG1sp6Ptu7QI49FAYXn8JcwVR_OeLL-EyLf0li0TIjkxUJnBACYBWC0V6UtedYwUmed-FHBz8Eedv9F9foBjVTp6gf4kVId_27W6RE9rw4dMu41efpzj2utWRh8AOu9DiP074lUA776rd4_PWwesC42jdTwQd3ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
باز هم شعار علیه حسن روحانی
🔴
نهپاد: نفوذی هدایت پذیر از راه دور
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/alonews/146846" target="_blank">📅 13:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146845">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
رویترز به نقل از آژانس بین‌المللی انرژی:
ذخایر نفت جهان در ماه اوت ۹۵ میلیون بشکه دیگر کاهش یافته است.
🔴
بازار نفت بیش از هر زمان دیگری به پیشرفت در مسیر حل‌وفصل درگیری‌ها در خاورمیانه و همچنین جنگ روسیه و اوکراین نیاز دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/146845" target="_blank">📅 13:03 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146844">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا: دوشنبه یک بانک بسیار بزرگ را به دلیل معامله با ایران تحریم خواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/146844" target="_blank">📅 12:59 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146843">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T5jsAH7FWPjwptdZd664nMPJKhZOmMvb6Jy5VGU6-QDYErt18QtJ8Ret17ioWm6pCmQtKbukGroBuHQJ09VajFvx5-trqlFQ7uXeSYyNA01Un-qvuuRJWtbLOoniPdM6f6ZRiiBq12VLUxF59r078O6hT5lCxZk4MPWcDrWYx_kUcBOg-szgxcqPj6obpuXhpqtEj2t0bHtbok2SxAWnSOc8_xXVDe2d4XeyBfaVDSbB8sTpze-uVAJFUu85DRbz-JrgcUDoli_Ea6trwrbPhUYP-XM456rY8RJJ-4yoQuQ9Ul_Zc6WMuWre0S44Qe4JrV9vITSOytuzjUPWM9ONbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صادق محصولی رئیس جبهه پایداری درباره مفقود شدن ۱۶۰میلیارد دلار پول در زمان وزارتش:
🔴
اون سهم امام زمانه که دست من امانته
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/146843" target="_blank">📅 12:55 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146842">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔴
دلار بزودی 300هزار میشه
⁉️
🔴
تحلیل ترسناک نوستراداموس ایرانی
👇
https://t.me/+WZbLEaPPJQUwZDU0
https://t.me/+WZbLEaPPJQUwZDU0</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/146842" target="_blank">📅 12:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146841">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd237427b5.mp4?token=qB94fkK_tNI-a2qNLGR1v0YkIjGsDKVk45mcjc_EBfamkj83My1zxL2mqk2UzR5nmn3CH0rraV9mTNGNocMFgu4CFbNuchSOIqjYg0f7vctj1gbkbyJM4LvFbt0CTkFnQZ9q6zjJTTSTWOA3Z3SAb7wBOLoJckfTdJ4jsWpOl7p1abwEdZv64yzILsf01GicJX0tAF_EiIHlqJyAZRqRRPVhu78MOrxwJab4Xu35V-jaWB8GYnIGHkIJ6T8UJpBXhUcMu6Ie9tl8XyW8kmBu_25qzatQ4aaJpkPfHFW6M4gGrDvItPuaLDUod6tOm7mCX5lNFq7vz_YDJO8g32vXwzbCKln9e1XhBS1qdZF9vknhkmpDWtqhjVL7TZmjdDUupMK4qC8y5CXpN6h8mueiQkVF-oxiGFXj7YxECnvOpK6JDoe_YK16M_vkUJF4Jpx6jKS43HbtY1foW8YSITG7D90TmTlr6yvjXXADD56dV1gmFm5vZxdkrUfg26qWfB1KDPeitqUDo7Okjk4pIPjv4uoYBMrJIuzdwy_eEMw4B_dimfckwnfd3NHP6mZNHJIavkTm8-tL0CJsyO8-VxLwRtRVbXWxrYXh-MYhrlNV1TLwNhfmfCRZ2Dgym9zol9vRJwN_QZLZBvAOSRDjqKe9Z6rP3lvGEdcpnlJJChTVW9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd237427b5.mp4?token=qB94fkK_tNI-a2qNLGR1v0YkIjGsDKVk45mcjc_EBfamkj83My1zxL2mqk2UzR5nmn3CH0rraV9mTNGNocMFgu4CFbNuchSOIqjYg0f7vctj1gbkbyJM4LvFbt0CTkFnQZ9q6zjJTTSTWOA3Z3SAb7wBOLoJckfTdJ4jsWpOl7p1abwEdZv64yzILsf01GicJX0tAF_EiIHlqJyAZRqRRPVhu78MOrxwJab4Xu35V-jaWB8GYnIGHkIJ6T8UJpBXhUcMu6Ie9tl8XyW8kmBu_25qzatQ4aaJpkPfHFW6M4gGrDvItPuaLDUod6tOm7mCX5lNFq7vz_YDJO8g32vXwzbCKln9e1XhBS1qdZF9vknhkmpDWtqhjVL7TZmjdDUupMK4qC8y5CXpN6h8mueiQkVF-oxiGFXj7YxECnvOpK6JDoe_YK16M_vkUJF4Jpx6jKS43HbtY1foW8YSITG7D90TmTlr6yvjXXADD56dV1gmFm5vZxdkrUfg26qWfB1KDPeitqUDo7Okjk4pIPjv4uoYBMrJIuzdwy_eEMw4B_dimfckwnfd3NHP6mZNHJIavkTm8-tL0CJsyO8-VxLwRtRVbXWxrYXh-MYhrlNV1TLwNhfmfCRZ2Dgym9zol9vRJwN_QZLZBvAOSRDjqKe9Z6rP3lvGEdcpnlJJChTVW9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شعار مرگ بر «هیلاری کلینتون» و «مرگ بر حسن روحانی» در تجمعات شبانه
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/146841" target="_blank">📅 12:52 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146840">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔴
فوری / نیروی هوایی عربستان سعودی دو حمله هوایی به بندر المخا انجام داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/alonews/146840" target="_blank">📅 12:38 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146839">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3890ff4c6d.mp4?token=Y8xu3TKjewP_dit1qXhkPWe0yC34DrQ1lFYL4OAvYp-JUxk6QgIr-JUf7rOpw2t53iz3gs3luQvrEvY6jJq1cBDewGY6NFOveaqd7ZhPh7XwMBMLwFbhpQW2HZYVB4LLwX7IHjai8Qeo7rYbm9Vej25BdFcQZsunC31tlLCA2dYq8se9rG_ii1uAw9UgyVk12RdLnFvJ2ilnY3xQWeClA34OpIDuF35LmOkX4ZCu1q94UPmFGugOJqA4q_roDN7RF7PUA90FOhuwZkP7JcrKCAqdHuxd3P3du7KDyuVRROm_x5sJUDf5odrx1ZEajqab5CSpOfwTNiLA5zXDd1NBeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3890ff4c6d.mp4?token=Y8xu3TKjewP_dit1qXhkPWe0yC34DrQ1lFYL4OAvYp-JUxk6QgIr-JUf7rOpw2t53iz3gs3luQvrEvY6jJq1cBDewGY6NFOveaqd7ZhPh7XwMBMLwFbhpQW2HZYVB4LLwX7IHjai8Qeo7rYbm9Vej25BdFcQZsunC31tlLCA2dYq8se9rG_ii1uAw9UgyVk12RdLnFvJ2ilnY3xQWeClA34OpIDuF35LmOkX4ZCu1q94UPmFGugOJqA4q_roDN7RF7PUA90FOhuwZkP7JcrKCAqdHuxd3P3du7KDyuVRROm_x5sJUDf5odrx1ZEajqab5CSpOfwTNiLA5zXDd1NBeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پست خواهر امیرمحمد شاه‌کرمی از جانباختگان دی ماه
🔴
۱۸شهریور، برگشتم به همان خیابانی که اخرین نگاه های برادرم آنجا بود ؛ تا صدایش را از همانجا دوباره بلند کنم.
اینبار ایستادم برای صدا زدن نام امیرمحمد شاه کرم
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/146839" target="_blank">📅 12:36 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146838">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
یک منبع پاکستانی با اشاره به گفتگوی عراقچی و عاصم منیر گفت: این مذاکرات بر جنگ میان واشنگتن و تهران، امکان بازگشت به مذاکرات، و همچنین حملات انصارالله و عربستان سعودی متمرکز بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/146838" target="_blank">📅 12:35 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146837">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
روسیه،‌ لیتوانی را به حمله اتمی تهدید کرد
🔴
سخنگوی ریاست جمهوری فدراسیون روسیه: استقرار سلاح‌های هسته‌ای در لیتوانی قطعا علیه طرف‌های خارجی خواهد بود. بدیهی است که این سلاح‌ها علیه غرب نیستند، بلکه به سمت شرق، یعنی روسیه نشانه می‌روند.
🔴
اگر سلاح‌های هسته‌ای در خاک لیتوانی وجود داشته باشند که ما را هدف قرار دهند، آنگاه خاک این کشور نیز در تیررس سلاح‌های هسته‌ای ما خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/146837" target="_blank">📅 12:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146836">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yz6QrGJml_HlRVqidNdRVOLoAMY7k87gClWte5KOccyAn0JkPCWtcLfdY2wJkKrCVD2JAhBVooAMtHRC-9NTXR_v_QdADm8MedV3Vy5tQXxzerpFmHB4k9hkNf_9inVQ6FnlDMC3d_1q_D95ubmd7rV9SfKrBQvsPay7dcexyxOt6N-sI9u16-jnXhVd-HzVQgl0IBRA0upH8QhWFrKOMXUYPYuTrp9HxWqIAkmPwXv306D4HvdXc07a5J4KPPqae9rx2_Pls4X92sG4COKQzkaDcQtqxUbM7xSAmg8ywqeTMYY4jEfXmoaE6aXQr2HKfeAWiRgYD2uoFz0l93knPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نفت برنت 5 دلار کاهش یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/146836" target="_blank">📅 12:26 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146835">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hcxCvdeCkJxMFYGkLzwP6Hod894l2qXrBq1lg6TUBQilWdnrKD9F4EPUOrfdudy6O180sfBjnCpDaQWqcCQJQkdCfCPvhtgjBEdgkicVjxLltGDpUpzvQnmYcmljj422yKvCjNmlGWzKWlvOxOUC4cGAjWDLObYt0OtcbZJZTYxjiiDJLfFVc8O9G9Omt3h0cJSI4mpHbLbL3EL_VTEfJT5vLmEuTZRYWdwDhdbPmTOwSePwZKiDAy8QlW9X7pht03EzxugRDRAhqTUOvO0vpY-cyas1fX8pOfPBMRElUhpwxiKOWoOzpFNoYEUQjsbent98k9L-xJgdiNRmzDdzTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ادعای دو منبع دولتی یمن به رویترز: نیرو های دولتی یمن از جزیره بریم در تنگه باب المندب عقب‌نشینی کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/146835" target="_blank">📅 12:21 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146834">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
پزشکیان دقایقی پیش وارد دهلی نو شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/146834" target="_blank">📅 12:17 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146833">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PzMoQt7INphLmUxCrquiIeK6HNMmk5KT7NwLNhGuFcs6RiAjakQ1EWzL6N9zfpijVkrmKt0G07LRISZfuJo5NRIXT0zveQRAMAFN6TnfsVvnHddGvgshIiq1lIkBm6lGizAH4oNArgJryoViq6MWPqR86UTiPqgSCfzlSipplO3cnb4GEd4rSstSU10_bddQuUhe_WT7t8b12mK8bBYm5Jweq_lbI292fqeWyLHBXMRWqhSiOJTXVjqQ8btsYqg_-PPJTIYzmwg-oTJ-qYAqxBoEKsuWhRBk7YtDGRFllSls7AGWDgYV7xZnzcUFPp1ByADwsi2OMv_-qM9wxS9n_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
25 سال پیش در چنین روزی گروهک القاعده توی 11 سپتامبر به رهبری بن لادن، برج های دوقلو آمریکا رو نابود کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/146833" target="_blank">📅 12:07 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146832">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
پزشکیان: موافق ادامه جنگ نیستم؛ اما باید تاب‌آوری کشور را افزایش دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/146832" target="_blank">📅 12:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146831">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
وزیر خارجه مصر: باید به یادداشت تفاهم اسلام آباد به عنوان روند مهم برای رسیدن به توافق فراگیر بازگشت
🔴
ما به تماس‌های خود با طرف‌های مختلف برای پیشبرد آتش‌بس ادامه می‌دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/146831" target="_blank">📅 12:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146830">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
خبرگزاری رویترز به نقل از یک منبع پاکستانی گزارش داد: وزیر امور خارجه ایران و فرمانده ارتش پاکستان در مورد راه‌های احیای تلاش‌ها برای کاهش تنش‌ها گفتگو کردند.
🔴
در مذاکرات بین عراقچی و فرمانده ارتش پاکستان، احتمال بازگشت به مذاکرات و حملات حوثی‌ها به عربستان سعودی مورد بحث قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/146830" target="_blank">📅 11:48 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146829">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YPQbT6hXBP2VfG0TNO166oT0V2H56gJTvkoYBGPI-izHuvsG6OLBvv11ZVOK7_jnS8XN3yfDODlkJezQBOOql6C47jNYNsREH19D7ys5vsOBGJES3oAe25z5GpuKwdfqDf0gu5K8hhnZ0mn7FXKeac3a2JTdM-59pXog1phlFiMoUo43a6_tJeW64SqFE6fRFKIMNJye83IV_I-k8XBZ9LlcWbD-LaKhE0_XqEYvP6MEKhh2FRi5WblamEkP4VlueQUsD2ril1fvHgqM6U3Px2bgKQ6DoGg8E_N_d0NId5wFmbnwoODoC28j-IS9xBps34OkMA37FUNvIWm0aSl65g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرگزاری فرانسه با استناد به منابع خود اعلام کرد که ارتش یمن کنترل جزیره میون را به دست گرفته و بر تنگه باب المندب مسلط شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/146829" target="_blank">📅 11:37 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146828">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
پاکستان: «کمی عدم تمایل» برای اجرای تفاهم‌نامه اسلام‌آباد وجود دارد، اما «پیگیر» هستیم
🔴
اگر توانستیم در آوریل در میانه جنگ شدید، ایران و امریکا را به این تفاهم‌نامه برسانیم، هیچ دلیلی وجود ندارد که نتوانیم دوباره آنها را به میز مذاکره بازگردانیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/146828" target="_blank">📅 11:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146827">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
خبرنگار المیادین: نیروهای انصارالله(حوثی ها) یمن به شهرستان ذوباب در ساحل غربی این کشور رسیده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/146827" target="_blank">📅 11:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146826">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mpysObYWAEuoygN3P42TWbz7lU-NC28NjNJ2wr4PShp63Eps9fJJTWJuU47enjm7t6fa8OKRYiOE5E332Zg6SeHb_wOq9HNukryktfzs-OAVnAXLxWqINwqcP2itZdOGOH8TGdjwcrj511Z0gBVK5E_pEVuUBNkuDe3AiFRlf8isJiNQhmoCCO12fr865_JFgNNi7CFNFRgUkpz7M_SFlqFZTmJOmRmXnFwNnB_hLuC_Z_xbeeawkx6eM8F0bZLT6nx8afjp3LBX4piGzfh3nQu-8LIKjqbOznxdkNwB941vzwJ_pcx6Kg99Z4tDydjNJtcpOhJuXeaQ4yZpKPmYDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرمانده تیپ خان‌یونس حماس در حمله شبانه اسرائیل به جنوب غزه کشته شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/146826" target="_blank">📅 11:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146825">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bt34H6-I_EAgjutb73N4vReRkgiWeWxVYz08t8UhUR8UOKGk8hMnG-ClPTM8iIWwlbpmWxsUXqCGU4QwRO1UCGSisavWxltf9XtbBnbBnBAzEGZ_oLLUMmNO-eu3lkzKFS_SpjHfSieNl35FFPU3Td8vRIqPf3BatEzvvaebaVZY_Fqckswfh2D7PNmHmo2VF92kKV6J9K773gj-vJBgoH1UEcsrN_uevk4oCLeqo7riebinaazo-nRSphgKymkbyO0QQP42JjK_cNRYhpgh96sjtxryPrtxWLqMN4bU5_35XpwB4KvN8jr7HaT45byBuk9tH0Y46jPzeUsiJccuQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دستیار قالیباف: تفاهم‌نامه‌ای که به قول خودتان مرده است، چگونه مقصر علی‌الطاهر است؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/146825" target="_blank">📅 11:17 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146824">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
الجزایر حریم هوایی خود را به روی هواپیماهای اماراتی بست
🔴
این اقدام در پی قطع روابط دیپلماتیک الجزایر با امارات صورت می‌گیرد. الجزایر، ابوظبی را به دخالت در امور داخلی خود متهم کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/146824" target="_blank">📅 11:12 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146822">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fFdYaPBH0Rne-hw-rrdjQEcehH7m3bNt6szbOFQ_ejvHSnPr5717knF-MJVfUz_lzhwtYDbU3ihOhXJenY8F0NnEAkWQNAcCbqX8hDpslW9LR6iGXZeqoj4ctUSZkl6NxvQpXKugLW7CTjYgA7Xxe0KSHVSP4R-CVGkmXxGUawMhMUXjV5YRvPQGBOW3yNBDRlAmzIV1uNKgIo-Nf8kc2L29uN6ISSiaAb5HYbXSC7dDQZsYPygHIxBXPL05eP454CJA40p5BIMm-5uy2_pyRz8s5eHe3onZ1SmjKLZzMMplJOt7j_VUI9-JPMuWbMWq0EPt831LEvIZR3igmemA0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff55988390.mp4?token=ijHkgFuevJXpsAoK1Nn4LeSp00gaMnmwL7uva3IX2zSxjNw3VCJM6_dh3ggm1mmydeG4DkaisZWp3LIKT6qr4Q2Ww_itUdoOtiFBJJtifzRmYSlA7jYB3FIWkAtI3KnN1dS-2cno1gsucl4lAOueH8zfGSqYgywe4JfRDMzwV8ad7n-E6ciNETDyohgnvAmfBdjOpHuEC8ZW0HxT2qoIHRbg_iOTJT9EGTHTkXb_PeOF0VJJNKyQ0V59cg9JOkxIs4AX9H9sbs2-3dU9fozUmovysAFX-0cbIzvezKTxpRtjmdbvmubwJ60cx_cHA2dNksL1bLWFR0LnB1Hb7sV7Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff55988390.mp4?token=ijHkgFuevJXpsAoK1Nn4LeSp00gaMnmwL7uva3IX2zSxjNw3VCJM6_dh3ggm1mmydeG4DkaisZWp3LIKT6qr4Q2Ww_itUdoOtiFBJJtifzRmYSlA7jYB3FIWkAtI3KnN1dS-2cno1gsucl4lAOueH8zfGSqYgywe4JfRDMzwV8ad7n-E6ciNETDyohgnvAmfBdjOpHuEC8ZW0HxT2qoIHRbg_iOTJT9EGTHTkXb_PeOF0VJJNKyQ0V59cg9JOkxIs4AX9H9sbs2-3dU9fozUmovysAFX-0cbIzvezKTxpRtjmdbvmubwJ60cx_cHA2dNksL1bLWFR0LnB1Hb7sV7Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
انفجار اسرائیلی‌ها شهرک المنصوری در جنوب لبنان را هدف قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/146822" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146821">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
پزشکیان: به جلیلی گفتم هرجا می‌تواند برای حل مشکلات اختیار می‌دهم
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/146821" target="_blank">📅 10:55 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146820">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
رویترز به نقل از مقام دولت ترامپ: حمله ایران به جنگنده‌های آمریکایی در اردن آسیب زد
🔴
یک فروند هواپیمای A-10 تاندربولت ۲، معروف به «وارثاگ»، هدف قرار گرفت و یکی از بال‌های آن از بین رفت؛ همچنین حدود هشت فروند جنگنده F-15 دچار آسیب‌های جزئی شدند
🔴
حمله ایران، نیروهای آمریکایی را مجبور کرد برای مقابله با موشک‌های ایرانی حدود ۳۰ موشک رهگیر پاتریوت شلیک کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/146820" target="_blank">📅 10:49 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146819">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b9cab6fc4.mp4?token=s0FPBsjSH50XAUSLVok540OV5wr0KMcPvfNMHLYgvFyjxyUiE7-RePvXejjP6SxtRYDqHX8Arz4sqsWPN_nZgZU0Z8Gs9IlyB_7FPsLe0JBX3BqmrcrXxcnQgMfmnhLBQCW_GamDqnUdOz-fyJNYaKPVwG2oPuLwv3gKFB0OKonaXpLPsa49lNA0w7vEqxfQzzFnX0sGCd-NAaNUHXU9hxz-TVU4fIbFwfxA3pROwFSH3hIRoKRbiu0hR61JMLzq-PZ1kHKCO-AOwBfr8rFU0oqFvYnxLcsdv6gbI_iSG2OW-tRO8KdFWspkS1OK6IhDKyUyMrK2zc5ZZznIwVQ8MkuCc6Fq5ORChhfDNg70ftXIsKWdSY5BuICO94TgTzuwUo3lQDFwvd7mE_JWkWB0xJMSPLNaOGxYn3qawVztpQuF3jwE1bIcwkkHIWr6-3Zd3q4AwQTBLIPzi38cIzKmj1RRCK5gruAKlmIxePjdlnN3AeJzqMIFMlACD487yICsYgDMpbnVEbo68vrx1m8ovkdawTQA8JAJh_nNy2gayLhmb8Ee_W_7v05j0WnEdrooDLIvgjV9F-vHJwKOYFtpTcwCoPikai7MPJsz8V7bigfhe0IZCgDHyj4vuUEGEKroI9uRUCKtVrRnHh_dpP1yJLxdD27ylUORWKRrJbUNLPI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b9cab6fc4.mp4?token=s0FPBsjSH50XAUSLVok540OV5wr0KMcPvfNMHLYgvFyjxyUiE7-RePvXejjP6SxtRYDqHX8Arz4sqsWPN_nZgZU0Z8Gs9IlyB_7FPsLe0JBX3BqmrcrXxcnQgMfmnhLBQCW_GamDqnUdOz-fyJNYaKPVwG2oPuLwv3gKFB0OKonaXpLPsa49lNA0w7vEqxfQzzFnX0sGCd-NAaNUHXU9hxz-TVU4fIbFwfxA3pROwFSH3hIRoKRbiu0hR61JMLzq-PZ1kHKCO-AOwBfr8rFU0oqFvYnxLcsdv6gbI_iSG2OW-tRO8KdFWspkS1OK6IhDKyUyMrK2zc5ZZznIwVQ8MkuCc6Fq5ORChhfDNg70ftXIsKWdSY5BuICO94TgTzuwUo3lQDFwvd7mE_JWkWB0xJMSPLNaOGxYn3qawVztpQuF3jwE1bIcwkkHIWr6-3Zd3q4AwQTBLIPzi38cIzKmj1RRCK5gruAKlmIxePjdlnN3AeJzqMIFMlACD487yICsYgDMpbnVEbo68vrx1m8ovkdawTQA8JAJh_nNy2gayLhmb8Ee_W_7v05j0WnEdrooDLIvgjV9F-vHJwKOYFtpTcwCoPikai7MPJsz8V7bigfhe0IZCgDHyj4vuUEGEKroI9uRUCKtVrRnHh_dpP1yJLxdD27ylUORWKRrJbUNLPI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار
:
«آیا ممکن است جنگ با ایران تا پایان دوره ریاست‌جمهوری شما ادامه داشته باشد؟»
🔴
ترامپ
:
«نه. حتی یک احتمال هم وجود ندارد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/146819" target="_blank">📅 10:43 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146818">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
خبرنگار: «درباره پرداخت‌ها؛ آمریکا ۴۰ تریلیون دلار بدهی دارد. اگر سیاست‌های اقتصادی شما موفق هستند، چرا باید برای حضور مردم در انتخابات مشوقی در نظر بگیرید؟»
🔴
ترامپ: «من این کار را به‌عنوان پاداشی برای مردمی انجام می‌دهم که مجبور شدند پنج سال شرایط وحشتناکی را که بایدن ایجاد کرده بود تحمل کنند.»
🔴
خبرنگار: «شما همچنین وعده چک‌های بازپرداخت درآمد حاصل از تعرفه‌ها را داده بودید…»
🔴
ترامپ: «نه تو. نه تو.»
🔴
خبرنگار: «اما این اتفاق نیفتاد.»
🔴
ترامپ: «نه تو. تو بدترین هستی.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/146818" target="_blank">📅 10:42 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146817">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
گفتگوی تلفنی وزرای خارجه ایران و کره‌جنوبی
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/146817" target="_blank">📅 10:41 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146816">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PhDzZsf-fQjHQXCaOkFjz5AL_eKTq31jcC4-hnXR_yZnVKALoGmyu5MhlTdZajvqYIVpYpnC9QWfjCnxLgHIRF7DGGt8t8eAOcdRbfStMYSotoKgH6capItHzQmyOx6M4Ah9pCH9S7DEfAr5gokmYS6VV0Nvn9DGrLtlLOYKKm7zxFXf727zp9LwrdCv4Ql0yQ14oZrG9ACT6_XRX2gGbi8hkm7-_mlJbku82VQQogiBPVb_odF3Ja3hP0RdUDw8hr4d_ckaWKP9-fNkAGy0ARjqYlneEWwMYQj5M9MXOVUnM2VgBxwKsPqQ3atVMY_RThgF2mOurW3BkQpUrnxCIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آموزش تیراندازی در شب نشینی شبانه
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/alonews/146816" target="_blank">📅 10:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146815">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
بر اساس گزارش رسانه‌های عبری، دور جدید مذاکرات میان لبنان و اسرائیل روزهای سه‌شنبه و چهارشنبه در رم برگزار خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/146815" target="_blank">📅 10:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146814">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
اکسیوس: ترامپ درخواست بن سلمان مبنی بر حمله به مواضع حوثی‌ها را رد کرد
🔴
دستور ترامپ این است که نیرو‌های آمریکایی بر ایران و تنگه هرمز متمرکز بمانند و از گشودن یک جبهه دیگر خودداری کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/146814" target="_blank">📅 10:11 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146813">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79badc7e41.mp4?token=uvmc9YneM_lvYhm72g4F2tHdW4fgJnWWCdt-QOCa6nr3wxaVt5s5KE7KJmtAh8drQieHGfKddkge3Kc3l7WRuEBgSQtBo4IWcQWl47K13ojf82JfVlE50BDLKocbxoSmaRx3PWtb_qjU9063xFNh8HSsqt7FGN0N-9DlBa7YBRtVgvw-x-Rh_0Qr0VTFDUFzykXg_iL-GSl2FYkOWNWZZj4aVzXCAuDxyxd4XJ_eJalC6GuSzrq-g3niEHFfWlZhUvAZO3SXHVDZWXTq6fyvtIXCuI1kM0jsKrKXrYcZAFFjBsjfK9VAzPF3VJY_Metd7hReNYSEx0eySZESPmdtZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79badc7e41.mp4?token=uvmc9YneM_lvYhm72g4F2tHdW4fgJnWWCdt-QOCa6nr3wxaVt5s5KE7KJmtAh8drQieHGfKddkge3Kc3l7WRuEBgSQtBo4IWcQWl47K13ojf82JfVlE50BDLKocbxoSmaRx3PWtb_qjU9063xFNh8HSsqt7FGN0N-9DlBa7YBRtVgvw-x-Rh_0Qr0VTFDUFzykXg_iL-GSl2FYkOWNWZZj4aVzXCAuDxyxd4XJ_eJalC6GuSzrq-g3niEHFfWlZhUvAZO3SXHVDZWXTq6fyvtIXCuI1kM0jsKrKXrYcZAFFjBsjfK9VAzPF3VJY_Metd7hReNYSEx0eySZESPmdtZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای، خسارات وارده به تاسیسات نفتی جازان متعلق به شرکت آرامکو در جنوب عربستان سعودی را به وضوح نشان می‌دهند، جایی که تعدادی از مخازن نفت تخریب شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/146813" target="_blank">📅 10:07 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146812">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
فایننشال تایمز: ایران و کشورهای خلیج فارس روز دوشنبه در عمان درباره تنگه هرمز مذاکره می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/146812" target="_blank">📅 09:59 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146808">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LSV6xfAHLDynPlNQacFKD11c2MujdWykZKo9GIjgJeVboVR48YlkkFf6AF4OyQrQEciuO4cV_qvXemDCiuo6ZhHg_kumJHMd77z0RwzoV5pos71QMwdngfveWP4azY3o3WwgVdT4CRHtrY68vL_qhshT3pWLwFQi8Ua6escSrGTb7KKyGsPP5vZLX8MZQ1X0ArU9xng89c-bZkOGBuZ-pNDUS2sCe-iFn7_xLY6fJ9iTiZx-_SvGYnBGrXwrOtxvY7sPl0j4WMdOuIQd-XtKGAOYX4DrHDAEEW0IH467C6SJb_j7ZP1073Ro17StD2G7-XxCGoEcmMZ8RqPjVP3f5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hMd-E26CAFyNuyw4iMGWz87pfglDICa7E_xT1oPm1kBHs8ufFlcV3nc_4XTqUjI_rZRxIAKSpX40yIyh4fIVHqlHLH9dEozA7c4eA4u0W4w6Wrlld6gjRLVlg_81j0vKlNbyxON1m6jh6it7RQGwzRa4grDipqUPtUh7nb4Ctia5je99W4I4xWgFxrAIGNDhATT8UXYxMScShuYszKdVyIsKXW9JiyBWqoQF6FNHFJkkDHRwXk_cDIKzzQewiHK9A7UuWJFINp40w_RqAM5_N2_JnQt5vf3Cyl9AG0yT9dv19A7RZLL7ldHsYKKWJFenA2BfLfxcpHsWJkxnbEoB_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uP1bAal2U7TnJT6eag5yz72jkYu_F63H9Phdk21U3HzlJX880wgEpg9iD33l0yCX4dvsVdrKHe4bIhVKhgEOgr1uuPD2nlIOo6owetRmLNyonpxVYGvl2vCC0i2Sr_uMBFVvMaQA4g9uH9VlhDBwvEF0gurBvoUZUQoKOOWwNMsRBhKr0gD4IZXYXCe5vUsuOMcdogVZDJKDN4dJua4YB9Aq3tvtgGCLsnLqPKXO5nP-gWgjgeATPQI__qOQLez0PBeOaMRsTy3jDjJV4Jw3OHyjlBvhXoEwm7sx67wsfX1BaX3CWA7L3Tgu4qMEmmy3eudqz4RzP9vJOZlI67oAPQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d91da570a.mp4?token=PLk_rj-FlGUbAIgFrvicQia8RlZUes4PmfyP02Mv-WXdjUp4Uv5Bpq4tVVp1OLgwVLa4nPc5ST-hnR7x2zy5Z-QjBB76IjthyXKOWNKwgEo_kAZYWhJ3YTUwI621uZiA-tSMw0hkx16drMWYOvzQv1eIfYWe83ciJW-oIV1BiHUM9Cm9xU-32XtYpprMp9l-UiieXqTUFqCU9Ex3fO-hJwTYYmKG7znOd0oeHydiPFHeX4d9qXLs71loKC0h1BswNiMy3Z0j23OwDGZeATqMmjI9lgLXP6CfecmywPY1F3vRstdxia33B-CnjtpbOpPx1K25WcEGuwF40UjZi1QNJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d91da570a.mp4?token=PLk_rj-FlGUbAIgFrvicQia8RlZUes4PmfyP02Mv-WXdjUp4Uv5Bpq4tVVp1OLgwVLa4nPc5ST-hnR7x2zy5Z-QjBB76IjthyXKOWNKwgEo_kAZYWhJ3YTUwI621uZiA-tSMw0hkx16drMWYOvzQv1eIfYWe83ciJW-oIV1BiHUM9Cm9xU-32XtYpprMp9l-UiieXqTUFqCU9Ex3fO-hJwTYYmKG7znOd0oeHydiPFHeX4d9qXLs71loKC0h1BswNiMy3Z0j23OwDGZeATqMmjI9lgLXP6CfecmywPY1F3vRstdxia33B-CnjtpbOpPx1K25WcEGuwF40UjZi1QNJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کلش ریپورت: تصاویر ماهواره‌ای و داده‌های حرارتی، از مشاهده ستون دود بسیار گسترده و چندین نقطه حرارتی در مسیر خط لوله نفتی شرق–غرب عربستان در جنوب‌شرقی مدینه خبر می‌دهند
🔴
برخی تحلیلگران از احتمال ۶ تا ۸ نقطه اصابت و آسیب یا پارگی خط لوله سخن گفته‌اند؛ با این حال، تا این لحظه آرامکو یا منابع رسمی عربستان این حمله را تأیید نکرده‌اند و رسانه‌های معتبر نیز هنوز تأیید مستقلی ارائه نداده‌اند. گزارش‌های شبکه‌های اجتماعی نیز همچنان متناقض است
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/146808" target="_blank">📅 09:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146807">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
رویترز: عبور کشتی‌ها از تنگه هرمز به ۷ فروند کاهش یافت
🔴
داده‌های اولیه ردیابی کشتی‌ها نشان می‌دهد که روز پنجشنبه تنها ۷ کشتی از تنگه هرمز عبور کرده‌اند؛ این رقم در روز گذشته ۱۱ فروند بود و همچنان بسیار پایین‌تر از میانگین ۱۵ کشتی در روز طی ۱۰ روز گذشته قرار دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/146807" target="_blank">📅 09:47 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146806">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WLBlLMw9xhWdqAM9ZPOuSWU0iYe7mAZXfUm9Xt9mGW6yO2julYRdBgIVIcXv8UY9v1yp6nLFpd4Zrm7SCnfYaaaGsI5cJgA89tWO7jLhe_Gz8d-SI3EDDwqhE866z9qJzr7CpttohbJUspgNyQ_2bz_sjAeCjfdJHZ8BYL02utscbpmMsOgxEbyH-4NQOh028CRv5IqFU-J9IKwURBAG2JxWl5sq4Ej3AbwalXLRM41i6Affe57CmE2y7JAkfDC2fkZMXAX4W9KR-kUIwWojAr1cbFjln-SQ9zIE0w2JMHrXm7vSvBgO2yAsO4w0sc4AlvQN22hImznnELVMQu_YKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش عراقچی به اعتراف مقام آمریکایی؛ مردم آمریکا نباید هزینه جنگ‌های اسرائیل را بپردازند
🔴
صراحت «هانگ کائو»، سرپرست وزارت نیروی دریایی آمریکا، جای تشکر دارد. او درست می‌گوید، نیروهای مسلح قدرتمند ما واقعاً «ستاد ناوگان پنجم آمریکا در بحرین را با خاک یکسان کردند»؛ همان‌ کاری که با دیگر پایگاه‌های پشتیبان تجاوز آمریکا هم انجام دادند. مردم آمریکا واقعا نباید هزینه جنگ‌های اسرائیل را بپردازند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/146806" target="_blank">📅 09:41 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146805">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lnj4h-e9lx1l5ACy0lk1HGdZhKZz60rLZLYalgeStyPH1xDZdkvOpFQdvE_9anOfrnT0oIqUJGycVjfNUx-c0UWJpjkOuQouc1SYukSFvQfDq-2qpIWZvvxeZGHWPuKvvd7nvRN0nWkaDX3JBdF1g9tu0_RzwyUIbQuRFULIPmZeGuavTmuuFl3bHIM8J8FvYnm58rjXiCSqvRpkxmA82xrRhT-y6FuxjxU7K_Et7wzB_RqG9tnUv4iPnmXc1ecFIZhjHfI1GZTKvpyG9beRL0damoj_6y2XHkW6aoheQZtQY5T0LTjtRY_WtakMKhe4UTXxyFyoXG2DdZMjiAwO9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان به منظور شرکت در اجلاس بریکس عازم هند شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/146805" target="_blank">📅 09:35 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146804">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5371cbfee.mp4?token=HSoQDmQitcDgkO56gHM5Wlia8VDYTBInsiLmMzGUgWu5gepaAUm3JaPdi8wQinwPEVWLDCKJvo8bUhEzEH0gm5GWGjINL-3hCBI464RwhXcoAPJNoq_spGHCyA6fPYcB4lDCZF_uG-I2z9JLDOkUmEBqnfMo6YQAQU-LUj6_6RGQJaD-2pgvBzFI5490T0jJb_42zvMLE5gghMfauAfqeyleoerHhU4IUQhqJPEPBEHGxz5rrAY5_qL7czUeirD-ZNhJOYfmiyIXeVqwyFwp4h1lhGsHiNf_V2g4yos9eNSQNNwerBo6nrTP7lkbDOxUnczMqD_dsTMViJpySUNhgDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5371cbfee.mp4?token=HSoQDmQitcDgkO56gHM5Wlia8VDYTBInsiLmMzGUgWu5gepaAUm3JaPdi8wQinwPEVWLDCKJvo8bUhEzEH0gm5GWGjINL-3hCBI464RwhXcoAPJNoq_spGHCyA6fPYcB4lDCZF_uG-I2z9JLDOkUmEBqnfMo6YQAQU-LUj6_6RGQJaD-2pgvBzFI5490T0jJb_42zvMLE5gghMfauAfqeyleoerHhU4IUQhqJPEPBEHGxz5rrAY5_qL7czUeirD-ZNhJOYfmiyIXeVqwyFwp4h1lhGsHiNf_V2g4yos9eNSQNNwerBo6nrTP7lkbDOxUnczMqD_dsTMViJpySUNhgDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رابرت اف. کندی جونیور، وزیر بهداشت آمریکا
:
«رئیس‌جمهور ترامپ ۹ جنگ را پایان داده است
🔴
او شایستگی و کارآمدی را به دولت ما بازگردانده، اعتماد عمومی را احیا کرده و
رهبری آمریکا در سراسر جهان
را دوباره برقرار کرده است.
🔴
من از خداوند بسیار سپاسگزارم که چنین رهبری را نصیب کشورمان کرده است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/146804" target="_blank">📅 09:26 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146802">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dqRBKgdb-IzlORH7d9DfVeD_Gs1kOY_uxtpBAoW_mRDHIDZL1FZTRqr7ciwJCeV0XHQAM_oqYG2LeZHOl7VHU_xY1Gd8jKRtPy_RZA7nFiYL-D-_tZdhU6nGdzVBNfI4Dr-43CxwdO1tn-9xU2PSf3yaZ7glRRuyPtfGO8Abp_nGBLWZhrs7v6HQcyl-HlsqkbELLiXzfxnFLjGZ8rQCcAC3bQwtpI6iPD_nKprmdgsFcnJJGsKAlPGSYq6MAtK9nCHVQ6SKlRAcEv8g5yvr0qmW6HIGWiLGxyzp8pdeaTHqcaTnk0T_eIOsLwOlZeYASxArJ36EAik228qLY1y74Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gbXdD5-R8BF-Givvdj5ESNfgYzE1T867PHOanUECeAJ-gEdNmeAD5c46SeJJihgiyVxjygngolRAru2Ia4WccjeNVVe3KazShUhJQFvChvt6-Ysi-T8dlmliJxkNTMUgHG2pa-KZyvMDPr2oOwIAtP-O54_GIpPvB8Y-1xi7Yz0xkUdmJRaq5rP5K6svKxMOG8_0wjij4LmV3_Kn6pcBBsDyFzz1dewEFFfgljAZJo3RQr-q_966E1PGnVNqXMhyorSvlFpoqBZSUBppG_0hFPo1yNvOROup4bTz3jijDv8qgfC2LYQU0mFqKuBNYyV5OKLml5dKRb3lkRLCPtyEXw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
پهپادهای اوکراینی پالایشگاه نفت ساراتوف در روسیه را هدف قرار داده‌اند.
🔴
چندین مورد
آتش‌سوزی
در این پالایشگاه مشاهده می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/146802" target="_blank">📅 09:12 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146801">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CtM9Dk_i9HtRLZ1Xwjyt9fHUR4UbOR58u31ZCl7vWNEpQyEC5_fqen90kF3EJmxyPViAXSfHHoMr1VP9aPs2WmIXUHUaKmGPfgSXEZpnqcuGo79HW-cTZqslUw33JZuP8mJ4x1DsWHVzq8pKYWibeoBFPnoOQyDSMvFDx7UiyTvWGPS-h4SydrOpKPaqmTIg2CC2tt2xWvws6X24it__pSkPQiYPYM5k-bHChBM4BV6mViVvu0ODuetM2kMou10cE4K3bRBkKWdEi-XN3bAmHaPqENCsII_UH87QGpIi_7Obq7yQQK8UGuXkPXSIrzKwvD8skBHa0uW6sD6X7VtJXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به نظر می‌رسد عربستان سعودی در حال آماده‌سازی برای بازپس‌گیری ذُباب و المخا از حوثی‌ها است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/146801" target="_blank">📅 09:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146800">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebf6a07434.mp4?token=YjVJw57twjrN833ZQjgOSLzfRVoMtCHyKvGA3Ao_81bgPWSyQFjCnagsmAhsKLgQAw5KrmJttRjtpOb3k_74DxIJsqpv0vcRRBDU3WPVtm_WJCm2XePxZ-a_Oi0FYpCl7-sogZdwFBOetKpIEedVd55qs1FEymLW3hK9zlQ6ibnWp6JITfRxuOVjNm9mEAZNuTxvSbBZAiI-mvxzY0ylaDncMC6oXby9yPjPz2IA3zuCAxYbhMj2HqfnVYhimshHYzgGVSVgu3RbsyBUF3kX2ajV7VC0xdEX4k3DmERSmDC2beRACCnQyX347RE21-EofVNJNLeuuHNmsveP42pw-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebf6a07434.mp4?token=YjVJw57twjrN833ZQjgOSLzfRVoMtCHyKvGA3Ao_81bgPWSyQFjCnagsmAhsKLgQAw5KrmJttRjtpOb3k_74DxIJsqpv0vcRRBDU3WPVtm_WJCm2XePxZ-a_Oi0FYpCl7-sogZdwFBOetKpIEedVd55qs1FEymLW3hK9zlQ6ibnWp6JITfRxuOVjNm9mEAZNuTxvSbBZAiI-mvxzY0ylaDncMC6oXby9yPjPz2IA3zuCAxYbhMj2HqfnVYhimshHYzgGVSVgu3RbsyBUF3kX2ajV7VC0xdEX4k3DmERSmDC2beRACCnQyX347RE21-EofVNJNLeuuHNmsveP42pw-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مایک جانسون، رئیس مجلس نمایندگان آمریکا: «رئیس‌جمهور ترامپ هیچ‌وقت نمی‌خوابد و ما هم همین‌طور. هه هه هه.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/146800" target="_blank">📅 08:59 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146799">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b21aeaca5.mp4?token=d8ApVyXs_7y72-ygm57XHdR7p0HmdrHxeFL9GT3hgn1S0Tf-pJGarSjR4TIn9-MlwY6188pilmwW_0HIAzS3NhU3Ee8A5zV6oZnp_6ar4W9wOWTP7h3rAykXLZ9so69S20dAq24dKGkNaKV8wacVeQvBBaFz28kcJWQjSrx7wo7ru4vdJcZq9x6IrL_5HGeU9PeYhv17Q7TIit6vPVmFVlrHyxkZLMqP0kdx1htK1fLIZA5bsrxWglQkdktbuT9GwsA1a6uMtxMTAtwOcSlg3-LW9QmHPL5BP3W1glapjWUCputbQ6_vfSuClU5Rkh1vRhT-vvE8IPp4UGSjAXp0mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b21aeaca5.mp4?token=d8ApVyXs_7y72-ygm57XHdR7p0HmdrHxeFL9GT3hgn1S0Tf-pJGarSjR4TIn9-MlwY6188pilmwW_0HIAzS3NhU3Ee8A5zV6oZnp_6ar4W9wOWTP7h3rAykXLZ9so69S20dAq24dKGkNaKV8wacVeQvBBaFz28kcJWQjSrx7wo7ru4vdJcZq9x6IrL_5HGeU9PeYhv17Q7TIit6vPVmFVlrHyxkZLMqP0kdx1htK1fLIZA5bsrxWglQkdktbuT9GwsA1a6uMtxMTAtwOcSlg3-LW9QmHPL5BP3W1glapjWUCputbQ6_vfSuClU5Rkh1vRhT-vvE8IPp4UGSjAXp0mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عناصر از نیروهای وفادار به عربستان سعودی مدعی شده‌اند که تجمع‌های آن‌ها با ۴ موشک از سوی حوثی های یمن مورد هدف قرار گرفته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/146799" target="_blank">📅 08:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146798">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qr24XCxm6pNnSTcJ7RT4O8LQ-EMuCy9RBYFgSVDvEUHPRa8qzqFRAT91NZohHKWXuqGK1kNlyPXwrI_aCqBkXLd-4qK79P8tRYBm7RGTUcR5D6o29vYEjNh9XHQ8cF9rdJsM-IxSJ5RkXlkrCdmhca-iM6prFpvRAPMY2bE4tiQvKXVs9ZGStyfzF0bZW25MRgvyul_npQbmevukggjXyjYVODlVgHrb2GKYMgYIa-aA10D__RS5NZkpYK43OMjhKeUpdJl8UKuLYAaV7hGyix8IcMcexaY47btBJeKg_3VcdFnmVahrYbguLpLdPCBNrGYQIfEoM0M3ZaJuq1-_Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اویل پرایس : در صورت تأیید گزارش‌ها، هدف قرار گرفتن خط لوله شرق-غرب عربستان می‌تواند تحول مهمی در بحران انرژی منطقه باشد؛ این خط لوله یکی از مهم‌ترین مسیرهای جایگزین عربستان برای انتقال نفت بدون عبور از تنگه هرمز است.
🔴
این خط لوله نفت را از مناطق تولیدی شرق عربستان به ساحل دریای سرخ منتقل می‌کند و در شرایط اختلال در تردد نفت‌کش‌ها از تنگه هرمز، اهمیت راهبردی ویژه‌ای برای صادرات نفت عربستان دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/146798" target="_blank">📅 08:51 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146797">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fa815d3aa.mp4?token=VsQrG7c7b4v2h39NUv1J9SWsMcTB8VItzThuvdOKFCngX_NY87OjEJY4GiYyWCaxpAJp6gzr_cBk8qLDEVfZoA0uiHy63k19rn63yhgi997sMREz7xr8qH3FAcXkGkoUaDy0c_ZrDpVU8SHrY0zv5n9MPPlHn6kPsWRbzz9_4DXf9rR3knJS5pcNJ8LOqAfH6iQqZCHzTxuYHsNI9Mn3T2OCmuB65Xv_HH43TDQQ72TeYhYxV5GP68fjfNMZfxu0WTPLR5E2f6HgynMWyXEopq83-B6egz6ezmc3ivoV775tBZfLt0wd_EfgJogswFJTKIHtevrrd3FMCgkLfWl7KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fa815d3aa.mp4?token=VsQrG7c7b4v2h39NUv1J9SWsMcTB8VItzThuvdOKFCngX_NY87OjEJY4GiYyWCaxpAJp6gzr_cBk8qLDEVfZoA0uiHy63k19rn63yhgi997sMREz7xr8qH3FAcXkGkoUaDy0c_ZrDpVU8SHrY0zv5n9MPPlHn6kPsWRbzz9_4DXf9rR3knJS5pcNJ8LOqAfH6iQqZCHzTxuYHsNI9Mn3T2OCmuB65Xv_HH43TDQQ72TeYhYxV5GP68fjfNMZfxu0WTPLR5E2f6HgynMWyXEopq83-B6egz6ezmc3ivoV775tBZfLt0wd_EfgJogswFJTKIHtevrrd3FMCgkLfWl7KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: حتی محافظه‌کارها هم می‌گویند اگر می‌خواهید وارد ایران شوید، به طور کامل وارد شوید. فقط وارد شوید و آن‌ها را از بین ببرید.
🔴
ترامپ: خب، شاید من این کار را انجام ندهم، چون انتخابات در راه است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/146797" target="_blank">📅 08:46 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146796">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c57019ecf0.mp4?token=aDD0yHz-eZiRusyQhnie60P7ZGflN6w4oV8ykeacXWw9eNhbbDvneMaaXpjfSt9-3reACfoS6lH7uxRIHzugPohJkaRbA-pROZTvrANeh-xb4d-aUrLNrL0lM85aC1xe8zdEoyzoYBntIYwNKNckLWsBztjrP5RQtIt483a3GvC6EEs3Kc_L9L7MyRLAQFZOC1g8Ne2vN2NryYgkiviv3ieNn0qzpxkJs1EZUWgrCLlqf1qS1RnQuCSkmkZIad62xaJ83Kc8nxm37aLSGjGvn3lnd8gNCJpvanvr3PV0azIk54xLauoAoKdLEMpK_pc_2tbpC5YevtzPdUeDfwkbjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c57019ecf0.mp4?token=aDD0yHz-eZiRusyQhnie60P7ZGflN6w4oV8ykeacXWw9eNhbbDvneMaaXpjfSt9-3reACfoS6lH7uxRIHzugPohJkaRbA-pROZTvrANeh-xb4d-aUrLNrL0lM85aC1xe8zdEoyzoYBntIYwNKNckLWsBztjrP5RQtIt483a3GvC6EEs3Kc_L9L7MyRLAQFZOC1g8Ne2vN2NryYgkiviv3ieNn0qzpxkJs1EZUWgrCLlqf1qS1RnQuCSkmkZIad62xaJ83Kc8nxm37aLSGjGvn3lnd8gNCJpvanvr3PV0azIk54xLauoAoKdLEMpK_pc_2tbpC5YevtzPdUeDfwkbjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ، درباره ایران: اگر ایران سلاح هسته‌ای داشت، ما با آن‌ها تماس می‌گرفتیم و می‌گفتیم: «آقایان، آیا امکان دارد که با هم ملاقات کنیم؟»
🔴
ما با آن‌ها به شکل بسیار متفاوتی برخورد می‌کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/alonews/146796" target="_blank">📅 08:42 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146794">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OCC-JbUMgk8Ge1PGDun9_zXXb1dWyTEBFi9kfcsN4IT46d_itAsQyN4XnI3OOBsmsZN8FPQImm7E2NiEKNhZIE-8gfum3AwwkN3jbOiO43yixU4YAn0lzBPSinOuYOwq2BU-B5wA3bCZ-gspKaTjNCEyDoQCMIvWjYcpGycwvTdgi_G2ZKibpNsCHke7nnYjwCrFQIAjdzd3UDWcTZXJ-RFNC_QiGnR7Att9-lwLYsGOxvw208mXNO5V-yVfjlyRBPUmfyIbGfzl0xutzx2AeMdDpAVNiTBH3-srdIbidd0QT5Wy4s26cV14RNKPkx-oRSy607pAZ8_XvUk9Q5NOTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sJ4dZwTMPTPJiA7SoqzhmuTfWx4MyPCwem4-xyUK3fH0wNgjdKJOSRN8omI0qGQiRKMwAiOdk7AbF9NRUNhwN4rzX1wahXx4o7QUl8TCbSnNl_3dwV956CWFS7wdOK9QAUdfLhNxt8BC5FhzT8nIVOaKkwGllAoCVe05p7_V8aDzR_f58q22LCCB3WSLUqzXzvnCeZVGfGnqTF4NlRLw9nfaWfFCaoZTrQczuN0tXvBkKUbvPtI-w_ptXga_2KSKpgJ4-q_PxSJ05aSvZXpyH2rk7LojaEhG_XrSfSUXlx8Dee4MxzDQwwT5_2kT6G5ti_majjhpZVlmD3ClBwrMsA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
در واکنش به تهدید عربستان برای بمباران شدید بندر المخا، محمد الفرح، عضو انصارالله، بندر نفتی رأس‌تنوره را تهدید کرد.
🔴
رأس‌تنوره یکی از مراکز مهم صادرات نفت عربستان در خلیج فارس است و حدود ۱٬۳۰۰ کیلومتر با صنعا و ۵۰۰ کیلومتر با عراق فاصله دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/alonews/146794" target="_blank">📅 08:37 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146793">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
ترامپ به فاکس نیوز: اگر ایران سلاح هسته‌ای داشت، اسرائیل و خاورمیانه را نابود می‌کرد و شهرهای آمریکا را هدف قرار می‌داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/alonews/146793" target="_blank">📅 03:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146792">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
ترامپ: دیشب ۲۲ قایق سپاه رو زدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.3K · <a href="https://t.me/alonews/146792" target="_blank">📅 03:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146791">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
ترامپ: بعد انتخابات جنگ رو تموم میکنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/146791" target="_blank">📅 03:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146789">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
خبرنگار فاکس نیوز: چگونه ایران می‌تواند موشک‌ها را پرتاب کند، در حالی که ما آن‌ها را نابود کرده‌ایم؟
🔴
ترامپ: آن‌ها همیشه می‌توانند موشک‌ها را پرتاب کنند. آن‌ها تعداد زیادی موشک داشتند و هنوز هم دارند. البته ما آن‌ها را سرنگون کردیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.3K · <a href="https://t.me/alonews/146789" target="_blank">📅 02:55 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146788">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2230f2a78e.mp4?token=kgkv7iEEwaXThp_JqKk7V_IihFp3GsJzIptUcWxcozUVamPe4z2MqWvfIF9AU63uroO4IrvPqdkAUGwWioHhMEeNBdZyxuK1TLANkw9DLvXKQG5Xy5I2g07qvOg6ZimPiT5hlfkK6tSfMX9xsdS_2KF3TevLCb2mYT80GgG5sU0vdEO7J-mGKRMkKzZ-31zIZxsm-fVqYTjpu-J581D91Um5ITfpYijS7hQI6Y6VjSkTE08tRb6lPHg_0ZoA92ex23YH-XKpoWeZq7IAWVW3HSADowgRocxps65Q4rA_AEpl8NIWnplPLkmtER5Nckqg8ef6am2gMSUAksCMMLIp3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2230f2a78e.mp4?token=kgkv7iEEwaXThp_JqKk7V_IihFp3GsJzIptUcWxcozUVamPe4z2MqWvfIF9AU63uroO4IrvPqdkAUGwWioHhMEeNBdZyxuK1TLANkw9DLvXKQG5Xy5I2g07qvOg6ZimPiT5hlfkK6tSfMX9xsdS_2KF3TevLCb2mYT80GgG5sU0vdEO7J-mGKRMkKzZ-31zIZxsm-fVqYTjpu-J581D91Um5ITfpYijS7hQI6Y6VjSkTE08tRb6lPHg_0ZoA92ex23YH-XKpoWeZq7IAWVW3HSADowgRocxps65Q4rA_AEpl8NIWnplPLkmtER5Nckqg8ef6am2gMSUAksCMMLIp3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار فاکس نیوز: چگونه ایران می‌تواند موشک‌ها را پرتاب کند، در حالی که ما آن‌ها را نابود کرده‌ایم؟
🔴
ترامپ: آن‌ها همیشه می‌توانند موشک‌ها را پرتاب کنند. آن‌ها تعداد زیادی موشک داشتند و هنوز هم دارند. البته ما آن‌ها را سرنگون کردیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78K · <a href="https://t.me/alonews/146788" target="_blank">📅 02:55 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146787">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا: روز دوشنبه یک بانک بزرگ را تحریم خواهیم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/alonews/146787" target="_blank">📅 02:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146786">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cnHIUaRP2rt97L2CazTKNZ1gmTQmpY5FJIXae63XZKXvFt4pwfvqampxnAJrl3nuJs_t64xYBcwgAPTHv4DLUIpugAJebwn2BDoei72eC0tW10_tqDV5-MnLT6iDEVS6wFi3vQZkhwd95_yYmrk4rkSj_pdOjupnOUr41ZXrzIbXd47nVtuV3DhJztLD2U1HAbmuUPAo2bCXocdk2F9Qh_e-ju1hLTXgfnqJpYr82-KX6Y8tkH3W3GHfCxBMK-akE0Pt21HKxp3vA1JEPfmPkFMTDEhkSTBAA_0wJH5JzWvb7rpGUQfMWwT7gia2QHDWVodv18Tf5u53xi8DwlNffA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
میثم مطیعی، مداح: مردم ایران فقط همینایی هستن که شب‌ها تو تجمعات هستن
🔴
پ.ن: منظورش اینه همین اندک زن‌ها و پیرمرد‌هایی هستن که میان شب نشینی شبانه به صرف چایی و شیرینی و.... تا حوصلشون سر نره خونه، مردم ایرانن
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.5K · <a href="https://t.me/alonews/146786" target="_blank">📅 01:55 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146785">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
حقوق ثابت نماینده‌های مجلس ۵۰درصد افزایش یافت و مزایای جانبی نیز افزایش پیدا کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.2K · <a href="https://t.me/alonews/146785" target="_blank">📅 01:33 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146784">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
جنگ نزدیکه
‼️
نفت 110دلار شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.4K · <a href="https://t.me/alonews/146784" target="_blank">📅 01:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146783">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1771681df.mp4?token=QFOm2bchVt-cJTagwOrhA-lR350FCH32T7UPUOL-MJ3XR0wsFBYxi_m5h-4_UaYRo3Xn64B6mcq_7kSaOjdUmqJWoX4TSbuM1YrdJjeqFaqWzZ-F8OyHu6KpzWQCtuRj_eIwQ8Y4Py09chjwRrmUMEM7Y8f-SQ18aUIcqaggb6hIZvf2IB3lH98F3hDBDz640PY0OL3VV07pNuqWMIBxOCZWpuUw2jbksOvZWV34vCawpF3q25dmcn3DzE_RC9iuFgvwPFB91au5pvz4fdrw5eSdaKa7ILIXudOioibgiItSGjxmcjqk7JRCd5_KbmuB05Ax60PHaqa8oDcdZhgfWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1771681df.mp4?token=QFOm2bchVt-cJTagwOrhA-lR350FCH32T7UPUOL-MJ3XR0wsFBYxi_m5h-4_UaYRo3Xn64B6mcq_7kSaOjdUmqJWoX4TSbuM1YrdJjeqFaqWzZ-F8OyHu6KpzWQCtuRj_eIwQ8Y4Py09chjwRrmUMEM7Y8f-SQ18aUIcqaggb6hIZvf2IB3lH98F3hDBDz640PY0OL3VV07pNuqWMIBxOCZWpuUw2jbksOvZWV34vCawpF3q25dmcn3DzE_RC9iuFgvwPFB91au5pvz4fdrw5eSdaKa7ILIXudOioibgiItSGjxmcjqk7JRCd5_KbmuB05Ax60PHaqa8oDcdZhgfWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جوری که تنگه هرمز بسته شد
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/alonews/146783" target="_blank">📅 01:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146782">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52ab0f48a8.mp4?token=v2mD0ekO2-m9jH6wLADEWyiOox8lxKxOpKkNm9k2JTb4gcQ3lUl05pDEqqpYXFYzvIB8bNWvwcTSjHT3YmUhFEdKKKwUQw9aH7iitcJ4E2vdiitng7ciOt6n3hDpxk53p-is5H3r9k4cwqXf6O-Obd6cydYZXFYhjXRdLO1kb3KToJHsyLuyKusiNGVnuZttbjgEiaeBNEXJ-LUdjat8765KuuPfzmStANJbi3hgIgu425X6JaJiWzJTqDegUXT4MyVQYNkM3Jt21Dge09X9FBCQRwBLLhJUxXkcW-Gkc9Fekx44_ONtExRubYqSuwf2DlZLwYwP3ypzyLEWDtq4HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52ab0f48a8.mp4?token=v2mD0ekO2-m9jH6wLADEWyiOox8lxKxOpKkNm9k2JTb4gcQ3lUl05pDEqqpYXFYzvIB8bNWvwcTSjHT3YmUhFEdKKKwUQw9aH7iitcJ4E2vdiitng7ciOt6n3hDpxk53p-is5H3r9k4cwqXf6O-Obd6cydYZXFYhjXRdLO1kb3KToJHsyLuyKusiNGVnuZttbjgEiaeBNEXJ-LUdjat8765KuuPfzmStANJbi3hgIgu425X6JaJiWzJTqDegUXT4MyVQYNkM3Jt21Dge09X9FBCQRwBLLhJUxXkcW-Gkc9Fekx44_ONtExRubYqSuwf2DlZLwYwP3ypzyLEWDtq4HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یمن موشک شلیک کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.6K · <a href="https://t.me/alonews/146782" target="_blank">📅 00:58 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146781">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
هم اکنون پرواز جنگنده‌های نیروی هوایی ایالات متحده بر فراز آسمان بغداد
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.1K · <a href="https://t.me/alonews/146781" target="_blank">📅 00:46 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146780">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
لحظه انفجار تونل های حزب الله از نزدیک
✅
@AloNews</div>
<div class="tg-footer">👁️ 90K · <a href="https://t.me/alonews/146780" target="_blank">📅 00:30 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146779">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
فارس: قیمت گازوئیل تو آمریکا از ۶ دلار رد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.5K · <a href="https://t.me/alonews/146779" target="_blank">📅 00:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146778">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
امواج مدیا: انتشار گسترده فیلم‌های هالیوودی از مجموعه تونل‌های حزب‌الله که امشب توسط اسرائیل تخریب شد،قابل توجه است.
🔴
یک احتمال این است که این فیلم برای ارائه به ترامپ - احتمالاً توسط هگزت - به عنوان بخشی از استدلال برای تشدید بیشتر تنش‌ها،از جمله حمله به «کوه کلنگ» در ایران، در نظر گرفته شده است. اتکای ترامپ به جلسات توجیهی ویدیویی در طول جنگ و ترجیح او برای نمایش بسیار مشهود نیروی نظامی، به خوبی مستند شده است.
🔴
زمان‌بندی نیز قابل توجه است. حملات اسرائیل همزمان با ارجاع پرونده هسته‌ای ایران به شورای امنیت سازمان ملل متحد، در لحظه‌ای که دولت ترامپ به نتایج ملموس از کمپین فشار تشدید شده خود علیه تهران نیاز دارد، رخ می‌دهد.این ترکیب می‌تواند انگیزه‌هایی برای تشدید بیشتر تنش‌ها ایجاد کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.9K · <a href="https://t.me/alonews/146778" target="_blank">📅 00:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146777">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
رسانه‌های آمریکایی گزارش داده‌اند واشنگتن علاوه بر پشتیبانی اطلاعاتی و هدف‌گیری جغرافیایی حملات علیه حوثی‌ها، یک سامانه هدف‌گیری میدانی و بلادرنگ مشابه سیستم «ماون» پنتاگون در اختیار عربستان سعودی قرار داده است.
🔴
با این حال، در ارتش آمریکا نسبت به مشارکت بیش از حد نزدیک در بمباران‌های تحت رهبری عربستان، به‌ویژه در صورت بروز تلفات غیرنظامی، نگرانی و احتیاط جدی وجود دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.6K · <a href="https://t.me/alonews/146777" target="_blank">📅 00:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146776">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
خبرفوری و مهم
👇
https://t.me/+WZbLEaPPJQUwZDU0
https://t.me/+WZbLEaPPJQUwZDU0</div>
<div class="tg-footer">👁️ 84.4K · <a href="https://t.me/alonews/146776" target="_blank">📅 00:12 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146775">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
فوری / برخی منابع عربی از هدف قرار گرفتن ۲ فروند کشتی در تنگه هرمز خبر می دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.7K · <a href="https://t.me/alonews/146775" target="_blank">📅 00:07 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146774">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
نتانیاهو: امشب، بزرگترین پایگاه ایرانی خارج از ایران را نابود کردیم. این پایگاه، تونل‌های علی الطاهر در لبنان بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.6K · <a href="https://t.me/alonews/146774" target="_blank">📅 00:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146773">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jZ6qOhJwERUBGkSqLTwzwbX4Z4rM9el5TPANxKCpYHC6k3nTO1SQch4CE7ZqJB3VcBF7acjhgpGcHM5YUBGztBtx-8ym-7jHX3ET-xsfWJvO7DSF9ZYb8H_SW1oHvRhQHBDqN_g6kOUaVackjYSCpuxawYktdzCWwiTkaFvK20u78NNMBr4nAxago7CKhdThEostVBqcrRicGk1-e6WIBA0dJGgwLAhCUs9b6RET6Fg31l7zSvdl2Psn8QBKOTRvXPpELT9MptOmnlvaDo0LPbS7VWdSBy3W4AlMx113046TDFL0gHQID4hKzDXumFTC9FBI_wmPuK9RKwdjcGyhNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیویورک تایمز: ونس ترامپ را دور زد؛ مستقیم از فرماندهان ارتش آمریکا ارزیابی از جنگ گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/alonews/146773" target="_blank">📅 00:01 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146772">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
روزنامه یدیعوت آحارونوت در گزارشی اعلام کرد که ارتش اسرائیل خود را برای مقابله با پاسخ احتمالی و واکنش حزب‌الله لبنان آماده می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/alonews/146772" target="_blank">📅 23:57 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146771">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
وزارت خزانه‌داری آمریکا در چارچوب «عملیات طرد اقتصادی» ۱۴ فرد و ۵ نهاد رو تحریم کرد. این تحریم‌ها شبکه‌های پشتیبان کتائب حزب‌الله، حزب‌الله لبنان، تدارکات نیروی قدس سپاه و شبکه‌های دور زدن تحریم‌ها رو هدف گرفته.
🔴
دفتر کنترل دارایی‌های خارجی آمریکا همچنین از توافقی به ارزش یک میلیون و ۴۲۷ هزار و ۲۳۰ دلار خبر داده و اعلام کرده رد کردن بیشتر درخواست‌های در انتظار برای مجوزهای اختصاصی مرتبط با ایران رو آغاز کرده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/alonews/146771" target="_blank">📅 23:52 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146770">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35cc518a6a.mp4?token=Wf7EXmPA3HyfEbwK1ZOw3QvDBNP3klBybqpVZhqrv38q0Nb_4rkauyH_gJyUMxByaRtQfrWMxB0Ao1vFoEs3LU3JEgpEUx01gnmyKmYMlbSdPIjSCavnVSvT01jKLkXuI4vHDIgoU2E4kwbohova2o08_APhT-PHa-ACzkn_WlWrE_NVmgW9gJZ3MI7f7SIp1w47v6W26Rrd_W_nDEPygpwLeUXSIjpH7FrX4cUoBYN2Q9uTCn-ythboSM6gnztp-S0ibysOzE2F4VWMhBi5bY_nNX0CySDZI8XyYrWRbSQM3vHZ83ZrqveTRlVoAJlc_Bqih2zWu3a0sQ_LC6JkAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35cc518a6a.mp4?token=Wf7EXmPA3HyfEbwK1ZOw3QvDBNP3klBybqpVZhqrv38q0Nb_4rkauyH_gJyUMxByaRtQfrWMxB0Ao1vFoEs3LU3JEgpEUx01gnmyKmYMlbSdPIjSCavnVSvT01jKLkXuI4vHDIgoU2E4kwbohova2o08_APhT-PHa-ACzkn_WlWrE_NVmgW9gJZ3MI7f7SIp1w47v6W26Rrd_W_nDEPygpwLeUXSIjpH7FrX4cUoBYN2Q9uTCn-ythboSM6gnztp-S0ibysOzE2F4VWMhBi5bY_nNX0CySDZI8XyYrWRbSQM3vHZ83ZrqveTRlVoAJlc_Bqih2zWu3a0sQ_LC6JkAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: وقتی افرادی را می‌بینم که مدال افتخار کنگره را دریافت کرده‌اند، کسانی که هنوز زنده هستند... بسیاری از آن‌ها فوت کرده‌اند. آن‌ها در جنگ جان خود را از دست دادند.
🔴
نکته‌ی مثبت در مورد مدال افتخار ریاست جمهوری این است که افراد معمولاً از سلامتی خوبی برخوردارند. آن‌ها این مدال را دریافت می‌کنند زیرا در ورزش‌ها پیروز شده‌اند. اما آن‌ها مجبور نیستند مورد اصابت گلوله قرار بگیرند
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/alonews/146770" target="_blank">📅 23:52 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146769">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15fee3e724.mp4?token=ZEl2sxYv2VUaNhzpmd8JVEJnkmNcJDHSeVDtnMGGQLJXPc0FWOJFdG7aotqAE6Li7w4yTBu2oFNXdxRolULwJO14RJA7-C4QPO_hQiBUCPFyWBd5RuE2lhvfp_A4t0EjQN_9LAxXL5UjaMSC8qWqcBedODhpQ8U7NnenjJxfs6LrH9O8sZQJUVvg8_-y_1lJkdZGOCLU7hDmp6ObRmG_ipE8qjDFjr2cBA3T9VWU-l4fglOJK0EV1MyusO8Cmusy6j4zeb9JDUSt2Oj2soapxcb2Cpgnou5EcnirVIjk-iGWDiqXdra9wYiHJ5ciitXxcs7EpIvjDF1Fy6T7LJrlUTyCmWjw_wHdxLR1MF5asx0BXFKg1724OrntonpE_XjmNYZNviFv81My-4Az8ejNmClOSe0gfsPWmbtWgmVaXx4FoGLSZsIvjb2VQXsiKPVRqxaNWCrkU_3-bnYMbwIhXK0TyC0ITOhLxrOlm6QhLT5lwS9eE63F8xjyEsKMAtSnN3uW_3XN5Sun2jsx4lOretq0ZPNpUjP8-LlPLdPkzBdPIvi3bNJzbHKtlnGhPqsTn_EuiQLAxibLpfRAYV2RLAKIklCOwg6lIyC0JwiXG7l5-iX9ZGOZ-NTz366qtlze6CxyOZlC3swK0AI_15CzVRP6xV6S08nuWfRtytO1eRo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15fee3e724.mp4?token=ZEl2sxYv2VUaNhzpmd8JVEJnkmNcJDHSeVDtnMGGQLJXPc0FWOJFdG7aotqAE6Li7w4yTBu2oFNXdxRolULwJO14RJA7-C4QPO_hQiBUCPFyWBd5RuE2lhvfp_A4t0EjQN_9LAxXL5UjaMSC8qWqcBedODhpQ8U7NnenjJxfs6LrH9O8sZQJUVvg8_-y_1lJkdZGOCLU7hDmp6ObRmG_ipE8qjDFjr2cBA3T9VWU-l4fglOJK0EV1MyusO8Cmusy6j4zeb9JDUSt2Oj2soapxcb2Cpgnou5EcnirVIjk-iGWDiqXdra9wYiHJ5ciitXxcs7EpIvjDF1Fy6T7LJrlUTyCmWjw_wHdxLR1MF5asx0BXFKg1724OrntonpE_XjmNYZNviFv81My-4Az8ejNmClOSe0gfsPWmbtWgmVaXx4FoGLSZsIvjb2VQXsiKPVRqxaNWCrkU_3-bnYMbwIhXK0TyC0ITOhLxrOlm6QhLT5lwS9eE63F8xjyEsKMAtSnN3uW_3XN5Sun2jsx4lOretq0ZPNpUjP8-LlPLdPkzBdPIvi3bNJzbHKtlnGhPqsTn_EuiQLAxibLpfRAYV2RLAKIklCOwg6lIyC0JwiXG7l5-iX9ZGOZ-NTz366qtlze6CxyOZlC3swK0AI_15CzVRP6xV6S08nuWfRtytO1eRo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: من شخصاً دوست دارم مدال افتخار کنگره را دریافت کنم، و من درباره آن مطالعه کرده‌ام و قصد دارم آن را به خودم اهدا کنم، هیچ مشکلی در این باره ندارم، اما اجازه ندارم این کار را انجام دهم. باور می‌کنید؟
🔴
تنها کاری که اجازه ندارم انجام دهم این است که آن را به خودم بدهم.
🔴
من فقط شوخی می‌کنم. در واقع، من شوخی نمی‌کنم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.1K · <a href="https://t.me/alonews/146769" target="_blank">📅 23:51 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146768">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6844b8766.mp4?token=gzUsQi9WAop-js0cLXDv0fLOr7LdERFJMmfnVDb5KcDunIvb5pB9e8IZfMP31KhA35N0n31BLYhDBHWUnWOksmC6c0aGWsL1gfOV7S7cgMDPzx4xpveDqdPDM9779WBgqfUkcVK5HkLsUUUTmf36V5Cn7xVHvOpXdXLR8SOe7ipjBJFcbd_TLbgq_fWEGBMDN5BHMrG1Gx7rgMZbGy1joRwEf1V0kDmRRpP39cnGdq4y3KNv6aPN9NAG5SymBBYm5mOzCeTmyChffxhqEnx2aLxu6-ea_zg7W4acXqmbqy5xkXVDIg5bPjGxI-KoFnp7nA-VpokSQ3NKv7Xm3w9iAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6844b8766.mp4?token=gzUsQi9WAop-js0cLXDv0fLOr7LdERFJMmfnVDb5KcDunIvb5pB9e8IZfMP31KhA35N0n31BLYhDBHWUnWOksmC6c0aGWsL1gfOV7S7cgMDPzx4xpveDqdPDM9779WBgqfUkcVK5HkLsUUUTmf36V5Cn7xVHvOpXdXLR8SOe7ipjBJFcbd_TLbgq_fWEGBMDN5BHMrG1Gx7rgMZbGy1joRwEf1V0kDmRRpP39cnGdq4y3KNv6aPN9NAG5SymBBYm5mOzCeTmyChffxhqEnx2aLxu6-ea_zg7W4acXqmbqy5xkXVDIg5bPjGxI-KoFnp7nA-VpokSQ3NKv7Xm3w9iAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه انفجار تونل های حزب الله از نزدیک
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.1K · <a href="https://t.me/alonews/146768" target="_blank">📅 23:36 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146766">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
خداداد عزیزی : فدراسیون پول آپدیت VARهای لیگ را نداده و اصلاً خط آفساید کار نمی‌کند و نمی‌توانند سر صحنه‌های آفساید خط‌کشی کنند و تنها با عکس تشخیص می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/alonews/146766" target="_blank">📅 23:28 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146765">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
صداسیما: بهترین برنج بازار الان کیلویی ۴۷۰ تومنه، گرون نخرید
✅
@AloNews</div>
<div class="tg-footer">👁️ 82K · <a href="https://t.me/alonews/146765" target="_blank">📅 23:18 · 19 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
