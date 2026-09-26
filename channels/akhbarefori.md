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
<img src="https://cdn4.telesco.pe/file/JKgikmVwZj_ooOa_vGgHKZPqgerJri3mvV_uW79Ynyxu-LQ8UCU-Fx8vc6PktmO4UWPN1L05YWGBf3jXd-LuuIIFmiiGcq30sg6PkpOjBstc5z4msYrSQNuzzNkiawTlfApv3FGTOVNy8Z4vRLfaPJtYJL7X8tb8sIzye9fEHIJoECtfM0VZ46k9IJOZMcYNZp-RWdpnOZUPq_XBq_90X142rKrjDhD-QMVF-eq5jC71OfM8zSPJKUxJ9kEP9k7CtCSd2OlP3w9Bb7G4enNi2oU6Q-Nkne2t0oa0HJFnBM5WWF71EhOQ8-6DXwRpQjspUGbgVj9A9u4VpsewakrPYA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.33M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-05 02:32:07</div>
<hr>

<div class="tg-post" id="msg-693303">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f6e6adadb.mp4?token=XprQxRPJkCcCTIQ1XB1_-jRtQICL762-q9nRf-uOXYTzY6daaI-mWbehGPQ9Hfv7TWhcYdD_1LzPEKBwYvlA6wr8s0Mwo4HyRwLublwDqL_8cQDdeF3-te0HKTU6QHh2O_Sr-Abu_nUTk_VMcklJeHc63nwYbJQbJU7vRM3C4uya3wvhR8BM6toTQxMvXYHrSrzLcBjp5GXmNUb7Unpgo11I8p2xLBt5k8jUyn4Xg_NkXUDnPhAeatnpx85B63OgLsW7FPgvDc_PmZUlTD_qNBZwc788WsfG1RqqylsdzX4uqtsTEmf8ayXUJmeEeDOgQIvyGLPxrs3wQ3zCGrYc3zgAK8wvuRDMsuW9gPKsxV9-tOYF3NxAXcx9z0UT0OGPo0vVjo8Fa2h4MRDjQco6f92l8dmtgDIfO9Zk3B8QBTWH5C3XsCVjns2uekl7wOk_FDxMHakB0nyFLZqWnArwJe-1lckm68qWILSqgIl2Q4KOgg_mrtMiL6byAhlvExArPq_fzlP8t9wcAVZvrLzLxGTDh2YwNp5xeQ2j4CX-LvhL8qRjDfp9lZsEt3dJ7otZZTBmcBMZPY_Ucf5WIh0YBYC7WcLuwzkazxqolyReOZ4-qRkAIxeb6esHL9mQL3F_RdpGZ5WVECErIJr_rO4l5Isw7Pmk2LvA1UPk5XDcIHE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f6e6adadb.mp4?token=XprQxRPJkCcCTIQ1XB1_-jRtQICL762-q9nRf-uOXYTzY6daaI-mWbehGPQ9Hfv7TWhcYdD_1LzPEKBwYvlA6wr8s0Mwo4HyRwLublwDqL_8cQDdeF3-te0HKTU6QHh2O_Sr-Abu_nUTk_VMcklJeHc63nwYbJQbJU7vRM3C4uya3wvhR8BM6toTQxMvXYHrSrzLcBjp5GXmNUb7Unpgo11I8p2xLBt5k8jUyn4Xg_NkXUDnPhAeatnpx85B63OgLsW7FPgvDc_PmZUlTD_qNBZwc788WsfG1RqqylsdzX4uqtsTEmf8ayXUJmeEeDOgQIvyGLPxrs3wQ3zCGrYc3zgAK8wvuRDMsuW9gPKsxV9-tOYF3NxAXcx9z0UT0OGPo0vVjo8Fa2h4MRDjQco6f92l8dmtgDIfO9Zk3B8QBTWH5C3XsCVjns2uekl7wOk_FDxMHakB0nyFLZqWnArwJe-1lckm68qWILSqgIl2Q4KOgg_mrtMiL6byAhlvExArPq_fzlP8t9wcAVZvrLzLxGTDh2YwNp5xeQ2j4CX-LvhL8qRjDfp9lZsEt3dJ7otZZTBmcBMZPY_Ucf5WIh0YBYC7WcLuwzkazxqolyReOZ4-qRkAIxeb6esHL9mQL3F_RdpGZ5WVECErIJr_rO4l5Isw7Pmk2LvA1UPk5XDcIHE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مضیف الکریم
نزدیک ترین رستوران بزرگ به
حرم امام رضا علیه السلام
غذای با کیفیت، قیمت مناسب، پذیرایی بی آلایش
⏰
هر روز هفته
ناهار از ۱۲.۳۰
شام از  ۱۹.۳۰
تا اتمام غذا
روزانه و درهر وعده فقط یک مدل غذا سرو می شود
جهت دریافت لیست غذاها و تاریخ سرو آنها پیج مضیف را دنبال کنید
📌
قیمت تمامی غذاها با برنج درجه یک ایرانی،
۳۸۵ (سیصد و هشتاد و پنج) هزار تومان + ۱۰ درصد مالیات بر ارزش افزوده
•
📌
مضیف هیچ ارتباطی با آستان قدس و مهمانسرا ندارد.
📍
آدرس:
حرم مطهر، ابتدای خیابان شیرازی، مجتمع جهان نما
ورودی پارکینگ مجتمع: از شیرازی ۹
•(اطلاعات بیشتر رو از طریق پیج اینستاگرام پیگیری بفرمایید)
https://www.instagram.com/mudhif_alkarim?stkn=N3gwam9rN3BkOGtw</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/akhbarefori/693303" target="_blank">📅 00:31 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693302">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acd7b5d2cb.mp4?token=aEuqky0QJrHbDT9ZuVwq-vwuhuGKqEPjP1XE5T_zxYmaNhxIwZw4fGpbQCjxloh1MRbB6bGoXixu7f96R9GprmZQGuBbw6t4MyX9h4MnnmpuNZ7n3WjrqNKEA315rWvFGbt7Z1taVFMdkvH4JjdCEKGihW7f46hQOhvniyg7uei5mh8HvHu3b4IrhmYCreex0RnVTHr8Rfo_OnxuzKm31WZJXrsjRedWTICWHzjHB4BCyeESy3w157DoZOXl9NCwhB0oGnfVXYbU0G1sMcBeW-68SOlWXHhx9de9iVFcN6xW25r559V-wA4jP6P4AiQhu__RoKnyKvXmR9PSP6OJcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acd7b5d2cb.mp4?token=aEuqky0QJrHbDT9ZuVwq-vwuhuGKqEPjP1XE5T_zxYmaNhxIwZw4fGpbQCjxloh1MRbB6bGoXixu7f96R9GprmZQGuBbw6t4MyX9h4MnnmpuNZ7n3WjrqNKEA315rWvFGbt7Z1taVFMdkvH4JjdCEKGihW7f46hQOhvniyg7uei5mh8HvHu3b4IrhmYCreex0RnVTHr8Rfo_OnxuzKm31WZJXrsjRedWTICWHzjHB4BCyeESy3w157DoZOXl9NCwhB0oGnfVXYbU0G1sMcBeW-68SOlWXHhx9de9iVFcN6xW25r559V-wA4jP6P4AiQhu__RoKnyKvXmR9PSP6OJcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌧
چسب همه‌کاره پلی‌اورتان آرازیم؛ مناسب روزهای بارونی!
برای آب‌بندی و درزگیری قسمت‌های مختلف مثل:
🔹
درز پنجره و درب
🔹
ترک و شکاف‌های ساختمانی
🔹
درزهای بین سطوح
🔹
جلوگیری از نفوذ آب و رطوبت
💪
چسبندگی بالا و مقاوم در برابر رطوبت
🎨
رنگ: خاکستری
🔴
قیمت 1,798,000 تومان
✅
پرداخت درب منزل
ضمانت تعویض سه روزه کالا
قبل از شروع بارندگی، درزهای باز رو جدی بگیر!
😉
خرید تلفنی
👇
https://memarket24.ir/product/fast/63720/180124/</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/693302" target="_blank">📅 00:31 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693301">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aBUd53iPH9HMbtKaSKe1PrnNwiKBZnFfrmiCIgXdMn5jFJveIlgNgt3lwvLgRWBEO9xfDHlh043KtTwZDuhIBKhcrCc5QLo3v2DisM2JBYHnLHRMtDB_9U8Gzf1bufKKJwfosL-iNy5Z6cJ2Xml6SO1wCrzWwmteTClOuIVNWRCyD2-vCN0SZfC4sCTXuw-WAJuLX6ECAS_4ck3t_HpDtRcV5VxDiw0fl176wv2y1usLNU7KTsOal6xBESkUDyGijObO1-VIFZ4dNkfhuO4zhbox45ykexcaEoJSN-bfeYGIYaWdz6USHqZ9Jc0gyizjLW91cccYXTt4gYrXO2zx0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انگشتر نقره میخوای ولی از قیمت های زیاد نمیتونی بخری؟؟؟
💎
کانال زیر انواع
#محصولات_نقره
رو با پایین ترین قیمت میفروشه
👇
😳
https://t.me/khalijjgallery
https://t.me/khalijjgallery
❌
تخفیف ویژه برای خرید اولی ها
❌</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/693301" target="_blank">📅 00:30 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693300">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AxEMgz1VgSE_K6Yct5BLBRGqE3BR7Rm_1o2Itrdydd0d7N4JnEiBzo2yl8QlCt-mv4028iTB5uaXzOM5fL4z9637Dae2L4DSqLb9yPY5X0_Yj_tibOtjM0qhWdQHgGp3rGzEn1FBwwqtuGipjtGzk3zIzd5g9pKrKvFG3aW6HDH9q76UGhlTPXNkMHuTykC3ciCnccizqpJGZmKxtxqHF0A6TZ_alvXP0fC_A83iufx9Fn504Ij2YvI9U42gmBrOcVOLUO6CvzhBU4kE_GN234wT-193pFWTmHqGRcHIKKMUOhApWzT125KqwNMgNQfQUOJ5koSBhvyxfLsSMeJ5wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری زیبا از ماه کامل امشب
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/693300" target="_blank">📅 00:28 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693299">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c245685da2.mp4?token=n80AibVqDIZoeP1VISGAsR5E0q42csRc4o9tmij-Bj5Ndg4t0vks0rAd_Br8uJiOsn67gkxcxpkgxwAArc5IP3p0KJ9FAKp1rTLJhKBnS5IFsI2_8U-eAfhAmJsx1h7AAKf4RLrKPOZfxgs7SeUZC4qbk9RDQiCCUocZEaqEsKCapEd5VUFSbx1S6Ft_8JeM7prGRA3iqCIDmDAV_9Eb7KCaP6UDFfMkjS4JzLQzz3GQyz-qpqMZPO3BNlXM-LPLFa31z25Te2fCs0cdxTA0pi_nQGKK_VLPaZSfm9Yh0BmwSWknPNhr7Ib-j8AYx1owG3hUbUiKRLuL5Ggf6wjhLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c245685da2.mp4?token=n80AibVqDIZoeP1VISGAsR5E0q42csRc4o9tmij-Bj5Ndg4t0vks0rAd_Br8uJiOsn67gkxcxpkgxwAArc5IP3p0KJ9FAKp1rTLJhKBnS5IFsI2_8U-eAfhAmJsx1h7AAKf4RLrKPOZfxgs7SeUZC4qbk9RDQiCCUocZEaqEsKCapEd5VUFSbx1S6Ft_8JeM7prGRA3iqCIDmDAV_9Eb7KCaP6UDFfMkjS4JzLQzz3GQyz-qpqMZPO3BNlXM-LPLFa31z25Te2fCs0cdxTA0pi_nQGKK_VLPaZSfm9Yh0BmwSWknPNhr7Ib-j8AYx1owG3hUbUiKRLuL5Ggf6wjhLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیو جالب از وضعیت دو مدرسه دولتی و غیرانتفاعی در کنار یک دیگر، استان مازندران
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/693299" target="_blank">📅 00:27 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693298">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
منابع عربی: شلیک سه موشک کروز ضدکشتی ایران به سمت تنگه هرمز/ هم‌میهن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/akhbarefori/693298" target="_blank">📅 00:24 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693297">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfc30cdd6c.mp4?token=YkHWD5dsetD9EGEoZWB43fGbPW9ONX-OrtrEO2TTX0OmOoG0WosCtkBePT7YP4mo18c6O42beNzzpy4NgSZIhkOQrTWnZZcLwGm9hfJzA4mcLhPt8uVZXYTqtoBqLDCbE5uzMVN7am6zUSPjUd3l3VsgE2oDZyohhkqbCDSSw9I1Ug-jwb3SROwU2fGJT82ODm2LxS0MAT_MXH7-jsSuMOf_-yGWs6u5vUwaopwg2A9tauvoGz2YfgQWN06Gr7XvNJCEIz7Pq-BBgpJbHHL4eV4qOjC_dEodLqAvY9Li2mb8Rkwv0hkhGeoxVnIH_ULmIElYlxXOPzbVUiyuOFOpaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfc30cdd6c.mp4?token=YkHWD5dsetD9EGEoZWB43fGbPW9ONX-OrtrEO2TTX0OmOoG0WosCtkBePT7YP4mo18c6O42beNzzpy4NgSZIhkOQrTWnZZcLwGm9hfJzA4mcLhPt8uVZXYTqtoBqLDCbE5uzMVN7am6zUSPjUd3l3VsgE2oDZyohhkqbCDSSw9I1Ug-jwb3SROwU2fGJT82ODm2LxS0MAT_MXH7-jsSuMOf_-yGWs6u5vUwaopwg2A9tauvoGz2YfgQWN06Gr7XvNJCEIz7Pq-BBgpJbHHL4eV4qOjC_dEodLqAvY9Li2mb8Rkwv0hkhGeoxVnIH_ULmIElYlxXOPzbVUiyuOFOpaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
به نظر شما چرا تریلی ها یک چرخ معلق دارن!؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/693297" target="_blank">📅 00:12 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693296">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
درگیری شدید در مرز افغانستان و پاکستان
🔹
گزارش‌ها از آغاز درگیری‌ شدید میان نیروهای طالبان و پاکستانی در خطوط مرزی منطقه خارلاشی در ولسوالی دنده پاتان، حکایت دارد.
🔹
بر اساس این گزارش‌ها، دو طرف در این درگیری‌ها از سلاح‌های سنگین استفاده می‌کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/akhbarefori/693296" target="_blank">📅 00:07 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693295">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔹
از خبرهای جذاب امروز و امشب جانمانید
🔹
🔹
مذاکرات نیویورک چطور شکست خورد؟
👇
khabarfoori.com/fa/tiny/news-3248085
🔹
ترامپ پیشنهاد ایران را رد کرد؛ جنگ شروع می‌شود؟
👇
khabarfoori.com/fa/tiny/news-3247922
🔹
موج عظیم ورود غیرقانونی افغانستانی ها به ایران | ویدئوی عبور مهاجران از مناطق خطرناک
👇
khabarfoori.com/fa/tiny/news-3247956
🔹
بازسازی جنگ سوم ایران و اسرائیل و آمریکا | سه روز نخست جنگ چه اتفاقاتی خواهد افتاد؟
👇
khabarfoori.com/fa/tiny/news-3247830
🔹
اقتصاد زیر فشار؛ آیا یک شوک بی‌سابقه در راه است؟ | این محاصره تا پایان سال دو دهک دیگر را به فقرا اضافه می‌کند!
👇
khabarfoori.com/fa/tiny/news-3247997
🔹
برای خبرهای بیشتر، کافیست کلیک کنید
🔹
khabarfoori.com/hottest-news</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/693295" target="_blank">📅 00:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693294">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yb3JAagYZ-HlSPN6Nq3x7nEp1Tca8C1I2XCOCcMM9B8Im86xcZxnhkjlQgLSRBRXjyGDfG-MirTXJKvTL3sEXdRoMIiwKHFPBZifaWQt4fyX-9-ecVVr7F27RAq2_K7IOByCYgcy8rltHf_GruZ01JsiIaRRQgY2MCcn1Vyc5ejCsRStHZGsM9II6L1HaEQXIBj6rvSuD-V4LmKjUSc7OnYoZn7aqJmf0KWmqTWury6WwYx3ndgacpCqczGNVl1QUEWR_lcWmdG9o8UsUWhQn5Fr_sbDrFRhqVzPYHtzcLK8QTRFFv6SubZ1WR32PFgYuRCIMfNqZMTtCTcvPdVGnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/akhbarefori/693294" target="_blank">📅 00:00 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693293">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PWNlxoHoq9u_q8pbXNmFTSDfrIn4wPaoxMXvOgzsBMZNZ7N8I05RhU9mwQP_iNAD9GP8hZ76vTfsgFQ1S3bElnmPukacpIP91LxO48-znNnqyhUKSKxiheB2l5rFzzvQbwPYsJI0HAWlfth_OiSjLWfTPI8lz8DI7pY4pmw4ZR8vBsSDGyuLdifaBeKE2iLogBJ2urZB5UUAU2l8A6zUH1D9YaLpL7eZ8TeHYwTzZ603ksW_3GrSNjiOn2HZfih3lOvdrfgPC7SriDI2_ytJLkPM7WgrDuRN0tTlAopo0Yx1b5chKatbfK0zbsXZJKCCFK8ehyW-tGptymXwWBYT_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
صالحی: فصل جدیدی در روابط فرهنگی ایران و روسیه شکل می‌گیرد
🔹
وزیر فرهنگ و ارشاد اسلامی در دیدار با وزیر فرهنگ روسیه در سن‌پترزبورگ، بر توسعه همکاری‌های فرهنگی و هنری میان دو کشور تأکید کرد و گفت: با برنامه‌ریزی انجام‌شده، اتفاقات بزرگی در ارتباطات دو ملت بر پایه فرهنگ و هنر رقم خواهد خورد.
🔹
سیدعباس صالحی همچنین اقتصاد فرهنگ و هنر، تولیدات مشترک، برگزاری رویدادهای فرهنگی و تقویت همکاری‌های آموزشی و علمی را از محورهای مهم همکاری ایران و روسیه دانست.
🔹
او با اشاره به ظرفیت موسیقی سنتی و نواحی دو کشور، آن را فرصتی برای تقویت مناسبات فرهنگی ایران و روسیه عنوان کرد و امضای موافقت‌نامه تولیدات مشترک سینمایی را گامی مهم در توسعه این همکاری‌ها دانست.
🔹
این دیدار در حاشیه سومین کمیته فرهنگی ایران و روسیه در سن‌پترزبورگ برگزار شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/693293" target="_blank">📅 00:00 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693292">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/203520b431.mp4?token=f9E-t_gFJUSn9gG13FCej6ZSC38vmYGewilE9Z6HZ_Fj2W2DnHSMPqdcORKc4_sgUz5QgmbvNrk2sCJygTQwmtJ_kSZ9lv_iMwS9kcCxuWcEqrmKzHj599nFhYMuua1vhrp72NEW7DFtRHqVc8w8l68nQN7CGlVeqmw5odnWv0v_iH4rynuG0VaPRwTgjUSEoKek0RrbT8-OSDvN_QyuNkoSmX6HL80TREIDeLNtDSVsyRw6JyPVTq4rB3XmyrruWyOv72ApVUdpdZIIOGThO6l9DduM4ihbir0j3Wj61ArDU6P8NeJNVgT2Bgv5ZNnD2vGbvgMFI_4E2d-8BkUMNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/203520b431.mp4?token=f9E-t_gFJUSn9gG13FCej6ZSC38vmYGewilE9Z6HZ_Fj2W2DnHSMPqdcORKc4_sgUz5QgmbvNrk2sCJygTQwmtJ_kSZ9lv_iMwS9kcCxuWcEqrmKzHj599nFhYMuua1vhrp72NEW7DFtRHqVc8w8l68nQN7CGlVeqmw5odnWv0v_iH4rynuG0VaPRwTgjUSEoKek0RrbT8-OSDvN_QyuNkoSmX6HL80TREIDeLNtDSVsyRw6JyPVTq4rB3XmyrruWyOv72ApVUdpdZIIOGThO6l9DduM4ihbir0j3Wj61ArDU6P8NeJNVgT2Bgv5ZNnD2vGbvgMFI_4E2d-8BkUMNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توهین نتانیاهو به سران کشورها: اگر بزدل‌های دیگری در سالن باقی مانده‌اند، همین حالا خارج شوند #Demon
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/693292" target="_blank">📅 23:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693291">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15026e426b.mp4?token=advj7Sd-hBSo-P5nWlprWFgaf50RmbhmNDtdZlkmPD5yFxbAXSwpM7nwk-EBfs-w6vvH5IrjDwBH8uy6U5_Y7d9cgUbgavU98jiDPSuB09Yq3-eOwvUaMnZb_bBYDGx9aJpCXsrbamhX0dAEfIkoXweEiB4ksSg0KW8Y-pYItzx48kE8ZIcaZPsJSR8ReAWs79VJJ_G0n02DA9yVYEslj-nfLpn8aTNGwWq02bxCSpFMqmeFMmB1EVDKPBRs-a1oiIwRcpbSme_rRfkb9SCRF_WEYm7tzoswqmA6zUH8fvvJNCjRY9PgkxwrwerUfJ_IxtMxz6mz-LxXXzU94V-Qng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15026e426b.mp4?token=advj7Sd-hBSo-P5nWlprWFgaf50RmbhmNDtdZlkmPD5yFxbAXSwpM7nwk-EBfs-w6vvH5IrjDwBH8uy6U5_Y7d9cgUbgavU98jiDPSuB09Yq3-eOwvUaMnZb_bBYDGx9aJpCXsrbamhX0dAEfIkoXweEiB4ksSg0KW8Y-pYItzx48kE8ZIcaZPsJSR8ReAWs79VJJ_G0n02DA9yVYEslj-nfLpn8aTNGwWq02bxCSpFMqmeFMmB1EVDKPBRs-a1oiIwRcpbSme_rRfkb9SCRF_WEYm7tzoswqmA6zUH8fvvJNCjRY9PgkxwrwerUfJ_IxtMxz6mz-LxXXzU94V-Qng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آغاز سال تحصیلی در بعضی مدارس اینجوری بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/693291" target="_blank">📅 23:43 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693290">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MWT-beOrb2BSJDRlJMUr_K5joBNu39eLHnKtJaYYipX_mYokC1e3bzvHyC6uSYxWKE1b2iQGTthEmJmYial9WlK_X6Dlvn4jZnkpTIjSA0J5JNsrEjosQ8DZYzDsQ16LcpTuM-QQnl_Ja90XZ4AC2LtgOdaVRnySbnMuxlY79xHtjHjDFbSYFW2fck4HVzHMb_X19jxxwoES-08Q89K27kGzxJwtarrgua8_hZDLguNZDqDXctC4miOh7G8MFOtlj7pdJUOZHdiyhVNTX7D1GR49-WB4ALoATr8KYsBy5D28WDaViFJMgHaiCXIzj_2V5jI2WiVKEoPNktfqgaLtEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«چاو مبارک»؛ نخستین پول کاغذی ایران
💴
🔹
حدود ۷۲۵ سال پیش، «گیخاتوخان» حاکم مغول ایران فرمان انتشار پول کاغذی با نام «چاو مبارک» را صادر کرد. این اسکناس در «چاوخانه» تبریز تولید شد، اما به‌دلیل بی‌اعتمادی مردم و استقبال‌نشدن از آن، مدت کوتاهی بعد انتشارش متوقف شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/693290" target="_blank">📅 23:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693289">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50d270ec2f.mp4?token=je01wXdotIGv6xkhEquFQnfcP19VaD4IgTXaoNwY1WaZXrH23KzYB88CXHtDKbZkHyE8MKsqjrQb5kQnxT-5ww1aoTl3VnU0C89bc95JLTicUJWCx2-YuyEqyUEsd_N9ie5a1WCFTInIIJCjXGP_YymZP2vY9bAtl2EjBr2-VVMZ7CWi1PDuqPumdsfwX0-32qX1dAFS6rDaxDslpgp0PpWsoC-JaQYK7RP8y-rEaYoMUZd3_kF8oTrlwD4_WE3IB9wQ5xn_BX0xJtjeFFKn8DXJWwu4FiIxZZE5zSjWakZoonAeLIrzeEul11Yg0yyWKKzZOd3XHyrIvMyUIFhRjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50d270ec2f.mp4?token=je01wXdotIGv6xkhEquFQnfcP19VaD4IgTXaoNwY1WaZXrH23KzYB88CXHtDKbZkHyE8MKsqjrQb5kQnxT-5ww1aoTl3VnU0C89bc95JLTicUJWCx2-YuyEqyUEsd_N9ie5a1WCFTInIIJCjXGP_YymZP2vY9bAtl2EjBr2-VVMZ7CWi1PDuqPumdsfwX0-32qX1dAFS6rDaxDslpgp0PpWsoC-JaQYK7RP8y-rEaYoMUZd3_kF8oTrlwD4_WE3IB9wQ5xn_BX0xJtjeFFKn8DXJWwu4FiIxZZE5zSjWakZoonAeLIrzeEul11Yg0yyWKKzZOd3XHyrIvMyUIFhRjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
داماد حسن روحانی: جلوی خانه کسی که به بنیان‌گذار جمهوری اسلامی لقب امام داد، قائم‌مقام جنگ بود، دو نشان فتح و نصر گرفت، ۱۶ سال دبیر شورای عالی امنیت ملی بود و دو بار با رأی مردم و تنفیذ رهبری رئیس‌جمهور شد عربده می‌کشند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/693289" target="_blank">📅 23:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693287">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20257d6f8e.mp4?token=fynG-f4E0XUMYOxDcZMod6eacqm09893NgstdM982vzfkpaj4qjJQPVNHDvxmEGH-lX3MpcqsQm-XQBj62rGARD1h9w8otn-r1twGH-EP5bqodc_HMKCyKmAzKwKcAkETE4MzNGgqWJ-RWLk0k_U6s7_ljvtd3y_YqbS56meelADGF9CrZbO9VZTUmTD66djiebe2cL_fHEj1ckaVXXYTawxz2csGT-3TabMBQWLTJlovRRC-CxMrO7v4GMXiIB5WDHDHA2xDDBJIDx2yB81HnrRwpDWJKexpqImSUlKwNWrDC5q0SyNLNate9lzQ5Y662Zuky72wxFhCGVjCyPLpYfiafVHYCNSRJakUjlqKQMg3iYoffLryL4tYIFi_KKZ4HAdSl1arspzkH4rfL7qXttjemKFYi7Ujm_ujv9wxIu7N1dIIGaQYflyOwPBZureOSlrzokyghnhkcAN3UsByjKIAIY-4LLu58bYQ5qRqPyRGs3vrf_NRnJ1B0BZOqc_BtAVFHjwcZR_HE5WY8UfSGg5d-W1vZfDOOqgihWENqrTbVlyvoFmKJJmHiMUySWA3DBBoC0VXhEkGwTuA7oT5GKBZE9T30PYm20vJJE72ftlhBK3Na0XUowlZGC0hsbsrh04fdp6ojnd_9bz4cuKvy-ruRN2VYXN3O7A7CXCY1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20257d6f8e.mp4?token=fynG-f4E0XUMYOxDcZMod6eacqm09893NgstdM982vzfkpaj4qjJQPVNHDvxmEGH-lX3MpcqsQm-XQBj62rGARD1h9w8otn-r1twGH-EP5bqodc_HMKCyKmAzKwKcAkETE4MzNGgqWJ-RWLk0k_U6s7_ljvtd3y_YqbS56meelADGF9CrZbO9VZTUmTD66djiebe2cL_fHEj1ckaVXXYTawxz2csGT-3TabMBQWLTJlovRRC-CxMrO7v4GMXiIB5WDHDHA2xDDBJIDx2yB81HnrRwpDWJKexpqImSUlKwNWrDC5q0SyNLNate9lzQ5Y662Zuky72wxFhCGVjCyPLpYfiafVHYCNSRJakUjlqKQMg3iYoffLryL4tYIFi_KKZ4HAdSl1arspzkH4rfL7qXttjemKFYi7Ujm_ujv9wxIu7N1dIIGaQYflyOwPBZureOSlrzokyghnhkcAN3UsByjKIAIY-4LLu58bYQ5qRqPyRGs3vrf_NRnJ1B0BZOqc_BtAVFHjwcZR_HE5WY8UfSGg5d-W1vZfDOOqgihWENqrTbVlyvoFmKJJmHiMUySWA3DBBoC0VXhEkGwTuA7oT5GKBZE9T30PYm20vJJE72ftlhBK3Na0XUowlZGC0hsbsrh04fdp6ojnd_9bz4cuKvy-ruRN2VYXN3O7A7CXCY1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کارشناس مسائل منطقه در شبکه سه: اگر امروز در مقابل محاصره هوایی اقدامی انجام ندهیم، قدم بعدی دشمن محاصره زمینی است/ می‌توانیم بین پروازهای غرب و شرق جهان دیوار ایجاد کنیم و روزانه ۲۵۰۰ پرواز را مختل کنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/693287" target="_blank">📅 23:26 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693286">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
سخنگوی ارشد نیروهای مسلح: از ترامپ و نتانیاهو و دیگر قاتلان امام شهیدمان نخواهیم گذشت؛ این موضوع دیر و زود دارد اما سوخت‌‌وسوز ندارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/693286" target="_blank">📅 23:24 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693276">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A8Bj-t-HnScK4DicPB5E4sWvMba1H9q5FdWjXnxxe-p3u01N4cgFVDbSBnVjP3aK9Og1sHqW87wEnNgMYpK2fqRAUqKJOuQ7rIfbo8n7d5PFcosN1oV8V-IqVbWt1fISMqUFNRA1KAwfO-xKBt-ieINuek8jvLQZRCvWeR2hwTYDDg1j_PBdgM3nTl2knwK1uoX4MxV_5gXs2bF02x4m6mSscjKIQhvq6cX-ATssV1sYv8ZjFpdRhGCpelSN0UN8E7oXXBF3__eYlP102XyVTRtnapbuDUIQ2y2wEqftYjI1WZMSgfPpdI_4OahBRdwepl9DAbluF8hk5G9WJaeF_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BrzKUs7MKJ6wEwnOdhP6iMtwUfOhJIptNPwVDmbE0SOoGI4Q-svKCgmSsIcrd8IQrBWEMk7ewH01jFrtbz_2zE6YoJs4zMsZAJmyttReWclp1tIvTQnmWM8qzan9cp_Jo9wSnYZDZvQmD3meszqBRUYq2n4PMGHiG8S3NUkzzPrhZCq3OIRRMMoL0o2qhKGn8lcqSmF9bcYklPI8Ocs2ZNBdQ0wHRrSo3VsiPd0azi3K3da9nUf3koIpsw6iX4QNEe6PkxkhIU5TDWq1zhxfkTizEKYSOMFU5gHiuYo5wfsoTiZF-cCYBdRPmQHkpX2f_gcJvHLpHJlyZwe2l2Xe9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WRQBBn4StQ5weNELVIxbQKDsVjVL_8gHiJXLM-uimwod89eg8QfL_wKh5X5CI1oPVaYFYCt1ZbpdXtv9e9yg6tqG_FFmnzklfr_vD_50wY20LWUXF1Z1ltU_l3vwR5aLwIxp5yUUEzqWH2rMGfIXkQ-2VTtBZA3ktSQuOseRsb9HmU_gUL_Bep5ZWj1s8lA7An8t8BlBLoME2ip4pKnvcOlX7fTOWUuj-3nTiMUk4lNZ9Rm0TJjMLYN2Hr8tKdMTSD6wq8bKwzWcm8DNOAHNHO8rIV3YXpHxESmoObV_QtyQGkFIchPzj1jN9zreBJlxgMXetHTrcBWiyPTbq4HySw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pPDO897mdJqr1r2I98jdb3mT3ZW1EQEq4ezYu7H34CRk3f6LWCrR5bAGLDDsZrSnxYMnGPhMaT2ibZ0x0TYWj-Rg5w8QVW1se2nyzuv7pNdkZ7e8su9ledAbnp1406bAqpEDBQyGcg72CODiwue2YSy73V6NPl-nMhNuubXinf9Hn07jrQYZ0o2fWaom9Z41lplMJ8fgCBrF4A5KKRW8fT4wtZC9RBrWtTHi-l5UwNny4EGSovRBq3p_Widm6r7gE8li3qM4TkIob_mUj4VVjN8bPkJtp1pR-XkqRoMYQNnSU1ND-flD6qA9DLB_9VPA-gxVqC6Rq2pvsYbM-X-qMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r-aLxRNzViX0jC54HPzvTNHnaiC6k05f7pTT-VzXLvlTC0UQDCDgUE4XIXjZ7af9I2gmx76iXEOncQC07JaFtKlU_m1Z910_CLz-z8pJEnNX1eoHDw8gjvOijxm6ZyALWMJtWAUjRKQezhj7dNQKKPUdRURKJUXwuAaYG2FeZ-xkCX1-hxAjbgBnyhe_DRhbvygbggPedUU8WKF8KsDZ2U08Yo2vKRzj-OYHJSPVkvXabgA2oiCfiw1m_qA-3ow9PCV2FNtrCNGJh26yQRdhR14LNCGYiTyfkIAdaL-yV587ZFvJjpAqfx424LqcHDcgax8y_3GpCzct9_YEMBVZ5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jzLC6EZT8dhJQEo5af93Zha30PF8RItoTxW1lnfSoCQoRmt8SVdr47L922YYCRCM-4p7nobIMG3ivYzZBqIy0i_kfTlYT0ewMo85zp-5UZpyXgo6lXkYbtDgZAd3aFA_xyeX-x7QWsC9QQB7giNEHWfJ76Jom61AAMsDzqe-CRLw-bi6BgMv-FWAdMNt26DFwoT6wJwvPn0RvaS0q-mu9vxsBYhR6jtaItLBrhJ10ihxDRCIV6PkvAoiEe75fIoSxQTJo1MD9kWc-Ax40JtWAAKCiQOQHd-aFrSMOyIArEKdM7EQE2kd3TgDFpIwYJqzUXkzMCJ9Obw9xJWBVrIrrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iQaL0YSnUfL7jBZZgAJ3Jploc1PSYpF7H2pzZ8RwlT6lWgj7_HfV9r_h34YT5sxXLGUoo1B5KsJynkpT4zVfKDV1kvDQq_8x-h4mQ8Jby8fcH6Q3UkJYU6QAX7Fk6ysDOe7mqQah4WW1eCvsat6MBgOQy3ytAZaxYwcUbnv96UkcxyiQIe5Q3RDqXNZ1ntznwplxasLlecsFZRQAdiMPau7KPzC-8ziybM7nQ3-Gwyl-HL7TuZd08rwhLmmAnrgElICwApm4U1zU8ehV_O5hbMdGYOV8kYPSdO1At9UdGEOXFnmfmB7vxeX7RrnY8B2PMWa6hM26ifhRmFfm6BhkhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iW7csjOY4ywSdEO5-KDGtMWSRbwMFDkAP9__TNWLMX4oreMSjQBFgs5InUUtW5Tj2y0KtmuLLdOcvPkyn7VxDvmXHVpSo9qc8M9zbZLFkJMI3WUCxVoJMawjUzIbeUEXy4baPH9f7-3x6lP2c4IZIbfXoqBadyyShyV6kbz38nDcwXfBTbXlxboK1VEBk99ph8RFe2DuUGkRNIzm7349sb-aNHy98bWXoaZpHHW4X3TvnNshknLdrcx4TimQJGd0uPAS42a1FFoTHPXggbce9uDap6RTVHWKn-82jYDZdTOXheclqe4reUIetPy-IuripbJX_f4y0QOo7zAzMZphtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YT77lV-24GBEsHSXyKvu6iy_vjsm3RZF3TB9wutRX3tuJMgVDpn5IQUiT3TmYlPxW5fbaf_70H2ccJ0C16dlx8xBRY9GIpKmIoN7qNFjJR91LVjq1dMQD132bEXf79WgjfXtqpOcvdYtcCB5tOlhZ-JwJPW5RBwfilgr2QWxxBD0WSE4kW1PelIDzpCQDOKrJrH2srw13txnz-seYkHXG-n8lQVSc50QE4-RlxNBfdh2Q8NhUpMDXq-2cTeylW1h6tqGmEa6JdQQafn-5mXpXfBaV7WG-JJWI5QgfWDZYlrRTfmJc2ekEDDtCDxm_MbILl7FpkeqxES590frTvzVJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bF1HntQB2oqEubK2OhErDOX6LA0ODRFs1HERIAnDM0fXY1mAS3p2ngi6lz_JcDtIcd4F2QtWhCWKYfDBCd4hSb7XD9eLVSDww-cD4d7s2b1LTvgwVVC0g8Hs8QgzUOHgu55EzucJo2_Qgs_USXBSaT7AAqSBPmA7H2R7TcZcUqOQWZpho_Oa8Fu9zA_4wF7z_W_MNTpNUyL2KFgnZuvP7f0s4zTeE2V50L9Bc6caJOy0Ms-JF8bQPMiDA7fvDHjpHSI1n5G14jetFw3RXufag_Rv2D5mxaqOnmgKd0beF2wUYMxrWME5y7PN_39WP4RR1rgX3yHsDGe2CHCqL8ofcA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۱۰
تصویر جذاب از ۱۴ سال کاوش مریخ‌نورد ناسا
در سیاره سرخ
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/693276" target="_blank">📅 23:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693275">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c4c438769.mp4?token=Vxc6nE6wtXidRuiseqrbqQH6U_-9hhrDmkzEhVM2NlVqs_KoZ9UiEtUtuMJnRhgRPjcFehyyynXfvTCP1AQ6WsyZtFhlskWU7K9OkTQz1PuaYUyX15WGlPx1Oqs-UvDIXoIASNMCqmUWbbViPQzhvEUcuj6ODkN2WcLZlgFqNjQA9RkbMCdATqZVa3SShc2X4N3vgqtRR9-waX3KVcBDB0uXQ6u_P1_22o1aarbUvLqUkErH3qjxxRdvd8r7hQz086VP3AZChcDo18c9VBbiFKzZ_a37J10FaMzTSvx3-Qa9XqvYwQykMdrqgTnTtfc8R7EVpN2AvwQp7CYVB_QW9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c4c438769.mp4?token=Vxc6nE6wtXidRuiseqrbqQH6U_-9hhrDmkzEhVM2NlVqs_KoZ9UiEtUtuMJnRhgRPjcFehyyynXfvTCP1AQ6WsyZtFhlskWU7K9OkTQz1PuaYUyX15WGlPx1Oqs-UvDIXoIASNMCqmUWbbViPQzhvEUcuj6ODkN2WcLZlgFqNjQA9RkbMCdATqZVa3SShc2X4N3vgqtRR9-waX3KVcBDB0uXQ6u_P1_22o1aarbUvLqUkErH3qjxxRdvd8r7hQz086VP3AZChcDo18c9VBbiFKzZ_a37J10FaMzTSvx3-Qa9XqvYwQykMdrqgTnTtfc8R7EVpN2AvwQp7CYVB_QW9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کارشناس نظامی: تمام کشتی ها را میزنیم؛ به جز شرکت ادنوک امارات!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/693275" target="_blank">📅 23:13 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693273">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
علی‌رغم ترک صندلی‌های سازمان ملل توسط سران کشورهای جهان به صورت گسترده، نماینده شیخک‌نشین امارات در سالن باقی‌ماند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/693273" target="_blank">📅 23:08 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693272">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf5ad2cef4.mp4?token=oD9u200ZwOMZ8k-aXMPj6_xbzd6zWPYp8HAVKRkBmK7agURAjEbSdMBZIsfrhGJXK5pTZ-jRBg8K--EjJTMtooJXonKoArDXxcf1VwYvBg04d6PNFvKqICs8pbv-LmBbjCFknxxacQq-mfOcCA-h9HRuYtx4ZiTmFJzkjI2NfbNaNFDFSkW0fDU-OMupelyumUsDDgVv2GZuC8KlCq4ha4VqRYaO9sygJh4HGYQw3xrXU_PGHHfgHSn01YRNgL4qxaxktPEG0AW1FFYHb5hTZ3kYFFkegUtXwNeWI12ra-lS6ElB04Kb_Rd8GVwc-losZqnKVF3Gs0Txl1kzIlKrA42Z82B9DYvCT_EI-R8RO0RtPMooHvY4Aqd3t-xHgS9a0xymweKGyngU2hzvq8dxvvAtZ_o_PIc9BGomm2yG-dtvmzqR6xqaoIYG0YWK-ZvHlYLyZT2wmLbLm5UbvzI2PcOVMg7XQdJu8rSuFcpyFq-wMNDll7BCwNeQIKvF_xIk3ANdSLzlBP1qieXppeZECFvVkcO1DakTh2r6ZPVLKtqxwfh0v5r6GYMx2BWZxOAO6t3YvBLJwfgSoRY1xdDyYcA2kufKPEQzKRBpivxJXBbIkWbkd-Hbzua4ZwbyhQbNudVUwd4poLGtaPBi1v4zrniqawgY-xAsOtzbPhKUl3I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf5ad2cef4.mp4?token=oD9u200ZwOMZ8k-aXMPj6_xbzd6zWPYp8HAVKRkBmK7agURAjEbSdMBZIsfrhGJXK5pTZ-jRBg8K--EjJTMtooJXonKoArDXxcf1VwYvBg04d6PNFvKqICs8pbv-LmBbjCFknxxacQq-mfOcCA-h9HRuYtx4ZiTmFJzkjI2NfbNaNFDFSkW0fDU-OMupelyumUsDDgVv2GZuC8KlCq4ha4VqRYaO9sygJh4HGYQw3xrXU_PGHHfgHSn01YRNgL4qxaxktPEG0AW1FFYHb5hTZ3kYFFkegUtXwNeWI12ra-lS6ElB04Kb_Rd8GVwc-losZqnKVF3Gs0Txl1kzIlKrA42Z82B9DYvCT_EI-R8RO0RtPMooHvY4Aqd3t-xHgS9a0xymweKGyngU2hzvq8dxvvAtZ_o_PIc9BGomm2yG-dtvmzqR6xqaoIYG0YWK-ZvHlYLyZT2wmLbLm5UbvzI2PcOVMg7XQdJu8rSuFcpyFq-wMNDll7BCwNeQIKvF_xIk3ANdSLzlBP1qieXppeZECFvVkcO1DakTh2r6ZPVLKtqxwfh0v5r6GYMx2BWZxOAO6t3YvBLJwfgSoRY1xdDyYcA2kufKPEQzKRBpivxJXBbIkWbkd-Hbzua4ZwbyhQbNudVUwd4poLGtaPBi1v4zrniqawgY-xAsOtzbPhKUl3I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چگونه در بازار سرخ‌رنگ بورس هم سود کنیم؟/ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/693272" target="_blank">📅 23:08 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693271">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">گذر از دجال-جلسه ششم</div>
  <div class="tg-doc-extra">علی مقدم</div>
