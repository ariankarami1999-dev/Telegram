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
<img src="https://cdn4.telesco.pe/file/t3KQqeGcR1_NBhvsWyql0PxRp4R6cuLImz-ePVi3w5nAE6lI0HTwIzLtLF_xmnkYU_BKmCQv87m9cjyrrGBecsx4f7ZZ1xVEbtjMOEo8QmKbnHCKmAV-DxyR6hnKLGCnhg_F6Fz45jC1LIhjTa0mPdqE96nW64kdmmfWimTLvK5DYvZK2pe2yppFGKxOkSSJRGx_P5usGmfeMejkRYhWAJH9nlCMoO39sxsQrTOoQsvXl_q62ZYqa_AU8XIUe8E5HwzSxQC8EaXd65XErPIxoRnoqVYSvBq5h6SQo_xAv6sKtDwhwliZU9QvSWfATF2sXboDBNixC14FErCt8seHhg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 950K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-02 03:38:14</div>
<hr>

<div class="tg-post" id="msg-129801">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبارفوری مذاکره | مذاکرات ایران امریکا</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qdMPO5m14LRUHCVhF-DPxDD5IV9CUjwgVWRW5VcZdsG6J3Q1VbF7bfqkMLPRuxmVK6Bb4zjGtr_i0DWpBfvpIbBP2Y85bugPzSY0SddhY_0faEByJqMebUooWIQFZnyZpDIds-Qt1HACjnEvp7EAfiQQlRaWc1wJ175YcHRviUQh82PRGspkBYP9fYj60_4EJCGGRL5ni6K2U0pkhMYp03mUcy8pK3pXdAcvGQ1SOpHzlyNbItZfsbBN7BxBKSyMBy-fRkbhgpQa3RtY8925Papy7om7kKK8XJTL-l6cPjgVrBo_pqIx9udcjKZskKmFJ6-MOcK2jUD90pyVCCxHVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
📈
بازار می‌ریزد؛ اما
آربیتراژ
متوقف نمی‌شود
وقتی معامله‌گران از ریزش بازار ضرر می‌کنند، ربات هوشمند اطلس اختلاف قیمت بین صرافی‌ها را به فرصت سود تبدیل می‌کند.
✅
برداشت سود روزانه
✅
گزارش لحظه ای معاملات آربیتراژ
✅
شروع سرمایه‌گذاری از ۵ دلار
✅
بدون نیاز به دانش ترید
🚀
مشاهده عملکرد اطلس:
@AtlasSmartBot
اطلاعات بیشتر در کانال تلگرام</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/129801" target="_blank">📅 01:31 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129800">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UxU-TmEIw4VRdBgu5_UidhYnZA2vl_YXKqgfwwHcLEy_jquGacUGpAFS54aLuY_yIhJ7bTvQ7i3PLLNTBTW-MXxw4hM5VQH839z17C5RRg-ILrni37Ne2hbx3_9PzkLIrL3hraZStYwcOtJTh9w3liJklaqhecgnrhPOk4M_ZLJhAuUlotBzQGTqZc6Zt9dsj3imbleCFMYCsalJGNiLwmYQweqBQhLf4BOfNX2W34qIYX84hUclI1sMh3yfTG4pKBkxUHWd3KZWFANC59fYqYOXfRyzHWGY8ElYnd8noCYY2ifHQ8thDJ4aM-iN16LKXNR2r3gnYH4R0COuBtIqqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عماد الدین باقی: طبق بند 2 توافق ایران و آمریکا، از این به بعد شعار مرگ بر آمریکا یا سوزاندن پرچم این کشور و لگد کردنش تو مراسم‌ها و اجتماعات رسمی (مثل نماز جمعه) ممنوعه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/alonews/129800" target="_blank">📅 01:17 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129799">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
وزیر خارجه عمان: به قانون بین‌المللی و تضمین عبور امن و بدون اخذ عوارض از تنگه هرمز  پایبندیم. به مذاکره‌کنندگان ایرانی بر تعهد خود به قانون بین‌المللی در ارتباط با تنگه هرمز، تاکید کردیم. مذاکرات سازنده‌ای با قالیباف و عراقچی درباره یادداشت تفاهم انجام دادیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/alonews/129799" target="_blank">📅 01:09 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129798">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jAZixioSL5fSCXY_YrNBDJSPdgWq2CUCO83iVTDRSRwJN38wS09u_toRkOjK0Ilazm6KkZgH7V1HQm5W4YLCoj0UQMhoV_BRSkVuSAPbxp91On9NhKYGDvRNRc-j5ACrHF6Tm5Vlhs4nul6DVewwJ3SB0HT3BENZCT3RxBSNtfwCRlH7fa6J0xKBOgXDV2fXUQpqOfeVSduUP4trWWLQj-TOPoKeXBCTt9F5SAUEL7uUBHBirVtW_TiLJye1ANzUZJwjtG_20Cdby_XS5NrGeV_IcUEmpGOwAX3702E5TepPE0mnyL8wmDuC_jlReh_muB8zR642CXh9g-m47Owo_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
چند روز دیگه
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/alonews/129798" target="_blank">📅 01:05 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129796">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
گویا علاوه بر سویا و گندم، قرار است سیب زمینی دشت مغان هم از آمریکا خریداری بشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/alonews/129796" target="_blank">📅 00:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129794">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f3WswkqEYdpVeE9YDg_lxzSgdscLWtdCXB2ItpEaBYR53BwCv1LA3qcODtOsPLliB05BsT4rPPtju5pUfQTYbkDvZ0i3O7fZ97C5TJXF_p23mx7teaairAjxPOL069OHOPQvWEtZgPy130m_xMvRWZq-k0NeQNJQvtMnNPv1zN2Y5pvVy12G6Q7mwbDl7u6E06lAJ8gL-O-SA1zasZJLIqQEja7LLdWxwwGNr5EC9u4Fma_0YOO6NkV4TeB55KJgwbMB6ptcKdxLIxNC1mQBl6BmDfiAPbQncbNlo0NlHqzIF2xwfkk0CJaJK9REIyr4VPOzYz1JQouoabhIg7H58Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vlAXTTexYnqmyPV6Vb6zcVVl8hQlaWlc5AB6w5f57Ackayh3WE5W0eN7sC6QJCxXaeJbw9mj8p0HTtNViKQyMBWzBqA6w0FOMNW30dHLO56fOOs8a0Lo0MoAZeudOg-vSrGSDqfpZ16aDiOFTep1YKbFhcpDeLJlaA2zy3-w0_o4wi_Pvt62bXNm7Z7g58YICxO6RHEYU9lgNXryMkC1KVojtMfbKzvNrdNJt8mxX6-LkwhUPc5OCQV4nYFbNxlcrfWBMjkMnnEC8o2nsUt2B3lXPaeCZ0c5qvnZGZ6c_EPzKDZNHAEbzqTL4yhuT1shMyCz36NdsZZinEdez4503A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ایران صاحب پیرترین ترکیب تاریخ جام جهانی شد
!
تیم ملی ایران در دیدار مقابل بلژیک با میانگین سنی ۳۲.۵ سال، پیرترین ترکیب اصلی تاریخ جام‌های جهانی را به میدان فرستاد و رکوردی تاریخی را به نام خود ثبت کرد.
@AloSport</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/129794" target="_blank">📅 00:45 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129793">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
یکی نفت رو میگیره بجاش سنگ پا و سوزن نخ کن میده یکی هم پولا نمیده و بجاش سویا میده
🔴
دیس ایز ایسلامیک ریپابلیک آو ایران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/alonews/129793" target="_blank">📅 00:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129792">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11e0b59223.mp4?token=ewA3AM7OO_HdZJztuOqU3hAtfsTCsvi03vkxl6CBA7pxq4I_FxBo1PoJ0TXWUEzaNHoy38t6aQHn9d_DkupE-UTE0MUVbBkpcMrT3NIsrCrj1B7E-QeznFD4-MiLOHqwPL5i4ssdW8XJoXrIfpJOB1HhHVdvrj5--yP6sh9cmBAks959GD-2yDMT0Nav9VWPx8drMciHRSdLVjOCBRmh6nGO5zObWN_jK3yTCit8brL2CDp43gsItBDn8QjgHkhjBhSKPh26Sb91hneK-II7gOM6uamrcdYeMdsF4_EGABZ_kPhylypspqYfsJW_EewJZkjXzRhN06CmqtPW5eiisg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11e0b59223.mp4?token=ewA3AM7OO_HdZJztuOqU3hAtfsTCsvi03vkxl6CBA7pxq4I_FxBo1PoJ0TXWUEzaNHoy38t6aQHn9d_DkupE-UTE0MUVbBkpcMrT3NIsrCrj1B7E-QeznFD4-MiLOHqwPL5i4ssdW8XJoXrIfpJOB1HhHVdvrj5--yP6sh9cmBAks959GD-2yDMT0Nav9VWPx8drMciHRSdLVjOCBRmh6nGO5zObWN_jK3yTCit8brL2CDp43gsItBDn8QjgHkhjBhSKPh26Sb91hneK-II7gOM6uamrcdYeMdsF4_EGABZ_kPhylypspqYfsJW_EewJZkjXzRhN06CmqtPW5eiisg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قالیباف و تیم مذاکره‌کننده وقتی ۱۲میلیارد دلار رو میدن تا از آمریکایی‌ها سویا و گندم بخرن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/129792" target="_blank">📅 00:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129791">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frommorteza</strong></div>
<div class="tg-text">داداش حساب کردم پشمات میریزه .نفری ۷۰ کیلو غلات میرسه بهمون</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/alonews/129791" target="_blank">📅 00:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129790">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HiLzPbwgzvcLKJge2sV3cnImQsFzMF9yuVloKrTguMkAQuCLb6GOaWjkBlDdEYJbkGcydehglT066Ti1eHsdMm2P1oBJ_YW-i6iqCbOscGH1EhOel9oRb5K_D_6aVEjl-apj7OFanKqLiqfK0y3Zaa82gbfoYcjKAgTu9mb6A0P2FBCUAKDzLFD3hHA26XMhMrvV1glHE_iamr2lrIGKFOHivgzFo-Fdem2RaKJ6cd2DMkVrI1e68UJNxq1QczYccWep7Z9zmTjmPHHQylMG61ZqolBRgvvrgX4b9JzsBobjXFbXGIOKea3fpU3gpqmehd3GPlNRJXsp3XPVct7Guw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
همتی: اگه آمریکایی‌ها قیمت سویا و نهاده‌ها رو خوب بگن ازشون میخریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/alonews/129790" target="_blank">📅 00:28 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129789">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oroXI2XkcOMktPzp2i5SKH_Fq6OPKzWeNpyV_DN9tIK2vtCRvvxtwrwLqSj3GsNlkul2nPCms3a9kyOIYtI6Vv3T20NhHm5-AwwhDNmpjrQTgkMAuESniTEKcfaxoT_H3mW_wAZ50XotnjP_uV-j7gDh53am0X5vMZV4FJwRPG3OeqW2UDCgXons5YrNXUFG_Y44_8NfxLASTH1gI2rFLjR48ISSbj9TpyGTenRLTu3Qy8sNmjTbDf5UFfjwC0-jLJsgKFAhGEzSd49M83cc3Iy2KR6uv17yp9WdULriJQnpFGkxVaPAFxATFuaSRBbiS_2D-XtIpdh8aihLuod7rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عوستاد خوش چشم:
هر پولی بیاد ما موشک میسازیم تا اسرائیل رو نابود کنیم و به آرزومون برسیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/alonews/129789" target="_blank">📅 00:24 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129788">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sG2d5pNA8TmMkXW77gOhx1iw3LMTkfFQpTYMfnTBn2AveOoKQNNEFOImDibk6fmJVoJIK4eKtFkCcAFzi72ndWI6K-weHSeamzIVBz5aOD4994LtJNmjVd_Fy_pkg8DoMC1vX2xZQGc2KtSJgTU-R-2dy0uXripOOev6r5CNsvz_DIID13rhyyUeeq7VwkGDzSaDtPtEpmz2d7MNL0arlT1E2o_lRRm9zCAbEJtjQvQ_MSO_54emrOiXycN5IO54dMFPGQA2VIazbSG8qrmMZ0L43L7v_osT8burDgh6nUJKFwoPBWoRouzE7gG9O-W86IXh4ccY5QpGAj-xn87yoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف: با آمریکایی‌ها عکس نمیگیریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/alonews/129788" target="_blank">📅 00:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129787">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
خبرنگار : سالگرد عملیات جکش نیمه شب هست، اگه برگردید عقب، چیزی رو عوض می‌کنید؟
🔴
ترامپ : نه، هیچ چیز
این موفق‌ترین حمله‌ای بود که کسی تا حالا با بمب‌افکن دیده؛ کاملاً توان هسته‌ای‌شون رو از بین برد
🔴
اگه اون کار رو نمی‌کردیم، الان اسرائیل وجود نداشت و بخش زیادی از خاورمیانه هم از بین رفته بود
🔴
اونا فقط دو هفته با ساخت سلاح هسته‌ای فاصله داشتن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/alonews/129787" target="_blank">📅 00:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129786">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
رئیس‌جمهور ترامپ درباره ناتو و ایران:
ایتالیا خیلی بد بود. آلمان خیلی بد بود. ناتو برای ما نبود.
ما سالانه صدها میلیون دلار برای دفاع از آن‌ها در برابر روسیه هزینه می‌کنیم، و سپس آن‌ها به ما می‌گویند، «ما ترجیح می‌دهیم کمک نکنیم.» حرف احمقانه‌ای است.
چون ما می‌توانیم این حرف را به آن‌ها بزنیم اگر بخواهیم، و ممکن است این کار را بکنیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/alonews/129786" target="_blank">📅 00:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129785">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
رئیس‌جمهور ترامپ درباره ناتو و ایران:
من حتی به کمک آن‌ها نیاز نداشتم. بیشتر از هر چیز کنجکاو بودم.
از آن‌ها خواستیم بیایند، اما برای ما نبودند. احمقانه بود که نبودند.
استارمر آنجا نبود و مردم بریتانیا از نبود او خوششان نیامد.
استارمر به ما گفت: «به محض اینکه شما پیروز شوید، ما آنجا خواهیم بود.» من گفتم: «وقتی ما پیروز شویم، به شما نیاز نداریم.» این وینستون چرچیل نبود که با او طرف بودیم؛ این را می‌توانم به شما بگویم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/alonews/129785" target="_blank">📅 00:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129784">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
ترامپ: اگر ایران به توافق خود پایبند نباشد یا رفتار مناسبی نداشته باشد، من آنچه باید انجام دهم را انجام خواهم داد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/129784" target="_blank">📅 23:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129783">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
ترامپ: اگر ایران به توافق خود پایبند نباشد یا رفتار مناسبی نداشته باشد، من آنچه باید انجام دهم را انجام خواهم داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/alonews/129783" target="_blank">📅 23:56 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129782">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb4f50edba.mp4?token=HVuoTKP8a1AdISmKqSJcVN65zDLOKfg2QlNGCQBASIlgtK1DLkWZUGL8EqfbcXU4LVYhwZifQs4Ww78mjhHi29dGyMlNTeMKGrv8RrWfIlO36CPOIUWBSttKDlvmhDVdZYtaC7J5FCKMLF4k0SiJQnFM3aYxIGwTTAUd597ZgSZq2gNDBEgbfKIoNxVsIAjXu64hqeRsj-EzcP2dwg63B2eGoISz-hMFsUPnfEa6Q-GyYkSc-FtjAK1GbHI1i2UCVrFLUr973XSaabqWwZnlgJnQBN3veViBhY4kN76bcwr73Y_6xqTvjK_0WlAv5g3vLeM_LfanoBIckq5tOzr5qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb4f50edba.mp4?token=HVuoTKP8a1AdISmKqSJcVN65zDLOKfg2QlNGCQBASIlgtK1DLkWZUGL8EqfbcXU4LVYhwZifQs4Ww78mjhHi29dGyMlNTeMKGrv8RrWfIlO36CPOIUWBSttKDlvmhDVdZYtaC7J5FCKMLF4k0SiJQnFM3aYxIGwTTAUd597ZgSZq2gNDBEgbfKIoNxVsIAjXu64hqeRsj-EzcP2dwg63B2eGoISz-hMFsUPnfEa6Q-GyYkSc-FtjAK1GbHI1i2UCVrFLUr973XSaabqWwZnlgJnQBN3veViBhY4kN76bcwr73Y_6xqTvjK_0WlAv5g3vLeM_LfanoBIckq5tOzr5qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قالیباف: اگر به سوئیس نمی‌رفتیم، هر لحظه خون بیشتری از مسلمانان و شیعیان لبنان ریخته می‌شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/alonews/129782" target="_blank">📅 23:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129781">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/054f327a6d.mp4?token=H_0PgpCfJtQdmv11OU1XojWfcHD23b0iKmahjGrHRJKMwaV0l5TaCbBza7X2lNi1F9hp6mRJNl3JBxyaADjD-Ju7pyYTDimp9j2wwjYBZ7r74BLX0AxpExaYG8-VUmKSfhDRNfS6FDoCw3QNZwsc4aoofwXAzb7ZqoLSE7ow7rzxVFuC1GXEfB1r0m0B6daaHM-pi-iQQOX5iaTk7wCQHh3Wio1MN3s_tiktE7-gKaCmf_J-O80QEWEWdXFzcp-8qZIVK5oM8sjkNSSz-mx_ePd-FOE1ozrYUgE_dd3-rjVjPj1fyrFSXhLxoQb-XFEvcwuiX9rqPptdJodJx1aCPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/054f327a6d.mp4?token=H_0PgpCfJtQdmv11OU1XojWfcHD23b0iKmahjGrHRJKMwaV0l5TaCbBza7X2lNi1F9hp6mRJNl3JBxyaADjD-Ju7pyYTDimp9j2wwjYBZ7r74BLX0AxpExaYG8-VUmKSfhDRNfS6FDoCw3QNZwsc4aoofwXAzb7ZqoLSE7ow7rzxVFuC1GXEfB1r0m0B6daaHM-pi-iQQOX5iaTk7wCQHh3Wio1MN3s_tiktE7-gKaCmf_J-O80QEWEWdXFzcp-8qZIVK5oM8sjkNSSz-mx_ePd-FOE1ozrYUgE_dd3-rjVjPj1fyrFSXhLxoQb-XFEvcwuiX9rqPptdJodJx1aCPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: نتانیاهو می‌گوید نیروهایش لبنان را ترک نمی‌کنند
ترامپ:
🔴
ما قرار است به این موضوع نگاهی بیندازیم. من یک حل‌کننده مشکل هستم؛ می‌توانم مشکلات را سریع حل کنم، از جمله با بیبی.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/alonews/129781" target="_blank">📅 23:48 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129780">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cc43c98ca.mp4?token=LLfMXJklF6jDFdQJsnufSP-dPPd42hHoU2QCOJh1neQyYrA0am9D45d2AEz51t82U9r-GK-FPbwMG_cmivNWePsi0mQvSohhWmTFBYuecaF3MSbTo-xpYx2g4gwa7JFKjx6fgDgozH6YpOc1UQH3KlMO-nvIcWOSLQ-V95pcUw7X1Ef6s-nNHX0-K_T_5tbHchQC0S442OTPVJLYTLQIm00eU6jcHfqVW5J8xKmAtaV4GM3MUP1dVMPT19h81MvG9qDLlTpC0IurNWGUARVHg8yu17sc9aeJeBBSro_E9RN1MWH5H-320Manc8BurK9EoY4W2mg8olTj3bpZr7Jm-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cc43c98ca.mp4?token=LLfMXJklF6jDFdQJsnufSP-dPPd42hHoU2QCOJh1neQyYrA0am9D45d2AEz51t82U9r-GK-FPbwMG_cmivNWePsi0mQvSohhWmTFBYuecaF3MSbTo-xpYx2g4gwa7JFKjx6fgDgozH6YpOc1UQH3KlMO-nvIcWOSLQ-V95pcUw7X1Ef6s-nNHX0-K_T_5tbHchQC0S442OTPVJLYTLQIm00eU6jcHfqVW5J8xKmAtaV4GM3MUP1dVMPT19h81MvG9qDLlTpC0IurNWGUARVHg8yu17sc9aeJeBBSro_E9RN1MWH5H-320Manc8BurK9EoY4W2mg8olTj3bpZr7Jm-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس‌جمهور ترامپ درباره ایران:
باید مکالمات آن‌ها را بشنوید: «چه کسی می‌خواهد رئیس‌جمهور شود؟» «من نمی‌خواهم.»
هیچ‌کس نمی‌خواهد رئیس‌جمهور شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/alonews/129780" target="_blank">📅 23:48 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129779">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15fe6d2c2d.mp4?token=no5-QAYRpMFeEUKVWC5aN5gct0deNsGL9WiCGZSNLpVL_ybzK2cWcnqAaOz0s5a6xjzAc_Uoy25d9GZcX5ZzoZ_yeRZdOaTRMDEGU7wOWLr5Yu2KnZwM5AocgCaeIPJXJ2lfNQLquKjhRPu3_S91J9qs2FfTzm0jsFmmdOA3BG-BFBRkRUFLzK8VSBky_uz99_1AqG3fkI5Cvbud6GCf62Wvgtck2Eco9AqvlbxTrZWvHJ_XyxRPoeGLG_mOC69j3M7xPEWl1ebtyZxup1OXDnCODUyvhdjNwXx2qXPL4uuTSaesB0wxqkxby0KSPAOYrrjopeuqASkbOcJkVADTJBSxyxzToJAqpoBAQB_QhtsU-6SwyVH4lPdGPERh-qMeVa_mV0UqSQ8BwUOTP5F-Kc_6E6YrV8g-9XwV6OUUKeYXxS3jY8sQnfIpBvf_J6Ii38r3TVXnELNXmpNYVNWbQm0EVB7o5NBVLYlz6BnT-XMiSdJyVhIqbiDiZXRIlFp472bE8Q-WvOylPe_uDlguGDenyTlEyhptNNqDex6JhkWwS4B37YL8F0j5k_F47iTNN6ccqzK11XLKxKZ1qRQX1gRehv4M3Hx7etvcwbveGGDxgYiKwdSBykq3piA1eplEgf5nYwaQFtb5aetGydtoaPEjQd-chxlfWQ9xsyLOruM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15fe6d2c2d.mp4?token=no5-QAYRpMFeEUKVWC5aN5gct0deNsGL9WiCGZSNLpVL_ybzK2cWcnqAaOz0s5a6xjzAc_Uoy25d9GZcX5ZzoZ_yeRZdOaTRMDEGU7wOWLr5Yu2KnZwM5AocgCaeIPJXJ2lfNQLquKjhRPu3_S91J9qs2FfTzm0jsFmmdOA3BG-BFBRkRUFLzK8VSBky_uz99_1AqG3fkI5Cvbud6GCf62Wvgtck2Eco9AqvlbxTrZWvHJ_XyxRPoeGLG_mOC69j3M7xPEWl1ebtyZxup1OXDnCODUyvhdjNwXx2qXPL4uuTSaesB0wxqkxby0KSPAOYrrjopeuqASkbOcJkVADTJBSxyxzToJAqpoBAQB_QhtsU-6SwyVH4lPdGPERh-qMeVa_mV0UqSQ8BwUOTP5F-Kc_6E6YrV8g-9XwV6OUUKeYXxS3jY8sQnfIpBvf_J6Ii38r3TVXnELNXmpNYVNWbQm0EVB7o5NBVLYlz6BnT-XMiSdJyVhIqbiDiZXRIlFp472bE8Q-WvOylPe_uDlguGDenyTlEyhptNNqDex6JhkWwS4B37YL8F0j5k_F47iTNN6ccqzK11XLKxKZ1qRQX1gRehv4M3Hx7etvcwbveGGDxgYiKwdSBykq3piA1eplEgf5nYwaQFtb5aetGydtoaPEjQd-chxlfWQ9xsyLOruM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس‌جمهور ترامپ درباره ایران:
ایران چهار ماه پیش نیروی دریایی و هوایی قدرتمندی داشت. بیشتر موشک‌ها، پرتابگرها و تأسیسات تولیدی آن‌ها از بین رفته است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/alonews/129779" target="_blank">📅 23:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129778">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75e37a8b38.mp4?token=jfpYha17_b2ug7oCu-kkqV1U7KEMXSPHgi4s23XhmfmUlkcI3LV9GAXVsPGeqIxlBZ0VO1fUTqKDbe_TndvfZTWE382-NXlWKGRGXugzMa7IhpF2T4Y6fhwE308AE_96YzAK3u-iidDSijkGsmSaVPDp80G92DQXI7djU67Gl6b7brgGHq97-riDlKAgTcqko_V1qL7RY_XaCUNnO4-hKbAQMLhsppx37LT-iMeQx4XxWlTtkTh8PYy5xodRrhwzuMZ9EARuYoi4EtQFHwPKIOrK3Tc0cjb_PDe1fPKZ5SaXc-2VWA0Md7LyhpRPQY_r1vQhaPHe-3rQR2UTl6KI5ayS8RGqqFFRQmbeA2xIhsNT2QqglPLBjF6RRXFhs0_61_aOPHN7zEAZiu3s4JwD1LExt2uEJ0iIKEDxlEFFIYzCLWaRy5bcRKfT2cWGVAVjWee3bo6hGgKCdeBvi1wBKTGMwpqVdEeetUednnvF2oY1SHh5KweImh4OrQ2C8IppkOpp95FDAskHTqB5B0N-iNZnYnoRIdokjdcCnzzWiF5SQfCEhhC9rFyyy08R6uubnMWtxbZMu8nt_tATuby3dz-tYbgO-qHUQ_w0-h-DvMdnN1mTAlcunL8A_OOUhhnR5-BgaTgNv7wvf00UBr1zaEhlguF4cahc_btcimwamWk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75e37a8b38.mp4?token=jfpYha17_b2ug7oCu-kkqV1U7KEMXSPHgi4s23XhmfmUlkcI3LV9GAXVsPGeqIxlBZ0VO1fUTqKDbe_TndvfZTWE382-NXlWKGRGXugzMa7IhpF2T4Y6fhwE308AE_96YzAK3u-iidDSijkGsmSaVPDp80G92DQXI7djU67Gl6b7brgGHq97-riDlKAgTcqko_V1qL7RY_XaCUNnO4-hKbAQMLhsppx37LT-iMeQx4XxWlTtkTh8PYy5xodRrhwzuMZ9EARuYoi4EtQFHwPKIOrK3Tc0cjb_PDe1fPKZ5SaXc-2VWA0Md7LyhpRPQY_r1vQhaPHe-3rQR2UTl6KI5ayS8RGqqFFRQmbeA2xIhsNT2QqglPLBjF6RRXFhs0_61_aOPHN7zEAZiu3s4JwD1LExt2uEJ0iIKEDxlEFFIYzCLWaRy5bcRKfT2cWGVAVjWee3bo6hGgKCdeBvi1wBKTGMwpqVdEeetUednnvF2oY1SHh5KweImh4OrQ2C8IppkOpp95FDAskHTqB5B0N-iNZnYnoRIdokjdcCnzzWiF5SQfCEhhC9rFyyy08R6uubnMWtxbZMu8nt_tATuby3dz-tYbgO-qHUQ_w0-h-DvMdnN1mTAlcunL8A_OOUhhnR5-BgaTgNv7wvf00UBr1zaEhlguF4cahc_btcimwamWk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار:
آیا می‌توانید تضمین کنید که ایرانی‌ها از سود فروش نفت برای بازسازی ارتش خود استفاده نکنند و فقط برای دولت بعدی آماده شوند؟
🔴
ترامپ:
خب، آن‌ها قرار نیست این کار را بکنند، قربان. خواهیم دید، اما قرار است پول را برای خرید غذا برای مردمشان استفاده کنند، چون در حال حاضر مردمشان خیلی گرسنه هستند و آن را فقط از ما می‌خرند — ذرت، سویا.
باید پول زیادی باشد. امیدوارم پول زیادی باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/129778" target="_blank">📅 23:44 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129777">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbc98d2cf2.mp4?token=bjtc1P2OfW2DoLd8zVJG3ZRJ1vkAAEr-nz4VgOdAFc3xYYbGV7IkXAK-1-65xYd80NgxYvMig7W6DqmejzKPef1c97AlnFFyFJ2jCU0iNJRdv6mm1NrxpiriaLIGwHaTP7z0t-QHXFqwnNNr3CCH1r9Rq41f3OZJKFrg7RpJN9LNzVRGwrO2uPTyABsZvtVNhQDRbZs-Y-xQWfHdYus2AA2VRiF2oGpawfr4e0c0NmxtSIwzcEHNvgxwNDv6KRUe6_1TTpFwXugHA0XFwdIcKph0K1275XpLrxkhcXcjuX649_cDHiis9Ng_PnHRtvg-vFoXL9-nhj2ZDXbK2zQSTXfLvwUc6WXvoQhumcSXCd7n9uD1AggU_WG2KsFlGcKJ8vwKhCgBoJ-UY1kLLj-2yHqdqzVlH7jknxMaeyt_MGX0xQCSOnl78ANyi-NrpWD-ELvrd5UzxifBK5OpxRxJBG2enmVbacrca9jPG8GBMI3gglS1PXcEG1r-NpwX9kpzDBIRX_uCnZytGg1UqOTehwQ5G2GGfKtBdSHbUFJsndCHFFQU4XEJGZGBZrkMeDHCOl1VwqqktLB-sWdPTG6S3tEKw3t1_sODPRXmUG7dSUb50aolOQq2nhPNAGQlUKaKVdGHrdGBwEht-2kf-fYuMXI0GR29011HbDv006L026g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbc98d2cf2.mp4?token=bjtc1P2OfW2DoLd8zVJG3ZRJ1vkAAEr-nz4VgOdAFc3xYYbGV7IkXAK-1-65xYd80NgxYvMig7W6DqmejzKPef1c97AlnFFyFJ2jCU0iNJRdv6mm1NrxpiriaLIGwHaTP7z0t-QHXFqwnNNr3CCH1r9Rq41f3OZJKFrg7RpJN9LNzVRGwrO2uPTyABsZvtVNhQDRbZs-Y-xQWfHdYus2AA2VRiF2oGpawfr4e0c0NmxtSIwzcEHNvgxwNDv6KRUe6_1TTpFwXugHA0XFwdIcKph0K1275XpLrxkhcXcjuX649_cDHiis9Ng_PnHRtvg-vFoXL9-nhj2ZDXbK2zQSTXfLvwUc6WXvoQhumcSXCd7n9uD1AggU_WG2KsFlGcKJ8vwKhCgBoJ-UY1kLLj-2yHqdqzVlH7jknxMaeyt_MGX0xQCSOnl78ANyi-NrpWD-ELvrd5UzxifBK5OpxRxJBG2enmVbacrca9jPG8GBMI3gglS1PXcEG1r-NpwX9kpzDBIRX_uCnZytGg1UqOTehwQ5G2GGfKtBdSHbUFJsndCHFFQU4XEJGZGBZrkMeDHCOl1VwqqktLB-sWdPTG6S3tEKw3t1_sODPRXmUG7dSUb50aolOQq2nhPNAGQlUKaKVdGHrdGBwEht-2kf-fYuMXI0GR29011HbDv006L026g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار:
خزانه‌داری تحریم‌های نفتی ایران را برداشت.
🔴
ترامپ:
من باید دقیقاً وضعیت را بفهمم، اما اگر تحریم‌ها برداشته شوند، پول به این کشور وارد خواهد شد. تمام آن پول بازمی‌گردد. آنها ۹۱ میلیون نفر جمعیت دارند؛ نمی‌توانند آنها را تغذیه کنند. پول عمدتاً به کشاورزان ما خواهد رسید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/alonews/129777" target="_blank">📅 23:44 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129776">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sNLctDdQBEbtKzWrzec7z-TFBN0qPVdY6opiH0QAHUTxeKrk4xgYv7J7jUMb2N-K-eYeBDHn7pidz-_FXBJmaNRO4HKsQAb1xB3W86wL7xcxJ5fAjk5wAta3WW4wheFV8ee1IhTWAqc1ONLO2Cr4yrlQKLjt30ERhr0lGrYTelMABLyVSlKtjfMAv0kV3fgXe1k77xDpxONyXBQ9WjQ1mwsDeLu4O9o2GYIeC9ryNfEebV0LZd9vNJnO07qGvfkxlgSqeOKHtLhl8pPtcEQh6crcsQlE4YuTvS52oU37wfxjaMYVtWv1R_R7r7tLKgjf4lrmbBc0ijNKH7iF2Hncwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف: ۱۲میلیارد دلار رو آزاد کردیم
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/alonews/129776" target="_blank">📅 23:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129775">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K5pwotO0pPUgRWO6XWRZyDfXNpeHv1hfoTq3u1Y3yBRNf5dyLHAhMYb42yvT-8P6O9KWArXpC925fwwR_ENWN9Ep-Ece72TBFeRyHKlA2MQvw8xf8wcIeahv32O68GQUOvGd4o3glTGZnHWmUegipKvEfdejd94w97nbSq9wxFNTLIvHMasdmDgW8nXNzMEjtSiw-_lJ3n0O8R3fCvh-RmLjOVH-fXEdp6u3U6Zbsrhyxfet_YAPTTH7Y2RgRNOoLLcqTcrZ195A7G2HDQVMBAvCJgnQx_Wkp4vNfmd11SNbWJVuLy0ByNL5V0zWk5VUgsZBaAOeT14yhqDOaAabpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف: ۱۲میلیارد دلار رو آزاد کردیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/alonews/129775" target="_blank">📅 23:37 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129774">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd99c1a494.mp4?token=iALgJyEIqRqggLDdeJ02bRJeF_Ouj99Ptp8icahQkya7vcUY6W8HbDhHV5JGAnZLW5rPJtXzmFj1ikLZXTtV5cvzaiA5R3GF1RYKo6yNnmFRkQdJwcAUY4OYFsKvq2Z8BQkKvjFrswLsaFwrpjEUkoVpdinTWMFaPMi_3Rwm--Z5rjFPJEUNruBqqaqnCZlRUQ_wCpaSRIKfmAYdQ_spMYiXDS-AFlulAcoBKzkKwR1Rpde7x4uWihK2jGiGJUj930knZ2jO0t3UDfcTs6qdoAvJG8VhVhjzI4Ye7bKetg1Yxc4W-b_UlbSlUsjNQTEYR6Y-aRgQczs3aiAXzOBUJYjuLxZfCHk0XFzDuB4U5W4SAsx3jYNWXqLTYRZ2ZNMhwCnFq6Vyi6iuuO0YB4JpHPLLcIKJb3HG3oT28D_BEHaj6-lW3msIObiZMVTHZZz7RxF4awDShR9pPtAmTdD2tqgcpmcqMmqhy_syQjoVeXWjivKLT5CgwcZ0DtedjKtQtUmBQO5PNpW1b1nRR4GafXfWvw_TxouupRq4KqdKQQr0W_CESfvNmEhwL9JNUcN64NZoJ7JP62Dgcse9trC-553fT14bRsr5l_LBi3zCEaANyCXOAU_RR_KwpTItgi2cqDw3VWzLE5l4gKv9avmiAJl30YbrgJE167F5z8DO-Dc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd99c1a494.mp4?token=iALgJyEIqRqggLDdeJ02bRJeF_Ouj99Ptp8icahQkya7vcUY6W8HbDhHV5JGAnZLW5rPJtXzmFj1ikLZXTtV5cvzaiA5R3GF1RYKo6yNnmFRkQdJwcAUY4OYFsKvq2Z8BQkKvjFrswLsaFwrpjEUkoVpdinTWMFaPMi_3Rwm--Z5rjFPJEUNruBqqaqnCZlRUQ_wCpaSRIKfmAYdQ_spMYiXDS-AFlulAcoBKzkKwR1Rpde7x4uWihK2jGiGJUj930knZ2jO0t3UDfcTs6qdoAvJG8VhVhjzI4Ye7bKetg1Yxc4W-b_UlbSlUsjNQTEYR6Y-aRgQczs3aiAXzOBUJYjuLxZfCHk0XFzDuB4U5W4SAsx3jYNWXqLTYRZ2ZNMhwCnFq6Vyi6iuuO0YB4JpHPLLcIKJb3HG3oT28D_BEHaj6-lW3msIObiZMVTHZZz7RxF4awDShR9pPtAmTdD2tqgcpmcqMmqhy_syQjoVeXWjivKLT5CgwcZ0DtedjKtQtUmBQO5PNpW1b1nRR4GafXfWvw_TxouupRq4KqdKQQr0W_CESfvNmEhwL9JNUcN64NZoJ7JP62Dgcse9trC-553fT14bRsr5l_LBi3zCEaANyCXOAU_RR_KwpTItgi2cqDw3VWzLE5l4gKv9avmiAJl30YbrgJE167F5z8DO-Dc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس‌جمهور ترامپ درباره ایران:
ما در مورد تنگه هرمز بسیار خوب عمل می‌کنیم.
دیروز نفت بیشتری نسبت به هر زمان دیگری که از این تنگه عبور کرده، دریافت کردیم. تنگه کاملاً باز است.
ما دو چیز داریم: یک تنگه باز و کشوری که هرگز سلاح هسته‌ای نخواهد داشت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/129774" target="_blank">📅 23:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129773">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fa7c9b7e2.mp4?token=nMz0locl-Arj4WyMZsKx6vR5zjg3UPtHXVCRMbfPJFBjhQaOPENRQchty-S44bpVv6rKsCOaFR1ofCly6UIhL_DLNKEjMv6scwzziHpCRGAk-KSW1MXaoWH2T3KkepNY2ouHEpBX76bnbAuIeU5pEXWxntOz4qmNNZ0Y7DKrx_0I8uG-c7V89S5HePbNberNIPWC_p-HRgBNOn-O2pjOeHJtnSrjjD_A7FACbpGTllWAp5ktkXoD-LdOVOrxa_Rkr0daLof53GgXDbgqD49j8CGuoOwe71ab1bbKFjZFTlUt86MUQ8anQ6ZLVM7cq5CIwo8sqknrCIYOmFy6wEyV4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fa7c9b7e2.mp4?token=nMz0locl-Arj4WyMZsKx6vR5zjg3UPtHXVCRMbfPJFBjhQaOPENRQchty-S44bpVv6rKsCOaFR1ofCly6UIhL_DLNKEjMv6scwzziHpCRGAk-KSW1MXaoWH2T3KkepNY2ouHEpBX76bnbAuIeU5pEXWxntOz4qmNNZ0Y7DKrx_0I8uG-c7V89S5HePbNberNIPWC_p-HRgBNOn-O2pjOeHJtnSrjjD_A7FACbpGTllWAp5ktkXoD-LdOVOrxa_Rkr0daLof53GgXDbgqD49j8CGuoOwe71ab1bbKFjZFTlUt86MUQ8anQ6ZLVM7cq5CIwo8sqknrCIYOmFy6wEyV4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران:
پول‌هایی که در حال آزاد شدن هستند، برای خرید مواد غذایی استفاده خواهند شد و این مواد غذایی به‌طور انحصاری از ایالات متحده و از کشاورزان آمریکایی خریداری می‌شوند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/129773" target="_blank">📅 23:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129772">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
وزیر دفاع پاکستان:
اسرائیل تنها تهدید توافق ایران و آمریکا است
🔴
اسرائیل به هر دری خواهد زد تا در مسیر توافق خرابکاری کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/alonews/129772" target="_blank">📅 23:25 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129771">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0a8a9b37f2.mp4?token=AIaqlqzWmczNal_5YKpDm-hSnUsgKwkesfnBeu0YEKPO1cgaCpBl0dJ9levUf-x-tJujP9-XjLJfnYMmWLboMfGpLgFxBbs01v3DdJTVnc--bltlDm05so0-T_S86bEUqX4JMRvb6VXFnJRIU4QY53crLf4zfrwyIKr6HSGEf8fUw6ZQKrApkX1u_pUwjoHQKxfLxTeMCO-dDH1pSHpRIS1eif21_4qik7-ebddSD_MloAV-jvdLw2Jiw0tRsL6RN97TfBGbl4KdTuzz9shEp1RD4x9TDrwgF_mYLDxLiqzgkXXJ7UY1OKMaBgyYlTVffSgIlxM2nlsap8Zcn4R0IQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0a8a9b37f2.mp4?token=AIaqlqzWmczNal_5YKpDm-hSnUsgKwkesfnBeu0YEKPO1cgaCpBl0dJ9levUf-x-tJujP9-XjLJfnYMmWLboMfGpLgFxBbs01v3DdJTVnc--bltlDm05so0-T_S86bEUqX4JMRvb6VXFnJRIU4QY53crLf4zfrwyIKr6HSGEf8fUw6ZQKrApkX1u_pUwjoHQKxfLxTeMCO-dDH1pSHpRIS1eif21_4qik7-ebddSD_MloAV-jvdLw2Jiw0tRsL6RN97TfBGbl4KdTuzz9shEp1RD4x9TDrwgF_mYLDxLiqzgkXXJ7UY1OKMaBgyYlTVffSgIlxM2nlsap8Zcn4R0IQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عجیب اما واقعی
‼️
🔴
تو یکی از تعزیه های اصفهان، جیگر امام حسین رو در آوردن
😐
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/alonews/129771" target="_blank">📅 23:20 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129770">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g2DkrgU3hHbLz8d-JO8gqTTCJpyxLvnKevpvryTSOmMVVxOYSGWhBm1T5RRLfYmneLAiUiNsts9nmFq2b5qr56dKWGYTog1A-nSDBeNW4zeW_CY6-tt4Owo1PPOm_Cq4IznEweH5acO8O9Xm3DDQMuyaGU8mPAd8--YfPFTi46m8uW1qScqytc1-oLxmfFAelRMdt_oehlTE6TUj7EMeqxsUF-XyhhwNShSA62vadI8wXxfVVrjygVo3Wws05-LqC35WszenEzcdYq6VrgFZPT0sz9C8bMlqk5fdex0D7IZGMsKheKOgcVjtCahA7YL1wu9xRwmGy3wvAm_QKybgpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی: میخوایم جلسه مجلس رو وسط خیابون برگزار کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/alonews/129770" target="_blank">📅 23:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129769">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔴
فوری / مختارنامه شروع شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/alonews/129769" target="_blank">📅 23:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129768">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
وزارت خارجه فرانسه: بدون موافقت اروپایی امکان ندارد تحریم‌ها از ایران رفع شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/alonews/129768" target="_blank">📅 23:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129767">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
وزارت خارجه فرانسه: احتمالا در مذاکرات فنی بین ‌آمریکا و ایران در سوئیس شرکت کنیم
🔴
بدون موافقت اروپایی امکان ندارد تحریم‌ها از ایران رفع شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/129767" target="_blank">📅 22:52 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129766">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d033d127d.mp4?token=WFbcTRJ5oxx_CTJLBoh0_Dyppd4jCW3ZBl_XY8Yh0zxmBvwdLqJn0XeU1it4eDo0hAcu0HjA-nBG52YouCDvkgcKG1u41mcj5sQIRDTEo_QbtiAG1ow1kdBs2Sgf2G2p3ZAzpaK_es8AL3yRz9i1CPXRBuuDGekEDTs2IFpSPn-v2J1pfQIXtNl_ztXFFanppA3W1lBn8bqJttbytlAPVz3WP99viI6um3WtMfpYxfp5EJGKtvjzx3JHfpI2dx_yKxkGoqMS9EEsdrW7NeBUUK5eeFkodF9ZpjLA7cKcxXf5Yj9ySXEIMI2FK7XI1ndJP1XL1ceNxQf4KSzirbLYWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d033d127d.mp4?token=WFbcTRJ5oxx_CTJLBoh0_Dyppd4jCW3ZBl_XY8Yh0zxmBvwdLqJn0XeU1it4eDo0hAcu0HjA-nBG52YouCDvkgcKG1u41mcj5sQIRDTEo_QbtiAG1ow1kdBs2Sgf2G2p3ZAzpaK_es8AL3yRz9i1CPXRBuuDGekEDTs2IFpSPn-v2J1pfQIXtNl_ztXFFanppA3W1lBn8bqJttbytlAPVz3WP99viI6um3WtMfpYxfp5EJGKtvjzx3JHfpI2dx_yKxkGoqMS9EEsdrW7NeBUUK5eeFkodF9ZpjLA7cKcxXf5Yj9ySXEIMI2FK7XI1ndJP1XL1ceNxQf4KSzirbLYWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شبکه 14 اسرائیل:
به نظر ما ایران داره با یه سلاح الکترومغناطیسی روی مغز ترامپ اثر می‌ذاره
🔴
رفتار و تصمیم‌های ترامپ نسبت به قبل فرق کرده و این اتفاق عادی نیست.
🔴
این فناوری شبیه تله‌پاتیه، با این تفاوت که از امواج الکترومغناطیسی استفاده می‌کنه.
روسیه و چین این تکنولوژی رو دارن و الان هم ایران هم بهش دست پیدا کرده.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/alonews/129766" target="_blank">📅 22:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129765">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/812edc498b.mp4?token=LJ-JjZkwAV4VXlLrzD6jhGgvS_J0B-CtIEILDHSGyT9nEFmIcSJp5unxmvhjRBnRYWnnjPe6F54Ce5fxZ6iqD9rRSLMukm8cSsw8aAc-Xvbm4sYp7LYM8XJCM7E02nnrCGUhP79azq6DL0gsKmYlTkHGz8eRTNRRg13X2BK8uxeaUF34yJ94WiKqGGavYb6B_xBT0fvyH9rQ0fTUGCHJfAcflWFrnGJ86ts_h7Q3tp2renJk_yvcr_oEjYz9lL-jQXsHPwWj_ByDnFg4Suc5AAHt4Bpa2vkNCDfx2-mgkDPKp_O72OJKOk0h-gZ4Ips86zwwWWkEA6hm3g5tT0vNxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/812edc498b.mp4?token=LJ-JjZkwAV4VXlLrzD6jhGgvS_J0B-CtIEILDHSGyT9nEFmIcSJp5unxmvhjRBnRYWnnjPe6F54Ce5fxZ6iqD9rRSLMukm8cSsw8aAc-Xvbm4sYp7LYM8XJCM7E02nnrCGUhP79azq6DL0gsKmYlTkHGz8eRTNRRg13X2BK8uxeaUF34yJ94WiKqGGavYb6B_xBT0fvyH9rQ0fTUGCHJfAcflWFrnGJ86ts_h7Q3tp2renJk_yvcr_oEjYz9lL-jQXsHPwWj_ByDnFg4Suc5AAHt4Bpa2vkNCDfx2-mgkDPKp_O72OJKOk0h-gZ4Ips86zwwWWkEA6hm3g5tT0vNxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
این کلیپ علیه قالیباف توسط علی الاصول‌ها درحال وایرال شدن هست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/alonews/129765" target="_blank">📅 22:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129764">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
وال استریت ژورنال: ترامپ قراره چهارشنبه بره کاخ سفید تا با مقام‌های ارشد پنتاگون و شرکت‌های بزرگ اسلحه‌سازی جلسه بذاره تا درباره نگرانی از کمبود ذخایر مهمات و تسلیحات صحبت کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/alonews/129764" target="_blank">📅 22:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129763">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rqyyf8XhzyfJGi3J9ylQu_mqvR3ivLDdTot4xBMj82J1MkoX_7JUjjQQh7xiOKZs0R_4Y87XMLdO1z5bV7uB1BpZnnZpOhYDpMot4g-ZKUM4rSbDmV933cbeJ1fcU1KysQ87NopjmITVAuWDzy6HJN_X7eqldiiiLQxx5h1XDMWpHvmazg86abPgGW-Z-QLi9aFCsjjphlSGrGZkQhiRzj6cj4iHl01q5nNtCo0SB8IVm29pa1CaUakapM6qsepDD7m6qc-UDMph7XuyBn-7yY4wgwoB3JAo8l-sWm2Ihuwx1eQd0HmLjKtsF04c4RQ0tfoDlhC-XdYDe4iNG7V0Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرستاده ویژه ترامپ به گرینلند جف لندری از طریق ایکس دیروز: روز ملی مبارک به همه مردم در سراسر جزیره شگفت‌انگیز گرینلند.
🔴
امیدواریم امروز یادآور فرهنگ غنی، سنت‌ها و ارزش‌هایی باشد که میراث شما را تعریف می‌کند.
🔴
همزمان با نزدیک شدن آمریکا به ۲۵۰مین سالگرد استقلال خود، ما در جشن آزادی و فرصت‌ها شریک می‌شویم.
🔴
شاید تولد ۲۵۱ام آمریکا با اضافه شدن ایالت ۵۱ام آن جشن گرفته شود!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/alonews/129763" target="_blank">📅 22:37 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129762">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aff2ab234.mp4?token=T77-Gi-FjzB-us-hQ92wWJNv-WceRmULn0VoP0sWNxb8EzoKKVE_vc1zFCf0r4wdx4M_SL5OqncHiuGDwPCm0q6gCEsNUSD0D8jO888rIiOH02dHhHmGeD60k-KbiZGnssxTg8AhxuuXYmmLYc3WzgUwpq9NmgqGFQVy6aGVbU1AdoxSmcvgS8sYRNN54rJuRXhXWHJjdx4Y88R-VFuREyFV5rMXh31L7eDY2uyN8BDolqmWWMrNy5uBbmvp1_9gI1phPi_50mp8y_fZiOkntYaGbrIzwryKOohy-nIn0hj8XdqwwwhRbhHuknqVpxTtA4esYoxBeWXU6dGuV95Kig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aff2ab234.mp4?token=T77-Gi-FjzB-us-hQ92wWJNv-WceRmULn0VoP0sWNxb8EzoKKVE_vc1zFCf0r4wdx4M_SL5OqncHiuGDwPCm0q6gCEsNUSD0D8jO888rIiOH02dHhHmGeD60k-KbiZGnssxTg8AhxuuXYmmLYc3WzgUwpq9NmgqGFQVy6aGVbU1AdoxSmcvgS8sYRNN54rJuRXhXWHJjdx4Y88R-VFuREyFV5rMXh31L7eDY2uyN8BDolqmWWMrNy5uBbmvp1_9gI1phPi_50mp8y_fZiOkntYaGbrIzwryKOohy-nIn0hj8XdqwwwhRbhHuknqVpxTtA4esYoxBeWXU6dGuV95Kig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی دی ونس:
چیزی که برای من خنده‌دار بود این بود که بعد از آن جلسه اولیه، نوعی طوفان رسانه‌ای در شبکه‌های اجتماعی به پا شد که همه می‌گفتند ایرانی‌ها قرار است بروند، و بعد ما حدود ۹ ساعت با آنها صحبت کردیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/129762" target="_blank">📅 22:29 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129760">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/bSdKaNpJSJyV5mjPh07UKNfhXWpHQVn5f26Ti6IbGoqcr6WhlwMgoSL6el48Ct6E2eOAKdP2XdP-kDfNOPlNy5F3UaY0e0slsm2JNi2PNkJ8dMfwwjxM6DUwOOYpZlXJx5StPGt15B9AN7nFEvCmNOwQQIDYY-9CsgUd_XT6MKcZp_PAH9VVPua3qXw3st7rAoAMWLS3PXJADu5brcSIV9AoqNCy_TMPG3bZHeHAUb_YoRaR6yKFU4NA0cQ0PBWQByXIXXI_XQ4Q2m33OqbzqvrUj1Lm88CLbzS3pEaF1xbZHYpgMFQbLpNHuocviFow3SEKhTM6a57ErLWfRPJPng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/0336eb3457.mp4?token=NXebh1vhxATw2tEDbjHAgH9FAMHuGUDRSxns52Fd98ue3X5QfhKM9jxUtBzKEBqjObc4dtiNphBFnULdkIIt4rpKxQDIC1sDq6OxVRFwZen-8KH19KSlp9Y83q9Oom3YDaNNvMoA0hMcWzDEdtgvELhRS5BUN1wBkRlvOg_TG8sae8kusqvC4_qXnMtuO4bUI7GMvyC9sjlazV8_FGE1E_u5ORB03XF-Q56VM_OGxXIw2dkDXDNSqB-KDwosZjcub8bfBV8pnEmyUO0kJXRwjTPPrl3XjzG-DAX87c5TTkZ9hyPnEvFfoPjPKE96X-u06ZyKStOE4zvc6-svBHxwjA" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/0336eb3457.mp4?token=NXebh1vhxATw2tEDbjHAgH9FAMHuGUDRSxns52Fd98ue3X5QfhKM9jxUtBzKEBqjObc4dtiNphBFnULdkIIt4rpKxQDIC1sDq6OxVRFwZen-8KH19KSlp9Y83q9Oom3YDaNNvMoA0hMcWzDEdtgvELhRS5BUN1wBkRlvOg_TG8sae8kusqvC4_qXnMtuO4bUI7GMvyC9sjlazV8_FGE1E_u5ORB03XF-Q56VM_OGxXIw2dkDXDNSqB-KDwosZjcub8bfBV8pnEmyUO0kJXRwjTPPrl3XjzG-DAX87c5TTkZ9hyPnEvFfoPjPKE96X-u06ZyKStOE4zvc6-svBHxwjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امشب دوباره صداوسیما دستش در رفت و دوتا از هوادارای آرژانتینی وسط صداسیما لبارو درگیر کردن
😂
@AloSport</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/alonews/129760" target="_blank">📅 22:23 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129758">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
وزیر دفاع پاکستان: توافق ایران و آمریکا، به معنای پایان سیاسی نتانیاهو است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/129758" target="_blank">📅 22:08 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129757">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/460ce843c3.mp4?token=RGlUCMkseOLFHTqbJujVisgo7GuyofbfseBDxPs-7E61FWUzFJCKggeaJQyJt8ymo-4VmJxREIv1GV3L5E_wlks5uqJkQhxduqSQ28OfM5pYnAtC-XJv16BiEVkrMCD-XAHSvhO5bEpIh47CdVRxbvgX06Ddq_AMyuG0lSfx1krLYN-t3RhlcmUcuwesaRjyJpqANWqx8BPZM1DD0uEqNHs03CsZoCXe-hIymQS_C9ilOHabmr1opqtwIHrWBwSmDppC7t00e2MzyqHSm7NRkxb7haWcC8TnKRYIeVTddoVJKNB3oXz6pdPxB7Jl6qNdqlHa8Cd1pBurJapT3heYow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/460ce843c3.mp4?token=RGlUCMkseOLFHTqbJujVisgo7GuyofbfseBDxPs-7E61FWUzFJCKggeaJQyJt8ymo-4VmJxREIv1GV3L5E_wlks5uqJkQhxduqSQ28OfM5pYnAtC-XJv16BiEVkrMCD-XAHSvhO5bEpIh47CdVRxbvgX06Ddq_AMyuG0lSfx1krLYN-t3RhlcmUcuwesaRjyJpqANWqx8BPZM1DD0uEqNHs03CsZoCXe-hIymQS_C9ilOHabmr1opqtwIHrWBwSmDppC7t00e2MzyqHSm7NRkxb7haWcC8TnKRYIeVTddoVJKNB3oXz6pdPxB7Jl6qNdqlHa8Cd1pBurJapT3heYow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش اسرائیل در ۱.۵ کیلومتری شهر نبطیه!
🔴
حضور تانک های اسرائیلی در روستای کفر رمان در فاصله ۱.۵ کیلومتری نبطیه در جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/129757" target="_blank">📅 21:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129756">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
ونس: دارایی‌های مسدود شده ایران آزاد نخواهد شد مگر اینکه در مذاکرات پیشرفتی حاصل شود؛
🔴
ایران برای اولین بار پس از مدت‌ها به بازرسان آژانس بین‌المللی انرژی اتمی اجازه ورود خواهد داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/alonews/129756" target="_blank">📅 21:48 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129755">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
وال استریت ژورنال: ترامپ قراره چهارشنبه بره کاخ سفید
🔴
با مقام‌های ارشد پنتاگون و شرکت‌های بزرگ اسلحه‌سازی جلسه بذاره تا درباره نگرانی از کمبود ذخایر مهمات و تسلیحات صحبت کنن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/alonews/129755" target="_blank">📅 21:46 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129754">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
ونس لحظاتی پیش سوئیس را به مقصد آمریکا ترک کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/alonews/129754" target="_blank">📅 21:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129753">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
قالیباف: حاکمیت ملی لبنان بر تمامیت سرزمین خودش انشالا در این گفتگوها به نتیجه نهایی میرسه و تا به نتیجه نرسه، رهاشون نخواهیم کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/129753" target="_blank">📅 21:37 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129752">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
قالیباف: بدون دیپلماسی زحمت عرصهٔ میدان به ثمر نخواهد نشست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/129752" target="_blank">📅 21:23 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129751">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
قالیباف: مذاکره، یک روش مبارزه است و ادامه آن است!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/129751" target="_blank">📅 21:12 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129750">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k5QHIfqtg7_c_Z6-_u-cWpkiSvy3Kf0EpvlnqVJbc0oJ6kOGlyQuO0JL1Pdo2jDErXazDemYUxWj6aghJEAk7_q1BuAzhf18o0n9bNhI_JSZAx0DFb1LZQ_Yp-qf-oeKkJ64Qbuw-bSp5w35PJ_VJtcCWNmgQ_PGG-4-IMRpYe0cB0t5JGcrfjtPi7uRAvy5CmNxOMWMEiRdy5IgNwuybhICJsZSzHcp9wmMQfeniQ0U1ah7TCw8AYUO_hnlTeAUTy_p7v_0LIppMqK8hRcc4mgf7ASN5SL2Yq2eWWpYn2ERPMJo6Wh6pyjvbPJSBt8hYywr4HJxQ6G9Nhb3MLUGmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عضو تیم مذاکره‌کننده ایران در اسلام‌آباد: احتمالا اموال بلوکه شده ایران صرف خرید مستقیم از آمریکا شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/129750" target="_blank">📅 21:11 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129749">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed2b1eb31f.mp4?token=WjQkffRfu7UHz9k_bMWdlgFfLwexCzC6j3ruYZICYQWbS55j7oY0VHTZOGdI98pImBpr7Jjk1R3zA90PxOugyqlI8gpGGYt9-76y8WDh2tVcQoTkpUup6BOgYYex0WtloPj-1PdwJQkdfEenIYFazn-_PAvqTec6fKIwO5VMXqhntEV2VXXr1vnXYG-BjI9CJaeKk2p8xFtjFm_BwTwPGPy2YeWhXoDzEN816ME41ncc21pA3XEUa18-kcmJwE2H79eHum1o2AXa22HtKnB2Bl98VmBgxmadvrqhzPAd-GF6YpnhbAKxRyMbqMNHSAFBfuAGZfoToOugHuhdRJnnsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed2b1eb31f.mp4?token=WjQkffRfu7UHz9k_bMWdlgFfLwexCzC6j3ruYZICYQWbS55j7oY0VHTZOGdI98pImBpr7Jjk1R3zA90PxOugyqlI8gpGGYt9-76y8WDh2tVcQoTkpUup6BOgYYex0WtloPj-1PdwJQkdfEenIYFazn-_PAvqTec6fKIwO5VMXqhntEV2VXXr1vnXYG-BjI9CJaeKk2p8xFtjFm_BwTwPGPy2YeWhXoDzEN816ME41ncc21pA3XEUa18-kcmJwE2H79eHum1o2AXa22HtKnB2Bl98VmBgxmadvrqhzPAd-GF6YpnhbAKxRyMbqMNHSAFBfuAGZfoToOugHuhdRJnnsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بنیامین نتانیاهو نخست وزیر اسرائیل با ژلیکا کوییانوویچ، رئیس دفتر ریاست جمهوری بوسنی و هرزگوین در اورشلیم دیدار کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/129749" target="_blank">📅 21:08 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129748">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
شبکه اسرائیلی i24: هیئت «اسرائیل» فردا راهی واشنگتن می‌شود؛ دور جدیدی از مذاکرات میان اسرائیل و لبنان از فردا سه‌شنبه در آمریکا آغاز خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/129748" target="_blank">📅 20:46 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129747">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_NIFbCiCuMIKYk_wiUjQSoZGRb0LKy7boMg-HstZqp7Iqjxru0OL58JO046gp9zaMK_os5vTA-wN_ZSEabtSRWRNzxD5oJKWLb2XTiWmWLio09_OeHiy8Q-Yb3RMabqBtvebS12g47VCtl2k7HUbEXpIm5kkkWIqPh1roa8CEYOhIuXNE4LHqJ7PEnMsMhG2_wpu21WlOtgDXc7YYlrBgCBBOvMi6BweO1Pwyc8soKOpFaJbn21FbUC3JzObZ54zeYQpskGsn0onhqgA8JWwEFo4Dbq_FtkbgZHTE0UWsCBlfOlTCr47Lb7UlwQGf_t8pPqMirG2S8aBgcUEv4iMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پرواز ۶ سوخت‌رسان آمریکایی بر فراز خلیج فارس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/129747" target="_blank">📅 20:41 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129746">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bC5Vi4uYqWkK10g7bXM-2508ulk9LCfT-fkSymF2keq67rb98z0qU6LmABc0K19dy6KhKThiFgo5mHv-uqW0eLYmzfcEIGmhkSAqGGgCL9NrWRhOzgTq0lhbTp-dE6vfb7TiDG_XAhGTwpocba6w0YSM53NMpw0aBjCFfOKIjsCw5Eg0G6vsy8KgrzSPfewcuQBnXx0OqwkqiUkTnATCmNOsdeP19hYEdyO9G3FCW_nn3XkJoi8Zzk7Cgi2lO3yrRIOhNde8VVellN_SGkaEnnLdn7upuzZ9BKZWjIYh35BGUptk7lFcup8cpCQ89aONbcOpIlryoUm0cArhrc37aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ:  همه به خوبی می‌دانند که ایران برای تضمین «صداقت هسته‌ای» در سال‌های آینده، با بازرسی‌های گسترده تسلیحاتی موافقت خواهد کرد. رئیس‌جمهور دونالد ج. ترامپ
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/129746" target="_blank">📅 20:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129745">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
در پی رفع تحریم نفتی ایران، قیمت خودروها از دقایقی قبل در بازار معاملات خودرو کاهشی شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/129745" target="_blank">📅 20:27 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129744">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
وزیر دفاع اسرائیل، کاتس : امنیت مردم و نیروهای اسرائیل اولویته
🔴
ارتش با حمایت کامل دولت اختیار کامل داره با هر تهدیدی تو غزه، لبنان و هر جا لازم باشه برخورد کنه
🔴
نیروها شبانه‌روز در حال عملیاتن و اسرائیل تو منطقه امنیتی لُبنان می‌مونه تا تهدیدها و زیرساخت‌های نظامی رو از بین ببره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/129744" target="_blank">📅 20:26 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129743">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
رویترز: ذخایر نفت خام آمریکا به پایین‌ترین سطح خود از سال ۱۹۸۳ رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/alonews/129743" target="_blank">📅 20:06 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129742">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XHHxAsRMYW7cRjriCiU5tDherX_fNHJ1RemK3IT9qe6_cG0DuBLjvvFZr8DSgIUXV-Eb9AU62PEVeXtSQhtQ7r0CNrLDJ8u1_qgCtPTfWwygsVWQSEnt77aurgLntDIfcLRMsEAY3n13kY2qubitBpWlKov4wqdMhXhM0SjtoseNCHhMgXcBiJvwCkduaGzSDQIYGxNijFQm5gob3xLFEMyqZLQvn6dvetIsfe3BI-_k4EW-HZNdJgVNdlveHUx3Y9zeLLq5Hj5ZMccqhOSM1kLlqRt5c8EtWqyEODxBXb37GwPgzl8C5RrCQup42nISFrhey5VkBhp3nTHWakUu7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا ادعا کرده، این معافیت تحریمی در ازای اجازه تهران برای بازرسی آژانس از تأسیسات هسته‌ای ایرانه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/129742" target="_blank">📅 20:05 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129741">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JZXOJO4tQPT6X49J8pw87nL7u3Ev5YHZSGdp3ZOJ8c1nObkBRE7LmgaYeGt7u-78EF8DE4Nhwhs7wOf_UMe2ewov_6GqA--YBpjPXDKbMUfSvWeQUHffm_-Emjtvx_UtMAKgWP42d-t3fdz_YLEcv3ZhVcFfRxkrt4ABqYUATyYKcLW_0rrfosFZxvQAQ8QDlJLRCF1P1SqhuNDsXcH_47j8dKX3QGBxACGIuZ8defOGoWTQBNYDi36Yrhda3vephEBYDqVItwUO_YlcTg_jykxurmlff4N6y0fXdfDNCcZASfBDjzRaXSNdDQ_jyj3WC9p5TVtygiYoMS9cCbYEIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / وزارت خزانه‌داری آمریکا رسماْ معافیت تحریم‌های نفتی ایران رو برای ۲ماه صادر کرد ( تا ۳۰ مرداد )
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/129741" target="_blank">📅 20:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129740">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cZYWxzqHfFmDxCT7vrQkL62KERbPpA00tspNtr85XgLKfjwZM-vfWeXeu26QC80UsrCmTf7CSanK_0Q3roFhtZjlGUX9Ya4CpgkQBE3460cZOHBe0DVxI2JC1-aem08N-9zSUue9KevRZzaeHVJRraEAleLotJqLT797_PnUav8BwzbLG0DGerJ-_3eDVqliC52l9-2Vpr5ab9l2Rl0wk8huiyJJfI7SDI6ThhDsJwFEL7lspLuo62vGcPY6FSMD7vqgho8y6FVN4dTWj0ZzBRT7mdE9-apU3q7C9ZagbLCCE0ranJsKcqB2CX1Rmc0sgwEzhcuWN2TJ0fwyJOSvXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مرندی: ایران قصد خرید کالاهای کشاورزی آمریکایی را ندارد و دیروز هیچ بحثی در مورد آمدن بازرسان آژانس بین‌المللی انرژی اتمی به ایران صورت نگرفت. تبلیغات غربی را نادیده بگیرید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/129740" target="_blank">📅 20:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129739">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21803dc203.mp4?token=vWI_CWb_JHG5J5SoIHbNwvLAMZIgjBJoBFS2vIP7jtIATEzsIRZZ9MhuO-BYtAp8lVC1KluotyXtyXiM1M1RQDsCSJXlfoJiwzKPVnneMlj7e_Ehua0MQIkp8w16OXWo29N5K4OQziZaX5rAtDH1JEQFW-PtYwN4jhtxJImFjrwWOXRuROGG60ixvxLSox8Y4BdfB1YhbQPh-8G9S4Mpz4cuZMFHUPalL5wj38aIQdK5Cy2Owa8JKAq-XVu8069jIR6Upaocn8mr82_vkOVSPRGwRZoHXymB5TpFZT9g72ZotC1wjyW7R__yMUmRQ0OT9X21FCprnz_epK4gteHv0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21803dc203.mp4?token=vWI_CWb_JHG5J5SoIHbNwvLAMZIgjBJoBFS2vIP7jtIATEzsIRZZ9MhuO-BYtAp8lVC1KluotyXtyXiM1M1RQDsCSJXlfoJiwzKPVnneMlj7e_Ehua0MQIkp8w16OXWo29N5K4OQziZaX5rAtDH1JEQFW-PtYwN4jhtxJImFjrwWOXRuROGG60ixvxLSox8Y4BdfB1YhbQPh-8G9S4Mpz4cuZMFHUPalL5wj38aIQdK5Cy2Owa8JKAq-XVu8069jIR6Upaocn8mr82_vkOVSPRGwRZoHXymB5TpFZT9g72ZotC1wjyW7R__yMUmRQ0OT9X21FCprnz_epK4gteHv0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اردوغان: به امید خدا، شهرت بین‌المللی آنکارا امسال بیش از هر زمان دیگری افزایش خواهد یافت
🔴
پایتخت ما نامی برای خود به عنوان مرکز دیپلماسی جهانی خواهد ساخت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/129739" target="_blank">📅 20:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129738">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
وزیر خارجه قطر: مذاکرات فنی میان ایران و آمریکا ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/129738" target="_blank">📅 19:56 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129737">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
فارس: ادعای معاون رئیس‌جمهور آمریکا دربارۀ بازگشت بازرسان آژانس به ایران کذب است
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/alonews/129737" target="_blank">📅 19:46 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129736">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
قطر: ایران و کشورهای عرب خلیج فارس نشست امنیتی برگزار می‌کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/129736" target="_blank">📅 19:46 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129735">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
به گزارش نیویورک تایمز با استناد به دو مقام اسرائیلی، سربازان اسرائیلی روز شنبه دستورالعمل‌های جدیدی دریافت کردند که عملیات آن‌ها در جنوب لبنان را به «اقدامات دفاعی» محدود می‌کند.
🔴
طبق دستورات به‌روزرسانی شده، نیروها تنها در صورت وجود تهدید فوری مجاز به شلیک هستند، مگر اینکه مجوزی از سوی رئیس ستاد ارتش دریافت کنند.
🔴
این دستورالعمل‌ها همچنین شلیک هشدار به غیرنظامیان بازگشته به جنوب لبنان را ممنوع می‌کند، مگر اینکه آن‌ها «بیش از حد نزدیک» به مواضع نظامی شوند. علاوه بر این، نیروها دیگر بدون تأیید فرماندهان ارشد مجاز به تخریب خانه‌ها یا سایر زیرساخت‌ها در منطقه امنیتی نیستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/alonews/129735" target="_blank">📅 19:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129734">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
فارس: ادعای معاون رئیس‌جمهور آمریکا دربارۀ بازگشت بازرسان آژانس به ایران کذب است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/129734" target="_blank">📅 19:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129733">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S4D5o6U-kXg2xBtJCeCZ7vHOU3pXrhsAk3xiOHRPLTRR80XuCRqKh0KgXvH1NZiKgBaCI4wf3ULoWtp4JhagvUoef_PO0BzK0Bo5aaqFKasj8Tmz9YfJY8X4yUS4MviCorzD3KOJa_v3iiFNSz9ol5uZTiNAHeOwjMl_2jt08Ol5STSgm6SiXmi2kVi-WEl1V6D1KU2-A_uAF82_jYrbXiMRM-JGkXlZiuJkPQt0jXSnfEG04mViCIYqMs-zorv3Mo1f0i7jRrYIxNLkQ5UVffHrQ0LDf844AJ32gl9V1EvffAMR5_sIyLTtFk898oVjDRM9HOFEN6HMeAO0yIUSaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف در سفر به عمان با  "هیثم بن طارق" سلطان عمان دیدار و در خصوص تشریک مساعی برای تثبیت ترتیبات ایرانی اداره تنگه هرمز گفت‌وگو خواهد کرد.
🔴
در این سفر عراقچی، رئیس هیئت مذاکره‌کننده ایران را همراهی می کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/alonews/129733" target="_blank">📅 19:25 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129732">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
قالیباف رئیس هیئت مذاکره‌کننده کشورمان دقایقی پیش تهران را به مقصد مسقط ترک کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/alonews/129732" target="_blank">📅 19:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129731">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q9UPLzjJIkWYy2srKCoK2hG7oMFD_5LBSorn17XMBESeKPNEbESXp8yYPFBU9W_uiJesXjPBUwuONjbtb15NMENy-02CR5hRmXbgBD_tp5vrn7IrAUQjwvDuKGn00DAvEkmtayEcD2WgvV3frhonmKbfVdy6V_5VBkWrIB64YChTtbHv2iME_djDxmwtcxbwQPm-JI8vKCzsUtTPOi6W2zmtMBWPGUrkQ91kTQSRuCbQOSVeAehjqOOq25WqIkdLA54tKw10l6jwmY49tACDsmRA6J8O6eq5qRmYz9s8-cO0LyI3pB6i9DgE1zkVbY53MnPplL3My-Ngx5fYKUemNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
باراک راوید خبرنگار آکسیوس:
🔴
وزارت امور خارجه تأیید کرد:  روبیو از ۲۳ تا ۲۵ ژوئن به امارات متحده عربی، کویت و بحرین سفر خواهد کرد. وزیر امور خارجه در مورد طیف وسیعی از اولویت‌های منطقه‌ای از جمله یادداشت تفاهم با ایران، تلاش‌ها برای تأمین ترانزیت کامل و آزاد و ایمن از طریق تنگه هرمز و اهمیت صلح و ثبات در منطقه گفتگو خواهد کرد.
🔴
وزیر امور خارجه در بحرین همچنین با شورای همکاری خلیج فارس دیدار خواهد کرد تا در مورد اولویت‌های مشترک در سراسر منطقه گفتگو کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/alonews/129731" target="_blank">📅 19:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129730">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
جی دی ونس:
اگه پول های بلوکه شده ایران رو هم آزاد کنیم؛ فقط باید باهاش از خودمون ذرت؛ گندم و غلات آمریکایی بخرن. تا هم کشاورزهای ما پولدار شن هم به نفع ایران بشه.
🔴
تیم ایرانی رفته اورانیوم ۶۰ درصد رو داده جاش ذرت و سویا گرفته‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/129730" target="_blank">📅 19:18 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129729">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
اسماعیل بقایی، سخنگوی وزارت امور خارجه:
تعامل ایران با آژانس بین‌المللی انرژی اتمی طبق روال جاری و بر اساس مصوبات مجلس شورای اسلامی و تصمیمات شورای عالی امنیت ملی ادامه خواهد یافت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/129729" target="_blank">📅 19:15 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129728">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
جهت رزرو تبلیغات در الونیوز به اینجا مراجعه کنید
⬇️
https://t.me/ads_alonews
https://t.me/ads_alonews</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/alonews/129728" target="_blank">📅 19:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129727">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d4e5db99c.mp4?token=qzBT69H71Q4k-AZPO89rNuPog-gBgCTjhHKlZX3BzUW5a2neYOGO1idLV7pde5ALpM13q2uVjHCdyrFdzghQPlJl8ZVxtNZYQxsO-jPTN2mTrySGshkij9tm432IWKjATn8k42AGMnhvR_aFOTWpPaBhYmv6QX2o3xs8AOPcMr0JgRvwueFa58giVNoWpOPnhhzgIMimudDnHsejy3HYidGB_kywvpXjK6UK1DAdSByyVkXfVfJB7GBgFviiPUd3MQpJzYiBpkrXk4wlmBVUskcraNmTJMydZhtL8DgG4V57AxR4Ua_lsK58AfzSRy3o0pf4w-ZslXeu1adWyR3894WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d4e5db99c.mp4?token=qzBT69H71Q4k-AZPO89rNuPog-gBgCTjhHKlZX3BzUW5a2neYOGO1idLV7pde5ALpM13q2uVjHCdyrFdzghQPlJl8ZVxtNZYQxsO-jPTN2mTrySGshkij9tm432IWKjATn8k42AGMnhvR_aFOTWpPaBhYmv6QX2o3xs8AOPcMr0JgRvwueFa58giVNoWpOPnhhzgIMimudDnHsejy3HYidGB_kywvpXjK6UK1DAdSByyVkXfVfJB7GBgFviiPUd3MQpJzYiBpkrXk4wlmBVUskcraNmTJMydZhtL8DgG4V57AxR4Ua_lsK58AfzSRy3o0pf4w-ZslXeu1adWyR3894WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خوش‌چشم، کارشناس صداوسیما:
خوش چشم
:
آمریکا ۱۰۰ آب‌نبات جلوی تیم مذاکره کننده ایرانی انداخته است تا مروارید ایران که تنگه هرمز است را از آن‌ها بگیرد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/alonews/129727" target="_blank">📅 18:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129726">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
ایرنا: تا این لحظه موضوع صدور مجوز برای ورود بازرسان آژانس به ایران توسط تیم مذاکره‌کننده یا مقامات تایید نشده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/alonews/129726" target="_blank">📅 18:43 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129725">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a94bde71b.mp4?token=eCd9RtfIX7_bmNh5TJrPZ-DDkh5ModqbEOjgH-TEyB8Er4q44ET595w1H9Rhitd1IA2vJjGzfrrkiG25Yf4aDUSbKSpPZYIa-p7XOLFN5CWTult48lw2O-54_56DbiwuyxmQsEk3YsA-l08i17P0jswvk9aH0j68rOOxrMxJY6jh4D_wUtagriU_eE7XB7fAtplZTv4KbEMrCvUbs4D-zvrM_MIYF39gReI5Hbt_VK4QTAhTHjAxFBFKllKqOTq71YUIigneBEA2Hl55S6WA8O8LRSIRk7MHsDHk6hZWGETzwXCN0_Hg6ewN_GRgVI72DV_oG_xDiw_rskhUAEXJhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a94bde71b.mp4?token=eCd9RtfIX7_bmNh5TJrPZ-DDkh5ModqbEOjgH-TEyB8Er4q44ET595w1H9Rhitd1IA2vJjGzfrrkiG25Yf4aDUSbKSpPZYIa-p7XOLFN5CWTult48lw2O-54_56DbiwuyxmQsEk3YsA-l08i17P0jswvk9aH0j68rOOxrMxJY6jh4D_wUtagriU_eE7XB7fAtplZTv4KbEMrCvUbs4D-zvrM_MIYF39gReI5Hbt_VK4QTAhTHjAxFBFKllKqOTq71YUIigneBEA2Hl55S6WA8O8LRSIRk7MHsDHk6hZWGETzwXCN0_Hg6ewN_GRgVI72DV_oG_xDiw_rskhUAEXJhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله مجری تلوزیون به قالیباف و عراقچی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/alonews/129725" target="_blank">📅 18:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129724">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HOnFpN9lBtb2yC1PCA0zCl644oqsEx1i8RjHbt53kXii2KoxIFUDhvyyN3E6N4tzeXHyHSHBvLit4v2_NdOLErt-UdzInUxKOZzYZ5_LKtPKlCrx70SpxKue0jYu1qL6kfKsBwimG3FG944R2EwSNr0JfTFteW1YTU0W3dN78zcd-uHxLEIUKIi9iOl3VdFqUGRxDKQnKytIpPpIcCnj46WziOb4q5Oy-N_uPB5D2X7B1QLxcGZM-OmErimTJ9XtqkdGB8t5C-inj7M9UZg3qfiOFk4zKtT7vNc_8ab6OkdiO2jSMM82uFebg9OwStxeF_Bptu4DkudsdSsT6fd91g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی: قالیباف، دستش تو دنس ونسه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/129724" target="_blank">📅 18:08 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129723">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HHx7SL8aSJRBq2gHfNNqHHyONIqv12pOP_JFjExm4PJa-dedaH9fe_UuijnRDWOHxOA52lWuqnETaCLhDZshToLxIbNAVItWICpErnndbKNfiH49fpUAqiP5sk799WbNr0ErGbuylzHOXjI1xvw_8IR1eAwn-l8IIbKB53URo6anjTcv-dA8v_7h4cRopbtIUIkdVUSyAs2q2kR5CQfXrmVcAu_87y1etQ6ndBxEiF4vWgR3a-qCtvpYcWRU9PbgvldRkkNFXJZPy00VCh22sD9ALNu0A1t_iDXT36_LtmqLubPMxrmNVLewXgmz-ObNkPgBFrPIAPzUjPDhb9eEbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کت و شلوار چروک آی هیمتی در مذاکرات هم سوژه شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/alonews/129723" target="_blank">📅 17:59 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129722">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5102504900.mp4?token=IaY9PVYTdP8hxNzcCEn-qZOjC4BKWuFtblRUI1baYSZtj1wEP7Dg685t2F7_LNaZ9GoFbzZFC9-xxjUkmCHjmmkIpqBSE-Z3SdwrrMjzRSPadCbOlnNUqlP01F6LgWx4rIl-0uPHQSV9k4RDuKxBq4p_TEmeKleanpKiOkZCkPgC3bU_RJOJQ0Q6ysJgINOtiJafPBTVzPzOBHHHEBCrFhqd9nvU05YLBZ2-jSVBChwCnJuQkRAG5jprG3R4PFtBLvEEtJrP4EMr_PpgZ9_JnuKtOSS99OVZvH5uo7vpgtaV8_MabANr28Ika74bONGIRpNr237pjku9oJZhAuIC-jwCrwPe1r2WnXZmi8GCuxV_mdI0SRENSJsOXUMwMj5HOKAvwHr2AzcYccy0IG1bI7Qj84_n_5atW3GsgyjISxwVCkHTCfuzNiWIz3Dol8pDvkgTdftGMf3lwdT40dLpZDn3wDj8iK4RLxaTqhI6_rL3iCAafjtfTHknpO6annEATEe9AOQKkd0jnGxUtJkrhqHNfHReOjWX0ifGNKJBohSdpvBmP4HYxfkCzGwnZrJYYs4wPWJZZZ8qzyiJXmy2eU5QjZFHqxpldeTh_hfVsJdgG8CR43Tpr7EEej32sukG4U34j3xF9N5AasXuQBJNmSedUSXgdWqaHbvMmMeS83g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5102504900.mp4?token=IaY9PVYTdP8hxNzcCEn-qZOjC4BKWuFtblRUI1baYSZtj1wEP7Dg685t2F7_LNaZ9GoFbzZFC9-xxjUkmCHjmmkIpqBSE-Z3SdwrrMjzRSPadCbOlnNUqlP01F6LgWx4rIl-0uPHQSV9k4RDuKxBq4p_TEmeKleanpKiOkZCkPgC3bU_RJOJQ0Q6ysJgINOtiJafPBTVzPzOBHHHEBCrFhqd9nvU05YLBZ2-jSVBChwCnJuQkRAG5jprG3R4PFtBLvEEtJrP4EMr_PpgZ9_JnuKtOSS99OVZvH5uo7vpgtaV8_MabANr28Ika74bONGIRpNr237pjku9oJZhAuIC-jwCrwPe1r2WnXZmi8GCuxV_mdI0SRENSJsOXUMwMj5HOKAvwHr2AzcYccy0IG1bI7Qj84_n_5atW3GsgyjISxwVCkHTCfuzNiWIz3Dol8pDvkgTdftGMf3lwdT40dLpZDn3wDj8iK4RLxaTqhI6_rL3iCAafjtfTHknpO6annEATEe9AOQKkd0jnGxUtJkrhqHNfHReOjWX0ifGNKJBohSdpvBmP4HYxfkCzGwnZrJYYs4wPWJZZZ8qzyiJXmy2eU5QjZFHqxpldeTh_hfVsJdgG8CR43Tpr7EEej32sukG4U34j3xF9N5AasXuQBJNmSedUSXgdWqaHbvMmMeS83g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش اسرائیل یک تونل زیرزمینی حزب‌الله رو در زیر روستای مجدل زون لبنان کشف کرد که حاوی سلاح، موشک، پهپاد و گودال‌های پرتاب موشک به سمت اسرائیل بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/alonews/129722" target="_blank">📅 17:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129721">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bIE_vKQUAuPMjmqWdP9SJzJ25-V0bQaqzmlXdpCLH82jbG5Dysm0AbUM-ETsyLf_0OH_0xhCymgLMeCgS0YndB1-fTozp8aO3_SRqYG3FpTHAkJ_Xth1Tq9z49EufQsOtuXzPSklQnfvPxWBzIN7gddODak8l7IOAl-ZIrdwmCt34ntvQC_nez47BhnNmck4UmIHMQ-iwRexc3nUhoGTofzBVo4V1z8LaaG8SAuO4NGwuY7iqdQBYmHB4TvRx8Zk0EunzwwRW-Tqd23Hdx-hRqxT293dafuuDPcruIqRUh4sfBIvQUrzF6EiDYhCXKP3Qd0r99e4A7izFz39ZIKZyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تعداد زیادی از نفتکش‌های ایران و چین اکنون در حال صادرات نفت از ایران هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/129721" target="_blank">📅 17:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129720">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aebfeb0373.mp4?token=JQyqWTyetlmW_gWYFVCs6kmHrxJTzI5PK8fnYH4MA-xCgoGH9BhY7IOF46woyrGCav1CZ2KdjTTAqoI1f3BvZbNkfU1kOrsQAi1VGT_7ruwGfNCAiKiq7k9cl32dqt7FcUn21i8lJWk6x64d_PyTLfZlLNMrHZKOtGi559mCdRswyHLWUPxa5CvMGcN1HJF8YSqadHbsAWLdwxLwI00DjH2YrH0O1shmXZ1y3MfYoQAz4kQlGm4b2lXvhcdGDQmJn9XfhKLv5KiYrK4FZrdtehMOQBG32gkdhulLuHtOlSXA05lrleri7f-duYfksK7g5--Fw60ZR9gHqe4aQhJPgQVvV-zx09fljCelelvkWB0ZVpwO_k1dQqyj3asW-8bwVLSHakJGLrWV5Ni7CgjzkvZ8Ngt-qsPu4UdoxE0Rl2bDaxQn41ET_K8KSy9t8_8krnRRS7UxKJJMOCgoVO6XDJrYT1wST9CKkTj26UYDnyn_IXqdDlpCeeUHs9aE93bkaaTbP59PpFoCdn7M2uIgAb9HgCosWAh8g2Nemb_jqn2egglhPsiU2E0J39Wu0p2DFcynw3YX07WLffnV3Sk6xjxeVIaz6so7bBNaaAl60-oCwHP1Pqmb0X4Kl2pC_2FY1XVGGjD3-HATkozgEm8F92KPPzBwQ_Q9_t_v0SiGjJY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aebfeb0373.mp4?token=JQyqWTyetlmW_gWYFVCs6kmHrxJTzI5PK8fnYH4MA-xCgoGH9BhY7IOF46woyrGCav1CZ2KdjTTAqoI1f3BvZbNkfU1kOrsQAi1VGT_7ruwGfNCAiKiq7k9cl32dqt7FcUn21i8lJWk6x64d_PyTLfZlLNMrHZKOtGi559mCdRswyHLWUPxa5CvMGcN1HJF8YSqadHbsAWLdwxLwI00DjH2YrH0O1shmXZ1y3MfYoQAz4kQlGm4b2lXvhcdGDQmJn9XfhKLv5KiYrK4FZrdtehMOQBG32gkdhulLuHtOlSXA05lrleri7f-duYfksK7g5--Fw60ZR9gHqe4aQhJPgQVvV-zx09fljCelelvkWB0ZVpwO_k1dQqyj3asW-8bwVLSHakJGLrWV5Ni7CgjzkvZ8Ngt-qsPu4UdoxE0Rl2bDaxQn41ET_K8KSy9t8_8krnRRS7UxKJJMOCgoVO6XDJrYT1wST9CKkTj26UYDnyn_IXqdDlpCeeUHs9aE93bkaaTbP59PpFoCdn7M2uIgAb9HgCosWAh8g2Nemb_jqn2egglhPsiU2E0J39Wu0p2DFcynw3YX07WLffnV3Sk6xjxeVIaz6so7bBNaaAl60-oCwHP1Pqmb0X4Kl2pC_2FY1XVGGjD3-HATkozgEm8F92KPPzBwQ_Q9_t_v0SiGjJY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خب تبلیغات حکومتی تموم شد/استقرار ون گشت ارشاد در خیابان‌های قم برای حجاب اجباری.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/129720" target="_blank">📅 17:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129719">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pt-XcPFgJVrg66EMBVsQmfaardAbUyEOqz-KfvonLbWrQ3Mna8br8RmDLHwgTEVNqKBP0SQCEYTwSPUBxrH2UghPjYTbA1osHz2QBKnrJ3lvMdm1SfBxKLjnMKuZjpntO2oZ-TA5DGjx-nbK4ubWA96CZZ2eyMA46UQmy4J1E_BtHrHgQeJTq8qR7EYs405sQC1fcvmscLTNXaLpNaHBEi8ZzCF_UL4WHIlsPLXAGSbvYtdQ1TDnocAHIQZXVEshfkb0Es0gpGwIR0rsO4A1nqh2o8OkQlqwM0wiLnjeYwshjN_8aUdvMBFg0lgw22GHmZdCeE-emepP6QB1wiVw-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خارجیا دارن میگن قیافه بیرو شبیه کوروش کبیره و مارو یاد اون میندازه
😂
@AloSport</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/129719" target="_blank">📅 17:44 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129718">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
داده‌های شرکت کپلر نشان می‌دهد که چهار فروند نفتکش حامل گاز طبیعی مایع متعلق به قطر، امروز در مسیر ورود به تنگه هرمز قرار دارند.
🔴
بر اساس گزارش رویترز، نفتکش‌های «وادی السیل»، «مکینس»، «السد» و «مسیمیر» برای نخستین‌بار از زمان آغاز جنگ در منطقه، از مسیر آبی ایران وارد این آبراه می‌شوند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/alonews/129718" target="_blank">📅 17:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129717">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb6c5b042d.mp4?token=iMsIeK73mOkNLhP32aRVER4yma-6YBF8bLo02UqPO0HAEv6hTSyUKgfeqVsFMy8NldLjhZuFyxAVbfhE_YdCMjMypTu8jE7RpHBU7lgY-ErYKAfmkwmUorCmmfO6OPhkZFNRZm-3WcubJ8osgA1ku-5bIMe78uD30PUurryXNVB-CAE51Jx0eGkyXHUu_zD-3VRMcUmaTKJpKV1T8OAdQJ03QrU_8XpPEn079Zzr4OSgpgL0ZiQxOI6827QiHI0o2yF1CB2-tXXu_1XasUoVHzdCM6NwWMlG2iJq7rZJMKd8KP6HwfGRvw_-1_BHZKbe9Vwc2-8eQuNlFweIvF7UOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb6c5b042d.mp4?token=iMsIeK73mOkNLhP32aRVER4yma-6YBF8bLo02UqPO0HAEv6hTSyUKgfeqVsFMy8NldLjhZuFyxAVbfhE_YdCMjMypTu8jE7RpHBU7lgY-ErYKAfmkwmUorCmmfO6OPhkZFNRZm-3WcubJ8osgA1ku-5bIMe78uD30PUurryXNVB-CAE51Jx0eGkyXHUu_zD-3VRMcUmaTKJpKV1T8OAdQJ03QrU_8XpPEn079Zzr4OSgpgL0ZiQxOI6827QiHI0o2yF1CB2-tXXu_1XasUoVHzdCM6NwWMlG2iJq7rZJMKd8KP6HwfGRvw_-1_BHZKbe9Vwc2-8eQuNlFweIvF7UOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو:
دستور من و وزیر دفاع به ارتش اسرائیل واضح و بدون تغییر است: نیروهای ما در جنوب لبنان آزادی کامل عمل برای مقابله با هر تهدید مستقیم یا نوظهور علیه خود یا ساکنان شمال دارند. ارتش اسرائیل در این زمینه هیچ محدودیتی ندارد.
من پشت آنها ایستاده‌ام و کل ملت پشت آنها ایستاده‌اند.
من در موضع خود ثابت‌قدم هستم که ما تا زمانی که لازم باشد در «منطقه امنیتی» در جنوب لبنان باقی خواهیم ماند تا از ساکنان شمال و همه شهروندان دولت اسرائیل محافظت کنیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/129717" target="_blank">📅 17:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129716">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQO5w1mStEVLYzg-W-uFdDaO5Mbj-aQM2lnsxaVAZSbB3Gq6YgpVunIa3FVrRmDTSmrC1v3Wyjf-gvI1XYmWkuBVaEIpKlXhsjwpLV2lfholRTSqGq6bpPIVSGekzoFzAz_pmp8G3d10zKjVBIYemj58843JtPslNQUtSsT8tOqO3DDgZ0plnbgCrro1IimDpxBJ8dWDIZ1kqL9kjSC2rd0OTSLsWv5zGqsn1--03RqhGIo8xKVjVT0UVxRy6OSvIlUFa8iUVW7rvIw8XrbeuP7P8jgCUyGlCk67vQoPg2j_bLLsv5gO2w8HuOt7vbrBndUCzUw92WkN7WCdRMXlBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسکات بسنت، وزیر خزانه داری آمریکا:
وزارت خزانه داری یک مجوز عمومی موقت ۶۰ روزه صادر کرده است که تولید، تحویل و فروش نفت ایران را مجاز می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/alonews/129716" target="_blank">📅 17:06 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129715">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
العربیه: وزارت خزانه‌داری آمریکا مجوز عمومی‌ای صادر کرد که اجازه می‌دهد واردات نفت خام ایران به مدت دو ماه انجام شود
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/129715" target="_blank">📅 17:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129714">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
العربیه:
وزارت خزانه‌داری آمریکا مجوز عمومی‌ای صادر کرد که اجازه می‌دهد واردات نفت خام ایران به مدت دو ماه انجام شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/alonews/129714" target="_blank">📅 16:56 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129713">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0q4-eR-r2vXTFa2pcGyFcIJOA6L1J41zsYsdNMgYIt4Q8l4bXj7CbwN3aZBHLMMwMy8dODoSB39ffCdO1VqT7TqtgAb_l0DvjHErVq1SiW8JkpmisuGPSgHlY-F2aBk3f-neKxO3ghZEUB-wYVuxQpQmA2qFCJgDeWEeR6zWVM3i73TKfgCwNTj3TNAXYMSqSKO7OusVHq5Wwex17Ds0eg28Y3x_6eEVbrOLmei06xYMWXe2YzVBg8uIeGXJHMHIV0sAMruf3_iwbyKwbN8KUXKnpMZavrKueqY_lEvicnA74tr9Z8tNq6xRb1Or632woVGJLh3xczw635bkdR1Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم اکنون بمباران توپخانه اسرائیل منطقه المشعع منصوری و منطقه بیوت السیاد در جنوب لبنان را هدف قرار داده است.‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/alonews/129713" target="_blank">📅 16:46 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129712">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
مهر: تحریم‌های نفتی و پتروشیمی ایران هنوز تعلیق نشده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/alonews/129712" target="_blank">📅 16:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129711">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/981bb19642.mp4?token=Y__jc6Hmq_uptrEiu_CtRLu2wOprjL2ud2z0s_ZBxhNrcmJFAxflUmffRhWjiItE2w49kahUI3WrU6qxd2fUa79GQ3d_z6MkJ7et8vk2iAzYDDWGLg-Z9KvGTe2ryP3iPP8DS4NsztkNJNoFTrpQ1Ad74uL8GH6Ydeox_WhxiDtIh_iqTM6DhmL3g2Al55pnUPoQHAxsXOjjlS4yGYCv8b4ZKjnNTMT0BtIIof10U7hCInGmJ-2bXOJWHVHPdlqavcwgcbGkoLdMvintGXsMp_qlCsFLfx2NybkYG5YFRseQl63knzZhy1kVOF2mf2oLcjWlUIeJLEqp9YDT_4AIrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/981bb19642.mp4?token=Y__jc6Hmq_uptrEiu_CtRLu2wOprjL2ud2z0s_ZBxhNrcmJFAxflUmffRhWjiItE2w49kahUI3WrU6qxd2fUa79GQ3d_z6MkJ7et8vk2iAzYDDWGLg-Z9KvGTe2ryP3iPP8DS4NsztkNJNoFTrpQ1Ad74uL8GH6Ydeox_WhxiDtIh_iqTM6DhmL3g2Al55pnUPoQHAxsXOjjlS4yGYCv8b4ZKjnNTMT0BtIIof10U7hCInGmJ-2bXOJWHVHPdlqavcwgcbGkoLdMvintGXsMp_qlCsFLfx2NybkYG5YFRseQl63knzZhy1kVOF2mf2oLcjWlUIeJLEqp9YDT_4AIrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
از عجایب ایرانی‌های خارج از کشور همین که لحظاتی قبل گل میگفتن بیشرف، بعد که گل شد خوشحالی کردن، بعد که آفساید شد هم خوشحالی کردن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/alonews/129711" target="_blank">📅 16:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129710">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b975a3371.mp4?token=MOst8DZ2piPo5Yvq1DvF7QswfxuZCpuOMhvTbNNxPNL3ylcePDOKB-3CNrgtPPxIy73lFpwgRBsRf-pRu4R2sWz9JRSKJvcPdum09wZv3_cOZvbwgVwLi8HA-riN1q1X8VAlp5_uz425O3mib-x-uSNu3TPsGwyMMRhyECL_Zg27B7ZIBAPvy23DhDba41qELImIOIQxCREhwxgPv9dVKa2y-YWhey20FIg5r3dPMOBfjYwnDo-oWVejLC7vtb2JG9k0M8s8-T9GB7cEY4KqGnswWBeGmk5JtWnAN3xW0seWgKSneAiZfTZAJdabe9tzilnv3blXFdvMUzRHzAZtVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b975a3371.mp4?token=MOst8DZ2piPo5Yvq1DvF7QswfxuZCpuOMhvTbNNxPNL3ylcePDOKB-3CNrgtPPxIy73lFpwgRBsRf-pRu4R2sWz9JRSKJvcPdum09wZv3_cOZvbwgVwLi8HA-riN1q1X8VAlp5_uz425O3mib-x-uSNu3TPsGwyMMRhyECL_Zg27B7ZIBAPvy23DhDba41qELImIOIQxCREhwxgPv9dVKa2y-YWhey20FIg5r3dPMOBfjYwnDo-oWVejLC7vtb2JG9k0M8s8-T9GB7cEY4KqGnswWBeGmk5JtWnAN3xW0seWgKSneAiZfTZAJdabe9tzilnv3blXFdvMUzRHzAZtVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که بلژیکی‌ها برا بیرو ساختن
@AloSport</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/129710" target="_blank">📅 16:29 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129709">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
جی دی ونس: این توافقی نیست که ایالات متحده آن را به منطقه تحمیل کند، این توافقی است که منطقه با ناامیدی، از ایالات متحده خواسته است تا آن را اجرا کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/alonews/129709" target="_blank">📅 16:07 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129708">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J3D1wuZeNmd7LjTzMvw_dzFOkF7PQ6BzpzC8jYXmggAgLpotEygAjqCFlUPIP6Puf13l_MO341PAB9s7ib0-l7-G_29vzOkXd9RlLkaxQIISLX_yD4jImGIWWfB4eSslaGjSLCiH2QDrDFlYlHVU9Q118mSAge1jTjuaN3a4zraxHpktwjYlYiZznEaNyq2IvkPf6cMFwJ90_4fVq0YwxZ7A7haw_vH7mhrppCFosbp6Oqqa5DSQpXHC8126PPS4odwE-1VxR5vc7E7mh0v2U1Zye8a59Li7hItG3axFzSW8byDM1OBxPHX1NY9YyQzBoTFSYyb69mBJqu5xUD1-DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله ثابتی به قالیباف
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/129708" target="_blank">📅 16:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129707">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4efa68723.mp4?token=Yfn8LgTw7OkwFDlyI_HZjQQEVtVTV_4fHZBsby9rGRp76jKieC8uoKvJtxhOxqPRHDkpGoYHMkzVmq0ZKCvjaCLHWSREKP-d5_AlCl23kQbH36BNE1NZ6eV1Ax5QwvWFbIJV2TmiqUdyJu0MYXTa7uCI9IsZ6A18RpHteliEw4t6IChBppd_L-4T3zdIGgfURHAlYlrTDcLR5qJMdi8iC_ZH5pghwRsiT6q9vfvN6zCKfV85jKGZ7D4EF7s7Dc07_ldpggiVSR_k-fPLUzvOz6-9EmGe2P_pYT5wQRvympmVzB3hOCxLwFW4T-u69qfPXoZOlGmHDhCqECq-c23OHLoUt_Oa82fQIXYOfG5HlYielXK_0n76xwcPspvnZefJxm9FrIPrm2Hs0pLBHX8N-3iadBvG2EchzN0YlWNWS_Yd6lBrDYoMRw1wwr2ZcWhnMlfUWdWI3YsJowiBi8CkZNHSUBfBKg_Z-ePhfADugsfCUSRvtcIxD7lP5mV7a3FAtURxFlNmxiTrCKums1pDGA9Y-7CWpc_XDNzYGAUXsRjKIoMxMObz6va6jw9hGHCb8s1P7Xt38ek2EFwFpg8pjfP3UDHscPb97n41BIZ6sBuySksg-xltZx9WO7vDftF_BiISbRViIpFpeKGIHhHQItolDnJwN0TqozllvX0xxtM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4efa68723.mp4?token=Yfn8LgTw7OkwFDlyI_HZjQQEVtVTV_4fHZBsby9rGRp76jKieC8uoKvJtxhOxqPRHDkpGoYHMkzVmq0ZKCvjaCLHWSREKP-d5_AlCl23kQbH36BNE1NZ6eV1Ax5QwvWFbIJV2TmiqUdyJu0MYXTa7uCI9IsZ6A18RpHteliEw4t6IChBppd_L-4T3zdIGgfURHAlYlrTDcLR5qJMdi8iC_ZH5pghwRsiT6q9vfvN6zCKfV85jKGZ7D4EF7s7Dc07_ldpggiVSR_k-fPLUzvOz6-9EmGe2P_pYT5wQRvympmVzB3hOCxLwFW4T-u69qfPXoZOlGmHDhCqECq-c23OHLoUt_Oa82fQIXYOfG5HlYielXK_0n76xwcPspvnZefJxm9FrIPrm2Hs0pLBHX8N-3iadBvG2EchzN0YlWNWS_Yd6lBrDYoMRw1wwr2ZcWhnMlfUWdWI3YsJowiBi8CkZNHSUBfBKg_Z-ePhfADugsfCUSRvtcIxD7lP5mV7a3FAtURxFlNmxiTrCKums1pDGA9Y-7CWpc_XDNzYGAUXsRjKIoMxMObz6va6jw9hGHCb8s1P7Xt38ek2EFwFpg8pjfP3UDHscPb97n41BIZ6sBuySksg-xltZx9WO7vDftF_BiISbRViIpFpeKGIHhHQItolDnJwN0TqozllvX0xxtM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی دی ونس:
همانطور که رئیس جمهور ترامپ گفته است ، گاهی اوقات این آتش بس ها به این معنی است که شما کمی کمتر شلیک می کنید.
🔴
اما ما می خواستیم اطمینان حاصل کنیم که هماهنگی مناسبی را تنظیم کرده ایم تا اگر تیراندازی رخ دهد ، اگر حزب الله به اسرائیل شلیک کند ، یا اگر اسرائیل پاسخ دهد ، یا اگر درگیری های دیگری در منطقه بوجود بیاید ، ما در واقع با یکدیگر صحبت می کنیم و می دانیم که چگونه تیراندازی را متوقف کنیم و چگونه منطقه را امن تر کنیم.
🔴
ما هم اين کار رو کرديم‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/129707" target="_blank">📅 16:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129706">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86b2b64c80.mp4?token=iE4cfq6tcBxm6xFjN6bjhVHbUzVP3kslpITgwDXRfVdNhOD0byX7Xy3npWjils-E0U3E-V_gfxqXsQXQzFovUGJFHHH0B_WyuvOLYvJ34FJk2n5FfOSUnieQjU5c_CyzPLJijdW8GEwyMb4Jom3G2Qopo6u-c4fIrNh0vY4NFthoWdKkSgn1WC-hmajLuF7v7G9byfdBuQDZk4G5EKWDYAbirLnsji8Q6I8z5wlXKEP8sJ5nKWysjyFeSlgRwscz6nc_LsZU_T3VJ2S7eoc52Y3dGN5d0cQp2xBX_fYfKNwFg7jrjn9J6X5QCiqRkHGh9XDyMQnAQRp_2eVXkihmu4hKG-cgXlPGCSycb3q8xltV1SYOxpdaYKihTgZl6p5Bw9DQh5NjI6W-n4d-0Klm2qsyQLYxyRTk6vRUuWrogDBIMSQhIekVZES-EZ-cA-zyj0EJqjGQvwMJYDzyVTN-VmEa9OC0I73f6niDenwtafe5KhQ0k_YU_DWo_EbGd-DOCey4DmfL2D7Drz8uJvIEMbSSvnyJ1q8rU8TMziE_efKh7bJrb_IEhb8NX7n9m8eEgsCrpKQO5WPTFEIG8CmORtz2K_0hXoKj4bCSEKb-toginoilCZNiXIEzKxG8cIiWcuqwMHqSldhil2ZPZt24srmpn0EsvI1yguhW8fjKoIM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86b2b64c80.mp4?token=iE4cfq6tcBxm6xFjN6bjhVHbUzVP3kslpITgwDXRfVdNhOD0byX7Xy3npWjils-E0U3E-V_gfxqXsQXQzFovUGJFHHH0B_WyuvOLYvJ34FJk2n5FfOSUnieQjU5c_CyzPLJijdW8GEwyMb4Jom3G2Qopo6u-c4fIrNh0vY4NFthoWdKkSgn1WC-hmajLuF7v7G9byfdBuQDZk4G5EKWDYAbirLnsji8Q6I8z5wlXKEP8sJ5nKWysjyFeSlgRwscz6nc_LsZU_T3VJ2S7eoc52Y3dGN5d0cQp2xBX_fYfKNwFg7jrjn9J6X5QCiqRkHGh9XDyMQnAQRp_2eVXkihmu4hKG-cgXlPGCSycb3q8xltV1SYOxpdaYKihTgZl6p5Bw9DQh5NjI6W-n4d-0Klm2qsyQLYxyRTk6vRUuWrogDBIMSQhIekVZES-EZ-cA-zyj0EJqjGQvwMJYDzyVTN-VmEa9OC0I73f6niDenwtafe5KhQ0k_YU_DWo_EbGd-DOCey4DmfL2D7Drz8uJvIEMbSSvnyJ1q8rU8TMziE_efKh7bJrb_IEhb8NX7n9m8eEgsCrpKQO5WPTFEIG8CmORtz2K_0hXoKj4bCSEKb-toginoilCZNiXIEzKxG8cIiWcuqwMHqSldhil2ZPZt24srmpn0EsvI1yguhW8fjKoIM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی دی ونس:
دیروز روز خیلی خیلی خوبی بود ما پیشرفت های خوبی داشتیم.
🔴
ما دقیقا کاری رو کردیم که میخواستیم انجام بدیم‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/alonews/129706" target="_blank">📅 16:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129704">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc60009d0.mp4?token=sh1R8g0tUVZhbBFP8QFLnZ2y3fGTdaqARE5MHTM3hMKBQDptmXymBwEFn3j6-lQbWCrMHcXXSV3kSTO6mv4iGO2ELazzuZpZ7jqV626iRBFut0RcMuuoX6xNNeurP5NaJEc6jtCLS2N8cxY0WhuhNiYwqrrZd5Gj6lmZoIBA1bZ19LUlMd1ZqhfKFvs9SDP-8KL1p-M7T1d5uJhUUElJtCKaMPCAeOzmjJ-QbzVT6vp9N6QeRKxUudj8tI9V6kf_ZrnrN-1RiZxWuAyut14qkL2wfn62RjhfetvsLkwL1wWRhvrIcV7DP4j_J8CVwttlE7hQYfdUPCvRTHf7fmsQQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc60009d0.mp4?token=sh1R8g0tUVZhbBFP8QFLnZ2y3fGTdaqARE5MHTM3hMKBQDptmXymBwEFn3j6-lQbWCrMHcXXSV3kSTO6mv4iGO2ELazzuZpZ7jqV626iRBFut0RcMuuoX6xNNeurP5NaJEc6jtCLS2N8cxY0WhuhNiYwqrrZd5Gj6lmZoIBA1bZ19LUlMd1ZqhfKFvs9SDP-8KL1p-M7T1d5uJhUUElJtCKaMPCAeOzmjJ-QbzVT6vp9N6QeRKxUudj8tI9V6kf_ZrnrN-1RiZxWuAyut14qkL2wfn62RjhfetvsLkwL1wWRhvrIcV7DP4j_J8CVwttlE7hQYfdUPCvRTHf7fmsQQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فشاری شدن عوستاد خوش چشم از عادل
عوستاد خوش چشم
❌
عوستاد معکوس
✔️
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/alonews/129704" target="_blank">📅 15:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129703">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86a16e823a.mp4?token=XlEljJrMPaVFlmJQX5GwszILk-8ybJ4BlKV3mtK0QvSJ8jBFFWyfMmCjDTnOpVv0U3zG1KlR7wdkA6KAM1UKFhRB2nGQNalPK-SA_sdoK16ajv05r7aMhe_IYxKHuxC_w4klTnClfa1RI_-dp5kyPcYbamA_LcFjbZPoskPa6zrylFxGLz5zU8wNrobfQexKW037SPXmwDR5e_cjmkyMhsL2y9P6OkyAloz2PLjP0-DIyguEp5_Ls2zPS7_VsNgsC6NG92zFKYexVSPtXVyn-kdRHssyUDoD1EN7hxzldWSDB-kE39mrDcf_punaOJWiSucDUxUkCExFIzwxqAlfcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86a16e823a.mp4?token=XlEljJrMPaVFlmJQX5GwszILk-8ybJ4BlKV3mtK0QvSJ8jBFFWyfMmCjDTnOpVv0U3zG1KlR7wdkA6KAM1UKFhRB2nGQNalPK-SA_sdoK16ajv05r7aMhe_IYxKHuxC_w4klTnClfa1RI_-dp5kyPcYbamA_LcFjbZPoskPa6zrylFxGLz5zU8wNrobfQexKW037SPXmwDR5e_cjmkyMhsL2y9P6OkyAloz2PLjP0-DIyguEp5_Ls2zPS7_VsNgsC6NG92zFKYexVSPtXVyn-kdRHssyUDoD1EN7hxzldWSDB-kE39mrDcf_punaOJWiSucDUxUkCExFIzwxqAlfcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فواد ایزدی : ایران از تنگه هرمز عوارض نخواهد گرفت، بعد از ۶۰ روز آمریکا از تنگه هرمز عوارض خواهد گرفت!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/alonews/129703" target="_blank">📅 15:44 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129702">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
ونس : من نمی‌تونم ۶۰ روز اینجا بمونم؛
برمی‌گردم آمریکا، تیم‌های فنی کار رو ادامه می‌دن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/129702" target="_blank">📅 15:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129701">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
جی‌دی ونس: معامله نهایی خانه است. ما پایه را گذاشتیم. هنوز خانه را نساخته‌ایم، اما پایه‌ای موفقیت‌آمیز بنا کرده‌ایم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/alonews/129701" target="_blank">📅 15:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129700">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5af1ea714e.mp4?token=gpcwQgCRG9lni7UpGF_QYDO_BlIWlFZr3D1vpzLchoPKmtBpR0S3tPw5xj47qoOJ2GKLRm8bxsaIcvA_LHiTxZyLSRYgDoez49QIYJ4xFCPmbUkPaHKz2mesCw53xGJSdC8dTy93MirkylYM047aIUJNp8OLfhm3ve3Eo15G4FJDQgHQhjJA0aCpuJpsBWBdfcy-5vPQFt1ezBwyzu_oyaps4E8MvhGBMNMVxaXeE6tKYI9SXZUcQFrjgYA6fKD9JVU_7PJSGiT0RYCWyo4McSx2dy3Ats5HBP7kmVQI2MY23UnDp6xA9P2c3fdL6oNSRiJyGS_tYrS7EpSsHCTyTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5af1ea714e.mp4?token=gpcwQgCRG9lni7UpGF_QYDO_BlIWlFZr3D1vpzLchoPKmtBpR0S3tPw5xj47qoOJ2GKLRm8bxsaIcvA_LHiTxZyLSRYgDoez49QIYJ4xFCPmbUkPaHKz2mesCw53xGJSdC8dTy93MirkylYM047aIUJNp8OLfhm3ve3Eo15G4FJDQgHQhjJA0aCpuJpsBWBdfcy-5vPQFt1ezBwyzu_oyaps4E8MvhGBMNMVxaXeE6tKYI9SXZUcQFrjgYA6fKD9JVU_7PJSGiT0RYCWyo4McSx2dy3Ats5HBP7kmVQI2MY23UnDp6xA9P2c3fdL6oNSRiJyGS_tYrS7EpSsHCTyTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی دی ونس: ایرانی‌ها تهدید به ترک جلسه کردند، یا حداقل در رسانه‌های اجتماعی تهدیدهایی مبنی بر ترک جلسه وجود داشت اما آنها جلسه را ترک نکردند.
🔴
ما دیروز به ایرانی‌ها گفتیم: «وقتی شما به چیزی که ما نسل هزاره ممکن است آن را یاوه‌گویی بنامیم، می‌پردازید، نمی‌توانید انتظار داشته باشید که ترامپ پاسخ ندهد.»
🔴
وقتی آنها چیزهایی می‌گویند که حقیقت ندارد، ترامپ به آن پاسخ خواهد داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/129700" target="_blank">📅 15:17 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129699">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
قطر: مسائلی مانند موضوع هسته‌ای میان واشنگتن و تهران در حال بررسی است
🔴
محمد بن عبدالرحمن آل ثانی نخست وزیر و وزیر خارجه قطر به الجزیره گفت که با یادداشت تفاهم میان امریکا و ایران به پایان جنگ دست یافتیم.
🔴
بن عبدالرحمن در ادامه هدف از یادداشت تفاهم میان واشنگتن و تهران را توقف جنگ و زمینه‌سازی مذاکرات اعلام کرد.
🔴
وی اظهار داشت که مسائلی مانند موضوع هسته‌ای میان واشنگتن و تهران و مسائلی دیگر مانند امنیت و تنگه هرمز، با منطقه در حال بررسی است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/alonews/129699" target="_blank">📅 15:11 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129698">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
جی دی ونس: آنچه جارد و قطری‌ها و کل تیم انجام دادند، به نظر من، یک توافق کلاسیک ترامپ است.
🔴
اگر دارایی‌های ایران آزاد شود، کشاورزان آمریکایی را ثروتمندتر می‌کند و به تغذیه مردم ایران کمک خواهد کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/129698" target="_blank">📅 15:10 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129697">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
ونس: اگر صلح در منطقه اتفاق نیفتد رئیس جمهور ترامپ همچنان گزینه‌های زیادی در اختیار دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/alonews/129697" target="_blank">📅 15:10 · 01 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
