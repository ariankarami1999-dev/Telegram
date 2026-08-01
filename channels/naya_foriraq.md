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
<img src="https://cdn4.telesco.pe/file/TqI87NaW7jnZsESUqDsR7eKyGCOYPOgXmq8uoY-VlsQZHRsE2cpdEJj6qNiiDGyO9nUDchbsS-Q5BaUAdKHxyXFYGaYYLE4Jitna0xGLjrieCQxDPzFSdCXIqyrx1JRFzA_cWOnft8J_-O4I0S8shjIgIE0tTJNHfRFzztzHRAEhVV3P_rZmMmfXh_zeglAzb3hbIenkeUz-WXB5H5TST2UFmEsEAQBhKpYSNwMe_D6sL8rzNFmSCeOB9KAS7UldBn94xJqa8x3MRbczXEBI1SsYL-M_Y1j6pDRwhhd71sbAIvpUQFDkle_DRrlDJDIdsWnZ83fqk3I5ETsUa7dDJQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 274K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-10 20:20:57</div>
<hr>

<div class="tg-post" id="msg-86656">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">الاعلام السعودي: أبلغنا العراق أننا سنضرب الميليشيات الموالية لإيران إذا هاجمت الأردن.</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/naya_foriraq/86656" target="_blank">📅 20:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86655">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">الاعلام السعودي:
أبلغنا العراق أننا سنضرب الميليشيات الموالية لإيران إذا هاجمت الأردن.</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/naya_foriraq/86655" target="_blank">📅 20:11 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86654">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇮🇷
🇺🇸
‏أفاد مسؤولون أمريكيون لصحيفة نيويورك تايمز بأن هجمات إلكترونية إيرانية مشتبه بها استهدفت شبكات المياه في سبع ولايات على الأقل. ولا توجد أي مؤشرات حتى الآن على تعرض أي من إمدادات المياه للتغيير أو جعلها غير صالحة للشرب.</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/naya_foriraq/86654" target="_blank">📅 20:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86653">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/119a2ee3a7.mp4?token=HF4JTHc0YGhTKLGnlqcIAjSS_7oazTikQ8gxSvc3D9KcU8blap9zeOoj1s0Egi32FovSO4XMvyqgWHAsEJGt8IKrKuLhSXG0bEqjw6RfXAYc_jxFZ623AKfpTlaPRZHj9fNk-uk99jRIrBKpcJl__UjDZYRZs-bv7Tcr8W4YHyi70g2yZV9fcUMPNwv3R4xsQeOpL8IusUmXC_tybWEw8nNtjUcLHSbCMVdLKiLHZ-7_-A6sU1p_MNwQs1MBvwnxvhevI6Wm-Tch86EDV4eHUGnZo68PIahx7qaHcanGPDPO02k6SQzJOieSu3LGTF18BDKzleGO4VmPc8EJiB3SjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/119a2ee3a7.mp4?token=HF4JTHc0YGhTKLGnlqcIAjSS_7oazTikQ8gxSvc3D9KcU8blap9zeOoj1s0Egi32FovSO4XMvyqgWHAsEJGt8IKrKuLhSXG0bEqjw6RfXAYc_jxFZ623AKfpTlaPRZHj9fNk-uk99jRIrBKpcJl__UjDZYRZs-bv7Tcr8W4YHyi70g2yZV9fcUMPNwv3R4xsQeOpL8IusUmXC_tybWEw8nNtjUcLHSbCMVdLKiLHZ-7_-A6sU1p_MNwQs1MBvwnxvhevI6Wm-Tch86EDV4eHUGnZo68PIahx7qaHcanGPDPO02k6SQzJOieSu3LGTF18BDKzleGO4VmPc8EJiB3SjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب يزور القوات الاميركية المتمركزة في ولاية نيوجيرسي، يذكر ان هناك انطباع سائد داخل الجيش الأمريكي إذا زارهم شخصيات سياسية أو صار اهتمام بطعامهم فهذا يعني أنهم سوف يُرسلون إلى القتال
😆</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/naya_foriraq/86653" target="_blank">📅 19:57 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86648">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fzHVSlKqn0xcqmz5gn8uImf0wU-MC2mlxeNZQA7hjr5Qg5Yj7MO7b-ypTVyJTka3L5-MZbx2a9ClX07Y48WK0Y7ds2ZyLGXLw2bSVbFIGaYQQxGGtCVUTUriPR67YzFLUF4izyFNrvBXKXbwnjboaKLE3-m7YeBn3RPIcM2lja9TrSzycXnD0slBK0kBBcXfcsbqbxwJM96Vh2Ct5mHUKIRKHvkmhn3JT6-QtIDV3RTfKQ181DJ4VNqtVpDPSxkVS9-e3lSUcZXIvyloUR6_8CeZRNa3vHo84A_DQec59igwWsWzW-8saHSsgqguoltySEQHL8VUV85r4LPmr8hocw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PYem2EzH0N368aJtqo3nZsP8mfb3C_fcuPB30npE2OwyzUkR2BN8ECn6JE9wryDO_X3Mji5oQb9STPmwYaScMp9kDx7ha1T7l73Ys96UfpsMJRjJiuLwU0nxvwlH9QKqdY1XBPJkcBfTtU3VeTmmZ4Ra5cb2M7WyB540j9K3cI5hn3LvTn6XZ5289ICtdmXvuIBWWf0wmHLI2BOJWFOZf54QeqZzfKdt6V-E31MA7HlF0CQdp2cwRPYhONVHw80aHECQFv8jf_O3KaWyMZusufd4UFHubIIWUfJ9JaaGCcJ3uxWT6slrbqtk--4owIYCwDyJr9hJf3mmqN2VA8A6mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rr-sG1zd7BvDMAbv49yNIg1Nbj8024heFOKhjStLjXbDZ4I1YXl6v1_Gufqe-_afaQfCC4BJNwSzf33ku9SiNLY0OSry41JPtigFUUeRDuA_lOsIyCH5dw_PFOmVAbS30rqyDYmYyOYdqlA3EKJntT0Wz6LZvlPsqI5LXsD6OhN03HAEPlYZLtUWWW-wABzCXbRMkW3VlhUbPTQFU-COTVql7D1zSwqdDxL4F1MVMxq97-qH_Y2Bk4AnvZPJfUfM94DEFUhw8XHuIQKUdMdfKoXqzL_F2-tmDwPAhebZ1j1J-urKJGhztESWvV0UV7GFvj0DKiXV1zd6bKp1fqH2uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KLlT3POrO0pnragPxbyT1J2QewprSbHVUJpxV0DIOAZVYnJYPPkJOTAJChRWYL--Pr_yoy0ebVnmkjTrzD6sPl5aKXdr7eL2k7Ucdy-sVXz8_w2V_e3HQiYmXtu2wILMK3Upaw-ECWPHKsNmNncddjA5pSIXDJurWtm0MQqd9x-9IamcOmgEXHNYQRZTGpVaMzC9fWexOIReCHhBYTWHNXk8nAN6Zw3IhMBP9URh9XKcrIQ0U7ZWOJL5G64OghSk7Jx9Igv95OSL3EV6qCOQfNkMzJ5cwxN-nZzGf0a2PEkHKG9NRR0zcgFT5yXPcykJweqpiYjPzGQgcW8vkq013g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YB9xRgmlg--HLp0bgrQtv4IzqaPeyKQGqctwLcu9DqE1floFLlO8jEv_J5tvcYvNFbJd08KwmyMv2XXKsU-bqL9oGjEpY6A1Lmo_sZ4_yh7qvygrxUWb9YgtWzib5h5a7VvgfxeW2qlPX6mHBScTlonOBEfm-gjzeAuJk3XJpORxVYMuqMkcw6QXVB9qJSTYCWODqK1bvxlgTOVJkuh47scw98OcBC1I4FrVT83lLJXp-YQaGUjdbkaI7xhday2jgrvrvuGEXHTVPHQqp7o9oNRskxeXZCPGSfUZFtiT-f9ddmQUnwwAEGj7x5UsR_SRtrinjTEOvcUrOJM16AEJKA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔻
🔻
القوة الأكثر احترافية في قوات الحشد الشعبي العراقية
نشرت مفارز لواء ٧٢ عاشوراء كلاب بوليسية على طوال طريق الزيارة الذي يمتد من العاصمة بغداد وحتى مدينة كربلاء المقدسة للبحث عن المتفجرات والممنوعات ؛ يذكر ان اللواء يعد ابرز الأولية داخل الحشد من حيث المعدات والتجربة الإعلامية العسكرية ..</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/naya_foriraq/86648" target="_blank">📅 19:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86647">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">‏
الصحة العالمية:
تفشي إيبولا في الكونغو الديمقراطية يخرج عن السيطرة.</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/naya_foriraq/86647" target="_blank">📅 19:25 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86646">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1f0463375.mp4?token=MuevMbm17vFZfddzAO0_xzYyBZA-0ZqcexHo3bCGntIPTw4eAXPHmthyU89nx2ubtCqtHq3VQi58jgVPVbtkPIyubu91dBH2KvonoVDvu7cXSYCx6xn8MK4Jac8I7IsairBwoTAheoCZZz--acZLbkjAjdo9sCGs1mVM4G5nGAnJU1NN4NNEAPfV2svmGPcMSmj6acpJytCvigM3mk7QiWycqL8R8W488HICD-sfIszJPr0w0dO0-FkuWQERvS06O9dyx_d7fCU9QY9Cb8GTLt7mTtmNHL0007HGGFyc3VnvtFm1yspRsvph41KAoiyHImnzFGwt16ckoug7BoltqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1f0463375.mp4?token=MuevMbm17vFZfddzAO0_xzYyBZA-0ZqcexHo3bCGntIPTw4eAXPHmthyU89nx2ubtCqtHq3VQi58jgVPVbtkPIyubu91dBH2KvonoVDvu7cXSYCx6xn8MK4Jac8I7IsairBwoTAheoCZZz--acZLbkjAjdo9sCGs1mVM4G5nGAnJU1NN4NNEAPfV2svmGPcMSmj6acpJytCvigM3mk7QiWycqL8R8W488HICD-sfIszJPr0w0dO0-FkuWQERvS06O9dyx_d7fCU9QY9Cb8GTLt7mTtmNHL0007HGGFyc3VnvtFm1yspRsvph41KAoiyHImnzFGwt16ckoug7BoltqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇭
‏إخلاء القواعد الجوية الاميركية في البحرين خوفا من الهجمة الوقائية الايرانية.</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/86646" target="_blank">📅 19:04 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86645">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cbf8f15b8.mp4?token=V5xEmydV7xKw3It1tLDoTuUM59WVA5OMGZ5VIKousj_WEkHE5AFOx8pcl76kcIOFJI0-axrorr3HR5ODRqTOS4LC_dbFFFHSkr-isB8Lp6G7cOuGhHdErVQzMIWRtDGBM5mkhpVv8mraznqm7XZb3Q96KbM5Z8QGc20pI_lWCgPdxEmZ4JeJOeb4GgtGowpPT32qrLF8NuI0_C_BJPsHnF9iVvQc7UEzZuii-8aoeYfdA7iHSmt-5jnIFFSzmEtfnZm8Sd0PEIXbw--KoX7ATzIBI2MxhOnt86qwinPQCUhHbHU0jgkEwiATkalWorPnl-WjdcERlcAHFmZA9JT87g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cbf8f15b8.mp4?token=V5xEmydV7xKw3It1tLDoTuUM59WVA5OMGZ5VIKousj_WEkHE5AFOx8pcl76kcIOFJI0-axrorr3HR5ODRqTOS4LC_dbFFFHSkr-isB8Lp6G7cOuGhHdErVQzMIWRtDGBM5mkhpVv8mraznqm7XZb3Q96KbM5Z8QGc20pI_lWCgPdxEmZ4JeJOeb4GgtGowpPT32qrLF8NuI0_C_BJPsHnF9iVvQc7UEzZuii-8aoeYfdA7iHSmt-5jnIFFSzmEtfnZm8Sd0PEIXbw--KoX7ATzIBI2MxhOnt86qwinPQCUhHbHU0jgkEwiATkalWorPnl-WjdcERlcAHFmZA9JT87g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
مشاهد اخرى لاحتراق مقرات المعارضة الايرانية ي محافظة السليمانية شمالي العراق اثر استهدافها بطائرات مسيرة.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/86645" target="_blank">📅 18:57 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86644">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89cbebf655.mp4?token=JE8_ZIGMH_upYXmM5QB1O8AIpS2mOsGiiC3pq-IdUTLetXHYrvrNO6wXboyK2j21ztoWdHmXg9U9xARN1k-077ghBUXFM8ZUFcs5HbSbuPY7UikEeoeBoDm1AjmcGFLwHQHbH3xrgl7i3IsZOaGauckeNsdtpDjX8x9HLahhTVNPGzcmFhTOO-zNsig0wwZkgLopsriyqk03FNbbVvdko_ppYRBMBqMThG_8a5pA_Dr82ejRd2fHKX8mYFp0eDFm7uVmVQAZtKFhj5ziclpr8rWZur5A56K1RLCmaFar5u09dnVVkiwj5JUAlW37omVzlyLBEbKpNFYs2ht00MUW0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89cbebf655.mp4?token=JE8_ZIGMH_upYXmM5QB1O8AIpS2mOsGiiC3pq-IdUTLetXHYrvrNO6wXboyK2j21ztoWdHmXg9U9xARN1k-077ghBUXFM8ZUFcs5HbSbuPY7UikEeoeBoDm1AjmcGFLwHQHbH3xrgl7i3IsZOaGauckeNsdtpDjX8x9HLahhTVNPGzcmFhTOO-zNsig0wwZkgLopsriyqk03FNbbVvdko_ppYRBMBqMThG_8a5pA_Dr82ejRd2fHKX8mYFp0eDFm7uVmVQAZtKFhj5ziclpr8rWZur5A56K1RLCmaFar5u09dnVVkiwj5JUAlW37omVzlyLBEbKpNFYs2ht00MUW0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من استهداف مقرات المعارضة الايرانية الكردية في محافظة السليمانية</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/86644" target="_blank">📅 18:53 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86643">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b27ee993f3.mp4?token=TkyvJxfDy6p9oIaeUwU7o1KZbHjFXOP13bE5AtEUw8Y8SA7QpATkc6a29kvbWBTEcaeXNUbtc50v6UHSF4yAFOfl92Ms7zvV0bpVxMCFeC1kIauUSRZAPVLc-r9TtGnMUb4tbhIbUBSUnTGutc_6YxBGkEIQ3d0HwPU5XDH-HFtPSnIZgUgOMgbyob2EVU2LCe8SlfoEt45fyCJHb96Drin2uLTm-uT59w7JaNLS5Ro4UnDMkwPvbIzWRxc0oz3-Y5ft78O3mFsPnkmwLE7uKE3klWa-sh0as6EpBi2VDyFZiZhHB1rh173hWGiPQWL0OKG9K1X0a8j0OnitsoFQ6rIYxYHjTXDkUc-yCe6-FegF-1p_DiY0d4rrdnvku4XR4M-5VNvG-i1zj2d8kRwx18DdS_UaLsiyO9hRHhb7L__yHQvqQWtqw9evCiux6mVdR62smg_tfhmc81PPfPaxPLW_cCxa0F5Lr_dEdM-Dg1cJuXsBGdp6bc6UA-j5oLgvBF50DIYh87tlc_9GH-WJHb9Le60WxhzRneuVx4nyKy7DOj5KhCFDZnOUknGYrYWee7MO1npkONXr0bUjj5SZuIED6MY-Lq98Cf_9Tuq7ntudKBNTzvfpZRfcNcVHdvCWBAVrcY_i4TTLHAUKA_rPpe153ZTWWRBXvgs2WGnH8hc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b27ee993f3.mp4?token=TkyvJxfDy6p9oIaeUwU7o1KZbHjFXOP13bE5AtEUw8Y8SA7QpATkc6a29kvbWBTEcaeXNUbtc50v6UHSF4yAFOfl92Ms7zvV0bpVxMCFeC1kIauUSRZAPVLc-r9TtGnMUb4tbhIbUBSUnTGutc_6YxBGkEIQ3d0HwPU5XDH-HFtPSnIZgUgOMgbyob2EVU2LCe8SlfoEt45fyCJHb96Drin2uLTm-uT59w7JaNLS5Ro4UnDMkwPvbIzWRxc0oz3-Y5ft78O3mFsPnkmwLE7uKE3klWa-sh0as6EpBi2VDyFZiZhHB1rh173hWGiPQWL0OKG9K1X0a8j0OnitsoFQ6rIYxYHjTXDkUc-yCe6-FegF-1p_DiY0d4rrdnvku4XR4M-5VNvG-i1zj2d8kRwx18DdS_UaLsiyO9hRHhb7L__yHQvqQWtqw9evCiux6mVdR62smg_tfhmc81PPfPaxPLW_cCxa0F5Lr_dEdM-Dg1cJuXsBGdp6bc6UA-j5oLgvBF50DIYh87tlc_9GH-WJHb9Le60WxhzRneuVx4nyKy7DOj5KhCFDZnOUknGYrYWee7MO1npkONXr0bUjj5SZuIED6MY-Lq98Cf_9Tuq7ntudKBNTzvfpZRfcNcVHdvCWBAVrcY_i4TTLHAUKA_rPpe153ZTWWRBXvgs2WGnH8hc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">في الموكب نفسه، تجسّد مشهدان متناقضان؛ الأول لمواطن يعبر عن ولائه برفع صورة السيد الشهيد و السيد مقتدى الصدر وسط الحشود بكل سلمية واحترام، والآخر لمندسّ استغل الصورة نفسها غطاءً ليشتم شهداء الحشد الشعبي، سعياً وراء إثارة الفتنة وشق الصف.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/86643" target="_blank">📅 18:51 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86641">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BdlyxkHwOifXUZXq0bLfyPJ7fQq0rdNfdVBA1Pr-KvLGc4Lj197zcKtkcp1MYbI-WW0QfNQCOvbS45ZFKVCPrjrThSwRN9rzf2ojUeAZu3gDEiEAyCkEIzoVjEdD0h7vctlgPu-7lbAweHODSKPWaXaxVlJaU4Gm5qR_URn91yEoYTrjPaOTv1akHD8-EuOoKNEp4JDYpL-5x0ny1PoIR2LDCu3GXUeonxmr8Q8WNxRCqwDjoVomMIPbMgNztQjJ-7WaEfB5qieTVYmMyFetHQehgGFGVRQE4dZ-Prnd4f3fOZ1K0XKmo80yVALG990ZsirPm8y7sg1y1Nh5IACfMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oHfXQfCAyjHKALzywLRr-aimac6gVFGi1gbov8s_cj7m5GYLmW7jTiQIcW29LZnUguC_-tP2hc18TxuZp2yKsmGo48zw4yL5A70X9FLeIu0Am4clkgqUR8w-Jg96lT4Tk-OsdsHARJ9pB4ZmZS8NTu26YON1rC6PpnlLPSorv0IDOswJpRS-GxRRibAZ3xXbzqNNDquHdZoQ6BW0FaXcPrPEL-qYikQHapmBkkYn3FTVZEAe2kL5jLzvqxGRa2-JS8dixr7bysO7isNDg0WBtaaoeU84P17ZFpvhgx7rPpIYCIIK79KeN3spqzZ2V20wUy4XY1rdNXVcfaBRHAdR8A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مشاهد لمنطاد التجسس الامريكي</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/86641" target="_blank">📅 18:34 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86639">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FjxB2Rzic_4UxQBr_UhTjWkEm7luPENnkKGUFYFIA4Lu33Vm_ZHmX02CEF0toDCDHSlgM2gnYrDer8tl47BGL5dc_oD5FxH9QXzt_95gZWi3gS6uTxnpid5-k_unPVZSLo5vsQaYKo-otRWUdWnboFOHTQ8ug6wqcLBo9g31eTJq1O2bBlvVxAqzCthSHcpH5twjJ2NuCLJhPl-GsLpI96Rz45jjr1FUBA8QiIg8BX0YDwSz4fctiMasajUG335OJfeSeRBeR5WVFcKKW9TDMdAI2U8IM_DhoxUR1tMy0EClEj1WhevsV7ePtXwVCdmQVq_DGVJCDOMYKkgBDx6wOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZDaU15LMvdnKwr0yN3mrTy-CKoHwb1A-DAoZtWVBeItnr4FkgznjgArILwv0Ma25VnaeJIT2vCqNF0gZTA_AYdJ3cZo_vyoUkaptoRWU7ScGoxGhMfMIuZn55Ab78AbXeC-us2aq6quH6lDWDKHzHgT_jSbtUUloB7UvJZygsQo_dpPgnnCvVhtOKsM8e4kFB78M9Fveq6rjhIl3umBps7lBGSLqAGCcVQiP8eHKjTK4C25f2DpPhR249Xcs6PWP974F6i8V-A8NumCnDBy1AsTM2sSfIJk89mDWteh7HGxfF8laoHHvLA_oB1ciOzWiP8R8ys8mvN6d0Pr6bZ6n9g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇸
جيش العدو الامريكي ينزل منطاد مراقبة مطار أربيل الذي كان بمثابة رادار لنظام باتريوت الأمريكي المضاد للصواريخ والذي تم تركيبه خلال الحرب الأمريكية على ايران.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/86639" target="_blank">📅 18:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86638">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2447c36d60.mp4?token=tn7Htfd_UhnzYU4TjWh0bNFrSCCUW8EVR4-yXFqEBDDr385amquoeJyYWMOb5GUveWlP1pq8GGlQeoabhHsUO5VAFiuGNHutKKoRlPHyPwtxMjszr8Izge93flKMh6428sFbnYwnD1L729AGfIaMjoJPa9vBlEWv2DopY94yTNi6H9eoe72m7OblnvUrZE5UE6YyeLk2pzsBr3ivqx_O7kO53ZROKA3d4PwAlcFwoMtI9NMpfIrksnNWhpcbJgxvEwgR652fL2_lTdb3VlgX-yRrwr5l4pfEHTEcSiSdCleI8_FMFGtKRhSr-rU0D_JrUCMZZDuVkXX0eU8nmA3clXECdWt_CGN-eLQ4I580ZkWd5ltgVOw5sgy7jQVMkyQX7DXb5qJe9vYVYLbAJDhB6BDZdOUqPwJKMZJZFXoOOr8IPnyCRXh3f7RtyeegZHjBJVRYP8y_F9VlpV7ar3oSGs6LCFSxHHEmgll5T8HP4z8yi4pIQN_cNHhUChOFF9hFXtizVOBPXxTKzgedQSF1fQ6pFf5mmF6NiJWIHeogSk1o6oVKsvh7CcZg-EBB6NQ6PkTqfcmVctjuBdtMs1-CxlhQqLttNxmKqc5EoyG-CYUfW0hUliCJNJQKXD4dBBCvLGtlRzZTrZEGmuVAAKTiVItMkOr52COZUrrsvYnE030" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2447c36d60.mp4?token=tn7Htfd_UhnzYU4TjWh0bNFrSCCUW8EVR4-yXFqEBDDr385amquoeJyYWMOb5GUveWlP1pq8GGlQeoabhHsUO5VAFiuGNHutKKoRlPHyPwtxMjszr8Izge93flKMh6428sFbnYwnD1L729AGfIaMjoJPa9vBlEWv2DopY94yTNi6H9eoe72m7OblnvUrZE5UE6YyeLk2pzsBr3ivqx_O7kO53ZROKA3d4PwAlcFwoMtI9NMpfIrksnNWhpcbJgxvEwgR652fL2_lTdb3VlgX-yRrwr5l4pfEHTEcSiSdCleI8_FMFGtKRhSr-rU0D_JrUCMZZDuVkXX0eU8nmA3clXECdWt_CGN-eLQ4I580ZkWd5ltgVOw5sgy7jQVMkyQX7DXb5qJe9vYVYLbAJDhB6BDZdOUqPwJKMZJZFXoOOr8IPnyCRXh3f7RtyeegZHjBJVRYP8y_F9VlpV7ar3oSGs6LCFSxHHEmgll5T8HP4z8yi4pIQN_cNHhUChOFF9hFXtizVOBPXxTKzgedQSF1fQ6pFf5mmF6NiJWIHeogSk1o6oVKsvh7CcZg-EBB6NQ6PkTqfcmVctjuBdtMs1-CxlhQqLttNxmKqc5EoyG-CYUfW0hUliCJNJQKXD4dBBCvLGtlRzZTrZEGmuVAAKTiVItMkOr52COZUrrsvYnE030" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاعد اعمدة الدخان من منطقة دوكان في محافظة السليمانية بعد هجوم مسير استهدف مقرات المعارضة الايرانية الكردية</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/86638" target="_blank">📅 18:23 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86637">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇺🇸
جيش العدو الامريكي ينزل منطاد مراقبة مطار أربيل الذي كان بمثابة رادار لنظام باتريوت الأمريكي المضاد للصواريخ والذي تم تركيبه خلال الحرب الأمريكية على ايران.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/86637" target="_blank">📅 18:18 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86636">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5826e91067.mp4?token=Z89u8emsWo8QtcXDBsy507Y8eLTUapXE1IovqoMY0ammHiWOhWq1wyfQ1W1grtr99VL41_1jagZU0JKAglMci1rnItgSPZw6YEFZTG01DVbo0fe_732dtpfm4JU7-tR_5jVH5ArM4UJwLsGDaBr6MP10XTxuwT8porZ03qksXIsWVlrf9qpPg-V6EdD5CD-SzvqfHOC8dxKkAl-35MiLqNYxdw2jK6IiAgX99VkIvr2IzLgu6BL0qbhiphCEoKaAJbC_hTPasc1pALc9qZWm6wscLFFBoCp5T08pJeery8Gzhi387Ez-W6cjWhU0RlhZGmSlx1bfY3bkadNeTsyE61D0__4nopxZgWeHELMHehOkxdePu5rKXu9wP0v89C6VuBKTlMaHHNK_IS7FnbpSvha0YfVAveopVCah_OOtsBfwZimcuVpHjwZVCUVqynl7A-dpposxqLq5pkhP53Q7gPlxIDDoEe6QgPlTGzDEkxtmUaSIWxZZb9dBRrNddp9u1W6-qye-hbmtjObgJgVCKiVhd2MUqrigYT-AVdpnFGSRPK9lbxeGrwNuJlBSZAJt2T3OkMXIV4Ot-uCMmHMvQq4Y9xX64T4TRWlyBmQybDc56igV2wQdcsmeUSOxWER9KVrBZwv9FRmklRGTE2fCMVdHLfjqggv_9XahSzgj2DM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5826e91067.mp4?token=Z89u8emsWo8QtcXDBsy507Y8eLTUapXE1IovqoMY0ammHiWOhWq1wyfQ1W1grtr99VL41_1jagZU0JKAglMci1rnItgSPZw6YEFZTG01DVbo0fe_732dtpfm4JU7-tR_5jVH5ArM4UJwLsGDaBr6MP10XTxuwT8porZ03qksXIsWVlrf9qpPg-V6EdD5CD-SzvqfHOC8dxKkAl-35MiLqNYxdw2jK6IiAgX99VkIvr2IzLgu6BL0qbhiphCEoKaAJbC_hTPasc1pALc9qZWm6wscLFFBoCp5T08pJeery8Gzhi387Ez-W6cjWhU0RlhZGmSlx1bfY3bkadNeTsyE61D0__4nopxZgWeHELMHehOkxdePu5rKXu9wP0v89C6VuBKTlMaHHNK_IS7FnbpSvha0YfVAveopVCah_OOtsBfwZimcuVpHjwZVCUVqynl7A-dpposxqLq5pkhP53Q7gPlxIDDoEe6QgPlTGzDEkxtmUaSIWxZZb9dBRrNddp9u1W6-qye-hbmtjObgJgVCKiVhd2MUqrigYT-AVdpnFGSRPK9lbxeGrwNuJlBSZAJt2T3OkMXIV4Ot-uCMmHMvQq4Y9xX64T4TRWlyBmQybDc56igV2wQdcsmeUSOxWER9KVrBZwv9FRmklRGTE2fCMVdHLfjqggv_9XahSzgj2DM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات تهز السليمانية</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/86636" target="_blank">📅 18:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86635">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">انفجارات تهز السليمانية</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/86635" target="_blank">📅 18:02 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86634">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">السلاح المنفلت في اقليم كردستان
هجوم مسلح في سوق كلار بمحافظة السليمانية يسفر عن مقتل شخص واصابة اخر والمسلحين يلوذون بالفرار</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/86634" target="_blank">📅 16:50 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86633">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f9790c4c7.mp4?token=QZ6oN4-eLw6uj7Nzap6ys4v9qNcoKkIDGn9FeVF7dolTPlmqaHLyHtMcS7C3K_P7Jzl0w4IGe4bUAEvHRID73Gv_xZbZI4H713QggYQaQ6GDaxgYIWDdih6zLKIE6KpyR3iZD4yt_msTTQ8GKijDnuVtXP2u-d_GEzsDbWo6dRopWeA350mDaaTqCMH9xVnpvTn6wQg32Q0iGmYQDXLdys-m6mI7jxhvBzXWop-V9pAiAQCA1ncConvEAp-wckF2WPUNVuRu6-WIGAXf_PBHsmP4o2WlO1MHcJ50FfUrXqlYC6PnRZbY3TXf-nLrlB0oq7p9YtRM79IUQekq4hOatQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f9790c4c7.mp4?token=QZ6oN4-eLw6uj7Nzap6ys4v9qNcoKkIDGn9FeVF7dolTPlmqaHLyHtMcS7C3K_P7Jzl0w4IGe4bUAEvHRID73Gv_xZbZI4H713QggYQaQ6GDaxgYIWDdih6zLKIE6KpyR3iZD4yt_msTTQ8GKijDnuVtXP2u-d_GEzsDbWo6dRopWeA350mDaaTqCMH9xVnpvTn6wQg32Q0iGmYQDXLdys-m6mI7jxhvBzXWop-V9pAiAQCA1ncConvEAp-wckF2WPUNVuRu6-WIGAXf_PBHsmP4o2WlO1MHcJ50FfUrXqlYC6PnRZbY3TXf-nLrlB0oq7p9YtRM79IUQekq4hOatQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
خاص لنايا | طيران حربي امريكي يحلق في اجواء شرق الاردن.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/86633" target="_blank">📅 16:42 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86632">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f255af304a.mp4?token=AoJHXpw_NbpyFRBMeVozMdii173_gvkTi9e9Qgvy_nzoMd5t0xtW9Z1AaQRzbierVhtdt8xUkP0pg8K09JCMSPq4L7baLLrhV8IMYYLXGnM4bvpYENl8tVTj6BTEIHUrpWWXHonalIAoD5Fy9rFS_PyAVBRBHlTkibhkFlII-A4JS4jlXRnou7JPmZwh8M31ZY61QbpNSnatW5lYl8WMCvYwuZytwUi9P5PAo2tjuVa3L2jpwMBWNeXRRw4peGjUZ-yf421yGdwc7G9H6hN4S4ISwwNPTn3ZAskFJknHiH5vOFnf8rTXL8vegXtqwCmCvEPzpQcR-iXGi1w3Vh8IDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f255af304a.mp4?token=AoJHXpw_NbpyFRBMeVozMdii173_gvkTi9e9Qgvy_nzoMd5t0xtW9Z1AaQRzbierVhtdt8xUkP0pg8K09JCMSPq4L7baLLrhV8IMYYLXGnM4bvpYENl8tVTj6BTEIHUrpWWXHonalIAoD5Fy9rFS_PyAVBRBHlTkibhkFlII-A4JS4jlXRnou7JPmZwh8M31ZY61QbpNSnatW5lYl8WMCvYwuZytwUi9P5PAo2tjuVa3L2jpwMBWNeXRRw4peGjUZ-yf421yGdwc7G9H6hN4S4ISwwNPTn3ZAskFJknHiH5vOFnf8rTXL8vegXtqwCmCvEPzpQcR-iXGi1w3Vh8IDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
خاص لنايا |
طيران حربي امريكي يحلق في اجواء شرق الاردن.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/86632" target="_blank">📅 16:41 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86631">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o6CvyZwYPdW4Nj1SFdc6nvbkirlYRK5Qvp3tmZh3fRXRHHP9b64ol2yTa0TkvM0bsVo0uAeNx7Y7OGSTFJl0PidaNIp88eyImYZMpdxnwYSV8RXhtIcbl7_KmLJ-mLE1KFXGHRyex31v80FEaQta0Lj_KZSnCejgkehEdCkZ9LvhHE6X522q2jbp2XbHW8KtfTD_aWoXwy1T7vvvL6TXj-PjDNChF46NTFVoMMxdps1qNLYDSnSp2vZol5wpYGIq_0hQa1PLUAlmK2NW-55OW3cp3LRAZfO5TYeyzKGi08BxYhBz9yITQ4qqaQukREJKohz0z38sYoetZuHEOHLAaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
السفارات الامريكية في بغداد وعمان والقدس المحتلة والقاهرة وبلدان اخرى تنشر:  يجب على الأمريكيين الموجودين حاليًا في الشرق الأوسط توخي الحذر واليقظة الشديدة، والاستعداد لإلغاء الرحلات الجوية، والإغلاقات الدورية للمجال الجوي، والاضطرابات المحتملة في السفر.…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/86631" target="_blank">📅 16:38 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86630">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bb6f4d28c.mp4?token=I-jO02b8EIaoCFkBHjNqnuL3Xfselfj3epMINc3InWRkGaW0Xhb-g9LVA_Qta1wfWFKTMkrTndCuaPGnL2ez7PcrpDYBgitqGAFpsQIpKEHBfgUv3Ic7ta6JfLJH51w51dMJHPQvGmURj_g4CIKpqeCLXzTp0aMhCPu9KIkawMkTDkfwfd1KabEiqW6tJ9Q2ngMU2awpSkH0fKe5E2IPq6CF4bbm72L_6kTGLg1Dl6t4Qp4HybvCXb5SkUWa9DvrUQ-N8zc8cjqEkls4twQksR_7eozZ7sQ3DYlpqt9AtJ35yhlig4IFZ1uqYL3TUBDGcBx9rrTX3sJ0vKBqjhgeXgaw9dtPehZCKqLBOB5hElBxI6nKUq0kHE3s4y7qAlXGnH1_GMXWyrlLTQUaOWxcmvJm10OC39i7bIeh6_EJQe0wqz4yc_8AdO7097zx5VlWuF5JI4R7kioX6hN7PaCOUfBO0l3Ps5GzTZxIv9yqJDoBWOyzfVR9u1UCRQFsRRaNzmH4SS9pFafyiDFdM61WK5OiG6whNqPeuK4_vMT4TrkOkS8tbeQIlBsbatbS8ft3Xi2ITjivd_gfZY56aW30JmmA6jbtM9Q3mxXOK2afsQOVM7C9kwS8mtsCdWEH95cm0YqqoLGbw9bQhuJ8ZUgps_wDhFPFOTs9KMpneCHTeHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bb6f4d28c.mp4?token=I-jO02b8EIaoCFkBHjNqnuL3Xfselfj3epMINc3InWRkGaW0Xhb-g9LVA_Qta1wfWFKTMkrTndCuaPGnL2ez7PcrpDYBgitqGAFpsQIpKEHBfgUv3Ic7ta6JfLJH51w51dMJHPQvGmURj_g4CIKpqeCLXzTp0aMhCPu9KIkawMkTDkfwfd1KabEiqW6tJ9Q2ngMU2awpSkH0fKe5E2IPq6CF4bbm72L_6kTGLg1Dl6t4Qp4HybvCXb5SkUWa9DvrUQ-N8zc8cjqEkls4twQksR_7eozZ7sQ3DYlpqt9AtJ35yhlig4IFZ1uqYL3TUBDGcBx9rrTX3sJ0vKBqjhgeXgaw9dtPehZCKqLBOB5hElBxI6nKUq0kHE3s4y7qAlXGnH1_GMXWyrlLTQUaOWxcmvJm10OC39i7bIeh6_EJQe0wqz4yc_8AdO7097zx5VlWuF5JI4R7kioX6hN7PaCOUfBO0l3Ps5GzTZxIv9yqJDoBWOyzfVR9u1UCRQFsRRaNzmH4SS9pFafyiDFdM61WK5OiG6whNqPeuK4_vMT4TrkOkS8tbeQIlBsbatbS8ft3Xi2ITjivd_gfZY56aW30JmmA6jbtM9Q3mxXOK2afsQOVM7C9kwS8mtsCdWEH95cm0YqqoLGbw9bQhuJ8ZUgps_wDhFPFOTs9KMpneCHTeHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
طائرات حربية مجهولة تحلق في أجواء مناطق سهل نينوى شمالي العراق.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/86630" target="_blank">📅 16:25 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86629">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇮🇶
طائرات حربية مجهولة تحلق في أجواء مناطق سهل نينوى شمالي العراق.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/86629" target="_blank">📅 16:22 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86628">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇺🇸
🇮🇷
مسؤول أميركي:
الجهود الدبلوماسية تتقدم ببطء واستئناف المفاوضات المباشرة مع إيران لا يبدو وشيكا.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/86628" target="_blank">📅 15:55 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86627">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IiwYWFEaMJM65osGE7IJEh8CWOBonjBbxIhSDkguvAdvKN_zvzgaQu7ZZkJeitte9AayXqSWOEg3WITjsRiQ94V5N098Q2qWbCqSPOPYzzV6THE7CKRC6_JP8cyyJDlwOqgGlRaLZkm9MSH5QL2M8n-RroA_qcJr8QkCnoKyQ8YU-wDCc5Zx82kdPLXd-fGSq5S-ruQZgO-X86P_DOHb67AJj-tU3kd_6Xat8mwnYuF1S51we09yP8wD4sbg6HVLwEC80dN9uBiDPDwWdmQRHGfPYd3N8WmufaSk1UPvN5yifeYr1wQivlHhFwv1alOb4uLiKQiw6EDuV3Umtx_1Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
واشنطن بوست:
الجنرال أليكسوس غرينكويتش القائد الأعلى للقوات الأمريكية في أوروبا يحذر البنتاغون من عدم كفاية عدد المدمرات البحرية لحماية إسرائيل من الهجمات الصاروخية الباليستية الإيرانية مع تلبية احتياجات الدفاع الأمريكية في الوقت نفسه.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/86627" target="_blank">📅 15:48 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86626">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇮🇶
وزارة النفط العراقية: اتفاقية ثلاثية لاستئناف التصدير عبر جيهان بطاقة 750 الف برميل يوميا.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/86626" target="_blank">📅 15:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86625">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p8CAT1CDS8GRRRaldp_pUYNOmwoDwKc3wAdh-qSQiahOmgkKTT1gNsvxt7gHPrM2bSdeX5qc_Vf7DLqCbJbRIMF4NNx8CHlsur0FI98wxXTXnWhwjprgbG3dbLVydzAMMGPav59aBKrdEZRKty6Hw5yyjsjmVqyqkTZL9EXKBL1GCXk7mTdiMKhoc6tMKYmXj_dWEneCTVyARN8y6IRqCSSpPmehXQQ7p-YRGm37909e0EkBxRvUlOzmfWAldHx5cEVgrGr8qC6ZIpfczHGVwbRBUf_v8DeCiIVW_mjlfQ3PKD621BdNFoYvak0df_FgCEdYAI44NEheevcbUqMNgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🌟
في ابهى صور الديمقراطية..
ترامب يهدد السلطات التشريعية باستهداف جو بايدن واوباما سياسيا في حال لم يتم تعيين تود بلانش بمنصب المدعي العام للولايات المتحدة مؤكدا انه سيبقي تود بلانش مدعيا بالوكالة.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/86625" target="_blank">📅 15:18 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86624">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CrtHcQahG0knrfBZ1Xe_hnlLZQho9fLR96b5TOkocmyg3QP56DiBYSvb-pUuyPiMfXCgzA9Prj2B-AWtxwaaA7h7TEFuX0KhXH1v5WJTNqICrnULN4CqQpdOshorv9VPTcDlLPAMUbJhhk9YfNIwpvaSXaPK5j8CqX6m3WkspZY5GM5CSZzxvehbtDdZ8BobcQU6LJ0amVdSy9XxUCmUN0cXk5qd3kOpZ7BBBjug_yi-W_1ppsVTZZPXA7dUCGnwq70nUTuFe7AR8x-9kmbtvW3t0gzqKoIp_eY5Lzu36HeGixP9Qv9PGz-3kndvrLLolIrp13cd6CLA9JF1MYLLXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
السفارات الامريكية في بغداد وعمان والقدس المحتلة والقاهرة وبلدان اخرى تنشر:
يجب على الأمريكيين الموجودين حاليًا في الشرق الأوسط توخي الحذر واليقظة الشديدة، والاستعداد لإلغاء الرحلات الجوية، والإغلاقات الدورية للمجال الجوي، والاضطرابات المحتملة في السفر. وقد أجلت بعض شركات الطيران في المنطقة استئناف جداول الرحلات السابقة؛ بينما ألغت شركات أخرى بعض الخطوط</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/86624" target="_blank">📅 15:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86623">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇮🇱
جيش العدو:
خلال الليلة الماضية أصيب ضابط في الجيش الإسرائيلي إصابة متوسطة خلال عملية عسكرية في جنوب لبنان. تم نقل الجندي إلى المستشفى لتلقي العلاج، وتم إبلاغ عائلته</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/86623" target="_blank">📅 14:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86622">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TBjbuHf-wgnv-G8OVYSjUVGT3oZKBv27clLNENCW7qscJk79sgSKXhw-c7m1Pe_VguKmipeM7btuOp7D_aEH7IzYQVzpxtu6bWL5_P8K9Gt3xP-ZwVgopoyR0iUJwL7fbyCT4zIi0jC5-TqW03tmd3cqypjs5uOi_rPUmrPveVpAOJLGb0UgNlwW5TUSKVTltTG_OY4ILgYiPpsvxyaw4CCIo037CF7pKfMP8A7x5U04tg-z3wFdQWFmO1KjFlRfkYj_QzBRSrRawgify5NC5zKIyliMwTcQf917RLG7wPh0UKk8rMdf0_2yRr8nYJiQHLivi1SafO5B4FuH0BsO4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نظام ال سعود يعلن فتح باب التطوع الى الجيش بسبب النقص في صفوفه لكثرة الانشقاقات ولصعوبة تجنيد مرتزقة بسبب شحة الموارد على خلفية اغلاق مضيق هرمز والحصار في البحر الاحمر.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/86622" target="_blank">📅 14:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86621">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇮🇶
🇮🇷
السفير الايراني في العراق:
موسم الزيارة الأربعينية لهذا العام يسير بأقل قدر من التحديات، هذا العام، بدلًا من الحديث عن المشاكل نتحدث عن الإنجازات التي حققها موسم الأربعين. الزائرين الايرانيين يتمتعون بصحة جيدة وفي ظروف مثالية لأداء الزيارة.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/86621" target="_blank">📅 14:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86620">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇮🇶
وزارة النفط العراقية:
اتفاقية ثلاثية لاستئناف التصدير عبر جيهان بطاقة 750 الف برميل يوميا.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/86620" target="_blank">📅 14:04 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86619">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">من الحريق في اربيل</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/86619" target="_blank">📅 13:26 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86618">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b34d9c123.mp4?token=aMTJq9f3UjmLU05nGSx2pJOkSSaPTYm2jBSCvoMZ95GXfHTiGufI0rhbExZuUiGA6aLZoT_qRhKpuvkoRs6in314qWduuU_4EQvoHx-V8Hs6aYc9jT4QF4WPtpcIk7pfY_jMO0ACA5tLUtEXFPVAUozHlgOs3pvFetnfNx3MQjHaw0yBCSwWhxbm7nBARWvsx5IIdxo9hKs5-ItOZ1nsoljGuK_4XCgpfSD2gOYa419dxyX0b5oNNoa7lbBFXKveb83_eWHaFfCnwo6A6-8wkSA8AfmEPIVEYURuKTUdQ7WKGqXrl7gAs6vRTBciyc4WsjRTzAP95Zzk1n_uC--gQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b34d9c123.mp4?token=aMTJq9f3UjmLU05nGSx2pJOkSSaPTYm2jBSCvoMZ95GXfHTiGufI0rhbExZuUiGA6aLZoT_qRhKpuvkoRs6in314qWduuU_4EQvoHx-V8Hs6aYc9jT4QF4WPtpcIk7pfY_jMO0ACA5tLUtEXFPVAUozHlgOs3pvFetnfNx3MQjHaw0yBCSwWhxbm7nBARWvsx5IIdxo9hKs5-ItOZ1nsoljGuK_4XCgpfSD2gOYa419dxyX0b5oNNoa7lbBFXKveb83_eWHaFfCnwo6A6-8wkSA8AfmEPIVEYURuKTUdQ7WKGqXrl7gAs6vRTBciyc4WsjRTzAP95Zzk1n_uC--gQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توثيقات اضافية من الحريق الذي التهم احدى مصافي محافظة اربيل</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/86618" target="_blank">📅 13:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86617">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇪🇸
وزارة ‏الداخلية الإسبانية:
وفاة ما لايقل عن 67 مهاجرا خلال عبورهم جيب سبتة.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/86617" target="_blank">📅 12:58 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86616">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e37647a01.mp4?token=efBAe7TJPDwYXUTx6SfVbC9XMqtRilpccBdTZKFCNMKPoQuKGRot8BS213nscgNKSCdfcJ6sRZrSOceG2WKEH4dlNarJH0Ey02L0iJfv8EHVdqCfL6o66OGWv35bl3ANBfPNvXQ5-e5E79DvTf_Pw_uPF9cCcUk8M8tXDDdOXTcQZv-MCDSJfdeH-9yKQXZVmttinpmNtYZstM0V4jMvIc6ftU-I7ySRMtYU9x3qrPadV1qS7zR_pOg3gcmJxjtNaeDc3ECQV7QHg3v-9GI61NwvK3TwArdMPHN4KJwatJnfHeTy8ef_eQi-ZwRh7vtIdOh1IWZEJLkfzxAgLghZKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e37647a01.mp4?token=efBAe7TJPDwYXUTx6SfVbC9XMqtRilpccBdTZKFCNMKPoQuKGRot8BS213nscgNKSCdfcJ6sRZrSOceG2WKEH4dlNarJH0Ey02L0iJfv8EHVdqCfL6o66OGWv35bl3ANBfPNvXQ5-e5E79DvTf_Pw_uPF9cCcUk8M8tXDDdOXTcQZv-MCDSJfdeH-9yKQXZVmttinpmNtYZstM0V4jMvIc6ftU-I7ySRMtYU9x3qrPadV1qS7zR_pOg3gcmJxjtNaeDc3ECQV7QHg3v-9GI61NwvK3TwArdMPHN4KJwatJnfHeTy8ef_eQi-ZwRh7vtIdOh1IWZEJLkfzxAgLghZKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من الحريق في مصفاة للنفط بناحية شمامك بمحافظة أربيل</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/86616" target="_blank">📅 12:55 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86615">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/feed9248e1.mp4?token=UfZjMyZNQV_bD5Z_CkEdfKSHx7IeI6zp6paobQ6YzgvtNq9-HjqaG_ROxf2M8FFRndsZoTe1YiYAw6adX-2-d__GLZdOhqZrQjos14gjSzORWFtvRZbvKixNbW3Tf6jdk_YlMJeXPysLvVaFnHoy7QM3GG8MwP_6LGrx1frjKH4VhoY5IAMgekGjUFh-nGWGS5RDF_zFBI8nooT6NMO_FVul9RrNdGbAMKvZmUkJ3wlRRz7lbaUbcoBR-WEJjfw9HXLBwtfMPJUQU441bBsN7uRaL1QDXxDYsss-vNY2yYWcMC8E9Nqz2WpYIc-QLcxELo1st8RSy-5KzWkcBT-AzwCvN5h4c-4kibyW9Av9nCur5ab1IPWFMwYp4kXMarfuTpfRPhbW01TV5kgb2SSDoFTm47d4WVkHv1DtadC2vyonkdAtFzrKfeyczVgNaBc7dH3ArEpVzQ1EFnfW5RlJgJY4feppej5J63ArUEzXQBkQrHWAt2tor02IhF848XrGyigwNBAcTUzO24wI2fhaJ3RGMP9e-bkFD9RXe4VouWTuOKR1J4xqEiJNXzMzKzxkgmKt7_Jw-KmzGY3nhAxkCgeHPD4NIyQqsy771S62TgogblKWmvgZ-1-dH2M-lHrTAawbPEqtZVauj6HVntp6C9b1fJmAVc4uZ_nnvgxqDmE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/feed9248e1.mp4?token=UfZjMyZNQV_bD5Z_CkEdfKSHx7IeI6zp6paobQ6YzgvtNq9-HjqaG_ROxf2M8FFRndsZoTe1YiYAw6adX-2-d__GLZdOhqZrQjos14gjSzORWFtvRZbvKixNbW3Tf6jdk_YlMJeXPysLvVaFnHoy7QM3GG8MwP_6LGrx1frjKH4VhoY5IAMgekGjUFh-nGWGS5RDF_zFBI8nooT6NMO_FVul9RrNdGbAMKvZmUkJ3wlRRz7lbaUbcoBR-WEJjfw9HXLBwtfMPJUQU441bBsN7uRaL1QDXxDYsss-vNY2yYWcMC8E9Nqz2WpYIc-QLcxELo1st8RSy-5KzWkcBT-AzwCvN5h4c-4kibyW9Av9nCur5ab1IPWFMwYp4kXMarfuTpfRPhbW01TV5kgb2SSDoFTm47d4WVkHv1DtadC2vyonkdAtFzrKfeyczVgNaBc7dH3ArEpVzQ1EFnfW5RlJgJY4feppej5J63ArUEzXQBkQrHWAt2tor02IhF848XrGyigwNBAcTUzO24wI2fhaJ3RGMP9e-bkFD9RXe4VouWTuOKR1J4xqEiJNXzMzKzxkgmKt7_Jw-KmzGY3nhAxkCgeHPD4NIyQqsy771S62TgogblKWmvgZ-1-dH2M-lHrTAawbPEqtZVauj6HVntp6C9b1fJmAVc4uZ_nnvgxqDmE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اندلاع حريق كبير في احدى مصافي محافظة اربيل في اقليم كردستان شمالي العراق</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/86615" target="_blank">📅 12:53 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86614">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c4b26c5b8.mp4?token=Up3xRWGHSU7zH0FeGM_03HhylJ2vPlaDljS0D1RK7XO24UxRh3Rbo_LRY6M_AB_6ulp8VKKYmPEd4OVzGgu3r4gpCyJLXZLbJXSsq98-s9rHsz7Nn7k2llgWzPWo91RO5RxPqr3nPi2hoIC8Nh-GXd3wnNM1pdYASONhxecOwtMayX26TfB981mFooRBpFTmq9uogolkAUW-kk3X9BHkoT95VLN2VKNJDJ1bWkzb2zlWhTuc4F-_X-vgTS0p38XQt67sXvqFaSUCIKZFgbeSZEWxL2SfUrPc3oBylbjQ8h0qNuK59znc49MPhQXgk5-S-dX4j_eys9wYGC5y60NIjTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c4b26c5b8.mp4?token=Up3xRWGHSU7zH0FeGM_03HhylJ2vPlaDljS0D1RK7XO24UxRh3Rbo_LRY6M_AB_6ulp8VKKYmPEd4OVzGgu3r4gpCyJLXZLbJXSsq98-s9rHsz7Nn7k2llgWzPWo91RO5RxPqr3nPi2hoIC8Nh-GXd3wnNM1pdYASONhxecOwtMayX26TfB981mFooRBpFTmq9uogolkAUW-kk3X9BHkoT95VLN2VKNJDJ1bWkzb2zlWhTuc4F-_X-vgTS0p38XQt67sXvqFaSUCIKZFgbeSZEWxL2SfUrPc3oBylbjQ8h0qNuK59znc49MPhQXgk5-S-dX4j_eys9wYGC5y60NIjTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اندلاع حريق كبير في احدى مصافي محافظة اربيل في اقليم كردستان شمالي العراق</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/86614" target="_blank">📅 12:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86613">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇺🇸
🇯🇴
🇮🇶
السفارات الأمريكية في العراق والأردن يتنافسن بالدعوة للمغادرة..
سفارة أمريكا في الأردن تدعو مواطنيها إلى التفكير في مغادرة منطقة الشرق الأوسط وتجنب القواعد العسكرية، وتحذر من أن النظام الإيراني غير متوقع، وأن هناك احتمالًا لتصعيد مفاجئ واضطرابات في الرحلات الجوية والمجال الجوي</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/86613" target="_blank">📅 11:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86612">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇮🇱
🇺🇸
منصات المستوطنين في الكيان تتحدث عن غضب في الولايات المتحدة .. نتنياهو يريد حرب دون نهاية وقد يقدم على عملية عسكرية قبل الانتخابات</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/86612" target="_blank">📅 11:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86611">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">هجوم مسير إيراني يغزو الكويت</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/86611" target="_blank">📅 11:31 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86610">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">هجوم مسير إيراني يغزو الكويت</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/86610" target="_blank">📅 11:31 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86609">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/86609" target="_blank">📅 11:30 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86608">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇮🇷
قائد مقر خاتم الأنبياء المركزي:
تسعى الولايات المتحدة الأمريكية، بوتيرة متسارعة، إلى إشعال فتيل حرب شاملة في المنطقة.
هذا النهج هو نتاج استراتيجية خطيرة تهدف إلى التوسع والهيمنة غير المشروعة في جميع أنحاء المنطقة.
لقد أثبتت الولايات المتحدة الأمريكية، في الحرب الأخيرة ضد إيران الإسلامية، أنها لا تتردد في ارتكاب أي جريمة أو تدمير ضد مصالح وموارد المسلمين، وذلك في سبيل تحقيق أهدافها وأهدافها الشيطانية.
يجب أن تدرك الدول الإسلامية في المنطقة أن الولايات المتحدة تستغل مواردها وثرواتها وبنيتها التحتية الحيوية ومواردها الاستراتيجية كدرع دفاعي لجيشها المتهالك، وفي الوقت نفسه، لتعزيز آلة الحرب والأمن للنظام الإسرائيلي الإرهابي الذي يقتل الأطفال.
لقد أثبتت الجمهورية الإسلامية الإيرانية وأبناؤها الشجعان والأبطال في القوات المسلحة وجبهة المقاومة أن ميزان القوى في المنطقة لم يعد يتبع المعايير السابقة، وأن عجز الولايات المتحدة عن تحقيق استراتيجياتها العدوانية وغير المشروعة ضد إيران الإسلامية قد دفع الجيش الأمريكي المتدهور والنظام الإسرائيلي المزيف إلى شن الحرب وإراقة الدماء والشر من وراء تحصينات الدول الإسلامية، وإلصاق تكاليف الحرب على حكومات المنطقة.
يُعلن بوضوح: يجب على الدول الإسلامية أن تراقب عن كثب جرائم الولايات المتحدة وأن تعيد النظر في تعاونها معها؛ وإلا، فإن أي دولة تعتبر نفسها درعًا دفاعيًا للولايات المتحدة الأمريكية الإجرامية والمتجاوزة، ستشتعل في نار الحرب.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/naya_foriraq/86608" target="_blank">📅 11:23 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86607">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🇮🇷
🇺🇸
إعلام العدو عن مسؤول أميركي: بعد الهجوم الصاروخي المفاجئ على قاعدة أميركية في الأردن الأربعاء نفذ الإيرانيون هجمات إضافية
الإيرانيون هاجموا سفناً في مضيق هرمز رغم تهديد ترامب بأن أي هجوم إضافي سيقابل بضربات أميركية</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/86607" target="_blank">📅 11:19 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86606">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇵🇰
إعلام باكستاني: العثور على جثث 8 من بين 10 متسلقين انقطع اتصالهم بعد انهيار جليدي على جبل "برود بيك" في باكستان</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/86606" target="_blank">📅 11:06 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86605">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🇺🇸
إعلام أمريكي : ‏دار نقاش حول محاولة إنهاء [الضربات الموسعة] بحلول موعد افتتاح الأسواق المالية يوم الاثنين، وذلك بسبب المخاوف بشأن تأثير التفجيرات على الاقتصاد الأمريكي والعالمي، لكن لم يتم تحديد موعد نهائي</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/86605" target="_blank">📅 10:29 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86604">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🇷🇺
🇺🇦
قصف صاروخي روسي كبير على العاصمة الأوكرانية كييف والنيران تشعل السماء وسط انقطاع واسع للكهرباء.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/86604" target="_blank">📅 10:26 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86603">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇺🇸
إعلام أمريكي :
‏دار نقاش حول محاولة إنهاء [الضربات الموسعة] بحلول موعد افتتاح الأسواق المالية يوم الاثنين، وذلك بسبب المخاوف بشأن تأثير التفجيرات على الاقتصاد الأمريكي والعالمي، لكن لم يتم تحديد موعد نهائي</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/86603" target="_blank">📅 10:24 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86602">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">هجوم بالمسيرات والصواريخ الإيرانية استهدف القواعد الأمريكية في الكويت</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/86602" target="_blank">📅 09:55 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86601">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/86601" target="_blank">📅 09:55 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86600">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BC_CCvPlPYo44Vn2gl1IRGLR_a7hHllKGL7c74S60hntSO3sBin3WKV-VojvyBqUuGpLGzXxqgSPmwpS4fF2_cqZ39PcWq6-scw1vljo9OGvwxzKkArlnsGbp-TYkqJwrAaWqVmlDFveiO-fnAjD4bGgpA1bXPTG6tGfSSmRX2zCCNGKpNt_zYWD494pUhDnQDxZa-z61Cnv0KGGbfdtWsbwAL0ftMFYAOiGLVuJU0TvZ89jdgBIad5SXqW_nUxB2suPhUxtjuJglZntWLX6i4LDkL2w1mQxvL1fUHVbxByCxnOKr3P-hc_WDqGXIXXvkYRCN5XywPtILqfhejnxZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدث بحري قبالة عمان</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/86600" target="_blank">📅 09:24 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86599">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">حدث بحري قبالة عمان</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/86599" target="_blank">📅 09:24 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86598">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/86598" target="_blank">📅 09:24 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86597">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇾🇪
إعلام يمني: أنباء عن سماع دوي انفجارات شمال شرق تعز في اليمن.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/86597" target="_blank">📅 09:08 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86596">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WK8fZ-aAvd5smSv8-LoAz_B8WjJwKURqop3Rlz8_iaMXTusN2wLHJqazRbzAq2mKbfXIHEhbfWvHQ6Sjjj0kKGnF1M3MEE5bc4Ka5ifiDg06e21qjjf_evUjUiwF09_xPkYecOTIQQ2-kwhWPC1REbiEG0A1qOh55M52GBYpb6Io5c7cDIsivEebpm1Llgz-TwG3J4fOrEpW4eJ2PGOxMnKHIa0vU7knajEg_V0mrfs9-nndibCoZApL6D1RKTryuz0cqccQ5vgpMgGqcD9WT4gRJEoXC6jq3L5P8v0mqM1z3W0m-DdMUgRiuyqBgQ6ucjO8JBCqQDhfRr2l3rFZhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الله أكبر
الهيئة البحرية البريطانية
: ‏شنت القوات الإيرانية هجوماً على ناقلة نفط أخرى في مضيق هرمز ليلاً أثناء عبورها الممر الذي تحرسه الولايات المتحدة. ‏أصيبت السفينة بقذيفة في غرفة محركاتها ولم تعد تحت القيادة.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/naya_foriraq/86596" target="_blank">📅 06:28 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86595">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/044c3ed5b4.mp4?token=Fyc1AVs35X__i6RuoZPlLwCGKFX2m1FZ6c7ykL6mk3ika9Oz58FNHZhKje3qrLV7saAlOn0MxI4K9-8QBlvdZ9rZvj0ro7v-0mNoeM07DbxWPLWFLJcpmjShmJj9J9Pxbg5IgTOfXr189FpSeXz8moJQuf4Yk3K8Oz_y9P23RQfTTD7BDEH-MKRtmMrkWKLfoxRouJ99wPbzDEsMo46pF70aupTKPj89UMRA1fsykqsl3za5ljqDeAZN38unl28ep2ncXmcdZcmPY9COKFvPw6aKR1gvzb3JU6B8OCdd-6H3e6xAkKrsFA9je8RN1PIs6ypsnAm6oYSw3pRLKZz6D05xs0TSJzbcQMTzWwk1JdfZXKW63LkQZ0ZOGLj9oaoaCmgVBkJFoaBeRRQYqiRqzDAirMOm6M26rtCk_qNhrU0HGhaVRaqIjsBoISd3-E4KgEPQddpIwmZgEh_SNfm_Z7WF9aEhozpIjUHOx4OF9JcZkUqQVU2-aQMsCp73TWaxxzbqArXg222GH3wNucbtJDsN-IVsPBlF15gdYOgj8rA78WQ2hzG0sirYvyxVXt4evuuHQqugszYxrwD5Ck5en-P9IXa_5__hMX3LGPGuaLFSEI2S2Dwg-VOfT4UvzHwAM9TjtZhBoR59jnSNtuFLKPrWVttv6chKXRpvmjNCobM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/044c3ed5b4.mp4?token=Fyc1AVs35X__i6RuoZPlLwCGKFX2m1FZ6c7ykL6mk3ika9Oz58FNHZhKje3qrLV7saAlOn0MxI4K9-8QBlvdZ9rZvj0ro7v-0mNoeM07DbxWPLWFLJcpmjShmJj9J9Pxbg5IgTOfXr189FpSeXz8moJQuf4Yk3K8Oz_y9P23RQfTTD7BDEH-MKRtmMrkWKLfoxRouJ99wPbzDEsMo46pF70aupTKPj89UMRA1fsykqsl3za5ljqDeAZN38unl28ep2ncXmcdZcmPY9COKFvPw6aKR1gvzb3JU6B8OCdd-6H3e6xAkKrsFA9je8RN1PIs6ypsnAm6oYSw3pRLKZz6D05xs0TSJzbcQMTzWwk1JdfZXKW63LkQZ0ZOGLj9oaoaCmgVBkJFoaBeRRQYqiRqzDAirMOm6M26rtCk_qNhrU0HGhaVRaqIjsBoISd3-E4KgEPQddpIwmZgEh_SNfm_Z7WF9aEhozpIjUHOx4OF9JcZkUqQVU2-aQMsCp73TWaxxzbqArXg222GH3wNucbtJDsN-IVsPBlF15gdYOgj8rA78WQ2hzG0sirYvyxVXt4evuuHQqugszYxrwD5Ck5en-P9IXa_5__hMX3LGPGuaLFSEI2S2Dwg-VOfT4UvzHwAM9TjtZhBoR59jnSNtuFLKPrWVttv6chKXRpvmjNCobM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">كلا كلا آل سعود..
تشييع الجثامين الطاهرة لشهداء اللواء 30 الذين ارتقوا نتيجة العدوان السعودي الأمريكي الغادر الغاشم في محافظة نينوى شمالي العراق.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/naya_foriraq/86595" target="_blank">📅 04:25 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86594">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🇮🇱
إعلام العدو:
حدث أمني في الجيش الإسرائيلي والتفاصيل لاحقًا.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/naya_foriraq/86594" target="_blank">📅 03:55 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86593">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cffc20c83.mp4?token=pzmL1UOyJfIi6irRdf2m4WyxoZ0QZqN3u71d4PwUplkYTq8Qfm3DiVwE-O7XdGIMYv3b8wdfZ5OO0C3Hf0JUaoAQ6sPPo7H7noro2NfwYyeLnqDBdSVpKCxYQJk0TK9DmLC7sbxMGCG_7t1L_YWtsoPfZDkk_7WELtRtzaCxLxwr1B9CN-glxlu6_IzCMnvt3Lp2aS_1bUdgBuvPFmQPWPKnY-HACtzkfu7Cxns9ImDJWJVGwqEgv5jPOkx5sF2umS-zfFU8ke3ZVXC5qk8MTAaDnweBiDpE2yikd4kcDq0FguWchnYa8-HX8JkGZues8pa-Vz-29O50sRkgE2emUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cffc20c83.mp4?token=pzmL1UOyJfIi6irRdf2m4WyxoZ0QZqN3u71d4PwUplkYTq8Qfm3DiVwE-O7XdGIMYv3b8wdfZ5OO0C3Hf0JUaoAQ6sPPo7H7noro2NfwYyeLnqDBdSVpKCxYQJk0TK9DmLC7sbxMGCG_7t1L_YWtsoPfZDkk_7WELtRtzaCxLxwr1B9CN-glxlu6_IzCMnvt3Lp2aS_1bUdgBuvPFmQPWPKnY-HACtzkfu7Cxns9ImDJWJVGwqEgv5jPOkx5sF2umS-zfFU8ke3ZVXC5qk8MTAaDnweBiDpE2yikd4kcDq0FguWchnYa8-HX8JkGZues8pa-Vz-29O50sRkgE2emUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
إقلاع مستمر للطيران الأمريكي في قاعدة موفق السلطي الجوية بالأردن.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/naya_foriraq/86593" target="_blank">📅 03:31 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86592">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇺🇸
إغلاق جزئي في مطار دنفر الدولي بالولايات المتحدة الأمريكية بسبب تهديد أمني محتمل.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/naya_foriraq/86592" target="_blank">📅 03:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86591">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cwVD4XVulCEc3PglvfyP5qh_YyoCfzu5eq4Db3XLx9iHdg7U64XFfj4RFpn2DnN0iKcTU3ZUdDLE5lWJWn7AZkzS-9v9v4y1EaxSLbmeYrg7mrJT5Nt9F9AMmrMuhK5QnNbtNUT8A84uulEXEXQey967X0EhnT0w-HDcpeMx8gOgndsaLfZimFr6nVawJvrvfD8tuZcVZiIuwdfr_9q5tdfMeijj_xhF-FjlioMprjSVnQXb_hOjNaQHTjUe5DomMQBbNrHytaB5F5v0eFJiCkmZCow_1JX4fuRtxjwP2BtmPbdtoHR0ISJXl5alien1bUdkvdmM3dMUeHFWmCQ9sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇷🇺
🇺🇦
قصف صاروخي روسي كبير على العاصمة الأوكرانية كييف والنيران تشعل السماء وسط انقطاع واسع للكهرباء.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/naya_foriraq/86591" target="_blank">📅 02:36 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86590">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇺🇸
🇮🇷
‏مسؤول أمريكي: ترامب أمر بجولة جديدة من الضربات ضد إيران ستستمر لعدة أيام</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/naya_foriraq/86590" target="_blank">📅 01:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86589">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇺🇸
البيت الأبيض:
طهران أخلت بمذكرة التفاهم وأطلقت النار على السفن و
قتلت جنودا أمريكيين
.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/naya_foriraq/86589" target="_blank">📅 01:29 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86588">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qu9fGDNEs-NbzdVh_tb4hQ2k7ucgQ25sRmixv4e7ZNm_qOzZ2I0fqPLYcQnupDaUD2CoglJ_C8Ltsdj588hNGx8mJET0AXMZJiTnO-awkBmT8AhIFtpf4Nm9qFI_vASklua9ntPCvBf26ey9BJxOFReNLHAamgAPw_MqZxYOtbmy-GF3QS0bpBOx9TB9Z4lEsAFpGfryQtnWYLKH0ojNIniKfrJIfK6-fN3qHnr5rjkfd_SosX8O8QlQqMLgTvUIS3iMW4qPnFNEs_lYieO6ZlDkArASb_kq_fRpXR3rdiPUGEOmW5LrGsl5VM19uoxnuFm_9ZIC5rRN445_oYpf9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
الأمين العام للمجلس الأعلى للأمن القومي الإيراني:
إن استمرار الحصار البحري وإشعال الحروب الذي يمارسه النظام الأمريكي سيؤدي إلى تشديد الحصار على مضيق هرمز وإغلاق المضائق والاختناقات الأخرى. وسيدفع الاقتصاد العالمي وسوق الطاقة والناخبون الأمريكيون الثمن.</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/naya_foriraq/86588" target="_blank">📅 01:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86587">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔹
مسؤولين أمريكيين وأوروبيين:
روسيا تزود إيران بمراقبة الأقمار الصناعية والاستخبارات الإلكترونية التي قد تساعد طهران في تحديد مواقع القوات الأمريكية، وتحسين دفاعاتها الجوية، وتشويش الأسلحة الأمريكية الصنع.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/naya_foriraq/86587" target="_blank">📅 00:58 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86586">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔻
تسجيل لمحادثة تحذيرية من قبل القوة البحرية التابعة لحرس الثورة الإيرانية، وعودة سفن النفط من مسار غير قانوني وغير مصرح به.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/naya_foriraq/86586" target="_blank">📅 00:55 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86585">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🇺🇸
🇮🇷
‏
مسؤول أمريكي:
ترامب أمر بجولة جديدة من الضربات ضد إيران ستستمر لعدة أيام</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/naya_foriraq/86585" target="_blank">📅 00:49 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86584">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇺🇸
🇮🇶
وسائل إعلام خليجية:
القوات الأميركية تبدأ الانسحاب التدريجي من إقليم كردستان العراق.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/naya_foriraq/86584" target="_blank">📅 00:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86583">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">الاعلام الغربي:
‏تستعد الولايات المتحدة وإسرائيل لقصف أهداف متعلقة بالطاقة في إيران في أقرب وقت ممكن نهاية هذا الأسبوع.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/naya_foriraq/86583" target="_blank">📅 00:28 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86582">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇾🇪
العميد يحيى سريع:
في إطار تثبيت معادلة "الحصار بالحصار" ونتيجة لإحكام قواتنا المسلحة للحظر البحرى على سفن العدو السعودي النفطية تم إجبار ثمان سفن نفطية سعودية على تغيير مسارها باتجاه الرجاء الصالح.
تؤكد القوات المسلحة أنها مستمرة في عملية الحصار للعدو السعودي وأن يد القوات المسلحة ستطال سفنه بإذن الله حيث ما تمكنت من ذلك.
تحيي القوات المسلحة بإعزاز وتقدير شعبنا اليمني العظيم المؤمن المجاهد على خروجه المليوني في الساحات والميادين رغم غزارة الأمطار ونؤكد له أننا لن نألو جهدا في إنهاء الحصار عنه واسترداد كل حقوقه بإذن الله وقوته.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/naya_foriraq/86582" target="_blank">📅 23:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86581">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇺🇸
ترامب: لو لم يكن لي، لما كانت إسرائيل موجودة اليوم. لمَا كانت موجودة، وكانت إيران على بعد أسبوعين فقط من امتلاك سلاح نووي.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/naya_foriraq/86581" target="_blank">📅 23:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86580">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇧🇭
إدارة مطار البحرين الدولي تُصدر تنبيهات احترازية للمسافرين والعاملين في المطار.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/naya_foriraq/86580" target="_blank">📅 23:55 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86579">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇺🇸
ترامب: أنا أقوم بعمل أكبر بكثير مما كنت قد أعلنت أنني سأفعله. كنت سأتدخل وأدمر قواتهم العسكرية، وأدخل، وأخرج.  ثم أدركت أنه إذا فعلنا ذلك، فعلينا أن نحافظ على هذا الوضع بطريقة ما. وإلا، فسوف يعيدون بناء ما دمرناه.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/86579" target="_blank">📅 23:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86578">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🇮🇷
🇺🇸
‏ترامب: ‏مع إيران، وبحسب التعريفات، فقدنا ما بين 16 و18 شخصاً، و‏نفس الأشخاص الذين أبقونا في فيتنام لمدة 21 عاماً يشتكون الآن من إيران.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/86578" target="_blank">📅 23:48 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86577">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇺🇸
ترامب: "هل تريدون أن تنتهي الأمور بسرعة؟ أعطوا الأشخاص المضطربين أسلحة نووية. ستنتهي الأمور بسرعة كبيرة."</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/86577" target="_blank">📅 23:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86576">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90150a3aec.mp4?token=IU1fx1jfLsn27_i0DhsxwvcGyv4OYuKAEni55SnXdq3qgP3s9NeRA03MdM4BYBzKfqLZt9SI7ItriDNPCh3kFRdaFt7kB1qvc_jteDCTrmm74bNsLOyAO10k6UCDEn6EpycvIIux2LbycqRv2sVAa9Y7_T680BoLLlBdqGSvoxX2ruOKEzhWWPX3jdyyTv2NPC-f0vXQNG7YvWVsI3dMAUDFw6bquheOXFo4Kxbjl0vrU_hoDkdvPsjE8N8HyqneYU2qCjWsDCb647DMpadUzaPIb_r4-CeConQKTogcKkq07L8p6Kgax2qcUN7Mws9mON_DM0rBzkUQhSD8l1uo8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90150a3aec.mp4?token=IU1fx1jfLsn27_i0DhsxwvcGyv4OYuKAEni55SnXdq3qgP3s9NeRA03MdM4BYBzKfqLZt9SI7ItriDNPCh3kFRdaFt7kB1qvc_jteDCTrmm74bNsLOyAO10k6UCDEn6EpycvIIux2LbycqRv2sVAa9Y7_T680BoLLlBdqGSvoxX2ruOKEzhWWPX3jdyyTv2NPC-f0vXQNG7YvWVsI3dMAUDFw6bquheOXFo4Kxbjl0vrU_hoDkdvPsjE8N8HyqneYU2qCjWsDCb647DMpadUzaPIb_r4-CeConQKTogcKkq07L8p6Kgax2qcUN7Mws9mON_DM0rBzkUQhSD8l1uo8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
انتشار عسكري كبير في حي جميلة بالعاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/naya_foriraq/86576" target="_blank">📅 23:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86575">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38ce236252.mp4?token=QDkP4qEt65rM1SATJPF3CuMVUJ_vBBJmlvtkQNXn-GUnZ6OXDeScalirm-iy8LCWg0yCJZ4fyI-NtzKkaDxM2W3VQvzXtD4frDZ769A2MhxceQquFjoomhSpIO_WU6G458HVRHz09c1kYo4npO1bwZq1GlCsM2LIxa8BXHuaWPNZMxLVmx9dFFZm2tdGDA5eB2hCUTdSCMWBSlRJhgFvqpsJ8h6KotZU5GONRug-R3O_2rOoWRyZWkQqJq20dF9BGnXgZoTwCFi9BPzlLeKvfVFrTZHcCGlrYE6HltyD3nCZ3S_O18Jj4Zaoo27jHkThtviHlIz9fu8hzdB0a6J0kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38ce236252.mp4?token=QDkP4qEt65rM1SATJPF3CuMVUJ_vBBJmlvtkQNXn-GUnZ6OXDeScalirm-iy8LCWg0yCJZ4fyI-NtzKkaDxM2W3VQvzXtD4frDZ769A2MhxceQquFjoomhSpIO_WU6G458HVRHz09c1kYo4npO1bwZq1GlCsM2LIxa8BXHuaWPNZMxLVmx9dFFZm2tdGDA5eB2hCUTdSCMWBSlRJhgFvqpsJ8h6KotZU5GONRug-R3O_2rOoWRyZWkQqJq20dF9BGnXgZoTwCFi9BPzlLeKvfVFrTZHcCGlrYE6HltyD3nCZ3S_O18Jj4Zaoo27jHkThtviHlIz9fu8hzdB0a6J0kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب
: "هل تريدون أن تنتهي الأمور بسرعة؟ أعطوا الأشخاص المضطربين أسلحة نووية. ستنتهي الأمور بسرعة كبيرة."</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/86575" target="_blank">📅 23:41 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86574">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">اندلاع حريق حريق مجهول قرب القاعدة العسكرية في مطار بغداد " مطار دبلن "</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/86574" target="_blank">📅 23:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86572">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇮🇶
استنفار بين البعثية للبحث عن الشخص الذي ظهر في مقطع الفيديو بعد مطالبته بمكافأة قدرها 33 مليون دولار زاعمًا أنه أبلغ عن مكان اختباء صدام حسين(
الحفرة
).
كفمي كفمي شوكلاطة
😆</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/86572" target="_blank">📅 22:43 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86571">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
‏تعرضت 67 سفينة على الأقل للهجوم أو الاقتحام، وقُتل 17 بحاراً، منذ بداية الحرب مع إيران.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/86571" target="_blank">📅 22:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86570">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5605707ff5.mp4?token=TLMQ_ZnBd--qsBkJtOoz8bDKsLduy4rJxa9xYCSqz1WCvU-6vTrzbqV6fsxBVDHMyrUqtQRYBGnKu6rgP85yo6xKN_HBb4UZklAs3TOS7baS-NgKX-jox8rIHtZfL4Y4XKl3j4sd50eWSno-ahiBMEgB-4CNvV03xBiDKd0zIA2mM3Gjrlsibm6f5J0x1G4RadwIsViX9c2vNANM8LYzkbSiCamQROWP0V2lUk74xZ96va77vZxIsAn9eBIeWafo0OSsrBYXDYgW8_73Ejif6Vy3MkZphp6bewGRgJQfjXbBxbAbRui7WjlM2uobswHdB04XlmOscp6uG1iEu5taDZNJ2-teutl50TRveo6ceUv7MKpYfNKHJUFwzTHHBEkHw5yIMHkcAgC7xYnP-shqQ3dQqh8eKNnmEx9qO4oLrd_CnqnFT5dAFw4-zdyn9C2MQ47ZbrzG8o3cxViFn3NDIUd7BIuVCkb7ErBy_DTJCyR91uq-pDfd7_x3SOdzjdPw_05oEBR9VIGzHiNZVP2H2sfTp_kQCIPUpvudQz8UZJq0lagHCtyIDkLH4gy6pANun1VVMdWqHk15v61GfjuLJt0JS2eQct25XUjqp0KsloSsUqlBhxu12qIOrgmrszu3t-NimUO5kNvK3XyYiUT-AYqycuKjjgFb7cqo0SuQcNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5605707ff5.mp4?token=TLMQ_ZnBd--qsBkJtOoz8bDKsLduy4rJxa9xYCSqz1WCvU-6vTrzbqV6fsxBVDHMyrUqtQRYBGnKu6rgP85yo6xKN_HBb4UZklAs3TOS7baS-NgKX-jox8rIHtZfL4Y4XKl3j4sd50eWSno-ahiBMEgB-4CNvV03xBiDKd0zIA2mM3Gjrlsibm6f5J0x1G4RadwIsViX9c2vNANM8LYzkbSiCamQROWP0V2lUk74xZ96va77vZxIsAn9eBIeWafo0OSsrBYXDYgW8_73Ejif6Vy3MkZphp6bewGRgJQfjXbBxbAbRui7WjlM2uobswHdB04XlmOscp6uG1iEu5taDZNJ2-teutl50TRveo6ceUv7MKpYfNKHJUFwzTHHBEkHw5yIMHkcAgC7xYnP-shqQ3dQqh8eKNnmEx9qO4oLrd_CnqnFT5dAFw4-zdyn9C2MQ47ZbrzG8o3cxViFn3NDIUd7BIuVCkb7ErBy_DTJCyR91uq-pDfd7_x3SOdzjdPw_05oEBR9VIGzHiNZVP2H2sfTp_kQCIPUpvudQz8UZJq0lagHCtyIDkLH4gy6pANun1VVMdWqHk15v61GfjuLJt0JS2eQct25XUjqp0KsloSsUqlBhxu12qIOrgmrszu3t-NimUO5kNvK3XyYiUT-AYqycuKjjgFb7cqo0SuQcNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مستمرين بالمواجهة لن نخضع ولا نركع إلا الله .. والسلاح هو ملك وخزينة للدفاع عن الشعب العراقي والمستضعفين
المقاومة الإسلامية كتائب سيد الشهداء</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/86570" target="_blank">📅 22:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86569">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
يواجه البنتاغون حقيقة متنامية بعد أشهر من القتال في إيران.
يتقلص مخزون أمريكا من صواريخ الاعتراض الدفاعية لدرجة أن المخططين العسكريين يدرسون ما إذا كان بإمكانهم مواصلة الدورة الحالية من الضربات الانتقامية المحدودة.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/86569" target="_blank">📅 22:09 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86568">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇺🇸
العقود الآجلة للخام الأمريكي ترتفع 1.29% لتبلغ عند التسوية 84.67 دولار للبرميل.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/86568" target="_blank">📅 22:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86565">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fG43g8zOAmay9RtgbzqdtGYiXmdAcaf6RZGPUG_wrxfj39xHI0kVit1LpFK1iRzyK9j-RDUPIuOL934LV8qhIXiMI0eUeqn_z7W_rQR0kHov4oddn1U0NtF-h37hcujzjq46l-xC48lj8pnUrw44HXOXd3vV45pIE0Kg6Rw_qVUEhmddsY1eE2P_zhlAr3adT0QtLqBuMm_Fhr3EoT5sPgZykezUwbGSxaOF36d2zNsEK6Xro0AR_yQQ4nqIPport6NT1Y3e9dAUknz5daj1EheWOCpww28-5opJzshNkStr-NkjhpwtBtR18vB8EFVG3m600c6FXfnRBwD540JkJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CLCh3DDhdycR1JGxvy151wyGqLgDExisK1QSUeXJu8tN9to_ZTFRnCrLpTrtOd_BN57kYQb_8uyK62XwVG8IphoMNgs-WZwNZ_NqJ-qY95vjut0s-x8BI7qgrTUDK9PZNMfDnBW1oOcZcSWEZ8QyEGxbEEkh4gLWBxRcciBDlniFg-NK0R0eiiSQOzr7Q8tyO5ACtpsaYoR2fZ0RFMR4vr-ieAguDlN7bNmO0I8Wxcf5ZrhuWdkFYTx10UlAZ_Kr746efqZj4u82RE79G3E-VFGhu0PhQAAQMgF_ue3mMVVdcytcz9xJoNwtvB1wwe1gqevwTMyS9dNArDdRB9DVyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sbe-MC4Zah9PtRjRhekgnPcVqCrz5U6vLuxIkoLdiMoaNyOLbCMX8l8PshuNdBsw6u0PeD43v5UdJFr0vOYQZcuUS4ldD7EbL7Z3rsk3bF-TB5dTx9zTBYh8_KqLXafdLKpNBkn_HpvS_99jmmQwAW__raGVOsUh83ZNLxTVdVft1z5QUE9Oe6JZELKrEqZ5njfh8eo4I0TvE_fjROTzrkOkFduD-GY8Gs95PoeJ8KfcdvFJx9yye6dTg1aBOr9NjVoBBbK7lh6KwTMF18aqPCfbMtplGs2oB1IWu0_I28XLESigYblcqRAgZwVugArNULys0goeVK6Cz782-9qnAA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🤡
🏴‍☠️
🇮🇶
خلايا اوكرانية تنفذ هجمات في العراق وتُنسب للفصائل.. مستشار الأمني القومي يكشف سراً "لم يسمعه العراقيون" من قبل</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/86565" target="_blank">📅 21:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86564">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e0d6ec59a.mp4?token=ePzGWfHt4Rj6W0NH2UcPniOcnB0LFcjmrJVFu9lcMh-1Uyes7hST-7H3a71jb6pNQQyj0htXaOA-y-YoIDuWEfPTfTzOCdlQlpMmCtxNgQAb1TutB1PQ_rw2RHWibgWM9FE1pKIbSNsAL9x7NsbkLFolz25AZd__D6WEjy6hf-JUfFoom3oJ2sUY2X0qCfkAgV2kBw29yfBmQiFM1IB8v2x3bOWlSKulYF8fuwZ79UrI507NH9dUmc7PjFYynj5Vx2eJlal7ZTl91VaG9QPzBIWSVP_k_vlgwyCP6oyxwviUzIPRLt9a6uND8AS2UtWD4IBk4T0NbuJcAVGhuU0h8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e0d6ec59a.mp4?token=ePzGWfHt4Rj6W0NH2UcPniOcnB0LFcjmrJVFu9lcMh-1Uyes7hST-7H3a71jb6pNQQyj0htXaOA-y-YoIDuWEfPTfTzOCdlQlpMmCtxNgQAb1TutB1PQ_rw2RHWibgWM9FE1pKIbSNsAL9x7NsbkLFolz25AZd__D6WEjy6hf-JUfFoom3oJ2sUY2X0qCfkAgV2kBw29yfBmQiFM1IB8v2x3bOWlSKulYF8fuwZ79UrI507NH9dUmc7PjFYynj5Vx2eJlal7ZTl91VaG9QPzBIWSVP_k_vlgwyCP6oyxwviUzIPRLt9a6uND8AS2UtWD4IBk4T0NbuJcAVGhuU0h8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ارتفاع اعمدة الدخان من وسط القاعدة الاميركية في ولاية كاليفورنيا. وتدمير طائرة F35</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/86564" target="_blank">📅 21:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86563">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67da2ed6f7.mp4?token=cu8DvjjPgiXi-nLhoHH9YhAUzOlu-wtmI0M_rHUv4HGu3980ZQloM4Jp7XZoppkhGJ3X7KSml82g5HWSLtKGm-OMB-b7GDbYefzx_DHvMhFL6RrHGTVGlxiJAjwmaFWyi731yo4_eYT3XTYOwOxPuAtBrVW_0kp2FPJRQ2RqOG-GE4N6t_5lRrUsAn3VzXucIdR9XrHUEcj1eUqtPwQiiktMbsPgVZnbL3HU2z0tTD4kImdKQ3bnPs4egl0prRDk16VWeRY_ZT0p-swKTSMCJUBzCKapaWO9TSgCZGi9b3i_sR3Q2oy2X_T74UkohyT8Vti1A33hBYaLg86Roh8OQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67da2ed6f7.mp4?token=cu8DvjjPgiXi-nLhoHH9YhAUzOlu-wtmI0M_rHUv4HGu3980ZQloM4Jp7XZoppkhGJ3X7KSml82g5HWSLtKGm-OMB-b7GDbYefzx_DHvMhFL6RrHGTVGlxiJAjwmaFWyi731yo4_eYT3XTYOwOxPuAtBrVW_0kp2FPJRQ2RqOG-GE4N6t_5lRrUsAn3VzXucIdR9XrHUEcj1eUqtPwQiiktMbsPgVZnbL3HU2z0tTD4kImdKQ3bnPs4egl0prRDk16VWeRY_ZT0p-swKTSMCJUBzCKapaWO9TSgCZGi9b3i_sR3Q2oy2X_T74UkohyT8Vti1A33hBYaLg86Roh8OQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات داخل قاعدة عسكرية أمريكية في كاليفورنيا</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/naya_foriraq/86563" target="_blank">📅 21:09 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86562">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">انفجارات داخل قاعدة عسكرية أمريكية في كاليفورنيا</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/86562" target="_blank">📅 21:07 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86560">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZlnFTEHyag_86UGniRf_SdiaJW5lzuqMkofFi3RtbAsAcxkngRjf_lBriTmgiiPT_n0s2Gx-wugv56sl8LZPaCMpDuzoPSnNYLbA7LMJ3iHUUK4uSsqr4GoARl4VLIPTn4nkmn25tN2n90dcxiuHyu9kI3oSyTUHFTsWff2ZD52fDa0L4PO0cMMk36zqXBwCOUmIMWm2HNXoEbxKM-Xm393fn938CZwiGCv7Xhm47i5hTFJDtl_WwbeIe4DKxsOfUPWE0BdXacIfdlTEr3y08xhxIFUc7h811dwa7lJ2FAE45Aeq1sC_bpWBluqN5Vk9yX4ah6gCqdYaC9ZalgqQeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتصرنا
😆</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/86560" target="_blank">📅 20:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86559">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be4999db8b.mp4?token=P9sRrNslLPNH6qvNmXuMPZ2iqsRh5PxBWN-wav90QG8axBdZOkVdQjsR0qn2j7RCShXW5Y9LIibEf3joIgMpwhRlb451yaPCXW8UkHOrDrJV095GQrpl3UJvx5KckghnwgoXMZv1Rsi_-cALrvhhYVUm8g5fOH9nmsww6hOgcrusHlkSRXJazpmHr6DrMHj5CZZNrKybl6jHXra20rR_rbYc7X_gssL0QeFP1daY85Yhj5kGKHz5uHxkLrxUfP9TN-M3AhiBt8OzQtBwyFB5bSqD550M6k1mIyKOIPkmQxJdnWWgmR2tHBqb8jW5UDpxKk61Oz1i9t2s2RX2XcjwJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be4999db8b.mp4?token=P9sRrNslLPNH6qvNmXuMPZ2iqsRh5PxBWN-wav90QG8axBdZOkVdQjsR0qn2j7RCShXW5Y9LIibEf3joIgMpwhRlb451yaPCXW8UkHOrDrJV095GQrpl3UJvx5KckghnwgoXMZv1Rsi_-cALrvhhYVUm8g5fOH9nmsww6hOgcrusHlkSRXJazpmHr6DrMHj5CZZNrKybl6jHXra20rR_rbYc7X_gssL0QeFP1daY85Yhj5kGKHz5uHxkLrxUfP9TN-M3AhiBt8OzQtBwyFB5bSqD550M6k1mIyKOIPkmQxJdnWWgmR2tHBqb8jW5UDpxKk61Oz1i9t2s2RX2XcjwJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب: إنهم يتحدثون عن البرنامج النووي لمدة سبع ساعات. وأقول: "لماذا سبع ساعات؟ يمكنكم إنجاز الأمر في خمس إلى عشر دقائق."</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/86559" target="_blank">📅 20:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86558">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇺🇸
ترامب: إنهم يتحدثون عن البرنامج النووي لمدة سبع ساعات. وأقول: "لماذا سبع ساعات؟ يمكنكم إنجاز الأمر في خمس إلى عشر دقائق."</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/86558" target="_blank">📅 20:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86557">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7828268882.mp4?token=Y5NfBOUDJRQB2m7qaYdePSG3hN_kGmc0mDAL164USAK-PnCb9c-qnk7kf_csKRlbTAjMhQaDljGzxJWRehSUKmBjzqcyhNbygKrEv6iEtT1Q7sg9qRFfZFRztsdRFVEZj2qEvNuU352KCvdykIgecM34NIw2qudTJ56tLcHXyr1gEF0I66BIHJVmMyLOsjddhK8gOrgBmP6n-vELxBlE3XgXK7unydD7EN-tp1bwJeYQ32hl45oFYwLa09LzJCRdPaRi64JV-1EZJWL4cbBrnIRvefeyaGLugmhZicqrgfAGvYap4MqeUwlE_eWqPu6GY8dFey8_wC5twRPam76SCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7828268882.mp4?token=Y5NfBOUDJRQB2m7qaYdePSG3hN_kGmc0mDAL164USAK-PnCb9c-qnk7kf_csKRlbTAjMhQaDljGzxJWRehSUKmBjzqcyhNbygKrEv6iEtT1Q7sg9qRFfZFRztsdRFVEZj2qEvNuU352KCvdykIgecM34NIw2qudTJ56tLcHXyr1gEF0I66BIHJVmMyLOsjddhK8gOrgBmP6n-vELxBlE3XgXK7unydD7EN-tp1bwJeYQ32hl45oFYwLa09LzJCRdPaRi64JV-1EZJWL4cbBrnIRvefeyaGLugmhZicqrgfAGvYap4MqeUwlE_eWqPu6GY8dFey8_wC5twRPam76SCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب: الدبابات الروسية كانت متجهة إلى كييف، لكنها علقت في الوحل، قرر أحد الجنرالات السير في الوحل بدلاً من السير على الطريق السريع، حيث كانوا يتقدمون بسرعة.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/86557" target="_blank">📅 20:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86556">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf2738436a.mp4?token=RWR9HrNWTbHvzeWqxP0iw5E7-6wGu-95HkBxt8fuBFWjYQtYQHJX2n5POlce32jBqkEgGXYJ-DTdionQhwdfYKMjEsJ33ELYAal54efHNqvJxG8HGa6aJpdeog8SEPZbW48ff8Fwxceqo_bSZq46ZRR7tY0CR6GnzjTWhphlf3rozwpVrxNXIuUwQMSpvUxB6zPMRN6fhKGiSuhl4hp9lGwSrjNajd477cfDmfJYUNUo9ClQllvWWxu6zXRzZLIjMg0R0kAIVelIep_mPWYaW0TfjNd0vyu8qC-6IcSfqlxeLhniU1wDACdCxPY0D3TbkU1g0k9h4gsCgZt9R0NtLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf2738436a.mp4?token=RWR9HrNWTbHvzeWqxP0iw5E7-6wGu-95HkBxt8fuBFWjYQtYQHJX2n5POlce32jBqkEgGXYJ-DTdionQhwdfYKMjEsJ33ELYAal54efHNqvJxG8HGa6aJpdeog8SEPZbW48ff8Fwxceqo_bSZq46ZRR7tY0CR6GnzjTWhphlf3rozwpVrxNXIuUwQMSpvUxB6zPMRN6fhKGiSuhl4hp9lGwSrjNajd477cfDmfJYUNUo9ClQllvWWxu6zXRzZLIjMg0R0kAIVelIep_mPWYaW0TfjNd0vyu8qC-6IcSfqlxeLhniU1wDACdCxPY0D3TbkU1g0k9h4gsCgZt9R0NtLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
المراسل: ذكرت أن إيران لا تزال لديها بعض القدرات. هل يجب على الأمريكيين الاستعداد لمواصلة هذه الهجمات المتبادلة حتى تصبح إيران غير قادرة ببساطة على الرد؟ ترامب: ستزداد قوتهم قليلًا، ربما الآن، ولكنهم سيصبحون أضعف. نعم، بالطبع. يجب دائمًا أن تكون حذرًا.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/86556" target="_blank">📅 20:09 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86555">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddb7c06f17.mp4?token=dxw_XaPlTMT-V4rU6dkd5q57qdpQRjQpdzTPqsbkreT5o63mLL3DOyK_nGNesYpc4I3hDwaSXtJYtmzIysRF1tbx8WG79dBBwlw95VJcGXPad_kmm6ibKH_B8Y7UqFLj42pgYjI1LL1bXwE1jiOXxGJgA7x12Iayx-EfwdT19qoIyr0JFPiTfPcsqWN9kkcJBvPqPh8gKPZkik4FJXdAkEqBG3TT6vxR8hdL6M_nVldraQcZSJD8gTscOIRbOg3qxaZ1FCHzt3bwFxxnJeY2GyDhWQ3Q3svpLSjkbwXlA2pV6fThjLpQPoYN74TTCZUlziiu4soatKK3ANb6ppdNfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddb7c06f17.mp4?token=dxw_XaPlTMT-V4rU6dkd5q57qdpQRjQpdzTPqsbkreT5o63mLL3DOyK_nGNesYpc4I3hDwaSXtJYtmzIysRF1tbx8WG79dBBwlw95VJcGXPad_kmm6ibKH_B8Y7UqFLj42pgYjI1LL1bXwE1jiOXxGJgA7x12Iayx-EfwdT19qoIyr0JFPiTfPcsqWN9kkcJBvPqPh8gKPZkik4FJXdAkEqBG3TT6vxR8hdL6M_nVldraQcZSJD8gTscOIRbOg3qxaZ1FCHzt3bwFxxnJeY2GyDhWQ3Q3svpLSjkbwXlA2pV6fThjLpQPoYN74TTCZUlziiu4soatKK3ANb6ppdNfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترمب: إيران تريد دائما التفاوض وتريد التوصل إلى اتفاق معنا، ويمكن التوصل لاتفاق مع إيران،ويتكوف وكوشنر وفانس وروبيو يشاركون في محادثات متعلقة بإيران.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/86555" target="_blank">📅 20:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86554">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a25f78e699.mp4?token=Jnw0tOtLxxJqH0qNvmkkEcV0lBqKfdhOLUB8M_U69sQkdBDU2dpVX1HhHxsoQ6OR0TbW-JCD7Xjkkk1p3cpO55uBIjS_UWiZG5fI_3C7EemwABVQe2e8Zbzo09RzGvaDgL-pppsxCTZBmP6V9HqBfWLdOHz9BFnsfJNeXcSPuCrQcFbOYVt74Rhm_HLJ7yIlj9tf3wwzbmCgzAPDFROJvQb_qsRu9Mrxq9IfmU-mfyDXlW7R_cft_1bC-AwEI0w-G7KslAKAI3qt7QidblVW1pFwogE7oPr8plC2tKJHdI3OWQ6nP-b3qEIWqeunQ9ZrmVoisOxwpTLG_KjJwdaKww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a25f78e699.mp4?token=Jnw0tOtLxxJqH0qNvmkkEcV0lBqKfdhOLUB8M_U69sQkdBDU2dpVX1HhHxsoQ6OR0TbW-JCD7Xjkkk1p3cpO55uBIjS_UWiZG5fI_3C7EemwABVQe2e8Zbzo09RzGvaDgL-pppsxCTZBmP6V9HqBfWLdOHz9BFnsfJNeXcSPuCrQcFbOYVt74Rhm_HLJ7yIlj9tf3wwzbmCgzAPDFROJvQb_qsRu9Mrxq9IfmU-mfyDXlW7R_cft_1bC-AwEI0w-G7KslAKAI3qt7QidblVW1pFwogE7oPr8plC2tKJHdI3OWQ6nP-b3qEIWqeunQ9ZrmVoisOxwpTLG_KjJwdaKww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب بينغ بينغ بينغ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/86554" target="_blank">📅 19:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86553">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇺🇸
ترامب : "إيران كانت تمتلك أسلحة دفاع جوي متطورة جدًا، ولكنها لم تكن فعالة."</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/86553" target="_blank">📅 19:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86552">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/377310bac7.mp4?token=t8pW_7yWGLX6ca15kCyc9m3IQRbm2S1z0qppsJ1M1DlvqrVylK7ztpcKt68DXc-_3Q7wkUtKEW7bDS18-ptXCZ64jXYND5HHERmQqmflNZpnr34HlIe2kJF_-zNSVTuoOW4iM2oeAqnYdAZfgiIbIJJgRSXuERZuSWypmoIE7ru8TmH89JVvYsip112hi8SHrhAQdaK2tzHCHz-B9WZg8gwnTvJtZ1lLpRsDqkfOcJpM2RvAcnABPXoYaqwQkTJU3i88PKb29af8yzLkOzdswZWDU9LAgFUmPoRMsMGiJdsAFwOQsrnuiVuc1pTmopsQz7Brsni7IKcJS32fa56zTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/377310bac7.mp4?token=t8pW_7yWGLX6ca15kCyc9m3IQRbm2S1z0qppsJ1M1DlvqrVylK7ztpcKt68DXc-_3Q7wkUtKEW7bDS18-ptXCZ64jXYND5HHERmQqmflNZpnr34HlIe2kJF_-zNSVTuoOW4iM2oeAqnYdAZfgiIbIJJgRSXuERZuSWypmoIE7ru8TmH89JVvYsip112hi8SHrhAQdaK2tzHCHz-B9WZg8gwnTvJtZ1lLpRsDqkfOcJpM2RvAcnABPXoYaqwQkTJU3i88PKb29af8yzLkOzdswZWDU9LAgFUmPoRMsMGiJdsAFwOQsrnuiVuc1pTmopsQz7Brsni7IKcJS32fa56zTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب حول إيران: "نحن نريد فقط الفوز.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/86552" target="_blank">📅 19:51 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86551">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caed943dd3.mp4?token=CY0H0cu6XBZ4QmS0-Tt7cWEzLi9QcGqMEUzDypKKzZw1lyoRYPAdEQnzm5Jvj_44Bd5q_zwwQbeEcuQFdc1VWy8xFLeA_uGe-SBJADoG1MZ3lQR26GcsVNXAGDMpTLdTgGTxkrkR4I0dNUlT9TIDQPjlsOK6FoYJdGASlFH5DQLVrEglgnxafNwA5LkfHyicNwcgsoB0OhMwbwlSnpGwfn13vFFxHkcB4MDm6Xlh46zladNSXopyp-x_NZn4170K2HyrdPj5XkG4x73NtXaGp0E9h7iGtBZculGcifpUJQyxkwJDGNzl3A6BeTZgIBVTB_mWYn3T6QdUgyYhHj35gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caed943dd3.mp4?token=CY0H0cu6XBZ4QmS0-Tt7cWEzLi9QcGqMEUzDypKKzZw1lyoRYPAdEQnzm5Jvj_44Bd5q_zwwQbeEcuQFdc1VWy8xFLeA_uGe-SBJADoG1MZ3lQR26GcsVNXAGDMpTLdTgGTxkrkR4I0dNUlT9TIDQPjlsOK6FoYJdGASlFH5DQLVrEglgnxafNwA5LkfHyicNwcgsoB0OhMwbwlSnpGwfn13vFFxHkcB4MDm6Xlh46zladNSXopyp-x_NZn4170K2HyrdPj5XkG4x73NtXaGp0E9h7iGtBZculGcifpUJQyxkwJDGNzl3A6BeTZgIBVTB_mWYn3T6QdUgyYhHj35gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب حول إيران: "نحن نريد فقط الفوز.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/86551" target="_blank">📅 19:51 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86550">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1facef9bcc.mp4?token=JRel8cWI7lKTaoUa4eEXcSjV7_dfEBCw3P9Fb0-Rn2xstduOUuiN-67UxvtoTSkKHx5xa0v5FRakVF0xfdUVrAqthlxftegt4JHeZ8SLjt1Czw21Rn-nZpLxI39S5FEoCCbd1u_AhDADmGKtSKN2v03LEVhEzFfLBoAVdaTTsLgocMciHwI4Xo4zh_HuG-q_7ANTTttUA-OnncW9bj6HXZXBUHz40U3EH_yxdWj-wQf7hMeu7oUOJVrfotzILxa0dlveW3O5BS-r-nbntMeF25SIpVINk8A6XF31K9JuXMQkDzpmFOfjANIsRk6hypWsmMLaawJy_I68JfR7fQKs1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1facef9bcc.mp4?token=JRel8cWI7lKTaoUa4eEXcSjV7_dfEBCw3P9Fb0-Rn2xstduOUuiN-67UxvtoTSkKHx5xa0v5FRakVF0xfdUVrAqthlxftegt4JHeZ8SLjt1Czw21Rn-nZpLxI39S5FEoCCbd1u_AhDADmGKtSKN2v03LEVhEzFfLBoAVdaTTsLgocMciHwI4Xo4zh_HuG-q_7ANTTttUA-OnncW9bj6HXZXBUHz40U3EH_yxdWj-wQf7hMeu7oUOJVrfotzILxa0dlveW3O5BS-r-nbntMeF25SIpVINk8A6XF31K9JuXMQkDzpmFOfjANIsRk6hypWsmMLaawJy_I68JfR7fQKs1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مشاهد حصرية لنايا...
اقلاعات متتالية من قاعدة الاحتلال الاميركي موفق السلطي في الاردن.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/86550" target="_blank">📅 19:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86549">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇺🇸
وزير الحرب الاميركي بيت هيغسيث: هل تتساءلون عن سبب عدم مشاركة الحوثيين في هذا الصراع، على الرغم من أنهم عملاء لإيران؟ ذلك لأنهم شعروا بوزن القوة الأمريكية لمدة 45 يومًا.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/86549" target="_blank">📅 19:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86548">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇮🇶
الناطق باسم القائد العام للقوات المسلحة العراقية:
القائد العام وجه برفع مستوى الإنذار والجاهزية في جميع المعسكرات والقواعد
القائد العام وجه بالخطط الاستخبارية الوقائية لإحباط أي استهدافات أو محاولات اختراق
توجه لتسريع خطة التجهيز والتسليح الخاصة بمنظومات الرادار والكشف المبكر والدفاع الجوي
حماية الأمن الداخلي مسؤولية حصرية لمؤسسات الدولة العسكرية والأمنية
بعض الأطراف الخارجية تحاول إقحام الأراضي والأجواء العراقية في حسابات الصراع
منظوماتنا العسكرية والأمنية تتصرف بأعلى درجات الانضباط والجاهزية</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/86548" target="_blank">📅 19:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86547">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/488504489f.mp4?token=VakH3D8lPWIzjLDjz_bTIGIjjFLdRdELe4Ceikid4NnWkP96583jG30H_aRbpcG3p8htFLNcGLUxGsrjl-NzN_CEvmZl0assU4wRgeY5WJ-1appoEacQdYlyxScjhImr4jFP5TuKaWYcKBAQWvswXmfu1iC3Sxe2PEA_-c1s7tm6CFylWIGeebABK3UzTf4zhbsFbABaYS7jcGjCzDL40I94TmQUj8118GmDxNtZa74C80iB19eYfEfr49T8C9d3h5pKWMgX00ClGtUe3bmavHrJyPWrkqyn9DI1_Zxlt-rkU0MD73GTGTbTcFilBeQSTXlvBDe261MnRchhsZE9sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/488504489f.mp4?token=VakH3D8lPWIzjLDjz_bTIGIjjFLdRdELe4Ceikid4NnWkP96583jG30H_aRbpcG3p8htFLNcGLUxGsrjl-NzN_CEvmZl0assU4wRgeY5WJ-1appoEacQdYlyxScjhImr4jFP5TuKaWYcKBAQWvswXmfu1iC3Sxe2PEA_-c1s7tm6CFylWIGeebABK3UzTf4zhbsFbABaYS7jcGjCzDL40I94TmQUj8118GmDxNtZa74C80iB19eYfEfr49T8C9d3h5pKWMgX00ClGtUe3bmavHrJyPWrkqyn9DI1_Zxlt-rkU0MD73GTGTbTcFilBeQSTXlvBDe261MnRchhsZE9sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب :لديهم بعض الصواريخ المتبقية، ولكن لديهم عدد أقل بكثير مما كان لديهم قبل أربعة أو خمسة أشهر، قدرتهم الإنتاجية قد تضاءلت إلى حد كبير. قدراتهم في مجال الطائرات بدون طيار قد تضاءلت إلى حد كبير، ولكن لا يزال لديهم بعض القدرات.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/86547" target="_blank">📅 19:30 · 09 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
