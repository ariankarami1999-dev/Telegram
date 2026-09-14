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
<img src="https://cdn4.telesco.pe/file/jUs1LVE8IrJ08hliFzORbwkUEW7yzJMtJ5DnHfnOhMJowumlQS_p9Uc4QxDNoCSXAuOkrjXFNP--C0H6keMTcpJExkCFOmxop1iNx8NR4zrfz39Wf8SQITGZk5QOyXmZ3agjfW-z5WkKly8stk9vAeodqgIyDXgjuuJC_Gyb3aZgQhPUHUMjZJPcBiFEIsRfHDtvFvU99cu-Z0aJ0X_hniGXxJxChUvWNQZ9hCVMb0GRqie8iBFUQHPfQb9K3EMSGyynsFFO5W3HWBOIU69AckEKi9GStCyYsqbFskAyLbynPV8WGQo7hD-_yRQLx-xsYcj1SQydfrt9QscliLtuQQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.18M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-23 11:50:28</div>
<hr>

<div class="tg-post" id="msg-689723">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ACrK97uVGx0fyctlyhE4WN_XThT2oY4ppnNHBHbmx3QBs14F3pbrzjPFgHALzR-Fs6OaG1lNi_XXsHoCklC_YI4KJjVwI_BgeOlBT7AT9O8WGWWnfoenDRULd4B1OuIOS-yQChYs-UqflOc4dCo7wGkjRBqLeElpk49uKKXQhn9VPmvrzK4utdC9RuSMHLb_uWBU63eIYRtUEciMuJL9paUikjialoiKy1XfNEhiH7xF8Ei1ywsO4wfnRAFA6YZ7_6mEN7ZV5wUDWUvlm5VKmur3RPozXXIwl6S34Wa608d4XDr5ECL_TWiACp5wlgXzdunCCFGVNJaTAjpwqkSP9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pyxHq4COUg9E4zYAG4_yauKTiTOgf89XjzFdJCXuhR9Ol8mzHkEpQkPlhKQmCngs8izf1D3p3uU6agAawXAkKK4zkknwZZxJi5k2E_o1EuZKaa-FFGPlnE-SfGerA01-RyrrLEMkLWm3KBT2Ai4CcBlAH-L4KFCnsciKLUruaeYK2OxyUEUza4BWU9NR8lAnQW4gd2XRZGtCsXy9HIswf-8fbbDaz1UlcUqRPCE8_6JSPrqV-a5_ub4kKSQyBhwTQRpaM7jdxPQTRiVtGOx76j6zSxvzMdhPioH9nrKQzPGm2OlFdYEXT_Hd9z9Z69N_jXEd_dSv28jP5u5mtR-AFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IqoyH630OUgnp5F1cSc9wFUF2CLOGOQvIFScBg15nYEdBs_BmvAfOajXn4eraOLdEPr_9F6TfFkmNPvFJo3BXPkpNv-fvoQ3vVjjRgsWpygaXtHa1eLHtVrG7rrmZgcL2Nw6SNpGo1ZGRTsINUWU6TcsT0EEozjG7kKIr4-VAI327bu1350ka3rqOnvvnxphB9ouN2o27M_reJYSFQD-DfmLVViNWWpSVJsK_sBRZax8TXaPMOicELNSX_-nRCUEx5H7InlOLbkHI0UcLUOqa2Xf7N3p_y1-vAhDPmSYxbL5GJAIg89KHJ3rhfJuWS88uRQMLB3IlLCvHu9mpBGOGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vnBumJiRVXhLapJnv0WJ0JXoVYy27M7OGXSOvdfAxk9GlmrpjCSmz1YW2570bhcl4AsSkHJQumptN_6ZxW08dXsgkajUJn6EGTHvEUKxdjtYC26F20aHLhQJeJ1sJPURDxexP6VuML2o5C_BT4QSApnU_vqp0Hh3uaSeZcjFA_6Rpc_lc0SnJeHFpEpgOD8ecGCAMdf1j4GBYp2ZYf1zBg99rOsKP6OAHTlPt77sbhSdXNb-19mfI7TyadkBojlmpx2ldf5Nui16rZxGKpxYe7x-Ko4ERW-agi2ZTArVlkEGbHbaLlRIuRIXQusXiJXrZWzLYlCWDAw5lTQEyuLr3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
وقتشه که برای صبحانه، پنیر برشته اصیل گیلانی که خیلی هم خوشمزست درست کنیم  مواد لازم:
🔹
کره: به میزان لازم
🔹
پنیر لیقوان، یا تبریزی یا سیاه‌مزگی: سه قاشق غذاخوری
🔹
زردچوبه: به مقدار لازم
🔹
شوید خشک: یک قاشق غذاخوری سرخالی
🔹
تخم مرغ: ۳ الی ۴ عدد #آشپزی
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 5 · <a href="https://t.me/akhbarefori/689723" target="_blank">📅 11:49 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689722">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
انتصاب مخبر به‌عنوان نماینده ایران در امور چین صحت ندارد
مسئول رسانه‌ای دفتر محمد مخبر:
🔹
انتصاب دکتر محمد مخبر مشاور و دستیار مقام معظم رهبری به عنوان نماینده ویژه جمهوری اسلامی ایران در امور چین صحت ندارد./ ایسنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/akhbarefori/689722" target="_blank">📅 11:43 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689721">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
یمن: به پایگاه هوایی ملک خالد عربستان حمله کردیم
سخنگوی نیروهای مسلح یمن:
🔹
با ده‌ها موشک و پهپاد، انبارهای هواپیما، رادارها، باندها و انبارهای مهمات را در پایگاه خمیس‌مشیط هدف قرار دادیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/akhbarefori/689721" target="_blank">📅 11:37 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689719">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
سپاه اصفهان: احتمال شنیده‌ شدن صدای انفجار کنترل‌شده در جنوب اصفهان تا ساعت ۱۴ امروز
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/akhbarefori/689719" target="_blank">📅 11:27 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689718">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e27a9a496c.mp4?token=n8ttmOrxdtsC_mhlgvjeMpgqhIBTmkhNZAct9-tR7zp7vTqL8W5jwRvG_0p2Ido1incexMs3JVBeMUv1eTVIh-TtaL5vv84k10XhecxQRccieF8L0VISaX8pk0eRiqMp06InvFvyPz1WV0SVxDDJ-FdlIxAJeRAsj0iFsMxwGIREUvzflZfqzVZJKaBFQp4LjRlg31XiW7tgFmJ2oY6YtFrSAR5YNZjWspVNj8mhRFEKtiQ3lwBsZp_ki14AO469KKAg5v6PouT8dTHwmrP51QAjKNHT5ol6y0EuYqZQXE_nmzv_cXDEZvhkkAb1m1aNlGtjIb6HyfGaIgSaVLeA-hvCDbt7uMYtaQ4xS7gMWPXwvc_KH1eZ4HcNXSy3-Yr5PB0iIKvOovf-rugTfbovXSBnZtewIiNjPxWR2E-JMX-1A10WH1afe8MZlmAl6j9COypo8PdsPAUH_Dks0jUdsgF4fU_X735M0HzqOtR1UUE9MvGEcbK6X2ErYWlvuCoicv6xmBzc9Sq8-5Mbue2T3eBYAd-R5l4Nqvxxh1rMwofuwgvMoTFbxCCyGe1KKE4smypnFlXlagjltO5BQ9kezJC1fqohKO7rZxkln1_o0xx3g3-aMjh2H0R0ziOjwVVA9hah90ChGR6RdwHahn2FXFH_3fEiYvlH3tsDjWG5SzY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e27a9a496c.mp4?token=n8ttmOrxdtsC_mhlgvjeMpgqhIBTmkhNZAct9-tR7zp7vTqL8W5jwRvG_0p2Ido1incexMs3JVBeMUv1eTVIh-TtaL5vv84k10XhecxQRccieF8L0VISaX8pk0eRiqMp06InvFvyPz1WV0SVxDDJ-FdlIxAJeRAsj0iFsMxwGIREUvzflZfqzVZJKaBFQp4LjRlg31XiW7tgFmJ2oY6YtFrSAR5YNZjWspVNj8mhRFEKtiQ3lwBsZp_ki14AO469KKAg5v6PouT8dTHwmrP51QAjKNHT5ol6y0EuYqZQXE_nmzv_cXDEZvhkkAb1m1aNlGtjIb6HyfGaIgSaVLeA-hvCDbt7uMYtaQ4xS7gMWPXwvc_KH1eZ4HcNXSy3-Yr5PB0iIKvOovf-rugTfbovXSBnZtewIiNjPxWR2E-JMX-1A10WH1afe8MZlmAl6j9COypo8PdsPAUH_Dks0jUdsgF4fU_X735M0HzqOtR1UUE9MvGEcbK6X2ErYWlvuCoicv6xmBzc9Sq8-5Mbue2T3eBYAd-R5l4Nqvxxh1rMwofuwgvMoTFbxCCyGe1KKE4smypnFlXlagjltO5BQ9kezJC1fqohKO7rZxkln1_o0xx3g3-aMjh2H0R0ziOjwVVA9hah90ChGR6RdwHahn2FXFH_3fEiYvlH3tsDjWG5SzY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقایی: عدم صدور روادید توسط اتریش نقض صریح تعهدات دولت میزبان است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/689718" target="_blank">📅 11:22 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689717">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/610f6a4bcc.mp4?token=I6IiM574psYegVkFQNLblus-MKRo4KaI4wysF49YMaRZ1jKaOodpFkgnuf-9Hqkv9eFEF7cQ1KdY0oaqu1dwVoF9txLad7Y66oIh6IhZVYzsXdDnlN-1iNF5RBlQydsuywZFheSSeU6lrFrSqPGHjnXXKPqbZd5yFoCX7XanEhEAMYePM65TXTeieJqJquvHMKxd0QIJZxISSW5dZ4boUqmioAW85p5DhwPr3GMk9epGNgMolujmg3DyzAZC77_PV1lz4XQdTIeTjeT-ULS_CVXgT6rDcZSRiZISFjyQZU2Ecw0SPe_kiiB9ooO71f1p8YBrhsXZgA2-LJOO3wbnow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/610f6a4bcc.mp4?token=I6IiM574psYegVkFQNLblus-MKRo4KaI4wysF49YMaRZ1jKaOodpFkgnuf-9Hqkv9eFEF7cQ1KdY0oaqu1dwVoF9txLad7Y66oIh6IhZVYzsXdDnlN-1iNF5RBlQydsuywZFheSSeU6lrFrSqPGHjnXXKPqbZd5yFoCX7XanEhEAMYePM65TXTeieJqJquvHMKxd0QIJZxISSW5dZ4boUqmioAW85p5DhwPr3GMk9epGNgMolujmg3DyzAZC77_PV1lz4XQdTIeTjeT-ULS_CVXgT6rDcZSRiZISFjyQZU2Ecw0SPe_kiiB9ooO71f1p8YBrhsXZgA2-LJOO3wbnow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقائی: زیردریایی توقیف نشده، غنیمت گرفته شده و غنیمت هم حلال است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/689717" target="_blank">📅 11:18 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689714">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfc9088d61.mp4?token=byWJ8gOvjVbJ6bBOk8aS4HWP9jsB4TpuVnukbd1zk1MB0TR1awy089M0gtcw_YV1RBajYzLpYvrspyoEqujiotEBQ1bUrrgjabHw9LO0JBHfvUZ2MurfCklmMz_jUmVQ7AFq9X-yXffHHychqk9zD3vI2mRFb4ceiMDJG71t1SeQzuSUQvsWo5gTA5mdxYgTCU4TF6kDOs1SJqLX93WQxa2hC4E7lqpseupHD81TityTSsRRGb41J8KsFem1eLfc0-EW0SjpNy0tRgIq0_RvWZ1jEzUYdg8RWqcYO2TTBaacO3fqoAZuobCv73qtzX98ly-AQhSIfXVVZvg1Y1W99w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfc9088d61.mp4?token=byWJ8gOvjVbJ6bBOk8aS4HWP9jsB4TpuVnukbd1zk1MB0TR1awy089M0gtcw_YV1RBajYzLpYvrspyoEqujiotEBQ1bUrrgjabHw9LO0JBHfvUZ2MurfCklmMz_jUmVQ7AFq9X-yXffHHychqk9zD3vI2mRFb4ceiMDJG71t1SeQzuSUQvsWo5gTA5mdxYgTCU4TF6kDOs1SJqLX93WQxa2hC4E7lqpseupHD81TityTSsRRGb41J8KsFem1eLfc0-EW0SjpNy0tRgIq0_RvWZ1jEzUYdg8RWqcYO2TTBaacO3fqoAZuobCv73qtzX98ly-AQhSIfXVVZvg1Y1W99w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقایی: گروسی طوری دربارهٔ تأسیسات کوه کلنگ صحبت می‌کند که انگار پروندهٔ محرمانه و جدیدی را کشف کرده!
🔹
۷ سال قبل هم مسئلهٔ بازرسی از کوه کلنگ مطرح شده بود و ما هرچقدر لازم بوده، به آژانس اطلاع‌ٰرسانی کرده‌ایم. این مکان حتی در معنای پادمانی «تأسیسات هسته‌ای» به‌حساب نمی‌آید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/689714" target="_blank">📅 11:12 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689713">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac8b20fea9.mp4?token=nUWhbeXmVpBML0d5H8wt223cio3WKJm0ctfWqeA7rrPvfV6IkmJpMVKkDXyqypraKfbp1NgPGpKyQcHIGDXYbL9wuZ7dme_xrxc58rfKU9yZRxN_xgB9qUmkt-FrlDuW1O-XYsmcSJGsMX1LK6WGzzqXOhLRauAlN9tD4pWh-khy-cwPw7iPIY_Fzn0ZNR6vjo6nJX2LY-md2FIISY0ixoqwXNKcHh_b4ASFHH5yMD6GJvZLKYnVtHS6NkbCxhh-m6BaSKUrBDYt5yseeix6kjlSULO0op0UJDgaPVxIaspmbux00JgoNH1rUWnCj7PsJoP2z7I3FDOKm5PG6VpAoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac8b20fea9.mp4?token=nUWhbeXmVpBML0d5H8wt223cio3WKJm0ctfWqeA7rrPvfV6IkmJpMVKkDXyqypraKfbp1NgPGpKyQcHIGDXYbL9wuZ7dme_xrxc58rfKU9yZRxN_xgB9qUmkt-FrlDuW1O-XYsmcSJGsMX1LK6WGzzqXOhLRauAlN9tD4pWh-khy-cwPw7iPIY_Fzn0ZNR6vjo6nJX2LY-md2FIISY0ixoqwXNKcHh_b4ASFHH5yMD6GJvZLKYnVtHS6NkbCxhh-m6BaSKUrBDYt5yseeix6kjlSULO0op0UJDgaPVxIaspmbux00JgoNH1rUWnCj7PsJoP2z7I3FDOKm5PG6VpAoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت امور خارجه: ایران هیچ مداخله‌ای در مباحث مرتبط با یمن ندارد/ یمنی‌ها خودشان برای خودشان تصمیم می‌گیرند
🔹
بقایی: دخالت ایران در این حملات به لوله‌های نفتی عربستان  را کاملا تکذیب می‌کنیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/689713" target="_blank">📅 11:11 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689712">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ukRnQLoNU8oe4OK8QAyjGDf9vmw1zI1QogpmZyKi-zJrttpB5jBP698pzBBvlAoBMgjSH8bGmLq3g0BTNFbpuD2YILbRfJ7-eeuZ_vyVFW0VwuH776gGdw3vy1JkgYd5KuNvtBUcE9yeFJmG3hz_9ob1N6BSYEWpgbBZ0imlqsYvf_OxPg28kbikvUPuZGyNJOc8i7OPIwIteRyKezVHlD8ECL6RefXJhv1t2uCLKqrLHTdj-ZX8KJAK2aXwQaup_TpJBhMMspKU0SxKZwLNu1mGjuKWJvEAozaqvrdKfg24IKcKdiME1Q7cXaCuL11ivU8xzEEoCay5Xc6nEXr93A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گام آخر برای احیای پل‌های محور بندرعباس - لار؛ پیشرفت ۹۳ درصدی بازسازی پل‌های کهورستان
🔹
مدیرکل راهداری و حمل‌ونقل جاده‌ای استان هرمزگان از پیشرفت ۹۳ درصدی عملیات بازسازی پل‌های کهورستان در مسیرهای رفت و برگشت محور بندرعباس - لار که در جریان حملات آمریکای جنایتکار آسیب دیده بودند، خبر داد.
🔹
عباس شرفی گفت: بازسازی این پل‌ها با بسیج ظرفیت‌های اجرایی و فعالیت بی‌وقفه ۱۴ اکیپ عملیاتی در حال انجام است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/689712" target="_blank">📅 11:10 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689711">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
کنترل ارتفاعات راهبردی باب المندب به دست انصارالله یمن افتاد
⁣
🔹
در ادامه پیشروی‌های منحصربه فرد نیروهای مسلح یمن، کنترل ارتفاعات مهم و راهبردی مشرف بر تنگه باب‌المندب به دست این نیروها افتاد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/689711" target="_blank">📅 11:02 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689710">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: عربستان درخواست کرد نشست عمان برگزار نشود/ انتظار می‌رفت کشورهای منطقه قدر این فرصت را می‌دانستند/ با دادن آدرس غلط مشکلات یمن حل نمی‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/689710" target="_blank">📅 11:00 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689709">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
بقائی: تبدیل مناطق غیرنظامی به میدان آزمایش سلاح، جنایت جنگی است  سخنگوی وزارت امور خارجه:
🔹
این اقدام، با هیچ معیار انسانی سازگار نیست؛ استفاده از چنین تسلیحاتی در مناطق غیرنظامی و هدف قرار دادن ورزشگاه، منازل مردم و مراکز آموزشی، مصداق روشن جنایت جنگی است.…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/689709" target="_blank">📅 10:59 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689708">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3819f38b38.mp4?token=NLj5sOtpinFAqdjDQYPBHkg23_RVoPftdFdfu-wEEfm1p5uMZNqmcXXYdz2_iqBVjbWDfFVZyTlAbr9WYRlkPF6XX9GC1ASlNfz3_gsslR06TUUV-5rztMdt3nhTQmW-MaXoqGbPdz1_NUdYOhYoGD3ptAX5AibU6tD73-o-PXHT_cTqs8b4-bK2XN-fCxuwzCc5vEgi9oiFUOYoYK_ymbrxo4P3f1RbEtg9anOHROvIZx-GseIGnjq081v5WKrrXa9SbsynFIos6cK9SxM5XQ97PaE-BJgsL2JJEboY1Ll_402OYrV1OrT2qZfu49eAZuj_q6_B5HihBHJ__iB13A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3819f38b38.mp4?token=NLj5sOtpinFAqdjDQYPBHkg23_RVoPftdFdfu-wEEfm1p5uMZNqmcXXYdz2_iqBVjbWDfFVZyTlAbr9WYRlkPF6XX9GC1ASlNfz3_gsslR06TUUV-5rztMdt3nhTQmW-MaXoqGbPdz1_NUdYOhYoGD3ptAX5AibU6tD73-o-PXHT_cTqs8b4-bK2XN-fCxuwzCc5vEgi9oiFUOYoYK_ymbrxo4P3f1RbEtg9anOHROvIZx-GseIGnjq081v5WKrrXa9SbsynFIos6cK9SxM5XQ97PaE-BJgsL2JJEboY1Ll_402OYrV1OrT2qZfu49eAZuj_q6_B5HihBHJ__iB13A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقائی: تبدیل مناطق غیرنظامی به میدان آزمایش سلاح، جنایت جنگی است
سخنگوی وزارت امور خارجه:
🔹
این اقدام، با هیچ معیار انسانی سازگار نیست؛ استفاده از چنین تسلیحاتی در مناطق غیرنظامی و هدف قرار دادن ورزشگاه، منازل مردم و مراکز آموزشی، مصداق روشن جنایت جنگی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/689708" target="_blank">📅 10:54 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689707">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/898b515771.mp4?token=A3TqmD57EKVgdj3ny8i4rjhX5zRD_CsnkdaaP-gKMI5b96VB_-MuYkWPCxA98CNu9h8sLlcb_1Qx24sSnrnHgah86OZqppM5-rduR_Wxm9L-CowUM5hD1KCh3oc8OgoEIS9ywkNMdnPqMD0kBWb2yl7rfE45gzccsmqduNPdQXr3C1ZM-OC8D93AKJzQoDBtME6JJWHSOi8DfVpZ4cgfXwQ8keVfgmAnLu4hceFEwcw-5Wnlbr6giC-dT3zJSWpRDpl2SZ9_Dmjun68n_5BMf7Cnnn3nwpWixsP-ybE600jUb5zVykOUtKqKXaIa1ORMOsb7snKxMRt-VW8Gv1tVoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/898b515771.mp4?token=A3TqmD57EKVgdj3ny8i4rjhX5zRD_CsnkdaaP-gKMI5b96VB_-MuYkWPCxA98CNu9h8sLlcb_1Qx24sSnrnHgah86OZqppM5-rduR_Wxm9L-CowUM5hD1KCh3oc8OgoEIS9ywkNMdnPqMD0kBWb2yl7rfE45gzccsmqduNPdQXr3C1ZM-OC8D93AKJzQoDBtME6JJWHSOi8DfVpZ4cgfXwQ8keVfgmAnLu4hceFEwcw-5Wnlbr6giC-dT3zJSWpRDpl2SZ9_Dmjun68n_5BMf7Cnnn3nwpWixsP-ybE600jUb5zVykOUtKqKXaIa1ORMOsb7snKxMRt-VW8Gv1tVoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت سخنگوی وزارت خارجه از رشادت مادری که پرستار ۳ جانباز نوجوان در لامرد است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/689707" target="_blank">📅 10:53 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689706">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
قیمت گازوئیل در آمریکا رسماً به رکورد ۶.۲۰ دلار در هر گالن افزایش یافت
🔹
نرخ گازوئیل طی ۹ ماه گذشته، ۷۸ درصد رشد کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/689706" target="_blank">📅 10:50 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689704">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CMp_N8EvdzWsICYlfqua9WScCanfzYu6R5GGGN5LskgBzDoAjjIwKprQ0LiEPxtJTBkNFCpKnZ7aCJubstN47j4xz3ZzeQmnzz58Yj4SIOF7qz-fQfVeiCn20upl5k99s9wIVHAQLHRL-NujtgnHXhwiUG4N8OKGg0YtvtLdZ7fr1WZjGkumMHc326xGVMhgg3MhWgYBBIL0R8_NC4gB8H6dqb4Q9-jdVjTULUekpjy_7Uro_EqQv9wbNwS1nHDq1tPOsuMnDduUxrafcKgi9boOuKNCj0qFlewVipYIoZ-CuneYP0HxD12mz9hBDLz91eUHURrsJJZaGa8DfvBf1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری بی‌نظیر از سقف کاخ هشت بهشت
😍
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/689704" target="_blank">📅 10:44 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689703">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
هشدار سردار رادان به اغتشاشگران: اگر‌ وطن‌فروشی به دعوت دشمن خواست ناامنی ایجاد کنه، همان برخوردی را خواهیم کرد که با دشمن می‌کنیم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/689703" target="_blank">📅 10:40 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689702">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jSYCNTDNSmtQDa_54E91vZ4mVU-Z5AXvfZ9Cktvxvwyv2GlAo6eztm0gMJONplkH5wE_cteRC5uVQEZy98MDeoXCTEJ7yzTeOacM_Elypc_WnVDYEKKe0lTpMVajBiNPshjqwJsbMKsuo2Ug8xBLlz9MYK3AVG1xwJg1hptXfztbApm--awSvX30BYPUxz-aZM3B3akf3iGIwD89xK4y4HHgvwMV4nLGZPnXpblmr1McJ9-cqjAMEdfypc3DEeNfNwBm4Uz_UstncZP5477ybux5dPeelEDvpZBux15JX1NMAnap74NhFJSRRHWoeMGVsZTilllMjVXUzPHHnoFbVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
تخفیف  50% ویژه هتل مشهد
گروه هتل‌های درویشی مشهد
🎁
هر ۴ شب اقامت = ۱ شب رایگان
🏊‍♂️
بزرگ‌ترین مجموعه آبی هتلی ایران
🏎️
🛥️
تور های سافاری/ یات‌سواری - رایگان
🕌
✈️
🚆
ترانسفر تمام‌وقت حرم، فرودگاه
🎮
🎱
گیم‌کلاب رایگان
📍
۴ دقیقه تا حرم
⏳
ظرفیت محدود
📞
05138080
🌐
darvishihotel.com</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/689702" target="_blank">📅 10:35 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689701">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
خسروپناه، دبیر شورای عالی انقلاب فرهنگی: قریب به اتفاق بانوانی که کشف حجاب کرده‌اند، هیچ لجاجتی با حاکمیت ندارند/ ۷۰ درصد مردم تلویزیون نگاه نمی‌کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/689701" target="_blank">📅 10:28 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689700">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4555af6a4a.mp4?token=nKe9le3PtJa9hKzl2usT9pWVkz1pFpjnheFFM_5m8FGZu8BVQNiEMCJl4Rk1qa33ljQ6kByDZKqsh8o4cBoTp35fvUHfM-M52w4qYznbtZgd7o1c9OBlFcr07TBjiOnemkH6YtSBUzo-ihc7sBQnRm_1VlA0BS02rAuO-2C-1DFBWautyAynaTTFUcjQxRuztcrOgxskxNXJW2p05A9AWM3p1vEXooMLzIPLWYaqdlWVqLKpTPSBSkmhoIz3t96bw2U05vqYD3PlIK7tOFCNKfmO17mXG_vjOlxG2BzCfVhbDM5mITY-WzrPrhhM88je8tjR4qPxX61zHG0lO_9BOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4555af6a4a.mp4?token=nKe9le3PtJa9hKzl2usT9pWVkz1pFpjnheFFM_5m8FGZu8BVQNiEMCJl4Rk1qa33ljQ6kByDZKqsh8o4cBoTp35fvUHfM-M52w4qYznbtZgd7o1c9OBlFcr07TBjiOnemkH6YtSBUzo-ihc7sBQnRm_1VlA0BS02rAuO-2C-1DFBWautyAynaTTFUcjQxRuztcrOgxskxNXJW2p05A9AWM3p1vEXooMLzIPLWYaqdlWVqLKpTPSBSkmhoIz3t96bw2U05vqYD3PlIK7tOFCNKfmO17mXG_vjOlxG2BzCfVhbDM5mITY-WzrPrhhM88je8tjR4qPxX61zHG0lO_9BOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترافیک دریایی آمستردام از نمایی متفاوت؛ خیابانی شلوغ که روی آب جریان دارد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/689700" target="_blank">📅 10:24 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689699">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
مایکروسافت هوش مصنوعی Grok را به word، اکسل و پاورپوینت آورد
🔹
کاربران سازمانی برای دسترسی به این ابزار باید تأییدیه مدیران IT شرکت خود را دریافت کنند؛ چرا که بخشی از داده‌های گراک در سرورهای خارجی پردازش می‌شود. این قابلیت در دوره پیش‌نمایش فعلی برای مشترکان مستقر در کشورهای اروپایی و بریتانیا در دسترس نیست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/689699" target="_blank">📅 10:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689698">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ly5HgTpynenwAPzphF-m0O64LQhMuPahVuU7ed5v6-vAWmyX6HXqJ8N2A23_KeUdIppQ0_R8vvxd3KiLYHp9z0ETsEfKiRLDm1CC6Fyx6jyGDOX9TL33XJPNcPT3Q_vgBt0TLK414cXeS18EB8TzQ9pWjQzePl92sp20hk0EqsuFZlyLpxk42u5joA9Zww_qApreYGpyE_Ym_L4eob9ZWeM-rmvAq_hsLrn0n-mvBmcz5K0YEhC8vnrF1it7epy9tfMvlB-aFp3jL9ecKMFB2ngNfS-LXmxlt-yOO4w5Ojny9H3xqMG5_P0rHBpWS0_O8FR2ZhjVmhYgE8JKS1AeUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چرا آمریکا پس از ماه‌ها، الان تصمیم گرفته ویدیوی نجات خلبان آمریکایی را منتشر کند؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/689698" target="_blank">📅 10:11 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689694">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/519699c391.mp4?token=Y-Ozv1aCyxdt8COFeIWqvS5Azr0iJOir7EvMyRLGmhx8M5JRrvqch124pzPiCXos2oDC03ls9t4oevMSoSuJcX9OLC5_OX3s3NnfbwdFRv3x3hyr8WOvs-WKYcFahU86ixLxOxmOmUPuP23KoKZg3UJef5o2oeqwSsnd9CGyFOs1MUPTVGt3jCyzIZnX1mOsnuvnZyw-05B1OTyDocRpZkkBuSjrfdEVovO-eahth7FdH0vrbwLnzREZ_CU_nRg4RvxzPgFVDEibhX6F5ScLz8L2BuCDFFyuWK_RX8BgN_NJldT0uJ2Zk2L5Hrnwmtr5nyfrAxtpDTIV5olL6b4P-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/519699c391.mp4?token=Y-Ozv1aCyxdt8COFeIWqvS5Azr0iJOir7EvMyRLGmhx8M5JRrvqch124pzPiCXos2oDC03ls9t4oevMSoSuJcX9OLC5_OX3s3NnfbwdFRv3x3hyr8WOvs-WKYcFahU86ixLxOxmOmUPuP23KoKZg3UJef5o2oeqwSsnd9CGyFOs1MUPTVGt3jCyzIZnX1mOsnuvnZyw-05B1OTyDocRpZkkBuSjrfdEVovO-eahth7FdH0vrbwLnzREZ_CU_nRg4RvxzPgFVDEibhX6F5ScLz8L2BuCDFFyuWK_RX8BgN_NJldT0uJ2Zk2L5Hrnwmtr5nyfrAxtpDTIV5olL6b4P-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای از خسارات وارده به عربستان در پی حملات ارتش یمن
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/689694" target="_blank">📅 10:08 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689692">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخیرینه</strong></div>
<div class="tg-text">🔴
مشارکت در تأمین آب آشامیدنی مدافعان وطن جنوب کشور
#ویدیوی_بالارو_حتما_ببینید
👆
​
📌
در پی حمله ناجوانمردانه آمریکا به تأسیسات آب‌شیرین‌کن هرمزگان، روند تأمین آب آشامیدنی در این منطقه با اختلال مواجه شده است. برای پشتیبانی از نیروهای مدافع وطن، با هر مبلغی که در توان دارید در این پویش حیاتی مشارکت کنید.
​
👈
حساب رسمی گروه جهادی خیرینه:
💳
5892107050077463
💳
100150050398011502323560
​
👈
مشارکت سریع از طریق سایت:
🔗
https://kheyrine.ir/product/38001
​(خیرینه کلیه مبالغ جمع شده را مطابق شرایط
مندرج در بیوی کانال زیر هزینه خواهد کرد.)
🆔
@kheyrine_ir</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/689692" target="_blank">📅 10:02 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689691">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">خبرفوری
pinned «
‼️
خبرفوری/روابط عمومی سپاه پاسداران: یک فروند پهپاد MQ-1 بر فراز آسمان تنگه هرمز توسط سامانه پدافند هوایی سپاه رهگیری و منهدم شد
🇮🇷
✊
@AkhbareFori | Link
»</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/689691" target="_blank">📅 10:00 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689689">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7cfef22b9.mp4?token=gjvB12y2-SRM8mJV8Nv087x6qhezP-c6fo0narB3vEJnKZNzLWrazKrLpqbBmawcYbHHkdXT3UxbDDv_CiOKw2ITPjuVtsCJjlv1hiJrTe4LiA3-DqR148r8ijb1WRN9aGyUz2mWGqylKaqsqVYmVjewFARbB17vzVjy1J8ElUbtHCxz6sooSOUbAkLWFpNJ6gKsb06ztBJtuc71ErL4JCNL69Jrm0ht8ZE97B2Efs1fcuNn-FNc1Rp9Pa6RLBMAe_NRB_S1omT9mXMnqCZYFA7zUNSdhv_-2J7ZKqaRvSWD713pIFf9Zg0fpA2e-fkmumch0cQE7zPz9EtbV3Y9BA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7cfef22b9.mp4?token=gjvB12y2-SRM8mJV8Nv087x6qhezP-c6fo0narB3vEJnKZNzLWrazKrLpqbBmawcYbHHkdXT3UxbDDv_CiOKw2ITPjuVtsCJjlv1hiJrTe4LiA3-DqR148r8ijb1WRN9aGyUz2mWGqylKaqsqVYmVjewFARbB17vzVjy1J8ElUbtHCxz6sooSOUbAkLWFpNJ6gKsb06ztBJtuc71ErL4JCNL69Jrm0ht8ZE97B2Efs1fcuNn-FNc1Rp9Pa6RLBMAe_NRB_S1omT9mXMnqCZYFA7zUNSdhv_-2J7ZKqaRvSWD713pIFf9Zg0fpA2e-fkmumch0cQE7zPz9EtbV3Y9BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شکستن گردو هم فوت‌وفن داره؛ این وسیله ساده کار رو راحت‌تر می‌کنه!
✨
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/689689" target="_blank">📅 09:50 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689688">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
وزیر بهداشت: اگر تجربه جنگ ۸ ساله نبود، در خیلی از جاها مجبور می‌شدیم از صفر شروع کنیم/ تیم سلامت در جنگ ۱۲ روزه، ۱۰ میلیون لیتر سرم از قبل آماده کرده بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/689688" target="_blank">📅 09:45 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689687">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/321ed4de18.mp4?token=uTV4_c0IR-k_R0bCekY7HyqCcoB05jL1nWIkklKptNEqXOOmXm9bk_XEhnH0nrJtbeL0y1BfrX_SdPExGw-psBKSwDvyW7_x1dqADAarwqXcpQ79Fez18cgg7-7hiUbG4Gq6BRe3-r2QDLH06DR6tQjYV9tpZlQdfE9C32iXcugKlIx3gtN5n1SaVpCx8SvGC4Iw5wWTpTqIJ_q5DEh5pkP8KbbYYl4s1dGKIa-v_Oz2Lc4Ybes3CZuK6p0nLju7KupDnOhzycZh1VcTptcDqdNrORnBJF_rhRf-P1XAQK8IqE1Ilnu3lCJEXu05r9Bx83OXEtSoindgEVmvB8UC6WOPZMjWz5spnoYpVivuE-1upgRTS5ouwlCwiKAvD9uYiQALzpp2IiO9YygHrJOynF-hC0LhNc6o5D2YNvWaZ3EFlzRGifiSJnmUiu20UPp19lXdiV7mb92imJVFvY_jMAT3QY1RwIL0WZIOBI_mMwJIKm3-NH6bwsiybjQuy7Xzh6U7KqAFGlSsM9eb_EwiNGQLhRWR3aeX1lc2zabs8R2hvVqh8AcNThD2-hp7YcP_ZrFlHRl7LSwigQPJhh29Ht09upXo4CnhOEXMHWLA8Y-gqs3BkRlyitM5ARcKrwU3JSG9MFoxNHQlCc56fKAzvNFO2BaNF0pMx267lQpBLoE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/321ed4de18.mp4?token=uTV4_c0IR-k_R0bCekY7HyqCcoB05jL1nWIkklKptNEqXOOmXm9bk_XEhnH0nrJtbeL0y1BfrX_SdPExGw-psBKSwDvyW7_x1dqADAarwqXcpQ79Fez18cgg7-7hiUbG4Gq6BRe3-r2QDLH06DR6tQjYV9tpZlQdfE9C32iXcugKlIx3gtN5n1SaVpCx8SvGC4Iw5wWTpTqIJ_q5DEh5pkP8KbbYYl4s1dGKIa-v_Oz2Lc4Ybes3CZuK6p0nLju7KupDnOhzycZh1VcTptcDqdNrORnBJF_rhRf-P1XAQK8IqE1Ilnu3lCJEXu05r9Bx83OXEtSoindgEVmvB8UC6WOPZMjWz5spnoYpVivuE-1upgRTS5ouwlCwiKAvD9uYiQALzpp2IiO9YygHrJOynF-hC0LhNc6o5D2YNvWaZ3EFlzRGifiSJnmUiu20UPp19lXdiV7mb92imJVFvY_jMAT3QY1RwIL0WZIOBI_mMwJIKm3-NH6bwsiybjQuy7Xzh6U7KqAFGlSsM9eb_EwiNGQLhRWR3aeX1lc2zabs8R2hvVqh8AcNThD2-hp7YcP_ZrFlHRl7LSwigQPJhh29Ht09upXo4CnhOEXMHWLA8Y-gqs3BkRlyitM5ARcKrwU3JSG9MFoxNHQlCc56fKAzvNFO2BaNF0pMx267lQpBLoE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس شورای اطلاع‌رسانی دولت: هر کدام از بحران‌های اخیر کافی بود که نه یک دولت که یک نظام را سرنگون کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/689687" target="_blank">📅 09:42 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689685">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c9745d0e6.mp4?token=dIkWWqQSO069FBTUNqFpzcUxWy5WzzzDKdnLZfd6DyCHj2aU9sVuRj0DZ9XfJ7Noj9uw6PouGIBKHWrEoczXM20t3pNcFZlQ7Xqe8h7DKvit2dFKxij7TUorSAaQ9XlzC-jx9e5dSg6N6ih6FWL7RzsVamaVsFp7qQCWdpdFUBEDMnsHrGc4j3rP113AX12h8eHsr7YYEJj9-xSuemRDBmxy_ifCee1mDzNG_In-fa0EQ8p8ydu_t7pdFUbBLTe0j8spiual58agWRBYSXhprRM1HXpVYdLPqpOQQsZ5Jf_qO6bBTEv1mbpT4J8yuYQ5TDwDMOKTf4Z-hUaHXuP8sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c9745d0e6.mp4?token=dIkWWqQSO069FBTUNqFpzcUxWy5WzzzDKdnLZfd6DyCHj2aU9sVuRj0DZ9XfJ7Noj9uw6PouGIBKHWrEoczXM20t3pNcFZlQ7Xqe8h7DKvit2dFKxij7TUorSAaQ9XlzC-jx9e5dSg6N6ih6FWL7RzsVamaVsFp7qQCWdpdFUBEDMnsHrGc4j3rP113AX12h8eHsr7YYEJj9-xSuemRDBmxy_ifCee1mDzNG_In-fa0EQ8p8ydu_t7pdFUbBLTe0j8spiual58agWRBYSXhprRM1HXpVYdLPqpOQQsZ5Jf_qO6bBTEv1mbpT4J8yuYQ5TDwDMOKTf4Z-hUaHXuP8sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ماجرای اخاذی شبکه باج نیوز از خانواده فعالان اقتصادی چه بود؟
سردار رادان:
🔹
این شبکه با ارتباطات خارج از کشور فعالیت می‌کرد و مدیران صنایع و برخی خانواده‌های مسئولان، به‌ویژه افرادی را که در حوزه‌های اقتصادی فعالیت داشتند، هدف قرار می‌داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/689685" target="_blank">📅 09:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689683">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eed8f35f44.mp4?token=qG5sPbCay64DFl9WdNTZh0-NODbYx7LyESavUv6Azd7LqcP_Rs67litDdQIby9L2Qv_AyXn9Q3UPeDIcIxAIqewy4wzPcuOrANEBn74LwQh2Ilw8PHEWyLEWmLgrsPb2x1qL9mzG2PJPVHP783tVP_3JdxQTIe_8QRoq0pAt_MWx0R2Trhtje-QDmj46gyQ2Hnv6wysy0CJUxO5NBDs9sJdHuQQOhXsoCSUYKW1QAnELORvsbEqW5_3Ql-3T0QjNGeAfsCtJ8vj5OrAOzCPfpgj9hqvphl6WTqc4W7t5jydUuHxCGTuvgLaLqY-_20QXlbyFr358xzv97tSsvps73w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eed8f35f44.mp4?token=qG5sPbCay64DFl9WdNTZh0-NODbYx7LyESavUv6Azd7LqcP_Rs67litDdQIby9L2Qv_AyXn9Q3UPeDIcIxAIqewy4wzPcuOrANEBn74LwQh2Ilw8PHEWyLEWmLgrsPb2x1qL9mzG2PJPVHP783tVP_3JdxQTIe_8QRoq0pAt_MWx0R2Trhtje-QDmj46gyQ2Hnv6wysy0CJUxO5NBDs9sJdHuQQOhXsoCSUYKW1QAnELORvsbEqW5_3Ql-3T0QjNGeAfsCtJ8vj5OrAOzCPfpgj9hqvphl6WTqc4W7t5jydUuHxCGTuvgLaLqY-_20QXlbyFr358xzv97tSsvps73w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کلاژن طبیعی در یک ترکیب ساده؛ ژلاتین، چغندر و لیمو برای سلامت پوست و مفاصل
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/689683" target="_blank">📅 09:12 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689681">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‼️
خبرفوری/روابط عمومی سپاه پاسداران: یک فروند پهپاد MQ-1 بر فراز آسمان تنگه هرمز توسط سامانه پدافند هوایی سپاه رهگیری و منهدم شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/689681" target="_blank">📅 09:02 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689680">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
ویدیویی دیگر از انفجار در ارتفاعات علی‌الطاهر لبنان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/689680" target="_blank">📅 08:54 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689679">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f3033346a.mp4?token=dgcHqIvVK4gR0PwQHkuF2M1GWLd52LJ7nN_vkJT5Hjwb9A-WznM3Nr_WumWg3_xhEc0T6c1WMNv2nAqsPoNCtgQIr8wGVQMq0sOB8rm_OkxJ9Q2mIBjCj8jC33Gj3gwGR1-5YuYRuCQvBuQKkcOVsqRveG6oFaG5DDaaon3nk2xq1QSmu8o3d6izyTt28Q-OUs7QoI9zGLHIpPZ3Vk5Krg9iqpPha1phqYGBWzAMXdLckiOPGWVQ5WMlE0Zz4OGAKejRPeeqrulzvL8Hzs2m2K9g4kCyC0y2gQrO1YJFrK_rarjZYFGnat-CdB1Yzz8oRxQuXZdVC3rlopZv5MLXYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f3033346a.mp4?token=dgcHqIvVK4gR0PwQHkuF2M1GWLd52LJ7nN_vkJT5Hjwb9A-WznM3Nr_WumWg3_xhEc0T6c1WMNv2nAqsPoNCtgQIr8wGVQMq0sOB8rm_OkxJ9Q2mIBjCj8jC33Gj3gwGR1-5YuYRuCQvBuQKkcOVsqRveG6oFaG5DDaaon3nk2xq1QSmu8o3d6izyTt28Q-OUs7QoI9zGLHIpPZ3Vk5Krg9iqpPha1phqYGBWzAMXdLckiOPGWVQ5WMlE0Zz4OGAKejRPeeqrulzvL8Hzs2m2K9g4kCyC0y2gQrO1YJFrK_rarjZYFGnat-CdB1Yzz8oRxQuXZdVC3rlopZv5MLXYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خلبان آمریکایی: کل امیدم برای بقا این جمله بود: «هرگز اجازه ندهید کمبود انگیزه باعث شود که شما را در تلویزیون ایران ببینند»
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/689679" target="_blank">📅 08:51 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689678">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0461c566db.mp4?token=rZhQ7my6SOijgasW3T1AVxaSG-HvpL44pWKuMxkHwTMGkV5dx772h_Ba59o5qSXFsuh2FqDa94du0YCeMR7UN5c1QQd1uHFJifxiyjvEwFfI2l6NWnRQj1FlcGOHNheYl6clZNP6yya0pgGovyOVMKK7FkQ6KKkl8AqWWSZeN65QOdNSdg7hJO98RHFrKHZuVRm1USnpuYxDKIEj_JRdPfks9YY1uA9GI-J6Mug5QZqjPi4UYmrtl1ftJXyLK2FW0PEeoXFtELva4QGrWU1L6TNHkijyajE2ym5yYsNIQe8nDh4kJCQPISNC-aE3O7ENiVYlyukKPHf0Jt1IWf4hYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0461c566db.mp4?token=rZhQ7my6SOijgasW3T1AVxaSG-HvpL44pWKuMxkHwTMGkV5dx772h_Ba59o5qSXFsuh2FqDa94du0YCeMR7UN5c1QQd1uHFJifxiyjvEwFfI2l6NWnRQj1FlcGOHNheYl6clZNP6yya0pgGovyOVMKK7FkQ6KKkl8AqWWSZeN65QOdNSdg7hJO98RHFrKHZuVRm1USnpuYxDKIEj_JRdPfks9YY1uA9GI-J6Mug5QZqjPi4UYmrtl1ftJXyLK2FW0PEeoXFtELva4QGrWU1L6TNHkijyajE2ym5yYsNIQe8nDh4kJCQPISNC-aE3O7ENiVYlyukKPHf0Jt1IWf4hYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خلبان آمریکایی که در ایران نجات داده شد: چتر نجاتم در حمله اولیه آسیب دید و به طور کامل باز نشد
🔹
با سرعت ۱۶۰ کیلومتر در ساعت به زمین برخورد کردم و در این حادثه، ستون فقرات، بازو و شانه‌ام شکست. با وجود این جراحات، از دره‌ای که فرود آمده بودم، یک مسیر کوهستانی به طول ۲ هزار متر را طی کردم تا از دسترس دشمن دور بمانم و منتظر نجات بمانم.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/689678" target="_blank">📅 08:48 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689677">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
ادعای بلومبرگ: دولت ترامپ از ورود رئیس سازمان انرژی اتمی ایران به کنفرانس آژانس بین‌المللی انرژی اتمی در وین جلوگیری کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/689677" target="_blank">📅 08:44 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689676">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
ادعای خبرنگار الجزیره: نشست عمان به درخواست عربستان سعودی و در پی حملات به خطوط لوله به تعویق افتاد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/689676" target="_blank">📅 08:37 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689675">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
مرز تجاری شلمچه فردا دوشنبه بازگشایی می‌شود  استاندار خوزستان:
🔹
با پیگیری‌های انجام شده مرزهای شلمچه و چذابه امروز برای تردد مسافران بازگشایی شد.
🔹
رایزنی‌ها برای بازگشایی مرز تجاری چذابه هم با طرف عراقی در حال انجام است.  #اخبار_خوزستان در فضای مجازی
👇
…</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/689675" target="_blank">📅 08:30 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689674">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81bb0ded9a.mp4?token=uch1DEa-OaWY53rZVgTddFKHQLkRQxF_V9WYPzZMaU7ZzNUpGoWjxsNOssJU_18M3RI2C42K78NxkYpBgKeV2lg4QGagcR66F7KQaqgIbTOsye4kVqIk-tPTivbXbEpGv6HN4VbLG7EuNUva62RisdJPUUJE0CLWmrLDuI0gFmVKIZz7IzWrCnNemqW7sfDzj6acxmEupaolq-qaaqp5Vf6JVtHB-BXVAjoptSegYbHzEF4j1533RqVb8iwrnUzyY3nPwRumUMVqgYwk8YRuIlR3-nj2MQfmEHdFt4f_eiZzuTXqiUt8eWUA_EhWp-URgpSAn6b_JFeOfVtp7obxgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81bb0ded9a.mp4?token=uch1DEa-OaWY53rZVgTddFKHQLkRQxF_V9WYPzZMaU7ZzNUpGoWjxsNOssJU_18M3RI2C42K78NxkYpBgKeV2lg4QGagcR66F7KQaqgIbTOsye4kVqIk-tPTivbXbEpGv6HN4VbLG7EuNUva62RisdJPUUJE0CLWmrLDuI0gFmVKIZz7IzWrCnNemqW7sfDzj6acxmEupaolq-qaaqp5Vf6JVtHB-BXVAjoptSegYbHzEF4j1533RqVb8iwrnUzyY3nPwRumUMVqgYwk8YRuIlR3-nj2MQfmEHdFt4f_eiZzuTXqiUt8eWUA_EhWp-URgpSAn6b_JFeOfVtp7obxgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کابوس جنگی نتانیاهو
«حتی خواب هم برایت امن نیست
»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/689674" target="_blank">📅 08:25 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689673">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZY0WZi_B5ascR5k9hUo_WKGNUfiXrMnuUjIFF4a02wQ2hqRk9vke3YKIxQIgczOaD2GYPeshU6ZtnOea81NJigrJRTFEMYdJCqtF2bs1IzX0XWgWnwuI32or6btMQHQNSlOxsIndxPNwIKiKbJi9Qb0o7JLyB-BKCUMW0L_UaC675aGKeT7k_NxobudAU2n8xkbGPORUJSq8ak342nXXrBUD2rBa6g2jqqRBHXBuq6iBaWJyX-UHeWQCPXyIUTkJo0xnVKMfEybFSjOx2sJrfOHV3RnC8n6mRJSJJwmYQH_oEKKq_X0Y_5kmSsmBl07nNVHtuJp6f_BOOLMsAu4z0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایلان ماسک: هوش مصنوعی خطرناک‌تر از سلاح هسته‌ای
🔹
ایلان ماسک بار دیگر درباره خطرات هوش مصنوعی هشدار داد و یادآور شد که ۱۲ سال پیش نیز نسبت به خطرناک‌تر بودن این فناوری از سلاح‌های هسته‌ای هشدار داده بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/689673" target="_blank">📅 08:20 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689672">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
مرکز رسانه قوه‌قضائیه: ۲۴۰ مورد از اموال وطن‌فروشان و خائنین به کشور با دستور قضایی توقیف و ۱۸۲ حساب بانکی متعلق به این افراد نیز مسدود شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/689672" target="_blank">📅 08:17 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689671">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb5658727e.mp4?token=MLP56RSSlfImulf0BxW3ayt3dam99FUaUqRJKLYcdHeyAbhAfEyP4E8GAkmYagg753FrbaUBMRXmDtf5bRHyHs462nPM6Id3aCeDqBkt1FymrGSOJ7FiTxIyNCXUmD4pv3IWuxWA16urW8AU71Sn41uLGrFnSOIxPv7DccKq5VpYEbWBrA4RKv6CII2xC8xRkQQNLFFTNM1Sqf2NdpR9jSEFfnaD-x6b_iuOH_7tdDQiIsgSyI2HLFvsfgXg9SO8jFNaJ-6xzyvqgNvfPAmy54r4WiVqHFPVVSBY9KNMDW6uSZ3LGYNtj0ibwXvzf6lkepreaQznn2XU-O3_FcfCNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb5658727e.mp4?token=MLP56RSSlfImulf0BxW3ayt3dam99FUaUqRJKLYcdHeyAbhAfEyP4E8GAkmYagg753FrbaUBMRXmDtf5bRHyHs462nPM6Id3aCeDqBkt1FymrGSOJ7FiTxIyNCXUmD4pv3IWuxWA16urW8AU71Sn41uLGrFnSOIxPv7DccKq5VpYEbWBrA4RKv6CII2xC8xRkQQNLFFTNM1Sqf2NdpR9jSEFfnaD-x6b_iuOH_7tdDQiIsgSyI2HLFvsfgXg9SO8jFNaJ-6xzyvqgNvfPAmy54r4WiVqHFPVVSBY9KNMDW6uSZ3LGYNtj0ibwXvzf6lkepreaQznn2XU-O3_FcfCNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هشدار سردار رادان به اغتشاشگران: اگر‌ وطن‌فروشی به دعوت دشمن خواست ناامنی ایجاد کنه، همان برخوردی را خواهیم کرد که با دشمن می‌کنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/689671" target="_blank">📅 08:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689670">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eWPaRVswjYU-2dfdQfL1X4tAMtNf55pbWZgFO3GUDVYcWaQmpQbGPFuxqLejA-e7RCU4mOWewpnBsbeTp8ptWonsAJPiG-CabaNLHKLvZ96FIEt4zJCK6kJVDe6djnBfNW9C9wW4x_-EaZBnst-Z1QN6Ab8iycDYRnkg5LNyh9I296eCjF4FD8xYZABx_dbQAYyZNqGAS9Ik5TvgB0UJ3TpePF1g4IDa-u6yhxFwWvxAQecC9EhgP6iDTiJOfghNexn9K5go83v4GgLNYl25_y9HOezxd9BNUno0xEJH1-QbwBtwFOgRBO7LwzWkxaaYoeRF2cQgG-3revZza3q9TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نفت
برنت به ۱۰۸ دلار رسید
🔹
قیمت نفت در آغاز معاملات هفته حدود ۳ درصد افزایش یافت و بهای نفت برنت با عبور از ۱۰۷ دلار، به ۱۰۸ دلار در هر بشکه رسید. نفت آمریکا نیز از ۱۰۲ دلار در هر بشکه فراتر رفت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/689670" target="_blank">📅 08:11 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689669">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d782a95eaf.mp4?token=Qeq060c4vEcT9ETDBNYr-wMFqKh9M55YW1mCKOTSpJsCgw8T5rJEhbQcOHniaMQgH5A0rDocznXPRy6y-viHmGvvqMC6qF49Nisp-u4CPf2jhGo_wmVgeARZcPj38kS1loPviZsK62e4fQldqCb5cn-iw4LoGUxqwWz3Cblcn8oQK6coGHKCSVPu2B47bnV4poCTTWrTBR-Gy-D4JBN4r60a1AWUhlpOTSYE7IayJHA_EcySPyyYBgyoOLXK-4MzfZ8G48nuyBM79A-lo0eLZlDYnh0U_nNTZm88VHGhrdx1f3tjMI1tlzsxSm4zqyMF3TtYeuy1hJtWvQHmckiCfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d782a95eaf.mp4?token=Qeq060c4vEcT9ETDBNYr-wMFqKh9M55YW1mCKOTSpJsCgw8T5rJEhbQcOHniaMQgH5A0rDocznXPRy6y-viHmGvvqMC6qF49Nisp-u4CPf2jhGo_wmVgeARZcPj38kS1loPviZsK62e4fQldqCb5cn-iw4LoGUxqwWz3Cblcn8oQK6coGHKCSVPu2B47bnV4poCTTWrTBR-Gy-D4JBN4r60a1AWUhlpOTSYE7IayJHA_EcySPyyYBgyoOLXK-4MzfZ8G48nuyBM79A-lo0eLZlDYnh0U_nNTZm88VHGhrdx1f3tjMI1tlzsxSm4zqyMF3TtYeuy1hJtWvQHmckiCfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی شنیدی جنگنده آمریکایی داخل ایران سقوط کرده، چی به ذهنت رسید؟
🔹
هگست، وزیر جنگ آمریکا: اولین فکری که به ذهنم رسید این بود: "شت."
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/689669" target="_blank">📅 08:09 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689668">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3845db1fee.mp4?token=gADhivIQtd5vNlWOxEpnb9Nk7Gi-WLUgCWegrVqQrskcmqiKwDVMUVkjBtH8SunqvO5_NSyPjdYrFen-O1YmSxtRnocUuRMOb5cgqz3JPnEBvscf3K7tr_jAVW3l5gLyg4qzBfYAyHDpQ6v1yp9NylzEE-WlBMivnrL8PCIDpL-gDKBGEmmL9bq_6U7g30E4kEWhBT0ncK3iHSYnF53L6RMo9VTc24vlgeT6UHaV-iEdwjzrc6TxKYp1jb9wzDBAL1Crtj8oUNzXs_VxYm3_1b-256f9mcOv17DrSZSjNX5AwScLPUI85t9nDgS2TWzn-eR7aN5FVZhiue71zaZCvgppKsrHbE8K-VL9lr6XsG02kKPqZR8HyvbU-gma4SRiwpSLmbfbZHA8cEz5SYsY1VQEKJJUCD4pOwDkITyevCc6D70Jcnyg1hTanZ8_TbBV5v1o4ZARkWLZ1Y_7nkgIEXQGaMbaMxYLzl20LO4qbM2Yk0g7Q_ngKYMK4oEVFkmT3W25vtvI-2KHbsiK3gBV6dC7dFpZcHju9kmv2jxOU8cXBpkOLWZwUHWEl_yZxZLQQyn_u3wMfjmTIN5h-b47jc-VoTHZqvfArNd5Xn7EgwSWSSFi5xtusMjkB8oft1erhfiG-1DupSGJuY-cPczEOdaVEBuUTEfba_EVBcvFckI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3845db1fee.mp4?token=gADhivIQtd5vNlWOxEpnb9Nk7Gi-WLUgCWegrVqQrskcmqiKwDVMUVkjBtH8SunqvO5_NSyPjdYrFen-O1YmSxtRnocUuRMOb5cgqz3JPnEBvscf3K7tr_jAVW3l5gLyg4qzBfYAyHDpQ6v1yp9NylzEE-WlBMivnrL8PCIDpL-gDKBGEmmL9bq_6U7g30E4kEWhBT0ncK3iHSYnF53L6RMo9VTc24vlgeT6UHaV-iEdwjzrc6TxKYp1jb9wzDBAL1Crtj8oUNzXs_VxYm3_1b-256f9mcOv17DrSZSjNX5AwScLPUI85t9nDgS2TWzn-eR7aN5FVZhiue71zaZCvgppKsrHbE8K-VL9lr6XsG02kKPqZR8HyvbU-gma4SRiwpSLmbfbZHA8cEz5SYsY1VQEKJJUCD4pOwDkITyevCc6D70Jcnyg1hTanZ8_TbBV5v1o4ZARkWLZ1Y_7nkgIEXQGaMbaMxYLzl20LO4qbM2Yk0g7Q_ngKYMK4oEVFkmT3W25vtvI-2KHbsiK3gBV6dC7dFpZcHju9kmv2jxOU8cXBpkOLWZwUHWEl_yZxZLQQyn_u3wMfjmTIN5h-b47jc-VoTHZqvfArNd5Xn7EgwSWSSFi5xtusMjkB8oft1erhfiG-1DupSGJuY-cPczEOdaVEBuUTEfba_EVBcvFckI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اولین
فیلمی که ادعا می‌شود مربوط به عملیات نجات خلبان F-15 سرنگون‌ شده آمریکا در ایران است
🔹
این تصاویر برای نخستین‌بار لحظات عملیات نجات خلبان پس از سقوط جنگنده آمریکایی در خاک ایران را نشان می‌دهد.
🔹
در این گزارش ادعا شد که خلبان آمریکایی با استفاده از فناوری مخصوص سازمان سیا ردیابی شده است.
🔹
رئیس ستاد مشترک ارتش آمریکا توضیح داد که عمدا تصویر بالگرد عملیات نجات مات شده تا مشخص نشود چه بالگردی مورد استفاده قرار گرفته و این فناوری فعلا پنهان بماند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/689668" target="_blank">📅 08:04 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689667">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U5nRV0QeqxGo62brPush88uvB958oCDSoXUJRtb96E09x1XJWVs1JpUUIEdQ7ZKznP9kPcthvwLVZ6qCP-wKbPeUktg6j_k5Ktg-yD4RL1LjG4Sm4r_tiGE6Fod8BeEh5wSWYUJfPnSPEEOBWRJis8ilXI3DY3Mj7YxDEeEu8Ia6T9CbhQL9L8pn3VetlnVCg8ptCNqso0pftGC13b_PhQ3i2nBRmpgU1G_TSo-yowiDKvOC3gcSgH44IqOvQhXdXYdLHk04H1jqDK4M2oeHKXMR5wTDnK5OVVaGs0D9TVdKUlofW0AkHNYLx8qhCJ1Mm2GSBxdS6-Vgf2socWAg4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شبکه المسیره یمن: ۴ تن از فرماندهان مزدور سعودی در جریان درگیری‌ها با نیروهای مسلح یمن در منطقه «کهبوب» کشته و ۵ تن دیگر مجروح شدند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/689667" target="_blank">📅 08:03 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689666">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/529ad3180e.mp4?token=bXJbMcvF_-tuMqXRcu4rw4Use7eqT17BRvbVf43aG4pPIJ4UygJiTtzqOV2l4RvmLOItJ3FWltLrXzmvgTDpE8n-YmiJvTBmIuV77IBEUw28rXg3UI-rkWTS5HZW6MVaw4FQhAQUs-fDafAzsX9AbWhR6k6TvRxVtK-G4G0pyoWOnv1TH_Lg4CAIDMGvYcFm_rLKLsAXQFltwwqmejoX_uhMKZqcqII6rqQPOYWkS8e5QxDnkwCStH94NLLblX369KafxIUnV081nK5smDBGCGrPCynVplQHijDSE-7MLMu89EULgSpvkMi9RIen07F7Jqo7ucBs54gxC_XWoJLGjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/529ad3180e.mp4?token=bXJbMcvF_-tuMqXRcu4rw4Use7eqT17BRvbVf43aG4pPIJ4UygJiTtzqOV2l4RvmLOItJ3FWltLrXzmvgTDpE8n-YmiJvTBmIuV77IBEUw28rXg3UI-rkWTS5HZW6MVaw4FQhAQUs-fDafAzsX9AbWhR6k6TvRxVtK-G4G0pyoWOnv1TH_Lg4CAIDMGvYcFm_rLKLsAXQFltwwqmejoX_uhMKZqcqII6rqQPOYWkS8e5QxDnkwCStH94NLLblX369KafxIUnV081nK5smDBGCGrPCynVplQHijDSE-7MLMu89EULgSpvkMi9RIen07F7Jqo7ucBs54gxC_XWoJLGjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله موشکی به مقر تروریست‌های تجزیه‌طلب در سلیمانیه
🔹
منابع محلی از حمله موشکی به مقرهای گروهک‌های تروریست تجزیه‌طلب در استان سلیمانیه در شمال عراق خبر دادند.
🔹
بر اساس گزارش‌های منتشرشده، پس از این حمله، شعله‌های آتش و ستون‌های دود از محل استقرار این گروه‌ها به آسمان برخاسته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/689666" target="_blank">📅 08:02 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689665">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c6rycYxgqn33pOmrCOmbXJtbG0UuylLdrODJrxwwSfJGYiar0d9EMmAbpfbF5k0h-ET04OsDqzjQRf7b-5I97kwGmJkADYdFBF4lDNnPkKZ8pxxofqeRL0o8A4MWTYbiJAzuaaJc3NnxJR3Yyqtznvr9Knc-dDBm3u6BpA_9M2q4cM-TGOcLDZfa16O3DIzBosJ2UaZuUGjbgGbd6nLjYK3tbecb7MU_R1XP3S8mktn-WYp_HpV39eI8dJanz6JsmlUciBwUkqn1ldz2ToBhlXGWp4Ni8Q9YBTuG9ZJgXt3CRrwlDNMouusKRNA-9xPMnOTBnwzdHNrDdIlJRgzjbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز دوشنبه
۲۳ شهریور ماه
۲ ربیع‌الثانی ‌‌۱۴۴۸
۱۴ سپتامبر ۲۰۲۶
دوشنبه‌ها
#زیارت_عاشورا
بخوانیم
⬅️
متن و صوت زیارت عاشورا
@AkhbareFor</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/689665" target="_blank">📅 08:00 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689664">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SileJXiiY6WK8yjZ4_xbzOTJKA1aXZ3K_jg5M_4UmOEKiXOiI5-X7lSUn6D3GZZNBCEsHtJrm7xHvQHhbKfyBBY5h5y_3MdXUcByJuAGl9n7nOzyGsCuZBPLgL1NtJToiuvttxvnABRPVvrJgmeKfx00x5Qnzra5dMq9eHDyaoX_l1kNS9hbfI5idYfJbNqO_MmKCto6LtjzpvyQY97N7hbE8foq3CYyqQ3mV8p2jO7WDe2BS-t1rD3fo9bzQYtnlzIeT8jayKdn8PM-uMqFWRFTNvMcTg5UdBnMJ1FPWYdqiWuxLBoE6s5S4aajzhU3oQJfGM5S4METise93Ra2HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دنبال قرص و آمپول واسه قد بچت نرو .....
❌
چون همشون عوارض بلند مدت داره و آسیب ببینه
🤱
منم اولش باورم نشد تا اینکه بعد از یه
مدت کوتاه تاثیر فوق‌العاده‌ش رو دیدم
😱
اینجا فقط با
#تغذیه
و
#حرکات_کششی
قدش بلند میشه
💯
اگه میخوای بچه‌ت کوتاه‌ نمونه
🤷‍♂
حتماً یه سر بزن
🥰
👇🏻
https://t.me/+6UzhH-bMsNUxMWM0</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/akhbarefori/689664" target="_blank">📅 00:30 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689663">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromDigikala | دیجی‌کالا</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PPCmcLBHxLwiew8EgUBEVnKqYsV20xTI1BKi9lqMVi87_xygGYYBbdZAKKeC3iwGV0UH8jHEke5EahFbSJ2ldjI_dvz2o36O2EaGtfXE5qp2MDRSsiJysms0MIWVE6NbnOYT-VHSkSUng3RiZy18wMDOo04DszWQEEG_kfoxMlV3WPerWOO0IqU4pXYlAQ01dSMvFHlfafvxDAa4str4ApEaAwaqqx4BXcLpPU7t7ar2072LY5jX6vanfq21LPAmgwsQk1QsJq57kF1g0KoCc0zIQZaEC7TwYQLOVNWagn0iC_0F1Y4mjDaEri6toIaE-PGOGGGjbgBdLb5HCRp7tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرفروش‌های آرایشی و بهداشتی رو با تخفیف بیشتر بخر!
🛍️
✨
از ماسک مو و آبرسان تا شامپو و خمیردندان و البته کلی
محصول پرفروش
دیگه، همه‌رو به راحتی از
دیجی‌کالا
سفارش بده.
🧴
🪄
🎁
۱۰۰ هزار تومان تخفیف بیشتر
برای خریدهای بالای ۷۰۰ هزار تومان
کد تخفیف
:
HBTOT05
🛒
برای خرید، وارد دیجی‌کالا شو.</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/akhbarefori/689663" target="_blank">📅 00:30 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689662">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KOeFuIDRzPRxexs9L2UIs_xuI2MHkk7htqSaIybh9id8Bq18C-yLxysbbTZmE0RnfLJ3WpZ90WoE7yThZ8QgsgEqmq6cKyKUiw8vNxrUE4ZAbRb3VrWB3xelDPtwcbmx3Y1PYiH_H-HgaUTEkIu9zuG-ChqN-qbCwNKIybQU1oQtdsZbsV1YPYPgIP9OVTWr281qCp5P0oq2ixwCKXmdOSj2m538q_ItftZL0RLnDyldYKYOhqG7BKGSflc8ccnf2B6UAPcRG9IsajiftYXRUcNgXWBsDS4DHzNmrew61fRA-Q84gDO9__3JKYdZPMvzTErDGWotQtkXw2tqYCgxuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
ست اسپرت مردانه Motorsport
سوییشرت + شلوار، یه استایل کامل و شیک
👌
🖤
مشکی | فری‌سایز مناسب L و XL
✨
سبک، نرم و مناسب استفاده روزمره
💥
فقط 1,650,000 تومان
🚚
پرداخت درب منزل
🔄
ضمانت تعویض ۳ روزه
خرید از سایت
👇
https://memarket24.ir/product/brief/47547/180124/
مشاهده حراج آخر فصل
https://l.memarket.me/lp/15/180124</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/akhbarefori/689662" target="_blank">📅 00:30 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689661">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc23d5bdf0.mp4?token=Nq67jbS_zJ_uQg34yWRviwuUnMo5teJZL-si4q7W901eI01KkN3PqK2oosTwYoqBXbis0mFc9UxjfuIKe9PiPR7mZPD8V1on0fTfqeZeR-B49MVyUX6NHly2OlLR8KqEobAaj9BL-tfS0f7FOJGqsriTcFQs8bffDnzs8Z0KO93L9SnMV_JGJEsNMg7bvVHaUgdbItmIIPdVDCJdqKTX0BY0IR-n7VwvHs93HIIA4z8zR5YN2iL2wkUaxSc0Sneo8BKYYJvxMGXvAzveEszdAWzHWjXqQsbPrF0ICQ-XHe9R7MLEmqOKTaGZGf2X6Bn582XuQwO6KFf7OhNYzWTGAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc23d5bdf0.mp4?token=Nq67jbS_zJ_uQg34yWRviwuUnMo5teJZL-si4q7W901eI01KkN3PqK2oosTwYoqBXbis0mFc9UxjfuIKe9PiPR7mZPD8V1on0fTfqeZeR-B49MVyUX6NHly2OlLR8KqEobAaj9BL-tfS0f7FOJGqsriTcFQs8bffDnzs8Z0KO93L9SnMV_JGJEsNMg7bvVHaUgdbItmIIPdVDCJdqKTX0BY0IR-n7VwvHs93HIIA4z8zR5YN2iL2wkUaxSc0Sneo8BKYYJvxMGXvAzveEszdAWzHWjXqQsbPrF0ICQ-XHe9R7MLEmqOKTaGZGf2X6Bn582XuQwO6KFf7OhNYzWTGAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایران آخرین خط دفاعی در برابر اسرائیل برای محافظت از خاورمیانه است!
🔹
نظر یک تظاهر کننده انگلیسی زبان درباره ایران.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/akhbarefori/689661" target="_blank">📅 00:24 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689660">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-poll">
<h4>📊 به نظر شما مهم‌ترین عامل در افزایش موج مهاجرت پرستاران از کشور چیست؟</h4>
<ul>
<li>✓ حقوق و مزایای پایین</li>
<li>✓ اضافه‌کاری اجباری یا سنگین</li>
<li>✓ فرسودگی شغلی و فشار روانی</li>
<li>✓ احساس تبعیض در نظام درمان</li>
<li>✓ سایر موارد</li>
</ul>
</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/akhbarefori/689660" target="_blank">📅 00:21 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689659">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JMfQfO45BHqbJDidl8ghjb-201hX-CO4XbCvS4xLKHzUKXUMSH34TZzw_UZSJzkYufk4fYH6cpCpdjv1mfMNyz6Hr8RLWAEiEgOu_jrX1AoMzJSg6szQO_44_aCyX_s4aH4DXyTBIO_X2zxinRjjyy09k-bIH0reaSZCeZ_f5qAyMic2xO7xke0OZKlTB6nN1GMEkH6oE0STxdBCVEecXw7qIDbjPLJhfjEts_o1_DWiqkvTwqijFOLwRWHPFIL20ErxO5AEYzJvLJq-S58n6Zk_NtUVAcoPMGIOD0-dgQvJ3cTnzdUXN6EtRrNXRIE3u0RKcB7xUZrWoPOz-zJDow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رسانه‌های غربی: ایستگاه پمپاژ نفتی عربستان به طور کامل نابود شده و بازسازی اولیه تا چند سال غیر ممکن است
🔹
خط لوله شرق به غرب هم منهدم شده و عملا بارگیری جدید در ینبع فعلا نداریم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/akhbarefori/689659" target="_blank">📅 00:21 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689658">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔹
خبرهای داغ امروز را از دست ندهید
🔹
🔹
عمان نشست دستیابی به توافق درباره تنگه هرمز را به تعویق انداخت
👇
khabarfoori.com/fa/tiny/news-3245023
🔹
سوپر ال نینو در راه است/ آیا ایران هم وارد زمستانی متفاوت می‌شود؟
👇
khabarfoori.com/fa/tiny/news-3244880
🔹
رسوایی عجیب در بیمارستان | پخش فیلم منشوری برای بیماران
👇
khabarfoori.com/fa/tiny/news-3244709
🔹
تصویری از نتانیاهو زمانی که یک کماندو بود!
👇
khabarfoori.com/fa/tiny/news-3244982
🔹
لباس های جنجالی بازیگران زن ایرانی در جشنواره ونیز
👇
khabarfoori.com/fa/tiny/news-3245025
🔹
صفحه ویژه اخبار پربازدید وبسایت خبرفوری را اینجا کلیک کنید
🔹
khabarfoori.com/hottest-news</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/akhbarefori/689658" target="_blank">📅 00:20 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689657">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nOHIz7zzhghUuNtUUJT2FrSKjlk4i5MUfG5TyD5vjU134wBnj47GHSfnUoBrfyg8pTrwQWnthFZHEZu1qe71UwYzvz6REGBdaak1d62--9iEPWQ7xvY20OR9kcng9OsYUjpH4sYdM9gp76q9oJYseJ4zU1f0jlXw4lIAaiudRb7lujJNKdEyFvOpKvMpK67WF5lZnR18fMXWttvoJ4TOvRQRJ_WYl-GxAa9HLwUX-haV1-acMeSfDimJam4j-ThiFhaf_dFh39fzXPGwiS0FTcN7SHtnMWS0Oi58FStxx1Fy9kkCYaIf-xJn0uFDaM_ogsuw9-5jUaGaVUstKtlOYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اختلاف قیمت خودروهای ایران‌خودرو در بازار
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/akhbarefori/689657" target="_blank">📅 00:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689656">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b669554442.mp4?token=V5L64m3vHSvXA-AUvUsR9Y77cToOakT4pU2PTgIezSHQLXDAX7RDjKIWpl6XP4iaJNu_6nNmbrJAYO2dyIOyFZGAJBBePEJSDrJ8nkjFqwB2gjgkpyYem5UL78KjX-0O5JxUe23i3tVFsAqdAciveoqXzHzHuqg0eIIGWwuuq0wcWOT6i60RSvEiKVXVxcqcTidlpg6p3sMPF3U64huqAsnd9pmVKnf8kK-_jzdguSw6GZFJd1MRZkNpZEUKMgR2xI5Mu5vGdXzC39DPy88Lo-CoRymMkpttLljMnO6iRM7QXuMJLq3jQqag5rxT-EqHJN4YYUgKHx4_ThYtcsKu3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b669554442.mp4?token=V5L64m3vHSvXA-AUvUsR9Y77cToOakT4pU2PTgIezSHQLXDAX7RDjKIWpl6XP4iaJNu_6nNmbrJAYO2dyIOyFZGAJBBePEJSDrJ8nkjFqwB2gjgkpyYem5UL78KjX-0O5JxUe23i3tVFsAqdAciveoqXzHzHuqg0eIIGWwuuq0wcWOT6i60RSvEiKVXVxcqcTidlpg6p3sMPF3U64huqAsnd9pmVKnf8kK-_jzdguSw6GZFJd1MRZkNpZEUKMgR2xI5Mu5vGdXzC39DPy88Lo-CoRymMkpttLljMnO6iRM7QXuMJLq3jQqag5rxT-EqHJN4YYUgKHx4_ThYtcsKu3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دو شورت‌کاتی که قطعا بدردتون میخوره
👩‍💻
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/akhbarefori/689656" target="_blank">📅 00:08 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689655">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
‌مرزهای عراق باز شدند   نهاد اطلاع‌رسانی امنیتی عراق:
🔹
تردد مسافران و تجارت در مرزهای الشیب(چذابه)، شلمچه و مندلی(سومار) از ساعت ۶ امروز از سر گرفته شده است.
🔹
عراق به‌دلیل آنچه «ساماندهی اداری و امنیتی» توصیف شده بود، این مرزها را از روز جمعه به‌طور کامل…</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/akhbarefori/689655" target="_blank">📅 00:02 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689654">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T5FnbDsVVxm0B7mNCOBcx-t9PiGbKBOgv-O8i_9J8wBeK0NFkYP9Iz4UaYchTh3NebOlHpKnKfytBDn3eX2Rznpw3eeRFLmg6cKmCeW6Zk9jlrJtja7SQjA3U-fVvR1dznme1fcq9eK1qq1zWEEC4NaJZ1Ywhj3GfVbQJ5cUIyLXqwgzV5vdu4Ic0kkUYheBaXuWD3pxuMeWLw8bQn5fEebLUBPLa0_RD2pD9_zOPoObRwq8exzdY-7Z2mnMLoOeRY9ym1Ddgi9MyunXlcovtAHo8pH-oqxQJcK693iyUEjF3ITDG91UTt2MNjxJL4Rnl6tUTMAhRKQ60h6qFJsZyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/689654" target="_blank">📅 00:00 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689653">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d11df278bb.mp4?token=uIlu06b6cmmd-L_U57Go8ph4gvKQj1kTWT2MaXEr1L6HO4iNtvMQ-qgweruQNuKZkqyyR9YejcodkurgH6eI5MtWg2J5GPQTg3sRptVyHu5cflDcwTo3hL4b4SACSZFT-Uo_JY1HDOtqqX2UNDA1aBmbu704vYVnjvIdSOi1hFy163pxSmjbjbAFLy9yt6a7q9TNYeQ-BgiHZFdfiP4-_ndORGgs4_VekOA2nejRWK98VogrNgtdKU70-UNMfQA6Yw1zG_4PdiT-a7Gm4NSINc_ZAKPbx579j26-ike7kQ0jum8zJ1MTlNi7CHDEEJHNT8_w9R74FeazNB8dGAFPfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d11df278bb.mp4?token=uIlu06b6cmmd-L_U57Go8ph4gvKQj1kTWT2MaXEr1L6HO4iNtvMQ-qgweruQNuKZkqyyR9YejcodkurgH6eI5MtWg2J5GPQTg3sRptVyHu5cflDcwTo3hL4b4SACSZFT-Uo_JY1HDOtqqX2UNDA1aBmbu704vYVnjvIdSOi1hFy163pxSmjbjbAFLy9yt6a7q9TNYeQ-BgiHZFdfiP4-_ndORGgs4_VekOA2nejRWK98VogrNgtdKU70-UNMfQA6Yw1zG_4PdiT-a7Gm4NSINc_ZAKPbx579j26-ike7kQ0jum8zJ1MTlNi7CHDEEJHNT8_w9R74FeazNB8dGAFPfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای برد کوپر ،فرمانده سنتکام: من اصلا نگران کمبود مهمات نیستم زیرا چنین چیزی اصلا وجود ندارد
🔹
ما به خوبی تجهیز شده‌ایم و آماده‌ایم با هر شرایطی مقابله کنیم.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/akhbarefori/689653" target="_blank">📅 23:57 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689652">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
مدیرکل خلیج‌فارس وزارت خارجه: تعویق نشست تنگۀ هرمز به درخواست برخی کشورهای منطقه و تصمیم مشترک تهران و مسقط صورت گرفت
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/akhbarefori/689652" target="_blank">📅 23:55 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689651">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61885d885f.mp4?token=tcKggx1baBvODIESo453-VC-ziaLxQEvEVLchGzRVxXz8c4SJ2GEzesJ_PoretNokwTsXkoeZ-mkRflRJOoMm_dO_UOJHi05DjC2vGwewPlyd4jwq0hlFwnaZUKBjWd6IQ2n0bnsnNuO0HiagS_CUtvXxDO8w3ofPY3EcLjo8nW668IQFImup0tSJ3NLwII6kZtSLslgFb7xnyPBjgKFxNgkg3xarvVP5eOu1NHMFn2J3iSjhxEu058OB5UqcX-5K7txMdy8RNWu4kr6l73zhwsUY7Zb6MiXxoJE2TEyzt5f09XjbF-iN5LkQ61Zkbe-Sq9Wz_O3Md35ortOAY4C3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61885d885f.mp4?token=tcKggx1baBvODIESo453-VC-ziaLxQEvEVLchGzRVxXz8c4SJ2GEzesJ_PoretNokwTsXkoeZ-mkRflRJOoMm_dO_UOJHi05DjC2vGwewPlyd4jwq0hlFwnaZUKBjWd6IQ2n0bnsnNuO0HiagS_CUtvXxDO8w3ofPY3EcLjo8nW668IQFImup0tSJ3NLwII6kZtSLslgFb7xnyPBjgKFxNgkg3xarvVP5eOu1NHMFn2J3iSjhxEu058OB5UqcX-5K7txMdy8RNWu4kr6l73zhwsUY7Zb6MiXxoJE2TEyzt5f09XjbF-iN5LkQ61Zkbe-Sq9Wz_O3Md35ortOAY4C3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس سازمان میراث فرهنگی استان اصفهان اعلام کرد که در پی حرکت یک جوان بر روی پل سی و سه پل، خوشبختانه آسیبی به این سازه وارد نشده است
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/akhbarefori/689651" target="_blank">📅 23:44 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689650">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
گزارش منابع محلی از شنیده‌شدن صدای شلیک چند موشک از سیریک
🔹
تا این لحظه، هیچ یک از مبادی رسمی اطلاعات تکمیلی درباره ابعاد این رویداد منتشر نکرده‌اند./ دانشجو
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/akhbarefori/689650" target="_blank">📅 23:41 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689649">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
رسانه کره‌ای: بین هشدار ایران و فشار آمریکا گیر کرده‌ایم  رسانه جونگ‌آنگ کره جنوبی:
🔹
سئول در حال بررسی گزینه‌های خود است تا از عواقب جدی بین‌المللی جلوگیری کند و در عین حال دونالد ترامپ، رئیس جمهور ایالات متحده، را راضی نگه دارد.
🔹
کره بین دو راهی گیر افتاده…</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/akhbarefori/689649" target="_blank">📅 23:39 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689648">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CEAO3zS_gxiWMIDNiFp-bZXM8vtugK808zIWLYzfus0Z7itTeZ2C9XQA2YhhcdhJT9WDMqtSo3hHdkuyLT4UMKosTvY5xoziXoAnKrjWIDxHrUZlgXyX0jN-A315yXRD8EhxWJQK3GNGAvRW1D01ytg8PAIBXsAzQHSQkqzTFN7aJF5gYt7Q5nilLo4D200ASxV86uB7N8t82Y4g0YpeFmJBVxzfBfaKr7s7oAYoWTLScR8lmCoW6DkmMxkNqrGC4QX6rpPnwy1ubbZs_jEIAudLHhSrC1d9F39qoQ9crHUeJ_corBjcq5bpI6DKG5qoRV8ZIDPCyzvCfdUbIx0weg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نوسان قیمت تتر در دقایق اخیر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/akhbarefori/689648" target="_blank">📅 23:39 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689647">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
پشت پرده شایعه جنجالی فروش طلای تقلبی چه بود؟
🔹
پس از شایعه فروش طلای تقلبی در پلتفرم میلی، یک خبرنگار تلاش کرده تا پشت پرده این ماجرا و صحت و سقم آن را بررسی کند.
🔹
بررسی‌ها نشان می‌دهد موضوع فروش طلای تقلبی توسط این پلتفرم صحت ندارد و لازم است نهادهای نظارتی به پشت پرده این ماجرا ورود کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/akhbarefori/689647" target="_blank">📅 23:37 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689646">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09c6c1534f.mp4?token=WuUYv3S3vPytJ_6sljmu1jmyazD5vw4jm1ABIlJZBmsqeYosyij0ZZJ7otQ8XyzQwLvtR_yG83Fxy7YBf-qUjsixWXNV-wmNye-1KEYblD8sj6sGDj8OpGbaOKVM8978p87iKM6IJ36wBe6vIxQTJrRZ2iOyskwBh45Ymo9_I2RE3ETkoFFsAxOhzFBQ-iQzay616IHcazSbQ47uuBzJwp-bp7KVRFpWFz5OD7XBt3P7QhMF-aSqWE4zbQ8-aLHVnwOBqEIXsOb_NsONpZiMnhCQMRx1u6HmBl1HHJfNVrRRM1H4s1reo9L8Vr0BvCS8qucOypRghmb77wldoMWSdnGO2GNAGfGlm5KUrTxM7CZRJ_ZLRqjw9UslotwZ18OirTTBqa91QkJIQURAeoziQKhcv3BSU4JiKM3qmHXWD1kZoJo3NF67UdsHXchUgyv33CRHzuVCVqYcHKLqOf0yaWJO5qh-Tw0bO4vearVBaqr4qfnfB3YWMoIXmuZMMaGQu82reUVMKAS7DZ43zqvBIQ03rjuqAch2V52KMQYOEiDktadlUSRRrTFYdwYfVIIc06gCDf-PcwTHlPrPIMD3niJjk5mBpeCrBTdrBmRxpcaZst6fms182R5IPL5khTFTg43Pbve0kIlN5Kp4Kw5X08ub9gHoAP_oB6sHQwzWjGk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09c6c1534f.mp4?token=WuUYv3S3vPytJ_6sljmu1jmyazD5vw4jm1ABIlJZBmsqeYosyij0ZZJ7otQ8XyzQwLvtR_yG83Fxy7YBf-qUjsixWXNV-wmNye-1KEYblD8sj6sGDj8OpGbaOKVM8978p87iKM6IJ36wBe6vIxQTJrRZ2iOyskwBh45Ymo9_I2RE3ETkoFFsAxOhzFBQ-iQzay616IHcazSbQ47uuBzJwp-bp7KVRFpWFz5OD7XBt3P7QhMF-aSqWE4zbQ8-aLHVnwOBqEIXsOb_NsONpZiMnhCQMRx1u6HmBl1HHJfNVrRRM1H4s1reo9L8Vr0BvCS8qucOypRghmb77wldoMWSdnGO2GNAGfGlm5KUrTxM7CZRJ_ZLRqjw9UslotwZ18OirTTBqa91QkJIQURAeoziQKhcv3BSU4JiKM3qmHXWD1kZoJo3NF67UdsHXchUgyv33CRHzuVCVqYcHKLqOf0yaWJO5qh-Tw0bO4vearVBaqr4qfnfB3YWMoIXmuZMMaGQu82reUVMKAS7DZ43zqvBIQ03rjuqAch2V52KMQYOEiDktadlUSRRrTFYdwYfVIIc06gCDf-PcwTHlPrPIMD3niJjk5mBpeCrBTdrBmRxpcaZst6fms182R5IPL5khTFTg43Pbve0kIlN5Kp4Kw5X08ub9gHoAP_oB6sHQwzWjGk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ابوالقاسم طالبی، کارگردان: آخرین باری که در میدان سخنرانی کردم دادگاهی شدم و الان با ۳۰۰ میلیون وثیقه بیرون هستم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/akhbarefori/689646" target="_blank">📅 23:36 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689645">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
چین قید ایران را زده؟
🔹
خیلی‌ها معتقد هستند که چین ایران را فقط به خاطر نفت ارزان می‌خواهد و اگر این ادعا درست باشد، یک سوال خیلی مهم مطرح می‌شود.
🔹
جزئیات را در این گزارش ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/akhbarefori/689645" target="_blank">📅 23:30 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689644">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efcb85004f.mp4?token=ikKJp1ox6lTCtQ3x_GFnAP85frgJj2bzjwP-G8qQpngOvYcODkOiRk4Pvv3V_t43tfYjUQRc-ndV4hGukRRq7CmSrhdS2OvvJegnmilPx1aykiMDkQSuZIY0VUIuD6ng_L1x8Qct-zo9GqrbToKS4xSSwycfzl7z6mJ7s2EZHN8vsEmKUtejNZiYHcMtlyBFmJHGD7SwozNzzGD5Ut6P5PbCQ2-wAYJOfu9Rqoh7_79lM23cqpNrnz-Iur3F0Y7UaC2Ng_MYPWVGrySzYho_fhl4YFnRZfiNQQ_lvzKOxjfJl_zx4wxIKihLiHrP0sWtn0tT6n1CsA88Hcwc0dR26A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efcb85004f.mp4?token=ikKJp1ox6lTCtQ3x_GFnAP85frgJj2bzjwP-G8qQpngOvYcODkOiRk4Pvv3V_t43tfYjUQRc-ndV4hGukRRq7CmSrhdS2OvvJegnmilPx1aykiMDkQSuZIY0VUIuD6ng_L1x8Qct-zo9GqrbToKS4xSSwycfzl7z6mJ7s2EZHN8vsEmKUtejNZiYHcMtlyBFmJHGD7SwozNzzGD5Ut6P5PbCQ2-wAYJOfu9Rqoh7_79lM23cqpNrnz-Iur3F0Y7UaC2Ng_MYPWVGrySzYho_fhl4YFnRZfiNQQ_lvzKOxjfJl_zx4wxIKihLiHrP0sWtn0tT6n1CsA88Hcwc0dR26A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصویر شهید جمشید رجبی، از خدمه کشتی کانتینربر تجاری، که صبح امروز در نزدیکی جزیره هنگام مورد حمله  آمریکا قرار گرفت
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/akhbarefori/689644" target="_blank">📅 23:28 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689643">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/742cd77352.mp4?token=V-3It6rqoP5kfArd-oRrwcgN-HHV1nAOFYaqvOC94874qCz7PcFSFWdvg4I0zoJM6aDPJ73zbU2tjOOSa6fBH4RAIlyMUzz-TY-zb5f-ZL4RQqEQ0tyWuLBiOtBP-avb06KwWSGTxOItLdoiSpeAsAoJ0x7OtJzq_ZdtUnWAUasXD9KOWyrkOK5O5R6t3ewBHOYZR1pul_r_hNOBG5fR2KqPIIGOnzZX4PwEAXrF5OyV4n0ftnR0wrEP25e4l3dfHpcpe_1roCmz9Ep95jOt_rwdLvpZSCNjnqjXtezj_5XvShESeQChpUzuoGnWFi-27Z0ZGg0BS-ifjOQXlyaNdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/742cd77352.mp4?token=V-3It6rqoP5kfArd-oRrwcgN-HHV1nAOFYaqvOC94874qCz7PcFSFWdvg4I0zoJM6aDPJ73zbU2tjOOSa6fBH4RAIlyMUzz-TY-zb5f-ZL4RQqEQ0tyWuLBiOtBP-avb06KwWSGTxOItLdoiSpeAsAoJ0x7OtJzq_ZdtUnWAUasXD9KOWyrkOK5O5R6t3ewBHOYZR1pul_r_hNOBG5fR2KqPIIGOnzZX4PwEAXrF5OyV4n0ftnR0wrEP25e4l3dfHpcpe_1roCmz9Ep95jOt_rwdLvpZSCNjnqjXtezj_5XvShESeQChpUzuoGnWFi-27Z0ZGg0BS-ifjOQXlyaNdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔄
با اصلاحات ارزی دی ماه بازگشت ارز ۲ برابر شده است
⚠️
پورابراهیمی، رئیس کمیسیون اقتصادی دبیرخانه مجمع تشخیص
: میانگین بازگشت ارز صادراتی به کشور در سال‌های ۱۳۹۷ تا ۱۴۰۱ حدود
۸۵ درصد
بود. اما بین سال‌های ۱۴۰۲ تا ۱۴۰۴ همزمان با اجرای سیاست تثبیت ارز به حدود
۵۵ درصد
در سال کاهش یافت؛
یعنی از هر ۱۰۰ دلار درآمدهای ارزی، فقط ۵۵ دلار آن به چرخه مبادله رسمی کشور برمی‌گشت
.
⛔️
سیاست تثبیت با الزام صادرکنندگان به
عرضه ارز با نرخ‌های دستوری
، عملاً انگیزه صادرکنندگان را برای بازگشت ارز سرکوب کرده بود.
📈
اما اصلاحات ارزی دی‌ماه مسیر ورود ارز را تغییر داد؛ به‌گونه‌ای که طبق گفته دستیار ارزی همتی
حجم بازگشت ارز صادرکنندگان خرد
نسبت به مدت مشابه سال گذشته
دو برابر
شده است.
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/akhbarefori/689643" target="_blank">📅 23:25 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689642">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fe7844ab3.mp4?token=LHzCx8I_mZlolHNq5wST-aGJ1dtgYFHr1jWWSLJdZRhfaZOGoCAYFcVEYkpapG_Z_p8xlII66ADTRqDk-HfR1QbCQBJThhRjS0eRtZ0KFesqRswEfKQtRnvKlc6PJUhaFDN0sfY0TvdGgA7cCCY5Legnkd30AcxdXIgrm5GrOx9NF-MMaM_NrrQrmr_-ML2xL7F7Urel23vk3ELvAUMkJaLhwWZi_Ez_UcZOFpMo5yap4gluVU_CIrdM06tbw6YKRWYMa7od10rb2aOlTDyisPp_brLAmcPQI1HyZn9VVTuBMqqDY4yPPZoU5w2kILJ-t-M43Nj7IefB8rr409WAyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fe7844ab3.mp4?token=LHzCx8I_mZlolHNq5wST-aGJ1dtgYFHr1jWWSLJdZRhfaZOGoCAYFcVEYkpapG_Z_p8xlII66ADTRqDk-HfR1QbCQBJThhRjS0eRtZ0KFesqRswEfKQtRnvKlc6PJUhaFDN0sfY0TvdGgA7cCCY5Legnkd30AcxdXIgrm5GrOx9NF-MMaM_NrrQrmr_-ML2xL7F7Urel23vk3ELvAUMkJaLhwWZi_Ez_UcZOFpMo5yap4gluVU_CIrdM06tbw6YKRWYMa7od10rb2aOlTDyisPp_brLAmcPQI1HyZn9VVTuBMqqDY4yPPZoU5w2kILJ-t-M43Nj7IefB8rr409WAyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک سرم با تزریق، یک میلیون تومان ناقابل!
🔹
عصبانیت مجری تلویزیونی از گرانی هزینه‌های درمان و نابسامانی بازار دارو: چرا باید بیمار هم درد بیماری را تحمل کند و هم درد نداری را ؟!/ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/akhbarefori/689642" target="_blank">📅 23:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689641">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35040ed076.mp4?token=YTZUtPPDeO57gzbzjAK18jn2YVuRAKJt6-W1Hw8A5CQKnuEUii-FFFYcRQmMM0NGIw16FSvwOONyoWXB7jCsk-9jSdB_2yHCWI8E3oGMg7PRSKaK8ohc7gi2lsvGs2kcTjVy_Yn27Ezta4GW_1cKcNmd-8dQ1KghIuFNsp944_N5P2YQXBsAEJaMW6DtZFTBqyfipdkDcUQYaA0mvuci3eJ0_5WXr0SCUtp58E7Jx51N9ugvQ7jWHaXufdfiTC7UWvdjV07qNRP9wmceWF1Y1aJB2tFmEjkpU7oYZt5lR5LCtnWaqqrXYuA7nQqu0BsBEcb4QrzCDj0RYXV3ovI6NUhy0UyQfFXvN-XYN6AI0F0V7xSFemfc1mJMLDgfMfsF1_DnND3o8Pbxhy_FRqPJEGXyzeAffX2vlngD8p1fIZ6Iu9G6tc5LEJpCGHNJfXKPl4JJOruGtDMIT72b_h9oLzIG8QEs9QlfUVUaeCMbHXPx2JiHarv-fZy1osgmc8qLIpA-hE-tq3LpSZdp5TyTdoHcHc4aFFEuhduzEqpF4Ny1eFNcC2k6EvwvTGqLlHeSc1rILZy7hbCK8nPdOTTerG5Gql5FXSdoHuc-WjcK2pWq2Oo2wC1lRtYCP8D6Y5jHy78uGdKYIsqMLJ1Qv9Gtwk0N9H8yhdRWW7Om-noJpkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35040ed076.mp4?token=YTZUtPPDeO57gzbzjAK18jn2YVuRAKJt6-W1Hw8A5CQKnuEUii-FFFYcRQmMM0NGIw16FSvwOONyoWXB7jCsk-9jSdB_2yHCWI8E3oGMg7PRSKaK8ohc7gi2lsvGs2kcTjVy_Yn27Ezta4GW_1cKcNmd-8dQ1KghIuFNsp944_N5P2YQXBsAEJaMW6DtZFTBqyfipdkDcUQYaA0mvuci3eJ0_5WXr0SCUtp58E7Jx51N9ugvQ7jWHaXufdfiTC7UWvdjV07qNRP9wmceWF1Y1aJB2tFmEjkpU7oYZt5lR5LCtnWaqqrXYuA7nQqu0BsBEcb4QrzCDj0RYXV3ovI6NUhy0UyQfFXvN-XYN6AI0F0V7xSFemfc1mJMLDgfMfsF1_DnND3o8Pbxhy_FRqPJEGXyzeAffX2vlngD8p1fIZ6Iu9G6tc5LEJpCGHNJfXKPl4JJOruGtDMIT72b_h9oLzIG8QEs9QlfUVUaeCMbHXPx2JiHarv-fZy1osgmc8qLIpA-hE-tq3LpSZdp5TyTdoHcHc4aFFEuhduzEqpF4Ny1eFNcC2k6EvwvTGqLlHeSc1rILZy7hbCK8nPdOTTerG5Gql5FXSdoHuc-WjcK2pWq2Oo2wC1lRtYCP8D6Y5jHy78uGdKYIsqMLJ1Qv9Gtwk0N9H8yhdRWW7Om-noJpkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا رگ‌های دست برجسته ‌می‌شوند؟!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/akhbarefori/689641" target="_blank">📅 23:11 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689640">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
ادعای خبرنگار الجزیره: نشست عمان به درخواست عربستان سعودی و در پی حملات به خطوط لوله به تعویق افتاد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/akhbarefori/689640" target="_blank">📅 23:11 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689639">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
شبکه المسیره یمن: ۴ تن از فرماندهان مزدور سعودی در جریان درگیری‌ها با نیروهای مسلح یمن در منطقه «کهبوب» کشته و ۵ تن دیگر مجروح شدند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/akhbarefori/689639" target="_blank">📅 23:07 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689638">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/psepmmTDwMcZugHWj0ocPz5muoTIRvaxTlRV7wpGYyAEFWv1echkLRnKm_NauokcDGzSq3tkMA7JSgXqdQxZLGy0s0nsOOk12FyOol_mmcWBCiFL2lW9bmUyL10dXW_TmVJF4CcuMQUhEtQYO7gj4p6ijdHNL6JUimB9Je3Yf-ptc00EXcvoDrNgd__MaKJRSh7X55a5B1ycZP1IyVZHJTgxVH3WVjkdrDQcb78V_Ffn0p9nXINANHNSGcKnitXJ-MUZoUctlAwmmf8IefgvD-TxuO1W08OXHtcS9cZMxG9q7ycH8hLcPIulJPMwpFi79WEPa3N4MA4UK8bluASgtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از این بدتر غیرممکن است که بشود
بلومبرگ:
🔹
در یک جایگاه سوخت در سن‌دیه گو که گازوئیل در آن با قیمت ۹.۹۹ دلار به ازای هر گالن عرضه می‌شود، ساکنان کالیفرنیا دست‌کم می‌توانند به این دلخوش باشند که از نظر تئوری، قیمت‌ها دیگر نمی‌توانند از این بدتر شوند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/akhbarefori/689638" target="_blank">📅 23:05 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689633">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/akh2FjEKpvF-PwqF2aEGXCp0-5-c2M4VxFw3mhFg0BVC0AyQWWJpqa7LjYUcWSiwzRVPip2DnZwow6ROAB-6kLiW6ik9kZhKQWxt3Ua_FZBARlR2PvVbuTS3pttEJ6V7Y6EXZaL3K_wXAI3MAM4hTXoMACwN55E8y0VCLgQ4s8nJKh8t9CeEOsZNP7PeB6GZxAr6z1XoNpGebOe6XOsWXUGYtYlcEsZAzeAG_I_9L1nhCD6fZIZcVcaGjbQtKzem-bIgA_thUWSbJOtxwGBuhWQU5mg-qUopbvdIyS2TK_hyQImcmhX362h3PAN5AEdSdGGhyofc6VsV1_zVh2-OTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FijM9tAv9TqbTCmsGhnh8fgdawLg5DdrBIfQWjeDpqbPNDVoGnnTCA9scoECldzD5zOXDf69nE7ZqfFyzV7u2zACPztUi76Wp-28r-C9e8LQ1uzNO9OdWCv65wjMLCtdsBde-aN-eBD7_gCULz96xEYd8gt7q6HQaWIoiQEBM3b-x8FAT42o_Jk6XBkS6D2dMGs5b62eMC82imrwkOITAhFLwZJ0DGkZy7kw3RS1MVivlGpj1j-xbQIUrrwmAt_J1dIZMasJg-iDYaI-FUSXP3Id_Gk0SGPX4nSx-ZpCrppdmmftGpuDu9CvOco6R5ngiNA0kqSwe0HGG6rgxdkcnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O1jBWnkq6iFwjmS2FW1pOPztQuTK4XTkQ6bfsYsxfdNpSDNo_HKWCh8TTFRm0rP4MY7KsCWEvX1L5AeCfFO6gtGCcE97xYwqlk5WHtbTj2zkbT6spejD5Y4WR3BI1E4Rp80ZQ3L0zEoj_cssIlC1I7_G6blinolx7ACwxTTNxKXCycAi9i8EpTaflGziMDZ9WU_ScdknsamguAr5EhhDopRmgDgKZbDeaSD9LRj3DwbsDzFfsadcep1ZYA87KjSzsQxb7omKXXb2EkQmZWagMJ6H37wjfa43DXdfkooJsTMPERf--ZdD4j8wjw3BUkpCwXXoiSfa66ZwjIaiOGmCnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PUQ1lg7HskqNq5iVnx55gu2EJu4ERlx4_FeOsWa8M4tXOwwyvGigjCumrHvG27lf97X5Sr-B5kokK8Ohzm0LLG90iulEI74-ja8EyCEwCeZpsJCnzOP8RDgTxyfF2-4j0p6NiQrSBi7wqgsPcLz9WgEPGI4f9Bd3Rig8btDAJihslrba_SJn9GOykLXHRiQ8XC3sI4rmTiKG79S8A6y7SAq1uymwzmlZEfP7bY-5VMk_D6EXXVPhBfUITwKoDQRgH38kjKvImA4UTrBetTKirdnxnAF-abRG18RF98iAFOARDFSB-QplJsGgiSNVvTNjUCGQWxPx7O46hKxCCV5cbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gWK_CreIvgOtxpL7VXR4aiaADTol8EUupBi0DyGqxokmxIviB2cuxkeZ67vD-W-OuS7X7_yv00g6-aS2uS6veOLTHIhFj9aDMjttnDI413AXDjzhiAxpLwb9zK5YMUlmhtqnaBg68HM3-SY24Aaxn_RFWwhFzG-PwB1bz-pRUUSM6_pCP6NGr71duFxPMDMpktgR73wYKJMhRYKs-Ld9kqlHBFGUCKpf4m3OT0YsVh5lt4v6wOdZvqdbs__lHmBPgi79Io5wsLxAGwfg0EzaKK1ww-h6uPQ4aE6u_sQCYSMtAa4W5CJv_jexyQfDP8tPFHQoNGAAdSh4e8GlXF9LQQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نگاهی آماری به وضعیت  برنامه‌نویسی در ایران
🔹
بر اساس داده‌های گزارش جامعه برنامه‌نویسی ایران، بیش از ۷۰ درصد فعالان این حوزه جوانان ۱۸ تا ۲۹ سال هستند.
🔹
همچنین بیش از ۵۴ درصد نیروها سابقه کاری کمتر از ۲ سال دارند و تنها ۱۸ درصد از آن‌ها بیش از ۵ سال در این حرفه دارای تجربه هستند.
🔹
از منظر جنسیتی و تحصیلات، ۸۲ درصد جامعه برنامه‌نویسان ایران را مردان و ۱۸ درصد را زنان تشکیل می‌دهند.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/akhbarefori/689633" target="_blank">📅 23:03 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689632">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
عمان نشست منطقه‌ای برای دستیابی به توافق درباره تنگه هرمز را به تعویق انداخت  بدر البوسعیدی، وزیر امور خارجه عمان:
🔹
وزیر خارجه عمان اعلام کرد نشست منطقه‌ای قرار بود فردا در صلاله برگزار شود، اما برای تضمین دستیابی به توافق، موعد آن به تعویق افتاد.
🇮🇷
✊
…</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/akhbarefori/689632" target="_blank">📅 22:58 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689631">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N-9H8XkRSpzzw5jdhPt5jBGIpcoFHU6sIj3LCas6eBZdYOW9q7hwk17PnzOAxvXML_I_Wy8GzH35aiDrsR_nrGi56Ny5mzU8AHCTP5JXTGi4jNxo0n-EytRvSKzhUdP8ndDCtxlleXcSx1N1T9ixzB7sMFVo4wzFjDPnOV696vtcrHDHxSp55WkNqELnY41mMkTwREheNvVSbD3grDwmc8oxzPlyFw_xsdmCEaWnWGfNdxm7poBYqPVzh4xxlz7fDdhFhQhqrabrOGLTIfjgEsnei8OxZBrrdgKJ-GP-67s08H1QFL6tQTe4ivtXosAnK4kKGbVgE0llQLcl8yB_BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«انفجار کنترل‌شده» تا «توطئه موساد» | پنج نظریه‌ای که ۲۵ سال است ۱۱ سپتامبر را رها نمی‌کنند
🔹
یازده سپتامبر ۲۰۰۱ به‌سرعت به بستری برای شکل‌گیری مجموعه‌ای از پرسش‌ها، تردیدها و نظریه‌های توطئه تبدیل شد. تصاویر فروریختن برج‌های مرکز تجارت جهانی، برخورد هواپیما با پنتاگون و حجم گسترده اطلاعات و هشدارهای پیش از حملات، برای سال‌ها خوراک روایت‌هایی بود که می‌کوشیدند توضیحی متفاوت از روایت رسمی ارائه دهند.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3244962</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/akhbarefori/689631" target="_blank">📅 22:55 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689630">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
چرا شعار «اگر قیمت انرژی را جهانی می‌کنید پس حقوق را هم جهانی کنید» پوپولیستی است و توسط برخی جریان‌های سیاسی برای عوام فریبی استفاده می‌شود؟ دکتر گلوانی، اقتصاددان پاسخ می‌دهد/ تیترتجارت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/akhbarefori/689630" target="_blank">📅 22:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689629">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
آتش‌سوزی در یک نفت‌کش در تنگۀ هرمز
سازمان تجارت دریایی انگلیس:
🔹
یک نفتکش که به‌طور کامل بارگیری شده و در تنگۀ هرمز مورد اصابت یک موشک قرارگرفته‌بود، دچار آتش‌سوزی شدید شده‌است.
🔹
این سازمان پیش‌ازاین خبر داده بود که یک نفتکش با پرچم پاناما هنگام عبور از تنگۀ هرمز مورد اصابت قرار گرفته و از کار افتاد./ فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/akhbarefori/689629" target="_blank">📅 22:51 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689628">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
سازمان رسانه‌ای اسرائیل مدعی شد ارتش به صورت محدود از ارتفاعات «علی الطاهر» به سمت قلعه «شقيف» در جنوب لبنان عقب‌نشینی کرده‌ است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/akhbarefori/689628" target="_blank">📅 22:46 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689627">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86cb4ec85c.mp4?token=qbT0vzBhsn2mfEZr5VLIwdSVvSfLeXj6grzKSI4uI5_ADSKuEevmqU0lEIcS1DNPXMoj4EVJMgqHuGlQbUOh_K7IN4lRw7_pLbjxfbQ-UngJKek6tRPEqSozSoxCpAsqXWPCmk3Ad0kMoKnK5fxiB521095niZb_WtuKxAdtgpo65-gQUvqtLNlQVWncYhGfmu9bA0NHFUK1twY6szfhZBg7Jw8m7L3mzzRpza2BZnyxzb5u09QLP2frP6OyfVvI7T6Q7TVi98V6HaI8ZUYbhlpzo_z-aCHp-ghoPStCmvf1oJuwYzx9B2wQ6eKyQjfFG7qRw6YEfWSIHY_ZeTS8kjM7s--E9BS3JFsWDyWwjV1i8GGorsL64BcZJvwvxThfF93rnoyADGrJ1I1QSsZhIEBap7oZgUdNeNhcsA_-nugLeEV7_rdha7uPO_RbIO9FUwt_tQ5_Jbd1ZznEJK6KZb-e8HrB4tZz4A-ToTXK0d6B4YrUzhAQzlEy9WXqNB7mNVo36xjWkGexV2UFYPRopWtAA3gDUFb46ZvE1AQjLq4kvsDSnlprX2g0d9-GVbXfuoAajcsxV709BsMvdB4br6I94VEZG64iOmjHR-Y6Blx4393RIeBIu9iktgWMcoBsMLKfXiOZHlagp3YhOICoLLxEFX06YSJlGf2zlVLQxYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86cb4ec85c.mp4?token=qbT0vzBhsn2mfEZr5VLIwdSVvSfLeXj6grzKSI4uI5_ADSKuEevmqU0lEIcS1DNPXMoj4EVJMgqHuGlQbUOh_K7IN4lRw7_pLbjxfbQ-UngJKek6tRPEqSozSoxCpAsqXWPCmk3Ad0kMoKnK5fxiB521095niZb_WtuKxAdtgpo65-gQUvqtLNlQVWncYhGfmu9bA0NHFUK1twY6szfhZBg7Jw8m7L3mzzRpza2BZnyxzb5u09QLP2frP6OyfVvI7T6Q7TVi98V6HaI8ZUYbhlpzo_z-aCHp-ghoPStCmvf1oJuwYzx9B2wQ6eKyQjfFG7qRw6YEfWSIHY_ZeTS8kjM7s--E9BS3JFsWDyWwjV1i8GGorsL64BcZJvwvxThfF93rnoyADGrJ1I1QSsZhIEBap7oZgUdNeNhcsA_-nugLeEV7_rdha7uPO_RbIO9FUwt_tQ5_Jbd1ZznEJK6KZb-e8HrB4tZz4A-ToTXK0d6B4YrUzhAQzlEy9WXqNB7mNVo36xjWkGexV2UFYPRopWtAA3gDUFb46ZvE1AQjLq4kvsDSnlprX2g0d9-GVbXfuoAajcsxV709BsMvdB4br6I94VEZG64iOmjHR-Y6Blx4393RIeBIu9iktgWMcoBsMLKfXiOZHlagp3YhOICoLLxEFX06YSJlGf2zlVLQxYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پایین دفترهاش می‌نوشت: سردار سپهبد شهید پارسا سوزنی
🔹
خاطرات شنیدنی پدر و مادر پارسا سوزنی از عشق و علاقه‌ی پارسا به شهادت از دوران کودکی.
🔹
سرباز شهید پارسا سوزنی، پهلوان شیروانی بود که در ۲۲شهریور۱۴۰۳ به‌همراه دو تن دیگر از همرزمانش به نام‌های امیر ابراهیم‌زاده و امین نارویی توسط گروهک جیش‌الظلم در میرجاوه به شهادت رسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/akhbarefori/689627" target="_blank">📅 22:44 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689626">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
ادعای سی‌ان‌ان: پیشنهاد عمان شامل پرداخت‌های داوطلبانه برای ایمنی کشتیرانی و حفاظت از محیط زیست است؛ این پیشنهاد پس از ردِ دریافتِ هزینه‌های اجباریِ مورد نظر ایران مطرح شده است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/akhbarefori/689626" target="_blank">📅 22:42 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689625">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f75d753ba1.mp4?token=Q8ajaaRJu4uOAD4yKAS9IWpwiV-kbEgsI93ixh0pIY6D1zhSVB4wopYZjcrLBjoe2rRWYgouKJ__FBKScHfsi3UkXzRklr9-_Q7nU7kMW5ounp4mw57VM0LTTCQTEUmS2_E2jq2_BuEU9Or5sT6WMFmRjrqRc3ZsqXAWMg5jKxDUg_oYaABP9J84UiyMWQAPe6RfBeW6HBStw8k6bWxuXApRdO5tJGa22imzNfay3WB1g1l9TUAs37h563OPlBDQOddkHPnvlDOhO9wnJ_UBwXULOuI4bWv-7RRvNixdZrq31CdVSr4ECVogcBoBK8PqOFCT9v6mJGx60OTLeBdNsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75d753ba1.mp4?token=Q8ajaaRJu4uOAD4yKAS9IWpwiV-kbEgsI93ixh0pIY6D1zhSVB4wopYZjcrLBjoe2rRWYgouKJ__FBKScHfsi3UkXzRklr9-_Q7nU7kMW5ounp4mw57VM0LTTCQTEUmS2_E2jq2_BuEU9Or5sT6WMFmRjrqRc3ZsqXAWMg5jKxDUg_oYaABP9J84UiyMWQAPe6RfBeW6HBStw8k6bWxuXApRdO5tJGa22imzNfay3WB1g1l9TUAs37h563OPlBDQOddkHPnvlDOhO9wnJ_UBwXULOuI4bWv-7RRvNixdZrq31CdVSr4ECVogcBoBK8PqOFCT9v6mJGx60OTLeBdNsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار رادان: بیش از ۵۰۰ سارق را با ضرب گلوله متوقف کردیم
🔹
۵۶ نفر از آنان که در مقابل ماموران اسلحه کشیده یا مقاومت کرده بودند هم کشته شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/akhbarefori/689625" target="_blank">📅 22:37 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689624">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f101950b56.mp4?token=sYdxmv4srzj0Ksb-YiKMlpXAfVLcXz1SjXYSUK9YWTz6qRR2C9Yq1H19CuYU5KoyAeN593YJo9e7yybDUC6i2-6j9HpBZ-NamtlI_XtFk_8aimmXkz_rzlt52fcScZl-YLKMhaV2w7vVvmbkvpK6fGH1AZpJ9QIMpujGPnK5xi22BEMsowTRH8fevnkXfZ8mt4x6nqB347wZRRREIXIYOFjzoVUnR_pMccezSuRq6DmY3hdx2Wh_biAUH3uXvJiZWwEU0-U3FsKxRrOlmQ528W2uSDxxSNgfT_K-iZqBvzkAJBzqc_gmyKR7p6keex0y12JT9Fc3kfN1aXhcWuC61Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f101950b56.mp4?token=sYdxmv4srzj0Ksb-YiKMlpXAfVLcXz1SjXYSUK9YWTz6qRR2C9Yq1H19CuYU5KoyAeN593YJo9e7yybDUC6i2-6j9HpBZ-NamtlI_XtFk_8aimmXkz_rzlt52fcScZl-YLKMhaV2w7vVvmbkvpK6fGH1AZpJ9QIMpujGPnK5xi22BEMsowTRH8fevnkXfZ8mt4x6nqB347wZRRREIXIYOFjzoVUnR_pMccezSuRq6DmY3hdx2Wh_biAUH3uXvJiZWwEU0-U3FsKxRrOlmQ528W2uSDxxSNgfT_K-iZqBvzkAJBzqc_gmyKR7p6keex0y12JT9Fc3kfN1aXhcWuC61Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سه نکته مهم برای فهم بهتر ادبیات روس
🇷🇺
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/akhbarefori/689624" target="_blank">📅 22:35 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689623">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b9pCqOUyelKwS_a3KW4SqVpESSc0_MlSLJb0LEdy1L3Ho3e5Ra3Ba-RTd7qZlTUxuJKKFkQKKSruRf4Dro0VYKEZK4RhY-pNp_tOJ4XLKO-2D9AL0WVcuYm3ZFto-XPKep8N9iNBqiDYH3g0vlP8ZKV9duoCXuL3jaaRgC6Us0Y9d9Em6wGY6WT4cjEAUybqzBp8Ev-zVGTdHokrIcTVWS3nNtm5tV0zILN77YdgttKzrQ-OAq7HjkESVlGplQ-YP8oHnVEcSQGOozIfoY1lR9lMOWo2ZY6hQCFLKypB9HGv5vIJ1l-IEl3ufsf5iYtBFxjUs237CLBwVCNjx2xp0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاربر توییتر: اگر ایران شروع به آزمایش سلاح هسته‌ای کند، با همان رویکردی که در قبال کره شمالی اتخاذ شده، با آن برخورد خواهد شد
🔹
ترامپ باسن آنها را خواهد بوسید و از جنگ با آنها اجتناب خواهد کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/akhbarefori/689623" target="_blank">📅 22:18 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689622">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lo-N3u72biP35YcN_AfBOnQZ0TXHTMeld4eLn1BxzJJ6WpbNRneyHhdrEhpQpJlpFrw51m9wKrdo9gS7wqPbQ8PvQW3IvOL5qHbAqq4BKML7KCGTanM3UXxVJUtiaEbQit-04a--6aMwwMghitE6RBAo0y2TiayfS76Sl78UJX_xy1cJY_RGpiGKy8EglB292YrVIlcHsH1GlsEQoDsBBGq1_MKNBgL4pwEbj7BfUs9HpFvjKlOO7jwH4W4EdDpM6SXkkAlr5AzvL00OXL7QJP-x5mQ_wiKXhjAQFf8bNx_qK3_UyZLuSKEgqo5PexH2Ke-qN0u8zGOIsaSKaOdKBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حازالدین رئیس اجرایی حزب شرقی در آمریکا: پرشیا یک کشور نیست
🔹
بلکه نوعی ابرهوش انسانی است که تمدن‌ها، اندیشه‌ها، باورها و هنجارهای گوناگون اوراسیا را در طول تاریخ جذب و با یکدیگر تلفیق کرده و از آن‌ها یک جهان‌بینی اخلاقیِ جهان‌شمول ساخته است.
🔹
در آینده‌ای بسیار دور، چنین نظمی جایگزین امپراتوری جهانی آمریکا خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/akhbarefori/689622" target="_blank">📅 22:05 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689620">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفروشگاه قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VRYiAP2rR3Dx77XEy0ixs02loHD3eXMvvn5R1cr4EVWb7ehSgOxxNcQUf6opGmtWZn1K4jibwbvZ1rEWiOJho8eP3Yke5-sVxHZW3mE0I6RHFwVaSqXHaJVuZN6JLg5RuSfyjiREPFaBd4flBar_r_ide6cs_PsaP75ykUms2l5n-DkK7pFCkOaA3A6BW0bNJ74fP1Qx9PIIB0N3zM4npMNDpS4Lu5S4ved8sSoa31nSn6Q8I1qN1CxqXgWxiNk2vkAd2gLz0E2ii3GUxnX_ASJrLc9xpaFHzaPoXazf09UTH2mSE8QR3F2f0dztbDHdf0RzCrnUor_c7-oVlwxlPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕊
جعبه هدیه صحن نو
بسته‌ای نفیس و معنوی برای تقدیم به عزیزانی که دوستشان دارید.
✨
مشخصات محصول:
▫️
نگین متبرک؛ تراش‌خورده از سنگ‌های روضه منوره حرم مطهر امام رضا (ع)
▫️
مُهر نماز؛ ساخته‌شده از سنگ‌فرش صحن‌های حرم رضوی
▫️
تسبیح سنگ هرکاره؛ یادگاری از سنگ مشهور و اصیل مشهد
▫️
عطر حرم رضوی؛ با رایحه مورد استفاده در روضه منوره و رواق‌های حرم
▫️
جعبه چوبی نفیس؛ مزین به نقش ایوان طلای صحن نو با نقاشی دستی برجسته
▫️
ابعاد: ۱۴ × ۱۴ × ۴ سانتی‌متر
▫️
متریال: MDF با روکش چوب راش
💰
قیمت اصلی: ۲٬۲۵۰٬۰۰۰ تومان
💰
قیمت ویژه: ۱٬۹۵۰٬۰۰۰ تومان
⏳
موجودی محدود؛ برای ثبت سفارش، همین حالا اقدام کنید.
📩
سفارش:
@gharar_order
🤍
هر خرید از «قرار»، سهمی در مسیر خیر.
@ghararshop</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/akhbarefori/689620" target="_blank">📅 22:00 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689619">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6908b4bb9b.mp4?token=Tgsep8jn5GsatkZ2SCPVMVyV1S8IY2Mqc3tI3OXq10BFxHcTHfRAnOwTscJa2vrLrFX4OXLvrxkbzlvxgAGP9miH8RGLIGSJUpIfZmxKlB5Lg3h2qSk7rwKtG1sPDLKjAF5EvBDVSCiLsderBcve39VtS4XX98In0K0WpP9HYRYKfeoyGr2D99k3aA6KXLhjMdjAg7Az43Y8Ep3EemfX-IYGrUKrarlCqhdHY-2Q9i-ezvoQ67ooNElKWMi0CQkVJrPp7sRj6L2AU-rCKLZGUUCZaqltGcWrhH2gIUFfxiUgkWI8s5xgw1uV2Rw6d0wqlGilx9QoA0C5jSJ6esdOHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6908b4bb9b.mp4?token=Tgsep8jn5GsatkZ2SCPVMVyV1S8IY2Mqc3tI3OXq10BFxHcTHfRAnOwTscJa2vrLrFX4OXLvrxkbzlvxgAGP9miH8RGLIGSJUpIfZmxKlB5Lg3h2qSk7rwKtG1sPDLKjAF5EvBDVSCiLsderBcve39VtS4XX98In0K0WpP9HYRYKfeoyGr2D99k3aA6KXLhjMdjAg7Az43Y8Ep3EemfX-IYGrUKrarlCqhdHY-2Q9i-ezvoQ67ooNElKWMi0CQkVJrPp7sRj6L2AU-rCKLZGUUCZaqltGcWrhH2gIUFfxiUgkWI8s5xgw1uV2Rw6d0wqlGilx9QoA0C5jSJ6esdOHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هم‌اکنون؛ بارش شدید باران
در کوچصفهان
#اخبار_گیلان
در فضای مجازی
👇
@akhbaregilan</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/akhbarefori/689619" target="_blank">📅 22:00 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689618">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
اتحادیه تالارهای پذیرایی: ۹۹ درصد خانه‌های عقد غیرقانونی هستند
بیژن عبداللهی‌مقدم، رئیس اتحادیه تالارهای پذیرایی و تجهیز مجالس تهران در
#گفتگو
با خبرفوری:
🔹
حدود ۹۰ درصد واحدهای تشریفات  که در برخی سایت‌های تبلیغاتی معرفی می‌شوند، فاقد مجوز هستند و بخش زیادی از آن‌ها کلاهبردار هستند.
🔹
برخی از این واحدها پس از دریافت بیعانه ناپدید می‌شوند و برخی نیز تنها ۵۰ درصد خدمات وعده‌ داده‌ شده را تحویل می‌دهند و همچنین ۹۹ درصد خانه‌های عقد غیرقانونی هستند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/akhbarefori/689618" target="_blank">📅 21:45 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689617">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
حذف سهمیه بنزین خودروهای نوشماره تکذیب شد
🔹
تمام خودروهای سواری شخصی موجود بجز خودروهای دولتی، وارداتی و مناطق آزاد و خودروی دوم به بعد مالکین چند خودرو، مشمول ۶۰ لیتر سهمیه ۱۵۰۰ تومانی و ۵۰ لیتر سهمیه ۳۰۰۰ تومانی می‌شوند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/akhbarefori/689617" target="_blank">📅 21:39 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689616">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7e719cff2.mp4?token=Iqz5Bs9Q_hc5Gz8hRng1bwj65QXOQLuOLiHq5PA-3i61uVh3_9HHRYOKSg6jyaNY4fHhukpyutztH04WdOAvIqeDVrhh8BMpVAYyx7NFXeadVcnBlsUZS1s1YZorjDaKOjArxz5SnFXkNiFW1Toc8ZHmIfnv2qmc2ymJ4qKrOT_o6yfKgZSDfsuOlT2XbMvVrpgfnhKEg0JHU8rFUUvwtS8M21O1leQ5DyQD6dQSLb_7wSqYMmTOZZMh5EgkjEkcFuSOOUNQVU5UgqPAAe1rDqjwjrX2IixndCMlhety8bRowHXoFFYKKxwcY4juCH9KEt6tfj19fqXbyBlyD8g5YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7e719cff2.mp4?token=Iqz5Bs9Q_hc5Gz8hRng1bwj65QXOQLuOLiHq5PA-3i61uVh3_9HHRYOKSg6jyaNY4fHhukpyutztH04WdOAvIqeDVrhh8BMpVAYyx7NFXeadVcnBlsUZS1s1YZorjDaKOjArxz5SnFXkNiFW1Toc8ZHmIfnv2qmc2ymJ4qKrOT_o6yfKgZSDfsuOlT2XbMvVrpgfnhKEg0JHU8rFUUvwtS8M21O1leQ5DyQD6dQSLb_7wSqYMmTOZZMh5EgkjEkcFuSOOUNQVU5UgqPAAe1rDqjwjrX2IixndCMlhety8bRowHXoFFYKKxwcY4juCH9KEt6tfj19fqXbyBlyD8g5YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجار بسته بمب‌گذاری شده در کلیسای مسیحی‌ها در حماه سوریه
🔹
بمب در مقابل کلیسای «السیده العذراء» متعلق به مسیحیان ارتدوکس، کار گذاشته شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/akhbarefori/689616" target="_blank">📅 21:37 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689615">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03c851e7d0.mp4?token=Pf43vMB6nkHF_e9191CdVaw8XzxLTQehs9omQQ4iHTWZGckuKooFOIB25s3--bjItw5_FN9FNK8NkBGLUE1J_tDxhAomNKkJ3i7irZQ2zmzG7dNy_52x83diw-KCUVboLAgHeDt4Efgl4aG5ye5xGvi9eRHVQBvPX8DyHLP4dN7nPPV8lU5SrO1-A8BNgJ_1Ua1J1MG5GbrFncoKRDk3mN_GVPiW7mvxutteV81UHU74oOJ3GqJ0caxB8d8icOHqboZ0p5tTwJtIiAyh7kS5AEJ7DCW-_v_q0s-dcQ8lvstxMe79wW7lUwpDheKkCjWsENpfgH3eHbm0LqwbMXIyDi_6G8mmjUkOGBk7orEd7A4R23gA95KU9LoPFR--_LBK9gyOVBN-9gaxAeXmlLviw3TtVGuJchCO9X3B5KorZRKBaKR6-35tXi6SZN7zQBVoJeT9en3ZHcasP08ZNKlsSAIC-P4OFp2XZZzRe6IiD4Y8DHgoS85g0koBGY20HAOItMlpyuSGkJhQduqEr8ZUTEFbAXiaPYDjw_ZnxD6m2MdI7s6ZJJ__SKVip67j5h4gO3fTShIlUOrLWiSgqyPvoKLtKlvbGs40d9RmerQzKafga6rmCqMCu2ZU0qJ0Vm2ArwgTub7g8qPM28jb1FxmFhmGe9n_CoUu5_G7cIv5-qU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03c851e7d0.mp4?token=Pf43vMB6nkHF_e9191CdVaw8XzxLTQehs9omQQ4iHTWZGckuKooFOIB25s3--bjItw5_FN9FNK8NkBGLUE1J_tDxhAomNKkJ3i7irZQ2zmzG7dNy_52x83diw-KCUVboLAgHeDt4Efgl4aG5ye5xGvi9eRHVQBvPX8DyHLP4dN7nPPV8lU5SrO1-A8BNgJ_1Ua1J1MG5GbrFncoKRDk3mN_GVPiW7mvxutteV81UHU74oOJ3GqJ0caxB8d8icOHqboZ0p5tTwJtIiAyh7kS5AEJ7DCW-_v_q0s-dcQ8lvstxMe79wW7lUwpDheKkCjWsENpfgH3eHbm0LqwbMXIyDi_6G8mmjUkOGBk7orEd7A4R23gA95KU9LoPFR--_LBK9gyOVBN-9gaxAeXmlLviw3TtVGuJchCO9X3B5KorZRKBaKR6-35tXi6SZN7zQBVoJeT9en3ZHcasP08ZNKlsSAIC-P4OFp2XZZzRe6IiD4Y8DHgoS85g0koBGY20HAOItMlpyuSGkJhQduqEr8ZUTEFbAXiaPYDjw_ZnxD6m2MdI7s6ZJJ__SKVip67j5h4gO3fTShIlUOrLWiSgqyPvoKLtKlvbGs40d9RmerQzKafga6rmCqMCu2ZU0qJ0Vm2ArwgTub7g8qPM28jb1FxmFhmGe9n_CoUu5_G7cIv5-qU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور قدرتمند کانون ایران نوین در جایتکس استانبول و استقبال بی نظیر بازدید کنندگان بین‌المللی و ایرانی
🔹
پس از حضور قدرتمند و متفاوت کانون ایران نوین در نمایشگاه الکامپ ۲۹، این مجموعه در نخستین حضور بین‌المللی خود، در نمایشگاه جایتکس استانبول، با استقبال قابل توجه بازدیدکنندگان بین‌المللی و ایرانیان حاضر در نمایشگاه و مواجه شد.
🔹
حضور کانون ایران نوین در جایتکس استانبول، فرصتی برای معرفی توانمندی‌ها، دستاوردها و راهکارهای این مجموعه در حوزه‌های بازاریابی، برند و فناوری‌های نوین بازاریابی بود؛ حوزه‌هایی که کانون ایران نوین طی ۳۶ سال فعالیت خود در بازار ایران، تجربه و دانش قابل توجهی در آنها به دست آورده  و آماده صادرات همه خدمات خود به بازارهای بین المللی است
🔹
جایتکس استانبول برای کانون ایران نوین فقط یک حضور نمایشگاهی نبود؛ آغاز مسیری بود برای اینکه تجربه و دستاوردهای یک مجموعه ایرانی، در مقیاسی فراتر از بازار ایران  عرضه شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/akhbarefori/689615" target="_blank">📅 21:36 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689614">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
شبکه عبری کان: جزئیات عملیات ارتش اسرائیل برای انهدام شبکه علی الطاهر فاش شد
🔹
این عملیات سه ماه ادامه داشت و با یک عملیات فریب پس از تصرف شقيف آغاز شد.
🔹
در جریان آن، ۵۰ عضو حزب‌الله که حاضر به تسلیم نشدند و تا پای مرگ جنگیدند، [شهید] شدند. این افراد داخل…</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/akhbarefori/689614" target="_blank">📅 21:36 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689613">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a702c90e1.mp4?token=ORMGKn0fLKheX8oIJSHj74OzRjFgaE6ZbxpdWQvkO-vlBjimeQg94wkG3rQB-cm47Skvw4WbhCNugfXMeTfSsRKKr9pA5L0fMCeyDkoQz1grBG0cx7ma2avYIB_Bm29SL_zuFJJKEMak4_TXrHWIg9B0qITP6ER07-Q2q_MOdyQDVZxst8RMtksgu84JOfukBhM1autGI8ZHcMHbDSrtu0PWkzourHZB1XPiacnd9kTfrcKA54vcqIcm26NmHBKFnJHVgFjJBpjqW3LhluvtBHz1hcczyxPNS749P0DUy5nTku7CUtosccpNXeBx8PaGqty-yeC07UnFmWYJT9C37U6edWAPESArKe991dblQm3Hk3F961PsZNFrad_avyeHkkF5EMpXDhIchWJo1LoI21olCYqMHcOcd83MSAZsh3SeIu-3mU45pE9fUH9FhwVNeDQJA2yoY5F_cUJ1VQV94FISEKmxse5w1jxb3QpiQL-I5TCABneJiCr8UlPd4TLZmEjX8yLehegkI2PCnHIyIwQIan2m0zSTLOKTSGwx06lGIkjBJMpFAyCFBdXLvlsEs-qiXnadzJEmkaLF-wZNSdoKJGrXvDRJz0pvQvHXSNo4WUOHGa8bUeA8rFiIhQqRzp6FqwmwjKnBSypCCsjb4LVxD2jPqUKJ9xvT6uOAcic" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a702c90e1.mp4?token=ORMGKn0fLKheX8oIJSHj74OzRjFgaE6ZbxpdWQvkO-vlBjimeQg94wkG3rQB-cm47Skvw4WbhCNugfXMeTfSsRKKr9pA5L0fMCeyDkoQz1grBG0cx7ma2avYIB_Bm29SL_zuFJJKEMak4_TXrHWIg9B0qITP6ER07-Q2q_MOdyQDVZxst8RMtksgu84JOfukBhM1autGI8ZHcMHbDSrtu0PWkzourHZB1XPiacnd9kTfrcKA54vcqIcm26NmHBKFnJHVgFjJBpjqW3LhluvtBHz1hcczyxPNS749P0DUy5nTku7CUtosccpNXeBx8PaGqty-yeC07UnFmWYJT9C37U6edWAPESArKe991dblQm3Hk3F961PsZNFrad_avyeHkkF5EMpXDhIchWJo1LoI21olCYqMHcOcd83MSAZsh3SeIu-3mU45pE9fUH9FhwVNeDQJA2yoY5F_cUJ1VQV94FISEKmxse5w1jxb3QpiQL-I5TCABneJiCr8UlPd4TLZmEjX8yLehegkI2PCnHIyIwQIan2m0zSTLOKTSGwx06lGIkjBJMpFAyCFBdXLvlsEs-qiXnadzJEmkaLF-wZNSdoKJGrXvDRJz0pvQvHXSNo4WUOHGa8bUeA8rFiIhQqRzp6FqwmwjKnBSypCCsjb4LVxD2jPqUKJ9xvT6uOAcic" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نظر علی دایی درباره مافیای خودرو در ایران: کجای جامعه مافیا ندارد که صنعت خودرو نداشته باشد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/akhbarefori/689613" target="_blank">📅 21:34 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689612">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
ایران چگونه روی اف-۳۵ لاک کرده بود؟/ آمریکا برای از کار انداختن سامانه‌های پدافند هوایی ایران آمده بود؛ اما ایران نقشه‌های دیگری در سر داشت!
🔹
در ۳۱ ژوئیه، ایالات متحده بخش قابل‌توجهی از ذخایر تسلیحاتی خود را برای نابودی سامانه پدافند هوایی ایران در جنوب به کار گرفت، اما تنها ساعاتی بعد با واقعیتی آشکار و غیرقابل‌انکار روبرو شد./ پرس‌تی‌وی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/akhbarefori/689612" target="_blank">📅 21:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689604">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاقدامات هیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jBqztibDuL_3lRUzj-rCeaTJjX_AwT_L-ubBT-WFHaxrjvYUEs1H837P47S8NHxXg-JxsMyhGyI4u1LhDK90sEtDrbQIAFPdQUMsEFDWpKA2gaYg7hj73qgld1IG2XAF7WNkd2K9H26Einl7LIdDjjHTY3ppO9mc2bPB7IrvdoGZ4ys9iQcTKMyGZQmUmW7CZGMeBLVQ0vUQQnhPtWJtMTIBqV7oDWsWMKCbLp_csP5y5PoAqS0dNqp5aRS1JdZWDdJtsDypyGwmdeYj4Juh0s-dyP1AGZoPom88wS549a2nSe-foEUlKSKIukt7JlAhRMh4JboFhZdBwvKqEF1IKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KZuYHKLuT3oX7W0SLc2VUizE0GQhgzJAcAaWbHTqoZSnTGDqnoMHQ6HD_-HzVWSaE52nAf9Q2vT9N0T9UsfmZsPWmMVWYS5s1gaf3wrXggONlfndbRL8CnoC4E9TeVfxmvoSOxBjMP-7HvMwiezHYWcsqlKNLew6Uz-LP9jcB_IZQZZ4lXdoePp68Wux49eBbEVC4h3YaaixUafZgswVMmmOew2QESpoEQZ7kFZxgsoGVt6u6f3J_3uZBXcCp6j67tlKP8hJtFZE_uYYA-96Mv-A_GFvrQBglq2qcvtJO-tbG7RdHbfEvdpovflXy14hjozczmMGSPx-JCGO6jan6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/acYzNe2RGiGZMvJ29_F7iBU3fEWtiSfeqpfmBRNwgGVRWHngCtIus2_EK-OEYAXvATTP5Brg_6_ng7ZtusmbyM55Fzm5D70ylxuG35dJBa_p6E2-we3fvxIhSZD4gVJ3WkDtWBV5nKURs1ILiKRFjH3QtRZcXCLhJ5U78cQZ45c6dxzLtu3RaFH1Fa7GUwJ1rO7ydiK7My9ipdA91gEhPXE5EhusgWP9-yvtdc9XIYGgJiOlwc65hzDzEiyyy_hEEya-EU-xEHczszzy7-i8dP4rF0xYkchlZcLDtmi23zEAYsN1S1KypMKOBexxjLrkPHjfROHQNpVZ1pJXIVTvCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G-KZp_WpZpj6ZmjvgyIEoulF11GLLBNm8CAZS1I7lkRKzgF0iROxAPvqKrIBlq3ONJBwDnTp6y7INH-4Aj-g8UKMPhQYZ9JmQfYZc-76nqX_vZujxXhSGWXYUNPcQw3facjQtDqoejFc_BCkKu0WyrKdD7Fm40zSmo9lNFwO-x4bi1LHhcYixuw5vGVmJqpzmm2wOM3KbYUSOEpUAY6smei_VTFGfzc-_g24QZP814AlqOU6rMR-KCKeZzAfY-o4CAWn1hzC5XfwQZDq-lA8Hue6W4CnP4GrIH54_jOqpfGFH9tp1gybgMJrmvArOhK64IAFgq4ZdVGU2LmOO4yXDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B1cPpQ8Bj_r3uTF9ONj-xm5_vjcpwUYInt0AG2h-FlX98Fsua7dNb0HAtVDGUxiHfxTt19gmVckHB37zW9AQKRBBQQFye6V9m_EVYVYFKNKzHeuPmwEC5Rw-gjzS0jwoIA3Ga1LHVezHU3Y50HRth3wYbPOl9Mvso7dl_EKieuBxTpCltcoRlpnr33M-zJQ808e9d4-k-iLMtS95gnQXrOSV5ub4kHxH6-Swgxom2lA85TeYQc0tSYB5wNsRKfy6erBmrzvqHUX9jIXzi-xhv4FFO14HWzOWpdg50ssunCKq1ofhK4kpRyUXGOUlCLOFwUC9MCXQp9b_-4W7647GHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nqGJvGbKmlxq60tPJ681Gxmz-OTyPil_jQEwUGc77TDZN9OFa0SsrCOAjrbAyFmJfopAZialJQHKpExn5MyVWlEjGlXYfvmHtDzGiEvXlJ0UXCX6ZRd8ahgSpFoOhrcUSUcHVCjDchMWez0BV2PgyFr50M3q2HWr4JP68rF6XJdsb9Ozbt0Bg20FOKo8ZFTJ9jJfEKcZyV7wpDtKXgBmEQOWAEPX6ntFaBKLdkkv2V6waCd32VjIo2eTrs9ublAzCnRzoysMIi0CC5TkE8fdholkL43YCf_bA8yFAS1gSxQSjjAn7AED11NXM9o-5k0A22sZir8tk2cGkS7GLoP41w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hGZa5fvnVT2JzejYRJJZZxTL3aX_ekkFkHxsNPn5dQ09YmfrZfq29V8Hnovb2BOtT1uiuX26rRiQIRE7bdROgrxSWAwWCnmWQN2slcclboVN86_dwfAATR64bXL5yqm165_yRJgd-lVU08ytNyRwijlt_CLKmGyR-7V-VJduJbjJpWoEMmDA1P6a3yFnoKBuCGID9GhcVD4D1sAcLg29_xz5mygRfpRjdUaG1RQBoqqu7mbMCLXkNkUz-712iRae1H26Tq21QE_5ZvM3yOlpw-y18r_O-lAL3Itkjfro3jfUtZ_ZuoisnSEp8HHaNO2vPvpdxVZr2DuJbzC9StSv-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dA8akCyDv_WsoJvcsX5erJO9HZUePozJGxZn-cn25mWv6p5f79JPrqLWCwObUpsoYO9f-Vkr272uvdKLeymUJz_ApGhR1DFD1h49wXOjE5bGR59qFw_49u96Hf4Do8pwHYnxlosV9UlPaFpTxXO3NY0_4rtCWppT9GVjnhRmXDnQFlEqKYDG74s-eWihAg1ZOlf4jXaM8BGTG7KcsNS6T8VfBm_p63OlfhLAe-TcpFMx5JLA3XQbMQbpqkbtyWAIGllcjH_2Wsg2yjVaMrJJJMIMumc04o2VQqaveZzuzGCIbqjMkeZ8IkhaQq4iyRCQSsgURILRx48l6omX_vfHtQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💫
روایت دل‌های هم‌قدم
💫
✨
وقتی دل‌ها برای یک نیت خیر کنار هم قرار می‌گیرند، هر قدم می‌تواند بخشی از یک اتفاق بزرگ‌تر باشد.
🌱
#هیات_قرار
با همراهی شما مردم عزیز، هر روز با نذر و قربانی و توزیع گوشت قربانی، در مسیر حمایت از خانواده‌های حائز صلاحیت، این هم‌قدمی را ادامه می‌دهد.
گزارش اقدامات هیئت قرار را در کانال زیر ببینید
👇🏻
@Heyate_gharar
شما نیز میتوانید در این کار خیر سهیم باشید
👇🏻
5029087002135690</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/akhbarefori/689604" target="_blank">📅 21:21 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689602">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/549ad3efd5.mp4?token=WfDVrhA-E5pNQ4yTWVLM2HU3pa50MltfIvgCnJT4p0dnM0n5t2IeL_Zx7ZoOFeiADf9X4QVTSKiFroafxjz8GavKkdMMTxQ1m_EYW70j-Pb9BkQ8OGnENRUK5T5S6qFa0YUjgyzvTNfiaRxioIdQqKpdnOzl6wnphbzIfNWmQTqrDJ28khNu9_Kuaxs875BRwELiI0E3KDpnrOKnoeCEq6JXHOIyiK9SFUCjDGU2Xf2yBosFjp8WV6oa2uah_e7ZPNCkR49CScjDefkiDY_LRRvBWzZDaNUJT_LIMhJR_5seFHdYGInjqZKfg7DN-yJc5K0phFP-X0jO_xzxkO0i6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/549ad3efd5.mp4?token=WfDVrhA-E5pNQ4yTWVLM2HU3pa50MltfIvgCnJT4p0dnM0n5t2IeL_Zx7ZoOFeiADf9X4QVTSKiFroafxjz8GavKkdMMTxQ1m_EYW70j-Pb9BkQ8OGnENRUK5T5S6qFa0YUjgyzvTNfiaRxioIdQqKpdnOzl6wnphbzIfNWmQTqrDJ28khNu9_Kuaxs875BRwELiI0E3KDpnrOKnoeCEq6JXHOIyiK9SFUCjDGU2Xf2yBosFjp8WV6oa2uah_e7ZPNCkR49CScjDefkiDY_LRRvBWzZDaNUJT_LIMhJR_5seFHdYGInjqZKfg7DN-yJc5K0phFP-X0jO_xzxkO0i6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی شام، یه توپ گلف از آب درمیاد!
🐍
🏌️‍♂️
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/akhbarefori/689602" target="_blank">📅 21:07 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689601">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aHFO2lgUAcJ-GY8XTVOIp5JxpwtIpelAfV8FX2qBoWsxsJS4AOSN9SEkz_G3ykq2dGPxu0L_YyZe771hlU7WcVXqfSgnlyp_Rw_4P7-KyC0bfx8EJMrO1GNON5x1-E0aZL2Lz5RbxN1Z0MW1rgxtm1vgsuGj7Wm9EhXixiD0B6tI-9b325F4nZ61ikzT3rvghVgcyeAu_MdmvuaygwNMQtZHDMl_hfjZJms-QYBl9OoyxJ32tSxgMXqM2vEzGMghMpUDpRy4tSxjILumG86X2nWjB99h8RoNX7JBwmP9rT0sUpVhqdFDlKUocltT1oKj-B9ymvN15nd_Lc9M-StByw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فیلیمو، فیلمنت و نماوا به پزشکیان شکایت بردند: ساترا سینماگران را عاصی کرده!
🔹
از متن نامه انجمن وی‌او‌دی خطاب به رئیس‌جمهور:
🔹
استمرار وضعیت موجود در فرآیند تنظیم‌گری و صدور مجوزهای تولید و پخش از سوی ساترا، فعالیت حرفه‌ای، سرمایه‌گذاری و اشتغال بخش قابل‌توجهی از فعالان این حوزه را با اختلال و بلاتکلیفی مواجه کرده و به عاملی برای دلسردی و کوچ بسیاری از تولیدکنندگان به سوی شبکه‌های ماهواره‌ای، پلتفرم‌های خارجی و تولیدات زیرزمینی بدل شده است.
🔹
استفاده از برچسب‌هایی چون «سیاه‌نمایی، خشونت، ابتذال و…» و هجمه‌های برنامه‌ریزی‌شده شبه‌رسانه‌ای، خلاف واقع و خلاف اخلاق، در توصیف هنرمندان و محتواها و متعاقب آن، ارجاع اختلافات و پرونده‌های مرتبط با آثار فرهنگی ‌هنری به مراجع قضایی... نگرانی‌ها را تشدید کرده است.
🔹
نهاد مدعی تنظیم‌گری، به‌جای گفت‌وگو، اصلاح، تعامل حرفه‌ای و حل مسئله در سازوکارهای فرهنگی، مسیر سلیقه‌گرایی فردی، شکایت، حذف و تعطیلی صنعت پلتفرم‌های نمایش خانگی و سرگرمی مردم را با بهره‌گیری از مجاری قضایی و امنیتی ترجیح می‌دهد.
🔹
قطعاً انتظار ما حذف نظارت نیست؛ مطالبه ما نظارتی ضابطه‌مند، شفاف، پاسخ‌گو، فرهنگی و قابل‌پیش‌بینی است.
درخواست‌ها از رئیس‌جمهور:
1️⃣
تعیین مهلت و زمانبندی روشن و الزام‌آور برای بررسی درخواست‌ها و پاسخ‌گویی به آنها
2️⃣
ارائه پاسخ مکتوب و مستدل به تمامی درخواست‌ها
3️⃣
ایجاد سازوکاری روشن برای اعتراض و تجدیدنظر
4️⃣
فراهم کردن سازوکار گفت و گو و حل اختلافات، پیش از ارجاع به مراجع قضایی
5️⃣
بررسی آثار و تبعات اقتصادی، فرهنگی و اشتغالی ناشی از بلاتکلیفی پروژه‌ها در ساترا
@KhabarOnline_ir
|
Khabaronline.ir
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/akhbarefori/689601" target="_blank">📅 21:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689600">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e5df19509.mp4?token=h6vT_jjOL-kIM0h7nr_wAjL0wmMmpQBU5sq0osJdiWx0720ChrX6EcU9YTWQcwL3zU-7jHIUyGevHJk0JlltlkHrQa7NrGhxlKKKdrj46SITSiCd5x9wV29FSga7hvYemqTeBQr9DVFo2Irbae-lGHaCg9PbkChAEVlW9djkKqQwFufPUilEjX5G7BJlK_ccYyAkuuXQhZ5JLLTlbNSlhqhuoFQOt5in3aYP0v-EaIAIznhDbjD6aKHaGPKxHM5TyE1IrAtStUwgYwuLzL262lf72gcUNjk0xApJxoK_TfJpdsqBWX2I5OLHwxYGP7sbz-SpBW9xmAVgTLmPKsM_LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e5df19509.mp4?token=h6vT_jjOL-kIM0h7nr_wAjL0wmMmpQBU5sq0osJdiWx0720ChrX6EcU9YTWQcwL3zU-7jHIUyGevHJk0JlltlkHrQa7NrGhxlKKKdrj46SITSiCd5x9wV29FSga7hvYemqTeBQr9DVFo2Irbae-lGHaCg9PbkChAEVlW9djkKqQwFufPUilEjX5G7BJlK_ccYyAkuuXQhZ5JLLTlbNSlhqhuoFQOt5in3aYP0v-EaIAIznhDbjD6aKHaGPKxHM5TyE1IrAtStUwgYwuLzL262lf72gcUNjk0xApJxoK_TfJpdsqBWX2I5OLHwxYGP7sbz-SpBW9xmAVgTLmPKsM_LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از آفند قدرتمند، دقیق و هوشمندانۀ سپاه  علیه پایگاه‌های شرارت تروریست های آمریکایی در عملیات تنبیه متجاوز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/akhbarefori/689600" target="_blank">📅 20:58 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689599">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
یک ایده ساده که می‌تواند پول را در محله نگه دارد!
🔹
راه‌حل‌ می‌تواند در جایی باشد که شاید خیلی کمتر به آن توجه کنید.
جزئیات را در این ویدیو ببینید.
#چرخ_زندگی
@Tv_Fori</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/akhbarefori/689599" target="_blank">📅 20:57 · 22 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
