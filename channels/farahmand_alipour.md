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
<img src="https://cdn4.telesco.pe/file/ufNmzAP2iep-muw_aoxfd_bSq4Ncpm19PuWDc1-pmLR_KKG2pUY4N7hFrvyR9_Sy8QvhZKIeNxnmTjKGfFdg6NofbTp2C_6R8YWOD1frB2pYa95NZnl8HmlVv48JU6ZXDr3zbRYeNdT4b6vo_eI_7oPuQAo85mCCjgL3QFe844su5uFKaZ-ZoMLVmoAwo99QRK6bS6r5EMDn6-fhBFEaU_sXEjFP2FZD8vA_RJ7kkCtWnJvo6Uzpv3Lv_CMbPYfaH7uB6cNPfOxDCDTCdd53VVkHYTlFrXgh37aNlDaL_GkZzxezuzjIQ4hLPiwbPG3piM6jDsoTUSvNB2oer7QePQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 64.5K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-22 16:18:56</div>
<hr>

<div class="tg-post" id="msg-6552">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ixqchdPXuTArqJNK3_zh6Ggm8Uw7xNqNx2VZw8zNTGe92I6YSy3bEHIFx-_R3R9yQQA1qegQkVLqX4xK2Y7MVdomnmpl86sF2VwHGWkSeDBNj7H0OhLY9buN6cy7WzfXABDrgucQEJMKl4pcEy_T7Dktbggnuij9YeHIO7YMp820ZjYhbxU611SsaK_MZ8G5b8pj_jmiQCPp4RMpJ8ke7-eUDjExQqKPInuHg016NU8m1IkGxS3rNPNX4xgCDuPYaz9hcilT01oAl9U0feLT5qf6TbPTxaeibtufs-LO_SvKycYiiwxx21kuVsbt1cOxTM_vc1iFU0gM_PvGqFDWyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا اون موشکی که زاکانی گفته بود دقیقا به خونه‌ مجتبی خورده بود و خودش از اهداف حمله بود، باعث ناخوش‌احوالی مجتبی شده و گفتن پول واریز کنید  زخمش خوب شه.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farahmand_alipour/6552" target="_blank">📅 10:33 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6551">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔺
آمریکا در آخرین هفته‌های سال ۲۰۲۵ (قبل از شروع جنگ ۴۰ روزه) حدود ۳.۹ میلیون بشکه نفت در روز صادر می‌کرد.
این میزان در ماه می، به رکورد ۵.۷ میلیون بشکه در روز رسید، یعنی افزایش ۴۳ درصدی صادرات نفت.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farahmand_alipour/6551" target="_blank">📅 10:29 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6550">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">وقتی ترامپ در ترکیه بود اعلام کرد که با «ایرفورس وان» ترکیه را ترک خواهد کرد.  جلوی دوربین‌ها وارد هواپیما شد،  اما بعد از درپشتی خارج شد و با یک هواپیمای نظامی ترکیه رو ترک کرد!  نگران از تهدیدهای جمهوری اسلامی.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farahmand_alipour/6550" target="_blank">📅 10:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6549">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RZAS8hiAKSGNNmaPjwtV4BX1NqmK0gUECxTQvx5GAbab0ba-_Nt7Ufd9yObbS-jtjxGzu_y3EwAPv6FBktiMDXmehG6CHX7kqvovYHiiWm3bagvOyNzLZv1-is-WPZ9oYMdH9i9rNqDdXHK87b2Hjtqd1KRXvfYYoCxuldSpLuxNNSrL69vcw-7jGm0Mr1RjT0VLOkJ-9Z5zXUAqTdZ3WWZMB87NvTmsu_1PacY_4zw2Gd1kg59cPSXWmXFRDdroCblVmavW1IvF5CjxSnhEynADxIMUiykOD5LtsIqahcFsNEpmjrFgwD5HuyJGAF98sdwVG54amM2okCx_nb6uHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لکه نفتی به جنگل حرا رسیده
و حیات درختان این جنگل به خطر افتاده.
اما این لکه نفتی که تهدیدی برای سواحل قشم شده از کجا اومده؟
جمهوری اسلامی ۱۲ مرداد (۳ آگوست)
به یک کشتی باربر (و نه نفتکش) حمله موشکی یا پهپادی انجام داد. کشتی داشت از آب‌های ساحلی عمان عبور می‌کرد.
پرتابه به موتورخانه کشتی «مینوان پایونیر» اصابت کرد و نشت نفت رخ داد. این لکه نفتی رو موج‌ها آوردند به ساحل ایران.
سخنگوی وزارت خارجه ج‌ا (بقایی) هم تایید کرد
که این لکه نفتی ناشی از یک کشتی‌فله‌بر است،
گرچه نگفت هنر دست خودشونه که برای بستن تنگه هرکز به کشتی‌هایی که در سواحل عمان حرکت میکنن، حمله می‌کنن.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farahmand_alipour/6549" target="_blank">📅 10:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6548">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z4N6YdQiwffcDdghLmWkNObjEASDtXrj9scezD3-eavBla1pLmPB_N509BxWxyCP-ZN7y74q1q1kHG8fUmQicJf6LNNuwMJrncfp_fWZn38gxbR4uH4Fr6Fm9yhzHuQGYNCF9BugJxrtWlATN_kXqeOV2pf8CgtSYpngsicXXGn-IPCbJd2tCwk7MdIp-qDEtYlAnwPjWS-ZMiQt0nkjbGdeGistvpscm76DLxp-N9VIt5NsQXT9aP_mM73trDkaFI4fh6EH5v1b2dJQeFIdmUTg5-eynhwBLjx0D5nmqhY1EmP2DnsuBvNgmtUDj5iSu6hiWbJXFwI1qKAiH1STOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
بنزین در کرمان ۸۷ هزار و ۲۰۰ تومان!
میخوان آروم آروم و استان به استان
قیمت بنزین رو گرون کنن که بتونن
با تفرقه انداختن بین مردم جلوی اعتراضات رو بگیرن و قیمت بنزین
رو
۱۵۴۰٪
افزایش بدن!!!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6548" target="_blank">📅 21:54 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6547">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WU_WkNruyvGgmMTtTtqNlKd1cclAxuFdzc9OJ-rmh5qyny1hi5mdcgdtyYZbp5z6JVaM6mNRBhmSiJEPdOiefcHewWAF0UEM4JMOclZijA5Vv-j7oSBd78J-YYA9SA05lPi9ySaAhZk0BWbEa8mVi9ogBCba1Tv5FFKXCAOgyD4ZM7OBOdCD_pAKcqkec5X9S-lbUc0nllJySqzuCmlJyTsRQdazCZ2yDDm3J3Q0YQi-vCpJuJiQDkNOPeE7Ljjo_zi5-5IuTdLL7UH1MN-hryOkXVg0wsWUsBDbLMtrm4N_gY2bgowKGZCJxDcpICRPL9kt_Rvr5EeaQ4DSm_oMfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زاکانی میگه : ۱- موشک مستقیم خورد به خونه مجتبی ۲- مجتبی خودش هدف بوده  ۳- زنش کشته شده!   اگه مجتبی هدف بوده و موشک خورده به خونه، قطعا همون لحظه مجتبی کشته شده!  اینها فقط برای اینکه حامیانشون رو نگه دارن، یک اسمی انداختن وسط و گفتن بیایید شعار بدید  که…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6547" target="_blank">📅 15:30 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6546">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7024d4011f.mp4?token=G7QPXRrh9eiLnUBTykZQxAZGs8NgOrYEBLiEQVtlqekGe_09M2iBuB2i4sycYkJHZkYbKeI25OmOOEIuKuB9EnkIlr6Mh3RTgBObIDEouS-4jpDc5emqxhtVT8KKzGjuPAI4mU45naqfcCLApna_8t6OjEHGkB7Eq-3lx6P9hE5vbkzWjPW5szpcCbMe87fQil7cjU6rJ_kc0lCUbujYuqyr24qxrQuJdKLvCLog7XCi228HN6T4Coe4X693VTlFFwGrxR2YnP7d0oHIxBoUgf9urAt2WUekCeNgYv9Zc364l3fuHvQr6kOzwYKBAmooDknO-iLuWbsGSH1R5x6OLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7024d4011f.mp4?token=G7QPXRrh9eiLnUBTykZQxAZGs8NgOrYEBLiEQVtlqekGe_09M2iBuB2i4sycYkJHZkYbKeI25OmOOEIuKuB9EnkIlr6Mh3RTgBObIDEouS-4jpDc5emqxhtVT8KKzGjuPAI4mU45naqfcCLApna_8t6OjEHGkB7Eq-3lx6P9hE5vbkzWjPW5szpcCbMe87fQil7cjU6rJ_kc0lCUbujYuqyr24qxrQuJdKLvCLog7XCi228HN6T4Coe4X693VTlFFwGrxR2YnP7d0oHIxBoUgf9urAt2WUekCeNgYv9Zc364l3fuHvQr6kOzwYKBAmooDknO-iLuWbsGSH1R5x6OLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی میگه :
۱- موشک مستقیم خورد به خونه مجتبی
۲- مجتبی خودش هدف بوده
۳- زنش کشته شده!
اگه مجتبی هدف بوده و موشک خورده
به خونه، قطعا همون لحظه مجتبی کشته شده!
اینها فقط برای اینکه حامیانشون رو نگه دارن، یک اسمی انداختن وسط و گفتن بیایید شعار بدید
که دست اسرائیل (دست خدا) عیان شد
و خامنه‌ای جوان شد، ولی از قرار معلوم میخوان آروم آروم بگن که دست خدا، هر دو رو از زمین برداشت.
موشک خورده به خونه و زخمی شده  باشه :))</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6546" target="_blank">📅 15:11 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6545">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yq0hLToYeUECcuzqiQsrTz45yPWZ7TuVkd-NGNolkOcXfbbfuuXXtMxpL6qhcdT781l8vO3onVlglQaiLoPuHjR9kACru_Wi9bfWPeFh2MjAgwyjdfP2EfKse8AxHvLbHSwZmtHHgGdc34sRWi_7ly0ngQSV0l2_6NLMThVwRJrHW4yTApDw82Q70g4MZ6F0ZeEPZGwo3lF1UMIhH1Ovggh-PEzbvIXogR36REY2dYmD6UOoCHcUcp191rJyOOhGNvethbGgStMELbA19FYpPeAbwbuWX29WQpZXEUvps39BvdDBNzijY9A-eD0C4DdU3SMrKMX4F7cepjxY2zMqZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شارلی ابدو
ایران - اینجا تمام سال
خورشید گرفتگی است.
(عمامه سیاه آخوند که مانع خورشیده
و کشت و کشتاری که پشت این عمامه سیاهه و روزگار خورشید گرفته ایران)</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6545" target="_blank">📅 02:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6544">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‏محسن رضایی دبیر شورای عالی امنیت ملی:
‏آمریکا باید جنگ را پایان دهد، پول‌های مسدود شده ایران را پرداخت کند و جنگ در سراسر منطقه، از جمله لبنان و غزه پایان یابد
‏-شروطی دیگر از طریق واسطه‌ها به آمریکایی‌ها منتقل شده
‏-تا زمانی که همه شرایط ایران برآورده نشود، تنگه هرمز بسته خواهد ماند.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6544" target="_blank">📅 00:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6543">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b8763e605.mp4?token=qzSVY4n7jy51CsQaPhz5tRial4qA4whUEfak9ARLcV_Mxpy8xGKOdHfxo-jFtkU6jSa-xRt82aof7H-mT-iV7Jo6Ta7ORdCI6XfDMbi7SPNVKlX_k8SS2gvUrEcDRM7p3v0sLQSF7H-MK9KIYAmrjs_Whpl9veC9R99cEzHeh27YmLEmnrMPpdCNGmvhjwIII_ulsdsyYsz_Q4A67NeadFxfsRbFxS3PbVPrXcAfCwnBpIEyGmRZUc2SBksGe6aUjCehw68H_NEiajLClEcU73lHKOGiICYaVEdfjgHwzmGZRasKiysBOohKZLWA06PQhwvK95f1vO-7ClK1O41Nug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b8763e605.mp4?token=qzSVY4n7jy51CsQaPhz5tRial4qA4whUEfak9ARLcV_Mxpy8xGKOdHfxo-jFtkU6jSa-xRt82aof7H-mT-iV7Jo6Ta7ORdCI6XfDMbi7SPNVKlX_k8SS2gvUrEcDRM7p3v0sLQSF7H-MK9KIYAmrjs_Whpl9veC9R99cEzHeh27YmLEmnrMPpdCNGmvhjwIII_ulsdsyYsz_Q4A67NeadFxfsRbFxS3PbVPrXcAfCwnBpIEyGmRZUc2SBksGe6aUjCehw68H_NEiajLClEcU73lHKOGiICYaVEdfjgHwzmGZRasKiysBOohKZLWA06PQhwvK95f1vO-7ClK1O41Nug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی ترامپ در ترکیه بود اعلام کرد که با «ایرفورس وان» ترکیه را ترک خواهد کرد.
جلوی دوربین‌ها وارد هواپیما شد،
اما بعد از درپشتی خارج شد و با یک هواپیمای نظامی ترکیه رو ترک کرد!
نگران از تهدیدهای جمهوری اسلامی.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6543" target="_blank">📅 10:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6542">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b31726f423.mp4?token=V26NixDAOVmB2YYwEcDO1w_n1gYAIisHBddZ53fTtq4te66bArhtJQmakzKRiMWDcHxT4vHKxuwlWJyoNhi7eSdjdhOlH-9U6aKlMdmkIFuI1O7WUzG4qySru-TNrQt_JqqM_QovwrgMr58dJUhIdMocvWBRCTFC08an3mnlNIxls6yaxnHoqiN4fzAsk6Uyfxlh9Mytcsj0NbegaAf3K3xHQpUpY9uGRdOmZEsBMwzq08hmNSANfxIHnvv8K6TGatC44lBE_SSgksJGyrJoc7Z3ShfJHHc5ziM9a4--WOK-gH6y-MMvprl82G3Ln22IK59dzs6Xe6bLCcAn5xruIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b31726f423.mp4?token=V26NixDAOVmB2YYwEcDO1w_n1gYAIisHBddZ53fTtq4te66bArhtJQmakzKRiMWDcHxT4vHKxuwlWJyoNhi7eSdjdhOlH-9U6aKlMdmkIFuI1O7WUzG4qySru-TNrQt_JqqM_QovwrgMr58dJUhIdMocvWBRCTFC08an3mnlNIxls6yaxnHoqiN4fzAsk6Uyfxlh9Mytcsj0NbegaAf3K3xHQpUpY9uGRdOmZEsBMwzq08hmNSANfxIHnvv8K6TGatC44lBE_SSgksJGyrJoc7Z3ShfJHHc5ziM9a4--WOK-gH6y-MMvprl82G3Ln22IK59dzs6Xe6bLCcAn5xruIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عضو فاطمیون (نیروی شبه نظامی تحت کنترل سپاه ) در تجمع افغانستانی‌ها در ایران ؛
هر کسی گفت تو افغانی هستی به تو ربطی نداره بزن توی دهنش.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6542" target="_blank">📅 10:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6541">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ترامپ درثروت سوشال و در واکنش به درخواست جمهوری اسلامی برای پرداخت غرامت نوشت: ‏باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران در طول ۵۰ سال گذشته کشته است غرامت پرداخت شود، چه برسد به ۵۲ هزار نفری که در همین پنج ماه اخیر کشته شده‌اند.  ‏</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6541" target="_blank">📅 21:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6540">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QkO8g5sVoRGhJBARz9NkKWjqHnRSNw05EgAvZ40AUm4FF9iIvGhADF4FpmVRNG3cLpq6mzD66-yl7UTf_yV66LAPrGMgkuF6EhioQL3vJCXiZbptg9VNg0RHzVq_t0eUfcYgMu687pNj1Nys01jtfFTa9Yy260nwY2qaUAYayZka3RVhH8NfPWsaIJj3L-jbg-z9GTU5IJD0YL_vfRCsIaR45uwTR3IjiB3cMzJs2YtuHQv0xAYW0gAxVUd1M8-096pgZFMdkSSPEXOAsocdwulTZ62zrlklEXPTuwkRA_X0cgnIEHkocC6_H5Om9pzNKXVfBM-B45Nt6OwNxI5xJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ درثروت سوشال و در واکنش به درخواست جمهوری اسلامی برای پرداخت غرامت نوشت:
‏باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران در طول ۵۰ سال گذشته کشته است غرامت پرداخت شود، چه برسد به ۵۲ هزار نفری که در همین پنج ماه اخیر کشته شده‌اند.
‏</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6540" target="_blank">📅 21:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6539">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIndyPersian</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tzbfIfJVBG5eHvuGEkk3EUXFpAHgtdorrOCu5HVAwVzkxO8mv1QqADUPalsT7lYx5drAEUq6aj6zbI2ynfG6Sd1dtAVBFv4d_L_9hIKkiyhGWh2wWcVIX9M91IzIIuYQrXybG8KjnB1-HgE4hHUd9pCP9hoMKfRB4rcHuG3If1Y1JQ9x9Boti6WkYDJrrNMSiQaN-vcn0XmYOPiVixvA-t7EvRFrlUW6xlPUCH4B7gFVEoaxJ7nqsNFswua6O6p0AfAfJFKO62WDGx38hd8dNsR4oD84RX8KKdNldaqRitPv0b4-Rs7ETm1K4cEoaCfIPM6NWsgM7D5_0bRZjT7A3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مجتبی خامنه‌ای با صدور احکامی جداگانه، شش تن از فرماندهان و مدیران عالی‌رتبه ستاد کل نیروهای مسلح، سپاه پاسداران و سازمان بسیج را منصوب کرد.
بر اساس این احکام، سرلشکر علی عبداللهی پس از کشته شدن سپهبد عبدالرحیم موسوی به ریاست ستاد کل نیروهای مسلح منصوب شد و سرتیپ کیومرث حیدری جانشینی او را بر عهده گرفت. در حکم انتصاب عبداللهی، بر ارتقای آمادگی‌های دفاعی و ادغام ستاد کل با قرارگاه مرکزی خاتم‌الانبیاء تاکید شده است.
همچنین احمد وحیدی با ارتقا به درجه سرلشکری به‌عنوان فرمانده کل سپاه پاسداران و سرلشکر مصطفی ایزدی به سمت جانشین فرمانده کل سپاه منصوب شدند. در بخش دیگری از این احکام، دریادار علی عظمایی به فرماندهی نیروی دریایی سپاه رسید.
در نهایت، حسین طائب نیز پس از کشته شدن غلامرضا سلیمانی، به ریاست سازمان بسیج مستضعفین منصوب شد. «گسترش فرهنگ بسیج، تقویت شبکه اطلاعات مردمی و مقابله با تهدیدات نوین» از مهم‌ترین ماموریت‌های محوله به طائب اعلام شده است.
@indypersian</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6539" target="_blank">📅 20:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6538">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eQ2T3reqIs-wekxGqFJtaiGdYmImDNMfQ_OOTDirBwQmkirbqdclitmQiGVKEwvtCY5VpLd3SuQsFp8j-60NY4LXJcH81hZb2UJc7RZDrQSr5XzhvYaVsOhZSHtlXDyYCl1PoQYn88-GwGTq7nprbP8Vv4iK6F0zCI0EcsVs7MgUb0Le2BImEZ2B9RLs7zOd2gaO4HNRN2Q6Py-IB35j1EtAeezgMe5t1dyKrEkSNV-6MTYYsym-Fa1PZRDr6XLFw-E3KlSR7zZRIXG0hGyUWIP8cq-IzDZiHkcmOBdHDWWs-1Nfg4sEnmAdKdMAZmGkrKA4TeEn0xalSVRgcjdNcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکله بندر عباس
اصلی‌ترین دروازه وارداتی کشور</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6538" target="_blank">📅 12:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6535">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
شرکت ملی نفت ابوظبی از حمله موشکی به یکی از شناورهایش در تنگه هرمز خبر داد.</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/farahmand_alipour/6535" target="_blank">📅 15:47 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6534">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e0455e32a.mp4?token=qkPCZhekZh_EM5nlr5dqAT9_XE6kt7PhiLOxSt7Hw5I_L3DARMA6ZSrxUKQDs1Q5-DIH2e_b5SSaGzuJTWvX6z-WH8wHokOZvA9W5EJoZlpw-SzUCyAn0BWuwE82xh12sBoCjSQdwunkjVwvLxlc1dE16MKc5qvgg7UMHi3f4doB70Tr8jeUlMlIr9fdcgqii_BKvl-lgHXi79zg6a671B1oDoQUeBDBwaGNL6eSJnqTXyfSvTD5voyhax_O1t6mEU4WW9X4_P8mL9JhuaA_44rwYRGZFkphFtiwpkBtAILqufCM8YS07jx_Dsuu_peVQO7ZtyQYCr1TDSmia2vpRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e0455e32a.mp4?token=qkPCZhekZh_EM5nlr5dqAT9_XE6kt7PhiLOxSt7Hw5I_L3DARMA6ZSrxUKQDs1Q5-DIH2e_b5SSaGzuJTWvX6z-WH8wHokOZvA9W5EJoZlpw-SzUCyAn0BWuwE82xh12sBoCjSQdwunkjVwvLxlc1dE16MKc5qvgg7UMHi3f4doB70Tr8jeUlMlIr9fdcgqii_BKvl-lgHXi79zg6a671B1oDoQUeBDBwaGNL6eSJnqTXyfSvTD5voyhax_O1t6mEU4WW9X4_P8mL9JhuaA_44rwYRGZFkphFtiwpkBtAILqufCM8YS07jx_Dsuu_peVQO7ZtyQYCr1TDSmia2vpRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسماعیل کوثری :
‏سردار کوثری: شمخانی برای جلسه فرماندهان در بیت بسیار اصرار کرد
‏سردار رادان جلسه را نیامد و سردار پاکپور هم نمی‌خواست جلسه را بیاید اما دستور شمخانی برای حضور بود؛
‏وزیر دفاع با معاونینش در جلسه حاضر شد؛</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/farahmand_alipour/6534" target="_blank">📅 10:23 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6533">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9163fd2da9.mp4?token=f76yVhF6o0FdNq6-sBbdzwb_6dYE_hropfzheEJ6c7txt9pu-6Gba8vZdLBD2SjZhpatT9GmgWYLa1KmEYUIFKYrmeD6dihoTytbreS0hYqyCtM9J9n35iHubtUvQUR76ZWldsNPb137a5hvWItzryn51lGsF1rEPuAq7_rkapkqetxuajxL6Nth9vX8XXcX1hzvTfoGHfiTOm6ae8vXtn1AI-pi11u5gdohx0eByLNILwFtfSfyZ04HKahnxGRMTdBidiICMroJ_bs_Q-TBWtzvXmGUiPOZmjBaj0obz7ZFoY_YJrRO_xNnZmi4M48psXsj1CjH7pjLqItRJd7Zgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9163fd2da9.mp4?token=f76yVhF6o0FdNq6-sBbdzwb_6dYE_hropfzheEJ6c7txt9pu-6Gba8vZdLBD2SjZhpatT9GmgWYLa1KmEYUIFKYrmeD6dihoTytbreS0hYqyCtM9J9n35iHubtUvQUR76ZWldsNPb137a5hvWItzryn51lGsF1rEPuAq7_rkapkqetxuajxL6Nth9vX8XXcX1hzvTfoGHfiTOm6ae8vXtn1AI-pi11u5gdohx0eByLNILwFtfSfyZ04HKahnxGRMTdBidiICMroJ_bs_Q-TBWtzvXmGUiPOZmjBaj0obz7ZFoY_YJrRO_xNnZmi4M48psXsj1CjH7pjLqItRJd7Zgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجی‌دلیگانی؛ نماینده مجلس:
ما الان جز ۴ ابرقدرت جهانیم. نمیگم چهارمیم؛ شاید حتی دوم‌ باشیم ولی دیگه جز ۴ تاییم و باید توی شورای امنیت حق وتو داشته باشیم!</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/farahmand_alipour/6533" target="_blank">📅 18:01 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6532">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/frEhci4jemGUO6SsiNPRiVC85Oq1mtSAwY9EZBJfOxSLJPI3l4nvzvgKJy7RDCTB7pa3lTiwjJhPVpYGxngZRuhZXDlHz0EWiMVnUbXyZuJ_wFWOe7ELm_fSv1ZA5IFWd7WzZMdc1Cgk-XM84gQAYa5OgjsCZjPSik7x3osXG7aCRcIt6DFV4pK56TMRI5-xAN8p34Nr1NheiyZoJe63agKoh9Tc0z0-cCOo9glDVz9M3tCC9-SNrwziVRZrGkbBkBP7KvVDh5Q0faqboRQ6RrbBZsIuBEQUs6EBjz7jqAEBaZclYDf3OpCRwynV_T_iFFvbbtpDZAq9ZcM_jmrBSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی دیگه از ریشه‌ها هم به این جریان برمیگرده  که پیامبر اسلام از نسل اسماعیله  و یهودیان جملگی از نسل اسحاق!  تمام پیامبران خدا،  یعقوب، یوسف، موسی، هارون، داوود،  سلیمان، عیسی، ایوب، یونس، دانیال،  ذکریا، یحیی و …… همه و همگی از نسل اسحاق هستند! پسر برگزیده…</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/farahmand_alipour/6532" target="_blank">📅 15:14 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6531">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m1Wwxgy_HD7FhQglvGNSY5HEBvrFYafTpU3XScatw_fTpJZ20cPnZ6LYxSx_9nMMa_QeAwQeN3p5bsWsbEA3TADOE05TI41gOgRb-tYeZ4TGSEeJJA5Ey4JwbvErt1S4sdOWXr1ndCbq6jDIqO28EHIVgyJty13OuOucXStnCVtr5ruJ1-Tg51ZY1BY2a4oI-s51_3_ya-Kk-ELL3kGXoshEpk4U60QGV7htfNzRC-YGDlO-y0V07ZtQlgLfGsU8rmbFQfe-y67ZhyDEhnBtc3RZiq8JFQuK3YTFejnMhDbBvI1yldGWhxHCPnTlg1IQrpIMjwNrO1sMhYVD4Jx-Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم در این آیه ۵ سوره قصص، هم در آیه ۱۳۷ سوره اعراف، هر دوبار  قرآن میگه که ما یهودیان و بنی‌اسرائیل رو تسلط دادیم و حاکم کردیم!  . «و آن قومی را که پیوسته به ضعف کشانده می‌شدند، [بنی‌اسرائیل] را وارث مشرق‌ها و مغرب‌های آن سرزمینی کردیم که در آن برکت نهاده…</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6531" target="_blank">📅 15:11 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6530">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">و شاید خیلی براتون جالب باشه که این آیه قرآن  (آیه ۵ سوره قصاص)  که خامنه‌ای برای  خودش  تفسیرش کرد،  در واقع قرآن داره درباره قوم یهود صحبت میکنه!  درباره بنی‌اسرائیل صحبت میکنه!  اینکه اونها رو از ضعف و بردگی در مصر به قدرت رسوند ! و اونها رو تبدیل  به حاکمان…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6530" target="_blank">📅 14:58 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6529">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/el6jcltZo5mKjxnMSOCqQiIDMvHxqmtxdgS-VFnKsRYb_MERQ5sfBeSCitKEsroOnp8nXxXyLSEDB7vC5aZ1ssgUV4-NtnA9ergqEL52b2MrlElKqj3y1PlqumOkXYHxPqinA7PKwnIcS7TrL5EVnCpcTEp218JZ6CKqCDvxc26c3FrH9Ntd3cYXpqmB8_fLd3nYwSVgAYj5kT2lTwZ2t3Uzd2t7dA4d-5UnZRlaGBqedXygpZpluc_y4dAX8NBNrlSeEynbFuCF4EAWm3ECYsC2dZedLsaoBEI7YPCowMWmNyvJQvmPJfI0WiyJS__x2id3PcPdLFwvaa-3Rv9f1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای در سال ۹۸  معنای «مستضعفین» رو هم تغییر داد و مفهومش رو از مردم مستضعف و مورد ظلم واقع شده رو تبدیل به معنای «پشوا و رهبر کشور» تبدیل کرد!  به نوعی گفت «مستضعف» من هستم و اگه میخواید خدمتی به مستضعفین کنید  به من و پسرهام خدمت کنید!  کفت قرآن اینطور…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6529" target="_blank">📅 14:51 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6528">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JnlMIVSZ0JElfK3oR2xdppR2HCyPDvQuqMGasdBOGDwAKcZ3lvyT_IEZhf4XRvJB32EhbY9_VeALH0Lu6wnOm5ykk5PEA11klYOjHRN2OS8M8P9fJudjnIyW-0ZquDzwbml8nYKHyRCx3tfUzG-gB-NxCTF3TsVyp1UweM7_8lxlxce5iUfdUoP61hHME5YxBgzT6D_6FVdh1Xa50VwtcJGKl6T1J2ZZ-7WTRm2x7RLzGhKgVYmYNjQSc6d-kuGeiUzMvIj4z9GqnPuDYepSTwa3JYb51Xg4-5h1XYIt5hLSpiS4cSZMxm92RE6c4u8qPVamceaM2yLAQPzr27VROA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان وقیح جمهوری اسلامی هم به مردم عاصی ایران از فقر و فلاکت کشور  دائم میگن :  شماها بیایید زیر پر و بال فقرای کشور  رو بگیرید، مدرسه و درمانگاه و….. بسازید،  به کودکان یتیم و سالمندان و….. برسید،  تا ما هم بخشی از ثروت‌های ایران رو یا خرج لبنان و فلسطین…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6528" target="_blank">📅 14:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6527">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lqIdjjh8Divv-RJu9DXILvLDWtJMZqMemja1yiLOeN8odix2qNerzlHmL8RqH8-j7oPk41ASYc7uNqFe02Z_Mxb2ZpCWfRZWSuDkLgXeZnQ-_P_NvnAY08aY3y91b2k3AoQiP6loCGv0RO0WAeNliZsYkV2hl7Leu_vTg2L9WrH6aaE2srvBQRKZjbsyQzqUNS3RTGIsicV1jhxWofNBebhoIPxPtIJnJK_7itHT2nLE0ht4nl7PAjpoYq-mZnXSySYZepjJE75kNn4ulEkwR8Gu4oT82wUDZzRt1oFg-V8pQ0l7JKzUnolY9CNwFLnkDvcoBOvuBYJK579B2zizcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اختلاس‌های ۳-۴ میلیارد دلاری!  خودشون  که هر سال یکی از اونها افشا میشه  به کنار!  بیش از ۳۰ میلیارد دلار هم در سرزمین سوریه ریختند و شکستی مفتضحانه هم خوردند و اومدن بیرون!</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6527" target="_blank">📅 14:34 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6524">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jJDvK6fTi40VyvpOa5ju2yUbNDZ6hCux1qMxc0cCU4a0qlgct8AIunjxtIl0bKqT8DLA5hFm9GUwoViWUYkE_ksA5Ijfn8B5zZ20uNluMp3Tfwrf18gmh7hMM9wNpYx4FmSdGb-4rg_4dDEINxvZR-qxOpx3-0FoA7hgufNwGht9RvM6FmoF_fzu1ekJDVfXd_PA5V3hXDW4INmvs9hMdOXW53M1JolqrJnpkyWzXAmBbh90UFm3M8CpfD7lZd6oko_R3JyANzEMlhz3bzXzjGJ2I62RVSedJyndbZo2cnLUrAKeKJsoK73ksFF5au3v-RkdxpC_Yt3o64qXsknIcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q-C7MsUxrBENYuFdaT9xqOBUmHa-8-_M6JvY6FkT2GKPL0L_S16gK58s3w85oC8q6cANPnJLOCelmnxQsnOtF6lJssPBeldSOfv7kzg7LUiYXxvzwnjNx1BN4LWgg0d0mBJr2b8GaPwXRjf96Nv4GiK46djK0asC53p8toA2gtAlsHqQhCYh2bBkqlsIt5eEDL056zO3NU7mX1AF753PY7AigmNfyoSnS3MqJlHG_vvBm-gGiK1LQJTCEu5cc1C_cIeXDPVPUmOTG1S-JLpCseajuztCptT5V3tsyXcflkT1U3uDtIQoZdk3MX673XjZC0AyISpn1pP0r0ATERGy2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KfXkQ-BF9OP8LGzLFo70L85hya5gTdpxFL_lypoTGvOC0M5NxSf0YYF6aSbl2qJBYA6kW0ne9OOaZYTTKBW6ppsSI42kI0aV6boiQmAbcSeFZDc2wW0z4ZZYjF-FQIb2JMM1gPLwAKVq1u_QOs9awJJcHGOsG50BKKrTqZhXR7oYgXfl3Wpl6ZixgeZq25KLjuTuyJcpo9HA6DeS37qd428DujOElLkgeXXp8p_BkQV4TJsCj005nNsPAhU5NLw7gs6qIl7_XBM7A4e6iSEVt-fAk10dynHiAagZDS65-Xe6O92IvU7ZFpQgMl5uSqTzJmzdV_zfEEytJnDgnQsZDw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خیرین مدرسه ساز در ایران،  ۶۲٪ از مسئولیت ساخت و ساز مدرسه  رو به عهده گرفتند. حدود هزار مدرسه.  فرض بگیریم همه اینها مدارس ۶ کلاسه هستند (برخی ها فقط ۲ کلاسه هستند)  اگه هر مدرسه ۶ کلاسه حدود ۱۲ میلیارد تومن هزینه داشته باشه، هزار تا از این مدرسه‌ها میشه…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6524" target="_blank">📅 14:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6523">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hS3zdNQYMJrlBOoL_VWmEYYq33k4i5-9C_EksMswnw3gxWgB0zNyEm4iA5G00HmjlVOuo7uAGm69BW_CL3W1CG8R4wzTkYAC9bcBg_YZ_BehZdQ2t2n8ZcholtbVy-Ti0b13q3Caf6oJgnDal1y3oN9SiEsfJHlXWCHD-MFoILbrCEdFCS9ywsTMZA9MqP1Kw9Y5IqRC3N7lDchEoUuxSP0IbwPiaEt7yZOpT757s0aEabLoaueSzthhO1X-qc6Jds57sdiLNGgOhA9VBpBwSsRh8tYnaL50HLwehww1NT3bm2zk0n5p-6V7bR2EzsFfped9mV7s3jxc9ntiR1zK_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لطفا این متن با دقت بخونید و قضاوت کنید:    پدر یک خانواده،  نیمی از درآمدش رو صرف مواد مخدر میکنه،  موضوعی که باعث فشار  و فقر در داخل خونه شده.  مادر خانواده ، چون بعد از اجاره و….  پولی براش نمی‌مونه، معمولا از بقیه کمک میگیره که پول پیاز و سیب زمینی و…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6523" target="_blank">📅 14:26 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6522">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">لطفا این متن با دقت بخونید
و قضاوت کنید:
پدر یک خانواده،
نیمی از درآمدش رو صرف مواد مخدر میکنه،
موضوعی که باعث فشار
و فقر در داخل خونه شده.
مادر خانواده ، چون بعد از اجاره و….
پولی براش نمی‌مونه،
معمولا از بقیه کمک میگیره
که پول پیاز و سیب زمینی و قبض آب و برق رو بده  برای سیر کردم شکم بچه‌ها و…..
هر روز هم دعواست که اگه پدر اعتیاد رو ترک کنه، هم پول بیشتری در خونه می‌مونه، هم کار آبرودارتری پیدا میکنه و پول بیشتری در میاره،
هم خانواده از این فشار و تلخی.
🔺
حالا سوال : به نظر شما افرادی
که به این خانم کمک می‌کنند، دارند کار خیر می‌کنند در سیر کردن شکم این بچه‌ها، یا دارند مسئولیت رو از دوش پدر بر میدارن،
و اون هم با فراغ بال بیشتر، با شنیدن غرهای کمتر، پول خرج اعتیادش میکنه
و در واقع کمک هست به پدر ناشایست؟</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6522" target="_blank">📅 14:19 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6521">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b591219d1e.mp4?token=qrgMGXrkU3pSE6kRbLXQxfWSi4d0ziH29CFbMD7Xu5m68gILUrtgrDm7wLLSEQuO2k1aJ0llIQABon_I9WOa2IVOPr1CuoDg8CDDVODuQkjjFDNdsPttH-kAKSoQNt4AVkzmKqq3Y99PNogtvpVlhYNgMkv2kcYsgzrxvi0_nyhjQEJ3dhaWyBd5xR1AUbum9CzqDRTijbCycm9N8ljyMDLe1J6ZQdkMSDYw7wMS7mtUDNt9wipn-hOnTXP6XvTFJL-HfSQXVHnnUkz4MPw02Cph3F6Fje8Ne2sw04djHu-RZECNr6Q7LNldbdMGQKIID1B_YO5Cs2hEAkrUNfbB7oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b591219d1e.mp4?token=qrgMGXrkU3pSE6kRbLXQxfWSi4d0ziH29CFbMD7Xu5m68gILUrtgrDm7wLLSEQuO2k1aJ0llIQABon_I9WOa2IVOPr1CuoDg8CDDVODuQkjjFDNdsPttH-kAKSoQNt4AVkzmKqq3Y99PNogtvpVlhYNgMkv2kcYsgzrxvi0_nyhjQEJ3dhaWyBd5xR1AUbum9CzqDRTijbCycm9N8ljyMDLe1J6ZQdkMSDYw7wMS7mtUDNt9wipn-hOnTXP6XvTFJL-HfSQXVHnnUkz4MPw02Cph3F6Fje8Ne2sw04djHu-RZECNr6Q7LNldbdMGQKIID1B_YO5Cs2hEAkrUNfbB7oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏رجب صفروف، عضو تیم روسیه در مذاکرات رژیم حقوقی دریای خزر، مرداد ۹۷:
‏همه ما انتظار داشتیم ایران درخواست ۵۰ درصد بکند. قانونی هم بود. اما جلسه اول یکباره جمهوری اسلامی گفت تقسیم برابر بین ۵ کشور، یعنی کمتر از ۲۰درصد
‏برای ما عجیب‌وغریب بود که چجور ایران دارد از حقوق خودش گذشت می‌کند
‏این برای بقیه کشورها مثل هدیه الهی بود. از خوشحالی نمی‌دانستند چکار کنند</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6521" target="_blank">📅 13:33 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6520">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fO79-A3ny5lxOkyGwN6GMwBfzjO0L6FwRHG7mCiZ4TflOqRgLQgktuCnZrdd9zJ-jUsmZJ7Ey-2P-BFJUGe7YAcAzVGzGnsaBZxckk78D8gUsC-FlX4dOSpE93wNHdLJGNQm9Sui0FwP8OSctpOAAXmaUILegoLfabvfLiR-9ZFgO4RBchxilttUfAC5ahQlsUSCxAUtR_nQqvQunj6_7tSyxkSFcZRGBxS4usdLFgc3DCexNv4nlYg8yhTbUa2Dc6J7VJ76IusLUshTM3NhhueHwhlC0dITN1rSGttZbl14Sm2f0MJrZsw3sgj7ucOZqNxT0Bmc0UtGxdKBExPwFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی به عنوان رئیس شورای عالی امنیت منصوب شد.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6520" target="_blank">📅 22:34 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6519">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q86fazjFhFADyx3f-Fgr0O1XqCbsFSRhOs0ewmwSxrNIMsl8LVAtQdVpY5ddXg8pNphAx8_YuA7M8a6SW4ISZsL9Us7rKlcrsnQcUfpr_9AAMg0_foFuraL7W3WupMKMGsFVZYPon3F6iUzbdsEcOIoTj7P9hGTPqy-86QV25_4oZvCzN9SRXAZrfAjdebysmHLqXffCSMlAMLm5b0B2ROmnbu2xfTQdjHzcDwX55Bx86KxP_hJnEiIaMNPPngg0sWDgc3Z_DO-78pD-itjNLazYr3w8fT9RBl5plJ1Gud10h1l5_6MDGK-yOCdCYEY2hVE66uCu5BGIuMYIZHU8zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«حمله‌ای گسترده در راه است…
نه، صبر کنید، می‌خواهند مذاکره کنند.»
این یعنی «دیپلماسی نمایشی»
که مدام در حال تکرار است.
استفاده از زورگویی، وعده‌های شکسته
و اخبار جعلی به‌عنوان ابزار فشار،
راهبردی شکست‌خورده است.
واقعیت‌ها را بپذیرید و به تعهدات خود عمل کنید.  ما به نمایش‌های بیشتری نیاز نداریم.
- فهمیدن حمله به کشتی‌ها و زدن زیر تفاهم‌نامه نمی‌تونه براشون دستاوردی داشته باشه ، از ترامپ میخوان که مذاکره کنند.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6519" target="_blank">📅 22:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6518">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HveGiTAm2lj-5BjA1tbdGhnEtYFHcOfn9-clEiXqHFqDcuVAqBYd_TqbuEEhbKZtE9y_QUjsoy0uFiPUuOytlztJrz2YZeJSFQeuQB-GVgqVF4Y_tuIuaD1tLcJcsDp0bNVEN7RU_Y5e-FhYH9T-KOVdEy3EeyDyovb6NdGKQEluCyivnuZXEwMe4lkVEPF2QsD5MQZRMVGTGlLaqrqKlMmlrhSgpBH5_r9bN6lJ4oeqL_oKC-eo5xPwfKQ6rqx9HCoW7AFcZVIY4poUqR5WqXtf1ABUEd4nU4zeKV9PUEW2f862jppPnJcpPHFQyDFcV6T9CWgdyTV_VXVthfUkSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به امید بالا رفتن قیمت نفت و فشار به ترامپ، زد زیر تفاهم نامه  و حمله به کشتی‌ها،  که با اقدام به موقع دوستان خودشون  در حزب کمونیست چین،  نقشه‌هاشون نقش بر آب شد!  خدایا عظمتت رو شکر!  اما در عوض برنامه آمریکا در پاسخ  به اقدام جمهوری اسلامی…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6518" target="_blank">📅 15:31 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6517">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UvsfjSrRmSm0FmkwT0sGqQUJhcL6aA7NE46s53ZW_RP3OoyJqVdvNACIi_gkmbdVnuzHdvfc-q-UC9U9-0z4e6be6zOlVdQRg0GFFC0YTpNboGTzLtKm-pHTnk-ARYa4iH22QT4pY1j-apc6fi24aoTOdUhac-cc5wIMd8iD-P1zEBErdQgNT3UmN4TiowfV_Hv2LLWb3-n_jA9xvwHvDF_5u6a_9cAjRKZOQhXFWipKilGCB6YnBHSELsk74JHjPjp6QGc1jbkdbTdIxIhZaS5rAErOlTwMsg7kWmbIB6rJOX4mUv4Mv8nhOFosdcOS6m0ef1UNSLRpUBEPUHlTwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته دوم : افزایش تولید نفت کشورهایی چون امریکا (که رکورد تا یخی زد)، کانادا،  برزیل، قزاقستان، ونزوئلا و….. است!  نکته سوم ترامپ!  و به نحوه مدیریت ترامپ برمیگرده!  بازار نفت به شدت حساسه به اخبار  و به انفجار و ناامنی و جنگ و…..!  خیلی وقت‌ها قیمتش «روانی»…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6517" target="_blank">📅 15:24 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6516">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T7nwFP0HOY0D_e5NP0QePAelbCmL1RdKs-DHEl1CdJGtOdqGC_PySY5OiaVzqjnDBDNvVpSqwJQYiwTnUh08qmhou-dDFJjkr2UYy31Piqc2CI6jKysLNF6Lu1BGZRvTs7nDl0EHIw17sL0euWVwfDPLYyJYgwsJGYyFBPsrA7rEfBGis_P5zTkcw1LzZtcnpkWtcQpUWaDwAV43elDrPvN-lMk9VK0Z10SgCd1MKhnedlgCgZ81FCpckPYvA1fWrGmqn6r9CxOkDXUL2ZMb0BCm9_3v3oLWzWyDWbSBWgDVtA3N1WAS8In1j2iIbhM8sQ-fUxP8Zl9-H2RRNhpPIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برخلاف نقشه‌ها و آرزوهای جمهوری اسلامی  قیمت نفت خیلی زیاد بالا نرفت!!  میانگین قیمت نفت در ماه اخیر با اینکه هر روز خبر حمله به کشتی‌ها رو منتشر میکنن، اما بین ۷۸-۸۰ دلار باقی موند!  یکی از مهم‌ترین دلایل اینکه قیمت نفت خیلی بابا نکشید دقیقا  «چین» بود! …</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6516" target="_blank">📅 15:17 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6514">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u4JCgMStIop1Jil94sEomfIEUDmjKch-whavhK5w98qlUI9QxlMJJMBn5E6qQgpTUIdyHH0GmjGB-Vm9WR1AX2L4cnMIUQe84fdpXH9Wc9LCUeDeJpPE8TCfIA8BMRLKA86MhouLTLcQNJA2ZtpGE3NSwm7H8JB7wrK8S5dLmCuTKPiwlpWN0J5-EDLQBGJyIb6amab8AyA9Pgwt6DtQy_-iiLYSzvtAR9cx_p3suC2xibuxvZ-mShTmsnsH1MT4BSNGN3RZuLu-oo6XTOeQRwsKaoqwhtm9M35529L9cOjQWhsr8cw5b0wV0u6w76bCPheWUwZqlaUjlkPXg4gh0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/haf8U9xgEWcYmtsy5bfmPIOZI3twSTYZlCxmJ3uJm6puv-BQUGpj19k5qE0vny8JvSJDKwltD8gsMI7DLnOBhHCITxJJ-RWCck2LQub3A_VqvnJ1kUUMP9A2M9QIsTfGCIahbiqk8jiDDilvY-7iskKK_-fwrUgHlJQ_lg9yhjMTwT0XtZZdX_suaNtbfM-RP50eFLv8bj9fr6nm0NcyJVj-ePojbyDRSUZByG20274KjfVYcp_NJ3E7Ms0YQ0WpWOvD-CjeVJhvjIbcHqKyV8l7hLvSrRRBTPzxX7U1E2yD3htL0hseaFaIcPtIg8j5p3MHHnUQHQ9T4eOBjde8iQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جمهوری اسلامی با امید به اینکه با حمله  به کشتی‌ها و کنار گذاشتن تفاهم نامه،  می‌تونه قیمت نفت رو ببره بالا و بر انتخابات داخلی آمریکا تاثیر بگذاره،  حمله به کشتی‌ها رو شروع کرد.  تا با ارسال پیام  «نا امن بودن» تنگه،  قیمت نفت رو به شدت ببره بالا،   حالا…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6514" target="_blank">📅 15:08 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6513">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">اینو ببینید تا یک نکته خدمتتون بگم.  اینها دنبال «اتفاق مبارک» افزایش قیمت  نفت در بازارهای جهانی هستند برای فشار به آمریکا و ترامپ.  اساسا با همین منظور شروع به حمله  به کشتی‌ها کردن …..</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6513" target="_blank">📅 15:02 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6512">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07b72cf9ab.mp4?token=I8fV_OWAnUNoTn2com5sF-JSNDv7MHhtP-8JuNpyPDCvakmp4DEnEZs9HwMNBM2_rlHZPXhswaGUhTfZXpheNdOsIPha0giY2ItdRzqlhg8W9SkbtyoasEkik4qtlg0_9aT1lZ_K4eFH75ObViCJj4Lbo-d_kUYsafrMom42yGovlMsFqDwOmLkVRU2m513tREKb9xy9PSQC5rkpvLEQWdUmgzWxD6JU12r54EOnIk4fPmtRG28VJGXhYH-uPOsFdl-dTY8xwX2UyWY-msN1uRTBDbVm5uOiUU80usFt-cYMLxmsKtQKIHn0iDbNjOqZ6I2fpvBpzVpc7YgTJ8ZUyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07b72cf9ab.mp4?token=I8fV_OWAnUNoTn2com5sF-JSNDv7MHhtP-8JuNpyPDCvakmp4DEnEZs9HwMNBM2_rlHZPXhswaGUhTfZXpheNdOsIPha0giY2ItdRzqlhg8W9SkbtyoasEkik4qtlg0_9aT1lZ_K4eFH75ObViCJj4Lbo-d_kUYsafrMom42yGovlMsFqDwOmLkVRU2m513tREKb9xy9PSQC5rkpvLEQWdUmgzWxD6JU12r54EOnIk4fPmtRG28VJGXhYH-uPOsFdl-dTY8xwX2UyWY-msN1uRTBDbVm5uOiUU80usFt-cYMLxmsKtQKIHn0iDbNjOqZ6I2fpvBpzVpc7YgTJ8ZUyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینو ببینید تا یک نکته خدمتتون بگم.
اینها دنبال «اتفاق مبارک» افزایش قیمت
نفت در بازارهای جهانی هستند برای فشار به آمریکا و ترامپ.
اساسا با همین منظور شروع به حمله
به کشتی‌ها کردن …..</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6512" target="_blank">📅 14:50 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6511">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">محمدباقر خرازی، دبیرکل حزب‌الله ایران، در اظهاراتی درباره مجتبی خامنه‌ای گفت تفکرات رهبر کنونی جمهوری اسلامی «خیلی تندتر از پدرش» است.   خرازی افزود سال‌هاست با مجتبی خامنه‌ای رفاقت نزدیک دارد و جلسات خصوصی بسیاری با او داشته است.   او همچنین با اشاره به اعتراض‌ها…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6511" target="_blank">📅 14:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6510">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/effee93ecf.mp4?token=E3sHn9y5RXAsd9HYLTThSXv56L3Gpb1ju-UZqKY7CYbtMBxDulRQfnDOne0vBPD18LTWxsmsuStPCgy1oz5SU_iQofNX6zKewejPubCnw62W7RDh5xLvLOB0SWSCmp4hVcjI4rt6vxN3L4mpthalcAF2TR7mxEsu8BRPlklas4QcoMQip0KkdxOHbuLGYQ9T0MOumbylOwk2a00_s3DI7MgJQg5SpGkWArp_uZtTQdG4xtHf90dNUlLqcCA3YM1EtrI6sV7BYge4WIOrWyMTlDpW0y_FfQb0Qo96gUSDR2XvKWvJKdh8YikAIqXU0RgBwlNg6THfSoN8If73dJoHAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/effee93ecf.mp4?token=E3sHn9y5RXAsd9HYLTThSXv56L3Gpb1ju-UZqKY7CYbtMBxDulRQfnDOne0vBPD18LTWxsmsuStPCgy1oz5SU_iQofNX6zKewejPubCnw62W7RDh5xLvLOB0SWSCmp4hVcjI4rt6vxN3L4mpthalcAF2TR7mxEsu8BRPlklas4QcoMQip0KkdxOHbuLGYQ9T0MOumbylOwk2a00_s3DI7MgJQg5SpGkWArp_uZtTQdG4xtHf90dNUlLqcCA3YM1EtrI6sV7BYge4WIOrWyMTlDpW0y_FfQb0Qo96gUSDR2XvKWvJKdh8YikAIqXU0RgBwlNg6THfSoN8If73dJoHAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر خرازی، دبیرکل حزب‌الله ایران، در اظهاراتی درباره مجتبی خامنه‌ای گفت تفکرات رهبر کنونی جمهوری اسلامی «خیلی تندتر از پدرش» است.
خرازی افزود سال‌هاست با مجتبی خامنه‌ای رفاقت نزدیک دارد و جلسات خصوصی بسیاری با او داشته است.
او همچنین با اشاره به اعتراض‌ها و تجمع‌های خیابانی گفت دولت مسعود پزشکیان به پایان دوره خود نخواهد رسید.
@iranintltv</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6510" target="_blank">📅 14:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6509">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LFUBPJh6HXJgcYoouw_H-v1wJI3kJnXfSEB75kC-EogROvPxhZKeL9kXhpb99vP0u8SZMKlFSVPHMHo_R6QbOFVcF5YQu05jUQkCsvDB6Yxe9dKzCqMqQiKASVXJPn_a0Zgi_ylIAsUKjmmzKTsOAZyxHilaZjUErRmVAv6VJdV94yNF_NTZkYQ4iqPMfJQ7nfQDrZBSIuOfEWSZ-qSA97xcc-nAeYotqWZP9MYmflNqlhYO52P8spUPod6fZiPQn4yZPvtuIIONnScvQjjNzuxdQBKI3ExAbxK-Mvx4MeXki7uW15h5YUXPyjcZL_mRj2-114NSUeUqkmLleS4J0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب PD که همون نسخه حزب دمکرات آمریکا در ایتالیاست،  هم چند هفته پیش، چند مسلمان بنگلادشی  را به عنوان نامزد خود برای پارلمان ایتالیا  در ونیز انتخاب کرد!!  که آشکارا شعارهای اسلامگرایانه هم میدن!!  مشکل ملیت و مذهب این افراد نیست!  مشکل اینه که اینها آشکار…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6509" target="_blank">📅 12:41 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6508">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YsVhCZfU-dR6JoX0nKu8fuxYY_PXTZ4n1mZKOQef54K4iZ8pqUlA2WLgoZqGuSLcwORRaq7U0LqhIC-28j_P-fIRZYChnRgTDQSgbWeEQJ5Md5fAI75CLyZfWc-8Bz9vel_Cv2_TouBEy0fgVJu37ola8lpEA9LiniEjMXoWfm56jnMmEHhmkChbMjMNqVMiq9NMm18g3OAx8uVxuE_J1nmYMga5Q3ynVWtlM16U3iTGmROrSHpiF0p_nQskuMciYkMTHrp2Q17OTmR-FqpJeX9iamMc-d79YuZ145-jcWBQSkmQRdvABzdN6ytX7X_JY_ReSNwc-AUWZdw3t609fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«عبدال السید» سوسیالیست مسلمان!  که حزب دمکرات اون رو نماینده خودش کرده در میشیگان و انتخابات مقدماتی پیروز شده و در یک قدمی ورود به سنای آمریکاست!</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6508" target="_blank">📅 12:37 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6507">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6e410a5f8.mp4?token=ZqAKA_13wwmWbPTAy3V19E3ei1raYSeeYDcVTOMAVT--K-s9GE90iFiXXimzKhJk2NCvog00RvoBsQtaeYVgs3KUg1kB6cCN0B6kwujJiaXQeq7bHu5jbcZC7r98hi9S9R-L_haZPV9RyAil1TQZNsYpTmYKsnOlu-csFSjDhYY62-bowKizLxRnyINdE8DoeDpF6NgHttMujQ7nCNpErndrwEp1NmP0NLYtHvb2b23IS_M8Rd_S4OEuAmhBvplkf2wkPKdEzRyIrBmLI-lHgDtwG54bKGosBWqFDcH-9pH4-KhKh3fqS1gngTT49ehZfJoS_g2LbTiGfF9IUFS0YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6e410a5f8.mp4?token=ZqAKA_13wwmWbPTAy3V19E3ei1raYSeeYDcVTOMAVT--K-s9GE90iFiXXimzKhJk2NCvog00RvoBsQtaeYVgs3KUg1kB6cCN0B6kwujJiaXQeq7bHu5jbcZC7r98hi9S9R-L_haZPV9RyAil1TQZNsYpTmYKsnOlu-csFSjDhYY62-bowKizLxRnyINdE8DoeDpF6NgHttMujQ7nCNpErndrwEp1NmP0NLYtHvb2b23IS_M8Rd_S4OEuAmhBvplkf2wkPKdEzRyIrBmLI-lHgDtwG54bKGosBWqFDcH-9pH4-KhKh3fqS1gngTT49ehZfJoS_g2LbTiGfF9IUFS0YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«عبدال السید» سوسیالیست مسلمان!
که حزب دمکرات اون رو نماینده خودش کرده در میشیگان و انتخابات مقدماتی پیروز شده
و در یک قدمی ورود به سنای آمریکاست!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6507" target="_blank">📅 12:34 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6506">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">محمد باقر خرازی ، برادر همسر مسعود خامنه‌ای : پزشکیان ۲۸ بار استعفا داده و دیگه «کاسه کوزه‌اش رو جمع کرد»</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6506" target="_blank">📅 08:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6505">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MCNb89AzNqNEX_Piul-zxPgcJxlu86xjYuG9-0JwydBlNRBFtDkgZZA3_OuT0FCh2lxM3PAliQr2mK-oxkul5p4FTBN9A2DOE2WYpN-VVPwa1JmE_4JE5oEC9ya3MtFKQhdnBMUmu3KXWKys86Z3M3VVzjLDgactWlh9H_2lB9PdmOOdZyUfv1P0OPxDox2YAGCkPPLzGKV6H9CkSD7As6sYtIM5pbFyxS9rHpI0avYs7ZJPVnYjtwgCc0Q3oUhT_j-VNWwCmEI1VAZ4jv7OF9ZWiTcTyj7QNM_nUV-RYU1yEJ-wDXN-NBqslgQpMMuFgcxQys5UEbOT9UWe0ASqBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توطئه است!</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6505" target="_blank">📅 01:23 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6504">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">آسوشیتدپرس: مذاکره‌کنندگان ایران و عمان پیش‌نویس توافق درباره تنگه هرمز را نهایی کرده‌اند؛ اقدامی که می‌تواند یک نقطه عطف احتمالی در بن‌بست مربوط به این مسیر حیاتی نفتی و کشتیرانی باشد.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6504" target="_blank">📅 17:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6503">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBBCPersian</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PK9dMARaI-DwknuU9qJCnUQY80WJKnLNuUBWE0bYbNjh5q2Z9Z0jp1sqlwxLEHcBtdPfM5FLcop-MVHPPRmL6YXW9F0xwJYqDhpvCq6ZgNufPQ9E6OtwnJQZQxurfYZQfhGv23O_UNGuYki11ccjWkPX1mTc-Nea7g-s9g81xMSjLpGQHM9qSMPtyiJ-OWDzMhxYF6s6SU8sHkNe4ZmyKYpjZmQN45GAP61gpkE2qpYV9HXufN5omu9qZ8jSGJv7YBFfHWlFZcWKxcVlcft08nOwyPIfdKtEJygalj0xpWhHGlf0-A9LPf3WdR6Vnq19_1N3C-FITrmfSTE6V9va1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔻
سازمان عملیات تجارت دریایی بریتانیا می‌گوید یک گزارش باتاخیر از یک کشتی در فاصله ۹ مایل دریایی (تقریبا ۱۶ کیلومتر) از بندر «مخا» در یمن دریافت کرده است.
بنابر این گزارش، یک شهپاد به این کشتی در دریای سرخ برخورد کرد و باعث آتش‌سوزی شد اما خدمه و کارکنان همگی سالم هستند و نجات یافته‌اند.
به گفته این سازمان این کشتی اکنون غرق شده است.
جزئیات بیشتری منتشر نشده است. ساعاتی پیش حوثی‌های یمن که همسو با ایران هستند، اعلام کردند که با موشک بالستیک به یک نفتکش سعودی در دریای سرخ حمله کرده‌اند.
این هشتمین شناوری بود که از زمان آغاز محاصره دریایی علیه عربستان سعودی هدف قرار گرفته است.
سخنگوی نظامی حوثی‌ها به زمان حمله اشاره نکرد.
📷
Getty
@BBCPersian</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6503" target="_blank">📅 16:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6502">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f29785e012.mp4?token=IVRaEF-rRkR7aroPzXf4dzzG7tpf0SRl33S-nS5J1vM8-4VqAURLTIkltgkfkNBiP46nb7GMhahJ8aOUoHBo7zsM8edepn0_j00pLzEx3H3zYmOF9XyiXvFm5IEEQS55ZDBuI-SbOtRu2I1qR7MPDBTIh8l_FWgN7pQ_aFHbyFAWh9VUvuAbxP0UFV3W7yzYrU4NaKNs2XawKlvrxrhYsJoFwuPNui5G8QaLOOK4aWXx4Wyzw9Nqtarvw-BFrfWtlqpDlOeEaN14Nd-G1WmFh24nB0ZHMH5zv8T0-cgt3OH4U-nSxA3oamviTBxR6vZsplddfTaORb8sUUmGzitFkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f29785e012.mp4?token=IVRaEF-rRkR7aroPzXf4dzzG7tpf0SRl33S-nS5J1vM8-4VqAURLTIkltgkfkNBiP46nb7GMhahJ8aOUoHBo7zsM8edepn0_j00pLzEx3H3zYmOF9XyiXvFm5IEEQS55ZDBuI-SbOtRu2I1qR7MPDBTIh8l_FWgN7pQ_aFHbyFAWh9VUvuAbxP0UFV3W7yzYrU4NaKNs2XawKlvrxrhYsJoFwuPNui5G8QaLOOK4aWXx4Wyzw9Nqtarvw-BFrfWtlqpDlOeEaN14Nd-G1WmFh24nB0ZHMH5zv8T0-cgt3OH4U-nSxA3oamviTBxR6vZsplddfTaORb8sUUmGzitFkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بر اثر یک انفجار در جنوب لبنان ۲ سرباز ارتش اسرائیل کشته و ۷ تن زخمی شدند،
ارتش اسرائیل دست به حملات توپخانه‌ای زد
و سپس دستور تخلیه فوری روستای المنصورن را صادر کرد.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6502" target="_blank">📅 16:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6501">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2a5730f1c.mp4?token=n9cZCk94Bjgq6di87qI3JF9c-vbCnsisTQzzjSbP_YyBFkwW0hiUEQenI48CsksR2k7-AQ1u9sNVvjP25aUBv0-IgeHI3b1s8nosZynwbCV9zd5B9NPqUj0myttSKE-kFNF3mFlCY_0Z3EAC3b3SaYZDQYLAK-n5qyhJUhmWFdv8Q_-SG-Jx8gT_NEUtBBJVKGOLrgBQCvjsro_hqbJSmO3bou8HtRmrp0ps3n13hkVa9eEA4Vr1lD905GUosU_Jlz8PyoLmxvVSnYGzcOxXlwV9SMeQhJ7oT0ZbVKrp2jDUnmt6eArzjx87S9CLll9oD-bgNueqR0U5-WhuxhJetg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2a5730f1c.mp4?token=n9cZCk94Bjgq6di87qI3JF9c-vbCnsisTQzzjSbP_YyBFkwW0hiUEQenI48CsksR2k7-AQ1u9sNVvjP25aUBv0-IgeHI3b1s8nosZynwbCV9zd5B9NPqUj0myttSKE-kFNF3mFlCY_0Z3EAC3b3SaYZDQYLAK-n5qyhJUhmWFdv8Q_-SG-Jx8gT_NEUtBBJVKGOLrgBQCvjsro_hqbJSmO3bou8HtRmrp0ps3n13hkVa9eEA4Vr1lD905GUosU_Jlz8PyoLmxvVSnYGzcOxXlwV9SMeQhJ7oT0ZbVKrp2jDUnmt6eArzjx87S9CLll9oD-bgNueqR0U5-WhuxhJetg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیلی منطقی بود!</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6501" target="_blank">📅 12:11 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6500">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5ac92640d.mp4?token=aZ0qzdOv03FxTOT0f_78VQYuNSJtgLdG2zyLsjy4cwXHmRw8Z2dhtmyj7woXluZR3h-tl9uWXdSAsgcEWHRj80Y0akhQ2VzKpJpXW4_GKeXzbboq4XVlUvAbM8oMvepIAmmJ_mxGaKL1q_TOC_17DF-_y5GfMKd9Ph1QtACVOgXM_qTYJZ4rqVUV9koWFk_8XsN2dxx1OVADLvYHasnr-V1hE0rAPa2_5vJLAYa_o5Ppq8v1CRBJojbQqQbf76aNR5lm7B-QvQ-9lHI3-XUbWSUf1lSYVVCB8a7Mq1O41-ktPkhOILCwaY950V2_Pf8y_NUNzE8CewtqDiPvnInNkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5ac92640d.mp4?token=aZ0qzdOv03FxTOT0f_78VQYuNSJtgLdG2zyLsjy4cwXHmRw8Z2dhtmyj7woXluZR3h-tl9uWXdSAsgcEWHRj80Y0akhQ2VzKpJpXW4_GKeXzbboq4XVlUvAbM8oMvepIAmmJ_mxGaKL1q_TOC_17DF-_y5GfMKd9Ph1QtACVOgXM_qTYJZ4rqVUV9koWFk_8XsN2dxx1OVADLvYHasnr-V1hE0rAPa2_5vJLAYa_o5Ppq8v1CRBJojbQqQbf76aNR5lm7B-QvQ-9lHI3-XUbWSUf1lSYVVCB8a7Mq1O41-ktPkhOILCwaY950V2_Pf8y_NUNzE8CewtqDiPvnInNkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عمان مخالف اینه که از کشتی‌های  عبوری عوارضی گرفته بشه،  جمهوری اسلامی چند هفته است عمان رو گذاشته زیر فشار که باید بیایی با هم این کار رو انجام بدیم!  عمان گفت : تو توی بخش خودت اعمال کن!  در آب‌های سرزمینی من، رایگان خواهد بود!  که خب جمهوری اسلامی فهمید…</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6500" target="_blank">📅 18:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6499">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lnPzD8eYfAhy9NqD1PcOrODKSMCu1eHezwoGrYFA_lsXafl2ceQaqtfXoj7ZC2C6tpxNRthKOVbsIuWGQ16CY1poykiqZVKX6SqF8eiV4t5eQbjXuUzCmqLnyAzf7h-1Y_sJ_n0GlsDs6TlC27o80VsnqgvUL7DyjpFOVbaq87ftAJ-UqQuWO2yJTT6lZcWKFBUKtrMEB3Q8ZYcYAv4LUM4NbGmPzsUPQRuDsNV06s2hYke68OQNGdyOk_LfoeEu_qKZvCDQuZy1de5eGA4OR80AomdsikjV27R7LETsT3-zJS1tJcm5SZfeEtVbB1ZZp8ntFOBtTufbVqtWCvElJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کار انتقال گاز از ترکمنستان به پاکستان  و هند که چند سالی متوقف شده بود،  دوباره با شدت شروع شد.  کار انتقال گاز ترکمنستان از طریق دریای خزر به آذربایجان و ارسال به اروپا در دستور اقدام قرار گرفته.  قزاقستان هم در حال احداث یک خط لوله انتقال نفت مستقیم به…</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6499" target="_blank">📅 17:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6498">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lFOcin3cqdmKHXKHmi7zY4w0LT0Zmf1ztA29g3ePW-H4NhMJHdkYBC2X7apIXKq-acw9lVq3izoGt40vd3Ino3Q7-Z06vfSeofvrhJD3gjYMO3JrJoU-b7F1lk9LVjHYzLZzt_nuGs78VM-APRigia-6ofsnnMWJ2AvC9nxRpQqRUmN4MvpN-_lSn7z5od7n_lTY4LpUeERgIf0idWeTWq6B_CEXuygHseHXWDtus999byiN71xKlkIFXRAm0F0zPTTnbW3ZiaEpAaZoAsasMgyisMqirKyNXnpBf_rHElcw28habAL6x_LL87YJDVvT5jVtYMO7SyOgOW40fRCRGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه‌های بزرگی که کشورهای عربی برای دور زدن همیشگی تنگه هرمز در دست احداث دارند.  عراق : از طریق خط لوله انتقال نفت به ترکیه  کویت : خط لوله به عراق و ترکیه و همچنین به عربستان بحرین : از طریق خاک عربستان و‌دریای سرخ   عربستان : صادرات از طریق سواحلش در…</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6498" target="_blank">📅 17:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6497">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JP5fHw66akRvP74cilRlOP56hT1tpyj6reaqYVzbkzSouG8i7oGwy5JCh9b5OhVHkphyFiotEUtfadjroyUm5-y4BObUGFQXb8o2_H6fiQ6wgse5u1_CGUAYJs7p1vIz_IlazmgEFCAGT5dqUG7bW0kaRvuS0pNonJqucHNtlpqgHZ3Kvx1i4lzlAORvUgdVV6shtTJQ40eH1PYbpL6KHzIU-27zQLx2-qHPfZoDOgpVMa0EuQEeaHjWxvFV-8NPUROXJccfjrGavYmyjDn34ePQWBABnNDNAXpxXeO3vsf_ryY5zCO0JTmN1y2NePq8I6UUnVa53qqonXWlBZ20AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه‌های بزرگی که کشورهای عربی برای دور زدن همیشگی تنگه هرمز در دست احداث دارند.
عراق : از طریق خط لوله انتقال نفت به ترکیه
کویت : خط لوله به عراق و ترکیه و همچنین به عربستان
بحرین : از طریق خاک عربستان و‌دریای سرخ
عربستان : صادرات از طریق سواحلش در دریای سرخ
(همین الان هم ۷۰٪ صادرات عربستان از دریای سرخه)
امارات : دور زدن تنگه و صادرات از  خلیج عمان)</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6497" target="_blank">📅 17:38 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6496">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
امارات ورود هرگونه کشتی و لنج ایرانی به سواحل این کشور را ممنوع اعلام کرد و خواستار خروج فوری کشتی‌های ایرانی از سواحل این کشور شد.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6496" target="_blank">📅 15:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6495">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce8527f3a7.mp4?token=eZ_qqrol0fP9lXwnsfAvsK6KZY8lMkJgplOOSM3z09CAmqKZA8eYZZOlv1CZQ6HAKZf8XOlr2hY6tUYipDZcs_-mF90RpcIt8oWii3P1t7VPZSFbso0n8daObo8ocZkTTfU-gsopzENMH4TjXkqjk4hc2EiaNsaoRfLf-mYluPCnX813i_gtQAOfrcyrWKzjcou_B23-1ao7lcPwnslx-gMnslIwwD7nvtKt65zRVyMqwwVcbzMm9JRyHp94h6IJ3dyEiiq1kR-HPxnQ8TCj5-juHpi4zj0zDvUFS_6dU5kJ5EHj1mTAJrY9Xav55WpAeEPwj9WnC1pjI6WLeTrcKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce8527f3a7.mp4?token=eZ_qqrol0fP9lXwnsfAvsK6KZY8lMkJgplOOSM3z09CAmqKZA8eYZZOlv1CZQ6HAKZf8XOlr2hY6tUYipDZcs_-mF90RpcIt8oWii3P1t7VPZSFbso0n8daObo8ocZkTTfU-gsopzENMH4TjXkqjk4hc2EiaNsaoRfLf-mYluPCnX813i_gtQAOfrcyrWKzjcou_B23-1ao7lcPwnslx-gMnslIwwD7nvtKt65zRVyMqwwVcbzMm9JRyHp94h6IJ3dyEiiq1kR-HPxnQ8TCj5-juHpi4zj0zDvUFS_6dU5kJ5EHj1mTAJrY9Xav55WpAeEPwj9WnC1pjI6WLeTrcKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان:
اگر استعفا بدهم، رسماً اعلام می‌کنم؛ استعفا نخواهم داد و خواهم ایستاد
ما با نیروهای نظامی، کاملاً هماهنگ هستیم. می‌خواهند اختلاف درست کنند که رهبری یک چیزی می‌گوید و این‌ها یک چیز دیگر
همه مردم برای ایران سختی‌ها را تحمل می‌کنند!
[تحمل نکنند هم یا زندان یا کشته میشن]
یک عدد سه هزار نفری را سی چهل هزار نفر گفتن، نشان می‌دهد که این‌ها چقدر نامرد و وطن‌فروش هستند.»
اونهایی که به قول خودش بین ۳ هزار نفر رو کشتن، نامرد و وطن فروش نیستن، کسانی که به کشتار و ظلم معترض هستند، نامردن!!</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6495" target="_blank">📅 12:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6494">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-text">جزئیات تازه از طرح تغییر رژیم ایران؛ قرار بود کردها «زیر پرچم شیروخورشید پیشروی کنند»
🔸
یک روزنامه‌نگار سرشناس اسرائیلی در گزارشی تازه نوشته که هدف حقیقی این کشور از جنگ ۴۰روزه با جمهوری اسلامی ایران، تغییر رژیم در تهران بود نه صرفاً نابودی برنامه هسته‌ای و موشکی‌اش.
🔸
نداو ایال مدعی است که ساقط کردن جمهوری اسلامی در حالی به‌عنوان هدف اصلی تعیین شده بود که نقشه راه حقیقی برای عملی کردن آن ترسیم نشده بود؛ تناسب این هدف با امکاناتی که اسرائیل در اختیار داشت به‌طور عمیق بررسی نشد، دولت بنیامین نتانیاهو هشدارهای ارتش این کشور در مورد مخاطرات این طرح را نادیده گرفت و به عواقب آن، مانند آسیب به جایگاه اسرائیل نزد آمریکا، فکر نکرده بود.
🔸
این روزنامه‌نگار در گزارشی که روز ۹ مرداد در مجلهٔ ضمیمه آخر هفتهٔ روزنامهٔ «یدیعوت آحرونوت» منتشر شد، جزئیاتی را از مباحثات کابینهٔ اسرائیل و اختلاف‌نظرها در میان مقامات ارشد سیاسی، اطلاعاتی و نظامی این کشور پیش و پس از جنگ‌های اخیر اسرائیل با ایران ارائه داده که خود آن را «اطلاعات تازه» خوانده است.
🔸
گزارش «رؤیاهای بزرگ؛ افشاگری‌های تازه دربارهٔ طرح تغییر رژیم ایران»، نتیجهٔ «یک تحقیق جامع» نداو ایال بر اساس گفت‌وگوهایش با ده منبع نظامی و سیاسی اسرائیل بوده است.
🔸
این روزنامه‌نگار مدعی است که تلاش او تصویری دقیق‌تر از پشت‌پرده‌ها در بالاترین سطوح امنیتی و سیاسی اسرائیل ترسیم می‌کند؛ فراتر از ادعاهای پیشین که دو روزنامهٔ «نیویورک‌تایمز» و «هاآرتص» در ماه‌های گذشته در خصوص تلاش دولت اسرائیل برای تغییر رژیم در ایران و جلب همکاری محمود احمدی‌نژاد، رئیس‌جمهور پیشین، به‌عنوان یک گزینهٔ رهبری منتشر کرده بودند و به‌شدت بحث‌برانگیز شد.
🔸
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، از بین بردن برنامهٔ هسته‌ای و مهار توان موشکی ایران را هدف‌های اول و دوم جنگ ۴۰ روزه اعلام کرده بود.
🔸
نتانیاهو اما از آغاز کار پنهان نکرد که هدف سوم جنگ هم فراهم کردن شرایطی برای مردم ایران است که بتوانند کار حکومت جمهوری اسلامی را یکسره کرده و اسرائیل نیز از وجود چنین رژیمی که نابودی این کشور را عملاً دنبال کرده و با تشکیل گروه‌های نیابتی در محور موسوم به «مقاومت» در اطراف اسرائیل «حلقه آتش» به پا کرده، رهایی یابد.
🔸
نداو ایال گزارش خود را حول این ادعا نوشته که «تغییر رژیم ایران» هدف واقعی جنگ بود، نه یک خواسته فرعی یا شعاری تبلیغاتی.
🔸
به نوشتهٔ او، چنین هدفی قرار بود بر اختلاف‌نظرها دربارهٔ ماهیت نهایی جنگ با ایران در میان مقام‌های اسرائیلی نقطه پایان بگذارد، در حالی که برخی از مقامات و نهادها همچنان خواهان محدود کردن جنگ به اهداف مشخص و معین نظامی بودند.
🔸
نسخه کامل این گزارش را در
وب‌سایت رادیوفردا
بخوانید.
@RadioFarda</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6494" target="_blank">📅 09:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6493">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d5918459d.mp4?token=iOBsnzKXm6y9X8zccdZ4CjaUawmHNAq7E_kapbELSXEc6EnhQBjGu7VD3KEfBxffDLljcG0kdSdGYMgZtEhO0uPCFrlv_hOBCeuzhamuTcdXIrCJKScmncj_DF-4tW1BZqSg-l9RlUcnYM9NlXkk2YCe3tGjYj294td9MSnVXJrF5DC18lLjkqTJCjNKFv6GM9h1g2B1CNcCH1I9zTgcjRcTMrevfb5zNLzigVvgWXVvs3Gxpktn_OrBNCc0HUFG2aTQWyyVEsRSFl4a2UZBXIUmxocfA-pcyt9jZ_uVqhrebWMdleSMuGoIS5tLMSyryRaa6hf1aMa_Sxaq_fm4vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d5918459d.mp4?token=iOBsnzKXm6y9X8zccdZ4CjaUawmHNAq7E_kapbELSXEc6EnhQBjGu7VD3KEfBxffDLljcG0kdSdGYMgZtEhO0uPCFrlv_hOBCeuzhamuTcdXIrCJKScmncj_DF-4tW1BZqSg-l9RlUcnYM9NlXkk2YCe3tGjYj294td9MSnVXJrF5DC18lLjkqTJCjNKFv6GM9h1g2B1CNcCH1I9zTgcjRcTMrevfb5zNLzigVvgWXVvs3Gxpktn_OrBNCc0HUFG2aTQWyyVEsRSFl4a2UZBXIUmxocfA-pcyt9jZ_uVqhrebWMdleSMuGoIS5tLMSyryRaa6hf1aMa_Sxaq_fm4vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد باقر خرازی ، برادر همسر مسعود خامنه‌ای :
پزشکیان ۲۸ بار استعفا داده
و دیگه «کاسه کوزه‌اش رو جمع کرد»</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6493" target="_blank">📅 00:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6492">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a204c96911.mp4?token=o6sZbBSTVksZHOh0RYLAUBilegzPbcry5oa5uFi13H-xF2BEasuieAIlVE_Wkaeam2xodZhcSB2QZ2JYIXAHwq6F7ZH2bA7LaMlNx-gDM-jzs3Wam8iHuoFNPAMp33cen3yFLy1xKfYelqExpBfcs2gIKeWnhgT5gP65fxf3gKmdWqOYS_f_C65E6kvqdIeUxB4kyTELstelzfWc1xY1b8661n9gXng_9r4k-rudG1LavvGJmyQi8KRD5L2XjpThQyFqRHAYN-s78CkfYCqBgfLMtV6qc2hahc8F5pmp0yvvMIkeBx1QhMMvJ274WIkFAfAqjy7MJOXoWdfeTuP47A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a204c96911.mp4?token=o6sZbBSTVksZHOh0RYLAUBilegzPbcry5oa5uFi13H-xF2BEasuieAIlVE_Wkaeam2xodZhcSB2QZ2JYIXAHwq6F7ZH2bA7LaMlNx-gDM-jzs3Wam8iHuoFNPAMp33cen3yFLy1xKfYelqExpBfcs2gIKeWnhgT5gP65fxf3gKmdWqOYS_f_C65E6kvqdIeUxB4kyTELstelzfWc1xY1b8661n9gXng_9r4k-rudG1LavvGJmyQi8KRD5L2XjpThQyFqRHAYN-s78CkfYCqBgfLMtV6qc2hahc8F5pmp0yvvMIkeBx1QhMMvJ274WIkFAfAqjy7MJOXoWdfeTuP47A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«تبعیت از ولی‌فقیه بر مسئولان واجب است»
می‌دو‌نید شمر تا آخر عمرش
از اینکه در کربلا شرکت کرده بود
هیچ گونه پشیمانی نداشت!
شمر خودش از فرماندهان ارشد امام علی بود!
توی روایات اسلامی هم هست که
هر بار بحثی پیش می‌اومد دفاع می‌کرد از کارش! میگفت  تبعیت از حاکم اسلامی بر من واجبه !</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6492" target="_blank">📅 17:28 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6491">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30ad02e26e.mp4?token=Zd4Z7MHurh2vBQtaycuuuzPrsMXbtendRQOacAI7kYSUwTQkZVm7ZyJHfNaCNaYY38_3vM0xQITbsfJR7wxXrlx6cBV1wQMqW8j6KX5jr-Y_lP_SpETbDxoDH5symtp94wJYVBVXYZtVFUWgilnrNIRmyhut4jEg1bApbKD3xARTXSzchEKtd2gQl9Xp-cD7mXpdtt22i9ChBrj8TAPza0YBDxuijfzgFhmpzv7DizimJ7eDOiPnd4DvF8KzlymBayEvwVMjImTLv9Ta6bejUhB2iPzWKbZUG_toWHyBiR2EX3WwuimVyQ6zvEO1HEhqbj8qNPR_99aad-gzjWL4Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30ad02e26e.mp4?token=Zd4Z7MHurh2vBQtaycuuuzPrsMXbtendRQOacAI7kYSUwTQkZVm7ZyJHfNaCNaYY38_3vM0xQITbsfJR7wxXrlx6cBV1wQMqW8j6KX5jr-Y_lP_SpETbDxoDH5symtp94wJYVBVXYZtVFUWgilnrNIRmyhut4jEg1bApbKD3xARTXSzchEKtd2gQl9Xp-cD7mXpdtt22i9ChBrj8TAPza0YBDxuijfzgFhmpzv7DizimJ7eDOiPnd4DvF8KzlymBayEvwVMjImTLv9Ta6bejUhB2iPzWKbZUG_toWHyBiR2EX3WwuimVyQ6zvEO1HEhqbj8qNPR_99aad-gzjWL4Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استقبال گرم نیروهای نظامی مراکشی، از مراکشی‌هایی که از خاک اسپانیا (سئوتا) بیرون انداخته شدن :)</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6491" target="_blank">📅 23:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6490">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QQuvicwLIkxkqIC67TdIzNIFiDuEUPK6MMPTrpPWdIhM2p4kv9EbYCZAa-zBrjfySTZpBlqwX2lxXN98PALX010EUbXdpIOeln41kdEccyrZVS-LpkFXqjVD6SlKkOUVubHCmYo1JhPztlxUgwxXUZG23jyHZg7UUd-h4lUbLHg4RtzzvJIFFvSYErgxG5pWpkUtTYZIkp8Jz_js8EYN_GGukKN1_LARa5XFSNT-S9TNWnp1fYj40HkmPi-4x5zYTAEKHXO82_eYdgBOHOwyjPf3gEfQdVAEYcX7WZeMQdmHMAW0RQKN3EbPwii3tvNqe39EXfuVGx1da7p_FMp7SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرگ نخست زادگان مصر اثر نقاش بریتانیایی «لاورنس آلما تادما» در ۱۸۷۲ تمرکزش به تصویر کشیدن  اندوه یک پدر است.  نقاش عامدانه موسی را مرکزیت نقاشی، آنگونه که سنت نقاشان بود، کنار زده،  و برخلاف نقاشانی که به خاطر آموزه‌های مذهبی،  روایتی یکسویه را ترویج می‌کنند،…</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6490" target="_blank">📅 16:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6489">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nbUjeXehjZXgOkAYkCM9p-7-xLWHcan1OnqTXloKhlza14OPyh1iht7WKFbBg-AIITzYbHVRtKK33wb83gj-jBRLkKXXP8Ws70KBsOWdROyoLuvUa_wSnayQeDK37LMBqFsufa7dfxFKHZGEJpx2Y9TVjMQgBMiPW-RhZv45OWXSxx1FvDSUc26gsjV5Kuni-YnY2z1TFjCu_IwCXFo-yEO0D4ykwhd5fxrRtqpVxiG58GyMxp3UP2X6d4gupyiJptyB6ygaKhLqweMuU5GMe3sqXAHVBCkCUPt82vZk3A3Io0Bou45ALhYFIfV_qMLoD3bIjhysRJsCfxGY7wPRjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد چی میشه؟ بعد میرسیم به آیه ۲۳  که خدا از زبان موسی بهشون میگن وارد این سرزمین بشید و با ساکنان  اون مبارزه کنید و اونها رو بیرون کنید!  ولی بنی‌اسرائیل قبول نمیکنه که بره بجنگه!  و اونها رو بیرون کنه!  بنی اسرائیل مخالفت میکنه از این‌ دستور  موسی و خدا!…</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6489" target="_blank">📅 16:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6487">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vI6leA4csW5l12O76CrRuE5ds19H8EN0Wk0MbkgvfkZA_DzUM_Or1Do-sVLzHC5hPGxMQizZ1I5qhPiAGvXFHmoP_boPHznikYKGGiioxEundYvc8LpRDsY5rsMGAR8QckwdgmTOvV0d51Ffv08NknM0NXqoRpW2jYth3sUAWRjBMsWvRzwybH9pXyEwqDCDJjyIOWegZnG84ZnxrBCMjcuoX5NrdxJqzVopw7tnvK8gFdQERaFSFZyRSUl9tVGRQp4hZ8Fy6r02OyA7kgDezxw4QivJuF0WHBFFFcoc8z5PS9fcJ6OtrLjsIWBVrMO60IYtoXD7VgiDlyy6rv3N-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m5Of2OMQTbPmgTZEiXoVCwXEWC5fw9nQ335bWNK0otg9g-BVRzv6f3DNaqrPvI24RMGCLV8fum1bPmbyhokgeCh9Z6I2Dy2qonz7WHiQLUkSeQktUVGxgy3gvKqtp-5N74uEdsY0zJOLNlULAYK6Y7L3tuO-6gun4yPzglFFLo0B_lIGddk6rFnAvieyPJXMIgIdEmeE-x5UHej_-vnw5i0NVo1b0aPJoV8FOOk8-wc3qBR5Mpd91yRl7THV66KVgJdLD44f4p2BBcE22JFgZ6BM6V-yFQCL_41q7aNUpdkUN9V-VTXIlvMbBg6pxRQni4XwDF7RN79nasvvJZXLGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هدف فقط رهایی قوم بنی‌اسرائیل  امر مصر بود و اسکان آنها در «سرزمین مقدس»،  سرزمینی که قرآن میگه :« کتب الله لکم»! «برایتان خدا مقرر کرده!» ثبت کرده! سند زده!   آیه ۲۱ سوره مائده  موسی خطاب به قوم بنی‌‌اسرائیل میگه :  «ای قوم! وارد سرزمین مقدس (کنعان - فلسطین)…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6487" target="_blank">📅 16:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6486">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YIi1V5VmEYbKWmPN9x74GDndZxLgOYLMtOIKLAZFLs8Vp0ghfRmbb2WaOHTWdB6GAvdxHot5yKDCX6LzKk84c39i5YCjkBjO3F34SBNGHezveD2shMhTlgO5DE0i5yiBCwRsSmAhrWXbUiw-NmylzJGk6doze-pbn-LGVBtftznFzJ8JqgZP8aKpaWoC4hywth_22hlRXVNNR3aBBrVroJJPe3qASxCAVdYIxO9vJuowohLQMaSQmKVEsXEpBg4V1o6ryg31OLcgT6px84CSylcZFqit707Tj_b1Wk6YErITEOlHMMtsjR4_7to-DYkkR0u_jKldImOgMKedy8wd1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همونطور که اشاره کردم، هیچ جای قرآن حتی  اشاره نشده که موسی رفته تا مردم مصر  رو از ظلم فرعون آزاد کنه!  هیچ جا اشاره نشده که رفته تا دین مردم رو عوض کنه و دین خدا رو تبلیغ کنه!  نه در قرآن و ته در تورات!  اتفاقا نه تنها مردم مصر، براش مسئله‌ای نبود  که در…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6486" target="_blank">📅 16:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6485">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LqIVVXzxOTEubAp1KRoQ0Gw-pywDUzxOp403l-1lQ5WLOKzqnBhucvIy35CozWAKsQKw_f1uUjoSOVHBIWzn0F8HwgG0i2Wl3IB-C8953qtHlRg8T4ZHGmbjY4a-ZZRfnsV99xYuQurM6kBajkYheUyqLjDpKRlwn4ScZjLOUJhE-ajuSi-HHg66EZEx8I9EtUei9qKzbg3D7m-LqmZB9C_Vd4EC1Wlle90K3Smweb0v_aZdURBoOZJPYQSb41qtzY54TCp_sd8ayE4T581fi2f_M96w8rQaTf0B3vRwSbdwxDq8akG035PtWo873mZqeGjI-rh_ZnZvbuOd7Of6_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشتن همه نخست زادگان مصر در یک نیمه شب،  تنها مجازات عمومی خدا،  در برابر سرسختی فرعون نبود!  قبلش آب رود نیل را تبدیل به خون کرد تا کسی نتواند آب بنوشید،  نه انسان، نه گیاه و نه حیوان!  قبل تر از آن آفتی فرستاد تا همه مزارع مصری‌ها از بین برود و قحطی و گرسنگی…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6485" target="_blank">📅 16:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6484">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rKolEiuD-0FcT1iNg4JXqUUwqLvHKT7o5MZeUITvINNHTF6AfV5l3wabDWyWnDUVWU0cTE6y6T_UUkw_0zMT37__m7ov653kjzl26sdUM6t5dAMsztp2OmkSRXtIQRwa9RnH34-8UQaN3dIbuOTU2W27hN9Ae1Ue77H_RF6nWjI0d3NyRnsvZF8yM9lY3x6FLu5UQ2Kvx4AwOaECsu5NGgmGrOJICR3lpKCG8ESoESU5Yqgj5_524_eTQv_hoO_-IFgs0MlyFW_Six6QiRtkODrNtpwU4NIWfhxRB4c6sneQCCkldIWBpAaYTyHyinA68taCbK8nMwItdod6BzgzLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا، موسی و برادرش هارون رو فرستاده بود پیش فرعون برای آزادی قوم برگزیده‌اش، «بنی‌اسرائیل»!  فقط برای همین منظور! موسی نه رفته بود مردم مصر را دعوت به دین خدا کند و ایمان آنها را تغییر دهد، نه ماموریتی داشت که علیه دین مصری‌ها حرفی بزند!  هیچ جای قرآن هم نیومده!…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6484" target="_blank">📅 16:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6483">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NCltZZnVzNjRf1CZWSdI3t1Gu64rbx4kObXtcAwTahJE_Rhcp_b_TXkaEJoeNoKBLmz3JfqnFpWKC5FdPzuv6XPVCeBASVDAh6kYHsE4ynLNk5lIioOC3X9g3GNXlp7g6UqZUKvL0AW_o1wfhfcCY9MbpQ4oKo0az9NURAYNtQBEWoJcd3ce_f7FIucuvpc9tjOpH0lSyqCzRjipbEDpLu1G8rNgxllYDT9fjO1LCHy41yFbtCfYphYGalgegkJMdNSdx3rqIMKNMr5LJ308JQVsgfZvMtGzF8a3lE4q90kv-5AcHzzu4lzD6Rp3Tv10_nwmQT9iozxYDuwzUiIWTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و همان نیمه شب …..  فرعون به هارون و به موسی گفت :  «برخیزید و از میان قوم من بیرون روید،  هم شما و هم بنی‌اسرائیل!»  ایرانیان زرتشتی، وقتی داستان‌های  کتاب‌های ادیان ابراهیمی را می‌خواندند،   دائم دچار شوک می‌شدند! و حیران می‌گفت : خدای ادیان ابراهیمی،  عجب…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6483" target="_blank">📅 15:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6482">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">فرعون، جسد نخست زاده خود  را در دست دارد، زن فرعون گریه می‌کند و موسی و هارون،  در گوشه‌ای از تصویر دیده می‌شوند.  برای مجازات فرعون، پسر او، و نخست زادگان «همه مصری‌ها»،  «حتی آن زن کنیزی که پشت سنگ آسیاب نشسته بود، حتی نخست زاده آن کس  که در زندان بود.»…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6482" target="_blank">📅 15:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6481">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ITLTQMhPSiSLLBq_APsyTHeRHSJ9kTl5HxFo_djxno65Iq8FTvctwgMsmoH1l0a8lUbs2yQ51mVrzMt6vPeAOf4taOe1jFc_9R7Vrc4pnJ0WunRAhsFf7qlgdp-0yBYwMvMkZdzy2rK7vwXAmyrQnY8kVMcyJZp9muj4u_bsqCmiYHbNHUGIe_gsB0PlpO20fdR7GEmYPq-XBmcjdkGnJgusSllewPvZoSHz3PxmaaqIKXJoE3hUMJMMHZ8jJH5FRX8fMqWV0O1a9c61nlLfdqOATWs0T8zuAgEVUqLxgbiDQHTruj7AuK7QU8tirymNr0B4lJT-45hhbSdsXkC36g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرعون، جسد نخست زاده خود
را در دست دارد، زن فرعون گریه می‌کند
و موسی و هارون،
در گوشه‌ای از تصویر دیده می‌شوند.
برای مجازات فرعون، پسر او،
و نخست زادگان «همه مصری‌ها»،
«حتی آن زن کنیزی که پشت سنگ آسیاب نشسته بود، حتی نخست زاده آن کس
که در زندان بود.» همگی کشته شدند!
حتی! حتی نخست زادگان گاو و گوسفندهای مردم مصر!
و این تصمیم و اراده خدا بود!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6481" target="_blank">📅 15:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6480">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-98FvWJjWyxxbsYTG7_N2LTWBocZR9f4qeV2LkN1XVmfpZaQzlthKk966v9Td8sbcgiwdLF2843ryHhwWKs-WwHCP5CJXotD5-ZBwSW8or9WBc50GsC3Q0BRjHbo8eZLfWQBl19sisEUtW8XViegT_PG0kI5xhWic7gteRxlcpH9-XGSrz04KRtVCcCfnJz6-DofK7U_4koXGZUvy33eJnAAgchQ9gszq6NTWey9SNwMmZJvsl2x6q0WWcIeEmZQzoOuv1KFXG_lDLG6mA-9zWhlJXcTRG1d4KfIF5jxR0_yiFjNS40-c_V-i2wnb_QHfHuMbhgNKs0qtYeKM6V8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏جلال آل احمد، گرچه فرزند یک آیت‌الله بود، اما اساسا فرد مذهبی نبود و در دوره جوانی هم به حزب توده پیوست.  ‏اتفاقا اهل مشروب و کارهای دیگه‌ای هم‌بود که خودش توضیح داده در سفر به اروپا انجام میداد،  ‏حتی به زنش - سیمین دانشور - گفته بود بره با یکی بخوابه، تا…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6480" target="_blank">📅 13:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6479">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IqFlgaDX4Ir1KQQKKdOuBsFMQe570yVBH0VLmjfIoTaBY8-lWDmAthqcAz2qFsTZuCIQTiAnY045N0hhFBCCK7T1ZbKpv3Mr_lMXTQ-6z8-oiyl2OFkQE7R5dBNEEF4a-vWabpFEl-ksFIKYwAJV9ov2huuPOP9Hga9IMen_FJmnnYsP4FpaT6pmXSbUm3FoLcjSS8DCWsc565ZJR1HpmhsW1gnJ4YSBouzBpxWKNsQtv1pbFw_EQ-XLfCrTFbJ4Cm0BnGSq9ful5tx8lH2QQwG8DJjMad8MZeM6Kkr7XUEYrDZV6s7FactLh2q2UQEmT_v8XTANa2RQyZbzyPV3Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏جلال آل احمد، گرچه فرزند یک آیت‌الله بود، اما اساسا فرد مذهبی نبود و در دوره جوانی هم به حزب توده پیوست.
‏اتفاقا اهل مشروب و کارهای دیگه‌ای هم‌بود که خودش توضیح داده در سفر به اروپا انجام میداد،
‏حتی به زنش - سیمین دانشور - گفته بود بره با یکی بخوابه، تا بتونن بچه‌ دار بشن. این رو خود آل احمد نوشته،
‏او اما آنچنان ضد غرب بود، که میگفت باید از اسلام، از منبر، از مسجد، سلاح و سنگری ساخت برای مبارزه با غرب! تمام هم و غم او‌مبارزه با غرب بود. می‌گفت روحانیون تنها رهبران طبیعی مردم هستند.
‏اساسا دنبال این نبود که اسلام تقویت بشه تا مردم برن به بهشت! میگفت تقویت بشه تا با غرب مبارزه کنیم!
‏علی شریعتی و علی خامنه‌ای، از چهره‌های شاخص تحت تاثیر اندیشه‌های او بودند.
https://x.com/farahmandalipur/status/2083853984113054084?s=46</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6479" target="_blank">📅 13:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6478">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PzUMhktBMkzdSR1kvZvYGiS88VuFKoFvs_34USu-lGero0PjLxknKGQqFjKh4LO6pd3IYry26bhOFTyasHBMvTJavx4hRGBMa0nhpctQEUnMFyqOfh4UflGYzPJfQ6lpd0xXWw5EcluqXP1aRxLOA6FVfSlv8WFFqc4skjkO7UZsZmopgVPv8uGfzluzccJL4EC_IHIdxs35I_v4ddoT222YfADts7I6xFJb8rkrxluMqtr5tqa4TsQqAZBBirFABUsg1ryW4JsN2zmpo54LQr79-3sS6Y8Y3rJws9K7NOnEvKaqfv5ocaHT1bt6ZRD_HV7TBnAvT_yOaZfY06toiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه شعرا و نویسندگان به مسعود رجوی  - سازمان مجاهدین خلق -  سازمانی که ترکیبی است  از اسلامگرایی افراطی و کمونیسم و مارکسیسم!  تباه در تباه!  خرداد ماه ۱۳۶۰ نامه نوشتن برای «تجدید عهد  با آرمان‌های زنان و مردانی که برای رهایی ایران پایه جنبشی انقلابی را گذاشتند».…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6478" target="_blank">📅 12:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6477">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/niFQUNiYYTNRqXeQ8JkqrMEaPKL5QeYh6yjswQt8wj7ty4MaXd2f4H5R2D7W3BLmaINqdZEGf9mDAqj2r7i4e8G6iImRw2l7X9PheA-Kl1uDPg2rdCnvxrt0CQiliGAlRzHZcAT9h9IO-iZ7uQ-KMDOSNCGkPmcCK8U0RvpVaG7AxkdA7gcuHYyKN6bkqfrELf1C__etYgVANQI_txA3tz8czY9UZ4ZC4tfpYmHfUhupQw8eZEkupuyHEYZLEBmusmfxwzKIlPMmq2FsTGcxaxNH85coTUsQ5KptydrJUyDEzDBya5dfA2_kfe9_mwH3dt1C5mseCNpM7fIpIp1oOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه شعرا و نویسندگان به مسعود رجوی  - سازمان مجاهدین خلق -
سازمانی که ترکیبی است  از اسلامگرایی افراطی و کمونیسم و مارکسیسم!
تباه در تباه!
خرداد ماه ۱۳۶۰ نامه نوشتن برای «تجدید عهد  با آرمان‌های زنان و مردانی که برای رهایی ایران پایه جنبشی انقلابی را گذاشتند».
احمد شاملو - غلامحسین ساعدی - اسماعیل خوئی - منوچهر هزارخانی - هوشنگ گلشیری - باقر پرهام - محمد علی سپانلو
اینها روشنفکران ما بودن،
جامعه آرمانی اینها، ترکیب کمونیسم و اسلامگرایی بود!
از مسببان انقلاب تباه ۵۷.
از مسببان گمراهی یک نسل از ایرانیان،
از‌مسببان  تنبیه نسل‌هایی از ایرانیان که هنوز  به دنیا نیامده بودند!</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6477" target="_blank">📅 12:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6475">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/seV_2yzVROJD2d3ikE2duDsvoO6qmRPocNOj1K1dYlaQcsJmiouMU9LQLT98Ioelm4y559h8-AG52f8jRQ_vpsDY9lmXUWoihZPm5-Sqvia1rVko3AJf-MMwHERoYLngXn4L2ibfliJjnmJTXDNfcm8x_qq7C0R576gtTMDc4YQ0WQWE9iSW6EonjKQ6RNrsLLIW1qiXhNv-A_DNW2srOPpML4p9HG0I0SESFpFJiKwA4L3Ta4u4t-HugFnW_9HgEjZ1B9R9_sjBbI6x0GNKZJq-o9l_dFs4ARSqx8yrPMi4J-1aykQOO3yYbyxHsj01IkZcChFB_mI6m_Top5BZWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9c460b262.mp4?token=XbAEkBHj1GSRnV6O5VKGX6B6OLpkzj6z2I9PNPTm3ASr828LU7LCrJ4jbQ0OcEBX4CBLaisPtLSZXomYcnVpg6rzwQxyH4PHJZkyywSeBT3TbNqzlAYErrtm22LOmaPRo72LsH6vgmYvGXBnO-zIGmjZ9topY7WZZA0o1WBcdxO7gDZb4mM_PMqPtUHCrAwWS96nRnuo06r_WX7zLcXYjlQoWMTxljmWAIbhAO5obVTQNoZhxRvaB7_cleJRgt56YY_p8MnLu-6WH-DpDTXlFlNUnjr_GmobgyHGg6GpkKgnHdOuD22WjR2l0vHAyhi6XsqRqHqjZz8mZ0f0KiPvtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9c460b262.mp4?token=XbAEkBHj1GSRnV6O5VKGX6B6OLpkzj6z2I9PNPTm3ASr828LU7LCrJ4jbQ0OcEBX4CBLaisPtLSZXomYcnVpg6rzwQxyH4PHJZkyywSeBT3TbNqzlAYErrtm22LOmaPRo72LsH6vgmYvGXBnO-zIGmjZ9topY7WZZA0o1WBcdxO7gDZb4mM_PMqPtUHCrAwWS96nRnuo06r_WX7zLcXYjlQoWMTxljmWAIbhAO5obVTQNoZhxRvaB7_cleJRgt56YY_p8MnLu-6WH-DpDTXlFlNUnjr_GmobgyHGg6GpkKgnHdOuD22WjR2l0vHAyhi6XsqRqHqjZz8mZ0f0KiPvtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل برخورد سربازان مسلمان با مردم مسلمان.
نیروهایی امنیتی مراکش برای جلوگیری از خروج گسترده جوانان مراکشی در مرز مراکش - اسپانیا مستقر شدن و مشغول ممانعت از گریز جوانان مسلمان از کشور مسلمان مراکش هستند.
تصویر البته مشخصا با هوش مصنوعی درست‌شده.
https://x.com/farahmandalipur/status/2083837885224988931?s=46</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6475" target="_blank">📅 12:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6474">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mGOzpSYemym0189eJGVHknSC_XKJo2P9dfHxVziZ1inBMh0bPY2EGl8V7sf0TLJLjz_ooTleP8xuDsvNbBQETdB1z_xjH8ZOi3kDAfGCP64lyAGCowGvHI_4O5DZ7Ds7fj94F7Jx0_cZqlq6BcPVruxDcRzN1SFwE06--dgbmdtakz67Ua9YQFCrqmD4jqeBxNxh6lrncAHhZ85ihXl1GHSLTW_GQyWzms50IiPyT55pExAVUSSIFMh45_a8ytvS1eal6icJmaE3pe7-PHSawkGjzmZM2fiREzUmI7BXVNq7KcswMi2yUP2Q0yVzyN1Yw2VChfZUb5W2amBUEHkTVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ترامپ : ایران و چند کشور خاورمیانه درخواست کرده‌اند که حمله متوقف شود چون چارچوب یک توافق شکل گرفته.. این توافق شامل بازگشایی کامل تنگه هرمز و پایان تهدید هسته‌ای ایران است و
به همین دلیل آمریکا و اسرائیل فعلاً حمله را لغو کرده‌اند
تا فرصت نهایی کردن توافق فراهم شود.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6474" target="_blank">📅 10:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6473">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fIj3F3aEDBRkvnDF5NkxyjXbnZ-K3u7vPT1X9WSxTjVrdPR1F2X1byk6U8HSUwLt21GpAx1vdxTJnZBaueQ9E5_zdFDJNBDFngC6dJukFVrOzfcPDjOCC1jM1jjPXluUe_Hfd7g55z2lU0lwNxxtdD1akAc4-3vEqrEocIbbHjHKlak-cOma2JUWa7uQKpUq-Q6xmH3JYJt7VLxmKDJU3LPbD7F8wC7YbfmFWOenVQNckZAt9BJpLIM7LstkrUVo4Luj3L4Iz_kJsjn7laP6rUCk1pi-mMxuZHnvvlUg5VNoRQrmz-CLr7sNwjgkUBGmIgNbSa7lKmNtPzEgm3HsKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ترامپ در آستانه
احتمال شروع جنگ</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6473" target="_blank">📅 21:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6472">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u5qFgl32rJDhjWETeyPNeCQFjqtzICOqOo7jjLRBxi3a54czJ2xfoJXV9UBtlS0ZF8z2pDnUD6-VV7-2ke204ERBr8TEnax4M0BoOtxo5W72JmTVdMJcsGYha7d42HwcZM6wRdF2MIlhSNTN1bG7Xfpp72jhAHzCWdp4vDtTqN4CqjbEb4cvvr-XQpJmxxH_qwK-Ne3uxnlCPJr8e79LXHOqkDFTko8Ab-mHs-w958YRhOk_lsgmQTQFut2gFtk1Xduzx-PZc1z6fAjKlqtnnSd7XwyyaY3VP7-tdQZFyALVtghTy2HrrNaTP-S-Als-Hz34gCIRznqznNxWA4F6pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه تنها بنزین گران شد بلکه سهمیه نیز کمتر شد.</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/farahmand_alipour/6472" target="_blank">📅 18:19 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6471">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‏سفارت آمریکا در اسرائیل از شهروندان آمریکایی خواست خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/farahmand_alipour/6471" target="_blank">📅 14:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6470">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A5VZJbWs-eJhpKczzi_GkpjFXinL128-uufAXIfbpkWTAh6eZV8tsX-yXrct4zAQJV-Xq7gtjVTKV9ri1cJe7wbla5_55r3XXGwsMBS70gBemksDxdfJJHHMlRufYcPbdTb75RG2hqCQ4Lg9AdeGml3rvb9dAXda2WLWPAls7KLrsSNlSzLSes01XeC8RrR5PXs9Gxyusqjsmmo6o97kWAIjYxV0bekR-qaAyXUL2LUG3QL_KT4hhVwN885f-LdykJBIqfxdCHQXDwsw7JGQ9reSSU62Do8vjcF7pam9MaExS9LtsnOv_wcCNyA1PmRPNalbhe8cDpuf2iO6P7jC3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرمین ۲۰ ساله و اهل شاهرود بود.
لعنت به جمهوری تبهکار اسلامی که هر روز ماندنش خسارت و زیان و هزینه به ایران و ایرانی است!</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/farahmand_alipour/6470" target="_blank">📅 14:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6469">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">‏فارس: شنیده‌شدن صدای انفجار از حوالی اسلام‌آباد غرب
🔺
دقایقی پیش صدای انفجار از حوالی اسلام‌آباد غرب شنیده شد. هنوز محل دقیق و علت وقوع این انفجار مشخص نیست.</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6469" target="_blank">📅 13:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6468">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">وقتی یک نماینده مجلس به‌جای سخن گفتن از پایان جنگ، حفظ جان مردم یا ساخت پناهگاه‌های عمومی، از ایجاد «شهرهای حکمرانی» در دل کوه برای حفاظت از مدیران و مسئولان سخن می‌گوید، این پرسش به‌طور طبیعی مطرح می‌شود که در این نگاه، جایگاه مردم کجاست؟
اگر قرار است منابع کشور صرف ساخت پناهگاه شود، بدیهی است که نخستین اولویت باید امنیت شهروندانی باشد که در زمان حملات، بی‌دفاع در خانه‌ها، محل کار و خیابان‌ها قرار دارند، نه مدیرانی که خود در جایگاه تصمیم‌گیری هستند. منتقدان می‌گویند این رویکرد، به‌جای آنکه دغدغه حفظ جان مردم را نشان دهد، بیش از هر چیز بر بقای ساختار قدرت متمرکز است.
مگر مردم تصمیم‌گیر آغاز یا ادامه جنگ بوده‌اند که اکنون باید بی‌پناه بمانند و سپر بلای پیامدهای آن شوند؟ اگر امنیت حق همگانی است، این حق پیش از هر چیز باید برای مردمی تضمین شود که بیشترین هزینه هر جنگ را با جان، خانه، معیشت و آینده خود می‌پردازند، نه برای حاکمانی که قرار است در «شهرهای حکمرانی» در دل کوه از خطر مصون بمانند.
اخبار جمهور</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6468" target="_blank">📅 13:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6467">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BsUQenSFMholMbzrcUjSzh9CiY65NKPjD0X4rpX_E533XHgYmg2DcbBCxGgqz_8qsDv4BHfaTbtJgM-5mIogWfJAI6n2x8NeTKnOqtm4sgFyQCafZoSPU2xKLF6G6sMFs_deafKUgTyimMwLOofKeLxBw5bPSddS813yL30DYwgaZy8jkNzyE8FcY4OnRjn8O6sQrNxUixqEyhbZGa2oGRdZ-zDSImnPBlOK46pMY0iO7zH8lGP3DAJxhnneDQrzAAP3X-BZ2xYNNAZ1WPs8zpt_ccOj61b3rficNmfnGuYG841pUIjlP5PaCX49LLaw9xX_9dNGDvecHEyVDtrpjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«علی لاریجانی» !!
در زمانی که رئیس سازمان صدا و سیما بود، بزرگ‌ترین دستگاه پروپاگاندا و تبلیغی کشور!</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6467" target="_blank">📅 13:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6466">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rxmWGUq1TLuBZPO36wVRO2lckv2t2EQhB1b6pKCk93CasLY6p0FyWhgOCBWQvyVhlDA-RzchxPoPIBasiaiJzDN5c5mNLU9aGNF6136YudHRtYE0uapCJjXUWKtnUqAP03yrnSlPjVtRPIyRi2nqfaYWCKDh3Qjx-tOZfG9x7Tnb6cLjKgPAljxdc_Rw2zK7i_yFW99IDEOl1nvrzmiXGWD6JIwHCzHdeF62se_SEvPU7zikgtdqrhaoNsoyWl5gY_G6NSRZ5Rub0MjtBjcbLLyRxHjB8UFC00LhpCSzEelcEbb093rgJVwUDEo5fOUFb25QETdyS3gCJWReo7IrsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌‌ان پیش بینی کرده که حملات همین آخر هفته (همین امروز و فردا)
شروع بشه
ترامپ گفته راه دیپلماسی رو نمی‌بنده
و اگر ج‌ا کوتاه بیاد از برنامه هسته‌ای و…..
حملات رو متوقف میکنه.</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6466" target="_blank">📅 11:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6465">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RfpIdu4LniHBlnFRgFHanJAAG-dc3tP334IJImcnqK0Ykfq2sftLhBm1RLtFqMBSEQ-ynrjJaDs8VA6xmVRf_4yLYXfREl4byJHshjDfy3iE-xNhI2WDWFXPujpMlcEbZl-7QJvNo6MWsZ2djA_Ud6G_e8sDeFrsPRuV5tiRSUwMNFY8y9-au8YHD47e20U66As01N5epKaXlpR5Jw-WyfFpanvSqrWBgBwPyndwVnB03SQqWWZGKdNvct6lK4S7tRoYgqGoy6WokSKnJfve8T1V3uHxnSNr0UOdcqOXg9uhy5WnEmhbuohmZoUGScwE5NHScMYDCa5LHH_6pH8uxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ دستور حمله به ایران را صادر کرد. حملات احتمالا از آخر همین هفته شروع شوند و برای چند روز ادامه داشته باشند.
بخش انرژی ایران از جمله اهداف اصلی حملات خواهد بود.</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/farahmand_alipour/6465" target="_blank">📅 01:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6464">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ttQd0QUdHyGiSI_ZSEp7aVS5VoGxGVSQB12wxwW605_gaJ0CnE-bEaW1QC8zfSgC-84ZlXzJA1kvzzifYHGPxfUxo72IKoYN9GhUUong9W_VzsTTPhwkMP2yQQokPq73tYO7pvbeCEeknF0D1BV4EoFfxi1BW5vxps-_UremkPPeS8SsWezk5SFhj54Rh-yTi4guhR31Ca9YYM0VN2fXUJJi4Yx84kNtAcu4hpgSAwwqKoCBjx2eaAbCC0TCufnYhpS1ldDXIFv5Rpp_qCTJWjdfoVBPWUF-wFQTkyNw3J4JwpIujPaTgwDhFMsq7seaKKdYkRDr6MiQbsplNJINQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
دولت ایتالیا آزادی رفت و آمد هوایی و دریایی
بین ایتالیا و اسپانیا رو به طور موقت لغو کرد!
این بدین معناست که تا اطلاع ثانوی،
پروازهایی که از اسپانیا به مقصد ایتالیا است،
دولت ایتالیا مسافران آن را کنترل خواهد کرد.
اقدام دولت راستگرای خانم ملونی،
فشار بر دولت چپگرای اسپانیا را افزایش می‌دهد.
دولت پدرو سانچز هم اکنون نیز دارای کمترین حمایت شده و پیش‌بینی‌ها حکایت از آن دارند که در انتخابات سال آینده از قدرت کنار خواهد رفت
گرچه برخی از راستگرایان امیدوارند با انجام انتخابات زودهنگام، انتقال قدرت سریعتر انجام شود.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6464" target="_blank">📅 23:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6463">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6463" target="_blank">📅 19:39 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6462">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6462" target="_blank">📅 19:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6461">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا  نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6461" target="_blank">📅 18:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6460">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا
نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6460" target="_blank">📅 18:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6459">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=D5leLTQlvof8sfwkpwxxAsjc_pfkADvIUcmY2J-b7GYDNZtpIrXmzGuOf8ewNhzz5SEm4qfcMPaEI-XL_zEo16VDC1GVV1drmxJnZtrhq_VwI_Sprft_Nu8qU6UA6RPGFepvTA63zl94pE5db2hVADQbTIGwRWL1EsHzlAgJPoCFCObN1gj5IYZLf-gpF7dwNBRhxRVyDuMlrJEV4XV2ldBpaY3YXT6VWdzE2H-o67N9Hc4oVR86DlhH9RgIIau81sEEW3qWg2xSlpleZoPaXbKMiNPTBL5s_OG0gyWh73v1GLEfDyf7gGWDw8o2WNV2w_weevBVdm4qmAi_1VuEFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=D5leLTQlvof8sfwkpwxxAsjc_pfkADvIUcmY2J-b7GYDNZtpIrXmzGuOf8ewNhzz5SEm4qfcMPaEI-XL_zEo16VDC1GVV1drmxJnZtrhq_VwI_Sprft_Nu8qU6UA6RPGFepvTA63zl94pE5db2hVADQbTIGwRWL1EsHzlAgJPoCFCObN1gj5IYZLf-gpF7dwNBRhxRVyDuMlrJEV4XV2ldBpaY3YXT6VWdzE2H-o67N9Hc4oVR86DlhH9RgIIau81sEEW3qWg2xSlpleZoPaXbKMiNPTBL5s_OG0gyWh73v1GLEfDyf7gGWDw8o2WNV2w_weevBVdm4qmAi_1VuEFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سانچز در میان اعتراضات مردم سئوتا
وارد ساختمان فرمانداری شهر شد.
(این شهر خودمختاره)</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6459" target="_blank">📅 18:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6458">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PBhLBLhVJr7mKPZt5iRQmyw0dZBIkQwXgAhbaiHhsz1NbY7ZPCwyKRFshPxBXgPvuxGgRRPG70E4ojBikaU6_HVgM1m79Nxz7z5BHF-raid9hXgIX3mu2glBiJHirO5JvP5scJVcFMuT0UcklsoljWkOd-R3o3wMY1lcyBK7l7c5P2hKr35kvk5NEUu1DkeUS_XumzCjD69MCCp_0icYe-a_ra90QZ-NIym9l6XhRxde94xJrGzwxwd-LA5jDthKjkkQCKI4ZZ4CYQb75ANCiV3ezmOrU9evKclfuUhXoVl_8uBNmsaNSwhiyEucVOMenY2mKW9uiOu2VgKB8_ZCPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته مهم :  چرا از دولت سانچز انتقاد میشه؟  به خاطر اینکه این پرونده حدود ۲ سال باز بود و مشخص بود که یک «خلا قانونی» وجود داره! و رای دادگاه سئوتا، ۲ سال پیش این مورد رو عیان کرده بود!  دادگاه هم قرار نیست طرف دولت رو بگیره!  انتظاری ازش نمیره!   اصلا دادگاه…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6458" target="_blank">📅 18:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6457">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">اینها که رد شدن روی شبکه‌های اجتماعی نوشتن که پلیس هیچ کاری به ما نداشت!  و فهمیدن اگه از طریق دریا بیان، دیگه پلیس دستگیر نمیکنه و …..!  خبر سریعا از طریق شبکه‌های اجتماعی دست به دست شد، چند روز پیش مثلا یهو ۲۰۰ نفر وارد شدند، اینها هم نوشتن که آقا مسیر دریا…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6457" target="_blank">📅 18:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6456">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CbVY4L5xWvWcR9EpGVKh0ujjE72TL8QmS9QPNNoOugRrf13Zs5IzAkuctob_8QIHB9WMsYOGm0swUg4eLcSDgWzX6GZiyy4dczNruXSAsf4jgQIkgdRylc7iuDOgAqe1efmO4faEqq7NjpVFRC34Dod1BFkCp80jtKWFr1VdGeenw7nwSBKjqHVKH-Vmf5ou2sPkBlIXplicvzxkQcm4vghBq9vK53Y5UCE0h30qI8Hed0XrGa_Fc29yqpYAkM_QRAMyGJBlG9RNyFiSuwZbnA1JO3xwsQNFzRCCLM_s2xdNW6qGD6BLWQP75Gj-bWJZ-oo5JTild0Lc5ArnvWIGpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادگاه سئوتا گفت حق با مرد الجزایری است!  در قانون اومده «موانع مرزی!»  دولت اسپانیا به رای دادگاه اعتراض کرد  (چون یک طرف شکایت پلیس بود دیگه،  و وزارت کشور و…..)  کار کشید به «دادگاه عالی» اسپانیا!  دادگاه عالی کی رای خودش رو داد؟  همین ۳ هفته پیش!  و گفت…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6456" target="_blank">📅 18:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6455">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JiIiEnZMcYwG7lR4Jf4QgQg5BsEaKAODMVbNqR2KsFuHvmYGFyIWy-4xD2WvNHarTrxgGju4tUC2QoqmPyzLCMHTDydRdRq5MRLy_AenQzHfvJbNM1O2aQLAVlKbQ3zFPtxvTfEkdzMwUom2VCJ-B7Y4RqTCJD1CF20gAXifMrwKFN5v_9ayzR7Aj_p-DJgiahtdFIXTE3LYbZbuHeLVmJEG0CoTFVdRmv8Hcmm6_Ebw5eD3vR9LYpMjj5vp8oKy41cS8mW7Ij_-vmc0iZVrfXrvgvwhxXEfNoI7ofugS0Tr_j96-bjiUa_ARZpKh7Wo7TPGVy0KSFwt0SitXJTRUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داستان اینه :  حدود ۲ سال پیش یک مرد الجزایری  شنا کنان رفته بود «سئوتا» پلیس اسپانیا سریع دستگیرش کرد و تحویل پلیس مراکش دادش  (چون مرز بین اسپانیا و مراکشه، و اون از مرز مراکش وارد شده بود)،  این مرد الجزایری با کمک ۳ ان‌جی‌او اسپانیایی، شکایتی تنظیم کردند…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6455" target="_blank">📅 18:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6454">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/darWKNE_bhT_dCt1sxBPB1RWUDY5gJj5dagDV5GfJsbNvS22jwHbbmtfMI8BbVCbdMV-b0psdKi6uZi5_1hEc8YMtLxPYTvgt5878pfXrpd0zfRJmCShamgZM9Fc7A8VkGqaE1NXe9D7CT_yAaiIAuAVsaAbhcP9hInI0wIEYq1Jkrx2cxk3TQjPxUgb-rihOIMOX9AlfqTQQkV1JS6lRWzkKeUuWhrnqwkijYbdqBuVLiol_HpDET5-_SD9b-2x9ugQ92ktTkBNOncARaBJA_7wghygEioJZ9atQoLP6COYlZDSObDmVN1Rz1d1iL6LF8OtZtbnEtydR4yRnlXlOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایس نقشه رو نگاه کنید ۱ سانتیمتر برابر با یک کیلومتره!  اینقدر کوچیکه! با این وجود ۸۰ هزار اسپانیایی اینجا زندگی میکنن.  حالا چی شد که یهو این همه جمعیت روانه اونجا شدند؟ چی شد که پلیس کاری نکرد؟</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6454" target="_blank">📅 17:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6453">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AP31PANDy_zCdSnD6v0Cfo2tsMulXWhV2R5N4g-E0eRCdQYFM8gjJ38lAA5w-0D62YmIfnrGmGMKV5m5Vhdt2iSERunOveQsOnoLjGORky_E06SChahEaLrp5NVDVHDOHb1IwPUst2y7VBlfIKEjOiKuRyQ-o8l34teMZw8TIcXCmkJuSIZz8duApkv41OeJ1oMBuAF_QfI8fced7KMjx_WkEQcMXTBCDpjSMsGUtmN5icgZwQgI5vT1NzXfeSlVokcSxspn2atw2BC0XA_-v3LV3kn-lsx0lJ2sz1Qh47sOnmB_R14ALLxaXH8FdfpRgFWADNCgsJ4OYQnG76Q9LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲- دو تیکه بسیار کوچیک از خاک اسپانیا، از جمله سئوتا ، که خیلی کوچیکه!  اندازه مثلا ۳ برابر شهرک اکباتان تهرانه!  چسبیده به خاک مراکش.  و بین این سرزمین کوچک اسپانیا  و سرزمین اصلی اسپانیا، دریای مدیترانه  و تنگه جبل الطارقه. پس برای مهاجرین مراکشی خیلی ساده…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6453" target="_blank">📅 17:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6452">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qqYioPYyzIyMeBqcnjm0wj4Z424FpiRQZgRoj3mDkjoWu1N4qd5S0PeFfvnoamXgnea8uDpmABne5s-j_sYhchgt6fx2W5WBHIAzjoFEWuf1wEjMh481ZWbB_NK06U7FCQyqHEY_YnAiwyzOnhgZ699BRx-gWedUcnHlwNkP9hOBW2Qq8eVA8WRvOULuXTf5qD-sNWocYjIlnsIpNfB-3I2vlCMenKyAbmuvg4zN0sX_rCf8ZAfYUqHU9zVBXqAZWYJ04dmQcbuoelB3aTg-5aoLf-YgIrDnEmnn9c_r9iWJsAxOsut4i_2YL1ca6Z05XO9tsW5PeSag5kEZA-BDCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا  دقیقا چیه؟ و مشکل از کجا شروع شده؟  چرا انتقادها به سمت دولت اسپانیا رفته؟   ۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،  حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند. …</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/6452" target="_blank">📅 17:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6451">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tysEp23eRWczRGVU0gOp-XXuBVC7iiYqkDg-RnJqHNEnK3dR_aO3n2eMygXN8C9itYlyG1XzSb-hxrz8KuNBH9nXIccjf9qvQRkfWL9mt3pkBAyhYDIW7R7lzEA2XRNfJq2_HGnH2bVfvzNGsOLV65PwMQtISAxICEwoJF6Civ-jc7qV-1m0WRBl-g22dlMlmEWW4RpT8qO9Y2jlhlp9TfDZ7CAo5QYeNVYPc58jg3qf5rD2ZP0EHtgi7PA0bL0VfwIlpYQFnTQcJHPFgygZc8qO4XiQdtCnEeLTnCezWwL2lwzUmBFPkAhRfq4hfLvmPAxsmjMxMDxdIH7vxrlqow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا
دقیقا چیه؟ و مشکل از کجا شروع شده؟
چرا انتقادها به سمت دولت اسپانیا رفته؟
۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،
حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند.
این خبری که می‌بنید و تصویر هم مال همون سال ۲۰۲۱ است که پلیس اسپانیا مهاجران غیرقانونی رو دستگیر کرده.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/6451" target="_blank">📅 17:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6450">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=o_VtMaxo-d0FHl3c-9b2IXUcmTOOMwrsmsdRLISV8fm7tVp95BkLRYRTvFvm2cyLSVDiRa9my1fxi7cHJRMOTcFb4GfIxJ_RbGHg57wHe3c_RslH5QYgpgkrHhNwvLVbV2AWR7wMyW80JBubgomS-eF68SBKCzwlX-p3VMA5gHNRVDlbcEp9nmw7qqJWWvyhEYjDdUjl3Dd3cXsGxl5d3knuO7oQkYbJQEqcP0iuVe-UNokXkLh2YycgpXYiPdCK1TTC4T-jajw70ZDTLJhfX69SnmYdF7dFY8e8_MS2jzTgteIV8hVGaDZsPIfvEQadg5BKNpyZyqQKXjAp1TNkMJa0LB2aVIetfmyshUddK_q1A9GqSaCYOqQuCRKHPuq8KT1870XVe84SVSKZ3qZ6uMtl3qfrDM6gIiUevhxMajIBrgpRwwgB9Cb4v-CuQWVSwIvNJAsnP3bchIKJVahtx3tmMGvrfjfEg8tht5O3OJTgIyWPAmZrzNmEcBKexUT6NvP1X7xQ3D2d9dSv7nYiTS9WDYbs8GL9qz3hMj5kC9Bmo7RAKYYcrZqAF-pR2c3-B_mPMQuo1PwFh-JV9aZTKlzFerOodTyXuEi9o4Skmx6Nzw3XUOpuK3qEUHNtOE56GpZMx76S31P_bNsm3ddMcIYvD3samYNm0tXW_h4_qvk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=o_VtMaxo-d0FHl3c-9b2IXUcmTOOMwrsmsdRLISV8fm7tVp95BkLRYRTvFvm2cyLSVDiRa9my1fxi7cHJRMOTcFb4GfIxJ_RbGHg57wHe3c_RslH5QYgpgkrHhNwvLVbV2AWR7wMyW80JBubgomS-eF68SBKCzwlX-p3VMA5gHNRVDlbcEp9nmw7qqJWWvyhEYjDdUjl3Dd3cXsGxl5d3knuO7oQkYbJQEqcP0iuVe-UNokXkLh2YycgpXYiPdCK1TTC4T-jajw70ZDTLJhfX69SnmYdF7dFY8e8_MS2jzTgteIV8hVGaDZsPIfvEQadg5BKNpyZyqQKXjAp1TNkMJa0LB2aVIetfmyshUddK_q1A9GqSaCYOqQuCRKHPuq8KT1870XVe84SVSKZ3qZ6uMtl3qfrDM6gIiUevhxMajIBrgpRwwgB9Cb4v-CuQWVSwIvNJAsnP3bchIKJVahtx3tmMGvrfjfEg8tht5O3OJTgIyWPAmZrzNmEcBKexUT6NvP1X7xQ3D2d9dSv7nYiTS9WDYbs8GL9qz3hMj5kC9Bmo7RAKYYcrZqAF-pR2c3-B_mPMQuo1PwFh-JV9aZTKlzFerOodTyXuEi9o4Skmx6Nzw3XUOpuK3qEUHNtOE56GpZMx76S31P_bNsm3ddMcIYvD3samYNm0tXW_h4_qvk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقاد یکی از سیاستمداران اسپانیایی
که مخالف  دولت پدرو سانچز است :
می‌دونید که پدرو سانچز بهترین دوست
آیت‌الله‌ها (جمهوری اسلامی) در اروپاست
و دوست خوب رژیم مادورو بود.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6450" target="_blank">📅 14:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6448">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=grR5M318DarDHdwM13xDmlTHLnpGurBJWHbKcoQxS9tbo_Tv1D9cACD_8M1uFNH1GtnpOvT-Rjcy-zHVLm3S2GhNo4DRYHz7jMRYhoEjZdkTF97E83N74hw_82jOju-6NnjOR39Xi_ipKOgcdMWqxSqsjDv2ac3J3zNhWq84wHQz79lDFMM_b4It45ajzD6N0X4UGrT6e1Mx-_1HvhX05K_Zz7qBQcR3jgX1tf3IEhx_7izKzxr1VFb22lz6KGshlDU3Bo5BOY_CGTDJyAGc5qkUh5D4vCRU0Sr1qIkFgFrB6ZVEaxiuCN8sNG0xCkPjVpc949-FwlzMHn_kOLdRaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=grR5M318DarDHdwM13xDmlTHLnpGurBJWHbKcoQxS9tbo_Tv1D9cACD_8M1uFNH1GtnpOvT-Rjcy-zHVLm3S2GhNo4DRYHz7jMRYhoEjZdkTF97E83N74hw_82jOju-6NnjOR39Xi_ipKOgcdMWqxSqsjDv2ac3J3zNhWq84wHQz79lDFMM_b4It45ajzD6N0X4UGrT6e1Mx-_1HvhX05K_Zz7qBQcR3jgX1tf3IEhx_7izKzxr1VFb22lz6KGshlDU3Bo5BOY_CGTDJyAGc5qkUh5D4vCRU0Sr1qIkFgFrB6ZVEaxiuCN8sNG0xCkPjVpc949-FwlzMHn_kOLdRaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟  دستاوردش برای انسان چی بود؟؟  به اندازه یک قرص سر درد،  تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟  اینها روشنفکرهای ما بودن!!  این‌ها بت‌های یک نسل از ایرانی‌ها بودن که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6448" target="_blank">📅 14:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6447">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q-C8K41dmI4qQsw9Xh1dTcZc2k1PTw-lTQY2Y7hG7wp5uKj2Cye__ABPmUu-3YeEZCU4b12no8spKA27dga_WSLtB_01_tH0K1IikmpxspCaudzCF0SS_WFf3MPlu_UVXd3XIM6PQqp8yGvW9GRbvEGQZmIaV2cDgrqaSBDPAtZiKiVjF3_o1EepQqkQb3lcrUd11xePkT4CydC1VaJehsZPK3tLBBc_uAH4SeqLh2h9XTATtqN0auQ6jAkal0iTux0UBXQsUi8dgjeNbsoDnbBpj5WqRGnawvrLvspoQR6pJVCEuT9sWYUUGvHgzQVbc4_TM0kfp1MgyTnE7c-8kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟
دستاوردش برای انسان چی بود؟؟
به اندازه یک قرص سر درد،
تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟
اینها روشنفکرهای ما بودن!!
این‌ها بت‌های یک نسل از ایرانی‌ها بودن
که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6447" target="_blank">📅 14:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6445">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l3-QfLT5olA7iFcxirmbJjIAhePApI6GoA9Ic1-TyeVXhqdgFpqdKkhAMvOoXbcIl75lif-e8W09VU8IM7VLtgrL-avT1olTJ1GK_loG_Psz7ZcQ8USZU0ZGYn0X49h0oFFTzL7j7CmWlqyanhn2DcI3CZUb0ICOiMTHTkK925AqLSOgs50VqtQHwQDXxlEV5HcjTFHUuJJN2XtY7ANmchKeNHtNpfc0yVK6hNEk3ol038dkCxsNs-dMvIU67H9E9GGa8GLWrsxdu04DfCoXxBpW7sPxYXcVZsGM45WqqTyElvVqOcN4PwLcIaf7DhV3naxdQfLZc5UMYjmPYKJLCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=VVvgeYwxcAdwGn0WyRpOVcakfRg244suERMHy5JosMbORujbjrRO6KgfX8sqiaIq9RiA-zq_SvfrF6y9TQsQVo_NlnIyNiohDtzc1TX34mtx1F6DhlyQy-nh-0xGzQdi4QVZb9sxILfFVKo6WrVPj3uU6_aV2S-YcZu3dwGHJ6EmCRLQeLdu8YKkvme96Xp9p_tQkk7JnXHCXvTbj8pCo5BM9ltNJkkoHXX4U-pUbb1SyHThUJjhv2R6dWCNcZfi8ai3Cu24tP5XBKho2dEN8QwUwLnzlQN2PlpUaT9kKSunI1jxseknsXrN_qsg17TtAxwuEZcUS_PaUw9hTzXBboi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=VVvgeYwxcAdwGn0WyRpOVcakfRg244suERMHy5JosMbORujbjrRO6KgfX8sqiaIq9RiA-zq_SvfrF6y9TQsQVo_NlnIyNiohDtzc1TX34mtx1F6DhlyQy-nh-0xGzQdi4QVZb9sxILfFVKo6WrVPj3uU6_aV2S-YcZu3dwGHJ6EmCRLQeLdu8YKkvme96Xp9p_tQkk7JnXHCXvTbj8pCo5BM9ltNJkkoHXX4U-pUbb1SyHThUJjhv2R6dWCNcZfi8ai3Cu24tP5XBKho2dEN8QwUwLnzlQN2PlpUaT9kKSunI1jxseknsXrN_qsg17TtAxwuEZcUS_PaUw9hTzXBboi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شما مشکل کفش‌هاتون توی مسجد
رو حل کنید که پلاستیک به دست نچرخید،
نمیخواد نظم جهانی بسازید!</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6445" target="_blank">📅 13:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6444">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V4jiQ8FItSB1swctGCSCa_4U8L8k2pSD1OXn7EQU1inC57lVkyp7WvuobaRh-ZkxSUSGfooSyb1i5Wq04zCMPW147KbYxOi27LoCqO_V-o875slpvqdI1UrluctrfBXKvfaXO8CvKBi5PE8oEtyg7xgjaRtyhkZ7n1TqkDQVY_tOBUeet-ma8hqg7UaIKiLRIQgoj2HzCmuNklKCcNr4vYyi0c4quM3YLWvxWfICg5nJM3SF2BC-lMEYXwzj6lGL_ObK5PwcESn_ezQvEs-GQ00gXUmKgojYzhQmceNuB8cZEnrL2RsyqPsJmEikoQDoTqMCUQ1vXGo7WBk7nAI_1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عباس عراقچی ۶-۷ جمله نوشته که خط به خطش دروغه!
نوشته که مصر یک شریک مهم منطقه‌ای برای ماست و نمی‌دونم امنیتش برای ما فوق‌العاده مهمه!
در حالی که مصر و جمهوری اسلامی ۴۷ ساله هیچ رابطه‌ای ندارن و مصر حتی ویزای توریستی هم به شهروندان ایرانی نمیده!
همون موقع که پروازهای جهانی در اوج بود، حتی یک پرواز بین دو کشور هم نبود!
نوشته که اسرائیل علیه اتحاد و همبستگی اسلامی است!!
مصر حتی برای کشته شدن خامنه‌ای، یک خط تسلیت هم نفرستاد! براش این اندازه هم اهمیتی نداشت! کدوم همبستگی؟؟!
🔺
دیروز به دو کشتی حامل گاز مایع در مصر حمله پهپادی شد، دو تن از مقامات ج‌ا به روباز گفتن این فقط یک هشدار بوده از سوی ما.
دمپایی پوشان یمنی هم گفتن کار ما نبوده!
حالا این اومده میگه ما روابط مهمی داریم و همبستگی اسلامی!!</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6444" target="_blank">📅 13:27 · 09 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
