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
<img src="https://cdn4.telesco.pe/file/mx8GcXtAhVdSzQLYhWFAigUkwdsmLCPqp2TfDAaB6Q4fTOK-K_Kf3M6EgzHWKWxBMbRXks5WKspsWHvVlpO4cXSosm-OTitviP7KJoaIITwjOYSggnjH6y-xpXdGafzoccOkKJoqbicjyvxuLiJRaCjtxRlCF6bgd5SsKA_4hFpwxmpJzCP1s-JavHDLbc9rdemvcPKhlbUJAcQqsVNaVPmxYKopT6Yivg1sr6C7QV7SAqC8Th3GafGX27rVa8H124sS3k_28SgCEQf9LiQUxh1Qn4cNqU6oN9ybe_Ry1B-zdvdAp5JYUCa76cvQUdFDH7I4egEhjQSi6m4BjNiu1Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 223K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-23 14:19:37</div>
<hr>

<div class="tg-post" id="msg-82192">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">تو اگه منو میخواستی و کیرخر.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/funhiphop/82192" target="_blank">📅 14:06 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82191">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">7Khat – Maye Bede ( ft. Hichkas & Makhmase )(2007) - @SCDownbot</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/funhiphop/82191" target="_blank">📅 13:20 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82190">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Maye Bede ( ft. Hichkas & Makhmase )(2007) - @SCDownbot</div>
  <div class="tg-doc-extra">7Khat</div>
