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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-26 15:32:33</div>
<hr>

<div class="tg-post" id="msg-6185">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/farahmand_alipour/6185" target="_blank">📅 15:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6184">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ijt5NRK3bltsYCoHkEWDkhrcfi5qZ--8GXUF5P3-8IK0TPqriYcGaj_rju2tJ7vUgwYsS5u9HmUMtsvwofBpwQIY_G8VauO1lhDEPE79BAXOnZcWgApkjZp8GP76Nxi2zQQ9wVFiPyWCkbhC-9yvd0w_1ZnHvvy65JIPelk236nzSTkWZJOOo82ttchl91wf8Wqd9mCD7pIa5mPzdbLXD1iNMUNym65cPe24AyUPfo20PC1xb_MnWNYdf5MmiJ0HfjfWiWjCciXf3-nfQwoVq71WQBin3R_7y7TWbh_DZcycgfxnLxzhmpI6d4g18W17wla0suaespRUpAdDgjiyJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جمهوری اسلامی به تاسیسات آب‌شیرین  و تولید برق کویت حمله کرده.</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/farahmand_alipour/6184" target="_blank">📅 14:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6183">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61a69b588c.mp4?token=JYCCchxyPd6A7ilQkz80EaXyVs2eEsT0foYs0LNA-hNCrlVX8uDIyd-GqnSj5S2pA-NoJCWDs722GN6rh_Ulp8FaQ0otBJuAQbmpJQ708RODUIsw74MXBXvtq7PL43Lw1-UcXriz7sjhxUJ_-S4b-ut0y0jgQ6bDNuTeQqHPL1cMhNAvReGvM30SDFNiUAhxndwwJO1AJzo07_DC2-7eu59ijUkCzJoG_7SBCDpUqnnqNyZzxS9d3tfNka8FoWGidqeZPqX2Fe-VYDqyVPpf4atEFBFm_dWFHWLR04c2eYcB5XOY4r0ClYFla4O8NDsMZLeR8uv-naHUfuY0s1njVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61a69b588c.mp4?token=JYCCchxyPd6A7ilQkz80EaXyVs2eEsT0foYs0LNA-hNCrlVX8uDIyd-GqnSj5S2pA-NoJCWDs722GN6rh_Ulp8FaQ0otBJuAQbmpJQ708RODUIsw74MXBXvtq7PL43Lw1-UcXriz7sjhxUJ_-S4b-ut0y0jgQ6bDNuTeQqHPL1cMhNAvReGvM30SDFNiUAhxndwwJO1AJzo07_DC2-7eu59ijUkCzJoG_7SBCDpUqnnqNyZzxS9d3tfNka8FoWGidqeZPqX2Fe-VYDqyVPpf4atEFBFm_dWFHWLR04c2eYcB5XOY4r0ClYFla4O8NDsMZLeR8uv-naHUfuY0s1njVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۱- ما مخالفت کردیم، بعله، کاملا درسته!  ولی آیا شما به خاطر حرف ما دیگه لبنان رو رها کردید؟ نجنگیدید؟ پول و سلاح نفرستادید؟  به خاطرش حتی موشک به اسرائیل نزدید؟  (که اونهم اومد در پاسخ ماهشهر رو زد؟)  خب جنگیدید و شکست خوردید!!! هم در لبنان،  هم ‌در سوریه…</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/farahmand_alipour/6183" target="_blank">📅 14:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6182">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farahmand_alipour/6182" target="_blank">📅 14:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6181">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farahmand_alipour/6181" target="_blank">📅 13:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6180">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/6180" target="_blank">📅 11:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6179">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6179" target="_blank">📅 09:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6178">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26ef12b93f.mp4?token=gQaoAYWVaDThIrFT6v0SMdZMNkx4TA3jclUzJzT9SgLoVyYvzuBAs6Gqhy-_N1k277GGoVX_IbMcnKXIi2CDlrcALulHj5YDfNCoc5xEiJmSd-oCVl67n9jjSyZmYi0GvVBmGcUzDtZOUCBay9OlrZL-K82Y7uepqgS64LBzJHQ9T2STfxdAwJyXZOvWXqob52USmf2qIcnLulhQS5Nx2tPylu74o9IGWjepVmiuJHO9Dm0DqB6uePJagxSEdy8Tpqe3kmyGHlbVpYfzZvIFNgyCM44qLm0sepNM26eUD5tGSKyO_EX3uoUX02PkJRi-qDv_EmDegjDMFWulTVmJPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26ef12b93f.mp4?token=gQaoAYWVaDThIrFT6v0SMdZMNkx4TA3jclUzJzT9SgLoVyYvzuBAs6Gqhy-_N1k277GGoVX_IbMcnKXIi2CDlrcALulHj5YDfNCoc5xEiJmSd-oCVl67n9jjSyZmYi0GvVBmGcUzDtZOUCBay9OlrZL-K82Y7uepqgS64LBzJHQ9T2STfxdAwJyXZOvWXqob52USmf2qIcnLulhQS5Nx2tPylu74o9IGWjepVmiuJHO9Dm0DqB6uePJagxSEdy8Tpqe3kmyGHlbVpYfzZvIFNgyCM44qLm0sepNM26eUD5tGSKyO_EX3uoUX02PkJRi-qDv_EmDegjDMFWulTVmJPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادی از سخنان سردار نقدی : اگه حتی به آمریکا حمله کنیم، قدرت پاسخ‌گویی هم ندارند!
با کدام پشتوانه اقتصادی میخواهند بجنگند؟ با کدام پشتوانه مردمی خودشان؟ همه جا در محاصره ما هستند.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6178" target="_blank">📅 08:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6177">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d050ea81f.mp4?token=GXFlQQbFMPL99OuKitmuYM7_gpOlEx2qvvIZ7PIOj8YGh4HIcm7Qf9a69gzckHFe2P6Rybhsfz85WWpn_UYp4cVW7Rl9b56DHYLZDncL0Faokm3P68zdXk2GDl8lju5GUM8ZYPRXODiqbeJojQDpsoS49r5oL07Gu3sQ_kciZ96BimKoCZnS-ciA_qz1mF_86f_hO-Jcorra3AJ8-nsM2eRkUGgFB2pjk_giCybNORsGxvGwwGxWkoiG1hpTKxYs__RiD87pTTElgON6_LsxkvLS1nohQtEmgs4QwKdwG5uS9_n6RIKT5PPvOgpRaX8uecZdxrTHU7CpjWftT5smiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d050ea81f.mp4?token=GXFlQQbFMPL99OuKitmuYM7_gpOlEx2qvvIZ7PIOj8YGh4HIcm7Qf9a69gzckHFe2P6Rybhsfz85WWpn_UYp4cVW7Rl9b56DHYLZDncL0Faokm3P68zdXk2GDl8lju5GUM8ZYPRXODiqbeJojQDpsoS49r5oL07Gu3sQ_kciZ96BimKoCZnS-ciA_qz1mF_86f_hO-Jcorra3AJ8-nsM2eRkUGgFB2pjk_giCybNORsGxvGwwGxWkoiG1hpTKxYs__RiD87pTTElgON6_LsxkvLS1nohQtEmgs4QwKdwG5uS9_n6RIKT5PPvOgpRaX8uecZdxrTHU7CpjWftT5smiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پل  کهورستان در اطراف بندرعباس
که شب گذشته مورد حمله ارتش آمریکا قرار گرفت</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6177" target="_blank">📅 08:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6176">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔺
معاون استانداری بوشهر:  شب گذشته ارتش آمریکا با چند موشک به پایگاه‌های هوایی و دریایی بوشهر حمله کرد.
🔺
خبرنگار صداوسیما: دیشب به تأسیسات برق و مخزن سوخت فرودگاه ایرانشهر حمله شد.
🔺
دیشب ۶ پل مورد حمله قرار گرفت از جمله پل‌های رفت و برگشت بندرعباس - لار …</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/6176" target="_blank">📅 08:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6175">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/6175" target="_blank">📅 08:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6174">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
حملات شدید به بوشهر</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6174" target="_blank">📅 01:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6173">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0adb998b26.mp4?token=rd13S5pp3Kce2cy9fpX1B_3zEhMs-C1kBcIzJxS1W10WbsOI4Zl5yMm6F_yeys6DbAZEWPTSeHC5tQZj208lKrKKqpufGoLsElX9B44vrWhqGk_2emnFfS1GGMgXrNpIKkOP4CA0Do1etuFX_ITx412w9AeVaNzJEkEKCuEYOibKHDvYJggvv18-gu78UagO_75uaTEVCABDih44ovev7qxpfBNLdXktrjvNFLfLKv5AAi3ZSoiruio6xY1VtxnvTGdSFbxwqs0B1ZW1V8dqhlvHo8CE5uxYGm48SfztDYa5QdB8XbXUIKunTFMFOmh4OxNKB-QZrEohR_8lqFrS3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0adb998b26.mp4?token=rd13S5pp3Kce2cy9fpX1B_3zEhMs-C1kBcIzJxS1W10WbsOI4Zl5yMm6F_yeys6DbAZEWPTSeHC5tQZj208lKrKKqpufGoLsElX9B44vrWhqGk_2emnFfS1GGMgXrNpIKkOP4CA0Do1etuFX_ITx412w9AeVaNzJEkEKCuEYOibKHDvYJggvv18-gu78UagO_75uaTEVCABDih44ovev7qxpfBNLdXktrjvNFLfLKv5AAi3ZSoiruio6xY1VtxnvTGdSFbxwqs0B1ZW1V8dqhlvHo8CE5uxYGm48SfztDYa5QdB8XbXUIKunTFMFOmh4OxNKB-QZrEohR_8lqFrS3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏فارس: جزییات حملۀ   آمریکا به پل‌هایی در شهرستان خمیر؛ ۲ نفر شهید و ۴ نفر مجروح شدند</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6173" target="_blank">📅 00:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6172">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iYCu8XrF-1WqfnO07o-fr9OaKRkYH1w8FqQMzfE9ZZDlMdXe3zyxME8VlPcIdomEPmFYv6E6wgnaYe7qNwZ1AyBqGhZuogz80itTU6NtXBkS0y3gAjYL9gwZ55u7zFKCD9SOlrEVg1hYxeeZexZNr89hUAV9Ifaeqa2MaFh0Q6F_h8Cp-J3H_r2I_g6ZwkFRUt1kWI6L1SKqFJAv_IbJMHdEt9vwTzRYkyv6bY55NmmA_mcih6bOVpyK58g9LTH4SEY_vNrImKx_28PZV2h7RRdQsvVwPblwpLzBdEeugkG3pRXNeHeyQ1oHW1hZBvzV8IVIABR6U_YGDiHuKssflA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله به یک پل در اطراف بندرعباس خبرگزاری‌های داخلی : پل ارتباطی بندرعباس و لار و شیراز  بود.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6172" target="_blank">📅 00:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6171">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
صدا و سیما :دقایقی پیش ایستگاه انشعاب راه آهن بندرعباس از سوی دشمن آمریکایی هدف قرار گرفته شده و ۲ هموطن مصدوم شدند.
بندرعباس مهم‌ترین دروازه واردات و صادرات کشور است و شبکه ریلی بخش بزرگی از این حمل و نقل را بر عهده دارد.
این حمله می‌تواند به حمل و نقل کالا ضربه بزند و به آن اختلال وارد کند،</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6171" target="_blank">📅 00:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6170">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
حملات گسترده به حمیدیه و شوش در خوزستان</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6170" target="_blank">📅 23:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6169">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
حمله جنگنده‌های آمریکایی به فرودگاه ایرانشهر</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6169" target="_blank">📅 23:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6168">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6168" target="_blank">📅 23:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6167">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6167" target="_blank">📅 22:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6166">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6166" target="_blank">📅 22:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6165">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‏
🚨
🚨
سنتکام: موج جدید حملات در پنجمین شب پیاپی را شروع کردیم.
🚨
مهر: حمله مجدد آمریکا بندرعباس
در ساعت ۲۱:۳۵ نقاطی در بندرعباس مورد اصابت قرار گرفت.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6165" target="_blank">📅 21:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6164">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbd6cb3b5f.mp4?token=lXXlwF25D4vSFSxBkC4LuszImi6PbkkRp_acZbSUSbROnMXQ8NmzZVcc5kc_l2f8GszCBG6LDLj3AU06zbae1o3xxCniTQ59Wnz-s4mRZVg8xyBtwAVhIxzKt0LZ7NcgFfbv2c56J_NEkqHT9akcucR_9P8AZG2hde3i4rNONn2Bce9mKXUIMsALQmjwmCofff0mo9nwORImES4xvHGKf5pCDbkmi7A-PvEWZp3A8z2QJEky2ttPEnl-BrGCXX5TEClwJkWQUmaRCbVDS0Ii8WqQiv-1bMDvwdazh34etFigWMg_gLBknuweeCHdmHVTp90COwFD7g8y8MiUQXttgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbd6cb3b5f.mp4?token=lXXlwF25D4vSFSxBkC4LuszImi6PbkkRp_acZbSUSbROnMXQ8NmzZVcc5kc_l2f8GszCBG6LDLj3AU06zbae1o3xxCniTQ59Wnz-s4mRZVg8xyBtwAVhIxzKt0LZ7NcgFfbv2c56J_NEkqHT9akcucR_9P8AZG2hde3i4rNONn2Bce9mKXUIMsALQmjwmCofff0mo9nwORImES4xvHGKf5pCDbkmi7A-PvEWZp3A8z2QJEky2ttPEnl-BrGCXX5TEClwJkWQUmaRCbVDS0Ii8WqQiv-1bMDvwdazh34etFigWMg_gLBknuweeCHdmHVTp90COwFD7g8y8MiUQXttgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ازغدی : اگر میخواهیم اغتشاش نشود
باید با آمریکا مبارزه کنیم
(که حواس مردم به جنگ پرت بشه
و تقصیر کاستی‌های حکومت بیفته پای جنگ
و دوباره جنگ بشه «نعمت» !)</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6164" target="_blank">📅 21:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6163">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
استانداری هرمزگان:  در ساعت ۱۸:۱۰ امروز نقطاتی در قشم مورد اصابت موشک‌های آمریکایی قرار گرفت.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6163" target="_blank">📅 19:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6162">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NiBKy1Q0TRHANsufzTEmKh4ZQa3pEDqfIFZyvbxEq0R3NyTBzs-d-Q5WzXvQGrQTItR_DqfAim_bZcYdmjf02eiwzgii3o9t46E3RCPOIxos5XCCFoL6akBZEdhjhD4eJNB5dNVl3wWPNhLTcl9TCFb-Aa9XOKffh2mAWFm9ax3U-9HsQMFH4bCLz_KOaSN0vW5WeXcMdPGG2xgbJEEZJMux8aGViewbLb8Lh6KDZR1gg10qlteBFTzGYociTA1kRK7KX3qE_EEQrv-G8HzR4-_UU1eVD0ezojSm6v0cJCRjshAi3QfsTyeqUIDJ79zq9q1i3ceL5xlKbjkhCSC7Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رویترز :
پاکستان به ایران هشدار داده‌ که اگر به عربستان سعودی حمله کند، پاکستان آن را حمله‌ای علیه خود خواهد دانست و اعلام کرده‌: «این خط قرمز ماست.
»
پاکستان و عربستان قرارداد پیمان دفاعی مشترک دارند که بر اساس آن حمله به هر کدام ، حمله به دیگری تلقی می‌شود.
🔺
برخی اعتقاد دارند که یکی از انگیزه‌های اصلی تلاش پاکستان برای میانجی‌گری میان ج‌ا و آمریکا ، نگرانی از وقوع جنگی است که دامنه‌اش به عربستان برسد و پاکستان را ناچار به ورود به این جنگ کند.
اینک که تفاهم نامه کنار رفته، پاکستان بیش از پیش نگران این موضوع است.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6162" target="_blank">📅 19:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6161">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
استانداری هرمزگان:
در ساعت ۱۸:۱۰ امروز نقطاتی در قشم مورد اصابت موشک‌های آمریکایی قرار گرفت.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6161" target="_blank">📅 19:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6160">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0a471388f.mp4?token=odTYSqMApeFPY7Ws3LYwEdDtCr4PAKpc1WF1v41-WwRQj1NXA8Mawe5r73_NVLAA-ZigfSxih1AzPsgWKZ3wV-Jer8RxRTaYiWCzoqCEE-CPfYExgiAu8607-nRwlUUMl0QjSs-Iie3V4kXOr4ZTGE6ZOJJQBXEvbN5ptDZy1o5-Nv3caKCdEPT1OZFkr4wWjao8NjA9M4raaS-SrrCqyvdHvwjMu4ulWkfw18RHTMraOIjLHqbjQLEGURy8gF2JFXjEbw6GBubCwF6_s_Mx5qZw9cmuE9ApKhe1tImAqvx_DCPwA7NXWDaQ-3lKfUo75XCR3igaax7aAZVP820Oa32sKePsq7gLL1aPGBKfKZlBJwNDD49Lfy6FrAkS4GmIa0DLCJJDsONyccLgSofPPcuN-4-iHoe30KL7p4yEilF8gH6JlZ4zDk3XG2UkkfLla-2mKyEUaqaII2SifzakgYZOP3pLPOJ-NLSKtF904N94Ijj_WcYbLsVL_uVauklOdGDvgnQAcwTO2sffLDgDcTgobYo3q1G85WdUlGDJF9KKB6wHn3HqJXUo7TI4mcP_VIygRGbNYDpuMJKtML4QikEEhtbZvw_pQFyN7wVgStZRWqf4O_P3cD6lsA27SFjfd95EUWAm4mYKBQ_ZxiZRvJYSlRQfBy_yB2jediJEJnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0a471388f.mp4?token=odTYSqMApeFPY7Ws3LYwEdDtCr4PAKpc1WF1v41-WwRQj1NXA8Mawe5r73_NVLAA-ZigfSxih1AzPsgWKZ3wV-Jer8RxRTaYiWCzoqCEE-CPfYExgiAu8607-nRwlUUMl0QjSs-Iie3V4kXOr4ZTGE6ZOJJQBXEvbN5ptDZy1o5-Nv3caKCdEPT1OZFkr4wWjao8NjA9M4raaS-SrrCqyvdHvwjMu4ulWkfw18RHTMraOIjLHqbjQLEGURy8gF2JFXjEbw6GBubCwF6_s_Mx5qZw9cmuE9ApKhe1tImAqvx_DCPwA7NXWDaQ-3lKfUo75XCR3igaax7aAZVP820Oa32sKePsq7gLL1aPGBKfKZlBJwNDD49Lfy6FrAkS4GmIa0DLCJJDsONyccLgSofPPcuN-4-iHoe30KL7p4yEilF8gH6JlZ4zDk3XG2UkkfLla-2mKyEUaqaII2SifzakgYZOP3pLPOJ-NLSKtF904N94Ijj_WcYbLsVL_uVauklOdGDvgnQAcwTO2sffLDgDcTgobYo3q1G85WdUlGDJF9KKB6wHn3HqJXUo7TI4mcP_VIygRGbNYDpuMJKtML4QikEEhtbZvw_pQFyN7wVgStZRWqf4O_P3cD6lsA27SFjfd95EUWAm4mYKBQ_ZxiZRvJYSlRQfBy_yB2jediJEJnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنرنمایی جدید جمهوری اسلامی</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6160" target="_blank">📅 19:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6159">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfb27a8797.mp4?token=OSC2d6TMY9bVnsYVoHTWa-X9an6-EHfvx6CiEO1e2VQPnteGyXm3lE0Fq_n49CvFbpSG5Zq_7Wds7iZ34aW1A50U7Kpvc2PzNcxPuVQ-VJ8J0juVQLj1yogKjgdayA_Nrs6Z_CWBfKGrQLaT9gFiWAq--m4zyIb1H96GfYvHRbF2eTzqvUj7D0t4V-MuTQpu-5b9lS626yEM1oDkq9sGYZJlrGh6JjlWQ7UCAQaENw4GK_FHK5zh3XuBJ5XiFTrcLWRB-I06rSz5sSl0rf6hL2s_WwR2a5EVxsubYaDV9JOEvlehFqxHORlDfU0IQStqgKHMAEsmxm0iImocFCS3Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfb27a8797.mp4?token=OSC2d6TMY9bVnsYVoHTWa-X9an6-EHfvx6CiEO1e2VQPnteGyXm3lE0Fq_n49CvFbpSG5Zq_7Wds7iZ34aW1A50U7Kpvc2PzNcxPuVQ-VJ8J0juVQLj1yogKjgdayA_Nrs6Z_CWBfKGrQLaT9gFiWAq--m4zyIb1H96GfYvHRbF2eTzqvUj7D0t4V-MuTQpu-5b9lS626yEM1oDkq9sGYZJlrGh6JjlWQ7UCAQaENw4GK_FHK5zh3XuBJ5XiFTrcLWRB-I06rSz5sSl0rf6hL2s_WwR2a5EVxsubYaDV9JOEvlehFqxHORlDfU0IQStqgKHMAEsmxm0iImocFCS3Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر قالیباف، تیر ۱۴۰۳:
ما غنی‌سازی را ۲۰ درصد کردیم جنگ شد؟ ۶۰ درصد کردیم جنگ شد؟
hafezeh_tarikhi</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6159" target="_blank">📅 18:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6158">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ایران که ۴۷ ساله که در آتش فتنه اینها می‌سوزه</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6158" target="_blank">📅 17:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6157">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">سخنگوی قرارگاه خاتم : هر چه در منطقه سالم مانده از نجابت جمهوری اسلامی است!
ذوالفقاری: «همه آنچه که بنا به نجابت ایران هنوز سالم مانده، یعنی تمامی زیرساخت‌ها در منطقه، زیر ضربات پولادین نیروهای مسلح مقتدر جمهوری اسلامی در هم کوبیده خواهد شد؛ آن‌چنان که اثری از آن‌ها بر جای نماند و گویی از ابتدا وجود نداشته‌اند.»
سخنگوی قرارگاه مرکزی خاتم‌الانبیا همچنین دخالت آمریکا در تنگه هرمز را «خط قرمز شکست‌ناپذیر» جمهوری اسلامی خواند.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6157" target="_blank">📅 15:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6156">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ca0d3dd94.mp4?token=ZamPiwXbfK9qVdHX1Pi0W_pbdpoQ_YIKQTJP5WdYKNjBwq5td4BRdpN3KIqtd1ziqA00_V2MaceLpa1mAlo7tUZR_1Pa07kcCFCndZa2TEdOOgh0YwOAo9MCSrsNb_ypEu_NuY1jrtafQyC9NFsNamUSuQZhgjivHvlekNyRYxiBNkHke2vavb8XSukjnvqkINtRFOiYpgtx7QYePYvkuHSp2YMcVqe4LC6--ld2zI0aN_um7sYlSyE-Kx0NZ0rIwP39SGL_gkOt2ROumlNgQvnw_1jkF5tfu2n1q9uQtPflMedT3HH5L4f316pTScMBISjdEHphOlBk0UrxbPTwWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ca0d3dd94.mp4?token=ZamPiwXbfK9qVdHX1Pi0W_pbdpoQ_YIKQTJP5WdYKNjBwq5td4BRdpN3KIqtd1ziqA00_V2MaceLpa1mAlo7tUZR_1Pa07kcCFCndZa2TEdOOgh0YwOAo9MCSrsNb_ypEu_NuY1jrtafQyC9NFsNamUSuQZhgjivHvlekNyRYxiBNkHke2vavb8XSukjnvqkINtRFOiYpgtx7QYePYvkuHSp2YMcVqe4LC6--ld2zI0aN_um7sYlSyE-Kx0NZ0rIwP39SGL_gkOt2ROumlNgQvnw_1jkF5tfu2n1q9uQtPflMedT3HH5L4f316pTScMBISjdEHphOlBk0UrxbPTwWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله شب گذشته ج‌ا به اربیل در عراق
علی‌الزیدی نخست‌وزیر عراق با صدور بیانیه‌ای،
این حمله را محکوم کرد.
در این بیانیه آمده که «به آژانس‌های امنیتی
مربوطه در هماهنگی با نیروهای امنیتی منطقه دستور داده شده که همۀ تدابیر لازم برای ممانعت از تکرار حملاتی از این دست، و نیز مقابله با هرکسی که به‌دنبال خدشه‌وارد کردن به امنیت جامعۀ سرفراز عراق باشد را اتخاذ کنند».</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6156" target="_blank">📅 14:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6155">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZoqXA0AsNtcLHYROAmpbsFTJ5M2ZCgqCah9YlaZr0Na8bUah0IugagHlU2X1kA721iscpz-VQ9ZCQ5QT3B-QBXfBQSp74hASe8lt060nb1CXdpNWye0C6GF-cwQSXt99GcW8NCjKS0zziAFJ5nya73Nwxm9oaTwLqKOK-fNRKEk76TwQnWsRR7cAyVYJV_ScAf1vHfCrHl1EYV3vZELqNlFKuxcYGAiULfABHtn8qkSRs3ZFA6Dg8uhQhg_VeCqHrKcyHKi09EwyFsxwuua-hpwDIeE7OVnTWFBk14cfVhBV3vsikOnJfLi5ZZCbp88us-RW1y5R0TTaxnyNS06uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وراجی نکنید  بگذارید بجنگند که صلح بیارن :)  مثل صلحی که ۴۷ ساله در لبنان  ‌ و غزه آوردن!  انتقاد از خامنه‌ای عین بی‌شعوری است!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6155" target="_blank">📅 12:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6154">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">وراجی نکنید
بگذارید بجنگند که صلح بیارن :)
مثل صلحی که ۴۷ ساله در لبنان
‌ و غزه آوردن!
انتقاد از خامنه‌ای عین بی‌شعوری است!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6154" target="_blank">📅 11:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6152">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1933ad174.mp4?token=Vmaxi51IxZXwfGWqjrEfRF6m36RiYJVpdMi398VqdLfQDqm0y0t-B2en7clDUyejlKisdclp9R93WGcL-viRXvpdpb3sHoAj6OGzh0FeVtUWoedqDnqB6o-zKPOZUZP2qj4c9CL0FGIVse82PhD1eOo2-pqQrlYynoyKKUPVSl4Z4sJO8s3ybKgJirfqjgaSQdPcmxmnOOnOY3He_H3_9Q0DPMi_qMjeZlU40GIkhQLpEpyLHOFbARf7BbVf9b1ZS6r8fckZt9WGZSZwL39rw9kdYc993baDh8L-i4UzvFq2IP-RLCaLNHUgodgQ-3JelEYFKPx5F8MPduCGIMasMmmgNJAarMuWZNuxyPkRwByIcmnSIS1cbNVTMvWNVLrinuROuAoS-UVAIej__gnY01dq2c9D69IF5oUPLjnR6lG8iGoc9JKyQy00OHT56-zVo0Oh3QFbaxukVLvtCBwd3RqBDdLlSmpzgwiwcFpMLedNycnUlwQdynHj6Kx3tFqLLhK4GoM1EHjPqNPweY1LRIPeH8q7KPfJFFir08jsLkvTcAIt2sib6qYtGK7shUGzDvWsSytz5vOXxJqHumi8Aqcx-5FWtKCjqOHJXm6LVjCC3vV_PzCpvpTAGAnrq3HzH6nyngVyac8065D0-tszANVUV6wExj0s6Bem418hJsI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1933ad174.mp4?token=Vmaxi51IxZXwfGWqjrEfRF6m36RiYJVpdMi398VqdLfQDqm0y0t-B2en7clDUyejlKisdclp9R93WGcL-viRXvpdpb3sHoAj6OGzh0FeVtUWoedqDnqB6o-zKPOZUZP2qj4c9CL0FGIVse82PhD1eOo2-pqQrlYynoyKKUPVSl4Z4sJO8s3ybKgJirfqjgaSQdPcmxmnOOnOY3He_H3_9Q0DPMi_qMjeZlU40GIkhQLpEpyLHOFbARf7BbVf9b1ZS6r8fckZt9WGZSZwL39rw9kdYc993baDh8L-i4UzvFq2IP-RLCaLNHUgodgQ-3JelEYFKPx5F8MPduCGIMasMmmgNJAarMuWZNuxyPkRwByIcmnSIS1cbNVTMvWNVLrinuROuAoS-UVAIej__gnY01dq2c9D69IF5oUPLjnR6lG8iGoc9JKyQy00OHT56-zVo0Oh3QFbaxukVLvtCBwd3RqBDdLlSmpzgwiwcFpMLedNycnUlwQdynHj6Kx3tFqLLhK4GoM1EHjPqNPweY1LRIPeH8q7KPfJFFir08jsLkvTcAIt2sib6qYtGK7shUGzDvWsSytz5vOXxJqHumi8Aqcx-5FWtKCjqOHJXm6LVjCC3vV_PzCpvpTAGAnrq3HzH6nyngVyac8065D0-tszANVUV6wExj0s6Bem418hJsI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینها اگر نوحه میخونن و مداحی و رجز خوانی و.. برای کودکان غزه و لبنان و میناب و….. از تاسف از دست رفتن زندگی نیست! میخوان در این جنگ بی‌‌‌‌پایانی که با جهان دارند،  از جمله و در صدر این‌جنگها،  با خود مردم ایران جنگ دارند، سربازگیری کنند! تا نیروهاشون بزرگ‌تر…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6152" target="_blank">📅 11:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6151">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">تمدن اسلامی! تا زمانی که توی مدینه و مگه بود قادر به ساخت «توالت» هم نبود!  مستراح هم نداشتن !! اما دنیا در چه وضعی بود؟  ۶۰۰ سال قبل از تولد اسلام!  توی بیشتر شهرهای جهان  داشتن توالت عمومی! اجباری بود!   اینها میشینن روی منبر  میگن «مدینه فاضله»!!  حالا…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6151" target="_blank">📅 10:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6150">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">تمدن مصر باستان رو مطالعه کنید ابتدا تا انتهاش بر مدار مرگ بود! فرعون از زمانی که سر کار می‌ا‌ومد به فکر مقدمات مرگش بود و قبرش بود!  هنر و پزشکی و علم و مهندسی مصر همه بر پایه صنعت مرگ بود!  مومیایی و اهرام و جراحی پزشکی و….. همه برای کار و کسب مرگ بود و…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6150" target="_blank">📅 10:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6149">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T3q3XE8AlrompvY_hYgaNv2B70r5ue6QI_1BPb9ADSGWtyA0tnBex5BsfUNLzgVi_ztE4Mr6UomiuAiys0_Bzw2DqdMO1k1OU7a6NC3hvG6pgXCc3BecRL6uSEji8LfcSmrkv44K8-hpqjXmPpIJARplnlNFA_MpAMoeohpiYvsWvbavrF3yHZHj8CEj61Hh-LzjEbdJIrotlOcb-39NhaeydWPagAUi046SJr6o03Q7IgTN0rtMIkUVfoWwb2bX96soVi7VzOAveXsEEt_hFLGaXl_XWYP27l8LWV1SFuqRk1XwPKmZnPKNnDoPcwCJ0Bzl34Zk2GKMvrmUd_uKBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها شنیدید جملاتی با این مفهوم رو که زندگی و این حیات «زندان مومنه»!  آرزوی اینها مرگه! مرگ براشون رهایی است!  اینکه برن و برسن به بهشت و به زندگی!!  مرگ رو آرمان خودشون می‌دونن و زندگی و زیبایی‌هاش  رو پست و حقیر معرفی میکنن!  و اینکه باید دائم به فکر مرگ…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6149" target="_blank">📅 10:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6148">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">اینها اگه می‌بینید برای مدرسه میناب و…..  سر و صدا میکنن، فکر نکنید به این خاطره که «اصل زندگی»  رو دوست دارند. و از مرگ متاثر میشن!  تمام هستی اینها :  مبارزه، جنگ، کشتن،  کشته شدن و….. است!  زندگی براشون چیزی نیست جز  «مبارزه  برای عقیده».  و خوشحال میشن…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6148" target="_blank">📅 10:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6147">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b6d93f0a9.mp4?token=IvX6LVgLWvqFAwdaSjOSrE2Y7csFP2IqW_9RP5HRlZ-D-VEnC2TaMuFhrfYaBFgoocqIA188KWNI7QBdqdPAvAw9Dj3c6SxXXV74cx5ASwiN8wUTCIZvd-jN5fAqY-ihuB5X3SpL9KbZ2fBELOI-X5GhkM6ywevDcTyWFxKweu2W_76V9--ztO0lCF9qpuCJYbZAwh5RAYyDYpl2Vs2-oTlAG6brEpVSDZn7XmZiE9BUDCzYEKnrq_b-6L-TLUxUNwRR-rvU8Sw0ZKhfW5naBjoED9UtB9swVsNRCtZYnbzCx421VOjdXrv4uD1qoE8NFRTX6lgHGdye3y3IoqDFRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b6d93f0a9.mp4?token=IvX6LVgLWvqFAwdaSjOSrE2Y7csFP2IqW_9RP5HRlZ-D-VEnC2TaMuFhrfYaBFgoocqIA188KWNI7QBdqdPAvAw9Dj3c6SxXXV74cx5ASwiN8wUTCIZvd-jN5fAqY-ihuB5X3SpL9KbZ2fBELOI-X5GhkM6ywevDcTyWFxKweu2W_76V9--ztO0lCF9qpuCJYbZAwh5RAYyDYpl2Vs2-oTlAG6brEpVSDZn7XmZiE9BUDCzYEKnrq_b-6L-TLUxUNwRR-rvU8Sw0ZKhfW5naBjoED9UtB9swVsNRCtZYnbzCx421VOjdXrv4uD1qoE8NFRTX6lgHGdye3y3IoqDFRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6147" target="_blank">📅 10:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6146">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YzCZBLa-TVB85hIhfPcVIybMnTkHbWHJGOT5J1e8Bf_LlIdIqD9IEYOEVo-1rv2aInab7wNYHBZpqUCao0yJQk19LsNPNcPvojfSALnU8LPzA5D2o3xJkAa4b19Y7kAz1c8Z3iQeQGGSjoDNNv5Vjtm6HOGne3tZveAjOLZjUCwXySogr75Z37lbAHGJHgwzJAulsXDqJoLAnOWWK0T7lU72r4_L5ip-Lour8Ri_wc-YdrRe_UMwzTTN4sMbljIWQ_9ypF6R92ocGRx7W0RfEMrrmxT27NNKmFky8CeCCf50dBTZ_-Jl3-EWPMgruqTMpIF3AAELwmWExU3hQJIfwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: ایران به یک شهروند زن آمریکایی که در دسامبر ۲۰۲۴ در دوران رئیس‌جمهوری جو بایدنِ خواب‌آلود به‌ناحق بازداشت شده بود، اجازه خروج از کشور داده است. او اکنون در سلامت کامل در خارج از ایران است. ایالات متحده آمریکا از این ژست حسن‌نیت ایران قدردانی می‌کند.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6146" target="_blank">📅 09:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6145">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6145" target="_blank">📅 09:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6144">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">استاندار مرکزی : شب گذشته به دو نظقه در اطراف شهر خنداب حمله شد.
این برای چندمین بار است که اطراف شهر خنداب مورد حمله قرار می‌گیرد.
نه آمریکا دقیقا مشخص میکند چه اهدافی را زده و نه ج‌ا می‌گوید به کجاهاش خورده.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6144" target="_blank">📅 08:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6143">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">اطلاعیه  ارتش:  سامانه‌های راداری، سامانه پدافندی پاتریوت و مخازن سوخت آمریکا در پایگاه علی‌السالم کویت را هدف قرار دادیم.
‏ رادار‌های سوپر هاوک، تأسیسات و سامانه‌های پاتریوت واشنگتن در پایگاه شیخ عیسی بحرین نیز طی حملاتی، آسیب‌های جدی دید.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6143" target="_blank">📅 08:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6142">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
استاندار سمنان : به بخش‌هایی از فرودگاه سمنان حمله شده، کسی کشته یا زخمی نشده.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6142" target="_blank">📅 08:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6141">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RQj-NceOuJyX8mkgNM_5AJ42qAygwlFb7EOmXMCXe3P9FBxZoc84RkQRdP_caIOMsUPiXA6Td5l4K2ZcX4Gf2vpkVXaq2eEiEVTpQ5cJu34jJc3jbkWTEAPiVp-jV62he2TE1M6VFDevqSXjJ0cG8okyCsIN9Iwqc2zPhw0uoQz7qEsHSiwurSA4u7YjiGwb0zulbbDPtzf0OEInEUHPHSZUVtFcBV3Jwnrtiw8LdvHzhrLTc6WKrdyMwBJFqMpP_YxZV_vxqXrnqFOEGSrrUJFDzsoYXx3J61_WKCGOa17nb1OQPSguhsrq0cFeh56c7w_xxW_-QdKbVbZBDQmrpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین یارو خودش از دست سپاه و نهادهای زیر نظر خامنه‌ای  فرار کرده و به آمریکا پناه برده!
و آمریکا رو خونه امنی پیدا کرد برای زندگی و نوشتن از اینکه اسلام چقدر زیباست و خوبه و سعادت انسان رو میخواد!
حالا از همونجا به ج‌ا میگه مبارزه کن با آمریکا! مطلقا تسلیم نشید! تا انتهاش برید!</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6141" target="_blank">📅 08:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6140">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">برخی گزارش‌ها از تداوم حملات به اهواز خبر می‌دهند و اینکه تاکنون ‌۹  انفجار  مهیب در شهر شنیده شده.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6140" target="_blank">📅 23:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6139">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
چندین انفجار مهیب در چابهار و بندرعباس
🚨
کویت : امروز ۲۱ پهپاد و ۴ موشک شلیک شده از سوی ج‌ا را منهدم کردیم.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6139" target="_blank">📅 22:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6138">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای ۲ یا ۳ انفجار در اهواز</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6138" target="_blank">📅 22:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6137">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h3srQERU60us3XboKTGy6pXHW8hDmQBkpo7g4s8bbQRnT8ohY2s_1vghPmMNn8fD8eVlkX3jyYPAuyqYYb-Q6Ntb6fWGdfq5onZp-L00qhSIyCI11twAznACtHRfni9ygzZEr0L5pZVhEDSuKy8veDrKylLE_WXYFolDO2NOOwa2DifBeYb1DvyLL3oGIDFAUOTgH_Dr0DnUppDV5taHSQb9Mz230fwzNqIHGhKWEWMu0z58zqp12PbE1Ut-N9aLiDK20zv0u69RfbEWFc-5O2odBCz1Cl9WCSomKeB-C1ObN_bJEdUe2EN5KowfQAWkau08OYnLFH8gKAIF_Fl-1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شما دیگه جرات حمله به اسرائیل
رو ندارید! خودتون هم خوب می‌دونید!
این ۴-۵ روز هم به همه جا حمله کردید
به جز به اون کشوری که بیت‌رهبری
رو زد نابود کرد!
و نشون داد دقیقا کجاست که سست‌تر از لانه عنکبوته!
ولی هر چقدر دوست دارید شعار بدید!
اون حزب‌الله تروریست هم رفت انتقام بگیره  هنوز و همین امروز هم نیم میلیون نفرشون  توی محله‌های مسیحی و سنی لبنان آواره شدن!</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6137" target="_blank">📅 20:39 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6136">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">آنچه شب گذشته در بمپور رخ داد و موجب  کشته شدن تعدادی ای نیروهای ارتشی شد، قابل اجتناب بود.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6136" target="_blank">📅 20:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6135">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20e615d142.mp4?token=gJEjwgWXIAWXaf_XSnGV-frc9O579_veg5vGvTnehH1WymRwL3fIzolkEZckCt6k70ZBLvlVlqxXjSQUIkHVD5Ewo7FPIMnfWT87oMqXN5at_tM016JmeDmSbvkfz18YOM2KM7nuI-erKPWcyAJdTxYI-Tmw2N4W9qYT_8bb-qIZ95V6sAwWlKCxIDqzcR_TIXFPjMVvbIO0YjfMrmGXngzPG9RGY6GPNK_jADrcUKWqW9QSxO522QWPdhkGnXT7lQ0hlAhCbi5cjWDxXSKpGVzkdSOapV7zrJbTAESh_vOTt9MigfuYO4FpjWbjUKrVTHXxHx95CXsL7XEUMg-YZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20e615d142.mp4?token=gJEjwgWXIAWXaf_XSnGV-frc9O579_veg5vGvTnehH1WymRwL3fIzolkEZckCt6k70ZBLvlVlqxXjSQUIkHVD5Ewo7FPIMnfWT87oMqXN5at_tM016JmeDmSbvkfz18YOM2KM7nuI-erKPWcyAJdTxYI-Tmw2N4W9qYT_8bb-qIZ95V6sAwWlKCxIDqzcR_TIXFPjMVvbIO0YjfMrmGXngzPG9RGY6GPNK_jADrcUKWqW9QSxO522QWPdhkGnXT7lQ0hlAhCbi5cjWDxXSKpGVzkdSOapV7zrJbTAESh_vOTt9MigfuYO4FpjWbjUKrVTHXxHx95CXsL7XEUMg-YZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیش بینی تاریخی بختیار
در دو کلمه، برای مردم ایران</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6135" target="_blank">📅 20:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6134">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/296fa239b5.mp4?token=Wvf1vrqZIlYI1eoSDjBfeaEkok3AViCCgYtDAmULxu1K5ATa5uiUzjb4RQBIsOUFyKFnqvu4PfaIPj8B7ZxpV_NdUZ5ZaDt3zv6AMujRLW-bpW1LUkID8o5RnibdsvP3uL0nvjMPO_ToU4vpP2ERMIm978zj_AAkrokTv5ZrdovRT15YyN5pnd05lpaTNUSA7PqVjDwXlJsI7No1aB43mZNLmAxv6wa1us25DQ4rPV8QfrF82FJFvY5nSEGU44Tgj0FjB5ZSWrrBKh2u4EMr5LBYNsqjb5E4tKDIEVK0uIgaZckmsuemLA1DCZ6WQ1H9wj0JCS3Auxnw-kD4AHgbwYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/296fa239b5.mp4?token=Wvf1vrqZIlYI1eoSDjBfeaEkok3AViCCgYtDAmULxu1K5ATa5uiUzjb4RQBIsOUFyKFnqvu4PfaIPj8B7ZxpV_NdUZ5ZaDt3zv6AMujRLW-bpW1LUkID8o5RnibdsvP3uL0nvjMPO_ToU4vpP2ERMIm978zj_AAkrokTv5ZrdovRT15YyN5pnd05lpaTNUSA7PqVjDwXlJsI7No1aB43mZNLmAxv6wa1us25DQ4rPV8QfrF82FJFvY5nSEGU44Tgj0FjB5ZSWrrBKh2u4EMr5LBYNsqjb5E4tKDIEVK0uIgaZckmsuemLA1DCZ6WQ1H9wj0JCS3Auxnw-kD4AHgbwYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی که فرمانده سپاه بود و سالها فرماندهی جنگ رو بر عهده داشت
اینجا میگه مطئنم که مسیری که در ذهن مجتبی خامنه‌ای است، بهتر از مسیری بود که شورای عالی امنیت ملی رفت.
مجری ازش می‌پرسه خب اون چه مسیری بود؟
میگه : نمی‌دونم ! نمی‌تونم که ذهن خوانی‌ کنم!
فقط می‌دونه خوب بود :) یه مشت چاپلوس !</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6134" target="_blank">📅 16:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6133">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVahid Online وحید آنلاین</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mB8Uocmo9ZVawfnFUKXkWAkEaghfjHggZDpZghM-puz3eWu03mmmX9Pz4dxEVhT6qAJYEP2RxvbTTDF_C-9vT1pqnRaOMy9GYTzgiOAnAdvpHS4Jcmt2asyPYk6xIWzaqmivxmCTSj5O-ALPSpU2Ky69lKSml_wmVNmFA9xAXu9ONl4vWFSgNtZRC9_GDRFa9aaKtp6Q0FlQ8dqON7Msv67tet5sLbR8a32hjZW4DKUoTU4qKV3d3CmGrihTRjS7nsz9R52D0-JmOAcstUWD9ZXDlxXWhCBW_YUHT2nsEYD0MhGu3N1MA90W2sb9J6scXb_cbX2NZrp2CUAB9erodA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
سنتکام : به تنب بزرگ حمله کردیم.
در جریان این موج ۹۰ دقیقه‌ای از حملات، با استفاده از مهمات هدایت‌شونده دقیق، سامانه‌های دفاع ساحلی و محل‌های ذخیره‌سازی و پرتاب موشک‌های کروز در جزیره تنب بزرگ را مورد حمله قرار داد.
این حملات توانایی ایران برای حمله به کشتی‌های تجاری در تنگه هرمز را بیش از پیش تضعیف کرد.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6132" target="_blank">📅 15:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6131">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">حمله امروز به چابهار</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6131" target="_blank">📅 14:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6130">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
ارتش: «آمریکا بامداد امروز با شلیک ۱۳ فروند موشک، آسایشگاه و محل اسکان یکی از پادگان‌های نیروی زمینی ارتش در بمپور را هدف قرار داد
دشمن به مهمانسرا و اماکن نگهبانی پادگان حمله کرد
‏ ۷ تن از کارکنان پایور و وظیفه تیپ ۳۸۸ ایرانشهر شهید و تعدادی مجروح شدند.»
‏</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6130" target="_blank">📅 14:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6129">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
سنتکام : از نیم ساعت پیش موج تازه‌ای از حملات را آغاز کرده‌ایم.
(از  ساعت ۱۳:۳۰ تهران)</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6129" target="_blank">📅 14:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6128">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xx0DIMicev4i1vFGxvI31sEL07guluXPclSTdrvbzInMRobalawOGmqGpzGV9OwraLPIHevt3XpHsW4Ho4KwTwymBE5Wn2eSiqBZkLUQ9RflLGJbZdd5czMrn6_R1WkdDLWON7CZa1afP_LlTK4vOct5eI814AOo-yW4d90_U0oKfXoVFeLvvQkNrMWUu0OutTj4OgG4TJazTXImbq3I0auh40sNkM1LMr6y4ICmGVXV4PvD-jj7dAWefRVlRDOMeqsLkfKOGGIci5gve4PNK-Bg0leLmJOc2-0crnyrTRIHm0eLtBk7Y7u5LXykZ4N8WZhVeLPKzVt0qMKHffwdLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قابل توجه ساختاری‌های محترم
مدیر حوزه‌های علمیه با بیان اینکه مسئولان باید تفاهم‌نامه‌ها را پایان‌یافته تلقی کنند، از دولت و شورای عالی امنیت ملی خواست به دلیل بدعهدی طرف مقابل، مسیر مذاکرات را متوقف کنند.
مشکلات اقتصادی یا ترس از آسیب به زیرساخت‌ها نباید موجب واهمه مسئولان و رویگردانی از مسیر «جهاد و استقامت» شود.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6128" target="_blank">📅 13:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6127">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd0a98053a.mp4?token=HwLBfPMBd2hfBuYzkJx6UHhy-TTbwKwP3N_vZ-6CSix-l1m4iDMHnbqx8YSA-Y8BeRh5Af1RD0vQ2NeKPHZH_YgtxWds_VSGp2fqsMhF1F50W5iHwcNo9c3DmN_gDC_eWCipZwc8B_JMFuYVDXOW1beHFOSAukt7nQsSzGwCsYwMxFoVZ0Jop6SnNEGfrctf9pNwCv29pVBsQIfUm2BAn0j6QH_HvZbdaNsxGlrtm5pMCxEvizTysTqu9Na1rePpiEmDBl-g-SYXf156UTJ1qrdqAGnBFMb5zL6acJpbeCbXY0-DKxLlFNOhAMbUxdwgrZldetgQUHurqw8f8Oz7f1c1Cax7_RoNE7fNmXLtZHuCOJKfB-vacPUQJVqgFaVNiP8b3PFdkCNeQIL0Dl7zqmZLIz-ijpQldapnyOa9KYZCUtzvqVki2ZJb_DGDPlg0Ju-necxnmhOqHiHhqqafn8KBNjQec1XzLzKU7ulnlVKiI0THsBMnbC6by8ewhm1RD74oKlqBZiwqYFKYqq9vCM_jCq1yYwQul9yP6qMhaRrQeeWMInJ8eSeYOEO75Br8SMOaiHzv_gMABY0LzvLQngtpsh6YvekIqJsocofhX2VmDqOVu5N4rbZ6SrazmACJeawyde_FW9ydNgixtnT-szI2bhNcVVpC0WMK-kbzj64" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd0a98053a.mp4?token=HwLBfPMBd2hfBuYzkJx6UHhy-TTbwKwP3N_vZ-6CSix-l1m4iDMHnbqx8YSA-Y8BeRh5Af1RD0vQ2NeKPHZH_YgtxWds_VSGp2fqsMhF1F50W5iHwcNo9c3DmN_gDC_eWCipZwc8B_JMFuYVDXOW1beHFOSAukt7nQsSzGwCsYwMxFoVZ0Jop6SnNEGfrctf9pNwCv29pVBsQIfUm2BAn0j6QH_HvZbdaNsxGlrtm5pMCxEvizTysTqu9Na1rePpiEmDBl-g-SYXf156UTJ1qrdqAGnBFMb5zL6acJpbeCbXY0-DKxLlFNOhAMbUxdwgrZldetgQUHurqw8f8Oz7f1c1Cax7_RoNE7fNmXLtZHuCOJKfB-vacPUQJVqgFaVNiP8b3PFdkCNeQIL0Dl7zqmZLIz-ijpQldapnyOa9KYZCUtzvqVki2ZJb_DGDPlg0Ju-necxnmhOqHiHhqqafn8KBNjQec1XzLzKU7ulnlVKiI0THsBMnbC6by8ewhm1RD74oKlqBZiwqYFKYqq9vCM_jCq1yYwQul9yP6qMhaRrQeeWMInJ8eSeYOEO75Br8SMOaiHzv_gMABY0LzvLQngtpsh6YvekIqJsocofhX2VmDqOVu5N4rbZ6SrazmACJeawyde_FW9ydNgixtnT-szI2bhNcVVpC0WMK-kbzj64" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سفیر اسبق جمهوری اسلامی در روسیه: مطمئن باشید اگر ترامپ را بکشیم نه تنها هیچ موشکی به سمت ما شلیک نخواهد شد، بلکه عقلای آمریکا با خوشحالی جنگ را تمام خواهند کرد.
کشتن ترامپ هیچ هزینه‌ای برای ما ندارد و با کشتن او جنگ هم تمام خواهد شد.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6127" target="_blank">📅 11:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6126">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">جلسه اتاق وضعیت برای بررسی حملات گسترده‌تر آمریکا علیه ایران؛ آیا ترامپ آماده تشدید جنگ است؟  به گزارش اکسیوس، دونالد ترامپ، رئیس‌جمهوری آمریکا روز سه‌شنبه برای گفتگو درباره عملیات تهاجمی گسترده علیه ایران جلسه‌ای را با حضور مشاوران ارشد خود در اتاق وضعیت…</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6126" target="_blank">📅 08:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6125">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VojhVPGrgxUnAfzyfMFRHcy24DZ9bDUNlQXCqI4whH17UCfIfjjB1BXScT-aIHbZAgSg7_TMyvXplBMZl57Bf3NcTGP_STPzTo_b5RMz5EuffbQ-kKU4koys10qNB7qhMVVIW7DKTiafmLCF1fPZ7P7Y-rEmCTa9A-jFvGFwieXPYQWy3db1tCpjJekH5X5Z5y425cdENiIMHbLqG03jo65eKGFMsGhwJQPquWggx6g1o3yseZePojFWrVmyNpGpayabZSHKS3eleD5Wse33DLUceZPtzh_28Mmqohat-fhWkBJSTkBy1NUHcBdEPO5inhpKc03XPVYgMlpATT_-lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلسه اتاق وضعیت برای بررسی حملات گسترده‌تر آمریکا علیه ایران؛ آیا ترامپ آماده تشدید جنگ است؟
به گزارش اکسیوس، دونالد ترامپ، رئیس‌جمهوری آمریکا روز سه‌شنبه برای گفتگو درباره عملیات تهاجمی گسترده علیه ایران جلسه‌ای را با حضور مشاوران ارشد خود در اتاق وضعیت کاخ سفید برگزار کرد.
به گفته سه منبع آگاه، در ابن جلسه که ارشد‌ترین مقامات نظامی و امنیتی آمریکا در آن حضور داشتند در خصوص گسترش حملات صحبت شد.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6125" target="_blank">📅 08:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6124">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bd4825a45.mp4?token=aEExiIsY1Ihv4h6-lLp_NksQyzRwuebf0RxZZeY7VF55zRnbG4ljpTAC6qZM91O5-sitamGjC1EdCo9JWgcQzsLuRgeoiE0TtAkQPWsR-htVP4qeIAwPeshtmWXRqjE7wNKt-7HLcTvsKhL0O6snqPFwuEjkWcVJQpDYwwj-LpTQJLAqQHihpDpO43_LiJUNxubcINxKiOhl7jMC4CVru1hxPAXamcXPEXDiBHfD2FbtazKyDXFJuVQWAdlFEDn-i2lH9elNlfGuSt65TPO7I-n582wNseqwtWLjJtktrI3fpkqBYVV-RIjy7mt2gPStM5oyHtJI_rXXLH4xG-EjcC4sxCLPN8phhV1iZVmwT7LnXcMJTR4rO2FgHaKeJ-VyMOuL2fY_PtyE44GpOYh4HMfgw_AksnySAUsywfKYH7D9yBYNsc1eOXDJBukM8Lou3MLZq9xwEIBoluNn_j5Nia9-FwiDr9VUk8oahjkr2ju_pLOVB9OCM_PprylkR5S29e6RaKIlwRHgstD1_iP9MdROD7yfcCBSt75EqyflptRFF8T9fQapoZBQ2gkVc23XQcJU2byM2i1n96Q5_w4cUuFQNg12b0UMZbcG58jd1Ld-O_II7sgr1r2eIt7j8pU9gedsiLkxvb2k5JjsXF1_oRsg7ZwsrhsOUUshN4qZMqY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bd4825a45.mp4?token=aEExiIsY1Ihv4h6-lLp_NksQyzRwuebf0RxZZeY7VF55zRnbG4ljpTAC6qZM91O5-sitamGjC1EdCo9JWgcQzsLuRgeoiE0TtAkQPWsR-htVP4qeIAwPeshtmWXRqjE7wNKt-7HLcTvsKhL0O6snqPFwuEjkWcVJQpDYwwj-LpTQJLAqQHihpDpO43_LiJUNxubcINxKiOhl7jMC4CVru1hxPAXamcXPEXDiBHfD2FbtazKyDXFJuVQWAdlFEDn-i2lH9elNlfGuSt65TPO7I-n582wNseqwtWLjJtktrI3fpkqBYVV-RIjy7mt2gPStM5oyHtJI_rXXLH4xG-EjcC4sxCLPN8phhV1iZVmwT7LnXcMJTR4rO2FgHaKeJ-VyMOuL2fY_PtyE44GpOYh4HMfgw_AksnySAUsywfKYH7D9yBYNsc1eOXDJBukM8Lou3MLZq9xwEIBoluNn_j5Nia9-FwiDr9VUk8oahjkr2ju_pLOVB9OCM_PprylkR5S29e6RaKIlwRHgstD1_iP9MdROD7yfcCBSt75EqyflptRFF8T9fQapoZBQ2gkVc23XQcJU2byM2i1n96Q5_w4cUuFQNg12b0UMZbcG58jd1Ld-O_II7sgr1r2eIt7j8pU9gedsiLkxvb2k5JjsXF1_oRsg7ZwsrhsOUUshN4qZMqY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مزدوران حکومتی شعار میدن
«جنوب ایران نکند جنوب لبنان شود»
عجب! شما دیگه چرا؟
خامنه‌ای میگفت «جنوب لبنان الگوی پیشرفته
و موفق مبارزه ایمانی است»! سالی یک میلیارد دلار از اموال ملت ایران رو میدین به گروه‌های تروریستی اونجا  و تبلیغ اینکه ما اونجا پیروزیم و …..!
ولی ظاهرا اسرائیل در جنوب لبنان چنان درسی بهتون داد که الان خودتون هم میگید نکنه بشیم شبیه اون «الگوی موفق»! معرفی شده توسط خامنه‌ای</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6124" target="_blank">📅 07:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6123">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0378588a4a.mp4?token=G3FkOFQM6VzcrLb8wjtnuGpo0725nKQk-MjtTZXT2nZdqUVykbzctO-uQ-9AH3smrQnGryPPYTHU0uRBHKZ7Zn1PfkqznUSYxre2hlzN0kahwGaL5HQVak8ttrrrQnMHvFHJ3sTYH8kLsOhl5zpt5jkD4hfsZ81_VPWZTxJX8m2UMAcbnghfKTJ9ylwbNZ8YM3BLJ-oc0w8RTEmOTIikfKgnpdMzksxLWu3hBZ7Ex8i4yNmpnQxGerhFkBowHY2o-m6EbIEFJy1M71lZlDO4ia9l8nmVpC7YXaknhMZ2kZAv4Y3MmPrBvkoN9pXGjNm0v9s3_Dc7TSr7t509_XTmFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0378588a4a.mp4?token=G3FkOFQM6VzcrLb8wjtnuGpo0725nKQk-MjtTZXT2nZdqUVykbzctO-uQ-9AH3smrQnGryPPYTHU0uRBHKZ7Zn1PfkqznUSYxre2hlzN0kahwGaL5HQVak8ttrrrQnMHvFHJ3sTYH8kLsOhl5zpt5jkD4hfsZ81_VPWZTxJX8m2UMAcbnghfKTJ9ylwbNZ8YM3BLJ-oc0w8RTEmOTIikfKgnpdMzksxLWu3hBZ7Ex8i4yNmpnQxGerhFkBowHY2o-m6EbIEFJy1M71lZlDO4ia9l8nmVpC7YXaknhMZ2kZAv4Y3MmPrBvkoN9pXGjNm0v9s3_Dc7TSr7t509_XTmFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه محلی «حال وش» از حمله به آسایشگاه سربازان در شهر «بمپور » در استان سیستان و بلوچستان خبر می‌دهد و کشته شدن ۱۰ سرباز و زخمی شدن ۱۵ سرباز</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6123" target="_blank">📅 07:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6122">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5b6a441ee.mp4?token=DKjN9v316uMcb1y5QpxEKmyDqt8XMt5EZBlEIgTVLp9h1hLToab1eFiKjpCXesjmcH2N4WlpLdv8xG1Qwrdm4-ehxrQsheS6VCgJIQXRyidspPFqBE-M8hXCCdDXoEKGBf5lPevbs178F7g6x5uKpgpBBQHak1drCfz0RmWpUmdVsDpsMnLAbypEI_Mv_q6KmxI1U4gOo29U-2k3hUu-m2RfMEfo1rtkq_jrrD6fnnOVgaK69YKndIXUkUXTxRauYxLP4farbLic0JI8k3tmFI698DrArEprJA3_PZZFlJ7utu1bptm_zctvmRX84gcFmRoAyfPuvT-fAbDOD5gkZHsnE6yVNMmQuedUv8WR9nIlMLzXzhpqJgeiR-Szjr7kNMUKsTA9mKDBVJZieV_Usa3KRmtnUwIYsCqiH62m0zvnrFyp7_DEppQjQgBHRNZvyJADkd7g1snHtKzDhVKbJKw-6vjb7HM_DSyDVkLMcrqjd2q-gkU05swMNR9j3wDho7DxoyD_j7hERtN956u8ra5jbMzXIpdAfhRYpoEwxPoqiFm8NS1VL6GgVTBw_aE6qDTnwl-HyJKhXF_U47C0VWMiidNiiiS-XZDA_TkYWcJHUAZCVo2lndBMEifk1XnuFJ3NEeHHP_66uC0hXi_QCdlvFyJaA-qcPn4AvpjlU2E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5b6a441ee.mp4?token=DKjN9v316uMcb1y5QpxEKmyDqt8XMt5EZBlEIgTVLp9h1hLToab1eFiKjpCXesjmcH2N4WlpLdv8xG1Qwrdm4-ehxrQsheS6VCgJIQXRyidspPFqBE-M8hXCCdDXoEKGBf5lPevbs178F7g6x5uKpgpBBQHak1drCfz0RmWpUmdVsDpsMnLAbypEI_Mv_q6KmxI1U4gOo29U-2k3hUu-m2RfMEfo1rtkq_jrrD6fnnOVgaK69YKndIXUkUXTxRauYxLP4farbLic0JI8k3tmFI698DrArEprJA3_PZZFlJ7utu1bptm_zctvmRX84gcFmRoAyfPuvT-fAbDOD5gkZHsnE6yVNMmQuedUv8WR9nIlMLzXzhpqJgeiR-Szjr7kNMUKsTA9mKDBVJZieV_Usa3KRmtnUwIYsCqiH62m0zvnrFyp7_DEppQjQgBHRNZvyJADkd7g1snHtKzDhVKbJKw-6vjb7HM_DSyDVkLMcrqjd2q-gkU05swMNR9j3wDho7DxoyD_j7hERtN956u8ra5jbMzXIpdAfhRYpoEwxPoqiFm8NS1VL6GgVTBw_aE6qDTnwl-HyJKhXF_U47C0VWMiidNiiiS-XZDA_TkYWcJHUAZCVo2lndBMEifk1XnuFJ3NEeHHP_66uC0hXi_QCdlvFyJaA-qcPn4AvpjlU2E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا میبینم راست میگه …</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6122" target="_blank">📅 07:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6121">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U-CygOy99SBaZy3xEtElCcLZKWRFKR0vM1-DiKrzegFY62h3GAbH6RL5Wil_le2lSdRjA4jPrHHkel9-7ZJptiASeKFroOU18yDdENBNDlEMRJY-yl_MjqAE9ayn6c20r7VZc_mG1h9iu0q0q2AM-vlXidPW11nA3rnywe9rjgW4RaCBMTdES-1NdRagCwUyox4aFHCbdtlzqr-CNhzPVs1pYt8O2bGfmitRCPVW6YHroovn0D_0l1Sn0-89hC3gFqf6n6BVbxFzHrMnfxFMo2kvX6HZhmDrzhBU_kO1DFrw6VAQ790bpe4PciEiwY_M6F59urCN4DturCYBAn9WEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6121" target="_blank">📅 06:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6120">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GoB2m00jtgh31ruqp_PV7B3QtIGpTUmDteugziImZ5tYp2CW3UUyO3pd4EMavM-5uOzuaLH49-EaiN_BDTB4983zYUo_Z4gpaMwIPOnwQrvsq64ASPZafmBsT9-_dJYw_EgX5D4BRHor4PfWmU99zASJf1_ajrbsqhMbwdfvCjHWkMgWJxFI6W13qrW595-ry69aoewwEMxgrz7whoLO6jZlP7Hbo-f2AXJmmEWCxULztMAmxPjM37lHEhnWJTluk-4Gn24I7yBz0iDVPWB6KiJrduJ50tlL3bt-wDEU0NDn6NThZvrotlU_PCYlHRniHpFgJW5OZA4WNrnwsO-bhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه محلی «حال وش» از حمله به آسایشگاه سربازان در شهر «بمپور » در استان سیستان و بلوچستان خبر می‌دهد و کشته شدن ۱۰ سرباز و زخمی شدن ۱۵ سرباز</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6120" target="_blank">📅 06:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6119">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba02e5e863.mp4?token=JZw0wqXDvqf6L1oJPrV_PTaguVajCD7OB6GIwKSaFD6fqwbloGf0use24v2WWQ_yBQV-ISAuhS9LDPmxpMwW4iWnIhYMl66TQr49IstEpkb1wTuwsuW62Yc8GAGjpSkhN0k3v9WESwMmgYwL50Dc2qGHNxLL82cFLNsRt9XwUDNILRFHvRdJEWcsAx8YssJ3MTbne81d6QSxObp7R7spI0TS1NYeq7c30ODHBYUeqbxO6hdAPbnXOYN5_A_tH1YcJzns-OGduyYbg1LKCZUNMHqb0zib_LR21hnKfp8pGPhP_RmdmquzCPIiFX2tz5M3h5My-djTKi-7Lc4yKhGh7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba02e5e863.mp4?token=JZw0wqXDvqf6L1oJPrV_PTaguVajCD7OB6GIwKSaFD6fqwbloGf0use24v2WWQ_yBQV-ISAuhS9LDPmxpMwW4iWnIhYMl66TQr49IstEpkb1wTuwsuW62Yc8GAGjpSkhN0k3v9WESwMmgYwL50Dc2qGHNxLL82cFLNsRt9XwUDNILRFHvRdJEWcsAx8YssJ3MTbne81d6QSxObp7R7spI0TS1NYeq7c30ODHBYUeqbxO6hdAPbnXOYN5_A_tH1YcJzns-OGduyYbg1LKCZUNMHqb0zib_LR21hnKfp8pGPhP_RmdmquzCPIiFX2tz5M3h5My-djTKi-7Lc4yKhGh7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام فیلمی از حملات خود به ایران منتشر کرد.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6119" target="_blank">📅 06:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6118">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b9746249d.mp4?token=lCHh_u_UwW7ytAnbnT4QB4huzt63ewvo71YwEPmOtuCYh6eFSxxbnM4E_HUi_xhaaLhVTIWXhcYyKpf2iToWdZ6XB8VLieaoPC0whwYwFgAO4RVPkBjwbGjYnd2t_jWftstsPAkQEUt1p0baWMbHGv_4Z3XbzxsiBPTRBtQKI2A4KhM6FJD4SJ70r1tUhH_9p-O4qWBfLkLw1L9dykFjdhTenfw-ektOKUfyI4HchKUcavOcb7gBU6UmaJE_QNZHRptCK7gVbvCD9EFaPu4M7GCD0r9tR2qP_96I1JmqqffwIwJ45GDtCgk6PV4fqhqXQZCcDVP1A4z-KCGFbD75QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b9746249d.mp4?token=lCHh_u_UwW7ytAnbnT4QB4huzt63ewvo71YwEPmOtuCYh6eFSxxbnM4E_HUi_xhaaLhVTIWXhcYyKpf2iToWdZ6XB8VLieaoPC0whwYwFgAO4RVPkBjwbGjYnd2t_jWftstsPAkQEUt1p0baWMbHGv_4Z3XbzxsiBPTRBtQKI2A4KhM6FJD4SJ70r1tUhH_9p-O4qWBfLkLw1L9dykFjdhTenfw-ektOKUfyI4HchKUcavOcb7gBU6UmaJE_QNZHRptCK7gVbvCD9EFaPu4M7GCD0r9tR2qP_96I1JmqqffwIwJ45GDtCgk6PV4fqhqXQZCcDVP1A4z-KCGFbD75QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : امشب، فردا و فرداشب به سختی به آنها ضربه خواهیم زد و هفته آینده پل‌ها و نیروگاه‌ها را هدف قرار خواهیم داد، مگر آنکه  مذاکره کنند.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6118" target="_blank">📅 06:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6117">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caeb092620.mp4?token=MX051ItliUeJ0VDiPNlOLmZJzghrDNdPJPmYJDY7HxjCXfkjxA3QjVqKsLmGuL14rw1TD8bUq2DcscsSnqqD3qx7CezNnIdEIQ5WZpGDkuJ8nO22agARqbvyyTH2c4Wade1f85i7zmEUN11pAzpAeQQZ_RArGy4zcfdJWpt4YBizVc3Poa1n5gfb2jNVKpbTUiqkOI8ptMngB2RGkPZIAiMDUlOv-rwSuO1JC3I_NNLG-NdtgSc_Y4Pxb3yEhiZFvy5SMmgwJi6pZJbAC94o9VtJUyNc9ozQTTt4f1n9QuDI0qrebf3_eWW6I0-2pib3SFsaj1gGN5-lUSqMzQ6ayA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caeb092620.mp4?token=MX051ItliUeJ0VDiPNlOLmZJzghrDNdPJPmYJDY7HxjCXfkjxA3QjVqKsLmGuL14rw1TD8bUq2DcscsSnqqD3qx7CezNnIdEIQ5WZpGDkuJ8nO22agARqbvyyTH2c4Wade1f85i7zmEUN11pAzpAeQQZ_RArGy4zcfdJWpt4YBizVc3Poa1n5gfb2jNVKpbTUiqkOI8ptMngB2RGkPZIAiMDUlOv-rwSuO1JC3I_NNLG-NdtgSc_Y4Pxb3yEhiZFvy5SMmgwJi6pZJbAC94o9VtJUyNc9ozQTTt4f1n9QuDI0qrebf3_eWW6I0-2pib3SFsaj1gGN5-lUSqMzQ6ayA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار ناشی از حمله پهپادی امشب سپاه به کویت
گفته می‌شود مخازن سوخت ارتش آمریکاست.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6117" target="_blank">📅 06:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6116">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/360d24e506.mp4?token=aI_R-ngW3Lod5Y3bTDPg-D7qkJ_nuZysAo88s0CJMEApj8pVkSlTGGSG3HZeydkH2CJ89cisueptGHjoXzjz0l-zKrfEx0zSmVViD1d6BHGA-Ue9Yupx2_snyNhxHDXXGwjgfnsO8xD1YYoAeC5KRL7KZ0OfUSmgMWunxmO-k-dJsuqE96gjjCr2JE4ALm3uKVFZ3zkirUNcoeIabimEBCn9wBb_yqBj8weobHhmtkcvcDkmxUpfvRe8OnBNO6Xg5pWiycsUrP-8g3a2d2fZ3Y9mk9mMxdozMk53GSVWaxNwGWiqVOE7zWfUtObbBlP4MqqkP06sGifhmkTm4nQ3kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/360d24e506.mp4?token=aI_R-ngW3Lod5Y3bTDPg-D7qkJ_nuZysAo88s0CJMEApj8pVkSlTGGSG3HZeydkH2CJ89cisueptGHjoXzjz0l-zKrfEx0zSmVViD1d6BHGA-Ue9Yupx2_snyNhxHDXXGwjgfnsO8xD1YYoAeC5KRL7KZ0OfUSmgMWunxmO-k-dJsuqE96gjjCr2JE4ALm3uKVFZ3zkirUNcoeIabimEBCn9wBb_yqBj8weobHhmtkcvcDkmxUpfvRe8OnBNO6Xg5pWiycsUrP-8g3a2d2fZ3Y9mk9mMxdozMk53GSVWaxNwGWiqVOE7zWfUtObbBlP4MqqkP06sGifhmkTm4nQ3kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی با موشک‌های حاوی بمب‌های خوشه‌ای به بحرین حمله کرد.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6116" target="_blank">📅 01:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6115">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
ارتش : به پایگاه‌ها اف ۱۸ های آمریکا در اردن حمله پهپادی انجام دادیم.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6115" target="_blank">📅 01:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6114">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">‏امشب اتفاق جالبی افتاده، به محض اینکه خبر انفجاری در شهر و استانی منتشر میشه، مسئولان جمهوری اسلامی سریعا مصاحبه میکنن و میگن دروغه و همه چی آرومه!
‏اینطوری مثلا میخوان صورت مسئله رو پاک کنن.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6114" target="_blank">📅 01:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6113">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rTGVPAk1mv06n7Qj8z2q9AjroTJBbARP_IxChEiBrSbFX24zaDbXD4jQwJcQtC7P87T291aVLhy4Oz1LVT6ssqDViiZA5btsHvm73PKX4EDrSAcchq061Lzf78iCII7CxK0F6jz0n611uZysDHP_157-PSQ4roRPPsWRILhtqCJ085auiuYDRfVWDoWiG-oymZbqPk-0G9XLBe1-cs4V44sNtD3RY0ofWSwtHZrU2LGMU4UD4tyxiPYrpwtihbesWcETsfGugiPnoqhVzBNVv93_9nxF2eOsHQdBXCzsGcpotj7Y0om-OEiMF2h73xUbrAfr5KzFlZgaj4a3ZeU-kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگارهاشون می‌نوشتن که کشتی‌ها دارند  از مسیر عمان رد می‌شوند، تشییع جنازه،  بریم و کاری کنیم که  کشتی‌ها مجبور بشن از آبهای ایران رد بشن  و شروع کردن به حملات به کشتی‌هایی که از مسیر آب‌های عمان میرن.  به زور حمله میگن کشتی‌ها باید از مسیر ما رد بشه.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6113" target="_blank">📅 01:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6112">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZS0kOXZneaBt-J-5HQNxmOa2qs_4xj-UUtwoZ0QG3ginMGxaWVXlgko73E5S2AR5NJOxAIkqHqu21QJZMli7vy7nJJN927BBVOLBgNgSWA2SYl1byKLYLUBXgiwCoJDAEQaf_58yd2XU1-QvNq5Gy2vuhZE5Ve2nKM_bXNRHfSI2ieFsgoksgGE57ZW6XLvuPMcFZsUKzne_f5ipMQ3H0ctDDlFYVNRwndygnBA9Rf6CWrEf3KfdBhr4jYbFGdRGlg5gW3wbl0kj-lVwvqJASJqSEEfw2ZtAG12lmsYLxAh-v7ABOXtxkHtNUsUedYkcuZIZj37O1p_zS7tbGPKDFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینجا در حاشیه خاکسپاری جسد خامنه‌ای و جلوی قالیباف شعار میدادن «مذاکره با دشمن خیانت است»  هنوز به سه کشتی حمله نکرده بودن و نزده بودن زیر تفاهم نامه</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6112" target="_blank">📅 00:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6111">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d90d3d98f9.mp4?token=E8z4upNE0QtG1IeS5quNejHNFJVaFuGDvea51BZNbHRbX-RwO_hBuNzK4Onxus7m68tJm6sXyZ-kX_niJE9552p5fa-tbWtSGCGt_SqLPblthq2zxEHJmjJ0SArW3av7-bnoWB7tqgLCG-IU7iDMc_w-YkMiKtzoH04qAciLybEvFWwheO5BYcrHhjZYpvDH_u5gaqhvd35MVZU7Jh2jkSaW_sMQjgyRfFfRTPmQBpolIPQpVKID4ugClDxOQHCv1VqVFI-Amdej5zdxVFpThchej1oSEqb-yoUqKvjqq4SBkWL2xR-s6BxWMISzMxAHCp0zwvjv4Mgli3WNK1hD9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d90d3d98f9.mp4?token=E8z4upNE0QtG1IeS5quNejHNFJVaFuGDvea51BZNbHRbX-RwO_hBuNzK4Onxus7m68tJm6sXyZ-kX_niJE9552p5fa-tbWtSGCGt_SqLPblthq2zxEHJmjJ0SArW3av7-bnoWB7tqgLCG-IU7iDMc_w-YkMiKtzoH04qAciLybEvFWwheO5BYcrHhjZYpvDH_u5gaqhvd35MVZU7Jh2jkSaW_sMQjgyRfFfRTPmQBpolIPQpVKID4ugClDxOQHCv1VqVFI-Amdej5zdxVFpThchej1oSEqb-yoUqKvjqq4SBkWL2xR-s6BxWMISzMxAHCp0zwvjv4Mgli3WNK1hD9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این استوری رو ۶ روز پیش گذاشته بودم  میگفتن آمریکا میخواد آتش بس حفظ بشه ولی جمهوری اسلامی باید «کار دیگر» بکنه!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6111" target="_blank">📅 00:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6110">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/550f13e765.mp4?token=jLcE2KQ_abePkPmg6mXpgNNX7Y1KHwy-nwzafmjS-sYdiP6Vlx4aH3HCHVG0fLCVfAEev6gypY0MLX7S7yumaeprCxEqMxhC-4ECcHT0YPrbBTZs3nndSyhHR75bIAoKKMuBoEvj2cH7c44fM-hGwHf6-CVk8HykyKK0E3hGyiQFU6Aj6zRL8ERG7THDsOiL0ZKRxqCQuUvVnc_hR_OdQK1D3OyfjOe4SjMkgHGBX_MLXgsWyIOV8iTa2cgiDm23a7kDQph74i_Hg4subByB7BZsDMQF_lfOxZ6SIIaI0ynRLQRyBRdprSD5fK18Knm8ZUqPgIKA4SJkclb7YvCKwIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/550f13e765.mp4?token=jLcE2KQ_abePkPmg6mXpgNNX7Y1KHwy-nwzafmjS-sYdiP6Vlx4aH3HCHVG0fLCVfAEev6gypY0MLX7S7yumaeprCxEqMxhC-4ECcHT0YPrbBTZs3nndSyhHR75bIAoKKMuBoEvj2cH7c44fM-hGwHf6-CVk8HykyKK0E3hGyiQFU6Aj6zRL8ERG7THDsOiL0ZKRxqCQuUvVnc_hR_OdQK1D3OyfjOe4SjMkgHGBX_MLXgsWyIOV8iTa2cgiDm23a7kDQph74i_Hg4subByB7BZsDMQF_lfOxZ6SIIaI0ynRLQRyBRdprSD5fK18Knm8ZUqPgIKA4SJkclb7YvCKwIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدئو رو دو هفته پیش گذاشته بودم.  معاون سیاسی نیروی دریایی سپاه اینجا در جمع حامیان حکومت بهشون میگه خیالتون راحت باشه، حملاتی که ‌ آمریکا انجام  میده «واکنش»  به اقدامات ماست!  «کنش» نیست!   تمام این ۴۷ سال همین بوده!  یه کاری میکنن ، تنش راه بیفته،…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6110" target="_blank">📅 00:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6109">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">محمد اکبرزاده، ‏ معاون سیاسی نیروی دریایی سپاه، ‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.   او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.   جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6109" target="_blank">📅 00:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6108">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0b9d2dcec.mp4?token=RXBqLDREe_ndif4YEfPo7kUW-n8jMWoWUqu-ZYi-tOxoypp3VLlKyqCfU1QmztD2o83AOJ3Ssk5OZIypw8e5hpclD0eNPUp-dQk6k1pa3-OhVYcSRr97CTtyKrTTOaQFy2n0pYI3HErjJFYIUUnEshe44BCoErXv0dFw6tg3kgXHifH9sPfVcjW5IJjcYnh9YeXhZdW9qEsCuNkgY4ID5VqatnNaAxfhdq2bTIK84BDRZTQSqyZM9DjoBg5tUnlqkL4VXYP5RlmVyyH8-ukK_tv8McEb36got4JmaU7h15A0-peQweaaebX2DN5TDl4Lre1b9BRxpp_oa8u2L5AXAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0b9d2dcec.mp4?token=RXBqLDREe_ndif4YEfPo7kUW-n8jMWoWUqu-ZYi-tOxoypp3VLlKyqCfU1QmztD2o83AOJ3Ssk5OZIypw8e5hpclD0eNPUp-dQk6k1pa3-OhVYcSRr97CTtyKrTTOaQFy2n0pYI3HErjJFYIUUnEshe44BCoErXv0dFw6tg3kgXHifH9sPfVcjW5IJjcYnh9YeXhZdW9qEsCuNkgY4ID5VqatnNaAxfhdq2bTIK84BDRZTQSqyZM9DjoBg5tUnlqkL4VXYP5RlmVyyH8-ukK_tv8McEb36got4JmaU7h15A0-peQweaaebX2DN5TDl4Lre1b9BRxpp_oa8u2L5AXAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گشت زنی اف ۱۸ آمریکایی بر فراز چابهار</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6108" target="_blank">📅 00:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6107">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا : محاصره دریایی ایران وارد فاز اجرایی شد.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6107" target="_blank">📅 23:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6106">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
چندین انفجار در بندرعباس
🔺
چندین انفجار در اهواز
🔺
پنج انفجار در قشم</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6106" target="_blank">📅 22:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6105">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/od8G_6FmRzGZ6TEJxzWfkEFbNQYGs3fOQHI2jrhSV0tD9ZNIwNiou1i6dSz_I9ipcIDPPJitDV6Q6xCwowKCRWEmf7luKY3I5__bt-fQXWKHzacj7wHX8X2qLIkmY2nyLq6xlzBm6ZIzMCCBXE_w6XMepKthS7rjHYKuRhIpIcLbgrnzLciSXt_smlwb3F99J9AxBYkJ9YXVeYSmiebj_dxPbkswoMhwCcLefVlKcfud7xkybGcQmh_292llarkktORuj7Sy6YuMUB-i6H34VGuXhO8ZryKIQvtVgUqvtsEcd3arg6qhIeHbZC0BEGnMrU0U-88xGk9FX6OtoG2Cvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2077085449948938568?s=46</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6105" target="_blank">📅 21:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6104">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
دقایقی پیش : حمله به قشم و شنیده شدن چندین انفجار
🔺
حمله به یک نفتکش اماراتی در سواحل عمان
🔺
فعال شدن پدافند در کویت</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6104" target="_blank">📅 20:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6103">
<div class="tg-post-header">📌 پیام #19</div>
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
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6103" target="_blank">📅 18:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6102">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yv-Wy-xrXZamlRoG6-7b0063c8jLgnik8dAhhS2IQeAU3TAtn8gXzulbcD0IRZdokbtWOUlP6p9Yi13Wh3ppP3q4vmXNNri2drB96Ga_rGKSIWMkkfZxNNuPuyJrQpkRkJKamovye_AbKBO3mxJ5pLzyUFHtBVLEUPf13bA_iwElwRDyesNLzxXlZML8Tkra_0D7lDpQmdVzs6jcYe2skvcO4R9jAEPzpITqWIw0FRDRnyOmROikElDGvacC9Kz9fiI5D1yWn26ra1TG16CU6_GRS7VRXwi4kToVej9db8LE5lfs4EkwaRnv7YzPzUoFvsoVdXvpELDtbdy9jp1GGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهپاد‌ها (قایق‌های تندرو بدون سرنشین) آمریکایی این مدلی به یکی از مهم‌ترین مراکز نیروی دریایی در بندرعباس نفوذ کردن و حمله کردن.  گفته می‌شود که در این حمله یک زیردریایی ج‌ا را نیز منهدم کردند.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6102" target="_blank">📅 18:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6101">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee96f6523b.mp4?token=Wg5EPVMvvXAE8ymYVlhRN589Eu-ohjlCJTCFjhZdW4DK3ChGlr73NdqAoRqbbxGwM4WTSBbgYyTWNkyeQa7ikZXOunCj7M74Z-WyIU3_d8L0V3KyyQ81XFAzntg8azpaPgLnAhoAeSSNKDubX4FZHTZoB6PUc9Qgmg4a-uv0Sa8dlSpm_Q90w__0l3IEqqOMbsW7CQ2bV9keIzsRl2lqG5ue-G1EZOYUjexwfYkrtpnyo4Vw3KV-uYyB6rhhOW3rwg4n8bWIuuaRJFyjdFEfue3mZ-RzxbiXWClRoVXSrILuXfuAO63n2V6peBhu8q6vr1ZFuc6NNQdMW0vSg84-LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee96f6523b.mp4?token=Wg5EPVMvvXAE8ymYVlhRN589Eu-ohjlCJTCFjhZdW4DK3ChGlr73NdqAoRqbbxGwM4WTSBbgYyTWNkyeQa7ikZXOunCj7M74Z-WyIU3_d8L0V3KyyQ81XFAzntg8azpaPgLnAhoAeSSNKDubX4FZHTZoB6PUc9Qgmg4a-uv0Sa8dlSpm_Q90w__0l3IEqqOMbsW7CQ2bV9keIzsRl2lqG5ue-G1EZOYUjexwfYkrtpnyo4Vw3KV-uYyB6rhhOW3rwg4n8bWIuuaRJFyjdFEfue3mZ-RzxbiXWClRoVXSrILuXfuAO63n2V6peBhu8q6vr1ZFuc6NNQdMW0vSg84-LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت جنگشون :)</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6101" target="_blank">📅 16:39 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6100">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EKrESF2JfB3tMZEdHHKEyku-CLqFoxsPzrshZbw5p-rJ71yETngjKfunu1yEQg2Zxo4xkadYMI0xgPqIRnJNexscu4DjVuw3SnWe4TJt0ldya94-uBURLUGNGJ06C_Wv29nw1XgD4oYuHvQOJbEO0OxykinU0mOE_dkZLy0n1px5Fr8C5IsFFrHAjXSM0bUL8vGXpiVAH7_17EUkObSyip2FP0HZggCl_woP8ehmFdFW4aOV3yf9A5HeL2prSMmKXrtlGI8nTfHzY0s-4eQD1V7nOuH_YapB8G8u8thOsbS4yiOLLQgTs-WXwHpj3KbPMBP2rwYhmpaxYM1F8SRx8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏آمریکا با استفاده از سه قایق بدون سرنشین (شِهپاد)، پایگاه دریایی دیروز بندرعباس را هدف قرار داد و تأسیسات نگهداری زیردریایی و کشتی را منهدم کرد.  این نخستین بار است که نیروهای آمریکایی در نبرد از قایق‌های تهاجمی بدون سرنشین استفاده میکنند.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6100" target="_blank">📅 16:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6099">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">۴۷ سال رژیم اسلامی</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6099" target="_blank">📅 15:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6098">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QBNv8I788jTxoM7o6LdELnV1YXUUD7bFQGMSEl5s7ut3A_Re4zF4BDiIDR9oHCmCwESikwmGV3wpSsFOFUh9AyOSfH5CV9SfM5JDLSX2AKlrT5FcoNLUUDFNP26qB33aZMYSvQhkyBEA2uq2NkXKcvfSsrQEe-_hSR7CWjG-1O92ztFrilahTakn4ng38VSZ5HHfYS40fNc8qWGRKX540WYro2DMnANioxDkJEkv8Cf1NyvSQ6RZSMoj2DvRpZdEW-yZPPsbFBelG5nTQImAj1AxE85R9NFPZfUQ6ievn--Jv4i8-kFpxVR0-T0RNCG0Chl47RKLwsO4rSHQWjZrrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
تخریب ساختمان مرکز آماد و پشتیبانی دریابانی نیروی انتظامی ⁧ بوشهر ⁩ در پی حملات هوایی ⁧ آمریکا ⁩ به مراکز نظامی جمهوری اسلامی</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6098" target="_blank">📅 15:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6097">
<div class="tg-post-header">📌 پیام #13</div>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac9c510f4f.mp4?token=iPloeib8-D1abP2oCgk-XtNxha6MLpQz2uqhtdi85eyH6Ca-qwt-u2lLAKOxiXVLXwh9IuzOX1edgCiRbBpm0hkCheJ0Gs-fKCZYNDh5jqugScUv05ieAASbbi9hwIAe0Z643drZpBBW6OttlLNsNuI9uhsAASXmQiS-eEKn_qYbUuNY9BmLOezxYjVD54M_Sj_gPFFgUvogynPXIW0iBB1bya1lkYy__lJn5KHwfvpapV8Dwn56cmGcVfqp4g8ELd3iaJq7ywIYxu-1Zeb2rF5UKHlIe4LtyGS8LwyWCFNgf90a2sl1rDMzkVI8vzMht-rjOY7C4itq1_4BbqHcgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9c510f4f.mp4?token=iPloeib8-D1abP2oCgk-XtNxha6MLpQz2uqhtdi85eyH6Ca-qwt-u2lLAKOxiXVLXwh9IuzOX1edgCiRbBpm0hkCheJ0Gs-fKCZYNDh5jqugScUv05ieAASbbi9hwIAe0Z643drZpBBW6OttlLNsNuI9uhsAASXmQiS-eEKn_qYbUuNY9BmLOezxYjVD54M_Sj_gPFFgUvogynPXIW0iBB1bya1lkYy__lJn5KHwfvpapV8Dwn56cmGcVfqp4g8ELd3iaJq7ywIYxu-1Zeb2rF5UKHlIe4LtyGS8LwyWCFNgf90a2sl1rDMzkVI8vzMht-rjOY7C4itq1_4BbqHcgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">می‌پرسه نظرتون درباره اینکه بدون هشدار قبلی برق رو قطع میکنن چیه؟
‏چمران میگه:
‏شما اگر بدونید پریروز چند نقطه برقی رو زدند دیگه این سؤالو نمی‌کردید.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6096" target="_blank">📅 14:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6095">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iSD2B6j11BjmJRExDtrE1qaDR7B6QySIJMGy8IRbUjPfBLW6x1IT606qqYpNORf-at2CaKjILvtRz0MC0dOzL2c6q8sS1I7Exo_dFqNhnO4pv2YOY9Sj4AliaCQfmR7YH64QAfLSmM780nkP_VScthrfeJVY_O6XjTZeeLbr7hRkBVZG8m5sTcO0pls4lo3WgVDxUHk8J4goxXVUZMGY6ggR6i_ncAzWt-Rc_wmGES-NYe6nCiCVKrN6ka3KgQ9bjyupfaAcnxLG5XaJvZWfvQ2Q1NikQPOG3QKcdKIZXs03UglsNOf9kpWocw8dTSOM1SnDX_TPtyJFtuC_twnK4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه ترکیه، دیروز جمهوری اسلامی
رو با اسرائیل مقایسه کرد و گفت
رفتار این دو شبیه هم هستند.
(کاری ندارم که ترکیه خودش چه افتضاحیه، اما نشون از تغییر رویکرد ترکیه نسبت به ج‌ا داره)
یادمون باشه فرمان حمله اخیر از سوی ترامپ در ترکیه صادر شد! یادمون باشه معاملاتی بین ترکیه و آمریکا رخ داد، که آرزوی ۲۰ ساله دولت ترکیه بود.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6095" target="_blank">📅 14:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6094">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
🚨
حملات دقایقی پیش به بوشهر ، خورموج و….
🔺
سنتکام چند ساعت پیش گفته بود که این دور از حملاتش متوقف شده.  در اسامی شهرهایی که مورد هدف قرار گرفته بود هم مثلا نامی از کیش نبود!  مشخص نیست آیا همه این حملات را آمریکا انجام می‌دهد، یا کشورهای دیگر (مثلا عربی)…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6094" target="_blank">📅 13:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6093">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/co9p7BuggPBVvm8Zv4NdPby-8BL4FAi76l5HzHnPElCiJ7CNyz5I1z1yo6xW1LZnxshk1cm5uKSzYRJ3fKn-EvTXy-HGUq_YISthBMqogH8uLW8cknHAPzMQabCc9kNZnjbObej6fNv-iPFvylmFB3rYErTAd9FVNj4j3aekdiDX_1oKXMKV1kL9YL71o_siDfQRxH5TWjLRfB1ooJ65RNRcne8Zo38yfiGEn4ktv4pojHuckpPphxbF5L02iYckS-m_-snRxO45F6oRF7OmS1d87MGFVpqEt0E5HDpl-47UV_H55EDpljAAP4EfXIkjAj4CNl-eGN9yAuncnL2NmQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6093" target="_blank">📅 13:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6092">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b04e0dceb0.mp4?token=q0rF3u2gpcAbTF0C_TgIc_HsaYlMB0B4kFzHAgw6PhsnxScNZ61tPWAuUlyxh4WF1-oucVneDnQXvc0p9a2jJqLcblrB3ASMncVa6BkCkomCIvYs8QjjMgjOGmvhwP1g114SF7v-LNErFiQrAsEDJZiDdQTH1zVC39YqZwIEQxswmCl1BLqoN8ZfWqK2HZOGDyI1Tgjj0IwuAY7VGyQPflau_1Bez2RYEjwofM9sDrInkaeM5lcwQx3twlQVNjIax_P-xeyPJcMSDB-tmxRIeC_f7L0unN3_Yt-eCEyemax3qe4lc8VLqln8zoggse60JeewBww2jWLN7hrDDRhJl4BtaZkJpORJJcwKkFlyESpAiKF8CnKuiopxvTy9WqbvIbYDS7vl2U8sSerhSqgrOchI2e65eizlJUmkxBWWn-tfAhbBXl3OvKfcNOlQkH4sixRWntx8Mnwun2lAuxaJ9H2-Bolk-Xg3CYuY6AU07WVShaJwVKI3CQzd-SovmHmiwwJaHLIJo0OKSja-aMS3IntbShYL6kCwIJFUf-UDB3l0Q5rQrwTfFY4ELlKbL5kQj6QfcYM8_IjvtV6WzlonsGwXjwqddUlkO2VXb0t6ToIAV5SWv1JXm010zjKhZTg306c3v2FdDdk0h9xVVHKXOC0SpVIiF_-YYIJjuA_GugY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b04e0dceb0.mp4?token=q0rF3u2gpcAbTF0C_TgIc_HsaYlMB0B4kFzHAgw6PhsnxScNZ61tPWAuUlyxh4WF1-oucVneDnQXvc0p9a2jJqLcblrB3ASMncVa6BkCkomCIvYs8QjjMgjOGmvhwP1g114SF7v-LNErFiQrAsEDJZiDdQTH1zVC39YqZwIEQxswmCl1BLqoN8ZfWqK2HZOGDyI1Tgjj0IwuAY7VGyQPflau_1Bez2RYEjwofM9sDrInkaeM5lcwQx3twlQVNjIax_P-xeyPJcMSDB-tmxRIeC_f7L0unN3_Yt-eCEyemax3qe4lc8VLqln8zoggse60JeewBww2jWLN7hrDDRhJl4BtaZkJpORJJcwKkFlyESpAiKF8CnKuiopxvTy9WqbvIbYDS7vl2U8sSerhSqgrOchI2e65eizlJUmkxBWWn-tfAhbBXl3OvKfcNOlQkH4sixRWntx8Mnwun2lAuxaJ9H2-Bolk-Xg3CYuY6AU07WVShaJwVKI3CQzd-SovmHmiwwJaHLIJo0OKSja-aMS3IntbShYL6kCwIJFUf-UDB3l0Q5rQrwTfFY4ELlKbL5kQj6QfcYM8_IjvtV6WzlonsGwXjwqddUlkO2VXb0t6ToIAV5SWv1JXm010zjKhZTg306c3v2FdDdk0h9xVVHKXOC0SpVIiF_-YYIJjuA_GugY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #7</div>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UQrha-zyre9fRMu-GzLJO1jOJB19ac8uyhzj4URFgV2CZdOUT5vfg9ahtI-kk7QuPOoD8J1LEh3gTxEAvsMpQImAZ7_oF-wCCf2rbCZvVWhNX079kQvaQhKK11p7i2RHN7uE9KD5rjj7P5UWVGcc7R_edhrbah0SL56i0sluxrE9Ghj7d0jODrQPLVDO4HvjyvFjhHjJu0jW4OmiqbmXfcg3Ju12iK8H8j4UjfKaB21jdRnEBxvOhQtIzyc62cxdgzfYDB2nSv8EtOiFvJ3eB2C0tgxc5pM746nnhuW22tPqyf8UaDGrtneRTCfUos4ranvnMiQnov23gGj1K318iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شب گذشته سپاه به دو سوپرنفتکش (در سواحل عمان) حمله کرد.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6090" target="_blank">📅 09:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6089">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/671b861555.mp4?token=gW11UoyPtege7kJvaY69D8UShSDXu6O8B-WsEpgT55kJvA2onf1WDWb9MGfcVJPPvYHBumqGMbnlJlUQaIlF0wgqjuAgB1BKPS9hvoALRNIMY2_IYSMUHB85IEa-Jh-s477_tSzRoQZTrpLzn22SvfEbUWESZ9pN-oBnd8Z7I2-7icQnooPrgqB3sE21OoRgEMvXl3gvs-dyHd2kSFGF32MbIEjD-9omHrRxGkF1Nllh2_ZTI8vXdXQ2_LpMS1WjD_OhxYZMm9qF79XVZrGiSAl56l1sc9WQ1WdD5yUosxdvjPgiKxmQ5Yw0qxfDAMGUZcHYhCpoIOiFiaigdGz5EbvFQ8-I3kRkwaJgk9fJSr6DEbJe3N_RuszUuDTnE4Eq9UUnEslUVjzCk2IB_YymtJ3d863CswE5yVrzXkJzUa2QIE5kR5tEoQ59HN8FpKs8JhQxF1yZOqszAeHkk2keUpFWYWLc-OGLq1UmLn_NtQCkxa4sA5jVqc4DBKyAg7M5zjgAU6IeD_u3i8bt5zo4RibEeL-b8jddzBXyeMEhkEl-958-eskf4l8MEiE3BLT1B0nGCYOI3l1M3Of_k92zYvy7BVoYfXKjG00YsMUnShV94_scQUXTLWO0sqJRtTFAUzCIwblNLJtcWshMikq-KptTBpmFJW8YGBDyAUcxG3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/671b861555.mp4?token=gW11UoyPtege7kJvaY69D8UShSDXu6O8B-WsEpgT55kJvA2onf1WDWb9MGfcVJPPvYHBumqGMbnlJlUQaIlF0wgqjuAgB1BKPS9hvoALRNIMY2_IYSMUHB85IEa-Jh-s477_tSzRoQZTrpLzn22SvfEbUWESZ9pN-oBnd8Z7I2-7icQnooPrgqB3sE21OoRgEMvXl3gvs-dyHd2kSFGF32MbIEjD-9omHrRxGkF1Nllh2_ZTI8vXdXQ2_LpMS1WjD_OhxYZMm9qF79XVZrGiSAl56l1sc9WQ1WdD5yUosxdvjPgiKxmQ5Yw0qxfDAMGUZcHYhCpoIOiFiaigdGz5EbvFQ8-I3kRkwaJgk9fJSr6DEbJe3N_RuszUuDTnE4Eq9UUnEslUVjzCk2IB_YymtJ3d863CswE5yVrzXkJzUa2QIE5kR5tEoQ59HN8FpKs8JhQxF1yZOqszAeHkk2keUpFWYWLc-OGLq1UmLn_NtQCkxa4sA5jVqc4DBKyAg7M5zjgAU6IeD_u3i8bt5zo4RibEeL-b8jddzBXyeMEhkEl-958-eskf4l8MEiE3BLT1B0nGCYOI3l1M3Of_k92zYvy7BVoYfXKjG00YsMUnShV94_scQUXTLWO0sqJRtTFAUzCIwblNLJtcWshMikq-KptTBpmFJW8YGBDyAUcxG3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: بیشتر موشک‌هاشون رو از کار انداختیم، بیشتر پهپادهاشون رو.
🔺
توان ساخت پهپادشون رو حدود ۹۲ درصد از بین بردیم. توان ساخت موشکشون رو ۸۹ درصد نابود کردیم.
🔺
یه کم توان براشون مونده، اما برای ما هیچ توانی ندارن. این دیگه تقریباً یه درگیری نظامی کوچیکه</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6089" target="_blank">📅 08:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6088">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3962370842.mp4?token=Cz8Vw9Q0Cg_TQDH4hEJDtEqq0EwkrDMMVMgh4PFVL7UbXlMcGekRqJLoFoSGXgDyQAqTjxxbl9Y2QNsZDDclt_XkEo6ounp8RC6oeJih8LeO1KPFEAaoMjNUftZg3iIJKGP0OFjrLw7-XfD42UzNJv2Fr_7ewmf6MbBoy4JPciu7FbHe34fWN5bhmoDqX49CPWI0BSfe3TIWE-c0Gpgc43IZ6op2HKi5FSmRNAHeyb2eFwxLxcq7VB7AEYbVElSwVd0Tmcssw6b2E0XQnRA6AtCcc1CXym_iNPuja8ikTOWIa8MfABTCxRgoUyakPp2KVjq_t5a94HD0VYv-8AI6mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3962370842.mp4?token=Cz8Vw9Q0Cg_TQDH4hEJDtEqq0EwkrDMMVMgh4PFVL7UbXlMcGekRqJLoFoSGXgDyQAqTjxxbl9Y2QNsZDDclt_XkEo6ounp8RC6oeJih8LeO1KPFEAaoMjNUftZg3iIJKGP0OFjrLw7-XfD42UzNJv2Fr_7ewmf6MbBoy4JPciu7FbHe34fWN5bhmoDqX49CPWI0BSfe3TIWE-c0Gpgc43IZ6op2HKi5FSmRNAHeyb2eFwxLxcq7VB7AEYbVElSwVd0Tmcssw6b2E0XQnRA6AtCcc1CXym_iNPuja8ikTOWIa8MfABTCxRgoUyakPp2KVjq_t5a94HD0VYv-8AI6mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات شدید به کنارک - امشب</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6088" target="_blank">📅 01:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6087">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
ترامپ : حملات جدید می‌تواند برای دو یا سه هفته ادامه یابد.
🔺
سنتکام : موج جدیدی از حملات را برای سومین شب پیاپی آغاز کردیم.
🔺
باشگاه خبرنگاران : ۷ انفجار بزرگ‌ در بندرعباس</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6087" target="_blank">📅 00:56 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6086">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
شنیده شدن ۳ انفجار شدید در جزیره کیش
🚨
انفجارهای شدید در جم - بوشهر
🚨
چند انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6086" target="_blank">📅 00:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6085">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
ترامپ : امشب و فرداشب با قدرت به ایران حمله خواهیم کرد.
تفاهم‌نامه آزمونی بود که جمهوری اسلامی به آن پایبند نماند.</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/6085" target="_blank">📅 23:48 · 22 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
