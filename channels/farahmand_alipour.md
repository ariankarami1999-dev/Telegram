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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-26 17:40:19</div>
<hr>

<div class="tg-post" id="msg-6186">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pj5r17LvhYKZPKH_z4Yr62thpiFHiUk8LiH26S0LqfbzRr4anLt-I4ZlHGmLLLokjaV7l3yCbMbH_sSwpzpoZRl_bN13-AuNvNRSDhRXn_0pWfAMFXI4j00iMQrdXOrrZlNW__UkxJ6YAYYDdIKuzjK2jXSON60UJVXKLGpSiLQs7ewG1M34omN483pt1bgKdxYdtLJ4MBnsrZGMgPCBlKZyeS0uSstBfzav_2qmMuBExOvZT22uS2fGMWylDiqDPF-rg6O1gBmACv9_Vtg-0tRr1_lFJMPu0svI6UoBFTlaJtH_Ay8aPYXXW4r5GwjOUXuhxMzY67FHpPB16lEb8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عقل عرزشی !
من میگم اینها شکست‌های تاریخ
رو پیدا میکنن و به عنوان الگوی خودشون معرفی می‌کنید باور نمیکنید :)
تنگه احد! که نماد بزرگ‌ترین شکست و عقب نشینی مسلمانان در تاریخ صدر اسلامه،
رو شباهت سازی میکنن با تنگه هرمز
‌‌میگن همونطور که اونو در سیطره داشتیم
اینو در سیطره خواهیم داشت.</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/farahmand_alipour/6186" target="_blank">📅 17:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6185">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farahmand_alipour/6185" target="_blank">📅 15:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6184">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ijt5NRK3bltsYCoHkEWDkhrcfi5qZ--8GXUF5P3-8IK0TPqriYcGaj_rju2tJ7vUgwYsS5u9HmUMtsvwofBpwQIY_G8VauO1lhDEPE79BAXOnZcWgApkjZp8GP76Nxi2zQQ9wVFiPyWCkbhC-9yvd0w_1ZnHvvy65JIPelk236nzSTkWZJOOo82ttchl91wf8Wqd9mCD7pIa5mPzdbLXD1iNMUNym65cPe24AyUPfo20PC1xb_MnWNYdf5MmiJ0HfjfWiWjCciXf3-nfQwoVq71WQBin3R_7y7TWbh_DZcycgfxnLxzhmpI6d4g18W17wla0suaespRUpAdDgjiyJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جمهوری اسلامی به تاسیسات آب‌شیرین  و تولید برق کویت حمله کرده.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farahmand_alipour/6184" target="_blank">📅 14:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6183">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61a69b588c.mp4?token=JYCCchxyPd6A7ilQkz80EaXyVs2eEsT0foYs0LNA-hNCrlVX8uDIyd-GqnSj5S2pA-NoJCWDs722GN6rh_Ulp8FaQ0otBJuAQbmpJQ708RODUIsw74MXBXvtq7PL43Lw1-UcXriz7sjhxUJ_-S4b-ut0y0jgQ6bDNuTeQqHPL1cMhNAvReGvM30SDFNiUAhxndwwJO1AJzo07_DC2-7eu59ijUkCzJoG_7SBCDpUqnnqNyZzxS9d3tfNka8FoWGidqeZPqX2Fe-VYDqyVPpf4atEFBFm_dWFHWLR04c2eYcB5XOY4r0ClYFla4O8NDsMZLeR8uv-naHUfuY0s1njVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61a69b588c.mp4?token=JYCCchxyPd6A7ilQkz80EaXyVs2eEsT0foYs0LNA-hNCrlVX8uDIyd-GqnSj5S2pA-NoJCWDs722GN6rh_Ulp8FaQ0otBJuAQbmpJQ708RODUIsw74MXBXvtq7PL43Lw1-UcXriz7sjhxUJ_-S4b-ut0y0jgQ6bDNuTeQqHPL1cMhNAvReGvM30SDFNiUAhxndwwJO1AJzo07_DC2-7eu59ijUkCzJoG_7SBCDpUqnnqNyZzxS9d3tfNka8FoWGidqeZPqX2Fe-VYDqyVPpf4atEFBFm_dWFHWLR04c2eYcB5XOY4r0ClYFla4O8NDsMZLeR8uv-naHUfuY0s1njVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۱- ما مخالفت کردیم، بعله، کاملا درسته!  ولی آیا شما به خاطر حرف ما دیگه لبنان رو رها کردید؟ نجنگیدید؟ پول و سلاح نفرستادید؟  به خاطرش حتی موشک به اسرائیل نزدید؟  (که اونهم اومد در پاسخ ماهشهر رو زد؟)  خب جنگیدید و شکست خوردید!!! هم در لبنان،  هم ‌در سوریه…</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farahmand_alipour/6183" target="_blank">📅 14:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6182">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farahmand_alipour/6182" target="_blank">📅 14:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6181">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/6181" target="_blank">📅 13:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6180">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6180" target="_blank">📅 11:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6179">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6179" target="_blank">📅 09:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6178">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26ef12b93f.mp4?token=gQaoAYWVaDThIrFT6v0SMdZMNkx4TA3jclUzJzT9SgLoVyYvzuBAs6Gqhy-_N1k277GGoVX_IbMcnKXIi2CDlrcALulHj5YDfNCoc5xEiJmSd-oCVl67n9jjSyZmYi0GvVBmGcUzDtZOUCBay9OlrZL-K82Y7uepqgS64LBzJHQ9T2STfxdAwJyXZOvWXqob52USmf2qIcnLulhQS5Nx2tPylu74o9IGWjepVmiuJHO9Dm0DqB6uePJagxSEdy8Tpqe3kmyGHlbVpYfzZvIFNgyCM44qLm0sepNM26eUD5tGSKyO_EX3uoUX02PkJRi-qDv_EmDegjDMFWulTVmJPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26ef12b93f.mp4?token=gQaoAYWVaDThIrFT6v0SMdZMNkx4TA3jclUzJzT9SgLoVyYvzuBAs6Gqhy-_N1k277GGoVX_IbMcnKXIi2CDlrcALulHj5YDfNCoc5xEiJmSd-oCVl67n9jjSyZmYi0GvVBmGcUzDtZOUCBay9OlrZL-K82Y7uepqgS64LBzJHQ9T2STfxdAwJyXZOvWXqob52USmf2qIcnLulhQS5Nx2tPylu74o9IGWjepVmiuJHO9Dm0DqB6uePJagxSEdy8Tpqe3kmyGHlbVpYfzZvIFNgyCM44qLm0sepNM26eUD5tGSKyO_EX3uoUX02PkJRi-qDv_EmDegjDMFWulTVmJPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادی از سخنان سردار نقدی : اگه حتی به آمریکا حمله کنیم، قدرت پاسخ‌گویی هم ندارند!
با کدام پشتوانه اقتصادی میخواهند بجنگند؟ با کدام پشتوانه مردمی خودشان؟ همه جا در محاصره ما هستند.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6178" target="_blank">📅 08:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6177">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d050ea81f.mp4?token=GXFlQQbFMPL99OuKitmuYM7_gpOlEx2qvvIZ7PIOj8YGh4HIcm7Qf9a69gzckHFe2P6Rybhsfz85WWpn_UYp4cVW7Rl9b56DHYLZDncL0Faokm3P68zdXk2GDl8lju5GUM8ZYPRXODiqbeJojQDpsoS49r5oL07Gu3sQ_kciZ96BimKoCZnS-ciA_qz1mF_86f_hO-Jcorra3AJ8-nsM2eRkUGgFB2pjk_giCybNORsGxvGwwGxWkoiG1hpTKxYs__RiD87pTTElgON6_LsxkvLS1nohQtEmgs4QwKdwG5uS9_n6RIKT5PPvOgpRaX8uecZdxrTHU7CpjWftT5smiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d050ea81f.mp4?token=GXFlQQbFMPL99OuKitmuYM7_gpOlEx2qvvIZ7PIOj8YGh4HIcm7Qf9a69gzckHFe2P6Rybhsfz85WWpn_UYp4cVW7Rl9b56DHYLZDncL0Faokm3P68zdXk2GDl8lju5GUM8ZYPRXODiqbeJojQDpsoS49r5oL07Gu3sQ_kciZ96BimKoCZnS-ciA_qz1mF_86f_hO-Jcorra3AJ8-nsM2eRkUGgFB2pjk_giCybNORsGxvGwwGxWkoiG1hpTKxYs__RiD87pTTElgON6_LsxkvLS1nohQtEmgs4QwKdwG5uS9_n6RIKT5PPvOgpRaX8uecZdxrTHU7CpjWftT5smiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پل  کهورستان در اطراف بندرعباس
که شب گذشته مورد حمله ارتش آمریکا قرار گرفت</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6177" target="_blank">📅 08:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6176">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔺
معاون استانداری بوشهر:  شب گذشته ارتش آمریکا با چند موشک به پایگاه‌های هوایی و دریایی بوشهر حمله کرد.
🔺
خبرنگار صداوسیما: دیشب به تأسیسات برق و مخزن سوخت فرودگاه ایرانشهر حمله شد.
🔺
دیشب ۶ پل مورد حمله قرار گرفت از جمله پل‌های رفت و برگشت بندرعباس - لار …</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6176" target="_blank">📅 08:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6175">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6175" target="_blank">📅 08:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6174">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
حملات شدید به بوشهر</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6174" target="_blank">📅 01:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6173">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0adb998b26.mp4?token=rd13S5pp3Kce2cy9fpX1B_3zEhMs-C1kBcIzJxS1W10WbsOI4Zl5yMm6F_yeys6DbAZEWPTSeHC5tQZj208lKrKKqpufGoLsElX9B44vrWhqGk_2emnFfS1GGMgXrNpIKkOP4CA0Do1etuFX_ITx412w9AeVaNzJEkEKCuEYOibKHDvYJggvv18-gu78UagO_75uaTEVCABDih44ovev7qxpfBNLdXktrjvNFLfLKv5AAi3ZSoiruio6xY1VtxnvTGdSFbxwqs0B1ZW1V8dqhlvHo8CE5uxYGm48SfztDYa5QdB8XbXUIKunTFMFOmh4OxNKB-QZrEohR_8lqFrS3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0adb998b26.mp4?token=rd13S5pp3Kce2cy9fpX1B_3zEhMs-C1kBcIzJxS1W10WbsOI4Zl5yMm6F_yeys6DbAZEWPTSeHC5tQZj208lKrKKqpufGoLsElX9B44vrWhqGk_2emnFfS1GGMgXrNpIKkOP4CA0Do1etuFX_ITx412w9AeVaNzJEkEKCuEYOibKHDvYJggvv18-gu78UagO_75uaTEVCABDih44ovev7qxpfBNLdXktrjvNFLfLKv5AAi3ZSoiruio6xY1VtxnvTGdSFbxwqs0B1ZW1V8dqhlvHo8CE5uxYGm48SfztDYa5QdB8XbXUIKunTFMFOmh4OxNKB-QZrEohR_8lqFrS3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏فارس: جزییات حملۀ   آمریکا به پل‌هایی در شهرستان خمیر؛ ۲ نفر شهید و ۴ نفر مجروح شدند</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6173" target="_blank">📅 00:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6172">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iYCu8XrF-1WqfnO07o-fr9OaKRkYH1w8FqQMzfE9ZZDlMdXe3zyxME8VlPcIdomEPmFYv6E6wgnaYe7qNwZ1AyBqGhZuogz80itTU6NtXBkS0y3gAjYL9gwZ55u7zFKCD9SOlrEVg1hYxeeZexZNr89hUAV9Ifaeqa2MaFh0Q6F_h8Cp-J3H_r2I_g6ZwkFRUt1kWI6L1SKqFJAv_IbJMHdEt9vwTzRYkyv6bY55NmmA_mcih6bOVpyK58g9LTH4SEY_vNrImKx_28PZV2h7RRdQsvVwPblwpLzBdEeugkG3pRXNeHeyQ1oHW1hZBvzV8IVIABR6U_YGDiHuKssflA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله به یک پل در اطراف بندرعباس خبرگزاری‌های داخلی : پل ارتباطی بندرعباس و لار و شیراز  بود.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6172" target="_blank">📅 00:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6171">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
صدا و سیما :دقایقی پیش ایستگاه انشعاب راه آهن بندرعباس از سوی دشمن آمریکایی هدف قرار گرفته شده و ۲ هموطن مصدوم شدند.
بندرعباس مهم‌ترین دروازه واردات و صادرات کشور است و شبکه ریلی بخش بزرگی از این حمل و نقل را بر عهده دارد.
این حمله می‌تواند به حمل و نقل کالا ضربه بزند و به آن اختلال وارد کند،</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6171" target="_blank">📅 00:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6170">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
حملات گسترده به حمیدیه و شوش در خوزستان</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6170" target="_blank">📅 23:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6169">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
حمله جنگنده‌های آمریکایی به فرودگاه ایرانشهر</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6169" target="_blank">📅 23:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6168">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6168" target="_blank">📅 23:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6167">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6167" target="_blank">📅 22:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6166">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48c1ef79b3.mp4?token=NQ6Qiy1Bhdewspuscq4b1vDu1heNLjed5DCLGlv3RmIBk2BVoIizo_g-g39BtMKOzzGXSwMk37BdN-5JrtXxfC8XjUtp0pnDvC5ZQXxJLUoZKu7j6wlr3cUld672B_QpUZ_RAx9hc4sKK3e51j_el4RUPuA0oOD7U0rMyge6NhMzcXoKdAhmnKNuOs1jMboMtomQ-rPE09opj6dXBgbmpyeqC3bKxplCvqa_HLf2g_PniT3UUmw4sxWN_flEZhtZCT3XijMDwn9ASn1ke6aKp-VHmpLeWqs0CaWgr_laWxi5DIhEZ7PUdyzosuFCVE9ptP3tRlZSa0H51oMTWaMahg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48c1ef79b3.mp4?token=NQ6Qiy1Bhdewspuscq4b1vDu1heNLjed5DCLGlv3RmIBk2BVoIizo_g-g39BtMKOzzGXSwMk37BdN-5JrtXxfC8XjUtp0pnDvC5ZQXxJLUoZKu7j6wlr3cUld672B_QpUZ_RAx9hc4sKK3e51j_el4RUPuA0oOD7U0rMyge6NhMzcXoKdAhmnKNuOs1jMboMtomQ-rPE09opj6dXBgbmpyeqC3bKxplCvqa_HLf2g_PniT3UUmw4sxWN_flEZhtZCT3XijMDwn9ASn1ke6aKp-VHmpLeWqs0CaWgr_laWxi5DIhEZ7PUdyzosuFCVE9ptP3tRlZSa0H51oMTWaMahg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئویی که گفته می‌شود
از حملات امشب به بندرعباس است.
دقایقی پیش بندرعباس ۴ بار مورد حمله
قرار گرفت.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6166" target="_blank">📅 22:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6165">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‏
🚨
🚨
سنتکام: موج جدید حملات در پنجمین شب پیاپی را شروع کردیم.
🚨
مهر: حمله مجدد آمریکا بندرعباس
در ساعت ۲۱:۳۵ نقاطی در بندرعباس مورد اصابت قرار گرفت.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6165" target="_blank">📅 21:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6164">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbd6cb3b5f.mp4?token=iLp-ZXF9yzNK8eKq8JlOazZkeRBp8Fy2MzQocQQm3cg6Dyokx82V9SPOtlt8syuLVJBFsqf0Z5ju1q2RzXSh1QixVn1CVNUlCsD4NNo2NKX0U3fy9p5kxQ15PPBxnnEW19Uymj3TLZL6Dr5tRZ6bjP1xe_TjXzJlErQeKIs4MdixgVyLI7KSYHNzzmqQTcyKt_w1EKrqF8YJ3EVCOVQnFerxJ9fLWWQmvuiOu7MCSvdNT5nbd4aKzZCzKGv6TQeAbT5NYUW_hlcvfsB9GWYk9zAM3JYky9UTtgTXiP3n-9UrBKg8ZkhHwRk_vK6rJlPvkX7nZjAEcjjNwfUKvzJ55Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbd6cb3b5f.mp4?token=iLp-ZXF9yzNK8eKq8JlOazZkeRBp8Fy2MzQocQQm3cg6Dyokx82V9SPOtlt8syuLVJBFsqf0Z5ju1q2RzXSh1QixVn1CVNUlCsD4NNo2NKX0U3fy9p5kxQ15PPBxnnEW19Uymj3TLZL6Dr5tRZ6bjP1xe_TjXzJlErQeKIs4MdixgVyLI7KSYHNzzmqQTcyKt_w1EKrqF8YJ3EVCOVQnFerxJ9fLWWQmvuiOu7MCSvdNT5nbd4aKzZCzKGv6TQeAbT5NYUW_hlcvfsB9GWYk9zAM3JYky9UTtgTXiP3n-9UrBKg8ZkhHwRk_vK6rJlPvkX7nZjAEcjjNwfUKvzJ55Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ازغدی : اگر میخواهیم اغتشاش نشود
باید با آمریکا مبارزه کنیم
(که حواس مردم به جنگ پرت بشه
و تقصیر کاستی‌های حکومت بیفته پای جنگ
و دوباره جنگ بشه «نعمت» !)</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6164" target="_blank">📅 21:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6163">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
استانداری هرمزگان:  در ساعت ۱۸:۱۰ امروز نقطاتی در قشم مورد اصابت موشک‌های آمریکایی قرار گرفت.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6163" target="_blank">📅 19:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6162">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ef2WqiV00GThLeJZ_LQP3Ng0_NrDYowKnswGMbZ45AKwzp1mJ-6zCJ9sHXBH6KosF7VfPF0H8AYJ7aR_mxAshr71X1dTOoblOlejJ7ldJrEhDgdhLn19g-cpLvyxa54riAnPJUxFlq7R7id_GRZ2ynZg31QECKLX3V6xWGUMgrpVGhMRSyhrEk691CkiN4AuV-njx9e3y5pvTD1BKRLN_vk9mmiC24NwROp2JgzMsxvpn5Mts1BqHWESLacWW4wSi_zhDO_glJm_OwSR6wTdJOQK9ruYY6oRfLeRtI1xpMac9QoUF2emZwIKjQNWW5VV1z5O1iU_8YHvc5H6I4iZYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رویترز :
پاکستان به ایران هشدار داده‌ که اگر به عربستان سعودی حمله کند، پاکستان آن را حمله‌ای علیه خود خواهد دانست و اعلام کرده‌: «این خط قرمز ماست.
»
پاکستان و عربستان قرارداد پیمان دفاعی مشترک دارند که بر اساس آن حمله به هر کدام ، حمله به دیگری تلقی می‌شود.
🔺
برخی اعتقاد دارند که یکی از انگیزه‌های اصلی تلاش پاکستان برای میانجی‌گری میان ج‌ا و آمریکا ، نگرانی از وقوع جنگی است که دامنه‌اش به عربستان برسد و پاکستان را ناچار به ورود به این جنگ کند.
اینک که تفاهم نامه کنار رفته، پاکستان بیش از پیش نگران این موضوع است.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6162" target="_blank">📅 19:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6161">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
استانداری هرمزگان:
در ساعت ۱۸:۱۰ امروز نقطاتی در قشم مورد اصابت موشک‌های آمریکایی قرار گرفت.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6161" target="_blank">📅 19:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6160">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0a471388f.mp4?token=odTYSqMApeFPY7Ws3LYwEdDtCr4PAKpc1WF1v41-WwRQj1NXA8Mawe5r73_NVLAA-ZigfSxih1AzPsgWKZ3wV-Jer8RxRTaYiWCzoqCEE-CPfYExgiAu8607-nRwlUUMl0QjSs-Iie3V4kXOr4ZTGE6ZOJJQBXEvbN5ptDZy1o5-Nv3caKCdEPT1OZFkr4wWjao8NjA9M4raaS-SrrCqyvdHvwjMu4ulWkfw18RHTMraOIjLHqbjQLEGURy8gF2JFXjEbw6GBubCwF6_s_Mx5qZw9cmuE9ApKhe1tImAqvx_DCPwA7NXWDaQ-3lKfUo75XCR3igaax7aAZVP820OazgqVtGIVf7ECbyHgNOUBz9sm9agT0jgFC83Iz6L0tYRiiwSTd4W14-DYJ1uTA2LGgfqizsKzXkYjnnDrsZsrXt8pbxw6_euMpbZ0mdznLGOrnkidUUmanjN9Kkm8uiZPifhLfqj7oh2jfLPA2DkgMb49rxOGvxEAOsU1aqbDNHZuCSg8CL_wib6neukSIs76Bgs7Tbq7nj3khrqou42rshpVV5bPRXQKrOxllfodoynyt1P_kyxz7I2ISmYY7sei-m2cin5rnSnOn4piN3i3HUWr1F2c2m_Yg7TniVlSlx7obkzaXRJ_f3FFaPLbdDbiRgNGkY3hgLmGrWnJ-de68A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0a471388f.mp4?token=odTYSqMApeFPY7Ws3LYwEdDtCr4PAKpc1WF1v41-WwRQj1NXA8Mawe5r73_NVLAA-ZigfSxih1AzPsgWKZ3wV-Jer8RxRTaYiWCzoqCEE-CPfYExgiAu8607-nRwlUUMl0QjSs-Iie3V4kXOr4ZTGE6ZOJJQBXEvbN5ptDZy1o5-Nv3caKCdEPT1OZFkr4wWjao8NjA9M4raaS-SrrCqyvdHvwjMu4ulWkfw18RHTMraOIjLHqbjQLEGURy8gF2JFXjEbw6GBubCwF6_s_Mx5qZw9cmuE9ApKhe1tImAqvx_DCPwA7NXWDaQ-3lKfUo75XCR3igaax7aAZVP820OazgqVtGIVf7ECbyHgNOUBz9sm9agT0jgFC83Iz6L0tYRiiwSTd4W14-DYJ1uTA2LGgfqizsKzXkYjnnDrsZsrXt8pbxw6_euMpbZ0mdznLGOrnkidUUmanjN9Kkm8uiZPifhLfqj7oh2jfLPA2DkgMb49rxOGvxEAOsU1aqbDNHZuCSg8CL_wib6neukSIs76Bgs7Tbq7nj3khrqou42rshpVV5bPRXQKrOxllfodoynyt1P_kyxz7I2ISmYY7sei-m2cin5rnSnOn4piN3i3HUWr1F2c2m_Yg7TniVlSlx7obkzaXRJ_f3FFaPLbdDbiRgNGkY3hgLmGrWnJ-de68A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنرنمایی جدید جمهوری اسلامی</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6160" target="_blank">📅 19:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6159">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfb27a8797.mp4?token=dCCP7YZjhoggxSFDllNVlCFBcUh8NXFIJVT-Pa0q0xmbGWaW46BrJpGwzW-OJSJmUG0jZusnikTAtW-6FKkgyrdr_IM_37UMALPcDF6RQQcVfsnpvAYOOpDpp6WVwX93Fuk-5SpG34QcwRbiqDVWUEknlcFehULrFFgseu2nAiRDEPykpllLNO-wnckalMhOPoUXRXliA-HmumOkRdgoCkmyB7U6IzgchfEgB9Qaedf_YIIwGh9G3QUP0-gqc2nJhm8RlXfefvTBcd--gvB-0cjPOSIxY5iAHroNOpK0rsYOy3G8PfDVdhhL5MGHuhE7w3D5tmGtagHEGCxfX8Y6oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfb27a8797.mp4?token=dCCP7YZjhoggxSFDllNVlCFBcUh8NXFIJVT-Pa0q0xmbGWaW46BrJpGwzW-OJSJmUG0jZusnikTAtW-6FKkgyrdr_IM_37UMALPcDF6RQQcVfsnpvAYOOpDpp6WVwX93Fuk-5SpG34QcwRbiqDVWUEknlcFehULrFFgseu2nAiRDEPykpllLNO-wnckalMhOPoUXRXliA-HmumOkRdgoCkmyB7U6IzgchfEgB9Qaedf_YIIwGh9G3QUP0-gqc2nJhm8RlXfefvTBcd--gvB-0cjPOSIxY5iAHroNOpK0rsYOy3G8PfDVdhhL5MGHuhE7w3D5tmGtagHEGCxfX8Y6oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر قالیباف، تیر ۱۴۰۳:
ما غنی‌سازی را ۲۰ درصد کردیم جنگ شد؟ ۶۰ درصد کردیم جنگ شد؟
hafezeh_tarikhi</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6159" target="_blank">📅 18:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6158">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ایران که ۴۷ ساله که در آتش فتنه اینها می‌سوزه</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6158" target="_blank">📅 17:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6157">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">سخنگوی قرارگاه خاتم : هر چه در منطقه سالم مانده از نجابت جمهوری اسلامی است!
ذوالفقاری: «همه آنچه که بنا به نجابت ایران هنوز سالم مانده، یعنی تمامی زیرساخت‌ها در منطقه، زیر ضربات پولادین نیروهای مسلح مقتدر جمهوری اسلامی در هم کوبیده خواهد شد؛ آن‌چنان که اثری از آن‌ها بر جای نماند و گویی از ابتدا وجود نداشته‌اند.»
سخنگوی قرارگاه مرکزی خاتم‌الانبیا همچنین دخالت آمریکا در تنگه هرمز را «خط قرمز شکست‌ناپذیر» جمهوری اسلامی خواند.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6157" target="_blank">📅 15:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6156">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ca0d3dd94.mp4?token=SitkDNqvuA8k0vcyauq_FSBtBsZxrGg7BM3c1SnpOb7L0dW3AWFSDGcWV2qDlzSp9vzUEmVhwoTrPeOjDE0Mpa7RrZjswN1b0MHZTh71l95IyFZzk-OJtw_h24Ta_xXOX8HfFc5Lr0h7E10HgWUn8SjYEsUqX-DE-8wDxd_khSSl0xYduzoMXZjAb-Ni7G1b1HZLiMo-w2JygaO0BC9QLDchxWFMnAISWOogrSOWkUFCHJf4tu6mcGPyFSwxFYdOCPv9QoHYdGPGDADOcIBXER0VSsVbt3ejcF5wU2BXC9U1y0onmrKXNEnUK0bgnNZY2x4Q0aOtA6Xm4t9VckxtUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ca0d3dd94.mp4?token=SitkDNqvuA8k0vcyauq_FSBtBsZxrGg7BM3c1SnpOb7L0dW3AWFSDGcWV2qDlzSp9vzUEmVhwoTrPeOjDE0Mpa7RrZjswN1b0MHZTh71l95IyFZzk-OJtw_h24Ta_xXOX8HfFc5Lr0h7E10HgWUn8SjYEsUqX-DE-8wDxd_khSSl0xYduzoMXZjAb-Ni7G1b1HZLiMo-w2JygaO0BC9QLDchxWFMnAISWOogrSOWkUFCHJf4tu6mcGPyFSwxFYdOCPv9QoHYdGPGDADOcIBXER0VSsVbt3ejcF5wU2BXC9U1y0onmrKXNEnUK0bgnNZY2x4Q0aOtA6Xm4t9VckxtUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله شب گذشته ج‌ا به اربیل در عراق
علی‌الزیدی نخست‌وزیر عراق با صدور بیانیه‌ای،
این حمله را محکوم کرد.
در این بیانیه آمده که «به آژانس‌های امنیتی
مربوطه در هماهنگی با نیروهای امنیتی منطقه دستور داده شده که همۀ تدابیر لازم برای ممانعت از تکرار حملاتی از این دست، و نیز مقابله با هرکسی که به‌دنبال خدشه‌وارد کردن به امنیت جامعۀ سرفراز عراق باشد را اتخاذ کنند».</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6156" target="_blank">📅 14:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6155">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LlJlo1fvwPJqjaQV99UIArElxsYBLXW4KDv8GSey-rXhCT042FYeFLatBDdZmiHWnCHT34c-rHT0Pyn8uAxkPmfXqjedSc66h7j0yG50VNkGnYfXlretu5n8WbJ6e8vyIs8LI8k-TyyRTTWPHuZht9r5Yn2XtzCi7rQHr7GVRZ_eRlsBFvcvXKSb1E3wxIQ6NR-fYE29xc7FhseGYLnfQD832KxCrWwI0XeqJL7pXq6SRvV_GC4xoR_zGQhxlyTSUFAsXavna8Rd0MJxKtRSNZ35O-K4kFd7Pgv6YOG6nEe8Ub6VX4GQxD5Peq9hnuJVrHWtCkkUVHmZslgOe5Uhvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وراجی نکنید  بگذارید بجنگند که صلح بیارن :)  مثل صلحی که ۴۷ ساله در لبنان  ‌ و غزه آوردن!  انتقاد از خامنه‌ای عین بی‌شعوری است!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6155" target="_blank">📅 12:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6154">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">وراجی نکنید
بگذارید بجنگند که صلح بیارن :)
مثل صلحی که ۴۷ ساله در لبنان
‌ و غزه آوردن!
انتقاد از خامنه‌ای عین بی‌شعوری است!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6154" target="_blank">📅 11:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6152">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1933ad174.mp4?token=ARlzLa20ayC3fcs8vxHrMmqdcPjoaFbz1-ltIsah79vvVyeCnSMGY-c7Mh7x575qFavwvY3B10Xm40_rPHCmP-b-YQ7-KkOL2eSnIiPNc9MZ0JoYN4LGCC-6_jI26rI1oobNUqkzKN0pbZ23r9N4XGXvDgt3l4EK3Yu6G22eoRQZeIdZK8Bmde4v6R4YdQa0KM1TT-MAqxjAudpIGsYgfOh--k7i3c1X6ethHaVhPn5F3Qt4EAtFso616Q-7r45LC__GCZR6m0GgliW-pcZIA7UMrZrU1eJ6MqDVMKbj6wZ1jQctGRK-toaUElGfWvIiIzTKE7honFZXySqByROodxb9pyhJfp65WJ7VGvVrhloGa7hMswy2VhHLDc72AMOUA0Ol1FJMMjqWExVrbp1Wzhdoe2hlDR2Pw2_F-L2R9LuQaAqK80iu0S3QxV80-27ZG1fYpOZuKDtG6Tf8gmU6MVPWhsaZE6Gv9INX5t273K0nefWZeQwuYwoYMxrQZJ9muFTnrrakdfmkSZsNKrXsdvCkQS6nrP4P2THvuL7GgavI2oWDMIOtN_MmilePXSe1zrswkb9foQmtmpltiF67WcaoSI8K02-4BOiEKKj7BWeuhp582rRlnkvJhkdwyQFUleHCWymxh1G6vzRpscTtket0BePYcUSeg5cvQrKSAbI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1933ad174.mp4?token=ARlzLa20ayC3fcs8vxHrMmqdcPjoaFbz1-ltIsah79vvVyeCnSMGY-c7Mh7x575qFavwvY3B10Xm40_rPHCmP-b-YQ7-KkOL2eSnIiPNc9MZ0JoYN4LGCC-6_jI26rI1oobNUqkzKN0pbZ23r9N4XGXvDgt3l4EK3Yu6G22eoRQZeIdZK8Bmde4v6R4YdQa0KM1TT-MAqxjAudpIGsYgfOh--k7i3c1X6ethHaVhPn5F3Qt4EAtFso616Q-7r45LC__GCZR6m0GgliW-pcZIA7UMrZrU1eJ6MqDVMKbj6wZ1jQctGRK-toaUElGfWvIiIzTKE7honFZXySqByROodxb9pyhJfp65WJ7VGvVrhloGa7hMswy2VhHLDc72AMOUA0Ol1FJMMjqWExVrbp1Wzhdoe2hlDR2Pw2_F-L2R9LuQaAqK80iu0S3QxV80-27ZG1fYpOZuKDtG6Tf8gmU6MVPWhsaZE6Gv9INX5t273K0nefWZeQwuYwoYMxrQZJ9muFTnrrakdfmkSZsNKrXsdvCkQS6nrP4P2THvuL7GgavI2oWDMIOtN_MmilePXSe1zrswkb9foQmtmpltiF67WcaoSI8K02-4BOiEKKj7BWeuhp582rRlnkvJhkdwyQFUleHCWymxh1G6vzRpscTtket0BePYcUSeg5cvQrKSAbI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینها اگر نوحه میخونن و مداحی و رجز خوانی و.. برای کودکان غزه و لبنان و میناب و….. از تاسف از دست رفتن زندگی نیست! میخوان در این جنگ بی‌‌‌‌پایانی که با جهان دارند،  از جمله و در صدر این‌جنگها،  با خود مردم ایران جنگ دارند، سربازگیری کنند! تا نیروهاشون بزرگ‌تر…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6152" target="_blank">📅 11:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6151">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">تمدن اسلامی! تا زمانی که توی مدینه و مگه بود قادر به ساخت «توالت» هم نبود!  مستراح هم نداشتن !! اما دنیا در چه وضعی بود؟  ۶۰۰ سال قبل از تولد اسلام!  توی بیشتر شهرهای جهان  داشتن توالت عمومی! اجباری بود!   اینها میشینن روی منبر  میگن «مدینه فاضله»!!  حالا…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6151" target="_blank">📅 10:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6150">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">تمدن مصر باستان رو مطالعه کنید ابتدا تا انتهاش بر مدار مرگ بود! فرعون از زمانی که سر کار می‌ا‌ومد به فکر مقدمات مرگش بود و قبرش بود!  هنر و پزشکی و علم و مهندسی مصر همه بر پایه صنعت مرگ بود!  مومیایی و اهرام و جراحی پزشکی و….. همه برای کار و کسب مرگ بود و…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6150" target="_blank">📅 10:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6149">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q-qV64l_dC64H9CLAM8Qvtx0ex128RvnQqIN1mIH3VhGG1qTClZG8tEovHH5_Mzt2-LY8C2CnlTdSU-d6sO4Sm7tgzQXAhUCaXDibwW-g7zUIKSVCs_4uosr1kf7TKSdSzfb5P9qw4xKvgzioU4xPxZJ6Dz6mkJenmtP88qnsTUdvL-lsAeO3fhHUXWUl5yLItubguQ33zDremvqu4LUjZmJ0kqwSd6n09Y2Rp_8bMJOTrbMSVUALrUAoPCrehxlJpNy8TqDQgX5JYfsbV-qhARvfDi_L9v6WZ3qU82tEzmVe0UXiMgGAR6csujlINRCVvldTtcBWOf31ckfACPxbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها شنیدید جملاتی با این مفهوم رو که زندگی و این حیات «زندان مومنه»!  آرزوی اینها مرگه! مرگ براشون رهایی است!  اینکه برن و برسن به بهشت و به زندگی!!  مرگ رو آرمان خودشون می‌دونن و زندگی و زیبایی‌هاش  رو پست و حقیر معرفی میکنن!  و اینکه باید دائم به فکر مرگ…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6149" target="_blank">📅 10:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6148">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">اینها اگه می‌بینید برای مدرسه میناب و…..  سر و صدا میکنن، فکر نکنید به این خاطره که «اصل زندگی»  رو دوست دارند. و از مرگ متاثر میشن!  تمام هستی اینها :  مبارزه، جنگ، کشتن،  کشته شدن و….. است!  زندگی براشون چیزی نیست جز  «مبارزه  برای عقیده».  و خوشحال میشن…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/6148" target="_blank">📅 10:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6147">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b6d93f0a9.mp4?token=d6V642rHxFhO0E53kqgrpAJKzUoUlT5D4cHx9h_yP4ej5AoURFLf_nAvNorn6NgJGj8MB8ib12bdSBN2DcFUVo7weFbxzWzZna287wZ9ic2_M6NyOCwfvT-TQstNg3f0INRMl8kcJSF51HewBry-E-dK_t_M8NdYC4GwJQnDccWFzlDvGKBFdZqu9IWI_fIPtDH_jNwcgcwGumI2OW0m81ebnmxrZ0hzVHv6Y2v-1EN5xo0nJFHcsmBxzPiI6DQcCFDMr1SxBqy78CVVgBmExBwbLIGJoDBUjtL5-zehAX0MMODplNA1WCKegXrW6l5sFHWamHrUhUMhNXLoi45glw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b6d93f0a9.mp4?token=d6V642rHxFhO0E53kqgrpAJKzUoUlT5D4cHx9h_yP4ej5AoURFLf_nAvNorn6NgJGj8MB8ib12bdSBN2DcFUVo7weFbxzWzZna287wZ9ic2_M6NyOCwfvT-TQstNg3f0INRMl8kcJSF51HewBry-E-dK_t_M8NdYC4GwJQnDccWFzlDvGKBFdZqu9IWI_fIPtDH_jNwcgcwGumI2OW0m81ebnmxrZ0hzVHv6Y2v-1EN5xo0nJFHcsmBxzPiI6DQcCFDMr1SxBqy78CVVgBmExBwbLIGJoDBUjtL5-zehAX0MMODplNA1WCKegXrW6l5sFHWamHrUhUMhNXLoi45glw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6147" target="_blank">📅 10:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6146">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UE84j2HhtqVHWU9eoYiIKhTrmHHABMyJkmDxn1fc9RHZIPFgeiBxoVlwJRhEVB0p7J8i4V0gHOUrGym1X_QCVFSJTfK-cA9GZPcZTWeVfpnuvzRpsnmNPyIYzkz9AdbTbSVT9UVj4DB7MTr0znd5O1J1OgTVvZTjo5kGjfqNX4qpS2gCWKf8FNRDWTvseLqsAa5t1O6a9iQqklNrU37gV3Ce06rsrhTFE8W3CjzI5rTmarJEbx35ewvdF4UmEOrxZuTJn18xcxyeS143Iq_GI_QcIYoUthFnTrDDuPQNvZ_YXY6TwQaxqtSCQ74FwPtpZLk0MFv_gUu_5SDhoyRAvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: ایران به یک شهروند زن آمریکایی که در دسامبر ۲۰۲۴ در دوران رئیس‌جمهوری جو بایدنِ خواب‌آلود به‌ناحق بازداشت شده بود، اجازه خروج از کشور داده است. او اکنون در سلامت کامل در خارج از ایران است. ایالات متحده آمریکا از این ژست حسن‌نیت ایران قدردانی می‌کند.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6146" target="_blank">📅 09:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6145">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6145" target="_blank">📅 09:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6144">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">استاندار مرکزی : شب گذشته به دو نظقه در اطراف شهر خنداب حمله شد.
این برای چندمین بار است که اطراف شهر خنداب مورد حمله قرار می‌گیرد.
نه آمریکا دقیقا مشخص میکند چه اهدافی را زده و نه ج‌ا می‌گوید به کجاهاش خورده.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6144" target="_blank">📅 08:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6143">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">اطلاعیه  ارتش:  سامانه‌های راداری، سامانه پدافندی پاتریوت و مخازن سوخت آمریکا در پایگاه علی‌السالم کویت را هدف قرار دادیم.
‏ رادار‌های سوپر هاوک، تأسیسات و سامانه‌های پاتریوت واشنگتن در پایگاه شیخ عیسی بحرین نیز طی حملاتی، آسیب‌های جدی دید.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6143" target="_blank">📅 08:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6142">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
استاندار سمنان : به بخش‌هایی از فرودگاه سمنان حمله شده، کسی کشته یا زخمی نشده.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6142" target="_blank">📅 08:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6141">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXLWQokM5H7tmOhpFGTrGe0YoT0kSjDdLz44G6qF_EmZpw2s1uknuRcYyvoHkgsOMbwXifNJp3JrM4ze5kdh-TozRYg_0pI7m6WUb8v9MrZ_i2gTDJMhoRv2miu6sBKWO0LSok-GWle_VCj7cxYLPcQfUlAiMWFGYd1GOJ5SpvI8FQxkMbIcxb-akZIYJHNPk8WSA2DHJM6v5dHQdNDWY96VtHD6CbN4ENrao_GtsTndPQ9elJReWdeqmXzK6onsAIQWLP0BFAGI4VYa3yVbnbcEFQbKNkBs1AxiJViVpk3gQqr_3Ns85_eItzW49OLYq6BsYr00EVAtbBUkayCAnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین یارو خودش از دست سپاه و نهادهای زیر نظر خامنه‌ای  فرار کرده و به آمریکا پناه برده!
و آمریکا رو خونه امنی پیدا کرد برای زندگی و نوشتن از اینکه اسلام چقدر زیباست و خوبه و سعادت انسان رو میخواد!
حالا از همونجا به ج‌ا میگه مبارزه کن با آمریکا! مطلقا تسلیم نشید! تا انتهاش برید!</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6141" target="_blank">📅 08:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6140">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">برخی گزارش‌ها از تداوم حملات به اهواز خبر می‌دهند و اینکه تاکنون ‌۹  انفجار  مهیب در شهر شنیده شده.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6140" target="_blank">📅 23:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6139">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
چندین انفجار مهیب در چابهار و بندرعباس
🚨
کویت : امروز ۲۱ پهپاد و ۴ موشک شلیک شده از سوی ج‌ا را منهدم کردیم.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6139" target="_blank">📅 22:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6138">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای ۲ یا ۳ انفجار در اهواز</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6138" target="_blank">📅 22:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6137">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RorTg30p8F9CgMDXfmFekAJdGW5t19AVP5F6YgfKUtpDWilXfHjPGJc8i8sIEqwHvW30F4oI28Jc40UO55TVX4UGdRoKi-r4oy5vTGZscWVjXakhbAsUN4xRDNjxOhNS5HW1ywsRfX827ysB4DXINzgn9ExR6iwLUQsxNeP8XiIlw4MCiSNvZ5JEphQE1lLVQjhfEM54Hy7N7wfC6gFSuRQTBHkOdYGdhHrru8_EYxYZUiXKOrq-4yEzEpqk-8MKZXDvIK-InoJDi69tt4e4wb2t0hqtYhsxJi1OtxT-kzE5mZoaQUkR2fkCznEz6gYyoFi3dtcPHfhoz4qdd51waw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شما دیگه جرات حمله به اسرائیل
رو ندارید! خودتون هم خوب می‌دونید!
این ۴-۵ روز هم به همه جا حمله کردید
به جز به اون کشوری که بیت‌رهبری
رو زد نابود کرد!
و نشون داد دقیقا کجاست که سست‌تر از لانه عنکبوته!
ولی هر چقدر دوست دارید شعار بدید!
اون حزب‌الله تروریست هم رفت انتقام بگیره  هنوز و همین امروز هم نیم میلیون نفرشون  توی محله‌های مسیحی و سنی لبنان آواره شدن!</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6137" target="_blank">📅 20:39 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6136">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">آنچه شب گذشته در بمپور رخ داد و موجب  کشته شدن تعدادی ای نیروهای ارتشی شد، قابل اجتناب بود.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6136" target="_blank">📅 20:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6135">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20e615d142.mp4?token=SmUuo5fFnMN8srKFHTNzWkpqeod7ByEMR78OFmuH7aO9vsa1Dz0jYT4MH3MWsoGIZSk2ogE38chxdQLP4cVDIPRSsG9s1hG9dfIL8TVl-7zh5SxBIjQODQBC13qot43uUcYaShYT5A6Nb4YqbDZ4PZ7ByEYqVym2mJ4grdmQpUbUWZha5iN-1-7RGWXdkSfTD6RyV670IuJz_AQh9XOTT1LuEKKxTARU9PM-fjaFDH3GGcvgabhaiKqxfat8s2U0WTP6FyHQZabrxs5EcVplliX9Xrsr1NnHG0GfM8X9Y7T168Zrrf0KOZMnswMDj6kxZAUdJ4MF05BRvF_23kn_vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20e615d142.mp4?token=SmUuo5fFnMN8srKFHTNzWkpqeod7ByEMR78OFmuH7aO9vsa1Dz0jYT4MH3MWsoGIZSk2ogE38chxdQLP4cVDIPRSsG9s1hG9dfIL8TVl-7zh5SxBIjQODQBC13qot43uUcYaShYT5A6Nb4YqbDZ4PZ7ByEYqVym2mJ4grdmQpUbUWZha5iN-1-7RGWXdkSfTD6RyV670IuJz_AQh9XOTT1LuEKKxTARU9PM-fjaFDH3GGcvgabhaiKqxfat8s2U0WTP6FyHQZabrxs5EcVplliX9Xrsr1NnHG0GfM8X9Y7T168Zrrf0KOZMnswMDj6kxZAUdJ4MF05BRvF_23kn_vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیش بینی تاریخی بختیار
در دو کلمه، برای مردم ایران</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6135" target="_blank">📅 20:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6134">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/296fa239b5.mp4?token=RhctMj27VYGNO3alohY03GpqQNIlgoTjMDZvKDqiXCXMmfRtqxEN6OBMzfu83cj6mWK7lRjLMH38KIH4Mu2mj32VdVAtQbz-eg2Ys2yPdr96_Mxs2ZTtHFAI1xl8NiRipeJAk-UM3zItFbFoyGpi8l6u8sGRfOQ9COZe06_-CiWYffSdNBbxp8D8kjZq68lxLuvTXvrbws8pyJel-tM-NeIqu_z86M490XQvyju9WyHbDfSZhdt2u0Oo9qSJ86Sl2BxxKiJ9x3txN3wbGIU136JrFQg_nhlZAfmCF0nE6ALj947UR9EcAdyaMJrIfShlDbprMShJu-i_2NMRzobJUoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/296fa239b5.mp4?token=RhctMj27VYGNO3alohY03GpqQNIlgoTjMDZvKDqiXCXMmfRtqxEN6OBMzfu83cj6mWK7lRjLMH38KIH4Mu2mj32VdVAtQbz-eg2Ys2yPdr96_Mxs2ZTtHFAI1xl8NiRipeJAk-UM3zItFbFoyGpi8l6u8sGRfOQ9COZe06_-CiWYffSdNBbxp8D8kjZq68lxLuvTXvrbws8pyJel-tM-NeIqu_z86M490XQvyju9WyHbDfSZhdt2u0Oo9qSJ86Sl2BxxKiJ9x3txN3wbGIU136JrFQg_nhlZAfmCF0nE6ALj947UR9EcAdyaMJrIfShlDbprMShJu-i_2NMRzobJUoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی که فرمانده سپاه بود و سالها فرماندهی جنگ رو بر عهده داشت
اینجا میگه مطئنم که مسیری که در ذهن مجتبی خامنه‌ای است، بهتر از مسیری بود که شورای عالی امنیت ملی رفت.
مجری ازش می‌پرسه خب اون چه مسیری بود؟
میگه : نمی‌دونم ! نمی‌تونم که ذهن خوانی‌ کنم!
فقط می‌دونه خوب بود :) یه مشت چاپلوس !</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6134" target="_blank">📅 16:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6133">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVahid Online وحید آنلاین</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ju91qPoZHrx7iX47jLZ-RZQ8pAdR06E6xStnmQ__Iu4PwmBU4r7nluwUfGUW03N6_FyMvOkreDRictmmqcVxN-zg2RpI_SuMvr4DnUvFKoH9d84QMnx1rv7KkdwK0R4pw8I4LnzYyMbllLOunWz3jWjCuIa6AnZvrPCohy1EqzzSzXSU99_hy523gjkSNd-ZqlldMIxWsBbrXDOBZ1c7JcXBa5RO_Lw39zA7xwxqxNU9OQdkpEwnuPN804Jc3EyzMZbnwiUTpskEe52g9w8A_IkIOX0M0u5FYNJ-4rB_i7V6GoHqOms2t1GlXflTX1RMQ5Q-SUOhYgeLytyxZBjlAg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
سنتکام : به تنب بزرگ حمله کردیم.
در جریان این موج ۹۰ دقیقه‌ای از حملات، با استفاده از مهمات هدایت‌شونده دقیق، سامانه‌های دفاع ساحلی و محل‌های ذخیره‌سازی و پرتاب موشک‌های کروز در جزیره تنب بزرگ را مورد حمله قرار داد.
این حملات توانایی ایران برای حمله به کشتی‌های تجاری در تنگه هرمز را بیش از پیش تضعیف کرد.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6132" target="_blank">📅 15:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6131">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">حمله امروز به چابهار</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6131" target="_blank">📅 14:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6130">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
ارتش: «آمریکا بامداد امروز با شلیک ۱۳ فروند موشک، آسایشگاه و محل اسکان یکی از پادگان‌های نیروی زمینی ارتش در بمپور را هدف قرار داد
دشمن به مهمانسرا و اماکن نگهبانی پادگان حمله کرد
‏ ۷ تن از کارکنان پایور و وظیفه تیپ ۳۸۸ ایرانشهر شهید و تعدادی مجروح شدند.»
‏</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6130" target="_blank">📅 14:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6129">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
سنتکام : از نیم ساعت پیش موج تازه‌ای از حملات را آغاز کرده‌ایم.
(از  ساعت ۱۳:۳۰ تهران)</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6129" target="_blank">📅 14:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6128">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jgm3FHumJcN37i__fY2HtsrxDUWp8iy8Ty-_4740NRhN4M53OsZwXt833cU4ubt1Rl3cekP5E8hXwkZTxKRxkT-3nx6yAAPKz9dq3o56RYRHpY85foDS_gFifwYTz9W9PUZ_TpQ3OT0XqI230afE6OQYsjZdnx5EreYhbk3T_6zrDBNOBJsy1G0zB8HbM_N4XCwLivvURi09taYgfQ7qLVn8vde4tEkGn3n0pRW5uu7SWWlUaNRgCT_jgH8GhaATK_N_u-GRE4GgayEvPrwsYfoWCR3ngpqudxm7gpc5BlF0BpLqmIjPshI5ayjoGiG6KzRgBJtZfE3nOl2nwW-96w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قابل توجه ساختاری‌های محترم
مدیر حوزه‌های علمیه با بیان اینکه مسئولان باید تفاهم‌نامه‌ها را پایان‌یافته تلقی کنند، از دولت و شورای عالی امنیت ملی خواست به دلیل بدعهدی طرف مقابل، مسیر مذاکرات را متوقف کنند.
مشکلات اقتصادی یا ترس از آسیب به زیرساخت‌ها نباید موجب واهمه مسئولان و رویگردانی از مسیر «جهاد و استقامت» شود.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6128" target="_blank">📅 13:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6127">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd0a98053a.mp4?token=h3zb6Rxx6E3jdHpwX-847M5vrov06i2F46Ww2Bo0wzKJyIKZkxg7x6Yndqcseu_T379jmt8qQEYz68UXzcbK1oCx424XXzHs0a7ZfTFWLqXct-ewrqcxbxlu0cyFdRKGcIa9Ar0kb6vtXtjsl9jKdec_yS2RbDBP_zX0iUAxl9zJvR94nnHuvyJth-x8e-0rejOyAdkOV53fb5TwqMT88WjN3-jfnSxHH9SEelNPtsrD8_H_dhtr4OeWKTc6l-bQXiNbr7GXstgAWsyGmDw8hrlgrYHzl8k16zJgnKfbYqscWY_saN7-H60orfNEz2a9zqGpVpYa4JfQDIUDAPClYASefxP4WVRvdgB4GzlDLMJpjazfLhgFtUhDIL325JNS0lSr3DKHOefdOjTaoYUXXgwAVzMrsjMhklrMe95P8tsKxfMvYsuk76GDILJsYrVW4f7y5aKnQHhx7thXMRKT0Zf82ghtd-Aa4ZbvnPTY5SIb-luG9xOPZK6mCWpuA63-KqTFyJRWZ6pIes3XzTbS2YS7b9rCWU4wnoLR_yMSrbFrb4wJfuD7_Da6T4LMbp6sq6aUMWR8inFD4B57J_O0rZUDsDHPfZb5xjwoGisMWmuhT1jzv9SIGH0J7-4BZmiAvIn5_qu_OeqM8dfLCsA5IKO2w4oaz95xm4BWzesIKZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd0a98053a.mp4?token=h3zb6Rxx6E3jdHpwX-847M5vrov06i2F46Ww2Bo0wzKJyIKZkxg7x6Yndqcseu_T379jmt8qQEYz68UXzcbK1oCx424XXzHs0a7ZfTFWLqXct-ewrqcxbxlu0cyFdRKGcIa9Ar0kb6vtXtjsl9jKdec_yS2RbDBP_zX0iUAxl9zJvR94nnHuvyJth-x8e-0rejOyAdkOV53fb5TwqMT88WjN3-jfnSxHH9SEelNPtsrD8_H_dhtr4OeWKTc6l-bQXiNbr7GXstgAWsyGmDw8hrlgrYHzl8k16zJgnKfbYqscWY_saN7-H60orfNEz2a9zqGpVpYa4JfQDIUDAPClYASefxP4WVRvdgB4GzlDLMJpjazfLhgFtUhDIL325JNS0lSr3DKHOefdOjTaoYUXXgwAVzMrsjMhklrMe95P8tsKxfMvYsuk76GDILJsYrVW4f7y5aKnQHhx7thXMRKT0Zf82ghtd-Aa4ZbvnPTY5SIb-luG9xOPZK6mCWpuA63-KqTFyJRWZ6pIes3XzTbS2YS7b9rCWU4wnoLR_yMSrbFrb4wJfuD7_Da6T4LMbp6sq6aUMWR8inFD4B57J_O0rZUDsDHPfZb5xjwoGisMWmuhT1jzv9SIGH0J7-4BZmiAvIn5_qu_OeqM8dfLCsA5IKO2w4oaz95xm4BWzesIKZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سفیر اسبق جمهوری اسلامی در روسیه: مطمئن باشید اگر ترامپ را بکشیم نه تنها هیچ موشکی به سمت ما شلیک نخواهد شد، بلکه عقلای آمریکا با خوشحالی جنگ را تمام خواهند کرد.
کشتن ترامپ هیچ هزینه‌ای برای ما ندارد و با کشتن او جنگ هم تمام خواهد شد.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6127" target="_blank">📅 11:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6126">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">جلسه اتاق وضعیت برای بررسی حملات گسترده‌تر آمریکا علیه ایران؛ آیا ترامپ آماده تشدید جنگ است؟  به گزارش اکسیوس، دونالد ترامپ، رئیس‌جمهوری آمریکا روز سه‌شنبه برای گفتگو درباره عملیات تهاجمی گسترده علیه ایران جلسه‌ای را با حضور مشاوران ارشد خود در اتاق وضعیت…</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6126" target="_blank">📅 08:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6125">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S5wHd1QHaqIvLtFEXkqDEz8IKnYzvuI5eOGpiYsJzXyWwHo--I6GaIyUr4svWnHRrauVlI0drdnbgQPzp388G9XvZduFG7tTb7ysFFMzVUhHWnGSue4Q-oNi4y9HIwKyRBJhnRFI5PKGFLgdPp63b3c1-VeVTeiKxEbWSZQpzVSHv7g5EnR_WP7icgn8fQXsfs6p_jdovEoz1ZfsAe22bYUvt2vx1h5I0PthAy36lIOu1U-V-PtNxICnb0FIsvk5a6acKGZywSXcaPGEm8mYa7VJzC7MbOPWbewQZWMksIwQjwsvXRpq1MKDr1jcn5rLHIPN03sBh0afejQ7b7DFiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلسه اتاق وضعیت برای بررسی حملات گسترده‌تر آمریکا علیه ایران؛ آیا ترامپ آماده تشدید جنگ است؟
به گزارش اکسیوس، دونالد ترامپ، رئیس‌جمهوری آمریکا روز سه‌شنبه برای گفتگو درباره عملیات تهاجمی گسترده علیه ایران جلسه‌ای را با حضور مشاوران ارشد خود در اتاق وضعیت کاخ سفید برگزار کرد.
به گفته سه منبع آگاه، در ابن جلسه که ارشد‌ترین مقامات نظامی و امنیتی آمریکا در آن حضور داشتند در خصوص گسترش حملات صحبت شد.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6125" target="_blank">📅 08:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6124">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bd4825a45.mp4?token=ftzrVPCGUjms8upJYiWhbV53NCWlmh2E6IG6fZ_NW_OHHTjKLiKddKaFZS99j6g-r_GeKAOdaFpUjuNia7HtL-_vsGMTnC4_4RaFub23HtHQdJP_nbsR6JLDoJPdY8zQOZGfPjBflU3MR87JAZQm_z3Fn3ctAO2E5FGjNGkpnYvTYmApLoFQ1JK8BV9TT8lj_eBpMukV9vciPrvbI-3ukFeDj2_KtzErZaI6mqchhW0qTtEB_-2ykwLKpGpe-w_nobY5GrhEerDGWtt3o-90mStvZXNdBy9ibX2QxfuFa5y4AxTqAK_1uynFRLBquSUUrNtfiQSxM1-rTGOhFV7AlXf29YX6W9wrUARoD1EBcMuEkSftl5yhnql6IZlwE7tLxR_9lTsowZ6Hq4o5OijqaitspYiF6Q8Nk4PzTtkzZIPOOdh-IAQqt-EJ5oQESTSA23-Ead3kAlQ_m7dwWu_P0msQzXqDYK7IZ4UR9UjBXoFHUOLbQ5MlfE2ZZSkQlqHKPFVrqM6g-iywqTBEcpdl7qvkXA2v21KGtfs_XRL-KxtBZR7l3hmzoPR_s8-M6GZZ0ChYTPrUbCcWizL8H7z11my-Sd4BN7xT7daccYhyVDwQ7ERpVziiX2uQsdPuk6yKJ9GmForm7jlxhw4ZD1S0HUqtNrSIWm-eS6dTOaWIjdM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bd4825a45.mp4?token=ftzrVPCGUjms8upJYiWhbV53NCWlmh2E6IG6fZ_NW_OHHTjKLiKddKaFZS99j6g-r_GeKAOdaFpUjuNia7HtL-_vsGMTnC4_4RaFub23HtHQdJP_nbsR6JLDoJPdY8zQOZGfPjBflU3MR87JAZQm_z3Fn3ctAO2E5FGjNGkpnYvTYmApLoFQ1JK8BV9TT8lj_eBpMukV9vciPrvbI-3ukFeDj2_KtzErZaI6mqchhW0qTtEB_-2ykwLKpGpe-w_nobY5GrhEerDGWtt3o-90mStvZXNdBy9ibX2QxfuFa5y4AxTqAK_1uynFRLBquSUUrNtfiQSxM1-rTGOhFV7AlXf29YX6W9wrUARoD1EBcMuEkSftl5yhnql6IZlwE7tLxR_9lTsowZ6Hq4o5OijqaitspYiF6Q8Nk4PzTtkzZIPOOdh-IAQqt-EJ5oQESTSA23-Ead3kAlQ_m7dwWu_P0msQzXqDYK7IZ4UR9UjBXoFHUOLbQ5MlfE2ZZSkQlqHKPFVrqM6g-iywqTBEcpdl7qvkXA2v21KGtfs_XRL-KxtBZR7l3hmzoPR_s8-M6GZZ0ChYTPrUbCcWizL8H7z11my-Sd4BN7xT7daccYhyVDwQ7ERpVziiX2uQsdPuk6yKJ9GmForm7jlxhw4ZD1S0HUqtNrSIWm-eS6dTOaWIjdM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0378588a4a.mp4?token=L7a9EAg4exW9YQFb3phZtHCKBO_HPs66FKLsUTifgUvoOsyyev56BFqK2rBjtVaUa-BAIDaxiPh73-l8G-FEoFPdtQs-i6xhjIRS8bThKflOB4PnzMnCQlRBipDJYjW_MOyc6bkHmemrK0Q354IggiM3V7wys30R9Fp9EKPptHhxV52RiponNCrceGu5Zq30gWSVr3NMzaJBxiw1BMaBa6QCC26PPH54X8uP1L4S5JXRr4AtaW7SV-0RSBl1HG4W76KXnCvriWtlWkE2CJxzGd6gz4Uw3CPZ3fOMUMcL-DlfWWlnwWFvpZODAnzu-JoFO8XMJN-SYdT4q7wJH-A4Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0378588a4a.mp4?token=L7a9EAg4exW9YQFb3phZtHCKBO_HPs66FKLsUTifgUvoOsyyev56BFqK2rBjtVaUa-BAIDaxiPh73-l8G-FEoFPdtQs-i6xhjIRS8bThKflOB4PnzMnCQlRBipDJYjW_MOyc6bkHmemrK0Q354IggiM3V7wys30R9Fp9EKPptHhxV52RiponNCrceGu5Zq30gWSVr3NMzaJBxiw1BMaBa6QCC26PPH54X8uP1L4S5JXRr4AtaW7SV-0RSBl1HG4W76KXnCvriWtlWkE2CJxzGd6gz4Uw3CPZ3fOMUMcL-DlfWWlnwWFvpZODAnzu-JoFO8XMJN-SYdT4q7wJH-A4Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه محلی «حال وش» از حمله به آسایشگاه سربازان در شهر «بمپور » در استان سیستان و بلوچستان خبر می‌دهد و کشته شدن ۱۰ سرباز و زخمی شدن ۱۵ سرباز</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6123" target="_blank">📅 07:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6122">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5b6a441ee.mp4?token=gb8J2SpU-zmevuSjRtGimkIvXVFjqXCfofwup8-XaYVfJAm5SqPHE2s37mktGnW-A7oxi-JpJEzxcGMALm_TLpebWaHMCpNT8saZRaXeYDc49gm7tna4620gcbCwGxS1hI1yID5MzpAPFsyPoWs62gqXhJiby0UXxgHtKSZP1iBg7qo-NvzAkUmQeYbURTTp1HruWnVRVveW6RQGyCTMUkw8qBghTR3ctqeBmTOklSnpc0A0v72BZnXDP7v0tG9aMYUvWSzt432CS5FbWR4JluMXrg0UK4Na10JMGk2JWTc0vfWqHqx_FAOc9aY1G9oA6zxBI_mtIOc_vucdmJbv5151HoizZWu8sCvgKEfJ45xgFZrOF4XLxgleUwgRilOevDMtkfUezKb7TmR9JscvBR_mk_YFApc7hxeeq_4TM5FMr4uKW_LKMXw8_cHTM1yUIn4VaaD2FsQki0EBHv3L3b_DUsanD81XM-MkFBCEdm6F1Hy-Kb50gCTt2CreiyWuvOXR4v12-0O5XX0rGIj3HnwW5RONK1GToEx7QyGUKE4LooceqdAxvd8RB6JOGEOBGFY8B4uuFQamzGZxZQWFEv2FJgIHabX2QN7eiIj3S1VHoaSzPyE2Z7VbMoNXQz4dWPPmuiu1DJeaFtyULi9qiRXdXySl_WaPpND3rD6QJhY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5b6a441ee.mp4?token=gb8J2SpU-zmevuSjRtGimkIvXVFjqXCfofwup8-XaYVfJAm5SqPHE2s37mktGnW-A7oxi-JpJEzxcGMALm_TLpebWaHMCpNT8saZRaXeYDc49gm7tna4620gcbCwGxS1hI1yID5MzpAPFsyPoWs62gqXhJiby0UXxgHtKSZP1iBg7qo-NvzAkUmQeYbURTTp1HruWnVRVveW6RQGyCTMUkw8qBghTR3ctqeBmTOklSnpc0A0v72BZnXDP7v0tG9aMYUvWSzt432CS5FbWR4JluMXrg0UK4Na10JMGk2JWTc0vfWqHqx_FAOc9aY1G9oA6zxBI_mtIOc_vucdmJbv5151HoizZWu8sCvgKEfJ45xgFZrOF4XLxgleUwgRilOevDMtkfUezKb7TmR9JscvBR_mk_YFApc7hxeeq_4TM5FMr4uKW_LKMXw8_cHTM1yUIn4VaaD2FsQki0EBHv3L3b_DUsanD81XM-MkFBCEdm6F1Hy-Kb50gCTt2CreiyWuvOXR4v12-0O5XX0rGIj3HnwW5RONK1GToEx7QyGUKE4LooceqdAxvd8RB6JOGEOBGFY8B4uuFQamzGZxZQWFEv2FJgIHabX2QN7eiIj3S1VHoaSzPyE2Z7VbMoNXQz4dWPPmuiu1DJeaFtyULi9qiRXdXySl_WaPpND3rD6QJhY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا میبینم راست میگه …</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6122" target="_blank">📅 07:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6121">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a2NTb-4z-yr-ilHM57A8J_csoYQuhCzcrIQPWCILdn3fj4pv55BFUFOCUNrG8radeNBSu7M4QtEwqZmLpJE-xalf82jU3xlhX9u1N_q2OyCjP9huuHDR8mb-sAlvdPH7p_uyA0HLjM_miz0maUHKsWVwwPRXRxtyOdT52uCsJNLh7rVWvu-L-2OvVokzIT3Axdpkvwuj8pONYkKclvzHZ7P3gCrbdF1ThCn3MnLjqAA74qDcxnJdg-c56jQ80ZOZ8psu_8JPWqOYJuMgc_t4ik2sAzPvNu2uXOcGJ2AgPdxOm3_wKgMZDrekP1Xe4X9sNHXqFp5gujUAqd_j5ayhYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6121" target="_blank">📅 06:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6120">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LuW8xw0lZQdYdoFX1U1SYiwj_Jpq79serFIesxxcSvg6OBxf6_IirieOcskuxm7zYX8WUz_hqVY4eGf_tw7CqrziAj7X4sRj0gq1rbxX3bQYSYjIAp_gwcTD-wR5o3Ru4x3MD5H9_zn79IharwTptLPd7nW6snql3yjkokOWIkyMufdrbl7FuPFL4rLPaYHh5ZkqnK4IQTQyvzz5yjvmc_4GLSFdqxvFNAr76PbARQEfCXQ6I16w71rFU9vYTEv97u3EE0ddon6AFTVWL1-NsvbjIig78Yn3nv5xMPimntvm_fbHO2tN_8eHKxx1e2yrcUpEWza0LzVi4f9-Sechfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه محلی «حال وش» از حمله به آسایشگاه سربازان در شهر «بمپور » در استان سیستان و بلوچستان خبر می‌دهد و کشته شدن ۱۰ سرباز و زخمی شدن ۱۵ سرباز</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6120" target="_blank">📅 06:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6119">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba02e5e863.mp4?token=Gz_Dj1R8rx9u378bY33Xz1HNZlOMHJ8fJUFVqkYhD5Ac_WJFLXtPPIfdY2Fk71rKtlvVKzKhgeK8BYrOluouaVxpaBNELEU2Y0pt5QecVOj6PleVJ_gEJ1hx_IfoI7vxoFzSHoUnWz8yimFciq6Nyw5VusQVbNVIMh6pRAeQ-6f77PPWBiOI6U49vv5exho6WuzfLyy54yT45WASe3krNUke0qWe-2h1YLWNtFRQjxzr2rqujc-dG6K5zbMvx6MLUIsDlXNN9N1hPALc0Bj6WieOM5gZFCigixpTThG7gW3gRxL0H8Xy2kFU0-6imOCbwLiSAIpvNt2md_mWjIimvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba02e5e863.mp4?token=Gz_Dj1R8rx9u378bY33Xz1HNZlOMHJ8fJUFVqkYhD5Ac_WJFLXtPPIfdY2Fk71rKtlvVKzKhgeK8BYrOluouaVxpaBNELEU2Y0pt5QecVOj6PleVJ_gEJ1hx_IfoI7vxoFzSHoUnWz8yimFciq6Nyw5VusQVbNVIMh6pRAeQ-6f77PPWBiOI6U49vv5exho6WuzfLyy54yT45WASe3krNUke0qWe-2h1YLWNtFRQjxzr2rqujc-dG6K5zbMvx6MLUIsDlXNN9N1hPALc0Bj6WieOM5gZFCigixpTThG7gW3gRxL0H8Xy2kFU0-6imOCbwLiSAIpvNt2md_mWjIimvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام فیلمی از حملات خود به ایران منتشر کرد.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6119" target="_blank">📅 06:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6118">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b9746249d.mp4?token=UQ7VXg3Ij8UbHZNPAFOifF8KdQqRFfLcLVYJB0zqdaG23oblwe9h9Ou-_LwubRSfZFcgwKTbeocIiGMP9xJ1RBvEJtgCVMcnQQz9Fv9FLFAHyxE03EAMTYcIxw3PBljBzseE9zEYd_QEL4LKVeL_LkUSp1fWy20h1dsVcjMvFLeWRK9b_dfObDb1Exj_JQUJduvbPX3ZWgGyIP-WXWhX8CfHYRZHbM1WqHu45lEKFif_M8-h-E0c0kfILbgQMV3YQHfKMl62DcMlxrB6apR8wTzi8zEwj0lw7ZFXpK-oDlQ6Xbi_sk0pGi8N4Cp5U4cyCHbks2_c4HBr9yunjxXQuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b9746249d.mp4?token=UQ7VXg3Ij8UbHZNPAFOifF8KdQqRFfLcLVYJB0zqdaG23oblwe9h9Ou-_LwubRSfZFcgwKTbeocIiGMP9xJ1RBvEJtgCVMcnQQz9Fv9FLFAHyxE03EAMTYcIxw3PBljBzseE9zEYd_QEL4LKVeL_LkUSp1fWy20h1dsVcjMvFLeWRK9b_dfObDb1Exj_JQUJduvbPX3ZWgGyIP-WXWhX8CfHYRZHbM1WqHu45lEKFif_M8-h-E0c0kfILbgQMV3YQHfKMl62DcMlxrB6apR8wTzi8zEwj0lw7ZFXpK-oDlQ6Xbi_sk0pGi8N4Cp5U4cyCHbks2_c4HBr9yunjxXQuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : امشب، فردا و فرداشب به سختی به آنها ضربه خواهیم زد و هفته آینده پل‌ها و نیروگاه‌ها را هدف قرار خواهیم داد، مگر آنکه  مذاکره کنند.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6118" target="_blank">📅 06:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6117">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caeb092620.mp4?token=UvZXbRanqO-9x87Pvb0n1T_uY-1TiPAu6plJXUqWQsefVVgdF0mj23kl2FI0CY_b60Q0LXAduQSN0eL1mkyz4hcUlYT05qhvM81ahgsrSZY0nNPnXf2987jQu46H3HAwGPbRZhG2EIFiBoLORyLIFGODW5Kmt9g6DieItmqaiiRtkuO4J66hVClfd54-XGpx21s-Dc5IyQYzT9naw-O-FwE8toqxrmw7OHOKIlqyGf453LV9RqJAXNjlwGd64AHekxEw_z-inbcdamJ5dLgb8_-B9zYugEQ61Mzi8UvROiiNanAIgsBDh7RabNLNQ2Jn8xSPT3oOBHuZL_g23kU_Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caeb092620.mp4?token=UvZXbRanqO-9x87Pvb0n1T_uY-1TiPAu6plJXUqWQsefVVgdF0mj23kl2FI0CY_b60Q0LXAduQSN0eL1mkyz4hcUlYT05qhvM81ahgsrSZY0nNPnXf2987jQu46H3HAwGPbRZhG2EIFiBoLORyLIFGODW5Kmt9g6DieItmqaiiRtkuO4J66hVClfd54-XGpx21s-Dc5IyQYzT9naw-O-FwE8toqxrmw7OHOKIlqyGf453LV9RqJAXNjlwGd64AHekxEw_z-inbcdamJ5dLgb8_-B9zYugEQ61Mzi8UvROiiNanAIgsBDh7RabNLNQ2Jn8xSPT3oOBHuZL_g23kU_Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار ناشی از حمله پهپادی امشب سپاه به کویت
گفته می‌شود مخازن سوخت ارتش آمریکاست.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6117" target="_blank">📅 06:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6116">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/360d24e506.mp4?token=WC13Q3c0DA5ich1befKtww-5hTNwigrYgX8n3TRgiKwWdEizq1Cj811WTrDipZrNo9cDtU4ofCUo-QueFtstP94MAUkbnN3rM5M5q8P8JcYvQYqjpXg8p86aYT6j06Ww-6k7VaJgrR-o-pw0WCsojyOxoGvkKspwlYdgdTIEmDZt1ap1xtcIKKF4sNkAPqGtaIZIOYU4JIZtNkY7L2Gw60CjETOZhnUmzuCo97xfPmahlDhsmRS6nK-mWCr2GDdm2w5LcXGaCgzxUS5u8mCtkAGH3HCTekVfER3GtEkcwK9u11cyYb-F_WKNLExmbJ-DNM8QP-01zHa6TEMee3vqGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/360d24e506.mp4?token=WC13Q3c0DA5ich1befKtww-5hTNwigrYgX8n3TRgiKwWdEizq1Cj811WTrDipZrNo9cDtU4ofCUo-QueFtstP94MAUkbnN3rM5M5q8P8JcYvQYqjpXg8p86aYT6j06Ww-6k7VaJgrR-o-pw0WCsojyOxoGvkKspwlYdgdTIEmDZt1ap1xtcIKKF4sNkAPqGtaIZIOYU4JIZtNkY7L2Gw60CjETOZhnUmzuCo97xfPmahlDhsmRS6nK-mWCr2GDdm2w5LcXGaCgzxUS5u8mCtkAGH3HCTekVfER3GtEkcwK9u11cyYb-F_WKNLExmbJ-DNM8QP-01zHa6TEMee3vqGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی با موشک‌های حاوی بمب‌های خوشه‌ای به بحرین حمله کرد.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6116" target="_blank">📅 01:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6115">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
ارتش : به پایگاه‌ها اف ۱۸ های آمریکا در اردن حمله پهپادی انجام دادیم.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6115" target="_blank">📅 01:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6114">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">‏امشب اتفاق جالبی افتاده، به محض اینکه خبر انفجاری در شهر و استانی منتشر میشه، مسئولان جمهوری اسلامی سریعا مصاحبه میکنن و میگن دروغه و همه چی آرومه!
‏اینطوری مثلا میخوان صورت مسئله رو پاک کنن.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6114" target="_blank">📅 01:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6113">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jID_ZqMbJuLSYPnmMgiQfQUz1BW8LeR8xer41POsYxRm7Iqe_3LxWGrO9IXhjfuy_8w2DzqwYUWm9-iuU38wIqLGV9vcrnRQqdtXPC5U7afRjwgEnmxHkFd4grGZagEkiFB-zWmufHmJo4VSmlZQoY74X_sQI0n7iP_r6cL58XTqwdnDm1lxVNk0v-KyRyNNZNa6CncZzZ1NvyPa79l0zjAAIpp0W5yfhTuJ2nUFg-MXAT_CVZWpDxmIxQnTRGQZnIMYD8_9c9SJLL33CFY-opcHgGXLX5RBPpp319ErFLoEBjZ68Eneql-zpsaC46Uk9XdlqABAAuY_wB1pxovlPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگارهاشون می‌نوشتن که کشتی‌ها دارند  از مسیر عمان رد می‌شوند، تشییع جنازه،  بریم و کاری کنیم که  کشتی‌ها مجبور بشن از آبهای ایران رد بشن  و شروع کردن به حملات به کشتی‌هایی که از مسیر آب‌های عمان میرن.  به زور حمله میگن کشتی‌ها باید از مسیر ما رد بشه.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6113" target="_blank">📅 01:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6112">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RUlMbB8iOdXaJ-4e-xp0vvJfl4Dw-7okuCJ-unaECWGNgFAQ5RLnVoMZq3QusUvEMpUePOhA-w1RpkZKsUahu5EAjdr5FyqJ0SWbjKswIvbUmm0KQke-YealEqvlrvzfk6sxGd6ZxiAm1mPoVCpdM1gaBXMBxbHnyaoZi1px8DcQtyDsbqMx5wb4V1rkWWT83Oo4xg-gPCPovgm80sBxzXxMFqGcvQujVE8ILDwQAZ9opSXdJsujlfIq4jC6djmZ4EXb1uw0rQ441-mljrckALygmeak_lYnBKy255yvw8fv5_o-3bLolTmQFrwtI3El5wOVu3JBc0CRFr67PqhdUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینجا در حاشیه خاکسپاری جسد خامنه‌ای و جلوی قالیباف شعار میدادن «مذاکره با دشمن خیانت است»  هنوز به سه کشتی حمله نکرده بودن و نزده بودن زیر تفاهم نامه</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6112" target="_blank">📅 00:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6111">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d90d3d98f9.mp4?token=WIra3rFtdsP-PfLsa_EqmHIvGbdu4-rsy6ptbKkkljjF4TjIRNzmugGGoU_A6c1Z_ms5CWP2idCuxWxSkg0Igptj2GqU6fctkrKMmspOFebUHwLdYDb3hsEkLWZpDz2r-Xv0tUeK3RNEod0FvMf0L4k8pebUkTzfwXLTwh_BixYsQJQKOFO1xBJR-wtURgDAmuGCCdVQ5wyGyWN28x71-91A-7UASCXzYi_bVzkPIk9Xd9EVPYV54vo2YnuBvVJELRgyigPkJwS_oRMn9yC9TcBfKGXrcA71x-rFnXen6txx61owjqdrKLlhtsDORKG-3rUu-oyVtOL-I0XADZTqqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d90d3d98f9.mp4?token=WIra3rFtdsP-PfLsa_EqmHIvGbdu4-rsy6ptbKkkljjF4TjIRNzmugGGoU_A6c1Z_ms5CWP2idCuxWxSkg0Igptj2GqU6fctkrKMmspOFebUHwLdYDb3hsEkLWZpDz2r-Xv0tUeK3RNEod0FvMf0L4k8pebUkTzfwXLTwh_BixYsQJQKOFO1xBJR-wtURgDAmuGCCdVQ5wyGyWN28x71-91A-7UASCXzYi_bVzkPIk9Xd9EVPYV54vo2YnuBvVJELRgyigPkJwS_oRMn9yC9TcBfKGXrcA71x-rFnXen6txx61owjqdrKLlhtsDORKG-3rUu-oyVtOL-I0XADZTqqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این استوری رو ۶ روز پیش گذاشته بودم  میگفتن آمریکا میخواد آتش بس حفظ بشه ولی جمهوری اسلامی باید «کار دیگر» بکنه!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6111" target="_blank">📅 00:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6110">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/550f13e765.mp4?token=KiXIYQm8Bf61g2TVGP5vGFt45x7AcDnX7HWp4zUiYylZDM9Qp9ENJhmsYeze-xYffEQp_V9zKw2B5mFhtd4dbH_-QwTLYpI3dxl499_0xM1Rahx1QuZv8vK9nQxXIiZEYKa5WR3LEOyWWL0PFCpmzWNu_KwFcVw3aQSqcT0P4Mle8MYg9vPrm2j7EpGwwCKDfDegS2LW0gFVAOxLq0uzged6UH-WxRLfQOUy7lxdrO2DK2OIuRv16cIoKsa6DYkxcPJ-DA0LOUq3aD4fxZDTzptMeA5c1SREwuxgMGEkA2p9JzRZoQUMSCAOVC32z6tscCWfMGCtBJS651LRU4QKAZ-3ZBQGea6109BbdS9-RScq8Qz3GcmU6dliQLCkin05sQjMiPQwMj1V5Iz_qnkKX5iteJd3n24MuG0fh-Zw76yYpDU9sb5YviYG4HJRJEUNtTQB0HFSp3Mk9dNIKJhK8N11GzI_rPCV84IJfERi5I6i0kRRlYoMhz5A5UspeYQuH7jgwA0iaqU3TOap2QGAQQKpNpNV5qRxeltGDUE6-7zFHz_kJhhg8-rwyBw-xgXoMI7ldAzVhC2lpzp14VEi8M5vnCdirvdMgn2huzeav60QmKpm9auF2obvHOh-C2n9vRaOLarxS2aWppnmzwuuRHyILIX-o4XmeD8oiWrrIus" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/550f13e765.mp4?token=KiXIYQm8Bf61g2TVGP5vGFt45x7AcDnX7HWp4zUiYylZDM9Qp9ENJhmsYeze-xYffEQp_V9zKw2B5mFhtd4dbH_-QwTLYpI3dxl499_0xM1Rahx1QuZv8vK9nQxXIiZEYKa5WR3LEOyWWL0PFCpmzWNu_KwFcVw3aQSqcT0P4Mle8MYg9vPrm2j7EpGwwCKDfDegS2LW0gFVAOxLq0uzged6UH-WxRLfQOUy7lxdrO2DK2OIuRv16cIoKsa6DYkxcPJ-DA0LOUq3aD4fxZDTzptMeA5c1SREwuxgMGEkA2p9JzRZoQUMSCAOVC32z6tscCWfMGCtBJS651LRU4QKAZ-3ZBQGea6109BbdS9-RScq8Qz3GcmU6dliQLCkin05sQjMiPQwMj1V5Iz_qnkKX5iteJd3n24MuG0fh-Zw76yYpDU9sb5YviYG4HJRJEUNtTQB0HFSp3Mk9dNIKJhK8N11GzI_rPCV84IJfERi5I6i0kRRlYoMhz5A5UspeYQuH7jgwA0iaqU3TOap2QGAQQKpNpNV5qRxeltGDUE6-7zFHz_kJhhg8-rwyBw-xgXoMI7ldAzVhC2lpzp14VEi8M5vnCdirvdMgn2huzeav60QmKpm9auF2obvHOh-C2n9vRaOLarxS2aWppnmzwuuRHyILIX-o4XmeD8oiWrrIus" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدئو رو دو هفته پیش گذاشته بودم.  معاون سیاسی نیروی دریایی سپاه اینجا در جمع حامیان حکومت بهشون میگه خیالتون راحت باشه، حملاتی که ‌ آمریکا انجام  میده «واکنش»  به اقدامات ماست!  «کنش» نیست!   تمام این ۴۷ سال همین بوده!  یه کاری میکنن ، تنش راه بیفته،…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6110" target="_blank">📅 00:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6109">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">محمد اکبرزاده، ‏ معاون سیاسی نیروی دریایی سپاه، ‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.   او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.   جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6109" target="_blank">📅 00:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6108">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0b9d2dcec.mp4?token=XByu_wosMUaTPL0TWv3-2-6Oz5I1_eOWPbNAx8IjdQFor8Vp4U9zyORw8VKYWeI9Dyo331iHuLg3fIyRFrGRs9mCwZAsW56oQQ1OLi7wDmTxHqxh9UY7HFbl7Y8g2BHP__F33z3qwJ6Em64J3Vr8rWwVmzK8C2BbpZ8gH8jVlrxXZm1hUgVDllsWLcs9h8Ir9uuPQEs-r9qVbmNda-2niyxbcNlig5Gw1IrRji09R8nWGC_bggpV8XrhF-5NcL1s4kzrzTP8eM7BksRIO_DkEaKxC-miB1JBqMYpEDwr1XWA7dlk6R-7PIebHmSlFedZ-R7GSZYxqnKhVutvpDHUQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0b9d2dcec.mp4?token=XByu_wosMUaTPL0TWv3-2-6Oz5I1_eOWPbNAx8IjdQFor8Vp4U9zyORw8VKYWeI9Dyo331iHuLg3fIyRFrGRs9mCwZAsW56oQQ1OLi7wDmTxHqxh9UY7HFbl7Y8g2BHP__F33z3qwJ6Em64J3Vr8rWwVmzK8C2BbpZ8gH8jVlrxXZm1hUgVDllsWLcs9h8Ir9uuPQEs-r9qVbmNda-2niyxbcNlig5Gw1IrRji09R8nWGC_bggpV8XrhF-5NcL1s4kzrzTP8eM7BksRIO_DkEaKxC-miB1JBqMYpEDwr1XWA7dlk6R-7PIebHmSlFedZ-R7GSZYxqnKhVutvpDHUQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گشت زنی اف ۱۸ آمریکایی بر فراز چابهار</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6108" target="_blank">📅 00:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6107">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا : محاصره دریایی ایران وارد فاز اجرایی شد.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6107" target="_blank">📅 23:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6106">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
چندین انفجار در بندرعباس
🔺
چندین انفجار در اهواز
🔺
پنج انفجار در قشم</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6106" target="_blank">📅 22:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6105">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sQoUCdqC19WbZxz67FhF31aLrbQOjzhmK8i7jDvXkR1JsPvIls0tPOJd_ZaLhsgKaax48mba0h0iuvzGqOAytVqglCmwRwBPc7UHxEFuDyPZ2x9iiKacyWhvP6HElPZOWxmWA3_0DfqeUllM3e2EJ9jlC8BWRu4XGWXkHWZQ0g2RSCgFj_qh6R_ZC8Nwzclyw9E2qUAaIdpsSNX6s5yIncU97lu4SXWYqy_Sd-2Xks3TWTuzhgAoEEXBJQg9UURjRT_uNoli5ICqbd5cMMwyU_KIxitqNOXDO8QrKuxRMK5LzaF_e_UXAFnUY7g16PVSCf3KVm7eH2gGPgJhBfxn0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2077085449948938568?s=46</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6105" target="_blank">📅 21:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6104">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
دقایقی پیش : حمله به قشم و شنیده شدن چندین انفجار
🔺
حمله به یک نفتکش اماراتی در سواحل عمان
🔺
فعال شدن پدافند در کویت</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6104" target="_blank">📅 20:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6103">
<div class="tg-post-header">📌 پیام #18</div>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u8jnTwbVC3xl0sS2gNvq2sdrHA6WzXxhqyNyBvd_x5AKbqclrmPzQorlIMjXD-N48ON0fGMhUrEzIG2k9Fs6J-vDVdYr0H6sRZkk_eKnnd_B2297jazfinO5g-UKm-yELRPL8krHMUcD7DzukUUU7_Oo-Y-xl7u0PjiIgbfeeNeyyo-8gBn5rZSa8rDGs2KWX5QDfstnqi3K6ZQU8WKEfUpXUZuxBP9WvWTHs0JJG3pjkVBHvaQZgGBoeQgcoF4fmJ-lhqkcQLeTEbVhZ5mt-PU8chjMoLJVEHPLpH5rcA71WmqPmP2RIhWGDJ3IwWmYDm_rLLV_paftrUyoqMU_wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهپاد‌ها (قایق‌های تندرو بدون سرنشین) آمریکایی این مدلی به یکی از مهم‌ترین مراکز نیروی دریایی در بندرعباس نفوذ کردن و حمله کردن.  گفته می‌شود که در این حمله یک زیردریایی ج‌ا را نیز منهدم کردند.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6102" target="_blank">📅 18:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6101">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee96f6523b.mp4?token=TN28G-rHv4lkl_rjDdx0yOl2rLeUyx62r7_PhrHjmVkyZSyrKn10M3P7GtbgadxwBTPvp_XLMKjzvhlwKZ7uV3xjdgxnfQhNwYewNUtxKaE42_0J8amDH4TkE7isopxN0rZAZvpdnX3EomPKR4SUDhUCmPtMDdxK4vZQltkBOgfwTc81lm0hUm7bnq4BiHbooDG4GxrTt4octVsPepIwa6ekKhORb6LJiDnLGUp_P_zmzOzYrS8oKqDBaxkoWNRgP9YoV2kki2tmvImf87BaUOkPvlWIvr7f_qfd2v3BaWf2nRlOjm4XXU1L1Q5YOsqw5E8SynV0dOsyGhJwIIe9vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee96f6523b.mp4?token=TN28G-rHv4lkl_rjDdx0yOl2rLeUyx62r7_PhrHjmVkyZSyrKn10M3P7GtbgadxwBTPvp_XLMKjzvhlwKZ7uV3xjdgxnfQhNwYewNUtxKaE42_0J8amDH4TkE7isopxN0rZAZvpdnX3EomPKR4SUDhUCmPtMDdxK4vZQltkBOgfwTc81lm0hUm7bnq4BiHbooDG4GxrTt4octVsPepIwa6ekKhORb6LJiDnLGUp_P_zmzOzYrS8oKqDBaxkoWNRgP9YoV2kki2tmvImf87BaUOkPvlWIvr7f_qfd2v3BaWf2nRlOjm4XXU1L1Q5YOsqw5E8SynV0dOsyGhJwIIe9vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت جنگشون :)</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6101" target="_blank">📅 16:39 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6100">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ihZNEF2_kSt5wAZpnp36xFHpsjhP1weAFkL13Pjsk_q4uFsy_Whk1yxQpom79nVSkAv-U2vJLs9a01_qtpON8gZMN56UTTpG9PyBQH5zWSgcIswBT7pczjuwlJ1WO9yP1yGWt4mhtEnXYaIJdsbOCR4d0BNM74Ljs5qYKk8HIM5DSy-SOE33No54sluURz23VPfn4EsK4Gtp39ZQlqVKSrisXQe1yXKZEl3VyYGaNZkHs0RsYjZaqlWc9Yzj0rcorgU47tpTyHDXf9LjGQodX3Z2QN90vd2S_b_-5e9JHTNigJBcBsIPzeIidLc9TtxM7JfrY0pXWeG-BqbThKP5Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏آمریکا با استفاده از سه قایق بدون سرنشین (شِهپاد)، پایگاه دریایی دیروز بندرعباس را هدف قرار داد و تأسیسات نگهداری زیردریایی و کشتی را منهدم کرد.  این نخستین بار است که نیروهای آمریکایی در نبرد از قایق‌های تهاجمی بدون سرنشین استفاده میکنند.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6100" target="_blank">📅 16:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6099">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">۴۷ سال رژیم اسلامی</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6099" target="_blank">📅 15:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6098">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZDxYCbbYJhWX4QvDXhZQU5qsQYlcsJ2ZwV75iQan7j5_zz4UcG5O9oOsGEwlYLBYzU3zFRxofLknd43jooiY7PU3_im_zNhJKqxWncpWHVY_Vy2csah45DV5uaUVLaHP8SZjOX_26QSTHysDewck5IBD67DS1rGF4uamTmZ529MaC9E51o6Ooff3as_AEUH00iQOY0hRGt2NoKw6x1NQGrYf1jrRx9xBFNhpP2K4ukZpRuz3LfA0jip6APIwtnq39vXOrmhpvAmMr6uiMnSoVf12S6hk7D_VCThqIA8r06zXu_l4gVfRcbjjdc_IxbJAzC83kpT-syr14sVJIrdGxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
تخریب ساختمان مرکز آماد و پشتیبانی دریابانی نیروی انتظامی ⁧ بوشهر ⁩ در پی حملات هوایی ⁧ آمریکا ⁩ به مراکز نظامی جمهوری اسلامی</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6098" target="_blank">📅 15:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6097">
<div class="tg-post-header">📌 پیام #12</div>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac9c510f4f.mp4?token=R1LNOv-Y577zKq7eoE_ZJE4OoGcEWhFgNY9nDkcGGY_BooT6A4EfLAABZUNzb51t02n-l661Ip3E25cj6s90ZpCerHwfCAqM_r0Eq-XAieTe_9ZexcETgt_Q2AeN-kZO9TLq1PYIVpCRUwtm1G0S_tAVHrfnD7qKDnMD8CfWJZrSy-QMswgj5BeXZCgULTa9bMBBn8c0_cnOTl4C28acYXq7GhdW-_DbZlJoYsI5VfzZ6eI7Qq_y36VybYcL7b8WDjLy_LWiDenfMk28Vg1pmAi0fnR72tti0jKmkE2lS8NYpRnOiRACm_lrbwq6ef0PYTfT2YmjnviAWT7wzg7T2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9c510f4f.mp4?token=R1LNOv-Y577zKq7eoE_ZJE4OoGcEWhFgNY9nDkcGGY_BooT6A4EfLAABZUNzb51t02n-l661Ip3E25cj6s90ZpCerHwfCAqM_r0Eq-XAieTe_9ZexcETgt_Q2AeN-kZO9TLq1PYIVpCRUwtm1G0S_tAVHrfnD7qKDnMD8CfWJZrSy-QMswgj5BeXZCgULTa9bMBBn8c0_cnOTl4C28acYXq7GhdW-_DbZlJoYsI5VfzZ6eI7Qq_y36VybYcL7b8WDjLy_LWiDenfMk28Vg1pmAi0fnR72tti0jKmkE2lS8NYpRnOiRACm_lrbwq6ef0PYTfT2YmjnviAWT7wzg7T2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">می‌پرسه نظرتون درباره اینکه بدون هشدار قبلی برق رو قطع میکنن چیه؟
‏چمران میگه:
‏شما اگر بدونید پریروز چند نقطه برقی رو زدند دیگه این سؤالو نمی‌کردید.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6096" target="_blank">📅 14:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6095">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bj2guGvkEoCJjMneA_lRZNs1sgk8_uFKR-d3qNzZ0cntnnHWiwGpUA7-Inn0gf9yp0fBpa2TF5Q5sHWGgKfbvtjEoGFh9VTZtEueMQEfSHKPpxD-fqjAlO5UiU6KXUiZySDnHaVA0QQTWwmagcXnwDGmYKBs8rGYrSPhRCJIUDDFwRnxw3c1qM8Z4HWTGrMkUXiohbjGWQoWuF2FQvV-Whp_7evDGLWrDYruJ1yZY9CncfHQFGup4ott_Tn-wlXQwgUTMmdz2MnLu9Ides_VMvVuIH7kd948UZ-fY5X2msUi1x7cHwgOxS6wIneZUfeObJ-xr_PhMGDcsQYYI6vrjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه ترکیه، دیروز جمهوری اسلامی
رو با اسرائیل مقایسه کرد و گفت
رفتار این دو شبیه هم هستند.
(کاری ندارم که ترکیه خودش چه افتضاحیه، اما نشون از تغییر رویکرد ترکیه نسبت به ج‌ا داره)
یادمون باشه فرمان حمله اخیر از سوی ترامپ در ترکیه صادر شد! یادمون باشه معاملاتی بین ترکیه و آمریکا رخ داد، که آرزوی ۲۰ ساله دولت ترکیه بود.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6095" target="_blank">📅 14:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6094">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
🚨
حملات دقایقی پیش به بوشهر ، خورموج و….
🔺
سنتکام چند ساعت پیش گفته بود که این دور از حملاتش متوقف شده.  در اسامی شهرهایی که مورد هدف قرار گرفته بود هم مثلا نامی از کیش نبود!  مشخص نیست آیا همه این حملات را آمریکا انجام می‌دهد، یا کشورهای دیگر (مثلا عربی)…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6094" target="_blank">📅 13:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6093">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dH3bby3wGDz2jlp9xaHtyuaFTblwfPsulXqjHj8XfJYm_q7fRPFS0g90bmX6ogmQ2_b0IlmCQnoIZQ0FTYSPRM2xcaIP724PplCSH14NH-QtNBZtbhKeuI7f0WhIbWI_78knFrsc6-jtpqw_x2WwXls1dwGSWXV4_7oYlrjwehiCE3qb3dfa1ZOejIJ7Xuf_fhMfzmhXVokIn1-TV0MK6gDbRrV3sFY3UNm2-CmYvIdut74BeeC8sjJ0JST5HyhKM2b5f0uueT__7XxfgMR8sfE1uL8cBA6x0gbOBj5XfvKDND-jMoWrLbTW99eo2LwqZiy_FPLMyaBfFU1RFNTuZg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b04e0dceb0.mp4?token=TSnmt-ViyMDTyhBdsVRIY3P4ZLhBmVutsSZbiH1-F9UVikFlcnBvpygTk809LnfeNK17DajrAAprfr4IQ1n_7Pexu2gnCLuHhbBA2pw2Orz5zaw5mm4BaA02hgT1tWEEoMA0Srx_eHqKl82Q0wM3r-cMyo3NI8sdnb5s6tWmfEm6FXyStynH9UBnnLFj12ubvSNPAgftseKMHG-4XsE25sCB8y94UZSvZ9iGqLIyr1fs75BGmStOvjxoXYp92mGGbZeLqyKFZIlfOhCypy9-2KW0u_XA9lAhoyFPz8bm37vXPZjWfRaBlZUAc8KYqekQe9QoRtwKoX4139mp6va85lozEhilWvzjA9pMVjEvNgMCUMRGCCZha5RQIBYsP88WPqMs8w6hOecaaYLc4c4fKHhfDntesZkVLbV3M0pZFcRx6qDDxJmqPQ0dRH3Nnf0QQcvROzvhbb40xm2vBmaEFvxfdzr1mtjcaFERELzEU23Gpwh9co3YrDbtFery3sAor9rrm1q6CpdfAgKiw2tZUban9LnRQpWPDJNrjAql5yR7wf3lhW3Xt8c95MCVOw7mjC3RyybV1t8mdMStB7nAxS1wy2QnZl_AbfyrQe9DGqaKHcDaZtYKCscZmjF16L6Li38FoJQ2kmjNkJpUFcWYFIw0YAoQyKb1acX39e6jWvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b04e0dceb0.mp4?token=TSnmt-ViyMDTyhBdsVRIY3P4ZLhBmVutsSZbiH1-F9UVikFlcnBvpygTk809LnfeNK17DajrAAprfr4IQ1n_7Pexu2gnCLuHhbBA2pw2Orz5zaw5mm4BaA02hgT1tWEEoMA0Srx_eHqKl82Q0wM3r-cMyo3NI8sdnb5s6tWmfEm6FXyStynH9UBnnLFj12ubvSNPAgftseKMHG-4XsE25sCB8y94UZSvZ9iGqLIyr1fs75BGmStOvjxoXYp92mGGbZeLqyKFZIlfOhCypy9-2KW0u_XA9lAhoyFPz8bm37vXPZjWfRaBlZUAc8KYqekQe9QoRtwKoX4139mp6va85lozEhilWvzjA9pMVjEvNgMCUMRGCCZha5RQIBYsP88WPqMs8w6hOecaaYLc4c4fKHhfDntesZkVLbV3M0pZFcRx6qDDxJmqPQ0dRH3Nnf0QQcvROzvhbb40xm2vBmaEFvxfdzr1mtjcaFERELzEU23Gpwh9co3YrDbtFery3sAor9rrm1q6CpdfAgKiw2tZUban9LnRQpWPDJNrjAql5yR7wf3lhW3Xt8c95MCVOw7mjC3RyybV1t8mdMStB7nAxS1wy2QnZl_AbfyrQe9DGqaKHcDaZtYKCscZmjF16L6Li38FoJQ2kmjNkJpUFcWYFIw0YAoQyKb1acX39e6jWvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #6</div>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TC5-zqYuh0ECxZ3uGvITx9IzeY1cGvEbboWZOzhpduYzXzump0K8Vu6SObCGZDpebomtJI9Qq17k_ZWY9FbaGb9j3pQfNI5cLz9JIxVsE8nV0eFtNuwTupZA-FHASr_DXK_IZZDtX2gTueqg2vQBJ_hjfOgG00ekGtXXeG8EaikDdItvE6zoh4uaRlnHkng8ZzXJd8ddJjTYdqRRKBTEC9g3n7dIdYhwGlFlAkbKXaoCEewlTKe2yc4-KvoCvmDNpoYCgYrnJGDTaR5AYDZ4ast5DloviQTt7yFspYJ7UarS0S_FSnEnknpvjveqMyxaXdJbnD-m99XcSCHEKbhdeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شب گذشته سپاه به دو سوپرنفتکش (در سواحل عمان) حمله کرد.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6090" target="_blank">📅 09:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6089">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/671b861555.mp4?token=CVIZ63WcdvE-sYBzn69AukNp9rOTN1aCaBxr8TCixnGydLF7EXbIpqnbxGpy0xPO1Sa7jk5kotdvJbErVRwjvYg45Rk4qovDi9DMj1Wi1S4ePV73II36LXl-03gEwP1NVeWVIc59rwaf81IwtCH-PStvwO-1ZNDz3wJEYM1PvtkV8WW_d6Y1ZYKN8PvRB0VQDZxE2j_6dqj79_DzgoMmobQ3OshIgcrScryZVZ1FKDbFEhctuKWQw3dJJiODn_sh3jskpoPLZSMemURCTKloqsY-IvxpsB0kRKbSYxP4zGEzjVwb8Us1rQuEQCanRHXC7_7MyYz1LJt-vYG0ebXcV7MqG_7tJ9m2EVakkzfXH3VNTWPtqi8c1UAGiX6fWqLfdW6QzcWNcqz-CSkIpTNpO0ndOaZGo5cW3yM_Qf7OwWIGgCPG81srZcbqHy2xodWdnNwVHpY2Jia1RovYQgnqaqWDKQfuT__KVB3FF8-WrPa-rLEOAV5B0xVoVGdaCM2VobNfDzXFh-bJ79XI_nc_VbuX8Ap5uPun0W0uoZU073VA1S5GLB9-I9yBBNoMOa5nWwTF_ccsG9CW4SWDrByPsGZd-NuFWOIWi0WeAqC6BP75eawpz4dd1DH0skeJ4C1tdD3elzpKhLynRo56CaFxy7avmysHJQoVYoflRCZBv2o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/671b861555.mp4?token=CVIZ63WcdvE-sYBzn69AukNp9rOTN1aCaBxr8TCixnGydLF7EXbIpqnbxGpy0xPO1Sa7jk5kotdvJbErVRwjvYg45Rk4qovDi9DMj1Wi1S4ePV73II36LXl-03gEwP1NVeWVIc59rwaf81IwtCH-PStvwO-1ZNDz3wJEYM1PvtkV8WW_d6Y1ZYKN8PvRB0VQDZxE2j_6dqj79_DzgoMmobQ3OshIgcrScryZVZ1FKDbFEhctuKWQw3dJJiODn_sh3jskpoPLZSMemURCTKloqsY-IvxpsB0kRKbSYxP4zGEzjVwb8Us1rQuEQCanRHXC7_7MyYz1LJt-vYG0ebXcV7MqG_7tJ9m2EVakkzfXH3VNTWPtqi8c1UAGiX6fWqLfdW6QzcWNcqz-CSkIpTNpO0ndOaZGo5cW3yM_Qf7OwWIGgCPG81srZcbqHy2xodWdnNwVHpY2Jia1RovYQgnqaqWDKQfuT__KVB3FF8-WrPa-rLEOAV5B0xVoVGdaCM2VobNfDzXFh-bJ79XI_nc_VbuX8Ap5uPun0W0uoZU073VA1S5GLB9-I9yBBNoMOa5nWwTF_ccsG9CW4SWDrByPsGZd-NuFWOIWi0WeAqC6BP75eawpz4dd1DH0skeJ4C1tdD3elzpKhLynRo56CaFxy7avmysHJQoVYoflRCZBv2o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: بیشتر موشک‌هاشون رو از کار انداختیم، بیشتر پهپادهاشون رو.
🔺
توان ساخت پهپادشون رو حدود ۹۲ درصد از بین بردیم. توان ساخت موشکشون رو ۸۹ درصد نابود کردیم.
🔺
یه کم توان براشون مونده، اما برای ما هیچ توانی ندارن. این دیگه تقریباً یه درگیری نظامی کوچیکه</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6089" target="_blank">📅 08:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6088">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3962370842.mp4?token=euGxk3TlzxBz48_UKotegnxcypbKIJjTbiD3H0UKCbCtOSyOZNyeAQcif7ISOc1c2gqmgNxhO_pA3LRZrJNjwv9ahA6mYzCqB5DaA5ilpnsluMKxL03pDlH-ULDFpe4ceWH7EzIJSkaco6CBw5Aut8T7vlBZyhg8cU59XZnrIGk8Irc46eVeESfN1q2ISwhwpFAyP_Scb0R59JJt79KBx6-KuZezPSDlNczaNZ5s7QVc4GYCg9eR4bMmjIhQmbhIeyaxwL5hJHROfQZPNdX6o2GWGbbUGRnwEPGLHDbvtRiCIPlYd-LfbYXFZebpMEbvSSB-d_f9BmyGv-euV5BqBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3962370842.mp4?token=euGxk3TlzxBz48_UKotegnxcypbKIJjTbiD3H0UKCbCtOSyOZNyeAQcif7ISOc1c2gqmgNxhO_pA3LRZrJNjwv9ahA6mYzCqB5DaA5ilpnsluMKxL03pDlH-ULDFpe4ceWH7EzIJSkaco6CBw5Aut8T7vlBZyhg8cU59XZnrIGk8Irc46eVeESfN1q2ISwhwpFAyP_Scb0R59JJt79KBx6-KuZezPSDlNczaNZ5s7QVc4GYCg9eR4bMmjIhQmbhIeyaxwL5hJHROfQZPNdX6o2GWGbbUGRnwEPGLHDbvtRiCIPlYd-LfbYXFZebpMEbvSSB-d_f9BmyGv-euV5BqBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات شدید به کنارک - امشب</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6088" target="_blank">📅 01:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6087">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
ترامپ : حملات جدید می‌تواند برای دو یا سه هفته ادامه یابد.
🔺
سنتکام : موج جدیدی از حملات را برای سومین شب پیاپی آغاز کردیم.
🔺
باشگاه خبرنگاران : ۷ انفجار بزرگ‌ در بندرعباس</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6087" target="_blank">📅 00:56 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6086">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
شنیده شدن ۳ انفجار شدید در جزیره کیش
🚨
انفجارهای شدید در جم - بوشهر
🚨
چند انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6086" target="_blank">📅 00:44 · 23 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
