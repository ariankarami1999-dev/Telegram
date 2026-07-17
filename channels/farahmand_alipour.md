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
<img src="https://cdn4.telesco.pe/file/a2To2rU4OGHu5F6psTQpCCJB3kR6F_d95r6UGIGyyOUj7tZooyO9L6A_THi6SsNirkOQKny-dssVH85FGyZDJusGL3rMlMNdvWT6t6VvU6fXalziRvILgwWlEKscEIdrDk3-nPtakxIkwduXXtfuvr_KuNfGMe7CmbrLZlksOWx1lysnddaMalrf5_6J8NFpYzxWtb1Mlig0wqtj8GKXYTQaM7xPbP0G_4BMn7e25J9aE0QIk2R_S938MJJPmIPehrytzU5aXHXufXYtOlAanVjkOFyQkcknNZ5qByTTHaFShSWkOpFeI-8czzsKjJ-j3arn3vctNLEz5eEBYskVxg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 64.9K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-26 19:23:01</div>
<hr>

<div class="tg-post" id="msg-6188">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lvDYAVxq_VcbEn0jaAtD5W0oDdCv3M8dmdxBphtzQ5ZwVVirnEuae7sQDY784gBK6BpZHGygBOPw0ePCzEjP8oa-y21b_C8vFWf_neLyAqf_Wbd7azZZUTfH89ug8shTlr8FOJfiyueNVS0BNi_E9sxOtFj-Zr9WdrRH6t2Mx6NALQBEyBifA83N9-w67rDqsQ-p0ZkWtPrVIBSdzYdbAZQSA8jNCx7-m0U0c5ubeMLRs6Ek-tOMEEqhg4k1z2U1vhP8aJsrJfW_zhBQbml2fRWDupFkGydVYyYxuDsrZrSNuy8hEr_6_uBv2KdiOOzC0chxlBOYOHNbuxHcbjYmzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک ایستگاه مترو در تهران با مجسمه مریم و عیسی درست کردن (که عجیب هم نیست،
نصف قرآن داستان‌های مریم و عیسی
و قوم یهوده) و پروپاگاندایی راه انداختن
که ما چقدر احترام میگذاریم به بقیه مذاهب.
بعد همزمان کلیساها رو مصادره میکنن
و صدها نفر به جرم مسیحی بودن
توی زندانهای ج‌ا هستن و اجازه داشتن
یک مسجد به سنی‌ها رو هم نمیدن!</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/farahmand_alipour/6188" target="_blank">📅 18:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6187">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o23JcAiz3J-Icg3U2M2NzvMMdb40oPmFoaBYdlEUwYBjyhuN5b7h2IyB8XgQrGu_Dq7InpDe7TcU2ZambOI_wXSGPPLisXRqSm0xPvHzpWORotmFzWGypHPDRcs28w5fgyeAPgPX9tmcEit4U8j9ZNBkqD25XpgTKaBzyczAQNroCMUmhkA_u6H04mdQtYeTzyX2ghvNenOWyuC42uvE645ZfSEQuwM6bftXXPSROfKTqucxUJy8Aa9k8LJWwmH-QDEjrouQMl89LJ258sbqW6S1tVKp-PMIp46gh9b6vqZvF-z-Z8kH5YlZDHes4FG4ujPhCMiuflxA-C9mAuAtDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب طلاقش بده :)
چرا اینهمه کینه؟</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farahmand_alipour/6187" target="_blank">📅 18:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6186">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pj5r17LvhYKZPKH_z4Yr62thpiFHiUk8LiH26S0LqfbzRr4anLt-I4ZlHGmLLLokjaV7l3yCbMbH_sSwpzpoZRl_bN13-AuNvNRSDhRXn_0pWfAMFXI4j00iMQrdXOrrZlNW__UkxJ6YAYYDdIKuzjK2jXSON60UJVXKLGpSiLQs7ewG1M34omN483pt1bgKdxYdtLJ4MBnsrZGMgPCBlKZyeS0uSstBfzav_2qmMuBExOvZT22uS2fGMWylDiqDPF-rg6O1gBmACv9_Vtg-0tRr1_lFJMPu0svI6UoBFTlaJtH_Ay8aPYXXW4r5GwjOUXuhxMzY67FHpPB16lEb8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عقل عرزشی !
من میگم اینها شکست‌های تاریخ
رو پیدا میکنن و به عنوان الگوی خودشون معرفی می‌کنید باور نمیکنید :)
تنگه احد! که نماد بزرگ‌ترین شکست و عقب نشینی مسلمانان در تاریخ صدر اسلامه،
رو شباهت سازی میکنن با تنگه هرمز
‌‌میگن همونطور که اونو در سیطره داشتیم
اینو در سیطره خواهیم داشت.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farahmand_alipour/6186" target="_blank">📅 17:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6185">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d213b51da.mp4?token=uPfrkKk8qYizG85BR1VSbl9IWLI-rvnGdT79fD90EKwOsa-JZHUFfT1bF62TLgyy2fQvaAxGqAn0SD5Ls_72TBBDgS9biyzk2o4Sn3ezOvu05dsALNLZiflvH9Jwkc-uQTfkucSVvj-XGwObOQ27LaGHT4M-KNIheZTvJAslpXucMOWANBxUJAG3gZnJ4ckWB128nqx8WH1C8WS6y7bIfrTRCNxmC_RrWBrDyixJJ0wvxcXnp1y-55lLOyPJkBa21jdAtAcjuMSJKZhuklrKEHk3Gnu9jC5QLJEFu6SS22WgvOHsAA61iaSpLRYZnzfjAcTsgBC-ph6d833v-Pm7JiqJqye3zdqbbRe61tMDRcNRd1HRUc8lwStEdbQx3VVCEWyoVq17TPi-MSLx_37Wk7962pQr0S4OxJ2-XvASxtp7NIqc-E7JezT6ns4DQnxD5uhBsTg0bVd7RW3am31cclvv04Dt2y4WnbYhwSsDG-AX6qNaIcFxcydkS7L40vrePM66G5ChtNGeybD5D7xlld9u0XZP7w3ZHcv6SEa7zjHlu2EWCtEA6mxikm7Ux77QHLAfxeZN4bmdoalyYF1j902Dt_OaFkQay4ODUaKCofw0gLn0U2ls930_94RLVk95vfPBB50OdPHPiRglhSM_HTEwMZ3i0PQTxJjXc_4dd-I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d213b51da.mp4?token=uPfrkKk8qYizG85BR1VSbl9IWLI-rvnGdT79fD90EKwOsa-JZHUFfT1bF62TLgyy2fQvaAxGqAn0SD5Ls_72TBBDgS9biyzk2o4Sn3ezOvu05dsALNLZiflvH9Jwkc-uQTfkucSVvj-XGwObOQ27LaGHT4M-KNIheZTvJAslpXucMOWANBxUJAG3gZnJ4ckWB128nqx8WH1C8WS6y7bIfrTRCNxmC_RrWBrDyixJJ0wvxcXnp1y-55lLOyPJkBa21jdAtAcjuMSJKZhuklrKEHk3Gnu9jC5QLJEFu6SS22WgvOHsAA61iaSpLRYZnzfjAcTsgBC-ph6d833v-Pm7JiqJqye3zdqbbRe61tMDRcNRd1HRUc8lwStEdbQx3VVCEWyoVq17TPi-MSLx_37Wk7962pQr0S4OxJ2-XvASxtp7NIqc-E7JezT6ns4DQnxD5uhBsTg0bVd7RW3am31cclvv04Dt2y4WnbYhwSsDG-AX6qNaIcFxcydkS7L40vrePM66G5ChtNGeybD5D7xlld9u0XZP7w3ZHcv6SEa7zjHlu2EWCtEA6mxikm7Ux77QHLAfxeZN4bmdoalyYF1j902Dt_OaFkQay4ODUaKCofw0gLn0U2ls930_94RLVk95vfPBB50OdPHPiRglhSM_HTEwMZ3i0PQTxJjXc_4dd-I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کیا بودن شعار به زبان عربی میدادن؟
چی میگفتن؟ میگفتن  سرباز ایران و وطن هستیم؟
نه میگفتن «سرباز دین و عقیده» شون هستن!
و کنار لبنان هستن! و مسیرشون همیشه مقاومته!</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/6185" target="_blank">📅 15:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6184">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ijt5NRK3bltsYCoHkEWDkhrcfi5qZ--8GXUF5P3-8IK0TPqriYcGaj_rju2tJ7vUgwYsS5u9HmUMtsvwofBpwQIY_G8VauO1lhDEPE79BAXOnZcWgApkjZp8GP76Nxi2zQQ9wVFiPyWCkbhC-9yvd0w_1ZnHvvy65JIPelk236nzSTkWZJOOo82ttchl91wf8Wqd9mCD7pIa5mPzdbLXD1iNMUNym65cPe24AyUPfo20PC1xb_MnWNYdf5MmiJ0HfjfWiWjCciXf3-nfQwoVq71WQBin3R_7y7TWbh_DZcycgfxnLxzhmpI6d4g18W17wla0suaespRUpAdDgjiyJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جمهوری اسلامی به تاسیسات آب‌شیرین  و تولید برق کویت حمله کرده.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/6184" target="_blank">📅 14:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6183">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61a69b588c.mp4?token=JYCCchxyPd6A7ilQkz80EaXyVs2eEsT0foYs0LNA-hNCrlVX8uDIyd-GqnSj5S2pA-NoJCWDs722GN6rh_Ulp8FaQ0otBJuAQbmpJQ708RODUIsw74MXBXvtq7PL43Lw1-UcXriz7sjhxUJ_-S4b-ut0y0jgQ6bDNuTeQqHPL1cMhNAvReGvM30SDFNiUAhxndwwJO1AJzo07_DC2-7eu59ijUkCzJoG_7SBCDpUqnnqNyZzxS9d3tfNka8FoWGidqeZPqX2Fe-VYDqyVPpf4atEFBFm_dWFHWLR04c2eYcB5XOY4r0ClYFla4O8NDsMZLeR8uv-naHUfuY0s1njVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61a69b588c.mp4?token=JYCCchxyPd6A7ilQkz80EaXyVs2eEsT0foYs0LNA-hNCrlVX8uDIyd-GqnSj5S2pA-NoJCWDs722GN6rh_Ulp8FaQ0otBJuAQbmpJQ708RODUIsw74MXBXvtq7PL43Lw1-UcXriz7sjhxUJ_-S4b-ut0y0jgQ6bDNuTeQqHPL1cMhNAvReGvM30SDFNiUAhxndwwJO1AJzo07_DC2-7eu59ijUkCzJoG_7SBCDpUqnnqNyZzxS9d3tfNka8FoWGidqeZPqX2Fe-VYDqyVPpf4atEFBFm_dWFHWLR04c2eYcB5XOY4r0ClYFla4O8NDsMZLeR8uv-naHUfuY0s1njVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۱- ما مخالفت کردیم، بعله، کاملا درسته!  ولی آیا شما به خاطر حرف ما دیگه لبنان رو رها کردید؟ نجنگیدید؟ پول و سلاح نفرستادید؟  به خاطرش حتی موشک به اسرائیل نزدید؟  (که اونهم اومد در پاسخ ماهشهر رو زد؟)  خب جنگیدید و شکست خوردید!!! هم در لبنان،  هم ‌در سوریه…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6183" target="_blank">📅 14:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6182">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/902cf63917.mp4?token=dWf6EZTzIZf3kpUPVPuf_cAJQ7CVsy6iOkabI1WMmPrMCmbCdf3PBOIlPELF9sFx9gbVeQWwfNcuLeUa4QU_BBCUd3gKmjlXvyZUZ08cBKj3nLAez_ENdXELSOpAIVZNTLgqL16rT199nbBMNVKcJtyIotZqRlVoIcu0OJ2cyfO-uznwRfHpz7MgJ0Ev7WFyG5nN24g6UmpbBqC-UR53wUpaTiq6S-XtObe077k_wLYzVjMumFAoJYCYg8FtdIrvQhkOV08qxdLb2Cq1z9Yq7_76v-YqTZSTTzJ8rXLZpwhRM6DHhgnsdNY7VKNLW7A-zQz65nNpv_7d9A2R3dhG9r3d8jVanJfe4kBsbvUeUUR7S09TeXOpP19Qu6UGBuaR30Q-QlCY9gEkKekSkEPOr2HoD88xfGyvODaPdd1H3ST_xupUfTkWFVxEadR6oOCxUqDjRLuBWsWsL3BaJu485qR-vQSJ96eaZRLdYqQ3y6phGUXEiLeVznHmfk8YdUlva7JDYRhAT8trRdobzd1OmEmQNlPP5HA1bTaz1-lNy6vBCFiuoLOOm93exEiOngC1zSziUSD6IXr0gqueGss_N3oTBj9jJliavg04_hkOhQ670MislNdEwnWkCsRPdvpyK2nPZfHcWtg7S039SnHp7EUjodPYTS1LKZRiu5vjTFM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/902cf63917.mp4?token=dWf6EZTzIZf3kpUPVPuf_cAJQ7CVsy6iOkabI1WMmPrMCmbCdf3PBOIlPELF9sFx9gbVeQWwfNcuLeUa4QU_BBCUd3gKmjlXvyZUZ08cBKj3nLAez_ENdXELSOpAIVZNTLgqL16rT199nbBMNVKcJtyIotZqRlVoIcu0OJ2cyfO-uznwRfHpz7MgJ0Ev7WFyG5nN24g6UmpbBqC-UR53wUpaTiq6S-XtObe077k_wLYzVjMumFAoJYCYg8FtdIrvQhkOV08qxdLb2Cq1z9Yq7_76v-YqTZSTTzJ8rXLZpwhRM6DHhgnsdNY7VKNLW7A-zQz65nNpv_7d9A2R3dhG9r3d8jVanJfe4kBsbvUeUUR7S09TeXOpP19Qu6UGBuaR30Q-QlCY9gEkKekSkEPOr2HoD88xfGyvODaPdd1H3ST_xupUfTkWFVxEadR6oOCxUqDjRLuBWsWsL3BaJu485qR-vQSJ96eaZRLdYqQ3y6phGUXEiLeVznHmfk8YdUlva7JDYRhAT8trRdobzd1OmEmQNlPP5HA1bTaz1-lNy6vBCFiuoLOOm93exEiOngC1zSziUSD6IXr0gqueGss_N3oTBj9jJliavg04_hkOhQ670MislNdEwnWkCsRPdvpyK2nPZfHcWtg7S039SnHp7EUjodPYTS1LKZRiu5vjTFM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۱- ما مخالفت کردیم، بعله، کاملا درسته!
ولی آیا شما به خاطر حرف ما دیگه لبنان رو رها کردید؟ نجنگیدید؟ پول و سلاح نفرستادید؟
به خاطرش حتی موشک به اسرائیل نزدید؟
(که اونهم اومد در پاسخ ماهشهر رو زد؟)
خب جنگیدید و شکست خوردید!!!
هم در لبنان،
هم ‌در سوریه هم در غزه به مردم گوش ندادید
جنگیدید و شکست خوردید!
۲- اتفاقا چون رفتید توی لبنان و غزه و…… دنبال کشیدن «دیوارهای آتشین» علیه اسرائیل و نابودی اسرائیل بودید، و افتخار میکردید که  بهشون
موشک میدید، از طرف دیگه دنبال اتم
و هسته‌ای بودید، اومدن و ایران رو زدن!
هم اونجا شکست خوردید و شهرهاشون نابود شدند
هم ایران داره نابود میشه!
نتیجه ۴۷ سال اسرائیل و آمریکا ستیزی شما!</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/6182" target="_blank">📅 14:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6181">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72c58aa42b.mp4?token=BMKZk7d4TR23meNbWRX1PGkNu2Mn9teJhV2hIIhgRKy1SYX3rYHnGJAe8gGLd8D-PtWThWt7VYClK57lxResftgq0XPtbYAL56vh_8i4GGHrZ7vk8jjA2rUykCAgxcHGOepVtRIBP1_AiCyL2QWAh5RUq-gz76N9Ndey5V3ubO5EskhcL07BziIP2yR5LeDRGNyBaCzLtY-WCf5mKaFPfxjjjm6MuKqHWf2uTCUwTD16N2PKWvztZIOSq7HKJWcB3ap0DVc5AfCgq7ymGNbcbJLKYgFlYuTVmrLWccrNTcyYjrVRnu5bzy8Q9reFPl7XebH7z-qOncChdI-sImZ6Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72c58aa42b.mp4?token=BMKZk7d4TR23meNbWRX1PGkNu2Mn9teJhV2hIIhgRKy1SYX3rYHnGJAe8gGLd8D-PtWThWt7VYClK57lxResftgq0XPtbYAL56vh_8i4GGHrZ7vk8jjA2rUykCAgxcHGOepVtRIBP1_AiCyL2QWAh5RUq-gz76N9Ndey5V3ubO5EskhcL07BziIP2yR5LeDRGNyBaCzLtY-WCf5mKaFPfxjjjm6MuKqHWf2uTCUwTD16N2PKWvztZIOSq7HKJWcB3ap0DVc5AfCgq7ymGNbcbJLKYgFlYuTVmrLWccrNTcyYjrVRnu5bzy8Q9reFPl7XebH7z-qOncChdI-sImZ6Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حکومت وراثتی بود
یکی می‌مرد یکی رو به جای خودش
معین می‌کرد
مردم هیچ نقشی نداشتن!
میخواستن، نمیخواستن باید قبول میکردن.
🔺
خودش چطور رهبر شد؟
با نقل یک جمله شفاهی از خمینی!
گفتیم بعد از شما چه کنیم؟
گفت : همین آقای خامنه‌ای»
🔺
حکومت وراثتی بود : مثل پسرش مجتبا!</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6181" target="_blank">📅 13:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6180">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BdWJgw0PLVMOxf50UHNevQWUOdCA1CdoPX_0z9iz-k6WtSxMwBr-aofRD7f9ll804XH6DaZJ1ELPMlMpuhOQnPKs8JyErM6SWhuaCnSujCteOBMVuvkNkNqsxjOXPXySGGOdgs5Wed63LZG86_J18AVtM37nK8R9JL2eln5jndKb_Z2F0Mk6GRCcGBIBmjQI3MHl6PmdvkwKaEc1wqoPtN2NrIi7CnCROH_ihPKlNdTdlLFiPa-EfnTyD2FmHRdh3vsEarEd2154QrYQ6vziE-pVQ7MiObpIamq4JpHZvvkfnLFujZqg-RUS6KcumrSZuy2CxkqlN2y7LDvTImj9yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تاریخ هزار سال پیش نیست!
که هر چی دوست دارند روایت می‌کنند.
داستان همین روزها و جلوی چشم همه ماست!
گروهی برای خونخواهی خامنه‌ای
دست به حمله به اسرائیل زدند،
اسرائیل برگشت و ضربه‌ای بهشون زد
که یک میلیون نفرشون آواره شدن!
و همین امروز و بعد از ۵ ماه، هنوز نیمی از این افراد آواره هستند!
۴ هزار نفرشون از جمله ۷۰۰ کودک کشته شدن (خود قالیباف و خود حکومت گفتن اینها برای جمهوری اسلامی کشته شدند)
بخش بزرگی از جنوب لبنان رفت
زیر چکمه سربازان اسرائیل،
رهبرانشون حذف شدند.
دستاوردش چی بود؟ افتادن به التماس
و زور و خواهش برای «آتش‌بس»!
الان میگن این «اسوه و الگوی مبارزه دلیران» است!
این اتفاقا آینه عبرت و نتیجه گنده‌گویان‌است!</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6180" target="_blank">📅 11:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6179">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d198d21980.mp4?token=KeLG4nrvOcrqw-ecUqQOZjSOFgxI5lJUni0cj1I4CP_UmpVt6El2b4Vn5tlOU31g3IOrk0-Z1D97UPEpNklg-SHmFK6ffKyH6yeZikVerP727AvhcXT3H_Rzrhjt3aDOJrWQrXOUU_uTABlVCDUTfmU0WZ16YoDv5GwjB403ZpdvA4qBKYr0CHXbb4AOkeiDt7W10XBJtYLrlq6yKpnplbDPed3A25hY_4wtEZLLCvATOsZTMHJ1mw9I4bBu3Al9cDGz8CbHpWsyJ1-L6Lt_S9mxwk8NRLezuwltOpeIopju7RKYAx7qGxJmxvKsH1BLnygm4M_Z-f7KMSIpnJehi4EroRuWm019d0RI5KVYJ8zkTnauORUvWhE3jsZt6U3dag6wVozCG1SkHLbOwVvktRSWMZQ1CtEcwA2qQfVOuenpO0VNN3iOT2NIiWwA2k88zywPdaOew_zzPpxfx4xWQt3ZeQ35Y2TlX03zqu2uh3bRU86xKa5mRW7o2i8VuUamuXIucXM5u252JvoVGB9WupXSWZsTf1Vhtj9NfVwygQ0lw-O1GSp9L5Za6be25TK00b9gdIblzB_LWSysxnagzjyI0e2_WNsWxWyIInOl03JXnCbJOpZvh1H1xREiUia1rkNRscZmbSLcQRiYbVl_B9RdGspN1nLKsC8VCBLIlu4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d198d21980.mp4?token=KeLG4nrvOcrqw-ecUqQOZjSOFgxI5lJUni0cj1I4CP_UmpVt6El2b4Vn5tlOU31g3IOrk0-Z1D97UPEpNklg-SHmFK6ffKyH6yeZikVerP727AvhcXT3H_Rzrhjt3aDOJrWQrXOUU_uTABlVCDUTfmU0WZ16YoDv5GwjB403ZpdvA4qBKYr0CHXbb4AOkeiDt7W10XBJtYLrlq6yKpnplbDPed3A25hY_4wtEZLLCvATOsZTMHJ1mw9I4bBu3Al9cDGz8CbHpWsyJ1-L6Lt_S9mxwk8NRLezuwltOpeIopju7RKYAx7qGxJmxvKsH1BLnygm4M_Z-f7KMSIpnJehi4EroRuWm019d0RI5KVYJ8zkTnauORUvWhE3jsZt6U3dag6wVozCG1SkHLbOwVvktRSWMZQ1CtEcwA2qQfVOuenpO0VNN3iOT2NIiWwA2k88zywPdaOew_zzPpxfx4xWQt3ZeQ35Y2TlX03zqu2uh3bRU86xKa5mRW7o2i8VuUamuXIucXM5u252JvoVGB9WupXSWZsTf1Vhtj9NfVwygQ0lw-O1GSp9L5Za6be25TK00b9gdIblzB_LWSysxnagzjyI0e2_WNsWxWyIInOl03JXnCbJOpZvh1H1xREiUia1rkNRscZmbSLcQRiYbVl_B9RdGspN1nLKsC8VCBLIlu4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو‌شب پیش شعار میدادن که
:
«
جنوب ایران نکند جنوب لبنان شود»!
حالا دیشب شعار دادن
«جنوب لبنان و جنوب ایران
اسوه! رزم همه دلیران! »
خودشون می‌دونن جنوب لبنان ویرانه است و
مر‌دمش هم‌ آواره! فعلا هم زیر چکمه‌های سربازان ارتش اسرائیله. برای همین اولش میگفتن
«نکنه مثل جنوب لبنان بشیم!»
حالا میخوان هندونه بگذارن که جنوب ایران «اسوه رزم » است و برید جلو!! بشو شبیه جنوب لبنان!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6179" target="_blank">📅 09:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6178">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26ef12b93f.mp4?token=gQaoAYWVaDThIrFT6v0SMdZMNkx4TA3jclUzJzT9SgLoVyYvzuBAs6Gqhy-_N1k277GGoVX_IbMcnKXIi2CDlrcALulHj5YDfNCoc5xEiJmSd-oCVl67n9jjSyZmYi0GvVBmGcUzDtZOUCBay9OlrZL-K82Y7uepqgS64LBzJHQ9T2STfxdAwJyXZOvWXqob52USmf2qIcnLulhQS5Nx2tPylu74o9IGWjepVmiuJHO9Dm0DqB6uePJagxSEdy8Tpqe3kmyGHlbVpYfzZvIFNgyCM44qLm0sepNM26eUD5tGSKyO_EX3uoUX02PkJRi-qDv_EmDegjDMFWulTVmJPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26ef12b93f.mp4?token=gQaoAYWVaDThIrFT6v0SMdZMNkx4TA3jclUzJzT9SgLoVyYvzuBAs6Gqhy-_N1k277GGoVX_IbMcnKXIi2CDlrcALulHj5YDfNCoc5xEiJmSd-oCVl67n9jjSyZmYi0GvVBmGcUzDtZOUCBay9OlrZL-K82Y7uepqgS64LBzJHQ9T2STfxdAwJyXZOvWXqob52USmf2qIcnLulhQS5Nx2tPylu74o9IGWjepVmiuJHO9Dm0DqB6uePJagxSEdy8Tpqe3kmyGHlbVpYfzZvIFNgyCM44qLm0sepNM26eUD5tGSKyO_EX3uoUX02PkJRi-qDv_EmDegjDMFWulTVmJPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادی از سخنان سردار نقدی : اگه حتی به آمریکا حمله کنیم، قدرت پاسخ‌گویی هم ندارند!
با کدام پشتوانه اقتصادی میخواهند بجنگند؟ با کدام پشتوانه مردمی خودشان؟ همه جا در محاصره ما هستند.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6178" target="_blank">📅 08:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6177">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d050ea81f.mp4?token=GXFlQQbFMPL99OuKitmuYM7_gpOlEx2qvvIZ7PIOj8YGh4HIcm7Qf9a69gzckHFe2P6Rybhsfz85WWpn_UYp4cVW7Rl9b56DHYLZDncL0Faokm3P68zdXk2GDl8lju5GUM8ZYPRXODiqbeJojQDpsoS49r5oL07Gu3sQ_kciZ96BimKoCZnS-ciA_qz1mF_86f_hO-Jcorra3AJ8-nsM2eRkUGgFB2pjk_giCybNORsGxvGwwGxWkoiG1hpTKxYs__RiD87pTTElgON6_LsxkvLS1nohQtEmgs4QwKdwG5uS9_n6RIKT5PPvOgpRaX8uecZdxrTHU7CpjWftT5smiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d050ea81f.mp4?token=GXFlQQbFMPL99OuKitmuYM7_gpOlEx2qvvIZ7PIOj8YGh4HIcm7Qf9a69gzckHFe2P6Rybhsfz85WWpn_UYp4cVW7Rl9b56DHYLZDncL0Faokm3P68zdXk2GDl8lju5GUM8ZYPRXODiqbeJojQDpsoS49r5oL07Gu3sQ_kciZ96BimKoCZnS-ciA_qz1mF_86f_hO-Jcorra3AJ8-nsM2eRkUGgFB2pjk_giCybNORsGxvGwwGxWkoiG1hpTKxYs__RiD87pTTElgON6_LsxkvLS1nohQtEmgs4QwKdwG5uS9_n6RIKT5PPvOgpRaX8uecZdxrTHU7CpjWftT5smiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پل  کهورستان در اطراف بندرعباس
که شب گذشته مورد حمله ارتش آمریکا قرار گرفت</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6177" target="_blank">📅 08:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6176">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔺
معاون استانداری بوشهر:  شب گذشته ارتش آمریکا با چند موشک به پایگاه‌های هوایی و دریایی بوشهر حمله کرد.
🔺
خبرنگار صداوسیما: دیشب به تأسیسات برق و مخزن سوخت فرودگاه ایرانشهر حمله شد.
🔺
دیشب ۶ پل مورد حمله قرار گرفت از جمله پل‌های رفت و برگشت بندرعباس - لار …</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6176" target="_blank">📅 08:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6175">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U0U_EV03l6hN6fSBEloHRSMdXvt-AQDCrioxAxL4daN53gLeS-G7IFuIYwMoYav9-xYxxZ8R0sedGTqwv0UFQF70JII-VgEczb2WO78y2luNQF-gXaJlpsJKT-EgQzhHLg64ATmrbTb6ZjTAB0f0nqgiJWFliHaxon2Q1WooQ0fuXxqZawswNYwktM-TNXowcq8t4w8WABfe7V76bob581Kp0Ptut1kVh4zljFIQS_YZJngZ4mg1vEJGmiU3FKnnzM5LesiOR6Y3EIhmBll4IwvzqweOgWXWBDEyXHXJJYDCN2wJGCZFh6OAJV9Vgy1rhuXzEf9JkeG3xHRRYhMk1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
معاون استانداری بوشهر:  شب گذشته ارتش آمریکا با چند موشک به پایگاه‌های هوایی و دریایی بوشهر حمله کرد.
🔺
خبرنگار صداوسیما: دیشب به تأسیسات برق و مخزن سوخت فرودگاه ایرانشهر حمله شد.
🔺
دیشب ۶ پل مورد حمله قرار گرفت از جمله پل‌های رفت و برگشت بندرعباس - لار - شیراز
🔺
تعداد کشته‌های حمله به پل‌های بندر خمیر به ۷ نفر افزایش یافت
🔺
تفنگداران آمریکا : یک نفتکش ایرانی را توقیف کردیم.
🔺
دیشب برای نخستین بار جمهوری اسلامی به خاک سوریه هم حمله کرد، هدف : پایگاه آمریکایی در التنف
🚨
تصویر : آمریکا برای سومین بار به برج مراقبت دریایی چابهار حمله کرد و این بار آنرا منهم کرد.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6175" target="_blank">📅 08:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6174">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
حملات شدید به بوشهر</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6174" target="_blank">📅 01:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6173">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0adb998b26.mp4?token=rd13S5pp3Kce2cy9fpX1B_3zEhMs-C1kBcIzJxS1W10WbsOI4Zl5yMm6F_yeys6DbAZEWPTSeHC5tQZj208lKrKKqpufGoLsElX9B44vrWhqGk_2emnFfS1GGMgXrNpIKkOP4CA0Do1etuFX_ITx412w9AeVaNzJEkEKCuEYOibKHDvYJggvv18-gu78UagO_75uaTEVCABDih44ovev7qxpfBNLdXktrjvNFLfLKv5AAi3ZSoiruio6xY1VtxnvTGdSFbxwqs0B1ZW1V8dqhlvHo8CE5uxYGm48SfztDYa5QdB8XbXUIKunTFMFOmh4OxNKB-QZrEohR_8lqFrS3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0adb998b26.mp4?token=rd13S5pp3Kce2cy9fpX1B_3zEhMs-C1kBcIzJxS1W10WbsOI4Zl5yMm6F_yeys6DbAZEWPTSeHC5tQZj208lKrKKqpufGoLsElX9B44vrWhqGk_2emnFfS1GGMgXrNpIKkOP4CA0Do1etuFX_ITx412w9AeVaNzJEkEKCuEYOibKHDvYJggvv18-gu78UagO_75uaTEVCABDih44ovev7qxpfBNLdXktrjvNFLfLKv5AAi3ZSoiruio6xY1VtxnvTGdSFbxwqs0B1ZW1V8dqhlvHo8CE5uxYGm48SfztDYa5QdB8XbXUIKunTFMFOmh4OxNKB-QZrEohR_8lqFrS3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏فارس: جزییات حملۀ   آمریکا به پل‌هایی در شهرستان خمیر؛ ۲ نفر شهید و ۴ نفر مجروح شدند</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6173" target="_blank">📅 00:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6172">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iYCu8XrF-1WqfnO07o-fr9OaKRkYH1w8FqQMzfE9ZZDlMdXe3zyxME8VlPcIdomEPmFYv6E6wgnaYe7qNwZ1AyBqGhZuogz80itTU6NtXBkS0y3gAjYL9gwZ55u7zFKCD9SOlrEVg1hYxeeZexZNr89hUAV9Ifaeqa2MaFh0Q6F_h8Cp-J3H_r2I_g6ZwkFRUt1kWI6L1SKqFJAv_IbJMHdEt9vwTzRYkyv6bY55NmmA_mcih6bOVpyK58g9LTH4SEY_vNrImKx_28PZV2h7RRdQsvVwPblwpLzBdEeugkG3pRXNeHeyQ1oHW1hZBvzV8IVIABR6U_YGDiHuKssflA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله به یک پل در اطراف بندرعباس خبرگزاری‌های داخلی : پل ارتباطی بندرعباس و لار و شیراز  بود.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6172" target="_blank">📅 00:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6171">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
صدا و سیما :دقایقی پیش ایستگاه انشعاب راه آهن بندرعباس از سوی دشمن آمریکایی هدف قرار گرفته شده و ۲ هموطن مصدوم شدند.
بندرعباس مهم‌ترین دروازه واردات و صادرات کشور است و شبکه ریلی بخش بزرگی از این حمل و نقل را بر عهده دارد.
این حمله می‌تواند به حمل و نقل کالا ضربه بزند و به آن اختلال وارد کند،</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6171" target="_blank">📅 00:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6170">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
حملات گسترده به حمیدیه و شوش در خوزستان</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6170" target="_blank">📅 23:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6169">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
حمله جنگنده‌های آمریکایی به فرودگاه ایرانشهر</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6169" target="_blank">📅 23:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6168">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/067abcc49e.mp4?token=tfnr8iEAbRWO9GfT1g7y8Rs-07Suzc8Vs2HzBlf-976hUKdkcpDQfiBxlwTlt3a-NiNBfNIz6ATLAM5jWm8JaesTXoScKuEtD6TVIPhW_GjZcNfcbJ6Xn-xPhoZ99dms1cEyF7WTyYPOw925smhbVg5bw40eqNbG28u_0vw65O2JX-9g-apoCKn4KBGLmnIgOFDWqMqFwXQjMK3fB58zm4ydRkrPYmzwp-07_7jCdNBTmaaRfhHtMS6gMjqTm3Y1jrRCIcWs_mfyo1y6gmAScqlQ6En5qXyVHcvHipc06Lyo09lqc8R9VA6UyqOd0XzbFY5wmkeN9uG_EeYjcIqryQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/067abcc49e.mp4?token=tfnr8iEAbRWO9GfT1g7y8Rs-07Suzc8Vs2HzBlf-976hUKdkcpDQfiBxlwTlt3a-NiNBfNIz6ATLAM5jWm8JaesTXoScKuEtD6TVIPhW_GjZcNfcbJ6Xn-xPhoZ99dms1cEyF7WTyYPOw925smhbVg5bw40eqNbG28u_0vw65O2JX-9g-apoCKn4KBGLmnIgOFDWqMqFwXQjMK3fB58zm4ydRkrPYmzwp-07_7jCdNBTmaaRfhHtMS6gMjqTm3Y1jrRCIcWs_mfyo1y6gmAScqlQ6En5qXyVHcvHipc06Lyo09lqc8R9VA6UyqOd0XzbFY5wmkeN9uG_EeYjcIqryQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حمله به یک پل در اطراف بندرعباس
خبرگزاری‌های داخلی : پل ارتباطی بندرعباس و لار و شیراز  بود.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6168" target="_blank">📅 23:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6167">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ocUvZInmXSgxOFR_PkkilUcR6lyDAdV74ZT8NWKgyv1oIgBPLnO_rDXZkuKDAxp4IFbybmmZj22RdK5ILR-kfn97u2bAGkbDZ1RcjdrjgVsMu4mb1eC9Y8_sctIdIhKeDUJdBiEV26gvb0eGq0E5VM1a8jE05TFg-zm4bhFH8F0VtD_fvtQVEZa0A6Fwx0KH8QkXtpbheu3-bZtskLP8O4SJnqgJfZH27xXhOFIDd9YtOCpNHfuEw8cE9J9c5qnFjpAF8S_Iu-HB7VRQoZPQ_0fV_Hx6PpXSTEhGZTnFMcWWRNWNizB18L5VMJ86wZqPPRfOlenrWrUI3w0mESdJgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اهواز تحت حمله شدید
حداقل پنج انفجار مهیب در اهواز
🔺
انفجارهای مجدد در بندرعباس  و قشم
🔺
انفجار در بهبهان
🔺
انفجار در بوشهر</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6167" target="_blank">📅 22:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6166">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48c1ef79b3.mp4?token=LXRsHH098X_PPLHNsr8LbzsLbmM5xmd4gYwgYx4nGjD6R2Ezi41QGl8ljq6Dlh7JdvQHBYapQNNQJ2OOMlGW4T0uHjomPs_mx25r-OHVJmVxBVcBd3E7eXTHzX70kWrmbph_e6IKrFaXUgYO8O573Ks161Ap6MAXONtEPCxmSObwBFDYS7rdoeWfB26BHFxaDzbe0WVSHhrN_Y-6XF3Cy0ATb3wZ-qjw6EUFw2MlzO-YcJHRWqnhM-p-vwo6j5cfgxEuNuWHAo71W3A3cKG8elyowtdpyo3vwWWCGo4-746EramtLQk9YwHb1cufdBBv8nhKh2gDV58t7-oH7idKFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48c1ef79b3.mp4?token=LXRsHH098X_PPLHNsr8LbzsLbmM5xmd4gYwgYx4nGjD6R2Ezi41QGl8ljq6Dlh7JdvQHBYapQNNQJ2OOMlGW4T0uHjomPs_mx25r-OHVJmVxBVcBd3E7eXTHzX70kWrmbph_e6IKrFaXUgYO8O573Ks161Ap6MAXONtEPCxmSObwBFDYS7rdoeWfB26BHFxaDzbe0WVSHhrN_Y-6XF3Cy0ATb3wZ-qjw6EUFw2MlzO-YcJHRWqnhM-p-vwo6j5cfgxEuNuWHAo71W3A3cKG8elyowtdpyo3vwWWCGo4-746EramtLQk9YwHb1cufdBBv8nhKh2gDV58t7-oH7idKFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئویی که گفته می‌شود
از حملات امشب به بندرعباس است.
دقایقی پیش بندرعباس ۴ بار مورد حمله
قرار گرفت.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6166" target="_blank">📅 22:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6165">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">‏
🚨
🚨
سنتکام: موج جدید حملات در پنجمین شب پیاپی را شروع کردیم.
🚨
مهر: حمله مجدد آمریکا بندرعباس
در ساعت ۲۱:۳۵ نقاطی در بندرعباس مورد اصابت قرار گرفت.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6165" target="_blank">📅 21:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6164">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbd6cb3b5f.mp4?token=WX1infyWrhnDLsqCWkTQmMeT_3Lis4yxXZs3AR7NGq5INhOAnfzv1UXQMT1ZdZb70pveFn9qkidT8bm5FfdkWbQL5yj65RR3xB7qmG5xjDK-ARebtp0uaLjext_MX1TtybCj3rwszwl29mfyiH3KtjAt0zrakfXt151pTapuOLlXli6UnSEArqThC1vOaTGonLX_zBMTZcwSLuEYu1KAF7SZx8HNuy6BxaSRJeqvZVawA64vU5LALaX861r3tot0_OueRdLb5KddDPMkMDuxV-3fohgTye6pNWGAZuC6w84hsFeuTmtxdHgg1evs3oK_Xk6-ePJXMGbVXIg1ypSmsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbd6cb3b5f.mp4?token=WX1infyWrhnDLsqCWkTQmMeT_3Lis4yxXZs3AR7NGq5INhOAnfzv1UXQMT1ZdZb70pveFn9qkidT8bm5FfdkWbQL5yj65RR3xB7qmG5xjDK-ARebtp0uaLjext_MX1TtybCj3rwszwl29mfyiH3KtjAt0zrakfXt151pTapuOLlXli6UnSEArqThC1vOaTGonLX_zBMTZcwSLuEYu1KAF7SZx8HNuy6BxaSRJeqvZVawA64vU5LALaX861r3tot0_OueRdLb5KddDPMkMDuxV-3fohgTye6pNWGAZuC6w84hsFeuTmtxdHgg1evs3oK_Xk6-ePJXMGbVXIg1ypSmsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ازغدی : اگر میخواهیم اغتشاش نشود
باید با آمریکا مبارزه کنیم
(که حواس مردم به جنگ پرت بشه
و تقصیر کاستی‌های حکومت بیفته پای جنگ
و دوباره جنگ بشه «نعمت» !)</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6164" target="_blank">📅 21:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6163">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
استانداری هرمزگان:  در ساعت ۱۸:۱۰ امروز نقطاتی در قشم مورد اصابت موشک‌های آمریکایی قرار گرفت.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6163" target="_blank">📅 19:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6162">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SiM-GpuMQPlqppMGO1sxv28I0NbKjnZ2alg0-x0h-4epoHRgnXjuI2kgvBqdwXC6QEDLYGcQMbbxn5Yb9R04HVrrn6-GUTEFJ1pChu5kg4jM7mTbwuauuk104fFiSQGN3IORbsLOj5MihDQupuTzlcRgROrlS5RP4t9iprIwJbQlmzYPfM2Tapfhg6nDGjDcvhTGxZN7xbvvQ7WSuFe7Kdg8ckDu9MH9qcs5WsNJU51ZyA9V-GlrlnbVFpmFwyCwJoYCSXjAZRWUXue8adSgfZ_ijJHhjpe7pMFnMpzYrqltzurA6z3yhxK13LmPtgzkXXypxdmOKdwrryHKH9EpXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رویترز :
پاکستان به ایران هشدار داده‌ که اگر به عربستان سعودی حمله کند، پاکستان آن را حمله‌ای علیه خود خواهد دانست و اعلام کرده‌: «این خط قرمز ماست.
»
پاکستان و عربستان قرارداد پیمان دفاعی مشترک دارند که بر اساس آن حمله به هر کدام ، حمله به دیگری تلقی می‌شود.
🔺
برخی اعتقاد دارند که یکی از انگیزه‌های اصلی تلاش پاکستان برای میانجی‌گری میان ج‌ا و آمریکا ، نگرانی از وقوع جنگی است که دامنه‌اش به عربستان برسد و پاکستان را ناچار به ورود به این جنگ کند.
اینک که تفاهم نامه کنار رفته، پاکستان بیش از پیش نگران این موضوع است.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6162" target="_blank">📅 19:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6161">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
استانداری هرمزگان:
در ساعت ۱۸:۱۰ امروز نقطاتی در قشم مورد اصابت موشک‌های آمریکایی قرار گرفت.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6161" target="_blank">📅 19:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6160">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0a471388f.mp4?token=odTYSqMApeFPY7Ws3LYwEdDtCr4PAKpc1WF1v41-WwRQj1NXA8Mawe5r73_NVLAA-ZigfSxih1AzPsgWKZ3wV-Jer8RxRTaYiWCzoqCEE-CPfYExgiAu8607-nRwlUUMl0QjSs-Iie3V4kXOr4ZTGE6ZOJJQBXEvbN5ptDZy1o5-Nv3caKCdEPT1OZFkr4wWjao8NjA9M4raaS-SrrCqyvdHvwjMu4ulWkfw18RHTMraOIjLHqbjQLEGURy8gF2JFXjEbw6GBubCwF6_s_Mx5qZw9cmuE9ApKhe1tImAqvx_DCPwA7NXWDaQ-3lKfUo75XCR3igaax7aAZVP820Oa0ye_f7TyL59NqAviB7sa0DfAJtmSChKD9UPPWIpCjqNXNnR6zoMn2ps-mfwyGtU2JXX2l7JIGvW4NFBP6I064n56Xe7R56wNrtiSw8z25TcIgQV-ejUDB8FrK1eQjPzrYhEegP5A3-yo-SO8V4WR7WUXqxwY656CTO5gjZ8xn-5BcK62bLLXdkLjTJ4_9oECOvOJ8aMPrrc2gF7y41jMcdnwM0AA56w-WVxg7u58XHfNOiRY9hQgFqX9y7JRuuHuYk8xrxN0h3OYnGpD3ZbvL1z5YLu0iAFATmdV2nzI6ktvIXlxBJCgSWuJ169T15GOIqhnmmFjNTD3rHgGIkj4vo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0a471388f.mp4?token=odTYSqMApeFPY7Ws3LYwEdDtCr4PAKpc1WF1v41-WwRQj1NXA8Mawe5r73_NVLAA-ZigfSxih1AzPsgWKZ3wV-Jer8RxRTaYiWCzoqCEE-CPfYExgiAu8607-nRwlUUMl0QjSs-Iie3V4kXOr4ZTGE6ZOJJQBXEvbN5ptDZy1o5-Nv3caKCdEPT1OZFkr4wWjao8NjA9M4raaS-SrrCqyvdHvwjMu4ulWkfw18RHTMraOIjLHqbjQLEGURy8gF2JFXjEbw6GBubCwF6_s_Mx5qZw9cmuE9ApKhe1tImAqvx_DCPwA7NXWDaQ-3lKfUo75XCR3igaax7aAZVP820Oa0ye_f7TyL59NqAviB7sa0DfAJtmSChKD9UPPWIpCjqNXNnR6zoMn2ps-mfwyGtU2JXX2l7JIGvW4NFBP6I064n56Xe7R56wNrtiSw8z25TcIgQV-ejUDB8FrK1eQjPzrYhEegP5A3-yo-SO8V4WR7WUXqxwY656CTO5gjZ8xn-5BcK62bLLXdkLjTJ4_9oECOvOJ8aMPrrc2gF7y41jMcdnwM0AA56w-WVxg7u58XHfNOiRY9hQgFqX9y7JRuuHuYk8xrxN0h3OYnGpD3ZbvL1z5YLu0iAFATmdV2nzI6ktvIXlxBJCgSWuJ169T15GOIqhnmmFjNTD3rHgGIkj4vo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنرنمایی جدید جمهوری اسلامی</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6160" target="_blank">📅 19:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6159">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfb27a8797.mp4?token=PQuPanN9rQm4n6XWz06dKt6-J0HpFWhsg9NDnysl8SpNfu-ukpx6PafkrR3q6A36DiODFDk5PwWTbaf0KO8PGFEcOwTlBQiJMsOwXhCgTUhtuRCtCw59YZC6Gj_sgjDBKGJL9nBagbj-cWYwM6oOHOtoIfPHt32Dx4IfmyRdcjhJljWW3p0KQuIdAWWdxtdnhXM5z3iXGLQKmXc1KbARcjJxXOxJEzQRemPnyPM5E-yvPzZBzKRQHSZ-MX2GMs-knfzcAqfxR5lyN8mT8PUknV3fpH8Pq4ohXiD_92HWGMZh5xeU5H7xt_VFn6FqM5HJ0Dv616lIkqGGqIpFVvFmnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfb27a8797.mp4?token=PQuPanN9rQm4n6XWz06dKt6-J0HpFWhsg9NDnysl8SpNfu-ukpx6PafkrR3q6A36DiODFDk5PwWTbaf0KO8PGFEcOwTlBQiJMsOwXhCgTUhtuRCtCw59YZC6Gj_sgjDBKGJL9nBagbj-cWYwM6oOHOtoIfPHt32Dx4IfmyRdcjhJljWW3p0KQuIdAWWdxtdnhXM5z3iXGLQKmXc1KbARcjJxXOxJEzQRemPnyPM5E-yvPzZBzKRQHSZ-MX2GMs-knfzcAqfxR5lyN8mT8PUknV3fpH8Pq4ohXiD_92HWGMZh5xeU5H7xt_VFn6FqM5HJ0Dv616lIkqGGqIpFVvFmnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر قالیباف، تیر ۱۴۰۳:
ما غنی‌سازی را ۲۰ درصد کردیم جنگ شد؟ ۶۰ درصد کردیم جنگ شد؟
hafezeh_tarikhi</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6159" target="_blank">📅 18:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6158">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ایران که ۴۷ ساله که در آتش فتنه اینها می‌سوزه</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6158" target="_blank">📅 17:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6157">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">سخنگوی قرارگاه خاتم : هر چه در منطقه سالم مانده از نجابت جمهوری اسلامی است!
ذوالفقاری: «همه آنچه که بنا به نجابت ایران هنوز سالم مانده، یعنی تمامی زیرساخت‌ها در منطقه، زیر ضربات پولادین نیروهای مسلح مقتدر جمهوری اسلامی در هم کوبیده خواهد شد؛ آن‌چنان که اثری از آن‌ها بر جای نماند و گویی از ابتدا وجود نداشته‌اند.»
سخنگوی قرارگاه مرکزی خاتم‌الانبیا همچنین دخالت آمریکا در تنگه هرمز را «خط قرمز شکست‌ناپذیر» جمهوری اسلامی خواند.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6157" target="_blank">📅 15:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6156">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ca0d3dd94.mp4?token=VWeJw8_9d89DF487kjGL0mUeWPXHLV0h9oPsZpDPY0vWTdI8Wj5wWzyztwGsQrz9htmCXatHgSSTlfZmtDiwDDcFC8yiYcW7PCnXvAFEWMdOH9vuhr53bbL1hhe2mhprrCqnSZbIfaXvoQ5wgl7mAr-BgOVMcs5-JZU8rE7D1Eg7IX41bBa_PUfzK47h9L0juImXP8s5f6tYxdTsmY21RaS1aPHmHRCz4q8_m8RaDIlBiVer5x1mHYJ5RMmJdHP3pIcbNUze4J4uD6H4BBxEwGhE3G5yXYONVYpX65-GOrLuwu2MqjmCMATaYvKke1YrIyk0NLcR7TqO4qa_zTCHbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ca0d3dd94.mp4?token=VWeJw8_9d89DF487kjGL0mUeWPXHLV0h9oPsZpDPY0vWTdI8Wj5wWzyztwGsQrz9htmCXatHgSSTlfZmtDiwDDcFC8yiYcW7PCnXvAFEWMdOH9vuhr53bbL1hhe2mhprrCqnSZbIfaXvoQ5wgl7mAr-BgOVMcs5-JZU8rE7D1Eg7IX41bBa_PUfzK47h9L0juImXP8s5f6tYxdTsmY21RaS1aPHmHRCz4q8_m8RaDIlBiVer5x1mHYJ5RMmJdHP3pIcbNUze4J4uD6H4BBxEwGhE3G5yXYONVYpX65-GOrLuwu2MqjmCMATaYvKke1YrIyk0NLcR7TqO4qa_zTCHbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله شب گذشته ج‌ا به اربیل در عراق
علی‌الزیدی نخست‌وزیر عراق با صدور بیانیه‌ای،
این حمله را محکوم کرد.
در این بیانیه آمده که «به آژانس‌های امنیتی
مربوطه در هماهنگی با نیروهای امنیتی منطقه دستور داده شده که همۀ تدابیر لازم برای ممانعت از تکرار حملاتی از این دست، و نیز مقابله با هرکسی که به‌دنبال خدشه‌وارد کردن به امنیت جامعۀ سرفراز عراق باشد را اتخاذ کنند».</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6156" target="_blank">📅 14:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6155">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dF8fTYS2hwRyr4uE2Y6qww9z2x6J8koaPszh9Fk1ReuM3s5IVINN3Sl928BrtHDekFH2e8_BunPBMiMJfpw1yS_Jq2NPO1EyMyfn5KTx813hqPYWaHbfVGfj_-bUOn8gFtMdwVGuIw39T7CHYzdYkDZs24EvjKpstgAT4KmWDb3Texlh9WRXUxvr9Qbjp7YX5kP7a-wgqdbadJN6tHnN-P8gVjBllxG6WYimFWROsWpAdXEUUw5xK1eW6WHmWkwWodYW_BDMhXDvdGdW3_2RMU7071LMdp_Ndz6sb-rrGnPMkY-oxTqSBFpM73Kd2D5IyRTB1X8H4_73OvIk54eoUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وراجی نکنید  بگذارید بجنگند که صلح بیارن :)  مثل صلحی که ۴۷ ساله در لبنان  ‌ و غزه آوردن!  انتقاد از خامنه‌ای عین بی‌شعوری است!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6155" target="_blank">📅 12:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6154">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">وراجی نکنید
بگذارید بجنگند که صلح بیارن :)
مثل صلحی که ۴۷ ساله در لبنان
‌ و غزه آوردن!
انتقاد از خامنه‌ای عین بی‌شعوری است!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6154" target="_blank">📅 11:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6152">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1933ad174.mp4?token=DTuoLHHnsBa-JrEuxmMrpgy_jiT9kBVP1Y6f-GKIkHDmLaVVopWhhuS9JTOgXHpjjNnYn4Nvxbg_-nhmGK_DxBWfE8Vnr4K3QXrmlgnBsu9u7U5Z3etyMnyDhp_JMbgUHf9VEfAYYrwCgrIeYPsnFcUzxTfFyQspK1sDV1G2jjwBFIz_DA2Xj4vjPN9SPtTpGf8BVSLsegSFaBuFc3Y3xVKZjCtlZcSsaqDLO_tY7AXgVsoP8xZiwi86QiL9m-7h3si9SN1GQZxEVa1vBxs-80ZEdlPXfM6PLEbeIUyVfz3b1iG4KndbBB6FNEYbkZkgmilBIOCXwdQS8qjGx0mvtXN9uyFQvwk2kwQyKDc9VdLsO8v-ZXqIDda7nPMEiFMuwy-hGV5ogVtEx976yPROOYGLUDYjUdHNP_gTRTpHnDciNi6zQyvnbC8zoUe8xgG-h8tn3ixuPPKZazcPz6INpDADTP0P63-HEUe9KUnhZGmQIeDK3C0EVj-DhfnNBlFVhgSdkOl6-uI4lhqc8tVYajTXZb8EMxRHcz3x32Ae4-pOKaS544oJWYlvyi5PcThxzcjdmJ3jhV3GNXtbZaaM1fwYjN8Xibm-KLatFGOGztQcJnDOdkiIqoPyIwmiOqRPmUaVZPf0WwWL0UyzGIvWbA48s35_g5htsiJE7kRUJXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1933ad174.mp4?token=DTuoLHHnsBa-JrEuxmMrpgy_jiT9kBVP1Y6f-GKIkHDmLaVVopWhhuS9JTOgXHpjjNnYn4Nvxbg_-nhmGK_DxBWfE8Vnr4K3QXrmlgnBsu9u7U5Z3etyMnyDhp_JMbgUHf9VEfAYYrwCgrIeYPsnFcUzxTfFyQspK1sDV1G2jjwBFIz_DA2Xj4vjPN9SPtTpGf8BVSLsegSFaBuFc3Y3xVKZjCtlZcSsaqDLO_tY7AXgVsoP8xZiwi86QiL9m-7h3si9SN1GQZxEVa1vBxs-80ZEdlPXfM6PLEbeIUyVfz3b1iG4KndbBB6FNEYbkZkgmilBIOCXwdQS8qjGx0mvtXN9uyFQvwk2kwQyKDc9VdLsO8v-ZXqIDda7nPMEiFMuwy-hGV5ogVtEx976yPROOYGLUDYjUdHNP_gTRTpHnDciNi6zQyvnbC8zoUe8xgG-h8tn3ixuPPKZazcPz6INpDADTP0P63-HEUe9KUnhZGmQIeDK3C0EVj-DhfnNBlFVhgSdkOl6-uI4lhqc8tVYajTXZb8EMxRHcz3x32Ae4-pOKaS544oJWYlvyi5PcThxzcjdmJ3jhV3GNXtbZaaM1fwYjN8Xibm-KLatFGOGztQcJnDOdkiIqoPyIwmiOqRPmUaVZPf0WwWL0UyzGIvWbA48s35_g5htsiJE7kRUJXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینها اگر نوحه میخونن و مداحی و رجز خوانی و.. برای کودکان غزه و لبنان و میناب و….. از تاسف از دست رفتن زندگی نیست! میخوان در این جنگ بی‌‌‌‌پایانی که با جهان دارند،  از جمله و در صدر این‌جنگها،  با خود مردم ایران جنگ دارند، سربازگیری کنند! تا نیروهاشون بزرگ‌تر…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6152" target="_blank">📅 11:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6151">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">تمدن اسلامی! تا زمانی که توی مدینه و مگه بود قادر به ساخت «توالت» هم نبود!  مستراح هم نداشتن !! اما دنیا در چه وضعی بود؟  ۶۰۰ سال قبل از تولد اسلام!  توی بیشتر شهرهای جهان  داشتن توالت عمومی! اجباری بود!   اینها میشینن روی منبر  میگن «مدینه فاضله»!!  حالا…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6151" target="_blank">📅 10:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6150">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">تمدن مصر باستان رو مطالعه کنید ابتدا تا انتهاش بر مدار مرگ بود! فرعون از زمانی که سر کار می‌ا‌ومد به فکر مقدمات مرگش بود و قبرش بود!  هنر و پزشکی و علم و مهندسی مصر همه بر پایه صنعت مرگ بود!  مومیایی و اهرام و جراحی پزشکی و….. همه برای کار و کسب مرگ بود و…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6150" target="_blank">📅 10:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6149">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vgPdbk8cVGvZv2nH72D6FtX6hMoM3KmaQLUevCXpmaJ937VOMC15eUpI45fIwcpdLThXO5uBwJM7-8jbTrivL5GfNI8SX1h1V2tvqXoMA3dDZE72OUXn-wBJE5uqcFuTeL3CtpoU-08Ayk0xw0S5cOtPlH3m0p8FjRd_E0_oNEoGAERXA7lG9ZLX0055S_42MtPR2qSemcneUgw1tGpJXHQqQWGSst4Ahj447Xz07-OQvFCXaWgL3ekD2cD5N-BrpsI8YmOs8OcDiQu_n9rc1H-UzGMkL1yoOMiHoJUsYhZXoQoFQikYMdgbq0eOJXoDW83S75YBBqfhniZJVGusCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها شنیدید جملاتی با این مفهوم رو که زندگی و این حیات «زندان مومنه»!  آرزوی اینها مرگه! مرگ براشون رهایی است!  اینکه برن و برسن به بهشت و به زندگی!!  مرگ رو آرمان خودشون می‌دونن و زندگی و زیبایی‌هاش  رو پست و حقیر معرفی میکنن!  و اینکه باید دائم به فکر مرگ…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6149" target="_blank">📅 10:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6148">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">اینها اگه می‌بینید برای مدرسه میناب و…..  سر و صدا میکنن، فکر نکنید به این خاطره که «اصل زندگی»  رو دوست دارند. و از مرگ متاثر میشن!  تمام هستی اینها :  مبارزه، جنگ، کشتن،  کشته شدن و….. است!  زندگی براشون چیزی نیست جز  «مبارزه  برای عقیده».  و خوشحال میشن…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6148" target="_blank">📅 10:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6147">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b6d93f0a9.mp4?token=MkwUsuvZrzb8ZKRcxejy3POAEaOm_6MRjDXZVi2DPJnGdJB5tFRBfo5beBcM2MwWUOlCoTTvt471-vyyzC266Ho6x757UrDFYDAQ5wnpVVh1gg-hEoaZvLFKKOIsZA4WhimiI_ZuyFCgEvYaJD2ADcoSb8Yly6qqezl4HvghE8kXZvUw3QVGG_sxhifrepvHVSBb8K8HI5VWMm4jQqlABH4cVu7KhfKEs25veHHRT8bTLbesVrPJNASrSdw669M-HPgsrziovdfT37tmkNUjj9vle0odYZCjPAe32ZasN_QArpaExpuavDYOLz0nvZpJVz7tD4Fy_d3cE-oBkyPZfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b6d93f0a9.mp4?token=MkwUsuvZrzb8ZKRcxejy3POAEaOm_6MRjDXZVi2DPJnGdJB5tFRBfo5beBcM2MwWUOlCoTTvt471-vyyzC266Ho6x757UrDFYDAQ5wnpVVh1gg-hEoaZvLFKKOIsZA4WhimiI_ZuyFCgEvYaJD2ADcoSb8Yly6qqezl4HvghE8kXZvUw3QVGG_sxhifrepvHVSBb8K8HI5VWMm4jQqlABH4cVu7KhfKEs25veHHRT8bTLbesVrPJNASrSdw669M-HPgsrziovdfT37tmkNUjj9vle0odYZCjPAe32ZasN_QArpaExpuavDYOLz0nvZpJVz7tD4Fy_d3cE-oBkyPZfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینها اگه می‌بینید برای مدرسه میناب و…..
سر و صدا میکنن، فکر نکنید به این خاطره که «اصل زندگی»  رو دوست دارند.
و از مرگ متاثر میشن!
تمام هستی اینها :
مبارزه، جنگ، کشتن،  کشته شدن و….. است!
زندگی براشون چیزی نیست جز
«مبارزه  برای عقیده».
و خوشحال میشن اگه زندگی رو به خاطر اون عقیده نابود کنن! زندگی نیمی از مردم جهان هم نابود بشه براشون مهم نیست!
چون «برای یک هدف بزرگ‌تر»! مبارزه میکنن!
پس چرا مثلا روی مدرسه میناب مانور میدن؟
چون میخوان شما رو بیارن توی صف مبارزه خودشون
برای اون هدف بزرگ‌تر !
برای جنگ‌های بی پایان تا رسیدن به هدف بزرگ‌تر!
اینها نمیجنگن تا در این دنیا آرامشی باشه
و صلح بلکه میجنگن برای آخرت!
برای اون دنیای دیگه مبارزه میکنن!
از این زندگی و این جهان متنفرن!
این زندگی رو فقط یک پل می‌بینن! یک فرصت برای مبارزه و کشتن و کشته شدن و….. که بعد توی اون جهان به آرامش برسن! این زندگی فقط عرصه و میدان جنگه براشون!</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6147" target="_blank">📅 10:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6146">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uGSNeh4twn0Kmj6Sz_8bVulbL2COdBeLzlUKsBCHnGfcz_NSbfDlTb6SqWaMxZ1PiHQH4lLwtGhdWiVvuvhQyCKuMQ8Km_k_PdzEZTC8tumQTIx95vfLHUNxlg3hMXXnnFYI73UopGmx_c-j6-UkTaw3PLqKwmx15MUIlnlLoJgXML0h3KpfJBk5wb9AazVWIG_-Qkc0ZV5JAcrN6WhBomKnMrPXJd8HBYy4dEwmBWU7XCqnKcI0RaVvBTcEWgTJnol6fP3r2HNq85tx-du4d_Gg0y8ln723fDAaiOV_PZ8BU_QmrSx8UD1qcieQQrBAj2QrIWDNqt0Vtte7sz-nPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: ایران به یک شهروند زن آمریکایی که در دسامبر ۲۰۲۴ در دوران رئیس‌جمهوری جو بایدنِ خواب‌آلود به‌ناحق بازداشت شده بود، اجازه خروج از کشور داده است. او اکنون در سلامت کامل در خارج از ایران است. ایالات متحده آمریکا از این ژست حسن‌نیت ایران قدردانی می‌کند.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6146" target="_blank">📅 09:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6145">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
حملات دیشب به استان‌های خوزستان، سمنان، مرکزی و لرستان
🔺
دیشب تعداد زیادی انفجار در اهواز شنیده شد. برخی‌ها تا ۹ انفجار و برخی تعداد انفجارها را بیشتر تخمین زدند.
🔺
گزارش‌ها حکایت از آن دارد که یکی از موشک‌ها در اهواز و در نزدیکی یک بیمارستان (بقایی) اصابت کرده.
🔺
دیشب همچنین به چند نقطه از استان لرستان حمله شد، برخی گزارش‌های تایید نشده از حمله به پایگاه موشکی امام علی در لرستان خبر می‌دهند.
🔺
استاندار سمنان نیز گفته که به بخش‌هایی از فرودگاه سمنان حمله شده، کسی کشته یا زخمی نشده.
🔺
استاندار مرکزی: شب گذشته به دو نقطه در اطراف شهر خنداب حمله شد. این برای چندمین بار است که اطراف شهر خنداب مورد حمله قرار می‌گیرد.
نه آمریکا دقیقاً مشخص می‌کند چه اهدافی را زده و نه ج.ا می‌گوید به کجاها حمله شده.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6145" target="_blank">📅 09:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6144">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">استاندار مرکزی : شب گذشته به دو نظقه در اطراف شهر خنداب حمله شد.
این برای چندمین بار است که اطراف شهر خنداب مورد حمله قرار می‌گیرد.
نه آمریکا دقیقا مشخص میکند چه اهدافی را زده و نه ج‌ا می‌گوید به کجاهاش خورده.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6144" target="_blank">📅 08:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6143">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">اطلاعیه  ارتش:  سامانه‌های راداری، سامانه پدافندی پاتریوت و مخازن سوخت آمریکا در پایگاه علی‌السالم کویت را هدف قرار دادیم.
‏ رادار‌های سوپر هاوک، تأسیسات و سامانه‌های پاتریوت واشنگتن در پایگاه شیخ عیسی بحرین نیز طی حملاتی، آسیب‌های جدی دید.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6143" target="_blank">📅 08:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6142">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
استاندار سمنان : به بخش‌هایی از فرودگاه سمنان حمله شده، کسی کشته یا زخمی نشده.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6142" target="_blank">📅 08:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6141">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OReWmHwQ3N_cljQw8iKKErQaQJLoPW5CDm2jsR7bfr8V3lSqc-8W92q2D9MoARKRgeP6hKdFAjK5hJiNhswl3DvQw2FXKYF68zFJZeos_5mrAK12vLUj-1WFlEiPeq6Qu5WcCJGibksuxCCrO06d-MQa0_GpDqjn6jKxYGxsxe9qfjed8gmGFXs_-L_EkMwx49svRo3zJ6nXs1pGqPtt2Ly1_ZKFXFuKyes2SWr608IKZBsfQz8nw3mxXNa181wl1lMoRRYZYalRuDl9WiuQmsCTGLT_olqLvT3RkkFDcZ1uE-_kCPb6rni1vP-lJ38oN53ft15j3ZeW6qFN12hx2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین یارو خودش از دست سپاه و نهادهای زیر نظر خامنه‌ای  فرار کرده و به آمریکا پناه برده!
و آمریکا رو خونه امنی پیدا کرد برای زندگی و نوشتن از اینکه اسلام چقدر زیباست و خوبه و سعادت انسان رو میخواد!
حالا از همونجا به ج‌ا میگه مبارزه کن با آمریکا! مطلقا تسلیم نشید! تا انتهاش برید!</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6141" target="_blank">📅 08:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6140">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">برخی گزارش‌ها از تداوم حملات به اهواز خبر می‌دهند و اینکه تاکنون ‌۹  انفجار  مهیب در شهر شنیده شده.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6140" target="_blank">📅 23:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6139">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
چندین انفجار مهیب در چابهار و بندرعباس
🚨
کویت : امروز ۲۱ پهپاد و ۴ موشک شلیک شده از سوی ج‌ا را منهدم کردیم.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6139" target="_blank">📅 22:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6138">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای ۲ یا ۳ انفجار در اهواز</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6138" target="_blank">📅 22:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6137">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T3DOfQeKWvJ710CCh02Rsm9vUBPIGtArjTTNvFlIqjW0Ibm9W8RhXBBCd0gsbYm0vMgzNgscs0fMu5b_PylJxGRm0L1XZHhx3dZvzbkmSIrblSpaZe8mNLRMInM1CZnNOWrtG9ewScoANv6zhv-P6VVVdDDL1zkHLD9MTwlSaNIuHQmbtMXuqMbHxdSeugATX5bOU-Tv6sKMByLyN0lHLxouDcaWvnooSTECe9zfthmH7uX9OaQlHb_YrRH1V9z1SuerUm0hNdzELGoaQqQh7tHZkUjrHj2NDQ-SFxp9stMVLrImwMnD0QZqIE90NkG6tQvhVpgQ3LXnMmDACsQwSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شما دیگه جرات حمله به اسرائیل
رو ندارید! خودتون هم خوب می‌دونید!
این ۴-۵ روز هم به همه جا حمله کردید
به جز به اون کشوری که بیت‌رهبری
رو زد نابود کرد!
و نشون داد دقیقا کجاست که سست‌تر از لانه عنکبوته!
ولی هر چقدر دوست دارید شعار بدید!
اون حزب‌الله تروریست هم رفت انتقام بگیره  هنوز و همین امروز هم نیم میلیون نفرشون  توی محله‌های مسیحی و سنی لبنان آواره شدن!</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6137" target="_blank">📅 20:39 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6136">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">آنچه شب گذشته در بمپور رخ داد و موجب  کشته شدن تعدادی ای نیروهای ارتشی شد، قابل اجتناب بود.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6136" target="_blank">📅 20:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6135">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20e615d142.mp4?token=rbKtNV8h4b1-xHhARCBs26oE8F1AmxtZVuekHBNNflWvvmdlWEs8-c7ZXqNjA5xu_BAIHoZlfRkmTl-QiJZMEbH359OA2cpk1rjthIbgMHTy7oWWNtDdLbj1nS4Q14LOuILMVNB7iJLorVZfN3VTNwGNBLu438JbYBDaOgl-_DUpvQf70-UqYfg_S3THufWPC6Hwx8o2C4RyXwZJH1e_W-5Maoke-ywNeRvuR7igal___QVY4YI9SFgwcGdHB6F7LNUY3eeRpdFsNEcyJIebHp8_x0zuysFRMJZZO2csfMFiczAipcrgg94XY1pACfW7xTQ_XRQZ2EC-qPWK08l_jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20e615d142.mp4?token=rbKtNV8h4b1-xHhARCBs26oE8F1AmxtZVuekHBNNflWvvmdlWEs8-c7ZXqNjA5xu_BAIHoZlfRkmTl-QiJZMEbH359OA2cpk1rjthIbgMHTy7oWWNtDdLbj1nS4Q14LOuILMVNB7iJLorVZfN3VTNwGNBLu438JbYBDaOgl-_DUpvQf70-UqYfg_S3THufWPC6Hwx8o2C4RyXwZJH1e_W-5Maoke-ywNeRvuR7igal___QVY4YI9SFgwcGdHB6F7LNUY3eeRpdFsNEcyJIebHp8_x0zuysFRMJZZO2csfMFiczAipcrgg94XY1pACfW7xTQ_XRQZ2EC-qPWK08l_jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیش بینی تاریخی بختیار
در دو کلمه، برای مردم ایران</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6135" target="_blank">📅 20:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6134">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/296fa239b5.mp4?token=I-TdwHhkERbx9UnKfPx4eXKPj7UOvox4M5AVYQpgbBkkQct4tggVg3eX5HVkNg_dvgU7f-9-M2gD5H04Ias8dBOhjmGtR8TMoQWRUQjikGbvX6NQq_1kJQFBruwJ4ql91KhQqPQtE5jRotsCNUk7_k5UgspXjuGfpcfMVAIBCaXeQS6Yo3c6ELu_RBRcsIJMZg09jnrmKkWDuepXh6Lfh7GYOFnEVJ7Qx72Gvx3F3aKM5oTTizx1l0I5wej7K-m5tupywMOd6hcc8MHtPHvYPuCC9JwnWxctYYqeXTPFHQRPMIrctgPHrRkszBVbymn846OdVUQYE5E1A2P-eZUME4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/296fa239b5.mp4?token=I-TdwHhkERbx9UnKfPx4eXKPj7UOvox4M5AVYQpgbBkkQct4tggVg3eX5HVkNg_dvgU7f-9-M2gD5H04Ias8dBOhjmGtR8TMoQWRUQjikGbvX6NQq_1kJQFBruwJ4ql91KhQqPQtE5jRotsCNUk7_k5UgspXjuGfpcfMVAIBCaXeQS6Yo3c6ELu_RBRcsIJMZg09jnrmKkWDuepXh6Lfh7GYOFnEVJ7Qx72Gvx3F3aKM5oTTizx1l0I5wej7K-m5tupywMOd6hcc8MHtPHvYPuCC9JwnWxctYYqeXTPFHQRPMIrctgPHrRkszBVbymn846OdVUQYE5E1A2P-eZUME4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی که فرمانده سپاه بود و سالها فرماندهی جنگ رو بر عهده داشت
اینجا میگه مطئنم که مسیری که در ذهن مجتبی خامنه‌ای است، بهتر از مسیری بود که شورای عالی امنیت ملی رفت.
مجری ازش می‌پرسه خب اون چه مسیری بود؟
میگه : نمی‌دونم ! نمی‌تونم که ذهن خوانی‌ کنم!
فقط می‌دونه خوب بود :) یه مشت چاپلوس !</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/6134" target="_blank">📅 16:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6133">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVahid Online وحید آنلاین</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/obU9WfBVcW67Mdky_qgWhIZKGCmp-UNlYH_xD9QRlK7sQHdjT3VolaxpSCDMeG254m_0NI6GONLcGk1B92BxHXxkpboJCsUsIxlMYagICNdmH8BWiul8OI8xlQFvDR4LZ1WtXFWSDqqODx9kHZPYSr0pkv0PuuYVkJ9qzifuubE6bWs83s6GDqfLE_0ptCgKLzLdEKCrjO7dNmO2m6-0NP-B0YvEu6N3_-Jx-cuM4upneLaOlFTIyXvhLRwrUMgFt-v3dA4mN9h00OyRgWGV_ZlVh_V9M-ghC__ZMweXmecSnXW_OiayFiLATKGbl0hCv4T1z_mfDBCmUHDSGMJR7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضاییه جمهوری اسلامی از اجرای حکم اعدام محمد امینی دهاقانی، از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴، خبر داد. مقام‌های قضایی او را به آتش‌زدن فرمانداری و کلانتری مرکزی شهرستان دهاقان در استان اصفهان متهم کرده‌اند؛ از روند بازداشت، بازجویی و جلسات دادگاه و … محمد امینی دهاقانی خبری منتشر نشده.
براساس اطلاعیه منتشر شده در خبرگزاری میزان، ارگان رسانه‌ای قوه قضاییه، حکم اعدام محمد امینی دهاقانی پس از تایید در دیوان عالی کشور، بامداد امروز ۲۴ تیر ۱۴۰۵ اجرا شده است.
در این اطلاعیه آمده است که امینی دهاقانی روز ۱۹ دی ۱۴۰۴ با پرتاب کوکتل مولوتف به ساختمان فرمانداری دهاقان باعث آتش‌سوزی شده و سپس یک کوکتل مولوتف دیگر نیز به سمت کلانتری این شهرستان پرتاب کرده است. مقام‌های قضایی همچنین مدعی شده‌اند او در تحریک معترضان برای حمله به کلانتری نقش داشته است.
دستگاه قضایی جمهوری اسلامی بخش عمده پرونده را بر اعترافات متهم استوار کرده است. در اطلاعیه رسمی ادعا شده که او در بازجویی‌ها پرتاب کوکتل مولوتف به سمت فرمانداری و کلانتری را پذیرفته و همچنین گفته است قصد داشته از یک قبضه سلاح کلاشینکف، که به ادعای مقام‌های امنیتی از ماموران گرفته شده بود، استفاده کند.
محمد امینی دهاقانی همچنین به «بازنشر و ارسال محتوای تبلیغی علیه جمهوری اسلامی، تشویش اذهان عمومی و برهم زدن امنیت روانی جامعه» متهم شده است.
او همچنین به «درخواست ارتباط‌گیری با حساب‌های کاربری» مخالفان جمهوری اسلامی و «درخواست ارتباط‌گیری» با صفحات مجازی مرتبط با خاندان پهلوی هم متهم شده است.
مقام‌های قضایی هیچ اطلاعاتی درباره نحوه دسترسی متهم به وکیل مستقل، شرایط بازجویی یا روند برگزاری دادگاه منتشر نکرده‌اند. همچنین مشخص نیست اعترافات منتشر شده در چه شرایطی اخذ شده و آیا متهم امکان رد یا اعتراض به آن‌ها را داشته است.
اعدام محمد امینی دهاقانی در حالی انجام شده است که نهادهای حقوق بشری بارها نسبت به افزایش صدور و اجرای احکام اعدام برای معترضان و متهمان پرونده‌های امنیتی در جمهوری اسلامی هشدار داده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6133" target="_blank">📅 15:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6132">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
سنتکام : به تنب بزرگ حمله کردیم.
در جریان این موج ۹۰ دقیقه‌ای از حملات، با استفاده از مهمات هدایت‌شونده دقیق، سامانه‌های دفاع ساحلی و محل‌های ذخیره‌سازی و پرتاب موشک‌های کروز در جزیره تنب بزرگ را مورد حمله قرار داد.
این حملات توانایی ایران برای حمله به کشتی‌های تجاری در تنگه هرمز را بیش از پیش تضعیف کرد.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6132" target="_blank">📅 15:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6131">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">حمله امروز به چابهار</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6131" target="_blank">📅 14:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6130">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
ارتش: «آمریکا بامداد امروز با شلیک ۱۳ فروند موشک، آسایشگاه و محل اسکان یکی از پادگان‌های نیروی زمینی ارتش در بمپور را هدف قرار داد
دشمن به مهمانسرا و اماکن نگهبانی پادگان حمله کرد
‏ ۷ تن از کارکنان پایور و وظیفه تیپ ۳۸۸ ایرانشهر شهید و تعدادی مجروح شدند.»
‏</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6130" target="_blank">📅 14:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6129">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
سنتکام : از نیم ساعت پیش موج تازه‌ای از حملات را آغاز کرده‌ایم.
(از  ساعت ۱۳:۳۰ تهران)</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6129" target="_blank">📅 14:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6128">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J97dGJ0IhaEe90o4U5AxezrPCM9p2AwuKyvnJ-CqqTWMxqNzYaJV5j6AMrLd_T0lTiyPkj2DY5lOnygGF86YrlxHVBuBJugMcVwAh85jGXfxnFSCz3VZCbZfdHM-vhhLL5lmLT1tLeKtsoBV81zVy1H7SL8V_uxboPyPkWE_QrE4GLGxT7DJ0nJPhyo-GMYurAA_Ove7p1lUdpMbanJ3hj5bUX6O_uWVM__HvAkB3eigQaIwKjUxJsx9I8n3VFu6W9g66bALfRe57gE-2tCNJ93_qLc2Wi3UnVAlnEhj_bEkrgfHjeenPfpteq4pc-zcXn9YBiSNSetcLvqUbgKFMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قابل توجه ساختاری‌های محترم
مدیر حوزه‌های علمیه با بیان اینکه مسئولان باید تفاهم‌نامه‌ها را پایان‌یافته تلقی کنند، از دولت و شورای عالی امنیت ملی خواست به دلیل بدعهدی طرف مقابل، مسیر مذاکرات را متوقف کنند.
مشکلات اقتصادی یا ترس از آسیب به زیرساخت‌ها نباید موجب واهمه مسئولان و رویگردانی از مسیر «جهاد و استقامت» شود.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6128" target="_blank">📅 13:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6127">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd0a98053a.mp4?token=mExnVbs6DHgOAYSD1VIxmRZBUHIZtrEIn2wG1AAW9EZVCs7yeImlyBNFXr3kICE2Notrbu5whb-A69-Bw2FZ41e26z1cUbGUuqv8s4eNNofR5ABe-I3oJpnOGTIc7Hn_reAM2A5aR4RMn457hBGpGlTi4gIuiiEqHzCa10hkk0TguKxsTafJVlttBvodVjbRm21BO_pNaqNmXMX-Rs525ELI-BMwFSEyMjGQuNdb1G4pMHGoUt9kilUOcizj1BMmKJzrTjwek3AcPmJnpdgo-H6K-V8r4sjw4AAG4HjISQqlrGzq15JORpgqsX3BEPiq2va-Us_xfo22wUTU7PUALTWxq3ghWh-KKJZp4JaFAtENCncLOaKUxd611KA9NGxEv5QSz8hzQHaITsJXRoHzZRVoht0FA0l33KDl-FwgXm2jRwm2HL0pYx9vh_XWmgBXOPHvnqkMOTSWb-MQpo7yEfgJTO9yC_-btMqYj6tjwRBTCgbeXKrNDk6degXAkkN2j2c__GHv9MqC6Fu84O_DCK6f4wtHVHCnKRKNpZMXJzGKVvIwaDFkGH1dqCEFHxwzpdocPyG6J8wbKBPmie1NKtr1uf3tAAYFWehG9UOBvs6OIXIw_4bPgGTs_G6Eu5ZEbuy2XArblSAe4i6Icqv3LO2AoxF3noJCGWr9r86X2zk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd0a98053a.mp4?token=mExnVbs6DHgOAYSD1VIxmRZBUHIZtrEIn2wG1AAW9EZVCs7yeImlyBNFXr3kICE2Notrbu5whb-A69-Bw2FZ41e26z1cUbGUuqv8s4eNNofR5ABe-I3oJpnOGTIc7Hn_reAM2A5aR4RMn457hBGpGlTi4gIuiiEqHzCa10hkk0TguKxsTafJVlttBvodVjbRm21BO_pNaqNmXMX-Rs525ELI-BMwFSEyMjGQuNdb1G4pMHGoUt9kilUOcizj1BMmKJzrTjwek3AcPmJnpdgo-H6K-V8r4sjw4AAG4HjISQqlrGzq15JORpgqsX3BEPiq2va-Us_xfo22wUTU7PUALTWxq3ghWh-KKJZp4JaFAtENCncLOaKUxd611KA9NGxEv5QSz8hzQHaITsJXRoHzZRVoht0FA0l33KDl-FwgXm2jRwm2HL0pYx9vh_XWmgBXOPHvnqkMOTSWb-MQpo7yEfgJTO9yC_-btMqYj6tjwRBTCgbeXKrNDk6degXAkkN2j2c__GHv9MqC6Fu84O_DCK6f4wtHVHCnKRKNpZMXJzGKVvIwaDFkGH1dqCEFHxwzpdocPyG6J8wbKBPmie1NKtr1uf3tAAYFWehG9UOBvs6OIXIw_4bPgGTs_G6Eu5ZEbuy2XArblSAe4i6Icqv3LO2AoxF3noJCGWr9r86X2zk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سفیر اسبق جمهوری اسلامی در روسیه: مطمئن باشید اگر ترامپ را بکشیم نه تنها هیچ موشکی به سمت ما شلیک نخواهد شد، بلکه عقلای آمریکا با خوشحالی جنگ را تمام خواهند کرد.
کشتن ترامپ هیچ هزینه‌ای برای ما ندارد و با کشتن او جنگ هم تمام خواهد شد.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6127" target="_blank">📅 11:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6126">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">جلسه اتاق وضعیت برای بررسی حملات گسترده‌تر آمریکا علیه ایران؛ آیا ترامپ آماده تشدید جنگ است؟  به گزارش اکسیوس، دونالد ترامپ، رئیس‌جمهوری آمریکا روز سه‌شنبه برای گفتگو درباره عملیات تهاجمی گسترده علیه ایران جلسه‌ای را با حضور مشاوران ارشد خود در اتاق وضعیت…</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6126" target="_blank">📅 08:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6125">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gFzTQcz2KM6Y-hH0Ig5JTNAvkBGBFLvL9YuPFcsD9tWYZFbLzFhCPEfdmBGOiylMfTEFLdqf-OuLWftAO4ManXXFrOddkXlFew3lGvvlok0NDmDxRxhMszyXHOvDN5-ad_5n45eGbxZ3abevfqkX8h7dSTaDjumM8qK877HK9QIdfeg-OGRDT-EzsCbS25ixjcXPnfiwlEGfJ-J7jAFaJXkOjAjqz32QBGvMQMY3zrZNE8eNSM45d-O6xAMZArH8nm2rJBQcWahTJhFSh4-_kdHfga23PJffyK_hrv0EeXHGg2TPsgMttl1-1fjzyVacCNzZtjk12W-zFgCO_YutLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلسه اتاق وضعیت برای بررسی حملات گسترده‌تر آمریکا علیه ایران؛ آیا ترامپ آماده تشدید جنگ است؟
به گزارش اکسیوس، دونالد ترامپ، رئیس‌جمهوری آمریکا روز سه‌شنبه برای گفتگو درباره عملیات تهاجمی گسترده علیه ایران جلسه‌ای را با حضور مشاوران ارشد خود در اتاق وضعیت کاخ سفید برگزار کرد.
به گفته سه منبع آگاه، در ابن جلسه که ارشد‌ترین مقامات نظامی و امنیتی آمریکا در آن حضور داشتند در خصوص گسترش حملات صحبت شد.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6125" target="_blank">📅 08:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6124">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bd4825a45.mp4?token=aEExiIsY1Ihv4h6-lLp_NksQyzRwuebf0RxZZeY7VF55zRnbG4ljpTAC6qZM91O5-sitamGjC1EdCo9JWgcQzsLuRgeoiE0TtAkQPWsR-htVP4qeIAwPeshtmWXRqjE7wNKt-7HLcTvsKhL0O6snqPFwuEjkWcVJQpDYwwj-LpTQJLAqQHihpDpO43_LiJUNxubcINxKiOhl7jMC4CVru1hxPAXamcXPEXDiBHfD2FbtazKyDXFJuVQWAdlFEDn-i2lH9elNlfGuSt65TPO7I-n582wNseqwtWLjJtktrI3fpkqBYVV-RIjy7mt2gPStM5oyHtJI_rXXLH4xG-EjcDK7crDkdPr8j2uEkKzbgzdeOdmeZzo4o-Fe0HLkvk-8ifZfG5-0ArFbVTSj9G7m3kIbkR4uJ2PhGBcF70exYg77ukh0ASANZ5-r5n_Zf49nnGfKzKfZRKmMuOLEEiej_1NCN0h_AuVFVUsq-qaUuvUH-eShJmapU8grqUiPGDnA9u0CSpEt7Cn4oRnq7g0W9cgEgvu2M5rS75mpyjCp3H9oGW_QiR9UE9X9Oc2brSQOgFNlOOdTjDmiJQb4Eh0SqYFXjMUsd94s11Rmc9M-h6szGEFkN1gXuOpEp126jOQUunTH3Y6lx0RmaqzKPQTWx0MToq5WUjca-VlHEnAd-Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bd4825a45.mp4?token=aEExiIsY1Ihv4h6-lLp_NksQyzRwuebf0RxZZeY7VF55zRnbG4ljpTAC6qZM91O5-sitamGjC1EdCo9JWgcQzsLuRgeoiE0TtAkQPWsR-htVP4qeIAwPeshtmWXRqjE7wNKt-7HLcTvsKhL0O6snqPFwuEjkWcVJQpDYwwj-LpTQJLAqQHihpDpO43_LiJUNxubcINxKiOhl7jMC4CVru1hxPAXamcXPEXDiBHfD2FbtazKyDXFJuVQWAdlFEDn-i2lH9elNlfGuSt65TPO7I-n582wNseqwtWLjJtktrI3fpkqBYVV-RIjy7mt2gPStM5oyHtJI_rXXLH4xG-EjcDK7crDkdPr8j2uEkKzbgzdeOdmeZzo4o-Fe0HLkvk-8ifZfG5-0ArFbVTSj9G7m3kIbkR4uJ2PhGBcF70exYg77ukh0ASANZ5-r5n_Zf49nnGfKzKfZRKmMuOLEEiej_1NCN0h_AuVFVUsq-qaUuvUH-eShJmapU8grqUiPGDnA9u0CSpEt7Cn4oRnq7g0W9cgEgvu2M5rS75mpyjCp3H9oGW_QiR9UE9X9Oc2brSQOgFNlOOdTjDmiJQb4Eh0SqYFXjMUsd94s11Rmc9M-h6szGEFkN1gXuOpEp126jOQUunTH3Y6lx0RmaqzKPQTWx0MToq5WUjca-VlHEnAd-Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مزدوران حکومتی شعار میدن
«جنوب ایران نکند جنوب لبنان شود»
عجب! شما دیگه چرا؟
خامنه‌ای میگفت «جنوب لبنان الگوی پیشرفته
و موفق مبارزه ایمانی است»! سالی یک میلیارد دلار از اموال ملت ایران رو میدین به گروه‌های تروریستی اونجا  و تبلیغ اینکه ما اونجا پیروزیم و …..!
ولی ظاهرا اسرائیل در جنوب لبنان چنان درسی بهتون داد که الان خودتون هم میگید نکنه بشیم شبیه اون «الگوی موفق»! معرفی شده توسط خامنه‌ای</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6124" target="_blank">📅 07:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6123">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0378588a4a.mp4?token=BM6mmldVGsoMN-kV6pdPINuQI6Xk2vYx2NgwVuYYA-nZvwsVerTfYdfQXKv1vs7GcNZl4ajNltCkJex318J7BFEnmwfe6wH3eeSMHDehLPSPqKsO9araf39fwce724JvGYqmAdl3TwWUbf9Kxi_7SdkOcLoxwsK86-tgkzOxErWvPURORJe2Aj8q8gcR5LGd1V-ajIhL1g0QgpX0WnoldOjkdmA14PcQvXG9EoKJd5_FhfLez0jqU2pdSKvOY1ek-UOZ5OdUT55-XxwKorAkQgOih-XMAEbCciA9eXC0_9EhKUQSv6DayrrSmXgsJQlympKchvZzjgSULL-xtB6VuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0378588a4a.mp4?token=BM6mmldVGsoMN-kV6pdPINuQI6Xk2vYx2NgwVuYYA-nZvwsVerTfYdfQXKv1vs7GcNZl4ajNltCkJex318J7BFEnmwfe6wH3eeSMHDehLPSPqKsO9araf39fwce724JvGYqmAdl3TwWUbf9Kxi_7SdkOcLoxwsK86-tgkzOxErWvPURORJe2Aj8q8gcR5LGd1V-ajIhL1g0QgpX0WnoldOjkdmA14PcQvXG9EoKJd5_FhfLez0jqU2pdSKvOY1ek-UOZ5OdUT55-XxwKorAkQgOih-XMAEbCciA9eXC0_9EhKUQSv6DayrrSmXgsJQlympKchvZzjgSULL-xtB6VuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه محلی «حال وش» از حمله به آسایشگاه سربازان در شهر «بمپور » در استان سیستان و بلوچستان خبر می‌دهد و کشته شدن ۱۰ سرباز و زخمی شدن ۱۵ سرباز</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6123" target="_blank">📅 07:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6122">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5b6a441ee.mp4?token=Q6jMtFA42EJVQOwI2AL-LF4AaWm9-PKgCjorYI8PnC2zUxQUQ_DhN-ZYjuz9ngyovxXceTUNhNEL1IxBm5lzuUX-TpFWJAbb4mnUCzqWfHihSeytOQJxodbOdVwMKyExqg0wG0N5WbSIpGWAJCKIej2r4bywrqlTmoYis_kVwpt99wpeW9JsG0NwqQyaYRZksLrbbltgqTqxGFjQZqLWK6tWogomqZqwsOFR_PSDuyC9OTkuZNaT-Zas74ADdU0hvXdi5a5HABE6U1JLl1jmOjwxgy3qbXFrOgb96pBD51mKxDfs3mZ57fZV3TKHUElYOrEMUXsA6xS5l5FBAMJubSDkq_8R2YknSJk3LJJ_VMAz0CmCWbs3V2yFobjJq5FKmLleFkPNVrT7gtbB0zunD4i6wxBWD3PS__HhETnsDXGauLvn44fMNghC-79O1E_62RlbIbOtdyU2nsfzGzydsBoYhGJbX0Bg4TlgLUudNSpcn9TmeHwbKnAvrWPqMpCxrQTiMendkyxv_qk7TXFnxFVnluqWp65xtbcatrSaPJkobp_6pBn1cXqzC4fWd9_FpaLyO6QylhL-1VqGxsGcX56QIW6QXevpSyIEaVAS_coN6NXVLf9IEx096y2NIYmxw6Uzgib6qvAPzBKGYyTZ0IZX6UilyM8uuovVzt7erMs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5b6a441ee.mp4?token=Q6jMtFA42EJVQOwI2AL-LF4AaWm9-PKgCjorYI8PnC2zUxQUQ_DhN-ZYjuz9ngyovxXceTUNhNEL1IxBm5lzuUX-TpFWJAbb4mnUCzqWfHihSeytOQJxodbOdVwMKyExqg0wG0N5WbSIpGWAJCKIej2r4bywrqlTmoYis_kVwpt99wpeW9JsG0NwqQyaYRZksLrbbltgqTqxGFjQZqLWK6tWogomqZqwsOFR_PSDuyC9OTkuZNaT-Zas74ADdU0hvXdi5a5HABE6U1JLl1jmOjwxgy3qbXFrOgb96pBD51mKxDfs3mZ57fZV3TKHUElYOrEMUXsA6xS5l5FBAMJubSDkq_8R2YknSJk3LJJ_VMAz0CmCWbs3V2yFobjJq5FKmLleFkPNVrT7gtbB0zunD4i6wxBWD3PS__HhETnsDXGauLvn44fMNghC-79O1E_62RlbIbOtdyU2nsfzGzydsBoYhGJbX0Bg4TlgLUudNSpcn9TmeHwbKnAvrWPqMpCxrQTiMendkyxv_qk7TXFnxFVnluqWp65xtbcatrSaPJkobp_6pBn1cXqzC4fWd9_FpaLyO6QylhL-1VqGxsGcX56QIW6QXevpSyIEaVAS_coN6NXVLf9IEx096y2NIYmxw6Uzgib6qvAPzBKGYyTZ0IZX6UilyM8uuovVzt7erMs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا میبینم راست میگه …</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6122" target="_blank">📅 07:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6121">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DeJQJM5rakIiz61aLiTobhlHPyagFcWcMLjIoy1igCT7af1K6DpI44OoMDR60D82sjTw-C9HMExSlEH9IVPzqGxc8oAjxin1fq0SW6u96tbyCLK5bRBFfF_BBkGr49WMDpXIhWqhykZ0o6cFE_KsDM-h38Pw0oiHHF_cPX8Hv4o8VsppDvf0hbpHBaaC6tyIMNJyOzQUUwLAYfOuG_msSn7p-pgCbkacgLwTw4MiCoeJaKlKMZ6Gfex8gmhPGjYc7a6dpLrd8U1f90bpppIiDRHJRjLXxxd_hNN8qsMlg6qg0eYZoWUzRjEeWotUvGSq-KGQvvOhpskeYykeaV6Hsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6121" target="_blank">📅 06:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6120">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CTX84QJcMu_SXOLEZK8SE0KJZnr20c4F9Si17jTK1EUi6muF3ttSpcWHFrz2QLvChilZM98CWKej64CidB5LDndQfEblBdKWDOevD0jVmqtQLN5S5V5DA0dF5EKImbR1uQaL5J-twBzerrDj5VpS1IT8-a8p40A4uM0J_MP6eD14h0PyzKS_EGHiUI31GDB5qt3867pWSKvRhwef2C9BCQCkvNWIgafaoRklBzsbX3N53J1TI-Fkqhv4MoP0vS2ng3X_XS-gc3sgLviVDxoioP4VsejUXMfadwFOsAem52L9pEpPRAbJd7YzIHS2G36WsLN9PIVDN_XVtdTffCAL6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه محلی «حال وش» از حمله به آسایشگاه سربازان در شهر «بمپور » در استان سیستان و بلوچستان خبر می‌دهد و کشته شدن ۱۰ سرباز و زخمی شدن ۱۵ سرباز</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6120" target="_blank">📅 06:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6119">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba02e5e863.mp4?token=WKEPZb7Gr6ITKUDa9DnEl6QeBAc9ql9L7p1IkSYB-zx5oQ405mX4Sqqq6vKNslF_Qq8wKvI4zn3zhamFeC6rCZuhNYbaqO-8qOzLr4_8nms0ldSn-_wJuxRP-kVHunXq94wcN-dBmCBkDCZqytm_3-CaTNv7Hp7KuE7TJqOgn2zPjYTttUb4CleWCa7LbAH6rqdkqXKU4vMfkAhMAA-vcpfOSRsnWi5kO9wcfP1RDQ04zRxzxZT7-ady5b1OD478wkVwqmXrPdzCLCSsw-qMH9jZ7gdLUC-8CYzyziCKNpdR29XfAI6epy6lITTvV2LH9MRMAGQphMPepvZSICPP3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba02e5e863.mp4?token=WKEPZb7Gr6ITKUDa9DnEl6QeBAc9ql9L7p1IkSYB-zx5oQ405mX4Sqqq6vKNslF_Qq8wKvI4zn3zhamFeC6rCZuhNYbaqO-8qOzLr4_8nms0ldSn-_wJuxRP-kVHunXq94wcN-dBmCBkDCZqytm_3-CaTNv7Hp7KuE7TJqOgn2zPjYTttUb4CleWCa7LbAH6rqdkqXKU4vMfkAhMAA-vcpfOSRsnWi5kO9wcfP1RDQ04zRxzxZT7-ady5b1OD478wkVwqmXrPdzCLCSsw-qMH9jZ7gdLUC-8CYzyziCKNpdR29XfAI6epy6lITTvV2LH9MRMAGQphMPepvZSICPP3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام فیلمی از حملات خود به ایران منتشر کرد.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6119" target="_blank">📅 06:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6118">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b9746249d.mp4?token=Aj4jpbN3np3bAXcD82h3eeNHKLZqMbAmHKhu-SOhO_88fnSMwBPIG5WrwEE5cdMoxd_0f09nzTHxer-2EGgGHTkLDpIBvP67XkHrymhD0dX2sHpVoVqHbMRjCfsu2ZMdG3MEFq3Ax-Hwg3Abb5UNTdBSB1DBRtZM8yVPGxIeAXkYyl2VkouHHw1g7XfprpL8vPIInlZYUJQrVwg9uCUPgR4CLecEKcNcrW5D5Zn1_a2AyUhmLPK8Ijwy_cb9etqGkjAO8oDSqwxz20hsR7glCpjwwri8pJv6Uj21y9y-dyYzetFnb0e21B8gV1FXMEJ5djNdK_TMHPush4jJtjN5vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b9746249d.mp4?token=Aj4jpbN3np3bAXcD82h3eeNHKLZqMbAmHKhu-SOhO_88fnSMwBPIG5WrwEE5cdMoxd_0f09nzTHxer-2EGgGHTkLDpIBvP67XkHrymhD0dX2sHpVoVqHbMRjCfsu2ZMdG3MEFq3Ax-Hwg3Abb5UNTdBSB1DBRtZM8yVPGxIeAXkYyl2VkouHHw1g7XfprpL8vPIInlZYUJQrVwg9uCUPgR4CLecEKcNcrW5D5Zn1_a2AyUhmLPK8Ijwy_cb9etqGkjAO8oDSqwxz20hsR7glCpjwwri8pJv6Uj21y9y-dyYzetFnb0e21B8gV1FXMEJ5djNdK_TMHPush4jJtjN5vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : امشب، فردا و فرداشب به سختی به آنها ضربه خواهیم زد و هفته آینده پل‌ها و نیروگاه‌ها را هدف قرار خواهیم داد، مگر آنکه  مذاکره کنند.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6118" target="_blank">📅 06:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6117">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caeb092620.mp4?token=hfvpmXTk_LHvJl9en6Upb1CY-vCK42518e5UWl1TOLvF1Y0mZ-04FDeEXugsWMVtrWQJp2N71O3V-dBngS3emHloDwXRNVxlj2Wt807gc-tuHkrK9E0RHcyOpcg24FKIlY3N_J5O4472NxjZWimdzv5NqEWFBQWg8GHoOdCHyztm1-Xb4972CCyYCk4M8oi20SdJUozVxldv0Y50qFGaRjYTsCMTNqYgMU-sunwpCHXuorW_9nQyji8OVjHBeNUKwEL4xepqAIsdULRocOJ95ud2GWfWUW6yi7FIBnN9eoaUWicThTkP0-yKpD3L3lf1h8MhFZvOmwGviiWtyt3VbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caeb092620.mp4?token=hfvpmXTk_LHvJl9en6Upb1CY-vCK42518e5UWl1TOLvF1Y0mZ-04FDeEXugsWMVtrWQJp2N71O3V-dBngS3emHloDwXRNVxlj2Wt807gc-tuHkrK9E0RHcyOpcg24FKIlY3N_J5O4472NxjZWimdzv5NqEWFBQWg8GHoOdCHyztm1-Xb4972CCyYCk4M8oi20SdJUozVxldv0Y50qFGaRjYTsCMTNqYgMU-sunwpCHXuorW_9nQyji8OVjHBeNUKwEL4xepqAIsdULRocOJ95ud2GWfWUW6yi7FIBnN9eoaUWicThTkP0-yKpD3L3lf1h8MhFZvOmwGviiWtyt3VbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار ناشی از حمله پهپادی امشب سپاه به کویت
گفته می‌شود مخازن سوخت ارتش آمریکاست.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6117" target="_blank">📅 06:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6116">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/360d24e506.mp4?token=FpLt6RpnLFId911WGOzQtNPAgz2m58pu5BvHYvFzR63h0G11cq0N1avFhh2jU4Kf27hYxTAMat1pcdiD5xRTLNZW2ZN2bRxnaq5hFMUUryDLpiJP82iM9sjT4iMaAxLgFUS13pF3QvjpnA51p17f7jTj6pNuqN9MYo8OsaMw58q4Y5ucc0Cvhme9cfYGolbMIN3PqXHwsjj2gmKgTTuZLOizeH9s9RQMuAAI7beMZWXyYC9fkxeTDFKsjCj7qz29ynfq0xlyhRFUbs3ZsuJurzBZAIDAjFjSncYezzuqw2t4CndFiTw8bIM4241jFf7Lvk7Vd3JOfqLnGsmNIQ4apQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/360d24e506.mp4?token=FpLt6RpnLFId911WGOzQtNPAgz2m58pu5BvHYvFzR63h0G11cq0N1avFhh2jU4Kf27hYxTAMat1pcdiD5xRTLNZW2ZN2bRxnaq5hFMUUryDLpiJP82iM9sjT4iMaAxLgFUS13pF3QvjpnA51p17f7jTj6pNuqN9MYo8OsaMw58q4Y5ucc0Cvhme9cfYGolbMIN3PqXHwsjj2gmKgTTuZLOizeH9s9RQMuAAI7beMZWXyYC9fkxeTDFKsjCj7qz29ynfq0xlyhRFUbs3ZsuJurzBZAIDAjFjSncYezzuqw2t4CndFiTw8bIM4241jFf7Lvk7Vd3JOfqLnGsmNIQ4apQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی با موشک‌های حاوی بمب‌های خوشه‌ای به بحرین حمله کرد.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6116" target="_blank">📅 01:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6115">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
ارتش : به پایگاه‌ها اف ۱۸ های آمریکا در اردن حمله پهپادی انجام دادیم.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6115" target="_blank">📅 01:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6114">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">‏امشب اتفاق جالبی افتاده، به محض اینکه خبر انفجاری در شهر و استانی منتشر میشه، مسئولان جمهوری اسلامی سریعا مصاحبه میکنن و میگن دروغه و همه چی آرومه!
‏اینطوری مثلا میخوان صورت مسئله رو پاک کنن.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6114" target="_blank">📅 01:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6113">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nwkyIIJLJqYGFJHvesxuOMlUTmqKKJNQ7FAO4mft6QXLnpk5xE6K4ovTkWF9GoBTY-461E5sQV6koZfD72PpB8dbsStl2qOY9bZm1rZ8Kv7258wzth17dT4YnMYx19DLxb0guT-Q1ZOlZI_Lpdaas07T92WPwv8142XbZr8khxqReENu_W-AwaWw7EDq8fpEwbsBUKaLJYJI9_lGFAjXC8tDx32lKPKHIYnQlyPdo6JJL5FxJ74heuPpgKMzLbR_MJyFaZJnt7ggZGzy6HJjWHJokBwB4LQWx3psaTkchyXdM18jGzgtW-roH9e6OcYiILHPW8Dfw6bu-06VbFLdBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگارهاشون می‌نوشتن که کشتی‌ها دارند  از مسیر عمان رد می‌شوند، تشییع جنازه،  بریم و کاری کنیم که  کشتی‌ها مجبور بشن از آبهای ایران رد بشن  و شروع کردن به حملات به کشتی‌هایی که از مسیر آب‌های عمان میرن.  به زور حمله میگن کشتی‌ها باید از مسیر ما رد بشه.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6113" target="_blank">📅 01:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6112">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AkyV9KhlwNN60lSz5fafcy0HOa5WOkvL-s9_wyVYiENBGcS9JIs79dsyo0tFCWXskq1Hv2-_GczQOwwYpLusgfqhvTTkwKM0RgzryEnfkqP6aeihumeuvYxTe7hZ7meDj9CS3DKWMVbqcbHTgxex0oKx3JjHvgewzfn9mjjEsXlEqWSoxz3vozuI18yWlXrpJ1XsWLZollsw03awAFfS__Zse_23tqj4NCN_XHkVbsTQ_3gcJkgtwx3LiZwoct__uazQvgaAfhAcLIpVHy_oYHSorcdsMekx4avHFInYq_X_N5VllI9eHd3uOA_926YRRvdDSklfF2ipjJlTONLk-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینجا در حاشیه خاکسپاری جسد خامنه‌ای و جلوی قالیباف شعار میدادن «مذاکره با دشمن خیانت است»  هنوز به سه کشتی حمله نکرده بودن و نزده بودن زیر تفاهم نامه</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6112" target="_blank">📅 00:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6111">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d90d3d98f9.mp4?token=jRE_aXh8NbuVxYkbMf-VTOIfggrGU2np15KFv1UcmWzWmTwrPPEfGb98OkvQFxViZyaJ8DshIBaMaObunrNZSzZrKDLi1aBbkMEm-eTUZjVxRU487FhSKC5vr3-8d2s_bD3MqJQ_8zEuHJbIFvz0cxDOf1utwRgrWy6he7KQmyT2BVrLBPX5bqP9adTaSu5T-xA2DhIsHatUdve-JA5KpJtx-lUC7JVH9Vs8jJfrij5J_553Po4Pt7s1H1hXaoXyPnOLWKCDuCNbzCF9-FbMGLNHlKwqHYvU_rxuAyIEeAX9yA-LS2TlfqEKM4AgPja3drkQ_VcU3rw25_i-j-ajvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d90d3d98f9.mp4?token=jRE_aXh8NbuVxYkbMf-VTOIfggrGU2np15KFv1UcmWzWmTwrPPEfGb98OkvQFxViZyaJ8DshIBaMaObunrNZSzZrKDLi1aBbkMEm-eTUZjVxRU487FhSKC5vr3-8d2s_bD3MqJQ_8zEuHJbIFvz0cxDOf1utwRgrWy6he7KQmyT2BVrLBPX5bqP9adTaSu5T-xA2DhIsHatUdve-JA5KpJtx-lUC7JVH9Vs8jJfrij5J_553Po4Pt7s1H1hXaoXyPnOLWKCDuCNbzCF9-FbMGLNHlKwqHYvU_rxuAyIEeAX9yA-LS2TlfqEKM4AgPja3drkQ_VcU3rw25_i-j-ajvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این استوری رو ۶ روز پیش گذاشته بودم  میگفتن آمریکا میخواد آتش بس حفظ بشه ولی جمهوری اسلامی باید «کار دیگر» بکنه!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6111" target="_blank">📅 00:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6110">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/550f13e765.mp4?token=iZB_-o3ctIvN8XcmpEhjBI1Iow6BoMFB3F24l3sBzElQyb0sqSk2iWOFl5aGLLcxbQLtSfYgLPPNrvKXGkg4JJrt6rBHEKSsVBdMk-Kva7gwOdUeM0AAGy2rAfqvpYDpqPz90DmX4yWt07ImTk7IYLcH8B-mhvKycvU1H66ALBRLw1YqqbbIs9c_Y_-ALWz76VffYLXM4DgqHVufyi1pU5ocnLN9uNkZqAmFcyJgn5vkWgZSJLRUyXGMzE3eoMJiR_4e2rfnwEhkOmimQ9XwYCkPJ6hGKyhUOdgBmA2u6ZZxZWjNeGZ4Yrd1yDe7QkfCbwppfll_68z98azUDDUknSlSb-5XafBgReHqfHyBKfeYI5QbHWo3HW_ebK16Zg5PI6ZlPZNBtueQHRtcoEjVWluY_SM0IHmuIhJEz9lKLk_z4BpMkfV0hGQpNyFtZZ5v4oOOz6JjVoF2T2RjIyrj9crX9Q8AVCZlTdIqNah60COUJh25AhQIMeSE1pWZQHxlKGw2tUuOSc6e438LT4dSUzC6ktSGMeTc85YwBRkTBP3PvHufrlkVQsTQppEdS-X3cG-rEXYiy62eirBy3FMsJ-PWk6AoNf8MRNziO_fqzLhaaoGn8pLVctv6QZdToSxhn0pfh0j0x2xN_V42pah-Qkl-SVNVGLHMJ1RJmr08dQM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/550f13e765.mp4?token=iZB_-o3ctIvN8XcmpEhjBI1Iow6BoMFB3F24l3sBzElQyb0sqSk2iWOFl5aGLLcxbQLtSfYgLPPNrvKXGkg4JJrt6rBHEKSsVBdMk-Kva7gwOdUeM0AAGy2rAfqvpYDpqPz90DmX4yWt07ImTk7IYLcH8B-mhvKycvU1H66ALBRLw1YqqbbIs9c_Y_-ALWz76VffYLXM4DgqHVufyi1pU5ocnLN9uNkZqAmFcyJgn5vkWgZSJLRUyXGMzE3eoMJiR_4e2rfnwEhkOmimQ9XwYCkPJ6hGKyhUOdgBmA2u6ZZxZWjNeGZ4Yrd1yDe7QkfCbwppfll_68z98azUDDUknSlSb-5XafBgReHqfHyBKfeYI5QbHWo3HW_ebK16Zg5PI6ZlPZNBtueQHRtcoEjVWluY_SM0IHmuIhJEz9lKLk_z4BpMkfV0hGQpNyFtZZ5v4oOOz6JjVoF2T2RjIyrj9crX9Q8AVCZlTdIqNah60COUJh25AhQIMeSE1pWZQHxlKGw2tUuOSc6e438LT4dSUzC6ktSGMeTc85YwBRkTBP3PvHufrlkVQsTQppEdS-X3cG-rEXYiy62eirBy3FMsJ-PWk6AoNf8MRNziO_fqzLhaaoGn8pLVctv6QZdToSxhn0pfh0j0x2xN_V42pah-Qkl-SVNVGLHMJ1RJmr08dQM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدئو رو دو هفته پیش گذاشته بودم.  معاون سیاسی نیروی دریایی سپاه اینجا در جمع حامیان حکومت بهشون میگه خیالتون راحت باشه، حملاتی که ‌ آمریکا انجام  میده «واکنش»  به اقدامات ماست!  «کنش» نیست!   تمام این ۴۷ سال همین بوده!  یه کاری میکنن ، تنش راه بیفته،…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6110" target="_blank">📅 00:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6109">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">محمد اکبرزاده، ‏ معاون سیاسی نیروی دریایی سپاه، ‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.   او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.   جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6109" target="_blank">📅 00:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6108">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0b9d2dcec.mp4?token=TNS-TR4ljhzSvQoxmilu7NioXZ92FLVAo-H97K401SqVNM8xuIZ-cK9vv7RdoHKF9qjAVBX85cNc6CtXClrhA4g5mjfvuUrSWV4CTVpTg1Mc8hFGrlD6Y_fEqFnazS2qYFla5Q-t5XKJv4oPHSFvrr85ywiRnKdCYrFcP1bS_aQSFmEwU006bjk9Pu2KFq93FcUJ8SgFlbwOxo-blwMxiRIh537iwOLL5zkm8Ly0HUnavjkPv-uz0-O9CpVRPN8Mt9Nw01bObolHTxBVe1mmuDnd7qGY7iU-GbYWHn7KwYfjMyjUbmZmKYp3y83f-LQWC-ezKuz5Ou1aA-sFchQbjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0b9d2dcec.mp4?token=TNS-TR4ljhzSvQoxmilu7NioXZ92FLVAo-H97K401SqVNM8xuIZ-cK9vv7RdoHKF9qjAVBX85cNc6CtXClrhA4g5mjfvuUrSWV4CTVpTg1Mc8hFGrlD6Y_fEqFnazS2qYFla5Q-t5XKJv4oPHSFvrr85ywiRnKdCYrFcP1bS_aQSFmEwU006bjk9Pu2KFq93FcUJ8SgFlbwOxo-blwMxiRIh537iwOLL5zkm8Ly0HUnavjkPv-uz0-O9CpVRPN8Mt9Nw01bObolHTxBVe1mmuDnd7qGY7iU-GbYWHn7KwYfjMyjUbmZmKYp3y83f-LQWC-ezKuz5Ou1aA-sFchQbjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گشت زنی اف ۱۸ آمریکایی بر فراز چابهار</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6108" target="_blank">📅 00:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6107">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا : محاصره دریایی ایران وارد فاز اجرایی شد.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6107" target="_blank">📅 23:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6106">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
چندین انفجار در بندرعباس
🔺
چندین انفجار در اهواز
🔺
پنج انفجار در قشم</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6106" target="_blank">📅 22:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6105">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQkzrnxRoefYII4U7S9bnJ0WYKlZThelEsRNrA9zU9UjtVn08RkK0_rxucC9xJaqTZHb3BTT7wPjIjzjG1t2kjiFtC2ndjilxUh8bFl2ovKmF-6fRlb59NO2XoaTht4i28FVmfKBx3fXkF56pSbzds2KKqRNQhhTrTVP1BHMcKIbm0RPd-VzREYJS5tagFHv-oWObSnpBr4ws72XphuoRlL4JMyXJoe2lTn_H1Cgoa1vrSNeO3vPduNBMURnEundrESIo3qVb0BNhfuWdGqYBcp1eI3Dg28589mvDz49iZP4XxJAROtvuTsHs-bguBu2rlBmzU9wHceDQAPWll1hQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2077085449948938568?s=46</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6105" target="_blank">📅 21:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6104">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
دقایقی پیش : حمله به قشم و شنیده شدن چندین انفجار
🔺
حمله به یک نفتکش اماراتی در سواحل عمان
🔺
فعال شدن پدافند در کویت</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6104" target="_blank">📅 20:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6103">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
ترامپ به فاصله ۲۴ ساعت، از ایده گرفتن ۲۰ درصد سود از کشتی‌های عبوری از تنگه هرمز کوتاه آمد.
«به لطف نیروهای نظامی آمریکا و همه اعضای قدرتمندترین نیروی نظامی جهان ــ با فاصله‌ای بسیار زیاد نسبت به دیگران ــ تنگه هرمز برای تردد همه کشتی‌ها باز است، به‌جز کشتی‌های ایران. و این هم به خاطر رهبری دروغگو، خشونت‌طلب و شرور ایران است که این کشور را به سوی نابودی کامل سوق می‌دهد.
بنابراین، ما
یک محاصره کامل
اعمال خواهیم کرد، اما
تنها علیه کشتی‌هایی که به بنادر ایران رفت‌وآمد می‌کنند یا هرگونه محموله مرتبط با ایران حمل می‌کنند.
بر اساس گفت‌وگوهای بسیار سازنده‌ای که با رهبران خاورمیانه داشته‌ام، تصمیم گرفته‌ام
کارمزد ۲۰ درصدی بازپرداخت به ایالات متحده
را با
توافق‌های تجاری و سرمایه‌گذاری
که کشورهای مختلف حوزه خلیج فارس در آمریکا انجام خواهند داد، جایگزین کنم.
این سرمایه‌گذاری‌ها عظیم خواهند بود و در عین حال برای خود آنها و آینده‌شان نیز فوق‌العاده سودمند خواهند بود.»</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6103" target="_blank">📅 18:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6102">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vnc7501NA1bcAq-IYU-ZYmdY1tVTKBZT_QgK_8RlGVMdS0mT3O13M-30B2vKYvoddaAmpi3z5bpuL0egTqH_gjMHQrwjQuyMTW_Siae8M4bRwyjqoU8ve0VqioGUvHMTk6yerIo6IWPC6pQ2OtC2Sz_eO1MROiwaEMNY3H9IE1ST2lNX5BsjDW1x6puRTfUsIqK4GFEsBZXbgGhaFK_AgQfw5z4jKK-wva8rUimo7nqywdGrWQuJvgQOrskqw-WEt3jYP_mgmmVmsTG3jzcrXThbgPzOna3R6nLra4L-SsSiRVtqjD2CxAq1dYnv-3FdcSejyrbk-4DUwuy_lER1Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهپاد‌ها (قایق‌های تندرو بدون سرنشین) آمریکایی این مدلی به یکی از مهم‌ترین مراکز نیروی دریایی در بندرعباس نفوذ کردن و حمله کردن.  گفته می‌شود که در این حمله یک زیردریایی ج‌ا را نیز منهدم کردند.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6102" target="_blank">📅 18:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6101">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee96f6523b.mp4?token=J9hDR09ILUB69mDwCzBKGvvoD6nEYehxthV7rPIN6TLfhrby7k7jrUNsiqJ54br9de3xufNwbtOERy4Jw4Q8gshqWgZcvHep8li5oIQaiOjyGEYuCCmK5of5pVV4g5pHgDewNfYH093nUeHLNR3l8lKb2ns7IRIWDRqTg6ebsU8pqvg4l5t6d-sR8qwcRWVUfsrB7p7xddFhHn8rwDP5TGU-HZQZAzwptcaldIMXHJaEzdVP8431aJQfuNg_3ovGmsAGXLMJq4rWh3JQfmtZYm_vqYC2H2nK4a9ONjPGA_kZf5YELXlu1551iIFG9Z_8sEOqJAcVZykVWZy3KKmr5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee96f6523b.mp4?token=J9hDR09ILUB69mDwCzBKGvvoD6nEYehxthV7rPIN6TLfhrby7k7jrUNsiqJ54br9de3xufNwbtOERy4Jw4Q8gshqWgZcvHep8li5oIQaiOjyGEYuCCmK5of5pVV4g5pHgDewNfYH093nUeHLNR3l8lKb2ns7IRIWDRqTg6ebsU8pqvg4l5t6d-sR8qwcRWVUfsrB7p7xddFhHn8rwDP5TGU-HZQZAzwptcaldIMXHJaEzdVP8431aJQfuNg_3ovGmsAGXLMJq4rWh3JQfmtZYm_vqYC2H2nK4a9ONjPGA_kZf5YELXlu1551iIFG9Z_8sEOqJAcVZykVWZy3KKmr5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت جنگشون :)</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6101" target="_blank">📅 16:39 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6100">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jxJgA0ItxrdEihfhsjYLF_DGEoefX2OwsCA_w41wNBSXP0z9t_xZyw2wmuw-5udRLvvnXaBghJYjub943FuyUicN52HTVnvNYSlyiRQNaj6dcS9Rpc9Q2I3SHmJ1jaDqpo3xPGAEcgUO6XdtmKt9Phr-JxpFlgP-zm0WhysuBVaihKpwnOQvfz4qTZLoAFGqC1sIbWZ3M9i2IxX-Zj3rDIJSJTLtuF0t3MoaLat8ju7H04vKIrAP_1pnCzNnAmsPWgsvOQ3RxV25n9Z-VO8h_SK4MKLz7VnXx7Rjp7gQU0TTV92ybWVi3BuGCSv0JMwqhg5nzEO-rpX0ttA_CTYAaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏آمریکا با استفاده از سه قایق بدون سرنشین (شِهپاد)، پایگاه دریایی دیروز بندرعباس را هدف قرار داد و تأسیسات نگهداری زیردریایی و کشتی را منهدم کرد.  این نخستین بار است که نیروهای آمریکایی در نبرد از قایق‌های تهاجمی بدون سرنشین استفاده میکنند.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6100" target="_blank">📅 16:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6099">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">۴۷ سال رژیم اسلامی</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6099" target="_blank">📅 15:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6098">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LyKpmdbi57hhkQy_AybuP5t3S9_XOYjJPziRDwwA2Bqzn_JDHLEgqiyc-le3mwhtKslpbEiYR2l79JhKYdxvU2itTHv1MgsgZykM4NBny5zfxnx1f77mxX5ZMBgG7XYefhlWjHxOQXwhgYpEFerkxzWOrhL13af3k-26A3SizGv64jpOtQTqTabkqm7-9wUaoM_-NDUoSWRXOvigGax5_GLLafvRNPTX1T3vEeha6BbNPo77WjpcA8PxHjNE7j-WLJsvZ2kmFe3r0E1Ya_pZPn43IwIUwSffF6BN2HZBpIDMla_pwsWXsljN3G2iKjuT3eqkS9oEqsHF5MpQiaTQ8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
تخریب ساختمان مرکز آماد و پشتیبانی دریابانی نیروی انتظامی ⁧ بوشهر ⁩ در پی حملات هوایی ⁧ آمریکا ⁩ به مراکز نظامی جمهوری اسلامی</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6098" target="_blank">📅 15:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6097">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
حمله به آبادان و ماهشهر
معاون امنیتی و انتظامی استانداری خوزستان:
🔺
امروز سه‌شنبه ۲۳ تیرماه،
در ساعت ۱۳:۲۵ نقطه‌ای در شهرستان آبادان
و در ساعت ۱۳:۳۰ نیز نقطه‌ای در حوالی ماهشهر هدف اصابت پرتابه قرار گرفت.
🔺
حادثه دوم به دو انفجار شدید منجر شده و جزئیات تکمیلی پس از ارزیابی‌های اولیه
اعلام خواهد شد.
🔺
جمهوری اسلامی در این ۴ شب و صدها مورد حملات، هرگز اعلام نکرده که چه تاسیسات
و مراکزی مورد هدف قرار گرفته‌اند.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6097" target="_blank">📅 14:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6096">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac9c510f4f.mp4?token=jjRfwFb1RCMe49JdDjktlo3KtHzU5HkNacLSmfjRvr_NN1YbtxaddTkicmStHiqGW0_t5vJpVPTwXHAVFM7ffy1wkcc8ibKTL-6TPLtEIVsJRgRUGfPBMWOuCxXOb7-nLLNVaWdvbLFBfs2kNtwknAY5d4oi4CYd4MeIkkMrKxi1bkx5Pmtbk4HJi53n__8WDSawrjQtdWUsrayX_s3KpM-1SlNJc-t6PMkVJlqEYFpaSWDNuW9M9djha9LyoOO5BAaQUulTK3w4FJI81r4ngB3qEIiDuFmPAk9-unVfbyE1PntlCEk8RknEDnyTmzrUlSuYkzyOcdGarIPTeMzOfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9c510f4f.mp4?token=jjRfwFb1RCMe49JdDjktlo3KtHzU5HkNacLSmfjRvr_NN1YbtxaddTkicmStHiqGW0_t5vJpVPTwXHAVFM7ffy1wkcc8ibKTL-6TPLtEIVsJRgRUGfPBMWOuCxXOb7-nLLNVaWdvbLFBfs2kNtwknAY5d4oi4CYd4MeIkkMrKxi1bkx5Pmtbk4HJi53n__8WDSawrjQtdWUsrayX_s3KpM-1SlNJc-t6PMkVJlqEYFpaSWDNuW9M9djha9LyoOO5BAaQUulTK3w4FJI81r4ngB3qEIiDuFmPAk9-unVfbyE1PntlCEk8RknEDnyTmzrUlSuYkzyOcdGarIPTeMzOfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">می‌پرسه نظرتون درباره اینکه بدون هشدار قبلی برق رو قطع میکنن چیه؟
‏چمران میگه:
‏شما اگر بدونید پریروز چند نقطه برقی رو زدند دیگه این سؤالو نمی‌کردید.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6096" target="_blank">📅 14:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6095">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KyFTjeZmPLc2uqq_TtciTNr4olMEgXMGuhEJpV82Di1gc2NRwvIG15eOdfFbJsAZK_xllJSXc7DrT_OIkVcq31Z2KMV5GCovZnsEyEAz1qXvkjHWQWWswJsFx9pmkzjNrIKVfMh5zayOEMD9lcr8lVAZDxtKjv60kK4Wt2ynJdaZwyK1T59ah4QAvK7DyY_Z5AIrrczTf9XkPufzYV5rWCGgpfOuwpX9Hy4ssuYd9SY7PnS-Rt686j7CGa2hbcXXI1lnx0VRWyPmxo0LWuRhu_UKMdpdly8ItrBSTWWTzfL6C2-PHtJVTWATmjIZniD766RsvQgbBGhNZpMADMDJhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه ترکیه، دیروز جمهوری اسلامی
رو با اسرائیل مقایسه کرد و گفت
رفتار این دو شبیه هم هستند.
(کاری ندارم که ترکیه خودش چه افتضاحیه، اما نشون از تغییر رویکرد ترکیه نسبت به ج‌ا داره)
یادمون باشه فرمان حمله اخیر از سوی ترامپ در ترکیه صادر شد! یادمون باشه معاملاتی بین ترکیه و آمریکا رخ داد، که آرزوی ۲۰ ساله دولت ترکیه بود.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6095" target="_blank">📅 14:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6094">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
🚨
حملات دقایقی پیش به بوشهر ، خورموج و….
🔺
سنتکام چند ساعت پیش گفته بود که این دور از حملاتش متوقف شده.  در اسامی شهرهایی که مورد هدف قرار گرفته بود هم مثلا نامی از کیش نبود!  مشخص نیست آیا همه این حملات را آمریکا انجام می‌دهد، یا کشورهای دیگر (مثلا عربی)…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6094" target="_blank">📅 13:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6093">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AJ87EgkJpHBetQS_tczx0xEeXBvpgcuqy8kb6movy1UGSdoB4dW0J78AiaQr7fvek_Sn0mwPgMEZ6BtspZiuDz8QZHOYdDL2-WqguarTgyB_DzfzRYMnlVkw8Ev3lcdExCWOOLE5XEleextqbJlxis1kFwu7O3UchVQScZt1yqQzvcdTPDwIPs_zVc1PBoPmgzSDqZ7xtIcxwX4UkdIteUoeqVzGKLL1evdXyBOG2vPNE09_IZtBePsCP9k8axSWPFyXfyraGnbpeiBFhAmJUcwc6CazI8PgC7hTqWWcaS_LJHb2vIzJZ37Pq_D9dpEZ33CS1h_nFmaoKFJ-elyeeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حملات دقایقی پیش به بوشهر ، خورموج و….
🔺
سنتکام چند ساعت پیش گفته بود که این دور از حملاتش متوقف شده.
در اسامی شهرهایی که مورد هدف قرار گرفته بود هم مثلا نامی از کیش نبود!
مشخص نیست آیا همه این حملات را آمریکا انجام می‌دهد، یا کشورهای دیگر (مثلا عربی) نیز در این حملات مشارکت دارند.
🔺
دفعه قبل هم که امارات در پاسخ به هفته‌ها حملات جمهوری اسلامی به جنوب ایران حمله کرد، مقامات ج‌ا تا چندین روز نگفتند که کار امارات بود.
الان هم برخی از این حملات مثلا دیشب، با حملات دقایقی پیش مشخص نیست کار کیه.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6093" target="_blank">📅 13:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6092">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b04e0dceb0.mp4?token=hrK6dPRnictY5aJ7K7GSqoO110lTb4WVACp6bgt2KuNEtdD1kcO1Zzdns94X27rDUxK-WE_bzon1I0rt_SqWHS6nEMBUYGo2s2u2YEQa8mr9dQi7GSXCxBwNGsp2ltkAgk5NUqfizu9Cz9vAePGFqFbgZ2gNWkTv-MXMQDJatvRKBKK7bHKMcmwxKUsukNd_RfvITm0Vkssj5BP0lYBxwbMRLaGEzSivVpObgKzUrThFsbtni8AZZS0uLuYOEV2rdukuO_8t8emapc0PD8I8ybsVINazL9XsfDzCsdJxRP-a0i58OOO_pDy989LlqbwaGXABRXiaDxs1dnRh4qNlghI5xHfsG7LUDqJOm9SsqtjUfkOZMZAXOJbC0SiNrXF5ar5VZxHsJuBgcHk4c1zMBdeHloDePUjgvR4YXdgk8XwNROayE3BmTGCGcz3p59HuiXJHcYHoXx1r0LII0S2i4rAvWDXIQkA35lFzUGbBtxBCxhf_1VxxZJOThtn7G6xTzFV5r7ykY79kJYinJJePCKtQjlKyYEC9Jm63kswSEj_rAv9KfLxdK6i-62QF2VFRC4BcKWGl8l3mmJR8bNj-0LcbCKFaBLdfVsNWOSqy2q1e0WKa1X6GK4Wx096hUcnUPZG079oom77YwK57FUQnIq4CcatB_KESeAJH-5DwrC8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b04e0dceb0.mp4?token=hrK6dPRnictY5aJ7K7GSqoO110lTb4WVACp6bgt2KuNEtdD1kcO1Zzdns94X27rDUxK-WE_bzon1I0rt_SqWHS6nEMBUYGo2s2u2YEQa8mr9dQi7GSXCxBwNGsp2ltkAgk5NUqfizu9Cz9vAePGFqFbgZ2gNWkTv-MXMQDJatvRKBKK7bHKMcmwxKUsukNd_RfvITm0Vkssj5BP0lYBxwbMRLaGEzSivVpObgKzUrThFsbtni8AZZS0uLuYOEV2rdukuO_8t8emapc0PD8I8ybsVINazL9XsfDzCsdJxRP-a0i58OOO_pDy989LlqbwaGXABRXiaDxs1dnRh4qNlghI5xHfsG7LUDqJOm9SsqtjUfkOZMZAXOJbC0SiNrXF5ar5VZxHsJuBgcHk4c1zMBdeHloDePUjgvR4YXdgk8XwNROayE3BmTGCGcz3p59HuiXJHcYHoXx1r0LII0S2i4rAvWDXIQkA35lFzUGbBtxBCxhf_1VxxZJOThtn7G6xTzFV5r7ykY79kJYinJJePCKtQjlKyYEC9Jm63kswSEj_rAv9KfLxdK6i-62QF2VFRC4BcKWGl8l3mmJR8bNj-0LcbCKFaBLdfVsNWOSqy2q1e0WKa1X6GK4Wx096hUcnUPZG079oom77YwK57FUQnIq4CcatB_KESeAJH-5DwrC8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجتبی خامنه‌ای «علی الاصول»
با تفاهم‌ مخالف بود!
و نوه خمینی هم این چند روز گرد و خاک به پا کرد و گفت هویت ما در مبارزه با آمریکاست!
اون‌هایی هم که نگران زیرساخت‌ها بودن
الان سکوت کردن  و صداشون در نمیاد!
آغاز دوران «علی الاصولی» !</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6092" target="_blank">📅 09:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6091">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">سنتکام ساعتی پیش
از پایان این مرحله از حملات خود خبر داد و نوشت :
🔺
جدیدترین موج حملات خود علیه ایران را به پایان رساندیم
🔺
در این عملیات پنج ساعته، به اهداف نظامی در بوشهر، چابهار، جاسک، کنارک، ابوموسی و بندرعباس حمله کردیم
🔺
سیستم‌های دفاع ساحلی و موشکی، سامانه‌های پهپادی و ظرفیت‌های دریایی ایران، هدف قرار گرفت.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6091" target="_blank">📅 09:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6090">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p3BZbUxfGCsKpCqaFx7dr2Rx56DAAo6o4BppETK2mPmZaHOCLDj2Y1nTlxWWgelLviud8aBAuPoBEMY3muB8BKbNI9Yffog-OksopTVUGS-okYwF6DYl7Jpy2kqF0BzsYnu710wkxCGp57kQswhgH-HSYQMMPXKwDPCgewQBxKxjDZnW24jUHF1C_3-X3STf7f1K16EnYbYxLSl1SOAfBlNfUEaoQlqaPwPlf4_mf0HIw_socBxb6E1v0mBj6UOCYM-_qqn82Okye2cKUWLwK3eT_jeUforXAxfKNA1e7ZqBd5lAPhRXinmYJvUF4CvHybLOLIT42eo7m_AOJAVdfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شب گذشته سپاه به دو سوپرنفتکش (در سواحل عمان) حمله کرد.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6090" target="_blank">📅 09:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6089">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/671b861555.mp4?token=gW11UoyPtege7kJvaY69D8UShSDXu6O8B-WsEpgT55kJvA2onf1WDWb9MGfcVJPPvYHBumqGMbnlJlUQaIlF0wgqjuAgB1BKPS9hvoALRNIMY2_IYSMUHB85IEa-Jh-s477_tSzRoQZTrpLzn22SvfEbUWESZ9pN-oBnd8Z7I2-7icQnooPrgqB3sE21OoRgEMvXl3gvs-dyHd2kSFGF32MbIEjD-9omHrRxGkF1Nllh2_ZTI8vXdXQ2_LpMS1WjD_OhxYZMm9qF79XVZrGiSAl56l1sc9WQ1WdD5yUosxdvjPgiKxmQ5Yw0qxfDAMGUZcHYhCpoIOiFiaigdGz5ESa1-78A9b96SUHRGxH0pY55LtnsFdgnONLNT4ooXQNOBf7PdA0BKXBFGnm6vfrnVnTYN0AdmW2PtL-hduE6FdD9Q0_PsXjvu0esJeeFAvYpqx3ES-CUUMqoyv7iUOYa_L_QLL0EcZ4N_5j3CFPoBlz1jIZreKX6LqcFQkqmRP0gU0OON6Nz15A6_ZXFDEG9T1wUAwfTGqRkvNfdTz34JpLlmiTDgHKczsEx0VQ90CYvYjNkARGWI40bCNgGN8mgX42nEt4OrxaDQBirEKLCjO0bWVEORVCp4ZX15Hub7xgZ12ie9Osbvs-9BQYLlJfrrzfCij3zGuIAhsCwcKteiNc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/671b861555.mp4?token=gW11UoyPtege7kJvaY69D8UShSDXu6O8B-WsEpgT55kJvA2onf1WDWb9MGfcVJPPvYHBumqGMbnlJlUQaIlF0wgqjuAgB1BKPS9hvoALRNIMY2_IYSMUHB85IEa-Jh-s477_tSzRoQZTrpLzn22SvfEbUWESZ9pN-oBnd8Z7I2-7icQnooPrgqB3sE21OoRgEMvXl3gvs-dyHd2kSFGF32MbIEjD-9omHrRxGkF1Nllh2_ZTI8vXdXQ2_LpMS1WjD_OhxYZMm9qF79XVZrGiSAl56l1sc9WQ1WdD5yUosxdvjPgiKxmQ5Yw0qxfDAMGUZcHYhCpoIOiFiaigdGz5ESa1-78A9b96SUHRGxH0pY55LtnsFdgnONLNT4ooXQNOBf7PdA0BKXBFGnm6vfrnVnTYN0AdmW2PtL-hduE6FdD9Q0_PsXjvu0esJeeFAvYpqx3ES-CUUMqoyv7iUOYa_L_QLL0EcZ4N_5j3CFPoBlz1jIZreKX6LqcFQkqmRP0gU0OON6Nz15A6_ZXFDEG9T1wUAwfTGqRkvNfdTz34JpLlmiTDgHKczsEx0VQ90CYvYjNkARGWI40bCNgGN8mgX42nEt4OrxaDQBirEKLCjO0bWVEORVCp4ZX15Hub7xgZ12ie9Osbvs-9BQYLlJfrrzfCij3zGuIAhsCwcKteiNc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: بیشتر موشک‌هاشون رو از کار انداختیم، بیشتر پهپادهاشون رو.
🔺
توان ساخت پهپادشون رو حدود ۹۲ درصد از بین بردیم. توان ساخت موشکشون رو ۸۹ درصد نابود کردیم.
🔺
یه کم توان براشون مونده، اما برای ما هیچ توانی ندارن. این دیگه تقریباً یه درگیری نظامی کوچیکه</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6089" target="_blank">📅 08:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6088">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3962370842.mp4?token=Z_mTgYhztS960-yCYE26uUIihn6VgikHCPMHdQI1i-gcrkz46LWgVfzc1kIkz1665psLSbHxHklH8Uc5jd5paTUi3lYh2DFFai6dQvVL-VAni1CzZ_65MG3Kp2dLoq0dwBDMwgzf0nfM3wSju852qF14x1xypikP4x504Z6d5TzcmnOu3lc7ZFVNh4fouhGGCAjw3ebNpMpDTvzEAFTbf5GpEGeh08fQGwFkLpf6BLoOoAZkL-jdfWGchoTh1_yVGOVIk-8B-MagOnO6mPhQMQNiQcuLcVopRJaLkoMfaEGMszh2hXICH6BIpeJy9pVVo0s4x1COFCXktF5u3_sFjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3962370842.mp4?token=Z_mTgYhztS960-yCYE26uUIihn6VgikHCPMHdQI1i-gcrkz46LWgVfzc1kIkz1665psLSbHxHklH8Uc5jd5paTUi3lYh2DFFai6dQvVL-VAni1CzZ_65MG3Kp2dLoq0dwBDMwgzf0nfM3wSju852qF14x1xypikP4x504Z6d5TzcmnOu3lc7ZFVNh4fouhGGCAjw3ebNpMpDTvzEAFTbf5GpEGeh08fQGwFkLpf6BLoOoAZkL-jdfWGchoTh1_yVGOVIk-8B-MagOnO6mPhQMQNiQcuLcVopRJaLkoMfaEGMszh2hXICH6BIpeJy9pVVo0s4x1COFCXktF5u3_sFjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات شدید به کنارک - امشب</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6088" target="_blank">📅 01:06 · 23 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
