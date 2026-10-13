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
<img src="https://cdn1.telesco.pe/file/IeQgqEogaksF80WOKKXkerdwfUT4-8mIdB-1LEne5UztoflPwAaWgdO-8MKD-ECRpOt2Y82H81s05k1xfzvHFBOPD3k-t2cYNPJ4UNmIVKEvaoqN_E_6iYKhD8o0dOM5QVIg2LLzW9q9zfIIY1wKrt-TPk9wBSe2lD1UKJIuLkdRowR7MKpO8OgIhdoJ0u1r6ipMbQZuuXuU6wUTcMyaljMpd5dOdeyI9B-nFGdi4Rf_sSBCw7-IFT4MMJAxgkwEUtquou3dErfpBOfoHhWr40doVSKFT2SVQljCek2GTXFvUAYI-0hHW2g3IsMhw3-KrLJzRobgabTpNRxCmhOzkw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 97K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-21 22:53:43</div>
<hr>

<div class="tg-post" id="msg-2672">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DQtsOWPPzqCTbI_SK0gmj51_S-p4e43DgEi4-X76_QjMBSaoYENJ2PVtr1zNnjSqvAvuahx183N476FpnrTaXkrq0r_W2bPO5fLEqDXrBUK_nOOtyqu4N-1UyeH4o0xueBHex1nmWwRBeB25DuMNNLr3SSuO7bpxwBEsgeBu6a1taea9T9gYZaxhaZu2An0EqllU2BRTHUGc2cRZZDh2PJedu_utedjVGG8JORGAs2H72YY4xaq-skMwra3DlUUC0taERiwOY9FZz9oYiiw9cim_Y8ljIn4Vqf9-pAFiemRG508gaQP1lCP8BFK5i2ZkUB-7CTaxSJGoMhqL6fchVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلد مارشال محسن رضایی: در صورت ازسرگیری جنگ به کابل‌های اینترنت و دیتاسنترهای خاورمیانه حمله می‌کنیم /انتخاب
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/ircfspace/2672" target="_blank">📅 22:12 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2671">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZV3Ze2aDLSyQ3PHvd-dnqcUg8OyPjZMYlmDIHA5uEgge-qi2dAgTdGs9fmG7a3REmVeW-fByH-iqNRYs0bWi7PvN35xbuLNlCflyLYqUyNPLHChNP6BxmQsGTsX6GOFt_FVs9sqbBG8ME1WA9mHvgscN90qq1e101rTVGCG9x9Ls2Uj1RdV3clCtusEL5VA4K78Wg2tJwkyfI75KJJLoUtFcnEO1m5kaBaYpPEB9iJJw3_ywZOUgdHuIKYtTYQzZSZER5r1eFT396X1D9Oy39RFqKHB9kxDY7a9WEKO2WmjphEM7E8E9Fn91Gm2mKghSQiUIsqKLocdUptX2gIfHCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته‌ای که در زمینه
محدودیت
دسترسی ۵ پلتفرم رمزارز به خدمات برداشت غیرحضوری بانکی وجود دارد، اختلاف بر سر نحوه دسترسی نهادهای مسئول به اطلاعات کاربران و ضرورت مشخص‌ شدن هدف جمع‌آوری داده‌ها، حدود دسترسی به آن‌ها و مسئولیت حفاظت از این اطلاعات است.
پلتفرم‌های فعال در این حوزه پیش از این گفته‌اند که بخشی از فشارها و محدودیت‌های اعمال‌شده به پافشاری بر حفظ حریم خصوصی کاربران و خودداری از ارائه اطلاعات بدون شفاف‌ شدن شرایط دسترسی مربوط می‌شود. /زومیت
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/ircfspace/2671" target="_blank">📅 22:03 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2670">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rkLdcKMxcf6fQGaZwA9FxHSMsvOwxI42Kg_SxV1e9ibyCnns3hP7zU2bMgo8liWN0nEw-HQFB827pUHSJPPSNCJ7_BOUsOXecpsiKX5uzFhtxO5WuXWF2jsPICTUnAcD5qwnGsMUqq59JLpVSE0hhEpU-xk7VE8AF0ANdDxalAdjhlC7GLDE6gsh5o_zpjZUO91v2eZoXS0gPBGzTOg2mrjNxL01N7iBUYZye6JJcQ8PffjN26cBU2ESIJ5KgWOwZHiowNgND8AdfwV_PN3vPhPvljyjlN9sl5EhOaw1eYPoiBUliVLxMEBvuwQWZ0qPZYdZnPZ5U25JXzZAXPPlCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌بانک مرکزی تسویه ریالی ۵ صرافی رمزارز نوبیتکس، بیت‌پین، رمزینکس، ارزینجا و تترلند را به مدت ۳ روزه محدود کرد.
دلیل این تصمیم تخلف از ابلاغیه مربوط به API اعلام شده و می‌تواند فرایند برداشت و تسویه ریالی کاربران را با تأخیر مواجه کند. /شرق
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/ircfspace/2670" target="_blank">📅 21:59 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2669">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K3Xo0b9w2_wXo_y7IV6PQnypKusHvZJrVyEeSLL9sROUzvMPhgDbR_DhGJWPVJ6d_-ws0ecCBqYUKhx36iP4mVGghKSZit6SudbfM5nnzJizryAlVbEPupmQRx8_T6hWUtPb6a0najs0F1vw8Cyvxh5HaGwAKPKtniodfz9g-Gyg3thwMk1ZlYkhG3jV6EgJelm5KuzoFldEeySPm9uYZtY_tkb9S9wKKEw7ENxUylHwEUeUbKROFUtOpuVvMUnN-2DTypmBm7e6wa_Da_zlF18MrYI_2NgtPo-ekjVYZosAN9p_1XlQk77PO_-tZHF48ZmqTCQkeFogZoPrrcOM6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در آپدیت جدید از فیلترشکن متن‌باز و رایگان PyWarp که برای ویندوز، لینوکس و مک ارائه شده، امکانات بیشتری برای مدیریت اتصال از طریق وارپ لحاظ شده.
حالا می‌تونین بین پروتکل‌های وایرگارد و مسک سوییچ کنین، مسیر اتصال رو هوشمندانه‌تر مدیریت کنین و از تنظیمات پیشرفته برای سازگاری بهتر با شبکه‌های محدود استفاده کنین. امکان مدیریت حساب‌های شخصی و Zero Trust، مشاهده کیفیت شبکه و بررسی خودکار بروزرسانی‌ها هم در رابط کاربری جدید این‌برنامه قرار گرفته.
👉
github.com/saeedmasoudie/pywarp/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/ircfspace/2669" target="_blank">📅 21:52 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2668">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iNm7fcUNzJGV1aNdtHaBSHQVCkfDDw26vb3isSssnqk3mNbW9a1Mn5saoaqoNXOJyMel1Vyu2q-hv6_RnsEK5LWzCUKpx100oZyPpb6oZNMPcwWYlop1ZtDjwjjPdNvK1HId1XzW-Bi-5bmHwUvubpvQ9dHhMglRRZdyUbxvCYL-h3eVbGsZV_qKwE6pBjow9KF-pbqddoeyjdh2Kqb85nXs2qpS8-Y70V27QJnj85BJ51nX_odW-XGMj3QVGj4lg_QvHp4tDSuqS3wrTbsP0znjZ7JOF_U8sLy82iMCMxTsjbVeABQIYmFzvtkjvlKuVcX3QfIEBQoT7B17b2JUsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روی حماقت امثال شریعتمداری حساب باز شده!
حسین شریعتمداری مدیرمسئول روزنامه کیهان: آیا حق مسلم ما نیست که برای به زانو درآوردن و قطع نفس این جرثومه‌های پلیدی، مانع عبور کابل‌های اینترنتی از عمق آب‌های خلیج‌فارس و تنگه هرمز بشویم؟ کابل‌ها برایمان دست تکان می‌دهند و با هزار زبان می‌گویند چرا نقش ما را در این جنگ فراموش کرده‌اید؟ /اکوایران
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/ircfspace/2668" target="_blank">📅 21:44 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2667">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CPXzPMPW4-AyUkAE3womFefdk8DKAizxeURZoZmCBVtCHyWKr6eii3sHGyMNFfHDe5dreLUrH9HD6oj5VJa2P_u6PP-pLoge8aTpMFArMovJbO72-KxDXiVPJekInI2TbAbJPtnAFDpRNI8Hf0zmlpuR1t3fvi6g66jWFHcts329GWdPTJMKhn2X_ZYlLOu5-46nNK2vJlVl-7F7QNZaXY3LbNJ5xCTUukmWf_-B4kZW-M6ZksolxQopnVUVFt21m_UkKl3nvpdXeC7coTwcU_AwkVeZsn1gGnCRCLuEtJ8ZawA3byw_WcLSE-Zc-0fvdA8qSCRf8fEIUdSVK3UFDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه CLI ابزار متن‌باز و رایگان GNet برای ویندوز، لینوکس و مک منتشر شده. جی‌نت که قبلاً بعنوان یک اپلیکیشن اندرویدی شناخته می‌شد، حالا با نسخه خط فرمان، امکان اشتراک‌گذاری اتصال VPN با دستگاه‌های دیگه رو هم فراهم می‌کنه.
با GNet CLI می‌تونین سیستم خودتون رو به یک سرور پروکسی تبدیل کنین و اتصال VPN رو از طریق پروتکل‌های HTTP و SOCKS5 در اختیار دستگاه‌های دیگه قرار بدین. به این ترتیب، می‌تونین ترافیک گوشی، تبلت، تلویزیون هوشمند و سایر دستگاه‌ها رو از طریق اتصال VPN سیستم عبور بدین. این اشتراک‌گذاری از راه‌های مختلفی مثل وای‌فای، لن، هات‌اسپات، اتصال USB یا ... امکان‌پذیره.
👉
github.com/frank-vpl/gnet-cli/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/ircfspace/2667" target="_blank">📅 07:47 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2666">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bOE11UDgjEAEIwqdd6vYaMG3vzL4KHHcZ3plDf37UoxZ8OjWygshiL8xd2HGZmUMKFThA1EytgK82npBKiN3nvhGAOtMgR68Q664axrg5zf91hSexRs0qRht6JMQ0ez-rmMIcpLruh5FcUye6iKhq01gBnFVRyg_zd4uhnfrUe0s_u0nmYRD32b0BaHbij4v8Zt7wFwK7y81McskbShUtnyz9shEZD0tGI2T1vOxBwCVhOPMig9_eis3M7bCKHCNeumYhSXxFhIuaE5OhSxJXYOH0ZP-omoeiC8Lm7NPlwSgxc641s8ljkRA_YlEJAkbiLzu2mP41ekLY_KKuutMlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واشنگتن‌پست در گزارشی نوشته افرادی که از داخل ایران به ChatGPT دسترسی داشتن، با استفاده از هوش مصنوعی و هویت‌های جعلی، نزدیک به ۱۰۰ مقاله درباره جنگ ایران و آمریکا تولید کردن و تونستن بعضی از اون‌ها رو در رسانه‌های آمریکایی منتشر کنن!
این افراد خودشون رو نویسنده و تحلیلگر سیاسی معرفی می‌کردن و از ChatGPT برای نوشتن مقاله‌ها و حتی ایمیل زدن به سردبیرها کمک می‌گرفتن.
طبق گزارش OpenAI، هنوز مشخص نیست چه کسانی پشت این عملیات بودن و شواهدی هم ارائه نشده که نشون بده مستقیماً توسط جمهوری اسلامی هدایت شده. این ماجرا نشون میده هوش مصنوعی چطور می‌تونه برای فریب رسانه‌ها و انتشار محتوای ساختگی استفاده بشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/ircfspace/2666" target="_blank">📅 07:31 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2665">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/F1qLZn4t4NvzlchncjmaBhJQDR8gAxdVAdWtfYf66BOGkZ5p_B1ARW94NF74EbzE0WAt-wd93jOfbV8RziFwcySsvwwb4fnZKL1Qu8lvW0xxpsAcv4t8Hz6XSSgD3h8BpKlyo27z7D8fqYMz1bQTaDn9s580i5yIRIywhUmH2kGdGoHzZRkyXBwMTR6qdqHfoPLbDt2GRPb806E2cvWRJJrdOouE-NAeAUZZsUTnVjT3G4Or6Ry2TnCaOaajHExajnZFvVczLe3brDRvLdy6L_3NqOd4wQql23Clnoi0wTQBuzrs3tLXtf4XXXgOO3q6PWAvNrJrE6GMGK9YR4rf3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تانل WatTunnel یه اسکریپت متن‌باز و رایگانه که برای انتقال ترافیک بین سرور ایران و خارج طراحی شده. باهاش می‌تونین پورت‌های TCP و UDP رو از طریق یه تانل رمزنگاری‌شده منتقل کنین و اگر این پورت‌ها مختل شدن، ترافیک رو از طریق ICMP عبور میده.
این اسکریپت از روش‌های مختلفی مثل ICMP، TCP، UDP، TLS، WebSocket و gRPC پشتیبانی می‌کنه، امکان استفاده از کلودفلر رو در اختیارتون میذاره و مدیریت همزمان چند تانل، تغییر پورت بدون قطع اتصال، پشتیبانی از ICMP معکوس و داشبورد مانیتورینگ از قابلیت‌های دیگه‌ش هست.
👉
github.com/JohnWatsoon/WatTunnel/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/ircfspace/2665" target="_blank">📅 22:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2664">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M1nH7uuKka2IB8kTejr_64AvMtYrdjbB_CeeEHFM5C8v7pWczgJjoSyaIfdWpezkEnCr_l9R_ZGHdFxe2NGh-HG9icZDKsrQU3DQnD_qSe7Eo5NexzzqBeRD0RbXGQ90xN7Lg19Jyw7UOiQRY35OgpL8yUk628Mb2Ngc_3emkTEMNRwLQbXeSX6S8BaW_lJgT62YhRpaotSpPMZDgD4ozeIl9Yxni3kN0JYFOYuX17Z5UaCMj207T_eEBZpIzhdMFD15rbvs1Mp1gamPlHwIPJHKWoG1tjD9N6zMebwct96pU9DkLpP3pjqoa78OaQjIOEAuChWBaG_JZiRW2u8amQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون توسعه شبکه ملی اطلاعات وزارت قطع‌ارتباطات: اگر جنگ یا ناآرامی رخ دهد،
احتمال دارد بار دیگر شاهد قطع اینترنت باشیم
؛ اما مشخص نیست که این موضوع در چه سطحی انجام شود. /سیتنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/ircfspace/2664" target="_blank">📅 22:14 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2663">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EgbvxOw85TkLeBx84s2GN4jY9ytUA-UyvVQQ6u8JB24Q4eVkvEry9Mi1mfgfdTeTMea8mZxqLljiwNrUi7G_sUZkb86bYezsT2gFSepiNsQd28s13kd25rp0H0_UGxLrIW3m_1g6dLEaBTonIkUpwxZvFxQn-0ZbLJR_nr8FuCGAAOw6udFTwdGPc7JEcb6uIMUrLDHElgtvmcSz_ZqQImTWoXef4OJ_yYCSBs4RtmPvqUTUAauWxsXgubn05pIZFHzoz13cpRjzo-84yz8sJeI4KRoTR3rqkeMEET84xoH6h0UEF2_qG4QKLvpYy2Un1f0gT1a2qL-GD1_culkCSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اخیرا یک آسیب‌پذیری امنیتی مهم با شناسه CVE‌-2026-‌107181 در تلگرام دسکتاپ شناسایی شده، که باعث میشه در نسخه‌های پایین‌تر از ۷.۲.۹، با کلیک بر روی یک لینک مخرب خاص، امکان سرقت سشن و تصاحب کامل حساب کاربری تلگرام فراهم بشه.‌
تلگرام بی‌سروصدا این آسیب‌پذیری رو حدود ۳ هفته پیش در نسخه ۷.۲.۹ رفع کرده و لازمه حتما اپ دسکتاپ رو به آخرین نسخه بروزرسانی کنین.
👉
beaksec.github.io/posts/telegram-desktop-one-click-account-takeover
©
MilaDnu
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/ircfspace/2663" target="_blank">📅 22:08 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2662">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j8fd6wsNTzDrsgCrrbUvm3DiXIm2FiyYP9DYCz7eekHtoJCHiW2oD82P_O10-Gv6HWKrjmIhwO3sCIjsTcvz1XeF8F15PGJ3x5AGQjIClcBmwkRo0wZU0JruJXd5S9eSqhYORffh6lISanes6sRDp-hJgv3_BaBhUTECE11sCBmG2T6h0TvjC64DvoOGKygAl19M6t6ntCjEgIZ16fVFhLTlXYrFGQqygLb3ph7zmCU8xWgo0JhdJsI-VLdPvWxzXtpx73U1sU7inwCUQvqDol-OK-mFaewzbjlkK5pXgLk1IvUlIOqEuwaXL9lzQLrE2gq4Vij909_ZvqujWNJMLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنل NoRoot VPN یه ابزار متن‌باز و رایگان برای راه‌اندازی کانفیگ VLESS/XHTTP روی هاست‌های اشتراکی معمولیه، که فقط با PHP کار می‌کنه و برای نصب و راه‌اندازی به دسترسی روت، SSH یا باز کردن پورت عمومی نیاز نداره.
این پنل از هسته واقعی ایکس‌ری استفاده می‌کنه و ترافیک رو از طریق یه اندپوینت PHP عبور میده تا حتی روی هاست‌های محدود هم بشه با هزینه کم کانفیگ VPN ساخت و مدیریت کرد. اگرچه باید سراغ هاست خارج از ایران برین، اما این روش به معنای ناشناس‌بودن یا تضمین امنیت و حریم خصوصی نیست؛ پس بهتره برای مصارف شخصی و محدود ازش استفاده کنین و مراقب اطلاعات هویتی، آی‌پی و ردپاهایی باشین که ممکنه از طریق هاست یا سرویس‌دهنده قابل شناسایی باشن.
👉
github.com/mr-r0ot/NoRootVpn-Panel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/ircfspace/2662" target="_blank">📅 15:16 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2660">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RcvEajRPMLUE3NDYXvl3z8M4Ip935NEFh4ZTJy1tlNGFbMwe2Y7HThTEFwKJ_bneJalSdER5OgmUf5ZCCPupg7PZJ1vd5dtLxWfh8tAMXP1Q_vpjkt6P3UlM30-PTbuvGph-TC8DKb1-NO34ONiXEBzUuSrjJGGM53Q-ILmnxKUNi3zc33NJeTUqF_JhfTQ3y-k-aKFtcpxvC1XkWJq16vdBD_WTBT4lCXfbhlmbKZrQFjI5kAFajN-eU-vSw2JyrpNyTgqHrzQDwCJ_ajA9sb2mCnacdAalOAetlo_W1WdMG_D1XzhwyJmVEb5FRHqGQYDzDy7jzx2RYlgvRsHIOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس‌کوچه در مورد Jet VPN که بیش از یک میلیون بار از گوگل‌پلی دانلود شده، گفته معماری این فیلترشکن دارای آسیب‌پذیری‌های امنیتی، با شدت بالاست!
این گروه قبلا در مورد خطرات استفاده از JumpJump هم به دفعات هشدار داده بود.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/ircfspace/2660" target="_blank">📅 15:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2659">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k-MBZobXl5LHDIDaT2qD1npV_0vRCPmVXd2xTG0k-ywd2FfZHACc2u7yOef_BVMf-6azigdmbZe2jXGp_Aa4HF_ggvgvfWCI9TITl1tLZ1vvfJIYkmlHscyn4jnv-IiQXUtz6_B5bzrzbJj1nLp_-L9uHP93UBugt8AfmA0wFEniD73Y5EkICU5rZEGOZHEYXA_C1YYfTZDwe46IA67bM1Hu6PtC0EbJJ6n-Hk52nimUtaXhFg70V7k0sOsHwo9syrl_e_OJXNdRbYiamqUYyv6kcXlH8u3Utn5dL2_rwdeWNKuGWUjOoZ-gGFdISpBxhqAUXX4GKxjY40kKoFzjzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاونت توسعه بازرگانی وزارت صمت در نامه‌ای به پلتفرم‌های خرید و فروش آنلاین طلا، از آنها خواست اطلاعات کاربران و میزان طلای تعهدشده به کاربران را به‌صورت کامل و صحیح، در قالب لوح فشرده (CD) به این وزارتخانه ارسال کنند.
در شرایطی که شرکت‌ها برای حفاظت از داده‌های کاربران و زیرساخت‌های خود هزینه می‌کنند، مشخص نیست اطلاعات کاربران پس از انتقال روی CD چگونه محافظت خواهد شد؟ /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/ircfspace/2659" target="_blank">📅 14:56 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2658">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VrgWqFIzbbxboeJfDch_ZnZ3OkvPDU_lOnqaguCpV5WJfkLaUOQa8s8bSMNb3NZMaQbEacJrsVqcF6K7dniF8CYqHfE5LmQZHFOqNdazuxR1a_53WIUckQdiFy4Y3lsJ02GLY3eLwE92f8DAXyivvbXCc8QkwtKbnWy_lyI26-r_zhsrfvEnXWsY2rn1e0qJMTocHML-xaz8tLClGpgBk3243kPqGHG3CF6DzZ9nzQsMJ9bQylDxeA6g37jQXUOhaIQXP0XK0cfi9kHxtyAw4Wu-DG31HlY-QxP57mrMWc-zqFD8VRMgyyLe6kWVJzm8UNNvsq_wDnyIAkrJSwLHvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گروه Void Verge مدعی شده با توجه به تغییراتی که دارن توی شبکه ایجاد می‌کنن، اختلال‌هایی که روی اینترنت و همینطور اتصال VPNها دیده میشه و مهمتر از همه خبرهایی که به گوش میرسه،
شبکه زیرساخت برای قطع خیلی از پروتکل‌ها آماده شده و فقط منتظر مجوز برای اجراست
!
روش‌های مبتنی بر کلودفلر، ایکس‌ری، سایفون، DNS و حتی تور جزو روش‌های اصلی اتصال فعلی هستن که فینگرپرینت شدن. تجربه جنگ‌های اخیر هم نشون داده روش‌هایی که عمومی شدن، زودتر شناسایی و مسدود میشن.
این گروه معتقده در چنین شرایطی به جز استارلینک که البته دسترسی بهش محدودیت‌ها و چالش‌های خاص داره، به مرور باید پروتکل‌های ناشناخته و ایده‌محور جای روش‌های اتصال فعلی رو بگیرن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 75.8K · <a href="https://t.me/ircfspace/2658" target="_blank">📅 07:51 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2657">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Bb1imAeWI3V3tGr16iN6j2w0y4TF4oY-y8pfIEbKjMm9viuhSDiafUWOxgmVvzZ2PYhCrlG0yJoGjXOXNSCpDYBzWiKgAlmevAIiRE28ruEXxbVBQWelgeraXoqE254s9BatIakC27_eQmX8-01u2Qq_8k5Nn1OTmrL7KSm-vWQMlBwS7s-nG_Uxso94FesrVO8LNc7AJ9mpRvRQrpFCHYHy6nS6NX9bhSDkQ97AET84ZsXJt2aFFAbh3aj_v_ORCwlcovUPIiOfB_sAnsdhzsXeHQO12V6AeaH5KFgividJr9hVCOTHnicxlKEgD8odiShkSFwOhS4w2jtMkxoJ5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت متن‌باز و رایگان ZedSecure آپدیت جدیدی برای اندروید، ویندوز، لینوکس، مک و NixOS منتشر کرده. در این کلاینت از هسته‌هایی مثل سینگ‌باکس، ایکس‌ری، اسلیپ‌نت و شیروخورشید پشتیبانی میشه و در کنار پروتکل‌های DNS، امکان استفاده از OpenConnect (سیسکو)، IKEv2، OpenVPN و AmneziaWG فراهم شده.
همینطور OpenConnect روی دسکتاپ بصورت VPN سیستمی قابل استفاده هست و امکان اجرای زنجیره‌ای روش‌های اتصال مختلف اضافه شده؛ مثلاً میشه سایفون، تور یا SSH رو از طریق یک کانفیگ Xray اجرا کرد. روی اندروید هم قوانین مسیریابی میتونن بر اساس نوع شبکه (مثل وای‌فای، دیتای موبایل یا اترنت) تنظیم بشن و با تعویض شبکه، بصورت خودکار تغییر کنن.
👉
github.com/CluvexStudio/ZedSecure/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/ircfspace/2657" target="_blank">📅 20:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2656">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MXZ0xusb45PnttyczHAaEFXD-aGgSLLLoBWjdDZjpSL72jgXgSy_2bTZzYBDDeeeGEGrrrNTQ03qPeUdD783sTD-9bRU7msz2tgWkCL0qlIvSCor3ZldaaQzU9ZQ2YuRPSKLZkzOzv2hq3ldd1R4d7Po4lSXrD64GmOISQoCCsExKx_5xY3axMp922zl33D88ygRndURb9vt44EAbw4MHwMVaszm7Xk4CX4GTfsUAR6Jjc-KWLRhx3G8laIeBOoH6qJf6WkX8VjdS-KTNNIJxmhkrmL_pQrmYkqUYhcUG4JHH7epaRh95KHa49X56i4zx0UJx6cJXhC935eka59lHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بر اساس داده‌های رادار کلودفلر، از ۱۲ مهر یک ناهنجاری ترافیکی در ایران ثبت شده که همچنان ادامه داره. ترافیک اینترنت بعد از شروع این اختلال بطور محسوسی کاهش پیدا کرده و حوالی بامداد ۱۴ مهر به پایین‌ترین سطح خودش در این بازه رسیده، هرچند بعد از اون کمی بهبود داشته.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/ircfspace/2656" target="_blank">📅 20:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2655">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NU7rNvClzN475wWe3PlTO0u9FMYLrBmBZfbCrTmRaeFS7dRmD3W4pgf9_RMLeI4Cvee6XM69CMEcryDrdOA5iS1ryR2IotbZPYaHPRCmOUsWzqV4Rpf7gtACU3TCW1LW9tcBgfRxdkeZXhK2sATlFfg-NyHNwb75m6n6msK-RVN1INUmMYJvqsyVrHp57uqX9Mob8ey11eU-zuMcduhjDaJkL9M6gzz4HMyxueN2hymlDlk_wKHHw3ggNkFiDA498UsC6P3pQWlhlNpWKivcEUqpVc1nLykeAPo8S0m9M62nGjaZCZjMAgCcU_XkD27docFRaNCVGRbq_Mwb94c7Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه جمهوری اسلامی در واکنش به سرکوب اعتراض‌های دانش‌آموزی در فرانسه، سفیر اون کشور در تهران رو احضار کرده!
با در نظر گرفتن کشتار ده‌ها هزار نفر معترض دی‌ماه و ۸۸ روز قطع سراسری اینترنت در ایران، ممکنه فکر کنین طنز باشه، ولی منبع خبر تسنیم بود.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/ircfspace/2655" target="_blank">📅 19:55 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2654">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/O750OwEotWM3ZRP-wCqbMoTGO9GPQChN2t_zV6knBIPDxu_nYSbi7-Ccngwiys5uuNtSQVbWtuXxkTkGMk5a8xOWKNZBM0itdlUEspsO5pJl4AOYhp5SWyYHChy3uyuy-yczkcykHz1oo-seJKH0cGO6QtzWe2xouHjqDXLBIPiO8aujUKJaVLAtwcj67Q-_0kTPxgeoRwEDmVW3Hu9ryoddUkYWmvS12kFy2n_LVC9jUKXmVgKPiV9tGE1nMTZNG2nYT5Y4vqZ-jWYQYwYnEkeFYEY_n5mVBT7bmURiNphcJhS7HpM67FHsafzPRhEidyY-fyOytX9aPuLG9SazNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید از اسکنر متن‌باز و رایگان SenPai Scanner برای ویندوز، لینوکس، مک و اندروید منتشر شد، که توی این آپدیت قابلیت Anti-DPI اضافه شده و با تکه‌تکه کردن ClientHello (مشابه چیزی که در PattNG انجام میشه) امکان دور زدن بعضی از محدودیت‌های DPI رو فراهم می‌کنه.
حالت Gentle هم برای اینترنت‌هایی که وسط اسکن آیپی‌های تمیز کلودفلر قطع میشن اضافه شده و حالا می‌تونین آیپی، رنج یا دامنه رو مستقیماً وارد کنید و اسکن رو از فاز دوم ادامه بدید. امکان ذخیره اسکن و ادامه دادن اون بعد از قطعی هم اضافه شده.
👉
github.com/MatinSenPai/SenPaiScanner/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/ircfspace/2654" target="_blank">📅 19:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2653">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">شستا ۱۰۰ درصد سهام رایتل و ۵ کرسی مدیریتی این شرکت را به مزایده گذاشت. قیمت پایه واگذاری ۱۳۰ هزار میلیارد تومان تعیین شده که با نرخ امروز دلار آزاد، تقریبا معادل ۴۸۳ میلیون دلار است. فروش به‌صورت نقدی و از طریق مزایده دومرحله‌ای انجام می‌شود.
©
stup360
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/ircfspace/2653" target="_blank">📅 19:38 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2652">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dq6w9MskrRP5mz2u1CdGvPyeR8jsp7dTnZQIZOVMrVHIq9CTg1hkXqizvJk13q-VlanyNKN0AIiqqH2xwp0pcUZthfSQgevjHnEU2WRm_4E8T3cgQn6Q0cWKQghH_fqVKB7lrmvUvqJo0XdCenYZX0ThFdyiCUNoHwKVJIscLvliZ4cEflwnJESpC-bLUfCxD7G-2Hy19yCJYpR1qWX5Dd7cn9LxTHfj72KgONuRVpkkvMQCviXxkqYNxg08Oee1808emwVkaI3_yJX8rZKyWGoiVEj1tp1BD3-ydVnPoW4q92Ym6-l_5loY7spXjG7n46GtWVBhLJZPSl0oRWG4Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پترنیها در تحلیل وضعیت فیلترینگ ایران، جمع‌بندی روش‌های فعلی اتصال به اینترنت آزاد از طریق کلودفلر روی فایروال همراه اول و ایرانسل رو منتشر کرده.
بر اساس این جمع‌بندی، روی فایروال همراه اول میشه برای اتصال به CDN یا Worker از روش ECH با یک IP مناسب استفاده کرد. استفاده از IPv6 هم یکی دیگه از روش‌های فعلیه که بسته به فیلتر بودن یا نبودن دامنه، تنظیمات متفاوتی برای finalMask داره. برای WARP هم میشه از متد WARP-in-WARP در اتر روی IPv6 استفاده کرد و با اسکن، IP مناسب رو پیدا کرد.
روی فایروال ایرانسل، برای CDN و Worker میشه از متد F&F استفاده کرد که نیاز به تنظیمات مشخصی برای finalMask، cipherSuites و فینگرپرینت داره. WARP هم روی این فایروال قابل استفاده هست و محدودیتی برای نوع IP وجود نداره. علاوه بر این، روش MASQUE/H2 با اسکن IP و تنظیمات مشخصی برای فینگرپرینت و finalMask می‌تونه برای اتصال به کلودفلر از طریق هسته اتر مورد استفاده قرار بگیره.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/ircfspace/2652" target="_blank">📅 23:57 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2651">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HyCxs5M7U8n4yMHxUtP44an8rnoJb9U-7k74phKo0xeYHX9IHfES5Aj6e7ZymENMAkxn49f7j_V8zpK32PsZnV4a2N-C23h4GVQPlRGdKh-T1BPklPIwBVy-iAPhC7HyvuEorirGWiHHIEQUUWLxjqAsNb0pn1gP1FL22rl50YuFroQa3Wxd7iP4gUKCxvRr7UF0E124peMwwsGsVXyNkCpdGxPC_fvaXrH0kw5pkuRrTOxX8rHSnhnJ6-5Vc6Vdeti02Q8OHX5uA-k2dCEIRdHmHSNuBrH25TKAxuKdD5PABVaJkpLi6kIHXHGBw6NZKdrz_fedvERWoJ2J5_1lIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن دیفیکس توی جدیدترین بروزرسانی خودش قابلیت تانل‌کردن کل سیستم رو بصورت آزمایشی برای ویندوز و لینوکس اضافه کرده.
در این بروزرسانی عملکرد کلی تانل بهبود پیدا کرده، مشکل نمایش پرچم کشور محل اتصال رفع شده و چند ایراد جزئی برطرف شدن. این نسخه درحال حاضر روی گیت‌هاب و گوگل‌پلی منتشر شده و بروزرسانی مایکروسافت‌استور و اپل‌استور هم بعد از تکمیل ریویو، در دسترس عموم قرار می‌گیرن.
👉
defyxvpn.com/download
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/ircfspace/2651" target="_blank">📅 23:34 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2650">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lNulvC8vFXbQeWBlFZg0IQ_4VTYqmCZKArM7ob_qEiWrXSAbGfvIW8PDS6OEKouxYytGGtoC1QqS678hwRekt9GgdPzG1ctODNJIbssTDPOpFfcKFMvhk9uspC4k4JC1nnHrN5m2rIGy4y5TZqou9TtF_SoqSW2X-PK6KyLWLt5s5umhyRfrrvxjQdusyRvk2I89F98O4k2Pwix3WhQaixVxfALJmBtHp3wuUS5Dy0HlWICvYRXU67DRoqVN-ZjatPAqiXwbW7OEtLuQO-S8N9sJWNK-tzxddnLJKYZdbltcITOIbR1F7JEgJrM5lZKc8CPyAaOSjo5OYCvbehKwjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای "قطع اینترنت کل کشور فرانسه به‌دلیل اعتراضات دانش‌آموزی" فیک‌نیوزه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/ircfspace/2650" target="_blank">📅 18:02 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2649">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/i1nXYMQ2UqMEXWCEfvXO6eWwHDKcCeshL1paHkG5SNnGX3CBH6QKGRaMBwiOYwEEXHjXl-PT6KzmLMb1xMGsHG4ghS6YBKpCBCFUlJIhaLrXey8WGoXyYvzXBpcvbmCLKI04zccsYm8zMywD5QMR7d-WZYnlTBu5Q7MrYMjmKFQvywY73GyM_Z9LgUrd8R61vXANdrYR_pLMm9PBw1zdYp-Mxr8u0HBVlxQiWb7rwU5XFj3CgioLGEU9joBW5Qj0NEQ6tyWW2UvlOCaxKmExJuZjmtEngChnv2CiWhKsZZZJ9JDL4lYofudCZMn1H1hiCk312zKZqzNLgINBQutJKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی در جریان اعتراضات دی‌ماه تونست با جمینگ و GPS spoofing روی
استارلینک
اختلال ایجاد کنه و حتی تو بعضی مناطق کیفیت اتصال رو به‌شدت پایین بیاره، اما اینکه بتونه استارلینک رو کلاً از کار بندازه، دور از واقعیته!
اسناد ITU نشون میدن که با وجود این اختلالات، ترمینال‌های استارلینک همچنان تونستن به اینترنت بین‌المللی وصل بشن. حتی راهکارهایی که SpaceX برای مقابله با این اختلالات اعمال کرد، باعث شده سرویس در بعضی مناطق دوباره پایدارتر بشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/ircfspace/2649" target="_blank">📅 17:53 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2648">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vco74nvQ0CzG7u8a_pdcapGjKDks4sJqpdmlpowQM4aTzXCHn5jKXlG9NeTD_q_NQcE0XmwoP_MSZYhS5CSh-2_d_S99ZmBJKxlXqkfXehcfxJy02UfxY97prtRZfGW7MillCIY9YKoYMQqEa0MaZYloaoD8xpVacaxb-ixoIOiCKa8EB9X0UKQ9E9ckcp4QL27P_JdC6RJ8f3piy4bJkuqU2VZRx9LoUArY-qWJE7ngzE2XGdbPsrdEbeqiDoh6WrpFChvgwEoSo6t6_djg1wk4Tbnwyc-djI1vkehM7CDmNtRA1bzFiKXrVXVua7G0-b1I1vaR8EvkuHfCzEaI_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس پلیس امنیت اقتصادی فراجا: هر سایتی که اقدام به اعلام قیمت‌های کاذب ارز کند، باید بداند که برخورد قضایی و پلیسی با آن به‌طور جدی انجام خواهد شد. /انتخاب
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/ircfspace/2648" target="_blank">📅 17:45 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2647">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/igdEBONpOkXBjW2MqRSBT3X-WXpRvltiA2H-M6fAh2Azm22v5mqvTwU6E-fmD8KRIsztkn9_Y5AHvE3WnnE0117MtBhWEnSnhicQK6c6QjMp_g5RyCXK0_0HclpfbbaDtYNwnw2OOazg3DewxhIbwHT8FAk54K2zRcty4LD1KOU-pj4VI1wK8GbroFHOpNsnUr4mGZvQuIMeOeVxHIh5IY41lv70S1263RqJS1eCDBRNnn2UgGY6F6YA6youvHIE-iyxwcdpC1kAHa_rjtHt8SnZ9b5cEA2UIOZv5RMGglzM2mgW1Obrk8IMWkyoj5aS2ZtVZJRoCi6wcNYVdikOYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت جدید از فیلترشکن متن‌باز و رایگان Aether-GUI با آپدیت هسته اتر به جدیدترین نسخه و اضافه‌شدن متدهای اتصال سایفون، تور و مسک‌این‌مسک برای ویندوز، لینوکس و مک در دسترس قرار گرفت.
👉
github.com/MatinSenPai/Aether-GUI/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/ircfspace/2647" target="_blank">📅 17:41 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2646">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GPvSdKdSDTSClij692C-yLt3dPS1DAaVW-si0F76FCzmZVQyFbp94TA1A1O2KH2LKoIVUXNUsQyMWFIU22qfqRGRZ6SYa1smzbdyU6dfYECCk382LQH9yeSPEVNrY9h2TAbg5ANcuj8j2J7YYH-9EIbiHvHChS_Slva1hxcA0yelSSc4zBrq1C8gDAjuqyF8WMUkYNf-uM2HPNFwGFzZMiuH42EkKOU9eNTR0fRYiCSYhbjWsGSCs0FxWIx_nZhXCkuUEnk41lLOy55nqoj4mTApzxi4rTxDdQCzvDD2NaESE4f5T81-_M387W3f6aIQTgJj83lJZU7UtgClxwEcyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس مرکز ملی فضای مجازی گفت: ایران برای اولین بار توانست با موفقیت پایانه‌های استارلینک را در جریانات دی‌ماه سال گذشته از کار بیندازد. /عصرایران
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/ircfspace/2646" target="_blank">📅 17:35 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2645">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bm-fvldQ1-EG_HxZs-Gc4c0dyhxFrD2hEunjRKQMV1DyFfOcoFCBDCm3Ti-J5zB_oo0ePIPeu_yR16VmwrNP6JuY3No2iVZfcqTIXbp0v0e4Ewxi7Ic89Y7mZDABfo8E3zt7YcA2KsSHqQjUV5RNmfJtflZG7p6w-JKLoaXCAo-LkkGNBAkMbHK62WnSGAOLZq4CGuk09tOyjSZKbT0hC9oMYvxZc3s_j-Me72J_EXHItlmDtf-_lOWRGrytYJoWWWVlGtvx9tdbdufifrPEdNXDPsfjykt8ODdUVLKbXFLxLSFzYePXpnSmXHdnzJEH8qoP-GUGMGtDCyYtnT8fSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زومیت در گزارشی نوشته که در حال حاضر دو راه رایج برای دانلود فیلترشکن JumpJump وجود داره، که یکی از گوگل‌پلی و دیگری در گروه‌های تلگرامی هست؛ اما بررسی کارشناس‌های امنیت سایبری نشون میده هر کدوم از این جامپ‌جامپ‌هارو دانلود کرده باشین باز هم در خطر هستین. فقط خطر یکی بیشتر و اون یکی کمتره!
جامپ‌جامپی که از گوگل‌پلی دانلود نشده احتمالا یک فیلترشکن دستکاری‌شده هست و به نظر می‌رسه این فایل یک exploit یا آسیب‌پذیری قابل سوءاستفاده داره که می‌تونه دسترسی root در اندروید بگیره و رد پای دولت‌ها در نسخه دستکاری شده دیده میشه.
حتی اگر نسخه کرک‌شده رو دانلود نکرده باشین، بازم برنامه اصلی دسترسی‌های نامتعارفی از دستگاه می‌گیره که نشون‌دهنده ناامن بودن این فیلترشکنه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/ircfspace/2645" target="_blank">📅 17:28 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2644">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vVNQNAQyncyv_Yy_VewKNetl5qj_9zxbLrD1BxqXWH9atSLN1vDdInMDt7dn611fD6_6GBKQ6S-nLoOAwNo9qAzQ3mtkDAP_oq36bBmYhEskmZzP5FeeGR7Xd4ZnK1xeaBLsNHW5sjyjZph_lSeUb5_rgjyYmL9NnfJ2r7JGs4sWH-DCR5Ro10WfFdlVeLLww2c3XkPuCtfPB8HkKfkFxAUcZhdITlRQ-1z0E-UMVxW9VdXCrcXWgs3FU-AYM1FuE2FR8jXKeTtgA5KBjm4H8AzihCKhJWaZCWUu9yFegcuUr8YZvm0eaFwnLIBG3tCFmJyfOUZSkuZbJkDZSCeUUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید از اپ سایفون چندروزه روی اپل‌استور در دسترس قرار گرفته.
👉
apps.apple.com/us/app/psiphon-vpn-secure-access/id1276263909
💡
play.google.com/store/apps/details?id=com.psiphon3
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/ircfspace/2644" target="_blank">📅 23:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2643">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/F_vCQinDuLnVE9CbF77OxSUuzPqYt13OqcHX6iBfSoRnG1xKvLbdTezhTNTGCuaZTrYixdZ4srV2FeXn30wogC6boG9q6qlY5OHCI9tiP_99WHhzn4tT1RaIcGB-JVfddPM99NenpBCosy04gj2F4vhkT5PzeXGe_kVQ52VkO6blca8KSxJwc3q6Khexs9pjp-HInknP-FpjcBhs7L680fHf_QAlquouu6WWK8Zt-dW-AWaRtHtS6_hfdxjYpL74hbjJm9EUcpLPAm3GRhEjuRO9mhXpXWEadaPQpyRFzWuPfwAVoVVEzpbL7wPHLli54cADJvetbVS1nx6L44u-2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق آمار رادار کلودفلر، از ۲ روز گذشته ترافیک ایران به کلودفلر به شدت کمتر شده. اکثر کانفیگ‌ها و اتصالات به کلودفلر مثل وبسوکت و xHttp مختل شدن، فرگمنت روی همراه اول و مخابرات بسته شده و روی ایرانسل ضعیف کار میکنه؛ همینطور پروتکل UDP به سمت کلودفلر کلاً بلاک شده و اکثر رنج آیپی‌های هتزنر و OVH از بیخ بلاک شدن.
©
mahsanet
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/ircfspace/2643" target="_blank">📅 23:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2642">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WKnkvBe5E6AXMbTa0RaOeNoGoyvRaXLz8hiaicHQStuknjwmFbLj4VOGWoK5HDGYtxYFI9fGY8KNRoFWglOhqm7mFueyBJv6EeQLpUg12ElYShxYL_MbkOMmZtwPpInQTHaxp7aVXeUR8EFKGYGpED5ixvKxatxKZAUAJv4OiFVIbKM5iLn4DQN9oUHcZqWjiifX6Oa3vFqnybfP4GLdSdSOPfP9yfFaOSyJlqf2ug4TAOzlJTdXz1a5zfAwMqE83nxMyUXHrBD6zsIN9uCioWYmU2Ukk681h_OZkAT_Z2lgfAtTP9CnPq4jLOAOde9nj9UGAQlQhruk6W37dvI0xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نحوه استفاده از برنامه‌های PattN و PattNG برای دورزدن فیلترینگ
📽
youtube.com/watch?v=CnEQipAJ2hE
💡
t.me/ircf_toolbox/25
©
𝐀𝐥𝐢
👉
github.com/patterniha/PattNG/releases
👉
github.com/patterniha/PattN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/ircfspace/2642" target="_blank">📅 23:19 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2640">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FKb9afPyUqV28Mj3hTtqxODaODQ5MvPi149jCG_SPHdf6hRXIvJm6VYkecTeh7RkQW2C3lOFIMR4WNCLcMqBM96EabefbvNHvTkohBYNWAC7f4jBGBKYTxy3xs2L5DcoaM9Rq6shkRnuN1CsCetJUrfKlS0JCoe71HKFqRHAuw-2aDIkfgh5qDfF_A8HZcQG6n1XTYm51-0wlw6o5ugphUektet_k4HnMk4KqvViRRUD0aXOo-Bjhos5EqfN0FXA8NS3wzFom3wTygxsBI2aswfeadrFx5tp9DGXPMsYsRZvhi0eDJOzhGGMRKlT-Ezy4D3Z6UO-bsxm6QGfPGNR1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت جدید از هسته Aether مشکل برگشت آیپی ایران در متد اتصال Gool رو برطرف کرده و محدودیت اخیر دریافت کلید وارپ و مسک رو روی بعضی از اینترنت‌ها دور زده.
اگه H2 روی سرویس دهنده‌هایی نظیر ایرانسل به هردلیلی ایراد داشت، میتونین طبق داکیومنت از فلگ فرگمنت استفاده کنین.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/ircfspace/2640" target="_blank">📅 23:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2639">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sg_4sHlQ6QtffkJPPwTWa8gLuDgyRVkOrqF9XhdD_41IueIzNk6vM2V4_IiK3sEC9_mP3fhGhLdsSwtdVzFBUuZi6zcspAnoHJBLoY2muHHP0Yg5z83eokd5dzHz8oobXbZCabeLeskMlbkVFfjFUasbQiAEY5ibaAjPhdqFJrZt2TOq7ItxPjS8Jw_MzfLPty2JwrdsOIkQugD24Bqh_hAl5rl-lwr2IXQUQhYRS79aFW2VYg7PjuJD-MThJH9fej4081BYWn12T53Vr8Im_6qEocorXujAc5mCMbKeC8rd-hpAJcAgW7kLnVGThweQUpzoQFgnodLWmPQwAVxVGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه ۱۸ از فیلترشکن اندرویدی MahsaNG منتشر شده و توی این نسخه هسته Xray مهسا آپدیت شده و پشتیبانی از پروتکل MASQUE رو اضافه کردن.
برای وایرگارد و مسک حالا یک اسکنر IP اختصاصی در دسترسه که از نویز و پورت پشتیبانی می‌کنه و میشه کانفیگ‌های این دو پروتکل رو با کلید Auto ساخت. امکان بکاپ از کانفیگ‌های شخصی، صفحه پروکسی تلگرام برای کپی و تست سریع پروکسی‌ها و بهبود Fragment و حالت Auto هم اضافه شدن.
چند نویز جدید برای عبور از فیلترینگ UDP، کانفیگ‌های جدید یوتیوب و پشتیبانی از Cipher Suite برای افزایش سرعت آپلود در متدهای پترنیها به این نسخه اضافه شده. FinalMask حالا روی پروتکل‌های جدید MASQUE و Hysteria در دسترسه و علاوه بر رفع یک سری از مشکلات، ابزار زنجیره‌ساز کانفیگ هم از Fragment، Hysteria و MASQUE پشتیبانی می‌کنه.
👉
github.com/GFW-knocker/MahsaNG/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/ircfspace/2639" target="_blank">📅 08:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2638">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BDvWe454PniS3q0uhR3UrpPn3Qbw-TK490aIz7SPjeSwjiq_-UeIjwSQCJbUEDwjeSTA1BWdSU7W5Vui-A6tGoUJGZsHlEkd5PtFDcQpqvtJh7KRxAYvj0cOf7wYt9T-pN4JMDNA6A4jeggVerufI7MzkK8ejUGJWjOyLXmKLASr3b-BTk3D16D2j-oAW_Jud4LFhE59-B3nk1mQs9XOfddV86FFHhREEsws3gxJPvt0OI0DnnBS_NMlEN2TZZvGkNivD57m2iTA_tnd19t7qRmZrPESfcLZfsdA0SK0NA9ewj8RqNYTJTpIcbYMC5GaPDPbkJcdapvWvClpB22dcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپل از نسخه iOS ۱۸.۱ قابلیتی گذاشته که اگه آیفون ۷۲ ساعت آنلاک نشه، خودش ری‌استارت میشه. این کار باعث میشه اطلاعات گوشی دوباره وارد حالت محافظت‌شده‌تری بشه و ابزارهای فورنزیک مثل GrayKey سخت‌تر بتونن قفل گوشی رو باز کنن.
حالا شرکت Magnet Forensics که سازنده GrayKey هست، ظاهراً راهی پیدا کرده که قبل از این ری‌استارت خودکار، گوشی رو در همون وضعیت نگه داره تا مأموران بتونن فرصت بیشتری برای استخراج اطلاعات داشته باشن. این قابلیت با نام GrayKey Preserve و همچنین Evidence Preservation Mode معرفی شده. البته فعلاً این موضوع بر اساس یک ویدیوی تبلیغاتی لو رفته از شرکت مطرح شده و جزئیات فنی روش منتشر نشده. در واقع جنگ بین اپل و ابزارهای بازکردن قفل گوشی همچنان ادامه داره.
ناگفته نمونه مأموران توی ایران برای باز کردن قفل گوشی بازداشت‌شده‌ها، نیازی به GrayKey و این ابزارها ندارن؛ زور و تهدید راه ساده‌تر و دم‌دست‌تریه واسشون!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/ircfspace/2638" target="_blank">📅 19:42 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2637">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">پروژه Nexora یک پنل برای مدیریت چندسروری VPN هست، که تا ۲۵ کاربر و ۱ نود رو بدون نیاز به لایسنس و با تمام امکانات پنل در اختیارتون میذاره و میتونه برای مصارف شخصی یا گروه دوستان یا خانواده قابل استفاده باشه.
نکسورا مدیریت کاربران، نودها، اشتراک‌ها و پروتکل‌ها رو از داخل یک پنل انجام میده و از پروتکل‌هایی مثل VLESS با REALITY، XHTTP و Encryption، VMess، Trojan، Shadowsocks، Hysteria2، TUIC، AnyTLS، Naive، ShadowTLS، Snell، Mieru، MTProxy و SSH پشتیبانی می‌کنه؛ در کنارش پروتکل‌های کلاسیک VPN مثل OpenVPN، OpenConnect و WireGuard هم قابل استفاده هستن.
از قابلیت‌های دیگه Nexora میشه به تانل بین نودها، پشتیبانی از CDN و چند آدرس برای هر نود، همگام‌سازی بدون نیاز به ری‌استارت، Rule-set برای مدیریت ترافیک، مسدودسازی تورنت، محدودیت دستگاه بر اساس HWID و انجام عملیات گروهی روی کاربران اشاره کرد.
برای مدیریت و نگهداری پنل هم امکاناتی مثل احراز هویت دوعاملی، بکاپ رمزنگاری‌شده، بروزرسانی خودکار و Webhook در نظر گرفته شده، امکان مهاجرت از پنل‌هایی مثل S-UI، 3X-UI، X-UI، Marzban، PasarGuard، Hiddify، Marzneshin و Remnawave رو داره و از زبان‌های انگلیسی، فارسی، روسی و چینی پشتیبانی می‌کنه.
👉
github.com/nexora-vpn/panel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/ircfspace/2637" target="_blank">📅 19:26 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2635">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DxCx-uvTe9k2lLHVRskUyFVjCb0jdftjHXsChaMtfByR_idqJ5J5vnNrUtP1vel1tqQk6MwuIi_GEDWFOqMcaJVnu-Mj6TOMBR8vbSNtrbGdkTQkfQt_7_HnOu8fI8PuMJMbRJqohnXgYrPdoAHwL0qv_OuMA-8k4rw7hxdjANrLdr_KG9QTISz6CF5bE6RvyFlqYCcUQfyzm6Dh9xGxcIdnZ2H4qcXo_Epmy1xHXIvPyIQwwn_WNp9TBXLAi0yJjWNwHFwjy1wuqQ_SiAwYuAWR0i3ckSiVITMj_X1-aZ_xMk3yaAGfYCmfVkiUlh7Aq_NvygZTEn196vukt1Hv3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حساب رسمی مایکروسافت در ایکس با بیش از ۱۳ میلیون دنبال‌کننده هک شد و مهاجما از اون برای تبلیغ یک رمزارز جعلی با نام $Clippy استفاده کردن.
هنوز مشخص نیست چطور به حساب دسترسی پیدا کردن و تحقیقات ادامه داره. مایکروسافت هم اعلام کرده هیچ ارتباطی با این رمزارز نداره و پیگیر اقدامات قانونیه.
©
theverge
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/ircfspace/2635" target="_blank">📅 19:09 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2634">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nRJFi3isdvc4v_RWBAmjXw1kLFfk-kxYkqh-jTbPKYdWCqUifPvjN9iyGvL-aTPw5cLOiAH64rszaDdOU5YI-AA-7LZUNVGQPDGE2oQ9ryAZ-nXsEfbl3UUXgBz_o7lSPwGpPYVkoKoYXPfO2gC9VIE0HJ5NMNE_A1mM4JQAN7R3ugsVaYgLoLVMBt2-2UIcizDBw0KJrBSmp0N6rxIGAcWq-uFPJxKF4mosKI2BDYkl9knRm8JMx97OH9qLuPNYIoEX_8LwFIbdTQsamz5hkUHE9aUyz6Z8RYoda_F9p3n0CxcRcrcEnZx3VsdW4EJgxNFAXrDvZixciIUrjuyhow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر میخواد تبدیل به یک مرجع عمومی صدور گواهی دیجیتال (CA) بشه و در قدم بعد، گواهی‌های جدیدی به اسم Merkle Tree Certificates رو هم در مقیاس بالا صادر کنه.
هدف اصلی این کار آماده‌کردن زیرساخت وب برای دوران کامپیوترهای کوانتومیه؛ چون الگوریتم‌های فعلی مثل RSA و ECC در برابر کامپیوترهای کوانتومی قدرتمند آسیب‌پذیر میشن. MTCها کمک می‌کنن گواهی‌های پساکوانتومی بدون اینکه حجم و فشار رمزنگاری روی اینترنت به شکل شدیدی زیاد بشه، قابل استفاده باشن. کلودفلر گفته هدفش اینه که این گواهی‌ها رو از اوایل ۲۰۲۷ وارد محیط عملیاتی کنه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/ircfspace/2634" target="_blank">📅 18:57 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2633">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/egrr5ifXJkbnjQEd5qoFv5XHnmr5K5NPvDMm1qis96VKxTKdm7mcA0VDa1IGPawpqqAuJ0sjjzzF1TkxBKgAG8bqtPe1WqdGETK_Cb79CSN6Hqw8eu60DCH68_ZgjvZbZmCxiapOlgL8eQTodSiQEhTP0r4WdtTco1dW_pdljK97sAVqhXH6WwP2_S-dYlETNOKf0tQSMWgyMF1LAhdMBEuoSxw6YNrd2RA-W9tHiI79JDJNWR5j2yyT3g7ge1BM_RtP5T938l2yM7-NzBQtLMHRh_02pgDsTY6ssA4Sg-gDFjpo51oZLDD63Wcf4q2jXqxswMBFiQxZC0H7PMxpsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه از TeamViewer استفاده می‌کنین، چند آسیب‌پذیری امنیتی با شدت بالا پیدا شده که در بعضی شرایط می‌تونه به مهاجم اجازه دسترسی غیرمجاز و حتی اجرای کد روی سیستم رو بده، که مهمترین مورد CVE-2026-92370 با امتیاز ۸.۸ هست.
فعلاً TeamViewer گفته شواهدی از سوءاستفاده فعال یا انتشار کد اکسپلویت عمومی برای این آسیب‌پذیری‌ها ندیده، اما در نسخه ۱۵.۸۲ این مشکلات رو برطرف کردن و لازمه آپدیت کنید.
©
bleepingcomputer
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/ircfspace/2633" target="_blank">📅 19:03 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2632">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aym1ie-E5CysgIorXKXRfHvTbi5xqR3rflmFGA08KlMc3yIEtUleG97H0cJCJxk8swlB-ad9iiwB7St2jf8NFiYG7clGQgis814M5XAJ_Py78CUG839w9u7VR2Seiyl9DdG1QJdsDTWSXCsxzn3pvGfakwYcVdZM62yGOThJBV41ablwOTXgJtFbfXeL3kU7_BL1Bx_iCrkJW6THe22gt6RcMzL0Ypv2Dx4zbK1PTW68iYtNSJI_02UldLBH5NIV_1qbUvIXfWPYKEMBYy0J1bQ4AL63Y_S7L6PKLoSFAJgd9UbitOEYpVimVmoD2D6pJPEaAlDnPbbaOSp8NigBVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ج.ا در سال ۲۰۲۶ رسیده به راهکار ماه‌های پایانی حکومت قذافی در برخورد با مخالفان: قطع سراسری برق!
©
ArminSoleimany
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/ircfspace/2632" target="_blank">📅 18:56 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2631">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QtOU25lq6FTftBC7SBo5tgzzmVquU29VNxwi5RhQVxGOk6bJa1SRUAGO4pPrbM6CHbhU0qTwHpTmfhd7278qJhhDTdsHiK7PWX_EH04LjWNytjhkYklnRLAjprNU-6_MKmOQOytBMN6ldAGMUg-NsLQhjRgTE41hp-xLeQCFh1_hpG_mtz-TA-dkHaTJvy4vJzV5vpYfWW96pAnUk_uupxCteJ1ILmki_gRpvntm2sKTNQtrY4xhMjGOWdqk1Fsrj09ZR1Qfdp2ZTOfMJv7qswUuNplSSI4EpolVOX2xx92owA0M8qEyTVb5z96Q2wTKbDijktyGO_hZ6wyk9imIHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتیجه این و اون خبر چند وقت پیش در مورد تغییر شرایط استفاده letsencrypt می‌شه گواهی ریشه داخلی و پایان بازی. از مسائل فنی اجرایی صرف نظر کنیم، بحث‌های مهمی باقی است: «حریم شخصی» و «امنیت».
در کشوری که با مداخله در پیامک احراز هویت ۲ مرحله‌ای حساب کاربری مردم رو تصاحب می‌کنند و پاسخگویی هم در نبود قانون و ضمانت اجرایی نیست، امکان جعل گواهی برای شنود به خصوص برای موارد بدون SSL pin هست.
©
Hamed
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/ircfspace/2631" target="_blank">📅 18:51 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2630">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pDQo2MxL3_hERmNjn2DF3r6NwAyBUHRTo-DhUdKq6Ed2a2W0GJNns5GgK1kGTNctP2IegPqeclfDVuuNyfMbOBLws0T3DMrGRqruwrihbs0cMGCnWpVawvXInW_zgJrGmqQA9QwGRK6VtFECWYbLzXEi1YFX4HHYr-pH0i0Eo327cWFBuRHgct3we2603fb78e20f225HyZUAP04I4M0FuWHHiQJW_W23SZpKBlQ7UeR4PS2ttEIbWLpl1y1_xNF-CVZS-EGH5NgZw0_bZ6sw2Gp3SrorDe-ap4Q0aMsSQlwNp9DmV9h9xF5vydiAVVkT4_n4io08Iw1ja4vt7g9hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راهکارشون برای مدیریت قیمت تتر چی بود؟
نمودار قیمت رو غیرفعال کردن!
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/ircfspace/2630" target="_blank">📅 18:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2629">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">کاربران در چند روز اخیر قطعی، ایران‌اکسس شدن و اختلال مضاعفی رو در اینترنت تلفن‌همراه و ثابت گزارش کردن و میگن آشغال‌نت چندروزه که شدیدا اسهال گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/ircfspace/2629" target="_blank">📅 07:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2628">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RDpolXBi_svfj5oX-kHkdEg51ETzT0UGUi2sU48U3YuiwL4ltK9A3yzSjaNlSVmIsMAiKADKTSpSSmlI686ht0nx-ikPZMEn_WU8azkKFIL8ow_5ofrlcSZMftv8OmwzDD_wt0_LpcFXVGPNui8DBInDnAnVK7_aWWHoWLSihd0PypWF-V7uObhOPcL-zeVj7C5fPtIwkcXOwhAUg3A4Ne47HwWIuEws6LTFbYXhvQb0BUjP3Nm74R-bj6KH8DrSRIwv-P5Reo-BRmjwTKhLqDh7OO6eji_6jnf5XuA90n5XVnjYe3Ru-8J1fulKeIAgBaRSWG3HQix4fRfZpy_FDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گزارش Group-IB، یک بدافزار ویندوزی به اسم HEAVYGRAM شناسایی شده که از تلگرام بعنوان کانال ارتباطی و کنترل (C2) استفاده می‌کنه. این بدافزار از پاییز ۲۰۲۳ برای هدف گرفتن روزنامه‌نگارها، مخالفان و منتقدان جمهوری اسلامی استفاده شده و می‌تونه از راه دور روی سیستم قربانی دستور اجرا کنه، فایل و اطلاعات بدزده و حتی از صفحه‌نمایش اسکرین‌شات بگیره.
نکته جالبش اینه که مهاجم به‌جای سرور C2 معمولی، از بات‌ها، اکانت‌ها و گروه‌های تلگرام برای کنترل بدافزار و خارج کردن اطلاعات استفاده می‌کنه. Group-IB در گزارشش ۲۹ نمونه جدید از این بدافزار و ابزارهای مرتبطش پیدا کرده و با اطمینان متوسط این فعالیت رو به گروه حنظله نسبت داده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/ircfspace/2628" target="_blank">📅 21:06 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2627">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">اتفاقات امروز و تصمیمات هوشمندانه‌ای که برای مدیریت اقتصادی کشور گرفته میشه، کله هممون رو خراب کرده احتمالا.
ساتوشی می‌تونست وایت‌پیپر بیت‌کوین رو خیلی کوتاه‌تر بنویسه: دست به دست هم دهیم و دستگاه چاپ پول رو در
ماتحت
بانک‌های مرکزی فرو کنیم.
حالا تقاضا رو سرکوب کن، حساب‌هارو ببند یا سلطان فلان و بیسار رو اعدام کن، این باتلاقیه که خودتون درست کردید، توش دست و پا می‌زنید و ازش خلاصی نیست. این وسط، عمر ما هم رفت سر ایدئولوژی شما.
©
GrizzlyBTCloverr
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/ircfspace/2627" target="_blank">📅 20:16 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2626">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EKo52MhcnJYeoBZhdfDEDrjqPRx4dUxKQ_NJZLZ6_QhncsUBb4R2AxhGFRIv3-xheSVDEPc7hSrRPkiwunV95cRpdhtkdXBJ4VGvgxz1HYsGC4Nj2GhBuI6mGnEwgrzbiGVBPR-9FXDaHa6-VtteoUAWEXzksMmG33WokwjTrz5UMigv0V8olH91k1mlWv58ZqyC1ByAhZBvzc_MxqOZqbs1Zs0LD-G9ECFPWAph-YxxC5cf_Dra8-_R2n_3ugwU7fnaA8YbDZC9fTB7Jx2KWEBVCVIjs_H9uFOeKczzQdwx06ruwBD2zxJbUOnesF8ctnjJk6_A_N2qnvpB27hiOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر از دیوار چنین پیامکی گرفتین، ازش بی‌تفاوت رد نشین!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/ircfspace/2626" target="_blank">📅 20:13 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2625">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Sam_G3pAJHxXNI0RjUU-hvgOQ6C0bo44e3ErKbgRHvlKFG23K0wwyVcGb_en70kH9dMdW8GmvwVYFpG0LX3pw1SlHk9g6CHL40ejRVKveudN4aMCMhUnGguBcaOzl_ptfsUR9VKI6cz4WqNvigD1xKvgDDvhypScoucdoVw46ZWiDFbXVFqGuScD5WcHYU_KkOY0-vz9tXYZ5y6w0KMIMSkpMKJMahG8pvqECPisCK5Ayjy9vUbQ4WGv4xUFxXwyqEUiv68cEOHZjumuVpDhEOhpgb2TYOLod2PwBaZW1xCa070A-CNWF62md3XvKdQE-YPnF9jgHKV7nw-AR8SwIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروکسی تلگرامه؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/ircfspace/2625" target="_blank">📅 20:09 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2623">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">مجموعه‌ای در حدود ۷۵۰ هزار رکورد از اطلاعات مرتبط با کاربران صرافی ارز دیجیتال والکس مربوط به سال‌های ۱۳۹۷ تا ۱۴۰۱، در فهرست فروشندگان بانک‌های اطلاعاتی غیرمجاز مشاهده شده.
این داده‌ها شامل اطلاعات هویتی مانند نام، نام خانوادگی، شماره ملی، تاریخ تولد، شماره تلفن، آدرس، ایمیل، اطلاعات مرتبط با احراز هویت و همچنین اطلاعات مالی از جمله شماره کارت بانکی، شماره شبا، اطلاعات صاحب حساب، آدرس و موجودی کیف‌پول‌های رمزارزی و سایر اطلاعات مرتبط با کاربران است.
افشای این اطلاعات می‌تواند زمینه‌ساز فیشینگ هدفمند، کلاهبرداری مالی، مهندسی اجتماعی و سوءاستفاده از اطلاعات هویتی و بانکی کاربران شود. به کاربران توصیه می‌شود در صورت فعال بودن کارت، برای تعویض آن اقدام کنند، نسبت به تماس‌ها، پیام‌ها و لینک‌های مشکوک هوشیار باشند و از ارائه اطلاعات شخصی خود به افراد ناشناس خودداری کنند.
©
leakfarsi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/ircfspace/2623" target="_blank">📅 20:05 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2622">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MJ4wJ9GU_YH1rGWv9TjEwIORDjlaLeCN4zvHAj4zJRQX5CoPSUCete8r1TQHqhGS9BKgJHesNLB4M83A6ayEXpW6_GCP4BYT6SwkAg52h9OYq06tuUxx7lqKY7nViS-Z3cNl7JN6i9biZwVATYoqzolB6az2TeFlu-8CEtxEeZ-rdWKzWm6urgbkuiTTsSTRaG8ue8BD-R9vVvHsEDNJHmpXkUoIj3C_QuldctvETIGmtYBFKShhGkBkDvb8KSgJx0GQqC0bthaQtfWSloMn1AgX0er8Ofu_SDPEqKsUS6yTN6RKi5Q2q8tYfRgiDGb-_SQbggsSTGeIRVfcWXkAKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون وزیر قطع‌ارتباطات گفته "فراگیری استارلینک میخ آخر را بر تابوت حکمرانی فضای مجازی می‌کوبد".
۸۸ روز اینترنت رو قطع کردین و نگران حکمرانی فضای مجازی هستین؟ بابت ده‌ها هزار خونی که ریخته شد، باید منتظر کوبیدن میخ آخر بر تابوت ج.ا باشین!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/ircfspace/2622" target="_blank">📅 19:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2621">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ttbp8ET3vvGB1HoS5sr8on3vKPwUBms4yCQFMRCebeiYQsAN94QleYdq3ysbFs2FmfJge56-QTzyVb2Z2QYnQ4PoCCeHZb2KDk6cLHjucSoNpVygoaYOTz937s2dyWuTIH7dAGPr47iZpiZHsrvep1vaO3Pb8XdtpqjSZEzb0xuVE_bvKgrK9IAKW91mBkvZ-VR-CAyOTdaptJ1Ha8atc5atfaaIR6d11Bs9acr8fxs6u9P5g6WzDObhe4eoIW3u5cz6BLikS33kTZnmply3cTpnC-m4piF4Ly2yqtGu2tdU0Omo_vxhC1oOZwKQ_5r0g2e39iuOi1Cg9nL9toBpoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانک مرکزی با ابلاغ یک بخشنامه‌ی رسمی، ارائه‌ی هرگونه تسهیلات بانکی برای خرید طلا، ارز و انواع رمزارز را بطور کامل ممنوع اعلام کرد.
این بخشنامه بر ممنوعیت مطلق پرداخت تسهیلات، چه بصورت مستقیم و چه غیرمستقیم، تأکید کرده و مقررات یادشده شامل پرداخت وام از طریق شعب بانکی یا بسترهای دیجیتال برای خرید طلا، ارزهای خارجی نظیر دلار، رمزارزها و همچنین فعالیت در سکوهای مبادلاتی مرتبط با دارایی‌های دیجیتال می‌شود. /تسنیم
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/ircfspace/2621" target="_blank">📅 19:52 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2620">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WRWRXv0PY4XNhhEqvKjVxSc3IcvYXWd8QxsB7ONEQdttv7ttIhjwZLdDOIh8edMeflX-2WWTkDLm8k2D2iyW13r9Z1PtqOOilwDTT78a7cOGKarATtpNuZesrFw6tB66r6azNPS9aCT7CbAZGdYc-xcA7Z2TLW6NMQSteIIOz3XERNthCJk-m7G5GV-jpe5RxHxE5CdXCwxaGCB8DHxm5Ct1DszeNmSiyXhvp58qbVYKSwqa-NEIf1PmKJe7AOXgTQU6d6KWN5jaQfo6OYgLiG1mQts8wR2pBGTUauf28eP8sYxMxQnSuAc_a4r8JJ1RFdrPZGJcGeWtjvxfFv-qhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت تتر به تازگی اعلام کرد "به مسدودسازی نزدیک به ۵۵۰ میلیون دلار دارایی مرتبط با بانک مرکزی جمهوری اسلامی و شبکه‌های تحریم‌شده کمک کرده".
الانم با عبور دلار از ۲۵۵ هزار تومان، صرافی‌های رمزارز (با دستور مراجع) معاملات تتر رو از ساعت ۲۱ تا ۹ صبح روز بعد متوقف کردن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/ircfspace/2620" target="_blank">📅 19:47 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2619">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">هم خبر تحریم ساخت ایمیل برای ایرانی‌ها توسط گوگل قدیمیه، هم خبر مسدود کردن ۶۰ اکانت مرتبط با صداوسیما توسط گوگل.
فعلاً اون لجنی که توشیم هیچ تغییر جدیدی نکرده
😄
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/ircfspace/2619" target="_blank">📅 07:48 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2618">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aDC0IEpw_NO-rb4CXAw8wdHEmbN8s2r_HKaXOe-GCAqMfvhmLNTjJXcr71yy7jXL-aKk2E6kuLaFGQxDVbnZHLvXvapdiE5dXPWRO--wNTHEW6wOUnBPfEsDfhWZbf1Gjsrs4IMDmf_zI-HXW67mW5MZNpRq6rMvUHLALVCTSSeWLy6ikneAKwJ6IMp1k3ORIHNs9QJJaIcVpRVUhACFZfu3F-OXA2PiwT_t3qRcP-vAAXu5dm1Xp6wCp1P3CVgDNSt92FfkiBjVBzLfKhZxYxyZw34bV_CgTR95NhSZmvWtu6KQfxOV65yuaElF5vo5x_R-hRYrJ58GhB2K6jI1YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ sushTun یک کلاینت متن‌باز و رایگان برای هسته ایکس‌ری هست، که از پروتکل‌هایی مثل VLESS، VMess، Trojan، Shadowsocks، Hysteria2 و WireGuard پشتیبانی می‌کنه و تمام ترافیک سیستم رو از طریق تانل ایکس‌ری عبور میده.
یکی از بخش‌های کاربردی این‌برنامه که برای ویندوز، لینوکس و مک ارائه شده، مسیریابی هوشمنده؛ تا بتونین مشخص کنین ترافیک ایران، روسیه، چین، تبلیغات و دامنه‌ها یا IPهای دلخواه از تانل عبور نکنن. امکان تنظیم DNS، فرگمنت برای TLS، Multiplexing و چند قابلیت دیگه هم وجود داره. حالت کم‌مصرف هم اجازه میده ترافیک‌های پس‌زمینه سیستم مثل Telemetry و آپدیت‌ها مستقیماً به اینترنت وصل بشن و از پروکسی عبور نکنن.
👉
github.com/soroushdeimi/sushTun/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/ircfspace/2618" target="_blank">📅 07:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2617">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/n5U_oihbK4S4-b3YqU2l-qphTTzp126jIZ0GohPrKLXatyzCKttdqAS6NpEE7ai6eLve0gaQ-G8b1eJi1rJDRG8CxCcS8iAWv3upTn_iPYuyc8jfx287GeEP24JhFfISWc7_VmbqiqjxGXslAxq1UCpipEB7jQmc7LyfRUUrcxzVN3pb9TN05VeZO6W0QfVbONDnhlwqkeCMeIaDRlFkUD5_sAI_o1fUp5Ec-Pk8QXDfGoHHV5HeGVt9vt2GAD3KPPe8PtGL8TuwKOVSVI-OgrtKhF_SHYrW2a9nrO2JmwaYCYJt_YjGEMeQOP_Sr05zIzAy_jQ8H94jIHqHpCLAsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت Satelite یک اپ پروکسی متن‌باز و رایگان برای اندروید، ویندوز، لینوکس و مک هست، که می‌تونه بین هسته‌‌های sing-box، Xray و mihomo سوییچ کنه.
از وارد کردن انواع سابسکریپشن و کانفیگ گرفته، تا Rule-based Routing، پراکسی‌چین، DNS هوشمند، System Proxy و TUN رو پوشش میده و یکی از قابلیت‌های جالبش، حالت Multi-Core هست که اجازه میده چند هسته همزمان کنار هم کار کنن؛ مثلاً سینگ‌باکس هسته اصلی باشه و بعضی پروتکل‌ها رو به ایکس‌ری یا mihomo بسپره.
انتخاب هوشمند نودها، تست تأخیر و IP خروجی، مدیریت DNS و Hosts، تشخیص اتوماتیک پروسه‌ها و اجرای دائمی در System Tray هم از دیگر امکاناتشه.
👉
github.com/zn0wii/satelite-proxy/releases
💡
github.com/zn0wii/satelite-one/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/ircfspace/2617" target="_blank">📅 07:44 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2616">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ni5akxyojsKtgMSBLFEFTc6szJTvzIhXL_FnuQAmNQAhOGTQIL7162hnAcG9pAys82_cTdh91dhpanedYPhVBHlyDGcaj8VbxLVBC44oHC-xU_S4f-pxFpB7b6XEk1W3OF-I3INGcrne4EREzLPGdRtGIMU4NYLwNaM34_79ZrBbEkI3PKIdlPc8ilbI6pl4y2jYgxqvPez4TsrjX-31boISMEJcCmJcnyh0VS13puUhrB2pCK5vTjKN3OQB-Dl9YTkom_6Txy9vm2ZECir9UakOjaECdPM2m6tCLnqNWiQQjNqXfQzO7VmpU6pYUZKBDa11joVnW4csPNRfCmavaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی فقط دسترسی به شبکه‌های اجتماعی را محدود نمی‌کند؛ محتوای حساب‌های شخصی را هم زیر کنترل می‌برد.
شماری از کاربران با انتشار پرچم حکومت نوشته‌اند که درباره فعالیت‌های «غیرمجاز» توجیه شده و تعهد داده‌اند در چارچوب قوانین جمهوری اسلامی فعالیت کنند. پیش‌تر، انتشار لوگوی پلیس فتا در صفحات اینفلوئنسرها و کسب‌وکارها نشانه توقیف یا محدودسازی آن‌ها بود. حالا انتشار این تعهدنامه‌ها، نگرانی از تبدیل حساب‌های شخصی به محل نمایش اطاعت را بیشتر می‌کند؛ جایی که مخاطب نمی‌داند آنچه می‌خواند، انتخاب صاحب حساب است یا حاصل فشار بر او.
©
filterbaan
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/ircfspace/2616" target="_blank">📅 07:38 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2615">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">معاون سازمان تنظیم مقررات و ارتباطات رادیویی گفته "حجم‌خوری نداریم و بخشی از ابهامات و برداشت‌های کاربران درباره نحوه محاسبه میزان مصرف ترافیک اینترنت، به وضعیت ثبت اطلاعات محتوای داخلی در سامانه تعرفه ترجیحی مربوط می‌شود".
خلاصه: حجم خوری ندارن، ولی باقی چیزارو قول نمیدن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/ircfspace/2615" target="_blank">📅 07:34 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2614">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VXD3k7E_cg377MQsif_p194_ImLKGZ89F2kIxVe0GHLZyv2MfeiMfRT0iKEbWCzm8cHOmK0BDjsnNFyFyELyFYG7O7sxS3gOjL8LfCWVjF66zwMq6UvIK9vlihZfPlLixaPx9f2W_t8gJMdVllcYa6hKzuxQOXSOXK0uTbxx7dysDa7OEozwmdv7LtZQvb2wQR5mWRHoH-G3upiDIyxUvH6WUzpLZBGL6_zUU2fgAL8E1OlHlsQaanjIIyL5-f5h-C3spBeIs9uKyO2ttGv4bX7E2AWi0U9ajpPK1MH15TQSy66rZjvlltaN3SNNQ5Z2NEw6_VeL3Yu_erS1AS7erA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گزارش Qrator Radar، شبکه همراه اول با شناسه AS197207 در ساعت ۱۳ روز ۲۹ شهریور، بطور ناگهانی ۱۹۰ پیشوند شبکه رو اعلام کرد که باعث ایجاد ۱۰٬۸۶۵ تداخل مسیریابی با ۱٬۵۲۴ شبکه در ۱۰۰ کشور شد.
این رخداد که بعنوان BGP Hijack ثبت شده، در ۲ مرحله اتفاق افتاد؛ مرحله اول حدود ۸ دقیقه و مرحله دوم حدود ۱۵ دقیقه طول کشید و حداکثر انتشار اون به ۱۰۰ درصد رسید.
وقوع BGP Hijack میتونه باعث قطع دسترسی، انحراف ترافیک، اختلال گسترده و در بعضی شرایط شنود یا دستکاری ارتباطات بشه!
البته در این‌مورد مشخص نیست که بصورت عمدی بوده، یا خطای فنی ...
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/ircfspace/2614" target="_blank">📅 08:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2613">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">بانک مرکزی نصب «گواهی ریشه داخلی» روی دستگاه مشتریان را یکی از راه‌های ادامه خدمات بانکی مطرح کرده است!
اما مسئله فقط رفع هشدار اینترنت‌بانک نیست؛ اگر این اعتماد در سطح کل دستگاه ایجاد شود، می‌تواند فراتر از سایت بانک اثر بگذارد و در شرایط مشخص، زمینه رهگیری ارتباطات رمزگذاری‌شده را فراهم کند.
مرورگر زمانی گواهی یک سایت را معتبر می‌داند که زنجیره آن به یک مرجع ریشه مورد اعتماد برسد. اگر کاربر یک ریشه داخلی را به سیستم‌عامل اضافه کند، دستگاه ممکن است گواهی‌های دیگری را هم که همان مرجع صادر کرده معتبر بشناسد.
خطر زمانی ایجاد می‌شود که آن مرجع برای یک سایت گواهی جعلی صادر کند و مهاجم نیز بتواند در مسیر ترافیک قرار بگیرد. در چنین شرایطی، مرورگر می‌تواند بدون هشدار معمول به واسطه اعتماد کند و حمله «مرد میانی» امکان رمزگشایی ارتباط را فراهم کند.
نصب گواهی ریشه به‌تنهایی به معنای شنود نیست؛ مسئله اصلی دامنه اختیاری است که به آن مرجع داده می‌شود.
البته راه کم‌خطرتر وجود دارد؛ اپ بانک می‌تواند فقط برای سرویس‌ها و دامنه‌های خودش به یک مرجع داخلی اعتماد کند، بدون تغییر فهرست اعتماد کل دستگاه.
پرسش اصلی طرح بانک مرکزی همین است: برای حل اختلال خدمات بانکی، چرا باید اعتماد یک مرجع تازه احتمالا به ارتباطات خارج از بانک هم گسترش پیدا کند؟
©
raaznet
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/ircfspace/2613" target="_blank">📅 07:52 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2612">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sboXPgquNbUsn4wtan3JJ4_hPO38xiBAVcvZ7l0_i5MeNoua03mEoL8QRv3Vwfaa9S2bQAokL_2E6k_Ear3suoP9jOp8MUtFlyKGOs-_9Cu7Px9DCxJ8y0AqKtpvkLchAOJHjIh0Frg-Iid0JBxu0k7xlhxvPXmukrR3T_U6spJyETceRg9uHwHhfGHchpAKak4y4Nq9wNwX3EgniLkJbrDToWiYSsOdixLahLzzaF872x1S7mDWaMXOGkNCj1jsIQLZ8BKdWpCagZbA8tD7FIES-ydSTq7982ETOnjleS-0ZsPoG73Wa0mfGtBA2O5WbH7ayzRrqZLkmQxj2Y-nsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراقب این نوع هک باشید!
یه صفحه جعلی شبیه Cloudflare میگه برای تأیید ربات نبودن، Win + R رو باز کن و Ctrl + V بزن.
چون شبیه تأییدیه‌های معمول کلودفلره، ممکنه طبق عادت انجامش بدید، اما در واقع دارید یه دستور مخرب رو اجرا می‌کنید.
©
milad_joodi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/ircfspace/2612" target="_blank">📅 07:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2611">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S0XxwLUFdJVwPO70Hnn2OK1tWcdgemCxOPFPvcm_9YVlTt4lj3rFZSy7npJyfo27IvUdrrWqXfRmy5Uh5EAPwGkVDFk3u2RE63QGhKeWt24s3OzLvQfYRxOJqRxoOxVjFwZbfIB7Q4rDBUjkIXPNRTvG9TtVLQSu3byDeBSvvFsFSqzg9OLsT3AV6MqOG3seC8z_j8Qj15eN4-zuK-5fh7xHE9rm_MjeTZNFXeSUhb7_Iuo-sBrS-bEz34SrOyC0t2aWTrxrOf0620fBFmrSqgFedxBi6HRKaJ0M6Le6LWJrYq2O3OWPQv0O88k3zR1LGywXhbiam6sgUQsR7emp4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زپتون یه موتور شبکه‌ی جدید، متن‌باز و بدون وابستگیه که با Zig نوشته شده و برای کار با رابط‌های TUN طراحی شده. ایده‌اش اینه که ترافیکی رو که سیستم‌عامل وارد TUN می‌کنه، مدیریت کنه و اون رو به ارتباط‌های TCP، UDP و ICMP تبدیل کنه؛ بعد هم ترافیک رو مستقیم یا از طریق SOCKS5 در اختیار برنامه‌ی دیگه‌ای قرار بده.
پروژه Zeptun امکاناتی مثل پشتیبانی همزمان از IPv4 و IPv6، NAT، مدیریت DNS، مسیریابی خودکار، فوروارد ICMP و پردازش چندصفی TUN رو داره و برای Linux، Android، Windows، macOS، iOS و FreeBSD ساخته شده. طبق بنچمارکی که روی یک رانر گیت‌هاب گرفته شده، زپتون عملکرد بهتری نسبت به Sing-box، Hev و Tun2socks داشته.
این مدل هسته‌های مستقل، می‌تونه برای پروژه‌هایی که نمیخوان تمام شبکه و TUN خودشون رو به هسته‌هایی مثل سینگ‌باکس وابسته کنن جالب باشه؛ مخصوصاً با توجه به اینکه استفاده و توزیع کدهای پروژه‌های دیگه می‌تونه الزامات لایسنس و کپی‌رایت خودش رو برای توسعه‌دهندگان داشته باشه.
👉
github.com/Noisemux/zeptun
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/ircfspace/2611" target="_blank">📅 08:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2610">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DYK-dGWN06oFe74wKF6jLjYzb7gsdBg3QJose_-fmJ8ZAtRv9WJ7dR3NlD3horI3q3wncPY4hEUEGxNPwnsTMuhG3cHDx9GuJ0dkaTh15-tJPPCq9hng9xfiRYESZ5UetxyqbkieB04_Y6q3v_h0p5dqxXPCOE3qLDWTZYYvUfPalXOYdda85DSt-5NqEykijQ-5vN9fEsts2XyiHVA3xTWp7J6Qfe61j9sRmu9qANjiANcngY03t0V8Ws2dhenmqi_AVcdQKYoWhMHyjbaLT0G0FqQPkwcGSzyZrsgMP4nhrdjubb7gHvVwgObR8-WoFuCe8JOtaqdk9Cn6sl0O0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وای، چه گوگولی
😄
فرمودن "مجلس بدلیل پایین بودن کیفیت دسترسی، با افزایش قیمت اینترنت مخالفه و انتظار داریم وزیر ارتباطات از حقوق مردم و افزایش سرعت و کیفیت اینترنت دفاع کنه".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/ircfspace/2610" target="_blank">📅 08:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2609">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rAg7mYZ4TTILiDZ7lojX0_r6rvTQWYQOpJYBypQh_eQH-AWVBo5wJ8CsDTSvx83HAy32M4U4tdgsYB7YAIMg9JpsJoXmU90qVrJtc46hOPSRnMiMw8QKzEfoQbWBUEx35PZxfXS3p-0npxwO2yfaEJTEnhVNgRpt6ROjDJ4aQ6-u2HtfhWvr45CQGvfuqmkHDGsL0KKon9C_1kC0-wIy9GvwjVdg7pbE_R7qOkABsYQUIxXTV1qzvTxJN18z5P2_fz1r0wR-23IyXYTBvRLVW_A7kNCWke1rrCCsa22KmJL63ZeK-soya66RHJd6RVp2fq5NAkm2nCK26kj3IxtFTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکریپت Google Flow Helper برای اجرا از طریق افزونه مرورگر Tampermonkey ساخته شده و کمک می‌کنه محدودیت‌های دسترسی به Google Flow برای کاربران ایرانی دور زده بشه.
این اسکریپت درخواست‌های داخلی Google Flow رو زیر نظر می‌گیره و وقتی به پاسخ مربوط به تنظیمات و محدودیت‌های سرویس میرسه، یه فلگ مشخص رو پیدا می‌کنه و مقدارش رو از false به true تغییر میده. بعد پاسخ اصلاح‌شده رو به خود رابط Flow تحویل میده؛ در نتیجه فرانت‌اند تصور می‌کنه اون قابلیت برای کاربر فعال شده و محدودیت مربوطه رو اعمال نمی‌کنه.
این ابزار VPN یا فیلترشکن نیست و خودش محدودیت شبکه یا فیلترینگ اینترنت ایران رو دور نمیزنه. آدرس
flow.google.com
باید از اینترنت شما قابل دسترس باشه. این اسکریپت بیشتر برای مرحله بعده؛ یعنی وقتی به Google Flow دسترسی دارید اما خود سرویس بخاطر محدودیت منطقه‌ای یا تنظیمات سمت کلاینت اجازه استفاده از سرویس رو نمیده.
👉
github.com/maanimeisam/Google-Flow-Helper
💡
telegra.ph/Google-Flow-Helper-09-20
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/ircfspace/2609" target="_blank">📅 07:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2608">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/H41KqunGNawLIsVnavttW55cgrQQDpbRqt5ZYPGN6BjEE7z84SWLA5s1RfwcSKLek9Rz1b3Pe0XCAjFeSEo_61PrR1IuDAu0h4axy9AVn4Dr-_8d_HqvB7s-ZK8_mmwAzpHi-lBMiSgF6B7e7ybcAIIO_3AjzD4gYn3iZSeGkN62-3ugnJYHhUggiTXBv-K9jF0VtldiRh7XP1kfLIc_7zeFZmYGslZHSjIzt1ALbG6LAfpFeCibC4f345CHVrOyK8T5vHPHqJE85WUx4UyCu-VypWibrrYEsc9hnJsDU8Z_4rCKZfeX8_Q77cwuQH0WuJ-rNA7lJqiYHzQN4FhEoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحقیقی از TechRadar روی نزدیک به ۴,۸۰۰ اپ VPN اندروید و iOS انجام شده که نشون میده تعداد زیادی از VPNهای موجود در گوگل‌پلی و اپ‌استور، اطلاعات شفاف و قابل‌اعتمادی درباره سازنده و سیاست‌های حریم خصوصی‌شون ارائه نمی‌کنن.
در این بررسی، ۳,۳۹۲ VPN اندروید و ۱,۳۸۷ VPN آیفون بررسی شدن. فقط ۶۱.۴ درصد از VPNهای iOS و ۴۰.۸ درصد از VPNهای اندروید تونستن تمام بررسی‌های اصلی اعتبارسنجی رو پاس کنن. بعضی از این اپ‌ها از آدرس‌های رایگان Gmail، سایت‌های ناقص یا غیرقابل‌اعتماد و سیاست‌های حریم خصوصی کپی‌شده استفاده می‌کنن و اطلاعات کافی درباره سازنده‌شون در اختیار کاربر نمی‌ذارن.
در نتیجه، صرفاً حضور یک VPN در گوگل‌پلی یا اپ‌استور به این معنی نیست که اون برنامه معتبر و قابل‌اعتماده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/ircfspace/2608" target="_blank">📅 17:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2607">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TUdUvA6sGywVMaxeGi2NwPNykECqvDaC8t0kx_SraBbMrUWa7kN7J9I5mLXaJMmtfgY1PvR25Bi7soiROcx4vPlhOGmBnPdUK2QsOCSXxFUWjI7wPwke_mqDL3nPYjeHcr6n02sZfTV4qqWOTAYUFjAtWqi3tYlJWuwHp1wp4tvy8uCBd5dEzKSqbTLmHKIZEzRy3MpOdxi2jg8Xyim75IYT8mgwc8XWd_9fJ7hb7RGEjeq3ZsQ5oVxs5yvwpo7ELbR6Z1IR_O_ebZGRQxCdccNkxlGfNvvwkqit3LOfNez4xgnxyyrUj5xYZPDuLFhG43Wqk1ICRIAQlGp7QpxlAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این عکس مربوط به مسابقه CTF بلوبانک هستش، که برای اینکه چالش‌های مسابقه با Ai Agentها حل نشن مورد توجه قرار گرفته.
طبق تصویر، در هدر یک دستور داخل Response گذاشتن که اگر یک AI Agent در حال تحلیل پاسخ HTTP باشه، سعی کنه اون رو بعنوان دستور خودش برداشت کنه و به کاربر بگه چالش قابل حل نیست و اصلاً آسیب‌پذیری‌ای وجود نداره
😁
مسابقات Capture The Flag، یکی از شناخته‌شده‌ترین مسابقات حوزه‌ امنیت سایبریه، که شرکت‌کنندگان باید در سیستم‌ها و برنامه‌های از پیش طراحی‌شده با آسیب‌پذیری عمدی، به دنبال رشته‌های متنی پنهانی موسوم به فلگ بگردن و با کشفشون، امتیاز کسب کنن.
©
Maji_Call
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/ircfspace/2607" target="_blank">📅 17:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2606">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cqDqvPBckl7H5GwgTbkZBfhTzqsrAqQwaozAzA_s-33vj6YEg8sCHDNCEht25IFyf1M5PTcLWTkxIkx1haxuAL0yGEzFZuxuJUTxeEXK70RZ7CdFiYAPBlATWTJlPszZth2yFrr2Ph6bAhk0SXVbFtp_8D2wYn00Pc4B3MeFUxBWDIH32Z_0Pq696QIwUMhENV9uzEfd34hVX15Zdwv5lzVRaxRTSwAgzIey1hVzlW9_YXWZ-SJ3V_9OUxeuXzmFG3hVQNwYoGU6OI7nw0U0w8ArguZSQBXtj0v587lGCdkoLY9gTrPW7HfO76b67KRrBJaYBY41Yqva62NokJRkMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از ویژگی‌های مهم Tor VPN Beta، ایزوله‌سازی برنامه‌هاست و هر اپلیکیشن IP خروجی مجزایی دریافت می‌کند، تا امکان ردیابی رفتار کاربر بین برنامه‌های مختلف سلب شود.
👉
play.google.com/store/apps/details?id=org.torproject.vpn
©
PasKoocheh
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/ircfspace/2606" target="_blank">📅 17:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2605">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lr0YBvnBzC-QWrO4lAUFytHLFpeh936cxTO-JYPN-Me-hUi8fX_qfqStWXRyHo710_jMF9KhayY0aqzkY_PhIq37f9KKj5RpXAr85NRZ9GfZJDGXIXA6dFxPEXdQkfEcFbqa27Mlw6NM6IcSwL48B9IOjUAYFAu2SNBvzEDzpDr6k_IOV8GT2h-xOwpLMTuzwEQORfElZp4SOKdEBUTqRf4N24aZeiW4Tq5nGhE7B__WVX52IvAntoWckd5Hfr8JpZAsYllp180B5YDxw9c3AOdytKkXK8bim_Lg1zwVveRdZqgJMe1nO8NPpXcnaK4v-PELHbwXAIcqYK7nLLAsrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کپی میکنید حداقل اسمش رو تغییر بدید :)
تصویر مربوط به نسخه وب ایتا هست.
©
Ralireza11
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/ircfspace/2605" target="_blank">📅 17:08 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2604">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ایران در جدیدترین گزارش اسپیدتست نه در رتبه‌بندی اینترنت موبایل و نه اینترنت ثابت حضور ندارد.
تا ماه گذشته، ایران فقط از رتبه‌بندی اینترنت موبایل حذف شده بود و در بخش اینترنت ثابت با رتبه ۱۴۰ جهان قرار داشت؛ اما حالا در گزارش جدید، رتبه ایران در هر دو بخش حذف شده است.
©
itiransite
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/ircfspace/2604" target="_blank">📅 17:07 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2603">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XnERb0uF7JsrzcSfN0HsuZ8hDum-dW7m20VToMPi6TlNLYKZaLpUHFsjnmRCrbhBPbM_y9OeXjgc_mw_Si3LbSkx4aKp_EwsKrpXFSygTZFV-qWiljKtM08eJ0Z5FDBIapsBitczly59S0ZsmSNjZjeBZWwZq6OF0vwj5VfwsLAG_ewMxR0OqObnWAT3p_ly9qurUdDEvFXX8uRx6qq4SJHTP86jwJsFuh_5eVdvtQprEgEycrlFzQYfJnW2A4ucABQDtHEv-KTwbkaiLEvIFC9YYFbKWGWa2EIW6XZEFDUn1sNlGjl1Duc-7no47PG_1eq-QBhCDrarVNUs-0VYKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صرافی رمزارز کوینکس اعلام کرده فعالیتش رو متوقف کرده و کاربران تا ۲۲ دسامبر فرصت دارن داراییشون رو برداشت کنن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/ircfspace/2603" target="_blank">📅 16:51 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2601">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tkDnFpVtw66_fLLaZtHvWW18dpv51ze6AycyNO4l0omb87hZHbFiZPstoB3O6dzaJfkOvqEyoHML3eKnlw3o_MZcZgoWQBxH9I72n7vqYc42_4h5ZevayR9DJqiazq-pxvplHgv_Bd9Q8Hsc5QfsHHBcH7OIBtvFtGe-8-2RiDvdXAIiOkyl7nSvpn-DctVq4hXXyRS9G_9bVkamfPzgrc0xbazh4M3xE8CzjI2q07UNJJw9jWVAGWGLtnB7j3hNKREJ8udcSr7bmUz7B-YDp9Lia-LUc4HYX3oCZSWHxlveu2NEgiObz4F0qAHw7tOPE-o5atYD8hdd-QrKHTY2bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی خبرها
دیدم
که ساکنان روستایی در منطقه فتح‌پور هند، در اعتراض به کیفیت پایین و ناپایدار اینترنت و خدمات تماس تلفنی در منطقه، یکی از کارکنان شرکت مخابراتی رو به یک دکل 5G بستن.
امیدوارم برای وزارت قطع‌ارتباطات پندآموز باشه!
😁
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/ircfspace/2601" target="_blank">📅 08:17 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2600">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LEympEFG3aCWINZLz01JAL2rwxKmCZFv9BhxZF84F9fY2TOeKK28v11q7rW6OhAt4nMLLWTjTTZ7JJhAWRrAly9vn4bmtnOwawURzEocRMz0aWnp8YgNzkEPcr9gaJJ4k7fzqScX6xIl_48t7GOI7y9LN0hC9ygfRoLRu_RpJSaOk8hg293ls09qcXXuKFJxfUdAzeLC_IJ-05ujQ8r4STNnfo0n9Xo4x7WLcn1EyhGIlIGw2dIT8XecW568M4y0l6HgeUHfkOeb4W_n21GmMyTnC0_gnE_LOdVackb1OvbDjuzSqYhGwgLqXRFhOt51hvj8_bwiJDnEpsiu7uZqbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات سرشو از برف بیرون آورده و گفته "اگر درباره محدودیت استفاده از IPv6 مصوبه قانونی وجود ندارد، دلیلی برای اعمال محدودیت در این زمینه وجود ندارد و موضوع باید با سرعت پیگیری و تعیین تکلیف شود".
به مناسبت همین دستور سریع، فوری و قاطع، از تصویر پیوستی اکلیل باریده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/ircfspace/2600" target="_blank">📅 08:09 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2599">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dtT37UEXsGCwMUVsphRnhNZ8bPUmDA4UUapyKVf4vhHxGBXUGYW3NrY2HImRTi_scH7Lk1uLM5Tm4LjSQVl8PND7vudnXUCmMu1ZctN8fXjtgm4uFhk0PcZvO3J5D6TMiKP3Ii8gbP3uFC5eqsV_LCE8PwaEECo26FJPQBQRQhEaYsLDPNa3FhRCpbDAUq3Zk8Zz98LgC0ky0ZkVRhzDOEZ1NbIZ0B1YH-xevNy6mpUUrtYo7Hfq3R8uzYjmv70QuTgIHGK4Eyh_z96N_x7FxjpRSzLUG7-jPUd71f0mLNAF5fy4O6oZJPjivppmZRGNkOYr6FmgTWdu0eB79M2r3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید از هسته متن‌باز و رایگان Aether منتشر شده و این بار Tor هم بهش اضافه کردن. حالا می‌تونین از تور بصورت اتصال مستقیم، اتصال Tor از طریق وارپ و حالت معکوس استفاده کنین. پل‌های Tor هم بصورت خودکار از BridgeDB گرفته میشن و Aether می‌تونه پل‌هایی مثل Snowflake و WebTunnel رو امتحان کنه.
یه قابلیت جالب دیگه MASQUE-in-MASQUE هست، که در واقع دو لایه‌ی مسک رو پشت سرهم برقرار می‌کنه. این حالت باعث میشه برای خروجی، رنج آی‌پی متفاوتی نسبت به یک اتصال MASQUE معمولی داشته باشین و توی این حالت دیگه آیپی ایران رو از کلودفلر نمی‌گیرین و رفتار اتصال تا حدی شبیه متد Gool میشه.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/ircfspace/2599" target="_blank">📅 07:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2598">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/prH30FkxGERhlOXj-2R6cRSyMkH7E5pKJuNZlRcmP4mhR57_fOln4_taw2aHUN2c0bIiM6y8qt2gyFwEcYPpQ737cJH9WMxy9IFlMbumVjHIVa7MTeXBXIBDYMdNuHFOb6jR2Rd0XN5ExTwhwvx1uM14UZJMeUkovR6HFmKTpJLM7Uoe_4eKI5SoMkLFOfT27fSjEo_n58MzSLFkpckUVvFJ3MDuZj0ycZlwmcqUKSnCXHyqAkZCyH93RO4Adf5Qlj00RwmcazW0EhB023Pc7zVQwN02wLEd7JoCYsRLg-SMAxDLv6kHXZbqn0vPj65y9sx0ie0jn9SFHgpsqaWxAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آنتروپیک، شرکت سازنده Claude، در گزارش تازه‌ای درباره سوءاستفاده از مدل‌های هوش مصنوعی، چندین عملیات مرتبط با ایران را بررسی کرده است. در این گزارش، ۴ عملیات مستقیماً به جمهوری اسلامی نسبت داده شده و مواردی هم به سازمان مجاهدین خلق و یک عملیات فیشینگ علیه کاربران ایرانی مربوط بوده است.
در یکی از موارد، یک مجموعه مرتبط با جمهوری اسلامی طی یک سال اطلاعات ۶٬۳۸۸ ایرانی را جمع‌آوری و پروفایل کرده و برای این کار ۱۵۵٬۲۱۶ توییت را تحلیل کرده است. در عملیاتی دیگر، بیش از ۵۰۰ کانال برای جمع‌آوری اطلاعات افراد داخل ایران بررسی و ۵۱٬۹۴۴ پیام برای ساخت پروفایل‌های روان‌شناختی تحلیل شده است.
استفاده از کلاود به تولید محتوای تبلیغاتی محدود نبوده و از آن برای جعل هویت، پروفایل‌سازی، توسعه ابزارهای نظارتی و حتی ساخت بدافزار و ابزارهای فیشینگ استفاده شده است.
©
RaazNet
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/ircfspace/2598" target="_blank">📅 11:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2597">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bZeoy_XbBcYIaLPLKH6b9mbp2T4t-mdUbggeU9YenPEXoUmUUzG0th9mML3mTSAh7SyYUWJjXEWsgWp_HhOZVKoPduO3GPbOfK-c8PbmVgRwBs9R4OZXz1qf5OEH7R-_5Xf4p4Om_yqMU0u6oJyeIqmVMyTSWgUBeKCxpN-90gC-2aVJ1CBnlogYUrxUr-kTgUyd8Eb6uFRkCj1HwWgoe57G8OmwG8eC6zpTnQPI5TRHf2yFUAACZl5a2GCmuLu3EdUCzgms6WoKVQmKJ77JmL0lUVcWHGE6FNojyOkufEfYmFmC2ha8CeFzckEZAoEEPOPj7pyU7vNzL4rSFSwPMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون علمی رئیس‌جمهور گفته "۸۳ درصد رتبه‌های برتر کنکور در ایران مانده‌اند. این موضوع نشان می‌دهد بخش قابل توجهی از استعدادهای برتر کشور در داخل فعالیت می‌کنند".
البته نگفته ۸۸ روز اینترنت رو قطع کردیم، هزاران نفر رو در خیابون کشتیم و خیلی از همون‌هایی که کشته یا سرکوب شدن، از استعدادهای برتر همین کشور بودن.
نگفته راه خروج از کشور رو برای خیلی‌ها سخت‌تر و پرهزینه‌تر کردیم، عوارض خروج گذاشتیم، ارزش ریال رو در برابر دلار به پایین‌ترین سطح ممکن رسوندیم و انقدر محدودیت‌های مختلف ایجاد کردیم که بخش قابل توجهی از آدم‌ها اصلاً امکان رفتن پیدا نکنن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/ircfspace/2597" target="_blank">📅 08:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2596">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IVcSx6vL6QRR4PVpT5vIupVa-oZjdgHz0LiF9s7ijZ8Enn1Fr68fpif0jVAFd8Lp3hFVieJimnVT2UyDUWyWTnaNZJ2fK4YqI2GtUDY2oDieXkwCMrkbj5sAkYdIzp0hMVEAN9A_U59AeI2plD7Q-VFg0si-JFFGJcN49PecWaPqMatxn-LzGK-1hmaVdVm89H6hdC2IcVigN9ApAjuBp0dhPUAn_yfHs6BFCCPo_DOWQ1JJlCLRTuEPzxpNl-EDmOKy0jzqfxOj1Kb4YvrVpSy767LQ38O7urkVZdljivEZApMk--98t0JDXI1W6GOo0Pjb6P6T54093jegVxlEvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیتابیسی که ادعا میشه مربوط به کاربران فیلترشکن JumpJump هست، توی یکی از فروم‌های دارک‌وب منتشر شده. منتشرکننده با شناسه leakhunter ادعا کرده این مجموعه فقط شامل اطلاعات معمول کاربران نیست و اطلاعات شخصی و نسبتاً حساسی مثل اطلاعات پرداخت، اطلاعات کارت‌های بانکی، تراکنش‌ها، موجودی، لاگ فعالیت کاربران و اطلاعات دستگاه‌ها رو هم شامل میشه.
البته فعلاً نمی‌شه صرفاً بر اساس ادعای منتشرکننده با اطمینان گفت تمام این اطلاعات واقعاً متعلق به کاربران JumpJump بوده یا اینکه کل دیتابیس ادعاشده صحت داره، اما درصورت صحت‌سنجی، همین اطلاعات نشون میده جامپ‌جامپ ظاهراً اطلاعات شخصی و جزئیات مختلفی از کاربرانش رو نگهداری می‌کرده، که این نشت می‌تونه برای کاربران دردسرساز بشه.
اسم JumpJump قبلاً چندین بار در گزارش‌ها بعنوان یک اپ ناامن و مشکوک مطرح شده بود. بنابراین اگر از این فیلترشکن استفاده می‌کنید یا قبلاً استفاده کردید، بهتره موضوع رو جدی بگیرید و حواستون به امنیت اطلاعات خودتون و افرادی که باهاشون در ارتباطین باشه.
©
hamedvpns
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 90.7K · <a href="https://t.me/ircfspace/2596" target="_blank">📅 08:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2595">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vrTqj5CDPGclbz5hsyc5ruKepj4vnJ926x_LJOEzo40JxmzPHewaTpynN4zXcwChAI3fkcyG3BumzbtJqYrtGc_h56UVAzO1-Y35EruC0N1P_DbZCGoIcKyhzdechjA0aQ8Witb3m33fQZXd2FYzVTub-XgvwbwBenslQwa8hsfJ1R5JsalXl4tbBMODeygKSq6j4RK8NstuQZ7FLb8No7S6Bs6bbBhWiX0qK--WFsQGyMDQWT6Cjomb_XX11MZfDasLq9mk8LRrIqKfiqDeCzUC5Yw6u0t-K9XzJt5gM4FQAifpTxYgzY5pHgdbnbRYWt2LrsW-v0Y1DTDnXgvpaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه پایدار است، یعنی به همون آشغال‌نت قبل از قطع فیبر نوری در ارمنستان برگشتیم!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/ircfspace/2595" target="_blank">📅 07:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2594">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mwZmzG3tYvPMf3qzD8gGwONPJHWrSlH1todluUYt2iQLQM0ywMQwbsEXhjZfJEzdTvS0RuPVNIatr3IoKLcqcUOiMzSyHm22f4UfxGB1ZvHuYGfV0Ohm8AjMfLeToGEkZj34Pc837hviygGz4c481t1B7yQHDeJXNCS1JytmR2bxCroZIx8WKaO84TPrylF4OjyjeMzvGY8HTsZKSDNcg-GrXLrH0BiyUHsUZQaOwpt-9BNkwj66YMhEwyuAJU5bmGqUUxSl_ZgT13UKFSd_Vb8JeB12jin4-JDW60h41N6ayS-aAap_I_QL_DPzLvlIfvd91DruDVndqdarXZov0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از مدت‌ها وقفه، بالاخره فیلترشکن Oblivion به مسیر توسعه برگشت.
در این نسخه که برای اندروید منتشر شده، هسته برنامه از وارپ‌پلاس به Aether سوییچ کرده، تا امکان اتصال و دورزدن فیلترینگ از طریق متدهای وارپ، گول، مسک و سایفون فراهم بشه.
👉
play.google.com/store/apps/details?id=org.bepass.oblivion
💡
github.com/bepass-org/oblivion/releases/latest
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/ircfspace/2594" target="_blank">📅 07:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2593">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X6yA-_6SCtKalO7v9dk6KlmXmU0LbDzMOSfLRuJXgNvy8MJGqm0jDyq0V2_rPnWzy7AHGLKFDqbin04RNwazqOcOJ4W2cBzObvPvxYqCahY7KnXckZfS_OjzubkaCKgqh2CzHmEpNz3Yty7GGq2DrNsdfd6j8WjtrLGQF84K0m2DxhD-BwB2ilKLUe8sjcrtyMzMG0fF-Nh4gb-pV5iANq4dCt0eW7eTKKdFpGtjQbkZt_QpHXeb8TP3_0lhpxnuWUnTjHXkariCTDQDj8jPtTRSySdT8jm8bVWsdkQNYxlAMOw6bga0MNZsuns8M_T_aHLdz0HvH-hFWf_0eWtqdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل یک آسیب‌پذیری روز صفر با شناسه CVE-2026-85046 را در موتور V8 کروم تأیید کرده و هشدار داده که هکرها از آن در حملات واقعی سوءاستفاده می‌کنند.
این نقص ممکن است با هدایت کاربر به یک صفحه آلوده فعال شود و مهاجمان را قادر به اجرای کد مخرب، سرقت اطلاعات یا از کار انداختن مرورگر کند.
لازم است پس از به‌روزرسانی، مرورگر را حتماً دوباره راه‌اندازی کنید.
/فیلتربان
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/ircfspace/2593" target="_blank">📅 20:10 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2592">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PQXqu5glofTR4t2Fs_A7HixJGRnNOJ1lw7DburPDuq49tZa0GE1Sb7ejviRmBvhfzfjUEs5lDSDVKs3n0Y71P7LEYUCjta1DUUezHiCwOvZjO95qOgwTcHGXvg3ZAr7wjCaKteHX-aMpaR-jzmcg_MIT0eO2unrYKoRefGNaDkIyK9KnGYTqghk_zJWPkgsEzj7wtiCRMPMCcMdlasyLDPfGseseqvCCIxUZHSc7qbuobNGqSQuBh_hwpjpiSIMlq_59La_sUveNK-ZIBZ6_PeJXqk_4Ys9nCpkwFb1KA6NkVslQdm6eSg54XBik7PYi-OrdALFlNYxeRC9P_jN_gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیفیکس اعلام کرده که این فیلترشکن توسط تیم امنیت
پس‌کوچه
مورد ممیزی امنیتی قرار گرفته و تیم توسعه درحال بررسی نتایج و کار روی چندین بروزرسانی کوچک و بزرگه، تا در کنار حفظ عملکرد و تجربه کاربری، کیفیت و امنیت برنامه رو بیشتر بهبود بده.
این تیم گفته ممیزی‌های مستقل و همکاری بین تیم‌های امنیت و توسعه، یکی از بهترین راه‌ها برای ساختن نرم‌افزارهای امن‌تر و قابل‌اعتمادتره. هدف این فرآیند، شناسایی و برطرف کردن مشکلات پیش از سوءاستفاده احتمالیه و انتشار خبر این ممیزی هم بخشی از شفافیتی محسوب میشه که به‌گفته دیفیکس، کاربرانش در چین، روسیه، ایران و ... که با فیلترینگ دست‌وپنجه نرم می‌کنن، باید ازش مطلع باشن.
💡
defyxvpn.com/download
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/ircfspace/2592" target="_blank">📅 18:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2591">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c4N9KgDvnItg1pgCuErwRpGIS3APY882mMXUeQyiYFBboO1V_UlKzlDAV-BJcZ3QKB9ypEzGEfrk7hShCzMydKgPh2HBgn1pZaO_PVuHPTw4BArXLf4K3I953OmAwMQUs_10yPHzU8oQY_cS2QbKYgg5m4ylKhAzOt5J41T8qOGO-XcltS8iVMQljt1mDI41Dh8mdRDh5nKWgsw7_mWqzoqGlexmXdCxI7p99fKYPjaQieD1d-9qxWNZkPUZUy4KeSRp91Eyt7IUgdIkS2wYMAgUZUXSWd998KrwmruaaZO-KUPeds9lfY_CBklcgh8AIXizJ5Io1VCbVlLtkRh2sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه کد QR حساسی رو می‌خواین مخفی یا مخدوش کنین، نصفه‌نیمه رهاش نکنین. ممکنه اطلاعاتش همچنان قابل استخراج باشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/ircfspace/2591" target="_blank">📅 18:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2590">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JDsGRWKBqmIRhDnyG0dkqwMa-PeErb3nlbOFfZkdlC8Bplrm2ckcg8MuRJ9xSZx5Cfafxrlm9NvA2_Wbhkzb3E4yS14AElI7t1dCDDStEH0Otl60L19tV1ueYAfmK3ZB1C6kTjUIuCmwGLs_l5wmttvk4ilYWdOI_UELdIzF5qqIs2b7f8lp3b7ZAfeSCR1jB_SL8AFSXsQU40MvwXN9hWX5Uq1hFBB-bWe8sRLQUN6uTXRRTZb_jcik8HH9ZZhkPizLoF4trz-Bbf5li3E3LTF3mne-YdxEbvo-se682z5RXynC377QcmPn3m08Po_CBlggpEXXt5zS2c33PSGi9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سم جدید
😃
☠️
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/ircfspace/2590" target="_blank">📅 18:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2589">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Cj4hLJH93wsYjZecRcUfCCKddtJS8qPYc3IfQHxLHWCQg5BljncDf9wTcFn39hkSPhspHRkTKq-UciavxN2MoTOZ5yI_xlBqveXsh7ZPrmBPKXNmBOspFnG146RvUJ9LqMA-5cR_A_je3T8vYEqDAuDpLHYyzWdCdyXBEjV_TOkR4DvG4iH01M9k9a1jlo6U4t2xPvkpKy5rD3LCdBWNKDJA8xxNrRO3Nd3eSnSGWKwMYdFBZ3U1KvVb72d__L6lhQMoHi-eBkHSCLRGlvulh1yuYEq1BD4-M2cS9oz7B5KXnAu8zqbAFact-kmtytgI4cXhVkac4cKYxzU7CFTmXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات معتقده "قیمت
#ملانت
به اندازه سایر کالاها گرون نشده" و احتمالا باید بیشتر از این دستشون رو توی جیب ملت فرو کنن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/ircfspace/2589" target="_blank">📅 17:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2588">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Pnz9Z1g5dGVgeQMFxJCWp-saCjn7DMWqq81FyAwRqEudXolsunfSIxdDYnWTmnix-i9l55O5a0GP02CZazNUe8oz0jcG_ccSystWta4UkgUYPoq3EBmHQefMv2jj6LOzc3XoKrU7ykhoNDm-UJXh27eZ-JHOUT7vhRX9sUhuWPUQkY9_epcTPTVGVKOL82JyCmmXav7xqqwOrE0rxoM_jsH_JO_C1bfBAeACirIvue5X19FWF2RdN5bYWvpYCoG3r_Trb3Qu9C4t77uwOlTbzfj29-H1idCwaWaubgl6C54DMxIdQ0IiMQPTWRiErl50PvzgbNV--R_x1k6ZhXKTyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واحد امنیت تیم پس‌کوچه در ماه‌های اخیر حرکت حمایتی قشنگی‌رو شروع کرده و اپ‌های VPN متن‌باز (که در ایران مورد استقبال قرار گرفتن) رو تحت ممیزی امنیتی قرار میده.
طبق آماری که دارم گزارش این ممیزی‌ها تا الان بصورت محرمانه برای ۷ فرد یا تیم توسعه فرستاده شده. اکثر این اپ‌ها درحال کار روی بروزرسانی‌های جدیدشون هستن و بیشتر از نصفشون آپدیت‌های کوچک و بزرگ داشتن.
این‌قضیه تقریبا برای توسعه‌دهنده‌ها و جامعه‌ی هدف برد-برد هست. اون فیلترشکن‌هایی هم که نسبت به مشکلات گزارش‌شده بی‌اعتنا باشن، به مرور از چرخه اطلاع‌رسانی و توصیه به افراد کنار گذاشته میشن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/ircfspace/2588" target="_blank">📅 17:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2587">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gypgLGqge_gxCsdee9zk9C-5AmTO2QLKkq6rRoqayvbWIlYHh1L0_ZMe9rW2yKncqFGyeNf3XOhhguM4fnK2Ws2anX0h_oBM3XPQ-pYT38xl4xor9BIrPepMLFid9Jjrv16FWFme5BhKoesn5e8vUYPdQGqd14jR8yFKzVt8CBXaJSF7gbhjThtQ4U9ma7fDyBZnqCszHiY3Dh0oKwwihtGyXspOoCodKQCKVwLg8Nh70nvzN0ocyUoIP1UwJFYTIQlGk98-iWy_lJr4JYdBQFljsWaOdBDF1nycvNekMapgV9LmTwVIvPSNpMe-hHIXyz5MLNIJGraEhB__p7_udg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجلسی که خودش کارت قرمز داره، به وزیر قطع‌ارتباطات کارت زرد داده
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/ircfspace/2587" target="_blank">📅 11:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2586">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ioK2D9Q3ssT9C5t3Hy96x84N8JwxhC0Va7klsqv8BMEM-_tHGPIrgtPmggkiOUsybhJMtiawW0s8bGaQWi6b4PChwC-FVjiL0c_gfuzHaQDgaSEjq23E4DbJWWvEaI7gKcgnPzoJww7IoJXv7d57sTpgDq74q2eUSi-CFHPQBlianjB5LPUCubAo5d53Ky3daMH4qNGbGPn6naUtKTXKxgN9qr_44rW-ZOR8hqgJUeRRBM7-OhEEm3A9zscYfaoaOHI87kxEL7bQYrabJBJ2AsEJawfW76aiSIrOTegNogTMhnHFCjD8Oc3RBBjo4EBE_RW13rEsAUluvf2oXm0xLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون ارتباطات و اطلاع‌رسانی دفتر معاون اول رئیس‌جمهور: طی ساعات اخیر اخباری کذب به نقل از اینجانب درباره رفع فیلتر اینستاگرام منتشر شده، که کاملاً ساختگی است.
/اقتصادآنلاین
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/ircfspace/2586" target="_blank">📅 09:11 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2585">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s7LbBJgmp9BimXBrEILbvxtoXYpYnblI66Y2Wz36_yXitzccBhIYWIY_pKDH3AaV3OC5Kh7Yq1OxwSqFIm6efaQZ_rOuxogJ0eGPBg71aadYOjoyz7UPq7TYwZHHqSKVWrTifqMVNU-H7F7wusbkWRW0Da62vJGZT26g0EHR4Fs66JZNe18O_25eNXGL4rrNcMQJCtUydszYQ9GAo7Rl2WE6GfOt9HuLxZ-UU2mgzZG5v4Hx3W0yfdW2W2fnpE2XOmgFFGaDtI-KvcvypRTc_-REgpizgq1iD2-oOquR5yWrDwATiEC2pcHaKVxRZAp6V4enQfF28pVs6hfkvPx12g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاسپین یه ابزار رایگان و متن‌باز برای ویندوز، مک، لینوکس و رزبری‌پای هست، که دستگاهتون رو به یک هات‌اسپات مجهز به VPN تبدیل می‌کنه تا بتونین فیلترشکن رو با همه دستگاه‌های خونه به اشتراک بذارین.
کافیه لینک VLESS، VMess، Trojan، Shadowsocks یا Hysteria2 خودتون رو وارد کنید، تا ترافیک دستگاه‌هایی که به Wifi کاسپین وصل میشن، از تانل Xray رد بشه؛ بدون اینکه لازم باشه روی تک‌تک دستگاه‌ها VPN یا پروکسی نصب کنین. درضمن اگه تانل قطع بشه، کاسپین دسترسی اینترنت دستگاه‌های متصل رو قطع می‌کنه.
👉
github.com/Iman/caspian/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/ircfspace/2585" target="_blank">📅 09:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2584">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/piUSvni70yJhnRcbyNoFw4SWlPU4mvF6IN2hPb7viTGzM2_olZbRPete3kQ11ZVldet_UGPVgJCaLkinh2e03MNms9-O0W5RX7CMVccpDxlLcEX0b27I-mvzGDL6SIM47KHT6fCnuKdeH3g59x-8ccWM5mashPA3pQCnnmAh2ofoxt94HfqT1XuXcswCnWcuVYiew7mI1Tt8LsHZDAO6pjRLUEmyyasanrPfmYqfwgbJHsKRlgZQxBGhA4LVdwEL3GzS-i3Tg2ocXbrgIasnIpHmZX3CPYNAYPV7t-WtAENARisViwy715hLStDzvwZCK99Kz3l7AoLAZ4B2ncTt3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Misga یک پیامک‌خوان متن‌باز و رایگان برای اندروید هست، که به شما اجازه میده پیامک‌های اسپم، تبلیغاتی و کلاهبرداری رو بصورت دلخواه فیلتر و مدیریت کنین.
این برنامه چند فیلتر داخلی برای اسپم‌ها و کلاهبرداری‌های رایج داره که می‌تونید نگهشون دارید، تغییر بدید یا کلاً حذف کنید و فیلترهای خودتون رو از صفر بسازید. با Filter Studio هم می‌تونید با Regex یا متن ساده، قانون‌های جدید تعریف کنین و حتی از هوش مصنوعی برای ساخت الگوی فیلتر کمک بگیرین.
👉
github.com/mirarr-app/Misga/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/ircfspace/2584" target="_blank">📅 08:53 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2583">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lxHVy3vYS6h75uwU_X606yXIIaySwdIPk4nJfdXyTO_d04Bw85JdItrFJdnqGkFgtO7V13g7RF5ae4tK8nckii94BRuGx3Abd4t95y8uxeVkah_dac8MCx_j1rD4Hy5kD2JVzRlbElAVw0DgxQYqFnduMjVriry-vBsR-lA3iyXcFNg2hd2cweMxTdjByUG0IHbcrYXaILkPWI3SZCX9Rl5B12KNJ4moDQkMksVhe9xPD2pCJAVYLF4ad72Gbcz6-Tej89GdiWv7BLAQuH2oGmDdwWq6vPEPaG3JUs72ZMjWypoI-26kJrH8u_7JwBXSaXoIpnKTraEvf6lX6wghkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چند آسیب‌پذیری بحرانی در RouterOS پیدا شده که بعضی از اونها در قالب زنجیره‌ای به اسم MikroTrick در حملات واقعی هم مورد سوءاستفاده قرار گرفتن و می‌تونن در شرایطی دسترسی کامل به روتر بدن.
از طرفی Shadowserver در اسکن اخیرش بیش از ۱۲۲ هزار MikroTik با SSH باز روی اینترنت پیدا کرده که حدود ۳ هزار موردش مربوط به ایرانه. این عدد لزوماً به معنی آسیب‌پذیر بودن همه این دستگاه‌ها نیست، ولی نشون میده تعداد قابل‌توجهی از روترها مستقیماً از اینترنت قابل دسترسیه.
اگه MikroTik دارید، حتماً RouterOS رو هرچه سریع‌تر آپدیت کنید و بعدش لاگ‌ها، یوزرها، Scriptها و سرویس‌های ناشناس رو بررسی کنین. SSH و WebFig هم بهتره مستقیماً روی اینترنت باز نباشن.
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/ircfspace/2583" target="_blank">📅 08:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2582">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Bk74e6yU92EPTNHGIf3jdcB9ss1SfpBoglZA_NbRNP0brm5Tz7M8gYSIwQu9VtJebve_ArJPE_250yZhWyfyN0zX4gO3kG8oVLwhSDdk7u-wLNT-Vx_3NtZzZnEyPhrqOULpOh-4nFbREsckWMqpbemp-0b9SYkSGJ5IUbclCxsl4UkzUIjVgk4rgRKytmazaK_5LYNszmNMzUH10BQwhqvL3rt08Okj1DZmCiL_7QKD7JtpmjMU1HUmot5mW2G7beqzyJKTyqnlTex0UsHiCM3rsQrod2B8tEnSFdn_qETYyy-BoQrXUCnKmod5MIv5TTTOq6yhY_kotwL0EWCYiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر میرسه یکی از زیردامنه‌های gov[.]ir به افراد دارای مدرک فوق‌دیپلم یا پایین‌تر اجازه ورود نمیده و حتما باید لیسانس داشته باشین
😁
©
SePeHr
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/ircfspace/2582" target="_blank">📅 07:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2581">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rlcI06SqYxclYRzb3nE4dRVXZyBhOlX4L3t3FkoF109nMQhhIrzNnT-qQEUlkqYu6AYrbaLkWeLJx4jrKVOYNNkFVTMrCtM0jPu84MvJzS2PauwaLQB6FRskLsLX7_6ud6PMypgxpBYodhs-VvVAk1T5qWYWSlUvDfs-2uMsML4HScOEoKJ_FsJ-CICaHZdY0HYIKG-gK0_eT8F0MXMTFPwlR_KK55vdTLSAPalqdcOzbp7guzyk7f9Xnw1cipw1LTFQE3dQ_HZL36kF3-Om3J1fttRqrb2-Mnflo7_1y-KvxwrB3jEDDM-L-8sMFuXAE2Uf0j5kUWWWgBlJ4bRWBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن متن‌باز و رایگان دیفیکس اطلاع‌رسانی کرده که امکان تغییر زبان رو در گزینه Diagnostics & Experiments مربوط به بخش "ترجیحات" این‌برنامه قرار داده و حالا کاربرانی که به چینی، روسی و فارسی صحبت می‌کنن، می‌تونن DefyxVPN رو به زبان مورد نظرشون تغییر بدن.
البته این‌بروزرسانی بصورت آزمایشی از طریق گیت‌هاب در دسترسه و بزودی از طریق استور هم در دسترس قرار می‌گیره.
👉
github.com/UnboundTechCo/defyxVPN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/ircfspace/2581" target="_blank">📅 07:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2580">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ایسنا خبر داده که
#قوه_عاقله
بخشنامه مربوط به "ممنوعیت استفاده از پیام‌رسان‌های غیربومی برای اطلاع‌رسانی رسمی دستگاه‌ها" رو لغو کرد.
😄
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/ircfspace/2580" target="_blank">📅 07:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2579">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">حکومت در حال تهیه لیست IP کاربران و در قدم اول مشتریان دیتاسنترها است.
در این طرح شماره موبایل + شماره ملی + آیپی به هم وصل می‌شوند و بدون ثبت آیپی در سامانه شاهکار، دسترسی به اینترنت ممکن نیست!
نقض حریم خصوصی کاربران و حق ناشناس ماندن در اینترنت با قدرت در حال اجراست.
©
souzangar
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/ircfspace/2579" target="_blank">📅 06:59 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2578">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ruelaJeoPvlf0hWYn_iWjJCzLAX5cw4oXUXddAMjb7MIP21zKuoxV-PJip6CBwYe6uW3Gq7Xs7khhfV9gRcYIwB0qcggviGx3ZsiOOttPLCCuUbVAJVEuNJClLfzq_2uuSxl2PuEcbmTaM_9UNFW52ypxvGRVRs03ddv-OlO2bHY0MMr_Q5lO2JToaNbt57F-uIJL60bHIwVLmLJLf8UABjaA3hKS_1v0UCnR4qTbBvwkrWwgNYAIJTjqgzgSlRDnIGE_0rlQMcFpKM5qOsruKdWtYkNfLIuw8M5gcbTZ_EeN8IvyTLA4rM75ot24SBpu9Cex0DoDqdO6GlopOtI1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید از هسته متن‌باز و رایگان Aether با تمرکز روی بهبود سرعت و عملکرد منتشر شده و مهمترین تغییر، فیکس شدن مشکل سرعت MASQUE روی HTTP/2 هست، که حالا با اصلاح پنجره Flow Control، مسیر ارسال، فریم‌بندی پکت‌ها و MTU داخلی، باید در شرایط مختلف عملکرد بهتری داشته باشه.
از طرف دیگه، محدودیتی که بخاطر بافر دریافت TCP در Netstack روی همه ترنسپورت‌ها وجود داشت برطرف شده و این بافر حالا بزرگتره. ضمن اینکه می‌تونین مقدار بافر دریافت و ارسال رو بصورت دستی تنظیم کنین. البته برای WARP-in-WARP چندین دستور جدید هم اضافه شده، که اجازه میده اندپوینت‌های مختلف رو بصورت دستی مشخص کنین.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/ircfspace/2578" target="_blank">📅 09:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2577">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cmkmGUFHaD6A9g0boKwqUJxDDFo4qCc8U5_ylYOkd0z-xvCVnNVGf9lCSD5mxmGJ42Leegl2gciHiHqMix9q2MYUqNGSqcR366EAdCIjJ9ydFwZZPzktwH_U0vOSbM9agWVaWYHc_6zmz64IkSjsFg-lWTjblm61TtQ0A8JW6AcWCnSpC05HW9Fe3hK3-dXu-cVCxdbf_G99-HK_VXqWc9OzQEZfQ_6mmEr1YxIgFlD_7vowbE9cYz2Xj1EIAGqlhmdFLGZNMx8QzkfLa1biXXST9foDG2QovNaklwgKRMDWRY6Ib9Irv6oVtFSlg3FbHCPhYhCrthBMOrkaywaU5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات در مورد ۸۸ روز قطع سراسری اینترنت و بعد از اون اختلال گسترده در سیستم بانکی کشور خودش‌رو به اون‌راه زده و با سیس عقاب اعلام کرده "آماده انتقال تجربیات سایبری خودمون به کشورهای منطقه هستیم".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/ircfspace/2577" target="_blank">📅 18:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2576">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/H60H9h_4xWEsnQXpNCKWXvycTdqYKOxLz-nP5226gw9n8GgOLQBtrr-9dnOl4BaRJGGR4Iaz61ilCIcJ87YJFERFsgXpKvBozz9s3jzdqLsOM7FKK6pkRn13fGbisMZXSrLo1PsKY-AcOHThe0dFvLTGwaK86kNojUkcfFD2euec_GPC-jQtKLfnwna5-Tgl1SnXqjdWcSH86GSbTqLm0DyQ6MzoLIYUxVAvlBFRa3VDZ3IZFznc_PR5gDpm_YEJdf3TW6sWnbBLKelrZVB1hfXAq20LqNi92W8hxaAze2N78xUje_BrYryxi6HEFy1KCyOAlSFiWGraU__32ZDVvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه باگ توی واتس‌اپ اندروید پیدا شده که روی بعضی گوشی‌ها می‌تونه اجازه بده بدون باز کردن قفل گوشی، به گالری و عکس‌های شخصی دسترسی پیدا بشه. این کار نه هک پیچیده‌ای میخواد و نه دانش فنی؛ فقط فرد باید گوشی رو در اختیار داشته باشه.
ماجرا از طریق تماس ویدیویی واتس‌اپ و گزینه‌های Meta AI انجام میشه و روی گوشی‌هایی مثل Pixel 6 Pro و Oppo K13 جواب داده، اما مثلاً Galaxy S25 Ultra جلوی این دسترسی رو می‌گیره.
©
notebookcheck
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/ircfspace/2576" target="_blank">📅 18:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2575">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">معاون سیاسی دفتر رئیس‌جمهور گفته "پزشکیان معتقده دوره محدودیت و فیلترینگ گذشته و اینترنت طبقاتی و فروش فیلترشکن به هیچ وجه قابل قبول نیست".
حالا حدس بزنین رئیس‌جمهور و رئیس شورای عالی فضای مجازی کیه؟
جواب درسته؛ مسعود پزشکیان
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/ircfspace/2575" target="_blank">📅 18:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2574">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DOOHGwKqf5sMEo4fR7u3C6N19EtYQjVECYEoxy80hspOuQx-FavgFJELwal4DGTqS4jYpnf8RDRCcEOXbtuF_L_9wDCMIjGbtY259_AFm5uT1ITd6v-BZwL2_W3iqOIYvHz1DNybmpktdIz8iCYZQNSoaTK2-9woi4lDedGaUgORDwBnPQZBIsq9ML-mVwhAbXWz_D3lD_951l-i0eF28xqLPhSJaqs8uJZaf85Qqj0vmMQcHuuGM-4Z_1a9azs5BZyQN4oQAc2888oM_gwOaeLYvJBmK7vQ7YRVY4Jlqit9Y6_aOQEWeEfKzdbFaRzYPYZbn1gIbzNneB9VJqj3HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Echoes یه ابزار متن‌باز و رایگان برای کارهای شبکه و توسعه هست، که چندین ابزار کاربردی رو یکجا در اختیارمون میذاره. از جمله امکاناتش میشه به پینگ، اسکن پورت، اتصال SSH به سرورها، بررسی اطلاعات DNS، WHOIS و IP/GeoIP، ارسال درخواست‌های HTTP و مدیریت DNSهای کلودفلر اشاره کرد. همچنین امکان بررسی وضعیت سرورها از نقاط مختلف دنیا و مانیتور کردن آپ‌تایم اونهارو داره.
👉
github.com/SinaXhpm/Echoes/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/ircfspace/2574" target="_blank">📅 11:52 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2573">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JlZBpB-Dr1MNF4uRF8xKUvpYw9wcnkyrINQ1DFN_ZI3qp8oAEawkRz5G-2LRh3MRUY5rl9wJa2BHDGipP0qniT-_LiYbfmDKDfwONlzhS8OGDx4jZJx1_1CLEzWUch_OnAFho11_bv3wIFPvthwiiB_GYHgnW8kHea6ve4hrz7EckNHtX9a2LSWHSvtOszpI0IpN35xiHADQs9IXI6WqyO3XhMnSKT3ElUzsFaWEbCCPDijt49bv7cS0emvzo9F4D3cXZp9DzQVQDqKXfErGink8XpTr2qUhWR79QGdkRwInCQ9NWhq-Nwcth5piTxZCx7fjJqfP85fJXOJH8TsWuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت بانک مهر ایران!
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/ircfspace/2573" target="_blank">📅 11:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2572">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DHPyLBW-GHF2OX5bxC8JLiEK-uvam9BqrTf02GQseozWPsEmO33naVdnunFm_k3EmpxnC4CRdf3DA3Jk3uoxm78AllqScyHSUdDe33Y4U15ksdLMNUFz2YsHFo9EaMR4Bxf-k385KtwtTLEu6Z090WmwCNHOtOqo5rEwtupmwAqEL2EcHjgPDFstHUeFgPSTN0inLuSdC1uAyvo5Ajj4nUzZV8IOsGRpEA7y6jrfsIcraV0m0DMK8bB5PSThHfDGlm2kjzFymnMiLIxXEdxKTlmu6Bl_ZBGxIQYLMyBakBlOUbqCZsQoJyEzHUs8smB4Y1sZtdSd45C9toKhd8EPFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتظاری که بانک مسکن داره، ستودنیه!
کاربران پیش از نصب نسخه اپلیکیشن همراه بانک لازم است، ابتدا هش نسخه دانلود شده از سایت بانک یا سایر منابع را با استفاده از الگوریتم استاندارد MD5 به یکی از طرق معمول محاسبه نموده و مقدار بدست آمده را با هش زیر، مقایسه و در صورت یکسان بودن مقادیر از اصالت و یکپارچگی نسخه دانلود شده، اطمینان حاصل و سپس نسبت به نصب نسخه اقدام نمایند.
©
alirazzazi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/ircfspace/2572" target="_blank">📅 11:41 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2571">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gPCH9sjZIacHhlkb79QonyN-6kY8Or62NvJisBCdDD2fk7iFZK80vZzT2_oS3d-hBq5PFobh4MZRnPjgY_BYXfkbsYJH4eQ74ZpoYyvywFNLeYNE70XVyLXepoOV_-Tty1eLzJZKNaBUlBqxdMRq-obXftF2d0mdcSWAvKVUmZWaOQGN7ztIkTLeDmltRk7aHEhuE0qi4-G9At-4YDvrtKLtHzQsgUf-LbFqRrPp1e_Y4J14WNWNgsIz48bTo1PUHvwn-VlpE6rgTcKPNy5IfwYqJfSmHBv059UHHqxcwHeDn8YUClGsCQla4RjRPXitd87ppD76MGjxdJXec74eBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چندروز قبل وزیر گفتاردرمان (و فاقد مصرف) قطع‌ارتباطات گفته بود "اگر استفاده از فناوری‌ها به نقطه غیرقابل بازگشت برسد، بخشی از حکمرانی کشور در حوزه فضای مجازی عملاً از دست خواهد رفت". در ادامه "بستن پرونده فیلترینگ را یکی از الزامات ارتقای حکمرانی در فضای مجازی دانست".
فقط نمیدونم مخاطب این صحبت کیه! اگر مخاطب مردم هستن، بدون تعارف بگه بیایم برای پیگیری و حل مشکلات وزارتخونه آستین بالا بزنیم.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/ircfspace/2571" target="_blank">📅 11:34 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2570">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">دستور پیگیری فوری
#ترافیک‌خواری
اپراتورها به کجا رسید؟
چندبرابر پول اینترنت میدیم، چندبرابر هزینه VPN میشه؛ تهشم آشغال‌نت تحویل می‌گیریم!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/ircfspace/2570" target="_blank">📅 11:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2569">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MspzTFdEWMVhSK62kAPITJcJ0G5fLp4E-cQLLEncvKFm_LfxkNPCPW1mZMSYuYupjPlCd0eVwKKo8qkwFhOq113r3y7SzrvWV28ducsZRxh1mmK442gWselLcmZtEDjubyH-BiqKz7yhhLGjMIQMMJDuedsCefPdzqEkVr607239Dv1F6q1gOZuO_RRnk5lCxc9dTzInTrL6QuxVcNXdBrQ36jNDvdcx7e6rNLzgW5Y5ad6iI9CyqJ3SaZwQ5ev0MYfGzzd4MUdOckaBb0XxBV-fdZ_NIccu95vKIJ0iY74CTaTf2A-kaN6h3lNNOgleDavkyqoDWx8kJ4XlQtEalQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پانتگنوس یه ابزار متن‌باز و رایگانه که برای پژوهش و بررسی‌های امنیتی روی فایل‌های کانفیگ VPN و پروکسی ساخته شده. این ابزار بصورت خط فرمان و نسخه تحت وب در دسترسه و می‌تونه فایل‌های رمزنگاری‌شده با فرمت‌های اختصاصی بعضی کلاینت‌های اندروید و دسکتاپ رو بررسی و اطلاعات قابل خوندن مثل مشخصات سرور و تنظیمات کانفیگ رو از داخلشون استخراج کنه.
ابزار Pantegnos از فرمت‌های مختلفی مثل SlipNet، HTTP Injector، DarkTunnel، NapsternetV، NetMod و Happ Proxy پشتیبانی می‌کنه و برای تحلیل و بررسی کانفیگ‌هایی که توسط بعضی کانال‌ها و منابع مشکوک منتشر میشن، می‌تونه مفید باشه.
👉
github.com/FrontierTM/Pantegnos/releases
💡
frontiertm.github.io/Pantegnos
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/ircfspace/2569" target="_blank">📅 11:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2568">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">از بین همکارا، اولین نفری که تغییر شغل داد و رفت سراغ آهنگری، شدیدا تعجب کردم! با اینکه خودم کم آورده بودم، ازش خواستم جا نزنه. اما بعد از چند جنگ، کشتار معترضین دی‌ماه، قطع طولانی‌مدت اینترنت و حالا تداوم یک آشغال‌نت پراختلال، آدم‌های ‌کاردرست و خفن زیادی رو از نزدیک میشناسم که سال‌ها در حوزه‌های برنامه‌نویسی، طراحی، شبکه، مارکتینگ و ... فعالیت تخصصی و رزومه قوی داشتن، اما در این چندماه رفتن سراغ مشاغل غیرمرتبط مثل نجاری، دست‌فروشی، مکانیکی، واسطه‌گری و و و ...!
لعنت به جمهوری اسلامی.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/ircfspace/2568" target="_blank">📅 07:54 · 03 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
