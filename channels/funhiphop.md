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
<img src="https://cdn4.telesco.pe/file/Zai4LCb0uhtXYbzoHIons0JyxEsqsqGySXsWD5lnwAlQzyMX7G5rf7yimedA6kHjULBKtTCXQpteImxQxouzHMlIR-uqmoraalO6lekhptjEf8P1Sm4_mrFFx9gkfPkLh9a_yv8pkxJ16yaRfHkfB1hHqyBNI1WBGsBfJHpxHp2lkMzA1Vpb6xnJlCsjYEB-ufC5ui89HAngBtDE4JKO1P2NhDkHEvudGg_ujCu4Q_bwNIEmAsxIcKz46-8QCM02yujYYfRTfItrHaQT-N1oH_eJQvcJ8WVUG31iFA6YbjWrlKBA0QSWsNlUURlOCYeWRZralpBGyOrSxJH6YW-QyA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 168K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-01 21:30:16</div>
<hr>

<div class="tg-post" id="msg-78509">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">رونالدو فقط و فقط ۹ تا گل فاصله داره تا آقای گل جام های جهانی بشه</div>
<div class="tg-footer">👁️ 308 · <a href="https://t.me/funhiphop/78509" target="_blank">📅 21:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78508">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">متاسفانه نیمه اول تموم شد و قراره به مدت ۱۵ دقیقه از تماشای بازی خداوند اصلی فوتبال محروم بشیم
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/funhiphop/78508" target="_blank">📅 21:24 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78507">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qe4s3FzXSpwl0Yfcxbq4qOOnUSggt_rGfCkUpRqfwVkYr32EWL-a7mEu9Q0E9QYNe5xH-9F-te-DVoICThysNyPVvnbLh5pnI3Iddr-9nbQ_SOLKc2HHNk3c-fg_dkuisvWuSkPVOtuMRUA4oRX10Si017PK4tWuHhamNe6RPZCcRlyDSixkw0DjWrnJ8m8viFvN-ZbYzrFrRdBBAo8eu6vTvWQ9iNooAN_I4CSU_w4u1oH6Q-Wlxgenyoz0ZWFbcTntFzvU56dD88y5uZ_PjKkjYksmuHRzXDKTn7nc49kPcC1Ewm35uAbakdZ7mbvrSz3c4tM3ygEwhTVwRDwEQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/funhiphop/78507" target="_blank">📅 21:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78506">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aiDboPs8_Wy2IgTDBZhdbSmYEWWarHOxc8EdprPCwheTXxwmCe9CAiRgUwjKW-kgD39TugFIpfB4zuYAJmFM-PggHZyrOXwDZhQw91mfAHB5piorJRlVV961u2TRRYPzkIdqN55i8O4VvpXtvKa66bXLQeS9ThYZ3regvNsmmOGouzEQhNNlOlbOOUq61ko0jVoxWrlQgS6hIyOv0z7TstcBReQTYh36tcEifqFrPRS9vQ_pyWAKcKpM8DyxB6OCnTpojoERZKW9RugaEGh9TRx5RAlCpHr7ZAgBdbqmG2wq_kJcZGmIqLWZPtxJQq5YoHAUEoQS84195xWOXFJXsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/funhiphop/78506" target="_blank">📅 21:12 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78505">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">رکورد کلوزه شکسته شد
سر تعظیم فرود میاوریم به احترام لیونل آندرس مسی
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/funhiphop/78505" target="_blank">📅 21:11 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78504">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">اسطوره بی همتای فوتبال جهان
گل اول رو میزنه
🔥
🔥
🔥
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/funhiphop/78504" target="_blank">📅 21:10 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78503">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">و گل مسی زد</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/funhiphop/78503" target="_blank">📅 21:09 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78502">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">یه بازی رو آرژانتین زدیم مسی تبدیل به رونالدو شد</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/funhiphop/78502" target="_blank">📅 21:09 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78501">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">یه بازی رو آرژانتین زدیم مسی تبدیل به رونالدو شد</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/funhiphop/78501" target="_blank">📅 21:07 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78500">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">رونالدو اینو میرید رسانه ها عزیزاشو میگاییدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/funhiphop/78500" target="_blank">📅 20:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78499">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">مسی کم بود بزنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/funhiphop/78499" target="_blank">📅 20:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78498">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">پشمام
چی گرفت بیرانوند
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/funhiphop/78498" target="_blank">📅 20:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78497">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">وقتشه پرتغال یه ستاره بزنه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/funhiphop/78497" target="_blank">📅 20:41 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78496">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">نویسنده کتاب تاریخ فوتبال اوانس داد و پنالتی رو زد بیرون
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/funhiphop/78496" target="_blank">📅 20:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78495">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">پنالتی برای آرژانتین
الله اکبر ازین تیم هجومی
🔥
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/funhiphop/78495" target="_blank">📅 20:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78494">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">دسخوش پسر فیفا</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/funhiphop/78494" target="_blank">📅 20:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78493">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NDSHkcEiAhblYQRvCVPsQUvTilRQu0lYdLc86n0S4oOOFG1q-5BJ7sQEaY9LXo9b6m8WA23w51q5LsrIgyTKwcVRXSERlypah4drYkjizk9DCJTsyOxS84Mvq10PCkXI7Mjp4gVBDRbWHGDkA8tkgL5rGNTirwPfs6lmvAj-Tb5TnIypXl8x5gmNlFhYlFdOdpl6jSvVGXC0rG_4tojz2EtChtxaowk0oGM0XROJ8JDx6enqdrL-I9bkANh2oSQ-HtgKUVODJ8Y2ZtKV77Z-qOdlXPeGiFJ3SS2MsyK560t6eXs-RiQjFfd_okk6nCTNifhl7z38dfoCCn1Qmd7t6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این پیام رو نخونید!
نماینده رباط کریم رسما درخواست فیلترینگ میم الاسکی را به کمیته مربوطه ارسال کرد!
میم الاسکی با سابقه 4 سال بزرگترین چنل میم بودن بهترین پست های کل تلگرامو جارو میکنه و با ذکر منبع میزنه چنلش و باعث شده مجلس از دستش فشاری شه!
جهت حمایت ازش جوین شید:
@meme_ol_ski</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/funhiphop/78493" target="_blank">📅 20:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78492">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">چیزی به بازی پروردگار فوتبال جهان، حضرت لیونل مسی نمونده
به امید درخشش برترین بازیکن تاریخ
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/funhiphop/78492" target="_blank">📅 20:18 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78491">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49461d24dd.mp4?token=dwhm1DWPmCRTqca0Swot6f1hgF-cT_fef1LyjAOEN4Y73HsX-uzWtIQW-u36l4Q9mm9E0TAFactYXvau2tsPYvEY3nqKtHU6I0UkUkGW8ECjreo2QVX9jUdAASLB3dLi6ElYwNdG6LmLnJfTEQ7ncXYfqw5Hxryc4PhQf_FJHaLcMnFUy3ZaEeHI5qslQYKezDjBa7JlrwI7dJy16mGK0Ma_wyMo5K_SsGXk3P6Bhh5J1iK63X_ptXSPvqycnse87J5GKg-co9lEA_OdQcJVb3l3ygDaTAczVresQnCek7KWVOhuxeG3n4YlWMO7e7U9r_Bwyd_BaFTohED7_7gvTyol__tfHpTh9TL9KkMcIFbdMLSSi3JyvCsUZZEdsYJtsu278SalxQh9nQZX4Pao5MPZZbpjmJ_b1cSuKIhkaoz4RDK3sQEUS6FvUjgLZjYr6MXJaSUfObEZX6UIwFCa-KoMhEqUWQqSq8wFqMXQmnJDQpvAkpNBi9FjNAZFhl0i8qEl5QiSiqS4faSdD_DZg--loMDmRv7T2GgfUpZN0PQwvTQh_WvKnmE3m7qG5sJRaitlfj1EgWMfG6D8aXWES2k3Xsx-6GCfkRsX-m6sQp8MAeztb1puxaU6FaYLRRpi7Nyd5AWwBNMkcvPCEDh9lzfRjUeqYbURhnBLBBNljzM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49461d24dd.mp4?token=dwhm1DWPmCRTqca0Swot6f1hgF-cT_fef1LyjAOEN4Y73HsX-uzWtIQW-u36l4Q9mm9E0TAFactYXvau2tsPYvEY3nqKtHU6I0UkUkGW8ECjreo2QVX9jUdAASLB3dLi6ElYwNdG6LmLnJfTEQ7ncXYfqw5Hxryc4PhQf_FJHaLcMnFUy3ZaEeHI5qslQYKezDjBa7JlrwI7dJy16mGK0Ma_wyMo5K_SsGXk3P6Bhh5J1iK63X_ptXSPvqycnse87J5GKg-co9lEA_OdQcJVb3l3ygDaTAczVresQnCek7KWVOhuxeG3n4YlWMO7e7U9r_Bwyd_BaFTohED7_7gvTyol__tfHpTh9TL9KkMcIFbdMLSSi3JyvCsUZZEdsYJtsu278SalxQh9nQZX4Pao5MPZZbpjmJ_b1cSuKIhkaoz4RDK3sQEUS6FvUjgLZjYr6MXJaSUfObEZX6UIwFCa-KoMhEqUWQqSq8wFqMXQmnJDQpvAkpNBi9FjNAZFhl0i8qEl5QiSiqS4faSdD_DZg--loMDmRv7T2GgfUpZN0PQwvTQh_WvKnmE3m7qG5sJRaitlfj1EgWMfG6D8aXWES2k3Xsx-6GCfkRsX-m6sQp8MAeztb1puxaU6FaYLRRpi7Nyd5AWwBNMkcvPCEDh9lzfRjUeqYbURhnBLBBNljzM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس علوم غریبه و جادوگری در شبکه ۱۴ اسرائیل:
دلیل اینکه یهو رفتارای ترامپ ۱۸۰ تغییر کرده اینه که ایرانیا با استفاده از یه سلاح الکترومغناطیسی با فرکانس پایین که توسط ایران و روسیه و کره شمالی ساخته شده، مغز ترامپ رو دستکاری کردن و این افکار مذاکره و امتیاز زیاد دادن و اینا رو تو ذهنش کاشتن؛
از منم خواسته شده که مغز نداشته‌ی ترامپ رو به حالت عادی برگردونم، منم دارم تمام تلاشم رو می‌کنم خواهیم دید چه خواهد شد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/funhiphop/78491" target="_blank">📅 20:12 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78490">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ایموند داداش این چه کاری بود کردی</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/funhiphop/78490" target="_blank">📅 20:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78489">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ahe5IBlL2rs5dYT1EBkm5Hzw8lfFxur7-40GAlkzmtlnz4sSkDlFlAv9p1Xi9J6vLVjOK6AcSmOw9rLsYhv4sVBPg8xWFBszUZXso-G0TrgXG3zcdQ9djPV2NRVvC57i2d6KGygnx8AfVrKMlKShy0P468dPOvJJh8NKl43LohEgcbalLQzL7yhsgyUMWIBjDEwIylBNLw7CK4VD5OBsUbwYzU_iGrQyTkly1V4RvIP3eT8L0idiYGp4-TkJRy1hUp1VeoOM-QM-MWmnG4wEkimquDGIQd_AmJJ5QsRtyplh_WpZ6PgWitDNuiftnasn1bjCPpeSWpc5tEY1xrZi2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دست خدا عیان شد سوارز جوان شد
بازیکن جدید لینک شده به بارسا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/funhiphop/78489" target="_blank">📅 18:58 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78488">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">فدایی به هرکسی دیس داد طرف بعدش چرا زنشو طلاق داد, اون از هیچکس اینم از حصین.  @FunHipHop | Reza</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/funhiphop/78488" target="_blank">📅 18:52 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78487">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">فدایی به هرکسی دیس داد طرف بعدش چرا زنشو طلاق داد, اون از هیچکس اینم از حصین.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/funhiphop/78487" target="_blank">📅 18:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78486">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">حصین زنشو طلاق داد
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/funhiphop/78486" target="_blank">📅 18:46 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78485">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">آمریکا تمام تحریم های نفتی ایرانو به مدت ۶۰ روز برداشت و ایران تو این مدت میتونه به قیمت بازار آزاد نفت بفروشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/funhiphop/78485" target="_blank">📅 17:26 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78484">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QHQ0Av46h2IFoaSf7pf6ujbzj7IFm5hCZqachT79lxbxM6Rz_0M1FvZG85nwQRbyWgLj-8B9aV9l9-eEQbbIj1_6jQHrYrSWGm0gvmwy-KGfTPJTBrFADiLic1OE6N0YtKNP0lJtJ91jBGoeZ5QvvUH1IjKvOw37S8_Y1C4nu5_p7eEEuRt71RCqXE1Ruoa2Cq8ViSdZ75YxXsKyp3AyzsA-u8t1gd9ifDuHvnVGj8P_Kbd5HXgtNDqWuruKRGVWWrRg-LOfYkn_Ge2ajpzoBCuXfkU0cxBdsxpmiUtZVv8vZ6xm4F81nl1sEAjfbU0H_HcueLGmuM1OBg1LeWglmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خودمونیم ترکیب دیشب ژنرال جلو بلژیک چقد هجومی بود.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/funhiphop/78484" target="_blank">📅 17:24 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78483">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🎁
هدیه‌ی ویژه برای کاربران جدید،
0️⃣
0️⃣
2️⃣
🔤
شارژ اضافه برای اولین واریز
💳
وارد سایت شو و هدیتو دریافت کن و با خیال راحت پیش بینی کن
فرصت محدود
🙂
🔤
Winro.io
🔤
Winro.io</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/funhiphop/78483" target="_blank">📅 17:24 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78482">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qfutxi1uzd5u4sfET7_JZecZ1dzf5HdKW0Dc5Qz87LJtZoMsSokSaC_uGSzYmOqpiD-FA2pXG3PD6kwDsm8qnHVCTiqW9ksbD6eFSdaVTh4g1p1cMOvjMAGMK0rgvk6N-JNTg9U_agXf96nca0Xjr6-R_sTr0LDiruw4bAkuhA4vIgZVLEq-mMujpkvtBw9CFVJDueB_d0eM4J3AEknlWg9S2W6ju3Yh3L8qtM_9FH-bspI8SUrHIWU1subNbUy7JLsxM8reA_Qu4VLWXNQ9h_S0VuTwJkxExg3owfyTlgBiT0t9b86bYeMuBhGr0WcZwhZfK_-S_vZAR-SEAnA_sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
هدیه‌ی ویژه برای کابران جدید
🎁
اولین واریزتو انجام بده و
0️⃣
0️⃣
2️⃣
🔣
بونوس اضافه بگیر
💰
⚡️
فرصت تکرارنشدنی به مناسبت افتتاحیه
⚡️
🔴
تا سقف ۳ میلیون تومان
🔴
⌛
فقط برای مدت محدود
💣
بالاترین بونوس‌ها فقط در سایت وینرو
🗣️
امکانات ویژه‌ی وینرو
G1
🅰
📺
تلویزیون لایو برای پوشش بازی ها
🛍
پیش‌بینی مسابقات با ضرایب رقابتی
🎇
بونوس‌های متنوع و جوایز ویژه
🔝
تجربه‌ای سریع، متفاوت و حرفه‌ای
🎰
همین الان وارد شو و با اولین شارژ تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگیر
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
📱
کانال اخبار و هدایــا
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/funhiphop/78482" target="_blank">📅 17:24 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78480">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">رفیقم زنگ زده میگه ضریب عراق جلو فرانسه خوبه ها
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/funhiphop/78480" target="_blank">📅 16:18 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78479">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbfa646697.mp4?token=nEsQopdD_-BiPXv2lFP75yrbQ2MjKNvSILW9Jf0gc2WevRmYtBj_cuF3rVR60TgFOxOi85urkV5gZhobG9ZK0Ka-m5MSDvr9_g1QHB7jYtHjK6HjlW3c8ruf4jznK6mGw9NDW06OLE_dvm_fhR8In5PhEBtLY7wYRaiY82T6pBxap1iwZN80OkUlPv7qN69v1QwQ7DNRqtb4380hKTL0z5_CQ9tAX5Ry_mMAFIcO0mRTpwUg16Sj_SVSvXL0jVAUXz-ueNDWVtYDPhbLiueFmbOYdh_73LTnEhCV0tv9gCfc9ss9UXP9jSCXFO9Io9uWlZ9PVyeUvB2oqVfmsuUnFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbfa646697.mp4?token=nEsQopdD_-BiPXv2lFP75yrbQ2MjKNvSILW9Jf0gc2WevRmYtBj_cuF3rVR60TgFOxOi85urkV5gZhobG9ZK0Ka-m5MSDvr9_g1QHB7jYtHjK6HjlW3c8ruf4jznK6mGw9NDW06OLE_dvm_fhR8In5PhEBtLY7wYRaiY82T6pBxap1iwZN80OkUlPv7qN69v1QwQ7DNRqtb4380hKTL0z5_CQ9tAX5Ry_mMAFIcO0mRTpwUg16Sj_SVSvXL0jVAUXz-ueNDWVtYDPhbLiueFmbOYdh_73LTnEhCV0tv9gCfc9ss9UXP9jSCXFO9Io9uWlZ9PVyeUvB2oqVfmsuUnFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/funhiphop/78479" target="_blank">📅 16:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78478">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">برنامه ابوطالب فقط اون تیکه هاییش که اینستا میزارن جالبه، بقیشو ندیدید هم ندیدید</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/funhiphop/78478" target="_blank">📅 16:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78477">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">کورتوا حسین کنعانی رو فالو کرده، احتمالا بمب 150 میلیون تومنی پرز کنعانی باشه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/78477" target="_blank">📅 15:27 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78476">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">پشه مادرجنده مگه قرار نبود فقط شبا نیش بزنی</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/78476" target="_blank">📅 14:29 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78475">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GK0er49TfgniShfO86WidDhXtpMB9-odAet3SiYmRbdKD_c-9LJ1yD1Cq7Tk6pbcXEazsBp6i7ig3aEFc3l1qO66hTkHgmExSvtpoDFvZSF_SqLtxXrExGKEx-dt78sT7ER0Soi1tscPOi9F-4JlPgSbmvNfUN3SzjwhAzvpDjYgqnmhpl13lfwTJrsaBl1bboJelByjzGfJEWS7vQX4XviMuWa7YrLdn8Mdsjb47ONclCbIKbCi9Ml-TS4yAIc1akO2BroAvBervCH6NQgslsPTIpmQxTLFIn3fI7wyv-wVnl7Gt6J9CYGbgTl4PglYEXcbguk13tfuEND-WRxMrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا حالا اینطوری قانع نشده بودم
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/78475" target="_blank">📅 14:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78474">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">تو جام‌جهانی فقط در صورتی که دستشونو بگیرن تو دهنشون فحش بدن اخراج میشن؟ یعنی حالت عادی بگن کص ننت هیچی نمیشه؟
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/78474" target="_blank">📅 14:07 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78473">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uCt5PRKIsv9VXRdHFVQy6yS96zyNTnxrTAUpmyTC7ulzGnb9zbTVmKUdfjrHuv2kb96ANDLaSo2XPR4W9zBpJPfnm5RZ9NDCAj-qYhM52RMMBaFKAYJJDi2D9GdbKZc6GAeEStqaud-qa6NtQWWDEk7GVrjxEg2wc9ICgZ35PzJXNAsyuQyTJuIQRZ11TzYU-hPW6A18qGRPdSloAOLgiqdycrU0ltYb1sqneFbH8RzA2eUXRCXOfRF1m4MrEd81Z0ZtNVn5YDg2pW2q2mB3G0Ld6eZIumAeQEJrhkJ4QZgx4YDZIPGTCZuupmQsFEtAzoIrkJyXqure88lOFBZkHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوروش کبیر از اون دنیا هم رفت
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/78473" target="_blank">📅 13:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78472">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">با توجه به اتفاقات اخیر بنظرتون بهترین آرتیست نسل چهار کیه؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/78472" target="_blank">📅 13:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78471">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">کیرم بعد ی دوری بسیار طولانی استعفا داد و برگشت پیش خودم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/78471" target="_blank">📅 12:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78469">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">هر سری که کارت بلو میگیرم جنسش یه لول افت کرده، چه گوهی دارید میخورید</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/78469" target="_blank">📅 12:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78468">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">هر سری که کارت بلو میگیرم جنسش یه لول افت کرده، چه گوهی دارید میخورید</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/78468" target="_blank">📅 12:29 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78467">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_7AodVo5P1Ce_AQ2FYc0snSqSY3jc6WroXnm4IsS0z2UcktBSpfKXkr2wiBrmhqwf5G2yyH36jPDH61HmaTsxcjKcpS1ZGxgHPEBhPTtW6DRQHfKnqTkyrIhZ1DYcKj6GU4dgZBr23hEzAkzfTwd93JCBFunsSFRGnHZbpLUKP2bNTStWq4FuzEqhzhu4p8sm1KtK9i_80dbGh52ENCdG9RRt1cM0aI0-kG3ZG5EVln7GBr9yYKEXsKLJaZ206m-cg9L-n1l-8CguyOWmnC0LCBzI60l0-CMRr74_z3b8F37NR-KapIswiaxLq24bd1YzcR4wH22HVhjGwyIGuQ9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصر هم بازی خودش رو برد و جدول گروه این شکلی شد :
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/78467" target="_blank">📅 12:15 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78466">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VtILpiWkoPXAUQXVQAkhelp6VRnsM1fFHBZMSnTVa0E4YQyh3hGZ2Q3raKue1g5Ynn1zu-PCyJQF_fTL4Qj-bsYKlWM-YlroKzJzKCzv3c6SW2EPr7hwbjdbA-u8xEFeoyPIczjx3aV9ERzc5D4NUdGFXfIU__QRgMo2TVSONSEezab25l1hAU13flr5vaCGTpO-_LTU6mU1Ztws1DI1tdi_fGMd1iLi_MI5lHzZ6D411XqU5Lch51LCKIxFurP4MT1ssqddAp2AUmEZf7JkvKM0Np23jnxPm2Px-Uc7OFhcyVZu9huvryTO6-xgdAEaINBXh-_faYGEwsewp2B3pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب الان این چیه کیرم تو دهنت
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/78466" target="_blank">📅 12:11 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78465">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">😄
😄
😄
😃
دلار درآمد با معرفی دوستات
🤝
💵
همین الان وارد شو و علاوه بر
0️⃣
0️⃣
2️⃣
🔣
بونوس اضافه اولین واریز با معرفی هرکدوم از دوستات به وینرو تا
🤩
🤩
🤩
🤩
دلار درآمد کسب کن
💰
فرصت محدود
🙂
🔤
Winro.io
🔤
Winro.io</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/78465" target="_blank">📅 12:11 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78464">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c6E8VEGTmar4OYg-5_aEk4LwGcC08oCDuxBax0x5lEqwIMJGutMPS-_Rx5W_33tsellt_JRDhLWYPjYbyoNzfNzYh1BDwfFdaDxmZ3-mGveIspJoFpCtdvX-INQF1MqZCRs670de-EjgT6xVESWkIQEhJ3l2nPgKuOE5CDW9shsdlPybu1VGgZRsmqPSvM9gHd0HZgCz3bE3k1YM1W4rFcqqmauMr_9WJwr1ysTTZFgUrqnl-qg1D4-XaiseKMxWRcouSqbMsnNr70W0HRnSj73A10qOqv1jk0RZ0bPUA1pocKLUcsObMCD3UIdXeaPqbrYcIUWiMfE5zW2sM4BgMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا
😄
😄
😄
😃
دلار درآمد با معرفی دوستات
🤝
💵
با معرفی هرکدوم از دوستات به وینرو میتونی تا
🤩
🤩
🤩
🤩
دلار درآمد داشته باشی
💰
🔝
فقط کافیه دوستتو به وینرو دعوت کنی و کسب درآمد کنی
این پاداش پول نقده و لحظه‌ای به حسابت واریز میشه و به صورت آنی میتونی برداشتش کنی
💰
💣
بالاترین بونوس‌ها فقط در سایت وینرو
پیش بینی کن و برنده شو
🎯
R1
🅰
📺
تلویزیون لایو برای پوشش بازی ها
🛍
بالاترین ضرایب ممکن
💰
expert tips bets
🎰
راستی با اولین واریزت هم میتونی تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگی
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
کلیک کن و درآمد کسب کن
📱
کانال اخبار و هدایــا
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/78464" target="_blank">📅 12:11 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78463">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PpXKKQfJpqBlBJhTJErB3Dg4QVKHBDv-Qh0x7PLuMOb4ha7aEeh_M_jwCi1tR1DIma6N0Pp99R5J0DKv1ZZH0cNtNmMbYwrGWDUAjIVw_bfJiBZ1TZBM10X_FjgUfqlru63iKzu_UIw7kB29VhEKsTXzzAASA0iI_TM-SA0ksVHQa15Tr1vqQDM8CVEoVPcCZmMr8l0-M2eRmygkkbvb4M5IJYJgvTTYB5QtqTZBU53J_4ZQfEW0knotr0Z86RbOD9rM0Z6HcQojDrcax6KeUEq_mD9KqMApp6eNDjidcBapov0i0cNP6vUHirQZkxfV_RN1bZVy_rQCvIohJN1R9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یاشاسین تیراختور
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/78463" target="_blank">📅 10:05 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78462">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/naF-oCngAZ1RxsnjoyaDVcyeqxLti7IXLUPKV-G5f7z9QFeWVrYU4bugLTORX46Nf-7Vrio6lO-kzbZ9a6Ijih0JZLZdLJa9ncpKDC0XLQ9tjRhqrvFAzQaYprFhR3GfpvLERov0ejUah2RPRvrQPz2uu_zI5ZB-QQ1DpwnhUKdyTbPNB8958Vi1YQsDRVw50uExwfgZ7RBqZ5z7OadriRDGaEBg3S1WWUsM3gjOE0j7I6IObwZ_WVIsl3eJ9sCteST0hWElXCXfxUqPRX7ljhDSIRehGH3VMY093bENStiwcquxr2BMqpzhp0SqifJN0sOp9cVorfM8_w4fQJKyxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رائفی پور آمریکایی ها ام استادیوم بوده مثل اینکه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/78462" target="_blank">📅 03:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78459">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">از وقتی یادم میاد موسلرا فوق العاده گلر کسشریه
چطوری نزدیک ۲ دهه گلر فیکس اروگوئه بوده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78459" target="_blank">📅 03:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78458">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">هم اکنون ریزش شدید فالوور های گلر کیپ ورد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/78458" target="_blank">📅 02:29 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78457">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">پس فردای شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/78457" target="_blank">📅 01:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78456">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZAS1OHOkdJ3twMyYAHyH_7B5VXfr_PnIy8PFfe8JzeeRttrH4QLyrdJAbHdgzdpk6q9KfCfwNtAe2JvIRy2xriPiqb3SvWgZAdEZUKZLF9wedImE1cR8PKsLygDo0OUg8HPS2XJ1UiUZ3VEG6ruMQQiEyVA44Uf3K3N_zuRVoQSGx0KSdYqNNZ1OIYE9q2q1sYK1p4Ko5cNVhqA2Ppc2NriNw7GN6_uhtQysEzcdRxw9L1mz4SbsmfXDTKUm3B7iLonrD7fCs2MsLCK4rk40H1xA7v6f57-c9e-fBKXgmSk_iwVCwWDcYlmErmYjMMgInDVlAOGSL5nIc7uzezqXIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و اما آخرین پست مربوط به فوتبال.
@FunHipHop
| Sogand</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/78456" target="_blank">📅 01:46 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78455">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">الان بیرانوند هی اینستاشو رفرش میکنه ببین فالووراش ده میلیون شدن یا نه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/78455" target="_blank">📅 01:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78454">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p5JkEZ4WHzwsZ1-iHF_bx-tkYcMSS6RMuJ9Nk8BXMrXX0tS8XdY6Vle3mWtRUlIBlq7hZ133FCTGnLjIPVlMweX7pb7bfBqlaw_AatR3uP4QhOoFN0FTUQZikWH_gKGS1PnZ3y-qAk4N8TqXTznoHptuWhNEmR9sSg1Yt77lyQvAx9a50CgU6H-ABOK7VmblsN5KMQaFzu2ExLN_xcDIirfVqDwWrHqTNprRNvz3mokEkRxZTJXxcKfXHUGVzoOPo4N9LA8u5iVYM8q5OLFisdFWLsUo1iBKNP-iDMgpIE6BhUgVpFbpmfqzmp1RN1UvtZiNPIP59wfOUUb32XflKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت جدید قالیشاه: ما اینطوری از کشورمون دفاع میکنیم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/78454" target="_blank">📅 01:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78453">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YmEVZX0b-xq2oheC-GkxFaelDT6jbd7TiHmqeBgfwU-2iv7219EsSdCrz2av2HJ_OufHZIR9iptlZp2LEsGODPttPEmkhrOHaYXmjwSSl_46jACjjMX7oVcxRBVqFhfY10wWIHG4QACb6RTwUSYg1dMikJ676X_MViLIeIL56-QAP70OA2ayYFoscEDsX5cgJ9Ui-el6bfxMbRtXxtYD6JEBYd550NStmCnoOXSnxXN-UWXtib5j3TmY5wclJxsTHUouAIEsC4r7meBON_7LceAFrbQJ3Vg0U_tArVN7gG8i3BSd75vo9o5EGVd3KmMRln7ubakz89CJS3aD2PyHJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهادت بده نویر
اعتراف کن بوفون
تایید کن کاسیاس
به راستی او بهترین دروازه بان تاریخ نیست؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/78453" target="_blank">📅 01:29 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78452">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">خب کصخل کورتوا هم نبود بلژیک گل خورده بود</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/78452" target="_blank">📅 01:24 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78451">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ولی جدای شوخی واقعا مساوی گرفتن از بلژیک ده نفره اونم با شیش تا دفاع و ی هافبک دفاعی کار خفنی نیست، اگه بیرانوند امشب رو دور نبود ممکن بود باز نتیجه ای مثل بازی انگلیس رقم بخوره.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/78451" target="_blank">📅 01:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78450">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ولی جدای شوخی واقعا مساوی گرفتن از بلژیک ده نفره اونم با شیش تا دفاع و ی هافبک دفاعی کار خفنی نیست، اگه بیرانوند امشب رو دور نبود ممکن بود باز نتیجه ای مثل بازی انگلیس رقم بخوره.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/78450" target="_blank">📅 01:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78449">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">خبرنگار خطاب به کنعانی: چجوری تونستید بلژیک رو متوقف کنید؟
کنعانی: رفتیم تو اتوووووبوووووث.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/78449" target="_blank">📅 01:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78448">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KA7krashHTa9OTH3qH0d7mDp83AcZ_mV3TqG1Gh7zuQ_HK8dKhUg_vpBpHPJMipgFvfiTr7cWEyfvYoQTgV_-aFeCiv3E4qXsPS94SZ5S4o01I5YlD9-bef_vM3jCZ4fyp6QYdv23SstiL9IQyBsasfu1SlhT8bvaB_u3uNLKcAgth2vHOjrZtiRgREDXYLcoh-Y9A6L-isS6HIw8rFm13jtXFKavPGc1IMYaoYCR1mN49i9Xa-UxiWHvn5Kbr6uJnj0ExkCwWf7p3SHswCjgO9gC3v3jfygULUUP7MkEQVAeqwoIq3KCL02hsUmUlaInyHKwBZ7gDuVFUDMX1TZCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا شوخیو بزاریم کنار کسمادر بقیه بهترین دروازه بان ایران ایشونه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/78448" target="_blank">📅 01:06 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78447">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JwzZLOB_bqZQHkR3GJmUCpyaxwQHdgCOlIrPHQybgOKylszxJik2fDH3qYz0rtmp7zJwfswp4Yk6idOTcBi8UOKM-dhsSxz9VA_32FTfQ2aFrCXN6M6kAo1PdnfkXYYDw-1vdkLKXpPTKor5j0vkAjw023SD86dZb-HYiHvrKPHHAhir9srJM7XLw06L-hogsJ8l1tdWRbMBflN_f8bx4zU1aRqp4xSHdJj5sJh3srhCzvFMuJciGPlbS8wKs4hq5tDeO8czWf5ZwzYG2Iyp2cslPKZV8RPyA4chqPdDQFjN9lnFS_ULj-BBxyI2GlYM9x3rdlnMVnKRg6HpfJrCOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یعنی الان بیرانوند قراره ۱۳ میلیون فالور بگیره؟</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78447" target="_blank">📅 01:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78446">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gu_bwrE3L4G1pC_fgsF8mo2f_k3XOrD0MTTDofw7YbPMpEGi0zWWmOvrr24OgwYqgR8iPOoGHJCW-8TK2mF0gzKVlKYmiScWNE5w15J9iXgG5ALm0R8-k_2VO-ad6n88HfnrY32VwTQuH4kiUKNT-ZLdI6OhymuXsW3C-0Xbtng96f2saxBmakLrLePfvhgkcbRfimpgus4zwiwLRdncGmTNoDY2d2hJNHzqo2zreUDu1MkWNmatRmavkD10Ulfk-0bxaKE-Ljnc9jZ9gwHJ0aZ4gI7nOdOcK4M5VPTp7ExvE9eyz6kfMPafMKP8qZAJ2etw3gbL6G7efEqMAGD4VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسخوش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/78446" target="_blank">📅 00:54 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78445">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8IIUr7DKjgLvzXZdr3wmXN2M4zzJV1DNIXHTxxi2XImF4Ycbc3zyRkAzbaYoXY6ILFWJDWB58pBk3KgB6ddPCI3o-u71jWgtgMO6bjcjD3iSQc_iGxDUwKP_O125rKlwv7uczF7wLDbRbXS3jxx7hY3Nn5IxlLu-j_9Trt_PZwPzk8PNna4l_JYuTDObyLpwkIP3Flj4XO-c-CqthPu6cOYRWSNoX6zqx_p58s-aZkBETCWlAc7JCcWQwAzYYBqbUqDTjOe7NQ75BdQWDmwz9UgEvydFxsHcP54Kvx2dCh7GB2aCuXYl9K2mbyCT8RyWgQLJC5W1Zxu2j0Hf3vSVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/78445" target="_blank">📅 00:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78444">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">نمره بیرانوندو  @FuunHipHop | Farid</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78444" target="_blank">📅 00:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78442">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b0kLCgjXLcZ_ZSh6PJAebGD8GBhGjgd0-hxoa69uIrV54vA1m6prq9P3OfC2j1a95SJzeeeAbyRZ2ysObhbIFk0UeP46LNv8quGKJWgFMt5iZyGGAKgG8G9RW2HBGeUjT5yNVR0KMUTcuHRUQYuBWvjvYOkvanG98LtunrCI9bRHjrf7xPskmkf33u4Op7dAYzKsyXKrJgxPVDcQNKY52R3AsIUf5a2-u94qyD4jTDgsc0b-A5RYMI41SePixflxNKCKk0Q23PfPGzVsH3en5MFEVLdRn5JRoV9GO1F3f2YZ6haQHcZV_C_IdUkS-XwyKXjm31Ogvx_SLsJTz2pLHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمره بیرانوندو
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/78442" target="_blank">📅 00:37 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78441">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">یعنی الان بیرانوند قراره ۱۳ میلیون فالور بگیره؟</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/78441" target="_blank">📅 00:33 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78434">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25a83c28b2.mp4?token=tOKnrTlcoG70zxQSNdw5M1X7QXCIUJGvkjJmAWxShbbxfcSvrxMkc0yC26OCYnRIry_wF4ob3PlI_7FynbTy2LhnpJet5FZWwxUUft6cdYMcKGhgubexiqg57hmw4HpJYJX43Dwx18_iLVCvg05eDSC99ZCDuVw_CRhkfbPpf4KgL09UClqoogA5xdVM95gGdBTNMMn9HGW6GdeEM2rzs27PXCpNSRKBzZD4J69CcRNqPuNISOwZvcywLP7oNpiRF_p1MfNzfSqvOD3uZsd2fNFk42kirMhh1IIxxhAWREwHdAUN9r26O7aca2Vx9KU4nY5bsfLCAXFWZgtKHXMGJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25a83c28b2.mp4?token=tOKnrTlcoG70zxQSNdw5M1X7QXCIUJGvkjJmAWxShbbxfcSvrxMkc0yC26OCYnRIry_wF4ob3PlI_7FynbTy2LhnpJet5FZWwxUUft6cdYMcKGhgubexiqg57hmw4HpJYJX43Dwx18_iLVCvg05eDSC99ZCDuVw_CRhkfbPpf4KgL09UClqoogA5xdVM95gGdBTNMMn9HGW6GdeEM2rzs27PXCpNSRKBzZD4J69CcRNqPuNISOwZvcywLP7oNpiRF_p1MfNzfSqvOD3uZsd2fNFk42kirMhh1IIxxhAWREwHdAUN9r26O7aca2Vx9KU4nY5bsfLCAXFWZgtKHXMGJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تاکتیک ژنرال برا بازی امروز
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/78434" target="_blank">📅 00:23 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78433">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">امریکا هم نمی تونه این تنگه رو باز بکنه</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/78433" target="_blank">📅 00:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78430">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d6215a59f.mp4?token=FOziYybCPeGQh1ql4fA_4kpNGNXLXQk5wC2DnfcwkAYUBVzbGIesiFgsNeJC_35AhbW-_R1rgZvGC8lm8z2ksq1a_xz7QiWFpLTYDQVO5CdD6IBzkuPnotfL9xgmPP0qC270VfHr3iHTyvMwSRoh6HFb9nfPtMEQNYyR2pJp6-MMP3gNLO_g4IVLPRugZ2um-3K2O1XWWjdtxdOVvtQKSgPaNZ2M7qDPhxYlebS5IN6rWzkuFtubrkKPjkD99giaKcBq4_rPgw1lRIAKzhcNq-3NZhktyTmA0NrALqorqoYUx3qeg0TLKlIhbY0dqlkqEyMsFUibRfyfAg4EZIjGKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d6215a59f.mp4?token=FOziYybCPeGQh1ql4fA_4kpNGNXLXQk5wC2DnfcwkAYUBVzbGIesiFgsNeJC_35AhbW-_R1rgZvGC8lm8z2ksq1a_xz7QiWFpLTYDQVO5CdD6IBzkuPnotfL9xgmPP0qC270VfHr3iHTyvMwSRoh6HFb9nfPtMEQNYyR2pJp6-MMP3gNLO_g4IVLPRugZ2um-3K2O1XWWjdtxdOVvtQKSgPaNZ2M7qDPhxYlebS5IN6rWzkuFtubrkKPjkD99giaKcBq4_rPgw1lRIAKzhcNq-3NZhktyTmA0NrALqorqoYUx3qeg0TLKlIhbY0dqlkqEyMsFUibRfyfAg4EZIjGKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سطح ایکیو اینو حاجی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/78430" target="_blank">📅 00:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78428">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">سیاه پوست فیکس میذاری همین میشه دیگه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/78428" target="_blank">📅 00:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78426">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">بلژیک اخراجی داد</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78426" target="_blank">📅 00:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78414">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eR-DNR9K1W046OwFv7YUdxgCgtttfNliwcMdqFeJ4g8OYDVUm6INnLsAoKkhFQ7lp-RH1x4EdfIk_F5_X9vbFGYwx4bih_4wVmv1A3reREmM_w1vQkM-svHlkNmiUbnIv9axKRFozGTSzl-9_ocO_QpsbAqX-DR0ZHkjR03-KCHTtbzO8rykzz--KBlmZypjDhr9MyuqpS7Vtqvz-jDieymiK4HRXf2kc4DyS3POFzEKqlG21IG0-CL8M6L8uo6vtpSTbWlrNVplXaOz_ASxRELxtrOKj2isJLzAljzbJKdGo7SZitlv0zvEKLF0pht6HPSlYXKQQyah8NP8ZX3BOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنر تماشاگر ایرانی
رشید مظاهری کجاست؟
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/78414" target="_blank">📅 23:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78412">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">گزارشگر آپارات اسپرتو فک کنم بازی تموم نشده بکنن تو گونی</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/78412" target="_blank">📅 23:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78410">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">دیبروینه سوپرگل میزنه و بلژیک میبره
بماند به یادگار
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78410" target="_blank">📅 23:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78407">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">عباس قانع راجب شیر و خورشید: پرچماشون فیک باشه ولی دلشون با تیم ملی باشه اوکیه</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/78407" target="_blank">📅 23:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78406">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">فوتبالو سیاسی نکنید دوستان</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/78406" target="_blank">📅 23:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78404">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">من کاملا فوتبالی از این تیم کیری بدم میاد</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/78404" target="_blank">📅 23:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78403">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">فوتبالو سیاسی نکنید دوستان</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/78403" target="_blank">📅 23:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78399">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">آفساید شه کون میدم   @FuunHipHop | Farid</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/78399" target="_blank">📅 22:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78397">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">آفساید شه کون میدم
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/78397" target="_blank">📅 22:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78392">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">گزارشگر آپارات اسپرتو فک کنم بازی تموم نشده بکنن تو گونی</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/78392" target="_blank">📅 22:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78390">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">گزارشگر آپارات اسپرتو فک کنم بازی تموم نشده بکنن تو گونی</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/78390" target="_blank">📅 22:47 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78385">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">بیرانوند همانند شهید تنگسیری ایستادگی کرد تا تنگه رو بسته نگه داره
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/78385" target="_blank">📅 22:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78382">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">بازی تیم مردمی بلژیک هم شروع شد
ببینیم چی میشه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78382" target="_blank">📅 22:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78381">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">نتانیاهو:
سال‌ها به ما می‌گفتند"نمی‌توانید به خاک ایران حمله کنید."
بله، می‌توانید عملیات‌های موساد انجام دهید. «ما هم عملیات‌های زیادی انجام دادیم، من هم تعداد زیادی را تایید کردم.» اما نمی‌توانید نیروی نظامی‌مان را به ایران بفرستید.
ما این را تغییر دادیم، ما خلبان‌های شجاع‌مان را به آسمان‌های ایران فرستادیم.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/78381" target="_blank">📅 22:16 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78377">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nv-p1MrhYImcYCu0tREMd1pS8M-p9NrJ0pVys1AAK1ptF0ZsOgF2geB8xAbDzVHXHQ69jtzj8OLmX7KpBFhHAaJNnjffsVTRN1CGgTt2TPRMQEAD1gbW61TDXuLXqGJnxPUo5WI7md_bfuRKy_zuGn__81i9EtgMuzQustQB7yUbmK_PvGr0R59zOmxq1uCTPWMqc3W2Uq469tCUu5A2AO7WGbvkf22AXzLXVUBdcRc6qKe85rSV67CwJd2ES-lqb-XJ5u_GaD_kFL9wU8zRoquzbClSQnY5YYK68Innvz_e9vk2C-3FsakwO6jsfSQAy_V_5StlIxu5qfvmyTJdIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/78377" target="_blank">📅 21:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78376">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">رو برد مساوی ایران بزنید پولدار شید</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/78376" target="_blank">📅 21:47 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78375">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mEbwglz7hQCEq-uneH9qIispbmEAMLDacvbc7okYP8tTmumYFqdOrVdesVo4k9PwXqnFHwVef0xxAaDs4h08Ju67lkS44x3vtwy8dLeLcR6gNXGGwIL0EwUplG9zQjrF23s2IE1yNq_YsB3gdY7cL9RQAnKIkFRyBbDJeLjvTQRhis22sH6YNayPf4Znc_TGkESXHHaE32k_irD2E57oY1XoYSCcns1jUDIL2HAJKiwj8e3rHU0ERxtfj4S8R31_zFQua76-SZKFAV9EvkamSSEdHz4sUeLlkfmMX0Xgvp58elxqP2d0QOU1oRM8XZsQA-PvC2ODtnXBqGdeaPBUeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ژنرال کاملا حجومی چیده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/78375" target="_blank">📅 21:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78373">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">امضا میکنم که نعمتی امشب بهترین بازیکن از نظر ما میشه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/78373" target="_blank">📅 21:02 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78372">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LIDKuxw4NGcESkVDLfgv5qvFoRQ-Bs60xWupVw2qzeD386mLYckjRbZw72O_kOjpTH1GF6wUzF5JFvWOVWaek7GuAoHpABr9GgI15DRMVmJ7IppQWga6LplzcEzB5vfQh9E0zyEoDqLOOS1HyxXrrC3CVWXeWf5BVQNChZ4ta2tf97ZyqDK7jFSOJflBwJ46NfpSycLqhVNUU7wrby7wIQkx1npXqpXd0L7Py3jGkqOgVpU_2vcYYO4WKX_03RAPYXEZKM4W9nUcc3q-4wqUbvJQctH7Ke92sJuyEHVwrbX0nFUyUvZ0uBfAIFqWwzlTEl7OOkDL6pvXPDwPpxnmAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب مادرجنده ها اومد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/78372" target="_blank">📅 21:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78371">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qhsUJ3VoM3_S9WYujYFkm73e1rCO4f0uLVEP8ABNEg3TNrNTwv3NcIZaFPh5V1ur94jcbuIPQPFbamRSdjZ0WHtRDEwL702r1LyfrKt8Ook15orO-9ibEG14zVGKmwRU48wbKppJc4sJ1Xs2gaeQHKPfxTS4RlysuKqfKUssaRVuCFvFHWWZluDHntLxu7b2-kB16alZIBm9DmqUJrRv8xB9ae_bLgR_12wbsz5QMXTf_QjKwr1CuWsUwxLP4QgpYYFjfYby5v9Y5F5aDO3sPWQCagoS8nyOtr1hOSQ8PDINO6I188ucVKq6RduKGFpguJ7939ntscOrsZtbdM8hEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محرم ۴۰۵
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/78371" target="_blank">📅 20:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78370">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca8a4c0df7.mp4?token=Hs7LBxgNG1s2BiomUzZMyBm7O7cuoSLe5qupnLINogKambfFYbijiO_Rw5jrINw3e_YOx9C1tEuLt3X_7Qxn_cMfK2Bb_f7TKOXkqBGrSZgm5gWaPIZPbMhWNzGsSKhKdXqGOi_Rw4hH4LUgejUUVBMuvjuTgfKMJT81Rma236rF7HLeDsLvZCgobWQDzLTwi-DYnNyht5Rusybl3wJPR2NiOhUjHDJXJ0PD94VFo5r7g7Gr62wyJRbwK01vDDrwlKLmwWLe9zH-F_6CwZ1X42jbLXdtdbiCQfWgCU8JFrDarXBL33WfjHp6Ww96axw2leUl1bIkOoIe9R6RN5qfbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca8a4c0df7.mp4?token=Hs7LBxgNG1s2BiomUzZMyBm7O7cuoSLe5qupnLINogKambfFYbijiO_Rw5jrINw3e_YOx9C1tEuLt3X_7Qxn_cMfK2Bb_f7TKOXkqBGrSZgm5gWaPIZPbMhWNzGsSKhKdXqGOi_Rw4hH4LUgejUUVBMuvjuTgfKMJT81Rma236rF7HLeDsLvZCgobWQDzLTwi-DYnNyht5Rusybl3wJPR2NiOhUjHDJXJ0PD94VFo5r7g7Gr62wyJRbwK01vDDrwlKLmwWLe9zH-F_6CwZ1X42jbLXdtdbiCQfWgCU8JFrDarXBL33WfjHp6Ww96axw2leUl1bIkOoIe9R6RN5qfbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهدی رو برد یه تیم میبنده
بازیکنای تیم مقابل روز مسابقه:
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/78370" target="_blank">📅 20:35 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78368">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ریدم قالیباف: تهدید های ترامپ بکیرمونم نیست  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/78368" target="_blank">📅 20:16 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78367">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">اویارزابال هم که به یامال  ایرانی پاس گل داد اصالتا اهل هراته و ریشه ی ایران باستان داره
هرات استان خونی خاکی ماست و به زودی به خاک مقدس ایران برمیگرده مثل اربیل و سلیمانیه و …
دو ایرانی اصیل کارو برای اسپانیایی های آریایی درآوردن
برادر برای برادر
❤️</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/78367" target="_blank">📅 20:06 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78365">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">آرژانتین به عربستان باخت و قهرمان شد
ولی اسپانیا داره به عربستان تجاوز میکنه
ینی قهرمانی اسپانیا منتفی شد ؟
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/78365" target="_blank">📅 20:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78363">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">مهد اسلام داره فرو میپاشه</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/78363" target="_blank">📅 19:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78362">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s-3N4HAVpsw6EjrJlf9iEEOoLFAg6aYOdyn1zDVNyKEnebeRiV3krfTTRZLI1djp2KKvRma3DOuPGM13Frjr96HvIXCst-0TKBOsdHNY2RofTDe0b4U01yFKmYJhHzMiiM-ZFteNp2LXuXlvNLtyOQO_b5YwZTZyiULzEe2KfxNXBXShoJVAYx3Z-HuTvWNbnizRLsuTMyQ1GLv8JQM02ltxvloDb-1Db7SF1QkZcRe1hIwufk9Bm0E3-UU0Powrbz48zibJNkmHpzZpMxnNiSpP5WNZOnt1xt8GpJIG9yI8Cv-1UOpPiKzvE8rN8EpXTeBxI0FdIw7-Uqj4zEa7UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ریدم
قالیباف: تهدید های ترامپ بکیرمونم نیست
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/78362" target="_blank">📅 19:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78359">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">نتانیاهو: تا هرزمان که لازم باشه برای حفظ شمال اسرائیل توی منطقه(جنوب لبنان) میمونیم و همچنین اجازه نمیدم جمهوری اسلامی به سلاح هسته‌ای دست پیدا کنه.
ما از جنوب لبنان عقب نشینی نخواهیم کرد و هیچکس نمیتونه اینو تغییر بده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/78359" target="_blank">📅 19:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78358">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
عباس بیا بگو چیکار کردی چه سوپرایزی برامون داری از مذاکرات
ترامپ به فاکس نیوز:
شاید کنترل تنگه هرمز را بدست بیاوریم.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/78358" target="_blank">📅 19:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78357">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">کونکشا دیگه زمستونم که مدرسه و دانشگاه نرفتید، دیگه دلیلتون برا تابستون فن بودن چیه ناموسا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/78357" target="_blank">📅 19:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78356">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">اووووو رامین رضاییان
🗣
🗣</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/78356" target="_blank">📅 19:02 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78355">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U7Y5FNdR_-WjSAvCyRbv4MczNXFWgsk1FXwOxJPDB1z7gYokMkftiJjmmpAq9M0mEM3wJlzDSkXtkqFDyu874eiek8Q42baFRWjuRMMlEuO1HDX4VRwF3idjPAMSr1r6l6OwTNW7w60Ned1sOhkDmAyI4oHC6KYdIod8LarFM4QB3zeDGSdXb9Fvifj7yKm8qki7Xm6AyDWRv3fg3JodnCbpAzlKmJ7M7tFN0CHkoJJk_48iADM-cNGi7No2fs_AzvD1IcHeoDc-3DRtopxkU8KJ2aO9wiCkrbmjE4xmnOq4_DmGpujfmqQP7-BbR0NvLkjN8rb8vPoBnv9DXX7oHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیده شده در بازی آمریکا و استرالیا
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/78355" target="_blank">📅 18:58 · 31 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