</div>
<a href="https://t.me/funhiphop/82190" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بخدا خود هیچکس یادش نبود همچین ترکی داره، بعد ممد ازش سمپل کرده
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/funhiphop/82190" target="_blank">📅 13:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82189">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ترک جدید ممد تونی به نام "مایه بده" منتشر شد.  Soundcloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/funhiphop/82189" target="_blank">📅 13:13 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82188">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iRybU_5qsPnsqtd2hbuKzv9UnDvCaOuEZHxNecUiWha0zwUfPcRkeUavUTGQPyu5kcAJcrpobLJU3SL9a4fJGbVhfr6-jvmJSiwoAuXgcD1QVZ1O1Xi4EdwPB6iTOUCVaQqVPvfDNY1GfT84oxw-n1f7UY5uGPsm-A9y-GZVlPQAe_0KP6p86K_DjvOpcHCftxnW_35n_eE38TaTnALL1y6e5Z8XNcaWwJKxqS_XVkplcuJIGSVRXUVZKbRPPqDIqPvW_J9NjFH4hQT-QgJlYPhj9cE_UvGeBY0G3rw5Hhg54UcpHSPc2XPun-w5TsK9YIHHGDTdVCWh8yOCyKzgCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید ممد تونی به نام "مایه بده" منتشر شد.
Soundcloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/funhiphop/82188" target="_blank">📅 13:13 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82187">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jO0X_RTtRlv4yLrKhqkyAXo1Zzx0Uiv-GARgs_XNyxrcfKXJkZou5pBdpdweSjyn9I5eqb3NrjPszj-OSnXqTR2GenSJsI5CYJxxWEqE6YQkXDYoygEI91jXlqbbOKtg68futtHqaqyg-mjW1IGuUnT1wwyC3l_05C7KBTvDI8poDce3KDe7EzH4hn6SR9Apw0hFtizYi0DPoNRYlbGvlSVef_6rtDdgZvONrDj8LWoupRwA2gWbOxuXJNBYuDS6dQcKpl4oju5uinLuAMlp9wYDj7wQpo7F5q6W61Mxg64JmtgVPiQl2vkxQ2l9azFnqGG5maHjZcufOlbZ_fa_5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد روبیو و ونس  ترامپ مسائل ایران رو سپرده به این یارو که در عین حال گی هم هست و شوهر داره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/funhiphop/82187" target="_blank">📅 11:44 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82186">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vQr4sD3iI3jTZ6o91qU5SNS32cPBkdZ2Gmw2u4ZppcAUshm014pzxtbZhF3RD3e398-3SMfXE4AEM9WcQkIZQdfBx10wV2R1zF-Gtf7VYrwQHY4KtwegXIEoGFj9PEUw62tC73ZkeAxMtoth2lEzJMva0ulvMTjILc-1ucmokfjmpL2lUTIr0kJDrM5Lm_Dn5lPy4h9MM2rWjiWyjGrF3OVdPcXyS2LpL9FFilMtmOyNvZi5y677ozk2t4QQJbyyMusi3XvCtnrMTvprUTToJcOrEJh-0eGSaKTviMYQ8eWZINHRKBqfWsPz78bUj3pVD-xXgMei_Mmm64qllJ-qsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون یه پلشت بی فرهنگ کون اینو نداره ۱۰۰ متر جلوتر پارک کنه و پیاده برگرده عقب، ماشینو ول میکنه وسط خیابون میره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/funhiphop/82186" target="_blank">📅 11:30 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82185">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tkKAB2c3glLYDpT1OUpY018g1qi6fMHmJ8iajTJAj7ua5o1O5VOE-tDoSxgE2o5lHYU5o0_yRtyrxv9lSPxEqV1ZQ5JQvupMi_OG6VyXNVqJ5WzT1-xVwCrVGAjGPyKp-Via6XoY63tFAKyQ97YKCD7o13PjHbccFe5rIizUWkV0tYvh7EaBR2c6I6lOhdBnxkn-NJiKb3EtsdTyUEprFXshLQuzCtGDeS4Uu5l4SYeTHCbSQQmxcqN0N0atM6lmJJ7eOVxRggir9xxnBV9JoJFCW2NLuFGaeXwCcBrLh_CCY0-vquxIDFqyo4Y6Wuz04hrXxxO7MeTUw543Obne-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
تراکتور
🔴
-
⚪️
پیکان
🏆
لیگ برتر خلیج فارس ایران
🙌
🕔
جمعه ساعت ۱۸:۰۰
🏟
ورزشگاه یادگار امام، تبریز
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز+
📊
نکاتی در مورد بازی‌های رودررو:
در ۱۰ تقابل اخیر، ۵ برد سهم تراکتور و ۱ برد سهم پیکان بوده و ۴ دیدار نیز با نتیجه تساوی به پایان رسیده است.
🧠
قبل از شروع، سقف مبلغ و زمان‌تان را تعیین کنید.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r23
💻
@BetForward</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/funhiphop/82185" target="_blank">📅 11:30 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82184">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OAgK5jTyzYRRaus0TXczZlGj3axbra2P-ytfFWx5P3YNMIsiMlOnEyHJWNqUHWv7mfHNUI262h8aKENBKkHPuyGVq9yh8E0TUJo3Lj-hUN8cwFEhv7RYcXY80wDv86wOrfVctiNvGsBPDGIMFH_Cgd2V_xMjVerC3M2ZmRIv7VbthhYiPFBbQ8J5jPTfYQzPSszNbML6juaKdYrUL3aQva6qNg2GA70XQzCIzeaMx3pMK__oXuuz_o5xqrvcj_acOuEzsba-WDCkYsUKXG6zgfV4atUrWM6vk16_FsSyr5y2X3tQjzRKR2Cm_zMu0qYD0JS-F4RAZe2oRvX__EBv2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز بیشتر پشمام می‌ریزه از ایران.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/funhiphop/82184" target="_blank">📅 10:54 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82183">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j791efj2N-kkCVcH43U2dqPBDb7ZeoU6ZwiqrhCYuJjoz0GioennyGOrst3Jn8eRCkTvhF0PtUHGYKUFQMKqdShUsXZcUudmkR6Zo-6Emv_9BvIlugH5N_kMGsBtm07ywv_jD0mfOAHLbN6wbcV9cF0wtyM30-teluqW6e7F43wKIRzUOTfxcdbmCm6VrLhxtgNa070GS7caJv-UiM3W-fJQEDkGGbkrXRVBlqvWNUt6AKUeUwrR16v55oCs9_PCaKDhck3sCGyzMC6Cg2iOA6twU8IuaTYWdt85QMAxP7SIfsYEr9hDRSj12PBsBOD_DCr5eYEu9TqYM1oCT2kwyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخدا که جای مغز تو کلتون ریدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/funhiphop/82183" target="_blank">📅 10:39 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82182">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/82182" target="_blank">📅 04:44 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82181">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ULBhW15QCQwWP_JeqTA15N4BVQlzX-DJitX7Oo56aLTtV0K4lXWMrJd9-1cWT88JUh1CdntrCrAb9Ik1ggBRqK0cV-CMgnvgexv2jPCw00N1PNbIzrtsWTP4NW1N67hOxsyLLbs5CMYLw-2OYJ01S4GNFEChoEA0G4P_nwHCVo48nz3moLAhymGgVj-48kAZV4VSoOnkmJFLmTTDtilxDX_WMteMH_SqF450Wt91uOgimt2AU_XV49e2Qn4I9GyOEtUF7JdXu41oR0mIvjnJADpsJBItMauu0cM3koXLauntsRTYHkhRjJ-z4_veqdcuEx-Qswz1qBK7AiS-XaAcXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من اگه رستوران بزنم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/82181" target="_blank">📅 02:51 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82180">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NBOKQHctaEEN1CivFE69SkS8YhScBVMzyaefIQyUCivesjgMDOQD9wNcPIomIBVLGI7ykfSPMlkIEXdVeAvEI_q0GPhLkYBlyWvM8dRhWH0nYgtV2Z7wWBkzEBTwIUAAvzWsNHxXlDVcdSUfbjNbliyVHT2FWMVu5x1kRUd33Y7ZkEUA1EzvRAJGe6mUzcPjfwmnXlLf52r3CusSGJORgKSqbgyC0Q2Oipv_lYI2w2I19kTquCxF0opcebx-_UjW8sHr95UnTg4iOSizwfg_JlHMktfUYw5KTLpIdoaGd9c6cG9viR4_TsmHVqiIIXcs11H30otu1yFtxmwndgc1PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوسه شکار شد
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/82180" target="_blank">📅 23:50 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82179">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NQTQGmgALQLnPYBOv_BznuKEvDe-Yx6ng7rfdZqgKwS63P9KXRh5UP9oqTeX-YPYB8eOx313xBoWYOhFwJS4V39d0REx631CTzcHcXX2-Q75zyE_E-F6AbYwu_LjzEZvV4EuBLPzys2ai0xIYrdsXeHkfvAAMKk8c0qn84QbQD2oftarctJYQUuRRpK6bQE9mbcHhnG-sgXnoiv826wsUwJFxV71oeKNhjlkgDDcq_QuKNaS5oGtRz_kO7WfFgFLoZsjBj_EqDYKZ2cphlRaNarJ9Jjw0Lkd0lAFQj4DRQ1gjeynGDQ-5wG6RmbzY8JoK2sLdROk2WRl6KpOjWoREQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیری پلشتی کیانوش  @FuunHipHop | Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/82179" target="_blank">📅 23:19 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82178">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5782494606.mp4?token=YxpJwdZfzl5-9JRJQDkt5OZw0zEWWxZohkhEz6vVxBhdwb5ZtAacy2FGK6YLoAKSde5tKJJKMP_pAxQkjtSz1eGIHaURiIB7xhO9bag1LnxPXwdIPTsa0akBsBmR9qjrYKqMhihFI7qlW5vDkC2qcZY_vWOQ0M7ku5AQuADogW5xKTCXjINAB3qH1J2KdPx3iqdno7iZpp2xuDSCP_xBl8UGXQZVZOsqLk2-6_oCgCdcoJ63g2f0DjI4VODuEWjkqedXlzi59by-S8N3z411T4xv6Osc4v82_-YA_Sm7gU6J2gVoO3AVmslzJeSEm5ld-aFRmiFrOI2kozD3yPPqKGmEtZbKvo6uuMV8b9BhLIhFK-giJL1YW4evdF8S52K0C4-ZcW8EK4ifw7LZaIXusYoHGgx1CZI3dY2lGv0iXHocCRRwTJjpPCMESRYIrZwWTDOT2Bwz7JYawrS9ulzNnD3az824j73Qr6Ch9eAhI4MIwvXQoqSTbmArSMMNbRLC_YCN6nPHWHQLQSiNUUz5_6KxoesWZRCm5UUx3B_UQ92jU1QcHwVohrU3tRZ6CQotPmJhUexI9tbzlf3p2p6YLv6WKBNc6695nfnep1WgiDSbFQ2JDtTOtNvJCTm7T_FrW85EOQ3S6YapB1sB6K9EKkrL-4Z1svqEM67hvhtEf1o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5782494606.mp4?token=YxpJwdZfzl5-9JRJQDkt5OZw0zEWWxZohkhEz6vVxBhdwb5ZtAacy2FGK6YLoAKSde5tKJJKMP_pAxQkjtSz1eGIHaURiIB7xhO9bag1LnxPXwdIPTsa0akBsBmR9qjrYKqMhihFI7qlW5vDkC2qcZY_vWOQ0M7ku5AQuADogW5xKTCXjINAB3qH1J2KdPx3iqdno7iZpp2xuDSCP_xBl8UGXQZVZOsqLk2-6_oCgCdcoJ63g2f0DjI4VODuEWjkqedXlzi59by-S8N3z411T4xv6Osc4v82_-YA_Sm7gU6J2gVoO3AVmslzJeSEm5ld-aFRmiFrOI2kozD3yPPqKGmEtZbKvo6uuMV8b9BhLIhFK-giJL1YW4evdF8S52K0C4-ZcW8EK4ifw7LZaIXusYoHGgx1CZI3dY2lGv0iXHocCRRwTJjpPCMESRYIrZwWTDOT2Bwz7JYawrS9ulzNnD3az824j73Qr6Ch9eAhI4MIwvXQoqSTbmArSMMNbRLC_YCN6nPHWHQLQSiNUUz5_6KxoesWZRCm5UUx3B_UQ92jU1QcHwVohrU3tRZ6CQotPmJhUexI9tbzlf3p2p6YLv6WKBNc6695nfnep1WgiDSbFQ2JDtTOtNvJCTm7T_FrW85EOQ3S6YapB1sB6K9EKkrL-4Z1svqEM67hvhtEf1o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قابل توجه عزيزانى كه از رفتن خانم کارولین لیویت سخنگوى كاخ سفيد ناراحت بودند ، مثل اينكه ايشون مى خواد بشه سخنگوى جديد كاخ سفيد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/82178" target="_blank">📅 22:07 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82177">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iocFO8DbP67uy7T5czEpjnm8rbnMD6pYt_lPyeoQygNAE3_54u78Rk2cDCfSIaxQUdsjC2wWBwJYa8-mVv1q2C1-ro0KX5WtE8jZXigCw_5tyMK5xof8xeaxqc7Aon5N4bwYaW0NM5VLLtmgUfrhPy8qLDlgOWL9cqrpe7uTLcerXDFMp95hvY38iLlI_roHU44Zbhp4KhkWbVh-0zU8MPiV-LJng4TvTFGllhDkOAtj7QnUJHwS4C18a3KSm96FCCHEiFr09B0cm2wCVT9T9Qe94kFSMLl18zMlcb3stKKriloGT6N2r2Y2zIdWdTaD5DA4Sx4r2d0z4Y1Y6ecqfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید ویناک به نام "قبلنا" منتشر شد
YouTube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/82177" target="_blank">📅 21:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82176">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/403c217675.mp4?token=fVobeB9eWSrBKRJFTBGTyHfaLLO-WrBO6Q1JqWqYq8iE6zJ35SnSnhksJWQCZNjZjwSuCx2GIbYohp_gdtgIeN0t7LvBAhQrSemHESgpsEt7QPKpB0BYrPy1X-KVsQ6w3D0qvdd5qSeKsOCGJar9zBuR_cZmuGco6zCeVnqv_xTs1oVcjbU8muoo8tQ_05QsHQLCFAEcoTAHql3phctm1PL3JcT2g2Ez1JyFe4ErzgqpAx9imVsBv0vPzSkfTuTCXBLqcV6QWANoEqaC7zLfu8mbsutYdLYUd6mt3vqIwp9Zvxn_qPvSmPhZ9fc73-fBlpAVOq_7nAjEV4ZogQqvtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403c217675.mp4?token=fVobeB9eWSrBKRJFTBGTyHfaLLO-WrBO6Q1JqWqYq8iE6zJ35SnSnhksJWQCZNjZjwSuCx2GIbYohp_gdtgIeN0t7LvBAhQrSemHESgpsEt7QPKpB0BYrPy1X-KVsQ6w3D0qvdd5qSeKsOCGJar9zBuR_cZmuGco6zCeVnqv_xTs1oVcjbU8muoo8tQ_05QsHQLCFAEcoTAHql3phctm1PL3JcT2g2Ez1JyFe4ErzgqpAx9imVsBv0vPzSkfTuTCXBLqcV6QWANoEqaC7zLfu8mbsutYdLYUd6mt3vqIwp9Zvxn_qPvSmPhZ9fc73-fBlpAVOq_7nAjEV4ZogQqvtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آروم بخندید
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/82176" target="_blank">📅 19:34 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82171">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mh0Ugk0BP-ww1e_W3Mqj4zrDmjwPaEg85GzO-u0ES6wYgnlslrAc1Iywbbi6Qr343VPeYB1AsZtSl5FYRiY_K3FoxfC2HtAtLOKMbvGp4AzZNBzIlxCqOkFmFho9hA87rr9AXDqMmnnvEAr5MeFPxnLB2rVhwMuZ3x5nUdQcd43Y0_IWjIsaVDaRYW0T1tlfNkD1VBDLOrTki42Rt9FMSBwraU2qG6kOSaKXMkGPyRHpkTf4lPbaMRHi9zlYiPJFLa7JPlZ6vvHIi-BcnafFk2PMz8QjZkonL6rV8JaCvaDwnNAEsz2RzD164x-SnyeFoi0VrXGyPLWMa5YXn3icug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R0NmXbTkahDlJI-ruZ0_SljfCW8JhpMHJZNDXKz31l6F4pXt-ng6seZQrPrFjq1BXy7lMpRGHEY9XAHzHnJKc4ZeAD-fncPLc4vAoOLfnT-sxwSCIjDQDhGUWJE9cyOxR7xIqlyzWevrqT5eWUKhy_0Vu7Eo29FfMMuPCMmQPMdz5editbUxCb-ynCsxeqhqRuGJrFI4_eTN8eUo_C_1zo6nbLr6uFzD5hkh3C_kq8N6rgWULD_8Y1EM8zMir3iTwf_nckAYayx4xidMldzAIphN9NWtZL0I4LW7xDBdAnALRlKTxbiizk1X3JbkjRyMuq32U_-lrlql-t8sTxB19A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DdyKgs0_Ix22KX3Vn_sAkBs1UD9ul22nYGwDieaMgbFD0mmVHYodt7J-Eblw4Aos9caGVjXOE_1FoMPBMpsAwU01lcA2gkodYVyaLaOU8UE1b6RneApFZh9qwY0hjpCTFFC4fHzoyRjL_PbVphyAySMqdca-_yxmTD_bHo5y6YrOKZ4ky2YOVtNuthXvrjoMqGSIQARHxMl2iWHstY6gJ6emdobRWTCdX8zI7HcoNrDAwV-QNvpD4kSIzlQAgIa9dvcWJl8SO96TzYxuzZu1lw4V5Kg0JVETxxTO-TqvYUPL53i1KuVlUwO54pxJOz7CVWanvLt3ofqvZiSLkRwEoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OpuHfARbMaqeRuX-K5FL1z8TjsJoPb7mffUyMxnvfqI9xpfUe_8Z9WT_zrHBKlr5bl_GYmThPNwqhGH9PWA5Tn4kTOvL_etLvyxHc9k0TU7Y5LM4nPPHgcvUf_Bq8H85tMwi75-v0q1sbLTiPOQjPByItrXZOoWEA4necxMgJOqUogqhDbcP7pW_LwcJzIk791iEMnT0jAuAot2fC2LQqCEJxG2BSsTCsQ3gIMeNrRgxgAxloA09vceefrsmFiuwAGdeHHlTUiAweTyv3YSsWdouOQbzZuSZj6B6zgN5o4lFeQh82XBhVqAMKMqdBbjF52YZavWHO2tm5GSa3QPN-A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3aa705dcf0.mp4?token=aa583E_oOognq4rjYh7NpXrXZYliBSJ_z450S5Lf6fmPfCpE-BW0MiEiujglWkKkGu1mZtrxRr4WX2YAwNVHAXY65xpbypjrBJ7YdjbGv5Dqn3E3xXp9r0_fqHsmD_nOhemQIpp9WSoYOgwOh957H0w93sPLjOWiVezjTeDATR87zqidf9NMFmZ4pwInrhV5e9FseFdbKuwS7rpH8c-UlBGSxcwuE9N3UmxlRvfnIHhgAx4bUquPFGDFdwsKHnp8cvkE9cdkFdufPcjsbSMCS8WjJOD3iUAzjqS0aNTgcZcZ8N8XPoIik0tjkc6DfJruuhdvCPJSs6h6BFe40IDHBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3aa705dcf0.mp4?token=aa583E_oOognq4rjYh7NpXrXZYliBSJ_z450S5Lf6fmPfCpE-BW0MiEiujglWkKkGu1mZtrxRr4WX2YAwNVHAXY65xpbypjrBJ7YdjbGv5Dqn3E3xXp9r0_fqHsmD_nOhemQIpp9WSoYOgwOh957H0w93sPLjOWiVezjTeDATR87zqidf9NMFmZ4pwInrhV5e9FseFdbKuwS7rpH8c-UlBGSxcwuE9N3UmxlRvfnIHhgAx4bUquPFGDFdwsKHnp8cvkE9cdkFdufPcjsbSMCS8WjJOD3iUAzjqS0aNTgcZcZ8N8XPoIik0tjkc6DfJruuhdvCPJSs6h6BFe40IDHBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کامنتای اینستا واقعا جذابه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/82171" target="_blank">📅 19:25 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82170">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RZc9c6cMt5f6P_jTPld5coap-fjKXzZ71TtTCnvdsPgF9kJ0JkRhKgUtSODawVCcP9oorzJzfYHjNOTxJrc4HHlExtrbTp8i52RsDHjp63mcrLaXku0kD2h3JgbG1UBSGh409mMDd0SA_WLvBlLlZDMlPPhaEh68L-VX-s7MLGsaDz0R5J4obYnWm4PWkLGhiHRaWNhHpbZ82sjFnx7jSxfYyS7IUmaDJ0XQQOvnr4zMbVfw_wO2s7guQ4XOiolG3mEwcdkYnjLAXzYaaWuZMXQjmQKG3npw8NJn2JTRf_yoBV3EPX1ox2U41D5O7LBslMkm8ypzaJaJgrR6rY7Jag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خودتو گول نزن ارسام کیر کاگانم نمیشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/82170" target="_blank">📅 18:53 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82169">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">پس دابل آلبوم و این کصشرا چی بود
این چه کصشریه</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/82169" target="_blank">📅 18:26 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82168">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">بزار جیبت بیبی</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/82168" target="_blank">📅 18:19 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82167">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ترک جدید دکی به نام "بزار جیبت بیبی" منتشر شد.  Youtube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/82167" target="_blank">📅 18:18 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82166">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ltZM5wQ10uVMdntH4Qu1m-AsdvtZTq37J0LJx_XiODEQzfEG2sRiOK3ATeel1d8E_Ne5sPxXcPAhsGRKRM5l2tfpEo8W5N-IkcxegZgWkAm7aZoPJFXhPPMNfX8jMB4ePga4mlq6C1KVU4dP8z4VTcysoChFMJgeORYKB4kHwOh8MIaxtE94umQYIoYAT3fZHzTPTSfqDP4-AnS-nJv_RkQUXky0RgDSsLKCIRLnj2knIYr4axzFWJ7S24IosMWVW03Mqy3gY3LtbvskxF3ohpsMxQVTDsxet35wJOt755velCKZerVT0_AItl4H5XvpUT-SvE9CR736J298qTZ5Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید دکی به نام "بزار جیبت بیبی" منتشر شد.
Youtube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/82166" target="_blank">📅 18:18 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82165">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gkjjUXNw48fGMEiA_dLwILZ1CynLFjL_TpCbpglgKAFP-i66dtdCwtws4N2DgS-8nHmQNEhUJgN-OQY8GOhc5gEkVmB-pBn-3B0rEkbM1sQ91wh8N5_JGqi4fQfBgK2SBQNPRDzZ-MIqQDzvtwC4HEJ6AOxcOYnBBa6u_iB7yqO24wwWxlKEDffdVIydZPaXQC1RShHSxHNrH8uZuxXwl6f2yr6WIx0L57uwexCp8VP-iOuKtjx1B4QW8JzcawFQpO4csYkis6D4lzStqjPdyI5_35aS18LF7-zIrx6Tog6h2-z46CHvQyFryd5iZjM_QIlSwMk85EzJuam535GBjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
تا صد درصد بیمه ویژه پیش‌بینی لیگ برتر خلیج فارس
🇮🇷
⚽️
با ثبت حداقل ۵ میلیون ریال  پیش‌بینی میکس بر روی رقابت‌‌های جذاب و تماشایی لیگ برتر خلیج فارس ایران، در صورت ناموفق شدن نتیجه، بت‌ فوروارد با توجه به مبلغ پیش‌بینی، در هر روز از رقابت‌های لیگ، تا ۱۰۰ درصد مبلغ پیش‌بینی را به عنوان اعتبار پیش‌بینی رایگان ورزشی به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bfrd.link/PERG100
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r22
💻
@BetForward</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/82165" target="_blank">📅 18:18 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82164">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">کاور ترک جدید دکی اینه احتمالا
😂
@Funhiphop | Menot</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/82164" target="_blank">📅 17:55 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82163">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jUbHpT_kNx3dYPex5xMqdZtNbcjz9EYVWHLFq_6ZyYzzOieIiSDqG4LB1sC32KALm8maE6C1fzGtEugBwvOsdCTundabEO4FKuGO51bNjdsN9258QGW9fFN6mPWqAbZMEbwKj6dQpd1-ZSBVhJUO1e-ILYtTjumY4LosBbXNPNtixZYKGRr-qK2cWgd1lKBIJSrzV2c1mLTgr1-JdvU5cjk1KYJFt_AGv8V1XKTTyFXG3h7aCkfvppZFpbbOcHGEoffuON6udAqL_weaCXYCbAuXEizhjpoy7TVOKnexjwmh7zUmm_vxbIrpWj2VFeMVX7lzE9wOzP3m0UcaQ9WXpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاور ترک جدید دکی اینه احتمالا
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/82163" target="_blank">📅 17:54 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82162">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4c7242a55.mp4?token=ibcAWDenwhrep3S_9FGeHdomuN0X7BWHWVnuexdpxxgGdkjARqE_PyOcS1CJz1kBHzMr8R2gRHf_mEcuyPejejo0-ijBph0ejaQAb98SIJux6Sl4rRuhvnr0tv0xZSmgdWBtrRI05svfU7t6Y-_PusoQ4waisqpnv_TE2z4noSQfJwNaQl6iY24WjY3vnJrSpT1pX-TI0dV5ea6wC3HpEAAmNuhHdRe7Pj20za_5MSNe-KHgd7vMgV4mps2Omfue0Sbmenc_pitVzBmpUZihS6n3CjSern1A52iuHPOzeawgBDX9fJFRQHR8m5y1v120Ax5zlyRc1Mnw8iQOBUjysw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4c7242a55.mp4?token=ibcAWDenwhrep3S_9FGeHdomuN0X7BWHWVnuexdpxxgGdkjARqE_PyOcS1CJz1kBHzMr8R2gRHf_mEcuyPejejo0-ijBph0ejaQAb98SIJux6Sl4rRuhvnr0tv0xZSmgdWBtrRI05svfU7t6Y-_PusoQ4waisqpnv_TE2z4noSQfJwNaQl6iY24WjY3vnJrSpT1pX-TI0dV5ea6wC3HpEAAmNuhHdRe7Pj20za_5MSNe-KHgd7vMgV4mps2Omfue0Sbmenc_pitVzBmpUZihS6n3CjSern1A52iuHPOzeawgBDX9fJFRQHR8m5y1v120Ax5zlyRc1Mnw8iQOBUjysw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/82162" target="_blank">📅 17:11 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82161">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a59034baf.mp4?token=l1sCns0lv0lXArw24NJLtzzDnGQ8APxFbBn6Yxq_C4CuAq2E1HNaNBqAoybnY9tjEt9LQrUyH6R_LMeuOPX1BasiJMZSu3fRzEupFyE_C6n03PyNtY98Z6Sdn6Zi9VaGBH3MQzAbJWPBYfk-FthQbHzR1rPe-yHNUZGcVz-Wkp4erEmLL4M_Nl3BhnB9bo7IFa_MKYRNVsGLnc5f3x7t667EmuMwJACpC3aWgmbZ0Zeeyq1XifBhCneNPLgQaMUIEnms9oFJf8dF--O__TkxSzosF27ezYKnrlUVBJ-Zo-FchLh6CcwIvidArZkxYEztEQmxm6OwgDCeW5J67b1NTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a59034baf.mp4?token=l1sCns0lv0lXArw24NJLtzzDnGQ8APxFbBn6Yxq_C4CuAq2E1HNaNBqAoybnY9tjEt9LQrUyH6R_LMeuOPX1BasiJMZSu3fRzEupFyE_C6n03PyNtY98Z6Sdn6Zi9VaGBH3MQzAbJWPBYfk-FthQbHzR1rPe-yHNUZGcVz-Wkp4erEmLL4M_Nl3BhnB9bo7IFa_MKYRNVsGLnc5f3x7t667EmuMwJACpC3aWgmbZ0Zeeyq1XifBhCneNPLgQaMUIEnms9oFJf8dF--O__TkxSzosF27ezYKnrlUVBJ-Zo-FchLh6CcwIvidArZkxYEztEQmxm6OwgDCeW5J67b1NTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بارتوش کورک
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/82161" target="_blank">📅 16:06 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82160">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">سیتی خداست، هر سری که تیما اون پولی که برا رودری میخوادو میدن میگه نه ده تا بیشتر، خلاصه قیمتشو از ۴۰ میل بردن رو ۸۰ میل
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/82160" target="_blank">📅 13:41 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82159">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IsnRbfI05GclzhAAtvLTHLB9nrVAsSGMkoBLDcvid0i54qy0m5rIXONfXiGSru6R4GocKoETTmLmmr4AAni11mlwzsT3wjdFnhld_y5py1SgBbNXYYSVARga-Y8Tq1Zj30jknWhh1Ww4YtBzuEoaWtkSQdruAdSKEbZcTCAU4GjSMLna9IvCS4eJMmRgty2uEBbCdE73SvXD5ERzmlt_BTuxyc2mBYIbXdi6mPTc2XJMwixqn5FmjfLu-34GJFkPeziJUb-LLCU37KEreAl8q9DyJiX1NsnOrB8T0EHVM143qteR3YATbLk-HFSl0Sl8U7M1ifKIpP46aFNxbPolkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تصویرو هربار میبینم جمله "آقایییی محترمممم" میاد تو ذهنم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/82159" target="_blank">📅 12:40 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82158">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CaVz4S98tMsFy9EFT72e_uS4bba5DGKhOWnlgDmNWEz1-OjLvs5_2mk0UvYPu82wOLrTGdvB8T0eiQto0RLsZVVIvM5pqUIZ8gi-fdJGhKg3_NsAktqMCWWTQKfJ7evCRfMEZgAmx9-4PVtBhbvJsIKimIJOxMsb9E5pgoTGFg-ARvDI-CrtisC1Mddy9mu2Nc4NEXHti1Q35RuHMK6QwQ6H5uv-X7tUkF_CRWOKHHpf-L9IbbayIInyPJ8Y0OQP08XI_T2lLuuLIMc-io4bbZYP63IxeRbZg-nYMmt5gXqa8QgpbhvfTXmNS9vx2s7tJokXmCZBXa8ATS7OK4pKvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خفه ریدم تو سلیقت
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/82158" target="_blank">📅 11:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82157">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e23ac6b2e.mp4?token=DbPu5mLSAZf0f9w5Mr5mUsPjNb0HSmlFKnTNTVSM8BJbEtqW6vaQgHpdcxW7NaMF44reZA40FhJUE3oN4MQrKQDhabJmRaqeoETzcPLs8q1sHyWqA9yvDkrVkAN7dv45JnLtPo4gXwOkjdARxe24l9sNmJmEWsjqM1KuxPywDcepI-kXzmqzZsKZS1-DRFpRTZRpnDgRkTQ6UnBQdYv7wByqIs1TNnPiVUcIyC1jW469jAhLa6LsHV3Il_-k4WP8VBaxsJ3fqYyDrUkfgpNj8PcZFjyCqhqJSxnTeQBs_4ahJTUP67gIClyKYeWelji933KN6p4A52fg3iihbyIiTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e23ac6b2e.mp4?token=DbPu5mLSAZf0f9w5Mr5mUsPjNb0HSmlFKnTNTVSM8BJbEtqW6vaQgHpdcxW7NaMF44reZA40FhJUE3oN4MQrKQDhabJmRaqeoETzcPLs8q1sHyWqA9yvDkrVkAN7dv45JnLtPo4gXwOkjdARxe24l9sNmJmEWsjqM1KuxPywDcepI-kXzmqzZsKZS1-DRFpRTZRpnDgRkTQ6UnBQdYv7wByqIs1TNnPiVUcIyC1jW469jAhLa6LsHV3Il_-k4WP8VBaxsJ3fqYyDrUkfgpNj8PcZFjyCqhqJSxnTeQBs_4ahJTUP67gIClyKYeWelji933KN6p4A52fg3iihbyIiTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سم آلتمن مدیرعامل OpenAi:
احتمالا تا ۶ ماه آینده، Chat gpt بتونه صفحه نمایش موبایل شمارو ببینه و بخونه!
به این صورته که کارایی که در طول روز با موبایل انجام میدین رو میتونه تحلیل کنه، مثلا وسط چت با پارتنر یا رفیقتون، کمک میکنه چی جواب بدین.
یا اینکه سر کلاس آنلاین، جواب معلم رو چی بدین؟ حتی می‌تونه تماساتونم ضبط کنه و وسط مکالمه کمک‌تون کنه!
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/82157" target="_blank">📅 11:03 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82156">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tu-SSRXZapPILfvYy7Fc7WxHM3H_-TNXuD-xcrtzv1vTa43JXQX8A0G7AkFrfc61Ffo3loG9XWsP-6awOEP6KOWLZNa2u-bzTWvUSW1B9CtF67LUITBeGs95XwDNg27Nb7fmKbyMqaZJuGDR13suqgAq-wdGBY4oj2RJIH6zq6ONT7TdkJbu8R_ofxWqy9RfXa0PXJMOAi04RwCgmoStaGdCC7UyjNeVqeh-Q-AqUQiaaYLUbV4rI_sVdCpTESYpgoHNPo7TlgfFeBG7CYXLSrrJvTwFIFlzu7MmxYUMUhrnBopQQ5FtsQqIrvsqve-3dugSt5RuGPqaMjv4NIzZuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
تا صد درصد بیمه ویژه پیش‌بینی لیگ برتر خلیج فارس
🇮🇷
⚽️
با ثبت حداقل ۵ میلیون ریال  پیش‌بینی میکس بر روی رقابت‌‌های جذاب و تماشایی لیگ برتر خلیج فارس ایران، در صورت ناموفق شدن نتیجه، بت‌ فوروارد با توجه به مبلغ پیش‌بینی، در هر روز از رقابت‌های لیگ، تا ۱۰۰ درصد مبلغ پیش‌بینی را به عنوان اعتبار پیش‌بینی رایگان ورزشی به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bfrd.link/PERG100
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r22
💻
@BetForward</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/82156" target="_blank">📅 11:03 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82155">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b33fe099a1.mp4?token=TpOdVZmDFDT8J3Fc4dZ5jg0PMDnEb-9ROuubf2_dvTk75lF_Wi4Zobf6wUqQO8S_LmHf8qX4I75BG7l-cRRQfIMDhX_zYxc35JQoSsw-vfcBUvim5JZ7-MysiAQ3VZeJcdNmmNqdhLgD_MUv3cWRTX37knGMmnC2W3-dyl3UMUaUSY_EQoSwJHJJcEKB-C912yn9qKsS2-9C9lbp7akwjSepuz-awqB2ZdnwvgmcAcyclVBpCdti3OylqrK4J-rHmmFwofpDG8_p8OxblOon1qNjJ0GadiyNjoNeJpiLahhqEe7U0vlrDg8G4gM2dJLuq2X2oxwT-eP0WGV4ZTy30g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b33fe099a1.mp4?token=TpOdVZmDFDT8J3Fc4dZ5jg0PMDnEb-9ROuubf2_dvTk75lF_Wi4Zobf6wUqQO8S_LmHf8qX4I75BG7l-cRRQfIMDhX_zYxc35JQoSsw-vfcBUvim5JZ7-MysiAQ3VZeJcdNmmNqdhLgD_MUv3cWRTX37knGMmnC2W3-dyl3UMUaUSY_EQoSwJHJJcEKB-C912yn9qKsS2-9C9lbp7akwjSepuz-awqB2ZdnwvgmcAcyclVBpCdti3OylqrK4J-rHmmFwofpDG8_p8OxblOon1qNjJ0GadiyNjoNeJpiLahhqEe7U0vlrDg8G4gM2dJLuq2X2oxwT-eP0WGV4ZTy30g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاید براتون سوال شده باشه اگه سندی چت کنه چی میشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/82155" target="_blank">📅 09:20 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82154">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">یعنی نتانیاهو با اونهمه قدرت نفهمیده پوریا زراعتی آدم جمهوری اسلامیه و بردتش اسرائیل و باهاش مصاحبه کرده ولی چارتا کصخل تو توییتر فهمیدن؟</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/82154" target="_blank">📅 08:14 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82153">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">درکل فیلم قشنگی‌ بود بشینید ببینید بفهمید تو چه کشور گوهی زندگی میکنید
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/82153" target="_blank">📅 03:14 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82152">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fe5c5e708.mp4?token=Q27CjRzx4c_i5mXLNG-h4_MyfirnywJGGAg2VCIjXELiQj56HFVSN0rSYX5byEMBvY8MXwc6soWLB5ZWnCWqw1yb1tFGFXrXaezUW8Q_pEf8Orvwb3nnts9DZuA-WqmwbpsV8ThBwIjhdl6AB97osAf2s2VesS-QGWSNgiSZB4366VYRnzbpDA5d_RcU9bTFmbhXwOJ1my1pXcDWi_AOYRJz6jfkNRx91TgDJDYafPtOdLKXSUsmYYqTTDX4x0uPPZOljIz_zrYiHo9YZEOpcv2bO6RUXZF1YWbRgRX2c7-TAJwc8mrKsokgHwID4g0t3gWlQV7q-o9uMdkN_atuRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fe5c5e708.mp4?token=Q27CjRzx4c_i5mXLNG-h4_MyfirnywJGGAg2VCIjXELiQj56HFVSN0rSYX5byEMBvY8MXwc6soWLB5ZWnCWqw1yb1tFGFXrXaezUW8Q_pEf8Orvwb3nnts9DZuA-WqmwbpsV8ThBwIjhdl6AB97osAf2s2VesS-QGWSNgiSZB4366VYRnzbpDA5d_RcU9bTFmbhXwOJ1my1pXcDWi_AOYRJz6jfkNRx91TgDJDYafPtOdLKXSUsmYYqTTDX4x0uPPZOljIz_zrYiHo9YZEOpcv2bO6RUXZF1YWbRgRX2c7-TAJwc8mrKsokgHwID4g0t3gWlQV7q-o9uMdkN_atuRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیداد خوبه یا همین سه چهارتا تیکش تو اینستا خوبه</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/82152" target="_blank">📅 02:52 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82150">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">بیداد خوبه یا همین سه چهارتا تیکش تو اینستا خوبه</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/82150" target="_blank">📅 02:20 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82148">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uFxnZZVKRNhQ8YNlHzwLSbC3C-q8jEh0hoHeq3YkLJO_4Vg71-S31a-rFcwAckpnpHsIZN4tBOGjT3GiBV9DvsxlfplXqpuw40gbrwQazUkwqIUzj5s2qW_akc7ekIJFIQ_tE9VA25m2bvHAV72WqCnTvR3pzp1JTc92-YVSfgMVokhiC7K-1xR-OF4pKL0X7ceGeGKz1rn_LsUXNfUWKP1Bbnmkb21M5Oyokrd1xkXEzrVxJu_uIK9E1INEBc9vHYhKv4Oxw3apIElHX4f9pePF6OOjeDzM-UE8tYO75kZGuiJaAcgwZoHnblN2-ubh3Ln3fI-1oeb2AvrYWgXWMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf0e2ba89a.mp4?token=Cqhut3N7YcfGjk0lSdmw8nVC-vFJNvdJlMHTzW0YXnZaOj-BNFXvJUxYvsRnPUA7Bgv3h15MVqu1Sk7Tm3lwhGupOH9vdm3_8gE0bOf6XnZBOUxjcRZAoP6vo3saxUZM8dpOV7jgwGcQfpUiTjEFKq8P52K2BsSl4mbar-6Akka33VahV_GqOF4WJgpXMI55Y_g4kj_Hyt71BAi2fGphI5SA-8N1yddKuqdhhyRgCx5oVjjVLSp51eLwjLS-nca2E2cquPtHgozGFfeCSIVGpIjU1LBO3cYVOTUBrj6SdD-4Zfs0QukEFfrs60z2BF8cdfY31Mgt74GEKHuBI491KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf0e2ba89a.mp4?token=Cqhut3N7YcfGjk0lSdmw8nVC-vFJNvdJlMHTzW0YXnZaOj-BNFXvJUxYvsRnPUA7Bgv3h15MVqu1Sk7Tm3lwhGupOH9vdm3_8gE0bOf6XnZBOUxjcRZAoP6vo3saxUZM8dpOV7jgwGcQfpUiTjEFKq8P52K2BsSl4mbar-6Akka33VahV_GqOF4WJgpXMI55Y_g4kj_Hyt71BAi2fGphI5SA-8N1yddKuqdhhyRgCx5oVjjVLSp51eLwjLS-nca2E2cquPtHgozGFfeCSIVGpIjU1LBO3cYVOTUBrj6SdD-4Zfs0QukEFfrs60z2BF8cdfY31Mgt74GEKHuBI491KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئال بعد دوسال جام گرفت
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/82148" target="_blank">📅 00:34 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82147">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/umr5fqNh0o9Oz2oDE3pKD07inYmLGtljblGpFTpiUrpG3d2EwAIaUulqeYspYbJUaoxHn5TPpn4LspyL-ETR7zHSN2Lqt0vt1GVFyl1PoU2r0Tj_gjf03Z9jYLLi28wHcVq1w2ytrjhJHkK7vylSFuF3DoBB_kV6O5Cywc1DAh9MH8uG_iPYC4fNnmfgtpm1lx8NER-0F93ztpSf_j7s5pAlWFPiQVCkxUfj3i6gnwo96JBlACMYGaMJR7YwVByYIUAFdgByy6kYaoQh2P-woC2ONOAkU4jmzcEMD6cOw-d9Xg-NnR3hz_R_Jw9Ux3jZ1cENfGT_aijwnL_ewHQL7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اوکراین هم عده‌ای از گیمرهایی رو که مأموریت هلی‌کوپتر GTA رو با موفقیت گذروندن استخدام و مأمور کنترل پهپاد‌های انتحاری کرده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/82147" target="_blank">📅 00:29 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82146">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">پاول گیفت تدی تروریست داد بیرون
🎁</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/82146" target="_blank">📅 23:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82145">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">کیرم تو توپ طلا اگه به کسی جز کوارتسخلیا برسه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/82145" target="_blank">📅 22:52 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82144">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e9VdPw5RHgbDjER-gHmOolAqsghzrOULAhOaPN_Nd0UGyz0bHkN-jjLagy-pZz-YAwQTzZb3WpSR3v_wFL3tQwShVCeM24yR4jNOj7wrDAPPVvJMW9Fwx-h-TQzGmZjdUfpEQC5pup-YPm57O2-gZmttESH7_ZIXQn2tz7BhNq8KtXXVc5J2Gz_1IbWNCsp2bhG_FXrqTXCBI-CyX5bfJxfRvKhZAeBtfJeOnwQAFZtbL5VHhr3n0WeOyuKkx3wKOBUMy1pLU8AVTK8YlCMiuP1AB5DDIzKYvrA9rlUV-ue-8xaSUWsx4FF8ryxcPyN5gUaBiuoMJCXkAB4sWg-ROQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام به قدرت جدید فوتبال ملی اروپا, هلند
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/82144" target="_blank">📅 22:45 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82140">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">البته ما کی باشیم نظر بدیم، چین برامون بنزین میخره</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/82140" target="_blank">📅 21:58 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82139">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">موضوع سادس، نه میتونن بنزین تولید کنن، نه پول خرید بنزین دارن، حتی اگه پولشم داشته باشن بخاطر محاصره دریایی نمیتونن وارد کنن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/82139" target="_blank">📅 21:53 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82138">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">تورو ناموستون شما دیگه حتی با افغانستانم نجنگید ممنون.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/82138" target="_blank">📅 21:41 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82137">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">داشتم فکر میکردم ماشینو بزارم خونه با مترو رفت و امد کنم یادم اومد کلا ۴ تا استان ایران مترو دارن</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/82137" target="_blank">📅 21:37 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82136">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">قیمتا دقیق:  نرخ اول: ۶۰ لیتر بنزین با نرخ ۱۵۰۰ تومان  نرخ دوم: ۵۰ لیتر با نرخ ۳۰۰۰ تومان  نرخ سوم: ۴۰ لیتر با نرخ ۷۸۰۰۰ تومان  نرخ چهارم: ۸۷,۲۰۰ تومان (نرخ آزاد)  پ.ن: فعلا این تغییر نرخا مربوط به ۲۰۴ جایگاه تو کرمانه، بقیه جاها اعمال نشده  @FunHipHop | چمن…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/82136" target="_blank">📅 21:35 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82135">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">قیمتا دقیق:
نرخ اول: ۶۰ لیتر بنزین با نرخ ۱۵۰۰ تومان
نرخ دوم: ۵۰ لیتر با نرخ ۳۰۰۰ تومان
نرخ سوم: ۴۰ لیتر با نرخ ۷۸۰۰۰ تومان
نرخ چهارم: ۸۷,۲۰۰ تومان (نرخ آزاد)
پ.ن: فعلا این تغییر نرخا مربوط به ۲۰۴ جایگاه تو کرمانه، بقیه جاها اعمال نشده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/82135" target="_blank">📅 21:33 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82134">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">میگن دارن سه تا نرخ بنزین "۱۵۰۰ تومنی ۳۰۰۰ تومنی و ۵۰۰۰ تومنی" رو سهمیه ای میکنن (۱۵۰تا سه تاش) و نرخ آزاد رپ نزدیک ۹۰ تومن میکنن، حالا کاری به این ندارم که ۱۵۰ تا ممکنه برا خیلیا کافی باشه، تکلیف این ماشینایی که از زمستون ۴۰۴ تولید شده و سهمیه ندارن چی میشه؟…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/82134" target="_blank">📅 21:27 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82133">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">میگن دارن سه تا نرخ بنزین "۱۵۰۰ تومنی ۳۰۰۰ تومنی و ۵۰۰۰ تومنی" رو سهمیه ای میکنن (۱۵۰تا سه تاش) و نرخ آزاد رپ نزدیک ۹۰ تومن میکنن، حالا کاری به این ندارم که ۱۵۰ تا ممکنه برا خیلیا کافی باشه، تکلیف این ماشینایی که از زمستون ۴۰۴ تولید شده و سهمیه ندارن چی میشه؟…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/82133" target="_blank">📅 21:16 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82132">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">میگن دارن سه تا نرخ بنزین "۱۵۰۰ تومنی ۳۰۰۰ تومنی و ۵۰۰۰ تومنی" رو سهمیه ای میکنن (۱۵۰تا سه تاش) و نرخ آزاد رپ نزدیک ۹۰ تومن میکنن، حالا کاری به این ندارم که ۱۵۰ تا ممکنه برا خیلیا کافی باشه، تکلیف این ماشینایی که از زمستون ۴۰۴ تولید شده و سهمیه ندارن چی میشه؟ کدوم کصخلی میاد به ماشین ایرانی بنزین لیتری ۹۰‌تومن بزنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/82132" target="_blank">📅 21:11 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82131">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">صبم خلسه اومد این ویسو داد بهش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/82131" target="_blank">📅 20:27 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82130">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">مگه دیروز تو البوم فیت نداشتن</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/82130" target="_blank">📅 20:26 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82129">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">کچی میخواد به خلسه دیس بده</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/82129" target="_blank">📅 20:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82128">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bWB79NTKoMVIc0MHR3WW0QvdYmv4Djon21dUt0Ki415HnJt31uI6EL7qnwiTIbJ7CBpJ8SO2C6l24b0EyzcoxMRMRkdoNvAn0MeM-F_Hm3vdL4KiSCfjY1YiTU6ThB59aqTsOp-axGXMkH195tJovUxPN7_-G7FDMRBH3LRqy7lexrFV9Q_246o5W53pWSVwb1SNU5P7LGvJZJIKa1qtGNOzi6FVftQ1PMV1JAX257XoHWF9G6KY79AAgod9FyBtXhaEKUPMAsDRaa9WAe6t-WTAVZkSyzNaxdAnk4fzXUzWJSBlnRxxYcC_zc4HQZeewGlQJDvdVGTGgzRSe7hNGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یادت باشه اولین چیزی که توی استایلت باید بدرخشه، موهاته.
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/82128" target="_blank">📅 19:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82127">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4765f0c41.mp4?token=MI1wDKEeIGa6fDGJc8NLCb6wGja3gYptZZtrEkL9JgLfTyyk7m2JVs3kDzj3S1jSdNg7JzZjLHhzWDYziwZTakxP67scCvg4RHSd1q98hHrBYcJPseM7v3M1F5LBrDw7OPl0iA54S2eA_5XzoiafRxzxYPIOklwgi4f8fTQQnfZciH_7kPrNe93HZ-llmHxj_rajZbwhqa2FXkxngpGGgWVg5-2BswheSq8-KePukvjZguc7IgP_rEqo2vUSRYoo00zPBk2XocYvtAZTvCw4iaDGtbO4Tal5ri40pJHk4Y5I5K8QkNN6qPf7O4uSDErtKrRVJkcnYAgtoS6fE_OqNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4765f0c41.mp4?token=MI1wDKEeIGa6fDGJc8NLCb6wGja3gYptZZtrEkL9JgLfTyyk7m2JVs3kDzj3S1jSdNg7JzZjLHhzWDYziwZTakxP67scCvg4RHSd1q98hHrBYcJPseM7v3M1F5LBrDw7OPl0iA54S2eA_5XzoiafRxzxYPIOklwgi4f8fTQQnfZciH_7kPrNe93HZ-llmHxj_rajZbwhqa2FXkxngpGGgWVg5-2BswheSq8-KePukvjZguc7IgP_rEqo2vUSRYoo00zPBk2XocYvtAZTvCw4iaDGtbO4Tal5ri40pJHk4Y5I5K8QkNN6qPf7O4uSDErtKrRVJkcnYAgtoS6fE_OqNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
زاکانی، شهردار تهران:
موشک مستقیم به طبقه خونه مجتبی خامنه‌ای خورد!
خانمش (زهرا حدادعادل) اون روز سردرد داشت و نرفت مدرسه، موند کنار همسرش و نهایتا ترور شد.
مجتبی خامنه‌ای خودش هم مجروح شد، ولی تو اون شرایط دائما دغدغه نماز داشت.
با وجود زخم‌هایی که داشت، خیلی مهربون و خوب بود و توکل به خدا داشت.
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/82127" target="_blank">📅 18:57 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82125">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rtaVotNFssGAxG_nmSR52xLhIBCQ6ojgXdIRj3gvrlcEl-HihdaLlVz6tLitAvrvlUHtOCHyJBjHrbNKwlNYU8YTwq8kz1fV9p0LD2_vThsD-fRLHnk1xJ-92j6kjli4TWP2OLUdu51vCiE7MuGZ1zF0lSGBNaC-59dZYO-xcQt-D4BVa7w3b2QHwCXWq6TeJ-8MWyN9OrUPjvskGz1GDocZoiLsHHSg6w0M_ATa0XHarbQYRfWxsApLH5KpAgOudd8fUlV7IokJvsbW016quglbvxTO6kM5hhTS5Kzn-7rtmaDQTcBOqfHcz51MNucRD6moBbhT-Wski83A3wtWKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلنوشته مسی برای پدر:
اینکه دیگه نبینمت و نتونم باهات حرف بزنم، واقعاً برام سخته. میدونستم روزای سختی داشتی و رنج می‌کشیدی، ولی اصلاً فکر نمیکردم اینقدر زود بری. هنوز کلی چیز داشتیم که باید باهم تجربه می‌کردیم.
همیشه دوست داشتی آخرین جام جهانی رو بازی کنم. چند روز قبل شروع مسابقات حالت بدتر شد، ولی من ادامه دادم. رسیدیم به فینال، اما تو دیه نتونستی اونجا کنارمون باشی. دلم می‌خواست قهرمان بشیم و جام رو برات بیارم… ولی نشد.
واقعاً نمیدونم بدون تو چطوری باید ادامه بدم. حتی نمیدونم تا کی قراره فوتبال بازی کنم. تو از همون بچگی همیشه کنارم بودی؛ منو می‌بردی تمرین، بازی هامو میدیدی و هیچ‌وقت تنهام نمی‌ذاشتی.
خیلی دلم برات تنگ میشه، ولی میدونم همیشه یه جایی کنارمی. راحت بخواب بابا… از اون بالا هم مثل همیشه حواست به ما باشه.
ممنونم برای همه‌چی. دوستت دارم بابا
❤
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/82125" target="_blank">📅 18:40 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82124">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QDLOESF6PZ1q5fNEojYRCkb0TPUF3wCVmkRKARYKiRJ7TaCBzw5tt8BgS2F5C6rKz7525GYjnQMnWlpEdyR46yMq2IZOqXHaIgfwhby-cbQcZ1r62OX5APcGUgL6fTyzygqwM80ZsQHEDwWLO4qHGvMbC64VAjWJvEISgU0GQ3jqPyA9isWGS1inxxM5-4E-ybcFzNy-H9K6t_6o8o0s9jsRcXtFY760GlyXfGvw_-HWWhXJLwFLIJLHIgSG3F8_34_EIxOXU4lptQXk2FTlDnFnMSDsk8tbEJwkCN5mmTPl8x_T0LSEGWm_29_5S0bVEEJYCn8umeACR60ZW9bb0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدی دوس دارم بدونم کی این توهم هارو بهتون تزریق میکنه پسر پوریا ادرویت به سپهر خلسه ویو بده؟  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/82124" target="_blank">📅 18:29 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82123">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ro48CarygLIRSP3XxjZs0E3D8fvhI0HSN0oLG4AnHan1szbWHPmrUsTPaw1-SAjfKzW7EBHt86XqDrk0P1rOo10Q7z-cvimYliW1fyjsEZBfqNxPEbmPCVqewKZLFcOkd1th6xdZQ6F5fcHhOatkhrvTVlizPT2czV-u2wWtbneT3lFkDQpeCvIZPq2h5m9wpVlQTH6mAaLpZPcv7TZFoJjcxfn3xYQLOWBDsdcVZGDpRQWUjECZoOyNwAbZZsOMmm8LG83z6jfC4VSAwog9Wk9aE6SRE8QPGXEzFUFXhzWXghHac95E09qWBmCUZVrpuwnFXA1jx-7G60QwbW39gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدی دوس دارم بدونم کی این توهم هارو بهتون تزریق میکنه پسر
پوریا ادرویت به سپهر خلسه ویو بده؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/82123" target="_blank">📅 18:19 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82122">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xgpyn69m0WJYv8aF8uSsit9ztaABhHP_GDmFx5bwODtZ9l-jz02GjMjRUJgQjhUcxCLeBQ3PDhJWt_Cq470W7rwQjj6wcpY3W5Pi8cmvXF-pVqScRPykg9McsJA9hDvy4eriAvPCa8e1K3TQAz8KzUE1duYVpqG6UIG4HMX3it0suTLwTjzJ0XN1VFr6Y_oXOUYGgn_pN4e31IYR7Yh_Aa0u_mnrQsFgDguVsR3MdFMjk6Zt6J9CmbSzalkpnk2DWLXZzN6ifBRqg4FhTBMELFzD8c_ISd9ILFaWS5YS2n0wiANr2HF50wnObGilmDS3MLmRydZ8yJ1VxN8-EkjFDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راستی، این یارو که چتای ملتفت رو پخش کرده یه ریکورد هم از پیوی مهدیار پخش کرد که بهش عکس یهویی داده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/82122" target="_blank">📅 18:02 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82121">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ترک جدید صادق به نام "گواه"  ریلیز شد.   Spotify  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/82121" target="_blank">📅 17:50 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82120">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wf_ilD6ELWFD0IvbZSy0R9DQdMNJX9cnxGZa4C_padMasLYQl89OSPZV93qD3I4peaKtXknCxPMb2FnDsPqosh398mPM5uZa6zLGxxsqE64iL7eMNWkyKJiLNr69dKaPfYGUS1r7hznD7v0XYu5nx6sjOUeVmfarDcCc7fj6Ob2ztVT_cxBttwdUO3yIxOWCNWjzV0CDOUDNneeWSeoyaQUNz5Vis9t292dWmJyf5FdUUnhyq6ughgapWrE37Zr_RckLa9pdBSegrXrZHfliSIIlOioC61dOQdhKYKVjKvWZhN_ul8B_UoyOmo1Qhn97DeoBRCxp7TkTGbdm_QuT9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید صادق به نام "گواه"  ریلیز شد.
Spotify
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/82120" target="_blank">📅 17:50 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82119">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">خفه شید عشقم آقای واحدی ترک داده</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/82119" target="_blank">📅 17:48 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82116">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DXXMzPFepQ1q56vDDQByh3pYhhlZ_WPll7Q7xxwt-YU-mo_M8QuRVMgrxGqamEa5SOm43uGnOnoAqyBRUoxz3Ixtgtb5EjduNZBYwd7hxlVtklJvOuIhwvvN498NX_WPYZiYcjkSslh_OOSjJZHeujcHSwnhUAMrCKPajVCiWVULEm-KiUKpYzzQrEkqVHEceA2K_R0Tqlg7lUrtlh5lHFNi9-rlTHIUDAkQ4c3mFsC5wUjuddldjTp7msLoyC1dzS6r4wjZW3mzszZtidngiD1pkeJdlFG-NnZi416CD5uN7rkliWNYt47iBP5-d2srD5_V2ksrT7SGggHAEoSt6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز ۳ تا اتفاق نجومی قراره همزمان تو آسمون رخ بده:
خورشیدگرفتگی، هم‌نشینی ۶ سیاره و اوج بارش شهابی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/82116" target="_blank">📅 17:28 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82115">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZVMfAw6-Cl9FK5K5V_RDTs1Vw4ceXZp7OyfTglE8PtepfKv38FkZ2okteO2SUCL16YPZwDc23SXrr9vGY933Ekg_1o_vbzYrc4NxT8nqKzJZ-Tjln-bG0VFvqF7jIX9yOQYTn_9muMUa9LHf-JwyulKoN2eD43S7639WimVZxjlfK4t_8SjlnwFXcxLfUmPdv-zVDY9JA7qpRKCAbUhLUeb8TbbcgP8sfpd3rNSNDDZW0aRKlEzkFBPLM6BkvLJ6PyullHwot5FgR6nQwFitupVWVwDPY20Du4YdACqH45Rehr008xxN3IXXibYr2IfhVAiztX9n76aboSHmmxpykg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونالدو فنا و مسی فنا باهم دیگ دوست باشید
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/82115" target="_blank">📅 17:14 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82114">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pkYdAP6GpiRseXnPT5h_4iPEwVC63IFVj1ACXLy_NPo8AEJlY3jRJN5zTEm3AbzFtDzXojHTTXXZdY0nwEyvWPRo8bNEXQRRXXzrJsESh81SK497o7ChQUIwzYABNas_lUjWjocVwV2nGrJoq8-DEO1bdZKDC_uW1QJM47oz_EAQM9d-3Pszp5mk85SKu7AC4H8ZPJGl6yJoqj5ybmH4M_L610eA2oxDm0nKssve9wXhlEytiSPd2h4szj00IgV36P5AOQ9FJdfVYhSzHLYchlr_uwdxYdezWnXDEShjrIik0RvOTDN6BXK4zRgKLzy2jRXgKgEjg1a5x5oGSe78tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خورخه مسی، پدر لیونل مسی در سن 68 سالگی بعد از یک دوره بیماری سخت درگذشت  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/82114" target="_blank">📅 16:57 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82113">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">دیروز دعوا سر این بود که کی کیو فید کرده، تا خلسه اومد و نشون داد دود از کنده بلند میشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/82113" target="_blank">📅 16:37 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82112">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">زاکانی، شهردار تهران: موشک مستقیم به طبقه آقا مجتبی خورد؛ همسرشان، شهید و خود ایشان مجروح شدند.
پس از حمله، اطرافیان قصد انجام اقدامات درمانی و بخیه جراحت را داشتند، اما رهبری در همان شرایط نیز دغدغه اقامه نماز داشتند و یکی از حاضران از آرامش، مهربانی و توکل بالای ایشان در لحظات پس از حمله سخن گفته است.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/82112" target="_blank">📅 15:16 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82111">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ویسای خلسه یه جا خطاب به خشی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/82111" target="_blank">📅 13:19 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82108">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">وزارت خارجه پاکستان:
پرونده میانجی‌گری بین واشنگتن و تهران را نبسته‌ایم و امکان تمدید دوره ۶۰ روزه در یادداشت تفاهم وجود دارد.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/82108" target="_blank">📅 13:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82107">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uP2tapPJmmE85lw53uBxlnKk3ozsOYDma5YZAMzcb1OV_kstNWHB4_ooBPJBVrOceQXCPdkPrQDV2-PaX7gAs_1BTakWVUtputKhHXnk9gxRjrwKmVzaC0W7hk5mAgKzsIH-J-OAEwuNnNMkEWYHxU-Gcglv_xjcG6l2lqEeHXu025iWu3fLpOukqoYNzeESsPxYnZ5eze12IIWX1cJNe1TnJt4aZyyCmYKkzO8M_Ot7-9sS9MiANEvxi85KnzPz7YeGb9pUOcIjSykd4oAOe8fpaPsgcbdrLkYuReRUPKeVViW688wI1P0XyvgoYYhKNcKvJNF9PWQqOBRZVTfHkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونالدو به مناسبت عروسیش یه قصر چند میلیون دلاری زده به نام خانومش
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/82107" target="_blank">📅 12:09 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82104">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dW7wfWnZSyiudgF4VFR1BEk591gYN92BK22RO2SLBPEhSoPRU0DScI7Fy4EoxpSrM0NI2PGztcyBprSQdZSBwCcGGU8QpFgtHg1fgbjvLsM03ZIxa_yTzdZF_HItkY-ztTvMDwLIDMSzrpU1Zh1QMYdMGUKytEmXYk-2EXhbsSa65pu11SOCoaCk7YB53CrQmUpLb_4UyY9O6sRVbavImnMijtnrjHewH2ApIxNnnIcpSHYTuNnolUmWLxzgiP_eULlk12mNZhef0ESdLSc5cv7P1cA8PD5Hyxor4sGdKkwIAz7xv4_lNQoGu8lnYSuVhJzWPg8h9M_xpld5jM5MhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EKMTWej1RKuIDI9qkfnYuW8JoWzohLku1GrjRCZunFd3CNAvcHP4HfdIfMK88hJXDtycjXCmqrPvqrIxOgyXkhdFj0k7YgbrW7nuT8uR6U7Efq7omViLR2f9HApK-1bwEmPTsIcU9WxRVtG4g3WkYgcOpqcyqITQeGHKf4HNtkZHKmzBVj9Q6axNglUCUy5ehdN0Cyami9PjZmMoGCRtyj-nN_KnE3UsRDCUcyH-SFAG0ssNXjfU-cc1RAP1LwYDuHxS7nP4ppfQEEglak3gLrKEDMEvJfhbyiN40DsjUxduAojjR75AysuwvSHkvRFKr_Mud81vtOL_TnaPxhOm7g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پسر شایع نسخه مینیمال خودشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/82104" target="_blank">📅 10:16 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82103">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2be999c32f.mp4?token=LOm-VvcQ3HWP9eVKW8X-k8ZxLGpnNdNlnIoMZTYbUOp6w0Tcf7UdDpsTW9IcMVGPry1zz3JpVF8B2AWVYJkVLm6qJy2ynDUOFoOxrQrQFZq8dfto7CbqP8mFMiLEvGvf22X1kl4mX2sHzQmsp0U6zb6eP7UXj0bln3NdemiItnBVWEKW9zW2mICv-0cqCxW-82r2uJUL6xZc3lXYcpb54sGDNu0VssqLzS-_0TCXLCeM89hpEC-VzNG0rEikZ5L_YnLy3lX6Wr8i__xwTgtAdSRnJZfyzUUMobA9E0AiMzQkQZSi9OLz4eKE-DXGq3wiVoAaEoIOcoKFcxiCsloxcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2be999c32f.mp4?token=LOm-VvcQ3HWP9eVKW8X-k8ZxLGpnNdNlnIoMZTYbUOp6w0Tcf7UdDpsTW9IcMVGPry1zz3JpVF8B2AWVYJkVLm6qJy2ynDUOFoOxrQrQFZq8dfto7CbqP8mFMiLEvGvf22X1kl4mX2sHzQmsp0U6zb6eP7UXj0bln3NdemiItnBVWEKW9zW2mICv-0cqCxW-82r2uJUL6xZc3lXYcpb54sGDNu0VssqLzS-_0TCXLCeM89hpEC-VzNG0rEikZ5L_YnLy3lX6Wr8i__xwTgtAdSRnJZfyzUUMobA9E0AiMzQkQZSi9OLz4eKE-DXGq3wiVoAaEoIOcoKFcxiCsloxcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تروخدا یکی از دوست آشنا های این ببرتش تیمارستانی جایی درمان بشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/82103" target="_blank">📅 02:29 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82102">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">کیر تو بارسلونای بدون فران تورس
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/82102" target="_blank">📅 01:25 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82101">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">علی گرامی به کدوم قبله قسمت بدم دیگه نخونی؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/82101" target="_blank">📅 00:14 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82100">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmir</strong></div>
<div class="tg-text">چشماش دنیام بودا
دلبر بی ناموس
🤙
🤙</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/82100" target="_blank">📅 23:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82099">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qlMndw_EhMaABeFitgvUgjXTbXQ51PotSV5kDzAo7ExehWh5Fvp2qCn4HhXG8zfmXC6J2sMR0y2pBWqKc9y9T8Ta0MgvFc_zrXUs6UFAf2PtoZGiVG1Wq1Gqdy2g92ov4fzrfsexthEuoDE_fUzMOyQYgZpfU53i2zobTz9qOY3XkrAxPQ7oZxYClfg8n0uV6ZooSAVxrNSx7HWS8omnjBMOnD7zJhPWbWv2Sxwt4n7Zh2JKLPbfAZcrpFvhceRHLKBbiP1N3vVG6Nw9YFNy0vcRfpqsKb9b04J4MIMdCkVt3BD0Yrr_eYSu__YhO_MfHVnqRVmIQ_aeHASEpSTlaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این عکس فقط یه کپشن "حسبی الله" کم داره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/82099" target="_blank">📅 23:17 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82098">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNoah</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B1pn11jD1uzyXt2sxnc-QHWgEPHw53omS8z0EtT9jeOfS1ujbN8-ZfXytn9PQlM0EIuzdioimcorBAiHYw-MV87IawCr3i5WF6OmITBSLikj56XkxvKZKwLr3fc-HjlsNHptER2QLU7D4TsvMI2vh7RsG_AxSSeu5ucyMcaCB9aS1mgxuKcZseBGt9Fo6JhDjtLnk5P3nHrMx-l63MdVZWQgzT5P0XRvag-nTMMhbRk6km2XAWhuvERFEuKvs1ZJgUijsqxNxD4L7gDNuP0HwoD3fnqSR0OmYN4Ldsx3O-qWS-qvMA1tp6YyKd-5HbYeCrNeFHhK-oW9egejvN-NuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونالدو حرومزاده یعنی چی که اسپید رو دعوت نکردی به عروسیت، من بت زده بودم روش</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/82098" target="_blank">📅 23:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82097">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q1sHmuAc9iOdLcU_qhlTSuE2GqUPmcQQQ_LW1Rz9cm4FIv3HdhZUV1GjY3m4u4UhRoaOieS-2stCx49uJF-whdXk477GtO2SaqwItOVpPwuGQA0P7B7cbHLhO8dG4KuIvf2fLOjxkbogDZBeaqdYaTOSSS7hOty0FrYOSeTsdk238xux-yeNoVdxqgsqO0mr18ZaQq4qJPJRnDwoay9DdUzp2-vs26GTlbS_wuZ1It5hTyfI-n8EZ-kYunHw5MTtU__pOuwmHM0TbYZpJJmjlkpi23851zu_quqpzQTdfWNaDJ4l_p0yAuVgCH-lexCgoYmDWtdPQVcwxn3D3-MDzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این رسما دزدیه‌بخدا</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/82097" target="_blank">📅 23:03 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82096">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">رونالدو و جورجینا به قاطی مرغا
هیر وی گو
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/82096" target="_blank">📅 22:56 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82095">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YuCBDqUirVusdj4NpBNd9KUV4ngrf9jLCUNL-EpCxHgxV-S53vaP0Jy5raHgPlzhdN8cHeUqvNgA-VZSainduxX46-t3VZ2dYv_jsVIqEOzRh3_Kh7xC_62DIhzSE2W8KicQOqtLEvByEHjKVCO44WKC59sV0q9GawpPeaCtsQWlaQWu0OA6k20rDo7WD5sHKbmGS5AFM_tK0A8ODbapvv2IBUravYKZI0fBH5xsXr9faVXgVg127UzEypxtq5-dFfm3tgFPBvKlsT9-5klj4lD3GMnNygrukX0UNVP1B3w60D4HwwD1SMQBvHlGFrFWlKi1wC6TNru6o9uGB66dQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داود کیم، خواننده سابق کیپاپ از مسلمان شدن میگوید: صدای اذان در تمام خیابان های کره شنیده خواهد شد و گفت امیدوار است بتواند به ترویج اسلام در کره ادامه دهد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/82095" target="_blank">📅 22:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82094">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">آلبوم جدید خلسه به اسم " Margo Zendegi " منتشر شد.   SoundCloud   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/82094" target="_blank">📅 21:07 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82093">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">آلبوم جدید خلسه به اسم " Margo Zendegi " منتشر شد.   SoundCloud   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/82093" target="_blank">📅 21:02 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82092">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WtOXMReZKbOvhn1z2cLfFfP0j_ocQyGLKK_ROR8XX3H0vmlYGTAzFZFu3T3wY_26FlDfWvuQeM9cSn6pwN3hbB4JRs1hSKShmHwq_hwlkMJW9vnI80PSIbf0W7pltcMNZno-am1wIa8L0nR-4xDkgLLRzRKGEgL2Pag827xPdUzot9QqxLgcNCHo2Jmt9Q8SquhnFBxjtwNzCu1UWyCWapfFZHA3UbwCSIL6hL8Vh3v4A39zyDxsIeX4ZYlyWddPVyt4sfYn9GtKjDbxOTd9h9KfzhDxRTvOjVY2LZ_dDSZx6hO6HAAasKgVWjmgzVBH8G4LY0EHPoI5Aivi2dwHFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلبوم جدید خلسه به اسم "
Margo Zendegi
" منتشر شد.
SoundCloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/82092" target="_blank">📅 21:02 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82091">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c8dwgfFxRYXvmKHDDDp3pGp2KqTgukMphSwQJpxYZMCjxtkCyVzs7hlnQdHYyS0avXp4Zsz_KriX7IupeuiP7zs3BwsWxrfWXgE4SHjYtcXTEs9KRoflBcq7ohc0UeBgFdmUsieQRGYcrn1eu1AVPImxPQl8DUB5u9hVFIlxgnJKFv5Ze9NdrQrS5Sv7QVUpp9gI8h6Ax3kcUVYoPQ7G0IaTo1OXROKWd5-Kqe8FWKdCuuFp0uPdTaEDNF8nUv3crX4Zaivd_jDKuqUrTLQRFqIqIf3NkGLwK26Zw3BBi5fAUEsb0FjMYMG1tmbTlZwb_SmXgOppHOJt39etpHkbtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#ایده
#تتو
#مهدی
#پسرعمو
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/82091" target="_blank">📅 20:50 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82090">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QCrlsjsdB2Ck_je6vN88-yALDCEdU9V8orb5tZ30zAhUbJCBJUEspZ0CuEhpJDR19CilsbL9gXBc4dRStNbKzSrzHdflvc_xrRQAPakPB4OEhGeho5UcEsZcKdURjMjwtan2CuWDZLOP8WBHy18CtLu_Dm_IcoWXAPzc01MerPwv7pa6js3xN4rgtmD5UJI48YGGLl1N4oDgAcErR-cvprYJfIPrtpPbEEk6mnUH6qym_Du9edB0WRxH9eSfAlC4v_Endd9lBwDoeFRzxP5MZ7D4BXxcPeKiOn7f1BkxsLK9RDHCsiIMF8Eh-JD6F2j6gC4y2zmkiwZ6OGA3bfgU7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
علم‌الهدی : اونایی که داخل کشور میگن جنگ رو تموم کنید، یا بی‌عقل و مریضن یا منافق؛
فکر نکنید اگه جنگ تموم بشه آمریکا دست از سر ما برمی‌داره، حتی اگه همه‌چی رو هم بهش بدیم، باز راضی نمیشه و در نهایت وارد کشور می‌شه و حمله زمینی می‌کنه.
@FuunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/82090" target="_blank">📅 19:45 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82089">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ckfGl6BFo3lrAvvBrnhUEs7s75a7l4rStdBu3shuUkamkzxOo33YTarF6IMQnEGfeuPb5RT84gyZAC-R_CQ5Ndf__UEqwwlH6kJDQSe-UjJ4odt7XH2SsQWO-EquVSvT_h09vn-fhbYkHTTcpUfeZ7ei89fHR2GTlaW1ZDADCIWyI1oub5uLqIIfE3sRJmUCSZAulu3j2Ok83ArnmS2J9IVMciBwspKnbYTBqKyjKhfQyQnLJC8-bgbnraHg9lgXNfZaTwKfft7clx_PN7lqQ2bzBwzo7YSuJ_4yeRaO5BGZ1sAk2bLTFIhzJ_QYc2T7f6l55zPDFWSPzoLD5Uvqsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
دولت لبنان رسما مجازاتِ اعدام توی این کشور رو لغو کرد.
مجلس لبنان با اکثریت آرا به لغو مجازات اعدام رای داد و این مجازات رو با "حبس ابد + اعمال شاقه تشدید شده(احتمالا کارهای سخت و اجباری تو دوران حبس)" جایگزین کرد.
لبنان اولین کشور عرب تو خاورمیانه‌ست که مجازات اعدام رو به طور کامل حذف میکنه.
@FuunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/82089" target="_blank">📅 19:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82087">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">اوه اوه آریا یوسفی از جنوا و مایورکا پیشنهاد دریافت کرده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/82087" target="_blank">📅 18:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82086">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc87bc1a00.mp4?token=nKqbcbEDF0VsYzBJV-lwvLjqqsSdafYUbKQnwSf1p_qDGNDtX6Fg0_mBLQ-gDRJHeKMhU2oMQFLkB4bscLw0x0kWFP_zVbQd3DC3Nr5RvCu9oz2lCjqygRrhWyYzBbYaPDs5ovEDScZ-XAsuzDTQDqwyt9kyO_DX4VEIlO7jzDVNJmpk3c1h09LYyVg_nVCPVI_gSm3IaOD6QcXkGK8n1eTuxIo3v9ZZzHNMwSE-FcQshImpIhKfI2z-npUGrZma6nuHUxn2rDeajsbRAx7uzPPNlA8pfPP_UNM3R9iYXQ1tWG0SVFUAab7pUkRQZcCIZsmrihes0aJAWz7xsTSuDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc87bc1a00.mp4?token=nKqbcbEDF0VsYzBJV-lwvLjqqsSdafYUbKQnwSf1p_qDGNDtX6Fg0_mBLQ-gDRJHeKMhU2oMQFLkB4bscLw0x0kWFP_zVbQd3DC3Nr5RvCu9oz2lCjqygRrhWyYzBbYaPDs5ovEDScZ-XAsuzDTQDqwyt9kyO_DX4VEIlO7jzDVNJmpk3c1h09LYyVg_nVCPVI_gSm3IaOD6QcXkGK8n1eTuxIo3v9ZZzHNMwSE-FcQshImpIhKfI2z-npUGrZma6nuHUxn2rDeajsbRAx7uzPPNlA8pfPP_UNM3R9iYXQ1tWG0SVFUAab7pUkRQZcCIZsmrihes0aJAWz7xsTSuDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رامین رضاییان: طارمی بخاطر تیم جلو بلژیک  گل نزد که زیر فشار نریم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/82086" target="_blank">📅 18:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82085">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75d87d048c.mp4?token=poMcLXzXBfjio78OYcKXfKHTI_AV8SfLCkm2MDz7ekCibU6Zj4VFaPSpTJ5BVxWzhZhVkHfHZUA1HD38X6lNM3yRmOxzWgpmrhR5WkFbYxL2NQB4EsNIugktaIwTGmthWPRVuhA93g8ho6KvDol8X8iNE29s9yWdDz_vaIYorwR2S-63T6eIQKEeT9q0pnU8Kd3eWakBBDBZo7OEBjocgd75VC7SxTDYphz4C2KLVOTJjHK93epI_2jwKrSTbCW9yZ5GZD-DFXTdLUWbEwLkw5S6kJ432aRBOhRevbZNXT6Nh8_KpyxfOvrKFezZlwxGMga8rguJiLN7_rY-HbfUYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75d87d048c.mp4?token=poMcLXzXBfjio78OYcKXfKHTI_AV8SfLCkm2MDz7ekCibU6Zj4VFaPSpTJ5BVxWzhZhVkHfHZUA1HD38X6lNM3yRmOxzWgpmrhR5WkFbYxL2NQB4EsNIugktaIwTGmthWPRVuhA93g8ho6KvDol8X8iNE29s9yWdDz_vaIYorwR2S-63T6eIQKEeT9q0pnU8Kd3eWakBBDBZo7OEBjocgd75VC7SxTDYphz4C2KLVOTJjHK93epI_2jwKrSTbCW9yZ5GZD-DFXTdLUWbEwLkw5S6kJ432aRBOhRevbZNXT6Nh8_KpyxfOvrKFezZlwxGMga8rguJiLN7_rY-HbfUYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایران چقد عجیب شده، تو دیجی کالا مواد می‌فروشن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/82085" target="_blank">📅 17:38 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82084">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rN-RVV_NGaMU2kh5uvp89XzgqJSmO6OCc7WaRsJ5YyyK7fgxf9SX6wizHkuOyBsJb9DtCGKlFXRZN6UOyQ3zXi483-mAzDkPy6jD75k7WkW6-6Sm4TrJbb3S62pNB1mX8mEJsAaPswAeJP88PWQA0egNJHz_BTFk2aIM2DNVgFRoYORKYwAXJOQLnIDklPslPZydU13CqwaUjRA0JaM6RQRabHmLRFdokFYquqVhBh-SenLnEiPtd12VCPlw0BH-DCblreEL03mw_BBVAHGH-oT2Rt8ORC4JYKD0lTiF0WRyTBv8oG59GM-HF9QBjZaFDnOhfBOIR0jIkxaYReonGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دورچیو
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/82084" target="_blank">📅 17:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82083">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ترک جدید متین فتاحی و سجاد شاهی بنام دو سه سال ریلیز شد   YouTube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/82083" target="_blank">📅 17:07 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82082">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RFIM2mt-r4OY-ZHaoSG35drlNcTLcFBlWhmp4hdppsqD3JKopYRRoVUjzqLpU59U40UamwaNCBoSv4H50CdaSG7nnoMwMfRkRW79Ap3zCvTLrMF5x8-uP5ifni4tEplGbc_3GryueiDh6a-cbgLohW-NDovNaogJcZ65ztthvhelFzGaE79oqTtPA3aA2kuODPf4efHdBxkjSYJbMgt71ZyunpnPvVZcSr-kALDfNHdpAgMAYNgjzDhS9nul9jB02GGqPgFfp6KbzJS6xnNOElIquihVX56hCTCwX8gHY255vU59zFBFKMtGQXUcPAlyHilqwMEH-QfXnvvpzJjziQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید متین فتاحی و سجاد شاهی بنام دو سه سال ریلیز شد
YouTube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/82082" target="_blank">📅 17:06 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82080">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ترک جدید سجاد شاهی و متین فتاحی یکم دیگه منتشر میشه</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/82080" target="_blank">📅 16:17 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82079">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ترک جدید سجاد شاهی و متین فتاحی یکم دیگه منتشر میشه</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/82079" target="_blank">📅 16:14 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82078">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GA7K70QXVQhFBp7_mWlhbRFRu7JFfS4-HtiqNEKniMT5-jWF9P22nDGem21LaM1ivTDj3_o9euKlYYcS4g7UauvJP9J_xqSwf_HN1NpiUBuDvUgCYe0BBorYfvfpiUTYq7biNSHuYTl8JJpPzamLghgCSqOS0-kl3G3SyFhHwkx763jSf96GciOl_F__f-_XLoXAC3nfSQTYwUg0C6bLZnzfpSrKZ5dlyF_8wAcNyc2P95Hcxox7J5ZtjwkZBxMhoyyA3fNGG8uYURymTvkUjsRpVi8xN_SYU28asf-YF_tQZ9J81H1H0eChdgHYvrPMtGEs81rAaKDr34crSgN0TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیپ استیلر ۲۹ سالش شد  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/82078" target="_blank">📅 16:01 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82077">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">بوی خداحافظی از فوتبال میاد
مسی بعد فوت پدرش هیچ زمان بازگشت دقیقی به اینترمیامی اعلام نکرده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/82077" target="_blank">📅 15:43 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82076">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CA7hJTO1s0EclUGMHuo70ulNkJNAxmrkhr_2PIWxC4jH2Kn0_ycpZrxKq-lNeFHGgZiDnaOqEUCC3-h8n9oGSjYlC4BKyPqE9A_zK141IWyr5kgL9ig4TpvSqeOihqUy5PGe_2NWBsPZq158udVAd6r8Vw-CYoH1NbbB8H5KjxKW0QFf9QxyP89eBOJUBfnvgjdg5nu6Q6ZlnDNI6PGBqfBx7-5sdB2UUi1aRh_kvbvaJRpGxy3IJ_Yk5GY7ZGLbt3uxBoFnH7p_a3AuwPVJKal2fbH-lieovtAqS6RHb6F1vCO73c4-43JG7vhV4mdIJbJ5_dkIVhi80m-ngmQeQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنجشنبه میخواد بگه دکی بیا بدهیتو بده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/82076" target="_blank">📅 15:06 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82074">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OmOz7n8f7q5wVtK0yopGd-p3p1phJGMf1idA7TWOPzRREIhejzV-1_uTDfHQ3VTft2d9_E0baYkeNz4yY4cjcHYJ6pPFGeAzGUr_C3WWGOJ-QB0a92Gv9GHBk6O8iKnXPIAV7D9GBjkTJyRsNYWsw5aFkyHCTvRCJI-S3yVYx6txN8Ljp5Pq8Yv4vPbTgya7HasKGy2uzTF1mdIFfmRrV61IfTn0uQJnKgS4vXWvMN4Oc9EnCQ-bdKyKZf6lB8ncYqzxA2G3ivWyQ4dA02WUM-ZIqEj8W-pu3eRQJTbpfspeSoOVIVeX5BtKoLHMHbWPmGsmo0Hi445podbQoWJNIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UlIOVeUWFRBzVA4OmZVMyTDFb7so5Bbrooddwaib5T6Kc0xWVwK9lS5YbnD6UWz-5OoUJFEokEmKt0MXxHgR3SNDiOBe4IElxV2EPwa-ugUWdT9s6RejSO1evIAJE0z-_EscRAwe6uuWA0MqTVriiExG56nptW7iiSx5_PkN3n_uzkB4MTxm1XBAEOgcMKjxjXqNkYlWOCVVgvms5K6fKcYhyykAvHtYAaTjC0NsXYNhIqMgkYxWo5-eEwMVNnj68SJyuUU2F8mr-6lm2sGqw69Gw50XMESLbH29Tbkho7rRdEhQlXDO4lcfuVZopW6-qafT3fFEleSSKUimJuH5Kg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شیپ استیلر ۲۹ سالش شد  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/82074" target="_blank">📅 14:35 · 20 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
