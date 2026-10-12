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
<img src="https://cdn4.telesco.pe/file/ZhlkQFHyBR2iTjyGzrG5ckF4J7tIZcQgI9Tr7ZN9jtNe4do8MRda41UhnuMrnSMJKUza8e2WfNt7IRje7y0-HIcsd31ni7HPAFcHDgHRU4qncsNOBfspv-DiedlJ-bTw6zArkLl8QtHb8bRzihmrIWwMgOKmeABsm2RNHqJGwg4mPIdgz_PWhk1Cq3amIwQosozRj6Tl6BrGeV6jNKRXpYTZFadOmfGOVnYfNeIXbiN108rtenfr5AZBidc652wqnEyddGEplDqr-q0kvwvBN0zfXlQW64s5cv07osk2S2kfpxDERXL_LTVNoU-iHGiAlPoxyF50275GrkM0mlPgFw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 104K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-20 11:11:52</div>
<hr>

<div class="tg-post" id="msg-73145">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/291083b4aa.mp4?token=Lt3NeG7K5q_WKkSofaZ5S9tLGuQA-JsxN0Y_I2HBjJ4qm7W8ZBAFqc07S7h9FTyvxHu2ZzA81wliJhYolWnyvWt7J0et1gxQ8WwNivNadC5NvIO6RtKdXs8dHZzcADI34y3fJmip4DUq8Q-gYw6aXxexEBcMFhJ4jgQ66IX10R-YUBmE5Lj4kTbiBcD4_P7f9U62pRfhwDuvL8V8yDZzWuWZQPKwEbpr2rodn7sV-3YMCNvuCSGjskPgFbocp-O1XSM2afMY8rCYxReooBxtcwujIWcztPTLZXzsBs1MgfoGMxqfXWBKw_hZOZV4ObhfETMduutYs6UnGpDdRk2knQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/291083b4aa.mp4?token=Lt3NeG7K5q_WKkSofaZ5S9tLGuQA-JsxN0Y_I2HBjJ4qm7W8ZBAFqc07S7h9FTyvxHu2ZzA81wliJhYolWnyvWt7J0et1gxQ8WwNivNadC5NvIO6RtKdXs8dHZzcADI34y3fJmip4DUq8Q-gYw6aXxexEBcMFhJ4jgQ66IX10R-YUBmE5Lj4kTbiBcD4_P7f9U62pRfhwDuvL8V8yDZzWuWZQPKwEbpr2rodn7sV-3YMCNvuCSGjskPgFbocp-O1XSM2afMY8rCYxReooBxtcwujIWcztPTLZXzsBs1MgfoGMxqfXWBKw_hZOZV4ObhfETMduutYs6UnGpDdRk2knQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتراف رائفی پور به باز بودن تنگه هرمز برای همه بجز جمهوری اسلامی!
@News_Hut</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/news_hut/73145" target="_blank">📅 11:02 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73143">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c29e4b6ff2.mp4?token=BE9DKmi0QQIBAdp40lmFEPqxQebk14Vzaxr6PqhvDuJGcXy0o3MgwNlCJEkoGLLM9wweiqhnG196fybT_VFDUjExRBIXUOfHV0scWEa6vHIbacz64eeDGR_DatRRp13bFdCyxsHGT_Nexh7ntnZr5eDJLOv58IvYiin91F-IE_wvW4rLSafiGqjf6b4MqhYT1UrESqIaX9XCdgAWmk9BZ_Yk3fHiB1WUmcKzvxYUKUY8HRX77c31aBrb_2wFis7lcWDnT6bG0QH8c4HacR3ZbEgbSIspUPNKHZjMHE0fds6UUTStf3AXJ9FqQrnsiPkShTtS9HNLgKGdAXVtJ00bSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c29e4b6ff2.mp4?token=BE9DKmi0QQIBAdp40lmFEPqxQebk14Vzaxr6PqhvDuJGcXy0o3MgwNlCJEkoGLLM9wweiqhnG196fybT_VFDUjExRBIXUOfHV0scWEa6vHIbacz64eeDGR_DatRRp13bFdCyxsHGT_Nexh7ntnZr5eDJLOv58IvYiin91F-IE_wvW4rLSafiGqjf6b4MqhYT1UrESqIaX9XCdgAWmk9BZ_Yk3fHiB1WUmcKzvxYUKUY8HRX77c31aBrb_2wFis7lcWDnT6bG0QH8c4HacR3ZbEgbSIspUPNKHZjMHE0fds6UUTStf3AXJ9FqQrnsiPkShTtS9HNLgKGdAXVtJ00bSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زینب ابوطالبی، مجری صداوسیما که سال ۹۸ گفته بود «مملکت مال حزب‌اللهی‌هاست، هرکی نمی‌خواد بذاره بره»، طبق گفته محمدرضا باهنر از ایران مهاجرت کرده!
@News_Hut</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/news_hut/73143" target="_blank">📅 10:33 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73142">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b195be8e00.mp4?token=dZJcVmRTJcMN-o7gagj6JehNXKdBjdiw3gr6GoAkuNMiJa8szBqZv4jWccKpUHJ4w_Ogmvg5GyjnIb_Gq9xE_MG3BQwxEpZP6ErlQj0ReXMQuBcOhTMNT0NKEVku7NJjCfsfBQUYCywiicndk-N9X7rU0lMxFeTkrioyiIQ73gSCr8flxBTaeqorkAv08vYIY5QX50Z40dF6j_KiWRx8oMepHFHSaMwLt4b4TC5SVdcuSFMCfmlYL5GXyJ300zLv3JyJP2PMe9Uzc0gcTf-bvvdzD9XIP8EfKWeJcG8NP2NBUraY1EhYgHWK0q1v5Pk0q2fwuxeMXae1NMfpzi9EmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b195be8e00.mp4?token=dZJcVmRTJcMN-o7gagj6JehNXKdBjdiw3gr6GoAkuNMiJa8szBqZv4jWccKpUHJ4w_Ogmvg5GyjnIb_Gq9xE_MG3BQwxEpZP6ErlQj0ReXMQuBcOhTMNT0NKEVku7NJjCfsfBQUYCywiicndk-N9X7rU0lMxFeTkrioyiIQ73gSCr8flxBTaeqorkAv08vYIY5QX50Z40dF6j_KiWRx8oMepHFHSaMwLt4b4TC5SVdcuSFMCfmlYL5GXyJ300zLv3JyJP2PMe9Uzc0gcTf-bvvdzD9XIP8EfKWeJcG8NP2NBUraY1EhYgHWK0q1v5Pk0q2fwuxeMXae1NMfpzi9EmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبتای این خانم در مورد کادوی روز دختر و گل‌های چند صد میلیونی که این روزا بلاگرا به پارتنرشون کادو میدن، حسابی وایرال شده:
@News_Hut</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/news_hut/73142" target="_blank">📅 10:05 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73141">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/479627e865.mp4?token=Zp-uMfAG7W5dfJH6WUzJC4I9t6-27OKNjLKl5wPgABvidlhcQcXZOatArAsciL0Lfi7GCEk4wr0YQ9tSC5c2SJCZb_R1ol3F4U2AwimvcKtHnJNWF4bz87Y7Dqs4xi2fPkgAwFn2wUP2FJYZX1AlsICY5EurfWQ6pE5fOcNogqI4W0nKG6MiVOM0oDmQcI1lHLlV7yrcTms9tWsoca57UXk3EAlymCTOSOLm8DVK7-kE_vP-SDthyd38KdmAMyiskR_GuPoxcaaYr9VA4TRHfF5PiAqGueFHrLBqgPIhYOFEn17Sdj8A7Yb04PGOqLStMuTI8QLTHnwm8hyHJFXXyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/479627e865.mp4?token=Zp-uMfAG7W5dfJH6WUzJC4I9t6-27OKNjLKl5wPgABvidlhcQcXZOatArAsciL0Lfi7GCEk4wr0YQ9tSC5c2SJCZb_R1ol3F4U2AwimvcKtHnJNWF4bz87Y7Dqs4xi2fPkgAwFn2wUP2FJYZX1AlsICY5EurfWQ6pE5fOcNogqI4W0nKG6MiVOM0oDmQcI1lHLlV7yrcTms9tWsoca57UXk3EAlymCTOSOLm8DVK7-kE_vP-SDthyd38KdmAMyiskR_GuPoxcaaYr9VA4TRHfF5PiAqGueFHrLBqgPIhYOFEn17Sdj8A7Yb04PGOqLStMuTI8QLTHnwm8hyHJFXXyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش شبکه یک صداوسیما:دانش آموزان معترض فرانسوی، می‌تونن بیان تو مدارس ایران که همگی فول امکانات هستن، تحصیل کنن.
شما هیچ معلمی ندارید، پلیس هم داره دستگیرتون می‌کنه.
ما اینجا کلی معلم اضافه و کلاس خالی داریم.
اینجا ما آرامش داریم و همه چیز عالیه.
@News_Hut</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/news_hut/73141" target="_blank">📅 09:32 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73140">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22084c4b3c.mp4?token=WahmhNzVg4qOy1nOd8gUttzA_i5ivOhpSSXCEucBUnbisGWCK77cp8AhCGrFkllCnG3QIPHW_-Afq1CkGLpc0afLfvRlT0ZDks4Mwq0L47C3nXQcLefx8TzalKRByyw-wq5IlnBO0qzB08sUhH87nNmWlhZwwLffLyOcwmD__15D2HBKUu-mJDv4bLBss0jUh_2g8baNXdLxvc7wpciDnpW3IpkwXI79qguaSBpdIK6kBnEGXiwNkELtw84Lkm2tFn_E9qSnjjOXwMC2yJpa4tMwjy-tM4UM8f4OgBmA3qux9YBCHp8Vv0Cm_WwZ9GkJC7KDKVVidp1ZEATAUTnDxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22084c4b3c.mp4?token=WahmhNzVg4qOy1nOd8gUttzA_i5ivOhpSSXCEucBUnbisGWCK77cp8AhCGrFkllCnG3QIPHW_-Afq1CkGLpc0afLfvRlT0ZDks4Mwq0L47C3nXQcLefx8TzalKRByyw-wq5IlnBO0qzB08sUhH87nNmWlhZwwLffLyOcwmD__15D2HBKUu-mJDv4bLBss0jUh_2g8baNXdLxvc7wpciDnpW3IpkwXI79qguaSBpdIK6kBnEGXiwNkELtw84Lkm2tFn_E9qSnjjOXwMC2yJpa4tMwjy-tM4UM8f4OgBmA3qux9YBCHp8Vv0Cm_WwZ9GkJC7KDKVVidp1ZEATAUTnDxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که روبیو درباره خشایارشا صحبت کرده و باعث شده عده زیادی از طرفدارای حکومت عصبی بشن، یادی کنیم از مصاحبه قدیمی خامنه‌ای درباره خشایار‌شا که دوباره وایرال شده؛ جایی که می‌گه خشایارشا با بیش از یک میلیون سرباز به یونان حمله کرد، شکست خورد و هیچ منفعت ملی‌ای برای ایران نداشت!!
@News_Hut</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/news_hut/73140" target="_blank">📅 09:02 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73139">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/73139" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/73139" target="_blank">📅 01:41 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73138">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qaVyTyM5_QxpCcudLLy0GJc2sBamo-IuNdy5WjEdqNN0zyIJkxgR5TKZmOueJj91PeiBqij4sLVas_Tw1puuUV8fRoxZTAhLO_h8npWs0xL6mnQGf0ak9iGAeErN3VXtCfPc1hoG69qTagBlmsZLAnlyHEweRBCqEx-CZkccAlFnr-ElLuBlJMYVTRf6onT2CXCmx18INaeXBOzxN858h_RfSo7sED4XPReyKUJCBUHZv8z0rbD75FIddEt_uScaZPjVbSQqqK5O9g-YRcVcY52EL_-wcXHGLAi3QQ0R68mH1v5EoXCtDGq3gyUQ4tlR5IXZEWKMMWjzayhpsDxJBw.jpg" alt="photo" loading="lazy"/></div>
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
[
قوانین رو در سایت مطالعه کنید
]
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
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/news_hut/73138" target="_blank">📅 01:41 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73137">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fi9WKRvstiP1My3ojy8x3Pkk9swCs-1EGVqZ78adqPaYoSKs9-ff3H9CQzTlr0zIB2VoyFzSxWNhpXK9gIhX-AuiHO6KQVXB4iwVCMWcVHwaey7tiSP4IU9bMhi8DfJwltCV8_99QdEZehyPS6D6-L8_6eKymITiUvlKZXkotBvVx61LiwBZaNgONDJ5q6NjRCuWwBdG8V9Xya6WUwFUUaijrt-UcCg-0uwm6-4zBuvqggH-DarGhRc9SwpGhGsaTB-WBYvWdJ6AZTB0DRtdxVtCT0dDSNwZuQQm725ha5SHMpltyYl1U6DJF1LppXJDsSOTpozfZt-Ne262Xt3Nyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی:
«آمریکا با بعضی از شروط هفت‌گانه ایران موافقت کرده، اما از نظر ما پاسخ آمریکا کافی نیست.
دیپلماسی ایران تغییر کرده و دیگه اوضاع به شرایط قبل برنمی‌گرده.»
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/73137" target="_blank">📅 01:01 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73136">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ویدئوی لحظه اصابت موشک حوثی‌ها به فرودگاه ریاض
تصاویر دوربین‌های مداربسته، لحظه اصابت موشک بالستیک حوثی‌ها (انصارالله) به ترمینال ۳ فرودگاه بین‌المللی ملک خالد در ریاض، در روز گذشته رو نشون می‌ده.
بر اساس این گزارش، دست‌کم ۱۳ نفر کشته و بیش از ۳۰۰ نفر زخمی شدن.
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/73136" target="_blank">📅 00:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73135">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c13d27cb81.mp4?token=SF9GZ7nxWQ7KWbM5nIbHyD9unfzuhxhluU6e3V4qxtJUpW6Vt4ZAOQ6g-aOD43DURcwCEpJOJi0LyQdS2lVC0l-1TrQGh8V7Y_OG-F5r_RKF0ENhCjL3VH5BbnxzfVnVsMaURQAVfCHeUiaJDVwitb0YMyrBs4qaUanINLiJt4SrgwPwfQnV5iyW6a2SaiTgpxTOs4tZjsqtTU4lXpmTq0IPX_O2H92DWCJCqX-NE1SbeAAcw7GAemTbtSKZyWRltmwIeUlAvyPEDqddpajsF863OqdKsMnvNebvHUrXeJNWlkwVABRmNz6GlpJa3trfX8G2gy8yOWt0JFkMNNoOjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c13d27cb81.mp4?token=SF9GZ7nxWQ7KWbM5nIbHyD9unfzuhxhluU6e3V4qxtJUpW6Vt4ZAOQ6g-aOD43DURcwCEpJOJi0LyQdS2lVC0l-1TrQGh8V7Y_OG-F5r_RKF0ENhCjL3VH5BbnxzfVnVsMaURQAVfCHeUiaJDVwitb0YMyrBs4qaUanINLiJt4SrgwPwfQnV5iyW6a2SaiTgpxTOs4tZjsqtTU4lXpmTq0IPX_O2H92DWCJCqX-NE1SbeAAcw7GAemTbtSKZyWRltmwIeUlAvyPEDqddpajsF863OqdKsMnvNebvHUrXeJNWlkwVABRmNz6GlpJa3trfX8G2gy8yOWt0JFkMNNoOjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو یکی از مدارس پسرونه، اسپایدرمن تبدیل به اسپایدرعن شد :
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/73135" target="_blank">📅 23:32 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73134">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cad58aeb38.mp4?token=K5dZ972oeY7oyZGaaPoDFSHJSB_3v7FJKN9VczOJOMC4KLL_J2e2ZU5lCnrZggo7uR4GQx2ftJJbJRIMLowQ4mzCJ2rqWPSViBCAQpTiW5EFO2rNSWK0aX2f606YB9_VGbPHvyxQJw8BcXy29B2koSF9OqfkWQHbce1z6rGFX8mFnpeP7B7lw9Ux-wOodNlCzEpiyk8N2FWVZN7cVGtnJkydHUDJg0vsGiBUIZDdH4FxMx_kY1ArkSj37gqt0AaM3yyoLYj-ZO8whcrzU8pkM2LmEQS5O7RqMlL_-M7i5sQZdfjzXUw_n2YK7T3GleH3iru1HKN7mXUOEyzQinBIpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cad58aeb38.mp4?token=K5dZ972oeY7oyZGaaPoDFSHJSB_3v7FJKN9VczOJOMC4KLL_J2e2ZU5lCnrZggo7uR4GQx2ftJJbJRIMLowQ4mzCJ2rqWPSViBCAQpTiW5EFO2rNSWK0aX2f606YB9_VGbPHvyxQJw8BcXy29B2koSF9OqfkWQHbce1z6rGFX8mFnpeP7B7lw9Ux-wOodNlCzEpiyk8N2FWVZN7cVGtnJkydHUDJg0vsGiBUIZDdH4FxMx_kY1ArkSj37gqt0AaM3yyoLYj-ZO8whcrzU8pkM2LmEQS5O7RqMlL_-M7i5sQZdfjzXUw_n2YK7T3GleH3iru1HKN7mXUOEyzQinBIpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان: اگر لازم باشد برق اتاق‌های دولت را خاموش می‌کنیم اما نمی‌گذاریم چرخ کارخانه و تولید متوقف شود. مردم همکاری کنند فشار دشمنان شکست خواهد خورد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/73134" target="_blank">📅 23:01 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73133">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67b9ee6a71.mp4?token=gE-S6nuK696uAH7Pkdqv0Od_vZCG1GjD6t5uwzORBgSa_PvJ5mAv-iYnYBRTJPG_wh72Pe0wxPimwfjhYqtVWZtbQsoCzRkp3lsmAHYX4e9q3JKbnjqxZM3LHNc-fQzT7VQiuRvY-FWT5DhBDpCNuUCF2c9QLFLPgzxAPYho9qPU5xhiiL3tay14IIVMN8L23ao54dtP39GzXAtuTKZkgGEz-FrvJKlSv4AAE0mIG4MBvlzCElYS4qjskESKL5jKeTWGbOnPSzkXmSouDpQ5G-J1CcJ4nq3Oho67inCWkSXbRuiv_YUHAnhPFq6K-uNkKTGgGEKXdOnGZd30BfASHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67b9ee6a71.mp4?token=gE-S6nuK696uAH7Pkdqv0Od_vZCG1GjD6t5uwzORBgSa_PvJ5mAv-iYnYBRTJPG_wh72Pe0wxPimwfjhYqtVWZtbQsoCzRkp3lsmAHYX4e9q3JKbnjqxZM3LHNc-fQzT7VQiuRvY-FWT5DhBDpCNuUCF2c9QLFLPgzxAPYho9qPU5xhiiL3tay14IIVMN8L23ao54dtP39GzXAtuTKZkgGEz-FrvJKlSv4AAE0mIG4MBvlzCElYS4qjskESKL5jKeTWGbOnPSzkXmSouDpQ5G-J1CcJ4nq3Oho67inCWkSXbRuiv_YUHAnhPFq6K-uNkKTGgGEKXdOnGZd30BfASHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این کلیپ مربوط به پشت‌صحنه یه تئاتره؛ جایی که همه با هم دست می‌دن و همدیگه رو بغل می‌کنن.
+ عرزشی‌ها هم از این صحنه به خشم اومدن و می‌گن باید این بساط جمع بشه؛ حالا هم افتادن به جون عوامل تئاتر!
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/73133" target="_blank">📅 22:16 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73132">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3915a2c4be.mp4?token=bryAnmdIHFW8ToqfKBPF4E19DKa27Y28at_c7m994YT4yudIW1Rm3EXuodKcfnhCTar0LbCTNKhVLrEozTT1Kk9rA6KxLwcM636dzScMDfjvtPxZ_vyUwHWZfeU2h0_BVjCye8j0k84MVoJ8lwNJC-r-W3ruFZRsQGLR4h0M1Md8tTvwY66wxuHZnVCxXb4yPo1fYdCmMI7Ppdfm_h7YhfIOGPc5X_tqIc6_e6r_DXPkfguMdsiQXuWgOotYInmD8TO2NogtNbJ6KO5Tddp5SyNybbEd13q-uXcRs3fG-thGniDKIS5JpGnDb_fBr2wttIW_Epo_5zhh-Iu0WLyDtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3915a2c4be.mp4?token=bryAnmdIHFW8ToqfKBPF4E19DKa27Y28at_c7m994YT4yudIW1Rm3EXuodKcfnhCTar0LbCTNKhVLrEozTT1Kk9rA6KxLwcM636dzScMDfjvtPxZ_vyUwHWZfeU2h0_BVjCye8j0k84MVoJ8lwNJC-r-W3ruFZRsQGLR4h0M1Md8tTvwY66wxuHZnVCxXb4yPo1fYdCmMI7Ppdfm_h7YhfIOGPc5X_tqIc6_e6r_DXPkfguMdsiQXuWgOotYInmD8TO2NogtNbJ6KO5Tddp5SyNybbEd13q-uXcRs3fG-thGniDKIS5JpGnDb_fBr2wttIW_Epo_5zhh-Iu0WLyDtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروی دریایی سپاه مدعی شد سومین نفتکش از دیروز تاکنون در جنوب تنگه هرمز با مین دریایی برخورد کرده و دچار انفجار و آتش‌سوزی شده است.
سپاه هشدار داد با کشتی‌هایی که سامانه‌های ناوبری و شناسایی خود را خاموش کنند، به‌شدت برخورد خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/73132" target="_blank">📅 21:37 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73131">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11e4cb03a5.mp4?token=JTMYakcFcbVy4tCF-yWhDtch2DMt5LHJ4QYDdJZ1bOCc82qy1gL7SBmnYNSvm_LA9RGccmJn3lYbpI1GAQQXqochgOpHjCg_MaIPhTtUi07kceKVbImi8RAR2MLevo3HSp1VvqpwAoIzrfsQreygcOVzbgWaDAEA4Zc-rLnJOzBV8g3hieHZF8ZDC5Dt4dx7yzSsIrQS-yUU5EBXS9JJoxuF_li_mwC1JEVIG33ATU2poqSqV9hWF7X3c4ye48yJwV0aDLTetZN2ag4wKGlQfREOLV1gi4uSIMDfzxVGRTwZ7uDiW4qmgE-WYo03bCGuPVMA57VhQUZa0oZ5ghlbww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11e4cb03a5.mp4?token=JTMYakcFcbVy4tCF-yWhDtch2DMt5LHJ4QYDdJZ1bOCc82qy1gL7SBmnYNSvm_LA9RGccmJn3lYbpI1GAQQXqochgOpHjCg_MaIPhTtUi07kceKVbImi8RAR2MLevo3HSp1VvqpwAoIzrfsQreygcOVzbgWaDAEA4Zc-rLnJOzBV8g3hieHZF8ZDC5Dt4dx7yzSsIrQS-yUU5EBXS9JJoxuF_li_mwC1JEVIG33ATU2poqSqV9hWF7X3c4ye48yJwV0aDLTetZN2ag4wKGlQfREOLV1gi4uSIMDfzxVGRTwZ7uDiW4qmgE-WYo03bCGuPVMA57VhQUZa0oZ5ghlbww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم وایرال شده از جشنی که یه خونواده، برای اولین پریود دخترشون گرفتن:
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/73131" target="_blank">📅 21:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73130">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa77f7e16d.mp4?token=sQ0qIcA_JXq4gHOqOVKjTxRk1x5NTnbk5dtQX4Gx1hqyuzT1m36t_RO1XcTEf3in4XsmyD5qtkLu8QfkgYNZTwKuCwD905mGFLoDtY0Ey5TtB_AAh9wh4NRDJAyVtzNjPmrqJBOqNW7Vs8PB8BuUbVeiHUqvfmMKi-oIEtNwNtw7r55-G3zjEZ-wJC5FyusACrTzKQBa3NAjd5RQEL_nFPgXGI6NIEH0k7jIQ50IhPgMTqO7lpCh1WPipHktU2hMwpq5ka52tspYFe9oc4qIKuFCKm0Z3aSwGHmQnj95ReKtyF_JVy3HOhPhJNdv-3GoFbks5d6fQI_iEcR3uRxOBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa77f7e16d.mp4?token=sQ0qIcA_JXq4gHOqOVKjTxRk1x5NTnbk5dtQX4Gx1hqyuzT1m36t_RO1XcTEf3in4XsmyD5qtkLu8QfkgYNZTwKuCwD905mGFLoDtY0Ey5TtB_AAh9wh4NRDJAyVtzNjPmrqJBOqNW7Vs8PB8BuUbVeiHUqvfmMKi-oIEtNwNtw7r55-G3zjEZ-wJC5FyusACrTzKQBa3NAjd5RQEL_nFPgXGI6NIEH0k7jIQ50IhPgMTqO7lpCh1WPipHktU2hMwpq5ka52tspYFe9oc4qIKuFCKm0Z3aSwGHmQnj95ReKtyF_JVy3HOhPhJNdv-3GoFbks5d6fQI_iEcR3uRxOBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی سازمان انرژی اتمی: منافعمان را یا با دیپلماسی می‌گیریم یا با نبرد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/73130" target="_blank">📅 21:03 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73126">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bf520c338.mp4?token=W-8GFaMV6gREUQs0D0BliJKyUW-31qf1EdfKTAQlZJ-VxQ5qH9ICNKf6m71qPK3S09Hi4Z1HNa3vIBmvRXgBjrvwgAzrpsW91Hqr_RsV5Cbrvp_F8bWysq2nkzQ1Fsqt_Q1ryiKXMlxR04_MlGIx2qMqN1S1cTcVN7j1xkXfHaioRrPz_Csjwo5-YclYISNprNXPVVb2b5pyNYXKXikHt2aQdLSeRDOzARO5sBNfTnNvQSeKBT1l525tPv4GLuXSiRYR1qbHqgDD5YOvbzenMFI8cFH1LymCtvPvqVCq7U8rgDZUHbPOc95_eADUwV6tR4oeVnzHVWbgwkv-RgfHfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bf520c338.mp4?token=W-8GFaMV6gREUQs0D0BliJKyUW-31qf1EdfKTAQlZJ-VxQ5qH9ICNKf6m71qPK3S09Hi4Z1HNa3vIBmvRXgBjrvwgAzrpsW91Hqr_RsV5Cbrvp_F8bWysq2nkzQ1Fsqt_Q1ryiKXMlxR04_MlGIx2qMqN1S1cTcVN7j1xkXfHaioRrPz_Csjwo5-YclYISNprNXPVVb2b5pyNYXKXikHt2aQdLSeRDOzARO5sBNfTnNvQSeKBT1l525tPv4GLuXSiRYR1qbHqgDD5YOvbzenMFI8cFH1LymCtvPvqVCq7U8rgDZUHbPOc95_eADUwV6tR4oeVnzHVWbgwkv-RgfHfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی امروز گسترده‌ترین رزمایش نظامی خود از ۲۸ فوریه تاکنون را با مشارکت سپاه و نیروی هوایی ارتش برگزار کرد. تصاویر منتشرشده، پرتاب پهپادهای انتحاری شاهد-۱۳۶ و موشک‌های بالستیک و پرواز جنگنده‌ها بر فراز تهران و شهرهای دیگر را نشان می‌دهد؛ تحرکاتی که می‌تواند نشانه آمادگی ایران برای دور تازه‌ای از درگیری باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/73126" target="_blank">📅 20:14 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73125">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">محسن رضایی:
«اگه جنگ دوباره شروع بشه، خیلی از کابل‌ها، دیتاسنترها، مراکز هوش مصنوعی و زیرساخت‌های دیگه تو منطقه نابود می‌شن.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/73125" target="_blank">📅 19:29 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73124">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fW-gJb0leROaxJ2RoSOurEkRYKve5D8zbZx8ehY0ja-d8CsipprPimOdGT4pJd4FdeGaROkO69yefkgNjpsYTNmoXQ8tNaHUfpYGm529msgCHa0c_MUaITdmUrPuv47sEZAbKaiju-mFHAlK_6rrAb3GU_0gff-txEAUjZxWEG-fZiP7lLpJPnqLYbN6Un1LUTqtkwtzXAgkhyXbfe5yAOjVpYULuGLr7e-XxEHHkyxeVlWuukVFS32PaISUTdFyqoBHi9m8xFo-E15qh1dUyenWt1kCwgQqXyO2BL14YEbK-QSZhsa5fEYZaNEeVt8vKZAhbkcG9T5rkl9hiMLVug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی، دبیر شورای عالی امنیت ملی:
«ترامپ به قاچاق روی آورده و با استخدام تعدادی مجرم که در آب‌های ساحلی عمان فعالیت می‌کنن، این کار رو پیش می‌بره.
اون هر روز ادعا می‌کنه تنگه هرمز بازه؛ اما من در پاسخ می‌گم شما مشغول قاچاق هستید، در حالی که تنگه هرمز تحت کنترل ایرانه و ما مدیریت اون رو در دست داریم.
طی چند ماه گذشته، هر شب پنج شناور مورد استفاده قاچاقچی‌ها رو در تنگه هرمز هدف قرار داده‌ایم.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/73124" target="_blank">📅 18:59 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73123">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee20290170.mp4?token=N8u0KRbKofWGMYEYqDwLZYt0AmyvatkQFTjaRAaCK9dC8UA-92HGNY76WvqdOansZ_-lAkukwjVkJ3ikov1zMp-nhecMkucv1zzHCYRGbbyPULsVXi8ESVqOLpoz1IUk3QjQiz1v6MPc1tKJWYRFtrsSm7uZ4NaC5mE9bCGUFD6Qx8ngLrQqd8wyNWRrTAmCB9FEoCtgflExNs-DqAuUckqf-N-pco3n_6eDkZOrE36F9lD6Z7kpwqmEHz_zZEgZfF6P1PCeLqhIteLmlKWzTdw5kR8hYiNiwHG0wHmJyZ_RD8KYgrB71LnD8aVBksvd97XiuOWJyFfucc_y7WoRhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee20290170.mp4?token=N8u0KRbKofWGMYEYqDwLZYt0AmyvatkQFTjaRAaCK9dC8UA-92HGNY76WvqdOansZ_-lAkukwjVkJ3ikov1zMp-nhecMkucv1zzHCYRGbbyPULsVXi8ESVqOLpoz1IUk3QjQiz1v6MPc1tKJWYRFtrsSm7uZ4NaC5mE9bCGUFD6Qx8ngLrQqd8wyNWRrTAmCB9FEoCtgflExNs-DqAuUckqf-N-pco3n_6eDkZOrE36F9lD6Z7kpwqmEHz_zZEgZfF6P1PCeLqhIteLmlKWzTdw5kR8hYiNiwHG0wHmJyZ_RD8KYgrB71LnD8aVBksvd97XiuOWJyFfucc_y7WoRhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طبق گزارشات رسانه‌های عربی حوثی ها مجددا به فرودگاه ریاض حمله کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/73123" target="_blank">📅 18:53 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73122">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">زلنسکی در گفت‌وگو با باراک راوید:
«اعلام آتش‌بس برای من هم خبر جدیدی بود. اما اگر روس‌ها با آتش‌بس در حوزه انرژی موافقت کنن، اوکراین هم موافقت خواهد کرد.
اگر رئیس‌جمهور ترامپ این توافق رو با پوتین مذاکره کرده، لطفاً به ما بگید آتش‌بس از چه زمانی شروع می‌شه. ما آماده‌ایم و این توافق رو می‌پذیریم.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/73122" target="_blank">📅 18:28 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73121">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tTGXL2q9qwQk8BDeXEYd8MkuWOPGp4PRpGppS6FCnXP6RVJDBWgVMicqcwUQ-_kh8g66YIbIsSzh_TEFcD--0ciqRXQbif_U3VZoFL3J7PNzlOCK2FFUJD-wqdwVT4gIFVJFAdet9WdqfSVYbTDps4Lib_nYNs-hUDYvjRo-vfxwIcELKKAngSss0bifi_jdK2auR4IDkVAmCovKaltSphuToLLnGaq9FalAXYdK_0S5ti9-bjDscB0OicLtAclAkFBm0GRscuqJ5aUhxcI__hESpQIHS83C_XfLxs9CImKlPqD35jgCQyM_VWKHZ6gClwly67zqLkecPWK3trV0FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ از آتش‌بس انرژی بین روسیه و اوکراین خبر داد
«از همین لحظه، آتش‌بس در حوزه انرژی در جنگ روسیه و اوکراین برقرار می‌شه.
هر دو طرف با این توافق موافقت کردن. این آتش‌بس رو نقض نکنید!
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/73121" target="_blank">📅 18:14 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73120">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/73120" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/73120" target="_blank">📅 18:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73119">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gz8-Fo5AB8jJbOZnMrxAOA8UxcofpxzwIkwTWFszJb05hwFNWf56iiQqFgNmSWjjM5U1wXdnAN2E7G1GpdvWXwQwgIzNYAoU3EE_Pgww7HLowwee90u9cRtw7gSg4fJQZhLjBpA_Lk7nRsFqKMbE2ojkAlc0H8Y68XM6l0XGCvARlUR6RdnaxnevqbBg8WulKxJVvtxZnlr9FILWYYAdej0ckzrnE8vs3V6QatAikuCe4_vuXomiPOZFKwnekfT-U6NVFhtFYCLsRmJ2JZpZbKuQ8cwCxyFHQD-Ebl0JYwGD6Nru7Pl_AeCY83ZOUtSXR_SiONFdNWKP0p0rTjZu2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان انگیز منچستر سیتی
🆚
لیورپول
را در
TrexBet
پیش‌بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
منچستر سیتی: ۵ برد و ۱۴ گل زده
لیورپول: ۴ برد، ۱ تساوی و ۸ گل زده
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
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/73119" target="_blank">📅 18:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73118">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb6d17c940.mp4?token=bFWnSVR5EbGbS2t6aKruAtr15dKGRVtBN_yePede-N4Dax73elX1nCa-hiV9RrXPjSQ3cXBIRQZMZcx3845cJ1JrPItPbURdzsD_1gB_MdEyse_ZseBh9QKjUKVj9c9nJpg9NdePOyHhV0NWWUiGlIaA9BxlSbgasfF7PKx0SPA1uQ1-tDhKaTGiCQ_etAhcBdR6T2dr0MQsg8X3Mpz8IA9KOqvtEhr5lKK1gRpZ350Sc1ELek-4teQVkRZZjh5i4Y3rbM06B9iMf1d_YTmuzMLFzHVguk81yEY7TSEmWdOIOVnAdcYPL-ruOlip4GW4wttNnQ72ziKA6DIX3ImJqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb6d17c940.mp4?token=bFWnSVR5EbGbS2t6aKruAtr15dKGRVtBN_yePede-N4Dax73elX1nCa-hiV9RrXPjSQ3cXBIRQZMZcx3845cJ1JrPItPbURdzsD_1gB_MdEyse_ZseBh9QKjUKVj9c9nJpg9NdePOyHhV0NWWUiGlIaA9BxlSbgasfF7PKx0SPA1uQ1-tDhKaTGiCQ_etAhcBdR6T2dr0MQsg8X3Mpz8IA9KOqvtEhr5lKK1gRpZ350Sc1ELek-4teQVkRZZjh5i4Y3rbM06B9iMf1d_YTmuzMLFzHVguk81yEY7TSEmWdOIOVnAdcYPL-ruOlip4GW4wttNnQ72ziKA6DIX3ImJqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت درباره ایران:
«نمی‌دونم این ماجرا چطور تموم می‌شه؛ هیچ‌وقت نمی‌شه از قبل دونست پایانش چطوریه. دیوار برلین هم بالاخره یه روز، یهو فرو ریخت.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/73118" target="_blank">📅 17:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73117">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4be03fff7.mp4?token=nGXWvdaBHuMOp13va-2ti78aE-9q_DT_gvuIoLg0qEmUZIHosKYouQyjYp58vygqbnrNRze1k175a-af1TdbOPRNeqVvnjfjttfhO0SezERVDqzJCvWpKeq0DmmmqsDxIPalm6Bu8kWeQFrvZcPaHT9dwIxytBF6YXo8n8eyo3gOseIaQ3JR1h9zZsAb4Sr1L4UfXyKm2Jo6_6D_yMXn5AWqG9jEbOUsFgkmZ9_J6xeXmI1Ga-tqDnjFy_Vn8hzxaWHSyyI2CYtdInK5HBR14DsGeU5ozTrWWdgl9M9GKS8fVKlXqAqNh7tEjx88i0yjMNxgeSRRb_1qNUXgtdqe_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4be03fff7.mp4?token=nGXWvdaBHuMOp13va-2ti78aE-9q_DT_gvuIoLg0qEmUZIHosKYouQyjYp58vygqbnrNRze1k175a-af1TdbOPRNeqVvnjfjttfhO0SezERVDqzJCvWpKeq0DmmmqsDxIPalm6Bu8kWeQFrvZcPaHT9dwIxytBF6YXo8n8eyo3gOseIaQ3JR1h9zZsAb4Sr1L4UfXyKm2Jo6_6D_yMXn5AWqG9jEbOUsFgkmZ9_J6xeXmI1Ga-tqDnjFy_Vn8hzxaWHSyyI2CYtdInK5HBR14DsGeU5ozTrWWdgl9M9GKS8fVKlXqAqNh7tEjx88i0yjMNxgeSRRb_1qNUXgtdqe_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت درباره ایران:
«اگه این ایرانی‌ها کشورشون رو دوست دارن، خب تبریک می‌گم؛ می‌تونن همون‌جا بمونن!
این فشار مستقیماً به نخبگان و مقام‌های حکومتی ضربه می‌زنه؛ دیگه نمی‌تونن برن لندن و اقوامشون رو ببینن، تو پاریس به دیدن دوست‌دخترهاشون برن یا به پول‌هاشون در سوئیس دسترسی داشته باشن.
اونا از دنیا جدا شدن و ما به ادامه این فشارها ادامه می‌دیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/73117" target="_blank">📅 17:33 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73116">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cfeac3aa6.mp4?token=lr4jiKPRh0QITzI3PmvFfSOSytVGTxVNg7CV_uIus2RsUAS2AmLXaXoo8nCcitbqn64r46j2U7yODQxRmryQ9088JMTpM_kTJ1x3fwO7blPEBfucxjQSk47L9OMM85pRtxWQ1_wpy-bGYg9lmDTEjx-XLVpWr1zoYTLejVgcFpPESTgx_g4BtF1SaFCUkWRdVKxqbD9dgjVypyOszb7SYb7vkTAN4DgO9AomvMHz0pUAJ0u93YxvwyaOwxnFniauftnasm0EklT3y7jOoVJYK7NXoMmoWqymcdsEQuhBBRw6r6Y_DIK8fufOYNFB1fIK1u4JlxUO3SgHPCHJX1Z-7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cfeac3aa6.mp4?token=lr4jiKPRh0QITzI3PmvFfSOSytVGTxVNg7CV_uIus2RsUAS2AmLXaXoo8nCcitbqn64r46j2U7yODQxRmryQ9088JMTpM_kTJ1x3fwO7blPEBfucxjQSk47L9OMM85pRtxWQ1_wpy-bGYg9lmDTEjx-XLVpWr1zoYTLejVgcFpPESTgx_g4BtF1SaFCUkWRdVKxqbD9dgjVypyOszb7SYb7vkTAN4DgO9AomvMHz0pUAJ0u93YxvwyaOwxnFniauftnasm0EklT3y7jOoVJYK7NXoMmoWqymcdsEQuhBBRw6r6Y_DIK8fufOYNFB1fIK1u4JlxUO3SgHPCHJX1Z-7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت:
«بزرگ‌ترین بازنده در این ماجرا، حکومت ایرانه.
اونا سعی کردن با بستن تنگه هرمز، مسیر عبور و مرور رو تحت فشار قرار بدن؛ اما این کارشون جواب نداد.
بعد تلاش کردن با بالا بردن قیمت گازوئیل، فشار ایجاد کنن؛ اما این یکی هم دیگه جواب نمی‌ده.»
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/73116" target="_blank">📅 17:31 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73115">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d595a9a29.mp4?token=aQg01greQGQCT1fwPi_hAfa2N2oHJkChBhiB4Ort_VBGwqvdnMy95-cyCC0F8El9UtnFaUs4X4vrcOxxv1zm7uQFY5LK-boInxyfyAuLi4ep8i4pFUdTrpbtK8qyXO65i9Pdwc6zgc8zZcocxZMxI0pCGFZRF7ZbdKJZc7FqYglxslY6DV43cxIhf6TRRlah_sCpGa28XHb1w-KJq-vR5_YlbnJ-3q6w7nmOm-IN3c-nWQlZfWtN4_K2P9NdNjFJ8ogsvBY-rIEJ2C2nIeRAuqw8nQXU2qVBFBg8i2NchnL6F5Lw5c6XQS7nAh3YE0Ix1ujW2qOiHotkIVkc3ZNKVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d595a9a29.mp4?token=aQg01greQGQCT1fwPi_hAfa2N2oHJkChBhiB4Ort_VBGwqvdnMy95-cyCC0F8El9UtnFaUs4X4vrcOxxv1zm7uQFY5LK-boInxyfyAuLi4ep8i4pFUdTrpbtK8qyXO65i9Pdwc6zgc8zZcocxZMxI0pCGFZRF7ZbdKJZc7FqYglxslY6DV43cxIhf6TRRlah_sCpGa28XHb1w-KJq-vR5_YlbnJ-3q6w7nmOm-IN3c-nWQlZfWtN4_K2P9NdNjFJ8ogsvBY-rIEJ2C2nIeRAuqw8nQXU2qVBFBg8i2NchnL6F5Lw5c6XQS7nAh3YE0Ix1ujW2qOiHotkIVkc3ZNKVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت:
«کارگرها دیگه سر کار حاضر نمی‌شن.
ایران به بازار دلار دسترسی نداره، برای همین کاری که می‌کنه، چاپ کردن پول بیشتره.»
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/73115" target="_blank">📅 17:28 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73114">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cbe1e496c.mp4?token=PYA_ais5gtNGDHBOW54RrF-9w_ysZ74HCzcsgsrC3xJncpjcijobB_2oWoxsy7c9Vk9ziwTy_7EzSfv_7cZi7tz1uUk8z7kQDmx-esos8kkPMHLSA_VFXr-dtUb9zE6r4T1cjSpNyQ81-vJU2BI0ev8xepkZilqM94shWZFEbeJdQUnD1fqeA2WzscO6htvypG6achiH8FzMePtMOzUAUroAexsw74IMQhrWRmV2Lld9uX7U6xBR2GV6zRswMPNcQQ7uss95lgKqRRDopgBu2lN89OS8xdOJQRMEUxZquz0mJVKBHUa6XnPC9Oya3fxPy33tP68aWx1UvwklHLCgvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cbe1e496c.mp4?token=PYA_ais5gtNGDHBOW54RrF-9w_ysZ74HCzcsgsrC3xJncpjcijobB_2oWoxsy7c9Vk9ziwTy_7EzSfv_7cZi7tz1uUk8z7kQDmx-esos8kkPMHLSA_VFXr-dtUb9zE6r4T1cjSpNyQ81-vJU2BI0ev8xepkZilqM94shWZFEbeJdQUnD1fqeA2WzscO6htvypG6achiH8FzMePtMOzUAUroAexsw74IMQhrWRmV2Lld9uX7U6xBR2GV6zRswMPNcQQ7uss95lgKqRRDopgBu2lN89OS8xdOJQRMEUxZquz0mJVKBHUa6XnPC9Oya3fxPy33tP68aWx1UvwklHLCgvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت:
«ایران دیگه هیچ محموله نفتی‌ای در مسیر انتقال نداره. جریان نقدی‌شون منفی شده و ما راهشون رو بستیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/73114" target="_blank">📅 17:26 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73113">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aafe668bc.mp4?token=LFsm0i1vddM2-YFv8Qxj1qW6Kxb0zZakpxgpeeBxpQdemqoSpSp0pQurqQHxh3fLvc2TlPk5GINPAlnuQFz_sbB2vqNcq-bNYLmcQf5q8vRuDnxL0Tl8iYYVlWsP5yTFAH8oJrcU_bVvcN__E-p3py3BUViuPX15Len8FFbc53sQAvoE3NRGEvMCkaXw964MeCaI5eyncWy4WIb7AcMJqqJR-W7boZVtQJcqcjCCIEWdM9q76pwkQ6Xt7nJRayOOwUVE4-ScD8bF3_F-mB2lxKmeWlw_Hjpon1rKqAPmlmaOcKNxi6Igk0chLAUSBJEMk90Nnf7mFIWsCoYX8f6xUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aafe668bc.mp4?token=LFsm0i1vddM2-YFv8Qxj1qW6Kxb0zZakpxgpeeBxpQdemqoSpSp0pQurqQHxh3fLvc2TlPk5GINPAlnuQFz_sbB2vqNcq-bNYLmcQf5q8vRuDnxL0Tl8iYYVlWsP5yTFAH8oJrcU_bVvcN__E-p3py3BUViuPX15Len8FFbc53sQAvoE3NRGEvMCkaXw964MeCaI5eyncWy4WIb7AcMJqqJR-W7boZVtQJcqcjCCIEWdM9q76pwkQ6Xt7nJRayOOwUVE4-ScD8bF3_F-mB2lxKmeWlw_Hjpon1rKqAPmlmaOcKNxi6Igk0chLAUSBJEMk90Nnf7mFIWsCoYX8f6xUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛
اسکات بسنت، وزیر خزانه‌داری آمریکا، درباره ایران:
«همون‌طور که رئیس‌جمهور گفته، انتظار نداره درگیری نظامی تا قبل از انتخابات میان‌دوره‌ای اتفاق بیفته؛ دست‌کم نه تا بعد از اون.
نمی‌دونم معادل عبارت «تسلیم شدن و درخواست توقف» به فارسی چیه، اما ایرانی‌ها بالاخره به جایی می‌رسن که از آمریکا درخواست کنن دست از فشار برداره و تسلیم می‌شن.»
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/73113" target="_blank">📅 17:25 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73112">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1394e2d860.mp4?token=BtjzbG6vqbOgpoOj5xEeWXJLKqZOKsvm28uLHSvO0Pl_lK_KmXj5lKz3xTi1oGh8Rbl11NYpbV8KBrY8YKIYLKLZ_1aQJB0Xt2jYARTpF5wm_WgdfrbkhJZ5Vcp_6CLkEMci-VG5Ansl4xSkLCq6JvhM5yr1HfJfUXoASod_C8yPcKaVntkoNOwsDCjlRN3g00wtttPckosZOQQO0zDdJhodbaJWBCyvgxc8L7mPNXsaKnjtD3Sp-p6Hy_mq8nLeZ4xZGB1o4WJjTrl5LuiHAe4ArLsOMOjy0fRJ-TQX4xf_4CSd8UQPGDv7yJGT80YEV59ggzXMoVw6v3DY3zz51Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1394e2d860.mp4?token=BtjzbG6vqbOgpoOj5xEeWXJLKqZOKsvm28uLHSvO0Pl_lK_KmXj5lKz3xTi1oGh8Rbl11NYpbV8KBrY8YKIYLKLZ_1aQJB0Xt2jYARTpF5wm_WgdfrbkhJZ5Vcp_6CLkEMci-VG5Ansl4xSkLCq6JvhM5yr1HfJfUXoASod_C8yPcKaVntkoNOwsDCjlRN3g00wtttPckosZOQQO0zDdJhodbaJWBCyvgxc8L7mPNXsaKnjtD3Sp-p6Hy_mq8nLeZ4xZGB1o4WJjTrl5LuiHAe4ArLsOMOjy0fRJ-TQX4xf_4CSd8UQPGDv7yJGT80YEV59ggzXMoVw6v3DY3zz51Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش‌سوزی یک کشتی در مسیر جنوبی تنگهٔ هرمز بر اثر اصابت یک پرتابه:
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/73112" target="_blank">📅 16:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73111">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">صدای دو انفجار از طرف تنگه هرمز شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/73111" target="_blank">📅 16:08 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73110">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de2a7fa633.mp4?token=P4jTGY5SDRsiq4ZZ85OY-HDocgGnl2xn6IxcnBgQhLCTF4soLaZSlhtYFQRXGJw3hs5xf9MIzkMppFCmxnu0axaQIt3JJ4wPpcDKWseBamV8JqXw_VxSFWGaPYBNyRfWGdoXhRkefA_ELUK5fWDVAu7ZQXzvqIXjDW3EqiKOIN8S8IZFECCmT2zqMzEx5TzN9jzAQNJXK18CwRFeqt26r4JZWijTSu8_Ls8MeBJETGFQD-fS4xDETwYoTwWsC51Xcio-aJFKDJwCyw_06G7TEx6RstsAGiEDsSyyKpDv3oUXK2KZxqBMBsTB-UaaBAqZ6bkg4innyzvdVGR-ECxB6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de2a7fa633.mp4?token=P4jTGY5SDRsiq4ZZ85OY-HDocgGnl2xn6IxcnBgQhLCTF4soLaZSlhtYFQRXGJw3hs5xf9MIzkMppFCmxnu0axaQIt3JJ4wPpcDKWseBamV8JqXw_VxSFWGaPYBNyRfWGdoXhRkefA_ELUK5fWDVAu7ZQXzvqIXjDW3EqiKOIN8S8IZFECCmT2zqMzEx5TzN9jzAQNJXK18CwRFeqt26r4JZWijTSu8_Ls8MeBJETGFQD-fS4xDETwYoTwWsC51Xcio-aJFKDJwCyw_06G7TEx6RstsAGiEDsSyyKpDv3oUXK2KZxqBMBsTB-UaaBAqZ6bkg4innyzvdVGR-ECxB6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس سازمان مدیریت بحران کشور: احتمالاً در ۴ ماه پایانی سال کسری انرژی خواهیم داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/73110" target="_blank">📅 16:01 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73109">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4f3b1e9af.mp4?token=bEWblb9hdbsrJocGiSLkIDGUDf4Brps2c-_XDlqOKQ5SZHDGCUN2MMMgaPmrgoBX9sIKyBO_SJJYHPjXZlyh-YceT1O94i4bHht5zYVMDFkECNeVaK7MCkorsbB7ir9T5mOadrQmCihzlwDd8W8_Q5oPXZiA83_vs-5c3oUUu1Fx6sd-mOfZDWdaMVS3aVyIKwCZOawe9EJqNWqxPWdCQGO5T2YvzC6Y93WTHovThU5WWANh4WaOGzqFzV6BVikZgwGbaeg1IcrS6p2HkzxxZ7bPBuRZcwDlB_btVy1UIBToaiSMdjOY0RtOxeO2aa7wEYVxxCTgLExCGnLb8BH1ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4f3b1e9af.mp4?token=bEWblb9hdbsrJocGiSLkIDGUDf4Brps2c-_XDlqOKQ5SZHDGCUN2MMMgaPmrgoBX9sIKyBO_SJJYHPjXZlyh-YceT1O94i4bHht5zYVMDFkECNeVaK7MCkorsbB7ir9T5mOadrQmCihzlwDd8W8_Q5oPXZiA83_vs-5c3oUUu1Fx6sd-mOfZDWdaMVS3aVyIKwCZOawe9EJqNWqxPWdCQGO5T2YvzC6Y93WTHovThU5WWANh4WaOGzqFzV6BVikZgwGbaeg1IcrS6p2HkzxxZ7bPBuRZcwDlB_btVy1UIBToaiSMdjOY0RtOxeO2aa7wEYVxxCTgLExCGnLb8BH1ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یا بچه مچه با خودتون نبرید طلافروشی، یا اگه میبرید با طناب ببندینش به خودتون که همچین منظره‌ای خلق نکنه :
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/73109" target="_blank">📅 15:30 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73106">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d18ce038cc.mp4?token=NA37AlFpnwBgdY0fr-S8wq7-qOWDSqpx5QvAmLIqiXW3R33bCXPfb1QNcHN_kG05iNPlobCSI8Sm_1SOC97c2riiHj4wNW-X_NJfuNCey7d5rwKig94kzDaQyLxT9y0pIRIe-1lM6Q0u3fH0_IrRgyt4hFbeFgUirlCCiv5cGgzlnRGTc88-Hqa7jo0hWXqIEnYPUoXS1lP5jv90y_enfx1TBCWvjPHV_9OL5ybPHbntgAUS86p46YXXM3erVW5s3yDQgwUBGD-cwQ90aca4dmHURs7iaD_BIPcGFwjJbnMt0_hWZ5obe3HcO-24CqTouMmh81a01Ax-Bs_yWjjSKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d18ce038cc.mp4?token=NA37AlFpnwBgdY0fr-S8wq7-qOWDSqpx5QvAmLIqiXW3R33bCXPfb1QNcHN_kG05iNPlobCSI8Sm_1SOC97c2riiHj4wNW-X_NJfuNCey7d5rwKig94kzDaQyLxT9y0pIRIe-1lM6Q0u3fH0_IrRgyt4hFbeFgUirlCCiv5cGgzlnRGTc88-Hqa7jo0hWXqIEnYPUoXS1lP5jv90y_enfx1TBCWvjPHV_9OL5ybPHbntgAUS86p46YXXM3erVW5s3yDQgwUBGD-cwQ90aca4dmHURs7iaD_BIPcGFwjJbnMt0_hWZ5obe3HcO-24CqTouMmh81a01Ax-Bs_yWjjSKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت گرگان بعد از سیلاب ساعاتی پیش.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/73106" target="_blank">📅 15:03 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73105">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/35cfb05bea.mp4?token=OV8j1LNObGj5Lv-XWra6oqSfhwiQzMW1XHf6S4a0axjzVK7Xkrrd3mOt0a2F6USLyafCqAGhuMZv0QNxOH-fRKK9C48pEomE2yVDORR6uO4kxoTmgNM33rLLul70Rks0SMoCo1lOXPbO-bJooCTvuShPd3U0INs7oMjQOljZmM5sze72fyxC0x0OOEqz5dmtbgaBya4wjmq9kgz9-E_HAypldoXFyT0tyaEy2Zcj6GKQRg5TaLm6I6TDP9lsyvmGKUxVgUWy-3ZN_r4WMjeVU30VIwjVhuZgIBBlCP5vW9F9bTfdAo5gwaKz-sdN-MpHc1n11SH4Vmdfu3wP7paSDg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/35cfb05bea.mp4?token=OV8j1LNObGj5Lv-XWra6oqSfhwiQzMW1XHf6S4a0axjzVK7Xkrrd3mOt0a2F6USLyafCqAGhuMZv0QNxOH-fRKK9C48pEomE2yVDORR6uO4kxoTmgNM33rLLul70Rks0SMoCo1lOXPbO-bJooCTvuShPd3U0INs7oMjQOljZmM5sze72fyxC0x0OOEqz5dmtbgaBya4wjmq9kgz9-E_HAypldoXFyT0tyaEy2Zcj6GKQRg5TaLm6I6TDP9lsyvmGKUxVgUWy-3ZN_r4WMjeVU30VIwjVhuZgIBBlCP5vW9F9bTfdAo5gwaKz-sdN-MpHc1n11SH4Vmdfu3wP7paSDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جواد ظریف:
من به مسئولین گفتم، با برجامی که کونتون رو پاک میکنین، فردا باید دماغ‌تون پاک کنین!
ما کشورهای منطقه رو تهدید می‌بینیم، برای همین سفرای ما در منطقه جا بازرگان و دیپلمات، نماینده سپاه قدس هستن.
ما همه چیزو تهدید می بینیم، زن رو تهدید دیدیم، اینترنت رو تهدید دیدیم، کشورای منطقه رو تهدید دیدیم، ما حتی حجاب هم خاکریز می‌بینیم!
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/73105" target="_blank">📅 14:28 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73104">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ac45cb0ca.mp4?token=bC2D_xWNqdViYPodxB9eeW5obGQhAmd4T95dRtOXW68gIiAYYrrO0ZMHLgN7RqMgxmwy5kHvZtIo_OfERWH66toELEsm_diisCj19Zy2KDZLvR_SovqUsDE-0SQ8xODhNmE3wBlE16jATED-zQeDUZ6iVB3GfEb7ehRNjMSQ2e4Nlh1E9O5vkljDvQhNfZYvAH5l8ScI80rq1wVJqHEy3ExOWif-_UeljbZ5y_cAwVdjwoY2OH_yzgUYiMgMzNA1Y-zqG3pTm7P5pN0KCg6BxRcToKylpbpJ0wEAQPL2lLZ2MKrhsn0ZWrjzZCrSjk4M20QTuGMPqa-8xnPr97ylqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ac45cb0ca.mp4?token=bC2D_xWNqdViYPodxB9eeW5obGQhAmd4T95dRtOXW68gIiAYYrrO0ZMHLgN7RqMgxmwy5kHvZtIo_OfERWH66toELEsm_diisCj19Zy2KDZLvR_SovqUsDE-0SQ8xODhNmE3wBlE16jATED-zQeDUZ6iVB3GfEb7ehRNjMSQ2e4Nlh1E9O5vkljDvQhNfZYvAH5l8ScI80rq1wVJqHEy3ExOWif-_UeljbZ5y_cAwVdjwoY2OH_yzgUYiMgMzNA1Y-zqG3pTm7P5pN0KCg6BxRcToKylpbpJ0wEAQPL2lLZ2MKrhsn0ZWrjzZCrSjk4M20QTuGMPqa-8xnPr97ylqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری منتشر شده است که لحظه حمله حوثی‌ها به فرودگاه بین‌المللی ملک خالد در ریاض را نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/73104" target="_blank">📅 13:46 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73103">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BZw75WAcmSClKeP4qE6atOx-p445hWeN8r4x5ElOvEWXprbpRUldKIufCObpJh-s1g8ie-F-htQ_sqybVnNm5S16InXjlzJwn0riv251zKmw6FiMjSS9SerMr4hDfBrL8DWhlROjp6_cOohDv7Nfz_JejPEgl2xkPUD24U3jbBEHznsSa-YEMBtveXUbsEjEfd-juQg3Hj4Ym4nsRoUC1wlxj8OfmyIFaJMhKd6ZPTCm5mpNfh2RsEmiHwmrF2Vui5QK4J2gRCVSLXECl3sOyJHQf9UlyHFG16Po7xVi6XqEHC4oqErVZhFNzSQtkjfBOgSnXTF4Pf0DjKuMpFMs1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روز جهانی دختر، بر دختران سربلند و آزاده‌ی ایران‌زمین فرخنده باد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/73103" target="_blank">📅 12:59 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73102">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uiEkVWCyoJosWNVR_Hc3kqACpKt4yRpxTZ4Q1k5qLD3qguTNP-ySPumIzvwJHVh-1rh-5pyDYVA74pmlJZoowzatVVOSrCNocc0gRvHXRk2za7Z5IXbs0pgeFA3LtT96kOJaKpZb4NJKQRegd77bJXxRWUdrgX_C-QzoNlEJD_A2Efjn33Vh_ZHrsMzr-04B_we7E3lp8Stm1drCHo4xG7JQ_9JJZjjIhV7ByKg4ywBIMDGqyIJLUGJbRcmHXMQ4OCx-lYxzGQclQkOK6JrY3Dcsf3qe9cZQUnVvgIBpkbAKpURuyKuSxEMBHACv5XqMDvz59kPxqXABCMuLlT5ayA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تست موشکی از جنوب تهران
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/73102" target="_blank">📅 12:52 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73101">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47fbc83428.mp4?token=s2HJYle5Gj1rMuuckE4cCzf12Lz5vXhiTvYailyUMvKDaBLDFT-g0M43pEnlJ0QMgFDbiwx8MloMthyxJC6CF56SzTvU3VJ9e07QC4qRVJp62bQ5tDLzdVz2eSH0cVOE-NDIeknXaQ1cme4uURUoHXexIHALXcSGj1uMcMipy90-7jJGRUaZ429bCfAtu7ItpkT7nJM7_1xSJzjqO4L5EIWEMnMwXsMqhydpLPO2YSeMcSdc2GiNAoHw1h3jJ7H-aM2ZWqVinHvHrbwfRhE9OK0olU_1zha8K3a1EnQo7Sk9zraciPx-C53nzPby1EPPIwBv2YwRw_JaRmX4qT-4Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47fbc83428.mp4?token=s2HJYle5Gj1rMuuckE4cCzf12Lz5vXhiTvYailyUMvKDaBLDFT-g0M43pEnlJ0QMgFDbiwx8MloMthyxJC6CF56SzTvU3VJ9e07QC4qRVJp62bQ5tDLzdVz2eSH0cVOE-NDIeknXaQ1cme4uURUoHXexIHALXcSGj1uMcMipy90-7jJGRUaZ429bCfAtu7ItpkT7nJM7_1xSJzjqO4L5EIWEMnMwXsMqhydpLPO2YSeMcSdc2GiNAoHw1h3jJ7H-aM2ZWqVinHvHrbwfRhE9OK0olU_1zha8K3a1EnQo7Sk9zraciPx-C53nzPby1EPPIwBv2YwRw_JaRmX4qT-4Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام: یک کشتی باری در دریای عمان هدف حمله آمریکا قرار گرفت
فرماندهی مرکزی آمریکا (سنتکام) اعلام کرد در ۱۰ اکتبر، یک کشتی باری با پرچم پاناما به نام Ocean Molica که پیش‌تر از یکی از بنادر ایران حرکت کرده بود، پس از بی‌توجهی به هشدارهای مکرر و تلاش برای عبور از محاصره دریایی، هدف مهمات دقیق یک جنگنده آمریکایی قرار گرفت.
به گفته سنتکام، این حمله پیشرانه کشتی را از کار انداخت و خدمه آسیبی ندیدند. همچنین، طی سه ماه اجرای محاصره دریایی، ۴ کشتی از کار انداخته و ۱۳۵ کشتی دیگر وادار به تغییر مسیر شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/73101" target="_blank">📅 12:29 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73099">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6da19cc3d2.mp4?token=Ycqf_8e-sDDsL9ZcS4FaCd-wpATp447wf9coVhIqBESgT8iwPCijo7au2RDs8wLrFZQRC5ooF0L-EwPnjARORmCR9xLuJO8DCS1h7G0EGjIrW6pB7iUzY4Y7q2D4i_J2BDTWxZbNEsXmlPPl1LV19JoI3aCeNrawsuCRttuMWEjlG4F7pX682nA5ZogzaPV3ZmA-IQFW4uaBsjzVZkc7rMM4qFp_9QjGNeWjfx5ehrKRdwplqWgvdtsjUkcluwB0ydzxkWTovrU5aOpUVPmNQgFc1vgnqsE9cIBTItp9M3iMLFO8HKDvIEMX0saOYnrzkuljnLyQyh-JgmlM8Uc77Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6da19cc3d2.mp4?token=Ycqf_8e-sDDsL9ZcS4FaCd-wpATp447wf9coVhIqBESgT8iwPCijo7au2RDs8wLrFZQRC5ooF0L-EwPnjARORmCR9xLuJO8DCS1h7G0EGjIrW6pB7iUzY4Y7q2D4i_J2BDTWxZbNEsXmlPPl1LV19JoI3aCeNrawsuCRttuMWEjlG4F7pX682nA5ZogzaPV3ZmA-IQFW4uaBsjzVZkc7rMM4qFp_9QjGNeWjfx5ehrKRdwplqWgvdtsjUkcluwB0ydzxkWTovrU5aOpUVPmNQgFc1vgnqsE9cIBTItp9M3iMLFO8HKDvIEMX0saOYnrzkuljnLyQyh-JgmlM8Uc77Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جدی رفتن ویدیوی رپ هوش‌مصنوعیِ بی‌بی رو نشون خودش دادن، اونم به شوخی میگه از کجا میدونید شاید واقعی باشه:)
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/73099" target="_blank">📅 11:59 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73098">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">مقام‌های سعودی اعلام کردند در حمله روز شنبه به فرودگاه ملک خالد ریاض، ۱۲ نفر کشته و ۳۰۹ نفر زخمی شدند.
ملیت کشته‌شدگان:
عربستان سعودی: ۴ نفر
بنگلادش: ۲ نفر
آمریکا: ۱ نفر
مصر: ۱ نفر
اردن: ۱ نفر
سوریه: ۱ نفر
فلسطین: ۱ نفر
سودان: ۱ نفر
برخی مجروحان در وضعیت وخیم قرار دارند و حمله خساراتی به تأسیسات فرودگاه وارد کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/73098" target="_blank">📅 11:14 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73097">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f2ae9fdb8.mp4?token=BJ7yUBa4yaw2J8EgW3mH0nfNn9UcnH3olhWtUEonc6cwdNSis64CSd-MYrCE5cw7P01Xf0fIxmMnZioWAhb5E8G_GU_3SffgRFLA59mxnVsCWqPVEg4HBzHkDsIhAD_5noQpYKuy-SydroayRU2g6I2tTvcOgmrTr6_XOazf7f3iObGDxeVFORWl9atJjdljx4j9ZwmOI4WnIvB7FEv-k9stl_rtkCo5ZcTeW12K-96JLCNe4j_A0Moilx9FInEb-3lqBKo9H17nFgBGREV7y7vrZ1TLtDuxzT2G9IV_4vH_TVKJX3Q7DSWTAG-TPlzVO-Paua_WZmN3WaDRfxKaew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f2ae9fdb8.mp4?token=BJ7yUBa4yaw2J8EgW3mH0nfNn9UcnH3olhWtUEonc6cwdNSis64CSd-MYrCE5cw7P01Xf0fIxmMnZioWAhb5E8G_GU_3SffgRFLA59mxnVsCWqPVEg4HBzHkDsIhAD_5noQpYKuy-SydroayRU2g6I2tTvcOgmrTr6_XOazf7f3iObGDxeVFORWl9atJjdljx4j9ZwmOI4WnIvB7FEv-k9stl_rtkCo5ZcTeW12K-96JLCNe4j_A0Moilx9FInEb-3lqBKo9H17nFgBGREV7y7vrZ1TLtDuxzT2G9IV_4vH_TVKJX3Q7DSWTAG-TPlzVO-Paua_WZmN3WaDRfxKaew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: نظرتون درباره حمله حوثی‌ها به فرودگاه ریاض چیه؟
ترامپ: «به نظرم اتفاق وحشتناکیه.»
خبرنگار: آیا آمریکا هم وارد ماجرا می‌شه؟
ترامپ: «خب، خودتون متوجه خواهید شد. اما به نظرم اتفاق وحشتناکیه.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/73097" target="_blank">📅 10:54 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73096">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ترامپ درباره یمن:
«ما با حوثی‌ها در ارتباط هستیم و باید ببینیم چه اتفاقی می‌افته.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/73096" target="_blank">📅 10:46 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73095">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/174ee9d3ac.mp4?token=KWmkSbc2Q-oJFbwtzVS55L1TDeF2dFuS8_k3RxTWQc1vwPWyyMdFiZRr_NGLx3YW4IqVdxdyPdsFMcv868MMOupdNK1C4phZ1pfA4zNR_6JkRArgNkGcX0Q33dAYNNvLBj6Anht5X8amXYSzSi_3nxj3ehZR0pEsPjLG8lITIt5A9-zdfUzlvz-cctPzF3qYFyt57dAaAym4JgYkXhyPpqeupvE8rMVmw56Cm1TDEWO5DimvMy6Hb1_OIyWHavDPD990nur9t4sSWMSv2Q1mTVEnl7WudBPwMGibiYidcNIuDSlGRi3dqKhnEhHXBO78f35_KXri19wI4CE_YXYFGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/174ee9d3ac.mp4?token=KWmkSbc2Q-oJFbwtzVS55L1TDeF2dFuS8_k3RxTWQc1vwPWyyMdFiZRr_NGLx3YW4IqVdxdyPdsFMcv868MMOupdNK1C4phZ1pfA4zNR_6JkRArgNkGcX0Q33dAYNNvLBj6Anht5X8amXYSzSi_3nxj3ehZR0pEsPjLG8lITIt5A9-zdfUzlvz-cctPzF3qYFyt57dAaAym4JgYkXhyPpqeupvE8rMVmw56Cm1TDEWO5DimvMy6Hb1_OIyWHavDPD990nur9t4sSWMSv2Q1mTVEnl7WudBPwMGibiYidcNIuDSlGRi3dqKhnEhHXBO78f35_KXri19wI4CE_YXYFGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آیا سعودی‌ها بدون حضور نیروهای آمریکایی هم می‌تونن از خودشون دفاع کنن؟
ترامپ: «بله، توانایی دفاع از خودشون رو دارن. سعودی‌ها جنگجوهای خوبی هستن، اما به نظرم اون حمله اتفاق وحشتناکی بود.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/73095" target="_blank">📅 10:45 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73094">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/73094" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/73094" target="_blank">📅 10:45 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73093">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ur7r7e5tS2Ttkn2uY1isxA-XJgkhX8oxFdLAgnMDU5HG5J6jWb4AhuI5Un0K-U10vWRMYJkB4EnTQeGzPvNLt34ZAkVcJV3fWYdPXcCXCwXcnVko08xCmC8hTKg-TbRN6bBipsQsoEHdpCraS4jnyvnMPb60xN2VRN9koHblPG4eGaJd4C0hojwXEFe4P_BQW0QXcQDhrKZbGlREMEjrRrCKK4kzy6alUp8QxPKXWnpEXLYaPnuC0Bo6cWfZwylgbWpHr1dfMaCEHMLSAVTn3vCJ4053JRZAj9JDvLfTyjhcjNhnRv-zTRxkluaYDAgC20TBJEK03w_qPeCqRr6n-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
ناتینگهام‌فارست
🆚
کریستال‌پالاس
اورتون
🆚
هال
منچسترسیتی
🆚
لیورپول
اوساسونا
🆚
راسینگ سانتاندر
رم
🆚
کومو
مونزا
🆚
لاتزیو
میلان
🆚
ساسولو
فروزینونه
🆚
ناپولی
یوونتوس
🆚
کالیاری
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
https://TrexBet.com</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/73093" target="_blank">📅 10:45 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73092">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71e6800693.mp4?token=iAPWtAGmJ9Zi3U28QDc_2R01RiPpH-1oqyvYHHqnIBKHahZz4-7NVRmLOjFhjRXVgmYzYaYIWLmDkIeDUosQn3JF84gvpr2A3j20TLxJvSyJeknmPOvgX6GISyzgK1M0FZcGPRff3nD19ejHMn1ygKB_gb_CB6r9VxOk5WeQ9lewZZflnxu6LdF9wcD-3bO_vLg49bMFWuj2HYpZK2lSrEFPYiaVdJwXq_SaxERzNNSClV0JTmDWmcVrrO6IskCHXVex2EIS0g4TPLt1AB2RnvX118tZbfG5LlB1ru2MQvQZCYga9y7--tIPDEkdPzawpbOpt2hff3UV0-AfyS3T_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71e6800693.mp4?token=iAPWtAGmJ9Zi3U28QDc_2R01RiPpH-1oqyvYHHqnIBKHahZz4-7NVRmLOjFhjRXVgmYzYaYIWLmDkIeDUosQn3JF84gvpr2A3j20TLxJvSyJeknmPOvgX6GISyzgK1M0FZcGPRff3nD19ejHMn1ygKB_gb_CB6r9VxOk5WeQ9lewZZflnxu6LdF9wcD-3bO_vLg49bMFWuj2HYpZK2lSrEFPYiaVdJwXq_SaxERzNNSClV0JTmDWmcVrrO6IskCHXVex2EIS0g4TPLt1AB2RnvX118tZbfG5LlB1ru2MQvQZCYga9y7--tIPDEkdPzawpbOpt2hff3UV0-AfyS3T_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امام جمعه تهران:
توقع مردم، تجدید نظر در دکترین هسته‌ای ایران است
از ان پی تی خارج شویم به غرب می‌گویم هسته‌ای ما به شما ربطی ندارد؛
غلط کردین؛ برید گم شید!
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/73092" target="_blank">📅 10:04 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73091">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce6a5528a8.mp4?token=byglz_51bMBaFEmzmf8N4w1nLAfHIKmXaDZSdFa0X5X-eJE_Gc3WL0EO5sYTbQRpFT9dquiII-yhDtwmOWz2nVL35HoQWxL_Js8luzr4ZxedaD4Hu4UJv-httZ5F7XAF5eh1s9IIiXf8ifkiKteuH4lPMuZ5rcB_Jpw3cW7H6WHgKOU_bwiEEKrme-Xs99rI3ZQu7EMkCLUmxQwgEBKqybqRXzVDcGxsTfnX21ulAOPIt9eN3HBtg9vyqHm74rHJrSvpTTL59q6UbeiDlU5DCWQnUedygGgf5HOjOE8IRf75V5gVAY0P4XhtBok-gHXpIM9oGy-bYt29yeyNa1NjGIkrdJB5hX6gEXA7Wq_3QjfNQlaN5MJ6btzBcsqtNUVMiqvT6BR3sXBwYFJu4NO5eVxAEVWsbOtvGwI8woz-fVODdOH_e8iKCtMU6mxa0yoU48DIKXQB5ZTd10qyv7G0WM29Ek-KhnATbRtuBMNunqYoqWGDWwI4PSz2qUkW7vrcufAPp4IofOYc-nR1qkJhu6HbC5HhFGHyaN9zQ6Q70T1MrONcA0yCBeeacwJcXp3aZg_n7WjPUo_G0CBY_RGygayRVDJvTydkdodnFLalANSZNSoznxf5XG-K3J138ff4MCJi2BUF_ocuecMwTSjO9yDnMdE8f7bauNcL2n1RGDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce6a5528a8.mp4?token=byglz_51bMBaFEmzmf8N4w1nLAfHIKmXaDZSdFa0X5X-eJE_Gc3WL0EO5sYTbQRpFT9dquiII-yhDtwmOWz2nVL35HoQWxL_Js8luzr4ZxedaD4Hu4UJv-httZ5F7XAF5eh1s9IIiXf8ifkiKteuH4lPMuZ5rcB_Jpw3cW7H6WHgKOU_bwiEEKrme-Xs99rI3ZQu7EMkCLUmxQwgEBKqybqRXzVDcGxsTfnX21ulAOPIt9eN3HBtg9vyqHm74rHJrSvpTTL59q6UbeiDlU5DCWQnUedygGgf5HOjOE8IRf75V5gVAY0P4XhtBok-gHXpIM9oGy-bYt29yeyNa1NjGIkrdJB5hX6gEXA7Wq_3QjfNQlaN5MJ6btzBcsqtNUVMiqvT6BR3sXBwYFJu4NO5eVxAEVWsbOtvGwI8woz-fVODdOH_e8iKCtMU6mxa0yoU48DIKXQB5ZTd10qyv7G0WM29Ek-KhnATbRtuBMNunqYoqWGDWwI4PSz2qUkW7vrcufAPp4IofOYc-nR1qkJhu6HbC5HhFGHyaN9zQ6Q70T1MrONcA0yCBeeacwJcXp3aZg_n7WjPUo_G0CBY_RGygayRVDJvTydkdodnFLalANSZNSoznxf5XG-K3J138ff4MCJi2BUF_ocuecMwTSjO9yDnMdE8f7bauNcL2n1RGDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شبکه بریتانیایی ITN حدود ۴ ساعت از تصاویر وقایع سال ۱۹۸۹ میدان تیان‌آن‌من را منتشر کرده است؛ تصاویری که پیش‌تر محرمانه نگه داشته شده بودند و توسط تیمی ضبط شدند که موفق شد این نوارها را مخفیانه از چین خارج کند.
این مجموعه که حدود ۳۵ سال در آرشیو نگهداری می‌شد، شامل یک ویدئوی تدوین‌شده‌ی ۲ ساعته از سرکوب‌ها و همچنین ۹۰ دقیقه تصاویر خام و مخفیانه‌ای است که در روزهای پس از آن واقعه ضبط شده‌اند؛
تصاویری که کامیون‌های نظامی در خیابان‌های پکن، جمعیت مردم و پیامدهای آن رویداد را به نمایش می‌گذارند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/73091" target="_blank">📅 09:30 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73090">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e31f09431.mp4?token=MJsGR5Ts5oNTdVt1Reh7wTf0e8b9c7OvJE62C09fqejgjfcg5sUBCqObHUuasx5bw8_3mkJiy_3D99pq4Xj45dD0_uPqmK9yUsagbHYlq_J4h0YFyLWv7XM_yt1TvCGx5cATTi8vSfyg3Ib3BEptO09u60wO9F_Vcu2doLVcOJyVY9dXhKhCR3eyD6EmGrGJpQelHxNc5TqrQn-MY8kWH_B_sjVVbVYg1aFmZ3-zlWqhEAOXnB8tXmDaQ8sHQw1WvjThPMQLfwb820IedNYwS_6ploMGTcLrXO9XOarbL-wRdLOw_attfCss3eNlhIn51i9BA_xZKU04Ggc6qPiWfoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e31f09431.mp4?token=MJsGR5Ts5oNTdVt1Reh7wTf0e8b9c7OvJE62C09fqejgjfcg5sUBCqObHUuasx5bw8_3mkJiy_3D99pq4Xj45dD0_uPqmK9yUsagbHYlq_J4h0YFyLWv7XM_yt1TvCGx5cATTi8vSfyg3Ib3BEptO09u60wO9F_Vcu2doLVcOJyVY9dXhKhCR3eyD6EmGrGJpQelHxNc5TqrQn-MY8kWH_B_sjVVbVYg1aFmZ3-zlWqhEAOXnB8tXmDaQ8sHQw1WvjThPMQLfwb820IedNYwS_6ploMGTcLrXO9XOarbL-wRdLOw_attfCss3eNlhIn51i9BA_xZKU04Ggc6qPiWfoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میرسلیم:
فلسفه بازنشستگی در یک کشور اسلامی هیچ مفهومی ندارد و مسلمان واقعی باید تا آنجا که می‌تواند خدمت کند
حیف است که افراد ۸۰ و ۹۰ ساله را از خدمت کنار بگذاریم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/73090" target="_blank">📅 09:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73089">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/73089" target="_blank">📅 01:57 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73088">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/73088" target="_blank">📅 01:57 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73087">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1848b3d2ec.mp4?token=JhuHFnpWm7-VCGgqSo8BRZmE91SH45t-tElGJV8mqwU6CZ4aWPGApmMJygA6dvjs_oGmTwS5JkZm7qKJox2HsuwhqftrfYb7v64zlt3hDdzY5iEf2h0tULa9wbuaXgmZJuiK1v-Dfw_3ug6pDXDbd5eMtJC_2k3zt1Vs5-4UxKEIEIHpizLMBju_ncXfJ8jHUgqy4HU01fb_rXE1O8dAZyiM-KDnm28MmJZPU_PMQPqDGumY3kM0xiki_MFSbjgMo1O8ah6keRmKvAbK9bNCGH9h_higvPr-nHou-lC_usXk0PPlLWFKTOefV99yF_EW9P2Q_aoGUSikp_JIVJhkLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1848b3d2ec.mp4?token=JhuHFnpWm7-VCGgqSo8BRZmE91SH45t-tElGJV8mqwU6CZ4aWPGApmMJygA6dvjs_oGmTwS5JkZm7qKJox2HsuwhqftrfYb7v64zlt3hDdzY5iEf2h0tULa9wbuaXgmZJuiK1v-Dfw_3ug6pDXDbd5eMtJC_2k3zt1Vs5-4UxKEIEIHpizLMBju_ncXfJ8jHUgqy4HU01fb_rXE1O8dAZyiM-KDnm28MmJZPU_PMQPqDGumY3kM0xiki_MFSbjgMo1O8ah6keRmKvAbK9bNCGH9h_higvPr-nHou-lC_usXk0PPlLWFKTOefV99yF_EW9P2Q_aoGUSikp_JIVJhkLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
«ایران کشور بسیار شروریه؛ بزرگ‌ترین حامی تروریسم در جهانه.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/73087" target="_blank">📅 01:54 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73086">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6a4893ab6.mp4?token=v_2oeoPS5F0Hx4HxudJyNMe2hYYaIjwMvbMVEE00fsCdmrv0TVA4NhDtt8Uz52nJ6a56csVoQ_mZdQ_gvhVvcewGYFoEO8lkGL-LtAb1z4aP_r_GfZmiMgOmdMapdlNHSobYUWEfb7otI5cRXNUZXre3tL71A9sBZaniO9EotvLqIexKEYx2PXKbADeK5lrFk_DHYsH1qRGz8IxYHIT2ZEYQ5T7YSipfTAnQehz5pNmcWD-ejNvprTVo3DwRx2I-4jZcrwXH7dEkRywXUmltBaJ7PRZ7IQig2_00WBQ1CdVkAXjClM7JOlbKz_FYcc_hWgjKB8APPYckT-4fruikBoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6a4893ab6.mp4?token=v_2oeoPS5F0Hx4HxudJyNMe2hYYaIjwMvbMVEE00fsCdmrv0TVA4NhDtt8Uz52nJ6a56csVoQ_mZdQ_gvhVvcewGYFoEO8lkGL-LtAb1z4aP_r_GfZmiMgOmdMapdlNHSobYUWEfb7otI5cRXNUZXre3tL71A9sBZaniO9EotvLqIexKEYx2PXKbADeK5lrFk_DHYsH1qRGz8IxYHIT2ZEYQ5T7YSipfTAnQehz5pNmcWD-ejNvprTVo3DwRx2I-4jZcrwXH7dEkRywXUmltBaJ7PRZ7IQig2_00WBQ1CdVkAXjClM7JOlbKz_FYcc_hWgjKB8APPYckT-4fruikBoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«اون جوان‌هایی که در جنگ علیه ایران از دست دادیم، بیهوده جونشون رو از دست ندادن.
نمی‌شه اجازه داد یه آدم کاملاً دیوونه به سلاح هسته‌ای دست پیدا کنه.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/73086" target="_blank">📅 01:50 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73084">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/595730e6c3.mp4?token=N7svXmUTaglfOKomh0R0qP6Zzgj2JjwHXx21POJFyF3KHyfdryJ0w1KXw03eN1j7sug43PigDivSZCsh9oUyXCYOLLfU8iu6VbR7jIKz7OescKTZiWYEuY9ezTz5mKbN6pVTtFUnqUDXj7SF6yHx4u5U2oWUxaWxpJ1HnYNMpHbIaQzAC1XsWqrFsUn4fN91NnqCnZUNxwmMh6yQ1avKzHHZrptiQUwmXQ3SYZLXhbk-y00_ORQJK_HhwJjMMOkDqLz3lRzbF8n0WE3b3tqhhRf4g5hSLEV2_oIzf0K_wPc7P27GCGd39zE5-ekqMLaZ9nQ3suODiGBiDrofbjV-Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/595730e6c3.mp4?token=N7svXmUTaglfOKomh0R0qP6Zzgj2JjwHXx21POJFyF3KHyfdryJ0w1KXw03eN1j7sug43PigDivSZCsh9oUyXCYOLLfU8iu6VbR7jIKz7OescKTZiWYEuY9ezTz5mKbN6pVTtFUnqUDXj7SF6yHx4u5U2oWUxaWxpJ1HnYNMpHbIaQzAC1XsWqrFsUn4fN91NnqCnZUNxwmMh6yQ1avKzHHZrptiQUwmXQ3SYZLXhbk-y00_ORQJK_HhwJjMMOkDqLz3lRzbF8n0WE3b3tqhhRf4g5hSLEV2_oIzf0K_wPc7P27GCGd39zE5-ekqMLaZ9nQ3suODiGBiDrofbjV-Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دلقک بازی املاکی
😐
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/73084" target="_blank">📅 00:59 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73083">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b6424edb4.mp4?token=POkJfRdPrMnpZFtFK87wBhOy8tlMqEVsNVUttG3thuJJcB1aDyIuoLF6z7D-JWELynVyLetFux6BXnz1r9SJi7e90H-8MZRWqaIWmxPTxApB1hKgYMUWQCgyK-v73NtZX3RtztUCnu9nAQ0zsZJy6lcFZw_E8yj0Ewiwg6tYlQAcupxPqDNKVGJ45vV8BxZOCvWiXMLBab3ouhmOV5qQ36yGtcObbrKYMl2umqWuwGo2zYd4jZ2bbnmoTok5c7f60rngVsVtZnP7fbkTXr6zxTY9a_5c3EF4_A5uE3SvPFcFtxovdGAJfFCgkP7vn8SDVNHR6Mo41Zb7ID-JxYE9uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b6424edb4.mp4?token=POkJfRdPrMnpZFtFK87wBhOy8tlMqEVsNVUttG3thuJJcB1aDyIuoLF6z7D-JWELynVyLetFux6BXnz1r9SJi7e90H-8MZRWqaIWmxPTxApB1hKgYMUWQCgyK-v73NtZX3RtztUCnu9nAQ0zsZJy6lcFZw_E8yj0Ewiwg6tYlQAcupxPqDNKVGJ45vV8BxZOCvWiXMLBab3ouhmOV5qQ36yGtcObbrKYMl2umqWuwGo2zYd4jZ2bbnmoTok5c7f60rngVsVtZnP7fbkTXr6zxTY9a_5c3EF4_A5uE3SvPFcFtxovdGAJfFCgkP7vn8SDVNHR6Mo41Zb7ID-JxYE9uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارسالی یکی از اعضا از گرگان:
بارندگی شدید امشب در گرگان باعث وقوع سیل و وارد شدن خسارت به اموال مردم شده.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/73083" target="_blank">📅 00:48 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73082">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c88cca8dd.mp4?token=guayppDn1AHJTdIjApHkwccKlITXhjO-_zMg-_9mxYPzqJ9jABJ9lQ7QgPhI7EJKJG7oP1TwybClLd9r0srvHk_GYPIa9O1AiCQcmU3LYbYpxu2vymxGuYzsJkPAZruYY82F9blqK8Sb_MGKDnkUpAI197OR3nff2D222QP_AnPUXUZxotEXnW5XJXg4EWwsRZF5Kay7I2ZZTDYp3-bM3SluVQoZW6uOWVcrJ23RUxETPdRNxGxvdzEwn5obByFoZ-87nd7IE7aNGk1kJlWw15TS5iDuQbcIKXb-uOk-tkb1RFEBk9sf6pADCyxSSlgG3yz8merv5c6st8jUIQ_GqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c88cca8dd.mp4?token=guayppDn1AHJTdIjApHkwccKlITXhjO-_zMg-_9mxYPzqJ9jABJ9lQ7QgPhI7EJKJG7oP1TwybClLd9r0srvHk_GYPIa9O1AiCQcmU3LYbYpxu2vymxGuYzsJkPAZruYY82F9blqK8Sb_MGKDnkUpAI197OR3nff2D222QP_AnPUXUZxotEXnW5XJXg4EWwsRZF5Kay7I2ZZTDYp3-bM3SluVQoZW6uOWVcrJ23RUxETPdRNxGxvdzEwn5obByFoZ-87nd7IE7aNGk1kJlWw15TS5iDuQbcIKXb-uOk-tkb1RFEBk9sf6pADCyxSSlgG3yz8merv5c6st8jUIQ_GqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">املاکی درباره تنگه هرمز:
«داریم به این فکر می‌کنیم که اسم تنگه هرمز رو به تنگه ترامپ تغییر بدیم!»
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/73082" target="_blank">📅 00:25 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73081">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e93cc318ec.mp4?token=Ka1ijmcul9M_x2FGe6sQ6vb1ECz3w5_3u_SNmgOBp28PiU_GryNFFMgOirmCOKKsa_Chd9UDLuN7tT6h34wWmP8-rPVcF0yTwBbmnmlCoc9cXquEMTuWSJqpa8HoXbQGYHTjS-qMnkuu-c4NZ_tf_qlPJZEKWicnSz5GME76Qj77-ORH3GP5-B86BrqJs4u4_CvlKEt4BiUeJIodd-dZBsgnAqVnCyaofaKp6WNP9XLJiNCc1oo670ggh6hbbF3IoJ0B2JY27lbJpFr_kdLlv_-9z7vM_ewsYK5j_MmR0dHkCZ6d572AFyTtOgX0SNtGFjKV9ZRjlrSBOvYzWLmZog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e93cc318ec.mp4?token=Ka1ijmcul9M_x2FGe6sQ6vb1ECz3w5_3u_SNmgOBp28PiU_GryNFFMgOirmCOKKsa_Chd9UDLuN7tT6h34wWmP8-rPVcF0yTwBbmnmlCoc9cXquEMTuWSJqpa8HoXbQGYHTjS-qMnkuu-c4NZ_tf_qlPJZEKWicnSz5GME76Qj77-ORH3GP5-B86BrqJs4u4_CvlKEt4BiUeJIodd-dZBsgnAqVnCyaofaKp6WNP9XLJiNCc1oo670ggh6hbbF3IoJ0B2JY27lbJpFr_kdLlv_-9z7vM_ewsYK5j_MmR0dHkCZ6d572AFyTtOgX0SNtGFjKV9ZRjlrSBOvYzWLmZog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«می‌تونیم خیلی سریع به این ماجرا پایان بدیم. ایرانی‌ها نمی‌دونن که من تا حالا چقدر باهاشون مدارا کردم و چقدر باهاشون راه اومدم.»
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/73081" target="_blank">📅 00:25 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73080">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/988c9468b6.mp4?token=ZmXCEjBHNzzV22fHM1VTzIG-uBWOFbibD1jSipIzB3v2C51Uo1SshqlJun8ECyi9WvvDOJtsk5kKm36ObUuudCWPaFjYAlnyLvZhkz9sLXB_9ebijTo1HXMOkrvSNvDLBHg3X8dBe8PdLdC6rJBH-sn7PkHTmV93_HjgtesaOik13H-7xJWQa_eiCbddCP4o2MaJfAhGhtK73PjJtfnxztTOIFD3CmeG4pqGTn3QtL-scwQyc50EMWB2whbNq0-bnqpf1vJhX012HUnCyl35wtRaZScU_kAiLONS-PpKwfZqCM7NmUz8nhFt1BHJX28Qe6mVCvz9xur9B768m6mu_wkfC1K0Cu1XC_pZQFESk2LafSqGU-WiS2GGHdrptK_6sWTEE3GrFhAxohuGc8brDo6mULoUQ3E7UDAPUoZSgUs4BlJzy3Wzno66aafGLuGO0KGnkY7f4FREYGuO2TZoreZuMfApEcWI8bF3EaPM0TF-Ov5qEabNk-OfmeUShPPXtJ2TptUfPc1PJPYuiAnVsz-6ETv_0Ib0vcDlGrNnwht_dhUBTod43eOn4n5iMjSfvhL6JlWYVAqr2tnPixlVK6K_ijjYsRb7l7_AhcY0xXC4q7s_frJi4mcd34Og0dR1zRjIvI14rzS9bB4YNGQ18zp1JfqTfrxXmZwHMjR93vs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/988c9468b6.mp4?token=ZmXCEjBHNzzV22fHM1VTzIG-uBWOFbibD1jSipIzB3v2C51Uo1SshqlJun8ECyi9WvvDOJtsk5kKm36ObUuudCWPaFjYAlnyLvZhkz9sLXB_9ebijTo1HXMOkrvSNvDLBHg3X8dBe8PdLdC6rJBH-sn7PkHTmV93_HjgtesaOik13H-7xJWQa_eiCbddCP4o2MaJfAhGhtK73PjJtfnxztTOIFD3CmeG4pqGTn3QtL-scwQyc50EMWB2whbNq0-bnqpf1vJhX012HUnCyl35wtRaZScU_kAiLONS-PpKwfZqCM7NmUz8nhFt1BHJX28Qe6mVCvz9xur9B768m6mu_wkfC1K0Cu1XC_pZQFESk2LafSqGU-WiS2GGHdrptK_6sWTEE3GrFhAxohuGc8brDo6mULoUQ3E7UDAPUoZSgUs4BlJzy3Wzno66aafGLuGO0KGnkY7f4FREYGuO2TZoreZuMfApEcWI8bF3EaPM0TF-Ov5qEabNk-OfmeUShPPXtJ2TptUfPc1PJPYuiAnVsz-6ETv_0Ib0vcDlGrNnwht_dhUBTod43eOn4n5iMjSfvhL6JlWYVAqr2tnPixlVK6K_ijjYsRb7l7_AhcY0xXC4q7s_frJi4mcd34Og0dR1zRjIvI14rzS9bB4YNGQ18zp1JfqTfrxXmZwHMjR93vs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«ایرانی‌ها می‌گن: همه رو می‌کشیمممم! همه روووو!
همچنین می‌گن: الحمدلله! الحمدلله! الحمدلله!
منم بهشون می‌گم: بابا، شماها واقعاً دیوونه‌اید!»
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/73080" target="_blank">📅 00:24 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73079">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8279d9c497.mp4?token=JNVQIalVOPBEMuYHlutWkmdq2j6Hww0sSVmj5jl8Tn8vl3S2HbwJINwVy0QwY6lSUFdcsRlW1Ri2AOcBt0Ja14OQimBYmVWW4aJq77QbcsO3qv0FhTD6nKcvwo6N1LH6qMeoadoKnCBwcH1RC4XE1-qBZ6RVYcmpvB6uqjPu0HooZZokkl56XGqQT4yVIdBFg0xMwpJMO8X3Gv1VEZVjg2G1fhWy7L9GyOJbR9sq2Qr9Nf4k14VtIsSsVSqXM579999OaQslv8-DpmS_d0mtjQigleBXItXt9ZaRsgoSnHlzUSdU-KPbamZmOCSH7AVUPGYKRus81gGqqDSLCHoDxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8279d9c497.mp4?token=JNVQIalVOPBEMuYHlutWkmdq2j6Hww0sSVmj5jl8Tn8vl3S2HbwJINwVy0QwY6lSUFdcsRlW1Ri2AOcBt0Ja14OQimBYmVWW4aJq77QbcsO3qv0FhTD6nKcvwo6N1LH6qMeoadoKnCBwcH1RC4XE1-qBZ6RVYcmpvB6uqjPu0HooZZokkl56XGqQT4yVIdBFg0xMwpJMO8X3Gv1VEZVjg2G1fhWy7L9GyOJbR9sq2Qr9Nf4k14VtIsSsVSqXM579999OaQslv8-DpmS_d0mtjQigleBXItXt9ZaRsgoSnHlzUSdU-KPbamZmOCSH7AVUPGYKRus81gGqqDSLCHoDxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حضور گلشیفته فراهانی در فیلم Matchbox: The Movie 2026 و صحنه لب گرفتن او با جان‌سینا!
+ نکته جالب اینکه همسر جان‌سینا هم ایرانیه!
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/73079" target="_blank">📅 23:52 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73078">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be8b607f1d.mp4?token=i7jtvuu2Y7IJ-d3bPSKPA656Zpn8FPLDf2nkZSqVfQ5njpaaHFIQWqMcFA5zyv8dJH7G43AxUbDxJDpLfG7NjKAwV0ENccIMoP-ojNYxpsJSjovkEy7xPtJWHPd1Qx0tfmwyHDvRC1iV-ko4hVx9b8vgVbPISSNh6U9CGroGJxAT1keT54MEBbMss0MHd72FgGF5rsbeCWb0sRXOvIq37zJM9cToFex0TIKtu7A6Z_ZQN-yWWbh18p5uCYSvUuHHxTttU-NCR87ocmDSgdN2-Qmub75SXcriddurIQ0DkiPXKBFHHBfytv03kovU7Gr-2HEeCcDktUb0AOf-QLvQig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be8b607f1d.mp4?token=i7jtvuu2Y7IJ-d3bPSKPA656Zpn8FPLDf2nkZSqVfQ5njpaaHFIQWqMcFA5zyv8dJH7G43AxUbDxJDpLfG7NjKAwV0ENccIMoP-ojNYxpsJSjovkEy7xPtJWHPd1Qx0tfmwyHDvRC1iV-ko4hVx9b8vgVbPISSNh6U9CGroGJxAT1keT54MEBbMss0MHd72FgGF5rsbeCWb0sRXOvIq37zJM9cToFex0TIKtu7A6Z_ZQN-yWWbh18p5uCYSvUuHHxTttU-NCR87ocmDSgdN2-Qmub75SXcriddurIQ0DkiPXKBFHHBfytv03kovU7Gr-2HEeCcDktUb0AOf-QLvQig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک پلنگ حکومتی :هر روز صبح و شب اینجام که بگم ما فقط جنگ میخوایم  و مذاکره نمی کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/73078" target="_blank">📅 23:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73074">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52a72e1a5c.mp4?token=iBuvrzL0h97GPg1p1ebF0m9jOMwO54arlTvkn0uZU1KNDtECcWczVB4xE2vO0QX3BJZAnKT0nIXNCyBT_bu0hjIrrCEKLsRw30Sv2f6Q2-llmv1MrzLdFktky8UKGPhtzUSElLPlddkKChNwtM61yozW7-pLq2f8OIhvD053fyEDVbwsYpWnVada5GW3dOeV_VEoDYuCCKbrEqt7_zdCWKpsZdUZUuXUl6HjjmRpdyRbFyMb6IbehRcYOsSwX8fpnPQb1PKBX511iIv2YOFNtdfWqAZ1VqpqojZILBPr3uALL1AV27dGkFDeVG5j2PSTNKEQxJ2Rzxkp_dZjgTDUTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52a72e1a5c.mp4?token=iBuvrzL0h97GPg1p1ebF0m9jOMwO54arlTvkn0uZU1KNDtECcWczVB4xE2vO0QX3BJZAnKT0nIXNCyBT_bu0hjIrrCEKLsRw30Sv2f6Q2-llmv1MrzLdFktky8UKGPhtzUSElLPlddkKChNwtM61yozW7-pLq2f8OIhvD053fyEDVbwsYpWnVada5GW3dOeV_VEoDYuCCKbrEqt7_zdCWKpsZdUZUuXUl6HjjmRpdyRbFyMb6IbehRcYOsSwX8fpnPQb1PKBX511iIv2YOFNtdfWqAZ1VqpqojZILBPr3uALL1AV27dGkFDeVG5j2PSTNKEQxJ2Rzxkp_dZjgTDUTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله هوایی اسرائیل به ساختمانی چندطبقه در غزه
دقایقی پیش، جنگنده‌های اسرائیلی یک ساختمان چندطبقه در شهر غزه رو هدف قرار دادن. پیش از حمله، دستور تخلیه ساختمان صادر شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/73074" target="_blank">📅 22:34 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73073">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d6e7ebfe2.mp4?token=T6kBQ0iO1BYB8k_KxTZyR3NZIO0oU_Cu3tkshIHc2J-9hVv2SlydMW3IqGqKDuGdQy8XTCXUyFHzrZpIrQYOZDqTja13-LVfg1SDfNpBOVLrs1P5e24iR_-Mpww_q01zLwqCNDtJzJNvMpTnybeHs8JFBXK_pny3R5tVf-vFFvFx7OF0HXcoeZIrCnqE9qmV9hU0QNezHhSqeGLr_I4KgU3qkjkj114I6u9Tp4-6IdKaoAgt_qKniFB-PcDi4Vh1eq1TDIcfnd9ChT5f5yXyRv8-0jRTdD9lA2TL6HuuVm52DSVKPhFlimXScJbkV8mKaCaHgXqbJGQ8ysJzTR6Kww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d6e7ebfe2.mp4?token=T6kBQ0iO1BYB8k_KxTZyR3NZIO0oU_Cu3tkshIHc2J-9hVv2SlydMW3IqGqKDuGdQy8XTCXUyFHzrZpIrQYOZDqTja13-LVfg1SDfNpBOVLrs1P5e24iR_-Mpww_q01zLwqCNDtJzJNvMpTnybeHs8JFBXK_pny3R5tVf-vFFvFx7OF0HXcoeZIrCnqE9qmV9hU0QNezHhSqeGLr_I4KgU3qkjkj114I6u9Tp4-6IdKaoAgt_qKniFB-PcDi4Vh1eq1TDIcfnd9ChT5f5yXyRv8-0jRTdD9lA2TL6HuuVm52DSVKPhFlimXScJbkV8mKaCaHgXqbJGQ8ysJzTR6Kww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ضرغامی: پخش خطبه‌های نماز جمعه از اشتباهات من بود!
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/73073" target="_blank">📅 22:31 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73072">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/be565181a8.mp4?token=M4uE5SuFbeIUrMa8vEeUjLwLK8iWT7mnKuz8sbWXJkye-gcfi0zbKJWqcHjeNDtE2cvhFPzpA3nO2uvAfKC_1E5xKVDG-x35SiTPqtu6Mzwdlo3z5wwYbtVNvYsrV1Sfqfab72ZgWLxWXdUU79KxfM6Bj6doRwl1L2-WjwVoaDfYoRFGMUqV74HkHadWGgih7Vgltvib45GsYQqz5R9r8CPuN1WQJQvlV9v4vQUD0Lb65kJYMBudc58KIsyjOgq2ieU-a56orHyvDhukTUYGcpUwrmRZi3a8UO-3qX9XHb61FP_Sur1v3vWw3ElqHTebxY6yOeJ-YiTo8f59CtTVcA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/be565181a8.mp4?token=M4uE5SuFbeIUrMa8vEeUjLwLK8iWT7mnKuz8sbWXJkye-gcfi0zbKJWqcHjeNDtE2cvhFPzpA3nO2uvAfKC_1E5xKVDG-x35SiTPqtu6Mzwdlo3z5wwYbtVNvYsrV1Sfqfab72ZgWLxWXdUU79KxfM6Bj6doRwl1L2-WjwVoaDfYoRFGMUqV74HkHadWGgih7Vgltvib45GsYQqz5R9r8CPuN1WQJQvlV9v4vQUD0Lb65kJYMBudc58KIsyjOgq2ieU-a56orHyvDhukTUYGcpUwrmRZi3a8UO-3qX9XHb61FP_Sur1v3vWw3ElqHTebxY6yOeJ-YiTo8f59CtTVcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند وقت پیش مصاحبه یه دختر 25 ساله منتشر شد که ماشین 50-60 میلیاردی سوار بود!
بهش گفتن چطوری این ماشین رو خریدی؟ گفت تلاش و استمرار!
رفتن امارش رو درآوردن، دیدن باباش حسابرس شهرداری تهرانه و دختره آقازاده‌اس!
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/73072" target="_blank">📅 21:59 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73071">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/118178a3fa.mp4?token=RDueuN7yilvlBhfcPkIvRo7QrbRSLLO-p93NA0ShDSHHbBorN2TPGmh2v8iTAruN5G9-fjSVzqaQ3XKVkpk4rvKU826_UTwJrjvMayFFgdXQTMjGRovXMCUvFU2CO_3aMhWByDOhMm7C15-s_M806G2k8bfbjQO5T6t8AqoLT2Fv4UE8UQwHQUwcv-yQkzQsQewRhnOZDsXEy6If3032R9baVie0AS-EvOv4ST0AeX6TYWe0Eo7MCsnJJXPVNU27TaDXlgUDlwN2kD9Om9BrrJwVDULnL1pex-I-rgDeE_Rmp5331El0RIhvDDAtQZpGmiyiUbIuRWcaA4TIo_quqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/118178a3fa.mp4?token=RDueuN7yilvlBhfcPkIvRo7QrbRSLLO-p93NA0ShDSHHbBorN2TPGmh2v8iTAruN5G9-fjSVzqaQ3XKVkpk4rvKU826_UTwJrjvMayFFgdXQTMjGRovXMCUvFU2CO_3aMhWByDOhMm7C15-s_M806G2k8bfbjQO5T6t8AqoLT2Fv4UE8UQwHQUwcv-yQkzQsQewRhnOZDsXEy6If3032R9baVie0AS-EvOv4ST0AeX6TYWe0Eo7MCsnJJXPVNU27TaDXlgUDlwN2kD9Om9BrrJwVDULnL1pex-I-rgDeE_Rmp5331El0RIhvDDAtQZpGmiyiUbIuRWcaA4TIo_quqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: زلنسکی گفته توافق نفتی شما با پوتین نشونه ضعف شماست.   ترامپ: کی اینو گفته؟  خبرنگار: زلنسکی.  ترامپ: باشه!  @News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/73071" target="_blank">📅 21:06 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73070">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2bf843dd2a.mp4?token=UGT9h9E4hZCvoLqQSIJi12cXMt5CnQ7xmNOLVLXlOdta0XG4DhbVrzyoumXM91RWy0E7-usyfWJoeG_qxYCBcHS4E0cT2xcMSBdWs1YAUfRJ8yVPSppfqOdWFiwjr-S8g9nmvSq6q9p_ZlzcMywYBPTlPlG3hnO1jGBGyDSUkxjq88gGMg_HIGGiy1ycx56Vwbb2nnbhiKiujeDYCFHHpc-YVw5F0u9ALGCuwablF6jtS0Unwjh5N1J21hLug4y3d3ql7Nz0Vnds1-t6m2IbMned6h1-IvDcVUharCmyIctuw2UhWGaz9SdfOVqtV-kxuZVRhlPf_xxtusmBdeKtsw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2bf843dd2a.mp4?token=UGT9h9E4hZCvoLqQSIJi12cXMt5CnQ7xmNOLVLXlOdta0XG4DhbVrzyoumXM91RWy0E7-usyfWJoeG_qxYCBcHS4E0cT2xcMSBdWs1YAUfRJ8yVPSppfqOdWFiwjr-S8g9nmvSq6q9p_ZlzcMywYBPTlPlG3hnO1jGBGyDSUkxjq88gGMg_HIGGiy1ycx56Vwbb2nnbhiKiujeDYCFHHpc-YVw5F0u9ALGCuwablF6jtS0Unwjh5N1J21hLug4y3d3ql7Nz0Vnds1-t6m2IbMned6h1-IvDcVUharCmyIctuw2UhWGaz9SdfOVqtV-kxuZVRhlPf_xxtusmBdeKtsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سپاه تصاویری از آتش‌سوزی گسترده و نشت نفت از یک نفتکش منتشر کرده که به گفته این نیرو، بر اثر برخورد با مین دریایی در تنگه هرمز آسیب دیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/73070" target="_blank">📅 21:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73069">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3875ef3f4f.mp4?token=V6y-4LY43QjHo_LnA5JCdFV6mLw40kDr3cc8yJXJxjUBGmlwIjwS7F7BOTatckCjT_2V7JTVGd8Xn2gFR74Y2HjoT__UKYxbjsaRWGVzq6Bxk-oJPcHWd1iQn2OsY42OoHdvw74w14EUerSqSiIygEadZaDPAYTyYO1jAotVixWx9yeYM_a-YekYvnPTcEgs1MPjN1Tt_7Ozp7BflRKJrvbprj3hrgIaUGW2d_2xAv56AGBg9srci1Bi-dUOrgG4m4ASNq2pXRTHBQKyyPRV9KcDt0hgWNbtjsqAJt1co4FKJPogRPKTj2aolmZDEUUbI3KIXOFwrD9zof_v3rKJoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3875ef3f4f.mp4?token=V6y-4LY43QjHo_LnA5JCdFV6mLw40kDr3cc8yJXJxjUBGmlwIjwS7F7BOTatckCjT_2V7JTVGd8Xn2gFR74Y2HjoT__UKYxbjsaRWGVzq6Bxk-oJPcHWd1iQn2OsY42OoHdvw74w14EUerSqSiIygEadZaDPAYTyYO1jAotVixWx9yeYM_a-YekYvnPTcEgs1MPjN1Tt_7Ozp7BflRKJrvbprj3hrgIaUGW2d_2xAv56AGBg9srci1Bi-dUOrgG4m4ASNq2pXRTHBQKyyPRV9KcDt0hgWNbtjsqAJt1co4FKJPogRPKTj2aolmZDEUUbI3KIXOFwrD9zof_v3rKJoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: شما گفته بودید تا بعد از انتخابات میان‌دوره‌ای به ایران حمله نمی‌کنید. حمله اخیر در عربستان باعث شده نظرتون عوض بشه؟
ترامپ: «بررسیش می‌کنیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/73069" target="_blank">📅 20:58 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73068">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ba9c18ae3.mp4?token=gle0EyNfv_X8KVdy7fgPFOlfP_BcmqpRCGGtZ6nt9U4pFRRyApHJnQ1OYfLX07BnN78s-iXaFQufEIsYCFiX-xzg7CjbkKAmgf6Ny8TElrTMo8wiX53m3hq-3K_aR8kuiP5L7Agd6VIGRGTAnRnOthhmfN1cBmVFD10tkL7yl-d4WF8aMk_h35_G60X_xD7jmGBvsbjMRFLzj1OiM6hTB_NlBtFlUsyAcYMLmPrMoSksjPUhzCLXcTv0KeknRemTQ6B9fhO2fuU8Hmbe7yLUTtNZSw1mHk_zkNopLwEFrw5OmlL9FI0s6VoF8Pn79aEjH6NYPVM_1-MPvchZwk32og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ba9c18ae3.mp4?token=gle0EyNfv_X8KVdy7fgPFOlfP_BcmqpRCGGtZ6nt9U4pFRRyApHJnQ1OYfLX07BnN78s-iXaFQufEIsYCFiX-xzg7CjbkKAmgf6Ny8TElrTMo8wiX53m3hq-3K_aR8kuiP5L7Agd6VIGRGTAnRnOthhmfN1cBmVFD10tkL7yl-d4WF8aMk_h35_G60X_xD7jmGBvsbjMRFLzj1OiM6hTB_NlBtFlUsyAcYMLmPrMoSksjPUhzCLXcTv0KeknRemTQ6B9fhO2fuU8Hmbe7yLUTtNZSw1mHk_zkNopLwEFrw5OmlL9FI0s6VoF8Pn79aEjH6NYPVM_1-MPvchZwk32og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در ویدیویی جدید که در تیک‌تاک منتشر کرده، در حال ورزش کردن در باشگاه دیده می‌شه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/73068" target="_blank">📅 20:34 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73067">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f89266c981.mp4?token=KtFFZNSeu2ZNC-HRorWHqPeDOoG9ADzJpMHpV2x5w6_5TdGckjBOp9rskiXic0hWtOHiK_xuIYzmwzwu1jmuYbCI51QPboMWbHjEII9EeWBMwBd0VatrYHtAn2ZWtsVRJRTpXU0QffMOUMWd3TArz4Rm3VDNCC796zwD7Jde4fv0RFHYlP4aFewxVSVtO-gXm6dQyeAe3xqy1FJKNqkUdiAXCnXJMLpB7Qv1ZVUrxEJJsvQl8sBQfoZHIG8AdjimB59XstH0vDGbpQbMpTeQm4yJLyMdhwDbFgq7HZC25BDFtLbVzd6JoCzC6lhYzwesZPyNaGLPR_R42pDq3Acat4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f89266c981.mp4?token=KtFFZNSeu2ZNC-HRorWHqPeDOoG9ADzJpMHpV2x5w6_5TdGckjBOp9rskiXic0hWtOHiK_xuIYzmwzwu1jmuYbCI51QPboMWbHjEII9EeWBMwBd0VatrYHtAn2ZWtsVRJRTpXU0QffMOUMWd3TArz4Rm3VDNCC796zwD7Jde4fv0RFHYlP4aFewxVSVtO-gXm6dQyeAe3xqy1FJKNqkUdiAXCnXJMLpB7Qv1ZVUrxEJJsvQl8sBQfoZHIG8AdjimB59XstH0vDGbpQbMpTeQm4yJLyMdhwDbFgq7HZC25BDFtLbVzd6JoCzC6lhYzwesZPyNaGLPR_R42pDq3Acat4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رائفی‌پور: آمریکا را پایین کشیدن کاری ندارد.روسیه باید پالایشگاه‌های آمریکا را هدف بگیرد تا حملات اوکراین متوقف شود.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/73067" target="_blank">📅 20:02 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73066">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WLQqzguGtKdtrX7v7RRp9JtWRzhsiGJ0zrurM81vQWciuxAdqiGWbGp5_qGzxjQI7H-V4RBjIvqOVBY4W5qAp_Rav34TCCLxfggGiP4naxDMRVxja8BDVEmGUO1Rj1vS6rvnJyFyapdeELEKLEvn0D0Xdy_fmd8kLKwope7K0rLkVsy12TUQ7J9q0i6TNH_269Q92JU_2_7m__XyB_PY2dMVam7ckDOJTUC_GYW4DUQbXeGljbRVvCEjbOtYsPe7ztETPrevXTXI3eT4NqlGZkDew4IpMTEGeKax5_xAQEx2qHn1R-SK7Rjdlf99JPF-0q85PyfNYAgX3owvdzZECA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین محموله گازوئیل روسیه به مقصد آمریکا حرکت کرد؛ قبل از اعلام توافق ترامپ!
اولین محموله گازوئیل روسیه که راهی آمریکاست، ۲۲ سپتامبر از بندر سن‌پترزبورگ حرکت کرده؛ یعنی دو هفته قبل از اینکه ترامپ توافق رو اعلام کنه.
این نفتکش یونانی با نام MINERVA ZEN حدود ۲۷۵ هزار بشکه گازوئیل حمل می‌کنه و پیش‌بینی می‌شه ۱۱ یا ۱۲ اکتبر به سواحل شرقی آمریکا برسه.
تحلیلگران می‌گن حجم این محموله‌ها در مقایسه با مصرف گازوئیل و سایر سوخت‌های تقطیری آمریکا، فقط برای چند روز کافیه. از طرفی، حملات اوکراین به پالایشگاه‌های روسیه هم باعث کاهش تولید گازوئیل این کشور شده.
@News_Hut
| Clash Report</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/73066" target="_blank">📅 19:21 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73065">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3e4a880ec.mp4?token=RpqzHCEMoNwSiLWJ6dUVTv-ATzCPEhf1zm7Jyo6nGuer0Bx3ta-2LcrOW2uaZHMXfjEibPnQ-XLS_FNs4c86mP9OXGUCGeT4fddzVSuZGq2BOGUyId843GDRyv8pwlGJVgjqPhsGk_V5MmR315bFf01wjZWn0mbuR5dqefa_s-3x-qRKASoZUPwOvFX1zGqOTqPaDE5OVXLpyMoKKEfvA_Acfmx3_nFwPG9O2SAJT-OfWfkloKT8DqeD802j9gtw5R2kVOiFwWwhUK_8qSgThxQtOYja5z948DaE5URj8oLi0x3l4ynmQLh6T6JKQpd_8f91URBIuKgCWQcOepoWBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3e4a880ec.mp4?token=RpqzHCEMoNwSiLWJ6dUVTv-ATzCPEhf1zm7Jyo6nGuer0Bx3ta-2LcrOW2uaZHMXfjEibPnQ-XLS_FNs4c86mP9OXGUCGeT4fddzVSuZGq2BOGUyId843GDRyv8pwlGJVgjqPhsGk_V5MmR315bFf01wjZWn0mbuR5dqefa_s-3x-qRKASoZUPwOvFX1zGqOTqPaDE5OVXLpyMoKKEfvA_Acfmx3_nFwPG9O2SAJT-OfWfkloKT8DqeD802j9gtw5R2kVOiFwWwhUK_8qSgThxQtOYja5z948DaE5URj8oLi0x3l4ynmQLh6T6JKQpd_8f91URBIuKgCWQcOepoWBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در جریان اجرای ارکسترال «آرش» در سالن اسپیناس تهران، در شامگاه جمعه ۱۷ مهر، تماشاگران در واکنش به صحبت‌های اسماعیل بقایی، سخنگوی وزارت امور خارجه جمهوری اسلامی، او را هو کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/73065" target="_blank">📅 19:14 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73064">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">برآوردهای اولیه از تلفات حمله به فرودگاه ریاض:
بر اساس برآوردهای فعلی، در پی اصابت یک تا دو موشک بالستیک انصارالله به ترمینال ۳ فرودگاه بین‌المللی ملک خالد در ریاض:
مجروحان: حدود ۴۰ تا ۷۰ نفر
کشته‌شدگان: حدود ۳ تا ۵ نفر
این آمار در حد برآورد اولیه است و هنوز تأیید رسمی آن مشخص نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/73064" target="_blank">📅 18:26 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73062">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23f8abc61b.mp4?token=u_BVmU1V1aJzXIjMo3iJtXPmTsxOoWDOZjyf7z0UKyCY8mnjmx26MSltDiNBIfkC9Yzb9uh-enEzv7C_LNzJ349ppSgkcBOqDRhSBEI37WZUoJ1qEqBkIMycUjDrsNuzu5thKVZJj_lLNXsPgKZRDZ2bxfezhoU8lh1EWtqPN2FA7RQiZRJD2x2b0B--fYFQ5AyfiH1h0IIL9nNxFvquOWQ99fdpR3i3_wVWLIpBlIkSMTZhsWrn7ttEAcIN4l-SdwVuaoOQ-yE_S3COGcsU7_xuRnVad_ZznyI2fQcGY-yTRRU6yXiI-zlNBt7fa1lX95RC-rv2d67Rewfmj6YUDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23f8abc61b.mp4?token=u_BVmU1V1aJzXIjMo3iJtXPmTsxOoWDOZjyf7z0UKyCY8mnjmx26MSltDiNBIfkC9Yzb9uh-enEzv7C_LNzJ349ppSgkcBOqDRhSBEI37WZUoJ1qEqBkIMycUjDrsNuzu5thKVZJj_lLNXsPgKZRDZ2bxfezhoU8lh1EWtqPN2FA7RQiZRJD2x2b0B--fYFQ5AyfiH1h0IIL9nNxFvquOWQ99fdpR3i3_wVWLIpBlIkSMTZhsWrn7ttEAcIN4l-SdwVuaoOQ-yE_S3COGcsU7_xuRnVad_ZznyI2fQcGY-yTRRU6yXiI-zlNBt7fa1lX95RC-rv2d67Rewfmj6YUDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از فرودگاه بین‌المللی ملک خالد در ریاض پس از حمله منتسب به حوثی‌ها (انصارالله)
در این تصاویر، آثار خون روی زمین دیده می‌شه و نیروهای امدادی گسترده‌ای در محل حضور دارن.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/73062" target="_blank">📅 18:21 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73061">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">گزارش‌ها از وقوع حادثه‌ای بزرگ در فرودگاه ریاض؛
گزارش‌ها حاکی از وقوع حادثه‌ای جدی در فرودگاه بین‌المللی ملک خالد در ریاضه. احتمال داده می‌شه یک موشک بالستیک حوثی‌ها (انصارالله) به این فرودگاه اصابت کرده باشه.
تعداد زیادی از نیروهای امدادی و اورژانسی به محل حادثه اعزام شدن.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/73061" target="_blank">📅 18:18 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73060">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">#فوری
؛ خبرگزاری فرانسه (AFP):
خبرگزاری فرانسه به نقل از سه شاهد عینی گزارش داده که در حال تخلیه افراد از فرودگاه بین‌المللی ملک خالد در ریاض، پایتخت عربستان سعودی، هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/73060" target="_blank">📅 18:16 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73059">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dc0bb8954.mp4?token=Ef_vdZM32WLV3F0anItSsSyYndkoki0LpdsjJVLDxG9qFpsdNJjiOQ_y_jXcNBYTBihW3m3fCD315UXcbIp2_s672C8zZTUSHFzNOCKVa4A-3Vc78HQwjlV-OiMj1dz3mqXZwBrzMf7iZtB9KEd6qUVkFx6FEpTiOdiD6B98bP_94KXqckuBvHe3hrFA5ulUmbBlNt5BpyMQkgWFrgg3SPcHFaDmTV-HLADQ5cJDpd4LFX-xMRWB6RTkBtZTZ7wPbU7gomQkzcMY3wtmxs8Wij5INfD1IgFzPlFO16chT7jBZxl0upMt2spQJgU3ZX2xM4tY6AwgHCKAwqH3U8TJSpxZXP6b3AyvAlLK3XI1Irdu_fEqkThEuLhuixfQPGfdLWclIhCr3uXe6HJscnxT1mVZ9rWcbD7gGChRIuZirwoxSXotb38tab3Nxjk1xE8Djd2-cKXMxx2tsMd8nx_6F2Emv_20qrhEp2x3skV91OrgZHiqO70yNmt8oa6K_CQurNOtpMxqgC3FbU7hJsQWs2LV0LleOHXgg6b1u7nO-nhpzOwL-0fsFiTTfIiVcZsdjRd2gy_5uELRDMEvZOMwcsWQlgFc_xVwh8dJDUBpWwXG92aZ948lspae2ZLWxHj_ONBfzEy8O7W-S6zB-AkhuO1Vp64nlHdBb-L9EHJY0CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dc0bb8954.mp4?token=Ef_vdZM32WLV3F0anItSsSyYndkoki0LpdsjJVLDxG9qFpsdNJjiOQ_y_jXcNBYTBihW3m3fCD315UXcbIp2_s672C8zZTUSHFzNOCKVa4A-3Vc78HQwjlV-OiMj1dz3mqXZwBrzMf7iZtB9KEd6qUVkFx6FEpTiOdiD6B98bP_94KXqckuBvHe3hrFA5ulUmbBlNt5BpyMQkgWFrgg3SPcHFaDmTV-HLADQ5cJDpd4LFX-xMRWB6RTkBtZTZ7wPbU7gomQkzcMY3wtmxs8Wij5INfD1IgFzPlFO16chT7jBZxl0upMt2spQJgU3ZX2xM4tY6AwgHCKAwqH3U8TJSpxZXP6b3AyvAlLK3XI1Irdu_fEqkThEuLhuixfQPGfdLWclIhCr3uXe6HJscnxT1mVZ9rWcbD7gGChRIuZirwoxSXotb38tab3Nxjk1xE8Djd2-cKXMxx2tsMd8nx_6F2Emv_20qrhEp2x3skV91OrgZHiqO70yNmt8oa6K_CQurNOtpMxqgC3FbU7hJsQWs2LV0LleOHXgg6b1u7nO-nhpzOwL-0fsFiTTfIiVcZsdjRd2gy_5uELRDMEvZOMwcsWQlgFc_xVwh8dJDUBpWwXG92aZ948lspae2ZLWxHj_ONBfzEy8O7W-S6zB-AkhuO1Vp64nlHdBb-L9EHJY0CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ملکه تایلند برای نخستین بار به تنهایی هدایت یک جنگنده گریپن سوئدی رو بر عهده گرفت و پس از فرود موفق، از پادشاه مدال دریافت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/73059" target="_blank">📅 18:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73058">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/73058" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/73058" target="_blank">📅 18:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73057">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z2Pdm0btVusoRNVrb3p9l_zVNEGjBWmOzHMnIfqEO4uzmw18SxfZbJ06yyARKU83CmhhtTWNXp2dzYZYkPEz1Es8IG6qQMQmouNAVnj1nBi5d3kBrGv48AgQYfxPkdNcuWz0tjH-PefBlSccj4SV4ilFN9M3lrT700B0VIv-nNXiAaVBRzP7m1EJyx7Md_pQOuXnYRdz55y4YKt5FHHBw0VL21-fsL7blc7p6dWmeVGd98qIcKOnUsdCOhagSvxHgIv-GkFKxTxGDEQnXBC2bxrxcPlRywTXbnm_IZnjadLdB5NEwTXATNBMyy4FbW3sJ3-cCI_pAC6DjPrL1KPFHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان انگیز ویارئال
🆚
رئال مادرید رو در
TrexBet
از دست نده!
📉
نگاهی به آمار ۲ تیم در ۵ رویارویی اخیر:
ویارئال: ۲ برد، ۳ شکست و ۱۱ گل زده
رئال مادرید: ۳ برد، ۲ شکست و ۱۰ گل زده
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
https://TrexBet.com</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/73057" target="_blank">📅 18:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73056">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c52e5fb32c.mp4?token=Q6HeNdRA-H_-NOwIJxjyfI6qiiRshSs8hDsmRfzoND10Yy5KN1JkrLRFDDtTqxbhqwf6ZENadR5xgCQT3zOnZtvImRaTRy1lBXEfpYQPsIj9bMHht5BfdP-djqtyWaNwTQLyPA__Xsb9sQunFhL6U1M3aWFTeAAq6abIACM2237YPw7rZSmNDouBAPWnZINa9bDM4ZVCjyxMf8LiDBsqJIG2mO0ve0qBuZyjjiBxDsTFGJoaGq_J0CCwWINC_7Nzr_KOTptPL1bJ-vEv-fLlwcRjfdkRgzwSTzf1lekt9QXoP5clNW-GWZAFt0uo8upGNxAqmkGLxoIAnvbzuEQSg6Oi6E7xMWwglzegds-2KZ311eFz40xSF0IaePDbEHoAgDeYna0q4DUuj3yADKtw_r01tsgbCE0hTg9WEwvmO41cuPkc51yUDrTgl0ieDS5lYqV7TS_ysivHD5lZPMUnu_diZcEpQlRsABXUelMSLXGJN3kbbJvKXKstDyNZ6rr3hhnWE9pKsspGMZHO1tEy1eX9Fnx8qFjCth_ixe_u8ReEJvUQ18Q7ywuNup23Rr5xol4EnKABT_kZkkqZ-4jVt9PAIdoUmZTfH6PNK4P3vAOLiKnS2aNbSe36Fgkt0hSI6juKhSa0BEKk6t_ZO-pRLAXrOlrj2XkDTZDeT7bkUFo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c52e5fb32c.mp4?token=Q6HeNdRA-H_-NOwIJxjyfI6qiiRshSs8hDsmRfzoND10Yy5KN1JkrLRFDDtTqxbhqwf6ZENadR5xgCQT3zOnZtvImRaTRy1lBXEfpYQPsIj9bMHht5BfdP-djqtyWaNwTQLyPA__Xsb9sQunFhL6U1M3aWFTeAAq6abIACM2237YPw7rZSmNDouBAPWnZINa9bDM4ZVCjyxMf8LiDBsqJIG2mO0ve0qBuZyjjiBxDsTFGJoaGq_J0CCwWINC_7Nzr_KOTptPL1bJ-vEv-fLlwcRjfdkRgzwSTzf1lekt9QXoP5clNW-GWZAFt0uo8upGNxAqmkGLxoIAnvbzuEQSg6Oi6E7xMWwglzegds-2KZ311eFz40xSF0IaePDbEHoAgDeYna0q4DUuj3yADKtw_r01tsgbCE0hTg9WEwvmO41cuPkc51yUDrTgl0ieDS5lYqV7TS_ysivHD5lZPMUnu_diZcEpQlRsABXUelMSLXGJN3kbbJvKXKstDyNZ6rr3hhnWE9pKsspGMZHO1tEy1eX9Fnx8qFjCth_ixe_u8ReEJvUQ18Q7ywuNup23Rr5xol4EnKABT_kZkkqZ-4jVt9PAIdoUmZTfH6PNK4P3vAOLiKnS2aNbSe36Fgkt0hSI6juKhSa0BEKk6t_ZO-pRLAXrOlrj2XkDTZDeT7bkUFo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این دختر خانوم با این پسره تو رابطه اس و که علاوه بره پسره، سگ دوست پسرش هم عاشق دوست دختر پسره شده.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/73056" target="_blank">📅 17:34 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73055">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/502e54151d.mp4?token=CGCawSAW37ELq02xUrclvxFzBiHfUkzdlYOz-1SaN7j4onq7I0LAFZBqF9KgHudjvy8KXSML6lKmjnK--KdRklcHGDDsI4SxW-hcNn4-oP5EivXltiLEyOVeWHLt-TJAmWK94CvaWPcvagInqtIGLEJiITofbh9scpy7ukNn2CBuwY-ZtrD1STX1J8AjKxuZwmERY3mmYBa1BZGP7YPgK4SfmA1VtSj9fZTBX8BymRUWYQGJogx-J25isc_d4DnXzJVaz9dSPMeiCllMBj9au8qh-1XlwNELeqGjusux_CIg0gHtOp9U10YlikQeMUm-LsbLD3MYzr88CUA1DmVSEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/502e54151d.mp4?token=CGCawSAW37ELq02xUrclvxFzBiHfUkzdlYOz-1SaN7j4onq7I0LAFZBqF9KgHudjvy8KXSML6lKmjnK--KdRklcHGDDsI4SxW-hcNn4-oP5EivXltiLEyOVeWHLt-TJAmWK94CvaWPcvagInqtIGLEJiITofbh9scpy7ukNn2CBuwY-ZtrD1STX1J8AjKxuZwmERY3mmYBa1BZGP7YPgK4SfmA1VtSj9fZTBX8BymRUWYQGJogx-J25isc_d4DnXzJVaz9dSPMeiCllMBj9au8qh-1XlwNELeqGjusux_CIg0gHtOp9U10YlikQeMUm-LsbLD3MYzr88CUA1DmVSEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از بمباران پادگان سپاه در خرم‌آباد، استان لرستان، در جریان جنگ ۴۰روزه:
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/73055" target="_blank">📅 17:02 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73054">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ze0B8t4Xij505FeBWt6UxKa4fTj3_S7uGbxlNF1XHuWHzNM4fNNibcFg6CefXWIYqeEiEewvPJ331VB34Eyz7cLGVe-VeE8KTWcTsf7npcSTvv_k6004FjQ8GW6vuvN_RryjEbT_ghyyjxjaXBRl2EnMu_YFwcpxjvNKND3j_yoPA9Jf6paVF8cBqUsfA5IP-A5n2oxlM2RTGxd6alPtHIYmlFOmO9sesPU6WK9zoV3W2a2feJQsk0Quw5QpclFs2YrQEvQOPQD3ffXMNnXBqRTLfgVEWOO4DDiSDuJge_r6FRj17DlVc3Kv8v_uUh6jiIvF66oYq76rATrDdz8xIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛
معاریو: آمریکا از اسرائیل خواسته به‌تنهایی به ایران حمله کنه!
طبق این گزارش، واشنگتن توی مذاکرات دو هفته اخیر از اسرائیل خواسته بود بدون مشارکت مستقیم آمریکا، حمله نظامی به ایران رو انجام بده.
هدف آمریکا این بوده که پیش از انتخابات میان‌دوره‌ای نوامبر، هزینه سیاسی حمله به ایران متوجه ترامپ نشه؛ درحالی‌که چنین حمله‌ای می‌تونست از نظر سیاسی به نفع نتانیاهو، پیش از انتخابات اسرائیل در ۲۷ اکتبر، تموم بشه.
ایال زامیر، رئیس ستاد ارتش اسرائیل، هشدار داده بود که ازسرگیری جنگ می‌تونه باعث تعویق انتخابات اسرائیل بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/73054" target="_blank">📅 16:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73053">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fca26fcca.mp4?token=AAFzJfxisOgCp1kt_6MERU3kFe5iXsVJcNzZ_CaZEkmowg2nKgeyjFLLgtOkDP1tRz8jogchQ4HD9kwJ1h3mmDRy_c1aaZFoJM_UVEi0LoeAsHSXNJrHIR5Fcs8USETRaWDzPyM2qWEuNlAnBCMAby77qwZ1lYftBniulfC_z8xrvGVVEXoiRs0oyOW7VqDTwFzr70Ydw9XCypowczNZ1KivU3gbRMuHPGrHkTGD80JOGxDIQANmO6e5XQugbODLln5jlX9dWosoyl6dUZB7ofJ-7rf9vr8IJmNICShs9Ali1JQ3ryJvqLKhKB9VoZGu2hJjk0yMzh6ZIeLCrVabDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fca26fcca.mp4?token=AAFzJfxisOgCp1kt_6MERU3kFe5iXsVJcNzZ_CaZEkmowg2nKgeyjFLLgtOkDP1tRz8jogchQ4HD9kwJ1h3mmDRy_c1aaZFoJM_UVEi0LoeAsHSXNJrHIR5Fcs8USETRaWDzPyM2qWEuNlAnBCMAby77qwZ1lYftBniulfC_z8xrvGVVEXoiRs0oyOW7VqDTwFzr70Ydw9XCypowczNZ1KivU3gbRMuHPGrHkTGD80JOGxDIQANmO6e5XQugbODLln5jlX9dWosoyl6dUZB7ofJ-7rf9vr8IJmNICShs9Ali1JQ3ryJvqLKhKB9VoZGu2hJjk0yMzh6ZIeLCrVabDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظاتی ترسناک و باورنکردنی که امواج عظیم زیر رعد و برق یک کشتی باری غول‌پیکر را ناچیز نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/73053" target="_blank">📅 16:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73052">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YWhpBqwE-hItW1x50K6PxoaZuOJK6FsKgE_UL5tYU7qTNduTOzrH2I4gzJfMX19wD4nP3_N37bfX3dSElDJWtpoo0P8u2SnysM1cunMbUgmvJewdk4W6HFwEFPVWMCwS8LNxPwd6RqAzUq6UJD0phPb7ccxj83y7CnpcIqsjlxoeJXRvtXMHpVCQyK9ZPeeaAzBTkOxipCUUuiYakBghhkfwhUHv0du5ZA-PvZTQfZRUSoBBVf9trCb9F3zQrnJhtIuvCdlY2vSKvR6yH0olISQ_KbAKbCC34-fXgGRaT3dykkrIZ1Bdz5kvEHvbBi5WsZbi2hxjEj8Sx5mMWAswIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:«من به ۸ جنگ پایان دادم و به پایان دادن یا حل‌وفصل ۲ جنگ دیگه هم نزدیکم.
همه گروگان‌های اسرائیلی، از جمله ۲۸ نفر آخر رو، چه زنده و چه کشته‌شده، برگردوندم.
صدها گروگان از کشورهای مختلف جهان رو آزاد کردم و به خونه‌هاشون برگردوندم.
در ونزوئلا در جنگ پیروز شدم و دیکتاتور خشنی رو که با بی‌رحمی اون کشور رو اداره می‌کرد، دستگیر کردم.
همچنین جلوی جمهوری اسلامی ایران، بزرگ‌ترین حامی دولتی تروریسم در جهان، رو گرفتم تا به سلاح هسته‌ای دست پیدا نکنه؛ و خیلی کارهای دیگه!
با وجود همه این کارها، نه من و نه ایالات متحده آمریکا جایزه صلح نوبل رو نگرفتیم. عجب!»
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/73052" target="_blank">📅 15:43 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73051">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f583eac4a.mp4?token=nn7XY0dGrCkGYE_efjwrO50jMfhCPRDlol4vTwHhZPxS6mnKRFp_Gd5J_SRdMJn2JEHo5IefQe795T9PGhiNp5dcMTDzkMQfCDfRx8n3UUWc0t-mW3TGW_aTqijxSUMBNDQGOSIZUylW6HxUP8jwxmTMczQ9sXjM6DZ8s-S4AqgLBBls63CIbYtka-NYxy1-kTR7zCgRPcoIyTpnxMy7oAnizgfyP288Sxu-Kjq56nCW3BqQRqVKlhAzWqG3DcT7m-Q9v8jMu-MX15pnH3VtZs_fOJ5du-itgmsye65Y6vsxuwCtlZ7rS1uQcg5pKYPv2lRaBAr8stDWvkFK9jtCvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f583eac4a.mp4?token=nn7XY0dGrCkGYE_efjwrO50jMfhCPRDlol4vTwHhZPxS6mnKRFp_Gd5J_SRdMJn2JEHo5IefQe795T9PGhiNp5dcMTDzkMQfCDfRx8n3UUWc0t-mW3TGW_aTqijxSUMBNDQGOSIZUylW6HxUP8jwxmTMczQ9sXjM6DZ8s-S4AqgLBBls63CIbYtka-NYxy1-kTR7zCgRPcoIyTpnxMy7oAnizgfyP288Sxu-Kjq56nCW3BqQRqVKlhAzWqG3DcT7m-Q9v8jMu-MX15pnH3VtZs_fOJ5du-itgmsye65Y6vsxuwCtlZ7rS1uQcg5pKYPv2lRaBAr8stDWvkFK9jtCvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شهرداری خرمشهر دیده یه سرسره تو پارک شکسته، با خودشون گفتن چکارکنیم چکارنکنیم؟؟
که این نیمه شاهکار رو پیاده کردن :
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/73051" target="_blank">📅 15:32 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73050">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76ef585e24.mp4?token=JqtWh_Lqn4ET50WRnNIgBodP8FWXJ8lb5LX6n7laD3TI2-GXB0dgxxupoFju6PfUMPpa-uakMwL9IVO7zf1IskaRlTzJeXl6PVQOqwuntDZzO_7SfoMr9AgZ8r5Wn50QAUbnquopahmuYnR5QCJJqaznwgxiLejieQd42WjPnYcSpXrnqaB0TJKAgXD1rfsKpvrs-bZ9FAirPp4p645JaMOkiJthMHL8AnpsFjOdlYJDzdWuJdqQb1Pm5w9lnIhPXGxo3l2vZVqXSqIg2NYgxv5oJLsbbVneAn24jgfDJqpT5d0S4GUQOgBbOIzapfWC8jN7ao6A0VJ7xoNs2-KrWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76ef585e24.mp4?token=JqtWh_Lqn4ET50WRnNIgBodP8FWXJ8lb5LX6n7laD3TI2-GXB0dgxxupoFju6PfUMPpa-uakMwL9IVO7zf1IskaRlTzJeXl6PVQOqwuntDZzO_7SfoMr9AgZ8r5Wn50QAUbnquopahmuYnR5QCJJqaznwgxiLejieQd42WjPnYcSpXrnqaB0TJKAgXD1rfsKpvrs-bZ9FAirPp4p645JaMOkiJthMHL8AnpsFjOdlYJDzdWuJdqQb1Pm5w9lnIhPXGxo3l2vZVqXSqIg2NYgxv5oJLsbbVneAn24jgfDJqpT5d0S4GUQOgBbOIzapfWC8jN7ao6A0VJ7xoNs2-KrWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میرسلیم:
نفت ایران مال مردم نیست و متعلق به خدا و پیامبره
مردم  حکومتو انتخاب میکنن فقط و اون حکومته که تصمیم میگیره چطوری نفت استفاده بشه
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/73050" target="_blank">📅 15:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73049">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/520264f117.mp4?token=uRB0__1r-Yr_G7_-UhgTUHzSTm0Bx8HPkhRr-skFueR8vwM0XvOvb6rozY4h2ShjDj-Vl7AOkq2QKtN8ZnlPgpFCKyhLXcnHkSPzey447xUoLBE5UsXvlerv0UkYVt-aMYSIfAakYTCmx_1_GKL5EGIMtdHabwU8P_FCYKZtyAUFYfyLBt8K7DjRVhKCHaO8WvCbTnemUKIQ86mWp1uAY98gV6yZ4kSMIPtZf4joxfLZP-ja1LNY6kTUBGMb5YDDia-akAkTyp7ydhf3IM6av5gxB3gXZPd4pdrcopzjYQvf1tnu80haR3zUHKgW33Uic3vBCAx25Rm6CQpmwlShmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/520264f117.mp4?token=uRB0__1r-Yr_G7_-UhgTUHzSTm0Bx8HPkhRr-skFueR8vwM0XvOvb6rozY4h2ShjDj-Vl7AOkq2QKtN8ZnlPgpFCKyhLXcnHkSPzey447xUoLBE5UsXvlerv0UkYVt-aMYSIfAakYTCmx_1_GKL5EGIMtdHabwU8P_FCYKZtyAUFYfyLBt8K7DjRVhKCHaO8WvCbTnemUKIQ86mWp1uAY98gV6yZ4kSMIPtZf4joxfLZP-ja1LNY6kTUBGMb5YDDia-akAkTyp7ydhf3IM6av5gxB3gXZPd4pdrcopzjYQvf1tnu80haR3zUHKgW33Uic3vBCAx25Rm6CQpmwlShmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی وایرال شده از اجرای امیرمحمد، نوجوون ارومیه‌ای داخل برنامه Kaos Show ترکیه:
+ این برنامه، عقب‌افتاده‌هایی که تو فضای مجازی معروف شدن رو دعوت میکنه تا مردم بهشون بخندن.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/73049" target="_blank">📅 14:32 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73048">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/983154ebcc.mp4?token=GLfjrNw7n4EJC7J9p2edp1GERSmFe1uF36EQaSfssZldw6jhr0BDDxtgNoitydoHuRYKinsbPrMab4X2y0rD-Z9AcUOyxBWYXsN5Wvk41wSxcbqpMaJjpZKDZDDxVm8yHJ3VBCFJn11d-_BqRv325hle49glOH8TOgLFOjpkllC88SpzMkwDvMI5dqPo1eXuhrkefW55JQoio7v8SHGgowkdD_E09yWWJPLXS-CAwwKDcYOojKWiahxKSc_9NbAaZIEvCy4uXNtG3KxGIWJoA3NjkZ18-Vo2WNlPR3JPfCPYZgkwRXkAfVZhgCrzl-GpKq62XgX2ULsWyTom1uirzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/983154ebcc.mp4?token=GLfjrNw7n4EJC7J9p2edp1GERSmFe1uF36EQaSfssZldw6jhr0BDDxtgNoitydoHuRYKinsbPrMab4X2y0rD-Z9AcUOyxBWYXsN5Wvk41wSxcbqpMaJjpZKDZDDxVm8yHJ3VBCFJn11d-_BqRv325hle49glOH8TOgLFOjpkllC88SpzMkwDvMI5dqPo1eXuhrkefW55JQoio7v8SHGgowkdD_E09yWWJPLXS-CAwwKDcYOojKWiahxKSc_9NbAaZIEvCy4uXNtG3KxGIWJoA3NjkZ18-Vo2WNlPR3JPfCPYZgkwRXkAfVZhgCrzl-GpKq62XgX2ULsWyTom1uirzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن نصرالله، رهبر کتلت شده حزب‌الله لبنان، ۲۷ خرداد ۱۳۸۸:
امروز در ایران چیزی به اسم تمدن پارسی وجود ندارد.
آن‌چه در ایران وجود دارد، دین محمدِ عرب است.
موسس جمهوری اسلامی هم عرب بود و عرب‌زاده. امام خامنه‌ای هم عرب است.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/73048" target="_blank">📅 13:45 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73046">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/97e3d7ab08.mov?token=htB8IezVQmD54uUQO4yRExCyJRG_CWEBmi3gz3iY76Xl650KveZxdxMz-CBRgNAB2MLpuB69uF7tmtaSv7zd0tvRon5FTmfrZsW8opKCraVg-s25dcKCgasxn24tpS6JpoM4cc2NO4LyzZ0FTbuQCtTM1SlKJtzo51YFIUx8BSEn3EZRjmo4lNU2wmDkNegLWhcPqn3LbmJjNb5U8ffNsL6XMszve_5hoZhgqOmYM6eCtW-YPsagzhbs2bsM8i0HRAruOhYbWA_H2hwf3v9qaojK5ipdMiJiqiEsMbIRAjJeuEhmUhxFhCv3Ufy7vHI8akuZeTqoxYUsuUSW6uMAaA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/97e3d7ab08.mov?token=htB8IezVQmD54uUQO4yRExCyJRG_CWEBmi3gz3iY76Xl650KveZxdxMz-CBRgNAB2MLpuB69uF7tmtaSv7zd0tvRon5FTmfrZsW8opKCraVg-s25dcKCgasxn24tpS6JpoM4cc2NO4LyzZ0FTbuQCtTM1SlKJtzo51YFIUx8BSEn3EZRjmo4lNU2wmDkNegLWhcPqn3LbmJjNb5U8ffNsL6XMszve_5hoZhgqOmYM6eCtW-YPsagzhbs2bsM8i0HRAruOhYbWA_H2hwf3v9qaojK5ipdMiJiqiEsMbIRAjJeuEhmUhxFhCv3Ufy7vHI8akuZeTqoxYUsuUSW6uMAaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب صدای این انفجارها توی شرق تهران شنیده شد که گویا تست پدافند بوده!
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/73046" target="_blank">📅 12:51 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73043">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/351194ef56.mp4?token=bNlQGUiZuoeEZHwjNs_dS59M5wRo58DwKYxnOmmfn3ilzWTQXh6zK7rEspd9tSshywnSy0E9ey2USGNTgLzjkWZ2EWuN7vYyIquZpRSULj3Do5j5PGHju7so19LatSsrmXkTwd8iWBIk0Xb02to78arZZxhExZGJbBNAkTL9ZDYEIwVjTQRLY73vUVt5MPOCL4jVw2oaJp4CuBI0qZmL-osDMTdKb4WE7io5Xy6SV3LMq0DO3UnV4X8IFSuSQKyI_DdZKC6DlsjGzzvzOVfOypTNg8r-Omb7Bs7JysPHq96LepOfAp4p_xXXHvxpu4XV77Ry5y1xk6K7Smpa0z3WTg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/351194ef56.mp4?token=bNlQGUiZuoeEZHwjNs_dS59M5wRo58DwKYxnOmmfn3ilzWTQXh6zK7rEspd9tSshywnSy0E9ey2USGNTgLzjkWZ2EWuN7vYyIquZpRSULj3Do5j5PGHju7so19LatSsrmXkTwd8iWBIk0Xb02to78arZZxhExZGJbBNAkTL9ZDYEIwVjTQRLY73vUVt5MPOCL4jVw2oaJp4CuBI0qZmL-osDMTdKb4WE7io5Xy6SV3LMq0DO3UnV4X8IFSuSQKyI_DdZKC6DlsjGzzvzOVfOypTNg8r-Omb7Bs7JysPHq96LepOfAp4p_xXXHvxpu4XV77Ry5y1xk6K7Smpa0z3WTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیشرو و هیچکس بعد از ۱۰ سال قهر و دعوا، دوباره باهم داداشی شدن و دیشب کنار هم روی استیج رفتن!
نکته جالب ماجرا این بود که سروش هیچکس فریاد «جاوید شاه» سر می‌داد و سالن رو به لرزه درآورده بود!
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/73043" target="_blank">📅 12:14 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73042">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/73042" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/73042" target="_blank">📅 12:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73041">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H3OHgO9akoUpUc4TfDLseYaVi54X73SkcS5pUXCm8UFEOQPwL-ZvGsB9pmFIbDpBMQ0dAz8rxT6wYp3sZDYg1uFf4p4m2L1bpQRx2VnoVGh6RFTHoHYDArAKu3LZWyqlidcL-ZxeZYueH017o9Hr2H1Z-Gb_059iwPmraY6WckWY76AUKDARPl8gUlUd8HsivQumPa7PQ-qbEXsLKARx37AqIQwvgNHkl-yiE7dVwKb67j1KisM-p98nP5_SCY7k2IU_KEhcUZwk8r1XFBpD2EoX1PNDAHMZlbiMOepVTzzNbwiZDm3akruf6m02EehKjcYziS7iMkvedrYgxL25YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
لیدز
🆚
آرسنال
بورنموث
🆚
چلسی
تاتنهام
🆚
منچستر یونایتد
ختافه
🆚
بارسلونا
ویارئال
🆚
رئال مادرید
بایرن مونیخ
🆚
آگزبورگ
پارما
🆚
اینتر
فروزینونه
🆚
ناپولی
لومان
🆚
پاریسن‌ژرمن
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
https://TrexBet.com</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/73041" target="_blank">📅 12:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73040">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e742ff38d.mp4?token=R8QeyqH34-K39a7GMHOjjJi_MUMbsIhtTMubdSpFjOszedNrOEKzvgDhWHEDc4YN3uP6KXohPtzW7dKuv0jmDODaCfdKf_yiKBmO5fU9m-kFDRAoeVxadDXlkJEtwP2XFLNYXKFSX1TrhhQM9ksq04pJ58ui7z6EDzmApwb26tsaSKBJlf-_gnSwwhjtzsE2ohTMbHRBPJouKiQdff1PP3lDWC2ts7kEjVoteBWKzsJ9Jb9F7OUUOEbzgdkR7RgzQBKc7GMHqmARL9izb4v_leih24RiQvqa5YQSGPxQeqDIyh2crvRrn7JxMHTVjuIGU20ccY_bm58as6nGSQrTWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e742ff38d.mp4?token=R8QeyqH34-K39a7GMHOjjJi_MUMbsIhtTMubdSpFjOszedNrOEKzvgDhWHEDc4YN3uP6KXohPtzW7dKuv0jmDODaCfdKf_yiKBmO5fU9m-kFDRAoeVxadDXlkJEtwP2XFLNYXKFSX1TrhhQM9ksq04pJ58ui7z6EDzmApwb26tsaSKBJlf-_gnSwwhjtzsE2ohTMbHRBPJouKiQdff1PP3lDWC2ts7kEjVoteBWKzsJ9Jb9F7OUUOEbzgdkR7RgzQBKc7GMHqmARL9izb4v_leih24RiQvqa5YQSGPxQeqDIyh2crvRrn7JxMHTVjuIGU20ccY_bm58as6nGSQrTWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میرسلیم:
مرگ مردم در تصادفات رانندگی به علت رانندگی بد آن‌ها است و ارتباطی به کیفیت خودروهای داخلی ندارد.
واردات خودرو خارجی باعث می‌شود کشور پیشرفت نکند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/73040" target="_blank">📅 11:27 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73039">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e55bfab16d.mp4?token=FAnQE72dUm8WOFKNHCmzHKcUJAZMCKMGid5e7HLyGw_NnRdKmlBxQipf4OlHu0jX9pfklB1EZKFDPrUBYPfGP8FI7rkXKpnj4b2NEDEvIbWJhdRgqPkQn-8gCtwcNKUWQNfoHep7SDGSvXGkueNny1mhAHmM4acaNlEEkwe1V-Zn9ut3rH3pvDXbsB_KsXVa5rjxmARyIk9ddFiWh4h2sOCm4jpqSbkjL5OfpUnLWNsfHeqU7MKNXnhhe_2Hs_d9x0szTffMymTvJs6d9URg6ZuGfZUXxN1tCrWbHSzAu_n9iH1Va7A1pl5oKMs_Z6rqoDNRCn8KNhJplQ78u9tifQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e55bfab16d.mp4?token=FAnQE72dUm8WOFKNHCmzHKcUJAZMCKMGid5e7HLyGw_NnRdKmlBxQipf4OlHu0jX9pfklB1EZKFDPrUBYPfGP8FI7rkXKpnj4b2NEDEvIbWJhdRgqPkQn-8gCtwcNKUWQNfoHep7SDGSvXGkueNny1mhAHmM4acaNlEEkwe1V-Zn9ut3rH3pvDXbsB_KsXVa5rjxmARyIk9ddFiWh4h2sOCm4jpqSbkjL5OfpUnLWNsfHeqU7MKNXnhhe_2Hs_d9x0szTffMymTvJs6d9URg6ZuGfZUXxN1tCrWbHSzAu_n9iH1Va7A1pl5oKMs_Z6rqoDNRCn8KNhJplQ78u9tifQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مایک تایسون، بوکسور افسانه‌ای:
«اگر رئیس‌جمهوری مثل دونالد ترامپ وجود نداشت، به‌هیچ‌وجه امکان نداشت امروز اینجا باشم. متشکرم.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/73039" target="_blank">📅 10:40 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73038">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d334669b16.mp4?token=MFFCK-f9n53fF1hSl3Pw3OqjOzA73JLjIrfEOJuelLKUfT9z-5HCtHFeJw1ykO4U-JF0BJ3HoPf9oi7Cc_v08QqKT_S-IaaYPXUi7RXu0WAVJcTV3VNUGW3YTYye6UEBJIUviQ2xMO0hk2NX6WPPMhtVWD7WhffAxjHhB3T6cqmg9RhUi541WM0tBgZlpVlFNqHKGV88j7qKoZebAOdaYQe2p7z7FRAij5OOBXSnfbM3zLYzoCpAL1qyu4Wk2yCZkrXj6COy1kISzJWs7xd7chvUYa2D3QCoxU37aiMW8fingtnR40OA2K3LqGxg6bQ01Y_fIYhXeOk61xogIb-4oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d334669b16.mp4?token=MFFCK-f9n53fF1hSl3Pw3OqjOzA73JLjIrfEOJuelLKUfT9z-5HCtHFeJw1ykO4U-JF0BJ3HoPf9oi7Cc_v08QqKT_S-IaaYPXUi7RXu0WAVJcTV3VNUGW3YTYye6UEBJIUviQ2xMO0hk2NX6WPPMhtVWD7WhffAxjHhB3T6cqmg9RhUi541WM0tBgZlpVlFNqHKGV88j7qKoZebAOdaYQe2p7z7FRAij5OOBXSnfbM3zLYzoCpAL1qyu4Wk2yCZkrXj6COy1kISzJWs7xd7chvUYa2D3QCoxU37aiMW8fingtnR40OA2K3LqGxg6bQ01Y_fIYhXeOk61xogIb-4oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوووری
؛ پرزیدنت ترامپ:
«ایران یا همه‌چیز رو به ما می‌ده، یا دیگه وجود نخواهد داشت. خودشون اینو می‌دونن.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/73038" target="_blank">📅 10:14 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73037">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">میرسلیم:
تیبا با خودروهای خارجی ظرفیت رقابت داره
واردات خودرو باید یک در هزار بشه هموناییم که وارد میشن برای این باشه که ببینیم چطوری ساخته شدن
مجری:
الان چرا کشورای حوزه خلیج فارس همه بنز و ماشینای خارجی سوار میشن ولی ما سمند و تیبا و دنا با این قیمتای بالا سوار بشیم...؟
میرسلیم:
میل و انتخاب خودتونه دیگه
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/73037" target="_blank">📅 10:03 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73036">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">سپاه  تصاویری از حملات پهپادهای «شاهد» و موشک‌های کروز به شناورها در تنگه هرمز منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/73036" target="_blank">📅 09:31 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73034">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ویدئو های وایرال شده از دعوای پشت پارک یه مدرسه دخترونه در تهرانپارس که دو تا اکیپ با دوس پسراشون رفتن داخل پارک بخاطر اینکه یکی از دخترا همزمان با 4 تا دوس پسرِ دوستاش داشته خیانت میکرده به رفیقاش و گرفتن چند نفری زدنش و دوستای دختره هم برای دفاع ازش اومدن!
نکته جالبم اینجاس که چرا دوس پسراشون ایستادن کنار نگاه میکننو نمیرن جلو جداشون کنن و گاهی تشویق هم میکنن که بیشتر بزن هم دیگه رو!
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/73034" target="_blank">📅 09:02 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73033">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/73033" target="_blank">📅 01:55 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73032">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WsGedYi81ikSFIhe59St12U-24DqNFsmC8g8d6pX_Ma_HEG-Bk84fiNzlaVsXcfyhdlB1LG1Crpqy6A0fEP1FK3fVliMwIUb5xJPU5HlG68qocdXm3h9JMl__FbRGZgrKpj_iIiEJ_7a5BQj7iZP57C4lPZ4hhpnx5QNOBNoMWDD4S5V_pXCbKUKEsW3fdrZYELwjoEthK_g5YlAC5WsEPR-KN2Z06kW3-3Whk5GiW9CAyiX4hQI6UFNTRyy6N2RKD7vwGUjb6Wm1pzklSLMvrPiKCqyKglp5eKd3n51VT7jqcu7yWXEZ38PyHXdQ_M3nJmXAuQddq6O6bZyH9tCGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/73032" target="_blank">📅 01:55 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73031">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d4fabef22.mp4?token=rpSZ1raB6T6x8jaa5I7ZdMoBs9s_EtD-luJfj7D1SFfInucCtVW45R-gYs65omv4IXk8WyyKDwwqiDsaFqmsAmWHOcto7-YN5bEcycxhKts212s4TByCMm3HgyiI_lw0BTi26BwWcqJr67_UqjWK50jvfWUNNy_JinXJuITYoAmT2ofdNN2ZUMgMIl7TRjP6zuFJsuHO9mGcnbkaIn35J9KOtLbyxYMWXeXTtuzl5rqkrEvEvVDNPDyE7SzXqx2wB21cy-FPu4oOaskYZdWnApRI0UT9x_mKhF-d3TAsNneJ0iwmAsl8EwKJ00MbxYRo9TTCbqLNfKh5fA9uay_vvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d4fabef22.mp4?token=rpSZ1raB6T6x8jaa5I7ZdMoBs9s_EtD-luJfj7D1SFfInucCtVW45R-gYs65omv4IXk8WyyKDwwqiDsaFqmsAmWHOcto7-YN5bEcycxhKts212s4TByCMm3HgyiI_lw0BTi26BwWcqJr67_UqjWK50jvfWUNNy_JinXJuITYoAmT2ofdNN2ZUMgMIl7TRjP6zuFJsuHO9mGcnbkaIn35J9KOtLbyxYMWXeXTtuzl5rqkrEvEvVDNPDyE7SzXqx2wB21cy-FPu4oOaskYZdWnApRI0UT9x_mKhF-d3TAsNneJ0iwmAsl8EwKJ00MbxYRo9TTCbqLNfKh5fA9uay_vvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ما در هیچ زمانی پیش از انتخابات میان‌دوره‌ای آمریکا در ۳ نوامبر به ایران حمله نخواهیم کرد.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/73031" target="_blank">📅 01:47 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73030">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MhfdI5yfl8PmMV08Z6q9tP2TmykrcFYQqfk6bqbfeK8WaTQhHtJ8jmnOYBDwS0Y2K2btiLSpnvNs3fFckQUuk2IPpGPUOr-wCyLUvTFAfuawagMDwljLg5SYm-h5NG0a0Hbja-u0FWk3SdIM8y_eWBHAqDbsxpHPiHH5tB3kbBgq1XfTylHXomuJdu0kDat88QvmQQronW-T443JEEUc4bTnb3uvWZ_7HfiVmqJtfafiBCd36BZGRDu6w-hf9ArJc8xL_qMP_75RrGufIW-eVIU7Q0_givdQfZzrhe4D-rmFCi51pXszqtrkCTZUSg8TdNn-WUY2HWEsBA9azlsFTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛
هشدار امنیتیِ وزارت امور خارجه آمریکا:
به شهروندان آمریکایی هشدار می‌دیم که فورا ایران رو ترک کنن و به هیچ عنوان به این کشور سفر نکنن!
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/73030" target="_blank">📅 01:14 · 18 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
