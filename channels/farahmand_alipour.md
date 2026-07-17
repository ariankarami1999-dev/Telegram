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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-26 20:31:51</div>
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
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farahmand_alipour/6188" target="_blank">📅 18:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6187">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o23JcAiz3J-Icg3U2M2NzvMMdb40oPmFoaBYdlEUwYBjyhuN5b7h2IyB8XgQrGu_Dq7InpDe7TcU2ZambOI_wXSGPPLisXRqSm0xPvHzpWORotmFzWGypHPDRcs28w5fgyeAPgPX9tmcEit4U8j9ZNBkqD25XpgTKaBzyczAQNroCMUmhkA_u6H04mdQtYeTzyX2ghvNenOWyuC42uvE645ZfSEQuwM6bftXXPSROfKTqucxUJy8Aa9k8LJWwmH-QDEjrouQMl89LJ258sbqW6S1tVKp-PMIp46gh9b6vqZvF-z-Z8kH5YlZDHes4FG4ujPhCMiuflxA-C9mAuAtDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب طلاقش بده :)
چرا اینهمه کینه؟</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/6187" target="_blank">📅 18:21 · 26 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/6186" target="_blank">📅 17:28 · 26 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/6185" target="_blank">📅 15:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6184">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ijt5NRK3bltsYCoHkEWDkhrcfi5qZ--8GXUF5P3-8IK0TPqriYcGaj_rju2tJ7vUgwYsS5u9HmUMtsvwofBpwQIY_G8VauO1lhDEPE79BAXOnZcWgApkjZp8GP76Nxi2zQQ9wVFiPyWCkbhC-9yvd0w_1ZnHvvy65JIPelk236nzSTkWZJOOo82ttchl91wf8Wqd9mCD7pIa5mPzdbLXD1iNMUNym65cPe24AyUPfo20PC1xb_MnWNYdf5MmiJ0HfjfWiWjCciXf3-nfQwoVq71WQBin3R_7y7TWbh_DZcycgfxnLxzhmpI6d4g18W17wla0suaespRUpAdDgjiyJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جمهوری اسلامی به تاسیسات آب‌شیرین  و تولید برق کویت حمله کرده.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6184" target="_blank">📅 14:33 · 26 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6183" target="_blank">📅 14:31 · 26 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6182" target="_blank">📅 14:13 · 26 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6181" target="_blank">📅 13:52 · 26 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6180" target="_blank">📅 11:48 · 26 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6179" target="_blank">📅 09:28 · 26 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6178" target="_blank">📅 08:58 · 26 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6177" target="_blank">📅 08:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6176">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔺
معاون استانداری بوشهر:  شب گذشته ارتش آمریکا با چند موشک به پایگاه‌های هوایی و دریایی بوشهر حمله کرد.
🔺
خبرنگار صداوسیما: دیشب به تأسیسات برق و مخزن سوخت فرودگاه ایرانشهر حمله شد.
🔺
دیشب ۶ پل مورد حمله قرار گرفت از جمله پل‌های رفت و برگشت بندرعباس - لار …</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6176" target="_blank">📅 08:52 · 26 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6175" target="_blank">📅 08:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6174">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
حملات شدید به بوشهر</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6174" target="_blank">📅 01:09 · 26 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6173" target="_blank">📅 00:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6172">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iYCu8XrF-1WqfnO07o-fr9OaKRkYH1w8FqQMzfE9ZZDlMdXe3zyxME8VlPcIdomEPmFYv6E6wgnaYe7qNwZ1AyBqGhZuogz80itTU6NtXBkS0y3gAjYL9gwZ55u7zFKCD9SOlrEVg1hYxeeZexZNr89hUAV9Ifaeqa2MaFh0Q6F_h8Cp-J3H_r2I_g6ZwkFRUt1kWI6L1SKqFJAv_IbJMHdEt9vwTzRYkyv6bY55NmmA_mcih6bOVpyK58g9LTH4SEY_vNrImKx_28PZV2h7RRdQsvVwPblwpLzBdEeugkG3pRXNeHeyQ1oHW1hZBvzV8IVIABR6U_YGDiHuKssflA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله به یک پل در اطراف بندرعباس خبرگزاری‌های داخلی : پل ارتباطی بندرعباس و لار و شیراز  بود.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6172" target="_blank">📅 00:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6171">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
صدا و سیما :دقایقی پیش ایستگاه انشعاب راه آهن بندرعباس از سوی دشمن آمریکایی هدف قرار گرفته شده و ۲ هموطن مصدوم شدند.
بندرعباس مهم‌ترین دروازه واردات و صادرات کشور است و شبکه ریلی بخش بزرگی از این حمل و نقل را بر عهده دارد.
این حمله می‌تواند به حمل و نقل کالا ضربه بزند و به آن اختلال وارد کند،</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6171" target="_blank">📅 00:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6170">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
حملات گسترده به حمیدیه و شوش در خوزستان</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6170" target="_blank">📅 23:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6169">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
حمله جنگنده‌های آمریکایی به فرودگاه ایرانشهر</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6169" target="_blank">📅 23:54 · 25 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6168" target="_blank">📅 23:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6167">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/snfCVrf4qe0R_L8_knidvAytRTwV_wifsPR1h84eDdPiliH8_t7gxLVNoq-EGPnSHGwyBVRVSI8M6qjHpO6SBimhQ6NkfPwKD3Mh4uUxXsiThKW2qi0dZrhqizj4_iipuumEGduC13lS2u5YyV_gfjqXYDrLjhkJrqe9d9AnxsN60l9ZiZzK_3QjBW3hqdSYlXN_k0A3j_uUJyyNjr2U3wApBDbAIIwlnx2uNtMcGJygDe2OTiKHlM7S-MP4lXLTA7G65hX40qNZpDP-BDFM4_eENnT_M_g2OqddC41QLg8Fr-_slwukE-lxxYQi1zRAjZSwI96Khbpinfl1tOCFQw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6167" target="_blank">📅 22:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6166">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48c1ef79b3.mp4?token=TF_rr_1_viDP1jogVOyOyFp2WcODoM7FzaOhj_oaLWljiTiHTy6DHyRFasgWYASJnuw4c-4hFp5qRsw0slphkfp2QaAd1nr6qM-HzzxWg_s8C3gmhpJZUDC04QphNV4C5uDXOwskcsZJMIAeFwIGirGc9FyhKl8vyAVAeL_N6zNr2kbmzSO83QVAdZu7QJQMvi5GQHt63hPD5ouyKRMp2guYhS42DkyjrX5yHVkvdM02sudYqbxLSmquAgbleDnramKwYkNuHetZG2qUfcfXryGyEIWQ7V3WbPAAWWHuHUq1Q0z2GwmnhnynWBxy7s2WK_gSaxmVCGbPomrLhkaG6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48c1ef79b3.mp4?token=TF_rr_1_viDP1jogVOyOyFp2WcODoM7FzaOhj_oaLWljiTiHTy6DHyRFasgWYASJnuw4c-4hFp5qRsw0slphkfp2QaAd1nr6qM-HzzxWg_s8C3gmhpJZUDC04QphNV4C5uDXOwskcsZJMIAeFwIGirGc9FyhKl8vyAVAeL_N6zNr2kbmzSO83QVAdZu7QJQMvi5GQHt63hPD5ouyKRMp2guYhS42DkyjrX5yHVkvdM02sudYqbxLSmquAgbleDnramKwYkNuHetZG2qUfcfXryGyEIWQ7V3WbPAAWWHuHUq1Q0z2GwmnhnynWBxy7s2WK_gSaxmVCGbPomrLhkaG6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئویی که گفته می‌شود
از حملات امشب به بندرعباس است.
دقایقی پیش بندرعباس ۴ بار مورد حمله
قرار گرفت.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6166" target="_blank">📅 22:13 · 25 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6165" target="_blank">📅 21:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6164">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbd6cb3b5f.mp4?token=N-n8tKOaslbn8E5640W6qOqoocPCaMvnL04Iw7QWHoUhxrcX-O23ch62ORudSNnqRAoHgLcoLEttcC6z7NNijKNFaloSj-5dEJs0y11fJDbcJ9kimlep0HRE_0TWdjgKUs18dMDYB4dKfTJDHM-3OJjA-Cx_1EuIqXHeX4PErGg8iDDVTctltxoh7R-GnF2YUf6ahvN9C95w_GnJSAAEYp0K_aU7a0BkKMMzhDpzeo6g1WsUtss8Wv3AHmu9oqUxjje2j_zwl3PytiQPAxBaam7RCBBE-CCIEVigGkf2uNzOfXr1CXkjYq9eUjl6tCEz-rzbJ97AwD__IU-og4iCAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbd6cb3b5f.mp4?token=N-n8tKOaslbn8E5640W6qOqoocPCaMvnL04Iw7QWHoUhxrcX-O23ch62ORudSNnqRAoHgLcoLEttcC6z7NNijKNFaloSj-5dEJs0y11fJDbcJ9kimlep0HRE_0TWdjgKUs18dMDYB4dKfTJDHM-3OJjA-Cx_1EuIqXHeX4PErGg8iDDVTctltxoh7R-GnF2YUf6ahvN9C95w_GnJSAAEYp0K_aU7a0BkKMMzhDpzeo6g1WsUtss8Wv3AHmu9oqUxjje2j_zwl3PytiQPAxBaam7RCBBE-CCIEVigGkf2uNzOfXr1CXkjYq9eUjl6tCEz-rzbJ97AwD__IU-og4iCAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ازغدی : اگر میخواهیم اغتشاش نشود
باید با آمریکا مبارزه کنیم
(که حواس مردم به جنگ پرت بشه
و تقصیر کاستی‌های حکومت بیفته پای جنگ
و دوباره جنگ بشه «نعمت» !)</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6164" target="_blank">📅 21:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6163">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
استانداری هرمزگان:  در ساعت ۱۸:۱۰ امروز نقطاتی در قشم مورد اصابت موشک‌های آمریکایی قرار گرفت.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6163" target="_blank">📅 19:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6162">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IOTu7yyL0UY1G7TfKuHXJatuWamRs5UmEZar3Czyi2HHzgliFyGUb0HoxJZvzUVzOtr64PHQ-2kWvRMRIkaR7PeLT_T-owF5JBfj46PkT9I3V2sS3dIV7Dt099xkThFnSKITtByqTRObOwP6c5Jb9h6cB74W-zHNjF4NfPqTKUKvQlm4oi-Rym7ZfBjO2Ktwwdu6gHfhF7ymp5zmXnABjNijlnr_wZaUmRywK3AbVyRWOBGYCt4Jsz5-ZOUJRvnYz6s2JYkYew3g-TXgtQkkYAItvLY_ov5U2pJhNx8qcRZeBAHBK20WCC7qlMM3mHwAGnXtwvLNZXwkMMzR0pfOPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رویترز :
پاکستان به ایران هشدار داده‌ که اگر به عربستان سعودی حمله کند، پاکستان آن را حمله‌ای علیه خود خواهد دانست و اعلام کرده‌: «این خط قرمز ماست.
»
پاکستان و عربستان قرارداد پیمان دفاعی مشترک دارند که بر اساس آن حمله به هر کدام ، حمله به دیگری تلقی می‌شود.
🔺
برخی اعتقاد دارند که یکی از انگیزه‌های اصلی تلاش پاکستان برای میانجی‌گری میان ج‌ا و آمریکا ، نگرانی از وقوع جنگی است که دامنه‌اش به عربستان برسد و پاکستان را ناچار به ورود به این جنگ کند.
اینک که تفاهم نامه کنار رفته، پاکستان بیش از پیش نگران این موضوع است.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6162" target="_blank">📅 19:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6161">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
استانداری هرمزگان:
در ساعت ۱۸:۱۰ امروز نقطاتی در قشم مورد اصابت موشک‌های آمریکایی قرار گرفت.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6161" target="_blank">📅 19:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6160">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0a471388f.mp4?token=jImyMp-059WAcGn1XBh77Z-ypxcO5RsOppGVegn-I1UznT3UYMBIlE4YfQml8P2acQD5FIv6-lpI6f0IYn6dXORZBQ-y3lte-vKFR5i3vkKErOiXF_gIWIkV4V1q52e7lmQsz1SjZMxA7AvfiqUMGnpRsHEFaagzcOxoIQZsXCFKhkxPP5qVlyf8f4s3VCiKZfk_QLuXKA7YwqHZD76ku7CyOxK8UNnPvwM04SxC2WM1aFDxPFMuglqkEbLvmmvbPE0b_aOY3QoW6Ok1L8OXg_FxoAgPRLv2BMmavgMWGaK6kUMKnghlkrAYRnslePkQD3YDI_NB7ZfNNM1udxdS-yvohy5h-dy9CkzKHz4ktU_BoqDSg4u2j5SF2zLDqyaF9iADv5Ru-u3ogIMASB3vEUlb-o_3nFo5io65TpkFos5_FxAPzWsTSMYlF95QiB8dWLYrnbqtkeOHpf32yJhrS98u11BM_0swDXnD6IPb8RGT7DvmIBv3VxjRDAf4dg2fNgLVNe7UukIVH2yCrRLLONv1aGzRnTUzPVK1Tu1nwm8RTot9YJIAh3t2cZUhQ3m6o-XaJGUJ_U4EfQuJcysMLtD-VTfDZDInoxZJHiFYjCAsSzkpSqZO5NActgUzl0tf4Plzt2oqcXgxyZzhGkYPFddIvd1rda7STyixCag7BdE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0a471388f.mp4?token=jImyMp-059WAcGn1XBh77Z-ypxcO5RsOppGVegn-I1UznT3UYMBIlE4YfQml8P2acQD5FIv6-lpI6f0IYn6dXORZBQ-y3lte-vKFR5i3vkKErOiXF_gIWIkV4V1q52e7lmQsz1SjZMxA7AvfiqUMGnpRsHEFaagzcOxoIQZsXCFKhkxPP5qVlyf8f4s3VCiKZfk_QLuXKA7YwqHZD76ku7CyOxK8UNnPvwM04SxC2WM1aFDxPFMuglqkEbLvmmvbPE0b_aOY3QoW6Ok1L8OXg_FxoAgPRLv2BMmavgMWGaK6kUMKnghlkrAYRnslePkQD3YDI_NB7ZfNNM1udxdS-yvohy5h-dy9CkzKHz4ktU_BoqDSg4u2j5SF2zLDqyaF9iADv5Ru-u3ogIMASB3vEUlb-o_3nFo5io65TpkFos5_FxAPzWsTSMYlF95QiB8dWLYrnbqtkeOHpf32yJhrS98u11BM_0swDXnD6IPb8RGT7DvmIBv3VxjRDAf4dg2fNgLVNe7UukIVH2yCrRLLONv1aGzRnTUzPVK1Tu1nwm8RTot9YJIAh3t2cZUhQ3m6o-XaJGUJ_U4EfQuJcysMLtD-VTfDZDInoxZJHiFYjCAsSzkpSqZO5NActgUzl0tf4Plzt2oqcXgxyZzhGkYPFddIvd1rda7STyixCag7BdE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنرنمایی جدید جمهوری اسلامی</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6160" target="_blank">📅 19:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6159">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfb27a8797.mp4?token=FhFZ0mzwamajY6Xp4VekYeKZmqSFm6ijQNVr8a-INJfmKTvA047cSTmhkBa7MtHqINrTrp-zR129ZKT5jRT4W4GqR19sWlmGb0V0ikQ6p5IR8qE0pQ9z-08Fgjm9RL2eT9ohDqrYOyXmZn_g5wbQCQInPX3QjFWbh_rnM1ZK-s5GAznJMMq6uZ3xx9cJoderyGH-3WYZY1nh0D66Gj8RYSoFA9YzJRspE4KZ3OP9xKWiT6iO4UtAhiUeHDTwxsJAZrx7HqUmuuwBvPA0E95wxkVcofsV7zvT0G4eNN7AycfdbNmpkUuyNwJ2Wj4HSDbgsmBfE8JfC0cTUUEZ1lvlaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfb27a8797.mp4?token=FhFZ0mzwamajY6Xp4VekYeKZmqSFm6ijQNVr8a-INJfmKTvA047cSTmhkBa7MtHqINrTrp-zR129ZKT5jRT4W4GqR19sWlmGb0V0ikQ6p5IR8qE0pQ9z-08Fgjm9RL2eT9ohDqrYOyXmZn_g5wbQCQInPX3QjFWbh_rnM1ZK-s5GAznJMMq6uZ3xx9cJoderyGH-3WYZY1nh0D66Gj8RYSoFA9YzJRspE4KZ3OP9xKWiT6iO4UtAhiUeHDTwxsJAZrx7HqUmuuwBvPA0E95wxkVcofsV7zvT0G4eNN7AycfdbNmpkUuyNwJ2Wj4HSDbgsmBfE8JfC0cTUUEZ1lvlaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر قالیباف، تیر ۱۴۰۳:
ما غنی‌سازی را ۲۰ درصد کردیم جنگ شد؟ ۶۰ درصد کردیم جنگ شد؟
hafezeh_tarikhi</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6159" target="_blank">📅 18:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6158">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ایران که ۴۷ ساله که در آتش فتنه اینها می‌سوزه</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6158" target="_blank">📅 17:27 · 25 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/8ca0d3dd94.mp4?token=QtYDECmfHzuoawbgLSBNUZfH9wN9RuQcmWhe44wM3NOQVz6qVuIB2o9D-GnMjW4gxFv7eqQUdMbeNUUqAm2yZexDqOC3D3kqNxNtiYWBUSoOnct9Jy81r3EEG1kh4TkjH2UVffCY4CxoMU3GoXE7xcjI-ZtS-E3aU0amAhlIH-WywFhPy0UkPILpT6RaVaBAsYD4h_-zd0o-6G_4li9Tt4o8g-VeDG1cQEjoLhRLFdCYoyTVNZb30DOIiyYkKQ79ua2lKu9zjFTvzBqw38dGkJN99ulJrwnXl5Qc2LiA-zDgLDf131WDhkWip5ZHt-oIMDGJi-YbpRMGoKeOTYxnRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ca0d3dd94.mp4?token=QtYDECmfHzuoawbgLSBNUZfH9wN9RuQcmWhe44wM3NOQVz6qVuIB2o9D-GnMjW4gxFv7eqQUdMbeNUUqAm2yZexDqOC3D3kqNxNtiYWBUSoOnct9Jy81r3EEG1kh4TkjH2UVffCY4CxoMU3GoXE7xcjI-ZtS-E3aU0amAhlIH-WywFhPy0UkPILpT6RaVaBAsYD4h_-zd0o-6G_4li9Tt4o8g-VeDG1cQEjoLhRLFdCYoyTVNZb30DOIiyYkKQ79ua2lKu9zjFTvzBqw38dGkJN99ulJrwnXl5Qc2LiA-zDgLDf131WDhkWip5ZHt-oIMDGJi-YbpRMGoKeOTYxnRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FCkeGdBXUg9NcooKDZCPYUpYEY8IRUZI7DYxI7PpTm4v5m5B7FEhhRKps7IIKnNJiqhAJ-oI52hOHwflfbPU7NI-XaSyDIjkD-ya8vv8rHBaWPz0bFMegzF3iYxIkZ_SPAgsxFAjoD0dn5-ljRzQPdI8EYGwqzYF94kvt3JJM7r0f646x863BGW0mgzUwBR2qNSAxAqJDfDxjofmILACfGIQMRkh3t2NR-F4CY502_0n6TfNNlSLvAR-98l2vTAzCMI0R9TStjfwtJFUwMptXw-fQ9WNlk5qrmjGiaD3mq9p0Qy9s_vyxgKir33oAASu1A9HXrwgPyh-z1i6wtZ5Xw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6154" target="_blank">📅 11:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6152">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1933ad174.mp4?token=imLsp2XAyub1VGwiPQS-Iwv6Dya8ADy6GUvJiMnzb2csors1dUJ3IDStexiE29GAUDEMFve1V6Z7v03mODXBY1F81T42gbw2kAYM3kmle4JjKflR1tDnMptdJN4_pYwRPXArKR2EBMxSUXUnIz8NZUvQk8Dl5Z5IXSd--Cmr3tKuC11xORqLQsLVYSUyBa9ukf9osUletPWLne9FSggl0y2ztautWJHKaDlSQknveeZMF9gL6Pwes9QubjJ3Oa9_LsYkziW0PJi5cX4fY-CyfPs-p8DjQrRda2Sz43xyCksRqhjgPfN82mD-bN-BJQlbD5-0S4VHDZIEeTRyi5zi7LOhKfCNPB3YvgKXVukqpO_5smZPRhCr_HDtAsQSruRsHRO0vllx0f7-H7w8bbj_A4Y79kx9KNlSwM6O-XLOHTEypItCr2Uw4BJBwJtEqfF499B5iuMqmanR7Eze7QcmCq6Xllqw29-RfjehxO4mpjBR5eLSBEMWARCIc2e-a6M55Mhx3hlhwR7OahlwHWOvCCVKCPxLGj5Ncr28M9Ggv_jPnlflo8On-grRmo8jkd3fEx6azw6RBtqMMrV4593ugc7Qh5ABObloI_lF8khC9ys_c2uax55KDmT92gAGhCOtvHSPaX8qB_ETQjk8CxgxUZ0Rl6Smzd34soqPfJdr59k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1933ad174.mp4?token=imLsp2XAyub1VGwiPQS-Iwv6Dya8ADy6GUvJiMnzb2csors1dUJ3IDStexiE29GAUDEMFve1V6Z7v03mODXBY1F81T42gbw2kAYM3kmle4JjKflR1tDnMptdJN4_pYwRPXArKR2EBMxSUXUnIz8NZUvQk8Dl5Z5IXSd--Cmr3tKuC11xORqLQsLVYSUyBa9ukf9osUletPWLne9FSggl0y2ztautWJHKaDlSQknveeZMF9gL6Pwes9QubjJ3Oa9_LsYkziW0PJi5cX4fY-CyfPs-p8DjQrRda2Sz43xyCksRqhjgPfN82mD-bN-BJQlbD5-0S4VHDZIEeTRyi5zi7LOhKfCNPB3YvgKXVukqpO_5smZPRhCr_HDtAsQSruRsHRO0vllx0f7-H7w8bbj_A4Y79kx9KNlSwM6O-XLOHTEypItCr2Uw4BJBwJtEqfF499B5iuMqmanR7Eze7QcmCq6Xllqw29-RfjehxO4mpjBR5eLSBEMWARCIc2e-a6M55Mhx3hlhwR7OahlwHWOvCCVKCPxLGj5Ncr28M9Ggv_jPnlflo8On-grRmo8jkd3fEx6azw6RBtqMMrV4593ugc7Qh5ABObloI_lF8khC9ys_c2uax55KDmT92gAGhCOtvHSPaX8qB_ETQjk8CxgxUZ0Rl6Smzd34soqPfJdr59k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینها اگر نوحه میخونن و مداحی و رجز خوانی و.. برای کودکان غزه و لبنان و میناب و….. از تاسف از دست رفتن زندگی نیست! میخوان در این جنگ بی‌‌‌‌پایانی که با جهان دارند،  از جمله و در صدر این‌جنگها،  با خود مردم ایران جنگ دارند، سربازگیری کنند! تا نیروهاشون بزرگ‌تر…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6152" target="_blank">📅 11:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6151">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">تمدن اسلامی! تا زمانی که توی مدینه و مگه بود قادر به ساخت «توالت» هم نبود!  مستراح هم نداشتن !! اما دنیا در چه وضعی بود؟  ۶۰۰ سال قبل از تولد اسلام!  توی بیشتر شهرهای جهان  داشتن توالت عمومی! اجباری بود!   اینها میشینن روی منبر  میگن «مدینه فاضله»!!  حالا…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6151" target="_blank">📅 10:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6150">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">تمدن مصر باستان رو مطالعه کنید ابتدا تا انتهاش بر مدار مرگ بود! فرعون از زمانی که سر کار می‌ا‌ومد به فکر مقدمات مرگش بود و قبرش بود!  هنر و پزشکی و علم و مهندسی مصر همه بر پایه صنعت مرگ بود!  مومیایی و اهرام و جراحی پزشکی و….. همه برای کار و کسب مرگ بود و…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6150" target="_blank">📅 10:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6149">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wq-cCLAmZ-diPpR_8rEkkklqMtMaYQ-oJK3B8RtXkF1rSg8lVq7GEz828mFAnawgONhSN8KhSf20PQDQWOyeQNjLUId2GsJuesvaADypXAl3I962DKd71F7sx0V4ryrm7kyTIM2ai1EJCSiOhMCckPUtJKu6QLkdiWL1afl1Se5FRzhCVQru6Eg35tVhqb0zKGlBeAQe8sl1ydzkxt0HnclCvcHKNF6P71_lO4dUMDiyX86sl0f2Bgjs9Xi7QJD2qt0yKrKCsjLKTtgfsAgEauAsI8YQLaPhZJfCZRr8VgCakX8uJEQw_eINYU7XvV2dxIlCjf1vW2_CBKk9AiXTFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها شنیدید جملاتی با این مفهوم رو که زندگی و این حیات «زندان مومنه»!  آرزوی اینها مرگه! مرگ براشون رهایی است!  اینکه برن و برسن به بهشت و به زندگی!!  مرگ رو آرمان خودشون می‌دونن و زندگی و زیبایی‌هاش  رو پست و حقیر معرفی میکنن!  و اینکه باید دائم به فکر مرگ…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6149" target="_blank">📅 10:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6148">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">اینها اگه می‌بینید برای مدرسه میناب و…..  سر و صدا میکنن، فکر نکنید به این خاطره که «اصل زندگی»  رو دوست دارند. و از مرگ متاثر میشن!  تمام هستی اینها :  مبارزه، جنگ، کشتن،  کشته شدن و….. است!  زندگی براشون چیزی نیست جز  «مبارزه  برای عقیده».  و خوشحال میشن…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6148" target="_blank">📅 10:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6147">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b6d93f0a9.mp4?token=KbQTnnfvjsJA0Y6eT-1axNse064RzBRDL2dmTVtARk4UM19W_E1kWCj2Jx56rkp1FvS-kEjvtfrEu1g4dyqeXc0ATZoJsnGMJWbhFGtNybrrk204qv9w2TaM2j5N47j_fcN3Dq-9ny103EJoCzYBkPXFbbPJtnNHRxkhX8Czv5ZiaFy0ktZWQRNX7SYs6y2oIjJb1z0ncnknJSWwun2iqaP8H2UbQkbrZopApZsbtZWRagM8x7WEkLNfTBuGjhV6dGzK1rRfNJypWdM4sY54U1XTsr2A39wLOlGhHDIcRGr0DXapXx6KGJwUlMeCVynJrYU2ebNLtsbUYAWFuIGKtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b6d93f0a9.mp4?token=KbQTnnfvjsJA0Y6eT-1axNse064RzBRDL2dmTVtARk4UM19W_E1kWCj2Jx56rkp1FvS-kEjvtfrEu1g4dyqeXc0ATZoJsnGMJWbhFGtNybrrk204qv9w2TaM2j5N47j_fcN3Dq-9ny103EJoCzYBkPXFbbPJtnNHRxkhX8Czv5ZiaFy0ktZWQRNX7SYs6y2oIjJb1z0ncnknJSWwun2iqaP8H2UbQkbrZopApZsbtZWRagM8x7WEkLNfTBuGjhV6dGzK1rRfNJypWdM4sY54U1XTsr2A39wLOlGhHDIcRGr0DXapXx6KGJwUlMeCVynJrYU2ebNLtsbUYAWFuIGKtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pyldZv2l67DdbZrWE-PilAst0TFZKqgDo5HqKqejuqReiLHSgaOAf0B0zfU9cm-IvmiOnAK-nv3quQhjqXsF0DV7iDXih5WrDQOlPwdgZ8VLChagErHxye3xR6IXjDNNT32JGxzhcq_it7ln1L4l_0yEC9ZA6-DBq-_iCkUX7o7Y1KQpV4qeVSidpHPzyCX3AkHBbRk4Q8BL2IUhoN8KZFUEloyoO0WOQk0zaHuZxctgerdVrFYqb3w79UofcnnuRjPWlCEKRsPGsDOZ4VwN_x4oKIFT_1kaKbfDVlhzWF6WaFP_b-8-B7zZu7frhYVdBHj_kaobWai1CiYZrjLIOg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6142" target="_blank">📅 08:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6141">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aa1hsaYe4G4eyvtQ4c3gB3uP7tK1K4qibvYzhqtUC77xJdngT_pi2HY4qZ0AbVPgGYubYTcZtWrtQC3UO0I93OBVZC6_uXJ6hwDm16J-Bc1LniuELhBIZ_gDHGVc9_uPz4c3kY-TuZykj4KalQBG0F0Yl37OJuUnSfjqOpMR0vXkD8rGpEA5WQg9Eifq6TkFZuhzqxiPUq5lWdlyHmXE08GuOt2NzN6RZT9ovDo3Y4vP758yUb8s-0AlLVC1NsOH9nrF5TTb7dYLl00VXUP38eLeWZR3j7jdWXXzPHrWnIGxRpAXg56YxI2tG0cYhL2DYI0wLjXeWAgcCehCANRKAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین یارو خودش از دست سپاه و نهادهای زیر نظر خامنه‌ای  فرار کرده و به آمریکا پناه برده!
و آمریکا رو خونه امنی پیدا کرد برای زندگی و نوشتن از اینکه اسلام چقدر زیباست و خوبه و سعادت انسان رو میخواد!
حالا از همونجا به ج‌ا میگه مبارزه کن با آمریکا! مطلقا تسلیم نشید! تا انتهاش برید!</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6141" target="_blank">📅 08:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6140">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">برخی گزارش‌ها از تداوم حملات به اهواز خبر می‌دهند و اینکه تاکنون ‌۹  انفجار  مهیب در شهر شنیده شده.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6140" target="_blank">📅 23:02 · 24 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jlKrrKZl0ZdLOg4GN7UKUPnsApHhgB6zJV4y9I-2l33PuUccvko7qXpgGoDIWnRSkVWgQ5dptFT94gkz1crBqdecEgg-bO2SGliZDPdV-9FQ_IwY3iL8XPIzwFlMKZJjM1YnmCPONXVuk_gzVZ5s70eR1jVktVHMeDu0lzWBdv0PPtddLQHsAb8aPZISYNbFfYUqOLeyDjpv0WFCuudy3uWoYg-O-f2y_4Wj3FAbD-qQRYkqC-2WmgfST7H4K4af-_kfN3xJOkhdxGKHkauMzjZU1HJIIUR-PAVwlwV0erCYhFen_t6YsXZ1ZLGgo9LwL7eRkMwuTMR1CBk4Hp-pew.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/20e615d142.mp4?token=UeUbbED_RNWYqlu_iiIKsHfpdoVKzHMMRBJe-VahzKWpyGOSySs_gJEz1R20eTkMPlFq900oBOJxnFMRiffMx7rNakuYrgGtPaeuQzL4feBaW5eHBfN2mtWwf5wMuopsIrP-kaSN_NOqMhb-dbLNspqzTI-XdbPGZAX30fooXm_FVrBUs9iG-XUQEWMlovg9e7zC9Njc6Lt7YzizU4ibiGgbs4Dqio3TqgVNUjAASVEP7EjGnlh-ysFptVmxACHLa2QNQTtFUETQ07XgrqQOiIRofsSzoIu5wJ8mHRMDiCyN8MPnsjR6t40WQopHp7vR5RP-SNJOKX8kVejcsbqbKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20e615d142.mp4?token=UeUbbED_RNWYqlu_iiIKsHfpdoVKzHMMRBJe-VahzKWpyGOSySs_gJEz1R20eTkMPlFq900oBOJxnFMRiffMx7rNakuYrgGtPaeuQzL4feBaW5eHBfN2mtWwf5wMuopsIrP-kaSN_NOqMhb-dbLNspqzTI-XdbPGZAX30fooXm_FVrBUs9iG-XUQEWMlovg9e7zC9Njc6Lt7YzizU4ibiGgbs4Dqio3TqgVNUjAASVEP7EjGnlh-ysFptVmxACHLa2QNQTtFUETQ07XgrqQOiIRofsSzoIu5wJ8mHRMDiCyN8MPnsjR6t40WQopHp7vR5RP-SNJOKX8kVejcsbqbKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیش بینی تاریخی بختیار
در دو کلمه، برای مردم ایران</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6135" target="_blank">📅 20:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6134">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/296fa239b5.mp4?token=c78Jg2k-U1U_V_RDQp7vN3coQUO11cqaiirrMxvUu1w7qyeHHYazfr7MTa92q3vUeS68amOwK5GsMfpxH4z6lVC6mB6uzGofqBiR7WUGlAJN1TLEMSm0deI_U-5OfrzK4fqHbcFZmhOn-qZTski7YVElmvLSTADKWixHVwEhyqpK54E8WCVcULSFhTrPlpsCwYlMrgEqXbtSPvXe_GdNAUY6gAPdWxYcmrPu16YF8r9Fceft-hntAh86Cd6fD9twcZ0jXwYRuEJQUC7JdWlGiL2Q9DA2p9QNrgyk3SXW4QrQl3hS2qzxxKA653WcAQtEatUJDJ0NVVvLpukjDv8UpIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/296fa239b5.mp4?token=c78Jg2k-U1U_V_RDQp7vN3coQUO11cqaiirrMxvUu1w7qyeHHYazfr7MTa92q3vUeS68amOwK5GsMfpxH4z6lVC6mB6uzGofqBiR7WUGlAJN1TLEMSm0deI_U-5OfrzK4fqHbcFZmhOn-qZTski7YVElmvLSTADKWixHVwEhyqpK54E8WCVcULSFhTrPlpsCwYlMrgEqXbtSPvXe_GdNAUY6gAPdWxYcmrPu16YF8r9Fceft-hntAh86Cd6fD9twcZ0jXwYRuEJQUC7JdWlGiL2Q9DA2p9QNrgyk3SXW4QrQl3hS2qzxxKA653WcAQtEatUJDJ0NVVvLpukjDv8UpIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kdlhnGtFLGJoDbRzCxmGRigR9fENTh7B3c6zDCKfCYQ5KPYL4P5gHLQVWwyh6ZC1kXIUc5Rf5hOerxve9OB9A2KMlfat13YdF-ctvy1cuCSDEf0nIGXzZkG0pe79xf_2MGg2nIeQ2IvjvDO9tAe_RwfIUorLvmeoOr-4YMNRx63yrko6mkBxWlzjZQn-oImgPbYdeRzkXgY-gCW_MOWhwUZCZPKeVJROmBJ2CDQsJQPo-bV2OduXQQH0b-uZbZlLyr7oZ2tJHIaZaQyY1tN3r1sp4ur9oYqRlgQHFKPvVlWAHI7aZjMiBYJ36XRtQlIin7qdBNQNe1duNX0jUgDZnw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IgYrP5uIIbCQ71bYYVIbfYh_fCXqT_cKpNs9DHnMR7DVshAvh-sOKFDrrpveF6Yp2iS-7NdNjilG9nkf3DhMg0czlpjramyUsEwj-cdZYbsbc2zmt4lYU8uBqyE9t6_ijDtXZo5E4_xIjbTKChEw5-9r_lD0iw_xt60nQKUDuCO-9WgSpD9QPxPd80V1PNmY9SJogHorFBskqgfH1bxduDXDwfEzpuqWLHbx2hrFEDonYQ4aKDiGihBBqg1aXQzzGpqME-5VGG6-ywc0VkfrGmNNYyPjRZG-_TbulvSzj-eR4DU4lSLJuduQeJGzS25OPIhZwsQ0IMnB2UXvxDD34g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قابل توجه ساختاری‌های محترم
مدیر حوزه‌های علمیه با بیان اینکه مسئولان باید تفاهم‌نامه‌ها را پایان‌یافته تلقی کنند، از دولت و شورای عالی امنیت ملی خواست به دلیل بدعهدی طرف مقابل، مسیر مذاکرات را متوقف کنند.
مشکلات اقتصادی یا ترس از آسیب به زیرساخت‌ها نباید موجب واهمه مسئولان و رویگردانی از مسیر «جهاد و استقامت» شود.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6128" target="_blank">📅 13:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6127">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd0a98053a.mp4?token=GJ_psZPGq3CGTtVxUjSdWMQxWQbBpDZ0bQOlGrsiAA_AOJsDbex7kN1QbpHEVk-i0DwLaykBqLIQ_H6hAOC8Jnz4CXryPUvX7qoxvTWk9VISfmAHbFKPjcqJuuHzSDfGIMCJktVENL-Iz1gfN874fwO7wtp69X1DmbEB5F7kUl7BZci2ywmZcGy1tl8Lg_AdvAkPxRhtmv6Si0UbcC7AO-3ANXxQhuitWMzjxJzUjaB6ND3uA39ZNmdKq8e9jNqMiQRapJJV2VTvn8a2QmW0J4ACioUFRqw6vD6Xmo7vMmBeFuor0WauCIfAFpFMXg_t7TIPZcasG9JwCYUQgdRZXyAsoX-6lAp9IrY8PaeZNnZA5AGYslzw_ix2whzezvT1kiu57FYanVnNeO9FD-PESGLnbnbxcsdZ_8QlI6eJPHB9EY4TxtFNU8lD6f-IT9aTiVSDBlF2QsSWQXXhISCCGeZdsGZiM8M_-DTcfmD5F_dAjV0BhcBvfPBCuGtwYob0nokUcWUsdcaypQQ4EOyhDoQjNj0N5kpNo-y9GQAwZu8Y2-IwPKSrBKz3AFsZTzFFDV8on4V1NbEOlrhFS736Q-xnJQHvRo5D3-H4c1dA2uerOhIr-MwHbLyMkJZkhBSm9SF4EaB-iFFtdI2Uu_DOChS0TDKiqPtaVRiLxjvd11I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd0a98053a.mp4?token=GJ_psZPGq3CGTtVxUjSdWMQxWQbBpDZ0bQOlGrsiAA_AOJsDbex7kN1QbpHEVk-i0DwLaykBqLIQ_H6hAOC8Jnz4CXryPUvX7qoxvTWk9VISfmAHbFKPjcqJuuHzSDfGIMCJktVENL-Iz1gfN874fwO7wtp69X1DmbEB5F7kUl7BZci2ywmZcGy1tl8Lg_AdvAkPxRhtmv6Si0UbcC7AO-3ANXxQhuitWMzjxJzUjaB6ND3uA39ZNmdKq8e9jNqMiQRapJJV2VTvn8a2QmW0J4ACioUFRqw6vD6Xmo7vMmBeFuor0WauCIfAFpFMXg_t7TIPZcasG9JwCYUQgdRZXyAsoX-6lAp9IrY8PaeZNnZA5AGYslzw_ix2whzezvT1kiu57FYanVnNeO9FD-PESGLnbnbxcsdZ_8QlI6eJPHB9EY4TxtFNU8lD6f-IT9aTiVSDBlF2QsSWQXXhISCCGeZdsGZiM8M_-DTcfmD5F_dAjV0BhcBvfPBCuGtwYob0nokUcWUsdcaypQQ4EOyhDoQjNj0N5kpNo-y9GQAwZu8Y2-IwPKSrBKz3AFsZTzFFDV8on4V1NbEOlrhFS736Q-xnJQHvRo5D3-H4c1dA2uerOhIr-MwHbLyMkJZkhBSm9SF4EaB-iFFtdI2Uu_DOChS0TDKiqPtaVRiLxjvd11I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/brTm9VmHuyt9FTh3bP1-t4CXJUjeK__syQVX-JkaFFHfSOhpR7GYBuy2ruKrwXQGVnp6p9dXMAV3nNYK0bDOnMlP5eVBzXvaJ9Te_iJcpMy7x96ibhmgf-wd_KlPMSq33gKtzkYuFhhLZeLkKmze-XbzcxfxRiAek39EzzTjmTfYVTtPvxMD-ynD3St08MRFt6ptIaTxDWNwRr9WuakzGtlR9PqOZn9k-OrDsGwQJIBiUihWCh8JV158T8G0GVdyi_2BWoZRQqvyh3rBmVaWz9BFqU9iz9Bxh7eQowbuDMqYobkee2vG18u5oyClF2Qcdvzmt3tkWp6FFFTDVG9HqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلسه اتاق وضعیت برای بررسی حملات گسترده‌تر آمریکا علیه ایران؛ آیا ترامپ آماده تشدید جنگ است؟
به گزارش اکسیوس، دونالد ترامپ، رئیس‌جمهوری آمریکا روز سه‌شنبه برای گفتگو درباره عملیات تهاجمی گسترده علیه ایران جلسه‌ای را با حضور مشاوران ارشد خود در اتاق وضعیت کاخ سفید برگزار کرد.
به گفته سه منبع آگاه، در ابن جلسه که ارشد‌ترین مقامات نظامی و امنیتی آمریکا در آن حضور داشتند در خصوص گسترش حملات صحبت شد.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6125" target="_blank">📅 08:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6124">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bd4825a45.mp4?token=ftzrVPCGUjms8upJYiWhbV53NCWlmh2E6IG6fZ_NW_OHHTjKLiKddKaFZS99j6g-r_GeKAOdaFpUjuNia7HtL-_vsGMTnC4_4RaFub23HtHQdJP_nbsR6JLDoJPdY8zQOZGfPjBflU3MR87JAZQm_z3Fn3ctAO2E5FGjNGkpnYvTYmApLoFQ1JK8BV9TT8lj_eBpMukV9vciPrvbI-3ukFeDj2_KtzErZaI6mqchhW0qTtEB_-2ykwLKpGpe-w_nobY5GrhEerDGWtt3o-90mStvZXNdBy9ibX2QxfuFa5y4AxTqAK_1uynFRLBquSUUrNtfiQSxM1-rTGOhFV7AlRg1dDm2b9ySG78xYLU4UplfhytXaHcDp-WDWw5Z3HlGJJM3k5T8crBXiXa8WVPB5kzRCkp7Ho7lDz3UK7d7ipYYFXkPVgud-0Nn2cc_sIuTn5_4QFZjS4sGlA_TooOQyRz2123MBKOrDPCujgEtNIowaXON4WJzcEKgVQMTXzSujKZI5J9Dmhfatrvx0MUGwWUDd55cNqNOojsIi2cIkwaKSQXrrcFuiO8JZp99JPaEaM-WasXcMvZ1jPYmzX5_xoujtnLVC9ulCEPEJ6e6GEjCkYLG5NRJA1wVmEtiMxFC_eKqTZnuyvQQXZdDZXv92Hg8wfMDJUkOi-C5cGgliig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bd4825a45.mp4?token=ftzrVPCGUjms8upJYiWhbV53NCWlmh2E6IG6fZ_NW_OHHTjKLiKddKaFZS99j6g-r_GeKAOdaFpUjuNia7HtL-_vsGMTnC4_4RaFub23HtHQdJP_nbsR6JLDoJPdY8zQOZGfPjBflU3MR87JAZQm_z3Fn3ctAO2E5FGjNGkpnYvTYmApLoFQ1JK8BV9TT8lj_eBpMukV9vciPrvbI-3ukFeDj2_KtzErZaI6mqchhW0qTtEB_-2ykwLKpGpe-w_nobY5GrhEerDGWtt3o-90mStvZXNdBy9ibX2QxfuFa5y4AxTqAK_1uynFRLBquSUUrNtfiQSxM1-rTGOhFV7AlRg1dDm2b9ySG78xYLU4UplfhytXaHcDp-WDWw5Z3HlGJJM3k5T8crBXiXa8WVPB5kzRCkp7Ho7lDz3UK7d7ipYYFXkPVgud-0Nn2cc_sIuTn5_4QFZjS4sGlA_TooOQyRz2123MBKOrDPCujgEtNIowaXON4WJzcEKgVQMTXzSujKZI5J9Dmhfatrvx0MUGwWUDd55cNqNOojsIi2cIkwaKSQXrrcFuiO8JZp99JPaEaM-WasXcMvZ1jPYmzX5_xoujtnLVC9ulCEPEJ6e6GEjCkYLG5NRJA1wVmEtiMxFC_eKqTZnuyvQQXZdDZXv92Hg8wfMDJUkOi-C5cGgliig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0378588a4a.mp4?token=GZa2r35F3h1GbQZPxSSPRIDV-rnLVZrkR9bDXnCwMHyJkX5Hz72qWc2UkUvPnkM_GjQwORE0bNCLE9x4JpJrDPnsafjtHSE21KOJaZlifFubOA3UCGHtho9S8ACMfEDHt3SSks0LO8pTN13DgQRDHQ3pJdHm2q_fDi643_RJIhtq-wAO5SQTfLx67-GbzELAJj-tW8QnX5A9jloB6CJdtg6JA5z1pAPys7LhoIxDOMU--mw9y9XJCGbEQwpw4y8hN-LZveerWCuVxJEio5fhlvLDNetx3UAOhVGeg0sQroiEb_atuIuf2FK-VIcVU5bRQLbxzIakNoM0b9IX758wjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0378588a4a.mp4?token=GZa2r35F3h1GbQZPxSSPRIDV-rnLVZrkR9bDXnCwMHyJkX5Hz72qWc2UkUvPnkM_GjQwORE0bNCLE9x4JpJrDPnsafjtHSE21KOJaZlifFubOA3UCGHtho9S8ACMfEDHt3SSks0LO8pTN13DgQRDHQ3pJdHm2q_fDi643_RJIhtq-wAO5SQTfLx67-GbzELAJj-tW8QnX5A9jloB6CJdtg6JA5z1pAPys7LhoIxDOMU--mw9y9XJCGbEQwpw4y8hN-LZveerWCuVxJEio5fhlvLDNetx3UAOhVGeg0sQroiEb_atuIuf2FK-VIcVU5bRQLbxzIakNoM0b9IX758wjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه محلی «حال وش» از حمله به آسایشگاه سربازان در شهر «بمپور » در استان سیستان و بلوچستان خبر می‌دهد و کشته شدن ۱۰ سرباز و زخمی شدن ۱۵ سرباز</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6123" target="_blank">📅 07:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6122">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5b6a441ee.mp4?token=HKnWPeG0NMWA6-cSbtifeNO9jEY8LZB5Sf-W7C_se4YJQ-GaDS0RgVdC2cqdL0Ju2noinusAhpYsjFAAVfwnon-NpkZvrDtDwAhYS2LPePcvutxCQkPWaqcIUaJ2qd6oF6MsHaftEGC1n0WxVVVARvGn-jtK_zOvbAdivELvAkpbFLoHpRz2_ygdBS9bejKv1Mkpg1SJ6Ql49bA9HgEBusA4Lff_3AoJ6OBbTGcVn48A1FXb5xTC7fTV5BT2vvHekvnQSn_lfiXFbjORmbBFwcOXdcyCWijuJAvopO3UFxVQ2pTL6nw_dPl4WfkfTBuoS67HJPc7CF1baxLUBZ-xDwB0nEvB-BgZmiOlLmSFDtJHbhbw7RrlTpk-rjRsXUuOwFjvkbmxcuFn-Rm8XaePAIHy-0oqqMC1gHLtmffpzjl-XLGe2gVEJ7rDcDajttjo8KRwf4NVmIkgNDHuq8vJ-xzKdr9LCAbQWRqHKGit5bHtNcb0IS7dVnHSmGXhVWF-_J5mDItVWuCU6brMUIyQwmEY5V3g27Dfzl5jgx9qh6kG1L4YOL3L--BgjzuxRLqlqX6h6173XM-y7aCWUz6VYwMeTIktuZWS2VuTNshM_xHK4nRdl4vtum-SqTFPRx4Zd_KlO3KWUpurwjEPFwTD9mcEg1eHG0YcyyuB30hfPm4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5b6a441ee.mp4?token=HKnWPeG0NMWA6-cSbtifeNO9jEY8LZB5Sf-W7C_se4YJQ-GaDS0RgVdC2cqdL0Ju2noinusAhpYsjFAAVfwnon-NpkZvrDtDwAhYS2LPePcvutxCQkPWaqcIUaJ2qd6oF6MsHaftEGC1n0WxVVVARvGn-jtK_zOvbAdivELvAkpbFLoHpRz2_ygdBS9bejKv1Mkpg1SJ6Ql49bA9HgEBusA4Lff_3AoJ6OBbTGcVn48A1FXb5xTC7fTV5BT2vvHekvnQSn_lfiXFbjORmbBFwcOXdcyCWijuJAvopO3UFxVQ2pTL6nw_dPl4WfkfTBuoS67HJPc7CF1baxLUBZ-xDwB0nEvB-BgZmiOlLmSFDtJHbhbw7RrlTpk-rjRsXUuOwFjvkbmxcuFn-Rm8XaePAIHy-0oqqMC1gHLtmffpzjl-XLGe2gVEJ7rDcDajttjo8KRwf4NVmIkgNDHuq8vJ-xzKdr9LCAbQWRqHKGit5bHtNcb0IS7dVnHSmGXhVWF-_J5mDItVWuCU6brMUIyQwmEY5V3g27Dfzl5jgx9qh6kG1L4YOL3L--BgjzuxRLqlqX6h6173XM-y7aCWUz6VYwMeTIktuZWS2VuTNshM_xHK4nRdl4vtum-SqTFPRx4Zd_KlO3KWUpurwjEPFwTD9mcEg1eHG0YcyyuB30hfPm4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا میبینم راست میگه …</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6122" target="_blank">📅 07:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6121">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qleEIjCZz2BPbF87evdHtZyMvYw9fDXLj_YeuTOro3qDsoZEQ1mp741wljsk-AoVb8hyNL5bkLd4PVysb8e9hcO5wYlSHeRXEZVA7IJ9-o_HYEiNG1B5pDTn92O4AZt8eAR9pqZoxEqdAv1UO_3ShvH1vde4f-O5g0wkexGUYYbOnB7-ANpAz4KYBpad_n0AWQtptRF1TjwvEkGs8U-nL0Nf72DM9BBFvekC6uAZhPlRNjOd5U2w6fzYD0VY_NbaCT7UxR1B6w-scigEUcyFh-DQAV8_hCOoDVDdp76pHYCnAdAjgFYWZC8FO1KEbO4IN9ZMugghzVF0AfUX7jHTdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6121" target="_blank">📅 06:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6120">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R8-IrvT3zHAxNCbBePFEPP9o9KD074sPP6CEbnog7j_ouwYPK5n78B7WQhkULzWzbPya0FHe7Lh5MJC6b4mRsNZsGn2d78XhKke4-knFMWhckcnmaEMC_74nqzPTxVUv32oSRuIpoR-2Ruom8ZMyA6A-j8UoHkEaikSe0C8SPH3yJFO1KGwlUCokQLZSEaMC5C9qI3Uv9wR_gOz0WZi2lVBC1FPns5r-Rnwz_yEDByoWp38pXJEQ-WnbyL3ghq_1g92NXXiy33rD-xgxGFwMRz6-QAIyBuUp3JEvxIBfrhul-HZmDtOZco5hor6SoSQwxUh57sKyEz0_NgAwfDJY4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه محلی «حال وش» از حمله به آسایشگاه سربازان در شهر «بمپور » در استان سیستان و بلوچستان خبر می‌دهد و کشته شدن ۱۰ سرباز و زخمی شدن ۱۵ سرباز</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6120" target="_blank">📅 06:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6119">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba02e5e863.mp4?token=qFUxzXhCSaTdt6I9o5gsTBwr4G_qvUhQJyt24BjDjdnsGtLtAmQcVYuW_SYBRp709WghPti5jRjVnEVyzGSe5T6QnN9OG4F7lna1Zoggm0PQVBbkS8NIa026GdqACauJwuZWp2pxTthhA_m_NrOvaAc6ihCKz7QCdVM7GYjER0nEXW2AUfi7r56gFjGpK4t3TyMobSxbMYcqWfiQa6o7a5X_-gVpP_mKrYZp-OEEAxwDbZ-KyUV5By0kV8HyxhPGEjYjyYVY2ettsYmhoLiNCPJH2Is6fEbjQznfPwW-snkxxFmXlNSKgBcwUODwsPsaxFQ9mFMC6I8M2-6ZZ9bVUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba02e5e863.mp4?token=qFUxzXhCSaTdt6I9o5gsTBwr4G_qvUhQJyt24BjDjdnsGtLtAmQcVYuW_SYBRp709WghPti5jRjVnEVyzGSe5T6QnN9OG4F7lna1Zoggm0PQVBbkS8NIa026GdqACauJwuZWp2pxTthhA_m_NrOvaAc6ihCKz7QCdVM7GYjER0nEXW2AUfi7r56gFjGpK4t3TyMobSxbMYcqWfiQa6o7a5X_-gVpP_mKrYZp-OEEAxwDbZ-KyUV5By0kV8HyxhPGEjYjyYVY2ettsYmhoLiNCPJH2Is6fEbjQznfPwW-snkxxFmXlNSKgBcwUODwsPsaxFQ9mFMC6I8M2-6ZZ9bVUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام فیلمی از حملات خود به ایران منتشر کرد.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6119" target="_blank">📅 06:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6118">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b9746249d.mp4?token=QRWKYE9pjWkdyvf3fzDDNVBKItC5ehXvfhgL1h7An5DYTXNfycVyKajtCxU_8Z8KXi5HptO4V22nJJXP5kZICX3PlJOJqfYTySam-3x0SBDHGK_2xJbxa6zz8xO6j6mcGU119voSkbEbJOhhctOEhhd9ivtzWTQCPoipk1WcArjn4wJEjWZ_pWcmrmvCx7dObgZ6gSnhf04TzDNHkDaZJvKeIy9odnFbsiUUxnbL4-HV3UyffeZBpMZpu6fiXdqo1Lgitvqs-_RGpCZeQ5DelGsfMHYpQVJHwGNBXobzYDg4QZDJXAAO8d4OOLvXSzY6Wq6l5hzxrmhM-ZdbN_yg8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b9746249d.mp4?token=QRWKYE9pjWkdyvf3fzDDNVBKItC5ehXvfhgL1h7An5DYTXNfycVyKajtCxU_8Z8KXi5HptO4V22nJJXP5kZICX3PlJOJqfYTySam-3x0SBDHGK_2xJbxa6zz8xO6j6mcGU119voSkbEbJOhhctOEhhd9ivtzWTQCPoipk1WcArjn4wJEjWZ_pWcmrmvCx7dObgZ6gSnhf04TzDNHkDaZJvKeIy9odnFbsiUUxnbL4-HV3UyffeZBpMZpu6fiXdqo1Lgitvqs-_RGpCZeQ5DelGsfMHYpQVJHwGNBXobzYDg4QZDJXAAO8d4OOLvXSzY6Wq6l5hzxrmhM-ZdbN_yg8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : امشب، فردا و فرداشب به سختی به آنها ضربه خواهیم زد و هفته آینده پل‌ها و نیروگاه‌ها را هدف قرار خواهیم داد، مگر آنکه  مذاکره کنند.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6118" target="_blank">📅 06:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6117">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caeb092620.mp4?token=SpDuig3KdYsNtCfLyQzvdgwzwhh2a8EqW5_4BZ5yJDuejEE7mFEcLwjtlZYU9kXNwa70Dk2I3o1Gbaowbl8WjpZBJke7ZH8gfV32afN2pUotERHDtZV6X9OtqoUCvUzRiyB_SZMPHCtYcDiBc8jJhrSP_7vIwgmqjneBQrDLVqSC1bzuKrFIUVBrpGkkDsqYOi3kJd9_AbCdmjnru7BHWwi5P-k7U4A6zG0JyoSVvFW7NE0-Oe06epyglaG6-hz1Wkqp9UWaq67_pbYFf4ci9K0qFpeE428oE2x3gbpCUtSfL-uWsb2BVeFeqKqlPDAAIevBfudxmi9GTOVYZWGdvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caeb092620.mp4?token=SpDuig3KdYsNtCfLyQzvdgwzwhh2a8EqW5_4BZ5yJDuejEE7mFEcLwjtlZYU9kXNwa70Dk2I3o1Gbaowbl8WjpZBJke7ZH8gfV32afN2pUotERHDtZV6X9OtqoUCvUzRiyB_SZMPHCtYcDiBc8jJhrSP_7vIwgmqjneBQrDLVqSC1bzuKrFIUVBrpGkkDsqYOi3kJd9_AbCdmjnru7BHWwi5P-k7U4A6zG0JyoSVvFW7NE0-Oe06epyglaG6-hz1Wkqp9UWaq67_pbYFf4ci9K0qFpeE428oE2x3gbpCUtSfL-uWsb2BVeFeqKqlPDAAIevBfudxmi9GTOVYZWGdvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار ناشی از حمله پهپادی امشب سپاه به کویت
گفته می‌شود مخازن سوخت ارتش آمریکاست.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6117" target="_blank">📅 06:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6116">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/360d24e506.mp4?token=fOr0dr6b34SIkGn11c4XIoPOHeR8c8PvW6OwEOPH8aPvCb87U7J-VIqrRmxp7leWByn2TvZsVw9u_lBpQaEsF_2v5ZOXfHqcJo7f82Ij6gO35pznUSGADPpmXV7zBZj3yc3kCe8ZXyS1VSmOqr0vbIMBm9nDC1dWf23v2tNVc_AqeQ_grzPYXi74uBkoVnggfSf2k2lh6r27XTwntQvJ-rLKqquKHlxgj9GXwkKWP8tNGO1TBEAyzWEd0geDSnGEmSF54Sp8SRyxYGOnGx3frsHAPcw_TvuvgN-9dCgp8_IHDHYXq_8zJmTGSEHkFAUkgYtkyx2gDrdcsdXX_m7QZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/360d24e506.mp4?token=fOr0dr6b34SIkGn11c4XIoPOHeR8c8PvW6OwEOPH8aPvCb87U7J-VIqrRmxp7leWByn2TvZsVw9u_lBpQaEsF_2v5ZOXfHqcJo7f82Ij6gO35pznUSGADPpmXV7zBZj3yc3kCe8ZXyS1VSmOqr0vbIMBm9nDC1dWf23v2tNVc_AqeQ_grzPYXi74uBkoVnggfSf2k2lh6r27XTwntQvJ-rLKqquKHlxgj9GXwkKWP8tNGO1TBEAyzWEd0geDSnGEmSF54Sp8SRyxYGOnGx3frsHAPcw_TvuvgN-9dCgp8_IHDHYXq_8zJmTGSEHkFAUkgYtkyx2gDrdcsdXX_m7QZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی با موشک‌های حاوی بمب‌های خوشه‌ای به بحرین حمله کرد.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6116" target="_blank">📅 01:44 · 24 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EFuz8A0bJQMbkPdOQgTgLQiI8LDamoxkiYi2y_ko77Q2QibDhNk2sKA7ZG4IVd6b1t_U5Ml0KGUQnA5Qcei4PfZh43wdpHr7loHLC0Rq1sonvvSDDUBKK9_LIBrY8sktyvrkLgo2viWE0M73VA2j8Jwwh-OaYKuz_uUtFaYxVYZK9iaLKXOx8kJ3DGmd3JBWcUjepzKBmwJlsvxcG6Q2R2h9h4upOuXYaKAQnS_U3U1wXdrfq9ps2VE1vcvXuPePBtKnaK7D2TJmsGjoS_6IVEws0t_puFbkM6tIgfTNuntbkADOrdgpXYfwCe-tvuqMd5uIGAzLMdTkMLivWyYpJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگارهاشون می‌نوشتن که کشتی‌ها دارند  از مسیر عمان رد می‌شوند، تشییع جنازه،  بریم و کاری کنیم که  کشتی‌ها مجبور بشن از آبهای ایران رد بشن  و شروع کردن به حملات به کشتی‌هایی که از مسیر آب‌های عمان میرن.  به زور حمله میگن کشتی‌ها باید از مسیر ما رد بشه.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6113" target="_blank">📅 01:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6112">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jPc7JCtRWY_35vUn0OZEzzQIbBdxUoLxSmkYuq64Z8icSOpOfuZ3fWhR8j_3qfZBvWv5WGP4hRNrNWce-4Ml7wYSR9rVv1W_PlOUSOJ1SueJY0U-hHQJ6oR4-b8tBLDDsObhGE7Eh0LvIjllRgfhofaPdxsz-OR2X6nXKVe9vurRm5wvJn8vmOBHM_1qp7Wdoy0BBcBlkSJVIEcbjLL9iSEUPG1Qu350ThNz5l8FcWFkRXH5EDfMdGzMDr-krwVMYEh55eVYZ01uhZc4ROsg6-Tlt-VJWU7wZhctnWfzrImGJNknH0vYbHl5WIjlUQNPuKpcLBFg1ZsyEU6-ZO6woA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینجا در حاشیه خاکسپاری جسد خامنه‌ای و جلوی قالیباف شعار میدادن «مذاکره با دشمن خیانت است»  هنوز به سه کشتی حمله نکرده بودن و نزده بودن زیر تفاهم نامه</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6112" target="_blank">📅 00:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6111">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d90d3d98f9.mp4?token=Ca_F9RG5LSicACCwhQjV-W1REz7TiozpOzyavyRf776qTDlKxItbiPCuPhA10zrzxLsEZEoEXL4CRVPWI1tbDTIxUCs4Ob9EGc2xGs4gTqwyIc0dGU6s7Fiu3H1Zy8fVqsPRMgbOuUUOCcD9JC4E36JfX-9KcdNigb7ikcA6TPKPlr1Y0qUjG8tP1gmSNlfPUm1wv1XiZUWpv0bZkJYy_XK-csrxZXD7UgF0tnrm4PzT8lcthxtRVBviy7ZBWYfZuIXpZ-mAttm451aYoezSJvic85MWod-mjapRC7ta0zjVAkJZICefClnDeSX-2tae6oyP-_poy3PAI8497Hk7Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d90d3d98f9.mp4?token=Ca_F9RG5LSicACCwhQjV-W1REz7TiozpOzyavyRf776qTDlKxItbiPCuPhA10zrzxLsEZEoEXL4CRVPWI1tbDTIxUCs4Ob9EGc2xGs4gTqwyIc0dGU6s7Fiu3H1Zy8fVqsPRMgbOuUUOCcD9JC4E36JfX-9KcdNigb7ikcA6TPKPlr1Y0qUjG8tP1gmSNlfPUm1wv1XiZUWpv0bZkJYy_XK-csrxZXD7UgF0tnrm4PzT8lcthxtRVBviy7ZBWYfZuIXpZ-mAttm451aYoezSJvic85MWod-mjapRC7ta0zjVAkJZICefClnDeSX-2tae6oyP-_poy3PAI8497Hk7Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این استوری رو ۶ روز پیش گذاشته بودم  میگفتن آمریکا میخواد آتش بس حفظ بشه ولی جمهوری اسلامی باید «کار دیگر» بکنه!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6111" target="_blank">📅 00:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6110">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/550f13e765.mp4?token=LVUU5qnCtlTHuBLGr3uAsAf2AmBdHuZusmDxLXJxoCpZNYSO5EpHLEBd8f2N32HnGXQz-WHWvR4HVtaRPfsSS-NajxPWr1Z44KaAA0hjbDUkHBnFv0ZNTCo9TRhgRTGmx5ht6KIvhVdz52Nw4AVhJ1YZnc_d11Z_y68l8pkig1NhIp6M7g0YPaVw7GpUMS0BBwc9QeUIf1HQmBPkfNuk3QsL75gjZ3ZLdxvufRRxqNSr2BnWtAlAmVo8NYNJ0YnMpAov7dOtU40vjQT3BN1E3x69TlzLUxtzPIgWQxnFXSjJOTKK6opYawPYzwnAvJwNux5d0MNIVVvoVYmNxO5OtYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/550f13e765.mp4?token=LVUU5qnCtlTHuBLGr3uAsAf2AmBdHuZusmDxLXJxoCpZNYSO5EpHLEBd8f2N32HnGXQz-WHWvR4HVtaRPfsSS-NajxPWr1Z44KaAA0hjbDUkHBnFv0ZNTCo9TRhgRTGmx5ht6KIvhVdz52Nw4AVhJ1YZnc_d11Z_y68l8pkig1NhIp6M7g0YPaVw7GpUMS0BBwc9QeUIf1HQmBPkfNuk3QsL75gjZ3ZLdxvufRRxqNSr2BnWtAlAmVo8NYNJ0YnMpAov7dOtU40vjQT3BN1E3x69TlzLUxtzPIgWQxnFXSjJOTKK6opYawPYzwnAvJwNux5d0MNIVVvoVYmNxO5OtYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/e0b9d2dcec.mp4?token=rBoMZ7mK4Cvv-HM6bH2Qb_cA718pGks0kyS9XncbNjHtbjSgbU9BhC62UqIPpviEw_7H2r_U5JyncZrgvQMYPZM8i00AGf8VlJjIo9PPoG6fOq9pbQ4p2D_nq-BqyuUjvN8FxJKI4rRi_mnzXmetHuhQ8DZzItzORtKStIbY2BBbNgUR9vMNQEH1aU0PvLhMYAz1DB0o4u6u2Tf0AL36FvRfNUrEJ_nQRbxtyV5ThFg25xKysGOKRXgRRskFh-EbRTqPAurQXD88HftK4dMk9AO_19BHY8p109VMNppw0W3TazMx3PyJi-zGps0_Fr9w7N6mVsJDq2XbZPM6r_ygtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0b9d2dcec.mp4?token=rBoMZ7mK4Cvv-HM6bH2Qb_cA718pGks0kyS9XncbNjHtbjSgbU9BhC62UqIPpviEw_7H2r_U5JyncZrgvQMYPZM8i00AGf8VlJjIo9PPoG6fOq9pbQ4p2D_nq-BqyuUjvN8FxJKI4rRi_mnzXmetHuhQ8DZzItzORtKStIbY2BBbNgUR9vMNQEH1aU0PvLhMYAz1DB0o4u6u2Tf0AL36FvRfNUrEJ_nQRbxtyV5ThFg25xKysGOKRXgRRskFh-EbRTqPAurQXD88HftK4dMk9AO_19BHY8p109VMNppw0W3TazMx3PyJi-zGps0_Fr9w7N6mVsJDq2XbZPM6r_ygtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6106" target="_blank">📅 22:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6105">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gyChOpwAysP_QViB3MIaQggp5TOCUP-hVAoVPhEN1sFJglZedZj_-_qawy5_SrNkXApOyx1t3HZ1slKTunYxla1ktCRFpwSbDJS6ffPKqi-hLWuPk1xmnGY-o5ygOlmlhPUeePufUz-0UYImobz1NBNfjMA-90Lx67mEGG0TzZ1Zi8u3arqCTjwvpmIt6DT5sH_ayOrR7CaN4zVxMDca4UDVDyyjp2SV5Ec2tgSFUy086SvTmr9BLZVX2NtWiV3W3jJ4caYdEYzHuT30nGHMmxTeyXu_oF2IxSFtWOcTDlOEupYGWD9YUwQU4JQeQxF76RR5ECc5wGrlNiZiefpFhw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6104" target="_blank">📅 20:00 · 23 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5EcNHmHo6hDE9gbcvWZgnTIyM6LNcCnOR14_P9Mao7dgOSFl6ffyLWdFxNaj2TFFHOjpYVGpmKpTq4toy2_uDtyFhVKQ-frbFxRGfhaTB5nA8U2ekrAmnNHMUqn5mi_M3HVE5di12EhJxBMJLg7qdXJb4XvqT2QS1u-1fpszwyn1o5h0Usg-ZpRnwg8I6d0A4gxPwIs4voBBbMqWzDF3u_VvGEb5OyDnSayTAdSnq4tK4CGRtNdM27-RvORYlAOBwU5LSDMJ5mUVcQCd4glyzKwCYxHA8GYzqi58LRbS4ykmT7c13QDzfQodtiHCcayxDeug7KYUuX8rHBawoFf7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهپاد‌ها (قایق‌های تندرو بدون سرنشین) آمریکایی این مدلی به یکی از مهم‌ترین مراکز نیروی دریایی در بندرعباس نفوذ کردن و حمله کردن.  گفته می‌شود که در این حمله یک زیردریایی ج‌ا را نیز منهدم کردند.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6102" target="_blank">📅 18:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6101">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee96f6523b.mp4?token=DUELQrybH9P20KMfQ7u8CpOCykcWapvl8Wk27PZBrmb2HhdYf0i_Xk9Pfu4CwoBCBSVAv1DuaaKvfuMjGrvhCT8MK06ZOxz-veC3Zk6RXLStD7wmrHtSTDJcHmeHB15gBJi94d_jiCMURfeNw81Tk5FEGBVmB7Y0M-nkaVOxMYIwXOreGxsBtplqwq2C9EBSROTW3DZ9fJoXx1UB1CKxI7kjPmFXuzgW8ZujA_lzrDeZgpqRNMWCYiA_t0rwkKMawSg3mucFMP-ww1nTIdG-1AS5hFlmqd_uYyajFMx4tCYYUajDLZVtJdKkbe994sInVutWSYHQz7IMMBbhZcOqbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee96f6523b.mp4?token=DUELQrybH9P20KMfQ7u8CpOCykcWapvl8Wk27PZBrmb2HhdYf0i_Xk9Pfu4CwoBCBSVAv1DuaaKvfuMjGrvhCT8MK06ZOxz-veC3Zk6RXLStD7wmrHtSTDJcHmeHB15gBJi94d_jiCMURfeNw81Tk5FEGBVmB7Y0M-nkaVOxMYIwXOreGxsBtplqwq2C9EBSROTW3DZ9fJoXx1UB1CKxI7kjPmFXuzgW8ZujA_lzrDeZgpqRNMWCYiA_t0rwkKMawSg3mucFMP-ww1nTIdG-1AS5hFlmqd_uYyajFMx4tCYYUajDLZVtJdKkbe994sInVutWSYHQz7IMMBbhZcOqbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت جنگشون :)</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6101" target="_blank">📅 16:39 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6100">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FkQ7qVe0Q6dv3FlCzb5B_05w17aBxwlOU24JWWdXjEl8FCfZRAf79htxs8ZEtI0tJ2uSqlexXF_Rk11UcsqLBgI2IP05VOBG11i6VOmF7GhKTg1zI29c_VaBOth2KN6riWiJbDspYSBS47_Bb956VDOnsmWq-CjFk53E31m2cTX21Je6sptfMa1A9VmROQpC2hbwpQXKucMd4jbdMYK_SvDL4YA5zp9t4_-upCTeSZBkC4VzVpVlN-86n3cFt-xyGSYrbFh_b0R16xjBSWAm74QtMm4KEJ_fcu2_Hr-F14Vx8BHbevXhRf0qilgq6lUhEGgukrQOyapuLAqA9GNODw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G-IP1CaEQhV9OLD-gRRYA4fdpkUK5xnd4vt3hLfV7nHVobtLwueX-fSsLAKz8RZ49E1Q9cCl7p_vmOWCEwnUIAqdckyfK2D5uETkx2g7PVcE-Q1eVpNT1O_5yLuLYwdama50nlgXj0gViHwGPtxriIQqMFkYre83qMT4lON_1w9nR4Cwo4WmMozSMqLoEmAZDFDbqs5CJQUS69aCnPKbloN38e1a6gZ-xuWIDht6tJjzAMysuWoiSDSnAtc5Z4A57dcMrJVA-lAwLfpwEXxGtkNO3b2qraOImufJqyfRreAH1ycRDbW4M_NJ550VkixrjHdyvUTJKN068-4YurP3dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
تخریب ساختمان مرکز آماد و پشتیبانی دریابانی نیروی انتظامی ⁧ بوشهر ⁩ در پی حملات هوایی ⁧ آمریکا ⁩ به مراکز نظامی جمهوری اسلامی</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6098" target="_blank">📅 15:42 · 23 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/ac9c510f4f.mp4?token=D9vC0MvIIdwJ7zoCiT-NXn4YIX9Teox0zVG0YzPE_V_Ee0RJLkvhscIMnKpr5gGJUy0mTGYH9CKJxzK4zXWkqw3wTno9FkkwIOHiKYpy_mOA_YTyyzsDqQbTAJT2SbViAfHuXDtQW3ucsK0FKKjyI-3rHyyzv5gyWF04kiYvLwH-ZulQLn7uqXd8ahfVTMcPE0JJtxf5J_RLr1ebSbZHWofCC_LJpwKwSRQD7sOB0KYAQyXcnODs5KqQxjJ30Ipd4hJ3O8aPwTwMx15TgMZweMrshK3t0DwTLYMIWWNusgwFyho4yVFjnrWkFSpm8bM8J9C_-6m9FwSxc06I31D7GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9c510f4f.mp4?token=D9vC0MvIIdwJ7zoCiT-NXn4YIX9Teox0zVG0YzPE_V_Ee0RJLkvhscIMnKpr5gGJUy0mTGYH9CKJxzK4zXWkqw3wTno9FkkwIOHiKYpy_mOA_YTyyzsDqQbTAJT2SbViAfHuXDtQW3ucsK0FKKjyI-3rHyyzv5gyWF04kiYvLwH-ZulQLn7uqXd8ahfVTMcPE0JJtxf5J_RLr1ebSbZHWofCC_LJpwKwSRQD7sOB0KYAQyXcnODs5KqQxjJ30Ipd4hJ3O8aPwTwMx15TgMZweMrshK3t0DwTLYMIWWNusgwFyho4yVFjnrWkFSpm8bM8J9C_-6m9FwSxc06I31D7GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">می‌پرسه نظرتون درباره اینکه بدون هشدار قبلی برق رو قطع میکنن چیه؟
‏چمران میگه:
‏شما اگر بدونید پریروز چند نقطه برقی رو زدند دیگه این سؤالو نمی‌کردید.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6096" target="_blank">📅 14:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6095">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UdnZtrU0YFMmkKSQNCi--HaOjbgdJIHYdtiu3XsffCxHxtUGK04wTZRVFOt_nA1lylYT3Az7rti2JhXlWeSldQ5ZuLp0JoKv6QxXM5ELm_LLyo-DdWu2rUtKFDz_60Q_hVNg4JeuYzIjQsNIg2Q4clb0C-XTe7MCgDCC1kX88p4bMdZNtFz3D3QraiXZYgPVDP2KNjVsQfICIdKZRNIT5PXDiIe5g3AD9fHJmLtvOSUjKbaUj2RCLK6YT2hdVUu34eU-LbIDhwhkA4ekLXGEQ-qdLceR7YviWlyjaxxO6MzRAksysDesurQgTlIZnim6XkkqVwdiMyDhpinc4jmDjw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cZypQBQUpwGKnIC5lNq2mRcONXC_EdODp3EmdqUJ0sV65Xyd8QP-qrObj-4woZjoC71zYBlA_P0Kyalx80Tm_pXhWdJ6TXUKtMbhxmzd0eE9Bai5zsRXl1oBOYTcFOk0WyXMjhjA_RMsIKbNBm5GECc4tWZ1Q_sUDL-hc-JXlmy5X6fNeDV7Amt79gQqaSV9d7eS5dSRzkcW60q7KAuS-Pfk8mcPAIiMZgRn36HOh7yi8QcSHmqopROJyLpI-UtN_d0JglzdEkT4u1fxpHvxqIfw9TLZmiar5VBMi62BsEbi3TkYRsBWwwrAk-a8ZzDjNOI5NXjVxnhElyivZVxc7g.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/b04e0dceb0.mp4?token=pfOeFum65ZKLxdL2h1Bq76zMSaQsPnm8yWmKYQUResu_GGBtU_knES9vbCT6nDWmiKTbhVSanKuCnaJxbwdVA7gJQtV_hMWxTMswk4irYxgkvdbTHhDxRyJuZrmkOX1F3xRlmKPYk3EdJSLkLTVYIhxKOrDMZiEBmki4Z36N5M9Wb0eHGLMmrcOx2bcqh-ws4x85i1mVzOnrxrYMyl59SOP-b-oiol7PY6KXufA8QEnhmOylEmkBjYJytWKL5wMVGdJkZ1X_VYBJTjsdbO9N4yvuRHCotRaNNngFm1GjK2UNr4O9GyeFZBT6cYfb7FGxBB1lrxpLGxlsTZ6lFz9sv51LwEQ67hA8sFXTorCmOb50eY3ndKp3Nd4kV2EDgst03MpURuXV0uQ8e6i-Rx1hXtfd89sZuY6xvh9Td6ivB3aJOestiE_q7j1yQcfzRZXDx6UyEzIgzFaZA3lArqEBnqROfW8CNOfxb_JfSAxtyp4K63-9RBbjvh8jyVu-Ha29xrvmVS5BSxiTv6xK0y1feR2YRxG2OowWLUkJ5qBOJ2skuqTcpj5kLQbL7-ImJL0Bn7KpkKjGV1M-42_z8GXi-Dkju3Ut7DpasnfgKT8ql2SAPudV3TB4k2tX7gUKlOxuunnxa4a423Ag-fwVWjkTHsae0RylMAPsUWTqIPKAhlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b04e0dceb0.mp4?token=pfOeFum65ZKLxdL2h1Bq76zMSaQsPnm8yWmKYQUResu_GGBtU_knES9vbCT6nDWmiKTbhVSanKuCnaJxbwdVA7gJQtV_hMWxTMswk4irYxgkvdbTHhDxRyJuZrmkOX1F3xRlmKPYk3EdJSLkLTVYIhxKOrDMZiEBmki4Z36N5M9Wb0eHGLMmrcOx2bcqh-ws4x85i1mVzOnrxrYMyl59SOP-b-oiol7PY6KXufA8QEnhmOylEmkBjYJytWKL5wMVGdJkZ1X_VYBJTjsdbO9N4yvuRHCotRaNNngFm1GjK2UNr4O9GyeFZBT6cYfb7FGxBB1lrxpLGxlsTZ6lFz9sv51LwEQ67hA8sFXTorCmOb50eY3ndKp3Nd4kV2EDgst03MpURuXV0uQ8e6i-Rx1hXtfd89sZuY6xvh9Td6ivB3aJOestiE_q7j1yQcfzRZXDx6UyEzIgzFaZA3lArqEBnqROfW8CNOfxb_JfSAxtyp4K63-9RBbjvh8jyVu-Ha29xrvmVS5BSxiTv6xK0y1feR2YRxG2OowWLUkJ5qBOJ2skuqTcpj5kLQbL7-ImJL0Bn7KpkKjGV1M-42_z8GXi-Dkju3Ut7DpasnfgKT8ql2SAPudV3TB4k2tX7gUKlOxuunnxa4a423Ag-fwVWjkTHsae0RylMAPsUWTqIPKAhlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RgTH6X0Q0safBt5e_BZTaRc9bA75sH5GNKGjYvkzxft8pENBAwWPKZ7pbrOMbySPw9-qh8o9qZ9I6QvxeBz-HVAuYzpfUkUaAu3Haqg7rrCFH3XAgt5gDmNeMQ9XT2TO3CpF8vOh_g3Lbfg2l8yD8qUggpp_QFvdB_LVsZOp0vkwI2kCBv5M9JAUXOGhpG8ghhGdIV5m-tOmjmC1IEajXYdPgU_1b67GWPjD34Tc9AQ-N172ccHjQmYj1h-r7WLts-b7oW2LrQB0VBL6-TxYL7A_MLINrgliSgajcoE5LBHBIq5IIsHDwVZCgandMoAWZc0jsHAWPygCoiIa6kpXbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شب گذشته سپاه به دو سوپرنفتکش (در سواحل عمان) حمله کرد.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6090" target="_blank">📅 09:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6089">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/671b861555.mp4?token=gW11UoyPtege7kJvaY69D8UShSDXu6O8B-WsEpgT55kJvA2onf1WDWb9MGfcVJPPvYHBumqGMbnlJlUQaIlF0wgqjuAgB1BKPS9hvoALRNIMY2_IYSMUHB85IEa-Jh-s477_tSzRoQZTrpLzn22SvfEbUWESZ9pN-oBnd8Z7I2-7icQnooPrgqB3sE21OoRgEMvXl3gvs-dyHd2kSFGF32MbIEjD-9omHrRxGkF1Nllh2_ZTI8vXdXQ2_LpMS1WjD_OhxYZMm9qF79XVZrGiSAl56l1sc9WQ1WdD5yUosxdvjPgiKxmQ5Yw0qxfDAMGUZcHYhCpoIOiFiaigdGz5ETe8uoaqU9ePmqxYBHoWfw1_HdGd70HUtn0JgFYCJscO_WVoERnKyNyObEsuYT19o9ppv4b21sWi1N6zqhyOLk-ab7gfggRrSbIQeRJlETQgjzvKQNHuusmLkBvb0DTsQHKZwfxkqDBLpNrz5YItXTSDiyVv-3apnQZpiAY7bQs8ZBNI_tTJluUY-HZjtaJBaG1QHpl93cZpvD_sQpopncFHLYdilTUi7cVeDofpLBBFowBzidhYOtQirJdic_OVfcy9zZM9POP9GlgwPFiAYl3YYbCAhx1oSnsdo0QZJuurRwkdocD2oETyAESRkZvMeAp5b428Mx9bDuNaEXMuiBM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/671b861555.mp4?token=gW11UoyPtege7kJvaY69D8UShSDXu6O8B-WsEpgT55kJvA2onf1WDWb9MGfcVJPPvYHBumqGMbnlJlUQaIlF0wgqjuAgB1BKPS9hvoALRNIMY2_IYSMUHB85IEa-Jh-s477_tSzRoQZTrpLzn22SvfEbUWESZ9pN-oBnd8Z7I2-7icQnooPrgqB3sE21OoRgEMvXl3gvs-dyHd2kSFGF32MbIEjD-9omHrRxGkF1Nllh2_ZTI8vXdXQ2_LpMS1WjD_OhxYZMm9qF79XVZrGiSAl56l1sc9WQ1WdD5yUosxdvjPgiKxmQ5Yw0qxfDAMGUZcHYhCpoIOiFiaigdGz5ETe8uoaqU9ePmqxYBHoWfw1_HdGd70HUtn0JgFYCJscO_WVoERnKyNyObEsuYT19o9ppv4b21sWi1N6zqhyOLk-ab7gfggRrSbIQeRJlETQgjzvKQNHuusmLkBvb0DTsQHKZwfxkqDBLpNrz5YItXTSDiyVv-3apnQZpiAY7bQs8ZBNI_tTJluUY-HZjtaJBaG1QHpl93cZpvD_sQpopncFHLYdilTUi7cVeDofpLBBFowBzidhYOtQirJdic_OVfcy9zZM9POP9GlgwPFiAYl3YYbCAhx1oSnsdo0QZJuurRwkdocD2oETyAESRkZvMeAp5b428Mx9bDuNaEXMuiBM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: بیشتر موشک‌هاشون رو از کار انداختیم، بیشتر پهپادهاشون رو.
🔺
توان ساخت پهپادشون رو حدود ۹۲ درصد از بین بردیم. توان ساخت موشکشون رو ۸۹ درصد نابود کردیم.
🔺
یه کم توان براشون مونده، اما برای ما هیچ توانی ندارن. این دیگه تقریباً یه درگیری نظامی کوچیکه</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6089" target="_blank">📅 08:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6088">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3962370842.mp4?token=kvqJNxHfac0sYOwE1_w5iBnTmr7oi0XXGTfJH-p9QPasCsjAXkQqemwoDY16FNkHdmVb7LESF0X2FOUiQUS1Fava6K09sHPVfhqmrmhbUykoaIWmZ6JlcC2pgmTwQXy6ce1Xn3-Mi6JXVGYV6bcC2p57jaGKyXU1rs0oGfF0VvJSykPAPVp8BNfr1Ze2diRj40imwtxeblSy0-Lp566MGUvkl9ZkDRbHF88iy45UnOdJfVqzl9t4SnjGwgTjmKJij3dIwylODPyYxARV1MSNgML9FXWiq00lNAQ1zmqthj9xvVx-CrkprL3wr5J36C_wN_WnQAhv52T6qd5jT7AW4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3962370842.mp4?token=kvqJNxHfac0sYOwE1_w5iBnTmr7oi0XXGTfJH-p9QPasCsjAXkQqemwoDY16FNkHdmVb7LESF0X2FOUiQUS1Fava6K09sHPVfhqmrmhbUykoaIWmZ6JlcC2pgmTwQXy6ce1Xn3-Mi6JXVGYV6bcC2p57jaGKyXU1rs0oGfF0VvJSykPAPVp8BNfr1Ze2diRj40imwtxeblSy0-Lp566MGUvkl9ZkDRbHF88iy45UnOdJfVqzl9t4SnjGwgTjmKJij3dIwylODPyYxARV1MSNgML9FXWiq00lNAQ1zmqthj9xvVx-CrkprL3wr5J36C_wN_WnQAhv52T6qd5jT7AW4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات شدید به کنارک - امشب</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6088" target="_blank">📅 01:06 · 23 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
