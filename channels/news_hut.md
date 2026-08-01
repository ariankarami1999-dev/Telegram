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
<img src="https://cdn4.telesco.pe/file/groI5xTpwv63gfZoi6J4nCDzOlcRYiL7alhPvmfSys8QS9iuFLn3N4KNX-dCNvym4v7j0bdQxS-ogrXW9QKkfhpqlFGC3LOOBlCFSi8DRxzRuhYuE12uKp8IWm5Q8oYnn5Dd6VABPOEdQ4RbRomkd5R03bDxF0BH2YU7It7nbLOcUU9Cvz57HF-l9sqznIzP27GAnZa4Wd98L-up_IT86s7Q0swHckr9_HxE5knU8gqfbWkSkbl1uv0dmCtMAmd5XZjW_L0lexBSNtKYIUgxAC_TWi6gkWzI0GZNdqQS4Ab_2Urlor3LYszHLvS5KhYuyEDAEpu4KLX0Q9TxtVkY0A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 139K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-10 15:08:29</div>
<hr>

<div class="tg-post" id="msg-69360">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MF55sVkMx6tJwMq7iEV5cmHfiEJgNyK8dZvkvfK944Mc897vksBO9OS0yd3I0h-THTlgugwUVO-B_ODfh2Wp-DKWhMFn7NR02zXKjjo-3zI7ldgeRe27UkbWIZ8111oy7F5fDRtQCpoXTG4BfVFCycrZtixftIzj_HbTQyrA6Ybr17Q3J-Lf6UdA3S6Cj7rIt_waVLcJKOKZ5PqlddpRBlEoM5Dk4wC7SUgZRP67OYo_pae7KEWEASDmC2b4UOHl-7Oy_UTBxr0uAz8FUv5g3I2Z2v1Fh39Mf6bnDND6MFnNO8QE431UPXtuepmnv_AHAhehJedc2TKzvQfxUg4b_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G_dyHqVFbzlAhCW9qC6bLeHjS_1dIPa4DH_BaaTYBGsqNKrcBWipWFWz7lDHK1uREA84ElSyN4EHmQ9scU9s4C5iaJs_Zu0G02Ja_moEAwEeRFJ--ePMO7NPAhniL1RE2Z-vLznvERf6r8HGEFnqWNx5x34zD4bd8hG6MEm4u-lyVzXxvi3ZzCHL8qsajtVIGVmL9hg1VNFHxCTENVPmSAgIgTVFV7BJP8lBbdP6kFl6wMBkWXv7z56rP7Oft8_38ShP2hNJXiPYgRrOONwS7XocW8Vj8BfG_KqojCRofNYwMVVLlN--A7lVKpWB8zpj6DmNsv-ou9IPAvH1toKIXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
سفارت آمریکا در اسرائیل و عراق:
آمریکایی‌های حاضر در منطقه باید آماده باشند و در صورت تشدید تنش، خروج از منطقه را در نظر بگیرند.
@News_Hut</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/news_hut/69360" target="_blank">📅 14:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69359">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bz4SiBeuFip66tG-OMYnXwo44le9Vwu22SxgprTP-et7LAUIGMR9kIir3J25MvRZyqJdfzzN5Qi0psPkRoniGE1RBBguqrAqaq_WBMRktVOGbNUcW_az-BaYfN2mu7eTthunjhdzRQyn9EfzGIaRmoV_uyFBXADFgaOFFS5jkEkG6iJ-B3gycrow3mvvR3uO0juIZwNyQqn4i6TQtw5wfnks_22t3wzcyY66OgZ7nkbFWerkLGaJ2tAyza7Ucfwgr3wp8HZfO69PlCXpTe2UESYNuoWRXRhEhe-5GkvkiMCtmk3GedwkjrnAlCXlLxjDQG4c1FTcafoHsjJS7aLAPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تسنیم:  بهمون حمله نشده، گلوله توپ زمان دفاع مقدس ۸ ساله منفجر شد.  @News_Hut</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/news_hut/69359" target="_blank">📅 14:42 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69358">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
تسنیم:
بهمون حمله نشده، گلوله توپ زمان دفاع مقدس ۸ ساله منفجر شد.
@News_Hut</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/news_hut/69358" target="_blank">📅 14:16 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69357">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
دقایقی پیش از حوالی اسلام‌آباد غرب کرمانشاه، صدای چند انفجار شنیده شده.
@News_Hut</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/news_hut/69357" target="_blank">📅 14:13 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69356">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c794c22fb.mp4?token=OirU70hTBtw_mLwloGcQ_8J4RTiPedGODYFn5UXdTuxNCwIyyzQTDpT1Gp_QTv0fzXmNJAQgHZUHQaZmqkwnWlsp1i6Q20vYpgytzSMgSS7ryxMbyXS0Hif3jOH4RlKzvSaoDPt4Z5ZCxzJhUITYTtHPOWkPweicXzoqeGmzmG1Jvju0RdPWhZp9U-A7lvHz-ybWmd6FNP5Ya6_C99liVVjonmq8zVDtopaAHmVwxS5Qo3790HGQ86uhVmRkP9aDjtWT8ASLcLNaowE0cBhdp2bR5I7khIGgPCqMRmAlnT12dmRnei4FjvVv8iVR44C_KS1A8V3AlsYEN5E59YlEVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c794c22fb.mp4?token=OirU70hTBtw_mLwloGcQ_8J4RTiPedGODYFn5UXdTuxNCwIyyzQTDpT1Gp_QTv0fzXmNJAQgHZUHQaZmqkwnWlsp1i6Q20vYpgytzSMgSS7ryxMbyXS0Hif3jOH4RlKzvSaoDPt4Z5ZCxzJhUITYTtHPOWkPweicXzoqeGmzmG1Jvju0RdPWhZp9U-A7lvHz-ybWmd6FNP5Ya6_C99liVVjonmq8zVDtopaAHmVwxS5Qo3790HGQ86uhVmRkP9aDjtWT8ASLcLNaowE0cBhdp2bR5I7khIGgPCqMRmAlnT12dmRnei4FjvVv8iVR44C_KS1A8V3AlsYEN5E59YlEVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه جوون عرب داشت به زائرا میگفت بیاید آب انگور بخورید که یه ایرانی رسید و بهش گفت:
آب‌انگور نه، بگوآب‌شنگول
@News_Hut</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/news_hut/69356" target="_blank">📅 13:50 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69355">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/917485436c.mp4?token=FEOkF7gZuO8e_rhVzD4hp_Yi4tSK-VI2eVseVWC7DpjGTq3eWAco2U9UWPbONzB2TUXzFRYaDXRw4ji59epu_I1jJS3NxyQ1VNlPcC7bJkvRrgDqrw8GOWWyInlDXsaMf6P8FOF-WmIEB98d4A7lervTWwOlsIj3cwfO89sxDG7KuR5IRZ7-M68421MCMmL7tGtL7x_Av8Y-hLHCGgWRPaPO2Ds94Cdo_jWWjQlZy2YV8-IcE3004EBzuX80NihFdk2k9ckqk7gPHaMD6nS72ifAjggxxXfniVkuoG5uHnkoizRcAEk9QW2o2_wSUQSGMEx36qB0rWUwTVqUD0SNRJ_96tkQMBGsrsfvcSGy3wUM2CzzQG2ifjkFJCjZ2WVVmn4anLCqKkDwcbQBW2VpFQgYNWYIlKrdJLG2OYEGX_VaFUdeCEixOnY7hGFktL9G5HODfgBefl--uKC7aTWGgTkGwGGZ6HPVsDvrqjrryPKs48JsULjKnQg_wpO5qAb1x7IKEn9_cEM4HIWAsixJGBKgoR2WTf3j45esqHV4aGMWdG86beY2XyR0g5pwWjyj6mfuOE7Z9o7CaSyuRB7aEa5ypu2XxMBfrZ9ZInQpUBUOaZckMdonNWzfMWHt3BHlFP6yjGSNTEyqpoa1AaX5Da-VD9z-VFnkz--P8xQDcr0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/917485436c.mp4?token=FEOkF7gZuO8e_rhVzD4hp_Yi4tSK-VI2eVseVWC7DpjGTq3eWAco2U9UWPbONzB2TUXzFRYaDXRw4ji59epu_I1jJS3NxyQ1VNlPcC7bJkvRrgDqrw8GOWWyInlDXsaMf6P8FOF-WmIEB98d4A7lervTWwOlsIj3cwfO89sxDG7KuR5IRZ7-M68421MCMmL7tGtL7x_Av8Y-hLHCGgWRPaPO2Ds94Cdo_jWWjQlZy2YV8-IcE3004EBzuX80NihFdk2k9ckqk7gPHaMD6nS72ifAjggxxXfniVkuoG5uHnkoizRcAEk9QW2o2_wSUQSGMEx36qB0rWUwTVqUD0SNRJ_96tkQMBGsrsfvcSGy3wUM2CzzQG2ifjkFJCjZ2WVVmn4anLCqKkDwcbQBW2VpFQgYNWYIlKrdJLG2OYEGX_VaFUdeCEixOnY7hGFktL9G5HODfgBefl--uKC7aTWGgTkGwGGZ6HPVsDvrqjrryPKs48JsULjKnQg_wpO5qAb1x7IKEn9_cEM4HIWAsixJGBKgoR2WTf3j45esqHV4aGMWdG86beY2XyR0g5pwWjyj6mfuOE7Z9o7CaSyuRB7aEa5ypu2XxMBfrZ9ZInQpUBUOaZckMdonNWzfMWHt3BHlFP6yjGSNTEyqpoa1AaX5Da-VD9z-VFnkz--P8xQDcr0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
آتش‌سوزی در یکی از پالایشگاه‌های استان اربیل در اقلیم کردستان عراق
@News_Hut</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/news_hut/69355" target="_blank">📅 13:28 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69354">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/532a951287.mp4?token=aqNQxIZn8qqI52meX3weeRolN44rtf-ffVN1710vghGa2buC7Z7klwwnEW-ZNnPbcuWDNVl_ddJLeTZI691aeXj-Ad_xtQCOW7kRHXr6r06g50_op_zC3QGRgFgC3Dx-U6nJUXGmUGEaa0k8hqWO0CFwbDXMoV4bJBfsXDq7BcL8KPa6Xfr8g5-TB22vKQFGUmU4XaPG98lxdkyd67SeDbJJ6oxyUazu3l7VieEb-Sm3mO09sQDBhswSjZ5pbMNWY4f-l-HVRi2rwhwJOuoVpaUvlKJ4Fygi8yfVVQgg_agnpTglbmCWP3x-nIb1iVrtgWRpz540hcjZKmbbtpntxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/532a951287.mp4?token=aqNQxIZn8qqI52meX3weeRolN44rtf-ffVN1710vghGa2buC7Z7klwwnEW-ZNnPbcuWDNVl_ddJLeTZI691aeXj-Ad_xtQCOW7kRHXr6r06g50_op_zC3QGRgFgC3Dx-U6nJUXGmUGEaa0k8hqWO0CFwbDXMoV4bJBfsXDq7BcL8KPa6Xfr8g5-TB22vKQFGUmU4XaPG98lxdkyd67SeDbJJ6oxyUazu3l7VieEb-Sm3mO09sQDBhswSjZ5pbMNWY4f-l-HVRi2rwhwJOuoVpaUvlKJ4Fygi8yfVVQgg_agnpTglbmCWP3x-nIb1iVrtgWRpz540hcjZKmbbtpntxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه لیلی فیلیپس پورن استار معروف که تو 24 ساعت با 2 هزار نفر سکس کرده بود!
دوس پسر لیلی: من اصلا از این موضوع ناراحت نیستم، چون اون واقعا زحمت می‌کشه.
مهم اینه که آخر شبا میاد پیش من، و اینکه من بوسیدن رو براش ممنوع کردم، اگه با بقیه سکس کنه مشکلی نداره، ولی فقط باید منو بوس کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/69354" target="_blank">📅 13:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69353">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d26851041.mp4?token=oP1afYrT6-l0X7IVrHxjz2E4qXn8yu7WMwJm8Lil7yCSTAy_zCO6L1eRccbLr3njIRku36wFYyxZWfe0XNzUIcJZTKaWgZHJy0CdCKsfQO8chOuUGBiXAWVWzLQS3W1JQ_rDm3ChiycZBROP--yf2vfxdUVjkSNoTXZc6CK3bs-sYsBr40RmQjvyQ24HTDcW0UwL79qFBff0VQWTqsVPXbFhxvKujRqlxrEWNgjCAEbQhkbKQAqDsBvQ2txyo_9PSbZtr98s9XLyXX7Bv7Yz8s42Gv9DGCS-VOGvYMoceVdAhu0IpKvBG29dNggEHcEanhKQ_mP3uTicdTzwTxFTog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d26851041.mp4?token=oP1afYrT6-l0X7IVrHxjz2E4qXn8yu7WMwJm8Lil7yCSTAy_zCO6L1eRccbLr3njIRku36wFYyxZWfe0XNzUIcJZTKaWgZHJy0CdCKsfQO8chOuUGBiXAWVWzLQS3W1JQ_rDm3ChiycZBROP--yf2vfxdUVjkSNoTXZc6CK3bs-sYsBr40RmQjvyQ24HTDcW0UwL79qFBff0VQWTqsVPXbFhxvKujRqlxrEWNgjCAEbQhkbKQAqDsBvQ2txyo_9PSbZtr98s9XLyXX7Bv7Yz8s42Gv9DGCS-VOGvYMoceVdAhu0IpKvBG29dNggEHcEanhKQ_mP3uTicdTzwTxFTog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از عوارض خوردن ساندیس زیاد
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/69353" target="_blank">📅 12:30 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69352">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e653ac6e6.mp4?token=W6M45h0ohiDOIxmUAiZgQVKkysaZHHL27MkCGzHdFpsRQzkMH80HYT9YrFivuB8ioJP_UmwnmwL1hvnWW0UpNTnFu7D3J5zwlFCG701BsBn1Afb2QDKdXevB0XmxNKPWobbYe_lXysh3ZRyvMG8oXGfojQ5Ur2YzVXOb_mbteIK2DpQw59Mb0Nrflj80MM9hv5pGCT942v2TdVFXx3qtoOzEjayoaFd_xINYAdAJZ_8prjKh4jeqp49tKw5phjxl7tZbH0vvoLyTGi6HKgRvmcfRaoXo4W2rL6M4v3RH0JVuub1xVL9pcBSxKjIfN_aHUOK5Fy-GQHzg2DJv4tzQfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e653ac6e6.mp4?token=W6M45h0ohiDOIxmUAiZgQVKkysaZHHL27MkCGzHdFpsRQzkMH80HYT9YrFivuB8ioJP_UmwnmwL1hvnWW0UpNTnFu7D3J5zwlFCG701BsBn1Afb2QDKdXevB0XmxNKPWobbYe_lXysh3ZRyvMG8oXGfojQ5Ur2YzVXOb_mbteIK2DpQw59Mb0Nrflj80MM9hv5pGCT942v2TdVFXx3qtoOzEjayoaFd_xINYAdAJZ_8prjKh4jeqp49tKw5phjxl7tZbH0vvoLyTGi6HKgRvmcfRaoXo4W2rL6M4v3RH0JVuub1xVL9pcBSxKjIfN_aHUOK5Fy-GQHzg2DJv4tzQfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
قالیباف: میخواستیم خبر شهادت رهبر را ساعت ۸ صبح اعلام کنیم اما تلویزیون‌های خارجی، زودتر اعلام کردند
.
در روز نخست جنگ و تنها یک ساعت پس از بمباران بیت، شهادت رهبر قطعی شده بود.
تا همدیگر را پیدا کنیم و هماهنگ شویم، ساعت ۸ شب شده بود.
قرار شد خبر را فردا ساعت ۸ صبح اعلام کنیم و از مردم بخواهیم به خیابان بیایند. اما تلویزیون‌های خارجی، [ منظور اعلام رسمی ترامپ]  خبر را ساعت ۹ و نیم شب اعلام کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/69352" target="_blank">📅 12:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69351">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">⏺
سفارت آمریکا در اردن:
از شهروندان آمریکایی مقیم در خاورمیانه درخواست می‌شود که برای ترک در صورت تشدید اوضاع آماده باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/69351" target="_blank">📅 11:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69349">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b14b8168f8.mp4?token=NG6lN-SmDBF1kEQyApB3wQbPvoCxwC8-d1UiqxSRMU9CBsWO3pUEK2dwINAhCg0cLhEj7eX8YcpHYJ4Nu8uNQ58UxzR5ie8g-eNYh7AfhATwbu4mc_kaQ_3HqE-SXRZsjqTHZCKYa3Uf8OQEsP8HevOErGcMtOlx8LXSLWMac19S1nll7k5S80U3n8Hfq-Vgrn2RLlz_b5lUW3SnNbmfJKfA80wwqwZar3bEtMz_UHnGOPuxtQouUJx2OEJbcrfJIUYlNZ3gvHGe8FEA6XPi6wYCJ8entl7JNyqYL6iaFKYW1VdxPgj3LpUNat3KHlK-34R0mT_qWkd-Du_yy1z7EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b14b8168f8.mp4?token=NG6lN-SmDBF1kEQyApB3wQbPvoCxwC8-d1UiqxSRMU9CBsWO3pUEK2dwINAhCg0cLhEj7eX8YcpHYJ4Nu8uNQ58UxzR5ie8g-eNYh7AfhATwbu4mc_kaQ_3HqE-SXRZsjqTHZCKYa3Uf8OQEsP8HevOErGcMtOlx8LXSLWMac19S1nll7k5S80U3n8Hfq-Vgrn2RLlz_b5lUW3SnNbmfJKfA80wwqwZar3bEtMz_UHnGOPuxtQouUJx2OEJbcrfJIUYlNZ3gvHGe8FEA6XPi6wYCJ8entl7JNyqYL6iaFKYW1VdxPgj3LpUNat3KHlK-34R0mT_qWkd-Du_yy1z7EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
یک انفجار بسیار بزرگ در یک انبار مهمات در شهر خملنیتسکی، واقع در غرب اوکراین، رخ داده است که پس از آن، انفجارهای ثانویه گسترده‌ای نیز به وقوع پیوسته است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/69349" target="_blank">📅 11:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69348">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71213a605e.mp4?token=HvV3YPFF7C6rwQGKWV4ObuAD7ud5WcupWaPsDbqs3SjP2tBNAvDPDRfwhcPjynGQihsBv8KxBFryOwB4vYwZuGPQLNJu0K9pFpmU4wzLvptweJv4vmXLqdJ7-BE0__OPvrsDhdGukdLp0NIraXAcE7uCT-vKTJiC9LyXT0_TLbi1PQ4q26v77CdUfJp_920rJrtJRPRVMQzpCs_vcSFMLsbwPbCWukmDz8rrf95xopbZESbqFodDD74hnPMsN9qE4pVKu0PEbe18-VQeuFVtVV3CeZug74Xb2Yk4DiAbBMjYWO5v8XdbKLuc59tPCrK5Cd9INFiDzOJtNvxpS-q0Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71213a605e.mp4?token=HvV3YPFF7C6rwQGKWV4ObuAD7ud5WcupWaPsDbqs3SjP2tBNAvDPDRfwhcPjynGQihsBv8KxBFryOwB4vYwZuGPQLNJu0K9pFpmU4wzLvptweJv4vmXLqdJ7-BE0__OPvrsDhdGukdLp0NIraXAcE7uCT-vKTJiC9LyXT0_TLbi1PQ4q26v77CdUfJp_920rJrtJRPRVMQzpCs_vcSFMLsbwPbCWukmDz8rrf95xopbZESbqFodDD74hnPMsN9qE4pVKu0PEbe18-VQeuFVtVV3CeZug74Xb2Yk4DiAbBMjYWO5v8XdbKLuc59tPCrK5Cd9INFiDzOJtNvxpS-q0Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مراد ویسی تحلیلگر ارشد اینترنشنال:
آمریکا و اسرائیل برای شدیدترین بمباران در روزهای شنبه و یکشنبه آماده شدن و ترامپ دستور حمله رو صادر کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/69348" target="_blank">📅 11:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69347">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PqjS9yyQR9WE0qztcvrY3fG5xPdGFwIUVGAANHNz65sgGdvRNATLdVAJA5ShnfNgiMFZi5Wi-HT3N5h3fBQDrIFTz3m_TfZGySu3tHqqUN2DNh-_bYZEJG-5z20pj-Cd18YeVplF_um7JgmhBWEautwP4vlR5j5kXvhTGJJNLdn0F8ewMkD7ilpfWaspZPAU7JC9JsHXm4mponQ_q7l8q-SWGLKguymrlTmWSRfYyeZ2SSKkDeuIKZmQpa1BgCbIvQxWcLL7wvfmP_m9yhoFVDPuXNNUhzrd0f-E2VXOzoEhQ2LcAcansFzU7pnQlXjM_JdSvErfus1AvLc2vL8cYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دقایقی قبل یک کشتی در نزدیکی خصب عمان مورد اصابت قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/69347" target="_blank">📅 10:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69344">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/383c08fc2d.mp4?token=g0zP31UQ5gOpszwG4vWI175WMdQlfHxa08PCHGtRpn1sK9nA31W4h4BYZhrTXLaasBwAqjsx2ktdAEichwPDA3TJrdJKsQyzh5Njn_rqIwKRPh9rjHlEYPDSeSbYw-WZNHY1uhDoPQDq_fdCC3DlOgfZMuYVw3sFt2dRj7ozCa74PF-qLqVBCRRd9smcVA-mYDF5UMGkGxS7LTyTQyAfdvz5KvWmog5q6Z2NQQ66hlTAmrojBMARFtmcVQlWdyHXu5aeARz5zBpTX2Zpn3e6KvJJMhyiGTaN65D5QyTrDSpsv-DBwtTTC3j0fAVNNvyX6nIGxB0-NitkzhwGA9YrEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/383c08fc2d.mp4?token=g0zP31UQ5gOpszwG4vWI175WMdQlfHxa08PCHGtRpn1sK9nA31W4h4BYZhrTXLaasBwAqjsx2ktdAEichwPDA3TJrdJKsQyzh5Njn_rqIwKRPh9rjHlEYPDSeSbYw-WZNHY1uhDoPQDq_fdCC3DlOgfZMuYVw3sFt2dRj7ozCa74PF-qLqVBCRRd9smcVA-mYDF5UMGkGxS7LTyTQyAfdvz5KvWmog5q6Z2NQQ66hlTAmrojBMARFtmcVQlWdyHXu5aeARz5zBpTX2Zpn3e6KvJJMhyiGTaN65D5QyTrDSpsv-DBwtTTC3j0fAVNNvyX6nIGxB0-NitkzhwGA9YrEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
بروزرسانی از اسپانیا:
نزدیک ۵۰ هزار نفر از مراکش و الجزایر فرار کردن و غیرقانونی ریختن اسپانیا!
برای کنترل این مهاجرای غیرقانونی پلیس فرستادن که پلیس هم کتک زدن.
این مهاجرا ریختن توی فروشگاه‌ها دارن غارت میکنن، از مردم دزدی میکنن و...
مثلا از یه مراکشی رندوم میپرسن چرا اومدی؟ میگه توی مراکش رفیقمو به قتل رسوندم، مردم هم باهام بد رفتار میکردن، منم فرار کردم اومدم اسپانیا.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/69344" target="_blank">📅 10:34 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69343">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/7cd4da48cd.mp4?token=rIZM4F3uqhhyg0Y5hNunnUBHQNEKDvEoRvaBLpXo8RFy6k5RAEcRvVDaxvawEPcHUqhQQge2afxcJ0dDCM_87mmZ5bGNSaqFb18aPbMq13_TiyrHMtbSSPcDvoOJ8V_euAKhQL3ocNMel6QM8zHt6-pRH4ol6hhEqrghzL6AWtnUAALo8vzbQ7kejgFiH9jeC4tkzq9vNta91A2UVownMOZxVMSbkCzbx8WPrDnzvkF9tf8qWYslgm0gKgOID5Af10AKvVTLX19m3Jd5HWgwZRJJGZdgk4CHq1PfenVUCgapx458MHXRbfyDkLL7pOvq4dFN2OY1Yb4TIpIJuNLrBjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/7cd4da48cd.mp4?token=rIZM4F3uqhhyg0Y5hNunnUBHQNEKDvEoRvaBLpXo8RFy6k5RAEcRvVDaxvawEPcHUqhQQge2afxcJ0dDCM_87mmZ5bGNSaqFb18aPbMq13_TiyrHMtbSSPcDvoOJ8V_euAKhQL3ocNMel6QM8zHt6-pRH4ol6hhEqrghzL6AWtnUAALo8vzbQ7kejgFiH9jeC4tkzq9vNta91A2UVownMOZxVMSbkCzbx8WPrDnzvkF9tf8qWYslgm0gKgOID5Af10AKvVTLX19m3Jd5HWgwZRJJGZdgk4CHq1PfenVUCgapx458MHXRbfyDkLL7pOvq4dFN2OY1Yb4TIpIJuNLrBjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
صحبت‌های عادل فردوسی‌پور درباره ماجرای دست‌بوسی عباس صالحی :
تو عُمرم دستِ مسئولی رو نبوسیدم!
عباس صالحی وارد مسجد شد و کاملاً اتفاقی روی صندلی کنار من نشست. به شوخی بهش گفتم اگه یه روزی فیلتر 360 برداشته بشه، همه این نشستن شما کنار من رو ربط میدن به رفع فیلتر!
همون موقع که داشتیم دست می‌دادیم و روی صندلی جا‌به‌جا می‌شدیم، شب دیدم یه ویدیو وایرال شده و با یه تیتر زشت نوشتن که من دست عباس صالحی رو بوسیدم.
اگه قرار بود دست‌بوس باشم که الان برنامه 90 رو داشتم و 360 رو هم فیلتر نمی‌کردن.
چطور ممکنه من برم تو اون مسجد، بین اون همه آدم، بیام دست عباس صالحی رو ببوسم و برای خودم حاشیه درست کنم؟
من همین چند روز پیش هم گفتم؛ بله‌قربان‌گو نبودم، نیستم و نخواهم بود!
همیشه روی اصول خودم ایستادم و سعی کردم کنار مردم باشم. واقعاً این حجم از هجمه‌ای که به من وارد میشه حیرت‌آوره.
من عاشق کارمم و اینو خودشون هم می‌دونن، ولی نه به هر قیمتی. اگه شرایطش فراهم باشه، تو فوتبال 360 به کارم ادامه میدم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/69343" target="_blank">📅 10:04 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69342">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75d1e6179c.mp4?token=HGvuXuXclK7XGX2a2Y6f3VzzXdurC3ap0yFIxmYeKUgphfJm9v50NPCGAEVbuSbwQGV1ghKymfXHXgvbnTbPLyEcKGf4w4EHcOioHew604Mthvc_m3SIScWWpiM4460dJKrQFGgcRthSuRo0ofZgz9-BixGPXd9T7wIIxLCsytGu3QGsDpapWKYgXBUXw6-DNuDP-eySANJMx4Fl8Hz5uMhN-avbRbqHrTdVRZsajShH2EOk2Oq0Pc3tVr-9Ql_pU5H_Vq5Rm7zBfa6o2op5VdcvLQlj5l45LtZrY0q08kP3idlDt0OlbN3C1fRBVW5Tl1Hmp5lmYy3D5so3u9lX9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75d1e6179c.mp4?token=HGvuXuXclK7XGX2a2Y6f3VzzXdurC3ap0yFIxmYeKUgphfJm9v50NPCGAEVbuSbwQGV1ghKymfXHXgvbnTbPLyEcKGf4w4EHcOioHew604Mthvc_m3SIScWWpiM4460dJKrQFGgcRthSuRo0ofZgz9-BixGPXd9T7wIIxLCsytGu3QGsDpapWKYgXBUXw6-DNuDP-eySANJMx4Fl8Hz5uMhN-avbRbqHrTdVRZsajShH2EOk2Oq0Pc3tVr-9Ql_pU5H_Vq5Rm7zBfa6o2op5VdcvLQlj5l45LtZrY0q08kP3idlDt0OlbN3C1fRBVW5Tl1Hmp5lmYy3D5so3u9lX9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سیدمحمود نبویان، نماینده مردم تهران، درباره شاهنشاه آریامهر؛
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/69342" target="_blank">📅 09:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69341">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">چقدر روی فوتبال باختی تا حالا؟ وقتش نیست سبک بازی تو عوض کنی؟
💸
دیگه دوران شرط‌بندی روی حس و حال و شانس تموم شده. اگر دنبال تحلیل‌های دقیق بر اساس آمار، فرم تیم‌ها و نرخ مصدومیت‌ها هستی، باید جایی باشی که تخصصش همینه.
🔹
تحلیل اختصاصی بازی‌های روز (جام جهانی،…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69341" target="_blank">📅 02:38 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69340">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=ubIFrIVmfrTWHnuCtbRzu9qoW7Z-60em047zEXd40AcIRseJ5178qUKDUbLuEsoQu4v4e1C1EGV0rV9aXC2UNR64NuWSAGkWJun1LEXmDPE5JDqSQrZD2yY0Qx7Zqfh5ktVWg2TV0pJJbZVUe5ujp6XAcfy-jQPw3XjSwvEHway5b0XoA12PgJLTnQNL1LlzKNkyffKgatA12xmYiAjsk8e-QHrYmeMJOZtJoNYcTz20rRvxdXr37MQidt3rO8TTw3tbW2sAodSCUnfOmGNPgBjrK8mY0iGB55CRTqYBp2rRparGohcKAI7pQEf2Tme6XaFOcN231ukuodXk5v_bKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=ubIFrIVmfrTWHnuCtbRzu9qoW7Z-60em047zEXd40AcIRseJ5178qUKDUbLuEsoQu4v4e1C1EGV0rV9aXC2UNR64NuWSAGkWJun1LEXmDPE5JDqSQrZD2yY0Qx7Zqfh5ktVWg2TV0pJJbZVUe5ujp6XAcfy-jQPw3XjSwvEHway5b0XoA12PgJLTnQNL1LlzKNkyffKgatA12xmYiAjsk8e-QHrYmeMJOZtJoNYcTz20rRvxdXr37MQidt3rO8TTw3tbW2sAodSCUnfOmGNPgBjrK8mY0iGB55CRTqYBp2rRparGohcKAI7pQEf2Tme6XaFOcN231ukuodXk5v_bKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چقدر روی فوتبال باختی تا حالا؟ وقتش نیست سبک بازی تو عوض کنی؟
💸
دیگه دوران شرط‌بندی روی حس و حال و شانس تموم شده. اگر دنبال تحلیل‌های دقیق بر اساس آمار، فرم تیم‌ها و نرخ مصدومیت‌ها هستی، باید جایی باشی که تخصصش همینه.
🔹
تحلیل اختصاصی بازی‌های روز (جام جهانی، باشگاهی و دوستانه)
🔹
پیشنهادهای دقیق گل بالا/پایین (Over/Under) و گلزنی هر دو تیم (BTTS)
🔹
بدون ادعای واهی ضریب ۱۰۰! فقط سود مستمر با مدیریت سرمایه.
آمار ما در ماه گذشته خودش گویای همه‌چیزه. فرم‌های امروز رو از دست نده
👇
🔗
[
ورود به کانال و دریافت فرم‌های رایگان امروز]</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/69340" target="_blank">📅 02:38 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69339">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
🚨
خبرگزاری فارس لیست اهداف انرژی منطقه رو منتشر کرد:مهم‌ترین تأسیسات انرژی جهان در تیررس موشک‌های ایرانی؛
❌
میدان نفتی غوار در عربستان
غوار ستون فقرات تولید عربستان است و هر گونه اختلال در آن، بیش از ۵ درصد از کل عرضۀ نفت جهان را به خطر می‌اندازد.
❌
تأسیسات ابقیق و خریص عربستان
قلب ماشین صادراتی عربستان که نفت خام میادین غوار، خریص و شیبه را تثبیت و برای صادرات آماده می‌کند.
ابقیق نیز تنها نقطه‌ای است که بیش از ۷ میلیون بشکه در روز از آن عبور می‌کند و هرگونه آسیب به آن، علاوه بر ایجاد بحران در صادرات نفت عربستان، زنجیرۀ تامین پتروشیمی‌ها و نیروگاه‌های داخلی و حتی آب‌شیرین‌کن‌ها را مختل می‌کند.
❌
پالایشگاه الرویس و میدان نفتی زاکوم در امارت
زاکوم دومین میدان بزرگ فراساحلی جهان و صاحب صادرات روزانه بیش از ۱ میلیون بشکه نفت خام است.
❌
میدان گازی گنبد شمالی و تأسیسات ال‌ان‌جی راس‌لفان قطر
بزرگ‌ترین میدان گازی جهان با ۲۵ درصد ذخایر اثبات‌شدۀ جهان؛ راس لفان تک‌مهم‌ترین پایانۀ صادراتی ال‌ان‌جی جهان و مسئول حدود ۲۰٪ از کل تجارت جهانی ال‌ان‌جی است.
❌
میدان نفتی برقان کویت
بزرگ‌ترین میدان نفتی کویت با ذخیرۀ حدود ۶۷ میلیارد بشکه؛ برقان یکی از میادین کلیدی است که در بحران اخیر، ۲ میلیون بشکه در روز از تولید کویت را از مدار خارج کرد.
❌
پالایشگاه ستره و تأسیسات المعامیر بحرین
بحرین به دلیل وابستگی شدید به این تاسیسات، آسیب‌پذیرترین کشورهای شورای همکاری خلیج‌فارس در برابر اختلالات انرژی محسوب می‌شود
❌
میدان‌های گازی لویاتان و تامار اسرائیل
ویاتان بزرگ‌ترین میدان گازی اسرائیل و تامار دومین میدان بزرگ آن رژیم است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69339" target="_blank">📅 02:11 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69338">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qdEUP66sOOgO_4Ls-NuHh_b0kpjNXegmhBgEICCxN6tashZKdjf3gCQ_yJL0F05MHman_kVXZYSGFywxZ_Gap4Md-17rEdBl1SB3dLoRE2o_f5xLx5-O_JUA6H4MUILYtdgqoSjtpoU-dFg1J-vGFOz7m1NLha0P_xvnSwcj1e6B00QkX_xUSASMG6vHe_GWU53e5_LFjEdfY6UUcOz-ZKQIYXP_QHC7fvXfpk1g1fS4Gb4ArTTZ9CHav5mMHW4RAfSDMws-Pi0inXg4sk24L48BKPCvdnN2Ddsgw2ikeX1jKwDoT8Gcir0TDBaQm6kp552dg9NXkLaujIMjfIwqvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
تسنیم:یه مقام ارشد امنیتی به ما‌گفته؛اگه آمریکا یا اسرائیل بخوان به زیرساخت‌های ایران حمله کنن؛
ایران از قبل یه برنامه گسترده برای جواب دادن آماده کرده.
به گفته این مقام، توی این برنامه، زیرساخت‌های حیاتی اسرائیل و تأسیسات انرژی آمریکا تو منطقه هم جزو اهداف در نظر گرفته شدن.
نیروهای مسلح ایران توی جنگ 40 روزه و اتفاقات هفته‌های اخیر نشون دادن هم توان انجام چنین عملیاتی رو دارن و هم برای انجامش اراده لازم رو.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/69338" target="_blank">📅 02:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69337">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/onJa64OPRxsktUbbnzAIzDIhzZw5A8cX5-c9asFs-3LM1EHBk8OhxQbHB1gtMqzpebuL1M1wLfpsi7YEKpfeZXZ_1g7U72kv-lQVliLtF1MUB2rwrd-nxr9MRS5J5BoqOS1xGDvxQH4PzV1NQSParyfiDi6SMp6ok8ehLtOyaqKi4si5MI2Mm6U7a4f6Qi9ejaMtC74DezHmkmd9hFLsmsLCS1YQv7Zybnn7KSsgwk_1E5AoJa0y_A1y7GJE8-6GM65xDYw9t5C6wejCK2sFxujgEJOMeaRPTEES7vHJDJAFEKyXejs8giZ3Zo-GhMkGayqpaEwks7JOAgnmZXN28g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری
؛آکسیوس:ترامپ در حال بررسی حمله به تأسیسات انرژی ایران ظرف چند روز آینده است.
یک مقام آمریکایی روز جمعه به «اکسیوس» گفت که رئیس‌جمهور ترامپ به‌طور جدی در حال بررسی انجام حملاتی علیه تأسیسات انرژی ایران در چند روز آینده است، اما هنوز دستور نهایی برای اجرای آن را صادر نکرده است.
این حملات همچنین ممکن است برای نخستین بار پس از چندین هفته، ارتش اسرائیل را نیز درگیر کند و چنین تشدید تنشی احتمالاً به حملات موشکی ایران علیه اسرائیل منجر خواهد شد.
سی‌بی‌اس نیوز و وال‌استریت ژورنال نخستین بار درباره حملات احتمالی گزارش دادند.
ترامپ در آغاز جلسه روز جمعه کابینه، با اشاره به حمله احتمالی گفت: «خب، ما ضربات بسیار سختی به آن‌ها وارد خواهیم کرد و می‌دانید، بالاخره زمانی فرا می‌رسد که آن‌ها خواهند گفت دیگر تاب و تحملش را نداریم.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69337" target="_blank">📅 01:49 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69336">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uqvMNNu63r7CrLwcSr_tTQ-gZA0UJmY_8r9eZQ3NVwm63t9AG3uOW8JFVgg5U_llGP3wxALnFWfgUe5-ij62590w-GJlBOYCaygsBLFRwTKmDOA1MJ7qYSuZGhHB0iwAMqdUV-OUFW4OKU2Z4mmiXr_uc1iSdVzMD7xkbl14S2hg4Cios8IgPrqR2VN1CHvR0LsIN2RqVK_TIYfydAOsAThf-9gV8eBDIW5X8pQE19T8lL-7amIVPziGfVJ_OauYid9KTQ6xtAZv4m13H70AlCkgRHUFx38GrjMeWRIbgvWUoxg7PjFPiqXPPANzNxy7WX-Iim-WjaQCG_UZctFzVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
🇮🇱
سی‌بی‌اس نیوز:
ایالات متحده و اسرائیل در حال آماده‌سازی یک کمپین بمباران مشترک بزرگ علیه زیرساخت‌های انرژی ایران، از جمله نیروگاه‌ها و پالایشگاه‌ها هستند.
ترامپ هنوز تأیید نهایی را نداده است، اما حملات ممکن است این آخر هفته آغاز شود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/69336" target="_blank">📅 01:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69335">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5040574e14.mp4?token=UE58ei9mh2UUVgaPM8X39bOHEAvZUvWnh36qnwOuHnJn1Sc6-1W4K7a79s0WH7Hd61zmGYr6TviCw3RjtML8PjfcoT9OrzGQWuALk8DdnudoYrc96oZKne3ghzklFqRSH0xerLwOGa2qoQtJazkzCA3MzVJ5IsqiLihlKrTxBtfaPJbQ6O29s5wUmYSs40GrhcXJZidDfjviT83kpYACQHdZRsyLyT_31c6YL1sIB5TooEQkrBY3Aey3chJ_MJiWuwZbQdSmjkxJ71Qekb9fbNsgij4qFLVWIV0fbVP3yasSs63PFaYFqk8sTKGhqXX6yqUgW8y3iQjuPrIkT7M_JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5040574e14.mp4?token=UE58ei9mh2UUVgaPM8X39bOHEAvZUvWnh36qnwOuHnJn1Sc6-1W4K7a79s0WH7Hd61zmGYr6TviCw3RjtML8PjfcoT9OrzGQWuALk8DdnudoYrc96oZKne3ghzklFqRSH0xerLwOGa2qoQtJazkzCA3MzVJ5IsqiLihlKrTxBtfaPJbQ6O29s5wUmYSs40GrhcXJZidDfjviT83kpYACQHdZRsyLyT_31c6YL1sIB5TooEQkrBY3Aey3chJ_MJiWuwZbQdSmjkxJ71Qekb9fbNsgij4qFLVWIV0fbVP3yasSs63PFaYFqk8sTKGhqXX6yqUgW8y3iQjuPrIkT7M_JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یک مهاجر مراکشی درحال رفتن به منطقه برون‌بومی اسپانیایی «سئوتا»
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/69335" target="_blank">📅 01:36 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69334">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری؛وال استریت ژورنال:ترامپ دستور حمله جدیدی به ایران را صادر کرد.   مقامات آمریکایی اعلام کردند که رئیس‌جمهور ترامپ دستور حمله جدیدی را به ایران صادر کرده است که هدف آن وادار کردن تهران به تسلیم است؛ این حمله ممکن است از همین آخر هفته آغاز شود و چند…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/69334" target="_blank">📅 01:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69333">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Asqdce7xv1hLUKAhNUNApCnXQ7Ya72SOmb6n62_QkeOsSnOCilTski1Zj9Fzk8334kqIceSERxEXbCxoAeEOV3JOdvy_71_JX0EwwsjoSxoWPnFlJBSVO5MuFKbRlZjBjkKI6kdOfjpkblWT3uTNTypTSKiGf19FuXRXVhKYG6Lxrm6uB2U8xz889Y3fN85_q6CcuhfR6IlD-W7qkN8_iCdqR2trromPncCi9TRTUEfUwaFg5tpFtYCC6uLLH4mx2lz4K50MkqchwhXoNEO1pkKNVKz6piVZ5eR5KgTmmcnthF7rsoGrtYaNO9UZXgy06yYQlrFIp6DQWxHkBU6oqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری
؛وال استریت ژورنال:ترامپ دستور حمله جدیدی به ایران را صادر کرد.
مقامات آمریکایی اعلام کردند که رئیس‌جمهور ترامپ دستور حمله جدیدی را به ایران صادر کرده است که هدف آن وادار کردن تهران به تسلیم است؛ این حمله ممکن است از همین آخر هفته آغاز شود و چند روز به طول انجامد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69333" target="_blank">📅 01:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69332">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">چندین منبع به CBS News گفته‌اند که حملات ممکن است در طول آخر هفته انجام شود</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/69332" target="_blank">📅 01:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69331">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3b500b5c2.mp4?token=gGS_W-fxnAmasusGuCeOc6ZyicLO_afeAcH_W2uZJlP5pCeUQ2YECjAmVBAlrYs9WwbwDgPIlOp435_lcZXv60iGmeuKltvXxLDkrm-A5ZcCFtjnLL3yePmpjxPOkkMarAn8jnchlhuCTvxx35q9Nkx_7roSqer0zy9Ls44B3Ul207yemylNx6rpur6Q8ecUj-mFQAk1NOcXZaK6kWB5kSxSTmI6MUEor_p2D4woxHdBoaEtHu0YHC4dewPEmvMK66zH6hZk9G9uxM1rKTweuH1TTnbO9j3886TUP05muweCYoYIDvU6-7h0nTNLWf7s_qU2WjZuwfdj3jcnAIh-h2w-p8HBuQhjFkJOcuRF4VhNpIfLEJi4eCBi0CdJinI_QatxnkfIuP1ktMT_wxAoWV43ZAukBifO2QFe8T5Xbiz_r6y0MHLJs_CQv_ZxbW_j-9zttvdQl3ZCxoNQRxnP6Ew0HUlsS8q8_TLle8xYKvcRw5OigOj7XcvdYeBHJZfqVO3Uh4NlSLgq0GFchmjGGaBjQn0gPq5_O7YM1Y5GkhwwafefOb9lPRQJnOTKXX-kBd5978Kia6Vq2wXZp5bElNPQjY0wYfT0peeZM4ns53IXv6ZHgOErCFd1C-OAiXmEtA6Q0IsqYTNAO-KpRvsoJQuWePbSHnLZh95r8qaN6R0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3b500b5c2.mp4?token=gGS_W-fxnAmasusGuCeOc6ZyicLO_afeAcH_W2uZJlP5pCeUQ2YECjAmVBAlrYs9WwbwDgPIlOp435_lcZXv60iGmeuKltvXxLDkrm-A5ZcCFtjnLL3yePmpjxPOkkMarAn8jnchlhuCTvxx35q9Nkx_7roSqer0zy9Ls44B3Ul207yemylNx6rpur6Q8ecUj-mFQAk1NOcXZaK6kWB5kSxSTmI6MUEor_p2D4woxHdBoaEtHu0YHC4dewPEmvMK66zH6hZk9G9uxM1rKTweuH1TTnbO9j3886TUP05muweCYoYIDvU6-7h0nTNLWf7s_qU2WjZuwfdj3jcnAIh-h2w-p8HBuQhjFkJOcuRF4VhNpIfLEJi4eCBi0CdJinI_QatxnkfIuP1ktMT_wxAoWV43ZAukBifO2QFe8T5Xbiz_r6y0MHLJs_CQv_ZxbW_j-9zttvdQl3ZCxoNQRxnP6Ew0HUlsS8q8_TLle8xYKvcRw5OigOj7XcvdYeBHJZfqVO3Uh4NlSLgq0GFchmjGGaBjQn0gPq5_O7YM1Y5GkhwwafefOb9lPRQJnOTKXX-kBd5978Kia6Vq2wXZp5bElNPQjY0wYfT0peeZM4ns53IXv6ZHgOErCFd1C-OAiXmEtA6Q0IsqYTNAO-KpRvsoJQuWePbSHnLZh95r8qaN6R0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
«قیمت‌ها حسابی اومده پایین، به‌جز نفت.
دو هفته پیش، وقتی همه فکر کردن توافق نزدیکه، قیمت‌ها مثل سنگ سقوط کرد.
ولی ما یه
توافق واقعی
می‌خوایم، نه یه توافق الکی.»
🎙
استیو گروبر:
درباره ایران، فکر می‌کنید چقدر طول بکشه تا این ماجرا تموم بشه؟ یه ماه؟ یه سال؟
🇺🇸
ترامپ:
«پیش‌بینی کردنش همیشه سخته.
ما ماجرای ونزوئلا رو توی کمتر از یه روز جمع کردیم.
اگه می‌خواید همه‌چیز خیلی سریع تموم بشه، کافیه به یه عده سلاح هسته‌ای بدید!
اون‌وقت همه‌چیز خیلی سریع تموم می‌شه.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69331" target="_blank">📅 00:31 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69330">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7487679e0.mp4?token=LZJB-fOIuzij9_ReRGb5ih5GqkLCthu-wlXttGQBLiIimQ2fZpi98gdCh0kYnHfeLigjZUZvbfJ6b7Lcij_MQWr2BlIyETEpN4Iqo-UbhZEtuYZTc6Y8g0l8OHEpVHrrZj1EdfzysIW7v8domvQe2QNHUjZ596rYrqV-9fIGu3kKgeGSggRKJweBt6iDyRg-5HJmd6I-bRCOsExKPJBDFrMACDIyddcdl29aki-fcEFtNVitX0IDUYJ-wpGaUf11bKByyO0XaKvywIxtkaXMl6dEFNrvK9YoZWgFvhB3HGgq4BlFOgYDmTeIifSAfxKrVRap_rVzr35y22IJN-wztg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7487679e0.mp4?token=LZJB-fOIuzij9_ReRGb5ih5GqkLCthu-wlXttGQBLiIimQ2fZpi98gdCh0kYnHfeLigjZUZvbfJ6b7Lcij_MQWr2BlIyETEpN4Iqo-UbhZEtuYZTc6Y8g0l8OHEpVHrrZj1EdfzysIW7v8domvQe2QNHUjZ596rYrqV-9fIGu3kKgeGSggRKJweBt6iDyRg-5HJmd6I-bRCOsExKPJBDFrMACDIyddcdl29aki-fcEFtNVitX0IDUYJ-wpGaUf11bKByyO0XaKvywIxtkaXMl6dEFNrvK9YoZWgFvhB3HGgq4BlFOgYDmTeIifSAfxKrVRap_rVzr35y22IJN-wztg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
توی درگیری با ایران، بسته به اینکه چه آماری رو حساب کنید،
16 تا 18 نفر
از نیروهامون رو از دست دادیم؛ که همین هم خیلی زیاده، چون حتی از دست دادن
یه نفر هم زیاده.
جنگ ویتنام
21 سال
طول کشید. ما تازه وارد
ماه پنجم
شدیم، ولی همون‌ها که آمریکا رو 21 سال توی ویتنام نگه داشتن، حالا می‌گن "چرا ماجرای ایران این‌قدر طول کشیده؟"
من الان دارم کاری خیلی بزرگ‌تر از چیزی که اول گفته بودم انجام می‌دم. قرار بود فقط وارد بشیم، توان نظامی ایران رو نابود کنیم و برگردیم.
ولی بعد دیدم اگه فقط این کار رو بکنیم و بریم، دوباره خودشون رو بازسازی می‌کنن. برای همین باید یه جور
کنترل و نظارت
هم وجود داشته باشه، وگرنه دوباره همه‌چیز رو از نو می‌سازن.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/69330" target="_blank">📅 00:16 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69329">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdc86e1f9d.mp4?token=llNC-Lu-DYyqTvKMfTkPrpiOeBt3H3gzvwcgBjRbnMlGRpSiBnrKsiB_jKIhi0a0--qHqgm-HN4HVAdLita63_uu7n-rjnarlBCVCVeWsBLHF-7o0l7EHlH1AMRnlWEp_R9LXxPt0TsvtrSlmDR91zbVv2ftao_rSuLXrkyNju8993shVft9DAz6vwx378OayX8ZldW-g_QhMQoAfe0KREqbvFKonAPRx2sIy0wm3pHEkJhCBT0M04Tv188954RWglFk2aLw2clmZynepw-il7PDpHhRqfO71YuhkNvmmuv6vzxB0N797S92vTQCChlXalBY1hRB48CUKiL0oFbEsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdc86e1f9d.mp4?token=llNC-Lu-DYyqTvKMfTkPrpiOeBt3H3gzvwcgBjRbnMlGRpSiBnrKsiB_jKIhi0a0--qHqgm-HN4HVAdLita63_uu7n-rjnarlBCVCVeWsBLHF-7o0l7EHlH1AMRnlWEp_R9LXxPt0TsvtrSlmDR91zbVv2ftao_rSuLXrkyNju8993shVft9DAz6vwx378OayX8ZldW-g_QhMQoAfe0KREqbvFKonAPRx2sIy0wm3pHEkJhCBT0M04Tv188954RWglFk2aLw2clmZynepw-il7PDpHhRqfO71YuhkNvmmuv6vzxB0N797S92vTQCChlXalBY1hRB48CUKiL0oFbEsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو وایرال شده از یه هموطن که تو خونش کره خر نگهداری میکنه و بردتش رو تردمیل تا دلتنگی بیرونو نکنه
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/69329" target="_blank">📅 23:55 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69328">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hr7WYAIbiBXgjariZmK1Gh4hKgiJSN7DMNwkDmL5HoJl9ktAlRsQURkkvAM52NXHl_tMMvVh-liyUTbgWPJSSVIbJZ_SFDInOFcdWBSIr7B94Qc0m-pNwrC18RrMA8z-5XJyeGEnHLpwTqwoT6cau4nMuZlnAb4Ie4DdVnyB45Ax6MI4lqWH6R9NJGIBJZTtHonY30KTqn_AFXSfMPBh0V-afIIUW7ZsBXAQcHsWtptSVtxbuRxlhnWGWzRauf3ewVjtAZTsjtwCFbFVBKWrft7MSXKkbis1iQDbBsr_wOkWTp96AHuC5qGs6Xovixaylj14PJM0AYaBUNoP17wN3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سنتکام برای بار هزارم:
تنگه هرمز بازه و ادعای سپاه مبنی بر بسته بودن تنگه هرمز دروغه.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/69328" target="_blank">📅 23:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69327">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdfe35db6c.mp4?token=bmMg0rnIySyfE3B4O35GPKETgrALWjmfPUbtVxoSj9GtUE9eYgR0bStufaVcKqhDJ-h7fMJTuzWAmnJZHvWTtdQMscIm_9ULy8-eTl7aKcp5Qoc_EX57dlAz-2AHgn2kHj6zW8gxCVNmURAxSxfd5g5vNbH2dFkjPuOpQ_-G9l-7H8NizSI-tsGIsrN_77XrEe1GTtuPoXD1F_UIM_esc1zNmaJaHqG7VUeQ2aM4E-3_bB74GORtiJoIG7Pv3qdkA8iUpW-legcPctHt4-7xZhYSqhfS-lAHqGJNdbyJoCEBsz1wve9dZBIh9ub2YJrBX4pV2sBRX8JFJd-DKYAMVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdfe35db6c.mp4?token=bmMg0rnIySyfE3B4O35GPKETgrALWjmfPUbtVxoSj9GtUE9eYgR0bStufaVcKqhDJ-h7fMJTuzWAmnJZHvWTtdQMscIm_9ULy8-eTl7aKcp5Qoc_EX57dlAz-2AHgn2kHj6zW8gxCVNmURAxSxfd5g5vNbH2dFkjPuOpQ_-G9l-7H8NizSI-tsGIsrN_77XrEe1GTtuPoXD1F_UIM_esc1zNmaJaHqG7VUeQ2aM4E-3_bB74GORtiJoIG7Pv3qdkA8iUpW-legcPctHt4-7xZhYSqhfS-lAHqGJNdbyJoCEBsz1wve9dZBIh9ub2YJrBX4pV2sBRX8JFJd-DKYAMVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ:
«این‌ها خیلی وقت‌ها زیر قولشون می‌زنن.
توافق می‌کنن، بعد می‌گن باید
7 ساعت
درباره برنامه هسته‌ای مذاکره کنیم.
من می‌گم: "آخه چرا 7 ساعت؟ مگه نمی‌شه تو
10 دقیقه
جمعش کرد؟"
شما
5 دقیقه
وقت دارید که تکلیفتون رو روشن کنید.
آخرش هم فقط کله منو کیری می‌کنن!»
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69327" target="_blank">📅 22:43 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69326">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/379fea6ae8.mp4?token=n1fcVA0yxGsDX9juKDKtJIGLqQTh14WQSbZn73XB9iMnO_jYuHezleaDsvYplP64f5W6o2zPY7jEhtzAYBRup8GG4wdNQyZCDA3oOUegTkgQ_bG25DI95fs7ZkcGAooLJWZqIuWfbRPfnd-QHlrN-_9VgCE4ZY2o_bRre671JnuEtYaic9dUPd688mcH7Osyx-xmriqrtYqZ3R0lKYHqtrlqtgLIFzjLDB7L2XyFg6rjGfpVol5tSLGroSG_mra0stcRk67SviS6sJy7ZZmBWk9W9QMJoIs7P-4m3upZN_RtJMAufUaQdFs6OfXfJ2U9bAJSdBUEV-ok4SPwLMw3rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/379fea6ae8.mp4?token=n1fcVA0yxGsDX9juKDKtJIGLqQTh14WQSbZn73XB9iMnO_jYuHezleaDsvYplP64f5W6o2zPY7jEhtzAYBRup8GG4wdNQyZCDA3oOUegTkgQ_bG25DI95fs7ZkcGAooLJWZqIuWfbRPfnd-QHlrN-_9VgCE4ZY2o_bRre671JnuEtYaic9dUPd688mcH7Osyx-xmriqrtYqZ3R0lKYHqtrlqtgLIFzjLDB7L2XyFg6rjGfpVol5tSLGroSG_mra0stcRk67SviS6sJy7ZZmBWk9W9QMJoIs7P-4m3upZN_RtJMAufUaQdFs6OfXfJ2U9bAJSdBUEV-ok4SPwLMw3rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎤
خبرنگار:
سنتکام گفته حملات اخیر برای کم کردن توان ایران در مختل کردن تردد کشتی‌ها در تنگه هرمز بوده. به نظرتون چند حمله دیگه لازمه تا به این هدف برسید؟
🇺🇸
ترامپ:
«هیچ‌وقت نمی‌شه دقیق گفت.
بیشتر کشورها تا الان تسلیم شده بودن.
ایران هنوز تسلیم نشده و بابت همین باید بهشون اعتبار داد.
اونا همیشه به سرسخت بودن معروف بودن؛ واقعاً هم سرسختن.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/69326" target="_blank">📅 22:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69325">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d8357e0fa.mp4?token=RWcfWtdNQ1NDUmBnUhGoGR3ae_JKdVRasDGrfToJ0S5pgOTrrGxHfWF1v4VsWNtz4y_kzI3pzDIK6bnwJghqM9cTYsMAmhTwkQXAEbzJOCTjTeg8lIzEGBjrCzlY2-L_yhLGSWd04C8B9P_ypwZjEIbIxOtJNdqo4ruXm_mCco1IqXH4xQuSd_uzDObDCJ9OKe_Sipt0Ux5LznFDES4rMRwcCD4VhbDlxx3qAsmCyp2hJaU9Zo4jNELAH31eiQfiliB5A-oZnWz2bv5wdbdfCkJ5qLiAOEuhVJw2jDJMrbvJOaE6chxy4xJU6xi7GilP6mKVeYiy2g53F1fRcvEVUSMdDn9YHQoGrENoAukKEIwv4FWnu--qpodNV2g_BFmHcne2-tzMzY_XZGt-ajr-J525mMwrqaNVMG7-1qeOjlGAbCqJzewS6lRqpx4p3KxYBGkSuMnLbK7HnOuNS2P5jLMfPcLiiEGIRUIpgOmh_nKqhS7TmjKn6lU3dUQHE1pCWbOeXld6dCt8t96zkfu4JL1trXMK1NoXiO3xfHJT5vRzJuW-FMldjUHsw1lTmfocZTQjGeWtxAfRTZ7eUpj5QxTa4-CrSMks-lqTMeE-2EO-HoVYRm6y-gvC4rqgZ2y3jYqEkedsOdlNrOh3lI3P42eDD2oa4QSnB7KxzJjUOH0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d8357e0fa.mp4?token=RWcfWtdNQ1NDUmBnUhGoGR3ae_JKdVRasDGrfToJ0S5pgOTrrGxHfWF1v4VsWNtz4y_kzI3pzDIK6bnwJghqM9cTYsMAmhTwkQXAEbzJOCTjTeg8lIzEGBjrCzlY2-L_yhLGSWd04C8B9P_ypwZjEIbIxOtJNdqo4ruXm_mCco1IqXH4xQuSd_uzDObDCJ9OKe_Sipt0Ux5LznFDES4rMRwcCD4VhbDlxx3qAsmCyp2hJaU9Zo4jNELAH31eiQfiliB5A-oZnWz2bv5wdbdfCkJ5qLiAOEuhVJw2jDJMrbvJOaE6chxy4xJU6xi7GilP6mKVeYiy2g53F1fRcvEVUSMdDn9YHQoGrENoAukKEIwv4FWnu--qpodNV2g_BFmHcne2-tzMzY_XZGt-ajr-J525mMwrqaNVMG7-1qeOjlGAbCqJzewS6lRqpx4p3KxYBGkSuMnLbK7HnOuNS2P5jLMfPcLiiEGIRUIpgOmh_nKqhS7TmjKn6lU3dUQHE1pCWbOeXld6dCt8t96zkfu4JL1trXMK1NoXiO3xfHJT5vRzJuW-FMldjUHsw1lTmfocZTQjGeWtxAfRTZ7eUpj5QxTa4-CrSMks-lqTMeE-2EO-HoVYRm6y-gvC4rqgZ2y3jYqEkedsOdlNrOh3lI3P42eDD2oa4QSnB7KxzJjUOH0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗣️
حسین جنتی، شاعر : سقوطِ زندگیم جایی اتفاق افتاد که سال 89 جلوی علی خامنه‌ای شعر خوندم؛
من سال 89 دعوت شدم به شعرخوانی تو بیت رهبری و شب قبلش بهم گفتن 5 تا از شعراتو باید بدی ما نگاه کنیم، درنهایت یکیشو اجازه میدیم بخونی.
ولی من شعری که اجازه نداشتم رو اونجا خوندم:
گشته‌ام میدان به میدان شهر را، هرگوشه دردی هست
ارتفاع درد از پیچ شمیران میرود بالا
درد من هرچند درد خانه و پوشاک ارزان نیست
با بهای سکه در بازار تهران میرود بالا
گفتم که خواجه در رویای خود از پای‌بست خانه میگوید
ناگهان صدها ترک از نقش ایوان میرود بالا
گفتم جوجه‌های اعتقادم را کجا پنهان کنم
وقتی شک شبیه گربه از دیوار ایمان میرود بالا
فردا صبحش اومدن سراغم و گفتن تو غلط میکنی با ولی‌امر مسلمین شوخی کردی و سقوط آزاد زندگی من همونجا اتفاق افتاد و اصلا هم پشیمون نیستم از کاری که کردم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/69325" target="_blank">📅 22:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69324">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d259260d40.mp4?token=UjaFkHjPSqurbywaIrC3xAMBRtG1tkXh-FV0PoJlF_yCtapX_6m4Y4XTQEUu2wiKvW3nLUuAWzuTr60-NmmSMLosSzxMiB3oFDxvQHqu8P8wVGLGmDiYL9EVM0x_8R2tC7KyOJUejJFOHTWEB5cKkqN6m_5F_l0UDxabd_Op6xInqACrCzDKPoMAkf5XgnCGZjnoSUzhbuO7T4IGwVas_UfoZph6l_-Cgp6EDXbma3o6YaTSYDQq8RSA0n9BQEjGSF9eXuhf47lMPG3qepUkPQAIhNiHDzHD3a_qepT0TYEdCt0f5X9DmYrx2_j_t9le2psqsnMwL2aIUDDml-6cFjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d259260d40.mp4?token=UjaFkHjPSqurbywaIrC3xAMBRtG1tkXh-FV0PoJlF_yCtapX_6m4Y4XTQEUu2wiKvW3nLUuAWzuTr60-NmmSMLosSzxMiB3oFDxvQHqu8P8wVGLGmDiYL9EVM0x_8R2tC7KyOJUejJFOHTWEB5cKkqN6m_5F_l0UDxabd_Op6xInqACrCzDKPoMAkf5XgnCGZjnoSUzhbuO7T4IGwVas_UfoZph6l_-Cgp6EDXbma3o6YaTSYDQq8RSA0n9BQEjGSF9eXuhf47lMPG3qepUkPQAIhNiHDzHD3a_qepT0TYEdCt0f5X9DmYrx2_j_t9le2psqsnMwL2aIUDDml-6cFjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت های یک عرب درباره ایران:
ایران از جامعه عرب متنفر است، یک تنفر تاریخی.
همانگونه که اسرائیل از جامعه عرب تنفر دارد.
اگر کتاب فردوسی(کتاب شاهنامه و قوم پارس)رو بخونید شک ندارم که ممکنه باعث بشه بالا بیارید.
چرا؟چون عرب را به زشت‌ترین اوصاف وصف میکند.
مثلا فردوسی گفته:عرب در آن مکان خورنده ادرار شتر است،خورنده ملخ اس، ولگرد و کثیف است.
اما فردوسی میگوید اینجا در ایران حتی یک سگ در اصفهان از آب پاک و زلال رودخانه میخورد.
حتی یک سگ در اصفهان شریف تر از عرب در آن مکان است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69324" target="_blank">📅 20:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69323">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea4c431667.mp4?token=nHzmzAAUOlPEj544qDNRl2XsyL8HygFLv8V8ZBNrJu8h7-FGOJR_tuxwVUGUBHV-WDkHopT3PKiVr9koZ53nk1wlt-H_et_Svpcf-hKRNMlliU0ZNT74N4etuRMHf-8QwvxWCzFjgDrwDVzYPkJwiezUM9D7b91CaI-6rSgqRC5pFIXVtMInH_dmcCsatDLW74ZwN1yfRfZAoqbvvXrYXS2rMVKBNoHM5Ew5lpKU09RPsvthrKUYAg1YHnon2oTHmUavmrhY8kanS8tr93mf4vS9B0xNAdkVjujdOOaMr59ULe-rLuvKh_KAr2GQlB_edAptGv2RQw6bjKF0Up4Few" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea4c431667.mp4?token=nHzmzAAUOlPEj544qDNRl2XsyL8HygFLv8V8ZBNrJu8h7-FGOJR_tuxwVUGUBHV-WDkHopT3PKiVr9koZ53nk1wlt-H_et_Svpcf-hKRNMlliU0ZNT74N4etuRMHf-8QwvxWCzFjgDrwDVzYPkJwiezUM9D7b91CaI-6rSgqRC5pFIXVtMInH_dmcCsatDLW74ZwN1yfRfZAoqbvvXrYXS2rMVKBNoHM5Ew5lpKU09RPsvthrKUYAg1YHnon2oTHmUavmrhY8kanS8tr93mf4vS9B0xNAdkVjujdOOaMr59ULe-rLuvKh_KAr2GQlB_edAptGv2RQw6bjKF0Up4Few" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🤡
یه بخشی از صحبت های خیلی مهم ترامپ: بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ  @HutNewsPlus</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69323" target="_blank">📅 19:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69322">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭𝐍𝐞𝐰𝐬➕]</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/884550e186.mp4?token=FSyzRKiTxtxGc1f0IO84IM6Y9feuABiMqTS63tqQk-a8WVaIJfcdPRsaFBf-2AKu_Po4jg5wYjiCO6IWFjnpGGZlZ6UL7IVxBqVYhbfGKln7XJRG7nsjxiZ0fb5GuscRgjMEZrEahNkYZBEmv56plNYujnFjQQvZmXWA2ndkrXCyJDQxyPp_WzpI69j5wJ8fDO9mr4HFUShmNu3FMiA8xn6y17npCuSeSVUUMw7a_2ox75i1a5c0YoRodxqcc40hC8aMk9GcVUkJ7D_C4yWPAuEhUDWa7zkMhH8KPpjWXgdoJ18SwclQQ1oyA7DzoEcqXsm7442UPLy4oTj_oIFdGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/884550e186.mp4?token=FSyzRKiTxtxGc1f0IO84IM6Y9feuABiMqTS63tqQk-a8WVaIJfcdPRsaFBf-2AKu_Po4jg5wYjiCO6IWFjnpGGZlZ6UL7IVxBqVYhbfGKln7XJRG7nsjxiZ0fb5GuscRgjMEZrEahNkYZBEmv56plNYujnFjQQvZmXWA2ndkrXCyJDQxyPp_WzpI69j5wJ8fDO9mr4HFUShmNu3FMiA8xn6y17npCuSeSVUUMw7a_2ox75i1a5c0YoRodxqcc40hC8aMk9GcVUkJ7D_C4yWPAuEhUDWa7zkMhH8KPpjWXgdoJ18SwclQQ1oyA7DzoEcqXsm7442UPLy4oTj_oIFdGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🤡
یه بخشی از صحبت های خیلی مهم ترامپ: بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ
@HutNewsPlus</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/69322" target="_blank">📅 19:56 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69321">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caed943dd3.mp4?token=h8ZkSbNjvfI0KQifZu50FyhSYxGK5qJBv-pl-p8Y6cXjnC5mhp2b4VzQWm4cWhPfBBULUJHij4eAvjJIaUZrhQwDnmLL-7BS87U5aI3EmG5eJ3AknuqN4uJRn-d0ZJnYWW9vZnyEfu8Th42-loJ0Vl14u1XmvMJWsWlJKFVbstnvHnLwci5ZnyaeB5FxU4UmKutokVYAFPwbIuzsH19QH9p2CWrUXERFOiwsUBGLEWc4qwVcNS0KitNAdIcPnp-9j_V9I9_NIpdpG6RDVa8VqK0aaSbuIXSiQG7vWTkVjTFzSQVAEC-_1WukwnfBf7gOYLxoATV4hhUdNmDuDz0QtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caed943dd3.mp4?token=h8ZkSbNjvfI0KQifZu50FyhSYxGK5qJBv-pl-p8Y6cXjnC5mhp2b4VzQWm4cWhPfBBULUJHij4eAvjJIaUZrhQwDnmLL-7BS87U5aI3EmG5eJ3AknuqN4uJRn-d0ZJnYWW9vZnyEfu8Th42-loJ0Vl14u1XmvMJWsWlJKFVbstnvHnLwci5ZnyaeB5FxU4UmKutokVYAFPwbIuzsH19QH9p2CWrUXERFOiwsUBGLEWc4qwVcNS0KitNAdIcPnp-9j_V9I9_NIpdpG6RDVa8VqK0aaSbuIXSiQG7vWTkVjTFzSQVAEC-_1WukwnfBf7gOYLxoATV4hhUdNmDuDz0QtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
خبرنگار:
در مورد ایران، گزارشی وجود دارد که نشان می‌دهد شما پیشنهادی از سوی ارتش برای گسترش چشمگیر فعالیت‌ها دریافت کرده‌اید.
ترامپ:
ما از قبل گسترش داشته‌ایم. منظور از "گسترش چشمگیر فعالیت‌ها" چیست؟
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/69321" target="_blank">📅 19:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69320">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">املاکی تو یه جمله همزمان گفت هم می‌خوایم خیلی شدید به اونا ضربه بزنیم و هم می‌خوایم خیلی مهربون باشیم باهاشون
🤡
#hjAly‌</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/69320" target="_blank">📅 19:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69319">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0411d5fa4.mp4?token=BaIV-8WR7DTGmjfpe_3rtxRXVXlY0pQCafYm2_CX8gRjfAFZ3bUZ8nFKh1lGB1G9BUlN4aBnwyTwTTrlm2LVcCLPCgcoQyeKaYly8h8RWvzqbo13zbXDP2U2_b7qQ6zDEoeq2yd0d6qquYy-KJ7g0it09JMIXN89086eP2wudYHqoNn6qsG1EoQv3qJoCZNHRF300HQ3zNMy0pTPT_doX05CLw18Bx6jbh85g4w1un-iLcn-c1zBXqEr8SgGCV5cQpo8k6b7H9HkI3zrbPSTTr037jWDscRBeuesz_aHeZdYYmg9yKJYIrhb5_A4VelbBh9oaJHaeEDwwvHLzJ0mKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0411d5fa4.mp4?token=BaIV-8WR7DTGmjfpe_3rtxRXVXlY0pQCafYm2_CX8gRjfAFZ3bUZ8nFKh1lGB1G9BUlN4aBnwyTwTTrlm2LVcCLPCgcoQyeKaYly8h8RWvzqbo13zbXDP2U2_b7qQ6zDEoeq2yd0d6qquYy-KJ7g0it09JMIXN89086eP2wudYHqoNn6qsG1EoQv3qJoCZNHRF300HQ3zNMy0pTPT_doX05CLw18Bx6jbh85g4w1un-iLcn-c1zBXqEr8SgGCV5cQpo8k6b7H9HkI3zrbPSTTr037jWDscRBeuesz_aHeZdYYmg9yKJYIrhb5_A4VelbBh9oaJHaeEDwwvHLzJ0mKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
«ایران وضعیت خیلی بدی داره؛ واقعاً خیلی بد. اوضاعشون خیلی خراب شده و تحت فشار شدیدی هستن.
تعامل باهاشون هم خیلی سخت بوده؛ هم صادق نبودن، هم قابل اعتماد رفتار نکردن.
ولی این چیزی رو عوض نمی‌کنه؛ چون در هر صورت، حال و روزشون خیلی بده.
ما فقط پنج ماهه اونجا هستیم. اگه به جنگ ویتنام نگاه کنید، می‌بینید آمریکا بیست سال اونجا بود. کاری که الان علیه ایران انجام می‌دیم، از نظر من یک عملیات نظامیه، نه جنگ.
ایران هنوز چند تا موشک داره، اما خیلی کمتر از چهار پنج ماه پیش.
توان تولید موشک‌شون تقریباً از بین رفته و ظرفیت پهپادیشون هم تقریباً نابود شده.
البته هنوز مقداری از این توانایی‌ها رو دارن.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/69319" target="_blank">📅 19:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69318">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b0ec710b6.mp4?token=BWoaeB7k6KE6JjdN5ZMoMB7x48d9aVGdMvvn4PU0wbS7Vz5UwnxCxju_IWkQZylT8Sa6QMxdUXieeZ2qv96XoqKsANJeMdIIKPq7jdZ97L06phjQSRaWYvQJn8ZWT17vo1SP-9L65Kc03aJWTbNlE4sX_JMP9jDJT0y3NStpTHIqpd-3NlWMjwAQE7a9riXboauH7fAdYmLObr8M5-hiU1ZGdnN1lfJQElqzUVFt58mc7EGaKezoJOiEN6DaWjar_jPd7WWRJuvAQcP196_dTSvDOdE2Fl_Ux-KFFlr4ykDrOhNxo6TXDllHzxMg2qz_yxnlxR_rP_eaxXsl2spjMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b0ec710b6.mp4?token=BWoaeB7k6KE6JjdN5ZMoMB7x48d9aVGdMvvn4PU0wbS7Vz5UwnxCxju_IWkQZylT8Sa6QMxdUXieeZ2qv96XoqKsANJeMdIIKPq7jdZ97L06phjQSRaWYvQJn8ZWT17vo1SP-9L65Kc03aJWTbNlE4sX_JMP9jDJT0y3NStpTHIqpd-3NlWMjwAQE7a9riXboauH7fAdYmLObr8M5-hiU1ZGdnN1lfJQElqzUVFt58mc7EGaKezoJOiEN6DaWjar_jPd7WWRJuvAQcP196_dTSvDOdE2Fl_Ux-KFFlr4ykDrOhNxo6TXDllHzxMg2qz_yxnlxR_rP_eaxXsl2spjMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پیت هگست:
اگر برایتان سؤال است که چرا حوثی‌ها، با وجود اینکه یکی از نیروهای نیابتی ایران هستند، وارد این درگیری نشده‌اند، دلیلش این است که به مدت ۴۵ روز، قدرت نظامی آمریکا را از نزدیک تجربه کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/69318" target="_blank">📅 19:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69314">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64a849aad2.mp4?token=n0otllv7Cz5sGUWunFQQNDP1i_Z2e_pSPFt-m8sczRsXwr9t65ae88DJPnlZPug7E1Q3TMoXpJ7yoQzvzSfyAYf04rXxzuEI28W7vvsfp49JzNKkbMwrCapRfLSJG9HW3Eb1XDHrxNcsNEBQegbFa2f0C4GqADwN9w6JymBSRNhrm2FKxa8vdWAaY8kuuvYECocmbx_LIeA1IreovkCucxWVOh-TFg64bjwM6nKRIrnf-BCVrsxZFbf2zm6t3ZMr-teVzV3bcZVnFA9kf4C_7o63h10j9aHMrucHSujnu_-eH74Jk2GyMtf4FE_jsSoxsW7mztB9Xznw6D_g0wqspw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64a849aad2.mp4?token=n0otllv7Cz5sGUWunFQQNDP1i_Z2e_pSPFt-m8sczRsXwr9t65ae88DJPnlZPug7E1Q3TMoXpJ7yoQzvzSfyAYf04rXxzuEI28W7vvsfp49JzNKkbMwrCapRfLSJG9HW3Eb1XDHrxNcsNEBQegbFa2f0C4GqADwN9w6JymBSRNhrm2FKxa8vdWAaY8kuuvYECocmbx_LIeA1IreovkCucxWVOh-TFg64bjwM6nKRIrnf-BCVrsxZFbf2zm6t3ZMr-teVzV3bcZVnFA9kf4C_7o63h10j9aHMrucHSujnu_-eH74Jk2GyMtf4FE_jsSoxsW7mztB9Xznw6D_g0wqspw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🇪🇸
آخرین آپدیت از وضعیت اسپانیا:
- مهاجرین غیرقانونی همین‌جوری تو سطح شهر پخش شدن.
- چندین مورد دزدی از فروشگاه‌ها گزارش شده.
- کنترل اوضاع از دست پلیس اسپانیا خارج شده.
- مردمِ محلی گروه تشکیل دادن و دارن هرجا مهاجر می‌بینن، کتک‌شون میزنن!
- تو بارسلون هم مردم دارن خونه‌هاشون رو از ترس مهاجرین، سیم خاردار می‌کشن...
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/69314" target="_blank">📅 19:39 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69313">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: به زودی، دیگر چیزی از ظرفیت نظامی ایران باقی نخواهد ماند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/69313" target="_blank">📅 19:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69312">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: ایران در تعامل با ما صادق نبوده است
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/69312" target="_blank">📅 19:29 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69311">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14e0b272c3.mp4?token=Zu096tdsWhkzqN6zKeJO9Ueb2ZL8OPk9j1ZlhfvouPFwpruKf0VwUkd2XtMtxRmrZ0uNJ5t2e1aoWginq4zm_Qbq7fIuRrKMWJmS4kYeTIbHnHMJLMXfpDhv86z2mYyQ4S38Tgj4dRtbE6PoSt-FnxMZxnbFi2YSrlzAXcYUcBfaA17sGZVw_MDkiUUO3gY8l_gtRZSjyqVUhbAv44r9bFnvv0unoH9BnvuBbzP0xgi0xuARnwviHu04fz2ioFGTb22qKuSkj79vofgKYRPTa03DYYXL8Fl7hBG3V_1Yu3DcoIoFQbhK3oh6W8RAZZGIJiopipEcZbKfzSj4FmmQpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14e0b272c3.mp4?token=Zu096tdsWhkzqN6zKeJO9Ueb2ZL8OPk9j1ZlhfvouPFwpruKf0VwUkd2XtMtxRmrZ0uNJ5t2e1aoWginq4zm_Qbq7fIuRrKMWJmS4kYeTIbHnHMJLMXfpDhv86z2mYyQ4S38Tgj4dRtbE6PoSt-FnxMZxnbFi2YSrlzAXcYUcBfaA17sGZVw_MDkiUUO3gY8l_gtRZSjyqVUhbAv44r9bFnvv0unoH9BnvuBbzP0xgi0xuARnwviHu04fz2ioFGTb22qKuSkj79vofgKYRPTa03DYYXL8Fl7hBG3V_1Yu3DcoIoFQbhK3oh6W8RAZZGIJiopipEcZbKfzSj4FmmQpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🚨
ترامپ با بالگرد «مارین وان» (Marine One) وارد «کمپ دیوید» شد تا سیزدهمین جلسه کابینه دولت دوم خود را در آنجا برگزار کند.
فاصله کمپ دیوید تا کاخ سفید با بالگرد تنها ۳۰ دقیقه است و رؤسای جمهور آمریکا از زمان فرانکلین روزولت (FDR) در سال ۱۹۴۲ از این مکان استفاده کرده‌اند.
نام این مکان برگرفته از نام نوه‌ی آیزنهاور، یعنی «دیوید» است که توسط خود او انتخاب شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69311" target="_blank">📅 19:09 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69310">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aNYH3anO-rMpGJzM6NNTIbtKGJPBWnBOEYon8CTdvqKfzHTyfnWjya0t6IAPSs7X_U6ddvySbfxy7T-9S7BeBlpSr9OkgGWC1nL7j_nc2HmEi4UmLjk8HnL2Kdi6EtD1VqkDI2L4K2Re6BZOjDyDYVnkOD4Uv8GHZt2yRNBgQ2u0i7ATzS2RY6dKe0lK4QXWihs2ZD2Jtr5a3g19aN7yLe9u79KaxfI1Y3ifKCbs-8H-W7T4pDk3xse5rbKt32THPN0A7kFXdUPuEwpq1TO4B7PkWjQDvQGGt5F4sFuDd9wZcAwe8l2z4i90ravggkMeYrE_lx6hGIWdTV5GSC0zaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
نهاد مدیریت آبراهه خلیج فارس:
به علت تداوم اقدامات تجاوزکارانه نیروهای نظامی ایالات متحده در منطقه، تردد از تنگه هرمز امکان‌پذیر نمی‌باشد. به محض برقراری ثبات و آرامش، کلیه درخواستها بر اساس ترتیب و زمان‌بندی بررسی و مجوزها به مرور صادر خواهند شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/69310" target="_blank">📅 18:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69309">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
حملات پهبادی به جزیره بوبیان کویت
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/69309" target="_blank">📅 18:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69308">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31550cb053.mp4?token=TJJRZkMC-1lOFTnnMBlzDfhih-aCb7ZGL3pV9nUqPBPTznwwvnROxI31m5vEFY40PHIDpQi6dif-ZngfNsoVA-Dt8tJH3nE47qcLF-3wJjRgAUOPeFRTCG8sVGLnZzJKCYWrZNYqHV4yTJZAiumpLHPtWbiMjxcEAGNcCw-NMaPe7cYTBvqxqSckl-tFk-wWiOTN_QExBez1VfEFosP9g-Cyg-d4viy6U-XxV1685qoENAuYpuXYypM4FhnXzx_tpU92sA7k1qPHut_WebM6Z4BU51mLOcX3lJgO2T0VR33_tJwtNYps0tKq9et3R1Qq_ATuMMFDqQqxDhgBBnqfDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31550cb053.mp4?token=TJJRZkMC-1lOFTnnMBlzDfhih-aCb7ZGL3pV9nUqPBPTznwwvnROxI31m5vEFY40PHIDpQi6dif-ZngfNsoVA-Dt8tJH3nE47qcLF-3wJjRgAUOPeFRTCG8sVGLnZzJKCYWrZNYqHV4yTJZAiumpLHPtWbiMjxcEAGNcCw-NMaPe7cYTBvqxqSckl-tFk-wWiOTN_QExBez1VfEFosP9g-Cyg-d4viy6U-XxV1685qoENAuYpuXYypM4FhnXzx_tpU92sA7k1qPHut_WebM6Z4BU51mLOcX3lJgO2T0VR33_tJwtNYps0tKq9et3R1Qq_ATuMMFDqQqxDhgBBnqfDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
رئیس‌جمهور ترامپ در گفتگو با فاکس‌نیوز:
«اوضاع خوب پیش می‌رود. تنها کاری که می‌توان کرد این است که به پیروزی ادامه دهیم؛
آن‌گاه سرانجام اتفاقی خواهد افتاد.
ما ضربات سختی به آن‌ها وارد می‌کنیم و آن‌ها را کاملاً گیج و سردرگم کرده‌ایم، و همچنان به پیروزی ادامه می‌دهیم.
سرانجام آن‌ها چاره‌ای جز بازگشت به خانه نخواهند داشت.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69308" target="_blank">📅 18:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69307">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mkMtRWAhpuI52c2XR9f8b8c5BO72jJvKB6H4rvy0tm51x-qUawWBEBbl9PYEGGmrkK3VEvBOkbE6Occ1cCjBSzbhzDDVpOlIQj_UViyPDVzxtdSrqwgAJyC2j2RneclRasa6af4rCIHNBg-crZVxJnZSa9bXz4e_931HMaHQCF9Sd8ANFCV-lw9zXu7ZQI6Ka6O6GP2kvK7l3Y2ZvIYWWLpLY4S-aokHwBvlFJk5sinf0R8zLSP2JMENHZwXpQlu3KbE_RJi0k75JIAdDK-KlRO1BJpkdmMJ5TtLyHuHV68fkPNgovf4J2sBPtKqn_ceqp6MdFG9ljv9BZ04jp09jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇼
❌
🇮🇷
وزارت دفاع کویت:
نیروهای مسلح پهپادهای خصمانه‌ای که اوایل امروز وارد آسمان کویت شدند را رهگیری و نابود کردند.
حملات ایرانی همچنین چندین سایت نظامی و زیرساخت‌های حیاتی را هدف قرار دادند که باعث آسیب مادی ناشی از سقوط آوار شد، اما هیچ تلفاتی گزارش نشد.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/69307" target="_blank">📅 17:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69306">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4497b03176.mp4?token=alQ49QLzGsqGsvancpo8uCvLsMhlF1s5F7bSXZ-CFE9IzH2EVpltLyW_I7xQ9YbKxcqkyd5DK29E9kGtGJzieP8Rxert_wj3ROKw82tjgzSKnph0tRN4huBfa4ox9nvVXf5WteqWKVH4Z3XkEkUTTYX0yC0aDa9xMAJWYu7FA4vD4puP512b5jAHWZBqEiOvVohpKaKOTFHeWnslArN3yIUWaW_HHYGSjhM0tHRbc8qlmgWLQf-1geR1H1lzu3RgoGY-LIjXniCJL_rcI_Szh9v50ym-6umFjNp4uNXzEtKrW-GoKpZVkofri89UKC-n9o5dQKa6q0ACuYLbjJY6qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4497b03176.mp4?token=alQ49QLzGsqGsvancpo8uCvLsMhlF1s5F7bSXZ-CFE9IzH2EVpltLyW_I7xQ9YbKxcqkyd5DK29E9kGtGJzieP8Rxert_wj3ROKw82tjgzSKnph0tRN4huBfa4ox9nvVXf5WteqWKVH4Z3XkEkUTTYX0yC0aDa9xMAJWYu7FA4vD4puP512b5jAHWZBqEiOvVohpKaKOTFHeWnslArN3yIUWaW_HHYGSjhM0tHRbc8qlmgWLQf-1geR1H1lzu3RgoGY-LIjXniCJL_rcI_Szh9v50ym-6umFjNp4uNXzEtKrW-GoKpZVkofri89UKC-n9o5dQKa6q0ACuYLbjJY6qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کابینه ترامپ برای بررسی اقدام بعدی خود در قبال ایران به کمپ دیوید می‌رود.
این خبر ساعاتی پس از آن منتشر شد که ترامپ از توافقی «تاریخی» با میانجیگری مصر، قطر و ترکیه خبر داد که بر اساس آن حماس با خلع سلاح کامل موافقت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/69306" target="_blank">📅 17:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69304">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/006b9f5bfa.mp4?token=iKdQQa_NKqcLM6yWyKNLpXpyXp1sZ9_HHQXum_SlNATNtEiRQUbPolO0GXCsVdRYlFUBPHZ3u35Ckb9NMvAhgsPUmW5FrCYmAzkJ-1b9gFMBKWR85CLc7zV3N61z8OzmmTSBaJl2EDPhNkPedxRfb-nXXW6Tn0Uvg5ViWwsrgWZEoJxxNY_PMTf-qRCEV8B6-YJk8oNeebzjrJ-tyDLPOtjKITxdPnwcK-kBbn22sSwmIrPfpBappvOdQhI9E54WbY1PDZLL2b1PzPshbPgn5LZ19jKlu8rD8hUgI_Amn8UsnJYbhGiCjBzbaU--lVx3XKiUt5HJB73dzKoYrbt0Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/006b9f5bfa.mp4?token=iKdQQa_NKqcLM6yWyKNLpXpyXp1sZ9_HHQXum_SlNATNtEiRQUbPolO0GXCsVdRYlFUBPHZ3u35Ckb9NMvAhgsPUmW5FrCYmAzkJ-1b9gFMBKWR85CLc7zV3N61z8OzmmTSBaJl2EDPhNkPedxRfb-nXXW6Tn0Uvg5ViWwsrgWZEoJxxNY_PMTf-qRCEV8B6-YJk8oNeebzjrJ-tyDLPOtjKITxdPnwcK-kBbn22sSwmIrPfpBappvOdQhI9E54WbY1PDZLL2b1PzPshbPgn5LZ19jKlu8rD8hUgI_Amn8UsnJYbhGiCjBzbaU--lVx3XKiUt5HJB73dzKoYrbt0Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
شهر سئوتا، منطقه تحت کنترل اسپانیا در شمال آفریقا، با یه بحران جدی امنیتی و انسانی روبه‌رو شده.
فقط توی یک هفته گذشته، حدود
1500 مهاجر
با شنا خودشون رو از مراکش به سئوتا رسوندن.
رئیس دولت محلی سئوتا گفته مراکز پذیرش دیگه ظرفیت ندارن، صدها نفر مجبور شدن توی فضای باز بخوابن و مراکز نگهداری از
کودکان و نوجوانان بدون همراه
با
2400 درصد ظرفیت
در حال فعالیت هستن.
الان به‌طور میانگین
روزانه 300 نفر
وارد سئوتا می‌شن و مقام‌های اسپانیایی نگرانن که دوباره بحران سال
2021
تکرار بشه؛ زمانی که حدود
10 هزار مهاجر
فقط در چند روز وارد این منطقه شده بودن.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/69304" target="_blank">📅 16:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69303">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fkKpHMC8KKIMiPugGySacB2Pay28ILoEsyyjVqGJ0ujIGOxXZI1uH8jvr6Zm4QEJbG-kI-B5oc1G9vaN3LM850Cprl_Mgv0MyoNTIXyO694gQlv1mNR5iJY-VLTKdrmi023lhWtvzgrm44MTd5TxKFuWCELf6pTq6CZ1LyTa5mPXcioMgcucgqZa3G0LG4Tzquwip6Rw9xDfHe_21F5Rs80PqfJlb1b8uU-ab68RyiJ-oOToRP_BH4rqqPgXfzaFSJCFQxF-Qa1DESWNjoH2H0lI_q1i-yMROZ2IlcFgiPgzWbw416P78Rm1W6HnxOyGXapLGLEuYmTLV46Mcrxcdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پسر رئیس بانک سپه که دهه هشتادیه معاون بانک دی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69303" target="_blank">📅 16:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69302">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g7vuiqrGEKsm-9OjfAI9C0vM2usR9jQC0akpA6RPwa6LyfcyTmVQd5goKw3r_vbbLxir9_bOlq073WpeS-CZ1SakRpUnP-2hx1VIkn6YwC7IJLfpWVrrcikmFRDulQHiPldFzxnu-iRJlyafVuQ0NpJq1Y0QYrdy-lBqctUoWUztiRuJfHHOhwJQff0-9SSdNtHx4qvqdbcnE7VOfdLiUDV89KExFW_H9wrrO1Aqog0mvrYZMjME9fdwJTgjic4Hwa3b3T9UjWCulUj5GWuE21YXvJaNj_NkTR5147CUn49s2go03BEuCo1kSw1q9xMcp7qdvcyr5bVfclCOcxMl1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
طبق داده های نت بلاکس دولت ترکیه اینترنت کل مردم رو قطع کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69302" target="_blank">📅 15:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69301">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OOnm7m7H-elohZAHCDaODmV5DL4DLleGv3a-9bckK3od86B1bxcjD874mgxNMgRbSVPkeZ-NtOFR9WHcWDMk-lTRzQB1xh8Asy3rNdQIKMexFiq3zFfowIjUEAgTzKAKzjo9ccrRZ4hHG8Dmnixu0NgYGOs0V5iyxHmWihuXmlK9jdFrW38n8cUZfQZzEDWDRwQOMYA0t7vcu2Lf09qodyGYFgRq1xp1HRiE9XCiIE8cBOSb-N1q8DE9h7UE-Crsy7jgYMwAEWer_KcdyWiWb6xGoWsO06c6-8sucEhIA2zq30FZrLZnki3nnDHd44Txa_5mIWRTFiQY83DjS5gBLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
گاردین:
عربستان داره خودشو برای یه عملیات نظامی گسترده دریایی و احتمالا زمینی، علیه حوثی‌های یمن آماده میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69301" target="_blank">📅 15:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69300">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🇺🇸
رویترز:
پرزیدنت ترامپ امروز در کمپ دیوید با مقامات ارشد دولت، تیم امنیت ملی و فرماندهان نظامی دیدار خواهد کرد تا درباره مسائل مختلف و از جمله جنگ ایران گفتگو کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69300" target="_blank">📅 15:10 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69299">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb0ff0fef7.mp4?token=NevpoSbCkW19zy2CyRBMH4QdtGDwoGEJQ3-WvAOLSsHBBZKHhYAKsMaSxyaPPjUZhmk0sKvtCTrXwk-8JlhHj6NUUc0j_i-OGDRdcm3GqBBGr4RsbAXXk4LD_dwdgLknTvkKOcXglxcgxmTs385tZVAcrEc0-6efVF-kyA835o_D7PSCw8w3aL1SI6p5IEAfqNXx6t8p3kozEYzJ6xoc74IGMha79--WhFpGY-X-i8mclXhvjRbSvDw20j9cNJoGnJFQaP8zaVwIicaM1Elb9jaquCXOGUtAMT9JT-gD2SV2WHDa437fwpgLX8jV527fOaEK7NgD0XAbvsXqXiFrsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb0ff0fef7.mp4?token=NevpoSbCkW19zy2CyRBMH4QdtGDwoGEJQ3-WvAOLSsHBBZKHhYAKsMaSxyaPPjUZhmk0sKvtCTrXwk-8JlhHj6NUUc0j_i-OGDRdcm3GqBBGr4RsbAXXk4LD_dwdgLknTvkKOcXglxcgxmTs385tZVAcrEc0-6efVF-kyA835o_D7PSCw8w3aL1SI6p5IEAfqNXx6t8p3kozEYzJ6xoc74IGMha79--WhFpGY-X-i8mclXhvjRbSvDw20j9cNJoGnJFQaP8zaVwIicaM1Elb9jaquCXOGUtAMT9JT-gD2SV2WHDa437fwpgLX8jV527fOaEK7NgD0XAbvsXqXiFrsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
🇺🇸
🇮🇱
تلگراف:آمریکا و اسرائیل در حال بررسی طرح محاصره زمینی ایران هستند!
به گزارش روزنامه «تلگراف»، آمریکا و اسرائیل در حال بررسی احتمال اعمال محاصره زمینی علیه ایران هستند تا فشار اقتصادی بر این حکومت را تشدید کنند.
دونالد ترامپ و بنیامین نتانیاهو در جریان گفتگوهای خود در دفتر بیضی‌شکل کاخ سفید، درباره «ابزارهای نظامی (کینتیک) و غیرنظامی (غیرکینتیک)» بحث و تبادل نظر کردند؛
از جمله اعمال فشار بر همسایگانی نظیر عراق و پاکستان برای تشدید کنترل یا بستن گذرگاه‌های مرزی.
یک مقام ارشد اسرائیلی به تلگراف گفت: «اگر مسیرهای زمینی را مسدود کنیم چه می‌شود؟ فرض کنید ایران دیگر نتواند هیچ کالایی وارد یا صادر کند.»
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69299" target="_blank">📅 14:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69298">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🇮🇱
وزیر دفاع اسرائیل ، یسرائیل کاتز:
اگر ترامپ از ما بخواهد، به حمله به ايران ملحق خواهیم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69298" target="_blank">📅 14:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69297">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34cbdd236b.mp4?token=gBqf6VYu9V8cKlOj7URWj5dbBulW1p3_LAW1U0EHJl-4eyGHPSNGeHfxOml5VAXGE2M6MRWMZz_uU9Xx2wKS_qS6fR3h5Nws574QJgKOYWhLjKbaSJVHjw3dNRxEbqS5nP9K5qGUGoT6uJGYlF2_iwXZPPuqEcnSHOA1nFDdbKgDl4Ku_roS2rJxWLe0M8URNKsikIN_3kGcX5byauhvwM0xHET3Mej1Byx5XbmPf3SfoYNI-fZ4LI3gBYOzln5o58ErFco3aiGprw6CFuU1gQEs8iv9YCNN-8SfozjewzYCAaeQIuw8mah5w49keMuJYV4jYelLvuKkXas1SEIw6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34cbdd236b.mp4?token=gBqf6VYu9V8cKlOj7URWj5dbBulW1p3_LAW1U0EHJl-4eyGHPSNGeHfxOml5VAXGE2M6MRWMZz_uU9Xx2wKS_qS6fR3h5Nws574QJgKOYWhLjKbaSJVHjw3dNRxEbqS5nP9K5qGUGoT6uJGYlF2_iwXZPPuqEcnSHOA1nFDdbKgDl4Ku_roS2rJxWLe0M8URNKsikIN_3kGcX5byauhvwM0xHET3Mej1Byx5XbmPf3SfoYNI-fZ4LI3gBYOzln5o58ErFco3aiGprw6CFuU1gQEs8iv9YCNN-8SfozjewzYCAaeQIuw8mah5w49keMuJYV4jYelLvuKkXas1SEIw6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو عراق اهو گرفتن بکشن بدن به زائرا
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/69297" target="_blank">📅 13:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69296">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37edae9b59.mp4?token=h2kKaY38aahyc09L0dI2UOJZYsWvhE0m4vUjYbRYK7upAipc8HHRgdE_pnceH7xGHD0eHfyb9FHsfULWAIij2wYLcDVEIlcPb0f-qHWOW24XfS3OoDiKGCPwiFvv8k0jeLSgV7Hb8ILI9dMPYpZJvsFOnIwwADyUoSUL63xxDOosj5dPoppyd2fAf9fmr_m5jRq6Lx5CeJCektr867Id1AAcd6txnz1Ssd4dIPKATEEI4_VbbEHxNdoCEmBZQwecrvRvP44pGH4sRTdjtYO67bCruqZ0aIAI7RK83FZnyoJU0m_0SxMXXiG3myAiq_AyY68KPN7JPEDTPSJkfncHBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37edae9b59.mp4?token=h2kKaY38aahyc09L0dI2UOJZYsWvhE0m4vUjYbRYK7upAipc8HHRgdE_pnceH7xGHD0eHfyb9FHsfULWAIij2wYLcDVEIlcPb0f-qHWOW24XfS3OoDiKGCPwiFvv8k0jeLSgV7Hb8ILI9dMPYpZJvsFOnIwwADyUoSUL63xxDOosj5dPoppyd2fAf9fmr_m5jRq6Lx5CeJCektr867Id1AAcd6txnz1Ssd4dIPKATEEI4_VbbEHxNdoCEmBZQwecrvRvP44pGH4sRTdjtYO67bCruqZ0aIAI7RK83FZnyoJU0m_0SxMXXiG3myAiq_AyY68KPN7JPEDTPSJkfncHBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇷
روابط عمومی سپاه پاسداران:
ساعات ابتدایی امروز  ۲ نفتکش متخلف به خیال اینکه میتوانند از مسیر غیراعلامی ما، تحت اسکورت هوایی ارتش کودک‌کش امریکا عبور کنند، بدون توجه به اخطارهای ما، در مسیر ناامن و غیرقانونی حرکت کردند که مورد اصابت قرار گرفته و متوقف شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69296" target="_blank">📅 13:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69294">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Qb4aQGGOb7GDYuja9GYjlHYVwuxGinieJWC6PYwToYsQt7reQKhxH6asXyUhDPZqxVxG2qzILwdfoQRsUZbPsaY2Exyznw5cuZlpdTgg9cnc-p-CgISyrGZvy_DaeHokEpevlsstyoNNLcLc7gxahWq7d-AMmAtePJoDAHZyWtNgOx28Dk0T38PFW_ZsbLxO5pYbuBUQLcxvbiUfcXFnkug-4A5Db_elOfjJUgES193bTz2dx0m240ltZNvmBW_P_jDnqhSbDXGek1AX4M3-PLX09HaU2B8hl0Dt5X1tSosU3GMOwQcBzuqy13A_dJVIMmHttZrhwqAZfQbSZC0-Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bb843e99ad.mp4?token=feVkmQY3eUf-zROsDyX-WJXRqQd6hsq_Gby5reY_XB3rjkN6lGt6cTYU25staf4kNtYS8BsjCwrjvn4L3h5VxFYFuEQ1xH9BvjijVh9GVtqcQ4T_WfdgbKI7P7yWW5lXMbAcwADtfE8Ggg7GwSuZ7DdOK3ULvONbWEcggePu1ggjPbzPjnBPo42CpYreJeJq-YWNX6j4CPw0_WskOjRBtUiCKXQLdwDglhf392eO2mZL1-BU3oxPcmWrQq3vQDXg2eXf34G1U8DfKxop09bzP24prZrd_zhZYD0ChkhrwnA3UxapvcwhVpJqRRnpyZ4anzzVZPI-352VYG_DXNKaNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bb843e99ad.mp4?token=feVkmQY3eUf-zROsDyX-WJXRqQd6hsq_Gby5reY_XB3rjkN6lGt6cTYU25staf4kNtYS8BsjCwrjvn4L3h5VxFYFuEQ1xH9BvjijVh9GVtqcQ4T_WfdgbKI7P7yWW5lXMbAcwADtfE8Ggg7GwSuZ7DdOK3ULvONbWEcggePu1ggjPbzPjnBPo42CpYreJeJq-YWNX6j4CPw0_WskOjRBtUiCKXQLdwDglhf392eO2mZL1-BU3oxPcmWrQq3vQDXg2eXf34G1U8DfKxop09bzP24prZrd_zhZYD0ChkhrwnA3UxapvcwhVpJqRRnpyZ4anzzVZPI-352VYG_DXNKaNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی خامنه‌ای توی کربلا در حال پخش شربت دیده شده
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/69294" target="_blank">📅 12:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69293">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dDp2yP4n8rI4aA032Cldt1sBoQl4rxA6FBC1_lG-3v0BWlFxucSK0OFP7db7bFUGlD97EWapptigFbdMs0qveXqunhlEm0uVuejg5-g1lg-XlBi1OOtecDzo92t2FBTOQ7KfTOp8oj6cbz00DdM_0flu9EnpsW3YmllXgvyO331PbHZgLsKff714D36387MQDN72WGGpkJcUR1Sdrv2atjxbT3tje3IqJOUz2oJdErpNTTsdsWs-UeGW28G8bJEPVUI9a0roYV95eJL80zSURlBgWo0PLEHO4Vv9WIdWxUH6ulrPmLDyjAc4uxRipNvU5j7aj1iWkgN_q-soFDGsdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
گاردین:
یک موشک بالستیک روسی کارخانه تولید پهپاد در کی‌یف را که متعلق به شرکت «ترمینال اتونومی» (Terminal Autonomy) —شرکتی ثبت‌شده در ایالات متحده— بود، منهدم کرد؛ این نخستین حمله شناخته‌شده روسیه به شرکتی با مالکیت آمریکایی در اوکراین محسوب می‌شود.
این کارخانه پهپادهای تهاجمی مجهز به هوش مصنوعی تولید می‌کرد و گزارشی مبنی بر تلفات جانی در این حادثه منتشر نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69293" target="_blank">📅 12:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69292">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RBDMAzluIAAbzu9CruvJ5YGFnMJUFJ_cnshYee5ubPqxu_AaUoGJKBEuNWX4nyg3TFPucC9zDy8d1z7IVSgGI9Zplv_JhYS_QgtW81TAFSBY5VoH5P4k_QFPSICjGigVNRN9OYFF-LWeXx5zjrs9V-EbYj24kNpb32icei7_4Mm5LdXt3eumuxJuYN5Vi9uggjc6a7Z7gWfKIKoWtB3pQCuKgw0XpjXvg4ZpvLGTJMVwCLFzKgQR5uXqALWLX5YgQe925uVZLKwbb66s_7zjNvXit6SvRiNr6k1-6GUQcl7T6ZKkK_6olrP2NW1nbzqGpuG2PoB1s4VMo6vK6iUZOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
باراک راوید:
به گفته یک منبع آگاه، مقامات سپاه پاسداران از هیئت حماس که برای مراسم خاکسپاری علی خامنه‌ای، رهبر عالی پیشین، به ایران سفر کرده بود، خواستند که در امضای توافق‌نامه عجله نکنند و وقت بخرند.
یک مقام ارشد آمریکایی مدعی شد که ایران تلاش کرد حماس را متقاعد کند تا این توافق را امضا نکند، اما این گروه تصمیم گرفت به این توصیه عمل نکند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69292" target="_blank">📅 11:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69291">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a885a777d.mp4?token=MuCLcPD5FcpJUT96-ZFquLn8E_eLFw8NDw91I6dCzuD8FWqFddBZBNlLayVGAUNHsPPfGYxEb03oC66qnE_CRhjgZMFT_3KxI_67OgDE8oqNw5HR3ydSps08Rq2vZ-lWJWKt19jqyAWebEvd8yWD9TWOVusEGDUOASCZt6UEeML-17-x4wXjTZRvG3lQ8IpF2safvQ_K8xtwJFO-VfyZ29urCAXIAqDpcgunNx0bijAwUrWNkFDql6j8KhLNRcqcFlU18glVEOvj473NKiNBcNxz24W64S4oSqSIKLy3mDOpmr_u1KPzHja-_3IcM9iW_UoKHALW1hevk_XE6DQ4XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a885a777d.mp4?token=MuCLcPD5FcpJUT96-ZFquLn8E_eLFw8NDw91I6dCzuD8FWqFddBZBNlLayVGAUNHsPPfGYxEb03oC66qnE_CRhjgZMFT_3KxI_67OgDE8oqNw5HR3ydSps08Rq2vZ-lWJWKt19jqyAWebEvd8yWD9TWOVusEGDUOASCZt6UEeML-17-x4wXjTZRvG3lQ8IpF2safvQ_K8xtwJFO-VfyZ29urCAXIAqDpcgunNx0bijAwUrWNkFDql6j8KhLNRcqcFlU18glVEOvj473NKiNBcNxz24W64S4oSqSIKLy3mDOpmr_u1KPzHja-_3IcM9iW_UoKHALW1hevk_XE6DQ4XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
ویدئو وایرال شده از یکی از مراسمات عجیب آفریقایی ها که با شمشیر همدیگه رو میزنن
🙂
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69291" target="_blank">📅 11:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69290">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ng6Iw0KmHG0BIfgsJH57ZWCwHwribQDRXG3XouOPBIATxni7AUYevy5CtRTke7bS2NOgorwkrTh88CB1Rmzw4sInOm3oLEI-jIkA80k8a5YAx3jPoCJdAorKQzSkXEZVYBFfIua_IE8Ht5kS6YT9KZJNytwPqVUj0se-e9ib2PRTTaVNc_6YKzB-zllRIkxOtOX-ch5O6RDlrmpM3fzHpk3WpI0vakp-40SlHeQdrW2Byw2pPoIc59SjHlFrJp-X-Zf-okklo-MM7u80YEZF0d6mEMuZGHHPpPoGgaJ_uGLTsoCV9vqfIauKKOvsdByyRWDjuFNS7nEmCDXcNjFZRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇮🇱
🇮🇷
تایمز:سازمان سیا و موساد اسرائیل در حال تشدید جستجوی خود برای یافتن آیت‌الله مجتبی خامنه‌ای، رهبر جدید ایران، هستند که از زمان جانشینی پدرش پس از حمله هوایی فوریه ۲۰۲۶، در ملاء عام دیده نشده است.
مقامات اطلاعاتی معتقدند که او در این حمله به شدت مجروح شده است، بیش از ۱۵۰ روز از استفاده از تلفن یا لپ‌تاپ خودداری کرده و در یک پناهگاه زیرزمینی به شدت محافظت‌شده، احتمالاً در تهران یا نزدیک قم، پنهان شده است.
با توجه به اینکه نظارت الکترونیکی سرنخ‌های کمی به دست می‌دهد، جستجو از اطلاعات سایبری به اطلاعات انسانی تغییر یافته است.
مقامات سابق موساد می‌گویند که اعتقاد بر این است که مجتبی از طریق چندین لایه پیک ناخواسته که پیام‌های دست‌نویس حمل می‌کنند، ارتباط برقرار می‌کند و نفوذ به حلقه داخلی او تنها راه واقع‌بینانه برای تأیید موقعیت مکانی او - یا حتی اینکه آیا هنوز زنده است یا خیر - است.
برخی از چهره‌های اطلاعاتی گمان می‌کنند که سپاه پاسداران ممکن است مرگ او را پنهان کند، در حالی که برخی دیگر هشدار می‌دهند که رژیم ممکن است از بدل‌ها برای پنهان کردن حرکات او استفاده کند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69290" target="_blank">📅 10:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69289">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9be197f29.mp4?token=pHS91oVViAj-MQYlAMnuC4UmL_lJeyCzSimaR885arRt6CA9reJyS86wqfOYi2Ld9amNSjENFtZcMRH3AhG6GuM04lhWpkvXPRNoKO-SFvhPZHbQ3kRcn8n4CfG8RXWU7_3wMEEorjKHxluG-3DGiEWicJRxJXE4Bm9aGn4OK3nIo3QW9rqIfgeagCqCMpY5pQ-rAMmR_BZ_T8-cVnahz9Et0FTpwfbiRK0WjTUqEGmz9y4aOxxd7qo6zg9mtJC11kmvGVgyNgBjTI9HNsaRhhZL6waA1Ws7n9eL8t1feyfeLmoduaq3xiEU6d4zamtrkm64vdMKYbQBK-uMM6xhXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9be197f29.mp4?token=pHS91oVViAj-MQYlAMnuC4UmL_lJeyCzSimaR885arRt6CA9reJyS86wqfOYi2Ld9amNSjENFtZcMRH3AhG6GuM04lhWpkvXPRNoKO-SFvhPZHbQ3kRcn8n4CfG8RXWU7_3wMEEorjKHxluG-3DGiEWicJRxJXE4Bm9aGn4OK3nIo3QW9rqIfgeagCqCMpY5pQ-rAMmR_BZ_T8-cVnahz9Et0FTpwfbiRK0WjTUqEGmz9y4aOxxd7qo6zg9mtJC11kmvGVgyNgBjTI9HNsaRhhZL6waA1Ws7n9eL8t1feyfeLmoduaq3xiEU6d4zamtrkm64vdMKYbQBK-uMM6xhXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو وایرال شده از حمله عجیب طرفداران حکومت به بنر ترامپ و نتانیاهو
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/69289" target="_blank">📅 09:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69288">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">‼️
دلایل سقوط شوروی که صداوسیما پخش کرد در مقایسه با وضعیت الان ایران!
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/69288" target="_blank">📅 09:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69287">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/418bb6362d.mp4?token=OeWCRz7xDfuK067U3WjrzTqEBiSCvseZPRXwyvpjdt9rcxHSSl56xtIaFOr9jhu9ujTjcwVRAdbHnTAHzHHYddDl8TisBPxafvgLuv5x5-imZLBWW_PM5vZE1e7jnrEiJ5M78eoX2PnUMsA7cAlDAbznl2WxOc5hLQdIcsg1anZFF-cjikgs_SkR0N9gp5DgSTGTNzgEZaOYkluvcpzqG8dIjT-QlI6bHn1m_hbkAWCwEYQBOSPb-01MsHLGN8j47yuSJaWjprBmCnwYgM0HSWV1OylAXv5_lBS0d_LaBrDlQm3X6JCJIrXcJA-m2GvfR0FK1rfR2MtQ6j2LClygzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/418bb6362d.mp4?token=OeWCRz7xDfuK067U3WjrzTqEBiSCvseZPRXwyvpjdt9rcxHSSl56xtIaFOr9jhu9ujTjcwVRAdbHnTAHzHHYddDl8TisBPxafvgLuv5x5-imZLBWW_PM5vZE1e7jnrEiJ5M78eoX2PnUMsA7cAlDAbznl2WxOc5hLQdIcsg1anZFF-cjikgs_SkR0N9gp5DgSTGTNzgEZaOYkluvcpzqG8dIjT-QlI6bHn1m_hbkAWCwEYQBOSPb-01MsHLGN8j47yuSJaWjprBmCnwYgM0HSWV1OylAXv5_lBS0d_LaBrDlQm3X6JCJIrXcJA-m2GvfR0FK1rfR2MtQ6j2LClygzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
خبرنگار :
کشور های منطقه که مورد حمله ایران گرفتن آیا باهاتون تماس گرفتن و ارتباط گرفتن ؟؟
🇮🇱
نتانیاهو:
بیشتر از چیزی که فکر میکنی و بیشتر از چیزی که میتونم بگم اتفاق افتاده
.
⏺
خبرنگار:
هدفتون درباره حکومت چیه
.
🇮🇱
نتانیاهو:
خب هدف مشترک من و پرزیدنت ترامپ مشخصه اگه بتونیم تهدید ایران به طور جدی کاهش دهیم توافق های صلح زیادی انجام میشه
!
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/69287" target="_blank">📅 02:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69286">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZckPhrt-HkgR3fnIwNAa5YQ5fJBczjOl0I8eKUnMYPclUGKhfrzftr6-RVOX8JXRxsw9yoY_7dk6TMYluRHjcsN8zH0-D4lTQbBI_ymZvXETLcGF67ucenN7AxkG3ABPsiHRJYO-5YBks4sl30g0xI3GO5FzINSYsaKjHE5ruA7LoQi3klPoc8dB2W1d_RXqMLB05dRiaUpclAy_4XDJujRi6ZxEVdXGJyu6QvNrNyJrDLcTCFvFMad9OdwJuJcQdJMVoTWhMo98aNknydlgYQa8szgQilizx2Ypgw_7Oqsi3mZJHCMp1dIzAdFTwkIth92G5eNyxd-CcojN0botIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
امروز، «شورای صلح» به توافقی تاریخی برای خلع سلاح کامل حماس و تمامی دیگر گروه‌های مسلح در غزه دست یافت. این گامی عظیم به سوی صلح و امنیت پایدار است.
این توافق گامی حیاتی است تا غزه سرانجام تحت اداره یک دولت جدید فلسطینی قرار گیرد؛ دولتی که برای یاری رساندن به مردم فلسطین، همکاری نزدیکی با «شورای صلح» خواهد داشت. هم‌زمان، اسرائیل از امنیتی که شایسته آن است برخوردار خواهد شد و غزه دیگر به پایگاهی برای حملات تروریستی بدل نخواهد گشت.
این رویداد، نقطه عطفی بزرگ در اجرای «طرح ۲۰ ماده‌ای ترامپ» محسوب می‌شود. این توافق طی مراحلی با برنامه‌ریزی دقیق اجرا خواهد شد. هم‌زمان با تکمیل روند خلع سلاح، نیروهای اسرائیلی عقب‌نشینی خواهند کرد و «نیروی بین‌المللی ثبات‌بخش» با همکاری نیروی پلیس جدید فلسطین، مسئولیت تأمین امنیت غزه را برای ساکنان آن و همسایگانش بر عهده خواهد گرفت.
یک سال پیش، شاهد جنگی شدید و خونین، بحرانی انسانی و نگهداری گروگان‌ها در شرایط اسارتی بی‌رحمانه بودیم. ما به پیشرفت‌های تاریخی دست یافته‌ایم، هرچند هنوز کارهای بسیاری در پیش است.
می‌خواهم از میانجی‌ها — مصر، قطر و ترکیه — به خاطر تلاش‌های مهمشان و به‌ویژه از تیم فوق‌العاده‌ام که با تلاش‌های خستگی‌ناپذیر خود دستیابی به این موفقیت تاریخی را ممکن ساختند، تشکر کنم.
اجازه داده نخواهد شد تهدیدی که در ۷ اکتبر از سوی غزه سر برآورد، دوباره بازسازی شود!
بر اساس این توافق، غزه سرانجام در اختیار دولت جدید فلسطینی قرار خواهد گرفت که در خدمت مردم خود است.
این دستاورد شگفت‌انگیز را — که همگان دستیابی به آن را غیرممکن می‌دانستند — به همه تبریک می‌گویم!
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/69286" target="_blank">📅 02:04 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69284">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ODLVbuQXIuJfjcU__rUO3TXMIt4sa_LkF2hhDY9Osmjy2FYsEpv1C5wTKyHO_hTQzwHc34jGQU6l8xkRjd74NyhLamtjUmHXfIBDzYbitHWBCm4DbBVFsgHALgin6ppSuU36p-YjpLdCWn1RR6w3bqLEP3qU4-4_CzviZeMXU4sgereryv3b8L6sgfVpNXR23KX98T0E7VJjW17aOpA-nY9ey2VpSGI_QWY6PNp6Tja9_YdX1qromdl8jztBRjqHzeSpYGk_3yV7B6M4q0OFqcnpKXzwVIAY2eZi3Tddn_Qv-z7uxpl6569NdA-T4IiCs00dHMb8hGohAsvhIVPjeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad9bb4c4a.mp4?token=AMlvF8HX4Y611mAen-31LYf5NTt-bJPL0IpRZslrLwW9YvVRR6SJfkOPSWheOUwPhG5GST5RuyPLyM9MBdvCdUPS_OIcr-VrW1a2zliElephqoHPsAa-uthWw3m-wJXPE4K94_WEKwX6oOeWUg38s6Bj2mUasK-BJ9ISRZe8n9it_i0PjGv5VJMhNIVEFOJkuKzflQYtgyk_wZVM-bptSXQo7eNOh4UjtqtSSia-wKrsa4Ovi1urYoYANDUWXB3fM9amzxla64FOJiyR-rAPUHwL-MuFcu-6EwzpzAZ7V0dT9zXQ4wYHs1eYTblm5IsjsX4ce7Id7lyLWQh2ZMcXEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad9bb4c4a.mp4?token=AMlvF8HX4Y611mAen-31LYf5NTt-bJPL0IpRZslrLwW9YvVRR6SJfkOPSWheOUwPhG5GST5RuyPLyM9MBdvCdUPS_OIcr-VrW1a2zliElephqoHPsAa-uthWw3m-wJXPE4K94_WEKwX6oOeWUg38s6Bj2mUasK-BJ9ISRZe8n9it_i0PjGv5VJMhNIVEFOJkuKzflQYtgyk_wZVM-bptSXQo7eNOh4UjtqtSSia-wKrsa4Ovi1urYoYANDUWXB3fM9amzxla64FOJiyR-rAPUHwL-MuFcu-6EwzpzAZ7V0dT9zXQ4wYHs1eYTblm5IsjsX4ce7Id7lyLWQh2ZMcXEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیدار عجیب نتانیاهو با یک سناتور!
امروز نتانیاهو با جان فترمن دیدار کرد و طرف با شرتک نشیته بود و سرش کلا تو گوشی بود
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/69284" target="_blank">📅 01:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69283">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">عجب سکوتیه، موشکی راکتی چیزی نداریم؟
🙁
#hjAly‌</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/69283" target="_blank">📅 01:48 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69282">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromلیوه</strong></div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/69282" target="_blank">📅 01:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69281">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">عجب سکوتیه، موشکی راکتی چیزی نداریم؟
🙁
#hjAly‌</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/69281" target="_blank">📅 01:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69280">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">▶️
تیزر جدیدی از سینمایی Spider-Man: Brand New Day منتشر شده که دیدنش خالی از لطف نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/69280" target="_blank">📅 01:18 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69279">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dNT4sDnFPor-Jmpuj0E13JV0tLifZ7n7YnyXeG2N1D9SgMg54wN-Iu5sqNA415w0e5EzRVGZh_IZqTWnSoqjkF13cQI79mOg8emIP1CT_8cv5j0TQCrbGMZyfmA_KN4QaQyiL8aSOyEf2cqMO9MH0F2sqNjomLbA_Qn0Qs4OgeFOGZu64ioAAfIQU-dEa64S2NUzFJ67iW0m1dNeNGgMA0-eLFp5c2NySCwhfnrRwK3mi9xHD_JWwf7QPdBD9bH_0pXtL3YUco_FuIYZwdGqiFmd93-AjHL2LfkFm_ztWuy5lHCDHWo3kTOJyprw3S6pC1kwbh3Z-WT5b0TP3QkhSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قالیباف:
«آمریکا هر روز یه جنایت جدید انجام میده. حمله به خونه‌های مردم عادی توی جزیره قشم، ادامه همون جنایت‌هاییه که قبلاً توی لبنان و غزه انجام داده.
آمریکایی‌ها عادت دارن هر وقت توی میدان نبرد کم میارن، با ریختن خون آدم‌های بی‌گناه جبرانش کنن.
ولی بابت این کارشون، تاوان پس میدن.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/69279" target="_blank">📅 00:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69278">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cba260d124.mp4?token=g0roXWHzPVpFnDotd5H1BUcRgHUq6rQ72paf3JxalOqQGF1zAaEhk1pl9-vLOSFeWBo6WBZ7NSQiu38wgovYK1S_zWmWUUm8z2_GkTyP-52_QZ7fD0gz1vSdLJOQrySaNOAwJo7da2PtpDbGIxJ7PsV9EKTF3m9hsLzxlHgDDU4Gwwj4cY_H9YEMM24MFJuOXvYAL7U0GCNBSdYfQB4BChXNwmRB2nlKykMQDotb0x_oTY_eBTv1XUQHEwudooKqfA54VkLS25AhngO1mJLBWXFGkJZ-kKHwX_Eg0sT2VUNE6BP6tcKRdUsIhGSJOqWCiVcFoKWjIi-m-rcgUn9vhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cba260d124.mp4?token=g0roXWHzPVpFnDotd5H1BUcRgHUq6rQ72paf3JxalOqQGF1zAaEhk1pl9-vLOSFeWBo6WBZ7NSQiu38wgovYK1S_zWmWUUm8z2_GkTyP-52_QZ7fD0gz1vSdLJOQrySaNOAwJo7da2PtpDbGIxJ7PsV9EKTF3m9hsLzxlHgDDU4Gwwj4cY_H9YEMM24MFJuOXvYAL7U0GCNBSdYfQB4BChXNwmRB2nlKykMQDotb0x_oTY_eBTv1XUQHEwudooKqfA54VkLS25AhngO1mJLBWXFGkJZ-kKHwX_Eg0sT2VUNE6BP6tcKRdUsIhGSJOqWCiVcFoKWjIi-m-rcgUn9vhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
سنتکام:
یک فروند هواپیمای P-8 Poseidon(هواپیمای شناسایی تخصصی) نیروی دریایی ایالات متحده در حین گشت‌زنی در خاورمیانه، برای سوخت‌گیری به یک فروند هواپیمای KC-135 Stratotanker نیروی هوایی ایالات متحده نزدیک می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/69278" target="_blank">📅 00:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69277">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aZaFc0R6Cb8XdZ_Bgo-vykwMAx9RSCYHyuPUL8v556re5XYIVm2WhnHEugtYKnvzI14RMPR3mEmgv4sTdYKYaK8fFTf7mqYO-ChV_hRWck_yq3u300ZgVYCKX4A6wB7xZZOQW_zy_VJF2PR5PHVB7abH8_XbsJ2zUDJcXDU8QxRCAX4QoM50349aCUfVwbhL9HxBbmtP0qQxopIzTT2oC2NgUrLniOIXovsVDk9r90Kdt4FNTupHRk7oLqGfL6n50wOBDb_pSLuP-jb8Kru81SstUW3sdCiS0IwtVPjSUvPy2Jw9Zli9ntY3bKNcQUqfdxgJxqoznsHA7RAQ4o9F2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
آی‌24نیوز:
اسرائیل کاتس، وزیر دفاع اسرائیل، روز پنج‌شنبه به همراه ایال زامیر، رئیس ستاد کل ارتش، جلسه‌ای برای ارزیابی وضعیت امنیتی برگزار کرد.
در این جلسه، تصویری از وضعیت اطلاعاتی و عملیاتی، سطح آمادگی ارتش و طرح‌های عملیاتی برای سناریوهای گوناگون در عرصه‌های مختلف به کاتس ارائه شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69277" target="_blank">📅 23:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69276">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/89da715482.mp4?token=YJxGuICbKhJw34yMFaveEvpV6HsWsUZgy61LMKx0gVHmNUDXR-itR9p4lngc69a7v2SFR_KATHc_NVPZpotV7A-WrEtfRsWR8PLm498k_CUXeLeZDT1TmYzFI1qx4HEkywme6Pi8IXznFtLCtWVoM-Mh4hHjkkLIzpi4ZRQKyH9YAz9phUNZQQTSOTZ5bB8kFdaJXShRjd4kuuwb2yRWKoGvAkHlVYGM2OIi-MF-iPfnWNR7GOkfY0W9U8BqAePC-yZ6uIaXVc79nEBNQogd273fclhPDy8nNngXAZWVz_-if5oIqkpIm7gngHMrECEYJ_lb7Qbf96Q8QuMgv6RfEA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/89da715482.mp4?token=YJxGuICbKhJw34yMFaveEvpV6HsWsUZgy61LMKx0gVHmNUDXR-itR9p4lngc69a7v2SFR_KATHc_NVPZpotV7A-WrEtfRsWR8PLm498k_CUXeLeZDT1TmYzFI1qx4HEkywme6Pi8IXznFtLCtWVoM-Mh4hHjkkLIzpi4ZRQKyH9YAz9phUNZQQTSOTZ5bB8kFdaJXShRjd4kuuwb2yRWKoGvAkHlVYGM2OIi-MF-iPfnWNR7GOkfY0W9U8BqAePC-yZ6uIaXVc79nEBNQogd273fclhPDy8nNngXAZWVz_-if5oIqkpIm7gngHMrECEYJ_lb7Qbf96Q8QuMgv6RfEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چند روز پیش یه پسر بچه به اسم امیرحسین رو آورده بودن صداوسیما که اینجوری جواب سوال مجریا رو داد
:
مجری:
منو عروسیت دعوت میکنی؟
امیرحسین:
معلومه که نه
مجری:
کارشناس برنامه، خانم دکتر رو چی؟
امیرحسین:
فرقی نداره، اونم نه.
مجری:
مامانت چی؟ اونو که دیگه دعوت میکنی؟
امیرحسین:
وقتی زن بگیرم مامانمو میخوام چیکار
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/69276" target="_blank">📅 23:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69275">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/671ccf87ea.mp4?token=A-ixdZE7j57Mq1rDG8s7SexxWtyTroTrFGE7_FhGNgMTuJGk0NqJRSHmhRGR7jZGU78vJgOe9muGVnBDtYkQfI9Gzfa7fkNA4FjM8LITAxvqIpahuKg-PerybWplUUykkMtRgSAuuB4ylsjL5DFXXYslSiMyHVxhmDFi27-EU0mpkvjO9pueThDJoAWt9qzND7LOZfUCB4C6hWry94mifGmVaSYwrmLTLXKNF_vMmMKlAwhGBlPEkNawCnOolym4No_SX5lX5v5bBVCQ2S97WBUTCXbTHI4GBLQCvVqE3s3dqcklI7hkc1Uvllb-Tn1zVbZdcaZ0OiOG2iExvrABeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/671ccf87ea.mp4?token=A-ixdZE7j57Mq1rDG8s7SexxWtyTroTrFGE7_FhGNgMTuJGk0NqJRSHmhRGR7jZGU78vJgOe9muGVnBDtYkQfI9Gzfa7fkNA4FjM8LITAxvqIpahuKg-PerybWplUUykkMtRgSAuuB4ylsjL5DFXXYslSiMyHVxhmDFi27-EU0mpkvjO9pueThDJoAWt9qzND7LOZfUCB4C6hWry94mifGmVaSYwrmLTLXKNF_vMmMKlAwhGBlPEkNawCnOolym4No_SX5lX5v5bBVCQ2S97WBUTCXbTHI4GBLQCvVqE3s3dqcklI7hkc1Uvllb-Tn1zVbZdcaZ0OiOG2iExvrABeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نقدعلی، نماینده مجلس:
با وضعیت حجاب میخوایم چیکار کنیم؟ والله جوابی برای خدا نداریم.
یه نماینده مجلس به من گفت از درد بی‌حجابی هر شب تو خونه گریه میکنه و خواب و خوراک نداره
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69275" target="_blank">📅 23:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69274">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NvRcdVzfP3EYvHnAcIEfAR5-ZVqmBdepuC3J4BhEjq-P5tomRnNAc-4-YCjnED6EYt3rBy8K7CvFh6fJQhv0b6Fq_GEZIYqiX6eTtLskTYFE-Bka2KVV2BWSwGq_gpEg4H_bJSKf4PW4ci_QnN91V3-rDeDzbAE-K3o2n6YnXe8zP17KJRnA5xMkKP_8gSzCln3FPFdNyt0jYHHNSvNqS1kDY1lzEtulTnb76EeRW-agan3fmQdIKuxIJ0_6L-VRtpUt1gl4tSKHc34Uw-YTb9Tkk4zLoca5EPfw0mgY7bpAefRG4E_nJy0X5vsi3HB0R55tX_79nJZWUjUIu4ePsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعدام می‌کنید؟ به‌به چه کتلت های تر و تازه‌ای داریم امشب  #hjAly</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69274" target="_blank">📅 23:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69273">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b3fe31b5c.mp4?token=ESpWshazxF0XtRX3D4ET_Y-o6KnPRpcblGphqvzGUvhVN2e0a3hyw6txk6Yc4H-NoCM4R2K599BaWxao6rhwASaBN3xq9h_IgwQXVbUguG0DFSFUuHJreeBCQOFMy3arFEkSqqelQrVrVDpPq4hpchb8gYCqfjyhnb5rZqmq6nbv2H9RACbkxnRoAz59YMLc_HO1v4IwFyKM8Y_KKPenrgcfcMlcb0txcnM-5HZpoGu4BYUtF1RPbhq2R69azTShVEb3hKiIBx5uvP_AsvRXFUIB6Ozc6k5ouXNwSeYGSY8XZ-5WG36NSjYBSl8Fwp-wslz5waa4yEoY9BRSSR7Zhny3_n-iI82-04LWL6Ix3FCUTwucv0SPQggrz2r-4i5Kq07vbtjE35djHDMt8u-10eqdP8fMS1AK6IH_8RpK_M65CdiArjhuvPn-Fn4sr6glz3qBr07Q4aXCAqPjLszC75OiDPPxzS3oCdtmrm7dxlcbBVha6DTO2oZdDFXTpoDdh7HU-tnUqRHwQCnUr8lyLn63_fBxDwgGiJrpqQ0JQULuN3KHUNm2-SujQ4ndsU8zRo-HUTOeQYLQoEUomFzEyA0CPWsBkemoQ9sv6JAYnJ8mEW-HPjnVT3tQiyyrDakI9VmndpG6RYJfbiPMQYxOcml4i4PdDOcUwSmfLPyYNmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b3fe31b5c.mp4?token=ESpWshazxF0XtRX3D4ET_Y-o6KnPRpcblGphqvzGUvhVN2e0a3hyw6txk6Yc4H-NoCM4R2K599BaWxao6rhwASaBN3xq9h_IgwQXVbUguG0DFSFUuHJreeBCQOFMy3arFEkSqqelQrVrVDpPq4hpchb8gYCqfjyhnb5rZqmq6nbv2H9RACbkxnRoAz59YMLc_HO1v4IwFyKM8Y_KKPenrgcfcMlcb0txcnM-5HZpoGu4BYUtF1RPbhq2R69azTShVEb3hKiIBx5uvP_AsvRXFUIB6Ozc6k5ouXNwSeYGSY8XZ-5WG36NSjYBSl8Fwp-wslz5waa4yEoY9BRSSR7Zhny3_n-iI82-04LWL6Ix3FCUTwucv0SPQggrz2r-4i5Kq07vbtjE35djHDMt8u-10eqdP8fMS1AK6IH_8RpK_M65CdiArjhuvPn-Fn4sr6glz3qBr07Q4aXCAqPjLszC75OiDPPxzS3oCdtmrm7dxlcbBVha6DTO2oZdDFXTpoDdh7HU-tnUqRHwQCnUr8lyLn63_fBxDwgGiJrpqQ0JQULuN3KHUNm2-SujQ4ndsU8zRo-HUTOeQYLQoEUomFzEyA0CPWsBkemoQ9sv6JAYnJ8mEW-HPjnVT3tQiyyrDakI9VmndpG6RYJfbiPMQYxOcml4i4PdDOcUwSmfLPyYNmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کویتی‌پور، معروف‌ترین مداح دوران جنگ ایران و عراق، دیگه حتی مداحی گوش نمیده
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/69273" target="_blank">📅 22:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69272">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h4y5l2StV_uetsxOz-A6v2TnWHrEypRdnoMYqx4N428yWvK9BHgk1v7vkaKZ7SIyz9MIMGB7VFO2768_W37d-n80iGikZljNGNRGtxxfXuSfCTPNp7LzKYKiAK8P4rmmm-TWD1HI1dLzL__muGsbKHy6cLwwPznaSOyzHAH-TRQ2RWekgvvcgMq2DJRzrPsLtrdUFVrVYbBXpwuij3Bbv1vdtRRQT2BEkoitZ7i35obLuYDqYtkoyFM97rlz1skzpTVRdisfDYaioJtf8oARx38fhksGVVFvuN-K02fRxlIeRYDLNA6YTEkc7lR85Sim2aitOhJDybmDC6C4oqxSSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😄
مالک تلگرام ، پاول دورف :  روسیه به‌دلیل اینکه حاضر نشدم خواسته‌هایش برای نظارت گسترده و سانسور در تلگرام را بپذیرم، مرا در فهرست «تروریست‌ها» قرار داده است. طبق قوانین روسیه، من از «انتشار هرگونه اطلاعات در اینترنت» منع شده‌ام.  ظاهراً مقام‌های روسیه هنوز…</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69272" target="_blank">📅 21:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69271">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lfoo90hFiqaWaTS5_8zlUgqXbvxrLG0-XJqsrd__f7uaEIo9sGjlHA7lrGycoKMlbJrgne5P1KAvInrs0BVSF4ZlWtHHFOu1BaiweAG82v_xmknQviZH-UmOqXbBE8aqjZu8ZF7I-8rAo6XnpqZWH--MnxKf9qOJmlP45is4nfmx2m_g_37fNxEcYuknuSh854UyMbq8IvfrVKKFLPuKW6oHxpG3PoRP1a99f1-s9elH2qNoD_H82U5SyAA6Ett_qU4YYohCG1itdp2t5V_tPCf-OTt9ixJ14gKm8iCCeXcmrbLYBmjOMF-qH3v73-qzajX45kDRs36_B-bkpk3S8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😄
مالک تلگرام ، پاول دورف :
روسیه به‌دلیل اینکه حاضر نشدم خواسته‌هایش برای نظارت گسترده و سانسور در تلگرام را بپذیرم، مرا در فهرست «تروریست‌ها» قرار داده است.
طبق قوانین روسیه، من از «انتشار هرگونه اطلاعات در اینترنت» منع شده‌ام.
ظاهراً مقام‌های روسیه هنوز نمی‌دانند که چه کسی می‌تواند چه کسی را از اینترنت محروم کند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69271" target="_blank">📅 21:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69270">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7ad22e432.mp4?token=nc8_FLpHubgPu56t-vUVdg8gru0Ys6lKew18KoH6__TYS78s3plY3Q3HK2dl4DUf1NRwMIzqaG6YEohfungxd8LlvVdY0BN6j6qcmyyan7j69xmygfNzkVlTl_H_wGEtp1TQxiigyepB-gq-B1U3o-zvKQT-DhrYyI1Z8d6P2DZE85LK2o53KoHFeMJNswVPjzt5B5ytbW5RrQaaL7qtp8mEmdpZPB6Y1Wn-19n35Do6bC6wQcyJJFJydxO9oZXomDnQDm7auLPmfUL5K9gqukhuOe3WuAFPjHHxS_av-Df2_AfT89DWM4X-auxhzQdOdGtvzixftEnKbt7ESX4uYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7ad22e432.mp4?token=nc8_FLpHubgPu56t-vUVdg8gru0Ys6lKew18KoH6__TYS78s3plY3Q3HK2dl4DUf1NRwMIzqaG6YEohfungxd8LlvVdY0BN6j6qcmyyan7j69xmygfNzkVlTl_H_wGEtp1TQxiigyepB-gq-B1U3o-zvKQT-DhrYyI1Z8d6P2DZE85LK2o53KoHFeMJNswVPjzt5B5ytbW5RrQaaL7qtp8mEmdpZPB6Y1Wn-19n35Do6bC6wQcyJJFJydxO9oZXomDnQDm7auLPmfUL5K9gqukhuOe3WuAFPjHHxS_av-Df2_AfT89DWM4X-auxhzQdOdGtvzixftEnKbt7ESX4uYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔝
سنای آمریکا به طرح قطعنامه‌ای برای توقف عملیات نظامی علیه ایران، مگر با کسب مجوز از کنگره، رأی منفی داد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69270" target="_blank">📅 21:12 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69269">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64cd6ef9d4.mp4?token=NuDUvrfX_4BpM2TAa993vfpHZIfxOsdll-V-XmT7Rn9U6qLXGJzMxe5BtS5FHHpr_ZQf02GGeTTAbTJOqNGV7UI53C80hYS22stSeWQUobshmliQkiTW2KlLcCJai3n6fi9aR1vG5B2fdYFbRSGeq97Pir2xx7N4J5SlCO1yI4eYDhEwccZ55MfiiA1L3qiym1Gp3YE2lcEDBVfjif0mRPBaYK12fPIPl8SSeK0NEamBu2qQdRwJoXjeKCfvShX-XYgG6ze8RZZfXiX5-fyli3u8azjyS2xzTLK4DN-v8-uqn8neSdx6pv_kVLNDRna5c4CB6ZE9KK8xmuWvnkmHdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64cd6ef9d4.mp4?token=NuDUvrfX_4BpM2TAa993vfpHZIfxOsdll-V-XmT7Rn9U6qLXGJzMxe5BtS5FHHpr_ZQf02GGeTTAbTJOqNGV7UI53C80hYS22stSeWQUobshmliQkiTW2KlLcCJai3n6fi9aR1vG5B2fdYFbRSGeq97Pir2xx7N4J5SlCO1yI4eYDhEwccZ55MfiiA1L3qiym1Gp3YE2lcEDBVfjif0mRPBaYK12fPIPl8SSeK0NEamBu2qQdRwJoXjeKCfvShX-XYgG6ze8RZZfXiX5-fyli3u8azjyS2xzTLK4DN-v8-uqn8neSdx6pv_kVLNDRna5c4CB6ZE9KK8xmuWvnkmHdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
📚
عمران عباسی، عضو کمیسیون آموزش مجلس
:
قطعا تو مهرماه باز شدن مدارس رو نخواهیم داشت.
چون برگزاری آزمون‌ها تقریبا یک ماه تاخیر داشته.
حالا همه تلاش‌مون رو می‌کنیم که اول آبان یا تو خودِ آبان ماه مدارس رو باز کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69269" target="_blank">📅 20:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69268">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dca29ad7e.mp4?token=AEHEdP75TbZoJpHx8hZZoVjIIyhONjKg7S-I144JN8I733haV3MtC1ooau9x34pNhmXDcn-uBxstiptbvhmWcryTCm_pko4OYsjLAfCJx9WEGkCM8hoyRHCQ9CzdpOt4qQEZ3eSzbwkUoo0AqKB818hrppKXdrLBcONugcWUT_WxuirvNSBHxHeWcwhrtnfuITI6UAjKZ_8HwHQA6rvwrGfzp4S3grI9ukLgHKg3jh82OK3GBqNP79l8Mcq_FTYnurMLGE3OL-q41C8bhfcg0Fd5j3NHkLafqTYTKwqXdOeirhfVtLBbe12z8SdIK_vG_aDrJzD2TTO_9O3SSbnDCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dca29ad7e.mp4?token=AEHEdP75TbZoJpHx8hZZoVjIIyhONjKg7S-I144JN8I733haV3MtC1ooau9x34pNhmXDcn-uBxstiptbvhmWcryTCm_pko4OYsjLAfCJx9WEGkCM8hoyRHCQ9CzdpOt4qQEZ3eSzbwkUoo0AqKB818hrppKXdrLBcONugcWUT_WxuirvNSBHxHeWcwhrtnfuITI6UAjKZ_8HwHQA6rvwrGfzp4S3grI9ukLgHKg3jh82OK3GBqNP79l8Mcq_FTYnurMLGE3OL-q41C8bhfcg0Fd5j3NHkLafqTYTKwqXdOeirhfVtLBbe12z8SdIK_vG_aDrJzD2TTO_9O3SSbnDCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
حکومت از امروز یه طرحی رو شروع کرده که بتونه فضای مجازی رو به صورت کامل به دست بگیره؛
طبق این طرح؛ قراره بلاگرها، اینفلوئنسرها و بقیه فعالای فضای مجازی ثبت و ساماندهی بشن.
در عوض می‌تونن از مزایایی مثل بیمه استفاده کنن، اما از اون طرف هم قراره نظارت روی محتوایی که منتشر می‌کنن بیشتر بشه و هر کسی خارج از چارچوب قوانین جمهوری اسلامی فعالیت کنه، صفحش بسته و با برخورد قانونی روبه‌رو میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69268" target="_blank">📅 20:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69267">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46911d7dc4.mp4?token=d8UTW5s8zPVsCl5VYNlWksvwgNXVL98GyPTd96GLfkEXliIIJR5IM2nL2JJUp42tMGR3W3TAjVgMBITRqZpQlujAhqaBdBm6BuVN-LhdxbQZ9jq_tx3ui83HGjjp_wVf4CkAziV6G_9UbKfDZmaXtRax6FUQi5gmXHyRxvLD-ihW6OZ5JR_kFq2c2yq8gzQhzohpA1HPrnv8s_xmcZTko6icXJVlcgGeRd7HyRshCFYd2lBIJytnobZBu1PIGo2IWNcWx0g_ASBQeud5eNynfbLxH-iiqMoZndXRVFWCPk30Gvpv91b6JvbsCs93VoqZy59P01Df2jeaNhZfp3SCLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46911d7dc4.mp4?token=d8UTW5s8zPVsCl5VYNlWksvwgNXVL98GyPTd96GLfkEXliIIJR5IM2nL2JJUp42tMGR3W3TAjVgMBITRqZpQlujAhqaBdBm6BuVN-LhdxbQZ9jq_tx3ui83HGjjp_wVf4CkAziV6G_9UbKfDZmaXtRax6FUQi5gmXHyRxvLD-ihW6OZ5JR_kFq2c2yq8gzQhzohpA1HPrnv8s_xmcZTko6icXJVlcgGeRd7HyRshCFYd2lBIJytnobZBu1PIGo2IWNcWx0g_ASBQeud5eNynfbLxH-iiqMoZndXRVFWCPk30Gvpv91b6JvbsCs93VoqZy59P01Df2jeaNhZfp3SCLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
آفرود سواری هم تو ایران ممنوع شد؛سازمان منابع طبیعی:
از این به بعد هر کسی بدون مجوز یا خارج از مسیرهای مشخص وارد مناطق طبیعی بشه، باهاش برخورد می‌کنیم. اگه هم آفرود به‌عنوان یه ورزش به رسمیت شناخته بشه، براش دستورالعمل و چارچوب مشخص تعیین می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69267" target="_blank">📅 20:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69266">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acbbb58fbc.mp4?token=asUybxu1EgJrfN25tDdO_JMxCe7_TSsBpMGtHw8GsOmoeTcUmJx7L0P2VkWbOR0R-6NRdMvaie-Id8Aw4r2CRp4Ty7ImVL5F0kYb-oaeOTvAs5oaAkxycZYCApCZByT2BaUvapiVyCoKlWGSQ5ZTbc3GHdmOYyrD9smW7WT87JmWfbRYh-8Dq74RNnBfbNj8CH80T1uWgeNRuCpXkIfy89nUM97_Cc5LBMUtEQfSaTcM_wYi5WVGlWYjO45JBF6ZmXzlDWyKcbk1_hiP5DaGVFXG7iPMzCg-g-_xFgx94KFPgmuuPs6CaNcjgdm-HKAjLpzWDcabIddkDZ7nVpl_8AEl9SsHIK2CXp2zp2604AslT3acsY0u9dpZS6WzCvU80IE1BFx_KWv9rqu8xTYwjveyz5iw9Ak5sbUb7hzPe0mHl_U0Ey3WR_Put502GGv-8RFOIL_2NrgGkPSpF_psp7JHU_J-mmWZaXaILKSsG1M7GiwFCOJvSjSPjLjIGRf6W7vqf4AT3Ri41oJ072FiuH-cqVt6PCIV_dal-F_pmwmMbmNda8u1p6CnmJY_T8soopTGHdrtEJ-YipaXWKCxts7PWfoY_VtAj4-rhVuIxjfz3dhYL9AXieKMf1Af0Y5J5gH71cl5JbTiXEGgD3WZ1362CqF90o7LMaJsii9swPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acbbb58fbc.mp4?token=asUybxu1EgJrfN25tDdO_JMxCe7_TSsBpMGtHw8GsOmoeTcUmJx7L0P2VkWbOR0R-6NRdMvaie-Id8Aw4r2CRp4Ty7ImVL5F0kYb-oaeOTvAs5oaAkxycZYCApCZByT2BaUvapiVyCoKlWGSQ5ZTbc3GHdmOYyrD9smW7WT87JmWfbRYh-8Dq74RNnBfbNj8CH80T1uWgeNRuCpXkIfy89nUM97_Cc5LBMUtEQfSaTcM_wYi5WVGlWYjO45JBF6ZmXzlDWyKcbk1_hiP5DaGVFXG7iPMzCg-g-_xFgx94KFPgmuuPs6CaNcjgdm-HKAjLpzWDcabIddkDZ7nVpl_8AEl9SsHIK2CXp2zp2604AslT3acsY0u9dpZS6WzCvU80IE1BFx_KWv9rqu8xTYwjveyz5iw9Ak5sbUb7hzPe0mHl_U0Ey3WR_Put502GGv-8RFOIL_2NrgGkPSpF_psp7JHU_J-mmWZaXaILKSsG1M7GiwFCOJvSjSPjLjIGRf6W7vqf4AT3Ri41oJ072FiuH-cqVt6PCIV_dal-F_pmwmMbmNda8u1p6CnmJY_T8soopTGHdrtEJ-YipaXWKCxts7PWfoY_VtAj4-rhVuIxjfz3dhYL9AXieKMf1Af0Y5J5gH71cl5JbTiXEGgD3WZ1362CqF90o7LMaJsii9swPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زنده‌یاد مانوک خدابخشیان:
"اگر رژیم مذاکره کنه باخته و اگر مذاکره نکنه هم باخته"
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69266" target="_blank">📅 19:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69265">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cce71ed1d1.mp4?token=v2_8Vpf2hSR9LdK_rZTOwcP1bOfNCHb15nU-fkO6U541RB_qDRdY85XVv6XBVultH9JmZyTAfqc2MRkiThFY5cKzEEJsfbh90sBIvDIrsx2OTnGM33LmWIQWu_4HPZy-ibv1xnCWFh2bY7ln7z0yKF20Qfr6cZ5cAVXu9ZNHEtU-zu9NkevP3Do-BI5taqFHfQsoyhj093Us5DN2vbpjMQyR3FjF_DuR3tJhSbp6YvuVSEY11Wicx5GzuK5zy8y_XETjc1sMZGXpGoPiMIADvT8RKDUZrHSAJVMvIP_o5sHGS0kVCwf-7Xpk6GvP8xEA7DVCSKGPouQMm3uy6MHCFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cce71ed1d1.mp4?token=v2_8Vpf2hSR9LdK_rZTOwcP1bOfNCHb15nU-fkO6U541RB_qDRdY85XVv6XBVultH9JmZyTAfqc2MRkiThFY5cKzEEJsfbh90sBIvDIrsx2OTnGM33LmWIQWu_4HPZy-ibv1xnCWFh2bY7ln7z0yKF20Qfr6cZ5cAVXu9ZNHEtU-zu9NkevP3Do-BI5taqFHfQsoyhj093Us5DN2vbpjMQyR3FjF_DuR3tJhSbp6YvuVSEY11Wicx5GzuK5zy8y_XETjc1sMZGXpGoPiMIADvT8RKDUZrHSAJVMvIP_o5sHGS0kVCwf-7Xpk6GvP8xEA7DVCSKGPouQMm3uy6MHCFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⁉️
سنتکام:در ساعات گذشته، رسانه‌های دولتی ایران به انتشار ادعاهای نادرست سپاه پاسداران انقلاب اسلامی (IRGC) ادامه داده‌اند؛به‌ویژه سه مورد زیر:
❌
ادعای اول: سپاه پاسداران (بار دیگر) مدعی است که مسیرهای آزاد و باز در تنگه هرمز برای کشتی‌های تجاری خطرناک هستند.
✔️
واقعیت: خطرات فوری که کشتی‌های تجاری و خدمه غیرنظامی آن‌ها را تهدید می‌کند، ناشی از تهدیدهای لفظی و تلاش‌های سپاه برای انجام حمله است.
❌
ادعای دوم: سپاه پاسداران مدعی است که سه جنگنده رادارگریز اف-۳۵ (F-35) و سه فروند هواپیمای دیگرِ ایالات متحده در جریان حمله اخیر ایران به یک پایگاه هوایی آمریکا منهدم شده‌اند.
✔️
واقعیت: هیچ‌یک از هواپیماهای ایالات متحده در تلاش‌های اخیر ایران برای حمله، منهدم یا دچار آسیب نشده‌اند. تمامی موشک‌ها و پهپادها رهگیری شدند یا به مناطق هدف‌گذاری‌شده نرسیدند.
❌
ادعای سوم: رسانه‌های دولتی ایران گزارش می‌دهند که یک نفتکش تجاری به نام «ام‌تی نورا» (M/T Nora) موفق شده است محاصره ایالات متحده را بشکند.
✔️
واقعیت: این کشتی تجاری موفق به شکستن محاصره مستحکم (دیوار فولادی) ایالات متحده نشده است. بیش از ۲۰ ناو جنگی، صدها هواپیما و هزاران نیروی نظامی آمریکا همچنان هوشیارانه به اجرای کامل این محاصره ادامه می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69265" target="_blank">📅 19:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69264">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/906e47e12d.mp4?token=QMM01Y0QRfMpjidmafnPQK_yH_-rfbi8YPHSbmLRnLNQW-xnEtW8Ba1Pm2Fgm33Ce1NEEY3yoNY6iqpaHtExGvmrkwQAFjyq4Gt5M54E03chHDE_OLwCg3vyHU2-c0tyL6Y612cvnuaudIG-UfW71ykwLWaWgPzsLQMgkVNqfe4CluNBzOyMX_BtIXFQ8ou-bmhfqaBiRH4eXjyYA1A1tUeHNFLzoly6UijiZXTJd1MzHVc59UzB-NLf4NPm_dpZzz6WR8kFkIKO1lFyYBEwnSpESdrcA8VqwsyoQ6VBchCGWJR6zT6MwZvxWXGYqIwa5EleIpb7MTRaxTaR75hhmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/906e47e12d.mp4?token=QMM01Y0QRfMpjidmafnPQK_yH_-rfbi8YPHSbmLRnLNQW-xnEtW8Ba1Pm2Fgm33Ce1NEEY3yoNY6iqpaHtExGvmrkwQAFjyq4Gt5M54E03chHDE_OLwCg3vyHU2-c0tyL6Y612cvnuaudIG-UfW71ykwLWaWgPzsLQMgkVNqfe4CluNBzOyMX_BtIXFQ8ou-bmhfqaBiRH4eXjyYA1A1tUeHNFLzoly6UijiZXTJd1MzHVc59UzB-NLf4NPm_dpZzz6WR8kFkIKO1lFyYBEwnSpESdrcA8VqwsyoQ6VBchCGWJR6zT6MwZvxWXGYqIwa5EleIpb7MTRaxTaR75hhmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه پسر جوون ایرانی رفت پشت فرمون ماشینش ی خر گذاشته رانندگی کنه خودشم داره از رانندگی خره فیلم‌ میگیره
😳
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69264" target="_blank">📅 18:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69263">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
انفجارهایی در صنعا، پایتخت یمن رخ داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69263" target="_blank">📅 18:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69262">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rDPPMlXo559SDrWayiNR5GcJYRDroXEgWq5FA9k7V3RgHuxEzByJdxCDAujtpQ7YnnVUCGBxlgSp6Vq8OhNliX_A81wn-x9_2fdg5TlVbfllSIbSV17IXYKFh23NmFy67JP4QCbQXBIv_ZaAvNBGATOLnfH4OSTZxApqXyOvKjupI7H8xbNwx4V24yi1poMoODdrOJ0H8AeKu-cmjJpPSxTvGSEoyxthR1_oB1v0STdUKNooFHwcs2oTbFiBKbsIedZVWccggBVaPFJAe4EpvzN3b2qe-rAWADKX7V1fTX9_6OMUkeg8QEWWArnOAEg3kc9Mnwu7EA6L9avuJ3izxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سه تا از تروریستای مفعول حشد‌الشعبی که در حمله مشترک آمریکا و عربستان به عراق کشته شدن!
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/69262" target="_blank">📅 17:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69261">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X3XHJ6_XfUe_yARVeybhWEBC3XI8M0xPRQw3Vlip1qiE3a8FxFnvez8vQb-Q48O2gCAf9TPaMC0z8MVT865ssl6LpWZlT384dsK-IUyWMhRrew-c_pxZYfcaPFQ1BqnXJM2Wlz39UEVW6mpspBEooFZjEuSSVSkfsfpsURNBtxMEIaC3_UYU5CTyX_qAOPKZL8jKdaFKxsNgkg_TEDTUtSA76QAxvs4wSp3HJghch3qP99klohrnPG7nZgd1o7_jwqQWrBO3TumkwpOr7J7N88F8OUi7dnBxDG3glzV3fWC1X7xQ3nNO1EkAsb7bpqAd4fOIStfg7HrGdraesX4bcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
روابط عمومی سپاه پاسداران؛اطلاعیه شماره ۵۶:
دو آشیانه پهپادی و یک مخزن سوخت هواپیما و بالگردهای نظامی در پایگاه علی السالم به آتش کشیده و منهدم شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69261" target="_blank">📅 17:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69260">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/262bb95a39.mp4?token=UlnaVYT_FYvCpsdH5zK7zIrBgNKG6xJ7kaNUMXdgMMELkBxdmOeHTIWc5qOKgZNO694Bjv1vnwUSHK4jMzgq4qfAm0PpQXrJZRImagqxfIPub5P_dhYeENJnKYuNxgF1ppLHMbrU_owzKBFA8_e76UUCL1qpC31CVnxsOSpcwM90R7w6j74v4THfTzAFus9kTJk0mKxodHgy5N_k7i0oBtFLvDIuDKUm78dJ2jL5NYWeOntqugRAjNFTzUXSKBTvhQ2dVX4E9S7msAyHO6YQ7lKJ8oZbpjVuzm5BE6mJzExpGg7J4k0kpdWQPjwllqhhOeVbXqivI-qiUhFAyO34fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/262bb95a39.mp4?token=UlnaVYT_FYvCpsdH5zK7zIrBgNKG6xJ7kaNUMXdgMMELkBxdmOeHTIWc5qOKgZNO694Bjv1vnwUSHK4jMzgq4qfAm0PpQXrJZRImagqxfIPub5P_dhYeENJnKYuNxgF1ppLHMbrU_owzKBFA8_e76UUCL1qpC31CVnxsOSpcwM90R7w6j74v4THfTzAFus9kTJk0mKxodHgy5N_k7i0oBtFLvDIuDKUm78dJ2jL5NYWeOntqugRAjNFTzUXSKBTvhQ2dVX4E9S7msAyHO6YQ7lKJ8oZbpjVuzm5BE6mJzExpGg7J4k0kpdWQPjwllqhhOeVbXqivI-qiUhFAyO34fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدویی از لحظه دستگیریِ نوید زیادخان قره‌داغی وسط خیابون بعد از شلیک دو گلوله به پا؛ این همون شخصیه که تو لایو دخترارو کتک می‌زد و...
⚠️
‌ ‌ ‌
حاوی خون و خون‌ریزی
🔗
‌
مشاهده ویدیوی کامل بازداشت
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69260" target="_blank">📅 17:24 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69257">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cea20ae2a1.mp4?token=mhro6SatBv19ykwafZWewC__rIyvDdaA_nXQjMc7qFoGxUL-HfYoQXZy3hd0CqcM9zMq3W_vulqcW49t_7C9gmBKvASaDyywQ8LDL9DgH9DO-FJkDnK_2pC6bYvMPo30qJk_qfnw1CcZSnvG8Cydj4jDXq53PGNgWWOYeijZYsj4Mc7k2F3qL1ryH87achi8L-ItEwQrkVryVCCU2H8GBP-GKxUqYChh9-f3Rmy6ic6F8G26nSXmZ858QDVAN1GXKZDbAA-Tax4IglOTPBPTlPJiwsLiIg12MpwPIC8uCqsNC7ZmH-JMTPBvTVEN-mDYzOOH-tPF-IIAOe96jXmEkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cea20ae2a1.mp4?token=mhro6SatBv19ykwafZWewC__rIyvDdaA_nXQjMc7qFoGxUL-HfYoQXZy3hd0CqcM9zMq3W_vulqcW49t_7C9gmBKvASaDyywQ8LDL9DgH9DO-FJkDnK_2pC6bYvMPo30qJk_qfnw1CcZSnvG8Cydj4jDXq53PGNgWWOYeijZYsj4Mc7k2F3qL1ryH87achi8L-ItEwQrkVryVCCU2H8GBP-GKxUqYChh9-f3Rmy6ic6F8G26nSXmZ858QDVAN1GXKZDbAA-Tax4IglOTPBPTlPJiwsLiIg12MpwPIC8uCqsNC7ZmH-JMTPBvTVEN-mDYzOOH-tPF-IIAOe96jXmEkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
حملات شبانه سنگین روسیه به کی‌یف، پایتخت اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/69257" target="_blank">📅 17:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69256">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d31a669dbb.mp4?token=qxFrA2d3fYqaZfYIn3kJs80uS4LQCit3htqv89kVsYtVwXmuiRWBzpU0D0I8D7i8_aVILyhpy7kmZo4q7kTUvkwSwmKVl7vKVg40mgUozGbFQwxadyqzny_u1G1zhQfB-M0iXP7nNXEk2-ymesf3yxSRuIcJ2DWyu-uct6yyQPIsXtRpfpYJcaNxDwqHTPb6jsEN6bYP_pYgMjsSQBfxAdmYIdEwpPSR11sVSVKEb10JCyrfV5Ms1NuTe0owGKh5mZtx9EHoBsgcvmjO-Y6ZqH4XscH4cz4Lw-_yU7MMQH3_YVty_zkG1-uu8P7cZ3cFpbzkHb5ilHKc8LMBSsZGCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d31a669dbb.mp4?token=qxFrA2d3fYqaZfYIn3kJs80uS4LQCit3htqv89kVsYtVwXmuiRWBzpU0D0I8D7i8_aVILyhpy7kmZo4q7kTUvkwSwmKVl7vKVg40mgUozGbFQwxadyqzny_u1G1zhQfB-M0iXP7nNXEk2-ymesf3yxSRuIcJ2DWyu-uct6yyQPIsXtRpfpYJcaNxDwqHTPb6jsEN6bYP_pYgMjsSQBfxAdmYIdEwpPSR11sVSVKEb10JCyrfV5Ms1NuTe0owGKh5mZtx9EHoBsgcvmjO-Y6ZqH4XscH4cz4Lw-_yU7MMQH3_YVty_zkG1-uu8P7cZ3cFpbzkHb5ilHKc8LMBSsZGCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
صبح امروز ارتش آمریکا به یک پایگاه پدافند هوایی سپاه‌پاسداران در اهواز حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69256" target="_blank">📅 16:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69255">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21d6f2f438.mp4?token=qUtx4kng4p3v41VKkatnYb5aNc_VqrzRorNj5Q59ts_eZZW-TL8NK_kiil1gkHC8W_oL1LU1TXZdAzW66AhHgi9tjgTxuyZQlyvabyO9VcJqpKJ5i4c5TOfWwnVRv2UjdPsfpnR8HpN_Yxkp02hw_B9CHh6sfZGL0pxx6EgYzBeRpfbRIq1s6yTSkMICAGywotdPU_baH65CezepG9zUUDh_mVOsf1qlHjCvGFfn1S1NerESU3hiT4L30CHHjYxJniLwWHV6WmCoyO1hT4T35V_HffhEIV4l9vIV2hp3DKewuQjP1l4a8eSAylRd9wf21wssrlmJMvpPJujPUud3zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21d6f2f438.mp4?token=qUtx4kng4p3v41VKkatnYb5aNc_VqrzRorNj5Q59ts_eZZW-TL8NK_kiil1gkHC8W_oL1LU1TXZdAzW66AhHgi9tjgTxuyZQlyvabyO9VcJqpKJ5i4c5TOfWwnVRv2UjdPsfpnR8HpN_Yxkp02hw_B9CHh6sfZGL0pxx6EgYzBeRpfbRIq1s6yTSkMICAGywotdPU_baH65CezepG9zUUDh_mVOsf1qlHjCvGFfn1S1NerESU3hiT4L30CHHjYxJniLwWHV6WmCoyO1hT4T35V_HffhEIV4l9vIV2hp3DKewuQjP1l4a8eSAylRd9wf21wssrlmJMvpPJujPUud3zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدویی از لحظه دستگیریِ نوید زیادخان قره‌داغی حرومزاده چهل پدر وسط خیابون:
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/69255" target="_blank">📅 15:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69254">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1666d9190.mp4?token=HNGnWVRuwV0MpccDptwP1kkBTRNIrYmHkA3RzkqMe7C7NzFySAvNLKL3BmR5vdbDaoWARXWOOKD0d7iiU-JgH70yklVoWRUGL4sQaCBnEFzx-qPfoNCb0XcZLTrMEfglXrtFtmfcCs6okfpNn1t3SVFz4Sl61BLAr6ajj1sYUW605Djrm_GHZop6L0tWstBj0wJvSo1ku4UhbfT7b9HyZ6SAOW-v6OKjPBEpOAm0dAjBtNpU6_ZMPramRJVNEXJaUAFlXmvaZXrL-pKtdW7a-FJpzoI4nwbu5FsS1IB8xhEvHKmEot8ep7HWaT-rO-VkjHAy4gj8Ire8AEDCSHBfUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1666d9190.mp4?token=HNGnWVRuwV0MpccDptwP1kkBTRNIrYmHkA3RzkqMe7C7NzFySAvNLKL3BmR5vdbDaoWARXWOOKD0d7iiU-JgH70yklVoWRUGL4sQaCBnEFzx-qPfoNCb0XcZLTrMEfglXrtFtmfcCs6okfpNn1t3SVFz4Sl61BLAr6ajj1sYUW605Djrm_GHZop6L0tWstBj0wJvSo1ku4UhbfT7b9HyZ6SAOW-v6OKjPBEpOAm0dAjBtNpU6_ZMPramRJVNEXJaUAFlXmvaZXrL-pKtdW7a-FJpzoI4nwbu5FsS1IB8xhEvHKmEot8ep7HWaT-rO-VkjHAy4gj8Ire8AEDCSHBfUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت صداوسیما بعد از هر حمله آمریکا
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69254" target="_blank">📅 15:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69253">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">‼️
🇨🇳
🇮🇷
رویترز:به گفته منابع، ایران ظرف چند هفته آینده سامانه‌های موشکی دوش‌پرتاب چینی دریافت خواهد کرد.  ۲۹ ژوئیه (رویترز) - سه منبع آگاه از این قرارداد به رویترز گفتند که انتظار می‌رود ایران ظرف چند هفته آینده، نخستین محموله از مجموع ۴۰۰ دستگاه پرتابگر موشک…</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69253" target="_blank">📅 15:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69251">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ImcUqZa2-MqiMt3JSJfzc9VGExD8JFFee1zi3nHUHMtuFHDeBXiZ_LiyBgVeGs90jgmBoEl1XV7_0WyR-QkOd_MZjRgbVjn5Z1xJhcpUpTkhjQkdlU-J2PDzLQSubiGtjGiP26sUO09tXoe8Btl2ikGUlseelLsyv3Za5GG2sWWenKiMcgr3-n-G5Zv9-VCLwiRGUPiNQ5j6EiMNwZbDbhCkv0UQ7gprl5Ut01vrpXsnM5iZpUkACWRG2CcrQw469zsxlXIozjbzclypG-TXJ6xTi1fJIyICul1zVI8eYoZwOxnlS2rUz6LISHqGEppoU2y0B7tR6QwYt6HnOnoWuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8b887c1d39.mp4?token=W-iuqv7s52ZTmJqWq7Jzh5bfxwPcrzyVuVY1EP_T_lhib7hcf8OWMQKQYWIRNYlD9wU4pizzs_SEYI3WB8Lns4zNBGQYSNy6cuRmJcMz45Qa1B2G0r29ZzEGnqtvHljbWH91H0r-DVowJu0y8cMRZGYiNkaNjh6wNwKbsUhPFhHPA5Yfxpwdx93GHjaazJ_GvvmSheVhneuBkH4gyKJfDJ-8luaf6dkNpYodGX4m-0Gl9fhA9AyEBH7-jthGjzMdtV9tU2SPzuwJ9zerO9QePHpwB_kALa1rzHbaMn89BLXs4b2fd-qhfrk8f67i_EqJmUDZ_tw9h0BN2mm2SNIalQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8b887c1d39.mp4?token=W-iuqv7s52ZTmJqWq7Jzh5bfxwPcrzyVuVY1EP_T_lhib7hcf8OWMQKQYWIRNYlD9wU4pizzs_SEYI3WB8Lns4zNBGQYSNy6cuRmJcMz45Qa1B2G0r29ZzEGnqtvHljbWH91H0r-DVowJu0y8cMRZGYiNkaNjh6wNwKbsUhPFhHPA5Yfxpwdx93GHjaazJ_GvvmSheVhneuBkH4gyKJfDJ-8luaf6dkNpYodGX4m-0Gl9fhA9AyEBH7-jthGjzMdtV9tU2SPzuwJ9zerO9QePHpwB_kALa1rzHbaMn89BLXs4b2fd-qhfrk8f67i_EqJmUDZ_tw9h0BN2mm2SNIalQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مادر جاوید‌نام ابوالفضل سپاهی، که توی میدان علیخانی اصفهان اعدام شد:
خطاب به یه نفر به اسم هادی: بگم برات که تیر زده بودن تو پای ابوالفضل؟ بگم برات که زیر چشماشو با فندک اتمی سوزونده بودن؟
بگم برات که ۲۰ روز بهش آب ندادن؟ بگم برات که فکشو شکسته بودن؟ بگم برات که دماغشو له کرده بودن و آویزون شده بود؟
هنوزم تحمل شنیدنشو داری که بگم برات...؟
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69251" target="_blank">📅 14:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69250">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🇮🇷
سپاه‌پاسداران:
تخریب کامل سه فروند هواپیمای اف 35 و ورود خسارت سنگین به سه فروند دیگر در الازرق در پاسخ به جنایت دشمن آمریکایی در قشم.
همچنین چند افسر و کادر فنی و تعمیرات دشمن نیز در این حمله کشته شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69250" target="_blank">📅 14:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69249">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/daa6076311.mp4?token=Mt70o-u7rHmUSA0beXdv0ScBcFIRAeM5ZboVgghvJKDfHe8Yy1hn96fLVa_EtQ67o5PTkvk6AbOYEGEIqnCOEOxjTdM1VwnrKdwQ-7WyZ_NRyVgbjHSro_ThbDki3rR7j1dtA6XQn2VDQr5stpYW4qZkb8k8PehJCmgZ1k4TdQUHeRqtu63imf0DRBwAKAA2qqeLhVi_6bswVHXRkzirQizDpO4UsjN3xCSzAexyAR7teNEeoLeziDS6zprDnkkpAIB_jdiAUOUUqbnc2XioJB69oApamMOJyQWDVTJ55JrGhE2I_ZPl26PIml1oef2vYrektYdem1C4T9VcZve8Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/daa6076311.mp4?token=Mt70o-u7rHmUSA0beXdv0ScBcFIRAeM5ZboVgghvJKDfHe8Yy1hn96fLVa_EtQ67o5PTkvk6AbOYEGEIqnCOEOxjTdM1VwnrKdwQ-7WyZ_NRyVgbjHSro_ThbDki3rR7j1dtA6XQn2VDQr5stpYW4qZkb8k8PehJCmgZ1k4TdQUHeRqtu63imf0DRBwAKAA2qqeLhVi_6bswVHXRkzirQizDpO4UsjN3xCSzAexyAR7teNEeoLeziDS6zprDnkkpAIB_jdiAUOUUqbnc2XioJB69oApamMOJyQWDVTJ55JrGhE2I_ZPl26PIml1oef2vYrektYdem1C4T9VcZve8Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فرود دیدنی یک F/A-18 Hornet بر روی ناو هواپیمابر.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/69249" target="_blank">📅 14:14 · 08 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
