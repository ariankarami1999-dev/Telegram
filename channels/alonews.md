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
<img src="https://cdn4.telesco.pe/file/GH370c3CoXfxxNOC_9z81wb50K6ayQ_3evKGfxtXiDv1_rvqF-b45Yp-8xjtB9z0ruJAaI_DXJzQ6eMQ17ZkyaSyaWwhkgDuOD5fM7wjVsDJbyampl6_ofJUxN1Le77qIgppXOXodv5EYvJ9iRqztQKo8fQ_QGb_y9ZG0468Ysn-5pz78RGerWQyZGEsyIOZT1HzQjeSWt5fgXcUMUNixH-QgoPuDbwfHcuf3cc_GjdtQg2TcXJudnGiKqmwH8s5lkFIg41KqgDktoxHjiAV7nvRjKt6klU0k5nMk24fo1qYnVq0-GJ6IZdMFVUbtVvvG_4QOcJ-YEtKS_RjIumGtA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 946K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌پشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotجهت رزرو تبلیغات👇https://t.me/ads_alonewshttps://t.me/ads_alonews</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-30 17:31:58</div>
<hr>

<div class="tg-post" id="msg-121323">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43f6765942.mp4?token=iixAwdI_qkyrNlAGt80QIt5a1ReEGioeSzHtrIEMaBuE3LaOOIDm_T-3nZVpoi1GSnBogZiVN6jhBYGNC8MoGIVQTaSlo7ELWeaE9xz1cCdY89W_vQnHtCDAWkvYh5wtp86qqylLLKKDLeWf-Mrl8cLKKticTVrIzf6qcPpqbaVo3iFZ8d185okJVyWJJZEIZQspw3fuHwRYWRMLCK99WvmHFK0IIgI-Xr5jSSTCHvJQi_Kw2gv-0YTxnZpW4qYhGicq0v-X85lRpXajWLFhuBPg4YTjscclE5OFIKBgoqy_Gan4m2U65K6-vw_iQUPB48N_kNpbUDRlhOH5B5OmhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43f6765942.mp4?token=iixAwdI_qkyrNlAGt80QIt5a1ReEGioeSzHtrIEMaBuE3LaOOIDm_T-3nZVpoi1GSnBogZiVN6jhBYGNC8MoGIVQTaSlo7ELWeaE9xz1cCdY89W_vQnHtCDAWkvYh5wtp86qqylLLKKDLeWf-Mrl8cLKKticTVrIzf6qcPpqbaVo3iFZ8d185okJVyWJJZEIZQspw3fuHwRYWRMLCK99WvmHFK0IIgI-Xr5jSSTCHvJQi_Kw2gv-0YTxnZpW4qYhGicq0v-X85lRpXajWLFhuBPg4YTjscclE5OFIKBgoqy_Gan4m2U65K6-vw_iQUPB48N_kNpbUDRlhOH5B5OmhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره خودش:
شما در نهایت خواهید گفت: «او بزرگترین رئیس‌جمهوری است که زندگی کرده است.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/alonews/121323" target="_blank">📅 17:27 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121322">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/753b6e158c.mp4?token=uXf3Xs4rMNiHTi0kgGBlFmPFkNLErxI-j4QZ-A1ivXeBzkOHSaazp7DtAjvuzQcIIRAkt8FLDYEyRXz-GDw9mkRQHpJLt6xYPYXkQ3w9MPVjJdCaK7eV39HhR8l69DWxR72VNIH2nxWheDBf1wYpM9AsQy-2HQ2quzHvnj-BWXFXGup5HLEl6nl5bqEdO1ErmlR7VMwwjFt3_TN-xEmj1oEQXh9Xhl_dsCzgSHEYI3QjHZt0y0bHA_Nwa3uvudKv9sZwaUhlABCv53TNlWHAak1M17bqEBdnmH5yp0IZ2rf9apv2RsaE_w5f0Cus0jCFVS7tSGxFet56nh3FctCps4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/753b6e158c.mp4?token=uXf3Xs4rMNiHTi0kgGBlFmPFkNLErxI-j4QZ-A1ivXeBzkOHSaazp7DtAjvuzQcIIRAkt8FLDYEyRXz-GDw9mkRQHpJLt6xYPYXkQ3w9MPVjJdCaK7eV39HhR8l69DWxR72VNIH2nxWheDBf1wYpM9AsQy-2HQ2quzHvnj-BWXFXGup5HLEl6nl5bqEdO1ErmlR7VMwwjFt3_TN-xEmj1oEQXh9Xhl_dsCzgSHEYI3QjHZt0y0bHA_Nwa3uvudKv9sZwaUhlABCv53TNlWHAak1M17bqEBdnmH5yp0IZ2rf9apv2RsaE_w5f0Cus0jCFVS7tSGxFet56nh3FctCps4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ: «در اسرائیل، میزان محبوبیت من ۹۹ درصد است. شاید به اسرائیل بروم و برای نخست وزیری نامزد شوم.».
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/alonews/121322" target="_blank">📅 17:25 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121321">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
ترامپ: رژیم ایران رو عوض کردم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/alonews/121321" target="_blank">📅 17:22 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121320">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12ab0a1951.mp4?token=XeST0lQWu3rUHyEkg1WmOOMEl2KeprNI5nyoPwgJvnbLRUu_xQvwa7lE9utYp1keHwkt3S7n0cEQrtGxHSKGjEalisS09-RnFV2WDRQN5rhTeEgFjQpvyv5yZIqirpEruSsnAT6s6wCsaRVXCs-EuhMtcjrva-mvm-2_VApnVG_5NLLOrDe1o1fHhIfG1toZfOARh2jiPxATWlcQBbxR9vcirmu_N-2Im97ukxkljj6g004KTHVSgzHOmoRMgojaO4oQDZhyyQoJJNn73gU8XQyu-C5cTuddA2xAK0Y_XtDfcYIjwEUNSN0FlILhXnZG5Iuq9bXw9rWHaTwh-P5GBZIgcDkx5DysZlCQ1CrKGN2HVxPknPINkAUyYtIFU3bbDOj1FqOz_VbVmqoTfOzMdFQ_E8W_VDPzDpdy8P872Tpt9i_u1WaBXXtaUw7Ei-rlgrWS5siafzwwsToF4NfshV1wWYlrYXflTsaF_5x1NDbOF8vSCjZ4vVQTPzs4xS2Nw6F8hxPiMN754trlO1fWPn8wUlRIbbeHkR6YvUIPjQVLBeSSp4YKI7ufHK5GRkoZmOuSLzaJ_c0d8p5lpzQ866noqaUU79D_dAXxNNHZJwfnweOnmXr3adD3HWE7NegH8JGJZ7ICQphqX2z7hqjJakFuxzA-Q0n4PveUOHHyZDY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12ab0a1951.mp4?token=XeST0lQWu3rUHyEkg1WmOOMEl2KeprNI5nyoPwgJvnbLRUu_xQvwa7lE9utYp1keHwkt3S7n0cEQrtGxHSKGjEalisS09-RnFV2WDRQN5rhTeEgFjQpvyv5yZIqirpEruSsnAT6s6wCsaRVXCs-EuhMtcjrva-mvm-2_VApnVG_5NLLOrDe1o1fHhIfG1toZfOARh2jiPxATWlcQBbxR9vcirmu_N-2Im97ukxkljj6g004KTHVSgzHOmoRMgojaO4oQDZhyyQoJJNn73gU8XQyu-C5cTuddA2xAK0Y_XtDfcYIjwEUNSN0FlILhXnZG5Iuq9bXw9rWHaTwh-P5GBZIgcDkx5DysZlCQ1CrKGN2HVxPknPINkAUyYtIFU3bbDOj1FqOz_VbVmqoTfOzMdFQ_E8W_VDPzDpdy8P872Tpt9i_u1WaBXXtaUw7Ei-rlgrWS5siafzwwsToF4NfshV1wWYlrYXflTsaF_5x1NDbOF8vSCjZ4vVQTPzs4xS2Nw6F8hxPiMN754trlO1fWPn8wUlRIbbeHkR6YvUIPjQVLBeSSp4YKI7ufHK5GRkoZmOuSLzaJ_c0d8p5lpzQ866noqaUU79D_dAXxNNHZJwfnweOnmXr3adD3HWE7NegH8JGJZ7ICQphqX2z7hqjJakFuxzA-Q0n4PveUOHHyZDY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار : درباره جنگ ایران چی میگید؟
🔴
ترامپ : بذار اینجوری بگم شما تو ویتنام ۱۹ سال بودید،جنگ جهانی دوم ۴ سال بود
- من ۳ ماهه درگیرم، خیلیاش هم آتش‌بس بوده. تو دو جنگ،ونزوئلا و اینجا، ما ۱۳ نفر از دست دادیم
- تو جنگ‌های دیگه صدها هزار نفر کشته دادید. ما عملاً ونزوئلا رو گرفتیم تقریباً هم ایران رو گرفتیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/alonews/121320" target="_blank">📅 17:21 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121319">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
ترامپ: به ایران فرصت میدم فکر کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/alonews/121319" target="_blank">📅 17:20 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121318">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
ترامپ: اگر عیسی مسیح پایین می آمد و رای ها را می شمرد ، من در کالیفرنیا برنده می شدم اما این یک انتخابات تقلبی است.‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/alonews/121318" target="_blank">📅 17:19 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121317">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
ترامپ: وقتی پرونده ایران را مطالعه می‌کنم اصلا به انتخابات میان دوره‌ای فکر نمی‌کنم و برای رسیدن به توافق عجله ندارم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/alonews/121317" target="_blank">📅 17:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121316">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
ترامپ: امروز خشم زیادی در ایران وجود دارد زیرا استاندارد زندگی بد است‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/alonews/121316" target="_blank">📅 17:16 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121315">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
فوری/ترامپ: برا جنگ عجله ندارم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/alonews/121315" target="_blank">📅 17:14 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121314">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
ترامپ: نتانیاهو کاری را که از او میخواهم انجام خواهد داد‌‌
🔴
من و نتانیاهو درباره ایران توافق داریم‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/alonews/121314" target="_blank">📅 17:11 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121313">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b6fdf71ef.mp4?token=Kvk5zumhzAP4QpEuxFw9cORQc46TROk6m88QLPZt34VRD4FB2fFz4RcbLilS2r_Ahz15Yt5_xm-rAMLn4sy0N7t3HSfmZL-YG1ybnikTQUzOVQJ5zLUnXFbPzneSDjAXCTUgumNG-CaarbSvuMw2XVixyc0LrWrYWUo00h_IOxvBSIBXwcpzBIZnyMZuQaSsHyJD1Yolj4ESV21b72k0w20jOXvtwdkxOTrHohN9v2oCBWDNFSNjSC--sEX14AXSakiwSubFX-y8nJ6tKxB_c2a7ORq-12NfwcuYzqboygiXz2AVwi4qJEkV8R-J7xHyue0l7WxCuwSMW-HBo03kaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b6fdf71ef.mp4?token=Kvk5zumhzAP4QpEuxFw9cORQc46TROk6m88QLPZt34VRD4FB2fFz4RcbLilS2r_Ahz15Yt5_xm-rAMLn4sy0N7t3HSfmZL-YG1ybnikTQUzOVQJ5zLUnXFbPzneSDjAXCTUgumNG-CaarbSvuMw2XVixyc0LrWrYWUo00h_IOxvBSIBXwcpzBIZnyMZuQaSsHyJD1Yolj4ESV21b72k0w20jOXvtwdkxOTrHohN9v2oCBWDNFSNjSC--sEX14AXSakiwSubFX-y8nJ6tKxB_c2a7ORq-12NfwcuYzqboygiXz2AVwi4qJEkV8R-J7xHyue0l7WxCuwSMW-HBo03kaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تسنیم تصاویری از حمله پهپادی به یک نفتکش منتشر کرد که سعی داشت بدون هماهنگی با مقامات ایرانی از تنگه هرمز عبور کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/alonews/121313" target="_blank">📅 17:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121312">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
دوستان ما در پیام رسان‌های داخلی هیچ کانالی نداریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/alonews/121312" target="_blank">📅 17:04 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121311">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9AkjOft93HmykOY-0Gr6iK92RjxHJx4NrMXZHcyj25ASR-gF7ADWqffywIkDX53wndwIWTumgkGqWpX_lvU87IlPmNWEFeVsLqhE6edM7yk751fxpYOhtawFg-XTNUmvi9S24WxH704ThZGWwRXKvwQ_INpO_rApVPIXxZqULFQ48qxUL-o4sbFHxHBqF8o_dZWp4Pi8gZVNBmzIjeP4H4FDW7wNPMg7aT3IanmuB1KTHj-uw63Y6Pyv5_ZRlMk_uKzXXOQq-uvPz7QBcG8Dp8ZDMx6G2biqATItWB37WKPvZE43BVDYo3Amt6J3Gtdsmo24M3qH7kWAQxZnkW4ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف: آمریکا دوباره در جنگی بی‌پایان که در آن امکان پیروزی ندارد گیر خواهد افتاد
رئیس مجلس در حساب کاربری خود در شبکهٔ ایکس، عبارتی از فصل ۱۱ کتاب خاطرات ونس، معاون اول رئیس جمهوری آمریکا نقل کرد:
🔴
«ما احساس می‌کردیم در دو جنگ بی‌پایان و بدون امکان برد گیر افتاده‌ایم و سهم نامتناسبی از سربازان از محله خودمان (محله فقرا) آمده بود.»
🔴
این وضعیت (گیر افتادن آمریکا در جنگی که نمی‌توانند ببرند) دوباره در حال تکرار شدن است. این بار فقرا و فراموش‌شدگان آمریکایی باید هزینهٔ جنگ‌افروزی الیگارش‌های نزدیک به کاخ سفید، افراد شیطان‌صفتی همچون جیمی دیمون و لابی تاجران جنگ در واشینگتن را بپردازند.
🔴
گفتنی است جیمی دیمون مدیرعامل موسسه مالی و بانک جی‌پی مورگان در آمریکا و از مهم‌ترین چهره‌های حلقهٔ تامین‌کنندگان مالی جنگ علیه ایران است که اخیرا نیز علیه کشورمان لفاظی کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/alonews/121311" target="_blank">📅 16:57 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121310">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bhL_cW9WSTETIPhmDVPTrUDxYPxOeP4wSWMDgoMYomXGlAzL-wABMUtEzTyzXPeYyhs83rYj27zrXlJBge6ZKYE2CJ3sL_WeSJxiPsztuu42uyit65GGf54zfqMzQIWaAZklidPIU5wO6FQb9jDzKEBMXzQ16VyddwLtEGQ6RXq15LDzK7VwNYWyF2qa6Fp5KmoRF3L1ZFmimsb0nA1XRh5fNj1MxpffCNADr8dQN8FtTWe6mZD3aN123ukq1LDtrZb10HdnysCOO2aQRqhBAc9DYEN7m0R3KGNcKli9zF4N8SBKKFpmGoMs6Cg2MfK8CdvjAc_m1biAYWY7NaBCHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله
بنی گور وزیر امنیت ملی اسرائیل به گیدعون ساعر وزیر خارجه:
برخی در دولت هنوز متوجه نشده‌اند که چگونه باید با طرفداران تروریسم رفتار کنند.
انتظار می‌رود وزیر خارجه اسرائیل درک کند که اسرائیل دیگر کشوری نیست که به راحتی تحت فشار قرار گیرد.
هر کس برای حمایت از تروریسم و هم‌سویی با حماس به سرزمین ما بیاید، کتک خواهد خورد و ما دیگر لایه‌ی دیگر صورت خود را به روی او نخواهیم چرخاند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/alonews/121310" target="_blank">📅 16:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121309">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/urCFY1X45udA7es1d8dD164R2cpO-vLKYzVCYuXfBD2a3br6q8VJT9vNvZA6E5IQhR788WjuUvnc5lgcNjTgzw40MA-O_skSpoCGp8DEkWg_FWQjChKUiO3urlD20-OlWSBl9wShTX5phaWSu9r2cL5GK0x2Ts8qfFLeaxCwS1Bzzx1DKXjd4vwMwfED8r8z6Zqwo0iv_Xj9K4xA4gAtl_p1iURq3C9G_SKYGcWR3fdvEHEIQ3EIHx6aTSPCWHKRwYsk-N4gFjYbibu-PCiFPrZPGIcfdDfqzjOMSJjGNFY3TAOU_jhlL4zVkxAH_kBEGJ9Ch_fEsRAcP-rz7bu9hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
درگیری بین وزرای اسرائیلی به فضای مجازی کشیده شد
‼️
🔴
وزیر امور خارجه اسرائیل، گیدئون ساعر، به بن-گیور:
به عمد به کشورمان در این نمایش ننگین آسیب رساندید - و این اولین بار نیست.
شما تلاش‌های عظیم، حرفه‌ای و موفق بسیاری از افراد را خنثی کرده‌اید — از سربازان ارتش اسرائیل تا کارکنان وزارت امور خارجه و بسیاری دیگر.
خیر، شما چهره اسرائیل نیستید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/alonews/121309" target="_blank">📅 16:44 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121308">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24468a4f6c.mp4?token=QVV6Z6FVnkZmyNBznspRqmmPZ-RTahPLSbxfxwqZme8VLyMQn_ajnb7BxWIdq_8Szw8Mk0R8ORcKXgMtxxRoRE8TbziQWDo6XwSOT5qpKGIVwZic44JFghLX0gtPeq8LqeXz_cJ2sKaSmucRi0pcs0uJhRkBuEoJY8jVv6MF5DxwjQjfvSRGFSyDCLXjom8MRzLt8QhUG2FihMYq43okTSak4vsuJTf-GVvOcpjD-KU0ZEetgxsRs9RSzonHS6F1IULFqfw-73612AF4RDklZk8lwIWOuJ5wpATKKVen5xkn50I0k2gHITKsMhJp6IQCOGV3V93wdbgxdMGeuD9qSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24468a4f6c.mp4?token=QVV6Z6FVnkZmyNBznspRqmmPZ-RTahPLSbxfxwqZme8VLyMQn_ajnb7BxWIdq_8Szw8Mk0R8ORcKXgMtxxRoRE8TbziQWDo6XwSOT5qpKGIVwZic44JFghLX0gtPeq8LqeXz_cJ2sKaSmucRi0pcs0uJhRkBuEoJY8jVv6MF5DxwjQjfvSRGFSyDCLXjom8MRzLt8QhUG2FihMYq43okTSak4vsuJTf-GVvOcpjD-KU0ZEetgxsRs9RSzonHS6F1IULFqfw-73612AF4RDklZk8lwIWOuJ5wpATKKVen5xkn50I0k2gHITKsMhJp6IQCOGV3V93wdbgxdMGeuD9qSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ممدجواد ظریف:
بر دهان مستکبران خواهیم کوبید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/alonews/121308" target="_blank">📅 16:42 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121307">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
تخفیف خفن فلش‌نت فقط به مدت ۵ ساعت!
⏰
از همین الان تا ۵ ساعت آینده،   تمام سرویس‌های ربات با قیمت ویژه هر گیگ فقط ۹۰ هزار تومان ارائه می‌شوند.
🎉
هدیه ویژه به مناسبت رسیدن خانواده فلش‌نت به ۲۲۵ هزار نفر
💎
۵ گیگابایت — ۶۵۰ هزار تومان
💎
۱۰ گیگابایت — ۹۰۰…</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/alonews/121307" target="_blank">📅 16:31 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121306">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
تخفیف خفن فلش‌نت فقط به مدت ۵ ساعت!
⏰
از همین الان تا ۵ ساعت آینده،
تمام سرویس‌های ربات با قیمت ویژه هر گیگ فقط ۹۰ هزار تومان ارائه می‌شوند.
🎉
هدیه ویژه به مناسبت رسیدن خانواده فلش‌نت به ۲۲۵ هزار نفر
💎
۵ گیگابایت — ۶۵۰ هزار تومان
💎
۱۰ گیگابایت — ۹۰۰ هزار تومان
💎
۵۰ گیگابایت — ۴ میلیون و ۵۰۰ هزار تومان
⚡️
فرصت محدود و تعداد سرویس‌ها محدود است.
🤖
همین حالا از طریق ربات فلش‌نت خرید خود را انجام دهید قبل از اینکه تخفیف به پایان برسد!
🙏
تیم فلش نت
@Flashnetofferbot</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/alonews/121306" target="_blank">📅 16:30 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121305">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
مارکو روبیو، وزیر خارجه آمریکا، رفت رو مخ حکومت کوبا و گفت وقتشه یه فصل جدید با مردم کوبا شروع بشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/alonews/121305" target="_blank">📅 16:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121304">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23b55e5d1e.mp4?token=CJ4HMJTvitUmhv6v5VLNXIlgnisXXA1lBTZEOKE3IOJ7-xn0ZBVYuOdrRKuWDir1q5pSRpzlk0xpvA5jnwBpGHGFfCA4YGOaLIhO6FWpkHqUQvNOzNXBppFpZFmDyIfx6K5hm848lZiHdheORK4t6f8Pig50Z0cGy-mqPT24AwTjr8B8MR3Jgc_KEY2bhj6yt-c0ug4M8Qr4EWSVRU0RRpd07Pb6D1FKBA7LlZ7VmK9cSRCcSlPr0Ts_f9NYsLybKv--WCQEzz14_p8rhTutuMwenwF491-UZmmZ-6cT5OSXxYeSFbgYymntcAHZEA8-h6z7ybjDZbNI1DC9zTIORQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23b55e5d1e.mp4?token=CJ4HMJTvitUmhv6v5VLNXIlgnisXXA1lBTZEOKE3IOJ7-xn0ZBVYuOdrRKuWDir1q5pSRpzlk0xpvA5jnwBpGHGFfCA4YGOaLIhO6FWpkHqUQvNOzNXBppFpZFmDyIfx6K5hm848lZiHdheORK4t6f8Pig50Z0cGy-mqPT24AwTjr8B8MR3Jgc_KEY2bhj6yt-c0ug4M8Qr4EWSVRU0RRpd07Pb6D1FKBA7LlZ7VmK9cSRCcSlPr0Ts_f9NYsLybKv--WCQEzz14_p8rhTutuMwenwF491-UZmmZ-6cT5OSXxYeSFbgYymntcAHZEA8-h6z7ybjDZbNI1DC9zTIORQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دبیرکل ناتو: روسیه میداند استفاده از سلاح هسته‌ای واکنشی ویرانگر خواهد داشت
🔴
مارک روته، دبیرکل ناتو، در پاسخ به سوالی درباره احتمال استفاده روسیه از سلاح هسته‌ای در جنگ اوکراین گفت: «آنها میدانند اگر چنین اتفاقی بیفتد، واکنش ویرانگر خواهد بود.»
روته جزئیات بیشتری درباره نوع واکنش احتمالی ارائه نکرد، اما این اظهارات در ادامه هشدارهای مکرر ناتو و کشورهای غربی درباره پیامدهای استفاده از سلاح هسته‌ای مطرح شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/alonews/121304" target="_blank">📅 16:23 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121303">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/612df8d7aa.mp4?token=vJfKzt_NUM-PrSMpFehYzEI_JtujhChiMwvm8jh6Go9Tm6bWZOhEC8ovNJhPgaSr2GK25qcJWCsjmhkTTM-NqcKTMr50SgUYwZVNUkVhMrUbwx9mUjwb6Ckyg6FS_QYwjmYZ5_LnAhCbs7Sf6nMOTpszBzBl8PLET34w-OVMmyA092txAMvKM3gU_Xp2iGdI-7xUhL5rv5U-VA1D1ohFUMBld5Tka3dNvVVI-6kh0majimMr718jCwWKnjiXRIKYrnb_bzK8OUuKiTxpH9d_SFp1reE4jDoUnbgCSBJrx97hZB2dKEB2kxW7l219K0eiemaI8OGhB6MFoH1p_QCaIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/612df8d7aa.mp4?token=vJfKzt_NUM-PrSMpFehYzEI_JtujhChiMwvm8jh6Go9Tm6bWZOhEC8ovNJhPgaSr2GK25qcJWCsjmhkTTM-NqcKTMr50SgUYwZVNUkVhMrUbwx9mUjwb6Ckyg6FS_QYwjmYZ5_LnAhCbs7Sf6nMOTpszBzBl8PLET34w-OVMmyA092txAMvKM3gU_Xp2iGdI-7xUhL5rv5U-VA1D1ohFUMBld5Tka3dNvVVI-6kh0majimMr718jCwWKnjiXRIKYrnb_bzK8OUuKiTxpH9d_SFp1reE4jDoUnbgCSBJrx97hZB2dKEB2kxW7l219K0eiemaI8OGhB6MFoH1p_QCaIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دبیرکل ناتو: وابستگی بیش از حد اروپا به آمریکا پایدار نیست
مارک روته، دبیرکل ناتو، اعلام کرد اروپا به همراه بریتانیا، ترکیه و نروژ بیش از ۵۰۰ میلیون نفر جمعیت دارد، در حالی که روسیه حدود ۱۲۰ تا ۱۴۰ میلیون نفر جمعیت دارد.
او گفت با این حال، اروپا همچنان برای دفاع از خود در برابر روسیه بیش از حد به آمریکا وابسته است؛ کشوری با حدود ۳۵۰ میلیون نفر جمعیت که نقش اصلی در تامین امنیت ناتو را بر عهده دارد.
روته تاکید کرد: «این وضعیت در بلندمدت پایدار نیست.»
تحلیل: اظهارات دبیرکل ناتو در شرایطی مطرح میشود که جنگ اوکراین و احتمال کاهش حضور نظامی آمریکا در اروپا، بحث درباره تقویت توان دفاعی مستقل اروپا را دوباره پررنگ کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/alonews/121303" target="_blank">📅 16:19 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121302">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m-uTUsYuRoHHhtD5DHJ3n50Yoa5r9U579kM4nFTiRuZ8oXHt0Ut9sRfTxKqAGqv8Qj6Z3uwZ7-Ex1TQLzeDcpr7u0U5X3rUp0cY9CdbunBTNW8lKtR5g_4s6ZbBdqjWl7xpMT3sEmYtEca_u_H7Ep5lz8oHdk76BpNnU2Sn_FQ-Xr9sJEmtmueZhl0F8pEOODWWYUPc4QDDn56amREp2k4NJvURH8I877uRNwXhyxuSvT0zpKDY6H8GPMTDLYU6Q4CAipe4hmS42XgFfEsdC5YMco9R0B1HYo3l9xFEjKKFxszvesYn2hiH-HY6MfOy9_ThWCAyANJCCFmF_6pAQMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بن‌گیور، وزیر امنیت ملی اسرائیل، از فعالان بازداشت‌شده در کاروان جهانی صمود غزه در بندر آشدود بازدید کرد.
🔴
به اسرائیل خوش آمدید، ما اینجا در کنترل هستیم. این همان چیزی است که باید باشد.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/alonews/121302" target="_blank">📅 16:17 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121301">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sKj44UEYNYMlQI-1n6DEr5nNQrtEECU3dXn_fKhEGiWCuFy2eN6NsYWc65uKxlbpW0MEBFz61VSbmlit4s90lhzJkQTiXM0GedjF2gJxD6tdpBZcGK7GGGhcrVgLzDoGYHcuF5qW2a-mx0bkdnaxWESw4yxygFbki1zJ5GnySCEMj48Fm1y0PDFWHdmYOhwNGnircUSX_ssM2hv_l7eVGCZB7vJearXsvKfR1IqRjZfLryCVfqptfyL7_qe96n82HACx2yQ3opAVZme-IV3qEv9aqhNxWCqHYwx1LIGv-99d8E6aFok_L7ee9GpTHLkieeK4qzkKZ7c5zDfI6PKi3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یه خانواده پاکستانی اسم 2 پسر دوقلوی تازه متولدشون رو "علی خامنه‌ای" و "علی لاریجانی" گذاشتن.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/alonews/121301" target="_blank">📅 16:13 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121300">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a2668c9eb.mp4?token=XudHcyQ4lgOPOBjz3GDBY3n-suV6oKvxxNhT-w0MXZ7l_xNt6CnYIne7-LZeM6O5KofHjshdX9zj24bG34wfa--hwPuMDcJUnLm9apApU-wnWvnlTHLypP03U2jTgOrCn_5R8zgsh8O9LkrGRzzQ9EqtrPvmS-zI2YIdPBW5dv0XRa-M7-Hjwc-oetQw-ISGE_k3mR_rDPvxirERz6lOkCMh5aacjRZRImFIeXUhO9pAWPp64-nOsXtwxM0J6cSg5w6IN11HyvyuJ59Gf5F-Nfbg4r_sW22cw6SSikffcPCtYiUXSzlJCGT_ipVppAZP6CKnqM_tF1vB9_NLH7sKBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a2668c9eb.mp4?token=XudHcyQ4lgOPOBjz3GDBY3n-suV6oKvxxNhT-w0MXZ7l_xNt6CnYIne7-LZeM6O5KofHjshdX9zj24bG34wfa--hwPuMDcJUnLm9apApU-wnWvnlTHLypP03U2jTgOrCn_5R8zgsh8O9LkrGRzzQ9EqtrPvmS-zI2YIdPBW5dv0XRa-M7-Hjwc-oetQw-ISGE_k3mR_rDPvxirERz6lOkCMh5aacjRZRImFIeXUhO9pAWPp64-nOsXtwxM0J6cSg5w6IN11HyvyuJ59Gf5F-Nfbg4r_sW22cw6SSikffcPCtYiUXSzlJCGT_ipVppAZP6CKnqM_tF1vB9_NLH7sKBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله به الدویر، لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/alonews/121300" target="_blank">📅 16:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121299">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/016dec75b2.mp4?token=rkJCU9AGMv0snXP0xue-gWyH79lgCDqLwcQTlmN559JLF5YlOFtbWp84Eqgd98fswtN5afhozLk3FD5Ys6eK9CT5UWQhj-liUG3RaUXklUWV2ZBK04N7hvO_RDY51iwmCx_IWXBYBoT8arSJeS_RrLZQgc9Yy4tYObUWj855ESszgJEwOSjU0tY-kJgnYoMd4XNEbQ893ihrmLaV4jBlmVhPF43jaw0BUqXX2CtRqD6sJEgEmB8bRX6RcmXQPbqHutk1IpMJvyWiU94BDB9zbX625WU5wTpean0J2Pfiz59c-hu80Oy72VhkbJhf-vhxJUwYygnD2NcGYz66yTSi7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/016dec75b2.mp4?token=rkJCU9AGMv0snXP0xue-gWyH79lgCDqLwcQTlmN559JLF5YlOFtbWp84Eqgd98fswtN5afhozLk3FD5Ys6eK9CT5UWQhj-liUG3RaUXklUWV2ZBK04N7hvO_RDY51iwmCx_IWXBYBoT8arSJeS_RrLZQgc9Yy4tYObUWj855ESszgJEwOSjU0tY-kJgnYoMd4XNEbQ893ihrmLaV4jBlmVhPF43jaw0BUqXX2CtRqD6sJEgEmB8bRX6RcmXQPbqHutk1IpMJvyWiU94BDB9zbX625WU5wTpean0J2Pfiz59c-hu80Oy72VhkbJhf-vhxJUwYygnD2NcGYz66yTSi7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
تصاویر دیده نشده از شب ۱۸ دی
👑
حماسه‌ای که ملت شیر و خورشید رقم زدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/alonews/121299" target="_blank">📅 16:11 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121298">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
حزب الله تصاوير منتشر کرد که نشان مي دهد يک fpv به يک باتري گنبد آهنين در محل اسرائيلي جلال العالم در مرز حمله کرده است.‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/alonews/121298" target="_blank">📅 16:11 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121297">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bfdabb819.mp4?token=D2IRCJ6QkB4nLUi2QX6J3SEUb1J7K8WGq8j3KQeLr08FxYa9C7Aa-UyteFyCii0XWiVxvOm-CGtKvkuN8vZzLN9pJDc53cX0fFDwClE7L2zdE03jynlTW1jXhK70FRg80yzTXoCwKvbIwVdWYoElqQhMyIjsS65TJ5WTiC6IoE_FTDttL2xvimOYkfQ3p97VjKts68lriPJ5Zg9HC8eRwFGovzGDt1piJSX5nGvCs15o62Q87pxf-xuvB_GT0lsi5-ukhKfLRKGI--4CMImT0faNtBEMYmGJsyuF1WKEv3-KBgvHk6jH834ofMujWvlXZ_EqJoO11i2WqDWVDiJu9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bfdabb819.mp4?token=D2IRCJ6QkB4nLUi2QX6J3SEUb1J7K8WGq8j3KQeLr08FxYa9C7Aa-UyteFyCii0XWiVxvOm-CGtKvkuN8vZzLN9pJDc53cX0fFDwClE7L2zdE03jynlTW1jXhK70FRg80yzTXoCwKvbIwVdWYoElqQhMyIjsS65TJ5WTiC6IoE_FTDttL2xvimOYkfQ3p97VjKts68lriPJ5Zg9HC8eRwFGovzGDt1piJSX5nGvCs15o62Q87pxf-xuvB_GT0lsi5-ukhKfLRKGI--4CMImT0faNtBEMYmGJsyuF1WKEv3-KBgvHk6jH834ofMujWvlXZ_EqJoO11i2WqDWVDiJu9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ظریف: ما نیاز به تضمین از قول‌شکنان و پیمان‌شکنان نداریم/ مردم و نیروهای مسلح ما بزرگ‌ترین تضمین برای ما هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/alonews/121297" target="_blank">📅 16:08 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121296">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">📱
لطفا توییتر الونیوز رو دنبال کنین
🔴
پست های انگلیسی در رابطه با جنایت های حکومت به انگلیسی نوشته شده و افراد مهم منشن و هشتگ های مهم قرار داده شده.
🔴
ریپست کنین. مهمترین کمک این روزها جلوگیری از پروپاگاندا حکومت علیه این قتل عام مردم هستش. خونشون نباید پایمال…</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/alonews/121296" target="_blank">📅 16:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121295">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cs3_qutmuwAz0sU-bQy7iMFdqE43_aIITHQIseQWhD6i4j6GgPiij0maIqxk5DU5JM0olpOsXaZSBVI47_FEzabCgzRwSniV1feb0Soes-M1pXq3XfbbWDjj4jWzHaw5cw7ZGIawOlCabDbBkXko3tCdHTHgAzmAmY2BTmFIY5ezLdw5_CY0dylVoXZ7sjEA6OkpAPgW9u6IN5uJ6-eNP8Sbossn-3W3rKm9pw0l1KKOa2u0gxUCXGSqa_Eq4jAcnxtEblvUmw7n97OMSPDEXoMTbWRudf-wi9cb5vo88zTqL0Rhx1PjTQq3A_ZfhfCoyri8ZH8SN6fnxLBEoAwpsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام: ۹۰ کشتی رو تغییر مسیر دادیم و ۴ کشتی رو غیرفعال کردیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/alonews/121295" target="_blank">📅 16:06 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121292">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XIuNqOiFOZytWS5W6FxpNKDJo5o7mkS4HHaOmFSM3P3FwnGu93r0rp90r0bQ9QBVeBnS2inOjEtMu6SMG-9I6Rt7X6GYTzIoSr2rScAiHQlVF_NOMmYR9-j8ja_tQzM1jiRl5JlxTCODUZCK8aLCbjxbVZwqSOpZdVqIFz7imIWvRoyeL0dCC_a4bo0JPPbUm9mIhbx0gPrDfe28lTjicZ5icWqVGFuFxW8xfMIV1sTp-pMJcG9CTW2dOLvxzCpR3U1MdeVyOvSsPDsG3FAlHubtbr8fZ0npo5IAd-Aaco8jJIUFBknhI5ZoA5rjlpfu1Tue6yhB8u7E1BEpUfhIJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8e6d5c062.mp4?token=fR995SI7pe4LTZG4ZkA6CInoYOlb1v8Avuf7te3XDHP_TV6lrBHiKFnTaC4-6YFvZs02-XRKzMSMLfmrQlQcqce37y8q_XYiEzBOmDwXLZSxcy8ELPNCSJi7gV_w_ZxYCDTZBch4kJ2Iwdh_SskSYBDvkl9ogbSAYYenikUSZv0HZG8BC4gKA9eNLskbcuRBPFt_xF1zg_nHmQGeeAy4avPPztCVrc3WzkJ71mhnzK8YMglGaxtnQDa9p-M2zdxHqVEyFTPitfwVY1nh4iOanchG8fp0LG-U7T0u-68fUi7ahTuEI8DOI_tXG5S0XKGoLFJvJIZJFxy0FnJguq8J_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8e6d5c062.mp4?token=fR995SI7pe4LTZG4ZkA6CInoYOlb1v8Avuf7te3XDHP_TV6lrBHiKFnTaC4-6YFvZs02-XRKzMSMLfmrQlQcqce37y8q_XYiEzBOmDwXLZSxcy8ELPNCSJi7gV_w_ZxYCDTZBch4kJ2Iwdh_SskSYBDvkl9ogbSAYYenikUSZv0HZG8BC4gKA9eNLskbcuRBPFt_xF1zg_nHmQGeeAy4avPPztCVrc3WzkJ71mhnzK8YMglGaxtnQDa9p-M2zdxHqVEyFTPitfwVY1nh4iOanchG8fp0LG-U7T0u-68fUi7ahTuEI8DOI_tXG5S0XKGoLFJvJIZJFxy0FnJguq8J_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیوهای که داخل رسانه‌ها وایرال شده، یه فرد شبیه چهره علی خامنه‌ای، هست و دست راستش هم آسیب دیده
🔴
میدونم AI هست ولی دلیلش چیه که دارن اینارو رو نشر میدن؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/alonews/121292" target="_blank">📅 15:59 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121291">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MH6VZYy0r4OQL-HfOMs98IzsdgCSPYwbcU8ZexqKWyiPI8cOWlIBMGCw4DPzkEFfRieNwy2MOSVaRu2jHOyWLZie3WnAX5as6W5UGk31wlKUS21fpUNVMMsOe6EfoHwpH-j1gEvqQual1IJtPHaxgGzt596mTV7syO7vn_k9SX089sqnqHH3zhvHlaOUyj9qEyWVXfRKddKEcr6UWvk8S7WrojSE1hrgT2F-AC3O-wWcXzG_miWe-In59ulRz8byqdiDwFIfcTaffze3tul0DY37hnf90WjSTGlRkdxOJzas_vhojTuc1X91MeZCSucB2grAPRe3zKJ_tRz4IY2TUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیروی دریایی سپاه: ۲۶ کشتی با هماهنگی نیرودریایی سپاه عبور کردند
🔴
تردد از تنگه هرمز با کسب مجوز و  با هماهنگی نیروی دریایی سپاه درحال انجام است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/alonews/121291" target="_blank">📅 15:55 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121290">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j4ycoI3wK1hyHMbaQzKA80_N2zqwuNGezMvof14DCF-JSW4nYBiRP3BFH1HWmnSMSzOU2_TD_8ug87F3yfFip-JNiAimJXJ2KMRJXMuk0obnsoghUF5CmY73KjZPH4nlMzSqkQNvpB-Wjs7x5eYfai_C6ZDm_D9TdiFFh6XRP90JAhp0OJSvQlmyungNXH6YiOzXDpvEW-hiKX0slliq5v-voBMj2SfY_YTvCQbyyZsjlSezFeyXsl9WwH94j0XskJ-f35XlkKbSpNZYRU0j77a8Ns9UlbeZlSENJjADeJqK9yF2mBotjlq5ZHY1COO5jidhO-6vtJfRfvJ0opxq8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عقاب‌های دفاعی جمهوری‌خواه در حال بحث درباره راه‌هایی برای مقابله با خروج برنامه‌ریزی‌شده نیروهای نظامی پنتاگون از آلمان هستند، طبق گزارش NOTUS.
🔴
قانون‌گذاران در حال بررسی درج مقرراتی در قوانین آینده مربوط به بودجه و سیاست‌های دفاعی هستند که می‌تواند تأمین مالی کاهش نیروها را مسدود کند یا نیاز به بازگشت تغییرات اخیر در استقرار نیروها را ایجاد نماید.
🔴
گزینه دیگری که در حال بحث است، اعمال تعلیق بر نامزدهای وزارت جنگ است که نیاز به تأیید سنا دارند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/121290" target="_blank">📅 15:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121289">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
منابع دیپلماتیک به سی‌بی‌اس نیوز گفتند که سفر وزیر کشور پاکستان به تهران بخشی از تلاشهای فشرده اسلام‌آباد برای میانجیگری برای توافق صلح با افزایش تنش بین آمریکا و ایران است.
🔴
یک دیپلمات ارشد پاکستانی گفت پاکستان برای یافتن راه‌حل، تلاش‌های خود را دوچندان کرده است
🔴
او افزود: اسلام‌آباد کلافگی‌ها را درک می‌کند، «اما از سرگیری جنگ برای همه یک فاجعه کامل خواهد بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/alonews/121289" target="_blank">📅 15:45 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121288">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
منابع شبکه العربیه
:
آمریکا به پاکستان اطلاع داده است که در مسئله هسته‌ای و مسئله تنگه هرمز هیچ امتیازی نخواهد داد
🔴
منابع افزودند که ایران تضمین‌های آمریکایی برای پایان جنگ را «کافی نمی‌داند»
🔴
آمریکا به پاکستان اطلاع داده است که در مسئله هسته‌ای و مسئله تنگه هرمز هیچ امتیازی نخواهد داد
🔴
منابع افزودند که ایران تضمین‌های آمریکایی برای پایان جنگ را «کافی نمی‌داند»
🔴
پاکستان از «انعطاف‌پذیری محدود آمریکا» در برخی از نکات اقتصادی مطلع شده است.
🔴
آمریکا درخواست‌های خود را در مورد مسئله هسته‌ای و امنیت دریایی در تنگه هرمز تشدید کرده است.
🔴
ایران هنوز معتقد است که تضمین‌های آمریکا در مورد یک جنگ جدید کافی نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/121288" target="_blank">📅 15:39 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121287">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
سی‌بی‌اس به نقل از منابع دیپلماتیک:
اسلام‌آباد تلاش‌های خود را برای حل مناقشه دوچندان کرده است و معتقد است که شروع مجدد جنگ برای همه فاجعه خواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/alonews/121287" target="_blank">📅 15:36 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121286">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
الحدث درمورد مذاکرات ایران و آمریکا: پاکستان از انعطاف محدود آمریکا در برخی موارد اقتصادی مطلع شده
🔴
آمریکا خواسته‌های خود را در بخش هسته‌ای و تنگه هرمز تشدید کرده است.
🔴
ایران همچنان معتقد است که تضمین‌های آمریکا درمورد عدم ازسرگیری جنگ کافی نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/alonews/121286" target="_blank">📅 15:30 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121285">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84d857cfaf.mp4?token=rhMq2_NkLt0ZbdZKbpy2GabV0NOF8GMkyaHQb9fYjPHsmPq2FBQTtk02XaOfqCdEoA1TjCSyAiQWp-BKcD7tyW9sVKBj0x_PzOAYxzEHEHiMTIH-V4381t_hv72UOI02miGyh00tCpfqMj8Fo_KfYy5TQZGWuR0CISjUPZwLugsPM4rJ-8YzcqPfjEnKzJMnr01VolUnivo1GslrYlZw0TPFYPJ_6SYO-zRs49wPmzT271gITcSvmILeN1QTaPRtcbXu10j4DFNRB2K-NCC-1LtnF-EN_xCBZ3EEI22JbUy2uget9uW7ZkmQT8lj_m88ga9H3f4XhOSW8LFH2ZLpsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84d857cfaf.mp4?token=rhMq2_NkLt0ZbdZKbpy2GabV0NOF8GMkyaHQb9fYjPHsmPq2FBQTtk02XaOfqCdEoA1TjCSyAiQWp-BKcD7tyW9sVKBj0x_PzOAYxzEHEHiMTIH-V4381t_hv72UOI02miGyh00tCpfqMj8Fo_KfYy5TQZGWuR0CISjUPZwLugsPM4rJ-8YzcqPfjEnKzJMnr01VolUnivo1GslrYlZw0TPFYPJ_6SYO-zRs49wPmzT271gITcSvmILeN1QTaPRtcbXu10j4DFNRB2K-NCC-1LtnF-EN_xCBZ3EEI22JbUy2uget9uW7ZkmQT8lj_m88ga9H3f4XhOSW8LFH2ZLpsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نخست‌وزیر بریتانیا، کیر استارمر، اشتباه کرد و گفت که بریتانیا با کره شمالی توافق تجاری امضا کرده است به جای کره جنوبی.
🔴
او پس از دریافت یادداشتی متوجه اشتباه خود شد و سریعاً آن را اصلاح کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/alonews/121285" target="_blank">📅 15:29 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121284">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
وزیر نیروهای مسلح فرانسه: ناو هواپیمابر شارل دوگل به منطقه عملیاتی شبه جزیره عربستان رسیده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/alonews/121284" target="_blank">📅 15:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121283">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YISoXma3UwJUOnvBf3zZ58qFkHoyaCUwf773dmxQ_JQNmAO5EDBKrES-D23bLuWG0VHVAg8TBAn_zKNuam98Qn5rGiXHJkPoJr2IQzFKPBR6g_V_ZsXkzy72ctP8xuvmYcxwZDbiYlQTkXUY_IT9a5Lp2cxuKaryh1Gxc5JJMfcelgvWl5zDSz83DeRF35SPF13t0dZTwjAJNm3gpYizXKJUbsyEIloNqlb4f6ik8VROO7ZyPN2Nm4Q9QsUgqfRwZi3HTqhlqeBqJsjXDwgajJ2uYOLoNKuz96sl0UgWyY-NBuUgzrWH84l44xKty_RZiaOqSfLSJ_hNiEzgFHds1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده:
از امروز، نیروهای ایالات متحده ۹۰ کشتی را تغییر مسیر داده و ۴ کشتی را غیرفعال کرده‌اند تا اطمینان حاصل شود که قوانین رعایت می‌شوند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/alonews/121283" target="_blank">📅 15:23 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121282">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4dbb78ffa.mp4?token=cje3LiTxQFlqH5Iwbp-MHox0RzL4slmUMs2nvC75KPKmei9fW2j9co5RVv5JG4JRp4DKNCs12NJTJEdXXlaLX2Oy3f25RLzAja9dS-SK7tjwA3pc_BmreE2eBRjw0sjzinETEgNg0vwbv0cOoeXplJATev__rmUp3mF23q4SRXcETse4A5g8GFkN_Il4p75u1m52s-PwLu2PT42_jOxCoUNRgoBZJ6apJiMYJmpvUW2o5m72F3Gi9lFAw6Ib4D1f820noZemsm3wnXSy2Qe8IbgacK1dxm7iWGebwwa6NS4NtsVHkK6T4EuckXYlXh4wMvqG9ffX810ZpBCzVx2Jmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4dbb78ffa.mp4?token=cje3LiTxQFlqH5Iwbp-MHox0RzL4slmUMs2nvC75KPKmei9fW2j9co5RVv5JG4JRp4DKNCs12NJTJEdXXlaLX2Oy3f25RLzAja9dS-SK7tjwA3pc_BmreE2eBRjw0sjzinETEgNg0vwbv0cOoeXplJATev__rmUp3mF23q4SRXcETse4A5g8GFkN_Il4p75u1m52s-PwLu2PT42_jOxCoUNRgoBZJ6apJiMYJmpvUW2o5m72F3Gi9lFAw6Ib4D1f820noZemsm3wnXSy2Qe8IbgacK1dxm7iWGebwwa6NS4NtsVHkK6T4EuckXYlXh4wMvqG9ffX810ZpBCzVx2Jmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نخست‌وزیر مجارستان، پتر ماجار:
اوکراین قربانی است و حق دارد با هر وسیله‌ای که در اختیار دارد از حاکمیت و تمامیت ارضی خود دفاع کند.
🔴
هدف همه، دستیابی به آتش‌بس پایدار و صلحی پایدار است که توسط جامعه بین‌المللی تضمین شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/alonews/121282" target="_blank">📅 15:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121281">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
صداو‌سیما: سرریز نفت در خارگ صحت ندارد و دریا سالم است
🔴
عبور شناورهای ملیت‌های مختلف به‌ویژه شرق آسیا از تنگۀ هرمز بیشتر شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/alonews/121281" target="_blank">📅 15:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121280">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
نیروهای دفاعی اسرائیل: پس از هشدار درباره یک حادثه امنیتی مشکوک که در منطقه نوفیم اعلام شد، نیروهای امنیتی در آن منطقه جستجو کردند و یک ساکن اسرائیلی از جامعه را در نزدیکی حصار شناسایی کردند.
🔴
نگرانی از بابت حادثه امنیتی وجود ندارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/alonews/121280" target="_blank">📅 15:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121279">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66d1114edb.mp4?token=Gqy4_4aOPHIg-4p0RbVMYamzV-gRXYNMvMjOxgbPVD4LfUSq7_CH_kOuJuEu7WZN_YroPNMRhzAdDLYZeoFFcCYnu9-SxEvy0YFLZxjfG86qafulf6gjb6SLB65v16lZRr4rqjch5pTpPMzTBH5Pg2-ryfCFUL-8DPzUS6JXBbNEuf_zH7vR8CLdz-hBpDA2t4otGI2sZQypwTIv3D0WpSKQvc48iBBfzxyLmIcf9QVT6AosAXHKoZQHB5kCC4cm5iMJZnUnFxMp4mNfcM9k64DKKUKKIZPFt4I0EM1ORTOcaLDtKFoKqq768byiU4btQ6FOtAjkkiTf2qXcR5KIMTIp0V-0u_hLMUi_O0wwq9dpVIBHm3lufnfrXfWkRArLItTTo3a_0K4Y1BuG1owY4azG8zICbALF64Wi74WUeuH8-qx5M4MUw3k0ucX7dbOMaGmF3t6WMM0g2hXf7Z38QR3s6EhfCIwZUKP5r67g3LDkZAnmxR_iU1CqYYol_pqMYGj8GJzHOMrlvbYFG3LjaKveF0TjpdW-RRRHZj5l4F_NN4gUGvj3LAPjPj-Xjx6ZLuEuJZkUKkY2fR9r4XtwEPd-zm_02aUzl82eVhyjQL_ll6dn4ZEp4vrgpI3lURx2bO-lqDEt4DiUhsxo87uqxoNILsaZKZQbYE5ib2vyTlk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66d1114edb.mp4?token=Gqy4_4aOPHIg-4p0RbVMYamzV-gRXYNMvMjOxgbPVD4LfUSq7_CH_kOuJuEu7WZN_YroPNMRhzAdDLYZeoFFcCYnu9-SxEvy0YFLZxjfG86qafulf6gjb6SLB65v16lZRr4rqjch5pTpPMzTBH5Pg2-ryfCFUL-8DPzUS6JXBbNEuf_zH7vR8CLdz-hBpDA2t4otGI2sZQypwTIv3D0WpSKQvc48iBBfzxyLmIcf9QVT6AosAXHKoZQHB5kCC4cm5iMJZnUnFxMp4mNfcM9k64DKKUKKIZPFt4I0EM1ORTOcaLDtKFoKqq768byiU4btQ6FOtAjkkiTf2qXcR5KIMTIp0V-0u_hLMUi_O0wwq9dpVIBHm3lufnfrXfWkRArLItTTo3a_0K4Y1BuG1owY4azG8zICbALF64Wi74WUeuH8-qx5M4MUw3k0ucX7dbOMaGmF3t6WMM0g2hXf7Z38QR3s6EhfCIwZUKP5r67g3LDkZAnmxR_iU1CqYYol_pqMYGj8GJzHOMrlvbYFG3LjaKveF0TjpdW-RRRHZj5l4F_NN4gUGvj3LAPjPj-Xjx6ZLuEuJZkUKkY2fR9r4XtwEPd-zm_02aUzl82eVhyjQL_ll6dn4ZEp4vrgpI3lURx2bO-lqDEt4DiUhsxo87uqxoNILsaZKZQbYE5ib2vyTlk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دبیرکل ناتو: می‌دانیم که چین در دور زدن تحریم‌ها و تحویل کالاهای دو منظوره فعال بوده است.
🔴
من هرگز در مورد نقش چین در جنگ روسیه علیه اوکراین ساده‌لوح نبوده‌ام
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/alonews/121279" target="_blank">📅 15:06 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121278">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lr1XJAwbO2K70nGii8YSrE-UHupE56A9qwkh2p3rp9DBofgOn9tSljAyVUDEvo9v_l35UC3zENVxunkzIxj6NGyS6lR86qPDpXA7vBxU4mMR99hgX2zKszoHO5b7ifxT4m0ttsGg9NT1Ik8DyLJVJCFV3nQuen91VM4sf1r5j3nzBYrLjD9FErBI5AvekmLstKKJsdL3U22j_Gogc7ccORvjbWw7AMeGdN_m6JAmAuTcv35EHmO2BftbsE9ETX0X-yrxxVEWqd1W8fJEiA0EEZ2DbHob09mq9IaMHPPaTt2fxH_5cDaQpGR4IL_wOWM6KSO6_QnXpIf0A3Xi_NFE-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امارات متحده عربی حملات تروریستی «خیانت‌آمیز» را محکوم کرد، اشاره به پهپادهایی که از خاک عراق پرتاب شده‌اند، از جمله یکی که روز یکشنبه به نیروگاه هسته‌ای باراکه در ابوظبی هدف گرفته شد، و از بغداد خواست فوراً و بدون قید و شرط از تمامی اقدامات خصمانه‌ای که از خاک آن نشأت می‌گیرد جلوگیری کند و فوراً به این تهدیدات رسیدگی نماید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/alonews/121278" target="_blank">📅 14:59 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121277">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
ناتو : رزمایش‌‌های هسته‌ای روسیه رو زیر نظر داریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/alonews/121277" target="_blank">📅 14:57 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121276">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
امارات به عراق هشدار داده جلوی اقدام یا حمله‌ای که از خاکش علیه دیگر کشورها انجام میشه رو بگیره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/alonews/121276" target="_blank">📅 14:53 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121274">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d1cc9d932.mp4?token=DVQu5yBcI9Z3PnTrAKpqn6xHed3ZJZx_ION0isLmOhaWeNbx2xdYuwrJaE0A7AWVy6KZQG40DySLfVxArZFyMQi_kyLHUOy6b6VKYAjtRYFvE2fVoizYXLh6cv__r4pM0ZJkXJJokHxxGk3AaomLTVlF9e4jLXojQznZ7UibjIL43reM3Z3AoJYW3YzSo1w1UyqqQxYoVswr4A-OhxC5LtaFCBwITSlN27gkkXYXbEbuzu6KKK7V8adUoU0M0mqkkTk2CD5GnHqcer7NSisK8PBRpjBQe6rpmoHH_xSWGv86684OCig3SIcJzsuQwipdWum0NuWOvXldSVa4bKFHMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d1cc9d932.mp4?token=DVQu5yBcI9Z3PnTrAKpqn6xHed3ZJZx_ION0isLmOhaWeNbx2xdYuwrJaE0A7AWVy6KZQG40DySLfVxArZFyMQi_kyLHUOy6b6VKYAjtRYFvE2fVoizYXLh6cv__r4pM0ZJkXJJokHxxGk3AaomLTVlF9e4jLXojQznZ7UibjIL43reM3Z3AoJYW3YzSo1w1UyqqQxYoVswr4A-OhxC5LtaFCBwITSlN27gkkXYXbEbuzu6KKK7V8adUoU0M0mqkkTk2CD5GnHqcer7NSisK8PBRpjBQe6rpmoHH_xSWGv86684OCig3SIcJzsuQwipdWum0NuWOvXldSVa4bKFHMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حزب‌الله از داخل ساختمونای غیرنظامی نیروها رو زیر نظر داشته
🔴
نیروهای یگان چندبعدی اسرائیل هم به تجهیزات دیده‌بانی حمله کردن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/alonews/121274" target="_blank">📅 14:43 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121273">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
صدا و سیما: ۵ ابرنفتکش برای گذر از تنگه از نیروی دریایی ما اجازه گرفتن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/alonews/121273" target="_blank">📅 14:42 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121272">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41b2997c91.mp4?token=h49sgTjVPxb6jKViBd1Zb6feoU2Vr6dwi671ePu0TrkZ5yBDTCmKlUGyRMwlax1WopCwe2Bu7gtXGc-6Y662I-Bu0IArbGyabs8PojCqM3b5RfUUx9he4DqDCo4KBPtrv12xKYyuyUnpIV9l6FS9Bw3sHZhWtfMmpWk5szBFiHC5iYR9G8tmOigOPmRjzROB-AP9VLZWQYHKEfm5NQCm6sQOWVwWF3S-jvck1RZ2WZQnaOi6kUHfuRUU9vOH_XE3ZlHSYVzWtjTwDT-aMTpr00rvoXlgFXZAjmyXG2E4qhOo57xYpVmFpgTNj1PqSDh3hPq7Hgbi4K4rxb6XEGdHz4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41b2997c91.mp4?token=h49sgTjVPxb6jKViBd1Zb6feoU2Vr6dwi671ePu0TrkZ5yBDTCmKlUGyRMwlax1WopCwe2Bu7gtXGc-6Y662I-Bu0IArbGyabs8PojCqM3b5RfUUx9he4DqDCo4KBPtrv12xKYyuyUnpIV9l6FS9Bw3sHZhWtfMmpWk5szBFiHC5iYR9G8tmOigOPmRjzROB-AP9VLZWQYHKEfm5NQCm6sQOWVwWF3S-jvck1RZ2WZQnaOi6kUHfuRUU9vOH_XE3ZlHSYVzWtjTwDT-aMTpr00rvoXlgFXZAjmyXG2E4qhOo57xYpVmFpgTNj1PqSDh3hPq7Hgbi4K4rxb6XEGdHz4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بن‌گیور، وزیر امنیت ملی اسرائیل، از فعالان بازداشت‌شده در کاروان جهانی صمود غزه در بندر آشدود بازدید کرد.
🔴
به اسرائیل خوش آمدید، ما اینجا در کنترل هستیم. این همان چیزی است که باید باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/alonews/121272" target="_blank">📅 14:37 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121271">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
کنست به انحلال خود و برگزاری زودهنگام انتخابات رای داد
🔴
کنست در جلسه مقدماتی خود با اکثریت ۱۱۰ عضو و بدون هیچ مخالفتی، به لایحه انحلال خود و جلو انداختن تاریخ انتخابات رأی داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/alonews/121271" target="_blank">📅 14:30 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121270">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
رئیس مرکز رسانه مجلس: ادعای کناره‌گیری قالیباف از سرپرستی تیم مذاکره‌ کننده، کذب محض و دروغی آشکار است
🔴
این ادعا امتداد همان خط تخریبی است که تا دیروز فرماندهان را نشانه می‌رفت و امروز شهدای والامقام را
🔴
البته از جریانی که سابقه هجمه به فرماندهان نظامی، دفتر مقام معظم رهبری و مراجع عظام تقلید را در کارنامه دارد، رفتاری غیر از این انتظار نمی‌رود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/alonews/121270" target="_blank">📅 14:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121269">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
پوتین و شی جین‌پینگ : جنگ ایران باید سریع متوقف شه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/121269" target="_blank">📅 14:11 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121268">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
رسانه عبری وای نت: امارات هماهنگی‌های امنیتی و عملیاتی با اسرائیل را تشدید کرده
🔴
این اقدام به منظور آمادگی برای سناریوی احتمالی بازگشت به نبرد علیه ایران صورت گرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/alonews/121268" target="_blank">📅 14:03 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121267">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
یک منبع بلندپایه دیپلماتیک گفت:
فضای بی‌اعتمادی هماهنگی‌های میان ایران و پاکستان را تحت تاثیر قرار داده و همکاری‌های فشرده دو کشور طی دو هفته گذشته اکنون متوقف شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/121267" target="_blank">📅 14:00 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121266">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
مقامات آلمانی دو شهروند آلمانی را به اتهام جاسوسی برای سرویس اطلاعاتی چین دستگیر کردند، دفتر دادستان فدرال آلمان گفت.
🔴
متهمان، که به عنوان شواچون و هوا شناسایی شدند، اطلاعاتی در مورد محصولات با فناوری بالا با کاربردهای نظامی جستجو کردند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/alonews/121266" target="_blank">📅 13:57 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121265">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
خبرگزاری قوه قضائیه: رشید مظاهری، بازیکن سابق فوتبال، هنگام خروج غیرقانونی از کشور دستگیر شده. پیگیری‌ها نشون میده این فرد قصد داشته با تغییر چهره و پول دادن به ماموران مرزبانی، از مرزهای غربی به صورت غیرقانونی از کشور فرار کنه، ولی موقع خروجش دستگیر شده.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/alonews/121265" target="_blank">📅 13:54 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121264">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d731a2a6c.mp4?token=vGdpqOer6_mR4Wmk1WnII2rTEl_aOvl81SS0XGPokVxa2Xn9ochSyxGxMkr-jurZUfNeL17j6WAZzZzxrEuLVB1M4YTv0-BkWRgDlnrOAA0k3N3e8hVoBhWJXoyFfXXayz9UKdggBFnTB3S-LMvJgi-LxNm1jY7SkcPFdy0ITKSOZDpj9pgt7oDKTycVlJdD6VJVgIxfkbtZgoPiQkwfT1xy18iQrB-TWj_B6UcIhYEuRYcOfl5CrYbFX-VcugNNlPxl1WI5vKDekfUjpC-qxtIKyezvQg1JQorZwtkP6_32wM_QTm_Egw-oCch4Vfu1K7d-689XwtFAR1N-vJkHNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d731a2a6c.mp4?token=vGdpqOer6_mR4Wmk1WnII2rTEl_aOvl81SS0XGPokVxa2Xn9ochSyxGxMkr-jurZUfNeL17j6WAZzZzxrEuLVB1M4YTv0-BkWRgDlnrOAA0k3N3e8hVoBhWJXoyFfXXayz9UKdggBFnTB3S-LMvJgi-LxNm1jY7SkcPFdy0ITKSOZDpj9pgt7oDKTycVlJdD6VJVgIxfkbtZgoPiQkwfT1xy18iQrB-TWj_B6UcIhYEuRYcOfl5CrYbFX-VcugNNlPxl1WI5vKDekfUjpC-qxtIKyezvQg1JQorZwtkP6_32wM_QTm_Egw-oCch4Vfu1K7d-689XwtFAR1N-vJkHNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ابوالفضل ظهره‌وند، نماینده مجلس : اگه دشمنامون بیان رهبرامونو ترور کنن
🔴
ما هم باید جوابشونو با ترور رهبرای اونا بدیم، نه اینکه بریم پای مذاکره
🔴
اگه آمریکا بخواد تو آینده رهبرامونو بزنه، ایرانم باید واشنگتن دی‌سی رو بزنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/121264" target="_blank">📅 13:49 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121263">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
سقوط قیمت طلا به پایین‌ترین سطح یک ماه و نیم اخیر
🔴
هر اونس با ۰.۴ درصد کاهش، ۴۴۶۴ دلار معامله شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/121263" target="_blank">📅 13:46 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121262">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
بریتانیا برخی تحریم‌ها علیه روسیه را با اجازه واردات دیزل و سوخت جت تصفیه شده از نفت خام روسی در کشورهای ثالث به بریتانیا، کاهش داده است.
🔴
این معافیت که امروز اجرایی شد، از طریق مجوزی دولتی صادر شده که «به صورت نامحدود» معتبر خواهد بود، مشروط به بازبینی دوره‌ای توسط وزیر تجارت.
🔴
برخی محدودیت‌ها بر حمل و نقل گاز طبیعی مایع شده روسیه نیز برداشته شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/alonews/121262" target="_blank">📅 13:42 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121261">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rU6r_cuuGAJpFVNw9gGCnLa1WWGHyPiC4fPZPoBIdGz59MEceenEJdxyZDxHjZ-SxtCF2adbCdXcc8_yemayKctAxUXA5L2nu5GRUlIQ3gLfGrAi2xRxGmrEAHfe7TC9Y2vDbuLLzaXGZOF3QtBcGEdsFNsu9kxdZKw_vhEY_31WAE1s5hsdhxMbHmx5M78i_HqFVQMDxwEI_5SPGBIfjfCSUfM6UWZAubS8jbNUgulbgpP9aNyZm4zJiWDt8_mOPq4qrBwC094lBb05HnDLPBUozbwN4XFlaV37szmUW2iXoAAHz5TH7NEpEoSHTaP-nEzAAm0XsEkTzSC4nKsdrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت استثنایی گیگی
9️⃣
8️⃣
1️⃣
تحویل زیر یک دقیقه
✅
دارای لینک سابسکریشن جهت دیدن حجم و کنترل مصرف
✅
بدون قطعی
✅
بدون محدودیت کاربر و زمان
✅
جمینایو چت جی بی تی و... کامل اوکیه با سرورامون
✅
🏪
پشتیبانی کامل
✅
شروع فعالیت از سال 2022
✅
پرداخت ریالی
✅
ضریب و این چیزا ندارن و تا آخرین مگابایت برای پشتیبانیش درختمتیم
🥂
💤
این تخفیف فقط تا ۱۲ شب فعاله
💤
⭐️
@Napsternetiran_bot
〰️
〰️
〰️
〰️
〰️
〰️
〰️
🔶
@Napsternetvirani</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/121261" target="_blank">📅 13:37 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121260">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
وزارت خارجه آمریکا تا سقف ۱۵ میلیون دلار پاداش برای اطلاعات در مورد شبکه مالی سپاه پاسداران تعیین کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/121260" target="_blank">📅 13:27 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121259">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
گروسی: برای تضمین امنیت هسته‌ای به خلیج فارس سفر می‌کنم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/alonews/121259" target="_blank">📅 13:20 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121258">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
دبیرکل ناتو: ایران با بستن تنگه هرمز، اقتصاد جهانی را گروگان گرفته است
🔴
مارک روته، دبیرکل پیمان آتلانتیک شمالی در اظهاراتی علیه ایران گفت: این اتحاد و جامعه بین‌المللی دستیابی ایران به سلاح هسته‌ای را رد می‌کنند. بسیاری از کشورها در ایجاد ائتلافی برای تضمین آزادی دریانوردی در تنگه هرمز مشارکت دارند.
🔴
ما در مورد حمایت از متحدان خود در منطقه خلیج فارس بحث خواهیم کرد.  کشورهای اروپایی، علاوه بر کانادا، از همان روز اول با گشودن پایگاه‌های نظامی به روی هواپیماهای آمریکایی، از ایالات متحده در عملیاتش علیه ایران حمایت کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/alonews/121258" target="_blank">📅 13:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121257">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
بنیات از اول خرداد ۲۰ درصد گرون میشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/alonews/121257" target="_blank">📅 13:08 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121256">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ub9ZZZSx-Qq3n9--JfyUoCfU2zlDTK_R_cIVmSSsRLQoQCvHRzqUDT5YWGvZoHxJfAOktnDRKElCmRJH8E1UGxdFI7dQA0XGL5xaf0bsxs0H1CNVw3OWI7xs_yaZBl0U6XIGEctR_IsDfNpaRrFobGlXdRdw1h1WEc7t_9xQbRV7lBWu2gwf8TtWgfLWpLefd_vOHrmDEGuGozNokudKL042h0hXD5kEQEab4AxPwlNFXtaUrKybE-KbGfdA0UgVHE7dOEjloXEiN9RY9z77NVaxoM6xcqP0mIJvFNnIhJm7l3iIh5u56JJVm7UEVNmH14kJCyPQybwF-TPIvoynWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اعلام قیمت نهایی خودروی وارداتی لکسوس LX600
🔴
110 میلیارد تومان...!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/alonews/121256" target="_blank">📅 13:04 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121255">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
نفوذ پهپاد به حریم هوایی اردن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/alonews/121255" target="_blank">📅 13:00 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121254">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be63a69a09.mp4?token=Y7CU-HShHEZeF2wIxeCKFZ-O5dS9tEgyq9yAe1uMNDEKqpA5nmQ4Z6qtRu4SELb3DugjeM62iGNfJDikTT7Q4t5xaAV6P2A0kotvh1cxlKFUMG_M6kYHGJWtzulMfq8jyeJ0oTATU1UtGaPgMC8cg_V5XH_oQhQt1NXZmyWMChqC3npcYIbuUiS_yW9BHpgqQOkMBCFW9xtmvDVfV7SRLaUQ5COMPDDHyGCWaBzJ0q6WwRn1PYlSzfnuDI2P93dsEEcTGrG_oX2G3Ljuy_I0KPAxppjkmyXEY7HCuxoCR-bYrWHdSXAJU8zEXH-evrX1JT8VBRjCScRCrnbspOJ1bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be63a69a09.mp4?token=Y7CU-HShHEZeF2wIxeCKFZ-O5dS9tEgyq9yAe1uMNDEKqpA5nmQ4Z6qtRu4SELb3DugjeM62iGNfJDikTT7Q4t5xaAV6P2A0kotvh1cxlKFUMG_M6kYHGJWtzulMfq8jyeJ0oTATU1UtGaPgMC8cg_V5XH_oQhQt1NXZmyWMChqC3npcYIbuUiS_yW9BHpgqQOkMBCFW9xtmvDVfV7SRLaUQ5COMPDDHyGCWaBzJ0q6WwRn1PYlSzfnuDI2P93dsEEcTGrG_oX2G3Ljuy_I0KPAxppjkmyXEY7HCuxoCR-bYrWHdSXAJU8zEXH-evrX1JT8VBRjCScRCrnbspOJ1bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارش‌هایی از یک رویداد با تلفات انبوه در شهر دویر در جنوب لبنان پس از یک حمله هوایی اسرائیلی که حدود ۳۰ دقیقه پیش منطقه را هدف قرار داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/alonews/121254" target="_blank">📅 12:59 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121253">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
وزیر کشور پاکستان عازم تهران شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/alonews/121253" target="_blank">📅 12:55 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121252">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
وزارت خارجه کره جنوبی اعلام کرد: کشتی تحت مدیریت این کشور پس از مشورت با مقامات ایرانی، با خیال راحت از تنگه هرمز عبور کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/alonews/121252" target="_blank">📅 12:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121251">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
بحرین : نیروهای ما تو حالت آمادگی رزمی "کامل" قرار داره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/alonews/121251" target="_blank">📅 12:46 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121250">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
«امارات متحده عربی به آرامی با پاکستان تماس گرفته و به دنبال درگیری مجدد است.
🔴
این حرکت پس از یک درک آشکار میان تصمیم‌گیرندگان اماراتی رخ داده است که پاکستان کشوری بسیار مهم است که نباید در سمت اشتباه قرار گیرد.
🔴
همچنین تغییری در سیاست امارات وجود دارد. برخلاف موضع قبلی خود، ابوظبی اکنون دیپلماسی را برای حل تعارض ایران-آمریکا ترجیح می‌دهد،» - کامران یوسف از شبکه جهانی تی‌آرتی و اکسپرس نیوز پاکستان.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/alonews/121250" target="_blank">📅 12:41 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121249">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
مقامات بحرین دو تبعه مصری را به اتهام ابراز همدردی با جمهوری اسلامی ایران به ۱۰ سال زندان محکوم کرده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/alonews/121249" target="_blank">📅 12:37 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121248">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
رشد ۴۲ هزار واحدی شاخص بورس در دومین روز بازگشایی بازار
🔴
شاخص کل بورس با رشد ۴۲ هزار واحدی در پایان معاملات امروز به ۳ میلیون و ۷۵۸ هزار واحد رسید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/alonews/121248" target="_blank">📅 12:36 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121247">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
رسانه‌های اسرائیلی: ترامپ و نتانیاهو دیشب تماس تلفنی طولانی داشتند که به عنوان تماس محوری توصیف شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/alonews/121247" target="_blank">📅 12:31 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121246">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
طبق مصوبه جدید کارگروه تنظیم بازار، قیمت انواع چای به‌صورت دوره‌ای تعیین و اعلام می‌شود و دولت بانک مرکزی و چند وزارتخانه را مکلف به کنترل بازار چای کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/alonews/121246" target="_blank">📅 12:25 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121245">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
الجزیره: اکثریت روس‌ها دیدار روسای جمهور روسیه و چین را تحول آفرین نمی‌دانند، بلکه آن را گامی مهم برای تقویت روابط اقتصادی می‌بینند
🔴
برای بسیاری از مردم روسیه ملاقات پوتین و زلنسکی، قطعاً حیاتی‌تر از این دیدار است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/121245" target="_blank">📅 12:22 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121244">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d355e12d20.mp4?token=nqMj3Ew5dOVcao6D3Vlncv2wz1BDt_C_xjDrOYubTJicMk3eK5o9bbq7wLpONPYr8n6yKoBpA_2HMNfcIT3xSg07S29oWSEUvOQPZkqNhGaDNlI9mwiabCUSR76wkUP8ZjmNnU6v2K0nn47zWTGnnSPAi8FaN9pG3csH1HmlX6f1tTdYnegRf3CKf50Jt8g5jQogegbhCjqgeHJDXqStDnofa5DfvxKgPMl4i2_P3vEvvxwnC5_zoSQCIumvl6xRaVK129TwtaWtPM-XRACo8byF9XC5K2eP1M6bkQVeBo06D3wa86w5gjFj8gNslE0_ZI5ZqgIXXXHeKWCExahAfA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d355e12d20.mp4?token=nqMj3Ew5dOVcao6D3Vlncv2wz1BDt_C_xjDrOYubTJicMk3eK5o9bbq7wLpONPYr8n6yKoBpA_2HMNfcIT3xSg07S29oWSEUvOQPZkqNhGaDNlI9mwiabCUSR76wkUP8ZjmNnU6v2K0nn47zWTGnnSPAi8FaN9pG3csH1HmlX6f1tTdYnegRf3CKf50Jt8g5jQogegbhCjqgeHJDXqStDnofa5DfvxKgPMl4i2_P3vEvvxwnC5_zoSQCIumvl6xRaVK129TwtaWtPM-XRACo8byF9XC5K2eP1M6bkQVeBo06D3wa86w5gjFj8gNslE0_ZI5ZqgIXXXHeKWCExahAfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مراسم عروسی جان فداها: عروس رفته تنگه هرمز گل بچینه!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/alonews/121244" target="_blank">📅 12:17 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121243">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rOn42s4cFHkuRMX42eltbnw9h6DhdO-8lfTjCDZ8yqJdSp1-hLcFfU6svnxOnTKm6nicUF20dwRxOk8uDA2tH8Yan-5Du3GBmF7fQr1tOkdqShb-SpaX21F371Ao77DOysN6CRtAHaoJkcNRnzQ1qXDbgld_U41-XQWFfrgPFQWCFV96GvcIx4ckhVejvyCScjAeHyujg5FroG0oAnKzz3YqgoyHS0e7kqa9ERmPGUb_zeSskpD2AUJdmN1uyeUvXdTvhPbEQ4KiLdBbCWSV2jY-Xrln2frdkZaJADmyBeyXnJh2ChouObQD-8i_Uoo6A77CR82zWsPLl57cBmJUjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حملات اسرائیل به جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/alonews/121243" target="_blank">📅 12:13 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121242">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
فرمانده سنتکام دلیل خروج ناوگروه «جرالد فورد» از خاورمیانه را اعلام کرد
🔴
«برد کوپر»، فرمانده ستاد فرماندهی مرکزی آمریکا (سنتکام)، علت خروج ناوگروه «جرالد فورد» از منطقه خاورمیانه را تشریح کرد.
🔴
دریاسالار کوپر عنوان داشت که «نیازی به حضور همزمان سه ناوگروه حامل پرچم در خاورمیانه نبود.»
🔴
وی افزود که ناوگروه‌های «جورج بوش» و «آبراهام لینکلن» همچنان در منطقه حضور دارند. کوپر گفت: «نیازی پایدار به وجود سه ناو هواپیمابر در منطقه احساس نمی‌شد.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/alonews/121242" target="_blank">📅 12:08 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121241">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X6R7qvrVpWeL291BKl6FWOMRjAURDfatz856p3vf_AIwD3KmDyvHwbfb07ZTj5zcQhif6yA27ataNuwBu4bNZfjkmnO3WNAKiIgkOHdRGXZ4o2stSQ5_NlzsMst5eXNpjXDf8NT8lDLXCBo5aSMvea7uABN4uig970UlwK4KCqLf5kytbyKViM7khnROutm4Vjic_ODM4IA_whqLmdpBj2Ke3rk6Qtw9NawMkmF-vU3Ekwo9I8EVFfGKp3w3wBC940bDQQzOw8Nd2ZJkWcKIQIKiG3WOTH5nX7aIAiFbpKtXgdTgFF3DxdyTGnopFbQC22yWM8Wj8ojoAZV0rV05jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش سوریه با یک واحد اصلی در تمرین نظامی EFES-2026 ارتش ترکیه شرکت می‌کند.
🔴
این اولین بار است که نیروهای سوریه از زمان تغییر حکومت در یک تمرین نظامی خارج از سوریه شرکت می‌کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/alonews/121241" target="_blank">📅 12:05 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121240">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d10e5ea2d.mp4?token=RpQY0Sp6hPe_Z3oZAF7RmNBO2GPK63x7CUv6YSz05ea2P6lCsq6DJ3AslYBic_OPq_YZaZ-P-vXe0sL98Q0jB0mMhcX-vLJrDRBE0btG3Y6JROrWQTzuEaiSsE1vdEwGaOQjDXG5xaXVB6oRhiwiprc0SCJ1lbpA3JgN_8d0VLZxtvwbCOb7q5cXo-HRPZx2M84RHxk_W2_qQG0qPTCh97cVxs7BP81GIs_sslvqCX9T8ADBmaPFqSj41iFRX3mdPkVYyBSoFwviqzZgbg3u8c9_q99K4o1TIV6bVRMn79nkBkGcbLa2KyIPhnaxgFB4isIuYb4WKtUCQZ21KfI22Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d10e5ea2d.mp4?token=RpQY0Sp6hPe_Z3oZAF7RmNBO2GPK63x7CUv6YSz05ea2P6lCsq6DJ3AslYBic_OPq_YZaZ-P-vXe0sL98Q0jB0mMhcX-vLJrDRBE0btG3Y6JROrWQTzuEaiSsE1vdEwGaOQjDXG5xaXVB6oRhiwiprc0SCJ1lbpA3JgN_8d0VLZxtvwbCOb7q5cXo-HRPZx2M84RHxk_W2_qQG0qPTCh97cVxs7BP81GIs_sslvqCX9T8ADBmaPFqSj41iFRX3mdPkVYyBSoFwviqzZgbg3u8c9_q99K4o1TIV6bVRMn79nkBkGcbLa2KyIPhnaxgFB4isIuYb4WKtUCQZ21KfI22Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شی جین‌پینگ: رئیس‌جمهور پوتین قبلاً برای بیست و پنجمین بار به چین سفر کرده است
🔴
این به خودی خود نشان‌دهنده سطح بالا و ماهیت خاص روابط چین و روسیه است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/alonews/121240" target="_blank">📅 11:57 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121239">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fcd06da20a.mp4?token=bH4FuD-QrRfl1cozUI6I7iRDRdX4JrIj9k5RMN1kbfOmVWQhnkGEjSax1u5VtdLOATtS12KqosHSjTPToYq-RESpT_zgorejXuQ9HWLnWD3Tyk2C4ikzc5Q0Td2AmxzyGLCYRvg2FGos3H2fpurfVkQvKtJJjdInxOJ_g5YRF-4yiTyXXTSo-OcSwLJaSjgEiSeVh3OOtRnViQIN6o4nF3d9Xqgug7pki8VDIHkY6us4A8yT8Vhp6pYpuBq2ULGvsf2caLG1rwX3IQ7CbNYA1wbpLG4_ci2qgpzqIqW9HslLuNna5WX0LT-eCspxkImZdL-bgwrSm3UZRNo0zUDZKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fcd06da20a.mp4?token=bH4FuD-QrRfl1cozUI6I7iRDRdX4JrIj9k5RMN1kbfOmVWQhnkGEjSax1u5VtdLOATtS12KqosHSjTPToYq-RESpT_zgorejXuQ9HWLnWD3Tyk2C4ikzc5Q0Td2AmxzyGLCYRvg2FGos3H2fpurfVkQvKtJJjdInxOJ_g5YRF-4yiTyXXTSo-OcSwLJaSjgEiSeVh3OOtRnViQIN6o4nF3d9Xqgug7pki8VDIHkY6us4A8yT8Vhp6pYpuBq2ULGvsf2caLG1rwX3IQ7CbNYA1wbpLG4_ci2qgpzqIqW9HslLuNna5WX0LT-eCspxkImZdL-bgwrSm3UZRNo0zUDZKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از  لحظه وقوع انفجار روز گذشته در دمشق
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/alonews/121239" target="_blank">📅 11:55 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121238">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
بیانیه مشترک چین و روسیه:
ما از طرف‌های درگیر در خاورمیانه می‌خواهیم که وارد مذاکره شوند.
🔴
هیچ کشوری یا مردمی درجه یک نیست و سلطه به هر شکلی غیرقابل قبول است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/121238" target="_blank">📅 11:51 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121237">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
دو نفتکش چینی پس از دو ماه معطلی در خلیج فارس، روز چهارشنبه از تنگه هرمز عبور کردند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/alonews/121237" target="_blank">📅 11:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121236">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
کشت خشخاش ممنوع شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/alonews/121236" target="_blank">📅 11:43 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121235">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
پژمان جمشیدی از اتهام آدم ربایی و تجاوز به عنف تبرئه شده و به دلیل رابطه نامشروع به ۹۹ ضربه شلاق محکوم شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/alonews/121235" target="_blank">📅 11:38 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121234">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dImrfMTGQZwYM1BY29q5gLpazpsimrakwuBq_fJ8Vfqx4yJnNqbR0vWGGKo_9jITU4zFl31vUv5YFyDNXOgV--9p-LP7AKDjD-v7H69lW1UPS5Kx7l4ODCZ6ETi0Dl7p2jQTu41ko8GCtptPCOulNaii7kcXi9tuW0zXS3RfmNgJI61f_9oH2D17qOx14L9jhPlnwMs0ZqNmPq6_bhC6GzJ0w0x3Thx7-2irZcIdTcL6C4q8F6BQBE1MTmQHcsmAVbKeoRs4qL6yLFtQ8fOhEzRSdLq4FzhG1Wxgt9eO-Fv72k9TOsw1_f4uae1DgMQMNs2Tpzn7U-WrYio3tv9L1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی، فعال رسانه‌ای: چین دیگر تمایلی به حفظ وضعیت فعلی تنگه هرمز توسط ایران ندارد و بنظر می‌رسد به زودی در بحث تنگه هرمز رودروی ایران قرار گیرد؛ آنها معتقدند ایران باید زودتر تنگه را «تعیین تکلیف» کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/alonews/121234" target="_blank">📅 11:32 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121233">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
گویا بخشی از اموال توقیف شده علی کریمی بدون مزایده به یک شخص دیگه واگذار شده!!!!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/alonews/121233" target="_blank">📅 11:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121232">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
وزارت خارجه روسیه: ایران از «پیمان منع گسترش سلاح‌های هسته‌ای» (ان‌پی‌تی) خارج نخواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/121232" target="_blank">📅 11:23 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121231">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
الجزیره: پوتین در پکن همان استقبالی که از ترامپ شد را دریافت کرد
🔴
تنها تفاوت در این بود که چه کسی در فرودگاه از او استقبال کرد؛ این فرد در مورد ترامپ، معاون رئیس‌جمهور بود و برای پوتین، وزیر امور خارجه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/alonews/121231" target="_blank">📅 11:19 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121230">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tkC3lU2u1nNzN_uuIGBOWZpZkJDLz2hungzHiLrWEjqZS4oAPBiKT6ih8Zhi8Nwo6cbCdPpdkPosLLxo6xK1kROTfRbFnNM1dmFLjlbD9GIIwxZqbhpTVS68IKfJpVLofYLRce6jqBGbLzPjjpeBCDgEM7W2n-lXg4LIuahjd4tB7ZTCqLqPKM8PJTMjKPF_olF0D5cI1M3aS9o4id1dBo08hTaj8qnL_hsqSzK7Yf8vV6QbT8U3Mj5eVqFUgl6OiPnWkyrpqExH1m6nsK8n-bpnvJLQXQfDrgoNgOQEuosZ6nh6u_34e0TR4m5B8zDYzalwa6QaVNpBJerfz9ppuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شبکه ۱۲ اسرائیل :
- اسرائیل و آمریکا برنامه ریزی کردن احمدی‌نژاد رو به‌عنوان رهبر ایران سر کار بیارن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/121230" target="_blank">📅 11:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121229">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
سپاه پاسداران: با تکرار تجاوز دشمن، جنگ را فرامنطقه‌ای می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/121229" target="_blank">📅 11:13 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121228">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
پل مرقص، وزیر اطلاع‌رسانی لبنان در مصاحبه با «العربیه» گفت: «رئیس‌جمهور لبنان خواهان تثبیت آتش‌بس جهت موفقیت روند مذاکرات است.»
🔴
او افزود لبنان با هدف دستیابی به حقوق حاکمیتی خود با ایالات متحده آمریکا همکاری می‌کند.
این وزیر لبنانی در ادامه گفت نبیه بری، رئیس پارلمان لبنان، «لحظه‌به‌لحظه» در جریان مذاکرات با اسرائیل طی دو روز گذشته قرار داشته است.
🔴
مرقص افزود مذاکرات با اسرائیل با هماهنگی قانونی رئیس‌جمهور و نخست‌وزیر انجام می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/alonews/121228" target="_blank">📅 11:09 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121227">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XdjqP6O7g8WU8FGVPVG0smC3zabECWPvFv8s36YuTvgLZZUTmmeJzZDOU4-ln9D_G3otDbpnvF_UdZwq1NekEgN82ikLgMFalGSXqIofOZFfNGEYCADPDe9_0H352GTJ-kTei8vlIr35lqXG1Ng54I3_g9aaRcQj836KV-nRXG48GJMEk4RImBY0uX16D701UKuhpTsUmwCjw0subr3BLkl-GBxb3cL2T21htfomAtmroPx17z2jJsCkvwMzffGn9O9C6sT5B8alauFVvOiLoH_iSTQL-FP5ZWpwhQ1wH_pmw1kEkpyRjwiYypn4FMRfzKvbDbojPi8EHQMTUqRBnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رادار کلادفلر خبر از افزایش ترافیک‌ اینترنت ایران می‌دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/alonews/121227" target="_blank">📅 11:09 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121226">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/i7esQQOoRtZP82qvHdQDt2q-b0Xh_lG7kV3UEvhqhPYrnMOT8UuER5xvT1KhkGVleY3DDHo_6hR_uZJIg_bIwzFUzbNyWw4RnGIVsVLDUu4GBz0qlbqrVUii4qkO26r4juqqWw5Ul26oTRp8KHWFl7fMKR5z-s_WbAhHI_4RswgsYZOhGgbEaIqCIm2-ca9YsECl29ZUL6RY_j9n_7WfuxpXxTBLNXsfZOXk5A2_BoswsVMxnBfWxJ3FTtNXF0lGoSnRMCCFIxn-o_5KM3vkcjQcsPDb7a6dx9aKP55QLdDeeDR1G-7kema_5kEFPGVvHyt6XZ5Um5Gik3FAlPZ13g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بدون شرح
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/alonews/121226" target="_blank">📅 11:04 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121225">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qfEMBVCmtzb1tfJRmdY6S3xFUtjMoCLCE4RhQ7oZCcN3BCK1idH7dfLNZ7GmSx9aeRfz0Ibhm7eyDblgJY4kjRj29jj5ZxSASPuSnMqYdhqtoKDSqZ0u0qcc_-BqQykf_fZsktQvgn4VkDSNLEPzGMkWp9f9yDOk42YIVS6fd3QMEzEC1ZRniNdJ6u94TSMkYuCAsK_puVoU7AUGqOzfVewEoy5FBnyV3tInhn8OnSmqBvqC7vJmUFrL81jhpkJ401FJNmNAVghBu5jOEoCZ4iQFKXFYEMTW-BIp6jg0zQLLN9NYnqfn8OLIwH_5YsCgocAjbiMHCsMadhN0ixSe6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
میانجی‌های منطقه‌ای و مقامات آمریکایی به WSJ می‌گویند: موضع ایران در مذاکرات با آمریکا عمدتاً بدون تغییر نسبت به پیشنهادات قبلی باقی مانده است.
🔴
ایران همچنان خواستار پایان خصومت‌ها، تسهیلات مالی، غرامت برای خسارات جنگ و نقشی در نظارت بر تنگه هرمز است، در حالی که با خواسته‌های آمریکا برای تعطیلی یا تعلیق بلندمدت برنامه هسته‌ای خود در تضاد باقی مانده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/121225" target="_blank">📅 10:59 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121223">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
مهر: قیمت خودرو روی کاغذ کاهش یافته، اما بازار همچنان آرام نشده و انتقادها از مدیریت فروش و عدم تناسب زیرساخت‌ها با تقاضای میلیونی ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/121223" target="_blank">📅 10:55 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121222">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NqZA2K39AdRGIrdI7I0dh73Aao-8A89qI_T4pVdn32_0pj7vDHsNEW_3wt7j2liYpPc43zX29dKCvbq8vxur9VbpQ45Zk2zKgYsFKUtao65yVFd4cJs-9RQ4_3R9nZwczLLIBCQu_k8TCBNI2lOkOGfxN_lHEECzJSTlbGnB6tVqOeZ_jJDKgh4EfpQ_96GUuAukW6NAUeMuNsR7IOJy2vQygYjFeypIjCVFzlfNCu0JJ7Nvg9_nTehPK6jfRK1aGO6tJxFvKXoIJCsEjkUW6Mb8ZyUXEM60KKU8SZjJ-8Aopl3oufllmoiRW7xXQ4I7FPt4Gk2_H5kYDqrcFU4K5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رادار کلادفلر خبر از افزایش ترافیک‌ اینترنت ایران می‌دهد؛
شروعی برای موج قوی تر فیلترینگ؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/alonews/121222" target="_blank">📅 10:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121221">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
قوه قضاییه: کشت هرگونه گیاهان مخدر از جمله خشخاش مطلقاً ممنوع و جرم است و مرتکبان به مجازات قانونی محکوم می‌شوند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/alonews/121221" target="_blank">📅 10:45 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121220">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D90udZftzerKC4M1fnfLsuIWBLJN6quGE2xACyeuTbCOwNH8AWb3eNFuZ9NIcXpMyNZLIXFKLHbWB-NBwfsXhXhL0CtAtbYQgp38lAEHYvyjfsKSMcMbg0XGLu0ZRJSdu_hxQtmAwA6ziNQ2ozXytuwKhmH2JI5trUv1X2HsdPRlUr7BdPJzacrE1FG_7BLXbSA6ngjaUk0hSqdlY3eG94Lzf3usIWS1M3lWOVdUEPUVXOxBfnSzUPgnk05BzepM6jG8oIMO1hAfHCWfR0oTJnuJ7scMgY68IXq6zJG9Uq1f1_kcW-_5XPsTolYlNmL39gShzhmsdxtGpq3w2NX0ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هند با هماهنگی ایران و آمریکا از خاورمیانه نفت می‌خواهد
!
🔴
بلومبرگ: هند برای اولین بار از آغاز جنگ علیه ایران، آماده اعزام نفتکش‌ها به تنگه هرمز و بارگیری نفت و LNG از خاورمیانه است.
🔴
این اقدام با هدف کاهش بحران انرژی و کمبود سوخت انجام می‌شود، اما با هماهنگی دیپلماتیک با ایران و آمریکا همراه است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/alonews/121220" target="_blank">📅 10:42 · 30 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