</div>
<a href="https://t.me/akhbarefori/693271" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
دوره‌ گذر از دجال
🔹
جلسه‌ ششم:
تفسیر دعای ندبه
🔹
دلیل تأکید بر خواندن دعاهایی با سند معتبر، این است که معصومین «نحوه حرف زدن با خدا» را به ما می‌آموزند و استفاده از این الگوها باعث اصلاح شیوه‌ی تفکر و باز شدن دروازه‌های استجابت می‌شود.
🔹
امروزه نباید به دنبال نوگرایی‌های شخصی در اندیشه دینی باشیم؛ فهمِ عمیقِ اصلِ دین کافی است.
🔹
حمد خداوند باعث می‌شود ذکر از سطح «زبان» عبور کرده، به «قلب» نفوذ کند و نور باطنی خود را نشان دهد.
🔹
وقتی انسان از درون با خدا وصل شود، دیگر نوسانات بیرونی زندگی او را افسرده نمی‌کند.
🔹
«پذیرشِ آگاهانه و سپاسگزارانه» نسبت به قضای الهی در دنیا، تنها راهِ عبور از فتنه‌های آخرالزمانی و تبدیل شدن به ابزاری در دست اولیای الهی است.
🔹
در آخرالزمان، پیچیدگی فتنه‌ها به قدری است که عقل به تنهایی پاسخگو نیست و باید زیر پرچم اولیای الهی باشیم تا به عنوان «ابزار» در دست آن‌ها قرار گیریم.
🔹
اسباب خدا شدن، حالتی است که فرد ناخواسته منشأ خیر می‌شود و با یک حرف یا نگاه، گره از کار کسی می‌گشاید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/693271" target="_blank">📅 23:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693270">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBimebazar</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dxdB-0oKbmGwETLqxQ_E2KRghEH0amFcc2iLS5H8b-VsyL2NlIBkrL9seo4i0drvrMXWDEJSIzpKuBXO2MnlVHhMIXYZx_iHDM3kb-FbAFp3Otdgj9kokFEhuC1do8uKNrI-mR0ix6u4HZZL5HAfOT8xDpwKSsixyHAFTP4lqYnZQKPh3WiPdaF18mVtcWKhvKzvizni5BZJDP-qYB9etEwSvifI03ZlOB55rRBy_nsqIbl_cn8OqvFo9L4wQN6HcHtLHk6xiZm1KeGGJOQ_XJa0Fkep5E11OFhMfFPOBrCBRbiuKQdB1zJc0Ds6oEpIryzZMOGzs9DhQS3avBO0BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
برای خرید بیمه بدنه، بیمه بازار داره!
ماشین‌مون فقط یه وسیله برای رفت‌و‌آمد نیست؛ یه
سرمایه‌ست
که با کلی زحمت به دست اومده...
برای همین،
بیمه بدنه
برای من یه انتخاب نیست، یه
ضرورته
که خیالم رو بابتش راحت کنم.
اما برای خریدش کجا برم؟
✅
راستش برای خریدش رفتم سراغ
بازارِش
!
چون می‌خواستم جایی باشه که بهم
راهنمایی
کنه و امکان خرید با
اقساط طولانی مدت
داشته باشه
👈
برای مقایسه و خرید بیمه بدنه وارد شو
#بیمه_بازار
🟡
@bimebazarco</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/693270" target="_blank">📅 23:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693269">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cede7dbb3e.mp4?token=EqlopLluHHZzzUE0M9URFv24icFtIY2tQlEiGjnp179ajQM-4T5L7Sl_bL57ICQ_wR5bkz_IVHsaeyU92-yTjmsw-9BiFtEMgNP9wzwjbWkV_OfRK_wo4itKLsjRoc2htHfLnlAEj30vxCg67s_KCqKcMPqgeX8JPQWf4-jsOCYlfryBafFzaJit2Mqlb4RjseC1Fp9JE_beJyCahTbpBrShjqrcIjxYcgFGPKkvSzHngf9ZxChBXsObftokqzBqyW11EDrZmnPsiMETgmpJ675Oz0XGJT74Y5WwFxPDpPQJ9gCywGx3jN4lqxUw9kzwm6S9jsW0PxXgBrlIdWRpcGK9l6XJLB3JfHtwcXwUs1b4n_6Lk5jh1EIEX5bZuEL3oSSr7TqHJ7an7nfkH-YQWjCc0y0jpv-ksRrSsaOmh1r0XytDCYC3YEy0DCX_v6MNBgLfOkIOj3vN9eEisv3d_qM4nLuB1kwfFug5TteTCyEWLfEt4KVPgBvb1gjp_vOYBnrMoL8lgMcfZP50UBLeqw9mVXUvaaf_4cUteOt9RLaFY_QSlyZLeA0x3YA4m_p3aq68NudzGUzgr4jFzlYuShl8-w5kPFmDT50n3Ujk_LfM__xig3_mV5UCJQetxF4O_z-fWbhG_3uOsNREGGTFzhSJfQTHCRlK4a6dOrkPOcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cede7dbb3e.mp4?token=EqlopLluHHZzzUE0M9URFv24icFtIY2tQlEiGjnp179ajQM-4T5L7Sl_bL57ICQ_wR5bkz_IVHsaeyU92-yTjmsw-9BiFtEMgNP9wzwjbWkV_OfRK_wo4itKLsjRoc2htHfLnlAEj30vxCg67s_KCqKcMPqgeX8JPQWf4-jsOCYlfryBafFzaJit2Mqlb4RjseC1Fp9JE_beJyCahTbpBrShjqrcIjxYcgFGPKkvSzHngf9ZxChBXsObftokqzBqyW11EDrZmnPsiMETgmpJ675Oz0XGJT74Y5WwFxPDpPQJ9gCywGx3jN4lqxUw9kzwm6S9jsW0PxXgBrlIdWRpcGK9l6XJLB3JfHtwcXwUs1b4n_6Lk5jh1EIEX5bZuEL3oSSr7TqHJ7an7nfkH-YQWjCc0y0jpv-ksRrSsaOmh1r0XytDCYC3YEy0DCX_v6MNBgLfOkIOj3vN9eEisv3d_qM4nLuB1kwfFug5TteTCyEWLfEt4KVPgBvb1gjp_vOYBnrMoL8lgMcfZP50UBLeqw9mVXUvaaf_4cUteOt9RLaFY_QSlyZLeA0x3YA4m_p3aq68NudzGUzgr4jFzlYuShl8-w5kPFmDT50n3Ujk_LfM__xig3_mV5UCJQetxF4O_z-fWbhG_3uOsNREGGTFzhSJfQTHCRlK4a6dOrkPOcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✂️
ماشین اصلاح GYT-999
✅
صفرزن و خط‌زن | تیغه استیل
🔋
شارژ Type-C |  تا ۴ ساعت استفاده
📊
نمایشگر شارژ + ۴ شانه اصلاح
🔥
فقط ۱,۳۹۸,۰۰۰ تومان
💰
قیمت قبلی:
۱,۶۹۸,۰۰۰
✅
پرداخت درب منزل | ضمانت تعویض ۳ روزه
✅
امکان پرداخت قسطی با ترب پی
خرید از سایت
👇
https://memarket24.ir/product/brief/47608/180124/
✨
تخفیف آخر ماه؛ فرصت آخر!
https://l.memarket.me/lp/65/180124</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/693269" target="_blank">📅 23:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693268">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e1e64dfd8.mp4?token=Ypy7ycSku3juRXZHzk5_PAnBweATX-b7ZmpDS7UWXcVprpuVgzgIfkP9rrBINmNmrzbmlXhwPVILhY4OYzXptW-dTH1qcN3n8UcZvdTX_TKOZoJ4y3hY9dzRNmoHrMhviA8wksHzPcd7WjczEj0crLlaIBghJrc-3WTXKXu3R0fSiM8jckQbCsl-YmcX9Kn0d1OX-i6OvfJjSi-BqwTTOiRYopcvDgxm2Hv_wz5eYewYdrINB3eG7mdIbcXIZq3jh3mAQubIiAcn2YxlCtosBgK_MSrN2c5NrcddCyLiu1H11FQQLll_8T9u1vTj67SxUWYUY45okfrEjyk9skZkGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e1e64dfd8.mp4?token=Ypy7ycSku3juRXZHzk5_PAnBweATX-b7ZmpDS7UWXcVprpuVgzgIfkP9rrBINmNmrzbmlXhwPVILhY4OYzXptW-dTH1qcN3n8UcZvdTX_TKOZoJ4y3hY9dzRNmoHrMhviA8wksHzPcd7WjczEj0crLlaIBghJrc-3WTXKXu3R0fSiM8jckQbCsl-YmcX9Kn0d1OX-i6OvfJjSi-BqwTTOiRYopcvDgxm2Hv_wz5eYewYdrINB3eG7mdIbcXIZq3jh3mAQubIiAcn2YxlCtosBgK_MSrN2c5NrcddCyLiu1H11FQQLll_8T9u1vTj67SxUWYUY45okfrEjyk9skZkGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس‌جمهور: ۲ بار با رهبر انقلاب دیدار کردم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/693268" target="_blank">📅 22:59 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693267">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
پزشکیان: برنامه بعدی آمریکا ایجاد اختلاف بین مسئولان است  رئیس‌جمهور در گفت‌وگو با شبکه الجزیره:
🔹
هیچ وقت وحدت در کشور و بین مسئولان و نیروهای مسلح مانند الان نبوده است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/693267" target="_blank">📅 22:50 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693266">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
پزشکیان: ما و یمن در حمله به خط‌لولۀ عربستان دخالت نداشتیم
🔹
احتمال این‌که اسرائیل این کار را انجام داده باشد تا اختلافات را شعله‌ور کند دور از انتظار نیست.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/693266" target="_blank">📅 22:50 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693265">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab28f65d1b.mp4?token=daZzj9BmOritgfyylXH4uha8TasUKNA5YD9X7OOE1T3gqDj2TwzaoU7WSX_DWjkjTsVeKgUkndGiNbvb1KPCL6qlzdCZ2Bvbctw9JsXJeY32Q5TW8BuaO8U6_Bb7Oev8d_-yGVkhTa2rFHZnsw_lbkc-zshG243GH0u-8mtsWBrSz9eEC-d1kLEE26qaNYnJNOj-FoOktZEl3OfY7deZ13lFz8cq_797by2-lAOIz9MuRMC9Slg6_Y8fPn75P7Aae2eDt3VZTFZH8EyJSBAfI8OftrrWj0Kxr4riP4pLzJblw4AwljNeHS1S7DWT7c-0knHfA0MFssTWrqSACKW05g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab28f65d1b.mp4?token=daZzj9BmOritgfyylXH4uha8TasUKNA5YD9X7OOE1T3gqDj2TwzaoU7WSX_DWjkjTsVeKgUkndGiNbvb1KPCL6qlzdCZ2Bvbctw9JsXJeY32Q5TW8BuaO8U6_Bb7Oev8d_-yGVkhTa2rFHZnsw_lbkc-zshG243GH0u-8mtsWBrSz9eEC-d1kLEE26qaNYnJNOj-FoOktZEl3OfY7deZ13lFz8cq_797by2-lAOIz9MuRMC9Slg6_Y8fPn75P7Aae2eDt3VZTFZH8EyJSBAfI8OftrrWj0Kxr4riP4pLzJblw4AwljNeHS1S7DWT7c-0knHfA0MFssTWrqSACKW05g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا باید از Projects در ChatGPT استفاده کنیم؟
🤖
🔹
به‌جای ساختن چت‌های جدا برای هر موضوع، می‌توان با قابلیت Projects فایل‌ها، چت‌های مرتبط و دستورالعمل‌های هر پروژه را در یک فضای مشترک نگه داشت تا برای کارهای طولانی‌مدت نیازی به توضیح دوباره زمینه کار نباشد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/693265" target="_blank">📅 22:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693264">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
بسیار کاربردی؛ ۱۲ ماه سال به انگلیسی
🔹
۱۱ دی (۳۱ روز): January
🔹
از ۱۲ بهمن (۲۸ روز): February
🔹
از ۱۰ اسفند (۳۱ روز): March
🔹
از ۱۲ فروردین(۳۰ روز): April
🔹
از ۱۱ اردیبهشت (۳۱ روز): May
🔹
از ۱۱ خرداد(۳۰ روز): June
🔹
از ۱۰ تیر (۳۱ روز): July
🔹
از ۱۰ مرداد (۳۱ روز): Augest
🔹
از ۱۰ شهریور (۳۰ روز): September
🔹
از ۹ مهر (۳۱ روز): October
🔹
از ۱۰ آبان (۳۰ روز): November
🔹
از ۱۰ آذر (۳۱ روز): December
#زبان_فوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/693264" target="_blank">📅 22:41 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693263">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/413608cbc5.mp4?token=Bo4mF-Gcrhc5uJDPcnBcFB_W4_AU2ZDoMKcD3qDCMnG2kYpKqfxlr9NfJnqx_RRcrozHpfTZ-VdSGoMdH9eq52m15T-RCFsO1Sg6jLNnHOsJT384jC9BXa6saqhmub9PY-KSR7vYQh98diLDWqIE98qc_nNzxS8RxURyWDDTOoczyxeI88iX1Papom-lPUmSl5hCCaNgsgS-Mz9QRu-3LJwGVJXD2r-FB0yvcl14Wq2h9AXvBxTbTfLT9I-OsxUVP8r9lgkxLJR-WZEr_e7Km37r9aPUw8c6t2R5Co8aAxABwsoNdzjj7ExYlR90kPGTwdPemLC2TtzVqgMlMnijSiamQj4itgTFyZNHdjbAGPbeXe_1ReA-rYlZReXBzA8CVr47g7k7zHyRGladRkTkvhOK4FArT3pP20IrJrQyhuBcMD1dCTpbfIXvk972SG0yF3qthCjrUiSF-8KCUG_xpNBO4aMPlk3MxOh931nuQnhlv1DgjwuDABwOgdZKe3jrLCm_xg2RfyamjzwpORE2hHxyIbLouQ5vYbr4BhBrPWUuEdMCV2rfL8m_HPIQ-iJ40AOW6zd7fuEavZzQ4l4iboMiXTVvz9YVlgzmd-0iURpiyzwvhhj6DqiP9uxyU8DajDhIl_srmy0V9mcy_vetSmrhNq6kzYdzdXsYcLkjKHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/413608cbc5.mp4?token=Bo4mF-Gcrhc5uJDPcnBcFB_W4_AU2ZDoMKcD3qDCMnG2kYpKqfxlr9NfJnqx_RRcrozHpfTZ-VdSGoMdH9eq52m15T-RCFsO1Sg6jLNnHOsJT384jC9BXa6saqhmub9PY-KSR7vYQh98diLDWqIE98qc_nNzxS8RxURyWDDTOoczyxeI88iX1Papom-lPUmSl5hCCaNgsgS-Mz9QRu-3LJwGVJXD2r-FB0yvcl14Wq2h9AXvBxTbTfLT9I-OsxUVP8r9lgkxLJR-WZEr_e7Km37r9aPUw8c6t2R5Co8aAxABwsoNdzjj7ExYlR90kPGTwdPemLC2TtzVqgMlMnijSiamQj4itgTFyZNHdjbAGPbeXe_1ReA-rYlZReXBzA8CVr47g7k7zHyRGladRkTkvhOK4FArT3pP20IrJrQyhuBcMD1dCTpbfIXvk972SG0yF3qthCjrUiSF-8KCUG_xpNBO4aMPlk3MxOh931nuQnhlv1DgjwuDABwOgdZKe3jrLCm_xg2RfyamjzwpORE2hHxyIbLouQ5vYbr4BhBrPWUuEdMCV2rfL8m_HPIQ-iJ40AOW6zd7fuEavZzQ4l4iboMiXTVvz9YVlgzmd-0iURpiyzwvhhj6DqiP9uxyU8DajDhIl_srmy0V9mcy_vetSmrhNq6kzYdzdXsYcLkjKHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا طلاق؟
🔹
سراغ شما آمدیم تا از شما بپرسیم، مهم‌ترین عاملی که باعث طلاق می‌شود، چه می‌تواند باشد. هر کدام نظر خاص خود را داشتید؛ اما واقعا مهم‌ترین عامل طلاق چیست؟
🔹
جزئیات را در این ویدئو ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/693263" target="_blank">📅 22:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693262">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcc810592c.mp4?token=omTbhJtL555KFEc1tfnbk7zhwt2pyaa6TCVtCdWsVCmbI6mZ2fhhoop2fHR4ovUvjC2HNuNJsB7rPWDM-tL21DMFuI0r1FRvYu2oBPO_Mn8-itKy0-o2IOiPlRwm1GXfXPRaLrNzrJwrFgSCVFK1WeJdmU1cl2u54DcLob0ZNtnJvNpcWCg9CF_TPMfau-OXtSehc4dTh-y9tJ6OOTeljNBoNxfCd5eBodXxWISt1OcaiC2bUFNvakvPtOCY865GMkZ-JARGfn43KTQ6ES-23pHXCjfUhLi-GDttiE5yDnVbQ8lNoxlSOKPFVUqhrYznwnJR-3wnJuBU1CUQtPLs_DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcc810592c.mp4?token=omTbhJtL555KFEc1tfnbk7zhwt2pyaa6TCVtCdWsVCmbI6mZ2fhhoop2fHR4ovUvjC2HNuNJsB7rPWDM-tL21DMFuI0r1FRvYu2oBPO_Mn8-itKy0-o2IOiPlRwm1GXfXPRaLrNzrJwrFgSCVFK1WeJdmU1cl2u54DcLob0ZNtnJvNpcWCg9CF_TPMfau-OXtSehc4dTh-y9tJ6OOTeljNBoNxfCd5eBodXxWISt1OcaiC2bUFNvakvPtOCY865GMkZ-JARGfn43KTQ6ES-23pHXCjfUhLi-GDttiE5yDnVbQ8lNoxlSOKPFVUqhrYznwnJR-3wnJuBU1CUQtPLs_DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قیمت بنزین و گازوییل در استرالیا رکورد زده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/693262" target="_blank">📅 22:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693261">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
ترامپ: امیدوارم روسیه و اوکراین قبل زمستان به توافق برسند
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/693261" target="_blank">📅 22:33 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693260">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a39ccd2db8.mp4?token=BpV4FuRezcF_jF5eQIxTLMmX_x7dZG8i_YGhz5u7x75Juiyu_qHsvb-rCteS5eQd8aYymUinzZrPCOfNJdmIrk8O7VmnmL-RQHFBZjaSMjXqWOZIcIpwKhJcR8AHAoLLvOq54brMVd8bZn47cONtNi1I7tH-a1LK-hvklehhwz0Fx_oQbq-w79qHpDSlnkCUVdECI2SDd0NjZyeJUo093279zwfKo1lsbTKqN0FfJYRyhLD6x4FFNZxPcxyz4RHvdjqQDlFA3qfTLcnpMRorSKuyHGFwaYqtX54jGIsf6sWUptaQ45877PnycCoxQqXbyg5QkwG-laijYLpXrade3Yj49Q2PaLGwiM0cPzOosfv8nlWuwPop-MKSSjgCUth-4N9O0XIf_RJjDnJiOlADNRfnrjen9eYGvuWQlQlWxkbCJ9UH4voeeMO0pJsToAEIdPmmFqLTBHltq1DiwIa_Py9cHQJmkc42Kk-CQxfqh4o13nHtiZ4FoCC34rqPjBfXj4RQp9LmaJzzHvibW6q3yvTVQqPzasdLoU5_IrD38DbzazqZRUjQb6cCXo3BIp-rAjw8nCScRhHa1oBgV2Q1ZVmaRimWKQYGScND5fFdXAQHmKLTPDlB7qSTKIB-YlbFitSHnBfP6CUKUyYydV9StX0C2eBmtMmo4XpmxiaL93c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a39ccd2db8.mp4?token=BpV4FuRezcF_jF5eQIxTLMmX_x7dZG8i_YGhz5u7x75Juiyu_qHsvb-rCteS5eQd8aYymUinzZrPCOfNJdmIrk8O7VmnmL-RQHFBZjaSMjXqWOZIcIpwKhJcR8AHAoLLvOq54brMVd8bZn47cONtNi1I7tH-a1LK-hvklehhwz0Fx_oQbq-w79qHpDSlnkCUVdECI2SDd0NjZyeJUo093279zwfKo1lsbTKqN0FfJYRyhLD6x4FFNZxPcxyz4RHvdjqQDlFA3qfTLcnpMRorSKuyHGFwaYqtX54jGIsf6sWUptaQ45877PnycCoxQqXbyg5QkwG-laijYLpXrade3Yj49Q2PaLGwiM0cPzOosfv8nlWuwPop-MKSSjgCUth-4N9O0XIf_RJjDnJiOlADNRfnrjen9eYGvuWQlQlWxkbCJ9UH4voeeMO0pJsToAEIdPmmFqLTBHltq1DiwIa_Py9cHQJmkc42Kk-CQxfqh4o13nHtiZ4FoCC34rqPjBfXj4RQp9LmaJzzHvibW6q3yvTVQqPzasdLoU5_IrD38DbzazqZRUjQb6cCXo3BIp-rAjw8nCScRhHa1oBgV2Q1ZVmaRimWKQYGScND5fFdXAQHmKLTPDlB7qSTKIB-YlbFitSHnBfP6CUKUyYydV9StX0C2eBmtMmo4XpmxiaL93c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این فیلم آمریکایی، ۱۸ سال پیش مقابل دوربین رفت و روی پرده اکران شد
🔹
در این فیلم به وضوح از اهمیت تنگه هرمز و لزوم کنترل آن توسط آمریکا (از دید دولتمردان آمریکا) صحبت می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/693260" target="_blank">📅 22:33 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693258">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da4e0877ee.mp4?token=ABIdRJf0PeSeLvTrm7pOKx0FuLy6D9XEyicBfhvzhqpbJTYfIC85eufPIMHzGyAU2HvB6wjDDLK0XWqsKYv5MxKILCxSsLBFCJYKHZx04wTtjXnIg8JriyVuOL89lMKwL6f5mzbfygr4VGnPhOEJgm-bzuzMPb2NIlibcPA7VYSB9Oej8-EFK4Q9jsGTPhwF_jhPlqm_lFroVvRB7DjHrb1Su3ugrD5PHAhm4M73JOr_WvzlB6t7P5y3G_tlXRDrcG9xrix8MYi48HQsQA7fAFb9RaeF7z5qvA-JCcZvIJcoXILTtm49tD4S45dHlGMdUDSUkTCBg0r4edbZMJbNSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da4e0877ee.mp4?token=ABIdRJf0PeSeLvTrm7pOKx0FuLy6D9XEyicBfhvzhqpbJTYfIC85eufPIMHzGyAU2HvB6wjDDLK0XWqsKYv5MxKILCxSsLBFCJYKHZx04wTtjXnIg8JriyVuOL89lMKwL6f5mzbfygr4VGnPhOEJgm-bzuzMPb2NIlibcPA7VYSB9Oej8-EFK4Q9jsGTPhwF_jhPlqm_lFroVvRB7DjHrb1Su3ugrD5PHAhm4M73JOr_WvzlB6t7P5y3G_tlXRDrcG9xrix8MYi48HQsQA7fAFb9RaeF7z5qvA-JCcZvIJcoXILTtm49tD4S45dHlGMdUDSUkTCBg0r4edbZMJbNSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نشریۀ اکونومیست: آمریکا از خاورمیانه خارج می‌شود و ایران ابرقدرت مطلق منطقه خواهد شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/693258" target="_blank">📅 22:30 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693257">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدپارتمان آموزش های مجازی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u9ZiBwHyHgidBy_HA6n3tBb4aP7HrF26Udqpp395R0bFojYW53YnwwJaJw16QMG8-RBz30Ph4I6JznTfNpt5Tqv6bImZe0DAwAz_N7ZU_KySIdXo1i6SCZkuLIbHUUr-DCDAoIiTpznBdYDMtr4o6Txciv4aQnAno0PLQPP-JASdma8W6HADnAelUEP8I0kxl0WroTbM4YBMdgucvSQDiBvcY9Ow5JKYASJg3rU6Lpt2qocSjWgotbf_YTE3z8x3JE-mzgHr6HvV7ceoAMnpy-p-H8aqgjfqEcJshRKp80EeIyr-ThZQtgSM0BgoNXASVk9X76A04yB22OgTW00Z8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
فرصت جدید ثبت‌نام ICDL آنلاین!
💻
یادگیری کاربردی
🎥
دسترسی به ویدئوهای کلاس
👨‍🏫
رفع اشکال با استاد
📜
مدرک معتبر مجتمع فنی تهران (قابل ترجمه رسمی و ارسال پستی)
📅
شروع قطعی:
۵ مهر ۱۴۰۵
⏰
روزهای فرد| ۱۷ تا ۲۱
🚨
ظرفیت محدود!
📞
02634127 داخلی ۱۲۰
📱
09032648676
🔗
ثبت‌نام آنلاین:
https://B2n.ir/kj1017
مشاوره و ارتباط تلگرامی:
@siam_lms
کانال دوره های مجازی:
https://t.me/siamlms</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/693257" target="_blank">📅 22:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693256">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72c55df22d.mp4?token=SmX7M_vpvcwJ40qK7tWL-hhXpU1svgjySTzJzTq0Yn7jOSwVq2RaWIJEgWu5QbDv4HSb4t-C2H3vd955OhDBL5KEPn0IYczCdqVL8vJpLqW83gDSV0gwmsLCxiWBF9kPsbUUrDNHpCG58Hwqoe4dCVQA7blnHSKxcfkZ5hmi1TkuYI4XhUcwckdP1Id0SRDS5FA4GBsQ8gE3VR6VOdbCZhKYjtDIHop1_xCkODE9r42HQfLFOWEDTS3m-AyKc_iG7pw7kCLYAd5rwYmq6n-sWJDk5pJob5r3ewogGzprv2_G6LncMH_1fxgtyIrzgLi-e77GMF3aLxoVHiHZ23CScQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72c55df22d.mp4?token=SmX7M_vpvcwJ40qK7tWL-hhXpU1svgjySTzJzTq0Yn7jOSwVq2RaWIJEgWu5QbDv4HSb4t-C2H3vd955OhDBL5KEPn0IYczCdqVL8vJpLqW83gDSV0gwmsLCxiWBF9kPsbUUrDNHpCG58Hwqoe4dCVQA7blnHSKxcfkZ5hmi1TkuYI4XhUcwckdP1Id0SRDS5FA4GBsQ8gE3VR6VOdbCZhKYjtDIHop1_xCkODE9r42HQfLFOWEDTS3m-AyKc_iG7pw7kCLYAd5rwYmq6n-sWJDk5pJob5r3ewogGzprv2_G6LncMH_1fxgtyIrzgLi-e77GMF3aLxoVHiHZ23CScQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای یک رسانه ترک: عربستان خط لوله نفت شرق به غرب خود را دوباره عملیاتی کرد/ احتمال ازسرگیری صادرات از بندر ینبع نیز وجود دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/693256" target="_blank">📅 22:21 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693255">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
پزشکیان: دیدار با ترامپ چه مشکلی را حل می‌کند؟  رئیس‌جمهور در گفت‌وگو با شبکه الجزیره:
🔹
وقتی آمریکا به آنچه نوشتیم عمل نمی‌کند، دیدار با ترامپ چه مشکلی را حل می‌کند؟
🔹
نمی‌دانیم بر اساس کدام قانون با آمریکا حرف بزنیم که به آن عمل کنند.
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/693255" target="_blank">📅 22:14 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693254">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
پزشکیان: نتانیاهو نتوانسته غزه را وادار به تسلیم کند، حالا می‌خواهد حکومت ایران را تغییر دهد؟
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/693254" target="_blank">📅 22:10 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693253">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac8de0a4b3.mp4?token=km-1dPs-LXUIH2Gmo47IbcK2uCCT5efNc82UbpKF7g5WVIu4IObZcf9_eh-x_nCAWKhOHhAIAJYZcBbT1a0ugN9AOzPtu5BPuhgcg8WO2Z9hIdSnEJYzQ8mu3J8LNlcejzHPwxu9Gb3MJ0VtbYg2hnLQjso-xD-f0q-Igd2Hx1f2I35297IQC89JAQzeFs8ruNLCkCxGPA4iB--Bsg0Og5cl-o2LmPs3HAFfcE44ma3zdJywzUzvi9sI01Z7R_JgEYujA0dxwPCncaYGiFiq-Q8HdHY6V-hMAkTlcF0a0Cur5d0dz2LlQmPev3iEA2m9ZxjJrmUl7LcGEA5B7RnBbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac8de0a4b3.mp4?token=km-1dPs-LXUIH2Gmo47IbcK2uCCT5efNc82UbpKF7g5WVIu4IObZcf9_eh-x_nCAWKhOHhAIAJYZcBbT1a0ugN9AOzPtu5BPuhgcg8WO2Z9hIdSnEJYzQ8mu3J8LNlcejzHPwxu9Gb3MJ0VtbYg2hnLQjso-xD-f0q-Igd2Hx1f2I35297IQC89JAQzeFs8ruNLCkCxGPA4iB--Bsg0Og5cl-o2LmPs3HAFfcE44ma3zdJywzUzvi9sI01Z7R_JgEYujA0dxwPCncaYGiFiq-Q8HdHY6V-hMAkTlcF0a0Cur5d0dz2LlQmPev3iEA2m9ZxjJrmUl7LcGEA5B7RnBbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: نتانیاهو نتوانسته غزه را وادار به تسلیم کند، حالا می‌خواهد حکومت ایران را تغییر دهد؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/693253" target="_blank">📅 22:09 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693252">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
پزشکیان: تروریست آمریکا و اسرائیل است و ما قربانی تروریست هستیم.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/693252" target="_blank">📅 22:06 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693251">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
رئیس‌جمهور در گفت‌وگو با شبکه الجزیره: ما اعتمادی به مذاکره با آمریکا نداریم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/693251" target="_blank">📅 22:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693250">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac92dad0c2.mp4?token=iw_4k8GeZMn696q3HkMWANnif78xcdhGkK8xztnM8HuFFOD_8Aqrj-dvK0D-5Zq-Sa8KtkxVIaRh6CTAOO05NQDw3Ivz0tEdKe1_EnRuOjsTOQrB4hKDwBKtAdT9ob2Tebbs4wWib2ISgKdVjDt65OW6lHhdLqEKeIVzBVdpGjKpyVMHFis29ToY93KcfLOFgZu6u_5aMaIKyQNrxYrAa_NKVP-f1JBybuUgv7hN41cOPc1iVtxfIMNgPyzyUgX8Ri5DICkgsl8Vwed69UtVaNsM8V5WxAdTOGsj2CXAPMQdRI4b74ZGLL8mHmkBVceGu0owGjW149SM1iwgQVJJWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac92dad0c2.mp4?token=iw_4k8GeZMn696q3HkMWANnif78xcdhGkK8xztnM8HuFFOD_8Aqrj-dvK0D-5Zq-Sa8KtkxVIaRh6CTAOO05NQDw3Ivz0tEdKe1_EnRuOjsTOQrB4hKDwBKtAdT9ob2Tebbs4wWib2ISgKdVjDt65OW6lHhdLqEKeIVzBVdpGjKpyVMHFis29ToY93KcfLOFgZu6u_5aMaIKyQNrxYrAa_NKVP-f1JBybuUgv7hN41cOPc1iVtxfIMNgPyzyUgX8Ri5DICkgsl8Vwed69UtVaNsM8V5WxAdTOGsj2CXAPMQdRI4b74ZGLL8mHmkBVceGu0owGjW149SM1iwgQVJJWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس‌جمهور در گفت‌وگو با شبکه الجزیره: ما اعتمادی به مذاکره با آمریکا نداریم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/693250" target="_blank">📅 22:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693249">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
پزشکیان وارد تهران شد
🔹
رئیس‌جمهور پس از پایان سفر به نیویورک و شرکت و سخنرانی در هشتاد و یکمین مجمع عمومی سازمان ملل متحد، وارد تهران شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/693249" target="_blank">📅 21:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693248">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/581bd5215c.mp4?token=CuA31kqaBseKXlLhiptMFVw8pqQNyIqVGG8FKInS0avgLg15AjdaSH5gQuzbxTVWucSg1JfI1h9gSDfvsO9-s91G9P-FHB3I9eFHJLnnF0LHj_bM1LJlH54yEjMGv4pu2hp14Owum0-CVOyiiaTLGRa6OHgORiWQYEfD7nytyVrBCTbUR7ESIJkOOmRnWzu81s3FmRIFRLYyKgUAN9pj7BYbVtWaoF_0ZmYlvPH00VXHCKHjEQt2M1Lx9H-49jREfJQasaguJ-7pfDJ2uDhWyF4J_YVv9eM3jjkxkURggcNrEfvLgWQ8A1KRM-02Llv_HvSJZImqjoD6Bdms46gKCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/581bd5215c.mp4?token=CuA31kqaBseKXlLhiptMFVw8pqQNyIqVGG8FKInS0avgLg15AjdaSH5gQuzbxTVWucSg1JfI1h9gSDfvsO9-s91G9P-FHB3I9eFHJLnnF0LHj_bM1LJlH54yEjMGv4pu2hp14Owum0-CVOyiiaTLGRa6OHgORiWQYEfD7nytyVrBCTbUR7ESIJkOOmRnWzu81s3FmRIFRLYyKgUAN9pj7BYbVtWaoF_0ZmYlvPH00VXHCKHjEQt2M1Lx9H-49jREfJQasaguJ-7pfDJ2uDhWyF4J_YVv9eM3jjkxkURggcNrEfvLgWQ8A1KRM-02Llv_HvSJZImqjoD6Bdms46gKCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تورها وارد فضای عجیب و غریبی شدن!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/693248" target="_blank">📅 21:57 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693247">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
نگهداری طلای پلتفرم‌های طلا در بانک به معنای خالی‌فروشی نیست
🔹
رئیس اتحادیه کسب‌وکارهای مجازی با اشاره به حواشی اخیر بازار طلای آنلاین گفت: صرف اینکه طلای یک سکو در کارگاه یا بانک نگهداری می‌شود، به‌معنای خالی‌فروشی نیست.
🔹
الفت‌نسب تأکید کرد که در بازاری که معاملات آن لحظه‌ای انجام می‌شود، نظارت هم باید لحظه‌ای باشد؛ یعنی موجودی طلا، تعهدات و معاملات سکوها به‌صورت هم‌زمان قابل تطبیق باشد.
🔹
او راه‌اندازی کامل سامانه نظارتی طلای آنلاین را یکی از مطالبات جدی این حوزه دانست؛ سامانه‌ای که به گفته او می‌تواند ابهامات را پیش از تبدیل‌شدن به نگرانی عمومی شناسایی کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/693247" target="_blank">📅 21:54 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693246">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
فوت موجر یا مستأجر قرارداد اجاره را باطل می‌کند؟
وکیل دادگستری:
🔹
در حالت کلی با فوت موجر و مستأجر قرارداد منحل نمی‌شود و به وراث منتقل می‌شود، مگر اینکه در قرارداد، مباشرت مستأجر جهت استفاده از مورد اجاره شرط شده باشد یا مدت اجاره تا زمان عمر موجر یا مستأجر تعیین گردیده و یا موجر فقط تا زمان حیات خود، مالک منافع ملک استیجاری بوده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/693246" target="_blank">📅 21:52 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693245">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S7NJIjc0yzRP16J7KkuOfsaST7XHvb8FE5qWZF6zj1Ktf4rmfdacBF5n1SebioSAH4v5uQcf5bZ6BAcEjlKnkPxq3Xi0IMXw_ZUxgNTySn_gr0LMFP7TFMYrFZv5iefs0jkyND1aX_48MuwlHW0wWWBuxi7vqNfgOcEvekvjcRhzetXBqsqbr9Ko5P98esclQbdArymMYmZFC1CAEElwON-4swLQDC_Nx9xw1YHpkda3ppWVhMHFAHZK_U_c3WhWYFP2Wy8h4vv8Z5JRhwnWkK7z7Go_aqkYVGZiro2W38tU2ej12umF43wQAUBDgcGhqJtxNj39gM7mniVbCwVIFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شناسایی پیکر شهید پس از ۴۰ سال
🔹
پیکر شهید «علی‌اکبر گندمی» از رزمندگان ارتش که سال ۱۳۶۵ در عملیات کربلای ۶ در منطقه سومار به شهادت رسیده بود، پس از ۴۰ سال در جریان تفحص شهدا کشف و شناسایی شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/693245" target="_blank">📅 21:50 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693244">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bO4bIdkp4vLLGMGcLUBuFYWc5VwiFd6akxUXznDI3pyWr5GEeD8BwEfyZKnR-WLDDR5XbvKHqTY-uYlB36MDWIVpuS50jDOJNLvBKqRPrmbVx5dHE66j0gLu7bqry5YYz_4BaMyVFFBWiE9mqkMqDvISbyrO8V3iajr-l5EkufmnftlKRnT8gmnd9amh4DzYjXRZmlsOsxV749mqjSNNyiAwX18-TDrUFp4wIOIDCQXOqIh3X-GmEdeI3GsHTkmdyUZ2MK6qBsxWD6Mos_ugz9r1wCdsM4Sohij4SH5ZEuS1GuZlQHvFFCbH6cNDo6DIzFm7a6JFiT93nkzcCyPWgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زیر خاکستر
🔹
مذاکرات غیرمستقیم ایران و آمریکا با فعال‌شدن دوباره میانجی‌ها وارد مرحله تازه‌ای شده است. ایران پیشنهاد هفت‌روزه‌ای برای بازگشایی تنگه هرمز و ازسرگیری مذاکرات ارائه کرده و پزشکیان و عراقچی تأکید کرده‌اند که اجرای این طرح به پذیرش شروط ایران از سوی آمریکا بستگی دارد. هم‌زمان، گزارش‌هایی از ادامه رایزنی‌های مثبت میان دو طرف و نیز مخالفت ترامپ با پیشنهاد ایران منتشر شده است. رئیس‌جمهور آمریکا اعلام کرد که پیشنهاد ارائه شده توسط ایران را که به موجب آن، تنگه هرمز ظرف مدت هفت روز باز می‌شد، رد کرده است. با این حال، بی‌اعتمادی عمیق و اختلاف بر سر شروط توافق همچنان پابرجاست و اگرچه تحرکات دیپلماتیک به کاهش موقت سطح تنش منجر شده اما تداوم فشارها و تهدیدهای نظامی، احتمال بازگشت درگیری‌ها را همچنان منتفی نکرده است.
🔹
هشتصدوهفتادمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/693244" target="_blank">📅 21:44 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693243">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59247c96c0.mp4?token=ETHo85toPUys0yBgWT85JRYd0XfektwWe0FGSuU_6lLyn-VyS8WSDdCSVOmEGsXdD6e8xBhjXqqE3tQL5slRDxKCTskOQyFD1BR1NhCYvLbmT9IYuu-hr8eCyqsDiEofr40uKhWRs4k_jI7LaGuKHGlhz-PFnnprR14kFnuXS070hTgZqHJwSuf8-0HPcPZeQ4iTX5R7bg7iVZdRnYHZhIA7NXWYMyI9JsKUk6nHb7NHDNajfAd7W8iVc3GjW3Xl5uqngTTutKFU-UXiGW4SirhMWEG7ovU8IXrYyJvZ1RFevVKQpGe64MS7djSpxHBgfV3Wb9kZCEOUAR8hLc8wZ2qvXUy0jWE4cOKWQrS40orO-DDqJUkrSxcTH4wWPFYsKuVbi2bcX1vbZGkj78jrDdpj9ISFV0GXNruQf8sMv4auRKZ1Qu4BOszVdnztliBjAx0TlSW5wdWzYBp6NA-XFYgY0RrtsPbQfoLnQEU3OlPbxH-Eu3ahyYmtvz-WKosLUmKkaYX_vfP4o2ZMJg-o8soimSlF8CBJl_KvdgNHU7pYikDSsQI_0G4u2QH3re6AqT7op5vXzkbkv96oNAJZtJJc7V9BLYtln_fXnLGLBYumqiQOMqSS4XGvH-7kdfBlJG5cDBCGAcBoTkjEdIVRQIwyBSVhSqdWcCSqYMlqeQo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59247c96c0.mp4?token=ETHo85toPUys0yBgWT85JRYd0XfektwWe0FGSuU_6lLyn-VyS8WSDdCSVOmEGsXdD6e8xBhjXqqE3tQL5slRDxKCTskOQyFD1BR1NhCYvLbmT9IYuu-hr8eCyqsDiEofr40uKhWRs4k_jI7LaGuKHGlhz-PFnnprR14kFnuXS070hTgZqHJwSuf8-0HPcPZeQ4iTX5R7bg7iVZdRnYHZhIA7NXWYMyI9JsKUk6nHb7NHDNajfAd7W8iVc3GjW3Xl5uqngTTutKFU-UXiGW4SirhMWEG7ovU8IXrYyJvZ1RFevVKQpGe64MS7djSpxHBgfV3Wb9kZCEOUAR8hLc8wZ2qvXUy0jWE4cOKWQrS40orO-DDqJUkrSxcTH4wWPFYsKuVbi2bcX1vbZGkj78jrDdpj9ISFV0GXNruQf8sMv4auRKZ1Qu4BOszVdnztliBjAx0TlSW5wdWzYBp6NA-XFYgY0RrtsPbQfoLnQEU3OlPbxH-Eu3ahyYmtvz-WKosLUmKkaYX_vfP4o2ZMJg-o8soimSlF8CBJl_KvdgNHU7pYikDSsQI_0G4u2QH3re6AqT7op5vXzkbkv96oNAJZtJJc7V9BLYtln_fXnLGLBYumqiQOMqSS4XGvH-7kdfBlJG5cDBCGAcBoTkjEdIVRQIwyBSVhSqdWcCSqYMlqeQo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نگاهی نزدیک به طراحی متفاوت خودروی برقی عربستانی CEER EXOBOT
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/693243" target="_blank">📅 21:42 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693242">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26e764cc31.mp4?token=DL3FEbZ1mxaPQ-et3gwgZVcsXP8cn6MIHFzrUXjTiTnuzmKDAAcxccVqRa2w51jv3YuNiqIYjvv6PTCmxXF6lL480fnpyUrNUDiWqxu9c8KAX_2AYsIlJxQJ6YeA0i4L7BKValv0iHa9jXlPEZvVUGHXCKzF4Stgj8v0bNf3s1Uz-W_FA7D18nWthEgxqQndt9KzkOqKzNW3RCtElCWbowaz18V7gBm2D4naNqx_uU_zJfd3tLS7IkLXNhz_TGBnCcDyn0iPHyfvXeNrDzCIMhGlYldZtq0KqEOSAK4puIbVcKSybfOdvlvlhH0xBRYeiVcm6yVPaAprrh44X4a9vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26e764cc31.mp4?token=DL3FEbZ1mxaPQ-et3gwgZVcsXP8cn6MIHFzrUXjTiTnuzmKDAAcxccVqRa2w51jv3YuNiqIYjvv6PTCmxXF6lL480fnpyUrNUDiWqxu9c8KAX_2AYsIlJxQJ6YeA0i4L7BKValv0iHa9jXlPEZvVUGHXCKzF4Stgj8v0bNf3s1Uz-W_FA7D18nWthEgxqQndt9KzkOqKzNW3RCtElCWbowaz18V7gBm2D4naNqx_uU_zJfd3tLS7IkLXNhz_TGBnCcDyn0iPHyfvXeNrDzCIMhGlYldZtq0KqEOSAK4puIbVcKSybfOdvlvlhH0xBRYeiVcm6yVPaAprrh44X4a9vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ماجرای خالی‌فروشی آنلاین طلا چیه؟
🔹
بعضی پلتفرم‌ها بدون اینکه به اندازه طلایی که به مشتری می‌فروشن، طلای فیزیکی داشته باشن، معامله انجام می‌دن؛ به این می‌گن «خالی‌فروشی».
🔹
طبق دستورالعمل جدید، پلتفرم‌ها باید طلا رو قبل از فروش به خزانه تحویل بدن و موجودی‌شون در «سامانه ناظر» ثبت بشه.
🔹
با توجه به تشکیل ۵۰۸ پرونده کلاهبرداری در سه سال گذشته، بهتره قبل از خرید، مجوز، کارمزد، محل نگهداری طلا و شرایط تحویل فیزیکی پلتفرم رو بررسی کنیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/693242" target="_blank">📅 21:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693241">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
ترامپ: پیشنهاد ایران را رد می‌کنم
🔹
ترامپ: من هر توافقی را که بر اساس آن ایران بخواهد فوراً تجارت را از سر بگیرد، رد می‌کنم. #Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/693241" target="_blank">📅 21:39 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693240">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2755b599d8.mp4?token=tmKn3s17WqWHd9U8HyEcFL7fbaUUJ9hZYdLElyuMCfq6a_5wSQuTdSluahnrQuLS_BWTPUohQcYH8Enj1d90QvqlJN2TWTxjbG2wkACOwFsVQngY6_51HaMHhHfVMNNSv1FStk7vkJVJI9x_RqI5tDSDgxB-BY26HPxqvzCg3ODXx6VbcblIz65pZlhrdae926CJZMx7ofbd_DjR64ZN8JMNR7MfkAdoPwyCm1AOSN-c9qW-CPZP6c_wFOxvru_WAGbiw8cqvffCKyyv818sOqpPj9_cwMfGE7AxvN_SO86Wj5DPc2gyM4pMW39GaQbVHUlV-5afMjavqf6kmaD_TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2755b599d8.mp4?token=tmKn3s17WqWHd9U8HyEcFL7fbaUUJ9hZYdLElyuMCfq6a_5wSQuTdSluahnrQuLS_BWTPUohQcYH8Enj1d90QvqlJN2TWTxjbG2wkACOwFsVQngY6_51HaMHhHfVMNNSv1FStk7vkJVJI9x_RqI5tDSDgxB-BY26HPxqvzCg3ODXx6VbcblIz65pZlhrdae926CJZMx7ofbd_DjR64ZN8JMNR7MfkAdoPwyCm1AOSN-c9qW-CPZP6c_wFOxvru_WAGbiw8cqvffCKyyv818sOqpPj9_cwMfGE7AxvN_SO86Wj5DPc2gyM4pMW39GaQbVHUlV-5afMjavqf6kmaD_TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حرکت جنجالی ترامپ پس از دست دادن با زلنسکی
🔹
حرکت دست ترامپ پس از دست دادن با زلنسکی در فضای مجازی با عنوان «دست شاخدار» پربازدید شده است؛ برخی کاربران خرافاتی این حرکت را نمادی برای دور کردن بدیمنی می‌دانند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/693240" target="_blank">📅 21:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693238">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
لینک یاب فایل های صوتی گنجینه معنوی کانال
:
🔹
زندگی پس از زندگی
فصل یک | فصل دو
| فصل سوم
|
فصل چهارم
|
فصل پنجم
|
فصل ششم
🔹
چله علم و نور  "یک"
،
چله"دوم"
،
چله"سوم"
🔹
آن ۳۱۳ نفر
🔹
تفسیر سوره‌های صف
|
مسد
🔹
سنت‌های الهی خداوند
🔹
شرح به وقت شام ۱
و
شرح به وقت ایران ۲
🔹
پادکست کسب‌وکار رادیو کار نکن
🔹
ادعیه روزهای هفته
🔹
برنامه کتاب‌باز
🔹
شرح و تفسیر کتب:
"سه دقیقه در قیامت"
،
"آن سوی مرگ"
،
شنود
🔹
چگونه با عبادت تفریح کنیم؟
🔹
حال خوش معنوی در زندگی
🔹
چله جوشن کبیر اول
و
چله دوم
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/693238" target="_blank">📅 21:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693236">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
رئیس‌جمهور در مصاحبه با شبکه CBS آمریکا: ما زندانیان آمریکایی را آزاد کردیم اما آمریکا زیر قولش زد و پول‌های ما را آزاد نکرد/ ما نمی‌خواهیم بجنگیم اما اگر بزنند، دفاع می‌کنیم
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/693236" target="_blank">📅 21:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693235">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d2ab6808bd.mp4?token=vOH6HwX9y8SM3GvMOBZEd2qvty2YxVPmSctP72V41N9ZZjFfT3M4QP11BldyjgFxjbLMONP3AdhTYw146nf6LTA6e446IKpG7b1eeYFlZd5kjRPHZ51pfKP9kMOHMH7ED9NLpnZxqaii77gFZEe9oym226voWBt37d87ZZ4DGg79uNX_kXYyEiIsY6138h-5bM73uW-Zl55x4Oeey9MDmRV_Bdzltp9nPhNa6oH__pgX4VFuUv0-7hb2Erl22PySZg6k-be3JvzLYepJ7AIFV0nyIun39AyK-T5Iu7z94vs4VdcT_uRIBxAYRiyAW48xCfBCsIqzkqzFide8x0yefjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d2ab6808bd.mp4?token=vOH6HwX9y8SM3GvMOBZEd2qvty2YxVPmSctP72V41N9ZZjFfT3M4QP11BldyjgFxjbLMONP3AdhTYw146nf6LTA6e446IKpG7b1eeYFlZd5kjRPHZ51pfKP9kMOHMH7ED9NLpnZxqaii77gFZEe9oym226voWBt37d87ZZ4DGg79uNX_kXYyEiIsY6138h-5bM73uW-Zl55x4Oeey9MDmRV_Bdzltp9nPhNa6oH__pgX4VFuUv0-7hb2Erl22PySZg6k-be3JvzLYepJ7AIFV0nyIun39AyK-T5Iu7z94vs4VdcT_uRIBxAYRiyAW48xCfBCsIqzkqzFide8x0yefjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمایت ۱۳ همتی بانک تجارت از جوانان با اعطای تسهیلات ازدواج و فرزندآوری
🔹
بانک تجارت با پرداخت ۵۱ هزار و ۵۷۷ فقره تسهیلات ازدواج و فرزندآوری شامل ۳۳ هزار و ۳۷۶ فقره تسهیلات ازدواج و ۱۸ هزار و ۲۰۱ فقره تسهیلات فرزندآوری جمعا بالغ بر ۱۳ همت، حضوری موثر در حمایت از جوانان و خانواده‌های ایرانی داشته است.
🔹
این بانک با بهره‌گیری از زیرساخت‌های دیجیتال و سامانه باجت، فرایند ثبت‌نام و پیگیری تسهیلات ازدواج و فرزندآوری را به‌صورت غیرحضوری فراهم کرده است تا متقاضیان بتوانند آسان‌تر از خدمات مربوط استفاده کنند.
📱
tejaratbankofficial
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/693235" target="_blank">📅 21:03 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693234">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
آجرلو، عضو رسانه‌ای تیم مذاکره کننده: با تفاهم اسلام‌آباد ۸۰ میلیون بشکه نفت فروختیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/693234" target="_blank">📅 21:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693233">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
واردات سامسونگ و ال‌جی آزاد شد  سازمان توسعه تجارت ایران در نامه‌ای به گمرک:
🔹
با توجه به تصمیمات کارگروه ساماندهی مبادلات مرزی، واردات لوازم خانگی از مبدأ کره جنوبی دیگر با هیچ محدودیتی مواجه نیست.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/693233" target="_blank">📅 20:54 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693232">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25fa0a337d.mp4?token=DQoZA6UJ8jRSGQpdxkhvxCWuiyJ9-9x8ahhHd-iCgnoT8S_xCyz3-y7XYiEfaznf7y0i7KqW030duLTPeFQQpgvHEKeSCJxA1WzBPO0wvGDTeSPs_ie5PwOYtTVa0TpD6tbvZ9TyprC2arbzd5XZUD6DuTv3gmTD1bQC11czVKXuMXtDQZ3Kq-dUViHtdilbax1Awt5WhdjTbtPiItf6W91QxtQ94Qr-_EvqTAkJQkZtdW6gIOmpmEfe40enDkUcf4W3zfp4VAlJAMtIhlyXm0ZACrvHCd4KEcFjEA8ukfH-S35eVlVFmZud-7rIpSUH9sgIRPKmnOGiX3FIWHt3OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25fa0a337d.mp4?token=DQoZA6UJ8jRSGQpdxkhvxCWuiyJ9-9x8ahhHd-iCgnoT8S_xCyz3-y7XYiEfaznf7y0i7KqW030duLTPeFQQpgvHEKeSCJxA1WzBPO0wvGDTeSPs_ie5PwOYtTVa0TpD6tbvZ9TyprC2arbzd5XZUD6DuTv3gmTD1bQC11czVKXuMXtDQZ3Kq-dUViHtdilbax1Awt5WhdjTbtPiItf6W91QxtQ94Qr-_EvqTAkJQkZtdW6gIOmpmEfe40enDkUcf4W3zfp4VAlJAMtIhlyXm0ZACrvHCd4KEcFjEA8ukfH-S35eVlVFmZud-7rIpSUH9sgIRPKmnOGiX3FIWHt3OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یعنی این جنگ رو ما خواهیم‌ بُرد!
🔹
جملات طوفانی شهید آیت الله خامنه‌ای خطاب به مجری آمریکایی.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/693232" target="_blank">📅 20:50 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693231">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
مهران مدیری دوباره راهی اتاق عمل شد
🔹
مهران مدیری برای دومین بار طی دو ماه گذشته تحت عمل جراحی دیسک کمر قرار گرفت و ادامه تولید آثارش فعلاً متوقف شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/693231" target="_blank">📅 20:47 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693229">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3053de3fdc.mp4?token=MQu6EzxyBPvgC-0zZYPx_t1rf4T1rEMlOvsDT2PO98SwAhuW6NUHcpi_PFnJpsh8-noMvIHTOpRsQYW1psU3SMqXgYxpfDaQYKRlgF-iMbSw9MO1ZXpcpgHaiWoJYOnOAcwFPfdd5HDLvp1KN8OoFJnzCTdzTkJbntTkJgN6U94g3qJczgiZJl8a_XjUqhM6ZYAVWh1AwYwm42LjgykAgEy6iDpU8UcPcetdnQBXc0JTLvb2xW5FXA7y12BiU6PI7dOnVAHeFEkbCxPoebtvDE9xZUOc11njQQ4eCDxN54khdE-XQR5sFX9rvmWwRHkt6pBRkafr7MLzE9NbFV0jGBlgpKbOGaI4OIY16jRTlrP6fmQByaPN_x0GFE77_jlilvP_cERdXd4QoitfEJlSwSQCyPV443vdNcvayi39Bv7Sr6S3GOd5x8uR6IhYS8AbuE8E4L6JW0oqa1AyzFNZe4Rz_T-1pceTE1N5yXfkUanftKZWnXHktHG0mWOtocThgliC830oJz0LUc5171FH2DqwrpCrv7HibY9V9URX9mxhZ2x-W6SaRuDTQ6kC1WhOhw_OUCtxXMX_U3c0UVkLJm6yDIWOoVzaJwUz4cAyd-RMoVc-RYJyu1oSizYhJer1AQYKDSGYxR9sNxmDB3ddBu6XQdSQI3y8IBD6dla4B6Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3053de3fdc.mp4?token=MQu6EzxyBPvgC-0zZYPx_t1rf4T1rEMlOvsDT2PO98SwAhuW6NUHcpi_PFnJpsh8-noMvIHTOpRsQYW1psU3SMqXgYxpfDaQYKRlgF-iMbSw9MO1ZXpcpgHaiWoJYOnOAcwFPfdd5HDLvp1KN8OoFJnzCTdzTkJbntTkJgN6U94g3qJczgiZJl8a_XjUqhM6ZYAVWh1AwYwm42LjgykAgEy6iDpU8UcPcetdnQBXc0JTLvb2xW5FXA7y12BiU6PI7dOnVAHeFEkbCxPoebtvDE9xZUOc11njQQ4eCDxN54khdE-XQR5sFX9rvmWwRHkt6pBRkafr7MLzE9NbFV0jGBlgpKbOGaI4OIY16jRTlrP6fmQByaPN_x0GFE77_jlilvP_cERdXd4QoitfEJlSwSQCyPV443vdNcvayi39Bv7Sr6S3GOd5x8uR6IhYS8AbuE8E4L6JW0oqa1AyzFNZe4Rz_T-1pceTE1N5yXfkUanftKZWnXHktHG0mWOtocThgliC830oJz0LUc5171FH2DqwrpCrv7HibY9V9URX9mxhZ2x-W6SaRuDTQ6kC1WhOhw_OUCtxXMX_U3c0UVkLJm6yDIWOoVzaJwUz4cAyd-RMoVc-RYJyu1oSizYhJer1AQYKDSGYxR9sNxmDB3ddBu6XQdSQI3y8IBD6dla4B6Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محسن کیایی و پوریا رحیمی سام در سانس‌های ویژه «قبض روح» روی صحنه می‌روند
🔹
بلیت سانس‌های ویژه از طریق فیدیبوآرت در دسترس است.
لینک تهیه بلیت
👇
https://fidb.ir/t8x
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/693229" target="_blank">📅 20:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693227">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
ادامه پیشروی یمن به سمت باب المندب
سخنگوی نیروهای مسلح یمن:
🔹
نیروهای یمنی در کمتر از دو هفته با پیشروی در جنوب و مناطق ساحلی، به مناطق مشرف به تنگه باب‌المندب رسیده‌اند و در واکنش به افزایش حملات هوایی عربستان، با حملات موشکی و پهپادی به عمق خاک این کشور پاسخ داده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/693227" target="_blank">📅 20:24 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693226">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6693eaba7.mp4?token=EUMTPevU_VG0fPCl1r63F0Btb57Ke2T5kZKyJnigKWEsqCHXyxhJcYLR6Pl7K7dAm8icyQ1Mk5j7k8qAdPFGwCVyJn18QRbwwC-lLUCkKIXctSDHaMM8EWmE6PdgBLIIXMvvdQPyVCEFDNl_etsmlI6-z1IzJBDUY7GWsE8-aaPqYCNQh6rPGU7WWc3E_bMVgct5j4hXpS2IcLldGxs9Wh3-MjdfNf2SPMrvYRhidNv3zCR2T496Wgmxcrrn2q1KlyAuyFZLGw1R44aQSEDT0uHRVf95dPfupF2l4oOIiRV4kUa47drG3hXSpnjp8nSl_i8h5UEi9PHOWqYHnNTqnU3jyfC2tsy7JuNOTWTPjdBXoeEMmdk5AqpMY0ehJckQZnKxoM3X08AKGGFCMyqaASFsM4UH7FZHkV-rhDosAK6FfNX9Oz5ra4YC29_WgiUklX8yyBpnOC__k4sVlfrXy714FQZHx6mTO6U1wfvLcNPcjDTE4wg8qxqtknNA6bWPC8LHXUJBbG4nGjXrEtnH3xsHmG8NjwljgwemTTMpKM601U2fkLYvnFEx6KkHVzoq3yCfmLKT9kFseyW22Rbr05EsQ6TR5XaO8wjePaBKayjpnu8mnzE948K0Q7SSPiJoVErvoW8fneQr4LP26r7Q4g7v3FIGPotVJUT_DhR1dxk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6693eaba7.mp4?token=EUMTPevU_VG0fPCl1r63F0Btb57Ke2T5kZKyJnigKWEsqCHXyxhJcYLR6Pl7K7dAm8icyQ1Mk5j7k8qAdPFGwCVyJn18QRbwwC-lLUCkKIXctSDHaMM8EWmE6PdgBLIIXMvvdQPyVCEFDNl_etsmlI6-z1IzJBDUY7GWsE8-aaPqYCNQh6rPGU7WWc3E_bMVgct5j4hXpS2IcLldGxs9Wh3-MjdfNf2SPMrvYRhidNv3zCR2T496Wgmxcrrn2q1KlyAuyFZLGw1R44aQSEDT0uHRVf95dPfupF2l4oOIiRV4kUa47drG3hXSpnjp8nSl_i8h5UEi9PHOWqYHnNTqnU3jyfC2tsy7JuNOTWTPjdBXoeEMmdk5AqpMY0ehJckQZnKxoM3X08AKGGFCMyqaASFsM4UH7FZHkV-rhDosAK6FfNX9Oz5ra4YC29_WgiUklX8yyBpnOC__k4sVlfrXy714FQZHx6mTO6U1wfvLcNPcjDTE4wg8qxqtknNA6bWPC8LHXUJBbG4nGjXrEtnH3xsHmG8NjwljgwemTTMpKM601U2fkLYvnFEx6KkHVzoq3yCfmLKT9kFseyW22Rbr05EsQ6TR5XaO8wjePaBKayjpnu8mnzE948K0Q7SSPiJoVErvoW8fneQr4LP26r7Q4g7v3FIGPotVJUT_DhR1dxk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علی ربیعی، دستیار رئیس جمهور در امور اجتماعی: بخش بزرگی از مردم می‌گویند هیچ راهی برای اعتراض ندارند / باید سازوکاری ایجاد کنیم که مردم بتوانند اعتراض کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/693226" target="_blank">📅 20:18 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693225">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
صالحی: چین میزبان نشست سه‌جانبه ایران و آمریکا شود
🔹
علی‌اکبر صالحی، وزیر خارجه پیشین ایران، پیشنهاد کرد چین با میانجی‌گری و تضمین اجرای توافق احتمالی، میزبان نشست سه‌جانبه ایران، آمریکا و چین باشد.
🔹
او تأکید کرد با وجود از دست رفتن برخی فرصت‌های دیپلماتیک، کانال‌های ارتباطی همچنان از طریق قطر و پاکستان ادامه دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/693225" target="_blank">📅 20:12 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693223">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QhsLHparwxx_cIt4XCh8X5Jx6G2zCIUi4-DvpUB9pUdOGXnyPMl6HSsg_u6YPKlC0YQ-QH4nwbrWCoAxf63ImaZglWp5beiYjVNEY1GKrQkj9eLmpmdCKkNRF7rINCRVUa_gUNcFW28dePturWrL0xH74hWwqcKVNPNsXqz0jWOV-TfPUs8ymrFM4P7vxSbd5lzM4Djlgd1LoNsxYYenlc-rKMey5SZ513EulpGNz0FC7OyuqJ4mE72ukSJ9neoJRV8BNdY-qP9t8O0ttEQQDl12MSRanjd_fskvTAuRs4WCUfXw9QDKbRR4hXASZuf0u0jteelKR7FJtY614vpuPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میلی: ۹۶۵ کیلوگرم طلای کاربران موجود است؛ تسویه و تحویل ادامه دارد
🔹
میلی در بیانیه‌ای درباره تأخیر در بخشی از تسویه‌ها، ضمن عذرخواهی از کاربران اعلام کرد معادل ۹۶۵ کیلوگرم طلای مربوط به تعهدات آنان به‌صورت فیزیکی در خزانه‌های امن و بانکی نگهداری می‌شود.
🔹
به گفته میلی، محدودیت دسترسی به بخشی از این طلا، از جمله در بانک کارگشایی، روند برخی تسویه‌ها را کند کرده است.
🔹
این شرکت همچنین از انجام بیش از ۷ هزار میلیارد تومان تسویه ریالی و تحویل فیزیکی بیش از ۳۶ کیلوگرم طلا در ۳۰ روز گذشته خبر داد و اعلام کرد پیگیری‌ها برای رفع محدودیت و انجام کامل تعهدات ادامه دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/akhbarefori/693223" target="_blank">📅 20:10 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693222">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">19-1 Ane Manaee (1404-02-06)Shahre Moghadas Ghom</div>
  <div class="tg-doc-extra">@Aminikhaah</div>
