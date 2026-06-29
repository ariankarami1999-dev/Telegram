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
<img src="https://cdn4.telesco.pe/file/AKt28UnJt5xTbRES830YgA0WAgEBAI6smTjlp4tuB_CuCGni2LhusWk8gxoBNEVtePcwOgkCrz4O6fdfo-5r7FRyRX_BJwLRXmGo5zD_gPWJ3bXnzhplwqwEMtkIJtN3PUTnfXThLgu1z5DT-ca9E9z-Snb0Q-WVfBame7CntBNHZg3jNRtsiAMUSnTQSHPiEnUEgUrcBLqmPC1K_fyp9mXutzQI4mIG2nCwxVOTmJOeFjW8HLdyTitjueUYpsqG8KdbtY5-hEZK3IJXP_AIJA_hFI4ySiNPhOUpbG9TUIH_3Wf-yudq97NqyachrH_nOnLLz8fJJEr3EAfXTUS2DQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 188K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-08 22:51:11</div>
<hr>

<div class="tg-post" id="msg-79055">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">امشب ژاپن کل دنیا را سوپرایز خواهد کرد  @Funhiphop | Farid</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/funhiphop/79055" target="_blank">📅 22:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79054">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">برزیل برد و رفت مرحله بعدی.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/funhiphop/79054" target="_blank">📅 22:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79053">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">مردان سرزمین قهوه چیه کصکش
😂
😂
😂</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/funhiphop/79053" target="_blank">📅 22:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79052">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">خارکسه چه لایی زد</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/funhiphop/79052" target="_blank">📅 21:50 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79051">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">وینی زد تیر</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/funhiphop/79051" target="_blank">📅 21:50 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79050">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">کاسمیرو زد</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/funhiphop/79050" target="_blank">📅 21:48 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79049">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">دیس ایز برازیل</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/funhiphop/79049" target="_blank">📅 21:47 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79048">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">گللللللللللللل</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/funhiphop/79048" target="_blank">📅 21:47 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79047">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">فقط باید برزیلی باشی که این موقعیتو برینی</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/funhiphop/79047" target="_blank">📅 21:45 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79046">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">چه گوهی خوردم رو برزیل بستم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/funhiphop/79046" target="_blank">📅 21:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79045">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">فک کنم اینم عموش آفریقاییه</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/funhiphop/79045" target="_blank">📅 21:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79044">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">گلر ژاپن چرا سیاهه</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/funhiphop/79044" target="_blank">📅 21:24 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79043">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">جدی باخت ژاپن به قلعه نویی عجیب ترین اتفاق ۲۰ سال اخیر فوتباله
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/funhiphop/79043" target="_blank">📅 21:22 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79042">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ژاپنیا همون عزیزان افغانی هستن که مهاجرت کردن به شرق آسیا
پس رگ و ریشه ی آریایی دارن زنده باد کوروش کبیر
🔥
🔥
#sajat</div>
<div class="tg-footer">👁️ 7.38K · <a href="https://t.me/funhiphop/79042" target="_blank">📅 21:14 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79040">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">گلر ژاپن چرا سیاهه</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/funhiphop/79040" target="_blank">📅 21:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79038">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">امشب زوج سوباسا و کاکرو کار برزیل رو تموم میکنن
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/funhiphop/79038" target="_blank">📅 20:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79037">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IdaPiid_9O1018EGI0icta4ekEmVM2jP8U_rwg6eKEYsOkwmPLkE0MLdIJZ6gOcrjBAIFb2f9eLkd-7CSodXQ4Hk2EBynu3vGByH74QDoxvaE1jx12djeMtfdA6b6khwoW6jSbGdayf729zdBIDY5JcpzxPwYfDHByCeb_oeFQ3_0fm8lgeN8alYyy-9PrI7WTaBFdIsWXV6lK44J5MWW2yxIeo_LwzM-V3VlwtAGbEWbu4NBnY9HmzlUh7-k96nEgxl4jY6KkkC9XigFPTVha4N8kFXcFQLZBPW3-19biMGG2XNycP7d6EZMc6FMrgfGCspyrrn-fOkFC_SakpD1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون موقع که ما به توماج صالحی فحش میدادیم امثال این آدم به ما میگفتن شما وصلید و فلانید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/funhiphop/79037" target="_blank">📅 19:48 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79035">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L5gdqIIIX1Na3A3UQW6gJC-DsjB71TV9bpuyoVX6Ry5wfjmuGS-lHc1fTEuLegQzZst9uYNNJ3STmUwG9zAyuF5WD1RA3b-icdITus8yR_wh02cgHzWNoS0SP8ihI9vB2cDxAE_KcDufbPcuXkgyk1uZrK_aEeU1YJW2Qd7Affy6CpiKkUsJIsiSPLu2vtZkUCHHezi8iafyTIIylRNvZ3HuSge1iWne-yoqbNSy1vbub2EUxwtbutypI3W3NF6r1LOeY7lbvDvOp4ADwXxwcLc8pKRgFeorR6n9LZ0z9cAwKNxYft87paYk91MqJTF9e1I-Xnb0XWZkxlccUgBwqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lozXHQH6h5glx6C7GOeazwFKo9saeRhe5PKW3exMThkv7lSu9_ijYxp_SLjs3z_9AUO6SqcFdwEIJRZD7kRK8kllsZ4ggjf-yKe9La0L6gmO3EvTkK2_XtskEr86CBc-jwlprrnZE8omjZbzXU3qpj5Pgdr3qEH23NtoGgROyD8tmZRK2qyv4LGtNeVqfAhnYy3NeZOlp8TB2Esnmz4ZLM7gdXjJ3GfqizvgUQwsOqWCb304ZUJFZT7jDi2QSkClL9UiFhejsKVxRPefFLp8fTmWKvaN87iIDMOaVc7J2rfqiDclGxV7hFh-AmPCQ8sWcyah2HlwxxgbijgRxcF41g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بیلی ایلیش رو به پسر ایرانی وقتی تو کامنتا چنلا یه پیامو کپی میکنه و ترتیب میره:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/funhiphop/79035" target="_blank">📅 19:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79034">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HmKnMnEiwV_XeKAP6AS7Cn5GE5qyNgVBii8tL01Gr8QKbOlzox6_bD4ZCo7WzeibjAECmnnJShp9yOzWype2h15pG7uFPASIYCTH_uYqFxj3CegrzQcoMUbZMmpTv1qUlLK3voN5bEOqBYllEYvc9tJXg8WBm17c4u0-e-coirAjBx4hyF7vv6yj5XHSVLvUDJVJO-VT-Ipa2DeWGj3JwUaIq8ZbKrD4N2w3N7kYaLZk1ZITGdlbs7lVolRDrQIrp38WhocisWn5SgJpfZ8fbJYRwIr3sjGBgM3JmbtfTH5d3QOk-IcEcus_QzdUu9N64AcGStPPWucNcvZkVWvP8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یادی کنیم از روزی که دمبله بعد بازی مسی رو لخت کرد.
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/funhiphop/79034" target="_blank">📅 18:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79033">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">جام جهانی را با بری بت  تجربه کنید
🔥
🔴</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/funhiphop/79033" target="_blank">📅 18:45 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79032">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/niULGSzNaqOEssEhktMw8ddOHcbC_b-5GPZuTNVnVhOmTO6wUycwHRz8bZ6ENP4sbiWfcK6Uz8c1xXLldjczNUWUGRjUYGz7FsqPczbKlKWDgXS5I_FhvX8_hAbt7tGyR-suyDfwWOfHq4wp_pvdTSyJS0Cdpl02wHLYmpXzVt1n9ekO7mVJThnFUvquDbyWFGJ8WsSlgyawsI4dxT3xNUxeN6HGO5_ExiNWzVlCWbGge5upfmi-eGHzNEzQbnvu6Cf84AFggRrwUdbQpMlCKhAHzs00t9qPUfaPuDZBTpaH_R9clTfdKTFBrfYwdD8rD2RU7dxbOLaBJed0nxToJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📈
دریافت
0️⃣
1️⃣
🔣
شارژ اضافه بر روی واریزی‌های ارز دیجیتال ویژه جام جهانی
📊
💻
در سایت بری بت وارد حساب کاربری خود شوید.
💰
از روش ارز دیجیتال اقدام به شارژ نمایید.
🔍
بر روی واریزی‌های ارز دیجیتال تا 10٪ شارژ اضافه دریافت نمایید.
🚀
افزایش سود شرط بندی تا
0️⃣
2️⃣
🔣
🚨
برای اولین واریز در هر روز
🎁
🅰
g8
💻
ورود به سایت
👇
🌐
https://d812eoxsady.shop/fa/affiliates/?btag=914641_l303106
🌐
کانال رسمی ما در تلگرام
👇
🌐
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/funhiphop/79032" target="_blank">📅 18:45 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79030">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">چرا هوس اف دراگون زمین تا آسمون با کتابش فرق داره</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/funhiphop/79030" target="_blank">📅 17:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79028">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">سارن و کوروش کی قراره به این نتیجه برسن که ترکیبشون کیریه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/79028" target="_blank">📅 17:07 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79027">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">دوستان پدیده یعنی شما حدس نزنید کدوم تیم قراره باشه، نه این که ۱۰ سال منتظر باشید مراکش و ژاپن همرو ببرن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/79027" target="_blank">📅 17:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79026">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">کسی داره ۱۰ هزار دلار دستی بده؟ بخدا برنمیگردونم
@Funhiphop
| محمدرضا ناصری آزاد</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/79026" target="_blank">📅 16:43 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79024">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">کسی داره ۱۰ هزار دلار دستی بده؟ بخدا یرمیگردونم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/79024" target="_blank">📅 16:17 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79022">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">حزب‌الله رو که دولت لبنان اجازه کامل به ارتش اسرائیل داد خلع سلاح کنه، عراقم که کودتا شده دارن مقاماتی که ایران تغذیه میکرد رو حذف میکنن، از جبهه مقاومت فقط یمن مونده درحال حاضر.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/79022" target="_blank">📅 16:04 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79021">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">حزب‌الله رو که دولت لبنان اجازه کامل به ارتش اسرائیل داد خلع سلاح کنه، عراقم که کودتا شده دارن مقاماتی که ایران تغذیه میکرد رو حذف میکنن، از جبهه مقاومت فقط یمن مونده درحال حاضر.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/79021" target="_blank">📅 16:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79020">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">فنای بارسا اینطورین که از بازیکنا هیچ تیمی اندازه اتلتیکو بدشون نمیاد ولی عاشق آرژانتین، حالا بازیکنا آرژانتین کجا بازی میکنن؟ نصف بیشترشون تو اتلتیکو
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/79020" target="_blank">📅 15:37 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79019">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DpWlAcqlkpU2xG8RuN8OJPA2z1tgJ7zq0y1BH4ou8uDK0_NRlGMkvu5PqqMgyxNLXtq_bpNYVtelGzsQW_jBHViAXi8hRYPWxK6qDkNK6phzj9oATXu2cjc9fuB60WeJ5-soUf2oNTRoGcXvslibhl6hU81KsBOevb3Gr_aZZdgN3Cc564rwLRBwA5iOUp_3crBJ5FbxATGFlzu_luGnCUdKg_7vxS6lm3kyN8GmbJxjF7_soEeTSq_5lBOCiHyZ8HN4wEiaDqHGqzeF_7I_Fjl_0T59wZYGFmHetDqyWdV_XGc0pzSrA2KPs6Ej6B0sPlLxfRzr2qOiPhRzuQu0gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایان خودت نزدیک تر بود ولی.
@FunHipHop
| Sogand</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/79019" target="_blank">📅 15:10 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79018">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ph7ZSmxhOnwrG-ulUBsKv3ZiH4oGWlob7IW4DIbXdWUW87DKSi1Lh3J27pJIvmqierd2IIOu8h2Tye5HS4_FTwh_7lyxCHVUCQmNQWiMGnrYSqYNHtHGQYv3-35tYzccwIvpG-nf29p3h4sIqy1qiYPahFam94zsHXoan5jOT5ZLbUuEEPufOYO4ACU20y8vDUHZstbJYvAaAPJ-Gvh6PG-dNCehzTybRhch8rSHS9mLyFA0pPbq3um4LJDQzEM6kxr9nrKJNMrpLgqFPWND_TO7QdI5mLiPbVYZAOb_-KsTHWyxg5k-23O6CYiXKVnWtlMjSXP0QBxCNwuTxQJzOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری یانگ کید
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/79018" target="_blank">📅 13:02 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79017">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">میدونستید یکی از اهداف اصلی ارتش اسرائیل برای جنگ بعدی سایپا و ایران خودروئه؟
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/79017" target="_blank">📅 12:45 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79016">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">آناناس مادرجنده تو دیگه چرا</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/79016" target="_blank">📅 12:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79015">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AbIdOr-Qej_kekhMKTRTPJJbY2rldMbNGt8tPYm4C7rzAMU7_rCpmo6matCmIkERKd23vCGz_IJA58cMp3MjAc4K6HScRbGGQFdaNVMWfEjlkuZIPDOPv50ebeHKhrApyMdP4uAjUIa49MgFAkTobDUGg7phjHGldgbXbostYBhLcyHGtoKs0Bkw-HsnNNpvP2rIBcRQ56nNlPwvkN6D4w7MoHfLKLKHgP1h5hdwJ18asNiE3UUYevuepWbrwNrRABhUGbe3TMl7Rez4HV0p6HmGZsVrjJrSK6o9NS_ztXRMohsI6SElt4-vWRieuzSgx3gElMMaZPiFp8-RPsFqfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید کوروش و سارن به نام بهار ما گذشته منتشر شد.
Youtube
Download
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/79015" target="_blank">📅 12:37 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79013">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">امشب ژاپن کل دنیا را سوپرایز خواهد کرد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/79013" target="_blank">📅 12:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79012">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5be7060d94.mp4?token=rhCGwSM6QBf40fNqyMUMZIPb9LBkAz-G8Ot33eq_0-2DiBCZ-X8X9n1C9SIqHDdfLonZp7KUjGhNMG59a1a22Oozfcz9VmkC0iaKs5GQNP1yShq1ibwrjLNk9qPwAUMLFW4Esm6M35v296h7iNBNtm1mzj1dlVr-YnQd_-ZKfJAvEHl8P3xJDfyZnyNptTtVtkC2HbIbsO8xPKIwjPSLZQy4ZmqTMeZE7mZmRRWeBsGZVsWM-fde7rtIJrVxY12KvoyM_0mS_Rs0Q5wYPoDsYPL7tHHQiz2y0pxpvdoUjkRa3Jjc7v0npGhI5Qjp9_aKhXtdtKveWdySnO0y9Ra7nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5be7060d94.mp4?token=rhCGwSM6QBf40fNqyMUMZIPb9LBkAz-G8Ot33eq_0-2DiBCZ-X8X9n1C9SIqHDdfLonZp7KUjGhNMG59a1a22Oozfcz9VmkC0iaKs5GQNP1yShq1ibwrjLNk9qPwAUMLFW4Esm6M35v296h7iNBNtm1mzj1dlVr-YnQd_-ZKfJAvEHl8P3xJDfyZnyNptTtVtkC2HbIbsO8xPKIwjPSLZQy4ZmqTMeZE7mZmRRWeBsGZVsWM-fde7rtIJrVxY12KvoyM_0mS_Rs0Q5wYPoDsYPL7tHHQiz2y0pxpvdoUjkRa3Jjc7v0npGhI5Qjp9_aKhXtdtKveWdySnO0y9Ra7nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کیلیان امباپه 178 سانتی متری در کنار ویکتور ومبنیاما 224 سانتی متری.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/79012" target="_blank">📅 12:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79011">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iibhe-EeG20IJ8aISIgSnrcufmevzfT-W2r1W2tjO-046M2QrjfxXNU61GvN_LRS0BIAnrh7vEGJes-EJlM89GwdctZOnwV68SGi2Kg6VtYlrtcptsCUWGmiLw2DyBf2lFfFQUGGI7-eUT1yFOyoaLgDFsHqN8HtoGIb9L7inVNAaikjoglTbEespMblgX3QfsH02AKufez2aEX4_cbMuruBj99xRlQ4mGSSvJh5FCiS_OlGa6vFnsA7yDwTTR8Sx-IrOK0cXKOYWYwWWGedrRG9iMu0ylMHMDCP3s8VcWbeCk48OG94z7RfjVzq4teEU1XhV55yeLdb3Y-iRfwy9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦁
ژاپن
🔹
برزیل
🦁
🏆
پیشبینی مسابقات فوتبال در
بری‌بت
🏆
🤩
🤩
😀
دریافت سود برد برای کاربران سایت
🎲
با بیش از ٣٠٠ نوع
آپشن پیش‌بینی‌
👑
بالاترین سرعت انتقال
برداشت‌
💲
۷٪ شارژ
بیشتر برای شارژ با روش رمزارز
👑
مجهز به سیستم
پی اس ووچر
👑
👨‍💻
ادرس سایت:
📱
https://d812eoxsady.shop/fa/affiliates/?btag=914641_l303106
🦁
کانال تلگرام: r8
🅰
📱
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/79011" target="_blank">📅 12:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79009">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jnFU7H3M0kB_-NhB53DiIktWl9ZJGy2S0nfx5A1jdVP9Mzpvr-tTZQG4zR2qvlamjkjXBU4DCEbbLSaHzBYN41VA0mGdPTtkkdCZggNgV3BtAsV614LDW6ygA1lEzKftia7n8JeRb9ZESzfJwaO00eDftwKGyN6PJklvJhlZS2y_wMznZqejqgnEDNNsoguZhsS8hkOMuavBmgcH1WEt8Nfiifv1Z3ybfzPVoxiPgMXSjRokKN2fSumyDj5HjWAsMaE-zcSTyH89__3twLYVi6damVgkIk7Qfnma_wcou8__sna7zLMsrONmFOdwkTeUYY8-oWgrZLV4jtLWQsBoWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امباپه کیرم تو دهنت.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/79009" target="_blank">📅 12:02 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79008">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ناموسا نمیدونم دخترا از چی پسرا خوششون میاد، پسر خیلی کیریه</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/79008" target="_blank">📅 11:37 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79007">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ناموسا نمیدونم دخترا از چی پسرا خوششون میاد، پسر خیلی کیریه</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/79007" target="_blank">📅 11:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79006">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">هعی از وقتی اومدم کسی من و تحویل نگرفته:)
چه چنل مسخره و دختر پسندی:)
ما پسریم همونایی که موقع حرف زدن بهشون میگن هیس:)
همونایی که نمیتونن کراپ صورتی بپوشن:)
💔
🥀
✌🏿
حرف دلته؟:)
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/79006" target="_blank">📅 11:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79005">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">حال و احوالتون چطوره؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/79005" target="_blank">📅 11:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79004">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">حال و احوالتون چطوره؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/79004" target="_blank">📅 10:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79003">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">پشمام با این گل کانادا رسما تیم قلعه نویی صعود میکنه مرحله بعد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/79003" target="_blank">📅 00:26 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79002">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">نتیجه میگیریم دریک کیر منم نیست</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/79002" target="_blank">📅 00:24 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79001">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">کانادا زددددد
دریک برد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/79001" target="_blank">📅 00:22 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79000">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">لیگ ایرانه یا جام جهانی؟
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/79000" target="_blank">📅 00:12 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78999">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">نیمه اول بازی کانادا آفریقای جنوبی از کل بازی پرتغال کنگو خسته کننده تر بود
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/78999" target="_blank">📅 23:19 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78998">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">مثلا بازی با سوئیس بره پنالتی و بیرانوند همه پنالتی هارو بگیره
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/78998" target="_blank">📅 22:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78997">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">بازی امشب میره به ضربات پنالتی
بماند به یادگار
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/78997" target="_blank">📅 21:46 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78996">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sH5vmDss_vaxVgfOBbjDyNH2o4fNJW79_qvHQsdCQ6lywtbba245l0qTKnSL6S4JwiKmJPLgBCyv27CLvp49LBNZtm1clKTQ7IdA6yXo1ZbueLHmOUqrmrDuLpBB8tFb-ufu9u4EVWdKRlI0nWI5845r2zmebKzIxwv49ACfuRPsXa7a8Asbg9orOI4DVtqmGouNXrBGoHYaGnafWbWhnATZiZJCnAGhnm6lTOPvDSl6WB9aj-X-E30q-GxHBuwmvjq3OdNMUnh9UcrhQWHaIl-tlcVUA_3MymCqssUdaCNdDgQsoiHnQUHIEtBCXsG2K9ORhOQYx7UmuRM6wGtXaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زندگیتونو بفروشید بزنید رو صعود آفریقا جنوبی، دریک رو کانادا زده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/78996" target="_blank">📅 20:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78995">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aaq3xOZd1ehnARxULGhi8YJ122q8bRTR9-ZOCKLxGfKNYHcXYwD4ccn3zle8lG25_-UBUPSgXTpA9iWi7w7zFgZ5PxsHOl_GJ6x5IC4CQnawWumU3ChDrT2CN7bKrF8bIrTzxGy1MXJdbhYQphxwDun3JpYnrp23EyJpOnrRZtfgsylPrVL2jvSrIIeS1gTszbaQPPGTbTBjciRlfKiseD-q0ba0xymRyYXM-ZXbHC4mNoREwhczTQersAiLJucvfWt32pwfs5Ch2RPt4YZIGcRgbEs08tRXNgTDI8bxh2t0d2mlP5ahTCAgpSi72zZhHIvC4SciK-TYqVF9Y3F8vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو افشاگری جدید برنامه Jeremy kyle مشخص شده این زوجِ گی بعد از اینکه 3 سال باهم رابطه جنسی داشتن فهمیدن با همدیگه برادرن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/78995" target="_blank">📅 19:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78994">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uqrQmlsMs0yt1jpJXnfooMZtG6yh-LAaEFsgNMktDbhMLmlZyRX3its6eMHH39W9ji6PcD4_r8DhJ-z3lNWQZODTyND4QbjzYBWWYNUMb277g63NwjNqqfhC_v73d_WkQJqWEPh4YzcVeU9rllss6cnaXys8N3oFgTgVL0uDk0VD5Fdw26nZNbNcFBYnlhD-6XNyoZij4--az2wAjhw029cUN5aipaNcSxxi2KCsngWM5NRy0MchiRtR45J0q3vCIdKUp25T8KV4OMWPV6MgM2OA8aKrUkVox_lQtHuA32XSlSbub01oMlCTvRa0Uu1ug_Fwb3i0wP213kDVKqq60Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب تکست کصشری داره ترک جدید پوری
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/78994" target="_blank">📅 18:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78993">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ge-PznlUMz2TDxoods3oIFeprFaygwg0sxZ8dSliuK0qDvTpabd8-En0pAA7YJhi-cgwo-VhshQXkhoPdjsJG2YTLAfOv9VlPyNIuiNWiSKHwMfJFZkT6sBpJDdkgkRlgEcL8giM9ecvPq7-5ca5hifTxnGODKI6yjmW-LVlmLLn4MunMHY6kANsDAaP4-beFQVJiqtvaRDNhRtuROaetWqPIln2T8GERxnh_qdQKGWd_l6cukeaLUM-mp_7Wg0kZLKSm3kVbTYFZIpH5zESJwm470mPVTfJCjPS2Pqscz3DyDrERqgtdbj79Ev2kIy1r2uHvv5h7e5LOUV3O6RH3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید گوگل و تبریک صعود به مصر :
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/78993" target="_blank">📅 18:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78990">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ETmRPpnDubDaMx4GWZRoFBLQAL-3CQsrJs5wUl2myNzkpBYxc7PEmKWyEn-SoW8I_uQh9CYqe9DMy9hvdaGCvXDbiJM9Ns23cxi5u3GE0VQQ1kOWZw_aB7nWRMT9UV38_j_B_qMsjoTUdnyLeqfS5LeoAWBIrUcSWesEsoGZqV1oneGjBm5YnSOZjq0C_7VxPpBwtazuWQeklvTWvcQtjPwkJxDWGN4XYCnWzQ0bUl8zAyn8CihEEBNikWL1ZFaQVFiF3KbDZfx0N2ajtAn56iwHxQNxdhucobHDO2wVaOboHcJE0WvaMk86rR1DlKMx5Kr1Eiq8Ze6D_X3VpX2N3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری کوروش
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/78990" target="_blank">📅 16:37 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78989">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ایران توی جام‌جهانی : ۳ بازی انجام داد، با ۳ مساوی ۳ امتیاز گرفت، ۳ گل زد، ۳ گل خورد، ۳ گل آفساید زد، ۳ تیرک زد، رتبه ۳‌ گروه شد، بازی ها از شبکه ۳ پخش شد و برای صعود باید منتظر ۳ بازی آینده بود و در نهایت با تساوی ۳ بر ۳ الجزایر و اتریش حذف شد  @FunHipHop…</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/78989" target="_blank">📅 16:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78987">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JgTyoPRT0e3oLkNGkbFUYofJEgoC6Rp5wTo86kObdMz6o_DErKVKYjhzSe1_7wq73aGvrTTLcbJlP_yNQWxmYLAK26z-ff7FHwQ3UBaG9qDtB6N3b0XjaLZKkyh3afcdxSYvpA7SKPyhcc56fRtiho7PeiyIBReA4ho_s81KQDuBMLUBA_0AFkVt-xiSS3x_oo81hipjyUlJqW6Q6fkpwSqRC1fAvLAZAsBiYxsABFZNtglHEmSRNXddUOAHEUvoG0gk5IadCQadL1SpFCEuCkGbd8siWjgZhj-YHnImHmwC9eRnxbJaMBOz7lKKmdkMAcRmPZc2Fs_w6vr5BuPf0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز خبر اومد که رئیس‌جمهور عراق یهو زده به سیم آخر.
یه شِبه کودتا کرده و با لشکر کشی و تانک و... حدودا ۱۵ تا ۲۰ نفر از وزرا و نماینده‌های مجلس عراق که اکثرا حامی حشدالشعبی بودن رو دستگیر کرده.
با خودم فکر کردم که یعنی چی می‌تونه عامل این اتفاقات یهویی و غیر منتظره باشه تا اینکه با این خبر شاهکار روبه‌رو شدم.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/78987" target="_blank">📅 15:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78986">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N6j8yrupF5mkqKZtjmWJ3_8rH-SOYAU1r0UViEXY5izaUDSGHIrZ2HAIiwVWMtLErjEZxXw5XN1rZiUUGMd9TcLvKvoFAA2e5b6iTTg_f86z7VgmuP8a4a7N-En8deMLGRTKyGdkFQYIu7ywGNjiWLLT8sDXv7hIJcSSG1SFRXWBBAAGJ4np6-gxZaq1Ym-HpC5SpZA_5IhstALgBlIkaAVVE04ddzhsZZoIuUs64hsKTlGNVY2hD0ELlkeGKTmEPnn9ZoSdvW8zHD819qBAn_kAkirHG7wg6HlQgOCUGwHt4EoiIbCHF2wb_nsG7xFKGOvbpUA46oIVsAGqe-VBcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری میثم پیرفلک پدر کیان پیرفلک عزیز
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/78986" target="_blank">📅 14:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78985">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sXhOYjrJfwhWcKbQXSGl3WlA_xTRk4FSVnglYtHlahZ2SeoRiYRF2dJPeWXMfceUmhdUyHYaReaz2C5oW-rltdM7b1_0yImnBMMNz8oD3oKLv-986xpOFdAJitEVU2s8CRUNk6kPl6aHM8B9SySYEp5mcpVBLLepjmMT7ZXW4UI87rZUOVsMWaFf7OJGnTVyK1SRv1DNc4fj-LpKVASbpfLSKGcvN5vmD4iQw5yVotyX-zZGZfEQhpXiMDhUPTj0giLY6sYVcYNFna5XzVHD1jPDIQ1aMgz8LZormt_pMF-DEnZg_cspSA0KJ0l_eJLsvCJOsRmz4ZsGG1aiQj8BWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شلیل زاده ببین کاراتو.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/78985" target="_blank">📅 14:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78984">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cac12d8a3.mp4?token=agqKRNEKHXCV2-JmwNOYZbvlkpOmYaeESEHNArIRNbZ1ucFye6T0jhD-ZgzqilqXTPqK5ZixHTsRj5gPElGHkZU7lAgeTaDmdPISUCIqh-_tRyUgieKWS9Lejd0njfltrZgE0bqF1-e2GSGAf5RAv8je4RP9b3FH4njE8xuqMcb1CnLjq-Kk1UyguIk9qoTVVEYto44b9_bCN39uQPzHps3PpjJ52qorQljh3Iv0f7QwtxLk74wjQB45HUIDQ2jUMRWdRJmU9BzKwpd2npHK9c_A94rOG-KeJqcV6zYeM2xpbscCriGZ1beuM3pKvx7wKMLtxfOT8YUlqm050AKDmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cac12d8a3.mp4?token=agqKRNEKHXCV2-JmwNOYZbvlkpOmYaeESEHNArIRNbZ1ucFye6T0jhD-ZgzqilqXTPqK5ZixHTsRj5gPElGHkZU7lAgeTaDmdPISUCIqh-_tRyUgieKWS9Lejd0njfltrZgE0bqF1-e2GSGAf5RAv8je4RP9b3FH4njE8xuqMcb1CnLjq-Kk1UyguIk9qoTVVEYto44b9_bCN39uQPzHps3PpjJ52qorQljh3Iv0f7QwtxLk74wjQB45HUIDQ2jUMRWdRJmU9BzKwpd2npHK9c_A94rOG-KeJqcV6zYeM2xpbscCriGZ1beuM3pKvx7wKMLtxfOT8YUlqm050AKDmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت هتل تیم فوتبال جمهوری اسلامی بعد گل سوم الجزایر
🤣
🤣
🤣
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/78984" target="_blank">📅 14:19 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78983">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">"من برگشتم" رونالدو مثل "من اومدم که نرم" یلس نشه صلوات
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/78983" target="_blank">📅 14:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78982">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">جدی چرا چیزی از ارزش هامون کم نمیشه هیچوقت، مگه چقد گرونیم؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/78982" target="_blank">📅 13:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78981">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">قایدی زن جنده تو که قرار بود یه دقیقه هم بازی نکنی همون نمیرفتی نمیریدی به محبوبیتت دیگه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/78981" target="_blank">📅 13:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78980">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">اوووووو رامین رضاییان اووووو رامین رضاییان</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/78980" target="_blank">📅 12:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78979">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZOD7Z87hf5phxhdY0w5wEP9EjYKT21mP1thvOxk5P_joktq4-G8dej7RVNXO4oUMJoY42iXqg06Ms4jBihzy_cuVIMRJAN9EY0kv5inK_2rkW1g--56H-wzqQmvw3GtoFc24HgRxzjaxUXLJJFZD363iQZ1JU9WbWZGhFEzhAP1dgw3EnEloA14WEXFpi4cxA0s6A9xCUGO4xg5V1opgOI53jvp9qR5n1Hvf7Zsj77TJzXxyF5fDNaE4eixz7mjN6b3mEOifkCwOpbc3-hCO1TqYghT1fy5o8ZFf8CKFE44I8YNAd5aNKbVhLduqSm-92gK6-xO7WCW1Y4mmUB9FaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هالند: مسی هیچ‌وقت قرار نیست بذاره من کفش طلای جام جهانی رو لمس کنم
😭
😭
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/78979" target="_blank">📅 11:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78978">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">سنگال با دو باخت صعود کرد، ایران بدون باخت سقوط</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/78978" target="_blank">📅 11:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78977">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">همه دارن خط حمله های آرژانتین و فرانسه رو مقایسه میکنن، ولی بنظر من کلید بازی دست انزو فرناندز و مک آلیستره</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/78977" target="_blank">📅 11:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78976">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/esT099IJ5nPC2lQVfduzUKKYPwpJqQ10DBoMCysaDW-qX7r1rl7ceSXhPmiJ5Ahwq_PzkT1Mvr-mu3y1vkP7sO97CwM2O7do7agwcZkobQz95Vj2LeMMYAcaVsMOBjLCTqAX-fgHDRvdxN3gd7A1X5zcfmBXw7zbS7YTxbECnJwUN2-b5f3QBtjVDIoiKYJ80CspIJ27zfdYsBfb6F8bXhpnCXIrfulfcVvAJgumSVNpibJW6D2MQiaGPjhQDaj8BJgdX-Pb3RhlZFFHBV5CcCwXGs_z71U5lF3HFJhMTIfA6mDTcbHevRtL96vFdWv2b_UswnQG44-vDprkYThFJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخدا خود فیفا هم نمیتونس همچین مسیری تا نیمه نهایی برا یه تیم بچینه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/78976" target="_blank">📅 11:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78975">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">هفته دیگه قلعه نویی میاد برنامه می‌ثاقی میگه فودباله دیگه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/78975" target="_blank">📅 10:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78974">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RbdEngTbzTArhGBmXYOkXPCG8dpiNQBS49xnInCdcuXxjlVHLz4ItLWeovM2C8F5Zphy63t-wCbQMBL8hLVqXp0uWBm8h6DOvKppxSdaCukCrMzJoOzIPe6w1FU_3snsu1YSFZglknGgcnxmnnf5gqjSDHC6yGZcK8vyCnlaU_cF0plbiRCeYVC2PqPQ8qIJmdd_fsE2zKEg2V2pUPW93s6z8uDSvYiysdbCXtEja3iu9BPaaKotg57JMwf1Nri7sOo56fr2qHj_2GcJ20SGEoYlTZQamtL8uhvfYL6Tj_aO9Mq__pXY0mxc5GWUgLtpKhbNlFirgQ9uuhswDbD01g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب یک بار دیگه پروردگار و اسطوره بی همتای فوتبال جهان، حضرت لیونل آندرس مسی نشون داد کت تن کیه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/78974" target="_blank">📅 10:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78973">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">1: باید یا غنا کروواسی را شکست دهد،  2: یا کنگو نتواند ازبکستان را ببرد،  3: یا بازی اتریش و الجزایر برنده داشته باشد  هرکدوم ازین نتایج رقم بخوره تیم قلعه نویی صعود میکنه  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/78973" target="_blank">📅 10:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78972">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PRUBRh3S3x48lsp_naxLt-WbthsekUBr5BVUmkWR7oiitbqUR1HTP_23Z5dFP1qIvWGrA9EspoMrCDrGVhq678nr1LyF1nnsbnx5_6prSoshm4xfJ2YsmX8zM08yp13Smz-S753AJa7sWwe2evnx-RNuzSLoTkfpLZnvghw7j5BKlDwhCF0PSNDWgf9YNK2UXh9KBSvS82g7vFH9IfxAoppxK6mzMRPFqYjBSKfkcfMp3mzS5RJPTm_2gu9j5CT4HdazkBvCv9KGBP1WR02gL589_2JdUPcp8qBO9cl3s6SoWb4zJI5CJaBO1kbdcXnqjx9kFtRR6T8c8c1P3pQC3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران توی جام‌جهانی : ۳ بازی انجام داد، با ۳ مساوی ۳ امتیاز گرفت، ۳ گل زد، ۳ گل خورد، ۳ گل آفساید زد، ۳ تیرک زد، رتبه ۳‌ گروه شد، بازی ها از شبکه ۳ پخش شد و برای صعود باید منتظر ۳ بازی آینده بود و در نهایت با تساوی ۳ بر ۳ الجزایر و اتریش حذف شد
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/78972" target="_blank">📅 09:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78966">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">سلام بچه ها من تازه بیدار شدم، بازی ایران سوییس چه روزیه و ساعت چنده؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/78966" target="_blank">📅 09:19 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78965">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">با ریدمان پرتغال جلوی کلمبیا، پرتغال، کرواسی، اسپانیا، مراکش، فرانسه، آلمان، هلند و بلژیک همه رفتن یک سمت جدول حذفی</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/78965" target="_blank">📅 08:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78963">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iTxgTV6EhyxZM3_vvUmDn8ux1cAzlRS-ZOSY_vuDUzKh8Jn-koyG9bmcyGqMk9Sqj6Kw8eJwJeZhiugR2tu5R16_c2rcWVaf_aASAwRYDQItcuVic3dzT320f5VUKOZ8C43hv9O0FawJs7i1FGguDURaZ47pzBJXhJCtOaZ4ikX9UuBUmb52mV6C_CVfCYfN4LD8BW6rPhcGhBusfHe8KAkrYO4qxQiXS-p3raFRVLRmNXV6H29V7Mesp1_axVKTl0yA6J8z8UA6eYC0sZCV7N-3MeKvH9SklfQzW2NNU8kLMgAwt0OflKxV--PVN3Pq7NCYHDMWXUMiM1B9fb7ZHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bzkZU7R9fXBXOL4Cb2g64wN1QKa2mjpaeb3V_yAscPE6_BVIKRq7fqe4k8f8OeKSaCJOwpz8gz4MDW60RyBnvw1S9uhb_Gal72ia1TXYzUM-87A-9q8ICvqeThBmrSo5KUKvsmq_auLFg6wrvAOc_RpALcIdmu9Fld2tlTao2nQ-JTWSRVOOsXY3_uqeiwqnicfbvIjz6nSPwnwi1Y1Gw9UQ0gutn-LkDW4hp8jcPmPQS1-mfJAVU9dzNZs6dubrO7soFjutLQt6BmwHlVJwxxlXIHFVfHkg-Wu3OKgM9cTA9Gdapbqy7RkRvLQVDCXhvs0tepoLGZDE2oK1Ah1aIw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من برگشتم !</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/78963" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78962">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QBXSS-WmBEIFHhDBZ6P4I_P2fN_O4XwQBvFVPmqJJn7f4tflXltaWcPPOeSc4GJ0w7cQAa9v5Gya8JTeXlWVhAZ2R_zmUYWF_dz2L2yoSumwvJMzwgtePBfMXAzWNe4-JtkaO3D5GGBZP8ud0CLKv9_l760rYw-rSi8NQXiu5kCctTxHMbkxk-us2s1Slg6WzkxQDNTn25S9P44AskfgefBkaSY22ddXF81_ErYiBL7dQhBW6iZnDSey2mmCRAKNEl7bcssec_qJBDY1_sgLo52kr97LtqMao_TPcbAltiSto5SAvNIiy4lbfTSL-HSpXT0iupMEhQZvy1xEtO_DFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ریدم</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/78962" target="_blank">📅 08:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78961">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">احتمالا نیمه نهایی انگلیس آرژانتین و فرانسه اسپانیا ببینیم</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/78961" target="_blank">📅 07:59 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78960">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2aa8b89a24.mp4?token=KnoGhTXaqs_6GdLRUB4VsGlqG2AkHEKoNWuDfkxzVf5DbFGqbvJuGQsVXhhsqnILP8PwsuTXdysV3JEZvwJW6Qs0AleWXEVDqIMP20WFiu9csKOLruG4Ow2oyptBoiDZeaBUCnGqapJ05Dhxg1jM6R2AgmIceidOUMfixxd85HHcdyFt81V0M6RitH-QNbC8zxjt-d-AkQumdn1RRuR5jTa5Oiybx2LIB5RwaPCLCwPFn4O7l1TVbnTqlS4dHdvIu2_V6wrCvff0WOmG9yGjiW-PZuHXhyNfq0KUDhfTbM3fs9SlYnx87o2bxvgFf0enPMzmnAZlAJQueNGoh71V9oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2aa8b89a24.mp4?token=KnoGhTXaqs_6GdLRUB4VsGlqG2AkHEKoNWuDfkxzVf5DbFGqbvJuGQsVXhhsqnILP8PwsuTXdysV3JEZvwJW6Qs0AleWXEVDqIMP20WFiu9csKOLruG4Ow2oyptBoiDZeaBUCnGqapJ05Dhxg1jM6R2AgmIceidOUMfixxd85HHcdyFt81V0M6RitH-QNbC8zxjt-d-AkQumdn1RRuR5jTa5Oiybx2LIB5RwaPCLCwPFn4O7l1TVbnTqlS4dHdvIu2_V6wrCvff0WOmG9yGjiW-PZuHXhyNfq0KUDhfTbM3fs9SlYnx87o2bxvgFf0enPMzmnAZlAJQueNGoh71V9oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارشگری که میگفتی عزت اللهی رو برای بازی بعدی از دست دادیم، بیشتر از همه به تو خندیدم حال ندارم اموجی خنده بزارم</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/78960" target="_blank">📅 07:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78959">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">یچی میگم نخندید،
تیمِ رنک ۲۰ فیفا
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/78959" target="_blank">📅 07:48 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78958">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">گزارشگری که میگفتی عزت اللهی رو برای بازی بعدی از دست دادیم، بیشتر از همه به تو خندیدم حال ندارم اموجی خنده بزارم</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/78958" target="_blank">📅 07:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78957">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTq6UvVJMK2WzHLF4heYf1Yoq39JgxMIaApBbRUQ6dVO5qraZiZwgKU8RqtbsI0ED54Faw2hW8vDH7eawPTlDiJuAMlwPmcIY3B2rp4W5xVR0mnWlcYQHSTeq37J-F-Zh3ZTXBjp332uhJ6trKGFQ6n98RtvqPpobp1H33BAB5TEuyIotP7ygi6T9AElUNKx0ML1OMt0rIS3vJKCvwztZHNsrQu2BlAHbVCSMo7zxbs912w-ori2cza2_QbRyP1vgr_MNOWUSCmwzv5rqqtkKEQ00aA59b4xVFvmxMOnwGyIKDT0dAXy0T-Y8JTA4KAk2O8KTHXlyVm4LvcYN3VIEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهدی داش چیا رو که از دست ندادی
😂</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/78957" target="_blank">📅 07:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78956">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">صبح بخیر</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78956" target="_blank">📅 07:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78955">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ژنرال خارکصه تو چقدر گناه کردی مگه خدا هم نمیخواد تیمت صعود کنه</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/78955" target="_blank">📅 07:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78954">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">عجب سوپری زد اتریش</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78954" target="_blank">📅 07:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78953">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">یکی ژنرال رو نجات بدههههههههه</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/78953" target="_blank">📅 07:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78952">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">وااااااایییییی</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/78952" target="_blank">📅 07:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78951">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ژنرال صعود کرد</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/78951" target="_blank">📅 07:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78950">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">اتریشششششش حذف شددددد</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/78950" target="_blank">📅 07:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78949">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">تاااااااسسسسسسس سومممممممم</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/78949" target="_blank">📅 07:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78948">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">تاااااسسسسسس سوممممممم</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/78948" target="_blank">📅 07:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78947">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ونزوئلا زلزله 7.5 ریشتری اومده  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/78947" target="_blank">📅 07:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78946">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">این وسط یه چند تا آژیر و صدای انفجار هم تو کویت و بحرین شنیده شد که چیز خاصی نیست احتمالا حملات پهپادی سپاه به کارخونه‌های پرچم کرنر سازی بوده.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78946" target="_blank">📅 07:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78945">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">حضور ۵ دقیقه‌ای ژنرال در دور حذفی باز هم لغو شد.
💔
گل دوم برای نماینده‌ی رژیم صهیونسیتی در جام جهانی.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/78945" target="_blank">📅 06:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78944">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">گل دوم برای تیم دوم ژنرال</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/78944" target="_blank">📅 06:48 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78943">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">نمیدونم چرا اینقد بدشانسیم
۱ بار ۲ بار ۳ بار ۴ بار ۵ بار</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/78943" target="_blank">📅 06:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78941">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">پایان نیمه اول
خلاصه:
ژنرال ۱۵ دقیقه در دور حذفی حضور پیدا کرد ولی در ادامه به واسطه تبانی پرچم کرنر با رژیم صهیونسیتی این حضور لغو شد.
💔
#پرچم_کرنر_۲۵_سال_آینده_را_نخواهد_دید
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/78941" target="_blank">📅 06:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78940">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">عجب چیزی زد بازیکن الجزایر</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/78940" target="_blank">📅 06:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78939">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">اتریش ناخواسته گل زد</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/78939" target="_blank">📅 05:59 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78938">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">این همه تلاش اتریش و الجزایر برا وقت تلف کردن و زدن توپ به در و دیوار دیگه صرفا از سر تاکتیک برا مساوی کردن نیست؛ انگار با ژنرال مشکل شخصی دارن بی‌وجودا...
💔
@FunHipHop | Nima</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/78938" target="_blank">📅 05:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78937">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">یادش بخیر مانوک خدابخشیان ۱۲ سال پیش خیلی دقیق این روزا رو پیش‌بینی کرد و گفت یه ژنرال با سه تا تاس بازی می‌کنه...  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/78937" target="_blank">📅 05:43 · 07 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
