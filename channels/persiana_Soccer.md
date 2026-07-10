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
<img src="https://cdn4.telesco.pe/file/CiZGMBNWMltb52ip6FFVQ_MdPlrw446EJCS2fInK8He-cmh35qVVrv5qRFzT8dRUXgf4nxKz5EcQJ942ev-oQpn3Qd67Z9o__p7n5FUUHZ0J50uXGBiufluMo-bYUE1v1Y2DSghfpZIVXEiEU7reW0ukZzq09n34joeapxxJthATJPyvJ235-Wtia9gtDbFLgJhhnRBqsSygkCCFfExnmUtko5yh6YUtffsTQKQeB_UD34qlP_3qG-365qp924abFFBfp0xKrzcweyHx1Od-TEyVY8jDvdbVaVzKME6G4aFrjOkGj23KYzm_hfvWCbNXfSs154KaG3t7d7MC9PGnpg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 423K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-19 13:54:21</div>
<hr>

<div class="tg-post" id="msg-25350">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MVjrPLcUGhViC4Xdn3s5ljrZL4hhHzeMof5X1euJgBUjd_I3Bln2FKQmc7ibm5QnuwHma4uuwa9jEj6vJPiFcS4UbFv8Iva348eBUejd3LgGXLTbF-8nyHvGtXoKWfHsaW8AVp0pFGQZcVoHX4K-edRDswU6sAPA5x-ZgoKmIX2ULWPkoniSL3-cJswEPWkhreQ1DEUThFgCPJpYeMgelzoZmGewiAMNQdLLIMg5KYCbjMrpuKoB1CX_7E6OXSWJA9zPOZg3zWGCg3i8FIebTn3KLtk2eGreGst-b8zMzXu3aDJ1xxdeL6he0Fw-XLZrc4XQAUji4YAM1ITtXFRBeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
کیلیان امباپه به این شکل به مایکل اولیور داور بازی امشب با نروژ بازوبند کاپیتانیو میده که بره به شوامنی بده؛‌ الحق‌ که لقب دیکتاتورباپه برازنده‌شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/persiana_Soccer/25350" target="_blank">📅 13:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25349">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VR4u6ejCdOHPKxH33cF4bV4Xa3beSQNhD_XVhLXaiWFTSRx20JLkVgp1WE3wCQIn5cNwbtyK7SORtRG8g3yC2B85V56JjQX2E7WrLV05h5LgJJK_YdxFZNTO7-hSLYe8wUE7k-JTL1tyNbPDZql7GJY0eD6-EOMKa4luNwyhmHBRBqQr3CkegRswu_07cqgzWk6BXJMX7WY5OiPJml4-TbdUKIruE_-LiN1zadUm2xbBgFBgfCEPQfHvnODipNCekIsAcjLC0GuwSsaOHmVlKxzQIs4IEfgNEabAJxWkpJ1rL8PNiz7Gw0E3LeqNQ-Yd3OQWYF-4-o4kwr8rjU3CAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال ساعتی قبل باباشگاه آلومینیوم بر سر انتقال محمد خلیفه دروازه‌بان ملی‌پوش ایرالکو به جمع آبی ها به توافق‌نهایی‌رسیدند‌. باشگاه استقلال بزودی 60 میلیارد تومان به حساب باشگاه اراکی واریز خواهد کرد و رضایت نامه خلیفه دو…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/persiana_Soccer/25349" target="_blank">📅 13:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25348">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VBNkh_stvNK6hNnSBABKwqCe0lHryqqwP9BiY-0UhnJJCO_N8lTZH2vngaKPwbRk9GKS_oh3_i4-Ev2f8VKaGX4MM1l0GacutDW-Ahk1vFwtkTYDJ1ZiEwz6ki3JTNQAlR9fNgl6RUedio1FuLVxrSI1y3KWilsIM6N4FZEp8Y-IUpjaxZ0mcQPEhaxG2MYUdnla5ymY1jguRGfFBf3jSwV4pf58xWRCaV1odxaAluGkf4XKHjIxqa1YucmugMykjaYFU20ksvqobkPhRx-jPlU_ifdPZwJcDwKawVGw6iz8xu2ejma6biov2S_eY1wH3FJIFmQJpd3pzHiVwC2uxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنان چادرملو به لیدری رضا میرزایی وینگر این‌تیم سرود قهرمانی این تیم تو آسیا رو خوندند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/persiana_Soccer/25348" target="_blank">📅 12:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25347">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PN0kcgVjIRl0N9OXtFFAKmrEFwDooGG85X98Ks-kefAaHj-Kcukeq6D0d6AFou3ZncXK893aTL7JEhagGmlY7NY2lE85vJez9AbHC7fg8eot2AO7yrhZOq7VFDhSTlUWxROMeOHqWKexeRJDYFrJTBEJ5celCP1mhTb68JCTPyNG9b5RpI2L5Q4NwF8gXiSX0wNKN4EiLZzFp5HVQ7WjRSYv0H0EooRXu7lTXMvGr2LM_uRDdXoMPvGFAEYCA595CONeFnGEGULULIUOy3MsLhDAhiRpl-gbgmHxGf7r8OLSTEMl9P7DczhVJr8pxDQCWAIbedeW2H73e8IsijbbKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق اخبار دریافتی رسانه پرشیانا؛ رامین رضاییان ستاره استقلال ازباشگاه الشارجه امارات که سرمربی‌آن‌مورایس‌است پیشنهاد دریافت کرده اما به مدیریت باشگاه استقلال اعلام کرده درصورتیکه کادر فنی آبی‌پوشان به‌سبک‌بازی او اعتقاد داشته باشند به قراردادش با آبی‌ها…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/persiana_Soccer/25347" target="_blank">📅 12:47 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25346">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">📱
اینستاگرام دراقدامی‌عجیب، قابلیتی اضافه کرده که با آن بقیه می‌توانند از عکس‌های شما برای ساخت تصاویر هوش مصنوعی استفاده کنند! اگر اکانت شما پابلیکه این قابلیت هم به‌صورت پیش‌فرض فعاله؛ به این‌صورت آن را خاموش کنید که مشکلی پیش نیاد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/persiana_Soccer/25346" target="_blank">📅 12:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25345">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YmABbc4rhwADA5JBexbIQA3s3E8Kyz2_sMFpRiYGJvTBjKDSQniNlYWs-mjp6Vl4oJ8LlDaQaFUMIXdywNOttzIMmR29ABgnDuQUtCaDgPzVVHUBGkfL5PtV80Oul46F2dp-hfi9FvvjFOVJkHsrvTLOEjNTJZpjCNrsRQp-nyH7gRdl-mv-YsFXLsthCoOsk3ZSt02QjCRXYbDB1VTYrYFvKfCEI8JhLRfjbw5voOrlgO3aU2Og83D4CahFvDabzcRJDwLPnTylIcwXlDZQ9CnNQarpYyJ7N-aUw2O8mL68c9reppUiiC-1JhMtWEBM5rWw6y9cE5mgTJrCOYsgpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌چهارم‌ نهایی رقابت‌های جام‌جهانی 2026؛ برد شیرین و ارزشمند خروس‌ها مقابل یاران اشرف حکیمی و صعود شیرین به مرحله نهایی رقابت‌ها. اسپانیا
🆚
بلژیک حریف خروس‌ها در نیمه‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/persiana_Soccer/25345" target="_blank">📅 12:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25344">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J1IIOYSsnNm6eHigd5uFKglqDxNt-UzEw63oAQWvdmqIikA4FO8jcPqiFdLebjIK_PAWciAtXoN38xlUTfvrKeMMbF67wCYtKRv1B080XIZsQPs47l_MsJORYCMm4SpXXt6ZgEYXCY7xOdi4saH7KGFBkfi88Y2FpQPSAHgPRNg-b5twkMl4usK3dzLysok21RI5QMrt2f8-S6m93uDvroyL8ucRd2Uc_V5JMilc9mA3WtBndxdYXAFij070KsBiProwrIFVIqlPtr01-_1iaJ0hQX7vLG7dUr9vXwP4lqQzuLBkrnPDAnLUW-jlqVHi0BN6j35jxfxStExkQGBwVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌های برزیلی مدعی‌شده‌اند که نیمار جونیور ستاره 34 ساله سابق بارسلونا تصمیم گرفته که برای همیشه از دنیای‌فوتبال خداحافظی‌کنه اما نزدیکانش میخوان او رو از این تصمیم عجیب منصرف کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/25344" target="_blank">📅 12:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25343">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c669eea570.mp4?token=fqRwsCoiAW4NWqCNvkA9BeMLJPze5flfmfHWpWuSZrzBM-oWT_zNgz-Lj0oFeTaSiY8QOUC-POSW0Xasod8DqAvWxVs-xskRbzOZgt0BwkSHRzy2_V-1tOuBreeJZr5cqa9QL_BiEckhL3O2dsDxDtCqjISFO6HUx_klgzO4ejd7VwYrC7Og8xYKHeiBgp4WPez8mwTFD0bhpuIfmqMm_gw_gxVcmfWvGpLUBhAwAfbVgaDg8NNbnpK5Ci37zIymOq2iO4nZojtnOgmBpJEkxx6xSD8S-ilIRO9OlIsjp-ITqzgj7le0iprGOtnX3roLakFR9IpfsGZZqKwI3C3AArUvAFAUU4LxCpW7izg1hnJ5skceJXDZCIS28pj95ThrUuusPDzv56kjx6-_BM7b9ye9JMy4B1Afl7Ad06xB9XYblM6H0YgRpynMNFrcvXVgUOwdN3KSXJqI_iYZWX4P6FLq56ySF1aQDounzlfxk5O7oF6pQvbC8eZnBRI1NaNzix7bVo0_tscq4JkhehcxPQG3vQktZYRsT9WEbX7UEFooZG2wF9o3SPb2Bg2TMFqQoUCiZdTm1qwwTK2lW7zULzgVvQx6zw-PzMgAys28DAO1s_1orDorN2aV9jDx5MVBnOaS830zLvtQoRr__xFSRb12Ky01Z3Y4J7jlGZAn45k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c669eea570.mp4?token=fqRwsCoiAW4NWqCNvkA9BeMLJPze5flfmfHWpWuSZrzBM-oWT_zNgz-Lj0oFeTaSiY8QOUC-POSW0Xasod8DqAvWxVs-xskRbzOZgt0BwkSHRzy2_V-1tOuBreeJZr5cqa9QL_BiEckhL3O2dsDxDtCqjISFO6HUx_klgzO4ejd7VwYrC7Og8xYKHeiBgp4WPez8mwTFD0bhpuIfmqMm_gw_gxVcmfWvGpLUBhAwAfbVgaDg8NNbnpK5Ci37zIymOq2iO4nZojtnOgmBpJEkxx6xSD8S-ilIRO9OlIsjp-ITqzgj7le0iprGOtnX3roLakFR9IpfsGZZqKwI3C3AArUvAFAUU4LxCpW7izg1hnJ5skceJXDZCIS28pj95ThrUuusPDzv56kjx6-_BM7b9ye9JMy4B1Afl7Ad06xB9XYblM6H0YgRpynMNFrcvXVgUOwdN3KSXJqI_iYZWX4P6FLq56ySF1aQDounzlfxk5O7oF6pQvbC8eZnBRI1NaNzix7bVo0_tscq4JkhehcxPQG3vQktZYRsT9WEbX7UEFooZG2wF9o3SPb2Bg2TMFqQoUCiZdTm1qwwTK2lW7zULzgVvQx6zw-PzMgAys28DAO1s_1orDorN2aV9jDx5MVBnOaS830zLvtQoRr__xFSRb12Ky01Z3Y4J7jlGZAn45k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شوهی‌های‌بامزه هاشم‌بیگ‌زاده با حسین ماهینی دو مدافع‌چپ و راست سابق استقلال و پرسپولیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/25343" target="_blank">📅 11:26 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25342">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TNdGRzrQxVlAFtN7Pi-s6PL3Yw_3n2j86O292qvHRM_TiL9cUHwhT_vjCTsVZpkoOl10T0Gmc4lgQDZcI-_EDjsW5vmN4f_SFP7IjDNyOoPr0-GC_-ntdwFTog_lMntR7Aqp42mSrSqC9usHeuL23KeQK_N9EK9KdWNMmWK-IKUU0sgRRCNF5IEtwoucV5hM0mXAKpkAGleRtNVqpl5nMsYTcj77B2FhvL3Qb5m0Vl2fMdIPePUfhNDK27z72-0S7X3lG4QMTo6Ar55NHNSIXtZvq272FkXzWhwKjanO-0sjlH1XJ2cl02ioMkef2VCUMp_b8Kbk1LZqFk4VyePoOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های پرشیانا؛ باشگاه الشمال با ارسال ایمیلی به باشگاه پرسپولیس خواستار جذب اوستون اورونوف ستاره 25 ساله ملی پوش سرخپوشان شد. این تیم قطری اعلام کرده حاضر است تا 3.5 میلیون دلار برای‌جذب اورونوف به‌پرسپولیس پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/25342" target="_blank">📅 10:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25340">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CsScjKLAfd-7ox1BwgTAFB7p8Zd8UO-_L7C8BnKIjwFMvaCDjaAcPf5LYCNfYfuYG6_C_ArP3iLF9FxJnk2tSO8PN94pQ7oPCfh1ePVPb5SebJ-2lCMz1X7ylPQMK6NFHrwD8hDL-ENELpLtFBClyMdEpoLq4cSAgTHp_1EOOy5kFXDhac0do5bEPB0tANC4K1_7spZNX8yxtMDSc_jjIuO7lR5c2lMlLTMQMBwTeq72rU-hJ_aia2UwaBPbhXAEeEctQa8k2VC7dAmJp-KJ2GWqrbqpEbNV0dxsd9vxYD40veE0ILQLDEIbGdnjD9orVAfiBeGzMyPihNdEn0WWig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ مهدی تارتار سرمربی جدید پرسپولیس بعداز منصرف کردن پوریا شهرآبادی برای‌رفتن‌به استقلال؛ ساعتی قبل با دانیال ایری مدافع 22 ساله تیم نساجی تلفنی صحبت کرده و از او خواسته بافشار به‌مدیران نساجی کمک کنه تا رضایت نامه اش رو صادر کنند…</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/25340" target="_blank">📅 10:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25339">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cQ84qBwmX77R1LcVPFxsUyfnI3uXvIlEdxvXLUflEKtMS6OsC6vvcYZS7OhrT6_XTZtzB21_CoBiuUGora4TP-7GLvmeM8C3YWkWwsnSk4pYO0N7ZcyygXx0TMoppvDAzx1-Kqj6TqCfD2pOa1S8VmhtAlEWeORiWhX_zy_Cwmm8m2bMubbCWXIKlNF9rpCVToz74RgdIe015aqkw0HSDRGnXL1IkuGOm3R4az64tUwun8zoGl118OF96qtTvzgA-EsiQsAsEKzZ858Ul59MVYqMTAZKwE8CFgx2kiFuyn_GkVaxY9sjxyOXbd3CE6kscneazA-xcXvYnlNG4jSCKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
«وزینا»همبازی مسی میشود؟ براساس گزارش روزنامه مارکا، باشگاه اینترمیامی قصد دارد ووزینا دروازه‌ بان 40 ساله تیم ملی کیپ ورد را به خدمت بگیرد. او پس از پایان قراردادش با تیم چاوس در لیگ دسته دوم پرتغال بازیکن آزاد شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/25339" target="_blank">📅 10:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25338">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45277758ee.mp4?token=gvfahH4mCHFb9ZUKmfJo801F3CDMmptF8cwDWH_h-h5MrNs8E0sdbhuS_BOj3j8Sz0h9ZdyxPhtaDASj3XXkGA5y8W1a_yxLxttkjFVb-CRk1vunQ4E62wUhKfB17SpuIi_3tDT-QLYrAmxqw_OMMbfCneKeTtCwm37YVcHsTyEGZkmhnqWaInmZSiItkwbb6iB2Ev0MZABxz1j0WGKUQsFokMvaen8QoqOCm8x-6bGxtkqmQXqMbBk4ctR2vmPt0ArXT2sCeA3-V9WK1r2vCx5qEbNG--ak3Cyl1rWkVocdsSgmsZsqp3misCH2y_wnn0RvNgD6pn1-ItFrEHkceQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45277758ee.mp4?token=gvfahH4mCHFb9ZUKmfJo801F3CDMmptF8cwDWH_h-h5MrNs8E0sdbhuS_BOj3j8Sz0h9ZdyxPhtaDASj3XXkGA5y8W1a_yxLxttkjFVb-CRk1vunQ4E62wUhKfB17SpuIi_3tDT-QLYrAmxqw_OMMbfCneKeTtCwm37YVcHsTyEGZkmhnqWaInmZSiItkwbb6iB2Ev0MZABxz1j0WGKUQsFokMvaen8QoqOCm8x-6bGxtkqmQXqMbBk4ctR2vmPt0ArXT2sCeA3-V9WK1r2vCx5qEbNG--ak3Cyl1rWkVocdsSgmsZsqp3misCH2y_wnn0RvNgD6pn1-ItFrEHkceQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امیر قلعه نویی بعد از دیدار برابر مصر: خدا سر ناسازگاری با ما داره. شایدم خدا داره من رو می‌کنه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/25338" target="_blank">📅 10:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25337">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pEdXilpWtSSQ3saVbsamFzdS22FM_pjxkqsq12he-XPJvwiVlG2_vXcWcoFAjA1NzgEXHa97oo2npC3mSntJY5ew-R8lq3YL7q2BaF41vd37LFpp0KeTeUVN1lkzLoqvgEUn3oHNi22DcHMiU4LSANy4JRvIhY6A0IejgWh5E4KnDa38UznogVvfGxJKJ0uf74Jv2cm2Qxkq34KsDrU2lfIlU2gdHMb6WhWgmFgpBr7wEa-xiFWsAl1hcWxAz4uSPqQUtKP1DDIy7e2KKv8hGdY4lvambACuup5yMeEXpOMLh5NYTTFBS4MIARSfhdJOlK8CZaoSrvjdX9jjNTvHpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی
⚽️
⚽️
اسپانیا
🇪🇸
✖️
🇧🇪
بلژیک
⏰
امشب ساعت 22:30
🚨
ورزشگاه سو فای
💰
در صورت پیش بینی اشتباه مسابقات جام جهانی ،
5️⃣
میلیون ریال فری بت دریافت کنید
🔥
🎲
با وینرو همیشه راهی برای برد پیدا میکنی
🔊
🎲
سایت وینرو
با بیش از 400 گزینه متنوع برای پیش‌بینی
📊
ضرایب ویژه و رقابتی
🎲
ثبت نام آسان و سریع کلیک  کنید
🎲
✅
🛍
پیش‌بینی به ضرایب بالا
✅
🤩
🤩
🤩
🤩
بونوس اولین واریز
✅
🤩
🤩
🤩
بونوس واریز کریپتو
✅
تا
🤩
🤩
🤩
🤩
بونوس روی برگه‌های ترکیبی
🎰
پخش زنده‌ی تمام مسابقات
کلیک کنید
💰
درگاه اختصاصی برای کاربران
🔊
اپلیکیشن حرفه ای
📱
🔊
همین الان وارد شو و فرصت را از دست نده!
📩
Winro.io
معتبرترین سایت ایران
🎲
🎲
🎲
🎲
🎲
📱
کانال اخبار و هدایــا
🌟
sr19
📩
@winro_io</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/25337" target="_blank">📅 10:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25336">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y_ya46_JdJ6ayzPSoFPO5rhjVwdsQIbW7atpx-hoe4M02WS9lAk47d-4g10CtCWsMyyKkT4oMH3j2uWBw5F9NpGICP9K_2pDss2pFkoYxqfuDNpTTdUIAuVbPYnInLOu4wCqxit8mXGrDLPw4jKT8o-z1BKcNetoa0LLgsZsQU0ZcWhlCFOcLxtPBLUwgZEGxeQC1ZD5IQn8hGSJS8Jt85DuKsyamen9SPsbxG-mwvnSjRXBIU-E1m7lQEhgVAnzMooi13ry8vEV5GV-Yn-3kjmc7UzLy_i9zFFrs5k2EE0VxX5zRgE_LuwzbG4KagWM_G8YxhTCokVZhtwaay1osQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ دوستان میگن امکان داره مشکل سربازی مهدی ترابی برطرف شود؟ باتوجه به عقاید او و همسویی‌اش‌بااین‌نظام بله یه تبصره‌ای همچون تمدید معافیت تحصیلی پیدا میشه و خدمت سربازی او تا یه مدتی به تعویق خواهد افتاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/25336" target="_blank">📅 10:10 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25335">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AjHsE8MRoYZpysf6D_wrv0pmjlLVqE1LzvhcR1dK-RJCBmU83FXVUDPGlL-P-2XjfDCQ8hiphZyyWkTzGzfd5m38uZAu_Rt-LCZ1PvS33sIkVGSw_Qlb5PcpLbTHCglljiSnfKBtIgEjC3bk-oS8XPrOy8-Ad2_vu0UqSWXSfkugbr-_8TTP_ncLxdh-7y2dwNvCuzlTH6mrZG1kJJeOU6qEbgxu6pzNvQNglpnewE6tilSHM5reDWH0R7yOkNz2ZS2fUMGZS8d7U8lxzG4ozasaohHURJAAza1eWoQpfl9qjrXYy0mYEYdovH__BamjEqjmIeX90dxn1JuSrHF_MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
👤
ابوالفضل بابایی و سروش رفیعی دو بازیکن دیگری هستند که بااعلام‌رسمی مدیربرنامه‌هاشون در ترانسفر مارکت از جمع سرخپوشان جدا شده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/25335" target="_blank">📅 10:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25334">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EY8KdJ0FSTSuawUihfVbioeS13PmuQE9neiyOfSaOdZzh7Wp8eVLb7NLss8Q_PoLRnt9zFMfNwNrouWRacq5xsjjr7xXOyue2PWqsu0Q9RNcS9paL9VTAKGgIOv3UwuSUi_DV-VA6AUPiCOG6_xG99tK31QfZ1zNIr8kJt7-uFfgukumoMaE6Q8zXqkgZIWRnqS_lP0gp_2AZ1bM7hM7VTrJ7ID0Ue1744Ysm6Bn3c-RdqNW6vWJ9s-g_j1mzNfuIpZXmG5GwArYkg6HffD2bHZowgoYfUQ3kKTG6At3qGRm-Liy1oobw8Ls7EaKOtSBuMmQhwb4P1VBMLUpW_CQPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد..بااعلام‌مدیربرنامه‌های مرتضی پورعلی گنجی، امیدعالیشاه و میلادسرلک در ترانسفرمارکت؛ این 3 بازیکن رسما از باشگاه پرسپولیس جدا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/25334" target="_blank">📅 08:23 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25333">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ekICyXWbcNqFGcoo2diI0U1cCR2ZTcsAwFuEsKr9YzIZvaaFEpBRUJL8iISzn2v1Usxitqm-94VAimWjHgaxVnzxhvS31Q0PJJ8iPkljhC5ZqNo6-hPpxbcRpnf7cJOH08Tgj9ZQ0FE5gj9qp61DQ-qR7ZxE4fOoDtfVP5eckcVcJWDn902KYh126po9c6mqazIWprWkZOYwxgdwuC-L9ZabqVEpvEnbvo5jfkx0gTo0AqfqDx-nN5sWgu_90X_ZqgWhqDLkgo2vox-mC41BlqUznYlN8GXIvIW5UCJyhHAaI4Kw5D_JmZrsuOLbJ63rE3OC3orwfE_KRZ5J0ewXow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
امید ابراهیمی هافبک 39 ساله سابق استقلال با عقد قراردادی یک ساله به تیم لوسیل قطر پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/25333" target="_blank">📅 08:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25331">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T0K-SWRQ3FBgfpjNUzSoEMiC1kmXop6KJ91FZzeb-cWa0HuA98GhfGL-_BIgr2x1XEjT5MLAsOdoTAMFKsqFUc3Mo4zEsXQ5cI-0iHJ8AuPMc5c0l_wzcKKktNFhNu_QhX2QhsYmJ8ytlAQ-BidGVXBXmE3Ci89ZxtqlzO8zal4-2FiEYbP_XgkS0hPW7i4FWuJaJeq3nINYjmHEhmjzDcQ9ZGvX_9iTetyYVo9wgYt1msH7u55n09PkTd4MhVa3oIn6ncRuvgAsLIWkYa5VO9zWjFOIl7mMupUZCnk3vYkdPKmg8kIUjXWZkdBetsrUhMNZB5tTmTIYTln3dyqIxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aQT-2r8dslh33peLPt4TwVquap-9Xs4NJ0VOq0BkS0BOlttKfwdl0poQBUPsPVuitjiAJ1-jRxb3wQnAIKSlqT_luVloak__uh6IsslFUddkOxrxIouw2_a8DIRQXytenKMBxAMwFSl2_kdHo1JUexGebBDmf34auxP4ISxi9t9EZYAEf9nU0ibqRdmYsoyTLALqK3OqFBY8HB7o3BWKKufNwQlc-2xf1nfoGI6BhPq2xg4SLJ8FI-GwupRySvarJ1dB64W891V8QptTV3s_weH7Rkw493Ey4EzFizQT2BoG56dJaQpi73UnALxDZg5umt9uWiAACh3rYjz1p008zg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🗓
#تقویم؛ 10 سال پیش درچنین شبی؛ تیم ملی پرتغال با کاپیتانی کریس رونالدو به اولین قهرمانی خود در رقابت‌های یورو 2016 شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/25331" target="_blank">📅 02:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25329">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ilI93RFLuURoToZnJ0884Is8QXSdn4ATsNoDfaRZzPR8QQZVBYqCcF06SuN1YJPTZ1i6x_6P8EqgCra3T9veCZiSKP1qWfKwRtRWwmjHtzHA9w_KCoSfIH863cbSWm_6OoUkAEY49eEvHNMPQhvFsgrp2y_gMTSXnC4nBbrmLb_K8XNCFODAmNyuVm_xUpJRMvWcXdHWfXXVEr6-9B6nEbLaxTiECsIl3uTgSxaz8PsUE0P3QDEEZAXaWguZCeijt4KGL8QQku6CPvPWpglHvv3hFUk6u2Ne6b7WmNOSG2Xm0mUHHO892WHv5NNosSpUbv4Jpkt2rkJRi_QCeQqI-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f0ejo86gQzXZE5bwLuENa71MEtX4GL_rIGewV2xBmROLmQh7pBiGzeoQhV39aH58Qp2xaCU-9z1guCquGiamjOUGvkgsZjfZy-KKW8Zxaeq2W_IRS9ILgKYSrjhk4R5B7jZpHIHR8I4TkwkGzPcMcWJ_VN1fIsgrONwa-C5iFskBA8wCERD-JEc1a9LquyuAOJqogJh6OJkAF0cstQWpv_18eEMqzqckCwD1uafCFm99KxncCatMEDRwBJzcaPzHBJduThGcruolB7XoyqK0SpN3Hk2FZtc0AdlttAqNiMou8oj22_oHxYSigg1nfJDDve3c7im22LSruGeLZcOpUQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
🇵🇹
ویدیویی‌زیباوالبته تلخ در وصف کریستیانو رونالدو کاپیتان پرتغال بعد از حذف از جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/25329" target="_blank">📅 02:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25328">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d4hkucHWRJrGx3bxwF-pC8npo7pP8xklfHAZqIvlkJayJpVWIIQNFmZXpk6Ektw3SLl3pnepsICqCErrBXcCE1Ln2kjMZTsodLACL84qVanPF_SqsBuas8C6BvJUtERuLrQL2rSI4PsaRUUfwk4nE9auRl8IipS7lCrGsboec-chTvPT9U1fHbG-wCs8Jd4C4XT-sp7gOVlKqUwtAGDz1bPSvXaWfNZFnlKBQ5S6q41_FsfRK3wNX5pkt-B_p2VL7x1VbqXws0gXLzYGd2VCjfxIYF6pgOoKbuDSwCjsJCPgFBAmy-4_kqU0Est9BuxelI65VQrGgeVBz4bndT9KiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فیروز خان کریمی برای کارشناسی مسابقه امشب مراکش - فرانسه رفته شبکه ماهواره‌ای جم اسپورت؛ خنده‌هاش رو ببینید دهن سرویس چه ذوقی کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/25328" target="_blank">📅 02:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25327">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lWLezMyytgoVThdEoRikhUWQrHzdCeImVMDgTsO2PA7D3Z-e9ozpdbaBhh6FCGfL_BxQ47EKk40DNtKgRqBEZrPaJ3N6CL6zl1Htu-Fn-tg3sTqgNqktcgl33BSfC04CvAysb7nLhsrIjurm9s0vVlRu7lRIJWzd356TnkvxqwYgt8tOHuH7m70-GUFH4htfZYZV7BQSTjD-2NVrSFtqpyyDcA51amhae5f2FApSaPV6NO4cOp_1ZNIBkkrnjPEiFD5cE34X70tpQNLYWDgoTSOYpx3TXARWf0pdlQgtcwtDIjOCYofzJC-PQyMuRRJI_zk6nSqrGPpL89ZhRL03SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ سهراب‌بختیاری‌زاده سرمربی جدید استقلال از پژمان منتطری کاپیتان‌سابق آبی‌ها و مربی الشحانیه‌قطر خواسته که به کادرفنی‌اش اضافه شود. درصورتیکه پژمان منتظری به باشگاه استقلال برگرده وریا غفوری قطعا از کادرفنی آبی‌ها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/25327" target="_blank">📅 02:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25326">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aROhzyBplmfJOKMVjZMRSfl_lsozUywVQiA8Ft-AjQWXZN1aHHcW-mEeb15aL8FnsasAG4pkfmiNs2974yz78c8QkiueI1vwGdggvl6u_zYr_s1cZCweYt-Ln5SYDJOcwtOFpcdqkuvBAfaD6qFK7oCocuLjuOCh75LPpJnWD28BxmDogYoikpdMFoJcVkhxEMGpH4Is3bvys8cFMx9C73nx2ZgZ3P3_kyJw1UbFvCXzSOkGwlQICDXmj4sx7ERRfPfrSNQ0rsAb4-li_akbJZ7uGcnI7kgiBFmEgj8C__-Bkvz-86MF4E9fzRVBjUGePZm3Cbo4hqVo5LaS09-xxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همان طور که دو ماه پیش نیز خبر دادیم؛ امید عالیشاه، مرتضی‌پورعلی‌گنجی، میلاد سرلک و سروش رفیعی درلیست مازاد مهدی تارتار قرار گرفته اند و به شکل قطعی از جمع سرخپوشان جدا خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/25326" target="_blank">📅 02:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25324">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OIUWxwoNJa8y4r6z9MAPF7aF8IKkR_37Ua_ZcPs5g2zl4JX5rx8_y6VESce5q3EPsU9XfxjvupT9-qJIKTiN3Fk81Ln3jIqGObSiU--YCFkmQt8X3GT8ao82F5xkcyXRsPk1pjzH51xDiGFBMnpKxibWn8mM7B0dNb3nhBpktbPR-_PQlc7X3PS_ggRgxAgfpTjJ6yL4y_518DRQQHvdPnOYZ_fPY8N13ztCjGVC8jU4dQEznuVdyG4OTfxqkmC--B4gKvIvwEvlEFy5WaifXFTfmHkgbBJNcz8hDj8l20X57s6c2VMXrZ_HJkBzxCtyb1CkuY-aZkLX8OuUskT-Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ieUVRmX3L9Dfv0mlUuRJ9LrgLgveZVc4DGkvOwM4xAtfyNq9UJDFbAAa2nv9c9biYIbsLhyaskmQQgiT-crLmbKY2T5sfTl_oAIbWnQwFuZm61qPeplI1UwH-U2UwYKyp5Nz5p2ubHjnS_Nq-c4xhKLh0daQE82ywil3qPo8NTteHaothEV_2-1WaFjlZgqJA9fl4G9Zh7z_2JJhLxcXvRLdwHqZV8QoqXKlLXXPjnl1uBel4QOC2FtSF1iFIxzqyhv-cQVZydpDyb-3wlB8FSnHANA8UQZoAkS5-OAua4qcAPYpCQQybOpLEJ4W8eUPS1x9-IhFI1wmWjPJiXQ-Rw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک‌چهارم‌ نهایی رقابت‌های جام‌جهانی 2026؛ برد شیرین و ارزشمند خروس‌ها مقابل یاران اشرف حکیمی و صعود شیرین به مرحله نهایی رقابت‌ها. اسپانیا
🆚
بلژیک حریف خروس‌ها در نیمه‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/25324" target="_blank">📅 01:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25323">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cPrQGkwJoghmnppGz73IBtsLsEYYYz4u0_BAM60AJd-gJcZlvmetHnrKj2F5ibf4CCs2y9WaCgeItSDvlzoX5ttGWGY1bdHmn8sNd4Ysb56xi1uf376rY3J0J4r5XvTcq0LTPcgFVsabjirh8Msd3KFnSah1Ey2ig-YU0BsO1UuhuzvsDGqIVRRzF4VvvdJvyBICBPgbQqxkWgGfcseJIBcq2XN2rOaEFcvWM57Kul_GH0qhgjFv55zwHgg5t29xr0xivajQFDC2AuRJDYAk_eMtDCmgW4c6JSW9BFahdtUVWo-9tn2prmHb_ducr_11P-Nvz5OOkF-LDamkgtS_pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌امروز؛
جدال‌اسپانیایی‌ها با یاران دی‌بروینه برای رسیدن به فرانسه در نیمه‌نهایی جام‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/25323" target="_blank">📅 01:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25322">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RwECH4KUsUlMItlJxkL5ab1aYPWpdRgVwtJMJWcvxapS1MnM4k67wd0yPRzjC9KKOPwUjLSVtjdVgDoBrT2TI7L6QGlML9n6NsAvZIRqC8B5ZBYcXJJCOnnK04e0x0A5veIh0y4fZ_GcyOHKwbtjbGPUxezDxRkvPuHVG1U0FoB7azkmxbQub3PT2_q41nFDSDPOCjy-Iricp0DqQSZRG5VUTq1o9wOLs6ZiCrJdcE5Ev9CtgNTZdTBDOVs9GtveWVWFpKE4ktZcubxgu5fmO9d0SSoZtpX5pS0fCzDmbNdepGCGKSUP5AGd2c6Waf_9DK2pi6dPMZ7ttv6c0NruQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدار های‌ دیروز؛
برتری شاگردان دشان مقابل مراکش با درخشش همیشگی کیلیان امباپه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/25322" target="_blank">📅 01:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25321">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dXeo5Us5VAMaorcYNjGdhx5NmPPod5uos1cEdGSJU14mujlyOd3xduqZ8OpuU3jKKmN8cl8_4zshmeX3j5qCBNi3ReQomuAC9XxNMzmypk96LYu5NUuuvxupQHb9vrSDw8zFcU5E5sy4EJYYuqTd3XlsGnXJNsB68Hb5Zd9Pe685nQHt_gUFRg9RG1zbDVpypoc_XgEY_6gRYHQUZ2LY4U_WBiCuJ2nzpFVcJpuX40zqo02kse-k0JQkjgLI4QfGjl5mGkQGxRGBZOz3dnb5zWfPV_MVXScAQeBSSr2-XJHGL9vE0Q6iyDhnX2wRj896Ja-X2e_e3Ki8IiGWs1yngw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
#تکمیلی؛ مدیریت باشگاه پرسپولیس بعد از عقد قرارداد با ابوالفضل جلالی و پوریا شهر آبادی از آن‌ها خواسته هیچ مصاحب‌ای مبنی بر عقد قرارداد قطعی باسرخپوشان دررسانه‌ها نداشته باشند تا زمان انتشار پوسترشون‌توسط باشگاه؛ بخش رسانه ای هم پوستر رو اماده کرده و بزودی…</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/25321" target="_blank">📅 01:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25320">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JBpxjyUfyj4m-a2yyjApRT0RRucd365eN3OWIZYijFG_GTDookNYfwAojOqz3w9drffbjQTwS6efRm694YdLk_x3Odxcxp57mMLyoiSuHjlF_MHp5D7z-HJ8H9JonPrE42QjmadVxpSvvOp1Wrz3_Jyw2Gez9IWV6UMOTsWOo63XKsw_DEV9rXO1I_-NO7f8L6Iw_MKYCv1_L2SZ1hUNAinFaSMqdZqTRE7z-3KiJCWWSHybuJ0riRP9ANr5aXh1xPtoISNy8Jfz6KagtEqxhaCQ0ZmskUJjju_3SbUyqy7hY_JvY3w8IdODcwVxFuCGRgK3Lug8mznN71sONJHUrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇫🇷
دیکتاتور جبران کرد؛ سوپرگل دیدنی کیلیان امباپه دربازی‌امشب‌دوتیم‌فرانسه
🆚
مراکش؛ این 20 امین گل امباپه در تاریخ رقابت های جام جهانی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/25320" target="_blank">📅 01:34 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25319">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OhjM4cu61bikvJpnzDFByalaSULkoQp5Ny7CikJG2g4QuA4rPUZuzq8QRYZKt7fpzdh5jNxTUcBxqiprjS6LCl7scwKF6jmENqDjIABSLTKWFxp2tF2k7IbhY869QMv82jrD3hpvAaTXicEUKrhWf7s80bAPHXUBAbm2W5D4KMthzBsQttSKTmSndi2xmd65py0u3rlo9uDr1WPNthgXsAhB9VAm5StYxnUykur91KCyFSk5iSnZ5UiJbZutrRSBEOsYt8AeDgvbEhMaQBX_iThDpwUtZWEuO_epCTKODI6ydlB55s3n_BeRnLueIo9NE5zQhUoZXC6D02efqdn7-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ طبق صحبت‌های امروز وکیل ایتالیایی استقلال؛ تا روز 25 تیرماه پنجره‌باز خواهد شد. کانال پرشیانا موظفه اخباری‌که از باشگاه ها دریافت میکنه روپوشش‌بده. بسته یا باز شدن پنجره دست ما نیست بخدا قسم که از ما گلگی میکنید‌ خبر موثقی که به ما میرسه در کانال…</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/25319" target="_blank">📅 01:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25318">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2548666d77.mp4?token=HHZmx2qQ6P7IWhVYc0R--uJTS0BcvI9NtTW2qJTvC4oHtihEF6LxQ7vYYPhGvH0NrKCrDx3EJHNZB1fwTrrZWg4JmAuqUUHM7ZYmM-qT4TLu2hBtFAKg_Rye8NyDEzgoRu3NY_xuTdOx1BV0JLee6nZCXMB5Dsoau_lTwESjRO2a6XHC4hCCxscwW2CavIC7aRqH8YE6bk0CbsENw2HCGR6spEiZsAPJMiVZblhH93cBShbbsBXtAUO0L45Tn_XW3LGjmTAZCpE2sATfP_JzYIKAIt7y2n7cipgF4eBHY1JFy-vms4zPw-gatO_qySDYwlDTBKdIcKNKDa_yLae34Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2548666d77.mp4?token=HHZmx2qQ6P7IWhVYc0R--uJTS0BcvI9NtTW2qJTvC4oHtihEF6LxQ7vYYPhGvH0NrKCrDx3EJHNZB1fwTrrZWg4JmAuqUUHM7ZYmM-qT4TLu2hBtFAKg_Rye8NyDEzgoRu3NY_xuTdOx1BV0JLee6nZCXMB5Dsoau_lTwESjRO2a6XHC4hCCxscwW2CavIC7aRqH8YE6bk0CbsENw2HCGR6spEiZsAPJMiVZblhH93cBShbbsBXtAUO0L45Tn_XW3LGjmTAZCpE2sATfP_JzYIKAIt7y2n7cipgF4eBHY1JFy-vms4zPw-gatO_qySDYwlDTBKdIcKNKDa_yLae34Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
شما حتی خارج از زمین‌بازی‌هم لایق احترام هستی آقای کریس رونالدو؛ شخصیت بینظیر و قلب بزرگی که داری رو هرگز فراموش نخواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/25318" target="_blank">📅 01:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25316">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f822cfdb19.mp4?token=sAqwSgejvXdBvdUg9ara1W57uSfY8GSXLBpARAJ3NP6T84-McSbYYQDWo0R2o7BRs4n3xCRiMZ_IJY1zwXTgpO7szGU2-V69BCtcawkWO04fX2sFf9-u51DnQifsYNvc0Ji8lYDf_itNiNUiVCxDokGMq6m-x1pEMny3AxX4jQ5Oa7Nn4HuPhcUbHR_Z2mOgLIpw7mejZW_hZrw8G3kILX0IwvHcARc4mGg0RZoZVaLY5amExrv3AdFwO9eoSx5jR9_4EYvzmhOr-T2J-PeAXhane-GS70uvSJGY2CDnjQqqfHwgJXfpmAcwzzkiaNTmB7HnteV7W1TPhBzOvjv81g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f822cfdb19.mp4?token=sAqwSgejvXdBvdUg9ara1W57uSfY8GSXLBpARAJ3NP6T84-McSbYYQDWo0R2o7BRs4n3xCRiMZ_IJY1zwXTgpO7szGU2-V69BCtcawkWO04fX2sFf9-u51DnQifsYNvc0Ji8lYDf_itNiNUiVCxDokGMq6m-x1pEMny3AxX4jQ5Oa7Nn4HuPhcUbHR_Z2mOgLIpw7mejZW_hZrw8G3kILX0IwvHcARc4mGg0RZoZVaLY5amExrv3AdFwO9eoSx5jR9_4EYvzmhOr-T2J-PeAXhane-GS70uvSJGY2CDnjQqqfHwgJXfpmAcwzzkiaNTmB7HnteV7W1TPhBzOvjv81g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🇫🇷
دیکتاتور جبران کرد؛ سوپرگل دیدنی کیلیان امباپه دربازی‌امشب‌دوتیم‌فرانسه
🆚
مراکش؛ این 20 امین گل امباپه در تاریخ رقابت های جام جهانی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/25316" target="_blank">📅 01:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25315">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43c42773d2.mp4?token=t8O9nEpLSKTDwkoSIhbWnim-ZQ1jZGJvB5VUcB6WpQ_wkrYphdRb_yt63-EpVIdJBsWP4J1NCv4TvFTxPLTrruBvZ_Tv3TXLeQuhIfID9Zx7LCjwOXqTanViiUQvvO7C6f1y0QO_HDC2Ea0BbB1bW_wxaxZc-aDAjklF_i_Y3UukLz2XLZcNly_6fl33y6ZjnYGS--dyvd54CB-gcS9skjtfaaMRxuZq7gg4Z7K-PQsTbwWf9kSw336Ci_BBXhmUG4kjw9ugit9c32QbvUUFJySYpPYDcS2AvFZz84UTjYbNMv6gh-LSMfWtAXwBJNb_5W8C0TOnlDbSmchmZ2pgWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43c42773d2.mp4?token=t8O9nEpLSKTDwkoSIhbWnim-ZQ1jZGJvB5VUcB6WpQ_wkrYphdRb_yt63-EpVIdJBsWP4J1NCv4TvFTxPLTrruBvZ_Tv3TXLeQuhIfID9Zx7LCjwOXqTanViiUQvvO7C6f1y0QO_HDC2Ea0BbB1bW_wxaxZc-aDAjklF_i_Y3UukLz2XLZcNly_6fl33y6ZjnYGS--dyvd54CB-gcS9skjtfaaMRxuZq7gg4Z7K-PQsTbwWf9kSw336Ci_BBXhmUG4kjw9ugit9c32QbvUUFJySYpPYDcS2AvFZz84UTjYbNMv6gh-LSMfWtAXwBJNb_5W8C0TOnlDbSmchmZ2pgWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🇲🇦
🇫🇷
پنالتی‌از دست‌رفته کیلیان امباپه در بازی امشب مقابل‌مراکش؛ یاسین‌بونو بازهم پنالتی گرفت. ازهشت‌پنالتی‌اخیر که براش زده شده در جام جهانی تنها دوتاش گل شده. شش تاش رو به راحتی گرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/25315" target="_blank">📅 00:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25314">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6hHEn-0CgQlNFcP8vtzSkyzkOqi-CHe8ZUDb0T_J830JWsdxS7SZvX-vOSFmL6vRwzt3IqOzJBV-ju9pdr_fd3yoD_pzIAtiArBTWo71aAbm36z5pTAOwBkhz68pEJ-hK7umpnpI8c2Qj80RF7VLh8lvY2qDrsyTmGavs5BVRWif-0YphzvyphPHNXtOVPWVgbVOCDV2qoLcLXAa48Hn5-Bzp3FrSnpBoidASuRRoe4KEvkpb8K3-m4oof7pvyhUsc1L8CqO6BPm1YyN9QTVt4d4_X56fJYmVPRHP7LZCK0MOBgaZPI2qvIF7hucsEX7fDgGeKMVLs5eyzL5U6TpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇲🇦
🇫🇷
پنالتی‌از دست‌رفته کیلیان امباپه در بازی امشب مقابل‌مراکش؛ یاسین‌بونو بازهم پنالتی گرفت. ازهشت‌پنالتی‌اخیر که براش زده شده در جام جهانی تنها دوتاش گل شده. شش تاش رو به راحتی گرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/25314" target="_blank">📅 00:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25312">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PwsQQdTyPzE-PN1-cnwCJjcFSIl1nBSZkfL2cJ1y82E2IYXH6e6Yma1C7M8C6H4KvNvw-AEhNCOvzjlR6ZSAP3gGGz_4ALA251vUegacMmkuWHjcjCi1MwtRvEBqSevhEwBkSVjiPMWDIXKe-6qT2V8ICU9VJcmJYroBE1rybe-nM1o9-mTIo3_LKVCLC7UBs6hccs9ZXm4EehskpAJVk8AP9T2mUr_166gtKJ-zoxI046UYmdWK1fS-cyujG1voGCDofaeievvLlvOJBpTivnngULGrhhgARIbrl_zciygnvXazCWhkN-HCYlbp69ZcCHiRBbecp1NAR7HlkrKyPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فیروز خان کریمی برای کارشناسی مسابقه امشب مراکش - فرانسه رفته شبکه ماهواره‌ای جم اسپورت؛ خنده‌هاش رو ببینید دهن سرویس چه ذوقی کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/25312" target="_blank">📅 00:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25311">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7769fa4e86.mp4?token=WakwM7_udoT5NkoGTweTia1z-VqYdXn6A0DBA2TT_CETwqVJK0vdzYvugoWuPzQmrM6HaGE04CS6I1xuzKnhbPcKpAkLV6hfpv_LsigeiD1YMk1lgA-h-iQpegyNZCxzKEJcSlxEcj4q05xPLpdRSPC2QBJKmujl69_TkWmYLeRPuYANMfEs4AzhtQpHOkx4gsKSjOZWWllHEqxFlkRnbxAi35eGaztH-H6bsC7268UF8CAlpLrMa3xIgQ6U66c57ilk_dH8Oe0WhvTccgCRAc5nFSpkmNGAYefd4D1eLeu5Gy8hnNC3Nw6z-I2qYzhM9uib07XCcQ7UupXgGcjexg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7769fa4e86.mp4?token=WakwM7_udoT5NkoGTweTia1z-VqYdXn6A0DBA2TT_CETwqVJK0vdzYvugoWuPzQmrM6HaGE04CS6I1xuzKnhbPcKpAkLV6hfpv_LsigeiD1YMk1lgA-h-iQpegyNZCxzKEJcSlxEcj4q05xPLpdRSPC2QBJKmujl69_TkWmYLeRPuYANMfEs4AzhtQpHOkx4gsKSjOZWWllHEqxFlkRnbxAi35eGaztH-H6bsC7268UF8CAlpLrMa3xIgQ6U66c57ilk_dH8Oe0WhvTccgCRAc5nFSpkmNGAYefd4D1eLeu5Gy8hnNC3Nw6z-I2qYzhM9uib07XCcQ7UupXgGcjexg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک‌هشتم نهایی‌جام‌جهانی 2026؛ شماتیک ترکیب دو تیم فرانسه - مراکش؛ ساعت 23:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/25311" target="_blank">📅 00:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25310">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kfMqrzUlUnOWUyCuwLXjrt5mGX3Lmgr_M2WpdKKA2AwVtRLlpr_ljRhd9SH05TWSb22jfxtQeyPVcDHr9vska6uoqi-st5t139oa5Y_8-wUXrHsmMyAvX8llsrDK2LOhwG_D0UixmJIGsqT8DMfpLmEMm6kKrHY9S27OBlWJGRw76MvYVi_-zQqJkuWzEsxfhdU4-kk_cfGM-szcPC2VVZDhQeCV4MzJH7R0UM9gjg-C3-DaE1q_zI5-SSVNC2nInyEhrEVbyNElpaw-jeV0OT4RxF9d02NlO8_IWSQKGDFbGzI0EDT77UQLOfCBSHuYVD4zVapg_4_vQdt4qee4TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین‌گلزنان‌تاریخ‌مقدماتی جام جهانی در آسیا. علی دایی با 35 گل زده در صدر و سردار آزمون با 29 گل و کریم باقری با 28 گل در رتبه دوم و سوم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25310" target="_blank">📅 23:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25309">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mgi_taLkpriUMqDDYf3zuVOBDWngWb1DZEjZoP0w3NV7Dn-_1tx3_VPLnrAmw_gqkA3cg0-J0nYV0ReZdAiTlRZWY-yxX4lotaZU5v5mNjtoE_vt6yDseSIfNcW47VX1xmTKvw0UxI4b9gbLywWW8KzYHZhZ2ICUoVR1kvFlG8zpYWisEY1029YclCKqFwY_0g-eoYDHb3lctFLdeok1p3cad3btV6So_WxZp0lDKW_bdkKSi1QkNKyRqLW3glniOdj6820GfXrvRVAEXfV1eA-DGiMbjyA852SSNVXgNQMh5HHq4IBgFQyNonlCTWF5Fl1ykQ-Q3x8BPqu7QGquRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌ترانسفر مارکت؛ باشگاه پرسپولیس برای جذب پوریاشهرآبادی20ساله؛ سهیل صحرایی مدافع راست جوان‌خود + 500هزار دلار حدود 90 میلیارد تومان به باشگاه گل‌گهر سیرجان داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/25309" target="_blank">📅 23:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25308">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DfvRYUapIK-EtOwNKxl7PR31Te-cn_XWjtOiRx3UsCenW4Qp8U4iYPA8goUTvhHam_GhuQcundGMrgntkREWpHoMMUyV3MnoRv2jFpKS5_AitZf2-L0p-xaAMWPIhcCFRU5NpbK-0EfADQCu5tJvufEacXzJD4g0eujhLLQ6SOG-_kogJNRPCIUHBQx71QD8Yl8ghDj5UZ0fTQPPHQlHnBhkb5pt8CW1bLGY1IvkU1e8yxyOPRZqeane3t5TcV85uXS5zQzIhVxk0ZAHSR3WsU3_cjGxekbEDEXuBdKD9zW_oWwtb3A4VZLWBWOtvKWJwWrbBQxBi9gOCOhTA68RQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
این‌بخش صحبت های فیروز کریمی هم عالیه؛ میگن الهویی دستیار امیر قلعه‌نویی گفته ما هفت تا پلن داشتیم برای جام جهانی؟ مگه فیلم هندیه اخه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/25308" target="_blank">📅 23:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25307">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LM2XjAEWdWSYvxKwmVcv12VFzJ2FMsTJX2EbQbpsgJxD6J_-KeL_Lb7ffAxCpkLKyydjkm31XJpf4K4GswVyqpsOpfbIGz-34JAqXnAcqxLuJpd-FkrteFkw2Y1RlcspBviVl73GeIT5tnnLg9XzQAqMVA_mfMMvaZv4_-Mmpqn7hYVLoY0EzEDhmZ4ej-eBm4f41hRogXyz-oFQ8cl1HSO_Oh6xGoxYPEnokwDHegvFW5L7K1BC2CjbRABsCxHLE0gO1h5kKNp10jGHqtdmy_REtM2a5brPhazoqQQVfzRZICyAFpmTbAtA-SgRPKgHGvI3BywXwDd6DlTKq0EYjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی دو روز پیش پرشیانا
🔴
پوریا شهرآبادی مهاجم جوان گل‌گهر با عقد قرار دادی چهار ساله رسما به‌باشگاه پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/25307" target="_blank">📅 22:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25306">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YaET22aaTYqOPNWUW3cWRnacsjgvLZJqfvNyZH4l3t0rpk-6-zi3S-tN92MQ4pM_z-EjnJeAGLfAoDBpaK4q4gKZmDegqr4tCHkOZm0qetzR41ami4w2O8Md0Yt1ya2MyMVqJHiUcr7JVZMeJmLHeA_K7r4_-DSZuwEHpU4_wAHFeERHBhEwVXyxLowimOBMNnqscxZ1MeYfU9foE5EnuzQwOlCFZWAli1NqNXLPoHc0kOQG0O0Th0EO1YApM1tj4ruukvh_HmXYy3J63aWwaFjV09YIF_Mnm9odNEen_1FhoP_R5OFv0cQ4SHojd_y3Vs14BeB_BzR7o0zLVafv9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی‌پرشیانا؛ جلسه مدیر عامل پرسپولیس با مهدی ترابی در منزل این بازیکن برگزار شد و دقایقی‌قبل به اتمام رسید. مهدی ترابی برای عقد قرار داد 2+1 ساله با باشگاه پرسپولیس به توافق کامل رسید و به پیمان حدادی اعلام کرده درصورتیکه تا هفته آینده مشکل…</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/25306" target="_blank">📅 22:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25304">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eiE8AXZWWEhPMWYUOd1yeQ3RAgQFPuIym1hz-B70L9dc94mPojNYPikOUVy9MBbe86Kgk4VeEZoymDAqCW4IUuT0gEHgS_HkwQpmF47zd0oUVpSIZE6cEj3uoHbQ0Enp6XPlTFOongzNqSde9HH-3igY8pohuxMAINDQkhG9_U5x9af0Y5_CY2N-fZsrqxrZ94sEclvnI4U1V2t_MESZk8mWFbXeuDkFKJaLqvHeKpBuJ9nAODVpteO6Cr7xI6Hi_TAtrlNs-_s4RVewBbrG4pkuOJlFhGd-65n3VZTJZagBgoEOuR1tvJ361gAurtUeAhtb91QqOgCdMjIapBW8lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R4SlqnyZkxRz6yluss5l7HFlMsfJ_k_gV4Dd2r9uOBwU4fwJmDqpIedPllW-vKOZu1-wtsiyYx-UX7yXwgJxAJndebdVxnQkdcT5Xs4bsod373tpf1DEN7uS2dNPSuJMWYNG3hs9SWJTczrw4Z9R1Oqhv5htU10jcLWhNuEP9mrm7x8qSPY37Q--eNyW-yZ-Psikv-VOdTz0hQQi9Qes9oX_8YrSzQVx-dkmYKILQXJc6fNAVKBcshwgjpUU6EQCZAPXEu_C4Iv4YZoMA0ByOfnlNa-OK5jcucVOt97RzKhqSbkvu4axRf59T_FHsgVHP8NbIT_OFglbphNudui6ow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
#تکمیلی؛ازترکیب دوتیم‌فرانسه-مراکش در جام جهانی 2022 فقط 9 بازیکن همچنان در این دو تیم باقی‌موندن. بقیه‌خداحافظی‌کرده‌اند از بازیهای ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/persiana_Soccer/25304" target="_blank">📅 22:36 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25303">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RwZAtIplzrtxMSAhq59CmMYy10-L-YG_qR9yU-9Wruo2ymAQWrgQMdDxDfTPzZqeFnPqcASysfJvisQ2WifGChHXFtm_Z37ebIdtdhFxULiGJXms4gIZD7BEK0qPVLVs0ag_ByzziCSGFYsAn-R0AYPdy_vJxMYYM6NGo8PA2pBodiVGbuEbOw-i_ov1_6VkJNwoikIZ0lGpA7oC6V4UOVfL01XeSJ47D24k2-ZVyPWSzJJXoJIpP3EdE-S36wUQXyRUTOvqj2WNynLmfOcTFRO2HxTt31KaDNridTpLY5rtfkBfw3UpMgAP6zXLndaHIy5ISKQn-66XTWybvMuuCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی‌پرشیانا؛ جلسه مدیر عامل پرسپولیس با مهدی ترابی در منزل این بازیکن برگزار شد و دقایقی‌قبل به اتمام رسید. مهدی ترابی برای عقد قرار داد 2+1 ساله با باشگاه پرسپولیس به توافق کامل رسید و به پیمان حدادی اعلام کرده درصورتیکه تا هفته آینده مشکل…</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/persiana_Soccer/25303" target="_blank">📅 22:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25302">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZ68MQ2wKg8DENeDn6UiKkOLc6N2Vsdv0a9UkPRSH4R45u5Ngvc4BkIPvlm5s5Z1-RUBkmhHwS5jyMm9kWL1vOBNcneYuHOKBZKHw2o3u-qjJi5BoTDDTwmTo-HNQq9mqZ6LO2DgtObh45uPTFicXAN6KloApGut3xkRfmxdwoQSkbNCfhIAf2InJuY6PVuxjCNGMYV0ihVYUilcNaq2ldGStFBlmzHbEX7O29M4QLO2P5JYKF2AUYt4tMOpYP7tycoMEG9ghKbJ8snZjFGGNlgqU2AZ582JXAD3ftn20qdwhes4sbMFLA6xnhzdXxYp-GfrWHy_AAsburp72uuS0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جلسه‌مدیران باشگاه پرسپولیس با مهدی ترابی و نماینده اش شروع شده است. تا ساعات آینده تکلیف ترابی با مدیران باشگاه پرسپولیس مشخص میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 74.9K · <a href="https://t.me/persiana_Soccer/25302" target="_blank">📅 22:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25301">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLorR57gnCGNM8tW_B6e8YzAZ2a8GYf2Man7oGHVuGvS51DSyXyPvHtLozPZCApS_b_tVNIMOP_gmwtBSSnGTtMv2QruRbS6T7JJFeWZBRqj9KDj8BdNPw52AnBhylyHtiYy8cS12xkYDoOkYyq93DjSUSsgIa3mzgd1r-3yJ0hOKnv8e3dDHEwmLAPpzmq1wGS2XjM59Mu4zYiiE5SVNePbMCNjjwAeWJOOTLFt1ZWwP2Mfzndn8hMKNyOdpXjyxZ69StwvywfxI5RxiTw9e14QND-QLWh1FuGJnKc9H3BcCQopDJ1YRc3PleoQ_QD4Yg-EA6o5-7Wc7fvHtOouag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
دیدارامشب‌ دوتیم‌‌ ملی‌ مراکش
🆚
فرانسه در ¼ نهایی جام جهانی رو عادل در آپارات گزارش میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/persiana_Soccer/25301" target="_blank">📅 22:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25300">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IlYHKGYQHrpQ-0V4VX32MRlSPy3Knb_RtHuyfKmDk_j5QFziHqrNshH2N2WTVKeMCnOC4dZPNsAGKN14PN9qUrH6pNObNeAr85lQSXK1wktgRtC8AC04IWa4y57xasbWXZ4VW6g4NGqMN1zfS8iR86Cs7QS5e0CFWrX564TWLQJ9BOFRL9fpUHVraidu-JYRJK9tkC1txCO4YlX3SoRjCVcrISsv_yMPILG5WGDHUHWNlTn98dvmS6plTyL-L55vi-VorfD4e6zQnBOeYI_MjEV_T0aCKWsCKG20h-g-jlHwhpwmAfflMrTJoAinMSqDN5aDtNqRe2mRih6N30e3DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
#تقویم؛ بیست سال پیش همچین روزی ایتالیا با غلبه بر فرانسه در ضربات پنالتی قهرمان جهان شد. با این حال، این مسابقه همیشه به خاطر اشتباه فاحش زیدان و ضربه‌ سرش‌به‌ماتراتزی تو یادها باقی مونده.
‼️
زیدان: از همهٔ کودکانی که اون صحنه رو دیدند عذرخواهی میکنم. هیچ…</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/25300" target="_blank">📅 21:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25299">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gKEJNO79ijOsEL_qXbhQyFAEKiJ4p8UI1LA1PcnVt7tjaCQXaWpayrQNcjq73ZcXJCicaI1JjrOpi6zRejBp7CqpQEPOPrW9vcvfemtatkxmZuTDkIXQnEPN4CQ-OXjW3o43lMzQYNtxc67ko3nijUdX66FjdhiCc9YPwyu7F_pSBMmIio6Z96Txp90uplSWyIdAygRBP147LmzxXEnHTPFqIc25ndRLW6izd89eSR5tx_whpTnaiLxWWh6lEEsNiezEht5QGMTLueyyxmrcpuXs_25H3UlzOn5rtI4KC8H9kos4rqWo5sKQCZXUvk1azGtK5vS6UwHD8y9_Ov9Hcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇦🇷
باشگاه یوونتوس برای عقدقرارداد دو ساله با امیلیانو مارتینز دروازه‌بان تیم ملی آرژانتین به توافق کامل رسید و تنها توافق با آستون ویلا باقی مونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/25299" target="_blank">📅 21:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25298">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LOOTE6BxetT1PnUBWMtWmAADuH2dTKClhB3H7l1NLJTqeZgiPPkFQkH5y-9K5l87KXObENkXV6vRZPGJ6dO8aL7xlrhe1umDKzfudFTv_AFb-YYQXFYneP5Fn2mhGlZNzckmIjay8BRs5Yt1M60ebBUWdCIO-j_enTWCaiYrdlE3ghrJhQk7ajaCki-4BJ31_0FH2Y65k6hTwtEXiIunjNwlsiR1cJAKQYSWQ71osyRbFWfhR1_z9RuXDvXEX7lttV_rBvLHIyxSpDZeUTAetp51C-cSRLmN6wXs43JHWIGTVtTQssnTcNzaxefag0bX0Qd4pNWdTUfHLOWuavcQMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇦
مراکش
🆚
🇫🇷
فرانسه
فکر می‌کنی کدوم تیم برنده می‌شه؟
👀
🎁
۵۰۰ دلار جایزه
بین تمام افرادی که نتیجه مسابقه را به‌درستی پیش‌بینی کنند، طبق قوانین سایت تقسیم می‌شود.
👇
همین حالا پیش‌بینی‌ات را ثبت کن:
https://t.me/betegram_bot?start=p4_r4EF37DCE
🎁
جایزه به‌صورت فری‌بت و مطابق قوانین سایت پرداخت می‌شود</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/25298" target="_blank">📅 21:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25297">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vez3-ANCZcKRni6TUaF8P8FkOTdqzcc1vQLBnc_l6lb7xLWw-D94nMyrKFg-LsydjSNqN1FpUB7hOyHPFBGfMsyKCl5m_VFp1K5c9mUs1wlF_0cIHtpJayqvOBI-woZR5hcyUwicV80kzTdHM6FxIeN9xw1jHv_5pJIryAZ54kP8jOLrGrRqR7DqSxPVHa2fc9rjBBV9YJy6VEe88ETQuEiw4rJmmyPllhMTSFZ4t6b6BqnFTGJ9mPN0QXB35NMeUrV6nxszomrfdDPdtKTLFMKGNVTYuXwi4OLsSydKPtRmlqlypqr2iMO9VLmazv3U3MtB3_Kaneuo23DRec6K-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
طبق شنیده‌های رسانه پرشیانا؛ هفته آینده جلسه‌‌ای بین ایگور سرگیف و مدیریت باشگاه پرسپولیس برگزار خواهد شد تا مدیریت‌سرخ‌ها این بازیکن رو برای‌موندن دراین باشگاه برای فصل آینده متقاعد کنند. سرگیف بخاطر مسائل خانوادگی قصد داره فصل جدید رو در لیگ برتر ازبکستان…</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/25297" target="_blank">📅 21:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25296">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TCZ-cgfl4K3xVHvOQdSDH22LcxVC34Iz7-BCwUptLADQ92fB2cwZAmlPZWrG2y6oeKx4aLLV6cuz_Zo1hqdeWymEItzf9EXUaFe-lSA1IMv73ObA7tYMVRTRW5pt4YzbuGKU0P3xIgamUGcwjnspnGyD8dy1Imv5x9YLXNPpqjCBwOv2v5SCznVMKV13ywEyLyLY8JgYDTrKvUq2iENb-imTOZwVyVCTUvST-FMvL_v9GXCC5_qAHeHRQzEA02UI5rajB-GSfVtdBhbVvrjv21YYzOwtZFudnkQPrwoe8uiRJrQsDyy403UxfXXSnmF31uM08g0zaPqeS8zmLBESzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
بنیامین تانیاهو
: راستش‌روکه بخواین لیونل مسی 39 سالشه و اون قبلاً هر چیزی که میخواست توی فوتبال به دست بیاره رو به دست آورده و بارها شجاعت و بزرگی‌خودش‌رو ثابت کرده. ولی واضحه که هنوز حرف‌های زیادی برای گفتن داره. من در جام جهانی طرفدار آرژانتین هستم؛ حالا از فردا بازی های آرژانتین از صداوسیما پخش نشد تعجب نکنید:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/25296" target="_blank">📅 20:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25295">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b0KLN7J3A9HuTcaUb2f5FEl0fMwUWUTYupMVSxxOPAaL0oe8CODzEMVhdJFj3cceA37q0c26yF9Cy06I_NJDm76Q-XLB-k63RoHbd-ylSQpLKWuz6-HY3Z3d-OWpAqKV1AU8mP4iC8D_BQo9EJrE5pECpjBDBk7ZsAZLyLMmKAcvHAWO7iEgaPB2zwfzJAA1Y1-OemWxcjn8VGQoWSVdHGnaJlvYzuYPrZQwzD72pENy0iWmH6-Ah3U8V670F2rT5fda6o8J5Mr1DVcyuGfzP-gDT2ft1I1rq3Zecd_UuCC4UvA6etlq0xAdJRDZGeZoaWWen2sz6tIMP8-V7hVK-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات|داوید دخیا سنگربان اسپانیایی 35 ساله فصل‌گذشته فیورنتینا آمادگی خود را برای بازگشت‌به‌باشگاه منچستر یونایتد اعلام کرده‌. دخیا میخواد دو فصل در منچستر یونایتد بازی کنه و با پیراهن این تیم از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/25295" target="_blank">📅 20:39 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25294">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vi8ONwqAvrgVg8NCyn6OCgVB4qamxSE2Vt1wYu-LfNmBaNow9T6WsWmXgGsmju24ZJSkj3SJ1-TTRBlx78OlvDNAW8pkTvMnLSlAMcWBVdsY7Z51LPEpEFqkjoevFz74rvQHK1vQUZN3sBQ6gLvAgrUPZuVWgmOx3FTA5sBE-jxtx-iOSypL44CMOa48zVkNHVf8fREKdoxzi8ne6HxcnKcENB4hXQRZf6To6PoNuJKCZ_5Ucb7uzqB4gzQQbE4QfSgmEsYFAvr8L4R-MF2q7iXW07p95dupgfxa5E5Ag1EmO1Sr0nQNSJq3li5dvuOZ80QSl7lEj_yQhA2k5Jg1VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ طبق اخبار دریافتی پرشیانا؛فرداشب‌حوالی‌ساعت 21:00 مدیر عامل باشگاه پرسپولیس در منزل مهدی ترابی جلسه مهم و سرنوشت‌سازی خواهد داشت و احتمال اینکه قرارداد 2+1 ساله امضا شود بسیار زیاد است.
‼️
پ.ن: دیگه داریم لحظه تمام اخبار داغ نقل…</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/25294" target="_blank">📅 20:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25293">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EUVTH4KFCtkmiaqUKLssh8MAIVBLBMtnsVbvvg7gYYaXTk52i-E4jc526Rt0a9nvP-YTL7FAaKKvgq70SutOme0j70wsL0CB1WvnnB-MTUioI9mA37a525aQ8t0TKYygpXGrVSDNgmbB-y3IyajGaN6IL0IqkAJWHNaLapvp0MKC2iaOEzoe_XJ6WSDk-LC7hVF8Pwwr1wEC4ZZeldv-iwVynM13_6wk8RVYcxB3BHOwk7559sOR8XKpTanOW38duMFMdp1x6NiOvyKC6Os8dH_DHN18ditoNp3bNoilnxKKYVXse1cKUWFkwoVFPtlz6iDqDNuD1a4XIJzNE5STeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
امید ابراهیمی هافبک 39 ساله سابق استقلال با عقد قراردادی یک ساله به تیم لوسیل قطر پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/25293" target="_blank">📅 20:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25292">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NNQHYlSNy4wGHCc8LbMg5h36X81QcI_SsQX1co1a3Vs17dZwoKueu7sUl-sF72y82EoHVlKaXeLErHBFxl2nKT1hcSshh1g0d0fl9iduTyFU57sjw0RSPX5hz9A47ol9mZ5vvZtn_aybGBODE-GHmt7XUYdblQ2ZPAOUbHK7qDeGBU7ZeHUC9JM9fCdK-Od-NKqySHTJ9RbqMbQqXINQYcGye4p5vYmKgw0EbHMMlSlqTytuKaLqUTmnobrJW9eFyNOuXV6cwiVXyW0RLV6MtR5LzY_vsoYFZxKEynJhJkP_9o5Ej5qisRqJLPZ31FMYzWQyRp7nmGadWlLwSeHXOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هادی حبیبی نژاد قبل از اومدن تارتار مذاکرات مثبتی باسران‌پرسپولیس‌داشت امابعد اومدن تارتار و درخواست جذب مهدی‌ترابی دیگر قید این بازیکن رو زدند و او با قراردادی دو ساله به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/25292" target="_blank">📅 19:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25291">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tsOrOoVSvqoV5LnwvEpPG7-u99w8C0JxxqcsVrTkP3TZxH6vxvmrqYiVOtiMLIcgrmSw9nFuKpoywkETS-Ak5Lkxk1-GrbQDUH8Aqbo3DePM3QsvZjnppPvyx8Pbgk8In47sV1JZEJb0Muj5EsKPYZTkd5sXi3tuoHkBaZcJAHRBLNthafRpVEJWgrtAZ-0ES_n-euakOur9EvLeu96VKZSsxnJhX4YdKx8tRushw6ELmjR4EY_MfUWsY_rJOIISm_CR4y87gd4A95DfayEtyQat7DLnznlpjr1g-Xu3BIPyfEiidioMrr5IeonkTB_XxhLcf7xTIseKWJ7a1CLSHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیرورزشی باشگاه‌الوحده به محمد قربانی گفته هرباشگاه ایرانی دو میلیون دلار پرداخت کنه رضایت نامه ات رو براشون صادر میکنیم. همانطور که دیروز گفتیم باشگاه پرسپولیس گفته ما تا 1.5 میلیون دلار حاضریم بابت رضایت نامه پرداخت کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/25291" target="_blank">📅 19:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25290">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qO-nme5pvgkUT9wtqrDeHxXSO4CyVFTR0ENwiZOpzmDuJWoR5L3JokfKpS6-1XUF3_I1jtCtKP2EQa_ZfusP0N16ugHMLrY0rZN52rAkkFc6UTG9zMieYCIG6tusSdXPGGDzFwJOB5KTLyuIki3zZCWc-DuXPMfzWyaRmamokF8M-pKRhRBzUyscVTmQl85uKbjKf9JIhv1dS5s5SfecM6-W96yTcSD5ftUW-F4G-g25vQ9XO_0gp7cXXddS7g0pZAPrF1fUu6H2ThwyfRoEpMCqhWlU1-mK6Rw5uFpMLNBaF1uMi5KG_taLCeXwTggMyAlAMPpXqDKE59xO5soipw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
تونی‌کروس اسطوره باشگاه رئال مادرید:
مردم همیشه دنبال‌بهانه‌اند. تکلیف‌فوتبال‌در ۹۰ دقیقه تعیین می‌شود، نه یک‌لحظه. مصر نیمه‌اول عالی بود اما بعد از اینکه ۲-۰ پیش‌افتاد کنترل‌را از دست‌داد و آرژانتین استفاده کرد. این تخصص تیم‌های نخبه است.
🔵
مردم مدام درمورد داور و VAR صحبت می‌کنند، اما دلیل‌بازگشت‌آرژانتینی‌ها کیفیت و ذهنیت‌شان بود. مصر نتوانست‌سطحی‌که ابتدا نشان داده بود را حفظ کند. اینکه مسابقه "دزدیده شده" یا به آرژانتین هدیه داده شده تئوری‌ توطئه است.
🔵
بخش‌سخت‌فوتبال پس از باخت، پذیرفتن اینه که حریف بهتربوده. آرژانتین‌شایسته تقدیره. مصر باید به عملکردش افتخارکند اما از اشتباهاتی که برایش گران تمام شد، درس بگیرد. فوتبال همین است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/25290" target="_blank">📅 18:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25289">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D1feT61UxeDmT9kJb0mutX2DBBiKYv0WLJebhoAYsj28afvpSa5IngyGgsnxUFMljsXPn91QifwasDCQdJ2u1p9syn6KlgS-IGUUhAs-KiDLrThhQiMDLQ-Sf8ch-RLcy0Vo6l-QrEexkoiqFx05uUwUTnn1-5JCN3HaqOLyBjwhNZQ1rbJ40yVu2HjWXWPMvZ86qQ05_bPVqIr7rMlZ-rtRt7GPxLGwIIfA47_ritBpjEKgIoPMPWEeWq6o_W2ddcmIEY2rO8_nZOlBGuXwBgI_yKbmCGAG7N_5RGGBN80EfBp2nE5KiJWlyaCY_bdVCBB1dFUhTsqR0Xr34y88vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه کامل و دقیق مسابقات مرحله یک چهارم نهایی رقابت های جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/25289" target="_blank">📅 18:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25288">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tPJMAUb2Rfi1oEEPrzvxxmjWuALNjH7SZ4lPqu88E88D67i7D9UzEKTiPjRHf8Vu23dw9xZyhf5T_aUi_tm8ubnxxE_cpYVaibLQ4ayVYVwRul0sN7qKAGeFENkz3pB3E7ZRdzrFmtYJjRM4ODKhFcyA3lnQOJOdX1CsG_QEF34z0hhLI4IMTyIFrs16Yyr7mzF2aveHAqbrwIauNmx6nePvrmdNyPmCB9Eljk1Fy_uIgXdWc0vsXdbgK8uP1onrWByzv0GRRt9W5m61LFajuAJNSujocbNsnVbkwNV8EB2ewjuQLQ5fM5At48szzTtAEN6QIK2VRh6D_FJqFg4gmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
#تقویم
؛ بیست سال پیش همچین روزی ایتالیا با غلبه بر فرانسه در ضربات پنالتی قهرمان جهان شد. با این حال، این مسابقه همیشه به خاطر اشتباه فاحش زیدان و ضربه‌ سرش‌به‌ماتراتزی تو یادها باقی مونده.
‼️
زیدان: از همهٔ کودکانی که اون صحنه رو دیدند عذرخواهی میکنم. هیچ توجیهی برای اون کار ندارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/25288" target="_blank">📅 18:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25287">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hI5jy8LQiprSJK3f75BmNBynBrLQ6_kZf33kOiZKbyI61XMKhpQ-O7aS_-MVRspTbtIqjp3ghs7X9Yru5hocmwBENDPHO1lyxHXBrxl1dQ_DMWeEi7imOjDHLPlGaaMlravdOR166NgUk9QpuhHhtXbYwoJTuhelF5xZp3h4H67mQ32cqqoSUy78VLEQG0k9RtbIy3i-wfClRNwE-f1QuNzAr5jdH-syawr8Xr704HcvILpY58RtcWmOQkd94Q_tap5R6mMHrFzy_u8Sh7IfydteH1pumi875vm_MtvlBvlel-6TqrsXXvvFUiOhyPQsU6LQ-6KWDnvbTO32sIQjIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#تکمیلی؛ طبق‌شنیده‌های پرشیانا؛ مدیریت باشگاه سپاهان درتماس بامدبربرنامه های علی نعمتی خواستار جذب این‌مدافع ملی پوش شده و به نعمتی اعلام‌کرده‌حاضره‌برای دوفصل‌حضور دراین تیم رقم مدنظرش که 150میلیاردتومانه روبه‌او پرداخت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/25287" target="_blank">📅 17:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25286">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rhnOO4Cc-fsyjvSkXgeumoUc8mXfYR53ptykXdwny2jp5nXPoVCIbQG2flJHXcMhbeLvAryB6KAduATLHopuPmJk6slkUsRo3cjv_2nw8EE8-46llMFMeFFd5eVlTU_JSuqgsvmFsZR23af0J9rXxyP3LIuCY6Sg97vTSSU6vPVnRCD9wyG-DSuiW-LsUDemBuembUq2nHyZ93zLvd8gMFi3CrzmBKWbWqkW33u9Uhb9finOYYP8LT_GlfPMM2YKmfWTwqxIpgFtr1nB0W8VAdIOmxCpzT4hBlWt3daX5u6zPojXWqdbFzpJhoSA7mrFaWEBs9Mz2vnCPE2V5piZiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
درخصوص اوستون اورونوف هم پنج روز پیش خبردادیم که چندپیشنهاد از جمله پیشنهاد الشمال رو‌ی‌میز مدیریت‌سرخ‌ها قرار داره و با توجه به‌ چراغ سبز مهدی تارتار برای فروش ستاره ازبکی درصورت پیشنهاد مالی مناسب؛ احتمال جدایی اوستون اورونوف از جمع سرخ ها وجود داره.…</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/25286" target="_blank">📅 17:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25285">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rhgn8YIKf6JjjzZ-SkZ2j1bi5DUCUkHKyzaVpMZj1Fq7eWiSccGTHjA8C4VnRy7FOG9kzWZwGzSzKB4dB7GT1sk5rro0-94Mx-Foq_GLJG0ln2ADtl21ewAviCZ3L_LvWMSXWMiQ4u_th0A3EQb27LS9FXr4bXTMj9eJtOHyiqFX715fY77Y_PSkZZ5gU1xgWMwSTLqvrACOiaQifuDjAcrdTZAidGGFgT1XJR9YQtvNyAIRFbyVPdFbCc03JncZ1mYzuEfa_WzuaZkgCZF6lAbavNBNopeEw3s_OLcCaiU5SaA8uh3rFRqjzkjDFZxck8aPXQYGVUm53nvMfqmA3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
ارلینگ هالند روزانه 6 وعده‌غذا میخوره و حدود 6000 کالری مصرف‌میکنه معادل 24 چیزبرگر. هالند عمدتاً به‌مرغ،پاستا، استیک، ماهی، سبزیجات و عسل علاقه داره و بیشتر آب مینوشه و ازتمام خوراکی‌‌های شکردار اجتناب می‌کنه. جاشوا کینگ هم تیمی سابق هالند گفت اون مثل یه خرس غذا می خوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/25285" target="_blank">📅 17:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25283">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e5NlEZGkf5VSVawmTsFRIoBcMWMGKOSa9L_n_ONgn9AN2d5PwIp4Bq33Nq7J8J69GssXY9hLGry4CY9QKx6MDu9V9rkhpv74mo5bgivLIcDwRmkm49ZxXt96EA4Z18bsT4OFKOUd2SPtiTABzbcs4wgwecNPxz2g4caSO6ceHgZnktY0dZD-4tA-bca9_5LDUDX6FKw0lfnYk2bb0hNxmfR41nS8PiFLyk_acna2cwdTKr_JdJeqc6NeqslsuaQBbPup7_hv8b6ZZEzhHUT5QX298JjQtNzNiqBq3eUQAFVExdStoXT-aGAwv5phto7tNDG5FfM0Kq7ZwLbY7neN_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
جواب‌ فوق‌ العاده رونالدو به‌ سوال خبرنگاری که گفته بود میتونی‌ اسپانیا رو ببری: من تموم تلاشم رو بکار میبرم تاوجدانم‌راحت باشه حالا هرچی شد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/25283" target="_blank">📅 17:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25282">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HpOMBwNKN2wfg_z08qmRZaWPjl98xYVMuV4G61aroynS8iB8BS3_TGmnM6-W-8hFAqSdM3xmCuNlzvv_yGsl4V1iRxwDQ-b7SylTsAAvvpzUFxurPDqixJV0y1nymIdOk-Pwom4XAinCPaF2WhZTwuWCf6B8nnrVe8PIWu5GEDWOoAZBdxTce_Dulk9rCunsaHmrrxLqnMb5YM3zJYBlCP_32eUMoZt40HRk7h54i1vUASYVZc-Nk5-Mo3D8qmSWlMbL6jf1gwQTD0qz-DHVaDtfQz09uwjEH-P62KcKOOFBa9JWuEDcmqLgU8kqqhAB-9yY9J2xHitbvoyMTR5H5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی دو روز پیش پرشیانا
🔴
پوریا شهرآبادی مهاجم جوان گل‌گهر با عقد قرار دادی چهار ساله رسما به‌باشگاه پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/25282" target="_blank">📅 16:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25281">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jbhEDAVpOCDSgxrNrxdN6Wkr3HXyCDvT-BNxMNZ-dQ4XGBSZpllVikcVFPhgKtOc7rOKvcYj9aE7DbkrauNQj9KDzLCNfY9QoTL8DaKvo9Mw3dHv4idg64V7EYUq9rqaO1Wji07H6g3KL3ontJN0QfrYBgxm3wRlfTv8kiDoC9ufnnxTUFabFZUXXGIcZkxCh3hXvQLTJeSfHg1Z24mCmzfbPAG4PRjTncJ3szRz5GagxhtCBUTNfCUMzjA37i6LRAulMmjcL_VtkAYswTcu2Cghfi1kbMroRiYWjhAKFMWAHX-GcqTvW8CC4CWJz-qwGVededh-pcza6I4Zsren1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ پیرو خبر روز گذشته پرشیانا؛ پوریا شهرآبادی مهاجم 20 ساله تیم گل گهر سیرجان دقایقی‌قبل درتماس با مهدی تارتار اعلام کرده که قید حضور در تیم استقلال رو زده و اماده عقد قرارداد با باشگاه پرسپولیسه. بدین ترتیب شهر آبادی ظرف 48 ساعت آینده با حضور درساختمان‌باشگاه…</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/25281" target="_blank">📅 16:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25280">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‼️
رونمایی‌از تاکتیک‌اصلی تیم قلعه نویی در رقابت های جام جهانی 2026 که سه مساوی بدست آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/25280" target="_blank">📅 16:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25279">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VSAgJro8c9tkqCKH6XqI793yc9GRkgOmendiurqI_rYCAZ94muTmXcNmsR9jMPYvbfu8mNFoDJWNJ8U7AVNMfnMuSI7tT4H5n4qhD4En9JzeceQFPZ9lWqNuP0n0ZcEGmFXFIBXG1OHyRhlJ0CF61i_VVI8flyKqQ9hK4Jzp6zhchYMCjMoG0kmYHPOUt89g8trTra8X86OZpvePYCWDYNrwoqROC8jfj6dPIFLLuWCINBk09erYohd4qBR1qJpgd0082m2uIHBkCswtVM0EjjIXFf0aO7udUjowo5ba2AtxkaX8dlKGvn1RDSAUHAOEmBLHzSB6ODjIJG9mRa9ILQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویدیو لو رفته از کلاس‌درس‌محرمانه امیر قلعه نویی برای سرمربیان آلمان، هلند، ژاپن و برزیل در خانه‌اش بعد از حذف این تیم‌ها از جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/25279" target="_blank">📅 15:54 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25278">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f4AbLNDyMCb9k4PW68_-BEk0disgfH6RbHKi-mIFk2m4pQBKzELOksGy6jaDO8e0Hdy-l3w9P37eX2YfRCqa6IA3jzLUP7UaqOxdtpbHhMqRwR4VjziO3prvFHGrItSRFmaZsNZ0wU6f2L52MgKKzqbpYMN-e_-Uq7E-WZxO3cjNDRaKRDUeJExF-l55holX6wsVwdLYhcc1ZBcMLcuLTS7K9PedSSS0dnyz8VJNWQBT9ACeghUs82D0EfWKfcurPthwyT3QigFBEVwGJaaSPRXR6x-34LOVAq4DclVEltS3heElu343DBEN-2fIHADvafmQZ61Myur3qfHa54AuOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛مدیریت‌باشگاه‌استقلال میخواد بعد از تمدیدقرارداد یاسر آسانی قرارداد رستم آشورماتف مدافع 28 ساله خود را نیز تا سال 2029 تمدید کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/25278" target="_blank">📅 15:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25277">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CJezddy_TNgbm75DIRcPu2rmLFDrxQHtinwQYmY5oF3L84RZebQJlFHBP_cuN1ADizCWCf1E9nLoM5W4R2ov6Lezm8Lb6ae4j86RoSUsB8j2XJ8bsHeQBP6_pgH_O_Pek8UGgnncITSPsqSpU59XPW9sfh-8gKPy7PVhxsQ-FvkWSUbD9Pb3YCCtKj053S0cod14Zy_CddiAApDzBSvS8MO1hnsGLnCbTntONHKHI93iu1rtP_NolwakITDQDgJ4UuclVWX7AUFFSXNXDcml4bAqwNoK5Ag13Mln0DorvXCd6p3FPZ7uhAao_sPaVZnp77yBgcVaKP67vdHA1Y_7iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
#تکمیلی؛ کریم آدیمی ستاره23ساله بورسیا دورتموند برای عقدقرارداد پنج‌ساله با سران بارسا به توافق نهایی رسیده و تنها توافق با مدیران دورتموند باقی مونده که باتوجه به علاقه آدیمی برای پیوستن به بارسا بزودی بند فسخ او رو فعال خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/25277" target="_blank">📅 15:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25276">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gOwU0r1NWsmhNeygxOO0YzG84AR90IFV-kHzeo0GlWb5CQ7Uw00Gs3UIGLGD7JI3QSgVBgaH51QA1k8cRaczIroX79v2xUgGbCCegCoK6wFMEJ-g1M-Kd9Wjy_kk68uu-FTkqAM8nzUepV2Ad42feFDE3ZSwyBQcokuN1kbVE6hilIbAPqieN2JP0U3UVQZ8FtCx3Z_55SBWvGzyjwPK8eAXRHdc8O0eCz85LVhiIVVKxru7cvNOCK73ogp0-BAYAVAFHT4Id0fSIAYHy3w3kh0EDsN4-qlRZyAl1chzM3ZXKC9-fjmjTvv0gnk7I4uHHXF8zween3FRFiZt_7XQGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌رومانو؛ ژابی آلونسو باعقد قراردادی پنج ساله بعنوان سرمربی جدید چلسی انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/25276" target="_blank">📅 15:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25275">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c-2mFTejh6U0UUJbqK6Oz7VJh2oIvyO_I36tS_I7-MWN554qC-4JO_0RBpvyuhD2ADjQuLwPU0aWPtyk-EC5nydRWvG1XidsS_q_kJ6vTA7bb7kNssogINrHcJ0R4WUnPWcEBv_qiz73pakfuwDaLnT_ucrDY3hUMk7-w-WyGvAbmvFxIjp28G_qHbBNcBmaTXmMBvm7-a3jHJ-L11wgjye8_xjaj8bcfGx0EnjNc4foxYsWpB_6YPagEQM03XtVSFx_tMIOe1Jx3-lt3XIe8oZLDFYHpXIn574TDyxYwV1LU6Ds-DVbV_kDwe5muZKwi-kxDmmoyW-dQIfazub6lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
#تکمیلی؛ ایگور سرگیف مهاجم ازبکستانی تیم پرسپولیس‌نیز درگفتگوبارسانه‌های ازبکستانی اعلام کرد که به قراردادش با سرخ‌ها پایبند خواهد بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/25275" target="_blank">📅 15:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25274">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pC_XMGJ--u4pip8OKiyznbPJN9Rhhnv2efRwio_eyKdYJoa-rq1PTFashlLLLdaI4x4UAwkjg1_chshgNj-alJ4Qt7IxNHVzrarIk9JSa9hDhruEiuzTovfwbYnxcO3hlcNyaJfmcPtmkvsCeCQDPq59ukGUpQAmjPp0XzjaAMSiltsc2CgeS0NJv3YhPOQjUnjuduoOSb2DxEUV6PbWHs3YNlMxuICE_XFfZQ7D0svM2pFNaOM8ba5QoIplCtoA2TaHNTkMXK4RBHuLlTbkL2u94VBtG-c8R3ZdR8WCUKjmCfEd-qwvqFaeJnrm30dFY8RAPLuU-q8yWX0jgi6rng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
آمار فینیشینگ و ایجاد موقعیت بازیکنان جام جهانی؛
همه چیز خوبه تا زمانی که گوشه راست بالا رونگاه‌نکنید. رامین‌رضاییان هم تو این لیست هست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25274" target="_blank">📅 14:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25273">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eaErXUHg_ZdciSLrdRYdEFwYyxsoGHImoQyyV7GXokBmNGtke9vUGr2plPTEOXF1NEASP2CYRYdio4VIm8HPYRWJbCfkvMiANrcpykZJdWwxLL58vbxmbCmmDtBFevZUwbZK0q16yJWg-Wway4WwYG6Qw2hkOUEvWMZI3DMK-Sq4tcb1mfUwRy2puEOE1VFj6cidd2qYxKtHjaPStt1NUAZt0haFvRryvhprNNJNI4FqgN1eYBRea-r4jC5TTGCE0Q746pCAKjXEtNXA8oHDx_s3SVdpew2RJY2n0p1ea3RDW4hBzMmXEcTGy77lNxv2ERyantb2mG5mNNZZcN-r2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های پرشیانا؛ باشگاه الشمال با ارسال ایمیلی به باشگاه پرسپولیس خواستار جذب اوستون اورونوف ستاره 25 ساله ملی پوش سرخپوشان شد. این تیم قطری اعلام کرده حاضر است تا 3.5 میلیون دلار برای‌جذب اورونوف به‌پرسپولیس پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25273" target="_blank">📅 14:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25272">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CTHlKOA6aNBjlvTXeTb06ZmJqFezMAPzSqQHanCRR4hQ0E2SmBEiXyTW9yHFW_4GQQKSbUUUZKgC0TyXipMdn-88WY5c4zmI5ozzqUX-Z2kYfktQ5CEzZP1kyLeaaS0v3diDz65hZ9QbSt0R4EJDsNuyL805ca9OMZVFpNPCUJjuyyOe2WGmrPacnbTSXMseKbreExbH70jVBT-51AEqmlHGqaRZIJmMJ7bXyErfoHi87FzjHvQ_-CBzs3RlG2BhjQKFAIl6cDiBATvJfXbH6F3JeiTO7C0KFw2w06jHZXXMPVmMODS3ItPyEGKz_fLuRqDKU6EsvRRTi8GOrtmLjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا؛ علیرضا کوشکی فصل آینده در استقلال خواهد بود. تمام‌توافقات برای تمدید قراردادش‌ انجام‌ شده و بزودی‌راهی ساختمان باشگاه خواهد شد تا قراردادش رو سه ساله تمدید کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25272" target="_blank">📅 13:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25271">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ik08UHZAeMusm4UT_RUKVFy-ipla8BphmjIEQk8xhr3O3pAYm6OyXFbl-y4TK3SMkQwggkMvF9_qH8AI1fXHWl9SfWEX8KUM4IT7EA3lrXf6UzJ2KX5yE117EOGEPMD1CjuELuwjcZIvh9Y0VB5R3tpyAMQmO8j7FSnF6rISQKBf_1FTmL3ijBZsi8k9VgRSlpiZp5JMEjUnWiofVFE4h2dcrG4uOYiMF2rLsmjSBqyk5Ot_OfEln-Rl-ukNqNo1PYd5R_tsbZV3aY5imH0nh1b2HCzA3pKGfuObH5lvdxbv2YGPAGdthhX4Fp_KdgoiFPTMaoTQJ54yLqvAxjZTSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی #اختصاصی_پرشیانا؛ باشگاه استقلال باشخص امید نورافکن برای عقد قراردادی 3 ساله به توافق کامل رسیده و هافبک سابق استقلالی‌ ها برای بازگشت به این تیم منتطربازشدن پنجره آبی‌هاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25271" target="_blank">📅 13:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25270">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dDvt08raBKqq0Q-Xa-NzkBre7TPRI4Fz1ec0kc8rEGpk46_GK7Q3W5SZ85-9nA-VkVqYu5NKOswTtejcO5HIOyFx9lKgHUQ0_3Z2CjuZBahmfEhA-R9NslYBgpa7Duon6btHNX7fqijBBtHEX28zB_db1ZO5rqPal7zisrhXhnhmjJ4-bNWq3M802FkvC5XmXNM5xJ23K9U4bmLZNRPi24BgAbNgEi4_cEUp1zlFr2li-kHwpT2fk2lreG7EG3bpHpXtWXR_EaSyQVkJoycR18WgW4jjSOaevV_aozUiCPijbmbklh3m8FsaTYZJVXFCPm2VZ8BV_wyjIZ4HiKWEWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇦🇷
باشگاه یوونتوس برای عقدقرارداد دو ساله با امیلیانو مارتینز دروازه‌بان تیم ملی آرژانتین به توافق کامل رسید و تنها توافق با آستون ویلا باقی مونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/25270" target="_blank">📅 13:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25269">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OeXyS7P5-qdsu0FJrrX-HVolJCmhu2ux4aomB5ngf0RPeNSjryqJuv7RLvXTMI-j1Q0I6LaPBdAqGIAlJcYbD3Vaq_jM2bm3KeAWjuKatBjbny0KEwXAcAzTOMHaiXwlIBTifk9Sv0fRThY6SrKLiV3jdyTnYr2wJxmQMobEGEmdW_DcYvjeQam_ifRW95t0RD6CovTPrKGIygccEPQhIr7pE0ic1vIfPjOEgieDB031fu2kdElOyDC6wwDgfB2r_ODD-c9M91bNuxSdrq0dLBDiZIAi4DDXnSKcLPjv_Cnx-IdqlpnBNp3yT5NCmLWUanXrwQwlIC3Q4GdNnxHK_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
کریم آدیمی‌درسال۲۰۲۱: بارسلونا یکی‌از بهترین باشگاه‌های جهان است و برای من مایه افتخار است که‌آن‌ها خواهان جذب من هستند. در خودم میبینم روزی به این باشگاه بزرگ بپیوندم و بدرخشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/25269" target="_blank">📅 12:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25268">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jJFpi5WqMi6k4PenHPolQHEOutceyAwq_YxNE9y4dqYmw_GPv3ZUASw2XELqoMLKcHLt_ta52DdtZTkTTF1pGI6BDctp9MPey8KMkRAdG3jfQvrZBFcxfY4uoEDTNfFSKbnB8s_TityJcMP8K2-PU9ffMboaCX9QMKvMV8mXFJacia50wAAP11h3mtk6xWvwLICpGpfKypJkSyc46JXPkz-0bmn07K7ryjMVaBxUvKMWBNXiH6iSKqYP1P5o0oFkbcn-KkL9A_WbkmXzsP5bgSupBetB0Jj-uyVz3PX_j_BlxQdzt7XubqVEg5cR8UopDxGWkkmyF0lX2ZXCavctnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آپدیت‌عملکردکلی لئو مسی فوق‌ستاره آرژانتینی 39 ساله فوتبال جهان در کل دوران حرفه ای خود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/25268" target="_blank">📅 12:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25267">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30af4fbd6d.mp4?token=DNNejWz9Fb4l0ZKH0n7LtUzIgokxTcgEWw7bAcJUA21LJLGFUiQ8CpRhHn0GwQHySp8OPZROgT1A0SXf8FYq2KgAZ5MAJeFdDqR6FUbTRsvJqfU4OEnwthVExr5fjsnTFZizW8Mf6mCZ3ggDKFw2_39GgRjXEwwd6kt3DDUkyRMK4uYPDyDroH-M3QHU3s6iFgrsrBn7mdiyJjEwNty3L3-F625PFahKgNwLWCWFvw7ouyMeilcgLCLHQrciNEJkkG9isYPVGLbbRcs1JhQ9KSNoToieBaYIkXTXgs37jOW2oWplvvzqpKfRvvkUQmfNYxvX2gNYlJUqLp3wxz5q8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30af4fbd6d.mp4?token=DNNejWz9Fb4l0ZKH0n7LtUzIgokxTcgEWw7bAcJUA21LJLGFUiQ8CpRhHn0GwQHySp8OPZROgT1A0SXf8FYq2KgAZ5MAJeFdDqR6FUbTRsvJqfU4OEnwthVExr5fjsnTFZizW8Mf6mCZ3ggDKFw2_39GgRjXEwwd6kt3DDUkyRMK4uYPDyDroH-M3QHU3s6iFgrsrBn7mdiyJjEwNty3L3-F625PFahKgNwLWCWFvw7ouyMeilcgLCLHQrciNEJkkG9isYPVGLbbRcs1JhQ9KSNoToieBaYIkXTXgs37jOW2oWplvvzqpKfRvvkUQmfNYxvX2gNYlJUqLp3wxz5q8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
جواب‌ فوق‌ العاده رونالدو به‌ سوال خبرنگاری که گفته بود میتونی‌ اسپانیا رو ببری: من تموم تلاشم رو بکار میبرم تاوجدانم‌راحت باشه حالا هرچی شد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/25267" target="_blank">📅 12:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25266">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nfZ9tplyJ1mETeoQvUgUroHTixplNsXSvQNEI10Gz4OAw0b3dLqSns8eYcBFkIJrObD9zfUUW_MAo3kL6vrAgHx-GiyHMhz1orwftEFG_LWy16zsRxw0LzUlHaZxRa8i0A6gpXDmtNqTWXuBUWSOBvwhemdB1JdCqW9lQUJMEdtl337r0Y18lN8LRibooEPErYlT0VDLyzDZqo1VblPPYnG7n8yemfWjI7h3jIiwJzsl-g1njyuPp3Jw20ZlTl64ZPq2222EEUGerKM1_6JqXWjGxQ6ik8KPOMmk3wWhBpvR8WtJ0fOCeDf_J8tWesXxgdVAGhuHgLA_Q_1gzBo38g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛آمادگی پرسپولیسی‌ها برای‌ پرداخت رضایت نامه قربانی ستاره الوحده.
🔴
باشگاه پرسپولیس ساعاتی‌قبل‌باارسال‌نامه ای به باشگاه الوحده امارات اعلام کرده تا 1.5 میلیون دلار حاضر است برای رضایت نامه محمد قربانی پرداخت کند. اماراتی‌ها 2 میلیون دلاربرای…</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/25266" target="_blank">📅 11:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25265">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HpKAPZOEyXVUV4hoTRx0EB02Uta9CYeSLxECBRUesJdGu5O5gafxBcuQamT6JNVKjH58fAsJUoCYRTErlpFqmtcxbrn3kd4ChPdtZltyJqDe4FNF2o6ermDz8BZip_0vB1YcE41AGGzfXPWVA1w-sXITaFkHhe9VdISmZMkr6K4pmZNKTR92sHx5O_QIN7mEuoGHEKFA90kRA1TKNO-A33LC9AgemBDihr4ngIdcnt-D0onuvBYzxoNuO6T2SBv4IRUD17bgClhLHXaSXVgWoFTrrh3FsqtPCYfswEU1y8gN3EVNBi2D1RChMwYAgRIXphYOXOo0oxFe4GY9fZ2oaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇳🇴
پدر ارلینگ‌هالند ستاره‌نروژی منچسترسیتی: شاید روزی در آینده نچندان دور هالند رو در تیم رئال ببینیم. ممکن است اتفاقات هیجان انگیزی رخ بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25265" target="_blank">📅 11:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25264">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gHR_Fqb47DIDbP4rTrLBCXeQHhfEOyLdiKx9Dp22XqtFgJ1kOyrcl5KmPqiVTy8ISevb-f6IatvQLDBWf4VhdM27q9ETXvwkE4Ax_flE40FNKp6VxnWiC0d2xIRyWDRwyKeb0AAGiCBU_v8lmZGF2sI-zDEzrjQYHZQN6efF7ztv8OlaMUBwm1p3AwXzH-m5SblHfiojVWiaXpP5VkgffVDS0mCP8la6Z9TjlxkaIRmKXC6SjtxPARhEX6-V-kv8WH4EXhqo4IBiozrDgXhkLfqeiGS2HsO_4zoV9rBxug9M-WbZNNfLkf5L80yFu0kTNPtn3XZT4I08Zhq6d9rKqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#اختصاصی_پرشیانا #فوری؛ پیغام‌جدید محمد قربانی به پیمان‌حدادی مدیرعامل باشگاه پرسپولیس: پیشنهاد مالی شما رو پذیرفته‌ام، رضایت نامه ام رو بگیرید روز شنبه قراردادم رو امضا خواهد کرد.
‼️
پیشنهادمالی‌پرسپولیس: سه ساله بوده. سال اول 80، سال دوم 110 و سال سوم 150…</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25264" target="_blank">📅 10:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25263">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94e6448be0.mp4?token=IFUJK6d62xE4t9zbir1_8IXXsQDyyDNKbIP7dUqIiLi0OEisPo_GffxgeoWnrmXIWVhEoZX7VFkhL9Y87bGGvMhTaZ2lRInYU6ziDzTEzvBvnGzoypERThr1oFJC0t4P3gdhMgVrTsqrbh0jY7noNjUspqy8A4w1Dgc01Oq5ngsyvBKgro618uh4umT-W4rlSffircAaU6Bs0HLP6ysE3j0ZdrND3Ux3Ob6WQlxN51WAwwFYHd9_gGJweZVAbmjmSjzdtx-sMPxqfLAEFjWLKWTBJxeATIZJOY2T6iNE90J7zAUnr7Oe3OUXMCdpn1c8vuVXVQdq5fEaRUauug-dzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94e6448be0.mp4?token=IFUJK6d62xE4t9zbir1_8IXXsQDyyDNKbIP7dUqIiLi0OEisPo_GffxgeoWnrmXIWVhEoZX7VFkhL9Y87bGGvMhTaZ2lRInYU6ziDzTEzvBvnGzoypERThr1oFJC0t4P3gdhMgVrTsqrbh0jY7noNjUspqy8A4w1Dgc01Oq5ngsyvBKgro618uh4umT-W4rlSffircAaU6Bs0HLP6ysE3j0ZdrND3Ux3Ob6WQlxN51WAwwFYHd9_gGJweZVAbmjmSjzdtx-sMPxqfLAEFjWLKWTBJxeATIZJOY2T6iNE90J7zAUnr7Oe3OUXMCdpn1c8vuVXVQdq5fEaRUauug-dzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عکس‌خاص‌وعجیب‌وغریب از 18 سالگی جواد خیابانی؛ خیابانی به خداداد میگه تعجب کن ببینم چطوری میشی. زنوزی‌هم به خداداد گفته بعد جام جهانی اول باید یه ماه تو تیمارستان بستریت کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/25263" target="_blank">📅 10:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25262">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UDoVUIfKTO0rPsu6jENYpa-HnZ2FvGEa5_X5WngejC1RZfVj0b7sodqJ5516FintBb-31o61xhs4fBUF9GRSA5KgrDQYVeI_kEMYXRki7cztOzCFtvRfLk4vVmEudz79b6p027LGw2mOtwo8UuqPxuerdjpCUqTrToPBELi2Da_RdnE438Sb_Z2pdiOwgJe2ULOO5b8wny4_rMV-jI184H95iyB5tehML969Fi_rnElYKKkLbwx__1jDZD6BThw_8fu71lZW919IUCte7ZKLrPw4gPUDQAAEmT1cH2YSh5xqRJ20eYk0SZrF1dzB15REoBcr0kPtCTsszgA2sTfBag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نوع‌حکومت در ۱۰ کشور برتر و ۱۰ کشور پایین جهان از نظر شادی و کیفیت زندگی؛ منبع: گزارش جهانی شادی ۲۰۲۴ و شاخص کیفیت زندگی ۲۰۲۴
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/25262" target="_blank">📅 10:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25261">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hrcmEUZtBBnRiz0nHcT_ZPWp5Vry3-bNy9Uppz-kApcBDMUjGVCXPUGPJwH18hOJaWy88NjRng1u-ue-CbWvsnm1UwfkUTm4HSw8sR7Q49JSexXXtoW9rNbbbq6pgtoT_qZLwws1WWrGVK1cQeeZNOP7BNanKvDeIetNltCFndrLFmOX6M2UiTTP9ym8WBEjZYzCACHCRh8MmYZfd4Z4p40dtQuXT_X_kqOS3vvplkmg9IFR4hRIIG0ya_9JS2qcZ2klb7u2G2y4Ao2EbQLrl61AqB_oQEN-SGx3UvqMPjQPgwUwn7z8fazKH_9DX_8fma_WtyY2ednQHw20waJ9nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویدیو لو رفته از کلاس‌درس‌محرمانه امیر قلعه نویی برای سرمربیان آلمان، هلند، ژاپن و برزیل در خانه‌اش بعد از حذف این تیم‌ها از جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/25261" target="_blank">📅 10:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25260">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qrRvqjhhupZnjCBuF3zO7busP4_LB62Wh8nxFsu1UIrvwjhYqsqOAF4wvPZrLz-ic0xMEoboNU7WRAbq1uanlYysj6CeUPBXyv6QqJ9l-MxmBVCe-3tw0M213r1T03nBNw7yxnrn3E7hz4v06aGysO1XdYm6-4kD-LQ_WcHTdZaYmIhIBSh_RUTE_N8SclO64s_FPN5-jx4e-mvuMwzzUnLJoETBouVpAe0Vr1s8q2xpuCh_Tckbvidy5qk49okcR2rXwos1avMdEDhI4VuhtH_XQu3vfTKnBXRtjUhaNLh-F0uNDyLBOelfcoCslOwCffRmiqdXU20StbP2eYMj2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
تصویری دیدنی از لئو مسی هنگام زدن کرنر دربازی شب‌گذشته آرژانتین مقابل مصر؛ آلبی سلسته شب گذشته با جادوی اعجوبه آرژانتینی خود سه بر دو از سد یاران محمد صلاح در مصر گذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25260" target="_blank">📅 10:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25259">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jCKWmM5l-V8QaPkW9wdoEIWeiuxqn16EA7cr9VwovATNsrhdd2ebB_rq5zd4QwBs6yBd2Y9dgUPfKc3cLywvD7igAR10QM4zaLQOASf19bLSmWfaZ0bhywKPcZhbAJIU8ZZGlFYHKl5r41wQ2l1P-tnXjFy7qoUiA7A7RB_9YcKUcdlhkDCkELz6_zQrPnvY5OXM8m4ov51vNGoYAwlezl2tBbcpV7KuyhgBUnsleIXh8M221RFrHw-XDJ8bU8-jDEUjy16eKaE_sdxlwc8fxzLJEemFVG8Zkqw080fj-kgYw0WZYTE8hHzXKn2D6ZQgk6PZys1zj8z0sntJXJP4yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ علی نعمتی مدافع‌ ملی‌پوش سابق باشگاه فولاد برای عقد قراردادی دوساله‌باپرسپولیس خواستار دریافت مبلغ سالانه 75 میلیاردتومان‌‌شده‌است. درصورتی‌که بانک شهر با این رقم موافقت کند به زودی پوستر رونمایی از مدافع جدید سرخ‌ها…</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25259" target="_blank">📅 09:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25258">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L_4Ubqn6nzPIf2-tXcriSpNeQdVtvN7VQn_9mU-Cag9Jl4AVLuoAwvDjH5bwjWC_csswBnZ966LplEmSaWgBDXP2ehcNJcssgJop56yY62dfIx8m0UXsQoPBRjLBt-5L-CM049Rrh4Q3NSwZTpp04QzwWDlTuNCCvofTwLDVtv9nCjkEEzEPL72YKq7MlvSna8CchSKP30e2vEFyqbZLIVMGewBF4z6X9y5IMo4nB9qtHut2S4BSud6kqBwcVfTDk7VzO8I3WwF1ZWEFgKS7DELHmpCJAoV49Ytdl7hS9HGPfE8KduzD9IdjdPr_Do83fKE7j3s7ercbwshp6KiTWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه کامل و دقیق مسابقات مرحله یک چهارم نهایی رقابت های جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/25258" target="_blank">📅 09:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25257">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LxcGEXfl-NM-Rej1VWf-5-I7SRbl6ohZpDnD0hc1kOQuQ_R16GeaewSif3ooYJxK6sYNtYutPLvcF0rHoATg1PSELVvIsi1aIR7-nNacVAgEMxf6zY67XytpA6vIrujzOuxLeli25IsDC5pRadc-PV5_PyV3Fuos8z73EyQcaqaQmZy-giaNqNamtxpMbMclox3VTRAlKuEjQV_9ixPNZ403wIK3SKzK3IDKdFDX3jXOgRhWEZr_gSBKwrK_KaO0EI00oxdQQnKavRcMPJr47vDX0SzSgLHUzOdg2_bH-D1y0UJk5-0jzk0rNdIvJ_yzHXXyAq5FtZUZZ1CNo6eA_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ آنتونیو آدان،عارف‌غلامی،آرمین‌سهرابیان، محمد رضا آزادی چهار بازیکنی هستندکه سهراب بختیاری‌زاده به مدیریت باشگاه استقلال اعلام‌کرده درصورتیکه حتی پنجره نقل و انتقالاتی آبی‌ها باز نشود باز هم نیازی به حضور این‌ها ندارد.…</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/25257" target="_blank">📅 09:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25256">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PKWHQRcsvA_w4WOKM4J0cujP-tz2n2wylma1inyzu8IFRTjMmL1-28osxoOaZrMqL35rWvln8KGzurAkutnho_8l_QIhO7_j9xIUk-ZUspCFJEfG-PWJzburHX8GOvyo-tXYElwskSh3dWs09pwIHbcjAOG4S3ONtrezMfbtWihXNX4L6G-Y_B_VPsXL0icosLf06U2j_rtriIgCGIx9Q8zNSxzdiGygHvGQvGnTA4CQnP5QRGlpRyryHJC-rMaJwqi6xDI0eIFkaxExpMVLRv9NZHvRUcmy55IGa0IHgzS4HO9RRJPWvdkv8VDuSIsog6q-4Gh1Ar8sWUM_oa5aEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدشد؛ باصلاحدید کادرفنی استقلال؛ آرمین سهرابیان دیگر مدافع میانی استقلال در لیست مازاد آبی‌ ها قرار گرفته و بزودی از جمع شاگردان سهراب بختیاری زاده جدا خواهد شد. پیش تر عارف غلامی نیز در لیست خروج استقلالی‌ها قرار گرفته بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/25256" target="_blank">📅 09:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25255">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8869652ba6.mp4?token=u9dUS-qIm9YpYUl4Fyec2HAabKg5vfuhM5hVLsDLp_FguthSYzR5CsplFtFJqG81sRhqy-Pso2K1dgiOX8-4BiwMX1HE1gQJfgwY-EaDEXKVc39cjjm8tT2eLL8qehOMXLivhqrFGOxCKyXhSuhNjeFgBoq2519Sk0o6CbyPwhQ3KnFs7HYn36oGej3VK5sljNdqo631CYdI9VLaH5vfzgmbpzsACzTfAUZizHlLozgmHvis9TZd3eovVbrCOZG9keHp3NT5wQJkiT2pZ4_ehgYec0MxThijVZMkKnGuhJOpS7svCvlnOOZxLc0iVQmSkFQ-tCfDwCOlGUOH3pltCQ5rtpXx21cno3rGGPnlJqyCdKYzBaIWwwuqgzdVdNbwRRZ6I_12BSb4VZntfjBye8GUYRXd5luo-KoOtl2HCtu2Xjej4UM50UyRaG-3v-ySAd7IyoPYTFYjfNefiJxsKxR_BWVrfTN-qu113a11npLvJjbogKbijFRIygwKyiIZNrlvu63LCrYJxgU-TC0xx7As9b6_kmMBNt4fbLomsE_npmghOh1E8aq4pe9PnClEOzLiNMTCv6u5_ZYlWns8Qqhq0QNhN_vN8Xby6q5baAhFUj2-9qIW6n7ucPwTNEwFz4FdxX8pK_AoZcsTF6qe_J4BZTLUe4BehBee03cioS4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8869652ba6.mp4?token=u9dUS-qIm9YpYUl4Fyec2HAabKg5vfuhM5hVLsDLp_FguthSYzR5CsplFtFJqG81sRhqy-Pso2K1dgiOX8-4BiwMX1HE1gQJfgwY-EaDEXKVc39cjjm8tT2eLL8qehOMXLivhqrFGOxCKyXhSuhNjeFgBoq2519Sk0o6CbyPwhQ3KnFs7HYn36oGej3VK5sljNdqo631CYdI9VLaH5vfzgmbpzsACzTfAUZizHlLozgmHvis9TZd3eovVbrCOZG9keHp3NT5wQJkiT2pZ4_ehgYec0MxThijVZMkKnGuhJOpS7svCvlnOOZxLc0iVQmSkFQ-tCfDwCOlGUOH3pltCQ5rtpXx21cno3rGGPnlJqyCdKYzBaIWwwuqgzdVdNbwRRZ6I_12BSb4VZntfjBye8GUYRXd5luo-KoOtl2HCtu2Xjej4UM50UyRaG-3v-ySAd7IyoPYTFYjfNefiJxsKxR_BWVrfTN-qu113a11npLvJjbogKbijFRIygwKyiIZNrlvu63LCrYJxgU-TC0xx7As9b6_kmMBNt4fbLomsE_npmghOh1E8aq4pe9PnClEOzLiNMTCv6u5_ZYlWns8Qqhq0QNhN_vN8Xby6q5baAhFUj2-9qIW6n7ucPwTNEwFz4FdxX8pK_AoZcsTF6qe_J4BZTLUe4BehBee03cioS4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
علی رضا فغانی:
دوست داشتم هرجا داری کنم نماینده ایران باشم اماخودشون‌گفتن ما نمیخوایمت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/25255" target="_blank">📅 08:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25253">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b2VXYQxCl2WijCJQz_KN8nylJtyMEjzOYw-FH7Trmlf2SqDUOxijtQmzIGXSQMbYttssl0w82qMvVzfYIDy6mLLte8amI97VjaXZmfvawDhvHg1AoLi1tW8PFtuPOEFU0LCuHSkinhvpgLUdtzZTTRVagcHKJqKzj8fAJB8gmziOkh9lw1vS-M-yzWH0Q8smb2U3csoDB2t7mDO-AZhVOuQWNy5cS_GjJ23vxrm7PW-EBbXeXSMfLiUyjro2m44AZIDy8sJTegt6X53LePi9PdmO_nMky8TqkpenH7q_LeQwQF7da-mztn8dJhS-7OchaI1_0EzPMOYCHrGttUUjgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تنها دیدار مهم امشب؛ آغاز مرحله حساس یک‌ چهارم نهایی بارویارویی‌مجدد فرانسه و مراکش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/25253" target="_blank">📅 08:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25252">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZzMMuhvEyfyk1eumEB20e8-kBF3-hSbJcBg65sCSZXXeCdCzf63MEZFHwtWqrvpAchJjrOyj_iilXqRTIZXSr14GtRdO0sB3H7OdSEmLK_uKJbF2Ho4pPTIN0VXPFUkcUkhDgBlC-Jx2JflEgkPiiXqQmU0mktxlnwTfliykgrDYng2KwJFPXWJ5_gGH2PEJfjA3gzCK3ZxAJeQCNu-V1hEjhRFOOrEJL_n28iGV-1QjrmNvNiM2RuhLu87llM4JrjDAEFKtb17g5paWVXV3JKGAg_tzDWH7uuUwHU92-c407EIUB_BBOftCV4vcJWNCqN7eMLziAGnY1Qg5aV4n0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
جرارد رومرو: ممکنه‌ طی‌ روزهای آینده کریم آدیمی ستاره جوان دورتموند با عقد قراردادی 5 ساله به بارسلونا بپیوندد. مذاکرات مثبتی صورت کرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/25252" target="_blank">📅 01:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25251">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f7uww2OfPTqHGyb-9_WTsYiBdIEkZw9zwQ1tn4fo-5BsoJIhfPBAUTmS1FNySj7PxxWhi7cWpQeNHSr1Ko2ZxQduIlywrIEHTYAMkSq_BEAt-mRXsSvdnQmEKTEMxEeZH7Y8bxQW-A0qpyb7thxIkOgphqxx3pUbUzy9_XDmsu82RZYpm0uidyd13GwwAetpS6H9WSybM-JjRfTNGRxDYdMUY_NEt7VimN0fWEr-s7wDpcdfFeMxcrDeYSx_2bieizCFNgGa4wrmipuwljONx29cm2zs7-4nSTZBlXaQ8NNKayuvcVVC0Tb_Gqm-GcGVw_6aC5ESVjolaN_vQ9J6JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇩🇪
نشریه‌بیلد: کریم آدیمی ستاره 23 ساله تیم دورتموند به مدیران این باشگاه اعلام کرده که قصد داره از این تیم جدا بشه. منچستریونایتد و بارسلونا به شدت دنبال این ستاره آلمانی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/25251" target="_blank">📅 01:45 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25250">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6798637471.mp4?token=L-bHw4Db_m247EMsX0_sZ0w-E4jgXs-iU_rn6GNxcRQSi186ZIIN9lHR3_aF82nArPjSmRju9KaY6__quzLzNLyXiRUeaBBuv4AjwgbsNSrtqz1U9MYSC-3wdYenahRbCS8t71_g4HcT4mP6UMXXAvXTvEEidXVsWcsiIUcK-gT4zboGJ809TsKTqtE6KMzs32CpBgN5LSluV3xykAbLSCYUWXiIWsUJK_ONkfirKHwKb3U-j36xU93RelZdS0b9rdw5k9FmV3M4rSNatDRT3RQYepS9ckhwqE1QERLDWuSPDa_QvMc_IsG9TvCbwvYrkOZnBxGlOY0Et9YDvGgg-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6798637471.mp4?token=L-bHw4Db_m247EMsX0_sZ0w-E4jgXs-iU_rn6GNxcRQSi186ZIIN9lHR3_aF82nArPjSmRju9KaY6__quzLzNLyXiRUeaBBuv4AjwgbsNSrtqz1U9MYSC-3wdYenahRbCS8t71_g4HcT4mP6UMXXAvXTvEEidXVsWcsiIUcK-gT4zboGJ809TsKTqtE6KMzs32CpBgN5LSluV3xykAbLSCYUWXiIWsUJK_ONkfirKHwKb3U-j36xU93RelZdS0b9rdw5k9FmV3M4rSNatDRT3RQYepS9ckhwqE1QERLDWuSPDa_QvMc_IsG9TvCbwvYrkOZnBxGlOY0Et9YDvGgg-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جوادخیابانی‌ تو ویژه‌ برنامه‌امشب جمله معروف
"گشتم نبود نگرد نیست رو گفت" خداداد هنگ کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/25250" target="_blank">📅 01:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25249">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QNDFIS8cmtzE1tX4rPcjp4h7IOD0S3dEkd7bRGO3ic80j4dYhRBBPzYkSEhADvd4GZZc5-sYTp18dIRgZB0x3NcqPraEcHL-xhCoaPipoqU3Zk95JH2XvvAkobxsv0kMXliv0uVNUvo1R6uq4e2l3A-lE0yjufV_PEOshCZTtGsVsyd6g4BvmCsuWSKlt9WupIkhHKNzJ56_shad9E0DOf8-HlYT0Quz84Oe3XjfFtWC4gdX5M8_aUJ4AqPEj9sW5bp4Ry2yCZMrIDHWHdG-bVx41JRADtd0RYL9SxkMxWq0Y0saKY3p-UhyIIgjCUVUase77qjtk2SBQccubRJIvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
خوزه‌فلیکس‌دیاز:باشگاه‌منچستریونایتد برای‌ جذب‌اورلین شوامنی هافبک26 ساله تیم ملی فرانسه به باشگاه‌رئال‌مادرید نامه زد. کهکشانی‌ها برای فروش شوامنی ملی پوش 100 میلیون یورو میخواهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/25249" target="_blank">📅 01:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25248">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rAfH2YM_o0JfztiZ4lYhmi0grRk04bTJw86d0UbogtlG1jWqodtV_AEasjaJAvkGWk9vigb_gI7Q53EO0-Wkq7iaPP9ZY15ychDkx9H6Oxs2qr0pRpbftpyg_mha11VjzUCIwn7O8i8S7mQAtZ59n-l06AZFR7Yze8mEvcf-BtGmK7eQTq9hxTxiTMwxQYYzWyxdBImxVchsLGWmZwNEDZoYtGFC_lTxoVJ6je-90RmygEfh_MMWRObWbD1mfZwE1bDJ6WA6oxQ7A9SPW4Ghr3f-VqE3DDK8iCOOTrUmSw0ib0F5WUMGSZEf6f_aJCW0tjbzAz_C_zoy1hpA2MEe9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تنها دیدار مهم امشب؛
آغاز مرحله حساس یک‌ چهارم نهایی بارویارویی‌مجدد فرانسه و مراکش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/25248" target="_blank">📅 00:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25247">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E3rMW3qMbaSwNxXoJAjr3poutJk7UxOF3He0vCm0M5edyC0FIL7kqGTK_hgtw7oaCt8eAcgCV2PbVNOeItqs4S1SXUgSOKyNUdTz3hjCyprvmRhJVi1yNdczNKUMQ8hIhWLWLC1Mc4YoyyjtSELrhUAUs0AKzfp7jXyTZw1KO-RXOoVbaaiuoxY9uJNFhd1CA40tnEEIi_Tt5vQA_TOAn6lKVppEHHzXjGUmzaf9egtjh5O3NUKrJJWd8sW-w1S3tIjSjWX48XBWoEJ8Nlmw5XSg9_xS8Fq6zqPDungZNgvwDHykv1gohz7-DRNBJHFT4Up_qYTxUbm3ikon5c-uPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عکس‌هایی‌که از وضعيت امشب بوشهر داره دست به دست میشه: یکی به این ترامپ احمق بگه هنوزجام‌جهانی‌تموم‌نشده دهنت سرویس.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/25247" target="_blank">📅 00:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25246">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OtB8ikIgbvmj3m2OsGAQ3uKOwgveddlRD76Mb_qAJK7CvBkJdd0XHVYwACvC58leDWggpwWWEn5cDFWr7z9rawTgKMjbMbTRErxDJrsX-_mAXfAoNVK9Y8bKVhkSn4zdZPmqQnetfeX_eOSNjmV0TA2X9b8MCcICr351ZbPgYM_943UR4JNBHUym4ZswRYf_2PdStqbSUyFkryf3w1jOcfiVmjLv3Op2SpKvCav7Ad6WchVf-383qT530CqAKtt2s8KNf5gSF9FGAzwh4b_ktLpGzJ0_5Q2FZk9V8dDJwzij3eUjDH6IStrPK1miGBpvB2ZNDDNEoumlK_sTeW1N2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه دهوک عراق بعداز جذب سینا اسدبیگی؛ حالا محمدرضا سلیمانی مهاجم فصل گذشته فولاد خوزستان هم با قراردادی دو ساله جذب کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/25246" target="_blank">📅 00:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25245">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GzSetNqlWmyygCbhuWiXYkUqSYsrXL4RnZs79SmhFHXa7UsyQXqOw3l5lhChpOHUwdVNHH94enwRLB7klo0eZqON30pkj3WiP5CAh2qH6-9j4K7YofGsfuAuDXxobPQtzFBWl0GR2bouMZbD5sl_AW2ndZQobgU-LQJ266NAiJtfzRyV-9ONdtKgSeXnS1CaF4lmr_zF8DonPt7JTGToOQYQb75fpweyMtSwKsQ720Lq92s2dSRfbAlX4h4jKgUOg9PWw80rZkDG7kTDoMeFwLpdC3LOXOEpsa5l69mEIE8pjscIDRqjNMsnIP_kl54uPDyNqVxTG8xZzKNDb8R7Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اگه نیمار جونیور روهم به عکس اضافه کنیم؛ چهار نفرازکسایی‌که فوتبال روبشدت برامون قشنگ تر کردن. کسایی که روزای قشنگی واسمون ساختن. کسایی‌که اسطورمون‌بودن رفتند، اونم برای همیشه؛ آقای‌مسی لطفاشما تا ته این مسیرو برو. بارها گفتیم که‌هم‌مسی‌هم رونالدو بشدت برامون…</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/25245" target="_blank">📅 23:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25244">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ppEmzxU3c0ae5yjZRxgNcUj3nkxHUkxnDDo5XR8mjcXey8ZykSuqMdSAus5H8dXJkb3jjVxAkJz9zl1-mJMYujak69Qzl1Np03SAariZsQpvxmEtq8qj4fyI5R9T0k4qOsM4oGWYlYYGkgfmcX66h1pKHYKwWfJM3EVo6GC4sZDo4LPpDeU_3X_LCYkITUKkFSci8f6Ijxz0hC7ozfiOYZAxJNYslX7OXK2skM8Xmlr-NKK8caq12wfQtrYDuHLMNtwUCFvLKI5zc0LjTf6ihu9dZGtpUZj1A9V1hNTC0bZZuJ1_kx0h2-YLaBtMii-ljnNM5lzjtAgD8CLpNbCi_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🔵
#اختصاصی_پرشیانا #فوری؛ مدیریت باشگاه‌سپاهان‌برای‌جذب‌قطعی‌سامان تورانیان مدافع راست آبی‌ها به باشگاه استقلال نامه زده. با توجه به اینکه‌باشگاه‌استقلال‌تمایل به‌جذب امید نورافکن داره و مذاکرات‌مثبتی با او نیزصورت‌گرفته درصورت باز شدن‌پنجره آبی ها این معاوضه…</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/25244" target="_blank">📅 23:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25243">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gL1zCPIcj0b_RdAuI_gnqXMvPEWdst_m3xt35eCtQDVNTzcAKEFyZw2T1HMzK8tnHoSMhzvErb6RNeMv5d9vOGgVhYvpomMPWvt_5Vp4WCPGcU3-Y6x-gAYPQNxiuNImPbUhE72m2D8NGkk56Ls6M4xek8VEyj7MQqgimEUfLOqzxqoSogXEmyyttAzda0AYJ7Mlf04Y5MpXMvI4Csgmz2hcr3_bPMxLzVYlz5ef726cr90dWYo9epx8IqFua9XSsAR9XzMtBRwVU-jfnYDe7Me1pREbGmjQ4RhTEPxEY76u7raiEsIdsj2y0TvxJQfLkTU_h3cyRLFPA07aStyC9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
تصویری دیدنی از لئو مسی هنگام زدن کرنر دربازی شب‌گذشته آرژانتین مقابل مصر؛ آلبی سلسته شب گذشته با جادوی اعجوبه آرژانتینی خود سه بر دو از سد یاران محمد صلاح در مصر گذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/25243" target="_blank">📅 22:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25241">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PsJEkheaFqNxSimG7kLCSq29xCzhkDsf46J2gVkVmU4hQk-2vd3Eh5tNKbquVRdAAUe2gkTd1F5XUSzMFX4sDeUCx1uuoLFOWs2VVwwfOCmKBD3ESG6ErChLdw4ugV8BCPI22WLSZ3nfM1onC91W-wyZyLvif7AtCYHmChWRl9J3AQOc10NzFmlcIcI7J0bm2tyF_VC35fMk2cmVZbMn_WdKFIa25qZ1kj6ZPUYUc2S5WYTvFEWmsRsp8MN2JwfOvcMmrv56ZPPKtJZr-3OiF973CIfq-DE_Wn-A_3qP8iVdWOIcftaHeSAM4I8TFcVX5ABddsGWQEsRPcG30Paoog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZN9YCKYrOmWPYOlrRajRW1XHcNP4wIGUNAGH9UUcbZjiTzEpMq16WQYEV1Cb_SbtQnkLbRFf6SFz5KG3dwOVDGI-BA9B4JPYFyU1d3FDdRj3KeEtu6JXUEaDOTqvxZPKLYppwvEhei_NCCxk8Ia06MhzKyxbFfvPsVTY299dvDY_PAfzwTHcz-NFFcaDfF-du_6soONF2JgGp7DO8Vr1vQrpnvf9RErkj44bW5G1kGuf6nowx80Opib-6Kt2RQL3euljGlgMlVPqw6S13qb1JnXvrBrM08Y_UFWbd8ZDoKCKegxNZgElIS1ZatkbUbXRQWZH-ClGtzO6BIqkCmXJDA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🤩
مجری شبکه رسمی باشگاه رئال مادرید که مدعیه‌کار انتقال انزو فرناندز به این‌تیم تموم شده و بلافاصله بعدازاتمام‌جام‌جهانی2026 انزو کهکشانی میشود. گفته با انزو در ارتباطه و انزو گفته به زودی به رئال مادرید خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/25241" target="_blank">📅 22:20 · 17 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