</div>
<a href="https://t.me/akhbarefori/693222" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
تفسیر سوره محمد| جلسه نوزدهم؛ بخش اول
حجت‌الاسلام امینی‌خواه:
🔹
توصیف منافقان و بیماردلان با ظاهر مؤمنانه و ایمان مستودع، در سوره مبارکه محمد [01:46]
🔹
چهره غلط‌‌انداز حق و باطل در فتنه‌های آخرالزمان؛ خطر سقوط برخی مؤمنان و فرصت عروج برخی کافران! [07:50]
🔹
وقوف به عجز و کاستی خویش، اولین و بزرگ‌ترین گام است در مسیر خود سازی و اصلاح نفس [17:45]
🔹
موضع‌گیری جریان‌های مختلف با فرمایشات رهبری در لباس تبعیّت از حق؛ مصداق "زُیِّنَ له سوءُ عمله" [22:08]
🔹
مَثَل فتنه‌های بزرگ و ایمان‌های ظاهری، مَثَل چوب است و لجن های ته حوض! و تکانه‌هایی‌ که باطن ما را بیرون می‌ریزند [26:50]
🔹
امتحان ولایت پذیری، سیلی خوردن از ولیّ خدا و ماندن پای اوست! نه صرفا ناسزا شنیدن از دشمن [31:13]
🔹
دایره امتحانات اهل حق؛ از شیرین بودن طعن و آزار فسّاق! تا شنیدنی بودن اذّیت مؤمنان! [34:43]
🔹
آیت‌الله مصباح و مخالفت با هر نوع مصلحت‌سنجی، بی هیچ رودربایستی! مردی که «از خدا کوتاه نمی‌آمد.» [37:56]
🔹
دین؛ ابزاریست برای توجیه نفس، یا تدیّنی برای تبعیت از حق؟! [42:30]
#تفسیر_سوره_محمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/693222" target="_blank">📅 20:08 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693221">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
محکومیت ترور رهبر شهید انقلاب از سوی لاوروف
🔹
وزیرخارجه روسیه در سخنرانی در مجمع عمومی سازمان ملل در نیویورک ترور رهبر عالی‌قدر و نمایندگان دولت ایران را نمایش غیرقابل‌قبول از دیکتاتوری و زور خواند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/693221" target="_blank">📅 19:56 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693220">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02bdbcc32d.mp4?token=TMGmIEzl4krRWzjr6cjQhbZ8InSyApQisLye792RkE8RDdcDUUCGPvC_2F_lWzO-JzSIOsivAVMsczW2blaXvBVdUgp0mMTclOsxcepL31gIxwmd74vKsQL32EVowf6gr0CwhRrfaVMgrqxtEdAiZ_Td1rQUP6m-I6Z9HVuIqsDFCL5Hb3roVzUgFqRocOT1R1grgz18Lo1hC8jv19_vffUiPt1rQFi7mOX2zu4PlSPc9YQmdMt4kLiW-tcUpXdqiMuyQVMRKfDxli_MV_O2iQ1SOh1YbJUNwxuKOS4PcgCvC8in9ceNvln9ZrplJhYcA8CXCJY_NlJ7SBA1vVHztA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02bdbcc32d.mp4?token=TMGmIEzl4krRWzjr6cjQhbZ8InSyApQisLye792RkE8RDdcDUUCGPvC_2F_lWzO-JzSIOsivAVMsczW2blaXvBVdUgp0mMTclOsxcepL31gIxwmd74vKsQL32EVowf6gr0CwhRrfaVMgrqxtEdAiZ_Td1rQUP6m-I6Z9HVuIqsDFCL5Hb3roVzUgFqRocOT1R1grgz18Lo1hC8jv19_vffUiPt1rQFi7mOX2zu4PlSPc9YQmdMt4kLiW-tcUpXdqiMuyQVMRKfDxli_MV_O2iQ1SOh1YbJUNwxuKOS4PcgCvC8in9ceNvln9ZrplJhYcA8CXCJY_NlJ7SBA1vVHztA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئوی پربازدید از دانشگاه آزاد تهران
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/693220" target="_blank">📅 19:52 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693219">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e51551b9b.mp4?token=m7BPyGm-EHLCWUecdmg6_7sDBkV6zi5Vc5HwpmQNESuTeCoVblLb6SG4-bjZArTU3dSV215Nw3vU9w-7OzYqGYFwtf40g_W8vHwZl6cFhEDRmrWnY5laWA5h-cjD8MnQAwSkvBB7jm_rF8bI0z3vKn6Q7-yxg64vVUyqdZcS1VvtX-Eq1gRq0utv4QDIkJ8hSzBuYT5Pw_P0M5J0OIrg-8K8laA8V2BulXxb1bw1wixRl2lwMN6idfvAH1O-A9LwcBWY8Ho7kKIp03syYqVsIFdLwh7vnybjUklAuHndo9AuFCgH5tiXfqQPYXQ7fxeaKqoG_da-jdFWSVL7WmUqvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e51551b9b.mp4?token=m7BPyGm-EHLCWUecdmg6_7sDBkV6zi5Vc5HwpmQNESuTeCoVblLb6SG4-bjZArTU3dSV215Nw3vU9w-7OzYqGYFwtf40g_W8vHwZl6cFhEDRmrWnY5laWA5h-cjD8MnQAwSkvBB7jm_rF8bI0z3vKn6Q7-yxg64vVUyqdZcS1VvtX-Eq1gRq0utv4QDIkJ8hSzBuYT5Pw_P0M5J0OIrg-8K8laA8V2BulXxb1bw1wixRl2lwMN6idfvAH1O-A9LwcBWY8Ho7kKIp03syYqVsIFdLwh7vnybjUklAuHndo9AuFCgH5tiXfqQPYXQ7fxeaKqoG_da-jdFWSVL7WmUqvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محکومیت ترور رهبر شهید انقلاب از سوی لاوروف
🔹
وزیرخارجه روسیه در سخنرانی در مجمع عمومی سازمان ملل در نیویورک ترور رهبر عالی‌قدر و نمایندگان دولت ایران را نمایش غیرقابل‌قبول از دیکتاتوری و زور خواند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/693219" target="_blank">📅 19:48 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693217">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f3137cf5f.mp4?token=XhLWEpw0t2tUk-66YtOMej-rE5XlePMIO1OXYeJzUs3X64JA4zBFhklYcS2xgR0Y3otBkbg3pLzywgI5dVntrALVhzyPwtnomT947eNHzDe5lzoyKH8R9B8m5uiNZNdBWAwTNR96XG6hB1-9bPV5k5k4YPMUXV5GNrw2x7mQBAbtkR8AaYKKrSg22hTPqRQFAwdL6HT4AKAZa4bH5Y_CYlAjvn2q97ALOSX61sFiijn3S3SCwmBJjm6ILOkdEFTDr6-tMen9-ypLYyeDY00ojr5gLsuoov5vl-Cte4IoXii0QSged8YVqB-GfjH-Bz-hCo3qB2zuD_nNS333b76K8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f3137cf5f.mp4?token=XhLWEpw0t2tUk-66YtOMej-rE5XlePMIO1OXYeJzUs3X64JA4zBFhklYcS2xgR0Y3otBkbg3pLzywgI5dVntrALVhzyPwtnomT947eNHzDe5lzoyKH8R9B8m5uiNZNdBWAwTNR96XG6hB1-9bPV5k5k4YPMUXV5GNrw2x7mQBAbtkR8AaYKKrSg22hTPqRQFAwdL6HT4AKAZa4bH5Y_CYlAjvn2q97ALOSX61sFiijn3S3SCwmBJjm6ILOkdEFTDr6-tMen9-ypLYyeDY00ojr5gLsuoov5vl-Cte4IoXii0QSged8YVqB-GfjH-Bz-hCo3qB2zuD_nNS333b76K8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پشت پرده تعلیق پروازهای ایران به نجف   یک منبع عراقی:
🔹
نخست‌وزیر عراق دستور تعلیق پروازهای ایرانی را به وزارت حمل‌ونقل این کشور داده تا این تصمیم به فرودگاه نجف ابلاغ شود؛ با این حال، تصمیم‌گیری درباره پروازهای فرودگاهی در اختیار سازمان هواپیمایی و وزارت…</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/akhbarefori/693217" target="_blank">📅 19:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693216">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
سی‌بی‌اس به نقل از یک منبع آگاه مدعی شد: مذاکرات آمریکا و ایران با وجود رد پیشنهاد توسط ترامپ، هفته آینده برگزار می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/693216" target="_blank">📅 19:30 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693215">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a21de8c005.mp4?token=jKJmlUkVjS4GBzWr902Kbf7W_wR_IdYzCMn-J7-0k5uLHL-ms8jmVlDJQ2sX27_GeNuimYIXYOxj8K_-3DWt05ie1NANbzDRqfNtn9_jZlJdPk1Dm9uEeb3umAAVFwFP7Uy7euXb7B8HPfzwaVMzCQWktGiPA4OIk-oLnSi_FSYJkAEU-GBwmDPbfLTw67KORO94k0rjs4aA_NF_xgag6B1ed_d1Kn12bLppZB099sqSmXc6bjQJQ_1eM8UWMadoud8eY49p_XQB61eHCBauVVTZ-_subKslqK1W6kYBv0UtWG2EY5y0sxoKymL7VQnAHsg10Hq237lS12-KSVwqBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a21de8c005.mp4?token=jKJmlUkVjS4GBzWr902Kbf7W_wR_IdYzCMn-J7-0k5uLHL-ms8jmVlDJQ2sX27_GeNuimYIXYOxj8K_-3DWt05ie1NANbzDRqfNtn9_jZlJdPk1Dm9uEeb3umAAVFwFP7Uy7euXb7B8HPfzwaVMzCQWktGiPA4OIk-oLnSi_FSYJkAEU-GBwmDPbfLTw67KORO94k0rjs4aA_NF_xgag6B1ed_d1Kn12bLppZB099sqSmXc6bjQJQ_1eM8UWMadoud8eY49p_XQB61eHCBauVVTZ-_subKslqK1W6kYBv0UtWG2EY5y0sxoKymL7VQnAHsg10Hq237lS12-KSVwqBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ربات پلیس انسان‌نما به خیابان‌های چین آمد؛ گشت‌زنی T800 در کنار افسران مسلح
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/akhbarefori/693215" target="_blank">📅 19:24 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693214">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tsEYoA24CFCscHkUA56ry1kDF-Bqb0nOgknm3hEA4foxKCgxekeBp7AumdWcy4OfmFgI2zji_TfingeFQREHmNPrQl_zXZGZQ8DOopwKXqF-Ear0bkRDIcNvDBNXitXKmoABlqs_8BgRzdF9SD1O0LdwDxB_2-67wb15TNP0o1cOROonUjC7ChEZe_p0OtHRp03DOuAVEvHpyyMWJrULdkezEgvIoCz0SR0NvQvpJ6I14ztCoZW7MvbNQ_e8IwI-mJDunAqjo0tYFSQdSmSUfv08dStg3HbecQ3V5Fqw4iq5tV-ZTCOdr3-xCV0M815IWV-TYwK-IEYkxL5lcdvMag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ممکن است اسرائیل جنگ جدیدی به راه بیندازد
مرندی، کارشناس مسائل بین‌الملل:
🔹
به نظر می‌رسد ترامپ تحت فشارنتانیاهو و متحدانش برای تشدید تنش، پیشنهاد ایران را که مبتنی بر تفاهم‌نامه اسلام‌آبادبود، رد کرده است.
🔹
اگر نتانیاهو تصور کند که درانتخابات شکست خواهد خورد، ممکن است برای به تعویق انداختن رأی‌گیری یا ایجاد فضای«همبستگی ملی در شرایط بحرانی» (پدیده «حمایت از پرچم»)، به دنبال جنگ باشد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/akhbarefori/693214" target="_blank">📅 19:14 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693212">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hu48Yk_O1A_Izr2doWg9DDLFuS8Xp00ABKmPcEIl5kPOUzYkCrjD_RA5X98IqxRJ9dTq7dxL0S4kR4TSQ03EnkRXXkOYcjrWsd5T1P3VYM0goOmhMix7E-Q_7wuOLfOwW0GbmVvDFlHIWB6o7K97zwhQL0atdnpzX7WsCbAMBrSs9zfOds2CLmJzG4eEP18YAYu1iibvMjvd98I20ZAh16TiZMxPFZPlthl2gCHTT0LRz0MKlgqjeJ13Ngwvk9QQeVOcXS5SkDYku0n13-T2zbDd_yXHsb3Dkf7I-cJyvWJEx88aFyEOkNIZ37NQN5yxk42ZyQ7prvvNaKO1OORs-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نجفی، مشاور محسن رضایی: هرچه جلوتر می‌رویم هزینه توافق برای دو طرف افزایش پیدا می‌کند همانطور که هزینه منازعه وسیع‌تر و شدیدتر می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/akhbarefori/693212" target="_blank">📅 19:07 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693211">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
چین: از بازگشت آمریکا و ایران به توافق اسلام آباد استقبال می‌کنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/693211" target="_blank">📅 19:06 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693210">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
ترامپ: پیشنهاد ایران را رد می‌کنم
🔹
ترامپ: من هر توافقی را که بر اساس آن ایران بخواهد فوراً تجارت را از سر بگیرد، رد می‌کنم. #Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/693210" target="_blank">📅 18:57 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693209">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AmitlysWqDgI4VvZ8pMOuWrhhr68OfyNr9x9hlN_vDavrqUp5OmYeiP-dx11W7HkglmhocpfHfxYLeYIdJTU8-0e3BjnV5gIZ_REj61ZfHG8T6XHYWr_WF-4ufXVbIvx1Q2iaTPshHvPD-PelPIOMABeid6DFk2k55KTJ2tfBY1PozO7WX9WTwdj4-O67lX68vMIsAfqzuVy_jbwKEpUzdbrCaXvik_lvhmukqdv4vyaq8ZEEoHWIGeuzcN4Nh2Mm7H2HFjGAp7zsh77rbwGNASDGo_eLMZwfyqK151KspANF67D4ljOFU80na2JHOui5QYqM5xHrWcGwvmPYTNeGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واردات سامسونگ و ال‌جی آزاد شد
سازمان توسعه تجارت ایران در نامه‌ای به گمرک:
🔹
با توجه به تصمیمات کارگروه ساماندهی مبادلات مرزی، واردات لوازم خانگی از مبدأ کره جنوبی دیگر با هیچ محدودیتی مواجه نیست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/akhbarefori/693209" target="_blank">📅 18:47 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693208">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
ادعای سفیر عراق در تهران: بغداد برای بازگرداندن پروازهای میان دو کشور به وضعیت عادی، رایزنی‌ها و تماس‌های فشرده‌ای را ادامه می‌دهد و توقف پروازها را موقت و گذرا دانست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/693208" target="_blank">📅 18:42 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693207">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
تقاضای مرغ ۵۰ درصد و گوشت قرمز ۶۰ درصد کاهش یافته است
مسعود رسولی، دبیر انجمن صنعت گوشت و مواد پروتئینی کشور در
#گفتگو
با خبرفوری:
🔹
واردات گوشت و مرغ بسیار کم شده و کشتار نیز کاهش قابل توجهی داشته و جوجه‌ریزی نیز نسبت به دوره ارز ترجیحی بسیار کمتر شده است.
🔹
تقاضای بازار برای گوشت مرغ حدود ۵۰ درصد و برای گوشت قرمز حدود ۶۰ درصد نسبت به سال گذشته کاهش پیدا کرده است و مردم دیگر از پروتئین دست شسته‌اند و به سمت کربوهیدرات رفته‌اند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/akhbarefori/693207" target="_blank">📅 18:39 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693203">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nDvEyDTUu9NCqYmJsuk1P7r9UzaqX25z6jton1EbeMy3H1Z6TvUlFYKabJBfuZtG0UMI61KvpvnK9xDAdXf5SWAbTGp1I-72l2ymd8BmnFwOv2WKq_GAtqXly2xI6ldnPUf0PJA98jTOgbFTqPJQZPUGJTL3L6oWyTJabLFUlrft_J0PYmJyX5wIaGhllMF_vxF8uaxS-y9pxkg6AlwCNY1WBTsf8Jb9MhGN4jKFZgJdJn0sxCKn55Ejz8S8K103UDI4mVjrJcFfXfXKlGOLL2QOb7VuDHB3BnJBGMO4uFKphwlSEGO25KtsfT2Au10-6yMQ92FNIG6xZ1Y92ey8ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fAwCz0YwNbwXBDdoesz1vGO4d8DS8NYcmWQ2NTN4F4kNzWvXS-d4KyYnsA2DEBZwnBhG1Wgr7PCodff0VKwif8nIZImtxf0O2RHLPXH8zmX38tYFTDKZ1VoisRBogCox7OPiLeEotc_JziQqvBHI8k26YCvtMNCkz1IsBkDqpqUf_a929fRms-cRzY5eTMMKcnT1tua5gdwvtc1PB11zRDnGJPLLl7K8p-721OpT2eyjDc-FHLudXBqJGWIbmGM4xoMUaxOWKQC1rR4Rpa7CkZabMSwQDU6-VlB7_AjsTS90Y3_LTl_TWdymKC3eQLw99nx3X50A9GwvhoajIarmmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ueglZIg8-GEqajnbleGd-ecKfk4XAAVBfKIouhn_v8KMjf_B6OIkTBaLkcvlLkz0bRU_DniVvAUmKjChWFXhtJogx9gPmqA5C9HgKkp695cFhJMWoxYW_eLucBThI2tg6h6l6XvIpuryViIiZGSSZ88FE9MTTW9XgglLbs_wHfLQmnGrNGQYQcvhm3taYAvd-x_7d2rsRLlJu_TjTe3118Fjz7Mc10L9J5UrkhInTgDvv1OSrk8u_OrZER5Tsgt5_uHaMqH7xaRXCvWUVZHQDAz9VUA_HVneIYdHffkCSrdqjze8LBJdOYVvXBNqh1dNP9S0nYay5IyM-wcSglAcvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uhcFRV6Ro0uBVJzy6rfVIEC5L0btiwBLAI2alrwJAivWQF-qTGWgpfMgqcvHLTquqwonjBkyo0db6IU0kMgZipZFHhb6GYTJmdMMC9M_7wSr0hmMS8shgBTUgJ5jEyQn0377j0BlORb5vp_UzSedy8hN0zBWtEpehBnLZRHhcTZDyBaaMrsP3ffynhvBKR3yv44kbR6Lc60aoRIxDRO80qA_RKdVUjGTVMmB2ev1yO836OfjXmxzjaCXwvVGP-LMyzIQcQZNKrXnvkfuACrM_Vr3B3liFfebMerMr9TfW2E_KgrV6oks4lX2cSLiVEuhJUgtrOAWlAgfDkur0oAsmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
پاییز با این دسرهای خوشمزه یک حال‌ و هوای دیگه داره
😋
🍁
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/693203" target="_blank">📅 18:28 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693201">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
ادعای اکسیوس: در حالی که ایران می‌خواهد هرگونه مذاکرات را بر موضوع تنگه هرمز و محاصره دریایی آمریکا متمرکز کند، دولت ترامپ خواستار آن است که ایرانی‌ها با امتیازدهی در موضوع هسته‌ای موافقت کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/693201" target="_blank">📅 18:21 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693200">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
اکونومیست: آمریکا پس از ۳۵ سال ناکامی در بازسازی منطقه، در حال عقب‌نشینی است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/693200" target="_blank">📅 18:12 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693197">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yv9l-oJANVNY7SGKW1-aAm2jdJzi6zKaPZ6Zb1dK9oHf_NbQjlUMmAioZG4qXNLXMgEkWvD5hk7LEj1u4RqCW6pB-JaokOI2Ry2hXwehTn308tDPhTgxnjC4L0iuZf-xa-uLnbuBes8YfzF7TvKczYS2lL5ZP4TJUm8VLGjb_n0T7L-gGG1dVIiX26Dg3k2-lQu63Yvl1MMTcsOuCFJ-U45xcSF5RfKCLKhrPdtKTrKwoK6RwNqVvXNSo3j_D_txmV2cTy6gvUMtbq_5krD9zlVO1DpU4ptY4kltc0v44L8GNeDhp9s0tOqK9L6joUxTvoRvKfUnEOPOxMn6oaJglw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EwdDbZ8F4HZctj-Azc8NrTwMNjOcryarDAJ4KczfF5w3SpTJurJ9fy8xYVY1_WarVYVWNyjdxiKDxfgmR0ZJ5h-cZXu-goxOSziRgTwML6O9aYy-BzAX4QZRd-DnnBs0vlrfaqMpn2Q9zyerfZY8lktrUuBAG5RcA-HIhoxF-3eNM-5qM5VTTBmcpXQWd7-fBaRmP0FdSnRFBnEaDXsZ5EBPl0AMWev2BMhxHBvCRbP5uWG2mZyPzhe1tsSmmSxCH8r_QrldHGANZWL8x9yNI5gWH0C5rEq9NHDKmSmG_ihFxNagMtZZOCtRg8h9D0ewP8ASDlIuegose1ZHDTFkbQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05c7e8903e.mp4?token=chz7IoIBeHO4wvdk6WoI_5QVzinHs8CBLq85uN8gl0a74IujAy6JZ9WSn52m_KQYYwpXuuN7ypnFzrd5S-M1AP45Rzr0d7jXzG41v1fgwYJQCo3E1KpUiDg9JOaWdSAEiccxRgYZWudEI-d2rnx0QwgCt-Cz-9WHaceZzQMMeimvLbkMIad4UHsL1IMrxK5tJry4_gCmc_4BEiz2kdegLluXAGjiYEAblMz7Rw4GhBmZYZK5Nr57jhzxa1z-0jTog2Sq-wb8-ccLM8YTrcC9AUShYb4KlUQVbid5P5r8xv5SR1yn1v6rIzLdAssC8nZiLOJ48qcTnxmw6N1QdtuU4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05c7e8903e.mp4?token=chz7IoIBeHO4wvdk6WoI_5QVzinHs8CBLq85uN8gl0a74IujAy6JZ9WSn52m_KQYYwpXuuN7ypnFzrd5S-M1AP45Rzr0d7jXzG41v1fgwYJQCo3E1KpUiDg9JOaWdSAEiccxRgYZWudEI-d2rnx0QwgCt-Cz-9WHaceZzQMMeimvLbkMIad4UHsL1IMrxK5tJry4_gCmc_4BEiz2kdegLluXAGjiYEAblMz7Rw4GhBmZYZK5Nr57jhzxa1z-0jTog2Sq-wb8-ccLM8YTrcC9AUShYb4KlUQVbid5P5r8xv5SR1yn1v6rIzLdAssC8nZiLOJ48qcTnxmw6N1QdtuU4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زیبایی‌های جاده چالوس زیر چتر پاییز هزار رنگ
😍
🍁
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/693197" target="_blank">📅 18:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693191">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AIUCa_7o4uO9vEiq0GObn0dIzKiWA-wISl-Hh7ywi9tPJaetMgfWL27KS2R3d1fehM1GFdshQqxm-6N-pYMRvbqfKJzn3I43t_pzw_iG5VGOUI5YEBCf-UoyBnz2_uZzPTJo8yScwcEIgJ4PFHvN0n-mml1HnYKyPOqXyz-W-A0ztkccER5M3s5R5DV7Y_k14IsRno5zKalApQFGfxgYn3IKsLPB6bHnskxtwqTGte4Db5nA5GmzygI--8QV_ilmkg_bnuCS3DEAAVlKeTbYbqmNclTvnyNJGhm4J6yQBtpLHzuQSMwTowVU4yrcQV7qd8E1L8_83bb0Lc7dFfz_yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ilkzDvqBJlzKBcB7atYdhfam7IXb108NbfQDhAlr1pDmqFMpgQexiO8MKNSxm_hYbfEdhQoYupurZHyt3gy7gZ9GC1lZ0f0ejQB0F1HkbS4osJPorxt2C59lVfqyihwx4hD20qQR8-SYTWMOoSc9C8Rx4Vn0LDwVuQ7mHJKFGNVmd6LJCtFlghR3bqKN9FLH-FBGhCOSUWtkxEohImmP9fWokRi8Kbp8oM6_v-qnXJgd5msh1nHX6t9lB0Me1hHZS16tpuWvcrKnVpq3_-xw8EKyVzLN3bzQRNPh9188ByZ9CMLddibyJQfGN3NTk_6WJGxbkaftbjrJf2PyukSArQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SZBBXpdFTcpLUftAvGtrKW1qjxGRzWQggo7Dax3pAPcp4TsRs65iOFn8FjsBRm5cSzIry-4VhDcr6im7YdiNqvVvc1jqJyudf3Dw_KSFuEPCAgHb3GRGaVBovJDX37Utpy1cWhKD1GnCS8n9SdnIulc0lIVJPlndMKdUFhsG3_Aio3HDriVkcik7X2ETOLDfZhe8QfZbxBvssQJHqeocGGy6WwNEuioQY3bS_7755qPIyA7hbOmF5O_DeI7FiWpgML6z6cV-8-vcDN_821jDCpgs6KUjtfCjWZhpD2vYKqlnezHnJjTdM7dRg5-seNkER9eKzC1Cv6Wjv7Qmf9o19w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JItzOKqOtHb4xgb6q7g2QchyQrf156HUNeAZeWduFfLC8_qv0zzp-InSQY4lAajJJN7FWqhnU38ZR0ddmCz-bamd3aTn-cCcw-pWEP6wP1aQIof7psBRUl6P6QZtP0VY8UVDpJKxLkLS6I5xCSuNEV8Fe9OwspfGWIbWX0SwTGX6kXAV-SlXIg33YFpqc3oV0KZ62lQUxLVuQah4bcHWdIbx8wsKWxHG6lTZfSHvbuYM-wd1cOYd47gbqNBBXKgEMiLTEmUCEyXpBFRxQiO5dr-pszxN21f_GweWuJasETQls_Xyw7AP2i6S6wK6GzeYw44qmZ3zybJCPCPMuBUgEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OYnH4Jcr3B-qguWtzRRSPT6PeCcSdP35BPdElOnGcs1e71Y4hsQpMLsWHiTs4e5YUGPr1yW4AbqZGZ09FkySgxQUSfrXkP8OKC_uAHGuzW5m-7m41aH1Pk_zvvwINvFCAhwonQV2GTufbsJyJt5rfScGT3v8vWNb-uwgOT2Ag1BA1t2J29Eeljbm72ZAtz2brrJn5afzsPUmpsi5A9egQStAmq2ABZQmY-J-Khk-j2JOTXqwcPeb0gHoLjMJqeXhV3il6rZ7QXyH4N6hHCVSeZSq-ELiv26jyxEN4nHkyYAZTJXbuQbo788EPTisiRHA48AMJMg6TdjHxhlDuOemsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N6q8p77AEHIjV9EBtqvOzLkFINXSHWjhLp_4kiUGGG_CKz8q10VV8HEAmZaRi3EuE53BwzaITnoWzWtbQHXe5MO3UID3ftZhfCXUDcMEHpE58--6qLSpYBWEKvJKehszYIDIc8BHRxxMCtg1MobUvv6c5Z--clGtUAcX45AKyJ96dZCTUJFYiS9GTclpHoQpz7vlJxAPU_8iqRj53wpLSU9T1VLXErzhY0CNgGze3C3YyzT6Lqh1hgwDg2bRIRf0I_4BSwpFRkuzRSBaRRGs4jY1Kxv2j_sA0Wg8clZGxuAYbzIG0mIqS3Fit3b7MvhrX2Q-PrxXcsDAKnAyDAN63w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
پیش‌بینی هفته
🔹
این هفته بازارها چه مسیری را در پیش دارند؟
🔹
از بورس و سهام تا طلا، دلار و دیگر بازارهای سرمایه‌ای؛ کارشناسان، روند بازارها را بررسی کرده‌ و از چشم‌انداز روزهای پیش‌رو می‌گویند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/akhbarefori/693191" target="_blank">📅 17:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693190">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b42553cf21.mp4?token=UkQBtsarBEctHtCgihBA41mU5w2Oi3eUWrMNn308ziGZ4kp8DuKq9KUPDpSBy7UxNAPnYTr9mpJthRmy9xObYHw-OBOLno7q4BHzxHey_EAfc_wDT5nvh7tcRRFPEIJ_pwL3_XxK-cYhlqUGIT3hfjgPdDimweJHkOqYfuLv7Xy8Jy_iR0sl6NdbWZ6H7654J6imSWSNyI3FDHHDYSkwNRpnYNXChXiVAzCK5mLtN8pVT0YRnvVXRvRcxJR9knwCeNwyseb3OFcztZfLym_qVcsdC4tfImcvCIuFYukJY1OjjH9qGVTtGBbo4ZHh9Za8HKHVdv-PAFozZo2iHwiO1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b42553cf21.mp4?token=UkQBtsarBEctHtCgihBA41mU5w2Oi3eUWrMNn308ziGZ4kp8DuKq9KUPDpSBy7UxNAPnYTr9mpJthRmy9xObYHw-OBOLno7q4BHzxHey_EAfc_wDT5nvh7tcRRFPEIJ_pwL3_XxK-cYhlqUGIT3hfjgPdDimweJHkOqYfuLv7Xy8Jy_iR0sl6NdbWZ6H7654J6imSWSNyI3FDHHDYSkwNRpnYNXChXiVAzCK5mLtN8pVT0YRnvVXRvRcxJR9knwCeNwyseb3OFcztZfLym_qVcsdC4tfImcvCIuFYukJY1OjjH9qGVTtGBbo4ZHh9Za8HKHVdv-PAFozZo2iHwiO1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هاوئین؛ بلور آبیِ فوق‌العاده کمیابی که درخشش آن خیره‌کننده است
🤩
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/akhbarefori/693190" target="_blank">📅 17:41 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693189">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
ترامپ: ایران با بستن تنگه هرمز به دردسر بزرگی افتاده است/ ما بزرگترین محاصره تاریخ را بر آنها تحمیل کردیم
#Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/akhbarefori/693189" target="_blank">📅 17:28 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693188">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
ادعای
مضحک
ترامپ: مقادیر عظیمی نفت از تنگه هرمز عبور می‌کند و دیشب ۲۹ کشتی از آن عبور کردند/ ایران می‌خواهد تنگه فورا باز شود چرا که خسارات زیادی متحمل شده
#Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/akhbarefori/693188" target="_blank">📅 17:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693187">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
ترامپ: ایران می‌خواهد توافق کند، من هم دوست دارم توافق کنم اما این پیشنهاد غیرقابل قبول است
#Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/akhbarefori/693187" target="_blank">📅 17:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693185">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
ترامپ: پیشنهاد ایران را رد می‌کنم
🔹
ترامپ: من هر توافقی را که بر اساس آن ایران بخواهد فوراً تجارت را از سر بگیرد، رد می‌کنم.
#Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/akhbarefori/693185" target="_blank">📅 17:21 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693183">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
ادعای العربیه به نقل از یک منبع آمریکایی: ترامپ به تیم مذاکره‌کننده ابلاغ کرده است که بدون اقدام اولیه از سوی ایران، هیچ توافقی در کار نخواهد بود
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/akhbarefori/693183" target="_blank">📅 17:18 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693181">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d54893051.mp4?token=HggAjoNmGRR8LoHf9YxlrnhxlaHVYnsEN2wxcGwbYs2hW30f4n1S3zbj8M0dwS0Rx-8khSlsvKZegeR9XrZEidoy6kTvWqoPSLQf0Cr_gnxKzHOnb6YqQKizX7JoxNqnMoIpLvtn0AkAi7JwCRmRAZocGy6hFXfd3MIobaD0BzOUaXZzECZy9AF3WXJa1ctgzFw5wKDs5XisDn2obhHgTVBsJrSsthWpFLyH3McpflNP011kTZOemoILnLrE9QApRALjDdM8a7CP-3rqJBO3jNnbHjA-6UiW8Rt9_3Cs7KlCjcxH-d51zxm4agigCSUUtWdGdA9I6frdxQp0kAGYTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d54893051.mp4?token=HggAjoNmGRR8LoHf9YxlrnhxlaHVYnsEN2wxcGwbYs2hW30f4n1S3zbj8M0dwS0Rx-8khSlsvKZegeR9XrZEidoy6kTvWqoPSLQf0Cr_gnxKzHOnb6YqQKizX7JoxNqnMoIpLvtn0AkAi7JwCRmRAZocGy6hFXfd3MIobaD0BzOUaXZzECZy9AF3WXJa1ctgzFw5wKDs5XisDn2obhHgTVBsJrSsthWpFLyH3McpflNP011kTZOemoILnLrE9QApRALjDdM8a7CP-3rqJBO3jNnbHjA-6UiW8Rt9_3Cs7KlCjcxH-d51zxm4agigCSUUtWdGdA9I6frdxQp0kAGYTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مردم عراق در اعتراض به لغو پروازهای ایران در بغداد و بصره تجمع کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/akhbarefori/693181" target="_blank">📅 17:17 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693179">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
عضو کمیسیون امنیت ملی: کشورهای محدودکننده پروازهای ایران متقابلاً متضرر می‌شوند
محمدرضا محسنی ثانی، عضو کمیسیون امنیت ملی مجلس در
#گفتگو
با خبرفوری:
🔹
آمریکا تاکنون از روش‌های مختلف برای اعمال فشار بر ایران استفاده کرده و محدودیت پروازهای ایرانی نیز در ادامه همین اقدامات است و با این حال این فشارها نتیجه مدنظر آن‌ها را نخواهد داشت.
🔹
اگر امکان برقراری پل هوایی با ایران از بین برود، کشورهایی که در این محدودیت‌ها همراهی می‌کنند نیز از کاهش رفت‌وآمد و تبعات اقتصادی و گردشگری آن متضرر خواهند شد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/akhbarefori/693179" target="_blank">📅 16:59 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693177">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cfb3b9c81.mp4?token=B8XSGuBDsj8cCNczT0MO-prCARN7txQHDVRi7szSt8FTnu9P3mWX5sGq8chyaAIEaMc2Y8q08bimH7yvC3PngJ-4JaaXwKNFDxGOzPpjvnHeCtWO9EIIIoAWdzVl4Kqy1EPdchMZtaXS2zlrgho5nzgrAtE_lyjHdT8K6-0bQCl5dCwJ7mkkrkhGjbnhBmJ6Qb9va4dD3_J1x5uLwc7YeVXByBuOxGRsRwnFPgXsICCbkAntb9my-3IlmaEe8wSemlFKRJLfNsEVF96cgEuvgMHt26zEYTrwmaWEkU1XgSQ3T-IMqDBwjIPuK7WCL8Ji8jgA4wzg-IYk0Z_gwOIuRCnbYEkS-5sUoFt4LZl8bSVKJC8BS-_9iL9CqD1oquUHSt-VAm8XX8v5k9lvrzdwCcGLiIbYJBD8n5t0Y3xkaMiPN2yGllfk_rXgYk--J3M7LsTD1QG8dvqQPkny57jCs-3lzHLoU7fiuTMBf4PuoY2oRAMWBjfhrbG3xKf5BSbpAbbMN59PsGKDG05aPq4tqrz21gaazsoHHvXlssiGHjxyn9anreiV0DFmc4NsQzQhSjgTRM5_g5RoKosOnuSa1lHz52i2XjAhvFKQ6ASlg72uSb1aREbBcgwnu6Z6k6-PTNEsaf97fxJoTaNP6mVEZDJxhpH1fYexF5PeisJrFDs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cfb3b9c81.mp4?token=B8XSGuBDsj8cCNczT0MO-prCARN7txQHDVRi7szSt8FTnu9P3mWX5sGq8chyaAIEaMc2Y8q08bimH7yvC3PngJ-4JaaXwKNFDxGOzPpjvnHeCtWO9EIIIoAWdzVl4Kqy1EPdchMZtaXS2zlrgho5nzgrAtE_lyjHdT8K6-0bQCl5dCwJ7mkkrkhGjbnhBmJ6Qb9va4dD3_J1x5uLwc7YeVXByBuOxGRsRwnFPgXsICCbkAntb9my-3IlmaEe8wSemlFKRJLfNsEVF96cgEuvgMHt26zEYTrwmaWEkU1XgSQ3T-IMqDBwjIPuK7WCL8Ji8jgA4wzg-IYk0Z_gwOIuRCnbYEkS-5sUoFt4LZl8bSVKJC8BS-_9iL9CqD1oquUHSt-VAm8XX8v5k9lvrzdwCcGLiIbYJBD8n5t0Y3xkaMiPN2yGllfk_rXgYk--J3M7LsTD1QG8dvqQPkny57jCs-3lzHLoU7fiuTMBf4PuoY2oRAMWBjfhrbG3xKf5BSbpAbbMN59PsGKDG05aPq4tqrz21gaazsoHHvXlssiGHjxyn9anreiV0DFmc4NsQzQhSjgTRM5_g5RoKosOnuSa1lHz52i2XjAhvFKQ6ASlg72uSb1aREbBcgwnu6Z6k6-PTNEsaf97fxJoTaNP6mVEZDJxhpH1fYexF5PeisJrFDs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت سیده سارا دستوم:
ضدانقلاب القا کرد که زنان بی‌حجاب، لزوما ضدانقلاب هستند؛ اما شکست خوردند؛ من اگر برگردم باز هم از انقلاب اسلامی حمایت می‌کنم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/akhbarefori/693177" target="_blank">📅 16:53 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693176">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a38f22edfd.mp4?token=PKY6t8HMPrg_Fy00igwMj_RojSRmN34FMQShZL2GEoizdkDp6UMatWHJE31JilWc_G7Md8S_BuuRshAUV7_YRLOnVBwq0kCdvsufF0ssmZMzgE7NpdFO6GLXmZrLc35By0YzfxZrk2Q0z4r7F9cJnli4PTa48kaU2Vkjmy_J0wA1kYOLMW7zkvZ5VJGjGqgJP73UlWAZW5Y_w_8d6fsOXxOCdLt0zObI_HeI7CxyzDMnmCzfAOuy4U7AyxangBzssw2y740BAEg_YuEwVBZsmBh8vdW5jqb4ij3D83CBuwsxAiiLVyo06Fq-dYHODNjf5bhawLZeEjkNAnRUNVXWCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a38f22edfd.mp4?token=PKY6t8HMPrg_Fy00igwMj_RojSRmN34FMQShZL2GEoizdkDp6UMatWHJE31JilWc_G7Md8S_BuuRshAUV7_YRLOnVBwq0kCdvsufF0ssmZMzgE7NpdFO6GLXmZrLc35By0YzfxZrk2Q0z4r7F9cJnli4PTa48kaU2Vkjmy_J0wA1kYOLMW7zkvZ5VJGjGqgJP73UlWAZW5Y_w_8d6fsOXxOCdLt0zObI_HeI7CxyzDMnmCzfAOuy4U7AyxangBzssw2y740BAEg_YuEwVBZsmBh8vdW5jqb4ij3D83CBuwsxAiiLVyo06Fq-dYHODNjf5bhawLZeEjkNAnRUNVXWCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراض دانشجویان دانشگاه رازی کرمانشاه به غذای سلف این دانشگاه و تاخیر چند ساعته در تحویل آن
#اخبار_کرمانشاه
در فضای مجازی
👇
@akhbare_kermanshah</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/693176" target="_blank">📅 16:48 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693175">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ONw6WFJiaqvs4-so_fNkP1Jn_nhuGdQHT2MCDvopLwQwRwZRyxkSa-O276YRmDaZ8B6YDN67TbTpc2dH-9fqyMSbEjp2HJZalx2sQsTJXXbTKG-ExmWWzZL-FoIf_6GdOf1h1mmOiC0seH-DviLnVI66rdlgwToiIbWQwt06xgRawtHHMhQcHetXWsFFtMWd-Hd0y6e70-DBMi_zYmCpo254ns3yKaifRH1xq9peB_YsWBgoDDYbz165-XqHbhQJdAtbRuNHziRjcyb9rD3TamwgY4PlDKcqH2_HecnmavHK8GD4KfLhpYILn80mqeWlg4S52g56JOFjfsE0mL3J3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وال‌استریت ژورنال: آمریکا با بیش از ۵۰ کشور تماس گرفته تا تحریم‌ها علیه ایران را تشدید کنند
🔹
آمریکا به انها گفته یا با ما هستید یا علیه ما
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/693175" target="_blank">📅 16:46 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693174">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
تصاویر جدید از حملات با پهپادهای انتحاری به تجمع‌ها و تجهیزات متعلق به دشمن سعودی در چندین جبهه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/693174" target="_blank">📅 16:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693173">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
انیمیشن لگویی هیولایی که بر پایه دهه‌ها غارت جهان ساخته شده؛ اکنون به وحشیانه‌ترین حالت خود رسیده و به پایانش نزدیک می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/akhbarefori/693173" target="_blank">📅 16:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693171">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
تسنیم: عراقچی و هیئت همراه سه‌شنبه به تهران باز می‌گردند
🔹
هیچ هیئت فنی از ایران به نیویورک جهت انجام مذاکره با آمریکا سفر نکرده است و این مطالب صرفا خبرسازی رسانه‌ای است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/693171" target="_blank">📅 16:31 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693169">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LYoVqP0TgqQ2MYe-WnzINzlizoLVVJi0veZZ-fqfUNQzY9h6w6a2D6MW-uJFE5Fa0ymPoEvxhHz15ixoaDCAZoGoxK8hG-wJBuQoqI-Xry9NgrQ-9M_Rp6ZaL74455aM7UvD-B5AJQkX4n68h52avRZzZUvV7Hjc50-6Bbd-fuPfs1Zl8Y0VypXXWsZTeQHgl1xKS8araIaw3yEEc25ujN_vjCJAmmx8Oy9AIj-RrWjIf7QXW6p2l2_UAACr8jBUYZv4ajn6oRWeYIR3Pb6fUNi83ciYc_HAYJ79Sll08zt-t4WZlzohCf0-cxdIgUW_N2dfebRtX6_clo4gPzmAUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تفاوت تیتر اکونومیست
🔹
قبل جنگ با اشاره به ایران:
ایران چگونه پایان میپذیرد؟
🔹
اکنون بعد از جنگ:
آمریکا کی از منطقه میره
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/693169" target="_blank">📅 16:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693168">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
سعید آجرلو، عضو کمیته رسانه‌ای تیم مذاکره‌کننده: آمریکایی‌ها در ابتدا پیشنهادی برای توافق ۳ روزه روی میز گذاشتند که محتوای آن عمدتا از جنس اسلام‌آباد بود
🔹
اکنون ما آن پیشنهاد را اصلاح کردیم و شروط خود را به آن اضافه کردیم این جمع‌بندی در کمیته مذاکرات در شعام انجام شده؛
در پیشنهاد ایران، از موضوع لبنان تا پایان جنگ، معافیت نفتی و لغو تحریم‌های جدید و محاصره وجود دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/693168" target="_blank">📅 16:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693167">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YiWkMUjoHhQ5yNnYv4NC0ZJ96hiEgETiyUoMYag2wOddxD20DzbLa89QaVIuo-27SPonq66peB4hgmWgfHTLvzhtWzXyCGmxY0Ha5mmj7CQQv4yycxyoUVoFiC89JMDJ-2BsX9m5-I8zpxfjeR85es1S8keBZbqSrQl70WYhdEKnKjQUM11mbbDvIlgFWH0MFQ2fFSSGVMbQfzOQkodf7xMRo8dOZfWuGQcqNPDl6dRiN7RFxfmUyN3Qpw7smW3FGcKpqdYehET46cyuZqluCA7lARGscc7gun39ojIqIMsgZuuoqDVQE3UjaJtwHX1AMurJRATkU7UzL9u3iUIUhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اطلاعیه دبیرخانه شورای عالی امنیت ملی درباره برخی اخبار خلاف واقع در‌ موضوع حمل و نقل هوایی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/akhbarefori/693167" target="_blank">📅 16:22 · 04 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
